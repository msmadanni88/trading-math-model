# ETH-USD 60s candle generator - report

- generated: 2026-10-15 07:34 UTC
- last closed candle: 2026-10-15 07:34 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.505 (671) [0.479, 0.535] | 0.513 (2875) [0.493, 0.531] | 0.510 (4122) [0.494, 0.525] | 0.506 (1150) [0.475, 0.538] | 0.533 (30) | 0.500 | flat -0.004 (noise 0.035) |
| colour_clear | 0.559 (843) | 0.541 (5560) [0.534, 0.549] | 0.515 (23376) [0.507, 0.523] | 0.509 (33481) [0.503, 0.515] | 0.543 (9243) [0.536, 0.549] | 0.557 (226) | 0.500 | flat +0.015 (noise 0.013) |
| colour_confident | 0.537 (67) | 0.599 (882) [0.574, 0.634] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.565 (23) | 0.500 | flat -0.010 (noise 0.033) |
| colour_next | 0.542 (1436) | 0.526 (9976) [0.520, 0.532] | 0.511 (42873) [0.506, 0.517] | 0.508 (61433) [0.504, 0.512] | 0.528 (17084) [0.522, 0.534] | 0.517 (453) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.501 (139664) [0.500, 0.502] | 0.501 (600222) [0.500, 0.502] | 0.501 (860062) [0.499, 0.502] | 0.500 (239176) [0.498, 0.502] | 0.514 (6342) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.462 (13) | 0.657 (233) [0.603, 0.720] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 1.000 (4) | 0.500 | flat +0.009 (noise 0.051) |
| reversal_k13_next | 0.244 (45) | 0.316 (471) [0.290, 0.342] | 0.314 (2053) [0.299, 0.330] | 0.305 (2977) [0.293, 0.319] | 0.319 (872) [0.303, 0.334] | 0.357 (14) | 0.077 | flat +0.005 (noise 0.029) |
| reversal_k13_now | 0.548 (42) | 0.593 (346) [0.566, 0.621] | 0.587 (1480) [0.567, 0.609] | 0.583 (2108) [0.567, 0.601] | 0.588 (636) [0.559, 0.621] | 0.500 (14) | 0.077 | flat +0.004 (noise 0.036) |
| reversal_k3_next | 0.591 (66) | 0.574 (676) [0.552, 0.598] | 0.583 (2477) [0.569, 0.599] | 0.584 (3532) [0.572, 0.597] | 0.576 (1092) [0.557, 0.599] | 0.455 (22) | 0.293 | flat -0.011 (noise 0.028) |
| reversal_k3_now | 0.980 (49) | 0.929 (423) [0.915, 0.947] | 0.939 (1723) [0.931, 0.947] | 0.938 (2459) [0.931, 0.945] | 0.930 (696) [0.919, 0.941] | 0.857 (14) | 0.293 | flat -0.001 (noise 0.018) |
| reversal_k5_next | 0.543 (94) | 0.489 (564) [0.469, 0.510] | 0.489 (2146) [0.472, 0.507] | 0.485 (3005) [0.471, 0.501] | 0.469 (1015) [0.445, 0.495] | 0.361 (36) | 0.187 | flat +0.027 (noise 0.028) |
| reversal_k5_now | 0.849 (33) | 0.811 (354) [0.785, 0.839] | 0.831 (1577) [0.815, 0.846] | 0.833 (2241) [0.820, 0.846] | 0.822 (630) [0.799, 0.844] | 0.692 (13) | 0.188 | flat -0.030 (noise 0.028) |
| reversal_k8_next | 0.386 (57) | 0.398 (571) [0.379, 0.418] | 0.410 (2107) [0.394, 0.429] | 0.396 (3097) [0.382, 0.410] | 0.395 (991) [0.376, 0.414] | 0.345 (29) | 0.122 | flat +0.000 (noise 0.030) |
| reversal_k8_now | 0.725 (40) | 0.674 (374) [0.640, 0.712] | 0.714 (1578) [0.693, 0.735] | 0.709 (2257) [0.693, 0.726] | 0.699 (670) [0.668, 0.730] | 0.636 (11) | 0.122 | flat -0.052 (noise 0.033) |
| overall | 0.507 (22062) | 0.504 (154090) [0.503, 0.506] | 0.504 (661111) [0.502, 0.505] | 0.503 (947293) [0.502, 0.504] | 0.504 (264012) [0.501, 0.506] | 0.513 (6978) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07516, 0.1166] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5262, 'levels': [{'threshold': 0.07516, 'calls_per_day': 142.1, 'win_rate': 0.594}, {'threshold': 0.1166, 'calls_per_day': 35.6, 'win_rate': 0.6706}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 16400, 'rate': 0.5293}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15032 | 0.336 | 0.519 (14798) | 0.601 (1231) | 0.777 (2435) |
| volatility: normal | 15031 | 0.363 | 0.513 (14969) | 0.585 (282) | 0.782 (2105) |
| volatility: wild | 15031 | 0.374 | 0.500 (14990) | 0.661 (118) | 0.768 (2057) |
| session: Asia 00-08 | 15334 | 0.356 | 0.516 (15236) | 0.604 (598) | 0.773 (2198) |
| session: Europe 08-13 | 9300 | 0.351 | 0.509 (9220) | 0.582 (407) | 0.783 (1425) |
| session: US 13-21 | 14880 | 0.367 | 0.507 (14785) | 0.583 (396) | 0.781 (2160) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5516) | 0.670 (230) | 0.753 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.361 | 0.335 | 0.215 | 0.215 | 0.517 | 0.248 | 0.475 | 1.239 |
| 6h | 360 | 0.369 | 0.361 | 0.289 | 0.323 | 0.507 | 0.247 | 0.492 | 1.268 |
| 24h | 1440 | 0.374 | 0.365 | 0.292 | 0.335 | 0.525 | 0.264 | 0.484 | 1.229 |
| 7d | 10080 | 0.357 | 0.350 | 0.273 | 0.303 | 0.526 | 0.258 | 0.456 | 1.241 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.512 | 0.250 | 0.465 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.361 / 0.517 / 0.917; 2: 0.344 / 0.550 / 0.917; 3: 0.362 / 0.483 / 0.933; 4: 0.378 / 0.600 / 0.883; 5: 0.355 / 0.467 / 0.900; 6: 0.357 / 0.517 / 0.850; 7: 0.353 / 0.517 / 0.883; 8: 0.340 / 0.450 / 0.883; 9: 0.339 / 0.483 / 0.883; 10: 0.349 / 0.417 / 0.883; 11: 0.356 / 0.533 / 0.867; 12: 0.330 / 0.450 / 0.800; 13: 0.352 / 0.533 / 0.767; 14: 0.347 / 0.500 / 0.800; 15: 0.356 / 0.517 / 0.850
- 6h: 1: 0.369 / 0.507 / 0.933; 2: 0.356 / 0.526 / 0.947; 3: 0.364 / 0.518 / 0.953; 4: 0.365 / 0.552 / 0.928; 5: 0.357 / 0.515 / 0.919; 6: 0.349 / 0.504 / 0.908; 7: 0.347 / 0.487 / 0.892; 8: 0.338 / 0.507 / 0.919; 9: 0.357 / 0.510 / 0.897; 10: 0.362 / 0.565 / 0.908; 11: 0.348 / 0.526 / 0.889; 12: 0.346 / 0.529 / 0.861; 13: 0.341 / 0.487 / 0.839; 14: 0.338 / 0.490 / 0.839; 15: 0.344 / 0.521 / 0.844
- 24h: 1: 0.374 / 0.525 / 0.910; 2: 0.358 / 0.497 / 0.903; 3: 0.366 / 0.513 / 0.910; 4: 0.364 / 0.518 / 0.904; 5: 0.359 / 0.503 / 0.901; 6: 0.361 / 0.512 / 0.897; 7: 0.357 / 0.501 / 0.899; 8: 0.351 / 0.478 / 0.897; 9: 0.362 / 0.492 / 0.895; 10: 0.360 / 0.516 / 0.897; 11: 0.360 / 0.516 / 0.894; 12: 0.352 / 0.488 / 0.891; 13: 0.355 / 0.503 / 0.884; 14: 0.351 / 0.489 / 0.889; 15: 0.364 / 0.533 / 0.889
- 7d: 1: 0.357 / 0.526 / 0.902; 2: 0.345 / 0.497 / 0.902; 3: 0.349 / 0.511 / 0.902; 4: 0.346 / 0.500 / 0.902; 5: 0.348 / 0.507 / 0.902; 6: 0.346 / 0.502 / 0.902; 7: 0.345 / 0.502 / 0.901; 8: 0.344 / 0.501 / 0.902; 9: 0.344 / 0.495 / 0.902; 10: 0.346 / 0.508 / 0.902; 11: 0.342 / 0.492 / 0.902; 12: 0.344 / 0.502 / 0.902; 13: 0.344 / 0.500 / 0.901; 14: 0.342 / 0.500 / 0.900; 15: 0.345 / 0.504 / 0.899
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.502 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.140 (body 0.091, range 0.188); 'price stays where it was' would score 0.211; colour right 0.500; typical miss of the close 11.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.141 (body 0.094, range 0.189); 'price stays where it was' would score 0.148; colour right 0.485; typical miss of the close 16.0 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.125 (body 0.083, range 0.167); 'price stays where it was' would score 0.134; colour right 0.483; typical miss of the close 13.2 bp; chain ended on the right side 0.469 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.127; colour right 0.494; typical miss of the close 7.5 bp; chain ended on the right side 0.510 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.515 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.197 / 4.5; 3: 0.164 / 6.1; 4: 0.132 / 6.8; 5: 0.121 / 7.5; 6: 0.108 / 8.0; 7: 0.102 / 8.4; 8: 0.095 / 8.7; 9: 0.086 / 8.8; 10: 0.083 / 9.6; 11: 0.078 / 10.3; 12: 0.075 / 10.7; 13: 0.063 / 10.9; 14: 0.065 / 11.2; 15: 0.060 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 105328, probability skill vs chance 0.2292, widened contest next: True
  - now: threshold 0.842, hit rate recent 0.939 / long run 0.9332
    - 6h: 8 calls (32 a day), hit rate 0.875, chance 0.292, naive rule 0.466, lift 3.00x
    - 24h: 47 calls (47 a day), hit rate 0.936, chance 0.288, naive rule 0.479, lift 3.25x
    - 7d: 414 calls (59 a day), hit rate 0.925, chance 0.298, naive rule 0.504, lift 3.10x
    - 30d: 1719 calls (57 a day), hit rate 0.939, chance 0.291, naive rule 0.482, lift 3.23x
  - next: threshold 0.5449, hit rate recent 0.5315 / long run 0.5727
    - 6h: 13 calls (53 a day), hit rate 0.385, chance 0.292, lift 1.32x
    - 24h: 57 calls (57 a day), hit rate 0.526, chance 0.288, lift 1.83x
    - 7d: 674 calls (96 a day), hit rate 0.568, chance 0.298, lift 1.91x
    - 30d: 2477 calls (83 a day), hit rate 0.583, chance 0.291, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.491; 0.35: 539, 0.513; 0.40: 484, 0.562; 0.45: 415, 0.632; 0.50: 362, 0.686; 0.55: 317, 0.728; 0.60: 270, 0.773; 0.65: 224, 0.803; 0.70: 180, 0.835; 0.75: 139, 0.873; 0.80: 96, 0.912; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.460; 0.40: 410, 0.489; 0.45: 315, 0.525; 0.50: 204, 0.560; 0.55: 91, 0.581; 0.60: 14, 0.602; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 105326, probability skill vs chance 0.2154, widened contest next: False
  - now: threshold 0.6987, hit rate recent 0.7987 / long run 0.8244
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.161, naive rule 0.329, lift 3.87x
    - 24h: 38 calls (38 a day), hit rate 0.789, chance 0.188, naive rule 0.405, lift 4.20x
    - 7d: 346 calls (49 a day), hit rate 0.809, chance 0.190, naive rule 0.412, lift 4.26x
    - 30d: 1574 calls (52 a day), hit rate 0.829, chance 0.187, naive rule 0.393, lift 4.43x
  - next: threshold 0.4241, hit rate recent 0.4553 / long run 0.4781
    - 6h: 26 calls (106 a day), hit rate 0.308, chance 0.161, lift 1.91x
    - 24h: 108 calls (109 a day), hit rate 0.509, chance 0.188, lift 2.71x
    - 7d: 580 calls (83 a day), hit rate 0.483, chance 0.190, lift 2.54x
    - 30d: 2167 calls (72 a day), hit rate 0.486, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 355, 0.481; 0.40: 286, 0.553; 0.45: 234, 0.610; 0.50: 182, 0.664; 0.55: 139, 0.709; 0.60: 109, 0.750; 0.65: 82, 0.792; 0.70: 60, 0.822; 0.75: 33, 0.862; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.389; 0.35: 251, 0.425; 0.40: 161, 0.455; 0.45: 79, 0.475; 0.50: 18, 0.513; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 105323, probability skill vs chance 0.2051, widened contest next: True
  - now: threshold 0.5836, hit rate recent 0.6882 / long run 0.701
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.099, naive rule 0.266, lift 5.80x
    - 24h: 37 calls (37 a day), hit rate 0.676, chance 0.114, naive rule 0.330, lift 5.93x
    - 7d: 369 calls (53 a day), hit rate 0.672, chance 0.123, naive rule 0.348, lift 5.45x
    - 30d: 1573 calls (52 a day), hit rate 0.713, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.3542, hit rate recent 0.3615 / long run 0.3952
    - 6h: 20 calls (82 a day), hit rate 0.250, chance 0.099, lift 2.54x
    - 24h: 67 calls (67 a day), hit rate 0.358, chance 0.114, lift 3.14x
    - 7d: 564 calls (81 a day), hit rate 0.390, chance 0.123, lift 3.16x
    - 30d: 2121 calls (71 a day), hit rate 0.409, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 261, 0.416; 0.35: 197, 0.491; 0.40: 151, 0.551; 0.45: 119, 0.593; 0.50: 91, 0.634; 0.55: 65, 0.684; 0.60: 45, 0.724; 0.65: 24, 0.775; 0.70: 9, 0.828; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.352; 0.35: 108, 0.390; 0.40: 45, 0.423; 0.45: 9, 0.464; 0.50: 1, 0.371
- **K=13**: model 1792022400, labels learned 105318, probability skill vs chance 0.1782, widened contest next: False
  - now: threshold 0.4015, hit rate recent 0.5584 / long run 0.5822
    - 6h: 11 calls (46 a day), hit rate 0.364, chance 0.070, naive rule 0.229, lift 5.23x
    - 24h: 42 calls (42 a day), hit rate 0.500, chance 0.073, naive rule 0.266, lift 6.82x
    - 7d: 347 calls (50 a day), hit rate 0.582, chance 0.079, naive rule 0.290, lift 7.35x
    - 30d: 1478 calls (49 a day), hit rate 0.588, chance 0.078, naive rule 0.273, lift 7.55x
  - next: threshold 0.301, hit rate recent 0.2808 / long run 0.3092
    - 6h: 7 calls (29 a day), hit rate 0.143, chance 0.070, lift 2.05x
    - 24h: 42 calls (42 a day), hit rate 0.262, chance 0.073, lift 3.57x
    - 7d: 463 calls (66 a day), hit rate 0.315, chance 0.079, lift 3.98x
    - 30d: 2045 calls (68 a day), hit rate 0.315, chance 0.078, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.454; 0.35: 85, 0.514; 0.40: 60, 0.564; 0.45: 41, 0.618; 0.50: 25, 0.652; 0.55: 14, 0.706; 0.60: 4, 0.752; 0.65: 1, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.329; 0.35: 13, 0.374; 0.40: 2, 0.420; 0.45: 0, 0.286

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.769 | -1.25% | 0.917 | 0.500 | 0.253 | 0.450 | -0.061 |
| 6h | 30.719 | 4.97% | 0.928 | 0.558 | 0.252 | 0.504 | 0.564 |
| 24h | 22.468 | 4.72% | 0.903 | 0.515 | 0.251 | 0.499 | 0.569 |
| 7d | 14.140 | 4.46% | 0.900 | 0.502 | 0.251 | 0.494 | 0.678 |
| 30d | 14.185 | 4.07% | 0.900 | 0.500 | 0.251 | 0.495 | 0.683 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.524 | 19.640 | 20.045 | 19.972 | 19.669 | 20.227 | 19.671 | 19.541 | 19.744 | 19.769 |
| 6h | 32.327 | 31.911 | 30.432 | 30.584 | 30.903 | 31.617 | 30.795 | 30.591 | 30.499 | 30.719 |
| 24h | 23.581 | 22.851 | 22.520 | 22.417 | 22.754 | 22.894 | 22.487 | 22.427 | 22.390 | 22.468 |
| 7d | 14.801 | 14.295 | 14.227 | 14.160 | 14.399 | 14.372 | 14.145 | 14.103 | 14.111 | 14.140 |
| 30d | 14.787 | 14.317 | 14.267 | 14.209 | 14.446 | 14.382 | 14.184 | 14.156 | 14.157 | 14.185 |

## Next candle

- candle starting 2026-10-15 07:34 UTC, last close 2367.96
- P(up) 0.5066, return quantiles (bp): {'05': -11.497, '10': -8.572, '25': -4.105, '40': -1.28, '50': 0.091, '60': 1.365, '75': 4.178, '90': 8.485, '95': 11.507}
- changepoint probability 0.0424, regime age 196.5 min
- agent weights: empirical 0.003, ewma 0.010, garch 0.250, har 0.234, bocpd 0.054, hmm 0.010, online_qr 0.164, lgbm 0.276

## Learning log

- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.09, 5.01, 13.97], current probabilities: [0.016, 0.881, 0.103]
- live generator: {'versions': 60, 'latest_effective': '2026-10-15 07:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.185, 'l_abs': 0.733, 'l_hi': 0.715, 'l_lo': 0.733, 'b05': 0.776, 'b25': 0.71, 'b75': 0.706, 'b95': 0.78}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.139, 1.317, 1.684, 2.003, 2.288, 2.683, 2.549, 2.82, 3.038, 3.39, 4.001, 4.704, 5.091, 5.176]}
- calibration offsets (in sigma): {'05': 0.0465, '10': 0.033, '25': 0.0625, '40': 0.072, '50': 0.025, '60': -0.012, '75': -0.0125, '90': -0.033, '95': -0.0465}
