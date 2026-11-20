# ETH-USD 60s candle generator - report

- generated: 2026-11-20 23:10 UTC
- last closed candle: 2026-11-20 23:10 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.525 (672) [0.495, 0.552] | 0.517 (2879) [0.502, 0.534] | 0.515 (7577) [0.505, 0.526] | 0.518 (4605) [0.503, 0.532] | 0.587 (92) | 0.500 | flat -0.002 (noise 0.027) |
| colour_clear | 0.537 (831) | 0.546 (5673) [0.536, 0.558] | 0.540 (23966) [0.534, 0.546] | 0.525 (62227) [0.520, 0.530] | 0.543 (37989) [0.539, 0.547] | 0.578 (801) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | 0.576 (151) | 0.556 (1085) [0.531, 0.583] | 0.577 (4499) [0.565, 0.589] | 0.586 (6910) [0.576, 0.596] | 0.586 (6910) [0.576, 0.596] | 0.562 (96) | 0.500 | flat -0.013 (noise 0.023) |
| colour_next | 0.535 (1436) | 0.533 (10046) [0.527, 0.539] | 0.530 (42892) [0.526, 0.534] | 0.518 (112914) [0.515, 0.522] | 0.530 (68565) [0.527, 0.533] | 0.544 (1389) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.499 (20104) | 0.502 (140644) [0.500, 0.504] | 0.502 (600488) [0.501, 0.503] | 0.501 (1580796) [0.500, 0.502] | 0.501 (959910) [0.500, 0.502] | 0.510 (19446) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.676 (34) | 0.606 (289) [0.570, 0.650] | 0.613 (1184) [0.596, 0.629] | 0.625 (1813) [0.610, 0.641] | 0.625 (1813) [0.610, 0.641] | 0.643 (14) | 0.500 | flat -0.017 (noise 0.042) |
| reversal_k13_next | 0.275 (91) | 0.300 (487) [0.271, 0.339] | 0.325 (1870) [0.309, 0.343] | 0.314 (5247) [0.304, 0.323] | 0.323 (3142) [0.312, 0.334] | 0.351 (57) | 0.077 | flat -0.035 (noise 0.030) |
| reversal_k13_now | 0.515 (68) | 0.560 (384) [0.513, 0.618] | 0.570 (1627) [0.549, 0.592] | 0.572 (4084) [0.560, 0.584] | 0.567 (2612) [0.551, 0.584] | 0.628 (43) | 0.077 | flat -0.019 (noise 0.037) |
| reversal_k3_next | 0.544 (79) | 0.595 (407) [0.567, 0.637] | 0.604 (2365) [0.593, 0.617] | 0.589 (6568) [0.580, 0.597] | 0.589 (4128) [0.579, 0.600] | 0.563 (158) | 0.293 | flat -0.014 (noise 0.035) |
| reversal_k3_now | 0.894 (66) | 0.941 (375) [0.924, 0.959] | 0.933 (1727) [0.924, 0.944] | 0.935 (4521) [0.930, 0.941] | 0.931 (2758) [0.924, 0.939] | 0.921 (63) | 0.293 | flat +0.023 (noise 0.018) |
| reversal_k5_next | 0.407 (54) | 0.475 (425) [0.422, 0.534] | 0.503 (2167) [0.488, 0.518] | 0.484 (5956) [0.473, 0.495] | 0.479 (3966) [0.465, 0.492] | 0.543 (46) | 0.187 | flat -0.024 (noise 0.039) |
| reversal_k5_now | 0.831 (65) | 0.775 (441) [0.748, 0.803] | 0.794 (1740) [0.777, 0.809] | 0.816 (4303) [0.806, 0.826] | 0.804 (2692) [0.792, 0.816] | 0.825 (63) | 0.187 | flat +0.015 (noise 0.032) |
| reversal_k8_next | 0.405 (89) | 0.395 (511) [0.365, 0.440] | 0.409 (2379) [0.394, 0.424] | 0.397 (6149) [0.387, 0.406] | 0.397 (4043) [0.385, 0.408] | 0.386 (83) | 0.121 | flat -0.024 (noise 0.031) |
| reversal_k8_now | 0.690 (71) | 0.659 (419) [0.617, 0.705] | 0.682 (1617) [0.663, 0.702] | 0.695 (4159) [0.683, 0.707] | 0.683 (2572) [0.668, 0.699] | 0.702 (57) | 0.122 | flat -0.024 (noise 0.034) |
| overall | 0.503 (22219) | 0.506 (154811) [0.504, 0.507] | 0.506 (661751) [0.505, 0.507] | 0.504 (1742274) [0.503, 0.505] | 0.505 (1058993) [0.504, 0.506] | 0.515 (21497) | - | flat +0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06948, 0.09992] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5348, 'levels': [{'threshold': 0.06948, 'calls_per_day': 144.7, 'win_rate': 0.5561}, {'threshold': 0.09992, 'calls_per_day': 35.8, 'win_rate': 0.6255}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42896, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15344 | 0.349 | 0.533 (15129) | 0.566 (2288) | 0.750 (2543) |
| volatility: normal | 15343 | 0.377 | 0.528 (15286) | 0.595 (1416) | 0.740 (2416) |
| volatility: wild | 15343 | 0.391 | 0.532 (15305) | 0.576 (1100) | 0.759 (2178) |
| session: Asia 00-08 | 15360 | 0.371 | 0.533 (15250) | 0.571 (1652) | 0.748 (2303) |
| session: Europe 08-13 | 9600 | 0.366 | 0.531 (9524) | 0.585 (1192) | 0.757 (1563) |
| session: US 13-21 | 15360 | 0.380 | 0.533 (15270) | 0.597 (1340) | 0.746 (2438) |
| session: late 21-24 | 5710 | 0.366 | 0.519 (5676) | 0.534 (620) | 0.749 (833) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.425 | 0.336 | 0.358 | 0.358 | 0.600 | 0.366 | 0.484 | 1.222 |
| 6h | 360 | 0.407 | 0.384 | 0.335 | 0.368 | 0.560 | 0.295 | 0.520 | 1.284 |
| 24h | 1440 | 0.401 | 0.388 | 0.320 | 0.355 | 0.549 | 0.283 | 0.519 | 1.193 |
| 7d | 10080 | 0.388 | 0.379 | 0.304 | 0.340 | 0.535 | 0.272 | 0.505 | 1.183 |
| 30d | 43200 | 0.372 | 0.365 | 0.286 | 0.317 | 0.530 | 0.266 | 0.478 | 1.260 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.425 / 0.600 / 0.933; 2: 0.373 / 0.450 / 1.000; 3: 0.367 / 0.467 / 1.000; 4: 0.377 / 0.533 / 0.983; 5: 0.369 / 0.567 / 0.983; 6: 0.390 / 0.600 / 0.950; 7: 0.364 / 0.433 / 1.000; 8: 0.358 / 0.433 / 1.000; 9: 0.352 / 0.417 / 1.000; 10: 0.370 / 0.500 / 1.000; 11: 0.346 / 0.483 / 1.000; 12: 0.367 / 0.533 / 1.000; 13: 0.375 / 0.500 / 1.000; 14: 0.358 / 0.517 / 1.000; 15: 0.385 / 0.533 / 1.000
- 6h: 1: 0.407 / 0.560 / 0.903; 2: 0.390 / 0.518 / 0.983; 3: 0.388 / 0.515 / 0.994; 4: 0.391 / 0.518 / 0.969; 5: 0.384 / 0.487 / 0.969; 6: 0.390 / 0.501 / 0.875; 7: 0.384 / 0.496 / 0.992; 8: 0.379 / 0.496 / 0.994; 9: 0.389 / 0.540 / 0.994; 10: 0.387 / 0.526 / 0.986; 11: 0.382 / 0.493 / 0.964; 12: 0.384 / 0.499 / 0.942; 13: 0.373 / 0.476 / 0.950; 14: 0.384 / 0.501 / 0.986; 15: 0.395 / 0.546 / 0.983
- 24h: 1: 0.401 / 0.549 / 0.893; 2: 0.389 / 0.523 / 0.909; 3: 0.386 / 0.513 / 0.881; 4: 0.386 / 0.500 / 0.902; 5: 0.391 / 0.527 / 0.909; 6: 0.384 / 0.498 / 0.893; 7: 0.379 / 0.491 / 0.914; 8: 0.382 / 0.502 / 0.909; 9: 0.384 / 0.511 / 0.913; 10: 0.387 / 0.528 / 0.928; 11: 0.381 / 0.504 / 0.940; 12: 0.383 / 0.502 / 0.906; 13: 0.383 / 0.517 / 0.901; 14: 0.376 / 0.492 / 0.914; 15: 0.383 / 0.511 / 0.910
- 7d: 1: 0.388 / 0.535 / 0.900; 2: 0.375 / 0.494 / 0.900; 3: 0.379 / 0.513 / 0.898; 4: 0.374 / 0.493 / 0.900; 5: 0.377 / 0.508 / 0.901; 6: 0.375 / 0.504 / 0.899; 7: 0.374 / 0.504 / 0.900; 8: 0.376 / 0.511 / 0.899; 9: 0.370 / 0.494 / 0.900; 10: 0.375 / 0.511 / 0.900; 11: 0.373 / 0.502 / 0.901; 12: 0.374 / 0.506 / 0.902; 13: 0.372 / 0.503 / 0.902; 14: 0.372 / 0.502 / 0.903; 15: 0.370 / 0.498 / 0.903
- 30d: 1: 0.372 / 0.530 / 0.897; 2: 0.359 / 0.493 / 0.900; 3: 0.363 / 0.512 / 0.899; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.500 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.357 / 0.503 / 0.900; 11: 0.357 / 0.505 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.500 / 0.900; 14: 0.356 / 0.501 / 0.900; 15: 0.356 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.161 (body 0.119, range 0.203); 'price stays where it was' would score 0.144; colour right 0.567; typical miss of the close 12.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.131 (body 0.088, range 0.174); 'price stays where it was' would score 0.142; colour right 0.529; typical miss of the close 28.5 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.136 (body 0.089, range 0.182); 'price stays where it was' would score 0.152; colour right 0.517; typical miss of the close 19.4 bp; chain ended on the right side 0.594 of 96 chains; n=1440
- 7d: match 0.129 (body 0.084, range 0.175); 'price stays where it was' would score 0.134; colour right 0.505; typical miss of the close 15.3 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 10.1 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.4; 2: 0.205 / 6.1; 3: 0.168 / 8.0; 4: 0.135 / 8.3; 5: 0.127 / 9.0; 6: 0.121 / 9.7; 7: 0.114 / 10.3; 8: 0.100 / 11.3; 9: 0.092 / 11.6; 10: 0.089 / 12.3; 11: 0.086 / 12.7; 12: 0.078 / 12.8; 13: 0.073 / 13.5; 14: 0.067 / 14.0; 15: 0.066 / 14.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 158104, probability skill vs chance 0.2335, widened contest next: False
  - now: threshold 0.8314, hit rate recent 0.9161 / long run 0.9294
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.308, naive rule 0.537, lift 3.04x
    - 24h: 65 calls (65 a day), hit rate 0.908, chance 0.296, naive rule 0.494, lift 3.06x
    - 7d: 382 calls (55 a day), hit rate 0.937, chance 0.291, naive rule 0.503, lift 3.22x
    - 30d: 1728 calls (58 a day), hit rate 0.931, chance 0.293, naive rule 0.500, lift 3.18x
  - next: threshold 0.5082, hit rate recent 0.5731 / long run 0.5896
    - 6h: 44 calls (178 a day), hit rate 0.636, chance 0.308, lift 2.06x
    - 24h: 163 calls (164 a day), hit rate 0.571, chance 0.296, lift 1.93x
    - 7d: 524 calls (75 a day), hit rate 0.578, chance 0.291, lift 1.99x
    - 30d: 2381 calls (79 a day), hit rate 0.598, chance 0.293, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.502; 0.35: 530, 0.526; 0.40: 477, 0.575; 0.45: 412, 0.641; 0.50: 363, 0.686; 0.55: 315, 0.731; 0.60: 265, 0.778; 0.65: 223, 0.807; 0.70: 175, 0.839; 0.75: 141, 0.872; 0.80: 93, 0.904; 0.85: 44, 0.939; 0.90: 4, 0.967
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 490, 0.468; 0.40: 388, 0.509; 0.45: 293, 0.543; 0.50: 188, 0.574; 0.55: 81, 0.584; 0.60: 11, 0.636; 0.65: 1, 0.529
- **K=5**: model 1794528000, labels learned 158102, probability skill vs chance 0.2146, widened contest next: False
  - now: threshold 0.7003, hit rate recent 0.8102 / long run 0.7882
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.217, naive rule 0.461, lift 4.33x
    - 24h: 65 calls (65 a day), hit rate 0.815, chance 0.198, naive rule 0.423, lift 4.12x
    - 7d: 435 calls (62 a day), hit rate 0.793, chance 0.189, naive rule 0.417, lift 4.20x
    - 30d: 1752 calls (58 a day), hit rate 0.795, chance 0.187, naive rule 0.410, lift 4.26x
  - next: threshold 0.463, hit rate recent 0.4857 / long run 0.4877
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.217, lift 2.94x
    - 24h: 48 calls (48 a day), hit rate 0.562, chance 0.198, lift 2.84x
    - 7d: 397 calls (57 a day), hit rate 0.474, chance 0.189, lift 2.51x
    - 30d: 2090 calls (70 a day), hit rate 0.505, chance 0.187, lift 2.71x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 362, 0.473; 0.40: 294, 0.540; 0.45: 238, 0.601; 0.50: 187, 0.652; 0.55: 150, 0.686; 0.60: 114, 0.733; 0.65: 81, 0.770; 0.70: 50, 0.806; 0.75: 27, 0.841; 0.80: 7, 0.863
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.390; 0.35: 252, 0.430; 0.40: 161, 0.459; 0.45: 65, 0.497; 0.50: 8, 0.550; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 158099, probability skill vs chance 0.2075, widened contest next: False
  - now: threshold 0.5773, hit rate recent 0.682 / long run 0.6763
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.124, naive rule 0.368, lift 6.19x
    - 24h: 58 calls (58 a day), hit rate 0.707, chance 0.126, naive rule 0.367, lift 5.62x
    - 7d: 414 calls (59 a day), hit rate 0.674, chance 0.122, naive rule 0.350, lift 5.51x
    - 30d: 1627 calls (54 a day), hit rate 0.682, chance 0.122, naive rule 0.343, lift 5.59x
  - next: threshold 0.3527, hit rate recent 0.3889 / long run 0.4035
    - 6h: 21 calls (86 a day), hit rate 0.381, chance 0.124, lift 3.07x
    - 24h: 85 calls (86 a day), hit rate 0.400, chance 0.126, lift 3.18x
    - 7d: 539 calls (77 a day), hit rate 0.397, chance 0.122, lift 3.25x
    - 30d: 2362 calls (79 a day), hit rate 0.408, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.424; 0.35: 199, 0.484; 0.40: 157, 0.534; 0.45: 120, 0.578; 0.50: 85, 0.636; 0.55: 61, 0.673; 0.60: 41, 0.714; 0.65: 23, 0.775; 0.70: 9, 0.819; 0.75: 2, 0.755
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 163, 0.373; 0.35: 85, 0.399; 0.40: 26, 0.430; 0.45: 6, 0.463; 0.50: 1, 0.704
- **K=13**: model 1795132800, labels learned 158094, probability skill vs chance 0.1852, widened contest next: False
  - now: threshold 0.4526, hit rate recent 0.5646 / long run 0.568
    - 6h: 10 calls (42 a day), hit rate 0.800, chance 0.083, naive rule 0.319, lift 9.68x
    - 24h: 44 calls (44 a day), hit rate 0.636, chance 0.084, naive rule 0.312, lift 7.56x
    - 7d: 369 calls (53 a day), hit rate 0.575, chance 0.080, naive rule 0.297, lift 7.21x
    - 30d: 1624 calls (54 a day), hit rate 0.571, chance 0.079, naive rule 0.290, lift 7.27x
  - next: threshold 0.3054, hit rate recent 0.3208 / long run 0.3178
    - 6h: 10 calls (42 a day), hit rate 0.300, chance 0.083, lift 3.63x
    - 24h: 58 calls (59 a day), hit rate 0.362, chance 0.084, lift 4.30x
    - 7d: 492 calls (70 a day), hit rate 0.309, chance 0.080, lift 3.88x
    - 30d: 1869 calls (62 a day), hit rate 0.326, chance 0.079, lift 4.14x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 139, 0.423; 0.35: 101, 0.472; 0.40: 70, 0.533; 0.45: 48, 0.583; 0.50: 34, 0.623; 0.55: 21, 0.647; 0.60: 10, 0.686; 0.65: 2, 0.603; 0.70: 0, 0.333
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.335; 0.35: 15, 0.361; 0.40: 2, 0.425; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.590 | 0.08% | 0.933 | 0.467 | 0.253 | 0.367 | 0.107 |
| 6h | 40.931 | 2.80% | 0.911 | 0.514 | 0.250 | 0.499 | 0.483 |
| 24h | 32.351 | 3.59% | 0.894 | 0.498 | 0.250 | 0.511 | 0.674 |
| 7d | 25.597 | 3.93% | 0.899 | 0.501 | 0.250 | 0.500 | 0.679 |
| 30d | 18.366 | 4.63% | 0.900 | 0.500 | 0.250 | 0.505 | 0.720 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 25.610 | 25.908 | 25.451 | 25.743 | 25.641 | 25.316 | 25.495 | 25.479 | 25.475 | 25.590 |
| 6h | 42.111 | 41.138 | 41.107 | 40.902 | 41.298 | 41.284 | 40.829 | 40.762 | 40.783 | 40.931 |
| 24h | 33.554 | 32.516 | 32.497 | 32.334 | 32.738 | 32.649 | 32.379 | 32.298 | 32.300 | 32.351 |
| 7d | 26.644 | 25.755 | 25.732 | 25.613 | 26.073 | 25.870 | 25.576 | 25.547 | 25.552 | 25.597 |
| 30d | 19.258 | 18.529 | 18.489 | 18.419 | 18.722 | 18.662 | 18.347 | 18.327 | 18.334 | 18.366 |

## Next candle

- candle starting 2026-11-20 23:10 UTC, last close 1620.78
- P(up) 0.4919, return quantiles (bp): {'05': -16.727, '10': -12.334, '25': -6.272, '40': -2.572, '50': -0.205, '60': 2.345, '75': 5.941, '90': 11.343, '95': 15.855}
- changepoint probability 0.045, regime age 64.6 min
- agent weights: empirical 0.003, ewma 0.070, garch 0.090, har 0.229, bocpd 0.041, hmm 0.050, online_qr 0.205, lgbm 0.312

## Learning log

- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- HMM volatility states (sd, bp per minute): [5.82, 9.8, 20.43], current probabilities: [0.34, 0.645, 0.014]
- live generator: {'versions': 60, 'latest_effective': '2026-11-20 23:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.344, 'l_abs': 0.681, 'l_hi': 0.807, 'l_lo': 0.716, 'b05': 0.725, 'b25': 0.663, 'b75': 0.658, 'b95': 0.745}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.646, 3.265, 2.073, 2.102, 3.052, 2.989, 3.683, 3.269, 3.252, 3.031, 3.172, 3.243, 2.991, 3.041]}
- calibration offsets (in sigma): {'05': -0.0655, '10': -0.041, '25': 0.0025, '40': -0.004, '50': 0.015, '60': 0.034, '75': 0.0075, '90': -0.029, '95': -0.0045}
