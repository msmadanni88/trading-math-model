# ETH-USD 60s candle generator - report

- generated: 2026-10-15 12:51 UTC
- last closed candle: 2026-10-15 12:51 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.505 (671) [0.479, 0.535] | 0.513 (2875) [0.493, 0.531] | 0.510 (4122) [0.494, 0.525] | 0.506 (1150) [0.475, 0.538] | 0.549 (51) | 0.500 | flat -0.004 (noise 0.035) |
| colour_clear | 0.559 (843) | 0.541 (5560) [0.534, 0.549] | 0.515 (23376) [0.507, 0.523] | 0.509 (33481) [0.503, 0.515] | 0.543 (9243) [0.536, 0.549] | 0.571 (413) | 0.500 | flat +0.015 (noise 0.013) |
| colour_confident | 0.537 (67) | 0.599 (882) [0.574, 0.634] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.641 (39) | 0.500 | flat -0.010 (noise 0.033) |
| colour_next | 0.542 (1436) | 0.526 (9976) [0.520, 0.532] | 0.511 (42873) [0.506, 0.517] | 0.508 (61433) [0.504, 0.512] | 0.528 (17084) [0.522, 0.534] | 0.534 (769) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.501 (139664) [0.500, 0.502] | 0.501 (600222) [0.500, 0.502] | 0.501 (860062) [0.499, 0.502] | 0.500 (239176) [0.498, 0.502] | 0.518 (10766) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.462 (13) | 0.657 (233) [0.603, 0.720] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 1.000 (5) | 0.500 | flat +0.009 (noise 0.051) |
| reversal_k13_next | 0.244 (45) | 0.316 (471) [0.290, 0.342] | 0.314 (2053) [0.299, 0.330] | 0.305 (2977) [0.293, 0.319] | 0.319 (872) [0.303, 0.334] | 0.292 (24) | 0.077 | flat +0.005 (noise 0.029) |
| reversal_k13_now | 0.548 (42) | 0.593 (346) [0.566, 0.621] | 0.587 (1480) [0.567, 0.609] | 0.583 (2108) [0.567, 0.601] | 0.588 (636) [0.559, 0.621] | 0.571 (28) | 0.077 | flat +0.004 (noise 0.036) |
| reversal_k3_next | 0.591 (66) | 0.574 (676) [0.552, 0.598] | 0.583 (2477) [0.569, 0.599] | 0.584 (3532) [0.572, 0.597] | 0.576 (1092) [0.557, 0.599] | 0.614 (44) | 0.293 | flat -0.011 (noise 0.028) |
| reversal_k3_now | 0.980 (49) | 0.929 (423) [0.915, 0.947] | 0.939 (1723) [0.931, 0.947] | 0.938 (2459) [0.931, 0.945] | 0.930 (696) [0.919, 0.941] | 0.920 (25) | 0.293 | flat -0.001 (noise 0.018) |
| reversal_k5_next | 0.543 (94) | 0.489 (564) [0.469, 0.510] | 0.489 (2146) [0.472, 0.507] | 0.485 (3005) [0.471, 0.501] | 0.469 (1015) [0.445, 0.495] | 0.450 (60) | 0.187 | flat +0.027 (noise 0.028) |
| reversal_k5_now | 0.849 (33) | 0.811 (354) [0.785, 0.839] | 0.831 (1577) [0.815, 0.846] | 0.833 (2241) [0.820, 0.846] | 0.822 (630) [0.799, 0.844] | 0.714 (28) | 0.188 | flat -0.030 (noise 0.028) |
| reversal_k8_next | 0.386 (57) | 0.398 (571) [0.379, 0.418] | 0.410 (2107) [0.394, 0.429] | 0.396 (3097) [0.382, 0.410] | 0.395 (991) [0.376, 0.414] | 0.404 (47) | 0.122 | flat +0.000 (noise 0.030) |
| reversal_k8_now | 0.725 (40) | 0.674 (374) [0.640, 0.712] | 0.714 (1578) [0.693, 0.735] | 0.709 (2257) [0.693, 0.726] | 0.699 (670) [0.668, 0.730] | 0.762 (21) | 0.122 | flat -0.052 (noise 0.033) |
| overall | 0.507 (22062) | 0.504 (154090) [0.503, 0.506] | 0.504 (661111) [0.502, 0.505] | 0.503 (947293) [0.502, 0.504] | 0.504 (264012) [0.501, 0.506] | 0.521 (11863) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07477, 0.1162] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5262, 'levels': [{'threshold': 0.07477, 'calls_per_day': 142.0, 'win_rate': 0.5966}, {'threshold': 0.1162, 'calls_per_day': 35.5, 'win_rate': 0.6813}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 16716, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15137 | 0.336 | 0.519 (14903) | 0.601 (1233) | 0.776 (2448) |
| volatility: normal | 15137 | 0.362 | 0.513 (15074) | 0.591 (286) | 0.784 (2113) |
| volatility: wild | 15137 | 0.375 | 0.502 (15096) | 0.664 (128) | 0.767 (2086) |
| session: Asia 00-08 | 15360 | 0.356 | 0.516 (15262) | 0.604 (598) | 0.772 (2201) |
| session: Europe 08-13 | 9591 | 0.352 | 0.510 (9510) | 0.589 (423) | 0.785 (1472) |
| session: US 13-21 | 14880 | 0.367 | 0.507 (14785) | 0.583 (396) | 0.781 (2160) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5516) | 0.670 (230) | 0.753 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.371 | 0.392 | 0.246 | 0.246 | 0.576 | 0.240 | 0.502 | 1.029 |
| 6h | 360 | 0.380 | 0.364 | 0.275 | 0.313 | 0.554 | 0.278 | 0.482 | 1.081 |
| 24h | 1440 | 0.377 | 0.371 | 0.294 | 0.334 | 0.524 | 0.265 | 0.488 | 1.133 |
| 7d | 10080 | 0.357 | 0.350 | 0.272 | 0.303 | 0.526 | 0.259 | 0.456 | 1.246 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.512 | 0.250 | 0.466 | 1.297 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.371 / 0.576 / 0.850; 2: 0.364 / 0.492 / 0.817; 3: 0.360 / 0.525 / 0.817; 4: 0.340 / 0.441 / 0.867; 5: 0.383 / 0.644 / 0.850; 6: 0.340 / 0.525 / 0.833; 7: 0.352 / 0.525 / 0.867; 8: 0.352 / 0.542 / 0.833; 9: 0.320 / 0.458 / 0.833; 10: 0.360 / 0.593 / 0.833; 11: 0.314 / 0.492 / 0.850; 12: 0.355 / 0.593 / 0.883; 13: 0.357 / 0.610 / 0.917; 14: 0.341 / 0.610 / 0.917; 15: 0.317 / 0.492 / 0.933
- 6h: 1: 0.380 / 0.554 / 0.900; 2: 0.362 / 0.487 / 0.822; 3: 0.372 / 0.535 / 0.831; 4: 0.372 / 0.507 / 0.833; 5: 0.378 / 0.557 / 0.853; 6: 0.372 / 0.526 / 0.872; 7: 0.365 / 0.510 / 0.892; 8: 0.366 / 0.493 / 0.867; 9: 0.356 / 0.499 / 0.886; 10: 0.370 / 0.529 / 0.889; 11: 0.362 / 0.501 / 0.906; 12: 0.364 / 0.524 / 0.925; 13: 0.383 / 0.577 / 0.939; 14: 0.371 / 0.549 / 0.953; 15: 0.363 / 0.529 / 0.967
- 24h: 1: 0.377 / 0.524 / 0.911; 2: 0.363 / 0.498 / 0.899; 3: 0.371 / 0.517 / 0.897; 4: 0.368 / 0.511 / 0.895; 5: 0.368 / 0.518 / 0.906; 6: 0.366 / 0.511 / 0.912; 7: 0.367 / 0.518 / 0.912; 8: 0.358 / 0.486 / 0.912; 9: 0.368 / 0.508 / 0.917; 10: 0.370 / 0.531 / 0.915; 11: 0.363 / 0.510 / 0.917; 12: 0.359 / 0.499 / 0.919; 13: 0.363 / 0.513 / 0.923; 14: 0.358 / 0.495 / 0.925; 15: 0.368 / 0.527 / 0.927
- 7d: 1: 0.357 / 0.526 / 0.903; 2: 0.346 / 0.498 / 0.899; 3: 0.349 / 0.512 / 0.899; 4: 0.346 / 0.499 / 0.899; 5: 0.348 / 0.509 / 0.899; 6: 0.346 / 0.502 / 0.900; 7: 0.345 / 0.502 / 0.900; 8: 0.344 / 0.500 / 0.898; 9: 0.344 / 0.496 / 0.899; 10: 0.346 / 0.509 / 0.899; 11: 0.342 / 0.493 / 0.900; 12: 0.344 / 0.503 / 0.900; 13: 0.344 / 0.503 / 0.900; 14: 0.342 / 0.502 / 0.900; 15: 0.345 / 0.506 / 0.901
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.163 (body 0.105, range 0.222); 'price stays where it was' would score 0.132; colour right 0.559; typical miss of the close 10.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.149 (body 0.099, range 0.200); 'price stays where it was' would score 0.141; colour right 0.540; typical miss of the close 10.4 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.135 (body 0.090, range 0.181); 'price stays where it was' would score 0.141; colour right 0.498; typical miss of the close 13.4 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.123 (body 0.084, range 0.161); 'price stays where it was' would score 0.127; colour right 0.496; typical miss of the close 7.6 bp; chain ended on the right side 0.508 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.515 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.1; 2: 0.197 / 4.5; 3: 0.165 / 6.1; 4: 0.132 / 6.8; 5: 0.121 / 7.5; 6: 0.108 / 8.0; 7: 0.102 / 8.4; 8: 0.096 / 8.8; 9: 0.087 / 8.8; 10: 0.083 / 9.6; 11: 0.078 / 10.3; 12: 0.075 / 10.7; 13: 0.063 / 10.9; 14: 0.065 / 11.2; 15: 0.059 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 105645, probability skill vs chance 0.2297, widened contest next: False
  - now: threshold 0.8413, hit rate recent 0.9493 / long run 0.9344
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.266, naive rule 0.452, lift 3.76x
    - 24h: 45 calls (45 a day), hit rate 0.933, chance 0.282, naive rule 0.473, lift 3.31x
    - 7d: 408 calls (58 a day), hit rate 0.926, chance 0.298, naive rule 0.502, lift 3.11x
    - 30d: 1717 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.24x
  - next: threshold 0.5416, hit rate recent 0.6113 / long run 0.58
    - 6h: 24 calls (97 a day), hit rate 0.750, chance 0.266, lift 2.82x
    - 24h: 64 calls (64 a day), hit rate 0.594, chance 0.282, lift 2.11x
    - 7d: 689 calls (98 a day), hit rate 0.573, chance 0.298, lift 1.93x
    - 30d: 2476 calls (83 a day), hit rate 0.584, chance 0.290, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.490; 0.35: 539, 0.512; 0.40: 484, 0.561; 0.45: 415, 0.631; 0.50: 361, 0.685; 0.55: 317, 0.727; 0.60: 270, 0.772; 0.65: 224, 0.801; 0.70: 180, 0.834; 0.75: 139, 0.871; 0.80: 96, 0.912; 0.85: 49, 0.951; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.459; 0.40: 410, 0.488; 0.45: 314, 0.524; 0.50: 204, 0.559; 0.55: 91, 0.581; 0.60: 14, 0.599; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 105643, probability skill vs chance 0.2185, widened contest next: True
  - now: threshold 0.6971, hit rate recent 0.784 / long run 0.8221
    - 6h: 15 calls (61 a day), hit rate 0.733, chance 0.193, naive rule 0.429, lift 3.81x
    - 24h: 42 calls (42 a day), hit rate 0.786, chance 0.191, naive rule 0.416, lift 4.12x
    - 7d: 347 calls (50 a day), hit rate 0.810, chance 0.190, naive rule 0.412, lift 4.26x
    - 30d: 1576 calls (53 a day), hit rate 0.828, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.4238, hit rate recent 0.4955 / long run 0.4822
    - 6h: 29 calls (118 a day), hit rate 0.552, chance 0.193, lift 2.86x
    - 24h: 107 calls (108 a day), hit rate 0.514, chance 0.191, lift 2.70x
    - 7d: 597 calls (85 a day), hit rate 0.486, chance 0.190, lift 2.56x
    - 30d: 2173 calls (72 a day), hit rate 0.486, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 355, 0.482; 0.40: 285, 0.553; 0.45: 234, 0.610; 0.50: 182, 0.664; 0.55: 139, 0.709; 0.60: 109, 0.750; 0.65: 82, 0.791; 0.70: 60, 0.821; 0.75: 33, 0.863; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 251, 0.425; 0.40: 161, 0.456; 0.45: 78, 0.474; 0.50: 18, 0.507; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 105640, probability skill vs chance 0.2061, widened contest next: False
  - now: threshold 0.5827, hit rate recent 0.7216 / long run 0.7043
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.123, naive rule 0.352, lift 7.33x
    - 24h: 34 calls (34 a day), hit rate 0.765, chance 0.113, naive rule 0.327, lift 6.79x
    - 7d: 363 calls (52 a day), hit rate 0.683, chance 0.124, naive rule 0.349, lift 5.51x
    - 30d: 1571 calls (52 a day), hit rate 0.714, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.3477, hit rate recent 0.4 / long run 0.3983
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.123, lift 3.66x
    - 24h: 71 calls (71 a day), hit rate 0.394, chance 0.113, lift 3.50x
    - 7d: 559 calls (80 a day), hit rate 0.395, chance 0.124, lift 3.19x
    - 30d: 2127 calls (71 a day), hit rate 0.409, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 261, 0.417; 0.35: 197, 0.491; 0.40: 151, 0.551; 0.45: 119, 0.594; 0.50: 91, 0.634; 0.55: 65, 0.684; 0.60: 44, 0.725; 0.65: 24, 0.776; 0.70: 9, 0.828; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.352; 0.35: 108, 0.390; 0.40: 44, 0.422; 0.45: 9, 0.462; 0.50: 1, 0.371
- **K=13**: model 1792022400, labels learned 105635, probability skill vs chance 0.1824, widened contest next: True
  - now: threshold 0.4185, hit rate recent 0.5784 / long run 0.5836
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.100, naive rule 0.374, lift 6.43x
    - 24h: 42 calls (42 a day), hit rate 0.571, chance 0.081, naive rule 0.287, lift 7.08x
    - 7d: 349 calls (50 a day), hit rate 0.590, chance 0.080, naive rule 0.291, lift 7.39x
    - 30d: 1479 calls (49 a day), hit rate 0.589, chance 0.078, naive rule 0.274, lift 7.55x
  - next: threshold 0.3006, hit rate recent 0.2688 / long run 0.3074
    - 6h: 10 calls (42 a day), hit rate 0.200, chance 0.100, lift 2.00x
    - 24h: 40 calls (40 a day), hit rate 0.275, chance 0.081, lift 3.41x
    - 7d: 459 calls (66 a day), hit rate 0.314, chance 0.080, lift 3.93x
    - 30d: 2036 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.454; 0.35: 85, 0.515; 0.40: 60, 0.565; 0.45: 41, 0.618; 0.50: 25, 0.654; 0.55: 14, 0.709; 0.60: 4, 0.760; 0.65: 1, 0.941
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.327; 0.35: 13, 0.373; 0.40: 2, 0.426; 0.45: 0, 0.286

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 32.351 | 5.76% | 0.867 | 0.517 | 0.248 | 0.627 | 0.504 |
| 6h | 19.387 | 2.18% | 0.914 | 0.478 | 0.251 | 0.490 | 0.556 |
| 24h | 23.141 | 4.43% | 0.905 | 0.498 | 0.250 | 0.510 | 0.578 |
| 7d | 14.287 | 4.50% | 0.901 | 0.501 | 0.251 | 0.494 | 0.679 |
| 30d | 14.242 | 4.06% | 0.900 | 0.500 | 0.251 | 0.495 | 0.683 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 34.327 | 33.170 | 32.511 | 32.092 | 33.500 | 33.132 | 32.028 | 32.442 | 32.283 | 32.351 |
| 6h | 19.819 | 19.480 | 19.498 | 19.375 | 19.623 | 19.678 | 19.284 | 19.354 | 19.348 | 19.387 |
| 24h | 24.215 | 23.477 | 23.121 | 23.111 | 23.308 | 23.582 | 23.141 | 23.109 | 23.064 | 23.141 |
| 7d | 14.960 | 14.445 | 14.376 | 14.306 | 14.550 | 14.519 | 14.288 | 14.249 | 14.257 | 14.287 |
| 30d | 14.845 | 14.374 | 14.325 | 14.265 | 14.504 | 14.441 | 14.240 | 14.213 | 14.213 | 14.242 |

## Next candle

- candle starting 2026-10-15 12:51 UTC, last close 2350.42
- P(up) 0.4908, return quantiles (bp): {'05': -18.4, '10': -14.479, '25': -7.541, '40': -2.417, '50': -0.199, '60': 2.016, '75': 7.248, '90': 14.914, '95': 19.036}
- changepoint probability 0.3145, regime age 19.6 min
- agent weights: empirical 0.004, ewma 0.025, garch 0.166, har 0.264, bocpd 0.042, hmm 0.016, online_qr 0.247, lgbm 0.236

## Learning log

- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- HMM volatility states (sd, bp per minute): [2.37, 5.56, 18.85], current probabilities: [0.007, 0.754, 0.238]
- live generator: {'versions': 60, 'latest_effective': '2026-10-15 13:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.268, 'l_abs': 0.742, 'l_hi': 0.707, 'l_lo': 0.735, 'b05': 0.763, 'b25': 0.722, 'b75': 0.706, 'b95': 0.775}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [2.047, 2.319, 2.738, 2.888, 2.756, 2.924, 3.326, 3.198, 3.378, 3.212, 3.166, 3.236, 3.233, 3.034]}
- calibration offsets (in sigma): {'05': 0.075, '10': 0.0, '25': -0.015, '40': 0.01, '50': -0.02, '60': -0.05, '75': -0.015, '90': 0.01, '95': -0.045}
