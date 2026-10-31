# ETH-USD 60s candle generator - report

- generated: 2026-10-31 20:36 UTC
- last closed candle: 2026-10-31 20:36 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.525 (672) [0.493, 0.564] | 0.520 (2877) [0.501, 0.539] | 0.516 (5658) [0.502, 0.529] | 0.521 (2686) [0.500, 0.541] | 0.537 (82) | 0.500 | flat -0.013 (noise 0.030) |
| colour_clear | 0.537 (771) | 0.538 (5578) [0.532, 0.544] | 0.541 (23615) [0.534, 0.547] | 0.519 (46326) [0.513, 0.525] | 0.545 (22088) [0.540, 0.549] | 0.574 (629) | 0.500 | flat -0.018 (noise 0.009) |
| colour_confident | 0.590 (78) | 0.592 (1175) [0.583, 0.602] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.581 (155) | 0.500 | flat -0.013 (noise 0.020) |
| colour_next | 0.532 (1435) | 0.525 (10026) [0.520, 0.528] | 0.527 (42871) [0.523, 0.531] | 0.514 (84351) [0.510, 0.518] | 0.529 (40002) [0.525, 0.533] | 0.559 (1206) | 0.500 | flat -0.013 (noise 0.007) |
| colour_path | 0.503 (20090) | 0.502 (140364) [0.500, 0.504] | 0.501 (600194) [0.499, 0.502] | 0.501 (1180914) [0.500, 0.502] | 0.501 (560028) [0.499, 0.502] | 0.502 (16884) | 0.500 | flat +0.003 (noise 0.002) |
| colour_strong | 0.538 (13) | 0.596 (369) [0.574, 0.625] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.659 (44) | 0.500 | flat -0.046 (noise 0.039) |
| reversal_k13_next | 0.283 (53) | 0.317 (391) [0.282, 0.359] | 0.315 (2003) [0.303, 0.327] | 0.308 (3946) [0.297, 0.319] | 0.317 (1841) [0.306, 0.329] | 0.404 (52) | 0.077 | flat +0.003 (noise 0.032) |
| reversal_k13_now | 0.597 (57) | 0.575 (419) [0.531, 0.618] | 0.567 (1653) [0.547, 0.587] | 0.572 (3019) [0.558, 0.587] | 0.564 (1547) [0.543, 0.587] | 0.621 (58) | 0.077 | flat +0.050 (noise 0.035) |
| reversal_k3_next | 0.595 (116) | 0.591 (726) [0.583, 0.599] | 0.583 (2939) [0.571, 0.595] | 0.584 (5234) [0.575, 0.594] | 0.582 (2794) [0.570, 0.593] | 0.573 (138) | 0.293 | flat +0.005 (noise 0.025) |
| reversal_k3_now | 0.933 (45) | 0.952 (393) [0.924, 0.977] | 0.936 (1731) [0.926, 0.946] | 0.939 (3367) [0.933, 0.946] | 0.936 (1604) [0.925, 0.947] | 0.927 (69) | 0.293 | flat +0.022 (noise 0.021) |
| reversal_k5_next | 0.568 (37) | 0.507 (580) [0.495, 0.524] | 0.471 (3038) [0.457, 0.485] | 0.479 (4761) [0.467, 0.492] | 0.469 (2771) [0.455, 0.484] | 0.525 (59) | 0.187 | flat +0.051 (noise 0.026) |
| reversal_k5_now | 0.780 (41) | 0.830 (400) [0.817, 0.839] | 0.824 (1619) [0.812, 0.835] | 0.830 (3116) [0.820, 0.840] | 0.822 (1505) [0.810, 0.833] | 0.780 (59) | 0.187 | flat +0.017 (noise 0.028) |
| reversal_k8_next | 0.402 (92) | 0.394 (703) [0.375, 0.412] | 0.386 (2799) [0.374, 0.398] | 0.390 (4804) [0.379, 0.400] | 0.384 (2698) [0.372, 0.397] | 0.477 (88) | 0.121 | flat +0.017 (noise 0.025) |
| reversal_k8_now | 0.614 (44) | 0.697 (376) [0.643, 0.740] | 0.689 (1571) [0.668, 0.709] | 0.701 (3060) [0.685, 0.717] | 0.687 (1473) [0.664, 0.709] | 0.741 (54) | 0.121 | flat +0.037 (noise 0.040) |
| overall | 0.506 (22106) | 0.506 (155050) [0.504, 0.508] | 0.504 (663295) [0.503, 0.506] | 0.503 (1302230) [0.502, 0.504] | 0.504 (618949) [0.503, 0.506] | 0.510 (18749) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08123, 0.125] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.08123, 'calls_per_day': 144.1, 'win_rate': 0.5921}, {'threshold': 0.125, 'calls_per_day': 36.3, 'win_rate': 0.6055}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 40065, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15292 | 0.337 | 0.524 (15047) | 0.579 (2057) | 0.755 (2675) |
| volatility: normal | 15292 | 0.366 | 0.531 (15219) | 0.614 (1442) | 0.750 (2257) |
| volatility: wild | 15292 | 0.381 | 0.525 (15249) | 0.630 (755) | 0.769 (2072) |
| session: Asia 00-08 | 15360 | 0.360 | 0.532 (15259) | 0.602 (1492) | 0.763 (2306) |
| session: Europe 08-13 | 9600 | 0.356 | 0.530 (9510) | 0.594 (1059) | 0.750 (1577) |
| session: US 13-21 | 15336 | 0.369 | 0.525 (15220) | 0.599 (1125) | 0.760 (2263) |
| session: late 21-24 | 5580 | 0.352 | 0.514 (5526) | 0.609 (578) | 0.749 (858) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.331 | 0.320 | 0.197 | 0.197 | 0.750 | 0.308 | 0.354 | 1.464 |
| 6h | 360 | 0.327 | 0.318 | 0.232 | 0.251 | 0.595 | 0.270 | 0.384 | 1.350 |
| 24h | 1440 | 0.334 | 0.329 | 0.244 | 0.263 | 0.551 | 0.260 | 0.409 | 1.237 |
| 7d | 10080 | 0.364 | 0.357 | 0.281 | 0.311 | 0.528 | 0.262 | 0.465 | 1.258 |
| 30d | 43200 | 0.361 | 0.353 | 0.275 | 0.304 | 0.529 | 0.260 | 0.462 | 1.278 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.331 / 0.750 / 0.867; 2: 0.229 / 0.339 / 0.917; 3: 0.287 / 0.607 / 0.817; 4: 0.243 / 0.411 / 0.833; 5: 0.293 / 0.643 / 0.833; 6: 0.296 / 0.589 / 0.817; 7: 0.251 / 0.429 / 0.883; 8: 0.288 / 0.554 / 0.833; 9: 0.273 / 0.518 / 0.867; 10: 0.275 / 0.571 / 0.867; 11: 0.243 / 0.429 / 0.917; 12: 0.258 / 0.482 / 0.950; 13: 0.292 / 0.554 / 0.983; 14: 0.281 / 0.500 / 0.983; 15: 0.274 / 0.554 / 1.000
- 6h: 1: 0.327 / 0.595 / 0.886; 2: 0.290 / 0.467 / 0.906; 3: 0.297 / 0.512 / 0.892; 4: 0.285 / 0.464 / 0.894; 5: 0.312 / 0.562 / 0.919; 6: 0.301 / 0.494 / 0.931; 7: 0.281 / 0.453 / 0.944; 8: 0.300 / 0.518 / 0.933; 9: 0.308 / 0.574 / 0.936; 10: 0.294 / 0.503 / 0.922; 11: 0.293 / 0.524 / 0.950; 12: 0.303 / 0.530 / 0.950; 13: 0.296 / 0.521 / 0.936; 14: 0.292 / 0.491 / 0.964; 15: 0.298 / 0.512 / 0.972
- 24h: 1: 0.334 / 0.551 / 0.883; 2: 0.317 / 0.492 / 0.900; 3: 0.319 / 0.499 / 0.903; 4: 0.314 / 0.498 / 0.909; 5: 0.321 / 0.527 / 0.901; 6: 0.312 / 0.490 / 0.902; 7: 0.314 / 0.490 / 0.901; 8: 0.318 / 0.523 / 0.901; 9: 0.325 / 0.539 / 0.902; 10: 0.313 / 0.490 / 0.897; 11: 0.310 / 0.490 / 0.899; 12: 0.316 / 0.498 / 0.906; 13: 0.317 / 0.509 / 0.907; 14: 0.311 / 0.477 / 0.905; 15: 0.319 / 0.512 / 0.909
- 7d: 1: 0.364 / 0.528 / 0.895; 2: 0.351 / 0.491 / 0.900; 3: 0.354 / 0.506 / 0.900; 4: 0.352 / 0.504 / 0.900; 5: 0.352 / 0.508 / 0.900; 6: 0.349 / 0.504 / 0.900; 7: 0.351 / 0.500 / 0.901; 8: 0.350 / 0.508 / 0.901; 9: 0.350 / 0.503 / 0.901; 10: 0.350 / 0.504 / 0.901; 11: 0.347 / 0.501 / 0.902; 12: 0.349 / 0.504 / 0.902; 13: 0.348 / 0.501 / 0.902; 14: 0.348 / 0.502 / 0.902; 15: 0.348 / 0.498 / 0.901
- 30d: 1: 0.361 / 0.529 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.346 / 0.498 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.502 / 0.900; 9: 0.345 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.344 / 0.497 / 0.900; 12: 0.346 / 0.504 / 0.900; 13: 0.345 / 0.501 / 0.900; 14: 0.345 / 0.500 / 0.900; 15: 0.345 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.093 (body 0.072, range 0.113); 'price stays where it was' would score 0.083; colour right 0.554; typical miss of the close 4.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.117 (body 0.091, range 0.142); 'price stays where it was' would score 0.121; colour right 0.556; typical miss of the close 4.7 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.116 (body 0.083, range 0.148); 'price stays where it was' would score 0.118; colour right 0.521; typical miss of the close 5.1 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.132; colour right 0.504; typical miss of the close 8.6 bp; chain ended on the right side 0.530 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.8 bp; chain ended on the right side 0.522 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.9; 2: 0.199 / 4.6; 3: 0.168 / 6.1; 4: 0.132 / 6.5; 5: 0.125 / 7.2; 6: 0.113 / 7.6; 7: 0.112 / 8.0; 8: 0.098 / 8.5; 9: 0.089 / 8.5; 10: 0.088 / 9.1; 11: 0.086 / 9.6; 12: 0.076 / 10.0; 13: 0.068 / 10.1; 14: 0.070 / 10.4; 15: 0.062 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 129150, probability skill vs chance 0.2259, widened contest next: False
  - now: threshold 0.8341, hit rate recent 0.935 / long run 0.942
    - 6h: 21 calls (85 a day), hit rate 0.857, chance 0.323, naive rule 0.548, lift 2.66x
    - 24h: 76 calls (76 a day), hit rate 0.921, chance 0.307, naive rule 0.519, lift 3.00x
    - 7d: 418 calls (60 a day), hit rate 0.945, chance 0.293, naive rule 0.496, lift 3.23x
    - 30d: 1739 calls (58 a day), hit rate 0.936, chance 0.294, naive rule 0.495, lift 3.18x
  - next: threshold 0.5299, hit rate recent 0.5922 / long run 0.5872
    - 6h: 38 calls (154 a day), hit rate 0.632, chance 0.323, lift 1.96x
    - 24h: 161 calls (162 a day), hit rate 0.571, chance 0.307, lift 1.86x
    - 7d: 816 calls (117 a day), hit rate 0.583, chance 0.293, lift 1.99x
    - 30d: 3001 calls (100 a day), hit rate 0.581, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 535, 0.523; 0.40: 474, 0.580; 0.45: 406, 0.651; 0.50: 355, 0.701; 0.55: 310, 0.743; 0.60: 262, 0.788; 0.65: 220, 0.814; 0.70: 173, 0.845; 0.75: 136, 0.879; 0.80: 92, 0.913; 0.85: 47, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.428; 0.35: 502, 0.464; 0.40: 406, 0.497; 0.45: 309, 0.532; 0.50: 200, 0.569; 0.55: 89, 0.571; 0.60: 13, 0.644; 0.65: 1, 0.630
- **K=5**: model 1792540800, labels learned 129148, probability skill vs chance 0.22, widened contest next: True
  - now: threshold 0.6782, hit rate recent 0.7875 / long run 0.8201
    - 6h: 18 calls (73 a day), hit rate 0.667, chance 0.194, naive rule 0.423, lift 3.44x
    - 24h: 61 calls (61 a day), hit rate 0.787, chance 0.195, naive rule 0.414, lift 4.04x
    - 7d: 409 calls (58 a day), hit rate 0.822, chance 0.187, naive rule 0.408, lift 4.40x
    - 30d: 1632 calls (54 a day), hit rate 0.822, chance 0.188, naive rule 0.404, lift 4.37x
  - next: threshold 0.4521, hit rate recent 0.5285 / long run 0.4977
    - 6h: 18 calls (73 a day), hit rate 0.556, chance 0.194, lift 2.86x
    - 24h: 68 calls (68 a day), hit rate 0.529, chance 0.195, lift 2.72x
    - 7d: 537 calls (77 a day), hit rate 0.512, chance 0.187, lift 2.74x
    - 30d: 2965 calls (99 a day), hit rate 0.470, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.493; 0.40: 278, 0.566; 0.45: 227, 0.620; 0.50: 180, 0.668; 0.55: 141, 0.707; 0.60: 108, 0.751; 0.65: 76, 0.789; 0.70: 51, 0.825; 0.75: 29, 0.870; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.388; 0.35: 255, 0.420; 0.40: 160, 0.457; 0.45: 68, 0.476; 0.50: 13, 0.494; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 129145, probability skill vs chance 0.2103, widened contest next: False
  - now: threshold 0.5644, hit rate recent 0.7256 / long run 0.6928
    - 6h: 16 calls (66 a day), hit rate 0.688, chance 0.109, naive rule 0.306, lift 6.33x
    - 24h: 58 calls (58 a day), hit rate 0.741, chance 0.127, naive rule 0.348, lift 5.86x
    - 7d: 380 calls (54 a day), hit rate 0.700, chance 0.122, naive rule 0.343, lift 5.72x
    - 30d: 1586 calls (53 a day), hit rate 0.690, chance 0.121, naive rule 0.333, lift 5.70x
  - next: threshold 0.3596, hit rate recent 0.4804 / long run 0.4041
    - 6h: 15 calls (62 a day), hit rate 0.667, chance 0.109, lift 6.14x
    - 24h: 100 calls (101 a day), hit rate 0.470, chance 0.127, lift 3.71x
    - 7d: 721 calls (103 a day), hit rate 0.406, chance 0.122, lift 3.32x
    - 30d: 2840 calls (95 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 189, 0.500; 0.40: 147, 0.547; 0.45: 113, 0.595; 0.50: 84, 0.638; 0.55: 61, 0.678; 0.60: 41, 0.714; 0.65: 24, 0.784; 0.70: 11, 0.812; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.357; 0.35: 92, 0.385; 0.40: 29, 0.406; 0.45: 6, 0.429; 0.50: 1, 0.630
- **K=13**: model 1793059200, labels learned 129140, probability skill vs chance 0.1923, widened contest next: False
  - now: threshold 0.4125, hit rate recent 0.6055 / long run 0.568
    - 6h: 16 calls (67 a day), hit rate 0.562, chance 0.101, naive rule 0.346, lift 5.54x
    - 24h: 64 calls (65 a day), hit rate 0.656, chance 0.086, naive rule 0.309, lift 7.60x
    - 7d: 431 calls (62 a day), hit rate 0.575, chance 0.079, naive rule 0.288, lift 7.33x
    - 30d: 1662 calls (55 a day), hit rate 0.568, chance 0.078, naive rule 0.279, lift 7.32x
  - next: threshold 0.2935, hit rate recent 0.366 / long run 0.3204
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.101, lift 6.07x
    - 24h: 56 calls (57 a day), hit rate 0.393, chance 0.086, lift 4.55x
    - 7d: 393 calls (56 a day), hit rate 0.338, chance 0.079, lift 4.31x
    - 30d: 1965 calls (66 a day), hit rate 0.317, chance 0.078, lift 4.09x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 127, 0.443; 0.35: 91, 0.496; 0.40: 64, 0.551; 0.45: 43, 0.597; 0.50: 29, 0.652; 0.55: 18, 0.693; 0.60: 9, 0.735; 0.65: 2, 0.730; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.325; 0.35: 14, 0.353; 0.40: 3, 0.451; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.392 | 3.15% | 0.883 | 0.517 | 0.245 | 0.625 | 0.158 |
| 6h | 7.027 | 4.93% | 0.900 | 0.503 | 0.249 | 0.538 | 0.409 |
| 24h | 8.149 | 13.70% | 0.899 | 0.515 | 0.249 | 0.537 | 0.457 |
| 7d | 15.828 | 4.98% | 0.899 | 0.501 | 0.250 | 0.503 | 0.744 |
| 30d | 14.084 | 4.47% | 0.900 | 0.500 | 0.251 | 0.497 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.600 | 6.465 | 6.613 | 6.447 | 6.875 | 7.051 | 6.385 | 6.389 | 6.399 | 6.392 |
| 6h | 7.392 | 7.114 | 7.227 | 7.062 | 7.361 | 7.574 | 7.017 | 7.039 | 7.029 | 7.027 |
| 24h | 9.442 | 8.206 | 8.371 | 8.190 | 8.401 | 8.557 | 8.140 | 8.129 | 8.142 | 8.149 |
| 7d | 16.657 | 16.011 | 15.955 | 15.861 | 16.162 | 16.106 | 15.811 | 15.789 | 15.799 | 15.828 |
| 30d | 14.743 | 14.235 | 14.180 | 14.112 | 14.351 | 14.294 | 14.079 | 14.056 | 14.058 | 14.084 |

## Next candle

- candle starting 2026-10-31 20:36 UTC, last close 2249.36
- P(up) 0.5231, return quantiles (bp): {'05': -3.92, '10': -2.924, '25': -1.11, '40': -0.219, '50': 0.063, '60': 0.545, '75': 1.405, '90': 2.791, '95': 3.861}
- changepoint probability 0.0305, regime age 166.9 min
- agent weights: empirical 0.003, ewma 0.140, garch 0.046, har 0.176, bocpd 0.023, hmm 0.006, online_qr 0.306, lgbm 0.300

## Learning log

- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- HMM volatility states (sd, bp per minute): [3.53, 7.0, 20.69], current probabilities: [0.966, 0.033, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-31 20:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.423, 'l_abs': 0.557, 'l_hi': 0.682, 'l_lo': 0.691, 'b05': 0.625, 'b25': 0.58, 'b75': 0.569, 'b95': 0.621}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.359, 1.667, 2.008, 2.119, 2.372, 2.37, 2.696, 2.865, 3.278, 3.244, 3.198, 3.269, 3.399, 3.669]}
- calibration offsets (in sigma): {'05': 0.0175, '10': -0.005, '25': 0.0875, '40': 0.07, '50': -0.005, '60': -0.02, '75': -0.0275, '90': -0.065, '95': -0.0375}
