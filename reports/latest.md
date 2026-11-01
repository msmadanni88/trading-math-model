# ETH-USD 60s candle generator - report

- generated: 2026-11-01 16:27 UTC
- last closed candle: 2026-11-01 16:27 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.524 (672) [0.491, 0.562] | 0.521 (2877) [0.502, 0.540] | 0.516 (5754) [0.503, 0.528] | 0.520 (2782) [0.502, 0.540] | 0.492 (65) | 0.500 | flat -0.019 (noise 0.030) |
| colour_clear | 0.569 (723) | 0.541 (5558) [0.533, 0.551] | 0.544 (23531) [0.539, 0.549] | 0.520 (47049) [0.514, 0.526] | 0.546 (22811) [0.541, 0.550] | 0.542 (500) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.582 (184) | 0.587 (1090) [0.579, 0.596] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.559 (186) | 0.500 | flat -0.021 (noise 0.020) |
| colour_next | 0.554 (1397) | 0.529 (9992) [0.522, 0.537] | 0.529 (42831) [0.525, 0.533] | 0.515 (85748) [0.510, 0.519] | 0.530 (41399) [0.526, 0.534] | 0.544 (962) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.504 (19558) | 0.502 (139888) [0.500, 0.504] | 0.501 (599634) [0.499, 0.502] | 0.501 (1200472) [0.500, 0.502] | 0.501 (579586) [0.499, 0.502] | 0.506 (13468) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.654 (52) | 0.604 (323) [0.574, 0.638] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.580 (50) | 0.500 | flat -0.032 (noise 0.038) |
| reversal_k13_next | 0.431 (58) | 0.339 (386) [0.297, 0.384] | 0.318 (1957) [0.306, 0.332] | 0.310 (4004) [0.299, 0.321] | 0.321 (1899) [0.308, 0.333] | 0.333 (18) | 0.077 | flat +0.030 (noise 0.032) |
| reversal_k13_now | 0.645 (62) | 0.577 (430) [0.535, 0.618] | 0.569 (1661) [0.549, 0.589] | 0.574 (3081) [0.560, 0.589] | 0.567 (1609) [0.547, 0.590] | 0.610 (41) | 0.077 | flat +0.047 (noise 0.037) |
| reversal_k3_next | 0.586 (157) | 0.588 (829) [0.582, 0.592] | 0.582 (3011) [0.572, 0.593] | 0.584 (5391) [0.575, 0.594] | 0.582 (2951) [0.571, 0.594] | 0.607 (84) | 0.294 | flat -0.005 (noise 0.025) |
| reversal_k3_now | 0.932 (74) | 0.945 (418) [0.920, 0.968] | 0.936 (1732) [0.926, 0.946] | 0.939 (3441) [0.933, 0.946] | 0.936 (1678) [0.926, 0.946] | 0.864 (44) | 0.294 | flat +0.000 (noise 0.018) |
| reversal_k5_next | 0.551 (69) | 0.519 (524) [0.507, 0.537] | 0.471 (2960) [0.458, 0.486] | 0.480 (4830) [0.469, 0.492] | 0.471 (2840) [0.456, 0.486] | 0.500 (40) | 0.187 | up +0.059 (noise 0.027) |
| reversal_k5_now | 0.797 (64) | 0.826 (409) [0.812, 0.839] | 0.822 (1628) [0.811, 0.833] | 0.829 (3180) [0.819, 0.839] | 0.821 (1569) [0.810, 0.832] | 0.841 (44) | 0.187 | flat +0.015 (noise 0.028) |
| reversal_k8_next | 0.484 (97) | 0.408 (714) [0.381, 0.436] | 0.388 (2842) [0.376, 0.401] | 0.391 (4901) [0.381, 0.402] | 0.388 (2795) [0.374, 0.401] | 0.444 (27) | 0.121 | flat +0.031 (noise 0.025) |
| reversal_k8_now | 0.763 (59) | 0.705 (380) [0.649, 0.749] | 0.692 (1583) [0.671, 0.712] | 0.702 (3119) [0.687, 0.718] | 0.690 (1532) [0.667, 0.711] | 0.744 (39) | 0.121 | flat +0.052 (noise 0.038) |
| overall | 0.511 (21691) | 0.507 (154642) [0.504, 0.509] | 0.504 (662716) [0.503, 0.506] | 0.504 (1323921) [0.503, 0.504] | 0.504 (640640) [0.503, 0.506] | 0.511 (14832) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08187, 0.1256] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5322, 'levels': [{'threshold': 0.08187, 'calls_per_day': 145.4, 'win_rate': 0.5977}, {'threshold': 0.1256, 'calls_per_day': 36.9, 'win_rate': 0.5939}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 41218, 'rate': 0.5308}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15209 | 0.334 | 0.527 (14928) | 0.580 (2202) | 0.756 (2668) |
| volatility: normal | 15209 | 0.366 | 0.532 (15136) | 0.609 (1499) | 0.749 (2272) |
| volatility: wild | 15209 | 0.380 | 0.526 (15166) | 0.631 (768) | 0.770 (2061) |
| session: Asia 00-08 | 15360 | 0.359 | 0.533 (15248) | 0.600 (1580) | 0.762 (2324) |
| session: Europe 08-13 | 9600 | 0.355 | 0.530 (9497) | 0.595 (1131) | 0.754 (1591) |
| session: US 13-21 | 15087 | 0.368 | 0.526 (14964) | 0.595 (1153) | 0.760 (2252) |
| session: late 21-24 | 5580 | 0.351 | 0.517 (5521) | 0.607 (605) | 0.749 (834) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.355 | 0.343 | 0.276 | 0.276 | 0.467 | 0.272 | 0.438 | 1.266 |
| 6h | 360 | 0.327 | 0.336 | 0.251 | 0.279 | 0.487 | 0.238 | 0.416 | 1.479 |
| 24h | 1440 | 0.319 | 0.313 | 0.234 | 0.254 | 0.551 | 0.251 | 0.387 | 1.290 |
| 7d | 10080 | 0.361 | 0.355 | 0.278 | 0.307 | 0.530 | 0.261 | 0.461 | 1.301 |
| 30d | 43200 | 0.360 | 0.352 | 0.274 | 0.302 | 0.530 | 0.260 | 0.459 | 1.282 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.355 / 0.467 / 0.933; 2: 0.361 / 0.550 / 0.900; 3: 0.363 / 0.533 / 0.950; 4: 0.337 / 0.400 / 0.983; 5: 0.375 / 0.567 / 0.983; 6: 0.357 / 0.517 / 0.967; 7: 0.345 / 0.533 / 1.000; 8: 0.383 / 0.667 / 1.000; 9: 0.330 / 0.383 / 0.983; 10: 0.336 / 0.467 / 0.967; 11: 0.364 / 0.600 / 0.967; 12: 0.356 / 0.583 / 1.000; 13: 0.344 / 0.500 / 1.000; 14: 0.386 / 0.600 / 0.983; 15: 0.389 / 0.617 / 1.000
- 6h: 1: 0.327 / 0.487 / 0.911; 2: 0.315 / 0.499 / 0.894; 3: 0.321 / 0.533 / 0.961; 4: 0.317 / 0.490 / 0.972; 5: 0.333 / 0.558 / 0.969; 6: 0.320 / 0.530 / 0.944; 7: 0.313 / 0.501 / 0.953; 8: 0.317 / 0.513 / 0.958; 9: 0.308 / 0.482 / 0.947; 10: 0.300 / 0.433 / 0.944; 11: 0.324 / 0.524 / 0.956; 12: 0.313 / 0.493 / 0.964; 13: 0.317 / 0.496 / 0.961; 14: 0.317 / 0.487 / 0.956; 15: 0.316 / 0.504 / 0.958
- 24h: 1: 0.319 / 0.551 / 0.890; 2: 0.298 / 0.478 / 0.900; 3: 0.307 / 0.529 / 0.903; 4: 0.301 / 0.494 / 0.908; 5: 0.313 / 0.548 / 0.910; 6: 0.303 / 0.509 / 0.915; 7: 0.297 / 0.480 / 0.918; 8: 0.300 / 0.504 / 0.920; 9: 0.307 / 0.514 / 0.919; 10: 0.299 / 0.505 / 0.919; 11: 0.305 / 0.520 / 0.924; 12: 0.298 / 0.504 / 0.919; 13: 0.303 / 0.520 / 0.922; 14: 0.295 / 0.481 / 0.924; 15: 0.304 / 0.530 / 0.920
- 7d: 1: 0.361 / 0.530 / 0.896; 2: 0.348 / 0.489 / 0.901; 3: 0.352 / 0.511 / 0.903; 4: 0.348 / 0.501 / 0.902; 5: 0.350 / 0.512 / 0.902; 6: 0.345 / 0.503 / 0.902; 7: 0.348 / 0.498 / 0.902; 8: 0.346 / 0.507 / 0.903; 9: 0.348 / 0.506 / 0.903; 10: 0.346 / 0.501 / 0.903; 11: 0.344 / 0.500 / 0.903; 12: 0.345 / 0.500 / 0.903; 13: 0.345 / 0.503 / 0.904; 14: 0.345 / 0.498 / 0.903; 15: 0.345 / 0.503 / 0.902
- 30d: 1: 0.360 / 0.530 / 0.898; 2: 0.348 / 0.497 / 0.900; 3: 0.350 / 0.509 / 0.900; 4: 0.346 / 0.499 / 0.901; 5: 0.347 / 0.504 / 0.901; 6: 0.345 / 0.498 / 0.901; 7: 0.345 / 0.499 / 0.901; 8: 0.345 / 0.502 / 0.901; 9: 0.344 / 0.498 / 0.901; 10: 0.345 / 0.505 / 0.901; 11: 0.343 / 0.498 / 0.901; 12: 0.344 / 0.503 / 0.900; 13: 0.344 / 0.502 / 0.901; 14: 0.343 / 0.499 / 0.900; 15: 0.343 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.174 (body 0.133, range 0.216); 'price stays where it was' would score 0.158; colour right 0.450; typical miss of the close 4.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.124 (body 0.089, range 0.159); 'price stays where it was' would score 0.134; colour right 0.450; typical miss of the close 4.6 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.110 (body 0.082, range 0.138); 'price stays where it was' would score 0.113; colour right 0.489; typical miss of the close 4.6 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 8.2 bp; chain ended on the right side 0.512 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.6 bp; chain ended on the right side 0.520 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.9; 2: 0.197 / 4.5; 3: 0.168 / 6.0; 4: 0.131 / 6.4; 5: 0.125 / 7.0; 6: 0.112 / 7.5; 7: 0.110 / 7.9; 8: 0.098 / 8.4; 9: 0.090 / 8.3; 10: 0.088 / 9.0; 11: 0.085 / 9.3; 12: 0.076 / 9.8; 13: 0.068 / 9.9; 14: 0.070 / 10.3; 15: 0.063 / 10.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 130341, probability skill vs chance 0.2265, widened contest next: True
  - now: threshold 0.8357, hit rate recent 0.8931 / long run 0.9368
    - 6h: 20 calls (81 a day), hit rate 0.800, chance 0.334, naive rule 0.553, lift 2.40x
    - 24h: 64 calls (64 a day), hit rate 0.891, chance 0.307, naive rule 0.532, lift 2.90x
    - 7d: 430 calls (61 a day), hit rate 0.940, chance 0.294, naive rule 0.498, lift 3.19x
    - 30d: 1736 calls (58 a day), hit rate 0.933, chance 0.295, naive rule 0.496, lift 3.17x
  - next: threshold 0.5305, hit rate recent 0.624 / long run 0.5926
    - 6h: 28 calls (114 a day), hit rate 0.714, chance 0.334, lift 2.14x
    - 24h: 131 calls (131 a day), hit rate 0.626, chance 0.307, lift 2.04x
    - 7d: 869 calls (124 a day), hit rate 0.589, chance 0.294, lift 2.00x
    - 30d: 3058 calls (102 a day), hit rate 0.582, chance 0.295, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 535, 0.523; 0.40: 474, 0.581; 0.45: 404, 0.653; 0.50: 354, 0.702; 0.55: 309, 0.745; 0.60: 260, 0.789; 0.65: 219, 0.814; 0.70: 173, 0.845; 0.75: 137, 0.879; 0.80: 92, 0.912; 0.85: 47, 0.946; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 591, 0.428; 0.35: 502, 0.464; 0.40: 407, 0.497; 0.45: 310, 0.531; 0.50: 201, 0.568; 0.55: 90, 0.571; 0.60: 13, 0.643; 0.65: 1, 0.640
- **K=5**: model 1792540800, labels learned 130339, probability skill vs chance 0.2248, widened contest next: False
  - now: threshold 0.68, hit rate recent 0.8236 / long run 0.8229
    - 6h: 18 calls (73 a day), hit rate 0.833, chance 0.207, naive rule 0.480, lift 4.03x
    - 24h: 60 calls (60 a day), hit rate 0.850, chance 0.197, naive rule 0.449, lift 4.31x
    - 7d: 420 calls (60 a day), hit rate 0.826, chance 0.190, naive rule 0.416, lift 4.34x
    - 30d: 1628 calls (54 a day), hit rate 0.821, chance 0.188, naive rule 0.405, lift 4.36x
  - next: threshold 0.4502, hit rate recent 0.5405 / long run 0.5011
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.207, lift 3.63x
    - 24h: 63 calls (63 a day), hit rate 0.540, chance 0.197, lift 2.74x
    - 7d: 471 calls (67 a day), hit rate 0.524, chance 0.190, lift 2.75x
    - 30d: 2929 calls (98 a day), hit rate 0.471, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.494; 0.40: 278, 0.568; 0.45: 227, 0.621; 0.50: 180, 0.668; 0.55: 142, 0.706; 0.60: 108, 0.750; 0.65: 76, 0.788; 0.70: 50, 0.824; 0.75: 30, 0.867; 0.80: 10, 0.891
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.387; 0.35: 256, 0.419; 0.40: 161, 0.457; 0.45: 69, 0.477; 0.50: 13, 0.487; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 130336, probability skill vs chance 0.2021, widened contest next: False
  - now: threshold 0.5655, hit rate recent 0.7447 / long run 0.6984
    - 6h: 15 calls (62 a day), hit rate 0.733, chance 0.129, naive rule 0.386, lift 5.70x
    - 24h: 53 calls (53 a day), hit rate 0.774, chance 0.118, naive rule 0.328, lift 6.57x
    - 7d: 386 calls (55 a day), hit rate 0.705, chance 0.124, naive rule 0.347, lift 5.67x
    - 30d: 1585 calls (53 a day), hit rate 0.691, chance 0.121, naive rule 0.333, lift 5.71x
  - next: threshold 0.3631, hit rate recent 0.4721 / long run 0.408
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.129, lift 3.46x
    - 24h: 44 calls (44 a day), hit rate 0.500, chance 0.118, lift 4.24x
    - 7d: 656 calls (94 a day), hit rate 0.413, chance 0.124, lift 3.32x
    - 30d: 2833 calls (94 a day), hit rate 0.389, chance 0.121, lift 3.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 189, 0.500; 0.40: 147, 0.547; 0.45: 113, 0.594; 0.50: 84, 0.639; 0.55: 61, 0.678; 0.60: 41, 0.715; 0.65: 24, 0.786; 0.70: 11, 0.808; 0.75: 2, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.356; 0.35: 92, 0.387; 0.40: 28, 0.412; 0.45: 5, 0.435; 0.50: 1, 0.630
- **K=13**: model 1793491200, labels learned 130331, probability skill vs chance 0.1917, widened contest next: False
  - now: threshold 0.4272, hit rate recent 0.6223 / long run 0.5735
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.065, naive rule 0.262, lift 9.86x
    - 24h: 54 calls (55 a day), hit rate 0.648, chance 0.079, naive rule 0.281, lift 8.25x
    - 7d: 432 calls (62 a day), hit rate 0.579, chance 0.079, naive rule 0.292, lift 7.29x
    - 30d: 1667 calls (56 a day), hit rate 0.569, chance 0.077, naive rule 0.279, lift 7.34x
  - next: threshold 0.2917, hit rate recent 0.3765 / long run 0.3241
    - 24h: 33 calls (33 a day), hit rate 0.485, chance 0.079, lift 6.17x
    - 7d: 351 calls (50 a day), hit rate 0.336, chance 0.079, lift 4.24x
    - 30d: 1933 calls (64 a day), hit rate 0.320, chance 0.077, lift 4.13x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 127, 0.445; 0.35: 91, 0.498; 0.40: 65, 0.553; 0.45: 43, 0.598; 0.50: 29, 0.654; 0.55: 18, 0.690; 0.60: 9, 0.738; 0.65: 2, 0.733; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.327; 0.35: 14, 0.353; 0.40: 3, 0.446; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.035 | -0.71% | 0.900 | 0.417 | 0.253 | 0.450 | 0.014 |
| 6h | 8.625 | 1.18% | 0.911 | 0.533 | 0.249 | 0.527 | 0.355 |
| 24h | 7.571 | 1.65% | 0.898 | 0.497 | 0.250 | 0.517 | 0.358 |
| 7d | 15.445 | 5.00% | 0.900 | 0.502 | 0.250 | 0.507 | 0.749 |
| 30d | 13.871 | 4.48% | 0.900 | 0.500 | 0.251 | 0.498 | 0.699 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.979 | 7.961 | 8.017 | 8.079 | 8.081 | 8.151 | 7.993 | 7.968 | 7.986 | 8.035 |
| 6h | 8.728 | 8.795 | 8.740 | 8.635 | 8.912 | 8.914 | 8.606 | 8.623 | 8.614 | 8.625 |
| 24h | 7.698 | 7.664 | 7.664 | 7.606 | 7.819 | 7.890 | 7.561 | 7.553 | 7.557 | 7.571 |
| 7d | 16.257 | 15.625 | 15.571 | 15.479 | 15.776 | 15.730 | 15.429 | 15.410 | 15.417 | 15.445 |
| 30d | 14.522 | 14.021 | 13.967 | 13.901 | 14.134 | 14.088 | 13.865 | 13.843 | 13.846 | 13.871 |

## Next candle

- candle starting 2026-11-01 16:27 UTC, last close 2266.85
- P(up) 0.5028, return quantiles (bp): {'05': -4.329, '10': -3.156, '25': -1.432, '40': -0.508, '50': 0.021, '60': 0.425, '75': 1.432, '90': 3.529, '95': 4.569}
- changepoint probability 0.052, regime age 191.4 min
- agent weights: empirical 0.053, ewma 0.065, garch 0.087, har 0.180, bocpd 0.015, hmm 0.010, online_qr 0.298, lgbm 0.292

## Learning log

- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- HMM volatility states (sd, bp per minute): [2.72, 6.38, 19.49], current probabilities: [0.965, 0.035, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-01 16:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.319, 'l_abs': 0.639, 'l_hi': 0.687, 'l_lo': 0.717, 'b05': 0.63, 'b25': 0.533, 'b75': 0.684, 'b95': 0.648}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.8], [1.3, 1.6], [1.2, 1.8], [1.2, 1.8], [1.3, 1.6]], 'cone_width': [1.383, 1.233, 1.398, 1.566, 1.619, 1.684, 1.665, 1.879, 1.984, 2.044, 2.364, 2.187, 2.367, 2.998]}
- calibration offsets (in sigma): {'05': 0.053, '10': 0.046, '25': 0.055, '40': 0.034, '50': 0.01, '60': -0.034, '75': -0.055, '90': 0.044, '95': -0.003}
