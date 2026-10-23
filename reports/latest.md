# ETH-USD 60s candle generator - report

- generated: 2026-10-23 19:17 UTC
- last closed candle: 2026-10-23 19:17 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: colour_path 0.498 in the last 7 days, -0.005 against the 7 before
- WIN RATE FALLING: overall 0.502 in the last 7 days, -0.004 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.542 (672) [0.504, 0.580] | 0.518 (2876) [0.498, 0.537] | 0.513 (4890) [0.499, 0.527] | 0.517 (1918) [0.492, 0.541] | 0.584 (77) | 0.500 | flat +0.035 (noise 0.029) |
| colour_clear | 0.545 (826) | 0.555 (5631) [0.546, 0.564] | 0.529 (23423) [0.520, 0.538] | 0.516 (39903) [0.510, 0.523] | 0.547 (15665) [0.542, 0.552] | 0.543 (685) | 0.500 | flat +0.015 (noise 0.009) |
| colour_confident | 0.585 (135) | 0.598 (1030) [0.581, 0.620] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.654 (159) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.529 (1435) | 0.535 (10022) [0.528, 0.542] | 0.519 (42861) [0.514, 0.525] | 0.512 (72891) [0.508, 0.516] | 0.530 (28542) [0.525, 0.535] | 0.538 (1152) | 0.500 | flat +0.011 (noise 0.007) |
| colour_path | 0.496 (20090) | 0.498 (140308) [0.496, 0.501] | 0.500 (600054) [0.499, 0.502] | 0.500 (1020474) [0.499, 0.501] | 0.500 (399588) [0.498, 0.502] | 0.502 (16128) | 0.500 | down -0.005 (noise 0.002) |
| colour_strong | 0.750 (16) | 0.628 (239) [0.595, 0.661] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.705 (44) | 0.500 | flat -0.054 (noise 0.044) |
| reversal_k13_next | 0.245 (49) | 0.315 (457) [0.296, 0.332] | 0.305 (2131) [0.293, 0.317] | 0.307 (3486) [0.296, 0.318] | 0.318 (1381) [0.306, 0.330] | 0.333 (54) | 0.077 | flat -0.002 (noise 0.031) |
| reversal_k13_now | 0.605 (38) | 0.538 (383) [0.504, 0.576] | 0.572 (1549) [0.553, 0.592] | 0.574 (2542) [0.559, 0.591] | 0.565 (1070) [0.542, 0.590] | 0.500 (48) | 0.077 | flat -0.037 (noise 0.037) |
| reversal_k3_next | 0.604 (96) | 0.581 (826) [0.557, 0.610] | 0.575 (2772) [0.562, 0.589] | 0.583 (4445) [0.572, 0.594] | 0.578 (2005) [0.563, 0.593] | 0.582 (55) | 0.293 | flat +0.003 (noise 0.025) |
| reversal_k3_now | 0.924 (53) | 0.933 (405) [0.909, 0.958] | 0.934 (1694) [0.926, 0.943] | 0.937 (2911) [0.931, 0.944] | 0.930 (1148) [0.920, 0.941] | 0.961 (51) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.485 (132) | 0.441 (938) [0.420, 0.462] | 0.463 (2650) [0.448, 0.477] | 0.474 (4049) [0.461, 0.487] | 0.455 (2059) [0.439, 0.472] | 0.533 (105) | 0.187 | flat -0.046 (noise 0.026) |
| reversal_k5_now | 0.829 (41) | 0.827 (364) [0.809, 0.845] | 0.830 (1557) [0.817, 0.844] | 0.831 (2658) [0.819, 0.842] | 0.820 (1047) [0.805, 0.836] | 0.812 (48) | 0.187 | flat +0.015 (noise 0.029) |
| reversal_k8_next | 0.337 (101) | 0.360 (784) [0.335, 0.382] | 0.383 (2416) [0.369, 0.396] | 0.388 (3975) [0.376, 0.401] | 0.379 (1869) [0.364, 0.396] | 0.420 (100) | 0.121 | flat -0.042 (noise 0.027) |
| reversal_k8_now | 0.737 (38) | 0.677 (328) [0.639, 0.715] | 0.707 (1527) [0.687, 0.727] | 0.704 (2628) [0.689, 0.720] | 0.690 (1041) [0.666, 0.714] | 0.600 (45) | 0.121 | flat -0.003 (noise 0.036) |
| overall | 0.499 (22169) | 0.502 (155487) [0.500, 0.505] | 0.503 (662087) [0.502, 0.505] | 0.503 (1124949) [0.502, 0.504] | 0.504 (441668) [0.502, 0.506] | 0.507 (17863) | - | down -0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06984, 0.1029] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5378, 'levels': [{'threshold': 0.06984, 'calls_per_day': 146.7, 'win_rate': 0.6002}, {'threshold': 0.1029, 'calls_per_day': 36.9, 'win_rate': 0.6538}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 28556, 'rate': 0.5313}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15266 | 0.337 | 0.523 (15020) | 0.586 (1537) | 0.765 (2509) |
| volatility: normal | 15265 | 0.366 | 0.521 (15198) | 0.628 (936) | 0.753 (2244) |
| volatility: wild | 15266 | 0.379 | 0.515 (15230) | 0.615 (408) | 0.773 (1984) |
| session: Asia 00-08 | 15360 | 0.359 | 0.526 (15260) | 0.614 (1041) | 0.765 (2221) |
| session: Europe 08-13 | 9600 | 0.355 | 0.520 (9515) | 0.601 (710) | 0.764 (1531) |
| session: US 13-21 | 15257 | 0.369 | 0.515 (15155) | 0.583 (709) | 0.768 (2163) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5518) | 0.620 (421) | 0.742 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.340 | 0.324 | 0.227 | 0.227 | 0.500 | 0.218 | 0.462 | 1.605 |
| 6h | 360 | 0.384 | 0.369 | 0.286 | 0.327 | 0.550 | 0.277 | 0.490 | 1.350 |
| 24h | 1440 | 0.377 | 0.363 | 0.273 | 0.305 | 0.539 | 0.273 | 0.481 | 1.267 |
| 7d | 10080 | 0.369 | 0.359 | 0.271 | 0.303 | 0.538 | 0.268 | 0.471 | 1.229 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.521 | 0.255 | 0.464 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.340 / 0.500 / 0.883; 2: 0.349 / 0.500 / 0.950; 3: 0.324 / 0.467 / 0.917; 4: 0.343 / 0.550 / 0.933; 5: 0.330 / 0.433 / 0.917; 6: 0.375 / 0.633 / 0.900; 7: 0.349 / 0.517 / 0.950; 8: 0.311 / 0.417 / 0.983; 9: 0.363 / 0.600 / 0.983; 10: 0.347 / 0.517 / 0.967; 11: 0.359 / 0.567 / 0.950; 12: 0.318 / 0.450 / 0.967; 13: 0.362 / 0.533 / 0.967; 14: 0.336 / 0.500 / 0.950; 15: 0.362 / 0.583 / 0.950
- 6h: 1: 0.384 / 0.550 / 0.892; 2: 0.371 / 0.506 / 0.925; 3: 0.380 / 0.536 / 0.919; 4: 0.360 / 0.511 / 0.919; 5: 0.362 / 0.483 / 0.911; 6: 0.353 / 0.489 / 0.908; 7: 0.364 / 0.514 / 0.911; 8: 0.362 / 0.517 / 0.917; 9: 0.354 / 0.483 / 0.919; 10: 0.356 / 0.503 / 0.922; 11: 0.344 / 0.475 / 0.933; 12: 0.359 / 0.500 / 0.942; 13: 0.356 / 0.483 / 0.928; 14: 0.363 / 0.506 / 0.922; 15: 0.357 / 0.500 / 0.925
- 24h: 1: 0.377 / 0.539 / 0.899; 2: 0.369 / 0.519 / 0.906; 3: 0.368 / 0.520 / 0.905; 4: 0.357 / 0.487 / 0.906; 5: 0.362 / 0.513 / 0.911; 6: 0.364 / 0.517 / 0.911; 7: 0.358 / 0.490 / 0.914; 8: 0.363 / 0.510 / 0.916; 9: 0.356 / 0.492 / 0.910; 10: 0.361 / 0.509 / 0.911; 11: 0.358 / 0.497 / 0.911; 12: 0.362 / 0.505 / 0.912; 13: 0.353 / 0.485 / 0.917; 14: 0.359 / 0.501 / 0.913; 15: 0.358 / 0.490 / 0.916
- 7d: 1: 0.369 / 0.538 / 0.895; 2: 0.356 / 0.498 / 0.901; 3: 0.357 / 0.507 / 0.902; 4: 0.351 / 0.492 / 0.902; 5: 0.352 / 0.499 / 0.902; 6: 0.353 / 0.496 / 0.903; 7: 0.351 / 0.495 / 0.903; 8: 0.353 / 0.506 / 0.903; 9: 0.350 / 0.495 / 0.903; 10: 0.353 / 0.510 / 0.903; 11: 0.348 / 0.494 / 0.903; 12: 0.351 / 0.503 / 0.904; 13: 0.348 / 0.494 / 0.904; 14: 0.350 / 0.500 / 0.904; 15: 0.348 / 0.497 / 0.904
- 30d: 1: 0.360 / 0.521 / 0.899; 2: 0.350 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.500 / 0.900; 7: 0.348 / 0.499 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.074 (body 0.044, range 0.105); 'price stays where it was' would score 0.106; colour right 0.483; typical miss of the close 8.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.146 (body 0.104, range 0.187); 'price stays where it was' would score 0.126; colour right 0.489; typical miss of the close 10.7 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.129 (body 0.088, range 0.169); 'price stays where it was' would score 0.132; colour right 0.499; typical miss of the close 9.3 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.131 (body 0.090, range 0.172); 'price stays where it was' would score 0.134; colour right 0.507; typical miss of the close 8.5 bp; chain ended on the right side 0.545 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.8; 2: 0.199 / 4.4; 3: 0.167 / 5.9; 4: 0.132 / 6.5; 5: 0.121 / 7.1; 6: 0.110 / 7.6; 7: 0.104 / 8.0; 8: 0.097 / 8.3; 9: 0.087 / 8.2; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.078 / 9.8; 13: 0.068 / 10.0; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 117551, probability skill vs chance 0.2251, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9499 / long run 0.9361
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.300, naive rule 0.533, lift 2.94x
    - 24h: 59 calls (59 a day), hit rate 0.966, chance 0.292, naive rule 0.494, lift 3.31x
    - 7d: 408 calls (58 a day), hit rate 0.931, chance 0.296, naive rule 0.494, lift 3.15x
    - 30d: 1691 calls (56 a day), hit rate 0.937, chance 0.293, naive rule 0.489, lift 3.19x
  - next: threshold 0.5695, hit rate recent 0.6052 / long run 0.5854
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.300, lift 2.12x
    - 24h: 70 calls (70 a day), hit rate 0.557, chance 0.292, lift 1.91x
    - 7d: 763 calls (109 a day), hit rate 0.585, chance 0.296, lift 1.98x
    - 30d: 2784 calls (93 a day), hit rate 0.577, chance 0.293, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.517; 0.40: 480, 0.572; 0.45: 411, 0.643; 0.50: 358, 0.696; 0.55: 313, 0.737; 0.60: 266, 0.782; 0.65: 222, 0.808; 0.70: 176, 0.840; 0.75: 136, 0.875; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.426; 0.35: 499, 0.463; 0.40: 406, 0.497; 0.45: 309, 0.530; 0.50: 201, 0.561; 0.55: 91, 0.568; 0.60: 14, 0.618; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 117549, probability skill vs chance 0.219, widened contest next: False
  - now: threshold 0.677, hit rate recent 0.8146 / long run 0.822
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.215, naive rule 0.467, lift 3.22x
    - 24h: 54 calls (54 a day), hit rate 0.833, chance 0.192, naive rule 0.418, lift 4.33x
    - 7d: 357 calls (51 a day), hit rate 0.821, chance 0.190, naive rule 0.407, lift 4.33x
    - 30d: 1551 calls (52 a day), hit rate 0.831, chance 0.188, naive rule 0.399, lift 4.41x
  - next: threshold 0.4194, hit rate recent 0.5327 / long run 0.4671
    - 6h: 26 calls (106 a day), hit rate 0.577, chance 0.215, lift 2.68x
    - 24h: 135 calls (136 a day), hit rate 0.504, chance 0.192, lift 2.62x
    - 7d: 941 calls (135 a day), hit rate 0.457, chance 0.190, lift 2.41x
    - 30d: 2717 calls (91 a day), hit rate 0.463, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 344, 0.495; 0.40: 276, 0.567; 0.45: 223, 0.624; 0.50: 176, 0.672; 0.55: 134, 0.713; 0.60: 104, 0.756; 0.65: 76, 0.792; 0.70: 54, 0.829; 0.75: 31, 0.872; 0.80: 10, 0.905
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 250, 0.421; 0.40: 156, 0.448; 0.45: 70, 0.460; 0.50: 15, 0.486; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 117546, probability skill vs chance 0.1951, widened contest next: True
  - now: threshold 0.5603, hit rate recent 0.6477 / long run 0.6835
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.129, naive rule 0.373, lift 4.79x
    - 24h: 49 calls (49 a day), hit rate 0.633, chance 0.117, naive rule 0.317, lift 5.42x
    - 7d: 321 calls (46 a day), hit rate 0.670, chance 0.117, naive rule 0.319, lift 5.73x
    - 30d: 1522 calls (51 a day), hit rate 0.704, chance 0.121, naive rule 0.329, lift 5.82x
  - next: threshold 0.3416, hit rate recent 0.4173 / long run 0.3788
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.129, lift 3.50x
    - 24h: 120 calls (121 a day), hit rate 0.417, chance 0.117, lift 3.57x
    - 7d: 779 calls (111 a day), hit rate 0.376, chance 0.117, lift 3.22x
    - 30d: 2479 calls (83 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.424; 0.35: 191, 0.493; 0.40: 146, 0.548; 0.45: 112, 0.594; 0.50: 85, 0.635; 0.55: 62, 0.679; 0.60: 41, 0.725; 0.65: 23, 0.792; 0.70: 10, 0.843; 0.75: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.350; 0.35: 100, 0.377; 0.40: 38, 0.399; 0.45: 8, 0.430; 0.50: 1, 0.531
- **K=13**: model 1792713600, labels learned 117541, probability skill vs chance 0.181, widened contest next: False
  - now: threshold 0.4076, hit rate recent 0.529 / long run 0.5544
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.087, naive rule 0.333, lift 4.79x
    - 24h: 53 calls (54 a day), hit rate 0.528, chance 0.076, naive rule 0.275, lift 6.91x
    - 7d: 366 calls (52 a day), hit rate 0.538, chance 0.076, naive rule 0.275, lift 7.09x
    - 30d: 1551 calls (52 a day), hit rate 0.570, chance 0.077, naive rule 0.272, lift 7.37x
  - next: threshold 0.2918, hit rate recent 0.3023 / long run 0.313
    - 6h: 10 calls (42 a day), hit rate 0.100, chance 0.087, lift 1.15x
    - 24h: 65 calls (66 a day), hit rate 0.323, chance 0.076, lift 4.22x
    - 7d: 454 calls (65 a day), hit rate 0.322, chance 0.076, lift 4.24x
    - 30d: 2148 calls (72 a day), hit rate 0.306, chance 0.077, lift 3.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.448; 0.35: 86, 0.502; 0.40: 61, 0.555; 0.45: 41, 0.610; 0.50: 25, 0.660; 0.55: 14, 0.710; 0.60: 6, 0.754; 0.65: 2, 0.848
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.318; 0.35: 13, 0.350; 0.40: 2, 0.443; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.000 | 1.02% | 0.883 | 0.533 | 0.252 | 0.450 | 0.194 |
| 6h | 18.803 | 3.49% | 0.897 | 0.517 | 0.250 | 0.494 | 0.663 |
| 24h | 14.527 | 2.09% | 0.902 | 0.496 | 0.250 | 0.498 | 0.617 |
| 7d | 14.676 | 3.48% | 0.900 | 0.500 | 0.250 | 0.500 | 0.645 |
| 30d | 13.499 | 4.08% | 0.900 | 0.500 | 0.251 | 0.496 | 0.668 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.113 | 10.974 | 10.989 | 10.891 | 11.097 | 10.989 | 10.904 | 11.051 | 10.938 | 11.000 |
| 6h | 19.483 | 18.958 | 18.908 | 18.809 | 19.276 | 18.978 | 18.698 | 18.732 | 18.753 | 18.803 |
| 24h | 14.837 | 14.604 | 14.577 | 14.517 | 14.742 | 14.607 | 14.486 | 14.489 | 14.491 | 14.527 |
| 7d | 15.204 | 14.805 | 14.768 | 14.693 | 14.926 | 14.818 | 14.659 | 14.642 | 14.648 | 14.676 |
| 30d | 14.073 | 13.621 | 13.581 | 13.521 | 13.743 | 13.684 | 13.494 | 13.474 | 13.473 | 13.499 |

## Next candle

- candle starting 2026-10-23 19:17 UTC, last close 2393.92
- P(up) 0.5029, return quantiles (bp): {'05': -7.632, '10': -5.79, '25': -3.146, '40': -1.094, '50': 0.03, '60': 1.251, '75': 2.923, '90': 5.781, '95': 7.2}
- changepoint probability 0.0542, regime age 120.7 min
- agent weights: empirical 0.011, ewma 0.081, garch 0.102, har 0.178, bocpd 0.020, hmm 0.074, online_qr 0.287, lgbm 0.248

## Learning log

- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- HMM volatility states (sd, bp per minute): [4.3, 6.8, 17.27], current probabilities: [0.801, 0.196, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-10-23 19:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.294, 'l_abs': 0.686, 'l_hi': 0.778, 'l_lo': 0.789, 'b05': 0.702, 'b25': 0.677, 'b75': 0.608, 'b95': 0.684}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.11, 1.39, 1.576, 1.766, 1.978, 1.976, 2.203, 2.295, 2.237, 2.214, 2.317, 2.417, 2.564, 2.659]}
- calibration offsets (in sigma): {'05': 0.018, '10': -0.004, '25': -0.06, '40': -0.016, '50': 0.0, '60': 0.026, '75': -0.01, '90': -0.016, '95': -0.068}
