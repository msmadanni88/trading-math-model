# ETH-USD 60s candle generator - report

- generated: 2026-10-29 01:19 UTC
- last closed candle: 2026-10-29 01:19 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.537 (672) [0.501, 0.573] | 0.520 (2876) [0.501, 0.539] | 0.517 (5466) [0.503, 0.531] | 0.524 (2494) [0.504, 0.546] | 0.200 (5) | 0.500 | flat -0.006 (noise 0.031) |
| colour_clear | 0.537 (786) | 0.542 (5666) [0.539, 0.547] | 0.538 (23626) [0.531, 0.545] | 0.519 (44743) [0.513, 0.525] | 0.546 (20505) [0.541, 0.550] | 0.477 (44) | 0.500 | flat -0.013 (noise 0.009) |
| colour_confident | 0.567 (120) | 0.601 (1315) [0.586, 0.617] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.375 (8) | 0.500 | flat +0.001 (noise 0.021) |
| colour_next | 0.531 (1431) | 0.528 (10027) [0.525, 0.531] | 0.526 (42877) [0.521, 0.530] | 0.514 (81483) [0.510, 0.518] | 0.529 (37134) [0.526, 0.533] | 0.456 (79) | 0.500 | flat -0.006 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.502 (140378) [0.500, 0.504] | 0.501 (600278) [0.499, 0.502] | 0.501 (1140762) [0.500, 0.502] | 0.501 (519876) [0.499, 0.502] | 0.495 (1106) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.500 (32) | 0.607 (405) [0.583, 0.639] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | - | 0.500 | flat -0.024 (noise 0.040) |
| reversal_k13_next | 0.302 (53) | 0.317 (410) [0.283, 0.357] | 0.310 (2116) [0.298, 0.323] | 0.309 (3847) [0.299, 0.320] | 0.320 (1742) [0.308, 0.332] | - | 0.077 | flat -0.007 (noise 0.032) |
| reversal_k13_now | 0.603 (63) | 0.568 (391) [0.519, 0.620] | 0.562 (1632) [0.542, 0.584] | 0.573 (2895) [0.558, 0.589] | 0.565 (1423) [0.543, 0.589] | 1.000 (2) | 0.077 | flat +0.043 (noise 0.036) |
| reversal_k3_next | 0.591 (115) | 0.593 (648) [0.584, 0.603] | 0.583 (2896) [0.572, 0.596] | 0.584 (4997) [0.574, 0.594] | 0.580 (2557) [0.568, 0.594] | 0.545 (11) | 0.293 | flat +0.016 (noise 0.026) |
| reversal_k3_now | 0.909 (66) | 0.942 (399) [0.918, 0.964] | 0.935 (1742) [0.926, 0.945] | 0.938 (3257) [0.931, 0.945] | 0.934 (1494) [0.923, 0.944] | 1.000 (5) | 0.293 | flat +0.010 (noise 0.021) |
| reversal_k5_next | 0.500 (64) | 0.501 (766) [0.491, 0.512] | 0.468 (3071) [0.455, 0.482] | 0.478 (4683) [0.466, 0.491] | 0.466 (2693) [0.452, 0.481] | 0.571 (7) | 0.187 | up +0.067 (noise 0.024) |
| reversal_k5_now | 0.838 (74) | 0.828 (389) [0.816, 0.837] | 0.826 (1616) [0.814, 0.837] | 0.830 (3006) [0.820, 0.840] | 0.822 (1395) [0.810, 0.834] | 0.833 (6) | 0.187 | flat +0.011 (noise 0.028) |
| reversal_k8_next | 0.446 (101) | 0.387 (744) [0.364, 0.410] | 0.384 (2742) [0.371, 0.397] | 0.389 (4618) [0.378, 0.400] | 0.383 (2512) [0.369, 0.396] | 0.000 (2) | 0.120 | flat +0.022 (noise 0.025) |
| reversal_k8_now | 0.770 (61) | 0.683 (369) [0.628, 0.736] | 0.689 (1559) [0.667, 0.709] | 0.701 (2959) [0.686, 0.716] | 0.687 (1372) [0.663, 0.710] | 0.667 (3) | 0.121 | flat +0.016 (noise 0.038) |
| overall | 0.508 (22158) | 0.506 (155193) [0.503, 0.508] | 0.504 (663405) [0.503, 0.506] | 0.503 (1257973) [0.502, 0.504] | 0.504 (574692) [0.503, 0.506] | 0.497 (1226) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08085, 0.1228] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5278, 'levels': [{'threshold': 0.08085, 'calls_per_day': 144.0, 'win_rate': 0.613}, {'threshold': 0.1228, 'calls_per_day': 36.4, 'win_rate': 0.6133}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 36074, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14907 | 0.340 | 0.522 (14683) | 0.583 (1962) | 0.751 (2548) |
| volatility: normal | 14906 | 0.366 | 0.531 (14841) | 0.611 (1301) | 0.750 (2201) |
| volatility: wild | 14906 | 0.380 | 0.523 (14866) | 0.635 (647) | 0.774 (1970) |
| session: Asia 00-08 | 14959 | 0.361 | 0.530 (14859) | 0.602 (1387) | 0.762 (2229) |
| session: Europe 08-13 | 9300 | 0.358 | 0.530 (9217) | 0.593 (964) | 0.747 (1501) |
| session: US 13-21 | 14880 | 0.370 | 0.521 (14788) | 0.602 (1002) | 0.765 (2142) |
| session: late 21-24 | 5580 | 0.351 | 0.516 (5526) | 0.610 (557) | 0.744 (847) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.356 | 0.359 | 0.247 | 0.247 | 0.483 | 0.263 | 0.448 | 1.120 |
| 6h | 360 | 0.381 | 0.378 | 0.299 | 0.323 | 0.542 | 0.272 | 0.489 | 1.431 |
| 24h | 1440 | 0.364 | 0.363 | 0.276 | 0.310 | 0.521 | 0.262 | 0.467 | 1.313 |
| 7d | 10080 | 0.368 | 0.359 | 0.279 | 0.310 | 0.528 | 0.265 | 0.470 | 1.244 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.307 | 0.525 | 0.259 | 0.465 | 1.279 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.356 / 0.483 / 0.850; 2: 0.373 / 0.600 / 0.883; 3: 0.308 / 0.383 / 0.850; 4: 0.376 / 0.633 / 0.850; 5: 0.297 / 0.433 / 0.883; 6: 0.292 / 0.333 / 0.883; 7: 0.331 / 0.500 / 0.833; 8: 0.327 / 0.483 / 0.833; 9: 0.330 / 0.567 / 0.833; 10: 0.345 / 0.550 / 0.833; 11: 0.348 / 0.517 / 0.800; 12: 0.338 / 0.517 / 0.800; 13: 0.321 / 0.400 / 0.817; 14: 0.360 / 0.567 / 0.833; 15: 0.357 / 0.583 / 0.800
- 6h: 1: 0.381 / 0.542 / 0.928; 2: 0.363 / 0.489 / 0.928; 3: 0.362 / 0.489 / 0.917; 4: 0.363 / 0.481 / 0.917; 5: 0.360 / 0.508 / 0.933; 6: 0.363 / 0.511 / 0.917; 7: 0.358 / 0.464 / 0.914; 8: 0.363 / 0.533 / 0.936; 9: 0.373 / 0.544 / 0.933; 10: 0.364 / 0.475 / 0.944; 11: 0.368 / 0.522 / 0.922; 12: 0.373 / 0.528 / 0.933; 13: 0.344 / 0.442 / 0.903; 14: 0.375 / 0.531 / 0.894; 15: 0.361 / 0.522 / 0.911
- 24h: 1: 0.364 / 0.521 / 0.916; 2: 0.351 / 0.486 / 0.901; 3: 0.353 / 0.498 / 0.903; 4: 0.357 / 0.511 / 0.902; 5: 0.347 / 0.484 / 0.901; 6: 0.350 / 0.507 / 0.897; 7: 0.352 / 0.494 / 0.895; 8: 0.352 / 0.516 / 0.897; 9: 0.353 / 0.515 / 0.899; 10: 0.354 / 0.500 / 0.900; 11: 0.352 / 0.514 / 0.897; 12: 0.352 / 0.501 / 0.901; 13: 0.345 / 0.493 / 0.894; 14: 0.351 / 0.507 / 0.892; 15: 0.350 / 0.508 / 0.898
- 7d: 1: 0.368 / 0.528 / 0.898; 2: 0.355 / 0.496 / 0.900; 3: 0.358 / 0.511 / 0.900; 4: 0.353 / 0.497 / 0.900; 5: 0.353 / 0.504 / 0.901; 6: 0.352 / 0.503 / 0.901; 7: 0.352 / 0.499 / 0.901; 8: 0.354 / 0.510 / 0.901; 9: 0.352 / 0.503 / 0.901; 10: 0.352 / 0.503 / 0.901; 11: 0.350 / 0.502 / 0.900; 12: 0.353 / 0.506 / 0.900; 13: 0.348 / 0.496 / 0.900; 14: 0.350 / 0.499 / 0.899; 15: 0.350 / 0.500 / 0.900
- 30d: 1: 0.362 / 0.525 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.501 / 0.900; 9: 0.347 / 0.497 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.102 (body 0.068, range 0.135); 'price stays where it was' would score 0.202; colour right 0.633; typical miss of the close 10.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.117 (body 0.082, range 0.153); 'price stays where it was' would score 0.155; colour right 0.497; typical miss of the close 10.2 bp; chain ended on the right side 0.292 of 24 chains; n=360
- 24h: match 0.136 (body 0.095, range 0.177); 'price stays where it was' would score 0.138; colour right 0.501; typical miss of the close 8.3 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.138; colour right 0.496; typical miss of the close 8.5 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.129; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.198 / 4.6; 3: 0.169 / 6.0; 4: 0.133 / 6.5; 5: 0.127 / 7.1; 6: 0.114 / 7.7; 7: 0.108 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.086 / 9.7; 12: 0.077 / 9.9; 13: 0.067 / 10.2; 14: 0.072 / 10.5; 15: 0.062 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 125113, probability skill vs chance 0.2265, widened contest next: False
  - now: threshold 0.8345, hit rate recent 0.9363 / long run 0.9387
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.259, naive rule 0.409, lift 3.86x
    - 24h: 68 calls (68 a day), hit rate 0.912, chance 0.284, naive rule 0.470, lift 3.21x
    - 7d: 403 calls (58 a day), hit rate 0.943, chance 0.295, naive rule 0.499, lift 3.20x
    - 30d: 1740 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.491, lift 3.19x
  - next: threshold 0.5303, hit rate recent 0.5832 / long run 0.5864
    - 6h: 35 calls (142 a day), hit rate 0.543, chance 0.259, lift 2.09x
    - 24h: 118 calls (118 a day), hit rate 0.568, chance 0.284, lift 2.00x
    - 7d: 652 calls (93 a day), hit rate 0.597, chance 0.295, lift 2.02x
    - 30d: 2896 calls (97 a day), hit rate 0.583, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 537, 0.519; 0.40: 477, 0.577; 0.45: 408, 0.647; 0.50: 357, 0.698; 0.55: 312, 0.739; 0.60: 264, 0.784; 0.65: 221, 0.810; 0.70: 175, 0.843; 0.75: 137, 0.874; 0.80: 92, 0.914; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 500, 0.465; 0.40: 407, 0.499; 0.45: 310, 0.534; 0.50: 200, 0.569; 0.55: 89, 0.572; 0.60: 13, 0.636; 0.65: 1, 0.645
- **K=5**: model 1792540800, labels learned 125111, probability skill vs chance 0.2219, widened contest next: False
  - now: threshold 0.6741, hit rate recent 0.8418 / long run 0.8258
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.159, naive rule 0.332, lift 5.95x
    - 24h: 73 calls (73 a day), hit rate 0.822, chance 0.176, naive rule 0.377, lift 4.68x
    - 7d: 394 calls (56 a day), hit rate 0.827, chance 0.185, naive rule 0.406, lift 4.47x
    - 30d: 1616 calls (54 a day), hit rate 0.827, chance 0.188, naive rule 0.402, lift 4.40x
  - next: threshold 0.4568, hit rate recent 0.5002 / long run 0.4879
    - 6h: 18 calls (73 a day), hit rate 0.444, chance 0.159, lift 2.80x
    - 24h: 68 calls (68 a day), hit rate 0.485, chance 0.176, lift 2.77x
    - 7d: 767 calls (110 a day), hit rate 0.505, chance 0.185, lift 2.72x
    - 30d: 3070 calls (102 a day), hit rate 0.469, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 346, 0.492; 0.40: 279, 0.565; 0.45: 227, 0.619; 0.50: 179, 0.669; 0.55: 139, 0.710; 0.60: 107, 0.753; 0.65: 76, 0.791; 0.70: 52, 0.830; 0.75: 30, 0.872; 0.80: 10, 0.901
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.391; 0.35: 254, 0.422; 0.40: 159, 0.457; 0.45: 70, 0.472; 0.50: 14, 0.495; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 125108, probability skill vs chance 0.2099, widened contest next: False
  - now: threshold 0.5607, hit rate recent 0.7471 / long run 0.6874
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.131, naive rule 0.340, lift 6.92x
    - 24h: 60 calls (60 a day), hit rate 0.750, chance 0.127, naive rule 0.351, lift 5.93x
    - 7d: 371 calls (53 a day), hit rate 0.682, chance 0.120, naive rule 0.335, lift 5.70x
    - 30d: 1556 calls (52 a day), hit rate 0.690, chance 0.121, naive rule 0.333, lift 5.68x
  - next: threshold 0.3329, hit rate recent 0.4311 / long run 0.3876
    - 6h: 22 calls (91 a day), hit rate 0.455, chance 0.131, lift 3.46x
    - 24h: 101 calls (102 a day), hit rate 0.426, chance 0.127, lift 3.36x
    - 7d: 739 calls (106 a day), hit rate 0.388, chance 0.120, lift 3.25x
    - 30d: 2735 calls (91 a day), hit rate 0.384, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 188, 0.499; 0.40: 146, 0.548; 0.45: 112, 0.593; 0.50: 84, 0.636; 0.55: 60, 0.674; 0.60: 40, 0.713; 0.65: 23, 0.776; 0.70: 11, 0.814; 0.75: 2, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.357; 0.35: 93, 0.385; 0.40: 32, 0.408; 0.45: 6, 0.417; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 125103, probability skill vs chance 0.1926, widened contest next: False
  - now: threshold 0.4059, hit rate recent 0.627 / long run 0.5647
    - 6h: 10 calls (42 a day), hit rate 1.000, chance 0.087, naive rule 0.306, lift 11.50x
    - 24h: 61 calls (62 a day), hit rate 0.590, chance 0.082, naive rule 0.295, lift 7.19x
    - 7d: 392 calls (56 a day), hit rate 0.569, chance 0.076, naive rule 0.281, lift 7.47x
    - 30d: 1628 calls (54 a day), hit rate 0.564, chance 0.077, naive rule 0.276, lift 7.32x
  - next: threshold 0.2947, hit rate recent 0.3421 / long run 0.3196
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.087, lift 5.75x
    - 24h: 51 calls (52 a day), hit rate 0.275, chance 0.082, lift 3.34x
    - 7d: 406 calls (58 a day), hit rate 0.320, chance 0.076, lift 4.21x
    - 30d: 2103 calls (70 a day), hit rate 0.311, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 125, 0.441; 0.35: 89, 0.492; 0.40: 63, 0.549; 0.45: 42, 0.602; 0.50: 27, 0.657; 0.55: 16, 0.703; 0.60: 8, 0.746; 0.65: 2, 0.797
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.326; 0.35: 14, 0.358; 0.40: 2, 0.452; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.967 | 0.65% | 0.850 | 0.467 | 0.248 | 0.583 | 0.264 |
| 6h | 14.771 | 2.06% | 0.911 | 0.522 | 0.250 | 0.525 | 0.572 |
| 24h | 14.437 | 3.99% | 0.910 | 0.504 | 0.250 | 0.505 | 0.593 |
| 7d | 14.612 | 3.53% | 0.901 | 0.501 | 0.250 | 0.499 | 0.649 |
| 30d | 13.749 | 4.08% | 0.900 | 0.500 | 0.251 | 0.495 | 0.665 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.051 | 13.213 | 12.918 | 12.965 | 13.047 | 12.888 | 13.022 | 13.003 | 12.967 | 12.967 |
| 6h | 15.083 | 14.990 | 14.835 | 14.811 | 15.122 | 14.832 | 14.748 | 14.774 | 14.758 | 14.771 |
| 24h | 15.037 | 14.648 | 14.571 | 14.441 | 14.909 | 14.619 | 14.415 | 14.409 | 14.411 | 14.437 |
| 7d | 15.148 | 14.768 | 14.706 | 14.631 | 14.906 | 14.761 | 14.595 | 14.577 | 14.582 | 14.612 |
| 30d | 14.333 | 13.884 | 13.834 | 13.773 | 14.002 | 13.930 | 13.744 | 13.723 | 13.723 | 13.749 |

## Next candle

- candle starting 2026-10-29 01:19 UTC, last close 2343.22
- P(up) 0.486, return quantiles (bp): {'05': -8.716, '10': -6.682, '25': -3.619, '40': -1.588, '50': -0.159, '60': 0.999, '75': 3.289, '90': 6.87, '95': 8.842}
- changepoint probability 0.0448, regime age 19.4 min
- agent weights: empirical 0.004, ewma 0.037, garch 0.083, har 0.243, bocpd 0.006, hmm 0.054, online_qr 0.295, lgbm 0.278

## Learning log

- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.53, 6.59, 15.41], current probabilities: [0.008, 0.927, 0.065]
- live generator: {'versions': 60, 'latest_effective': '2026-10-29 01:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.336, 'l_abs': 0.717, 'l_hi': 0.737, 'l_lo': 0.761, 'b05': 0.712, 'b25': 0.735, 'b75': 0.642, 'b95': 0.684}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.298, 1.561, 1.806, 2.064, 2.406, 2.656, 2.575, 2.906, 2.89, 3.357, 3.243, 3.89, 4.127, 3.873]}
- calibration offsets (in sigma): {'05': 0.089, '10': 0.028, '25': -0.045, '40': -0.078, '50': -0.07, '60': -0.082, '75': -0.075, '90': -0.048, '95': -0.039}
