# ETH-USD 60s candle generator - report

- generated: 2026-10-20 17:28 UTC
- last closed candle: 2026-10-20 17:28 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.604 (96) | 0.539 (672) [0.501, 0.576] | 0.525 (2876) [0.506, 0.545] | 0.514 (4602) [0.499, 0.529] | 0.520 (1630) [0.491, 0.548] | 0.449 (69) | 0.500 | flat +0.044 (noise 0.034) |
| colour_clear | 0.556 (806) | 0.548 (5555) [0.539, 0.557] | 0.524 (23366) [0.516, 0.533] | 0.514 (37413) [0.507, 0.520] | 0.545 (13175) [0.539, 0.550] | 0.594 (641) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.664 (152) | 0.602 (721) [0.575, 0.632] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.626 (139) | 0.500 | flat +0.013 (noise 0.026) |
| colour_next | 0.549 (1436) | 0.530 (10019) [0.521, 0.539] | 0.517 (42857) [0.511, 0.522] | 0.511 (68583) [0.506, 0.515] | 0.529 (24234) [0.523, 0.534] | 0.557 (1047) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140266) [0.499, 0.505] | 0.501 (599998) [0.500, 0.502] | 0.501 (960162) [0.500, 0.502] | 0.500 (339276) [0.498, 0.503] | 0.495 (14658) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.615 (39) | 0.611 (162) [0.575, 0.662] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.800 (35) | 0.500 | flat -0.041 (noise 0.048) |
| reversal_k13_next | 0.313 (83) | 0.300 (443) [0.284, 0.315] | 0.308 (2089) [0.295, 0.321] | 0.306 (3301) [0.295, 0.318] | 0.318 (1196) [0.306, 0.330] | 0.379 (58) | 0.077 | flat -0.029 (noise 0.030) |
| reversal_k13_now | 0.474 (57) | 0.535 (383) [0.499, 0.575] | 0.577 (1552) [0.557, 0.599] | 0.575 (2406) [0.558, 0.591] | 0.565 (934) [0.539, 0.593] | 0.512 (41) | 0.077 | flat -0.033 (noise 0.036) |
| reversal_k3_next | 0.547 (117) | 0.561 (780) [0.551, 0.573] | 0.576 (2618) [0.563, 0.589] | 0.581 (4081) [0.571, 0.592] | 0.572 (1641) [0.559, 0.588] | 0.511 (92) | 0.292 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.911 (56) | 0.938 (371) [0.912, 0.963] | 0.935 (1706) [0.927, 0.944] | 0.937 (2737) [0.930, 0.944] | 0.928 (974) [0.917, 0.939] | 0.930 (43) | 0.293 | flat +0.021 (noise 0.018) |
| reversal_k5_next | 0.440 (141) | 0.453 (853) [0.434, 0.476] | 0.470 (2467) [0.455, 0.486] | 0.476 (3660) [0.464, 0.490] | 0.456 (1670) [0.440, 0.474] | 0.404 (99) | 0.187 | flat -0.015 (noise 0.029) |
| reversal_k5_now | 0.821 (56) | 0.818 (351) [0.793, 0.841] | 0.828 (1605) [0.814, 0.842] | 0.831 (2513) [0.819, 0.843] | 0.820 (902) [0.802, 0.837] | 0.850 (40) | 0.187 | flat +0.014 (noise 0.029) |
| reversal_k8_next | 0.333 (114) | 0.365 (702) [0.339, 0.390] | 0.393 (2286) [0.376, 0.410] | 0.390 (3661) [0.377, 0.402] | 0.381 (1555) [0.362, 0.399] | 0.409 (88) | 0.121 | flat -0.024 (noise 0.027) |
| reversal_k8_now | 0.580 (50) | 0.672 (329) [0.637, 0.704] | 0.710 (1566) [0.690, 0.730] | 0.705 (2500) [0.689, 0.721] | 0.689 (913) [0.663, 0.715] | 0.645 (31) | 0.122 | flat +0.006 (noise 0.035) |
| overall | 0.504 (22310) | 0.505 (155169) [0.502, 0.507] | 0.504 (661620) [0.502, 0.505] | 0.503 (1058206) [0.502, 0.504] | 0.504 (374925) [0.502, 0.506] | 0.500 (16266) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06589, 0.09829] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5328, 'levels': [{'threshold': 0.06589, 'calls_per_day': 146.1, 'win_rate': 0.5821}, {'threshold': 0.09829, 'calls_per_day': 36.5, 'win_rate': 0.6537}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 24143, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15230 | 0.336 | 0.523 (14982) | 0.591 (1456) | 0.769 (2495) |
| volatility: normal | 15229 | 0.363 | 0.519 (15165) | 0.633 (610) | 0.764 (2251) |
| volatility: wild | 15229 | 0.378 | 0.509 (15190) | 0.622 (275) | 0.778 (2059) |
| session: Asia 00-08 | 15360 | 0.358 | 0.523 (15260) | 0.613 (864) | 0.770 (2280) |
| session: Europe 08-13 | 9600 | 0.354 | 0.518 (9515) | 0.599 (598) | 0.774 (1505) |
| session: US 13-21 | 15148 | 0.367 | 0.511 (15045) | 0.581 (559) | 0.776 (2190) |
| session: late 21-24 | 5580 | 0.350 | 0.513 (5517) | 0.637 (320) | 0.748 (830) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.361 | 0.367 | 0.270 | 0.270 | 0.517 | 0.252 | 0.471 | 1.524 |
| 6h | 360 | 0.386 | 0.375 | 0.291 | 0.333 | 0.525 | 0.282 | 0.491 | 1.351 |
| 24h | 1440 | 0.376 | 0.369 | 0.275 | 0.309 | 0.542 | 0.275 | 0.477 | 1.083 |
| 7d | 10080 | 0.370 | 0.359 | 0.277 | 0.310 | 0.533 | 0.267 | 0.472 | 1.195 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.518 | 0.253 | 0.466 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.361 / 0.517 / 0.933; 2: 0.385 / 0.583 / 0.967; 3: 0.346 / 0.483 / 0.950; 4: 0.340 / 0.467 / 0.950; 5: 0.345 / 0.467 / 0.967; 6: 0.370 / 0.517 / 0.917; 7: 0.357 / 0.467 / 0.967; 8: 0.356 / 0.467 / 0.983; 9: 0.385 / 0.600 / 0.983; 10: 0.369 / 0.550 / 0.983; 11: 0.344 / 0.467 / 0.900; 12: 0.356 / 0.500 / 0.850; 13: 0.366 / 0.550 / 0.950; 14: 0.331 / 0.417 / 0.950; 15: 0.363 / 0.567 / 0.917
- 6h: 1: 0.386 / 0.525 / 0.894; 2: 0.376 / 0.528 / 0.908; 3: 0.365 / 0.508 / 0.883; 4: 0.356 / 0.467 / 0.875; 5: 0.369 / 0.547 / 0.875; 6: 0.358 / 0.475 / 0.839; 7: 0.358 / 0.475 / 0.842; 8: 0.356 / 0.506 / 0.850; 9: 0.354 / 0.472 / 0.856; 10: 0.359 / 0.533 / 0.858; 11: 0.366 / 0.536 / 0.842; 12: 0.355 / 0.489 / 0.825; 13: 0.340 / 0.439 / 0.844; 14: 0.339 / 0.453 / 0.839; 15: 0.339 / 0.483 / 0.819
- 24h: 1: 0.376 / 0.542 / 0.899; 2: 0.366 / 0.517 / 0.899; 3: 0.363 / 0.511 / 0.899; 4: 0.355 / 0.481 / 0.890; 5: 0.354 / 0.482 / 0.897; 6: 0.354 / 0.475 / 0.901; 7: 0.353 / 0.482 / 0.898; 8: 0.358 / 0.516 / 0.904; 9: 0.358 / 0.494 / 0.908; 10: 0.361 / 0.518 / 0.903; 11: 0.359 / 0.511 / 0.902; 12: 0.360 / 0.516 / 0.903; 13: 0.353 / 0.485 / 0.901; 14: 0.354 / 0.487 / 0.908; 15: 0.345 / 0.468 / 0.899
- 7d: 1: 0.370 / 0.533 / 0.899; 2: 0.356 / 0.495 / 0.899; 3: 0.359 / 0.505 / 0.900; 4: 0.354 / 0.495 / 0.900; 5: 0.355 / 0.501 / 0.900; 6: 0.355 / 0.499 / 0.898; 7: 0.353 / 0.497 / 0.898; 8: 0.353 / 0.498 / 0.898; 9: 0.354 / 0.502 / 0.898; 10: 0.356 / 0.511 / 0.898; 11: 0.350 / 0.499 / 0.898; 12: 0.353 / 0.505 / 0.898; 13: 0.352 / 0.501 / 0.898; 14: 0.352 / 0.503 / 0.899; 15: 0.351 / 0.500 / 0.899
- 30d: 1: 0.360 / 0.518 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.497 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.495 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.094 (body 0.072, range 0.116); 'price stays where it was' would score 0.137; colour right 0.517; typical miss of the close 21.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.130 (body 0.095, range 0.165); 'price stays where it was' would score 0.118; colour right 0.483; typical miss of the close 16.9 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.116 (body 0.077, range 0.155); 'price stays where it was' would score 0.112; colour right 0.514; typical miss of the close 10.5 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.127 (body 0.086, range 0.167); 'price stays where it was' would score 0.132; colour right 0.501; typical miss of the close 9.2 bp; chain ended on the right side 0.534 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.9; 2: 0.197 / 4.6; 3: 0.163 / 6.1; 4: 0.132 / 6.6; 5: 0.120 / 7.3; 6: 0.109 / 7.8; 7: 0.103 / 8.2; 8: 0.095 / 8.5; 9: 0.086 / 8.5; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.077 / 10.2; 13: 0.065 / 10.5; 14: 0.066 / 10.7; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 113122, probability skill vs chance 0.2188, widened contest next: True
  - now: threshold 0.8355, hit rate recent 0.9227 / long run 0.9307
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.299, naive rule 0.481, lift 3.07x
    - 24h: 62 calls (62 a day), hit rate 0.919, chance 0.277, naive rule 0.457, lift 3.31x
    - 7d: 381 calls (54 a day), hit rate 0.932, chance 0.289, naive rule 0.479, lift 3.23x
    - 30d: 1707 calls (57 a day), hit rate 0.934, chance 0.292, naive rule 0.484, lift 3.20x
  - next: threshold 0.5328, hit rate recent 0.5129 / long run 0.5605
    - 6h: 30 calls (122 a day), hit rate 0.433, chance 0.299, lift 1.45x
    - 24h: 121 calls (121 a day), hit rate 0.529, chance 0.277, lift 1.91x
    - 7d: 734 calls (105 a day), hit rate 0.557, chance 0.289, lift 1.93x
    - 30d: 2634 calls (88 a day), hit rate 0.572, chance 0.292, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 540, 0.514; 0.40: 482, 0.567; 0.45: 413, 0.637; 0.50: 361, 0.689; 0.55: 316, 0.730; 0.60: 269, 0.774; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 138, 0.870; 0.80: 94, 0.911; 0.85: 48, 0.949; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 498, 0.461; 0.40: 406, 0.492; 0.45: 311, 0.524; 0.50: 202, 0.555; 0.55: 90, 0.571; 0.60: 14, 0.609; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 113120, probability skill vs chance 0.2123, widened contest next: True
  - now: threshold 0.6828, hit rate recent 0.8331 / long run 0.8252
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.212, naive rule 0.453, lift 4.34x
    - 24h: 56 calls (56 a day), hit rate 0.821, chance 0.185, naive rule 0.393, lift 4.43x
    - 7d: 355 calls (51 a day), hit rate 0.820, chance 0.186, naive rule 0.397, lift 4.42x
    - 30d: 1592 calls (53 a day), hit rate 0.828, chance 0.187, naive rule 0.394, lift 4.42x
  - next: threshold 0.4168, hit rate recent 0.4133 / long run 0.4452
    - 6h: 36 calls (147 a day), hit rate 0.389, chance 0.212, lift 1.83x
    - 24h: 129 calls (130 a day), hit rate 0.411, chance 0.185, lift 2.22x
    - 7d: 867 calls (124 a day), hit rate 0.442, chance 0.186, lift 2.38x
    - 30d: 2487 calls (83 a day), hit rate 0.466, chance 0.187, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.423; 0.35: 348, 0.488; 0.40: 280, 0.559; 0.45: 227, 0.615; 0.50: 180, 0.663; 0.55: 137, 0.708; 0.60: 107, 0.750; 0.65: 80, 0.789; 0.70: 57, 0.823; 0.75: 32, 0.864; 0.80: 10, 0.886
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.418; 0.40: 158, 0.444; 0.45: 73, 0.460; 0.50: 17, 0.497; 0.55: 2, 0.510
- **K=8**: model 1792454400, labels learned 113117, probability skill vs chance 0.2008, widened contest next: True
  - now: threshold 0.5692, hit rate recent 0.6313 / long run 0.6858
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.129, naive rule 0.372, lift 5.44x
    - 24h: 48 calls (48 a day), hit rate 0.625, chance 0.119, naive rule 0.320, lift 5.27x
    - 7d: 327 calls (47 a day), hit rate 0.664, chance 0.119, naive rule 0.321, lift 5.58x
    - 30d: 1561 calls (52 a day), hit rate 0.705, chance 0.122, naive rule 0.328, lift 5.79x
  - next: threshold 0.3461, hit rate recent 0.4082 / long run 0.3768
    - 6h: 30 calls (123 a day), hit rate 0.500, chance 0.129, lift 3.89x
    - 24h: 114 calls (115 a day), hit rate 0.368, chance 0.119, lift 3.11x
    - 7d: 724 calls (104 a day), hit rate 0.365, chance 0.119, lift 3.07x
    - 30d: 2329 calls (78 a day), hit rate 0.390, chance 0.122, lift 3.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 255, 0.421; 0.35: 194, 0.491; 0.40: 148, 0.547; 0.45: 116, 0.590; 0.50: 89, 0.632; 0.55: 64, 0.679; 0.60: 43, 0.722; 0.65: 24, 0.781; 0.70: 10, 0.828; 0.75: 1, 0.793
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.350; 0.35: 103, 0.381; 0.40: 41, 0.408; 0.45: 8, 0.427; 0.50: 1, 0.471
- **K=13**: model 1792454400, labels learned 113112, probability skill vs chance 0.1879, widened contest next: True
  - now: threshold 0.424, hit rate recent 0.4916 / long run 0.5535
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.091, naive rule 0.354, lift 6.39x
    - 24h: 64 calls (65 a day), hit rate 0.469, chance 0.078, naive rule 0.262, lift 6.02x
    - 7d: 392 calls (56 a day), hit rate 0.518, chance 0.077, naive rule 0.271, lift 6.74x
    - 30d: 1553 calls (52 a day), hit rate 0.572, chance 0.078, naive rule 0.272, lift 7.35x
  - next: threshold 0.2758, hit rate recent 0.3467 / long run 0.3163
    - 6h: 25 calls (104 a day), hit rate 0.360, chance 0.091, lift 3.94x
    - 24h: 78 calls (79 a day), hit rate 0.372, chance 0.078, lift 4.77x
    - 7d: 441 calls (63 a day), hit rate 0.313, chance 0.077, lift 4.07x
    - 30d: 2112 calls (70 a day), hit rate 0.309, chance 0.078, lift 3.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.450; 0.35: 86, 0.504; 0.40: 61, 0.553; 0.45: 41, 0.609; 0.50: 25, 0.656; 0.55: 14, 0.710; 0.60: 5, 0.750; 0.65: 1, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.321; 0.35: 13, 0.356; 0.40: 2, 0.433

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.735 | -0.99% | 0.917 | 0.600 | 0.249 | 0.550 | 0.088 |
| 6h | 27.319 | 5.64% | 0.883 | 0.547 | 0.251 | 0.497 | 0.599 |
| 24h | 17.462 | 3.24% | 0.894 | 0.502 | 0.250 | 0.511 | 0.654 |
| 7d | 16.232 | 4.33% | 0.899 | 0.500 | 0.251 | 0.493 | 0.652 |
| 30d | 13.908 | 4.03% | 0.900 | 0.500 | 0.251 | 0.495 | 0.676 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.522 | 21.672 | 21.667 | 21.742 | 21.862 | 22.164 | 21.723 | 21.653 | 21.678 | 21.735 |
| 6h | 28.952 | 27.493 | 27.304 | 27.165 | 27.667 | 27.643 | 27.382 | 27.232 | 27.237 | 27.319 |
| 24h | 18.047 | 17.558 | 17.500 | 17.454 | 17.711 | 17.600 | 17.475 | 17.418 | 17.425 | 17.462 |
| 7d | 16.966 | 16.412 | 16.317 | 16.242 | 16.479 | 16.432 | 16.231 | 16.211 | 16.200 | 16.232 |
| 30d | 14.492 | 14.032 | 13.993 | 13.931 | 14.156 | 14.095 | 13.905 | 13.882 | 13.881 | 13.908 |

## Next candle

- candle starting 2026-10-20 17:28 UTC, last close 2446.83
- P(up) 0.5402, return quantiles (bp): {'05': -11.052, '10': -8.707, '25': -4.27, '40': -1.008, '50': 0.653, '60': 2.131, '75': 4.668, '90': 8.858, '95': 11.799}
- changepoint probability 0.0551, regime age 83.2 min
- agent weights: empirical 0.003, ewma 0.073, garch 0.160, har 0.273, bocpd 0.024, hmm 0.039, online_qr 0.146, lgbm 0.282

## Learning log

- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.79, 15.89], current probabilities: [0.039, 0.947, 0.014]
- live generator: {'versions': 60, 'latest_effective': '2026-10-20 17:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.206, 'l_abs': 0.724, 'l_hi': 0.811, 'l_lo': 0.792, 'b05': 0.711, 'b25': 0.68, 'b75': 0.714, 'b95': 0.713}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.755, 1.949, 2.542, 2.848, 3.387, 3.593, 3.625, 3.852, 3.832, 4.191, 4.565, 4.667, 4.757, 5.238]}
- calibration offsets (in sigma): {'05': 0.0235, '10': -0.003, '25': 0.0175, '40': 0.058, '50': 0.065, '60': 0.052, '75': 0.0325, '90': 0.023, '95': 0.0065}
