# ETH-USD 60s candle generator - report

- generated: 2026-11-20 08:36 UTC
- last closed candle: 2026-11-20 08:36 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.525 (672) [0.495, 0.552] | 0.517 (2879) [0.502, 0.534] | 0.515 (7577) [0.505, 0.526] | 0.518 (4605) [0.503, 0.532] | 0.529 (34) | 0.500 | flat -0.002 (noise 0.027) |
| colour_clear | 0.537 (831) | 0.546 (5673) [0.536, 0.558] | 0.540 (23966) [0.534, 0.546] | 0.525 (62227) [0.520, 0.530] | 0.543 (37989) [0.539, 0.547] | 0.572 (299) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | 0.576 (151) | 0.556 (1085) [0.531, 0.583] | 0.577 (4499) [0.565, 0.589] | 0.586 (6910) [0.576, 0.596] | 0.586 (6910) [0.576, 0.596] | 0.564 (39) | 0.500 | flat -0.013 (noise 0.023) |
| colour_next | 0.535 (1436) | 0.533 (10046) [0.527, 0.539] | 0.530 (42892) [0.526, 0.534] | 0.518 (112914) [0.515, 0.522] | 0.530 (68565) [0.527, 0.533] | 0.510 (516) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.499 (20104) | 0.502 (140644) [0.500, 0.504] | 0.502 (600488) [0.501, 0.503] | 0.501 (1580796) [0.500, 0.502] | 0.501 (959910) [0.500, 0.502] | 0.513 (7224) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.676 (34) | 0.606 (289) [0.570, 0.650] | 0.613 (1184) [0.596, 0.629] | 0.625 (1813) [0.610, 0.641] | 0.625 (1813) [0.610, 0.641] | 0.400 (5) | 0.500 | flat -0.017 (noise 0.042) |
| reversal_k13_next | 0.275 (91) | 0.300 (487) [0.271, 0.339] | 0.325 (1870) [0.309, 0.343] | 0.314 (5247) [0.304, 0.323] | 0.323 (3142) [0.312, 0.334] | 0.308 (26) | 0.077 | flat -0.035 (noise 0.030) |
| reversal_k13_now | 0.515 (68) | 0.560 (384) [0.513, 0.618] | 0.570 (1627) [0.549, 0.592] | 0.572 (4084) [0.560, 0.584] | 0.567 (2612) [0.551, 0.584] | 0.786 (14) | 0.077 | flat -0.019 (noise 0.037) |
| reversal_k3_next | 0.544 (79) | 0.595 (407) [0.567, 0.637] | 0.604 (2365) [0.593, 0.617] | 0.589 (6568) [0.580, 0.597] | 0.589 (4128) [0.579, 0.600] | 0.553 (47) | 0.293 | flat -0.014 (noise 0.035) |
| reversal_k3_now | 0.894 (66) | 0.941 (375) [0.924, 0.959] | 0.933 (1727) [0.924, 0.944] | 0.935 (4521) [0.930, 0.941] | 0.931 (2758) [0.924, 0.939] | 0.960 (25) | 0.293 | flat +0.023 (noise 0.018) |
| reversal_k5_next | 0.407 (54) | 0.475 (425) [0.422, 0.534] | 0.503 (2167) [0.488, 0.518] | 0.484 (5956) [0.473, 0.495] | 0.479 (3966) [0.465, 0.492] | 0.533 (15) | 0.187 | flat -0.024 (noise 0.039) |
| reversal_k5_now | 0.831 (65) | 0.775 (441) [0.748, 0.803] | 0.794 (1740) [0.777, 0.809] | 0.816 (4303) [0.806, 0.826] | 0.804 (2692) [0.792, 0.816] | 0.950 (20) | 0.187 | flat +0.015 (noise 0.032) |
| reversal_k8_next | 0.405 (89) | 0.395 (511) [0.365, 0.440] | 0.409 (2379) [0.394, 0.424] | 0.397 (6149) [0.387, 0.406] | 0.397 (4043) [0.385, 0.408] | 0.304 (23) | 0.121 | flat -0.024 (noise 0.031) |
| reversal_k8_now | 0.690 (71) | 0.659 (419) [0.617, 0.705] | 0.682 (1617) [0.663, 0.702] | 0.695 (4159) [0.683, 0.707] | 0.683 (2572) [0.668, 0.699] | 0.889 (18) | 0.122 | flat -0.024 (noise 0.034) |
| overall | 0.503 (22219) | 0.506 (154811) [0.504, 0.507] | 0.506 (661751) [0.505, 0.507] | 0.504 (1742274) [0.503, 0.505] | 0.505 (1058993) [0.504, 0.506] | 0.516 (7962) | - | flat +0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06925, 0.1] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5326, 'levels': [{'threshold': 0.06925, 'calls_per_day': 144.8, 'win_rate': 0.5565}, {'threshold': 0.1, 'calls_per_day': 35.9, 'win_rate': 0.619}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42893, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15052 | 0.349 | 0.534 (14837) | 0.569 (2264) | 0.750 (2501) |
| volatility: normal | 15052 | 0.376 | 0.527 (14996) | 0.592 (1391) | 0.740 (2341) |
| volatility: wild | 15052 | 0.390 | 0.530 (15014) | 0.576 (1092) | 0.760 (2146) |
| session: Asia 00-08 | 15360 | 0.371 | 0.533 (15250) | 0.571 (1652) | 0.748 (2303) |
| session: Europe 08-13 | 9336 | 0.365 | 0.529 (9260) | 0.587 (1163) | 0.757 (1521) |
| session: US 13-21 | 14880 | 0.379 | 0.533 (14791) | 0.595 (1315) | 0.749 (2342) |
| session: late 21-24 | 5580 | 0.366 | 0.518 (5546) | 0.535 (617) | 0.746 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.392 | 0.372 | 0.295 | 0.295 | 0.500 | 0.254 | 0.530 | 0.925 |
| 6h | 360 | 0.390 | 0.383 | 0.319 | 0.362 | 0.486 | 0.265 | 0.515 | 1.223 |
| 24h | 1440 | 0.386 | 0.384 | 0.302 | 0.342 | 0.531 | 0.262 | 0.509 | 1.233 |
| 7d | 10080 | 0.386 | 0.377 | 0.302 | 0.337 | 0.532 | 0.271 | 0.502 | 1.166 |
| 30d | 43200 | 0.371 | 0.365 | 0.285 | 0.317 | 0.530 | 0.266 | 0.477 | 1.261 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.392 / 0.500 / 0.867; 2: 0.406 / 0.617 / 0.917; 3: 0.379 / 0.450 / 0.983; 4: 0.396 / 0.517 / 0.883; 5: 0.393 / 0.467 / 0.883; 6: 0.385 / 0.467 / 0.900; 7: 0.395 / 0.483 / 0.967; 8: 0.403 / 0.517 / 0.967; 9: 0.398 / 0.500 / 0.967; 10: 0.401 / 0.567 / 1.000; 11: 0.407 / 0.550 / 1.000; 12: 0.363 / 0.400 / 0.850; 13: 0.387 / 0.467 / 0.800; 14: 0.380 / 0.483 / 0.900; 15: 0.380 / 0.417 / 0.883
- 6h: 1: 0.390 / 0.486 / 0.911; 2: 0.399 / 0.550 / 0.947; 3: 0.393 / 0.506 / 0.981; 4: 0.391 / 0.500 / 0.906; 5: 0.397 / 0.531 / 0.908; 6: 0.391 / 0.489 / 0.878; 7: 0.393 / 0.508 / 0.958; 8: 0.396 / 0.522 / 0.964; 9: 0.393 / 0.517 / 0.953; 10: 0.396 / 0.539 / 1.000; 11: 0.393 / 0.511 / 1.000; 12: 0.385 / 0.486 / 0.850; 13: 0.391 / 0.511 / 0.819; 14: 0.380 / 0.467 / 0.878; 15: 0.386 / 0.494 / 0.844
- 24h: 1: 0.386 / 0.531 / 0.892; 2: 0.380 / 0.507 / 0.899; 3: 0.374 / 0.498 / 0.910; 4: 0.381 / 0.498 / 0.894; 5: 0.387 / 0.539 / 0.890; 6: 0.381 / 0.518 / 0.887; 7: 0.378 / 0.494 / 0.895; 8: 0.383 / 0.534 / 0.896; 9: 0.378 / 0.514 / 0.893; 10: 0.376 / 0.510 / 0.895; 11: 0.377 / 0.505 / 0.893; 12: 0.369 / 0.491 / 0.885; 13: 0.377 / 0.509 / 0.878; 14: 0.370 / 0.484 / 0.885; 15: 0.372 / 0.495 / 0.878
- 7d: 1: 0.386 / 0.532 / 0.899; 2: 0.374 / 0.494 / 0.900; 3: 0.378 / 0.513 / 0.900; 4: 0.372 / 0.492 / 0.900; 5: 0.375 / 0.508 / 0.899; 6: 0.373 / 0.503 / 0.899; 7: 0.374 / 0.506 / 0.901; 8: 0.375 / 0.514 / 0.901; 9: 0.368 / 0.492 / 0.901; 10: 0.373 / 0.509 / 0.901; 11: 0.372 / 0.506 / 0.901; 12: 0.371 / 0.503 / 0.899; 13: 0.370 / 0.502 / 0.899; 14: 0.371 / 0.502 / 0.900; 15: 0.368 / 0.496 / 0.898
- 30d: 1: 0.371 / 0.530 / 0.898; 2: 0.359 / 0.493 / 0.900; 3: 0.362 / 0.512 / 0.900; 4: 0.358 / 0.497 / 0.900; 5: 0.359 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.501 / 0.900; 8: 0.358 / 0.508 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.357 / 0.502 / 0.900; 11: 0.356 / 0.504 / 0.900; 12: 0.356 / 0.503 / 0.900; 13: 0.355 / 0.500 / 0.899; 14: 0.355 / 0.501 / 0.900; 15: 0.355 / 0.500 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.168 (body 0.128, range 0.208); 'price stays where it was' would score 0.193; colour right 0.517; typical miss of the close 13.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.152 (body 0.113, range 0.192); 'price stays where it was' would score 0.157; colour right 0.497; typical miss of the close 15.2 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.138 (body 0.089, range 0.188); 'price stays where it was' would score 0.144; colour right 0.516; typical miss of the close 15.5 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.128 (body 0.084, range 0.173); 'price stays where it was' would score 0.132; colour right 0.505; typical miss of the close 14.9 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.129; colour right 0.502; typical miss of the close 10.0 bp; chain ended on the right side 0.516 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.3; 2: 0.205 / 6.0; 3: 0.168 / 7.9; 4: 0.135 / 8.2; 5: 0.127 / 8.9; 6: 0.119 / 9.7; 7: 0.113 / 10.3; 8: 0.100 / 11.3; 9: 0.093 / 11.5; 10: 0.089 / 12.1; 11: 0.086 / 12.5; 12: 0.078 / 12.6; 13: 0.074 / 13.3; 14: 0.068 / 13.7; 15: 0.067 / 14.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 157230, probability skill vs chance 0.2358, widened contest next: True
  - now: threshold 0.8313, hit rate recent 0.9278 / long run 0.9316
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.289, naive rule 0.500, lift 3.20x
    - 24h: 69 calls (69 a day), hit rate 0.913, chance 0.290, naive rule 0.492, lift 3.15x
    - 7d: 378 calls (54 a day), hit rate 0.939, chance 0.291, naive rule 0.503, lift 3.23x
    - 30d: 1731 calls (58 a day), hit rate 0.934, chance 0.293, naive rule 0.500, lift 3.18x
  - next: threshold 0.5122, hit rate recent 0.5555 / long run 0.5939
    - 6h: 32 calls (130 a day), hit rate 0.531, chance 0.289, lift 1.84x
    - 24h: 107 calls (107 a day), hit rate 0.533, chance 0.290, lift 1.84x
    - 7d: 440 calls (63 a day), hit rate 0.591, chance 0.291, lift 2.03x
    - 30d: 2359 calls (79 a day), hit rate 0.600, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.501; 0.35: 530, 0.526; 0.40: 477, 0.576; 0.45: 411, 0.642; 0.50: 362, 0.688; 0.55: 314, 0.734; 0.60: 264, 0.780; 0.65: 223, 0.809; 0.70: 175, 0.841; 0.75: 141, 0.873; 0.80: 93, 0.906; 0.85: 45, 0.941; 0.90: 4, 0.967
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.434; 0.35: 491, 0.467; 0.40: 389, 0.508; 0.45: 293, 0.543; 0.50: 187, 0.574; 0.55: 81, 0.585; 0.60: 11, 0.632; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 157228, probability skill vs chance 0.2096, widened contest next: True
  - now: threshold 0.6999, hit rate recent 0.8477 / long run 0.7898
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.171, naive rule 0.376, lift 5.83x
    - 24h: 61 calls (61 a day), hit rate 0.869, chance 0.189, naive rule 0.399, lift 4.59x
    - 7d: 436 calls (62 a day), hit rate 0.784, chance 0.187, naive rule 0.414, lift 4.19x
    - 30d: 1742 calls (58 a day), hit rate 0.797, chance 0.186, naive rule 0.410, lift 4.27x
  - next: threshold 0.4627, hit rate recent 0.4393 / long run 0.4845
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.171, lift 3.50x
    - 24h: 57 calls (57 a day), hit rate 0.421, chance 0.189, lift 2.23x
    - 7d: 421 calls (60 a day), hit rate 0.482, chance 0.187, lift 2.58x
    - 30d: 2137 calls (71 a day), hit rate 0.501, chance 0.186, lift 2.69x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 362, 0.473; 0.40: 293, 0.542; 0.45: 238, 0.602; 0.50: 188, 0.652; 0.55: 150, 0.687; 0.60: 114, 0.734; 0.65: 80, 0.773; 0.70: 50, 0.809; 0.75: 28, 0.840; 0.80: 7, 0.863
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.389; 0.35: 252, 0.428; 0.40: 161, 0.457; 0.45: 65, 0.496; 0.50: 8, 0.555; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 157225, probability skill vs chance 0.2033, widened contest next: True
  - now: threshold 0.5762, hit rate recent 0.7292 / long run 0.6803
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.124, naive rule 0.351, lift 7.38x
    - 24h: 66 calls (66 a day), hit rate 0.727, chance 0.116, naive rule 0.323, lift 6.28x
    - 7d: 414 calls (59 a day), hit rate 0.669, chance 0.122, naive rule 0.346, lift 5.49x
    - 30d: 1617 calls (54 a day), hit rate 0.685, chance 0.122, naive rule 0.342, lift 5.64x
  - next: threshold 0.3488, hit rate recent 0.354 / long run 0.4022
    - 6h: 18 calls (74 a day), hit rate 0.278, chance 0.124, lift 2.23x
    - 24h: 92 calls (93 a day), hit rate 0.337, chance 0.116, lift 2.91x
    - 7d: 520 calls (74 a day), hit rate 0.394, chance 0.122, lift 3.23x
    - 30d: 2364 calls (79 a day), hit rate 0.407, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 253, 0.425; 0.35: 198, 0.486; 0.40: 156, 0.535; 0.45: 119, 0.580; 0.50: 85, 0.636; 0.55: 60, 0.677; 0.60: 40, 0.717; 0.65: 23, 0.778; 0.70: 10, 0.829; 0.75: 2, 0.755
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 163, 0.372; 0.35: 85, 0.399; 0.40: 26, 0.429; 0.45: 5, 0.465; 0.50: 1, 0.731
- **K=13**: model 1795132800, labels learned 157220, probability skill vs chance 0.1787, widened contest next: True
  - now: threshold 0.4542, hit rate recent 0.5625 / long run 0.5688
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.096, naive rule 0.344, lift 9.15x
    - 24h: 59 calls (60 a day), hit rate 0.576, chance 0.079, naive rule 0.264, lift 7.27x
    - 7d: 377 calls (54 a day), hit rate 0.565, chance 0.079, naive rule 0.296, lift 7.11x
    - 30d: 1626 calls (54 a day), hit rate 0.573, chance 0.078, naive rule 0.289, lift 7.31x
  - next: threshold 0.3005, hit rate recent 0.2812 / long run 0.3142
    - 6h: 19 calls (79 a day), hit rate 0.263, chance 0.096, lift 2.75x
    - 24h: 94 calls (95 a day), hit rate 0.255, chance 0.079, lift 3.22x
    - 7d: 501 calls (72 a day), hit rate 0.301, chance 0.079, lift 3.79x
    - 30d: 1869 calls (62 a day), hit rate 0.324, chance 0.078, lift 4.14x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 139, 0.424; 0.35: 101, 0.473; 0.40: 70, 0.534; 0.45: 48, 0.584; 0.50: 34, 0.625; 0.55: 21, 0.646; 0.60: 11, 0.683; 0.65: 3, 0.603; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.333; 0.35: 14, 0.353; 0.40: 2, 0.403; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 22.577 | -0.28% | 0.883 | 0.467 | 0.253 | 0.400 | -0.080 |
| 6h | 24.177 | 0.67% | 0.900 | 0.500 | 0.252 | 0.489 | 0.405 |
| 24h | 24.626 | 2.82% | 0.890 | 0.501 | 0.250 | 0.520 | 0.600 |
| 7d | 24.344 | 3.82% | 0.899 | 0.501 | 0.250 | 0.499 | 0.664 |
| 30d | 17.983 | 4.61% | 0.900 | 0.500 | 0.250 | 0.505 | 0.710 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 22.513 | 22.724 | 22.680 | 22.374 | 22.517 | 22.602 | 22.671 | 22.595 | 22.540 | 22.577 |
| 6h | 24.341 | 24.125 | 24.112 | 24.133 | 24.302 | 24.295 | 24.109 | 24.114 | 24.075 | 24.177 |
| 24h | 25.340 | 24.711 | 24.739 | 24.650 | 24.984 | 24.884 | 24.593 | 24.619 | 24.587 | 24.626 |
| 7d | 25.311 | 24.497 | 24.472 | 24.352 | 24.814 | 24.608 | 24.313 | 24.301 | 24.300 | 24.344 |
| 30d | 18.852 | 18.143 | 18.104 | 18.038 | 18.338 | 18.275 | 17.962 | 17.944 | 17.951 | 17.983 |

## Next candle

- candle starting 2026-11-20 08:36 UTC, last close 1754.61
- P(up) 0.5012, return quantiles (bp): {'05': -11.266, '10': -8.812, '25': -4.42, '40': -1.92, '50': 0.032, '60': 1.733, '75': 4.788, '90': 9.201, '95': 12.646}
- changepoint probability 0.0379, regime age 161.4 min
- agent weights: empirical 0.017, ewma 0.148, garch 0.141, har 0.174, bocpd 0.040, hmm 0.069, online_qr 0.213, lgbm 0.198

## Learning log

- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- HMM volatility states (sd, bp per minute): [5.69, 9.84, 21.45], current probabilities: [0.709, 0.285, 0.006]
- live generator: {'versions': 60, 'latest_effective': '2026-11-20 08:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.325, 'l_abs': 0.697, 'l_hi': 0.82, 'l_lo': 0.719, 'b05': 0.727, 'b25': 0.642, 'b75': 0.707, 'b95': 0.704}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.5, 1.8], [1.5, 1.6], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.158, 1.26, 1.854, 2.161, 2.784, 2.188, 2.297, 2.541, 2.738, 3.18, 4.771, 5.839, 4.588, 5.93]}
- calibration offsets (in sigma): {'05': 0.0275, '10': 0.005, '25': 0.0375, '40': -0.02, '50': 0.025, '60': 0.02, '75': 0.0525, '90': 0.045, '95': 0.0425}
