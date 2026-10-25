# ETH-USD 60s candle generator - report

- generated: 2026-10-25 19:20 UTC
- last closed candle: 2026-10-25 19:20 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.543 (672) [0.509, 0.577] | 0.517 (2876) [0.498, 0.536] | 0.515 (5082) [0.500, 0.528] | 0.519 (2110) [0.495, 0.543] | 0.636 (77) | 0.500 | flat +0.040 (noise 0.027) |
| colour_clear | 0.544 (743) | 0.553 (5669) [0.547, 0.562] | 0.533 (23412) [0.525, 0.541] | 0.517 (41491) [0.511, 0.524] | 0.547 (17253) [0.542, 0.552] | 0.546 (636) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.606 (269) | 0.608 (1282) [0.589, 0.628] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.570 (235) | 0.500 | flat +0.016 (noise 0.023) |
| colour_next | 0.522 (1431) | 0.534 (10039) [0.527, 0.541] | 0.523 (42853) [0.517, 0.528] | 0.513 (75756) [0.508, 0.517] | 0.530 (31407) [0.525, 0.534] | 0.531 (1156) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.501 (140546) [0.498, 0.503] | 0.501 (599942) [0.499, 0.502] | 0.501 (1060584) [0.500, 0.501] | 0.500 (439698) [0.498, 0.502] | 0.506 (16184) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.602 (98) | 0.636 (335) [0.607, 0.672] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.604 (96) | 0.500 | flat -0.005 (noise 0.045) |
| reversal_k13_next | 0.286 (63) | 0.310 (481) [0.291, 0.327] | 0.305 (2173) [0.292, 0.317] | 0.306 (3618) [0.296, 0.318] | 0.316 (1513) [0.305, 0.327] | 0.368 (57) | 0.077 | flat +0.004 (noise 0.031) |
| reversal_k13_now | 0.647 (51) | 0.530 (366) [0.490, 0.576] | 0.570 (1560) [0.549, 0.591] | 0.573 (2651) [0.557, 0.590] | 0.564 (1179) [0.540, 0.590] | 0.595 (42) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.630 (54) | 0.592 (699) [0.564, 0.624] | 0.580 (2792) [0.566, 0.594] | 0.584 (4562) [0.573, 0.594] | 0.580 (2122) [0.565, 0.596] | 0.579 (57) | 0.293 | flat +0.024 (noise 0.026) |
| reversal_k3_now | 0.980 (49) | 0.945 (397) [0.928, 0.962] | 0.938 (1690) [0.929, 0.947] | 0.938 (3023) [0.932, 0.945] | 0.933 (1260) [0.923, 0.944] | 0.882 (34) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.480 (125) | 0.460 (939) [0.433, 0.486] | 0.464 (2842) [0.449, 0.479] | 0.476 (4306) [0.463, 0.489] | 0.460 (2316) [0.445, 0.476] | 0.505 (109) | 0.187 | flat -0.006 (noise 0.025) |
| reversal_k5_now | 0.818 (55) | 0.812 (361) [0.800, 0.823] | 0.831 (1561) [0.818, 0.844] | 0.830 (2771) [0.819, 0.841] | 0.819 (1160) [0.804, 0.833] | 0.838 (37) | 0.187 | flat -0.006 (noise 0.029) |
| reversal_k8_next | 0.384 (86) | 0.377 (757) [0.359, 0.394] | 0.383 (2519) [0.370, 0.396] | 0.389 (4187) [0.377, 0.400] | 0.381 (2081) [0.367, 0.395] | 0.400 (100) | 0.120 | flat +0.004 (noise 0.026) |
| reversal_k8_now | 0.709 (55) | 0.654 (332) [0.613, 0.693] | 0.701 (1523) [0.681, 0.722] | 0.702 (2739) [0.686, 0.718] | 0.685 (1152) [0.662, 0.708] | 0.744 (39) | 0.121 | flat -0.031 (noise 0.036) |
| overall | 0.505 (22099) | 0.504 (155589) [0.501, 0.507] | 0.504 (662331) [0.502, 0.505] | 0.503 (1169279) [0.502, 0.504] | 0.504 (485998) [0.502, 0.506] | 0.509 (17892) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07634, 0.1134] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5356, 'levels': [{'threshold': 0.07634, 'calls_per_day': 150.8, 'win_rate': 0.6138}, {'threshold': 0.1134, 'calls_per_day': 39.3, 'win_rate': 0.6522}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 31424, 'rate': 0.5309}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15267 | 0.336 | 0.524 (15018) | 0.587 (1723) | 0.761 (2522) |
| volatility: normal | 15266 | 0.364 | 0.523 (15199) | 0.607 (1179) | 0.759 (2243) |
| volatility: wild | 15267 | 0.378 | 0.519 (15228) | 0.639 (526) | 0.771 (1922) |
| session: Asia 00-08 | 15360 | 0.357 | 0.527 (15256) | 0.607 (1220) | 0.766 (2206) |
| session: Europe 08-13 | 9600 | 0.355 | 0.524 (9513) | 0.598 (858) | 0.761 (1524) |
| session: US 13-21 | 15260 | 0.368 | 0.518 (15159) | 0.595 (855) | 0.771 (2143) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5517) | 0.610 (495) | 0.737 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.363 | 0.343 | 0.223 | 0.223 | 0.550 | 0.262 | 0.465 | 1.351 |
| 6h | 360 | 0.362 | 0.355 | 0.272 | 0.280 | 0.526 | 0.266 | 0.457 | 1.123 |
| 24h | 1440 | 0.351 | 0.342 | 0.265 | 0.287 | 0.522 | 0.261 | 0.440 | 1.316 |
| 7d | 10080 | 0.371 | 0.361 | 0.275 | 0.307 | 0.536 | 0.269 | 0.472 | 1.207 |
| 30d | 43200 | 0.359 | 0.353 | 0.276 | 0.304 | 0.524 | 0.257 | 0.462 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.363 / 0.550 / 0.933; 2: 0.342 / 0.483 / 0.983; 3: 0.332 / 0.467 / 0.983; 4: 0.340 / 0.483 / 0.983; 5: 0.347 / 0.500 / 0.983; 6: 0.355 / 0.567 / 1.000; 7: 0.334 / 0.433 / 0.983; 8: 0.332 / 0.550 / 0.983; 9: 0.359 / 0.567 / 0.983; 10: 0.319 / 0.450 / 1.000; 11: 0.323 / 0.500 / 1.000; 12: 0.352 / 0.550 / 1.000; 13: 0.328 / 0.483 / 1.000; 14: 0.317 / 0.433 / 1.000; 15: 0.328 / 0.517 / 1.000
- 6h: 1: 0.362 / 0.526 / 0.900; 2: 0.347 / 0.490 / 0.914; 3: 0.354 / 0.521 / 0.881; 4: 0.344 / 0.518 / 0.886; 5: 0.341 / 0.490 / 0.894; 6: 0.358 / 0.554 / 0.919; 7: 0.342 / 0.487 / 0.908; 8: 0.347 / 0.543 / 0.906; 9: 0.349 / 0.499 / 0.914; 10: 0.338 / 0.487 / 0.892; 11: 0.349 / 0.526 / 0.892; 12: 0.338 / 0.515 / 0.883; 13: 0.343 / 0.518 / 0.869; 14: 0.324 / 0.468 / 0.864; 15: 0.341 / 0.507 / 0.858
- 24h: 1: 0.351 / 0.522 / 0.893; 2: 0.336 / 0.501 / 0.901; 3: 0.337 / 0.501 / 0.896; 4: 0.342 / 0.528 / 0.899; 5: 0.332 / 0.497 / 0.901; 6: 0.338 / 0.519 / 0.906; 7: 0.334 / 0.500 / 0.904; 8: 0.336 / 0.512 / 0.903; 9: 0.333 / 0.486 / 0.907; 10: 0.335 / 0.506 / 0.905; 11: 0.334 / 0.520 / 0.908; 12: 0.337 / 0.525 / 0.906; 13: 0.333 / 0.503 / 0.903; 14: 0.332 / 0.509 / 0.905; 15: 0.333 / 0.499 / 0.903
- 7d: 1: 0.371 / 0.536 / 0.899; 2: 0.358 / 0.503 / 0.900; 3: 0.358 / 0.509 / 0.900; 4: 0.353 / 0.495 / 0.900; 5: 0.354 / 0.501 / 0.900; 6: 0.353 / 0.496 / 0.901; 7: 0.351 / 0.494 / 0.900; 8: 0.355 / 0.510 / 0.900; 9: 0.352 / 0.498 / 0.900; 10: 0.353 / 0.506 / 0.900; 11: 0.351 / 0.501 / 0.900; 12: 0.352 / 0.504 / 0.899; 13: 0.349 / 0.496 / 0.899; 14: 0.351 / 0.498 / 0.899; 15: 0.350 / 0.501 / 0.899
- 30d: 1: 0.359 / 0.524 / 0.899; 2: 0.349 / 0.498 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.347 / 0.498 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.347 / 0.500 / 0.900; 7: 0.346 / 0.499 / 0.900; 8: 0.346 / 0.503 / 0.900; 9: 0.344 / 0.496 / 0.900; 10: 0.346 / 0.505 / 0.900; 11: 0.344 / 0.499 / 0.900; 12: 0.346 / 0.504 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.344 / 0.498 / 0.900; 15: 0.344 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.183 (body 0.133, range 0.234); 'price stays where it was' would score 0.139; colour right 0.533; typical miss of the close 3.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.131 (body 0.092, range 0.171); 'price stays where it was' would score 0.133; colour right 0.471; typical miss of the close 6.7 bp; chain ended on the right side 0.708 of 24 chains; n=360
- 24h: match 0.127 (body 0.091, range 0.163); 'price stays where it was' would score 0.131; colour right 0.489; typical miss of the close 6.3 bp; chain ended on the right side 0.615 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.168); 'price stays where it was' would score 0.134; colour right 0.501; typical miss of the close 8.8 bp; chain ended on the right side 0.552 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.5 bp; chain ended on the right side 0.523 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.195 / 4.4; 3: 0.168 / 5.7; 4: 0.132 / 6.3; 5: 0.123 / 6.9; 6: 0.112 / 7.5; 7: 0.106 / 7.8; 8: 0.097 / 8.2; 9: 0.087 / 8.2; 10: 0.087 / 8.8; 11: 0.084 / 9.3; 12: 0.077 / 9.6; 13: 0.068 / 9.7; 14: 0.069 / 10.2; 15: 0.059 / 10.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 120434, probability skill vs chance 0.2227, widened contest next: False
  - now: threshold 0.8342, hit rate recent 0.9273 / long run 0.936
    - 6h: 7 calls (28 a day), hit rate 0.857, chance 0.297, naive rule 0.530, lift 2.88x
    - 24h: 41 calls (41 a day), hit rate 0.902, chance 0.296, naive rule 0.521, lift 3.05x
    - 7d: 381 calls (54 a day), hit rate 0.937, chance 0.295, naive rule 0.500, lift 3.17x
    - 30d: 1683 calls (56 a day), hit rate 0.935, chance 0.294, naive rule 0.493, lift 3.18x
  - next: threshold 0.537, hit rate recent 0.5735 / long run 0.5897
    - 6h: 23 calls (93 a day), hit rate 0.391, chance 0.297, lift 1.32x
    - 24h: 64 calls (64 a day), hit rate 0.562, chance 0.296, lift 1.90x
    - 7d: 678 calls (97 a day), hit rate 0.591, chance 0.295, lift 2.00x
    - 30d: 2797 calls (93 a day), hit rate 0.579, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 538, 0.520; 0.40: 478, 0.576; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 312, 0.740; 0.60: 264, 0.784; 0.65: 220, 0.809; 0.70: 174, 0.841; 0.75: 135, 0.874; 0.80: 91, 0.913; 0.85: 46, 0.950; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.426; 0.35: 502, 0.463; 0.40: 408, 0.498; 0.45: 310, 0.533; 0.50: 201, 0.567; 0.55: 91, 0.575; 0.60: 14, 0.618; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 120432, probability skill vs chance 0.2089, widened contest next: False
  - now: threshold 0.6724, hit rate recent 0.8186 / long run 0.8208
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.150, naive rule 0.369, lift 5.99x
    - 24h: 46 calls (46 a day), hit rate 0.804, chance 0.170, naive rule 0.394, lift 4.72x
    - 7d: 359 calls (51 a day), hit rate 0.811, chance 0.182, naive rule 0.401, lift 4.45x
    - 30d: 1560 calls (52 a day), hit rate 0.831, chance 0.187, naive rule 0.400, lift 4.44x
  - next: threshold 0.4195, hit rate recent 0.4894 / long run 0.4756
    - 6h: 30 calls (122 a day), hit rate 0.467, chance 0.150, lift 3.11x
    - 24h: 139 calls (140 a day), hit rate 0.482, chance 0.170, lift 2.83x
    - 7d: 922 calls (132 a day), hit rate 0.470, chance 0.182, lift 2.58x
    - 30d: 2926 calls (98 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.426; 0.35: 343, 0.493; 0.40: 276, 0.565; 0.45: 223, 0.620; 0.50: 176, 0.670; 0.55: 135, 0.711; 0.60: 104, 0.755; 0.65: 75, 0.792; 0.70: 53, 0.832; 0.75: 31, 0.878; 0.80: 10, 0.903
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.388; 0.35: 252, 0.420; 0.40: 158, 0.453; 0.45: 70, 0.464; 0.50: 15, 0.490; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 120429, probability skill vs chance 0.1995, widened contest next: False
  - now: threshold 0.556, hit rate recent 0.704 / long run 0.6857
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.120, naive rule 0.348, lift 6.25x
    - 24h: 47 calls (47 a day), hit rate 0.745, chance 0.110, naive rule 0.326, lift 6.74x
    - 7d: 336 calls (48 a day), hit rate 0.661, chance 0.115, naive rule 0.319, lift 5.75x
    - 30d: 1525 calls (51 a day), hit rate 0.698, chance 0.121, naive rule 0.330, lift 5.78x
  - next: threshold 0.3369, hit rate recent 0.4019 / long run 0.3819
    - 6h: 28 calls (115 a day), hit rate 0.393, chance 0.120, lift 3.27x
    - 24h: 119 calls (120 a day), hit rate 0.403, chance 0.110, lift 3.65x
    - 7d: 767 calls (110 a day), hit rate 0.377, chance 0.115, lift 3.28x
    - 30d: 2579 calls (86 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.426; 0.35: 188, 0.495; 0.40: 144, 0.548; 0.45: 110, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.674; 0.60: 41, 0.722; 0.65: 23, 0.788; 0.70: 10, 0.831; 0.75: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.351; 0.35: 97, 0.379; 0.40: 36, 0.397; 0.45: 8, 0.424; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 120424, probability skill vs chance 0.178, widened contest next: False
  - now: threshold 0.4056, hit rate recent 0.6009 / long run 0.5608
    - 6h: 11 calls (46 a day), hit rate 0.818, chance 0.067, naive rule 0.235, lift 12.27x
    - 24h: 49 calls (50 a day), hit rate 0.633, chance 0.069, naive rule 0.252, lift 9.11x
    - 7d: 355 calls (51 a day), hit rate 0.546, chance 0.073, naive rule 0.265, lift 7.45x
    - 30d: 1569 calls (52 a day), hit rate 0.568, chance 0.077, naive rule 0.272, lift 7.37x
  - next: threshold 0.2946, hit rate recent 0.3373 / long run 0.3134
    - 6h: 15 calls (63 a day), hit rate 0.267, chance 0.067, lift 4.00x
    - 24h: 73 calls (74 a day), hit rate 0.384, chance 0.069, lift 5.52x
    - 7d: 478 calls (68 a day), hit rate 0.314, chance 0.073, lift 4.28x
    - 30d: 2174 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.444; 0.35: 87, 0.495; 0.40: 62, 0.552; 0.45: 41, 0.603; 0.50: 26, 0.658; 0.55: 15, 0.703; 0.60: 7, 0.745; 0.65: 2, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.316; 0.35: 14, 0.345; 0.40: 2, 0.420; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.186 | 3.58% | 0.933 | 0.583 | 0.251 | 0.533 | -0.054 |
| 6h | 12.071 | 1.32% | 0.911 | 0.503 | 0.250 | 0.513 | 0.364 |
| 24h | 11.069 | 1.97% | 0.894 | 0.501 | 0.250 | 0.498 | 0.480 |
| 7d | 14.990 | 3.24% | 0.900 | 0.500 | 0.250 | 0.502 | 0.647 |
| 30d | 13.269 | 4.19% | 0.900 | 0.500 | 0.251 | 0.495 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.453 | 7.243 | 7.100 | 7.084 | 7.265 | 7.428 | 7.205 | 7.143 | 7.146 | 7.186 |
| 6h | 12.233 | 12.260 | 12.185 | 12.090 | 12.478 | 12.244 | 12.059 | 11.980 | 12.033 | 12.071 |
| 24h | 11.292 | 11.203 | 11.148 | 11.105 | 11.374 | 11.280 | 11.059 | 11.011 | 11.045 | 11.069 |
| 7d | 15.492 | 15.139 | 15.069 | 15.008 | 15.266 | 15.143 | 14.977 | 14.953 | 14.962 | 14.990 |
| 30d | 13.850 | 13.398 | 13.353 | 13.293 | 13.510 | 13.463 | 13.265 | 13.246 | 13.245 | 13.269 |

## Next candle

- candle starting 2026-10-25 19:20 UTC, last close 2352.14
- P(up) 0.5098, return quantiles (bp): {'05': -5.305, '10': -4.116, '25': -2.145, '40': -0.713, '50': 0.076, '60': 0.832, '75': 2.075, '90': 4.28, '95': 5.445}
- changepoint probability 0.0488, regime age 93.0 min
- agent weights: empirical 0.025, ewma 0.040, garch 0.084, har 0.152, bocpd 0.008, hmm 0.034, online_qr 0.233, lgbm 0.424

## Learning log

- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.8, 19.68], current probabilities: [0.954, 0.045, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-25 19:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.507, 'l_abs': 0.718, 'l_hi': 0.776, 'l_lo': 0.765, 'b05': 0.722, 'b25': 0.709, 'b75': 0.69, 'b95': 0.681}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.295, 1.865, 2.073, 2.323, 2.216, 2.447, 2.784, 3.018, 3.385, 3.557, 3.798, 4.206, 4.373, 4.628]}
- calibration offsets (in sigma): {'05': 0.0595, '10': 0.009, '25': -0.0125, '40': 0.016, '50': 0.015, '60': 0.014, '75': 0.0025, '90': -0.009, '95': -0.0195}
