# ETH-USD 60s candle generator - report

- generated: 2026-11-05 14:29 UTC
- last closed candle: 2026-11-05 14:29 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.470 in the last 7 days, -0.067 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.470 (672) [0.448, 0.490] | 0.511 (2879) [0.494, 0.530] | 0.512 (6138) [0.500, 0.525] | 0.513 (3166) [0.494, 0.532] | 0.526 (57) | 0.500 | down -0.067 (noise 0.027) |
| colour_clear | 0.483 (783) | 0.526 (5464) [0.511, 0.541] | 0.541 (23808) [0.535, 0.546] | 0.520 (50207) [0.514, 0.526] | 0.542 (25969) [0.537, 0.547] | 0.549 (515) | 0.500 | flat -0.016 (noise 0.009) |
| colour_confident | 0.556 (108) | 0.575 (901) [0.562, 0.591] | 0.592 (4356) [0.581, 0.603] | 0.597 (4803) [0.585, 0.608] | 0.597 (4803) [0.585, 0.608] | 0.559 (68) | 0.500 | flat -0.026 (noise 0.021) |
| colour_next | 0.500 (1435) | 0.526 (9978) [0.516, 0.536] | 0.528 (42861) [0.524, 0.531] | 0.515 (91461) [0.511, 0.519] | 0.529 (47112) [0.525, 0.532] | 0.525 (866) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.504 (20090) | 0.502 (139692) [0.500, 0.504] | 0.501 (600054) [0.500, 0.502] | 0.501 (1280454) [0.500, 0.502] | 0.501 (659568) [0.500, 0.502] | 0.513 (12124) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.556 (27) | 0.631 (198) [0.592, 0.675] | 0.627 (1141) [0.608, 0.648] | 0.631 (1271) [0.612, 0.650] | 0.631 (1271) [0.612, 0.650] | 0.583 (12) | 0.500 | flat +0.024 (noise 0.042) |
| reversal_k13_next | 0.318 (44) | 0.355 (349) [0.312, 0.394] | 0.326 (1830) [0.312, 0.340] | 0.313 (4196) [0.302, 0.324] | 0.326 (2091) [0.314, 0.339] | 0.333 (36) | 0.077 | flat +0.038 (noise 0.034) |
| reversal_k13_now | 0.547 (53) | 0.574 (413) [0.538, 0.610] | 0.561 (1658) [0.541, 0.580] | 0.573 (3308) [0.559, 0.587] | 0.567 (1836) [0.548, 0.587] | 0.552 (29) | 0.077 | flat +0.006 (noise 0.036) |
| reversal_k3_next | 0.641 (39) | 0.600 (743) [0.581, 0.618] | 0.586 (2983) [0.574, 0.597] | 0.586 (5740) [0.577, 0.595] | 0.585 (3300) [0.573, 0.596] | 0.703 (37) | 0.293 | flat +0.008 (noise 0.026) |
| reversal_k3_now | 0.922 (51) | 0.927 (413) [0.908, 0.951] | 0.932 (1738) [0.922, 0.943] | 0.937 (3670) [0.930, 0.943] | 0.932 (1907) [0.923, 0.942] | 0.903 (31) | 0.293 | flat -0.015 (noise 0.020) |
| reversal_k5_next | 0.510 (51) | 0.537 (376) [0.514, 0.557] | 0.478 (2721) [0.464, 0.494] | 0.482 (5059) [0.471, 0.494] | 0.475 (3069) [0.461, 0.490] | 0.615 (39) | 0.187 | flat +0.036 (noise 0.031) |
| reversal_k5_now | 0.812 (48) | 0.810 (410) [0.796, 0.823] | 0.815 (1631) [0.805, 0.825] | 0.828 (3416) [0.819, 0.837] | 0.819 (1805) [0.810, 0.829] | 0.846 (26) | 0.187 | flat -0.018 (noise 0.027) |
| reversal_k8_next | 0.429 (49) | 0.436 (488) [0.411, 0.465] | 0.391 (2762) [0.378, 0.405] | 0.394 (5106) [0.383, 0.404] | 0.392 (3000) [0.379, 0.405] | 0.528 (36) | 0.121 | flat +0.049 (noise 0.029) |
| reversal_k8_now | 0.652 (46) | 0.697 (369) [0.663, 0.729] | 0.679 (1570) [0.660, 0.698] | 0.701 (3328) [0.687, 0.715] | 0.689 (1741) [0.669, 0.707] | 0.739 (23) | 0.121 | flat +0.014 (noise 0.037) |
| overall | 0.505 (22002) | 0.506 (153903) [0.504, 0.508] | 0.504 (662687) [0.503, 0.506] | 0.504 (1411876) [0.503, 0.505] | 0.505 (728595) [0.503, 0.506] | 0.516 (13304) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07706, 0.116] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5246, 'levels': [{'threshold': 0.07706, 'calls_per_day': 143.4, 'win_rate': 0.571}, {'threshold': 0.116, 'calls_per_day': 35.6, 'win_rate': 0.627}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42866, 'rate': 0.5276}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15170 | 0.343 | 0.528 (14930) | 0.574 (2232) | 0.738 (2592) |
| volatility: normal | 15169 | 0.366 | 0.533 (15099) | 0.612 (1455) | 0.752 (2255) |
| volatility: wild | 15170 | 0.381 | 0.524 (15128) | 0.618 (840) | 0.764 (2081) |
| session: Asia 00-08 | 15360 | 0.364 | 0.536 (15256) | 0.599 (1587) | 0.752 (2283) |
| session: Europe 08-13 | 9600 | 0.358 | 0.534 (9501) | 0.596 (1180) | 0.742 (1578) |
| session: US 13-21 | 14969 | 0.371 | 0.523 (14871) | 0.592 (1154) | 0.756 (2241) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5529) | 0.584 (606) | 0.743 (826) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.389 | 0.378 | 0.256 | 0.256 | 0.583 | 0.295 | 0.483 | 1.238 |
| 6h | 360 | 0.366 | 0.360 | 0.271 | 0.297 | 0.520 | 0.248 | 0.483 | 1.124 |
| 24h | 1440 | 0.373 | 0.364 | 0.295 | 0.331 | 0.511 | 0.255 | 0.492 | 1.206 |
| 7d | 10080 | 0.361 | 0.356 | 0.276 | 0.307 | 0.526 | 0.259 | 0.463 | 1.267 |
| 30d | 43200 | 0.364 | 0.356 | 0.277 | 0.308 | 0.528 | 0.262 | 0.465 | 1.250 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.389 / 0.583 / 0.933; 2: 0.346 / 0.417 / 1.000; 3: 0.373 / 0.567 / 1.000; 4: 0.377 / 0.533 / 1.000; 5: 0.333 / 0.450 / 0.983; 6: 0.368 / 0.517 / 1.000; 7: 0.400 / 0.633 / 0.983; 8: 0.385 / 0.550 / 1.000; 9: 0.371 / 0.567 / 0.967; 10: 0.372 / 0.483 / 0.950; 11: 0.364 / 0.517 / 0.933; 12: 0.355 / 0.467 / 0.883; 13: 0.364 / 0.550 / 0.933; 14: 0.343 / 0.433 / 0.933; 15: 0.344 / 0.467 / 0.983
- 6h: 1: 0.366 / 0.520 / 0.897; 2: 0.358 / 0.508 / 0.975; 3: 0.367 / 0.547 / 0.964; 4: 0.365 / 0.536 / 0.975; 5: 0.356 / 0.503 / 0.922; 6: 0.367 / 0.522 / 0.939; 7: 0.362 / 0.517 / 0.875; 8: 0.368 / 0.534 / 0.944; 9: 0.365 / 0.528 / 0.894; 10: 0.356 / 0.500 / 0.872; 11: 0.348 / 0.464 / 0.867; 12: 0.357 / 0.514 / 0.822; 13: 0.354 / 0.492 / 0.828; 14: 0.360 / 0.522 / 0.842; 15: 0.351 / 0.503 / 0.836
- 24h: 1: 0.373 / 0.511 / 0.897; 2: 0.365 / 0.504 / 0.912; 3: 0.371 / 0.518 / 0.905; 4: 0.373 / 0.526 / 0.904; 5: 0.368 / 0.501 / 0.901; 6: 0.369 / 0.517 / 0.903; 7: 0.368 / 0.514 / 0.886; 8: 0.367 / 0.518 / 0.901; 9: 0.369 / 0.516 / 0.887; 10: 0.362 / 0.500 / 0.881; 11: 0.357 / 0.474 / 0.878; 12: 0.370 / 0.533 / 0.865; 13: 0.363 / 0.497 / 0.864; 14: 0.360 / 0.503 / 0.869; 15: 0.358 / 0.502 / 0.865
- 7d: 1: 0.361 / 0.526 / 0.896; 2: 0.351 / 0.498 / 0.902; 3: 0.353 / 0.511 / 0.902; 4: 0.350 / 0.502 / 0.902; 5: 0.351 / 0.511 / 0.901; 6: 0.349 / 0.508 / 0.902; 7: 0.349 / 0.499 / 0.899; 8: 0.346 / 0.505 / 0.900; 9: 0.350 / 0.508 / 0.898; 10: 0.345 / 0.494 / 0.896; 11: 0.346 / 0.499 / 0.896; 12: 0.347 / 0.504 / 0.894; 13: 0.349 / 0.505 / 0.894; 14: 0.346 / 0.498 / 0.895; 15: 0.348 / 0.508 / 0.894
- 30d: 1: 0.364 / 0.528 / 0.898; 2: 0.352 / 0.496 / 0.900; 3: 0.355 / 0.510 / 0.900; 4: 0.351 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.350 / 0.499 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.349 / 0.501 / 0.900; 10: 0.349 / 0.503 / 0.899; 11: 0.347 / 0.497 / 0.899; 12: 0.349 / 0.502 / 0.899; 13: 0.348 / 0.500 / 0.899; 14: 0.347 / 0.501 / 0.899; 15: 0.348 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.173 (body 0.130, range 0.216); 'price stays where it was' would score 0.252; colour right 0.450; typical miss of the close 10.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.138 (body 0.096, range 0.181); 'price stays where it was' would score 0.155; colour right 0.492; typical miss of the close 8.3 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.125 (body 0.083, range 0.166); 'price stays where it was' would score 0.126; colour right 0.511; typical miss of the close 11.5 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.160); 'price stays where it was' would score 0.123; colour right 0.503; typical miss of the close 8.9 bp; chain ended on the right side 0.476 of 672 chains; n=10080
- 30d: match 0.124 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 8.4 bp; chain ended on the right side 0.511 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.3; 2: 0.200 / 5.0; 3: 0.169 / 6.6; 4: 0.131 / 6.9; 5: 0.125 / 7.7; 6: 0.114 / 8.5; 7: 0.111 / 8.7; 8: 0.098 / 9.7; 9: 0.090 / 9.5; 10: 0.089 / 10.1; 11: 0.086 / 10.2; 12: 0.078 / 10.6; 13: 0.071 / 10.9; 14: 0.072 / 11.4; 15: 0.065 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 135983, probability skill vs chance 0.2292, widened contest next: False
  - now: threshold 0.8368, hit rate recent 0.9142 / long run 0.9294
    - 6h: 15 calls (61 a day), hit rate 0.867, chance 0.308, naive rule 0.519, lift 2.81x
    - 24h: 48 calls (48 a day), hit rate 0.938, chance 0.283, naive rule 0.475, lift 3.31x
    - 7d: 407 calls (58 a day), hit rate 0.919, chance 0.292, naive rule 0.497, lift 3.14x
    - 30d: 1728 calls (58 a day), hit rate 0.933, chance 0.293, naive rule 0.494, lift 3.18x
  - next: threshold 0.5651, hit rate recent 0.6494 / long run 0.6042
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.308, lift 2.36x
    - 24h: 51 calls (51 a day), hit rate 0.686, chance 0.283, lift 2.43x
    - 7d: 694 calls (99 a day), hit rate 0.611, chance 0.292, lift 2.09x
    - 30d: 3001 calls (100 a day), hit rate 0.586, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.497; 0.35: 533, 0.523; 0.40: 473, 0.579; 0.45: 404, 0.650; 0.50: 354, 0.700; 0.55: 308, 0.743; 0.60: 260, 0.787; 0.65: 218, 0.812; 0.70: 173, 0.842; 0.75: 138, 0.875; 0.80: 92, 0.908; 0.85: 46, 0.948; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 499, 0.462; 0.40: 403, 0.499; 0.45: 306, 0.533; 0.50: 197, 0.569; 0.55: 89, 0.572; 0.60: 12, 0.631; 0.65: 1, 0.619
- **K=5**: model 1792540800, labels learned 135981, probability skill vs chance 0.2148, widened contest next: False
  - now: threshold 0.6872, hit rate recent 0.8172 / long run 0.8185
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.194, naive rule 0.430, lift 4.64x
    - 24h: 42 calls (42 a day), hit rate 0.810, chance 0.182, naive rule 0.380, lift 4.45x
    - 7d: 400 calls (57 a day), hit rate 0.807, chance 0.187, naive rule 0.412, lift 4.32x
    - 30d: 1623 calls (54 a day), hit rate 0.818, chance 0.187, naive rule 0.405, lift 4.38x
  - next: threshold 0.4539, hit rate recent 0.5656 / long run 0.5157
    - 6h: 15 calls (61 a day), hit rate 0.667, chance 0.194, lift 3.44x
    - 24h: 59 calls (59 a day), hit rate 0.576, chance 0.182, lift 3.17x
    - 7d: 388 calls (55 a day), hit rate 0.546, chance 0.187, lift 2.93x
    - 30d: 2734 calls (91 a day), hit rate 0.480, chance 0.187, lift 2.57x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.424; 0.35: 346, 0.490; 0.40: 280, 0.562; 0.45: 229, 0.614; 0.50: 183, 0.663; 0.55: 146, 0.700; 0.60: 110, 0.749; 0.65: 76, 0.788; 0.70: 48, 0.821; 0.75: 29, 0.863; 0.80: 10, 0.877
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.385; 0.35: 256, 0.421; 0.40: 160, 0.460; 0.45: 68, 0.483; 0.50: 12, 0.493; 0.55: 1, 0.444
- **K=8**: model 1793059200, labels learned 135978, probability skill vs chance 0.2145, widened contest next: False
  - now: threshold 0.5713, hit rate recent 0.6879 / long run 0.6921
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.124, naive rule 0.402, lift 5.36x
    - 24h: 38 calls (38 a day), hit rate 0.658, chance 0.119, naive rule 0.338, lift 5.55x
    - 7d: 360 calls (51 a day), hit rate 0.697, chance 0.123, naive rule 0.347, lift 5.69x
    - 30d: 1551 calls (52 a day), hit rate 0.681, chance 0.120, naive rule 0.335, lift 5.66x
  - next: threshold 0.3582, hit rate recent 0.4768 / long run 0.4241
    - 6h: 18 calls (74 a day), hit rate 0.500, chance 0.124, lift 4.02x
    - 24h: 57 calls (57 a day), hit rate 0.509, chance 0.119, lift 4.29x
    - 7d: 463 calls (66 a day), hit rate 0.456, chance 0.123, lift 3.72x
    - 30d: 2747 calls (92 a day), hit rate 0.391, chance 0.120, lift 3.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.431; 0.35: 191, 0.495; 0.40: 150, 0.543; 0.45: 116, 0.592; 0.50: 84, 0.639; 0.55: 60, 0.671; 0.60: 41, 0.705; 0.65: 24, 0.782; 0.70: 12, 0.816; 0.75: 2, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.362; 0.35: 90, 0.388; 0.40: 26, 0.413; 0.45: 5, 0.434; 0.50: 1, 0.654
- **K=13**: model 1793577600, labels learned 135973, probability skill vs chance 0.1819, widened contest next: False
  - now: threshold 0.4407, hit rate recent 0.5509 / long run 0.5679
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.070, naive rule 0.292, lift 6.53x
    - 24h: 49 calls (50 a day), hit rate 0.490, chance 0.073, naive rule 0.256, lift 6.68x
    - 7d: 403 calls (58 a day), hit rate 0.583, chance 0.080, naive rule 0.290, lift 7.32x
    - 30d: 1648 calls (55 a day), hit rate 0.563, chance 0.077, naive rule 0.280, lift 7.28x
  - next: threshold 0.2859, hit rate recent 0.3348 / long run 0.3369
    - 6h: 12 calls (50 a day), hit rate 0.167, chance 0.070, lift 2.40x
    - 24h: 55 calls (56 a day), hit rate 0.309, chance 0.073, lift 4.21x
    - 7d: 356 calls (51 a day), hit rate 0.365, chance 0.080, lift 4.58x
    - 30d: 1828 calls (61 a day), hit rate 0.325, chance 0.077, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 130, 0.438; 0.35: 93, 0.489; 0.40: 66, 0.545; 0.45: 45, 0.587; 0.50: 30, 0.650; 0.55: 19, 0.679; 0.60: 10, 0.712; 0.65: 3, 0.685; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.329; 0.35: 13, 0.341; 0.40: 3, 0.410; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.436 | -0.10% | 0.867 | 0.467 | 0.249 | 0.550 | 0.106 |
| 6h | 14.533 | 3.20% | 0.894 | 0.525 | 0.250 | 0.500 | 0.558 |
| 24h | 17.407 | 4.15% | 0.899 | 0.506 | 0.251 | 0.477 | 0.728 |
| 7d | 15.659 | 4.98% | 0.900 | 0.501 | 0.250 | 0.504 | 0.750 |
| 30d | 14.819 | 4.23% | 0.900 | 0.500 | 0.250 | 0.498 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.416 | 19.307 | 19.352 | 19.459 | 19.853 | 20.032 | 19.354 | 19.313 | 19.352 | 19.436 |
| 6h | 15.014 | 14.560 | 14.602 | 14.520 | 14.861 | 14.790 | 14.479 | 14.424 | 14.502 | 14.533 |
| 24h | 18.160 | 17.485 | 17.418 | 17.391 | 17.630 | 17.684 | 17.457 | 17.392 | 17.375 | 17.407 |
| 7d | 16.479 | 15.811 | 15.771 | 15.702 | 15.954 | 16.000 | 15.651 | 15.629 | 15.632 | 15.659 |
| 30d | 15.473 | 14.969 | 14.910 | 14.847 | 15.087 | 15.035 | 14.813 | 14.789 | 14.791 | 14.819 |

## Next candle

- candle starting 2026-11-05 14:29 UTC, last close 2382.75
- P(up) 0.483, return quantiles (bp): {'05': -12.099, '10': -9.172, '25': -4.75, '40': -1.717, '50': -0.229, '60': 1.153, '75': 3.832, '90': 8.655, '95': 11.537}
- changepoint probability 0.0364, regime age 71.2 min
- agent weights: empirical 0.008, ewma 0.126, garch 0.131, har 0.159, bocpd 0.026, hmm 0.039, online_qr 0.215, lgbm 0.297

## Learning log

- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- HMM volatility states (sd, bp per minute): [2.39, 4.93, 13.06], current probabilities: [0.0, 0.378, 0.622]
- live generator: {'versions': 60, 'latest_effective': '2026-11-05 14:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.266, 'l_abs': 0.687, 'l_hi': 0.742, 'l_lo': 0.795, 'b05': 0.734, 'b25': 0.698, 'b75': 0.603, 'b95': 0.702}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.062, 1.412, 1.57, 2.023, 2.009, 3.586, 2.284, 3.844, 4.959, 5.317, 7.976, 9.011, 8.146, 8.971]}
- calibration offsets (in sigma): {'05': -0.006, '10': 0.008, '25': 0.0, '40': -0.008, '50': -0.02, '60': -0.062, '75': -0.07, '90': -0.038, '95': -0.064}
