# ETH-USD 60s candle generator - report

- generated: 2026-11-03 11:22 UTC
- last closed candle: 2026-11-03 11:22 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.498 (672) [0.476, 0.521] | 0.517 (2878) [0.498, 0.536] | 0.514 (5946) [0.501, 0.527] | 0.517 (2974) [0.499, 0.536] | 0.400 (45) | 0.500 | flat -0.031 (noise 0.027) |
| colour_clear | 0.524 (809) | 0.540 (5488) [0.531, 0.550] | 0.544 (23646) [0.540, 0.549] | 0.521 (48605) [0.515, 0.527] | 0.545 (24367) [0.540, 0.548] | 0.531 (401) | 0.500 | flat -0.008 (noise 0.009) |
| colour_confident | 0.568 (88) | 0.575 (979) [0.564, 0.587] | 0.597 (4516) [0.585, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.720 (50) | 0.500 | flat -0.026 (noise 0.021) |
| colour_next | 0.530 (1434) | 0.531 (9968) [0.525, 0.538] | 0.530 (42837) [0.526, 0.534] | 0.515 (88590) [0.511, 0.519] | 0.530 (44241) [0.526, 0.533] | 0.532 (681) | 0.500 | flat +0.000 (noise 0.007) |
| colour_path | 0.498 (20076) | 0.502 (139552) [0.500, 0.504] | 0.501 (599718) [0.500, 0.502] | 0.501 (1240260) [0.500, 0.502] | 0.501 (619374) [0.499, 0.502] | 0.510 (9534) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.706 (17) | 0.619 (236) [0.577, 0.663] | 0.633 (1203) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.714 (7) | 0.500 | flat -0.008 (noise 0.040) |
| reversal_k13_next | 0.404 (47) | 0.356 (343) [0.308, 0.402] | 0.323 (1879) [0.310, 0.337] | 0.311 (4086) [0.301, 0.323] | 0.323 (1981) [0.311, 0.336] | 0.485 (33) | 0.077 | flat +0.043 (noise 0.034) |
| reversal_k13_now | 0.471 (51) | 0.581 (422) [0.543, 0.614] | 0.560 (1681) [0.541, 0.579] | 0.572 (3198) [0.558, 0.586] | 0.565 (1726) [0.545, 0.585] | 0.640 (25) | 0.077 | flat +0.035 (noise 0.035) |
| reversal_k3_next | 0.646 (113) | 0.599 (877) [0.587, 0.614] | 0.588 (3052) [0.577, 0.598] | 0.586 (5636) [0.578, 0.596] | 0.585 (3196) [0.575, 0.597] | 0.513 (37) | 0.293 | flat -0.002 (noise 0.025) |
| reversal_k3_now | 0.898 (59) | 0.934 (441) [0.912, 0.958] | 0.934 (1747) [0.924, 0.944] | 0.938 (3567) [0.931, 0.944] | 0.933 (1804) [0.923, 0.943] | 0.857 (28) | 0.293 | flat -0.012 (noise 0.020) |
| reversal_k5_next | 0.564 (55) | 0.543 (392) [0.528, 0.558] | 0.479 (2766) [0.464, 0.494] | 0.482 (4945) [0.471, 0.494] | 0.474 (2955) [0.460, 0.490] | 0.455 (33) | 0.187 | up +0.064 (noise 0.030) |
| reversal_k5_now | 0.803 (66) | 0.822 (443) [0.808, 0.834] | 0.821 (1645) [0.809, 0.832] | 0.829 (3317) [0.820, 0.838] | 0.821 (1706) [0.810, 0.831] | 0.724 (29) | 0.187 | flat +0.002 (noise 0.027) |
| reversal_k8_next | 0.475 (40) | 0.435 (575) [0.411, 0.461] | 0.391 (2808) [0.377, 0.405] | 0.393 (4991) [0.382, 0.404] | 0.391 (2885) [0.378, 0.404] | 0.455 (33) | 0.121 | up +0.056 (noise 0.027) |
| reversal_k8_now | 0.635 (52) | 0.716 (391) [0.680, 0.746] | 0.686 (1596) [0.665, 0.706] | 0.701 (3233) [0.687, 0.716] | 0.689 (1646) [0.667, 0.709] | 0.633 (30) | 0.122 | flat +0.058 (noise 0.036) |
| overall | 0.503 (22089) | 0.507 (154076) [0.504, 0.509] | 0.505 (662607) [0.503, 0.506] | 0.504 (1367769) [0.503, 0.505] | 0.505 (684488) [0.503, 0.506] | 0.513 (10508) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0801, 0.1219] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5313, 'levels': [{'threshold': 0.0801, 'calls_per_day': 142.9, 'win_rate': 0.5786}, {'threshold': 0.1219, 'calls_per_day': 35.5, 'win_rate': 0.6135}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42845, 'rate': 0.53}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15108 | 0.334 | 0.527 (14826) | 0.577 (2255) | 0.758 (2633) |
| volatility: normal | 15107 | 0.366 | 0.534 (15034) | 0.612 (1563) | 0.741 (2272) |
| volatility: wild | 15107 | 0.381 | 0.529 (15062) | 0.631 (832) | 0.763 (2089) |
| session: Asia 00-08 | 15360 | 0.360 | 0.536 (15245) | 0.603 (1639) | 0.759 (2286) |
| session: Europe 08-13 | 9502 | 0.354 | 0.533 (9398) | 0.595 (1179) | 0.745 (1595) |
| session: US 13-21 | 14880 | 0.367 | 0.527 (14758) | 0.596 (1199) | 0.759 (2271) |
| session: late 21-24 | 5580 | 0.351 | 0.516 (5521) | 0.596 (633) | 0.744 (842) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.377 | 0.393 | 0.260 | 0.260 | 0.550 | 0.281 | 0.473 | 1.250 |
| 6h | 360 | 0.380 | 0.375 | 0.292 | 0.337 | 0.521 | 0.267 | 0.493 | 1.173 |
| 24h | 1440 | 0.376 | 0.375 | 0.296 | 0.337 | 0.522 | 0.266 | 0.486 | 1.102 |
| 7d | 10080 | 0.360 | 0.356 | 0.275 | 0.306 | 0.530 | 0.261 | 0.459 | 1.277 |
| 30d | 43200 | 0.363 | 0.355 | 0.276 | 0.306 | 0.530 | 0.262 | 0.463 | 1.252 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.377 / 0.550 / 0.900; 2: 0.367 / 0.517 / 0.983; 3: 0.390 / 0.600 / 0.950; 4: 0.375 / 0.483 / 0.950; 5: 0.344 / 0.433 / 1.000; 6: 0.371 / 0.483 / 0.983; 7: 0.370 / 0.483 / 1.000; 8: 0.378 / 0.533 / 1.000; 9: 0.361 / 0.450 / 1.000; 10: 0.373 / 0.500 / 1.000; 11: 0.413 / 0.633 / 1.000; 12: 0.340 / 0.467 / 1.000; 13: 0.340 / 0.467 / 1.000; 14: 0.372 / 0.533 / 1.000; 15: 0.381 / 0.533 / 1.000
- 6h: 1: 0.380 / 0.521 / 0.886; 2: 0.368 / 0.513 / 0.975; 3: 0.376 / 0.549 / 0.869; 4: 0.370 / 0.507 / 0.900; 5: 0.366 / 0.493 / 0.961; 6: 0.379 / 0.549 / 0.861; 7: 0.378 / 0.518 / 0.969; 8: 0.373 / 0.518 / 0.967; 9: 0.368 / 0.499 / 0.956; 10: 0.358 / 0.474 / 0.975; 11: 0.387 / 0.560 / 0.953; 12: 0.349 / 0.437 / 0.917; 13: 0.374 / 0.535 / 0.947; 14: 0.371 / 0.526 / 0.922; 15: 0.383 / 0.549 / 0.931
- 24h: 1: 0.376 / 0.522 / 0.889; 2: 0.370 / 0.507 / 0.910; 3: 0.367 / 0.507 / 0.887; 4: 0.365 / 0.496 / 0.889; 5: 0.363 / 0.497 / 0.901; 6: 0.368 / 0.512 / 0.885; 7: 0.373 / 0.522 / 0.899; 8: 0.368 / 0.510 / 0.899; 9: 0.363 / 0.499 / 0.897; 10: 0.360 / 0.486 / 0.898; 11: 0.368 / 0.509 / 0.901; 12: 0.360 / 0.478 / 0.897; 13: 0.367 / 0.512 / 0.901; 14: 0.363 / 0.508 / 0.898; 15: 0.369 / 0.519 / 0.902
- 7d: 1: 0.360 / 0.530 / 0.897; 2: 0.348 / 0.495 / 0.902; 3: 0.350 / 0.507 / 0.900; 4: 0.348 / 0.502 / 0.900; 5: 0.349 / 0.513 / 0.903; 6: 0.346 / 0.506 / 0.900; 7: 0.348 / 0.500 / 0.903; 8: 0.346 / 0.509 / 0.903; 9: 0.346 / 0.502 / 0.902; 10: 0.345 / 0.498 / 0.902; 11: 0.345 / 0.502 / 0.903; 12: 0.344 / 0.495 / 0.902; 13: 0.346 / 0.505 / 0.903; 14: 0.344 / 0.500 / 0.902; 15: 0.346 / 0.508 / 0.903
- 30d: 1: 0.363 / 0.530 / 0.898; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.350 / 0.505 / 0.901; 6: 0.348 / 0.501 / 0.900; 7: 0.348 / 0.500 / 0.901; 8: 0.348 / 0.503 / 0.901; 9: 0.347 / 0.499 / 0.901; 10: 0.348 / 0.504 / 0.901; 11: 0.345 / 0.497 / 0.901; 12: 0.347 / 0.501 / 0.901; 13: 0.347 / 0.502 / 0.901; 14: 0.346 / 0.500 / 0.900; 15: 0.347 / 0.502 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.215 (body 0.169, range 0.260); 'price stays where it was' would score 0.219; colour right 0.483; typical miss of the close 4.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.121 (body 0.086, range 0.157); 'price stays where it was' would score 0.124; colour right 0.510; typical miss of the close 8.8 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.123 (body 0.085, range 0.160); 'price stays where it was' would score 0.117; colour right 0.499; typical miss of the close 10.4 bp; chain ended on the right side 0.427 of 96 chains; n=1440
- 7d: match 0.124 (body 0.085, range 0.162); 'price stays where it was' would score 0.126; colour right 0.503; typical miss of the close 8.2 bp; chain ended on the right side 0.490 of 672 chains; n=10080
- 30d: match 0.124 (body 0.085, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.0 bp; chain ended on the right side 0.513 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.1; 2: 0.199 / 4.8; 3: 0.168 / 6.3; 4: 0.131 / 6.7; 5: 0.125 / 7.4; 6: 0.114 / 8.0; 7: 0.111 / 8.3; 8: 0.098 / 9.0; 9: 0.089 / 8.9; 10: 0.089 / 9.5; 11: 0.085 / 9.9; 12: 0.076 / 10.3; 13: 0.068 / 10.4; 14: 0.070 / 11.0; 15: 0.062 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 132916, probability skill vs chance 0.2196, widened contest next: True
  - now: threshold 0.8393, hit rate recent 0.8844 / long run 0.9304
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.270, naive rule 0.460, lift 3.08x
    - 24h: 64 calls (64 a day), hit rate 0.891, chance 0.270, naive rule 0.441, lift 3.30x
    - 7d: 434 calls (62 a day), hit rate 0.926, chance 0.291, naive rule 0.494, lift 3.19x
    - 30d: 1749 calls (58 a day), hit rate 0.933, chance 0.294, naive rule 0.494, lift 3.17x
  - next: threshold 0.5627, hit rate recent 0.5694 / long run 0.5978
    - 6h: 14 calls (57 a day), hit rate 0.571, chance 0.270, lift 2.11x
    - 24h: 94 calls (94 a day), hit rate 0.574, chance 0.270, lift 2.13x
    - 7d: 852 calls (122 a day), hit rate 0.597, chance 0.291, lift 2.05x
    - 30d: 3046 calls (102 a day), hit rate 0.587, chance 0.294, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.497; 0.35: 535, 0.522; 0.40: 474, 0.580; 0.45: 405, 0.651; 0.50: 355, 0.700; 0.55: 310, 0.743; 0.60: 262, 0.787; 0.65: 220, 0.812; 0.70: 174, 0.844; 0.75: 138, 0.878; 0.80: 93, 0.910; 0.85: 47, 0.946; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 500, 0.464; 0.40: 405, 0.499; 0.45: 307, 0.534; 0.50: 199, 0.571; 0.55: 90, 0.574; 0.60: 12, 0.649; 0.65: 1, 0.652
- **K=5**: model 1792540800, labels learned 132914, probability skill vs chance 0.2164, widened contest next: True
  - now: threshold 0.6911, hit rate recent 0.776 / long run 0.816
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.177, naive rule 0.361, lift 3.88x
    - 24h: 66 calls (66 a day), hit rate 0.788, chance 0.174, naive rule 0.358, lift 4.52x
    - 7d: 439 calls (63 a day), hit rate 0.813, chance 0.187, naive rule 0.411, lift 4.34x
    - 30d: 1645 calls (55 a day), hit rate 0.817, chance 0.188, naive rule 0.405, lift 4.35x
  - next: threshold 0.4533, hit rate recent 0.5141 / long run 0.5093
    - 6h: 15 calls (61 a day), hit rate 0.400, chance 0.177, lift 2.26x
    - 24h: 65 calls (65 a day), hit rate 0.492, chance 0.174, lift 2.82x
    - 7d: 395 calls (56 a day), hit rate 0.534, chance 0.187, lift 2.85x
    - 30d: 2748 calls (92 a day), hit rate 0.480, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 347, 0.492; 0.40: 280, 0.566; 0.45: 229, 0.618; 0.50: 183, 0.665; 0.55: 144, 0.702; 0.60: 110, 0.749; 0.65: 77, 0.787; 0.70: 50, 0.819; 0.75: 29, 0.862; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.387; 0.35: 256, 0.421; 0.40: 160, 0.460; 0.45: 68, 0.483; 0.50: 13, 0.500; 0.55: 1, 0.486
- **K=8**: model 1793059200, labels learned 132911, probability skill vs chance 0.2035, widened contest next: True
  - now: threshold 0.5727, hit rate recent 0.6485 / long run 0.6886
    - 6h: 18 calls (74 a day), hit rate 0.556, chance 0.099, naive rule 0.265, lift 5.64x
    - 24h: 64 calls (64 a day), hit rate 0.656, chance 0.121, naive rule 0.320, lift 5.44x
    - 7d: 394 calls (56 a day), hit rate 0.703, chance 0.124, naive rule 0.347, lift 5.65x
    - 30d: 1604 calls (53 a day), hit rate 0.684, chance 0.121, naive rule 0.334, lift 5.65x
  - next: threshold 0.3635, hit rate recent 0.4711 / long run 0.4197
    - 6h: 16 calls (66 a day), hit rate 0.438, chance 0.099, lift 4.44x
    - 24h: 54 calls (54 a day), hit rate 0.463, chance 0.121, lift 3.84x
    - 7d: 565 calls (81 a day), hit rate 0.437, chance 0.124, lift 3.52x
    - 30d: 2809 calls (94 a day), hit rate 0.392, chance 0.121, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 191, 0.499; 0.40: 150, 0.544; 0.45: 115, 0.592; 0.50: 85, 0.638; 0.55: 62, 0.673; 0.60: 42, 0.705; 0.65: 24, 0.779; 0.70: 12, 0.810; 0.75: 2, 0.767
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.360; 0.35: 92, 0.389; 0.40: 27, 0.424; 0.45: 5, 0.460; 0.50: 1, 0.680
- **K=13**: model 1793577600, labels learned 132906, probability skill vs chance 0.1895, widened contest next: False
  - now: threshold 0.4482, hit rate recent 0.5607 / long run 0.5662
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.070, naive rule 0.260, lift 9.24x
    - 24h: 55 calls (56 a day), hit rate 0.564, chance 0.081, naive rule 0.277, lift 6.95x
    - 7d: 423 calls (61 a day), hit rate 0.579, chance 0.080, naive rule 0.295, lift 7.23x
    - 30d: 1678 calls (56 a day), hit rate 0.561, chance 0.077, naive rule 0.280, lift 7.25x
  - next: threshold 0.288, hit rate recent 0.426 / long run 0.3391
    - 6h: 15 calls (63 a day), hit rate 0.400, chance 0.070, lift 5.75x
    - 24h: 59 calls (60 a day), hit rate 0.458, chance 0.081, lift 5.65x
    - 7d: 354 calls (51 a day), hit rate 0.362, chance 0.080, lift 4.51x
    - 30d: 1879 calls (63 a day), hit rate 0.327, chance 0.077, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.440; 0.35: 93, 0.493; 0.40: 66, 0.546; 0.45: 44, 0.588; 0.50: 30, 0.649; 0.55: 19, 0.682; 0.60: 10, 0.726; 0.65: 3, 0.713; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.331; 0.35: 13, 0.362; 0.40: 3, 0.427; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.238 | 3.96% | 0.900 | 0.533 | 0.249 | 0.583 | 0.006 |
| 6h | 11.841 | 1.75% | 0.900 | 0.486 | 0.251 | 0.493 | 0.200 |
| 24h | 15.483 | 3.87% | 0.892 | 0.498 | 0.250 | 0.499 | 0.603 |
| 7d | 14.864 | 4.97% | 0.900 | 0.499 | 0.250 | 0.508 | 0.745 |
| 30d | 14.308 | 4.32% | 0.900 | 0.499 | 0.250 | 0.498 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.660 | 10.253 | 10.277 | 10.275 | 10.289 | 10.497 | 10.190 | 10.181 | 10.196 | 10.238 |
| 6h | 12.051 | 11.858 | 11.874 | 11.870 | 11.885 | 12.130 | 11.819 | 11.816 | 11.812 | 11.841 |
| 24h | 16.107 | 15.564 | 15.616 | 15.614 | 15.674 | 15.816 | 15.470 | 15.456 | 15.462 | 15.483 |
| 7d | 15.641 | 15.031 | 14.992 | 14.910 | 15.190 | 15.181 | 14.848 | 14.835 | 14.840 | 14.864 |
| 30d | 14.955 | 14.456 | 14.404 | 14.341 | 14.571 | 14.520 | 14.301 | 14.279 | 14.282 | 14.308 |

## Next candle

- candle starting 2026-11-03 11:22 UTC, last close 2264.66
- P(up) 0.5183, return quantiles (bp): {'05': -6.779, '10': -4.987, '25': -2.674, '40': -0.712, '50': 0.155, '60': 1.18, '75': 2.689, '90': 5.254, '95': 7.084}
- changepoint probability 0.049, regime age 379.1 min
- agent weights: empirical 0.012, ewma 0.138, garch 0.110, har 0.118, bocpd 0.063, hmm 0.019, online_qr 0.253, lgbm 0.288

## Learning log

- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.67, 6.48, 20.04], current probabilities: [0.086, 0.907, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-11-03 11:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.26, 'l_abs': 0.649, 'l_hi': 0.717, 'l_lo': 0.749, 'b05': 0.719, 'b25': 0.581, 'b75': 0.652, 'b95': 0.714}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 2.0], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.015, 2.094, 2.149, 1.68, 3.164, 2.077, 2.181, 2.318, 2.352, 2.375, 3.036, 2.698, 3.227, 3.152]}
- calibration offsets (in sigma): {'05': -0.0095, '10': 0.011, '25': -0.0275, '40': 0.034, '50': 0.025, '60': 0.046, '75': 0.0375, '90': 0.019, '95': 0.0495}
