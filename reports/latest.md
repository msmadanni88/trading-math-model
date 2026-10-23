# ETH-USD 60s candle generator - report

- generated: 2026-10-23 10:16 UTC
- last closed candle: 2026-10-23 10:15 UTC (staleness 1.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: colour_path 0.498 in the last 7 days, -0.005 against the 7 before
- WIN RATE FALLING: overall 0.502 in the last 7 days, -0.004 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.542 (672) [0.504, 0.580] | 0.518 (2876) [0.498, 0.537] | 0.513 (4890) [0.499, 0.527] | 0.517 (1918) [0.492, 0.541] | 0.634 (41) | 0.500 | flat +0.035 (noise 0.029) |
| colour_clear | 0.545 (826) | 0.555 (5631) [0.546, 0.564] | 0.529 (23423) [0.520, 0.538] | 0.516 (39903) [0.510, 0.523] | 0.547 (15665) [0.542, 0.552] | 0.530 (366) | 0.500 | flat +0.015 (noise 0.009) |
| colour_confident | 0.585 (135) | 0.598 (1030) [0.581, 0.620] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.601 (2722) [0.585, 0.618] | 0.626 (91) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.529 (1435) | 0.535 (10022) [0.528, 0.542] | 0.519 (42861) [0.514, 0.525] | 0.512 (72891) [0.508, 0.516] | 0.530 (28542) [0.525, 0.535] | 0.540 (611) | 0.500 | flat +0.011 (noise 0.007) |
| colour_path | 0.496 (20090) | 0.498 (140308) [0.496, 0.501] | 0.500 (600054) [0.499, 0.502] | 0.500 (1020474) [0.499, 0.501] | 0.500 (399588) [0.498, 0.502] | 0.501 (8554) | 0.500 | down -0.005 (noise 0.002) |
| colour_strong | 0.750 (16) | 0.628 (239) [0.595, 0.661] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.648 (684) [0.622, 0.676] | 0.643 (28) | 0.500 | flat -0.054 (noise 0.044) |
| reversal_k13_next | 0.245 (49) | 0.315 (457) [0.296, 0.332] | 0.305 (2131) [0.293, 0.317] | 0.307 (3486) [0.296, 0.318] | 0.318 (1381) [0.306, 0.330] | 0.394 (33) | 0.077 | flat -0.002 (noise 0.031) |
| reversal_k13_now | 0.605 (38) | 0.538 (383) [0.504, 0.576] | 0.572 (1549) [0.553, 0.592] | 0.574 (2542) [0.559, 0.591] | 0.565 (1070) [0.542, 0.590] | 0.615 (26) | 0.077 | flat -0.037 (noise 0.037) |
| reversal_k3_next | 0.604 (96) | 0.581 (826) [0.557, 0.610] | 0.575 (2772) [0.562, 0.589] | 0.583 (4445) [0.572, 0.594] | 0.578 (2005) [0.563, 0.593] | 0.556 (36) | 0.293 | flat +0.003 (noise 0.025) |
| reversal_k3_now | 0.924 (53) | 0.933 (405) [0.909, 0.958] | 0.934 (1694) [0.926, 0.943] | 0.937 (2911) [0.931, 0.944] | 0.930 (1148) [0.920, 0.941] | 1.000 (26) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.485 (132) | 0.441 (938) [0.420, 0.462] | 0.463 (2650) [0.448, 0.477] | 0.474 (4049) [0.461, 0.487] | 0.455 (2059) [0.439, 0.472] | 0.508 (61) | 0.187 | flat -0.046 (noise 0.026) |
| reversal_k5_now | 0.829 (41) | 0.827 (364) [0.809, 0.845] | 0.830 (1557) [0.817, 0.844] | 0.831 (2658) [0.819, 0.842] | 0.820 (1047) [0.805, 0.836] | 0.862 (29) | 0.187 | flat +0.015 (noise 0.029) |
| reversal_k8_next | 0.337 (101) | 0.360 (784) [0.335, 0.382] | 0.383 (2416) [0.369, 0.396] | 0.388 (3975) [0.376, 0.401] | 0.379 (1869) [0.364, 0.396] | 0.413 (63) | 0.121 | flat -0.042 (noise 0.027) |
| reversal_k8_now | 0.737 (38) | 0.677 (328) [0.639, 0.715] | 0.707 (1527) [0.687, 0.727] | 0.704 (2628) [0.689, 0.720] | 0.690 (1041) [0.666, 0.714] | 0.750 (24) | 0.121 | flat -0.003 (noise 0.036) |
| overall | 0.499 (22169) | 0.502 (155487) [0.500, 0.505] | 0.503 (662087) [0.502, 0.505] | 0.503 (1124949) [0.502, 0.504] | 0.504 (441668) [0.502, 0.506] | 0.507 (9504) | - | down -0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06896, 0.1023] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5365, 'levels': [{'threshold': 0.06896, 'calls_per_day': 144.7, 'win_rate': 0.5908}, {'threshold': 0.1023, 'calls_per_day': 36.1, 'win_rate': 0.6457}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 28015, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15085 | 0.337 | 0.523 (14839) | 0.588 (1522) | 0.764 (2478) |
| volatility: normal | 15085 | 0.365 | 0.521 (15019) | 0.618 (901) | 0.757 (2220) |
| volatility: wild | 15085 | 0.379 | 0.514 (15049) | 0.618 (390) | 0.775 (1952) |
| session: Asia 00-08 | 15360 | 0.359 | 0.526 (15260) | 0.614 (1041) | 0.765 (2221) |
| session: Europe 08-13 | 9435 | 0.355 | 0.521 (9351) | 0.596 (685) | 0.769 (1500) |
| session: US 13-21 | 14880 | 0.368 | 0.513 (14778) | 0.578 (666) | 0.771 (2107) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5518) | 0.620 (421) | 0.742 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.347 | 0.361 | 0.248 | 0.248 | 0.467 | 0.261 | 0.433 | 1.195 |
| 6h | 360 | 0.365 | 0.357 | 0.268 | 0.286 | 0.518 | 0.264 | 0.466 | 1.179 |
| 24h | 1440 | 0.378 | 0.367 | 0.275 | 0.303 | 0.537 | 0.273 | 0.483 | 1.208 |
| 7d | 10080 | 0.370 | 0.359 | 0.273 | 0.304 | 0.537 | 0.268 | 0.471 | 1.219 |
| 30d | 43200 | 0.360 | 0.354 | 0.278 | 0.307 | 0.520 | 0.255 | 0.465 | 1.291 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.347 / 0.467 / 0.833; 2: 0.345 / 0.500 / 0.867; 3: 0.335 / 0.417 / 0.883; 4: 0.331 / 0.450 / 0.933; 5: 0.380 / 0.583 / 0.917; 6: 0.361 / 0.500 / 0.917; 7: 0.352 / 0.450 / 0.900; 8: 0.354 / 0.467 / 0.900; 9: 0.346 / 0.433 / 0.883; 10: 0.355 / 0.467 / 0.867; 11: 0.341 / 0.433 / 0.817; 12: 0.363 / 0.500 / 0.800; 13: 0.356 / 0.533 / 0.767; 14: 0.338 / 0.417 / 0.767; 15: 0.380 / 0.500 / 0.783
- 6h: 1: 0.365 / 0.518 / 0.900; 2: 0.369 / 0.524 / 0.900; 3: 0.363 / 0.504 / 0.900; 4: 0.358 / 0.493 / 0.922; 5: 0.372 / 0.543 / 0.936; 6: 0.360 / 0.510 / 0.939; 7: 0.352 / 0.476 / 0.933; 8: 0.359 / 0.499 / 0.942; 9: 0.361 / 0.479 / 0.919; 10: 0.359 / 0.493 / 0.911; 11: 0.358 / 0.487 / 0.894; 12: 0.369 / 0.524 / 0.889; 13: 0.354 / 0.487 / 0.900; 14: 0.357 / 0.490 / 0.900; 15: 0.363 / 0.485 / 0.897
- 24h: 1: 0.378 / 0.537 / 0.898; 2: 0.371 / 0.527 / 0.896; 3: 0.367 / 0.518 / 0.894; 4: 0.359 / 0.494 / 0.903; 5: 0.362 / 0.510 / 0.899; 6: 0.362 / 0.505 / 0.894; 7: 0.354 / 0.477 / 0.894; 8: 0.363 / 0.510 / 0.899; 9: 0.356 / 0.485 / 0.894; 10: 0.359 / 0.503 / 0.893; 11: 0.360 / 0.500 / 0.890; 12: 0.363 / 0.511 / 0.889; 13: 0.353 / 0.480 / 0.892; 14: 0.357 / 0.490 / 0.891; 15: 0.359 / 0.497 / 0.892
- 7d: 1: 0.370 / 0.537 / 0.895; 2: 0.357 / 0.499 / 0.900; 3: 0.357 / 0.504 / 0.900; 4: 0.352 / 0.494 / 0.900; 5: 0.353 / 0.498 / 0.899; 6: 0.353 / 0.495 / 0.900; 7: 0.351 / 0.495 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.351 / 0.498 / 0.899; 10: 0.353 / 0.508 / 0.899; 11: 0.348 / 0.495 / 0.899; 12: 0.351 / 0.504 / 0.899; 13: 0.349 / 0.494 / 0.899; 14: 0.350 / 0.499 / 0.899; 15: 0.349 / 0.499 / 0.899
- 30d: 1: 0.360 / 0.520 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.499 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.169 (body 0.130, range 0.208); 'price stays where it was' would score 0.206; colour right 0.500; typical miss of the close 7.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.148; colour right 0.529; typical miss of the close 8.7 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.125 (body 0.086, range 0.163); 'price stays where it was' would score 0.133; colour right 0.502; typical miss of the close 10.0 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.133; colour right 0.507; typical miss of the close 8.8 bp; chain ended on the right side 0.551 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.8; 2: 0.198 / 4.4; 3: 0.167 / 6.0; 4: 0.131 / 6.5; 5: 0.121 / 7.2; 6: 0.109 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.3; 10: 0.087 / 9.1; 11: 0.083 / 9.5; 12: 0.078 / 9.9; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 117009, probability skill vs chance 0.2177, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9679 / long run 0.9368
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.287, naive rule 0.455, lift 3.49x
    - 24h: 56 calls (56 a day), hit rate 0.982, chance 0.301, naive rule 0.509, lift 3.26x
    - 7d: 398 calls (57 a day), hit rate 0.935, chance 0.294, naive rule 0.489, lift 3.18x
    - 30d: 1685 calls (56 a day), hit rate 0.936, chance 0.293, naive rule 0.488, lift 3.20x
  - next: threshold 0.5682, hit rate recent 0.5932 / long run 0.5839
    - 6h: 20 calls (81 a day), hit rate 0.600, chance 0.287, lift 2.09x
    - 24h: 78 calls (78 a day), hit rate 0.615, chance 0.301, lift 2.04x
    - 7d: 797 calls (114 a day), hit rate 0.575, chance 0.294, lift 1.96x
    - 30d: 2784 calls (93 a day), hit rate 0.576, chance 0.293, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.492; 0.35: 541, 0.516; 0.40: 481, 0.570; 0.45: 411, 0.641; 0.50: 359, 0.694; 0.55: 314, 0.735; 0.60: 266, 0.780; 0.65: 223, 0.805; 0.70: 177, 0.838; 0.75: 136, 0.873; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.425; 0.35: 499, 0.462; 0.40: 406, 0.496; 0.45: 309, 0.529; 0.50: 201, 0.560; 0.55: 91, 0.568; 0.60: 14, 0.615; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 117007, probability skill vs chance 0.2162, widened contest next: False
  - now: threshold 0.6807, hit rate recent 0.8461 / long run 0.8248
    - 6h: 20 calls (82 a day), hit rate 0.900, chance 0.169, naive rule 0.346, lift 5.32x
    - 24h: 52 calls (52 a day), hit rate 0.865, chance 0.188, naive rule 0.414, lift 4.62x
    - 7d: 358 calls (51 a day), hit rate 0.824, chance 0.188, naive rule 0.401, lift 4.39x
    - 30d: 1555 calls (52 a day), hit rate 0.832, chance 0.188, naive rule 0.398, lift 4.43x
  - next: threshold 0.4189, hit rate recent 0.4917 / long run 0.4593
    - 6h: 32 calls (131 a day), hit rate 0.500, chance 0.169, lift 2.96x
    - 24h: 141 calls (142 a day), hit rate 0.511, chance 0.188, lift 2.72x
    - 7d: 952 calls (136 a day), hit rate 0.446, chance 0.188, lift 2.38x
    - 30d: 2689 calls (90 a day), hit rate 0.464, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 345, 0.494; 0.40: 277, 0.565; 0.45: 223, 0.622; 0.50: 176, 0.671; 0.55: 135, 0.713; 0.60: 104, 0.756; 0.65: 77, 0.793; 0.70: 54, 0.830; 0.75: 31, 0.874; 0.80: 10, 0.906
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 250, 0.421; 0.40: 156, 0.448; 0.45: 70, 0.461; 0.50: 16, 0.497; 0.55: 1, 0.513
- **K=8**: model 1792540800, labels learned 117004, probability skill vs chance 0.2019, widened contest next: False
  - now: threshold 0.5624, hit rate recent 0.733 / long run 0.6925
    - 6h: 16 calls (66 a day), hit rate 0.750, chance 0.115, naive rule 0.292, lift 6.54x
    - 24h: 44 calls (44 a day), hit rate 0.795, chance 0.118, naive rule 0.324, lift 6.73x
    - 7d: 322 calls (46 a day), hit rate 0.689, chance 0.116, naive rule 0.313, lift 5.94x
    - 30d: 1524 calls (51 a day), hit rate 0.706, chance 0.121, naive rule 0.328, lift 5.83x
  - next: threshold 0.3356, hit rate recent 0.395 / long run 0.3753
    - 6h: 32 calls (132 a day), hit rate 0.438, chance 0.115, lift 3.82x
    - 24h: 115 calls (116 a day), hit rate 0.417, chance 0.118, lift 3.53x
    - 7d: 797 calls (114 a day), hit rate 0.365, chance 0.116, lift 3.15x
    - 30d: 2461 calls (82 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.423; 0.35: 191, 0.493; 0.40: 146, 0.548; 0.45: 112, 0.595; 0.50: 86, 0.636; 0.55: 62, 0.681; 0.60: 42, 0.726; 0.65: 23, 0.791; 0.70: 10, 0.846; 0.75: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 100, 0.380; 0.40: 38, 0.398; 0.45: 8, 0.422; 0.50: 1, 0.515
- **K=13**: model 1792713600, labels learned 116999, probability skill vs chance 0.1944, widened contest next: False
  - now: threshold 0.4105, hit rate recent 0.6005 / long run 0.5616
    - 6h: 17 calls (71 a day), hit rate 0.647, chance 0.076, naive rule 0.259, lift 8.56x
    - 24h: 49 calls (50 a day), hit rate 0.633, chance 0.081, naive rule 0.298, lift 7.80x
    - 7d: 375 calls (54 a day), hit rate 0.547, chance 0.075, naive rule 0.268, lift 7.27x
    - 30d: 1554 calls (52 a day), hit rate 0.571, chance 0.077, naive rule 0.272, lift 7.39x
  - next: threshold 0.2945, hit rate recent 0.3309 / long run 0.3156
    - 6h: 16 calls (67 a day), hit rate 0.438, chance 0.076, lift 5.79x
    - 24h: 57 calls (58 a day), hit rate 0.386, chance 0.081, lift 4.76x
    - 7d: 470 calls (67 a day), hit rate 0.315, chance 0.075, lift 4.19x
    - 30d: 2145 calls (72 a day), hit rate 0.307, chance 0.077, lift 3.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.448; 0.35: 86, 0.502; 0.40: 61, 0.556; 0.45: 41, 0.610; 0.50: 25, 0.661; 0.55: 14, 0.716; 0.60: 6, 0.767; 0.65: 2, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.318; 0.35: 13, 0.349; 0.40: 2, 0.450; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.117 | -1.82% | 0.833 | 0.483 | 0.251 | 0.483 | 0.294 |
| 6h | 12.278 | 1.42% | 0.900 | 0.478 | 0.251 | 0.479 | 0.260 |
| 24h | 15.082 | 2.62% | 0.901 | 0.493 | 0.250 | 0.503 | 0.628 |
| 7d | 14.991 | 3.62% | 0.899 | 0.499 | 0.251 | 0.497 | 0.648 |
| 30d | 13.546 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.847 | 15.069 | 14.928 | 15.381 | 15.192 | 15.002 | 15.249 | 15.049 | 15.082 | 15.117 |
| 6h | 12.454 | 12.312 | 12.309 | 12.283 | 12.380 | 12.317 | 12.293 | 12.229 | 12.250 | 12.278 |
| 24h | 15.489 | 15.205 | 15.148 | 15.059 | 15.314 | 15.152 | 15.054 | 15.081 | 15.048 | 15.082 |
| 7d | 15.553 | 15.135 | 15.076 | 15.012 | 15.244 | 15.127 | 14.980 | 14.965 | 14.964 | 14.991 |
| 30d | 14.127 | 13.669 | 13.628 | 13.567 | 13.789 | 13.731 | 13.543 | 13.523 | 13.521 | 13.546 |

## Next candle

- candle starting 2026-10-23 10:15 UTC, last close 2399.94
- P(up) 0.4947, return quantiles (bp): {'05': -7.979, '10': -6.111, '25': -3.315, '40': -1.408, '50': -0.045, '60': 0.966, '75': 3.245, '90': 6.354, '95': 7.641}
- changepoint probability 0.0618, regime age 282.6 min
- agent weights: empirical 0.028, ewma 0.097, garch 0.126, har 0.186, bocpd 0.048, hmm 0.118, online_qr 0.189, lgbm 0.208

## Learning log

- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.11, 6.6, 17.07], current probabilities: [0.656, 0.339, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-23 10:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.269, 'l_abs': 0.693, 'l_hi': 0.763, 'l_lo': 0.771, 'b05': 0.705, 'b25': 0.669, 'b75': 0.62, 'b95': 0.65}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.566, 1.847, 1.972, 2.209, 2.425, 2.522, 2.444, 2.871, 3.156, 3.452, 3.836, 3.768, 4.078, 4.315]}
- calibration offsets (in sigma): {'05': 0.007, '10': -0.016, '25': -0.035, '40': -0.054, '50': 0.0, '60': -0.026, '75': 0.035, '90': 0.056, '95': -0.047}
