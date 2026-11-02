# ETH-USD 60s candle generator - report

- generated: 2026-11-02 22:28 UTC
- last closed candle: 2026-11-02 22:28 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.448 (96) | 0.495 (672) [0.473, 0.518] | 0.518 (2878) [0.498, 0.538] | 0.514 (5850) [0.501, 0.527] | 0.518 (2878) [0.498, 0.538] | 0.494 (89) | 0.500 | flat -0.052 (noise 0.027) |
| colour_clear | 0.537 (747) | 0.542 (5503) [0.533, 0.551] | 0.545 (23558) [0.541, 0.549] | 0.520 (47796) [0.514, 0.527] | 0.545 (23558) [0.541, 0.549] | 0.518 (764) | 0.500 | flat -0.009 (noise 0.009) |
| colour_confident | 0.550 (229) | 0.581 (1051) [0.567, 0.595] | 0.598 (4512) [0.586, 0.610] | 0.598 (4512) [0.586, 0.610] | 0.598 (4512) [0.586, 0.610] | 0.573 (82) | 0.500 | flat -0.025 (noise 0.020) |
| colour_next | 0.529 (1408) | 0.530 (9966) [0.523, 0.538] | 0.530 (42807) [0.526, 0.533] | 0.515 (87156) [0.511, 0.519] | 0.530 (42807) [0.526, 0.533] | 0.528 (1342) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.505 (19712) | 0.502 (139524) [0.500, 0.504] | 0.501 (599298) [0.499, 0.502] | 0.501 (1220184) [0.500, 0.502] | 0.501 (599298) [0.499, 0.502] | 0.499 (18788) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.607 (56) | 0.610 (272) [0.574, 0.646] | 0.632 (1213) [0.613, 0.652] | 0.632 (1213) [0.613, 0.652] | 0.632 (1213) [0.613, 0.652] | 0.706 (17) | 0.500 | flat -0.018 (noise 0.038) |
| reversal_k13_next | 0.343 (35) | 0.335 (355) [0.288, 0.384] | 0.321 (1934) [0.309, 0.334] | 0.310 (4039) [0.299, 0.322] | 0.321 (1934) [0.309, 0.334] | 0.422 (45) | 0.077 | flat +0.018 (noise 0.033) |
| reversal_k13_now | 0.576 (66) | 0.574 (441) [0.534, 0.613] | 0.568 (1675) [0.548, 0.588] | 0.574 (3147) [0.559, 0.588] | 0.568 (1675) [0.548, 0.588] | 0.468 (47) | 0.077 | flat +0.022 (noise 0.035) |
| reversal_k3_next | 0.614 (132) | 0.591 (881) [0.584, 0.599] | 0.583 (3083) [0.573, 0.594] | 0.585 (5523) [0.576, 0.594] | 0.583 (3083) [0.573, 0.594] | 0.676 (105) | 0.293 | flat -0.002 (noise 0.025) |
| reversal_k3_now | 0.895 (67) | 0.945 (439) [0.923, 0.968] | 0.935 (1745) [0.924, 0.945] | 0.938 (3508) [0.932, 0.945] | 0.935 (1745) [0.924, 0.945] | 0.907 (54) | 0.294 | flat +0.010 (noise 0.020) |
| reversal_k5_next | 0.567 (60) | 0.532 (447) [0.518, 0.549] | 0.473 (2900) [0.458, 0.488] | 0.481 (4890) [0.470, 0.493] | 0.473 (2900) [0.458, 0.488] | 0.596 (52) | 0.187 | up +0.063 (noise 0.029) |
| reversal_k5_now | 0.831 (71) | 0.826 (431) [0.813, 0.837] | 0.821 (1640) [0.811, 0.832] | 0.829 (3251) [0.820, 0.839] | 0.821 (1640) [0.811, 0.832] | 0.806 (62) | 0.187 | flat +0.008 (noise 0.027) |
| reversal_k8_next | 0.500 (50) | 0.415 (645) [0.385, 0.449] | 0.390 (2845) [0.377, 0.404] | 0.392 (4951) [0.381, 0.404] | 0.390 (2845) [0.377, 0.404] | 0.487 (39) | 0.121 | flat +0.037 (noise 0.026) |
| reversal_k8_now | 0.710 (62) | 0.703 (394) [0.649, 0.747] | 0.691 (1594) [0.669, 0.711] | 0.702 (3181) [0.688, 0.717] | 0.691 (1594) [0.669, 0.711] | 0.652 (46) | 0.121 | flat +0.038 (noise 0.040) |
| overall | 0.510 (21759) | 0.507 (154195) [0.504, 0.509] | 0.505 (662399) [0.503, 0.506] | 0.504 (1345680) [0.503, 0.505] | 0.505 (662399) [0.503, 0.506] | 0.504 (20669) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08088, 0.1232] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.532, 'levels': [{'threshold': 0.08088, 'calls_per_day': 143.0, 'win_rate': 0.582}, {'threshold': 0.1232, 'calls_per_day': 35.6, 'win_rate': 0.6111}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42831, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15331 | 0.334 | 0.526 (15045) | 0.576 (2261) | 0.758 (2691) |
| volatility: normal | 15328 | 0.366 | 0.533 (15253) | 0.610 (1537) | 0.742 (2284) |
| volatility: wild | 15329 | 0.381 | 0.527 (15283) | 0.632 (796) | 0.769 (2104) |
| session: Asia 00-08 | 15360 | 0.360 | 0.535 (15245) | 0.600 (1604) | 0.760 (2296) |
| session: Europe 08-13 | 9600 | 0.354 | 0.531 (9497) | 0.594 (1164) | 0.751 (1591) |
| session: US 13-21 | 15360 | 0.368 | 0.527 (15235) | 0.596 (1199) | 0.760 (2335) |
| session: late 21-24 | 5668 | 0.351 | 0.514 (5604) | 0.597 (627) | 0.743 (857) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.399 | 0.384 | 0.325 | 0.325 | 0.492 | 0.302 | 0.496 | 0.980 |
| 6h | 360 | 0.380 | 0.383 | 0.321 | 0.369 | 0.485 | 0.253 | 0.507 | 1.145 |
| 24h | 1440 | 0.372 | 0.371 | 0.289 | 0.323 | 0.522 | 0.264 | 0.480 | 1.132 |
| 7d | 10080 | 0.360 | 0.355 | 0.275 | 0.304 | 0.530 | 0.260 | 0.459 | 1.291 |
| 30d | 43200 | 0.361 | 0.354 | 0.275 | 0.305 | 0.530 | 0.262 | 0.461 | 1.263 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.399 / 0.492 / 0.933; 2: 0.371 / 0.441 / 0.933; 3: 0.392 / 0.508 / 0.850; 4: 0.365 / 0.441 / 0.850; 5: 0.412 / 0.610 / 0.833; 6: 0.398 / 0.492 / 0.933; 7: 0.386 / 0.559 / 0.883; 8: 0.325 / 0.254 / 0.900; 9: 0.385 / 0.508 / 0.883; 10: 0.368 / 0.390 / 0.900; 11: 0.410 / 0.610 / 0.917; 12: 0.343 / 0.356 / 0.933; 13: 0.398 / 0.525 / 0.900; 14: 0.383 / 0.508 / 0.900; 15: 0.372 / 0.492 / 0.917
- 6h: 1: 0.380 / 0.485 / 0.908; 2: 0.397 / 0.538 / 0.933; 3: 0.376 / 0.493 / 0.844; 4: 0.382 / 0.499 / 0.828; 5: 0.382 / 0.521 / 0.817; 6: 0.390 / 0.518 / 0.853; 7: 0.385 / 0.526 / 0.797; 8: 0.376 / 0.482 / 0.797; 9: 0.375 / 0.482 / 0.808; 10: 0.371 / 0.474 / 0.792; 11: 0.378 / 0.501 / 0.814; 12: 0.368 / 0.468 / 0.828; 13: 0.389 / 0.524 / 0.819; 14: 0.373 / 0.496 / 0.822; 15: 0.372 / 0.493 / 0.836
- 24h: 1: 0.372 / 0.522 / 0.906; 2: 0.365 / 0.498 / 0.909; 3: 0.364 / 0.503 / 0.897; 4: 0.360 / 0.497 / 0.892; 5: 0.361 / 0.510 / 0.888; 6: 0.367 / 0.522 / 0.900; 7: 0.364 / 0.517 / 0.887; 8: 0.355 / 0.494 / 0.895; 9: 0.358 / 0.497 / 0.891; 10: 0.356 / 0.483 / 0.891; 11: 0.354 / 0.486 / 0.901; 12: 0.356 / 0.488 / 0.901; 13: 0.358 / 0.491 / 0.903; 14: 0.358 / 0.506 / 0.902; 15: 0.353 / 0.490 / 0.899
- 7d: 1: 0.360 / 0.530 / 0.898; 2: 0.348 / 0.493 / 0.901; 3: 0.351 / 0.507 / 0.898; 4: 0.347 / 0.499 / 0.897; 5: 0.349 / 0.514 / 0.897; 6: 0.346 / 0.506 / 0.898; 7: 0.347 / 0.500 / 0.896; 8: 0.345 / 0.508 / 0.896; 9: 0.346 / 0.503 / 0.897; 10: 0.345 / 0.499 / 0.897; 11: 0.344 / 0.500 / 0.898; 12: 0.344 / 0.496 / 0.899; 13: 0.345 / 0.505 / 0.898; 14: 0.344 / 0.500 / 0.898; 15: 0.344 / 0.503 / 0.898
- 30d: 1: 0.361 / 0.530 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.348 / 0.505 / 0.899; 6: 0.347 / 0.500 / 0.900; 7: 0.347 / 0.500 / 0.899; 8: 0.347 / 0.503 / 0.899; 9: 0.346 / 0.499 / 0.899; 10: 0.347 / 0.504 / 0.899; 11: 0.344 / 0.497 / 0.899; 12: 0.346 / 0.502 / 0.900; 13: 0.345 / 0.501 / 0.899; 14: 0.344 / 0.500 / 0.900; 15: 0.345 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.162 (body 0.133, range 0.191); 'price stays where it was' would score 0.186; colour right 0.525; typical miss of the close 6.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.114 (body 0.075, range 0.153); 'price stays where it was' would score 0.118; colour right 0.499; typical miss of the close 11.9 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.123; colour right 0.491; typical miss of the close 10.8 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.164); 'price stays where it was' would score 0.128; colour right 0.500; typical miss of the close 8.1 bp; chain ended on the right side 0.499 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.9 bp; chain ended on the right side 0.516 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.0; 2: 0.200 / 4.6; 3: 0.169 / 6.1; 4: 0.131 / 6.6; 5: 0.125 / 7.3; 6: 0.113 / 7.8; 7: 0.111 / 8.1; 8: 0.098 / 8.8; 9: 0.090 / 8.7; 10: 0.089 / 9.3; 11: 0.085 / 9.7; 12: 0.076 / 10.1; 13: 0.068 / 10.2; 14: 0.070 / 10.7; 15: 0.062 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 132142, probability skill vs chance 0.2323, widened contest next: False
  - now: threshold 0.8386, hit rate recent 0.9144 / long run 0.935
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.265, naive rule 0.439, lift 3.51x
    - 24h: 58 calls (58 a day), hit rate 0.897, chance 0.283, naive rule 0.479, lift 3.17x
    - 7d: 436 calls (62 a day), hit rate 0.936, chance 0.293, naive rule 0.499, lift 3.19x
    - 30d: 1744 calls (58 a day), hit rate 0.934, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.5491, hit rate recent 0.6554 / long run 0.6079
    - 6h: 19 calls (77 a day), hit rate 0.579, chance 0.265, lift 2.19x
    - 24h: 112 calls (112 a day), hit rate 0.652, chance 0.283, lift 2.30x
    - 7d: 879 calls (126 a day), hit rate 0.602, chance 0.293, lift 2.05x
    - 30d: 3051 calls (102 a day), hit rate 0.589, chance 0.294, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 535, 0.523; 0.40: 473, 0.581; 0.45: 404, 0.653; 0.50: 354, 0.702; 0.55: 309, 0.744; 0.60: 262, 0.788; 0.65: 220, 0.813; 0.70: 174, 0.845; 0.75: 138, 0.879; 0.80: 92, 0.912; 0.85: 47, 0.947; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.428; 0.35: 501, 0.464; 0.40: 405, 0.499; 0.45: 308, 0.535; 0.50: 199, 0.572; 0.55: 89, 0.576; 0.60: 12, 0.655; 0.65: 1, 0.636
- **K=5**: model 1792540800, labels learned 132140, probability skill vs chance 0.2355, widened contest next: False
  - now: threshold 0.6873, hit rate recent 0.8214 / long run 0.8211
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.188, naive rule 0.399, lift 4.68x
    - 24h: 69 calls (69 a day), hit rate 0.783, chance 0.192, naive rule 0.424, lift 4.09x
    - 7d: 441 calls (63 a day), hit rate 0.819, chance 0.190, naive rule 0.420, lift 4.32x
    - 30d: 1643 calls (55 a day), hit rate 0.821, chance 0.188, naive rule 0.407, lift 4.37x
  - next: threshold 0.4526, hit rate recent 0.5893 / long run 0.515
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.188, lift 2.65x
    - 24h: 55 calls (55 a day), hit rate 0.582, chance 0.192, lift 3.04x
    - 7d: 397 calls (57 a day), hit rate 0.547, chance 0.190, lift 2.88x
    - 30d: 2774 calls (92 a day), hit rate 0.480, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.427; 0.35: 346, 0.493; 0.40: 279, 0.568; 0.45: 228, 0.621; 0.50: 182, 0.668; 0.55: 144, 0.704; 0.60: 110, 0.751; 0.65: 77, 0.790; 0.70: 50, 0.824; 0.75: 29, 0.868; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.388; 0.35: 256, 0.422; 0.40: 160, 0.462; 0.45: 68, 0.483; 0.50: 13, 0.501; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 132137, probability skill vs chance 0.2117, widened contest next: False
  - now: threshold 0.5709, hit rate recent 0.6792 / long run 0.6933
    - 6h: 15 calls (62 a day), hit rate 0.600, chance 0.149, naive rule 0.394, lift 4.04x
    - 24h: 52 calls (52 a day), hit rate 0.615, chance 0.133, naive rule 0.378, lift 4.62x
    - 7d: 387 calls (55 a day), hit rate 0.718, chance 0.126, naive rule 0.357, lift 5.70x
    - 30d: 1592 calls (53 a day), hit rate 0.687, chance 0.121, naive rule 0.336, lift 5.65x
  - next: threshold 0.364, hit rate recent 0.487 / long run 0.4184
    - 24h: 46 calls (46 a day), hit rate 0.435, chance 0.133, lift 3.26x
    - 7d: 583 calls (83 a day), hit rate 0.434, chance 0.126, lift 3.44x
    - 30d: 2809 calls (94 a day), hit rate 0.392, chance 0.121, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.435; 0.35: 190, 0.501; 0.40: 149, 0.547; 0.45: 114, 0.593; 0.50: 84, 0.638; 0.55: 61, 0.675; 0.60: 41, 0.710; 0.65: 24, 0.783; 0.70: 12, 0.809; 0.75: 2, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.361; 0.35: 91, 0.390; 0.40: 27, 0.424; 0.45: 5, 0.460; 0.50: 1, 0.680
- **K=13**: model 1793577600, labels learned 132132, probability skill vs chance 0.1854, widened contest next: True
  - now: threshold 0.4456, hit rate recent 0.5203 / long run 0.5635
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.080, naive rule 0.259, lift 4.18x
    - 24h: 53 calls (54 a day), hit rate 0.453, chance 0.076, naive rule 0.298, lift 5.92x
    - 7d: 422 calls (60 a day), hit rate 0.581, chance 0.080, naive rule 0.300, lift 7.25x
    - 30d: 1678 calls (56 a day), hit rate 0.560, chance 0.077, naive rule 0.280, lift 7.24x
  - next: threshold 0.2887, hit rate recent 0.4002 / long run 0.3319
    - 6h: 9 calls (38 a day), hit rate 0.556, chance 0.080, lift 6.97x
    - 24h: 49 calls (50 a day), hit rate 0.408, chance 0.076, lift 5.34x
    - 7d: 347 calls (50 a day), hit rate 0.354, chance 0.080, lift 4.43x
    - 30d: 1878 calls (63 a day), hit rate 0.324, chance 0.077, lift 4.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 128, 0.441; 0.35: 92, 0.492; 0.40: 66, 0.544; 0.45: 44, 0.587; 0.50: 29, 0.646; 0.55: 19, 0.677; 0.60: 10, 0.722; 0.65: 3, 0.713; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.330; 0.35: 13, 0.362; 0.40: 3, 0.434; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.085 | 1.17% | 0.917 | 0.467 | 0.257 | 0.407 | 0.298 |
| 6h | 18.130 | 2.19% | 0.914 | 0.506 | 0.251 | 0.479 | 0.438 |
| 24h | 16.411 | 4.46% | 0.901 | 0.500 | 0.250 | 0.513 | 0.550 |
| 7d | 14.954 | 4.95% | 0.901 | 0.500 | 0.250 | 0.507 | 0.744 |
| 30d | 14.182 | 4.35% | 0.900 | 0.500 | 0.251 | 0.498 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.228 | 11.958 | 12.027 | 12.358 | 12.038 | 12.299 | 11.941 | 11.927 | 11.929 | 12.085 |
| 6h | 18.536 | 18.150 | 18.230 | 18.491 | 18.309 | 18.378 | 18.137 | 18.114 | 18.110 | 18.130 |
| 24h | 17.178 | 16.506 | 16.571 | 16.576 | 16.746 | 16.788 | 16.414 | 16.394 | 16.395 | 16.411 |
| 7d | 15.733 | 15.123 | 15.081 | 15.002 | 15.285 | 15.257 | 14.940 | 14.924 | 14.930 | 14.954 |
| 30d | 14.828 | 14.331 | 14.278 | 14.215 | 14.448 | 14.396 | 14.176 | 14.154 | 14.157 | 14.182 |

## Next candle

- candle starting 2026-11-02 22:28 UTC, last close 2250.2
- P(up) 0.4867, return quantiles (bp): {'05': -7.44, '10': -5.836, '25': -3.228, '40': -1.367, '50': -0.128, '60': 0.857, '75': 2.515, '90': 5.474, '95': 7.297}
- changepoint probability 0.0571, regime age 71.7 min
- agent weights: empirical 0.003, ewma 0.143, garch 0.067, har 0.042, bocpd 0.029, hmm 0.012, online_qr 0.325, lgbm 0.380

## Learning log

- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- HMM volatility states (sd, bp per minute): [2.67, 6.37, 20.05], current probabilities: [0.056, 0.93, 0.014]
- live generator: {'versions': 60, 'latest_effective': '2026-11-02 22:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.465, 'l_abs': 0.55, 'l_hi': 0.728, 'l_lo': 0.764, 'b05': 0.65, 'b25': 0.612, 'b75': 0.646, 'b95': 0.655}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.225, 2.684, 3.364, 4.249, 3.669, 6.043, 5.976, 5.633, 6.708, 5.435, 4.945, 5.933, 6.047, 6.026]}
- calibration offsets (in sigma): {'05': 0.0235, '10': -0.023, '25': -0.0925, '40': -0.092, '50': -0.035, '60': -0.018, '75': -0.0375, '90': -0.027, '95': -0.0135}
