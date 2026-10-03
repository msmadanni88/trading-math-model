"""Evaluation of the stored forecasts and everything the site and the weekly
review read: reports/latest.md|json, live/latest.json, live/params.json."""
import json
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import goal, store, student
from .config import GRAN, HORIZON, PRODUCT, REV_H, REV_K
from .core import QUANTILES

TAUS = [f"{int(round(t * 100)):02d}" for t in QUANTILES]
WINDOWS = {"1h": 60, "6h": 360, "24h": 1440, "7d": 10080, "30d": 43200}


def _iso(ts):
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _r(x, k=4):
    return None if x is None or not np.isfinite(x) else round(float(x), k)


def add_locked(fc):
    """The locked candle of minute M is the 5th candle of the path generated
    five minutes earlier. Adds where it opens (`lk_o`, log-offset from the
    close it was made from) and how far the real market had moved by then
    (`lk_real`), so both can be compared in absolute price."""
    fc = fc.copy()
    step = fc["ts"].diff()
    contiguous = (step.rolling(HORIZON - 1).max() == GRAN)
    chain = sum(fc["g_b" if j == 1 else f"g{j}_b"].shift(HORIZON - j) for j in range(1, HORIZON))
    o = fc["g5_o"] if "g5_o" in fc else pd.Series(np.nan, index=fc.index)
    fc["lk_o"] = o.where(o.notna(), chain.where(contiguous))
    fc["lk_real"] = fc["y"].shift(1).rolling(HORIZON - 1).sum().where(contiguous)
    return fc


def locked_score(d):
    """Match of the locked candles with the real ones, both placed at their
    actual price level (so being in the wrong place counts)."""
    x = d[d["lk_o"].notna() & d["lk_real"].notna() & d["g5_b"].notna()]
    if len(x) < 30:
        return None
    sh = x["lk_real"] - x["lk_o"]
    body, rng, sc = goal.candle_score(x["g5_b"], x["g5_u"], x["g5_d"], x["ao"] + sh, x["y"] + sh, x["ah"] + sh, x["al"] + sh)
    return {"n": int(len(x)), "score": float(sc.mean()), "body_iou": float(body.mean()), "range_iou": float(rng.mean()),
            "median_miss_bp": float(np.median(np.abs(x["lk_real"] + x["y"] - x["lk_o"] - x["g5_b"])) * 1e4)}


def swing_table(candles):
    """Swing highs / lows of order REV_K in the real candles, plus what two
    naive callers would have scored (for the reversal agent to beat)."""
    h, l = candles["high"], candles["low"]
    w = 2 * REV_K + 1
    top = (h >= h.rolling(w, center=True).max()).astype(float).where(h.rolling(w, center=True).max().notna())
    bot = (l <= l.rolling(w, center=True).min()).astype(float).where(l.rolling(w, center=True).min().notna())
    out = pd.DataFrame({"ts": candles["ts"], "top": top, "bot": bot})
    for k in ("top", "bot"):                      # a swing point within one candle of this minute
        out[k + "3"] = out[k].rolling(3, center=True).max()
    # naive caller: "a candle that makes a fresh K-candle high is the top" (and mirrored)
    out["new_hi"] = h >= h.shift(1).rolling(REV_K).max()
    out["new_lo"] = l <= l.shift(1).rolling(REV_K).min()
    return out


def reversal_metrics(calls, sw, since_ts):
    c = calls[(calls["for_ts"] >= since_ts) & calls["hit"].notna()]
    s = sw[(sw["ts"] >= since_ts) & sw["top3"].notna()]
    if len(c) < 5 or len(s) < 30:
        return {"n": int(len(c))}
    naive_hits = pd.concat([s.loc[s["new_hi"] == True, "top3"], s.loc[s["new_lo"] == True, "bot3"]])
    chance = float(pd.concat([s["top3"], s["bot3"]]).mean())
    return {"n": int(len(c)), "hit_rate": float(c["hit"].mean()), "chance": chance,
            "naive_rule": float(naive_hits.mean()) if len(naive_hits) else None,
            "naive_calls": int(len(naive_hits)), "lift": float(c["hit"].mean() / chance) if chance > 0 else None,
            "tops": int((c["side"] > 0).sum()), "bottoms": int((c["side"] < 0).sum())}


def window_metrics(d, agents):
    d = d[d["cal_50"].notna()]
    n = len(d)
    if n < 30:
        return {"n": int(n)}
    y = d["y"].to_numpy()
    m = {"n": int(n)}
    # --- the goal: how close are the generated candles ---------------------
    m["student"] = goal.summarize(d, "g")           # what the site shows
    m["teacher"] = goal.summarize(d, "t")           # full cloud model
    m["baseline"] = goal.baselines(d)
    # candles generated 2..HORIZON minutes ahead (1 = the row above)
    m["ahead"] = {"1": {"score": m["student"]["score"], "dir_acc": m["student"]["dir_acc"]}} if m["student"] else {}
    for hz in range(2, HORIZON + 1):
        if f"g{hz}_b" not in d:
            continue
        sm = goal.summarize(d, f"g{hz}")
        if sm:
            inside = d[f"c{hz}_in"].dropna()
            m["ahead"][str(hz)] = {"score": sm["score"], "dir_acc": sm["dir_acc"],
                                   "cone90": float(inside.mean()) if len(inside) else None}
    m["locked"] = locked_score(d) if "lk_o" in d else None
    # --- probability quality -------------------------------------------------
    m["loss_cal"] = float(d["loss_cal"].mean())
    m["loss_raw"] = float(d["loss_ens"].mean())
    m["agents"] = {}
    for e in agents:
        col = d[f"loss_{e}"]
        ok = col.notna()
        if ok.sum() >= 30:
            m["agents"][e] = float(col[ok].mean())
    if "empirical" in m["agents"]:
        ok = d["loss_empirical"].notna()
        m["skill_vs_empirical"] = float(1 - d.loc[ok, "loss_cal"].mean() / d.loc[ok, "loss_empirical"].mean())
    m["cov90"] = float(((y >= d["cal_05"]) & (y <= d["cal_95"])).mean())
    m["cov50"] = float(((y >= d["cal_25"]) & (y <= d["cal_75"])).mean())
    g = d[d["g_05"].notna()]
    if len(g) >= 30:
        yg = g["y"].to_numpy()
        m["cov90_site"] = float(((yg >= g["g_05"]) & (yg <= g["g_95"])).mean())
        m["cov50_site"] = float(((yg >= g["g_25"]) & (yg <= g["g_75"])).mean())
    nz = y != 0
    up = (y > 0).astype(float)
    p = d["p_up"].to_numpy()
    if nz.sum() >= 30:
        m["brier"] = float(np.mean((p[nz] - up[nz]) ** 2))
        m["dir_acc_teacher"] = float(np.mean((p[nz] > 0.5) == (up[nz] > 0.5)))
    width = (d["cal_95"] - d["cal_05"]).to_numpy()
    rng = (d["ah"] - d["al"]).to_numpy()
    if np.std(width) > 0 and np.std(rng) > 0:
        m["vol_corr"] = float(np.corrcoef(width, rng)[0, 1])
    return m


def build(fc, eng, candles, status, state_dir):
    agents = eng.names
    now_ts = int(status["run_ts"])
    last = int(candles["ts"].iloc[-1])
    rep = {"generated": _iso(now_ts), "product": PRODUCT, "gran": GRAN,
           "last_candle_close": _iso(last + GRAN),
           "staleness_min": round((now_ts - (last + GRAN)) / 60, 1),
           "n_candles_loaded": int(len(candles)),
           "filled_last_24h": int(candles["filled"].iloc[-1440:].sum()),
           "state_version": eng.version, "status": status}
    if len(fc):
        fc = add_locked(fc)
    rep["windows"] = {k: window_metrics(fc.iloc[-n:], agents) for k, n in WINDOWS.items()} if len(fc) else {}
    # reversal agent: its calls against chance and against a naive rule
    calls = store.read_calls(state_dir, now_ts - 31 * 86400)
    sw = swing_table(candles)
    rep["reversal"] = dict(eng.rev.summary(), k=REV_K, h=REV_H,
                           windows={k: reversal_metrics(calls, sw, now_ts - n * GRAN) for k, n in WINDOWS.items() if k != "1h"})

    P = eng.pending
    if P is not None and P.get("cal") is not None:
        c = float(candles["close"].iloc[-1])
        rep["next"] = {"for_candle": _iso(P["for_ts"]), "last_close": c, "p_up": _r(P["p_up"]),
                       "return_quantiles_bp": {t: _r(q * 1e4, 3) for t, q in zip(TAUS, P["cal"])},
                       "weights": {k: _r(v) for k, v in P["w"].items()},
                       "changepoint_prob": _r(P["cp_prob"]), "regime_age_min": _r(P["exp_run"], 1)}
    hmm = next((e for e in eng.agents if e.name == "hmm"), None)
    if hmm is not None and hmm.m.A is not None:
        rep["hmm"] = {"state_sd_bp": [_r(s, 2) for s in hmm.m.sd], "state_prob": [_r(a, 3) for a in hmm.m.alpha]}
    rep["calibration_offsets_sigma"] = {t: _r(v) for t, v in zip(TAUS, eng.calib.theta)}
    kb, kr = eng.tuner.scales()
    rep["goal_tuner"] = {"body_scale": kb, "reach_scale": kr,
                         "ahead": [[float(x) for x in t.scales()] for t in eng.tuners_h],
                         "cone_width": [round(float(c), 3) for c in eng.cone]}
    last_contest = next((e["lgbm"] for e in reversed(eng.retrain_log) if "lgbm" in e), None)
    rep["learning"] = {"candles_learned": int(eng.n), "body_scale": kb, "reach_scale": kr,
                       "last_contest": last_contest, "versions_published": len(eng.versions)}
    rep["retrain_log"] = eng.retrain_log[-8:]
    if eng.versions:
        v = eng.versions[-1]
        rep["student"] = {"versions": len(eng.versions), "latest_effective": _iso(v["eff"]), "rows": v["n"],
                          "fit_r2": dict(zip(student.OUTPUTS, v["r2"]))}

    # ---- goal keeper: is the team on track? ---------------------------------
    al = []
    if rep["staleness_min"] > 25:
        al.append(f"DATA STALE: last closed candle is {rep['staleness_min']} min old")
    if rep["filled_last_24h"] > 30:
        al.append(f"{rep['filled_last_24h']} missing candles were gap-filled in the last 24h")
    w = rep["windows"].get("24h", {})
    if w.get("n", 0) >= 600:
        st, te, bl = w.get("student"), w.get("teacher"), w["baseline"]
        if st and st["score"] < bl["typical"]["score"]:
            al.append(f"OFF TRACK: 24h candle score {st['score']:.3f} is below the naive 'typical candle' "
                      f"baseline {bl['typical']['score']:.3f}")
        if st and te and st["score"] < 0.93 * te["score"]:
            al.append(f"live generator loses to the full model: {st['score']:.3f} vs {te['score']:.3f}")
        if abs(w["cov90"] - 0.90) > 0.03:
            al.append(f"24h coverage of the 90% interval is {w['cov90']:.3f}")
        if abs(w["cov50"] - 0.50) > 0.04:
            al.append(f"24h coverage of the 50% interval is {w['cov50']:.3f}")
        if w.get("skill_vs_empirical", 0) < 0:
            al.append("24h: ensemble is WORSE than the unconditional baseline")
        if w["agents"] and w["loss_cal"] > 1.03 * min(w["agents"].values()):
            al.append("24h: ensemble is >3% worse than its best single agent")
    r7 = (rep.get("reversal") or {}).get("windows", {}).get("7d", {})
    if r7.get("n", 0) >= 200 and r7.get("naive_rule") is not None and r7["hit_rate"] < r7["naive_rule"]:
        al.append(f"reversal agent OFF TRACK: 7d hit rate {r7['hit_rate']:.3f} is below the naive rule {r7['naive_rule']:.3f}")
    if P is None or P.get("cal") is None:
        al.append("no forecast is pending for the next candle")
    elif P.get("gen") is None:
        al.append("no generated candle for the next minute (no live-generator version in effect)")
    if status.get("error"):
        al.append("last run error: " + str(status["error"])[:300])
    rep["alerts"] = al

    rd = os.path.join(state_dir, "reports")
    os.makedirs(rd, exist_ok=True)
    store.write_json(os.path.join(rd, "latest.json"), rep, indent=1)
    with open(os.path.join(rd, "latest.md"), "w") as f:
        f.write(markdown(rep, agents))
    publish(fc, eng, candles, rep, state_dir, calls)
    return rep


def publish(fc, eng, candles, rep, state_dir, calls, n=720):
    """Files the site reads straight from the `state` branch."""
    c = candles.iloc[-n:]
    cand = [[int(t), round(o, 2), round(h, 2), round(l, 2), round(cl, 2), round(v, 4)]
            for t, o, h, l, cl, v in zip(c["ts"], c["open"], c["high"], c["low"], c["close"], c["volume"])]
    gen = []
    if len(fc):
        g = fc[fc["g_b"].notna()].iloc[-n:]
        gen = [[int(t)] + [float(f"{x:.6g}") for x in vals]
               for t, *vals in zip(g["ts"], g["g_b"], g["g_u"], g["g_d"], g["g_p"], g["g_05"], g["g_25"], g["g_75"], g["g_95"])]
    P = eng.pending
    if P is not None and P.get("gen"):
        gg = P["gen"]
        gen.append([int(P["for_ts"])] + [float(f"{gg[k]:.6g}") for k in ("b", "u", "d", "p", "q05", "q25", "q75", "q95")])
    # the fixed record: each minute's candle as it was first generated (5 minutes ahead)
    locked = []
    if len(fc) and "lk_o" in fc:
        k = fc[fc["lk_o"].notna() & fc["g5_b"].notna()].iloc[-n:]
        locked = [[int(t)] + [float(f"{x:.6g}") for x in vals]
                  for t, *vals in zip(k["ts"], k["lk_o"], k["g5_b"], k["g5_u"], k["g5_d"])]
    for t in sorted(eng.multi):                           # minutes that have not closed yet
        e = eng.multi[t].get(HORIZON)
        if e is not None:
            locked.append([int(t)] + [float(f"{e[x]:.6g}") for x in ("o", "b", "u", "d")])
    cl = calls[calls["for_ts"] >= int(candles["ts"].iloc[-n])] if len(calls) else calls
    rev_calls = [[int(r.made_ts), int(r.for_ts), int(r.side), float(r.p), float(r.level),
                  None if r.hit != r.hit else int(r.hit)] for r in cl.itertuples()]
    path = None
    if P is not None and P.get("path"):
        path = {"origin": int(P["for_ts"]) - GRAN,
                "candles": [[float(f"{g[k]:.6g}") for k in ("b", "u", "d", "p", "lo", "hi")] for g in P["path"]]}
    slim = {}
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30:
            continue
        slim[k] = {"n": m["n"], "student": m["student"], "teacher": m["teacher"], "baseline": m["baseline"],
                   "ahead": m.get("ahead"), "locked": m.get("locked"),
                   "cov90": _r(m["cov90"]), "cov50": _r(m["cov50"]), "skill": _r(m.get("skill_vs_empirical")),
                   "brier": _r(m.get("brier")), "vol_corr": _r(m.get("vol_corr"))}
    latest = {"v": 1, "product": PRODUCT, "gran": GRAN, "generated": int(rep["status"]["run_ts"]),
              "last_ts": int(candles["ts"].iloc[-1]), "candles": cand,
              "gen_cols": ["ts", "b", "u", "d", "p", "q05", "q25", "q75", "q95"], "gen": gen,
              "path_cols": ["b", "u", "d", "p", "lo", "hi"], "path": path, "horizon": HORIZON,
              "locked_cols": ["ts", "o", "b", "u", "d"], "locked": locked,
              "rev_cols": ["made_ts", "for_ts", "side", "p", "level", "hit"], "rev_calls": rev_calls,
              "reversal": rep.get("reversal"),
              "learning": rep.get("learning"),
              "windows": slim, "next": rep.get("next"), "hmm": rep.get("hmm"), "student": rep.get("student"),
              "alerts": rep["alerts"], "retrain_log": rep["retrain_log"][-3:]}
    store.write_json(os.path.join(state_dir, "live", "latest.json"), latest)
    params = {"v": 1, "win": student.STUDENT_WIN, "lam": student.LAM, "features": student.FEATURES,
              "rev_features": student.REV_FEATURES, "rev_k": REV_K, "rev_h": REV_H,
              "outputs": student.OUTPUTS,
              "h_outputs": student.H_OUTPUTS,
              "versions": [{"eff": v["eff"], "W": v["W"].tolist(),
                            "H": None if v.get("H") is None else np.asarray(v["H"]).tolist(),
                            "R": None if v.get("R") is None else np.asarray(v["R"]).tolist(), "rt": v.get("rt"),
                            "scale": v.get("scale"), "cone": v.get("cone")} for v in eng.versions[-10:]]}
    store.write_json(os.path.join(state_dir, "live", "params.json"), params)


def markdown(rep, agents):
    L = [f"# {rep['product']} {rep['gran']}s candle generator - report", "",
         f"- generated: {rep['generated']}",
         f"- last closed candle: {rep['last_candle_close']} (staleness {rep['staleness_min']} min)", ""]
    L += ["## Goal keeper alerts", ""] + ([f"- {a}" for a in rep["alerts"]] or ["- none: on track"]) + [""]
    L += ["## The goal: generated candle vs real candle", "",
          "score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live "
          "generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.", "",
          "| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    f3 = lambda x: "-" if x is None else f"{x:.3f}"
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30:
            continue
        s, t, b = m.get("student") or {}, m.get("teacher") or {}, m["baseline"]
        L.append(f"| {k} | {m['n']} | {f3(s.get('score'))} | {f3(t.get('score'))} | {f3(b['repeat']['score'])} "
                 f"| {f3(b['typical']['score'])} | {f3(s.get('dir_acc'))} | {f3(s.get('body_iou'))} "
                 f"| {f3(s.get('range_iou'))} | {f3(s.get('body_size_ratio'))} |")
    L += ["", "## Candles generated further ahead (score / colour right / 90% cone held the close)", ""]
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30 or not m.get("ahead"):
            continue
        L.append(f"- {k}: " + "; ".join(
            f"{h} min ahead {f3(a['score'])} / {f3(a.get('dir_acc'))} / {f3(a.get('cone90'))}" for h, a in m["ahead"].items()))
    L += ["", "## The fixed record: candles locked 5 minutes ahead, compared at their real price level", ""]
    for k, m in rep["windows"].items():
        lk = m.get("locked")
        if lk:
            L.append(f"- {k}: match {lk['score']:.3f} (body {lk['body_iou']:.3f}, range {lk['range_iou']:.3f}), "
                     f"typical miss of the close {lk['median_miss_bp']:.1f} bp, n={lk['n']}")
    rv = rep.get("reversal") or {}
    L += ["", "## Reversal agent", "",
          f"- a swing point = highest high / lowest low of {rv.get('k')} candles on each side; a call is a hit if "
          "one forms within one candle of the minute it names",
          f"- model mix: {rv.get('weights')}, probability skill vs chance (Brier): {rv.get('brier_skill')}, "
          f"call threshold {rv.get('threshold')}, labels learned {rv.get('labels_learned')}"]
    for k, m in (rv.get("windows") or {}).items():
        if m.get("n", 0) >= 5 and "hit_rate" in m:
            L.append(f"- {k}: {m['n']} calls ({m['tops']} tops, {m['bottoms']} bottoms), hit rate {m['hit_rate']:.3f}, "
                     f"chance {m['chance']:.3f}, naive rule {f3(m.get('naive_rule'))} on {m['naive_calls']} calls, lift {m['lift']:.2f}x")
    L += ["", "## Probability quality (full model)", "",
          "| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |",
          "|---|---|---|---|---|---|---|---|"]
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30:
            continue
        L.append(f"| {k} | {m['loss_cal'] * 1e5:.3f} | {m.get('skill_vs_empirical', float('nan')) * 100:.2f}% "
                 f"| {m['cov90']:.3f} | {m['cov50']:.3f} | {f3(m.get('brier'))} | {f3(m.get('dir_acc_teacher'))} "
                 f"| {f3(m.get('vol_corr'))} |")
    L += ["", "## Per-agent pinball loss x1e5", "", "| window | " + " | ".join(agents) + " | ensemble | calibrated |",
          "|---|" + "---|" * (len(agents) + 2)]
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30:
            continue
        L.append(f"| {k} | " + " | ".join(f"{m['agents'][e] * 1e5:.3f}" if e in m["agents"] else "-" for e in agents)
                 + f" | {m['loss_raw'] * 1e5:.3f} | {m['loss_cal'] * 1e5:.3f} |")
    nx = rep.get("next")
    if nx:
        L += ["", "## Next candle", "", f"- candle starting {nx['for_candle']}, last close {nx['last_close']}",
              f"- P(up) {nx['p_up']}, return quantiles (bp): {nx['return_quantiles_bp']}",
              f"- changepoint probability {nx['changepoint_prob']}, regime age {nx['regime_age_min']} min",
              "- agent weights: " + ", ".join(f"{k} {v:.3f}" for k, v in nx["weights"].items())]
    L += ["", "## Learning log", ""]
    for e in rep["retrain_log"][-5:]:
        L.append(f"- {_iso(e['ts'])}: " + json.dumps({k: v for k, v in e.items() if k != 'ts'}))
    if "hmm" in rep:
        L.append(f"- HMM volatility states (sd, bp per minute): {rep['hmm']['state_sd_bp']}, "
                 f"current probabilities: {rep['hmm']['state_prob']}")
    if "student" in rep:
        L.append(f"- live generator: {rep['student']}")
    L.append(f"- goal tuner (multipliers that currently maximise the candle score): {rep['goal_tuner']}")
    L.append(f"- calibration offsets (in sigma): {rep['calibration_offsets_sigma']}")
    return "\n".join(L) + "\n"
