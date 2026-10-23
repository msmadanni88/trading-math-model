# ETH-USD 60s candle generator - report

- generated: 2026-10-23 00:35 UTC
- last closed candle: 2026-10-23 00:35 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: colour_path 0.498 in the last 7 days, -0.005 against the 7 before
- WIN RATE FALLING: overall 0.502 in the last 7 days, -0.004 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.542 (672) [0.504, 0.580] | 0.518 (2876) [0.498, 0.537] | 0.513 (4890) [0.499, 0.527] | 0.517 (1918) [0.492, 0.541] | 1.000 (2) | 0.500 | flat +0.035 (noise 0.029) |
| colour_clear | 0.545 (826) | 0.555 (5631) [0.546, 0.564] | 0.529 (23423) [0.520, 0.538] | 0.516 (39903) [0.510, 0.523] | 0.547 (15665) [0.542, 0.552] | 0.654 (26) | 0.500 | flat +0.015 (noise 0.009) |
| colour_confident | 0.585 (135) | 0.598 (1030) [0.581, 0.620] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.667 (6) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.529 (1435) | 0.535 (10022) [0.528, 0.542] | 0.519 (42861) [0.514, 0.525] | 0.512 (72891) [0.508, 0.516] | 0.530 (28542) [0.525, 0.535] | 0.657 (35) | 0.500 | flat +0.011 (noise 0.007) |
| colour_path | 0.496 (20090) | 0.498 (140308) [0.496, 0.501] | 0.500 (600054) [0.499, 0.502] | 0.500 (1020474) [0.499, 0.501] | 0.500 (399588) [0.498, 0.502] | 0.488 (490) | 0.500 | down -0.005 (noise 0.002) |
| colour_strong | 0.750 (16) | 0.628 (239) [0.595, 0.661] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 1.000 (1) | 0.500 | flat -0.054 (noise 0.044) |
| reversal_k13_next | 0.245 (49) | 0.315 (457) [0.296, 0.332] | 0.305 (2131) [0.293, 0.317] | 0.307 (3486) [0.296, 0.318] | 0.318 (1381) [0.306, 0.330] | 1.000 (2) | 0.077 | flat -0.002 (noise 0.031) |
| reversal_k13_now | 0.605 (38) | 0.538 (383) [0.504, 0.576] | 0.572 (1549) [0.553, 0.592] | 0.574 (2542) [0.559, 0.591] | 0.565 (1070) [0.542, 0.590] | 0.500 (2) | 0.077 | flat -0.037 (noise 0.037) |
| reversal_k3_next | 0.604 (96) | 0.581 (826) [0.557, 0.610] | 0.575 (2772) [0.562, 0.589] | 0.583 (4445) [0.572, 0.594] | 0.578 (2005) [0.563, 0.593] | 0.000 (2) | 0.293 | flat +0.003 (noise 0.025) |
| reversal_k3_now | 0.924 (53) | 0.933 (405) [0.909, 0.958] | 0.934 (1694) [0.926, 0.943] | 0.937 (2911) [0.931, 0.944] | 0.930 (1148) [0.920, 0.941] | 1.000 (2) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.485 (132) | 0.441 (938) [0.420, 0.462] | 0.463 (2650) [0.448, 0.477] | 0.474 (4049) [0.461, 0.487] | 0.455 (2059) [0.439, 0.472] | 0.667 (3) | 0.187 | flat -0.046 (noise 0.026) |
| reversal_k5_now | 0.829 (41) | 0.827 (364) [0.809, 0.845] | 0.830 (1557) [0.817, 0.844] | 0.831 (2658) [0.819, 0.842] | 0.820 (1047) [0.805, 0.836] | 0.333 (3) | 0.187 | flat +0.015 (noise 0.029) |
| reversal_k8_next | 0.337 (101) | 0.360 (784) [0.335, 0.382] | 0.383 (2416) [0.369, 0.396] | 0.388 (3975) [0.376, 0.401] | 0.379 (1869) [0.364, 0.396] | 1.000 (2) | 0.121 | flat -0.042 (noise 0.027) |
| reversal_k8_now | 0.737 (38) | 0.677 (328) [0.639, 0.715] | 0.707 (1527) [0.687, 0.727] | 0.704 (2628) [0.689, 0.720] | 0.690 (1041) [0.666, 0.714] | 0.500 (2) | 0.121 | flat -0.003 (noise 0.036) |
| overall | 0.499 (22169) | 0.502 (155487) [0.500, 0.505] | 0.503 (662087) [0.502, 0.505] | 0.503 (1124949) [0.502, 0.504] | 0.504 (441668) [0.502, 0.506] | 0.505 (545) | - | down -0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0689, 0.1023] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5345, 'levels': [{'threshold': 0.0689, 'calls_per_day': 145.2, 'win_rate': 0.5832}, {'threshold': 0.1023, 'calls_per_day': 35.5, 'win_rate': 0.64}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 27439, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14892 | 0.337 | 0.523 (14646) | 0.588 (1507) | 0.763 (2452) |
| volatility: normal | 14891 | 0.365 | 0.521 (14828) | 0.618 (846) | 0.756 (2168) |
| volatility: wild | 14892 | 0.379 | 0.514 (14857) | 0.616 (375) | 0.775 (1934) |
| session: Asia 00-08 | 14915 | 0.359 | 0.526 (14819) | 0.610 (984) | 0.764 (2163) |
| session: Europe 08-13 | 9300 | 0.355 | 0.520 (9216) | 0.600 (657) | 0.767 (1462) |
| session: US 13-21 | 14880 | 0.368 | 0.513 (14778) | 0.578 (666) | 0.771 (2107) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5518) | 0.620 (421) | 0.742 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.387 | 0.355 | 0.244 | 0.244 | 0.583 | 0.305 | 0.468 | 1.093 |
| 6h | 360 | 0.381 | 0.361 | 0.273 | 0.307 | 0.549 | 0.281 | 0.481 | 1.321 |
| 24h | 1440 | 0.376 | 0.368 | 0.276 | 0.308 | 0.532 | 0.270 | 0.483 | 1.207 |
| 7d | 10080 | 0.370 | 0.360 | 0.274 | 0.306 | 0.536 | 0.267 | 0.472 | 1.219 |
| 30d | 43200 | 0.359 | 0.354 | 0.278 | 0.307 | 0.520 | 0.254 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.387 / 0.583 / 0.850; 2: 0.374 / 0.550 / 0.900; 3: 0.335 / 0.450 / 0.933; 4: 0.356 / 0.583 / 0.883; 5: 0.352 / 0.500 / 0.867; 6: 0.352 / 0.467 / 0.933; 7: 0.318 / 0.367 / 0.933; 8: 0.338 / 0.450 / 0.967; 9: 0.322 / 0.467 / 1.000; 10: 0.354 / 0.567 / 0.983; 11: 0.367 / 0.567 / 1.000; 12: 0.320 / 0.400 / 0.983; 13: 0.354 / 0.517 / 0.967; 14: 0.334 / 0.467 / 0.983; 15: 0.331 / 0.483 / 0.983
- 6h: 1: 0.381 / 0.549 / 0.889; 2: 0.372 / 0.518 / 0.881; 3: 0.367 / 0.515 / 0.889; 4: 0.361 / 0.507 / 0.892; 5: 0.367 / 0.532 / 0.908; 6: 0.360 / 0.501 / 0.911; 7: 0.347 / 0.435 / 0.917; 8: 0.364 / 0.490 / 0.922; 9: 0.350 / 0.482 / 0.906; 10: 0.368 / 0.524 / 0.889; 11: 0.370 / 0.535 / 0.850; 12: 0.362 / 0.510 / 0.850; 13: 0.347 / 0.468 / 0.856; 14: 0.358 / 0.507 / 0.844; 15: 0.354 / 0.493 / 0.867
- 24h: 1: 0.376 / 0.532 / 0.896; 2: 0.370 / 0.522 / 0.897; 3: 0.363 / 0.505 / 0.897; 4: 0.361 / 0.502 / 0.900; 5: 0.356 / 0.497 / 0.901; 6: 0.359 / 0.498 / 0.905; 7: 0.354 / 0.479 / 0.905; 8: 0.363 / 0.517 / 0.908; 9: 0.356 / 0.499 / 0.908; 10: 0.354 / 0.494 / 0.904; 11: 0.355 / 0.494 / 0.898; 12: 0.353 / 0.497 / 0.892; 13: 0.348 / 0.467 / 0.892; 14: 0.353 / 0.484 / 0.890; 15: 0.354 / 0.496 / 0.889
- 7d: 1: 0.370 / 0.536 / 0.895; 2: 0.356 / 0.496 / 0.900; 3: 0.357 / 0.503 / 0.900; 4: 0.353 / 0.497 / 0.900; 5: 0.353 / 0.497 / 0.900; 6: 0.352 / 0.493 / 0.900; 7: 0.351 / 0.494 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.352 / 0.499 / 0.900; 10: 0.354 / 0.506 / 0.900; 11: 0.348 / 0.493 / 0.900; 12: 0.351 / 0.501 / 0.900; 13: 0.350 / 0.493 / 0.900; 14: 0.350 / 0.498 / 0.899; 15: 0.348 / 0.498 / 0.900
- 30d: 1: 0.359 / 0.520 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.502 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.499 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.090 (body 0.061, range 0.119); 'price stays where it was' would score 0.049; colour right 0.417; typical miss of the close 8.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.085, range 0.150); 'price stays where it was' would score 0.128; colour right 0.479; typical miss of the close 8.5 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.137 (body 0.097, range 0.178); 'price stays where it was' would score 0.144; colour right 0.490; typical miss of the close 9.5 bp; chain ended on the right side 0.469 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.169); 'price stays where it was' would score 0.132; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.542 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 3.8; 2: 0.199 / 4.5; 3: 0.166 / 6.0; 4: 0.132 / 6.5; 5: 0.121 / 7.2; 6: 0.109 / 7.7; 7: 0.103 / 8.1; 8: 0.095 / 8.4; 9: 0.087 / 8.3; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.078 / 9.9; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 116429, probability skill vs chance 0.2206, widened contest next: False
  - now: threshold 0.8361, hit rate recent 0.9519 / long run 0.9342
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.307, naive rule 0.509, lift 3.26x
    - 24h: 55 calls (55 a day), hit rate 0.927, chance 0.305, naive rule 0.524, lift 3.04x
    - 7d: 402 calls (57 a day), hit rate 0.933, chance 0.295, naive rule 0.491, lift 3.17x
    - 30d: 1693 calls (56 a day), hit rate 0.935, chance 0.293, naive rule 0.488, lift 3.19x
  - next: threshold 0.5637, hit rate recent 0.5979 / long run 0.5837
    - 6h: 20 calls (81 a day), hit rate 0.500, chance 0.307, lift 1.63x
    - 24h: 95 calls (95 a day), hit rate 0.600, chance 0.305, lift 1.97x
    - 7d: 823 calls (118 a day), hit rate 0.580, chance 0.295, lift 1.97x
    - 30d: 2774 calls (92 a day), hit rate 0.575, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.516; 0.40: 481, 0.570; 0.45: 411, 0.642; 0.50: 359, 0.694; 0.55: 314, 0.736; 0.60: 266, 0.780; 0.65: 223, 0.806; 0.70: 177, 0.839; 0.75: 137, 0.873; 0.80: 92, 0.913; 0.85: 47, 0.949; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.425; 0.35: 499, 0.462; 0.40: 406, 0.495; 0.45: 309, 0.528; 0.50: 201, 0.560; 0.55: 90, 0.567; 0.60: 14, 0.611; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 116427, probability skill vs chance 0.2163, widened contest next: False
  - now: threshold 0.6818, hit rate recent 0.8048 / long run 0.8205
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.190, naive rule 0.422, lift 4.31x
    - 24h: 44 calls (44 a day), hit rate 0.795, chance 0.190, naive rule 0.422, lift 4.19x
    - 7d: 362 calls (52 a day), hit rate 0.820, chance 0.187, naive rule 0.401, lift 4.39x
    - 30d: 1557 calls (52 a day), hit rate 0.830, chance 0.188, naive rule 0.398, lift 4.41x
  - next: threshold 0.4173, hit rate recent 0.4895 / long run 0.4553
    - 6h: 37 calls (151 a day), hit rate 0.432, chance 0.190, lift 2.28x
    - 24h: 132 calls (133 a day), hit rate 0.492, chance 0.190, lift 2.59x
    - 7d: 940 calls (134 a day), hit rate 0.443, chance 0.187, lift 2.37x
    - 30d: 2649 calls (88 a day), hit rate 0.463, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 345, 0.494; 0.40: 277, 0.565; 0.45: 224, 0.622; 0.50: 177, 0.670; 0.55: 135, 0.712; 0.60: 104, 0.757; 0.65: 77, 0.792; 0.70: 55, 0.827; 0.75: 31, 0.871; 0.80: 10, 0.899
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 250, 0.421; 0.40: 156, 0.447; 0.45: 70, 0.460; 0.50: 16, 0.494; 0.55: 1, 0.500
- **K=8**: model 1792540800, labels learned 116424, probability skill vs chance 0.1969, widened contest next: False
  - now: threshold 0.5642, hit rate recent 0.7148 / long run 0.6895
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.131, naive rule 0.326, lift 6.66x
    - 24h: 40 calls (40 a day), hit rate 0.725, chance 0.115, naive rule 0.318, lift 6.28x
    - 7d: 327 calls (47 a day), hit rate 0.679, chance 0.117, naive rule 0.315, lift 5.81x
    - 30d: 1529 calls (51 a day), hit rate 0.706, chance 0.121, naive rule 0.328, lift 5.83x
  - next: threshold 0.332, hit rate recent 0.3891 / long run 0.3733
    - 6h: 24 calls (99 a day), hit rate 0.458, chance 0.131, lift 3.49x
    - 24h: 100 calls (101 a day), hit rate 0.350, chance 0.115, lift 3.03x
    - 7d: 783 calls (112 a day), hit rate 0.360, chance 0.117, lift 3.08x
    - 30d: 2417 calls (81 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.423; 0.35: 191, 0.494; 0.40: 146, 0.547; 0.45: 113, 0.595; 0.50: 86, 0.636; 0.55: 63, 0.680; 0.60: 42, 0.724; 0.65: 24, 0.786; 0.70: 10, 0.845; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.351; 0.35: 100, 0.378; 0.40: 38, 0.399; 0.45: 8, 0.421; 0.50: 1, 0.515
- **K=13**: model 1792713600, labels learned 116419, probability skill vs chance 0.1855, widened contest next: False
  - now: threshold 0.4128, hit rate recent 0.5843 / long run 0.5589
    - 6h: 8 calls (33 a day), hit rate 0.750, chance 0.083, naive rule 0.288, lift 9.08x
    - 24h: 40 calls (40 a day), hit rate 0.600, chance 0.077, naive rule 0.292, lift 7.77x
    - 7d: 382 calls (55 a day), hit rate 0.539, chance 0.076, naive rule 0.270, lift 7.12x
    - 30d: 1551 calls (52 a day), hit rate 0.572, chance 0.077, naive rule 0.272, lift 7.39x
  - next: threshold 0.2942, hit rate recent 0.3094 / long run 0.3135
    - 6h: 14 calls (58 a day), hit rate 0.357, chance 0.083, lift 4.32x
    - 24h: 50 calls (51 a day), hit rate 0.280, chance 0.077, lift 3.63x
    - 7d: 459 calls (66 a day), hit rate 0.318, chance 0.076, lift 4.20x
    - 30d: 2133 calls (71 a day), hit rate 0.305, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.448; 0.35: 86, 0.502; 0.40: 61, 0.556; 0.45: 41, 0.610; 0.50: 25, 0.662; 0.55: 14, 0.711; 0.60: 6, 0.762; 0.65: 2, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.316; 0.35: 13, 0.347; 0.40: 2, 0.458; 0.45: 0, 0.333

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.384 | 3.62% | 0.833 | 0.417 | 0.251 | 0.500 | 0.549 |
| 6h | 12.448 | 1.93% | 0.889 | 0.489 | 0.251 | 0.499 | 0.368 |
| 24h | 15.855 | 2.53% | 0.897 | 0.497 | 0.250 | 0.510 | 0.597 |
| 7d | 14.986 | 3.75% | 0.898 | 0.499 | 0.250 | 0.499 | 0.648 |
| 30d | 13.560 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.887 | 13.663 | 13.469 | 13.349 | 13.659 | 13.414 | 13.217 | 13.350 | 13.336 | 13.384 |
| 6h | 12.693 | 12.469 | 12.471 | 12.438 | 12.527 | 12.476 | 12.392 | 12.397 | 12.401 | 12.448 |
| 24h | 16.268 | 16.005 | 15.945 | 15.830 | 16.141 | 15.934 | 15.819 | 15.848 | 15.826 | 15.855 |
| 7d | 15.570 | 15.134 | 15.077 | 15.009 | 15.243 | 15.128 | 14.973 | 14.958 | 14.959 | 14.986 |
| 30d | 14.140 | 13.683 | 13.642 | 13.581 | 13.803 | 13.745 | 13.556 | 13.536 | 13.534 | 13.560 |

## Next candle

- candle starting 2026-10-23 00:35 UTC, last close 2387.41
- P(up) 0.4711, return quantiles (bp): {'05': -9.374, '10': -7.049, '25': -3.777, '40': -1.524, '50': -0.391, '60': 0.985, '75': 3.437, '90': 7.009, '95': 9.251}
- changepoint probability 0.041, regime age 30.0 min
- agent weights: empirical 0.009, ewma 0.071, garch 0.105, har 0.208, bocpd 0.031, hmm 0.109, online_qr 0.261, lgbm 0.206

## Learning log

- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.11, 6.6, 17.07], current probabilities: [0.083, 0.896, 0.022]
- live generator: {'versions': 60, 'latest_effective': '2026-10-23 00:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.247, 'l_abs': 0.648, 'l_hi': 0.758, 'l_lo': 0.778, 'b05': 0.682, 'b25': 0.612, 'b75': 0.651, 'b95': 0.637}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.475, 1.739, 2.012, 2.254, 2.425, 2.625, 2.812, 2.929, 3.351, 4.133, 4.413, 4.602, 4.882, 4.768]}
- calibration offsets (in sigma): {'05': -0.003, '10': 0.004, '25': -0.025, '40': -0.014, '50': -0.03, '60': -0.006, '75': 0.025, '90': 0.016, '95': -0.017}
