# ETH-USD 60s candle generator - report

- generated: 2026-10-15 23:14 UTC
- last closed candle: 2026-10-15 23:14 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.505 (671) [0.479, 0.535] | 0.513 (2875) [0.493, 0.531] | 0.510 (4122) [0.494, 0.525] | 0.506 (1150) [0.475, 0.538] | 0.478 (92) | 0.500 | flat -0.004 (noise 0.035) |
| colour_clear | 0.559 (843) | 0.541 (5560) [0.534, 0.549] | 0.515 (23376) [0.507, 0.523] | 0.509 (33481) [0.503, 0.515] | 0.543 (9243) [0.536, 0.549] | 0.548 (765) | 0.500 | flat +0.015 (noise 0.013) |
| colour_confident | 0.537 (67) | 0.599 (882) [0.574, 0.634] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.592 (76) | 0.500 | flat -0.010 (noise 0.033) |
| colour_next | 0.542 (1436) | 0.526 (9976) [0.520, 0.532] | 0.511 (42873) [0.506, 0.517] | 0.508 (61433) [0.504, 0.512] | 0.528 (17084) [0.522, 0.534] | 0.519 (1390) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.501 (139664) [0.500, 0.502] | 0.501 (600222) [0.500, 0.502] | 0.501 (860062) [0.499, 0.502] | 0.500 (239176) [0.498, 0.502] | 0.511 (19460) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.462 (13) | 0.657 (233) [0.603, 0.720] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.833 (12) | 0.500 | flat +0.009 (noise 0.051) |
| reversal_k13_next | 0.244 (45) | 0.316 (471) [0.290, 0.342] | 0.314 (2053) [0.299, 0.330] | 0.305 (2977) [0.293, 0.319] | 0.319 (872) [0.303, 0.334] | 0.341 (44) | 0.077 | flat +0.005 (noise 0.029) |
| reversal_k13_now | 0.548 (42) | 0.593 (346) [0.566, 0.621] | 0.587 (1480) [0.567, 0.609] | 0.583 (2108) [0.567, 0.601] | 0.588 (636) [0.559, 0.621] | 0.521 (48) | 0.077 | flat +0.004 (noise 0.036) |
| reversal_k3_next | 0.591 (66) | 0.574 (676) [0.552, 0.598] | 0.583 (2477) [0.569, 0.599] | 0.584 (3532) [0.572, 0.597] | 0.576 (1092) [0.557, 0.599] | 0.559 (84) | 0.293 | flat -0.011 (noise 0.028) |
| reversal_k3_now | 0.980 (49) | 0.929 (423) [0.915, 0.947] | 0.939 (1723) [0.931, 0.947] | 0.938 (2459) [0.931, 0.945] | 0.930 (696) [0.919, 0.941] | 0.915 (47) | 0.293 | flat -0.001 (noise 0.018) |
| reversal_k5_next | 0.543 (94) | 0.489 (564) [0.469, 0.510] | 0.489 (2146) [0.472, 0.507] | 0.485 (3005) [0.471, 0.501] | 0.469 (1015) [0.445, 0.495] | 0.429 (105) | 0.187 | flat +0.027 (noise 0.028) |
| reversal_k5_now | 0.849 (33) | 0.811 (354) [0.785, 0.839] | 0.831 (1577) [0.815, 0.846] | 0.833 (2241) [0.820, 0.846] | 0.822 (630) [0.799, 0.844] | 0.755 (53) | 0.188 | flat -0.030 (noise 0.028) |
| reversal_k8_next | 0.386 (57) | 0.398 (571) [0.379, 0.418] | 0.410 (2107) [0.394, 0.429] | 0.396 (3097) [0.382, 0.410] | 0.395 (991) [0.376, 0.414] | 0.379 (87) | 0.122 | flat +0.000 (noise 0.030) |
| reversal_k8_now | 0.725 (40) | 0.674 (374) [0.640, 0.712] | 0.714 (1578) [0.693, 0.735] | 0.709 (2257) [0.693, 0.726] | 0.699 (670) [0.668, 0.730] | 0.667 (42) | 0.122 | flat -0.052 (noise 0.033) |
| overall | 0.507 (22062) | 0.504 (154090) [0.503, 0.506] | 0.504 (661111) [0.502, 0.505] | 0.503 (947293) [0.502, 0.504] | 0.504 (264012) [0.501, 0.506] | 0.512 (21452) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07457, 0.116] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.525, 'levels': [{'threshold': 0.07457, 'calls_per_day': 143.1, 'win_rate': 0.5949}, {'threshold': 0.116, 'calls_per_day': 35.8, 'win_rate': 0.6838}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 17337, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15345 | 0.337 | 0.518 (15111) | 0.600 (1236) | 0.776 (2470) |
| volatility: normal | 15344 | 0.362 | 0.513 (15278) | 0.593 (305) | 0.784 (2141) |
| volatility: wild | 15345 | 0.375 | 0.502 (15305) | 0.643 (143) | 0.763 (2124) |
| session: Asia 00-08 | 15360 | 0.356 | 0.516 (15262) | 0.604 (598) | 0.772 (2201) |
| session: Europe 08-13 | 9600 | 0.352 | 0.510 (9519) | 0.589 (423) | 0.785 (1472) |
| session: US 13-21 | 15360 | 0.367 | 0.506 (15263) | 0.583 (424) | 0.778 (2231) |
| session: late 21-24 | 5714 | 0.350 | 0.510 (5650) | 0.661 (239) | 0.753 (831) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.325 | 0.309 | 0.265 | 0.265 | 0.450 | 0.193 | 0.457 | 1.520 |
| 6h | 360 | 0.364 | 0.364 | 0.282 | 0.318 | 0.515 | 0.255 | 0.472 | 1.375 |
| 24h | 1440 | 0.374 | 0.368 | 0.289 | 0.324 | 0.519 | 0.265 | 0.483 | 1.171 |
| 7d | 10080 | 0.357 | 0.349 | 0.272 | 0.303 | 0.524 | 0.258 | 0.455 | 1.258 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.512 | 0.250 | 0.466 | 1.299 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.325 / 0.450 / 0.900; 2: 0.342 / 0.583 / 0.850; 3: 0.296 / 0.350 / 0.883; 4: 0.350 / 0.617 / 0.883; 5: 0.321 / 0.400 / 0.850; 6: 0.316 / 0.433 / 0.850; 7: 0.338 / 0.550 / 0.833; 8: 0.295 / 0.367 / 0.800; 9: 0.332 / 0.600 / 0.800; 10: 0.300 / 0.367 / 0.783; 11: 0.354 / 0.633 / 0.783; 12: 0.310 / 0.500 / 0.783; 13: 0.278 / 0.317 / 0.817; 14: 0.336 / 0.583 / 0.817; 15: 0.323 / 0.483 / 0.850
- 6h: 1: 0.364 / 0.515 / 0.897; 2: 0.345 / 0.468 / 0.883; 3: 0.358 / 0.518 / 0.886; 4: 0.347 / 0.479 / 0.881; 5: 0.343 / 0.460 / 0.869; 6: 0.355 / 0.490 / 0.872; 7: 0.348 / 0.496 / 0.883; 8: 0.344 / 0.474 / 0.900; 9: 0.359 / 0.526 / 0.897; 10: 0.353 / 0.499 / 0.886; 11: 0.359 / 0.529 / 0.889; 12: 0.357 / 0.529 / 0.900; 13: 0.334 / 0.471 / 0.906; 14: 0.361 / 0.571 / 0.922; 15: 0.346 / 0.490 / 0.928
- 24h: 1: 0.374 / 0.519 / 0.907; 2: 0.363 / 0.498 / 0.895; 3: 0.368 / 0.513 / 0.899; 4: 0.366 / 0.503 / 0.897; 5: 0.366 / 0.515 / 0.893; 6: 0.365 / 0.506 / 0.892; 7: 0.364 / 0.514 / 0.895; 8: 0.354 / 0.487 / 0.897; 9: 0.364 / 0.515 / 0.894; 10: 0.365 / 0.518 / 0.892; 11: 0.362 / 0.516 / 0.892; 12: 0.362 / 0.521 / 0.888; 13: 0.355 / 0.501 / 0.887; 14: 0.361 / 0.531 / 0.887; 15: 0.360 / 0.516 / 0.886
- 7d: 1: 0.357 / 0.524 / 0.902; 2: 0.346 / 0.498 / 0.899; 3: 0.349 / 0.511 / 0.900; 4: 0.345 / 0.498 / 0.899; 5: 0.348 / 0.509 / 0.899; 6: 0.346 / 0.504 / 0.899; 7: 0.344 / 0.501 / 0.899; 8: 0.344 / 0.500 / 0.900; 9: 0.344 / 0.498 / 0.899; 10: 0.346 / 0.508 / 0.899; 11: 0.342 / 0.496 / 0.899; 12: 0.344 / 0.505 / 0.898; 13: 0.343 / 0.502 / 0.898; 14: 0.342 / 0.504 / 0.898; 15: 0.345 / 0.505 / 0.899
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.090 (body 0.050, range 0.130); 'price stays where it was' would score 0.125; colour right 0.483; typical miss of the close 10.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.116 (body 0.077, range 0.155); 'price stays where it was' would score 0.138; colour right 0.496; typical miss of the close 10.7 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.133 (body 0.089, range 0.177); 'price stays where it was' would score 0.146; colour right 0.497; typical miss of the close 13.3 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.160); 'price stays where it was' would score 0.128; colour right 0.496; typical miss of the close 7.6 bp; chain ended on the right side 0.510 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.515 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.196 / 4.5; 3: 0.165 / 6.1; 4: 0.133 / 6.8; 5: 0.121 / 7.4; 6: 0.109 / 8.0; 7: 0.102 / 8.3; 8: 0.096 / 8.8; 9: 0.086 / 8.7; 10: 0.084 / 9.5; 11: 0.078 / 10.3; 12: 0.075 / 10.6; 13: 0.063 / 10.9; 14: 0.065 / 11.3; 15: 0.058 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 106268, probability skill vs chance 0.2258, widened contest next: False
  - now: threshold 0.841, hit rate recent 0.9392 / long run 0.9335
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.292, naive rule 0.470, lift 3.43x
    - 24h: 48 calls (48 a day), hit rate 0.917, chance 0.285, naive rule 0.465, lift 3.22x
    - 7d: 403 calls (58 a day), hit rate 0.928, chance 0.298, naive rule 0.503, lift 3.11x
    - 30d: 1718 calls (57 a day), hit rate 0.938, chance 0.290, naive rule 0.481, lift 3.23x
  - next: threshold 0.5397, hit rate recent 0.5721 / long run 0.5751
    - 6h: 24 calls (97 a day), hit rate 0.667, chance 0.292, lift 2.29x
    - 24h: 85 calls (85 a day), hit rate 0.553, chance 0.285, lift 1.94x
    - 7d: 690 calls (99 a day), hit rate 0.578, chance 0.298, lift 1.94x
    - 30d: 2496 calls (83 a day), hit rate 0.582, chance 0.290, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.562; 0.45: 414, 0.632; 0.50: 361, 0.686; 0.55: 317, 0.727; 0.60: 270, 0.772; 0.65: 224, 0.801; 0.70: 180, 0.834; 0.75: 139, 0.870; 0.80: 96, 0.910; 0.85: 49, 0.950; 0.90: 3, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.459; 0.40: 410, 0.489; 0.45: 314, 0.524; 0.50: 204, 0.559; 0.55: 92, 0.580; 0.60: 14, 0.598; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 106266, probability skill vs chance 0.2107, widened contest next: False
  - now: threshold 0.6962, hit rate recent 0.7938 / long run 0.8213
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.187, naive rule 0.381, lift 4.97x
    - 24h: 53 calls (53 a day), hit rate 0.755, chance 0.181, naive rule 0.383, lift 4.17x
    - 7d: 349 calls (50 a day), hit rate 0.811, chance 0.190, naive rule 0.412, lift 4.27x
    - 30d: 1581 calls (53 a day), hit rate 0.828, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.4234, hit rate recent 0.4566 / long run 0.4764
    - 6h: 19 calls (78 a day), hit rate 0.526, chance 0.187, lift 2.81x
    - 24h: 106 calls (107 a day), hit rate 0.425, chance 0.181, lift 2.34x
    - 7d: 600 calls (86 a day), hit rate 0.488, chance 0.190, lift 2.57x
    - 30d: 2199 calls (73 a day), hit rate 0.484, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 354, 0.482; 0.40: 284, 0.555; 0.45: 233, 0.611; 0.50: 182, 0.665; 0.55: 138, 0.710; 0.60: 109, 0.749; 0.65: 82, 0.790; 0.70: 60, 0.821; 0.75: 33, 0.865; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 251, 0.425; 0.40: 161, 0.454; 0.45: 78, 0.472; 0.50: 18, 0.505; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 106263, probability skill vs chance 0.1967, widened contest next: False
  - now: threshold 0.5655, hit rate recent 0.6792 / long run 0.6998
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.111, naive rule 0.288, lift 5.98x
    - 24h: 42 calls (42 a day), hit rate 0.667, chance 0.112, naive rule 0.305, lift 5.96x
    - 7d: 354 calls (51 a day), hit rate 0.681, chance 0.123, naive rule 0.348, lift 5.52x
    - 30d: 1570 calls (52 a day), hit rate 0.714, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.3443, hit rate recent 0.3832 / long run 0.3953
    - 6h: 19 calls (78 a day), hit rate 0.421, chance 0.111, lift 3.78x
    - 24h: 88 calls (89 a day), hit rate 0.375, chance 0.112, lift 3.35x
    - 7d: 539 calls (77 a day), hit rate 0.403, chance 0.123, lift 3.27x
    - 30d: 2125 calls (71 a day), hit rate 0.407, chance 0.122, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.418; 0.35: 196, 0.492; 0.40: 151, 0.552; 0.45: 119, 0.596; 0.50: 91, 0.636; 0.55: 65, 0.685; 0.60: 44, 0.726; 0.65: 24, 0.775; 0.70: 9, 0.829; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.352; 0.35: 107, 0.388; 0.40: 44, 0.422; 0.45: 9, 0.461; 0.50: 1, 0.364
- **K=13**: model 1792022400, labels learned 106258, probability skill vs chance 0.1723, widened contest next: True
  - now: threshold 0.427, hit rate recent 0.5407 / long run 0.5792
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.061, naive rule 0.208, lift 7.47x
    - 24h: 48 calls (49 a day), hit rate 0.521, chance 0.078, naive rule 0.268, lift 6.66x
    - 7d: 347 calls (50 a day), hit rate 0.579, chance 0.079, naive rule 0.288, lift 7.32x
    - 30d: 1477 calls (49 a day), hit rate 0.589, chance 0.078, naive rule 0.274, lift 7.55x
  - next: threshold 0.3005, hit rate recent 0.3093 / long run 0.3105
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.061, lift 9.39x
    - 24h: 44 calls (44 a day), hit rate 0.341, chance 0.078, lift 4.36x
    - 7d: 450 calls (64 a day), hit rate 0.318, chance 0.079, lift 4.01x
    - 30d: 2020 calls (67 a day), hit rate 0.315, chance 0.078, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.455; 0.35: 84, 0.516; 0.40: 60, 0.566; 0.45: 41, 0.620; 0.50: 25, 0.653; 0.55: 14, 0.705; 0.60: 4, 0.746; 0.65: 0, 1.000
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.328; 0.35: 13, 0.366; 0.40: 2, 0.406

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.505 | 10.10% | 0.900 | 0.583 | 0.255 | 0.383 | 0.261 |
| 6h | 14.161 | 5.94% | 0.900 | 0.539 | 0.250 | 0.521 | 0.374 |
| 24h | 23.166 | 4.52% | 0.909 | 0.507 | 0.250 | 0.512 | 0.613 |
| 7d | 14.175 | 4.13% | 0.901 | 0.500 | 0.251 | 0.493 | 0.669 |
| 30d | 14.152 | 3.97% | 0.900 | 0.500 | 0.251 | 0.495 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.798 | 11.360 | 11.507 | 11.262 | 11.455 | 11.519 | 11.324 | 11.378 | 11.341 | 11.505 |
| 6h | 15.057 | 14.284 | 14.283 | 14.186 | 14.342 | 14.250 | 14.108 | 14.143 | 14.144 | 14.161 |
| 24h | 24.262 | 23.571 | 23.177 | 23.148 | 23.381 | 23.618 | 23.197 | 23.182 | 23.111 | 23.166 |
| 7d | 14.785 | 14.327 | 14.264 | 14.194 | 14.432 | 14.376 | 14.183 | 14.142 | 14.148 | 14.175 |
| 30d | 14.737 | 14.277 | 14.235 | 14.176 | 14.409 | 14.344 | 14.150 | 14.123 | 14.124 | 14.152 |

## Next candle

- candle starting 2026-10-15 23:14 UTC, last close 2439.84
- P(up) 0.499, return quantiles (bp): {'05': -9.162, '10': -6.647, '25': -3.217, '40': -1.07, '50': -0.031, '60': 1.492, '75': 3.588, '90': 6.975, '95': 8.719}
- changepoint probability 0.0944, regime age 178.5 min
- agent weights: empirical 0.003, ewma 0.074, garch 0.145, har 0.243, bocpd 0.077, hmm 0.045, online_qr 0.213, lgbm 0.199

## Learning log

- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- HMM volatility states (sd, bp per minute): [2.37, 5.56, 18.85], current probabilities: [0.014, 0.941, 0.045]
- live generator: {'versions': 60, 'latest_effective': '2026-10-15 23:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.25, 'l_abs': 0.741, 'l_hi': 0.71, 'l_lo': 0.732, 'b05': 0.777, 'b25': 0.692, 'b75': 0.67, 'b95': 0.783}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.569, 1.778, 2.141, 2.546, 2.852, 2.849, 2.874, 3.179, 3.495, 3.747, 3.921, 4.172, 4.338, 4.411]}
- calibration offsets (in sigma): {'05': 0.0765, '10': 0.033, '25': 0.0325, '40': 0.012, '50': -0.045, '60': 0.008, '75': -0.0225, '90': -0.023, '95': -0.1065}
