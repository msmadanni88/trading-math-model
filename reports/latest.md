# ETH-USD 60s candle generator - report

- generated: 2026-10-27 00:34 UTC
- last closed candle: 2026-10-27 00:34 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.530 (672) [0.494, 0.569] | 0.522 (2876) [0.503, 0.542] | 0.516 (5274) [0.503, 0.530] | 0.523 (2302) [0.499, 0.546] | 0.000 (2) | 0.500 | flat -0.009 (noise 0.032) |
| colour_clear | 0.538 (824) | 0.548 (5704) [0.540, 0.558] | 0.536 (23552) [0.528, 0.543] | 0.518 (43117) [0.512, 0.524] | 0.546 (18879) [0.541, 0.550] | 0.478 (23) | 0.500 | flat -0.001 (noise 0.009) |
| colour_confident | 0.613 (160) | 0.601 (1419) [0.588, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.714 (7) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.522 (1432) | 0.531 (10039) [0.525, 0.537] | 0.524 (42872) [0.520, 0.529] | 0.513 (78622) [0.509, 0.517] | 0.529 (34273) [0.525, 0.533] | 0.471 (34) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.499 (20048) | 0.500 (140546) [0.498, 0.503] | 0.501 (600208) [0.499, 0.502] | 0.501 (1100708) [0.500, 0.502] | 0.500 (479822) [0.499, 0.502] | 0.500 (476) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.604 (53) | 0.626 (420) [0.602, 0.667] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.667 (3) | 0.500 | flat +0.015 (noise 0.045) |
| reversal_k13_next | 0.271 (59) | 0.312 (442) [0.287, 0.336] | 0.304 (2171) [0.292, 0.316] | 0.307 (3743) [0.297, 0.318] | 0.316 (1638) [0.305, 0.327] | 0.000 (1) | 0.076 | flat +0.012 (noise 0.031) |
| reversal_k13_now | 0.457 (70) | 0.546 (370) [0.500, 0.594] | 0.561 (1601) [0.541, 0.583] | 0.571 (2776) [0.555, 0.587] | 0.560 (1304) [0.537, 0.585] | 0.250 (4) | 0.076 | flat +0.011 (noise 0.036) |
| reversal_k3_next | 0.590 (117) | 0.600 (678) [0.572, 0.628] | 0.582 (2864) [0.570, 0.595] | 0.584 (4759) [0.574, 0.595] | 0.580 (2319) [0.567, 0.595] | 1.000 (3) | 0.293 | flat +0.039 (noise 0.026) |
| reversal_k3_now | 0.983 (57) | 0.946 (389) [0.921, 0.968] | 0.936 (1694) [0.927, 0.946] | 0.938 (3126) [0.931, 0.945] | 0.933 (1363) [0.922, 0.944] | 1.000 (4) | 0.293 | flat +0.008 (noise 0.021) |
| reversal_k5_next | 0.509 (110) | 0.479 (893) [0.448, 0.502] | 0.465 (3032) [0.451, 0.478] | 0.477 (4553) [0.465, 0.490] | 0.464 (2563) [0.449, 0.480] | 0.500 (2) | 0.187 | flat +0.027 (noise 0.024) |
| reversal_k5_now | 0.833 (54) | 0.820 (361) [0.808, 0.831] | 0.829 (1568) [0.816, 0.842] | 0.830 (2874) [0.819, 0.840] | 0.820 (1263) [0.807, 0.833] | 0.250 (4) | 0.187 | flat +0.002 (noise 0.029) |
| reversal_k8_next | 0.336 (110) | 0.379 (755) [0.359, 0.396] | 0.380 (2651) [0.368, 0.392] | 0.388 (4416) [0.377, 0.399] | 0.380 (2310) [0.367, 0.394] | 0.000 (1) | 0.120 | flat +0.014 (noise 0.025) |
| reversal_k8_now | 0.545 (55) | 0.658 (342) [0.608, 0.707] | 0.689 (1530) [0.667, 0.710] | 0.699 (2842) [0.683, 0.715] | 0.680 (1255) [0.657, 0.705] | 0.250 (4) | 0.121 | flat -0.014 (noise 0.036) |
| overall | 0.501 (22208) | 0.504 (155487) [0.501, 0.507] | 0.504 (663067) [0.503, 0.505] | 0.503 (1213693) [0.502, 0.504] | 0.504 (530412) [0.502, 0.506] | 0.495 (535) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07923, 0.1183] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5303, 'levels': [{'threshold': 0.07923, 'calls_per_day': 146.4, 'win_rate': 0.6064}, {'threshold': 0.1183, 'calls_per_day': 37.0, 'win_rate': 0.6346}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 33168, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14892 | 0.336 | 0.523 (14648) | 0.588 (1726) | 0.765 (2479) |
| volatility: normal | 14891 | 0.364 | 0.526 (14819) | 0.609 (1271) | 0.746 (2217) |
| volatility: wild | 14891 | 0.379 | 0.522 (14848) | 0.634 (631) | 0.765 (1904) |
| session: Asia 00-08 | 14914 | 0.358 | 0.530 (14809) | 0.608 (1279) | 0.759 (2168) |
| session: Europe 08-13 | 9300 | 0.355 | 0.528 (9212) | 0.599 (893) | 0.757 (1482) |
| session: US 13-21 | 14880 | 0.367 | 0.519 (14776) | 0.596 (921) | 0.767 (2119) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.609 (535) | 0.737 (831) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.305 | 0.369 | 0.246 | 0.246 | 0.390 | 0.165 | 0.446 | 1.249 |
| 6h | 360 | 0.337 | 0.346 | 0.282 | 0.296 | 0.494 | 0.233 | 0.442 | 1.138 |
| 24h | 1440 | 0.371 | 0.365 | 0.297 | 0.332 | 0.522 | 0.260 | 0.483 | 1.202 |
| 7d | 10080 | 0.369 | 0.359 | 0.277 | 0.310 | 0.530 | 0.267 | 0.472 | 1.212 |
| 30d | 43200 | 0.361 | 0.354 | 0.277 | 0.306 | 0.524 | 0.258 | 0.464 | 1.274 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.305 / 0.390 / 0.917; 2: 0.374 / 0.610 / 0.950; 3: 0.326 / 0.424 / 0.917; 4: 0.366 / 0.610 / 0.933; 5: 0.305 / 0.407 / 0.950; 6: 0.370 / 0.661 / 0.917; 7: 0.312 / 0.424 / 0.917; 8: 0.298 / 0.407 / 0.933; 9: 0.346 / 0.508 / 0.933; 10: 0.329 / 0.492 / 0.967; 11: 0.321 / 0.441 / 0.917; 12: 0.321 / 0.424 / 0.900; 13: 0.337 / 0.475 / 0.883; 14: 0.350 / 0.475 / 0.883; 15: 0.316 / 0.458 / 0.883
- 6h: 1: 0.337 / 0.494 / 0.897; 2: 0.334 / 0.483 / 0.903; 3: 0.345 / 0.511 / 0.892; 4: 0.356 / 0.522 / 0.911; 5: 0.333 / 0.489 / 0.933; 6: 0.341 / 0.506 / 0.914; 7: 0.351 / 0.522 / 0.900; 8: 0.333 / 0.486 / 0.892; 9: 0.357 / 0.528 / 0.867; 10: 0.338 / 0.472 / 0.856; 11: 0.332 / 0.458 / 0.856; 12: 0.345 / 0.520 / 0.858; 13: 0.349 / 0.522 / 0.839; 14: 0.340 / 0.503 / 0.836; 15: 0.352 / 0.514 / 0.842
- 24h: 1: 0.371 / 0.522 / 0.893; 2: 0.361 / 0.483 / 0.903; 3: 0.363 / 0.508 / 0.901; 4: 0.362 / 0.501 / 0.906; 5: 0.362 / 0.506 / 0.903; 6: 0.358 / 0.497 / 0.906; 7: 0.357 / 0.496 / 0.906; 8: 0.355 / 0.480 / 0.903; 9: 0.366 / 0.518 / 0.901; 10: 0.359 / 0.508 / 0.900; 11: 0.354 / 0.483 / 0.899; 12: 0.361 / 0.513 / 0.897; 13: 0.354 / 0.483 / 0.894; 14: 0.359 / 0.508 / 0.894; 15: 0.359 / 0.502 / 0.892
- 7d: 1: 0.369 / 0.530 / 0.897; 2: 0.357 / 0.500 / 0.900; 3: 0.357 / 0.509 / 0.901; 4: 0.355 / 0.500 / 0.901; 5: 0.354 / 0.502 / 0.900; 6: 0.352 / 0.496 / 0.901; 7: 0.352 / 0.498 / 0.900; 8: 0.353 / 0.506 / 0.900; 9: 0.353 / 0.500 / 0.900; 10: 0.352 / 0.504 / 0.900; 11: 0.350 / 0.497 / 0.900; 12: 0.352 / 0.504 / 0.900; 13: 0.349 / 0.494 / 0.899; 14: 0.350 / 0.494 / 0.900; 15: 0.350 / 0.501 / 0.899
- 30d: 1: 0.361 / 0.524 / 0.898; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.505 / 0.900; 13: 0.346 / 0.501 / 0.899; 14: 0.345 / 0.499 / 0.899; 15: 0.346 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.136 (body 0.082, range 0.191); 'price stays where it was' would score 0.160; colour right 0.458; typical miss of the close 8.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.138 (body 0.093, range 0.182); 'price stays where it was' would score 0.136; colour right 0.486; typical miss of the close 7.7 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.130 (body 0.085, range 0.175); 'price stays where it was' would score 0.142; colour right 0.491; typical miss of the close 10.8 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.135; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.530 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.9; 2: 0.197 / 4.5; 3: 0.168 / 6.0; 4: 0.131 / 6.5; 5: 0.123 / 7.2; 6: 0.112 / 7.7; 7: 0.107 / 8.0; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.087 / 9.1; 11: 0.085 / 9.6; 12: 0.076 / 9.9; 13: 0.067 / 10.2; 14: 0.069 / 10.6; 15: 0.060 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 122188, probability skill vs chance 0.2381, widened contest next: False
  - now: threshold 0.8339, hit rate recent 0.9583 / long run 0.9388
    - 6h: 15 calls (61 a day), hit rate 1.000, chance 0.294, naive rule 0.507, lift 3.40x
    - 24h: 61 calls (61 a day), hit rate 0.984, chance 0.293, naive rule 0.483, lift 3.36x
    - 7d: 390 calls (56 a day), hit rate 0.949, chance 0.298, naive rule 0.504, lift 3.18x
    - 30d: 1698 calls (57 a day), hit rate 0.936, chance 0.294, naive rule 0.492, lift 3.19x
  - next: threshold 0.5304, hit rate recent 0.6099 / long run 0.5923
    - 6h: 33 calls (134 a day), hit rate 0.667, chance 0.294, lift 2.26x
    - 24h: 119 calls (119 a day), hit rate 0.597, chance 0.293, lift 2.04x
    - 7d: 678 calls (97 a day), hit rate 0.602, chance 0.298, lift 2.02x
    - 30d: 2863 calls (95 a day), hit rate 0.583, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.494; 0.35: 538, 0.519; 0.40: 478, 0.575; 0.45: 408, 0.646; 0.50: 356, 0.698; 0.55: 312, 0.741; 0.60: 264, 0.785; 0.65: 221, 0.811; 0.70: 175, 0.843; 0.75: 136, 0.875; 0.80: 91, 0.914; 0.85: 47, 0.951; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.427; 0.35: 502, 0.464; 0.40: 408, 0.499; 0.45: 310, 0.534; 0.50: 201, 0.570; 0.55: 90, 0.574; 0.60: 14, 0.629; 0.65: 1, 0.677
- **K=5**: model 1792540800, labels learned 122186, probability skill vs chance 0.2163, widened contest next: True
  - now: threshold 0.6716, hit rate recent 0.7771 / long run 0.8181
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.190, naive rule 0.396, lift 3.62x
    - 24h: 58 calls (58 a day), hit rate 0.793, chance 0.190, naive rule 0.395, lift 4.17x
    - 7d: 362 calls (52 a day), hit rate 0.815, chance 0.185, naive rule 0.407, lift 4.40x
    - 30d: 1572 calls (52 a day), hit rate 0.828, chance 0.187, naive rule 0.400, lift 4.42x
  - next: threshold 0.449, hit rate recent 0.4981 / long run 0.4807
    - 6h: 26 calls (106 a day), hit rate 0.500, chance 0.190, lift 2.63x
    - 24h: 111 calls (112 a day), hit rate 0.505, chance 0.190, lift 2.65x
    - 7d: 892 calls (128 a day), hit rate 0.479, chance 0.185, lift 2.59x
    - 30d: 3032 calls (101 a day), hit rate 0.465, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.425; 0.35: 344, 0.492; 0.40: 277, 0.564; 0.45: 225, 0.619; 0.50: 177, 0.669; 0.55: 137, 0.710; 0.60: 105, 0.753; 0.65: 76, 0.789; 0.70: 52, 0.829; 0.75: 30, 0.874; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.390; 0.35: 253, 0.421; 0.40: 158, 0.453; 0.45: 70, 0.466; 0.50: 15, 0.488; 0.55: 1, 0.528
- **K=8**: model 1793059200, labels learned 122183, probability skill vs chance 0.194, widened contest next: True
  - now: threshold 0.5555, hit rate recent 0.5821 / long run 0.6703
    - 6h: 15 calls (62 a day), hit rate 0.600, chance 0.106, naive rule 0.295, lift 5.68x
    - 24h: 58 calls (58 a day), hit rate 0.517, chance 0.113, naive rule 0.301, lift 4.58x
    - 7d: 343 calls (49 a day), hit rate 0.653, chance 0.116, naive rule 0.322, lift 5.64x
    - 30d: 1533 calls (51 a day), hit rate 0.688, chance 0.121, naive rule 0.329, lift 5.71x
  - next: threshold 0.3357, hit rate recent 0.3338 / long run 0.3744
    - 6h: 28 calls (115 a day), hit rate 0.321, chance 0.106, lift 3.04x
    - 24h: 110 calls (111 a day), hit rate 0.327, chance 0.113, lift 2.90x
    - 7d: 752 calls (108 a day), hit rate 0.379, chance 0.116, lift 3.28x
    - 30d: 2649 calls (88 a day), hit rate 0.380, chance 0.121, lift 3.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.426; 0.35: 188, 0.496; 0.40: 145, 0.547; 0.45: 111, 0.592; 0.50: 84, 0.634; 0.55: 61, 0.669; 0.60: 40, 0.715; 0.65: 23, 0.789; 0.70: 10, 0.833; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.354; 0.35: 96, 0.381; 0.40: 34, 0.401; 0.45: 7, 0.427; 0.50: 1, 0.600
- **K=13**: model 1793059200, labels learned 122178, probability skill vs chance 0.174, widened contest next: True
  - now: threshold 0.4161, hit rate recent 0.4772 / long run 0.5482
    - 6h: 20 calls (83 a day), hit rate 0.450, chance 0.065, naive rule 0.221, lift 6.90x
    - 24h: 73 calls (74 a day), hit rate 0.438, chance 0.073, naive rule 0.246, lift 5.98x
    - 7d: 371 calls (53 a day), hit rate 0.544, chance 0.073, naive rule 0.265, lift 7.45x
    - 30d: 1605 calls (54 a day), hit rate 0.561, chance 0.077, naive rule 0.272, lift 7.28x
  - next: threshold 0.2947, hit rate recent 0.2813 / long run 0.3091
    - 6h: 13 calls (54 a day), hit rate 0.154, chance 0.065, lift 2.36x
    - 24h: 60 calls (61 a day), hit rate 0.267, chance 0.073, lift 3.64x
    - 7d: 439 calls (63 a day), hit rate 0.312, chance 0.073, lift 4.27x
    - 30d: 2172 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.440; 0.35: 88, 0.491; 0.40: 62, 0.547; 0.45: 41, 0.598; 0.50: 26, 0.655; 0.55: 16, 0.707; 0.60: 7, 0.748; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.315; 0.35: 14, 0.349; 0.40: 2, 0.449; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.974 | 9.51% | 0.917 | 0.533 | 0.249 | 0.525 | -0.017 |
| 6h | 12.621 | 4.94% | 0.900 | 0.478 | 0.250 | 0.506 | 0.280 |
| 24h | 17.739 | 4.39% | 0.902 | 0.497 | 0.251 | 0.499 | 0.646 |
| 7d | 15.267 | 3.61% | 0.899 | 0.500 | 0.251 | 0.500 | 0.662 |
| 30d | 13.694 | 4.15% | 0.900 | 0.499 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.022 | 9.990 | 9.961 | 10.175 | 10.089 | 9.960 | 10.086 | 9.964 | 9.970 | 9.974 |
| 6h | 13.277 | 12.707 | 12.660 | 12.761 | 12.778 | 12.677 | 12.662 | 12.598 | 12.615 | 12.621 |
| 24h | 18.554 | 17.853 | 17.879 | 17.797 | 17.925 | 17.976 | 17.725 | 17.698 | 17.701 | 17.739 |
| 7d | 15.838 | 15.407 | 15.345 | 15.289 | 15.528 | 15.417 | 15.256 | 15.225 | 15.235 | 15.267 |
| 30d | 14.288 | 13.827 | 13.779 | 13.719 | 13.939 | 13.874 | 13.689 | 13.670 | 13.669 | 13.694 |

## Next candle

- candle starting 2026-10-27 00:34 UTC, last close 2322.86
- P(up) 0.5205, return quantiles (bp): {'05': -8.546, '10': -6.575, '25': -3.11, '40': -0.95, '50': 0.241, '60': 1.626, '75': 3.713, '90': 6.429, '95': 8.379}
- changepoint probability 0.1923, regime age 77.6 min
- agent weights: empirical 0.004, ewma 0.093, garch 0.133, har 0.116, bocpd 0.051, hmm 0.110, online_qr 0.192, lgbm 0.301

## Learning log

- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- HMM volatility states (sd, bp per minute): [3.4, 6.54, 17.69], current probabilities: [0.184, 0.768, 0.047]
- live generator: {'versions': 60, 'latest_effective': '2026-10-27 00:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.333, 'l_abs': 0.705, 'l_hi': 0.801, 'l_lo': 0.793, 'b05': 0.753, 'b25': 0.716, 'b75': 0.676, 'b95': 0.718}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8]], 'cone_width': [1.42, 1.85, 1.899, 2.259, 2.479, 2.849, 3.113, 3.444, 3.786, 4.059, 4.421, 4.799, 4.7, 4.875]}
- calibration offsets (in sigma): {'05': -0.0335, '10': -0.047, '25': 0.0125, '40': 0.032, '50': 0.055, '60': 0.098, '75': 0.1075, '90': -0.003, '95': -0.0365}
