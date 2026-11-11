# ETH-USD 60s candle generator - report

- generated: 2026-11-11 18:09 UTC
- last closed candle: 2026-11-11 18:09 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.522 (672) [0.490, 0.555] | 0.518 (2880) [0.502, 0.535] | 0.513 (6714) [0.502, 0.525] | 0.515 (3742) [0.499, 0.531] | 0.597 (72) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.543 (777) | 0.541 (5503) [0.522, 0.558] | 0.543 (23887) [0.537, 0.549] | 0.523 (54927) [0.517, 0.528] | 0.543 (30689) [0.538, 0.548] | 0.511 (642) | 0.500 | flat +0.007 (noise 0.012) |
| colour_confident | 0.455 (88) | 0.570 (988) [0.540, 0.594] | 0.588 (4263) [0.578, 0.598] | 0.593 (5683) [0.582, 0.604] | 0.593 (5683) [0.582, 0.604] | 0.509 (53) | 0.500 | flat -0.006 (noise 0.023) |
| colour_next | 0.519 (1434) | 0.530 (9968) [0.518, 0.543] | 0.530 (42864) [0.526, 0.534] | 0.517 (99994) [0.513, 0.521] | 0.530 (55645) [0.526, 0.534] | 0.501 (1088) | 0.500 | flat -0.000 (noise 0.009) |
| colour_path | 0.496 (20076) | 0.501 (139552) [0.499, 0.504] | 0.502 (600096) [0.500, 0.503] | 0.501 (1399916) [0.500, 0.502] | 0.501 (779030) [0.500, 0.502] | 0.510 (15232) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.733 (15) | 0.625 (264) [0.589, 0.647] | 0.622 (1111) [0.606, 0.639] | 0.631 (1508) [0.615, 0.648] | 0.631 (1508) [0.615, 0.648] | 0.500 (2) | 0.500 | flat +0.004 (noise 0.045) |
| reversal_k13_next | 0.384 (73) | 0.328 (472) [0.305, 0.353] | 0.324 (1839) [0.310, 0.340] | 0.314 (4624) [0.304, 0.324] | 0.326 (2519) [0.315, 0.338] | 0.396 (53) | 0.077 | flat -0.024 (noise 0.033) |
| reversal_k13_now | 0.646 (48) | 0.573 (351) [0.546, 0.602] | 0.561 (1638) [0.542, 0.581] | 0.574 (3606) [0.561, 0.587] | 0.568 (2134) [0.551, 0.586] | 0.615 (39) | 0.077 | flat -0.009 (noise 0.036) |
| reversal_k3_next | 0.521 (48) | 0.619 (352) [0.588, 0.646] | 0.589 (2826) [0.578, 0.601] | 0.588 (6053) [0.579, 0.596] | 0.588 (3613) [0.577, 0.598] | 0.600 (30) | 0.293 | flat +0.022 (noise 0.031) |
| reversal_k3_now | 0.919 (62) | 0.921 (406) [0.912, 0.931] | 0.933 (1717) [0.923, 0.944] | 0.935 (4025) [0.930, 0.941] | 0.931 (2262) [0.923, 0.939] | 0.929 (42) | 0.294 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.532 (62) | 0.533 (392) [0.511, 0.553] | 0.488 (2680) [0.472, 0.505] | 0.486 (5400) [0.475, 0.497] | 0.481 (3410) [0.466, 0.496] | 0.436 (39) | 0.187 | flat -0.002 (noise 0.036) |
| reversal_k5_now | 0.829 (70) | 0.799 (368) [0.758, 0.832] | 0.812 (1627) [0.800, 0.823] | 0.825 (3736) [0.816, 0.834] | 0.816 (2125) [0.805, 0.826] | 0.704 (54) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.443 (70) | 0.422 (445) [0.392, 0.454] | 0.397 (2622) [0.383, 0.412] | 0.396 (5502) [0.386, 0.406] | 0.396 (3396) [0.383, 0.408] | 0.490 (51) | 0.121 | flat -0.016 (noise 0.032) |
| reversal_k8_now | 0.737 (57) | 0.695 (357) [0.671, 0.716] | 0.686 (1524) [0.666, 0.704] | 0.701 (3639) [0.688, 0.713] | 0.691 (2052) [0.673, 0.708] | 0.691 (42) | 0.122 | flat -0.019 (noise 0.034) |
| overall | 0.500 (22096) | 0.505 (153335) [0.503, 0.508] | 0.505 (662313) [0.504, 0.507] | 0.504 (1543209) [0.503, 0.505] | 0.505 (859928) [0.504, 0.506] | 0.512 (16742) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0762, 0.1159] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5301, 'levels': [{'threshold': 0.0762, 'calls_per_day': 140.9, 'win_rate': 0.5697}, {'threshold': 0.1159, 'calls_per_day': 34.9, 'win_rate': 0.6194}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42867, 'rate': 0.5291}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15243 | 0.343 | 0.531 (14988) | 0.569 (2351) | 0.737 (2568) |
| volatility: normal | 15243 | 0.369 | 0.532 (15178) | 0.607 (1373) | 0.751 (2275) |
| volatility: wild | 15243 | 0.385 | 0.525 (15205) | 0.612 (788) | 0.770 (2071) |
| session: Asia 00-08 | 15360 | 0.365 | 0.535 (15226) | 0.593 (1608) | 0.752 (2306) |
| session: Europe 08-13 | 9600 | 0.360 | 0.533 (9518) | 0.586 (1184) | 0.755 (1572) |
| session: US 13-21 | 15189 | 0.373 | 0.527 (15085) | 0.598 (1172) | 0.751 (2261) |
| session: late 21-24 | 5580 | 0.358 | 0.513 (5542) | 0.555 (548) | 0.745 (775) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.397 | 0.435 | 0.340 | 0.340 | 0.450 | 0.279 | 0.514 | 1.298 |
| 6h | 360 | 0.383 | 0.397 | 0.314 | 0.336 | 0.506 | 0.267 | 0.499 | 1.335 |
| 24h | 1440 | 0.374 | 0.379 | 0.293 | 0.322 | 0.500 | 0.259 | 0.489 | 1.161 |
| 7d | 10080 | 0.370 | 0.364 | 0.281 | 0.313 | 0.530 | 0.265 | 0.474 | 1.359 |
| 30d | 43200 | 0.367 | 0.360 | 0.279 | 0.310 | 0.529 | 0.264 | 0.470 | 1.259 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.397 / 0.450 / 0.917; 2: 0.377 / 0.517 / 0.950; 3: 0.428 / 0.650 / 0.950; 4: 0.331 / 0.383 / 0.933; 5: 0.393 / 0.550 / 0.900; 6: 0.393 / 0.533 / 0.883; 7: 0.359 / 0.533 / 0.833; 8: 0.404 / 0.583 / 0.883; 9: 0.363 / 0.517 / 0.883; 10: 0.392 / 0.600 / 0.900; 11: 0.375 / 0.500 / 0.917; 12: 0.326 / 0.417 / 0.883; 13: 0.374 / 0.517 / 0.900; 14: 0.318 / 0.417 / 0.850; 15: 0.366 / 0.433 / 0.850
- 6h: 1: 0.383 / 0.506 / 0.886; 2: 0.362 / 0.469 / 0.931; 3: 0.389 / 0.550 / 0.897; 4: 0.370 / 0.489 / 0.883; 5: 0.372 / 0.506 / 0.867; 6: 0.376 / 0.528 / 0.872; 7: 0.364 / 0.494 / 0.858; 8: 0.383 / 0.542 / 0.897; 9: 0.366 / 0.503 / 0.892; 10: 0.372 / 0.528 / 0.908; 11: 0.389 / 0.561 / 0.933; 12: 0.370 / 0.472 / 0.914; 13: 0.389 / 0.561 / 0.908; 14: 0.376 / 0.497 / 0.886; 15: 0.376 / 0.506 / 0.889
- 24h: 1: 0.374 / 0.500 / 0.887; 2: 0.365 / 0.494 / 0.903; 3: 0.379 / 0.529 / 0.903; 4: 0.369 / 0.499 / 0.907; 5: 0.371 / 0.514 / 0.909; 6: 0.367 / 0.500 / 0.899; 7: 0.364 / 0.495 / 0.890; 8: 0.376 / 0.521 / 0.907; 9: 0.367 / 0.502 / 0.907; 10: 0.364 / 0.493 / 0.902; 11: 0.375 / 0.533 / 0.906; 12: 0.362 / 0.485 / 0.904; 13: 0.375 / 0.530 / 0.904; 14: 0.365 / 0.496 / 0.906; 15: 0.369 / 0.509 / 0.901
- 7d: 1: 0.370 / 0.530 / 0.896; 2: 0.356 / 0.487 / 0.901; 3: 0.362 / 0.518 / 0.900; 4: 0.356 / 0.495 / 0.900; 5: 0.358 / 0.506 / 0.900; 6: 0.354 / 0.498 / 0.901; 7: 0.354 / 0.497 / 0.899; 8: 0.357 / 0.503 / 0.901; 9: 0.357 / 0.508 / 0.901; 10: 0.356 / 0.506 / 0.901; 11: 0.357 / 0.509 / 0.901; 12: 0.354 / 0.504 / 0.901; 13: 0.354 / 0.498 / 0.901; 14: 0.354 / 0.505 / 0.901; 15: 0.353 / 0.498 / 0.901
- 30d: 1: 0.367 / 0.529 / 0.898; 2: 0.355 / 0.494 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.353 / 0.498 / 0.899; 5: 0.354 / 0.505 / 0.899; 6: 0.352 / 0.501 / 0.899; 7: 0.352 / 0.498 / 0.899; 8: 0.353 / 0.504 / 0.899; 9: 0.353 / 0.504 / 0.899; 10: 0.353 / 0.503 / 0.900; 11: 0.351 / 0.501 / 0.900; 12: 0.351 / 0.503 / 0.900; 13: 0.351 / 0.500 / 0.899; 14: 0.351 / 0.501 / 0.899; 15: 0.351 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.137 (body 0.100, range 0.175); 'price stays where it was' would score 0.124; colour right 0.517; typical miss of the close 12.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.131 (body 0.086, range 0.176); 'price stays where it was' would score 0.144; colour right 0.514; typical miss of the close 12.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.133 (body 0.089, range 0.177); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 10.3 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.124 (body 0.083, range 0.164); 'price stays where it was' would score 0.123; colour right 0.503; typical miss of the close 8.9 bp; chain ended on the right side 0.534 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.518 of 2880 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.6; 2: 0.203 / 5.4; 3: 0.167 / 7.1; 4: 0.132 / 7.3; 5: 0.125 / 8.1; 6: 0.115 / 8.9; 7: 0.109 / 9.1; 8: 0.097 / 10.1; 9: 0.090 / 10.2; 10: 0.092 / 10.7; 11: 0.088 / 10.8; 12: 0.079 / 11.1; 13: 0.073 / 11.7; 14: 0.070 / 12.2; 15: 0.066 / 12.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 144843, probability skill vs chance 0.2336, widened contest next: False
  - now: threshold 0.8392, hit rate recent 0.9162 / long run 0.9262
    - 6h: 6 calls (24 a day), hit rate 0.833, chance 0.275, naive rule 0.510, lift 3.03x
    - 24h: 57 calls (57 a day), hit rate 0.912, chance 0.273, naive rule 0.473, lift 3.34x
    - 7d: 411 calls (59 a day), hit rate 0.925, chance 0.296, naive rule 0.503, lift 3.13x
    - 30d: 1711 calls (57 a day), hit rate 0.932, chance 0.293, naive rule 0.494, lift 3.18x
  - next: threshold 0.5663, hit rate recent 0.5766 / long run 0.6029
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.275, lift 2.55x
    - 24h: 40 calls (40 a day), hit rate 0.500, chance 0.273, lift 1.83x
    - 7d: 353 calls (50 a day), hit rate 0.618, chance 0.296, lift 2.09x
    - 30d: 2815 calls (94 a day), hit rate 0.590, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.498; 0.35: 532, 0.523; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.695; 0.55: 309, 0.739; 0.60: 260, 0.784; 0.65: 219, 0.811; 0.70: 172, 0.844; 0.75: 138, 0.875; 0.80: 91, 0.905; 0.85: 46, 0.946; 0.90: 4, 0.992
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 497, 0.463; 0.40: 398, 0.501; 0.45: 300, 0.535; 0.50: 192, 0.567; 0.55: 86, 0.577; 0.60: 12, 0.642; 0.65: 1, 0.571
- **K=5**: model 1794268800, labels learned 144841, probability skill vs chance 0.2258, widened contest next: True
  - now: threshold 0.6854, hit rate recent 0.7529 / long run 0.7985
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.204, naive rule 0.497, lift 3.81x
    - 24h: 74 calls (74 a day), hit rate 0.703, chance 0.172, naive rule 0.382, lift 4.08x
    - 7d: 385 calls (55 a day), hit rate 0.782, chance 0.186, naive rule 0.406, lift 4.20x
    - 30d: 1641 calls (55 a day), hit rate 0.807, chance 0.186, naive rule 0.405, lift 4.34x
  - next: threshold 0.4586, hit rate recent 0.4938 / long run 0.5154
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.204, lift 2.86x
    - 24h: 54 calls (54 a day), hit rate 0.444, chance 0.172, lift 2.58x
    - 7d: 390 calls (56 a day), hit rate 0.523, chance 0.186, lift 2.81x
    - 30d: 2654 calls (88 a day), hit rate 0.487, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 353, 0.481; 0.40: 286, 0.553; 0.45: 233, 0.606; 0.50: 186, 0.655; 0.55: 149, 0.693; 0.60: 112, 0.743; 0.65: 75, 0.779; 0.70: 47, 0.815; 0.75: 28, 0.850; 0.80: 10, 0.870
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.383; 0.35: 256, 0.421; 0.40: 160, 0.458; 0.45: 65, 0.492; 0.50: 10, 0.506; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 144838, probability skill vs chance 0.2227, widened contest next: False
  - now: threshold 0.5668, hit rate recent 0.7176 / long run 0.6945
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.150, naive rule 0.539, lift 4.76x
    - 24h: 55 calls (55 a day), hit rate 0.691, chance 0.127, naive rule 0.356, lift 5.46x
    - 7d: 363 calls (52 a day), hit rate 0.694, chance 0.123, naive rule 0.344, lift 5.65x
    - 30d: 1523 calls (51 a day), hit rate 0.685, chance 0.121, naive rule 0.335, lift 5.69x
  - next: threshold 0.3642, hit rate recent 0.4895 / long run 0.4254
    - 6h: 15 calls (62 a day), hit rate 0.667, chance 0.150, lift 4.44x
    - 24h: 65 calls (65 a day), hit rate 0.492, chance 0.127, lift 3.89x
    - 7d: 458 calls (65 a day), hit rate 0.434, chance 0.123, lift 3.54x
    - 30d: 2615 calls (87 a day), hit rate 0.398, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.428; 0.35: 192, 0.492; 0.40: 152, 0.537; 0.45: 117, 0.585; 0.50: 84, 0.636; 0.55: 59, 0.673; 0.60: 39, 0.711; 0.65: 24, 0.779; 0.70: 12, 0.815; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 171, 0.365; 0.35: 87, 0.395; 0.40: 23, 0.429; 0.45: 4, 0.426; 0.50: 1, 0.773
- **K=13**: model 1794355200, labels learned 144833, probability skill vs chance 0.2015, widened contest next: False
  - now: threshold 0.4497, hit rate recent 0.6238 / long run 0.5758
    - 6h: 11 calls (46 a day), hit rate 0.636, chance 0.091, naive rule 0.444, lift 6.97x
    - 24h: 48 calls (49 a day), hit rate 0.625, chance 0.086, naive rule 0.329, lift 7.30x
    - 7d: 349 calls (50 a day), hit rate 0.579, chance 0.080, naive rule 0.291, lift 7.27x
    - 30d: 1637 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.283, lift 7.25x
  - next: threshold 0.2925, hit rate recent 0.3938 / long run 0.3414
    - 6h: 16 calls (67 a day), hit rate 0.375, chance 0.091, lift 4.11x
    - 24h: 73 calls (74 a day), hit rate 0.411, chance 0.086, lift 4.80x
    - 7d: 491 calls (70 a day), hit rate 0.336, chance 0.080, lift 4.22x
    - 30d: 1840 calls (61 a day), hit rate 0.328, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.431; 0.35: 97, 0.480; 0.40: 68, 0.538; 0.45: 46, 0.584; 0.50: 31, 0.640; 0.55: 21, 0.660; 0.60: 12, 0.694; 0.65: 4, 0.670; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.334; 0.35: 13, 0.339; 0.40: 3, 0.407; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 27.068 | 5.73% | 0.917 | 0.533 | 0.247 | 0.567 | 0.340 |
| 6h | 23.717 | 4.86% | 0.900 | 0.511 | 0.248 | 0.564 | 0.542 |
| 24h | 16.688 | 3.18% | 0.897 | 0.500 | 0.250 | 0.511 | 0.570 |
| 7d | 16.442 | 6.33% | 0.900 | 0.500 | 0.250 | 0.505 | 0.683 |
| 30d | 15.821 | 4.72% | 0.900 | 0.500 | 0.250 | 0.502 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 28.714 | 28.683 | 28.829 | 27.485 | 28.998 | 27.181 | 27.026 | 26.976 | 27.062 | 27.068 |
| 6h | 24.930 | 24.459 | 24.306 | 23.980 | 24.790 | 23.926 | 23.735 | 23.495 | 23.686 | 23.717 |
| 24h | 17.236 | 16.904 | 16.862 | 16.827 | 17.063 | 16.853 | 16.664 | 16.598 | 16.653 | 16.688 |
| 7d | 17.553 | 16.586 | 16.570 | 16.583 | 16.766 | 16.831 | 16.402 | 16.389 | 16.407 | 16.442 |
| 30d | 16.606 | 15.982 | 15.928 | 15.874 | 16.119 | 16.085 | 15.807 | 15.787 | 15.791 | 15.821 |

## Next candle

- candle starting 2026-11-11 18:09 UTC, last close 2084.81
- P(up) 0.4863, return quantiles (bp): {'05': -10.787, '10': -7.643, '25': -3.836, '40': -1.878, '50': -0.291, '60': 1.884, '75': 4.694, '90': 8.752, '95': 12.249}
- changepoint probability 0.0412, regime age 41.2 min
- agent weights: empirical 0.003, ewma 0.013, garch 0.021, har 0.072, bocpd 0.004, hmm 0.059, online_qr 0.242, lgbm 0.585

## Learning log

- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- HMM volatility states (sd, bp per minute): [2.2, 5.74, 18.32], current probabilities: [0.074, 0.921, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-11-11 18:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.526, 'l_abs': 0.625, 'l_hi': 0.763, 'l_lo': 0.738, 'b05': 0.714, 'b25': 0.688, 'b75': 0.692, 'b95': 0.708}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.406, 1.796, 2.39, 2.731, 3.058, 3.515, 3.273, 3.549, 3.53, 3.357, 3.513, 3.813, 4.127, 4.196]}
- calibration offsets (in sigma): {'05': 0.074, '10': 0.098, '25': 0.03, '40': -0.048, '50': -0.05, '60': -0.002, '75': 0.01, '90': -0.008, '95': 0.026}
