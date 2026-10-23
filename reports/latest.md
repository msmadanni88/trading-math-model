# ETH-USD 60s candle generator - report

- generated: 2026-10-23 15:12 UTC
- last closed candle: 2026-10-23 15:12 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: colour_path 0.498 in the last 7 days, -0.005 against the 7 before
- WIN RATE FALLING: overall 0.502 in the last 7 days, -0.004 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.542 (672) [0.504, 0.580] | 0.518 (2876) [0.498, 0.537] | 0.513 (4890) [0.499, 0.527] | 0.517 (1918) [0.492, 0.541] | 0.617 (60) | 0.500 | flat +0.035 (noise 0.029) |
| colour_clear | 0.545 (826) | 0.555 (5631) [0.546, 0.564] | 0.529 (23423) [0.520, 0.538] | 0.516 (39903) [0.510, 0.523] | 0.547 (15665) [0.542, 0.552] | 0.539 (557) | 0.500 | flat +0.015 (noise 0.009) |
| colour_confident | 0.585 (135) | 0.598 (1030) [0.581, 0.620] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.656 (128) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.529 (1435) | 0.535 (10022) [0.528, 0.542] | 0.519 (42861) [0.514, 0.525] | 0.512 (72891) [0.508, 0.516] | 0.530 (28542) [0.525, 0.535] | 0.539 (907) | 0.500 | flat +0.011 (noise 0.007) |
| colour_path | 0.496 (20090) | 0.498 (140308) [0.496, 0.501] | 0.500 (600054) [0.499, 0.502] | 0.500 (1020474) [0.499, 0.501] | 0.500 (399588) [0.498, 0.502] | 0.501 (12698) | 0.500 | down -0.005 (noise 0.002) |
| colour_strong | 0.750 (16) | 0.628 (239) [0.595, 0.661] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.667 (36) | 0.500 | flat -0.054 (noise 0.044) |
| reversal_k13_next | 0.245 (49) | 0.315 (457) [0.296, 0.332] | 0.305 (2131) [0.293, 0.317] | 0.307 (3486) [0.296, 0.318] | 0.318 (1381) [0.306, 0.330] | 0.333 (51) | 0.077 | flat -0.002 (noise 0.031) |
| reversal_k13_now | 0.605 (38) | 0.538 (383) [0.504, 0.576] | 0.572 (1549) [0.553, 0.592] | 0.574 (2542) [0.559, 0.591] | 0.565 (1070) [0.542, 0.590] | 0.512 (41) | 0.077 | flat -0.037 (noise 0.037) |
| reversal_k3_next | 0.604 (96) | 0.581 (826) [0.557, 0.610] | 0.575 (2772) [0.562, 0.589] | 0.583 (4445) [0.572, 0.594] | 0.578 (2005) [0.563, 0.593] | 0.562 (48) | 0.293 | flat +0.003 (noise 0.025) |
| reversal_k3_now | 0.924 (53) | 0.933 (405) [0.909, 0.958] | 0.934 (1694) [0.926, 0.943] | 0.937 (2911) [0.931, 0.944] | 0.930 (1148) [0.920, 0.941] | 0.975 (40) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.485 (132) | 0.441 (938) [0.420, 0.462] | 0.463 (2650) [0.448, 0.477] | 0.474 (4049) [0.461, 0.487] | 0.455 (2059) [0.439, 0.472] | 0.500 (86) | 0.187 | flat -0.046 (noise 0.026) |
| reversal_k5_now | 0.829 (41) | 0.827 (364) [0.809, 0.845] | 0.830 (1557) [0.817, 0.844] | 0.831 (2658) [0.819, 0.842] | 0.820 (1047) [0.805, 0.836] | 0.825 (40) | 0.187 | flat +0.015 (noise 0.029) |
| reversal_k8_next | 0.337 (101) | 0.360 (784) [0.335, 0.382] | 0.383 (2416) [0.369, 0.396] | 0.388 (3975) [0.376, 0.401] | 0.379 (1869) [0.364, 0.396] | 0.407 (91) | 0.121 | flat -0.042 (noise 0.027) |
| reversal_k8_now | 0.737 (38) | 0.677 (328) [0.639, 0.715] | 0.707 (1527) [0.687, 0.727] | 0.704 (2628) [0.689, 0.720] | 0.690 (1041) [0.666, 0.714] | 0.595 (37) | 0.121 | flat -0.003 (noise 0.036) |
| overall | 0.499 (22169) | 0.502 (155487) [0.500, 0.505] | 0.503 (662087) [0.502, 0.505] | 0.503 (1124949) [0.502, 0.504] | 0.504 (441668) [0.502, 0.506] | 0.506 (14099) | - | down -0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06931, 0.1026] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5367, 'levels': [{'threshold': 0.06931, 'calls_per_day': 145.7, 'win_rate': 0.5965}, {'threshold': 0.1026, 'calls_per_day': 36.5, 'win_rate': 0.6459}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 28311, 'rate': 0.5313}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15184 | 0.337 | 0.523 (14938) | 0.588 (1530) | 0.765 (2487) |
| volatility: normal | 15184 | 0.366 | 0.521 (15117) | 0.623 (923) | 0.753 (2241) |
| volatility: wild | 15184 | 0.379 | 0.515 (15148) | 0.617 (397) | 0.773 (1975) |
| session: Asia 00-08 | 15360 | 0.359 | 0.526 (15260) | 0.614 (1041) | 0.765 (2221) |
| session: Europe 08-13 | 9600 | 0.355 | 0.520 (9515) | 0.601 (710) | 0.764 (1531) |
| session: US 13-21 | 15012 | 0.368 | 0.514 (14910) | 0.580 (678) | 0.769 (2129) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5518) | 0.620 (421) | 0.742 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.420 | 0.370 | 0.299 | 0.299 | 0.633 | 0.320 | 0.519 | 1.357 |
| 6h | 360 | 0.378 | 0.372 | 0.279 | 0.319 | 0.526 | 0.272 | 0.483 | 1.072 |
| 24h | 1440 | 0.378 | 0.366 | 0.274 | 0.305 | 0.535 | 0.273 | 0.483 | 1.242 |
| 7d | 10080 | 0.370 | 0.360 | 0.272 | 0.304 | 0.538 | 0.268 | 0.471 | 1.222 |
| 30d | 43200 | 0.360 | 0.354 | 0.278 | 0.306 | 0.521 | 0.255 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.420 / 0.633 / 0.933; 2: 0.363 / 0.500 / 0.900; 3: 0.370 / 0.483 / 0.883; 4: 0.375 / 0.533 / 0.867; 5: 0.377 / 0.500 / 0.850; 6: 0.357 / 0.550 / 0.850; 7: 0.378 / 0.583 / 0.783; 8: 0.360 / 0.500 / 0.800; 9: 0.354 / 0.433 / 0.800; 10: 0.381 / 0.583 / 0.783; 11: 0.361 / 0.533 / 0.800; 12: 0.378 / 0.517 / 0.783; 13: 0.347 / 0.467 / 0.767; 14: 0.351 / 0.400 / 0.817; 15: 0.386 / 0.550 / 0.833
- 6h: 1: 0.378 / 0.526 / 0.892; 2: 0.362 / 0.493 / 0.911; 3: 0.370 / 0.507 / 0.900; 4: 0.355 / 0.457 / 0.900; 5: 0.372 / 0.529 / 0.906; 6: 0.375 / 0.529 / 0.906; 7: 0.367 / 0.504 / 0.892; 8: 0.368 / 0.515 / 0.858; 9: 0.356 / 0.485 / 0.878; 10: 0.361 / 0.501 / 0.897; 11: 0.357 / 0.482 / 0.900; 12: 0.368 / 0.510 / 0.903; 13: 0.359 / 0.504 / 0.897; 14: 0.356 / 0.462 / 0.911; 15: 0.368 / 0.487 / 0.917
- 24h: 1: 0.378 / 0.535 / 0.901; 2: 0.371 / 0.526 / 0.901; 3: 0.367 / 0.514 / 0.902; 4: 0.358 / 0.489 / 0.897; 5: 0.363 / 0.519 / 0.898; 6: 0.366 / 0.521 / 0.897; 7: 0.354 / 0.477 / 0.896; 8: 0.364 / 0.510 / 0.888; 9: 0.356 / 0.488 / 0.892; 10: 0.360 / 0.507 / 0.894; 11: 0.361 / 0.504 / 0.894; 12: 0.363 / 0.505 / 0.894; 13: 0.354 / 0.487 / 0.889; 14: 0.358 / 0.487 / 0.892; 15: 0.358 / 0.491 / 0.893
- 7d: 1: 0.370 / 0.538 / 0.896; 2: 0.356 / 0.497 / 0.900; 3: 0.357 / 0.505 / 0.900; 4: 0.352 / 0.492 / 0.900; 5: 0.353 / 0.499 / 0.901; 6: 0.353 / 0.496 / 0.901; 7: 0.351 / 0.495 / 0.901; 8: 0.354 / 0.506 / 0.900; 9: 0.351 / 0.496 / 0.901; 10: 0.354 / 0.509 / 0.902; 11: 0.348 / 0.495 / 0.902; 12: 0.351 / 0.503 / 0.902; 13: 0.349 / 0.494 / 0.902; 14: 0.350 / 0.499 / 0.902; 15: 0.349 / 0.499 / 0.902
- 30d: 1: 0.360 / 0.521 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.497 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.499 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.112 (body 0.092, range 0.132); 'price stays where it was' would score 0.110; colour right 0.533; typical miss of the close 29.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.163 (body 0.118, range 0.208); 'price stays where it was' would score 0.160; colour right 0.487; typical miss of the close 8.2 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.130 (body 0.089, range 0.171); 'price stays where it was' would score 0.138; colour right 0.493; typical miss of the close 9.8 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.130 (body 0.089, range 0.171); 'price stays where it was' would score 0.134; colour right 0.507; typical miss of the close 8.6 bp; chain ended on the right side 0.551 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.162); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.8; 2: 0.199 / 4.4; 3: 0.168 / 6.0; 4: 0.132 / 6.5; 5: 0.121 / 7.2; 6: 0.111 / 7.7; 7: 0.104 / 8.1; 8: 0.097 / 8.3; 9: 0.087 / 8.2; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.078 / 9.9; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 117306, probability skill vs chance 0.2206, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9585 / long run 0.9366
    - 6h: 17 calls (69 a day), hit rate 0.941, chance 0.299, naive rule 0.502, lift 3.15x
    - 24h: 55 calls (55 a day), hit rate 0.982, chance 0.301, naive rule 0.498, lift 3.26x
    - 7d: 400 calls (57 a day), hit rate 0.932, chance 0.295, naive rule 0.490, lift 3.17x
    - 30d: 1686 calls (56 a day), hit rate 0.937, chance 0.293, naive rule 0.489, lift 3.19x
  - next: threshold 0.5664, hit rate recent 0.5915 / long run 0.5839
    - 6h: 15 calls (61 a day), hit rate 0.533, chance 0.299, lift 1.79x
    - 24h: 71 calls (71 a day), hit rate 0.563, chance 0.301, lift 1.87x
    - 7d: 776 calls (111 a day), hit rate 0.580, chance 0.295, lift 1.97x
    - 30d: 2781 calls (93 a day), hit rate 0.576, chance 0.293, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.516; 0.40: 481, 0.571; 0.45: 411, 0.643; 0.50: 358, 0.695; 0.55: 313, 0.737; 0.60: 266, 0.782; 0.65: 222, 0.808; 0.70: 177, 0.840; 0.75: 136, 0.874; 0.80: 92, 0.912; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.426; 0.35: 499, 0.463; 0.40: 406, 0.497; 0.45: 309, 0.530; 0.50: 200, 0.561; 0.55: 90, 0.567; 0.60: 14, 0.617; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 117304, probability skill vs chance 0.2173, widened contest next: False
  - now: threshold 0.6788, hit rate recent 0.8248 / long run 0.823
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.188, naive rule 0.419, lift 4.17x
    - 24h: 52 calls (52 a day), hit rate 0.865, chance 0.187, naive rule 0.409, lift 4.63x
    - 7d: 353 calls (50 a day), hit rate 0.824, chance 0.188, naive rule 0.403, lift 4.38x
    - 30d: 1551 calls (52 a day), hit rate 0.831, chance 0.188, naive rule 0.398, lift 4.42x
  - next: threshold 0.42, hit rate recent 0.4846 / long run 0.4601
    - 6h: 31 calls (126 a day), hit rate 0.452, chance 0.188, lift 2.40x
    - 24h: 136 calls (137 a day), hit rate 0.485, chance 0.187, lift 2.59x
    - 7d: 944 calls (135 a day), hit rate 0.450, chance 0.188, lift 2.39x
    - 30d: 2702 calls (90 a day), hit rate 0.462, chance 0.188, lift 2.45x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 344, 0.494; 0.40: 276, 0.566; 0.45: 223, 0.624; 0.50: 176, 0.672; 0.55: 135, 0.714; 0.60: 104, 0.757; 0.65: 76, 0.793; 0.70: 54, 0.829; 0.75: 31, 0.873; 0.80: 10, 0.908
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 250, 0.421; 0.40: 156, 0.448; 0.45: 70, 0.460; 0.50: 15, 0.487; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 117301, probability skill vs chance 0.196, widened contest next: True
  - now: threshold 0.5618, hit rate recent 0.6511 / long run 0.6843
    - 6h: 15 calls (62 a day), hit rate 0.400, chance 0.107, naive rule 0.297, lift 3.73x
    - 24h: 48 calls (48 a day), hit rate 0.667, chance 0.115, naive rule 0.311, lift 5.78x
    - 7d: 321 calls (46 a day), hit rate 0.670, chance 0.116, naive rule 0.315, lift 5.76x
    - 30d: 1524 calls (51 a day), hit rate 0.705, chance 0.121, naive rule 0.329, lift 5.82x
  - next: threshold 0.3454, hit rate recent 0.3944 / long run 0.3761
    - 6h: 37 calls (152 a day), hit rate 0.351, chance 0.107, lift 3.28x
    - 24h: 122 calls (123 a day), hit rate 0.393, chance 0.115, lift 3.41x
    - 7d: 792 calls (113 a day), hit rate 0.370, chance 0.116, lift 3.18x
    - 30d: 2472 calls (82 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.424; 0.35: 191, 0.494; 0.40: 146, 0.549; 0.45: 112, 0.595; 0.50: 86, 0.636; 0.55: 62, 0.680; 0.60: 42, 0.726; 0.65: 23, 0.791; 0.70: 10, 0.843; 0.75: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 100, 0.378; 0.40: 38, 0.399; 0.45: 8, 0.430; 0.50: 1, 0.531
- **K=13**: model 1792713600, labels learned 117296, probability skill vs chance 0.1843, widened contest next: False
  - now: threshold 0.4093, hit rate recent 0.5415 / long run 0.5559
    - 6h: 17 calls (71 a day), hit rate 0.353, chance 0.070, naive rule 0.223, lift 5.07x
    - 24h: 52 calls (53 a day), hit rate 0.538, chance 0.077, naive rule 0.271, lift 6.98x
    - 7d: 371 calls (53 a day), hit rate 0.536, chance 0.075, naive rule 0.271, lift 7.11x
    - 30d: 1552 calls (52 a day), hit rate 0.571, chance 0.077, naive rule 0.272, lift 7.38x
  - next: threshold 0.2903, hit rate recent 0.3006 / long run 0.3128
    - 6h: 23 calls (96 a day), hit rate 0.217, chance 0.070, lift 3.12x
    - 24h: 69 calls (70 a day), hit rate 0.304, chance 0.077, lift 3.94x
    - 7d: 465 calls (67 a day), hit rate 0.314, chance 0.075, lift 4.16x
    - 30d: 2150 calls (72 a day), hit rate 0.306, chance 0.077, lift 3.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.448; 0.35: 86, 0.503; 0.40: 61, 0.556; 0.45: 41, 0.609; 0.50: 25, 0.660; 0.55: 14, 0.711; 0.60: 6, 0.759; 0.65: 2, 0.848
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.317; 0.35: 13, 0.350; 0.40: 2, 0.443; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 31.981 | 7.17% | 0.933 | 0.533 | 0.250 | 0.467 | 0.392 |
| 6h | 18.551 | 3.14% | 0.897 | 0.483 | 0.250 | 0.510 | 0.668 |
| 24h | 15.519 | 2.40% | 0.903 | 0.500 | 0.250 | 0.502 | 0.643 |
| 7d | 14.954 | 3.66% | 0.900 | 0.499 | 0.250 | 0.500 | 0.652 |
| 30d | 13.528 | 4.08% | 0.900 | 0.500 | 0.251 | 0.496 | 0.668 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 34.452 | 32.315 | 32.280 | 31.984 | 33.040 | 32.669 | 31.779 | 31.714 | 31.870 | 31.981 |
| 6h | 19.152 | 18.655 | 18.622 | 18.606 | 18.941 | 18.720 | 18.503 | 18.434 | 18.512 | 18.551 |
| 24h | 15.900 | 15.604 | 15.576 | 15.516 | 15.761 | 15.608 | 15.480 | 15.475 | 15.481 | 15.519 |
| 7d | 15.523 | 15.094 | 15.044 | 14.976 | 15.211 | 15.093 | 14.942 | 14.925 | 14.928 | 14.954 |
| 30d | 14.103 | 13.651 | 13.611 | 13.550 | 13.772 | 13.713 | 13.524 | 13.503 | 13.503 | 13.528 |

## Next candle

- candle starting 2026-10-23 15:12 UTC, last close 2398.86
- P(up) 0.4893, return quantiles (bp): {'05': -15.746, '10': -12.192, '25': -6.887, '40': -2.828, '50': -0.278, '60': 2.374, '75': 6.688, '90': 12.52, '95': 15.025}
- changepoint probability 0.0265, regime age 85.0 min
- agent weights: empirical 0.005, ewma 0.075, garch 0.092, har 0.172, bocpd 0.015, hmm 0.058, online_qr 0.259, lgbm 0.324

## Learning log

- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- HMM volatility states (sd, bp per minute): [4.3, 6.8, 17.27], current probabilities: [0.006, 0.895, 0.099]
- live generator: {'versions': 60, 'latest_effective': '2026-10-23 15:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.193, 'l_abs': 0.701, 'l_hi': 0.764, 'l_lo': 0.773, 'b05': 0.71, 'b25': 0.685, 'b75': 0.617, 'b95': 0.677}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.397, 1.821, 2.065, 2.179, 2.391, 2.694, 3.319, 3.322, 3.112, 3.142, 3.355, 3.295, 3.227, 3.347]}
- calibration offsets (in sigma): {'05': 0.0255, '10': -0.009, '25': -0.0525, '40': -0.036, '50': -0.005, '60': 0.026, '75': 0.0725, '90': 0.059, '95': -0.0555}
