# ETH-USD 60s candle generator - report

- generated: 2026-10-23 22:22 UTC
- last closed candle: 2026-10-23 22:22 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: colour_path 0.498 in the last 7 days, -0.005 against the 7 before
- WIN RATE FALLING: overall 0.502 in the last 7 days, -0.004 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.542 (672) [0.504, 0.580] | 0.518 (2876) [0.498, 0.537] | 0.513 (4890) [0.499, 0.527] | 0.517 (1918) [0.492, 0.541] | 0.596 (89) | 0.500 | flat +0.035 (noise 0.029) |
| colour_clear | 0.545 (826) | 0.555 (5631) [0.546, 0.564] | 0.529 (23423) [0.520, 0.538] | 0.516 (39903) [0.510, 0.523] | 0.547 (15665) [0.542, 0.552] | 0.545 (792) | 0.500 | flat +0.015 (noise 0.009) |
| colour_confident | 0.585 (135) | 0.598 (1030) [0.581, 0.620] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.665 (191) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.529 (1435) | 0.535 (10022) [0.528, 0.542] | 0.519 (42861) [0.514, 0.525] | 0.512 (72891) [0.508, 0.516] | 0.530 (28542) [0.525, 0.535] | 0.540 (1336) | 0.500 | flat +0.011 (noise 0.007) |
| colour_path | 0.496 (20090) | 0.498 (140308) [0.496, 0.501] | 0.500 (600054) [0.499, 0.502] | 0.500 (1020474) [0.499, 0.501] | 0.500 (399588) [0.498, 0.502] | 0.503 (18704) | 0.500 | down -0.005 (noise 0.002) |
| colour_strong | 0.750 (16) | 0.628 (239) [0.595, 0.661] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.686 (51) | 0.500 | flat -0.054 (noise 0.044) |
| reversal_k13_next | 0.245 (49) | 0.315 (457) [0.296, 0.332] | 0.305 (2131) [0.293, 0.317] | 0.307 (3486) [0.296, 0.318] | 0.318 (1381) [0.306, 0.330] | 0.328 (61) | 0.077 | flat -0.002 (noise 0.031) |
| reversal_k13_now | 0.605 (38) | 0.538 (383) [0.504, 0.576] | 0.572 (1549) [0.553, 0.592] | 0.574 (2542) [0.559, 0.591] | 0.565 (1070) [0.542, 0.590] | 0.500 (52) | 0.077 | flat -0.037 (noise 0.037) |
| reversal_k3_next | 0.604 (96) | 0.581 (826) [0.557, 0.610] | 0.575 (2772) [0.562, 0.589] | 0.583 (4445) [0.572, 0.594] | 0.578 (2005) [0.563, 0.593] | 0.590 (61) | 0.293 | flat +0.003 (noise 0.025) |
| reversal_k3_now | 0.924 (53) | 0.933 (405) [0.909, 0.958] | 0.934 (1694) [0.926, 0.943] | 0.937 (2911) [0.931, 0.944] | 0.930 (1148) [0.920, 0.941] | 0.951 (61) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.485 (132) | 0.441 (938) [0.420, 0.462] | 0.463 (2650) [0.448, 0.477] | 0.474 (4049) [0.461, 0.487] | 0.455 (2059) [0.439, 0.472] | 0.533 (120) | 0.187 | flat -0.046 (noise 0.026) |
| reversal_k5_now | 0.829 (41) | 0.827 (364) [0.809, 0.845] | 0.830 (1557) [0.817, 0.844] | 0.831 (2658) [0.819, 0.842] | 0.820 (1047) [0.805, 0.836] | 0.830 (53) | 0.187 | flat +0.015 (noise 0.029) |
| reversal_k8_next | 0.337 (101) | 0.360 (784) [0.335, 0.382] | 0.383 (2416) [0.369, 0.396] | 0.388 (3975) [0.376, 0.401] | 0.379 (1869) [0.364, 0.396] | 0.421 (114) | 0.121 | flat -0.042 (noise 0.027) |
| reversal_k8_now | 0.737 (38) | 0.677 (328) [0.639, 0.715] | 0.707 (1527) [0.687, 0.727] | 0.704 (2628) [0.689, 0.720] | 0.690 (1041) [0.666, 0.714] | 0.588 (51) | 0.121 | flat -0.003 (noise 0.036) |
| overall | 0.499 (22169) | 0.502 (155487) [0.500, 0.505] | 0.503 (662087) [0.502, 0.505] | 0.503 (1124949) [0.502, 0.504] | 0.504 (441668) [0.502, 0.506] | 0.508 (20702) | - | down -0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06984, 0.1029] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5378, 'levels': [{'threshold': 0.06984, 'calls_per_day': 146.7, 'win_rate': 0.6002}, {'threshold': 0.1029, 'calls_per_day': 36.9, 'win_rate': 0.6538}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 28740, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15328 | 0.337 | 0.523 (15081) | 0.588 (1552) | 0.765 (2517) |
| volatility: normal | 15327 | 0.366 | 0.521 (15260) | 0.628 (950) | 0.752 (2257) |
| volatility: wild | 15327 | 0.379 | 0.515 (15291) | 0.616 (411) | 0.773 (1988) |
| session: Asia 00-08 | 15360 | 0.359 | 0.526 (15260) | 0.614 (1041) | 0.765 (2221) |
| session: Europe 08-13 | 9600 | 0.355 | 0.520 (9515) | 0.601 (710) | 0.764 (1531) |
| session: US 13-21 | 15360 | 0.369 | 0.515 (15258) | 0.587 (726) | 0.768 (2174) |
| session: late 21-24 | 5662 | 0.351 | 0.515 (5599) | 0.622 (436) | 0.743 (836) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.341 | 0.338 | 0.276 | 0.276 | 0.559 | 0.234 | 0.448 | 1.347 |
| 6h | 360 | 0.373 | 0.364 | 0.271 | 0.333 | 0.526 | 0.268 | 0.478 | 1.237 |
| 24h | 1440 | 0.377 | 0.364 | 0.271 | 0.306 | 0.538 | 0.274 | 0.481 | 1.253 |
| 7d | 10080 | 0.369 | 0.359 | 0.271 | 0.304 | 0.538 | 0.268 | 0.470 | 1.221 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.521 | 0.255 | 0.464 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.341 / 0.559 / 0.900; 2: 0.322 / 0.475 / 0.783; 3: 0.346 / 0.508 / 0.733; 4: 0.337 / 0.458 / 0.767; 5: 0.341 / 0.492 / 0.700; 6: 0.349 / 0.508 / 0.750; 7: 0.326 / 0.475 / 0.717; 8: 0.367 / 0.627 / 0.733; 9: 0.321 / 0.458 / 0.750; 10: 0.351 / 0.508 / 0.717; 11: 0.312 / 0.424 / 0.683; 12: 0.361 / 0.576 / 0.700; 13: 0.345 / 0.542 / 0.717; 14: 0.327 / 0.441 / 0.833; 15: 0.337 / 0.559 / 0.917
- 6h: 1: 0.373 / 0.526 / 0.889; 2: 0.361 / 0.507 / 0.883; 3: 0.380 / 0.549 / 0.883; 4: 0.359 / 0.507 / 0.883; 5: 0.363 / 0.493 / 0.875; 6: 0.359 / 0.496 / 0.894; 7: 0.363 / 0.487 / 0.886; 8: 0.366 / 0.532 / 0.919; 9: 0.370 / 0.532 / 0.914; 10: 0.358 / 0.485 / 0.900; 11: 0.351 / 0.465 / 0.886; 12: 0.360 / 0.501 / 0.886; 13: 0.362 / 0.496 / 0.881; 14: 0.365 / 0.507 / 0.897; 15: 0.364 / 0.521 / 0.903
- 24h: 1: 0.377 / 0.538 / 0.901; 2: 0.368 / 0.517 / 0.903; 3: 0.371 / 0.529 / 0.904; 4: 0.356 / 0.484 / 0.903; 5: 0.363 / 0.510 / 0.903; 6: 0.363 / 0.507 / 0.908; 7: 0.361 / 0.497 / 0.904; 8: 0.364 / 0.513 / 0.910; 9: 0.360 / 0.502 / 0.912; 10: 0.362 / 0.508 / 0.915; 11: 0.358 / 0.492 / 0.919; 12: 0.365 / 0.510 / 0.918; 13: 0.357 / 0.495 / 0.917; 14: 0.359 / 0.493 / 0.925; 15: 0.359 / 0.493 / 0.924
- 7d: 1: 0.369 / 0.538 / 0.894; 2: 0.356 / 0.498 / 0.899; 3: 0.358 / 0.509 / 0.899; 4: 0.351 / 0.492 / 0.899; 5: 0.352 / 0.499 / 0.899; 6: 0.353 / 0.496 / 0.900; 7: 0.351 / 0.495 / 0.900; 8: 0.354 / 0.507 / 0.900; 9: 0.351 / 0.496 / 0.901; 10: 0.353 / 0.508 / 0.901; 11: 0.348 / 0.494 / 0.900; 12: 0.351 / 0.503 / 0.901; 13: 0.348 / 0.493 / 0.901; 14: 0.351 / 0.500 / 0.902; 15: 0.348 / 0.498 / 0.902
- 30d: 1: 0.360 / 0.521 / 0.899; 2: 0.350 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.500 / 0.900; 7: 0.348 / 0.499 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.119 (body 0.092, range 0.145); 'price stays where it was' would score 0.142; colour right 0.576; typical miss of the close 5.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.090, range 0.168); 'price stays where it was' would score 0.133; colour right 0.538; typical miss of the close 7.1 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.132 (body 0.091, range 0.173); 'price stays where it was' would score 0.138; colour right 0.503; typical miss of the close 8.4 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.131 (body 0.090, range 0.171); 'price stays where it was' would score 0.134; colour right 0.507; typical miss of the close 8.4 bp; chain ended on the right side 0.545 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.198 / 4.4; 3: 0.167 / 5.9; 4: 0.131 / 6.5; 5: 0.121 / 7.1; 6: 0.110 / 7.6; 7: 0.104 / 8.0; 8: 0.097 / 8.3; 9: 0.088 / 8.2; 10: 0.086 / 9.0; 11: 0.083 / 9.5; 12: 0.078 / 9.8; 13: 0.068 / 10.0; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 117736, probability skill vs chance 0.2302, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9418 / long run 0.9355
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.311, naive rule 0.540, lift 2.83x
    - 24h: 64 calls (64 a day), hit rate 0.953, chance 0.297, naive rule 0.505, lift 3.21x
    - 7d: 411 calls (59 a day), hit rate 0.929, chance 0.297, naive rule 0.497, lift 3.13x
    - 30d: 1691 calls (56 a day), hit rate 0.936, chance 0.293, naive rule 0.489, lift 3.19x
  - next: threshold 0.5695, hit rate recent 0.6111 / long run 0.5862
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.311, lift 2.22x
    - 24h: 66 calls (66 a day), hit rate 0.591, chance 0.297, lift 1.99x
    - 7d: 761 calls (109 a day), hit rate 0.585, chance 0.297, lift 1.97x
    - 30d: 2787 calls (93 a day), hit rate 0.577, chance 0.293, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.517; 0.40: 480, 0.572; 0.45: 411, 0.643; 0.50: 358, 0.696; 0.55: 313, 0.737; 0.60: 265, 0.783; 0.65: 222, 0.808; 0.70: 176, 0.840; 0.75: 136, 0.875; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.426; 0.35: 499, 0.464; 0.40: 406, 0.497; 0.45: 309, 0.530; 0.50: 201, 0.561; 0.55: 91, 0.569; 0.60: 14, 0.619; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 117734, probability skill vs chance 0.22, widened contest next: False
  - now: threshold 0.677, hit rate recent 0.8295 / long run 0.8235
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.200, naive rule 0.433, lift 4.17x
    - 24h: 55 calls (55 a day), hit rate 0.836, chance 0.192, naive rule 0.419, lift 4.35x
    - 7d: 356 calls (51 a day), hit rate 0.820, chance 0.190, naive rule 0.408, lift 4.33x
    - 30d: 1548 calls (52 a day), hit rate 0.831, chance 0.188, naive rule 0.399, lift 4.42x
  - next: threshold 0.4194, hit rate recent 0.5324 / long run 0.4687
    - 6h: 30 calls (122 a day), hit rate 0.567, chance 0.200, lift 2.84x
    - 24h: 131 calls (132 a day), hit rate 0.527, chance 0.192, lift 2.74x
    - 7d: 948 calls (136 a day), hit rate 0.458, chance 0.190, lift 2.42x
    - 30d: 2726 calls (91 a day), hit rate 0.463, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 344, 0.495; 0.40: 276, 0.567; 0.45: 223, 0.624; 0.50: 176, 0.672; 0.55: 134, 0.713; 0.60: 104, 0.756; 0.65: 76, 0.793; 0.70: 54, 0.829; 0.75: 31, 0.872; 0.80: 10, 0.905
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 250, 0.421; 0.40: 156, 0.448; 0.45: 69, 0.460; 0.50: 15, 0.485; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 117731, probability skill vs chance 0.1949, widened contest next: True
  - now: threshold 0.5603, hit rate recent 0.6339 / long run 0.6817
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.141, naive rule 0.406, lift 3.81x
    - 24h: 53 calls (53 a day), hit rate 0.604, chance 0.117, naive rule 0.325, lift 5.15x
    - 7d: 323 calls (46 a day), hit rate 0.666, chance 0.117, naive rule 0.322, lift 5.67x
    - 30d: 1520 calls (51 a day), hit rate 0.702, chance 0.121, naive rule 0.329, lift 5.80x
  - next: threshold 0.3416, hit rate recent 0.4212 / long run 0.38
    - 6h: 20 calls (82 a day), hit rate 0.500, chance 0.141, lift 3.54x
    - 24h: 122 calls (123 a day), hit rate 0.418, chance 0.117, lift 3.57x
    - 7d: 782 calls (112 a day), hit rate 0.380, chance 0.117, lift 3.23x
    - 30d: 2484 calls (83 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.424; 0.35: 191, 0.494; 0.40: 146, 0.549; 0.45: 112, 0.595; 0.50: 85, 0.634; 0.55: 62, 0.677; 0.60: 41, 0.723; 0.65: 23, 0.789; 0.70: 10, 0.840; 0.75: 1, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.350; 0.35: 100, 0.378; 0.40: 38, 0.399; 0.45: 8, 0.430; 0.50: 1, 0.531
- **K=13**: model 1792713600, labels learned 117726, probability skill vs chance 0.18, widened contest next: False
  - now: threshold 0.4076, hit rate recent 0.5271 / long run 0.5541
    - 6h: 10 calls (42 a day), hit rate 0.400, chance 0.087, naive rule 0.364, lift 4.60x
    - 24h: 55 calls (56 a day), hit rate 0.509, chance 0.078, naive rule 0.285, lift 6.57x
    - 7d: 365 calls (52 a day), hit rate 0.532, chance 0.076, naive rule 0.277, lift 7.01x
    - 30d: 1548 calls (52 a day), hit rate 0.568, chance 0.077, naive rule 0.272, lift 7.36x
  - next: threshold 0.2918, hit rate recent 0.3015 / long run 0.3126
    - 6h: 7 calls (29 a day), hit rate 0.286, chance 0.087, lift 3.29x
    - 24h: 66 calls (67 a day), hit rate 0.333, chance 0.078, lift 4.30x
    - 7d: 459 calls (66 a day), hit rate 0.320, chance 0.076, lift 4.22x
    - 30d: 2150 calls (72 a day), hit rate 0.305, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.447; 0.35: 86, 0.500; 0.40: 61, 0.554; 0.45: 41, 0.608; 0.50: 25, 0.658; 0.55: 14, 0.708; 0.60: 6, 0.751; 0.65: 2, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.318; 0.35: 13, 0.349; 0.40: 2, 0.443; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.888 | 5.13% | 0.900 | 0.567 | 0.250 | 0.492 | 0.274 |
| 6h | 11.625 | 1.51% | 0.894 | 0.514 | 0.250 | 0.490 | 0.408 |
| 24h | 14.165 | 2.34% | 0.905 | 0.499 | 0.250 | 0.497 | 0.641 |
| 7d | 14.611 | 3.49% | 0.900 | 0.500 | 0.250 | 0.500 | 0.646 |
| 30d | 13.488 | 4.07% | 0.900 | 0.500 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.368 | 8.851 | 8.944 | 8.822 | 9.051 | 9.148 | 8.931 | 8.891 | 8.878 | 8.888 |
| 6h | 11.803 | 11.639 | 11.689 | 11.615 | 11.775 | 11.719 | 11.583 | 11.642 | 11.600 | 11.625 |
| 24h | 14.504 | 14.247 | 14.225 | 14.156 | 14.397 | 14.261 | 14.121 | 14.138 | 14.132 | 14.165 |
| 7d | 15.139 | 14.738 | 14.703 | 14.628 | 14.859 | 14.754 | 14.594 | 14.579 | 14.584 | 14.611 |
| 30d | 14.061 | 13.610 | 13.571 | 13.510 | 13.731 | 13.674 | 13.484 | 13.465 | 13.463 | 13.488 |

## Next candle

- candle starting 2026-10-23 22:22 UTC, last close 2393.06
- P(up) 0.4983, return quantiles (bp): {'05': -6.295, '10': -4.666, '25': -2.369, '40': -1.039, '50': -0.01, '60': 0.87, '75': 2.573, '90': 4.791, '95': 6.317}
- changepoint probability 0.0728, regime age 158.9 min
- agent weights: empirical 0.013, ewma 0.105, garch 0.110, har 0.186, bocpd 0.028, hmm 0.074, online_qr 0.264, lgbm 0.220

## Learning log

- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- HMM volatility states (sd, bp per minute): [4.3, 6.8, 17.27], current probabilities: [0.865, 0.132, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-10-23 22:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.25, 'l_abs': 0.683, 'l_hi': 0.779, 'l_lo': 0.794, 'b05': 0.702, 'b25': 0.676, 'b75': 0.597, 'b95': 0.69}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.426, 1.821, 2.024, 2.268, 2.208, 2.588, 2.509, 2.613, 2.706, 3.019, 3.223, 3.295, 2.862, 2.852]}
- calibration offsets (in sigma): {'05': 0.0305, '10': 0.011, '25': -0.0175, '40': -0.066, '50': -0.025, '60': -0.034, '75': -0.0025, '90': -0.051, '95': -0.0605}
