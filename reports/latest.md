# ETH-USD 60s candle generator - report

- generated: 2026-10-30 16:25 UTC
- last closed candle: 2026-10-30 16:25 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.539 (672) [0.504, 0.574] | 0.520 (2877) [0.502, 0.539] | 0.516 (5562) [0.503, 0.530] | 0.522 (2590) [0.501, 0.544] | 0.462 (65) | 0.500 | flat -0.003 (noise 0.032) |
| colour_clear | 0.522 (812) | 0.539 (5652) [0.533, 0.545] | 0.539 (23642) [0.532, 0.545] | 0.519 (45555) [0.513, 0.525] | 0.545 (21317) [0.541, 0.549] | 0.544 (535) | 0.500 | flat -0.016 (noise 0.009) |
| colour_confident | 0.588 (119) | 0.601 (1299) [0.586, 0.618] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.600 (55) | 0.500 | flat +0.003 (noise 0.020) |
| colour_next | 0.512 (1433) | 0.525 (10025) [0.521, 0.530] | 0.526 (42874) [0.522, 0.530] | 0.514 (82916) [0.510, 0.517] | 0.529 (38567) [0.525, 0.533] | 0.530 (983) | 0.500 | flat -0.010 (noise 0.007) |
| colour_path | 0.497 (20062) | 0.502 (140350) [0.500, 0.504] | 0.501 (600236) [0.499, 0.502] | 0.501 (1160824) [0.500, 0.502] | 0.501 (539938) [0.499, 0.502] | 0.502 (13762) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.789 (19) | 0.610 (408) [0.584, 0.648] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.556 (9) | 0.500 | flat -0.017 (noise 0.040) |
| reversal_k13_next | 0.261 (46) | 0.319 (407) [0.286, 0.358] | 0.312 (2054) [0.300, 0.325] | 0.308 (3893) [0.298, 0.319] | 0.318 (1788) [0.307, 0.330] | 0.263 (38) | 0.077 | flat +0.004 (noise 0.032) |
| reversal_k13_now | 0.522 (67) | 0.557 (420) [0.510, 0.605] | 0.564 (1641) [0.544, 0.585] | 0.572 (2962) [0.557, 0.587] | 0.563 (1490) [0.542, 0.586] | 0.533 (45) | 0.077 | flat +0.019 (noise 0.036) |
| reversal_k3_next | 0.595 (121) | 0.591 (673) [0.583, 0.601] | 0.581 (2921) [0.569, 0.593] | 0.584 (5118) [0.575, 0.594] | 0.581 (2678) [0.569, 0.594] | 0.565 (69) | 0.293 | flat +0.010 (noise 0.026) |
| reversal_k3_now | 1.000 (65) | 0.954 (411) [0.927, 0.978] | 0.936 (1740) [0.927, 0.947] | 0.939 (3322) [0.933, 0.946] | 0.936 (1559) [0.925, 0.947] | 0.933 (30) | 0.293 | flat +0.021 (noise 0.021) |
| reversal_k5_next | 0.537 (41) | 0.507 (675) [0.496, 0.518] | 0.468 (3060) [0.455, 0.483] | 0.479 (4724) [0.467, 0.491] | 0.467 (2734) [0.453, 0.482] | 0.526 (19) | 0.187 | up +0.065 (noise 0.025) |
| reversal_k5_now | 0.841 (69) | 0.830 (417) [0.819, 0.839] | 0.826 (1628) [0.815, 0.836] | 0.831 (3075) [0.821, 0.841] | 0.823 (1464) [0.811, 0.834] | 0.727 (33) | 0.187 | flat +0.003 (noise 0.027) |
| reversal_k8_next | 0.394 (94) | 0.395 (737) [0.375, 0.412] | 0.384 (2774) [0.371, 0.396] | 0.389 (4712) [0.379, 0.400] | 0.384 (2606) [0.371, 0.397] | 0.359 (64) | 0.121 | flat +0.035 (noise 0.025) |
| reversal_k8_now | 0.754 (57) | 0.688 (388) [0.632, 0.741] | 0.692 (1568) [0.671, 0.712] | 0.702 (3016) [0.687, 0.718] | 0.689 (1429) [0.667, 0.712] | 0.576 (33) | 0.121 | flat +0.011 (noise 0.041) |
| overall | 0.500 (22151) | 0.506 (155175) [0.504, 0.508] | 0.504 (663373) [0.503, 0.506] | 0.503 (1280124) [0.502, 0.504] | 0.504 (596843) [0.503, 0.506] | 0.504 (15141) | - | flat +0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08202, 0.1249] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5257, 'levels': [{'threshold': 0.08202, 'calls_per_day': 142.9, 'win_rate': 0.608}, {'threshold': 0.1249, 'calls_per_day': 36.0, 'win_rate': 0.6008}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 38409, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15209 | 0.341 | 0.522 (14982) | 0.584 (2003) | 0.752 (2589) |
| volatility: normal | 15208 | 0.366 | 0.532 (15142) | 0.613 (1354) | 0.753 (2276) |
| volatility: wild | 15208 | 0.381 | 0.521 (15169) | 0.627 (719) | 0.764 (2083) |
| session: Asia 00-08 | 15360 | 0.361 | 0.531 (15259) | 0.603 (1454) | 0.754 (2314) |
| session: Europe 08-13 | 9600 | 0.358 | 0.528 (9515) | 0.593 (1012) | 0.750 (1552) |
| session: US 13-21 | 15085 | 0.370 | 0.521 (14993) | 0.600 (1045) | 0.763 (2216) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5526) | 0.612 (565) | 0.749 (866) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.407 | 0.369 | 0.296 | 0.296 | 0.567 | 0.326 | 0.489 | 1.065 |
| 6h | 360 | 0.387 | 0.379 | 0.291 | 0.316 | 0.518 | 0.275 | 0.500 | 1.032 |
| 24h | 1440 | 0.385 | 0.377 | 0.301 | 0.339 | 0.515 | 0.264 | 0.506 | 1.119 |
| 7d | 10080 | 0.368 | 0.360 | 0.284 | 0.316 | 0.524 | 0.263 | 0.473 | 1.239 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.307 | 0.526 | 0.259 | 0.464 | 1.273 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.407 / 0.567 / 0.883; 2: 0.392 / 0.550 / 0.900; 3: 0.374 / 0.467 / 1.000; 4: 0.384 / 0.483 / 1.000; 5: 0.384 / 0.483 / 0.967; 6: 0.373 / 0.500 / 0.867; 7: 0.394 / 0.500 / 0.850; 8: 0.369 / 0.467 / 0.833; 9: 0.362 / 0.483 / 0.817; 10: 0.392 / 0.533 / 0.833; 11: 0.364 / 0.433 / 0.817; 12: 0.391 / 0.567 / 0.750; 13: 0.368 / 0.450 / 0.717; 14: 0.399 / 0.617 / 0.750; 15: 0.380 / 0.517 / 0.717
- 6h: 1: 0.387 / 0.518 / 0.892; 2: 0.379 / 0.501 / 0.867; 3: 0.381 / 0.510 / 0.978; 4: 0.380 / 0.507 / 0.958; 5: 0.385 / 0.510 / 0.906; 6: 0.386 / 0.549 / 0.817; 7: 0.379 / 0.504 / 0.839; 8: 0.371 / 0.487 / 0.811; 9: 0.373 / 0.493 / 0.792; 10: 0.373 / 0.493 / 0.814; 11: 0.366 / 0.446 / 0.803; 12: 0.379 / 0.526 / 0.764; 13: 0.377 / 0.510 / 0.775; 14: 0.376 / 0.513 / 0.781; 15: 0.375 / 0.507 / 0.744
- 24h: 1: 0.385 / 0.515 / 0.901; 2: 0.376 / 0.489 / 0.897; 3: 0.375 / 0.507 / 0.912; 4: 0.376 / 0.503 / 0.919; 5: 0.376 / 0.508 / 0.910; 6: 0.376 / 0.522 / 0.899; 7: 0.378 / 0.500 / 0.900; 8: 0.369 / 0.497 / 0.890; 9: 0.370 / 0.490 / 0.887; 10: 0.371 / 0.503 / 0.887; 11: 0.369 / 0.498 / 0.889; 12: 0.369 / 0.495 / 0.883; 13: 0.372 / 0.506 / 0.882; 14: 0.369 / 0.503 / 0.886; 15: 0.368 / 0.491 / 0.881
- 7d: 1: 0.368 / 0.524 / 0.898; 2: 0.355 / 0.491 / 0.898; 3: 0.359 / 0.509 / 0.900; 4: 0.356 / 0.501 / 0.901; 5: 0.355 / 0.504 / 0.899; 6: 0.352 / 0.504 / 0.898; 7: 0.355 / 0.502 / 0.898; 8: 0.354 / 0.507 / 0.898; 9: 0.354 / 0.501 / 0.897; 10: 0.354 / 0.504 / 0.897; 11: 0.351 / 0.502 / 0.897; 12: 0.353 / 0.502 / 0.896; 13: 0.352 / 0.502 / 0.896; 14: 0.352 / 0.502 / 0.896; 15: 0.352 / 0.500 / 0.896
- 30d: 1: 0.362 / 0.526 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.348 / 0.501 / 0.899; 9: 0.347 / 0.497 / 0.899; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.504 / 0.899; 13: 0.347 / 0.501 / 0.899; 14: 0.346 / 0.500 / 0.899; 15: 0.346 / 0.498 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.153 (body 0.107, range 0.198); 'price stays where it was' would score 0.153; colour right 0.500; typical miss of the close 18.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.139 (body 0.089, range 0.190); 'price stays where it was' would score 0.134; colour right 0.521; typical miss of the close 14.7 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.142 (body 0.098, range 0.187); 'price stays where it was' would score 0.141; colour right 0.514; typical miss of the close 14.4 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.129 (body 0.087, range 0.170); 'price stays where it was' would score 0.136; colour right 0.500; typical miss of the close 9.1 bp; chain ended on the right side 0.525 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.164); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 7.9 bp; chain ended on the right side 0.520 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.0; 2: 0.200 / 4.6; 3: 0.168 / 6.1; 4: 0.132 / 6.6; 5: 0.127 / 7.3; 6: 0.114 / 7.8; 7: 0.112 / 8.1; 8: 0.099 / 8.6; 9: 0.089 / 8.8; 10: 0.088 / 9.3; 11: 0.085 / 9.8; 12: 0.076 / 10.1; 13: 0.068 / 10.3; 14: 0.071 / 10.7; 15: 0.062 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 127459, probability skill vs chance 0.2382, widened contest next: False
  - now: threshold 0.8343, hit rate recent 0.9636 / long run 0.9441
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.283, naive rule 0.517, lift 3.53x
    - 24h: 55 calls (55 a day), hit rate 0.964, chance 0.301, naive rule 0.516, lift 3.20x
    - 7d: 397 calls (57 a day), hit rate 0.950, chance 0.292, naive rule 0.497, lift 3.25x
    - 30d: 1741 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5291, hit rate recent 0.5878 / long run 0.5868
    - 6h: 28 calls (114 a day), hit rate 0.500, chance 0.283, lift 1.77x
    - 24h: 93 calls (93 a day), hit rate 0.602, chance 0.301, lift 2.00x
    - 7d: 694 calls (99 a day), hit rate 0.591, chance 0.292, lift 2.02x
    - 30d: 2928 calls (98 a day), hit rate 0.579, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 536, 0.520; 0.40: 476, 0.577; 0.45: 407, 0.648; 0.50: 356, 0.699; 0.55: 311, 0.741; 0.60: 263, 0.787; 0.65: 220, 0.813; 0.70: 174, 0.845; 0.75: 137, 0.878; 0.80: 92, 0.915; 0.85: 47, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 500, 0.464; 0.40: 407, 0.497; 0.45: 310, 0.531; 0.50: 199, 0.567; 0.55: 88, 0.568; 0.60: 13, 0.635; 0.65: 1, 0.607
- **K=5**: model 1792540800, labels learned 127457, probability skill vs chance 0.226, widened contest next: False
  - now: threshold 0.6781, hit rate recent 0.7968 / long run 0.822
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.178, naive rule 0.432, lift 4.55x
    - 24h: 59 calls (59 a day), hit rate 0.763, chance 0.186, naive rule 0.425, lift 4.10x
    - 7d: 409 calls (58 a day), hit rate 0.822, chance 0.184, naive rule 0.407, lift 4.46x
    - 30d: 1630 calls (54 a day), hit rate 0.823, chance 0.188, naive rule 0.403, lift 4.38x
  - next: threshold 0.4557, hit rate recent 0.517 / long run 0.4914
    - 6h: 6 calls (24 a day), hit rate 0.333, chance 0.178, lift 1.87x
    - 24h: 27 calls (27 a day), hit rate 0.556, chance 0.186, lift 2.99x
    - 7d: 604 calls (86 a day), hit rate 0.505, chance 0.184, lift 2.74x
    - 30d: 3050 calls (102 a day), hit rate 0.469, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.492; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 180, 0.668; 0.55: 141, 0.708; 0.60: 108, 0.754; 0.65: 77, 0.791; 0.70: 51, 0.828; 0.75: 30, 0.869; 0.80: 10, 0.891
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.388; 0.35: 254, 0.420; 0.40: 158, 0.455; 0.45: 68, 0.473; 0.50: 14, 0.494; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 127454, probability skill vs chance 0.2022, widened contest next: False
  - now: threshold 0.5649, hit rate recent 0.6908 / long run 0.6875
    - 6h: 15 calls (62 a day), hit rate 0.600, chance 0.103, naive rule 0.315, lift 5.83x
    - 24h: 53 calls (53 a day), hit rate 0.660, chance 0.119, naive rule 0.337, lift 5.55x
    - 7d: 383 calls (55 a day), hit rate 0.687, chance 0.122, naive rule 0.341, lift 5.65x
    - 30d: 1575 calls (53 a day), hit rate 0.690, chance 0.121, naive rule 0.333, lift 5.69x
  - next: threshold 0.3315, hit rate recent 0.3917 / long run 0.3872
    - 6h: 29 calls (119 a day), hit rate 0.345, chance 0.103, lift 3.35x
    - 24h: 85 calls (86 a day), hit rate 0.388, chance 0.119, lift 3.27x
    - 7d: 707 calls (101 a day), hit rate 0.390, chance 0.122, lift 3.21x
    - 30d: 2792 calls (93 a day), hit rate 0.384, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.430; 0.35: 190, 0.498; 0.40: 147, 0.549; 0.45: 112, 0.595; 0.50: 84, 0.638; 0.55: 61, 0.677; 0.60: 40, 0.710; 0.65: 23, 0.776; 0.70: 11, 0.810; 0.75: 2, 0.746
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.357; 0.35: 92, 0.384; 0.40: 30, 0.407; 0.45: 6, 0.429; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 127449, probability skill vs chance 0.1761, widened contest next: False
  - now: threshold 0.4106, hit rate recent 0.548 / long run 0.5573
    - 6h: 20 calls (83 a day), hit rate 0.450, chance 0.078, naive rule 0.292, lift 5.75x
    - 24h: 67 calls (68 a day), hit rate 0.552, chance 0.077, naive rule 0.273, lift 7.15x
    - 7d: 423 calls (61 a day), hit rate 0.558, chance 0.076, naive rule 0.280, lift 7.32x
    - 30d: 1656 calls (55 a day), hit rate 0.566, chance 0.077, naive rule 0.276, lift 7.33x
  - next: threshold 0.2934, hit rate recent 0.2917 / long run 0.3122
    - 6h: 21 calls (88 a day), hit rate 0.286, chance 0.078, lift 3.65x
    - 24h: 49 calls (50 a day), hit rate 0.286, chance 0.077, lift 3.70x
    - 7d: 391 calls (56 a day), hit rate 0.312, chance 0.076, lift 4.09x
    - 30d: 2019 calls (67 a day), hit rate 0.314, chance 0.077, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.442; 0.35: 90, 0.494; 0.40: 64, 0.549; 0.45: 42, 0.599; 0.50: 28, 0.655; 0.55: 17, 0.696; 0.60: 8, 0.737; 0.65: 2, 0.725; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.325; 0.35: 14, 0.355; 0.40: 3, 0.443; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 32.408 | 2.82% | 0.883 | 0.400 | 0.250 | 0.433 | 0.241 |
| 6h | 26.454 | 2.82% | 0.897 | 0.453 | 0.251 | 0.479 | 0.588 |
| 24h | 27.495 | 6.38% | 0.904 | 0.491 | 0.251 | 0.490 | 0.726 |
| 7d | 16.427 | 4.47% | 0.900 | 0.499 | 0.251 | 0.498 | 0.730 |
| 30d | 14.210 | 4.26% | 0.900 | 0.499 | 0.251 | 0.496 | 0.691 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 33.348 | 32.612 | 32.608 | 32.634 | 32.824 | 33.480 | 32.313 | 32.315 | 32.428 | 32.408 |
| 6h | 27.223 | 26.711 | 26.550 | 26.470 | 26.807 | 26.889 | 26.408 | 26.395 | 26.414 | 26.454 |
| 24h | 29.369 | 27.977 | 27.644 | 27.555 | 28.023 | 28.203 | 27.462 | 27.419 | 27.446 | 27.495 |
| 7d | 17.195 | 16.636 | 16.531 | 16.460 | 16.761 | 16.670 | 16.414 | 16.387 | 16.396 | 16.427 |
| 30d | 14.843 | 14.361 | 14.300 | 14.238 | 14.475 | 14.411 | 14.205 | 14.184 | 14.185 | 14.210 |

## Next candle

- candle starting 2026-10-30 16:25 UTC, last close 2231.67
- P(up) 0.5071, return quantiles (bp): {'05': -16.731, '10': -12.523, '25': -7.565, '40': -2.44, '50': 0.176, '60': 3.296, '75': 6.989, '90': 12.372, '95': 15.967}
- changepoint probability 0.0339, regime age 142.9 min
- agent weights: empirical 0.003, ewma 0.043, garch 0.118, har 0.176, bocpd 0.024, hmm 0.017, online_qr 0.294, lgbm 0.325

## Learning log

- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- HMM volatility states (sd, bp per minute): [3.95, 7.23, 20.79], current probabilities: [0.004, 0.397, 0.598]
- live generator: {'versions': 60, 'latest_effective': '2026-10-30 16:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.413, 'l_abs': 0.707, 'l_hi': 0.733, 'l_lo': 0.729, 'b05': 0.761, 'b25': 0.673, 'b75': 0.712, 'b95': 0.761}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.838, 1.542, 1.521, 2.123, 3.407, 3.473, 4.279, 4.829, 4.615, 4.948, 6.077, 6.212, 6.083, 7.404]}
- calibration offsets (in sigma): {'05': 0.012, '10': 0.004, '25': -0.1, '40': 0.006, '50': 0.01, '60': 0.084, '75': 0.07, '90': -0.014, '95': -0.072}
