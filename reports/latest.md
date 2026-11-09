# ETH-USD 60s candle generator - report

- generated: 2026-11-09 02:29 UTC
- last closed candle: 2026-11-09 02:29 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.500 (672) [0.469, 0.527] | 0.518 (2879) [0.500, 0.535] | 0.513 (6522) [0.501, 0.525] | 0.514 (3550) [0.497, 0.531] | 0.667 (9) | 0.500 | flat +0.004 (noise 0.027) |
| colour_clear | 0.568 (764) | 0.537 (5563) [0.518, 0.555] | 0.543 (23815) [0.537, 0.549] | 0.522 (53359) [0.516, 0.528] | 0.544 (29121) [0.538, 0.549] | 0.608 (79) | 0.500 | flat -0.005 (noise 0.012) |
| colour_confident | 0.571 (305) | 0.581 (1033) [0.568, 0.599] | 0.589 (4596) [0.581, 0.599] | 0.594 (5545) [0.585, 0.606] | 0.594 (5545) [0.585, 0.606] | 1.000 (2) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.564 (1391) | 0.532 (9968) [0.519, 0.544] | 0.530 (42800) [0.526, 0.535] | 0.517 (97124) [0.513, 0.521] | 0.530 (52775) [0.526, 0.534] | 0.574 (148) | 0.500 | flat +0.002 (noise 0.009) |
| colour_path | 0.504 (19474) | 0.502 (139552) [0.500, 0.504] | 0.502 (599200) [0.500, 0.503] | 0.501 (1359736) [0.500, 0.502] | 0.501 (738850) [0.500, 0.502] | 0.488 (2072) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.630 (108) | 0.622 (278) [0.585, 0.641] | 0.625 (1247) [0.611, 0.639] | 0.630 (1491) [0.614, 0.647] | 0.630 (1491) [0.614, 0.647] | - | 0.500 | flat +0.012 (noise 0.042) |
| reversal_k13_next | 0.304 (102) | 0.335 (445) [0.306, 0.367] | 0.324 (1838) [0.310, 0.339] | 0.312 (4484) [0.302, 0.323] | 0.324 (2379) [0.313, 0.335] | 0.250 (8) | 0.077 | flat -0.000 (noise 0.034) |
| reversal_k13_now | 0.569 (58) | 0.565 (370) [0.529, 0.600] | 0.561 (1659) [0.542, 0.579] | 0.573 (3517) [0.560, 0.586] | 0.567 (2045) [0.549, 0.585] | 0.333 (6) | 0.077 | flat -0.009 (noise 0.035) |
| reversal_k3_next | 0.631 (65) | 0.624 (441) [0.590, 0.649] | 0.592 (2952) [0.581, 0.604] | 0.588 (5964) [0.579, 0.597] | 0.588 (3524) [0.577, 0.599] | 0.500 (2) | 0.294 | flat +0.032 (noise 0.028) |
| reversal_k3_now | 0.949 (59) | 0.917 (400) [0.907, 0.929] | 0.933 (1737) [0.922, 0.944] | 0.936 (3908) [0.930, 0.942] | 0.931 (2145) [0.923, 0.940] | 1.000 (6) | 0.294 | flat -0.028 (noise 0.018) |
| reversal_k5_next | 0.568 (81) | 0.530 (411) [0.505, 0.555] | 0.487 (2715) [0.472, 0.503] | 0.485 (5301) [0.475, 0.497] | 0.480 (3311) [0.465, 0.495] | 0.667 (3) | 0.187 | flat -0.002 (noise 0.034) |
| reversal_k5_now | 0.754 (57) | 0.808 (376) [0.786, 0.830] | 0.819 (1631) [0.809, 0.829] | 0.827 (3627) [0.818, 0.836] | 0.819 (2016) [0.809, 0.828] | 0.500 (4) | 0.187 | flat -0.018 (noise 0.027) |
| reversal_k8_next | 0.348 (89) | 0.416 (416) [0.385, 0.451] | 0.394 (2640) [0.381, 0.409] | 0.394 (5367) [0.384, 0.405] | 0.393 (3261) [0.380, 0.406] | 0.500 (6) | 0.121 | flat +0.000 (noise 0.031) |
| reversal_k8_now | 0.660 (53) | 0.688 (353) [0.666, 0.709] | 0.688 (1540) [0.669, 0.706] | 0.701 (3534) [0.688, 0.714] | 0.690 (1947) [0.672, 0.707] | 0.500 (4) | 0.121 | flat -0.015 (noise 0.034) |
| overall | 0.509 (21525) | 0.506 (153404) [0.504, 0.508] | 0.505 (661591) [0.504, 0.507] | 0.504 (1499084) [0.503, 0.505] | 0.505 (815803) [0.504, 0.506] | 0.495 (2268) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07828, 0.1186] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5309, 'levels': [{'threshold': 0.07828, 'calls_per_day': 144.8, 'win_rate': 0.5785}, {'threshold': 0.1186, 'calls_per_day': 36.7, 'win_rate': 0.6308}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42799, 'rate': 0.5306}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14930 | 0.338 | 0.530 (14628) | 0.570 (2442) | 0.741 (2517) |
| volatility: normal | 14929 | 0.367 | 0.536 (14863) | 0.619 (1455) | 0.756 (2211) |
| volatility: wild | 14930 | 0.383 | 0.525 (14890) | 0.613 (835) | 0.764 (2063) |
| session: Asia 00-08 | 15029 | 0.363 | 0.536 (14895) | 0.599 (1659) | 0.759 (2216) |
| session: Europe 08-13 | 9300 | 0.356 | 0.534 (9190) | 0.591 (1258) | 0.745 (1514) |
| session: US 13-21 | 14880 | 0.370 | 0.527 (14765) | 0.596 (1240) | 0.755 (2273) |
| session: late 21-24 | 5580 | 0.356 | 0.515 (5531) | 0.569 (575) | 0.745 (788) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.426 | 0.363 | 0.300 | 0.300 | 0.617 | 0.353 | 0.499 | 1.126 |
| 6h | 360 | 0.383 | 0.372 | 0.314 | 0.334 | 0.521 | 0.265 | 0.500 | 1.606 |
| 24h | 1440 | 0.343 | 0.327 | 0.259 | 0.274 | 0.564 | 0.268 | 0.418 | 1.055 |
| 7d | 10080 | 0.365 | 0.360 | 0.276 | 0.307 | 0.532 | 0.263 | 0.468 | 1.306 |
| 30d | 43200 | 0.363 | 0.355 | 0.275 | 0.305 | 0.531 | 0.263 | 0.464 | 1.273 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.426 / 0.617 / 0.933; 2: 0.356 / 0.400 / 0.983; 3: 0.411 / 0.567 / 1.000; 4: 0.404 / 0.517 / 1.000; 5: 0.389 / 0.550 / 1.000; 6: 0.406 / 0.483 / 1.000; 7: 0.360 / 0.483 / 1.000; 8: 0.417 / 0.583 / 1.000; 9: 0.382 / 0.467 / 1.000; 10: 0.371 / 0.517 / 1.000; 11: 0.393 / 0.450 / 1.000; 12: 0.335 / 0.400 / 1.000; 13: 0.391 / 0.517 / 1.000; 14: 0.337 / 0.367 / 1.000; 15: 0.376 / 0.467 / 1.000
- 6h: 1: 0.383 / 0.521 / 0.894; 2: 0.367 / 0.479 / 0.931; 3: 0.376 / 0.524 / 0.947; 4: 0.371 / 0.496 / 0.942; 5: 0.365 / 0.471 / 0.928; 6: 0.370 / 0.507 / 0.942; 7: 0.347 / 0.443 / 0.928; 8: 0.366 / 0.499 / 0.933; 9: 0.367 / 0.479 / 0.936; 10: 0.348 / 0.487 / 0.931; 11: 0.366 / 0.501 / 0.922; 12: 0.348 / 0.496 / 0.933; 13: 0.364 / 0.496 / 0.922; 14: 0.354 / 0.510 / 0.914; 15: 0.346 / 0.476 / 0.922
- 24h: 1: 0.343 / 0.564 / 0.885; 2: 0.325 / 0.496 / 0.902; 3: 0.330 / 0.528 / 0.903; 4: 0.321 / 0.490 / 0.902; 5: 0.326 / 0.506 / 0.898; 6: 0.320 / 0.487 / 0.901; 7: 0.319 / 0.489 / 0.899; 8: 0.326 / 0.502 / 0.899; 9: 0.325 / 0.507 / 0.899; 10: 0.319 / 0.506 / 0.899; 11: 0.325 / 0.510 / 0.899; 12: 0.322 / 0.513 / 0.897; 13: 0.320 / 0.487 / 0.899; 14: 0.327 / 0.532 / 0.895; 15: 0.315 / 0.482 / 0.897
- 7d: 1: 0.365 / 0.532 / 0.895; 2: 0.354 / 0.492 / 0.901; 3: 0.357 / 0.515 / 0.901; 4: 0.353 / 0.500 / 0.901; 5: 0.354 / 0.503 / 0.901; 6: 0.352 / 0.506 / 0.902; 7: 0.351 / 0.499 / 0.901; 8: 0.351 / 0.499 / 0.902; 9: 0.353 / 0.507 / 0.901; 10: 0.350 / 0.498 / 0.901; 11: 0.351 / 0.501 / 0.902; 12: 0.351 / 0.505 / 0.902; 13: 0.349 / 0.493 / 0.902; 14: 0.351 / 0.506 / 0.902; 15: 0.349 / 0.500 / 0.902
- 30d: 1: 0.363 / 0.531 / 0.897; 2: 0.351 / 0.494 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.499 / 0.900; 8: 0.349 / 0.504 / 0.900; 9: 0.349 / 0.503 / 0.900; 10: 0.349 / 0.504 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.504 / 0.900; 13: 0.347 / 0.499 / 0.900; 14: 0.347 / 0.501 / 0.900; 15: 0.347 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.126 (body 0.086, range 0.165); 'price stays where it was' would score 0.120; colour right 0.483; typical miss of the close 25.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.105 (body 0.067, range 0.142); 'price stays where it was' would score 0.127; colour right 0.471; typical miss of the close 22.1 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.107 (body 0.073, range 0.141); 'price stays where it was' would score 0.112; colour right 0.492; typical miss of the close 5.6 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.162); 'price stays where it was' would score 0.124; colour right 0.505; typical miss of the close 8.6 bp; chain ended on the right side 0.499 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.2 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.4; 2: 0.198 / 5.0; 3: 0.167 / 6.4; 4: 0.131 / 6.8; 5: 0.127 / 7.4; 6: 0.115 / 8.2; 7: 0.111 / 8.4; 8: 0.098 / 9.4; 9: 0.091 / 9.3; 10: 0.092 / 9.9; 11: 0.086 / 10.0; 12: 0.078 / 10.4; 13: 0.073 / 10.7; 14: 0.071 / 11.2; 15: 0.065 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 141023, probability skill vs chance 0.2196, widened contest next: False
  - now: threshold 0.8379, hit rate recent 0.9364 / long run 0.9295
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.292, naive rule 0.480, lift 3.18x
    - 24h: 56 calls (56 a day), hit rate 0.946, chance 0.289, naive rule 0.493, lift 3.28x
    - 7d: 402 calls (57 a day), hit rate 0.920, chance 0.297, naive rule 0.498, lift 3.10x
    - 30d: 1734 calls (58 a day), hit rate 0.934, chance 0.295, naive rule 0.497, lift 3.16x
  - next: threshold 0.5663, hit rate recent 0.64 / long run 0.6097
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.292, lift 2.67x
    - 24h: 59 calls (59 a day), hit rate 0.644, chance 0.289, lift 2.23x
    - 7d: 433 calls (62 a day), hit rate 0.626, chance 0.297, lift 2.10x
    - 30d: 2943 calls (98 a day), hit rate 0.592, chance 0.295, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.500; 0.35: 534, 0.525; 0.40: 474, 0.581; 0.45: 405, 0.651; 0.50: 355, 0.699; 0.55: 308, 0.742; 0.60: 260, 0.786; 0.65: 218, 0.812; 0.70: 172, 0.845; 0.75: 138, 0.876; 0.80: 92, 0.908; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.430; 0.35: 499, 0.464; 0.40: 402, 0.502; 0.45: 304, 0.538; 0.50: 196, 0.570; 0.55: 89, 0.578; 0.60: 12, 0.653; 0.65: 1, 0.619
- **K=5**: model 1792540800, labels learned 141021, probability skill vs chance 0.2062, widened contest next: True
  - now: threshold 0.6847, hit rate recent 0.7665 / long run 0.8135
    - 6h: 15 calls (61 a day), hit rate 0.667, chance 0.166, naive rule 0.360, lift 4.02x
    - 24h: 54 calls (54 a day), hit rate 0.741, chance 0.185, naive rule 0.400, lift 4.00x
    - 7d: 375 calls (54 a day), hit rate 0.805, chance 0.187, naive rule 0.405, lift 4.30x
    - 30d: 1627 calls (54 a day), hit rate 0.820, chance 0.187, naive rule 0.408, lift 4.38x
  - next: threshold 0.4529, hit rate recent 0.5738 / long run 0.5207
    - 6h: 15 calls (61 a day), hit rate 0.733, chance 0.166, lift 4.43x
    - 24h: 76 calls (76 a day), hit rate 0.566, chance 0.185, lift 3.05x
    - 7d: 407 calls (58 a day), hit rate 0.533, chance 0.187, lift 2.85x
    - 30d: 2714 calls (90 a day), hit rate 0.487, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.424; 0.35: 350, 0.488; 0.40: 282, 0.560; 0.45: 232, 0.611; 0.50: 186, 0.660; 0.55: 149, 0.696; 0.60: 113, 0.745; 0.65: 76, 0.786; 0.70: 47, 0.825; 0.75: 28, 0.857; 0.80: 11, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 349, 0.384; 0.35: 257, 0.422; 0.40: 161, 0.461; 0.45: 67, 0.493; 0.50: 11, 0.524; 0.55: 1, 0.421
- **K=8**: model 1794182400, labels learned 141018, probability skill vs chance 0.1899, widened contest next: True
  - now: threshold 0.5702, hit rate recent 0.6799 / long run 0.6925
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.124, naive rule 0.344, lift 4.83x
    - 24h: 52 calls (52 a day), hit rate 0.654, chance 0.117, naive rule 0.308, lift 5.60x
    - 7d: 355 calls (51 a day), hit rate 0.685, chance 0.122, naive rule 0.339, lift 5.61x
    - 30d: 1536 calls (51 a day), hit rate 0.689, chance 0.121, naive rule 0.336, lift 5.69x
  - next: threshold 0.3602, hit rate recent 0.3748 / long run 0.4121
    - 6h: 18 calls (74 a day), hit rate 0.389, chance 0.124, lift 3.13x
    - 24h: 88 calls (89 a day), hit rate 0.330, chance 0.117, lift 2.82x
    - 7d: 416 calls (59 a day), hit rate 0.416, chance 0.122, lift 3.41x
    - 30d: 2642 calls (88 a day), hit rate 0.394, chance 0.121, lift 3.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 192, 0.494; 0.40: 151, 0.540; 0.45: 117, 0.587; 0.50: 85, 0.639; 0.55: 60, 0.677; 0.60: 40, 0.715; 0.65: 24, 0.783; 0.70: 12, 0.808; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.363; 0.35: 89, 0.389; 0.40: 24, 0.423; 0.45: 4, 0.452; 0.50: 1, 0.727
- **K=13**: model 1794096000, labels learned 141013, probability skill vs chance 0.1702, widened contest next: False
  - now: threshold 0.4516, hit rate recent 0.5401 / long run 0.5664
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.061, naive rule 0.237, lift 7.04x
    - 24h: 60 calls (61 a day), hit rate 0.550, chance 0.073, naive rule 0.257, lift 7.50x
    - 7d: 374 calls (54 a day), hit rate 0.561, chance 0.078, naive rule 0.283, lift 7.15x
    - 30d: 1658 calls (55 a day), hit rate 0.561, chance 0.078, naive rule 0.282, lift 7.23x
  - next: threshold 0.2875, hit rate recent 0.3156 / long run 0.3253
    - 6h: 20 calls (83 a day), hit rate 0.350, chance 0.061, lift 5.75x
    - 24h: 102 calls (103 a day), hit rate 0.304, chance 0.073, lift 4.14x
    - 7d: 445 calls (64 a day), hit rate 0.328, chance 0.078, lift 4.18x
    - 30d: 1836 calls (61 a day), hit rate 0.322, chance 0.078, lift 4.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 132, 0.435; 0.35: 95, 0.483; 0.40: 67, 0.541; 0.45: 46, 0.584; 0.50: 31, 0.646; 0.55: 20, 0.672; 0.60: 12, 0.706; 0.65: 4, 0.670; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.329; 0.35: 13, 0.344; 0.40: 3, 0.412; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.003 | 13.92% | 0.900 | 0.417 | 0.252 | 0.467 | 0.085 |
| 6h | 35.422 | 18.41% | 0.894 | 0.486 | 0.253 | 0.490 | 0.592 |
| 24h | 13.545 | 13.29% | 0.893 | 0.501 | 0.251 | 0.493 | 0.703 |
| 7d | 15.717 | 6.26% | 0.899 | 0.501 | 0.250 | 0.504 | 0.728 |
| 30d | 14.995 | 4.75% | 0.900 | 0.500 | 0.250 | 0.499 | 0.709 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 29.045 | 24.850 | 25.328 | 25.700 | 24.925 | 26.128 | 24.568 | 24.602 | 24.585 | 25.003 |
| 6h | 43.414 | 35.791 | 35.633 | 36.379 | 35.468 | 36.509 | 35.120 | 35.078 | 35.317 | 35.422 |
| 24h | 15.620 | 13.658 | 13.617 | 13.815 | 13.690 | 14.040 | 13.467 | 13.446 | 13.506 | 13.545 |
| 7d | 16.766 | 15.845 | 15.817 | 15.805 | 15.977 | 16.125 | 15.690 | 15.681 | 15.687 | 15.717 |
| 30d | 15.743 | 15.148 | 15.094 | 15.032 | 15.270 | 15.249 | 14.983 | 14.963 | 14.967 | 14.995 |

## Next candle

- candle starting 2026-11-09 02:29 UTC, last close 2150.79
- P(up) 0.4839, return quantiles (bp): {'05': -16.559, '10': -12.252, '25': -6.142, '40': -2.932, '50': -0.328, '60': 1.753, '75': 5.818, '90': 12.464, '95': 16.634}
- changepoint probability 0.0311, regime age 104.2 min
- agent weights: empirical 0.003, ewma 0.010, garch 0.020, har 0.003, bocpd 0.024, hmm 0.003, online_qr 0.378, lgbm 0.560

## Learning log

- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.28, 5.65, 17.98], current probabilities: [0.0, 0.132, 0.868]
- live generator: {'versions': 60, 'latest_effective': '2026-11-09 02:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.233, 'l_abs': 0.628, 'l_hi': 0.737, 'l_lo': 0.709, 'b05': 0.638, 'b25': 0.602, 'b75': 0.584, 'b95': 0.654}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.298, 1.561, 1.918, 2.148, 2.177, 2.452, 2.68, 2.792, 2.777, 2.918, 3.054, 3.249, 3.588, 3.647]}
- calibration offsets (in sigma): {'05': -0.066, '10': -0.022, '25': 0.01, '40': -0.048, '50': -0.03, '60': -0.052, '75': -0.01, '90': 0.002, '95': -0.004}
