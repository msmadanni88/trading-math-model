# ETH-USD 60s candle generator - report

- generated: 2026-10-25 01:47 UTC
- last closed candle: 2026-10-25 01:47 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.543 (672) [0.509, 0.577] | 0.517 (2876) [0.498, 0.536] | 0.515 (5082) [0.500, 0.528] | 0.519 (2110) [0.495, 0.543] | 0.857 (7) | 0.500 | flat +0.040 (noise 0.027) |
| colour_clear | 0.544 (743) | 0.553 (5669) [0.547, 0.562] | 0.533 (23412) [0.525, 0.541] | 0.517 (41491) [0.511, 0.524] | 0.547 (17253) [0.542, 0.552] | 0.444 (45) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.606 (269) | 0.608 (1282) [0.589, 0.628] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.333 (18) | 0.500 | flat +0.016 (noise 0.023) |
| colour_next | 0.522 (1431) | 0.534 (10039) [0.527, 0.541] | 0.523 (42853) [0.517, 0.528] | 0.513 (75756) [0.508, 0.517] | 0.530 (31407) [0.525, 0.534] | 0.411 (107) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.501 (140546) [0.498, 0.503] | 0.501 (599942) [0.499, 0.502] | 0.501 (1060584) [0.500, 0.501] | 0.500 (439698) [0.498, 0.502] | 0.514 (1498) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.602 (98) | 0.636 (335) [0.607, 0.672] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.500 (10) | 0.500 | flat -0.005 (noise 0.045) |
| reversal_k13_next | 0.286 (63) | 0.310 (481) [0.291, 0.327] | 0.305 (2173) [0.292, 0.317] | 0.306 (3618) [0.296, 0.318] | 0.316 (1513) [0.305, 0.327] | 0.500 (4) | 0.077 | flat +0.004 (noise 0.031) |
| reversal_k13_now | 0.647 (51) | 0.530 (366) [0.490, 0.576] | 0.570 (1560) [0.549, 0.591] | 0.573 (2651) [0.557, 0.590] | 0.564 (1179) [0.540, 0.590] | 0.500 (2) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.630 (54) | 0.592 (699) [0.564, 0.624] | 0.580 (2792) [0.566, 0.594] | 0.584 (4562) [0.573, 0.594] | 0.580 (2122) [0.565, 0.596] | 1.000 (2) | 0.293 | flat +0.024 (noise 0.026) |
| reversal_k3_now | 0.980 (49) | 0.945 (397) [0.928, 0.962] | 0.938 (1690) [0.929, 0.947] | 0.938 (3023) [0.932, 0.945] | 0.933 (1260) [0.923, 0.944] | 1.000 (5) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.480 (125) | 0.460 (939) [0.433, 0.486] | 0.464 (2842) [0.449, 0.479] | 0.476 (4306) [0.463, 0.489] | 0.460 (2316) [0.445, 0.476] | 0.700 (10) | 0.187 | flat -0.006 (noise 0.025) |
| reversal_k5_now | 0.818 (55) | 0.812 (361) [0.800, 0.823] | 0.831 (1561) [0.818, 0.844] | 0.830 (2771) [0.819, 0.841] | 0.819 (1160) [0.804, 0.833] | 1.000 (4) | 0.187 | flat -0.006 (noise 0.029) |
| reversal_k8_next | 0.384 (86) | 0.377 (757) [0.359, 0.394] | 0.383 (2519) [0.370, 0.396] | 0.389 (4187) [0.377, 0.400] | 0.381 (2081) [0.367, 0.395] | 0.500 (8) | 0.120 | flat +0.004 (noise 0.026) |
| reversal_k8_now | 0.709 (55) | 0.654 (332) [0.613, 0.693] | 0.701 (1523) [0.681, 0.722] | 0.702 (2739) [0.686, 0.718] | 0.685 (1152) [0.662, 0.708] | 1.000 (2) | 0.121 | flat -0.031 (noise 0.036) |
| overall | 0.505 (22099) | 0.504 (155589) [0.501, 0.507] | 0.504 (662331) [0.502, 0.505] | 0.503 (1169279) [0.502, 0.504] | 0.504 (485998) [0.502, 0.506] | 0.514 (1649) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07348, 0.1081] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5343, 'levels': [{'threshold': 0.07348, 'calls_per_day': 148.5, 'win_rate': 0.6044}, {'threshold': 0.1081, 'calls_per_day': 37.7, 'win_rate': 0.6491}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 30376, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14916 | 0.336 | 0.524 (14669) | 0.587 (1659) | 0.764 (2470) |
| volatility: normal | 14915 | 0.364 | 0.521 (14848) | 0.617 (1056) | 0.755 (2192) |
| volatility: wild | 14916 | 0.378 | 0.518 (14879) | 0.627 (496) | 0.773 (1886) |
| session: Asia 00-08 | 14987 | 0.357 | 0.526 (14885) | 0.608 (1138) | 0.768 (2155) |
| session: Europe 08-13 | 9300 | 0.355 | 0.523 (9214) | 0.597 (780) | 0.763 (1483) |
| session: US 13-21 | 14880 | 0.368 | 0.518 (14780) | 0.597 (798) | 0.770 (2096) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5517) | 0.610 (495) | 0.737 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.322 | 0.321 | 0.248 | 0.248 | 0.483 | 0.239 | 0.405 | 1.579 |
| 6h | 360 | 0.337 | 0.345 | 0.276 | 0.287 | 0.458 | 0.235 | 0.439 | 1.375 |
| 24h | 1440 | 0.356 | 0.348 | 0.273 | 0.302 | 0.512 | 0.260 | 0.452 | 1.236 |
| 7d | 10080 | 0.371 | 0.361 | 0.275 | 0.307 | 0.533 | 0.268 | 0.473 | 1.205 |
| 30d | 43200 | 0.360 | 0.353 | 0.277 | 0.305 | 0.522 | 0.256 | 0.463 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.322 / 0.483 / 0.900; 2: 0.332 / 0.500 / 0.867; 3: 0.327 / 0.483 / 0.900; 4: 0.335 / 0.600 / 0.933; 5: 0.323 / 0.550 / 0.917; 6: 0.311 / 0.450 / 0.917; 7: 0.370 / 0.600 / 0.933; 8: 0.318 / 0.467 / 0.917; 9: 0.349 / 0.533 / 0.917; 10: 0.307 / 0.450 / 0.967; 11: 0.328 / 0.517 / 0.983; 12: 0.347 / 0.600 / 0.983; 13: 0.301 / 0.467 / 1.000; 14: 0.325 / 0.500 / 1.000; 15: 0.313 / 0.450 / 1.000
- 6h: 1: 0.337 / 0.458 / 0.911; 2: 0.338 / 0.503 / 0.889; 3: 0.335 / 0.492 / 0.886; 4: 0.338 / 0.514 / 0.903; 5: 0.334 / 0.536 / 0.914; 6: 0.327 / 0.503 / 0.906; 7: 0.341 / 0.522 / 0.906; 8: 0.336 / 0.511 / 0.897; 9: 0.337 / 0.497 / 0.908; 10: 0.337 / 0.522 / 0.917; 11: 0.337 / 0.531 / 0.917; 12: 0.349 / 0.550 / 0.908; 13: 0.343 / 0.517 / 0.903; 14: 0.345 / 0.534 / 0.908; 15: 0.337 / 0.514 / 0.911
- 24h: 1: 0.356 / 0.512 / 0.908; 2: 0.343 / 0.486 / 0.900; 3: 0.348 / 0.515 / 0.901; 4: 0.338 / 0.479 / 0.903; 5: 0.342 / 0.514 / 0.908; 6: 0.334 / 0.483 / 0.906; 7: 0.342 / 0.506 / 0.910; 8: 0.342 / 0.506 / 0.908; 9: 0.339 / 0.497 / 0.906; 10: 0.341 / 0.504 / 0.906; 11: 0.341 / 0.509 / 0.904; 12: 0.346 / 0.512 / 0.903; 13: 0.343 / 0.519 / 0.903; 14: 0.340 / 0.505 / 0.903; 15: 0.344 / 0.524 / 0.907
- 7d: 1: 0.371 / 0.533 / 0.900; 2: 0.359 / 0.501 / 0.900; 3: 0.359 / 0.509 / 0.900; 4: 0.354 / 0.492 / 0.901; 5: 0.354 / 0.499 / 0.901; 6: 0.353 / 0.494 / 0.900; 7: 0.353 / 0.495 / 0.900; 8: 0.356 / 0.510 / 0.900; 9: 0.353 / 0.499 / 0.899; 10: 0.354 / 0.507 / 0.899; 11: 0.351 / 0.500 / 0.899; 12: 0.353 / 0.504 / 0.899; 13: 0.351 / 0.496 / 0.898; 14: 0.352 / 0.499 / 0.898; 15: 0.351 / 0.504 / 0.899
- 30d: 1: 0.360 / 0.522 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.502 / 0.900; 9: 0.345 / 0.497 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.499 / 0.900; 12: 0.346 / 0.503 / 0.900; 13: 0.346 / 0.503 / 0.900; 14: 0.344 / 0.498 / 0.900; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.094 (body 0.063, range 0.125); 'price stays where it was' would score 0.141; colour right 0.500; typical miss of the close 4.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.110 (body 0.074, range 0.146); 'price stays where it was' would score 0.122; colour right 0.492; typical miss of the close 5.8 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.121 (body 0.084, range 0.158); 'price stays where it was' would score 0.144; colour right 0.488; typical miss of the close 7.0 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.127 (body 0.087, range 0.167); 'price stays where it was' would score 0.133; colour right 0.504; typical miss of the close 9.0 bp; chain ended on the right side 0.545 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.5 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.196 / 4.4; 3: 0.168 / 5.8; 4: 0.130 / 6.4; 5: 0.122 / 7.1; 6: 0.110 / 7.6; 7: 0.105 / 7.9; 8: 0.097 / 8.2; 9: 0.087 / 8.2; 10: 0.087 / 8.9; 11: 0.084 / 9.4; 12: 0.077 / 9.7; 13: 0.068 / 9.9; 14: 0.068 / 10.3; 15: 0.059 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 119381, probability skill vs chance 0.228, widened contest next: False
  - now: threshold 0.8354, hit rate recent 0.9671 / long run 0.9397
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.289, naive rule 0.522, lift 3.46x
    - 24h: 50 calls (50 a day), hit rate 0.980, chance 0.309, naive rule 0.534, lift 3.17x
    - 7d: 396 calls (57 a day), hit rate 0.944, chance 0.296, naive rule 0.499, lift 3.19x
    - 30d: 1687 calls (56 a day), hit rate 0.938, chance 0.294, naive rule 0.491, lift 3.19x
  - next: threshold 0.5696, hit rate recent 0.6328 / long run 0.5925
    - 6h: 8 calls (32 a day), hit rate 0.500, chance 0.289, lift 1.73x
    - 24h: 52 calls (52 a day), hit rate 0.654, chance 0.309, lift 2.12x
    - 7d: 699 calls (100 a day), hit rate 0.594, chance 0.296, lift 2.01x
    - 30d: 2791 calls (93 a day), hit rate 0.579, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.494; 0.35: 539, 0.518; 0.40: 479, 0.574; 0.45: 409, 0.645; 0.50: 357, 0.698; 0.55: 312, 0.740; 0.60: 264, 0.784; 0.65: 221, 0.809; 0.70: 175, 0.841; 0.75: 136, 0.875; 0.80: 91, 0.914; 0.85: 47, 0.953; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.426; 0.35: 500, 0.464; 0.40: 407, 0.499; 0.45: 310, 0.533; 0.50: 202, 0.566; 0.55: 91, 0.573; 0.60: 14, 0.614; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 119379, probability skill vs chance 0.2225, widened contest next: False
  - now: threshold 0.6749, hit rate recent 0.811 / long run 0.8209
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.183, naive rule 0.427, lift 4.10x
    - 24h: 56 calls (56 a day), hit rate 0.821, chance 0.180, naive rule 0.430, lift 4.56x
    - 7d: 361 calls (52 a day), hit rate 0.812, chance 0.185, naive rule 0.403, lift 4.39x
    - 30d: 1557 calls (52 a day), hit rate 0.832, chance 0.188, naive rule 0.400, lift 4.43x
  - next: threshold 0.4194, hit rate recent 0.5226 / long run 0.474
    - 6h: 36 calls (147 a day), hit rate 0.500, chance 0.183, lift 2.74x
    - 24h: 123 calls (124 a day), hit rate 0.512, chance 0.180, lift 2.84x
    - 7d: 944 calls (135 a day), hit rate 0.461, chance 0.185, lift 2.49x
    - 30d: 2851 calls (95 a day), hit rate 0.465, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.427; 0.35: 343, 0.495; 0.40: 276, 0.567; 0.45: 223, 0.623; 0.50: 175, 0.673; 0.55: 135, 0.713; 0.60: 104, 0.756; 0.65: 76, 0.793; 0.70: 53, 0.833; 0.75: 31, 0.877; 0.80: 10, 0.907
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.390; 0.35: 252, 0.422; 0.40: 157, 0.451; 0.45: 70, 0.463; 0.50: 15, 0.491; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 119376, probability skill vs chance 0.2052, widened contest next: False
  - now: threshold 0.5585, hit rate recent 0.6758 / long run 0.6829
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.120, naive rule 0.380, lift 6.48x
    - 24h: 54 calls (54 a day), hit rate 0.722, chance 0.124, naive rule 0.364, lift 5.83x
    - 7d: 331 calls (47 a day), hit rate 0.653, chance 0.116, naive rule 0.318, lift 5.64x
    - 30d: 1520 calls (51 a day), hit rate 0.701, chance 0.121, naive rule 0.330, lift 5.79x
  - next: threshold 0.3397, hit rate recent 0.4192 / long run 0.3803
    - 6h: 26 calls (107 a day), hit rate 0.462, chance 0.120, lift 3.85x
    - 24h: 83 calls (84 a day), hit rate 0.410, chance 0.124, lift 3.31x
    - 7d: 760 calls (109 a day), hit rate 0.375, chance 0.116, lift 3.24x
    - 30d: 2524 calls (84 a day), hit rate 0.384, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 249, 0.427; 0.35: 189, 0.497; 0.40: 144, 0.552; 0.45: 111, 0.597; 0.50: 84, 0.638; 0.55: 61, 0.677; 0.60: 41, 0.724; 0.65: 23, 0.793; 0.70: 10, 0.839; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.352; 0.35: 98, 0.379; 0.40: 36, 0.400; 0.45: 8, 0.435; 0.50: 1, 0.567
- **K=13**: model 1792800000, labels learned 119371, probability skill vs chance 0.1858, widened contest next: False
  - now: threshold 0.4197, hit rate recent 0.5814 / long run 0.5579
    - 6h: 9 calls (38 a day), hit rate 0.778, chance 0.083, naive rule 0.356, lift 9.42x
    - 24h: 50 calls (51 a day), hit rate 0.640, chance 0.074, naive rule 0.293, lift 8.64x
    - 7d: 363 calls (52 a day), hit rate 0.529, chance 0.074, naive rule 0.268, lift 7.15x
    - 30d: 1558 calls (52 a day), hit rate 0.569, chance 0.077, naive rule 0.274, lift 7.35x
  - next: threshold 0.2921, hit rate recent 0.3145 / long run 0.3093
    - 6h: 18 calls (75 a day), hit rate 0.444, chance 0.083, lift 5.38x
    - 24h: 63 calls (64 a day), hit rate 0.317, chance 0.074, lift 4.29x
    - 7d: 483 calls (69 a day), hit rate 0.311, chance 0.074, lift 4.20x
    - 30d: 2172 calls (72 a day), hit rate 0.305, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.447; 0.35: 87, 0.499; 0.40: 61, 0.553; 0.45: 41, 0.607; 0.50: 25, 0.661; 0.55: 15, 0.705; 0.60: 6, 0.756; 0.65: 2, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.317; 0.35: 13, 0.353; 0.40: 2, 0.429; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.465 | 5.04% | 0.917 | 0.517 | 0.252 | 0.450 | -0.023 |
| 6h | 9.734 | 2.91% | 0.906 | 0.533 | 0.251 | 0.489 | 0.516 |
| 24h | 12.623 | 6.12% | 0.907 | 0.512 | 0.251 | 0.492 | 0.711 |
| 7d | 15.100 | 3.31% | 0.902 | 0.501 | 0.251 | 0.499 | 0.647 |
| 30d | 13.404 | 4.21% | 0.900 | 0.500 | 0.251 | 0.495 | 0.672 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.861 | 7.490 | 7.568 | 7.515 | 7.649 | 7.907 | 7.473 | 7.444 | 7.471 | 7.465 |
| 6h | 10.026 | 9.848 | 9.797 | 9.775 | 9.975 | 9.955 | 9.754 | 9.715 | 9.741 | 9.734 |
| 24h | 13.447 | 12.841 | 12.698 | 12.689 | 12.872 | 12.852 | 12.644 | 12.572 | 12.609 | 12.623 |
| 7d | 15.617 | 15.246 | 15.177 | 15.117 | 15.366 | 15.239 | 15.088 | 15.064 | 15.072 | 15.100 |
| 30d | 13.993 | 13.531 | 13.487 | 13.426 | 13.647 | 13.595 | 13.400 | 13.381 | 13.379 | 13.404 |

## Next candle

- candle starting 2026-10-25 01:47 UTC, last close 2358.89
- P(up) 0.4943, return quantiles (bp): {'05': -4.216, '10': -2.895, '25': -1.501, '40': -0.649, '50': -0.035, '60': 0.588, '75': 1.643, '90': 3.176, '95': 4.421}
- changepoint probability 0.0346, regime age 120.6 min
- agent weights: empirical 0.003, ewma 0.043, garch 0.148, har 0.136, bocpd 0.034, hmm 0.049, online_qr 0.204, lgbm 0.383

## Learning log

- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.96, 7.08, 20.11], current probabilities: [0.97, 0.029, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-25 01:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.453, 'l_abs': 0.672, 'l_hi': 0.772, 'l_lo': 0.774, 'b05': 0.723, 'b25': 0.708, 'b75': 0.61, 'b95': 0.686}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.44, 1.803, 1.887, 2.072, 2.368, 2.512, 2.915, 3.289, 3.272, 3.8, 4.057, 4.317, 4.489, 4.473]}
- calibration offsets (in sigma): {'05': 0.123, '10': 0.166, '25': 0.095, '40': 0.034, '50': 0.02, '60': 0.006, '75': -0.015, '90': -0.066, '95': -0.083}
