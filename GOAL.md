# The goal

**Generate the next candle so that it matches the candle the market then
prints: colour, direction, body size, wicks.** Keep learning from every candle
until the generated chart and the real chart are as close as they can be.

## How "close" is measured

Every generated candle is compared with the real one the moment it closes
(`probcast/goal.py`, mirrored in `docs/student.js`):

- **body overlap** — overlap / union of the generated body and the real body.
  It is zero whenever the colour is wrong.
- **range overlap** — overlap / union of the generated high–low range and the
  real one.
- **score = 0.5 × body overlap + 0.5 × range overlap.** 1.00 is an identical
  candle.

Two naive generators are scored next to the model on the same candles, and the
model has to beat them:

- `repeat` — the next candle is a copy of the last one
- `typical` — colour of the last candle, sizes = medians of the last hour

## What pulls the team toward the goal, automatically

| mechanism | what it does | cadence |
|---|---|---|
| Hedge weights | agents that forecast badly lose weight, good ones gain | every candle |
| conformal calibration | keeps the 50% / 90% ranges honest when the market shifts | every candle |
| online learners | quantile regression, reach model, HAR volatility take one learning step | every candle |
| goal tuner | learns from the score itself which body / reach size scores best, separately for candles 1 to 5 minutes ahead | every candle |
| cone width | widens or narrows the 90% range of each further-ahead candle until it holds 90% of the time | every candle |
| outcome heads | candles 2 to 5 minutes ahead are refitted on what the market really printed | every cloud run |
| distillation | the live generator in the browser is refitted to the full model | every cloud run |
| refits | GARCH, HMM | every 12 hours |
| champion / challenger | a new tree model replaces the old one only if it wins on unseen data | daily |
| goal keeper | raises an alert when the score drops under the naive baseline, calibration drifts, an agent drags the ensemble, or data goes stale | every cloud run |

## What is and is not achievable (measured, not assumed)

On two months of one-minute ETH-USD candles, forecast strictly before each
candle existed:

- **Size and range are forecastable.** The 90% range contains the close 90.0%
  of the time and the 50% range 50.0%; the model's candle score is about 12%
  above the best naive generator.
- **Colour is not, with candles alone.** Direction is right 50.0% of the time —
  a coin flip. Because body overlap is zero on a wrong colour, this caps the
  score near 0.35 until an agent with real directional information joins.
- The most promising source of that information is order flow (who is hitting
  the bid and the offer), which candles do not contain. That is the job of the
  planned volume / order-flow agents.

- **Several candles ahead.** Five candles are generated at every minute. Their
  shape scores about the same as the first one (size is as forecastable five
  minutes out as one minute out) and their 90% ranges hold about 90% of the
  time, but the price path itself gets less certain with every step: the range
  roughly doubles by the fifth candle.

A score that jumps far above this without a new information source should be
treated as a bug (look-ahead) until proven otherwise.
