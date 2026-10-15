# ETH-USD 60s candle generator - report

- generated: 2026-10-15 20:29 UTC
- last closed candle: 2026-10-15 20:29 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.505 (671) [0.479, 0.535] | 0.513 (2875) [0.493, 0.531] | 0.510 (4122) [0.494, 0.525] | 0.506 (1150) [0.475, 0.538] | 0.494 (81) | 0.500 | flat -0.004 (noise 0.035) |
| colour_clear | 0.559 (843) | 0.541 (5560) [0.534, 0.549] | 0.515 (23376) [0.507, 0.523] | 0.509 (33481) [0.503, 0.515] | 0.543 (9243) [0.536, 0.549] | 0.547 (674) | 0.500 | flat +0.015 (noise 0.013) |
| colour_confident | 0.537 (67) | 0.599 (882) [0.574, 0.634] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.569 (58) | 0.500 | flat -0.010 (noise 0.033) |
| colour_next | 0.542 (1436) | 0.526 (9976) [0.520, 0.532] | 0.511 (42873) [0.506, 0.517] | 0.508 (61433) [0.504, 0.512] | 0.528 (17084) [0.522, 0.534] | 0.519 (1225) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.501 (139664) [0.500, 0.502] | 0.501 (600222) [0.500, 0.502] | 0.501 (860062) [0.499, 0.502] | 0.500 (239176) [0.498, 0.502] | 0.512 (17150) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.462 (13) | 0.657 (233) [0.603, 0.720] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.800 (10) | 0.500 | flat +0.009 (noise 0.051) |
| reversal_k13_next | 0.244 (45) | 0.316 (471) [0.290, 0.342] | 0.314 (2053) [0.299, 0.330] | 0.305 (2977) [0.293, 0.319] | 0.319 (872) [0.303, 0.334] | 0.300 (40) | 0.077 | flat +0.005 (noise 0.029) |
| reversal_k13_now | 0.548 (42) | 0.593 (346) [0.566, 0.621] | 0.587 (1480) [0.567, 0.609] | 0.583 (2108) [0.567, 0.601] | 0.588 (636) [0.559, 0.621] | 0.537 (41) | 0.077 | flat +0.004 (noise 0.036) |
| reversal_k3_next | 0.591 (66) | 0.574 (676) [0.552, 0.598] | 0.583 (2477) [0.569, 0.599] | 0.584 (3532) [0.572, 0.597] | 0.576 (1092) [0.557, 0.599] | 0.534 (73) | 0.293 | flat -0.011 (noise 0.028) |
| reversal_k3_now | 0.980 (49) | 0.929 (423) [0.915, 0.947] | 0.939 (1723) [0.931, 0.947] | 0.938 (2459) [0.931, 0.945] | 0.930 (696) [0.919, 0.941] | 0.895 (38) | 0.293 | flat -0.001 (noise 0.018) |
| reversal_k5_next | 0.543 (94) | 0.489 (564) [0.469, 0.510] | 0.489 (2146) [0.472, 0.507] | 0.485 (3005) [0.471, 0.501] | 0.469 (1015) [0.445, 0.495] | 0.406 (96) | 0.187 | flat +0.027 (noise 0.028) |
| reversal_k5_now | 0.849 (33) | 0.811 (354) [0.785, 0.839] | 0.831 (1577) [0.815, 0.846] | 0.833 (2241) [0.820, 0.846] | 0.822 (630) [0.799, 0.844] | 0.733 (45) | 0.188 | flat -0.030 (noise 0.028) |
| reversal_k8_next | 0.386 (57) | 0.398 (571) [0.379, 0.418] | 0.410 (2107) [0.394, 0.429] | 0.396 (3097) [0.382, 0.410] | 0.395 (991) [0.376, 0.414] | 0.370 (81) | 0.122 | flat +0.000 (noise 0.030) |
| reversal_k8_now | 0.725 (40) | 0.674 (374) [0.640, 0.712] | 0.714 (1578) [0.693, 0.735] | 0.709 (2257) [0.693, 0.726] | 0.699 (670) [0.668, 0.730] | 0.676 (34) | 0.122 | flat -0.052 (noise 0.033) |
| overall | 0.507 (22062) | 0.504 (154090) [0.503, 0.506] | 0.504 (661111) [0.502, 0.505] | 0.503 (947293) [0.502, 0.504] | 0.504 (264012) [0.501, 0.506] | 0.513 (18904) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07457, 0.116] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.525, 'levels': [{'threshold': 0.07457, 'calls_per_day': 143.1, 'win_rate': 0.5949}, {'threshold': 0.116, 'calls_per_day': 35.8, 'win_rate': 0.6838}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 17172, 'rate': 0.5289}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15290 | 0.337 | 0.519 (15056) | 0.600 (1236) | 0.776 (2469) |
| volatility: normal | 15289 | 0.362 | 0.512 (15223) | 0.592 (289) | 0.784 (2117) |
| volatility: wild | 15290 | 0.375 | 0.502 (15250) | 0.638 (141) | 0.764 (2117) |
| session: Asia 00-08 | 15360 | 0.356 | 0.516 (15262) | 0.604 (598) | 0.772 (2201) |
| session: Europe 08-13 | 9600 | 0.352 | 0.510 (9519) | 0.589 (423) | 0.785 (1472) |
| session: US 13-21 | 15329 | 0.367 | 0.506 (15232) | 0.576 (415) | 0.778 (2216) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5516) | 0.670 (230) | 0.753 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.364 | 0.383 | 0.287 | 0.287 | 0.550 | 0.263 | 0.465 | 1.285 |
| 6h | 360 | 0.384 | 0.384 | 0.294 | 0.337 | 0.511 | 0.280 | 0.487 | 1.148 |
| 24h | 1440 | 0.374 | 0.370 | 0.291 | 0.331 | 0.521 | 0.265 | 0.483 | 1.143 |
| 7d | 10080 | 0.357 | 0.349 | 0.272 | 0.302 | 0.525 | 0.259 | 0.455 | 1.247 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.512 | 0.250 | 0.466 | 1.299 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.364 / 0.550 / 0.883; 2: 0.336 / 0.483 / 0.883; 3: 0.358 / 0.550 / 0.867; 4: 0.372 / 0.517 / 0.917; 5: 0.339 / 0.467 / 0.950; 6: 0.383 / 0.583 / 0.950; 7: 0.330 / 0.417 / 0.900; 8: 0.372 / 0.533 / 0.950; 9: 0.387 / 0.617 / 0.983; 10: 0.354 / 0.533 / 0.983; 11: 0.404 / 0.650 / 0.983; 12: 0.375 / 0.600 / 1.000; 13: 0.371 / 0.600 / 1.000; 14: 0.368 / 0.583 / 1.000; 15: 0.357 / 0.517 / 1.000
- 6h: 1: 0.384 / 0.511 / 0.928; 2: 0.366 / 0.450 / 0.942; 3: 0.382 / 0.503 / 0.922; 4: 0.369 / 0.444 / 0.925; 5: 0.377 / 0.508 / 0.922; 6: 0.388 / 0.511 / 0.914; 7: 0.372 / 0.506 / 0.906; 8: 0.374 / 0.497 / 0.922; 9: 0.372 / 0.500 / 0.914; 10: 0.375 / 0.492 / 0.911; 11: 0.380 / 0.534 / 0.906; 12: 0.383 / 0.520 / 0.900; 13: 0.366 / 0.503 / 0.900; 14: 0.376 / 0.536 / 0.889; 15: 0.371 / 0.500 / 0.867
- 24h: 1: 0.374 / 0.521 / 0.906; 2: 0.364 / 0.494 / 0.901; 3: 0.369 / 0.511 / 0.901; 4: 0.366 / 0.501 / 0.898; 5: 0.366 / 0.522 / 0.899; 6: 0.366 / 0.508 / 0.895; 7: 0.365 / 0.519 / 0.895; 8: 0.356 / 0.494 / 0.897; 9: 0.361 / 0.500 / 0.899; 10: 0.364 / 0.519 / 0.899; 11: 0.360 / 0.512 / 0.899; 12: 0.361 / 0.515 / 0.897; 13: 0.360 / 0.517 / 0.894; 14: 0.358 / 0.517 / 0.890; 15: 0.362 / 0.522 / 0.887
- 7d: 1: 0.357 / 0.525 / 0.903; 2: 0.346 / 0.496 / 0.900; 3: 0.349 / 0.512 / 0.899; 4: 0.345 / 0.497 / 0.900; 5: 0.348 / 0.510 / 0.900; 6: 0.346 / 0.503 / 0.900; 7: 0.345 / 0.502 / 0.900; 8: 0.344 / 0.501 / 0.901; 9: 0.344 / 0.496 / 0.901; 10: 0.346 / 0.509 / 0.901; 11: 0.342 / 0.496 / 0.900; 12: 0.344 / 0.504 / 0.900; 13: 0.344 / 0.504 / 0.900; 14: 0.342 / 0.503 / 0.900; 15: 0.345 / 0.505 / 0.900
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.096 (body 0.063, range 0.129); 'price stays where it was' would score 0.121; colour right 0.417; typical miss of the close 13.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.113 (body 0.079, range 0.148); 'price stays where it was' would score 0.152; colour right 0.466; typical miss of the close 14.5 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.133 (body 0.089, range 0.176); 'price stays where it was' would score 0.143; colour right 0.493; typical miss of the close 13.8 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.122 (body 0.084, range 0.160); 'price stays where it was' would score 0.129; colour right 0.496; typical miss of the close 7.5 bp; chain ended on the right side 0.505 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.515 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.196 / 4.5; 3: 0.165 / 6.1; 4: 0.133 / 6.8; 5: 0.121 / 7.5; 6: 0.109 / 8.0; 7: 0.102 / 8.4; 8: 0.096 / 8.8; 9: 0.086 / 8.7; 10: 0.084 / 9.6; 11: 0.078 / 10.3; 12: 0.075 / 10.7; 13: 0.063 / 10.9; 14: 0.065 / 11.3; 15: 0.058 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 106103, probability skill vs chance 0.2243, widened contest next: False
  - now: threshold 0.841, hit rate recent 0.9293 / long run 0.9325
    - 6h: 7 calls (28 a day), hit rate 0.857, chance 0.277, naive rule 0.435, lift 3.09x
    - 24h: 44 calls (44 a day), hit rate 0.909, chance 0.286, naive rule 0.472, lift 3.18x
    - 7d: 404 calls (58 a day), hit rate 0.926, chance 0.298, naive rule 0.503, lift 3.10x
    - 30d: 1716 calls (57 a day), hit rate 0.938, chance 0.290, naive rule 0.482, lift 3.23x
  - next: threshold 0.5397, hit rate recent 0.544 / long run 0.5723
    - 6h: 22 calls (89 a day), hit rate 0.500, chance 0.277, lift 1.80x
    - 24h: 75 calls (75 a day), hit rate 0.533, chance 0.286, lift 1.86x
    - 7d: 690 calls (99 a day), hit rate 0.575, chance 0.298, lift 1.93x
    - 30d: 2486 calls (83 a day), hit rate 0.581, chance 0.290, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.490; 0.35: 539, 0.513; 0.40: 484, 0.562; 0.45: 415, 0.631; 0.50: 361, 0.686; 0.55: 317, 0.727; 0.60: 270, 0.772; 0.65: 224, 0.801; 0.70: 179, 0.834; 0.75: 139, 0.871; 0.80: 96, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.459; 0.40: 410, 0.489; 0.45: 314, 0.524; 0.50: 204, 0.559; 0.55: 91, 0.579; 0.60: 14, 0.597; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 106101, probability skill vs chance 0.2112, widened contest next: True
  - now: threshold 0.6962, hit rate recent 0.7817 / long run 0.8206
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.161, naive rule 0.326, lift 5.07x
    - 24h: 49 calls (49 a day), hit rate 0.755, chance 0.183, naive rule 0.393, lift 4.13x
    - 7d: 349 calls (50 a day), hit rate 0.808, chance 0.190, naive rule 0.413, lift 4.26x
    - 30d: 1579 calls (53 a day), hit rate 0.828, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.4234, hit rate recent 0.4248 / long run 0.4735
    - 6h: 27 calls (110 a day), hit rate 0.333, chance 0.161, lift 2.06x
    - 24h: 101 calls (101 a day), hit rate 0.406, chance 0.183, lift 2.22x
    - 7d: 602 calls (86 a day), hit rate 0.487, chance 0.190, lift 2.56x
    - 30d: 2192 calls (73 a day), hit rate 0.483, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.418; 0.35: 355, 0.482; 0.40: 285, 0.554; 0.45: 233, 0.610; 0.50: 182, 0.665; 0.55: 138, 0.710; 0.60: 109, 0.750; 0.65: 82, 0.791; 0.70: 60, 0.821; 0.75: 33, 0.865; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 251, 0.425; 0.40: 161, 0.454; 0.45: 78, 0.471; 0.50: 18, 0.504; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 106098, probability skill vs chance 0.1993, widened contest next: False
  - now: threshold 0.5655, hit rate recent 0.6871 / long run 0.7008
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.111, naive rule 0.261, lift 4.99x
    - 24h: 38 calls (38 a day), hit rate 0.711, chance 0.114, naive rule 0.315, lift 6.25x
    - 7d: 353 calls (50 a day), hit rate 0.686, chance 0.124, naive rule 0.350, lift 5.53x
    - 30d: 1568 calls (52 a day), hit rate 0.714, chance 0.122, naive rule 0.330, lift 5.83x
  - next: threshold 0.3443, hit rate recent 0.3716 / long run 0.3942
    - 6h: 26 calls (107 a day), hit rate 0.308, chance 0.111, lift 2.76x
    - 24h: 85 calls (86 a day), hit rate 0.365, chance 0.114, lift 3.21x
    - 7d: 543 calls (78 a day), hit rate 0.403, chance 0.124, lift 3.26x
    - 30d: 2126 calls (71 a day), hit rate 0.406, chance 0.122, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 261, 0.417; 0.35: 197, 0.491; 0.40: 151, 0.551; 0.45: 119, 0.595; 0.50: 91, 0.636; 0.55: 65, 0.684; 0.60: 44, 0.725; 0.65: 24, 0.777; 0.70: 9, 0.829; 0.75: 1, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.351; 0.35: 108, 0.387; 0.40: 44, 0.420; 0.45: 9, 0.461; 0.50: 1, 0.364
- **K=13**: model 1792022400, labels learned 106093, probability skill vs chance 0.1742, widened contest next: False
  - now: threshold 0.427, hit rate recent 0.555 / long run 0.581
    - 6h: 9 calls (38 a day), hit rate 0.333, chance 0.070, naive rule 0.204, lift 4.79x
    - 24h: 45 calls (45 a day), hit rate 0.578, chance 0.082, naive rule 0.288, lift 7.04x
    - 7d: 345 calls (49 a day), hit rate 0.588, chance 0.080, naive rule 0.292, lift 7.36x
    - 30d: 1475 calls (49 a day), hit rate 0.589, chance 0.078, naive rule 0.273, lift 7.55x
  - next: threshold 0.3005, hit rate recent 0.279 / long run 0.3075
    - 6h: 13 calls (54 a day), hit rate 0.231, chance 0.070, lift 3.32x
    - 24h: 42 calls (42 a day), hit rate 0.310, chance 0.082, lift 3.77x
    - 7d: 450 calls (64 a day), hit rate 0.318, chance 0.080, lift 3.98x
    - 30d: 2025 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.455; 0.35: 84, 0.516; 0.40: 60, 0.566; 0.45: 41, 0.619; 0.50: 25, 0.652; 0.55: 14, 0.704; 0.60: 4, 0.746; 0.65: 0, 1.000
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.326; 0.35: 13, 0.365; 0.40: 2, 0.406

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.931 | 3.53% | 0.883 | 0.483 | 0.246 | 0.583 | -0.095 |
| 6h | 20.652 | 3.95% | 0.931 | 0.522 | 0.249 | 0.531 | 0.625 |
| 24h | 23.998 | 4.10% | 0.904 | 0.501 | 0.250 | 0.516 | 0.589 |
| 7d | 14.144 | 4.07% | 0.902 | 0.500 | 0.251 | 0.493 | 0.668 |
| 30d | 14.175 | 3.94% | 0.900 | 0.500 | 0.251 | 0.495 | 0.678 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.477 | 14.951 | 15.052 | 15.072 | 14.962 | 14.874 | 15.127 | 14.969 | 14.978 | 14.931 |
| 6h | 21.501 | 20.834 | 20.768 | 20.813 | 20.779 | 20.973 | 20.809 | 20.874 | 20.729 | 20.652 |
| 24h | 25.025 | 24.408 | 24.011 | 23.992 | 24.240 | 24.457 | 24.048 | 24.003 | 23.943 | 23.998 |
| 7d | 14.745 | 14.294 | 14.231 | 14.170 | 14.399 | 14.342 | 14.154 | 14.110 | 14.117 | 14.144 |
| 30d | 14.757 | 14.299 | 14.258 | 14.200 | 14.432 | 14.369 | 14.174 | 14.146 | 14.147 | 14.175 |

## Next candle

- candle starting 2026-10-15 20:29 UTC, last close 2459.47
- P(up) 0.5361, return quantiles (bp): {'05': -9.452, '10': -6.972, '25': -3.48, '40': -0.866, '50': 0.477, '60': 1.998, '75': 4.368, '90': 7.62, '95': 9.6}
- changepoint probability 0.0383, regime age 151.9 min
- agent weights: empirical 0.003, ewma 0.068, garch 0.180, har 0.215, bocpd 0.083, hmm 0.039, online_qr 0.193, lgbm 0.218

## Learning log

- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- HMM volatility states (sd, bp per minute): [2.37, 5.56, 18.85], current probabilities: [0.0, 0.968, 0.032]
- live generator: {'versions': 60, 'latest_effective': '2026-10-15 20:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.309, 'l_abs': 0.736, 'l_hi': 0.711, 'l_lo': 0.732, 'b05': 0.768, 'b25': 0.719, 'b75': 0.682, 'b95': 0.777}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.351, 1.796, 1.996, 2.192, 2.454, 2.765, 2.734, 2.906, 3.008, 3.161, 3.308, 3.664, 4.127, 4.455]}
- calibration offsets (in sigma): {'05': 0.114, '10': 0.088, '25': 0.08, '40': 0.112, '50': 0.09, '60': 0.108, '75': 0.08, '90': 0.002, '95': -0.094}
