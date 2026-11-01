# ETH-USD 60s candle generator - report

- generated: 2026-11-01 09:45 UTC
- last closed candle: 2026-11-01 09:45 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.524 (672) [0.491, 0.562] | 0.521 (2877) [0.502, 0.540] | 0.516 (5754) [0.503, 0.528] | 0.520 (2782) [0.502, 0.540] | 0.487 (39) | 0.500 | flat -0.019 (noise 0.030) |
| colour_clear | 0.569 (723) | 0.541 (5558) [0.533, 0.551] | 0.544 (23531) [0.539, 0.549] | 0.520 (47049) [0.514, 0.526] | 0.546 (22811) [0.541, 0.550] | 0.557 (318) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.582 (184) | 0.587 (1090) [0.579, 0.596] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.602 (118) | 0.500 | flat -0.021 (noise 0.020) |
| colour_next | 0.554 (1397) | 0.529 (9992) [0.522, 0.537] | 0.529 (42831) [0.525, 0.533] | 0.515 (85748) [0.510, 0.519] | 0.530 (41399) [0.526, 0.534] | 0.575 (569) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.504 (19558) | 0.502 (139888) [0.500, 0.504] | 0.501 (599634) [0.499, 0.502] | 0.501 (1200472) [0.500, 0.502] | 0.501 (579586) [0.499, 0.502] | 0.509 (7966) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.654 (52) | 0.604 (323) [0.574, 0.638] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.600 (35) | 0.500 | flat -0.032 (noise 0.038) |
| reversal_k13_next | 0.431 (58) | 0.339 (386) [0.297, 0.384] | 0.318 (1957) [0.306, 0.332] | 0.310 (4004) [0.299, 0.321] | 0.321 (1899) [0.308, 0.333] | 0.375 (16) | 0.077 | flat +0.030 (noise 0.032) |
| reversal_k13_now | 0.645 (62) | 0.577 (430) [0.535, 0.618] | 0.569 (1661) [0.549, 0.589] | 0.574 (3081) [0.560, 0.589] | 0.567 (1609) [0.547, 0.590] | 0.593 (27) | 0.077 | flat +0.047 (noise 0.037) |
| reversal_k3_next | 0.586 (157) | 0.588 (829) [0.582, 0.592] | 0.582 (3011) [0.572, 0.593] | 0.584 (5391) [0.575, 0.594] | 0.582 (2951) [0.571, 0.594] | 0.547 (53) | 0.294 | flat -0.005 (noise 0.025) |
| reversal_k3_now | 0.932 (74) | 0.945 (418) [0.920, 0.968] | 0.936 (1732) [0.926, 0.946] | 0.939 (3441) [0.933, 0.946] | 0.936 (1678) [0.926, 0.946] | 0.955 (22) | 0.294 | flat +0.000 (noise 0.018) |
| reversal_k5_next | 0.551 (69) | 0.519 (524) [0.507, 0.537] | 0.471 (2960) [0.458, 0.486] | 0.480 (4830) [0.469, 0.492] | 0.471 (2840) [0.456, 0.486] | 0.400 (25) | 0.187 | up +0.059 (noise 0.027) |
| reversal_k5_now | 0.797 (64) | 0.826 (409) [0.812, 0.839] | 0.822 (1628) [0.811, 0.833] | 0.829 (3180) [0.819, 0.839] | 0.821 (1569) [0.810, 0.832] | 0.840 (25) | 0.187 | flat +0.015 (noise 0.028) |
| reversal_k8_next | 0.484 (97) | 0.408 (714) [0.381, 0.436] | 0.388 (2842) [0.376, 0.401] | 0.391 (4901) [0.381, 0.402] | 0.388 (2795) [0.374, 0.401] | 0.444 (18) | 0.121 | flat +0.031 (noise 0.025) |
| reversal_k8_now | 0.763 (59) | 0.705 (380) [0.649, 0.749] | 0.692 (1583) [0.671, 0.712] | 0.702 (3119) [0.687, 0.718] | 0.690 (1532) [0.667, 0.711] | 0.739 (23) | 0.121 | flat +0.052 (noise 0.038) |
| overall | 0.511 (21691) | 0.507 (154642) [0.504, 0.509] | 0.504 (662716) [0.503, 0.506] | 0.504 (1323921) [0.503, 0.504] | 0.504 (640640) [0.503, 0.506] | 0.515 (8783) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08153, 0.1254] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5323, 'levels': [{'threshold': 0.08153, 'calls_per_day': 144.0, 'win_rate': 0.5978}, {'threshold': 0.1254, 'calls_per_day': 36.1, 'win_rate': 0.6}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 40825, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15075 | 0.335 | 0.527 (14803) | 0.581 (2163) | 0.756 (2643) |
| volatility: normal | 15075 | 0.366 | 0.532 (15002) | 0.613 (1476) | 0.749 (2240) |
| volatility: wild | 15075 | 0.380 | 0.526 (15032) | 0.631 (762) | 0.771 (2047) |
| session: Asia 00-08 | 15360 | 0.359 | 0.533 (15248) | 0.600 (1580) | 0.762 (2324) |
| session: Europe 08-13 | 9405 | 0.355 | 0.530 (9310) | 0.597 (1089) | 0.754 (1559) |
| session: US 13-21 | 14880 | 0.368 | 0.527 (14758) | 0.600 (1127) | 0.759 (2213) |
| session: late 21-24 | 5580 | 0.351 | 0.517 (5521) | 0.607 (605) | 0.749 (834) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.305 | 0.328 | 0.211 | 0.211 | 0.448 | 0.205 | 0.405 | 1.371 |
| 6h | 360 | 0.299 | 0.295 | 0.216 | 0.228 | 0.565 | 0.229 | 0.368 | 1.191 |
| 24h | 1440 | 0.319 | 0.312 | 0.230 | 0.248 | 0.577 | 0.255 | 0.384 | 1.277 |
| 7d | 10080 | 0.362 | 0.356 | 0.278 | 0.308 | 0.532 | 0.261 | 0.462 | 1.277 |
| 30d | 43200 | 0.360 | 0.352 | 0.274 | 0.303 | 0.530 | 0.260 | 0.460 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.305 / 0.448 / 0.917; 2: 0.305 / 0.483 / 0.933; 3: 0.317 / 0.534 / 0.917; 4: 0.306 / 0.466 / 0.917; 5: 0.295 / 0.517 / 0.900; 6: 0.299 / 0.500 / 0.933; 7: 0.281 / 0.397 / 0.900; 8: 0.312 / 0.517 / 0.900; 9: 0.306 / 0.483 / 0.917; 10: 0.289 / 0.466 / 0.917; 11: 0.276 / 0.397 / 0.917; 12: 0.291 / 0.552 / 0.867; 13: 0.312 / 0.569 / 0.850; 14: 0.297 / 0.517 / 0.867; 15: 0.317 / 0.569 / 0.850
- 6h: 1: 0.299 / 0.565 / 0.875; 2: 0.277 / 0.443 / 0.931; 3: 0.300 / 0.551 / 0.911; 4: 0.282 / 0.458 / 0.883; 5: 0.299 / 0.539 / 0.878; 6: 0.295 / 0.516 / 0.931; 7: 0.273 / 0.441 / 0.917; 8: 0.298 / 0.513 / 0.919; 9: 0.296 / 0.499 / 0.925; 10: 0.294 / 0.522 / 0.925; 11: 0.283 / 0.481 / 0.914; 12: 0.281 / 0.507 / 0.872; 13: 0.300 / 0.577 / 0.897; 14: 0.282 / 0.499 / 0.903; 15: 0.293 / 0.548 / 0.850
- 24h: 1: 0.319 / 0.577 / 0.878; 2: 0.297 / 0.479 / 0.906; 3: 0.305 / 0.526 / 0.895; 4: 0.296 / 0.494 / 0.887; 5: 0.308 / 0.544 / 0.887; 6: 0.298 / 0.500 / 0.901; 7: 0.290 / 0.467 / 0.901; 8: 0.297 / 0.513 / 0.901; 9: 0.307 / 0.527 / 0.906; 10: 0.298 / 0.511 / 0.904; 11: 0.296 / 0.507 / 0.906; 12: 0.295 / 0.507 / 0.896; 13: 0.301 / 0.525 / 0.898; 14: 0.291 / 0.483 / 0.900; 15: 0.301 / 0.530 / 0.894
- 7d: 1: 0.362 / 0.532 / 0.895; 2: 0.349 / 0.490 / 0.901; 3: 0.352 / 0.510 / 0.900; 4: 0.349 / 0.501 / 0.900; 5: 0.350 / 0.511 / 0.900; 6: 0.346 / 0.504 / 0.901; 7: 0.348 / 0.497 / 0.901; 8: 0.347 / 0.509 / 0.901; 9: 0.349 / 0.506 / 0.902; 10: 0.348 / 0.505 / 0.902; 11: 0.345 / 0.500 / 0.901; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.504 / 0.901; 14: 0.345 / 0.499 / 0.900; 15: 0.346 / 0.502 / 0.899
- 30d: 1: 0.360 / 0.530 / 0.898; 2: 0.348 / 0.497 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.347 / 0.504 / 0.900; 6: 0.345 / 0.498 / 0.900; 7: 0.346 / 0.499 / 0.900; 8: 0.346 / 0.502 / 0.900; 9: 0.345 / 0.498 / 0.900; 10: 0.346 / 0.505 / 0.900; 11: 0.343 / 0.497 / 0.900; 12: 0.345 / 0.503 / 0.900; 13: 0.344 / 0.502 / 0.900; 14: 0.343 / 0.500 / 0.900; 15: 0.344 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.123 (body 0.093, range 0.153); 'price stays where it was' would score 0.074; colour right 0.328; typical miss of the close 5.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.087 (body 0.066, range 0.108); 'price stays where it was' would score 0.068; colour right 0.461; typical miss of the close 5.5 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.113 (body 0.084, range 0.142); 'price stays where it was' would score 0.112; colour right 0.511; typical miss of the close 4.5 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.166); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 8.5 bp; chain ended on the right side 0.513 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 7.7 bp; chain ended on the right side 0.519 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.9; 2: 0.198 / 4.5; 3: 0.168 / 6.0; 4: 0.131 / 6.4; 5: 0.125 / 7.1; 6: 0.113 / 7.5; 7: 0.111 / 7.9; 8: 0.098 / 8.5; 9: 0.089 / 8.4; 10: 0.088 / 9.1; 11: 0.085 / 9.5; 12: 0.076 / 9.9; 13: 0.067 / 10.0; 14: 0.069 / 10.4; 15: 0.063 / 10.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 129939, probability skill vs chance 0.2312, widened contest next: False
  - now: threshold 0.8348, hit rate recent 0.9434 / long run 0.9429
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.249, naive rule 0.452, lift 3.70x
    - 24h: 68 calls (68 a day), hit rate 0.941, chance 0.299, naive rule 0.516, lift 3.15x
    - 7d: 420 calls (60 a day), hit rate 0.950, chance 0.292, naive rule 0.495, lift 3.25x
    - 30d: 1732 calls (58 a day), hit rate 0.935, chance 0.294, naive rule 0.495, lift 3.18x
  - next: threshold 0.5303, hit rate recent 0.5685 / long run 0.5864
    - 6h: 29 calls (118 a day), hit rate 0.483, chance 0.249, lift 1.94x
    - 24h: 140 calls (140 a day), hit rate 0.593, chance 0.299, lift 1.98x
    - 7d: 859 calls (123 a day), hit rate 0.582, chance 0.292, lift 1.99x
    - 30d: 3050 calls (102 a day), hit rate 0.580, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.497; 0.35: 535, 0.522; 0.40: 474, 0.580; 0.45: 404, 0.652; 0.50: 354, 0.701; 0.55: 309, 0.743; 0.60: 261, 0.788; 0.65: 219, 0.814; 0.70: 173, 0.846; 0.75: 136, 0.879; 0.80: 92, 0.914; 0.85: 47, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.427; 0.35: 502, 0.463; 0.40: 407, 0.496; 0.45: 310, 0.531; 0.50: 201, 0.568; 0.55: 90, 0.570; 0.60: 13, 0.646; 0.65: 1, 0.654
- **K=5**: model 1792540800, labels learned 129937, probability skill vs chance 0.2232, widened contest next: False
  - now: threshold 0.6789, hit rate recent 0.8141 / long run 0.8223
    - 6h: 14 calls (57 a day), hit rate 0.714, chance 0.171, naive rule 0.384, lift 4.17x
    - 24h: 62 calls (62 a day), hit rate 0.790, chance 0.195, naive rule 0.430, lift 4.04x
    - 7d: 414 calls (59 a day), hit rate 0.831, chance 0.188, naive rule 0.410, lift 4.42x
    - 30d: 1629 calls (54 a day), hit rate 0.823, chance 0.188, naive rule 0.405, lift 4.37x
  - next: threshold 0.4517, hit rate recent 0.5024 / long run 0.4969
    - 6h: 16 calls (65 a day), hit rate 0.375, chance 0.171, lift 2.19x
    - 24h: 66 calls (66 a day), hit rate 0.485, chance 0.195, lift 2.48x
    - 7d: 491 calls (70 a day), hit rate 0.513, chance 0.188, lift 2.73x
    - 30d: 2958 calls (99 a day), hit rate 0.471, chance 0.188, lift 2.51x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.493; 0.40: 278, 0.567; 0.45: 227, 0.620; 0.50: 180, 0.668; 0.55: 142, 0.707; 0.60: 108, 0.751; 0.65: 76, 0.790; 0.70: 50, 0.826; 0.75: 30, 0.870; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.388; 0.35: 256, 0.419; 0.40: 161, 0.457; 0.45: 69, 0.477; 0.50: 13, 0.489; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 129934, probability skill vs chance 0.2081, widened contest next: False
  - now: threshold 0.5651, hit rate recent 0.7429 / long run 0.697
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.123, naive rule 0.307, lift 5.01x
    - 24h: 59 calls (59 a day), hit rate 0.746, chance 0.119, naive rule 0.324, lift 6.25x
    - 7d: 381 calls (54 a day), hit rate 0.709, chance 0.123, naive rule 0.343, lift 5.74x
    - 30d: 1586 calls (53 a day), hit rate 0.692, chance 0.121, naive rule 0.334, lift 5.71x
  - next: threshold 0.3611, hit rate recent 0.4767 / long run 0.4075
    - 6h: 10 calls (41 a day), hit rate 0.400, chance 0.123, lift 3.26x
    - 24h: 65 calls (65 a day), hit rate 0.492, chance 0.119, lift 4.13x
    - 7d: 681 calls (97 a day), hit rate 0.410, chance 0.123, lift 3.32x
    - 30d: 2839 calls (95 a day), hit rate 0.389, chance 0.121, lift 3.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 189, 0.502; 0.40: 147, 0.548; 0.45: 113, 0.596; 0.50: 84, 0.640; 0.55: 61, 0.679; 0.60: 41, 0.715; 0.65: 24, 0.787; 0.70: 11, 0.812; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.357; 0.35: 92, 0.386; 0.40: 28, 0.410; 0.45: 6, 0.430; 0.50: 1, 0.630
- **K=13**: model 1793491200, labels learned 129929, probability skill vs chance 0.1976, widened contest next: False
  - now: threshold 0.4132, hit rate recent 0.6177 / long run 0.5719
    - 6h: 15 calls (63 a day), hit rate 0.533, chance 0.078, naive rule 0.250, lift 6.81x
    - 24h: 65 calls (66 a day), hit rate 0.569, chance 0.084, naive rule 0.284, lift 6.79x
    - 7d: 432 calls (62 a day), hit rate 0.581, chance 0.080, naive rule 0.290, lift 7.30x
    - 30d: 1669 calls (56 a day), hit rate 0.569, chance 0.078, naive rule 0.279, lift 7.33x
  - next: threshold 0.293, hit rate recent 0.3894 / long run 0.3252
    - 6h: 8 calls (33 a day), hit rate 0.375, chance 0.078, lift 4.79x
    - 24h: 51 calls (52 a day), hit rate 0.392, chance 0.084, lift 4.68x
    - 7d: 373 calls (53 a day), hit rate 0.338, chance 0.080, lift 4.24x
    - 30d: 1948 calls (65 a day), hit rate 0.319, chance 0.078, lift 4.11x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 127, 0.445; 0.35: 91, 0.498; 0.40: 65, 0.553; 0.45: 43, 0.598; 0.50: 29, 0.654; 0.55: 18, 0.694; 0.60: 9, 0.740; 0.65: 2, 0.733; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.326; 0.35: 14, 0.353; 0.40: 3, 0.446; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.628 | -0.40% | 0.900 | 0.533 | 0.250 | 0.534 | 0.177 |
| 6h | 6.664 | 0.73% | 0.886 | 0.500 | 0.250 | 0.504 | 0.346 |
| 24h | 7.270 | 4.86% | 0.889 | 0.492 | 0.249 | 0.531 | 0.372 |
| 7d | 15.611 | 4.95% | 0.899 | 0.501 | 0.250 | 0.506 | 0.747 |
| 30d | 13.969 | 4.50% | 0.900 | 0.500 | 0.251 | 0.498 | 0.698 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.597 | 7.642 | 7.650 | 7.764 | 7.917 | 7.814 | 7.586 | 7.529 | 7.594 | 7.628 |
| 6h | 6.712 | 6.693 | 6.681 | 6.699 | 6.816 | 6.878 | 6.662 | 6.618 | 6.646 | 6.664 |
| 24h | 7.641 | 7.344 | 7.396 | 7.314 | 7.519 | 7.646 | 7.258 | 7.255 | 7.260 | 7.270 |
| 7d | 16.425 | 15.792 | 15.738 | 15.644 | 15.947 | 15.890 | 15.594 | 15.574 | 15.582 | 15.611 |
| 30d | 14.627 | 14.119 | 14.065 | 13.999 | 14.233 | 14.184 | 13.965 | 13.942 | 13.944 | 13.969 |

## Next candle

- candle starting 2026-11-01 09:45 UTC, last close 2268.07
- P(up) 0.5157, return quantiles (bp): {'05': -4.455, '10': -3.27, '25': -1.517, '40': -0.255, '50': 0.043, '60': 0.458, '75': 1.71, '90': 3.588, '95': 4.621}
- changepoint probability 0.1211, regime age 74.4 min
- agent weights: empirical 0.028, ewma 0.108, garch 0.106, har 0.151, bocpd 0.023, hmm 0.011, online_qr 0.257, lgbm 0.315

## Learning log

- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- HMM volatility states (sd, bp per minute): [3.03, 6.64, 20.06], current probabilities: [0.983, 0.016, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-01 09:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.343, 'l_abs': 0.614, 'l_hi': 0.693, 'l_lo': 0.73, 'b05': 0.631, 'b25': 0.552, 'b75': 0.674, 'b95': 0.634}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.308, 2.0, 2.558, 2.809, 2.33, 2.625, 2.756, 2.814, 2.913, 3.251, 4.073, 3.693, 3.764, 4.963]}
- calibration offsets (in sigma): {'05': 0.012, '10': 0.034, '25': 0.02, '40': 0.046, '50': -0.01, '60': -0.066, '75': -0.0, '90': 0.066, '95': 0.018}
