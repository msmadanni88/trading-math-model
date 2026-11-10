# ETH-USD 60s candle generator - report

- generated: 2026-11-10 18:36 UTC
- last closed candle: 2026-11-10 18:36 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.516 (672) [0.478, 0.554] | 0.519 (2879) [0.502, 0.537] | 0.514 (6618) [0.503, 0.526] | 0.517 (3646) [0.500, 0.534] | 0.460 (74) | 0.500 | flat +0.018 (noise 0.027) |
| colour_clear | 0.531 (791) | 0.538 (5545) [0.519, 0.556] | 0.543 (23828) [0.537, 0.549] | 0.522 (54150) [0.517, 0.528] | 0.543 (29912) [0.538, 0.548] | 0.554 (614) | 0.500 | flat -0.002 (noise 0.012) |
| colour_confident | 0.640 (50) | 0.585 (995) [0.572, 0.608] | 0.591 (4371) [0.582, 0.601] | 0.595 (5595) [0.585, 0.606] | 0.595 (5595) [0.585, 0.606] | 0.464 (69) | 0.500 | flat +0.010 (noise 0.022) |
| colour_next | 0.529 (1436) | 0.531 (9970) [0.519, 0.544] | 0.530 (42849) [0.526, 0.534] | 0.517 (98560) [0.513, 0.521] | 0.530 (54211) [0.526, 0.534] | 0.524 (1110) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.503 (139580) [0.501, 0.504] | 0.502 (599886) [0.500, 0.503] | 0.501 (1379840) [0.500, 0.502] | 0.501 (758954) [0.500, 0.502] | 0.495 (15540) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.500 (2) | 0.616 (263) [0.560, 0.634] | 0.623 (1161) [0.607, 0.638] | 0.630 (1493) [0.614, 0.647] | 0.630 (1493) [0.614, 0.647] | 0.889 (9) | 0.500 | flat -0.003 (noise 0.044) |
| reversal_k13_next | 0.358 (67) | 0.331 (465) [0.305, 0.361] | 0.324 (1833) [0.309, 0.338] | 0.313 (4551) [0.303, 0.323] | 0.325 (2446) [0.313, 0.336] | 0.358 (53) | 0.077 | flat -0.025 (noise 0.034) |
| reversal_k13_now | 0.537 (41) | 0.575 (360) [0.547, 0.605] | 0.559 (1641) [0.540, 0.578] | 0.573 (3558) [0.560, 0.586] | 0.567 (2086) [0.549, 0.585] | 0.641 (39) | 0.077 | flat -0.006 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.615 (369) [0.582, 0.646] | 0.591 (2864) [0.580, 0.603] | 0.588 (6005) [0.579, 0.597] | 0.589 (3565) [0.578, 0.599] | 0.605 (38) | 0.294 | flat +0.017 (noise 0.030) |
| reversal_k3_now | 0.909 (55) | 0.919 (396) [0.910, 0.930] | 0.933 (1725) [0.922, 0.943] | 0.936 (3963) [0.930, 0.942] | 0.931 (2200) [0.923, 0.940] | 0.938 (48) | 0.294 | flat -0.015 (noise 0.018) |
| reversal_k5_next | 0.513 (37) | 0.524 (393) [0.498, 0.550] | 0.487 (2679) [0.472, 0.504] | 0.485 (5338) [0.474, 0.497] | 0.480 (3348) [0.466, 0.495] | 0.553 (47) | 0.187 | flat -0.019 (noise 0.036) |
| reversal_k5_now | 0.641 (39) | 0.791 (349) [0.749, 0.826] | 0.813 (1607) [0.800, 0.824] | 0.825 (3666) [0.816, 0.835] | 0.816 (2055) [0.804, 0.826] | 0.882 (51) | 0.187 | flat -0.031 (noise 0.028) |
| reversal_k8_next | 0.462 (65) | 0.417 (441) [0.388, 0.449] | 0.395 (2636) [0.380, 0.409] | 0.395 (5432) [0.385, 0.406] | 0.395 (3326) [0.382, 0.407] | 0.429 (56) | 0.121 | flat -0.018 (noise 0.031) |
| reversal_k8_now | 0.646 (48) | 0.691 (349) [0.670, 0.710] | 0.684 (1527) [0.665, 0.702] | 0.700 (3582) [0.686, 0.714] | 0.689 (1995) [0.672, 0.706] | 0.750 (44) | 0.121 | flat -0.026 (noise 0.034) |
| overall | 0.506 (22029) | 0.506 (153344) [0.505, 0.508] | 0.505 (662126) [0.504, 0.507] | 0.504 (1521113) [0.503, 0.505] | 0.505 (837832) [0.504, 0.506] | 0.500 (17100) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07703, 0.1173] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5302, 'levels': [{'threshold': 0.07703, 'calls_per_day': 143.0, 'win_rate': 0.5702}, {'threshold': 0.1173, 'calls_per_day': 35.6, 'win_rate': 0.623}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42860, 'rate': 0.5303}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15252 | 0.340 | 0.531 (14951) | 0.568 (2480) | 0.741 (2564) |
| volatility: normal | 15252 | 0.368 | 0.535 (15184) | 0.606 (1436) | 0.752 (2276) |
| volatility: wild | 15252 | 0.385 | 0.525 (15211) | 0.620 (799) | 0.770 (2092) |
| session: Asia 00-08 | 15360 | 0.364 | 0.537 (15220) | 0.596 (1676) | 0.755 (2297) |
| session: Europe 08-13 | 9600 | 0.357 | 0.534 (9489) | 0.588 (1250) | 0.753 (1556) |
| session: US 13-21 | 15216 | 0.371 | 0.527 (15101) | 0.590 (1232) | 0.754 (2302) |
| session: late 21-24 | 5580 | 0.357 | 0.516 (5536) | 0.562 (557) | 0.747 (777) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.378 | 0.367 | 0.332 | 0.332 | 0.500 | 0.257 | 0.499 | 1.229 |
| 6h | 360 | 0.374 | 0.387 | 0.319 | 0.353 | 0.471 | 0.243 | 0.506 | 1.556 |
| 24h | 1440 | 0.381 | 0.374 | 0.301 | 0.333 | 0.532 | 0.270 | 0.492 | 1.182 |
| 7d | 10080 | 0.368 | 0.362 | 0.279 | 0.311 | 0.531 | 0.264 | 0.472 | 1.397 |
| 30d | 43200 | 0.367 | 0.359 | 0.278 | 0.309 | 0.530 | 0.264 | 0.469 | 1.253 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.378 / 0.500 / 0.883; 2: 0.374 / 0.500 / 0.733; 3: 0.368 / 0.467 / 0.767; 4: 0.366 / 0.467 / 0.750; 5: 0.357 / 0.383 / 0.717; 6: 0.416 / 0.667 / 0.767; 7: 0.365 / 0.450 / 0.917; 8: 0.375 / 0.500 / 0.750; 9: 0.381 / 0.517 / 0.767; 10: 0.385 / 0.533 / 0.900; 11: 0.386 / 0.533 / 0.900; 12: 0.392 / 0.517 / 0.933; 13: 0.365 / 0.500 / 0.933; 14: 0.390 / 0.483 / 0.917; 15: 0.388 / 0.500 / 0.933
- 6h: 1: 0.374 / 0.471 / 0.919; 2: 0.382 / 0.510 / 0.844; 3: 0.375 / 0.490 / 0.850; 4: 0.369 / 0.485 / 0.797; 5: 0.373 / 0.490 / 0.781; 6: 0.379 / 0.526 / 0.822; 7: 0.368 / 0.476 / 0.894; 8: 0.369 / 0.501 / 0.794; 9: 0.368 / 0.490 / 0.794; 10: 0.380 / 0.526 / 0.850; 11: 0.367 / 0.510 / 0.839; 12: 0.363 / 0.479 / 0.844; 13: 0.366 / 0.507 / 0.833; 14: 0.367 / 0.504 / 0.811; 15: 0.352 / 0.451 / 0.847
- 24h: 1: 0.381 / 0.532 / 0.910; 2: 0.367 / 0.485 / 0.884; 3: 0.365 / 0.510 / 0.885; 4: 0.359 / 0.476 / 0.880; 5: 0.362 / 0.494 / 0.876; 6: 0.361 / 0.492 / 0.881; 7: 0.363 / 0.490 / 0.888; 8: 0.361 / 0.497 / 0.879; 9: 0.367 / 0.512 / 0.877; 10: 0.367 / 0.513 / 0.876; 11: 0.366 / 0.520 / 0.878; 12: 0.358 / 0.492 / 0.879; 13: 0.359 / 0.504 / 0.878; 14: 0.363 / 0.501 / 0.874; 15: 0.360 / 0.494 / 0.881
- 7d: 1: 0.368 / 0.531 / 0.899; 2: 0.356 / 0.490 / 0.902; 3: 0.359 / 0.514 / 0.898; 4: 0.355 / 0.497 / 0.897; 5: 0.356 / 0.500 / 0.900; 6: 0.352 / 0.497 / 0.898; 7: 0.353 / 0.496 / 0.902; 8: 0.353 / 0.500 / 0.899; 9: 0.356 / 0.509 / 0.899; 10: 0.355 / 0.506 / 0.900; 11: 0.354 / 0.505 / 0.901; 12: 0.353 / 0.508 / 0.900; 13: 0.351 / 0.495 / 0.901; 14: 0.354 / 0.507 / 0.899; 15: 0.351 / 0.497 / 0.901
- 30d: 1: 0.367 / 0.530 / 0.899; 2: 0.354 / 0.494 / 0.900; 3: 0.357 / 0.510 / 0.900; 4: 0.353 / 0.497 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.501 / 0.900; 7: 0.352 / 0.499 / 0.900; 8: 0.352 / 0.504 / 0.900; 9: 0.353 / 0.504 / 0.900; 10: 0.352 / 0.504 / 0.900; 11: 0.350 / 0.500 / 0.900; 12: 0.351 / 0.504 / 0.900; 13: 0.350 / 0.499 / 0.900; 14: 0.350 / 0.501 / 0.900; 15: 0.350 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.096 (body 0.059, range 0.133); 'price stays where it was' would score 0.087; colour right 0.450; typical miss of the close 21.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.119 (body 0.070, range 0.168); 'price stays where it was' would score 0.106; colour right 0.465; typical miss of the close 21.9 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.110 (body 0.069, range 0.151); 'price stays where it was' would score 0.101; colour right 0.497; typical miss of the close 13.3 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.122 (body 0.081, range 0.162); 'price stays where it was' would score 0.122; colour right 0.502; typical miss of the close 9.2 bp; chain ended on the right side 0.521 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.6; 2: 0.200 / 5.4; 3: 0.166 / 7.0; 4: 0.131 / 7.2; 5: 0.126 / 8.0; 6: 0.116 / 8.9; 7: 0.110 / 9.1; 8: 0.097 / 10.1; 9: 0.091 / 10.1; 10: 0.093 / 10.7; 11: 0.087 / 10.6; 12: 0.078 / 11.1; 13: 0.073 / 11.6; 14: 0.070 / 12.1; 15: 0.066 / 12.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 143430, probability skill vs chance 0.2367, widened contest next: False
  - now: threshold 0.8383, hit rate recent 0.9228 / long run 0.9278
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.275, naive rule 0.495, lift 3.24x
    - 24h: 58 calls (58 a day), hit rate 0.897, chance 0.288, naive rule 0.492, lift 3.12x
    - 7d: 403 calls (58 a day), hit rate 0.926, chance 0.298, naive rule 0.506, lift 3.10x
    - 30d: 1711 calls (57 a day), hit rate 0.934, chance 0.293, naive rule 0.495, lift 3.18x
  - next: threshold 0.5664, hit rate recent 0.6252 / long run 0.6099
    - 6h: 8 calls (32 a day), hit rate 0.750, chance 0.275, lift 2.73x
    - 24h: 45 calls (45 a day), hit rate 0.622, chance 0.288, lift 2.16x
    - 7d: 358 calls (51 a day), hit rate 0.626, chance 0.298, lift 2.10x
    - 30d: 2823 calls (94 a day), hit rate 0.591, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.498; 0.35: 533, 0.523; 0.40: 474, 0.579; 0.45: 406, 0.650; 0.50: 356, 0.697; 0.55: 309, 0.742; 0.60: 260, 0.786; 0.65: 219, 0.812; 0.70: 172, 0.844; 0.75: 138, 0.875; 0.80: 91, 0.907; 0.85: 46, 0.947; 0.90: 4, 0.992
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 498, 0.463; 0.40: 399, 0.501; 0.45: 300, 0.535; 0.50: 193, 0.569; 0.55: 86, 0.579; 0.60: 12, 0.645; 0.65: 1, 0.600
- **K=5**: model 1794268800, labels learned 143428, probability skill vs chance 0.2234, widened contest next: False
  - now: threshold 0.6819, hit rate recent 0.815 / long run 0.811
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.178, naive rule 0.411, lift 4.74x
    - 24h: 58 calls (58 a day), hit rate 0.862, chance 0.192, naive rule 0.422, lift 4.49x
    - 7d: 361 calls (52 a day), hit rate 0.809, chance 0.188, naive rule 0.411, lift 4.31x
    - 30d: 1615 calls (54 a day), hit rate 0.815, chance 0.187, naive rule 0.407, lift 4.37x
  - next: threshold 0.4566, hit rate recent 0.5433 / long run 0.522
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.178, lift 3.36x
    - 24h: 53 calls (53 a day), hit rate 0.528, chance 0.192, lift 2.75x
    - 7d: 393 calls (56 a day), hit rate 0.532, chance 0.188, lift 2.83x
    - 30d: 2673 calls (89 a day), hit rate 0.489, chance 0.187, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.421; 0.35: 352, 0.485; 0.40: 284, 0.556; 0.45: 233, 0.608; 0.50: 186, 0.657; 0.55: 150, 0.695; 0.60: 112, 0.746; 0.65: 75, 0.782; 0.70: 46, 0.821; 0.75: 28, 0.854; 0.80: 10, 0.874
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.384; 0.35: 256, 0.422; 0.40: 160, 0.461; 0.45: 65, 0.494; 0.50: 10, 0.510; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 143425, probability skill vs chance 0.214, widened contest next: False
  - now: threshold 0.5665, hit rate recent 0.7307 / long run 0.6947
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.133, naive rule 0.392, lift 6.84x
    - 24h: 50 calls (50 a day), hit rate 0.760, chance 0.123, naive rule 0.346, lift 6.17x
    - 7d: 352 calls (50 a day), hit rate 0.702, chance 0.122, naive rule 0.342, lift 5.77x
    - 30d: 1523 calls (51 a day), hit rate 0.685, chance 0.120, naive rule 0.335, lift 5.69x
  - next: threshold 0.3625, hit rate recent 0.4263 / long run 0.4174
    - 6h: 17 calls (70 a day), hit rate 0.412, chance 0.133, lift 3.10x
    - 24h: 63 calls (63 a day), hit rate 0.444, chance 0.123, lift 3.61x
    - 7d: 442 calls (63 a day), hit rate 0.419, chance 0.122, lift 3.44x
    - 30d: 2621 calls (87 a day), hit rate 0.397, chance 0.120, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.428; 0.35: 192, 0.492; 0.40: 152, 0.538; 0.45: 117, 0.584; 0.50: 84, 0.638; 0.55: 59, 0.673; 0.60: 39, 0.713; 0.65: 24, 0.782; 0.70: 12, 0.815; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 171, 0.363; 0.35: 87, 0.392; 0.40: 23, 0.425; 0.45: 4, 0.432; 0.50: 1, 0.727
- **K=13**: model 1794096000, labels learned 143420, probability skill vs chance 0.1907, widened contest next: False
  - now: threshold 0.4532, hit rate recent 0.6085 / long run 0.5716
    - 6h: 10 calls (42 a day), hit rate 0.700, chance 0.091, naive rule 0.352, lift 7.67x
    - 24h: 44 calls (44 a day), hit rate 0.659, chance 0.086, naive rule 0.314, lift 7.70x
    - 7d: 356 calls (51 a day), hit rate 0.576, chance 0.079, naive rule 0.288, lift 7.27x
    - 30d: 1638 calls (55 a day), hit rate 0.561, chance 0.077, naive rule 0.282, lift 7.25x
  - next: threshold 0.2832, hit rate recent 0.3676 / long run 0.3324
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.091, lift 4.69x
    - 24h: 64 calls (65 a day), hit rate 0.359, chance 0.086, lift 4.20x
    - 7d: 467 calls (67 a day), hit rate 0.321, chance 0.079, lift 4.05x
    - 30d: 1827 calls (61 a day), hit rate 0.323, chance 0.077, lift 4.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 133, 0.431; 0.35: 96, 0.479; 0.40: 67, 0.538; 0.45: 46, 0.583; 0.50: 31, 0.644; 0.55: 21, 0.667; 0.60: 12, 0.702; 0.65: 4, 0.670; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.329; 0.35: 13, 0.339; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.589 | 1.80% | 0.850 | 0.467 | 0.260 | 0.400 | 0.149 |
| 6h | 33.955 | 7.48% | 0.908 | 0.500 | 0.253 | 0.476 | 0.340 |
| 24h | 19.760 | 5.33% | 0.901 | 0.504 | 0.251 | 0.500 | 0.504 |
| 7d | 16.898 | 6.41% | 0.901 | 0.500 | 0.251 | 0.501 | 0.692 |
| 30d | 15.726 | 4.73% | 0.900 | 0.500 | 0.250 | 0.501 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.057 | 25.246 | 25.459 | 25.546 | 25.255 | 26.044 | 25.354 | 25.179 | 25.281 | 25.589 |
| 6h | 36.700 | 34.294 | 34.348 | 34.190 | 34.977 | 34.394 | 33.978 | 33.958 | 33.939 | 33.955 |
| 24h | 20.873 | 19.915 | 19.925 | 19.873 | 20.336 | 20.083 | 19.734 | 19.721 | 19.724 | 19.760 |
| 7d | 18.054 | 17.038 | 17.008 | 17.015 | 17.210 | 17.310 | 16.869 | 16.857 | 16.863 | 16.898 |
| 30d | 16.506 | 15.884 | 15.832 | 15.775 | 16.019 | 15.989 | 15.712 | 15.693 | 15.696 | 15.726 |

## Next candle

- candle starting 2026-11-10 18:36 UTC, last close 2038.31
- P(up) 0.47, return quantiles (bp): {'05': -16.52, '10': -12.279, '25': -6.747, '40': -2.888, '50': -0.847, '60': 2.017, '75': 5.888, '90': 12.279, '95': 16.302}
- changepoint probability 0.057, regime age 93.4 min
- agent weights: empirical 0.003, ewma 0.078, garch 0.073, har 0.124, bocpd 0.006, hmm 0.023, online_qr 0.324, lgbm 0.369

## Learning log

- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- HMM volatility states (sd, bp per minute): [2.27, 5.7, 16.94], current probabilities: [0.0, 0.214, 0.785]
- live generator: {'versions': 60, 'latest_effective': '2026-11-10 18:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.194, 'l_abs': 0.688, 'l_hi': 0.799, 'l_lo': 0.744, 'b05': 0.702, 'b25': 0.642, 'b75': 0.583, 'b95': 0.731}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.3, 1.6], [1.4, 1.8], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.66, 2.078, 3.245, 4.018, 3.267, 2.619, 4.357, 4.63, 3.847, 4.043, 3.985, 4.325, 4.872, 4.393]}
- calibration offsets (in sigma): {'05': 0.0375, '10': 0.065, '25': -0.0025, '40': -0.02, '50': -0.045, '60': -0.01, '75': 0.0025, '90': -0.025, '95': -0.0375}
