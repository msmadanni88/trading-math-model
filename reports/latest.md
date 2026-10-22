# ETH-USD 60s candle generator - report

- generated: 2026-10-22 22:02 UTC
- last closed candle: 2026-10-22 22:02 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_next 0.434 in the last 7 days, -0.055 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.543 (672) [0.507, 0.580] | 0.520 (2876) [0.500, 0.540] | 0.515 (4794) [0.500, 0.529] | 0.520 (1822) [0.492, 0.545] | 0.466 (88) | 0.500 | flat +0.038 (noise 0.027) |
| colour_clear | 0.550 (816) | 0.555 (5596) [0.546, 0.564] | 0.528 (23440) [0.519, 0.537] | 0.516 (39077) [0.509, 0.523] | 0.547 (14839) [0.541, 0.553] | 0.545 (759) | 0.500 | flat +0.014 (noise 0.009) |
| colour_confident | 0.602 (176) | 0.600 (979) [0.581, 0.622] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.588 (119) | 0.500 | flat +0.001 (noise 0.023) |
| colour_next | 0.533 (1434) | 0.534 (10023) [0.525, 0.542] | 0.519 (42861) [0.513, 0.525] | 0.512 (71456) [0.507, 0.516] | 0.530 (27107) [0.525, 0.535] | 0.530 (1317) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.505 (20076) | 0.500 (140322) [0.497, 0.504] | 0.501 (600054) [0.499, 0.502] | 0.501 (1000384) [0.499, 0.502] | 0.500 (379498) [0.498, 0.502] | 0.495 (18438) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.590 (39) | 0.631 (236) [0.595, 0.671] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.733 (15) | 0.500 | flat -0.025 (noise 0.044) |
| reversal_k13_next | 0.333 (60) | 0.324 (460) [0.314, 0.335] | 0.307 (2133) [0.295, 0.319] | 0.308 (3437) [0.297, 0.319] | 0.321 (1332) [0.309, 0.331] | 0.238 (42) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.596 (47) | 0.525 (396) [0.495, 0.560] | 0.571 (1555) [0.552, 0.591] | 0.574 (2504) [0.558, 0.591] | 0.564 (1032) [0.540, 0.591] | 0.588 (34) | 0.077 | flat -0.067 (noise 0.036) |
| reversal_k3_next | 0.657 (146) | 0.577 (817) [0.551, 0.607] | 0.575 (2745) [0.561, 0.589] | 0.582 (4349) [0.572, 0.594] | 0.576 (1909) [0.561, 0.593] | 0.614 (88) | 0.293 | flat +0.003 (noise 0.026) |
| reversal_k3_now | 0.984 (64) | 0.932 (399) [0.906, 0.959] | 0.934 (1701) [0.925, 0.943] | 0.937 (2858) [0.931, 0.944] | 0.931 (1095) [0.920, 0.942] | 0.918 (49) | 0.293 | flat +0.003 (noise 0.018) |
| reversal_k5_next | 0.484 (128) | 0.434 (912) [0.415, 0.453] | 0.463 (2571) [0.448, 0.478] | 0.474 (3917) [0.460, 0.488] | 0.453 (1927) [0.436, 0.471] | 0.487 (117) | 0.187 | down -0.055 (noise 0.027) |
| reversal_k5_now | 0.796 (54) | 0.817 (376) [0.792, 0.839] | 0.827 (1577) [0.813, 0.842] | 0.831 (2617) [0.819, 0.842] | 0.820 (1006) [0.804, 0.836] | 0.816 (38) | 0.187 | flat +0.006 (noise 0.029) |
| reversal_k8_next | 0.404 (104) | 0.365 (777) [0.341, 0.388] | 0.387 (2380) [0.373, 0.401] | 0.390 (3874) [0.377, 0.402] | 0.382 (1768) [0.366, 0.398] | 0.333 (90) | 0.121 | flat -0.032 (noise 0.027) |
| reversal_k8_now | 0.729 (48) | 0.667 (333) [0.631, 0.703] | 0.706 (1542) [0.686, 0.726] | 0.704 (2590) [0.688, 0.720] | 0.688 (1003) [0.663, 0.713] | 0.714 (35) | 0.121 | flat -0.007 (noise 0.035) |
| overall | 0.509 (22257) | 0.504 (155487) [0.501, 0.507] | 0.504 (661995) [0.502, 0.505] | 0.503 (1102780) [0.502, 0.504] | 0.504 (419499) [0.502, 0.506] | 0.498 (20336) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06876, 0.1025] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5346, 'levels': [{'threshold': 0.06876, 'calls_per_day': 145.5, 'win_rate': 0.584}, {'threshold': 0.1025, 'calls_per_day': 35.7, 'win_rate': 0.6414}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 27286, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15321 | 0.337 | 0.523 (15072) | 0.586 (1530) | 0.765 (2512) |
| volatility: normal | 15320 | 0.366 | 0.522 (15259) | 0.624 (828) | 0.754 (2207) |
| volatility: wild | 15321 | 0.379 | 0.510 (15283) | 0.615 (348) | 0.774 (2040) |
| session: Asia 00-08 | 15360 | 0.359 | 0.524 (15264) | 0.609 (978) | 0.763 (2233) |
| session: Europe 08-13 | 9600 | 0.356 | 0.520 (9516) | 0.600 (657) | 0.764 (1516) |
| session: US 13-21 | 15360 | 0.369 | 0.513 (15256) | 0.578 (666) | 0.773 (2185) |
| session: late 21-24 | 5642 | 0.351 | 0.514 (5578) | 0.622 (405) | 0.744 (825) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.348 | 0.329 | 0.304 | 0.304 | 0.559 | 0.241 | 0.456 | 1.279 |
| 6h | 360 | 0.379 | 0.372 | 0.282 | 0.324 | 0.531 | 0.266 | 0.492 | 1.283 |
| 24h | 1440 | 0.374 | 0.368 | 0.278 | 0.310 | 0.529 | 0.264 | 0.483 | 1.172 |
| 7d | 10080 | 0.369 | 0.359 | 0.274 | 0.306 | 0.535 | 0.266 | 0.472 | 1.222 |
| 30d | 43200 | 0.359 | 0.354 | 0.278 | 0.307 | 0.520 | 0.254 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.348 / 0.559 / 0.867; 2: 0.334 / 0.407 / 0.850; 3: 0.341 / 0.492 / 0.833; 4: 0.329 / 0.441 / 0.833; 5: 0.334 / 0.458 / 0.867; 6: 0.361 / 0.559 / 0.850; 7: 0.334 / 0.441 / 0.817; 8: 0.363 / 0.542 / 0.867; 9: 0.334 / 0.475 / 0.817; 10: 0.351 / 0.492 / 0.800; 11: 0.341 / 0.525 / 0.717; 12: 0.330 / 0.475 / 0.700; 13: 0.332 / 0.458 / 0.767; 14: 0.338 / 0.525 / 0.700; 15: 0.346 / 0.508 / 0.750
- 6h: 1: 0.379 / 0.531 / 0.894; 2: 0.376 / 0.536 / 0.883; 3: 0.370 / 0.508 / 0.892; 4: 0.370 / 0.525 / 0.875; 5: 0.365 / 0.520 / 0.883; 6: 0.367 / 0.536 / 0.867; 7: 0.345 / 0.439 / 0.875; 8: 0.366 / 0.511 / 0.864; 9: 0.354 / 0.480 / 0.856; 10: 0.360 / 0.492 / 0.847; 11: 0.358 / 0.489 / 0.822; 12: 0.355 / 0.483 / 0.825; 13: 0.343 / 0.453 / 0.803; 14: 0.367 / 0.508 / 0.803; 15: 0.355 / 0.489 / 0.811
- 24h: 1: 0.374 / 0.529 / 0.897; 2: 0.366 / 0.513 / 0.899; 3: 0.362 / 0.503 / 0.896; 4: 0.362 / 0.504 / 0.894; 5: 0.355 / 0.488 / 0.894; 6: 0.359 / 0.499 / 0.893; 7: 0.355 / 0.490 / 0.894; 8: 0.361 / 0.514 / 0.896; 9: 0.358 / 0.503 / 0.896; 10: 0.351 / 0.490 / 0.895; 11: 0.352 / 0.485 / 0.890; 12: 0.350 / 0.496 / 0.890; 13: 0.345 / 0.457 / 0.892; 14: 0.355 / 0.490 / 0.891; 15: 0.355 / 0.503 / 0.892
- 7d: 1: 0.369 / 0.535 / 0.895; 2: 0.356 / 0.497 / 0.900; 3: 0.357 / 0.502 / 0.900; 4: 0.353 / 0.498 / 0.900; 5: 0.353 / 0.496 / 0.900; 6: 0.352 / 0.493 / 0.900; 7: 0.352 / 0.496 / 0.900; 8: 0.354 / 0.505 / 0.899; 9: 0.352 / 0.501 / 0.899; 10: 0.353 / 0.505 / 0.899; 11: 0.348 / 0.493 / 0.898; 12: 0.350 / 0.501 / 0.898; 13: 0.349 / 0.492 / 0.899; 14: 0.350 / 0.499 / 0.899; 15: 0.348 / 0.498 / 0.899
- 30d: 1: 0.359 / 0.520 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.502 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.503 / 0.899; 9: 0.346 / 0.496 / 0.899; 10: 0.348 / 0.505 / 0.899; 11: 0.346 / 0.498 / 0.899; 12: 0.347 / 0.503 / 0.899; 13: 0.347 / 0.501 / 0.899; 14: 0.345 / 0.498 / 0.899; 15: 0.345 / 0.498 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.091 (body 0.052, range 0.130); 'price stays where it was' would score 0.112; colour right 0.458; typical miss of the close 10.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.133 (body 0.093, range 0.172); 'price stays where it was' would score 0.140; colour right 0.478; typical miss of the close 11.5 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.135 (body 0.093, range 0.176); 'price stays where it was' would score 0.138; colour right 0.490; typical miss of the close 10.0 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.169); 'price stays where it was' would score 0.132; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.8; 2: 0.199 / 4.5; 3: 0.166 / 6.0; 4: 0.132 / 6.5; 5: 0.121 / 7.2; 6: 0.109 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.3; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.078 / 9.9; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 116276, probability skill vs chance 0.2205, widened contest next: False
  - now: threshold 0.8361, hit rate recent 0.9468 / long run 0.9336
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.337, naive rule 0.545, lift 2.97x
    - 24h: 54 calls (54 a day), hit rate 0.926, chance 0.308, naive rule 0.518, lift 3.01x
    - 7d: 403 calls (58 a day), hit rate 0.933, chance 0.294, naive rule 0.489, lift 3.17x
    - 30d: 1693 calls (56 a day), hit rate 0.934, chance 0.293, naive rule 0.487, lift 3.19x
  - next: threshold 0.5634, hit rate recent 0.6354 / long run 0.5868
    - 6h: 14 calls (57 a day), hit rate 0.571, chance 0.337, lift 1.70x
    - 24h: 96 calls (96 a day), hit rate 0.604, chance 0.308, lift 1.96x
    - 7d: 825 calls (118 a day), hit rate 0.581, chance 0.294, lift 1.98x
    - 30d: 2767 calls (92 a day), hit rate 0.575, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 541, 0.516; 0.40: 482, 0.570; 0.45: 412, 0.642; 0.50: 359, 0.694; 0.55: 314, 0.736; 0.60: 266, 0.780; 0.65: 223, 0.806; 0.70: 177, 0.839; 0.75: 137, 0.873; 0.80: 92, 0.913; 0.85: 47, 0.949; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.425; 0.35: 499, 0.462; 0.40: 406, 0.495; 0.45: 309, 0.528; 0.50: 201, 0.559; 0.55: 90, 0.568; 0.60: 14, 0.611; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 116274, probability skill vs chance 0.2163, widened contest next: False
  - now: threshold 0.6827, hit rate recent 0.82 / long run 0.822
    - 6h: 8 calls (33 a day), hit rate 1.000, chance 0.208, naive rule 0.463, lift 4.80x
    - 24h: 44 calls (44 a day), hit rate 0.818, chance 0.189, naive rule 0.419, lift 4.33x
    - 7d: 363 calls (52 a day), hit rate 0.826, chance 0.187, naive rule 0.400, lift 4.42x
    - 30d: 1561 calls (52 a day), hit rate 0.829, chance 0.188, naive rule 0.397, lift 4.41x
  - next: threshold 0.4146, hit rate recent 0.4858 / long run 0.4539
    - 6h: 34 calls (139 a day), hit rate 0.471, chance 0.208, lift 2.26x
    - 24h: 126 calls (127 a day), hit rate 0.484, chance 0.189, lift 2.56x
    - 7d: 928 calls (133 a day), hit rate 0.441, chance 0.187, lift 2.36x
    - 30d: 2640 calls (88 a day), hit rate 0.462, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 345, 0.493; 0.40: 277, 0.564; 0.45: 224, 0.621; 0.50: 177, 0.669; 0.55: 135, 0.711; 0.60: 104, 0.756; 0.65: 77, 0.792; 0.70: 55, 0.827; 0.75: 31, 0.870; 0.80: 10, 0.899
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 250, 0.420; 0.40: 156, 0.446; 0.45: 70, 0.458; 0.50: 16, 0.493; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 116271, probability skill vs chance 0.2003, widened contest next: False
  - now: threshold 0.565, hit rate recent 0.7076 / long run 0.6886
    - 6h: 6 calls (25 a day), hit rate 0.833, chance 0.124, naive rule 0.347, lift 6.70x
    - 24h: 39 calls (39 a day), hit rate 0.718, chance 0.114, naive rule 0.317, lift 6.32x
    - 7d: 328 calls (47 a day), hit rate 0.671, chance 0.117, naive rule 0.316, lift 5.74x
    - 30d: 1529 calls (51 a day), hit rate 0.706, chance 0.121, naive rule 0.328, lift 5.83x
  - next: threshold 0.3432, hit rate recent 0.3694 / long run 0.3714
    - 6h: 19 calls (78 a day), hit rate 0.368, chance 0.124, lift 2.96x
    - 24h: 98 calls (99 a day), hit rate 0.337, chance 0.114, lift 2.96x
    - 7d: 782 calls (112 a day), hit rate 0.359, chance 0.117, lift 3.07x
    - 30d: 2409 calls (80 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.423; 0.35: 192, 0.493; 0.40: 146, 0.546; 0.45: 113, 0.593; 0.50: 86, 0.635; 0.55: 63, 0.680; 0.60: 42, 0.723; 0.65: 23, 0.787; 0.70: 10, 0.845; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 100, 0.377; 0.40: 38, 0.398; 0.45: 8, 0.421; 0.50: 1, 0.515
- **K=13**: model 1792454400, labels learned 116266, probability skill vs chance 0.188, widened contest next: False
  - now: threshold 0.4155, hit rate recent 0.5759 / long run 0.5578
    - 6h: 6 calls (25 a day), hit rate 0.667, chance 0.084, naive rule 0.304, lift 7.93x
    - 24h: 39 calls (39 a day), hit rate 0.590, chance 0.076, naive rule 0.293, lift 7.71x
    - 7d: 384 calls (55 a day), hit rate 0.529, chance 0.075, naive rule 0.268, lift 7.04x
    - 30d: 1549 calls (52 a day), hit rate 0.571, chance 0.077, naive rule 0.272, lift 7.39x
  - next: threshold 0.2946, hit rate recent 0.2852 / long run 0.3115
    - 6h: 10 calls (42 a day), hit rate 0.200, chance 0.084, lift 2.38x
    - 24h: 46 calls (46 a day), hit rate 0.239, chance 0.076, lift 3.13x
    - 7d: 460 calls (66 a day), hit rate 0.315, chance 0.075, lift 4.20x
    - 30d: 2127 calls (71 a day), hit rate 0.305, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.447; 0.35: 86, 0.502; 0.40: 61, 0.555; 0.45: 41, 0.610; 0.50: 25, 0.660; 0.55: 14, 0.709; 0.60: 6, 0.762; 0.65: 2, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.315; 0.35: 13, 0.346; 0.40: 2, 0.458; 0.45: 0, 0.333

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.302 | 2.59% | 0.900 | 0.533 | 0.254 | 0.407 | 0.386 |
| 6h | 16.515 | 1.32% | 0.894 | 0.539 | 0.251 | 0.514 | 0.593 |
| 24h | 15.965 | 2.33% | 0.899 | 0.502 | 0.250 | 0.511 | 0.585 |
| 7d | 14.990 | 3.83% | 0.898 | 0.500 | 0.251 | 0.498 | 0.647 |
| 30d | 13.574 | 4.09% | 0.900 | 0.500 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.628 | 12.339 | 12.301 | 12.310 | 12.382 | 12.271 | 12.335 | 12.226 | 12.262 | 12.302 |
| 6h | 16.736 | 16.549 | 16.503 | 16.534 | 16.714 | 16.546 | 16.485 | 16.466 | 16.470 | 16.515 |
| 24h | 16.345 | 16.117 | 16.059 | 15.939 | 16.253 | 16.059 | 15.938 | 15.956 | 15.938 | 15.965 |
| 7d | 15.587 | 15.137 | 15.081 | 15.011 | 15.248 | 15.133 | 14.977 | 14.962 | 14.963 | 14.990 |
| 30d | 14.153 | 13.697 | 13.656 | 13.596 | 13.818 | 13.759 | 13.571 | 13.550 | 13.549 | 13.574 |

## Next candle

- candle starting 2026-10-22 22:02 UTC, last close 2391.37
- P(up) 0.4963, return quantiles (bp): {'05': -7.962, '10': -6.001, '25': -3.012, '40': -0.936, '50': -0.042, '60': 0.987, '75': 2.902, '90': 6.086, '95': 7.878}
- changepoint probability 0.0535, regime age 130.4 min
- agent weights: empirical 0.010, ewma 0.070, garch 0.108, har 0.221, bocpd 0.024, hmm 0.100, online_qr 0.248, lgbm 0.219

## Learning log

- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- HMM volatility states (sd, bp per minute): [3.89, 6.21, 16.2], current probabilities: [0.878, 0.118, 0.004]
- live generator: {'versions': 60, 'latest_effective': '2026-10-22 22:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.198, 'l_abs': 0.649, 'l_hi': 0.757, 'l_lo': 0.772, 'b05': 0.688, 'b25': 0.614, 'b75': 0.645, 'b95': 0.629}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.484, 1.895, 2.107, 2.313, 2.806, 2.86, 3.253, 3.599, 3.878, 4.688, 4.906, 5.015, 5.428, 5.518]}
- calibration offsets (in sigma): {'05': 0.0005, '10': -0.009, '25': 0.0225, '40': 0.054, '50': 0.015, '60': -0.004, '75': -0.0025, '90': 0.019, '95': -0.0305}
