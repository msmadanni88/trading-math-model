# ETH-USD 60s candle generator - report

- generated: 2026-10-28 00:05 UTC
- last closed candle: 2026-10-28 00:05 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.537 (672) [0.501, 0.574] | 0.520 (2876) [0.500, 0.539] | 0.517 (5370) [0.503, 0.530] | 0.523 (2398) [0.501, 0.546] | - | 0.500 | flat +0.003 (noise 0.032) |
| colour_clear | 0.556 (840) | 0.544 (5696) [0.540, 0.549] | 0.537 (23618) [0.530, 0.544] | 0.519 (43957) [0.512, 0.525] | 0.546 (19719) [0.542, 0.551] | 0.750 (4) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.596 (161) | 0.604 (1371) [0.591, 0.619] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.000 (2) | 0.500 | flat +0.010 (noise 0.021) |
| colour_next | 0.530 (1430) | 0.528 (10030) [0.525, 0.532] | 0.525 (42880) [0.521, 0.530] | 0.513 (80052) [0.509, 0.517] | 0.529 (35703) [0.525, 0.533] | 0.600 (5) | 0.500 | flat -0.007 (noise 0.007) |
| colour_path | 0.506 (20020) | 0.502 (140420) [0.500, 0.504] | 0.501 (600320) [0.499, 0.503] | 0.501 (1120728) [0.500, 0.502] | 0.501 (499842) [0.499, 0.502] | 0.471 (70) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.596 (47) | 0.614 (412) [0.596, 0.644] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | - | 0.500 | flat -0.015 (noise 0.041) |
| reversal_k13_next | 0.451 (51) | 0.321 (417) [0.287, 0.360] | 0.309 (2160) [0.297, 0.322] | 0.309 (3794) [0.298, 0.320] | 0.320 (1689) [0.308, 0.333] | - | 0.077 | flat +0.007 (noise 0.032) |
| reversal_k13_now | 0.643 (56) | 0.565 (375) [0.516, 0.620] | 0.561 (1611) [0.541, 0.582] | 0.572 (2832) [0.557, 0.588] | 0.563 (1360) [0.541, 0.587] | - | 0.077 | flat +0.046 (noise 0.036) |
| reversal_k3_next | 0.569 (123) | 0.607 (679) [0.587, 0.629] | 0.584 (2878) [0.572, 0.597] | 0.584 (4882) [0.574, 0.594] | 0.580 (2442) [0.567, 0.593] | 1.000 (1) | 0.293 | flat +0.045 (noise 0.026) |
| reversal_k3_now | 0.969 (65) | 0.955 (397) [0.931, 0.974] | 0.937 (1714) [0.927, 0.946] | 0.939 (3191) [0.932, 0.946] | 0.935 (1428) [0.924, 0.946] | - | 0.293 | flat +0.025 (noise 0.019) |
| reversal_k5_next | 0.530 (66) | 0.499 (830) [0.489, 0.511] | 0.467 (3054) [0.453, 0.480] | 0.478 (4619) [0.466, 0.490] | 0.466 (2629) [0.451, 0.481] | - | 0.187 | up +0.060 (noise 0.024) |
| reversal_k5_now | 0.845 (58) | 0.821 (369) [0.809, 0.833] | 0.826 (1581) [0.814, 0.837] | 0.830 (2932) [0.820, 0.841] | 0.821 (1321) [0.809, 0.834] | - | 0.187 | flat -0.001 (noise 0.028) |
| reversal_k8_next | 0.396 (101) | 0.382 (747) [0.362, 0.400] | 0.381 (2684) [0.369, 0.394] | 0.388 (4517) [0.377, 0.399] | 0.381 (2411) [0.368, 0.394] | - | 0.120 | flat +0.020 (noise 0.025) |
| reversal_k8_now | 0.732 (56) | 0.674 (356) [0.624, 0.726] | 0.686 (1533) [0.665, 0.705] | 0.700 (2898) [0.685, 0.715] | 0.683 (1311) [0.660, 0.706] | - | 0.121 | flat +0.010 (noise 0.037) |
| overall | 0.510 (22122) | 0.506 (155292) [0.503, 0.508] | 0.504 (663291) [0.503, 0.506] | 0.503 (1235815) [0.502, 0.504] | 0.504 (552534) [0.503, 0.506] | 0.487 (76) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08028, 0.121] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5277, 'levels': [{'threshold': 0.08028, 'calls_per_day': 145.3, 'win_rate': 0.6086}, {'threshold': 0.121, 'calls_per_day': 36.4, 'win_rate': 0.6133}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 34569, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14882 | 0.338 | 0.523 (14656) | 0.586 (1827) | 0.758 (2507) |
| volatility: normal | 14881 | 0.366 | 0.529 (14812) | 0.614 (1304) | 0.751 (2188) |
| volatility: wild | 14882 | 0.380 | 0.522 (14839) | 0.623 (653) | 0.768 (1933) |
| session: Asia 00-08 | 14885 | 0.360 | 0.531 (14781) | 0.608 (1326) | 0.760 (2172) |
| session: Europe 08-13 | 9300 | 0.357 | 0.529 (9217) | 0.596 (931) | 0.754 (1508) |
| session: US 13-21 | 14880 | 0.369 | 0.520 (14783) | 0.597 (976) | 0.769 (2111) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5526) | 0.608 (551) | 0.736 (837) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.381 | 0.332 | 0.296 | 0.296 | 0.617 | 0.311 | 0.450 | 1.383 |
| 6h | 360 | 0.347 | 0.343 | 0.292 | 0.335 | 0.514 | 0.247 | 0.448 | 1.354 |
| 24h | 1440 | 0.370 | 0.362 | 0.293 | 0.325 | 0.531 | 0.261 | 0.479 | 1.242 |
| 7d | 10080 | 0.368 | 0.358 | 0.281 | 0.312 | 0.528 | 0.265 | 0.472 | 1.231 |
| 30d | 43200 | 0.362 | 0.355 | 0.278 | 0.307 | 0.525 | 0.258 | 0.465 | 1.278 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.381 / 0.617 / 0.900; 2: 0.291 / 0.333 / 0.900; 3: 0.377 / 0.533 / 0.867; 4: 0.347 / 0.483 / 0.917; 5: 0.376 / 0.583 / 0.917; 6: 0.366 / 0.533 / 0.950; 7: 0.376 / 0.567 / 0.933; 8: 0.382 / 0.567 / 0.933; 9: 0.308 / 0.383 / 0.867; 10: 0.374 / 0.567 / 0.850; 11: 0.356 / 0.450 / 0.883; 12: 0.350 / 0.483 / 0.867; 13: 0.331 / 0.417 / 0.867; 14: 0.383 / 0.600 / 0.900; 15: 0.337 / 0.383 / 0.867
- 6h: 1: 0.347 / 0.514 / 0.883; 2: 0.333 / 0.466 / 0.883; 3: 0.355 / 0.520 / 0.894; 4: 0.347 / 0.486 / 0.911; 5: 0.361 / 0.547 / 0.903; 6: 0.339 / 0.508 / 0.900; 7: 0.353 / 0.511 / 0.911; 8: 0.361 / 0.536 / 0.911; 9: 0.330 / 0.483 / 0.903; 10: 0.354 / 0.528 / 0.919; 11: 0.341 / 0.492 / 0.908; 12: 0.340 / 0.472 / 0.903; 13: 0.345 / 0.500 / 0.908; 14: 0.359 / 0.567 / 0.919; 15: 0.344 / 0.489 / 0.906
- 24h: 1: 0.370 / 0.531 / 0.890; 2: 0.360 / 0.490 / 0.900; 3: 0.369 / 0.518 / 0.903; 4: 0.359 / 0.488 / 0.898; 5: 0.365 / 0.530 / 0.902; 6: 0.357 / 0.510 / 0.902; 7: 0.361 / 0.509 / 0.906; 8: 0.365 / 0.516 / 0.908; 9: 0.353 / 0.490 / 0.906; 10: 0.363 / 0.514 / 0.910; 11: 0.358 / 0.513 / 0.911; 12: 0.358 / 0.494 / 0.911; 13: 0.360 / 0.509 / 0.915; 14: 0.362 / 0.515 / 0.914; 15: 0.355 / 0.483 / 0.912
- 7d: 1: 0.368 / 0.528 / 0.895; 2: 0.356 / 0.495 / 0.900; 3: 0.359 / 0.512 / 0.900; 4: 0.354 / 0.498 / 0.900; 5: 0.356 / 0.510 / 0.900; 6: 0.353 / 0.501 / 0.900; 7: 0.353 / 0.501 / 0.901; 8: 0.355 / 0.511 / 0.901; 9: 0.353 / 0.500 / 0.900; 10: 0.353 / 0.505 / 0.901; 11: 0.350 / 0.498 / 0.900; 12: 0.352 / 0.504 / 0.900; 13: 0.350 / 0.498 / 0.901; 14: 0.351 / 0.499 / 0.901; 15: 0.351 / 0.502 / 0.901
- 30d: 1: 0.362 / 0.525 / 0.898; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.498 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.347 / 0.496 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.150 (body 0.120, range 0.180); 'price stays where it was' would score 0.173; colour right 0.383; typical miss of the close 6.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.081, range 0.169); 'price stays where it was' would score 0.148; colour right 0.475; typical miss of the close 6.5 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.128 (body 0.083, range 0.173); 'price stays where it was' would score 0.139; colour right 0.491; typical miss of the close 8.5 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.130 (body 0.088, range 0.171); 'price stays where it was' would score 0.138; colour right 0.498; typical miss of the close 8.5 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.128; colour right 0.497; typical miss of the close 7.9 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.1; 2: 0.198 / 4.6; 3: 0.170 / 6.1; 4: 0.132 / 6.6; 5: 0.125 / 7.3; 6: 0.112 / 7.8; 7: 0.107 / 8.2; 8: 0.095 / 8.6; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.086 / 9.8; 12: 0.077 / 10.0; 13: 0.068 / 10.3; 14: 0.070 / 10.6; 15: 0.061 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 123599, probability skill vs chance 0.2416, widened contest next: False
  - now: threshold 0.8347, hit rate recent 0.9671 / long run 0.9416
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.261, naive rule 0.415, lift 3.84x
    - 24h: 64 calls (64 a day), hit rate 0.969, chance 0.288, naive rule 0.476, lift 3.36x
    - 7d: 397 calls (57 a day), hit rate 0.955, chance 0.297, naive rule 0.503, lift 3.21x
    - 30d: 1714 calls (57 a day), hit rate 0.937, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5326, hit rate recent 0.5701 / long run 0.5868
    - 6h: 34 calls (138 a day), hit rate 0.500, chance 0.261, lift 1.92x
    - 24h: 124 calls (124 a day), hit rate 0.573, chance 0.288, lift 1.99x
    - 7d: 680 calls (97 a day), hit rate 0.607, chance 0.297, lift 2.04x
    - 30d: 2879 calls (96 a day), hit rate 0.584, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 537, 0.519; 0.40: 477, 0.576; 0.45: 408, 0.647; 0.50: 357, 0.698; 0.55: 312, 0.740; 0.60: 264, 0.785; 0.65: 221, 0.811; 0.70: 174, 0.843; 0.75: 136, 0.875; 0.80: 91, 0.914; 0.85: 47, 0.952; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 501, 0.466; 0.40: 408, 0.500; 0.45: 310, 0.534; 0.50: 200, 0.570; 0.55: 89, 0.575; 0.60: 13, 0.643; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 123597, probability skill vs chance 0.2235, widened contest next: False
  - now: threshold 0.6717, hit rate recent 0.8386 / long run 0.8241
    - 6h: 6 calls (24 a day), hit rate 0.833, chance 0.201, naive rule 0.384, lift 4.14x
    - 24h: 57 calls (57 a day), hit rate 0.860, chance 0.195, naive rule 0.413, lift 4.40x
    - 7d: 368 calls (53 a day), hit rate 0.821, chance 0.186, naive rule 0.408, lift 4.41x
    - 30d: 1581 calls (53 a day), hit rate 0.826, chance 0.188, naive rule 0.401, lift 4.40x
  - next: threshold 0.4475, hit rate recent 0.5119 / long run 0.4857
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.201, lift 2.24x
    - 24h: 66 calls (66 a day), hit rate 0.530, chance 0.195, lift 2.71x
    - 7d: 830 calls (119 a day), hit rate 0.499, chance 0.186, lift 2.68x
    - 30d: 3054 calls (102 a day), hit rate 0.467, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 345, 0.492; 0.40: 278, 0.566; 0.45: 226, 0.619; 0.50: 178, 0.668; 0.55: 138, 0.709; 0.60: 106, 0.751; 0.65: 76, 0.788; 0.70: 51, 0.828; 0.75: 30, 0.873; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.390; 0.35: 253, 0.421; 0.40: 158, 0.454; 0.45: 70, 0.471; 0.50: 15, 0.489; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 123594, probability skill vs chance 0.2039, widened contest next: False
  - now: threshold 0.5577, hit rate recent 0.6883 / long run 0.6785
    - 6h: 6 calls (25 a day), hit rate 0.833, chance 0.130, naive rule 0.340, lift 6.41x
    - 24h: 55 calls (55 a day), hit rate 0.745, chance 0.129, naive rule 0.360, lift 5.76x
    - 7d: 356 calls (51 a day), hit rate 0.674, chance 0.118, naive rule 0.329, lift 5.73x
    - 30d: 1533 calls (51 a day), hit rate 0.686, chance 0.121, naive rule 0.331, lift 5.67x
  - next: threshold 0.3349, hit rate recent 0.3856 / long run 0.3782
    - 6h: 25 calls (103 a day), hit rate 0.400, chance 0.130, lift 3.08x
    - 24h: 101 calls (102 a day), hit rate 0.396, chance 0.129, lift 3.06x
    - 7d: 747 calls (107 a day), hit rate 0.382, chance 0.118, lift 3.24x
    - 30d: 2684 calls (89 a day), hit rate 0.381, chance 0.121, lift 3.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.428; 0.35: 188, 0.496; 0.40: 145, 0.546; 0.45: 111, 0.591; 0.50: 84, 0.633; 0.55: 60, 0.670; 0.60: 40, 0.712; 0.65: 23, 0.781; 0.70: 10, 0.824; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.355; 0.35: 94, 0.382; 0.40: 33, 0.405; 0.45: 7, 0.426; 0.50: 1, 0.600
- **K=13**: model 1793059200, labels learned 123589, probability skill vs chance 0.202, widened contest next: False
  - now: threshold 0.4049, hit rate recent 0.5958 / long run 0.5586
    - 6h: 9 calls (38 a day), hit rate 0.778, chance 0.087, naive rule 0.311, lift 8.94x
    - 24h: 55 calls (56 a day), hit rate 0.655, chance 0.085, naive rule 0.328, lift 7.71x
    - 7d: 374 calls (54 a day), hit rate 0.564, chance 0.075, naive rule 0.275, lift 7.57x
    - 30d: 1611 calls (54 a day), hit rate 0.561, chance 0.077, naive rule 0.274, lift 7.29x
  - next: threshold 0.2947, hit rate recent 0.3789 / long run 0.3211
    - 6h: 14 calls (58 a day), hit rate 0.357, chance 0.087, lift 4.11x
    - 24h: 51 calls (52 a day), hit rate 0.451, chance 0.085, lift 5.31x
    - 7d: 417 calls (60 a day), hit rate 0.321, chance 0.075, lift 4.31x
    - 30d: 2159 calls (72 a day), hit rate 0.309, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.440; 0.35: 89, 0.491; 0.40: 63, 0.546; 0.45: 42, 0.597; 0.50: 26, 0.657; 0.55: 16, 0.706; 0.60: 7, 0.749; 0.65: 2, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.361; 0.40: 2, 0.451; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.507 | 2.75% | 0.900 | 0.450 | 0.250 | 0.417 | -0.025 |
| 6h | 10.863 | 2.74% | 0.897 | 0.519 | 0.251 | 0.486 | 0.471 |
| 24h | 13.659 | 1.66% | 0.898 | 0.506 | 0.250 | 0.494 | 0.527 |
| 7d | 14.765 | 3.40% | 0.900 | 0.500 | 0.250 | 0.500 | 0.652 |
| 30d | 13.848 | 4.11% | 0.900 | 0.500 | 0.251 | 0.495 | 0.666 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.775 | 9.473 | 9.594 | 9.479 | 9.608 | 9.532 | 9.453 | 9.490 | 9.472 | 9.507 |
| 6h | 11.169 | 10.919 | 10.948 | 10.883 | 11.031 | 10.879 | 10.825 | 10.865 | 10.839 | 10.863 |
| 24h | 13.889 | 13.735 | 13.722 | 13.704 | 13.874 | 13.721 | 13.634 | 13.613 | 13.627 | 13.659 |
| 7d | 15.286 | 14.908 | 14.853 | 14.793 | 15.029 | 14.908 | 14.750 | 14.726 | 14.736 | 14.765 |
| 30d | 14.442 | 13.982 | 13.933 | 13.874 | 14.095 | 14.026 | 13.842 | 13.823 | 13.822 | 13.848 |

## Next candle

- candle starting 2026-10-28 00:05 UTC, last close 2344.88
- P(up) 0.508, return quantiles (bp): {'05': -6.53, '10': -5.102, '25': -2.572, '40': -0.857, '50': 0.073, '60': 1.007, '75': 2.486, '90': 5.023, '95': 7.026}
- changepoint probability 0.0458, regime age 98.6 min
- agent weights: empirical 0.019, ewma 0.097, garch 0.099, har 0.129, bocpd 0.032, hmm 0.130, online_qr 0.259, lgbm 0.237

## Learning log

- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.41, 6.59, 17.7], current probabilities: [0.936, 0.062, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-28 00:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.256, 'l_abs': 0.706, 'l_hi': 0.761, 'l_lo': 0.784, 'b05': 0.734, 'b25': 0.774, 'b75': 0.597, 'b95': 0.683}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8]], 'cone_width': [1.475, 1.739, 2.053, 2.209, 2.33, 2.423, 2.494, 2.929, 2.972, 3.062, 3.335, 3.276, 3.339, 3.604]}
- calibration offsets (in sigma): {'05': 0.042, '10': 0.004, '25': 0.0, '40': 0.016, '50': 0.0, '60': -0.006, '75': -0.04, '90': -0.054, '95': 0.058}
