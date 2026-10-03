# Weekly review checklist

Read on the `state` branch: `reports/latest.md`, `reports/latest.json`,
`status.json`, `ledger/winrate.csv`; and the recent runs of the `live`
workflow. Open the site once. Then check, in this order:

1. **Is it alive?** No `error` in `status.json`, the scheduled workflow still
   enabled, no streak of failed runs. GitHub runs the schedule only every few
   hours on this account; the site fills the gaps itself, so a staleness of a
   few hours is normal and a full day is not.
2. **Data.** Gap-filled candles in the last 24h; suspicious candles in
   `candles/` (zero volume, extreme range).
3. **Win-rate ledger — the main check.** For every layer: 7-day and 30-day
   rate against its chance level, the trend verdict, and the rate
   `since go-live` against the replayed history before it (a live rate clearly
   below the replay means the design was over-fitted to the past). Report
   every `down`. A layer that has been `flat` for three weeks has used up its
   inputs: say so and propose the next information source.
4. **Reversal agents**, per turn size: hit rate of both call types on 7d / 30d
   against `chance` and (for "turn is in") against `naive_rule`; calls per day
   against the minimum; the threshold each agent picked; whether a widened
   contest ran and who won. The curve in the report shows what each threshold
   would have given.
5. **Candle goal.** Score of the site generator against the `typical` and
   `repeat` baselines on 24h / 7d / 30d; site score vs full-model score (the
   distillation gap should be small); per-candle scores of the chain.
6. **Calibration.** 7d and 30d coverage of the 90% and 50% ranges within about
   0.02 of nominal; every candle of the chain near 0.90.
7. **Colour.** Report it honestly (history: about 51% for the next candle,
   50% further out). Do not tune for it; a sudden jump is a look-ahead bug
   until proven otherwise.
8. **The record.** Spot-check that rows of older days in `forecasts/`,
   `calls/` and `ledger/winrate.csv` are byte-identical to last week's copy
   (git history of the `state` branch): nothing the models said may change.
9. **Learning.** `retrain_log`: refits happening, parameters sane, how often a
   challenger is promoted. Agent weights: has one collapsed or taken over.
   Goal-tuner multipliers stable.
10. **Cost and size.** Duration of a run (seconds; a rebuild takes about 20
    minutes), size of the `state` branch and of `live/*.json`.

Fix what is broken. A change to model logic needs: tests passing
(`pytest`, `tests/parity.mjs` when anything the browser computes changes,
`tests/site.mjs` when the page changes), a `STATE_VERSION` bump if saved
state becomes invalid, and a before/after comparison on the replayed history —
never judge a change on a few hours. Never edit stored candles, stored
predictions, stored calls or the ledger. Never raise a win rate by changing
what counts as a win.
