# ETH-USD 60s candle generator - report

- generated: 2026-10-09 22:56 UTC
- last closed candle: 2026-10-09 22:56 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.506 (670) [0.454, 0.558] | 0.505 (2875) [0.485, 0.526] | 0.509 (3547) [0.492, 0.526] | 0.499 (575) [0.443, 0.557] | 0.494 (91) | 0.500 | flat -0.002 (noise 0.040) |
| colour_clear | 0.555 (827) | 0.540 (5230) [0.526, 0.552] | 0.507 (23188) [0.500, 0.514] | 0.504 (28748) [0.498, 0.510] | 0.547 (4510) [0.536, 0.556] | 0.542 (764) | 0.500 | up +0.048 (noise 0.010) |
| colour_confident | 0.596 (89) | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.672 (125) | 0.500 | - |
| colour_next | 0.528 (1434) | 0.527 (9974) [0.517, 0.538] | 0.507 (42883) [0.501, 0.512] | 0.505 (52891) [0.501, 0.510] | 0.531 (8542) [0.521, 0.541] | 0.514 (1370) | 0.500 | up +0.025 (noise 0.007) |
| colour_path | 0.497 (20076) | 0.498 (139636) [0.495, 0.502] | 0.501 (600362) [0.499, 0.502] | 0.500 (740474) [0.499, 0.502] | 0.499 (119588) [0.494, 0.503] | 0.500 (19180) | 0.500 | flat -0.005 (noise 0.003) |
| colour_strong | 0.500 (20) | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.864 (22) | 0.500 | - |
| reversal_k13_next | 0.318 (66) | 0.312 (525) [0.291, 0.331] | 0.308 (2040) [0.294, 0.324] | 0.304 (2572) [0.290, 0.318] | 0.321 (467) [0.306, 0.336] | 0.324 (71) | 0.077 | flat +0.030 (noise 0.027) |
| reversal_k13_now | 0.612 (49) | 0.591 (391) [0.553, 0.636] | 0.585 (1481) [0.563, 0.609] | 0.582 (1811) [0.564, 0.602] | 0.587 (339) [0.544, 0.641] | 0.682 (44) | 0.077 | flat +0.007 (noise 0.038) |
| reversal_k3_next | 0.521 (71) | 0.572 (547) [0.542, 0.609] | 0.588 (2352) [0.572, 0.603] | 0.585 (2927) [0.572, 0.599] | 0.571 (487) [0.538, 0.613] | 0.549 (82) | 0.292 | flat -0.006 (noise 0.029) |
| reversal_k3_now | 0.917 (72) | 0.927 (399) [0.918, 0.939] | 0.940 (1692) [0.932, 0.948] | 0.939 (2108) [0.932, 0.947] | 0.927 (345) [0.917, 0.941] | 0.931 (58) | 0.292 | flat -0.028 (noise 0.017) |
| reversal_k5_next | 0.422 (71) | 0.449 (642) [0.420, 0.481] | 0.488 (2100) [0.468, 0.506] | 0.483 (2512) [0.466, 0.501] | 0.441 (522) [0.412, 0.480] | 0.479 (73) | 0.187 | flat -0.034 (noise 0.032) |
| reversal_k5_now | 0.758 (62) | 0.826 (397) [0.795, 0.858] | 0.833 (1573) [0.817, 0.849] | 0.835 (1949) [0.821, 0.850] | 0.823 (338) [0.788, 0.858] | 0.795 (44) | 0.187 | flat -0.042 (noise 0.026) |
| reversal_k8_next | 0.367 (120) | 0.387 (587) [0.359, 0.418] | 0.402 (2096) [0.385, 0.421] | 0.394 (2646) [0.379, 0.411] | 0.385 (540) [0.355, 0.418] | 0.397 (78) | 0.121 | flat -0.005 (noise 0.032) |
| reversal_k8_now | 0.625 (64) | 0.715 (411) [0.677, 0.756] | 0.723 (1582) [0.703, 0.742] | 0.713 (1947) [0.695, 0.732] | 0.711 (360) [0.670, 0.756] | 0.614 (44) | 0.121 | flat -0.038 (noise 0.036) |
| overall | 0.500 (22181) | 0.502 (154179) [0.498, 0.507] | 0.503 (661036) [0.502, 0.505] | 0.503 (815384) [0.501, 0.504] | 0.502 (132103) [0.497, 0.508] | 0.503 (21135) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07771, 0.1166] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5323, 'levels': [{'threshold': 0.07771, 'calls_per_day': 145.3, 'win_rate': 0.6148}, {'threshold': 0.1166, 'calls_per_day': 36.3, 'win_rate': 0.6537}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 8780, 'rate': 0.531}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15339 | 0.335 | 0.514 (15124) | 0.611 (712) | 0.775 (2464) |
| volatility: normal | 15338 | 0.361 | 0.511 (15270) | 0.617 (162) | 0.772 (2156) |
| volatility: wild | 15339 | 0.374 | 0.497 (15293) | 0.667 (66) | 0.776 (2134) |
| session: Asia 00-08 | 15360 | 0.353 | 0.508 (15258) | 0.593 (327) | 0.778 (2199) |
| session: Europe 08-13 | 9600 | 0.351 | 0.506 (9540) | 0.598 (194) | 0.764 (1507) |
| session: US 13-21 | 15360 | 0.367 | 0.506 (15260) | 0.630 (249) | 0.782 (2244) |
| session: late 21-24 | 5696 | 0.349 | 0.511 (5629) | 0.659 (170) | 0.765 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.334 | 0.305 | 0.285 | 0.285 | 0.569 | 0.247 | 0.420 | 1.581 |
| 6h | 360 | 0.356 | 0.355 | 0.266 | 0.285 | 0.515 | 0.244 | 0.468 | 1.328 |
| 24h | 1440 | 0.360 | 0.359 | 0.275 | 0.309 | 0.513 | 0.255 | 0.464 | 1.137 |
| 7d | 10080 | 0.351 | 0.345 | 0.271 | 0.296 | 0.528 | 0.253 | 0.448 | 1.228 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.282 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.334 / 0.569 / 0.850; 2: 0.315 / 0.431 / 0.850; 3: 0.311 / 0.534 / 0.967; 4: 0.283 / 0.431 / 0.800; 5: 0.313 / 0.500 / 0.767; 6: 0.290 / 0.448 / 0.700; 7: 0.307 / 0.534 / 0.733; 8: 0.303 / 0.448 / 0.700; 9: 0.320 / 0.483 / 0.717; 10: 0.323 / 0.569 / 0.600; 11: 0.317 / 0.569 / 0.617; 12: 0.318 / 0.552 / 0.567; 13: 0.301 / 0.517 / 0.533; 14: 0.327 / 0.603 / 0.583; 15: 0.301 / 0.431 / 0.567
- 6h: 1: 0.356 / 0.515 / 0.897; 2: 0.351 / 0.499 / 0.919; 3: 0.354 / 0.510 / 0.922; 4: 0.344 / 0.487 / 0.911; 5: 0.340 / 0.445 / 0.906; 6: 0.345 / 0.482 / 0.894; 7: 0.338 / 0.487 / 0.897; 8: 0.355 / 0.530 / 0.886; 9: 0.342 / 0.485 / 0.900; 10: 0.346 / 0.518 / 0.875; 11: 0.355 / 0.546 / 0.875; 12: 0.349 / 0.504 / 0.864; 13: 0.349 / 0.515 / 0.850; 14: 0.353 / 0.538 / 0.853; 15: 0.348 / 0.479 / 0.842
- 24h: 1: 0.360 / 0.513 / 0.899; 2: 0.350 / 0.492 / 0.901; 3: 0.353 / 0.507 / 0.891; 4: 0.355 / 0.513 / 0.903; 5: 0.354 / 0.507 / 0.899; 6: 0.353 / 0.502 / 0.899; 7: 0.345 / 0.490 / 0.897; 8: 0.351 / 0.502 / 0.899; 9: 0.348 / 0.485 / 0.901; 10: 0.352 / 0.500 / 0.895; 11: 0.353 / 0.501 / 0.894; 12: 0.349 / 0.498 / 0.889; 13: 0.349 / 0.495 / 0.888; 14: 0.348 / 0.511 / 0.889; 15: 0.351 / 0.497 / 0.890
- 7d: 1: 0.351 / 0.528 / 0.896; 2: 0.341 / 0.502 / 0.900; 3: 0.343 / 0.509 / 0.899; 4: 0.340 / 0.505 / 0.900; 5: 0.337 / 0.496 / 0.900; 6: 0.336 / 0.494 / 0.900; 7: 0.337 / 0.501 / 0.900; 8: 0.336 / 0.489 / 0.899; 9: 0.333 / 0.487 / 0.900; 10: 0.337 / 0.503 / 0.900; 11: 0.336 / 0.499 / 0.899; 12: 0.336 / 0.500 / 0.898; 13: 0.337 / 0.505 / 0.898; 14: 0.335 / 0.499 / 0.898; 15: 0.335 / 0.493 / 0.898
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.500 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.496 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.101 (body 0.087, range 0.114); 'price stays where it was' would score 0.089; colour right 0.534; typical miss of the close 11.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.137 (body 0.086, range 0.188); 'price stays where it was' would score 0.140; colour right 0.490; typical miss of the close 5.7 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.129 (body 0.090, range 0.169); 'price stays where it was' would score 0.133; colour right 0.494; typical miss of the close 7.5 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.116 (body 0.079, range 0.152); 'price stays where it was' would score 0.119; colour right 0.498; typical miss of the close 6.1 bp; chain ended on the right side 0.498 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.503 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.1; 2: 0.200 / 4.4; 3: 0.167 / 6.1; 4: 0.131 / 6.7; 5: 0.119 / 7.4; 6: 0.111 / 8.1; 7: 0.100 / 8.6; 8: 0.091 / 8.8; 9: 0.086 / 9.1; 10: 0.080 / 9.9; 11: 0.076 / 10.5; 12: 0.075 / 10.9; 13: 0.063 / 11.2; 14: 0.064 / 11.3; 15: 0.061 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 97610, probability skill vs chance 0.234, widened contest next: True
  - now: threshold 0.841, hit rate recent 0.9154 / long run 0.9345
    - 6h: 18 calls (73 a day), hit rate 0.833, chance 0.315, naive rule 0.527, lift 2.64x
    - 24h: 63 calls (63 a day), hit rate 0.921, chance 0.304, naive rule 0.523, lift 3.03x
    - 7d: 403 calls (58 a day), hit rate 0.928, chance 0.293, naive rule 0.490, lift 3.16x
    - 30d: 1706 calls (57 a day), hit rate 0.940, chance 0.291, naive rule 0.481, lift 3.23x
  - next: threshold 0.5474, hit rate recent 0.5434 / long run 0.5737
    - 6h: 23 calls (93 a day), hit rate 0.478, chance 0.315, lift 1.52x
    - 24h: 84 calls (84 a day), hit rate 0.560, chance 0.304, lift 1.84x
    - 7d: 572 calls (82 a day), hit rate 0.566, chance 0.293, lift 1.93x
    - 30d: 2352 calls (78 a day), hit rate 0.583, chance 0.291, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.516; 0.40: 486, 0.561; 0.45: 418, 0.629; 0.50: 366, 0.683; 0.55: 321, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 138, 0.873; 0.80: 96, 0.913; 0.85: 49, 0.949; 0.90: 2, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.459; 0.40: 412, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.551; 0.55: 91, 0.582; 0.60: 13, 0.599; 0.65: 1, 0.682
- **K=5**: model 1790208000, labels learned 97608, probability skill vs chance 0.2048, widened contest next: True
  - now: threshold 0.7131, hit rate recent 0.7911 / long run 0.8283
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.200, naive rule 0.393, lift 3.76x
    - 24h: 48 calls (48 a day), hit rate 0.792, chance 0.199, naive rule 0.425, lift 3.99x
    - 7d: 382 calls (55 a day), hit rate 0.819, chance 0.190, naive rule 0.393, lift 4.31x
    - 30d: 1576 calls (53 a day), hit rate 0.835, chance 0.187, naive rule 0.391, lift 4.47x
  - next: threshold 0.4475, hit rate recent 0.4733 / long run 0.4658
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.200, lift 2.25x
    - 24h: 75 calls (75 a day), hit rate 0.493, chance 0.199, lift 2.48x
    - 7d: 602 calls (86 a day), hit rate 0.444, chance 0.190, lift 2.34x
    - 30d: 2114 calls (70 a day), hit rate 0.487, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 429, 0.414; 0.35: 365, 0.469; 0.40: 295, 0.539; 0.45: 241, 0.599; 0.50: 186, 0.658; 0.55: 141, 0.704; 0.60: 109, 0.747; 0.65: 84, 0.792; 0.70: 62, 0.825; 0.75: 34, 0.865; 0.80: 9, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 252, 0.425; 0.40: 165, 0.451; 0.45: 84, 0.474; 0.50: 20, 0.513; 0.55: 2, 0.548
- **K=8**: model 1791417600, labels learned 97605, probability skill vs chance 0.1991, widened contest next: True
  - now: threshold 0.5787, hit rate recent 0.6332 / long run 0.7065
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.117, naive rule 0.295, lift 5.34x
    - 24h: 46 calls (46 a day), hit rate 0.609, chance 0.124, naive rule 0.358, lift 4.89x
    - 7d: 404 calls (58 a day), hit rate 0.700, chance 0.122, naive rule 0.328, lift 5.75x
    - 30d: 1583 calls (53 a day), hit rate 0.721, chance 0.121, naive rule 0.326, lift 5.94x
  - next: threshold 0.366, hit rate recent 0.383 / long run 0.3912
    - 6h: 16 calls (66 a day), hit rate 0.250, chance 0.117, lift 2.13x
    - 24h: 80 calls (81 a day), hit rate 0.400, chance 0.124, lift 3.21x
    - 7d: 621 calls (89 a day), hit rate 0.386, chance 0.122, lift 3.17x
    - 30d: 2123 calls (71 a day), hit rate 0.404, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 270, 0.404; 0.35: 203, 0.480; 0.40: 156, 0.541; 0.45: 123, 0.587; 0.50: 94, 0.631; 0.55: 67, 0.687; 0.60: 46, 0.728; 0.65: 24, 0.772; 0.70: 9, 0.822; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 184, 0.350; 0.35: 114, 0.388; 0.40: 48, 0.414; 0.45: 10, 0.437; 0.50: 1, 0.429
- **K=13**: model 1791504000, labels learned 97600, probability skill vs chance 0.1822, widened contest next: False
  - now: threshold 0.4281, hit rate recent 0.6373 / long run 0.5894
    - 6h: 11 calls (46 a day), hit rate 0.727, chance 0.071, naive rule 0.212, lift 10.24x
    - 24h: 46 calls (46 a day), hit rate 0.674, chance 0.074, naive rule 0.268, lift 9.15x
    - 7d: 383 calls (55 a day), hit rate 0.598, chance 0.078, naive rule 0.271, lift 7.71x
    - 30d: 1484 calls (49 a day), hit rate 0.589, chance 0.077, naive rule 0.267, lift 7.66x
  - next: threshold 0.2791, hit rate recent 0.3238 / long run 0.3092
    - 6h: 18 calls (75 a day), hit rate 0.278, chance 0.071, lift 3.91x
    - 24h: 72 calls (73 a day), hit rate 0.319, chance 0.074, lift 4.34x
    - 7d: 541 calls (77 a day), hit rate 0.320, chance 0.078, lift 4.12x
    - 30d: 2042 calls (68 a day), hit rate 0.310, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.441; 0.35: 87, 0.502; 0.40: 62, 0.554; 0.45: 43, 0.612; 0.50: 27, 0.634; 0.55: 15, 0.686; 0.60: 5, 0.710; 0.65: 1, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.322; 0.35: 15, 0.349; 0.40: 3, 0.348; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.672 | 7.59% | 0.867 | 0.633 | 0.252 | 0.431 | 0.208 |
| 6h | 9.201 | 4.86% | 0.894 | 0.533 | 0.251 | 0.504 | 0.463 |
| 24h | 12.483 | 4.25% | 0.901 | 0.508 | 0.251 | 0.505 | 0.533 |
| 7d | 10.903 | 5.39% | 0.899 | 0.500 | 0.251 | 0.497 | 0.677 |
| 30d | 14.215 | 4.42% | 0.900 | 0.500 | 0.251 | 0.497 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.302 | 7.957 | 7.931 | 7.674 | 8.053 | 7.856 | 7.635 | 7.664 | 7.697 | 7.672 |
| 6h | 9.671 | 9.294 | 9.294 | 9.245 | 9.484 | 9.351 | 9.212 | 9.163 | 9.197 | 9.201 |
| 24h | 13.037 | 12.620 | 12.585 | 12.538 | 12.761 | 12.638 | 12.487 | 12.419 | 12.465 | 12.483 |
| 7d | 11.524 | 11.005 | 10.991 | 10.955 | 11.105 | 11.154 | 10.900 | 10.886 | 10.886 | 10.903 |
| 30d | 14.873 | 14.346 | 14.297 | 14.246 | 14.485 | 14.443 | 14.218 | 14.189 | 14.188 | 14.215 |

## Next candle

- candle starting 2026-10-09 22:56 UTC, last close 2487.86
- P(up) 0.5055, return quantiles (bp): {'05': -3.986, '10': -2.764, '25': -1.248, '40': -0.365, '50': 0.019, '60': 0.44, '75': 1.301, '90': 3.179, '95': 4.09}
- changepoint probability 0.02, regime age 102.5 min
- agent weights: empirical 0.004, ewma 0.073, garch 0.098, har 0.160, bocpd 0.020, hmm 0.044, online_qr 0.247, lgbm 0.355

## Learning log

- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- HMM volatility states (sd, bp per minute): [2.34, 4.79, 15.13], current probabilities: [0.957, 0.042, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-09 23:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.545, 'l_abs': 0.753, 'l_hi': 0.754, 'l_lo': 0.717, 'b05': 0.696, 'b25': 0.663, 'b75': 0.661, 'b95': 0.673}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.305, 2.163, 1.746, 2.119, 2.279, 2.517, 2.75, 2.808, 3.344, 3.445, 3.828, 4.24, 4.408, 4.665]}
- calibration offsets (in sigma): {'05': 0.0575, '10': 0.095, '25': 0.0875, '40': 0.07, '50': 0.015, '60': -0.03, '75': -0.0675, '90': 0.015, '95': -0.0275}
