# ETH-USD 60s candle generator - report

- generated: 2026-11-10 23:43 UTC
- last closed candle: 2026-11-10 23:42 UTC (staleness 1.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.516 (672) [0.478, 0.554] | 0.519 (2879) [0.502, 0.537] | 0.514 (6618) [0.503, 0.526] | 0.517 (3646) [0.500, 0.534] | 0.425 (94) | 0.500 | flat +0.018 (noise 0.027) |
| colour_clear | 0.531 (791) | 0.538 (5545) [0.519, 0.556] | 0.543 (23828) [0.537, 0.549] | 0.522 (54150) [0.517, 0.528] | 0.543 (29912) [0.538, 0.548] | 0.545 (769) | 0.500 | flat -0.002 (noise 0.012) |
| colour_confident | 0.640 (50) | 0.585 (995) [0.572, 0.608] | 0.591 (4371) [0.582, 0.601] | 0.595 (5595) [0.585, 0.606] | 0.595 (5595) [0.585, 0.606] | 0.455 (88) | 0.500 | flat +0.010 (noise 0.022) |
| colour_next | 0.529 (1436) | 0.531 (9970) [0.519, 0.544] | 0.530 (42849) [0.526, 0.534] | 0.517 (98560) [0.513, 0.521] | 0.530 (54211) [0.526, 0.534] | 0.519 (1416) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.503 (139580) [0.501, 0.504] | 0.502 (599886) [0.500, 0.503] | 0.501 (1379840) [0.500, 0.502] | 0.501 (758954) [0.500, 0.502] | 0.496 (19824) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.500 (2) | 0.616 (263) [0.560, 0.634] | 0.623 (1161) [0.607, 0.638] | 0.630 (1493) [0.614, 0.647] | 0.630 (1493) [0.614, 0.647] | 0.733 (15) | 0.500 | flat -0.003 (noise 0.044) |
| reversal_k13_next | 0.358 (67) | 0.331 (465) [0.305, 0.361] | 0.324 (1833) [0.309, 0.338] | 0.313 (4551) [0.303, 0.323] | 0.325 (2446) [0.313, 0.336] | 0.375 (72) | 0.077 | flat -0.025 (noise 0.034) |
| reversal_k13_now | 0.537 (41) | 0.575 (360) [0.547, 0.605] | 0.559 (1641) [0.540, 0.578] | 0.573 (3558) [0.560, 0.586] | 0.567 (2086) [0.549, 0.585] | 0.646 (48) | 0.077 | flat -0.006 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.615 (369) [0.582, 0.646] | 0.591 (2864) [0.580, 0.603] | 0.588 (6005) [0.579, 0.597] | 0.589 (3565) [0.578, 0.599] | 0.532 (47) | 0.294 | flat +0.017 (noise 0.030) |
| reversal_k3_now | 0.909 (55) | 0.919 (396) [0.910, 0.930] | 0.933 (1725) [0.922, 0.943] | 0.936 (3963) [0.930, 0.942] | 0.931 (2200) [0.923, 0.940] | 0.919 (62) | 0.294 | flat -0.015 (noise 0.018) |
| reversal_k5_next | 0.513 (37) | 0.524 (393) [0.498, 0.550] | 0.487 (2679) [0.472, 0.504] | 0.485 (5338) [0.474, 0.497] | 0.480 (3348) [0.466, 0.495] | 0.525 (61) | 0.187 | flat -0.019 (noise 0.036) |
| reversal_k5_now | 0.641 (39) | 0.791 (349) [0.749, 0.826] | 0.813 (1607) [0.800, 0.824] | 0.825 (3666) [0.816, 0.835] | 0.816 (2055) [0.804, 0.826] | 0.829 (70) | 0.187 | flat -0.031 (noise 0.028) |
| reversal_k8_next | 0.462 (65) | 0.417 (441) [0.388, 0.449] | 0.395 (2636) [0.380, 0.409] | 0.395 (5432) [0.385, 0.406] | 0.395 (3326) [0.382, 0.407] | 0.435 (69) | 0.121 | flat -0.018 (noise 0.031) |
| reversal_k8_now | 0.646 (48) | 0.691 (349) [0.670, 0.710] | 0.684 (1527) [0.665, 0.702] | 0.700 (3582) [0.686, 0.714] | 0.689 (1995) [0.672, 0.706] | 0.737 (57) | 0.121 | flat -0.026 (noise 0.034) |
| overall | 0.506 (22029) | 0.506 (153344) [0.505, 0.508] | 0.505 (662126) [0.504, 0.507] | 0.504 (1521113) [0.503, 0.505] | 0.505 (837832) [0.504, 0.506] | 0.500 (21820) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07703, 0.1173] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5302, 'levels': [{'threshold': 0.07703, 'calls_per_day': 143.0, 'win_rate': 0.5702}, {'threshold': 0.1173, 'calls_per_day': 35.6, 'win_rate': 0.623}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42861, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15354 | 0.340 | 0.531 (15053) | 0.567 (2497) | 0.740 (2569) |
| volatility: normal | 15354 | 0.368 | 0.534 (15286) | 0.607 (1429) | 0.751 (2310) |
| volatility: wild | 15354 | 0.385 | 0.525 (15313) | 0.616 (808) | 0.771 (2108) |
| session: Asia 00-08 | 15360 | 0.364 | 0.537 (15220) | 0.596 (1676) | 0.755 (2297) |
| session: Europe 08-13 | 9600 | 0.357 | 0.534 (9489) | 0.588 (1250) | 0.753 (1556) |
| session: US 13-21 | 15360 | 0.371 | 0.527 (15245) | 0.588 (1243) | 0.753 (2328) |
| session: late 21-24 | 5742 | 0.358 | 0.515 (5698) | 0.561 (565) | 0.748 (806) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.370 | 0.372 | 0.287 | 0.287 | 0.517 | 0.263 | 0.477 | 1.105 |
| 6h | 360 | 0.375 | 0.368 | 0.293 | 0.318 | 0.500 | 0.259 | 0.492 | 1.294 |
| 24h | 1440 | 0.379 | 0.374 | 0.300 | 0.329 | 0.521 | 0.267 | 0.492 | 1.204 |
| 7d | 10080 | 0.369 | 0.363 | 0.281 | 0.312 | 0.530 | 0.264 | 0.474 | 1.406 |
| 30d | 43200 | 0.367 | 0.359 | 0.278 | 0.310 | 0.530 | 0.264 | 0.470 | 1.255 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.370 / 0.517 / 0.900; 2: 0.366 / 0.467 / 0.917; 3: 0.360 / 0.483 / 0.917; 4: 0.348 / 0.433 / 0.983; 5: 0.352 / 0.467 / 1.000; 6: 0.325 / 0.350 / 0.950; 7: 0.359 / 0.500 / 0.817; 8: 0.360 / 0.500 / 0.967; 9: 0.350 / 0.433 / 0.983; 10: 0.372 / 0.533 / 0.850; 11: 0.387 / 0.550 / 0.850; 12: 0.350 / 0.450 / 0.817; 13: 0.357 / 0.467 / 0.850; 14: 0.358 / 0.533 / 0.900; 15: 0.320 / 0.350 / 0.850
- 6h: 1: 0.375 / 0.500 / 0.886; 2: 0.359 / 0.472 / 0.911; 3: 0.383 / 0.539 / 0.917; 4: 0.371 / 0.494 / 0.956; 5: 0.364 / 0.492 / 0.956; 6: 0.356 / 0.453 / 0.928; 7: 0.369 / 0.517 / 0.864; 8: 0.373 / 0.497 / 0.928; 9: 0.372 / 0.494 / 0.944; 10: 0.372 / 0.514 / 0.897; 11: 0.367 / 0.506 / 0.894; 12: 0.369 / 0.494 / 0.875; 13: 0.378 / 0.517 / 0.889; 14: 0.365 / 0.486 / 0.897; 15: 0.365 / 0.475 / 0.872
- 24h: 1: 0.379 / 0.521 / 0.899; 2: 0.365 / 0.480 / 0.902; 3: 0.368 / 0.513 / 0.903; 4: 0.363 / 0.483 / 0.905; 5: 0.361 / 0.492 / 0.899; 6: 0.359 / 0.480 / 0.904; 7: 0.365 / 0.502 / 0.899; 8: 0.364 / 0.500 / 0.897; 9: 0.366 / 0.501 / 0.898; 10: 0.369 / 0.513 / 0.895; 11: 0.365 / 0.512 / 0.891; 12: 0.357 / 0.483 / 0.886; 13: 0.365 / 0.511 / 0.885; 14: 0.361 / 0.492 / 0.887; 15: 0.358 / 0.480 / 0.882
- 7d: 1: 0.369 / 0.530 / 0.898; 2: 0.356 / 0.488 / 0.901; 3: 0.360 / 0.514 / 0.901; 4: 0.355 / 0.496 / 0.901; 5: 0.356 / 0.501 / 0.900; 6: 0.353 / 0.495 / 0.900; 7: 0.354 / 0.498 / 0.899; 8: 0.354 / 0.501 / 0.900; 9: 0.357 / 0.509 / 0.900; 10: 0.355 / 0.507 / 0.899; 11: 0.354 / 0.506 / 0.899; 12: 0.354 / 0.507 / 0.898; 13: 0.352 / 0.495 / 0.898; 14: 0.354 / 0.507 / 0.898; 15: 0.351 / 0.495 / 0.897
- 30d: 1: 0.367 / 0.530 / 0.898; 2: 0.354 / 0.494 / 0.900; 3: 0.357 / 0.511 / 0.900; 4: 0.353 / 0.497 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.500 / 0.900; 7: 0.352 / 0.499 / 0.900; 8: 0.352 / 0.504 / 0.900; 9: 0.353 / 0.504 / 0.900; 10: 0.352 / 0.504 / 0.900; 11: 0.350 / 0.500 / 0.900; 12: 0.351 / 0.504 / 0.900; 13: 0.350 / 0.499 / 0.900; 14: 0.350 / 0.501 / 0.900; 15: 0.350 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.089 (body 0.065, range 0.114); 'price stays where it was' would score 0.091; colour right 0.467; typical miss of the close 10.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.099 (body 0.062, range 0.136); 'price stays where it was' would score 0.115; colour right 0.475; typical miss of the close 13.3 bp; chain ended on the right side 0.292 of 24 chains; n=360
- 24h: match 0.104 (body 0.065, range 0.144); 'price stays where it was' would score 0.106; colour right 0.489; typical miss of the close 13.7 bp; chain ended on the right side 0.438 of 96 chains; n=1440
- 7d: match 0.122 (body 0.082, range 0.162); 'price stays where it was' would score 0.123; colour right 0.502; typical miss of the close 9.3 bp; chain ended on the right side 0.521 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.128; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.7; 2: 0.200 / 5.5; 3: 0.165 / 7.1; 4: 0.131 / 7.3; 5: 0.126 / 8.0; 6: 0.115 / 8.9; 7: 0.110 / 9.1; 8: 0.097 / 10.2; 9: 0.091 / 10.2; 10: 0.092 / 10.7; 11: 0.087 / 10.7; 12: 0.078 / 11.1; 13: 0.073 / 11.6; 14: 0.070 / 12.1; 15: 0.066 / 12.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 143736, probability skill vs chance 0.2303, widened contest next: True
  - now: threshold 0.8383, hit rate recent 0.9065 / long run 0.9261
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.237, naive rule 0.402, lift 3.42x
    - 24h: 62 calls (62 a day), hit rate 0.919, chance 0.274, naive rule 0.474, lift 3.35x
    - 7d: 406 calls (58 a day), hit rate 0.921, chance 0.296, naive rule 0.502, lift 3.11x
    - 30d: 1717 calls (57 a day), hit rate 0.933, chance 0.293, naive rule 0.494, lift 3.18x
  - next: threshold 0.5664, hit rate recent 0.5676 / long run 0.6041
    - 6h: 9 calls (37 a day), hit rate 0.222, chance 0.237, lift 0.94x
    - 24h: 47 calls (47 a day), hit rate 0.532, chance 0.274, lift 1.94x
    - 7d: 352 calls (50 a day), hit rate 0.619, chance 0.296, lift 2.09x
    - 30d: 2826 calls (94 a day), hit rate 0.590, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.498; 0.35: 533, 0.522; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 356, 0.696; 0.55: 309, 0.740; 0.60: 260, 0.785; 0.65: 219, 0.811; 0.70: 173, 0.844; 0.75: 139, 0.875; 0.80: 91, 0.905; 0.85: 46, 0.947; 0.90: 4, 0.992
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 498, 0.463; 0.40: 399, 0.500; 0.45: 300, 0.535; 0.50: 194, 0.568; 0.55: 87, 0.578; 0.60: 12, 0.642; 0.65: 1, 0.600
- **K=5**: model 1794268800, labels learned 143734, probability skill vs chance 0.2185, widened contest next: False
  - now: threshold 0.6819, hit rate recent 0.7793 / long run 0.8071
    - 6h: 20 calls (82 a day), hit rate 0.700, chance 0.162, naive rule 0.332, lift 4.32x
    - 24h: 70 calls (70 a day), hit rate 0.829, chance 0.183, naive rule 0.396, lift 4.53x
    - 7d: 368 calls (53 a day), hit rate 0.799, chance 0.187, naive rule 0.409, lift 4.26x
    - 30d: 1627 calls (54 a day), hit rate 0.813, chance 0.186, naive rule 0.405, lift 4.37x
  - next: threshold 0.4566, hit rate recent 0.5195 / long run 0.5198
    - 6h: 14 calls (57 a day), hit rate 0.429, chance 0.162, lift 2.65x
    - 24h: 61 calls (61 a day), hit rate 0.525, chance 0.183, lift 2.87x
    - 7d: 393 calls (56 a day), hit rate 0.532, chance 0.187, lift 2.84x
    - 30d: 2679 calls (89 a day), hit rate 0.488, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 352, 0.482; 0.40: 285, 0.554; 0.45: 233, 0.607; 0.50: 187, 0.656; 0.55: 150, 0.694; 0.60: 112, 0.744; 0.65: 75, 0.781; 0.70: 47, 0.819; 0.75: 28, 0.852; 0.80: 10, 0.873
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.383; 0.35: 257, 0.421; 0.40: 160, 0.460; 0.45: 65, 0.493; 0.50: 10, 0.508; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 143731, probability skill vs chance 0.2112, widened contest next: False
  - now: threshold 0.5665, hit rate recent 0.723 / long run 0.6946
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.133, naive rule 0.329, lift 5.20x
    - 24h: 57 calls (57 a day), hit rate 0.737, chance 0.125, naive rule 0.339, lift 5.88x
    - 7d: 357 calls (51 a day), hit rate 0.695, chance 0.122, naive rule 0.343, lift 5.68x
    - 30d: 1524 calls (51 a day), hit rate 0.686, chance 0.120, naive rule 0.334, lift 5.69x
  - next: threshold 0.3625, hit rate recent 0.4343 / long run 0.4184
    - 6h: 13 calls (54 a day), hit rate 0.462, chance 0.133, lift 3.46x
    - 24h: 69 calls (70 a day), hit rate 0.435, chance 0.125, lift 3.47x
    - 7d: 445 calls (64 a day), hit rate 0.420, chance 0.122, lift 3.44x
    - 30d: 2621 calls (87 a day), hit rate 0.397, chance 0.120, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 192, 0.492; 0.40: 152, 0.538; 0.45: 118, 0.584; 0.50: 84, 0.637; 0.55: 59, 0.673; 0.60: 39, 0.712; 0.65: 24, 0.780; 0.70: 12, 0.814; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 171, 0.364; 0.35: 87, 0.392; 0.40: 23, 0.425; 0.45: 4, 0.432; 0.50: 1, 0.727
- **K=13**: model 1794096000, labels learned 143726, probability skill vs chance 0.1937, widened contest next: False
  - now: threshold 0.4532, hit rate recent 0.6169 / long run 0.573
    - 6h: 9 calls (38 a day), hit rate 0.667, chance 0.083, naive rule 0.314, lift 8.05x
    - 24h: 48 calls (49 a day), hit rate 0.646, chance 0.084, naive rule 0.302, lift 7.73x
    - 7d: 352 calls (50 a day), hit rate 0.571, chance 0.079, naive rule 0.289, lift 7.24x
    - 30d: 1638 calls (55 a day), hit rate 0.561, chance 0.077, naive rule 0.281, lift 7.26x
  - next: threshold 0.2832, hit rate recent 0.3821 / long run 0.3352
    - 6h: 19 calls (80 a day), hit rate 0.421, chance 0.083, lift 5.08x
    - 24h: 72 calls (73 a day), hit rate 0.375, chance 0.084, lift 4.49x
    - 7d: 472 calls (68 a day), hit rate 0.326, chance 0.079, lift 4.14x
    - 30d: 1838 calls (61 a day), hit rate 0.324, chance 0.077, lift 4.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.431; 0.35: 96, 0.479; 0.40: 68, 0.537; 0.45: 46, 0.583; 0.50: 31, 0.642; 0.55: 21, 0.664; 0.60: 12, 0.699; 0.65: 4, 0.670; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.329; 0.35: 13, 0.340; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.232 | 4.20% | 0.917 | 0.433 | 0.252 | 0.483 | 0.441 |
| 6h | 16.186 | 1.62% | 0.886 | 0.511 | 0.252 | 0.464 | 0.483 |
| 24h | 19.661 | 4.79% | 0.894 | 0.499 | 0.251 | 0.497 | 0.509 |
| 7d | 17.002 | 6.38% | 0.900 | 0.501 | 0.251 | 0.501 | 0.690 |
| 30d | 15.753 | 4.71% | 0.900 | 0.500 | 0.250 | 0.501 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.812 | 13.474 | 13.391 | 13.385 | 13.587 | 13.421 | 13.124 | 13.183 | 13.209 | 13.232 |
| 6h | 16.452 | 16.242 | 16.259 | 16.316 | 16.402 | 16.298 | 16.089 | 16.096 | 16.114 | 16.186 |
| 24h | 20.649 | 19.811 | 19.815 | 19.745 | 20.189 | 19.941 | 19.638 | 19.631 | 19.629 | 19.661 |
| 7d | 18.162 | 17.147 | 17.116 | 17.125 | 17.318 | 17.414 | 16.973 | 16.962 | 16.968 | 17.002 |
| 30d | 16.531 | 15.910 | 15.858 | 15.803 | 16.045 | 16.016 | 15.739 | 15.720 | 15.723 | 15.753 |

## Next candle

- candle starting 2026-11-10 23:42 UTC, last close 2051.5
- P(up) 0.4746, return quantiles (bp): {'05': -6.802, '10': -4.897, '25': -2.488, '40': -1.285, '50': -0.296, '60': 0.89, '75': 2.539, '90': 5.202, '95': 6.918}
- changepoint probability 0.0385, regime age 126.5 min
- agent weights: empirical 0.003, ewma 0.094, garch 0.091, har 0.113, bocpd 0.013, hmm 0.050, online_qr 0.318, lgbm 0.318

## Learning log

- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- HMM volatility states (sd, bp per minute): [2.27, 5.7, 16.94], current probabilities: [0.049, 0.941, 0.009]
- live generator: {'versions': 60, 'latest_effective': '2026-11-10 23:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.26, 'l_abs': 0.631, 'l_hi': 0.79, 'l_lo': 0.737, 'b05': 0.709, 'b25': 0.69, 'b75': 0.616, 'b95': 0.718}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.5, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.316, 1.648, 1.945, 2.36, 2.489, 3.564, 3.189, 3.067, 4.036, 4.242, 4.906, 4.819, 5.01, 5.518]}
- calibration offsets (in sigma): {'05': 0.0305, '10': 0.101, '25': 0.0625, '40': -0.036, '50': -0.035, '60': 0.016, '75': 0.0175, '90': 0.019, '95': -0.0105}
