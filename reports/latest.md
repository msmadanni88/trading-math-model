# ETH-USD 60s candle generator - report

- generated: 2026-10-26 21:16 UTC
- last closed candle: 2026-10-26 21:16 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.646 (96) | 0.548 (672) [0.509, 0.588] | 0.525 (2876) [0.506, 0.545] | 0.517 (5178) [0.503, 0.532] | 0.524 (2206) [0.501, 0.548] | 0.447 (85) | 0.500 | flat +0.021 (noise 0.030) |
| colour_clear | 0.534 (802) | 0.550 (5686) [0.543, 0.559] | 0.535 (23445) [0.527, 0.542] | 0.518 (42293) [0.511, 0.524] | 0.546 (18055) [0.541, 0.551] | 0.537 (738) | 0.500 | flat +0.005 (noise 0.009) |
| colour_confident | 0.578 (268) | 0.607 (1411) [0.590, 0.627] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.608 (143) | 0.500 | flat +0.023 (noise 0.024) |
| colour_next | 0.523 (1434) | 0.535 (10043) [0.528, 0.541] | 0.524 (42849) [0.520, 0.529] | 0.513 (77190) [0.509, 0.517] | 0.530 (32841) [0.525, 0.534] | 0.526 (1269) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.506 (20076) | 0.501 (140602) [0.498, 0.503] | 0.501 (599886) [0.499, 0.502] | 0.501 (1080660) [0.500, 0.502] | 0.500 (459774) [0.499, 0.502] | 0.500 (17766) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.589 (107) | 0.628 (406) [0.603, 0.666] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.612 (49) | 0.500 | flat +0.012 (noise 0.048) |
| reversal_k13_next | 0.364 (66) | 0.318 (466) [0.295, 0.338] | 0.304 (2171) [0.292, 0.315] | 0.307 (3684) [0.297, 0.318] | 0.318 (1579) [0.307, 0.329] | 0.294 (51) | 0.077 | flat +0.022 (noise 0.031) |
| reversal_k13_now | 0.600 (55) | 0.552 (357) [0.510, 0.599] | 0.569 (1575) [0.549, 0.590] | 0.574 (2706) [0.558, 0.590] | 0.566 (1234) [0.543, 0.590] | 0.435 (62) | 0.077 | flat +0.009 (noise 0.037) |
| reversal_k3_next | 0.588 (80) | 0.593 (678) [0.563, 0.626] | 0.580 (2811) [0.566, 0.594] | 0.584 (4642) [0.573, 0.595] | 0.580 (2202) [0.566, 0.595] | 0.590 (100) | 0.293 | flat +0.027 (noise 0.026) |
| reversal_k3_now | 0.870 (46) | 0.936 (388) [0.911, 0.958] | 0.935 (1685) [0.926, 0.945] | 0.937 (3069) [0.930, 0.944] | 0.931 (1306) [0.920, 0.942] | 0.982 (56) | 0.293 | flat -0.003 (noise 0.021) |
| reversal_k5_next | 0.496 (137) | 0.470 (924) [0.441, 0.494] | 0.464 (2951) [0.450, 0.478] | 0.476 (4443) [0.464, 0.489] | 0.462 (2453) [0.447, 0.477] | 0.505 (99) | 0.186 | flat +0.012 (noise 0.024) |
| reversal_k5_now | 0.837 (49) | 0.818 (363) [0.807, 0.829] | 0.831 (1563) [0.817, 0.844] | 0.830 (2820) [0.819, 0.841] | 0.820 (1209) [0.806, 0.833] | 0.863 (51) | 0.187 | flat +0.008 (noise 0.029) |
| reversal_k8_next | 0.403 (119) | 0.378 (759) [0.359, 0.396] | 0.382 (2589) [0.370, 0.395] | 0.389 (4306) [0.378, 0.401] | 0.382 (2200) [0.368, 0.396] | 0.340 (97) | 0.120 | flat +0.000 (noise 0.026) |
| reversal_k8_now | 0.729 (48) | 0.665 (337) [0.621, 0.710] | 0.698 (1525) [0.677, 0.718] | 0.702 (2787) [0.686, 0.717] | 0.687 (1200) [0.665, 0.710] | 0.549 (51) | 0.121 | flat -0.016 (noise 0.036) |
| overall | 0.509 (22206) | 0.504 (155589) [0.502, 0.507] | 0.504 (662481) [0.503, 0.506] | 0.503 (1191485) [0.502, 0.504] | 0.504 (508204) [0.502, 0.506] | 0.503 (19687) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07887, 0.1175] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5308, 'levels': [{'threshold': 0.07887, 'calls_per_day': 147.3, 'win_rate': 0.6058}, {'threshold': 0.1175, 'calls_per_day': 37.0, 'win_rate': 0.6346}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 32971, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15306 | 0.336 | 0.523 (15057) | 0.588 (1742) | 0.762 (2531) |
| volatility: normal | 15305 | 0.365 | 0.525 (15237) | 0.608 (1240) | 0.755 (2274) |
| volatility: wild | 15305 | 0.379 | 0.520 (15262) | 0.632 (622) | 0.768 (1947) |
| session: Asia 00-08 | 15360 | 0.358 | 0.529 (15254) | 0.608 (1272) | 0.765 (2214) |
| session: Europe 08-13 | 9600 | 0.355 | 0.525 (9512) | 0.599 (893) | 0.759 (1519) |
| session: US 13-21 | 15360 | 0.368 | 0.519 (15256) | 0.596 (921) | 0.768 (2190) |
| session: late 21-24 | 5596 | 0.351 | 0.513 (5534) | 0.608 (518) | 0.742 (829) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.333 | 0.335 | 0.220 | 0.220 | 0.533 | 0.244 | 0.423 | 0.757 |
| 6h | 360 | 0.377 | 0.364 | 0.296 | 0.332 | 0.513 | 0.257 | 0.496 | 1.191 |
| 24h | 1440 | 0.376 | 0.367 | 0.303 | 0.340 | 0.522 | 0.263 | 0.490 | 1.191 |
| 7d | 10080 | 0.370 | 0.360 | 0.278 | 0.310 | 0.531 | 0.268 | 0.472 | 1.212 |
| 30d | 43200 | 0.361 | 0.354 | 0.277 | 0.306 | 0.525 | 0.258 | 0.464 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.333 / 0.533 / 0.817; 2: 0.325 / 0.500 / 0.900; 3: 0.329 / 0.500 / 0.950; 4: 0.326 / 0.500 / 0.917; 5: 0.315 / 0.500 / 1.000; 6: 0.312 / 0.483 / 0.983; 7: 0.346 / 0.583 / 0.950; 8: 0.313 / 0.500 / 0.933; 9: 0.326 / 0.533 / 0.883; 10: 0.311 / 0.483 / 0.850; 11: 0.311 / 0.450 / 0.900; 12: 0.335 / 0.550 / 0.867; 13: 0.334 / 0.567 / 0.883; 14: 0.305 / 0.500 / 0.850; 15: 0.315 / 0.500 / 0.867
- 6h: 1: 0.377 / 0.513 / 0.892; 2: 0.372 / 0.493 / 0.906; 3: 0.372 / 0.487 / 0.933; 4: 0.376 / 0.513 / 0.939; 5: 0.381 / 0.546 / 0.947; 6: 0.367 / 0.490 / 0.953; 7: 0.377 / 0.513 / 0.922; 8: 0.372 / 0.499 / 0.903; 9: 0.384 / 0.543 / 0.869; 10: 0.355 / 0.448 / 0.853; 11: 0.371 / 0.490 / 0.878; 12: 0.383 / 0.538 / 0.856; 13: 0.365 / 0.474 / 0.869; 14: 0.367 / 0.507 / 0.875; 15: 0.368 / 0.493 / 0.858
- 24h: 1: 0.376 / 0.522 / 0.885; 2: 0.363 / 0.474 / 0.902; 3: 0.368 / 0.513 / 0.906; 4: 0.362 / 0.501 / 0.902; 5: 0.367 / 0.508 / 0.900; 6: 0.359 / 0.492 / 0.901; 7: 0.360 / 0.499 / 0.899; 8: 0.359 / 0.485 / 0.896; 9: 0.369 / 0.524 / 0.894; 10: 0.361 / 0.503 / 0.892; 11: 0.361 / 0.497 / 0.897; 12: 0.364 / 0.515 / 0.892; 13: 0.355 / 0.485 / 0.897; 14: 0.360 / 0.502 / 0.897; 15: 0.356 / 0.494 / 0.895
- 7d: 1: 0.370 / 0.531 / 0.896; 2: 0.358 / 0.501 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.355 / 0.499 / 0.900; 5: 0.355 / 0.503 / 0.900; 6: 0.353 / 0.495 / 0.901; 7: 0.353 / 0.497 / 0.900; 8: 0.354 / 0.508 / 0.900; 9: 0.353 / 0.500 / 0.900; 10: 0.353 / 0.504 / 0.899; 11: 0.351 / 0.499 / 0.899; 12: 0.352 / 0.504 / 0.899; 13: 0.349 / 0.494 / 0.899; 14: 0.350 / 0.495 / 0.900; 15: 0.350 / 0.501 / 0.899
- 30d: 1: 0.361 / 0.525 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.505 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.499 / 0.900; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.142 (body 0.091, range 0.194); 'price stays where it was' would score 0.181; colour right 0.550; typical miss of the close 7.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.117 (body 0.070, range 0.163); 'price stays where it was' would score 0.133; colour right 0.501; typical miss of the close 10.8 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.123 (body 0.077, range 0.170); 'price stays where it was' would score 0.136; colour right 0.498; typical miss of the close 11.6 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.127 (body 0.087, range 0.168); 'price stays where it was' would score 0.134; colour right 0.502; typical miss of the close 8.9 bp; chain ended on the right side 0.530 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.127; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.9; 2: 0.196 / 4.5; 3: 0.168 / 6.0; 4: 0.131 / 6.5; 5: 0.123 / 7.3; 6: 0.111 / 7.7; 7: 0.106 / 8.0; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.087 / 9.1; 11: 0.084 / 9.6; 12: 0.076 / 9.9; 13: 0.067 / 10.2; 14: 0.069 / 10.5; 15: 0.060 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 121990, probability skill vs chance 0.2386, widened contest next: False
  - now: threshold 0.8342, hit rate recent 0.9546 / long run 0.9383
    - 6h: 20 calls (81 a day), hit rate 1.000, chance 0.276, naive rule 0.475, lift 3.62x
    - 24h: 62 calls (62 a day), hit rate 0.968, chance 0.290, naive rule 0.472, lift 3.34x
    - 7d: 400 calls (57 a day), hit rate 0.943, chance 0.298, naive rule 0.503, lift 3.16x
    - 30d: 1698 calls (57 a day), hit rate 0.936, chance 0.294, naive rule 0.492, lift 3.19x
  - next: threshold 0.5305, hit rate recent 0.5913 / long run 0.5903
    - 6h: 30 calls (122 a day), hit rate 0.600, chance 0.276, lift 2.17x
    - 24h: 112 calls (112 a day), hit rate 0.589, chance 0.290, lift 2.03x
    - 7d: 671 calls (96 a day), hit rate 0.605, chance 0.298, lift 2.03x
    - 30d: 2856 calls (95 a day), hit rate 0.582, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.494; 0.35: 538, 0.519; 0.40: 478, 0.575; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 311, 0.741; 0.60: 263, 0.786; 0.65: 221, 0.812; 0.70: 174, 0.844; 0.75: 136, 0.876; 0.80: 91, 0.915; 0.85: 47, 0.951; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.427; 0.35: 502, 0.465; 0.40: 408, 0.499; 0.45: 310, 0.534; 0.50: 201, 0.570; 0.55: 90, 0.575; 0.60: 14, 0.627; 0.65: 1, 0.677
- **K=5**: model 1792540800, labels learned 121988, probability skill vs chance 0.2224, widened contest next: False
  - now: threshold 0.6719, hit rate recent 0.8384 / long run 0.8243
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.194, naive rule 0.397, lift 4.51x
    - 24h: 57 calls (57 a day), hit rate 0.860, chance 0.192, naive rule 0.396, lift 4.48x
    - 7d: 367 calls (52 a day), hit rate 0.823, chance 0.185, naive rule 0.406, lift 4.44x
    - 30d: 1568 calls (52 a day), hit rate 0.830, chance 0.187, naive rule 0.400, lift 4.43x
  - next: threshold 0.4392, hit rate recent 0.4895 / long run 0.4795
    - 6h: 28 calls (114 a day), hit rate 0.429, chance 0.194, lift 2.21x
    - 24h: 119 calls (120 a day), hit rate 0.504, chance 0.192, lift 2.63x
    - 7d: 888 calls (127 a day), hit rate 0.479, chance 0.185, lift 2.58x
    - 30d: 3024 calls (101 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.425; 0.35: 344, 0.492; 0.40: 277, 0.565; 0.45: 224, 0.620; 0.50: 176, 0.670; 0.55: 136, 0.711; 0.60: 105, 0.755; 0.65: 76, 0.791; 0.70: 52, 0.830; 0.75: 30, 0.875; 0.80: 10, 0.903
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.390; 0.35: 253, 0.421; 0.40: 158, 0.453; 0.45: 70, 0.464; 0.50: 15, 0.486; 0.55: 1, 0.513
- **K=8**: model 1792800000, labels learned 121985, probability skill vs chance 0.2002, widened contest next: True
  - now: threshold 0.5562, hit rate recent 0.6121 / long run 0.6743
    - 6h: 16 calls (66 a day), hit rate 0.688, chance 0.114, naive rule 0.311, lift 6.02x
    - 24h: 56 calls (56 a day), hit rate 0.554, chance 0.119, naive rule 0.317, lift 4.66x
    - 7d: 348 calls (50 a day), hit rate 0.658, chance 0.116, naive rule 0.322, lift 5.68x
    - 30d: 1530 calls (51 a day), hit rate 0.690, chance 0.121, naive rule 0.329, lift 5.72x
  - next: threshold 0.3356, hit rate recent 0.348 / long run 0.3765
    - 6h: 29 calls (119 a day), hit rate 0.345, chance 0.114, lift 3.02x
    - 24h: 111 calls (112 a day), hit rate 0.342, chance 0.119, lift 2.88x
    - 7d: 748 calls (107 a day), hit rate 0.378, chance 0.116, lift 3.27x
    - 30d: 2647 calls (88 a day), hit rate 0.380, chance 0.121, lift 3.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 188, 0.496; 0.40: 145, 0.548; 0.45: 111, 0.593; 0.50: 84, 0.635; 0.55: 61, 0.670; 0.60: 40, 0.717; 0.65: 23, 0.790; 0.70: 10, 0.833; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.353; 0.35: 96, 0.380; 0.40: 35, 0.398; 0.45: 7, 0.421; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 121980, probability skill vs chance 0.174, widened contest next: True
  - now: threshold 0.4044, hit rate recent 0.474 / long run 0.5492
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.061, naive rule 0.212, lift 5.48x
    - 24h: 70 calls (71 a day), hit rate 0.457, chance 0.075, naive rule 0.258, lift 6.12x
    - 7d: 375 calls (54 a day), hit rate 0.539, chance 0.073, naive rule 0.263, lift 7.41x
    - 30d: 1596 calls (53 a day), hit rate 0.562, chance 0.077, naive rule 0.272, lift 7.29x
  - next: threshold 0.2945, hit rate recent 0.3091 / long run 0.3121
    - 6h: 12 calls (50 a day), hit rate 0.250, chance 0.061, lift 4.11x
    - 24h: 58 calls (59 a day), hit rate 0.293, chance 0.075, lift 3.92x
    - 7d: 440 calls (63 a day), hit rate 0.314, chance 0.073, lift 4.31x
    - 30d: 2166 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.441; 0.35: 88, 0.492; 0.40: 62, 0.548; 0.45: 41, 0.600; 0.50: 26, 0.657; 0.55: 15, 0.706; 0.60: 7, 0.748; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.316; 0.35: 14, 0.348; 0.40: 2, 0.443; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.912 | -0.43% | 0.800 | 0.350 | 0.249 | 0.533 | 0.239 |
| 6h | 15.863 | 1.27% | 0.903 | 0.478 | 0.251 | 0.474 | 0.515 |
| 24h | 19.183 | 4.92% | 0.896 | 0.493 | 0.251 | 0.500 | 0.616 |
| 7d | 15.246 | 3.59% | 0.899 | 0.500 | 0.250 | 0.501 | 0.663 |
| 30d | 13.673 | 4.14% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 16.840 | 17.197 | 16.947 | 16.836 | 17.018 | 16.984 | 16.981 | 17.107 | 16.974 | 16.912 |
| 6h | 16.068 | 15.860 | 15.862 | 16.084 | 15.900 | 15.877 | 15.898 | 15.843 | 15.842 | 15.863 |
| 24h | 20.176 | 19.347 | 19.341 | 19.241 | 19.463 | 19.399 | 19.169 | 19.144 | 19.140 | 19.183 |
| 7d | 15.813 | 15.389 | 15.325 | 15.267 | 15.509 | 15.398 | 15.233 | 15.206 | 15.214 | 15.246 |
| 30d | 14.263 | 13.806 | 13.758 | 13.698 | 13.917 | 13.854 | 13.668 | 13.649 | 13.647 | 13.673 |

## Next candle

- candle starting 2026-10-26 21:16 UTC, last close 2300.97
- P(up) 0.4889, return quantiles (bp): {'05': -9.883, '10': -7.59, '25': -4.041, '40': -1.695, '50': -0.16, '60': 1.308, '75': 3.531, '90': 6.845, '95': 9.324}
- changepoint probability 0.044, regime age 39.2 min
- agent weights: empirical 0.004, ewma 0.085, garch 0.131, har 0.115, bocpd 0.054, hmm 0.089, online_qr 0.226, lgbm 0.296

## Learning log

- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- HMM volatility states (sd, bp per minute): [3.43, 6.5, 17.71], current probabilities: [0.05, 0.931, 0.019]
- live generator: {'versions': 60, 'latest_effective': '2026-10-26 21:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.346, 'l_abs': 0.731, 'l_hi': 0.814, 'l_lo': 0.801, 'b05': 0.755, 'b25': 0.72, 'b75': 0.699, 'b95': 0.717}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8]], 'cone_width': [1.386, 1.479, 1.854, 2.161, 2.147, 2.517, 2.806, 3.23, 3.771, 3.445, 3.985, 3.836, 3.91, 4.221]}
- calibration offsets (in sigma): {'05': -0.0425, '10': -0.075, '25': -0.1125, '40': -0.08, '50': -0.035, '60': -0.01, '75': 0.0025, '90': -0.015, '95': -0.0275}
