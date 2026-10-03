# Architecture

```
 exchange (Coinbase public feed)          other venue (OKX public feed): candles of the same asset
      │ candles (REST)                                  trades (websocket)
      ▼                                                       │
┌──────────────────────── cloud: GitHub Actions (scheduled) ──┼───────────────┐
│ data.py ──► store.py (state branch: candles/, forecasts/, calls/, ledger/)  │
│                 │                                           │               │
│            features.py  (41 causal features)                │               │
│                 ▼                                           │               │
│   engine.py  — the ORCHESTRATOR, one loop per candle        │               │
│     blackboard (ctx): features, volatility scale, regime,   │               │
│                       signals from signal agents            │               │
│     ├─ forecast agents ─► Hedge weights ─► conformal calibration            │
│     ├─ shape agent (reach above / below the last close)     │               │
│     ├─ goal tuners (sizes that maximise the candle score)   │               │
│     ├─ per-candle heads + chain builder (student.py)        │               │
│     ├─ reversal agents, one per turn size (agents/reversal.py)              │
│     └─ publishes what the browser needs: live/params.json, live/rev_k*.json │
│   goal.py + report.py — GOAL KEEPER: scores, win-rate ledger, alerts        │
│                 ▼                                           │               │
│   state branch: live/*.json, reports/, ledger/winrate.csv   │               │
└─────────────────┬───────────────────────────────────────────┼───────────────┘
                  ▼                                           ▼
┌──────────────────────── browser: GitHub Pages (docs/) ──────────────────────┐
│ app.js: real candles (the exchange's own, or built from the complete trade  │
│         stream), redrawn each second                                        │
│ student.js: at each minute close, the 15-candle chain and the reversal      │
│             agents' calls, with the parameters published before that minute │
│ chart: prediction, fixed history, match per candle, reversal calls + panel  │
└─────────────────────────────────────────────────────────────────────────────┘
```

Why two places: a free cloud job cannot run every minute, and a static site
cannot train models. So the cloud **learns** (all agents, every candle, in
order) and the browser **acts** in real time with what the cloud last
published. `tests/parity.mjs` proves the browser and the cloud compute the
same chain and the same reversal probabilities (it walks the same trees), and
the cloud stores exactly those as the official record.

## Agents

All agents live in `probcast/agents/` (the per-candle heads and the chain
builder in `probcast/student.py`, because the browser mirrors them). They are
algorithms, not chatbots: they must answer within milliseconds, every minute,
for free.

### Running today

| agent | file | role | its number |
|---|---|---|---|
| empirical | `baseline.py` | benchmark every other forecast agent is measured against | pinball loss |
| ewma, garch, har | `volatility.py` | how big the next candle will be | pinball loss |
| bocpd | `regime.py` | has the market just changed regime (Bayesian changepoint) | pinball loss |
| hmm | `regime.py` | calm / normal / turbulent state | pinball loss |
| online_qr | `learners.py` | linear quantile model, one learning step per candle | pinball loss |
| lgbm | `learners.py` | boosted trees, champion / challenger | pinball loss |
| reach | `shape.py` | how far above and below the last close the candle reaches | candle score |
| orchestrator | `engine.py` | runs the loop, weights the forecast agents (Hedge), calibrates | coverage |
| goal tuners | `engine.py` | turn forecasts into the candle that scores best, one per candle of the chain | candle score |
| per-candle heads | `student.py` | colour and size of each of the next 15 candles, learned from realised candles | `colour_next`, `colour_path` |
| cross-venue | `student.py` (`x_features`, head `HX`), `data.py` (`fetch_x`) | reads the same asset on another venue (the ETH perpetual on OKX), where the price is set a moment earlier: the gap to this market and how much further the other venue has moved. Decides the colour of candle 1 whenever its candle for the closed minute is there; otherwise the head for this market alone speaks, and the record says which (`g_x`) | `colour_next`, `colour_confident`, `colour_strong` |
| colour caller | `agents/colour.py` | which colour calls the model stands behind: two lines on how far P(up) is from 50% (confident, strong), re-drawn to keep a fixed number of calls a day | `colour_confident`, `colour_strong` |
| chain builder | `student.py`, `docs/student.js` | connects the 15 candles and keeps the chain inside the model's own range; frozen every quarter hour as the fixed history | `chain_end_side`, fixed-history match |
| reversal K=3, 5, 8, 13 | `agents/reversal.py` | "the turn is in" and "a turn is coming" for swing points of that size; own tree model, own thresholds, own daily contest | `reversal_k<K>_now`, `_next` |
| live generator | `docs/student.js`, `docs/app.js` | all of the above in the browser, in real time | parity with the cloud |
| goal keeper | `goal.py`, `report.py` | measures every layer, keeps the win-rate ledger, raises alerts | — |

### How agents work together

1. **The blackboard.** Each candle the orchestrator fills `ctx` (features,
   volatility scale, regime state, `ctx["signals"]`); every agent reads from
   it. A signal agent only writes there.
2. **The shared record.** Whatever an agent says is stored before the outcome
   exists — forecast quantiles, generated candles, the frozen chain, reversal
   probabilities and calls (`forecasts/`, `calls/`). Any agent may learn from
   any other agent's stored output, because it is known at that time.
3. **One weighting for interchangeable agents.** Forecast agents are mixed by
   Hedge on their out-of-sample loss; a weak one fades without anyone
   deciding it.
4. **One scoreboard.** Every layer has a line in the win-rate ledger with its
   chance level, its interval and its trend, and the report cuts the main
   numbers by market regime (volatility thirds, time of day). Every idea that
   was tested - kept or thrown away - is written down in EXPERIMENTS.md. An agent or a link between agents earns its
   place only if a ledger layer goes up. (Example of a link that was tested
   and rejected: feeding the reversal agents' probabilities to the colour
   heads did not improve colour, so it is not in the model.)
5. **Escalation.** A falling layer raises an alert; the agent reacts on its
   own first (weights, thresholds, widened contest — see GOAL.md). A layer
   that stays flat needs new information: a new agent.

### Planned (extension points already in place)

| planned agent | kind | where it plugs in | layer it must lift |
|---|---|---|---|
| cross-venue in the full model | signal | the other venue's view appended to the full model's features, so the range forecast moves with it too (EXPERIMENTS.md, E15) | candle score |
| second venue | signal | a second source for the cross-venue agent, so that one outage does not blind it | `colour_*` |
| trade flow | signal | tested on 15 million trades (E13): no lift for colour or turning points, a small one for the high-low range; kept out until a retest on a longer history passes the gate | range overlap |
| meta-learner | supervisor | learns from every agent's stored outputs which agent to trust in which regime | `colour_confident`, `overall` |
| trend | signal + forecast | multi-timeframe trend state on the blackboard | `chain_end_side` |
| volume profile (visible range) | signal | distance to POC / value-area edges | `reversal_*` |
| ML monitor | supervisor | per-agent drift → reset or retrain an agent | all |
| goal reminder | supervisor | extends the goal keeper: forces action when alerts persist | all |
| candle foundation model (Kronos / Chronos) | forecast | another entry in `registry.forecast_agents()` | candle score |
| LLM reviewer | supervisor (slow) | weekly review of reports; proposes code changes with tests | all |

Contracts:

- **forecast agent** → nine quantiles of the next return. Add it to
  `registry.forecast_agents()`; the orchestrator starts weighting it by its
  out-of-sample loss with no other change.
- **signal agent** → `signals(ctx) -> {"name": value}` written to
  `ctx["signals"]` for the others to read. To let the learners use a signal it
  also has to be appended to a feature vector (bump `STATE_VERSION`); if the
  browser must compute it too, it needs a mirror in `docs/student.js` and a
  case in `tests/parity.mjs`.
- **calling agent** (like the reversal agents) → `observe` (judge old calls,
  learn), `probs` (speak with the *published* model), `call`, `tune`,
  `retrain`, `summary`; its calls go to `calls/` and its layer to the ledger.
- **supervisor** → reads the ledger / reports and acts on other agents
  (reweight, reset, retrain). Fast supervisors are code; slow ones can be an
  LLM session reading `reports/latest.json`.

### The record

`forecasts/` holds, for every minute: the candle generated one minute ahead
(`g_*`), its candle in the frozen chain (`lk_*`), how each candle of the chain
generated for it did (`s<h>`, `d<h>`, `c<h>_in`), and what each reversal
model said (`r<K>_*`), and whether the colour call was a confident one
(`g_call`). `calls/` holds every reversal call. `run.py` never
rewrites a stored value of these (`PROTECTED` columns; an empty cell may be
filled once) and `store.merge_calls` never edits a stored call. Columns of
retired designs stay in the files (`g2_*`..`g5_*`, `reversals/`). A decision
about a prediction (`g_call`, `g_x`) is only ever stored with the prediction it was
made about: a rebuild does not attach it to an older stored prediction that
the rebuilt engine would have made differently. The browser
applies the same rule to what it has already shown (kept in local storage),
so a visitor never sees a past prediction move.

### Rules every agent must obey

1. Use only candles that are already closed. `tests/` checks that changing the
   future never changes a stored prediction.
2. Be deterministic: the engine must be rebuildable from the candles alone.
3. Speak only with published parameters: the cloud's record is produced with
   the version that was already public when the minute started, so the site
   and the record cannot disagree.
4. Be judged out of sample: no agent is trusted on its own claims, only on its
   ledger layer.

### The candles on the site

A candle on the chart is the exchange's own candle, or — for the minute in
progress and the few seconds until the exchange publishes a minute that just
closed — built in the browser from the trade stream. Such a candle counts as
exact only if the page heard every trade of that minute (the stream was
running before the minute began, no trade number skipped). Anything else is
replaced by the exchange's numbers before a prediction is made from it, and a
stale price is never carried into a new candle. `tests/site.mjs` checks this
through a reload, a gap in the stream, a frozen tab and a dropped connection.

### The other venue

The cloud downloads the other venue's complete one-minute candles next to this
market's (`xcandles/` on the `state` branch; `probe.py` records once which
venues answer from the cloud runner). The browser asks the same venue directly
at every minute close and waits up to about three seconds for the candle of
the minute that just closed; if it does not come, the prediction is made from
this market alone and marked so. The cloud applies the same rule to its own
record. Neither ever uses a candle the venue has not marked complete.

## Later: more timeframes and assets

`config.py` holds the timeframe (`GRAN`) and the asset (`PRODUCT`); every
window is expressed in candles. Multi-timeframe = one engine per timeframe
writing to its own state folder, plus a signal agent that passes the higher
timeframe's state down to the lower one. Every timeframe gets its own ledger
layers; the pooled win rate is computed over all of them.
