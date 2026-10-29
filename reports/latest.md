# ETH-USD 60s candle generator - report

- generated: 2026-10-29 19:48 UTC
- last closed candle: 2026-10-29 19:48 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.537 (672) [0.501, 0.573] | 0.520 (2876) [0.501, 0.539] | 0.517 (5466) [0.503, 0.531] | 0.524 (2494) [0.504, 0.546] | 0.481 (79) | 0.500 | flat -0.006 (noise 0.031) |
| colour_clear | 0.537 (786) | 0.542 (5666) [0.539, 0.547] | 0.538 (23626) [0.531, 0.545] | 0.519 (44743) [0.513, 0.525] | 0.546 (20505) [0.541, 0.550] | 0.530 (670) | 0.500 | flat -0.013 (noise 0.009) |
| colour_confident | 0.567 (120) | 0.601 (1315) [0.586, 0.617] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.589 (107) | 0.500 | flat +0.001 (noise 0.021) |
| colour_next | 0.531 (1431) | 0.528 (10027) [0.525, 0.531] | 0.526 (42877) [0.521, 0.530] | 0.514 (81483) [0.510, 0.518] | 0.529 (37134) [0.526, 0.533] | 0.525 (1181) | 0.500 | flat -0.006 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.502 (140378) [0.500, 0.504] | 0.501 (600278) [0.499, 0.502] | 0.501 (1140762) [0.500, 0.502] | 0.501 (519876) [0.499, 0.502] | 0.496 (16534) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.500 (32) | 0.607 (405) [0.583, 0.639] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.750 (16) | 0.500 | flat -0.024 (noise 0.040) |
| reversal_k13_next | 0.302 (53) | 0.317 (410) [0.283, 0.357] | 0.310 (2116) [0.298, 0.323] | 0.309 (3847) [0.299, 0.320] | 0.320 (1742) [0.308, 0.332] | 0.270 (37) | 0.077 | flat -0.007 (noise 0.032) |
| reversal_k13_now | 0.603 (63) | 0.568 (391) [0.519, 0.620] | 0.562 (1632) [0.542, 0.584] | 0.573 (2895) [0.558, 0.589] | 0.565 (1423) [0.543, 0.589] | 0.500 (56) | 0.077 | flat +0.043 (noise 0.036) |
| reversal_k3_next | 0.591 (115) | 0.593 (648) [0.584, 0.603] | 0.583 (2896) [0.572, 0.596] | 0.584 (4997) [0.574, 0.594] | 0.580 (2557) [0.568, 0.594] | 0.570 (107) | 0.293 | flat +0.016 (noise 0.026) |
| reversal_k3_now | 0.909 (66) | 0.942 (399) [0.918, 0.964] | 0.935 (1742) [0.926, 0.945] | 0.938 (3257) [0.931, 0.945] | 0.934 (1494) [0.923, 0.944] | 1.000 (50) | 0.293 | flat +0.010 (noise 0.021) |
| reversal_k5_next | 0.500 (64) | 0.501 (766) [0.491, 0.512] | 0.468 (3071) [0.455, 0.482] | 0.478 (4683) [0.466, 0.491] | 0.466 (2693) [0.452, 0.481] | 0.543 (35) | 0.187 | up +0.067 (noise 0.024) |
| reversal_k5_now | 0.838 (74) | 0.828 (389) [0.816, 0.837] | 0.826 (1616) [0.814, 0.837] | 0.830 (3006) [0.820, 0.840] | 0.822 (1395) [0.810, 0.834] | 0.836 (55) | 0.187 | flat +0.011 (noise 0.028) |
| reversal_k8_next | 0.446 (101) | 0.387 (744) [0.364, 0.410] | 0.384 (2742) [0.371, 0.397] | 0.389 (4618) [0.378, 0.400] | 0.383 (2512) [0.369, 0.396] | 0.388 (80) | 0.120 | flat +0.022 (noise 0.025) |
| reversal_k8_now | 0.770 (61) | 0.683 (369) [0.628, 0.736] | 0.689 (1559) [0.667, 0.709] | 0.701 (2959) [0.686, 0.716] | 0.687 (1372) [0.663, 0.710] | 0.750 (44) | 0.121 | flat +0.016 (noise 0.038) |
| overall | 0.508 (22158) | 0.506 (155193) [0.503, 0.508] | 0.504 (663405) [0.503, 0.506] | 0.503 (1257973) [0.502, 0.504] | 0.504 (574692) [0.503, 0.506] | 0.501 (18258) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08204, 0.1244] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5264, 'levels': [{'threshold': 0.08204, 'calls_per_day': 146.3, 'win_rate': 0.6087}, {'threshold': 0.1244, 'calls_per_day': 36.5, 'win_rate': 0.607}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 37175, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15276 | 0.341 | 0.522 (15049) | 0.584 (2006) | 0.752 (2589) |
| volatility: normal | 15276 | 0.366 | 0.530 (15209) | 0.611 (1325) | 0.751 (2268) |
| volatility: wild | 15276 | 0.380 | 0.523 (15234) | 0.633 (678) | 0.771 (2051) |
| session: Asia 00-08 | 15360 | 0.361 | 0.531 (15257) | 0.605 (1425) | 0.759 (2293) |
| session: Europe 08-13 | 9600 | 0.358 | 0.529 (9514) | 0.590 (996) | 0.749 (1541) |
| session: US 13-21 | 15288 | 0.370 | 0.521 (15195) | 0.601 (1031) | 0.766 (2227) |
| session: late 21-24 | 5580 | 0.351 | 0.516 (5526) | 0.610 (557) | 0.744 (847) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.433 | 0.396 | 0.313 | 0.313 | 0.593 | 0.335 | 0.531 | 1.389 |
| 6h | 360 | 0.394 | 0.388 | 0.311 | 0.363 | 0.521 | 0.279 | 0.510 | 1.263 |
| 24h | 1440 | 0.373 | 0.371 | 0.289 | 0.320 | 0.533 | 0.265 | 0.481 | 1.241 |
| 7d | 10080 | 0.367 | 0.359 | 0.280 | 0.312 | 0.528 | 0.265 | 0.470 | 1.244 |
| 30d | 43200 | 0.362 | 0.354 | 0.277 | 0.306 | 0.526 | 0.259 | 0.464 | 1.276 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.433 / 0.593 / 0.933; 2: 0.363 / 0.356 / 0.950; 3: 0.401 / 0.593 / 0.950; 4: 0.391 / 0.492 / 0.983; 5: 0.385 / 0.593 / 0.967; 6: 0.405 / 0.559 / 0.967; 7: 0.383 / 0.475 / 0.967; 8: 0.357 / 0.407 / 0.850; 9: 0.392 / 0.475 / 0.950; 10: 0.450 / 0.661 / 0.933; 11: 0.384 / 0.475 / 0.933; 12: 0.389 / 0.508 / 0.883; 13: 0.375 / 0.508 / 0.883; 14: 0.381 / 0.475 / 0.900; 15: 0.379 / 0.492 / 0.883
- 6h: 1: 0.394 / 0.521 / 0.906; 2: 0.384 / 0.518 / 0.894; 3: 0.383 / 0.524 / 0.925; 4: 0.379 / 0.496 / 0.931; 5: 0.384 / 0.521 / 0.911; 6: 0.379 / 0.485 / 0.900; 7: 0.383 / 0.490 / 0.872; 8: 0.367 / 0.465 / 0.803; 9: 0.374 / 0.482 / 0.850; 10: 0.387 / 0.510 / 0.844; 11: 0.383 / 0.513 / 0.833; 12: 0.368 / 0.474 / 0.794; 13: 0.380 / 0.515 / 0.808; 14: 0.372 / 0.487 / 0.800; 15: 0.375 / 0.515 / 0.800
- 24h: 1: 0.373 / 0.533 / 0.907; 2: 0.362 / 0.507 / 0.899; 3: 0.361 / 0.502 / 0.897; 4: 0.361 / 0.495 / 0.898; 5: 0.360 / 0.508 / 0.901; 6: 0.355 / 0.491 / 0.895; 7: 0.363 / 0.497 / 0.892; 8: 0.357 / 0.506 / 0.887; 9: 0.357 / 0.493 / 0.897; 10: 0.362 / 0.502 / 0.899; 11: 0.357 / 0.493 / 0.894; 12: 0.354 / 0.487 / 0.887; 13: 0.352 / 0.488 / 0.887; 14: 0.361 / 0.505 / 0.883; 15: 0.354 / 0.499 / 0.884
- 7d: 1: 0.367 / 0.528 / 0.899; 2: 0.354 / 0.494 / 0.899; 3: 0.358 / 0.511 / 0.900; 4: 0.353 / 0.497 / 0.900; 5: 0.354 / 0.505 / 0.900; 6: 0.351 / 0.502 / 0.900; 7: 0.353 / 0.500 / 0.899; 8: 0.353 / 0.507 / 0.899; 9: 0.352 / 0.500 / 0.900; 10: 0.354 / 0.506 / 0.900; 11: 0.351 / 0.503 / 0.900; 12: 0.352 / 0.503 / 0.899; 13: 0.349 / 0.500 / 0.900; 14: 0.351 / 0.501 / 0.899; 15: 0.350 / 0.500 / 0.899
- 30d: 1: 0.362 / 0.526 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.899; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.504 / 0.899; 13: 0.346 / 0.501 / 0.899; 14: 0.346 / 0.499 / 0.899; 15: 0.346 / 0.499 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.127 (body 0.086, range 0.168); 'price stays where it was' would score 0.097; colour right 0.542; typical miss of the close 8.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.139 (body 0.091, range 0.187); 'price stays where it was' would score 0.133; colour right 0.499; typical miss of the close 12.6 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.125 (body 0.083, range 0.168); 'price stays where it was' would score 0.127; colour right 0.502; typical miss of the close 10.1 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.135; colour right 0.496; typical miss of the close 8.5 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.129; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.522 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.199 / 4.6; 3: 0.167 / 6.1; 4: 0.133 / 6.5; 5: 0.126 / 7.2; 6: 0.113 / 7.7; 7: 0.109 / 8.1; 8: 0.097 / 8.5; 9: 0.086 / 8.6; 10: 0.088 / 9.2; 11: 0.085 / 9.7; 12: 0.077 / 9.9; 13: 0.068 / 10.1; 14: 0.072 / 10.5; 15: 0.063 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 126222, probability skill vs chance 0.2387, widened contest next: False
  - now: threshold 0.8346, hit rate recent 0.9701 / long run 0.9432
    - 6h: 15 calls (61 a day), hit rate 1.000, chance 0.293, naive rule 0.500, lift 3.41x
    - 24h: 61 calls (61 a day), hit rate 1.000, chance 0.282, naive rule 0.479, lift 3.54x
    - 7d: 404 calls (58 a day), hit rate 0.953, chance 0.293, naive rule 0.496, lift 3.26x
    - 30d: 1736 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5306, hit rate recent 0.5985 / long run 0.5848
    - 6h: 25 calls (101 a day), hit rate 0.640, chance 0.293, lift 2.18x
    - 24h: 127 calls (127 a day), hit rate 0.567, chance 0.282, lift 2.01x
    - 7d: 671 calls (96 a day), hit rate 0.587, chance 0.293, lift 2.01x
    - 30d: 2922 calls (97 a day), hit rate 0.581, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 536, 0.520; 0.40: 476, 0.577; 0.45: 407, 0.649; 0.50: 356, 0.699; 0.55: 311, 0.740; 0.60: 263, 0.785; 0.65: 221, 0.811; 0.70: 174, 0.844; 0.75: 137, 0.877; 0.80: 92, 0.914; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 500, 0.465; 0.40: 407, 0.498; 0.45: 310, 0.533; 0.50: 200, 0.569; 0.55: 89, 0.572; 0.60: 13, 0.633; 0.65: 1, 0.621
- **K=5**: model 1792540800, labels learned 126220, probability skill vs chance 0.2299, widened contest next: False
  - now: threshold 0.677, hit rate recent 0.8378 / long run 0.8266
    - 6h: 21 calls (86 a day), hit rate 0.810, chance 0.198, naive rule 0.448, lift 4.08x
    - 24h: 67 calls (67 a day), hit rate 0.866, chance 0.185, naive rule 0.409, lift 4.67x
    - 7d: 409 calls (58 a day), hit rate 0.831, chance 0.186, naive rule 0.408, lift 4.47x
    - 30d: 1621 calls (54 a day), hit rate 0.826, chance 0.188, naive rule 0.403, lift 4.39x
  - next: threshold 0.4573, hit rate recent 0.5219 / long run 0.4902
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.198, lift 3.53x
    - 24h: 44 calls (44 a day), hit rate 0.500, chance 0.185, lift 2.70x
    - 7d: 693 calls (99 a day), hit rate 0.506, chance 0.186, lift 2.73x
    - 30d: 3062 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.493; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 180, 0.668; 0.55: 140, 0.708; 0.60: 107, 0.753; 0.65: 76, 0.791; 0.70: 51, 0.830; 0.75: 30, 0.871; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.391; 0.35: 254, 0.421; 0.40: 159, 0.457; 0.45: 69, 0.472; 0.50: 14, 0.490; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 126217, probability skill vs chance 0.2109, widened contest next: False
  - now: threshold 0.563, hit rate recent 0.7648 / long run 0.6921
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.136, naive rule 0.391, lift 6.23x
    - 24h: 52 calls (52 a day), hit rate 0.788, chance 0.127, naive rule 0.346, lift 6.21x
    - 7d: 379 calls (54 a day), hit rate 0.689, chance 0.121, naive rule 0.339, lift 5.68x
    - 30d: 1561 calls (52 a day), hit rate 0.691, chance 0.121, naive rule 0.334, lift 5.69x
  - next: threshold 0.3438, hit rate recent 0.435 / long run 0.3893
    - 6h: 22 calls (91 a day), hit rate 0.500, chance 0.136, lift 3.68x
    - 24h: 98 calls (99 a day), hit rate 0.408, chance 0.127, lift 3.22x
    - 7d: 740 calls (106 a day), hit rate 0.396, chance 0.121, lift 3.27x
    - 30d: 2771 calls (92 a day), hit rate 0.384, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 189, 0.498; 0.40: 146, 0.548; 0.45: 112, 0.595; 0.50: 84, 0.637; 0.55: 60, 0.677; 0.60: 40, 0.712; 0.65: 23, 0.775; 0.70: 10, 0.813; 0.75: 2, 0.800
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.356; 0.35: 93, 0.384; 0.40: 31, 0.406; 0.45: 6, 0.419; 0.50: 1, 0.655
- **K=13**: model 1793059200, labels learned 126212, probability skill vs chance 0.1891, widened contest next: False
  - now: threshold 0.4078, hit rate recent 0.5607 / long run 0.5578
    - 6h: 18 calls (75 a day), hit rate 0.611, chance 0.094, naive rule 0.322, lift 6.49x
    - 24h: 64 calls (65 a day), hit rate 0.562, chance 0.080, naive rule 0.292, lift 7.06x
    - 7d: 414 calls (59 a day), hit rate 0.558, chance 0.076, naive rule 0.280, lift 7.34x
    - 30d: 1636 calls (55 a day), hit rate 0.564, chance 0.077, naive rule 0.277, lift 7.31x
  - next: threshold 0.295, hit rate recent 0.322 / long run 0.3168
    - 6h: 10 calls (42 a day), hit rate 0.500, chance 0.094, lift 5.31x
    - 24h: 44 calls (44 a day), hit rate 0.318, chance 0.080, lift 3.99x
    - 7d: 408 calls (58 a day), hit rate 0.321, chance 0.076, lift 4.22x
    - 30d: 2062 calls (69 a day), hit rate 0.312, chance 0.077, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 125, 0.442; 0.35: 90, 0.494; 0.40: 64, 0.549; 0.45: 42, 0.598; 0.50: 27, 0.656; 0.55: 16, 0.697; 0.60: 8, 0.748; 0.65: 2, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.354; 0.40: 2, 0.453; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.419 | 1.73% | 0.933 | 0.583 | 0.247 | 0.576 | 0.108 |
| 6h | 19.798 | 2.04% | 0.911 | 0.514 | 0.250 | 0.518 | 0.470 |
| 24h | 16.655 | 2.76% | 0.898 | 0.499 | 0.250 | 0.517 | 0.596 |
| 7d | 14.629 | 3.57% | 0.900 | 0.500 | 0.251 | 0.499 | 0.650 |
| 30d | 13.772 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.665 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.637 | 12.524 | 12.453 | 12.651 | 12.789 | 12.512 | 12.328 | 12.355 | 12.408 | 12.419 |
| 6h | 20.211 | 19.819 | 19.849 | 19.895 | 19.983 | 19.913 | 19.792 | 19.810 | 19.783 | 19.798 |
| 24h | 17.127 | 16.781 | 16.718 | 16.678 | 16.960 | 16.766 | 16.641 | 16.652 | 16.631 | 16.655 |
| 7d | 15.171 | 14.778 | 14.717 | 14.655 | 14.917 | 14.781 | 14.615 | 14.593 | 14.600 | 14.629 |
| 30d | 14.362 | 13.909 | 13.857 | 13.798 | 14.027 | 13.953 | 13.767 | 13.747 | 13.747 | 13.772 |

## Next candle

- candle starting 2026-10-29 19:48 UTC, last close 2332.03
- P(up) 0.5267, return quantiles (bp): {'05': -7.785, '10': -5.561, '25': -2.938, '40': -0.852, '50': 0.303, '60': 1.432, '75': 3.07, '90': 5.591, '95': 7.635}
- changepoint probability 0.0473, regime age 66.6 min
- agent weights: empirical 0.009, ewma 0.094, garch 0.145, har 0.145, bocpd 0.026, hmm 0.090, online_qr 0.245, lgbm 0.245

## Learning log

- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.69, 15.08], current probabilities: [0.835, 0.161, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-29 20:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.254, 'l_abs': 0.725, 'l_hi': 0.734, 'l_lo': 0.759, 'b05': 0.717, 'b25': 0.729, 'b75': 0.604, 'b95': 0.701}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.557, 1.799, 2.04, 2.427, 2.944, 3.522, 4.516, 3.776, 3.832, 4.362, 5.576, 5.368, 6.047, 6.272]}
- calibration offsets (in sigma): {'05': 0.0435, '10': 0.057, '25': 0.0075, '40': 0.028, '50': 0.045, '60': 0.052, '75': 0.0125, '90': -0.037, '95': -0.0235}
