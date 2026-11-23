# ETH-USD 60s candle generator - report

- generated: 2026-11-23 01:10 UTC
- last closed candle: 2026-11-23 01:10 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.533 (672) [0.507, 0.558] | 0.517 (2879) [0.501, 0.533] | 0.515 (7865) [0.505, 0.526] | 0.518 (4893) [0.504, 0.532] | 0.500 (4) | 0.500 | flat +0.011 (noise 0.029) |
| colour_clear | 0.529 (780) | 0.546 (5561) [0.532, 0.561] | 0.541 (23786) [0.535, 0.547] | 0.526 (64534) [0.520, 0.531] | 0.543 (40296) [0.539, 0.548] | 0.535 (43) | 0.500 | flat +0.007 (noise 0.010) |
| colour_confident | 0.588 (272) | 0.576 (1351) [0.556, 0.593] | 0.574 (4578) [0.563, 0.584] | 0.586 (7502) [0.577, 0.595] | 0.586 (7502) [0.577, 0.595] | 0.444 (9) | 0.500 | flat +0.046 (noise 0.024) |
| colour_next | 0.532 (1435) | 0.530 (10047) [0.524, 0.536] | 0.530 (42899) [0.526, 0.534] | 0.519 (117224) [0.515, 0.522] | 0.530 (72875) [0.527, 0.533] | 0.529 (70) | 0.500 | flat +0.002 (noise 0.007) |
| colour_path | 0.499 (20090) | 0.503 (140658) [0.501, 0.505] | 0.502 (600586) [0.501, 0.503] | 0.501 (1641136) [0.500, 0.502] | 0.501 (1020250) [0.500, 0.502] | 0.512 (980) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.635 (96) | 0.615 (395) [0.584, 0.647] | 0.609 (1257) [0.594, 0.623] | 0.625 (1993) [0.610, 0.638] | 0.625 (1993) [0.610, 0.638] | 0.250 (4) | 0.500 | flat +0.036 (noise 0.054) |
| reversal_k13_next | 0.455 (44) | 0.326 (476) [0.286, 0.376] | 0.336 (1843) [0.318, 0.355] | 0.317 (5398) [0.307, 0.326] | 0.328 (3293) [0.317, 0.340] | - | 0.078 | flat -0.026 (noise 0.033) |
| reversal_k13_now | 0.577 (52) | 0.555 (373) [0.520, 0.595] | 0.577 (1628) [0.557, 0.596] | 0.574 (4228) [0.561, 0.586] | 0.570 (2756) [0.555, 0.586] | 0.667 (3) | 0.078 | flat -0.049 (noise 0.037) |
| reversal_k3_next | 0.657 (169) | 0.600 (797) [0.568, 0.628] | 0.604 (2553) [0.592, 0.617] | 0.591 (7061) [0.582, 0.599] | 0.593 (4621) [0.582, 0.603] | 0.500 (6) | 0.294 | flat -0.024 (noise 0.033) |
| reversal_k3_now | 0.950 (60) | 0.938 (388) [0.921, 0.956] | 0.931 (1718) [0.922, 0.941] | 0.935 (4692) [0.930, 0.941] | 0.931 (2929) [0.925, 0.938] | 1.000 (2) | 0.293 | flat +0.014 (noise 0.018) |
| reversal_k5_next | 0.639 (36) | 0.487 (355) [0.429, 0.558] | 0.512 (1890) [0.493, 0.531] | 0.487 (6071) [0.476, 0.498] | 0.483 (4081) [0.469, 0.498] | 0.000 (1) | 0.187 | flat -0.019 (noise 0.048) |
| reversal_k5_now | 0.864 (59) | 0.801 (418) [0.772, 0.828] | 0.796 (1761) [0.780, 0.812] | 0.817 (4477) [0.807, 0.826] | 0.805 (2866) [0.793, 0.816] | 1.000 (4) | 0.187 | flat +0.058 (noise 0.029) |
| reversal_k8_next | 0.467 (75) | 0.411 (569) [0.381, 0.446] | 0.417 (2285) [0.402, 0.434] | 0.399 (6386) [0.389, 0.409] | 0.400 (4280) [0.388, 0.412] | 0.667 (3) | 0.121 | flat -0.027 (noise 0.031) |
| reversal_k8_now | 0.656 (61) | 0.662 (423) [0.637, 0.684] | 0.682 (1645) [0.664, 0.700] | 0.694 (4329) [0.682, 0.707] | 0.683 (2742) [0.668, 0.697] | 0.667 (3) | 0.122 | flat -0.005 (noise 0.034) |
| overall | 0.505 (22177) | 0.507 (155176) [0.505, 0.509] | 0.506 (661687) [0.505, 0.507] | 0.504 (1808867) [0.503, 0.505] | 0.505 (1125586) [0.504, 0.506] | 0.517 (1076) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07507, 0.107] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5302, 'levels': [{'threshold': 0.07507, 'calls_per_day': 148.8, 'win_rate': 0.5809}, {'threshold': 0.107, 'calls_per_day': 38.0, 'win_rate': 0.603}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42898, 'rate': 0.5295}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14904 | 0.349 | 0.533 (14688) | 0.565 (2239) | 0.754 (2515) |
| volatility: normal | 14903 | 0.378 | 0.527 (14850) | 0.584 (1446) | 0.736 (2388) |
| volatility: wild | 14903 | 0.390 | 0.530 (14865) | 0.592 (1104) | 0.755 (2096) |
| session: Asia 00-08 | 14950 | 0.371 | 0.529 (14838) | 0.565 (1658) | 0.750 (2261) |
| session: Europe 08-13 | 9300 | 0.366 | 0.532 (9226) | 0.582 (1183) | 0.755 (1489) |
| session: US 13-21 | 14880 | 0.380 | 0.534 (14791) | 0.607 (1337) | 0.742 (2407) |
| session: late 21-24 | 5580 | 0.366 | 0.517 (5548) | 0.534 (611) | 0.748 (842) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.362 | 0.383 | 0.278 | 0.278 | 0.517 | 0.259 | 0.464 | 1.070 |
| 6h | 360 | 0.369 | 0.373 | 0.281 | 0.302 | 0.540 | 0.263 | 0.474 | 1.082 |
| 24h | 1440 | 0.370 | 0.371 | 0.269 | 0.293 | 0.530 | 0.256 | 0.485 | 1.241 |
| 7d | 10080 | 0.384 | 0.377 | 0.300 | 0.334 | 0.530 | 0.266 | 0.502 | 1.195 |
| 30d | 43200 | 0.372 | 0.366 | 0.286 | 0.317 | 0.530 | 0.265 | 0.479 | 1.266 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.362 / 0.517 / 0.767; 2: 0.331 / 0.417 / 0.867; 3: 0.358 / 0.517 / 0.883; 4: 0.326 / 0.483 / 0.767; 5: 0.380 / 0.617 / 0.750; 6: 0.353 / 0.483 / 0.750; 7: 0.373 / 0.583 / 0.750; 8: 0.361 / 0.533 / 0.783; 9: 0.324 / 0.450 / 0.783; 10: 0.329 / 0.483 / 0.800; 11: 0.339 / 0.500 / 0.883; 12: 0.354 / 0.533 / 0.850; 13: 0.355 / 0.567 / 0.850; 14: 0.349 / 0.550 / 0.833; 15: 0.328 / 0.450 / 0.867
- 6h: 1: 0.369 / 0.540 / 0.872; 2: 0.347 / 0.474 / 0.867; 3: 0.350 / 0.507 / 0.864; 4: 0.350 / 0.482 / 0.817; 5: 0.364 / 0.571 / 0.786; 6: 0.346 / 0.465 / 0.792; 7: 0.354 / 0.535 / 0.764; 8: 0.344 / 0.482 / 0.772; 9: 0.353 / 0.515 / 0.775; 10: 0.352 / 0.535 / 0.775; 11: 0.353 / 0.515 / 0.803; 12: 0.353 / 0.515 / 0.803; 13: 0.352 / 0.515 / 0.825; 14: 0.340 / 0.487 / 0.797; 15: 0.336 / 0.468 / 0.811
- 24h: 1: 0.370 / 0.530 / 0.892; 2: 0.352 / 0.472 / 0.898; 3: 0.359 / 0.511 / 0.892; 4: 0.351 / 0.483 / 0.880; 5: 0.360 / 0.517 / 0.875; 6: 0.353 / 0.493 / 0.876; 7: 0.350 / 0.503 / 0.867; 8: 0.356 / 0.517 / 0.864; 9: 0.351 / 0.486 / 0.861; 10: 0.352 / 0.508 / 0.865; 11: 0.352 / 0.506 / 0.874; 12: 0.353 / 0.509 / 0.876; 13: 0.349 / 0.499 / 0.875; 14: 0.348 / 0.508 / 0.866; 15: 0.345 / 0.492 / 0.869
- 7d: 1: 0.384 / 0.530 / 0.900; 2: 0.372 / 0.493 / 0.900; 3: 0.373 / 0.506 / 0.900; 4: 0.370 / 0.496 / 0.899; 5: 0.374 / 0.510 / 0.898; 6: 0.370 / 0.502 / 0.899; 7: 0.370 / 0.505 / 0.898; 8: 0.372 / 0.511 / 0.898; 9: 0.367 / 0.496 / 0.898; 10: 0.370 / 0.510 / 0.898; 11: 0.369 / 0.506 / 0.899; 12: 0.369 / 0.505 / 0.900; 13: 0.367 / 0.503 / 0.900; 14: 0.367 / 0.501 / 0.899; 15: 0.366 / 0.498 / 0.900
- 30d: 1: 0.372 / 0.530 / 0.898; 2: 0.359 / 0.491 / 0.900; 3: 0.363 / 0.511 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.501 / 0.900; 8: 0.358 / 0.507 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.358 / 0.504 / 0.900; 11: 0.357 / 0.506 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.502 / 0.900; 14: 0.356 / 0.502 / 0.900; 15: 0.356 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.102 (body 0.063, range 0.141); 'price stays where it was' would score 0.131; colour right 0.633; typical miss of the close 14.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.104 (body 0.063, range 0.146); 'price stays where it was' would score 0.123; colour right 0.479; typical miss of the close 9.7 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.126 (body 0.079, range 0.174); 'price stays where it was' would score 0.138; colour right 0.477; typical miss of the close 11.0 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.132 (body 0.086, range 0.179); 'price stays where it was' would score 0.139; colour right 0.506; typical miss of the close 13.8 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.169); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 10.3 bp; chain ended on the right side 0.517 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 5.5; 2: 0.205 / 6.2; 3: 0.168 / 8.1; 4: 0.135 / 8.6; 5: 0.126 / 9.2; 6: 0.120 / 9.9; 7: 0.116 / 10.4; 8: 0.101 / 11.4; 9: 0.092 / 12.0; 10: 0.090 / 12.5; 11: 0.087 / 12.9; 12: 0.081 / 13.0; 13: 0.074 / 13.8; 14: 0.069 / 14.1; 15: 0.067 / 14.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 161104, probability skill vs chance 0.2381, widened contest next: False
  - now: threshold 0.8297, hit rate recent 0.9372 / long run 0.9321
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.299, naive rule 0.517, lift 2.93x
    - 24h: 58 calls (58 a day), hit rate 0.948, chance 0.314, naive rule 0.571, lift 3.02x
    - 7d: 387 calls (55 a day), hit rate 0.941, chance 0.295, naive rule 0.512, lift 3.19x
    - 30d: 1719 calls (57 a day), hit rate 0.931, chance 0.294, naive rule 0.503, lift 3.17x
  - next: threshold 0.5113, hit rate recent 0.6373 / long run 0.6129
    - 6h: 33 calls (134 a day), hit rate 0.606, chance 0.299, lift 2.03x
    - 24h: 168 calls (169 a day), hit rate 0.649, chance 0.314, lift 2.07x
    - 7d: 799 calls (114 a day), hit rate 0.599, chance 0.295, lift 2.03x
    - 30d: 2557 calls (85 a day), hit rate 0.604, chance 0.294, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 558, 0.504; 0.35: 529, 0.528; 0.40: 478, 0.575; 0.45: 413, 0.641; 0.50: 363, 0.686; 0.55: 315, 0.732; 0.60: 265, 0.777; 0.65: 223, 0.807; 0.70: 176, 0.837; 0.75: 141, 0.872; 0.80: 93, 0.904; 0.85: 43, 0.939; 0.90: 4, 0.963
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.435; 0.35: 490, 0.468; 0.40: 387, 0.508; 0.45: 291, 0.543; 0.50: 186, 0.577; 0.55: 79, 0.587; 0.60: 10, 0.635; 0.65: 0, 0.533
- **K=5**: model 1794528000, labels learned 161102, probability skill vs chance 0.2326, widened contest next: False
  - now: threshold 0.6996, hit rate recent 0.8406 / long run 0.7952
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.197, naive rule 0.458, lift 4.48x
    - 24h: 60 calls (60 a day), hit rate 0.867, chance 0.205, naive rule 0.493, lift 4.22x
    - 7d: 417 calls (60 a day), hit rate 0.806, chance 0.194, naive rule 0.429, lift 4.16x
    - 30d: 1765 calls (59 a day), hit rate 0.797, chance 0.188, naive rule 0.414, lift 4.24x
  - next: threshold 0.4605, hit rate recent 0.599 / long run 0.5077
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.197, lift 2.73x
    - 24h: 37 calls (37 a day), hit rate 0.622, chance 0.205, lift 3.03x
    - 7d: 352 calls (50 a day), hit rate 0.489, chance 0.194, lift 2.52x
    - 30d: 1885 calls (63 a day), hit rate 0.512, chance 0.188, lift 2.73x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.424; 0.35: 361, 0.476; 0.40: 293, 0.543; 0.45: 237, 0.604; 0.50: 186, 0.655; 0.55: 149, 0.688; 0.60: 115, 0.734; 0.65: 83, 0.772; 0.70: 51, 0.806; 0.75: 27, 0.839; 0.80: 6, 0.852
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 335, 0.393; 0.35: 249, 0.433; 0.40: 159, 0.465; 0.45: 64, 0.507; 0.50: 8, 0.558; 0.55: 1, 0.471
- **K=8**: model 1794960000, labels learned 161099, probability skill vs chance 0.2143, widened contest next: False
  - now: threshold 0.5813, hit rate recent 0.6714 / long run 0.6728
    - 6h: 20 calls (82 a day), hit rate 0.700, chance 0.129, naive rule 0.407, lift 5.44x
    - 24h: 61 calls (61 a day), hit rate 0.656, chance 0.127, naive rule 0.388, lift 5.17x
    - 7d: 422 calls (60 a day), hit rate 0.664, chance 0.125, naive rule 0.357, lift 5.32x
    - 30d: 1648 calls (55 a day), hit rate 0.682, chance 0.123, naive rule 0.348, lift 5.54x
  - next: threshold 0.3532, hit rate recent 0.4958 / long run 0.425
    - 6h: 17 calls (70 a day), hit rate 0.647, chance 0.129, lift 5.03x
    - 24h: 78 calls (79 a day), hit rate 0.474, chance 0.127, lift 3.74x
    - 7d: 568 calls (81 a day), hit rate 0.414, chance 0.125, lift 3.31x
    - 30d: 2282 calls (76 a day), hit rate 0.418, chance 0.123, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.430; 0.35: 199, 0.489; 0.40: 157, 0.538; 0.45: 120, 0.580; 0.50: 86, 0.639; 0.55: 62, 0.675; 0.60: 41, 0.712; 0.65: 24, 0.763; 0.70: 9, 0.804; 0.75: 1, 0.732
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 160, 0.377; 0.35: 83, 0.408; 0.40: 27, 0.442; 0.45: 6, 0.468; 0.50: 1, 0.667
- **K=13**: model 1795132800, labels learned 161094, probability skill vs chance 0.2001, widened contest next: False
  - now: threshold 0.4552, hit rate recent 0.6037 / long run 0.5755
    - 6h: 15 calls (63 a day), hit rate 0.667, chance 0.084, naive rule 0.367, lift 7.93x
    - 24h: 53 calls (54 a day), hit rate 0.566, chance 0.084, naive rule 0.360, lift 6.78x
    - 7d: 374 calls (54 a day), hit rate 0.556, chance 0.081, naive rule 0.301, lift 6.89x
    - 30d: 1631 calls (54 a day), hit rate 0.577, chance 0.079, naive rule 0.295, lift 7.27x
  - next: threshold 0.3063, hit rate recent 0.4459 / long run 0.3397
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.084, lift 6.94x
    - 24h: 44 calls (44 a day), hit rate 0.455, chance 0.084, lift 5.44x
    - 7d: 471 calls (67 a day), hit rate 0.329, chance 0.081, lift 4.07x
    - 30d: 1840 calls (61 a day), hit rate 0.336, chance 0.079, lift 4.24x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 140, 0.426; 0.35: 102, 0.476; 0.40: 71, 0.537; 0.45: 50, 0.587; 0.50: 34, 0.623; 0.55: 21, 0.649; 0.60: 10, 0.677; 0.65: 2, 0.537; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.345; 0.35: 15, 0.381; 0.40: 3, 0.429; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 24.416 | 2.02% | 0.750 | 0.467 | 0.246 | 0.600 | 0.239 |
| 6h | 16.197 | 3.19% | 0.869 | 0.458 | 0.248 | 0.540 | 0.567 |
| 24h | 19.678 | 2.69% | 0.885 | 0.499 | 0.249 | 0.527 | 0.507 |
| 7d | 23.859 | 3.99% | 0.899 | 0.501 | 0.250 | 0.502 | 0.666 |
| 30d | 18.939 | 4.85% | 0.900 | 0.500 | 0.250 | 0.505 | 0.715 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 24.920 | 24.872 | 24.858 | 24.481 | 24.499 | 24.565 | 23.918 | 24.211 | 24.190 | 24.416 |
| 6h | 16.731 | 16.403 | 16.364 | 16.195 | 16.647 | 16.713 | 16.060 | 16.122 | 16.129 | 16.197 |
| 24h | 20.221 | 19.968 | 19.860 | 19.700 | 20.315 | 19.993 | 19.617 | 19.627 | 19.643 | 19.678 |
| 7d | 24.849 | 24.089 | 24.021 | 23.872 | 24.360 | 24.148 | 23.846 | 23.810 | 23.822 | 23.859 |
| 30d | 19.905 | 19.125 | 19.079 | 18.997 | 19.335 | 19.259 | 18.924 | 18.898 | 18.908 | 18.939 |

## Next candle

- candle starting 2026-11-23 01:10 UTC, last close 1709.04
- P(up) 0.5412, return quantiles (bp): {'05': -15.318, '10': -11.758, '25': -5.109, '40': -1.382, '50': 0.945, '60': 2.857, '75': 6.097, '90': 10.926, '95': 13.856}
- changepoint probability 0.0391, regime age 119.6 min
- agent weights: empirical 0.012, ewma 0.052, garch 0.072, har 0.181, bocpd 0.011, hmm 0.027, online_qr 0.362, lgbm 0.282

## Learning log

- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- 2026-11-22 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9215}, "hmm": {"sd_bp": [5.69, 10.58, 28.33], "stay": [0.985, 0.953, 0.874]}, "lgbm": {"challenger_loss": 0.24557, "champion_loss": 0.24554, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48129, "challengers": 1, "chance_loss": 0.60807, "widened": false, "champion_loss": 0.47918, "promoted": false}, "reversal_k5": {"challenger_loss": 0.381, "challengers": 1, "chance_loss": 0.49754, "widened": false, "champion_loss": 0.37986, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28291, "challengers": 1, "chance_loss": 0.38778, "widened": false, "champion_loss": 0.28187, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20591, "challengers": 1, "chance_loss": 0.29298, "widened": false, "champion_loss": 0.20541, "promoted": false}}
- 2026-11-22 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.9173}, "hmm": {"sd_bp": [5.55, 10.36, 28.43], "stay": [0.982, 0.95, 0.859]}}
- 2026-11-23 00:00 UTC: {"garch": {"alpha": 0.0752, "beta": 0.917}, "hmm": {"sd_bp": [5.28, 10.22, 28.39], "stay": [0.976, 0.946, 0.857]}, "lgbm": {"challenger_loss": 0.24364, "champion_loss": 0.24354, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.61601, "widened": false, "champion_loss": 0.4869, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38212, "challengers": 1, "chance_loss": 0.503, "widened": false, "champion_loss": 0.38113, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29091, "challengers": 1, "chance_loss": 0.3912, "widened": false, "champion_loss": 0.28935, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20987, "challengers": 1, "chance_loss": 0.29233, "widened": false, "champion_loss": 0.20927, "promoted": false}}
- HMM volatility states (sd, bp per minute): [5.28, 10.22, 28.39], current probabilities: [0.031, 0.935, 0.033]
- live generator: {'versions': 60, 'latest_effective': '2026-11-23 01:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.406, 'l_abs': 0.789, 'l_hi': 0.8, 'l_lo': 0.767, 'b05': 0.781, 'b25': 0.79, 'b75': 0.73, 'b95': 0.758}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [1.55, 1.941, 3.032, 3.986, 4.288, 5.446, 5.834, 6.2, 6.292, 5.635, 5.666, 5.347, 6.395, 6.123]}
- calibration offsets (in sigma): {'05': 0.0345, '10': -0.011, '25': 0.0325, '40': 0.016, '50': 0.025, '60': -0.006, '75': -0.0125, '90': -0.029, '95': -0.0345}
