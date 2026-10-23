# ETH-USD 60s candle generator - report

- generated: 2026-10-23 05:20 UTC
- last closed candle: 2026-10-23 05:20 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: colour_path 0.498 in the last 7 days, -0.005 against the 7 before
- WIN RATE FALLING: overall 0.502 in the last 7 days, -0.004 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.542 (672) [0.504, 0.580] | 0.518 (2876) [0.498, 0.537] | 0.513 (4890) [0.499, 0.527] | 0.517 (1918) [0.492, 0.541] | 0.619 (21) | 0.500 | flat +0.035 (noise 0.029) |
| colour_clear | 0.545 (826) | 0.555 (5631) [0.546, 0.564] | 0.529 (23423) [0.520, 0.538] | 0.516 (39903) [0.510, 0.523] | 0.547 (15665) [0.542, 0.552] | 0.549 (175) | 0.500 | flat +0.015 (noise 0.009) |
| colour_confident | 0.585 (135) | 0.598 (1030) [0.581, 0.620] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.718 (39) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.529 (1435) | 0.535 (10022) [0.528, 0.542] | 0.519 (42861) [0.514, 0.525] | 0.512 (72891) [0.508, 0.516] | 0.530 (28542) [0.525, 0.535] | 0.568 (317) | 0.500 | flat +0.011 (noise 0.007) |
| colour_path | 0.496 (20090) | 0.498 (140308) [0.496, 0.501] | 0.500 (600054) [0.499, 0.502] | 0.500 (1020474) [0.499, 0.501] | 0.500 (399588) [0.498, 0.502] | 0.508 (4438) | 0.500 | down -0.005 (noise 0.002) |
| colour_strong | 0.750 (16) | 0.628 (239) [0.595, 0.661] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.900 (10) | 0.500 | flat -0.054 (noise 0.044) |
| reversal_k13_next | 0.245 (49) | 0.315 (457) [0.296, 0.332] | 0.305 (2131) [0.293, 0.317] | 0.307 (3486) [0.296, 0.318] | 0.318 (1381) [0.306, 0.330] | 0.333 (18) | 0.077 | flat -0.002 (noise 0.031) |
| reversal_k13_now | 0.605 (38) | 0.538 (383) [0.504, 0.576] | 0.572 (1549) [0.553, 0.592] | 0.574 (2542) [0.559, 0.591] | 0.565 (1070) [0.542, 0.590] | 0.556 (9) | 0.077 | flat -0.037 (noise 0.037) |
| reversal_k3_next | 0.604 (96) | 0.581 (826) [0.557, 0.610] | 0.575 (2772) [0.562, 0.589] | 0.583 (4445) [0.572, 0.594] | 0.578 (2005) [0.563, 0.593] | 0.444 (18) | 0.293 | flat +0.003 (noise 0.025) |
| reversal_k3_now | 0.924 (53) | 0.933 (405) [0.909, 0.958] | 0.934 (1694) [0.926, 0.943] | 0.937 (2911) [0.931, 0.944] | 0.930 (1148) [0.920, 0.941] | 1.000 (11) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.485 (132) | 0.441 (938) [0.420, 0.462] | 0.463 (2650) [0.448, 0.477] | 0.474 (4049) [0.461, 0.487] | 0.455 (2059) [0.439, 0.472] | 0.500 (36) | 0.187 | flat -0.046 (noise 0.026) |
| reversal_k5_now | 0.829 (41) | 0.827 (364) [0.809, 0.845] | 0.830 (1557) [0.817, 0.844] | 0.831 (2658) [0.819, 0.842] | 0.820 (1047) [0.805, 0.836] | 0.833 (12) | 0.187 | flat +0.015 (noise 0.029) |
| reversal_k8_next | 0.337 (101) | 0.360 (784) [0.335, 0.382] | 0.383 (2416) [0.369, 0.396] | 0.388 (3975) [0.376, 0.401] | 0.379 (1869) [0.364, 0.396] | 0.389 (36) | 0.121 | flat -0.042 (noise 0.027) |
| reversal_k8_now | 0.737 (38) | 0.677 (328) [0.639, 0.715] | 0.707 (1527) [0.687, 0.727] | 0.704 (2628) [0.689, 0.720] | 0.690 (1041) [0.666, 0.714] | 0.778 (9) | 0.121 | flat -0.003 (noise 0.036) |
| overall | 0.499 (22169) | 0.502 (155487) [0.500, 0.505] | 0.503 (662087) [0.502, 0.505] | 0.503 (1124949) [0.502, 0.504] | 0.504 (441668) [0.502, 0.506] | 0.513 (4925) | - | down -0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0689, 0.1023] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5345, 'levels': [{'threshold': 0.0689, 'calls_per_day': 145.2, 'win_rate': 0.5832}, {'threshold': 0.1023, 'calls_per_day': 35.5, 'win_rate': 0.64}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 27721, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14987 | 0.337 | 0.524 (14741) | 0.589 (1512) | 0.763 (2460) |
| volatility: normal | 14986 | 0.365 | 0.521 (14921) | 0.620 (862) | 0.757 (2181) |
| volatility: wild | 14987 | 0.379 | 0.514 (14951) | 0.618 (387) | 0.775 (1945) |
| session: Asia 00-08 | 15200 | 0.359 | 0.526 (15101) | 0.614 (1017) | 0.765 (2195) |
| session: Europe 08-13 | 9300 | 0.355 | 0.520 (9216) | 0.600 (657) | 0.767 (1462) |
| session: US 13-21 | 14880 | 0.368 | 0.513 (14778) | 0.578 (666) | 0.771 (2107) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5518) | 0.620 (421) | 0.742 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.332 | 0.339 | 0.268 | 0.268 | 0.550 | 0.219 | 0.445 | 1.254 |
| 6h | 360 | 0.370 | 0.350 | 0.261 | 0.284 | 0.560 | 0.266 | 0.474 | 1.418 |
| 24h | 1440 | 0.374 | 0.366 | 0.272 | 0.305 | 0.535 | 0.262 | 0.485 | 1.256 |
| 7d | 10080 | 0.369 | 0.359 | 0.273 | 0.305 | 0.537 | 0.267 | 0.472 | 1.224 |
| 30d | 43200 | 0.360 | 0.354 | 0.278 | 0.307 | 0.520 | 0.254 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.332 / 0.550 / 0.867; 2: 0.374 / 0.617 / 0.883; 3: 0.355 / 0.567 / 0.883; 4: 0.357 / 0.600 / 0.900; 5: 0.359 / 0.550 / 0.867; 6: 0.332 / 0.467 / 0.850; 7: 0.306 / 0.417 / 0.783; 8: 0.322 / 0.483 / 0.833; 9: 0.362 / 0.550 / 0.750; 10: 0.320 / 0.467 / 0.800; 11: 0.354 / 0.567 / 0.933; 12: 0.353 / 0.517 / 0.950; 13: 0.330 / 0.533 / 0.933; 14: 0.352 / 0.583 / 0.967; 15: 0.331 / 0.533 / 0.933
- 6h: 1: 0.370 / 0.560 / 0.897; 2: 0.366 / 0.555 / 0.892; 3: 0.354 / 0.521 / 0.900; 4: 0.340 / 0.476 / 0.881; 5: 0.343 / 0.493 / 0.861; 6: 0.351 / 0.487 / 0.864; 7: 0.346 / 0.504 / 0.861; 8: 0.350 / 0.501 / 0.883; 9: 0.352 / 0.527 / 0.881; 10: 0.348 / 0.521 / 0.900; 11: 0.356 / 0.538 / 0.958; 12: 0.351 / 0.493 / 0.958; 13: 0.346 / 0.513 / 0.950; 14: 0.344 / 0.496 / 0.956; 15: 0.339 / 0.504 / 0.942
- 24h: 1: 0.374 / 0.535 / 0.895; 2: 0.372 / 0.540 / 0.892; 3: 0.362 / 0.514 / 0.893; 4: 0.358 / 0.499 / 0.889; 5: 0.355 / 0.504 / 0.887; 6: 0.360 / 0.500 / 0.887; 7: 0.353 / 0.485 / 0.888; 8: 0.362 / 0.518 / 0.894; 9: 0.355 / 0.500 / 0.892; 10: 0.353 / 0.498 / 0.894; 11: 0.358 / 0.503 / 0.903; 12: 0.354 / 0.495 / 0.900; 13: 0.349 / 0.479 / 0.897; 14: 0.354 / 0.493 / 0.898; 15: 0.353 / 0.499 / 0.898
- 7d: 1: 0.369 / 0.537 / 0.895; 2: 0.356 / 0.498 / 0.899; 3: 0.357 / 0.505 / 0.900; 4: 0.352 / 0.495 / 0.899; 5: 0.352 / 0.496 / 0.899; 6: 0.353 / 0.495 / 0.899; 7: 0.351 / 0.495 / 0.899; 8: 0.354 / 0.506 / 0.899; 9: 0.351 / 0.499 / 0.899; 10: 0.353 / 0.508 / 0.900; 11: 0.348 / 0.494 / 0.901; 12: 0.351 / 0.501 / 0.902; 13: 0.349 / 0.493 / 0.902; 14: 0.350 / 0.499 / 0.901; 15: 0.348 / 0.500 / 0.901
- 30d: 1: 0.360 / 0.520 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.502 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.100 (body 0.064, range 0.136); 'price stays where it was' would score 0.130; colour right 0.600; typical miss of the close 9.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.106 (body 0.065, range 0.146); 'price stays where it was' would score 0.105; colour right 0.496; typical miss of the close 10.2 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.130 (body 0.090, range 0.170); 'price stays where it was' would score 0.135; colour right 0.498; typical miss of the close 10.1 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.132; colour right 0.506; typical miss of the close 8.8 bp; chain ended on the right side 0.548 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.8; 2: 0.198 / 4.4; 3: 0.167 / 6.0; 4: 0.132 / 6.5; 5: 0.121 / 7.2; 6: 0.110 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.3; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.078 / 9.9; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 116714, probability skill vs chance 0.2181, widened contest next: False
  - now: threshold 0.8361, hit rate recent 0.9586 / long run 0.9352
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.245, naive rule 0.413, lift 4.08x
    - 24h: 56 calls (56 a day), hit rate 0.964, chance 0.302, naive rule 0.518, lift 3.20x
    - 7d: 394 calls (56 a day), hit rate 0.934, chance 0.294, naive rule 0.490, lift 3.18x
    - 30d: 1687 calls (56 a day), hit rate 0.935, chance 0.293, naive rule 0.488, lift 3.19x
  - next: threshold 0.5637, hit rate recent 0.5716 / long run 0.5814
    - 6h: 21 calls (85 a day), hit rate 0.429, chance 0.245, lift 1.75x
    - 24h: 81 calls (81 a day), hit rate 0.617, chance 0.302, lift 2.05x
    - 7d: 811 calls (116 a day), hit rate 0.577, chance 0.294, lift 1.96x
    - 30d: 2782 calls (93 a day), hit rate 0.575, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.492; 0.35: 541, 0.515; 0.40: 481, 0.570; 0.45: 411, 0.641; 0.50: 359, 0.694; 0.55: 314, 0.736; 0.60: 266, 0.780; 0.65: 223, 0.806; 0.70: 177, 0.838; 0.75: 136, 0.873; 0.80: 92, 0.913; 0.85: 47, 0.950; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.425; 0.35: 499, 0.462; 0.40: 406, 0.495; 0.45: 309, 0.528; 0.50: 201, 0.560; 0.55: 91, 0.568; 0.60: 14, 0.613; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 116712, probability skill vs chance 0.2174, widened contest next: False
  - now: threshold 0.6818, hit rate recent 0.8322 / long run 0.8231
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.156, naive rule 0.331, lift 5.43x
    - 24h: 46 calls (46 a day), hit rate 0.848, chance 0.192, naive rule 0.422, lift 4.41x
    - 7d: 358 calls (51 a day), hit rate 0.824, chance 0.187, naive rule 0.401, lift 4.41x
    - 30d: 1553 calls (52 a day), hit rate 0.831, chance 0.188, naive rule 0.398, lift 4.42x
  - next: threshold 0.4173, hit rate recent 0.4811 / long run 0.4568
    - 6h: 40 calls (163 a day), hit rate 0.475, chance 0.156, lift 3.05x
    - 24h: 139 calls (140 a day), hit rate 0.496, chance 0.192, lift 2.58x
    - 7d: 953 calls (136 a day), hit rate 0.444, chance 0.187, lift 2.38x
    - 30d: 2674 calls (89 a day), hit rate 0.463, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 345, 0.494; 0.40: 277, 0.565; 0.45: 224, 0.623; 0.50: 177, 0.671; 0.55: 135, 0.713; 0.60: 104, 0.757; 0.65: 76, 0.793; 0.70: 55, 0.828; 0.75: 31, 0.871; 0.80: 10, 0.898
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 250, 0.421; 0.40: 156, 0.448; 0.45: 70, 0.461; 0.50: 16, 0.495; 0.55: 1, 0.513
- **K=8**: model 1792540800, labels learned 116709, probability skill vs chance 0.1982, widened contest next: False
  - now: threshold 0.5642, hit rate recent 0.7306 / long run 0.6914
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.101, naive rule 0.258, lift 7.89x
    - 24h: 40 calls (40 a day), hit rate 0.775, chance 0.116, naive rule 0.321, lift 6.70x
    - 7d: 321 calls (46 a day), hit rate 0.682, chance 0.116, naive rule 0.314, lift 5.88x
    - 30d: 1524 calls (51 a day), hit rate 0.705, chance 0.121, naive rule 0.328, lift 5.83x
  - next: threshold 0.332, hit rate recent 0.3747 / long run 0.3722
    - 6h: 40 calls (165 a day), hit rate 0.375, chance 0.101, lift 3.70x
    - 24h: 110 calls (111 a day), hit rate 0.373, chance 0.116, lift 3.22x
    - 7d: 794 calls (114 a day), hit rate 0.363, chance 0.116, lift 3.13x
    - 30d: 2441 calls (81 a day), hit rate 0.383, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.423; 0.35: 191, 0.493; 0.40: 146, 0.548; 0.45: 113, 0.595; 0.50: 86, 0.636; 0.55: 62, 0.680; 0.60: 42, 0.723; 0.65: 23, 0.785; 0.70: 10, 0.844; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 100, 0.379; 0.40: 38, 0.399; 0.45: 8, 0.422; 0.50: 1, 0.515
- **K=13**: model 1792713600, labels learned 116704, probability skill vs chance 0.1884, widened contest next: False
  - now: threshold 0.4128, hit rate recent 0.5834 / long run 0.5591
    - 6h: 10 calls (42 a day), hit rate 0.600, chance 0.071, naive rule 0.252, lift 8.45x
    - 24h: 41 calls (41 a day), hit rate 0.610, chance 0.075, naive rule 0.291, lift 8.08x
    - 7d: 374 calls (54 a day), hit rate 0.535, chance 0.075, naive rule 0.269, lift 7.12x
    - 30d: 1551 calls (52 a day), hit rate 0.571, chance 0.077, naive rule 0.272, lift 7.38x
  - next: threshold 0.2942, hit rate recent 0.2948 / long run 0.3118
    - 6h: 21 calls (88 a day), hit rate 0.333, chance 0.071, lift 4.69x
    - 24h: 52 calls (53 a day), hit rate 0.288, chance 0.075, lift 3.82x
    - 7d: 464 calls (66 a day), hit rate 0.312, chance 0.075, lift 4.16x
    - 30d: 2137 calls (71 a day), hit rate 0.306, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.448; 0.35: 86, 0.503; 0.40: 61, 0.556; 0.45: 41, 0.609; 0.50: 25, 0.662; 0.55: 14, 0.714; 0.60: 6, 0.765; 0.65: 2, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.316; 0.35: 13, 0.349; 0.40: 2, 0.467; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.932 | 0.54% | 0.883 | 0.483 | 0.251 | 0.483 | 0.047 |
| 6h | 14.306 | 1.51% | 0.900 | 0.500 | 0.251 | 0.499 | 0.475 |
| 24h | 15.790 | 2.38% | 0.899 | 0.503 | 0.250 | 0.508 | 0.587 |
| 7d | 14.991 | 3.68% | 0.899 | 0.500 | 0.251 | 0.498 | 0.647 |
| 30d | 13.557 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.002 | 12.954 | 12.935 | 12.856 | 13.000 | 12.973 | 13.007 | 12.868 | 12.902 | 12.932 |
| 6h | 14.525 | 14.421 | 14.346 | 14.239 | 14.499 | 14.364 | 14.285 | 14.327 | 14.271 | 14.306 |
| 24h | 16.176 | 15.932 | 15.868 | 15.745 | 16.065 | 15.872 | 15.753 | 15.798 | 15.758 | 15.790 |
| 7d | 15.564 | 15.137 | 15.080 | 15.012 | 15.246 | 15.130 | 14.979 | 14.965 | 14.964 | 14.991 |
| 30d | 14.137 | 13.680 | 13.639 | 13.578 | 13.800 | 13.742 | 13.554 | 13.534 | 13.532 | 13.557 |

## Next candle

- candle starting 2026-10-23 05:20 UTC, last close 2399.24
- P(up) 0.5115, return quantiles (bp): {'05': -7.079, '10': -5.387, '25': -2.698, '40': -0.58, '50': 0.071, '60': 0.829, '75': 2.623, '90': 5.596, '95': 7.015}
- changepoint probability 0.0476, regime age 112.2 min
- agent weights: empirical 0.018, ewma 0.077, garch 0.118, har 0.252, bocpd 0.035, hmm 0.107, online_qr 0.213, lgbm 0.179

## Learning log

- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.11, 6.6, 17.07], current probabilities: [0.757, 0.239, 0.004]
- live generator: {'versions': 60, 'latest_effective': '2026-10-23 05:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.299, 'l_abs': 0.687, 'l_hi': 0.756, 'l_lo': 0.776, 'b05': 0.699, 'b25': 0.649, 'b75': 0.65, 'b95': 0.641}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.582, 1.865, 2.291, 2.953, 3.373, 3.651, 3.539, 3.914, 3.816, 3.155, 3.302, 3.584, 3.727, 4.023]}
- calibration offsets (in sigma): {'05': -0.0005, '10': -0.011, '25': -0.0025, '40': 0.066, '50': 0.015, '60': -0.016, '75': -0.0075, '90': 0.011, '95': -0.0495}
