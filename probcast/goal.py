"""The goal, as a number.

GOAL: generate the next candle so that it matches the real one - colour,
direction, body size, wicks. `candle_score` measures exactly that overlap:

  body IoU   overlap / union of the generated and the real candle BODY
             (zero whenever the colour is wrong)
  range IoU  overlap / union of the generated and the real HIGH-LOW range
  score      0.5 * body IoU + 0.5 * range IoU      (1.0 = identical candle)

All inputs are log-price offsets from the previous close, which is where the
generated candle opens.
"""
import numpy as np


def _iou(lo1, hi1, lo2, hi2):
    inter = np.maximum(0.0, np.minimum(hi1, hi2) - np.maximum(lo1, lo2))
    union = np.maximum(hi1, hi2) - np.minimum(lo1, lo2)
    return np.where(union > 0, inter / np.where(union > 0, union, 1.0), 1.0)


def candle_score(gb, gu, gd, ao, ac, ah, al):
    """gb: generated signed body; gu, gd: generated wicks (>= 0).
    ao, ac, ah, al: real open / close / high / low offsets. Arrays or scalars.
    Returns (body_iou, range_iou, score)."""
    gb, gu, gd, ao, ac, ah, al = (np.asarray(x, float) for x in (gb, gu, gd, ao, ac, ah, al))
    g_lo, g_hi = np.minimum(0.0, gb), np.maximum(0.0, gb)
    a_lo, a_hi = np.minimum(ao, ac), np.maximum(ao, ac)
    body = _iou(g_lo, g_hi, a_lo, a_hi)
    rng = _iou(g_lo - gd, g_hi + gu, al, ah)
    return body, rng, 0.5 * body + 0.5 * rng


def summarize(d, prefix):
    """d: DataFrame with <prefix>_b/_u/_d and y, ao, ah, al. Mean scores."""
    ok = d[f"{prefix}_b"].notna()
    if ok.sum() < 30:
        return None
    x = d[ok]
    body, rng, sc = candle_score(x[f"{prefix}_b"], x[f"{prefix}_u"], x[f"{prefix}_d"], x["ao"], x["y"], x["ah"], x["al"])
    y = x["y"].to_numpy()
    nz = y != 0
    gsize = np.abs(x[f"{prefix}_b"].to_numpy())
    return {"n": int(len(x)), "score": float(sc.mean()), "body_iou": float(body.mean()), "range_iou": float(rng.mean()),
            "dir_acc": float(np.mean((x[f"{prefix}_b"].to_numpy()[nz] > 0) == (y[nz] > 0))) if nz.sum() else None,
            "body_size_ratio": float(np.median(gsize) / max(np.median(np.abs(y)), 1e-12)),
            "range_size_ratio": float(np.median(gsize + x[f"{prefix}_u"] + x[f"{prefix}_d"]) /
                                      max(np.median(x["ah"] - x["al"]), 1e-12))}


def baselines(d):
    """Reference generators any model must beat:
    repeat  - the next candle is a copy of the last one
    typical - colour of the last candle, sizes = medians of the last 60 candles"""
    ao, ac, ah, al = (d[k].to_numpy() for k in ("ao", "y", "ah", "al"))
    up = ah - np.maximum(0.0, ac)
    dn = np.minimum(0.0, ac) - al
    up, dn = np.maximum(up, 0), np.maximum(dn, 0)
    out = {}
    b1 = candle_score(ac[:-1], up[:-1], dn[:-1], ao[1:], ac[1:], ah[1:], al[1:])
    out["repeat"] = {"score": float(b1[2].mean()), "body_iou": float(b1[0].mean()), "range_iou": float(b1[1].mean())}
    import pandas as pd
    s = pd.DataFrame({"a": np.abs(ac), "u": up, "d": dn}).rolling(60).median().shift(1)
    sign = np.sign(np.r_[0.0, ac[:-1]])
    ok = s["a"].notna().to_numpy()
    if ok.sum() < 30:
        out["typical"] = dict(out["repeat"])
        return out
    b2 = candle_score((sign * s["a"].to_numpy())[ok], s["u"].to_numpy()[ok], s["d"].to_numpy()[ok],
                      ao[ok], ac[ok], ah[ok], al[ok])
    out["typical"] = {"score": float(b2[2].mean()), "body_iou": float(b2[0].mean()), "range_iou": float(b2[1].mean())}
    return out
