# ETH-USD 60s candle generator - report

- generated: 2026-10-22 14:42 UTC
- last closed candle: 2026-10-22 14:42 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_next 0.434 in the last 7 days, -0.055 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.543 (672) [0.507, 0.580] | 0.520 (2876) [0.500, 0.540] | 0.515 (4794) [0.500, 0.529] | 0.520 (1822) [0.492, 0.545] | 0.448 (58) | 0.500 | flat +0.038 (noise 0.027) |
| colour_clear | 0.550 (816) | 0.555 (5596) [0.546, 0.564] | 0.528 (23440) [0.519, 0.537] | 0.516 (39077) [0.509, 0.523] | 0.547 (14839) [0.541, 0.553] | 0.527 (510) | 0.500 | flat +0.014 (noise 0.009) |
| colour_confident | 0.602 (176) | 0.600 (979) [0.581, 0.622] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.584 (77) | 0.500 | flat +0.001 (noise 0.023) |
| colour_next | 0.533 (1434) | 0.534 (10023) [0.525, 0.542] | 0.519 (42861) [0.513, 0.525] | 0.512 (71456) [0.507, 0.516] | 0.530 (27107) [0.525, 0.535] | 0.528 (879) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.505 (20076) | 0.500 (140322) [0.497, 0.504] | 0.501 (600054) [0.499, 0.502] | 0.501 (1000384) [0.499, 0.502] | 0.500 (379498) [0.498, 0.502] | 0.491 (12306) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.590 (39) | 0.631 (236) [0.595, 0.671] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.571 (7) | 0.500 | flat -0.025 (noise 0.044) |
| reversal_k13_next | 0.333 (60) | 0.324 (460) [0.314, 0.335] | 0.307 (2133) [0.295, 0.319] | 0.308 (3437) [0.297, 0.319] | 0.321 (1332) [0.309, 0.331] | 0.233 (30) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.596 (47) | 0.525 (396) [0.495, 0.560] | 0.571 (1555) [0.552, 0.591] | 0.574 (2504) [0.558, 0.591] | 0.564 (1032) [0.540, 0.591] | 0.577 (26) | 0.077 | flat -0.067 (noise 0.036) |
| reversal_k3_next | 0.657 (146) | 0.577 (817) [0.551, 0.607] | 0.575 (2745) [0.561, 0.589] | 0.582 (4349) [0.572, 0.594] | 0.576 (1909) [0.561, 0.593] | 0.600 (70) | 0.293 | flat +0.003 (noise 0.026) |
| reversal_k3_now | 0.984 (64) | 0.932 (399) [0.906, 0.959] | 0.934 (1701) [0.925, 0.943] | 0.937 (2858) [0.931, 0.944] | 0.931 (1095) [0.920, 0.942] | 0.892 (37) | 0.293 | flat +0.003 (noise 0.018) |
| reversal_k5_next | 0.484 (128) | 0.434 (912) [0.415, 0.453] | 0.463 (2571) [0.448, 0.478] | 0.474 (3917) [0.460, 0.488] | 0.453 (1927) [0.436, 0.471] | 0.481 (79) | 0.187 | down -0.055 (noise 0.027) |
| reversal_k5_now | 0.796 (54) | 0.817 (376) [0.792, 0.839] | 0.827 (1577) [0.813, 0.842] | 0.831 (2617) [0.819, 0.842] | 0.820 (1006) [0.804, 0.836] | 0.759 (29) | 0.187 | flat +0.006 (noise 0.029) |
| reversal_k8_next | 0.404 (104) | 0.365 (777) [0.341, 0.388] | 0.387 (2380) [0.373, 0.401] | 0.390 (3874) [0.377, 0.402] | 0.382 (1768) [0.366, 0.398] | 0.324 (68) | 0.121 | flat -0.032 (noise 0.027) |
| reversal_k8_now | 0.729 (48) | 0.667 (333) [0.631, 0.703] | 0.706 (1542) [0.686, 0.726] | 0.704 (2590) [0.688, 0.720] | 0.688 (1003) [0.663, 0.713] | 0.667 (27) | 0.121 | flat -0.007 (noise 0.035) |
| overall | 0.509 (22257) | 0.504 (155487) [0.501, 0.507] | 0.504 (661995) [0.502, 0.505] | 0.503 (1102780) [0.502, 0.504] | 0.504 (419499) [0.502, 0.506] | 0.495 (13609) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06859, 0.1026] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5323, 'levels': [{'threshold': 0.06859, 'calls_per_day': 145.2, 'win_rate': 0.5793}, {'threshold': 0.1026, 'calls_per_day': 35.5, 'win_rate': 0.636}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 26848, 'rate': 0.531}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15174 | 0.337 | 0.523 (14928) | 0.586 (1522) | 0.764 (2490) |
| volatility: normal | 15174 | 0.366 | 0.521 (15111) | 0.623 (811) | 0.755 (2195) |
| volatility: wild | 15174 | 0.379 | 0.510 (15137) | 0.619 (331) | 0.773 (2037) |
| session: Asia 00-08 | 15360 | 0.359 | 0.524 (15264) | 0.609 (978) | 0.763 (2233) |
| session: Europe 08-13 | 9600 | 0.356 | 0.520 (9516) | 0.600 (657) | 0.764 (1516) |
| session: US 13-21 | 14982 | 0.368 | 0.512 (14879) | 0.577 (640) | 0.771 (2152) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5517) | 0.625 (389) | 0.743 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.389 | 0.399 | 0.332 | 0.332 | 0.508 | 0.259 | 0.518 | 1.249 |
| 6h | 360 | 0.375 | 0.374 | 0.284 | 0.318 | 0.517 | 0.254 | 0.496 | 1.234 |
| 24h | 1440 | 0.371 | 0.366 | 0.281 | 0.307 | 0.527 | 0.259 | 0.484 | 1.178 |
| 7d | 10080 | 0.369 | 0.359 | 0.274 | 0.306 | 0.534 | 0.266 | 0.472 | 1.220 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.307 | 0.519 | 0.254 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.389 / 0.508 / 0.900; 2: 0.401 / 0.610 / 0.917; 3: 0.395 / 0.576 / 0.833; 4: 0.366 / 0.458 / 0.933; 5: 0.359 / 0.441 / 0.917; 6: 0.382 / 0.492 / 0.917; 7: 0.382 / 0.508 / 0.867; 8: 0.393 / 0.542 / 0.883; 9: 0.378 / 0.576 / 0.900; 10: 0.364 / 0.508 / 0.917; 11: 0.357 / 0.441 / 0.950; 12: 0.359 / 0.475 / 0.933; 13: 0.352 / 0.458 / 0.950; 14: 0.350 / 0.424 / 0.967; 15: 0.376 / 0.542 / 0.983
- 6h: 1: 0.375 / 0.517 / 0.894; 2: 0.371 / 0.514 / 0.900; 3: 0.364 / 0.508 / 0.861; 4: 0.364 / 0.508 / 0.908; 5: 0.357 / 0.475 / 0.908; 6: 0.360 / 0.475 / 0.908; 7: 0.363 / 0.494 / 0.900; 8: 0.369 / 0.525 / 0.925; 9: 0.360 / 0.506 / 0.914; 10: 0.353 / 0.483 / 0.919; 11: 0.354 / 0.486 / 0.919; 12: 0.357 / 0.517 / 0.914; 13: 0.351 / 0.469 / 0.950; 14: 0.352 / 0.492 / 0.944; 15: 0.361 / 0.500 / 0.953
- 24h: 1: 0.371 / 0.527 / 0.901; 2: 0.363 / 0.497 / 0.906; 3: 0.361 / 0.503 / 0.900; 4: 0.357 / 0.489 / 0.906; 5: 0.356 / 0.492 / 0.912; 6: 0.358 / 0.484 / 0.916; 7: 0.363 / 0.513 / 0.918; 8: 0.362 / 0.517 / 0.921; 9: 0.362 / 0.511 / 0.920; 10: 0.353 / 0.498 / 0.917; 11: 0.350 / 0.476 / 0.922; 12: 0.349 / 0.490 / 0.920; 13: 0.349 / 0.472 / 0.928; 14: 0.355 / 0.495 / 0.928; 15: 0.353 / 0.503 / 0.924
- 7d: 1: 0.369 / 0.534 / 0.896; 2: 0.355 / 0.493 / 0.901; 3: 0.357 / 0.503 / 0.900; 4: 0.353 / 0.495 / 0.901; 5: 0.353 / 0.495 / 0.901; 6: 0.353 / 0.492 / 0.902; 7: 0.352 / 0.498 / 0.901; 8: 0.354 / 0.505 / 0.902; 9: 0.352 / 0.502 / 0.902; 10: 0.354 / 0.506 / 0.901; 11: 0.348 / 0.494 / 0.901; 12: 0.351 / 0.501 / 0.901; 13: 0.349 / 0.493 / 0.902; 14: 0.351 / 0.501 / 0.902; 15: 0.348 / 0.498 / 0.901
- 30d: 1: 0.360 / 0.519 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.901; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.901; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.145 (body 0.093, range 0.198); 'price stays where it was' would score 0.156; colour right 0.559; typical miss of the close 13.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.135 (body 0.098, range 0.173); 'price stays where it was' would score 0.135; colour right 0.520; typical miss of the close 10.0 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.132 (body 0.090, range 0.174); 'price stays where it was' would score 0.139; colour right 0.487; typical miss of the close 9.7 bp; chain ended on the right side 0.438 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.162); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 3.8; 2: 0.198 / 4.5; 3: 0.166 / 6.0; 4: 0.133 / 6.5; 5: 0.121 / 7.2; 6: 0.109 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.088 / 8.3; 10: 0.087 / 9.0; 11: 0.084 / 9.5; 12: 0.079 / 9.9; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 115836, probability skill vs chance 0.216, widened contest next: False
  - now: threshold 0.8359, hit rate recent 0.9349 / long run 0.9322
    - 6h: 19 calls (77 a day), hit rate 0.895, chance 0.300, naive rule 0.537, lift 2.98x
    - 24h: 63 calls (63 a day), hit rate 0.937, chance 0.295, naive rule 0.498, lift 3.17x
    - 7d: 405 calls (58 a day), hit rate 0.931, chance 0.292, naive rule 0.486, lift 3.19x
    - 30d: 1705 calls (57 a day), hit rate 0.933, chance 0.293, naive rule 0.487, lift 3.19x
  - next: threshold 0.555, hit rate recent 0.6282 / long run 0.5844
    - 6h: 20 calls (81 a day), hit rate 0.700, chance 0.300, lift 2.33x
    - 24h: 123 calls (123 a day), hit rate 0.585, chance 0.295, lift 1.98x
    - 7d: 835 calls (119 a day), hit rate 0.581, chance 0.292, lift 1.99x
    - 30d: 2763 calls (92 a day), hit rate 0.575, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.492; 0.35: 541, 0.515; 0.40: 482, 0.569; 0.45: 412, 0.641; 0.50: 359, 0.693; 0.55: 314, 0.734; 0.60: 267, 0.778; 0.65: 224, 0.805; 0.70: 177, 0.838; 0.75: 137, 0.872; 0.80: 93, 0.911; 0.85: 48, 0.948; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.425; 0.35: 499, 0.461; 0.40: 406, 0.494; 0.45: 310, 0.527; 0.50: 201, 0.559; 0.55: 90, 0.568; 0.60: 14, 0.614; 0.65: 1, 0.710
- **K=5**: model 1792540800, labels learned 115834, probability skill vs chance 0.2101, widened contest next: False
  - now: threshold 0.6843, hit rate recent 0.7906 / long run 0.8193
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.190, naive rule 0.448, lift 4.14x
    - 24h: 50 calls (50 a day), hit rate 0.760, chance 0.188, naive rule 0.406, lift 4.04x
    - 7d: 371 calls (53 a day), hit rate 0.822, chance 0.186, naive rule 0.397, lift 4.42x
    - 30d: 1569 calls (52 a day), hit rate 0.826, chance 0.188, naive rule 0.397, lift 4.40x
  - next: threshold 0.4103, hit rate recent 0.4855 / long run 0.451
    - 6h: 33 calls (135 a day), hit rate 0.515, chance 0.190, lift 2.71x
    - 24h: 122 calls (123 a day), hit rate 0.475, chance 0.188, lift 2.53x
    - 7d: 920 calls (132 a day), hit rate 0.438, chance 0.186, lift 2.36x
    - 30d: 2613 calls (87 a day), hit rate 0.462, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.425; 0.35: 346, 0.492; 0.40: 278, 0.563; 0.45: 225, 0.620; 0.50: 177, 0.668; 0.55: 136, 0.710; 0.60: 105, 0.755; 0.65: 78, 0.790; 0.70: 55, 0.823; 0.75: 32, 0.865; 0.80: 10, 0.898
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 250, 0.419; 0.40: 156, 0.446; 0.45: 71, 0.461; 0.50: 16, 0.496; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 115831, probability skill vs chance 0.1956, widened contest next: False
  - now: threshold 0.5654, hit rate recent 0.683 / long run 0.6861
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.124, naive rule 0.369, lift 6.58x
    - 24h: 43 calls (43 a day), hit rate 0.698, chance 0.109, naive rule 0.297, lift 6.42x
    - 7d: 335 calls (48 a day), hit rate 0.663, chance 0.116, naive rule 0.313, lift 5.70x
    - 30d: 1539 calls (51 a day), hit rate 0.703, chance 0.121, naive rule 0.328, lift 5.82x
  - next: threshold 0.3475, hit rate recent 0.3673 / long run 0.3716
    - 6h: 24 calls (99 a day), hit rate 0.542, chance 0.124, lift 4.36x
    - 24h: 100 calls (101 a day), hit rate 0.340, chance 0.109, lift 3.13x
    - 7d: 788 calls (113 a day), hit rate 0.360, chance 0.116, lift 3.10x
    - 30d: 2407 calls (80 a day), hit rate 0.383, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 253, 0.421; 0.35: 192, 0.491; 0.40: 147, 0.545; 0.45: 113, 0.592; 0.50: 87, 0.633; 0.55: 63, 0.678; 0.60: 42, 0.721; 0.65: 23, 0.785; 0.70: 10, 0.841; 0.75: 1, 0.824
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 101, 0.378; 0.40: 39, 0.400; 0.45: 8, 0.428; 0.50: 1, 0.531
- **K=13**: model 1792454400, labels learned 115826, probability skill vs chance 0.1865, widened contest next: False
  - now: threshold 0.4183, hit rate recent 0.5674 / long run 0.5569
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.074, naive rule 0.333, lift 9.37x
    - 24h: 44 calls (44 a day), hit rate 0.591, chance 0.072, naive rule 0.273, lift 8.22x
    - 7d: 390 calls (56 a day), hit rate 0.523, chance 0.074, naive rule 0.264, lift 7.03x
    - 30d: 1555 calls (52 a day), hit rate 0.570, chance 0.077, naive rule 0.271, lift 7.38x
  - next: threshold 0.2946, hit rate recent 0.2941 / long run 0.3128
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.074, lift 6.76x
    - 24h: 47 calls (47 a day), hit rate 0.234, chance 0.072, lift 3.25x
    - 7d: 461 calls (66 a day), hit rate 0.319, chance 0.074, lift 4.28x
    - 30d: 2129 calls (71 a day), hit rate 0.306, chance 0.077, lift 3.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.448; 0.35: 86, 0.500; 0.40: 61, 0.552; 0.45: 41, 0.608; 0.50: 25, 0.658; 0.55: 14, 0.707; 0.60: 6, 0.754; 0.65: 1, 0.837
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.316; 0.35: 13, 0.352; 0.40: 2, 0.466; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.149 | 6.62% | 0.900 | 0.450 | 0.248 | 0.559 | 0.432 |
| 6h | 16.254 | 3.69% | 0.900 | 0.486 | 0.250 | 0.506 | 0.607 |
| 24h | 15.932 | 2.64% | 0.903 | 0.500 | 0.250 | 0.511 | 0.584 |
| 7d | 15.038 | 3.92% | 0.899 | 0.500 | 0.250 | 0.499 | 0.649 |
| 30d | 13.555 | 4.08% | 0.900 | 0.500 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.932 | 25.698 | 25.233 | 25.126 | 25.939 | 25.203 | 24.947 | 25.345 | 25.064 | 25.149 |
| 6h | 16.878 | 16.570 | 16.387 | 16.107 | 16.716 | 16.287 | 16.178 | 16.274 | 16.195 | 16.254 |
| 24h | 16.364 | 16.124 | 16.041 | 15.936 | 16.245 | 16.043 | 15.905 | 15.919 | 15.910 | 15.932 |
| 7d | 15.651 | 15.190 | 15.132 | 15.062 | 15.293 | 15.187 | 15.029 | 15.018 | 15.014 | 15.038 |
| 30d | 14.132 | 13.679 | 13.639 | 13.577 | 13.800 | 13.741 | 13.551 | 13.531 | 13.530 | 13.555 |

## Next candle

- candle starting 2026-10-22 14:42 UTC, last close 2408.34
- P(up) 0.4612, return quantiles (bp): {'05': -15.526, '10': -12.284, '25': -6.61, '40': -2.578, '50': -0.738, '60': 1.199, '75': 5.506, '90': 10.797, '95': 14.033}
- changepoint probability 0.066, regime age 38.3 min
- agent weights: empirical 0.006, ewma 0.029, garch 0.070, har 0.344, bocpd 0.012, hmm 0.098, online_qr 0.271, lgbm 0.170

## Learning log

- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- HMM volatility states (sd, bp per minute): [3.89, 6.21, 16.2], current probabilities: [0.02, 0.92, 0.06]
- live generator: {'versions': 60, 'latest_effective': '2026-10-22 14:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.292, 'l_abs': 0.651, 'l_hi': 0.762, 'l_lo': 0.777, 'b05': 0.702, 'b25': 0.66, 'b75': 0.681, 'b95': 0.662}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.454, 2.012, 1.945, 1.932, 1.919, 2.206, 2.138, 2.412, 2.498, 2.472, 2.802, 2.299, 2.538, 2.581]}
- calibration offsets (in sigma): {'05': -0.0195, '10': -0.059, '25': -0.0375, '40': 0.004, '50': -0.045, '60': -0.064, '75': 0.0275, '90': -0.001, '95': -0.0505}
