# ETH-USD 60s candle generator - report

- generated: 2026-11-02 13:34 UTC
- last closed candle: 2026-11-02 13:34 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.448 (96) | 0.495 (672) [0.473, 0.518] | 0.518 (2878) [0.498, 0.538] | 0.514 (5850) [0.501, 0.527] | 0.518 (2878) [0.498, 0.538] | 0.556 (54) | 0.500 | flat -0.052 (noise 0.027) |
| colour_clear | 0.537 (747) | 0.542 (5503) [0.533, 0.551] | 0.545 (23558) [0.541, 0.549] | 0.520 (47796) [0.514, 0.527] | 0.545 (23558) [0.541, 0.549] | 0.542 (456) | 0.500 | flat -0.009 (noise 0.009) |
| colour_confident | 0.550 (229) | 0.581 (1051) [0.567, 0.595] | 0.598 (4512) [0.586, 0.610] | 0.598 (4512) [0.586, 0.610] | 0.598 (4512) [0.586, 0.610] | 0.569 (58) | 0.500 | flat -0.025 (noise 0.020) |
| colour_next | 0.529 (1408) | 0.530 (9966) [0.523, 0.538] | 0.530 (42807) [0.526, 0.533] | 0.515 (87156) [0.511, 0.519] | 0.530 (42807) [0.526, 0.533] | 0.550 (809) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.505 (19712) | 0.502 (139524) [0.500, 0.504] | 0.501 (599298) [0.499, 0.502] | 0.501 (1220184) [0.500, 0.502] | 0.501 (599298) [0.499, 0.502] | 0.495 (11326) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.607 (56) | 0.610 (272) [0.574, 0.646] | 0.632 (1213) [0.613, 0.652] | 0.632 (1213) [0.613, 0.652] | 0.632 (1213) [0.613, 0.652] | 0.692 (13) | 0.500 | flat -0.018 (noise 0.038) |
| reversal_k13_next | 0.343 (35) | 0.335 (355) [0.288, 0.384] | 0.321 (1934) [0.309, 0.334] | 0.310 (4039) [0.299, 0.322] | 0.321 (1934) [0.309, 0.334] | 0.400 (25) | 0.077 | flat +0.018 (noise 0.033) |
| reversal_k13_now | 0.576 (66) | 0.574 (441) [0.534, 0.613] | 0.568 (1675) [0.548, 0.588] | 0.574 (3147) [0.559, 0.588] | 0.568 (1675) [0.548, 0.588] | 0.458 (24) | 0.077 | flat +0.022 (noise 0.035) |
| reversal_k3_next | 0.614 (132) | 0.591 (881) [0.584, 0.599] | 0.583 (3083) [0.573, 0.594] | 0.585 (5523) [0.576, 0.594] | 0.583 (3083) [0.573, 0.594] | 0.676 (68) | 0.293 | flat -0.002 (noise 0.025) |
| reversal_k3_now | 0.895 (67) | 0.945 (439) [0.923, 0.968] | 0.935 (1745) [0.924, 0.945] | 0.938 (3508) [0.932, 0.945] | 0.935 (1745) [0.924, 0.945] | 0.889 (27) | 0.294 | flat +0.010 (noise 0.020) |
| reversal_k5_next | 0.567 (60) | 0.532 (447) [0.518, 0.549] | 0.473 (2900) [0.458, 0.488] | 0.481 (4890) [0.470, 0.493] | 0.473 (2900) [0.458, 0.488] | 0.600 (30) | 0.187 | up +0.063 (noise 0.029) |
| reversal_k5_now | 0.831 (71) | 0.826 (431) [0.813, 0.837] | 0.821 (1640) [0.811, 0.832] | 0.829 (3251) [0.820, 0.839] | 0.821 (1640) [0.811, 0.832] | 0.758 (33) | 0.187 | flat +0.008 (noise 0.027) |
| reversal_k8_next | 0.500 (50) | 0.415 (645) [0.385, 0.449] | 0.390 (2845) [0.377, 0.404] | 0.392 (4951) [0.381, 0.404] | 0.390 (2845) [0.377, 0.404] | 0.478 (23) | 0.121 | flat +0.037 (noise 0.026) |
| reversal_k8_now | 0.710 (62) | 0.703 (394) [0.649, 0.747] | 0.691 (1594) [0.669, 0.711] | 0.702 (3181) [0.688, 0.717] | 0.691 (1594) [0.669, 0.711] | 0.571 (21) | 0.121 | flat +0.038 (noise 0.040) |
| overall | 0.510 (21759) | 0.507 (154195) [0.504, 0.509] | 0.505 (662399) [0.503, 0.506] | 0.504 (1345680) [0.503, 0.505] | 0.505 (662399) [0.503, 0.506] | 0.502 (12440) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08106, 0.1234] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5313, 'levels': [{'threshold': 0.08106, 'calls_per_day': 143.3, 'win_rate': 0.5809}, {'threshold': 0.1234, 'calls_per_day': 35.3, 'win_rate': 0.608}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42473, 'rate': 0.5308}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15152 | 0.334 | 0.527 (14866) | 0.578 (2238) | 0.759 (2644) |
| volatility: normal | 15151 | 0.365 | 0.532 (15078) | 0.607 (1535) | 0.742 (2278) |
| volatility: wild | 15151 | 0.381 | 0.529 (15104) | 0.634 (797) | 0.767 (2053) |
| session: Asia 00-08 | 15360 | 0.360 | 0.535 (15245) | 0.600 (1604) | 0.760 (2296) |
| session: Europe 08-13 | 9600 | 0.354 | 0.531 (9497) | 0.594 (1164) | 0.751 (1591) |
| session: US 13-21 | 14914 | 0.367 | 0.528 (14789) | 0.595 (1180) | 0.760 (2242) |
| session: late 21-24 | 5580 | 0.350 | 0.515 (5517) | 0.600 (622) | 0.744 (846) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.341 | 0.375 | 0.245 | 0.245 | 0.500 | 0.226 | 0.457 | 0.829 |
| 6h | 360 | 0.352 | 0.351 | 0.259 | 0.290 | 0.538 | 0.259 | 0.446 | 1.111 |
| 24h | 1440 | 0.355 | 0.350 | 0.265 | 0.295 | 0.527 | 0.260 | 0.450 | 1.279 |
| 7d | 10080 | 0.359 | 0.353 | 0.274 | 0.304 | 0.531 | 0.260 | 0.458 | 1.289 |
| 30d | 43200 | 0.361 | 0.352 | 0.274 | 0.303 | 0.531 | 0.261 | 0.460 | 1.272 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.341 / 0.500 / 0.867; 2: 0.347 / 0.467 / 0.833; 3: 0.355 / 0.483 / 0.867; 4: 0.352 / 0.517 / 0.867; 5: 0.338 / 0.483 / 0.900; 6: 0.352 / 0.467 / 0.867; 7: 0.350 / 0.550 / 0.917; 8: 0.335 / 0.500 / 0.900; 9: 0.335 / 0.500 / 0.883; 10: 0.335 / 0.433 / 0.900; 11: 0.345 / 0.450 / 0.933; 12: 0.348 / 0.517 / 0.933; 13: 0.336 / 0.500 / 0.933; 14: 0.361 / 0.617 / 0.933; 15: 0.376 / 0.617 / 0.950
- 6h: 1: 0.352 / 0.538 / 0.894; 2: 0.341 / 0.510 / 0.858; 3: 0.347 / 0.507 / 0.894; 4: 0.336 / 0.513 / 0.914; 5: 0.340 / 0.521 / 0.922; 6: 0.345 / 0.538 / 0.914; 7: 0.346 / 0.513 / 0.931; 8: 0.334 / 0.499 / 0.936; 9: 0.338 / 0.513 / 0.928; 10: 0.328 / 0.443 / 0.939; 11: 0.332 / 0.482 / 0.942; 12: 0.338 / 0.493 / 0.942; 13: 0.327 / 0.443 / 0.939; 14: 0.331 / 0.476 / 0.947; 15: 0.334 / 0.496 / 0.953
- 24h: 1: 0.355 / 0.527 / 0.904; 2: 0.343 / 0.490 / 0.895; 3: 0.347 / 0.506 / 0.902; 4: 0.343 / 0.510 / 0.906; 5: 0.342 / 0.511 / 0.908; 6: 0.344 / 0.514 / 0.900; 7: 0.339 / 0.503 / 0.906; 8: 0.335 / 0.498 / 0.903; 9: 0.337 / 0.493 / 0.906; 10: 0.334 / 0.477 / 0.906; 11: 0.340 / 0.502 / 0.905; 12: 0.337 / 0.493 / 0.908; 13: 0.337 / 0.489 / 0.904; 14: 0.340 / 0.500 / 0.905; 15: 0.339 / 0.504 / 0.912
- 7d: 1: 0.359 / 0.531 / 0.897; 2: 0.346 / 0.490 / 0.900; 3: 0.350 / 0.507 / 0.901; 4: 0.347 / 0.501 / 0.902; 5: 0.348 / 0.516 / 0.902; 6: 0.344 / 0.505 / 0.902; 7: 0.346 / 0.498 / 0.903; 8: 0.344 / 0.507 / 0.902; 9: 0.346 / 0.504 / 0.902; 10: 0.344 / 0.498 / 0.902; 11: 0.342 / 0.498 / 0.902; 12: 0.344 / 0.498 / 0.901; 13: 0.344 / 0.502 / 0.901; 14: 0.343 / 0.499 / 0.901; 15: 0.344 / 0.503 / 0.901
- 30d: 1: 0.361 / 0.531 / 0.898; 2: 0.348 / 0.497 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.347 / 0.504 / 0.900; 6: 0.346 / 0.500 / 0.900; 7: 0.346 / 0.499 / 0.901; 8: 0.346 / 0.502 / 0.901; 9: 0.345 / 0.499 / 0.901; 10: 0.346 / 0.505 / 0.901; 11: 0.343 / 0.497 / 0.901; 12: 0.345 / 0.502 / 0.900; 13: 0.344 / 0.502 / 0.900; 14: 0.343 / 0.499 / 0.900; 15: 0.344 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.090 (body 0.067, range 0.113); 'price stays where it was' would score 0.070; colour right 0.400; typical miss of the close 17.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.124 (body 0.086, range 0.163); 'price stays where it was' would score 0.127; colour right 0.524; typical miss of the close 9.3 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.126 (body 0.087, range 0.165); 'price stays where it was' would score 0.130; colour right 0.478; typical miss of the close 6.8 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.1 bp; chain ended on the right side 0.504 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.7 bp; chain ended on the right side 0.518 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.9; 2: 0.198 / 4.5; 3: 0.168 / 6.1; 4: 0.131 / 6.5; 5: 0.125 / 7.1; 6: 0.112 / 7.6; 7: 0.110 / 8.0; 8: 0.098 / 8.6; 9: 0.090 / 8.5; 10: 0.088 / 9.1; 11: 0.085 / 9.6; 12: 0.076 / 9.9; 13: 0.068 / 10.0; 14: 0.070 / 10.5; 15: 0.063 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 131608, probability skill vs chance 0.2339, widened contest next: False
  - now: threshold 0.8382, hit rate recent 0.9063 / long run 0.9354
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.315, naive rule 0.507, lift 2.91x
    - 24h: 60 calls (60 a day), hit rate 0.900, chance 0.301, naive rule 0.521, lift 2.99x
    - 7d: 434 calls (62 a day), hit rate 0.940, chance 0.294, naive rule 0.502, lift 3.20x
    - 30d: 1737 calls (58 a day), hit rate 0.934, chance 0.295, naive rule 0.496, lift 3.17x
  - next: threshold 0.5306, hit rate recent 0.6561 / long run 0.6037
    - 6h: 37 calls (150 a day), hit rate 0.649, chance 0.315, lift 2.06x
    - 24h: 132 calls (132 a day), hit rate 0.659, chance 0.301, lift 2.19x
    - 7d: 887 calls (127 a day), hit rate 0.599, chance 0.294, lift 2.04x
    - 30d: 3079 calls (103 a day), hit rate 0.587, chance 0.295, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.499; 0.35: 535, 0.524; 0.40: 473, 0.582; 0.45: 404, 0.653; 0.50: 354, 0.703; 0.55: 309, 0.745; 0.60: 261, 0.790; 0.65: 219, 0.815; 0.70: 174, 0.845; 0.75: 137, 0.879; 0.80: 92, 0.913; 0.85: 46, 0.947; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.428; 0.35: 502, 0.464; 0.40: 406, 0.498; 0.45: 309, 0.533; 0.50: 200, 0.571; 0.55: 90, 0.575; 0.60: 13, 0.653; 0.65: 1, 0.640
- **K=5**: model 1792540800, labels learned 131606, probability skill vs chance 0.2284, widened contest next: False
  - now: threshold 0.6838, hit rate recent 0.7935 / long run 0.8191
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.193, naive rule 0.414, lift 4.22x
    - 24h: 70 calls (70 a day), hit rate 0.800, chance 0.192, naive rule 0.439, lift 4.18x
    - 7d: 433 calls (62 a day), hit rate 0.818, chance 0.190, naive rule 0.420, lift 4.31x
    - 30d: 1636 calls (55 a day), hit rate 0.820, chance 0.188, naive rule 0.406, lift 4.36x
  - next: threshold 0.4488, hit rate recent 0.5937 / long run 0.5122
    - 6h: 17 calls (69 a day), hit rate 0.706, chance 0.193, lift 3.66x
    - 24h: 59 calls (59 a day), hit rate 0.644, chance 0.192, lift 3.36x
    - 7d: 417 calls (60 a day), hit rate 0.537, chance 0.190, lift 2.83x
    - 30d: 2826 calls (94 a day), hit rate 0.477, chance 0.188, lift 2.53x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.427; 0.35: 346, 0.493; 0.40: 278, 0.568; 0.45: 227, 0.620; 0.50: 181, 0.668; 0.55: 143, 0.704; 0.60: 109, 0.749; 0.65: 76, 0.788; 0.70: 50, 0.823; 0.75: 29, 0.869; 0.80: 10, 0.891
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.387; 0.35: 256, 0.420; 0.40: 160, 0.460; 0.45: 69, 0.480; 0.50: 13, 0.497; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 131603, probability skill vs chance 0.2053, widened contest next: False
  - now: threshold 0.5709, hit rate recent 0.6704 / long run 0.6923
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.130, naive rule 0.371, lift 4.62x
    - 24h: 52 calls (52 a day), hit rate 0.635, chance 0.129, naive rule 0.383, lift 4.93x
    - 7d: 387 calls (55 a day), hit rate 0.705, chance 0.124, naive rule 0.352, lift 5.67x
    - 30d: 1584 calls (53 a day), hit rate 0.686, chance 0.121, naive rule 0.335, lift 5.66x
  - next: threshold 0.3642, hit rate recent 0.488 / long run 0.4162
    - 6h: 12 calls (49 a day), hit rate 0.417, chance 0.130, lift 3.21x
    - 24h: 50 calls (50 a day), hit rate 0.520, chance 0.129, lift 4.04x
    - 7d: 611 calls (87 a day), hit rate 0.426, chance 0.124, lift 3.42x
    - 30d: 2828 calls (94 a day), hit rate 0.391, chance 0.121, lift 3.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.434; 0.35: 190, 0.501; 0.40: 148, 0.546; 0.45: 113, 0.593; 0.50: 84, 0.637; 0.55: 61, 0.674; 0.60: 41, 0.710; 0.65: 24, 0.786; 0.70: 11, 0.813; 0.75: 2, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.359; 0.35: 92, 0.389; 0.40: 28, 0.418; 0.45: 5, 0.450; 0.50: 1, 0.654
- **K=13**: model 1793577600, labels learned 131598, probability skill vs chance 0.1873, widened contest next: False
  - now: threshold 0.4448, hit rate recent 0.5482 / long run 0.5669
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.081, naive rule 0.326, lift 7.58x
    - 24h: 56 calls (57 a day), hit rate 0.500, chance 0.071, naive rule 0.292, lift 7.02x
    - 7d: 425 calls (61 a day), hit rate 0.576, chance 0.079, naive rule 0.295, lift 7.31x
    - 30d: 1672 calls (56 a day), hit rate 0.563, chance 0.077, naive rule 0.280, lift 7.28x
  - next: threshold 0.2897, hit rate recent 0.3781 / long run 0.3279
    - 6h: 13 calls (54 a day), hit rate 0.308, chance 0.081, lift 3.79x
    - 24h: 43 calls (43 a day), hit rate 0.372, chance 0.071, lift 5.22x
    - 7d: 349 calls (50 a day), hit rate 0.347, chance 0.079, lift 4.39x
    - 30d: 1905 calls (64 a day), hit rate 0.322, chance 0.077, lift 4.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 128, 0.442; 0.35: 92, 0.494; 0.40: 65, 0.547; 0.45: 44, 0.592; 0.50: 29, 0.650; 0.55: 18, 0.682; 0.60: 9, 0.731; 0.65: 3, 0.727; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.328; 0.35: 14, 0.358; 0.40: 3, 0.434; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.234 | 3.28% | 0.883 | 0.400 | 0.249 | 0.550 | 0.430 |
| 6h | 13.340 | 1.50% | 0.889 | 0.469 | 0.249 | 0.526 | 0.292 |
| 24h | 11.709 | 2.93% | 0.901 | 0.486 | 0.250 | 0.509 | 0.508 |
| 7d | 14.853 | 4.83% | 0.900 | 0.499 | 0.250 | 0.505 | 0.749 |
| 30d | 13.986 | 4.32% | 0.900 | 0.500 | 0.251 | 0.498 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 16.785 | 16.644 | 16.637 | 16.237 | 16.596 | 16.405 | 16.283 | 16.202 | 16.283 | 16.234 |
| 6h | 13.543 | 13.450 | 13.518 | 13.318 | 13.642 | 13.600 | 13.326 | 13.298 | 13.317 | 13.340 |
| 24h | 12.062 | 11.794 | 11.811 | 11.753 | 11.998 | 11.947 | 11.705 | 11.684 | 11.690 | 11.709 |
| 7d | 15.607 | 15.023 | 14.970 | 14.886 | 15.179 | 15.134 | 14.839 | 14.819 | 14.826 | 14.853 |
| 30d | 14.618 | 14.134 | 14.079 | 14.015 | 14.250 | 14.199 | 13.979 | 13.958 | 13.960 | 13.986 |

## Next candle

- candle starting 2026-11-02 13:34 UTC, last close 2275.31
- P(up) 0.4997, return quantiles (bp): {'05': -10.977, '10': -8.377, '25': -4.318, '40': -1.309, '50': -0.004, '60': 1.31, '75': 4.173, '90': 7.923, '95': 10.536}
- changepoint probability 0.1688, regime age 109.6 min
- agent weights: empirical 0.010, ewma 0.078, garch 0.058, har 0.174, bocpd 0.010, hmm 0.013, online_qr 0.274, lgbm 0.384

## Learning log

- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- HMM volatility states (sd, bp per minute): [2.67, 6.37, 20.05], current probabilities: [0.0, 0.792, 0.208]
- live generator: {'versions': 60, 'latest_effective': '2026-11-02 13:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.435, 'l_abs': 0.631, 'l_hi': 0.739, 'l_lo': 0.757, 'b05': 0.639, 'b25': 0.661, 'b75': 0.687, 'b95': 0.669}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.538, 1.485, 1.586, 1.673, 2.071, 1.948, 2.087, 2.174, 2.206, 2.365, 2.682, 2.741, 2.851, 2.957]}
- calibration offsets (in sigma): {'05': 0.0365, '10': -0.027, '25': -0.1075, '40': -0.028, '50': -0.045, '60': -0.062, '75': -0.0125, '90': -0.023, '95': -0.0165}
