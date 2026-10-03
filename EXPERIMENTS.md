# Experiment registry

Every idea that was tested, kept or thrown away, with the number that decided
it. The rule: a change goes into the model only if a ledger layer goes up
beyond noise in a walk-forward test (the model sees only the past at every
step). An idea that failed stays listed, so it is not tried again by accident
and so its number can be beaten later with new information.

Data unless noted: ETH-USD one-minute candles, August - early October 2026.
`se` = one standard error; `CI` = 90% interval from resampling whole days.

| id | idea | verdict | layer | number that decided it |
|---|---|---|---|---|
| E01 | one direction head per candle of the chain, fitted on realised colours (instead of reading the colour off the range forecast) | **kept** (v5) | `colour_next` | 50.0% → 51.0% over 62 days, 86,303 candles (se 0.17) |
| E02 | boosted trees instead of the linear head for colour | rejected | `colour_next` | no better than the linear head; most confident 10% about the same (52.5%) |
| E03 | feed the reversal agents' probabilities to the colour heads | rejected | `colour_next` | after a confirmed top the next candles are red about half the time; no lift |
| E04 | band rule: the chain may not leave the model's own 50% range | **kept** (v5) | fixed history | a free-running chain misses the price 15 minutes out by 24 bp, the banded chain by 12 bp |
| E05 | chain length | **kept**: 15 | `colour_path`, score | shape advantage halves by candle 17; colour is a coin flip from candle 14; size keeps 3/4 of its correlation at 15 |
| E06 | a linear copy of the reversal model for the browser | rejected | `reversal_*` | hit rate fell to 46-50% from 67-79%; the trees themselves are published instead |
| E07 | reversal agents: one tree model per swing size, calls "turn is in" / "turn coming" | **kept** (v5) | `reversal_k*_now` | 94 / 84 / 71 / 58% for K = 3 / 5 / 8 / 13, chance 29 / 19 / 12 / 8% |
| E08 | one shared call record for both call types | rejected | `reversal_*` | "turn coming" calls crowded out "turn is in" calls below the minimum per day; the types keep separate records |
| E09 | claim a colour only when the head is far from 50%: lines at a fixed number of calls a day | **kept** (v6) | `colour_confident`, `colour_strong` | walk-forward, 55 days: every minute 51.0%; 144 most confident a day 52.6% (CI 51.7-53.6, n 7,487); 72 a day 54.0% (CI 52.8-55.3); 36 a day 54.9% (CI 53.1-56.6, n 1,969). First half / second half: 52.7 / 52.5 and 55.2 / 54.4 |
| E10 | pick the confidence line by its recent win rate (best lower bound over 7, 14 or 30 days) | rejected | `colour_confident` | 51.5% (7 days), 51.2% (14), 51.0% (30) against 52.6% for the plain fixed-rate line: a week of calls cannot tell neighbouring lines apart, the rule chases noise |
| E11 | count a colour call as confident only when the full model's P(up) agrees with the head | rejected | `colour_confident` | agree 53.2% (n 1,204), disagree 51.7% (n 859): inside the noise; over all minutes agreement was not better (50.6% against 51.7%) |
| E12 | colour judged only on candles that really moved (more than half a typical move) | kept as a view | `colour_clear` | 51.5% against 50.3% on the tiny candles: the edge is in the candles that matter |
| E13 | trade flow: who is hitting the bid and the offer. 15.1 million ETH-USD trades since 1 August in 10-second bars; 30 features (signed volume over 1-15 minutes, trade-count imbalance, pressure in the last 10 / 20 / 30 seconds, where in the minute the high and low were made, absorption, price impact, one-sidedness, large prints) | **not shipped** - gate not passed | all | walk-forward, 47 days. `colour_next`: 50.9% with and without (difference -0.04 points, CI -0.4 to +0.4), linear and trees alike. `colour_confident` (144 a day): trees with flow 53.5% against 52.3% for the model as it is: +1.1 points, CI -0.2 to +2.4 - a hint, not beyond noise. `colour_strong`: +1.6, CI -1.2 to +4.6. Reversal agents K=5 and K=13: unchanged at every call rate (for example K=5 "turn is in", 50 a day: 86.1% against 85.3%). Size of the next body: unchanged. High-low range of the next candle: R2 0.133 → 0.142, a small real gain. Reading: what the trades of a minute say about direction is already in that minute's candle. To retest when the history is twice as long (the downloader resumes) |
| E14 | other markets leading this one. One-minute candles since 1 August of BTC and SOL (Coinbase), ETH perpetuals on Binance, Bybit and OKX, ETH spot on OKX. Features: the price gap to this market against its own one-hour median, and how much further the other market moved over the last 1, 3 and 5 minutes | **kept** (v7): the same asset on another venue; BTC and SOL rejected | `colour_next`, `colour_confident`, `colour_strong` | walk-forward, 47 days, against the model as it was. ETH perpetual on OKX: every minute 50.9% → 52.3% (first half 51.8, second half 52.9); confident calls 52.3% → 55.9% (54.8 / 56.6); strong calls 53.3% → 57.8% (56.9 / 58.4). Binance and Bybit perpetuals: the same (every minute +1.5 and +1.6 points, CI +1.1 to +2.0; confident +4.4 and +4.8, CI +3.2 to +5.8). OKX spot: 51.8 / 56.0 / 58.0. BTC (spot and perpetual) and SOL: nothing beyond noise. Only candle 1 gains; candles 2-15, candle size and range do not. Trees on top of it: +0.3. OKX was chosen because it answers both from the cloud runner and from browsers; Binance and Bybit refuse the cloud runner's address. Reading: the price of the same asset is set a moment earlier on the perpetual venues, and this market's last trade of the minute lags it |
| E15 | the other venue's view in the full model (the range forecast and its location, not only the colour of candle 1) | **next** | candle score | the forecast of the next return correlates 0.07 with the outcome when the other venue is read, 0.02 without |

## How an experiment is run

1. Fix the layer and its definition of a win before looking at any result.
2. Walk forward: fit on the past, predict the next block, move on. Never fit
   on the days being judged.
3. Compare with the model as it is, on the same minutes.
4. Report the number with its noise (standard error, or the day-block
   interval when the predictions of one day depend on each other).
5. Check both halves of the period. An edge that lives in one half only is
   not kept.
6. Write the result here whatever it is.

## Why "pending" ideas are in the roadmap in that order

Colour from this market's own candles and trades is at its ceiling (E01, E02,
E13); what lifted it was information from outside this market (E14). The
next steps follow from that: give the other venue's view to the full model
(E15), read a second venue so that one outage does not blind the agent, a
meta-learner over the agents' stored outputs, then order-book depth, which
needs an always-on collector because no free history exists.
