# ETH-USD 60s candle generator - report

- generated: 2026-10-14 01:52 UTC
- last closed candle: 2026-10-14 01:52 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.489 (671) [0.448, 0.530] | 0.509 (2875) [0.489, 0.530] | 0.510 (4026) [0.494, 0.526] | 0.508 (1054) [0.473, 0.542] | 0.857 (7) | 0.500 | flat -0.035 (noise 0.034) |
| colour_clear | 0.526 (780) | 0.538 (5463) [0.532, 0.544] | 0.512 (23311) [0.504, 0.520] | 0.508 (32638) [0.502, 0.514] | 0.541 (8400) [0.535, 0.547] | 0.568 (74) | 0.500 | flat +0.018 (noise 0.013) |
| colour_confident | 0.633 (60) | 0.605 (926) [0.583, 0.636] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.000 (6) | 0.500 | flat -0.003 (noise 0.038) |
| colour_next | 0.514 (1433) | 0.523 (9974) [0.519, 0.527] | 0.510 (42868) [0.504, 0.515] | 0.507 (59997) [0.503, 0.512] | 0.527 (15648) [0.521, 0.533] | 0.589 (112) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.504 (20062) | 0.499 (139636) [0.496, 0.501] | 0.501 (600152) [0.500, 0.503] | 0.500 (839958) [0.499, 0.501] | 0.500 (219072) [0.497, 0.502] | 0.503 (1568) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.714 (7) | 0.676 (250) [0.633, 0.740] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | - | 0.500 | flat +0.043 (noise 0.052) |
| reversal_k13_next | 0.270 (74) | 0.321 (495) [0.299, 0.343] | 0.316 (2093) [0.302, 0.331] | 0.306 (2932) [0.294, 0.319] | 0.323 (827) [0.307, 0.338] | 0.125 (8) | 0.077 | flat +0.020 (noise 0.028) |
| reversal_k13_now | 0.651 (43) | 0.589 (353) [0.560, 0.621] | 0.592 (1488) [0.572, 0.614] | 0.584 (2066) [0.567, 0.601] | 0.591 (594) [0.562, 0.625] | 0.000 (3) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.539 (165) | 0.566 (664) [0.541, 0.592] | 0.585 (2478) [0.570, 0.600] | 0.584 (3466) [0.571, 0.597] | 0.575 (1026) [0.555, 0.599] | 0.667 (9) | 0.293 | flat -0.021 (noise 0.028) |
| reversal_k3_now | 0.977 (44) | 0.926 (417) [0.915, 0.941] | 0.939 (1717) [0.931, 0.947] | 0.937 (2410) [0.930, 0.945] | 0.926 (647) [0.917, 0.936] | 1.000 (2) | 0.293 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.481 (104) | 0.468 (524) [0.440, 0.488] | 0.484 (2110) [0.466, 0.502] | 0.484 (2911) [0.469, 0.500] | 0.462 (921) [0.439, 0.486] | 0.200 (5) | 0.187 | flat +0.004 (noise 0.029) |
| reversal_k5_now | 0.804 (46) | 0.809 (367) [0.784, 0.836] | 0.832 (1586) [0.816, 0.848] | 0.833 (2208) [0.819, 0.846] | 0.821 (597) [0.796, 0.845] | 0.000 (1) | 0.188 | flat -0.033 (noise 0.028) |
| reversal_k8_next | 0.407 (81) | 0.387 (607) [0.363, 0.414] | 0.411 (2117) [0.394, 0.429] | 0.396 (3040) [0.383, 0.410] | 0.395 (934) [0.375, 0.416] | 0.167 (6) | 0.122 | flat -0.013 (noise 0.030) |
| reversal_k8_now | 0.674 (46) | 0.669 (393) [0.639, 0.703] | 0.717 (1590) [0.696, 0.738] | 0.709 (2217) [0.692, 0.726] | 0.697 (630) [0.665, 0.730] | 0.250 (4) | 0.122 | flat -0.065 (noise 0.033) |
| overall | 0.506 (22194) | 0.502 (154101) [0.499, 0.505] | 0.504 (661074) [0.503, 0.505] | 0.503 (925231) [0.502, 0.504] | 0.503 (241950) [0.501, 0.506] | 0.505 (1725) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07732, 0.12] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5232, 'levels': [{'threshold': 0.07732, 'calls_per_day': 140.9, 'win_rate': 0.6048}, {'threshold': 0.12, 'calls_per_day': 35.3, 'win_rate': 0.664}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 14623, 'rate': 0.5289}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14918 | 0.334 | 0.519 (14670) | 0.598 (1197) | 0.779 (2407) |
| volatility: normal | 14917 | 0.360 | 0.510 (14855) | 0.598 (249) | 0.773 (2087) |
| volatility: wild | 14917 | 0.374 | 0.501 (14873) | 0.683 (101) | 0.772 (2094) |
| session: Asia 00-08 | 14992 | 0.353 | 0.514 (14885) | 0.599 (554) | 0.774 (2165) |
| session: Europe 08-13 | 9300 | 0.349 | 0.506 (9218) | 0.589 (377) | 0.781 (1423) |
| session: US 13-21 | 14880 | 0.366 | 0.508 (14780) | 0.588 (388) | 0.781 (2165) |
| session: late 21-24 | 5580 | 0.349 | 0.509 (5515) | 0.667 (228) | 0.751 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.420 | 0.394 | 0.266 | 0.266 | 0.633 | 0.329 | 0.511 | 1.039 |
| 6h | 360 | 0.358 | 0.343 | 0.267 | 0.287 | 0.513 | 0.252 | 0.464 | 1.006 |
| 24h | 1440 | 0.372 | 0.367 | 0.284 | 0.315 | 0.522 | 0.263 | 0.481 | 1.175 |
| 7d | 10080 | 0.356 | 0.349 | 0.273 | 0.301 | 0.524 | 0.257 | 0.454 | 1.259 |
| 30d | 43200 | 0.357 | 0.355 | 0.279 | 0.308 | 0.510 | 0.249 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.420 / 0.633 / 0.883; 2: 0.415 / 0.617 / 0.917; 3: 0.381 / 0.483 / 0.933; 4: 0.384 / 0.550 / 0.917; 5: 0.383 / 0.550 / 0.917; 6: 0.379 / 0.500 / 0.850; 7: 0.370 / 0.467 / 0.867; 8: 0.356 / 0.433 / 0.867; 9: 0.373 / 0.483 / 0.900; 10: 0.380 / 0.517 / 0.850; 11: 0.346 / 0.383 / 0.800; 12: 0.368 / 0.467 / 0.800; 13: 0.361 / 0.400 / 0.817; 14: 0.382 / 0.533 / 0.750; 15: 0.413 / 0.583 / 0.750
- 6h: 1: 0.358 / 0.513 / 0.892; 2: 0.355 / 0.515 / 0.892; 3: 0.344 / 0.471 / 0.903; 4: 0.356 / 0.515 / 0.922; 5: 0.348 / 0.513 / 0.922; 6: 0.352 / 0.507 / 0.883; 7: 0.344 / 0.490 / 0.881; 8: 0.343 / 0.485 / 0.850; 9: 0.350 / 0.529 / 0.867; 10: 0.351 / 0.535 / 0.842; 11: 0.330 / 0.434 / 0.833; 12: 0.347 / 0.487 / 0.833; 13: 0.344 / 0.479 / 0.856; 14: 0.342 / 0.485 / 0.842; 15: 0.359 / 0.513 / 0.844
- 24h: 1: 0.372 / 0.522 / 0.914; 2: 0.357 / 0.488 / 0.906; 3: 0.368 / 0.519 / 0.915; 4: 0.362 / 0.502 / 0.910; 5: 0.365 / 0.514 / 0.917; 6: 0.364 / 0.514 / 0.906; 7: 0.364 / 0.500 / 0.919; 8: 0.362 / 0.511 / 0.908; 9: 0.360 / 0.507 / 0.908; 10: 0.361 / 0.507 / 0.903; 11: 0.351 / 0.482 / 0.905; 12: 0.364 / 0.502 / 0.910; 13: 0.359 / 0.498 / 0.919; 14: 0.357 / 0.490 / 0.912; 15: 0.365 / 0.505 / 0.909
- 7d: 1: 0.356 / 0.524 / 0.900; 2: 0.344 / 0.494 / 0.900; 3: 0.348 / 0.512 / 0.901; 4: 0.344 / 0.498 / 0.901; 5: 0.346 / 0.506 / 0.902; 6: 0.343 / 0.497 / 0.902; 7: 0.343 / 0.500 / 0.903; 8: 0.342 / 0.499 / 0.901; 9: 0.340 / 0.492 / 0.901; 10: 0.343 / 0.504 / 0.902; 11: 0.339 / 0.490 / 0.900; 12: 0.341 / 0.499 / 0.900; 13: 0.342 / 0.499 / 0.900; 14: 0.341 / 0.503 / 0.900; 15: 0.342 / 0.497 / 0.900
- 30d: 1: 0.357 / 0.510 / 0.900; 2: 0.351 / 0.498 / 0.900; 3: 0.354 / 0.511 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.504 / 0.899; 13: 0.347 / 0.502 / 0.899; 14: 0.345 / 0.497 / 0.899; 15: 0.345 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.113 (body 0.062, range 0.164); 'price stays where it was' would score 0.158; colour right 0.483; typical miss of the close 10.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.132 (body 0.088, range 0.176); 'price stays where it was' would score 0.121; colour right 0.496; typical miss of the close 7.1 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.122 (body 0.082, range 0.162); 'price stays where it was' would score 0.120; colour right 0.489; typical miss of the close 9.9 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.120 (body 0.082, range 0.158); 'price stays where it was' would score 0.124; colour right 0.494; typical miss of the close 7.2 bp; chain ended on the right side 0.496 of 671 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.124; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.510 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.198 / 4.4; 3: 0.165 / 6.0; 4: 0.133 / 6.7; 5: 0.119 / 7.4; 6: 0.108 / 7.9; 7: 0.101 / 8.4; 8: 0.094 / 8.7; 9: 0.086 / 8.8; 10: 0.081 / 9.6; 11: 0.076 / 10.3; 12: 0.074 / 10.8; 13: 0.062 / 11.0; 14: 0.063 / 11.2; 15: 0.059 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 103546, probability skill vs chance 0.2277, widened contest next: False
  - now: threshold 0.842, hit rate recent 0.9415 / long run 0.9314
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.321, naive rule 0.528, lift 2.80x
    - 24h: 42 calls (42 a day), hit rate 0.976, chance 0.286, naive rule 0.473, lift 3.41x
    - 7d: 418 calls (60 a day), hit rate 0.926, chance 0.296, naive rule 0.498, lift 3.13x
    - 30d: 1716 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.24x
  - next: threshold 0.5643, hit rate recent 0.557 / long run 0.577
    - 6h: 20 calls (81 a day), hit rate 0.650, chance 0.321, lift 2.02x
    - 24h: 159 calls (160 a day), hit rate 0.541, chance 0.286, lift 1.89x
    - 7d: 666 calls (95 a day), hit rate 0.571, chance 0.296, lift 1.93x
    - 30d: 2481 calls (83 a day), hit rate 0.585, chance 0.290, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.490; 0.35: 539, 0.513; 0.40: 484, 0.561; 0.45: 416, 0.629; 0.50: 363, 0.683; 0.55: 318, 0.725; 0.60: 271, 0.769; 0.65: 224, 0.801; 0.70: 180, 0.833; 0.75: 139, 0.871; 0.80: 96, 0.912; 0.85: 48, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.459; 0.40: 411, 0.488; 0.45: 316, 0.522; 0.50: 205, 0.557; 0.55: 91, 0.583; 0.60: 14, 0.598; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 103544, probability skill vs chance 0.2137, widened contest next: True
  - now: threshold 0.7044, hit rate recent 0.7807 / long run 0.8246
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.153, naive rule 0.329, lift 4.09x
    - 24h: 43 calls (43 a day), hit rate 0.767, chance 0.172, naive rule 0.363, lift 4.45x
    - 7d: 363 calls (52 a day), hit rate 0.807, chance 0.188, naive rule 0.403, lift 4.29x
    - 30d: 1583 calls (53 a day), hit rate 0.831, chance 0.186, naive rule 0.391, lift 4.46x
  - next: threshold 0.44, hit rate recent 0.4382 / long run 0.4729
    - 6h: 13 calls (53 a day), hit rate 0.308, chance 0.153, lift 2.01x
    - 24h: 104 calls (105 a day), hit rate 0.462, chance 0.172, lift 2.68x
    - 7d: 519 calls (74 a day), hit rate 0.470, chance 0.188, lift 2.50x
    - 30d: 2109 calls (70 a day), hit rate 0.483, chance 0.186, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 425, 0.416; 0.35: 357, 0.477; 0.40: 288, 0.548; 0.45: 236, 0.604; 0.50: 184, 0.658; 0.55: 139, 0.705; 0.60: 109, 0.747; 0.65: 83, 0.790; 0.70: 61, 0.823; 0.75: 33, 0.866; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 251, 0.424; 0.40: 162, 0.454; 0.45: 80, 0.473; 0.50: 19, 0.513; 0.55: 2, 0.577
- **K=8**: model 1791936000, labels learned 103541, probability skill vs chance 0.2064, widened contest next: True
  - now: threshold 0.5827, hit rate recent 0.634 / long run 0.6976
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.120, naive rule 0.288, lift 3.57x
    - 24h: 47 calls (47 a day), hit rate 0.617, chance 0.120, naive rule 0.315, lift 5.14x
    - 7d: 393 calls (56 a day), hit rate 0.664, chance 0.123, naive rule 0.342, lift 5.40x
    - 30d: 1590 calls (53 a day), hit rate 0.715, chance 0.122, naive rule 0.329, lift 5.86x
  - next: threshold 0.3721, hit rate recent 0.3716 / long run 0.3966
    - 6h: 15 calls (62 a day), hit rate 0.200, chance 0.120, lift 1.67x
    - 24h: 79 calls (80 a day), hit rate 0.354, chance 0.120, lift 2.96x
    - 7d: 600 calls (86 a day), hit rate 0.390, chance 0.123, lift 3.17x
    - 30d: 2117 calls (71 a day), hit rate 0.410, chance 0.122, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 263, 0.411; 0.35: 199, 0.485; 0.40: 153, 0.546; 0.45: 120, 0.590; 0.50: 92, 0.633; 0.55: 66, 0.686; 0.60: 45, 0.728; 0.65: 24, 0.776; 0.70: 9, 0.833; 0.75: 1, 0.789
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 181, 0.351; 0.35: 110, 0.390; 0.40: 46, 0.423; 0.45: 10, 0.462; 0.50: 1, 0.378
- **K=13**: model 1791849600, labels learned 103536, probability skill vs chance 0.1865, widened contest next: True
  - now: threshold 0.4357, hit rate recent 0.5647 / long run 0.5838
    - 6h: 13 calls (54 a day), hit rate 0.308, chance 0.077, naive rule 0.245, lift 4.01x
    - 24h: 44 calls (44 a day), hit rate 0.591, chance 0.078, naive rule 0.276, lift 7.62x
    - 7d: 352 calls (50 a day), hit rate 0.582, chance 0.079, naive rule 0.286, lift 7.37x
    - 30d: 1487 calls (50 a day), hit rate 0.590, chance 0.078, naive rule 0.272, lift 7.58x
  - next: threshold 0.2997, hit rate recent 0.2616 / long run 0.3105
    - 6h: 16 calls (67 a day), hit rate 0.125, chance 0.077, lift 1.63x
    - 24h: 75 calls (76 a day), hit rate 0.267, chance 0.078, lift 3.44x
    - 7d: 491 calls (70 a day), hit rate 0.320, chance 0.079, lift 4.05x
    - 30d: 2093 calls (70 a day), hit rate 0.315, chance 0.078, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.451; 0.35: 86, 0.513; 0.40: 61, 0.565; 0.45: 42, 0.620; 0.50: 25, 0.650; 0.55: 14, 0.711; 0.60: 4, 0.775; 0.65: 1, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.329; 0.35: 14, 0.362; 0.40: 2, 0.411; 0.45: 0, 0.300

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.769 | -1.02% | 0.883 | 0.450 | 0.251 | 0.483 | -0.050 |
| 6h | 11.218 | 5.06% | 0.883 | 0.469 | 0.251 | 0.448 | 0.543 |
| 24h | 15.465 | 2.37% | 0.898 | 0.488 | 0.250 | 0.501 | 0.555 |
| 7d | 13.030 | 4.39% | 0.900 | 0.499 | 0.251 | 0.494 | 0.657 |
| 30d | 14.010 | 4.04% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.620 | 14.736 | 14.797 | 14.732 | 14.838 | 14.802 | 14.684 | 14.840 | 14.748 | 14.769 |
| 6h | 11.817 | 11.274 | 11.202 | 11.289 | 11.289 | 11.238 | 11.195 | 11.205 | 11.190 | 11.218 |
| 24h | 15.841 | 15.612 | 15.585 | 15.531 | 15.774 | 15.570 | 15.451 | 15.421 | 15.438 | 15.465 |
| 7d | 13.628 | 13.155 | 13.110 | 13.070 | 13.274 | 13.223 | 13.034 | 12.996 | 13.007 | 13.030 |
| 30d | 14.600 | 14.134 | 14.096 | 14.039 | 14.271 | 14.209 | 14.009 | 13.982 | 13.984 | 14.010 |

## Next candle

- candle starting 2026-10-14 01:52 UTC, last close 2508.78
- P(up) 0.4796, return quantiles (bp): {'05': -10.752, '10': -8.243, '25': -4.793, '40': -1.928, '50': -0.328, '60': 1.303, '75': 4.069, '90': 7.639, '95': 10.592}
- changepoint probability 0.0659, regime age 86.9 min
- agent weights: empirical 0.008, ewma 0.101, garch 0.129, har 0.143, bocpd 0.037, hmm 0.100, online_qr 0.228, lgbm 0.253

## Learning log

- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.05, 4.75, 12.9], current probabilities: [0.011, 0.474, 0.516]
- live generator: {'versions': 60, 'latest_effective': '2026-10-14 02:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.547, 'l_abs': 0.754, 'l_hi': 0.756, 'l_lo': 0.711, 'b05': 0.765, 'b25': 0.756, 'b75': 0.733, 'b95': 0.717}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.576, 1.749, 2.149, 2.408, 3.04, 3.037, 3.974, 3.899, 4.551, 5.078, 5.422, 5.22, 6.37, 6.475]}
- calibration offsets (in sigma): {'05': 0.0355, '10': 0.001, '25': -0.0825, '40': -0.006, '50': -0.015, '60': 0.006, '75': 0.0525, '90': 0.019, '95': 0.0045}
