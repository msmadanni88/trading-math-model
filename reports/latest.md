# ETH-USD 60s candle generator - report

- generated: 2026-11-19 10:11 UTC
- last closed candle: 2026-11-19 10:11 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.528 (671) [0.498, 0.554] | 0.517 (2879) [0.500, 0.533] | 0.515 (7481) [0.504, 0.527] | 0.518 (4509) [0.503, 0.533] | 0.550 (40) | 0.500 | flat -0.004 (noise 0.027) |
| colour_clear | 0.582 (802) | 0.546 (5627) [0.535, 0.559] | 0.542 (23983) [0.536, 0.548] | 0.525 (61396) [0.519, 0.530] | 0.543 (37158) [0.538, 0.548] | 0.508 (366) | 0.500 | flat +0.000 (noise 0.011) |
| colour_confident | 0.619 (181) | 0.554 (1009) [0.529, 0.583] | 0.577 (4557) [0.565, 0.588] | 0.586 (6759) [0.576, 0.597] | 0.586 (6759) [0.576, 0.597] | 0.494 (79) | 0.500 | flat -0.013 (noise 0.023) |
| colour_next | 0.539 (1433) | 0.533 (10045) [0.527, 0.539] | 0.530 (42895) [0.526, 0.534] | 0.518 (111478) [0.515, 0.522] | 0.530 (67129) [0.527, 0.533] | 0.514 (609) | 0.500 | flat +0.002 (noise 0.008) |
| colour_path | 0.506 (20062) | 0.502 (140630) [0.501, 0.504] | 0.502 (600530) [0.501, 0.503] | 0.501 (1560692) [0.500, 0.502] | 0.501 (939806) [0.500, 0.502] | 0.492 (8526) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.679 (56) | 0.590 (266) [0.553, 0.633] | 0.615 (1205) [0.597, 0.632] | 0.625 (1779) [0.609, 0.641] | 0.625 (1779) [0.609, 0.641] | 0.619 (21) | 0.500 | flat -0.038 (noise 0.043) |
| reversal_k13_next | 0.322 (87) | 0.311 (460) [0.278, 0.351] | 0.329 (1855) [0.312, 0.345] | 0.314 (5156) [0.305, 0.324] | 0.325 (3051) [0.313, 0.335] | 0.323 (31) | 0.077 | flat -0.021 (noise 0.030) |
| reversal_k13_now | 0.542 (59) | 0.570 (358) [0.522, 0.629] | 0.571 (1610) [0.550, 0.592] | 0.573 (4016) [0.561, 0.586] | 0.569 (2544) [0.552, 0.585] | 0.560 (25) | 0.077 | flat -0.007 (noise 0.037) |
| reversal_k3_next | 0.613 (62) | 0.602 (387) [0.576, 0.644] | 0.603 (2408) [0.590, 0.616] | 0.589 (6489) [0.581, 0.597] | 0.590 (4049) [0.580, 0.601] | 0.625 (24) | 0.293 | flat -0.025 (noise 0.036) |
| reversal_k3_now | 0.983 (57) | 0.944 (373) [0.930, 0.959] | 0.934 (1718) [0.925, 0.944] | 0.936 (4455) [0.930, 0.941] | 0.932 (2692) [0.925, 0.940] | 0.917 (24) | 0.293 | flat +0.024 (noise 0.018) |
| reversal_k5_next | 0.436 (55) | 0.481 (445) [0.433, 0.534] | 0.498 (2242) [0.480, 0.516] | 0.485 (5902) [0.473, 0.496] | 0.480 (3912) [0.466, 0.494] | 0.500 (18) | 0.186 | flat -0.037 (noise 0.039) |
| reversal_k5_now | 0.772 (57) | 0.762 (433) [0.739, 0.787] | 0.794 (1725) [0.778, 0.809] | 0.816 (4238) [0.806, 0.826] | 0.803 (2627) [0.791, 0.815] | 0.846 (26) | 0.187 | flat -0.012 (noise 0.032) |
| reversal_k8_next | 0.391 (87) | 0.402 (488) [0.367, 0.447] | 0.407 (2399) [0.393, 0.422] | 0.397 (6060) [0.386, 0.406] | 0.397 (3954) [0.385, 0.409] | 0.577 (26) | 0.121 | flat -0.021 (noise 0.032) |
| reversal_k8_now | 0.692 (65) | 0.649 (393) [0.612, 0.697] | 0.680 (1588) [0.660, 0.701] | 0.695 (4088) [0.682, 0.708] | 0.683 (2501) [0.667, 0.699] | 0.760 (25) | 0.122 | flat -0.046 (noise 0.034) |
| overall | 0.510 (22120) | 0.506 (154683) [0.505, 0.508] | 0.506 (661849) [0.505, 0.507] | 0.504 (1720055) [0.503, 0.505] | 0.505 (1036774) [0.504, 0.506] | 0.497 (9374) | - | flat +0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06838, 0.09898] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5316, 'levels': [{'threshold': 0.06838, 'calls_per_day': 147.2, 'win_rate': 0.5445}, {'threshold': 0.09898, 'calls_per_day': 37.3, 'win_rate': 0.5954}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42893, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15084 | 0.349 | 0.533 (14870) | 0.569 (2281) | 0.750 (2516) |
| volatility: normal | 15083 | 0.375 | 0.529 (15025) | 0.600 (1396) | 0.733 (2321) |
| volatility: wild | 15084 | 0.390 | 0.530 (15045) | 0.573 (1111) | 0.761 (2123) |
| session: Asia 00-08 | 15360 | 0.371 | 0.534 (15248) | 0.576 (1668) | 0.745 (2299) |
| session: Europe 08-13 | 9431 | 0.365 | 0.531 (9354) | 0.591 (1168) | 0.750 (1511) |
| session: US 13-21 | 14880 | 0.379 | 0.533 (14791) | 0.595 (1312) | 0.751 (2296) |
| session: late 21-24 | 5580 | 0.364 | 0.515 (5547) | 0.531 (640) | 0.741 (854) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.360 | 0.373 | 0.315 | 0.315 | 0.417 | 0.223 | 0.497 | 1.085 |
| 6h | 360 | 0.391 | 0.384 | 0.320 | 0.362 | 0.525 | 0.277 | 0.504 | 1.152 |
| 24h | 1440 | 0.390 | 0.382 | 0.306 | 0.344 | 0.524 | 0.270 | 0.510 | 1.146 |
| 7d | 10080 | 0.386 | 0.377 | 0.302 | 0.335 | 0.531 | 0.272 | 0.500 | 1.154 |
| 30d | 43200 | 0.371 | 0.364 | 0.284 | 0.316 | 0.530 | 0.266 | 0.476 | 1.255 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.360 / 0.417 / 0.883; 2: 0.360 / 0.417 / 0.950; 3: 0.372 / 0.500 / 0.850; 4: 0.376 / 0.500 / 0.900; 5: 0.385 / 0.450 / 0.917; 6: 0.385 / 0.550 / 0.833; 7: 0.378 / 0.467 / 0.900; 8: 0.375 / 0.517 / 0.917; 9: 0.367 / 0.500 / 0.933; 10: 0.358 / 0.433 / 0.950; 11: 0.373 / 0.500 / 1.000; 12: 0.395 / 0.533 / 0.933; 13: 0.366 / 0.433 / 0.900; 14: 0.378 / 0.550 / 0.933; 15: 0.358 / 0.467 / 0.933
- 6h: 1: 0.391 / 0.525 / 0.911; 2: 0.366 / 0.453 / 0.964; 3: 0.382 / 0.508 / 0.886; 4: 0.379 / 0.494 / 0.933; 5: 0.380 / 0.503 / 0.942; 6: 0.377 / 0.494 / 0.917; 7: 0.378 / 0.475 / 0.950; 8: 0.372 / 0.494 / 0.947; 9: 0.369 / 0.486 / 0.947; 10: 0.378 / 0.492 / 0.967; 11: 0.378 / 0.517 / 0.983; 12: 0.374 / 0.475 / 0.947; 13: 0.369 / 0.466 / 0.933; 14: 0.394 / 0.547 / 0.947; 15: 0.371 / 0.472 / 0.950
- 24h: 1: 0.390 / 0.524 / 0.905; 2: 0.381 / 0.501 / 0.912; 3: 0.377 / 0.492 / 0.890; 4: 0.379 / 0.508 / 0.906; 5: 0.380 / 0.506 / 0.919; 6: 0.373 / 0.478 / 0.893; 7: 0.379 / 0.508 / 0.926; 8: 0.379 / 0.517 / 0.922; 9: 0.374 / 0.500 / 0.924; 10: 0.372 / 0.495 / 0.915; 11: 0.377 / 0.506 / 0.924; 12: 0.378 / 0.506 / 0.919; 13: 0.373 / 0.498 / 0.915; 14: 0.380 / 0.532 / 0.917; 15: 0.368 / 0.476 / 0.913
- 7d: 1: 0.386 / 0.531 / 0.899; 2: 0.372 / 0.491 / 0.901; 3: 0.377 / 0.514 / 0.899; 4: 0.371 / 0.493 / 0.901; 5: 0.373 / 0.502 / 0.901; 6: 0.371 / 0.501 / 0.900; 7: 0.373 / 0.507 / 0.901; 8: 0.374 / 0.512 / 0.901; 9: 0.366 / 0.487 / 0.901; 10: 0.372 / 0.507 / 0.901; 11: 0.371 / 0.506 / 0.902; 12: 0.372 / 0.506 / 0.900; 13: 0.368 / 0.498 / 0.900; 14: 0.370 / 0.506 / 0.900; 15: 0.367 / 0.496 / 0.900
- 30d: 1: 0.371 / 0.530 / 0.897; 2: 0.358 / 0.493 / 0.900; 3: 0.362 / 0.512 / 0.900; 4: 0.358 / 0.498 / 0.900; 5: 0.359 / 0.505 / 0.900; 6: 0.356 / 0.501 / 0.900; 7: 0.357 / 0.501 / 0.900; 8: 0.358 / 0.507 / 0.900; 9: 0.356 / 0.500 / 0.900; 10: 0.356 / 0.502 / 0.900; 11: 0.356 / 0.504 / 0.900; 12: 0.356 / 0.502 / 0.900; 13: 0.355 / 0.499 / 0.900; 14: 0.355 / 0.502 / 0.900; 15: 0.354 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.150 (body 0.107, range 0.193); 'price stays where it was' would score 0.116; colour right 0.583; typical miss of the close 12.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.157 (body 0.107, range 0.208); 'price stays where it was' would score 0.170; colour right 0.506; typical miss of the close 7.9 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.135 (body 0.089, range 0.182); 'price stays where it was' would score 0.141; colour right 0.509; typical miss of the close 13.0 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.127 (body 0.084, range 0.171); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 14.7 bp; chain ended on the right side 0.529 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.129; colour right 0.502; typical miss of the close 9.9 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.2; 2: 0.204 / 6.0; 3: 0.167 / 7.7; 4: 0.134 / 8.1; 5: 0.125 / 8.8; 6: 0.120 / 9.6; 7: 0.112 / 10.1; 8: 0.100 / 11.0; 9: 0.093 / 11.3; 10: 0.090 / 11.8; 11: 0.086 / 12.1; 12: 0.079 / 12.5; 13: 0.074 / 13.1; 14: 0.068 / 13.5; 15: 0.067 / 14.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 155885, probability skill vs chance 0.2343, widened contest next: False
  - now: threshold 0.8316, hit rate recent 0.9488 / long run 0.9341
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.297, naive rule 0.519, lift 2.99x
    - 24h: 56 calls (56 a day), hit rate 0.946, chance 0.295, naive rule 0.510, lift 3.20x
    - 7d: 370 calls (53 a day), hit rate 0.941, chance 0.289, naive rule 0.502, lift 3.26x
    - 30d: 1715 calls (57 a day), hit rate 0.934, chance 0.294, naive rule 0.501, lift 3.18x
  - next: threshold 0.5624, hit rate recent 0.5973 / long run 0.6055
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.297, lift 2.24x
    - 24h: 59 calls (59 a day), hit rate 0.610, chance 0.295, lift 2.07x
    - 7d: 374 calls (53 a day), hit rate 0.615, chance 0.289, lift 2.13x
    - 30d: 2377 calls (79 a day), hit rate 0.605, chance 0.294, lift 2.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.502; 0.35: 530, 0.527; 0.40: 476, 0.577; 0.45: 410, 0.645; 0.50: 361, 0.690; 0.55: 312, 0.736; 0.60: 262, 0.782; 0.65: 222, 0.810; 0.70: 173, 0.843; 0.75: 139, 0.874; 0.80: 92, 0.907; 0.85: 44, 0.943; 0.90: 4, 0.968
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.434; 0.35: 492, 0.467; 0.40: 390, 0.508; 0.45: 293, 0.544; 0.50: 188, 0.577; 0.55: 81, 0.588; 0.60: 11, 0.644; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 155883, probability skill vs chance 0.2133, widened contest next: True
  - now: threshold 0.6985, hit rate recent 0.8103 / long run 0.782
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.201, naive rule 0.441, lift 4.47x
    - 24h: 60 calls (60 a day), hit rate 0.783, chance 0.191, naive rule 0.411, lift 4.10x
    - 7d: 438 calls (63 a day), hit rate 0.774, chance 0.186, naive rule 0.412, lift 4.17x
    - 30d: 1728 calls (58 a day), hit rate 0.795, chance 0.186, naive rule 0.410, lift 4.26x
  - next: threshold 0.4626, hit rate recent 0.4442 / long run 0.4907
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.201, lift 2.76x
    - 24h: 49 calls (49 a day), hit rate 0.449, chance 0.191, lift 2.35x
    - 7d: 432 calls (62 a day), hit rate 0.486, chance 0.186, lift 2.62x
    - 30d: 2205 calls (74 a day), hit rate 0.502, chance 0.186, lift 2.69x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 361, 0.474; 0.40: 292, 0.543; 0.45: 236, 0.603; 0.50: 187, 0.653; 0.55: 150, 0.688; 0.60: 113, 0.735; 0.65: 79, 0.772; 0.70: 49, 0.806; 0.75: 27, 0.840; 0.80: 8, 0.867
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.389; 0.35: 253, 0.429; 0.40: 161, 0.459; 0.45: 64, 0.502; 0.50: 8, 0.562; 0.55: 1, 0.476
- **K=8**: model 1794960000, labels learned 155880, probability skill vs chance 0.2118, widened contest next: False
  - now: threshold 0.573, hit rate recent 0.7121 / long run 0.6758
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.143, naive rule 0.448, lift 6.36x
    - 24h: 66 calls (66 a day), hit rate 0.712, chance 0.126, naive rule 0.355, lift 5.66x
    - 7d: 401 calls (57 a day), hit rate 0.661, chance 0.123, naive rule 0.349, lift 5.37x
    - 30d: 1595 calls (53 a day), hit rate 0.682, chance 0.122, naive rule 0.342, lift 5.61x
  - next: threshold 0.3662, hit rate recent 0.4629 / long run 0.4141
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.143, lift 5.00x
    - 24h: 79 calls (80 a day), hit rate 0.456, chance 0.126, lift 3.62x
    - 7d: 480 calls (69 a day), hit rate 0.412, chance 0.123, lift 3.35x
    - 30d: 2373 calls (79 a day), hit rate 0.412, chance 0.122, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.426; 0.35: 197, 0.487; 0.40: 155, 0.534; 0.45: 118, 0.578; 0.50: 84, 0.636; 0.55: 60, 0.673; 0.60: 40, 0.709; 0.65: 23, 0.771; 0.70: 10, 0.817; 0.75: 2, 0.750
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 163, 0.372; 0.35: 84, 0.403; 0.40: 25, 0.439; 0.45: 5, 0.465; 0.50: 1, 0.731
- **K=13**: model 1794960000, labels learned 155875, probability skill vs chance 0.1846, widened contest next: False
  - now: threshold 0.449, hit rate recent 0.5478 / long run 0.5695
    - 6h: 12 calls (50 a day), hit rate 0.667, chance 0.091, naive rule 0.410, lift 7.30x
    - 24h: 64 calls (65 a day), hit rate 0.547, chance 0.084, naive rule 0.315, lift 6.52x
    - 7d: 366 calls (52 a day), hit rate 0.577, chance 0.079, naive rule 0.301, lift 7.27x
    - 30d: 1609 calls (54 a day), hit rate 0.572, chance 0.078, naive rule 0.290, lift 7.30x
  - next: threshold 0.2902, hit rate recent 0.3073 / long run 0.3213
    - 6h: 17 calls (71 a day), hit rate 0.294, chance 0.091, lift 3.22x
    - 24h: 82 calls (83 a day), hit rate 0.329, chance 0.084, lift 3.93x
    - 7d: 459 calls (66 a day), hit rate 0.312, chance 0.079, lift 3.93x
    - 30d: 1856 calls (62 a day), hit rate 0.328, chance 0.078, lift 4.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 138, 0.427; 0.35: 100, 0.475; 0.40: 69, 0.534; 0.45: 48, 0.585; 0.50: 33, 0.625; 0.55: 21, 0.644; 0.60: 11, 0.686; 0.65: 3, 0.617; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.335; 0.35: 14, 0.349; 0.40: 2, 0.417; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.794 | 3.81% | 0.900 | 0.467 | 0.250 | 0.500 | 0.091 |
| 6h | 13.938 | 3.27% | 0.914 | 0.492 | 0.251 | 0.494 | 0.264 |
| 24h | 20.804 | 2.92% | 0.901 | 0.498 | 0.251 | 0.490 | 0.619 |
| 7d | 24.276 | 4.21% | 0.900 | 0.500 | 0.250 | 0.499 | 0.665 |
| 30d | 17.689 | 4.68% | 0.900 | 0.500 | 0.250 | 0.504 | 0.710 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.340 | 13.945 | 13.948 | 13.670 | 13.971 | 13.998 | 13.706 | 13.819 | 13.757 | 13.794 |
| 6h | 14.409 | 14.025 | 14.016 | 13.933 | 14.132 | 14.116 | 13.871 | 13.899 | 13.906 | 13.938 |
| 24h | 21.429 | 20.979 | 20.900 | 20.864 | 21.153 | 20.934 | 20.740 | 20.734 | 20.758 | 20.804 |
| 7d | 25.344 | 24.464 | 24.420 | 24.300 | 24.774 | 24.566 | 24.257 | 24.229 | 24.236 | 24.276 |
| 30d | 18.557 | 17.849 | 17.806 | 17.743 | 18.038 | 17.978 | 17.670 | 17.649 | 17.657 | 17.689 |

## Next candle

- candle starting 2026-11-19 10:11 UTC, last close 1806.49
- P(up) 0.5039, return quantiles (bp): {'05': -11.475, '10': -8.733, '25': -4.608, '40': -1.741, '50': 0.069, '60': 2.048, '75': 4.801, '90': 9.244, '95': 12.269}
- changepoint probability 0.1646, regime age 220.1 min
- agent weights: empirical 0.015, ewma 0.107, garch 0.124, har 0.166, bocpd 0.050, hmm 0.069, online_qr 0.246, lgbm 0.224

## Learning log

- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- HMM volatility states (sd, bp per minute): [5.82, 10.34, 24.91], current probabilities: [0.589, 0.379, 0.032]
- live generator: {'versions': 60, 'latest_effective': '2026-11-19 10:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.431, 'l_abs': 0.728, 'l_hi': 0.789, 'l_lo': 0.723, 'b05': 0.723, 'b25': 0.706, 'b75': 0.692, 'b95': 0.708}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.037, 2.016, 1.763, 1.86, 2.494, 2.166, 2.367, 2.516, 2.503, 2.428, 3.43, 3.798, 3.503, 3.781]}
- calibration offsets (in sigma): {'05': 0.105, '10': 0.05, '25': -0.005, '40': 0.01, '50': 0.03, '60': 0.07, '75': 0.035, '90': 0.01, '95': -0.005}
