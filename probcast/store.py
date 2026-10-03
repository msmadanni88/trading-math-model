"""On-disk layout of the state directory (kept on the `state` git branch).

Plain-text CSV, one file per UTC day: a run appends a few lines to one small
file, so git stores only tiny deltas.

  candles/YYYY-MM-DD.csv    forecasts/YYYY-MM-DD.csv    calls/YYYY-MM-DD.csv
  xcandles/YYYY-MM-DD.csv                 candles of the same asset on the other venue
  ledger/winrate.csv                      win rate per day and layer (archive)
  live/head.json latest.json params.json rev_k<K>.json      what the site reads
  reports/latest.md|json  status.json
"""
import calendar
import csv
import glob
import json
import math
import os
import time

import numpy as np
import pandas as pd

CANDLE_COLS = ["ts", "open", "high", "low", "close", "volume"]


def day(ts):
    return time.strftime("%Y-%m-%d", time.gmtime(int(ts)))


def _atomic_text(path, write):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", newline="") as f:
        write(f)
    os.replace(tmp, path)


def _files(sd, kind, since_ts):
    fs = sorted(glob.glob(os.path.join(sd, kind, "*.csv")))
    if since_ts is not None:
        d0 = day(since_ts)
        fs = [p for p in fs if os.path.basename(p)[:10] >= d0]
    return fs


def read_candles(sd, since_ts=None, kind="candles"):
    rows = []
    for p in _files(sd, kind, since_ts):
        with open(p, newline="") as f:
            rd = csv.reader(f)
            next(rd, None)
            rows += [[int(r[0])] + [float(x) for x in r[1:6]] for r in rd if r]
    rows.sort(key=lambda r: r[0])
    return rows


def write_candles(sd, rows, since_ts=None, kind="candles"):
    """Write the daily files that contain candles with ts >= since_ts (all
    days present in `rows` if since_ts is None)."""
    by = {}
    for r in rows:
        by.setdefault(day(r[0]), []).append(r)
    todo = by if since_ts is None else [m for m in by if m >= day(since_ts)]
    for m in todo:
        def w(f, m=m):
            wr = csv.writer(f, lineterminator="\n")
            wr.writerow(CANDLE_COLS)
            for r in by[m]:
                wr.writerow([int(r[0])] + [repr(float(x)) for x in r[1:6]])
        _atomic_text(os.path.join(sd, kind, m + ".csv"), w)


def read_forecasts(sd, since_ts=None):
    files = _files(sd, "forecasts", since_ts)
    if not files:
        return pd.DataFrame()
    return pd.concat([pd.read_csv(p) for p in files], ignore_index=True)


def write_forecasts(sd, fc, since_ts):
    """Rewrite the daily files for days >= day(since_ts) from `fc` (which must
    contain every row of those days)."""
    if not len(fc):
        return
    key = fc["ts"].map(day)
    for m in sorted(set(key[key >= day(since_ts)])):
        part = fc[key == m]
        _atomic_text(os.path.join(sd, "forecasts", m + ".csv"),
                     lambda f, part=part: part.to_csv(f, index=False, float_format="%.6g", lineterminator="\n"))


def clean(o):
    """NaN / inf are not valid JSON for a browser: turn them into null."""
    if isinstance(o, dict):
        return {k: clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (float, np.floating)):
        return float(o) if math.isfinite(o) else None
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


CALL_COLS = ["made_ts", "for_ts", "k", "side", "typ", "p", "level", "model", "hit"]


def read_calls(sd, since_ts=None):
    files = _files(sd, "calls", since_ts)
    if not files:
        return pd.DataFrame(columns=CALL_COLS)
    return pd.concat([pd.read_csv(p) for p in files], ignore_index=True)


def merge_calls(sd, events):
    """Append new reversal calls and fill in outcomes. A stored call is never
    edited: a call that already exists is left as it is, and an outcome is
    written only once. (The `reversals/` folder next to this one is the
    archive of the first generation of the agent; it is not touched.)"""
    if not events:
        return
    days = {}
    for kind, e in events:
        ts = e["for_ts"] if kind == "new" else e[0]
        days.setdefault(day(ts), []).append((kind, e))
    for d, evs in days.items():
        path = os.path.join(sd, "calls", d + ".csv")
        rows = {}
        if os.path.exists(path):
            for r in pd.read_csv(path).to_dict("records"):
                rows[(int(r["for_ts"]), int(r["k"]), int(r["side"]), int(r["typ"]))] = r
        for kind, e in evs:
            if kind == "new":
                rows.setdefault((e["for_ts"], e["k"], e["side"], e["typ"]), dict(e, hit=np.nan))
            else:
                r = rows.get((e[0], e[1], e[2], e[3]))
                if r is not None and not (r["hit"] == r["hit"]):        # outcome still empty
                    r["hit"] = e[4]
        df = pd.DataFrame([rows[k] for k in sorted(rows)], columns=CALL_COLS)
        _atomic_text(path, lambda f, df=df: df.to_csv(f, index=False, float_format="%.6g", lineterminator="\n"))


LEDGER_COLS = ["day", "layer", "n", "wins", "base", "live"]


def merge_ledger(sd, fresh, today):
    """The win-rate archive. A day is written for good once it is two days
    old (so that every prediction made on it has been judged); until then it
    is recomputed on every run. Returns the whole ledger."""
    path = os.path.join(sd, "ledger", "winrate.csv")
    old = pd.read_csv(path, dtype={"day": str}) if os.path.exists(path) else pd.DataFrame(columns=LEDGER_COLS)
    frozen_before = day(calendar.timegm(time.strptime(today, "%Y-%m-%d")) - 86400)
    keep = old[old["day"] < frozen_before]
    have = set(zip(keep["day"], keep["layer"]))
    add = fresh[[(d, l) not in have for d, l in zip(fresh["day"], fresh["layer"])]] if len(fresh) else fresh
    led = pd.concat([keep, add[LEDGER_COLS]], ignore_index=True) if len(add) else keep
    led = led.sort_values(["day", "layer"]).reset_index(drop=True)
    if len(led):
        _atomic_text(path, lambda f: led.to_csv(f, index=False, float_format="%.6g", lineterminator="\n"))
    return led


def write_json(path, obj, indent=None):
    _atomic_text(path, lambda f: json.dump(clean(obj), f, indent=indent, allow_nan=False,
                                           separators=(",", ":") if indent is None else None))


def read_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def prune(sd, now, keep_forecast_days=180, keep_candle_days=400):
    """Old daily files are dropped so the state branch stays small."""
    for kind, days in (("forecasts", keep_forecast_days), ("calls", keep_forecast_days), ("candles", keep_candle_days),
                       ("xcandles", keep_candle_days)):
        cut = day(now - days * 86400)
        for p in glob.glob(os.path.join(sd, kind, "*.csv")):
            if os.path.basename(p)[:10] < cut:
                os.remove(p)
