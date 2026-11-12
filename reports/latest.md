# ETH-USD 60s candle generator - report

- generated: 2026-11-12 22:20 UTC
- last closed candle: 2026-11-12 22:20 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.531 (672) [0.497, 0.561] | 0.519 (2880) [0.502, 0.537] | 0.514 (6810) [0.502, 0.526] | 0.516 (3838) [0.500, 0.532] | 0.528 (89) | 0.500 | up +0.061 (noise 0.027) |
| colour_clear | 0.517 (842) | 0.546 (5562) [0.533, 0.559] | 0.543 (23911) [0.536, 0.548] | 0.522 (55769) [0.517, 0.528] | 0.543 (31531) [0.538, 0.547] | 0.534 (725) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.507 (67) | 0.567 (947) [0.535, 0.591] | 0.587 (4269) [0.577, 0.598] | 0.592 (5750) [0.581, 0.602] | 0.592 (5750) [0.581, 0.602] | 0.589 (73) | 0.500 | flat -0.008 (noise 0.023) |
| colour_next | 0.507 (1439) | 0.531 (9972) [0.520, 0.544] | 0.530 (42869) [0.525, 0.534] | 0.517 (101433) [0.513, 0.521] | 0.529 (57084) [0.525, 0.533] | 0.531 (1335) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.508 (20146) | 0.502 (139608) [0.499, 0.505] | 0.502 (600166) [0.500, 0.503] | 0.501 (1420062) [0.500, 0.502] | 0.501 (799176) [0.500, 0.502] | 0.505 (18690) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.400 (5) | 0.628 (242) [0.588, 0.648] | 0.620 (1101) [0.604, 0.637] | 0.630 (1513) [0.614, 0.647] | 0.630 (1513) [0.614, 0.647] | 0.455 (11) | 0.500 | flat -0.003 (noise 0.046) |
| reversal_k13_next | 0.347 (72) | 0.332 (500) [0.309, 0.355] | 0.326 (1838) [0.312, 0.341] | 0.315 (4696) [0.304, 0.325] | 0.327 (2591) [0.315, 0.338] | 0.317 (60) | 0.077 | flat -0.023 (noise 0.033) |
| reversal_k13_now | 0.577 (52) | 0.577 (350) [0.551, 0.605] | 0.563 (1635) [0.543, 0.582] | 0.574 (3658) [0.561, 0.586] | 0.569 (2186) [0.551, 0.586] | 0.556 (36) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.694 (49) | 0.627 (362) [0.592, 0.659] | 0.591 (2801) [0.579, 0.604] | 0.588 (6102) [0.579, 0.597] | 0.589 (3662) [0.578, 0.600] | 0.569 (58) | 0.293 | flat +0.027 (noise 0.031) |
| reversal_k3_now | 0.912 (57) | 0.920 (412) [0.911, 0.930] | 0.933 (1716) [0.923, 0.944] | 0.935 (4082) [0.929, 0.941] | 0.930 (2319) [0.922, 0.938] | 0.909 (55) | 0.294 | flat -0.007 (noise 0.018) |
| reversal_k5_next | 0.404 (57) | 0.518 (398) [0.477, 0.550] | 0.486 (2650) [0.471, 0.503] | 0.485 (5457) [0.474, 0.496] | 0.480 (3467) [0.466, 0.495] | 0.449 (69) | 0.187 | flat -0.020 (noise 0.036) |
| reversal_k5_now | 0.667 (69) | 0.774 (389) [0.724, 0.821] | 0.808 (1643) [0.791, 0.821] | 0.822 (3805) [0.812, 0.832] | 0.811 (2194) [0.798, 0.824] | 0.735 (49) | 0.187 | flat -0.036 (noise 0.031) |
| reversal_k8_next | 0.429 (70) | 0.423 (466) [0.392, 0.452] | 0.397 (2613) [0.383, 0.411] | 0.396 (5572) [0.386, 0.407] | 0.396 (3466) [0.384, 0.408] | 0.426 (61) | 0.121 | flat -0.014 (noise 0.032) |
| reversal_k8_now | 0.661 (56) | 0.695 (367) [0.675, 0.716] | 0.686 (1524) [0.668, 0.704] | 0.700 (3695) [0.687, 0.713] | 0.690 (2108) [0.672, 0.706] | 0.605 (38) | 0.122 | flat -0.002 (noise 0.034) |
| overall | 0.510 (22163) | 0.506 (153496) [0.503, 0.509] | 0.505 (662335) [0.504, 0.507] | 0.504 (1565372) [0.503, 0.505] | 0.505 (882091) [0.504, 0.506] | 0.508 (20540) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07482, 0.1144] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5337, 'levels': [{'threshold': 0.07482, 'calls_per_day': 141.5, 'win_rate': 0.5774}, {'threshold': 0.1144, 'calls_per_day': 35.8, 'win_rate': 0.6206}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42869, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15327 | 0.346 | 0.533 (15087) | 0.567 (2286) | 0.734 (2586) |
| volatility: normal | 15326 | 0.370 | 0.529 (15262) | 0.608 (1351) | 0.750 (2260) |
| volatility: wild | 15327 | 0.386 | 0.527 (15289) | 0.610 (766) | 0.766 (2072) |
| session: Asia 00-08 | 15360 | 0.367 | 0.535 (15234) | 0.592 (1551) | 0.752 (2277) |
| session: Europe 08-13 | 9600 | 0.361 | 0.532 (9520) | 0.586 (1146) | 0.751 (1557) |
| session: US 13-21 | 15360 | 0.374 | 0.528 (15260) | 0.597 (1158) | 0.751 (2296) |
| session: late 21-24 | 5660 | 0.359 | 0.513 (5624) | 0.553 (548) | 0.730 (788) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.370 | 0.345 | 0.293 | 0.293 | 0.500 | 0.253 | 0.488 | 1.079 |
| 6h | 360 | 0.373 | 0.369 | 0.301 | 0.354 | 0.511 | 0.259 | 0.488 | 1.125 |
| 24h | 1440 | 0.376 | 0.372 | 0.295 | 0.330 | 0.533 | 0.273 | 0.479 | 1.094 |
| 7d | 10080 | 0.369 | 0.364 | 0.281 | 0.313 | 0.533 | 0.268 | 0.471 | 1.348 |
| 30d | 43200 | 0.367 | 0.360 | 0.279 | 0.311 | 0.530 | 0.264 | 0.470 | 1.256 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.370 / 0.500 / 0.900; 2: 0.377 / 0.500 / 0.950; 3: 0.373 / 0.450 / 0.967; 4: 0.335 / 0.433 / 0.917; 5: 0.392 / 0.533 / 0.883; 6: 0.330 / 0.417 / 0.917; 7: 0.353 / 0.450 / 1.000; 8: 0.390 / 0.567 / 1.000; 9: 0.362 / 0.467 / 0.967; 10: 0.385 / 0.533 / 0.983; 11: 0.361 / 0.483 / 1.000; 12: 0.351 / 0.467 / 1.000; 13: 0.339 / 0.400 / 1.000; 14: 0.303 / 0.283 / 1.000; 15: 0.334 / 0.367 / 1.000
- 6h: 1: 0.373 / 0.511 / 0.900; 2: 0.366 / 0.483 / 0.950; 3: 0.382 / 0.517 / 0.969; 4: 0.352 / 0.458 / 0.878; 5: 0.378 / 0.511 / 0.892; 6: 0.355 / 0.467 / 0.906; 7: 0.373 / 0.494 / 0.967; 8: 0.378 / 0.525 / 0.972; 9: 0.365 / 0.494 / 0.961; 10: 0.381 / 0.497 / 0.972; 11: 0.382 / 0.528 / 0.997; 12: 0.373 / 0.500 / 0.994; 13: 0.371 / 0.481 / 0.994; 14: 0.363 / 0.461 / 0.992; 15: 0.378 / 0.500 / 0.983
- 24h: 1: 0.376 / 0.533 / 0.899; 2: 0.352 / 0.463 / 0.904; 3: 0.371 / 0.519 / 0.904; 4: 0.365 / 0.509 / 0.893; 5: 0.364 / 0.494 / 0.897; 6: 0.365 / 0.507 / 0.899; 7: 0.369 / 0.511 / 0.907; 8: 0.368 / 0.519 / 0.904; 9: 0.366 / 0.508 / 0.903; 10: 0.365 / 0.494 / 0.903; 11: 0.365 / 0.509 / 0.888; 12: 0.368 / 0.519 / 0.885; 13: 0.366 / 0.513 / 0.890; 14: 0.361 / 0.507 / 0.890; 15: 0.365 / 0.507 / 0.886
- 7d: 1: 0.369 / 0.533 / 0.897; 2: 0.354 / 0.483 / 0.902; 3: 0.360 / 0.517 / 0.902; 4: 0.354 / 0.495 / 0.901; 5: 0.356 / 0.504 / 0.901; 6: 0.352 / 0.494 / 0.903; 7: 0.354 / 0.498 / 0.901; 8: 0.355 / 0.501 / 0.904; 9: 0.356 / 0.506 / 0.901; 10: 0.355 / 0.503 / 0.901; 11: 0.357 / 0.515 / 0.899; 12: 0.353 / 0.502 / 0.900; 13: 0.353 / 0.500 / 0.901; 14: 0.353 / 0.505 / 0.900; 15: 0.353 / 0.497 / 0.900
- 30d: 1: 0.367 / 0.530 / 0.897; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.499 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.500 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.353 / 0.504 / 0.900; 9: 0.353 / 0.504 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.351 / 0.502 / 0.900; 12: 0.352 / 0.503 / 0.900; 13: 0.351 / 0.500 / 0.900; 14: 0.351 / 0.502 / 0.900; 15: 0.351 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.161 (body 0.119, range 0.204); 'price stays where it was' would score 0.163; colour right 0.450; typical miss of the close 6.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.123 (body 0.081, range 0.165); 'price stays where it was' would score 0.139; colour right 0.467; typical miss of the close 11.1 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.124 (body 0.084, range 0.164); 'price stays where it was' would score 0.132; colour right 0.504; typical miss of the close 10.9 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.124 (body 0.083, range 0.165); 'price stays where it was' would score 0.125; colour right 0.503; typical miss of the close 8.6 bp; chain ended on the right side 0.530 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 8.9 bp; chain ended on the right side 0.519 of 2880 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.7; 2: 0.202 / 5.5; 3: 0.168 / 7.1; 4: 0.133 / 7.2; 5: 0.127 / 8.0; 6: 0.116 / 8.9; 7: 0.110 / 9.1; 8: 0.098 / 10.0; 9: 0.091 / 10.2; 10: 0.093 / 10.5; 11: 0.089 / 10.8; 12: 0.079 / 11.1; 13: 0.073 / 11.7; 14: 0.070 / 12.2; 15: 0.066 / 12.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 146534, probability skill vs chance 0.223, widened contest next: False
  - now: threshold 0.8399, hit rate recent 0.8969 / long run 0.9232
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.280, naive rule 0.463, lift 2.92x
    - 24h: 57 calls (57 a day), hit rate 0.912, chance 0.294, naive rule 0.476, lift 3.11x
    - 7d: 413 calls (59 a day), hit rate 0.920, chance 0.297, naive rule 0.504, lift 3.10x
    - 30d: 1731 calls (58 a day), hit rate 0.931, chance 0.293, naive rule 0.495, lift 3.17x
  - next: threshold 0.5675, hit rate recent 0.6119 / long run 0.6068
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.280, lift 2.50x
    - 24h: 63 calls (63 a day), hit rate 0.587, chance 0.294, lift 2.00x
    - 7d: 360 calls (51 a day), hit rate 0.608, chance 0.297, lift 2.05x
    - 30d: 2698 calls (90 a day), hit rate 0.593, chance 0.293, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.579; 0.45: 406, 0.649; 0.50: 357, 0.695; 0.55: 310, 0.739; 0.60: 261, 0.783; 0.65: 220, 0.810; 0.70: 172, 0.842; 0.75: 138, 0.874; 0.80: 92, 0.903; 0.85: 46, 0.943; 0.90: 4, 0.993
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.431; 0.35: 497, 0.464; 0.40: 397, 0.502; 0.45: 299, 0.535; 0.50: 192, 0.567; 0.55: 86, 0.578; 0.60: 11, 0.647; 0.65: 1, 0.667
- **K=5**: model 1794441600, labels learned 146532, probability skill vs chance 0.2155, widened contest next: True
  - now: threshold 0.6872, hit rate recent 0.7325 / long run 0.7875
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.187, naive rule 0.407, lift 4.90x
    - 24h: 54 calls (54 a day), hit rate 0.704, chance 0.184, naive rule 0.388, lift 3.83x
    - 7d: 392 calls (56 a day), hit rate 0.760, chance 0.187, naive rule 0.409, lift 4.06x
    - 30d: 1649 calls (55 a day), hit rate 0.805, chance 0.186, naive rule 0.406, lift 4.32x
  - next: threshold 0.4463, hit rate recent 0.4547 / long run 0.5034
    - 6h: 23 calls (94 a day), hit rate 0.522, chance 0.187, lift 2.79x
    - 24h: 74 calls (74 a day), hit rate 0.419, chance 0.184, lift 2.28x
    - 7d: 411 calls (59 a day), hit rate 0.499, chance 0.187, lift 2.67x
    - 30d: 2618 calls (87 a day), hit rate 0.485, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.420; 0.35: 355, 0.480; 0.40: 287, 0.551; 0.45: 233, 0.606; 0.50: 187, 0.654; 0.55: 149, 0.691; 0.60: 112, 0.740; 0.65: 75, 0.778; 0.70: 47, 0.814; 0.75: 28, 0.847; 0.80: 10, 0.870
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.383; 0.35: 256, 0.423; 0.40: 160, 0.457; 0.45: 65, 0.492; 0.50: 10, 0.516; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 146529, probability skill vs chance 0.2039, widened contest next: True
  - now: threshold 0.5674, hit rate recent 0.6505 / long run 0.6864
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.141, naive rule 0.392, lift 4.71x
    - 24h: 44 calls (44 a day), hit rate 0.568, chance 0.127, naive rule 0.340, lift 4.48x
    - 7d: 362 calls (52 a day), hit rate 0.682, chance 0.124, naive rule 0.345, lift 5.52x
    - 30d: 1520 calls (51 a day), hit rate 0.684, chance 0.121, naive rule 0.335, lift 5.67x
  - next: threshold 0.3653, hit rate recent 0.4318 / long run 0.4209
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.141, lift 3.81x
    - 24h: 66 calls (66 a day), hit rate 0.394, chance 0.127, lift 3.10x
    - 7d: 468 calls (67 a day), hit rate 0.412, chance 0.124, lift 3.33x
    - 30d: 2597 calls (87 a day), hit rate 0.397, chance 0.121, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 193, 0.490; 0.40: 152, 0.534; 0.45: 118, 0.581; 0.50: 84, 0.635; 0.55: 59, 0.672; 0.60: 39, 0.710; 0.65: 23, 0.775; 0.70: 11, 0.812; 0.75: 2, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 170, 0.364; 0.35: 86, 0.391; 0.40: 23, 0.416; 0.45: 4, 0.413; 0.50: 1, 0.773
- **K=13**: model 1794355200, labels learned 146524, probability skill vs chance 0.1885, widened contest next: False
  - now: threshold 0.4465, hit rate recent 0.5861 / long run 0.5724
    - 6h: 8 calls (33 a day), hit rate 0.750, chance 0.074, naive rule 0.289, lift 10.15x
    - 24h: 42 calls (42 a day), hit rate 0.500, chance 0.069, naive rule 0.258, lift 7.20x
    - 7d: 333 calls (48 a day), hit rate 0.577, chance 0.079, naive rule 0.293, lift 7.31x
    - 30d: 1632 calls (54 a day), hit rate 0.559, chance 0.077, naive rule 0.282, lift 7.22x
  - next: threshold 0.2961, hit rate recent 0.3308 / long run 0.3354
    - 6h: 14 calls (58 a day), hit rate 0.357, chance 0.074, lift 4.83x
    - 24h: 65 calls (66 a day), hit rate 0.292, chance 0.069, lift 4.21x
    - 7d: 499 calls (71 a day), hit rate 0.331, chance 0.079, lift 4.19x
    - 30d: 1829 calls (61 a day), hit rate 0.328, chance 0.077, lift 4.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.429; 0.35: 97, 0.477; 0.40: 67, 0.534; 0.45: 46, 0.581; 0.50: 31, 0.638; 0.55: 20, 0.658; 0.60: 12, 0.690; 0.65: 3, 0.660; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.334; 0.35: 13, 0.333; 0.40: 2, 0.395; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.248 | 4.40% | 0.917 | 0.533 | 0.250 | 0.400 | 0.312 |
| 6h | 17.235 | 0.49% | 0.894 | 0.514 | 0.250 | 0.489 | 0.475 |
| 24h | 19.318 | 5.00% | 0.901 | 0.504 | 0.249 | 0.523 | 0.666 |
| 7d | 16.250 | 5.90% | 0.901 | 0.501 | 0.250 | 0.512 | 0.658 |
| 30d | 15.884 | 4.77% | 0.900 | 0.500 | 0.250 | 0.503 | 0.689 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.811 | 12.309 | 12.341 | 12.238 | 12.581 | 12.580 | 12.172 | 12.235 | 12.225 | 12.248 |
| 6h | 17.320 | 17.295 | 17.281 | 17.308 | 17.470 | 17.395 | 17.237 | 17.206 | 17.216 | 17.235 |
| 24h | 20.335 | 19.565 | 19.520 | 19.347 | 19.790 | 19.735 | 19.279 | 19.265 | 19.279 | 19.318 |
| 7d | 17.268 | 16.407 | 16.397 | 16.389 | 16.604 | 16.623 | 16.212 | 16.193 | 16.216 | 16.250 |
| 30d | 16.680 | 16.047 | 15.993 | 15.937 | 16.181 | 16.156 | 15.868 | 15.850 | 15.854 | 15.884 |

## Next candle

- candle starting 2026-11-12 22:20 UTC, last close 2008.12
- P(up) 0.5128, return quantiles (bp): {'05': -10.942, '10': -7.538, '25': -3.585, '40': -1.163, '50': 0.168, '60': 1.775, '75': 4.397, '90': 8.165, '95': 10.684}
- changepoint probability 0.0601, regime age 138.0 min
- agent weights: empirical 0.003, ewma 0.046, garch 0.062, har 0.183, bocpd 0.013, hmm 0.032, online_qr 0.309, lgbm 0.352

## Learning log

- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- HMM volatility states (sd, bp per minute): [2.31, 5.8, 18.24], current probabilities: [0.0, 0.949, 0.051]
- live generator: {'versions': 60, 'latest_effective': '2026-11-12 22:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.236, 'l_abs': 0.684, 'l_hi': 0.738, 'l_lo': 0.711, 'b05': 0.726, 'b25': 0.708, 'b75': 0.704, 'b95': 0.711}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.172, 1.438, 2.202, 2.102, 2.261, 1.964, 2.021, 2.192, 2.315, 3.853, 4.114, 4.041, 4.202, 4.536]}
- calibration offsets (in sigma): {'05': 0.0395, '10': 0.069, '25': 0.0475, '40': 0.006, '50': -0.015, '60': 0.004, '75': -0.0175, '90': -0.039, '95': -0.0695}
