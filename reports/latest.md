# ETH-USD 60s candle generator - report

- generated: 2026-10-22 04:49 UTC
- last closed candle: 2026-10-22 04:49 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_next 0.434 in the last 7 days, -0.055 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.543 (672) [0.507, 0.580] | 0.520 (2876) [0.500, 0.540] | 0.515 (4794) [0.500, 0.529] | 0.520 (1822) [0.492, 0.545] | 0.474 (19) | 0.500 | flat +0.038 (noise 0.027) |
| colour_clear | 0.550 (816) | 0.555 (5596) [0.546, 0.564] | 0.528 (23440) [0.519, 0.537] | 0.516 (39077) [0.509, 0.523] | 0.547 (14839) [0.541, 0.553] | 0.522 (161) | 0.500 | flat +0.014 (noise 0.009) |
| colour_confident | 0.602 (176) | 0.600 (979) [0.581, 0.622] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.538 (26) | 0.500 | flat +0.001 (noise 0.023) |
| colour_next | 0.533 (1434) | 0.534 (10023) [0.525, 0.542] | 0.519 (42861) [0.513, 0.525] | 0.512 (71456) [0.507, 0.516] | 0.530 (27107) [0.525, 0.535] | 0.535 (288) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.505 (20076) | 0.500 (140322) [0.497, 0.504] | 0.501 (600054) [0.499, 0.502] | 0.501 (1000384) [0.499, 0.502] | 0.500 (379498) [0.498, 0.502] | 0.481 (4032) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.590 (39) | 0.631 (236) [0.595, 0.671] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.000 (1) | 0.500 | flat -0.025 (noise 0.044) |
| reversal_k13_next | 0.333 (60) | 0.324 (460) [0.314, 0.335] | 0.307 (2133) [0.295, 0.319] | 0.308 (3437) [0.297, 0.319] | 0.321 (1332) [0.309, 0.331] | 0.167 (12) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.596 (47) | 0.525 (396) [0.495, 0.560] | 0.571 (1555) [0.552, 0.591] | 0.574 (2504) [0.558, 0.591] | 0.564 (1032) [0.540, 0.591] | 0.400 (5) | 0.077 | flat -0.067 (noise 0.036) |
| reversal_k3_next | 0.657 (146) | 0.577 (817) [0.551, 0.607] | 0.575 (2745) [0.561, 0.589] | 0.582 (4349) [0.572, 0.594] | 0.576 (1909) [0.561, 0.593] | 0.481 (27) | 0.293 | flat +0.003 (noise 0.026) |
| reversal_k3_now | 0.984 (64) | 0.932 (399) [0.906, 0.959] | 0.934 (1701) [0.925, 0.943] | 0.937 (2858) [0.931, 0.944] | 0.931 (1095) [0.920, 0.942] | 0.667 (6) | 0.293 | flat +0.003 (noise 0.018) |
| reversal_k5_next | 0.484 (128) | 0.434 (912) [0.415, 0.453] | 0.463 (2571) [0.448, 0.478] | 0.474 (3917) [0.460, 0.488] | 0.453 (1927) [0.436, 0.471] | 0.435 (23) | 0.187 | down -0.055 (noise 0.027) |
| reversal_k5_now | 0.796 (54) | 0.817 (376) [0.792, 0.839] | 0.827 (1577) [0.813, 0.842] | 0.831 (2617) [0.819, 0.842] | 0.820 (1006) [0.804, 0.836] | 0.600 (5) | 0.187 | flat +0.006 (noise 0.029) |
| reversal_k8_next | 0.404 (104) | 0.365 (777) [0.341, 0.388] | 0.387 (2380) [0.373, 0.401] | 0.390 (3874) [0.377, 0.402] | 0.382 (1768) [0.366, 0.398] | 0.261 (23) | 0.121 | flat -0.032 (noise 0.027) |
| reversal_k8_now | 0.729 (48) | 0.667 (333) [0.631, 0.703] | 0.706 (1542) [0.686, 0.726] | 0.704 (2590) [0.688, 0.720] | 0.688 (1003) [0.663, 0.713] | 0.500 (6) | 0.121 | flat -0.007 (noise 0.035) |
| overall | 0.509 (22257) | 0.504 (155487) [0.501, 0.507] | 0.504 (661995) [0.502, 0.505] | 0.503 (1102780) [0.502, 0.504] | 0.504 (419499) [0.502, 0.506] | 0.483 (4446) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06792, 0.1027] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5335, 'levels': [{'threshold': 0.06792, 'calls_per_day': 146.9, 'win_rate': 0.5764}, {'threshold': 0.1027, 'calls_per_day': 36.4, 'win_rate': 0.6406}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 26257, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14977 | 0.337 | 0.524 (14731) | 0.588 (1507) | 0.764 (2457) |
| volatility: normal | 14976 | 0.366 | 0.520 (14914) | 0.620 (782) | 0.754 (2169) |
| volatility: wild | 14976 | 0.379 | 0.510 (14940) | 0.617 (324) | 0.773 (1999) |
| session: Asia 00-08 | 15169 | 0.359 | 0.524 (15073) | 0.610 (954) | 0.761 (2205) |
| session: Europe 08-13 | 9300 | 0.356 | 0.520 (9217) | 0.597 (635) | 0.768 (1469) |
| session: US 13-21 | 14880 | 0.368 | 0.513 (14778) | 0.578 (635) | 0.770 (2130) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5517) | 0.625 (389) | 0.743 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.366 | 0.326 | 0.283 | 0.283 | 0.567 | 0.271 | 0.461 | 1.580 |
| 6h | 360 | 0.376 | 0.366 | 0.286 | 0.314 | 0.521 | 0.278 | 0.473 | 1.166 |
| 24h | 1440 | 0.374 | 0.365 | 0.286 | 0.316 | 0.539 | 0.274 | 0.475 | 1.186 |
| 7d | 10080 | 0.370 | 0.360 | 0.276 | 0.308 | 0.533 | 0.267 | 0.472 | 1.222 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.519 | 0.254 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.366 / 0.567 / 0.883; 2: 0.313 / 0.417 / 0.933; 3: 0.330 / 0.450 / 0.950; 4: 0.342 / 0.517 / 0.967; 5: 0.340 / 0.483 / 0.917; 6: 0.344 / 0.483 / 0.950; 7: 0.319 / 0.417 / 0.933; 8: 0.317 / 0.433 / 0.950; 9: 0.326 / 0.450 / 0.950; 10: 0.334 / 0.450 / 0.983; 11: 0.312 / 0.450 / 0.983; 12: 0.323 / 0.517 / 0.967; 13: 0.322 / 0.433 / 0.983; 14: 0.313 / 0.417 / 0.983; 15: 0.357 / 0.583 / 0.950
- 6h: 1: 0.376 / 0.521 / 0.908; 2: 0.348 / 0.435 / 0.908; 3: 0.363 / 0.490 / 0.914; 4: 0.361 / 0.501 / 0.919; 5: 0.346 / 0.451 / 0.911; 6: 0.359 / 0.507 / 0.914; 7: 0.349 / 0.482 / 0.906; 8: 0.350 / 0.471 / 0.919; 9: 0.365 / 0.529 / 0.914; 10: 0.355 / 0.499 / 0.914; 11: 0.347 / 0.476 / 0.911; 12: 0.343 / 0.493 / 0.919; 13: 0.337 / 0.446 / 0.936; 14: 0.350 / 0.460 / 0.925; 15: 0.356 / 0.526 / 0.914
- 24h: 1: 0.374 / 0.539 / 0.898; 2: 0.359 / 0.481 / 0.902; 3: 0.359 / 0.502 / 0.899; 4: 0.358 / 0.500 / 0.903; 5: 0.358 / 0.507 / 0.899; 6: 0.360 / 0.500 / 0.897; 7: 0.360 / 0.502 / 0.892; 8: 0.356 / 0.503 / 0.892; 9: 0.357 / 0.506 / 0.890; 10: 0.357 / 0.510 / 0.894; 11: 0.349 / 0.481 / 0.893; 12: 0.349 / 0.494 / 0.897; 13: 0.351 / 0.498 / 0.897; 14: 0.355 / 0.499 / 0.899; 15: 0.354 / 0.517 / 0.895
- 7d: 1: 0.370 / 0.533 / 0.896; 2: 0.355 / 0.492 / 0.900; 3: 0.358 / 0.503 / 0.900; 4: 0.354 / 0.496 / 0.900; 5: 0.354 / 0.497 / 0.900; 6: 0.354 / 0.495 / 0.899; 7: 0.353 / 0.497 / 0.899; 8: 0.354 / 0.502 / 0.899; 9: 0.353 / 0.501 / 0.899; 10: 0.355 / 0.509 / 0.899; 11: 0.349 / 0.494 / 0.899; 12: 0.352 / 0.505 / 0.900; 13: 0.351 / 0.497 / 0.900; 14: 0.352 / 0.503 / 0.900; 15: 0.350 / 0.500 / 0.900
- 30d: 1: 0.360 / 0.519 / 0.899; 2: 0.351 / 0.495 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.347 / 0.502 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.154 (body 0.126, range 0.182); 'price stays where it was' would score 0.201; colour right 0.517; typical miss of the close 6.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.135 (body 0.092, range 0.178); 'price stays where it was' would score 0.143; colour right 0.451; typical miss of the close 8.7 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.133 (body 0.091, range 0.176); 'price stays where it was' would score 0.139; colour right 0.508; typical miss of the close 9.3 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 8.9 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.9; 2: 0.197 / 4.5; 3: 0.166 / 6.0; 4: 0.132 / 6.5; 5: 0.120 / 7.2; 6: 0.109 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.088 / 8.3; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.079 / 9.9; 13: 0.068 / 10.1; 14: 0.068 / 10.4; 15: 0.059 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 115243, probability skill vs chance 0.209, widened contest next: False
  - now: threshold 0.8357, hit rate recent 0.9352 / long run 0.9321
    - 6h: 8 calls (32 a day), hit rate 0.750, chance 0.276, naive rule 0.443, lift 2.72x
    - 24h: 57 calls (57 a day), hit rate 0.965, chance 0.299, naive rule 0.494, lift 3.22x
    - 7d: 394 calls (56 a day), hit rate 0.931, chance 0.291, naive rule 0.482, lift 3.21x
    - 30d: 1695 calls (57 a day), hit rate 0.934, chance 0.293, naive rule 0.485, lift 3.19x
  - next: threshold 0.528, hit rate recent 0.5706 / long run 0.5776
    - 6h: 32 calls (130 a day), hit rate 0.469, chance 0.276, lift 1.70x
    - 24h: 143 calls (143 a day), hit rate 0.594, chance 0.299, lift 1.99x
    - 7d: 830 calls (119 a day), hit rate 0.573, chance 0.291, lift 1.97x
    - 30d: 2757 calls (92 a day), hit rate 0.574, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.491; 0.35: 541, 0.515; 0.40: 482, 0.568; 0.45: 412, 0.639; 0.50: 360, 0.691; 0.55: 314, 0.733; 0.60: 267, 0.776; 0.65: 223, 0.805; 0.70: 177, 0.837; 0.75: 137, 0.870; 0.80: 93, 0.910; 0.85: 47, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.425; 0.35: 499, 0.461; 0.40: 406, 0.493; 0.45: 310, 0.525; 0.50: 201, 0.557; 0.55: 91, 0.567; 0.60: 14, 0.613; 0.65: 1, 0.710
- **K=5**: model 1792540800, labels learned 115241, probability skill vs chance 0.21, widened contest next: False
  - now: threshold 0.6838, hit rate recent 0.7931 / long run 0.8205
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.154, naive rule 0.357, lift 4.32x
    - 24h: 48 calls (48 a day), hit rate 0.792, chance 0.182, naive rule 0.393, lift 4.34x
    - 7d: 371 calls (53 a day), hit rate 0.819, chance 0.185, naive rule 0.395, lift 4.43x
    - 30d: 1564 calls (52 a day), hit rate 0.827, chance 0.188, naive rule 0.395, lift 4.41x
  - next: threshold 0.4195, hit rate recent 0.4517 / long run 0.4461
    - 6h: 28 calls (114 a day), hit rate 0.429, chance 0.154, lift 2.78x
    - 24h: 125 calls (126 a day), hit rate 0.456, chance 0.182, lift 2.50x
    - 7d: 914 calls (131 a day), hit rate 0.434, chance 0.185, lift 2.35x
    - 30d: 2579 calls (86 a day), hit rate 0.462, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 346, 0.490; 0.40: 278, 0.562; 0.45: 225, 0.618; 0.50: 177, 0.668; 0.55: 136, 0.710; 0.60: 105, 0.754; 0.65: 78, 0.789; 0.70: 56, 0.824; 0.75: 31, 0.866; 0.80: 10, 0.897
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.418; 0.40: 157, 0.445; 0.45: 72, 0.461; 0.50: 16, 0.495; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 115238, probability skill vs chance 0.1972, widened contest next: False
  - now: threshold 0.5661, hit rate recent 0.6674 / long run 0.685
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.099, naive rule 0.276, lift 5.07x
    - 24h: 43 calls (43 a day), hit rate 0.744, chance 0.112, naive rule 0.305, lift 6.67x
    - 7d: 330 calls (47 a day), hit rate 0.667, chance 0.116, naive rule 0.312, lift 5.74x
    - 30d: 1536 calls (51 a day), hit rate 0.704, chance 0.121, naive rule 0.327, lift 5.83x
  - next: threshold 0.3407, hit rate recent 0.3498 / long run 0.3727
    - 6h: 27 calls (111 a day), hit rate 0.296, chance 0.099, lift 3.01x
    - 24h: 103 calls (104 a day), hit rate 0.369, chance 0.112, lift 3.31x
    - 7d: 779 calls (111 a day), hit rate 0.359, chance 0.116, lift 3.10x
    - 30d: 2394 calls (80 a day), hit rate 0.385, chance 0.121, lift 3.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 253, 0.421; 0.35: 192, 0.491; 0.40: 147, 0.546; 0.45: 114, 0.592; 0.50: 87, 0.633; 0.55: 63, 0.678; 0.60: 42, 0.722; 0.65: 24, 0.787; 0.70: 10, 0.840; 0.75: 1, 0.812
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.349; 0.35: 102, 0.378; 0.40: 39, 0.402; 0.45: 8, 0.427; 0.50: 1, 0.545
- **K=13**: model 1792454400, labels learned 115233, probability skill vs chance 0.1839, widened contest next: False
  - now: threshold 0.4356, hit rate recent 0.5422 / long run 0.5547
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.075, naive rule 0.275, lift 6.63x
    - 24h: 44 calls (44 a day), hit rate 0.614, chance 0.071, naive rule 0.262, lift 8.66x
    - 7d: 393 calls (56 a day), hit rate 0.522, chance 0.076, naive rule 0.266, lift 6.90x
    - 30d: 1549 calls (52 a day), hit rate 0.570, chance 0.077, naive rule 0.271, lift 7.36x
  - next: threshold 0.294, hit rate recent 0.2938 / long run 0.3138
    - 6h: 14 calls (58 a day), hit rate 0.214, chance 0.075, lift 2.84x
    - 24h: 57 calls (58 a day), hit rate 0.263, chance 0.071, lift 3.71x
    - 7d: 460 calls (66 a day), hit rate 0.317, chance 0.076, lift 4.20x
    - 30d: 2138 calls (71 a day), hit rate 0.305, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.449; 0.35: 86, 0.501; 0.40: 61, 0.551; 0.45: 41, 0.609; 0.50: 25, 0.658; 0.55: 14, 0.704; 0.60: 6, 0.753; 0.65: 1, 0.825
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.316; 0.35: 13, 0.351; 0.40: 2, 0.450; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.250 | 1.80% | 0.900 | 0.567 | 0.251 | 0.483 | 0.181 |
| 6h | 14.626 | 1.76% | 0.906 | 0.486 | 0.250 | 0.513 | 0.547 |
| 24h | 16.121 | 2.85% | 0.903 | 0.493 | 0.250 | 0.520 | 0.598 |
| 7d | 15.475 | 3.93% | 0.900 | 0.499 | 0.251 | 0.498 | 0.660 |
| 30d | 13.570 | 4.09% | 0.900 | 0.500 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.456 | 11.267 | 11.234 | 11.122 | 11.494 | 11.260 | 11.186 | 11.217 | 11.189 | 11.250 |
| 6h | 14.888 | 14.781 | 14.734 | 14.640 | 14.860 | 14.715 | 14.643 | 14.595 | 14.620 | 14.626 |
| 24h | 16.595 | 16.277 | 16.235 | 16.182 | 16.414 | 16.260 | 16.117 | 16.060 | 16.103 | 16.121 |
| 7d | 16.108 | 15.618 | 15.568 | 15.506 | 15.721 | 15.642 | 15.470 | 15.451 | 15.451 | 15.475 |
| 30d | 14.149 | 13.693 | 13.653 | 13.593 | 13.815 | 13.756 | 13.566 | 13.546 | 13.545 | 13.570 |

## Next candle

- candle starting 2026-10-22 04:49 UTC, last close 2439.35
- P(up) 0.5095, return quantiles (bp): {'05': -7.43, '10': -6.024, '25': -3.165, '40': -1.07, '50': 0.11, '60': 1.141, '75': 2.624, '90': 5.405, '95': 7.151}
- changepoint probability 0.0423, regime age 83.7 min
- agent weights: empirical 0.013, ewma 0.071, garch 0.102, har 0.168, bocpd 0.028, hmm 0.091, online_qr 0.217, lgbm 0.309

## Learning log

- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.56, 5.88, 15.56], current probabilities: [0.265, 0.725, 0.01]
- live generator: {'versions': 60, 'latest_effective': '2026-10-22 05:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.406, 'l_abs': 0.639, 'l_hi': 0.761, 'l_lo': 0.778, 'b05': 0.709, 'b25': 0.618, 'b75': 0.662, 'b95': 0.666}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.272, 1.561, 1.701, 2.148, 2.454, 2.765, 3.082, 3.342, 3.324, 3.494, 3.375, 3.315, 3.517, 3.796]}
- calibration offsets (in sigma): {'05': -0.006, '10': -0.092, '25': -0.08, '40': -0.018, '50': 0.02, '60': 0.018, '75': -0.04, '90': -0.058, '95': -0.074}
