"""Causal candle features (the "full" feature set used by the cloud models).

Every feature at row t uses candles <= t only and a FINITE look-back window, so
computing on the full history or on a short tail gives identical values (this
is what the tests check, and it is the guard against look-ahead).
"""
import numpy as np
import pandas as pd

from .config import BUF, GRAN, W_LONG, W_MID, W_SHORT

FD_D = 0.4           # fractional differentiation order
FD_K = 240           # truncated weight window
EPS = 1e-12


def regularize(rows):
    """rows: list of [ts, o, h, l, c, v] -> DataFrame on a gap-free time grid.
    Missing candles (no trades / exchange outage) become flat zero-volume bars
    and are flagged in `filled`."""
    df = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume"])
    df = df.drop_duplicates("ts").sort_values("ts").set_index("ts")
    full = np.arange(df.index[0], df.index[-1] + GRAN, GRAN)
    out = df.reindex(full)
    out["filled"] = out["close"].isna().astype(np.int8)
    out["close"] = out["close"].ffill()
    for c in ("open", "high", "low"):
        out[c] = out[c].fillna(out["close"])
    out["volume"] = out["volume"].fillna(0.0)
    out.index.name = "ts"
    return out.reset_index()


def _fd_weights(d=FD_D, k=FD_K):
    w = [1.0]
    for i in range(1, k):
        w.append(-w[-1] * (d - i + 1) / i)
    return np.array(w[::-1])            # oldest ... newest


def _levy_area(a, b, win):
    """Rolling Levy area (level-2 path-signature antisymmetric term) of the
    2-D path whose increments are (a, b), over `win` steps:
        A = 1/2 * sum_{i<j} (a_i b_j - a_j b_i)
    Computed in O(n) from rolling sums."""
    a = pd.Series(a)
    b = pd.Series(b)
    ca = a.cumsum()
    cb = b.cumsum()
    ca_prev = ca.shift(1).fillna(0.0)
    cb_prev = cb.shift(1).fillna(0.0)
    s_ab = (ca_prev * b).rolling(win).sum()
    s_ba = (cb_prev * a).rolling(win).sum()
    a0 = ca.shift(win).fillna(0.0)      # cumulative sum just before the window
    b0 = cb.shift(win).fillna(0.0)
    sb = b.rolling(win).sum()
    sa = a.rolling(win).sum()
    area = 0.5 * ((s_ab - a0 * sb) - (s_ba - b0 * sa))
    return area.to_numpy()


def compute_features(df):
    """df: output of regularize() (any contiguous slice). Returns DataFrame of
    features aligned with df rows. Rows inside the warm-up contain NaN."""
    o = df["open"].to_numpy(float)
    h = df["high"].to_numpy(float)
    l = df["low"].to_numpy(float)
    c = df["close"].to_numpy(float)
    v = df["volume"].to_numpy(float)
    ts = df["ts"].to_numpy(np.int64)
    lc = np.log(c)
    r = pd.Series(np.diff(lc, prepend=np.nan))
    S, M, Lg = W_SHORT, W_MID, W_LONG
    F = {}

    # --- volatility scales -------------------------------------------------
    vol_s, vol_m, vol_l = r.rolling(S).std(), r.rolling(M).std(), r.rolling(Lg).std()
    s = vol_l + EPS                      # slow scale used to normalise
    F["lvol_s_m"] = np.log((vol_s + EPS) / (vol_m + EPS))
    F["lvol_m_l"] = np.log((vol_m + EPS) / s)

    # range-based variance estimators (far less noisy than r^2)
    hl = np.log(h / l)
    co = np.log(c / o)
    gk = pd.Series(0.5 * hl ** 2 - (2 * np.log(2) - 1) * co ** 2).clip(lower=0)
    pk = pd.Series(hl ** 2 / (4 * np.log(2)))
    gk_s, gk_m, gk_l = gk.rolling(S // 2).mean(), gk.rolling(M // 2).mean(), gk.rolling(Lg).mean()
    fl = 0.05 * gk_l + 1e-14
    F["lgk_1_m"] = 0.5 * np.log((gk + fl) / (gk_m + fl))
    F["lgk_s_m"] = 0.5 * np.log((gk_s + fl) / (gk_m + fl))
    F["lgk_m_l"] = 0.5 * np.log((gk_m + fl) / (gk_l + fl))
    F["lpk_gk_m"] = 0.5 * np.log((pk.rolling(M // 2).mean() + fl) / (gk_m + fl))
    r2m = (r ** 2).rolling(M // 2).mean() + 1e-14
    oc = pd.Series(np.log(o / np.roll(c, 1)))
    oc.iloc[0] = np.nan
    F["gap_share"] = ((oc ** 2).rolling(M // 2).mean() / r2m).clip(0, 5)
    F["down_share"] = (r.clip(upper=0) ** 2).rolling(M // 2).mean() / r2m

    # --- returns / momentum (scale free) -----------------------------------
    z = (r / s).clip(-12, 12)
    for k in (0, 1, 2):
        F[f"z_lag{k}"] = z.shift(k)
    for k in (3, 5, 15, 30, 60, 240):
        F[f"mom_{k}"] = (r.rolling(k).sum() / (s * np.sqrt(k))).clip(-12, 12)
    F["abs_z"] = z.abs()
    F["ac1"] = r.rolling(120).corr(r.shift(1))
    F["skew"] = r.rolling(240).skew().clip(-10, 10)

    # --- candle shape -------------------------------------------------------
    rng = (h - l)
    safe = np.where(rng > 0, rng, np.nan)
    F["body"] = pd.Series((c - o) / safe).fillna(0.0)
    F["wick_up"] = pd.Series((h - np.maximum(o, c)) / safe).fillna(0.0)
    F["wick_dn"] = pd.Series((np.minimum(o, c) - l) / safe).fillna(0.0)
    for k in (M, Lg):
        hh = pd.Series(h).rolling(k).max()
        ll = pd.Series(l).rolling(k).min()
        F[f"pos_{k}"] = (pd.Series(c) - ll) / (hh - ll + EPS) - 0.5

    # --- volume -------------------------------------------------------------
    vs = pd.Series(v)
    v_m, v_l = vs.rolling(M // 2).mean(), vs.rolling(Lg).mean()
    F["lv_1_m"] = np.log((vs + 1e-6) / (v_m + 1e-6)).clip(-6, 6)
    F["lv_m_l"] = np.log((v_m + 1e-6) / (v_l + 1e-6)).clip(-6, 6)
    sv = pd.Series(np.sign(r.fillna(0.0).to_numpy()) * v)
    F["signed_v"] = sv.rolling(M // 2).sum() / (vs.rolling(M // 2).sum() + 1e-6)

    # --- fractional differentiation of log price ----------------------------
    w = _fd_weights()
    fd = np.full(len(lc), np.nan)
    if len(lc) >= FD_K:
        win = np.lib.stride_tricks.sliding_window_view(lc, FD_K)
        # weights applied to (past log price - current log price): removes the
        # price level, leaving a stationary long-memory momentum measure
        fd[FD_K - 1:] = (win - win[:, -1:]) @ w
    F["fracdiff"] = (pd.Series(fd) / (s * np.sqrt(M // 2))).clip(-12, 12)

    # --- path signature (level 2, Levy areas) -------------------------------
    zr = z.fillna(0.0).to_numpy()
    one = np.ones(len(zr))
    vshare = (vs / (v_m * (M // 2) + 1e-6)).fillna(0.0).to_numpy()
    for k in (M // 2, 2 * M):
        F[f"sig_tp_{k}"] = _levy_area(one, zr, k) / k ** 1.5      # time x price
        F[f"sig_pv_{k}"] = _levy_area(zr, vshare, k) / np.sqrt(k)  # price x volume

    # --- calendar (of the NEXT candle, the one being forecast) --------------
    nxt = ts + GRAN
    minute = (nxt // 60) % 60
    hour = (nxt // 3600) % 24
    dow = (nxt // 86400 + 4) % 7
    F["min_sin"] = np.sin(2 * np.pi * minute / 60)
    F["min_cos"] = np.cos(2 * np.pi * minute / 60)
    F["top_hour"] = (minute == 0).astype(float)
    F["top_quarter"] = (minute % 15 == 0).astype(float)
    F["hr_sin"] = np.sin(2 * np.pi * hour / 24)
    F["hr_cos"] = np.cos(2 * np.pi * hour / 24)
    F["dow_sin"] = np.sin(2 * np.pi * dow / 7)
    F["dow_cos"] = np.cos(2 * np.pi * dow / 7)

    out = pd.DataFrame({k: np.asarray(val, dtype=float) for k, val in F.items()})
    out = out.replace([np.inf, -np.inf], np.nan)
    out["_gk"] = gk.to_numpy()           # raw (not model-input) column the engine needs
    out.index = df.index
    return out


_NAMES = None


def feature_names():
    global _NAMES
    if _NAMES is None:
        n = BUF
        rng = np.random.default_rng(0)
        c = 100 * np.exp(np.cumsum(rng.normal(0, 0.001, n)))
        d = pd.DataFrame({"ts": np.arange(n) * GRAN, "open": c, "high": c * 1.001, "low": c * 0.999,
                          "close": c, "volume": np.ones(n)})
        _NAMES = [x for x in compute_features(d).columns if not x.startswith("_")]
    return _NAMES
