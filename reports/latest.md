# ETH-USD 60s candle generator - report

- generated: 2026-11-21 19:42 UTC
- last closed candle: 2026-11-21 19:42 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.539 (672) [0.506, 0.567] | 0.519 (2879) [0.502, 0.535] | 0.516 (7673) [0.505, 0.528] | 0.519 (4701) [0.505, 0.534] | 0.462 (78) | 0.500 | flat +0.010 (noise 0.027) |
| colour_clear | 0.577 (822) | 0.551 (5657) [0.538, 0.565] | 0.541 (23972) [0.535, 0.548] | 0.525 (63049) [0.520, 0.531] | 0.544 (38811) [0.539, 0.548] | 0.541 (560) | 0.500 | flat +0.010 (noise 0.010) |
| colour_confident | 0.562 (96) | 0.556 (1109) [0.533, 0.583] | 0.576 (4419) [0.564, 0.587] | 0.586 (7006) [0.576, 0.596] | 0.586 (7006) [0.576, 0.596] | 0.605 (172) | 0.500 | flat -0.003 (noise 0.022) |
| colour_next | 0.542 (1438) | 0.536 (10050) [0.529, 0.541] | 0.530 (42896) [0.526, 0.534] | 0.519 (114352) [0.515, 0.522] | 0.530 (70003) [0.527, 0.533] | 0.519 (1179) | 0.500 | flat +0.006 (noise 0.007) |
| colour_path | 0.509 (20132) | 0.503 (140700) [0.501, 0.506] | 0.502 (600544) [0.501, 0.503] | 0.501 (1600928) [0.500, 0.502] | 0.501 (980042) [0.500, 0.503] | 0.504 (16506) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.643 (14) | 0.611 (288) [0.576, 0.657] | 0.614 (1159) [0.598, 0.631] | 0.626 (1827) [0.610, 0.641] | 0.626 (1827) [0.610, 0.641] | 0.612 (49) | 0.500 | flat -0.012 (noise 0.043) |
| reversal_k13_next | 0.362 (58) | 0.310 (493) [0.278, 0.352] | 0.326 (1868) [0.310, 0.343] | 0.314 (5305) [0.305, 0.323] | 0.324 (3200) [0.313, 0.335] | 0.410 (39) | 0.077 | flat -0.016 (noise 0.030) |
| reversal_k13_now | 0.644 (45) | 0.577 (371) [0.526, 0.637] | 0.572 (1625) [0.552, 0.593] | 0.573 (4129) [0.561, 0.586] | 0.569 (2657) [0.553, 0.585] | 0.605 (38) | 0.077 | flat +0.016 (noise 0.038) |
| reversal_k3_next | 0.562 (160) | 0.578 (526) [0.560, 0.609] | 0.598 (2379) [0.587, 0.610] | 0.588 (6728) [0.580, 0.596] | 0.588 (4288) [0.579, 0.599] | 0.625 (128) | 0.293 | flat -0.039 (noise 0.034) |
| reversal_k3_now | 0.922 (64) | 0.937 (383) [0.920, 0.954] | 0.931 (1727) [0.922, 0.940] | 0.935 (4585) [0.930, 0.940] | 0.931 (2822) [0.924, 0.938] | 0.914 (35) | 0.293 | flat +0.017 (noise 0.018) |
| reversal_k5_next | 0.553 (47) | 0.476 (397) [0.423, 0.542] | 0.505 (2086) [0.490, 0.522] | 0.485 (6003) [0.474, 0.496] | 0.480 (4013) [0.466, 0.494] | 0.696 (23) | 0.187 | flat -0.024 (noise 0.041) |
| reversal_k5_now | 0.831 (65) | 0.794 (437) [0.770, 0.816] | 0.795 (1751) [0.779, 0.810] | 0.817 (4368) [0.806, 0.826] | 0.804 (2757) [0.792, 0.816] | 0.744 (39) | 0.187 | flat +0.056 (noise 0.029) |
| reversal_k8_next | 0.388 (85) | 0.397 (541) [0.369, 0.441] | 0.408 (2360) [0.394, 0.423] | 0.397 (6234) [0.387, 0.406] | 0.397 (4128) [0.385, 0.408] | 0.475 (59) | 0.121 | flat -0.013 (noise 0.031) |
| reversal_k8_now | 0.712 (59) | 0.675 (416) [0.636, 0.718] | 0.682 (1628) [0.662, 0.701] | 0.695 (4218) [0.683, 0.708] | 0.684 (2631) [0.669, 0.699] | 0.632 (38) | 0.122 | flat +0.012 (noise 0.034) |
| overall | 0.514 (22249) | 0.507 (154986) [0.505, 0.510] | 0.506 (661743) [0.505, 0.507] | 0.504 (1764523) [0.503, 0.505] | 0.505 (1081242) [0.504, 0.506] | 0.507 (18162) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07136, 0.1017] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5331, 'levels': [{'threshold': 0.07136, 'calls_per_day': 148.1, 'win_rate': 0.5567}, {'threshold': 0.1017, 'calls_per_day': 36.9, 'win_rate': 0.6293}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42896, 'rate': 0.53}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15274 | 0.349 | 0.532 (15055) | 0.568 (2237) | 0.756 (2541) |
| volatility: normal | 15274 | 0.378 | 0.528 (15219) | 0.589 (1438) | 0.738 (2397) |
| volatility: wild | 15274 | 0.390 | 0.530 (15235) | 0.584 (1092) | 0.755 (2156) |
| session: Asia 00-08 | 15360 | 0.370 | 0.530 (15247) | 0.570 (1665) | 0.748 (2300) |
| session: Europe 08-13 | 9600 | 0.366 | 0.531 (9525) | 0.584 (1192) | 0.756 (1540) |
| session: US 13-21 | 15282 | 0.380 | 0.534 (15192) | 0.601 (1332) | 0.747 (2434) |
| session: late 21-24 | 5580 | 0.366 | 0.518 (5545) | 0.536 (578) | 0.750 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.394 | 0.379 | 0.283 | 0.283 | 0.550 | 0.258 | 0.530 | 1.282 |
| 6h | 360 | 0.386 | 0.374 | 0.294 | 0.315 | 0.525 | 0.266 | 0.506 | 1.516 |
| 24h | 1440 | 0.384 | 0.374 | 0.299 | 0.321 | 0.525 | 0.264 | 0.504 | 1.556 |
| 7d | 10080 | 0.387 | 0.378 | 0.304 | 0.340 | 0.533 | 0.270 | 0.504 | 1.197 |
| 30d | 43200 | 0.372 | 0.365 | 0.286 | 0.318 | 0.530 | 0.266 | 0.479 | 1.264 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.394 / 0.550 / 0.933; 2: 0.385 / 0.483 / 0.867; 3: 0.356 / 0.417 / 0.867; 4: 0.403 / 0.617 / 0.883; 5: 0.387 / 0.517 / 0.900; 6: 0.388 / 0.533 / 0.883; 7: 0.384 / 0.483 / 0.850; 8: 0.390 / 0.533 / 0.817; 9: 0.379 / 0.517 / 0.800; 10: 0.392 / 0.600 / 0.867; 11: 0.346 / 0.400 / 0.933; 12: 0.366 / 0.483 / 0.900; 13: 0.383 / 0.533 / 0.900; 14: 0.372 / 0.450 / 0.983; 15: 0.367 / 0.533 / 1.000
- 6h: 1: 0.386 / 0.525 / 0.939; 2: 0.367 / 0.486 / 0.881; 3: 0.350 / 0.439 / 0.850; 4: 0.373 / 0.517 / 0.897; 5: 0.377 / 0.522 / 0.936; 6: 0.362 / 0.492 / 0.947; 7: 0.370 / 0.508 / 0.936; 8: 0.368 / 0.519 / 0.903; 9: 0.368 / 0.522 / 0.914; 10: 0.381 / 0.567 / 0.928; 11: 0.362 / 0.500 / 0.936; 12: 0.373 / 0.531 / 0.928; 13: 0.358 / 0.506 / 0.931; 14: 0.365 / 0.511 / 0.950; 15: 0.355 / 0.472 / 0.953
- 24h: 1: 0.384 / 0.525 / 0.926; 2: 0.372 / 0.504 / 0.918; 3: 0.364 / 0.486 / 0.934; 4: 0.366 / 0.501 / 0.915; 5: 0.367 / 0.499 / 0.919; 6: 0.364 / 0.503 / 0.921; 7: 0.364 / 0.503 / 0.928; 8: 0.363 / 0.508 / 0.927; 9: 0.364 / 0.514 / 0.926; 10: 0.368 / 0.528 / 0.925; 11: 0.361 / 0.506 / 0.922; 12: 0.362 / 0.496 / 0.917; 13: 0.356 / 0.494 / 0.917; 14: 0.357 / 0.490 / 0.917; 15: 0.362 / 0.519 / 0.918
- 7d: 1: 0.387 / 0.533 / 0.902; 2: 0.375 / 0.497 / 0.900; 3: 0.376 / 0.507 / 0.900; 4: 0.374 / 0.497 / 0.901; 5: 0.376 / 0.509 / 0.901; 6: 0.374 / 0.506 / 0.902; 7: 0.373 / 0.503 / 0.901; 8: 0.374 / 0.510 / 0.901; 9: 0.370 / 0.498 / 0.901; 10: 0.374 / 0.512 / 0.901; 11: 0.372 / 0.504 / 0.902; 12: 0.372 / 0.506 / 0.902; 13: 0.370 / 0.503 / 0.902; 14: 0.370 / 0.500 / 0.902; 15: 0.369 / 0.501 / 0.903
- 30d: 1: 0.372 / 0.530 / 0.898; 2: 0.359 / 0.493 / 0.900; 3: 0.363 / 0.511 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.901; 7: 0.358 / 0.501 / 0.901; 8: 0.359 / 0.507 / 0.900; 9: 0.357 / 0.502 / 0.900; 10: 0.358 / 0.504 / 0.900; 11: 0.357 / 0.506 / 0.901; 12: 0.357 / 0.503 / 0.901; 13: 0.356 / 0.501 / 0.901; 14: 0.356 / 0.501 / 0.901; 15: 0.356 / 0.501 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.123 (body 0.071, range 0.175); 'price stays where it was' would score 0.098; colour right 0.400; typical miss of the close 8.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.144 (body 0.093, range 0.196); 'price stays where it was' would score 0.156; colour right 0.561; typical miss of the close 13.8 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.140 (body 0.093, range 0.186); 'price stays where it was' would score 0.143; colour right 0.531; typical miss of the close 17.1 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.129 (body 0.084, range 0.175); 'price stays where it was' would score 0.135; colour right 0.508; typical miss of the close 15.6 bp; chain ended on the right side 0.524 of 672 chains; n=10080
- 30d: match 0.126 (body 0.084, range 0.168); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.3 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.5; 2: 0.204 / 6.2; 3: 0.168 / 8.1; 4: 0.135 / 8.5; 5: 0.126 / 9.1; 6: 0.120 / 9.8; 7: 0.115 / 10.4; 8: 0.101 / 11.4; 9: 0.092 / 11.9; 10: 0.089 / 12.5; 11: 0.086 / 12.9; 12: 0.079 / 12.9; 13: 0.074 / 13.6; 14: 0.068 / 14.1; 15: 0.066 / 14.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 159336, probability skill vs chance 0.2354, widened contest next: False
  - now: threshold 0.8301, hit rate recent 0.9203 / long run 0.9287
    - 6h: 8 calls (32 a day), hit rate 1.000, chance 0.311, naive rule 0.585, lift 3.21x
    - 24h: 46 calls (46 a day), hit rate 0.913, chance 0.301, naive rule 0.543, lift 3.04x
    - 7d: 370 calls (53 a day), hit rate 0.932, chance 0.292, naive rule 0.504, lift 3.20x
    - 30d: 1717 calls (57 a day), hit rate 0.931, chance 0.293, naive rule 0.501, lift 3.18x
  - next: threshold 0.5084, hit rate recent 0.5992 / long run 0.5958
    - 6h: 41 calls (166 a day), hit rate 0.561, chance 0.311, lift 1.80x
    - 24h: 155 calls (156 a day), hit rate 0.619, chance 0.301, lift 2.06x
    - 7d: 632 calls (90 a day), hit rate 0.579, chance 0.292, lift 1.99x
    - 30d: 2424 calls (81 a day), hit rate 0.599, chance 0.293, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.502; 0.35: 529, 0.527; 0.40: 477, 0.575; 0.45: 412, 0.641; 0.50: 363, 0.686; 0.55: 314, 0.732; 0.60: 265, 0.778; 0.65: 223, 0.808; 0.70: 175, 0.839; 0.75: 141, 0.872; 0.80: 93, 0.904; 0.85: 44, 0.941; 0.90: 4, 0.965
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 490, 0.469; 0.40: 388, 0.509; 0.45: 292, 0.543; 0.50: 187, 0.576; 0.55: 80, 0.585; 0.60: 10, 0.631; 0.65: 0, 0.533
- **K=5**: model 1794528000, labels learned 159334, probability skill vs chance 0.2217, widened contest next: False
  - now: threshold 0.6998, hit rate recent 0.7784 / long run 0.7861
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.205, naive rule 0.497, lift 3.79x
    - 24h: 50 calls (50 a day), hit rate 0.780, chance 0.199, naive rule 0.467, lift 3.92x
    - 7d: 422 calls (60 a day), hit rate 0.791, chance 0.191, naive rule 0.421, lift 4.14x
    - 30d: 1755 calls (59 a day), hit rate 0.794, chance 0.187, naive rule 0.412, lift 4.25x
  - next: threshold 0.4616, hit rate recent 0.5583 / long run 0.4963
    - 6h: 8 calls (33 a day), hit rate 0.750, chance 0.205, lift 3.65x
    - 24h: 30 calls (30 a day), hit rate 0.700, chance 0.199, lift 3.52x
    - 7d: 376 calls (54 a day), hit rate 0.465, chance 0.191, lift 2.44x
    - 30d: 2002 calls (67 a day), hit rate 0.508, chance 0.187, lift 2.72x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.422; 0.35: 362, 0.474; 0.40: 293, 0.542; 0.45: 237, 0.602; 0.50: 186, 0.654; 0.55: 149, 0.687; 0.60: 114, 0.732; 0.65: 81, 0.769; 0.70: 50, 0.805; 0.75: 27, 0.841; 0.80: 7, 0.858
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 336, 0.392; 0.35: 251, 0.431; 0.40: 160, 0.461; 0.45: 64, 0.501; 0.50: 8, 0.552; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 159331, probability skill vs chance 0.2188, widened contest next: False
  - now: threshold 0.5797, hit rate recent 0.6633 / long run 0.6746
    - 6h: 8 calls (33 a day), hit rate 0.750, chance 0.134, naive rule 0.450, lift 5.59x
    - 24h: 45 calls (45 a day), hit rate 0.689, chance 0.139, naive rule 0.442, lift 4.96x
    - 7d: 417 calls (60 a day), hit rate 0.659, chance 0.124, naive rule 0.354, lift 5.31x
    - 30d: 1632 calls (54 a day), hit rate 0.680, chance 0.123, naive rule 0.346, lift 5.54x
  - next: threshold 0.355, hit rate recent 0.4289 / long run 0.4102
    - 6h: 24 calls (99 a day), hit rate 0.417, chance 0.134, lift 3.10x
    - 24h: 73 calls (74 a day), hit rate 0.479, chance 0.139, lift 3.45x
    - 7d: 554 calls (79 a day), hit rate 0.392, chance 0.124, lift 3.16x
    - 30d: 2336 calls (78 a day), hit rate 0.413, chance 0.123, lift 3.37x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 253, 0.428; 0.35: 199, 0.488; 0.40: 156, 0.538; 0.45: 120, 0.580; 0.50: 85, 0.636; 0.55: 61, 0.671; 0.60: 41, 0.714; 0.65: 24, 0.770; 0.70: 9, 0.811; 0.75: 2, 0.727
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 162, 0.376; 0.35: 84, 0.404; 0.40: 26, 0.436; 0.45: 6, 0.470; 0.50: 1, 0.704
- **K=13**: model 1795132800, labels learned 159326, probability skill vs chance 0.1996, widened contest next: False
  - now: threshold 0.4533, hit rate recent 0.5934 / long run 0.5717
    - 6h: 6 calls (25 a day), hit rate 0.833, chance 0.088, naive rule 0.467, lift 9.43x
    - 24h: 44 calls (44 a day), hit rate 0.659, chance 0.089, naive rule 0.386, lift 7.42x
    - 7d: 372 calls (53 a day), hit rate 0.562, chance 0.080, naive rule 0.298, lift 7.03x
    - 30d: 1630 calls (54 a day), hit rate 0.572, chance 0.079, naive rule 0.293, lift 7.25x
  - next: threshold 0.3073, hit rate recent 0.3649 / long run 0.3246
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.088, lift 4.71x
    - 24h: 44 calls (44 a day), hit rate 0.409, chance 0.089, lift 4.61x
    - 7d: 495 calls (71 a day), hit rate 0.303, chance 0.080, lift 3.79x
    - 30d: 1869 calls (62 a day), hit rate 0.330, chance 0.079, lift 4.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 139, 0.424; 0.35: 102, 0.474; 0.40: 70, 0.533; 0.45: 49, 0.583; 0.50: 34, 0.624; 0.55: 21, 0.650; 0.60: 10, 0.683; 0.65: 2, 0.567; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.339; 0.35: 15, 0.370; 0.40: 2, 0.419; 0.45: 0, 0.600

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.561 | 19.68% | 0.950 | 0.500 | 0.250 | 0.517 | 0.177 |
| 6h | 23.121 | 6.40% | 0.928 | 0.511 | 0.250 | 0.500 | 0.665 |
| 24h | 32.322 | 5.67% | 0.924 | 0.519 | 0.251 | 0.494 | 0.629 |
| 7d | 26.268 | 4.22% | 0.901 | 0.501 | 0.251 | 0.498 | 0.673 |
| 30d | 18.794 | 4.78% | 0.900 | 0.500 | 0.250 | 0.504 | 0.719 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.639 | 12.577 | 12.795 | 12.752 | 12.752 | 12.911 | 12.550 | 12.543 | 12.622 | 12.561 |
| 6h | 24.702 | 23.466 | 23.474 | 23.125 | 23.964 | 23.383 | 23.322 | 23.177 | 23.149 | 23.121 |
| 24h | 34.266 | 33.034 | 32.748 | 32.364 | 33.351 | 32.772 | 32.404 | 32.270 | 32.303 | 32.322 |
| 7d | 27.424 | 26.497 | 26.434 | 26.271 | 26.801 | 26.571 | 26.266 | 26.220 | 26.227 | 26.268 |
| 30d | 19.739 | 18.974 | 18.928 | 18.850 | 19.175 | 19.102 | 18.780 | 18.754 | 18.763 | 18.794 |

## Next candle

- candle starting 2026-11-21 19:42 UTC, last close 1684.79
- P(up) 0.5137, return quantiles (bp): {'05': -7.211, '10': -5.155, '25': -2.386, '40': -0.688, '50': 0.106, '60': 0.967, '75': 2.591, '90': 5.703, '95': 7.669}
- changepoint probability 0.0159, regime age 114.5 min
- agent weights: empirical 0.003, ewma 0.040, garch 0.056, har 0.277, bocpd 0.009, hmm 0.077, online_qr 0.204, lgbm 0.335

## Learning log

- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- HMM volatility states (sd, bp per minute): [5.86, 10.53, 26.19], current probabilities: [0.964, 0.034, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-11-21 19:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.209, 'l_abs': 0.672, 'l_hi': 0.796, 'l_lo': 0.734, 'b05': 0.739, 'b25': 0.726, 'b75': 0.693, 'b95': 0.742}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.2, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5]], 'cone_width': [1.397, 1.858, 1.76, 1.647, 1.635, 1.917, 2.509, 2.365, 2.352, 2.192, 2.341, 2.592, 2.59, 2.581]}
- calibration offsets (in sigma): {'05': 0.1405, '10': 0.161, '25': 0.1125, '40': 0.074, '50': 0.025, '60': -0.014, '75': -0.0525, '90': -0.051, '95': -0.0905}
