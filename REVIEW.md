# Weekly review checklist

Read on the `state` branch: `reports/latest.md`, `reports/latest.json`,
`status.json`; and the recent runs of the `live` workflow. Open the site once.
Then check, in this order:

1. **Is it alive?** Staleness under 25 minutes, no `error` in `status.json`,
   the scheduled workflow still enabled, no streak of failed runs. Expect
   roughly 100-290 runs per day (GitHub delays scheduled jobs).
2. **Data.** Gap-filled candles in the last 24h; suspicious candles in
   `candles/` (zero volume, extreme range).
3. **Goal.** Candle score of the site generator against the `typical` and
   `repeat` baselines on 24h / 7d / 30d. Site score vs full-model score (the
   distillation gap should be small). Trend of the score week over week.
4. **Calibration.** 7d and 30d coverage of the 90% and 50% ranges within about
   0.02 of nominal, for both the full model and the site bands.
5. **Skill.** `skill_vs_empirical` positive on 7d / 30d; the ensemble not more
   than about 1% worse than its best agent.
6. **Direction.** Report it honestly (history: 50%). Do not tune for it; a
   sudden jump is a look-ahead bug until proven otherwise.
7. **Reversal agent.** Hit rate of its calls on 7d / 30d against `chance` and
   against `naive_rule` in `reports/latest.json` (it must beat both; beating
   only chance means it has learned nothing beyond "a fresh high is often a
   top"). Number of calls per day (budget is about 8% of minutes per side).
8. **Fixed record.** Spot-check that rows of older days in `forecasts/` and
   `reversals/` are byte-identical to last week's copy (git history of the
   `state` branch): generated columns and calls must never change.
9. **Learning.** `retrain_log`: refits happening, parameters sane, how often
   the tree challenger is promoted. Agent weights: has one collapsed or taken
   over. Goal-tuner multipliers stable.
10. **Cost and size.** Duration of a run (about a minute), size of the `state`
   branch.

Fix what is broken. A change to model logic needs: tests passing (including
`tests/parity.mjs` when the generator changes), a `STATE_VERSION` bump if saved
state becomes invalid, and a before/after comparison on the replayed history —
never judge a change on a few hours. Never edit stored candles or stored
generated candles.
