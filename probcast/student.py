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

from .config import STUDENT_WIN

LAM = 0.97
FEATURES = ["bias", "z0", "z1", "z2", "m5", "m15", "m60", "lv", "rv5", "body", "wick_up", "wick_dn",
            "rng", "vr", "pos60", "min_sin", "min_cos", "top_hour", "top_quarter", "hr_sin", "hr_cos"]
OUTPUTS = ["logit_p", "l_abs", "l_hi", "l_lo", "b05", "b25", "b75", "b95"]
OFF = 0.01
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


def fit(X, Y):
    """Ridge regression (bias not penalised). Returns W with shape (outputs, features)."""
    reg = np.eye(X.shape[1]) * RIDGE
    reg[0, 0] = 0.0
    return np.linalg.solve(X.T @ X + reg, X.T @ Y).T


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
