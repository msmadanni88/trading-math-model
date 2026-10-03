# The goal

**Say what the market will do in the next minutes, before it does it — the
next candles (colour, body, wicks) and the turning points — and be right more
often every week.** Every prediction is written down before its outcome
exists, judged when the outcome is known, and archived. The archive of win
rates is the scoreboard; the one rule for every agent is that its win rate
has to go up.

## The win-rate ledger

`ledger/winrate.csv` on the `state` branch: one line per UTC day and layer —
how many predictions were judged and how many were right, next to what chance
would score. A day is written for good once it is two days old. The site and
`reports/latest.md` show, per layer and for everything pooled: the day in
progress, last day, 7 days, 30 days, and the trend (last 7 days against the
7 before).

Every win rate comes with a 90% interval from a day-block bootstrap: whole
days are resampled, because the predictions of one day succeed and fail
together and are not independent coin flips. The trend is called `up` or
`down` only when the change is larger than twice the wider of the two noise
estimates (binomial, and day-to-day); otherwise it is `flat`.

| layer | one prediction | a win |
|---|---|---|
| `colour_next` | the colour of the next candle | same colour as the real candle |
| `colour_confident` | the colour calls the model stands behind: P(up) far enough from 50% to be among its roughly 144 most confident minutes of a day (decided and stored before the candle exists) | same colour |
| `colour_strong` | the strongest of those: roughly the 36 most confident minutes of a day | same colour |
| `colour_clear` | the colour of the next candle, counted only when the real candle moved more than half a typical move | same colour |
| `colour_path` | the colour of each of candles 2–15 of the chain | same colour |
| `chain_end_side` | the frozen chain's last close, above or below its start | the market ended on that side 15 minutes later |
| `reversal_k<K>_now` | "the turn is in": a swing point of size K at the candle that just closed, give or take one | it is confirmed K candles later |
| `reversal_k<K>_next` | "a turn is coming": a swing point of size K in one of the next three candles | it forms there |
| `overall` | every prediction above, pooled (`colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted a second time) | — |

Definitions are fixed. A win rate may not be raised by loosening what counts
as a win or by going quiet: the reversal agents must keep making
`REV_MIN_PER_DAY` calls a day of each kind, the colour caller's lines are set by a fixed
number of calls a day (`COL_PER_DAY`), not by what scored well, and the candle layers predict every
minute. The only legitimate routes up are being pickier among at least that
many calls, learning better, and new information.

The days before a generation of models went live are a replay of history:
the models walked through it minute by minute seeing only the past. That is
an honest test, but the design choices were made by someone who had seen
those days, so the numbers that count are the ones `since go-live`.

## Measured so far (two months of one-minute ETH-USD candles, replay)

**Candle shape and range are forecastable.**
- next candle: match 35.7/100 against 31.1 for the best naive generator; the
  90% range holds the close 90.0% of the time, the 50% range 50.0%
- candles 2–15 of the chain, each judged from its own open: 35.5 falling to
  34.6; their 90% ranges hold 90% of the time

**Colour is the hardest layer - the model knows when it has something to
say, and the same asset on another venue tells it more.**
- next candle, every minute: 52.3% when the cross-venue agent reads the ETH
  perpetual on OKX; 51.0% from this market alone (the generation before the
  per-candle direction head had 50.0%)
- its confident calls (about 144 a day): 55.9% with the other venue, 52.6%
  without; its strong calls (about 36 a day): 57.8% with, 54.9% without -
  walking forward, and in both halves of the period
- candles that really moved (more than half a typical move): 51.5%
- candles 2–15: 50.1%
- tree models did no better than the linear head, and trade flow (15 million
  trades, who hit the bid and the offer) added nothing to the colour of the
  next candle: what a minute's trades say about direction is already in its
  candle (EXPERIMENTS.md, E13). What did help is information that is not in
  this market's own tape: the price of the same asset is set a moment earlier
  on the perpetual venues (E14). BTC and SOL added nothing.

**Turning points are forecastable.** Hit rate of the calls, at about 50 calls
a day each; chance is how often the event happens anyway:

| turn size K | "turn is in" | chance | naive rule | "turn coming" | chance |
|---|---|---|---|---|---|
| 3 | 94% | 29% | 48% | 59% | 29% |
| 5 | 84% | 19% | 39% | 49% | 19% |
| 8 | 71% | 12% | 33% | 40% | 12% |
| 13 | 58% | 8% | 27% | 30% | 8% |

The naive rule is "a candle that makes a fresh K-candle high is the top".
What a turn call does **not** tell: the colour of the following candles. After
a confirmed top the next candles are red about half the time — a turn that
holds is a statement about the extreme, not about direction.

**The price level several minutes out is not forecastable**, and the fixed
history shows it honestly: the frozen 15-candle chain, compared where it
actually stood, matches 12/100 on average (36 for its first candle, 6 for its
fifteenth) — about what a chain that simply stayed at the starting price
would score (13). It ends on the right side of its start 51% of the time.

A number that jumps far above these without a new information source is a
look-ahead bug until proven otherwise.

## Why the chain is 15 candles long

Measured per candle of the chain, walking forward through the history: the
advantage of the model's candle shape over the naive generator halves by about
candle 17, the colour accuracy is indistinguishable from a coin flip from
about candle 14 on, and the size forecast keeps three quarters of its
correlation at candle 15. Fifteen is the last candle where every part of the
prediction still carries measurable information — and it is one quarter hour,
so the fixed history lines up with the clock.

## How "match" is measured (candle score)

Every predicted candle is compared with the real one the moment it closes
(`probcast/goal.py`, mirrored in `docs/student.js`):

- **body overlap** — overlap / union of the predicted body and the real body.
  It is zero whenever the colour is wrong.
- **range overlap** — overlap / union of the predicted high–low range and the
  real one.
- **score = 0.5 × body overlap + 0.5 × range overlap.** 1.00 is an identical
  candle; the site shows it as 1–100.

Two naive generators are scored next to the model on the same candles, and the
model has to beat them: `repeat` (a copy of the last candle) and `typical`
(colour of the last candle, sizes = medians of the last hour).

## The chain of predicted candles

At every minute close the model draws the next 15 candles as one connected
chain: each candle opens where the previous one closed. Colour comes from that
candle's own direction head, size from its own size head, the range for its
close from the cone. One rule keeps the chain honest: it may never walk out of
the model's own 50% range for that minute — a candle that would is drawn in
the other colour. Without that rule, heads that all lean the same way draw a
staircase the model itself does not believe; measured, such a staircase misses
the price level 15 minutes out by 24 bp instead of 12.

On the chart each past blue candle starts from the real close before it (it
was made one minute ahead, from that close); the blue candles right of the
price are the chain, redrawn every minute.

## The fixed history

At the start of every quarter hour the chain is frozen exactly as it stood:
15 candles, stored once, never touched again — not by a later forecast, not
when an older engine copy re-learns a minute, not when the whole engine is
rebuilt (`PROTECTED` columns in `run.py`; first-write-wins in the browser).
The site draws it as its own layer, so what the model said can be compared
with what the market did, even after the market has gone somewhere else.

## What pulls every layer toward its goal, automatically

| mechanism | what it does | cadence |
|---|---|---|
| Hedge weights | forecast agents that predict the range badly lose weight | every candle |
| conformal calibration | keeps the 50% / 90% ranges honest when the market shifts | every candle |
| online learners | quantile regression, reach model, HAR volatility take one step | every candle |
| goal tuner | learns from the score itself which body / reach size scores best, per candle of the chain | every candle |
| cone width | widens or narrows the 90% range of each candle of the chain until it holds 90% | every candle |
| per-candle heads | colour and size of candles 1–15, refitted on what the market really printed | every cloud run |
| distillation | the live generator in the browser is refitted to the full model | every cloud run |
| swing labels | every confirmed swing point is a new training row for the reversal agents | every candle |
| cross-venue head | the head that reads the other venue is refitted on what the market really printed, like the other heads | every cloud run |
| colour caller | re-draws the two lines (confident, strong): the confidence that gave 144 and 36 calls a day over its last 7 days; measures whether confidence still pays | every 6 hours |
| threshold tuning | each reversal agent re-picks the confidence that gave its best hit rate (beyond luck) over its last 7 days, among those keeping the minimum number of calls | every 6 hours |
| refits | GARCH, HMM | every 12 hours |
| champion / challenger | a new tree model replaces the old one only if it wins on two unseen days | daily |
| widened contest | a reversal agent whose recent hit rate has slipped below its long-run level sends three different challengers instead of one | daily, while slipping |
| goal keeper | alerts: a win rate falling beyond noise, an agent below its naive rule or below its minimum calls, calibration drifting, score under the naive baseline, stale data | every cloud run |

## When a win rate stalls

The ledger's trend decides. `flat` means the change is within noise; `down`
is an alert and the agent's own machinery reacts first (re-weighting,
threshold, widened contest). If a layer stays flat for weeks the model has
used up what its inputs contain — the next step is then a new agent with new
information on the blackboard (see ARCHITECTURE.md), measured the same way:
it earns its place only if a ledger layer goes up.
