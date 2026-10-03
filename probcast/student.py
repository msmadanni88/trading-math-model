"""Live generator ("student") and everything else the browser computes itself.

The full model stack (teacher) only runs in the cloud, every few minutes or
hours. To draw the next candles at the exact moment a minute closes, the
browser needs models it can evaluate by itself, from numbers the cloud
published BEFORE that minute started:

  W       linear copy of the full model for the next candle (size, range, quantiles)
  H       one linear head per candle 1..HORIZON, fitted on what the market really did
          (direction, body size, reach above / below)
  scale   per-candle size multipliers learned from the goal score
  cone    per-candle width of the range for the close
  trees   the reversal agents' tree models, evaluated node by node
  HX      direction head of the next candle that also reads the other venue (x_features)

docs/student.js is a line-by-line mirror of this file; tests/parity.mjs proves
both give the same numbers. The cloud's record is produced by these same
functions with the parameter version that was already published when that
minute started, so what the site showed live is what gets stored.
"""
import numpy as np

from .config import HORIZON, STUDENT_WIN, X_MIN, X_WIN

LAM = 0.97
FEATURES = ["bias", "z0", "z1", "z2", "m5", "m15", "m60", "lv", "rv5", "body", "wick_up", "wick_dn",
            "rng", "vr", "pos60", "min_sin", "min_cos", "top_hour", "top_quarter", "hr_sin", "hr_cos"]
OUTPUTS = ["logit_p", "l_abs", "l_hi", "l_lo", "b05", "b25", "b75", "b95"]
H_OUTPUTS = ["s_dir", "l_abs", "l_hi", "l_lo"]      # per candle 1..HORIZON
REV_EXTRA = ["gap_k", "gap_2k", "gap_4k", "gap_30", "d_k", "d_30", "reject", "dh1", "dh2", "r1", "r2", "range",
             "leg", "leg_2k", "cpos", "cbody", "age", "run", "prev_reject", "prev_gap"]
REV_FEATURES = FEATURES + REV_EXTRA
X_FEATURES = ["x_gap", "x_lead1", "x_lead3", "x_lead5"]      # the cross-venue agent's view (see x_features)
_FLIP = [1, 2, 3, 4, 5, 6, 9, 14]                   # compact features whose sign mirrors with the side
OFF = 0.01
OFF_H = 0.1
RIDGE_H = 30.0
_W = LAM ** np.arange(STUDENT_WIN)          # weight 1 for the newest return
RIDGE = 3.0
FORMAT = 2                                  # layout of a published version (see generate_path)


def _clip(x, a):
    return max(-a, min(a, x))


def compact(C, next_ts):
    """C: array (STUDENT_WIN + 1, 5) of the latest closed candles [o, h, l, c, v],
    oldest first. Returns (features, sigma)."""
    o, h, l, c, v = C[-1]
    cl = C[:, 3]
    r = np.log(cl[1:] / cl[:-1])                       # STUDENT_WIN returns, newest last
    r2 = r * r
    sig = max(float(np.sqrt(np.sum(_W * r2[::-1]) / np.sum(_W))), 1e-6)
    slong = max(float(np.sqrt(np.mean(r2))), 1e-6)
    rng_ = h - l
    hi60 = float(np.max(C[-60:, 1]))
    lo60 = float(np.min(C[-60:, 2]))
    minute = (next_ts // 60) % 60
    hour = (next_ts // 3600) % 24
    f = [1.0,
         _clip(r[-1] / sig, 6), _clip(r[-2] / sig, 6), _clip(r[-3] / sig, 6),
         _clip(float(np.sum(r[-5:])) / (sig * np.sqrt(5)), 6),
         _clip(float(np.sum(r[-15:])) / (sig * np.sqrt(15)), 6),
         _clip(float(np.sum(r[-60:])) / (sig * np.sqrt(60)), 6),
         _clip(float(np.log(sig / slong)), 3),
         _clip(float(np.log(np.sqrt(np.mean(r2[-5:])) / sig + 0.05)), 3),
         (c - o) / rng_ if rng_ > 0 else 0.0,
         (h - max(o, c)) / rng_ if rng_ > 0 else 0.0,
         (min(o, c) - l) / rng_ if rng_ > 0 else 0.0,
         _clip(float(np.log(np.log(h / l) / sig + 0.05)), 3),
         _clip(float(np.log((v + 1e-6) / (float(np.mean(C[-30:, 4])) + 1e-6))), 5),
         (c - lo60) / (hi60 - lo60 + 1e-12) - 0.5,
         float(np.sin(2 * np.pi * minute / 60)), float(np.cos(2 * np.pi * minute / 60)),
         1.0 if minute == 0 else 0.0, 1.0 if minute % 15 == 0 else 0.0,
         float(np.sin(2 * np.pi * hour / 24)), float(np.cos(2 * np.pi * hour / 24))]
    return np.array(f), sig


def teacher_targets(p_up, a, e_up, e_dn, q05, q25, q75, q95, sig):
    """a: median |body|; e_up / e_dn: reach above / below the last close."""
    p = min(max(p_up, 0.02), 0.98)
    return np.array([np.log(p / (1 - p)), np.log(a / sig + OFF), np.log(e_up / sig + OFF), np.log(e_dn / sig + OFF),
                     q05 / sig, q25 / sig, q75 / sig, q95 / sig])


def fit(X, Y, ridge=RIDGE):
    """Ridge regression (bias not penalised). Returns W with shape (outputs, features)."""
    reg = np.eye(X.shape[1]) * ridge
    reg[0, 0] = 0.0
    return np.linalg.solve(X.T @ X + reg, X.T @ Y).T


def outcome_targets(r, e_up, e_dn, sig):
    """Targets of the per-candle heads, taken from what the market actually
    printed (arrays). sig: volatility scale at the moment of the forecast."""
    q = lambda v: np.log(np.clip(v / sig, 0, 20) + OFF_H)
    return np.column_stack([np.sign(r), q(np.abs(r)), q(e_up), q(e_dn)])


def horizon_raw(Wh, f, sig):
    """Unscaled forecast of one candle from its head: (direction, |body|,
    reach up, reach down, P(up))."""
    y = Wh @ f
    p = min(max(0.5 + 0.5 * float(y[0]), 0.02), 0.98)
    size = lambda v: sig * max(float(np.exp(v)) - OFF_H, 0.0)
    return (1.0 if p >= 0.5 else -1.0, size(y[1]), size(y[2]), size(y[3]), p)


def _next_raw(W, f, sig):
    """The full model's view of the next candle, through its linear copy."""
    y = W @ f
    return {"p": float(1.0 / (1.0 + np.exp(-y[0]))),
            "a": sig * max(float(np.exp(y[1])) - OFF, 0.0),
            "e_up": sig * max(float(np.exp(y[2])) - OFF, 0.0), "e_dn": sig * max(float(np.exp(y[3])) - OFF, 0.0),
            "q05": float(sig * y[4]), "q25": float(sig * y[5]), "q75": float(sig * y[6]), "q95": float(sig * y[7])}


def generate(W, f, sig):
    """The next candle from the linear copy alone. Returns dict: p (P(up)),
    b (signed body), u, d (wicks beyond the body), q05..q95 - all as log-price
    offsets from the last close."""
    n = _next_raw(W, f, sig)
    b = n["a"] if n["p"] >= 0.5 else -n["a"]
    return {"p": n["p"], "b": float(b), "u": max(n["e_up"] - max(b, 0.0), 0.0), "d": max(n["e_dn"] - max(-b, 0.0), 0.0),
            "q05": n["q05"], "q25": n["q25"], "q75": n["q75"], "q95": n["q95"]}


def x_features(close, xclose, sig):
    """The cross-venue agent's view at a minute close.

    close, xclose: closes of this market and of the same asset on the other
    venue for the same minutes, oldest first, the last one being the candle
    that just closed (NaN where the other venue has no candle). With
    g = log(other venue / this market):

      x_gap     g now against its own median of the last X_WIN minutes: is the
                other venue richer or cheaper than usual right now
      x_lead_k  g now minus g k minutes ago (k = 1, 3, 5): how much further the
                other venue has moved than this market over those minutes

    all in units of this market's typical one-minute move. Returns None when
    the other venue has no candle for the minute that just closed, or too few
    in the window - the caller then falls back to the head without them."""
    c = np.asarray(close[-X_WIN:], float)
    x = np.asarray(xclose[-X_WIN:], float)
    if len(c) < X_WIN or len(x) < X_WIN or not sig > 0:
        return None
    ok = np.isfinite(x) & (x > 0)
    if not ok[-1] or int(ok.sum()) < X_MIN:
        return None
    g = np.where(ok, np.log(np.where(ok, x, 1.0) / c), np.nan)
    med = float(np.median(g[ok]))

    def back(k):                                # g as it was known k minutes ago (the latest candle up to then)
        i = len(g) - 1 - k
        while i >= 0 and not ok[i]:
            i -= 1
        return g[i] if i >= 0 else g[-1]
    out = [(g[-1] - med) / sig] + [(g[-1] - back(k)) / (sig * np.sqrt(k)) for k in (1, 3, 5)]
    return np.array([_clip(float(v), 8.0) for v in out])


def call_level(ver, p):
    """How far the model stands behind a colour call with P(up) = p:
    0 = close to a coin flip, 1 = confident, 2 = strong. `ct` holds the colour
    caller's published lines (agents/colour.py), ascending. Compared in
    millionths, so the site and the cloud cannot disagree over the last digit
    of a float."""
    ct = ver.get("ct")
    if not ct:
        return 0
    c = int(abs(p - 0.5) * 1e6 + 0.5)
    return sum(1 for t in ct if c >= int(t * 1e6 + 0.5))


def generate_path(ver, f, sig, x=None):
    """The next HORIZON candles, as one connected chain.

    Every candle h has
      colour   from its own direction head H[h-1], fitted on real outcomes;
               candle 1, when the other venue's view `x` is available and a
               head for it is published: from HX, which reads f and x
      size     candle 1: the full model's sizes; candles 2..: its own head
               times the multipliers the goal tuner learned for that candle
      o        where it opens = where the previous candle of the chain closed
      lo, hi   the 90% range for its CLOSE (`cone` times the range of candle 1)
    all as log-offsets from the last real close.

    One rule keeps the chain honest: it may never walk out of the model's own
    50% range for that minute. If the colour a head prefers would close the
    candle outside it (and the other colour would not be further out), the
    candle takes the other colour (`flip`). Without this rule, heads that all
    lean the same way draw a staircase the model itself does not believe.
    """
    n = _next_raw(ver["W"], f, sig)
    H = ver.get("H")
    if H is None or ver.get("fmt") != FORMAT:
        g = generate(ver["W"], f, sig)
        g.update(o=0.0, lo=g["q05"], hi=g["q95"], flip=0, call=0, x=0)
        return [g]
    HX = ver.get("HX")
    iq = 0.5 * (n["q75"] - n["q25"])
    path, o = [], 0.0
    for h in range(1, len(H) + 1):
        d, a, e_up, e_dn, p = horizon_raw(np.asarray(H[h - 1]), f, sig)
        used = 0
        if h == 1 and x is not None and HX is not None:
            p = min(max(0.5 + 0.5 * float(np.dot(np.asarray(HX), np.concatenate([f, x]))), 0.02), 0.98)
            d, used = (1.0 if p >= 0.5 else -1.0), 1
        raw = (d, a, e_up, e_dn)                      # what the head said, before any multiplier
        if h == 1:
            a, e_up, e_dn, cone = n["a"], n["e_up"], n["e_dn"], 1.0
        else:
            kb, kr = ver["scale"][h - 1]
            a, e_up, e_dn, cone = a * kb, e_up * kr, e_dn * kr, ver["cone"][h - 1]
        b = d * a
        w = max(cone * iq, a)
        flip = abs(o + b) > w and abs(o - b) < abs(o + b)
        if flip:
            b = -b
        g = {"p": p, "b": float(b), "u": max(e_up - max(b, 0.0), 0.0), "d": max(e_dn - max(-b, 0.0), 0.0),
             "o": float(o), "lo": cone * n["q05"], "hi": cone * n["q95"], "flip": int(flip), "raw": raw}
        if h == 1:
            g.update(q05=n["q05"], q25=n["q25"], q75=n["q75"], q95=n["q95"], call=call_level(ver, p), x=used)
        path.append(g)
        o += b
    return path


# ---------------------------------------------------------------- reversal agents
def rev_features(C, f, sig, side, K):
    """What a reversal agent of swing size K looks at after a candle closes.
    side = +1 for a top (swing high), -1 for a bottom (swing low). A bottom is
    a top of the mirrored price, so one model serves both sides: every price
    below is taken in mirrored form (high -> -low, close -> -close ...).
    C: latest closed candles [o, h, l, c, v] (oldest first, at least 4K + 2 and
    32 of them); f, sig: compact(). Distances are in units of the current
    one-minute volatility."""
    m = [float(x) for x in f]
    for i in _FLIP:
        m[i] = side * m[i]
    if side < 0:
        m[10], m[11] = m[11], m[10]
    n = max(4 * K, 30) + 2
    W = [list(map(float, r)) for r in C[-n:]]
    if side > 0:
        Hh, Ll = [r[1] for r in W], [r[2] for r in W]
        Cc, Oo = [r[3] for r in W], [r[0] for r in W]
    else:
        Hh, Ll = [-r[2] for r in W], [-r[1] for r in W]
        Cc, Oo = [-r[3] for r in W], [-r[0] for r in W]
    sg = sig * W[-1][3]
    rng = W[-1][1] - W[-1][2]
    top = lambda w: max(Hh[-w:])
    age = 0
    best = max(Hh[-(2 * K + 1):])
    while Hh[-1 - age] != best:                  # candles since the high of the last 2K + 1
        age += 1
    run = 0
    while run < 5 and Cc[-1 - run] > Cc[-2 - run]:
        run += 1
    x = [(top(K) - Hh[-1]) / sg, (top(2 * K) - Hh[-1]) / sg, (top(4 * K) - Hh[-1]) / sg, (top(30) - Hh[-1]) / sg,
         (top(K) - Cc[-1]) / sg, (top(30) - Cc[-1]) / sg, (Hh[-1] - Cc[-1]) / sg,
         (Hh[-1] - Hh[-2]) / sg, (Hh[-2] - Hh[-3]) / sg, (Cc[-1] - Cc[-2]) / sg, (Cc[-2] - Cc[-3]) / sg, rng / sg,
         (Cc[-1] - min(Ll[-10:])) / sg, (Cc[-1] - min(Ll[-2 * K:])) / sg,
         (Hh[-1] - Cc[-1]) / rng if rng > 0 else 0.5, (Cc[-1] - Oo[-1]) / rng if rng > 0 else 0.0,
         age / (2.0 * K), run / 5.0,
         (Hh[-2] - Cc[-2]) / sg, (max(Hh[-K - 1:-1]) - Hh[-2]) / sg]
    return np.array(m + [_clip(v, 20.0) for v in x])


def pack_trees(dump):
    """LightGBM's dump_model() -> flat arrays the browser can walk. Numbers
    are rounded to keep the file small: the packed model IS the published
    model, and every implementation walks exactly these numbers.
    f / t: split feature and threshold of every internal node; l / r: child
    (>= 0: internal node, < 0: leaf number -(x) - 1); v: leaf values; roots:
    first node of every tree."""
    F, T, L, R, V, roots = [], [], [], [], [], []

    def walk(nd):
        if "leaf_value" in nd:
            V.append(float(f"{nd['leaf_value']:.5g}"))
            return -len(V)
        if nd["decision_type"] != "<=":
            raise ValueError("only numerical splits are supported")
        i = len(F)
        F.append(int(nd["split_feature"]))
        T.append(float(f"{nd['threshold']:.7g}"))
        L.append(0)
        R.append(0)
        L[i] = walk(nd["left_child"])
        R[i] = walk(nd["right_child"])
        return i

    for t in dump["tree_info"]:
        roots.append(walk(t["tree_structure"]))
    return {"nf": int(dump["max_feature_idx"]) + 1, "f": F, "t": T, "l": L, "r": R, "v": V, "roots": roots}


def _arrays(model):
    a = model.get("_np")
    if a is None:
        a = model["_np"] = tuple(np.asarray(model[k], dtype=d) for k, d in
                                 (("f", np.int64), ("t", float), ("l", np.int64), ("r", np.int64), ("v", float), ("roots", np.int64)))
    return a


def tree_probs(model, X):
    """Probability from a packed tree model for every row of X (rows x features).
    Features are rounded to single precision first - the precision the trees
    were trained in - so every implementation takes the same branches."""
    F, T, L, R, V, roots = _arrays(model)
    X = np.asarray(X, dtype=np.float32).astype(float)
    node = np.tile(roots, (len(X), 1))
    rows = np.broadcast_to(np.arange(len(X))[:, None], node.shape)
    act = node >= 0
    while act.any():
        nd = node[act]
        node[act] = np.where(X[rows[act], F[nd]] <= T[nd], L[nd], R[nd])
        act = node >= 0
    raw = np.cumsum(V[-node - 1], axis=1)[:, -1]         # summed tree by tree, in order
    return 1.0 / (1.0 + np.exp(-raw))


def rev_rows(phi_top, phi_bottom, horizons):
    """Model input for both sides and every call type: [top x horizons, bottom x horizons]."""
    return np.array([list(phi) + [float(j)] for phi in (phi_top, phi_bottom) for j in horizons])
