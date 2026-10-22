# ETH-USD 60s candle generator - report

- generated: 2026-10-22 18:52 UTC
- last closed candle: 2026-10-22 18:52 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_next 0.434 in the last 7 days, -0.055 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.543 (672) [0.507, 0.580] | 0.520 (2876) [0.500, 0.540] | 0.515 (4794) [0.500, 0.529] | 0.520 (1822) [0.492, 0.545] | 0.467 (75) | 0.500 | flat +0.038 (noise 0.027) |
| colour_clear | 0.550 (816) | 0.555 (5596) [0.546, 0.564] | 0.528 (23440) [0.519, 0.537] | 0.516 (39077) [0.509, 0.523] | 0.547 (14839) [0.541, 0.553] | 0.539 (658) | 0.500 | flat +0.014 (noise 0.009) |
| colour_confident | 0.602 (176) | 0.600 (979) [0.581, 0.622] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.579 (95) | 0.500 | flat +0.001 (noise 0.023) |
| colour_next | 0.533 (1434) | 0.534 (10023) [0.525, 0.542] | 0.519 (42861) [0.513, 0.525] | 0.512 (71456) [0.507, 0.516] | 0.530 (27107) [0.525, 0.535] | 0.526 (1128) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.505 (20076) | 0.500 (140322) [0.497, 0.504] | 0.501 (600054) [0.499, 0.502] | 0.501 (1000384) [0.499, 0.502] | 0.500 (379498) [0.498, 0.502] | 0.493 (15792) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.590 (39) | 0.631 (236) [0.595, 0.671] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.700 (10) | 0.500 | flat -0.025 (noise 0.044) |
| reversal_k13_next | 0.333 (60) | 0.324 (460) [0.314, 0.335] | 0.307 (2133) [0.295, 0.319] | 0.308 (3437) [0.297, 0.319] | 0.321 (1332) [0.309, 0.331] | 0.243 (37) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.596 (47) | 0.525 (396) [0.495, 0.560] | 0.571 (1555) [0.552, 0.591] | 0.574 (2504) [0.558, 0.591] | 0.564 (1032) [0.540, 0.591] | 0.562 (32) | 0.077 | flat -0.067 (noise 0.036) |
| reversal_k3_next | 0.657 (146) | 0.577 (817) [0.551, 0.607] | 0.575 (2745) [0.561, 0.589] | 0.582 (4349) [0.572, 0.594] | 0.576 (1909) [0.561, 0.593] | 0.620 (79) | 0.293 | flat +0.003 (noise 0.026) |
| reversal_k3_now | 0.984 (64) | 0.932 (399) [0.906, 0.959] | 0.934 (1701) [0.925, 0.943] | 0.937 (2858) [0.931, 0.944] | 0.931 (1095) [0.920, 0.942] | 0.909 (44) | 0.293 | flat +0.003 (noise 0.018) |
| reversal_k5_next | 0.484 (128) | 0.434 (912) [0.415, 0.453] | 0.463 (2571) [0.448, 0.478] | 0.474 (3917) [0.460, 0.488] | 0.453 (1927) [0.436, 0.471] | 0.505 (99) | 0.187 | down -0.055 (noise 0.027) |
| reversal_k5_now | 0.796 (54) | 0.817 (376) [0.792, 0.839] | 0.827 (1577) [0.813, 0.842] | 0.831 (2617) [0.819, 0.842] | 0.820 (1006) [0.804, 0.836] | 0.794 (34) | 0.187 | flat +0.006 (noise 0.029) |
| reversal_k8_next | 0.404 (104) | 0.365 (777) [0.341, 0.388] | 0.387 (2380) [0.373, 0.401] | 0.390 (3874) [0.377, 0.402] | 0.382 (1768) [0.366, 0.398] | 0.317 (79) | 0.121 | flat -0.032 (noise 0.027) |
| reversal_k8_now | 0.729 (48) | 0.667 (333) [0.631, 0.703] | 0.706 (1542) [0.686, 0.726] | 0.704 (2590) [0.688, 0.720] | 0.688 (1003) [0.663, 0.713] | 0.697 (33) | 0.121 | flat -0.007 (noise 0.035) |
| overall | 0.509 (22257) | 0.504 (155487) [0.501, 0.507] | 0.504 (661995) [0.502, 0.505] | 0.503 (1102780) [0.502, 0.504] | 0.504 (419499) [0.502, 0.506] | 0.497 (17432) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06876, 0.1025] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5346, 'levels': [{'threshold': 0.06876, 'calls_per_day': 145.5, 'win_rate': 0.584}, {'threshold': 0.1025, 'calls_per_day': 35.7, 'win_rate': 0.6414}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 27097, 'rate': 0.5309}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15258 | 0.337 | 0.523 (15011) | 0.586 (1525) | 0.764 (2495) |
| volatility: normal | 15257 | 0.366 | 0.521 (15195) | 0.624 (810) | 0.754 (2217) |
| volatility: wild | 15257 | 0.379 | 0.510 (15219) | 0.614 (347) | 0.774 (2034) |
| session: Asia 00-08 | 15360 | 0.359 | 0.524 (15264) | 0.609 (978) | 0.763 (2233) |
| session: Europe 08-13 | 9600 | 0.356 | 0.520 (9516) | 0.600 (657) | 0.764 (1516) |
| session: US 13-21 | 15232 | 0.369 | 0.513 (15128) | 0.576 (658) | 0.772 (2176) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5517) | 0.625 (389) | 0.743 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.387 | 0.376 | 0.296 | 0.296 | 0.458 | 0.244 | 0.530 | 1.505 |
| 6h | 360 | 0.386 | 0.389 | 0.288 | 0.329 | 0.515 | 0.272 | 0.500 | 1.321 |
| 24h | 1440 | 0.374 | 0.368 | 0.276 | 0.306 | 0.529 | 0.266 | 0.483 | 1.184 |
| 7d | 10080 | 0.369 | 0.360 | 0.274 | 0.306 | 0.534 | 0.266 | 0.472 | 1.219 |
| 30d | 43200 | 0.359 | 0.354 | 0.278 | 0.307 | 0.519 | 0.254 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.387 / 0.458 / 0.950; 2: 0.365 / 0.407 / 0.950; 3: 0.416 / 0.559 / 0.983; 4: 0.380 / 0.458 / 0.933; 5: 0.386 / 0.508 / 0.933; 6: 0.361 / 0.407 / 0.917; 7: 0.388 / 0.525 / 0.933; 8: 0.374 / 0.441 / 0.850; 9: 0.385 / 0.508 / 0.933; 10: 0.384 / 0.492 / 0.950; 11: 0.360 / 0.407 / 0.967; 12: 0.386 / 0.525 / 0.967; 13: 0.361 / 0.441 / 0.950; 14: 0.374 / 0.390 / 0.967; 15: 0.370 / 0.458 / 0.967
- 6h: 1: 0.386 / 0.515 / 0.894; 2: 0.380 / 0.541 / 0.911; 3: 0.380 / 0.527 / 0.900; 4: 0.370 / 0.515 / 0.889; 5: 0.366 / 0.499 / 0.858; 6: 0.368 / 0.513 / 0.836; 7: 0.357 / 0.471 / 0.836; 8: 0.368 / 0.515 / 0.819; 9: 0.360 / 0.487 / 0.850; 10: 0.357 / 0.490 / 0.861; 11: 0.361 / 0.485 / 0.872; 12: 0.367 / 0.518 / 0.869; 13: 0.359 / 0.471 / 0.844; 14: 0.362 / 0.468 / 0.861; 15: 0.366 / 0.499 / 0.850
- 24h: 1: 0.374 / 0.529 / 0.902; 2: 0.366 / 0.509 / 0.906; 3: 0.363 / 0.506 / 0.901; 4: 0.361 / 0.501 / 0.898; 5: 0.354 / 0.487 / 0.892; 6: 0.359 / 0.494 / 0.893; 7: 0.357 / 0.498 / 0.894; 8: 0.360 / 0.511 / 0.890; 9: 0.359 / 0.503 / 0.899; 10: 0.352 / 0.494 / 0.899; 11: 0.350 / 0.475 / 0.903; 12: 0.349 / 0.490 / 0.903; 13: 0.347 / 0.464 / 0.903; 14: 0.354 / 0.487 / 0.906; 15: 0.354 / 0.507 / 0.903
- 7d: 1: 0.369 / 0.534 / 0.895; 2: 0.356 / 0.496 / 0.900; 3: 0.357 / 0.504 / 0.900; 4: 0.353 / 0.498 / 0.900; 5: 0.352 / 0.494 / 0.900; 6: 0.352 / 0.493 / 0.900; 7: 0.352 / 0.496 / 0.900; 8: 0.353 / 0.504 / 0.899; 9: 0.352 / 0.502 / 0.900; 10: 0.353 / 0.505 / 0.900; 11: 0.348 / 0.493 / 0.901; 12: 0.351 / 0.501 / 0.901; 13: 0.349 / 0.493 / 0.901; 14: 0.350 / 0.500 / 0.902; 15: 0.348 / 0.498 / 0.902
- 30d: 1: 0.359 / 0.519 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.502 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.345 / 0.498 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.138 (body 0.085, range 0.191); 'price stays where it was' would score 0.196; colour right 0.407; typical miss of the close 8.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.137 (body 0.094, range 0.180); 'price stays where it was' would score 0.150; colour right 0.485; typical miss of the close 13.4 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.136 (body 0.095, range 0.178); 'price stays where it was' would score 0.141; colour right 0.490; typical miss of the close 9.9 bp; chain ended on the right side 0.438 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.539 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.8; 2: 0.198 / 4.5; 3: 0.166 / 6.0; 4: 0.132 / 6.5; 5: 0.121 / 7.2; 6: 0.109 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.3; 10: 0.087 / 9.1; 11: 0.083 / 9.5; 12: 0.078 / 9.9; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 116086, probability skill vs chance 0.2224, widened contest next: False
  - now: threshold 0.8361, hit rate recent 0.9421 / long run 0.933
    - 6h: 15 calls (61 a day), hit rate 1.000, chance 0.318, naive rule 0.562, lift 3.14x
    - 24h: 60 calls (60 a day), hit rate 0.933, chance 0.304, naive rule 0.512, lift 3.07x
    - 7d: 408 calls (58 a day), hit rate 0.934, chance 0.294, naive rule 0.489, lift 3.18x
    - 30d: 1701 calls (57 a day), hit rate 0.934, chance 0.293, naive rule 0.487, lift 3.19x
  - next: threshold 0.5634, hit rate recent 0.6487 / long run 0.5873
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.318, lift 2.55x
    - 24h: 107 calls (107 a day), hit rate 0.626, chance 0.304, lift 2.06x
    - 7d: 833 calls (119 a day), hit rate 0.585, chance 0.294, lift 1.99x
    - 30d: 2760 calls (92 a day), hit rate 0.576, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 541, 0.516; 0.40: 481, 0.570; 0.45: 412, 0.641; 0.50: 359, 0.694; 0.55: 314, 0.736; 0.60: 267, 0.779; 0.65: 223, 0.806; 0.70: 177, 0.839; 0.75: 137, 0.872; 0.80: 92, 0.913; 0.85: 48, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.425; 0.35: 499, 0.461; 0.40: 406, 0.494; 0.45: 309, 0.528; 0.50: 201, 0.559; 0.55: 90, 0.568; 0.60: 14, 0.613; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 116084, probability skill vs chance 0.2151, widened contest next: False
  - now: threshold 0.6827, hit rate recent 0.8075 / long run 0.8208
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.214, naive rule 0.470, lift 4.16x
    - 24h: 46 calls (46 a day), hit rate 0.783, chance 0.193, naive rule 0.417, lift 4.06x
    - 7d: 369 calls (53 a day), hit rate 0.827, chance 0.187, naive rule 0.401, lift 4.41x
    - 30d: 1564 calls (52 a day), hit rate 0.827, chance 0.188, naive rule 0.397, lift 4.40x
  - next: threshold 0.4146, hit rate recent 0.5186 / long run 0.4559
    - 6h: 32 calls (131 a day), hit rate 0.562, chance 0.214, lift 2.63x
    - 24h: 126 calls (127 a day), hit rate 0.508, chance 0.193, lift 2.64x
    - 7d: 920 calls (132 a day), hit rate 0.446, chance 0.187, lift 2.38x
    - 30d: 2626 calls (88 a day), hit rate 0.463, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 346, 0.493; 0.40: 277, 0.564; 0.45: 224, 0.621; 0.50: 177, 0.669; 0.55: 135, 0.711; 0.60: 105, 0.756; 0.65: 77, 0.791; 0.70: 55, 0.825; 0.75: 31, 0.867; 0.80: 10, 0.898
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 250, 0.420; 0.40: 156, 0.446; 0.45: 70, 0.460; 0.50: 16, 0.494; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 116081, probability skill vs chance 0.1962, widened contest next: False
  - now: threshold 0.565, hit rate recent 0.6976 / long run 0.6875
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.121, naive rule 0.352, lift 6.74x
    - 24h: 40 calls (40 a day), hit rate 0.700, chance 0.108, naive rule 0.306, lift 6.48x
    - 7d: 335 calls (48 a day), hit rate 0.669, chance 0.117, naive rule 0.317, lift 5.72x
    - 30d: 1535 calls (51 a day), hit rate 0.704, chance 0.121, naive rule 0.328, lift 5.82x
  - next: threshold 0.3432, hit rate recent 0.3508 / long run 0.3698
    - 6h: 20 calls (82 a day), hit rate 0.350, chance 0.121, lift 2.88x
    - 24h: 98 calls (99 a day), hit rate 0.327, chance 0.108, lift 3.02x
    - 7d: 783 calls (112 a day), hit rate 0.363, chance 0.117, lift 3.10x
    - 30d: 2406 calls (80 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.422; 0.35: 192, 0.492; 0.40: 147, 0.546; 0.45: 113, 0.593; 0.50: 87, 0.634; 0.55: 63, 0.678; 0.60: 42, 0.722; 0.65: 23, 0.787; 0.70: 10, 0.845; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 101, 0.377; 0.40: 39, 0.399; 0.45: 8, 0.424; 0.50: 1, 0.515
- **K=13**: model 1792454400, labels learned 116076, probability skill vs chance 0.1854, widened contest next: False
  - now: threshold 0.4155, hit rate recent 0.5614 / long run 0.5564
    - 6h: 11 calls (46 a day), hit rate 0.636, chance 0.093, naive rule 0.351, lift 6.86x
    - 24h: 41 calls (41 a day), hit rate 0.561, chance 0.076, naive rule 0.293, lift 7.33x
    - 7d: 389 calls (56 a day), hit rate 0.527, chance 0.075, naive rule 0.268, lift 7.02x
    - 30d: 1554 calls (52 a day), hit rate 0.570, chance 0.077, naive rule 0.272, lift 7.38x
  - next: threshold 0.2946, hit rate recent 0.2921 / long run 0.3124
    - 6h: 12 calls (50 a day), hit rate 0.500, chance 0.093, lift 5.39x
    - 24h: 46 calls (46 a day), hit rate 0.239, chance 0.076, lift 3.13x
    - 7d: 458 calls (66 a day), hit rate 0.321, chance 0.075, lift 4.28x
    - 30d: 2129 calls (71 a day), hit rate 0.305, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.447; 0.35: 86, 0.500; 0.40: 61, 0.553; 0.45: 41, 0.608; 0.50: 25, 0.660; 0.55: 14, 0.708; 0.60: 6, 0.762; 0.65: 2, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.315; 0.35: 13, 0.347; 0.40: 2, 0.458; 0.45: 0, 0.333

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.085 | -1.63% | 0.917 | 0.617 | 0.253 | 0.475 | 0.070 |
| 6h | 21.760 | 4.27% | 0.892 | 0.506 | 0.250 | 0.532 | 0.541 |
| 24h | 16.102 | 2.57% | 0.903 | 0.501 | 0.250 | 0.511 | 0.605 |
| 7d | 15.005 | 3.91% | 0.898 | 0.500 | 0.250 | 0.499 | 0.646 |
| 30d | 13.572 | 4.10% | 0.900 | 0.500 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.860 | 13.955 | 13.874 | 14.079 | 14.041 | 13.929 | 13.962 | 13.822 | 13.929 | 14.085 |
| 6h | 22.731 | 22.073 | 21.922 | 21.704 | 22.278 | 21.891 | 21.717 | 21.812 | 21.716 | 21.760 |
| 24h | 16.527 | 16.271 | 16.198 | 16.083 | 16.427 | 16.212 | 16.075 | 16.095 | 16.076 | 16.102 |
| 7d | 15.616 | 15.154 | 15.099 | 15.027 | 15.264 | 15.149 | 14.994 | 14.979 | 14.979 | 15.005 |
| 30d | 14.153 | 13.696 | 13.655 | 13.594 | 13.818 | 13.758 | 13.569 | 13.549 | 13.547 | 13.572 |

## Next candle

- candle starting 2026-10-22 18:52 UTC, last close 2382.88
- P(up) 0.4827, return quantiles (bp): {'05': -8.707, '10': -6.873, '25': -3.61, '40': -1.364, '50': -0.179, '60': 0.88, '75': 3.079, '90': 6.158, '95': 8.194}
- changepoint probability 0.0573, regime age 65.0 min
- agent weights: empirical 0.005, ewma 0.047, garch 0.092, har 0.260, bocpd 0.014, hmm 0.091, online_qr 0.283, lgbm 0.207

## Learning log

- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- HMM volatility states (sd, bp per minute): [3.89, 6.21, 16.2], current probabilities: [0.404, 0.583, 0.013]
- live generator: {'versions': 60, 'latest_effective': '2026-10-22 19:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.216, 'l_abs': 0.652, 'l_hi': 0.76, 'l_lo': 0.773, 'b05': 0.695, 'b25': 0.624, 'b75': 0.661, 'b95': 0.637}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.264, 1.583, 1.945, 2.456, 2.751, 3.037, 3.668, 3.129, 3.112, 2.901, 3.097, 3.43, 3.292, 3.774]}
- calibration offsets (in sigma): {'05': 0.0055, '10': -0.039, '25': -0.0225, '40': -0.016, '50': -0.015, '60': -0.034, '75': -0.0175, '90': -0.031, '95': -0.0455}
