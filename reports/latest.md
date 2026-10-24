# ETH-USD 60s candle generator - report

- generated: 2026-10-24 00:53 UTC
- last closed candle: 2026-10-24 00:53 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.000 (3) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.517 (29) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.500 (8) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.604 (53) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.477 (742) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.500 (2) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.000 (3) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | - | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.000 (1) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 1.000 (1) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.250 (4) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | - | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.250 (4) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | - | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.480 (811) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07055, 0.1039] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5373, 'levels': [{'threshold': 0.07055, 'calls_per_day': 148.0, 'win_rate': 0.5998}, {'threshold': 0.1039, 'calls_per_day': 36.8, 'win_rate': 0.6486}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 28891, 'rate': 0.5315}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14898 | 0.337 | 0.524 (14651) | 0.590 (1521) | 0.765 (2447) |
| volatility: normal | 14897 | 0.365 | 0.522 (14834) | 0.624 (974) | 0.749 (2215) |
| volatility: wild | 14898 | 0.378 | 0.515 (14863) | 0.609 (437) | 0.777 (1901) |
| session: Asia 00-08 | 14933 | 0.359 | 0.527 (14836) | 0.613 (1049) | 0.765 (2154) |
| session: Europe 08-13 | 9300 | 0.355 | 0.520 (9215) | 0.601 (710) | 0.763 (1492) |
| session: US 13-21 | 14880 | 0.368 | 0.516 (14779) | 0.587 (726) | 0.769 (2103) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5518) | 0.615 (447) | 0.741 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.398 | 0.351 | 0.256 | 0.256 | 0.600 | 0.335 | 0.462 | 1.360 |
| 6h | 360 | 0.374 | 0.350 | 0.268 | 0.306 | 0.546 | 0.277 | 0.470 | 1.162 |
| 24h | 1440 | 0.375 | 0.361 | 0.274 | 0.306 | 0.536 | 0.271 | 0.480 | 1.263 |
| 7d | 10080 | 0.369 | 0.359 | 0.271 | 0.303 | 0.538 | 0.268 | 0.471 | 1.222 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.522 | 0.255 | 0.464 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.398 / 0.600 / 0.950; 2: 0.394 / 0.600 / 0.900; 3: 0.375 / 0.483 / 0.933; 4: 0.350 / 0.500 / 0.917; 5: 0.385 / 0.500 / 0.933; 6: 0.326 / 0.433 / 0.900; 7: 0.383 / 0.483 / 0.917; 8: 0.355 / 0.467 / 0.900; 9: 0.368 / 0.450 / 0.867; 10: 0.357 / 0.450 / 0.883; 11: 0.348 / 0.517 / 0.850; 12: 0.335 / 0.400 / 0.883; 13: 0.342 / 0.450 / 0.900; 14: 0.358 / 0.450 / 0.850; 15: 0.346 / 0.500 / 0.817
- 6h: 1: 0.374 / 0.546 / 0.906; 2: 0.355 / 0.515 / 0.861; 3: 0.358 / 0.513 / 0.853; 4: 0.352 / 0.493 / 0.847; 5: 0.359 / 0.499 / 0.828; 6: 0.349 / 0.510 / 0.828; 7: 0.351 / 0.476 / 0.808; 8: 0.354 / 0.529 / 0.817; 9: 0.363 / 0.518 / 0.817; 10: 0.353 / 0.499 / 0.811; 11: 0.349 / 0.507 / 0.794; 12: 0.347 / 0.493 / 0.800; 13: 0.352 / 0.510 / 0.797; 14: 0.346 / 0.462 / 0.800; 15: 0.356 / 0.540 / 0.786
- 24h: 1: 0.375 / 0.536 / 0.903; 2: 0.365 / 0.518 / 0.899; 3: 0.369 / 0.522 / 0.895; 4: 0.355 / 0.483 / 0.894; 5: 0.362 / 0.509 / 0.890; 6: 0.360 / 0.510 / 0.890; 7: 0.359 / 0.499 / 0.887; 8: 0.361 / 0.516 / 0.887; 9: 0.360 / 0.503 / 0.885; 10: 0.358 / 0.501 / 0.890; 11: 0.353 / 0.490 / 0.894; 12: 0.359 / 0.502 / 0.895; 13: 0.354 / 0.494 / 0.895; 14: 0.356 / 0.488 / 0.897; 15: 0.358 / 0.499 / 0.891
- 7d: 1: 0.369 / 0.538 / 0.895; 2: 0.356 / 0.499 / 0.900; 3: 0.358 / 0.509 / 0.900; 4: 0.351 / 0.492 / 0.899; 5: 0.352 / 0.498 / 0.899; 6: 0.353 / 0.496 / 0.899; 7: 0.351 / 0.495 / 0.898; 8: 0.354 / 0.508 / 0.898; 9: 0.351 / 0.496 / 0.898; 10: 0.353 / 0.507 / 0.898; 11: 0.348 / 0.495 / 0.897; 12: 0.350 / 0.502 / 0.898; 13: 0.348 / 0.492 / 0.898; 14: 0.350 / 0.499 / 0.898; 15: 0.348 / 0.498 / 0.897
- 30d: 1: 0.360 / 0.522 / 0.899; 2: 0.350 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.500 / 0.900; 7: 0.347 / 0.499 / 0.899; 8: 0.348 / 0.503 / 0.899; 9: 0.346 / 0.496 / 0.899; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.899; 12: 0.347 / 0.503 / 0.899; 13: 0.346 / 0.501 / 0.899; 14: 0.345 / 0.497 / 0.899; 15: 0.345 / 0.499 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.128 (body 0.097, range 0.158); 'price stays where it was' would score 0.128; colour right 0.583; typical miss of the close 13.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.111 (body 0.077, range 0.144); 'price stays where it was' would score 0.130; colour right 0.526; typical miss of the close 8.0 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.130 (body 0.089, range 0.171); 'price stays where it was' would score 0.134; colour right 0.506; typical miss of the close 9.2 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.130 (body 0.090, range 0.170); 'price stays where it was' would score 0.133; colour right 0.507; typical miss of the close 8.6 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.8; 2: 0.198 / 4.4; 3: 0.167 / 5.9; 4: 0.131 / 6.5; 5: 0.121 / 7.2; 6: 0.110 / 7.6; 7: 0.104 / 8.0; 8: 0.097 / 8.3; 9: 0.088 / 8.3; 10: 0.086 / 9.1; 11: 0.083 / 9.6; 12: 0.077 / 9.8; 13: 0.068 / 10.0; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 117887, probability skill vs chance 0.231, widened contest next: False
  - now: threshold 0.8358, hit rate recent 0.9447 / long run 0.9358
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.280, naive rule 0.505, lift 3.34x
    - 24h: 62 calls (62 a day), hit rate 0.952, chance 0.287, naive rule 0.492, lift 3.32x
    - 7d: 407 calls (58 a day), hit rate 0.931, chance 0.296, naive rule 0.497, lift 3.15x
    - 30d: 1691 calls (56 a day), hit rate 0.936, chance 0.293, naive rule 0.489, lift 3.20x
  - next: threshold 0.5668, hit rate recent 0.6135 / long run 0.5866
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.280, lift 2.38x
    - 24h: 59 calls (59 a day), hit rate 0.610, chance 0.287, lift 2.13x
    - 7d: 754 calls (108 a day), hit rate 0.589, chance 0.296, lift 1.99x
    - 30d: 2787 calls (93 a day), hit rate 0.578, chance 0.293, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.516; 0.40: 480, 0.572; 0.45: 410, 0.642; 0.50: 358, 0.696; 0.55: 313, 0.737; 0.60: 265, 0.782; 0.65: 222, 0.808; 0.70: 176, 0.840; 0.75: 136, 0.875; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.426; 0.35: 499, 0.463; 0.40: 406, 0.497; 0.45: 309, 0.530; 0.50: 201, 0.561; 0.55: 91, 0.569; 0.60: 14, 0.620; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 117885, probability skill vs chance 0.2164, widened contest next: False
  - now: threshold 0.6766, hit rate recent 0.7952 / long run 0.82
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.163, naive rule 0.351, lift 4.09x
    - 24h: 55 calls (55 a day), hit rate 0.818, chance 0.186, naive rule 0.402, lift 4.40x
    - 7d: 355 calls (51 a day), hit rate 0.814, chance 0.188, naive rule 0.406, lift 4.32x
    - 30d: 1551 calls (52 a day), hit rate 0.830, chance 0.188, naive rule 0.398, lift 4.42x
  - next: threshold 0.4198, hit rate recent 0.4955 / long run 0.4662
    - 6h: 31 calls (126 a day), hit rate 0.452, chance 0.163, lift 2.77x
    - 24h: 129 calls (130 a day), hit rate 0.519, chance 0.186, lift 2.79x
    - 7d: 956 calls (137 a day), hit rate 0.455, chance 0.188, lift 2.42x
    - 30d: 2738 calls (91 a day), hit rate 0.463, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 344, 0.495; 0.40: 276, 0.566; 0.45: 223, 0.623; 0.50: 176, 0.672; 0.55: 135, 0.712; 0.60: 104, 0.755; 0.65: 76, 0.791; 0.70: 54, 0.829; 0.75: 31, 0.872; 0.80: 10, 0.905
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 250, 0.421; 0.40: 156, 0.448; 0.45: 69, 0.460; 0.50: 15, 0.488; 0.55: 1, 0.513
- **K=8**: model 1792800000, labels learned 117882, probability skill vs chance 0.1901, widened contest next: True
  - now: threshold 0.5605, hit rate recent 0.6153 / long run 0.6793
    - 6h: 12 calls (49 a day), hit rate 0.500, chance 0.120, naive rule 0.321, lift 4.17x
    - 24h: 54 calls (54 a day), hit rate 0.574, chance 0.116, naive rule 0.322, lift 4.95x
    - 7d: 324 calls (46 a day), hit rate 0.657, chance 0.117, naive rule 0.319, lift 5.64x
    - 30d: 1523 calls (51 a day), hit rate 0.701, chance 0.121, naive rule 0.328, lift 5.79x
  - next: threshold 0.3399, hit rate recent 0.3813 / long run 0.3766
    - 6h: 30 calls (123 a day), hit rate 0.333, chance 0.120, lift 2.78x
    - 24h: 124 calls (125 a day), hit rate 0.403, chance 0.116, lift 3.47x
    - 7d: 792 calls (113 a day), hit rate 0.375, chance 0.117, lift 3.22x
    - 30d: 2493 calls (83 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.424; 0.35: 191, 0.494; 0.40: 146, 0.548; 0.45: 112, 0.594; 0.50: 85, 0.633; 0.55: 62, 0.676; 0.60: 41, 0.722; 0.65: 23, 0.789; 0.70: 10, 0.840; 0.75: 1, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.350; 0.35: 100, 0.377; 0.40: 38, 0.400; 0.45: 8, 0.434; 0.50: 1, 0.531
- **K=13**: model 1792800000, labels learned 117877, probability skill vs chance 0.1695, widened contest next: True
  - now: threshold 0.4071, hit rate recent 0.4932 / long run 0.5502
    - 6h: 11 calls (46 a day), hit rate 0.364, chance 0.065, naive rule 0.237, lift 5.58x
    - 24h: 55 calls (56 a day), hit rate 0.473, chance 0.074, naive rule 0.271, lift 6.36x
    - 7d: 366 calls (52 a day), hit rate 0.525, chance 0.075, naive rule 0.273, lift 7.01x
    - 30d: 1553 calls (52 a day), hit rate 0.567, chance 0.077, naive rule 0.272, lift 7.34x
  - next: threshold 0.2926, hit rate recent 0.2654 / long run 0.3086
    - 6h: 18 calls (75 a day), hit rate 0.167, chance 0.065, lift 2.56x
    - 24h: 66 calls (67 a day), hit rate 0.288, chance 0.074, lift 3.87x
    - 7d: 466 calls (67 a day), hit rate 0.309, chance 0.075, lift 4.13x
    - 30d: 2159 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.446; 0.35: 86, 0.499; 0.40: 61, 0.552; 0.45: 41, 0.605; 0.50: 25, 0.655; 0.55: 14, 0.705; 0.60: 6, 0.749; 0.65: 2, 0.848
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.316; 0.35: 13, 0.348; 0.40: 2, 0.443; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.101 | 0.81% | 0.950 | 0.400 | 0.251 | 0.450 | 0.286 |
| 6h | 14.699 | 4.59% | 0.914 | 0.506 | 0.251 | 0.476 | 0.630 |
| 24h | 15.146 | 2.70% | 0.908 | 0.502 | 0.250 | 0.494 | 0.631 |
| 7d | 14.795 | 3.47% | 0.900 | 0.499 | 0.250 | 0.500 | 0.644 |
| 30d | 13.524 | 4.08% | 0.900 | 0.500 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.217 | 14.531 | 14.241 | 13.973 | 14.528 | 14.326 | 14.239 | 14.311 | 14.152 | 14.101 |
| 6h | 15.406 | 14.999 | 14.755 | 14.582 | 14.984 | 14.791 | 14.717 | 14.750 | 14.667 | 14.699 |
| 24h | 15.566 | 15.289 | 15.203 | 15.110 | 15.409 | 15.243 | 15.120 | 15.125 | 15.111 | 15.146 |
| 7d | 15.327 | 14.933 | 14.884 | 14.809 | 15.049 | 14.937 | 14.780 | 14.765 | 14.768 | 14.795 |
| 30d | 14.099 | 13.647 | 13.606 | 13.545 | 13.767 | 13.709 | 13.520 | 13.500 | 13.498 | 13.524 |

## Next candle

- candle starting 2026-10-24 00:53 UTC, last close 2373.61
- P(up) 0.4876, return quantiles (bp): {'05': -10.311, '10': -8.004, '25': -4.429, '40': -2.023, '50': -0.207, '60': 1.491, '75': 3.799, '90': 6.879, '95': 9.487}
- changepoint probability 0.0666, regime age 69.0 min
- agent weights: empirical 0.004, ewma 0.034, garch 0.119, har 0.333, bocpd 0.019, hmm 0.087, online_qr 0.211, lgbm 0.192

## Learning log

- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.32, 7.07, 17.63], current probabilities: [0.332, 0.65, 0.018]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 01:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.261, 'l_abs': 0.681, 'l_hi': 0.791, 'l_lo': 0.791, 'b05': 0.723, 'b25': 0.705, 'b75': 0.618, 'b95': 0.696}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.481, 1.93, 2.278, 2.877, 3.158, 3.777, 4.128, 4.387, 4.364, 4.773, 4.896, 5.106, 5.205, 5.966]}
- calibration offsets (in sigma): {'05': 0.046, '10': -0.008, '25': -0.06, '40': -0.062, '50': -0.01, '60': 0.032, '75': -0.0, '90': -0.082, '95': -0.096}
