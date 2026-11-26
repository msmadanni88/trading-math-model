# ETH-USD 60s candle generator - report

- generated: 2026-11-26 11:04 UTC
- last closed candle: 2026-11-26 11:04 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.501 (672) [0.473, 0.531] | 0.510 (2879) [0.495, 0.525] | 0.514 (8153) [0.504, 0.525] | 0.516 (5181) [0.502, 0.529] | 0.591 (44) | 0.500 | flat -0.026 (noise 0.027) |
| colour_clear | 0.556 (787) | 0.551 (5509) [0.540, 0.561] | 0.543 (23788) [0.536, 0.549] | 0.527 (66905) [0.522, 0.532] | 0.544 (42667) [0.540, 0.548] | 0.603 (373) | 0.500 | flat +0.005 (noise 0.009) |
| colour_confident | 0.589 (168) | 0.575 (1312) [0.560, 0.586] | 0.569 (4450) [0.559, 0.579] | 0.584 (8071) [0.575, 0.593] | 0.584 (8071) [0.575, 0.593] | 0.590 (83) | 0.500 | flat +0.021 (noise 0.021) |
| colour_next | 0.535 (1434) | 0.535 (10048) [0.529, 0.542] | 0.531 (42904) [0.527, 0.536] | 0.520 (121526) [0.516, 0.523] | 0.530 (77177) [0.528, 0.534] | 0.556 (662) | 0.500 | flat +0.002 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.502 (140672) [0.500, 0.504] | 0.502 (600656) [0.501, 0.503] | 0.501 (1701364) [0.500, 0.502] | 0.501 (1080478) [0.500, 0.502] | 0.485 (9268) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.521 (48) | 0.576 (387) [0.526, 0.618] | 0.598 (1172) [0.576, 0.619] | 0.616 (2166) [0.599, 0.631] | 0.616 (2166) [0.599, 0.631] | 0.500 (22) | 0.500 | flat -0.014 (noise 0.039) |
| reversal_k13_next | 0.297 (74) | 0.357 (414) [0.315, 0.413] | 0.339 (1827) [0.321, 0.358] | 0.318 (5570) [0.308, 0.327] | 0.328 (3465) [0.317, 0.340] | 0.259 (27) | 0.078 | flat +0.047 (noise 0.037) |
| reversal_k13_now | 0.711 (45) | 0.611 (360) [0.559, 0.667] | 0.586 (1600) [0.565, 0.608] | 0.576 (4376) [0.564, 0.589] | 0.574 (2904) [0.558, 0.590] | 0.611 (18) | 0.078 | flat +0.041 (noise 0.047) |
| reversal_k3_next | 0.588 (131) | 0.592 (999) [0.565, 0.619] | 0.599 (2729) [0.586, 0.612] | 0.590 (7488) [0.581, 0.597] | 0.591 (5048) [0.581, 0.600] | 0.565 (69) | 0.294 | flat -0.011 (noise 0.029) |
| reversal_k3_now | 0.923 (65) | 0.922 (425) [0.911, 0.935] | 0.929 (1754) [0.921, 0.937] | 0.935 (4880) [0.929, 0.940] | 0.931 (3117) [0.924, 0.937] | 1.000 (18) | 0.294 | flat -0.021 (noise 0.018) |
| reversal_k5_next | 0.446 (56) | 0.510 (359) [0.459, 0.575] | 0.510 (1708) [0.488, 0.532] | 0.486 (6261) [0.475, 0.497] | 0.483 (4271) [0.469, 0.497] | 0.531 (32) | 0.187 | flat +0.029 (noise 0.047) |
| reversal_k5_now | 0.784 (74) | 0.816 (440) [0.797, 0.834] | 0.794 (1804) [0.778, 0.809] | 0.816 (4678) [0.807, 0.826] | 0.805 (3067) [0.794, 0.815] | 0.920 (25) | 0.188 | flat +0.054 (noise 0.028) |
| reversal_k8_next | 0.301 (83) | 0.419 (563) [0.371, 0.470] | 0.420 (2207) [0.402, 0.438] | 0.399 (6623) [0.388, 0.408] | 0.400 (4517) [0.387, 0.411] | 0.375 (40) | 0.121 | flat +0.018 (noise 0.038) |
| reversal_k8_now | 0.714 (56) | 0.689 (421) [0.660, 0.718] | 0.687 (1667) [0.669, 0.704] | 0.695 (4509) [0.683, 0.706] | 0.684 (2922) [0.670, 0.699] | 0.773 (22) | 0.122 | flat +0.040 (noise 0.033) |
| overall | 0.507 (22190) | 0.507 (155373) [0.505, 0.509] | 0.506 (661735) [0.505, 0.507] | 0.504 (1875428) [0.504, 0.505] | 0.505 (1192147) [0.504, 0.506] | 0.493 (10225) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08131, 0.118] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5366, 'levels': [{'threshold': 0.08131, 'calls_per_day': 145.3, 'win_rate': 0.5873}, {'threshold': 0.118, 'calls_per_day': 36.6, 'win_rate': 0.5681}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42908, 'rate': 0.5316}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15102 | 0.354 | 0.536 (14886) | 0.562 (1964) | 0.750 (2554) |
| volatility: normal | 15101 | 0.380 | 0.526 (15046) | 0.567 (1539) | 0.747 (2444) |
| volatility: wild | 15101 | 0.392 | 0.533 (15066) | 0.590 (1190) | 0.761 (2146) |
| session: Asia 00-08 | 15360 | 0.375 | 0.534 (15250) | 0.562 (1655) | 0.750 (2325) |
| session: Europe 08-13 | 9484 | 0.369 | 0.529 (9409) | 0.578 (1141) | 0.767 (1510) |
| session: US 13-21 | 14880 | 0.382 | 0.534 (14791) | 0.596 (1313) | 0.743 (2446) |
| session: late 21-24 | 5580 | 0.369 | 0.521 (5548) | 0.526 (584) | 0.759 (863) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.396 | 0.368 | 0.271 | 0.271 | 0.600 | 0.299 | 0.492 | 1.268 |
| 6h | 360 | 0.403 | 0.378 | 0.284 | 0.314 | 0.573 | 0.299 | 0.508 | 1.181 |
| 24h | 1440 | 0.391 | 0.379 | 0.296 | 0.332 | 0.537 | 0.277 | 0.505 | 1.205 |
| 7d | 10080 | 0.388 | 0.380 | 0.296 | 0.329 | 0.538 | 0.270 | 0.505 | 1.217 |
| 30d | 43200 | 0.375 | 0.369 | 0.288 | 0.320 | 0.532 | 0.266 | 0.484 | 1.272 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.396 / 0.600 / 0.900; 2: 0.364 / 0.483 / 0.917; 3: 0.372 / 0.533 / 0.833; 4: 0.377 / 0.517 / 0.833; 5: 0.372 / 0.533 / 0.867; 6: 0.362 / 0.433 / 0.917; 7: 0.368 / 0.567 / 0.867; 8: 0.352 / 0.500 / 0.950; 9: 0.362 / 0.467 / 0.817; 10: 0.375 / 0.583 / 0.900; 11: 0.360 / 0.500 / 0.767; 12: 0.387 / 0.617 / 0.800; 13: 0.348 / 0.450 / 0.817; 14: 0.365 / 0.500 / 0.900; 15: 0.354 / 0.483 / 0.883
- 6h: 1: 0.403 / 0.573 / 0.908; 2: 0.363 / 0.453 / 0.903; 3: 0.374 / 0.508 / 0.806; 4: 0.376 / 0.489 / 0.861; 5: 0.364 / 0.483 / 0.800; 6: 0.375 / 0.520 / 0.889; 7: 0.366 / 0.492 / 0.864; 8: 0.362 / 0.464 / 0.961; 9: 0.371 / 0.492 / 0.856; 10: 0.365 / 0.478 / 0.936; 11: 0.369 / 0.514 / 0.811; 12: 0.373 / 0.517 / 0.819; 13: 0.364 / 0.483 / 0.836; 14: 0.366 / 0.466 / 0.931; 15: 0.354 / 0.450 / 0.908
- 24h: 1: 0.391 / 0.537 / 0.907; 2: 0.370 / 0.485 / 0.928; 3: 0.374 / 0.496 / 0.908; 4: 0.376 / 0.512 / 0.890; 5: 0.369 / 0.493 / 0.913; 6: 0.373 / 0.499 / 0.922; 7: 0.373 / 0.510 / 0.890; 8: 0.370 / 0.508 / 0.898; 9: 0.367 / 0.491 / 0.922; 10: 0.367 / 0.492 / 0.896; 11: 0.366 / 0.495 / 0.918; 12: 0.372 / 0.507 / 0.919; 13: 0.364 / 0.481 / 0.908; 14: 0.362 / 0.481 / 0.894; 15: 0.360 / 0.484 / 0.895
- 7d: 1: 0.388 / 0.538 / 0.900; 2: 0.371 / 0.492 / 0.899; 3: 0.373 / 0.506 / 0.897; 4: 0.371 / 0.498 / 0.898; 5: 0.373 / 0.507 / 0.896; 6: 0.369 / 0.498 / 0.900; 7: 0.370 / 0.503 / 0.898; 8: 0.370 / 0.509 / 0.900; 9: 0.368 / 0.498 / 0.898; 10: 0.370 / 0.513 / 0.900; 11: 0.368 / 0.502 / 0.896; 12: 0.369 / 0.504 / 0.898; 13: 0.365 / 0.492 / 0.899; 14: 0.364 / 0.494 / 0.900; 15: 0.365 / 0.500 / 0.900
- 30d: 1: 0.375 / 0.532 / 0.899; 2: 0.362 / 0.491 / 0.900; 3: 0.365 / 0.511 / 0.899; 4: 0.361 / 0.498 / 0.900; 5: 0.363 / 0.505 / 0.900; 6: 0.360 / 0.501 / 0.900; 7: 0.361 / 0.502 / 0.900; 8: 0.361 / 0.507 / 0.901; 9: 0.359 / 0.500 / 0.900; 10: 0.360 / 0.505 / 0.900; 11: 0.360 / 0.505 / 0.900; 12: 0.360 / 0.503 / 0.900; 13: 0.358 / 0.499 / 0.900; 14: 0.358 / 0.501 / 0.901; 15: 0.358 / 0.501 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.149 (body 0.108, range 0.190); 'price stays where it was' would score 0.154; colour right 0.533; typical miss of the close 6.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.141 (body 0.094, range 0.189); 'price stays where it was' would score 0.123; colour right 0.478; typical miss of the close 8.7 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.127 (body 0.084, range 0.171); 'price stays where it was' would score 0.151; colour right 0.492; typical miss of the close 14.0 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.135 (body 0.087, range 0.183); 'price stays where it was' would score 0.144; colour right 0.501; typical miss of the close 14.1 bp; chain ended on the right side 0.506 of 672 chains; n=10080
- 30d: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 11.0 bp; chain ended on the right side 0.511 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.372 / 5.9; 2: 0.205 / 6.7; 3: 0.165 / 8.7; 4: 0.136 / 9.0; 5: 0.124 / 9.9; 6: 0.119 / 10.7; 7: 0.117 / 11.1; 8: 0.102 / 12.2; 9: 0.093 / 12.9; 10: 0.090 / 13.2; 11: 0.088 / 13.7; 12: 0.083 / 13.8; 13: 0.077 / 14.8; 14: 0.071 / 15.1; 15: 0.067 / 15.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 166018, probability skill vs chance 0.2332, widened contest next: False
  - now: threshold 0.8313, hit rate recent 0.9298 / long run 0.9304
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.334, naive rule 0.553, lift 3.00x
    - 24h: 58 calls (58 a day), hit rate 0.914, chance 0.307, naive rule 0.515, lift 2.98x
    - 7d: 414 calls (59 a day), hit rate 0.925, chance 0.301, naive rule 0.522, lift 3.07x
    - 30d: 1737 calls (58 a day), hit rate 0.929, chance 0.294, naive rule 0.504, lift 3.16x
  - next: threshold 0.5352, hit rate recent 0.5881 / long run 0.5907
    - 6h: 36 calls (146 a day), hit rate 0.611, chance 0.334, lift 1.83x
    - 24h: 145 calls (146 a day), hit rate 0.572, chance 0.307, lift 1.87x
    - 7d: 1041 calls (149 a day), hit rate 0.590, chance 0.301, lift 1.96x
    - 30d: 2737 calls (91 a day), hit rate 0.599, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.503; 0.35: 530, 0.528; 0.40: 482, 0.571; 0.45: 419, 0.634; 0.50: 368, 0.681; 0.55: 321, 0.725; 0.60: 271, 0.771; 0.65: 227, 0.802; 0.70: 178, 0.834; 0.75: 142, 0.870; 0.80: 94, 0.900; 0.85: 42, 0.941; 0.90: 3, 0.958
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 486, 0.470; 0.40: 383, 0.510; 0.45: 290, 0.543; 0.50: 187, 0.571; 0.55: 78, 0.590; 0.60: 10, 0.640; 0.65: 0, 0.538
- **K=5**: model 1794528000, labels learned 166016, probability skill vs chance 0.2199, widened contest next: False
  - now: threshold 0.704, hit rate recent 0.8464 / long run 0.8022
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.204, naive rule 0.452, lift 4.60x
    - 24h: 68 calls (68 a day), hit rate 0.838, chance 0.181, naive rule 0.408, lift 4.62x
    - 7d: 435 calls (62 a day), hit rate 0.818, chance 0.194, naive rule 0.437, lift 4.21x
    - 30d: 1796 calls (60 a day), hit rate 0.795, chance 0.188, naive rule 0.416, lift 4.22x
  - next: threshold 0.4483, hit rate recent 0.5058 / long run 0.4999
    - 6h: 22 calls (90 a day), hit rate 0.591, chance 0.204, lift 2.90x
    - 24h: 70 calls (70 a day), hit rate 0.500, chance 0.181, lift 2.76x
    - 7d: 372 calls (53 a day), hit rate 0.511, chance 0.194, lift 2.63x
    - 30d: 1711 calls (57 a day), hit rate 0.510, chance 0.188, lift 2.71x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.426; 0.35: 364, 0.474; 0.40: 295, 0.541; 0.45: 239, 0.602; 0.50: 186, 0.654; 0.55: 149, 0.685; 0.60: 116, 0.730; 0.65: 85, 0.766; 0.70: 54, 0.802; 0.75: 27, 0.839; 0.80: 6, 0.841
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 331, 0.396; 0.35: 246, 0.433; 0.40: 156, 0.460; 0.45: 63, 0.508; 0.50: 9, 0.568; 0.55: 1, 0.529
- **K=8**: model 1794960000, labels learned 166013, probability skill vs chance 0.2184, widened contest next: True
  - now: threshold 0.587, hit rate recent 0.7302 / long run 0.6853
    - 6h: 16 calls (66 a day), hit rate 0.750, chance 0.111, naive rule 0.345, lift 6.73x
    - 24h: 53 calls (53 a day), hit rate 0.717, chance 0.121, naive rule 0.352, lift 5.91x
    - 7d: 415 calls (59 a day), hit rate 0.687, chance 0.126, naive rule 0.368, lift 5.47x
    - 30d: 1662 calls (55 a day), hit rate 0.686, chance 0.124, naive rule 0.351, lift 5.55x
  - next: threshold 0.373, hit rate recent 0.3533 / long run 0.4087
    - 6h: 17 calls (70 a day), hit rate 0.353, chance 0.111, lift 3.17x
    - 24h: 96 calls (97 a day), hit rate 0.333, chance 0.121, lift 2.75x
    - 7d: 573 calls (82 a day), hit rate 0.410, chance 0.126, lift 3.27x
    - 30d: 2205 calls (74 a day), hit rate 0.420, chance 0.124, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.426; 0.35: 204, 0.487; 0.40: 159, 0.538; 0.45: 120, 0.582; 0.50: 87, 0.636; 0.55: 64, 0.674; 0.60: 43, 0.716; 0.65: 25, 0.768; 0.70: 10, 0.803; 0.75: 1, 0.737
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.377; 0.35: 84, 0.409; 0.40: 30, 0.440; 0.45: 7, 0.488; 0.50: 1, 0.694
- **K=13**: model 1795478400, labels learned 166008, probability skill vs chance 0.203, widened contest next: True
  - now: threshold 0.457, hit rate recent 0.6628 / long run 0.5928
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.091, naive rule 0.364, lift 6.39x
    - 24h: 46 calls (46 a day), hit rate 0.674, chance 0.088, naive rule 0.345, lift 7.68x
    - 7d: 350 calls (50 a day), hit rate 0.611, chance 0.084, naive rule 0.327, lift 7.27x
    - 30d: 1594 calls (53 a day), hit rate 0.585, chance 0.081, naive rule 0.302, lift 7.24x
  - next: threshold 0.3076, hit rate recent 0.295 / long run 0.3365
    - 6h: 13 calls (54 a day), hit rate 0.231, chance 0.091, lift 2.53x
    - 24h: 70 calls (71 a day), hit rate 0.271, chance 0.088, lift 3.09x
    - 7d: 406 calls (58 a day), hit rate 0.355, chance 0.084, lift 4.22x
    - 30d: 1833 calls (61 a day), hit rate 0.337, chance 0.081, lift 4.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 143, 0.429; 0.35: 104, 0.477; 0.40: 72, 0.541; 0.45: 51, 0.589; 0.50: 35, 0.624; 0.55: 22, 0.646; 0.60: 10, 0.665; 0.65: 2, 0.532
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.341; 0.35: 15, 0.382; 0.40: 2, 0.452

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.751 | 9.11% | 0.917 | 0.500 | 0.252 | 0.467 | 0.142 |
| 6h | 14.561 | 7.69% | 0.903 | 0.492 | 0.250 | 0.528 | 0.399 |
| 24h | 24.982 | 6.53% | 0.906 | 0.496 | 0.250 | 0.513 | 0.665 |
| 7d | 25.532 | 4.66% | 0.900 | 0.500 | 0.250 | 0.514 | 0.659 |
| 30d | 20.110 | 4.86% | 0.900 | 0.500 | 0.250 | 0.507 | 0.706 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.030 | 12.623 | 12.700 | 12.750 | 12.797 | 12.744 | 12.739 | 12.682 | 12.688 | 12.751 |
| 6h | 15.773 | 14.636 | 14.638 | 14.576 | 14.930 | 14.765 | 14.568 | 14.513 | 14.535 | 14.561 |
| 24h | 26.727 | 25.187 | 25.189 | 25.035 | 25.656 | 25.578 | 24.950 | 24.907 | 24.930 | 24.982 |
| 7d | 26.781 | 25.810 | 25.723 | 25.559 | 26.149 | 25.925 | 25.523 | 25.469 | 25.495 | 25.532 |
| 30d | 21.136 | 20.301 | 20.253 | 20.165 | 20.542 | 20.454 | 20.091 | 20.065 | 20.076 | 20.110 |

## Next candle

- candle starting 2026-11-26 11:04 UTC, last close 1691.97
- P(up) 0.5282, return quantiles (bp): {'05': -7.614, '10': -5.692, '25': -2.872, '40': -0.77, '50': 0.294, '60': 1.253, '75': 3.012, '90': 5.425, '95': 7.387}
- changepoint probability 0.0273, regime age 190.2 min
- agent weights: empirical 0.003, ewma 0.106, garch 0.108, har 0.174, bocpd 0.022, hmm 0.050, online_qr 0.241, lgbm 0.297

## Learning log

- 2026-11-24 00:00 UTC: {"garch": {"alpha": 0.0886, "beta": 0.9021}, "hmm": {"sd_bp": [4.97, 10.02, 31.47], "stay": [0.968, 0.952, 0.875]}, "lgbm": {"challenger_loss": 0.25051, "champion_loss": 0.25047, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48498, "challengers": 3, "chance_loss": 0.6173, "widened": true, "champion_loss": 0.48458, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37971, "challengers": 1, "chance_loss": 0.49915, "widened": false, "champion_loss": 0.37928, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27848, "challengers": 3, "chance_loss": 0.37338, "widened": true, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20281, "challengers": 3, "chance_loss": 0.28057, "widened": true, "champion_loss": 0.20335, "promoted": true}}
- 2026-11-24 12:00 UTC: {"garch": {"alpha": 0.0937, "beta": 0.8962}, "hmm": {"sd_bp": [5.06, 10.1, 31.41], "stay": [0.968, 0.948, 0.887]}}
- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- 2026-11-25 12:00 UTC: {"garch": {"alpha": 0.091, "beta": 0.8903}, "hmm": {"sd_bp": [4.89, 9.77, 34.58], "stay": [0.96, 0.954, 0.849]}}
- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.93, 9.77, 29.75], current probabilities: [0.949, 0.05, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-26 11:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.413, 'l_abs': 0.627, 'l_hi': 0.77, 'l_lo': 0.711, 'b05': 0.694, 'b25': 0.657, 'b75': 0.633, 'b95': 0.697}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.5], [1.3, 1.5], [1.2, 1.6], [1.3, 1.5], [1.3, 1.6], [1.3, 1.6], [1.2, 1.5], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.285, 3.305, 2.366, 3.954, 2.479, 2.965, 2.129, 3.584, 2.39, 5.479, 4.886, 4.09, 2.967, 3.267]}
- calibration offsets (in sigma): {'05': 0.0515, '10': 0.053, '25': 0.0175, '40': 0.032, '50': 0.045, '60': 0.008, '75': -0.0075, '90': -0.103, '95': -0.0815}
