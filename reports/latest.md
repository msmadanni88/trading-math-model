# ETH-USD 60s candle generator - report

- generated: 2026-10-25 21:56 UTC
- last closed candle: 2026-10-25 21:56 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.543 (672) [0.509, 0.577] | 0.517 (2876) [0.498, 0.536] | 0.515 (5082) [0.500, 0.528] | 0.519 (2110) [0.495, 0.543] | 0.644 (87) | 0.500 | flat +0.040 (noise 0.027) |
| colour_clear | 0.544 (743) | 0.553 (5669) [0.547, 0.562] | 0.533 (23412) [0.525, 0.541] | 0.517 (41491) [0.511, 0.524] | 0.547 (17253) [0.542, 0.552] | 0.536 (729) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.606 (269) | 0.608 (1282) [0.589, 0.628] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.580 (257) | 0.500 | flat +0.016 (noise 0.023) |
| colour_next | 0.522 (1431) | 0.534 (10039) [0.527, 0.541] | 0.523 (42853) [0.517, 0.528] | 0.513 (75756) [0.508, 0.517] | 0.530 (31407) [0.525, 0.534] | 0.525 (1311) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.501 (140546) [0.498, 0.503] | 0.501 (599942) [0.499, 0.502] | 0.501 (1060584) [0.500, 0.501] | 0.500 (439698) [0.498, 0.502] | 0.506 (18354) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.602 (98) | 0.636 (335) [0.607, 0.672] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.608 (102) | 0.500 | flat -0.005 (noise 0.045) |
| reversal_k13_next | 0.286 (63) | 0.310 (481) [0.291, 0.327] | 0.305 (2173) [0.292, 0.317] | 0.306 (3618) [0.296, 0.318] | 0.316 (1513) [0.305, 0.327] | 0.367 (60) | 0.077 | flat +0.004 (noise 0.031) |
| reversal_k13_now | 0.647 (51) | 0.530 (366) [0.490, 0.576] | 0.570 (1560) [0.549, 0.591] | 0.573 (2651) [0.557, 0.590] | 0.564 (1179) [0.540, 0.590] | 0.604 (48) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.630 (54) | 0.592 (699) [0.564, 0.624] | 0.580 (2792) [0.566, 0.594] | 0.584 (4562) [0.573, 0.594] | 0.580 (2122) [0.565, 0.596] | 0.571 (70) | 0.293 | flat +0.024 (noise 0.026) |
| reversal_k3_now | 0.980 (49) | 0.945 (397) [0.928, 0.962] | 0.938 (1690) [0.929, 0.947] | 0.938 (3023) [0.932, 0.945] | 0.933 (1260) [0.923, 0.944] | 0.878 (41) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.480 (125) | 0.460 (939) [0.433, 0.486] | 0.464 (2842) [0.449, 0.479] | 0.476 (4306) [0.463, 0.489] | 0.460 (2316) [0.445, 0.476] | 0.488 (121) | 0.187 | flat -0.006 (noise 0.025) |
| reversal_k5_now | 0.818 (55) | 0.812 (361) [0.800, 0.823] | 0.831 (1561) [0.818, 0.844] | 0.830 (2771) [0.819, 0.841] | 0.819 (1160) [0.804, 0.833] | 0.841 (44) | 0.187 | flat -0.006 (noise 0.029) |
| reversal_k8_next | 0.384 (86) | 0.377 (757) [0.359, 0.394] | 0.383 (2519) [0.370, 0.396] | 0.389 (4187) [0.377, 0.400] | 0.381 (2081) [0.367, 0.395] | 0.404 (109) | 0.120 | flat +0.004 (noise 0.026) |
| reversal_k8_now | 0.709 (55) | 0.654 (332) [0.613, 0.693] | 0.701 (1523) [0.681, 0.722] | 0.702 (2739) [0.686, 0.718] | 0.685 (1152) [0.662, 0.708] | 0.744 (43) | 0.121 | flat -0.031 (noise 0.036) |
| overall | 0.505 (22099) | 0.504 (155589) [0.501, 0.507] | 0.504 (662331) [0.502, 0.505] | 0.503 (1169279) [0.502, 0.504] | 0.504 (485998) [0.502, 0.506] | 0.509 (20288) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07634, 0.1134] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5356, 'levels': [{'threshold': 0.07634, 'calls_per_day': 150.8, 'win_rate': 0.6138}, {'threshold': 0.1134, 'calls_per_day': 39.3, 'win_rate': 0.6522}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 31579, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15319 | 0.336 | 0.524 (15070) | 0.588 (1741) | 0.761 (2532) |
| volatility: normal | 15318 | 0.364 | 0.522 (15250) | 0.607 (1179) | 0.758 (2248) |
| volatility: wild | 15319 | 0.378 | 0.519 (15280) | 0.640 (530) | 0.772 (1931) |
| session: Asia 00-08 | 15360 | 0.357 | 0.527 (15256) | 0.607 (1220) | 0.766 (2206) |
| session: Europe 08-13 | 9600 | 0.355 | 0.524 (9513) | 0.598 (858) | 0.761 (1524) |
| session: US 13-21 | 15360 | 0.367 | 0.518 (15258) | 0.599 (867) | 0.771 (2162) |
| session: late 21-24 | 5636 | 0.350 | 0.513 (5573) | 0.608 (505) | 0.738 (819) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.327 | 0.319 | 0.276 | 0.276 | 0.433 | 0.238 | 0.416 | 0.976 |
| 6h | 360 | 0.345 | 0.340 | 0.263 | 0.298 | 0.506 | 0.252 | 0.439 | 1.199 |
| 24h | 1440 | 0.346 | 0.337 | 0.259 | 0.286 | 0.522 | 0.258 | 0.434 | 1.277 |
| 7d | 10080 | 0.370 | 0.360 | 0.274 | 0.307 | 0.535 | 0.268 | 0.471 | 1.209 |
| 30d | 43200 | 0.359 | 0.353 | 0.276 | 0.304 | 0.524 | 0.257 | 0.462 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.327 / 0.433 / 0.883; 2: 0.331 / 0.483 / 0.767; 3: 0.340 / 0.483 / 0.867; 4: 0.334 / 0.500 / 0.883; 5: 0.318 / 0.433 / 0.917; 6: 0.296 / 0.367 / 0.867; 7: 0.348 / 0.450 / 0.867; 8: 0.336 / 0.500 / 0.883; 9: 0.337 / 0.533 / 0.900; 10: 0.327 / 0.450 / 0.900; 11: 0.355 / 0.500 / 0.850; 12: 0.323 / 0.467 / 0.900; 13: 0.342 / 0.533 / 0.917; 14: 0.309 / 0.400 / 0.950; 15: 0.328 / 0.500 / 0.917
- 6h: 1: 0.345 / 0.506 / 0.906; 2: 0.346 / 0.514 / 0.892; 3: 0.337 / 0.497 / 0.906; 4: 0.350 / 0.547 / 0.914; 5: 0.323 / 0.450 / 0.922; 6: 0.339 / 0.517 / 0.911; 7: 0.345 / 0.503 / 0.903; 8: 0.332 / 0.517 / 0.925; 9: 0.346 / 0.522 / 0.928; 10: 0.329 / 0.472 / 0.928; 11: 0.343 / 0.531 / 0.919; 12: 0.335 / 0.517 / 0.942; 13: 0.340 / 0.522 / 0.942; 14: 0.322 / 0.458 / 0.947; 15: 0.331 / 0.503 / 0.942
- 24h: 1: 0.346 / 0.522 / 0.887; 2: 0.334 / 0.506 / 0.892; 3: 0.335 / 0.501 / 0.897; 4: 0.340 / 0.531 / 0.896; 5: 0.330 / 0.494 / 0.901; 6: 0.336 / 0.518 / 0.901; 7: 0.333 / 0.503 / 0.902; 8: 0.335 / 0.520 / 0.907; 9: 0.332 / 0.492 / 0.910; 10: 0.334 / 0.510 / 0.909; 11: 0.333 / 0.522 / 0.910; 12: 0.335 / 0.528 / 0.913; 13: 0.330 / 0.502 / 0.914; 14: 0.326 / 0.495 / 0.914; 15: 0.328 / 0.493 / 0.911
- 7d: 1: 0.370 / 0.535 / 0.899; 2: 0.358 / 0.503 / 0.899; 3: 0.357 / 0.509 / 0.900; 4: 0.353 / 0.496 / 0.900; 5: 0.353 / 0.501 / 0.901; 6: 0.352 / 0.497 / 0.901; 7: 0.351 / 0.494 / 0.901; 8: 0.354 / 0.511 / 0.901; 9: 0.352 / 0.498 / 0.901; 10: 0.352 / 0.506 / 0.901; 11: 0.350 / 0.501 / 0.901; 12: 0.351 / 0.504 / 0.901; 13: 0.349 / 0.495 / 0.901; 14: 0.349 / 0.496 / 0.901; 15: 0.349 / 0.501 / 0.901
- 30d: 1: 0.359 / 0.524 / 0.898; 2: 0.349 / 0.498 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.347 / 0.498 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.346 / 0.499 / 0.900; 7: 0.346 / 0.499 / 0.900; 8: 0.346 / 0.503 / 0.900; 9: 0.344 / 0.496 / 0.900; 10: 0.346 / 0.505 / 0.900; 11: 0.344 / 0.499 / 0.900; 12: 0.346 / 0.504 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.343 / 0.498 / 0.900; 15: 0.344 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.069 (body 0.038, range 0.099); 'price stays where it was' would score 0.083; colour right 0.450; typical miss of the close 8.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.122 (body 0.088, range 0.157); 'price stays where it was' would score 0.123; colour right 0.492; typical miss of the close 5.9 bp; chain ended on the right side 0.708 of 24 chains; n=360
- 24h: match 0.126 (body 0.091, range 0.161); 'price stays where it was' would score 0.129; colour right 0.490; typical miss of the close 6.1 bp; chain ended on the right side 0.635 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.168); 'price stays where it was' would score 0.134; colour right 0.501; typical miss of the close 8.7 bp; chain ended on the right side 0.552 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.5 bp; chain ended on the right side 0.524 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.195 / 4.4; 3: 0.167 / 5.7; 4: 0.132 / 6.3; 5: 0.123 / 6.9; 6: 0.112 / 7.5; 7: 0.106 / 7.8; 8: 0.097 / 8.1; 9: 0.087 / 8.1; 10: 0.087 / 8.8; 11: 0.084 / 9.3; 12: 0.077 / 9.6; 13: 0.068 / 9.7; 14: 0.069 / 10.2; 15: 0.059 / 10.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 120590, probability skill vs chance 0.2247, widened contest next: False
  - now: threshold 0.8342, hit rate recent 0.919 / long run 0.9351
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.314, naive rule 0.563, lift 2.55x
    - 24h: 44 calls (44 a day), hit rate 0.886, chance 0.297, naive rule 0.521, lift 2.99x
    - 7d: 385 calls (55 a day), hit rate 0.938, chance 0.296, naive rule 0.502, lift 3.16x
    - 30d: 1682 calls (56 a day), hit rate 0.936, chance 0.294, naive rule 0.493, lift 3.18x
  - next: threshold 0.537, hit rate recent 0.5635 / long run 0.5886
    - 6h: 27 calls (110 a day), hit rate 0.519, chance 0.314, lift 1.65x
    - 24h: 73 calls (73 a day), hit rate 0.562, chance 0.297, lift 1.89x
    - 7d: 678 calls (97 a day), hit rate 0.590, chance 0.296, lift 1.99x
    - 30d: 2806 calls (94 a day), hit rate 0.579, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.496; 0.35: 538, 0.520; 0.40: 478, 0.576; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 312, 0.741; 0.60: 264, 0.785; 0.65: 220, 0.810; 0.70: 174, 0.841; 0.75: 135, 0.875; 0.80: 90, 0.914; 0.85: 46, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.426; 0.35: 502, 0.464; 0.40: 408, 0.498; 0.45: 310, 0.533; 0.50: 201, 0.568; 0.55: 91, 0.574; 0.60: 14, 0.623; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 120588, probability skill vs chance 0.2083, widened contest next: False
  - now: threshold 0.6724, hit rate recent 0.8223 / long run 0.8212
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.190, naive rule 0.426, lift 4.39x
    - 24h: 47 calls (47 a day), hit rate 0.830, chance 0.175, naive rule 0.401, lift 4.74x
    - 7d: 360 calls (51 a day), hit rate 0.817, chance 0.183, naive rule 0.403, lift 4.46x
    - 30d: 1560 calls (52 a day), hit rate 0.831, chance 0.187, naive rule 0.400, lift 4.44x
  - next: threshold 0.4195, hit rate recent 0.4619 / long run 0.4728
    - 6h: 30 calls (122 a day), hit rate 0.500, chance 0.190, lift 2.63x
    - 24h: 136 calls (137 a day), hit rate 0.485, chance 0.175, lift 2.77x
    - 7d: 917 calls (131 a day), hit rate 0.468, chance 0.183, lift 2.56x
    - 30d: 2937 calls (98 a day), hit rate 0.463, chance 0.187, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.426; 0.35: 343, 0.494; 0.40: 276, 0.565; 0.45: 223, 0.621; 0.50: 176, 0.670; 0.55: 135, 0.711; 0.60: 104, 0.755; 0.65: 75, 0.793; 0.70: 53, 0.832; 0.75: 31, 0.878; 0.80: 10, 0.903
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.388; 0.35: 252, 0.420; 0.40: 158, 0.451; 0.45: 70, 0.463; 0.50: 15, 0.490; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 120585, probability skill vs chance 0.2, widened contest next: False
  - now: threshold 0.556, hit rate recent 0.7068 / long run 0.6861
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.137, naive rule 0.410, lift 5.30x
    - 24h: 47 calls (47 a day), hit rate 0.723, chance 0.113, naive rule 0.333, lift 6.41x
    - 7d: 334 calls (48 a day), hit rate 0.665, chance 0.115, naive rule 0.321, lift 5.76x
    - 30d: 1522 calls (51 a day), hit rate 0.698, chance 0.121, naive rule 0.329, lift 5.78x
  - next: threshold 0.3369, hit rate recent 0.4079 / long run 0.3828
    - 6h: 26 calls (107 a day), hit rate 0.500, chance 0.137, lift 3.65x
    - 24h: 120 calls (121 a day), hit rate 0.408, chance 0.113, lift 3.62x
    - 7d: 760 calls (109 a day), hit rate 0.376, chance 0.115, lift 3.26x
    - 30d: 2582 calls (86 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.426; 0.35: 188, 0.496; 0.40: 144, 0.549; 0.45: 110, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.675; 0.60: 41, 0.721; 0.65: 23, 0.789; 0.70: 10, 0.831; 0.75: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.351; 0.35: 97, 0.378; 0.40: 36, 0.398; 0.45: 8, 0.424; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 120580, probability skill vs chance 0.1805, widened contest next: False
  - now: threshold 0.4056, hit rate recent 0.6069 / long run 0.5618
    - 6h: 11 calls (46 a day), hit rate 0.727, chance 0.071, naive rule 0.276, lift 10.24x
    - 24h: 52 calls (53 a day), hit rate 0.615, chance 0.068, naive rule 0.248, lift 9.09x
    - 7d: 353 calls (51 a day), hit rate 0.552, chance 0.074, naive rule 0.267, lift 7.50x
    - 30d: 1568 calls (52 a day), hit rate 0.569, chance 0.077, naive rule 0.272, lift 7.38x
  - next: threshold 0.2946, hit rate recent 0.3371 / long run 0.3135
    - 6h: 8 calls (33 a day), hit rate 0.375, chance 0.071, lift 5.28x
    - 24h: 67 calls (68 a day), hit rate 0.373, chance 0.068, lift 5.51x
    - 7d: 468 calls (67 a day), hit rate 0.316, chance 0.074, lift 4.30x
    - 30d: 2170 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.444; 0.35: 87, 0.496; 0.40: 62, 0.553; 0.45: 41, 0.604; 0.50: 26, 0.659; 0.55: 15, 0.703; 0.60: 7, 0.746; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.316; 0.35: 14, 0.347; 0.40: 2, 0.420; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.190 | 0.67% | 0.883 | 0.417 | 0.251 | 0.450 | 0.198 |
| 6h | 10.645 | 0.99% | 0.903 | 0.506 | 0.250 | 0.503 | 0.335 |
| 24h | 10.891 | 1.99% | 0.890 | 0.494 | 0.250 | 0.489 | 0.479 |
| 7d | 14.827 | 3.17% | 0.900 | 0.499 | 0.250 | 0.501 | 0.647 |
| 30d | 13.268 | 4.19% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.272 | 12.164 | 12.168 | 12.398 | 12.503 | 12.418 | 12.237 | 12.224 | 12.194 | 12.190 |
| 6h | 10.752 | 10.742 | 10.691 | 10.730 | 10.998 | 10.859 | 10.643 | 10.607 | 10.624 | 10.645 |
| 24h | 11.112 | 11.021 | 10.969 | 10.933 | 11.175 | 11.114 | 10.882 | 10.839 | 10.868 | 10.891 |
| 7d | 15.313 | 14.970 | 14.904 | 14.845 | 15.105 | 14.979 | 14.814 | 14.789 | 14.799 | 14.827 |
| 30d | 13.848 | 13.396 | 13.351 | 13.291 | 13.509 | 13.462 | 13.264 | 13.245 | 13.244 | 13.268 |

## Next candle

- candle starting 2026-10-25 21:56 UTC, last close 2332.75
- P(up) 0.4955, return quantiles (bp): {'05': -7.666, '10': -5.656, '25': -2.961, '40': -1.129, '50': -0.036, '60': 0.874, '75': 2.465, '90': 4.921, '95': 6.693}
- changepoint probability 0.0724, regime age 32.2 min
- agent weights: empirical 0.037, ewma 0.067, garch 0.122, har 0.127, bocpd 0.013, hmm 0.037, online_qr 0.238, lgbm 0.359

## Learning log

- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.8, 19.68], current probabilities: [0.586, 0.406, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-10-25 22:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.507, 'l_abs': 0.735, 'l_hi': 0.778, 'l_lo': 0.764, 'b05': 0.725, 'b25': 0.733, 'b75': 0.683, 'b95': 0.681}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.727, 1.918, 2.09, 2.205, 2.42, 2.672, 2.642, 2.865, 3.15, 3.515, 3.328, 3.541, 3.538, 3.744]}
- calibration offsets (in sigma): {'05': -0.0125, '10': -0.055, '25': -0.0825, '40': -0.05, '50': -0.025, '60': -0.03, '75': -0.0475, '90': -0.045, '95': -0.0275}
