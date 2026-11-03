# ETH-USD 60s candle generator - report

- generated: 2026-11-03 23:38 UTC
- last closed candle: 2026-11-03 23:38 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.498 (672) [0.476, 0.521] | 0.517 (2878) [0.498, 0.536] | 0.514 (5946) [0.501, 0.527] | 0.517 (2974) [0.499, 0.536] | 0.394 (94) | 0.500 | flat -0.031 (noise 0.027) |
| colour_clear | 0.524 (809) | 0.540 (5488) [0.531, 0.550] | 0.544 (23646) [0.540, 0.549] | 0.521 (48605) [0.515, 0.527] | 0.545 (24367) [0.540, 0.548] | 0.524 (806) | 0.500 | flat -0.008 (noise 0.009) |
| colour_confident | 0.568 (88) | 0.575 (979) [0.564, 0.587] | 0.597 (4516) [0.585, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.641 (92) | 0.500 | flat -0.026 (noise 0.021) |
| colour_next | 0.530 (1434) | 0.531 (9968) [0.525, 0.538] | 0.530 (42837) [0.526, 0.534] | 0.515 (88590) [0.511, 0.519] | 0.530 (44241) [0.526, 0.533] | 0.532 (1414) | 0.500 | flat +0.000 (noise 0.007) |
| colour_path | 0.498 (20076) | 0.502 (139552) [0.500, 0.504] | 0.501 (599718) [0.500, 0.502] | 0.501 (1240260) [0.500, 0.502] | 0.501 (619374) [0.499, 0.502] | 0.505 (19796) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.706 (17) | 0.619 (236) [0.577, 0.663] | 0.633 (1203) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.571 (14) | 0.500 | flat -0.008 (noise 0.040) |
| reversal_k13_next | 0.404 (47) | 0.356 (343) [0.308, 0.402] | 0.323 (1879) [0.310, 0.337] | 0.311 (4086) [0.301, 0.323] | 0.323 (1981) [0.311, 0.336] | 0.422 (64) | 0.077 | flat +0.043 (noise 0.034) |
| reversal_k13_now | 0.471 (51) | 0.581 (422) [0.543, 0.614] | 0.560 (1681) [0.541, 0.579] | 0.572 (3198) [0.558, 0.586] | 0.565 (1726) [0.545, 0.585] | 0.661 (56) | 0.077 | flat +0.035 (noise 0.035) |
| reversal_k3_next | 0.646 (113) | 0.599 (877) [0.587, 0.614] | 0.588 (3052) [0.577, 0.598] | 0.586 (5636) [0.578, 0.596] | 0.585 (3196) [0.575, 0.597] | 0.540 (63) | 0.293 | flat -0.002 (noise 0.025) |
| reversal_k3_now | 0.898 (59) | 0.934 (441) [0.912, 0.958] | 0.934 (1747) [0.924, 0.944] | 0.938 (3567) [0.931, 0.944] | 0.933 (1804) [0.923, 0.943] | 0.902 (51) | 0.293 | flat -0.012 (noise 0.020) |
| reversal_k5_next | 0.564 (55) | 0.543 (392) [0.528, 0.558] | 0.479 (2766) [0.464, 0.494] | 0.482 (4945) [0.471, 0.494] | 0.474 (2955) [0.460, 0.490] | 0.483 (60) | 0.187 | up +0.064 (noise 0.030) |
| reversal_k5_now | 0.803 (66) | 0.822 (443) [0.808, 0.834] | 0.821 (1645) [0.809, 0.832] | 0.829 (3317) [0.820, 0.838] | 0.821 (1706) [0.810, 0.831] | 0.780 (50) | 0.187 | flat +0.002 (noise 0.027) |
| reversal_k8_next | 0.475 (40) | 0.435 (575) [0.411, 0.461] | 0.391 (2808) [0.377, 0.405] | 0.393 (4991) [0.382, 0.404] | 0.391 (2885) [0.378, 0.404] | 0.422 (64) | 0.121 | up +0.056 (noise 0.027) |
| reversal_k8_now | 0.635 (52) | 0.716 (391) [0.680, 0.746] | 0.686 (1596) [0.665, 0.706] | 0.701 (3233) [0.687, 0.716] | 0.689 (1646) [0.667, 0.709] | 0.708 (48) | 0.122 | flat +0.058 (noise 0.036) |
| overall | 0.503 (22089) | 0.507 (154076) [0.504, 0.509] | 0.505 (662607) [0.503, 0.506] | 0.504 (1367769) [0.503, 0.505] | 0.505 (684488) [0.503, 0.506] | 0.509 (21760) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07903, 0.1193] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5299, 'levels': [{'threshold': 0.07903, 'calls_per_day': 140.8, 'win_rate': 0.5783}, {'threshold': 0.1193, 'calls_per_day': 34.2, 'win_rate': 0.6322}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42855, 'rate': 0.5295}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15353 | 0.334 | 0.527 (15071) | 0.576 (2281) | 0.758 (2684) |
| volatility: normal | 15352 | 0.366 | 0.534 (15276) | 0.612 (1566) | 0.743 (2289) |
| volatility: wild | 15353 | 0.381 | 0.528 (15308) | 0.631 (845) | 0.763 (2114) |
| session: Asia 00-08 | 15360 | 0.360 | 0.536 (15245) | 0.603 (1639) | 0.759 (2286) |
| session: Europe 08-13 | 9600 | 0.355 | 0.533 (9495) | 0.594 (1187) | 0.743 (1609) |
| session: US 13-21 | 15360 | 0.367 | 0.527 (15236) | 0.597 (1223) | 0.762 (2331) |
| session: late 21-24 | 5738 | 0.351 | 0.515 (5679) | 0.594 (643) | 0.747 (861) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.319 | 0.339 | 0.212 | 0.212 | 0.500 | 0.240 | 0.397 | 1.300 |
| 6h | 360 | 0.351 | 0.354 | 0.241 | 0.273 | 0.529 | 0.251 | 0.451 | 1.290 |
| 24h | 1440 | 0.372 | 0.370 | 0.276 | 0.314 | 0.531 | 0.265 | 0.478 | 1.225 |
| 7d | 10080 | 0.360 | 0.356 | 0.272 | 0.303 | 0.531 | 0.261 | 0.459 | 1.273 |
| 30d | 43200 | 0.363 | 0.356 | 0.276 | 0.307 | 0.530 | 0.262 | 0.464 | 1.246 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.319 / 0.500 / 0.867; 2: 0.299 / 0.400 / 0.983; 3: 0.329 / 0.567 / 0.817; 4: 0.333 / 0.567 / 0.850; 5: 0.342 / 0.567 / 1.000; 6: 0.297 / 0.367 / 0.867; 7: 0.335 / 0.550 / 0.967; 8: 0.306 / 0.483 / 0.983; 9: 0.311 / 0.483 / 0.983; 10: 0.336 / 0.483 / 0.983; 11: 0.337 / 0.583 / 0.983; 12: 0.315 / 0.533 / 0.933; 13: 0.334 / 0.550 / 0.983; 14: 0.295 / 0.450 / 0.983; 15: 0.324 / 0.533 / 1.000
- 6h: 1: 0.351 / 0.529 / 0.908; 2: 0.362 / 0.546 / 0.933; 3: 0.356 / 0.552 / 0.858; 4: 0.357 / 0.499 / 0.861; 5: 0.353 / 0.504 / 0.931; 6: 0.343 / 0.485 / 0.881; 7: 0.341 / 0.485 / 0.922; 8: 0.333 / 0.457 / 0.922; 9: 0.342 / 0.504 / 0.919; 10: 0.350 / 0.485 / 0.925; 11: 0.352 / 0.521 / 0.939; 12: 0.352 / 0.518 / 0.928; 13: 0.346 / 0.490 / 0.956; 14: 0.343 / 0.462 / 0.950; 15: 0.354 / 0.524 / 0.961
- 24h: 1: 0.372 / 0.531 / 0.897; 2: 0.363 / 0.505 / 0.897; 3: 0.365 / 0.530 / 0.910; 4: 0.362 / 0.492 / 0.913; 5: 0.360 / 0.505 / 0.919; 6: 0.356 / 0.509 / 0.913; 7: 0.360 / 0.498 / 0.929; 8: 0.359 / 0.500 / 0.927; 9: 0.357 / 0.508 / 0.924; 10: 0.357 / 0.486 / 0.930; 11: 0.363 / 0.515 / 0.921; 12: 0.358 / 0.500 / 0.922; 13: 0.359 / 0.497 / 0.926; 14: 0.357 / 0.499 / 0.929; 15: 0.368 / 0.528 / 0.928
- 7d: 1: 0.360 / 0.531 / 0.898; 2: 0.348 / 0.495 / 0.900; 3: 0.350 / 0.510 / 0.899; 4: 0.348 / 0.500 / 0.900; 5: 0.348 / 0.511 / 0.900; 6: 0.345 / 0.506 / 0.900; 7: 0.347 / 0.498 / 0.899; 8: 0.345 / 0.506 / 0.899; 9: 0.346 / 0.505 / 0.899; 10: 0.344 / 0.495 / 0.899; 11: 0.344 / 0.501 / 0.899; 12: 0.344 / 0.497 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.344 / 0.497 / 0.900; 15: 0.346 / 0.508 / 0.900
- 30d: 1: 0.363 / 0.530 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.349 / 0.500 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.348 / 0.499 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.346 / 0.497 / 0.900; 12: 0.348 / 0.501 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.347 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.083 (body 0.043, range 0.122); 'price stays where it was' would score 0.107; colour right 0.467; typical miss of the close 5.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.089 (body 0.053, range 0.126); 'price stays where it was' would score 0.106; colour right 0.485; typical miss of the close 9.2 bp; chain ended on the right side 0.292 of 24 chains; n=360
- 24h: match 0.118 (body 0.079, range 0.157); 'price stays where it was' would score 0.116; colour right 0.506; typical miss of the close 9.2 bp; chain ended on the right side 0.406 of 96 chains; n=1440
- 7d: match 0.123 (body 0.084, range 0.161); 'price stays where it was' would score 0.125; colour right 0.504; typical miss of the close 8.2 bp; chain ended on the right side 0.479 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.2 bp; chain ended on the right side 0.509 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.2; 2: 0.200 / 4.8; 3: 0.168 / 6.4; 4: 0.131 / 6.8; 5: 0.124 / 7.6; 6: 0.114 / 8.2; 7: 0.111 / 8.4; 8: 0.098 / 9.2; 9: 0.089 / 9.2; 10: 0.088 / 9.7; 11: 0.085 / 10.0; 12: 0.076 / 10.4; 13: 0.068 / 10.7; 14: 0.069 / 11.2; 15: 0.062 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 133652, probability skill vs chance 0.2219, widened contest next: False
  - now: threshold 0.8388, hit rate recent 0.9097 / long run 0.9314
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.306, naive rule 0.509, lift 3.27x
    - 24h: 51 calls (51 a day), hit rate 0.902, chance 0.290, naive rule 0.471, lift 3.11x
    - 7d: 427 calls (61 a day), hit rate 0.925, chance 0.292, naive rule 0.497, lift 3.16x
    - 30d: 1735 calls (58 a day), hit rate 0.933, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.5655, hit rate recent 0.5706 / long run 0.5969
    - 6h: 16 calls (65 a day), hit rate 0.500, chance 0.306, lift 1.64x
    - 24h: 64 calls (64 a day), hit rate 0.547, chance 0.290, lift 1.88x
    - 7d: 818 calls (117 a day), hit rate 0.598, chance 0.292, lift 2.04x
    - 30d: 2991 calls (100 a day), hit rate 0.586, chance 0.294, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 534, 0.523; 0.40: 474, 0.580; 0.45: 406, 0.651; 0.50: 355, 0.701; 0.55: 310, 0.743; 0.60: 262, 0.787; 0.65: 220, 0.812; 0.70: 174, 0.844; 0.75: 138, 0.878; 0.80: 92, 0.910; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 500, 0.464; 0.40: 404, 0.500; 0.45: 307, 0.535; 0.50: 198, 0.572; 0.55: 89, 0.572; 0.60: 12, 0.645; 0.65: 1, 0.636
- **K=5**: model 1792540800, labels learned 133650, probability skill vs chance 0.2194, widened contest next: False
  - now: threshold 0.6789, hit rate recent 0.801 / long run 0.8175
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.177, naive rule 0.382, lift 5.13x
    - 24h: 50 calls (50 a day), hit rate 0.780, chance 0.176, naive rule 0.366, lift 4.44x
    - 7d: 435 calls (62 a day), hit rate 0.814, chance 0.187, naive rule 0.412, lift 4.36x
    - 30d: 1628 calls (54 a day), hit rate 0.816, chance 0.188, naive rule 0.406, lift 4.35x
  - next: threshold 0.4497, hit rate recent 0.5155 / long run 0.5097
    - 6h: 14 calls (57 a day), hit rate 0.429, chance 0.177, lift 2.42x
    - 24h: 60 calls (60 a day), hit rate 0.483, chance 0.176, lift 2.75x
    - 7d: 387 calls (55 a day), hit rate 0.535, chance 0.187, lift 2.87x
    - 30d: 2706 calls (90 a day), hit rate 0.479, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 347, 0.492; 0.40: 280, 0.566; 0.45: 230, 0.617; 0.50: 183, 0.665; 0.55: 145, 0.702; 0.60: 110, 0.749; 0.65: 77, 0.787; 0.70: 49, 0.819; 0.75: 29, 0.861; 0.80: 10, 0.880
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.387; 0.35: 255, 0.421; 0.40: 159, 0.460; 0.45: 67, 0.481; 0.50: 12, 0.496; 0.55: 1, 0.457
- **K=8**: model 1793059200, labels learned 133647, probability skill vs chance 0.2042, widened contest next: False
  - now: threshold 0.5738, hit rate recent 0.7004 / long run 0.6929
    - 6h: 7 calls (29 a day), hit rate 1.000, chance 0.119, naive rule 0.329, lift 8.43x
    - 24h: 48 calls (48 a day), hit rate 0.708, chance 0.112, naive rule 0.306, lift 6.31x
    - 7d: 383 calls (55 a day), hit rate 0.713, chance 0.124, naive rule 0.348, lift 5.76x
    - 30d: 1585 calls (53 a day), hit rate 0.683, chance 0.121, naive rule 0.335, lift 5.66x
  - next: threshold 0.3637, hit rate recent 0.4345 / long run 0.418
    - 6h: 11 calls (45 a day), hit rate 0.364, chance 0.119, lift 3.07x
    - 24h: 64 calls (64 a day), hit rate 0.422, chance 0.112, lift 3.76x
    - 7d: 539 calls (77 a day), hit rate 0.440, chance 0.124, lift 3.55x
    - 30d: 2785 calls (93 a day), hit rate 0.390, chance 0.121, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 191, 0.497; 0.40: 150, 0.542; 0.45: 115, 0.590; 0.50: 85, 0.638; 0.55: 61, 0.673; 0.60: 41, 0.704; 0.65: 24, 0.779; 0.70: 12, 0.810; 0.75: 2, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.360; 0.35: 91, 0.386; 0.40: 26, 0.417; 0.45: 5, 0.453; 0.50: 1, 0.667
- **K=13**: model 1793577600, labels learned 133642, probability skill vs chance 0.1921, widened contest next: False
  - now: threshold 0.4505, hit rate recent 0.6143 / long run 0.5719
    - 6h: 13 calls (54 a day), hit rate 0.769, chance 0.096, naive rule 0.300, lift 8.04x
    - 24h: 56 calls (57 a day), hit rate 0.661, chance 0.085, naive rule 0.287, lift 7.81x
    - 7d: 422 calls (60 a day), hit rate 0.583, chance 0.080, naive rule 0.295, lift 7.26x
    - 30d: 1672 calls (56 a day), hit rate 0.562, chance 0.077, naive rule 0.280, lift 7.26x
  - next: threshold 0.2877, hit rate recent 0.3939 / long run 0.3398
    - 6h: 15 calls (63 a day), hit rate 0.267, chance 0.096, lift 2.79x
    - 24h: 64 calls (65 a day), hit rate 0.422, chance 0.085, lift 4.99x
    - 7d: 356 calls (51 a day), hit rate 0.354, chance 0.080, lift 4.41x
    - 30d: 1858 calls (62 a day), hit rate 0.325, chance 0.077, lift 4.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.440; 0.35: 93, 0.492; 0.40: 66, 0.546; 0.45: 44, 0.586; 0.50: 29, 0.648; 0.55: 19, 0.678; 0.60: 10, 0.718; 0.65: 3, 0.702; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.331; 0.35: 13, 0.354; 0.40: 3, 0.415; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.329 | 2.73% | 0.883 | 0.533 | 0.248 | 0.533 | 0.187 |
| 6h | 11.351 | 1.57% | 0.919 | 0.503 | 0.250 | 0.526 | 0.330 |
| 24h | 13.642 | 2.68% | 0.902 | 0.501 | 0.250 | 0.522 | 0.550 |
| 7d | 14.968 | 5.01% | 0.901 | 0.499 | 0.250 | 0.511 | 0.744 |
| 30d | 14.436 | 4.29% | 0.901 | 0.500 | 0.250 | 0.499 | 0.685 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.619 | 10.416 | 10.454 | 10.407 | 10.779 | 10.466 | 10.254 | 10.256 | 10.313 | 10.329 |
| 6h | 11.532 | 11.355 | 11.386 | 11.357 | 11.585 | 11.498 | 11.338 | 11.323 | 11.324 | 11.351 |
| 24h | 14.017 | 13.716 | 13.712 | 13.664 | 13.882 | 13.833 | 13.605 | 13.612 | 13.612 | 13.642 |
| 7d | 15.758 | 15.135 | 15.096 | 15.011 | 15.302 | 15.292 | 14.951 | 14.939 | 14.944 | 14.968 |
| 30d | 15.083 | 14.585 | 14.532 | 14.469 | 14.702 | 14.648 | 14.428 | 14.407 | 14.410 | 14.436 |

## Next candle

- candle starting 2026-11-03 23:38 UTC, last close 2286.75
- P(up) 0.5296, return quantiles (bp): {'05': -6.678, '10': -5.351, '25': -2.589, '40': -0.631, '50': 0.258, '60': 1.143, '75': 2.774, '90': 5.376, '95': 7.019}
- changepoint probability 0.0564, regime age 134.6 min
- agent weights: empirical 0.011, ewma 0.126, garch 0.118, har 0.150, bocpd 0.022, hmm 0.048, online_qr 0.271, lgbm 0.255

## Learning log

- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- HMM volatility states (sd, bp per minute): [2.59, 5.61, 12.38], current probabilities: [0.955, 0.044, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-03 23:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.216, 'l_abs': 0.668, 'l_hi': 0.761, 'l_lo': 0.798, 'b05': 0.742, 'b25': 0.629, 'b75': 0.604, 'b95': 0.717}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.557, 1.988, 2.255, 2.476, 2.509, 2.715, 2.968, 3.091, 3.265, 3.501, 3.06, 3.191, 3.003, 3.177]}
- calibration offsets (in sigma): {'05': 0.0285, '10': -0.013, '25': 0.0025, '40': 0.048, '50': 0.045, '60': 0.022, '75': 0.0175, '90': 0.003, '95': -0.0085}
