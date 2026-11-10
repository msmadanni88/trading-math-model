# ETH-USD 60s candle generator - report

- generated: 2026-11-10 10:59 UTC
- last closed candle: 2026-11-10 10:59 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.516 (672) [0.478, 0.554] | 0.519 (2879) [0.502, 0.537] | 0.514 (6618) [0.503, 0.526] | 0.517 (3646) [0.500, 0.534] | 0.442 (43) | 0.500 | flat +0.018 (noise 0.027) |
| colour_clear | 0.531 (791) | 0.538 (5545) [0.519, 0.556] | 0.543 (23828) [0.537, 0.549] | 0.522 (54150) [0.517, 0.528] | 0.543 (29912) [0.538, 0.548] | 0.575 (376) | 0.500 | flat -0.002 (noise 0.012) |
| colour_confident | 0.640 (50) | 0.585 (995) [0.572, 0.608] | 0.591 (4371) [0.582, 0.601] | 0.595 (5595) [0.585, 0.606] | 0.595 (5595) [0.585, 0.606] | 0.471 (51) | 0.500 | flat +0.010 (noise 0.022) |
| colour_next | 0.529 (1436) | 0.531 (9970) [0.519, 0.544] | 0.530 (42849) [0.526, 0.534] | 0.517 (98560) [0.513, 0.521] | 0.530 (54211) [0.526, 0.534] | 0.547 (654) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.503 (139580) [0.501, 0.504] | 0.502 (599886) [0.500, 0.503] | 0.501 (1379840) [0.500, 0.502] | 0.501 (758954) [0.500, 0.502] | 0.495 (9156) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.500 (2) | 0.616 (263) [0.560, 0.634] | 0.623 (1161) [0.607, 0.638] | 0.630 (1493) [0.614, 0.647] | 0.630 (1493) [0.614, 0.647] | 0.800 (5) | 0.500 | flat -0.003 (noise 0.044) |
| reversal_k13_next | 0.358 (67) | 0.331 (465) [0.305, 0.361] | 0.324 (1833) [0.309, 0.338] | 0.313 (4551) [0.303, 0.323] | 0.325 (2446) [0.313, 0.336] | 0.343 (35) | 0.077 | flat -0.025 (noise 0.034) |
| reversal_k13_now | 0.537 (41) | 0.575 (360) [0.547, 0.605] | 0.559 (1641) [0.540, 0.578] | 0.573 (3558) [0.560, 0.586] | 0.567 (2086) [0.549, 0.585] | 0.630 (27) | 0.077 | flat -0.006 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.615 (369) [0.582, 0.646] | 0.591 (2864) [0.580, 0.603] | 0.588 (6005) [0.579, 0.597] | 0.589 (3565) [0.578, 0.599] | 0.560 (25) | 0.294 | flat +0.017 (noise 0.030) |
| reversal_k3_now | 0.909 (55) | 0.919 (396) [0.910, 0.930] | 0.933 (1725) [0.922, 0.943] | 0.936 (3963) [0.930, 0.942] | 0.931 (2200) [0.923, 0.940] | 0.944 (36) | 0.294 | flat -0.015 (noise 0.018) |
| reversal_k5_next | 0.513 (37) | 0.524 (393) [0.498, 0.550] | 0.487 (2679) [0.472, 0.504] | 0.485 (5338) [0.474, 0.497] | 0.480 (3348) [0.466, 0.495] | 0.562 (32) | 0.187 | flat -0.019 (noise 0.036) |
| reversal_k5_now | 0.641 (39) | 0.791 (349) [0.749, 0.826] | 0.813 (1607) [0.800, 0.824] | 0.825 (3666) [0.816, 0.835] | 0.816 (2055) [0.804, 0.826] | 0.914 (35) | 0.187 | flat -0.031 (noise 0.028) |
| reversal_k8_next | 0.462 (65) | 0.417 (441) [0.388, 0.449] | 0.395 (2636) [0.380, 0.409] | 0.395 (5432) [0.385, 0.406] | 0.395 (3326) [0.382, 0.407] | 0.455 (33) | 0.121 | flat -0.018 (noise 0.031) |
| reversal_k8_now | 0.646 (48) | 0.691 (349) [0.670, 0.710] | 0.684 (1527) [0.665, 0.702] | 0.700 (3582) [0.686, 0.714] | 0.689 (1995) [0.672, 0.706] | 0.710 (31) | 0.121 | flat -0.026 (noise 0.034) |
| overall | 0.506 (22029) | 0.506 (153344) [0.505, 0.508] | 0.505 (662126) [0.504, 0.507] | 0.504 (1521113) [0.503, 0.505] | 0.505 (837832) [0.504, 0.506] | 0.502 (10107) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0773, 0.1175] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5322, 'levels': [{'threshold': 0.0773, 'calls_per_day': 141.6, 'win_rate': 0.5798}, {'threshold': 0.1175, 'calls_per_day': 35.3, 'win_rate': 0.612}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42856, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15100 | 0.340 | 0.531 (14801) | 0.566 (2453) | 0.741 (2543) |
| volatility: normal | 15099 | 0.368 | 0.536 (15030) | 0.611 (1438) | 0.754 (2248) |
| volatility: wild | 15100 | 0.384 | 0.525 (15059) | 0.618 (806) | 0.767 (2088) |
| session: Asia 00-08 | 15360 | 0.364 | 0.537 (15220) | 0.596 (1676) | 0.755 (2297) |
| session: Europe 08-13 | 9479 | 0.357 | 0.534 (9368) | 0.589 (1241) | 0.755 (1543) |
| session: US 13-21 | 14880 | 0.371 | 0.528 (14766) | 0.591 (1223) | 0.751 (2262) |
| session: late 21-24 | 5580 | 0.357 | 0.516 (5536) | 0.562 (557) | 0.747 (777) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.353 | 0.370 | 0.251 | 0.251 | 0.467 | 0.217 | 0.490 | 1.451 |
| 6h | 360 | 0.382 | 0.369 | 0.293 | 0.302 | 0.542 | 0.282 | 0.482 | 1.077 |
| 24h | 1440 | 0.385 | 0.377 | 0.298 | 0.334 | 0.546 | 0.276 | 0.493 | 1.198 |
| 7d | 10080 | 0.368 | 0.362 | 0.278 | 0.309 | 0.533 | 0.264 | 0.472 | 1.381 |
| 30d | 43200 | 0.366 | 0.359 | 0.278 | 0.309 | 0.531 | 0.264 | 0.469 | 1.256 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.353 / 0.467 / 0.900; 2: 0.372 / 0.567 / 1.000; 3: 0.368 / 0.483 / 1.000; 4: 0.346 / 0.467 / 1.000; 5: 0.363 / 0.483 / 1.000; 6: 0.346 / 0.450 / 1.000; 7: 0.365 / 0.517 / 1.000; 8: 0.354 / 0.467 / 1.000; 9: 0.355 / 0.517 / 1.000; 10: 0.350 / 0.500 / 1.000; 11: 0.378 / 0.550 / 1.000; 12: 0.337 / 0.450 / 1.000; 13: 0.356 / 0.483 / 1.000; 14: 0.356 / 0.533 / 1.000; 15: 0.371 / 0.533 / 1.000
- 6h: 1: 0.382 / 0.542 / 0.903; 2: 0.362 / 0.500 / 0.992; 3: 0.356 / 0.506 / 0.989; 4: 0.358 / 0.497 / 0.975; 5: 0.347 / 0.464 / 0.958; 6: 0.358 / 0.503 / 0.975; 7: 0.358 / 0.489 / 0.981; 8: 0.357 / 0.506 / 0.972; 9: 0.358 / 0.497 / 0.961; 10: 0.357 / 0.503 / 0.983; 11: 0.354 / 0.494 / 0.975; 12: 0.344 / 0.475 / 0.964; 13: 0.350 / 0.503 / 0.953; 14: 0.359 / 0.503 / 0.972; 15: 0.355 / 0.511 / 0.933
- 24h: 1: 0.385 / 0.546 / 0.913; 2: 0.369 / 0.490 / 0.905; 3: 0.369 / 0.522 / 0.911; 4: 0.362 / 0.481 / 0.908; 5: 0.362 / 0.494 / 0.908; 6: 0.359 / 0.482 / 0.910; 7: 0.364 / 0.497 / 0.897; 8: 0.362 / 0.501 / 0.905; 9: 0.369 / 0.522 / 0.906; 10: 0.365 / 0.508 / 0.904; 11: 0.371 / 0.526 / 0.906; 12: 0.361 / 0.503 / 0.906; 13: 0.359 / 0.497 / 0.905; 14: 0.364 / 0.507 / 0.906; 15: 0.364 / 0.508 / 0.901
- 7d: 1: 0.368 / 0.533 / 0.898; 2: 0.356 / 0.490 / 0.899; 3: 0.359 / 0.515 / 0.902; 4: 0.354 / 0.496 / 0.902; 5: 0.355 / 0.501 / 0.900; 6: 0.352 / 0.497 / 0.902; 7: 0.352 / 0.496 / 0.899; 8: 0.353 / 0.499 / 0.900; 9: 0.356 / 0.511 / 0.900; 10: 0.354 / 0.503 / 0.899; 11: 0.353 / 0.505 / 0.899; 12: 0.354 / 0.511 / 0.900; 13: 0.351 / 0.492 / 0.899; 14: 0.353 / 0.507 / 0.900; 15: 0.351 / 0.498 / 0.900
- 30d: 1: 0.366 / 0.531 / 0.899; 2: 0.354 / 0.494 / 0.900; 3: 0.357 / 0.510 / 0.900; 4: 0.352 / 0.497 / 0.900; 5: 0.353 / 0.504 / 0.900; 6: 0.351 / 0.501 / 0.900; 7: 0.352 / 0.499 / 0.900; 8: 0.351 / 0.504 / 0.900; 9: 0.352 / 0.504 / 0.900; 10: 0.352 / 0.504 / 0.900; 11: 0.349 / 0.500 / 0.900; 12: 0.351 / 0.504 / 0.900; 13: 0.349 / 0.498 / 0.900; 14: 0.350 / 0.501 / 0.900; 15: 0.350 / 0.502 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.059 (body 0.027, range 0.092); 'price stays where it was' would score 0.061; colour right 0.467; typical miss of the close 29.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.108 (body 0.067, range 0.149); 'price stays where it was' would score 0.113; colour right 0.497; typical miss of the close 11.4 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.113 (body 0.073, range 0.154); 'price stays where it was' would score 0.108; colour right 0.503; typical miss of the close 12.2 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.123 (body 0.082, range 0.163); 'price stays where it was' would score 0.123; colour right 0.504; typical miss of the close 8.9 bp; chain ended on the right side 0.519 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.8 bp; chain ended on the right side 0.516 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.6; 2: 0.201 / 5.3; 3: 0.167 / 6.9; 4: 0.132 / 7.1; 5: 0.126 / 7.9; 6: 0.115 / 8.8; 7: 0.110 / 9.0; 8: 0.097 / 10.0; 9: 0.091 / 10.0; 10: 0.092 / 10.5; 11: 0.086 / 10.5; 12: 0.077 / 11.0; 13: 0.072 / 11.4; 14: 0.070 / 12.0; 15: 0.065 / 12.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 142973, probability skill vs chance 0.2315, widened contest next: False
  - now: threshold 0.8376, hit rate recent 0.9256 / long run 0.928
    - 6h: 19 calls (77 a day), hit rate 0.947, chance 0.289, naive rule 0.504, lift 3.28x
    - 24h: 63 calls (63 a day), hit rate 0.905, chance 0.293, naive rule 0.505, lift 3.08x
    - 7d: 407 calls (58 a day), hit rate 0.921, chance 0.299, naive rule 0.506, lift 3.08x
    - 30d: 1724 calls (57 a day), hit rate 0.934, chance 0.294, naive rule 0.496, lift 3.18x
  - next: threshold 0.5661, hit rate recent 0.6063 / long run 0.608
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.289, lift 2.13x
    - 24h: 44 calls (44 a day), hit rate 0.568, chance 0.293, lift 1.94x
    - 7d: 357 calls (51 a day), hit rate 0.622, chance 0.299, lift 2.08x
    - 30d: 2834 calls (94 a day), hit rate 0.592, chance 0.294, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.499; 0.35: 533, 0.524; 0.40: 474, 0.580; 0.45: 405, 0.651; 0.50: 356, 0.698; 0.55: 308, 0.743; 0.60: 260, 0.786; 0.65: 219, 0.813; 0.70: 173, 0.844; 0.75: 139, 0.875; 0.80: 91, 0.906; 0.85: 46, 0.948; 0.90: 4, 0.992
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 498, 0.464; 0.40: 399, 0.502; 0.45: 301, 0.537; 0.50: 194, 0.570; 0.55: 87, 0.579; 0.60: 12, 0.646; 0.65: 1, 0.600
- **K=5**: model 1794268800, labels learned 142971, probability skill vs chance 0.2181, widened contest next: False
  - now: threshold 0.6818, hit rate recent 0.8114 / long run 0.811
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.173, naive rule 0.391, lift 5.47x
    - 24h: 54 calls (54 a day), hit rate 0.833, chance 0.195, naive rule 0.427, lift 4.27x
    - 7d: 358 calls (51 a day), hit rate 0.804, chance 0.188, naive rule 0.411, lift 4.28x
    - 30d: 1617 calls (54 a day), hit rate 0.815, chance 0.187, naive rule 0.407, lift 4.37x
  - next: threshold 0.4558, hit rate recent 0.5445 / long run 0.5217
    - 6h: 17 calls (69 a day), hit rate 0.529, chance 0.173, lift 3.06x
    - 24h: 52 calls (52 a day), hit rate 0.538, chance 0.195, lift 2.76x
    - 7d: 392 calls (56 a day), hit rate 0.533, chance 0.188, lift 2.84x
    - 30d: 2685 calls (90 a day), hit rate 0.488, chance 0.187, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 352, 0.485; 0.40: 284, 0.557; 0.45: 233, 0.609; 0.50: 187, 0.658; 0.55: 150, 0.696; 0.60: 113, 0.746; 0.65: 76, 0.782; 0.70: 47, 0.820; 0.75: 28, 0.854; 0.80: 10, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.383; 0.35: 257, 0.422; 0.40: 160, 0.461; 0.45: 66, 0.494; 0.50: 10, 0.519; 0.55: 1, 0.447
- **K=8**: model 1794182400, labels learned 142968, probability skill vs chance 0.2085, widened contest next: False
  - now: threshold 0.5674, hit rate recent 0.6998 / long run 0.6913
    - 6h: 17 calls (70 a day), hit rate 0.824, chance 0.117, naive rule 0.348, lift 7.03x
    - 24h: 56 calls (56 a day), hit rate 0.679, chance 0.120, naive rule 0.348, lift 5.66x
    - 7d: 353 calls (50 a day), hit rate 0.694, chance 0.121, naive rule 0.340, lift 5.74x
    - 30d: 1529 calls (51 a day), hit rate 0.687, chance 0.120, naive rule 0.335, lift 5.70x
  - next: threshold 0.3617, hit rate recent 0.4415 / long run 0.4184
    - 6h: 21 calls (86 a day), hit rate 0.476, chance 0.117, lift 4.07x
    - 24h: 63 calls (63 a day), hit rate 0.476, chance 0.120, lift 3.97x
    - 7d: 441 calls (63 a day), hit rate 0.417, chance 0.121, lift 3.45x
    - 30d: 2628 calls (88 a day), hit rate 0.398, chance 0.120, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.428; 0.35: 192, 0.492; 0.40: 152, 0.539; 0.45: 118, 0.585; 0.50: 85, 0.637; 0.55: 60, 0.673; 0.60: 39, 0.714; 0.65: 24, 0.785; 0.70: 12, 0.816; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 171, 0.363; 0.35: 87, 0.392; 0.40: 23, 0.430; 0.45: 4, 0.434; 0.50: 1, 0.727
- **K=13**: model 1794096000, labels learned 142963, probability skill vs chance 0.1872, widened contest next: False
  - now: threshold 0.4545, hit rate recent 0.5932 / long run 0.5696
    - 6h: 14 calls (58 a day), hit rate 0.786, chance 0.097, naive rule 0.353, lift 8.09x
    - 24h: 48 calls (49 a day), hit rate 0.625, chance 0.082, naive rule 0.305, lift 7.58x
    - 7d: 363 calls (52 a day), hit rate 0.573, chance 0.079, naive rule 0.287, lift 7.26x
    - 30d: 1640 calls (55 a day), hit rate 0.562, chance 0.077, naive rule 0.282, lift 7.28x
  - next: threshold 0.2831, hit rate recent 0.3568 / long run 0.3307
    - 6h: 20 calls (83 a day), hit rate 0.400, chance 0.097, lift 4.12x
    - 24h: 65 calls (66 a day), hit rate 0.400, chance 0.082, lift 4.85x
    - 7d: 467 calls (67 a day), hit rate 0.321, chance 0.079, lift 4.07x
    - 30d: 1832 calls (61 a day), hit rate 0.323, chance 0.077, lift 4.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 133, 0.431; 0.35: 96, 0.479; 0.40: 68, 0.538; 0.45: 46, 0.583; 0.50: 31, 0.643; 0.55: 21, 0.666; 0.60: 12, 0.702; 0.65: 4, 0.667; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.327; 0.35: 13, 0.337; 0.40: 3, 0.410; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 18.284 | 1.11% | 0.883 | 0.550 | 0.249 | 0.500 | 0.309 |
| 6h | 16.302 | 2.39% | 0.881 | 0.483 | 0.251 | 0.506 | 0.488 |
| 24h | 17.160 | 3.38% | 0.903 | 0.495 | 0.250 | 0.513 | 0.561 |
| 7d | 16.329 | 6.24% | 0.901 | 0.500 | 0.250 | 0.505 | 0.723 |
| 30d | 15.526 | 4.71% | 0.900 | 0.500 | 0.250 | 0.501 | 0.699 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 18.490 | 18.461 | 18.480 | 18.418 | 18.572 | 18.650 | 18.314 | 18.230 | 18.252 | 18.284 |
| 6h | 16.700 | 16.424 | 16.375 | 16.303 | 16.824 | 16.607 | 16.277 | 16.224 | 16.247 | 16.302 |
| 24h | 17.761 | 17.296 | 17.288 | 17.302 | 17.595 | 17.418 | 17.130 | 17.099 | 17.117 | 17.160 |
| 7d | 17.415 | 16.462 | 16.429 | 16.440 | 16.619 | 16.729 | 16.297 | 16.288 | 16.293 | 16.329 |
| 30d | 16.293 | 15.682 | 15.629 | 15.574 | 15.814 | 15.788 | 15.513 | 15.493 | 15.496 | 15.526 |

## Next candle

- candle starting 2026-11-10 10:59 UTC, last close 2088.66
- P(up) 0.5001, return quantiles (bp): {'05': -10.71, '10': -8.709, '25': -4.349, '40': -1.493, '50': 0.027, '60': 1.122, '75': 3.912, '90': 7.205, '95': 9.52}
- changepoint probability 0.0931, regime age 84.4 min
- agent weights: empirical 0.005, ewma 0.095, garch 0.115, har 0.131, bocpd 0.009, hmm 0.027, online_qr 0.266, lgbm 0.351

## Learning log

- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.32, 6.18, 17.35], current probabilities: [0.102, 0.889, 0.009]
- live generator: {'versions': 60, 'latest_effective': '2026-11-10 11:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.2, 'l_abs': 0.693, 'l_hi': 0.772, 'l_lo': 0.737, 'b05': 0.665, 'b25': 0.643, 'b75': 0.559, 'b95': 0.669}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.6], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.174, 1.53, 1.57, 1.69, 1.97, 2.878, 2.066, 2.24, 3.131, 3.037, 3.179, 3.185, 3.057, 3.647]}
- calibration offsets (in sigma): {'05': -0.001, '10': -0.062, '25': -0.035, '40': 0.002, '50': -0.01, '60': -0.032, '75': 0.015, '90': -0.038, '95': -0.069}
