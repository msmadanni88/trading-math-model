# ETH-USD 60s candle generator - report

- generated: 2026-11-17 22:01 UTC
- last closed candle: 2026-11-17 22:01 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: colour_confident 0.533 in the last 7 days, -0.052 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.583 (96) | 0.517 (671) [0.480, 0.551] | 0.522 (2879) [0.503, 0.539] | 0.515 (7289) [0.503, 0.526] | 0.517 (4317) [0.502, 0.533] | 0.545 (88) | 0.500 | flat +0.001 (noise 0.032) |
| colour_clear | 0.533 (825) | 0.539 (5648) [0.531, 0.547] | 0.542 (23976) [0.536, 0.548] | 0.524 (59798) [0.519, 0.529] | 0.543 (35560) [0.538, 0.547] | 0.518 (729) | 0.500 | flat +0.002 (noise 0.012) |
| colour_confident | 0.563 (238) | 0.533 (794) [0.506, 0.555] | 0.581 (4478) [0.569, 0.592] | 0.587 (6389) [0.577, 0.598] | 0.587 (6389) [0.577, 0.598] | 0.521 (167) | 0.500 | down -0.052 (noise 0.024) |
| colour_next | 0.529 (1432) | 0.529 (10049) [0.521, 0.536] | 0.531 (42892) [0.527, 0.535] | 0.518 (108609) [0.514, 0.522] | 0.530 (64260) [0.526, 0.533] | 0.514 (1318) | 0.500 | flat -0.003 (noise 0.009) |
| colour_path | 0.502 (20048) | 0.502 (140686) [0.499, 0.504] | 0.502 (600488) [0.501, 0.503] | 0.501 (1520526) [0.500, 0.502] | 0.501 (899640) [0.500, 0.502] | 0.504 (18452) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.549 (82) | 0.567 (187) [0.531, 0.610] | 0.611 (1181) [0.595, 0.628] | 0.623 (1680) [0.606, 0.639] | 0.623 (1680) [0.606, 0.639] | 0.600 (40) | 0.500 | flat -0.049 (noise 0.047) |
| reversal_k13_next | 0.284 (74) | 0.339 (445) [0.306, 0.376] | 0.331 (1859) [0.316, 0.348] | 0.316 (4996) [0.305, 0.325] | 0.327 (2891) [0.316, 0.338] | 0.232 (69) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.548 (42) | 0.605 (339) [0.562, 0.653] | 0.568 (1612) [0.547, 0.590] | 0.575 (3897) [0.563, 0.588] | 0.572 (2425) [0.555, 0.588] | 0.463 (54) | 0.077 | flat +0.030 (noise 0.037) |
| reversal_k3_next | 0.573 (82) | 0.613 (341) [0.574, 0.662] | 0.601 (2483) [0.589, 0.613] | 0.589 (6346) [0.580, 0.598] | 0.591 (3906) [0.580, 0.602] | 0.557 (79) | 0.293 | flat -0.002 (noise 0.037) |
| reversal_k3_now | 0.942 (52) | 0.929 (393) [0.919, 0.939] | 0.932 (1730) [0.922, 0.941] | 0.935 (4356) [0.929, 0.941] | 0.931 (2593) [0.924, 0.938] | 0.950 (40) | 0.293 | flat +0.010 (noise 0.019) |
| reversal_k5_next | 0.478 (69) | 0.501 (447) [0.460, 0.549] | 0.496 (2418) [0.479, 0.514] | 0.487 (5785) [0.476, 0.498] | 0.483 (3795) [0.468, 0.497] | 0.367 (60) | 0.186 | flat -0.023 (noise 0.035) |
| reversal_k5_now | 0.726 (62) | 0.750 (455) [0.716, 0.784] | 0.795 (1711) [0.777, 0.810] | 0.817 (4121) [0.806, 0.827] | 0.804 (2510) [0.790, 0.816] | 0.804 (56) | 0.187 | flat -0.041 (noise 0.032) |
| reversal_k8_next | 0.352 (71) | 0.421 (456) [0.381, 0.465] | 0.405 (2458) [0.391, 0.421] | 0.397 (5888) [0.387, 0.407] | 0.398 (3782) [0.386, 0.410] | 0.367 (79) | 0.121 | flat +0.004 (noise 0.033) |
| reversal_k8_now | 0.589 (56) | 0.658 (380) [0.612, 0.709] | 0.677 (1555) [0.656, 0.698] | 0.696 (3962) [0.683, 0.709] | 0.684 (2375) [0.667, 0.701] | 0.643 (56) | 0.122 | flat -0.033 (noise 0.035) |
| overall | 0.505 (22084) | 0.506 (154662) [0.503, 0.507] | 0.506 (662085) [0.505, 0.507] | 0.504 (1675775) [0.503, 0.505] | 0.505 (992494) [0.504, 0.506] | 0.505 (20351) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06636, 0.09608] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.06636, 'calls_per_day': 145.8, 'win_rate': 0.5357}, {'threshold': 0.09608, 'calls_per_day': 36.3, 'win_rate': 0.5569}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42898, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15321 | 0.347 | 0.534 (15084) | 0.564 (2306) | 0.740 (2541) |
| volatility: normal | 15320 | 0.372 | 0.529 (15261) | 0.601 (1405) | 0.744 (2333) |
| volatility: wild | 15320 | 0.389 | 0.529 (15280) | 0.580 (1065) | 0.759 (2157) |
| session: Asia 00-08 | 15360 | 0.369 | 0.534 (15239) | 0.579 (1666) | 0.747 (2266) |
| session: Europe 08-13 | 9600 | 0.362 | 0.530 (9517) | 0.581 (1177) | 0.746 (1556) |
| session: US 13-21 | 15360 | 0.377 | 0.533 (15261) | 0.597 (1329) | 0.750 (2363) |
| session: late 21-24 | 5641 | 0.364 | 0.516 (5608) | 0.533 (604) | 0.740 (846) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.415 | 0.426 | 0.275 | 0.275 | 0.567 | 0.316 | 0.514 | 1.238 |
| 6h | 360 | 0.389 | 0.382 | 0.290 | 0.339 | 0.528 | 0.285 | 0.493 | 1.218 |
| 24h | 1440 | 0.377 | 0.367 | 0.307 | 0.340 | 0.511 | 0.262 | 0.492 | 1.123 |
| 7d | 10080 | 0.383 | 0.377 | 0.299 | 0.331 | 0.528 | 0.271 | 0.495 | 1.158 |
| 30d | 43200 | 0.370 | 0.364 | 0.283 | 0.314 | 0.531 | 0.266 | 0.475 | 1.249 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.415 / 0.567 / 0.933; 2: 0.370 / 0.417 / 0.800; 3: 0.403 / 0.617 / 0.783; 4: 0.358 / 0.450 / 0.767; 5: 0.414 / 0.650 / 0.800; 6: 0.351 / 0.400 / 0.683; 7: 0.423 / 0.600 / 0.783; 8: 0.406 / 0.533 / 0.800; 9: 0.377 / 0.500 / 0.817; 10: 0.395 / 0.517 / 0.750; 11: 0.397 / 0.517 / 0.783; 12: 0.404 / 0.567 / 0.833; 13: 0.422 / 0.633 / 0.933; 14: 0.392 / 0.550 / 0.933; 15: 0.372 / 0.467 / 1.000
- 6h: 1: 0.389 / 0.528 / 0.892; 2: 0.358 / 0.458 / 0.858; 3: 0.379 / 0.539 / 0.833; 4: 0.359 / 0.455 / 0.856; 5: 0.381 / 0.536 / 0.908; 6: 0.364 / 0.500 / 0.833; 7: 0.380 / 0.542 / 0.914; 8: 0.377 / 0.520 / 0.908; 9: 0.354 / 0.475 / 0.914; 10: 0.370 / 0.492 / 0.878; 11: 0.366 / 0.508 / 0.878; 12: 0.367 / 0.508 / 0.897; 13: 0.372 / 0.511 / 0.939; 14: 0.375 / 0.508 / 0.961; 15: 0.356 / 0.450 / 1.000
- 24h: 1: 0.377 / 0.511 / 0.888; 2: 0.372 / 0.497 / 0.878; 3: 0.377 / 0.524 / 0.868; 4: 0.369 / 0.494 / 0.874; 5: 0.376 / 0.522 / 0.881; 6: 0.370 / 0.512 / 0.867; 7: 0.375 / 0.515 / 0.891; 8: 0.368 / 0.499 / 0.886; 9: 0.361 / 0.476 / 0.888; 10: 0.369 / 0.502 / 0.874; 11: 0.367 / 0.509 / 0.876; 12: 0.370 / 0.513 / 0.884; 13: 0.367 / 0.495 / 0.898; 14: 0.369 / 0.504 / 0.901; 15: 0.365 / 0.490 / 0.894
- 7d: 1: 0.383 / 0.528 / 0.897; 2: 0.368 / 0.487 / 0.898; 3: 0.377 / 0.517 / 0.896; 4: 0.369 / 0.495 / 0.897; 5: 0.371 / 0.502 / 0.900; 6: 0.370 / 0.506 / 0.896; 7: 0.371 / 0.506 / 0.899; 8: 0.372 / 0.509 / 0.900; 9: 0.365 / 0.489 / 0.899; 10: 0.370 / 0.503 / 0.898; 11: 0.371 / 0.513 / 0.898; 12: 0.368 / 0.503 / 0.899; 13: 0.369 / 0.505 / 0.901; 14: 0.368 / 0.502 / 0.902; 15: 0.368 / 0.501 / 0.899
- 30d: 1: 0.370 / 0.531 / 0.897; 2: 0.358 / 0.493 / 0.899; 3: 0.361 / 0.513 / 0.899; 4: 0.356 / 0.497 / 0.899; 5: 0.358 / 0.504 / 0.900; 6: 0.355 / 0.501 / 0.899; 7: 0.356 / 0.499 / 0.900; 8: 0.357 / 0.506 / 0.900; 9: 0.355 / 0.501 / 0.900; 10: 0.356 / 0.503 / 0.900; 11: 0.355 / 0.505 / 0.900; 12: 0.355 / 0.503 / 0.900; 13: 0.354 / 0.499 / 0.900; 14: 0.354 / 0.501 / 0.900; 15: 0.354 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.107 (body 0.069, range 0.146); 'price stays where it was' would score 0.134; colour right 0.567; typical miss of the close 19.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.147 (body 0.098, range 0.196); 'price stays where it was' would score 0.154; colour right 0.480; typical miss of the close 15.4 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.124 (body 0.081, range 0.167); 'price stays where it was' would score 0.122; colour right 0.492; typical miss of the close 14.6 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.128 (body 0.085, range 0.171); 'price stays where it was' would score 0.130; colour right 0.505; typical miss of the close 13.8 bp; chain ended on the right side 0.532 of 671 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.502; typical miss of the close 9.7 bp; chain ended on the right side 0.521 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.1; 2: 0.204 / 5.9; 3: 0.167 / 7.7; 4: 0.133 / 8.1; 5: 0.125 / 8.7; 6: 0.118 / 9.6; 7: 0.111 / 10.0; 8: 0.099 / 10.9; 9: 0.092 / 11.2; 10: 0.090 / 11.5; 11: 0.085 / 11.9; 12: 0.079 / 12.3; 13: 0.073 / 12.9; 14: 0.068 / 13.3; 15: 0.067 / 13.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794873600, labels learned 153715, probability skill vs chance 0.2278, widened contest next: True
  - now: threshold 0.8336, hit rate recent 0.9421 / long run 0.9298
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.269, naive rule 0.467, lift 3.45x
    - 24h: 43 calls (43 a day), hit rate 0.930, chance 0.272, naive rule 0.466, lift 3.41x
    - 7d: 375 calls (54 a day), hit rate 0.928, chance 0.288, naive rule 0.498, lift 3.23x
    - 30d: 1717 calls (57 a day), hit rate 0.932, chance 0.293, naive rule 0.498, lift 3.18x
  - next: threshold 0.5578, hit rate recent 0.5415 / long run 0.6042
    - 6h: 16 calls (65 a day), hit rate 0.500, chance 0.269, lift 1.86x
    - 24h: 88 calls (88 a day), hit rate 0.534, chance 0.272, lift 1.96x
    - 7d: 375 calls (54 a day), hit rate 0.608, chance 0.288, lift 2.11x
    - 30d: 2470 calls (82 a day), hit rate 0.600, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.501; 0.35: 530, 0.526; 0.40: 474, 0.578; 0.45: 407, 0.647; 0.50: 358, 0.692; 0.55: 311, 0.736; 0.60: 261, 0.781; 0.65: 220, 0.811; 0.70: 172, 0.842; 0.75: 138, 0.874; 0.80: 91, 0.906; 0.85: 45, 0.941; 0.90: 4, 0.969
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.433; 0.35: 493, 0.466; 0.40: 391, 0.506; 0.45: 293, 0.541; 0.50: 186, 0.572; 0.55: 81, 0.584; 0.60: 11, 0.640; 0.65: 1, 0.579
- **K=5**: model 1794528000, labels learned 153713, probability skill vs chance 0.2206, widened contest next: True
  - now: threshold 0.6989, hit rate recent 0.7935 / long run 0.7784
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.183, naive rule 0.404, lift 5.08x
    - 24h: 61 calls (61 a day), hit rate 0.770, chance 0.180, naive rule 0.402, lift 4.27x
    - 7d: 447 calls (64 a day), hit rate 0.743, chance 0.183, naive rule 0.408, lift 4.06x
    - 30d: 1722 calls (57 a day), hit rate 0.795, chance 0.186, naive rule 0.408, lift 4.28x
  - next: threshold 0.4527, hit rate recent 0.4143 / long run 0.4973
    - 6h: 17 calls (69 a day), hit rate 0.471, chance 0.183, lift 2.58x
    - 24h: 67 calls (67 a day), hit rate 0.328, chance 0.180, lift 1.82x
    - 7d: 451 calls (64 a day), hit rate 0.479, chance 0.183, lift 2.62x
    - 30d: 2334 calls (78 a day), hit rate 0.497, chance 0.186, lift 2.68x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.419; 0.35: 358, 0.474; 0.40: 290, 0.543; 0.45: 235, 0.603; 0.50: 187, 0.652; 0.55: 150, 0.688; 0.60: 113, 0.736; 0.65: 78, 0.772; 0.70: 48, 0.806; 0.75: 27, 0.838; 0.80: 8, 0.869
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.387; 0.35: 253, 0.426; 0.40: 161, 0.458; 0.45: 64, 0.503; 0.50: 9, 0.547; 0.55: 1, 0.391
- **K=8**: model 1794873600, labels learned 153710, probability skill vs chance 0.1987, widened contest next: True
  - now: threshold 0.5693, hit rate recent 0.6417 / long run 0.6704
    - 6h: 15 calls (62 a day), hit rate 0.733, chance 0.129, naive rule 0.362, lift 5.70x
    - 24h: 63 calls (63 a day), hit rate 0.635, chance 0.120, naive rule 0.327, lift 5.31x
    - 7d: 382 calls (55 a day), hit rate 0.644, chance 0.122, naive rule 0.348, lift 5.26x
    - 30d: 1570 calls (52 a day), hit rate 0.676, chance 0.121, naive rule 0.339, lift 5.59x
  - next: threshold 0.3629, hit rate recent 0.374 / long run 0.4099
    - 6h: 19 calls (78 a day), hit rate 0.421, chance 0.129, lift 3.27x
    - 24h: 85 calls (86 a day), hit rate 0.341, chance 0.120, lift 2.85x
    - 7d: 471 calls (67 a day), hit rate 0.410, chance 0.122, lift 3.35x
    - 30d: 2430 calls (81 a day), hit rate 0.404, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 250, 0.426; 0.35: 196, 0.488; 0.40: 154, 0.533; 0.45: 118, 0.578; 0.50: 84, 0.635; 0.55: 59, 0.668; 0.60: 40, 0.708; 0.65: 23, 0.768; 0.70: 10, 0.814; 0.75: 2, 0.776
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 164, 0.369; 0.35: 84, 0.397; 0.40: 24, 0.431; 0.45: 5, 0.447; 0.50: 1, 0.739
- **K=13**: model 1794873600, labels learned 153705, probability skill vs chance 0.1663, widened contest next: True
  - now: threshold 0.4437, hit rate recent 0.5283 / long run 0.5734
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.083, naive rule 0.318, lift 6.05x
    - 24h: 61 calls (62 a day), hit rate 0.459, chance 0.073, naive rule 0.249, lift 6.32x
    - 7d: 348 calls (50 a day), hit rate 0.578, chance 0.078, naive rule 0.298, lift 7.36x
    - 30d: 1604 calls (53 a day), hit rate 0.569, chance 0.078, naive rule 0.287, lift 7.30x
  - next: threshold 0.2907, hit rate recent 0.2753 / long run 0.3217
    - 6h: 22 calls (92 a day), hit rate 0.318, chance 0.083, lift 3.85x
    - 24h: 76 calls (77 a day), hit rate 0.211, chance 0.073, lift 2.90x
    - 7d: 448 calls (64 a day), hit rate 0.317, chance 0.078, lift 4.04x
    - 30d: 1854 calls (62 a day), hit rate 0.328, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 136, 0.428; 0.35: 99, 0.474; 0.40: 68, 0.534; 0.45: 46, 0.586; 0.50: 32, 0.629; 0.55: 20, 0.657; 0.60: 11, 0.694; 0.65: 3, 0.639; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.335; 0.35: 14, 0.351; 0.40: 2, 0.414; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 24.307 | 0.46% | 0.933 | 0.500 | 0.247 | 0.633 | 0.193 |
| 6h | 28.345 | 2.81% | 0.886 | 0.508 | 0.250 | 0.517 | 0.485 |
| 24h | 22.381 | 3.24% | 0.897 | 0.501 | 0.251 | 0.468 | 0.615 |
| 7d | 23.562 | 4.25% | 0.899 | 0.499 | 0.250 | 0.508 | 0.679 |
| 30d | 17.503 | 4.66% | 0.900 | 0.500 | 0.250 | 0.504 | 0.711 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 24.419 | 24.481 | 24.462 | 24.430 | 25.062 | 25.222 | 24.130 | 24.027 | 24.241 | 24.307 |
| 6h | 29.164 | 28.462 | 28.352 | 28.347 | 28.693 | 28.783 | 28.260 | 28.172 | 28.252 | 28.345 |
| 24h | 23.131 | 22.462 | 22.423 | 22.380 | 22.680 | 22.613 | 22.332 | 22.311 | 22.325 | 22.381 |
| 7d | 24.608 | 23.754 | 23.713 | 23.596 | 24.061 | 23.873 | 23.550 | 23.514 | 23.524 | 23.562 |
| 30d | 18.358 | 17.662 | 17.620 | 17.557 | 17.852 | 17.791 | 17.485 | 17.464 | 17.471 | 17.503 |

## Next candle

- candle starting 2026-11-17 22:01 UTC, last close 1801.36
- P(up) 0.4766, return quantiles (bp): {'05': -14.915, '10': -11.006, '25': -5.555, '40': -2.655, '50': -0.532, '60': 1.773, '75': 5.062, '90': 10.76, '95': 14.033}
- changepoint probability 0.055, regime age 146.0 min
- agent weights: empirical 0.004, ewma 0.103, garch 0.138, har 0.174, bocpd 0.030, hmm 0.041, online_qr 0.228, lgbm 0.283

## Learning log

- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- 2026-11-16 00:00 UTC: {"garch": {"alpha": 0.0649, "beta": 0.9281}, "hmm": {"sd_bp": [5.12, 9.52, 24.14], "stay": [0.982, 0.963, 0.92]}, "lgbm": {"challenger_loss": 0.24944, "champion_loss": 0.2494, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47719, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47655, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3653, "challengers": 1, "chance_loss": 0.4822, "widened": false, "champion_loss": 0.36306, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2714, "challengers": 1, "chance_loss": 0.37579, "widened": false, "champion_loss": 0.27207, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19602, "challengers": 1, "chance_loss": 0.28273, "widened": false, "champion_loss": 0.19594, "promoted": false}}
- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- HMM volatility states (sd, bp per minute): [5.63, 9.77, 23.96], current probabilities: [0.682, 0.306, 0.013]
- live generator: {'versions': 60, 'latest_effective': '2026-11-17 22:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.282, 'l_abs': 0.784, 'l_hi': 0.835, 'l_lo': 0.769, 'b05': 0.716, 'b25': 0.764, 'b75': 0.755, 'b95': 0.697}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [2.263, 3.98, 3.846, 3.129, 6.013, 3.363, 3.676, 4.066, 5.914, 5.737, 4.916, 3.506, 3.433, 5.529]}
- calibration offsets (in sigma): {'05': -0.01, '10': 0.02, '25': 0.02, '40': -0.05, '50': -0.05, '60': -0.01, '75': -0.01, '90': 0.03, '95': -0.0}
