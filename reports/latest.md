# ETH-USD 60s candle generator - report

- generated: 2026-11-09 20:47 UTC
- last closed candle: 2026-11-09 20:47 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.500 (672) [0.469, 0.527] | 0.518 (2879) [0.500, 0.535] | 0.513 (6522) [0.501, 0.525] | 0.514 (3550) [0.497, 0.531] | 0.602 (83) | 0.500 | flat +0.004 (noise 0.027) |
| colour_clear | 0.568 (764) | 0.537 (5563) [0.518, 0.555] | 0.543 (23815) [0.537, 0.549] | 0.522 (53359) [0.516, 0.528] | 0.544 (29121) [0.538, 0.549] | 0.522 (696) | 0.500 | flat -0.005 (noise 0.012) |
| colour_confident | 0.571 (305) | 0.581 (1033) [0.568, 0.599] | 0.589 (4596) [0.581, 0.599] | 0.594 (5545) [0.585, 0.606] | 0.594 (5545) [0.585, 0.606] | 0.646 (48) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.564 (1391) | 0.532 (9968) [0.519, 0.544] | 0.530 (42800) [0.526, 0.535] | 0.517 (97124) [0.513, 0.521] | 0.530 (52775) [0.526, 0.534] | 0.524 (1243) | 0.500 | flat +0.002 (noise 0.009) |
| colour_path | 0.504 (19474) | 0.502 (139552) [0.500, 0.504] | 0.502 (599200) [0.500, 0.503] | 0.501 (1359736) [0.500, 0.502] | 0.501 (738850) [0.500, 0.502] | 0.501 (17402) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.630 (108) | 0.622 (278) [0.585, 0.641] | 0.625 (1247) [0.611, 0.639] | 0.630 (1491) [0.614, 0.647] | 0.630 (1491) [0.614, 0.647] | 0.500 (2) | 0.500 | flat +0.012 (noise 0.042) |
| reversal_k13_next | 0.304 (102) | 0.335 (445) [0.306, 0.367] | 0.324 (1838) [0.310, 0.339] | 0.312 (4484) [0.302, 0.323] | 0.324 (2379) [0.313, 0.335] | 0.371 (62) | 0.077 | flat -0.000 (noise 0.034) |
| reversal_k13_now | 0.569 (58) | 0.565 (370) [0.529, 0.600] | 0.561 (1659) [0.542, 0.579] | 0.573 (3517) [0.560, 0.586] | 0.567 (2045) [0.549, 0.585] | 0.500 (38) | 0.077 | flat -0.009 (noise 0.035) |
| reversal_k3_next | 0.631 (65) | 0.624 (441) [0.590, 0.649] | 0.592 (2952) [0.581, 0.604] | 0.588 (5964) [0.579, 0.597] | 0.588 (3524) [0.577, 0.599] | 0.622 (37) | 0.294 | flat +0.032 (noise 0.028) |
| reversal_k3_now | 0.949 (59) | 0.917 (400) [0.907, 0.929] | 0.933 (1737) [0.922, 0.944] | 0.936 (3908) [0.930, 0.942] | 0.931 (2145) [0.923, 0.940] | 0.938 (48) | 0.294 | flat -0.028 (noise 0.018) |
| reversal_k5_next | 0.568 (81) | 0.530 (411) [0.505, 0.555] | 0.487 (2715) [0.472, 0.503] | 0.485 (5301) [0.475, 0.497] | 0.480 (3311) [0.465, 0.495] | 0.515 (33) | 0.187 | flat -0.002 (noise 0.034) |
| reversal_k5_now | 0.754 (57) | 0.808 (376) [0.786, 0.830] | 0.819 (1631) [0.809, 0.829] | 0.827 (3627) [0.818, 0.836] | 0.819 (2016) [0.809, 0.828] | 0.618 (34) | 0.187 | flat -0.018 (noise 0.027) |
| reversal_k8_next | 0.348 (89) | 0.416 (416) [0.385, 0.451] | 0.394 (2640) [0.381, 0.409] | 0.394 (5367) [0.384, 0.405] | 0.393 (3261) [0.380, 0.406] | 0.460 (63) | 0.121 | flat +0.000 (noise 0.031) |
| reversal_k8_now | 0.660 (53) | 0.688 (353) [0.666, 0.709] | 0.688 (1540) [0.669, 0.706] | 0.701 (3534) [0.688, 0.714] | 0.690 (1947) [0.672, 0.707] | 0.628 (43) | 0.121 | flat -0.015 (noise 0.034) |
| overall | 0.509 (21525) | 0.506 (153404) [0.504, 0.508] | 0.505 (661591) [0.504, 0.507] | 0.504 (1499084) [0.503, 0.505] | 0.505 (815803) [0.504, 0.506] | 0.504 (19086) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07785, 0.118] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5294, 'levels': [{'threshold': 0.07785, 'calls_per_day': 142.3, 'win_rate': 0.5809}, {'threshold': 0.118, 'calls_per_day': 35.6, 'win_rate': 0.6151}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42842, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15296 | 0.339 | 0.530 (14994) | 0.571 (2487) | 0.739 (2563) |
| volatility: normal | 15295 | 0.368 | 0.535 (15226) | 0.616 (1469) | 0.751 (2273) |
| volatility: wild | 15296 | 0.384 | 0.524 (15256) | 0.617 (822) | 0.767 (2098) |
| session: Asia 00-08 | 15360 | 0.363 | 0.535 (15223) | 0.599 (1680) | 0.756 (2272) |
| session: Europe 08-13 | 9600 | 0.357 | 0.533 (9490) | 0.591 (1271) | 0.749 (1548) |
| session: US 13-21 | 15347 | 0.371 | 0.528 (15232) | 0.597 (1252) | 0.752 (2326) |
| session: late 21-24 | 5580 | 0.356 | 0.515 (5531) | 0.569 (575) | 0.745 (788) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.405 | 0.381 | 0.307 | 0.307 | 0.617 | 0.303 | 0.507 | 1.395 |
| 6h | 360 | 0.387 | 0.384 | 0.298 | 0.351 | 0.542 | 0.271 | 0.503 | 1.124 |
| 24h | 1440 | 0.385 | 0.381 | 0.299 | 0.339 | 0.517 | 0.264 | 0.506 | 1.180 |
| 7d | 10080 | 0.367 | 0.362 | 0.277 | 0.310 | 0.530 | 0.264 | 0.471 | 1.346 |
| 30d | 43200 | 0.365 | 0.357 | 0.276 | 0.307 | 0.531 | 0.263 | 0.467 | 1.264 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.405 / 0.617 / 0.933; 2: 0.355 / 0.400 / 0.933; 3: 0.392 / 0.567 / 0.983; 4: 0.377 / 0.450 / 0.950; 5: 0.399 / 0.583 / 0.950; 6: 0.398 / 0.583 / 1.000; 7: 0.351 / 0.367 / 1.000; 8: 0.371 / 0.483 / 1.000; 9: 0.380 / 0.483 / 1.000; 10: 0.382 / 0.567 / 0.983; 11: 0.360 / 0.467 / 0.983; 12: 0.373 / 0.450 / 0.967; 13: 0.367 / 0.500 / 0.950; 14: 0.402 / 0.567 / 0.933; 15: 0.367 / 0.483 / 0.933
- 6h: 1: 0.387 / 0.542 / 0.928; 2: 0.368 / 0.472 / 0.936; 3: 0.386 / 0.542 / 0.958; 4: 0.376 / 0.489 / 0.914; 5: 0.372 / 0.506 / 0.900; 6: 0.368 / 0.486 / 0.939; 7: 0.369 / 0.486 / 0.931; 8: 0.366 / 0.494 / 0.900; 9: 0.379 / 0.503 / 0.908; 10: 0.369 / 0.500 / 0.956; 11: 0.378 / 0.522 / 0.947; 12: 0.366 / 0.475 / 0.950; 13: 0.367 / 0.486 / 0.933; 14: 0.386 / 0.550 / 0.942; 15: 0.371 / 0.489 / 0.933
- 24h: 1: 0.385 / 0.517 / 0.915; 2: 0.376 / 0.493 / 0.919; 3: 0.384 / 0.524 / 0.924; 4: 0.373 / 0.485 / 0.917; 5: 0.375 / 0.500 / 0.913; 6: 0.372 / 0.494 / 0.920; 7: 0.369 / 0.483 / 0.922; 8: 0.374 / 0.506 / 0.916; 9: 0.375 / 0.503 / 0.915; 10: 0.371 / 0.507 / 0.922; 11: 0.375 / 0.512 / 0.918; 12: 0.370 / 0.508 / 0.919; 13: 0.369 / 0.488 / 0.915; 14: 0.371 / 0.509 / 0.917; 15: 0.370 / 0.490 / 0.916
- 7d: 1: 0.367 / 0.530 / 0.897; 2: 0.356 / 0.491 / 0.902; 3: 0.360 / 0.516 / 0.904; 4: 0.355 / 0.499 / 0.904; 5: 0.356 / 0.503 / 0.904; 6: 0.353 / 0.501 / 0.904; 7: 0.353 / 0.498 / 0.906; 8: 0.353 / 0.500 / 0.905; 9: 0.355 / 0.508 / 0.905; 10: 0.353 / 0.502 / 0.907; 11: 0.354 / 0.505 / 0.905; 12: 0.353 / 0.507 / 0.905; 13: 0.352 / 0.493 / 0.905; 14: 0.353 / 0.508 / 0.905; 15: 0.353 / 0.501 / 0.905
- 30d: 1: 0.365 / 0.531 / 0.898; 2: 0.353 / 0.495 / 0.900; 3: 0.356 / 0.510 / 0.901; 4: 0.351 / 0.498 / 0.900; 5: 0.352 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.901; 7: 0.351 / 0.499 / 0.901; 8: 0.351 / 0.504 / 0.900; 9: 0.351 / 0.503 / 0.901; 10: 0.351 / 0.504 / 0.901; 11: 0.348 / 0.499 / 0.901; 12: 0.350 / 0.504 / 0.901; 13: 0.348 / 0.498 / 0.901; 14: 0.348 / 0.501 / 0.901; 15: 0.349 / 0.502 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.152 (body 0.102, range 0.201); 'price stays where it was' would score 0.096; colour right 0.467; typical miss of the close 12.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.123 (body 0.077, range 0.170); 'price stays where it was' would score 0.111; colour right 0.489; typical miss of the close 15.6 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.126 (body 0.081, range 0.171); 'price stays where it was' would score 0.128; colour right 0.483; typical miss of the close 14.9 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.124 (body 0.084, range 0.164); 'price stays where it was' would score 0.125; colour right 0.504; typical miss of the close 8.7 bp; chain ended on the right side 0.510 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.6 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.5; 2: 0.200 / 5.2; 3: 0.167 / 6.8; 4: 0.132 / 7.0; 5: 0.127 / 7.7; 6: 0.115 / 8.5; 7: 0.111 / 8.8; 8: 0.096 / 9.8; 9: 0.091 / 9.7; 10: 0.092 / 10.3; 11: 0.088 / 10.3; 12: 0.079 / 10.7; 13: 0.073 / 11.1; 14: 0.071 / 11.6; 15: 0.066 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 142121, probability skill vs chance 0.2263, widened contest next: False
  - now: threshold 0.8386, hit rate recent 0.9301 / long run 0.9294
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.282, naive rule 0.490, lift 3.16x
    - 24h: 56 calls (56 a day), hit rate 0.929, chance 0.290, naive rule 0.501, lift 3.21x
    - 7d: 397 calls (57 a day), hit rate 0.922, chance 0.297, naive rule 0.500, lift 3.10x
    - 30d: 1727 calls (58 a day), hit rate 0.933, chance 0.295, naive rule 0.497, lift 3.17x
  - next: threshold 0.5661, hit rate recent 0.6351 / long run 0.6108
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.282, lift 2.18x
    - 24h: 43 calls (43 a day), hit rate 0.651, chance 0.290, lift 2.25x
    - 7d: 377 calls (54 a day), hit rate 0.607, chance 0.297, lift 2.04x
    - 30d: 2878 calls (96 a day), hit rate 0.591, chance 0.295, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.500; 0.35: 533, 0.525; 0.40: 474, 0.581; 0.45: 405, 0.651; 0.50: 356, 0.699; 0.55: 309, 0.743; 0.60: 260, 0.786; 0.65: 219, 0.811; 0.70: 173, 0.843; 0.75: 139, 0.874; 0.80: 92, 0.905; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.430; 0.35: 498, 0.465; 0.40: 400, 0.502; 0.45: 302, 0.537; 0.50: 194, 0.569; 0.55: 87, 0.579; 0.60: 12, 0.650; 0.65: 1, 0.619
- **K=5**: model 1792540800, labels learned 142119, probability skill vs chance 0.2084, widened contest next: True
  - now: threshold 0.6834, hit rate recent 0.7151 / long run 0.8047
    - 6h: 5 calls (20 a day), hit rate 0.400, chance 0.191, naive rule 0.425, lift 2.09x
    - 24h: 44 calls (44 a day), hit rate 0.636, chance 0.178, naive rule 0.398, lift 3.58x
    - 7d: 352 calls (50 a day), hit rate 0.793, chance 0.186, naive rule 0.404, lift 4.25x
    - 30d: 1611 calls (54 a day), hit rate 0.814, chance 0.187, naive rule 0.407, lift 4.35x
  - next: threshold 0.4552, hit rate recent 0.5417 / long run 0.5196
    - 6h: 12 calls (49 a day), hit rate 0.500, chance 0.191, lift 2.61x
    - 24h: 44 calls (44 a day), hit rate 0.568, chance 0.178, lift 3.19x
    - 7d: 394 calls (56 a day), hit rate 0.523, chance 0.186, lift 2.80x
    - 30d: 2680 calls (89 a day), hit rate 0.488, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.423; 0.35: 351, 0.486; 0.40: 284, 0.558; 0.45: 233, 0.608; 0.50: 187, 0.658; 0.55: 150, 0.694; 0.60: 113, 0.743; 0.65: 76, 0.781; 0.70: 47, 0.818; 0.75: 28, 0.852; 0.80: 10, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.384; 0.35: 256, 0.422; 0.40: 160, 0.461; 0.45: 66, 0.494; 0.50: 11, 0.523; 0.55: 1, 0.447
- **K=8**: model 1794182400, labels learned 142116, probability skill vs chance 0.2033, widened contest next: False
  - now: threshold 0.5708, hit rate recent 0.6644 / long run 0.6893
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.116, naive rule 0.350, lift 5.76x
    - 24h: 48 calls (48 a day), hit rate 0.625, chance 0.119, naive rule 0.353, lift 5.27x
    - 7d: 354 calls (51 a day), hit rate 0.684, chance 0.121, naive rule 0.337, lift 5.66x
    - 30d: 1532 calls (51 a day), hit rate 0.685, chance 0.121, naive rule 0.335, lift 5.68x
  - next: threshold 0.3613, hit rate recent 0.4246 / long run 0.4161
    - 6h: 19 calls (78 a day), hit rate 0.421, chance 0.116, lift 3.64x
    - 24h: 74 calls (75 a day), hit rate 0.432, chance 0.119, lift 3.65x
    - 7d: 440 calls (63 a day), hit rate 0.416, chance 0.121, lift 3.45x
    - 30d: 2640 calls (88 a day), hit rate 0.395, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.429; 0.35: 192, 0.492; 0.40: 152, 0.537; 0.45: 118, 0.584; 0.50: 85, 0.636; 0.55: 60, 0.670; 0.60: 40, 0.711; 0.65: 24, 0.782; 0.70: 12, 0.808; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.362; 0.35: 88, 0.390; 0.40: 24, 0.428; 0.45: 4, 0.439; 0.50: 1, 0.727
- **K=13**: model 1794096000, labels learned 142111, probability skill vs chance 0.178, widened contest next: False
  - now: threshold 0.4543, hit rate recent 0.5373 / long run 0.5646
    - 6h: 9 calls (38 a day), hit rate 0.444, chance 0.084, naive rule 0.315, lift 5.29x
    - 24h: 45 calls (45 a day), hit rate 0.489, chance 0.076, naive rule 0.295, lift 6.42x
    - 7d: 364 calls (52 a day), hit rate 0.569, chance 0.079, naive rule 0.285, lift 7.20x
    - 30d: 1645 calls (55 a day), hit rate 0.559, chance 0.077, naive rule 0.281, lift 7.24x
  - next: threshold 0.2853, hit rate recent 0.3728 / long run 0.331
    - 6h: 20 calls (83 a day), hit rate 0.450, chance 0.084, lift 5.35x
    - 24h: 72 calls (73 a day), hit rate 0.361, chance 0.076, lift 4.74x
    - 7d: 463 calls (66 a day), hit rate 0.333, chance 0.079, lift 4.21x
    - 30d: 1833 calls (61 a day), hit rate 0.324, chance 0.077, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 133, 0.431; 0.35: 96, 0.478; 0.40: 67, 0.537; 0.45: 46, 0.582; 0.50: 31, 0.640; 0.55: 20, 0.663; 0.60: 12, 0.703; 0.65: 4, 0.667; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.341; 0.40: 3, 0.410; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.693 | 2.48% | 0.917 | 0.550 | 0.247 | 0.517 | 0.092 |
| 6h | 21.338 | 3.72% | 0.917 | 0.481 | 0.249 | 0.506 | 0.614 |
| 24h | 24.504 | 9.51% | 0.910 | 0.494 | 0.251 | 0.505 | 0.606 |
| 7d | 16.134 | 6.13% | 0.901 | 0.500 | 0.250 | 0.503 | 0.729 |
| 30d | 15.365 | 4.69% | 0.900 | 0.500 | 0.250 | 0.501 | 0.704 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 16.092 | 16.034 | 16.109 | 16.458 | 16.201 | 15.677 | 15.692 | 15.542 | 15.663 | 15.693 |
| 6h | 22.162 | 21.555 | 21.574 | 21.622 | 21.748 | 21.540 | 21.304 | 21.249 | 21.290 | 21.338 |
| 24h | 27.080 | 24.701 | 24.690 | 25.063 | 24.810 | 24.970 | 24.403 | 24.368 | 24.439 | 24.504 |
| 7d | 17.188 | 16.264 | 16.233 | 16.248 | 16.400 | 16.528 | 16.102 | 16.093 | 16.099 | 16.134 |
| 30d | 16.121 | 15.520 | 15.466 | 15.412 | 15.647 | 15.621 | 15.351 | 15.331 | 15.335 | 15.365 |

## Next candle

- candle starting 2026-11-09 20:47 UTC, last close 2127.79
- P(up) 0.476, return quantiles (bp): {'05': -9.221, '10': -7.319, '25': -3.712, '40': -1.498, '50': -0.361, '60': 1.173, '75': 3.576, '90': 6.971, '95': 9.308}
- changepoint probability 0.0617, regime age 55.9 min
- agent weights: empirical 0.003, ewma 0.066, garch 0.061, har 0.020, bocpd 0.018, hmm 0.030, online_qr 0.346, lgbm 0.457

## Learning log

- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- 2026-11-09 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9334}, "hmm": {"sd_bp": [2.32, 6.39, 18.36], "stay": [0.988, 0.969, 0.943]}}
- HMM volatility states (sd, bp per minute): [2.32, 6.39, 18.36], current probabilities: [0.0, 0.968, 0.032]
- live generator: {'versions': 60, 'latest_effective': '2026-11-09 20:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.281, 'l_abs': 0.696, 'l_hi': 0.749, 'l_lo': 0.728, 'b05': 0.672, 'b25': 0.618, 'b75': 0.578, 'b95': 0.635}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [0.946, 1.138, 1.608, 1.875, 1.685, 1.684, 2.203, 2.341, 1.832, 2.044, 2.139, 2.417, 2.367, 2.607]}
- calibration offsets (in sigma): {'05': 0.073, '10': 0.016, '25': -0.005, '40': -0.026, '50': -0.04, '60': -0.004, '75': 0.015, '90': -0.006, '95': -0.023}
