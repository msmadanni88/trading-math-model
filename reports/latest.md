# ETH-USD 60s candle generator - report

- generated: 2026-11-26 02:16 UTC
- last closed candle: 2026-11-26 02:16 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.501 (672) [0.473, 0.531] | 0.510 (2879) [0.495, 0.525] | 0.514 (8153) [0.504, 0.525] | 0.516 (5181) [0.502, 0.529] | 0.667 (9) | 0.500 | flat -0.026 (noise 0.027) |
| colour_clear | 0.556 (787) | 0.551 (5509) [0.540, 0.561] | 0.543 (23788) [0.536, 0.549] | 0.527 (66905) [0.522, 0.532] | 0.544 (42667) [0.540, 0.548] | 0.595 (74) | 0.500 | flat +0.005 (noise 0.009) |
| colour_confident | 0.589 (168) | 0.575 (1312) [0.560, 0.586] | 0.569 (4450) [0.559, 0.579] | 0.584 (8071) [0.575, 0.593] | 0.584 (8071) [0.575, 0.593] | 0.769 (13) | 0.500 | flat +0.021 (noise 0.021) |
| colour_next | 0.535 (1434) | 0.535 (10048) [0.529, 0.542] | 0.531 (42904) [0.527, 0.536] | 0.520 (121526) [0.516, 0.523] | 0.530 (77177) [0.528, 0.534] | 0.515 (136) | 0.500 | flat +0.002 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.502 (140672) [0.500, 0.504] | 0.502 (600656) [0.501, 0.503] | 0.501 (1701364) [0.500, 0.502] | 0.501 (1080478) [0.500, 0.502] | 0.493 (1904) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.521 (48) | 0.576 (387) [0.526, 0.618] | 0.598 (1172) [0.576, 0.619] | 0.616 (2166) [0.599, 0.631] | 0.616 (2166) [0.599, 0.631] | 0.667 (3) | 0.500 | flat -0.014 (noise 0.039) |
| reversal_k13_next | 0.297 (74) | 0.357 (414) [0.315, 0.413] | 0.339 (1827) [0.321, 0.358] | 0.318 (5570) [0.308, 0.327] | 0.328 (3465) [0.317, 0.340] | 0.200 (5) | 0.078 | flat +0.047 (noise 0.037) |
| reversal_k13_now | 0.711 (45) | 0.611 (360) [0.559, 0.667] | 0.586 (1600) [0.565, 0.608] | 0.576 (4376) [0.564, 0.589] | 0.574 (2904) [0.558, 0.590] | 1.000 (2) | 0.078 | flat +0.041 (noise 0.047) |
| reversal_k3_next | 0.588 (131) | 0.592 (999) [0.565, 0.619] | 0.599 (2729) [0.586, 0.612] | 0.590 (7488) [0.581, 0.597] | 0.591 (5048) [0.581, 0.600] | 0.412 (17) | 0.294 | flat -0.011 (noise 0.029) |
| reversal_k3_now | 0.923 (65) | 0.922 (425) [0.911, 0.935] | 0.929 (1754) [0.921, 0.937] | 0.935 (4880) [0.929, 0.940] | 0.931 (3117) [0.924, 0.937] | 1.000 (2) | 0.294 | flat -0.021 (noise 0.018) |
| reversal_k5_next | 0.446 (56) | 0.510 (359) [0.459, 0.575] | 0.510 (1708) [0.488, 0.532] | 0.486 (6261) [0.475, 0.497] | 0.483 (4271) [0.469, 0.497] | 0.333 (3) | 0.187 | flat +0.029 (noise 0.047) |
| reversal_k5_now | 0.784 (74) | 0.816 (440) [0.797, 0.834] | 0.794 (1804) [0.778, 0.809] | 0.816 (4678) [0.807, 0.826] | 0.805 (3067) [0.794, 0.815] | 1.000 (2) | 0.188 | flat +0.054 (noise 0.028) |
| reversal_k8_next | 0.301 (83) | 0.419 (563) [0.371, 0.470] | 0.420 (2207) [0.402, 0.438] | 0.399 (6623) [0.388, 0.408] | 0.400 (4517) [0.387, 0.411] | 0.364 (11) | 0.121 | flat +0.018 (noise 0.038) |
| reversal_k8_now | 0.714 (56) | 0.689 (421) [0.660, 0.718] | 0.687 (1667) [0.669, 0.704] | 0.695 (4509) [0.683, 0.706] | 0.684 (2922) [0.670, 0.699] | 1.000 (2) | 0.122 | flat +0.040 (noise 0.033) |
| overall | 0.507 (22190) | 0.507 (155373) [0.505, 0.509] | 0.506 (661735) [0.505, 0.507] | 0.504 (1875428) [0.504, 0.505] | 0.505 (1192147) [0.504, 0.506] | 0.495 (2093) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08094, 0.1176] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5351, 'levels': [{'threshold': 0.08094, 'calls_per_day': 145.8, 'win_rate': 0.582}, {'threshold': 0.1176, 'calls_per_day': 36.3, 'win_rate': 0.5725}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42904, 'rate': 0.5313}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14926 | 0.353 | 0.535 (14712) | 0.562 (1941) | 0.751 (2531) |
| volatility: normal | 14925 | 0.380 | 0.525 (14870) | 0.566 (1506) | 0.746 (2413) |
| volatility: wild | 14925 | 0.392 | 0.533 (14890) | 0.593 (1176) | 0.760 (2125) |
| session: Asia 00-08 | 15016 | 0.374 | 0.533 (14907) | 0.563 (1618) | 0.749 (2275) |
| session: Europe 08-13 | 9300 | 0.368 | 0.528 (9226) | 0.578 (1108) | 0.767 (1485) |
| session: US 13-21 | 14880 | 0.382 | 0.534 (14791) | 0.596 (1313) | 0.743 (2446) |
| session: late 21-24 | 5580 | 0.369 | 0.521 (5548) | 0.526 (584) | 0.759 (863) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.423 | 0.393 | 0.304 | 0.304 | 0.583 | 0.335 | 0.511 | 1.244 |
| 6h | 360 | 0.387 | 0.380 | 0.283 | 0.317 | 0.532 | 0.273 | 0.501 | 1.297 |
| 24h | 1440 | 0.388 | 0.382 | 0.298 | 0.335 | 0.526 | 0.268 | 0.508 | 1.275 |
| 7d | 10080 | 0.387 | 0.380 | 0.296 | 0.331 | 0.536 | 0.268 | 0.506 | 1.211 |
| 30d | 43200 | 0.375 | 0.369 | 0.288 | 0.320 | 0.531 | 0.266 | 0.484 | 1.271 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.423 / 0.583 / 0.917; 2: 0.365 / 0.467 / 0.883; 3: 0.378 / 0.500 / 0.967; 4: 0.380 / 0.500 / 1.000; 5: 0.401 / 0.550 / 1.000; 6: 0.370 / 0.450 / 0.983; 7: 0.362 / 0.467 / 1.000; 8: 0.386 / 0.550 / 1.000; 9: 0.376 / 0.500 / 0.983; 10: 0.373 / 0.517 / 1.000; 11: 0.375 / 0.483 / 1.000; 12: 0.400 / 0.583 / 1.000; 13: 0.372 / 0.467 / 1.000; 14: 0.378 / 0.467 / 1.000; 15: 0.334 / 0.450 / 1.000
- 6h: 1: 0.387 / 0.532 / 0.919; 2: 0.362 / 0.496 / 0.869; 3: 0.373 / 0.504 / 0.925; 4: 0.368 / 0.499 / 0.969; 5: 0.369 / 0.507 / 0.936; 6: 0.370 / 0.504 / 0.886; 7: 0.373 / 0.526 / 0.972; 8: 0.364 / 0.532 / 0.986; 9: 0.357 / 0.510 / 0.894; 10: 0.361 / 0.507 / 0.978; 11: 0.348 / 0.468 / 0.942; 12: 0.364 / 0.507 / 0.919; 13: 0.351 / 0.465 / 0.886; 14: 0.349 / 0.476 / 0.981; 15: 0.343 / 0.490 / 0.975
- 24h: 1: 0.388 / 0.526 / 0.908; 2: 0.374 / 0.500 / 0.902; 3: 0.379 / 0.519 / 0.910; 4: 0.376 / 0.513 / 0.927; 5: 0.373 / 0.506 / 0.908; 6: 0.370 / 0.487 / 0.901; 7: 0.375 / 0.515 / 0.906; 8: 0.372 / 0.519 / 0.891; 9: 0.369 / 0.494 / 0.899; 10: 0.372 / 0.510 / 0.899; 11: 0.369 / 0.502 / 0.902; 12: 0.373 / 0.520 / 0.897; 13: 0.368 / 0.492 / 0.898; 14: 0.364 / 0.490 / 0.899; 15: 0.363 / 0.489 / 0.889
- 7d: 1: 0.387 / 0.536 / 0.900; 2: 0.371 / 0.492 / 0.901; 3: 0.373 / 0.506 / 0.901; 4: 0.370 / 0.497 / 0.902; 5: 0.374 / 0.508 / 0.903; 6: 0.370 / 0.499 / 0.901; 7: 0.371 / 0.503 / 0.902; 8: 0.370 / 0.510 / 0.899; 9: 0.368 / 0.499 / 0.902; 10: 0.371 / 0.515 / 0.900; 11: 0.369 / 0.504 / 0.904; 12: 0.369 / 0.503 / 0.902; 13: 0.365 / 0.492 / 0.901; 14: 0.366 / 0.498 / 0.899; 15: 0.366 / 0.501 / 0.900
- 30d: 1: 0.375 / 0.531 / 0.898; 2: 0.361 / 0.491 / 0.900; 3: 0.365 / 0.512 / 0.901; 4: 0.361 / 0.497 / 0.900; 5: 0.363 / 0.506 / 0.900; 6: 0.360 / 0.501 / 0.900; 7: 0.361 / 0.502 / 0.900; 8: 0.361 / 0.508 / 0.900; 9: 0.359 / 0.500 / 0.900; 10: 0.360 / 0.505 / 0.900; 11: 0.360 / 0.506 / 0.901; 12: 0.359 / 0.503 / 0.901; 13: 0.358 / 0.499 / 0.900; 14: 0.358 / 0.502 / 0.900; 15: 0.358 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.195 (body 0.114, range 0.276); 'price stays where it was' would score 0.226; colour right 0.483; typical miss of the close 8.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.155 (body 0.106, range 0.203); 'price stays where it was' would score 0.182; colour right 0.493; typical miss of the close 11.1 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.117 (body 0.075, range 0.160); 'price stays where it was' would score 0.151; colour right 0.497; typical miss of the close 16.8 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.135 (body 0.087, range 0.183); 'price stays where it was' would score 0.144; colour right 0.502; typical miss of the close 14.2 bp; chain ended on the right side 0.504 of 672 chains; n=10080
- 30d: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 11.0 bp; chain ended on the right side 0.510 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 5.9; 2: 0.206 / 6.7; 3: 0.164 / 8.7; 4: 0.136 / 9.1; 5: 0.124 / 9.9; 6: 0.119 / 10.7; 7: 0.116 / 11.2; 8: 0.102 / 12.1; 9: 0.093 / 12.9; 10: 0.089 / 13.1; 11: 0.088 / 13.7; 12: 0.083 / 13.9; 13: 0.076 / 14.8; 14: 0.070 / 15.1; 15: 0.067 / 15.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 165490, probability skill vs chance 0.2282, widened contest next: False
  - now: threshold 0.8318, hit rate recent 0.9081 / long run 0.9285
    - 6h: 15 calls (61 a day), hit rate 0.867, chance 0.289, naive rule 0.491, lift 3.00x
    - 24h: 59 calls (59 a day), hit rate 0.915, chance 0.302, naive rule 0.510, lift 3.03x
    - 7d: 420 calls (60 a day), hit rate 0.924, chance 0.300, naive rule 0.518, lift 3.08x
    - 30d: 1749 calls (58 a day), hit rate 0.929, chance 0.294, naive rule 0.503, lift 3.16x
  - next: threshold 0.5344, hit rate recent 0.5598 / long run 0.5886
    - 6h: 35 calls (142 a day), hit rate 0.571, chance 0.289, lift 1.98x
    - 24h: 136 calls (136 a day), hit rate 0.588, chance 0.302, lift 1.95x
    - 7d: 1008 calls (144 a day), hit rate 0.587, chance 0.300, lift 1.96x
    - 30d: 2735 calls (91 a day), hit rate 0.597, chance 0.294, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.503; 0.35: 530, 0.527; 0.40: 482, 0.571; 0.45: 419, 0.634; 0.50: 368, 0.681; 0.55: 320, 0.725; 0.60: 271, 0.772; 0.65: 227, 0.803; 0.70: 178, 0.834; 0.75: 142, 0.870; 0.80: 95, 0.901; 0.85: 42, 0.941; 0.90: 3, 0.959
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 486, 0.470; 0.40: 384, 0.510; 0.45: 290, 0.542; 0.50: 187, 0.570; 0.55: 78, 0.587; 0.60: 10, 0.636; 0.65: 0, 0.538
- **K=5**: model 1794528000, labels learned 165488, probability skill vs chance 0.2191, widened contest next: False
  - now: threshold 0.7041, hit rate recent 0.8166 / long run 0.7979
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.166, naive rule 0.351, lift 5.53x
    - 24h: 70 calls (70 a day), hit rate 0.786, chance 0.183, naive rule 0.414, lift 4.30x
    - 7d: 434 calls (62 a day), hit rate 0.818, chance 0.194, naive rule 0.435, lift 4.21x
    - 30d: 1798 calls (60 a day), hit rate 0.795, chance 0.188, naive rule 0.416, lift 4.23x
  - next: threshold 0.4503, hit rate recent 0.4776 / long run 0.4973
    - 6h: 11 calls (45 a day), hit rate 0.455, chance 0.166, lift 2.74x
    - 24h: 55 calls (55 a day), hit rate 0.455, chance 0.183, lift 2.49x
    - 7d: 356 calls (51 a day), hit rate 0.508, chance 0.194, lift 2.62x
    - 30d: 1704 calls (57 a day), hit rate 0.510, chance 0.188, lift 2.71x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.425; 0.35: 364, 0.474; 0.40: 295, 0.542; 0.45: 239, 0.602; 0.50: 186, 0.654; 0.55: 149, 0.686; 0.60: 116, 0.730; 0.65: 85, 0.767; 0.70: 54, 0.802; 0.75: 27, 0.841; 0.80: 6, 0.843
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 331, 0.396; 0.35: 246, 0.433; 0.40: 157, 0.459; 0.45: 63, 0.508; 0.50: 8, 0.563; 0.55: 1, 0.556
- **K=8**: model 1794960000, labels learned 165485, probability skill vs chance 0.2214, widened contest next: True
  - now: threshold 0.5876, hit rate recent 0.7274 / long run 0.6832
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.107, naive rule 0.308, lift 5.33x
    - 24h: 51 calls (51 a day), hit rate 0.725, chance 0.126, naive rule 0.352, lift 5.78x
    - 7d: 417 calls (60 a day), hit rate 0.693, chance 0.126, naive rule 0.369, lift 5.49x
    - 30d: 1661 calls (55 a day), hit rate 0.688, chance 0.124, naive rule 0.351, lift 5.55x
  - next: threshold 0.3654, hit rate recent 0.3432 / long run 0.4102
    - 6h: 28 calls (115 a day), hit rate 0.286, chance 0.107, lift 2.67x
    - 24h: 88 calls (89 a day), hit rate 0.318, chance 0.126, lift 2.53x
    - 7d: 568 calls (81 a day), hit rate 0.419, chance 0.126, lift 3.32x
    - 30d: 2210 calls (74 a day), hit rate 0.419, chance 0.124, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.427; 0.35: 203, 0.487; 0.40: 159, 0.538; 0.45: 121, 0.582; 0.50: 87, 0.637; 0.55: 63, 0.675; 0.60: 43, 0.717; 0.65: 24, 0.768; 0.70: 10, 0.804; 0.75: 1, 0.737
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.377; 0.35: 84, 0.409; 0.40: 29, 0.442; 0.45: 7, 0.483; 0.50: 1, 0.686
- **K=13**: model 1795478400, labels learned 165480, probability skill vs chance 0.2081, widened contest next: True
  - now: threshold 0.4582, hit rate recent 0.6932 / long run 0.5936
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.075, naive rule 0.276, lift 9.48x
    - 24h: 43 calls (43 a day), hit rate 0.721, chance 0.091, naive rule 0.353, lift 7.90x
    - 7d: 356 calls (51 a day), hit rate 0.615, chance 0.084, naive rule 0.325, lift 7.34x
    - 30d: 1596 calls (53 a day), hit rate 0.586, chance 0.081, naive rule 0.302, lift 7.28x
  - next: threshold 0.3022, hit rate recent 0.3049 / long run 0.3388
    - 6h: 17 calls (71 a day), hit rate 0.118, chance 0.075, lift 1.56x
    - 24h: 73 calls (74 a day), hit rate 0.288, chance 0.091, lift 3.15x
    - 7d: 411 calls (59 a day), hit rate 0.355, chance 0.084, lift 4.24x
    - 30d: 1826 calls (61 a day), hit rate 0.339, chance 0.081, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 142, 0.428; 0.35: 104, 0.477; 0.40: 72, 0.541; 0.45: 51, 0.591; 0.50: 35, 0.628; 0.55: 22, 0.649; 0.60: 10, 0.671; 0.65: 2, 0.532
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.344; 0.35: 15, 0.382; 0.40: 2, 0.444; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.472 | 2.75% | 0.917 | 0.550 | 0.247 | 0.567 | 0.212 |
| 6h | 20.052 | 5.26% | 0.922 | 0.539 | 0.250 | 0.540 | 0.538 |
| 24h | 27.234 | 4.66% | 0.908 | 0.502 | 0.250 | 0.510 | 0.600 |
| 7d | 25.570 | 4.50% | 0.900 | 0.500 | 0.250 | 0.513 | 0.657 |
| 30d | 20.095 | 4.80% | 0.900 | 0.500 | 0.250 | 0.507 | 0.706 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 20.022 | 19.914 | 19.614 | 19.691 | 20.130 | 19.627 | 19.499 | 19.406 | 19.459 | 19.472 |
| 6h | 21.165 | 20.459 | 20.316 | 20.227 | 20.898 | 20.269 | 19.900 | 19.943 | 19.992 | 20.052 |
| 24h | 28.566 | 27.480 | 27.501 | 27.272 | 27.989 | 27.852 | 27.192 | 27.138 | 27.174 | 27.234 |
| 7d | 26.775 | 25.847 | 25.761 | 25.596 | 26.178 | 25.964 | 25.558 | 25.509 | 25.533 | 25.570 |
| 30d | 21.108 | 20.286 | 20.237 | 20.150 | 20.525 | 20.438 | 20.075 | 20.049 | 20.061 | 20.095 |

## Next candle

- candle starting 2026-11-26 02:16 UTC, last close 1701.11
- P(up) 0.5044, return quantiles (bp): {'05': -10.938, '10': -7.896, '25': -4.02, '40': -1.551, '50': 0.063, '60': 1.901, '75': 4.502, '90': 9.236, '95': 11.941}
- changepoint probability 0.0389, regime age 89.1 min
- agent weights: empirical 0.003, ewma 0.052, garch 0.065, har 0.138, bocpd 0.008, hmm 0.021, online_qr 0.332, lgbm 0.382

## Learning log

- 2026-11-24 00:00 UTC: {"garch": {"alpha": 0.0886, "beta": 0.9021}, "hmm": {"sd_bp": [4.97, 10.02, 31.47], "stay": [0.968, 0.952, 0.875]}, "lgbm": {"challenger_loss": 0.25051, "champion_loss": 0.25047, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48498, "challengers": 3, "chance_loss": 0.6173, "widened": true, "champion_loss": 0.48458, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37971, "challengers": 1, "chance_loss": 0.49915, "widened": false, "champion_loss": 0.37928, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27848, "challengers": 3, "chance_loss": 0.37338, "widened": true, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20281, "challengers": 3, "chance_loss": 0.28057, "widened": true, "champion_loss": 0.20335, "promoted": true}}
- 2026-11-24 12:00 UTC: {"garch": {"alpha": 0.0937, "beta": 0.8962}, "hmm": {"sd_bp": [5.06, 10.1, 31.41], "stay": [0.968, 0.948, 0.887]}}
- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- 2026-11-25 12:00 UTC: {"garch": {"alpha": 0.091, "beta": 0.8903}, "hmm": {"sd_bp": [4.89, 9.77, 34.58], "stay": [0.96, 0.954, 0.849]}}
- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.93, 9.77, 29.75], current probabilities: [0.164, 0.829, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-11-26 02:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.412, 'l_abs': 0.655, 'l_hi': 0.774, 'l_lo': 0.704, 'b05': 0.724, 'b25': 0.672, 'b75': 0.657, 'b95': 0.713}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.5], [1.3, 1.5], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.6], [1.2, 1.6], [1.2, 1.5]], 'cone_width': [1.443, 1.286, 1.711, 1.601, 2.147, 2.188, 4.535, 2.393, 4.337, 2.309, 2.566, 2.899, 5.173, 4.759]}
- calibration offsets (in sigma): {'05': 0.0975, '10': 0.095, '25': 0.0475, '40': 0.02, '50': 0.015, '60': 0.03, '75': 0.0125, '90': 0.035, '95': 0.0125}
