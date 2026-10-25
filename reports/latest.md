# ETH-USD 60s candle generator - report

- generated: 2026-10-25 06:59 UTC
- last closed candle: 2026-10-25 06:58 UTC (staleness 1.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.543 (672) [0.509, 0.577] | 0.517 (2876) [0.498, 0.536] | 0.515 (5082) [0.500, 0.528] | 0.519 (2110) [0.495, 0.543] | 0.667 (27) | 0.500 | flat +0.040 (noise 0.027) |
| colour_clear | 0.544 (743) | 0.553 (5669) [0.547, 0.562] | 0.533 (23412) [0.525, 0.541] | 0.517 (41491) [0.511, 0.524] | 0.547 (17253) [0.542, 0.552] | 0.522 (230) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.606 (269) | 0.608 (1282) [0.589, 0.628] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.533 (90) | 0.500 | flat +0.016 (noise 0.023) |
| colour_next | 0.522 (1431) | 0.534 (10039) [0.527, 0.541] | 0.523 (42853) [0.517, 0.528] | 0.513 (75756) [0.508, 0.517] | 0.530 (31407) [0.525, 0.534] | 0.494 (417) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.501 (140546) [0.498, 0.503] | 0.501 (599942) [0.499, 0.502] | 0.501 (1060584) [0.500, 0.501] | 0.500 (439698) [0.498, 0.502] | 0.503 (5838) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.602 (98) | 0.636 (335) [0.607, 0.672] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.605 (38) | 0.500 | flat -0.005 (noise 0.045) |
| reversal_k13_next | 0.286 (63) | 0.310 (481) [0.291, 0.327] | 0.305 (2173) [0.292, 0.317] | 0.306 (3618) [0.296, 0.318] | 0.316 (1513) [0.305, 0.327] | 0.333 (21) | 0.077 | flat +0.004 (noise 0.031) |
| reversal_k13_now | 0.647 (51) | 0.530 (366) [0.490, 0.576] | 0.570 (1560) [0.549, 0.591] | 0.573 (2651) [0.557, 0.590] | 0.564 (1179) [0.540, 0.590] | 0.529 (17) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.630 (54) | 0.592 (699) [0.564, 0.624] | 0.580 (2792) [0.566, 0.594] | 0.584 (4562) [0.573, 0.594] | 0.580 (2122) [0.565, 0.596] | 0.750 (16) | 0.293 | flat +0.024 (noise 0.026) |
| reversal_k3_now | 0.980 (49) | 0.945 (397) [0.928, 0.962] | 0.938 (1690) [0.929, 0.947] | 0.938 (3023) [0.932, 0.945] | 0.933 (1260) [0.923, 0.944] | 0.933 (15) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.480 (125) | 0.460 (939) [0.433, 0.486] | 0.464 (2842) [0.449, 0.479] | 0.476 (4306) [0.463, 0.489] | 0.460 (2316) [0.445, 0.476] | 0.535 (43) | 0.187 | flat -0.006 (noise 0.025) |
| reversal_k5_now | 0.818 (55) | 0.812 (361) [0.800, 0.823] | 0.831 (1561) [0.818, 0.844] | 0.830 (2771) [0.819, 0.841] | 0.819 (1160) [0.804, 0.833] | 0.857 (14) | 0.187 | flat -0.006 (noise 0.029) |
| reversal_k8_next | 0.384 (86) | 0.377 (757) [0.359, 0.394] | 0.383 (2519) [0.370, 0.396] | 0.389 (4187) [0.377, 0.400] | 0.381 (2081) [0.367, 0.395] | 0.368 (38) | 0.120 | flat +0.004 (noise 0.026) |
| reversal_k8_now | 0.709 (55) | 0.654 (332) [0.613, 0.693] | 0.701 (1523) [0.681, 0.722] | 0.702 (2739) [0.686, 0.718] | 0.685 (1152) [0.662, 0.708] | 0.733 (15) | 0.121 | flat -0.031 (noise 0.036) |
| overall | 0.505 (22099) | 0.504 (155589) [0.501, 0.507] | 0.504 (662331) [0.502, 0.505] | 0.503 (1169279) [0.502, 0.504] | 0.504 (485998) [0.502, 0.506] | 0.505 (6461) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07441, 0.1098] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5333, 'levels': [{'threshold': 0.07441, 'calls_per_day': 150.2, 'win_rate': 0.6047}, {'threshold': 0.1098, 'calls_per_day': 38.7, 'win_rate': 0.6507}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 30685, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15020 | 0.336 | 0.524 (14774) | 0.587 (1706) | 0.763 (2482) |
| volatility: normal | 15019 | 0.364 | 0.521 (14950) | 0.615 (1079) | 0.756 (2212) |
| volatility: wild | 15019 | 0.378 | 0.518 (14982) | 0.628 (498) | 0.772 (1902) |
| session: Asia 00-08 | 15298 | 0.357 | 0.526 (15195) | 0.607 (1210) | 0.767 (2203) |
| session: Europe 08-13 | 9300 | 0.355 | 0.523 (9214) | 0.597 (780) | 0.763 (1483) |
| session: US 13-21 | 14880 | 0.368 | 0.518 (14780) | 0.597 (798) | 0.770 (2096) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5517) | 0.610 (495) | 0.737 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.340 | 0.353 | 0.236 | 0.236 | 0.517 | 0.254 | 0.427 | 1.156 |
| 6h | 360 | 0.344 | 0.335 | 0.256 | 0.290 | 0.515 | 0.264 | 0.424 | 1.090 |
| 24h | 1440 | 0.359 | 0.349 | 0.271 | 0.300 | 0.516 | 0.267 | 0.451 | 1.222 |
| 7d | 10080 | 0.371 | 0.361 | 0.274 | 0.307 | 0.533 | 0.268 | 0.473 | 1.211 |
| 30d | 43200 | 0.360 | 0.353 | 0.277 | 0.305 | 0.523 | 0.256 | 0.463 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.340 / 0.517 / 0.883; 2: 0.328 / 0.500 / 0.867; 3: 0.316 / 0.467 / 0.867; 4: 0.361 / 0.517 / 0.850; 5: 0.327 / 0.400 / 0.817; 6: 0.360 / 0.583 / 0.900; 7: 0.340 / 0.483 / 0.900; 8: 0.336 / 0.500 / 0.917; 9: 0.358 / 0.550 / 0.917; 10: 0.306 / 0.383 / 0.883; 11: 0.323 / 0.433 / 0.900; 12: 0.347 / 0.517 / 0.900; 13: 0.301 / 0.367 / 0.917; 14: 0.334 / 0.533 / 0.917; 15: 0.318 / 0.450 / 0.933
- 6h: 1: 0.344 / 0.515 / 0.872; 2: 0.334 / 0.526 / 0.889; 3: 0.329 / 0.490 / 0.883; 4: 0.346 / 0.557 / 0.856; 5: 0.333 / 0.487 / 0.856; 6: 0.337 / 0.526 / 0.864; 7: 0.336 / 0.524 / 0.856; 8: 0.333 / 0.493 / 0.875; 9: 0.334 / 0.487 / 0.878; 10: 0.319 / 0.460 / 0.861; 11: 0.325 / 0.485 / 0.881; 12: 0.346 / 0.554 / 0.886; 13: 0.320 / 0.457 / 0.892; 14: 0.328 / 0.507 / 0.897; 15: 0.325 / 0.479 / 0.892
- 24h: 1: 0.359 / 0.516 / 0.899; 2: 0.343 / 0.495 / 0.897; 3: 0.345 / 0.507 / 0.892; 4: 0.342 / 0.495 / 0.885; 5: 0.344 / 0.513 / 0.889; 6: 0.337 / 0.493 / 0.889; 7: 0.344 / 0.511 / 0.887; 8: 0.342 / 0.502 / 0.887; 9: 0.339 / 0.491 / 0.885; 10: 0.340 / 0.502 / 0.881; 11: 0.338 / 0.496 / 0.880; 12: 0.347 / 0.521 / 0.878; 13: 0.341 / 0.502 / 0.876; 14: 0.339 / 0.503 / 0.880; 15: 0.338 / 0.501 / 0.881
- 7d: 1: 0.371 / 0.533 / 0.899; 2: 0.359 / 0.503 / 0.899; 3: 0.359 / 0.509 / 0.899; 4: 0.354 / 0.494 / 0.898; 5: 0.354 / 0.500 / 0.899; 6: 0.353 / 0.495 / 0.899; 7: 0.352 / 0.495 / 0.899; 8: 0.355 / 0.509 / 0.899; 9: 0.353 / 0.499 / 0.899; 10: 0.353 / 0.506 / 0.898; 11: 0.351 / 0.499 / 0.898; 12: 0.354 / 0.506 / 0.898; 13: 0.350 / 0.495 / 0.899; 14: 0.352 / 0.500 / 0.898; 15: 0.351 / 0.502 / 0.899
- 30d: 1: 0.360 / 0.523 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.498 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.344 / 0.498 / 0.900; 12: 0.346 / 0.503 / 0.900; 13: 0.345 / 0.502 / 0.899; 14: 0.344 / 0.498 / 0.899; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.127 (body 0.088, range 0.166); 'price stays where it was' would score 0.203; colour right 0.517; typical miss of the close 8.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.095, range 0.163); 'price stays where it was' would score 0.144; colour right 0.507; typical miss of the close 4.6 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.122 (body 0.085, range 0.160); 'price stays where it was' would score 0.140; colour right 0.483; typical miss of the close 7.1 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.168); 'price stays where it was' would score 0.134; colour right 0.504; typical miss of the close 8.9 bp; chain ended on the right side 0.545 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.5 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.196 / 4.4; 3: 0.167 / 5.7; 4: 0.131 / 6.4; 5: 0.123 / 7.1; 6: 0.110 / 7.6; 7: 0.105 / 7.9; 8: 0.096 / 8.2; 9: 0.087 / 8.2; 10: 0.087 / 8.9; 11: 0.084 / 9.4; 12: 0.077 / 9.7; 13: 0.068 / 9.9; 14: 0.068 / 10.3; 15: 0.059 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 119692, probability skill vs chance 0.2301, widened contest next: False
  - now: threshold 0.8351, hit rate recent 0.9571 / long run 0.939
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.294, naive rule 0.520, lift 3.09x
    - 24h: 46 calls (46 a day), hit rate 0.957, chance 0.311, naive rule 0.540, lift 3.08x
    - 7d: 392 calls (56 a day), hit rate 0.941, chance 0.297, naive rule 0.501, lift 3.17x
    - 30d: 1688 calls (56 a day), hit rate 0.937, chance 0.294, naive rule 0.491, lift 3.19x
  - next: threshold 0.5568, hit rate recent 0.649 / long run 0.5953
    - 6h: 15 calls (61 a day), hit rate 0.733, chance 0.294, lift 2.50x
    - 24h: 50 calls (50 a day), hit rate 0.680, chance 0.311, lift 2.19x
    - 7d: 691 calls (99 a day), hit rate 0.599, chance 0.297, lift 2.02x
    - 30d: 2792 calls (93 a day), hit rate 0.581, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.494; 0.35: 539, 0.519; 0.40: 479, 0.575; 0.45: 409, 0.645; 0.50: 357, 0.698; 0.55: 312, 0.740; 0.60: 264, 0.784; 0.65: 221, 0.809; 0.70: 175, 0.841; 0.75: 136, 0.875; 0.80: 91, 0.914; 0.85: 47, 0.952; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.426; 0.35: 501, 0.464; 0.40: 407, 0.498; 0.45: 310, 0.532; 0.50: 202, 0.566; 0.55: 91, 0.574; 0.60: 14, 0.611; 0.65: 1, 0.697
- **K=5**: model 1792540800, labels learned 119690, probability skill vs chance 0.22, widened contest next: False
  - now: threshold 0.6744, hit rate recent 0.8088 / long run 0.8205
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.190, naive rule 0.433, lift 4.38x
    - 24h: 53 calls (53 a day), hit rate 0.792, chance 0.181, naive rule 0.438, lift 4.37x
    - 7d: 362 calls (52 a day), hit rate 0.809, chance 0.185, naive rule 0.406, lift 4.37x
    - 30d: 1558 calls (52 a day), hit rate 0.832, chance 0.188, naive rule 0.400, lift 4.43x
  - next: threshold 0.4196, hit rate recent 0.5012 / long run 0.4745
    - 6h: 38 calls (155 a day), hit rate 0.526, chance 0.190, lift 2.77x
    - 24h: 133 calls (134 a day), hit rate 0.526, chance 0.181, lift 2.90x
    - 7d: 939 calls (134 a day), hit rate 0.466, chance 0.185, lift 2.52x
    - 30d: 2880 calls (96 a day), hit rate 0.464, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 343, 0.495; 0.40: 276, 0.566; 0.45: 223, 0.622; 0.50: 175, 0.673; 0.55: 135, 0.712; 0.60: 104, 0.756; 0.65: 76, 0.793; 0.70: 53, 0.833; 0.75: 31, 0.877; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.390; 0.35: 252, 0.421; 0.40: 158, 0.451; 0.45: 70, 0.463; 0.50: 15, 0.489; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 119687, probability skill vs chance 0.2001, widened contest next: False
  - now: threshold 0.5571, hit rate recent 0.6788 / long run 0.6831
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.106, naive rule 0.308, lift 6.53x
    - 24h: 57 calls (57 a day), hit rate 0.667, chance 0.118, naive rule 0.364, lift 5.64x
    - 7d: 336 calls (48 a day), hit rate 0.655, chance 0.116, naive rule 0.323, lift 5.63x
    - 30d: 1526 calls (51 a day), hit rate 0.701, chance 0.121, naive rule 0.330, lift 5.79x
  - next: threshold 0.338, hit rate recent 0.3813 / long run 0.3779
    - 6h: 32 calls (132 a day), hit rate 0.344, chance 0.106, lift 3.24x
    - 24h: 101 calls (102 a day), hit rate 0.416, chance 0.118, lift 3.52x
    - 7d: 765 calls (109 a day), hit rate 0.375, chance 0.116, lift 3.22x
    - 30d: 2545 calls (85 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 249, 0.426; 0.35: 189, 0.496; 0.40: 144, 0.551; 0.45: 111, 0.596; 0.50: 84, 0.638; 0.55: 62, 0.677; 0.60: 41, 0.724; 0.65: 23, 0.790; 0.70: 10, 0.833; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.351; 0.35: 98, 0.378; 0.40: 36, 0.399; 0.45: 8, 0.436; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 119682, probability skill vs chance 0.1775, widened contest next: False
  - now: threshold 0.4113, hit rate recent 0.572 / long run 0.5573
    - 6h: 15 calls (63 a day), hit rate 0.533, chance 0.052, naive rule 0.179, lift 10.19x
    - 24h: 53 calls (54 a day), hit rate 0.566, chance 0.069, naive rule 0.275, lift 8.22x
    - 7d: 365 calls (52 a day), hit rate 0.532, chance 0.074, naive rule 0.269, lift 7.21x
    - 30d: 1566 calls (52 a day), hit rate 0.568, chance 0.077, naive rule 0.273, lift 7.35x
  - next: threshold 0.2933, hit rate recent 0.3069 / long run 0.3088
    - 6h: 17 calls (71 a day), hit rate 0.294, chance 0.052, lift 5.62x
    - 24h: 71 calls (72 a day), hit rate 0.338, chance 0.069, lift 4.91x
    - 7d: 482 calls (69 a day), hit rate 0.307, chance 0.074, lift 4.16x
    - 30d: 2173 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.446; 0.35: 87, 0.497; 0.40: 61, 0.552; 0.45: 41, 0.605; 0.50: 26, 0.658; 0.55: 15, 0.702; 0.60: 6, 0.753; 0.65: 2, 0.837
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.316; 0.35: 14, 0.351; 0.40: 2, 0.418; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.201 | -0.52% | 0.867 | 0.467 | 0.250 | 0.533 | 0.396 |
| 6h | 9.001 | 3.83% | 0.881 | 0.478 | 0.251 | 0.504 | 0.567 |
| 24h | 13.016 | 5.13% | 0.895 | 0.496 | 0.251 | 0.498 | 0.707 |
| 7d | 15.112 | 3.37% | 0.901 | 0.500 | 0.250 | 0.501 | 0.647 |
| 30d | 13.388 | 4.22% | 0.900 | 0.500 | 0.251 | 0.496 | 0.672 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.127 | 14.165 | 14.238 | 14.296 | 14.336 | 14.307 | 14.283 | 14.198 | 14.204 | 14.201 |
| 6h | 9.359 | 9.046 | 9.047 | 9.050 | 9.081 | 9.372 | 9.017 | 8.964 | 8.975 | 9.001 |
| 24h | 13.720 | 13.218 | 13.067 | 13.096 | 13.239 | 13.201 | 13.049 | 12.958 | 12.998 | 13.016 |
| 7d | 15.639 | 15.259 | 15.190 | 15.130 | 15.378 | 15.261 | 15.101 | 15.077 | 15.085 | 15.112 |
| 30d | 13.977 | 13.515 | 13.471 | 13.410 | 13.630 | 13.580 | 13.384 | 13.365 | 13.363 | 13.388 |

## Next candle

- candle starting 2026-10-25 06:58 UTC, last close 2337.91
- P(up) 0.4838, return quantiles (bp): {'05': -8.667, '10': -6.561, '25': -3.518, '40': -1.75, '50': -0.217, '60': 1.142, '75': 3.063, '90': 5.989, '95': 7.851}
- changepoint probability 0.0539, regime age 74.5 min
- agent weights: empirical 0.005, ewma 0.076, garch 0.155, har 0.135, bocpd 0.060, hmm 0.023, online_qr 0.197, lgbm 0.349

## Learning log

- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.96, 7.08, 20.11], current probabilities: [0.345, 0.647, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-10-25 07:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.492, 'l_abs': 0.675, 'l_hi': 0.763, 'l_lo': 0.767, 'b05': 0.717, 'b25': 0.692, 'b75': 0.621, 'b95': 0.683}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.588, 2.069, 2.7, 2.906, 3.064, 3.522, 3.553, 3.93, 4.587, 4.725, 4.847, 5.055, 5.051, 5.238]}
- calibration offsets (in sigma): {'05': 0.0385, '10': 0.017, '25': -0.0275, '40': -0.082, '50': -0.035, '60': -0.028, '75': -0.0525, '90': -0.077, '95': -0.0785}
