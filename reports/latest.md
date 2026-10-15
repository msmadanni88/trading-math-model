# ETH-USD 60s candle generator - report

- generated: 2026-10-15 17:27 UTC
- last closed candle: 2026-10-15 17:27 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.505 (671) [0.479, 0.535] | 0.513 (2875) [0.493, 0.531] | 0.510 (4122) [0.494, 0.525] | 0.506 (1150) [0.475, 0.538] | 0.493 (69) | 0.500 | flat -0.004 (noise 0.035) |
| colour_clear | 0.559 (843) | 0.541 (5560) [0.534, 0.549] | 0.515 (23376) [0.507, 0.523] | 0.509 (33481) [0.503, 0.515] | 0.543 (9243) [0.536, 0.549] | 0.546 (584) | 0.500 | flat +0.015 (noise 0.013) |
| colour_confident | 0.537 (67) | 0.599 (882) [0.574, 0.634] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.612 (49) | 0.500 | flat -0.010 (noise 0.033) |
| colour_next | 0.542 (1436) | 0.526 (9976) [0.520, 0.532] | 0.511 (42873) [0.506, 0.517] | 0.508 (61433) [0.504, 0.512] | 0.528 (17084) [0.522, 0.534] | 0.520 (1044) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.501 (139664) [0.500, 0.502] | 0.501 (600222) [0.500, 0.502] | 0.501 (860062) [0.499, 0.502] | 0.500 (239176) [0.498, 0.502] | 0.514 (14616) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.462 (13) | 0.657 (233) [0.603, 0.720] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 1.000 (8) | 0.500 | flat +0.009 (noise 0.051) |
| reversal_k13_next | 0.244 (45) | 0.316 (471) [0.290, 0.342] | 0.314 (2053) [0.299, 0.330] | 0.305 (2977) [0.293, 0.319] | 0.319 (872) [0.303, 0.334] | 0.297 (37) | 0.077 | flat +0.005 (noise 0.029) |
| reversal_k13_now | 0.548 (42) | 0.593 (346) [0.566, 0.621] | 0.587 (1480) [0.567, 0.609] | 0.583 (2108) [0.567, 0.601] | 0.588 (636) [0.559, 0.621] | 0.540 (37) | 0.077 | flat +0.004 (noise 0.036) |
| reversal_k3_next | 0.591 (66) | 0.574 (676) [0.552, 0.598] | 0.583 (2477) [0.569, 0.599] | 0.584 (3532) [0.572, 0.597] | 0.576 (1092) [0.557, 0.599] | 0.517 (60) | 0.293 | flat -0.011 (noise 0.028) |
| reversal_k3_now | 0.980 (49) | 0.929 (423) [0.915, 0.947] | 0.939 (1723) [0.931, 0.947] | 0.938 (2459) [0.931, 0.945] | 0.930 (696) [0.919, 0.941] | 0.879 (33) | 0.293 | flat -0.001 (noise 0.018) |
| reversal_k5_next | 0.543 (94) | 0.489 (564) [0.469, 0.510] | 0.489 (2146) [0.472, 0.507] | 0.485 (3005) [0.471, 0.501] | 0.469 (1015) [0.445, 0.495] | 0.407 (86) | 0.187 | flat +0.027 (noise 0.028) |
| reversal_k5_now | 0.849 (33) | 0.811 (354) [0.785, 0.839] | 0.831 (1577) [0.815, 0.846] | 0.833 (2241) [0.820, 0.846] | 0.822 (630) [0.799, 0.844] | 0.692 (39) | 0.188 | flat -0.030 (noise 0.028) |
| reversal_k8_next | 0.386 (57) | 0.398 (571) [0.379, 0.418] | 0.410 (2107) [0.394, 0.429] | 0.396 (3097) [0.382, 0.410] | 0.395 (991) [0.376, 0.414] | 0.368 (68) | 0.122 | flat +0.000 (noise 0.030) |
| reversal_k8_now | 0.725 (40) | 0.674 (374) [0.640, 0.712] | 0.714 (1578) [0.693, 0.735] | 0.709 (2257) [0.693, 0.726] | 0.699 (670) [0.668, 0.730] | 0.667 (30) | 0.122 | flat -0.052 (noise 0.033) |
| overall | 0.507 (22062) | 0.504 (154090) [0.503, 0.506] | 0.504 (661111) [0.502, 0.505] | 0.503 (947293) [0.502, 0.504] | 0.504 (264012) [0.501, 0.506] | 0.514 (16119) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07477, 0.1162] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5262, 'levels': [{'threshold': 0.07477, 'calls_per_day': 142.0, 'win_rate': 0.5966}, {'threshold': 0.1162, 'calls_per_day': 35.5, 'win_rate': 0.6813}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 16991, 'rate': 0.529}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15229 | 0.337 | 0.519 (14995) | 0.601 (1234) | 0.777 (2460) |
| volatility: normal | 15229 | 0.362 | 0.512 (15164) | 0.594 (286) | 0.783 (2114) |
| volatility: wild | 15229 | 0.375 | 0.502 (15189) | 0.650 (137) | 0.763 (2110) |
| session: Asia 00-08 | 15360 | 0.356 | 0.516 (15262) | 0.604 (598) | 0.772 (2201) |
| session: Europe 08-13 | 9600 | 0.352 | 0.510 (9519) | 0.589 (423) | 0.785 (1472) |
| session: US 13-21 | 15147 | 0.367 | 0.506 (15051) | 0.581 (406) | 0.778 (2197) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5516) | 0.670 (230) | 0.753 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.401 | 0.389 | 0.232 | 0.232 | 0.593 | 0.320 | 0.482 | 1.019 |
| 6h | 360 | 0.381 | 0.377 | 0.294 | 0.336 | 0.500 | 0.268 | 0.495 | 1.190 |
| 24h | 1440 | 0.376 | 0.371 | 0.294 | 0.332 | 0.518 | 0.266 | 0.486 | 1.103 |
| 7d | 10080 | 0.357 | 0.349 | 0.272 | 0.303 | 0.525 | 0.259 | 0.456 | 1.237 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.512 | 0.250 | 0.466 | 1.296 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.401 / 0.593 / 0.933; 2: 0.357 / 0.407 / 0.950; 3: 0.411 / 0.559 / 0.933; 4: 0.394 / 0.576 / 0.933; 5: 0.410 / 0.610 / 0.933; 6: 0.387 / 0.576 / 0.900; 7: 0.366 / 0.458 / 0.883; 8: 0.351 / 0.542 / 0.883; 9: 0.362 / 0.492 / 0.883; 10: 0.386 / 0.559 / 0.883; 11: 0.342 / 0.390 / 0.817; 12: 0.350 / 0.475 / 0.783; 13: 0.368 / 0.475 / 0.800; 14: 0.353 / 0.458 / 0.800; 15: 0.358 / 0.407 / 0.783
- 6h: 1: 0.381 / 0.500 / 0.903; 2: 0.389 / 0.506 / 0.933; 3: 0.384 / 0.497 / 0.928; 4: 0.377 / 0.469 / 0.942; 5: 0.397 / 0.573 / 0.936; 6: 0.381 / 0.511 / 0.906; 7: 0.382 / 0.514 / 0.906; 8: 0.374 / 0.506 / 0.900; 9: 0.370 / 0.500 / 0.883; 10: 0.380 / 0.503 / 0.889; 11: 0.367 / 0.492 / 0.864; 12: 0.386 / 0.545 / 0.850; 13: 0.373 / 0.508 / 0.842; 14: 0.377 / 0.534 / 0.825; 15: 0.376 / 0.503 / 0.811
- 24h: 1: 0.376 / 0.518 / 0.906; 2: 0.368 / 0.503 / 0.895; 3: 0.372 / 0.512 / 0.898; 4: 0.369 / 0.507 / 0.898; 5: 0.371 / 0.527 / 0.901; 6: 0.367 / 0.505 / 0.897; 7: 0.367 / 0.518 / 0.894; 8: 0.356 / 0.484 / 0.894; 9: 0.365 / 0.505 / 0.895; 10: 0.366 / 0.516 / 0.895; 11: 0.360 / 0.500 / 0.890; 12: 0.362 / 0.508 / 0.887; 13: 0.365 / 0.517 / 0.887; 14: 0.361 / 0.503 / 0.885; 15: 0.366 / 0.521 / 0.883
- 7d: 1: 0.357 / 0.525 / 0.903; 2: 0.347 / 0.498 / 0.899; 3: 0.350 / 0.512 / 0.900; 4: 0.346 / 0.498 / 0.900; 5: 0.349 / 0.511 / 0.900; 6: 0.347 / 0.503 / 0.900; 7: 0.346 / 0.502 / 0.901; 8: 0.345 / 0.501 / 0.900; 9: 0.344 / 0.497 / 0.900; 10: 0.347 / 0.510 / 0.900; 11: 0.343 / 0.494 / 0.900; 12: 0.344 / 0.503 / 0.899; 13: 0.345 / 0.503 / 0.899; 14: 0.343 / 0.502 / 0.899; 15: 0.346 / 0.506 / 0.899
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.899; 14: 0.346 / 0.498 / 0.899; 15: 0.346 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.166 (body 0.118, range 0.214); 'price stays where it was' would score 0.156; colour right 0.576; typical miss of the close 8.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.131 (body 0.090, range 0.171); 'price stays where it was' would score 0.162; colour right 0.494; typical miss of the close 18.1 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.131 (body 0.088, range 0.174); 'price stays where it was' would score 0.143; colour right 0.489; typical miss of the close 13.8 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.122 (body 0.084, range 0.161); 'price stays where it was' would score 0.128; colour right 0.496; typical miss of the close 7.6 bp; chain ended on the right side 0.507 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.516 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.197 / 4.5; 3: 0.165 / 6.1; 4: 0.132 / 6.8; 5: 0.121 / 7.5; 6: 0.109 / 8.0; 7: 0.103 / 8.4; 8: 0.096 / 8.8; 9: 0.086 / 8.8; 10: 0.084 / 9.6; 11: 0.078 / 10.3; 12: 0.075 / 10.8; 13: 0.063 / 11.0; 14: 0.065 / 11.3; 15: 0.058 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 105921, probability skill vs chance 0.2265, widened contest next: True
  - now: threshold 0.8413, hit rate recent 0.9231 / long run 0.9319
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.287, naive rule 0.484, lift 2.98x
    - 24h: 47 calls (47 a day), hit rate 0.915, chance 0.284, naive rule 0.473, lift 3.23x
    - 7d: 405 calls (58 a day), hit rate 0.923, chance 0.298, naive rule 0.502, lift 3.10x
    - 30d: 1716 calls (57 a day), hit rate 0.938, chance 0.290, naive rule 0.481, lift 3.23x
  - next: threshold 0.5416, hit rate recent 0.5272 / long run 0.5713
    - 6h: 21 calls (85 a day), hit rate 0.429, chance 0.287, lift 1.49x
    - 24h: 69 calls (69 a day), hit rate 0.522, chance 0.284, lift 1.84x
    - 7d: 691 calls (99 a day), hit rate 0.570, chance 0.298, lift 1.91x
    - 30d: 2478 calls (83 a day), hit rate 0.582, chance 0.290, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.490; 0.35: 539, 0.513; 0.40: 484, 0.562; 0.45: 414, 0.631; 0.50: 361, 0.686; 0.55: 317, 0.728; 0.60: 270, 0.773; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 138, 0.871; 0.80: 95, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.459; 0.40: 410, 0.489; 0.45: 314, 0.524; 0.50: 204, 0.559; 0.55: 91, 0.580; 0.60: 14, 0.596; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 105919, probability skill vs chance 0.213, widened contest next: True
  - now: threshold 0.6971, hit rate recent 0.7585 / long run 0.8188
    - 6h: 17 calls (69 a day), hit rate 0.647, chance 0.163, naive rule 0.362, lift 3.97x
    - 24h: 50 calls (50 a day), hit rate 0.760, chance 0.188, naive rule 0.408, lift 4.05x
    - 7d: 347 calls (50 a day), hit rate 0.804, chance 0.190, naive rule 0.412, lift 4.24x
    - 30d: 1581 calls (53 a day), hit rate 0.827, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.4238, hit rate recent 0.4272 / long run 0.4748
    - 6h: 29 calls (118 a day), hit rate 0.310, chance 0.163, lift 1.91x
    - 24h: 103 calls (104 a day), hit rate 0.447, chance 0.188, lift 2.38x
    - 7d: 603 calls (86 a day), hit rate 0.484, chance 0.190, lift 2.55x
    - 30d: 2189 calls (73 a day), hit rate 0.484, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 355, 0.482; 0.40: 285, 0.554; 0.45: 233, 0.611; 0.50: 182, 0.665; 0.55: 138, 0.710; 0.60: 109, 0.750; 0.65: 82, 0.791; 0.70: 60, 0.820; 0.75: 33, 0.863; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 251, 0.425; 0.40: 162, 0.455; 0.45: 78, 0.473; 0.50: 18, 0.506; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 105916, probability skill vs chance 0.2036, widened contest next: True
  - now: threshold 0.5827, hit rate recent 0.6832 / long run 0.7005
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.104, naive rule 0.287, lift 5.23x
    - 24h: 41 calls (41 a day), hit rate 0.732, chance 0.114, naive rule 0.328, lift 6.40x
    - 7d: 358 calls (51 a day), hit rate 0.682, chance 0.124, naive rule 0.348, lift 5.51x
    - 30d: 1571 calls (52 a day), hit rate 0.714, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.3477, hit rate recent 0.364 / long run 0.3944
    - 6h: 26 calls (107 a day), hit rate 0.346, chance 0.104, lift 3.32x
    - 24h: 77 calls (78 a day), hit rate 0.377, chance 0.114, lift 3.29x
    - 7d: 550 calls (79 a day), hit rate 0.395, chance 0.124, lift 3.19x
    - 30d: 2131 calls (71 a day), hit rate 0.408, chance 0.122, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 261, 0.417; 0.35: 197, 0.492; 0.40: 151, 0.552; 0.45: 119, 0.595; 0.50: 91, 0.636; 0.55: 65, 0.685; 0.60: 44, 0.725; 0.65: 24, 0.774; 0.70: 9, 0.826; 0.75: 1, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.352; 0.35: 108, 0.389; 0.40: 44, 0.423; 0.45: 9, 0.464; 0.50: 1, 0.364
- **K=13**: model 1792022400, labels learned 105911, probability skill vs chance 0.1788, widened contest next: True
  - now: threshold 0.4185, hit rate recent 0.5588 / long run 0.5815
    - 6h: 12 calls (50 a day), hit rate 0.500, chance 0.078, naive rule 0.271, lift 6.39x
    - 24h: 48 calls (49 a day), hit rate 0.583, chance 0.082, naive rule 0.297, lift 7.10x
    - 7d: 347 calls (50 a day), hit rate 0.588, chance 0.080, naive rule 0.291, lift 7.36x
    - 30d: 1478 calls (49 a day), hit rate 0.589, chance 0.078, naive rule 0.274, lift 7.54x
  - next: threshold 0.3006, hit rate recent 0.2759 / long run 0.3074
    - 6h: 15 calls (63 a day), hit rate 0.267, chance 0.078, lift 3.41x
    - 24h: 41 calls (41 a day), hit rate 0.317, chance 0.082, lift 3.86x
    - 7d: 455 calls (65 a day), hit rate 0.316, chance 0.080, lift 3.96x
    - 30d: 2033 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.455; 0.35: 84, 0.516; 0.40: 60, 0.566; 0.45: 41, 0.618; 0.50: 25, 0.651; 0.55: 14, 0.704; 0.60: 4, 0.748; 0.65: 0, 0.938
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.327; 0.35: 13, 0.369; 0.40: 2, 0.409; 0.45: 0, 0.200

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 22.168 | 0.44% | 0.917 | 0.467 | 0.247 | 0.610 | 0.343 |
| 6h | 30.751 | 4.87% | 0.908 | 0.478 | 0.251 | 0.503 | 0.521 |
| 24h | 24.154 | 3.66% | 0.903 | 0.497 | 0.250 | 0.512 | 0.587 |
| 7d | 14.265 | 3.97% | 0.902 | 0.499 | 0.251 | 0.492 | 0.671 |
| 30d | 14.284 | 4.06% | 0.900 | 0.500 | 0.251 | 0.495 | 0.685 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 22.267 | 22.313 | 22.411 | 22.262 | 22.779 | 22.553 | 22.322 | 22.179 | 22.271 | 22.168 |
| 6h | 32.325 | 31.035 | 30.828 | 30.721 | 31.127 | 31.389 | 30.885 | 30.900 | 30.748 | 30.751 |
| 24h | 25.071 | 24.535 | 24.157 | 24.133 | 24.391 | 24.638 | 24.202 | 24.157 | 24.092 | 24.154 |
| 7d | 14.854 | 14.409 | 14.348 | 14.286 | 14.516 | 14.464 | 14.267 | 14.226 | 14.233 | 14.265 |
| 30d | 14.889 | 14.415 | 14.367 | 14.308 | 14.545 | 14.484 | 14.285 | 14.257 | 14.256 | 14.284 |

## Next candle

- candle starting 2026-10-15 17:27 UTC, last close 2443.24
- P(up) 0.5258, return quantiles (bp): {'05': -15.546, '10': -11.921, '25': -6.708, '40': -2.08, '50': 0.709, '60': 3.255, '75': 7.198, '90': 12.734, '95': 16.891}
- changepoint probability 0.2604, regime age 22.9 min
- agent weights: empirical 0.003, ewma 0.052, garch 0.208, har 0.293, bocpd 0.061, hmm 0.016, online_qr 0.171, lgbm 0.196

## Learning log

- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- HMM volatility states (sd, bp per minute): [2.37, 5.56, 18.85], current probabilities: [0.001, 0.648, 0.352]
- live generator: {'versions': 60, 'latest_effective': '2026-10-15 17:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.309, 'l_abs': 0.736, 'l_hi': 0.716, 'l_lo': 0.73, 'b05': 0.762, 'b25': 0.724, 'b75': 0.688, 'b95': 0.777}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.44, 1.698, 1.964, 2.157, 2.565, 2.832, 3.221, 3.492, 3.544, 4.116, 4.667, 5.272, 5.939, 6.284]}
- calibration offsets (in sigma): {'05': 0.113, '10': 0.066, '25': -0.005, '40': 0.044, '50': 0.08, '60': 0.106, '75': 0.085, '90': -0.016, '95': -0.053}
