# ETH-USD 60s candle generator - report

- generated: 2026-10-30 09:52 UTC
- last closed candle: 2026-10-30 09:52 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.539 (672) [0.504, 0.574] | 0.520 (2877) [0.502, 0.539] | 0.516 (5562) [0.503, 0.530] | 0.522 (2590) [0.501, 0.544] | 0.410 (39) | 0.500 | flat -0.003 (noise 0.032) |
| colour_clear | 0.522 (812) | 0.539 (5652) [0.533, 0.545] | 0.539 (23642) [0.532, 0.545] | 0.519 (45555) [0.513, 0.525] | 0.545 (21317) [0.541, 0.549] | 0.550 (289) | 0.500 | flat -0.016 (noise 0.009) |
| colour_confident | 0.588 (119) | 0.601 (1299) [0.586, 0.618] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.571 (35) | 0.500 | flat +0.003 (noise 0.020) |
| colour_next | 0.512 (1433) | 0.525 (10025) [0.521, 0.530] | 0.526 (42874) [0.522, 0.530] | 0.514 (82916) [0.510, 0.517] | 0.529 (38567) [0.525, 0.533] | 0.541 (591) | 0.500 | flat -0.010 (noise 0.007) |
| colour_path | 0.497 (20062) | 0.502 (140350) [0.500, 0.504] | 0.501 (600236) [0.499, 0.502] | 0.501 (1160824) [0.500, 0.502] | 0.501 (539938) [0.499, 0.502] | 0.498 (8274) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.789 (19) | 0.610 (408) [0.584, 0.648] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.500 (4) | 0.500 | flat -0.017 (noise 0.040) |
| reversal_k13_next | 0.261 (46) | 0.319 (407) [0.286, 0.358] | 0.312 (2054) [0.300, 0.325] | 0.308 (3893) [0.298, 0.319] | 0.318 (1788) [0.307, 0.330] | 0.200 (15) | 0.077 | flat +0.004 (noise 0.032) |
| reversal_k13_now | 0.522 (67) | 0.557 (420) [0.510, 0.605] | 0.564 (1641) [0.544, 0.585] | 0.572 (2962) [0.557, 0.587] | 0.563 (1490) [0.542, 0.586] | 0.600 (25) | 0.077 | flat +0.019 (noise 0.036) |
| reversal_k3_next | 0.595 (121) | 0.591 (673) [0.583, 0.601] | 0.581 (2921) [0.569, 0.593] | 0.584 (5118) [0.575, 0.594] | 0.581 (2678) [0.569, 0.594] | 0.605 (38) | 0.293 | flat +0.010 (noise 0.026) |
| reversal_k3_now | 1.000 (65) | 0.954 (411) [0.927, 0.978] | 0.936 (1740) [0.927, 0.947] | 0.939 (3322) [0.933, 0.946] | 0.936 (1559) [0.925, 0.947] | 0.875 (16) | 0.293 | flat +0.021 (noise 0.021) |
| reversal_k5_next | 0.537 (41) | 0.507 (675) [0.496, 0.518] | 0.468 (3060) [0.455, 0.483] | 0.479 (4724) [0.467, 0.491] | 0.467 (2734) [0.453, 0.482] | 0.636 (11) | 0.187 | up +0.065 (noise 0.025) |
| reversal_k5_now | 0.841 (69) | 0.830 (417) [0.819, 0.839] | 0.826 (1628) [0.815, 0.836] | 0.831 (3075) [0.821, 0.841] | 0.823 (1464) [0.811, 0.834] | 0.647 (17) | 0.187 | flat +0.003 (noise 0.027) |
| reversal_k8_next | 0.394 (94) | 0.395 (737) [0.375, 0.412] | 0.384 (2774) [0.371, 0.396] | 0.389 (4712) [0.379, 0.400] | 0.384 (2606) [0.371, 0.397] | 0.367 (30) | 0.121 | flat +0.035 (noise 0.025) |
| reversal_k8_now | 0.754 (57) | 0.688 (388) [0.632, 0.741] | 0.692 (1568) [0.671, 0.712] | 0.702 (3016) [0.687, 0.718] | 0.689 (1429) [0.667, 0.712] | 0.556 (18) | 0.121 | flat +0.011 (noise 0.041) |
| overall | 0.500 (22151) | 0.506 (155175) [0.504, 0.508] | 0.504 (663373) [0.503, 0.506] | 0.503 (1280124) [0.502, 0.504] | 0.504 (596843) [0.503, 0.506] | 0.502 (9074) | - | flat +0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08228, 0.1249] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5249, 'levels': [{'threshold': 0.08228, 'calls_per_day': 144.1, 'win_rate': 0.6075}, {'threshold': 0.1249, 'calls_per_day': 36.1, 'win_rate': 0.6063}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 38017, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15078 | 0.340 | 0.522 (14852) | 0.582 (1988) | 0.751 (2575) |
| volatility: normal | 15077 | 0.366 | 0.532 (15012) | 0.614 (1356) | 0.752 (2267) |
| volatility: wild | 15077 | 0.380 | 0.523 (15037) | 0.631 (712) | 0.767 (2041) |
| session: Asia 00-08 | 15360 | 0.361 | 0.531 (15259) | 0.603 (1454) | 0.754 (2314) |
| session: Europe 08-13 | 9412 | 0.358 | 0.529 (9327) | 0.592 (1002) | 0.751 (1523) |
| session: US 13-21 | 14880 | 0.370 | 0.521 (14789) | 0.600 (1035) | 0.765 (2180) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5526) | 0.612 (565) | 0.749 (866) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.403 | 0.394 | 0.256 | 0.256 | 0.542 | 0.296 | 0.510 | 1.187 |
| 6h | 360 | 0.390 | 0.383 | 0.296 | 0.326 | 0.543 | 0.273 | 0.507 | 1.171 |
| 24h | 1440 | 0.383 | 0.377 | 0.303 | 0.342 | 0.515 | 0.263 | 0.502 | 1.220 |
| 7d | 10080 | 0.368 | 0.360 | 0.283 | 0.316 | 0.525 | 0.264 | 0.472 | 1.241 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.307 | 0.526 | 0.259 | 0.465 | 1.275 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.403 / 0.542 / 0.883; 2: 0.355 / 0.424 / 0.867; 3: 0.380 / 0.492 / 0.867; 4: 0.362 / 0.492 / 0.917; 5: 0.395 / 0.492 / 0.900; 6: 0.364 / 0.458 / 0.933; 7: 0.372 / 0.407 / 0.933; 8: 0.382 / 0.542 / 0.950; 9: 0.389 / 0.525 / 0.983; 10: 0.385 / 0.525 / 0.967; 11: 0.384 / 0.542 / 0.983; 12: 0.381 / 0.475 / 1.000; 13: 0.372 / 0.508 / 1.000; 14: 0.384 / 0.508 / 1.000; 15: 0.387 / 0.492 / 1.000
- 6h: 1: 0.390 / 0.543 / 0.903; 2: 0.367 / 0.432 / 0.875; 3: 0.376 / 0.510 / 0.808; 4: 0.373 / 0.474 / 0.847; 5: 0.385 / 0.526 / 0.864; 6: 0.380 / 0.524 / 0.922; 7: 0.379 / 0.474 / 0.903; 8: 0.379 / 0.515 / 0.922; 9: 0.373 / 0.487 / 0.933; 10: 0.375 / 0.499 / 0.911; 11: 0.378 / 0.535 / 0.928; 12: 0.376 / 0.476 / 0.961; 13: 0.368 / 0.487 / 0.944; 14: 0.379 / 0.507 / 0.953; 15: 0.373 / 0.471 / 0.972
- 24h: 1: 0.383 / 0.515 / 0.898; 2: 0.372 / 0.494 / 0.899; 3: 0.371 / 0.505 / 0.887; 4: 0.372 / 0.506 / 0.898; 5: 0.369 / 0.506 / 0.897; 6: 0.368 / 0.504 / 0.906; 7: 0.375 / 0.503 / 0.906; 8: 0.365 / 0.496 / 0.903; 9: 0.362 / 0.478 / 0.908; 10: 0.368 / 0.498 / 0.904; 11: 0.368 / 0.508 / 0.906; 12: 0.362 / 0.479 / 0.911; 13: 0.367 / 0.499 / 0.905; 14: 0.362 / 0.493 / 0.907; 15: 0.362 / 0.486 / 0.914
- 7d: 1: 0.368 / 0.525 / 0.899; 2: 0.355 / 0.491 / 0.900; 3: 0.359 / 0.510 / 0.898; 4: 0.355 / 0.500 / 0.899; 5: 0.355 / 0.504 / 0.900; 6: 0.352 / 0.502 / 0.901; 7: 0.355 / 0.502 / 0.901; 8: 0.354 / 0.508 / 0.900; 9: 0.353 / 0.500 / 0.901; 10: 0.354 / 0.504 / 0.901; 11: 0.351 / 0.503 / 0.901; 12: 0.353 / 0.501 / 0.902; 13: 0.351 / 0.501 / 0.902; 14: 0.351 / 0.501 / 0.902; 15: 0.351 / 0.499 / 0.903
- 30d: 1: 0.362 / 0.526 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.901; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.346 / 0.497 / 0.901; 10: 0.348 / 0.506 / 0.901; 11: 0.346 / 0.499 / 0.901; 12: 0.347 / 0.503 / 0.901; 13: 0.346 / 0.500 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.346 / 0.498 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.188 (body 0.126, range 0.249); 'price stays where it was' would score 0.174; colour right 0.559; typical miss of the close 8.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.155 (body 0.114, range 0.196); 'price stays where it was' would score 0.162; colour right 0.552; typical miss of the close 9.7 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.133 (body 0.089, range 0.178); 'price stays where it was' would score 0.137; colour right 0.501; typical miss of the close 13.4 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.130 (body 0.088, range 0.171); 'price stays where it was' would score 0.137; colour right 0.498; typical miss of the close 8.9 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 7.9 bp; chain ended on the right side 0.519 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.0; 2: 0.200 / 4.7; 3: 0.168 / 6.2; 4: 0.132 / 6.6; 5: 0.127 / 7.3; 6: 0.114 / 7.8; 7: 0.111 / 8.1; 8: 0.098 / 8.7; 9: 0.088 / 8.8; 10: 0.087 / 9.3; 11: 0.085 / 9.8; 12: 0.076 / 10.1; 13: 0.068 / 10.3; 14: 0.071 / 10.7; 15: 0.062 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 127066, probability skill vs chance 0.2387, widened contest next: False
  - now: threshold 0.8347, hit rate recent 0.954 / long run 0.9428
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.300, naive rule 0.507, lift 3.00x
    - 24h: 55 calls (55 a day), hit rate 0.964, chance 0.300, naive rule 0.510, lift 3.21x
    - 7d: 402 calls (57 a day), hit rate 0.948, chance 0.293, naive rule 0.498, lift 3.23x
    - 30d: 1738 calls (58 a day), hit rate 0.936, chance 0.294, naive rule 0.492, lift 3.19x
  - next: threshold 0.5296, hit rate recent 0.6229 / long run 0.5904
    - 6h: 25 calls (101 a day), hit rate 0.560, chance 0.300, lift 1.87x
    - 24h: 104 calls (104 a day), hit rate 0.644, chance 0.300, lift 2.15x
    - 7d: 676 calls (97 a day), hit rate 0.595, chance 0.293, lift 2.03x
    - 30d: 2918 calls (97 a day), hit rate 0.581, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.496; 0.35: 536, 0.521; 0.40: 476, 0.578; 0.45: 407, 0.649; 0.50: 356, 0.700; 0.55: 312, 0.741; 0.60: 263, 0.787; 0.65: 220, 0.812; 0.70: 174, 0.845; 0.75: 137, 0.878; 0.80: 92, 0.914; 0.85: 47, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.465; 0.40: 407, 0.498; 0.45: 310, 0.533; 0.50: 199, 0.569; 0.55: 88, 0.570; 0.60: 13, 0.636; 0.65: 1, 0.607
- **K=5**: model 1792540800, labels learned 127064, probability skill vs chance 0.2261, widened contest next: False
  - now: threshold 0.6786, hit rate recent 0.7946 / long run 0.8223
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.195, naive rule 0.408, lift 3.07x
    - 24h: 64 calls (64 a day), hit rate 0.781, chance 0.195, naive rule 0.438, lift 4.01x
    - 7d: 407 calls (58 a day), hit rate 0.821, chance 0.186, naive rule 0.409, lift 4.42x
    - 30d: 1626 calls (54 a day), hit rate 0.823, chance 0.188, naive rule 0.403, lift 4.38x
  - next: threshold 0.4565, hit rate recent 0.5379 / long run 0.4929
    - 6h: 6 calls (24 a day), hit rate 0.500, chance 0.195, lift 2.56x
    - 24h: 32 calls (32 a day), hit rate 0.625, chance 0.195, lift 3.21x
    - 7d: 626 calls (89 a day), hit rate 0.510, chance 0.186, lift 2.74x
    - 30d: 3056 calls (102 a day), hit rate 0.469, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 346, 0.492; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 180, 0.669; 0.55: 141, 0.709; 0.60: 108, 0.754; 0.65: 77, 0.790; 0.70: 51, 0.827; 0.75: 30, 0.867; 0.80: 10, 0.891
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.389; 0.35: 254, 0.420; 0.40: 158, 0.456; 0.45: 69, 0.473; 0.50: 14, 0.494; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 127061, probability skill vs chance 0.2073, widened contest next: False
  - now: threshold 0.5652, hit rate recent 0.7161 / long run 0.6897
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.134, naive rule 0.338, lift 4.47x
    - 24h: 53 calls (53 a day), hit rate 0.736, chance 0.128, naive rule 0.359, lift 5.75x
    - 7d: 383 calls (55 a day), hit rate 0.679, chance 0.122, naive rule 0.342, lift 5.58x
    - 30d: 1571 calls (52 a day), hit rate 0.689, chance 0.122, naive rule 0.334, lift 5.67x
  - next: threshold 0.3336, hit rate recent 0.4171 / long run 0.3892
    - 6h: 22 calls (91 a day), hit rate 0.455, chance 0.134, lift 3.38x
    - 24h: 82 calls (83 a day), hit rate 0.439, chance 0.128, lift 3.43x
    - 7d: 706 calls (101 a day), hit rate 0.392, chance 0.122, lift 3.22x
    - 30d: 2773 calls (92 a day), hit rate 0.384, chance 0.122, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 189, 0.498; 0.40: 147, 0.549; 0.45: 112, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.676; 0.60: 40, 0.710; 0.65: 23, 0.773; 0.70: 11, 0.804; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.357; 0.35: 92, 0.384; 0.40: 30, 0.406; 0.45: 6, 0.432; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 127056, probability skill vs chance 0.1825, widened contest next: False
  - now: threshold 0.4105, hit rate recent 0.5888 / long run 0.561
    - 6h: 16 calls (67 a day), hit rate 0.625, chance 0.070, naive rule 0.237, lift 8.98x
    - 24h: 66 calls (67 a day), hit rate 0.606, chance 0.080, naive rule 0.288, lift 7.61x
    - 7d: 419 calls (60 a day), hit rate 0.556, chance 0.076, naive rule 0.280, lift 7.30x
    - 30d: 1648 calls (55 a day), hit rate 0.566, chance 0.077, naive rule 0.277, lift 7.32x
  - next: threshold 0.2941, hit rate recent 0.2866 / long run 0.3126
    - 6h: 11 calls (46 a day), hit rate 0.273, chance 0.070, lift 3.92x
    - 24h: 43 calls (43 a day), hit rate 0.279, chance 0.080, lift 3.50x
    - 7d: 389 calls (56 a day), hit rate 0.308, chance 0.076, lift 4.05x
    - 30d: 2023 calls (67 a day), hit rate 0.313, chance 0.077, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.442; 0.35: 90, 0.494; 0.40: 64, 0.550; 0.45: 42, 0.598; 0.50: 28, 0.653; 0.55: 17, 0.692; 0.60: 8, 0.738; 0.65: 2, 0.735; 0.70: 0, 0.429
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.356; 0.40: 2, 0.447; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 18.346 | 0.60% | 0.883 | 0.467 | 0.250 | 0.525 | -0.083 |
| 6h | 17.323 | 2.42% | 0.894 | 0.450 | 0.251 | 0.510 | 0.302 |
| 24h | 25.618 | 6.87% | 0.899 | 0.501 | 0.251 | 0.500 | 0.742 |
| 7d | 16.152 | 4.51% | 0.900 | 0.501 | 0.251 | 0.499 | 0.728 |
| 30d | 14.171 | 4.32% | 0.900 | 0.500 | 0.251 | 0.496 | 0.690 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 18.456 | 18.300 | 18.465 | 18.468 | 18.437 | 18.519 | 18.260 | 18.089 | 18.252 | 18.346 |
| 6h | 17.753 | 17.408 | 17.371 | 17.509 | 17.632 | 17.419 | 17.267 | 17.276 | 17.296 | 17.323 |
| 24h | 27.508 | 26.091 | 25.774 | 25.678 | 26.153 | 26.264 | 25.604 | 25.567 | 25.583 | 25.618 |
| 7d | 16.915 | 16.357 | 16.255 | 16.186 | 16.490 | 16.385 | 16.138 | 16.110 | 16.121 | 16.152 |
| 30d | 14.811 | 14.322 | 14.260 | 14.199 | 14.436 | 14.370 | 14.166 | 14.145 | 14.145 | 14.171 |

## Next candle

- candle starting 2026-10-30 09:52 UTC, last close 2225.11
- P(up) 0.5006, return quantiles (bp): {'05': -9.623, '10': -7.326, '25': -3.753, '40': -1.363, '50': 0.032, '60': 0.99, '75': 3.489, '90': 6.68, '95': 9.261}
- changepoint probability 0.0405, regime age 125.6 min
- agent weights: empirical 0.003, ewma 0.030, garch 0.126, har 0.157, bocpd 0.017, hmm 0.018, online_qr 0.297, lgbm 0.353

## Learning log

- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.9, 7.28, 18.78], current probabilities: [0.309, 0.676, 0.015]
- live generator: {'versions': 60, 'latest_effective': '2026-10-30 10:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.358, 'l_abs': 0.698, 'l_hi': 0.729, 'l_lo': 0.73, 'b05': 0.764, 'b25': 0.688, 'b75': 0.688, 'b95': 0.761}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.2, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.6], [1.2, 1.8], [1.2, 1.8], [1.2, 1.6], [1.2, 1.8], [1.2, 1.8], [1.2, 1.8], [1.2, 1.6], [1.2, 1.6]], 'cone_width': [1.426, 2.771, 2.423, 2.268, 1.919, 2.25, 2.363, 2.272, 2.652, 2.625, 2.388, 2.698, 2.75, 2.581]}
- calibration offsets (in sigma): {'05': 0.0055, '10': -0.019, '25': -0.0125, '40': -0.006, '50': 0.005, '60': -0.014, '75': -0.0075, '90': -0.091, '95': -0.0755}
