# Candle generator — self-learning, live (ETH-USD, 1-minute)

A statistical observatory, not a trading system: it holds no funds, places no
orders, and nothing it outputs is investment advice.

- **Live site:** the model draws the next candle before the minute starts; the
  real market is drawn over it and scored. Source in `docs/`.
- **Goal:** [GOAL.md](GOAL.md) — what "matching the real candle" means and what
  is realistically achievable.
- **Design and agents:** [ARCHITECTURE.md](ARCHITECTURE.md).
- **Weekly review checklist:** [REVIEW.md](REVIEW.md).

## How it runs

`.github/workflows/live.yml` runs every few minutes on GitHub's servers: it
downloads the candles that closed since the last run, lets every agent learn
from each of them in order, and publishes forecasts, reports and a fresh
version of the live generator to the `state` branch. No server, no PC.

- branch `main`: code (`probcast/`), tests, site (`docs/`)
- branch `state`: `candles/`, `forecasts/` (one CSV per day), `live/` (what the
  site reads), `reports/latest.md`, `status.json`
- the fitted engine is kept in the Actions cache; if it is lost, or
  `STATE_VERSION` in `probcast/engine.py` changes, the next run replays the
  last 60 days (about 6 minutes) and rebuilds everything from the candles

## Honesty rules built into the code

- A forecast is stored before its candle exists; evaluation is always out of sample.
- Features use finite look-back windows; tests prove that changing the future
  never changes a past feature or forecast.
- Stored candles and stored generated candles are never rewritten.
- The browser and the cloud generate candles with the same function and the
  same published parameters (`tests/parity.mjs`).

## Run locally

    pip install -r requirements.txt pytest
    PARITY_FIXTURE=parity.json python -m pytest -q tests && node tests/parity.mjs parity.json
    python -m probcast.run step --state-dir state --cache-dir cache
