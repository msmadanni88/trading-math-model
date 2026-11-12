# ETH-USD 60s candle generator - report

- generated: 2026-11-12 00:43 UTC
- last closed candle: 2026-11-12 00:43 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.531 (672) [0.497, 0.561] | 0.519 (2880) [0.502, 0.537] | 0.514 (6810) [0.502, 0.526] | 0.516 (3838) [0.500, 0.532] | 0.000 (2) | 0.500 | up +0.061 (noise 0.027) |
| colour_clear | 0.517 (842) | 0.546 (5562) [0.533, 0.559] | 0.543 (23911) [0.536, 0.548] | 0.522 (55769) [0.517, 0.528] | 0.543 (31531) [0.538, 0.547] | 0.500 (24) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.507 (67) | 0.567 (947) [0.535, 0.591] | 0.587 (4269) [0.577, 0.598] | 0.592 (5750) [0.581, 0.602] | 0.592 (5750) [0.581, 0.602] | - | 0.500 | flat -0.008 (noise 0.023) |
| colour_next | 0.507 (1439) | 0.531 (9972) [0.520, 0.544] | 0.530 (42869) [0.525, 0.534] | 0.517 (101433) [0.513, 0.521] | 0.529 (57084) [0.525, 0.533] | 0.581 (43) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.508 (20146) | 0.502 (139608) [0.499, 0.505] | 0.502 (600166) [0.500, 0.503] | 0.501 (1420062) [0.500, 0.502] | 0.501 (799176) [0.500, 0.502] | 0.497 (602) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.400 (5) | 0.628 (242) [0.588, 0.648] | 0.620 (1101) [0.604, 0.637] | 0.630 (1513) [0.614, 0.647] | 0.630 (1513) [0.614, 0.647] | - | 0.500 | flat -0.003 (noise 0.046) |
| reversal_k13_next | 0.347 (72) | 0.332 (500) [0.309, 0.355] | 0.326 (1838) [0.312, 0.341] | 0.315 (4696) [0.304, 0.325] | 0.327 (2591) [0.315, 0.338] | 0.000 (1) | 0.077 | flat -0.023 (noise 0.033) |
| reversal_k13_now | 0.577 (52) | 0.577 (350) [0.551, 0.605] | 0.563 (1635) [0.543, 0.582] | 0.574 (3658) [0.561, 0.586] | 0.569 (2186) [0.551, 0.586] | 1.000 (1) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.694 (49) | 0.627 (362) [0.592, 0.659] | 0.591 (2801) [0.579, 0.604] | 0.588 (6102) [0.579, 0.597] | 0.589 (3662) [0.578, 0.600] | 0.000 (2) | 0.293 | flat +0.027 (noise 0.031) |
| reversal_k3_now | 0.912 (57) | 0.920 (412) [0.911, 0.930] | 0.933 (1716) [0.923, 0.944] | 0.935 (4082) [0.929, 0.941] | 0.930 (2319) [0.922, 0.938] | 1.000 (1) | 0.294 | flat -0.007 (noise 0.018) |
| reversal_k5_next | 0.404 (57) | 0.518 (398) [0.477, 0.550] | 0.486 (2650) [0.471, 0.503] | 0.485 (5457) [0.474, 0.496] | 0.480 (3467) [0.466, 0.495] | 0.000 (1) | 0.187 | flat -0.020 (noise 0.036) |
| reversal_k5_now | 0.667 (69) | 0.774 (389) [0.724, 0.821] | 0.808 (1643) [0.791, 0.821] | 0.822 (3805) [0.812, 0.832] | 0.811 (2194) [0.798, 0.824] | 1.000 (1) | 0.187 | flat -0.036 (noise 0.031) |
| reversal_k8_next | 0.429 (70) | 0.423 (466) [0.392, 0.452] | 0.397 (2613) [0.383, 0.411] | 0.396 (5572) [0.386, 0.407] | 0.396 (3466) [0.384, 0.408] | 0.000 (1) | 0.121 | flat -0.014 (noise 0.032) |
| reversal_k8_now | 0.661 (56) | 0.695 (367) [0.675, 0.716] | 0.686 (1524) [0.668, 0.704] | 0.700 (3695) [0.687, 0.713] | 0.690 (2108) [0.672, 0.706] | 1.000 (1) | 0.122 | flat -0.002 (noise 0.034) |
| overall | 0.510 (22163) | 0.506 (153496) [0.503, 0.509] | 0.505 (662335) [0.504, 0.507] | 0.504 (1565372) [0.503, 0.505] | 0.505 (882091) [0.504, 0.506] | 0.500 (656) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0758, 0.1152] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.531, 'levels': [{'threshold': 0.0758, 'calls_per_day': 141.1, 'win_rate': 0.5731}, {'threshold': 0.1152, 'calls_per_day': 35.3, 'win_rate': 0.628}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42868, 'rate': 0.5297}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14895 | 0.346 | 0.533 (14659) | 0.568 (2248) | 0.737 (2521) |
| volatility: normal | 14894 | 0.370 | 0.530 (14830) | 0.607 (1328) | 0.750 (2205) |
| volatility: wild | 14894 | 0.385 | 0.525 (14857) | 0.609 (754) | 0.766 (2018) |
| session: Asia 00-08 | 14923 | 0.367 | 0.535 (14799) | 0.591 (1527) | 0.754 (2219) |
| session: Europe 08-13 | 9300 | 0.361 | 0.532 (9223) | 0.586 (1121) | 0.754 (1511) |
| session: US 13-21 | 14880 | 0.374 | 0.528 (14780) | 0.597 (1135) | 0.749 (2230) |
| session: late 21-24 | 5580 | 0.359 | 0.513 (5544) | 0.554 (547) | 0.730 (784) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.415 | 0.386 | 0.261 | 0.261 | 0.617 | 0.334 | 0.497 | 1.112 |
| 6h | 360 | 0.386 | 0.383 | 0.294 | 0.323 | 0.539 | 0.283 | 0.490 | 1.043 |
| 24h | 1440 | 0.377 | 0.384 | 0.298 | 0.332 | 0.509 | 0.265 | 0.490 | 1.086 |
| 7d | 10080 | 0.370 | 0.365 | 0.281 | 0.312 | 0.531 | 0.266 | 0.474 | 1.348 |
| 30d | 43200 | 0.367 | 0.360 | 0.279 | 0.310 | 0.530 | 0.264 | 0.470 | 1.259 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.415 / 0.617 / 0.900; 2: 0.385 / 0.483 / 0.917; 3: 0.416 / 0.583 / 0.983; 4: 0.421 / 0.533 / 1.000; 5: 0.399 / 0.533 / 1.000; 6: 0.431 / 0.583 / 1.000; 7: 0.393 / 0.500 / 1.000; 8: 0.350 / 0.333 / 1.000; 9: 0.402 / 0.483 / 0.983; 10: 0.402 / 0.550 / 0.983; 11: 0.376 / 0.433 / 0.933; 12: 0.426 / 0.567 / 0.967; 13: 0.411 / 0.550 / 0.967; 14: 0.371 / 0.483 / 0.983; 15: 0.421 / 0.567 / 1.000
- 6h: 1: 0.386 / 0.539 / 0.894; 2: 0.368 / 0.478 / 0.886; 3: 0.386 / 0.519 / 0.894; 4: 0.385 / 0.544 / 0.928; 5: 0.379 / 0.503 / 0.939; 6: 0.380 / 0.517 / 0.933; 7: 0.377 / 0.531 / 0.947; 8: 0.356 / 0.433 / 0.928; 9: 0.365 / 0.472 / 0.942; 10: 0.363 / 0.467 / 0.922; 11: 0.367 / 0.517 / 0.878; 12: 0.374 / 0.503 / 0.897; 13: 0.378 / 0.531 / 0.900; 14: 0.359 / 0.511 / 0.900; 15: 0.376 / 0.528 / 0.900
- 24h: 1: 0.377 / 0.509 / 0.894; 2: 0.368 / 0.500 / 0.896; 3: 0.379 / 0.521 / 0.896; 4: 0.373 / 0.510 / 0.900; 5: 0.374 / 0.510 / 0.904; 6: 0.374 / 0.516 / 0.901; 7: 0.367 / 0.499 / 0.912; 8: 0.369 / 0.497 / 0.905; 9: 0.367 / 0.502 / 0.906; 10: 0.362 / 0.480 / 0.909; 11: 0.375 / 0.536 / 0.901; 12: 0.364 / 0.489 / 0.909; 13: 0.376 / 0.534 / 0.906; 14: 0.363 / 0.498 / 0.905; 15: 0.371 / 0.514 / 0.908
- 7d: 1: 0.370 / 0.531 / 0.895; 2: 0.356 / 0.487 / 0.900; 3: 0.362 / 0.517 / 0.900; 4: 0.356 / 0.497 / 0.901; 5: 0.358 / 0.504 / 0.902; 6: 0.355 / 0.497 / 0.901; 7: 0.355 / 0.500 / 0.901; 8: 0.357 / 0.501 / 0.901; 9: 0.358 / 0.508 / 0.902; 10: 0.356 / 0.504 / 0.901; 11: 0.357 / 0.511 / 0.901; 12: 0.354 / 0.502 / 0.901; 13: 0.354 / 0.498 / 0.902; 14: 0.355 / 0.506 / 0.901; 15: 0.353 / 0.497 / 0.902
- 30d: 1: 0.367 / 0.530 / 0.898; 2: 0.355 / 0.494 / 0.900; 3: 0.358 / 0.511 / 0.901; 4: 0.354 / 0.498 / 0.901; 5: 0.354 / 0.505 / 0.901; 6: 0.353 / 0.501 / 0.901; 7: 0.353 / 0.499 / 0.901; 8: 0.353 / 0.504 / 0.901; 9: 0.353 / 0.504 / 0.901; 10: 0.353 / 0.503 / 0.901; 11: 0.351 / 0.502 / 0.901; 12: 0.352 / 0.502 / 0.901; 13: 0.351 / 0.500 / 0.901; 14: 0.351 / 0.501 / 0.901; 15: 0.351 / 0.502 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.124 (body 0.074, range 0.173); 'price stays where it was' would score 0.134; colour right 0.550; typical miss of the close 13.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.143 (body 0.091, range 0.194); 'price stays where it was' would score 0.139; colour right 0.542; typical miss of the close 11.5 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.143 (body 0.095, range 0.190); 'price stays where it was' would score 0.135; colour right 0.521; typical miss of the close 9.9 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.125 (body 0.083, range 0.166); 'price stays where it was' would score 0.124; colour right 0.504; typical miss of the close 8.9 bp; chain ended on the right side 0.530 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.519 of 2880 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.6; 2: 0.202 / 5.5; 3: 0.168 / 7.1; 4: 0.132 / 7.3; 5: 0.125 / 8.1; 6: 0.116 / 8.9; 7: 0.111 / 9.1; 8: 0.097 / 10.1; 9: 0.091 / 10.2; 10: 0.092 / 10.7; 11: 0.088 / 10.8; 12: 0.080 / 11.1; 13: 0.073 / 11.7; 14: 0.070 / 12.2; 15: 0.067 / 12.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 145237, probability skill vs chance 0.2347, widened contest next: False
  - now: threshold 0.8393, hit rate recent 0.9056 / long run 0.9249
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.296, naive rule 0.524, lift 2.96x
    - 24h: 54 calls (54 a day), hit rate 0.907, chance 0.284, naive rule 0.504, lift 3.20x
    - 7d: 412 calls (59 a day), hit rate 0.920, chance 0.296, naive rule 0.506, lift 3.10x
    - 30d: 1715 calls (57 a day), hit rate 0.933, chance 0.293, naive rule 0.495, lift 3.18x
  - next: threshold 0.5666, hit rate recent 0.6249 / long run 0.6083
    - 6h: 18 calls (73 a day), hit rate 0.722, chance 0.296, lift 2.44x
    - 24h: 51 calls (51 a day), hit rate 0.667, chance 0.284, lift 2.35x
    - 7d: 362 calls (52 a day), hit rate 0.624, chance 0.296, lift 2.11x
    - 30d: 2799 calls (93 a day), hit rate 0.591, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.498; 0.35: 532, 0.523; 0.40: 474, 0.579; 0.45: 406, 0.648; 0.50: 357, 0.695; 0.55: 310, 0.739; 0.60: 261, 0.784; 0.65: 220, 0.811; 0.70: 172, 0.844; 0.75: 138, 0.875; 0.80: 91, 0.905; 0.85: 46, 0.946; 0.90: 4, 0.992
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 497, 0.463; 0.40: 397, 0.501; 0.45: 299, 0.535; 0.50: 192, 0.568; 0.55: 86, 0.579; 0.60: 12, 0.645; 0.65: 1, 0.571
- **K=5**: model 1794441600, labels learned 145235, probability skill vs chance 0.2162, widened contest next: True
  - now: threshold 0.6862, hit rate recent 0.7068 / long run 0.7922
    - 6h: 16 calls (65 a day), hit rate 0.562, chance 0.190, naive rule 0.412, lift 2.96x
    - 24h: 64 calls (64 a day), hit rate 0.688, chance 0.181, naive rule 0.414, lift 3.80x
    - 7d: 389 calls (56 a day), hit rate 0.774, chance 0.186, naive rule 0.409, lift 4.15x
    - 30d: 1642 calls (55 a day), hit rate 0.808, chance 0.186, naive rule 0.405, lift 4.34x
  - next: threshold 0.4589, hit rate recent 0.4398 / long run 0.5091
    - 6h: 19 calls (78 a day), hit rate 0.316, chance 0.190, lift 1.66x
    - 24h: 58 calls (58 a day), hit rate 0.397, chance 0.181, lift 2.19x
    - 7d: 398 calls (57 a day), hit rate 0.515, chance 0.186, lift 2.76x
    - 30d: 2650 calls (88 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 354, 0.480; 0.40: 286, 0.552; 0.45: 233, 0.605; 0.50: 187, 0.654; 0.55: 149, 0.693; 0.60: 112, 0.742; 0.65: 75, 0.779; 0.70: 47, 0.814; 0.75: 28, 0.848; 0.80: 10, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.382; 0.35: 256, 0.422; 0.40: 160, 0.458; 0.45: 65, 0.491; 0.50: 10, 0.508; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 145232, probability skill vs chance 0.2129, widened contest next: False
  - now: threshold 0.5671, hit rate recent 0.6898 / long run 0.6921
    - 6h: 15 calls (62 a day), hit rate 0.600, chance 0.114, naive rule 0.325, lift 5.25x
    - 24h: 51 calls (51 a day), hit rate 0.686, chance 0.123, naive rule 0.365, lift 5.59x
    - 7d: 367 calls (52 a day), hit rate 0.695, chance 0.123, naive rule 0.345, lift 5.66x
    - 30d: 1523 calls (51 a day), hit rate 0.686, chance 0.120, naive rule 0.334, lift 5.70x
  - next: threshold 0.365, hit rate recent 0.4178 / long run 0.4196
    - 6h: 19 calls (78 a day), hit rate 0.211, chance 0.114, lift 1.84x
    - 24h: 71 calls (71 a day), hit rate 0.423, chance 0.123, lift 3.44x
    - 7d: 466 calls (67 a day), hit rate 0.423, chance 0.123, lift 3.45x
    - 30d: 2611 calls (87 a day), hit rate 0.396, chance 0.120, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 192, 0.490; 0.40: 152, 0.536; 0.45: 118, 0.583; 0.50: 84, 0.636; 0.55: 59, 0.674; 0.60: 39, 0.711; 0.65: 24, 0.779; 0.70: 12, 0.815; 0.75: 2, 0.767
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 170, 0.364; 0.35: 87, 0.392; 0.40: 23, 0.424; 0.45: 4, 0.440; 0.50: 1, 0.773
- **K=13**: model 1794355200, labels learned 145227, probability skill vs chance 0.1934, widened contest next: False
  - now: threshold 0.4493, hit rate recent 0.5961 / long run 0.574
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.070, naive rule 0.245, lift 7.19x
    - 24h: 49 calls (50 a day), hit rate 0.592, chance 0.081, naive rule 0.312, lift 7.30x
    - 7d: 347 calls (50 a day), hit rate 0.579, chance 0.080, naive rule 0.296, lift 7.26x
    - 30d: 1635 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.282, lift 7.25x
  - next: threshold 0.2935, hit rate recent 0.3371 / long run 0.3367
    - 6h: 20 calls (83 a day), hit rate 0.200, chance 0.070, lift 2.88x
    - 24h: 71 calls (72 a day), hit rate 0.338, chance 0.081, lift 4.17x
    - 7d: 499 calls (71 a day), hit rate 0.331, chance 0.080, lift 4.14x
    - 30d: 1837 calls (61 a day), hit rate 0.327, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.431; 0.35: 97, 0.479; 0.40: 68, 0.537; 0.45: 46, 0.585; 0.50: 31, 0.639; 0.55: 20, 0.662; 0.60: 12, 0.694; 0.65: 4, 0.673; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.332; 0.35: 13, 0.336; 0.40: 3, 0.405; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.771 | 0.25% | 0.883 | 0.517 | 0.255 | 0.483 | -0.242 |
| 6h | 18.451 | 1.96% | 0.897 | 0.481 | 0.248 | 0.553 | 0.464 |
| 24h | 17.582 | 3.06% | 0.901 | 0.497 | 0.249 | 0.536 | 0.557 |
| 7d | 16.557 | 6.30% | 0.899 | 0.500 | 0.250 | 0.509 | 0.683 |
| 30d | 15.817 | 4.68% | 0.900 | 0.500 | 0.250 | 0.502 | 0.687 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.821 | 19.675 | 19.687 | 19.602 | 20.103 | 19.972 | 19.581 | 19.650 | 19.597 | 19.771 |
| 6h | 18.820 | 18.520 | 18.515 | 18.463 | 18.684 | 18.910 | 18.459 | 18.438 | 18.437 | 18.451 |
| 24h | 18.138 | 17.809 | 17.752 | 17.690 | 17.963 | 17.815 | 17.582 | 17.508 | 17.557 | 17.582 |
| 7d | 17.670 | 16.706 | 16.689 | 16.697 | 16.883 | 16.961 | 16.519 | 16.507 | 16.525 | 16.557 |
| 30d | 16.594 | 15.976 | 15.923 | 15.870 | 16.110 | 16.081 | 15.802 | 15.783 | 15.787 | 15.817 |

## Next candle

- candle starting 2026-11-12 00:43 UTC, last close 2058.3
- P(up) 0.4516, return quantiles (bp): {'05': -10.369, '10': -7.587, '25': -3.974, '40': -2.306, '50': -0.873, '60': 0.965, '75': 4.279, '90': 7.743, '95': 10.761}
- changepoint probability 0.0777, regime age 65.4 min
- agent weights: empirical 0.006, ewma 0.046, garch 0.067, har 0.158, bocpd 0.014, hmm 0.026, online_qr 0.269, lgbm 0.414

## Learning log

- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.15, 5.74, 18.21], current probabilities: [0.022, 0.971, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-11-12 00:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.605, 'l_abs': 0.708, 'l_hi': 0.77, 'l_lo': 0.737, 'b05': 0.711, 'b25': 0.693, 'b75': 0.704, 'b95': 0.703}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6]], 'cone_width': [1.481, 1.746, 1.828, 1.928, 2.248, 2.337, 2.504, 2.456, 2.81, 3.68, 3.348, 3.563, 3.856, 3.92]}
- calibration offsets (in sigma): {'05': 0.051, '10': 0.072, '25': 0.015, '40': -0.072, '50': -0.09, '60': -0.048, '75': 0.035, '90': -0.052, '95': -0.001}
