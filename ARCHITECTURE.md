# Architecture

```
 exchange (Coinbase public feed)
      │ candles (REST)                                  trades (websocket)
      ▼                                                       │
┌──────────────────────── cloud: GitHub Actions, every ~5 min ┼───────────────┐
│ data.py ──► store.py (state branch: candles/, forecasts/)   │               │
│                 │                                           │               │
│            features.py  (41 causal features)                │               │
│                 ▼                                           │               │
│   engine.py  — the ORCHESTRATOR, one loop per candle        │               │
│     blackboard (ctx): features, volatility scale, regime,   │               │
│                       signals from signal agents            │               │
│     ├─ forecast agents ─► Hedge weights ─► conformal calibration            │
│     ├─ shape agent (reach above / below the last close)     │               │
│     ├─ goal tuner (sizes that maximise the candle score)    │               │
│     └─ student.py: distil everything into a tiny linear     │               │
│        model the browser can run  ─► live/params.json       │               │
│   goal.py + report.py — GOAL KEEPER: scores, baselines, alerts              │
│                 ▼                                           │               │
│   state branch: live/latest.json, live/params.json, reports/                │
└─────────────────┬───────────────────────────────────────────┼───────────────┘
                  ▼                                           ▼
┌──────────────────────── browser: GitHub Pages (docs/) ──────────────────────┐
│ app.js: real candles built from every trade, redrawn each second            │
│ student.js: at each minute close, generates the next candle with the        │
│             parameter version published before that minute started          │
│ chart: generated candles overlaid on real candles, score per candle         │
└─────────────────────────────────────────────────────────────────────────────┘
```

Why two places: a free cloud job cannot run every minute, and a static site
cannot train models. So the cloud **learns** (all agents, every candle, in
order) and the browser **acts** in real time with what the cloud last
published. `tests/parity.mjs` proves the browser and the cloud compute the same
generated candle, and the cloud stores exactly that candle as the official
record.

## Agents

All agents live in `probcast/agents/` and share one interface
(`agents/base.py`): `observe` (learn from the candle that just closed),
`predict` (forecast the next one), `retrain` (periodic heavier refit). They
are algorithms, not chatbots: they must answer within milliseconds, every
minute, for free.

### Running today

| agent | file | role |
|---|---|---|
| empirical | `baseline.py` | benchmark every other agent is measured against |
| ewma, garch, har | `volatility.py` | how big the next candle will be |
| bocpd | `regime.py` | has the market just changed regime (Bayesian changepoint) |
| hmm | `regime.py` | calm / normal / turbulent state |
| online_qr | `learners.py` | linear quantile model, one learning step per candle |
| lgbm | `learners.py` | boosted trees, champion / challenger |
| reach | `shape.py` | how far above and below the last close the candle reaches |
| orchestrator | `engine.py` | runs the loop, weights the agents (Hedge), calibrates |
| goal tuner | `engine.py` | turns forecasts into the candle that scores best (one per horizon) |
| outcome heads | `student.py` | candles 2-5 minutes ahead, learned from realised candles |
| live generator | `student.py`, `docs/student.js` | real-time modelling in the browser |
| goal keeper | `goal.py`, `report.py` | measures the goal, raises off-track alerts |
| reversal | `agents/reversal.py`, `student.py` | calls swing highs / lows up to 5 minutes ahead; own models (online logit + trees, mixed by Hedge), own goal, own immutable record of calls |

### Planned (extension points already in place)

| planned agent | kind | where it plugs in |
|---|---|---|
| BTC / ETH cross-asset | signal | `registry.signal_agents()`: publishes BTC lead-lag on the blackboard |
| trend | signal + forecast | multi-timeframe trend state on the blackboard |
| volume / order flow | signal + forecast | signed trade volume; needs the trade stream stored going forward |
| volume profile (visible range) | signal | distance to POC / value-area edges |
| ML monitor | supervisor | per-agent loss drift → reset or retrain an agent |
| goal reminder | supervisor | extends the goal keeper: forces action when alerts persist |
| candle foundation model (Kronos / Chronos) | forecast | another entry in `registry.forecast_agents()` |
| LLM reviewer | supervisor (slow) | weekly review of reports; proposes code changes with tests |

Three kinds, three contracts:

- **forecast agent** → returns nine quantiles of the next return. Add it to
  `registry.forecast_agents()`; the orchestrator starts weighting it by its
  out-of-sample loss with no other change.
- **signal agent** → `signals(ctx) -> {"name": value}` written to
  `ctx["signals"]` for the others to read. To let the learners use a signal it
  also has to be appended to the feature vector (bump `STATE_VERSION`).
- **supervisor** → reads the reports / per-agent losses and acts on other
  agents (reweight, reset, retrain). Fast supervisors are code; slow ones can
  be an LLM session reading `reports/latest.json`.

### The fixed record

`forecasts/` holds, for every minute, the candle generated one minute ahead and
the one locked five minutes ahead (`g5_*`, opening offset `g5_o`);
`reversals/` holds every reversal call. `run.py` never rewrites a stored
generated candle (`PROTECTED` columns) and `store.merge_calls` never edits a
stored call. The browser applies the same rule to what it has already shown
(kept in local storage), so a visitor never sees a past forecast move.

### Rules every agent must obey

1. Use only candles that are already closed. `tests/` checks that changing the
   future never changes a stored forecast.
2. Be deterministic: the engine must be rebuildable from the candles alone.
3. Be judged out of sample: no agent is trusted on its own claims, only on its
   loss and on the goal score.

## Later: more timeframes and assets

`config.py` holds the timeframe (`GRAN`) and the asset (`PRODUCT`); every
window is expressed in candles. Multi-timeframe = one engine per timeframe
writing to its own state folder, plus a signal agent that passes the higher
timeframe's state down to the lower one.
