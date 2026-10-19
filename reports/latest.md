# ETH-USD 60s candle generator - report

- generated: 2026-10-19 19:51 UTC
- last closed candle: 2026-10-19 19:51 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.527 (672) [0.495, 0.561] | 0.522 (2875) [0.504, 0.542] | 0.512 (4506) [0.497, 0.527] | 0.514 (1534) [0.486, 0.543] | 0.557 (79) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.555 (785) | 0.545 (5567) [0.537, 0.555] | 0.522 (23331) [0.514, 0.530] | 0.513 (36607) [0.506, 0.519] | 0.544 (12369) [0.539, 0.550] | 0.568 (673) | 0.500 | flat +0.004 (noise 0.009) |
| colour_confident | 0.568 (139) | 0.584 (630) [0.568, 0.603] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.708 (113) | 0.500 | flat -0.018 (noise 0.025) |
| colour_next | 0.520 (1430) | 0.526 (10017) [0.519, 0.534] | 0.515 (42854) [0.509, 0.520] | 0.510 (67147) [0.505, 0.514] | 0.528 (22798) [0.523, 0.533] | 0.559 (1187) | 0.500 | flat -0.001 (noise 0.007) |
| colour_path | 0.504 (20020) | 0.502 (140238) [0.499, 0.505] | 0.501 (599956) [0.500, 0.503] | 0.501 (940058) [0.500, 0.502] | 0.500 (319172) [0.498, 0.503] | 0.501 (16618) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.583 (36) | 0.616 (138) [0.574, 0.680] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.655 (29) | 0.500 | flat -0.044 (noise 0.050) |
| reversal_k13_next | 0.309 (81) | 0.296 (433) [0.281, 0.310] | 0.312 (2060) [0.298, 0.327] | 0.306 (3218) [0.294, 0.318] | 0.318 (1113) [0.305, 0.330] | 0.294 (68) | 0.077 | flat -0.034 (noise 0.030) |
| reversal_k13_now | 0.469 (64) | 0.543 (381) [0.510, 0.582] | 0.584 (1534) [0.564, 0.605] | 0.577 (2349) [0.561, 0.595] | 0.571 (877) [0.548, 0.599] | 0.488 (41) | 0.077 | flat -0.029 (noise 0.036) |
| reversal_k3_next | 0.584 (101) | 0.566 (737) [0.555, 0.578] | 0.578 (2604) [0.565, 0.592] | 0.582 (3964) [0.572, 0.594] | 0.574 (1524) [0.560, 0.590] | 0.510 (98) | 0.293 | flat -0.026 (noise 0.028) |
| reversal_k3_now | 0.946 (55) | 0.938 (373) [0.913, 0.964] | 0.938 (1718) [0.929, 0.947] | 0.937 (2681) [0.931, 0.945] | 0.929 (918) [0.918, 0.941] | 0.925 (40) | 0.293 | flat +0.016 (noise 0.018) |
| reversal_k5_next | 0.434 (152) | 0.458 (799) [0.439, 0.484] | 0.472 (2424) [0.457, 0.489] | 0.478 (3519) [0.464, 0.492] | 0.457 (1529) [0.440, 0.477] | 0.435 (124) | 0.187 | flat -0.012 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.810 (348) [0.784, 0.838] | 0.832 (1608) [0.816, 0.847] | 0.832 (2457) [0.819, 0.844] | 0.820 (846) [0.800, 0.840] | 0.833 (42) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k8_next | 0.393 (117) | 0.378 (667) [0.348, 0.403] | 0.400 (2238) [0.381, 0.419] | 0.391 (3547) [0.379, 0.405] | 0.385 (1441) [0.365, 0.404] | 0.340 (97) | 0.121 | flat -0.003 (noise 0.027) |
| reversal_k8_now | 0.651 (43) | 0.681 (335) [0.657, 0.706] | 0.719 (1571) [0.698, 0.739] | 0.707 (2450) [0.691, 0.723] | 0.695 (863) [0.670, 0.721] | 0.571 (35) | 0.122 | flat -0.004 (noise 0.034) |
| overall | 0.506 (22206) | 0.505 (155000) [0.502, 0.507] | 0.504 (661442) [0.503, 0.505] | 0.503 (1035896) [0.502, 0.504] | 0.504 (352615) [0.502, 0.506] | 0.505 (18429) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06498, 0.09758] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.529, 'levels': [{'threshold': 0.06498, 'calls_per_day': 144.0, 'win_rate': 0.572}, {'threshold': 0.09758, 'calls_per_day': 35.8, 'win_rate': 0.623}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 22847, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15277 | 0.336 | 0.523 (15029) | 0.592 (1435) | 0.770 (2505) |
| volatility: normal | 15277 | 0.363 | 0.517 (15210) | 0.623 (512) | 0.765 (2235) |
| volatility: wild | 15277 | 0.378 | 0.509 (15234) | 0.648 (216) | 0.773 (2071) |
| session: Asia 00-08 | 15360 | 0.357 | 0.521 (15256) | 0.612 (804) | 0.770 (2288) |
| session: Europe 08-13 | 9600 | 0.353 | 0.516 (9514) | 0.586 (555) | 0.773 (1496) |
| session: US 13-21 | 15291 | 0.368 | 0.512 (15187) | 0.590 (517) | 0.772 (2223) |
| session: late 21-24 | 5580 | 0.350 | 0.515 (5516) | 0.652 (287) | 0.752 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.373 | 0.371 | 0.341 | 0.341 | 0.550 | 0.255 | 0.492 | 1.173 |
| 6h | 360 | 0.382 | 0.389 | 0.286 | 0.334 | 0.528 | 0.267 | 0.496 | 1.179 |
| 24h | 1440 | 0.379 | 0.370 | 0.280 | 0.312 | 0.556 | 0.275 | 0.484 | 1.208 |
| 7d | 10080 | 0.369 | 0.359 | 0.280 | 0.311 | 0.529 | 0.264 | 0.473 | 1.220 |
| 30d | 43200 | 0.359 | 0.355 | 0.279 | 0.308 | 0.517 | 0.253 | 0.465 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.373 / 0.550 / 0.883; 2: 0.365 / 0.517 / 0.967; 3: 0.364 / 0.517 / 0.983; 4: 0.344 / 0.450 / 0.983; 5: 0.326 / 0.350 / 0.983; 6: 0.375 / 0.517 / 0.983; 7: 0.351 / 0.517 / 1.000; 8: 0.387 / 0.600 / 1.000; 9: 0.342 / 0.433 / 1.000; 10: 0.398 / 0.650 / 1.000; 11: 0.386 / 0.567 / 1.000; 12: 0.378 / 0.567 / 1.000; 13: 0.372 / 0.550 / 1.000; 14: 0.343 / 0.433 / 1.000; 15: 0.362 / 0.483 / 1.000
- 6h: 1: 0.382 / 0.528 / 0.922; 2: 0.373 / 0.500 / 0.961; 3: 0.372 / 0.489 / 0.958; 4: 0.375 / 0.500 / 0.953; 5: 0.357 / 0.461 / 0.964; 6: 0.367 / 0.475 / 0.961; 7: 0.359 / 0.483 / 0.972; 8: 0.376 / 0.522 / 0.969; 9: 0.361 / 0.442 / 0.972; 10: 0.373 / 0.517 / 0.964; 11: 0.363 / 0.489 / 0.969; 12: 0.372 / 0.511 / 0.961; 13: 0.367 / 0.469 / 0.969; 14: 0.382 / 0.531 / 0.967; 15: 0.351 / 0.433 / 0.961
- 24h: 1: 0.379 / 0.556 / 0.909; 2: 0.362 / 0.483 / 0.906; 3: 0.365 / 0.507 / 0.912; 4: 0.355 / 0.477 / 0.915; 5: 0.359 / 0.497 / 0.913; 6: 0.362 / 0.509 / 0.908; 7: 0.354 / 0.483 / 0.912; 8: 0.361 / 0.502 / 0.907; 9: 0.359 / 0.510 / 0.903; 10: 0.362 / 0.518 / 0.911; 11: 0.360 / 0.516 / 0.910; 12: 0.361 / 0.521 / 0.910; 13: 0.358 / 0.500 / 0.912; 14: 0.363 / 0.524 / 0.903; 15: 0.355 / 0.494 / 0.912
- 7d: 1: 0.369 / 0.529 / 0.901; 2: 0.354 / 0.491 / 0.900; 3: 0.360 / 0.506 / 0.900; 4: 0.355 / 0.499 / 0.900; 5: 0.355 / 0.501 / 0.900; 6: 0.356 / 0.506 / 0.899; 7: 0.354 / 0.500 / 0.900; 8: 0.354 / 0.500 / 0.899; 9: 0.354 / 0.502 / 0.899; 10: 0.356 / 0.508 / 0.900; 11: 0.350 / 0.495 / 0.900; 12: 0.354 / 0.506 / 0.900; 13: 0.353 / 0.504 / 0.900; 14: 0.352 / 0.504 / 0.898; 15: 0.353 / 0.505 / 0.900
- 30d: 1: 0.359 / 0.517 / 0.899; 2: 0.350 / 0.495 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.349 / 0.497 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.502 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.348 / 0.504 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.346 / 0.499 / 0.899; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.177 (body 0.101, range 0.253); 'price stays where it was' would score 0.122; colour right 0.483; typical miss of the close 6.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.128 (body 0.081, range 0.175); 'price stays where it was' would score 0.128; colour right 0.489; typical miss of the close 13.4 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.132 (body 0.087, range 0.177); 'price stays where it was' would score 0.138; colour right 0.495; typical miss of the close 9.6 bp; chain ended on the right side 0.615 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.131; colour right 0.497; typical miss of the close 9.4 bp; chain ended on the right side 0.525 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.523 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.196 / 4.5; 3: 0.163 / 6.0; 4: 0.132 / 6.6; 5: 0.121 / 7.2; 6: 0.110 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.076 / 10.2; 13: 0.065 / 10.5; 14: 0.066 / 10.7; 15: 0.058 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 111825, probability skill vs chance 0.2163, widened contest next: True
  - now: threshold 0.8348, hit rate recent 0.9223 / long run 0.9323
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.296, naive rule 0.464, lift 2.82x
    - 24h: 44 calls (44 a day), hit rate 0.932, chance 0.282, naive rule 0.464, lift 3.30x
    - 7d: 363 calls (52 a day), hit rate 0.937, chance 0.289, naive rule 0.480, lift 3.25x
    - 30d: 1700 calls (57 a day), hit rate 0.936, chance 0.292, naive rule 0.483, lift 3.21x
  - next: threshold 0.5332, hit rate recent 0.5038 / long run 0.5635
    - 6h: 22 calls (89 a day), hit rate 0.455, chance 0.296, lift 1.54x
    - 24h: 118 calls (118 a day), hit rate 0.517, chance 0.282, lift 1.83x
    - 7d: 783 calls (112 a day), hit rate 0.559, chance 0.289, lift 1.94x
    - 30d: 2616 calls (87 a day), hit rate 0.575, chance 0.292, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.514; 0.40: 482, 0.566; 0.45: 413, 0.636; 0.50: 360, 0.688; 0.55: 315, 0.730; 0.60: 269, 0.773; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 138, 0.871; 0.80: 94, 0.912; 0.85: 48, 0.952; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.424; 0.35: 499, 0.459; 0.40: 407, 0.490; 0.45: 312, 0.523; 0.50: 202, 0.554; 0.55: 92, 0.573; 0.60: 14, 0.607; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 111823, probability skill vs chance 0.2093, widened contest next: False
  - now: threshold 0.6827, hit rate recent 0.8129 / long run 0.8243
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.167, naive rule 0.356, lift 4.79x
    - 24h: 46 calls (46 a day), hit rate 0.826, chance 0.175, naive rule 0.374, lift 4.73x
    - 7d: 347 calls (50 a day), hit rate 0.807, chance 0.185, naive rule 0.395, lift 4.37x
    - 30d: 1601 calls (53 a day), hit rate 0.829, chance 0.187, naive rule 0.393, lift 4.44x
  - next: threshold 0.4038, hit rate recent 0.435 / long run 0.452
    - 6h: 35 calls (143 a day), hit rate 0.429, chance 0.167, lift 2.56x
    - 24h: 147 calls (148 a day), hit rate 0.442, chance 0.175, lift 2.53x
    - 7d: 849 calls (121 a day), hit rate 0.455, chance 0.185, lift 2.46x
    - 30d: 2465 calls (82 a day), hit rate 0.469, chance 0.187, lift 2.51x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.421; 0.35: 349, 0.486; 0.40: 280, 0.557; 0.45: 228, 0.614; 0.50: 180, 0.662; 0.55: 137, 0.708; 0.60: 107, 0.748; 0.65: 80, 0.789; 0.70: 58, 0.823; 0.75: 32, 0.867; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.419; 0.40: 159, 0.445; 0.45: 74, 0.459; 0.50: 18, 0.496; 0.55: 2, 0.549
- **K=8**: model 1791936000, labels learned 111820, probability skill vs chance 0.1843, widened contest next: True
  - now: threshold 0.5696, hit rate recent 0.6257 / long run 0.6902
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.103, naive rule 0.259, lift 5.83x
    - 24h: 39 calls (39 a day), hit rate 0.590, chance 0.114, naive rule 0.307, lift 5.17x
    - 7d: 324 calls (46 a day), hit rate 0.664, chance 0.119, naive rule 0.321, lift 5.60x
    - 30d: 1560 calls (52 a day), hit rate 0.713, chance 0.122, naive rule 0.329, lift 5.85x
  - next: threshold 0.3418, hit rate recent 0.316 / long run 0.3734
    - 6h: 24 calls (99 a day), hit rate 0.208, chance 0.103, lift 2.03x
    - 24h: 121 calls (122 a day), hit rate 0.347, chance 0.114, lift 3.05x
    - 7d: 700 calls (100 a day), hit rate 0.369, chance 0.119, lift 3.11x
    - 30d: 2279 calls (76 a day), hit rate 0.394, chance 0.122, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.420; 0.35: 194, 0.491; 0.40: 148, 0.549; 0.45: 116, 0.591; 0.50: 89, 0.632; 0.55: 65, 0.681; 0.60: 43, 0.728; 0.65: 24, 0.788; 0.70: 9, 0.838; 0.75: 1, 0.786
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.352; 0.35: 104, 0.383; 0.40: 41, 0.410; 0.45: 9, 0.440; 0.50: 1, 0.471
- **K=13**: model 1792022400, labels learned 111815, probability skill vs chance 0.1767, widened contest next: True
  - now: threshold 0.413, hit rate recent 0.4865 / long run 0.5597
    - 6h: 12 calls (50 a day), hit rate 0.500, chance 0.078, naive rule 0.279, lift 6.39x
    - 24h: 47 calls (47 a day), hit rate 0.511, chance 0.078, naive rule 0.273, lift 6.56x
    - 7d: 379 calls (54 a day), hit rate 0.533, chance 0.076, naive rule 0.272, lift 7.00x
    - 30d: 1544 calls (51 a day), hit rate 0.580, chance 0.078, naive rule 0.273, lift 7.44x
  - next: threshold 0.2768, hit rate recent 0.2806 / long run 0.3077
    - 6h: 15 calls (63 a day), hit rate 0.267, chance 0.078, lift 3.41x
    - 24h: 83 calls (84 a day), hit rate 0.289, chance 0.078, lift 3.71x
    - 7d: 444 calls (64 a day), hit rate 0.297, chance 0.076, lift 3.90x
    - 30d: 2089 calls (70 a day), hit rate 0.308, chance 0.078, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.509; 0.40: 61, 0.559; 0.45: 41, 0.616; 0.50: 25, 0.659; 0.55: 14, 0.712; 0.60: 5, 0.752; 0.65: 1, 0.821
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.321; 0.35: 13, 0.354; 0.40: 2, 0.413; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.104 | 0.90% | 0.900 | 0.550 | 0.251 | 0.500 | 0.130 |
| 6h | 21.123 | 3.81% | 0.917 | 0.506 | 0.250 | 0.531 | 0.552 |
| 24h | 16.503 | 2.54% | 0.908 | 0.502 | 0.250 | 0.506 | 0.582 |
| 7d | 16.384 | 4.24% | 0.901 | 0.500 | 0.251 | 0.494 | 0.643 |
| 30d | 13.802 | 4.03% | 0.900 | 0.500 | 0.251 | 0.496 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.224 | 13.195 | 13.239 | 13.181 | 13.449 | 13.281 | 13.034 | 13.107 | 13.081 | 13.104 |
| 6h | 21.959 | 21.467 | 21.408 | 21.167 | 21.728 | 21.419 | 21.152 | 21.133 | 21.136 | 21.123 |
| 24h | 16.933 | 16.682 | 16.644 | 16.545 | 16.873 | 16.709 | 16.485 | 16.465 | 16.477 | 16.503 |
| 7d | 17.110 | 16.578 | 16.491 | 16.399 | 16.666 | 16.596 | 16.386 | 16.364 | 16.355 | 16.384 |
| 30d | 14.381 | 13.927 | 13.890 | 13.827 | 14.050 | 13.989 | 13.799 | 13.776 | 13.776 | 13.802 |

## Next candle

- candle starting 2026-10-19 19:51 UTC, last close 2392.58
- P(up) 0.476, return quantiles (bp): {'05': -9.817, '10': -7.181, '25': -3.881, '40': -1.797, '50': -0.41, '60': 1.321, '75': 3.648, '90': 7.553, '95': 10.027}
- changepoint probability 0.0912, regime age 145.9 min
- agent weights: empirical 0.008, ewma 0.049, garch 0.061, har 0.235, bocpd 0.013, hmm 0.042, online_qr 0.285, lgbm 0.307

## Learning log

- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- HMM volatility states (sd, bp per minute): [3.26, 6.11, 16.29], current probabilities: [0.001, 0.96, 0.038]
- live generator: {'versions': 60, 'latest_effective': '2026-10-19 20:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.386, 'l_abs': 0.752, 'l_hi': 0.768, 'l_lo': 0.745, 'b05': 0.731, 'b25': 0.758, 'b75': 0.709, 'b95': 0.713}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8]], 'cone_width': [1.372, 1.464, 1.564, 2.056, 2.702, 2.542, 3.07, 3.606, 3.118, 3.343, 3.715, 3.649, 4.543, 3.858]}
- calibration offsets (in sigma): {'05': 0.075, '10': 0.01, '25': -0.075, '40': -0.11, '50': -0.08, '60': -0.04, '75': -0.035, '90': -0.03, '95': -0.025}
