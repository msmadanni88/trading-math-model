# ETH-USD 60s candle generator - report

- generated: 2026-11-01 20:45 UTC
- last closed candle: 2026-11-01 20:45 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.524 (672) [0.491, 0.562] | 0.521 (2877) [0.502, 0.540] | 0.516 (5754) [0.503, 0.528] | 0.520 (2782) [0.502, 0.540] | 0.470 (83) | 0.500 | flat -0.019 (noise 0.030) |
| colour_clear | 0.569 (723) | 0.541 (5558) [0.533, 0.551] | 0.544 (23531) [0.539, 0.549] | 0.520 (47049) [0.514, 0.526] | 0.546 (22811) [0.541, 0.550] | 0.547 (643) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.582 (184) | 0.587 (1090) [0.579, 0.596] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.564 (211) | 0.500 | flat -0.021 (noise 0.020) |
| colour_next | 0.554 (1397) | 0.529 (9992) [0.522, 0.537] | 0.529 (42831) [0.525, 0.533] | 0.515 (85748) [0.510, 0.519] | 0.530 (41399) [0.526, 0.534] | 0.539 (1218) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.504 (19558) | 0.502 (139888) [0.500, 0.504] | 0.501 (599634) [0.499, 0.502] | 0.501 (1200472) [0.500, 0.502] | 0.501 (579586) [0.499, 0.502] | 0.505 (17052) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.654 (52) | 0.604 (323) [0.574, 0.638] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.618 (55) | 0.500 | flat -0.032 (noise 0.038) |
| reversal_k13_next | 0.431 (58) | 0.339 (386) [0.297, 0.384] | 0.318 (1957) [0.306, 0.332] | 0.310 (4004) [0.299, 0.321] | 0.321 (1899) [0.308, 0.333] | 0.333 (24) | 0.077 | flat +0.030 (noise 0.032) |
| reversal_k13_now | 0.645 (62) | 0.577 (430) [0.535, 0.618] | 0.569 (1661) [0.549, 0.589] | 0.574 (3081) [0.560, 0.589] | 0.567 (1609) [0.547, 0.590] | 0.604 (53) | 0.077 | flat +0.047 (noise 0.037) |
| reversal_k3_next | 0.586 (157) | 0.588 (829) [0.582, 0.592] | 0.582 (3011) [0.572, 0.593] | 0.584 (5391) [0.575, 0.594] | 0.582 (2951) [0.571, 0.594] | 0.631 (111) | 0.294 | flat -0.005 (noise 0.025) |
| reversal_k3_now | 0.932 (74) | 0.945 (418) [0.920, 0.968] | 0.936 (1732) [0.926, 0.946] | 0.939 (3441) [0.933, 0.946] | 0.936 (1678) [0.926, 0.946] | 0.895 (57) | 0.294 | flat +0.000 (noise 0.018) |
| reversal_k5_next | 0.551 (69) | 0.519 (524) [0.507, 0.537] | 0.471 (2960) [0.458, 0.486] | 0.480 (4830) [0.469, 0.492] | 0.471 (2840) [0.456, 0.486] | 0.553 (47) | 0.187 | up +0.059 (noise 0.027) |
| reversal_k5_now | 0.797 (64) | 0.826 (409) [0.812, 0.839] | 0.822 (1628) [0.811, 0.833] | 0.829 (3180) [0.819, 0.839] | 0.821 (1569) [0.810, 0.832] | 0.848 (59) | 0.187 | flat +0.015 (noise 0.028) |
| reversal_k8_next | 0.484 (97) | 0.408 (714) [0.381, 0.436] | 0.388 (2842) [0.376, 0.401] | 0.391 (4901) [0.381, 0.402] | 0.388 (2795) [0.374, 0.401] | 0.514 (35) | 0.121 | flat +0.031 (noise 0.025) |
| reversal_k8_now | 0.763 (59) | 0.705 (380) [0.649, 0.749] | 0.692 (1583) [0.671, 0.712] | 0.702 (3119) [0.687, 0.718] | 0.690 (1532) [0.667, 0.711] | 0.726 (51) | 0.121 | flat +0.052 (noise 0.038) |
| overall | 0.511 (21691) | 0.507 (154642) [0.504, 0.509] | 0.504 (662716) [0.503, 0.506] | 0.504 (1323921) [0.503, 0.504] | 0.504 (640640) [0.503, 0.506] | 0.511 (18790) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08154, 0.125] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.53, 'levels': [{'threshold': 0.08154, 'calls_per_day': 142.4, 'win_rate': 0.5893}, {'threshold': 0.125, 'calls_per_day': 35.3, 'win_rate': 0.596}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 41474, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15295 | 0.334 | 0.527 (15013) | 0.580 (2209) | 0.754 (2692) |
| volatility: normal | 15295 | 0.365 | 0.531 (15221) | 0.607 (1508) | 0.753 (2289) |
| volatility: wild | 15295 | 0.380 | 0.526 (15252) | 0.632 (777) | 0.769 (2072) |
| session: Asia 00-08 | 15360 | 0.359 | 0.533 (15248) | 0.600 (1580) | 0.762 (2324) |
| session: Europe 08-13 | 9600 | 0.355 | 0.530 (9497) | 0.595 (1131) | 0.754 (1591) |
| session: US 13-21 | 15345 | 0.367 | 0.526 (15220) | 0.595 (1178) | 0.760 (2304) |
| session: late 21-24 | 5580 | 0.351 | 0.517 (5521) | 0.607 (605) | 0.749 (834) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.343 | 0.300 | 0.277 | 0.277 | 0.583 | 0.268 | 0.417 | 0.913 |
| 6h | 360 | 0.337 | 0.329 | 0.242 | 0.286 | 0.510 | 0.248 | 0.426 | 1.166 |
| 24h | 1440 | 0.323 | 0.318 | 0.239 | 0.265 | 0.536 | 0.246 | 0.400 | 1.224 |
| 7d | 10080 | 0.360 | 0.354 | 0.278 | 0.307 | 0.530 | 0.261 | 0.460 | 1.312 |
| 30d | 43200 | 0.360 | 0.352 | 0.273 | 0.302 | 0.530 | 0.260 | 0.459 | 1.279 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.343 / 0.583 / 0.933; 2: 0.329 / 0.533 / 0.867; 3: 0.320 / 0.500 / 0.700; 4: 0.301 / 0.417 / 0.717; 5: 0.353 / 0.533 / 0.700; 6: 0.312 / 0.450 / 0.683; 7: 0.364 / 0.583 / 0.667; 8: 0.307 / 0.433 / 0.633; 9: 0.360 / 0.583 / 0.667; 10: 0.311 / 0.450 / 0.633; 11: 0.373 / 0.617 / 0.650; 12: 0.317 / 0.483 / 0.683; 13: 0.345 / 0.567 / 0.650; 14: 0.341 / 0.567 / 0.667; 15: 0.365 / 0.617 / 0.717
- 6h: 1: 0.337 / 0.510 / 0.889; 2: 0.338 / 0.513 / 0.878; 3: 0.331 / 0.490 / 0.814; 4: 0.333 / 0.504 / 0.828; 5: 0.338 / 0.527 / 0.817; 6: 0.332 / 0.496 / 0.797; 7: 0.325 / 0.501 / 0.789; 8: 0.333 / 0.521 / 0.753; 9: 0.330 / 0.496 / 0.794; 10: 0.316 / 0.459 / 0.778; 11: 0.348 / 0.571 / 0.775; 12: 0.332 / 0.515 / 0.811; 13: 0.334 / 0.507 / 0.767; 14: 0.334 / 0.510 / 0.775; 15: 0.345 / 0.557 / 0.833
- 24h: 1: 0.323 / 0.536 / 0.892; 2: 0.311 / 0.491 / 0.895; 3: 0.315 / 0.516 / 0.884; 4: 0.311 / 0.496 / 0.888; 5: 0.319 / 0.539 / 0.883; 6: 0.310 / 0.506 / 0.882; 7: 0.307 / 0.490 / 0.877; 8: 0.307 / 0.504 / 0.873; 9: 0.314 / 0.509 / 0.881; 10: 0.305 / 0.494 / 0.881; 11: 0.315 / 0.519 / 0.878; 12: 0.306 / 0.500 / 0.881; 13: 0.311 / 0.517 / 0.873; 14: 0.304 / 0.481 / 0.874; 15: 0.313 / 0.532 / 0.883
- 7d: 1: 0.360 / 0.530 / 0.895; 2: 0.348 / 0.489 / 0.900; 3: 0.351 / 0.509 / 0.898; 4: 0.348 / 0.499 / 0.899; 5: 0.350 / 0.513 / 0.898; 6: 0.345 / 0.501 / 0.897; 7: 0.347 / 0.498 / 0.897; 8: 0.346 / 0.506 / 0.896; 9: 0.348 / 0.507 / 0.897; 10: 0.346 / 0.502 / 0.897; 11: 0.344 / 0.501 / 0.897; 12: 0.345 / 0.500 / 0.897; 13: 0.345 / 0.503 / 0.897; 14: 0.345 / 0.499 / 0.897; 15: 0.345 / 0.504 / 0.898
- 30d: 1: 0.360 / 0.530 / 0.897; 2: 0.348 / 0.497 / 0.900; 3: 0.350 / 0.509 / 0.899; 4: 0.346 / 0.499 / 0.900; 5: 0.347 / 0.504 / 0.900; 6: 0.345 / 0.498 / 0.899; 7: 0.345 / 0.499 / 0.899; 8: 0.345 / 0.502 / 0.899; 9: 0.344 / 0.498 / 0.900; 10: 0.345 / 0.505 / 0.899; 11: 0.342 / 0.498 / 0.899; 12: 0.344 / 0.502 / 0.899; 13: 0.344 / 0.502 / 0.899; 14: 0.343 / 0.499 / 0.899; 15: 0.343 / 0.500 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.119 (body 0.071, range 0.166); 'price stays where it was' would score 0.137; colour right 0.467; typical miss of the close 5.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.142; colour right 0.462; typical miss of the close 4.6 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.110 (body 0.079, range 0.141); 'price stays where it was' would score 0.115; colour right 0.475; typical miss of the close 4.8 bp; chain ended on the right side 0.438 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.2 bp; chain ended on the right side 0.501 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.128; colour right 0.500; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.9; 2: 0.198 / 4.5; 3: 0.168 / 5.9; 4: 0.131 / 6.4; 5: 0.125 / 7.0; 6: 0.112 / 7.4; 7: 0.110 / 7.9; 8: 0.098 / 8.4; 9: 0.090 / 8.3; 10: 0.088 / 8.9; 11: 0.085 / 9.3; 12: 0.075 / 9.7; 13: 0.067 / 9.8; 14: 0.070 / 10.3; 15: 0.063 / 10.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 130599, probability skill vs chance 0.2361, widened contest next: False
  - now: threshold 0.8369, hit rate recent 0.914 / long run 0.9382
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.314, naive rule 0.578, lift 3.01x
    - 24h: 60 calls (60 a day), hit rate 0.900, chance 0.298, naive rule 0.531, lift 3.02x
    - 7d: 436 calls (62 a day), hit rate 0.943, chance 0.293, naive rule 0.498, lift 3.21x
    - 30d: 1745 calls (58 a day), hit rate 0.934, chance 0.295, naive rule 0.496, lift 3.17x
  - next: threshold 0.5304, hit rate recent 0.6513 / long run 0.5975
    - 6h: 38 calls (154 a day), hit rate 0.684, chance 0.314, lift 2.18x
    - 24h: 127 calls (127 a day), hit rate 0.630, chance 0.298, lift 2.11x
    - 7d: 874 calls (125 a day), hit rate 0.593, chance 0.293, lift 2.02x
    - 30d: 3076 calls (103 a day), hit rate 0.583, chance 0.295, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.499; 0.35: 535, 0.524; 0.40: 474, 0.581; 0.45: 404, 0.653; 0.50: 354, 0.703; 0.55: 309, 0.745; 0.60: 261, 0.789; 0.65: 219, 0.815; 0.70: 173, 0.846; 0.75: 137, 0.879; 0.80: 92, 0.913; 0.85: 47, 0.947; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 591, 0.428; 0.35: 502, 0.464; 0.40: 407, 0.497; 0.45: 310, 0.531; 0.50: 201, 0.568; 0.55: 90, 0.572; 0.60: 13, 0.645; 0.65: 1, 0.640
- **K=5**: model 1792540800, labels learned 130597, probability skill vs chance 0.2276, widened contest next: False
  - now: threshold 0.6817, hit rate recent 0.8318 / long run 0.824
    - 6h: 21 calls (86 a day), hit rate 0.857, chance 0.188, naive rule 0.442, lift 4.55x
    - 24h: 62 calls (62 a day), hit rate 0.855, chance 0.192, naive rule 0.449, lift 4.46x
    - 7d: 426 calls (61 a day), hit rate 0.826, chance 0.190, naive rule 0.417, lift 4.35x
    - 30d: 1637 calls (55 a day), hit rate 0.821, chance 0.188, naive rule 0.405, lift 4.37x
  - next: threshold 0.4493, hit rate recent 0.5748 / long run 0.5052
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.188, lift 4.17x
    - 24h: 57 calls (57 a day), hit rate 0.579, chance 0.192, lift 3.02x
    - 7d: 456 calls (65 a day), hit rate 0.531, chance 0.190, lift 2.79x
    - 30d: 2909 calls (97 a day), hit rate 0.471, chance 0.188, lift 2.51x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.493; 0.40: 278, 0.568; 0.45: 227, 0.620; 0.50: 180, 0.668; 0.55: 142, 0.706; 0.60: 109, 0.750; 0.65: 76, 0.789; 0.70: 51, 0.824; 0.75: 30, 0.867; 0.80: 11, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.387; 0.35: 256, 0.419; 0.40: 161, 0.457; 0.45: 69, 0.477; 0.50: 13, 0.491; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 130594, probability skill vs chance 0.2048, widened contest next: False
  - now: threshold 0.5667, hit rate recent 0.7296 / long run 0.6977
    - 6h: 16 calls (66 a day), hit rate 0.688, chance 0.130, naive rule 0.403, lift 5.29x
    - 24h: 54 calls (54 a day), hit rate 0.741, chance 0.121, naive rule 0.350, lift 6.14x
    - 7d: 390 calls (56 a day), hit rate 0.703, chance 0.124, naive rule 0.347, lift 5.66x
    - 30d: 1593 calls (53 a day), hit rate 0.691, chance 0.121, naive rule 0.334, lift 5.71x
  - next: threshold 0.3637, hit rate recent 0.5068 / long run 0.4125
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.130, lift 5.38x
    - 24h: 42 calls (42 a day), hit rate 0.500, chance 0.121, lift 4.14x
    - 7d: 647 calls (93 a day), hit rate 0.414, chance 0.124, lift 3.34x
    - 30d: 2835 calls (95 a day), hit rate 0.389, chance 0.121, lift 3.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 189, 0.501; 0.40: 148, 0.547; 0.45: 113, 0.594; 0.50: 84, 0.639; 0.55: 61, 0.677; 0.60: 41, 0.714; 0.65: 24, 0.785; 0.70: 11, 0.809; 0.75: 2, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.357; 0.35: 92, 0.387; 0.40: 28, 0.412; 0.45: 5, 0.438; 0.50: 1, 0.630
- **K=13**: model 1793491200, labels learned 130589, probability skill vs chance 0.1957, widened contest next: False
  - now: threshold 0.4352, hit rate recent 0.6156 / long run 0.5737
    - 6h: 16 calls (67 a day), hit rate 0.562, chance 0.080, naive rule 0.333, lift 7.06x
    - 24h: 56 calls (57 a day), hit rate 0.625, chance 0.076, naive rule 0.287, lift 8.21x
    - 7d: 439 calls (63 a day), hit rate 0.576, chance 0.080, naive rule 0.294, lift 7.22x
    - 30d: 1671 calls (56 a day), hit rate 0.569, chance 0.078, naive rule 0.279, lift 7.33x
  - next: threshold 0.2905, hit rate recent 0.3729 / long run 0.3242
    - 6h: 6 calls (25 a day), hit rate 0.333, chance 0.080, lift 4.18x
    - 24h: 30 calls (30 a day), hit rate 0.400, chance 0.076, lift 5.25x
    - 7d: 353 calls (51 a day), hit rate 0.334, chance 0.080, lift 4.19x
    - 30d: 1929 calls (64 a day), hit rate 0.320, chance 0.078, lift 4.13x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 127, 0.445; 0.35: 91, 0.498; 0.40: 65, 0.552; 0.45: 44, 0.598; 0.50: 29, 0.655; 0.55: 18, 0.690; 0.60: 9, 0.737; 0.65: 3, 0.727; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.327; 0.35: 14, 0.352; 0.40: 3, 0.439; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.060 | -0.54% | 0.917 | 0.433 | 0.252 | 0.383 | -0.021 |
| 6h | 7.805 | 0.96% | 0.892 | 0.458 | 0.251 | 0.482 | 0.306 |
| 24h | 7.688 | 1.38% | 0.899 | 0.490 | 0.250 | 0.507 | 0.360 |
| 7d | 15.379 | 5.02% | 0.900 | 0.500 | 0.250 | 0.506 | 0.751 |
| 30d | 13.817 | 4.47% | 0.900 | 0.500 | 0.251 | 0.498 | 0.700 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.017 | 7.973 | 8.048 | 7.990 | 8.036 | 8.003 | 8.020 | 8.077 | 8.007 | 8.060 |
| 6h | 7.881 | 7.852 | 7.852 | 7.814 | 7.912 | 7.864 | 7.780 | 7.770 | 7.780 | 7.805 |
| 24h | 7.796 | 7.786 | 7.760 | 7.708 | 7.898 | 7.913 | 7.675 | 7.667 | 7.672 | 7.688 |
| 7d | 16.191 | 15.557 | 15.505 | 15.411 | 15.703 | 15.657 | 15.362 | 15.344 | 15.350 | 15.379 |
| 30d | 14.465 | 13.964 | 13.913 | 13.846 | 14.077 | 14.033 | 13.811 | 13.789 | 13.792 | 13.817 |

## Next candle

- candle starting 2026-11-01 20:45 UTC, last close 2259.97
- P(up) 0.5011, return quantiles (bp): {'05': -4.678, '10': -3.614, '25': -1.905, '40': -0.638, '50': 0.012, '60': 0.548, '75': 1.607, '90': 3.312, '95': 4.544}
- changepoint probability 0.0405, regime age 72.7 min
- agent weights: empirical 0.043, ewma 0.060, garch 0.081, har 0.183, bocpd 0.024, hmm 0.031, online_qr 0.275, lgbm 0.303

## Learning log

- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- HMM volatility states (sd, bp per minute): [2.72, 6.38, 19.49], current probabilities: [0.975, 0.025, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-01 20:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.308, 'l_abs': 0.677, 'l_hi': 0.698, 'l_lo': 0.728, 'b05': 0.63, 'b25': 0.585, 'b75': 0.731, 'b95': 0.649}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.8], [1.3, 1.6], [1.2, 1.8], [1.3, 1.8], [1.3, 1.6]], 'cone_width': [1.566, 2.594, 2.771, 3.431, 3.919, 4.504, 5.776, 4.829, 5.637, 5.924, 5.498, 7.004, 6.997, 5.942]}
- calibration offsets (in sigma): {'05': 0.022, '10': -0.016, '25': -0.02, '40': -0.004, '50': 0.01, '60': -0.006, '75': 0.01, '90': -0.004, '95': -0.012}
