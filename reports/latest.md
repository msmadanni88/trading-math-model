# ETH-USD 60s candle generator - report

- generated: 2026-11-24 05:22 UTC
- last closed candle: 2026-11-24 05:22 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.525 (672) [0.504, 0.548] | 0.517 (2879) [0.501, 0.533] | 0.516 (7961) [0.505, 0.526] | 0.518 (4989) [0.504, 0.532] | 0.524 (21) | 0.500 | flat +0.008 (noise 0.027) |
| colour_clear | 0.568 (780) | 0.551 (5516) [0.537, 0.565] | 0.541 (23823) [0.535, 0.548] | 0.526 (65314) [0.521, 0.531] | 0.544 (41076) [0.539, 0.548] | 0.585 (171) | 0.500 | flat +0.011 (noise 0.010) |
| colour_confident | 0.568 (213) | 0.577 (1326) [0.557, 0.593] | 0.572 (4522) [0.562, 0.581] | 0.585 (7715) [0.576, 0.595] | 0.585 (7715) [0.576, 0.595] | 0.606 (33) | 0.500 | flat +0.044 (noise 0.022) |
| colour_next | 0.556 (1432) | 0.534 (10047) [0.526, 0.542] | 0.531 (42900) [0.527, 0.535] | 0.519 (118656) [0.516, 0.523] | 0.530 (74307) [0.527, 0.534] | 0.556 (322) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.499 (20048) | 0.503 (140658) [0.500, 0.505] | 0.502 (600600) [0.501, 0.503] | 0.501 (1661184) [0.500, 0.502] | 0.501 (1040298) [0.500, 0.502] | 0.503 (4508) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.571 (63) | 0.622 (376) [0.597, 0.648] | 0.608 (1222) [0.593, 0.622] | 0.623 (2056) [0.609, 0.638] | 0.623 (2056) [0.609, 0.638] | 0.600 (10) | 0.500 | flat +0.056 (noise 0.044) |
| reversal_k13_next | 0.319 (47) | 0.332 (449) [0.290, 0.383] | 0.337 (1827) [0.320, 0.355] | 0.317 (5445) [0.307, 0.326] | 0.328 (3340) [0.316, 0.339] | 0.429 (7) | 0.078 | flat -0.007 (noise 0.035) |
| reversal_k13_now | 0.500 (48) | 0.549 (379) [0.513, 0.588] | 0.572 (1625) [0.552, 0.592] | 0.573 (4276) [0.561, 0.585] | 0.569 (2804) [0.554, 0.584] | 0.500 (8) | 0.078 | flat -0.056 (noise 0.037) |
| reversal_k3_next | 0.547 (150) | 0.593 (865) [0.559, 0.624] | 0.600 (2649) [0.588, 0.613] | 0.590 (7211) [0.581, 0.598] | 0.591 (4771) [0.580, 0.602] | 0.513 (39) | 0.294 | flat -0.020 (noise 0.032) |
| reversal_k3_now | 0.942 (52) | 0.938 (388) [0.921, 0.956] | 0.930 (1721) [0.922, 0.939] | 0.935 (4744) [0.930, 0.940] | 0.932 (2981) [0.925, 0.939] | 1.000 (10) | 0.294 | flat +0.009 (noise 0.018) |
| reversal_k5_next | 0.417 (60) | 0.477 (346) [0.418, 0.556] | 0.511 (1825) [0.491, 0.531] | 0.486 (6131) [0.475, 0.498] | 0.482 (4141) [0.468, 0.497] | 0.464 (28) | 0.187 | flat -0.024 (noise 0.049) |
| reversal_k5_now | 0.807 (57) | 0.814 (413) [0.794, 0.833] | 0.796 (1763) [0.779, 0.811] | 0.817 (4534) [0.806, 0.826] | 0.805 (2923) [0.793, 0.816] | 0.800 (10) | 0.188 | up +0.064 (noise 0.028) |
| reversal_k8_next | 0.354 (79) | 0.411 (577) [0.380, 0.448] | 0.416 (2278) [0.401, 0.432] | 0.398 (6465) [0.388, 0.408] | 0.399 (4359) [0.388, 0.411] | 0.571 (14) | 0.121 | flat -0.010 (noise 0.031) |
| reversal_k8_now | 0.625 (56) | 0.667 (423) [0.647, 0.685] | 0.679 (1646) [0.661, 0.698] | 0.693 (4385) [0.682, 0.706] | 0.682 (2798) [0.667, 0.696] | 0.615 (13) | 0.122 | flat +0.009 (noise 0.033) |
| overall | 0.504 (22125) | 0.507 (155217) [0.505, 0.509] | 0.506 (661713) [0.505, 0.507] | 0.504 (1830992) [0.503, 0.505] | 0.505 (1147711) [0.504, 0.506] | 0.508 (4980) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07715, 0.1101] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5344, 'levels': [{'threshold': 0.07715, 'calls_per_day': 144.7, 'win_rate': 0.5856}, {'threshold': 0.1101, 'calls_per_day': 36.6, 'win_rate': 0.6148}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42900, 'rate': 0.5313}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14988 | 0.349 | 0.533 (14769) | 0.561 (2182) | 0.748 (2502) |
| volatility: normal | 14987 | 0.379 | 0.528 (14936) | 0.581 (1500) | 0.748 (2402) |
| volatility: wild | 14987 | 0.390 | 0.532 (14948) | 0.588 (1142) | 0.751 (2102) |
| session: Asia 00-08 | 15202 | 0.371 | 0.530 (15091) | 0.561 (1694) | 0.749 (2285) |
| session: Europe 08-13 | 9300 | 0.367 | 0.533 (9224) | 0.583 (1188) | 0.759 (1468) |
| session: US 13-21 | 14880 | 0.380 | 0.535 (14790) | 0.602 (1336) | 0.741 (2403) |
| session: late 21-24 | 5580 | 0.367 | 0.517 (5548) | 0.533 (606) | 0.752 (850) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.365 | 0.365 | 0.263 | 0.263 | 0.567 | 0.251 | 0.480 | 1.186 |
| 6h | 360 | 0.367 | 0.364 | 0.283 | 0.302 | 0.539 | 0.252 | 0.482 | 1.222 |
| 24h | 1440 | 0.386 | 0.377 | 0.296 | 0.332 | 0.552 | 0.273 | 0.499 | 1.137 |
| 7d | 10080 | 0.385 | 0.378 | 0.298 | 0.331 | 0.536 | 0.269 | 0.502 | 1.191 |
| 30d | 43200 | 0.373 | 0.367 | 0.287 | 0.319 | 0.531 | 0.266 | 0.481 | 1.262 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.365 / 0.567 / 0.883; 2: 0.317 / 0.417 / 0.967; 3: 0.371 / 0.633 / 0.983; 4: 0.357 / 0.533 / 1.000; 5: 0.319 / 0.517 / 1.000; 6: 0.348 / 0.500 / 1.000; 7: 0.331 / 0.467 / 0.967; 8: 0.363 / 0.550 / 0.967; 9: 0.341 / 0.467 / 1.000; 10: 0.355 / 0.517 / 1.000; 11: 0.364 / 0.533 / 1.000; 12: 0.367 / 0.550 / 1.000; 13: 0.332 / 0.400 / 1.000; 14: 0.349 / 0.483 / 1.000; 15: 0.326 / 0.467 / 1.000
- 6h: 1: 0.367 / 0.539 / 0.869; 2: 0.355 / 0.519 / 0.944; 3: 0.361 / 0.525 / 0.981; 4: 0.358 / 0.519 / 1.000; 5: 0.343 / 0.478 / 0.983; 6: 0.357 / 0.536 / 0.992; 7: 0.357 / 0.517 / 0.886; 8: 0.357 / 0.511 / 0.894; 9: 0.355 / 0.508 / 0.919; 10: 0.360 / 0.522 / 0.978; 11: 0.355 / 0.500 / 0.994; 12: 0.350 / 0.469 / 0.997; 13: 0.332 / 0.408 / 1.000; 14: 0.350 / 0.500 / 1.000; 15: 0.340 / 0.481 / 0.997
- 24h: 1: 0.386 / 0.552 / 0.888; 2: 0.365 / 0.488 / 0.900; 3: 0.375 / 0.519 / 0.908; 4: 0.363 / 0.497 / 0.895; 5: 0.370 / 0.495 / 0.916; 6: 0.361 / 0.485 / 0.915; 7: 0.373 / 0.518 / 0.910; 8: 0.368 / 0.502 / 0.908; 9: 0.367 / 0.503 / 0.912; 10: 0.370 / 0.516 / 0.922; 11: 0.368 / 0.508 / 0.912; 12: 0.369 / 0.502 / 0.910; 13: 0.358 / 0.465 / 0.912; 14: 0.370 / 0.514 / 0.924; 15: 0.361 / 0.491 / 0.918
- 7d: 1: 0.385 / 0.536 / 0.900; 2: 0.371 / 0.494 / 0.904; 3: 0.371 / 0.507 / 0.904; 4: 0.369 / 0.495 / 0.903; 5: 0.373 / 0.512 / 0.906; 6: 0.368 / 0.497 / 0.904; 7: 0.370 / 0.506 / 0.902; 8: 0.370 / 0.510 / 0.903; 9: 0.366 / 0.498 / 0.902; 10: 0.369 / 0.511 / 0.905; 11: 0.367 / 0.506 / 0.904; 12: 0.368 / 0.504 / 0.903; 13: 0.364 / 0.496 / 0.903; 14: 0.365 / 0.503 / 0.903; 15: 0.364 / 0.499 / 0.901
- 30d: 1: 0.373 / 0.531 / 0.898; 2: 0.360 / 0.491 / 0.900; 3: 0.364 / 0.511 / 0.900; 4: 0.360 / 0.497 / 0.900; 5: 0.361 / 0.506 / 0.900; 6: 0.358 / 0.502 / 0.900; 7: 0.359 / 0.501 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.358 / 0.501 / 0.900; 10: 0.359 / 0.504 / 0.900; 11: 0.358 / 0.506 / 0.900; 12: 0.358 / 0.503 / 0.900; 13: 0.357 / 0.499 / 0.900; 14: 0.357 / 0.502 / 0.900; 15: 0.356 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.093 (body 0.060, range 0.127); 'price stays where it was' would score 0.095; colour right 0.517; typical miss of the close 20.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.097 (body 0.054, range 0.139); 'price stays where it was' would score 0.112; colour right 0.464; typical miss of the close 20.1 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.131 (body 0.084, range 0.178); 'price stays where it was' would score 0.124; colour right 0.483; typical miss of the close 14.6 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.134 (body 0.087, range 0.180); 'price stays where it was' would score 0.139; colour right 0.503; typical miss of the close 13.9 bp; chain ended on the right side 0.524 of 672 chains; n=10080
- 30d: match 0.127 (body 0.084, range 0.169); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 10.7 bp; chain ended on the right side 0.516 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.7; 2: 0.207 / 6.5; 3: 0.167 / 8.4; 4: 0.136 / 8.8; 5: 0.126 / 9.6; 6: 0.119 / 10.3; 7: 0.116 / 10.9; 8: 0.100 / 11.8; 9: 0.092 / 12.3; 10: 0.089 / 12.8; 11: 0.087 / 13.3; 12: 0.081 / 13.4; 13: 0.074 / 14.3; 14: 0.070 / 14.6; 15: 0.067 / 15.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 162796, probability skill vs chance 0.2342, widened contest next: True
  - now: threshold 0.8291, hit rate recent 0.942 / long run 0.9338
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.321, naive rule 0.568, lift 3.11x
    - 24h: 55 calls (55 a day), hit rate 0.945, chance 0.301, naive rule 0.536, lift 3.14x
    - 7d: 389 calls (56 a day), hit rate 0.938, chance 0.296, naive rule 0.516, lift 3.17x
    - 30d: 1719 calls (57 a day), hit rate 0.931, chance 0.293, naive rule 0.503, lift 3.17x
  - next: threshold 0.5193, hit rate recent 0.553 / long run 0.594
    - 6h: 44 calls (178 a day), hit rate 0.568, chance 0.321, lift 1.77x
    - 24h: 153 calls (154 a day), hit rate 0.542, chance 0.301, lift 1.80x
    - 7d: 886 calls (127 a day), hit rate 0.588, chance 0.296, lift 1.98x
    - 30d: 2679 calls (89 a day), hit rate 0.598, chance 0.293, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 558, 0.503; 0.35: 529, 0.528; 0.40: 479, 0.573; 0.45: 415, 0.638; 0.50: 365, 0.683; 0.55: 317, 0.729; 0.60: 267, 0.775; 0.65: 225, 0.805; 0.70: 177, 0.835; 0.75: 142, 0.871; 0.80: 93, 0.903; 0.85: 43, 0.940; 0.90: 4, 0.962
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 488, 0.469; 0.40: 385, 0.509; 0.45: 291, 0.542; 0.50: 186, 0.573; 0.55: 78, 0.584; 0.60: 10, 0.639; 0.65: 0, 0.571
- **K=5**: model 1794528000, labels learned 162794, probability skill vs chance 0.2248, widened contest next: False
  - now: threshold 0.7003, hit rate recent 0.8089 / long run 0.795
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.180, naive rule 0.415, lift 4.63x
    - 24h: 52 calls (52 a day), hit rate 0.769, chance 0.185, naive rule 0.421, lift 4.16x
    - 7d: 409 calls (58 a day), hit rate 0.817, chance 0.194, naive rule 0.432, lift 4.20x
    - 30d: 1763 calls (59 a day), hit rate 0.795, chance 0.188, naive rule 0.414, lift 4.23x
  - next: threshold 0.4382, hit rate recent 0.4749 / long run 0.4981
    - 6h: 30 calls (122 a day), hit rate 0.467, chance 0.180, lift 2.59x
    - 24h: 78 calls (78 a day), hit rate 0.410, chance 0.185, lift 2.22x
    - 7d: 361 calls (52 a day), hit rate 0.479, chance 0.194, lift 2.47x
    - 30d: 1824 calls (61 a day), hit rate 0.508, chance 0.188, lift 2.71x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.424; 0.35: 363, 0.474; 0.40: 294, 0.542; 0.45: 238, 0.603; 0.50: 186, 0.653; 0.55: 150, 0.685; 0.60: 116, 0.732; 0.65: 83, 0.769; 0.70: 52, 0.803; 0.75: 27, 0.839; 0.80: 6, 0.846
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 334, 0.394; 0.35: 248, 0.432; 0.40: 158, 0.461; 0.45: 63, 0.508; 0.50: 8, 0.564; 0.55: 1, 0.471
- **K=8**: model 1794960000, labels learned 162791, probability skill vs chance 0.2096, widened contest next: True
  - now: threshold 0.5835, hit rate recent 0.6331 / long run 0.6673
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.130, naive rule 0.364, lift 4.81x
    - 24h: 56 calls (56 a day), hit rate 0.607, chance 0.121, naive rule 0.344, lift 5.02x
    - 7d: 424 calls (61 a day), hit rate 0.665, chance 0.124, naive rule 0.358, lift 5.36x
    - 30d: 1649 calls (55 a day), hit rate 0.678, chance 0.123, naive rule 0.348, lift 5.51x
  - next: threshold 0.3558, hit rate recent 0.4278 / long run 0.4188
    - 6h: 16 calls (66 a day), hit rate 0.562, chance 0.130, lift 4.33x
    - 24h: 74 calls (75 a day), hit rate 0.378, chance 0.121, lift 3.13x
    - 7d: 575 calls (82 a day), hit rate 0.416, chance 0.124, lift 3.35x
    - 30d: 2266 calls (76 a day), hit rate 0.417, chance 0.123, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 255, 0.427; 0.35: 202, 0.486; 0.40: 158, 0.535; 0.45: 121, 0.576; 0.50: 86, 0.634; 0.55: 63, 0.668; 0.60: 42, 0.707; 0.65: 24, 0.765; 0.70: 9, 0.802; 0.75: 1, 0.725
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 158, 0.376; 0.35: 83, 0.407; 0.40: 28, 0.444; 0.45: 6, 0.472; 0.50: 1, 0.656
- **K=13**: model 1795478400, labels learned 162786, probability skill vs chance 0.1926, widened contest next: True
  - now: threshold 0.4574, hit rate recent 0.5292 / long run 0.5682
    - 6h: 10 calls (42 a day), hit rate 0.500, chance 0.074, naive rule 0.263, lift 6.76x
    - 24h: 45 calls (45 a day), hit rate 0.467, chance 0.078, naive rule 0.294, lift 5.99x
    - 7d: 376 calls (54 a day), hit rate 0.551, chance 0.081, naive rule 0.306, lift 6.82x
    - 30d: 1622 calls (54 a day), hit rate 0.572, chance 0.080, naive rule 0.296, lift 7.19x
  - next: threshold 0.3046, hit rate recent 0.3937 / long run 0.3394
    - 6h: 7 calls (29 a day), hit rate 0.429, chance 0.074, lift 5.80x
    - 24h: 42 calls (42 a day), hit rate 0.333, chance 0.078, lift 4.28x
    - 7d: 443 calls (63 a day), hit rate 0.343, chance 0.081, lift 4.25x
    - 30d: 1821 calls (61 a day), hit rate 0.337, chance 0.080, lift 4.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 141, 0.423; 0.35: 104, 0.471; 0.40: 72, 0.532; 0.45: 50, 0.581; 0.50: 34, 0.620; 0.55: 21, 0.646; 0.60: 10, 0.667; 0.65: 2, 0.523; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.342; 0.35: 15, 0.385; 0.40: 2, 0.447; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 20.245 | 0.27% | 0.900 | 0.467 | 0.248 | 0.567 | 0.020 |
| 6h | 25.584 | 0.91% | 0.869 | 0.478 | 0.252 | 0.500 | 0.530 |
| 24h | 26.658 | 4.94% | 0.895 | 0.502 | 0.250 | 0.511 | 0.675 |
| 7d | 24.660 | 4.37% | 0.900 | 0.501 | 0.250 | 0.507 | 0.667 |
| 30d | 19.511 | 4.81% | 0.900 | 0.500 | 0.250 | 0.506 | 0.710 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 20.300 | 20.058 | 20.179 | 20.633 | 20.183 | 20.466 | 20.413 | 20.039 | 20.202 | 20.245 |
| 6h | 25.819 | 25.635 | 25.559 | 25.571 | 25.874 | 25.802 | 25.592 | 25.507 | 25.500 | 25.584 |
| 24h | 28.044 | 26.892 | 26.656 | 26.601 | 27.174 | 27.041 | 26.667 | 26.591 | 26.619 | 26.658 |
| 7d | 25.786 | 24.922 | 24.823 | 24.671 | 25.194 | 24.978 | 24.651 | 24.604 | 24.624 | 24.660 |
| 30d | 20.498 | 19.699 | 19.649 | 19.564 | 19.920 | 19.836 | 19.495 | 19.469 | 19.479 | 19.511 |

## Next candle

- candle starting 2026-11-24 05:22 UTC, last close 1704.72
- P(up) 0.5163, return quantiles (bp): {'05': -11.766, '10': -8.719, '25': -4.652, '40': -1.449, '50': 0.276, '60': 1.568, '75': 3.626, '90': 8.31, '95': 11.564}
- changepoint probability 0.0378, regime age 90.6 min
- agent weights: empirical 0.005, ewma 0.084, garch 0.176, har 0.210, bocpd 0.024, hmm 0.038, online_qr 0.186, lgbm 0.278

## Learning log

- 2026-11-22 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9215}, "hmm": {"sd_bp": [5.69, 10.58, 28.33], "stay": [0.985, 0.953, 0.874]}, "lgbm": {"challenger_loss": 0.24557, "champion_loss": 0.24554, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48129, "challengers": 1, "chance_loss": 0.60807, "widened": false, "champion_loss": 0.47918, "promoted": false}, "reversal_k5": {"challenger_loss": 0.381, "challengers": 1, "chance_loss": 0.49754, "widened": false, "champion_loss": 0.37986, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28291, "challengers": 1, "chance_loss": 0.38778, "widened": false, "champion_loss": 0.28187, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20591, "challengers": 1, "chance_loss": 0.29298, "widened": false, "champion_loss": 0.20541, "promoted": false}}
- 2026-11-22 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.9173}, "hmm": {"sd_bp": [5.55, 10.36, 28.43], "stay": [0.982, 0.95, 0.859]}}
- 2026-11-23 00:00 UTC: {"garch": {"alpha": 0.0752, "beta": 0.917}, "hmm": {"sd_bp": [5.28, 10.22, 28.39], "stay": [0.976, 0.946, 0.857]}, "lgbm": {"challenger_loss": 0.24364, "champion_loss": 0.24354, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.61601, "widened": false, "champion_loss": 0.4869, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38212, "challengers": 1, "chance_loss": 0.503, "widened": false, "champion_loss": 0.38113, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29091, "challengers": 1, "chance_loss": 0.3912, "widened": false, "champion_loss": 0.28935, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20987, "challengers": 1, "chance_loss": 0.29233, "widened": false, "champion_loss": 0.20927, "promoted": false}}
- 2026-11-23 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.9112}, "hmm": {"sd_bp": [5.07, 10.1, 28.28], "stay": [0.973, 0.946, 0.862]}}
- 2026-11-24 00:00 UTC: {"garch": {"alpha": 0.0886, "beta": 0.9021}, "hmm": {"sd_bp": [4.97, 10.02, 31.47], "stay": [0.968, 0.952, 0.875]}, "lgbm": {"challenger_loss": 0.25051, "champion_loss": 0.25047, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48498, "challengers": 3, "chance_loss": 0.6173, "widened": true, "champion_loss": 0.48458, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37971, "challengers": 1, "chance_loss": 0.49915, "widened": false, "champion_loss": 0.37928, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27848, "challengers": 3, "chance_loss": 0.37338, "widened": true, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20281, "challengers": 3, "chance_loss": 0.28057, "widened": true, "champion_loss": 0.20335, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.97, 10.02, 31.47], current probabilities: [0.866, 0.132, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-11-24 05:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.133, 'l_abs': 0.664, 'l_hi': 0.81, 'l_lo': 0.764, 'b05': 0.73, 'b25': 0.642, 'b75': 0.603, 'b95': 0.701}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.5], [1.3, 1.6], [1.3, 1.5], [1.3, 1.6], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.6], [1.3, 1.5], [1.3, 1.5], [1.3, 1.6], [1.3, 1.6], [1.3, 1.5]], 'cone_width': [1.343, 1.432, 2.625, 1.857, 1.997, 3.037, 3.253, 3.006, 2.215, 2.843, 3.036, 2.923, 2.488, 2.91]}
- calibration offsets (in sigma): {'05': -0.0295, '10': 0.001, '25': -0.0075, '40': 0.054, '50': 0.055, '60': 0.026, '75': -0.0525, '90': -0.021, '95': -0.0205}
