"""Candle download. Standard library only.

Source: Coinbase Exchange public market data (no API key; reachable from
GitHub-hosted runners). A candle is identified by its bucket START time in
epoch seconds (UTC). Only CLOSED candles are ever returned.
"""
import json
import time
import urllib.request
from datetime import datetime, timezone

from concurrent.futures import ThreadPoolExecutor
import threading

from .config import GRAN, PRODUCT, X_INST

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


# ---------------------------------------------------------------- the other venue
# OKX public market data (no key). One-minute candles of the same asset as a
# perpetual; only candles the venue has marked complete are returned.
X_BASE = "https://www.okx.com/api/v5/market/history-candles"
_pace, _last = threading.Lock(), [0.0]


def _x_page(a, b, inst):
    """complete candles with a <= ts < b (at most 100 minutes)"""
    with _pace:                                 # the venue allows 20 requests per 2 seconds: stay well below
        wait = _last[0] + 0.15 - time.time()
        if wait > 0:
            time.sleep(wait)
        _last[0] = time.time()
    d = _get(f"{X_BASE}?instId={inst}&bar=1m&after={b * 1000}&before={(a - GRAN) * 1000}&limit=100")
    if str(d.get("code")) != "0":
        raise RuntimeError(f"other venue: {str(d)[:200]}")
    out = []
    for r in d.get("data", []):                 # [ts ms, open, high, low, close, volume, ..., confirm]
        if str(r[-1]) != "1":
            continue
        out.append([int(r[0]) // 1000] + [float(x) for x in r[1:6]])
    return out


def fetch_x(start_ts, end_ts, inst=X_INST, gran=GRAN, now=None, threads=4):
    """Complete candles of the other venue with start_ts <= ts < end_ts, sorted,
    as lists [ts, open, high, low, close, volume]."""
    now = time.time() if now is None else now
    start_ts = int(start_ts) // gran * gran
    pages = [(a, min(a + 100 * gran, end_ts)) for a in range(start_ts, int(end_ts), 100 * gran)]
    out, failed = {}, []

    def one(p):                                 # a page that keeps failing leaves a hole; it is asked for again next run
        try:
            return _x_page(p[0], p[1], inst)
        except Exception as e:
            failed.append(e)
            return []
    with ThreadPoolExecutor(threads) as ex:
        for rows in ex.map(one, pages):
            for r in rows:
                if start_ts <= r[0] < end_ts and r[0] + gran <= now and r[4] > 0:
                    out[r[0]] = r
    if pages and len(failed) == len(pages):
        raise RuntimeError(f"other venue unreachable: {failed[0]}")
    return [out[k] for k in sorted(out)]


def update_x(rows, start_ts, now=None, overlap=3):
    """rows: candles of the other venue already stored. Downloads what is
    missing; stored candles are never rewritten."""
    now = time.time() if now is None else now
    have = {r[0] for r in rows}
    last = rows[-1][0] if rows else None
    s = start_ts if last is None else max(start_ts, last - overlap * GRAN)
    end = int(now) // GRAN * GRAN
    new = [r for r in fetch_x(s, end, now=now, threads=4 if end - s > 6000 else 1) if r[0] not in have]
    return sorted(rows + new, key=lambda r: r[0]), new
