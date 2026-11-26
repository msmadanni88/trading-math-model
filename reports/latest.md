# ETH-USD 60s candle generator - report

- generated: 2026-11-26 20:07 UTC
- last closed candle: 2026-11-26 20:07 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.501 (672) [0.473, 0.531] | 0.510 (2879) [0.495, 0.525] | 0.514 (8153) [0.504, 0.525] | 0.516 (5181) [0.502, 0.529] | 0.525 (80) | 0.500 | flat -0.026 (noise 0.027) |
| colour_clear | 0.556 (787) | 0.551 (5509) [0.540, 0.561] | 0.543 (23788) [0.536, 0.549] | 0.527 (66905) [0.522, 0.532] | 0.544 (42667) [0.540, 0.548] | 0.601 (674) | 0.500 | flat +0.005 (noise 0.009) |
| colour_confident | 0.589 (168) | 0.575 (1312) [0.560, 0.586] | 0.569 (4450) [0.559, 0.579] | 0.584 (8071) [0.575, 0.593] | 0.584 (8071) [0.575, 0.593] | 0.589 (163) | 0.500 | flat +0.021 (noise 0.021) |
| colour_next | 0.535 (1434) | 0.535 (10048) [0.529, 0.542] | 0.531 (42904) [0.527, 0.536] | 0.520 (121526) [0.516, 0.523] | 0.530 (77177) [0.528, 0.534] | 0.571 (1201) | 0.500 | flat +0.002 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.502 (140672) [0.500, 0.504] | 0.502 (600656) [0.501, 0.503] | 0.501 (1701364) [0.500, 0.502] | 0.501 (1080478) [0.500, 0.502] | 0.490 (16814) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.521 (48) | 0.576 (387) [0.526, 0.618] | 0.598 (1172) [0.576, 0.619] | 0.616 (2166) [0.599, 0.631] | 0.616 (2166) [0.599, 0.631] | 0.500 (40) | 0.500 | flat -0.014 (noise 0.039) |
| reversal_k13_next | 0.297 (74) | 0.357 (414) [0.315, 0.413] | 0.339 (1827) [0.321, 0.358] | 0.318 (5570) [0.308, 0.327] | 0.328 (3465) [0.317, 0.340] | 0.282 (39) | 0.078 | flat +0.047 (noise 0.037) |
| reversal_k13_now | 0.711 (45) | 0.611 (360) [0.559, 0.667] | 0.586 (1600) [0.565, 0.608] | 0.576 (4376) [0.564, 0.589] | 0.574 (2904) [0.558, 0.590] | 0.548 (42) | 0.078 | flat +0.041 (noise 0.047) |
| reversal_k3_next | 0.588 (131) | 0.592 (999) [0.565, 0.619] | 0.599 (2729) [0.586, 0.612] | 0.590 (7488) [0.581, 0.597] | 0.591 (5048) [0.581, 0.600] | 0.627 (110) | 0.294 | flat -0.011 (noise 0.029) |
| reversal_k3_now | 0.923 (65) | 0.922 (425) [0.911, 0.935] | 0.929 (1754) [0.921, 0.937] | 0.935 (4880) [0.929, 0.940] | 0.931 (3117) [0.924, 0.937] | 0.949 (39) | 0.294 | flat -0.021 (noise 0.018) |
| reversal_k5_next | 0.446 (56) | 0.510 (359) [0.459, 0.575] | 0.510 (1708) [0.488, 0.532] | 0.486 (6261) [0.475, 0.497] | 0.483 (4271) [0.469, 0.497] | 0.517 (58) | 0.187 | flat +0.029 (noise 0.047) |
| reversal_k5_now | 0.784 (74) | 0.816 (440) [0.797, 0.834] | 0.794 (1804) [0.778, 0.809] | 0.816 (4678) [0.807, 0.826] | 0.805 (3067) [0.794, 0.815] | 0.882 (51) | 0.188 | flat +0.054 (noise 0.028) |
| reversal_k8_next | 0.301 (83) | 0.419 (563) [0.371, 0.470] | 0.420 (2207) [0.402, 0.438] | 0.399 (6623) [0.388, 0.408] | 0.400 (4517) [0.387, 0.411] | 0.462 (65) | 0.121 | flat +0.018 (noise 0.038) |
| reversal_k8_now | 0.714 (56) | 0.689 (421) [0.660, 0.718] | 0.687 (1667) [0.669, 0.704] | 0.695 (4509) [0.683, 0.706] | 0.684 (2922) [0.670, 0.699] | 0.674 (46) | 0.122 | flat +0.040 (noise 0.033) |
| overall | 0.507 (22190) | 0.507 (155373) [0.505, 0.509] | 0.506 (661735) [0.505, 0.507] | 0.504 (1875428) [0.504, 0.505] | 0.505 (1192147) [0.504, 0.506] | 0.499 (18545) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08269, 0.1194] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.54, 'levels': [{'threshold': 0.08269, 'calls_per_day': 147.8, 'win_rate': 0.5829}, {'threshold': 0.1194, 'calls_per_day': 37.2, 'win_rate': 0.567}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42906, 'rate': 0.5323}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15283 | 0.354 | 0.537 (15066) | 0.564 (1990) | 0.750 (2601) |
| volatility: normal | 15282 | 0.380 | 0.526 (15224) | 0.565 (1564) | 0.748 (2464) |
| volatility: wild | 15282 | 0.392 | 0.533 (15247) | 0.590 (1219) | 0.759 (2174) |
| session: Asia 00-08 | 15360 | 0.375 | 0.534 (15250) | 0.562 (1655) | 0.750 (2325) |
| session: Europe 08-13 | 9600 | 0.369 | 0.531 (9523) | 0.579 (1161) | 0.766 (1533) |
| session: US 13-21 | 15307 | 0.382 | 0.535 (15216) | 0.594 (1373) | 0.742 (2518) |
| session: late 21-24 | 5580 | 0.369 | 0.521 (5548) | 0.526 (584) | 0.759 (863) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.419 | 0.372 | 0.284 | 0.284 | 0.633 | 0.343 | 0.495 | 1.247 |
| 6h | 360 | 0.387 | 0.369 | 0.297 | 0.313 | 0.546 | 0.280 | 0.495 | 1.256 |
| 24h | 1440 | 0.392 | 0.374 | 0.289 | 0.319 | 0.568 | 0.287 | 0.497 | 1.205 |
| 7d | 10080 | 0.388 | 0.379 | 0.295 | 0.328 | 0.541 | 0.271 | 0.504 | 1.219 |
| 30d | 43200 | 0.375 | 0.369 | 0.288 | 0.320 | 0.532 | 0.267 | 0.484 | 1.272 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.419 / 0.633 / 0.950; 2: 0.374 / 0.517 / 0.967; 3: 0.364 / 0.450 / 1.000; 4: 0.371 / 0.533 / 1.000; 5: 0.367 / 0.450 / 1.000; 6: 0.349 / 0.467 / 0.983; 7: 0.370 / 0.433 / 0.983; 8: 0.374 / 0.533 / 0.950; 9: 0.384 / 0.517 / 1.000; 10: 0.358 / 0.517 / 0.983; 11: 0.379 / 0.483 / 1.000; 12: 0.376 / 0.467 / 1.000; 13: 0.388 / 0.517 / 1.000; 14: 0.360 / 0.483 / 0.983; 15: 0.381 / 0.517 / 1.000
- 6h: 1: 0.387 / 0.546 / 0.886; 2: 0.362 / 0.462 / 0.881; 3: 0.368 / 0.496 / 0.978; 4: 0.359 / 0.490 / 0.944; 5: 0.369 / 0.513 / 0.969; 6: 0.358 / 0.490 / 0.928; 7: 0.358 / 0.460 / 0.942; 8: 0.362 / 0.510 / 0.864; 9: 0.361 / 0.490 / 0.942; 10: 0.358 / 0.493 / 0.875; 11: 0.362 / 0.501 / 0.967; 12: 0.358 / 0.490 / 0.944; 13: 0.359 / 0.507 / 0.928; 14: 0.358 / 0.510 / 0.886; 15: 0.361 / 0.532 / 0.908
- 24h: 1: 0.392 / 0.568 / 0.906; 2: 0.360 / 0.464 / 0.891; 3: 0.368 / 0.496 / 0.901; 4: 0.366 / 0.498 / 0.923; 5: 0.364 / 0.497 / 0.902; 6: 0.363 / 0.489 / 0.897; 7: 0.367 / 0.505 / 0.920; 8: 0.363 / 0.502 / 0.938; 9: 0.362 / 0.493 / 0.895; 10: 0.358 / 0.485 / 0.930; 11: 0.359 / 0.490 / 0.899; 12: 0.362 / 0.494 / 0.893; 13: 0.357 / 0.486 / 0.890; 14: 0.359 / 0.494 / 0.933; 15: 0.357 / 0.504 / 0.932
- 7d: 1: 0.388 / 0.541 / 0.900; 2: 0.370 / 0.490 / 0.904; 3: 0.372 / 0.506 / 0.900; 4: 0.369 / 0.497 / 0.903; 5: 0.372 / 0.505 / 0.903; 6: 0.368 / 0.495 / 0.902; 7: 0.369 / 0.503 / 0.906; 8: 0.368 / 0.506 / 0.904; 9: 0.367 / 0.496 / 0.905; 10: 0.369 / 0.512 / 0.906; 11: 0.367 / 0.504 / 0.907; 12: 0.368 / 0.503 / 0.902; 13: 0.363 / 0.491 / 0.901; 14: 0.364 / 0.496 / 0.903; 15: 0.365 / 0.503 / 0.903
- 30d: 1: 0.375 / 0.532 / 0.898; 2: 0.361 / 0.490 / 0.900; 3: 0.365 / 0.511 / 0.900; 4: 0.361 / 0.497 / 0.901; 5: 0.363 / 0.505 / 0.900; 6: 0.360 / 0.500 / 0.900; 7: 0.361 / 0.502 / 0.900; 8: 0.361 / 0.507 / 0.900; 9: 0.359 / 0.500 / 0.900; 10: 0.360 / 0.504 / 0.900; 11: 0.360 / 0.505 / 0.900; 12: 0.359 / 0.503 / 0.900; 13: 0.358 / 0.499 / 0.900; 14: 0.358 / 0.502 / 0.900; 15: 0.358 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.103 (body 0.072, range 0.134); 'price stays where it was' would score 0.134; colour right 0.417; typical miss of the close 14.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.144 (body 0.097, range 0.192); 'price stays where it was' would score 0.164; colour right 0.474; typical miss of the close 11.0 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.149 (body 0.101, range 0.197); 'price stays where it was' would score 0.161; colour right 0.478; typical miss of the close 9.6 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.135 (body 0.087, range 0.183); 'price stays where it was' would score 0.144; colour right 0.498; typical miss of the close 13.8 bp; chain ended on the right side 0.501 of 672 chains; n=10080
- 30d: match 0.128 (body 0.085, range 0.170); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 11.0 bp; chain ended on the right side 0.510 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.373 / 5.9; 2: 0.206 / 6.7; 3: 0.167 / 8.7; 4: 0.137 / 9.0; 5: 0.125 / 9.9; 6: 0.119 / 10.7; 7: 0.117 / 11.1; 8: 0.103 / 12.2; 9: 0.093 / 12.9; 10: 0.089 / 13.1; 11: 0.087 / 13.7; 12: 0.082 / 13.9; 13: 0.077 / 14.8; 14: 0.071 / 15.1; 15: 0.068 / 15.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 166561, probability skill vs chance 0.2349, widened contest next: False
  - now: threshold 0.8302, hit rate recent 0.9231 / long run 0.9295
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.324, naive rule 0.569, lift 2.85x
    - 24h: 52 calls (52 a day), hit rate 0.923, chance 0.313, naive rule 0.541, lift 2.95x
    - 7d: 404 calls (58 a day), hit rate 0.928, chance 0.303, naive rule 0.526, lift 3.06x
    - 30d: 1734 calls (58 a day), hit rate 0.928, chance 0.295, naive rule 0.505, lift 3.15x
  - next: threshold 0.5353, hit rate recent 0.657 / long run 0.6
    - 6h: 24 calls (97 a day), hit rate 0.708, chance 0.324, lift 2.19x
    - 24h: 130 calls (130 a day), hit rate 0.638, chance 0.313, lift 2.04x
    - 7d: 1047 calls (150 a day), hit rate 0.600, chance 0.303, lift 1.98x
    - 30d: 2740 calls (91 a day), hit rate 0.601, chance 0.295, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.504; 0.35: 530, 0.529; 0.40: 482, 0.572; 0.45: 420, 0.634; 0.50: 369, 0.681; 0.55: 321, 0.726; 0.60: 272, 0.771; 0.65: 227, 0.802; 0.70: 178, 0.833; 0.75: 143, 0.869; 0.80: 95, 0.900; 0.85: 42, 0.941; 0.90: 3, 0.957
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.435; 0.35: 487, 0.470; 0.40: 383, 0.511; 0.45: 290, 0.543; 0.50: 187, 0.573; 0.55: 78, 0.592; 0.60: 10, 0.638; 0.65: 0, 0.500
- **K=5**: model 1794528000, labels learned 166559, probability skill vs chance 0.2233, widened contest next: False
  - now: threshold 0.704, hit rate recent 0.8473 / long run 0.8041
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.198, naive rule 0.477, lift 4.10x
    - 24h: 62 calls (62 a day), hit rate 0.887, chance 0.195, naive rule 0.439, lift 4.54x
    - 7d: 430 calls (61 a day), hit rate 0.821, chance 0.196, naive rule 0.443, lift 4.20x
    - 30d: 1801 calls (60 a day), hit rate 0.795, chance 0.189, naive rule 0.417, lift 4.22x
  - next: threshold 0.4528, hit rate recent 0.5065 / long run 0.4999
    - 6h: 14 calls (57 a day), hit rate 0.500, chance 0.198, lift 2.52x
    - 24h: 67 calls (67 a day), hit rate 0.522, chance 0.195, lift 2.67x
    - 7d: 372 calls (53 a day), hit rate 0.524, chance 0.196, lift 2.68x
    - 30d: 1717 calls (57 a day), hit rate 0.510, chance 0.189, lift 2.70x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.427; 0.35: 364, 0.475; 0.40: 295, 0.542; 0.45: 238, 0.602; 0.50: 186, 0.654; 0.55: 149, 0.685; 0.60: 116, 0.730; 0.65: 85, 0.766; 0.70: 54, 0.803; 0.75: 27, 0.837; 0.80: 6, 0.841
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 330, 0.396; 0.35: 246, 0.434; 0.40: 156, 0.461; 0.45: 63, 0.508; 0.50: 9, 0.569; 0.55: 0, 0.562
- **K=8**: model 1794960000, labels learned 166556, probability skill vs chance 0.2137, widened contest next: False
  - now: threshold 0.5868, hit rate recent 0.6881 / long run 0.6814
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.107, naive rule 0.366, lift 6.67x
    - 24h: 52 calls (52 a day), hit rate 0.654, chance 0.116, naive rule 0.357, lift 5.62x
    - 7d: 402 calls (57 a day), hit rate 0.689, chance 0.126, naive rule 0.374, lift 5.46x
    - 30d: 1662 calls (55 a day), hit rate 0.685, chance 0.124, naive rule 0.351, lift 5.54x
  - next: threshold 0.3783, hit rate recent 0.4441 / long run 0.4166
    - 6h: 17 calls (70 a day), hit rate 0.765, chance 0.107, lift 7.14x
    - 24h: 84 calls (85 a day), hit rate 0.417, chance 0.116, lift 3.58x
    - 7d: 552 calls (79 a day), hit rate 0.428, chance 0.126, lift 3.38x
    - 30d: 2188 calls (73 a day), hit rate 0.422, chance 0.124, lift 3.42x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.426; 0.35: 204, 0.486; 0.40: 160, 0.537; 0.45: 121, 0.581; 0.50: 87, 0.635; 0.55: 64, 0.674; 0.60: 43, 0.714; 0.65: 25, 0.770; 0.70: 9, 0.805; 0.75: 1, 0.730
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.377; 0.35: 84, 0.411; 0.40: 30, 0.443; 0.45: 7, 0.486; 0.50: 1, 0.676
- **K=13**: model 1795478400, labels learned 166551, probability skill vs chance 0.1988, widened contest next: True
  - now: threshold 0.4551, hit rate recent 0.6098 / long run 0.5892
    - 6h: 16 calls (67 a day), hit rate 0.500, chance 0.078, naive rule 0.346, lift 6.39x
    - 24h: 48 calls (49 a day), hit rate 0.562, chance 0.080, naive rule 0.327, lift 7.03x
    - 7d: 341 calls (49 a day), hit rate 0.619, chance 0.084, naive rule 0.335, lift 7.34x
    - 30d: 1594 calls (53 a day), hit rate 0.583, chance 0.081, naive rule 0.302, lift 7.24x
  - next: threshold 0.3032, hit rate recent 0.3031 / long run 0.3364
    - 6h: 10 calls (42 a day), hit rate 0.300, chance 0.078, lift 3.83x
    - 24h: 52 calls (53 a day), hit rate 0.250, chance 0.080, lift 3.12x
    - 7d: 376 calls (54 a day), hit rate 0.367, chance 0.084, lift 4.35x
    - 30d: 1825 calls (61 a day), hit rate 0.335, chance 0.081, lift 4.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 143, 0.427; 0.35: 105, 0.475; 0.40: 72, 0.539; 0.45: 51, 0.588; 0.50: 35, 0.623; 0.55: 22, 0.647; 0.60: 10, 0.667; 0.65: 2, 0.516
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.340; 0.35: 15, 0.381; 0.40: 2, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.665 | 4.92% | 0.950 | 0.533 | 0.250 | 0.500 | 0.028 |
| 6h | 18.765 | 2.47% | 0.900 | 0.497 | 0.251 | 0.496 | 0.593 |
| 24h | 17.158 | 5.36% | 0.909 | 0.508 | 0.250 | 0.521 | 0.535 |
| 7d | 25.102 | 4.61% | 0.901 | 0.501 | 0.250 | 0.513 | 0.660 |
| 30d | 20.142 | 4.87% | 0.900 | 0.500 | 0.250 | 0.507 | 0.705 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.216 | 10.776 | 10.817 | 10.785 | 11.038 | 10.954 | 10.625 | 10.731 | 10.721 | 10.665 |
| 6h | 19.240 | 19.088 | 18.900 | 18.725 | 19.233 | 18.853 | 18.757 | 18.666 | 18.722 | 18.765 |
| 24h | 18.130 | 17.375 | 17.305 | 17.214 | 17.672 | 17.341 | 17.106 | 17.085 | 17.118 | 17.158 |
| 7d | 26.316 | 25.384 | 25.288 | 25.124 | 25.724 | 25.483 | 25.092 | 25.034 | 25.063 | 25.102 |
| 30d | 21.174 | 20.335 | 20.286 | 20.197 | 20.577 | 20.488 | 20.123 | 20.097 | 20.109 | 20.142 |

## Next candle

- candle starting 2026-11-26 20:07 UTC, last close 1702.51
- P(up) 0.5074, return quantiles (bp): {'05': -6.953, '10': -5.116, '25': -2.634, '40': -1.179, '50': 0.093, '60': 1.194, '75': 2.866, '90': 5.37, '95': 7.259}
- changepoint probability 0.034, regime age 62.5 min
- agent weights: empirical 0.005, ewma 0.069, garch 0.099, har 0.183, bocpd 0.016, hmm 0.067, online_qr 0.256, lgbm 0.305

## Learning log

- 2026-11-24 12:00 UTC: {"garch": {"alpha": 0.0937, "beta": 0.8962}, "hmm": {"sd_bp": [5.06, 10.1, 31.41], "stay": [0.968, 0.948, 0.887]}}
- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- 2026-11-25 12:00 UTC: {"garch": {"alpha": 0.091, "beta": 0.8903}, "hmm": {"sd_bp": [4.89, 9.77, 34.58], "stay": [0.96, 0.954, 0.849]}}
- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- 2026-11-26 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.8951}, "hmm": {"sd_bp": [5.1, 9.79, 29.67], "stay": [0.964, 0.952, 0.897]}}
- HMM volatility states (sd, bp per minute): [5.1, 9.79, 29.67], current probabilities: [0.933, 0.065, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-11-26 20:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.448, 'l_abs': 0.676, 'l_hi': 0.763, 'l_lo': 0.713, 'b05': 0.696, 'b25': 0.671, 'b75': 0.637, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.4, 1.6], [1.4, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.6], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [1.499, 1.506, 1.485, 1.952, 2.058, 2.098, 2.915, 2.693, 3.272, 3.238, 3.671, 3.606, 3.675, 3.314]}
- calibration offsets (in sigma): {'05': 0.103, '10': 0.086, '25': 0.045, '40': 0.004, '50': 0.04, '60': 0.046, '75': 0.015, '90': -0.036, '95': -0.033}
