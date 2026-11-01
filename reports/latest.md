# ETH-USD 60s candle generator - report

- generated: 2026-11-01 23:56 UTC
- last closed candle: 2026-11-01 23:56 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.524 (672) [0.491, 0.562] | 0.521 (2877) [0.502, 0.540] | 0.516 (5754) [0.503, 0.528] | 0.520 (2782) [0.502, 0.540] | 0.453 (95) | 0.500 | flat -0.019 (noise 0.030) |
| colour_clear | 0.569 (723) | 0.541 (5558) [0.533, 0.551] | 0.544 (23531) [0.539, 0.549] | 0.520 (47049) [0.514, 0.526] | 0.546 (22811) [0.541, 0.550] | 0.537 (746) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.582 (184) | 0.587 (1090) [0.579, 0.596] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.550 (229) | 0.500 | flat -0.021 (noise 0.020) |
| colour_next | 0.554 (1397) | 0.529 (9992) [0.522, 0.537] | 0.529 (42831) [0.525, 0.533] | 0.515 (85748) [0.510, 0.519] | 0.530 (41399) [0.526, 0.534] | 0.531 (1404) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.504 (19558) | 0.502 (139888) [0.500, 0.504] | 0.501 (599634) [0.499, 0.502] | 0.501 (1200472) [0.500, 0.502] | 0.501 (579586) [0.499, 0.502] | 0.505 (19656) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.654 (52) | 0.604 (323) [0.574, 0.638] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.607 (56) | 0.500 | flat -0.032 (noise 0.038) |
| reversal_k13_next | 0.431 (58) | 0.339 (386) [0.297, 0.384] | 0.318 (1957) [0.306, 0.332] | 0.310 (4004) [0.299, 0.321] | 0.321 (1899) [0.308, 0.333] | 0.343 (35) | 0.077 | flat +0.030 (noise 0.032) |
| reversal_k13_now | 0.645 (62) | 0.577 (430) [0.535, 0.618] | 0.569 (1661) [0.549, 0.589] | 0.574 (3081) [0.560, 0.589] | 0.567 (1609) [0.547, 0.590] | 0.576 (66) | 0.077 | flat +0.047 (noise 0.037) |
| reversal_k3_next | 0.586 (157) | 0.588 (829) [0.582, 0.592] | 0.582 (3011) [0.572, 0.593] | 0.584 (5391) [0.575, 0.594] | 0.582 (2951) [0.571, 0.594] | 0.614 (132) | 0.294 | flat -0.005 (noise 0.025) |
| reversal_k3_now | 0.932 (74) | 0.945 (418) [0.920, 0.968] | 0.936 (1732) [0.926, 0.946] | 0.939 (3441) [0.933, 0.946] | 0.936 (1678) [0.926, 0.946] | 0.895 (67) | 0.294 | flat +0.000 (noise 0.018) |
| reversal_k5_next | 0.551 (69) | 0.519 (524) [0.507, 0.537] | 0.471 (2960) [0.458, 0.486] | 0.480 (4830) [0.469, 0.492] | 0.471 (2840) [0.456, 0.486] | 0.567 (60) | 0.187 | up +0.059 (noise 0.027) |
| reversal_k5_now | 0.797 (64) | 0.826 (409) [0.812, 0.839] | 0.822 (1628) [0.811, 0.833] | 0.829 (3180) [0.819, 0.839] | 0.821 (1569) [0.810, 0.832] | 0.831 (71) | 0.187 | flat +0.015 (noise 0.028) |
| reversal_k8_next | 0.484 (97) | 0.408 (714) [0.381, 0.436] | 0.388 (2842) [0.376, 0.401] | 0.391 (4901) [0.381, 0.402] | 0.388 (2795) [0.374, 0.401] | 0.500 (50) | 0.121 | flat +0.031 (noise 0.025) |
| reversal_k8_now | 0.763 (59) | 0.705 (380) [0.649, 0.749] | 0.692 (1583) [0.671, 0.712] | 0.702 (3119) [0.687, 0.718] | 0.690 (1532) [0.667, 0.711] | 0.710 (62) | 0.121 | flat +0.052 (noise 0.038) |
| overall | 0.511 (21691) | 0.507 (154642) [0.504, 0.509] | 0.504 (662716) [0.503, 0.506] | 0.504 (1323921) [0.503, 0.504] | 0.504 (640640) [0.503, 0.506] | 0.510 (21698) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08154, 0.125] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.53, 'levels': [{'threshold': 0.08154, 'calls_per_day': 142.4, 'win_rate': 0.5893}, {'threshold': 0.125, 'calls_per_day': 35.3, 'win_rate': 0.596}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 41660, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15359 | 0.334 | 0.527 (15073) | 0.579 (2217) | 0.755 (2710) |
| volatility: normal | 15358 | 0.365 | 0.530 (15284) | 0.606 (1514) | 0.750 (2308) |
| volatility: wild | 15359 | 0.380 | 0.526 (15315) | 0.632 (781) | 0.770 (2081) |
| session: Asia 00-08 | 15360 | 0.359 | 0.533 (15248) | 0.600 (1580) | 0.762 (2324) |
| session: Europe 08-13 | 9600 | 0.355 | 0.530 (9497) | 0.595 (1131) | 0.754 (1591) |
| session: US 13-21 | 15360 | 0.367 | 0.526 (15234) | 0.595 (1179) | 0.760 (2304) |
| session: late 21-24 | 5756 | 0.350 | 0.515 (5693) | 0.600 (622) | 0.746 (880) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.366 | 0.380 | 0.309 | 0.309 | 0.433 | 0.216 | 0.517 | 1.094 |
| 6h | 360 | 0.345 | 0.338 | 0.264 | 0.283 | 0.508 | 0.240 | 0.449 | 1.068 |
| 24h | 1440 | 0.329 | 0.325 | 0.245 | 0.267 | 0.531 | 0.247 | 0.411 | 1.184 |
| 7d | 10080 | 0.360 | 0.354 | 0.277 | 0.306 | 0.530 | 0.260 | 0.460 | 1.311 |
| 30d | 43200 | 0.360 | 0.352 | 0.273 | 0.302 | 0.530 | 0.260 | 0.459 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.366 / 0.433 / 0.867; 2: 0.371 / 0.433 / 0.900; 3: 0.362 / 0.450 / 0.983; 4: 0.374 / 0.517 / 0.983; 5: 0.363 / 0.483 / 0.983; 6: 0.379 / 0.567 / 0.983; 7: 0.333 / 0.450 / 1.000; 8: 0.341 / 0.483 / 1.000; 9: 0.348 / 0.500 / 1.000; 10: 0.375 / 0.550 / 1.000; 11: 0.373 / 0.533 / 1.000; 12: 0.351 / 0.517 / 0.967; 13: 0.358 / 0.500 / 0.983; 14: 0.370 / 0.567 / 0.967; 15: 0.335 / 0.483 / 0.950
- 6h: 1: 0.345 / 0.508 / 0.869; 2: 0.340 / 0.483 / 0.886; 3: 0.343 / 0.492 / 0.842; 4: 0.339 / 0.506 / 0.842; 5: 0.328 / 0.483 / 0.850; 6: 0.332 / 0.492 / 0.833; 7: 0.324 / 0.492 / 0.822; 8: 0.327 / 0.489 / 0.806; 9: 0.331 / 0.525 / 0.831; 10: 0.330 / 0.514 / 0.814; 11: 0.343 / 0.540 / 0.803; 12: 0.332 / 0.508 / 0.811; 13: 0.340 / 0.525 / 0.778; 14: 0.340 / 0.525 / 0.794; 15: 0.330 / 0.514 / 0.817
- 24h: 1: 0.329 / 0.531 / 0.885; 2: 0.315 / 0.483 / 0.893; 3: 0.322 / 0.515 / 0.890; 4: 0.318 / 0.495 / 0.894; 5: 0.324 / 0.529 / 0.892; 6: 0.316 / 0.504 / 0.890; 7: 0.311 / 0.483 / 0.886; 8: 0.313 / 0.499 / 0.883; 9: 0.317 / 0.500 / 0.890; 10: 0.314 / 0.501 / 0.889; 11: 0.321 / 0.522 / 0.887; 12: 0.314 / 0.505 / 0.890; 13: 0.319 / 0.522 / 0.883; 14: 0.313 / 0.488 / 0.886; 15: 0.318 / 0.525 / 0.890
- 7d: 1: 0.360 / 0.530 / 0.896; 2: 0.347 / 0.490 / 0.900; 3: 0.351 / 0.508 / 0.900; 4: 0.348 / 0.500 / 0.900; 5: 0.350 / 0.514 / 0.900; 6: 0.345 / 0.501 / 0.900; 7: 0.347 / 0.496 / 0.900; 8: 0.346 / 0.506 / 0.899; 9: 0.348 / 0.506 / 0.900; 10: 0.346 / 0.503 / 0.900; 11: 0.344 / 0.501 / 0.900; 12: 0.345 / 0.500 / 0.900; 13: 0.345 / 0.503 / 0.899; 14: 0.345 / 0.501 / 0.899; 15: 0.345 / 0.504 / 0.899
- 30d: 1: 0.360 / 0.530 / 0.897; 2: 0.348 / 0.497 / 0.900; 3: 0.350 / 0.509 / 0.900; 4: 0.346 / 0.499 / 0.900; 5: 0.347 / 0.504 / 0.900; 6: 0.345 / 0.499 / 0.900; 7: 0.345 / 0.499 / 0.899; 8: 0.345 / 0.502 / 0.899; 9: 0.344 / 0.498 / 0.900; 10: 0.345 / 0.505 / 0.899; 11: 0.342 / 0.498 / 0.899; 12: 0.344 / 0.503 / 0.899; 13: 0.344 / 0.502 / 0.899; 14: 0.343 / 0.499 / 0.899; 15: 0.343 / 0.500 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.135 (body 0.086, range 0.185); 'price stays where it was' would score 0.089; colour right 0.450; typical miss of the close 12.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.115 (body 0.074, range 0.156); 'price stays where it was' would score 0.117; colour right 0.483; typical miss of the close 5.8 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.110 (body 0.079, range 0.142); 'price stays where it was' would score 0.111; colour right 0.478; typical miss of the close 5.2 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.166); 'price stays where it was' would score 0.131; colour right 0.501; typical miss of the close 8.1 bp; chain ended on the right side 0.496 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.128; colour right 0.500; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.198 / 4.5; 3: 0.168 / 5.9; 4: 0.131 / 6.4; 5: 0.124 / 7.0; 6: 0.112 / 7.5; 7: 0.109 / 7.9; 8: 0.098 / 8.4; 9: 0.089 / 8.3; 10: 0.088 / 9.0; 11: 0.085 / 9.3; 12: 0.076 / 9.7; 13: 0.067 / 9.8; 14: 0.070 / 10.3; 15: 0.063 / 10.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 130790, probability skill vs chance 0.2381, widened contest next: False
  - now: threshold 0.8369, hit rate recent 0.9112 / long run 0.9375
    - 6h: 19 calls (77 a day), hit rate 0.947, chance 0.279, naive rule 0.512, lift 3.40x
    - 24h: 67 calls (67 a day), hit rate 0.896, chance 0.293, naive rule 0.516, lift 3.05x
    - 7d: 439 calls (63 a day), hit rate 0.945, chance 0.294, naive rule 0.498, lift 3.22x
    - 30d: 1745 calls (58 a day), hit rate 0.935, chance 0.295, naive rule 0.496, lift 3.17x
  - next: threshold 0.5304, hit rate recent 0.6081 / long run 0.5949
    - 6h: 38 calls (154 a day), hit rate 0.579, chance 0.279, lift 2.08x
    - 24h: 132 calls (132 a day), hit rate 0.614, chance 0.293, lift 2.09x
    - 7d: 881 calls (126 a day), hit rate 0.591, chance 0.294, lift 2.01x
    - 30d: 3083 calls (103 a day), hit rate 0.583, chance 0.295, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.499; 0.35: 534, 0.524; 0.40: 473, 0.582; 0.45: 404, 0.653; 0.50: 354, 0.703; 0.55: 309, 0.745; 0.60: 261, 0.789; 0.65: 219, 0.815; 0.70: 173, 0.846; 0.75: 137, 0.879; 0.80: 92, 0.914; 0.85: 47, 0.947; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 591, 0.428; 0.35: 502, 0.464; 0.40: 407, 0.497; 0.45: 310, 0.532; 0.50: 201, 0.569; 0.55: 90, 0.572; 0.60: 13, 0.647; 0.65: 1, 0.640
- **K=5**: model 1792540800, labels learned 130788, probability skill vs chance 0.2301, widened contest next: False
  - now: threshold 0.6817, hit rate recent 0.8155 / long run 0.8225
    - 6h: 23 calls (94 a day), hit rate 0.783, chance 0.177, naive rule 0.422, lift 4.42x
    - 24h: 71 calls (71 a day), hit rate 0.831, chance 0.188, naive rule 0.441, lift 4.42x
    - 7d: 431 calls (62 a day), hit rate 0.826, chance 0.190, naive rule 0.416, lift 4.36x
    - 30d: 1640 calls (55 a day), hit rate 0.821, chance 0.188, naive rule 0.405, lift 4.37x
  - next: threshold 0.4493, hit rate recent 0.5815 / long run 0.5076
    - 6h: 18 calls (73 a day), hit rate 0.667, chance 0.177, lift 3.77x
    - 24h: 60 calls (60 a day), hit rate 0.567, chance 0.188, lift 3.01x
    - 7d: 447 calls (64 a day), hit rate 0.532, chance 0.190, lift 2.81x
    - 30d: 2901 calls (97 a day), hit rate 0.473, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 345, 0.493; 0.40: 278, 0.567; 0.45: 227, 0.621; 0.50: 180, 0.668; 0.55: 142, 0.706; 0.60: 109, 0.750; 0.65: 76, 0.790; 0.70: 51, 0.824; 0.75: 30, 0.869; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.387; 0.35: 256, 0.419; 0.40: 161, 0.457; 0.45: 69, 0.479; 0.50: 13, 0.496; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 130785, probability skill vs chance 0.2105, widened contest next: False
  - now: threshold 0.5667, hit rate recent 0.7124 / long run 0.6966
    - 6h: 19 calls (78 a day), hit rate 0.632, chance 0.114, naive rule 0.343, lift 5.53x
    - 24h: 62 calls (62 a day), hit rate 0.710, chance 0.123, naive rule 0.356, lift 5.75x
    - 7d: 394 calls (56 a day), hit rate 0.703, chance 0.124, naive rule 0.347, lift 5.69x
    - 30d: 1594 calls (53 a day), hit rate 0.691, chance 0.121, naive rule 0.334, lift 5.71x
  - next: threshold 0.3637, hit rate recent 0.4941 / long run 0.4138
    - 6h: 19 calls (78 a day), hit rate 0.526, chance 0.114, lift 4.61x
    - 24h: 50 calls (50 a day), hit rate 0.500, chance 0.123, lift 4.05x
    - 7d: 645 calls (92 a day), hit rate 0.416, chance 0.124, lift 3.36x
    - 30d: 2845 calls (95 a day), hit rate 0.390, chance 0.121, lift 3.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 189, 0.501; 0.40: 148, 0.547; 0.45: 113, 0.594; 0.50: 84, 0.639; 0.55: 61, 0.677; 0.60: 41, 0.713; 0.65: 24, 0.786; 0.70: 11, 0.811; 0.75: 2, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.357; 0.35: 92, 0.387; 0.40: 28, 0.416; 0.45: 5, 0.438; 0.50: 1, 0.630
- **K=13**: model 1793491200, labels learned 130780, probability skill vs chance 0.1941, widened contest next: False
  - now: threshold 0.4352, hit rate recent 0.5845 / long run 0.5713
    - 6h: 21 calls (88 a day), hit rate 0.524, chance 0.072, naive rule 0.279, lift 7.23x
    - 24h: 66 calls (67 a day), hit rate 0.576, chance 0.076, naive rule 0.280, lift 7.60x
    - 7d: 441 calls (63 a day), hit rate 0.574, chance 0.080, naive rule 0.293, lift 7.21x
    - 30d: 1675 calls (56 a day), hit rate 0.568, chance 0.078, naive rule 0.279, lift 7.32x
  - next: threshold 0.2905, hit rate recent 0.3716 / long run 0.3249
    - 6h: 15 calls (63 a day), hit rate 0.400, chance 0.072, lift 5.52x
    - 24h: 35 calls (35 a day), hit rate 0.343, chance 0.076, lift 4.52x
    - 7d: 355 calls (51 a day), hit rate 0.335, chance 0.080, lift 4.21x
    - 30d: 1934 calls (64 a day), hit rate 0.321, chance 0.078, lift 4.14x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 128, 0.444; 0.35: 92, 0.496; 0.40: 65, 0.551; 0.45: 44, 0.596; 0.50: 29, 0.654; 0.55: 18, 0.687; 0.60: 9, 0.734; 0.65: 3, 0.727; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.328; 0.35: 14, 0.351; 0.40: 3, 0.434; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.683 | 6.25% | 0.900 | 0.517 | 0.248 | 0.517 | 0.423 |
| 6h | 9.747 | 3.21% | 0.883 | 0.464 | 0.250 | 0.480 | 0.540 |
| 24h | 8.152 | 1.79% | 0.894 | 0.486 | 0.250 | 0.505 | 0.449 |
| 7d | 15.193 | 4.89% | 0.900 | 0.500 | 0.250 | 0.505 | 0.753 |
| 30d | 13.834 | 4.44% | 0.899 | 0.499 | 0.251 | 0.498 | 0.700 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.663 | 14.750 | 14.740 | 14.890 | 14.862 | 14.831 | 14.816 | 14.767 | 14.732 | 14.683 |
| 6h | 10.071 | 9.839 | 9.823 | 9.786 | 9.917 | 9.817 | 9.753 | 9.737 | 9.739 | 9.747 |
| 24h | 8.300 | 8.242 | 8.206 | 8.173 | 8.333 | 8.323 | 8.142 | 8.136 | 8.137 | 8.152 |
| 7d | 15.974 | 15.363 | 15.315 | 15.227 | 15.504 | 15.476 | 15.176 | 15.159 | 15.165 | 15.193 |
| 30d | 14.477 | 13.981 | 13.929 | 13.863 | 14.094 | 14.049 | 13.828 | 13.806 | 13.809 | 13.834 |

## Next candle

- candle starting 2026-11-01 23:56 UTC, last close 2272.65
- P(up) 0.5484, return quantiles (bp): {'05': -6.925, '10': -5.415, '25': -2.503, '40': -0.376, '50': 0.335, '60': 1.183, '75': 3.005, '90': 5.245, '95': 7.064}
- changepoint probability 0.05, regime age 60.1 min
- agent weights: empirical 0.012, ewma 0.086, garch 0.107, har 0.163, bocpd 0.023, hmm 0.034, online_qr 0.275, lgbm 0.299

## Learning log

- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- HMM volatility states (sd, bp per minute): [2.72, 6.38, 19.49], current probabilities: [0.464, 0.531, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-11-02 00:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.32, 'l_abs': 0.659, 'l_hi': 0.707, 'l_lo': 0.717, 'b05': 0.627, 'b25': 0.612, 'b75': 0.733, 'b95': 0.648}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.5, 1.8], [1.4, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.6]], 'cone_width': [1.563, 2.078, 2.264, 2.588, 3.139, 3.466, 4.357, 3.642, 4.337, 4.744, 4.493, 5.61, 5.604, 5.366]}
- calibration offsets (in sigma): {'05': 0.0075, '10': -0.035, '25': 0.0275, '40': 0.11, '50': 0.075, '60': 0.05, '75': 0.0725, '90': 0.015, '95': 0.0025}
