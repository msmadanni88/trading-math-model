# ETH-USD 60s candle generator - report

- generated: 2026-11-10 02:59 UTC
- last closed candle: 2026-11-10 02:58 UTC (staleness 1.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.516 (672) [0.478, 0.554] | 0.519 (2879) [0.502, 0.537] | 0.514 (6618) [0.503, 0.526] | 0.517 (3646) [0.500, 0.534] | 0.364 (11) | 0.500 | flat +0.018 (noise 0.027) |
| colour_clear | 0.531 (791) | 0.538 (5545) [0.519, 0.556] | 0.543 (23828) [0.537, 0.549] | 0.522 (54150) [0.517, 0.528] | 0.543 (29912) [0.538, 0.548] | 0.578 (102) | 0.500 | flat -0.002 (noise 0.012) |
| colour_confident | 0.640 (50) | 0.585 (995) [0.572, 0.608] | 0.591 (4371) [0.582, 0.601] | 0.595 (5595) [0.585, 0.606] | 0.595 (5595) [0.585, 0.606] | 0.273 (11) | 0.500 | flat +0.010 (noise 0.022) |
| colour_next | 0.529 (1436) | 0.531 (9970) [0.519, 0.544] | 0.530 (42849) [0.526, 0.534] | 0.517 (98560) [0.513, 0.521] | 0.530 (54211) [0.526, 0.534] | 0.568 (176) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.503 (139580) [0.501, 0.504] | 0.502 (599886) [0.500, 0.503] | 0.501 (1379840) [0.500, 0.502] | 0.501 (758954) [0.500, 0.502] | 0.492 (2464) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.500 (2) | 0.616 (263) [0.560, 0.634] | 0.623 (1161) [0.607, 0.638] | 0.630 (1493) [0.614, 0.647] | 0.630 (1493) [0.614, 0.647] | 0.000 (1) | 0.500 | flat -0.003 (noise 0.044) |
| reversal_k13_next | 0.358 (67) | 0.331 (465) [0.305, 0.361] | 0.324 (1833) [0.309, 0.338] | 0.313 (4551) [0.303, 0.323] | 0.325 (2446) [0.313, 0.336] | 0.111 (9) | 0.077 | flat -0.025 (noise 0.034) |
| reversal_k13_now | 0.537 (41) | 0.575 (360) [0.547, 0.605] | 0.559 (1641) [0.540, 0.578] | 0.573 (3558) [0.560, 0.586] | 0.567 (2086) [0.549, 0.585] | 0.500 (6) | 0.077 | flat -0.006 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.615 (369) [0.582, 0.646] | 0.591 (2864) [0.580, 0.603] | 0.588 (6005) [0.579, 0.597] | 0.589 (3565) [0.578, 0.599] | 0.375 (8) | 0.294 | flat +0.017 (noise 0.030) |
| reversal_k3_now | 0.909 (55) | 0.919 (396) [0.910, 0.930] | 0.933 (1725) [0.922, 0.943] | 0.936 (3963) [0.930, 0.942] | 0.931 (2200) [0.923, 0.940] | 0.917 (12) | 0.294 | flat -0.015 (noise 0.018) |
| reversal_k5_next | 0.513 (37) | 0.524 (393) [0.498, 0.550] | 0.487 (2679) [0.472, 0.504] | 0.485 (5338) [0.474, 0.497] | 0.480 (3348) [0.466, 0.495] | 0.571 (7) | 0.187 | flat -0.019 (noise 0.036) |
| reversal_k5_now | 0.641 (39) | 0.791 (349) [0.749, 0.826] | 0.813 (1607) [0.800, 0.824] | 0.825 (3666) [0.816, 0.835] | 0.816 (2055) [0.804, 0.826] | 0.889 (9) | 0.187 | flat -0.031 (noise 0.028) |
| reversal_k8_next | 0.462 (65) | 0.417 (441) [0.388, 0.449] | 0.395 (2636) [0.380, 0.409] | 0.395 (5432) [0.385, 0.406] | 0.395 (3326) [0.382, 0.407] | 0.333 (6) | 0.121 | flat -0.018 (noise 0.031) |
| reversal_k8_now | 0.646 (48) | 0.691 (349) [0.670, 0.710] | 0.684 (1527) [0.665, 0.702] | 0.700 (3582) [0.686, 0.714] | 0.689 (1995) [0.672, 0.706] | 0.429 (7) | 0.121 | flat -0.026 (noise 0.034) |
| overall | 0.506 (22029) | 0.506 (153344) [0.505, 0.508] | 0.505 (662126) [0.504, 0.507] | 0.504 (1521113) [0.503, 0.505] | 0.505 (837832) [0.504, 0.506] | 0.498 (2715) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07752, 0.1178] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5315, 'levels': [{'threshold': 0.07752, 'calls_per_day': 141.9, 'win_rate': 0.5837}, {'threshold': 0.1178, 'calls_per_day': 35.6, 'win_rate': 0.6111}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42850, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14940 | 0.339 | 0.531 (14641) | 0.567 (2434) | 0.740 (2514) |
| volatility: normal | 14939 | 0.368 | 0.535 (14871) | 0.612 (1423) | 0.754 (2213) |
| volatility: wild | 14939 | 0.384 | 0.525 (14900) | 0.616 (800) | 0.764 (2057) |
| session: Asia 00-08 | 15058 | 0.364 | 0.537 (14920) | 0.598 (1644) | 0.755 (2246) |
| session: Europe 08-13 | 9300 | 0.357 | 0.534 (9190) | 0.588 (1233) | 0.750 (1499) |
| session: US 13-21 | 14880 | 0.371 | 0.528 (14766) | 0.591 (1223) | 0.751 (2262) |
| session: late 21-24 | 5580 | 0.357 | 0.516 (5536) | 0.562 (557) | 0.747 (777) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.401 | 0.404 | 0.317 | 0.317 | 0.542 | 0.280 | 0.522 | 1.113 |
| 6h | 360 | 0.388 | 0.383 | 0.309 | 0.340 | 0.564 | 0.283 | 0.494 | 1.281 |
| 24h | 1440 | 0.386 | 0.382 | 0.299 | 0.341 | 0.530 | 0.269 | 0.504 | 1.215 |
| 7d | 10080 | 0.368 | 0.362 | 0.278 | 0.309 | 0.532 | 0.264 | 0.472 | 1.361 |
| 30d | 43200 | 0.366 | 0.358 | 0.277 | 0.308 | 0.531 | 0.264 | 0.468 | 1.261 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.401 / 0.542 / 0.967; 2: 0.357 / 0.322 / 0.783; 3: 0.356 / 0.441 / 0.767; 4: 0.379 / 0.407 / 0.850; 5: 0.387 / 0.559 / 0.850; 6: 0.373 / 0.458 / 0.800; 7: 0.390 / 0.525 / 0.767; 8: 0.376 / 0.458 / 0.850; 9: 0.400 / 0.542 / 0.800; 10: 0.391 / 0.475 / 0.683; 11: 0.378 / 0.525 / 0.700; 12: 0.386 / 0.475 / 0.700; 13: 0.382 / 0.542 / 0.717; 14: 0.385 / 0.441 / 0.767; 15: 0.395 / 0.492 / 0.817
- 6h: 1: 0.388 / 0.564 / 0.914; 2: 0.371 / 0.461 / 0.747; 3: 0.358 / 0.492 / 0.742; 4: 0.355 / 0.455 / 0.817; 5: 0.370 / 0.534 / 0.842; 6: 0.347 / 0.425 / 0.772; 7: 0.370 / 0.520 / 0.714; 8: 0.369 / 0.506 / 0.819; 9: 0.380 / 0.559 / 0.822; 10: 0.368 / 0.497 / 0.711; 11: 0.380 / 0.553 / 0.739; 12: 0.378 / 0.547 / 0.753; 13: 0.365 / 0.517 / 0.781; 14: 0.361 / 0.480 / 0.764; 15: 0.368 / 0.511 / 0.794
- 24h: 1: 0.386 / 0.530 / 0.919; 2: 0.378 / 0.491 / 0.872; 3: 0.379 / 0.515 / 0.872; 4: 0.368 / 0.473 / 0.885; 5: 0.378 / 0.519 / 0.890; 6: 0.365 / 0.470 / 0.878; 7: 0.374 / 0.502 / 0.867; 8: 0.372 / 0.503 / 0.885; 9: 0.378 / 0.520 / 0.885; 10: 0.376 / 0.510 / 0.868; 11: 0.378 / 0.524 / 0.872; 12: 0.376 / 0.521 / 0.874; 13: 0.369 / 0.493 / 0.879; 14: 0.370 / 0.498 / 0.879; 15: 0.374 / 0.497 / 0.884
- 7d: 1: 0.368 / 0.532 / 0.898; 2: 0.356 / 0.491 / 0.898; 3: 0.360 / 0.516 / 0.897; 4: 0.355 / 0.497 / 0.899; 5: 0.356 / 0.503 / 0.900; 6: 0.352 / 0.499 / 0.898; 7: 0.353 / 0.498 / 0.898; 8: 0.353 / 0.500 / 0.900; 9: 0.356 / 0.511 / 0.900; 10: 0.354 / 0.503 / 0.899; 11: 0.355 / 0.507 / 0.898; 12: 0.354 / 0.510 / 0.898; 13: 0.352 / 0.494 / 0.899; 14: 0.354 / 0.507 / 0.899; 15: 0.352 / 0.500 / 0.900
- 30d: 1: 0.366 / 0.531 / 0.898; 2: 0.353 / 0.495 / 0.899; 3: 0.356 / 0.510 / 0.899; 4: 0.352 / 0.497 / 0.900; 5: 0.353 / 0.504 / 0.900; 6: 0.351 / 0.500 / 0.899; 7: 0.351 / 0.499 / 0.899; 8: 0.351 / 0.504 / 0.899; 9: 0.352 / 0.504 / 0.899; 10: 0.351 / 0.503 / 0.899; 11: 0.349 / 0.500 / 0.899; 12: 0.350 / 0.504 / 0.899; 13: 0.349 / 0.499 / 0.899; 14: 0.349 / 0.501 / 0.899; 15: 0.349 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.031 (body 0.019, range 0.043); 'price stays where it was' would score 0.040; colour right 0.492; typical miss of the close 14.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.091 (body 0.062, range 0.120); 'price stays where it was' would score 0.075; colour right 0.522; typical miss of the close 11.8 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.122 (body 0.080, range 0.164); 'price stays where it was' would score 0.113; colour right 0.495; typical miss of the close 13.0 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.123; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.516 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.7 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.5; 2: 0.201 / 5.3; 3: 0.167 / 6.9; 4: 0.132 / 7.1; 5: 0.126 / 7.8; 6: 0.115 / 8.7; 7: 0.110 / 9.0; 8: 0.096 / 9.9; 9: 0.090 / 9.9; 10: 0.092 / 10.4; 11: 0.087 / 10.4; 12: 0.078 / 10.8; 13: 0.073 / 11.3; 14: 0.071 / 11.8; 15: 0.066 / 12.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 142492, probability skill vs chance 0.2219, widened contest next: False
  - now: threshold 0.8379, hit rate recent 0.908 / long run 0.9267
    - 6h: 18 calls (73 a day), hit rate 0.833, chance 0.328, naive rule 0.528, lift 2.54x
    - 24h: 59 calls (59 a day), hit rate 0.915, chance 0.295, naive rule 0.505, lift 3.10x
    - 7d: 398 calls (57 a day), hit rate 0.920, chance 0.299, naive rule 0.505, lift 3.07x
    - 30d: 1724 calls (57 a day), hit rate 0.933, chance 0.295, naive rule 0.497, lift 3.17x
  - next: threshold 0.5661, hit rate recent 0.5941 / long run 0.6069
    - 6h: 12 calls (49 a day), hit rate 0.417, chance 0.328, lift 1.27x
    - 24h: 45 calls (45 a day), hit rate 0.578, chance 0.295, lift 1.96x
    - 7d: 361 calls (52 a day), hit rate 0.623, chance 0.299, lift 2.08x
    - 30d: 2855 calls (95 a day), hit rate 0.591, chance 0.295, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.500; 0.35: 533, 0.525; 0.40: 474, 0.581; 0.45: 406, 0.651; 0.50: 356, 0.698; 0.55: 308, 0.743; 0.60: 260, 0.786; 0.65: 219, 0.812; 0.70: 173, 0.843; 0.75: 139, 0.874; 0.80: 92, 0.905; 0.85: 46, 0.948; 0.90: 4, 0.993
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.430; 0.35: 498, 0.464; 0.40: 399, 0.502; 0.45: 301, 0.537; 0.50: 194, 0.569; 0.55: 87, 0.577; 0.60: 12, 0.650; 0.65: 1, 0.619
- **K=5**: model 1794268800, labels learned 142490, probability skill vs chance 0.2083, widened contest next: True
  - now: threshold 0.6822, hit rate recent 0.7462 / long run 0.806
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.202, naive rule 0.429, lift 4.20x
    - 24h: 43 calls (43 a day), hit rate 0.721, chance 0.188, naive rule 0.413, lift 3.83x
    - 7d: 349 calls (50 a day), hit rate 0.791, chance 0.187, naive rule 0.408, lift 4.22x
    - 30d: 1610 calls (54 a day), hit rate 0.814, chance 0.187, naive rule 0.407, lift 4.36x
  - next: threshold 0.4555, hit rate recent 0.5418 / long run 0.5201
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.202, lift 2.70x
    - 24h: 39 calls (39 a day), hit rate 0.513, chance 0.188, lift 2.72x
    - 7d: 390 calls (56 a day), hit rate 0.528, chance 0.187, lift 2.82x
    - 30d: 2685 calls (90 a day), hit rate 0.488, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 351, 0.486; 0.40: 284, 0.557; 0.45: 233, 0.608; 0.50: 187, 0.657; 0.55: 150, 0.695; 0.60: 113, 0.744; 0.65: 76, 0.781; 0.70: 46, 0.819; 0.75: 28, 0.851; 0.80: 10, 0.873
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.383; 0.35: 256, 0.421; 0.40: 160, 0.460; 0.45: 66, 0.493; 0.50: 11, 0.520; 0.55: 1, 0.447
- **K=8**: model 1794182400, labels learned 142487, probability skill vs chance 0.1954, widened contest next: True
  - now: threshold 0.5686, hit rate recent 0.6483 / long run 0.6872
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.123, naive rule 0.296, lift 4.43x
    - 24h: 49 calls (49 a day), hit rate 0.653, chance 0.120, naive rule 0.344, lift 5.46x
    - 7d: 350 calls (50 a day), hit rate 0.686, chance 0.120, naive rule 0.338, lift 5.69x
    - 30d: 1526 calls (51 a day), hit rate 0.683, chance 0.120, naive rule 0.335, lift 5.67x
  - next: threshold 0.3616, hit rate recent 0.4182 / long run 0.4155
    - 6h: 8 calls (33 a day), hit rate 0.375, chance 0.123, lift 3.04x
    - 24h: 62 calls (62 a day), hit rate 0.452, chance 0.120, lift 3.77x
    - 7d: 436 calls (62 a day), hit rate 0.417, chance 0.120, lift 3.47x
    - 30d: 2632 calls (88 a day), hit rate 0.396, chance 0.120, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.429; 0.35: 192, 0.492; 0.40: 152, 0.538; 0.45: 118, 0.584; 0.50: 85, 0.636; 0.55: 60, 0.670; 0.60: 39, 0.711; 0.65: 24, 0.782; 0.70: 12, 0.810; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 171, 0.361; 0.35: 88, 0.390; 0.40: 23, 0.426; 0.45: 4, 0.439; 0.50: 1, 0.727
- **K=13**: model 1794096000, labels learned 142482, probability skill vs chance 0.1741, widened contest next: False
  - now: threshold 0.4544, hit rate recent 0.5545 / long run 0.5661
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.078, naive rule 0.272, lift 7.96x
    - 24h: 39 calls (39 a day), hit rate 0.590, chance 0.082, naive rule 0.312, lift 7.18x
    - 7d: 359 calls (51 a day), hit rate 0.571, chance 0.079, naive rule 0.286, lift 7.27x
    - 30d: 1641 calls (55 a day), hit rate 0.559, chance 0.077, naive rule 0.281, lift 7.26x
  - next: threshold 0.284, hit rate recent 0.3251 / long run 0.3266
    - 6h: 14 calls (59 a day), hit rate 0.143, chance 0.078, lift 1.82x
    - 24h: 64 calls (65 a day), hit rate 0.359, chance 0.082, lift 4.37x
    - 7d: 462 calls (66 a day), hit rate 0.325, chance 0.079, lift 4.13x
    - 30d: 1831 calls (61 a day), hit rate 0.323, chance 0.077, lift 4.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 133, 0.430; 0.35: 96, 0.478; 0.40: 67, 0.536; 0.45: 46, 0.581; 0.50: 31, 0.641; 0.55: 20, 0.665; 0.60: 12, 0.703; 0.65: 4, 0.667; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.326; 0.35: 13, 0.342; 0.40: 3, 0.410; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.247 | 5.87% | 0.967 | 0.467 | 0.250 | 0.559 | 0.191 |
| 6h | 13.296 | 6.11% | 0.914 | 0.497 | 0.250 | 0.520 | 0.212 |
| 24h | 18.748 | 3.94% | 0.914 | 0.499 | 0.250 | 0.509 | 0.564 |
| 7d | 16.161 | 6.26% | 0.902 | 0.501 | 0.250 | 0.504 | 0.727 |
| 30d | 15.425 | 4.71% | 0.900 | 0.500 | 0.250 | 0.500 | 0.702 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.948 | 11.164 | 11.133 | 11.336 | 11.493 | 11.607 | 11.300 | 11.263 | 11.243 | 11.247 |
| 6h | 14.161 | 13.365 | 13.389 | 13.367 | 13.680 | 13.679 | 13.252 | 13.292 | 13.277 | 13.296 |
| 24h | 19.517 | 18.870 | 18.902 | 19.047 | 19.134 | 19.029 | 18.709 | 18.696 | 18.704 | 18.748 |
| 7d | 17.241 | 16.293 | 16.262 | 16.273 | 16.437 | 16.561 | 16.129 | 16.122 | 16.127 | 16.161 |
| 30d | 16.188 | 15.581 | 15.527 | 15.473 | 15.710 | 15.684 | 15.412 | 15.392 | 15.396 | 15.425 |

## Next candle

- candle starting 2026-11-10 02:58 UTC, last close 2119.09
- P(up) 0.5006, return quantiles (bp): {'05': -6.899, '10': -5.486, '25': -2.731, '40': -1.317, '50': 0.027, '60': 0.879, '75': 2.78, '90': 5.135, '95': 6.899}
- changepoint probability 0.0468, regime age 63.9 min
- agent weights: empirical 0.003, ewma 0.103, garch 0.100, har 0.060, bocpd 0.021, hmm 0.027, online_qr 0.345, lgbm 0.341

## Learning log

- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.32, 6.18, 17.35], current probabilities: [0.003, 0.982, 0.015]
- live generator: {'versions': 60, 'latest_effective': '2026-11-10 03:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.274, 'l_abs': 0.673, 'l_hi': 0.78, 'l_lo': 0.739, 'b05': 0.651, 'b25': 0.605, 'b75': 0.56, 'b95': 0.629}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [2.78, 3.481, 2.925, 2.792, 4.137, 6.29, 4.006, 4.09, 6.982, 6.379, 6.04, 5.587, 6.169, 5.452]}
- calibration offsets (in sigma): {'05': 0.0885, '10': 0.017, '25': -0.0175, '40': -0.082, '50': -0.015, '60': -0.038, '75': -0.0125, '90': -0.047, '95': -0.0685}
