"""Live generator ("student").

The full model stack (teacher) only runs in the cloud, every few minutes. To
draw the next candle at the exact moment a minute closes, the browser needs a
model it can evaluate by itself. The student is that model: a small linear map
from compact, cheap features to the teacher's outputs (knowledge distillation),
refitted on every cloud run and published as plain numbers.

docs/student.js is a line-by-line mirror of this file; tests/parity.mjs proves
both give the same numbers. The official record of generated candles is
produced by the same function with the parameter version that was already
published when that minute started, so what the site showed live is exactly
what is stored.
"""
import numpy as np

from .config import HORIZON, REV_K, STUDENT_WIN

LAM = 0.97
FEATURES = ["bias", "z0", "z1", "z2", "m5", "m15", "m60", "lv", "rv5", "body", "wick_up", "wick_dn",
            "rng", "vr", "pos60", "min_sin", "min_cos", "top_hour", "top_quarter", "hr_sin", "hr_cos"]
OUTPUTS = ["logit_p", "l_abs", "l_hi", "l_lo", "b05", "b25", "b75", "b95"]
H_OUTPUTS = ["s_dir", "l_abs", "l_hi", "l_lo"]      # per extra horizon (candles 2..HORIZON)
REV_FEATURES = FEATURES + ["d_k", "d_2k", "d_30", "is_new", "age", "run", "reject", "leg"]
_FLIP = [1, 2, 3, 4, 5, 6, 9, 14]                   # features whose sign mirrors with the side
OFF = 0.01
OFF_H = 0.1
RIDGE_H = 30.0
_W = LAM ** np.arange(STUDENT_WIN)          # weight 1 for the newest return
RIDGE = 3.0


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
    """Targets for the candles further ahead, taken from what the market
    actually printed (arrays). sig: volatility scale at the moment of forecast."""
    q = lambda v: np.log(np.clip(v / sig, 0, 20) + OFF_H)
    return np.column_stack([np.sign(r), q(np.abs(r)), q(e_up), q(e_dn)])


def horizon_raw(Wh, f, sig):
    """Unscaled forecast of one further-ahead candle: (direction, |body|,
    reach up, reach down, P(up))."""
    y = Wh @ f
    p = min(max(0.5 + 0.5 * float(y[0]), 0.02), 0.98)
    size = lambda v: sig * max(float(np.exp(v)) - OFF_H, 0.0)
    return (1.0 if p >= 0.5 else -1.0, size(y[1]), size(y[2]), size(y[3]), p)


def generate(W, f, sig):
    """Returns dict: p (P(up)), b (signed body), u, d (wicks beyond the body),
    q05..q95 - all as log-price offsets from the last close."""
    y = W @ f
    p = 1.0 / (1.0 + np.exp(-y[0]))
    a = sig * max(float(np.exp(y[1])) - OFF, 0.0)
    b = a if p >= 0.5 else -a
    e_up = sig * max(float(np.exp(y[2])) - OFF, 0.0)
    e_dn = sig * max(float(np.exp(y[3])) - OFF, 0.0)
    return {"p": float(p), "b": float(b),
            "u": max(e_up - max(b, 0.0), 0.0), "d": max(e_dn - max(-b, 0.0), 0.0),
            "q05": float(sig * y[4]), "q25": float(sig * y[5]), "q75": float(sig * y[6]), "q95": float(sig * y[7])}


def generate_path(ver, f, sig):
    """The next HORIZON candles. Candle 1 is the distilled full model; candles
    2.. come from heads fitted on real outcomes, sized by multipliers the goal
    tuner learned for that horizon. `o` is where each candle opens and `lo` /
    `hi` bound its CLOSE (90% cone) - all as log-offsets from the last real close."""
    g = generate(ver["W"], f, sig)
    g["o"], g["lo"], g["hi"] = 0.0, g["q05"], g["q95"]
    path = [g]
    if ver.get("H") is None:
        return path
    o = g["b"]
    for j, Wh in enumerate(ver["H"]):
        d, a, e_up, e_dn, p = horizon_raw(np.asarray(Wh), f, sig)
        kb, kr = ver["scale"][j]
        b = d * a * kb
        c = ver["cone"][j]
        path.append({"p": p, "b": float(b), "u": max(kr * e_up - max(b, 0.0), 0.0),
                     "d": max(kr * e_dn - max(-b, 0.0), 0.0), "o": float(o), "lo": c * g["q05"], "hi": c * g["q95"]})
        o += b
    return path


# ---------------------------------------------------------------- reversal agent
def rev_features(C, f, sig, side):
    """Features for "will a swing point form in the next candles".
    side = +1 for a top (swing high), -1 for a bottom (swing low). A bottom is
    a top of the mirrored price, so one model serves both sides.
    C: latest closed candles [o, h, l, c, v] (oldest first); f, sig: compact()."""
    m = [float(x) for x in f]
    for i in _FLIP:
        m[i] = side * m[i]
    if side < 0:
        m[10], m[11] = m[11], m[10]
    c = C[-1][3]
    hi, lo = [r[1] for r in C[-31:]], [r[2] for r in C[-31:]]
    if side > 0:
        ext = hi
        dist = lambda n: float(np.log(max(ext[-n:]) / c)) / sig
        reject = float(np.log(hi[-1] / c)) / sig
        leg = float(np.log(c / min(lo[-10:]))) / sig
        is_new = 1.0 if hi[-1] >= max(hi[-REV_K - 1:-1]) else 0.0
        best = max(ext[-10:])
    else:
        ext = lo
        dist = lambda n: float(np.log(c / min(ext[-n:]))) / sig
        reject = float(np.log(c / lo[-1])) / sig
        leg = float(np.log(max(hi[-10:]) / c)) / sig
        is_new = 1.0 if lo[-1] <= min(lo[-REV_K - 1:-1]) else 0.0
        best = min(ext[-10:])
    age = 0
    while ext[-1 - age] != best:                 # candles since the extreme of the last 10
        age += 1
    run = 0
    while run < 5 and side * (C[-1 - run][3] - C[-2 - run][3]) > 0:
        run += 1
    cl = lambda x, a: min(max(x, 0.0), a)
    return np.array(m + [cl(dist(REV_K), 8), cl(dist(2 * REV_K), 8), cl(dist(30), 8), is_new, age / 10.0,
                         run / 5.0, cl(reject, 8), cl(leg, 12)])


def rev_probs(R, phi):
    """R: (horizons, features). Probability that the candle j steps ahead is a swing point."""
    z = np.clip(np.asarray(R) @ phi, -30, 30)
    return 1.0 / (1.0 + np.exp(-z))
