# ETH-USD 60s candle generator - report

- generated: 2026-10-29 23:39 UTC
- last closed candle: 2026-10-29 23:39 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.537 (672) [0.501, 0.573] | 0.520 (2876) [0.501, 0.539] | 0.517 (5466) [0.503, 0.531] | 0.524 (2494) [0.504, 0.546] | 0.479 (94) | 0.500 | flat -0.006 (noise 0.031) |
| colour_clear | 0.537 (786) | 0.542 (5666) [0.539, 0.547] | 0.538 (23626) [0.531, 0.545] | 0.519 (44743) [0.513, 0.525] | 0.546 (20505) [0.541, 0.550] | 0.524 (800) | 0.500 | flat -0.013 (noise 0.009) |
| colour_confident | 0.567 (120) | 0.601 (1315) [0.586, 0.617] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.583 (115) | 0.500 | flat +0.001 (noise 0.021) |
| colour_next | 0.531 (1431) | 0.528 (10027) [0.525, 0.531] | 0.526 (42877) [0.521, 0.530] | 0.514 (81483) [0.510, 0.518] | 0.529 (37134) [0.526, 0.533] | 0.513 (1412) | 0.500 | flat -0.006 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.502 (140378) [0.500, 0.504] | 0.501 (600278) [0.499, 0.502] | 0.501 (1140762) [0.500, 0.502] | 0.501 (519876) [0.499, 0.502] | 0.497 (19768) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.500 (32) | 0.607 (405) [0.583, 0.639] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.765 (17) | 0.500 | flat -0.024 (noise 0.040) |
| reversal_k13_next | 0.302 (53) | 0.317 (410) [0.283, 0.357] | 0.310 (2116) [0.298, 0.323] | 0.309 (3847) [0.299, 0.320] | 0.320 (1742) [0.308, 0.332] | 0.261 (46) | 0.077 | flat -0.007 (noise 0.032) |
| reversal_k13_now | 0.603 (63) | 0.568 (391) [0.519, 0.620] | 0.562 (1632) [0.542, 0.584] | 0.573 (2895) [0.558, 0.589] | 0.565 (1423) [0.543, 0.589] | 0.515 (66) | 0.077 | flat +0.043 (noise 0.036) |
| reversal_k3_next | 0.591 (115) | 0.593 (648) [0.584, 0.603] | 0.583 (2896) [0.572, 0.596] | 0.584 (4997) [0.574, 0.594] | 0.580 (2557) [0.568, 0.594] | 0.595 (121) | 0.293 | flat +0.016 (noise 0.026) |
| reversal_k3_now | 0.909 (66) | 0.942 (399) [0.918, 0.964] | 0.935 (1742) [0.926, 0.945] | 0.938 (3257) [0.931, 0.945] | 0.934 (1494) [0.923, 0.944] | 1.000 (63) | 0.293 | flat +0.010 (noise 0.021) |
| reversal_k5_next | 0.500 (64) | 0.501 (766) [0.491, 0.512] | 0.468 (3071) [0.455, 0.482] | 0.478 (4683) [0.466, 0.491] | 0.466 (2693) [0.452, 0.481] | 0.537 (41) | 0.187 | up +0.067 (noise 0.024) |
| reversal_k5_now | 0.838 (74) | 0.828 (389) [0.816, 0.837] | 0.826 (1616) [0.814, 0.837] | 0.830 (3006) [0.820, 0.840] | 0.822 (1395) [0.810, 0.834] | 0.838 (68) | 0.187 | flat +0.011 (noise 0.028) |
| reversal_k8_next | 0.446 (101) | 0.387 (744) [0.364, 0.410] | 0.384 (2742) [0.371, 0.397] | 0.389 (4618) [0.378, 0.400] | 0.383 (2512) [0.369, 0.396] | 0.394 (94) | 0.120 | flat +0.022 (noise 0.025) |
| reversal_k8_now | 0.770 (61) | 0.683 (369) [0.628, 0.736] | 0.689 (1559) [0.667, 0.709] | 0.701 (2959) [0.686, 0.716] | 0.687 (1372) [0.663, 0.710] | 0.750 (56) | 0.121 | flat +0.016 (noise 0.038) |
| overall | 0.508 (22158) | 0.506 (155193) [0.503, 0.508] | 0.504 (663405) [0.503, 0.506] | 0.503 (1257973) [0.502, 0.504] | 0.504 (574692) [0.503, 0.506] | 0.500 (21829) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08204, 0.1244] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5264, 'levels': [{'threshold': 0.08204, 'calls_per_day': 146.3, 'win_rate': 0.6087}, {'threshold': 0.1244, 'calls_per_day': 36.5, 'win_rate': 0.607}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 37405, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15353 | 0.341 | 0.522 (15125) | 0.585 (2010) | 0.751 (2599) |
| volatility: normal | 15353 | 0.366 | 0.530 (15287) | 0.610 (1327) | 0.752 (2284) |
| volatility: wild | 15353 | 0.380 | 0.522 (15311) | 0.629 (680) | 0.771 (2073) |
| session: Asia 00-08 | 15360 | 0.361 | 0.531 (15257) | 0.605 (1425) | 0.759 (2293) |
| session: Europe 08-13 | 9600 | 0.358 | 0.529 (9514) | 0.590 (996) | 0.749 (1541) |
| session: US 13-21 | 15360 | 0.370 | 0.520 (15267) | 0.600 (1035) | 0.766 (2248) |
| session: late 21-24 | 5739 | 0.352 | 0.515 (5685) | 0.611 (561) | 0.749 (874) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.364 | 0.381 | 0.294 | 0.294 | 0.450 | 0.227 | 0.502 | 1.457 |
| 6h | 360 | 0.379 | 0.370 | 0.323 | 0.349 | 0.499 | 0.254 | 0.504 | 1.384 |
| 24h | 1440 | 0.370 | 0.368 | 0.290 | 0.321 | 0.513 | 0.256 | 0.484 | 1.154 |
| 7d | 10080 | 0.367 | 0.359 | 0.282 | 0.312 | 0.525 | 0.264 | 0.470 | 1.237 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.306 | 0.526 | 0.259 | 0.464 | 1.274 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.364 / 0.450 / 0.900; 2: 0.386 / 0.517 / 1.000; 3: 0.378 / 0.450 / 0.983; 4: 0.396 / 0.583 / 0.983; 5: 0.373 / 0.517 / 1.000; 6: 0.370 / 0.483 / 1.000; 7: 0.386 / 0.533 / 1.000; 8: 0.375 / 0.467 / 1.000; 9: 0.388 / 0.583 / 1.000; 10: 0.374 / 0.500 / 1.000; 11: 0.369 / 0.500 / 1.000; 12: 0.373 / 0.517 / 1.000; 13: 0.372 / 0.500 / 1.000; 14: 0.359 / 0.433 / 1.000; 15: 0.380 / 0.500 / 1.000
- 6h: 1: 0.379 / 0.499 / 0.894; 2: 0.371 / 0.482 / 0.911; 3: 0.374 / 0.521 / 0.917; 4: 0.381 / 0.535 / 0.914; 5: 0.368 / 0.521 / 0.906; 6: 0.369 / 0.524 / 0.897; 7: 0.368 / 0.493 / 0.892; 8: 0.355 / 0.462 / 0.850; 9: 0.366 / 0.496 / 0.858; 10: 0.368 / 0.515 / 0.858; 11: 0.359 / 0.501 / 0.853; 12: 0.351 / 0.476 / 0.836; 13: 0.377 / 0.524 / 0.825; 14: 0.350 / 0.476 / 0.833; 15: 0.356 / 0.493 / 0.836
- 24h: 1: 0.370 / 0.513 / 0.899; 2: 0.365 / 0.514 / 0.897; 3: 0.361 / 0.501 / 0.895; 4: 0.365 / 0.511 / 0.895; 5: 0.359 / 0.507 / 0.897; 6: 0.352 / 0.484 / 0.894; 7: 0.364 / 0.505 / 0.892; 8: 0.354 / 0.490 / 0.883; 9: 0.352 / 0.484 / 0.888; 10: 0.360 / 0.507 / 0.890; 11: 0.353 / 0.488 / 0.889; 12: 0.349 / 0.476 / 0.881; 13: 0.357 / 0.500 / 0.885; 14: 0.356 / 0.498 / 0.886; 15: 0.352 / 0.495 / 0.881
- 7d: 1: 0.367 / 0.525 / 0.899; 2: 0.354 / 0.494 / 0.900; 3: 0.358 / 0.511 / 0.900; 4: 0.354 / 0.499 / 0.900; 5: 0.354 / 0.505 / 0.900; 6: 0.351 / 0.502 / 0.899; 7: 0.353 / 0.501 / 0.899; 8: 0.353 / 0.507 / 0.898; 9: 0.352 / 0.501 / 0.899; 10: 0.353 / 0.505 / 0.900; 11: 0.350 / 0.501 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.350 / 0.501 / 0.899; 14: 0.350 / 0.500 / 0.899; 15: 0.350 / 0.499 / 0.899
- 30d: 1: 0.362 / 0.526 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.899; 13: 0.346 / 0.501 / 0.899; 14: 0.346 / 0.499 / 0.899; 15: 0.346 / 0.499 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.199 (body 0.148, range 0.250); 'price stays where it was' would score 0.243; colour right 0.467; typical miss of the close 11.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.139 (body 0.096, range 0.183); 'price stays where it was' would score 0.147; colour right 0.499; typical miss of the close 16.7 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.130 (body 0.085, range 0.175); 'price stays where it was' would score 0.133; colour right 0.502; typical miss of the close 11.0 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.170); 'price stays where it was' would score 0.135; colour right 0.496; typical miss of the close 8.7 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.129; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.0; 2: 0.200 / 4.6; 3: 0.167 / 6.1; 4: 0.133 / 6.5; 5: 0.126 / 7.2; 6: 0.113 / 7.7; 7: 0.109 / 8.1; 8: 0.096 / 8.6; 9: 0.086 / 8.7; 10: 0.087 / 9.3; 11: 0.085 / 9.7; 12: 0.077 / 9.9; 13: 0.068 / 10.2; 14: 0.072 / 10.5; 15: 0.062 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 126453, probability skill vs chance 0.24, widened contest next: False
  - now: threshold 0.8346, hit rate recent 0.976 / long run 0.9444
    - 6h: 21 calls (85 a day), hit rate 1.000, chance 0.321, naive rule 0.544, lift 3.11x
    - 24h: 63 calls (63 a day), hit rate 1.000, chance 0.289, naive rule 0.494, lift 3.46x
    - 7d: 409 calls (58 a day), hit rate 0.954, chance 0.292, naive rule 0.495, lift 3.27x
    - 30d: 1738 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5306, hit rate recent 0.6362 / long run 0.5895
    - 6h: 21 calls (85 a day), hit rate 0.714, chance 0.321, lift 2.22x
    - 24h: 123 calls (123 a day), hit rate 0.585, chance 0.289, lift 2.02x
    - 7d: 676 calls (97 a day), hit rate 0.590, chance 0.292, lift 2.02x
    - 30d: 2921 calls (97 a day), hit rate 0.581, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 536, 0.520; 0.40: 476, 0.577; 0.45: 407, 0.649; 0.50: 356, 0.699; 0.55: 312, 0.740; 0.60: 264, 0.786; 0.65: 221, 0.811; 0.70: 174, 0.844; 0.75: 137, 0.877; 0.80: 92, 0.914; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 500, 0.465; 0.40: 407, 0.498; 0.45: 310, 0.533; 0.50: 200, 0.569; 0.55: 89, 0.571; 0.60: 13, 0.636; 0.65: 1, 0.607
- **K=5**: model 1792540800, labels learned 126451, probability skill vs chance 0.2341, widened contest next: False
  - now: threshold 0.677, hit rate recent 0.8405 / long run 0.8271
    - 6h: 20 calls (82 a day), hit rate 0.850, chance 0.205, naive rule 0.472, lift 4.14x
    - 24h: 68 calls (68 a day), hit rate 0.838, chance 0.193, naive rule 0.427, lift 4.34x
    - 7d: 416 calls (59 a day), hit rate 0.829, chance 0.185, naive rule 0.407, lift 4.47x
    - 30d: 1627 calls (54 a day), hit rate 0.825, chance 0.188, naive rule 0.404, lift 4.39x
  - next: threshold 0.4573, hit rate recent 0.5188 / long run 0.4903
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.205, lift 3.04x
    - 24h: 41 calls (41 a day), hit rate 0.537, chance 0.193, lift 2.78x
    - 7d: 678 calls (97 a day), hit rate 0.506, chance 0.185, lift 2.73x
    - 30d: 3061 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.493; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 180, 0.669; 0.55: 140, 0.709; 0.60: 108, 0.753; 0.65: 77, 0.791; 0.70: 51, 0.829; 0.75: 30, 0.869; 0.80: 10, 0.902
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.390; 0.35: 254, 0.421; 0.40: 159, 0.456; 0.45: 69, 0.472; 0.50: 14, 0.491; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 126448, probability skill vs chance 0.2151, widened contest next: False
  - now: threshold 0.563, hit rate recent 0.7645 / long run 0.6933
    - 6h: 19 calls (78 a day), hit rate 0.789, chance 0.129, naive rule 0.402, lift 6.14x
    - 24h: 56 calls (56 a day), hit rate 0.750, chance 0.126, naive rule 0.352, lift 5.97x
    - 7d: 387 calls (55 a day), hit rate 0.687, chance 0.121, naive rule 0.339, lift 5.69x
    - 30d: 1568 calls (52 a day), hit rate 0.692, chance 0.121, naive rule 0.334, lift 5.70x
  - next: threshold 0.3438, hit rate recent 0.4339 / long run 0.3902
    - 6h: 18 calls (74 a day), hit rate 0.389, chance 0.129, lift 3.02x
    - 24h: 96 calls (97 a day), hit rate 0.385, chance 0.126, lift 3.07x
    - 7d: 740 calls (106 a day), hit rate 0.395, chance 0.121, lift 3.27x
    - 30d: 2775 calls (93 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 189, 0.499; 0.40: 146, 0.549; 0.45: 112, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.677; 0.60: 40, 0.713; 0.65: 23, 0.775; 0.70: 11, 0.809; 0.75: 2, 0.774
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.356; 0.35: 93, 0.383; 0.40: 31, 0.404; 0.45: 6, 0.425; 0.50: 1, 0.655
- **K=13**: model 1793059200, labels learned 126443, probability skill vs chance 0.1899, widened contest next: False
  - now: threshold 0.4078, hit rate recent 0.5671 / long run 0.5585
    - 6h: 19 calls (79 a day), hit rate 0.579, chance 0.087, naive rule 0.300, lift 6.66x
    - 24h: 66 calls (67 a day), hit rate 0.515, chance 0.081, naive rule 0.294, lift 6.38x
    - 7d: 419 calls (60 a day), hit rate 0.556, chance 0.076, naive rule 0.280, lift 7.27x
    - 30d: 1641 calls (55 a day), hit rate 0.564, chance 0.077, naive rule 0.277, lift 7.30x
  - next: threshold 0.295, hit rate recent 0.3085 / long run 0.3154
    - 6h: 10 calls (42 a day), hit rate 0.300, chance 0.087, lift 3.45x
    - 24h: 46 calls (46 a day), hit rate 0.261, chance 0.081, lift 3.23x
    - 7d: 410 calls (59 a day), hit rate 0.320, chance 0.076, lift 4.18x
    - 30d: 2055 calls (69 a day), hit rate 0.312, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.443; 0.35: 90, 0.494; 0.40: 64, 0.548; 0.45: 42, 0.598; 0.50: 28, 0.655; 0.55: 16, 0.694; 0.60: 8, 0.743; 0.65: 2, 0.742; 0.70: 0, 0.500
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.356; 0.40: 2, 0.453; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 27.326 | 1.49% | 0.900 | 0.550 | 0.252 | 0.483 | 0.049 |
| 6h | 34.092 | 11.57% | 0.894 | 0.514 | 0.251 | 0.479 | 0.777 |
| 24h | 21.155 | 6.69% | 0.893 | 0.499 | 0.251 | 0.507 | 0.788 |
| 7d | 15.386 | 4.32% | 0.900 | 0.500 | 0.251 | 0.498 | 0.719 |
| 30d | 13.960 | 4.28% | 0.900 | 0.500 | 0.251 | 0.496 | 0.683 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 27.738 | 27.260 | 27.551 | 27.255 | 27.878 | 27.634 | 27.431 | 27.329 | 27.294 | 27.326 |
| 6h | 38.553 | 34.926 | 34.412 | 33.854 | 34.530 | 35.744 | 34.078 | 33.991 | 33.991 | 34.092 |
| 24h | 22.671 | 21.469 | 21.277 | 21.102 | 21.484 | 21.651 | 21.162 | 21.136 | 21.118 | 21.155 |
| 7d | 16.081 | 15.566 | 15.485 | 15.401 | 15.688 | 15.596 | 15.374 | 15.349 | 15.355 | 15.386 |
| 30d | 14.584 | 14.104 | 14.048 | 13.984 | 14.217 | 14.154 | 13.955 | 13.934 | 13.934 | 13.960 |

## Next candle

- candle starting 2026-10-29 23:39 UTC, last close 2257.72
- P(up) 0.4967, return quantiles (bp): {'05': -16.361, '10': -12.29, '25': -5.968, '40': -2.547, '50': -0.044, '60': 1.948, '75': 5.81, '90': 11.118, '95': 15.735}
- changepoint probability 0.0443, regime age 54.6 min
- agent weights: empirical 0.003, ewma 0.009, garch 0.052, har 0.431, bocpd 0.015, hmm 0.003, online_qr 0.204, lgbm 0.284

## Learning log

- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.69, 15.08], current probabilities: [0.027, 0.87, 0.103]
- live generator: {'versions': 60, 'latest_effective': '2026-10-29 23:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.302, 'l_abs': 0.733, 'l_hi': 0.73, 'l_lo': 0.746, 'b05': 0.735, 'b25': 0.734, 'b75': 0.613, 'b95': 0.728}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.493, 1.76, 2.077, 2.374, 2.938, 3.244, 4.161, 4.082, 3.901, 4.441, 5.347, 5.804, 6.157, 6.514]}
- calibration offsets (in sigma): {'05': -0.011, '10': -0.022, '25': -0.015, '40': -0.048, '50': -0.01, '60': -0.032, '75': -0.015, '90': -0.058, '95': -0.039}
