"""Candle download. Standard library only.

Source: Coinbase Exchange public market data (no API key; reachable from
GitHub-hosted runners). A candle is identified by its bucket START time in
epoch seconds (UTC). Only CLOSED candles are ever returned.
"""
import json
import time
import urllib.request
from datetime import datetime, timezone

from .config import GRAN, PRODUCT

BASE = "https://api.exchange.coinbase.com/products/{p}/candles"
HEADERS = {"User-Agent": "probcast/1.0 (research; public data)", "Accept": "application/json"}


def iso(ts):
    return datetime.fromtimestamp(ts, tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _get(url, retries=6):
    err = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode())
        except Exception as e:  # network, rate limit, bad JSON
            err = e
            time.sleep(1.5 * (i + 1))
    raise RuntimeError(f"fetch failed after {retries} tries: {url}: {err}")


def fetch_range(start_ts, end_ts, product=PRODUCT, gran=GRAN, pause=0.15, now=None, verbose=False):
    """Closed candles with start_ts <= ts < end_ts, sorted, as lists
    [ts, open, high, low, close, volume]."""
    now = time.time() if now is None else now
    start_ts = int(start_ts) // gran * gran
    out = {}
    s = start_ts
    n_req = 0
    while s < end_ts:
        e = min(s + 299 * gran, end_ts - gran)
        if e < s:
            break
        url = f"{BASE.format(p=product)}?granularity={gran}&start={iso(s)}&end={iso(e)}"
        rows = _get(url)
        n_req += 1
        if not isinstance(rows, list):
            raise RuntimeError(f"unexpected response: {str(rows)[:200]}")
        for r in rows:  # [time, low, high, open, close, volume]
            ts = int(r[0])
            if ts < start_ts or ts >= end_ts or ts + gran > now:
                continue
            o, h, l, c, v = float(r[3]), float(r[2]), float(r[1]), float(r[4]), float(r[5])
            if not (h >= max(o, c) - 1e-9 and l <= min(o, c) + 1e-9 and l > 0):
                continue  # malformed bar
            out[ts] = [ts, o, h, l, c, v]
        if verbose and n_req % 25 == 0:
            print(f"  downloaded up to {iso(s)}  total={len(out)}", flush=True)
        s += 300 * gran
        time.sleep(pause)
    return [out[k] for k in sorted(out)]


def update(rows, start_ts, now=None, verbose=False, overlap=3):
    """rows: candles already stored. Downloads what is missing and returns
    (all_rows, new_rows). Stored candles are never rewritten: the models
    already learned from them."""
    now = time.time() if now is None else now
    have = {r[0] for r in rows}
    last = rows[-1][0] if rows else None
    s = start_ts if last is None else max(start_ts, last - overlap * GRAN)
    end = int(now) // GRAN * GRAN          # start of the still-open candle
    new = [r for r in fetch_range(s, end, now=now, verbose=verbose) if r[0] not in have]
    return sorted(rows + new, key=lambda r: r[0]), new
