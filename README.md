# Candle generator — self-learning, live (ETH-USD, 1-minute)

A statistical observatory, not a trading system: it holds no funds, places no
orders, and nothing it outputs is investment advice.

- **Live site:** the models draw the next 15 candles and call turning points
  before they happen; the real market is drawn over them and every prediction
  is scored. Source in `docs/`.
- **Goal:** [GOAL.md](GOAL.md) — the win-rate ledger, what each layer predicts,
  and what is realistically achievable.
- **Design and agents:** [ARCHITECTURE.md](ARCHITECTURE.md).
- **Every idea that was tested, kept or rejected:** [EXPERIMENTS.md](EXPERIMENTS.md).
- **Weekly review checklist:** [REVIEW.md](REVIEW.md).

## How it runs

`.github/workflows/live.yml` runs every few minutes on GitHub's servers: it
downloads the candles that closed since the last run, lets every agent learn
from each of them in order, and publishes forecasts, reports and a fresh
version of the live generator to the `state` branch. No server, no PC.

- branch `main`: code (`probcast/`), tests, site (`docs/`)
- branch `state`: `candles/`, `xcandles/` (the same asset on the other venue), `forecasts/`, `calls/` (one CSV per day),
  `ledger/winrate.csv`, `live/` (what the site reads), `reports/latest.md`,
  `status.json`
- the fitted engine is kept in the Actions cache; if it is lost, or
  `STATE_VERSION` in `probcast/engine.py` changes, the next run replays the
  last 60 days (about 20 minutes) and rebuilds everything from the candles

## Honesty rules built into the code

- A forecast is stored before its candle exists; evaluation is always out of sample.
- Features use finite look-back windows; tests prove that changing the future
  never changes a past feature or forecast.
- Stored candles, stored predictions, stored calls and the win-rate ledger are
  never rewritten.
- The browser and the cloud compute predictions with the same functions and
  the same published parameters (`tests/parity.mjs`).
- A candle on the site is the exchange's own, or built from the complete trade
  stream; a stale price is never drawn (`tests/site.mjs`).

## Run locally

    pip install -r requirements.txt pytest
    PARITY_FIXTURE=parity.json python -m pytest -q tests && node tests/parity.mjs parity.json
    python -m probcast.run step --state-dir state --cache-dir cache

    # the page, end to end, against a stand-in exchange (needs `npm i playwright-core ws` and a Chromium)
    node tests/site_mock.mjs docs state/live 8 8765 &
    CHROME=/path/to/chrome node tests/site.mjs http://127.0.0.1:8765
