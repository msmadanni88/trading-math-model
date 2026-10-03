"""Entry point:  python -m probcast.run step --state-dir state --cache-dir cache

Downloads the candles that closed since the last run, lets every agent learn
from each of them in order, stores forecasts + reports + the files the site
reads, and publishes a fresh version of the live generator. If no valid engine
is found (first run, cache lost, or STATE_VERSION changed) the recent history
is replayed: the system rebuilds itself from the stored candles alone.
"""
import argparse
import gzip
import json
import os
import pickle
import re
import sys
import time
import traceback
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from . import data, report, store
from .config import BUF, GRAN, PRODUCT, REPLAY_DAYS, START, STUDENT_LEAD, STUDENT_STEP
from .engine import STATE_VERSION, Engine
from .features import compute_features, feature_names, regularize


# THE RECORD: every column that holds something the models said before the
# outcome existed - generated candles, the frozen chain, per-candle results of
# the chain, reversal probabilities. Once written, a value is never rewritten.
PROTECTED = re.compile(r"^(g\d*_|c\d+_in$|s\d+$|d\d+$|lk_|r\d+_)")
DECISIONS = ("g_call",)       # columns that qualify the stored prediction of the same row


def load_engine(path):
    if not os.path.exists(path):
        return None, "no saved engine"
    try:
        with gzip.open(path, "rb") as f:
            eng = pickle.load(f)
        if getattr(eng, "version", None) != STATE_VERSION:
            return None, "state version changed"
        return eng, None
    except Exception as e:
        return None, f"saved engine unreadable: {type(e).__name__}: {e}"


def save_engine(eng, path):
    tmp = path + ".tmp"
    with gzip.open(tmp, "wb", compresslevel=4) as f:
        pickle.dump(eng, f, protocol=4)
    os.replace(tmp, path)


def run_engine(eng, df, start_idx, progress=False):
    """Process df rows [start_idx:]. Returns list of scored log rows."""
    lo = max(0, start_idx - BUF)
    feats = compute_features(df.iloc[lo:].reset_index(drop=True))
    F = feats[feature_names()].to_numpy(float)[start_idx - lo:]
    gk = feats["_gk"].to_numpy(float)[start_idx - lo:]
    sub = df.iloc[start_idx:]
    ts = sub["ts"].to_numpy(np.int64)
    o, h, l, c, v = (sub[k].to_numpy(float) for k in ("open", "high", "low", "close", "volume"))
    rows = []
    t0 = time.time()
    for i in range(len(sub)):
        row = eng.process(ts[i], o[i], h[i], l[i], c[i], v[i], F[i], gk[i])
        if row is not None:
            rows.append(row)
        if progress and (i + 1) % 10000 == 0:
            print(f"  replay {i + 1}/{len(sub)}  {time.time() - t0:.0f}s", flush=True)
    return rows


def step(state_dir, cache_dir, offline=False, now=None):
    t_start = time.time()
    now = time.time() if now is None else now
    os.makedirs(state_dir, exist_ok=True)
    os.makedirs(cache_dir, exist_ok=True)
    eng_path = os.path.join(cache_dir, "engine.pkl.gz")
    start_ts = int(datetime.strptime(START, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())
    status = {"run_ts": int(now), "run_at": data.iso(int(now)), "product": PRODUCT, "error": None}

    horizon = int(now) - (REPLAY_DAYS + 1) * 86400
    rows = store.read_candles(state_dir, max(start_ts, horizon))
    new, fetch_err = [], None
    if not offline:
        try:
            first = not rows
            rows, new = data.update(rows, max(start_ts, horizon), now=now, verbose=first)
            if new:
                store.write_candles(state_dir, rows, new[0][0])
        except Exception as e:      # keep going with what we have; report it
            fetch_err = f"{type(e).__name__}: {e}"
    if not rows:
        raise RuntimeError(f"no candles available ({fetch_err})")
    df = regularize(rows)

    eng, why = load_engine(eng_path)
    replay = False
    if eng is not None:
        idx = np.searchsorted(df["ts"].to_numpy(), eng.last_ts)
        if idx >= len(df) or df["ts"].iloc[idx] != eng.last_ts:
            eng, why = None, "saved engine does not match candle history"
    if eng is None:
        print(f"replaying history: {why}", flush=True)
        eng, replay, start_idx = Engine(fast_backfill=True), True, 0
    else:
        start_idx = int(idx) + 1

        # versions published by runs newer than the restored engine
        pub = store.read_json(os.path.join(state_dir, "versions.json"))
        eng.merge_versions((pub or {}).get("versions", []))

    new_rows = run_engine(eng, df, start_idx, progress=replay) if start_idx < len(df) else []
    eng.fast_backfill = False
    eng.simulate_publish = False

    # a new live-generator version, effective a few minutes from now so every
    # open browser has it before it is used (and the record stays reproducible)
    eff = -(-(int(now) + STUDENT_LEAD) // STUDENT_STEP) * STUDENT_STEP
    eng.fit_student(eff, np.iinfo(np.int64).max)

    # reversal calls: appended, never edited (see store.merge_calls)
    for ag in eng.rev.values():
        store.merge_calls(state_dir, ag.events)
        ag.events = []

    # when did this generation of the models start running for real? Everything
    # stored for earlier minutes is a replay of history, and reports say so.
    meta_path = os.path.join(state_dir, "meta.json")
    meta = store.read_json(meta_path) or {}
    if meta.get("engine") != STATE_VERSION:
        meta = {"engine": STATE_VERSION, "live_since": int(now)}
        store.write_json(meta_path, meta, indent=1)

    fc_new = pd.DataFrame(new_rows)
    if len(fc_new):
        t0 = int(fc_new["ts"].iloc[0])
        old = store.read_forecasts(state_dir, t0 - 86400)
        if len(old):
            # THE RECORD: whatever the models said about a candle and is already
            # stored is never rewritten - not when an older engine copy re-learns
            # that minute, and not when the whole engine is rebuilt. A cell that
            # is still empty (a column that did not exist then) may be filled once.
            keep = old[old["ts"] >= t0].set_index("ts")
            if len(keep):
                fc_new = fc_new.set_index("ts")
                both = keep.index.intersection(fc_new.index)
                # a decision about a prediction (is this colour call a confident one?)
                # belongs to that prediction: it is not added to a stored prediction
                # that this engine would have made differently
                other = pd.Series(False, index=both)
                if "g_p" in keep.columns and "g_p" in fc_new.columns:
                    sp, fp = keep.loc[both, "g_p"], fc_new.loc[both, "g_p"]
                    other = sp.notna() & ~np.isclose(sp, fp, rtol=2e-5, atol=1e-9)    # stored with 6 digits
                for c in [c for c in keep.columns if PROTECTED.match(c)]:
                    if c not in fc_new.columns:
                        fc_new[c] = np.nan                      # a retired column stays in the archive
                    stored = keep.loc[both, c]
                    fc_new.loc[both, c] = stored.where(stored.notna(), fc_new.loc[both, c])
                for c in DECISIONS:
                    if c in fc_new.columns:
                        had = keep.loc[both, c].notna() if c in keep.columns else pd.Series(False, index=both)
                        fc_new.loc[both[(other & ~had).to_numpy()], c] = np.nan
                fc_new = fc_new.reset_index()
        fc_tail = pd.concat([old[old["ts"] < t0], fc_new], ignore_index=True) if len(old) else fc_new
        store.write_forecasts(state_dir, fc_tail, t0)
    # the fitted engine is uploaded to the cache only every ~30 minutes (or
    # after a replay); in between, a run simply re-learns the last few candles
    stamp = os.path.join(cache_dir, "saved_at")
    saved_at = float(open(stamp).read()) if os.path.exists(stamp) else 0.0
    upload = replay or now - saved_at >= 1700
    if upload or not os.path.exists(eng_path):
        save_engine(eng, eng_path)
        with open(stamp, "w") as f:
            f.write(str(int(now)))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"save_cache={'true' if upload else 'false'}\n")
    store.prune(state_dir, now)

    fc = store.read_forecasts(state_dir, int(now) - 31 * 86400)
    status.update(n_new_candles=len(new), n_processed=int(len(df) - start_idx), replay=replay,
                  replay_reason=why if replay else None, fetch_error=fetch_err,
                  last_candle_ts=int(df["ts"].iloc[-1]), duration_s=round(time.time() - t_start, 1))
    if fetch_err:
        status["error"] = "candle download failed: " + fetch_err
    rep = report.build(fc, eng, df, status, state_dir, meta)
    with open(os.path.join(state_dir, "status.json"), "w") as f:
        json.dump(status, f, indent=1)
    print(json.dumps({k: status[k] for k in ("run_at", "n_new_candles", "n_processed", "replay", "duration_s", "error")}))
    for a in rep["alerts"]:
        print("ALERT:", a)
    return status, rep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["step"])
    ap.add_argument("--state-dir", default=os.environ.get("STATE_DIR", "state"))
    ap.add_argument("--cache-dir", default=os.environ.get("CACHE_DIR", "cache"))
    ap.add_argument("--offline", action="store_true", help="do not download, use stored candles")
    a = ap.parse_args()
    try:
        step(a.state_dir, a.cache_dir, offline=a.offline)
    except Exception as e:
        traceback.print_exc()
        os.makedirs(a.state_dir, exist_ok=True)
        with open(os.path.join(a.state_dir, "status.json"), "w") as f:
            json.dump({"run_at": data.iso(int(time.time())), "error": f"{type(e).__name__}: {e}"}, f)
        sys.exit(1)
    # a failed download is not fatal: the next run catches up, and the error is
    # recorded in status.json / the report
    sys.exit(0)


if __name__ == "__main__":
    main()
