# ETH-USD 60s candle generator - report

- generated: 2026-11-11 10:49 UTC
- last closed candle: 2026-11-11 10:49 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.522 (672) [0.490, 0.555] | 0.518 (2880) [0.502, 0.535] | 0.513 (6714) [0.502, 0.525] | 0.515 (3742) [0.499, 0.531] | 0.628 (43) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.543 (777) | 0.541 (5503) [0.522, 0.558] | 0.543 (23887) [0.537, 0.549] | 0.523 (54927) [0.517, 0.528] | 0.543 (30689) [0.538, 0.548] | 0.514 (379) | 0.500 | flat +0.007 (noise 0.012) |
| colour_confident | 0.455 (88) | 0.570 (988) [0.540, 0.594] | 0.588 (4263) [0.578, 0.598] | 0.593 (5683) [0.582, 0.604] | 0.593 (5683) [0.582, 0.604] | 0.476 (42) | 0.500 | flat -0.006 (noise 0.023) |
| colour_next | 0.519 (1434) | 0.530 (9968) [0.518, 0.543] | 0.530 (42864) [0.526, 0.534] | 0.517 (99994) [0.513, 0.521] | 0.530 (55645) [0.526, 0.534] | 0.503 (648) | 0.500 | flat -0.000 (noise 0.009) |
| colour_path | 0.496 (20076) | 0.501 (139552) [0.499, 0.504] | 0.502 (600096) [0.500, 0.503] | 0.501 (1399916) [0.500, 0.502] | 0.501 (779030) [0.500, 0.502] | 0.504 (9072) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.733 (15) | 0.625 (264) [0.589, 0.647] | 0.622 (1111) [0.606, 0.639] | 0.631 (1508) [0.615, 0.648] | 0.631 (1508) [0.615, 0.648] | 0.000 (1) | 0.500 | flat +0.004 (noise 0.045) |
| reversal_k13_next | 0.384 (73) | 0.328 (472) [0.305, 0.353] | 0.324 (1839) [0.310, 0.340] | 0.314 (4624) [0.304, 0.324] | 0.326 (2519) [0.315, 0.338] | 0.382 (34) | 0.077 | flat -0.024 (noise 0.033) |
| reversal_k13_now | 0.646 (48) | 0.573 (351) [0.546, 0.602] | 0.561 (1638) [0.542, 0.581] | 0.574 (3606) [0.561, 0.587] | 0.568 (2134) [0.551, 0.586] | 0.560 (25) | 0.077 | flat -0.009 (noise 0.036) |
| reversal_k3_next | 0.521 (48) | 0.619 (352) [0.588, 0.646] | 0.589 (2826) [0.578, 0.601] | 0.588 (6053) [0.579, 0.596] | 0.588 (3613) [0.577, 0.598] | 0.500 (18) | 0.293 | flat +0.022 (noise 0.031) |
| reversal_k3_now | 0.919 (62) | 0.921 (406) [0.912, 0.931] | 0.933 (1717) [0.923, 0.944] | 0.935 (4025) [0.930, 0.941] | 0.931 (2262) [0.923, 0.939] | 0.938 (32) | 0.294 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.532 (62) | 0.533 (392) [0.511, 0.553] | 0.488 (2680) [0.472, 0.505] | 0.486 (5400) [0.475, 0.497] | 0.481 (3410) [0.466, 0.496] | 0.292 (24) | 0.187 | flat -0.002 (noise 0.036) |
| reversal_k5_now | 0.829 (70) | 0.799 (368) [0.758, 0.832] | 0.812 (1627) [0.800, 0.823] | 0.825 (3736) [0.816, 0.834] | 0.816 (2125) [0.805, 0.826] | 0.641 (39) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.443 (70) | 0.422 (445) [0.392, 0.454] | 0.397 (2622) [0.383, 0.412] | 0.396 (5502) [0.386, 0.406] | 0.396 (3396) [0.383, 0.408] | 0.394 (33) | 0.121 | flat -0.016 (noise 0.032) |
| reversal_k8_now | 0.737 (57) | 0.695 (357) [0.671, 0.716] | 0.686 (1524) [0.666, 0.704] | 0.701 (3639) [0.688, 0.713] | 0.691 (2052) [0.673, 0.708] | 0.645 (31) | 0.122 | flat -0.019 (noise 0.034) |
| overall | 0.500 (22096) | 0.505 (153335) [0.503, 0.508] | 0.505 (662313) [0.504, 0.507] | 0.504 (1543209) [0.503, 0.505] | 0.505 (859928) [0.504, 0.506] | 0.506 (9999) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07682, 0.1174] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5294, 'levels': [{'threshold': 0.07682, 'calls_per_day': 143.0, 'win_rate': 0.5711}, {'threshold': 0.1174, 'calls_per_day': 36.0, 'win_rate': 0.6196}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42866, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15097 | 0.343 | 0.531 (14842) | 0.569 (2337) | 0.738 (2545) |
| volatility: normal | 15096 | 0.369 | 0.533 (15033) | 0.605 (1373) | 0.746 (2251) |
| volatility: wild | 15096 | 0.385 | 0.525 (15056) | 0.613 (791) | 0.772 (2068) |
| session: Asia 00-08 | 15360 | 0.365 | 0.535 (15226) | 0.593 (1608) | 0.752 (2306) |
| session: Europe 08-13 | 9469 | 0.360 | 0.534 (9387) | 0.587 (1178) | 0.752 (1551) |
| session: US 13-21 | 14880 | 0.372 | 0.527 (14776) | 0.597 (1167) | 0.751 (2232) |
| session: late 21-24 | 5580 | 0.358 | 0.513 (5542) | 0.555 (548) | 0.745 (775) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.352 | 0.364 | 0.243 | 0.243 | 0.500 | 0.249 | 0.454 | 1.419 |
| 6h | 360 | 0.370 | 0.382 | 0.284 | 0.314 | 0.510 | 0.255 | 0.485 | 1.215 |
| 24h | 1440 | 0.371 | 0.373 | 0.291 | 0.325 | 0.498 | 0.253 | 0.489 | 1.158 |
| 7d | 10080 | 0.369 | 0.363 | 0.280 | 0.312 | 0.530 | 0.264 | 0.473 | 1.372 |
| 30d | 43200 | 0.367 | 0.360 | 0.278 | 0.310 | 0.530 | 0.264 | 0.470 | 1.259 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.352 / 0.500 / 0.883; 2: 0.387 / 0.617 / 0.917; 3: 0.383 / 0.617 / 0.900; 4: 0.352 / 0.433 / 0.883; 5: 0.363 / 0.567 / 0.933; 6: 0.354 / 0.517 / 0.933; 7: 0.339 / 0.450 / 0.983; 8: 0.357 / 0.500 / 0.933; 9: 0.357 / 0.567 / 0.933; 10: 0.333 / 0.417 / 0.900; 11: 0.359 / 0.533 / 0.900; 12: 0.326 / 0.433 / 0.917; 13: 0.359 / 0.550 / 0.900; 14: 0.332 / 0.467 / 0.917; 15: 0.330 / 0.433 / 0.933
- 6h: 1: 0.370 / 0.510 / 0.889; 2: 0.373 / 0.524 / 0.878; 3: 0.372 / 0.518 / 0.903; 4: 0.372 / 0.504 / 0.900; 5: 0.369 / 0.507 / 0.928; 6: 0.371 / 0.510 / 0.928; 7: 0.359 / 0.487 / 0.936; 8: 0.374 / 0.499 / 0.922; 9: 0.374 / 0.535 / 0.933; 10: 0.351 / 0.443 / 0.908; 11: 0.362 / 0.493 / 0.892; 12: 0.345 / 0.446 / 0.911; 13: 0.369 / 0.524 / 0.897; 14: 0.359 / 0.482 / 0.908; 15: 0.363 / 0.490 / 0.911
- 24h: 1: 0.371 / 0.498 / 0.894; 2: 0.367 / 0.500 / 0.885; 3: 0.373 / 0.517 / 0.893; 4: 0.365 / 0.487 / 0.887; 5: 0.368 / 0.512 / 0.890; 6: 0.366 / 0.497 / 0.891; 7: 0.362 / 0.491 / 0.904; 8: 0.369 / 0.508 / 0.885; 9: 0.364 / 0.495 / 0.886; 10: 0.365 / 0.497 / 0.893; 11: 0.365 / 0.513 / 0.885; 12: 0.357 / 0.487 / 0.890; 13: 0.366 / 0.510 / 0.887; 14: 0.359 / 0.495 / 0.889; 15: 0.360 / 0.490 / 0.894
- 7d: 1: 0.369 / 0.530 / 0.896; 2: 0.356 / 0.489 / 0.898; 3: 0.360 / 0.515 / 0.899; 4: 0.355 / 0.497 / 0.899; 5: 0.357 / 0.505 / 0.900; 6: 0.353 / 0.497 / 0.899; 7: 0.353 / 0.497 / 0.900; 8: 0.355 / 0.503 / 0.898; 9: 0.357 / 0.507 / 0.899; 10: 0.355 / 0.504 / 0.898; 11: 0.355 / 0.506 / 0.898; 12: 0.353 / 0.506 / 0.898; 13: 0.352 / 0.495 / 0.898; 14: 0.353 / 0.505 / 0.899; 15: 0.351 / 0.496 / 0.899
- 30d: 1: 0.367 / 0.530 / 0.898; 2: 0.354 / 0.494 / 0.900; 3: 0.357 / 0.510 / 0.900; 4: 0.353 / 0.498 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.501 / 0.900; 7: 0.352 / 0.498 / 0.900; 8: 0.352 / 0.504 / 0.900; 9: 0.353 / 0.504 / 0.900; 10: 0.352 / 0.503 / 0.900; 11: 0.350 / 0.500 / 0.900; 12: 0.351 / 0.503 / 0.900; 13: 0.350 / 0.499 / 0.900; 14: 0.350 / 0.501 / 0.900; 15: 0.351 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.107 (body 0.066, range 0.148); 'price stays where it was' would score 0.084; colour right 0.500; typical miss of the close 9.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.147 (body 0.101, range 0.194); 'price stays where it was' would score 0.110; colour right 0.490; typical miss of the close 8.4 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.126 (body 0.083, range 0.169); 'price stays where it was' would score 0.116; colour right 0.486; typical miss of the close 11.8 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.164); 'price stays where it was' would score 0.123; colour right 0.502; typical miss of the close 9.0 bp; chain ended on the right side 0.531 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.518 of 2880 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.6; 2: 0.202 / 5.4; 3: 0.167 / 7.1; 4: 0.132 / 7.3; 5: 0.125 / 8.0; 6: 0.115 / 8.9; 7: 0.110 / 9.1; 8: 0.097 / 10.2; 9: 0.091 / 10.2; 10: 0.091 / 10.7; 11: 0.088 / 10.8; 12: 0.078 / 11.2; 13: 0.073 / 11.7; 14: 0.070 / 12.1; 15: 0.066 / 12.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 144403, probability skill vs chance 0.2292, widened contest next: True
  - now: threshold 0.8388, hit rate recent 0.9206 / long run 0.9267
    - 6h: 17 calls (69 a day), hit rate 0.941, chance 0.277, naive rule 0.498, lift 3.39x
    - 24h: 58 calls (58 a day), hit rate 0.914, chance 0.272, naive rule 0.474, lift 3.36x
    - 7d: 413 calls (59 a day), hit rate 0.925, chance 0.296, naive rule 0.503, lift 3.13x
    - 30d: 1720 calls (57 a day), hit rate 0.933, chance 0.293, naive rule 0.495, lift 3.18x
  - next: threshold 0.5663, hit rate recent 0.5405 / long run 0.6
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.277, lift 1.60x
    - 24h: 41 calls (41 a day), hit rate 0.488, chance 0.272, lift 1.79x
    - 7d: 351 calls (50 a day), hit rate 0.613, chance 0.296, lift 2.07x
    - 30d: 2818 calls (94 a day), hit rate 0.589, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.498; 0.35: 533, 0.523; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.695; 0.55: 309, 0.740; 0.60: 260, 0.785; 0.65: 219, 0.811; 0.70: 172, 0.844; 0.75: 138, 0.875; 0.80: 91, 0.905; 0.85: 46, 0.946; 0.90: 4, 0.992
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 497, 0.463; 0.40: 398, 0.501; 0.45: 300, 0.535; 0.50: 193, 0.567; 0.55: 86, 0.578; 0.60: 12, 0.642; 0.65: 1, 0.571
- **K=5**: model 1794268800, labels learned 144401, probability skill vs chance 0.2101, widened contest next: True
  - now: threshold 0.6837, hit rate recent 0.7238 / long run 0.7968
    - 6h: 20 calls (82 a day), hit rate 0.700, chance 0.160, naive rule 0.382, lift 4.37x
    - 24h: 74 calls (74 a day), hit rate 0.689, chance 0.164, naive rule 0.363, lift 4.20x
    - 7d: 383 calls (55 a day), hit rate 0.778, chance 0.185, naive rule 0.405, lift 4.20x
    - 30d: 1644 calls (55 a day), hit rate 0.807, chance 0.185, naive rule 0.404, lift 4.35x
  - next: threshold 0.4578, hit rate recent 0.448 / long run 0.5116
    - 6h: 12 calls (49 a day), hit rate 0.250, chance 0.160, lift 1.56x
    - 24h: 54 calls (54 a day), hit rate 0.407, chance 0.164, lift 2.48x
    - 7d: 393 calls (56 a day), hit rate 0.522, chance 0.185, lift 2.81x
    - 30d: 2672 calls (89 a day), hit rate 0.486, chance 0.185, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.419; 0.35: 353, 0.480; 0.40: 286, 0.552; 0.45: 233, 0.605; 0.50: 187, 0.653; 0.55: 150, 0.692; 0.60: 112, 0.741; 0.65: 76, 0.777; 0.70: 47, 0.815; 0.75: 28, 0.850; 0.80: 10, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.382; 0.35: 257, 0.420; 0.40: 160, 0.457; 0.45: 65, 0.493; 0.50: 10, 0.506; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 144398, probability skill vs chance 0.21, widened contest next: False
  - now: threshold 0.5671, hit rate recent 0.6991 / long run 0.6922
    - 6h: 15 calls (62 a day), hit rate 0.733, chance 0.123, naive rule 0.333, lift 5.97x
    - 24h: 57 calls (57 a day), hit rate 0.702, chance 0.122, naive rule 0.333, lift 5.73x
    - 7d: 362 calls (52 a day), hit rate 0.691, chance 0.122, naive rule 0.340, lift 5.68x
    - 30d: 1530 calls (51 a day), hit rate 0.684, chance 0.120, naive rule 0.333, lift 5.69x
  - next: threshold 0.3634, hit rate recent 0.4286 / long run 0.4181
    - 6h: 18 calls (74 a day), hit rate 0.389, chance 0.123, lift 3.17x
    - 24h: 70 calls (70 a day), hit rate 0.414, chance 0.122, lift 3.39x
    - 7d: 457 calls (65 a day), hit rate 0.420, chance 0.122, lift 3.45x
    - 30d: 2623 calls (87 a day), hit rate 0.396, chance 0.120, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 192, 0.490; 0.40: 152, 0.536; 0.45: 118, 0.583; 0.50: 85, 0.635; 0.55: 60, 0.671; 0.60: 39, 0.709; 0.65: 24, 0.776; 0.70: 12, 0.812; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 171, 0.363; 0.35: 87, 0.393; 0.40: 23, 0.424; 0.45: 4, 0.427; 0.50: 1, 0.762
- **K=13**: model 1794355200, labels learned 144393, probability skill vs chance 0.192, widened contest next: False
  - now: threshold 0.4511, hit rate recent 0.6029 / long run 0.5725
    - 6h: 11 calls (46 a day), hit rate 0.636, chance 0.084, naive rule 0.283, lift 7.57x
    - 24h: 46 calls (46 a day), hit rate 0.609, chance 0.085, naive rule 0.303, lift 7.20x
    - 7d: 349 calls (50 a day), hit rate 0.567, chance 0.079, naive rule 0.288, lift 7.18x
    - 30d: 1639 calls (55 a day), hit rate 0.561, chance 0.077, naive rule 0.281, lift 7.24x
  - next: threshold 0.29, hit rate recent 0.3898 / long run 0.3389
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.084, lift 3.97x
    - 24h: 72 calls (73 a day), hit rate 0.403, chance 0.085, lift 4.76x
    - 7d: 491 calls (70 a day), hit rate 0.332, chance 0.079, lift 4.20x
    - 30d: 1842 calls (61 a day), hit rate 0.326, chance 0.077, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.430; 0.35: 97, 0.477; 0.40: 68, 0.537; 0.45: 46, 0.582; 0.50: 31, 0.638; 0.55: 21, 0.658; 0.60: 12, 0.696; 0.65: 4, 0.670; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.332; 0.35: 13, 0.339; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.050 | 2.99% | 0.883 | 0.550 | 0.248 | 0.583 | 0.005 |
| 6h | 14.023 | 1.92% | 0.894 | 0.503 | 0.250 | 0.535 | 0.191 |
| 24h | 19.389 | 4.47% | 0.897 | 0.507 | 0.251 | 0.492 | 0.511 |
| 7d | 16.630 | 6.36% | 0.899 | 0.500 | 0.251 | 0.502 | 0.693 |
| 30d | 15.769 | 4.71% | 0.900 | 0.500 | 0.250 | 0.502 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.453 | 13.077 | 13.133 | 13.042 | 13.129 | 13.272 | 13.125 | 12.961 | 13.041 | 13.050 |
| 6h | 14.299 | 14.002 | 14.022 | 14.109 | 14.066 | 14.127 | 13.971 | 13.989 | 13.979 | 14.023 |
| 24h | 20.296 | 19.518 | 19.527 | 19.526 | 19.783 | 19.616 | 19.363 | 19.359 | 19.360 | 19.389 |
| 7d | 17.760 | 16.759 | 16.737 | 16.757 | 16.929 | 17.039 | 16.601 | 16.589 | 16.596 | 16.630 |
| 30d | 16.547 | 15.924 | 15.872 | 15.819 | 16.060 | 16.032 | 15.754 | 15.736 | 15.738 | 15.769 |

## Next candle

- candle starting 2026-11-11 10:49 UTC, last close 2055.82
- P(up) 0.5338, return quantiles (bp): {'05': -8.561, '10': -6.367, '25': -2.983, '40': -0.913, '50': 0.456, '60': 1.5, '75': 3.507, '90': 6.531, '95': 8.465}
- changepoint probability 0.051, regime age 416.3 min
- agent weights: empirical 0.009, ewma 0.145, garch 0.140, har 0.110, bocpd 0.056, hmm 0.059, online_qr 0.228, lgbm 0.252

## Learning log

- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- 2026-11-10 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.32, 6.18, 17.35], "stay": [0.99, 0.975, 0.939]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25158, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48381, "challengers": 1, "chance_loss": 0.60555, "widened": false, "champion_loss": 0.48264, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37224, "challengers": 3, "chance_loss": 0.47928, "widened": true, "champion_loss": 0.37283, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27274, "challengers": 1, "chance_loss": 0.36464, "widened": false, "champion_loss": 0.27266, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19883, "challengers": 1, "chance_loss": 0.27546, "widened": false, "champion_loss": 0.19846, "promoted": false}}
- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.27, 5.87, 18.61], current probabilities: [0.0, 0.979, 0.021]
- live generator: {'versions': 60, 'latest_effective': '2026-11-11 11:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.392, 'l_abs': 0.599, 'l_hi': 0.775, 'l_lo': 0.745, 'b05': 0.713, 'b25': 0.68, 'b75': 0.67, 'b95': 0.718}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.823, 1.907, 2.342, 2.281, 2.606, 2.604, 3.273, 3.41, 3.901, 4.716, 4.291, 4.657, 4.295, 4.455]}
- calibration offsets (in sigma): {'05': 0.004, '10': 0.008, '25': 0.04, '40': 0.032, '50': 0.06, '60': 0.028, '75': -0.0, '90': 0.002, '95': -0.014}
