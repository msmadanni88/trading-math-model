# ETH-USD 60s candle generator - report

- generated: 2026-11-11 03:07 UTC
- last closed candle: 2026-11-11 03:07 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.522 (672) [0.490, 0.555] | 0.518 (2880) [0.502, 0.535] | 0.513 (6714) [0.502, 0.525] | 0.515 (3742) [0.499, 0.531] | 0.667 (12) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.543 (777) | 0.541 (5503) [0.522, 0.558] | 0.543 (23887) [0.537, 0.549] | 0.523 (54927) [0.517, 0.528] | 0.543 (30689) [0.538, 0.548] | 0.559 (111) | 0.500 | flat +0.007 (noise 0.012) |
| colour_confident | 0.455 (88) | 0.570 (988) [0.540, 0.594] | 0.588 (4263) [0.578, 0.598] | 0.593 (5683) [0.582, 0.604] | 0.593 (5683) [0.582, 0.604] | 0.167 (6) | 0.500 | flat -0.006 (noise 0.023) |
| colour_next | 0.519 (1434) | 0.530 (9968) [0.518, 0.543] | 0.530 (42864) [0.526, 0.534] | 0.517 (99994) [0.513, 0.521] | 0.530 (55645) [0.526, 0.534] | 0.513 (187) | 0.500 | flat -0.000 (noise 0.009) |
| colour_path | 0.496 (20076) | 0.501 (139552) [0.499, 0.504] | 0.502 (600096) [0.500, 0.503] | 0.501 (1399916) [0.500, 0.502] | 0.501 (779030) [0.500, 0.502] | 0.516 (2618) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.733 (15) | 0.625 (264) [0.589, 0.647] | 0.622 (1111) [0.606, 0.639] | 0.631 (1508) [0.615, 0.648] | 0.631 (1508) [0.615, 0.648] | - | 0.500 | flat +0.004 (noise 0.045) |
| reversal_k13_next | 0.384 (73) | 0.328 (472) [0.305, 0.353] | 0.324 (1839) [0.310, 0.340] | 0.314 (4624) [0.304, 0.324] | 0.326 (2519) [0.315, 0.338] | 0.385 (13) | 0.077 | flat -0.024 (noise 0.033) |
| reversal_k13_now | 0.646 (48) | 0.573 (351) [0.546, 0.602] | 0.561 (1638) [0.542, 0.581] | 0.574 (3606) [0.561, 0.587] | 0.568 (2134) [0.551, 0.586] | 0.417 (12) | 0.077 | flat -0.009 (noise 0.036) |
| reversal_k3_next | 0.521 (48) | 0.619 (352) [0.588, 0.646] | 0.589 (2826) [0.578, 0.601] | 0.588 (6053) [0.579, 0.596] | 0.588 (3613) [0.577, 0.598] | 0.600 (5) | 0.293 | flat +0.022 (noise 0.031) |
| reversal_k3_now | 0.919 (62) | 0.921 (406) [0.912, 0.931] | 0.933 (1717) [0.923, 0.944] | 0.935 (4025) [0.930, 0.941] | 0.931 (2262) [0.923, 0.939] | 0.923 (13) | 0.294 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.532 (62) | 0.533 (392) [0.511, 0.553] | 0.488 (2680) [0.472, 0.505] | 0.486 (5400) [0.475, 0.497] | 0.481 (3410) [0.466, 0.496] | 0.250 (8) | 0.187 | flat -0.002 (noise 0.036) |
| reversal_k5_now | 0.829 (70) | 0.799 (368) [0.758, 0.832] | 0.812 (1627) [0.800, 0.823] | 0.825 (3736) [0.816, 0.834] | 0.816 (2125) [0.805, 0.826] | 0.571 (14) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.443 (70) | 0.422 (445) [0.392, 0.454] | 0.397 (2622) [0.383, 0.412] | 0.396 (5502) [0.386, 0.406] | 0.396 (3396) [0.383, 0.408] | 0.364 (11) | 0.121 | flat -0.016 (noise 0.032) |
| reversal_k8_now | 0.737 (57) | 0.695 (357) [0.671, 0.716] | 0.686 (1524) [0.666, 0.704] | 0.701 (3639) [0.688, 0.713] | 0.691 (2052) [0.673, 0.708] | 0.538 (13) | 0.122 | flat -0.019 (noise 0.034) |
| overall | 0.500 (22096) | 0.505 (153335) [0.503, 0.508] | 0.505 (662313) [0.504, 0.507] | 0.504 (1543209) [0.503, 0.505] | 0.505 (859928) [0.504, 0.506] | 0.516 (2906) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07694, 0.1174] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5294, 'levels': [{'threshold': 0.07694, 'calls_per_day': 143.3, 'win_rate': 0.569}, {'threshold': 0.1174, 'calls_per_day': 36.2, 'win_rate': 0.625}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42865, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14943 | 0.343 | 0.531 (14689) | 0.569 (2320) | 0.736 (2510) |
| volatility: normal | 14942 | 0.369 | 0.534 (14877) | 0.607 (1364) | 0.750 (2246) |
| volatility: wild | 14942 | 0.385 | 0.525 (14904) | 0.611 (781) | 0.770 (2033) |
| session: Asia 00-08 | 15067 | 0.365 | 0.536 (14933) | 0.593 (1588) | 0.753 (2263) |
| session: Europe 08-13 | 9300 | 0.359 | 0.534 (9219) | 0.588 (1162) | 0.749 (1519) |
| session: US 13-21 | 14880 | 0.372 | 0.527 (14776) | 0.597 (1167) | 0.751 (2232) |
| session: late 21-24 | 5580 | 0.358 | 0.513 (5542) | 0.555 (548) | 0.745 (775) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.406 | 0.380 | 0.312 | 0.312 | 0.583 | 0.301 | 0.512 | 1.162 |
| 6h | 360 | 0.365 | 0.363 | 0.276 | 0.300 | 0.494 | 0.252 | 0.479 | 1.236 |
| 24h | 1440 | 0.375 | 0.369 | 0.293 | 0.323 | 0.512 | 0.263 | 0.487 | 1.184 |
| 7d | 10080 | 0.369 | 0.362 | 0.281 | 0.312 | 0.530 | 0.265 | 0.473 | 1.396 |
| 30d | 43200 | 0.367 | 0.359 | 0.278 | 0.310 | 0.530 | 0.264 | 0.470 | 1.256 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.406 / 0.583 / 0.933; 2: 0.356 / 0.417 / 0.900; 3: 0.389 / 0.500 / 0.833; 4: 0.369 / 0.467 / 0.867; 5: 0.391 / 0.500 / 0.900; 6: 0.399 / 0.567 / 0.917; 7: 0.356 / 0.400 / 1.000; 8: 0.392 / 0.567 / 0.967; 9: 0.376 / 0.450 / 0.917; 10: 0.362 / 0.467 / 0.983; 11: 0.408 / 0.667 / 0.983; 12: 0.380 / 0.533 / 1.000; 13: 0.386 / 0.533 / 1.000; 14: 0.379 / 0.517 / 1.000; 15: 0.390 / 0.533 / 1.000
- 6h: 1: 0.365 / 0.494 / 0.878; 2: 0.353 / 0.472 / 0.900; 3: 0.372 / 0.528 / 0.900; 4: 0.356 / 0.475 / 0.919; 5: 0.359 / 0.511 / 0.931; 6: 0.357 / 0.494 / 0.908; 7: 0.350 / 0.483 / 0.903; 8: 0.367 / 0.528 / 0.933; 9: 0.348 / 0.447 / 0.906; 10: 0.351 / 0.486 / 0.917; 11: 0.371 / 0.558 / 0.917; 12: 0.364 / 0.544 / 0.911; 13: 0.352 / 0.483 / 0.925; 14: 0.355 / 0.528 / 0.933; 15: 0.355 / 0.503 / 0.922
- 24h: 1: 0.375 / 0.512 / 0.896; 2: 0.363 / 0.490 / 0.922; 3: 0.368 / 0.519 / 0.922; 4: 0.361 / 0.485 / 0.910; 5: 0.359 / 0.488 / 0.902; 6: 0.360 / 0.496 / 0.913; 7: 0.360 / 0.493 / 0.924; 8: 0.363 / 0.507 / 0.907; 9: 0.358 / 0.485 / 0.901; 10: 0.364 / 0.510 / 0.924; 11: 0.362 / 0.513 / 0.918; 12: 0.355 / 0.491 / 0.913; 13: 0.359 / 0.503 / 0.910; 14: 0.360 / 0.508 / 0.913; 15: 0.357 / 0.494 / 0.906
- 7d: 1: 0.369 / 0.530 / 0.898; 2: 0.356 / 0.487 / 0.900; 3: 0.360 / 0.515 / 0.900; 4: 0.354 / 0.495 / 0.900; 5: 0.356 / 0.502 / 0.900; 6: 0.353 / 0.497 / 0.901; 7: 0.353 / 0.496 / 0.900; 8: 0.355 / 0.502 / 0.900; 9: 0.356 / 0.507 / 0.900; 10: 0.355 / 0.507 / 0.900; 11: 0.355 / 0.508 / 0.900; 12: 0.354 / 0.509 / 0.901; 13: 0.352 / 0.495 / 0.900; 14: 0.354 / 0.509 / 0.900; 15: 0.351 / 0.496 / 0.901
- 30d: 1: 0.367 / 0.530 / 0.898; 2: 0.354 / 0.494 / 0.900; 3: 0.357 / 0.510 / 0.900; 4: 0.353 / 0.497 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.501 / 0.900; 7: 0.352 / 0.499 / 0.900; 8: 0.352 / 0.504 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.352 / 0.504 / 0.900; 11: 0.350 / 0.500 / 0.900; 12: 0.351 / 0.504 / 0.900; 13: 0.350 / 0.499 / 0.900; 14: 0.350 / 0.502 / 0.900; 15: 0.350 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.183 (body 0.136, range 0.230); 'price stays where it was' would score 0.142; colour right 0.483; typical miss of the close 7.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.091, range 0.160); 'price stays where it was' would score 0.122; colour right 0.469; typical miss of the close 9.2 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.115 (body 0.074, range 0.156); 'price stays where it was' would score 0.114; colour right 0.491; typical miss of the close 13.1 bp; chain ended on the right side 0.469 of 96 chains; n=1440
- 7d: match 0.123 (body 0.082, range 0.163); 'price stays where it was' would score 0.123; colour right 0.503; typical miss of the close 9.1 bp; chain ended on the right side 0.528 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.128; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.519 of 2880 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.6; 2: 0.201 / 5.4; 3: 0.166 / 7.1; 4: 0.131 / 7.3; 5: 0.126 / 8.0; 6: 0.115 / 8.9; 7: 0.110 / 9.2; 8: 0.097 / 10.2; 9: 0.091 / 10.2; 10: 0.091 / 10.7; 11: 0.087 / 10.7; 12: 0.078 / 11.2; 13: 0.073 / 11.6; 14: 0.070 / 12.1; 15: 0.066 / 12.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 143941, probability skill vs chance 0.2283, widened contest next: True
  - now: threshold 0.8386, hit rate recent 0.9095 / long run 0.926
    - 6h: 20 calls (81 a day), hit rate 0.850, chance 0.300, naive rule 0.478, lift 2.83x
    - 24h: 62 calls (62 a day), hit rate 0.919, chance 0.272, naive rule 0.465, lift 3.38x
    - 7d: 408 calls (58 a day), hit rate 0.922, chance 0.296, naive rule 0.502, lift 3.11x
    - 30d: 1724 calls (57 a day), hit rate 0.933, chance 0.293, naive rule 0.494, lift 3.18x
  - next: threshold 0.5663, hit rate recent 0.5618 / long run 0.6031
    - 6h: 9 calls (37 a day), hit rate 0.333, chance 0.300, lift 1.11x
    - 24h: 44 calls (44 a day), hit rate 0.545, chance 0.272, lift 2.00x
    - 7d: 353 calls (50 a day), hit rate 0.618, chance 0.296, lift 2.08x
    - 30d: 2824 calls (94 a day), hit rate 0.589, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.498; 0.35: 533, 0.523; 0.40: 474, 0.578; 0.45: 406, 0.649; 0.50: 357, 0.695; 0.55: 309, 0.740; 0.60: 260, 0.785; 0.65: 219, 0.811; 0.70: 173, 0.844; 0.75: 139, 0.875; 0.80: 92, 0.906; 0.85: 46, 0.946; 0.90: 4, 0.992
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 498, 0.463; 0.40: 399, 0.500; 0.45: 300, 0.535; 0.50: 194, 0.568; 0.55: 87, 0.578; 0.60: 12, 0.639; 0.65: 1, 0.600
- **K=5**: model 1794268800, labels learned 143939, probability skill vs chance 0.2089, widened contest next: True
  - now: threshold 0.6828, hit rate recent 0.7373 / long run 0.8017
    - 6h: 23 calls (94 a day), hit rate 0.652, chance 0.153, naive rule 0.333, lift 4.26x
    - 24h: 73 calls (73 a day), hit rate 0.767, chance 0.169, naive rule 0.370, lift 4.53x
    - 7d: 371 calls (53 a day), hit rate 0.792, chance 0.186, naive rule 0.407, lift 4.25x
    - 30d: 1637 calls (55 a day), hit rate 0.810, chance 0.186, naive rule 0.404, lift 4.36x
  - next: threshold 0.4572, hit rate recent 0.4923 / long run 0.517
    - 6h: 17 calls (69 a day), hit rate 0.412, chance 0.153, lift 2.69x
    - 24h: 62 calls (62 a day), hit rate 0.484, chance 0.169, lift 2.86x
    - 7d: 394 calls (56 a day), hit rate 0.525, chance 0.186, lift 2.82x
    - 30d: 2683 calls (89 a day), hit rate 0.487, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.419; 0.35: 353, 0.481; 0.40: 285, 0.553; 0.45: 233, 0.606; 0.50: 187, 0.654; 0.55: 150, 0.692; 0.60: 113, 0.742; 0.65: 76, 0.779; 0.70: 47, 0.816; 0.75: 28, 0.850; 0.80: 10, 0.873
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.381; 0.35: 257, 0.420; 0.40: 160, 0.459; 0.45: 66, 0.492; 0.50: 10, 0.505; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 143936, probability skill vs chance 0.208, widened contest next: False
  - now: threshold 0.5669, hit rate recent 0.6879 / long run 0.6913
    - 6h: 19 calls (78 a day), hit rate 0.632, chance 0.110, naive rule 0.288, lift 5.74x
    - 24h: 61 calls (61 a day), hit rate 0.738, chance 0.122, naive rule 0.338, lift 6.05x
    - 7d: 359 calls (51 a day), hit rate 0.694, chance 0.122, naive rule 0.342, lift 5.68x
    - 30d: 1529 calls (51 a day), hit rate 0.685, chance 0.120, naive rule 0.333, lift 5.70x
  - next: threshold 0.3629, hit rate recent 0.4325 / long run 0.4184
    - 6h: 19 calls (78 a day), hit rate 0.474, chance 0.110, lift 4.31x
    - 24h: 75 calls (76 a day), hit rate 0.440, chance 0.122, lift 3.61x
    - 7d: 449 calls (64 a day), hit rate 0.421, chance 0.122, lift 3.45x
    - 30d: 2626 calls (88 a day), hit rate 0.396, chance 0.120, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.426; 0.35: 192, 0.491; 0.40: 152, 0.537; 0.45: 118, 0.583; 0.50: 85, 0.636; 0.55: 60, 0.672; 0.60: 39, 0.710; 0.65: 24, 0.778; 0.70: 12, 0.814; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.363; 0.35: 87, 0.392; 0.40: 23, 0.422; 0.45: 4, 0.419; 0.50: 1, 0.727
- **K=13**: model 1794355200, labels learned 143931, probability skill vs chance 0.1898, widened contest next: False
  - now: threshold 0.4522, hit rate recent 0.5805 / long run 0.5699
    - 6h: 17 calls (71 a day), hit rate 0.529, chance 0.072, naive rule 0.257, lift 7.31x
    - 24h: 52 calls (53 a day), hit rate 0.615, chance 0.086, naive rule 0.312, lift 7.19x
    - 7d: 351 calls (50 a day), hit rate 0.573, chance 0.079, naive rule 0.289, lift 7.24x
    - 30d: 1642 calls (55 a day), hit rate 0.560, chance 0.077, naive rule 0.281, lift 7.24x
  - next: threshold 0.2875, hit rate recent 0.3917 / long run 0.3373
    - 6h: 23 calls (96 a day), hit rate 0.435, chance 0.072, lift 6.00x
    - 24h: 77 calls (78 a day), hit rate 0.416, chance 0.086, lift 4.85x
    - 7d: 479 calls (69 a day), hit rate 0.330, chance 0.079, lift 4.17x
    - 30d: 1845 calls (62 a day), hit rate 0.325, chance 0.077, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.430; 0.35: 97, 0.478; 0.40: 68, 0.536; 0.45: 46, 0.582; 0.50: 31, 0.639; 0.55: 21, 0.660; 0.60: 12, 0.696; 0.65: 4, 0.670; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.330; 0.35: 13, 0.338; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.462 | 0.77% | 0.933 | 0.500 | 0.251 | 0.467 | 0.077 |
| 6h | 13.916 | 2.97% | 0.889 | 0.494 | 0.251 | 0.486 | 0.433 |
| 24h | 20.028 | 4.41% | 0.891 | 0.500 | 0.251 | 0.489 | 0.506 |
| 7d | 16.855 | 6.32% | 0.900 | 0.500 | 0.251 | 0.501 | 0.690 |
| 30d | 15.763 | 4.70% | 0.900 | 0.500 | 0.250 | 0.501 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.583 | 15.472 | 15.538 | 15.564 | 15.738 | 15.474 | 15.480 | 15.542 | 15.473 | 15.462 |
| 6h | 14.342 | 14.013 | 13.974 | 14.034 | 14.140 | 14.101 | 13.867 | 13.862 | 13.877 | 13.916 |
| 24h | 20.951 | 20.186 | 20.185 | 20.133 | 20.542 | 20.302 | 20.004 | 19.985 | 19.992 | 20.028 |
| 7d | 17.992 | 16.991 | 16.967 | 16.982 | 17.172 | 17.265 | 16.826 | 16.813 | 16.821 | 16.855 |
| 30d | 16.541 | 15.920 | 15.868 | 15.814 | 16.055 | 16.027 | 15.749 | 15.730 | 15.734 | 15.763 |

## Next candle

- candle starting 2026-11-11 03:07 UTC, last close 2060.73
- P(up) 0.4733, return quantiles (bp): {'05': -9.179, '10': -6.978, '25': -3.984, '40': -2.003, '50': -0.433, '60': 1.21, '75': 3.616, '90': 7.952, '95': 10.366}
- changepoint probability 0.0432, regime age 66.0 min
- agent weights: empirical 0.004, ewma 0.097, garch 0.106, har 0.100, bocpd 0.022, hmm 0.052, online_qr 0.300, lgbm 0.319

## Learning log

- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.27, 5.87, 18.61], current probabilities: [0.0, 0.982, 0.017]
- live generator: {'versions': 60, 'latest_effective': '2026-11-11 03:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.264, 'l_abs': 0.637, 'l_hi': 0.771, 'l_lo': 0.746, 'b05': 0.72, 'b25': 0.7, 'b75': 0.65, 'b95': 0.726}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.469, 1.914, 2.215, 2.582, 2.835, 3.13, 3.221, 3.86, 3.616, 3.877, 4.223, 4.147, 4.313, 4.563]}
- calibration offsets (in sigma): {'05': 0.033, '10': 0.076, '25': 0.035, '40': -0.006, '50': 0.02, '60': 0.036, '75': 0.035, '90': 0.074, '95': 0.007}
