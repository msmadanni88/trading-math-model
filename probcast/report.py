"""Evaluation of the stored forecasts and everything the site and the weekly
review read: reports/latest.md|json, live/*.json, ledger/winrate.csv."""
import json
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import goal, store, student
from .agents.reversal import TYPES, spaced
from .config import GRAN, HORIZON, PRODUCT, REV_HS, REV_K, REV_KS, REV_MIN_PER_DAY
from .core import QUANTILES

TAUS = [f"{int(round(t * 100)):02d}" for t in QUANTILES]
WINDOWS = {"1h": 60, "6h": 360, "24h": 1440, "7d": 10080, "30d": 43200}
CURVE = [round(0.30 + 0.05 * i, 2) for i in range(13)]          # confidence thresholds shown in the control panel


def _iso(ts):
    return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def _r(x, k=4):
    return None if x is None or not np.isfinite(x) else round(float(x), k)


# ---------------------------------------------------------------- the fixed record
def locked_score(d):
    """The frozen chains against the real candles, both at their actual price
    level (being in the wrong place counts). `flat` is the same candles drawn
    at the price the chain started from - what "price stays here" would score."""
    if "lk_o" not in d:
        return None
    x = d[d["lk_o"].notna() & d["lk_r"].notna()]
    if len(x) < 30:
        return None
    sh = x["lk_r"] - x["lk_o"]
    body, rng, sc = goal.candle_score(x["lk_b"], x["lk_u"], x["lk_d"], x["ao"] + sh, x["y"] + sh, x["ah"] + sh, x["al"] + sh)
    _, _, fl = goal.candle_score(x["lk_b"], x["lk_u"], x["lk_d"], x["ao"] + x["lk_r"], x["y"] + x["lk_r"],
                                 x["ah"] + x["lk_r"], x["al"] + x["lk_r"])
    real_close = x["lk_r"] + x["y"]
    nz = x["y"] != 0
    out = {"n": int(len(x)), "score": float(sc.mean()), "body_iou": float(body.mean()), "range_iou": float(rng.mean()),
           "flat_score": float(fl.mean()),
           "colour_right": float(((x["lk_b"] > 0) == (x["y"] > 0))[nz].mean()) if nz.any() else None,
           "median_miss_bp": float(np.median(np.abs(real_close - x["lk_o"] - x["lk_b"])) * 1e4),
           "by_candle": {}}
    for h in range(1, HORIZON + 1):
        m = (x["lk_h"] == h).to_numpy()
        if m.sum() >= 5:
            out["by_candle"][str(h)] = {"score": float(sc[m].mean()),
                                        "miss_bp": float(np.median(np.abs(real_close - x["lk_o"] - x["lk_b"])[m]) * 1e4)}
    e = x[(x["lk_h"] == HORIZON) & (real_close != 0)]           # where the chain ended vs where the market ended
    if len(e) >= 5:
        out["end_side_right"] = float(((e["lk_o"] + e["lk_b"] > 0) == (e["lk_r"] + e["y"] > 0)).mean())
        out["chains"] = int(len(e))
    return out


# ---------------------------------------------------------------- reversal agents
def swing_table(candles, K):
    """Swing highs / lows of size K in the real candles, plus what a naive
    caller would have scored (for the agent to beat)."""
    h, l = candles["high"], candles["low"]
    w = 2 * K + 1
    top = (h >= h.rolling(w, center=True).max()).astype(float).where(h.rolling(w, center=True).max().notna())
    bot = (l <= l.rolling(w, center=True).min()).astype(float).where(l.rolling(w, center=True).min().notna())
    out = pd.DataFrame({"ts": candles["ts"].to_numpy(), "top": top.to_numpy(), "bot": bot.to_numpy()})
    for k in ("top", "bot"):                      # a swing point within one candle of this minute
        out[k + "3"] = out[k].rolling(3, center=True).max()
    # naive caller: "a candle that makes a fresh K-candle high is the top" (and mirrored)
    out["new_hi"] = (h >= h.shift(1).rolling(K).max()).to_numpy()
    out["new_lo"] = (l <= l.shift(1).rolling(K).min()).to_numpy()
    return out


def reversal_window(calls, sw, since_ts, typ):
    c = calls[(calls["for_ts"] >= since_ts) & calls["hit"].notna() & (calls["typ"] == typ)]
    s = sw[(sw["ts"] >= since_ts) & sw["top3"].notna()]
    if len(s) < 30:
        return {"n": int(len(c))}
    chance = float(pd.concat([s["top3"], s["bot3"]]).mean())
    out = {"n": int(len(c)), "chance": chance, "per_day": float(len(c) / max(len(s) / 1440.0, 1e-9))}
    if typ == 0:
        naive = pd.concat([s.loc[s["new_hi"], "top3"], s.loc[s["new_lo"], "bot3"]])
        out["naive_rule"] = float(naive.mean()) if len(naive) else None
        out["naive_calls"] = int(len(naive))
    if len(c) >= 5:
        out["hit_rate"] = float(c["hit"].mean())
        out["lift"] = float(c["hit"].mean() / chance) if chance > 0 else None
        out["tops"] = int((c["side"] > 0).sum())
        out["bottoms"] = int((c["side"] < 0).sum())
    return out


def reversal_curve(fc, sw, K, since_ts):
    """What every confidence threshold would have given over a period: calls a
    day and hit rate, per call type. This is the control panel's map - it is
    computed from the probabilities the published model issued at the time."""
    cols = [f"r{K}_tn", f"r{K}_tx", f"r{K}_bn", f"r{K}_bx"]
    if cols[0] not in fc:
        return None
    d = fc.loc[fc["ts"] >= since_ts, ["ts"] + cols].merge(sw[["ts", "top3", "bot3"]], on="ts", how="left")
    if len(d) < 300:
        return None
    lab = {s: d.set_index("ts")[s] for s in ("top3", "bot3")}
    out, ts = {}, d["ts"].to_numpy()
    days = len(d) / 1440.0
    for a, typ in enumerate(TYPES):
        pts = []
        Y = [lab[s].reindex(ts + REV_HS[a] * GRAN).to_numpy() for s in ("top3", "bot3")]
        Pm = [d[cols[0 + a]].to_numpy(), d[cols[2 + a]].to_numpy()]
        for thr in CURVE:
            n = h = 0
            for side in (0, 1):
                ok = np.isfinite(Y[side]) & (Pm[side] >= thr)
                idx = spaced((ts[ok] // GRAN).tolist())
                if idx:
                    pos = np.searchsorted(ts // GRAN, idx)
                    n += len(idx)
                    h += float(Y[side][pos].sum())
            pts.append([thr, round(n / days, 1), None if n < 5 else round(h / n, 4), int(n)])
        out[typ] = pts
    return out


def reversal_report(eng, fc, candles, calls, now_ts):
    rep = {}
    for K in REV_KS:
        ag = eng.rev[K]
        sw = swing_table(candles, K)
        ck = calls[calls["k"] == K] if len(calls) else calls
        r = dict(ag.summary(), tuned=ag.tuned, windows={})
        for name, n in WINDOWS.items():
            if name == "1h":
                continue
            r["windows"][name] = {t: reversal_window(ck, sw, now_ts - n * GRAN, a) for a, t in enumerate(TYPES)}
        r["curve"] = {"7d": reversal_curve(fc, sw, K, now_ts - 7 * 86400), "30d": reversal_curve(fc, sw, K, now_ts - 30 * 86400)} \
            if len(fc) else None
        rep[str(K)] = r
    return rep


# ---------------------------------------------------------------- win-rate ledger
def ledger_days(fc, calls, candles, live_since):
    """One line per UTC day and layer: how many predictions were judged and
    how many were right. `base` is what chance alone would score."""
    rows = []
    if len(fc):
        day = fc["ts"].map(store.day)
        x = fc[(fc["y"] != 0) & fc["g_b"].notna()]
        win = ((x["g_b"] > 0) == (x["y"] > 0)).astype(int).groupby(day.loc[x.index]).agg(["count", "sum"])
        for dname, r in win.iterrows():
            rows.append([dname, "colour_next", int(r["count"]), int(r["sum"]), 0.5])
        dc = [c for c in fc.columns if c[0] == "d" and c[1:].isdigit()]
        if dc:
            cnt = fc[dc].notna().sum(axis=1).groupby(day).sum()
            win = fc[dc].sum(axis=1).groupby(day).sum()
            for dname in cnt.index:
                if cnt[dname] > 0:
                    rows.append([dname, "colour_path", int(cnt[dname]), int(win[dname]), 0.5])
        if "lk_o" in fc:
            e = fc[(fc["lk_h"] == HORIZON) & fc["lk_o"].notna() & (fc["lk_r"] + fc["y"] != 0)]
            if len(e):
                ok_e = (e["lk_o"] + e["lk_b"] > 0) == (e["lk_r"] + e["y"] > 0)
                de = e["ts"].map(store.day)
                for dname in sorted(set(de)):
                    m = (de == dname).to_numpy()
                    rows.append([dname, "chain_end_side", int(m.sum()), int(ok_e.to_numpy()[m].sum()), 0.5])
    if len(calls):
        c = calls[calls["hit"].notna()]
        dc_ = c["for_ts"].map(store.day)
        chance = {}
        for K in REV_KS:
            sw = swing_table(candles, K)
            sd = sw["ts"].map(store.day)
            ch = pd.concat([sw["top3"], sw["bot3"]], axis=1).mean(axis=1).groupby(sd).mean()
            chance[K] = ch
        for (dname, K, typ), g in c.groupby([dc_, "k", "typ"]):
            base = chance.get(int(K), pd.Series(dtype=float)).get(dname, np.nan)
            rows.append([dname, f"reversal_k{int(K)}_{TYPES[int(typ)]}", int(len(g)), int(g["hit"].sum()),
                         None if base != base else round(float(base), 4)])
    out = pd.DataFrame(rows, columns=["day", "layer", "n", "wins", "base"])
    live_day = store.day(live_since) if live_since else "9999"
    out["live"] = (out["day"] >= live_day).astype(int)
    return out


def ledger_summary(led, today):
    """Per layer: win rate over the last complete day, 7 and 30 days and since
    the archive began, the trend (last 7 days against the 7 before), and the
    same for everything pooled."""
    if not len(led):
        return {}
    done = led[led["day"] < today]                    # complete days only
    days = sorted(set(done["day"]))
    if not days:
        return {}
    out = {}

    def agg(x):
        n = int(x["n"].sum())
        return None if n == 0 else {"n": n, "rate": round(float(x["wins"].sum() / n), 4)}

    def block(x):
        if not len(x):
            return None
        b = x.dropna(subset=["base"])
        res = {"1d": agg(x[x["day"] == days[-1]]), "7d": agg(x[x["day"].isin(days[-7:])]),
               "30d": agg(x[x["day"].isin(days[-30:])]), "all": agg(x), "since": min(x["day"]),
               "live": agg(x[x["live"] == 1]),
               "base": round(float((b["base"] * b["n"]).sum() / b["n"].sum()), 4) if len(b) and b["n"].sum() else None}
        prev = agg(x[x["day"].isin(days[-14:-7])])
        if res["7d"] and prev and prev["n"] >= 30 and res["7d"]["n"] >= 30:
            p, q = res["7d"]["rate"], prev["rate"]
            se = float(np.sqrt(p * (1 - p) / res["7d"]["n"] + q * (1 - q) / prev["n"]))
            res["trend"] = {"change": round(p - q, 4), "noise": round(se, 4),
                            "verdict": "up" if p - q > 2 * se else "down" if q - p > 2 * se else "flat"}
        return res

    for layer in sorted(set(done["layer"])):
        out[layer] = block(done[done["layer"] == layer])
    out["overall"] = block(done.assign(base=np.nan))
    return out


# ---------------------------------------------------------------- windows
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
    m["cov90"] = float(((y >= d["cal_05"]) & (y <= d["cal_95"])).mean())
    m["cov50"] = float(((y >= d["cal_25"]) & (y <= d["cal_75"])).mean())
    g = d[d["g_05"].notna()]
    if len(g) >= 30:
        yg = g["y"].to_numpy()
        m["cov90_site"] = float(((yg >= g["g_05"]) & (yg <= g["g_95"])).mean())
        m["cov50_site"] = float(((yg >= g["g_25"]) & (yg <= g["g_75"])).mean())
    # every candle of the chain, each judged from its own open (shape and colour only)
    m["ahead"] = {"1": {"score": m["student"]["score"], "dir_acc": m["student"]["dir_acc"],
                        "cone90": m.get("cov90_site")}} if m["student"] else {}
    for hz in range(2, HORIZON + 1):
        if f"s{hz}" not in d:
            continue
        s, dd, ci = d[f"s{hz}"].dropna(), d[f"d{hz}"].dropna(), d[f"c{hz}_in"].dropna()
        if len(s) >= 30:
            m["ahead"][str(hz)] = {"score": float(s.mean()), "dir_acc": float(dd.mean()) if len(dd) else None,
                                   "cone90": float(ci.mean()) if len(ci) else None}
    m["locked"] = locked_score(d)
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


def build(fc, eng, candles, status, state_dir, meta=None):
    agents = eng.names
    now_ts = int(status["run_ts"])
    meta = meta or {}
    last = int(candles["ts"].iloc[-1])
    rep = {"generated": _iso(now_ts), "product": PRODUCT, "gran": GRAN,
           "last_candle_close": _iso(last + GRAN),
           "staleness_min": round((now_ts - (last + GRAN)) / 60, 1),
           "n_candles_loaded": int(len(candles)),
           "filled_last_24h": int(candles["filled"].iloc[-1440:].sum()),
           "state_version": eng.version, "live_since": meta.get("live_since"), "status": status}
    rep["windows"] = {k: window_metrics(fc.iloc[-n:], agents) for k, n in WINDOWS.items()} if len(fc) else {}
    calls = store.read_calls(state_dir, now_ts - 31 * 86400)
    rep["reversal"] = reversal_report(eng, fc, candles, calls, now_ts)

    # the win-rate ledger: complete days are written once and kept
    led = store.merge_ledger(state_dir, ledger_days(fc, calls, candles, meta.get("live_since")), store.day(now_ts))
    rep["ledger"] = ledger_summary(led, store.day(now_ts))

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
                         "ahead": [[float(x) for x in t.scales()] for t in eng.tuners_h[1:]],
                         "cone_width": [round(float(c), 3) for c in eng.cone[1:]]}
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
    for K, r in rep["reversal"].items():
        w7 = r["windows"].get("7d", {})
        now7 = w7.get("now", {})
        if now7.get("n", 0) >= 100 and now7.get("naive_rule") is not None and now7.get("hit_rate", 1) < now7["naive_rule"]:
            al.append(f"reversal agent K={K} OFF TRACK: 7d hit rate {now7['hit_rate']:.3f} is below the naive rule {now7['naive_rule']:.3f}")
        for t in TYPES:
            x = w7.get(t, {})
            if x.get("n", 0) and x.get("per_day", REV_MIN_PER_DAY) < 0.5 * REV_MIN_PER_DAY:
                al.append(f"reversal agent K={K}: only {x['per_day']:.0f} '{t}' calls a day in the last 7 days")
        if r.get("stalled"):
            al.append(f"reversal agent K={K}: recent hit rate is below its long-run level - its next daily contest is widened")
    for layer, b in rep["ledger"].items():
        t = (b or {}).get("trend")
        if t and t["verdict"] == "down":
            al.append(f"WIN RATE FALLING: {layer} {b['7d']['rate']:.3f} in the last 7 days, {t['change']:+.3f} against the 7 before")
    if P is None or P.get("cal") is None:
        al.append("no forecast is pending for the next candle")
    elif P.get("gen") is None:
        al.append("no generated candle for the next minute (no live-generator version in effect)")
    elif not P.get("path") or len(P["path"]) < HORIZON:
        al.append("the chain of generated candles is incomplete (per-candle heads not fitted yet)")
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
    first = int(c["ts"].iloc[0])
    cand = [[int(t), round(o, 2), round(h, 2), round(l, 2), round(cl, 2), round(v, 4)]
            for t, o, h, l, cl, v in zip(c["ts"], c["open"], c["high"], c["low"], c["close"], c["volume"])]
    sig6 = lambda x: float(f"{x:.6g}")
    gen, locked, probs = [], [], {str(K): [] for K in REV_KS}
    if len(fc):
        tail = fc[fc["ts"] >= first]
        g = tail[tail["g_b"].notna()]
        gen = [[int(t)] + [sig6(x) for x in vals]
               for t, *vals in zip(g["ts"], g["g_b"], g["g_u"], g["g_d"], g["g_p"], g["g_05"], g["g_25"], g["g_75"], g["g_95"])]
        if "lk_o" in tail:
            k = tail[tail["lk_o"].notna()]
            locked = [[int(t), int(h)] + [sig6(x) for x in vals]
                      for t, h, *vals in zip(k["ts"], k["lk_h"], k["lk_o"], k["lk_b"], k["lk_u"], k["lk_d"])]
        for K in REV_KS:                                    # what the published model said, per minute (x1000)
            cols = [f"r{K}_tn", f"r{K}_tx", f"r{K}_bn", f"r{K}_bx"]
            if cols[0] in tail:
                q = tail[tail[cols[0]].notna()]
                probs[str(K)] = [[int(t)] + [int(round(1000 * x)) for x in vals] for t, *vals in zip(q["ts"], *(q[x] for x in cols))]
    P = eng.pending
    if P is not None and P.get("gen"):
        gg = P["gen"]
        gen.append([int(P["for_ts"])] + [sig6(gg[k]) for k in ("b", "u", "d", "p", "q05", "q25", "q75", "q95")])
    for t in sorted(eng.snap):                              # minutes of the current chain that have not closed yet
        e = eng.snap[t]
        locked.append([int(t), int(e["h"])] + [sig6(e[x]) for x in ("o", "b", "u", "d")])
    path = None
    if P is not None and P.get("path"):
        path = {"origin": int(P["for_ts"]) - GRAN,
                "candles": [[sig6(g[k]) for k in ("b", "u", "d", "p", "o", "lo", "hi")] for g in P["path"]]}
    rev = {}
    for K in REV_KS:
        ck = calls[(calls["k"] == K) & (calls["for_ts"] >= first)] if len(calls) else calls
        rc = [[int(r.made_ts), int(r.for_ts), int(r.side), int(r.typ), float(r.p), float(r.level),
               None if r.hit != r.hit else int(r.hit)] for r in ck.itertuples()]
        rev[str(K)] = dict(rep["reversal"][str(K)], calls=rc, probs=probs[str(K)])
    slim = {}
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30:
            continue
        slim[k] = {"n": m["n"], "student": m["student"], "teacher": m["teacher"], "baseline": m["baseline"],
                   "ahead": m.get("ahead"), "locked": m.get("locked"),
                   "cov90": _r(m["cov90"]), "cov50": _r(m["cov50"]), "skill": _r(m.get("skill_vs_empirical")),
                   "brier": _r(m.get("brier")), "vol_corr": _r(m.get("vol_corr"))}
    gen_ts = int(rep["status"]["run_ts"])
    latest = {"v": 2, "product": PRODUCT, "gran": GRAN, "generated": gen_ts,
              "last_ts": int(candles["ts"].iloc[-1]), "live_since": rep.get("live_since"), "candles": cand,
              "gen_cols": ["ts", "b", "u", "d", "p", "q05", "q25", "q75", "q95"], "gen": gen,
              "path_cols": ["b", "u", "d", "p", "o", "lo", "hi"], "path": path, "horizon": HORIZON,
              "locked_cols": ["ts", "h", "o", "b", "u", "d"], "locked": locked,
              "rev_cols": {"calls": ["made_ts", "for_ts", "side", "typ", "p", "level", "hit"],
                           "probs": ["ts", "top_now", "top_next", "bottom_now", "bottom_next"]},
              "rev": rev, "rev_min_per_day": REV_MIN_PER_DAY, "curve_thresholds": CURVE,
              "ledger": rep.get("ledger"), "learning": rep.get("learning"),
              "windows": slim, "next": rep.get("next"), "hmm": rep.get("hmm"), "student": rep.get("student"),
              "alerts": rep["alerts"], "retrain_log": rep["retrain_log"][-3:]}
    live = os.path.join(state_dir, "live")
    store.write_json(os.path.join(live, "latest.json"), latest)
    # Published parameter versions. The site needs the few that can still be
    # in force; a restored engine (see run.py) may need to look further back.
    out = lambda v: {"eff": v["eff"], "fmt": v.get("fmt"), "W": v["W"].tolist(),
                     "H": None if v.get("H") is None else np.asarray(v["H"]).tolist(),
                     "scale": v.get("scale"), "cone": v.get("cone"), "rm": v.get("rm"), "rt": v.get("rt")}
    vers = eng.versions[-4:]
    params = {"v": 2, "fmt": student.FORMAT, "win": student.STUDENT_WIN, "lam": student.LAM, "horizon": HORIZON,
              "features": student.FEATURES, "outputs": student.OUTPUTS, "h_outputs": student.H_OUTPUTS,
              "rev": {"ks": list(REV_KS), "k": REV_K, "hs": list(REV_HS), "features": student.REV_FEATURES},
              "versions": [out(v) for v in vers]}
    store.write_json(os.path.join(live, "params.json"), params)
    store.write_json(os.path.join(state_dir, "versions.json"), {"v": 2, "versions": [out(v) for v in eng.versions[-14:]]})
    # the tree models those versions refer to: one small file per swing size
    ids = {}
    for K, ag in eng.rev.items():
        want = {int((v.get("rm") or {}).get(str(K), 0)) for v in vers} | {int(ag.model_id)}      # at most three exist
        ms = {str(i): {a: b for a, b in ag.models[i].items() if a != "_np"} for i in sorted(want) if i in ag.models}
        ids[str(K)] = sorted(ms)
        store.write_json(os.path.join(live, f"rev_k{K}.json"), {"v": 2, "k": K, "models": ms})
    # a few bytes the site polls every minute; the big files are fetched only when this changes
    store.write_json(os.path.join(live, "head.json"), {"v": 2, "generated": gen_ts, "last_ts": latest["last_ts"],
                                                       "eff": [v["eff"] for v in vers], "models": ids})


def markdown(rep, agents):
    L = [f"# {rep['product']} {rep['gran']}s candle generator - report", "",
         f"- generated: {rep['generated']}",
         f"- last closed candle: {rep['last_candle_close']} (staleness {rep['staleness_min']} min)",
         f"- this generation of the models went live: {_iso(rep['live_since']) if rep.get('live_since') else 'unknown'}"
         " (numbers for earlier days are a replay of history, minute by minute, with only the past visible)", ""]
    L += ["## Goal keeper alerts", ""] + ([f"- {a}" for a in rep["alerts"]] or ["- none: on track"]) + [""]
    f3 = lambda x: "-" if x is None else f"{x:.3f}"
    L += ["## Win-rate ledger (complete UTC days only; archived in ledger/winrate.csv)", "",
          "| layer | last day | 7 days | 30 days | all | since go-live | chance | trend |", "|---|---|---|---|---|---|---|---|"]
    cell = lambda a: "-" if not a else f"{a['rate']:.3f} ({a['n']})"
    trend = lambda t: "-" if not t else f"{t['verdict']} {t['change']:+.3f}"
    for layer, b in (rep.get("ledger") or {}).items():
        if b:
            L.append(f"| {layer} | {cell(b['1d'])} | {cell(b['7d'])} | {cell(b['30d'])} | {cell(b['all'])} | {cell(b['live'])} "
                     f"| {f3(b.get('base'))} | {trend(b.get('trend'))} |")
    L += ["", "## The goal: generated candle vs real candle", "",
          "score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live "
          "generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.", "",
          "| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30:
            continue
        s, t, b = m.get("student") or {}, m.get("teacher") or {}, m["baseline"]
        L.append(f"| {k} | {m['n']} | {f3(s.get('score'))} | {f3(t.get('score'))} | {f3(b['repeat']['score'])} "
                 f"| {f3(b['typical']['score'])} | {f3(s.get('dir_acc'))} | {f3(s.get('body_iou'))} "
                 f"| {f3(s.get('range_iou'))} | {f3(s.get('body_size_ratio'))} |")
    L += ["", f"## Every candle of the {HORIZON}-candle chain, judged from its own open (score / colour right / 90% range held the close)", ""]
    for k, m in rep["windows"].items():
        if m.get("n", 0) < 30 or not m.get("ahead"):
            continue
        L.append(f"- {k}: " + "; ".join(
            f"{h}: {f3(a['score'])} / {f3(a.get('dir_acc'))} / {f3(a.get('cone90'))}" for h, a in m["ahead"].items()))
    L += ["", f"## The fixed record: the chain frozen at the start of every {HORIZON} minutes, compared at its real price level", ""]
    for k, m in rep["windows"].items():
        lk = m.get("locked")
        if lk:
            L.append(f"- {k}: match {lk['score']:.3f} (body {lk['body_iou']:.3f}, range {lk['range_iou']:.3f}); "
                     f"'price stays where it was' would score {lk['flat_score']:.3f}; colour right {f3(lk.get('colour_right'))}; "
                     f"typical miss of the close {lk['median_miss_bp']:.1f} bp; chain ended on the right side "
                     f"{f3(lk.get('end_side_right'))} of {lk.get('chains', 0)} chains; n={lk['n']}")
    lk = (rep["windows"].get("30d") or {}).get("locked") or (rep["windows"].get("7d") or {}).get("locked")
    if lk and lk.get("by_candle"):
        L.append("- by candle of the chain (match / typical miss of the close in bp): " +
                 "; ".join(f"{h}: {v['score']:.3f} / {v['miss_bp']:.1f}" for h, v in lk["by_candle"].items()))
    L += ["", "## Reversal agents", "",
          "- a swing point of size K = highest high / lowest low of K candles on each side",
          "- `now`: the turn is in (a swing point at the candle that just closed, give or take one); "
          "`next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.",
          f"- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep "
          f"{REV_MIN_PER_DAY} calls a day"]
    for K, r in (rep.get("reversal") or {}).items():
        L.append(f"- **K={K}**: model {r['model_id']}, labels learned {r['labels_learned']}, probability skill vs chance "
                 f"{r.get('brier_skill')}, widened contest next: {r.get('stalled')}")
        for t in TYPES:
            ty = r["types"][t]
            L.append(f"  - {t}: threshold {ty['threshold']}, hit rate recent {ty['recent']} / long run {ty['long_run']}")
            for wn, wv in r["windows"].items():
                x = wv.get(t, {})
                if "hit_rate" in x:
                    L.append(f"    - {wn}: {x['n']} calls ({x['per_day']:.0f} a day), hit rate {x['hit_rate']:.3f}, chance {x['chance']:.3f}"
                             + (f", naive rule {f3(x.get('naive_rule'))}" if t == "now" else "") + f", lift {x['lift']:.2f}x")
        cv = (r.get("curve") or {}).get("30d") or (r.get("curve") or {}).get("7d")
        if cv:
            for t in TYPES:
                L.append(f"  - {t}, what each threshold would give (threshold: calls a day, hit rate): " +
                         "; ".join(f"{p[0]:.2f}: {p[1]:.0f}, {f3(p[2])}" for p in cv[t] if p[3] >= 5))
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
