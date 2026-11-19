# ETH-USD 60s candle generator - report

- generated: 2026-11-19 02:02 UTC
- last closed candle: 2026-11-19 02:02 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.528 (671) [0.498, 0.554] | 0.517 (2879) [0.500, 0.533] | 0.515 (7481) [0.504, 0.527] | 0.518 (4509) [0.503, 0.533] | 0.375 (8) | 0.500 | flat -0.004 (noise 0.027) |
| colour_clear | 0.582 (802) | 0.546 (5627) [0.535, 0.559] | 0.542 (23983) [0.536, 0.548] | 0.525 (61396) [0.519, 0.530] | 0.543 (37158) [0.538, 0.548] | 0.471 (70) | 0.500 | flat +0.000 (noise 0.011) |
| colour_confident | 0.619 (181) | 0.554 (1009) [0.529, 0.583] | 0.577 (4557) [0.565, 0.588] | 0.586 (6759) [0.576, 0.597] | 0.586 (6759) [0.576, 0.597] | 0.333 (21) | 0.500 | flat -0.013 (noise 0.023) |
| colour_next | 0.539 (1433) | 0.533 (10045) [0.527, 0.539] | 0.530 (42895) [0.526, 0.534] | 0.518 (111478) [0.515, 0.522] | 0.530 (67129) [0.527, 0.533] | 0.459 (122) | 0.500 | flat +0.002 (noise 0.008) |
| colour_path | 0.506 (20062) | 0.502 (140630) [0.501, 0.504] | 0.502 (600530) [0.501, 0.503] | 0.501 (1560692) [0.500, 0.502] | 0.501 (939806) [0.500, 0.502] | 0.486 (1708) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.679 (56) | 0.590 (266) [0.553, 0.633] | 0.615 (1205) [0.597, 0.632] | 0.625 (1779) [0.609, 0.641] | 0.625 (1779) [0.609, 0.641] | 0.500 (6) | 0.500 | flat -0.038 (noise 0.043) |
| reversal_k13_next | 0.322 (87) | 0.311 (460) [0.278, 0.351] | 0.329 (1855) [0.312, 0.345] | 0.314 (5156) [0.305, 0.324] | 0.325 (3051) [0.313, 0.335] | 0.286 (7) | 0.077 | flat -0.021 (noise 0.030) |
| reversal_k13_now | 0.542 (59) | 0.570 (358) [0.522, 0.629] | 0.571 (1610) [0.550, 0.592] | 0.573 (4016) [0.561, 0.586] | 0.569 (2544) [0.552, 0.585] | 0.500 (6) | 0.077 | flat -0.007 (noise 0.037) |
| reversal_k3_next | 0.613 (62) | 0.602 (387) [0.576, 0.644] | 0.603 (2408) [0.590, 0.616] | 0.589 (6489) [0.581, 0.597] | 0.590 (4049) [0.580, 0.601] | 0.714 (7) | 0.293 | flat -0.025 (noise 0.036) |
| reversal_k3_now | 0.983 (57) | 0.944 (373) [0.930, 0.959] | 0.934 (1718) [0.925, 0.944] | 0.936 (4455) [0.930, 0.941] | 0.932 (2692) [0.925, 0.940] | 0.857 (7) | 0.293 | flat +0.024 (noise 0.018) |
| reversal_k5_next | 0.436 (55) | 0.481 (445) [0.433, 0.534] | 0.498 (2242) [0.480, 0.516] | 0.485 (5902) [0.473, 0.496] | 0.480 (3912) [0.466, 0.494] | 0.500 (6) | 0.186 | flat -0.037 (noise 0.039) |
| reversal_k5_now | 0.772 (57) | 0.762 (433) [0.739, 0.787] | 0.794 (1725) [0.778, 0.809] | 0.816 (4238) [0.806, 0.826] | 0.803 (2627) [0.791, 0.815] | 0.750 (8) | 0.187 | flat -0.012 (noise 0.032) |
| reversal_k8_next | 0.391 (87) | 0.402 (488) [0.367, 0.447] | 0.407 (2399) [0.393, 0.422] | 0.397 (6060) [0.386, 0.406] | 0.397 (3954) [0.385, 0.409] | 0.333 (6) | 0.121 | flat -0.021 (noise 0.032) |
| reversal_k8_now | 0.692 (65) | 0.649 (393) [0.612, 0.697] | 0.680 (1588) [0.660, 0.701] | 0.695 (4088) [0.682, 0.708] | 0.683 (2501) [0.667, 0.699] | 0.500 (6) | 0.122 | flat -0.046 (noise 0.034) |
| overall | 0.510 (22120) | 0.506 (154683) [0.505, 0.508] | 0.506 (661849) [0.505, 0.507] | 0.504 (1720055) [0.503, 0.505] | 0.505 (1036774) [0.504, 0.506] | 0.486 (1891) | - | flat +0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06795, 0.09842] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5333, 'levels': [{'threshold': 0.06795, 'calls_per_day': 147.4, 'win_rate': 0.5507}, {'threshold': 0.09842, 'calls_per_day': 37.6, 'win_rate': 0.5909}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42894, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14921 | 0.349 | 0.533 (14709) | 0.568 (2254) | 0.748 (2495) |
| volatility: normal | 14920 | 0.375 | 0.529 (14862) | 0.600 (1380) | 0.733 (2289) |
| volatility: wild | 14921 | 0.390 | 0.530 (14882) | 0.575 (1096) | 0.761 (2103) |
| session: Asia 00-08 | 15002 | 0.370 | 0.534 (14890) | 0.577 (1632) | 0.743 (2237) |
| session: Europe 08-13 | 9300 | 0.364 | 0.531 (9225) | 0.591 (1146) | 0.749 (1500) |
| session: US 13-21 | 14880 | 0.379 | 0.533 (14791) | 0.595 (1312) | 0.751 (2296) |
| session: late 21-24 | 5580 | 0.364 | 0.515 (5547) | 0.531 (640) | 0.741 (854) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.366 | 0.355 | 0.254 | 0.254 | 0.483 | 0.216 | 0.515 | 1.272 |
| 6h | 360 | 0.370 | 0.372 | 0.298 | 0.327 | 0.490 | 0.242 | 0.499 | 1.139 |
| 24h | 1440 | 0.388 | 0.376 | 0.300 | 0.344 | 0.533 | 0.272 | 0.503 | 1.111 |
| 7d | 10080 | 0.385 | 0.376 | 0.300 | 0.333 | 0.532 | 0.271 | 0.498 | 1.163 |
| 30d | 43200 | 0.371 | 0.364 | 0.284 | 0.315 | 0.530 | 0.266 | 0.476 | 1.252 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.366 / 0.483 / 0.883; 2: 0.385 / 0.567 / 0.767; 3: 0.344 / 0.367 / 0.867; 4: 0.362 / 0.467 / 0.833; 5: 0.367 / 0.417 / 0.767; 6: 0.366 / 0.483 / 0.967; 7: 0.360 / 0.517 / 0.800; 8: 0.379 / 0.550 / 0.800; 9: 0.374 / 0.500 / 0.833; 10: 0.349 / 0.450 / 0.767; 11: 0.371 / 0.500 / 0.717; 12: 0.390 / 0.533 / 0.900; 13: 0.369 / 0.500 / 0.917; 14: 0.366 / 0.533 / 0.900; 15: 0.381 / 0.567 / 0.867
- 6h: 1: 0.370 / 0.490 / 0.911; 2: 0.388 / 0.560 / 0.858; 3: 0.357 / 0.437 / 0.917; 4: 0.369 / 0.507 / 0.869; 5: 0.363 / 0.460 / 0.875; 6: 0.370 / 0.479 / 0.942; 7: 0.367 / 0.507 / 0.897; 8: 0.367 / 0.515 / 0.867; 9: 0.368 / 0.487 / 0.897; 10: 0.362 / 0.487 / 0.875; 11: 0.369 / 0.504 / 0.833; 12: 0.366 / 0.476 / 0.919; 13: 0.370 / 0.507 / 0.936; 14: 0.359 / 0.501 / 0.925; 15: 0.358 / 0.451 / 0.911
- 24h: 1: 0.388 / 0.533 / 0.903; 2: 0.382 / 0.505 / 0.896; 3: 0.374 / 0.510 / 0.915; 4: 0.375 / 0.503 / 0.903; 5: 0.372 / 0.500 / 0.892; 6: 0.370 / 0.486 / 0.915; 7: 0.370 / 0.506 / 0.892; 8: 0.380 / 0.542 / 0.890; 9: 0.372 / 0.500 / 0.892; 10: 0.369 / 0.506 / 0.898; 11: 0.372 / 0.506 / 0.889; 12: 0.378 / 0.517 / 0.897; 13: 0.371 / 0.504 / 0.892; 14: 0.369 / 0.507 / 0.889; 15: 0.362 / 0.480 / 0.895
- 7d: 1: 0.385 / 0.532 / 0.899; 2: 0.370 / 0.489 / 0.899; 3: 0.376 / 0.514 / 0.900; 4: 0.369 / 0.493 / 0.898; 5: 0.371 / 0.501 / 0.898; 6: 0.370 / 0.502 / 0.899; 7: 0.372 / 0.508 / 0.898; 8: 0.373 / 0.514 / 0.898; 9: 0.366 / 0.489 / 0.898; 10: 0.370 / 0.506 / 0.898; 11: 0.371 / 0.508 / 0.898; 12: 0.371 / 0.508 / 0.899; 13: 0.368 / 0.501 / 0.900; 14: 0.368 / 0.503 / 0.899; 15: 0.366 / 0.497 / 0.899
- 30d: 1: 0.371 / 0.530 / 0.897; 2: 0.358 / 0.493 / 0.900; 3: 0.362 / 0.512 / 0.900; 4: 0.357 / 0.497 / 0.900; 5: 0.358 / 0.505 / 0.900; 6: 0.356 / 0.501 / 0.900; 7: 0.357 / 0.501 / 0.900; 8: 0.357 / 0.507 / 0.900; 9: 0.356 / 0.500 / 0.900; 10: 0.356 / 0.502 / 0.900; 11: 0.356 / 0.504 / 0.900; 12: 0.356 / 0.503 / 0.900; 13: 0.355 / 0.500 / 0.900; 14: 0.354 / 0.501 / 0.900; 15: 0.354 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.078 (body 0.033, range 0.122); 'price stays where it was' would score 0.078; colour right 0.483; typical miss of the close 20.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.109 (body 0.064, range 0.154); 'price stays where it was' would score 0.145; colour right 0.493; typical miss of the close 15.0 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.129 (body 0.085, range 0.173); 'price stays where it was' would score 0.127; colour right 0.510; typical miss of the close 12.9 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.126 (body 0.083, range 0.170); 'price stays where it was' would score 0.129; colour right 0.504; typical miss of the close 14.4 bp; chain ended on the right side 0.528 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.9 bp; chain ended on the right side 0.517 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.1; 2: 0.204 / 6.0; 3: 0.167 / 7.7; 4: 0.135 / 8.1; 5: 0.125 / 8.8; 6: 0.119 / 9.6; 7: 0.111 / 10.2; 8: 0.099 / 11.0; 9: 0.092 / 11.3; 10: 0.090 / 11.7; 11: 0.085 / 12.1; 12: 0.079 / 12.5; 13: 0.073 / 13.3; 14: 0.068 / 13.5; 15: 0.067 / 14.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 155396, probability skill vs chance 0.2306, widened contest next: False
  - now: threshold 0.8317, hit rate recent 0.9522 / long run 0.9339
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.285, naive rule 0.500, lift 3.10x
    - 24h: 61 calls (61 a day), hit rate 0.967, chance 0.294, naive rule 0.506, lift 3.29x
    - 7d: 375 calls (54 a day), hit rate 0.941, chance 0.289, naive rule 0.499, lift 3.26x
    - 30d: 1718 calls (57 a day), hit rate 0.934, chance 0.294, naive rule 0.500, lift 3.18x
  - next: threshold 0.5627, hit rate recent 0.5995 / long run 0.606
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.285, lift 2.24x
    - 24h: 61 calls (61 a day), hit rate 0.607, chance 0.294, lift 2.07x
    - 7d: 389 calls (56 a day), hit rate 0.607, chance 0.289, lift 2.10x
    - 30d: 2407 calls (80 a day), hit rate 0.603, chance 0.294, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.502; 0.35: 530, 0.527; 0.40: 476, 0.577; 0.45: 410, 0.646; 0.50: 360, 0.691; 0.55: 312, 0.736; 0.60: 262, 0.782; 0.65: 221, 0.810; 0.70: 173, 0.842; 0.75: 139, 0.873; 0.80: 92, 0.906; 0.85: 44, 0.942; 0.90: 4, 0.968
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.434; 0.35: 492, 0.467; 0.40: 390, 0.507; 0.45: 294, 0.543; 0.50: 187, 0.575; 0.55: 81, 0.586; 0.60: 11, 0.647; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 155394, probability skill vs chance 0.2074, widened contest next: True
  - now: threshold 0.6981, hit rate recent 0.7836 / long run 0.7787
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.194, naive rule 0.422, lift 4.19x
    - 24h: 60 calls (60 a day), hit rate 0.783, chance 0.189, naive rule 0.397, lift 4.15x
    - 7d: 437 calls (62 a day), hit rate 0.762, chance 0.185, naive rule 0.408, lift 4.11x
    - 30d: 1727 calls (58 a day), hit rate 0.794, chance 0.186, naive rule 0.409, lift 4.26x
  - next: threshold 0.4627, hit rate recent 0.4314 / long run 0.4905
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.194, lift 2.81x
    - 24h: 56 calls (56 a day), hit rate 0.464, chance 0.189, lift 2.46x
    - 7d: 446 calls (64 a day), hit rate 0.480, chance 0.185, lift 2.59x
    - 30d: 2241 calls (75 a day), hit rate 0.498, chance 0.186, lift 2.67x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.420; 0.35: 360, 0.474; 0.40: 292, 0.542; 0.45: 237, 0.602; 0.50: 187, 0.652; 0.55: 150, 0.687; 0.60: 113, 0.734; 0.65: 79, 0.771; 0.70: 49, 0.805; 0.75: 27, 0.838; 0.80: 8, 0.868
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.388; 0.35: 253, 0.428; 0.40: 161, 0.457; 0.45: 65, 0.501; 0.50: 9, 0.556; 0.55: 1, 0.476
- **K=8**: model 1794960000, labels learned 155391, probability skill vs chance 0.1939, widened contest next: False
  - now: threshold 0.5717, hit rate recent 0.6588 / long run 0.6704
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.117, naive rule 0.310, lift 5.34x
    - 24h: 65 calls (65 a day), hit rate 0.692, chance 0.120, naive rule 0.324, lift 5.76x
    - 7d: 396 calls (57 a day), hit rate 0.644, chance 0.122, naive rule 0.343, lift 5.27x
    - 30d: 1588 calls (53 a day), hit rate 0.679, chance 0.121, naive rule 0.341, lift 5.59x
  - next: threshold 0.3661, hit rate recent 0.3881 / long run 0.4061
    - 6h: 14 calls (58 a day), hit rate 0.357, chance 0.117, lift 3.05x
    - 24h: 87 calls (88 a day), hit rate 0.414, chance 0.120, lift 3.44x
    - 7d: 487 calls (70 a day), hit rate 0.400, chance 0.122, lift 3.28x
    - 30d: 2397 calls (80 a day), hit rate 0.408, chance 0.121, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.425; 0.35: 197, 0.486; 0.40: 155, 0.533; 0.45: 119, 0.578; 0.50: 84, 0.634; 0.55: 60, 0.670; 0.60: 40, 0.708; 0.65: 23, 0.769; 0.70: 10, 0.814; 0.75: 2, 0.754
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 164, 0.369; 0.35: 84, 0.400; 0.40: 25, 0.436; 0.45: 5, 0.458; 0.50: 1, 0.731
- **K=13**: model 1794960000, labels learned 155386, probability skill vs chance 0.1733, widened contest next: True
  - now: threshold 0.4473, hit rate recent 0.5319 / long run 0.5691
    - 6h: 18 calls (75 a day), hit rate 0.500, chance 0.077, naive rule 0.260, lift 6.51x
    - 24h: 60 calls (61 a day), hit rate 0.567, chance 0.085, naive rule 0.300, lift 6.65x
    - 7d: 360 calls (52 a day), hit rate 0.572, chance 0.079, naive rule 0.295, lift 7.28x
    - 30d: 1609 calls (54 a day), hit rate 0.571, chance 0.078, naive rule 0.288, lift 7.30x
  - next: threshold 0.29, hit rate recent 0.303 / long run 0.3209
    - 6h: 17 calls (71 a day), hit rate 0.294, chance 0.077, lift 3.83x
    - 24h: 86 calls (87 a day), hit rate 0.349, chance 0.085, lift 4.09x
    - 7d: 460 calls (66 a day), hit rate 0.311, chance 0.079, lift 3.96x
    - 30d: 1854 calls (62 a day), hit rate 0.329, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 137, 0.426; 0.35: 100, 0.474; 0.40: 69, 0.534; 0.45: 47, 0.585; 0.50: 33, 0.626; 0.55: 21, 0.647; 0.60: 11, 0.691; 0.65: 3, 0.617; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.336; 0.35: 14, 0.348; 0.40: 2, 0.408; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 23.471 | -0.59% | 0.867 | 0.517 | 0.257 | 0.400 | 0.157 |
| 6h | 19.972 | 0.42% | 0.897 | 0.486 | 0.252 | 0.468 | 0.356 |
| 24h | 20.712 | 3.46% | 0.901 | 0.494 | 0.251 | 0.486 | 0.641 |
| 7d | 24.084 | 4.26% | 0.901 | 0.500 | 0.250 | 0.501 | 0.673 |
| 30d | 17.677 | 4.66% | 0.900 | 0.500 | 0.250 | 0.504 | 0.711 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 23.334 | 23.374 | 23.515 | 23.197 | 23.744 | 23.849 | 23.172 | 23.298 | 23.316 | 23.471 |
| 6h | 20.057 | 19.978 | 19.950 | 20.077 | 20.292 | 20.083 | 19.977 | 19.900 | 19.913 | 19.972 |
| 24h | 21.455 | 20.903 | 20.824 | 20.772 | 21.105 | 20.844 | 20.644 | 20.619 | 20.664 | 20.712 |
| 7d | 25.156 | 24.270 | 24.226 | 24.108 | 24.585 | 24.377 | 24.065 | 24.035 | 24.043 | 24.084 |
| 30d | 18.541 | 17.836 | 17.793 | 17.732 | 18.025 | 17.964 | 17.658 | 17.636 | 17.645 | 17.677 |

## Next candle

- candle starting 2026-11-19 02:02 UTC, last close 1774.9
- P(up) 0.5169, return quantiles (bp): {'05': -13.379, '10': -10.309, '25': -5.158, '40': -1.603, '50': 0.318, '60': 2.026, '75': 5.258, '90': 9.287, '95': 12.9}
- changepoint probability 0.0363, regime age 122.9 min
- agent weights: empirical 0.010, ewma 0.083, garch 0.124, har 0.126, bocpd 0.020, hmm 0.084, online_qr 0.247, lgbm 0.305

## Learning log

- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- HMM volatility states (sd, bp per minute): [5.82, 10.34, 24.91], current probabilities: [0.135, 0.843, 0.022]
- live generator: {'versions': 60, 'latest_effective': '2026-11-19 02:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.358, 'l_abs': 0.727, 'l_hi': 0.805, 'l_lo': 0.72, 'b05': 0.729, 'b25': 0.731, 'b75': 0.684, 'b95': 0.719}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.776, 1.715, 2.375, 2.77, 2.539, 3.161, 3.596, 3.672, 4.286, 5.285, 3.859, 3.642, 4.102, 4.428]}
- calibration offsets (in sigma): {'05': 0.0305, '10': 0.011, '25': 0.0225, '40': 0.044, '50': 0.045, '60': 0.016, '75': 0.0075, '90': -0.071, '95': -0.0505}
