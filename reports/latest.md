# ETH-USD 60s candle generator - report

- generated: 2026-11-20 01:11 UTC
- last closed candle: 2026-11-20 01:11 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.525 (672) [0.495, 0.552] | 0.517 (2879) [0.502, 0.534] | 0.515 (7577) [0.505, 0.526] | 0.518 (4605) [0.503, 0.532] | 0.500 (4) | 0.500 | flat -0.002 (noise 0.027) |
| colour_clear | 0.537 (831) | 0.546 (5673) [0.536, 0.558] | 0.540 (23966) [0.534, 0.546] | 0.525 (62227) [0.520, 0.530] | 0.543 (37989) [0.539, 0.547] | 0.596 (52) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | 0.576 (151) | 0.556 (1085) [0.531, 0.583] | 0.577 (4499) [0.565, 0.589] | 0.586 (6910) [0.576, 0.596] | 0.586 (6910) [0.576, 0.596] | 0.714 (7) | 0.500 | flat -0.013 (noise 0.023) |
| colour_next | 0.535 (1436) | 0.533 (10046) [0.527, 0.539] | 0.530 (42892) [0.526, 0.534] | 0.518 (112914) [0.515, 0.522] | 0.530 (68565) [0.527, 0.533] | 0.549 (71) | 0.500 | flat +0.000 (noise 0.008) |
| colour_path | 0.499 (20104) | 0.502 (140644) [0.500, 0.504] | 0.502 (600488) [0.501, 0.503] | 0.501 (1580796) [0.500, 0.502] | 0.501 (959910) [0.500, 0.502] | 0.530 (994) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.676 (34) | 0.606 (289) [0.570, 0.650] | 0.613 (1184) [0.596, 0.629] | 0.625 (1813) [0.610, 0.641] | 0.625 (1813) [0.610, 0.641] | 0.000 (1) | 0.500 | flat -0.017 (noise 0.042) |
| reversal_k13_next | 0.275 (91) | 0.300 (487) [0.271, 0.339] | 0.325 (1870) [0.309, 0.343] | 0.314 (5247) [0.304, 0.323] | 0.323 (3142) [0.312, 0.334] | 0.333 (3) | 0.077 | flat -0.035 (noise 0.030) |
| reversal_k13_now | 0.515 (68) | 0.560 (384) [0.513, 0.618] | 0.570 (1627) [0.549, 0.592] | 0.572 (4084) [0.560, 0.584] | 0.567 (2612) [0.551, 0.584] | 1.000 (2) | 0.077 | flat -0.019 (noise 0.037) |
| reversal_k3_next | 0.544 (79) | 0.595 (407) [0.567, 0.637] | 0.604 (2365) [0.593, 0.617] | 0.589 (6568) [0.580, 0.597] | 0.589 (4128) [0.579, 0.600] | 0.600 (10) | 0.293 | flat -0.014 (noise 0.035) |
| reversal_k3_now | 0.894 (66) | 0.941 (375) [0.924, 0.959] | 0.933 (1727) [0.924, 0.944] | 0.935 (4521) [0.930, 0.941] | 0.931 (2758) [0.924, 0.939] | 1.000 (7) | 0.293 | flat +0.023 (noise 0.018) |
| reversal_k5_next | 0.407 (54) | 0.475 (425) [0.422, 0.534] | 0.503 (2167) [0.488, 0.518] | 0.484 (5956) [0.473, 0.495] | 0.479 (3966) [0.465, 0.492] | 0.333 (3) | 0.187 | flat -0.024 (noise 0.039) |
| reversal_k5_now | 0.831 (65) | 0.775 (441) [0.748, 0.803] | 0.794 (1740) [0.777, 0.809] | 0.816 (4303) [0.806, 0.826] | 0.804 (2692) [0.792, 0.816] | 1.000 (4) | 0.187 | flat +0.015 (noise 0.032) |
| reversal_k8_next | 0.405 (89) | 0.395 (511) [0.365, 0.440] | 0.409 (2379) [0.394, 0.424] | 0.397 (6149) [0.387, 0.406] | 0.397 (4043) [0.385, 0.408] | 0.333 (3) | 0.121 | flat -0.024 (noise 0.031) |
| reversal_k8_now | 0.690 (71) | 0.659 (419) [0.617, 0.705] | 0.682 (1617) [0.663, 0.702] | 0.695 (4159) [0.683, 0.707] | 0.683 (2572) [0.668, 0.699] | 1.000 (3) | 0.122 | flat -0.024 (noise 0.034) |
| overall | 0.503 (22219) | 0.506 (154811) [0.504, 0.507] | 0.506 (661751) [0.505, 0.507] | 0.504 (1742274) [0.503, 0.505] | 0.505 (1058993) [0.504, 0.506] | 0.537 (1104) | - | flat +0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06912, 0.1] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5337, 'levels': [{'threshold': 0.06912, 'calls_per_day': 144.1, 'win_rate': 0.5524}, {'threshold': 0.1, 'calls_per_day': 36.0, 'win_rate': 0.6206}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42891, 'rate': 0.53}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14904 | 0.349 | 0.533 (14689) | 0.569 (2252) | 0.752 (2479) |
| volatility: normal | 14903 | 0.376 | 0.527 (14847) | 0.591 (1364) | 0.738 (2325) |
| volatility: wild | 14904 | 0.390 | 0.531 (14866) | 0.579 (1099) | 0.757 (2123) |
| session: Asia 00-08 | 14951 | 0.370 | 0.533 (14841) | 0.571 (1623) | 0.744 (2246) |
| session: Europe 08-13 | 9300 | 0.365 | 0.529 (9224) | 0.589 (1160) | 0.756 (1517) |
| session: US 13-21 | 14880 | 0.379 | 0.533 (14791) | 0.595 (1315) | 0.749 (2342) |
| session: late 21-24 | 5580 | 0.366 | 0.518 (5546) | 0.535 (617) | 0.746 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.394 | 0.411 | 0.295 | 0.295 | 0.550 | 0.274 | 0.515 | 0.958 |
| 6h | 360 | 0.395 | 0.383 | 0.300 | 0.344 | 0.574 | 0.288 | 0.502 | 1.191 |
| 24h | 1440 | 0.387 | 0.383 | 0.302 | 0.341 | 0.540 | 0.266 | 0.508 | 1.204 |
| 7d | 10080 | 0.386 | 0.378 | 0.301 | 0.336 | 0.533 | 0.271 | 0.501 | 1.158 |
| 30d | 43200 | 0.371 | 0.365 | 0.285 | 0.316 | 0.530 | 0.266 | 0.477 | 1.259 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.394 / 0.550 / 0.900; 2: 0.412 / 0.583 / 0.983; 3: 0.358 / 0.433 / 0.800; 4: 0.408 / 0.533 / 0.950; 5: 0.415 / 0.567 / 0.983; 6: 0.374 / 0.483 / 0.933; 7: 0.390 / 0.517 / 1.000; 8: 0.403 / 0.550 / 1.000; 9: 0.399 / 0.567 / 1.000; 10: 0.394 / 0.550 / 1.000; 11: 0.384 / 0.500 / 1.000; 12: 0.369 / 0.467 / 0.967; 13: 0.386 / 0.533 / 0.950; 14: 0.399 / 0.550 / 0.983; 15: 0.419 / 0.567 / 0.983
- 6h: 1: 0.395 / 0.574 / 0.908; 2: 0.384 / 0.552 / 0.997; 3: 0.366 / 0.465 / 0.833; 4: 0.391 / 0.532 / 0.969; 5: 0.388 / 0.538 / 0.997; 6: 0.379 / 0.496 / 0.956; 7: 0.374 / 0.493 / 1.000; 8: 0.376 / 0.515 / 1.000; 9: 0.375 / 0.518 / 1.000; 10: 0.365 / 0.479 / 1.000; 11: 0.375 / 0.515 / 1.000; 12: 0.358 / 0.465 / 0.992; 13: 0.364 / 0.471 / 0.992; 14: 0.376 / 0.496 / 0.997; 15: 0.373 / 0.490 / 0.997
- 24h: 1: 0.387 / 0.540 / 0.897; 2: 0.375 / 0.493 / 0.897; 3: 0.371 / 0.486 / 0.887; 4: 0.377 / 0.498 / 0.905; 5: 0.383 / 0.524 / 0.902; 6: 0.378 / 0.511 / 0.907; 7: 0.377 / 0.495 / 0.892; 8: 0.377 / 0.519 / 0.894; 9: 0.372 / 0.506 / 0.896; 10: 0.372 / 0.497 / 0.884; 11: 0.372 / 0.500 / 0.880; 12: 0.368 / 0.485 / 0.907; 13: 0.372 / 0.496 / 0.909; 14: 0.377 / 0.513 / 0.904; 15: 0.372 / 0.498 / 0.908
- 7d: 1: 0.386 / 0.533 / 0.899; 2: 0.373 / 0.492 / 0.899; 3: 0.377 / 0.512 / 0.898; 4: 0.372 / 0.492 / 0.900; 5: 0.374 / 0.505 / 0.900; 6: 0.372 / 0.503 / 0.901; 7: 0.373 / 0.506 / 0.899; 8: 0.374 / 0.513 / 0.898; 9: 0.367 / 0.489 / 0.900; 10: 0.372 / 0.506 / 0.898; 11: 0.371 / 0.506 / 0.896; 12: 0.371 / 0.503 / 0.901; 13: 0.370 / 0.501 / 0.901; 14: 0.370 / 0.503 / 0.900; 15: 0.368 / 0.496 / 0.901
- 30d: 1: 0.371 / 0.530 / 0.897; 2: 0.359 / 0.492 / 0.900; 3: 0.362 / 0.512 / 0.900; 4: 0.358 / 0.497 / 0.900; 5: 0.359 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.501 / 0.900; 8: 0.358 / 0.508 / 0.900; 9: 0.356 / 0.501 / 0.900; 10: 0.357 / 0.502 / 0.900; 11: 0.356 / 0.504 / 0.899; 12: 0.356 / 0.503 / 0.900; 13: 0.355 / 0.500 / 0.900; 14: 0.355 / 0.502 / 0.900; 15: 0.355 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.105 (body 0.052, range 0.158); 'price stays where it was' would score 0.166; colour right 0.500; typical miss of the close 17.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.069, range 0.168); 'price stays where it was' would score 0.114; colour right 0.521; typical miss of the close 18.8 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.132 (body 0.081, range 0.183); 'price stays where it was' would score 0.141; colour right 0.512; typical miss of the close 13.6 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.128 (body 0.083, range 0.172); 'price stays where it was' would score 0.131; colour right 0.506; typical miss of the close 14.9 bp; chain ended on the right side 0.525 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.168); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.9 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.3; 2: 0.205 / 6.0; 3: 0.168 / 7.8; 4: 0.135 / 8.1; 5: 0.127 / 8.9; 6: 0.119 / 9.6; 7: 0.112 / 10.1; 8: 0.100 / 11.1; 9: 0.093 / 11.3; 10: 0.090 / 11.9; 11: 0.086 / 12.2; 12: 0.079 / 12.6; 13: 0.074 / 13.3; 14: 0.067 / 13.5; 15: 0.067 / 14.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 156785, probability skill vs chance 0.2362, widened contest next: True
  - now: threshold 0.8314, hit rate recent 0.9207 / long run 0.9312
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.310, naive rule 0.537, lift 3.01x
    - 24h: 67 calls (67 a day), hit rate 0.910, chance 0.291, naive rule 0.494, lift 3.13x
    - 7d: 377 calls (54 a day), hit rate 0.942, chance 0.289, naive rule 0.502, lift 3.25x
    - 30d: 1731 calls (58 a day), hit rate 0.934, chance 0.294, naive rule 0.500, lift 3.18x
  - next: threshold 0.518, hit rate recent 0.566 / long run 0.5973
    - 6h: 32 calls (130 a day), hit rate 0.656, chance 0.310, lift 2.12x
    - 24h: 85 calls (85 a day), hit rate 0.541, chance 0.291, lift 1.86x
    - 7d: 413 calls (59 a day), hit rate 0.596, chance 0.289, lift 2.06x
    - 30d: 2370 calls (79 a day), hit rate 0.604, chance 0.294, lift 2.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.501; 0.35: 530, 0.526; 0.40: 477, 0.576; 0.45: 411, 0.643; 0.50: 362, 0.689; 0.55: 314, 0.735; 0.60: 264, 0.781; 0.65: 223, 0.809; 0.70: 174, 0.841; 0.75: 140, 0.873; 0.80: 93, 0.906; 0.85: 45, 0.942; 0.90: 4, 0.967
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.434; 0.35: 491, 0.467; 0.40: 390, 0.508; 0.45: 293, 0.544; 0.50: 188, 0.576; 0.55: 82, 0.587; 0.60: 11, 0.634; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 156783, probability skill vs chance 0.2072, widened contest next: True
  - now: threshold 0.7005, hit rate recent 0.8191 / long run 0.7857
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.201, naive rule 0.436, lift 3.62x
    - 24h: 62 calls (62 a day), hit rate 0.855, chance 0.195, naive rule 0.411, lift 4.39x
    - 7d: 441 calls (63 a day), hit rate 0.778, chance 0.187, naive rule 0.413, lift 4.16x
    - 30d: 1741 calls (58 a day), hit rate 0.796, chance 0.187, naive rule 0.410, lift 4.27x
  - next: threshold 0.4622, hit rate recent 0.4066 / long run 0.4825
    - 6h: 14 calls (57 a day), hit rate 0.429, chance 0.201, lift 2.13x
    - 24h: 54 calls (54 a day), hit rate 0.389, chance 0.195, lift 2.00x
    - 7d: 425 calls (61 a day), hit rate 0.475, chance 0.187, lift 2.54x
    - 30d: 2165 calls (72 a day), hit rate 0.503, chance 0.187, lift 2.70x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 361, 0.473; 0.40: 293, 0.542; 0.45: 237, 0.603; 0.50: 187, 0.653; 0.55: 150, 0.687; 0.60: 114, 0.734; 0.65: 80, 0.771; 0.70: 50, 0.807; 0.75: 28, 0.840; 0.80: 7, 0.865
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 253, 0.429; 0.40: 162, 0.459; 0.45: 65, 0.497; 0.50: 8, 0.557; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 156780, probability skill vs chance 0.1975, widened contest next: False
  - now: threshold 0.5768, hit rate recent 0.6901 / long run 0.6756
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.107, naive rule 0.312, lift 6.46x
    - 24h: 69 calls (69 a day), hit rate 0.725, chance 0.119, naive rule 0.341, lift 6.10x
    - 7d: 418 calls (60 a day), hit rate 0.660, chance 0.121, naive rule 0.344, lift 5.45x
    - 30d: 1617 calls (54 a day), hit rate 0.683, chance 0.122, naive rule 0.342, lift 5.62x
  - next: threshold 0.3672, hit rate recent 0.3792 / long run 0.4057
    - 6h: 22 calls (91 a day), hit rate 0.364, chance 0.107, lift 3.39x
    - 24h: 88 calls (89 a day), hit rate 0.409, chance 0.119, lift 3.44x
    - 7d: 513 calls (73 a day), hit rate 0.396, chance 0.121, lift 3.26x
    - 30d: 2377 calls (79 a day), hit rate 0.408, chance 0.122, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 252, 0.425; 0.35: 198, 0.486; 0.40: 156, 0.535; 0.45: 119, 0.579; 0.50: 85, 0.635; 0.55: 60, 0.675; 0.60: 40, 0.715; 0.65: 23, 0.777; 0.70: 10, 0.830; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 163, 0.372; 0.35: 85, 0.399; 0.40: 26, 0.431; 0.45: 5, 0.459; 0.50: 1, 0.731
- **K=13**: model 1795132800, labels learned 156775, probability skill vs chance 0.1693, widened contest next: True
  - now: threshold 0.4551, hit rate recent 0.5192 / long run 0.5651
    - 6h: 15 calls (63 a day), hit rate 0.400, chance 0.070, naive rule 0.227, lift 5.75x
    - 24h: 65 calls (66 a day), hit rate 0.538, chance 0.078, naive rule 0.271, lift 6.91x
    - 7d: 383 calls (55 a day), hit rate 0.561, chance 0.079, naive rule 0.294, lift 7.09x
    - 30d: 1626 calls (54 a day), hit rate 0.571, chance 0.078, naive rule 0.289, lift 7.31x
  - next: threshold 0.2943, hit rate recent 0.2713 / long run 0.3146
    - 6h: 24 calls (100 a day), hit rate 0.250, chance 0.070, lift 3.59x
    - 24h: 88 calls (89 a day), hit rate 0.284, chance 0.078, lift 3.65x
    - 7d: 489 calls (70 a day), hit rate 0.301, chance 0.079, lift 3.80x
    - 30d: 1866 calls (62 a day), hit rate 0.325, chance 0.078, lift 4.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 138, 0.424; 0.35: 100, 0.473; 0.40: 70, 0.533; 0.45: 48, 0.583; 0.50: 34, 0.625; 0.55: 21, 0.644; 0.60: 11, 0.684; 0.65: 3, 0.603; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 53, 0.334; 0.35: 14, 0.349; 0.40: 2, 0.403; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.040 | 1.29% | 0.850 | 0.400 | 0.251 | 0.517 | 0.508 |
| 6h | 25.012 | 0.96% | 0.892 | 0.478 | 0.250 | 0.518 | 0.368 |
| 24h | 21.702 | 3.02% | 0.892 | 0.492 | 0.250 | 0.517 | 0.638 |
| 7d | 24.525 | 4.03% | 0.899 | 0.499 | 0.250 | 0.501 | 0.663 |
| 30d | 17.831 | 4.65% | 0.900 | 0.500 | 0.250 | 0.505 | 0.711 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 25.366 | 25.240 | 25.339 | 24.975 | 25.508 | 25.465 | 25.003 | 24.951 | 25.034 | 25.040 |
| 6h | 25.256 | 25.183 | 25.192 | 25.041 | 25.384 | 25.205 | 24.910 | 24.952 | 24.951 | 25.012 |
| 24h | 22.378 | 21.813 | 21.852 | 21.722 | 22.008 | 21.973 | 21.632 | 21.679 | 21.666 | 21.702 |
| 7d | 25.555 | 24.690 | 24.661 | 24.547 | 25.004 | 24.806 | 24.503 | 24.481 | 24.485 | 24.525 |
| 30d | 18.699 | 17.992 | 17.952 | 17.886 | 18.184 | 18.121 | 17.810 | 17.791 | 17.799 | 17.831 |

## Next candle

- candle starting 2026-11-20 01:11 UTC, last close 1761.35
- P(up) 0.4757, return quantiles (bp): {'05': -21.311, '10': -16.106, '25': -9.188, '40': -4.133, '50': -0.751, '60': 2.377, '75': 8.086, '90': 16.702, '95': 22.678}
- changepoint probability 0.6366, regime age 26.0 min
- agent weights: empirical 0.006, ewma 0.089, garch 0.078, har 0.170, bocpd 0.028, hmm 0.051, online_qr 0.325, lgbm 0.254

## Learning log

- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- HMM volatility states (sd, bp per minute): [5.69, 9.84, 21.45], current probabilities: [0.005, 0.391, 0.604]
- live generator: {'versions': 60, 'latest_effective': '2026-11-20 01:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.573, 'l_abs': 0.693, 'l_hi': 0.809, 'l_lo': 0.708, 'b05': 0.735, 'b25': 0.653, 'b75': 0.754, 'b95': 0.697}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.5, 1.6], [1.5, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.71, 2.366, 1.872, 2.183, 2.212, 3.501, 3.75, 3.753, 5.682, 7.441, 3.103, 2.814, 3.573, 3.287]}
- calibration offsets (in sigma): {'05': 0.045, '10': -0.01, '25': -0.095, '40': -0.06, '50': -0.02, '60': -0.01, '75': 0.005, '90': 0.04, '95': 0.055}
