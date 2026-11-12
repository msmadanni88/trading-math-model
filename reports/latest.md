# ETH-USD 60s candle generator - report

- generated: 2026-11-12 07:46 UTC
- last closed candle: 2026-11-12 07:46 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.531 (672) [0.497, 0.561] | 0.519 (2880) [0.502, 0.537] | 0.514 (6810) [0.502, 0.526] | 0.516 (3838) [0.500, 0.532] | 0.484 (31) | 0.500 | up +0.061 (noise 0.027) |
| colour_clear | 0.517 (842) | 0.546 (5562) [0.533, 0.559] | 0.543 (23911) [0.536, 0.548] | 0.522 (55769) [0.517, 0.528] | 0.543 (31531) [0.538, 0.547] | 0.558 (260) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.507 (67) | 0.567 (947) [0.535, 0.591] | 0.587 (4269) [0.577, 0.598] | 0.592 (5750) [0.581, 0.602] | 0.592 (5750) [0.581, 0.602] | 0.625 (24) | 0.500 | flat -0.008 (noise 0.023) |
| colour_next | 0.507 (1439) | 0.531 (9972) [0.520, 0.544] | 0.530 (42869) [0.525, 0.534] | 0.517 (101433) [0.513, 0.521] | 0.529 (57084) [0.525, 0.533] | 0.537 (464) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.508 (20146) | 0.502 (139608) [0.499, 0.505] | 0.502 (600166) [0.500, 0.503] | 0.501 (1420062) [0.500, 0.502] | 0.501 (799176) [0.500, 0.502] | 0.505 (6496) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.400 (5) | 0.628 (242) [0.588, 0.648] | 0.620 (1101) [0.604, 0.637] | 0.630 (1513) [0.614, 0.647] | 0.630 (1513) [0.614, 0.647] | 0.500 (4) | 0.500 | flat -0.003 (noise 0.046) |
| reversal_k13_next | 0.347 (72) | 0.332 (500) [0.309, 0.355] | 0.326 (1838) [0.312, 0.341] | 0.315 (4696) [0.304, 0.325] | 0.327 (2591) [0.315, 0.338] | 0.304 (23) | 0.077 | flat -0.023 (noise 0.033) |
| reversal_k13_now | 0.577 (52) | 0.577 (350) [0.551, 0.605] | 0.563 (1635) [0.543, 0.582] | 0.574 (3658) [0.561, 0.586] | 0.569 (2186) [0.551, 0.586] | 0.385 (13) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.694 (49) | 0.627 (362) [0.592, 0.659] | 0.591 (2801) [0.579, 0.604] | 0.588 (6102) [0.579, 0.597] | 0.589 (3662) [0.578, 0.600] | 0.542 (24) | 0.293 | flat +0.027 (noise 0.031) |
| reversal_k3_now | 0.912 (57) | 0.920 (412) [0.911, 0.930] | 0.933 (1716) [0.923, 0.944] | 0.935 (4082) [0.929, 0.941] | 0.930 (2319) [0.922, 0.938] | 0.955 (22) | 0.294 | flat -0.007 (noise 0.018) |
| reversal_k5_next | 0.404 (57) | 0.518 (398) [0.477, 0.550] | 0.486 (2650) [0.471, 0.503] | 0.485 (5457) [0.474, 0.496] | 0.480 (3467) [0.466, 0.495] | 0.500 (18) | 0.187 | flat -0.020 (noise 0.036) |
| reversal_k5_now | 0.667 (69) | 0.774 (389) [0.724, 0.821] | 0.808 (1643) [0.791, 0.821] | 0.822 (3805) [0.812, 0.832] | 0.811 (2194) [0.798, 0.824] | 0.667 (15) | 0.187 | flat -0.036 (noise 0.031) |
| reversal_k8_next | 0.429 (70) | 0.423 (466) [0.392, 0.452] | 0.397 (2613) [0.383, 0.411] | 0.396 (5572) [0.386, 0.407] | 0.396 (3466) [0.384, 0.408] | 0.458 (24) | 0.121 | flat -0.014 (noise 0.032) |
| reversal_k8_now | 0.661 (56) | 0.695 (367) [0.675, 0.716] | 0.686 (1524) [0.668, 0.704] | 0.700 (3695) [0.687, 0.713] | 0.690 (2108) [0.672, 0.706] | 0.583 (12) | 0.122 | flat -0.002 (noise 0.034) |
| overall | 0.510 (22163) | 0.506 (153496) [0.503, 0.509] | 0.505 (662335) [0.504, 0.507] | 0.504 (1565372) [0.503, 0.505] | 0.505 (882091) [0.504, 0.506] | 0.508 (7142) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07567, 0.1149] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5319, 'levels': [{'threshold': 0.07567, 'calls_per_day': 142.8, 'win_rate': 0.5752}, {'threshold': 0.1149, 'calls_per_day': 35.8, 'win_rate': 0.6245}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42867, 'rate': 0.5297}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15036 | 0.346 | 0.533 (14798) | 0.568 (2262) | 0.736 (2549) |
| volatility: normal | 15035 | 0.370 | 0.530 (14972) | 0.607 (1334) | 0.749 (2217) |
| volatility: wild | 15035 | 0.385 | 0.525 (14997) | 0.610 (758) | 0.766 (2036) |
| session: Asia 00-08 | 15346 | 0.367 | 0.535 (15220) | 0.592 (1551) | 0.752 (2277) |
| session: Europe 08-13 | 9300 | 0.361 | 0.532 (9223) | 0.586 (1121) | 0.754 (1511) |
| session: US 13-21 | 14880 | 0.374 | 0.528 (14780) | 0.597 (1135) | 0.749 (2230) |
| session: late 21-24 | 5580 | 0.359 | 0.513 (5544) | 0.554 (547) | 0.730 (784) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.367 | 0.357 | 0.273 | 0.273 | 0.467 | 0.290 | 0.444 | 0.937 |
| 6h | 360 | 0.367 | 0.358 | 0.281 | 0.297 | 0.525 | 0.262 | 0.472 | 1.200 |
| 24h | 1440 | 0.381 | 0.381 | 0.295 | 0.325 | 0.523 | 0.272 | 0.489 | 1.091 |
| 7d | 10080 | 0.370 | 0.365 | 0.280 | 0.311 | 0.532 | 0.267 | 0.473 | 1.353 |
| 30d | 43200 | 0.367 | 0.360 | 0.279 | 0.310 | 0.530 | 0.264 | 0.470 | 1.257 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.367 / 0.467 / 0.933; 2: 0.327 / 0.400 / 0.900; 3: 0.364 / 0.550 / 0.900; 4: 0.337 / 0.450 / 0.783; 5: 0.360 / 0.533 / 0.800; 6: 0.342 / 0.433 / 0.817; 7: 0.351 / 0.467 / 0.850; 8: 0.391 / 0.617 / 0.783; 9: 0.364 / 0.517 / 0.750; 10: 0.337 / 0.467 / 0.817; 11: 0.400 / 0.633 / 0.933; 12: 0.387 / 0.567 / 0.950; 13: 0.344 / 0.483 / 0.933; 14: 0.355 / 0.450 / 0.917; 15: 0.366 / 0.483 / 0.917
- 6h: 1: 0.367 / 0.525 / 0.903; 2: 0.346 / 0.478 / 0.903; 3: 0.350 / 0.475 / 0.906; 4: 0.353 / 0.503 / 0.858; 5: 0.351 / 0.478 / 0.844; 6: 0.354 / 0.508 / 0.864; 7: 0.363 / 0.500 / 0.872; 8: 0.370 / 0.550 / 0.867; 9: 0.366 / 0.545 / 0.847; 10: 0.347 / 0.453 / 0.872; 11: 0.386 / 0.598 / 0.939; 12: 0.354 / 0.500 / 0.917; 13: 0.364 / 0.525 / 0.922; 14: 0.348 / 0.489 / 0.922; 15: 0.363 / 0.511 / 0.928
- 24h: 1: 0.381 / 0.523 / 0.894; 2: 0.362 / 0.482 / 0.910; 3: 0.379 / 0.526 / 0.904; 4: 0.371 / 0.507 / 0.899; 5: 0.371 / 0.499 / 0.896; 6: 0.371 / 0.511 / 0.899; 7: 0.370 / 0.510 / 0.903; 8: 0.372 / 0.511 / 0.905; 9: 0.371 / 0.519 / 0.903; 10: 0.361 / 0.473 / 0.903; 11: 0.382 / 0.552 / 0.916; 12: 0.365 / 0.479 / 0.915; 13: 0.379 / 0.541 / 0.913; 14: 0.362 / 0.488 / 0.911; 15: 0.374 / 0.518 / 0.915
- 7d: 1: 0.370 / 0.532 / 0.896; 2: 0.355 / 0.485 / 0.902; 3: 0.361 / 0.517 / 0.902; 4: 0.356 / 0.497 / 0.901; 5: 0.357 / 0.503 / 0.899; 6: 0.354 / 0.496 / 0.900; 7: 0.354 / 0.497 / 0.900; 8: 0.357 / 0.502 / 0.901; 9: 0.357 / 0.508 / 0.900; 10: 0.356 / 0.502 / 0.901; 11: 0.358 / 0.514 / 0.902; 12: 0.353 / 0.501 / 0.902; 13: 0.354 / 0.499 / 0.902; 14: 0.354 / 0.505 / 0.902; 15: 0.353 / 0.498 / 0.903
- 30d: 1: 0.367 / 0.530 / 0.897; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.498 / 0.900; 5: 0.354 / 0.505 / 0.900; 6: 0.352 / 0.501 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.353 / 0.504 / 0.900; 9: 0.353 / 0.504 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.351 / 0.502 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.351 / 0.500 / 0.900; 14: 0.351 / 0.501 / 0.900; 15: 0.351 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.164 (body 0.108, range 0.220); 'price stays where it was' would score 0.152; colour right 0.667; typical miss of the close 6.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.130 (body 0.089, range 0.171); 'price stays where it was' would score 0.137; colour right 0.531; typical miss of the close 7.6 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.137 (body 0.090, range 0.183); 'price stays where it was' would score 0.140; colour right 0.530; typical miss of the close 9.7 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.125 (body 0.084, range 0.166); 'price stays where it was' would score 0.125; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.502; typical miss of the close 8.9 bp; chain ended on the right side 0.520 of 2880 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.7; 2: 0.202 / 5.4; 3: 0.168 / 7.0; 4: 0.132 / 7.2; 5: 0.126 / 8.0; 6: 0.116 / 8.8; 7: 0.111 / 9.1; 8: 0.098 / 10.0; 9: 0.091 / 10.2; 10: 0.093 / 10.6; 11: 0.089 / 10.7; 12: 0.080 / 11.1; 13: 0.074 / 11.6; 14: 0.071 / 12.1; 15: 0.067 / 12.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 145660, probability skill vs chance 0.2333, widened contest next: False
  - now: threshold 0.8395, hit rate recent 0.9183 / long run 0.9258
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.304, naive rule 0.468, lift 3.10x
    - 24h: 55 calls (55 a day), hit rate 0.927, chance 0.292, naive rule 0.499, lift 3.18x
    - 7d: 419 calls (60 a day), hit rate 0.921, chance 0.299, naive rule 0.508, lift 3.09x
    - 30d: 1723 calls (57 a day), hit rate 0.933, chance 0.294, naive rule 0.495, lift 3.18x
  - next: threshold 0.567, hit rate recent 0.6138 / long run 0.6077
    - 6h: 20 calls (81 a day), hit rate 0.600, chance 0.304, lift 1.97x
    - 24h: 59 calls (59 a day), hit rate 0.661, chance 0.292, lift 2.26x
    - 7d: 362 calls (52 a day), hit rate 0.619, chance 0.299, lift 2.07x
    - 30d: 2776 calls (93 a day), hit rate 0.591, chance 0.294, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 533, 0.524; 0.40: 474, 0.579; 0.45: 407, 0.649; 0.50: 357, 0.695; 0.55: 310, 0.740; 0.60: 261, 0.784; 0.65: 220, 0.811; 0.70: 173, 0.844; 0.75: 138, 0.875; 0.80: 91, 0.905; 0.85: 46, 0.946; 0.90: 4, 0.993
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.430; 0.35: 497, 0.464; 0.40: 397, 0.501; 0.45: 300, 0.535; 0.50: 192, 0.567; 0.55: 86, 0.578; 0.60: 12, 0.646; 0.65: 1, 0.591
- **K=5**: model 1794441600, labels learned 145658, probability skill vs chance 0.215, widened contest next: True
  - now: threshold 0.6867, hit rate recent 0.6905 / long run 0.7888
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.204, naive rule 0.395, lift 2.86x
    - 24h: 54 calls (54 a day), hit rate 0.722, chance 0.192, naive rule 0.421, lift 3.77x
    - 7d: 389 calls (56 a day), hit rate 0.769, chance 0.187, naive rule 0.411, lift 4.10x
    - 30d: 1640 calls (55 a day), hit rate 0.807, chance 0.186, naive rule 0.406, lift 4.33x
  - next: threshold 0.451, hit rate recent 0.4578 / long run 0.5097
    - 6h: 14 calls (57 a day), hit rate 0.500, chance 0.204, lift 2.45x
    - 24h: 57 calls (57 a day), hit rate 0.456, chance 0.192, lift 2.38x
    - 7d: 395 calls (56 a day), hit rate 0.516, chance 0.187, lift 2.75x
    - 30d: 2644 calls (88 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.420; 0.35: 354, 0.480; 0.40: 287, 0.551; 0.45: 234, 0.605; 0.50: 187, 0.653; 0.55: 150, 0.691; 0.60: 112, 0.741; 0.65: 75, 0.777; 0.70: 47, 0.815; 0.75: 28, 0.847; 0.80: 10, 0.869
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.382; 0.35: 256, 0.422; 0.40: 161, 0.457; 0.45: 65, 0.492; 0.50: 10, 0.503; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 145655, probability skill vs chance 0.2114, widened contest next: False
  - now: threshold 0.5672, hit rate recent 0.6626 / long run 0.6894
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.130, naive rule 0.338, lift 3.42x
    - 24h: 45 calls (45 a day), hit rate 0.689, chance 0.129, naive rule 0.375, lift 5.34x
    - 7d: 366 calls (52 a day), hit rate 0.689, chance 0.123, naive rule 0.346, lift 5.59x
    - 30d: 1519 calls (51 a day), hit rate 0.685, chance 0.121, naive rule 0.335, lift 5.68x
  - next: threshold 0.3658, hit rate recent 0.4336 / long run 0.4218
    - 6h: 18 calls (74 a day), hit rate 0.444, chance 0.130, lift 3.42x
    - 24h: 72 calls (73 a day), hit rate 0.458, chance 0.129, lift 3.55x
    - 7d: 474 calls (68 a day), hit rate 0.420, chance 0.123, lift 3.41x
    - 30d: 2615 calls (87 a day), hit rate 0.397, chance 0.121, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.428; 0.35: 193, 0.490; 0.40: 152, 0.535; 0.45: 118, 0.582; 0.50: 84, 0.635; 0.55: 59, 0.672; 0.60: 39, 0.711; 0.65: 24, 0.775; 0.70: 12, 0.813; 0.75: 2, 0.767
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 170, 0.364; 0.35: 87, 0.393; 0.40: 23, 0.426; 0.45: 4, 0.432; 0.50: 1, 0.773
- **K=13**: model 1794355200, labels learned 145650, probability skill vs chance 0.1896, widened contest next: False
  - now: threshold 0.4488, hit rate recent 0.5499 / long run 0.5692
    - 6h: 9 calls (38 a day), hit rate 0.444, chance 0.065, naive rule 0.240, lift 6.81x
    - 24h: 47 calls (47 a day), hit rate 0.553, chance 0.080, naive rule 0.313, lift 6.91x
    - 7d: 346 calls (50 a day), hit rate 0.569, chance 0.079, naive rule 0.294, lift 7.20x
    - 30d: 1631 calls (54 a day), hit rate 0.560, chance 0.078, naive rule 0.283, lift 7.21x
  - next: threshold 0.2943, hit rate recent 0.3312 / long run 0.3361
    - 6h: 17 calls (71 a day), hit rate 0.294, chance 0.065, lift 4.51x
    - 24h: 70 calls (71 a day), hit rate 0.314, chance 0.080, lift 3.93x
    - 7d: 500 calls (72 a day), hit rate 0.326, chance 0.079, lift 4.12x
    - 30d: 1836 calls (61 a day), hit rate 0.327, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.430; 0.35: 97, 0.479; 0.40: 67, 0.537; 0.45: 46, 0.581; 0.50: 31, 0.639; 0.55: 20, 0.658; 0.60: 12, 0.689; 0.65: 4, 0.667; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.334; 0.35: 13, 0.332; 0.40: 3, 0.405; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.476 | 0.36% | 0.933 | 0.350 | 0.253 | 0.500 | 0.115 |
| 6h | 12.963 | 1.73% | 0.911 | 0.503 | 0.250 | 0.528 | 0.366 |
| 24h | 17.298 | 3.09% | 0.901 | 0.502 | 0.249 | 0.544 | 0.573 |
| 7d | 16.602 | 6.27% | 0.900 | 0.500 | 0.250 | 0.510 | 0.682 |
| 30d | 15.779 | 4.69% | 0.900 | 0.500 | 0.250 | 0.502 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.524 | 13.455 | 13.443 | 13.601 | 13.579 | 13.490 | 13.417 | 13.399 | 13.429 | 13.476 |
| 6h | 13.192 | 12.979 | 13.001 | 12.984 | 13.101 | 13.198 | 12.924 | 12.900 | 12.924 | 12.963 |
| 24h | 17.850 | 17.528 | 17.494 | 17.373 | 17.703 | 17.591 | 17.285 | 17.217 | 17.272 | 17.298 |
| 7d | 17.712 | 16.751 | 16.736 | 16.740 | 16.933 | 17.014 | 16.562 | 16.551 | 16.568 | 16.602 |
| 30d | 16.556 | 15.938 | 15.885 | 15.831 | 16.072 | 16.047 | 15.763 | 15.745 | 15.749 | 15.779 |

## Next candle

- candle starting 2026-11-12 07:46 UTC, last close 2046.18
- P(up) 0.4657, return quantiles (bp): {'05': -6.706, '10': -5.155, '25': -2.554, '40': -1.101, '50': -0.282, '60': 0.558, '75': 2.695, '90': 5.051, '95': 6.747}
- changepoint probability 0.0401, regime age 240.3 min
- agent weights: empirical 0.015, ewma 0.089, garch 0.097, har 0.155, bocpd 0.033, hmm 0.031, online_qr 0.258, lgbm 0.322

## Learning log

- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.15, 5.74, 18.21], current probabilities: [0.027, 0.966, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-11-12 07:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.47, 'l_abs': 0.681, 'l_hi': 0.751, 'l_lo': 0.713, 'b05': 0.714, 'b25': 0.683, 'b75': 0.716, 'b95': 0.706}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.6], [1.5, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.5, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.332, 1.602, 2.404, 2.86, 2.84, 2.781, 2.979, 3.57, 3.412, 2.604, 2.893, 3.018, 3.201, 3.065]}
- calibration offsets (in sigma): {'05': 0.0325, '10': 0.005, '25': 0.0025, '40': -0.03, '50': -0.045, '60': -0.06, '75': 0.0375, '90': -0.015, '95': -0.0325}
