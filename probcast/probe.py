"""Which public market-data endpoints can the cloud runner reach?

Other venues' prices are candidates for new agents (EXPERIMENTS.md, E14), but
an agent can only use a source that answers from where the engine runs. This
asks each candidate once (per PROBE_V) for two one-minute candles and records
what came back in reports/probe.json. It reads public data only and never
affects a forecast.
"""
import json
import time
import urllib.request

PROBE_V = 1


def _targets(now):
    a, b = now - 600, now
    iso = lambda t: time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t))
    return {
        "binance_perp": ("https://fapi.binance.com/fapi/v1/klines?symbol=ETHUSDT&interval=1m&limit=2", None),
        "binance_spot_data": ("https://data-api.binance.vision/api/v3/klines?symbol=ETHUSDT&interval=1m&limit=2", None),
        "bybit_perp": ("https://api.bybit.com/v5/market/kline?category=linear&symbol=ETHUSDT&interval=1&limit=2", None),
        "okx_swap": ("https://www.okx.com/api/v5/market/history-candles?instId=ETH-USDT-SWAP&bar=1m&limit=2", None),
        "kraken_futures": (f"https://futures.kraken.com/api/charts/v1/trade/PF_ETHUSD/1m?from={a}&to={b}", None),
        "kraken_spot": ("https://api.kraken.com/0/public/OHLC?pair=ETHUSD&interval=1", None),
        "coinbase_adv_perp": (f"https://api.coinbase.com/api/v3/brokerage/market/products/ETH-PERP-INTX/candles?start={a}&end={b}&granularity=ONE_MINUTE", None),
        "coinbase_intx": (f"https://api.international.coinbase.com/api/v1/instruments/ETH-PERP/candles?granularity=ONE_MINUTE&start={iso(a)}&end={iso(b)}", None),
        "hyperliquid": ("https://api.hyperliquid.xyz/info", {"type": "candleSnapshot", "req": {"coin": "ETH", "interval": "1m", "startTime": a * 1000, "endTime": b * 1000}}),
        "dydx": ("https://indexer.dydx.trade/v4/candles/perpetualMarkets/ETH-USD?resolution=1MIN&limit=2", None),
        "gate_perp": ("https://api.gateio.ws/api/v4/futures/usdt/candlesticks?contract=ETH_USDT&interval=1m&limit=2", None),
        "bitfinex_perp": ("https://api-pub.bitfinex.com/v2/candles/trade:1m:tETHF0:USTF0/hist?limit=2", None),
        "deribit_perp": (f"https://www.deribit.com/api/v2/public/get_tradingview_chart_data?instrument_name=ETH-PERPETUAL&resolution=1&start_timestamp={a * 1000}&end_timestamp={b * 1000}", None),
        "bitstamp_spot": ("https://www.bitstamp.net/api/v2/ohlc/ethusd/?step=60&limit=2", None),
    }


def run(now):
    out = {"v": PROBE_V, "at": int(now), "sources": {}}
    for name, (url, body) in _targets(int(now)).items():
        t0 = time.time()
        try:
            req = urllib.request.Request(url, data=None if body is None else json.dumps(body).encode(),
                                         headers={"User-Agent": "probcast-research", "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=8) as r:
                txt = r.read(400).decode("utf-8", "replace")
                res = {"status": r.status, "sample": txt[:160]}
        except Exception as e:
            res = {"status": getattr(e, "code", None), "error": f"{type(e).__name__}: {e}"[:160]}
        res["seconds"] = round(time.time() - t0, 2)
        out["sources"][name] = res
    return out
