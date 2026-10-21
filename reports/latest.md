# ETH-USD 60s candle generator - report

- generated: 2026-10-21 07:24 UTC
- last closed candle: 2026-10-21 07:24 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.534 (672) [0.497, 0.571] | 0.521 (2876) [0.502, 0.539] | 0.514 (4698) [0.498, 0.528] | 0.518 (1726) [0.491, 0.545] | 0.655 (29) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.579 (848) | 0.556 (5623) [0.548, 0.565] | 0.526 (23426) [0.517, 0.535] | 0.515 (38261) [0.508, 0.522] | 0.547 (14023) [0.541, 0.553] | 0.563 (261) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.579 (209) | 0.594 (870) [0.572, 0.620] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.610 (59) | 0.500 | flat -0.011 (noise 0.023) |
| colour_next | 0.548 (1439) | 0.535 (10025) [0.526, 0.543] | 0.517 (42863) [0.512, 0.524] | 0.511 (70022) [0.507, 0.516] | 0.530 (25673) [0.525, 0.535] | 0.529 (442) | 0.500 | flat +0.012 (noise 0.007) |
| colour_path | 0.493 (20146) | 0.500 (140350) [0.496, 0.504] | 0.501 (600082) [0.499, 0.502] | 0.500 (980308) [0.499, 0.501] | 0.500 (359422) [0.498, 0.502] | 0.504 (6188) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.691 (55) | 0.629 (210) [0.581, 0.672] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.529 (17) | 0.500 | flat -0.047 (noise 0.045) |
| reversal_k13_next | 0.355 (76) | 0.315 (445) [0.298, 0.330] | 0.308 (2119) [0.296, 0.320] | 0.307 (3377) [0.296, 0.319] | 0.320 (1272) [0.308, 0.332] | 0.450 (20) | 0.077 | flat -0.007 (noise 0.030) |
| reversal_k13_now | 0.510 (51) | 0.519 (391) [0.491, 0.550] | 0.571 (1553) [0.551, 0.591] | 0.574 (2457) [0.557, 0.590] | 0.562 (985) [0.538, 0.588] | 0.500 (10) | 0.077 | flat -0.070 (noise 0.036) |
| reversal_k3_next | 0.533 (122) | 0.562 (737) [0.550, 0.573] | 0.571 (2652) [0.559, 0.584] | 0.580 (4203) [0.570, 0.591] | 0.570 (1763) [0.557, 0.585] | 0.783 (46) | 0.292 | flat -0.005 (noise 0.026) |
| reversal_k3_now | 0.912 (57) | 0.930 (384) [0.906, 0.954] | 0.933 (1700) [0.925, 0.943] | 0.936 (2794) [0.929, 0.944] | 0.927 (1031) [0.917, 0.938] | 0.938 (16) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.380 (129) | 0.439 (878) [0.415, 0.464] | 0.462 (2498) [0.447, 0.478] | 0.473 (3789) [0.460, 0.488] | 0.450 (1799) [0.434, 0.469] | 0.605 (38) | 0.187 | flat -0.029 (noise 0.028) |
| reversal_k5_now | 0.840 (50) | 0.823 (355) [0.796, 0.846] | 0.827 (1584) [0.813, 0.841] | 0.831 (2563) [0.819, 0.843] | 0.821 (952) [0.804, 0.838] | 0.769 (13) | 0.187 | flat +0.013 (noise 0.029) |
| reversal_k8_next | 0.376 (109) | 0.362 (730) [0.337, 0.384] | 0.387 (2335) [0.372, 0.401] | 0.389 (3770) [0.377, 0.402] | 0.380 (1664) [0.363, 0.398] | 0.441 (34) | 0.121 | flat -0.025 (noise 0.027) |
| reversal_k8_now | 0.619 (42) | 0.665 (325) [0.629, 0.701] | 0.704 (1553) [0.685, 0.724] | 0.703 (2542) [0.687, 0.720] | 0.686 (955) [0.661, 0.710] | 0.615 (13) | 0.122 | flat -0.005 (noise 0.035) |
| overall | 0.497 (22317) | 0.504 (155292) [0.501, 0.507] | 0.503 (661815) [0.502, 0.505] | 0.503 (1080523) [0.502, 0.504] | 0.503 (397242) [0.501, 0.506] | 0.510 (6849) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06708, 0.1016] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5322, 'levels': [{'threshold': 0.06708, 'calls_per_day': 147.3, 'win_rate': 0.5728}, {'threshold': 0.1016, 'calls_per_day': 37.9, 'win_rate': 0.6292}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 24977, 'rate': 0.531}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15028 | 0.336 | 0.522 (14782) | 0.587 (1491) | 0.765 (2464) |
| volatility: normal | 15028 | 0.365 | 0.522 (14966) | 0.630 (695) | 0.759 (2176) |
| volatility: wild | 15028 | 0.378 | 0.510 (14990) | 0.613 (284) | 0.775 (2041) |
| session: Asia 00-08 | 15324 | 0.359 | 0.524 (15225) | 0.613 (923) | 0.767 (2252) |
| session: Europe 08-13 | 9300 | 0.354 | 0.519 (9216) | 0.599 (598) | 0.771 (1463) |
| session: US 13-21 | 14880 | 0.368 | 0.512 (14778) | 0.576 (587) | 0.769 (2141) |
| session: late 21-24 | 5580 | 0.351 | 0.515 (5519) | 0.622 (362) | 0.744 (825) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.398 | 0.344 | 0.264 | 0.264 | 0.617 | 0.347 | 0.449 | 1.085 |
| 6h | 360 | 0.384 | 0.361 | 0.299 | 0.326 | 0.536 | 0.284 | 0.484 | 1.152 |
| 24h | 1440 | 0.376 | 0.365 | 0.281 | 0.319 | 0.530 | 0.272 | 0.479 | 1.102 |
| 7d | 10080 | 0.369 | 0.359 | 0.277 | 0.310 | 0.533 | 0.267 | 0.472 | 1.215 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.518 | 0.253 | 0.466 | 1.290 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.398 / 0.617 / 0.933; 2: 0.354 / 0.517 / 0.933; 3: 0.355 / 0.500 / 0.917; 4: 0.394 / 0.600 / 0.900; 5: 0.370 / 0.600 / 0.917; 6: 0.370 / 0.567 / 0.933; 7: 0.346 / 0.400 / 0.917; 8: 0.383 / 0.583 / 0.900; 9: 0.360 / 0.483 / 0.900; 10: 0.342 / 0.467 / 0.917; 11: 0.335 / 0.400 / 0.900; 12: 0.344 / 0.450 / 0.950; 13: 0.343 / 0.483 / 0.933; 14: 0.342 / 0.467 / 0.967; 15: 0.362 / 0.533 / 0.967
- 6h: 1: 0.384 / 0.536 / 0.906; 2: 0.357 / 0.489 / 0.908; 3: 0.368 / 0.528 / 0.944; 4: 0.370 / 0.522 / 0.919; 5: 0.381 / 0.567 / 0.928; 6: 0.370 / 0.531 / 0.922; 7: 0.356 / 0.461 / 0.933; 8: 0.377 / 0.547 / 0.925; 9: 0.368 / 0.492 / 0.936; 10: 0.365 / 0.497 / 0.944; 11: 0.356 / 0.466 / 0.939; 12: 0.357 / 0.455 / 0.953; 13: 0.362 / 0.497 / 0.947; 14: 0.361 / 0.497 / 0.967; 15: 0.373 / 0.534 / 0.958
- 24h: 1: 0.376 / 0.530 / 0.897; 2: 0.363 / 0.511 / 0.893; 3: 0.361 / 0.509 / 0.901; 4: 0.364 / 0.507 / 0.892; 5: 0.361 / 0.509 / 0.892; 6: 0.356 / 0.479 / 0.891; 7: 0.356 / 0.491 / 0.895; 8: 0.359 / 0.505 / 0.891; 9: 0.355 / 0.486 / 0.892; 10: 0.357 / 0.505 / 0.892; 11: 0.354 / 0.493 / 0.893; 12: 0.351 / 0.473 / 0.895; 13: 0.351 / 0.481 / 0.894; 14: 0.352 / 0.489 / 0.897; 15: 0.353 / 0.499 / 0.896
- 7d: 1: 0.369 / 0.533 / 0.898; 2: 0.355 / 0.494 / 0.899; 3: 0.359 / 0.505 / 0.901; 4: 0.354 / 0.498 / 0.900; 5: 0.354 / 0.498 / 0.900; 6: 0.354 / 0.497 / 0.900; 7: 0.352 / 0.496 / 0.901; 8: 0.353 / 0.499 / 0.900; 9: 0.353 / 0.500 / 0.900; 10: 0.355 / 0.508 / 0.900; 11: 0.350 / 0.499 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.351 / 0.499 / 0.900; 14: 0.351 / 0.502 / 0.901; 15: 0.351 / 0.502 / 0.901
- 30d: 1: 0.360 / 0.518 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.350 / 0.500 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.495 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.348 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.135 (body 0.101, range 0.169); 'price stays where it was' would score 0.168; colour right 0.600; typical miss of the close 6.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.157 (body 0.103, range 0.211); 'price stays where it was' would score 0.158; colour right 0.547; typical miss of the close 6.0 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.129; colour right 0.510; typical miss of the close 9.7 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.127 (body 0.086, range 0.168); 'price stays where it was' would score 0.133; colour right 0.503; typical miss of the close 9.3 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.8 bp; chain ended on the right side 0.523 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.9; 2: 0.197 / 4.5; 3: 0.164 / 6.0; 4: 0.132 / 6.6; 5: 0.119 / 7.2; 6: 0.110 / 7.7; 7: 0.104 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.3; 10: 0.086 / 9.2; 11: 0.082 / 9.7; 12: 0.078 / 10.1; 13: 0.067 / 10.4; 14: 0.067 / 10.6; 15: 0.059 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 113958, probability skill vs chance 0.2278, widened contest next: False
  - now: threshold 0.8357, hit rate recent 0.918 / long run 0.9293
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.314, naive rule 0.515, lift 3.18x
    - 24h: 53 calls (53 a day), hit rate 0.925, chance 0.304, naive rule 0.502, lift 3.04x
    - 7d: 384 calls (55 a day), hit rate 0.927, chance 0.290, naive rule 0.481, lift 3.20x
    - 30d: 1697 calls (57 a day), hit rate 0.933, chance 0.292, naive rule 0.484, lift 3.19x
  - next: threshold 0.5182, hit rate recent 0.6773 / long run 0.5787
    - 6h: 41 calls (166 a day), hit rate 0.780, chance 0.314, lift 2.48x
    - 24h: 127 calls (127 a day), hit rate 0.646, chance 0.304, lift 2.12x
    - 7d: 752 calls (107 a day), hit rate 0.573, chance 0.290, lift 1.98x
    - 30d: 2678 calls (89 a day), hit rate 0.575, chance 0.292, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.491; 0.35: 541, 0.514; 0.40: 482, 0.567; 0.45: 413, 0.637; 0.50: 361, 0.690; 0.55: 316, 0.731; 0.60: 269, 0.775; 0.65: 224, 0.803; 0.70: 178, 0.836; 0.75: 138, 0.871; 0.80: 94, 0.911; 0.85: 48, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 498, 0.462; 0.40: 406, 0.493; 0.45: 311, 0.525; 0.50: 201, 0.556; 0.55: 91, 0.570; 0.60: 14, 0.610; 0.65: 1, 0.690
- **K=5**: model 1792540800, labels learned 113956, probability skill vs chance 0.2158, widened contest next: False
  - now: threshold 0.6832, hit rate recent 0.8188 / long run 0.8236
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.204, naive rule 0.460, lift 4.41x
    - 24h: 46 calls (46 a day), hit rate 0.826, chance 0.191, naive rule 0.415, lift 4.32x
    - 7d: 360 calls (51 a day), hit rate 0.819, chance 0.186, naive rule 0.399, lift 4.40x
    - 30d: 1578 calls (53 a day), hit rate 0.827, chance 0.187, naive rule 0.394, lift 4.42x
  - next: threshold 0.4194, hit rate recent 0.4864 / long run 0.4485
    - 6h: 33 calls (135 a day), hit rate 0.636, chance 0.204, lift 3.12x
    - 24h: 126 calls (127 a day), hit rate 0.460, chance 0.191, lift 2.41x
    - 7d: 894 calls (128 a day), hit rate 0.446, chance 0.186, lift 2.39x
    - 30d: 2514 calls (84 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 348, 0.488; 0.40: 279, 0.559; 0.45: 227, 0.615; 0.50: 179, 0.665; 0.55: 136, 0.710; 0.60: 106, 0.753; 0.65: 79, 0.789; 0.70: 57, 0.822; 0.75: 32, 0.865; 0.80: 10, 0.894
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.387; 0.35: 249, 0.418; 0.40: 157, 0.443; 0.45: 73, 0.458; 0.50: 17, 0.497; 0.55: 2, 0.511
- **K=8**: model 1792540800, labels learned 113953, probability skill vs chance 0.1977, widened contest next: True
  - now: threshold 0.5676, hit rate recent 0.619 / long run 0.6818
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.133, naive rule 0.377, lift 5.85x
    - 24h: 42 calls (42 a day), hit rate 0.595, chance 0.117, naive rule 0.327, lift 5.07x
    - 7d: 325 calls (46 a day), hit rate 0.658, chance 0.117, naive rule 0.319, lift 5.61x
    - 30d: 1547 calls (52 a day), hit rate 0.705, chance 0.121, naive rule 0.328, lift 5.81x
  - next: threshold 0.3498, hit rate recent 0.397 / long run 0.3759
    - 6h: 29 calls (119 a day), hit rate 0.448, chance 0.133, lift 3.37x
    - 24h: 104 calls (105 a day), hit rate 0.433, chance 0.117, lift 3.68x
    - 7d: 745 calls (107 a day), hit rate 0.364, chance 0.117, lift 3.10x
    - 30d: 2348 calls (78 a day), hit rate 0.388, chance 0.121, lift 3.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 255, 0.421; 0.35: 194, 0.491; 0.40: 148, 0.547; 0.45: 115, 0.591; 0.50: 88, 0.634; 0.55: 64, 0.678; 0.60: 43, 0.723; 0.65: 23, 0.785; 0.70: 10, 0.835; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.349; 0.35: 102, 0.379; 0.40: 40, 0.406; 0.45: 8, 0.429; 0.50: 1, 0.500
- **K=13**: model 1792454400, labels learned 113948, probability skill vs chance 0.1811, widened contest next: True
  - now: threshold 0.4337, hit rate recent 0.4963 / long run 0.5518
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.074, naive rule 0.277, lift 7.73x
    - 24h: 44 calls (44 a day), hit rate 0.500, chance 0.077, naive rule 0.272, lift 6.51x
    - 7d: 387 calls (55 a day), hit rate 0.514, chance 0.076, naive rule 0.268, lift 6.77x
    - 30d: 1548 calls (52 a day), hit rate 0.570, chance 0.078, naive rule 0.271, lift 7.36x
  - next: threshold 0.288, hit rate recent 0.3612 / long run 0.3196
    - 6h: 13 calls (54 a day), hit rate 0.462, chance 0.074, lift 6.24x
    - 24h: 75 calls (76 a day), hit rate 0.387, chance 0.077, lift 5.03x
    - 7d: 448 calls (64 a day), hit rate 0.321, chance 0.076, lift 4.23x
    - 30d: 2129 calls (71 a day), hit rate 0.309, chance 0.078, lift 3.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.450; 0.35: 86, 0.503; 0.40: 61, 0.552; 0.45: 41, 0.608; 0.50: 25, 0.655; 0.55: 14, 0.710; 0.60: 5, 0.761; 0.65: 1, 0.849
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.320; 0.35: 13, 0.353; 0.40: 2, 0.448

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.485 | 5.23% | 0.933 | 0.450 | 0.253 | 0.417 | 0.096 |
| 6h | 10.797 | 3.58% | 0.908 | 0.478 | 0.251 | 0.472 | 0.403 |
| 24h | 15.828 | 3.95% | 0.898 | 0.502 | 0.251 | 0.490 | 0.697 |
| 7d | 16.220 | 4.32% | 0.900 | 0.501 | 0.251 | 0.495 | 0.651 |
| 30d | 13.739 | 4.03% | 0.900 | 0.500 | 0.251 | 0.495 | 0.675 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.008 | 9.479 | 9.492 | 9.538 | 9.566 | 9.533 | 9.478 | 9.302 | 9.446 | 9.485 |
| 6h | 11.197 | 10.789 | 10.760 | 10.838 | 10.904 | 10.794 | 10.817 | 10.766 | 10.771 | 10.797 |
| 24h | 16.479 | 15.892 | 15.820 | 15.838 | 15.997 | 15.955 | 15.830 | 15.792 | 15.789 | 15.828 |
| 7d | 16.953 | 16.397 | 16.302 | 16.232 | 16.466 | 16.423 | 16.218 | 16.200 | 16.187 | 16.220 |
| 30d | 14.315 | 13.861 | 13.822 | 13.763 | 13.983 | 13.925 | 13.734 | 13.714 | 13.713 | 13.739 |

## Next candle

- candle starting 2026-10-21 07:24 UTC, last close 2441.76
- P(up) 0.5001, return quantiles (bp): {'05': -5.446, '10': -4.153, '25': -2.423, '40': -0.909, '50': 0.001, '60': 0.903, '75': 2.282, '90': 4.493, '95': 5.689}
- changepoint probability 0.0361, regime age 219.2 min
- agent weights: empirical 0.006, ewma 0.131, garch 0.187, har 0.134, bocpd 0.058, hmm 0.093, online_qr 0.179, lgbm 0.211

## Learning log

- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.18, 5.74, 16.45], current probabilities: [0.95, 0.049, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-21 07:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.136, 'l_abs': 0.67, 'l_hi': 0.767, 'l_lo': 0.795, 'b05': 0.698, 'b25': 0.632, 'b75': 0.629, 'b95': 0.703}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.364, 1.398, 1.861, 2.044, 2.288, 2.153, 2.549, 2.551, 2.749, 2.832, 2.848, 2.911, 2.908, 3.077]}
- calibration offsets (in sigma): {'05': 0.0315, '10': 0.023, '25': -0.0525, '40': -0.008, '50': 0.005, '60': 0.028, '75': 0.0125, '90': 0.047, '95': -0.0015}
