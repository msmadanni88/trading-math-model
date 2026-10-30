# ETH-USD 60s candle generator - report

- generated: 2026-10-30 02:58 UTC
- last closed candle: 2026-10-30 02:58 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.539 (672) [0.504, 0.574] | 0.520 (2877) [0.502, 0.539] | 0.516 (5562) [0.503, 0.530] | 0.522 (2590) [0.501, 0.544] | 0.545 (11) | 0.500 | flat -0.003 (noise 0.032) |
| colour_clear | 0.522 (812) | 0.539 (5652) [0.533, 0.545] | 0.539 (23642) [0.532, 0.545] | 0.519 (45555) [0.513, 0.525] | 0.545 (21317) [0.541, 0.549] | 0.548 (73) | 0.500 | flat -0.016 (noise 0.009) |
| colour_confident | 0.588 (119) | 0.601 (1299) [0.586, 0.618] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.333 (3) | 0.500 | flat +0.003 (noise 0.020) |
| colour_next | 0.512 (1433) | 0.525 (10025) [0.521, 0.530] | 0.526 (42874) [0.522, 0.530] | 0.514 (82916) [0.510, 0.517] | 0.529 (38567) [0.525, 0.533] | 0.506 (178) | 0.500 | flat -0.010 (noise 0.007) |
| colour_path | 0.497 (20062) | 0.502 (140350) [0.500, 0.504] | 0.501 (600236) [0.499, 0.502] | 0.501 (1160824) [0.500, 0.502] | 0.501 (539938) [0.499, 0.502] | 0.507 (2492) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.789 (19) | 0.610 (408) [0.584, 0.648] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.000 (1) | 0.500 | flat -0.017 (noise 0.040) |
| reversal_k13_next | 0.261 (46) | 0.319 (407) [0.286, 0.358] | 0.312 (2054) [0.300, 0.325] | 0.308 (3893) [0.298, 0.319] | 0.318 (1788) [0.307, 0.330] | 0.000 (3) | 0.077 | flat +0.004 (noise 0.032) |
| reversal_k13_now | 0.522 (67) | 0.557 (420) [0.510, 0.605] | 0.564 (1641) [0.544, 0.585] | 0.572 (2962) [0.557, 0.587] | 0.563 (1490) [0.542, 0.586] | 0.429 (7) | 0.077 | flat +0.019 (noise 0.036) |
| reversal_k3_next | 0.595 (121) | 0.591 (673) [0.583, 0.601] | 0.581 (2921) [0.569, 0.593] | 0.584 (5118) [0.575, 0.594] | 0.581 (2678) [0.569, 0.594] | 0.750 (12) | 0.293 | flat +0.010 (noise 0.026) |
| reversal_k3_now | 1.000 (65) | 0.954 (411) [0.927, 0.978] | 0.936 (1740) [0.927, 0.947] | 0.939 (3322) [0.933, 0.946] | 0.936 (1559) [0.925, 0.947] | 0.800 (5) | 0.293 | flat +0.021 (noise 0.021) |
| reversal_k5_next | 0.537 (41) | 0.507 (675) [0.496, 0.518] | 0.468 (3060) [0.455, 0.483] | 0.479 (4724) [0.467, 0.491] | 0.467 (2734) [0.453, 0.482] | 0.800 (5) | 0.187 | up +0.065 (noise 0.025) |
| reversal_k5_now | 0.841 (69) | 0.830 (417) [0.819, 0.839] | 0.826 (1628) [0.815, 0.836] | 0.831 (3075) [0.821, 0.841] | 0.823 (1464) [0.811, 0.834] | 0.667 (6) | 0.187 | flat +0.003 (noise 0.027) |
| reversal_k8_next | 0.394 (94) | 0.395 (737) [0.375, 0.412] | 0.384 (2774) [0.371, 0.396] | 0.389 (4712) [0.379, 0.400] | 0.384 (2606) [0.371, 0.397] | 0.167 (6) | 0.121 | flat +0.035 (noise 0.025) |
| reversal_k8_now | 0.754 (57) | 0.688 (388) [0.632, 0.741] | 0.692 (1568) [0.671, 0.712] | 0.702 (3016) [0.687, 0.718] | 0.689 (1429) [0.667, 0.712] | 0.333 (6) | 0.121 | flat +0.011 (noise 0.041) |
| overall | 0.500 (22151) | 0.506 (155175) [0.504, 0.508] | 0.504 (663373) [0.503, 0.506] | 0.503 (1280124) [0.502, 0.504] | 0.504 (596843) [0.503, 0.506] | 0.507 (2731) | - | flat +0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08227, 0.1248] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5254, 'levels': [{'threshold': 0.08227, 'calls_per_day': 144.5, 'win_rate': 0.6116}, {'threshold': 0.1248, 'calls_per_day': 36.4, 'win_rate': 0.6133}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 37604, 'rate': 0.5295}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14940 | 0.340 | 0.522 (14715) | 0.582 (1970) | 0.752 (2557) |
| volatility: normal | 14939 | 0.366 | 0.531 (14873) | 0.613 (1358) | 0.750 (2239) |
| volatility: wild | 14939 | 0.380 | 0.522 (14900) | 0.632 (696) | 0.770 (2035) |
| session: Asia 00-08 | 15058 | 0.361 | 0.531 (14957) | 0.604 (1428) | 0.757 (2272) |
| session: Europe 08-13 | 9300 | 0.357 | 0.529 (9216) | 0.590 (996) | 0.750 (1513) |
| session: US 13-21 | 14880 | 0.370 | 0.521 (14789) | 0.600 (1035) | 0.765 (2180) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5526) | 0.612 (565) | 0.749 (866) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.351 | 0.373 | 0.300 | 0.300 | 0.433 | 0.190 | 0.511 | 1.790 |
| 6h | 360 | 0.380 | 0.374 | 0.306 | 0.356 | 0.481 | 0.242 | 0.519 | 1.530 |
| 24h | 1440 | 0.373 | 0.369 | 0.295 | 0.328 | 0.514 | 0.258 | 0.489 | 1.166 |
| 7d | 10080 | 0.367 | 0.359 | 0.282 | 0.313 | 0.524 | 0.263 | 0.471 | 1.226 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.306 | 0.526 | 0.259 | 0.464 | 1.271 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.351 / 0.433 / 0.950; 2: 0.423 / 0.600 / 1.000; 3: 0.334 / 0.367 / 1.000; 4: 0.396 / 0.533 / 1.000; 5: 0.340 / 0.400 / 1.000; 6: 0.360 / 0.450 / 1.000; 7: 0.409 / 0.583 / 1.000; 8: 0.374 / 0.500 / 1.000; 9: 0.358 / 0.483 / 1.000; 10: 0.370 / 0.533 / 1.000; 11: 0.349 / 0.450 / 1.000; 12: 0.338 / 0.433 / 1.000; 13: 0.357 / 0.517 / 1.000; 14: 0.355 / 0.533 / 1.000; 15: 0.357 / 0.483 / 1.000
- 6h: 1: 0.380 / 0.481 / 0.919; 2: 0.391 / 0.539 / 0.956; 3: 0.371 / 0.461 / 0.958; 4: 0.391 / 0.547 / 0.947; 5: 0.366 / 0.478 / 0.961; 6: 0.377 / 0.506 / 0.958; 7: 0.382 / 0.514 / 0.978; 8: 0.378 / 0.517 / 0.989; 9: 0.379 / 0.511 / 0.978; 10: 0.369 / 0.492 / 0.978; 11: 0.374 / 0.514 / 0.978; 12: 0.370 / 0.492 / 0.981; 13: 0.381 / 0.511 / 0.992; 14: 0.368 / 0.492 / 0.992; 15: 0.375 / 0.483 / 0.986
- 24h: 1: 0.373 / 0.514 / 0.903; 2: 0.367 / 0.513 / 0.904; 3: 0.365 / 0.504 / 0.909; 4: 0.366 / 0.512 / 0.907; 5: 0.361 / 0.504 / 0.907; 6: 0.356 / 0.491 / 0.903; 7: 0.367 / 0.509 / 0.907; 8: 0.359 / 0.498 / 0.903; 9: 0.356 / 0.483 / 0.904; 10: 0.362 / 0.507 / 0.909; 11: 0.356 / 0.492 / 0.908; 12: 0.350 / 0.474 / 0.906; 13: 0.360 / 0.507 / 0.907; 14: 0.356 / 0.498 / 0.907; 15: 0.355 / 0.495 / 0.903
- 7d: 1: 0.367 / 0.524 / 0.899; 2: 0.355 / 0.495 / 0.902; 3: 0.358 / 0.510 / 0.902; 4: 0.355 / 0.500 / 0.901; 5: 0.354 / 0.505 / 0.902; 6: 0.351 / 0.502 / 0.902; 7: 0.354 / 0.502 / 0.902; 8: 0.353 / 0.507 / 0.901; 9: 0.353 / 0.501 / 0.901; 10: 0.353 / 0.505 / 0.901; 11: 0.350 / 0.500 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.350 / 0.501 / 0.900; 14: 0.351 / 0.501 / 0.900; 15: 0.350 / 0.499 / 0.900
- 30d: 1: 0.362 / 0.526 / 0.899; 2: 0.351 / 0.498 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.115 (body 0.075, range 0.154); 'price stays where it was' would score 0.091; colour right 0.483; typical miss of the close 23.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.137 (body 0.093, range 0.182); 'price stays where it was' would score 0.147; colour right 0.497; typical miss of the close 26.2 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.133 (body 0.088, range 0.178); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 12.2 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.129 (body 0.087, range 0.170); 'price stays where it was' would score 0.136; colour right 0.498; typical miss of the close 8.8 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.129; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.520 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.200 / 4.6; 3: 0.167 / 6.1; 4: 0.133 / 6.6; 5: 0.126 / 7.3; 6: 0.113 / 7.8; 7: 0.110 / 8.1; 8: 0.097 / 8.6; 9: 0.087 / 8.8; 10: 0.087 / 9.3; 11: 0.085 / 9.8; 12: 0.076 / 10.0; 13: 0.068 / 10.3; 14: 0.070 / 10.6; 15: 0.062 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 126652, probability skill vs chance 0.2399, widened contest next: False
  - now: threshold 0.8349, hit rate recent 0.9628 / long run 0.9434
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.314, naive rule 0.525, lift 2.98x
    - 24h: 61 calls (61 a day), hit rate 0.984, chance 0.301, naive rule 0.522, lift 3.27x
    - 7d: 410 calls (59 a day), hit rate 0.951, chance 0.293, naive rule 0.496, lift 3.24x
    - 30d: 1737 calls (58 a day), hit rate 0.936, chance 0.294, naive rule 0.493, lift 3.19x
  - next: threshold 0.5303, hit rate recent 0.6581 / long run 0.5926
    - 6h: 21 calls (85 a day), hit rate 0.714, chance 0.314, lift 2.27x
    - 24h: 113 calls (113 a day), hit rate 0.637, chance 0.301, lift 2.12x
    - 7d: 673 calls (96 a day), hit rate 0.596, chance 0.293, lift 2.03x
    - 30d: 2919 calls (97 a day), hit rate 0.581, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.496; 0.35: 536, 0.521; 0.40: 476, 0.578; 0.45: 407, 0.649; 0.50: 356, 0.700; 0.55: 311, 0.741; 0.60: 263, 0.787; 0.65: 221, 0.812; 0.70: 174, 0.845; 0.75: 137, 0.877; 0.80: 92, 0.914; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 501, 0.465; 0.40: 407, 0.498; 0.45: 310, 0.533; 0.50: 199, 0.570; 0.55: 89, 0.571; 0.60: 13, 0.636; 0.65: 1, 0.607
- **K=5**: model 1792540800, labels learned 126650, probability skill vs chance 0.2341, widened contest next: False
  - now: threshold 0.6784, hit rate recent 0.827 / long run 0.8258
    - 6h: 15 calls (61 a day), hit rate 0.800, chance 0.174, naive rule 0.424, lift 4.59x
    - 24h: 65 calls (65 a day), hit rate 0.846, chance 0.195, naive rule 0.450, lift 4.34x
    - 7d: 415 calls (59 a day), hit rate 0.829, chance 0.185, naive rule 0.407, lift 4.48x
    - 30d: 1626 calls (54 a day), hit rate 0.825, chance 0.188, naive rule 0.403, lift 4.39x
  - next: threshold 0.4572, hit rate recent 0.542 / long run 0.4929
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.174, lift 3.19x
    - 24h: 36 calls (36 a day), hit rate 0.583, chance 0.195, lift 2.99x
    - 7d: 660 calls (94 a day), hit rate 0.506, chance 0.185, lift 2.74x
    - 30d: 3058 calls (102 a day), hit rate 0.469, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.493; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 180, 0.669; 0.55: 140, 0.708; 0.60: 107, 0.753; 0.65: 77, 0.790; 0.70: 51, 0.828; 0.75: 30, 0.868; 0.80: 10, 0.898
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.390; 0.35: 254, 0.421; 0.40: 158, 0.457; 0.45: 69, 0.474; 0.50: 14, 0.493; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 126647, probability skill vs chance 0.2144, widened contest next: False
  - now: threshold 0.5646, hit rate recent 0.7278 / long run 0.6902
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.116, naive rule 0.372, lift 5.98x
    - 24h: 55 calls (55 a day), hit rate 0.727, chance 0.124, naive rule 0.362, lift 5.84x
    - 7d: 387 calls (55 a day), hit rate 0.682, chance 0.121, naive rule 0.340, lift 5.64x
    - 30d: 1568 calls (52 a day), hit rate 0.690, chance 0.121, naive rule 0.334, lift 5.69x
  - next: threshold 0.3375, hit rate recent 0.4084 / long run 0.388
    - 6h: 14 calls (58 a day), hit rate 0.357, chance 0.116, lift 3.09x
    - 24h: 85 calls (86 a day), hit rate 0.412, chance 0.124, lift 3.31x
    - 7d: 721 calls (103 a day), hit rate 0.393, chance 0.121, lift 3.24x
    - 30d: 2768 calls (92 a day), hit rate 0.384, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 189, 0.499; 0.40: 146, 0.549; 0.45: 112, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.675; 0.60: 40, 0.711; 0.65: 23, 0.774; 0.70: 11, 0.809; 0.75: 2, 0.774
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.357; 0.35: 92, 0.383; 0.40: 30, 0.406; 0.45: 6, 0.425; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 126642, probability skill vs chance 0.1868, widened contest next: False
  - now: threshold 0.4094, hit rate recent 0.5597 / long run 0.5578
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.078, naive rule 0.326, lift 7.45x
    - 24h: 62 calls (63 a day), hit rate 0.565, chance 0.080, naive rule 0.308, lift 7.09x
    - 7d: 418 calls (60 a day), hit rate 0.555, chance 0.076, naive rule 0.281, lift 7.27x
    - 30d: 1644 calls (55 a day), hit rate 0.564, chance 0.077, naive rule 0.277, lift 7.30x
  - next: threshold 0.2953, hit rate recent 0.2934 / long run 0.3138
    - 6h: 6 calls (25 a day), hit rate 0.167, chance 0.078, lift 2.13x
    - 24h: 42 calls (42 a day), hit rate 0.286, chance 0.080, lift 3.59x
    - 7d: 395 calls (57 a day), hit rate 0.314, chance 0.076, lift 4.11x
    - 30d: 2044 calls (68 a day), hit rate 0.313, chance 0.077, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.442; 0.35: 90, 0.493; 0.40: 64, 0.548; 0.45: 42, 0.597; 0.50: 28, 0.653; 0.55: 17, 0.693; 0.60: 8, 0.741; 0.65: 2, 0.742; 0.70: 0, 0.500
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.325; 0.35: 14, 0.356; 0.40: 2, 0.453; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 26.782 | 0.70% | 0.950 | 0.600 | 0.252 | 0.417 | 0.574 |
| 6h | 41.212 | 7.81% | 0.922 | 0.553 | 0.251 | 0.472 | 0.595 |
| 24h | 24.584 | 6.86% | 0.900 | 0.506 | 0.251 | 0.499 | 0.761 |
| 7d | 15.933 | 4.53% | 0.900 | 0.502 | 0.251 | 0.498 | 0.732 |
| 30d | 14.114 | 4.32% | 0.900 | 0.500 | 0.251 | 0.496 | 0.690 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.970 | 27.424 | 26.336 | 27.169 | 27.140 | 26.662 | 26.782 | 26.589 | 26.726 | 26.782 |
| 6h | 44.701 | 42.018 | 41.578 | 41.329 | 42.752 | 42.222 | 41.113 | 41.104 | 41.131 | 41.212 |
| 24h | 26.394 | 25.065 | 24.726 | 24.580 | 25.131 | 25.204 | 24.561 | 24.532 | 24.538 | 24.584 |
| 7d | 16.689 | 16.137 | 16.037 | 15.955 | 16.266 | 16.164 | 15.919 | 15.892 | 15.901 | 15.933 |
| 30d | 14.752 | 14.264 | 14.203 | 14.139 | 14.379 | 14.313 | 14.109 | 14.088 | 14.088 | 14.114 |

## Next candle

- candle starting 2026-10-30 02:58 UTC, last close 2203.96
- P(up) 0.4768, return quantiles (bp): {'05': -14.043, '10': -10.145, '25': -4.094, '40': -1.716, '50': -0.456, '60': 1.566, '75': 3.893, '90': 8.747, '95': 13.057}
- changepoint probability 0.0435, regime age 20.9 min
- agent weights: empirical 0.003, ewma 0.005, garch 0.070, har 0.259, bocpd 0.005, hmm 0.003, online_qr 0.287, lgbm 0.368

## Learning log

- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.9, 7.28, 18.78], current probabilities: [0.83, 0.165, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-30 03:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.288, 'l_abs': 0.727, 'l_hi': 0.723, 'l_lo': 0.756, 'b05': 0.746, 'b25': 0.722, 'b75': 0.647, 'b95': 0.738}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6]], 'cone_width': [1.249, 1.415, 1.774, 1.909, 2.411, 2.507, 3.027, 3.154, 3.075, 3.501, 4.131, 4.139, 4.391, 4.836]}
- calibration offsets (in sigma): {'05': -0.0115, '10': -0.013, '25': 0.0325, '40': -0.022, '50': -0.045, '60': -0.028, '75': -0.0825, '90': -0.097, '95': -0.0785}
