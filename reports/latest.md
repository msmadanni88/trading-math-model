# ETH-USD 60s candle generator - report

- generated: 2026-11-19 19:00 UTC
- last closed candle: 2026-11-19 19:00 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.528 (671) [0.498, 0.554] | 0.517 (2879) [0.500, 0.533] | 0.515 (7481) [0.504, 0.527] | 0.518 (4509) [0.503, 0.533] | 0.513 (76) | 0.500 | flat -0.004 (noise 0.027) |
| colour_clear | 0.582 (802) | 0.546 (5627) [0.535, 0.559] | 0.542 (23983) [0.536, 0.548] | 0.525 (61396) [0.519, 0.530] | 0.543 (37158) [0.538, 0.548] | 0.519 (671) | 0.500 | flat +0.000 (noise 0.011) |
| colour_confident | 0.619 (181) | 0.554 (1009) [0.529, 0.583] | 0.577 (4557) [0.565, 0.588] | 0.586 (6759) [0.576, 0.597] | 0.586 (6759) [0.576, 0.597] | 0.564 (133) | 0.500 | flat -0.013 (noise 0.023) |
| colour_next | 0.539 (1433) | 0.533 (10045) [0.527, 0.539] | 0.530 (42895) [0.526, 0.534] | 0.518 (111478) [0.515, 0.522] | 0.530 (67129) [0.527, 0.533] | 0.522 (1137) | 0.500 | flat +0.002 (noise 0.008) |
| colour_path | 0.506 (20062) | 0.502 (140630) [0.501, 0.504] | 0.502 (600530) [0.501, 0.503] | 0.501 (1560692) [0.500, 0.502] | 0.501 (939806) [0.500, 0.502] | 0.500 (15918) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.679 (56) | 0.590 (266) [0.553, 0.633] | 0.615 (1205) [0.597, 0.632] | 0.625 (1779) [0.609, 0.641] | 0.625 (1779) [0.609, 0.641] | 0.645 (31) | 0.500 | flat -0.038 (noise 0.043) |
| reversal_k13_next | 0.322 (87) | 0.311 (460) [0.278, 0.351] | 0.329 (1855) [0.312, 0.345] | 0.314 (5156) [0.305, 0.324] | 0.325 (3051) [0.313, 0.335] | 0.303 (66) | 0.077 | flat -0.021 (noise 0.030) |
| reversal_k13_now | 0.542 (59) | 0.570 (358) [0.522, 0.629] | 0.571 (1610) [0.550, 0.592] | 0.573 (4016) [0.561, 0.586] | 0.569 (2544) [0.552, 0.585] | 0.566 (53) | 0.077 | flat -0.007 (noise 0.037) |
| reversal_k3_next | 0.613 (62) | 0.602 (387) [0.576, 0.644] | 0.603 (2408) [0.590, 0.616] | 0.589 (6489) [0.581, 0.597] | 0.590 (4049) [0.580, 0.601] | 0.509 (55) | 0.293 | flat -0.025 (noise 0.036) |
| reversal_k3_now | 0.983 (57) | 0.944 (373) [0.930, 0.959] | 0.934 (1718) [0.925, 0.944] | 0.936 (4455) [0.930, 0.941] | 0.932 (2692) [0.925, 0.940] | 0.895 (57) | 0.293 | flat +0.024 (noise 0.018) |
| reversal_k5_next | 0.436 (55) | 0.481 (445) [0.433, 0.534] | 0.498 (2242) [0.480, 0.516] | 0.485 (5902) [0.473, 0.496] | 0.480 (3912) [0.466, 0.494] | 0.395 (43) | 0.186 | flat -0.037 (noise 0.039) |
| reversal_k5_now | 0.772 (57) | 0.762 (433) [0.739, 0.787] | 0.794 (1725) [0.778, 0.809] | 0.816 (4238) [0.806, 0.826] | 0.803 (2627) [0.791, 0.815] | 0.862 (58) | 0.187 | flat -0.012 (noise 0.032) |
| reversal_k8_next | 0.391 (87) | 0.402 (488) [0.367, 0.447] | 0.407 (2399) [0.393, 0.422] | 0.397 (6060) [0.386, 0.406] | 0.397 (3954) [0.385, 0.409] | 0.420 (69) | 0.121 | flat -0.021 (noise 0.032) |
| reversal_k8_now | 0.692 (65) | 0.649 (393) [0.612, 0.697] | 0.680 (1588) [0.660, 0.701] | 0.695 (4088) [0.682, 0.708] | 0.683 (2501) [0.667, 0.699] | 0.712 (59) | 0.122 | flat -0.046 (noise 0.034) |
| overall | 0.510 (22120) | 0.506 (154683) [0.505, 0.508] | 0.506 (661849) [0.505, 0.507] | 0.504 (1720055) [0.503, 0.505] | 0.505 (1036774) [0.504, 0.506] | 0.503 (17591) | - | flat +0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06905, 0.09993] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5313, 'levels': [{'threshold': 0.06905, 'calls_per_day': 145.7, 'win_rate': 0.5484}, {'threshold': 0.09993, 'calls_per_day': 36.7, 'win_rate': 0.6085}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42892, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15260 | 0.349 | 0.533 (15045) | 0.570 (2302) | 0.749 (2554) |
| volatility: normal | 15260 | 0.375 | 0.530 (15203) | 0.600 (1412) | 0.737 (2359) |
| volatility: wild | 15260 | 0.390 | 0.529 (15220) | 0.575 (1128) | 0.759 (2174) |
| session: Asia 00-08 | 15360 | 0.371 | 0.534 (15248) | 0.576 (1668) | 0.745 (2299) |
| session: Europe 08-13 | 9600 | 0.365 | 0.531 (9523) | 0.592 (1192) | 0.753 (1549) |
| session: US 13-21 | 15240 | 0.379 | 0.533 (15150) | 0.596 (1342) | 0.750 (2385) |
| session: late 21-24 | 5580 | 0.364 | 0.515 (5547) | 0.531 (640) | 0.741 (854) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.360 | 0.386 | 0.286 | 0.286 | 0.475 | 0.181 | 0.540 | 1.413 |
| 6h | 360 | 0.390 | 0.402 | 0.298 | 0.332 | 0.535 | 0.256 | 0.524 | 1.106 |
| 24h | 1440 | 0.383 | 0.382 | 0.302 | 0.340 | 0.521 | 0.258 | 0.507 | 1.187 |
| 7d | 10080 | 0.386 | 0.377 | 0.301 | 0.335 | 0.531 | 0.270 | 0.501 | 1.154 |
| 30d | 43200 | 0.371 | 0.364 | 0.284 | 0.316 | 0.530 | 0.265 | 0.477 | 1.256 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.360 / 0.475 / 0.917; 2: 0.400 / 0.525 / 0.867; 3: 0.375 / 0.508 / 0.983; 4: 0.404 / 0.492 / 0.917; 5: 0.375 / 0.559 / 0.883; 6: 0.401 / 0.559 / 0.950; 7: 0.365 / 0.390 / 0.817; 8: 0.391 / 0.525 / 0.817; 9: 0.384 / 0.508 / 0.817; 10: 0.399 / 0.525 / 0.717; 11: 0.372 / 0.407 / 0.700; 12: 0.378 / 0.576 / 0.867; 13: 0.373 / 0.508 / 0.883; 14: 0.378 / 0.458 / 0.867; 15: 0.404 / 0.559 / 0.867
- 6h: 1: 0.390 / 0.535 / 0.875; 2: 0.384 / 0.493 / 0.786; 3: 0.379 / 0.496 / 0.939; 4: 0.376 / 0.462 / 0.847; 5: 0.392 / 0.538 / 0.825; 6: 0.388 / 0.526 / 0.878; 7: 0.382 / 0.496 / 0.794; 8: 0.387 / 0.513 / 0.800; 9: 0.385 / 0.524 / 0.806; 10: 0.379 / 0.510 / 0.756; 11: 0.369 / 0.465 / 0.731; 12: 0.379 / 0.510 / 0.853; 13: 0.384 / 0.526 / 0.864; 14: 0.372 / 0.482 / 0.833; 15: 0.382 / 0.515 / 0.850
- 24h: 1: 0.383 / 0.521 / 0.900; 2: 0.377 / 0.494 / 0.870; 3: 0.371 / 0.485 / 0.908; 4: 0.373 / 0.491 / 0.883; 5: 0.379 / 0.513 / 0.879; 6: 0.375 / 0.504 / 0.897; 7: 0.377 / 0.498 / 0.874; 8: 0.376 / 0.519 / 0.869; 9: 0.372 / 0.502 / 0.878; 10: 0.371 / 0.498 / 0.856; 11: 0.372 / 0.501 / 0.850; 12: 0.370 / 0.487 / 0.893; 13: 0.375 / 0.506 / 0.899; 14: 0.374 / 0.514 / 0.890; 15: 0.368 / 0.485 / 0.892
- 7d: 1: 0.386 / 0.531 / 0.898; 2: 0.372 / 0.490 / 0.896; 3: 0.377 / 0.512 / 0.901; 4: 0.371 / 0.491 / 0.898; 5: 0.374 / 0.504 / 0.896; 6: 0.372 / 0.503 / 0.898; 7: 0.373 / 0.506 / 0.895; 8: 0.374 / 0.513 / 0.895; 9: 0.366 / 0.489 / 0.895; 10: 0.372 / 0.507 / 0.894; 11: 0.371 / 0.506 / 0.895; 12: 0.371 / 0.503 / 0.900; 13: 0.369 / 0.500 / 0.900; 14: 0.369 / 0.502 / 0.899; 15: 0.367 / 0.496 / 0.900
- 30d: 1: 0.371 / 0.530 / 0.897; 2: 0.358 / 0.492 / 0.899; 3: 0.362 / 0.512 / 0.900; 4: 0.358 / 0.497 / 0.900; 5: 0.359 / 0.505 / 0.899; 6: 0.356 / 0.501 / 0.900; 7: 0.357 / 0.501 / 0.899; 8: 0.358 / 0.507 / 0.899; 9: 0.356 / 0.501 / 0.899; 10: 0.356 / 0.502 / 0.898; 11: 0.356 / 0.504 / 0.898; 12: 0.356 / 0.503 / 0.899; 13: 0.355 / 0.500 / 0.900; 14: 0.355 / 0.502 / 0.899; 15: 0.355 / 0.501 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.105 (body 0.056, range 0.153); 'price stays where it was' would score 0.177; colour right 0.576; typical miss of the close 17.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.146 (body 0.088, range 0.204); 'price stays where it was' would score 0.160; colour right 0.535; typical miss of the close 17.3 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.133 (body 0.082, range 0.184); 'price stays where it was' would score 0.151; colour right 0.500; typical miss of the close 13.0 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.128 (body 0.083, range 0.172); 'price stays where it was' would score 0.132; colour right 0.504; typical miss of the close 14.5 bp; chain ended on the right side 0.526 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.9 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.2; 2: 0.205 / 6.0; 3: 0.168 / 7.7; 4: 0.135 / 8.1; 5: 0.126 / 8.8; 6: 0.120 / 9.6; 7: 0.112 / 10.1; 8: 0.100 / 11.1; 9: 0.093 / 11.3; 10: 0.090 / 11.8; 11: 0.086 / 12.1; 12: 0.079 / 12.5; 13: 0.074 / 13.1; 14: 0.068 / 13.5; 15: 0.067 / 14.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 156414, probability skill vs chance 0.23, widened contest next: True
  - now: threshold 0.8317, hit rate recent 0.9153 / long run 0.9311
    - 6h: 22 calls (89 a day), hit rate 0.864, chance 0.279, naive rule 0.462, lift 3.10x
    - 24h: 70 calls (70 a day), hit rate 0.900, chance 0.294, naive rule 0.497, lift 3.06x
    - 7d: 381 calls (54 a day), hit rate 0.940, chance 0.288, naive rule 0.500, lift 3.26x
    - 30d: 1729 calls (58 a day), hit rate 0.933, chance 0.294, naive rule 0.501, lift 3.18x
  - next: threshold 0.5301, hit rate recent 0.5207 / long run 0.596
    - 6h: 24 calls (97 a day), hit rate 0.417, chance 0.279, lift 1.49x
    - 24h: 60 calls (60 a day), hit rate 0.500, chance 0.294, lift 1.70x
    - 7d: 393 calls (56 a day), hit rate 0.598, chance 0.288, lift 2.07x
    - 30d: 2365 calls (79 a day), hit rate 0.603, chance 0.294, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.502; 0.35: 530, 0.526; 0.40: 477, 0.576; 0.45: 411, 0.644; 0.50: 361, 0.689; 0.55: 313, 0.735; 0.60: 263, 0.782; 0.65: 222, 0.810; 0.70: 174, 0.841; 0.75: 140, 0.873; 0.80: 92, 0.906; 0.85: 45, 0.942; 0.90: 4, 0.967
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.434; 0.35: 491, 0.467; 0.40: 390, 0.508; 0.45: 293, 0.544; 0.50: 187, 0.576; 0.55: 82, 0.585; 0.60: 11, 0.634; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 156412, probability skill vs chance 0.2098, widened contest next: True
  - now: threshold 0.7003, hit rate recent 0.8355 / long run 0.7868
    - 6h: 21 calls (86 a day), hit rate 0.857, chance 0.191, naive rule 0.375, lift 4.48x
    - 24h: 69 calls (69 a day), hit rate 0.870, chance 0.196, naive rule 0.410, lift 4.44x
    - 7d: 450 calls (64 a day), hit rate 0.782, chance 0.187, naive rule 0.412, lift 4.19x
    - 30d: 1740 calls (58 a day), hit rate 0.795, chance 0.186, naive rule 0.409, lift 4.27x
  - next: threshold 0.4623, hit rate recent 0.4008 / long run 0.4837
    - 6h: 21 calls (86 a day), hit rate 0.286, chance 0.191, lift 1.49x
    - 24h: 49 calls (49 a day), hit rate 0.408, chance 0.196, lift 2.09x
    - 7d: 434 calls (62 a day), hit rate 0.482, chance 0.187, lift 2.58x
    - 30d: 2180 calls (73 a day), hit rate 0.501, chance 0.186, lift 2.69x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 361, 0.473; 0.40: 293, 0.542; 0.45: 237, 0.602; 0.50: 187, 0.653; 0.55: 150, 0.687; 0.60: 114, 0.735; 0.65: 80, 0.772; 0.70: 49, 0.807; 0.75: 28, 0.840; 0.80: 7, 0.865
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 252, 0.428; 0.40: 161, 0.459; 0.45: 65, 0.498; 0.50: 8, 0.553; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 156409, probability skill vs chance 0.2016, widened contest next: False
  - now: threshold 0.5758, hit rate recent 0.6927 / long run 0.6758
    - 6h: 25 calls (103 a day), hit rate 0.640, chance 0.111, naive rule 0.291, lift 5.74x
    - 24h: 72 calls (73 a day), hit rate 0.722, chance 0.125, naive rule 0.344, lift 5.79x
    - 7d: 419 calls (60 a day), hit rate 0.663, chance 0.122, naive rule 0.346, lift 5.44x
    - 30d: 1613 calls (54 a day), hit rate 0.682, chance 0.121, naive rule 0.341, lift 5.62x
  - next: threshold 0.3661, hit rate recent 0.3892 / long run 0.408
    - 6h: 32 calls (132 a day), hit rate 0.312, chance 0.111, lift 2.80x
    - 24h: 81 calls (82 a day), hit rate 0.407, chance 0.125, lift 3.26x
    - 7d: 503 calls (72 a day), hit rate 0.404, chance 0.122, lift 3.31x
    - 30d: 2380 calls (79 a day), hit rate 0.408, chance 0.121, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 253, 0.425; 0.35: 197, 0.486; 0.40: 156, 0.534; 0.45: 119, 0.578; 0.50: 85, 0.635; 0.55: 60, 0.673; 0.60: 40, 0.713; 0.65: 23, 0.775; 0.70: 10, 0.827; 0.75: 2, 0.746
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 163, 0.371; 0.35: 85, 0.399; 0.40: 25, 0.431; 0.45: 5, 0.455; 0.50: 1, 0.731
- **K=13**: model 1794960000, labels learned 156404, probability skill vs chance 0.1762, widened contest next: False
  - now: threshold 0.4533, hit rate recent 0.5509 / long run 0.5695
    - 6h: 21 calls (88 a day), hit rate 0.524, chance 0.070, naive rule 0.227, lift 7.53x
    - 24h: 68 calls (69 a day), hit rate 0.559, chance 0.080, naive rule 0.281, lift 7.02x
    - 7d: 380 calls (54 a day), hit rate 0.571, chance 0.080, naive rule 0.299, lift 7.15x
    - 30d: 1619 calls (54 a day), hit rate 0.572, chance 0.078, naive rule 0.289, lift 7.31x
  - next: threshold 0.283, hit rate recent 0.3005 / long run 0.3193
    - 6h: 25 calls (104 a day), hit rate 0.280, chance 0.070, lift 4.03x
    - 24h: 80 calls (81 a day), hit rate 0.287, chance 0.080, lift 3.61x
    - 7d: 473 calls (68 a day), hit rate 0.311, chance 0.080, lift 3.89x
    - 30d: 1863 calls (62 a day), hit rate 0.326, chance 0.078, lift 4.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 138, 0.425; 0.35: 100, 0.474; 0.40: 70, 0.534; 0.45: 48, 0.584; 0.50: 34, 0.625; 0.55: 21, 0.645; 0.60: 11, 0.681; 0.65: 3, 0.608; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 53, 0.334; 0.35: 14, 0.343; 0.40: 2, 0.408; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 23.859 | 1.42% | 0.933 | 0.567 | 0.246 | 0.593 | 0.214 |
| 6h | 29.328 | 5.80% | 0.878 | 0.467 | 0.249 | 0.557 | 0.608 |
| 24h | 20.385 | 2.93% | 0.897 | 0.495 | 0.250 | 0.506 | 0.636 |
| 7d | 24.178 | 4.10% | 0.899 | 0.499 | 0.250 | 0.500 | 0.670 |
| 30d | 17.717 | 4.68% | 0.900 | 0.500 | 0.250 | 0.504 | 0.712 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 24.203 | 23.853 | 23.905 | 24.061 | 24.411 | 23.990 | 23.698 | 23.843 | 23.783 | 23.859 |
| 6h | 31.135 | 29.483 | 29.561 | 29.426 | 29.687 | 29.676 | 29.286 | 29.357 | 29.303 | 29.328 |
| 24h | 21.000 | 20.454 | 20.476 | 20.439 | 20.699 | 20.633 | 20.352 | 20.371 | 20.357 | 20.385 |
| 7d | 25.212 | 24.342 | 24.309 | 24.200 | 24.652 | 24.457 | 24.158 | 24.134 | 24.138 | 24.178 |
| 30d | 18.587 | 17.877 | 17.836 | 17.773 | 18.068 | 18.007 | 17.696 | 17.677 | 17.685 | 17.717 |

## Next candle

- candle starting 2026-11-19 19:00 UTC, last close 1775.74
- P(up) 0.458, return quantiles (bp): {'05': -17.03, '10': -13.373, '25': -8.15, '40': -3.556, '50': -1.092, '60': 1.546, '75': 5.936, '90': 12.6, '95': 16.818}
- changepoint probability 0.0579, regime age 44.9 min
- agent weights: empirical 0.003, ewma 0.117, garch 0.093, har 0.166, bocpd 0.030, hmm 0.042, online_qr 0.304, lgbm 0.246

## Learning log

- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- HMM volatility states (sd, bp per minute): [5.66, 9.9, 23.56], current probabilities: [0.79, 0.207, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-11-19 19:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.544, 'l_abs': 0.702, 'l_hi': 0.774, 'l_lo': 0.707, 'b05': 0.706, 'b25': 0.667, 'b75': 0.705, 'b95': 0.679}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [3.315, 1.497, 3.156, 4.494, 3.373, 7.352, 7.719, 7.726, 11.933, 15.013, 6.138, 5.565, 7.356, 6.767]}
- calibration offsets (in sigma): {'05': 0.0795, '10': -0.001, '25': -0.0825, '40': -0.044, '50': -0.075, '60': -0.066, '75': -0.0375, '90': 0.041, '95': 0.0605}
