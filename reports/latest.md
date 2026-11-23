# ETH-USD 60s candle generator - report

- generated: 2026-11-23 09:06 UTC
- last closed candle: 2026-11-23 09:06 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.533 (672) [0.507, 0.558] | 0.517 (2879) [0.501, 0.533] | 0.515 (7865) [0.505, 0.526] | 0.518 (4893) [0.504, 0.532] | 0.500 (36) | 0.500 | flat +0.011 (noise 0.029) |
| colour_clear | 0.529 (780) | 0.546 (5561) [0.532, 0.561] | 0.541 (23786) [0.535, 0.547] | 0.526 (64534) [0.520, 0.531] | 0.543 (40296) [0.539, 0.548] | 0.583 (307) | 0.500 | flat +0.007 (noise 0.010) |
| colour_confident | 0.588 (272) | 0.576 (1351) [0.556, 0.593] | 0.574 (4578) [0.563, 0.584] | 0.586 (7502) [0.577, 0.595] | 0.586 (7502) [0.577, 0.595] | 0.562 (89) | 0.500 | flat +0.046 (noise 0.024) |
| colour_next | 0.532 (1435) | 0.530 (10047) [0.524, 0.536] | 0.530 (42899) [0.526, 0.534] | 0.519 (117224) [0.515, 0.522] | 0.530 (72875) [0.527, 0.533] | 0.562 (543) | 0.500 | flat +0.002 (noise 0.007) |
| colour_path | 0.499 (20090) | 0.503 (140658) [0.501, 0.505] | 0.502 (600586) [0.501, 0.503] | 0.501 (1641136) [0.500, 0.502] | 0.501 (1020250) [0.500, 0.502] | 0.492 (7602) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.635 (96) | 0.615 (395) [0.584, 0.647] | 0.609 (1257) [0.594, 0.623] | 0.625 (1993) [0.610, 0.638] | 0.625 (1993) [0.610, 0.638] | 0.588 (34) | 0.500 | flat +0.036 (noise 0.054) |
| reversal_k13_next | 0.455 (44) | 0.326 (476) [0.286, 0.376] | 0.336 (1843) [0.318, 0.355] | 0.317 (5398) [0.307, 0.326] | 0.328 (3293) [0.317, 0.340] | 0.308 (13) | 0.078 | flat -0.026 (noise 0.033) |
| reversal_k13_now | 0.577 (52) | 0.555 (373) [0.520, 0.595] | 0.577 (1628) [0.557, 0.596] | 0.574 (4228) [0.561, 0.586] | 0.570 (2756) [0.555, 0.586] | 0.533 (15) | 0.078 | flat -0.049 (noise 0.037) |
| reversal_k3_next | 0.657 (169) | 0.600 (797) [0.568, 0.628] | 0.604 (2553) [0.592, 0.617] | 0.591 (7061) [0.582, 0.599] | 0.593 (4621) [0.582, 0.603] | 0.586 (58) | 0.294 | flat -0.024 (noise 0.033) |
| reversal_k3_now | 0.950 (60) | 0.938 (388) [0.921, 0.956] | 0.931 (1718) [0.922, 0.941] | 0.935 (4692) [0.930, 0.941] | 0.931 (2929) [0.925, 0.938] | 1.000 (13) | 0.293 | flat +0.014 (noise 0.018) |
| reversal_k5_next | 0.639 (36) | 0.487 (355) [0.429, 0.558] | 0.512 (1890) [0.493, 0.531] | 0.487 (6071) [0.476, 0.498] | 0.483 (4081) [0.469, 0.498] | 0.600 (10) | 0.187 | flat -0.019 (noise 0.048) |
| reversal_k5_now | 0.864 (59) | 0.801 (418) [0.772, 0.828] | 0.796 (1761) [0.780, 0.812] | 0.817 (4477) [0.807, 0.826] | 0.805 (2866) [0.793, 0.816] | 0.947 (19) | 0.187 | flat +0.058 (noise 0.029) |
| reversal_k8_next | 0.467 (75) | 0.411 (569) [0.381, 0.446] | 0.417 (2285) [0.402, 0.434] | 0.399 (6386) [0.389, 0.409] | 0.400 (4280) [0.388, 0.412] | 0.417 (24) | 0.121 | flat -0.027 (noise 0.031) |
| reversal_k8_now | 0.656 (61) | 0.662 (423) [0.637, 0.684] | 0.682 (1645) [0.664, 0.700] | 0.694 (4329) [0.682, 0.707] | 0.683 (2742) [0.668, 0.697] | 0.667 (18) | 0.122 | flat -0.005 (noise 0.034) |
| overall | 0.505 (22177) | 0.507 (155176) [0.505, 0.509] | 0.506 (661687) [0.505, 0.507] | 0.504 (1808867) [0.503, 0.505] | 0.505 (1125586) [0.504, 0.506] | 0.499 (8351) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07568, 0.1078] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5311, 'levels': [{'threshold': 0.07568, 'calls_per_day': 147.1, 'win_rate': 0.5837}, {'threshold': 0.1078, 'calls_per_day': 36.9, 'win_rate': 0.6062}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42900, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15062 | 0.349 | 0.532 (14845) | 0.564 (2250) | 0.753 (2542) |
| volatility: normal | 15062 | 0.378 | 0.527 (15009) | 0.586 (1482) | 0.739 (2386) |
| volatility: wild | 15062 | 0.390 | 0.532 (15022) | 0.590 (1137) | 0.754 (2124) |
| session: Asia 00-08 | 15360 | 0.371 | 0.530 (15245) | 0.564 (1724) | 0.750 (2311) |
| session: Europe 08-13 | 9366 | 0.367 | 0.532 (9292) | 0.584 (1197) | 0.756 (1492) |
| session: US 13-21 | 14880 | 0.380 | 0.534 (14791) | 0.607 (1337) | 0.742 (2407) |
| session: late 21-24 | 5580 | 0.366 | 0.517 (5548) | 0.534 (611) | 0.748 (842) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.369 | 0.342 | 0.240 | 0.240 | 0.517 | 0.275 | 0.463 | 0.828 |
| 6h | 360 | 0.387 | 0.377 | 0.297 | 0.328 | 0.559 | 0.279 | 0.496 | 1.155 |
| 24h | 1440 | 0.377 | 0.374 | 0.281 | 0.314 | 0.553 | 0.264 | 0.489 | 1.254 |
| 7d | 10080 | 0.384 | 0.377 | 0.299 | 0.333 | 0.531 | 0.266 | 0.501 | 1.185 |
| 30d | 43200 | 0.373 | 0.366 | 0.287 | 0.318 | 0.530 | 0.265 | 0.480 | 1.266 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.369 / 0.517 / 0.850; 2: 0.350 / 0.450 / 0.850; 3: 0.386 / 0.617 / 0.900; 4: 0.344 / 0.500 / 0.950; 5: 0.359 / 0.500 / 0.967; 6: 0.351 / 0.517 / 0.967; 7: 0.337 / 0.483 / 1.000; 8: 0.341 / 0.483 / 1.000; 9: 0.346 / 0.467 / 1.000; 10: 0.297 / 0.367 / 1.000; 11: 0.341 / 0.433 / 1.000; 12: 0.320 / 0.367 / 1.000; 13: 0.358 / 0.533 / 1.000; 14: 0.337 / 0.450 / 1.000; 15: 0.334 / 0.433 / 1.000
- 6h: 1: 0.387 / 0.559 / 0.914; 2: 0.357 / 0.483 / 0.919; 3: 0.374 / 0.553 / 0.939; 4: 0.358 / 0.506 / 0.978; 5: 0.366 / 0.494 / 0.981; 6: 0.364 / 0.494 / 0.981; 7: 0.355 / 0.492 / 0.989; 8: 0.346 / 0.455 / 0.989; 9: 0.357 / 0.486 / 0.992; 10: 0.353 / 0.480 / 0.992; 11: 0.363 / 0.508 / 0.983; 12: 0.365 / 0.503 / 0.981; 13: 0.362 / 0.489 / 0.969; 14: 0.355 / 0.494 / 0.975; 15: 0.361 / 0.511 / 0.972
- 24h: 1: 0.377 / 0.553 / 0.899; 2: 0.358 / 0.481 / 0.902; 3: 0.362 / 0.524 / 0.903; 4: 0.353 / 0.481 / 0.912; 5: 0.362 / 0.517 / 0.909; 6: 0.356 / 0.495 / 0.909; 7: 0.351 / 0.497 / 0.908; 8: 0.350 / 0.498 / 0.911; 9: 0.352 / 0.488 / 0.912; 10: 0.350 / 0.497 / 0.914; 11: 0.355 / 0.496 / 0.915; 12: 0.353 / 0.505 / 0.915; 13: 0.353 / 0.494 / 0.925; 14: 0.352 / 0.509 / 0.924; 15: 0.351 / 0.501 / 0.933
- 7d: 1: 0.384 / 0.531 / 0.901; 2: 0.371 / 0.491 / 0.901; 3: 0.372 / 0.506 / 0.901; 4: 0.370 / 0.496 / 0.902; 5: 0.374 / 0.511 / 0.902; 6: 0.370 / 0.502 / 0.902; 7: 0.369 / 0.503 / 0.901; 8: 0.371 / 0.511 / 0.902; 9: 0.366 / 0.495 / 0.901; 10: 0.369 / 0.509 / 0.902; 11: 0.368 / 0.506 / 0.902; 12: 0.368 / 0.503 / 0.902; 13: 0.366 / 0.501 / 0.902; 14: 0.366 / 0.501 / 0.902; 15: 0.365 / 0.499 / 0.902
- 30d: 1: 0.373 / 0.530 / 0.898; 2: 0.359 / 0.490 / 0.900; 3: 0.363 / 0.511 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.358 / 0.502 / 0.900; 7: 0.358 / 0.501 / 0.900; 8: 0.359 / 0.506 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.358 / 0.504 / 0.900; 11: 0.357 / 0.506 / 0.900; 12: 0.357 / 0.504 / 0.900; 13: 0.356 / 0.501 / 0.900; 14: 0.356 / 0.502 / 0.900; 15: 0.356 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.176 (body 0.124, range 0.229); 'price stays where it was' would score 0.170; colour right 0.467; typical miss of the close 8.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.143 (body 0.098, range 0.189); 'price stays where it was' would score 0.142; colour right 0.492; typical miss of the close 13.1 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.131 (body 0.083, range 0.178); 'price stays where it was' would score 0.138; colour right 0.490; typical miss of the close 11.4 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.134 (body 0.087, range 0.181); 'price stays where it was' would score 0.140; colour right 0.505; typical miss of the close 13.7 bp; chain ended on the right side 0.524 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.169); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 10.4 bp; chain ended on the right side 0.517 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.6; 2: 0.206 / 6.3; 3: 0.168 / 8.2; 4: 0.136 / 8.6; 5: 0.125 / 9.3; 6: 0.120 / 10.0; 7: 0.116 / 10.6; 8: 0.100 / 11.5; 9: 0.092 / 12.0; 10: 0.089 / 12.6; 11: 0.087 / 13.0; 12: 0.081 / 13.1; 13: 0.074 / 13.9; 14: 0.070 / 14.3; 15: 0.067 / 14.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 161580, probability skill vs chance 0.2431, widened contest next: False
  - now: threshold 0.8295, hit rate recent 0.9478 / long run 0.9334
    - 6h: 7 calls (28 a day), hit rate 1.000, chance 0.313, naive rule 0.573, lift 3.20x
    - 24h: 57 calls (57 a day), hit rate 0.947, chance 0.315, naive rule 0.568, lift 3.01x
    - 7d: 383 calls (55 a day), hit rate 0.943, chance 0.296, naive rule 0.515, lift 3.19x
    - 30d: 1709 calls (57 a day), hit rate 0.931, chance 0.294, naive rule 0.503, lift 3.17x
  - next: threshold 0.5115, hit rate recent 0.6208 / long run 0.6116
    - 6h: 36 calls (146 a day), hit rate 0.583, chance 0.313, lift 1.87x
    - 24h: 174 calls (175 a day), hit rate 0.638, chance 0.315, lift 2.03x
    - 7d: 823 calls (118 a day), hit rate 0.600, chance 0.296, lift 2.03x
    - 30d: 2587 calls (86 a day), hit rate 0.603, chance 0.294, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 558, 0.504; 0.35: 529, 0.528; 0.40: 478, 0.576; 0.45: 413, 0.641; 0.50: 363, 0.686; 0.55: 315, 0.732; 0.60: 266, 0.777; 0.65: 223, 0.806; 0.70: 175, 0.837; 0.75: 141, 0.871; 0.80: 92, 0.903; 0.85: 43, 0.939; 0.90: 4, 0.962
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.436; 0.35: 489, 0.469; 0.40: 386, 0.509; 0.45: 291, 0.543; 0.50: 186, 0.577; 0.55: 79, 0.587; 0.60: 10, 0.639; 0.65: 0, 0.533
- **K=5**: model 1794528000, labels learned 161578, probability skill vs chance 0.2334, widened contest next: False
  - now: threshold 0.7001, hit rate recent 0.8616 / long run 0.7986
    - 6h: 6 calls (24 a day), hit rate 1.000, chance 0.214, naive rule 0.503, lift 4.68x
    - 24h: 60 calls (60 a day), hit rate 0.883, chance 0.217, naive rule 0.504, lift 4.06x
    - 7d: 418 calls (60 a day), hit rate 0.811, chance 0.196, naive rule 0.435, lift 4.14x
    - 30d: 1760 calls (59 a day), hit rate 0.797, chance 0.188, naive rule 0.415, lift 4.24x
  - next: threshold 0.4289, hit rate recent 0.609 / long run 0.5101
    - 24h: 34 calls (34 a day), hit rate 0.647, chance 0.217, lift 2.98x
    - 7d: 338 calls (48 a day), hit rate 0.485, chance 0.196, lift 2.48x
    - 30d: 1854 calls (62 a day), hit rate 0.514, chance 0.188, lift 2.73x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.425; 0.35: 362, 0.476; 0.40: 293, 0.544; 0.45: 237, 0.603; 0.50: 186, 0.654; 0.55: 149, 0.687; 0.60: 115, 0.733; 0.65: 82, 0.771; 0.70: 51, 0.806; 0.75: 27, 0.839; 0.80: 6, 0.851
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 335, 0.394; 0.35: 249, 0.433; 0.40: 159, 0.464; 0.45: 64, 0.509; 0.50: 8, 0.568; 0.55: 1, 0.471
- **K=8**: model 1794960000, labels learned 161575, probability skill vs chance 0.2167, widened contest next: False
  - now: threshold 0.5821, hit rate recent 0.6681 / long run 0.6726
    - 6h: 6 calls (25 a day), hit rate 0.667, chance 0.141, naive rule 0.456, lift 4.71x
    - 24h: 62 calls (62 a day), hit rate 0.694, chance 0.131, naive rule 0.408, lift 5.28x
    - 7d: 424 calls (61 a day), hit rate 0.663, chance 0.125, naive rule 0.361, lift 5.29x
    - 30d: 1643 calls (55 a day), hit rate 0.680, chance 0.123, naive rule 0.349, lift 5.53x
  - next: threshold 0.3526, hit rate recent 0.4647 / long run 0.4235
    - 6h: 13 calls (53 a day), hit rate 0.462, chance 0.141, lift 3.26x
    - 24h: 74 calls (75 a day), hit rate 0.473, chance 0.131, lift 3.60x
    - 7d: 564 calls (81 a day), hit rate 0.413, chance 0.125, lift 3.30x
    - 30d: 2276 calls (76 a day), hit rate 0.419, chance 0.123, lift 3.40x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.429; 0.35: 200, 0.488; 0.40: 157, 0.537; 0.45: 120, 0.579; 0.50: 86, 0.637; 0.55: 62, 0.673; 0.60: 41, 0.711; 0.65: 24, 0.762; 0.70: 9, 0.804; 0.75: 1, 0.744
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 159, 0.378; 0.35: 83, 0.408; 0.40: 27, 0.440; 0.45: 6, 0.469; 0.50: 1, 0.667
- **K=13**: model 1795132800, labels learned 161570, probability skill vs chance 0.1984, widened contest next: False
  - now: threshold 0.456, hit rate recent 0.5828 / long run 0.574
    - 6h: 6 calls (25 a day), hit rate 0.333, chance 0.074, naive rule 0.351, lift 4.51x
    - 24h: 48 calls (49 a day), hit rate 0.562, chance 0.079, naive rule 0.362, lift 7.09x
    - 7d: 378 calls (54 a day), hit rate 0.556, chance 0.080, naive rule 0.304, lift 6.92x
    - 30d: 1622 calls (54 a day), hit rate 0.575, chance 0.079, naive rule 0.296, lift 7.25x
  - next: threshold 0.3061, hit rate recent 0.4187 / long run 0.339
    - 6h: 6 calls (25 a day), hit rate 0.333, chance 0.074, lift 4.51x
    - 24h: 42 calls (42 a day), hit rate 0.429, chance 0.079, lift 5.40x
    - 7d: 463 calls (66 a day), hit rate 0.330, chance 0.080, lift 4.11x
    - 30d: 1837 calls (61 a day), hit rate 0.337, chance 0.079, lift 4.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 140, 0.425; 0.35: 102, 0.475; 0.40: 71, 0.536; 0.45: 49, 0.585; 0.50: 34, 0.622; 0.55: 21, 0.646; 0.60: 10, 0.668; 0.65: 2, 0.529; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.344; 0.35: 15, 0.381; 0.40: 3, 0.429; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.810 | 0.18% | 0.900 | 0.350 | 0.251 | 0.467 | 0.284 |
| 6h | 20.918 | 2.03% | 0.917 | 0.478 | 0.250 | 0.506 | 0.450 |
| 24h | 19.891 | 2.42% | 0.897 | 0.492 | 0.249 | 0.524 | 0.513 |
| 7d | 23.861 | 4.05% | 0.900 | 0.499 | 0.250 | 0.503 | 0.664 |
| 30d | 19.080 | 4.81% | 0.900 | 0.500 | 0.250 | 0.505 | 0.712 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.845 | 20.082 | 19.805 | 19.765 | 20.168 | 20.005 | 19.799 | 19.866 | 19.769 | 19.810 |
| 6h | 21.352 | 21.122 | 20.963 | 20.943 | 21.459 | 21.113 | 20.958 | 20.875 | 20.877 | 20.918 |
| 24h | 20.384 | 20.183 | 20.054 | 19.901 | 20.492 | 20.184 | 19.857 | 19.853 | 19.857 | 19.891 |
| 7d | 24.869 | 24.101 | 24.027 | 23.877 | 24.373 | 24.150 | 23.850 | 23.813 | 23.825 | 23.861 |
| 30d | 20.044 | 19.267 | 19.220 | 19.138 | 19.479 | 19.398 | 19.065 | 19.038 | 19.048 | 19.080 |

## Next candle

- candle starting 2026-11-23 09:06 UTC, last close 1725.0
- P(up) 0.4886, return quantiles (bp): {'05': -9.227, '10': -7.509, '25': -4.289, '40': -1.447, '50': -0.171, '60': 1.359, '75': 3.958, '90': 7.516, '95': 10.364}
- changepoint probability 0.0547, regime age 93.6 min
- agent weights: empirical 0.021, ewma 0.066, garch 0.119, har 0.202, bocpd 0.017, hmm 0.056, online_qr 0.243, lgbm 0.277

## Learning log

- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- 2026-11-22 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9215}, "hmm": {"sd_bp": [5.69, 10.58, 28.33], "stay": [0.985, 0.953, 0.874]}, "lgbm": {"challenger_loss": 0.24557, "champion_loss": 0.24554, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48129, "challengers": 1, "chance_loss": 0.60807, "widened": false, "champion_loss": 0.47918, "promoted": false}, "reversal_k5": {"challenger_loss": 0.381, "challengers": 1, "chance_loss": 0.49754, "widened": false, "champion_loss": 0.37986, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28291, "challengers": 1, "chance_loss": 0.38778, "widened": false, "champion_loss": 0.28187, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20591, "challengers": 1, "chance_loss": 0.29298, "widened": false, "champion_loss": 0.20541, "promoted": false}}
- 2026-11-22 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.9173}, "hmm": {"sd_bp": [5.55, 10.36, 28.43], "stay": [0.982, 0.95, 0.859]}}
- 2026-11-23 00:00 UTC: {"garch": {"alpha": 0.0752, "beta": 0.917}, "hmm": {"sd_bp": [5.28, 10.22, 28.39], "stay": [0.976, 0.946, 0.857]}, "lgbm": {"challenger_loss": 0.24364, "champion_loss": 0.24354, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.61601, "widened": false, "champion_loss": 0.4869, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38212, "challengers": 1, "chance_loss": 0.503, "widened": false, "champion_loss": 0.38113, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29091, "challengers": 1, "chance_loss": 0.3912, "widened": false, "champion_loss": 0.28935, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20987, "challengers": 1, "chance_loss": 0.29233, "widened": false, "champion_loss": 0.20927, "promoted": false}}
- HMM volatility states (sd, bp per minute): [5.28, 10.22, 28.39], current probabilities: [0.944, 0.054, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-11-23 09:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.444, 'l_abs': 0.785, 'l_hi': 0.811, 'l_lo': 0.771, 'b05': 0.776, 'b25': 0.793, 'b75': 0.729, 'b95': 0.759}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.3, 1.5], [1.3, 1.6], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.4, 1.5]], 'cone_width': [1.305, 1.539, 1.548, 1.956, 2.022, 2.568, 2.642, 2.698, 2.684, 2.552, 2.618, 2.676, 3.201, 3.127]}
- calibration offsets (in sigma): {'05': 0.0825, '10': -0.015, '25': -0.0675, '40': 0.01, '50': -0.005, '60': 0.01, '75': 0.0375, '90': -0.015, '95': -0.0125}
