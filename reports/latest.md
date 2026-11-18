# ETH-USD 60s candle generator - report

- generated: 2026-11-18 12:16 UTC
- last closed candle: 2026-11-18 12:16 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.532 (671) [0.501, 0.559] | 0.519 (2879) [0.502, 0.536] | 0.515 (7385) [0.504, 0.527] | 0.518 (4413) [0.502, 0.532] | 0.510 (49) | 0.500 | flat +0.010 (noise 0.027) |
| colour_clear | 0.521 (796) | 0.536 (5667) [0.528, 0.545] | 0.541 (23987) [0.535, 0.547] | 0.524 (60594) [0.519, 0.529] | 0.542 (36356) [0.538, 0.547] | 0.593 (415) | 0.500 | flat -0.005 (noise 0.012) |
| colour_confident | 0.518 (189) | 0.537 (895) [0.521, 0.556] | 0.579 (4528) [0.566, 0.591] | 0.585 (6578) [0.575, 0.596] | 0.585 (6578) [0.575, 0.596] | 0.663 (95) | 0.500 | flat -0.032 (noise 0.023) |
| colour_next | 0.516 (1436) | 0.528 (10051) [0.520, 0.536] | 0.531 (42898) [0.526, 0.535] | 0.518 (110045) [0.514, 0.521] | 0.530 (65696) [0.526, 0.533] | 0.544 (731) | 0.500 | flat -0.002 (noise 0.009) |
| colour_path | 0.503 (20104) | 0.503 (140714) [0.501, 0.505] | 0.502 (600572) [0.501, 0.503] | 0.501 (1540630) [0.500, 0.502] | 0.501 (919744) [0.500, 0.502] | 0.503 (10234) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.605 (43) | 0.563 (215) [0.532, 0.585] | 0.612 (1188) [0.595, 0.629] | 0.623 (1723) [0.607, 0.638] | 0.623 (1723) [0.607, 0.638] | 0.655 (29) | 0.500 | flat -0.062 (noise 0.045) |
| reversal_k13_next | 0.233 (73) | 0.315 (445) [0.279, 0.358] | 0.329 (1851) [0.312, 0.345] | 0.314 (5069) [0.304, 0.324] | 0.325 (2964) [0.314, 0.336] | 0.348 (46) | 0.077 | flat -0.014 (noise 0.031) |
| reversal_k13_now | 0.467 (60) | 0.576 (351) [0.524, 0.634] | 0.568 (1608) [0.547, 0.590] | 0.574 (3957) [0.561, 0.587] | 0.569 (2485) [0.553, 0.587] | 0.560 (25) | 0.077 | flat +0.003 (noise 0.037) |
| reversal_k3_next | 0.556 (81) | 0.612 (374) [0.578, 0.666] | 0.600 (2463) [0.586, 0.613] | 0.589 (6427) [0.580, 0.597] | 0.590 (3987) [0.580, 0.601] | 0.605 (38) | 0.293 | flat -0.007 (noise 0.036) |
| reversal_k3_now | 0.952 (42) | 0.933 (373) [0.922, 0.945] | 0.932 (1717) [0.922, 0.942] | 0.935 (4398) [0.930, 0.941] | 0.931 (2635) [0.924, 0.938] | 1.000 (31) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.355 (62) | 0.476 (447) [0.425, 0.534] | 0.496 (2328) [0.478, 0.514] | 0.485 (5847) [0.474, 0.497] | 0.481 (3857) [0.467, 0.495] | 0.469 (32) | 0.186 | flat -0.057 (noise 0.036) |
| reversal_k5_now | 0.817 (60) | 0.746 (445) [0.714, 0.776] | 0.796 (1724) [0.779, 0.811] | 0.817 (4181) [0.806, 0.827] | 0.804 (2570) [0.791, 0.817] | 0.800 (30) | 0.187 | flat -0.053 (noise 0.030) |
| reversal_k8_next | 0.365 (85) | 0.408 (471) [0.369, 0.455] | 0.404 (2426) [0.389, 0.421] | 0.397 (5973) [0.386, 0.407] | 0.397 (3867) [0.385, 0.409] | 0.409 (44) | 0.121 | flat -0.015 (noise 0.033) |
| reversal_k8_now | 0.639 (61) | 0.643 (384) [0.608, 0.692] | 0.676 (1573) [0.656, 0.697] | 0.695 (4023) [0.683, 0.708] | 0.683 (2436) [0.667, 0.699] | 0.719 (32) | 0.122 | flat -0.051 (noise 0.035) |
| overall | 0.504 (22160) | 0.506 (154726) [0.505, 0.508] | 0.506 (662039) [0.504, 0.507] | 0.504 (1697935) [0.503, 0.505] | 0.505 (1014654) [0.504, 0.506] | 0.508 (11292) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06705, 0.09685] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5317, 'levels': [{'threshold': 0.06705, 'calls_per_day': 144.4, 'win_rate': 0.5513}, {'threshold': 0.09685, 'calls_per_day': 37.0, 'win_rate': 0.5769}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42895, 'rate': 0.5303}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15126 | 0.348 | 0.532 (14908) | 0.567 (2302) | 0.744 (2517) |
| volatility: normal | 15125 | 0.374 | 0.530 (15064) | 0.603 (1386) | 0.736 (2327) |
| volatility: wild | 15125 | 0.389 | 0.529 (15087) | 0.579 (1074) | 0.762 (2105) |
| session: Asia 00-08 | 15360 | 0.369 | 0.534 (15242) | 0.579 (1681) | 0.746 (2279) |
| session: Europe 08-13 | 9556 | 0.364 | 0.530 (9477) | 0.588 (1176) | 0.750 (1546) |
| session: US 13-21 | 14880 | 0.378 | 0.533 (14792) | 0.597 (1290) | 0.748 (2281) |
| session: late 21-24 | 5580 | 0.365 | 0.516 (5548) | 0.532 (615) | 0.740 (843) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.406 | 0.370 | 0.247 | 0.247 | 0.567 | 0.284 | 0.527 | 1.276 |
| 6h | 360 | 0.391 | 0.367 | 0.310 | 0.360 | 0.539 | 0.281 | 0.501 | 1.171 |
| 24h | 1440 | 0.387 | 0.375 | 0.305 | 0.348 | 0.538 | 0.276 | 0.498 | 1.132 |
| 7d | 10080 | 0.384 | 0.377 | 0.301 | 0.333 | 0.532 | 0.272 | 0.497 | 1.160 |
| 30d | 43200 | 0.371 | 0.364 | 0.283 | 0.315 | 0.530 | 0.266 | 0.476 | 1.250 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.406 / 0.567 / 0.867; 2: 0.368 / 0.417 / 0.917; 3: 0.394 / 0.617 / 0.933; 4: 0.378 / 0.500 / 0.917; 5: 0.387 / 0.533 / 0.850; 6: 0.351 / 0.433 / 0.983; 7: 0.392 / 0.567 / 0.933; 8: 0.377 / 0.533 / 0.983; 9: 0.348 / 0.450 / 0.983; 10: 0.359 / 0.533 / 1.000; 11: 0.361 / 0.417 / 1.000; 12: 0.411 / 0.650 / 0.983; 13: 0.371 / 0.533 / 0.967; 14: 0.382 / 0.550 / 0.967; 15: 0.359 / 0.533 / 0.983
- 6h: 1: 0.391 / 0.539 / 0.900; 2: 0.373 / 0.458 / 0.881; 3: 0.379 / 0.553 / 0.917; 4: 0.377 / 0.469 / 0.875; 5: 0.377 / 0.514 / 0.792; 6: 0.374 / 0.492 / 0.931; 7: 0.360 / 0.458 / 0.783; 8: 0.386 / 0.548 / 0.814; 9: 0.365 / 0.461 / 0.786; 10: 0.387 / 0.567 / 0.858; 11: 0.374 / 0.486 / 0.831; 12: 0.400 / 0.579 / 0.783; 13: 0.368 / 0.480 / 0.775; 14: 0.384 / 0.534 / 0.781; 15: 0.366 / 0.492 / 0.800
- 24h: 1: 0.387 / 0.538 / 0.895; 2: 0.371 / 0.478 / 0.895; 3: 0.375 / 0.528 / 0.900; 4: 0.368 / 0.481 / 0.897; 5: 0.373 / 0.514 / 0.884; 6: 0.369 / 0.494 / 0.906; 7: 0.376 / 0.524 / 0.874; 8: 0.374 / 0.515 / 0.883; 9: 0.363 / 0.475 / 0.878; 10: 0.371 / 0.502 / 0.892; 11: 0.367 / 0.493 / 0.884; 12: 0.378 / 0.524 / 0.874; 13: 0.370 / 0.502 / 0.881; 14: 0.370 / 0.504 / 0.886; 15: 0.362 / 0.487 / 0.919
- 7d: 1: 0.384 / 0.532 / 0.898; 2: 0.368 / 0.486 / 0.900; 3: 0.377 / 0.518 / 0.900; 4: 0.370 / 0.494 / 0.900; 5: 0.371 / 0.500 / 0.896; 6: 0.371 / 0.506 / 0.901; 7: 0.372 / 0.507 / 0.896; 8: 0.372 / 0.510 / 0.897; 9: 0.365 / 0.487 / 0.896; 10: 0.371 / 0.506 / 0.899; 11: 0.370 / 0.509 / 0.898; 12: 0.370 / 0.506 / 0.896; 13: 0.368 / 0.503 / 0.896; 14: 0.368 / 0.502 / 0.895; 15: 0.367 / 0.500 / 0.896
- 30d: 1: 0.371 / 0.530 / 0.897; 2: 0.358 / 0.493 / 0.900; 3: 0.362 / 0.513 / 0.900; 4: 0.357 / 0.497 / 0.900; 5: 0.358 / 0.504 / 0.899; 6: 0.356 / 0.501 / 0.901; 7: 0.356 / 0.500 / 0.899; 8: 0.357 / 0.507 / 0.900; 9: 0.355 / 0.500 / 0.900; 10: 0.356 / 0.503 / 0.900; 11: 0.355 / 0.504 / 0.900; 12: 0.355 / 0.503 / 0.899; 13: 0.354 / 0.499 / 0.899; 14: 0.354 / 0.501 / 0.900; 15: 0.354 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.218 (body 0.153, range 0.284); 'price stays where it was' would score 0.147; colour right 0.533; typical miss of the close 6.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.138 (body 0.094, range 0.182); 'price stays where it was' would score 0.111; colour right 0.503; typical miss of the close 8.7 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.127 (body 0.083, range 0.171); 'price stays where it was' would score 0.121; colour right 0.492; typical miss of the close 13.0 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.126 (body 0.083, range 0.170); 'price stays where it was' would score 0.129; colour right 0.505; typical miss of the close 14.1 bp; chain ended on the right side 0.525 of 671 chains; n=10080
- 30d: match 0.125 (body 0.084, range 0.166); 'price stays where it was' would score 0.128; colour right 0.502; typical miss of the close 9.8 bp; chain ended on the right side 0.520 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.1; 2: 0.204 / 5.9; 3: 0.166 / 7.7; 4: 0.134 / 8.1; 5: 0.125 / 8.7; 6: 0.119 / 9.6; 7: 0.111 / 10.1; 8: 0.099 / 11.0; 9: 0.091 / 11.3; 10: 0.090 / 11.6; 11: 0.084 / 12.1; 12: 0.078 / 12.4; 13: 0.073 / 13.0; 14: 0.068 / 13.5; 15: 0.067 / 13.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 154570, probability skill vs chance 0.2305, widened contest next: True
  - now: threshold 0.8317, hit rate recent 0.9668 / long run 0.9336
    - 6h: 20 calls (81 a day), hit rate 1.000, chance 0.290, naive rule 0.495, lift 3.45x
    - 24h: 53 calls (53 a day), hit rate 0.962, chance 0.281, naive rule 0.480, lift 3.42x
    - 7d: 368 calls (53 a day), hit rate 0.938, chance 0.289, naive rule 0.500, lift 3.25x
    - 30d: 1723 calls (57 a day), hit rate 0.933, chance 0.293, naive rule 0.499, lift 3.18x
  - next: threshold 0.5616, hit rate recent 0.5693 / long run 0.6039
    - 6h: 19 calls (77 a day), hit rate 0.526, chance 0.290, lift 1.81x
    - 24h: 74 calls (74 a day), hit rate 0.568, chance 0.281, lift 2.02x
    - 7d: 392 calls (56 a day), hit rate 0.615, chance 0.289, lift 2.13x
    - 30d: 2433 calls (81 a day), hit rate 0.602, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.501; 0.35: 530, 0.526; 0.40: 476, 0.577; 0.45: 409, 0.646; 0.50: 359, 0.691; 0.55: 312, 0.736; 0.60: 262, 0.781; 0.65: 221, 0.810; 0.70: 173, 0.842; 0.75: 139, 0.873; 0.80: 92, 0.904; 0.85: 45, 0.941; 0.90: 4, 0.969
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.434; 0.35: 492, 0.467; 0.40: 391, 0.507; 0.45: 294, 0.542; 0.50: 186, 0.574; 0.55: 81, 0.585; 0.60: 11, 0.643; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 154568, probability skill vs chance 0.2177, widened contest next: True
  - now: threshold 0.6975, hit rate recent 0.8047 / long run 0.7808
    - 6h: 17 calls (69 a day), hit rate 0.765, chance 0.191, naive rule 0.382, lift 4.00x
    - 24h: 61 calls (61 a day), hit rate 0.836, chance 0.192, naive rule 0.405, lift 4.36x
    - 7d: 430 calls (61 a day), hit rate 0.756, chance 0.186, naive rule 0.413, lift 4.07x
    - 30d: 1727 calls (58 a day), hit rate 0.795, chance 0.186, naive rule 0.408, lift 4.28x
  - next: threshold 0.4614, hit rate recent 0.4325 / long run 0.4943
    - 6h: 16 calls (65 a day), hit rate 0.438, chance 0.191, lift 2.29x
    - 24h: 66 calls (66 a day), hit rate 0.455, chance 0.192, lift 2.37x
    - 7d: 452 calls (65 a day), hit rate 0.482, chance 0.186, lift 2.59x
    - 30d: 2279 calls (76 a day), hit rate 0.498, chance 0.186, lift 2.68x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.419; 0.35: 360, 0.474; 0.40: 291, 0.543; 0.45: 236, 0.602; 0.50: 187, 0.651; 0.55: 150, 0.686; 0.60: 113, 0.734; 0.65: 78, 0.772; 0.70: 49, 0.806; 0.75: 27, 0.840; 0.80: 8, 0.870
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.387; 0.35: 253, 0.427; 0.40: 161, 0.458; 0.45: 64, 0.503; 0.50: 9, 0.554; 0.55: 1, 0.455
- **K=8**: model 1794960000, labels learned 154565, probability skill vs chance 0.2029, widened contest next: False
  - now: threshold 0.5683, hit rate recent 0.6756 / long run 0.6724
    - 6h: 18 calls (74 a day), hit rate 0.667, chance 0.116, naive rule 0.313, lift 5.76x
    - 24h: 64 calls (64 a day), hit rate 0.688, chance 0.125, naive rule 0.343, lift 5.51x
    - 7d: 381 calls (54 a day), hit rate 0.646, chance 0.123, naive rule 0.351, lift 5.24x
    - 30d: 1587 calls (53 a day), hit rate 0.677, chance 0.121, naive rule 0.340, lift 5.59x
  - next: threshold 0.366, hit rate recent 0.4021 / long run 0.4093
    - 6h: 21 calls (86 a day), hit rate 0.429, chance 0.116, lift 3.70x
    - 24h: 90 calls (91 a day), hit rate 0.422, chance 0.125, lift 3.38x
    - 7d: 479 calls (68 a day), hit rate 0.407, chance 0.123, lift 3.30x
    - 30d: 2408 calls (80 a day), hit rate 0.405, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.426; 0.35: 196, 0.487; 0.40: 155, 0.533; 0.45: 119, 0.578; 0.50: 84, 0.634; 0.55: 60, 0.669; 0.60: 40, 0.709; 0.65: 23, 0.772; 0.70: 10, 0.818; 0.75: 2, 0.772
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 163, 0.369; 0.35: 84, 0.398; 0.40: 24, 0.436; 0.45: 5, 0.452; 0.50: 1, 0.750
- **K=13**: model 1794960000, labels learned 154560, probability skill vs chance 0.1769, widened contest next: False
  - now: threshold 0.4441, hit rate recent 0.5429 / long run 0.5722
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.090, naive rule 0.333, lift 6.85x
    - 24h: 56 calls (57 a day), hit rate 0.554, chance 0.084, naive rule 0.304, lift 6.60x
    - 7d: 348 calls (50 a day), hit rate 0.572, chance 0.079, naive rule 0.300, lift 7.27x
    - 30d: 1612 calls (54 a day), hit rate 0.569, chance 0.078, naive rule 0.288, lift 7.29x
  - next: threshold 0.2894, hit rate recent 0.3314 / long run 0.3234
    - 6h: 19 calls (79 a day), hit rate 0.474, chance 0.090, lift 5.27x
    - 24h: 85 calls (86 a day), hit rate 0.329, chance 0.084, lift 3.93x
    - 7d: 454 calls (65 a day), hit rate 0.311, chance 0.079, lift 3.95x
    - 30d: 1849 calls (62 a day), hit rate 0.329, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 137, 0.426; 0.35: 99, 0.473; 0.40: 68, 0.533; 0.45: 47, 0.585; 0.50: 32, 0.627; 0.55: 21, 0.653; 0.60: 11, 0.695; 0.65: 3, 0.631; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.336; 0.35: 14, 0.350; 0.40: 2, 0.420; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.633 | 3.32% | 0.850 | 0.550 | 0.250 | 0.500 | 0.440 |
| 6h | 13.695 | 5.40% | 0.900 | 0.489 | 0.251 | 0.469 | 0.248 |
| 24h | 21.450 | 4.19% | 0.899 | 0.496 | 0.251 | 0.497 | 0.654 |
| 7d | 23.751 | 4.29% | 0.900 | 0.500 | 0.250 | 0.506 | 0.673 |
| 30d | 17.533 | 4.68% | 0.900 | 0.500 | 0.250 | 0.504 | 0.710 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.136 | 14.726 | 14.714 | 14.620 | 14.784 | 14.810 | 14.497 | 14.445 | 14.546 | 14.633 |
| 6h | 14.477 | 13.723 | 13.755 | 13.705 | 13.804 | 13.891 | 13.672 | 13.661 | 13.670 | 13.695 |
| 24h | 22.388 | 21.562 | 21.530 | 21.440 | 21.713 | 21.663 | 21.412 | 21.372 | 21.403 | 21.450 |
| 7d | 24.815 | 23.949 | 23.909 | 23.776 | 24.259 | 24.064 | 23.738 | 23.702 | 23.713 | 23.751 |
| 30d | 18.394 | 17.692 | 17.650 | 17.586 | 17.880 | 17.821 | 17.515 | 17.494 | 17.502 | 17.533 |

## Next candle

- candle starting 2026-11-18 12:16 UTC, last close 1799.32
- P(up) 0.4859, return quantiles (bp): {'05': -8.686, '10': -6.799, '25': -3.419, '40': -1.29, '50': -0.188, '60': 1.171, '75': 3.171, '90': 6.013, '95': 8.343}
- changepoint probability 0.0535, regime age 331.7 min
- agent weights: empirical 0.005, ewma 0.111, garch 0.111, har 0.180, bocpd 0.058, hmm 0.054, online_qr 0.225, lgbm 0.255

## Learning log

- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- HMM volatility states (sd, bp per minute): [5.62, 10.24, 24.94], current probabilities: [0.945, 0.053, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-18 12:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.283, 'l_abs': 0.723, 'l_hi': 0.8, 'l_lo': 0.73, 'b05': 0.728, 'b25': 0.756, 'b75': 0.668, 'b95': 0.723}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.627, 1.57, 2.264, 4.621, 1.982, 6.315, 5.538, 6.771, 4.337, 5.912, 8.868, 9.065, 9.24, 8.5]}
- calibration offsets (in sigma): {'05': 0.0175, '10': -0.045, '25': -0.0125, '40': 0.01, '50': -0.025, '60': -0.0, '75': -0.0175, '90': -0.095, '95': -0.0575}
