# ETH-USD 60s candle generator - report

- generated: 2026-11-20 17:15 UTC
- last closed candle: 2026-11-20 17:15 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.525 (672) [0.495, 0.552] | 0.517 (2879) [0.502, 0.534] | 0.515 (7577) [0.505, 0.526] | 0.518 (4605) [0.503, 0.532] | 0.580 (69) | 0.500 | flat -0.002 (noise 0.027) |
| colour_clear | 0.537 (831) | 0.546 (5673) [0.536, 0.558] | 0.540 (23966) [0.534, 0.546] | 0.525 (62227) [0.520, 0.530] | 0.543 (37989) [0.539, 0.547] | 0.577 (605) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | 0.576 (151) | 0.556 (1085) [0.531, 0.583] | 0.577 (4499) [0.565, 0.589] | 0.586 (6910) [0.576, 0.596] | 0.586 (6910) [0.576, 0.596] | 0.568 (88) | 0.500 | flat -0.013 (noise 0.023) |
| colour_next | 0.535 (1436) | 0.533 (10046) [0.527, 0.539] | 0.530 (42892) [0.526, 0.534] | 0.518 (112914) [0.515, 0.522] | 0.530 (68565) [0.527, 0.533] | 0.539 (1035) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.499 (20104) | 0.502 (140644) [0.500, 0.504] | 0.502 (600488) [0.501, 0.503] | 0.501 (1580796) [0.500, 0.502] | 0.501 (959910) [0.500, 0.502] | 0.510 (14490) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.676 (34) | 0.606 (289) [0.570, 0.650] | 0.613 (1184) [0.596, 0.629] | 0.625 (1813) [0.610, 0.641] | 0.625 (1813) [0.610, 0.641] | 0.615 (13) | 0.500 | flat -0.017 (noise 0.042) |
| reversal_k13_next | 0.275 (91) | 0.300 (487) [0.271, 0.339] | 0.325 (1870) [0.309, 0.343] | 0.314 (5247) [0.304, 0.323] | 0.323 (3142) [0.312, 0.334] | 0.356 (45) | 0.077 | flat -0.035 (noise 0.030) |
| reversal_k13_now | 0.515 (68) | 0.560 (384) [0.513, 0.618] | 0.570 (1627) [0.549, 0.592] | 0.572 (4084) [0.560, 0.584] | 0.567 (2612) [0.551, 0.584] | 0.576 (33) | 0.077 | flat -0.019 (noise 0.037) |
| reversal_k3_next | 0.544 (79) | 0.595 (407) [0.567, 0.637] | 0.604 (2365) [0.593, 0.617] | 0.589 (6568) [0.580, 0.597] | 0.589 (4128) [0.579, 0.600] | 0.535 (114) | 0.293 | flat -0.014 (noise 0.035) |
| reversal_k3_now | 0.894 (66) | 0.941 (375) [0.924, 0.959] | 0.933 (1727) [0.924, 0.944] | 0.935 (4521) [0.930, 0.941] | 0.931 (2758) [0.924, 0.939] | 0.915 (47) | 0.293 | flat +0.023 (noise 0.018) |
| reversal_k5_next | 0.407 (54) | 0.475 (425) [0.422, 0.534] | 0.503 (2167) [0.488, 0.518] | 0.484 (5956) [0.473, 0.495] | 0.479 (3966) [0.465, 0.492] | 0.514 (35) | 0.187 | flat -0.024 (noise 0.039) |
| reversal_k5_now | 0.831 (65) | 0.775 (441) [0.748, 0.803] | 0.794 (1740) [0.777, 0.809] | 0.816 (4303) [0.806, 0.826] | 0.804 (2692) [0.792, 0.816] | 0.787 (47) | 0.187 | flat +0.015 (noise 0.032) |
| reversal_k8_next | 0.405 (89) | 0.395 (511) [0.365, 0.440] | 0.409 (2379) [0.394, 0.424] | 0.397 (6149) [0.387, 0.406] | 0.397 (4043) [0.385, 0.408] | 0.393 (61) | 0.121 | flat -0.024 (noise 0.031) |
| reversal_k8_now | 0.690 (71) | 0.659 (419) [0.617, 0.705] | 0.682 (1617) [0.663, 0.702] | 0.695 (4159) [0.683, 0.707] | 0.683 (2572) [0.668, 0.699] | 0.682 (44) | 0.122 | flat -0.024 (noise 0.034) |
| overall | 0.503 (22219) | 0.506 (154811) [0.504, 0.507] | 0.506 (661751) [0.505, 0.507] | 0.504 (1742274) [0.503, 0.505] | 0.505 (1058993) [0.504, 0.506] | 0.514 (16020) | - | flat +0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06934, 0.1] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.534, 'levels': [{'threshold': 0.06934, 'calls_per_day': 144.6, 'win_rate': 0.5557}, {'threshold': 0.1, 'calls_per_day': 35.9, 'win_rate': 0.619}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42895, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15225 | 0.349 | 0.533 (15010) | 0.567 (2279) | 0.752 (2529) |
| volatility: normal | 15225 | 0.377 | 0.528 (15168) | 0.594 (1408) | 0.736 (2393) |
| volatility: wild | 15225 | 0.391 | 0.531 (15188) | 0.577 (1109) | 0.758 (2160) |
| session: Asia 00-08 | 15360 | 0.371 | 0.533 (15250) | 0.571 (1652) | 0.748 (2303) |
| session: Europe 08-13 | 9600 | 0.366 | 0.531 (9524) | 0.585 (1192) | 0.757 (1563) |
| session: US 13-21 | 15135 | 0.380 | 0.533 (15046) | 0.597 (1335) | 0.744 (2394) |
| session: late 21-24 | 5580 | 0.366 | 0.518 (5546) | 0.535 (617) | 0.746 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.421 | 0.408 | 0.321 | 0.321 | 0.550 | 0.283 | 0.559 | 1.483 |
| 6h | 360 | 0.411 | 0.394 | 0.318 | 0.345 | 0.556 | 0.291 | 0.530 | 1.182 |
| 24h | 1440 | 0.396 | 0.387 | 0.308 | 0.349 | 0.545 | 0.275 | 0.518 | 1.185 |
| 7d | 10080 | 0.388 | 0.378 | 0.302 | 0.338 | 0.535 | 0.271 | 0.504 | 1.173 |
| 30d | 43200 | 0.372 | 0.365 | 0.285 | 0.317 | 0.530 | 0.266 | 0.478 | 1.261 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.421 / 0.550 / 0.917; 2: 0.367 / 0.500 / 0.867; 3: 0.416 / 0.567 / 0.833; 4: 0.360 / 0.417 / 0.917; 5: 0.366 / 0.450 / 0.950; 6: 0.329 / 0.350 / 0.950; 7: 0.377 / 0.533 / 0.933; 8: 0.373 / 0.483 / 0.917; 9: 0.390 / 0.517 / 0.917; 10: 0.368 / 0.467 / 0.950; 11: 0.363 / 0.517 / 0.983; 12: 0.397 / 0.517 / 1.000; 13: 0.400 / 0.533 / 1.000; 14: 0.365 / 0.517 / 0.983; 15: 0.381 / 0.483 / 1.000
- 6h: 1: 0.411 / 0.556 / 0.872; 2: 0.384 / 0.481 / 0.800; 3: 0.393 / 0.542 / 0.736; 4: 0.381 / 0.483 / 0.842; 5: 0.394 / 0.528 / 0.850; 6: 0.382 / 0.492 / 0.892; 7: 0.375 / 0.486 / 0.797; 8: 0.379 / 0.483 / 0.775; 9: 0.374 / 0.481 / 0.794; 10: 0.389 / 0.533 / 0.792; 11: 0.367 / 0.483 / 0.828; 12: 0.399 / 0.553 / 0.875; 13: 0.397 / 0.564 / 0.894; 14: 0.373 / 0.497 / 0.847; 15: 0.380 / 0.508 / 0.872
- 24h: 1: 0.396 / 0.545 / 0.897; 2: 0.385 / 0.518 / 0.899; 3: 0.381 / 0.504 / 0.853; 4: 0.386 / 0.501 / 0.896; 5: 0.390 / 0.535 / 0.907; 6: 0.384 / 0.503 / 0.911; 7: 0.378 / 0.487 / 0.902; 8: 0.381 / 0.505 / 0.896; 9: 0.381 / 0.503 / 0.899; 10: 0.383 / 0.517 / 0.910; 11: 0.379 / 0.503 / 0.925; 12: 0.379 / 0.504 / 0.907; 13: 0.382 / 0.520 / 0.901; 14: 0.373 / 0.483 / 0.904; 15: 0.380 / 0.501 / 0.901
- 7d: 1: 0.388 / 0.535 / 0.899; 2: 0.374 / 0.494 / 0.899; 3: 0.378 / 0.513 / 0.897; 4: 0.373 / 0.492 / 0.899; 5: 0.376 / 0.509 / 0.900; 6: 0.374 / 0.503 / 0.901; 7: 0.374 / 0.505 / 0.898; 8: 0.375 / 0.513 / 0.898; 9: 0.369 / 0.492 / 0.897; 10: 0.374 / 0.510 / 0.898; 11: 0.372 / 0.504 / 0.899; 12: 0.373 / 0.505 / 0.899; 13: 0.371 / 0.504 / 0.899; 14: 0.371 / 0.502 / 0.898; 15: 0.369 / 0.497 / 0.899
- 30d: 1: 0.372 / 0.530 / 0.897; 2: 0.359 / 0.493 / 0.899; 3: 0.363 / 0.512 / 0.898; 4: 0.358 / 0.497 / 0.899; 5: 0.360 / 0.506 / 0.899; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.500 / 0.899; 8: 0.358 / 0.507 / 0.899; 9: 0.357 / 0.501 / 0.899; 10: 0.357 / 0.502 / 0.899; 11: 0.357 / 0.504 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.501 / 0.900; 14: 0.356 / 0.501 / 0.900; 15: 0.355 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.142 (body 0.078, range 0.207); 'price stays where it was' would score 0.171; colour right 0.383; typical miss of the close 29.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.143 (body 0.091, range 0.196); 'price stays where it was' would score 0.152; colour right 0.528; typical miss of the close 22.3 bp; chain ended on the right side 0.708 of 24 chains; n=360
- 24h: match 0.133 (body 0.084, range 0.183); 'price stays where it was' would score 0.149; colour right 0.517; typical miss of the close 17.9 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.129 (body 0.083, range 0.174); 'price stays where it was' would score 0.134; colour right 0.506; typical miss of the close 15.0 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 10.1 bp; chain ended on the right side 0.517 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.4; 2: 0.205 / 6.0; 3: 0.167 / 7.9; 4: 0.135 / 8.2; 5: 0.127 / 8.9; 6: 0.120 / 9.7; 7: 0.114 / 10.3; 8: 0.100 / 11.3; 9: 0.093 / 11.5; 10: 0.089 / 12.2; 11: 0.086 / 12.6; 12: 0.078 / 12.8; 13: 0.073 / 13.4; 14: 0.067 / 13.8; 15: 0.066 / 14.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 157749, probability skill vs chance 0.2298, widened contest next: True
  - now: threshold 0.8314, hit rate recent 0.9103 / long run 0.9292
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.292, naive rule 0.452, lift 3.00x
    - 24h: 61 calls (61 a day), hit rate 0.902, chance 0.289, naive rule 0.482, lift 3.12x
    - 7d: 377 calls (54 a day), hit rate 0.936, chance 0.290, naive rule 0.500, lift 3.23x
    - 30d: 1729 calls (58 a day), hit rate 0.932, chance 0.293, naive rule 0.499, lift 3.18x
  - next: threshold 0.5094, hit rate recent 0.5229 / long run 0.5862
    - 6h: 45 calls (183 a day), hit rate 0.511, chance 0.292, lift 1.75x
    - 24h: 141 calls (141 a day), hit rate 0.546, chance 0.289, lift 1.89x
    - 7d: 492 calls (70 a day), hit rate 0.577, chance 0.290, lift 1.99x
    - 30d: 2373 calls (79 a day), hit rate 0.597, chance 0.293, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.501; 0.35: 530, 0.526; 0.40: 477, 0.575; 0.45: 412, 0.641; 0.50: 363, 0.686; 0.55: 314, 0.732; 0.60: 265, 0.779; 0.65: 223, 0.807; 0.70: 175, 0.839; 0.75: 141, 0.871; 0.80: 93, 0.903; 0.85: 44, 0.940; 0.90: 4, 0.967
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 490, 0.468; 0.40: 389, 0.508; 0.45: 293, 0.543; 0.50: 187, 0.574; 0.55: 81, 0.583; 0.60: 11, 0.636; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 157747, probability skill vs chance 0.2104, widened contest next: True
  - now: threshold 0.6996, hit rate recent 0.7721 / long run 0.7842
    - 6h: 21 calls (86 a day), hit rate 0.571, chance 0.180, naive rule 0.367, lift 3.18x
    - 24h: 60 calls (60 a day), hit rate 0.767, chance 0.187, naive rule 0.399, lift 4.11x
    - 7d: 435 calls (62 a day), hit rate 0.784, chance 0.188, naive rule 0.414, lift 4.17x
    - 30d: 1748 calls (58 a day), hit rate 0.793, chance 0.186, naive rule 0.409, lift 4.26x
  - next: threshold 0.4629, hit rate recent 0.4542 / long run 0.4849
    - 6h: 15 calls (61 a day), hit rate 0.467, chance 0.180, lift 2.59x
    - 24h: 51 calls (51 a day), hit rate 0.490, chance 0.187, lift 2.63x
    - 7d: 410 calls (59 a day), hit rate 0.468, chance 0.188, lift 2.49x
    - 30d: 2108 calls (70 a day), hit rate 0.503, chance 0.186, lift 2.70x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 362, 0.473; 0.40: 294, 0.541; 0.45: 238, 0.601; 0.50: 187, 0.652; 0.55: 150, 0.686; 0.60: 114, 0.732; 0.65: 81, 0.769; 0.70: 50, 0.805; 0.75: 27, 0.840; 0.80: 7, 0.861
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.390; 0.35: 252, 0.428; 0.40: 161, 0.459; 0.45: 65, 0.496; 0.50: 8, 0.554; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 157744, probability skill vs chance 0.2066, widened contest next: False
  - now: threshold 0.5759, hit rate recent 0.659 / long run 0.6743
    - 6h: 20 calls (82 a day), hit rate 0.500, chance 0.129, naive rule 0.348, lift 3.89x
    - 24h: 62 calls (62 a day), hit rate 0.661, chance 0.120, naive rule 0.335, lift 5.53x
    - 7d: 415 calls (59 a day), hit rate 0.665, chance 0.122, naive rule 0.346, lift 5.47x
    - 30d: 1623 calls (54 a day), hit rate 0.681, chance 0.122, naive rule 0.342, lift 5.60x
  - next: threshold 0.3511, hit rate recent 0.394 / long run 0.4049
    - 6h: 30 calls (123 a day), hit rate 0.433, chance 0.129, lift 3.37x
    - 24h: 93 calls (94 a day), hit rate 0.376, chance 0.120, lift 3.15x
    - 7d: 536 calls (77 a day), hit rate 0.396, chance 0.122, lift 3.25x
    - 30d: 2357 calls (79 a day), hit rate 0.408, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 253, 0.425; 0.35: 198, 0.485; 0.40: 157, 0.534; 0.45: 120, 0.578; 0.50: 85, 0.634; 0.55: 61, 0.672; 0.60: 41, 0.713; 0.65: 23, 0.772; 0.70: 10, 0.818; 0.75: 2, 0.740
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 162, 0.372; 0.35: 84, 0.399; 0.40: 26, 0.430; 0.45: 6, 0.457; 0.50: 1, 0.704
- **K=13**: model 1795132800, labels learned 157739, probability skill vs chance 0.1791, widened contest next: True
  - now: threshold 0.453, hit rate recent 0.5211 / long run 0.5641
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.083, naive rule 0.292, lift 4.04x
    - 24h: 52 calls (53 a day), hit rate 0.500, chance 0.078, naive rule 0.267, lift 6.42x
    - 7d: 372 calls (53 a day), hit rate 0.567, chance 0.079, naive rule 0.294, lift 7.17x
    - 30d: 1626 calls (54 a day), hit rate 0.570, chance 0.078, naive rule 0.289, lift 7.26x
  - next: threshold 0.3039, hit rate recent 0.3192 / long run 0.3175
    - 6h: 15 calls (63 a day), hit rate 0.400, chance 0.083, lift 4.84x
    - 24h: 79 calls (80 a day), hit rate 0.316, chance 0.078, lift 4.06x
    - 7d: 498 calls (71 a day), hit rate 0.305, chance 0.079, lift 3.86x
    - 30d: 1866 calls (62 a day), hit rate 0.325, chance 0.078, lift 4.14x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 139, 0.423; 0.35: 101, 0.472; 0.40: 70, 0.531; 0.45: 48, 0.581; 0.50: 34, 0.621; 0.55: 21, 0.644; 0.60: 10, 0.685; 0.65: 2, 0.595; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 53, 0.334; 0.35: 14, 0.360; 0.40: 2, 0.425; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 45.672 | 4.96% | 0.900 | 0.583 | 0.250 | 0.517 | 0.214 |
| 6h | 40.280 | 6.89% | 0.875 | 0.489 | 0.250 | 0.517 | 0.702 |
| 24h | 28.777 | 3.53% | 0.894 | 0.501 | 0.250 | 0.519 | 0.684 |
| 7d | 24.846 | 3.95% | 0.899 | 0.500 | 0.250 | 0.500 | 0.678 |
| 30d | 18.140 | 4.65% | 0.900 | 0.500 | 0.250 | 0.505 | 0.717 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 48.056 | 46.474 | 46.052 | 46.089 | 46.813 | 46.014 | 45.626 | 45.343 | 45.683 | 45.672 |
| 6h | 43.260 | 40.816 | 40.723 | 40.215 | 40.835 | 40.833 | 40.501 | 40.289 | 40.332 | 40.280 |
| 24h | 29.831 | 28.920 | 28.890 | 28.801 | 29.161 | 29.030 | 28.801 | 28.765 | 28.746 | 28.777 |
| 7d | 25.868 | 25.004 | 24.980 | 24.863 | 25.320 | 25.117 | 24.826 | 24.802 | 24.806 | 24.846 |
| 30d | 19.025 | 18.302 | 18.262 | 18.194 | 18.495 | 18.435 | 18.122 | 18.102 | 18.109 | 18.140 |

## Next candle

- candle starting 2026-11-20 17:15 UTC, last close 1627.93
- P(up) 0.4734, return quantiles (bp): {'05': -33.292, '10': -25.662, '25': -14.735, '40': -6.499, '50': -1.168, '60': 3.299, '75': 11.73, '90': 23.739, '95': 33.419}
- changepoint probability 0.0227, regime age 120.9 min
- agent weights: empirical 0.003, ewma 0.069, garch 0.085, har 0.298, bocpd 0.038, hmm 0.043, online_qr 0.166, lgbm 0.298

## Learning log

- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- HMM volatility states (sd, bp per minute): [5.82, 9.8, 20.43], current probabilities: [0.003, 0.201, 0.796]
- live generator: {'versions': 60, 'latest_effective': '2026-11-20 17:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.302, 'l_abs': 0.688, 'l_hi': 0.814, 'l_lo': 0.723, 'b05': 0.733, 'b25': 0.653, 'b75': 0.682, 'b95': 0.742}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.5, 1.6], [1.5, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [3.03, 6.51, 3.384, 3.431, 2.524, 5.726, 7.197, 6.389, 5.985, 4.754, 4.24, 4.602, 5.504, 5.485]}
- calibration offsets (in sigma): {'05': -0.043, '10': -0.056, '25': -0.095, '40': -0.084, '50': -0.06, '60': -0.066, '75': -0.035, '90': -0.034, '95': 0.053}
