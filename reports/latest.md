# ETH-USD 60s candle generator - report

- generated: 2026-10-09 05:59 UTC
- last closed candle: 2026-10-09 05:59 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.506 (670) [0.454, 0.558] | 0.505 (2875) [0.485, 0.526] | 0.509 (3547) [0.492, 0.526] | 0.499 (575) [0.443, 0.557] | 0.435 (23) | 0.500 | flat -0.002 (noise 0.040) |
| colour_clear | 0.555 (827) | 0.540 (5230) [0.526, 0.552] | 0.507 (23188) [0.500, 0.514] | 0.504 (28748) [0.498, 0.510] | 0.547 (4510) [0.536, 0.556] | 0.548 (206) | 0.500 | up +0.048 (noise 0.010) |
| colour_confident | 0.596 (89) | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.600 (35) | 0.500 | - |
| colour_next | 0.528 (1434) | 0.527 (9974) [0.517, 0.538] | 0.507 (42883) [0.501, 0.512] | 0.505 (52891) [0.501, 0.510] | 0.531 (8542) [0.521, 0.541] | 0.508 (358) | 0.500 | up +0.025 (noise 0.007) |
| colour_path | 0.497 (20076) | 0.498 (139636) [0.495, 0.502] | 0.501 (600362) [0.499, 0.502] | 0.500 (740474) [0.499, 0.502] | 0.499 (119588) [0.494, 0.503] | 0.510 (5012) | 0.500 | flat -0.005 (noise 0.003) |
| colour_strong | 0.500 (20) | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 1.000 (5) | 0.500 | - |
| reversal_k13_next | 0.318 (66) | 0.312 (525) [0.291, 0.331] | 0.308 (2040) [0.294, 0.324] | 0.304 (2572) [0.290, 0.318] | 0.321 (467) [0.306, 0.336] | 0.375 (16) | 0.077 | flat +0.030 (noise 0.027) |
| reversal_k13_now | 0.612 (49) | 0.591 (391) [0.553, 0.636] | 0.585 (1481) [0.563, 0.609] | 0.582 (1811) [0.564, 0.602] | 0.587 (339) [0.544, 0.641] | 0.667 (9) | 0.077 | flat +0.007 (noise 0.038) |
| reversal_k3_next | 0.521 (71) | 0.572 (547) [0.542, 0.609] | 0.588 (2352) [0.572, 0.603] | 0.585 (2927) [0.572, 0.599] | 0.571 (487) [0.538, 0.613] | 0.588 (17) | 0.292 | flat -0.006 (noise 0.029) |
| reversal_k3_now | 0.917 (72) | 0.927 (399) [0.918, 0.939] | 0.940 (1692) [0.932, 0.948] | 0.939 (2108) [0.932, 0.947] | 0.927 (345) [0.917, 0.941] | 1.000 (13) | 0.292 | flat -0.028 (noise 0.017) |
| reversal_k5_next | 0.422 (71) | 0.449 (642) [0.420, 0.481] | 0.488 (2100) [0.468, 0.506] | 0.483 (2512) [0.466, 0.501] | 0.441 (522) [0.412, 0.480] | 0.471 (17) | 0.187 | flat -0.034 (noise 0.032) |
| reversal_k5_now | 0.758 (62) | 0.826 (397) [0.795, 0.858] | 0.833 (1573) [0.817, 0.849] | 0.835 (1949) [0.821, 0.850] | 0.823 (338) [0.788, 0.858] | 0.889 (9) | 0.187 | flat -0.042 (noise 0.026) |
| reversal_k8_next | 0.367 (120) | 0.387 (587) [0.359, 0.418] | 0.402 (2096) [0.385, 0.421] | 0.394 (2646) [0.379, 0.411] | 0.385 (540) [0.355, 0.418] | 0.412 (17) | 0.121 | flat -0.005 (noise 0.032) |
| reversal_k8_now | 0.625 (64) | 0.715 (411) [0.677, 0.756] | 0.723 (1582) [0.703, 0.742] | 0.713 (1947) [0.695, 0.732] | 0.711 (360) [0.670, 0.756] | 0.571 (7) | 0.121 | flat -0.038 (noise 0.036) |
| overall | 0.500 (22181) | 0.502 (154179) [0.498, 0.507] | 0.503 (661036) [0.502, 0.505] | 0.503 (815384) [0.501, 0.504] | 0.502 (132103) [0.497, 0.508] | 0.511 (5498) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07651, 0.1151] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5339, 'levels': [{'threshold': 0.07651, 'calls_per_day': 143.8, 'win_rate': 0.6106}, {'threshold': 0.1151, 'calls_per_day': 36.2, 'win_rate': 0.6484}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 7768, 'rate': 0.533}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15000 | 0.335 | 0.515 (14789) | 0.606 (649) | 0.778 (2392) |
| volatility: normal | 14999 | 0.361 | 0.511 (14932) | 0.601 (148) | 0.771 (2108) |
| volatility: wild | 15000 | 0.374 | 0.496 (14954) | 0.641 (53) | 0.775 (2102) |
| session: Asia 00-08 | 15239 | 0.353 | 0.509 (15137) | 0.600 (315) | 0.778 (2177) |
| session: Europe 08-13 | 9300 | 0.351 | 0.505 (9240) | 0.577 (156) | 0.766 (1458) |
| session: US 13-21 | 14880 | 0.367 | 0.506 (14781) | 0.600 (220) | 0.782 (2176) |
| session: late 21-24 | 5580 | 0.350 | 0.511 (5517) | 0.660 (159) | 0.764 (791) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.379 | 0.373 | 0.294 | 0.294 | 0.533 | 0.286 | 0.471 | 1.098 |
| 6h | 360 | 0.355 | 0.351 | 0.279 | 0.307 | 0.507 | 0.256 | 0.455 | 1.171 |
| 24h | 1440 | 0.374 | 0.370 | 0.295 | 0.327 | 0.529 | 0.263 | 0.484 | 1.044 |
| 7d | 10080 | 0.351 | 0.345 | 0.273 | 0.297 | 0.527 | 0.252 | 0.450 | 1.240 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.507 | 0.248 | 0.465 | 1.286 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.379 / 0.533 / 0.867; 2: 0.369 / 0.500 / 0.833; 3: 0.354 / 0.517 / 0.817; 4: 0.385 / 0.600 / 0.733; 5: 0.360 / 0.550 / 0.717; 6: 0.367 / 0.483 / 0.717; 7: 0.348 / 0.467 / 0.767; 8: 0.355 / 0.500 / 0.800; 9: 0.407 / 0.683 / 0.750; 10: 0.344 / 0.367 / 0.700; 11: 0.390 / 0.550 / 0.600; 12: 0.348 / 0.383 / 0.567; 13: 0.382 / 0.500 / 0.583; 14: 0.364 / 0.533 / 0.633; 15: 0.361 / 0.450 / 0.633
- 6h: 1: 0.355 / 0.507 / 0.892; 2: 0.351 / 0.493 / 0.903; 3: 0.346 / 0.507 / 0.878; 4: 0.358 / 0.549 / 0.842; 5: 0.359 / 0.540 / 0.847; 6: 0.354 / 0.507 / 0.822; 7: 0.346 / 0.490 / 0.811; 8: 0.349 / 0.490 / 0.831; 9: 0.362 / 0.543 / 0.822; 10: 0.359 / 0.521 / 0.811; 11: 0.353 / 0.490 / 0.797; 12: 0.351 / 0.510 / 0.769; 13: 0.351 / 0.493 / 0.792; 14: 0.346 / 0.513 / 0.811; 15: 0.351 / 0.493 / 0.842
- 24h: 1: 0.374 / 0.529 / 0.899; 2: 0.360 / 0.485 / 0.904; 3: 0.367 / 0.509 / 0.894; 4: 0.368 / 0.511 / 0.895; 5: 0.368 / 0.515 / 0.903; 6: 0.361 / 0.490 / 0.891; 7: 0.364 / 0.513 / 0.887; 8: 0.361 / 0.497 / 0.897; 9: 0.359 / 0.490 / 0.892; 10: 0.363 / 0.508 / 0.890; 11: 0.357 / 0.479 / 0.890; 12: 0.362 / 0.504 / 0.888; 13: 0.362 / 0.494 / 0.889; 14: 0.360 / 0.505 / 0.890; 15: 0.361 / 0.494 / 0.894
- 7d: 1: 0.351 / 0.527 / 0.898; 2: 0.342 / 0.502 / 0.900; 3: 0.343 / 0.508 / 0.899; 4: 0.341 / 0.505 / 0.899; 5: 0.338 / 0.498 / 0.899; 6: 0.337 / 0.491 / 0.898; 7: 0.339 / 0.505 / 0.898; 8: 0.336 / 0.491 / 0.898; 9: 0.334 / 0.490 / 0.898; 10: 0.336 / 0.501 / 0.898; 11: 0.336 / 0.499 / 0.898; 12: 0.337 / 0.503 / 0.897; 13: 0.337 / 0.504 / 0.897; 14: 0.336 / 0.498 / 0.898; 15: 0.335 / 0.491 / 0.899
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.500 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.502 / 0.899; 13: 0.346 / 0.501 / 0.899; 14: 0.345 / 0.496 / 0.900; 15: 0.344 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.077 (body 0.058, range 0.096); 'price stays where it was' would score 0.070; colour right 0.550; typical miss of the close 12.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.112 (body 0.079, range 0.146); 'price stays where it was' would score 0.119; colour right 0.501; typical miss of the close 8.3 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.124 (body 0.082, range 0.166); 'price stays where it was' would score 0.123; colour right 0.492; typical miss of the close 10.5 bp; chain ended on the right side 0.438 of 96 chains; n=1440
- 7d: match 0.115 (body 0.078, range 0.153); 'price stays where it was' would score 0.120; colour right 0.499; typical miss of the close 6.2 bp; chain ended on the right side 0.497 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.1 bp; chain ended on the right side 0.504 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.1; 2: 0.200 / 4.5; 3: 0.167 / 6.1; 4: 0.131 / 6.8; 5: 0.118 / 7.5; 6: 0.110 / 8.2; 7: 0.099 / 8.6; 8: 0.091 / 8.9; 9: 0.085 / 9.2; 10: 0.080 / 10.1; 11: 0.075 / 10.6; 12: 0.075 / 10.9; 13: 0.062 / 11.3; 14: 0.065 / 11.4; 15: 0.060 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 96593, probability skill vs chance 0.2327, widened contest next: True
  - now: threshold 0.8394, hit rate recent 0.9305 / long run 0.9364
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.286, naive rule 0.502, lift 3.50x
    - 24h: 67 calls (67 a day), hit rate 0.910, chance 0.273, naive rule 0.465, lift 3.34x
    - 7d: 396 calls (57 a day), hit rate 0.927, chance 0.292, naive rule 0.486, lift 3.18x
    - 30d: 1691 calls (56 a day), hit rate 0.941, chance 0.291, naive rule 0.481, lift 3.24x
  - next: threshold 0.5577, hit rate recent 0.5391 / long run 0.5776
    - 6h: 17 calls (69 a day), hit rate 0.588, chance 0.286, lift 2.06x
    - 24h: 69 calls (69 a day), hit rate 0.507, chance 0.273, lift 1.86x
    - 7d: 555 calls (79 a day), hit rate 0.568, chance 0.292, lift 1.95x
    - 30d: 2349 calls (78 a day), hit rate 0.587, chance 0.291, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.516; 0.40: 486, 0.561; 0.45: 418, 0.628; 0.50: 366, 0.681; 0.55: 322, 0.724; 0.60: 274, 0.767; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 138, 0.872; 0.80: 96, 0.912; 0.85: 48, 0.949; 0.90: 2, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 497, 0.458; 0.40: 412, 0.488; 0.45: 316, 0.519; 0.50: 206, 0.552; 0.55: 92, 0.586; 0.60: 13, 0.602; 0.65: 1, 0.737
- **K=5**: model 1790208000, labels learned 96591, probability skill vs chance 0.2117, widened contest next: True
  - now: threshold 0.7144, hit rate recent 0.8007 / long run 0.8317
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.176, naive rule 0.419, lift 5.06x
    - 24h: 54 calls (54 a day), hit rate 0.778, chance 0.181, naive rule 0.388, lift 4.29x
    - 7d: 389 calls (56 a day), hit rate 0.828, chance 0.190, naive rule 0.396, lift 4.36x
    - 30d: 1571 calls (52 a day), hit rate 0.834, chance 0.186, naive rule 0.390, lift 4.48x
  - next: threshold 0.4454, hit rate recent 0.4404 / long run 0.464
    - 6h: 17 calls (69 a day), hit rate 0.471, chance 0.176, lift 2.68x
    - 24h: 70 calls (70 a day), hit rate 0.429, chance 0.181, lift 2.36x
    - 7d: 645 calls (92 a day), hit rate 0.448, chance 0.190, lift 2.36x
    - 30d: 2101 calls (70 a day), hit rate 0.487, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.412; 0.35: 366, 0.467; 0.40: 296, 0.537; 0.45: 242, 0.597; 0.50: 187, 0.655; 0.55: 142, 0.702; 0.60: 110, 0.744; 0.65: 84, 0.789; 0.70: 62, 0.821; 0.75: 34, 0.864; 0.80: 9, 0.881
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 253, 0.424; 0.40: 166, 0.449; 0.45: 84, 0.474; 0.50: 20, 0.511; 0.55: 2, 0.554
- **K=8**: model 1791417600, labels learned 96588, probability skill vs chance 0.2076, widened contest next: True
  - now: threshold 0.5772, hit rate recent 0.6397 / long run 0.7119
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.123, naive rule 0.390, lift 4.65x
    - 24h: 59 calls (59 a day), hit rate 0.610, chance 0.117, naive rule 0.327, lift 5.22x
    - 7d: 405 calls (58 a day), hit rate 0.711, chance 0.123, naive rule 0.332, lift 5.76x
    - 30d: 1578 calls (53 a day), hit rate 0.722, chance 0.121, naive rule 0.325, lift 5.96x
  - next: threshold 0.3542, hit rate recent 0.3604 / long run 0.3908
    - 6h: 17 calls (70 a day), hit rate 0.412, chance 0.123, lift 3.35x
    - 24h: 113 calls (114 a day), hit rate 0.354, chance 0.117, lift 3.03x
    - 7d: 589 calls (84 a day), hit rate 0.387, chance 0.123, lift 3.14x
    - 30d: 2101 calls (70 a day), hit rate 0.401, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 271, 0.402; 0.35: 204, 0.478; 0.40: 157, 0.539; 0.45: 124, 0.586; 0.50: 94, 0.630; 0.55: 67, 0.684; 0.60: 46, 0.730; 0.65: 24, 0.770; 0.70: 9, 0.816; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 185, 0.347; 0.35: 115, 0.385; 0.40: 48, 0.410; 0.45: 10, 0.425; 0.50: 1, 0.410
- **K=13**: model 1791504000, labels learned 96583, probability skill vs chance 0.1933, widened contest next: False
  - now: threshold 0.4253, hit rate recent 0.5893 / long run 0.5836
    - 6h: 9 calls (38 a day), hit rate 0.667, chance 0.078, naive rule 0.290, lift 8.52x
    - 24h: 49 calls (50 a day), hit rate 0.612, chance 0.079, naive rule 0.286, lift 7.76x
    - 7d: 387 calls (55 a day), hit rate 0.589, chance 0.078, naive rule 0.274, lift 7.55x
    - 30d: 1480 calls (49 a day), hit rate 0.586, chance 0.077, naive rule 0.267, lift 7.63x
  - next: threshold 0.2908, hit rate recent 0.3321 / long run 0.3091
    - 6h: 16 calls (67 a day), hit rate 0.375, chance 0.078, lift 4.79x
    - 24h: 67 calls (68 a day), hit rate 0.343, chance 0.079, lift 4.35x
    - 7d: 522 calls (75 a day), hit rate 0.314, chance 0.078, lift 4.03x
    - 30d: 2038 calls (68 a day), hit rate 0.308, chance 0.077, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.440; 0.35: 88, 0.500; 0.40: 62, 0.550; 0.45: 44, 0.608; 0.50: 27, 0.633; 0.55: 15, 0.684; 0.60: 6, 0.707; 0.65: 1, 0.780
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.317; 0.35: 16, 0.343; 0.40: 3, 0.347; 0.45: 1, 0.368

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.847 | 4.38% | 0.883 | 0.500 | 0.251 | 0.517 | 0.134 |
| 6h | 12.364 | 3.75% | 0.892 | 0.500 | 0.251 | 0.510 | 0.348 |
| 24h | 17.633 | 6.06% | 0.901 | 0.503 | 0.250 | 0.512 | 0.713 |
| 7d | 11.280 | 5.26% | 0.900 | 0.500 | 0.251 | 0.496 | 0.675 |
| 30d | 14.301 | 4.39% | 0.900 | 0.500 | 0.251 | 0.497 | 0.693 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.344 | 10.881 | 10.840 | 10.865 | 10.888 | 10.880 | 10.883 | 10.866 | 10.839 | 10.847 |
| 6h | 12.847 | 12.452 | 12.456 | 12.412 | 12.554 | 12.339 | 12.363 | 12.274 | 12.340 | 12.364 |
| 24h | 18.771 | 17.772 | 17.712 | 17.663 | 17.835 | 18.050 | 17.622 | 17.611 | 17.610 | 17.633 |
| 7d | 11.907 | 11.395 | 11.365 | 11.326 | 11.492 | 11.518 | 11.286 | 11.271 | 11.264 | 11.280 |
| 30d | 14.957 | 14.433 | 14.382 | 14.332 | 14.573 | 14.526 | 14.303 | 14.275 | 14.274 | 14.301 |

## Next candle

- candle starting 2026-10-09 05:59 UTC, last close 2489.8
- P(up) 0.5196, return quantiles (bp): {'05': -5.583, '10': -3.994, '25': -1.76, '40': -0.567, '50': 0.134, '60': 0.905, '75': 2.387, '90': 4.195, '95': 5.625}
- changepoint probability 0.0365, regime age 152.2 min
- agent weights: empirical 0.003, ewma 0.095, garch 0.124, har 0.156, bocpd 0.053, hmm 0.043, online_qr 0.227, lgbm 0.298

## Learning log

- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.22, 4.81, 14.65], current probabilities: [0.685, 0.313, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-09 06:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.539, 'l_abs': 0.702, 'l_hi': 0.729, 'l_lo': 0.707, 'b05': 0.697, 'b25': 0.696, 'b75': 0.669, 'b95': 0.689}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.463, 2.065, 2.749, 2.731, 3.589, 4.125, 3.919, 4.422, 4.861, 5.534, 6.53, 6.04, 5.46, 4.637]}
- calibration offsets (in sigma): {'05': 0.039, '10': 0.018, '25': 0.045, '40': 0.022, '50': 0.02, '60': 0.028, '75': 0.075, '90': -0.018, '95': -0.019}
