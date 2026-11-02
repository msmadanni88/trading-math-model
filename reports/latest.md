# ETH-USD 60s candle generator - report

- generated: 2026-11-02 05:12 UTC
- last closed candle: 2026-11-02 05:12 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.448 (96) | 0.495 (672) [0.473, 0.518] | 0.518 (2878) [0.498, 0.538] | 0.514 (5850) [0.501, 0.527] | 0.518 (2878) [0.498, 0.538] | 0.700 (20) | 0.500 | flat -0.052 (noise 0.027) |
| colour_clear | 0.537 (747) | 0.542 (5503) [0.533, 0.551] | 0.545 (23558) [0.541, 0.549] | 0.520 (47796) [0.514, 0.527] | 0.545 (23558) [0.541, 0.549] | 0.564 (163) | 0.500 | flat -0.009 (noise 0.009) |
| colour_confident | 0.550 (229) | 0.581 (1051) [0.567, 0.595] | 0.598 (4512) [0.586, 0.610] | 0.598 (4512) [0.586, 0.610] | 0.598 (4512) [0.586, 0.610] | 0.643 (14) | 0.500 | flat -0.025 (noise 0.020) |
| colour_next | 0.529 (1408) | 0.530 (9966) [0.523, 0.538] | 0.530 (42807) [0.526, 0.533] | 0.515 (87156) [0.511, 0.519] | 0.530 (42807) [0.526, 0.533] | 0.570 (309) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.505 (19712) | 0.502 (139524) [0.500, 0.504] | 0.501 (599298) [0.499, 0.502] | 0.501 (1220184) [0.500, 0.502] | 0.501 (599298) [0.499, 0.502] | 0.499 (4326) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.607 (56) | 0.610 (272) [0.574, 0.646] | 0.632 (1213) [0.613, 0.652] | 0.632 (1213) [0.613, 0.652] | 0.632 (1213) [0.613, 0.652] | 1.000 (3) | 0.500 | flat -0.018 (noise 0.038) |
| reversal_k13_next | 0.343 (35) | 0.335 (355) [0.288, 0.384] | 0.321 (1934) [0.309, 0.334] | 0.310 (4039) [0.299, 0.322] | 0.321 (1934) [0.309, 0.334] | 0.600 (10) | 0.077 | flat +0.018 (noise 0.033) |
| reversal_k13_now | 0.576 (66) | 0.574 (441) [0.534, 0.613] | 0.568 (1675) [0.548, 0.588] | 0.574 (3147) [0.559, 0.588] | 0.568 (1675) [0.548, 0.588] | 0.500 (6) | 0.077 | flat +0.022 (noise 0.035) |
| reversal_k3_next | 0.614 (132) | 0.591 (881) [0.584, 0.599] | 0.583 (3083) [0.573, 0.594] | 0.585 (5523) [0.576, 0.594] | 0.583 (3083) [0.573, 0.594] | 0.632 (19) | 0.293 | flat -0.002 (noise 0.025) |
| reversal_k3_now | 0.895 (67) | 0.945 (439) [0.923, 0.968] | 0.935 (1745) [0.924, 0.945] | 0.938 (3508) [0.932, 0.945] | 0.935 (1745) [0.924, 0.945] | 0.778 (9) | 0.294 | flat +0.010 (noise 0.020) |
| reversal_k5_next | 0.567 (60) | 0.532 (447) [0.518, 0.549] | 0.473 (2900) [0.458, 0.488] | 0.481 (4890) [0.470, 0.493] | 0.473 (2900) [0.458, 0.488] | 0.364 (11) | 0.187 | up +0.063 (noise 0.029) |
| reversal_k5_now | 0.831 (71) | 0.826 (431) [0.813, 0.837] | 0.821 (1640) [0.811, 0.832] | 0.829 (3251) [0.820, 0.839] | 0.821 (1640) [0.811, 0.832] | 0.778 (9) | 0.187 | flat +0.008 (noise 0.027) |
| reversal_k8_next | 0.500 (50) | 0.415 (645) [0.385, 0.449] | 0.390 (2845) [0.377, 0.404] | 0.392 (4951) [0.381, 0.404] | 0.390 (2845) [0.377, 0.404] | 0.444 (9) | 0.121 | flat +0.037 (noise 0.026) |
| reversal_k8_now | 0.710 (62) | 0.703 (394) [0.649, 0.747] | 0.691 (1594) [0.669, 0.711] | 0.702 (3181) [0.688, 0.717] | 0.691 (1594) [0.669, 0.711] | 0.714 (7) | 0.121 | flat +0.038 (noise 0.040) |
| overall | 0.510 (21759) | 0.507 (154195) [0.504, 0.509] | 0.505 (662399) [0.503, 0.506] | 0.504 (1345680) [0.503, 0.505] | 0.505 (662399) [0.503, 0.506] | 0.506 (4735) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08138, 0.1243] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5298, 'levels': [{'threshold': 0.08138, 'calls_per_day': 142.8, 'win_rate': 0.5846}, {'threshold': 0.1243, 'calls_per_day': 35.3, 'win_rate': 0.6}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 41973, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14984 | 0.334 | 0.528 (14699) | 0.579 (2222) | 0.757 (2619) |
| volatility: normal | 14984 | 0.366 | 0.532 (14911) | 0.607 (1518) | 0.746 (2253) |
| volatility: wild | 14984 | 0.380 | 0.528 (14938) | 0.632 (786) | 0.769 (2029) |
| session: Asia 00-08 | 15192 | 0.360 | 0.535 (15078) | 0.600 (1594) | 0.763 (2266) |
| session: Europe 08-13 | 9300 | 0.354 | 0.530 (9198) | 0.595 (1131) | 0.750 (1548) |
| session: US 13-21 | 14880 | 0.367 | 0.528 (14755) | 0.595 (1179) | 0.759 (2241) |
| session: late 21-24 | 5580 | 0.350 | 0.515 (5517) | 0.600 (622) | 0.744 (846) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.343 | 0.328 | 0.283 | 0.283 | 0.500 | 0.252 | 0.433 | 2.227 |
| 6h | 360 | 0.388 | 0.374 | 0.301 | 0.329 | 0.549 | 0.289 | 0.488 | 1.345 |
| 24h | 1440 | 0.339 | 0.334 | 0.255 | 0.283 | 0.527 | 0.252 | 0.427 | 1.185 |
| 7d | 10080 | 0.360 | 0.354 | 0.277 | 0.306 | 0.532 | 0.261 | 0.460 | 1.316 |
| 30d | 43200 | 0.360 | 0.352 | 0.274 | 0.303 | 0.531 | 0.261 | 0.459 | 1.279 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.343 / 0.500 / 0.950; 2: 0.366 / 0.603 / 0.967; 3: 0.321 / 0.500 / 0.950; 4: 0.329 / 0.483 / 0.917; 5: 0.345 / 0.569 / 0.917; 6: 0.325 / 0.500 / 0.917; 7: 0.326 / 0.517 / 0.883; 8: 0.323 / 0.431 / 0.917; 9: 0.351 / 0.569 / 0.850; 10: 0.346 / 0.586 / 0.867; 11: 0.333 / 0.517 / 0.883; 12: 0.317 / 0.517 / 0.833; 13: 0.307 / 0.414 / 0.917; 14: 0.324 / 0.414 / 0.917; 15: 0.352 / 0.586 / 0.867
- 6h: 1: 0.388 / 0.549 / 0.928; 2: 0.364 / 0.468 / 0.942; 3: 0.363 / 0.490 / 0.944; 4: 0.365 / 0.507 / 0.922; 5: 0.355 / 0.504 / 0.917; 6: 0.359 / 0.515 / 0.925; 7: 0.361 / 0.521 / 0.928; 8: 0.356 / 0.499 / 0.947; 9: 0.360 / 0.501 / 0.919; 10: 0.358 / 0.504 / 0.928; 11: 0.351 / 0.476 / 0.928; 12: 0.357 / 0.513 / 0.903; 13: 0.360 / 0.515 / 0.931; 14: 0.361 / 0.518 / 0.914; 15: 0.355 / 0.504 / 0.894
- 24h: 1: 0.339 / 0.527 / 0.897; 2: 0.324 / 0.478 / 0.909; 3: 0.330 / 0.507 / 0.907; 4: 0.326 / 0.491 / 0.903; 5: 0.327 / 0.520 / 0.899; 6: 0.324 / 0.507 / 0.896; 7: 0.321 / 0.494 / 0.894; 8: 0.323 / 0.500 / 0.892; 9: 0.323 / 0.502 / 0.893; 10: 0.320 / 0.490 / 0.890; 11: 0.327 / 0.513 / 0.888; 12: 0.321 / 0.505 / 0.883; 13: 0.326 / 0.517 / 0.885; 14: 0.321 / 0.493 / 0.883; 15: 0.323 / 0.514 / 0.878
- 7d: 1: 0.360 / 0.532 / 0.896; 2: 0.347 / 0.489 / 0.900; 3: 0.350 / 0.508 / 0.900; 4: 0.348 / 0.500 / 0.899; 5: 0.349 / 0.515 / 0.899; 6: 0.344 / 0.502 / 0.899; 7: 0.346 / 0.497 / 0.898; 8: 0.345 / 0.505 / 0.898; 9: 0.347 / 0.505 / 0.898; 10: 0.345 / 0.501 / 0.898; 11: 0.343 / 0.499 / 0.898; 12: 0.344 / 0.500 / 0.897; 13: 0.344 / 0.502 / 0.897; 14: 0.344 / 0.500 / 0.897; 15: 0.345 / 0.504 / 0.897
- 30d: 1: 0.360 / 0.531 / 0.897; 2: 0.348 / 0.497 / 0.900; 3: 0.350 / 0.509 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.347 / 0.504 / 0.900; 6: 0.345 / 0.499 / 0.900; 7: 0.345 / 0.499 / 0.900; 8: 0.345 / 0.502 / 0.900; 9: 0.344 / 0.498 / 0.900; 10: 0.346 / 0.505 / 0.900; 11: 0.343 / 0.497 / 0.900; 12: 0.344 / 0.503 / 0.900; 13: 0.344 / 0.502 / 0.900; 14: 0.343 / 0.499 / 0.899; 15: 0.344 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.090 (body 0.055, range 0.124); 'price stays where it was' would score 0.168; colour right 0.466; typical miss of the close 11.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.141 (body 0.096, range 0.185); 'price stays where it was' would score 0.140; colour right 0.473; typical miss of the close 9.4 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.118 (body 0.083, range 0.153); 'price stays where it was' would score 0.118; colour right 0.465; typical miss of the close 5.7 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.131; colour right 0.499; typical miss of the close 8.0 bp; chain ended on the right side 0.503 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.6 bp; chain ended on the right side 0.519 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.9; 2: 0.199 / 4.5; 3: 0.168 / 6.0; 4: 0.132 / 6.4; 5: 0.125 / 7.0; 6: 0.112 / 7.5; 7: 0.110 / 7.9; 8: 0.098 / 8.4; 9: 0.090 / 8.4; 10: 0.088 / 9.0; 11: 0.085 / 9.4; 12: 0.076 / 9.8; 13: 0.068 / 9.8; 14: 0.071 / 10.3; 15: 0.063 / 10.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 131106, probability skill vs chance 0.2392, widened contest next: True
  - now: threshold 0.838, hit rate recent 0.8935 / long run 0.9352
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.280, naive rule 0.500, lift 2.85x
    - 24h: 66 calls (66 a day), hit rate 0.864, chance 0.292, naive rule 0.515, lift 2.95x
    - 7d: 440 calls (63 a day), hit rate 0.941, chance 0.294, naive rule 0.501, lift 3.20x
    - 30d: 1741 calls (58 a day), hit rate 0.933, chance 0.295, naive rule 0.496, lift 3.17x
  - next: threshold 0.5307, hit rate recent 0.6181 / long run 0.5961
    - 6h: 22 calls (89 a day), hit rate 0.591, chance 0.280, lift 2.11x
    - 24h: 121 calls (121 a day), hit rate 0.612, chance 0.292, lift 2.09x
    - 7d: 879 calls (126 a day), hit rate 0.592, chance 0.294, lift 2.01x
    - 30d: 3080 calls (103 a day), hit rate 0.584, chance 0.295, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 534, 0.524; 0.40: 473, 0.582; 0.45: 404, 0.654; 0.50: 354, 0.703; 0.55: 308, 0.745; 0.60: 260, 0.789; 0.65: 219, 0.815; 0.70: 173, 0.845; 0.75: 137, 0.879; 0.80: 92, 0.913; 0.85: 47, 0.946; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.428; 0.35: 502, 0.464; 0.40: 407, 0.498; 0.45: 310, 0.532; 0.50: 201, 0.569; 0.55: 90, 0.573; 0.60: 13, 0.646; 0.65: 1, 0.640
- **K=5**: model 1792540800, labels learned 131104, probability skill vs chance 0.2341, widened contest next: False
  - now: threshold 0.6721, hit rate recent 0.81 / long run 0.8218
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.194, naive rule 0.458, lift 4.22x
    - 24h: 67 calls (67 a day), hit rate 0.806, chance 0.187, naive rule 0.440, lift 4.32x
    - 7d: 430 calls (61 a day), hit rate 0.821, chance 0.190, naive rule 0.421, lift 4.31x
    - 30d: 1636 calls (55 a day), hit rate 0.821, chance 0.188, naive rule 0.406, lift 4.37x
  - next: threshold 0.4489, hit rate recent 0.5452 / long run 0.505
    - 6h: 13 calls (53 a day), hit rate 0.385, chance 0.194, lift 1.98x
    - 24h: 61 calls (61 a day), hit rate 0.541, chance 0.187, lift 2.90x
    - 7d: 433 calls (62 a day), hit rate 0.536, chance 0.190, lift 2.82x
    - 30d: 2864 calls (95 a day), hit rate 0.473, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.493; 0.40: 278, 0.568; 0.45: 227, 0.621; 0.50: 181, 0.668; 0.55: 142, 0.705; 0.60: 109, 0.750; 0.65: 76, 0.789; 0.70: 50, 0.824; 0.75: 30, 0.869; 0.80: 10, 0.891
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.388; 0.35: 256, 0.420; 0.40: 161, 0.458; 0.45: 69, 0.478; 0.50: 13, 0.497; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 131101, probability skill vs chance 0.214, widened contest next: False
  - now: threshold 0.5694, hit rate recent 0.7129 / long run 0.6968
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.136, naive rule 0.405, lift 5.73x
    - 24h: 56 calls (56 a day), hit rate 0.679, chance 0.124, naive rule 0.364, lift 5.45x
    - 7d: 391 calls (56 a day), hit rate 0.703, chance 0.124, naive rule 0.350, lift 5.68x
    - 30d: 1588 calls (53 a day), hit rate 0.690, chance 0.121, naive rule 0.335, lift 5.69x
  - next: threshold 0.3642, hit rate recent 0.4874 / long run 0.4143
    - 6h: 12 calls (49 a day), hit rate 0.417, chance 0.136, lift 3.07x
    - 24h: 51 calls (51 a day), hit rate 0.490, chance 0.124, lift 3.94x
    - 7d: 636 calls (91 a day), hit rate 0.417, chance 0.124, lift 3.36x
    - 30d: 2841 calls (95 a day), hit rate 0.390, chance 0.121, lift 3.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.434; 0.35: 189, 0.501; 0.40: 148, 0.547; 0.45: 113, 0.593; 0.50: 84, 0.638; 0.55: 61, 0.676; 0.60: 41, 0.712; 0.65: 24, 0.787; 0.70: 11, 0.811; 0.75: 2, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.358; 0.35: 92, 0.388; 0.40: 28, 0.417; 0.45: 5, 0.441; 0.50: 1, 0.630
- **K=13**: model 1793577600, labels learned 131096, probability skill vs chance 0.1994, widened contest next: False
  - now: threshold 0.4414, hit rate recent 0.5768 / long run 0.5706
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.081, naive rule 0.369, lift 7.70x
    - 24h: 57 calls (58 a day), hit rate 0.544, chance 0.073, naive rule 0.287, lift 7.49x
    - 7d: 432 calls (62 a day), hit rate 0.572, chance 0.079, naive rule 0.295, lift 7.24x
    - 30d: 1669 calls (56 a day), hit rate 0.567, chance 0.078, naive rule 0.280, lift 7.31x
  - next: threshold 0.2903, hit rate recent 0.4072 / long run 0.3294
    - 6h: 11 calls (46 a day), hit rate 0.636, chance 0.081, lift 7.84x
    - 24h: 37 calls (37 a day), hit rate 0.405, chance 0.073, lift 5.58x
    - 7d: 354 calls (51 a day), hit rate 0.345, chance 0.079, lift 4.36x
    - 30d: 1924 calls (64 a day), hit rate 0.323, chance 0.078, lift 4.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 128, 0.444; 0.35: 92, 0.496; 0.40: 65, 0.551; 0.45: 44, 0.596; 0.50: 29, 0.654; 0.55: 18, 0.686; 0.60: 9, 0.734; 0.65: 3, 0.727; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.329; 0.35: 14, 0.353; 0.40: 3, 0.434; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.677 | -2.22% | 0.900 | 0.583 | 0.255 | 0.483 | 0.279 |
| 6h | 15.237 | 5.19% | 0.922 | 0.542 | 0.250 | 0.518 | 0.395 |
| 24h | 9.903 | 3.21% | 0.901 | 0.502 | 0.250 | 0.505 | 0.545 |
| 7d | 14.978 | 4.81% | 0.901 | 0.501 | 0.250 | 0.505 | 0.747 |
| 30d | 13.900 | 4.41% | 0.900 | 0.500 | 0.251 | 0.498 | 0.698 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.402 | 12.639 | 12.414 | 12.746 | 12.894 | 12.851 | 12.791 | 12.639 | 12.626 | 12.677 |
| 6h | 16.071 | 15.345 | 15.292 | 15.329 | 15.828 | 15.613 | 15.256 | 15.206 | 15.211 | 15.237 |
| 24h | 10.231 | 10.004 | 9.973 | 9.937 | 10.193 | 10.134 | 9.900 | 9.881 | 9.886 | 9.903 |
| 7d | 15.736 | 15.152 | 15.091 | 15.012 | 15.305 | 15.250 | 14.963 | 14.945 | 14.951 | 14.978 |
| 30d | 14.542 | 14.048 | 13.994 | 13.930 | 14.163 | 14.116 | 13.894 | 13.872 | 13.875 | 13.900 |

## Next candle

- candle starting 2026-11-02 05:12 UTC, last close 2288.7
- P(up) 0.5156, return quantiles (bp): {'05': -9.321, '10': -7.252, '25': -3.222, '40': -0.959, '50': 0.172, '60': 1.229, '75': 3.55, '90': 6.907, '95': 9.959}
- changepoint probability 0.0505, regime age 24.9 min
- agent weights: empirical 0.003, ewma 0.078, garch 0.122, har 0.141, bocpd 0.005, hmm 0.014, online_qr 0.255, lgbm 0.383

## Learning log

- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.63, 6.47, 19.79], current probabilities: [0.01, 0.946, 0.044]
- live generator: {'versions': 60, 'latest_effective': '2026-11-02 05:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.331, 'l_abs': 0.643, 'l_hi': 0.729, 'l_lo': 0.744, 'b05': 0.629, 'b25': 0.639, 'b75': 0.716, 'b95': 0.657}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.215, 1.648, 2.107, 2.456, 2.806, 3.099, 3.386, 3.458, 3.878, 4.242, 4.809, 4.819, 5.32, 5.743]}
- calibration offsets (in sigma): {'05': 0.0455, '10': 0.021, '25': 0.0275, '40': 0.024, '50': 0.015, '60': -0.014, '75': -0.0275, '90': -0.091, '95': -0.0155}
