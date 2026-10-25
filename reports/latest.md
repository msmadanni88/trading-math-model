# ETH-USD 60s candle generator - report

- generated: 2026-10-25 23:57 UTC
- last closed candle: 2026-10-25 23:57 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.543 (672) [0.509, 0.577] | 0.517 (2876) [0.498, 0.536] | 0.515 (5082) [0.500, 0.528] | 0.519 (2110) [0.495, 0.543] | 0.653 (95) | 0.500 | flat +0.040 (noise 0.027) |
| colour_clear | 0.544 (743) | 0.553 (5669) [0.547, 0.562] | 0.533 (23412) [0.525, 0.541] | 0.517 (41491) [0.511, 0.524] | 0.547 (17253) [0.542, 0.552] | 0.534 (802) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.606 (269) | 0.608 (1282) [0.589, 0.628] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.577 (267) | 0.500 | flat +0.016 (noise 0.023) |
| colour_next | 0.522 (1431) | 0.534 (10039) [0.527, 0.541] | 0.523 (42853) [0.517, 0.528] | 0.513 (75756) [0.508, 0.517] | 0.530 (31407) [0.525, 0.534] | 0.523 (1431) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.501 (140546) [0.498, 0.503] | 0.501 (599942) [0.499, 0.502] | 0.501 (1060584) [0.500, 0.501] | 0.500 (439698) [0.498, 0.502] | 0.506 (20034) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.602 (98) | 0.636 (335) [0.607, 0.672] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.589 (107) | 0.500 | flat -0.005 (noise 0.045) |
| reversal_k13_next | 0.286 (63) | 0.310 (481) [0.291, 0.327] | 0.305 (2173) [0.292, 0.317] | 0.306 (3618) [0.296, 0.318] | 0.316 (1513) [0.305, 0.327] | 0.364 (66) | 0.077 | flat +0.004 (noise 0.031) |
| reversal_k13_now | 0.647 (51) | 0.530 (366) [0.490, 0.576] | 0.570 (1560) [0.549, 0.591] | 0.573 (2651) [0.557, 0.590] | 0.564 (1179) [0.540, 0.590] | 0.600 (55) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.630 (54) | 0.592 (699) [0.564, 0.624] | 0.580 (2792) [0.566, 0.594] | 0.584 (4562) [0.573, 0.594] | 0.580 (2122) [0.565, 0.596] | 0.588 (80) | 0.293 | flat +0.024 (noise 0.026) |
| reversal_k3_now | 0.980 (49) | 0.945 (397) [0.928, 0.962] | 0.938 (1690) [0.929, 0.947] | 0.938 (3023) [0.932, 0.945] | 0.933 (1260) [0.923, 0.944] | 0.870 (46) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.480 (125) | 0.460 (939) [0.433, 0.486] | 0.464 (2842) [0.449, 0.479] | 0.476 (4306) [0.463, 0.489] | 0.460 (2316) [0.445, 0.476] | 0.496 (137) | 0.187 | flat -0.006 (noise 0.025) |
| reversal_k5_now | 0.818 (55) | 0.812 (361) [0.800, 0.823] | 0.831 (1561) [0.818, 0.844] | 0.830 (2771) [0.819, 0.841] | 0.819 (1160) [0.804, 0.833] | 0.837 (49) | 0.187 | flat -0.006 (noise 0.029) |
| reversal_k8_next | 0.384 (86) | 0.377 (757) [0.359, 0.394] | 0.383 (2519) [0.370, 0.396] | 0.389 (4187) [0.377, 0.400] | 0.381 (2081) [0.367, 0.395] | 0.403 (119) | 0.120 | flat +0.004 (noise 0.026) |
| reversal_k8_now | 0.709 (55) | 0.654 (332) [0.613, 0.693] | 0.701 (1523) [0.681, 0.722] | 0.702 (2739) [0.686, 0.718] | 0.685 (1152) [0.662, 0.708] | 0.729 (48) | 0.121 | flat -0.031 (noise 0.036) |
| overall | 0.505 (22099) | 0.504 (155589) [0.501, 0.507] | 0.504 (662331) [0.502, 0.505] | 0.503 (1169279) [0.502, 0.504] | 0.504 (485998) [0.502, 0.506] | 0.509 (22160) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07634, 0.1134] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5356, 'levels': [{'threshold': 0.07634, 'calls_per_day': 150.8, 'win_rate': 0.6138}, {'threshold': 0.1134, 'calls_per_day': 39.3, 'win_rate': 0.6522}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 31699, 'rate': 0.5306}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15359 | 0.336 | 0.524 (15110) | 0.588 (1742) | 0.761 (2536) |
| volatility: normal | 15359 | 0.364 | 0.522 (15291) | 0.607 (1184) | 0.759 (2260) |
| volatility: wild | 15359 | 0.378 | 0.519 (15319) | 0.637 (534) | 0.770 (1937) |
| session: Asia 00-08 | 15360 | 0.357 | 0.527 (15256) | 0.607 (1220) | 0.766 (2206) |
| session: Europe 08-13 | 9600 | 0.355 | 0.524 (9513) | 0.598 (858) | 0.761 (1524) |
| session: US 13-21 | 15360 | 0.367 | 0.518 (15258) | 0.599 (867) | 0.771 (2162) |
| session: late 21-24 | 5757 | 0.351 | 0.513 (5693) | 0.606 (515) | 0.736 (841) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.393 | 0.378 | 0.344 | 0.344 | 0.542 | 0.310 | 0.475 | 0.934 |
| 6h | 360 | 0.349 | 0.339 | 0.275 | 0.297 | 0.501 | 0.252 | 0.446 | 1.142 |
| 24h | 1440 | 0.349 | 0.338 | 0.266 | 0.287 | 0.523 | 0.261 | 0.437 | 1.267 |
| 7d | 10080 | 0.370 | 0.360 | 0.274 | 0.306 | 0.535 | 0.269 | 0.471 | 1.207 |
| 30d | 43200 | 0.359 | 0.353 | 0.276 | 0.304 | 0.524 | 0.257 | 0.462 | 1.287 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.393 / 0.542 / 0.833; 2: 0.364 / 0.475 / 0.917; 3: 0.366 / 0.542 / 0.867; 4: 0.367 / 0.525 / 0.817; 5: 0.338 / 0.458 / 0.750; 6: 0.354 / 0.559 / 0.700; 7: 0.374 / 0.610 / 0.683; 8: 0.345 / 0.508 / 0.700; 9: 0.346 / 0.525 / 0.717; 10: 0.343 / 0.475 / 0.750; 11: 0.359 / 0.559 / 0.800; 12: 0.353 / 0.559 / 0.750; 13: 0.325 / 0.441 / 0.800; 14: 0.343 / 0.475 / 0.817; 15: 0.335 / 0.458 / 0.850
- 6h: 1: 0.349 / 0.501 / 0.878; 2: 0.335 / 0.457 / 0.883; 3: 0.346 / 0.529 / 0.906; 4: 0.343 / 0.513 / 0.897; 5: 0.334 / 0.471 / 0.900; 6: 0.342 / 0.538 / 0.875; 7: 0.346 / 0.524 / 0.867; 8: 0.341 / 0.541 / 0.889; 9: 0.344 / 0.521 / 0.889; 10: 0.337 / 0.501 / 0.897; 11: 0.349 / 0.543 / 0.897; 12: 0.338 / 0.527 / 0.903; 13: 0.342 / 0.529 / 0.917; 14: 0.318 / 0.431 / 0.925; 15: 0.324 / 0.476 / 0.936
- 24h: 1: 0.349 / 0.523 / 0.883; 2: 0.335 / 0.493 / 0.894; 3: 0.337 / 0.505 / 0.897; 4: 0.341 / 0.531 / 0.895; 5: 0.331 / 0.490 / 0.894; 6: 0.338 / 0.520 / 0.894; 7: 0.335 / 0.508 / 0.892; 8: 0.335 / 0.516 / 0.897; 9: 0.333 / 0.490 / 0.899; 10: 0.333 / 0.502 / 0.899; 11: 0.336 / 0.522 / 0.903; 12: 0.333 / 0.525 / 0.904; 13: 0.330 / 0.501 / 0.907; 14: 0.325 / 0.487 / 0.909; 15: 0.328 / 0.487 / 0.910
- 7d: 1: 0.370 / 0.535 / 0.898; 2: 0.357 / 0.502 / 0.899; 3: 0.357 / 0.509 / 0.899; 4: 0.353 / 0.496 / 0.899; 5: 0.353 / 0.501 / 0.900; 6: 0.353 / 0.498 / 0.900; 7: 0.351 / 0.494 / 0.899; 8: 0.354 / 0.511 / 0.900; 9: 0.352 / 0.498 / 0.900; 10: 0.352 / 0.506 / 0.900; 11: 0.351 / 0.501 / 0.900; 12: 0.351 / 0.504 / 0.901; 13: 0.349 / 0.495 / 0.901; 14: 0.349 / 0.494 / 0.901; 15: 0.349 / 0.500 / 0.902
- 30d: 1: 0.359 / 0.524 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.347 / 0.498 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.346 / 0.499 / 0.900; 7: 0.346 / 0.500 / 0.899; 8: 0.346 / 0.503 / 0.900; 9: 0.344 / 0.496 / 0.900; 10: 0.346 / 0.505 / 0.900; 11: 0.344 / 0.499 / 0.900; 12: 0.345 / 0.504 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.343 / 0.498 / 0.900; 15: 0.344 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.087 (body 0.065, range 0.109); 'price stays where it was' would score 0.057; colour right 0.559; typical miss of the close 16.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.114 (body 0.080, range 0.148); 'price stays where it was' would score 0.103; colour right 0.529; typical miss of the close 7.1 bp; chain ended on the right side 0.708 of 24 chains; n=360
- 24h: match 0.124 (body 0.089, range 0.159); 'price stays where it was' would score 0.123; colour right 0.492; typical miss of the close 6.7 bp; chain ended on the right side 0.646 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.168); 'price stays where it was' would score 0.133; colour right 0.501; typical miss of the close 8.7 bp; chain ended on the right side 0.549 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.5 bp; chain ended on the right side 0.525 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.195 / 4.4; 3: 0.166 / 5.7; 4: 0.132 / 6.3; 5: 0.122 / 7.0; 6: 0.111 / 7.5; 7: 0.106 / 7.8; 8: 0.097 / 8.1; 9: 0.087 / 8.1; 10: 0.088 / 8.8; 11: 0.084 / 9.3; 12: 0.077 / 9.6; 13: 0.068 / 9.7; 14: 0.069 / 10.2; 15: 0.059 / 10.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 120711, probability skill vs chance 0.2259, widened contest next: False
  - now: threshold 0.8342, hit rate recent 0.9091 / long run 0.934
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.294, naive rule 0.502, lift 2.61x
    - 24h: 46 calls (46 a day), hit rate 0.870, chance 0.298, naive rule 0.518, lift 2.92x
    - 7d: 388 calls (55 a day), hit rate 0.936, chance 0.296, naive rule 0.501, lift 3.16x
    - 30d: 1685 calls (56 a day), hit rate 0.935, chance 0.294, naive rule 0.493, lift 3.18x
  - next: threshold 0.537, hit rate recent 0.5834 / long run 0.5904
    - 6h: 31 calls (126 a day), hit rate 0.581, chance 0.294, lift 1.97x
    - 24h: 80 calls (80 a day), hit rate 0.588, chance 0.298, lift 1.97x
    - 7d: 678 calls (97 a day), hit rate 0.593, chance 0.296, lift 2.00x
    - 30d: 2811 calls (94 a day), hit rate 0.580, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.496; 0.35: 538, 0.520; 0.40: 478, 0.576; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 311, 0.741; 0.60: 263, 0.785; 0.65: 220, 0.811; 0.70: 174, 0.842; 0.75: 135, 0.875; 0.80: 91, 0.914; 0.85: 46, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.426; 0.35: 502, 0.464; 0.40: 408, 0.498; 0.45: 311, 0.534; 0.50: 202, 0.568; 0.55: 91, 0.574; 0.60: 14, 0.622; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 120709, probability skill vs chance 0.2114, widened contest next: False
  - now: threshold 0.6724, hit rate recent 0.8203 / long run 0.821
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.188, naive rule 0.399, lift 4.17x
    - 24h: 49 calls (49 a day), hit rate 0.837, chance 0.177, naive rule 0.401, lift 4.72x
    - 7d: 363 calls (52 a day), hit rate 0.818, chance 0.183, naive rule 0.404, lift 4.46x
    - 30d: 1563 calls (52 a day), hit rate 0.831, chance 0.187, naive rule 0.400, lift 4.44x
  - next: threshold 0.4195, hit rate recent 0.4802 / long run 0.4751
    - 6h: 35 calls (143 a day), hit rate 0.457, chance 0.188, lift 2.43x
    - 24h: 137 calls (138 a day), hit rate 0.496, chance 0.177, lift 2.80x
    - 7d: 924 calls (132 a day), hit rate 0.470, chance 0.183, lift 2.56x
    - 30d: 2951 calls (98 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.426; 0.35: 343, 0.494; 0.40: 276, 0.566; 0.45: 223, 0.621; 0.50: 176, 0.671; 0.55: 136, 0.711; 0.60: 104, 0.755; 0.65: 76, 0.793; 0.70: 53, 0.832; 0.75: 31, 0.877; 0.80: 10, 0.899
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.388; 0.35: 252, 0.420; 0.40: 158, 0.452; 0.45: 70, 0.463; 0.50: 15, 0.488; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 120706, probability skill vs chance 0.2023, widened contest next: False
  - now: threshold 0.556, hit rate recent 0.6982 / long run 0.6854
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.124, naive rule 0.354, lift 5.12x
    - 24h: 48 calls (48 a day), hit rate 0.729, chance 0.111, naive rule 0.324, lift 6.58x
    - 7d: 337 calls (48 a day), hit rate 0.665, chance 0.116, naive rule 0.322, lift 5.74x
    - 30d: 1525 calls (51 a day), hit rate 0.698, chance 0.121, naive rule 0.330, lift 5.78x
  - next: threshold 0.3369, hit rate recent 0.4041 / long run 0.3831
    - 6h: 27 calls (111 a day), hit rate 0.407, chance 0.124, lift 3.28x
    - 24h: 119 calls (120 a day), hit rate 0.403, chance 0.111, lift 3.64x
    - 7d: 759 calls (109 a day), hit rate 0.378, chance 0.116, lift 3.27x
    - 30d: 2589 calls (86 a day), hit rate 0.382, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 188, 0.497; 0.40: 144, 0.549; 0.45: 110, 0.596; 0.50: 84, 0.638; 0.55: 61, 0.675; 0.60: 41, 0.722; 0.65: 23, 0.789; 0.70: 10, 0.828; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.352; 0.35: 97, 0.379; 0.40: 36, 0.398; 0.45: 8, 0.424; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 120701, probability skill vs chance 0.1793, widened contest next: False
  - now: threshold 0.4056, hit rate recent 0.6033 / long run 0.562
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.071, naive rule 0.273, lift 8.05x
    - 24h: 55 calls (56 a day), hit rate 0.600, chance 0.066, naive rule 0.236, lift 9.14x
    - 7d: 357 calls (51 a day), hit rate 0.552, chance 0.073, naive rule 0.267, lift 7.51x
    - 30d: 1575 calls (53 a day), hit rate 0.569, chance 0.077, naive rule 0.272, lift 7.39x
  - next: threshold 0.2946, hit rate recent 0.337 / long run 0.3137
    - 6h: 9 calls (38 a day), hit rate 0.333, chance 0.071, lift 4.69x
    - 24h: 66 calls (67 a day), hit rate 0.364, chance 0.066, lift 5.54x
    - 7d: 466 calls (67 a day), hit rate 0.318, chance 0.073, lift 4.32x
    - 30d: 2171 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.444; 0.35: 87, 0.495; 0.40: 62, 0.553; 0.45: 41, 0.604; 0.50: 26, 0.660; 0.55: 15, 0.702; 0.60: 7, 0.744; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.315; 0.35: 14, 0.346; 0.40: 2, 0.420; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 29.347 | 13.61% | 0.850 | 0.450 | 0.249 | 0.542 | 0.532 |
| 6h | 14.592 | 7.51% | 0.878 | 0.503 | 0.250 | 0.510 | 0.711 |
| 24h | 12.191 | 3.69% | 0.885 | 0.490 | 0.250 | 0.494 | 0.624 |
| 7d | 14.867 | 3.35% | 0.899 | 0.499 | 0.250 | 0.502 | 0.651 |
| 30d | 13.323 | 4.20% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 33.971 | 30.368 | 30.168 | 29.419 | 30.905 | 29.405 | 29.434 | 29.387 | 29.410 | 29.347 |
| 6h | 15.776 | 14.898 | 14.710 | 14.579 | 15.109 | 14.668 | 14.619 | 14.593 | 14.573 | 14.592 |
| 24h | 12.659 | 12.378 | 12.296 | 12.215 | 12.571 | 12.392 | 12.184 | 12.142 | 12.166 | 12.191 |
| 7d | 15.382 | 15.017 | 14.949 | 14.883 | 15.153 | 15.014 | 14.855 | 14.829 | 14.839 | 14.867 |
| 30d | 13.908 | 13.454 | 13.407 | 13.347 | 13.568 | 13.514 | 13.319 | 13.300 | 13.299 | 13.323 |

## Next candle

- candle starting 2026-10-25 23:57 UTC, last close 2328.06
- P(up) 0.4706, return quantiles (bp): {'05': -18.64, '10': -14.308, '25': -8.317, '40': -3.716, '50': -0.889, '60': 2.177, '75': 5.991, '90': 12.252, '95': 16.876}
- changepoint probability 0.0912, regime age 28.1 min
- agent weights: empirical 0.003, ewma 0.020, garch 0.065, har 0.213, bocpd 0.004, hmm 0.079, online_qr 0.241, lgbm 0.376

## Learning log

- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.8, 19.68], current probabilities: [0.046, 0.881, 0.074]
- live generator: {'versions': 60, 'latest_effective': '2026-10-26 00:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.492, 'l_abs': 0.734, 'l_hi': 0.768, 'l_lo': 0.761, 'b05': 0.715, 'b25': 0.723, 'b75': 0.672, 'b95': 0.678}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.6], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.69, 2.074, 2.448, 2.688, 3.133, 3.6, 3.489, 3.783, 4.077, 4.284, 4.395, 4.404, 4.313, 4.212]}
- calibration offsets (in sigma): {'05': -0.052, '10': -0.094, '25': -0.11, '40': -0.076, '50': -0.06, '60': -0.014, '75': -0.04, '90': -0.026, '95': -0.008}
