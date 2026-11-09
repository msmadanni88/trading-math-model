# ETH-USD 60s candle generator - report

- generated: 2026-11-09 10:12 UTC
- last closed candle: 2026-11-09 10:12 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.500 (672) [0.469, 0.527] | 0.518 (2879) [0.500, 0.535] | 0.513 (6522) [0.501, 0.525] | 0.514 (3550) [0.497, 0.531] | 0.625 (40) | 0.500 | flat +0.004 (noise 0.027) |
| colour_clear | 0.568 (764) | 0.537 (5563) [0.518, 0.555] | 0.543 (23815) [0.537, 0.549] | 0.522 (53359) [0.516, 0.528] | 0.544 (29121) [0.538, 0.549] | 0.510 (337) | 0.500 | flat -0.005 (noise 0.012) |
| colour_confident | 0.571 (305) | 0.581 (1033) [0.568, 0.599] | 0.589 (4596) [0.581, 0.599] | 0.594 (5545) [0.585, 0.606] | 0.594 (5545) [0.585, 0.606] | 0.567 (30) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.564 (1391) | 0.532 (9968) [0.519, 0.544] | 0.530 (42800) [0.526, 0.535] | 0.517 (97124) [0.513, 0.521] | 0.530 (52775) [0.526, 0.534] | 0.513 (608) | 0.500 | flat +0.002 (noise 0.009) |
| colour_path | 0.504 (19474) | 0.502 (139552) [0.500, 0.504] | 0.502 (599200) [0.500, 0.503] | 0.501 (1359736) [0.500, 0.502] | 0.501 (738850) [0.500, 0.502] | 0.495 (8512) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.630 (108) | 0.622 (278) [0.585, 0.641] | 0.625 (1247) [0.611, 0.639] | 0.630 (1491) [0.614, 0.647] | 0.630 (1491) [0.614, 0.647] | 0.000 (1) | 0.500 | flat +0.012 (noise 0.042) |
| reversal_k13_next | 0.304 (102) | 0.335 (445) [0.306, 0.367] | 0.324 (1838) [0.310, 0.339] | 0.312 (4484) [0.302, 0.323] | 0.324 (2379) [0.313, 0.335] | 0.270 (37) | 0.077 | flat -0.000 (noise 0.034) |
| reversal_k13_now | 0.569 (58) | 0.565 (370) [0.529, 0.600] | 0.561 (1659) [0.542, 0.579] | 0.573 (3517) [0.560, 0.586] | 0.567 (2045) [0.549, 0.585] | 0.389 (18) | 0.077 | flat -0.009 (noise 0.035) |
| reversal_k3_next | 0.631 (65) | 0.624 (441) [0.590, 0.649] | 0.592 (2952) [0.581, 0.604] | 0.588 (5964) [0.579, 0.597] | 0.588 (3524) [0.577, 0.599] | 0.636 (22) | 0.294 | flat +0.032 (noise 0.028) |
| reversal_k3_now | 0.949 (59) | 0.917 (400) [0.907, 0.929] | 0.933 (1737) [0.922, 0.944] | 0.936 (3908) [0.930, 0.942] | 0.931 (2145) [0.923, 0.940] | 0.960 (25) | 0.294 | flat -0.028 (noise 0.018) |
| reversal_k5_next | 0.568 (81) | 0.530 (411) [0.505, 0.555] | 0.487 (2715) [0.472, 0.503] | 0.485 (5301) [0.475, 0.497] | 0.480 (3311) [0.465, 0.495] | 0.529 (17) | 0.187 | flat -0.002 (noise 0.034) |
| reversal_k5_now | 0.754 (57) | 0.808 (376) [0.786, 0.830] | 0.819 (1631) [0.809, 0.829] | 0.827 (3627) [0.818, 0.836] | 0.819 (2016) [0.809, 0.828] | 0.556 (18) | 0.187 | flat -0.018 (noise 0.027) |
| reversal_k8_next | 0.348 (89) | 0.416 (416) [0.385, 0.451] | 0.394 (2640) [0.381, 0.409] | 0.394 (5367) [0.384, 0.405] | 0.393 (3261) [0.380, 0.406] | 0.441 (34) | 0.121 | flat +0.000 (noise 0.031) |
| reversal_k8_now | 0.660 (53) | 0.688 (353) [0.666, 0.709] | 0.688 (1540) [0.669, 0.706] | 0.701 (3534) [0.688, 0.714] | 0.690 (1947) [0.672, 0.707] | 0.619 (21) | 0.121 | flat -0.015 (noise 0.034) |
| overall | 0.509 (21525) | 0.506 (153404) [0.504, 0.508] | 0.505 (661591) [0.504, 0.507] | 0.504 (1499084) [0.503, 0.505] | 0.505 (815803) [0.504, 0.506] | 0.497 (9352) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07823, 0.1187] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5308, 'levels': [{'threshold': 0.07823, 'calls_per_day': 143.5, 'win_rate': 0.5787}, {'threshold': 0.1187, 'calls_per_day': 36.0, 'win_rate': 0.6235}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42808, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15084 | 0.339 | 0.530 (14782) | 0.570 (2462) | 0.740 (2539) |
| volatility: normal | 15084 | 0.367 | 0.536 (15016) | 0.619 (1461) | 0.754 (2244) |
| volatility: wild | 15084 | 0.384 | 0.524 (15043) | 0.611 (837) | 0.765 (2070) |
| session: Asia 00-08 | 15360 | 0.363 | 0.535 (15223) | 0.599 (1680) | 0.756 (2272) |
| session: Europe 08-13 | 9432 | 0.356 | 0.533 (9322) | 0.590 (1265) | 0.746 (1520) |
| session: US 13-21 | 14880 | 0.370 | 0.527 (14765) | 0.596 (1240) | 0.755 (2273) |
| session: late 21-24 | 5580 | 0.356 | 0.515 (5531) | 0.569 (575) | 0.745 (788) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.391 | 0.398 | 0.332 | 0.332 | 0.467 | 0.252 | 0.529 | 1.489 |
| 6h | 360 | 0.381 | 0.384 | 0.309 | 0.343 | 0.483 | 0.249 | 0.514 | 1.221 |
| 24h | 1440 | 0.372 | 0.360 | 0.285 | 0.317 | 0.541 | 0.271 | 0.472 | 1.468 |
| 7d | 10080 | 0.367 | 0.361 | 0.277 | 0.309 | 0.529 | 0.263 | 0.471 | 1.324 |
| 30d | 43200 | 0.364 | 0.356 | 0.275 | 0.306 | 0.530 | 0.263 | 0.465 | 1.270 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.391 / 0.467 / 0.967; 2: 0.410 / 0.583 / 0.883; 3: 0.394 / 0.500 / 0.867; 4: 0.373 / 0.450 / 0.883; 5: 0.404 / 0.550 / 0.867; 6: 0.376 / 0.467 / 0.817; 7: 0.391 / 0.500 / 0.900; 8: 0.421 / 0.567 / 0.900; 9: 0.375 / 0.450 / 0.917; 10: 0.427 / 0.583 / 0.850; 11: 0.346 / 0.400 / 0.817; 12: 0.394 / 0.517 / 0.800; 13: 0.392 / 0.483 / 0.833; 14: 0.388 / 0.500 / 0.867; 15: 0.398 / 0.500 / 0.900
- 6h: 1: 0.381 / 0.483 / 0.911; 2: 0.389 / 0.494 / 0.875; 3: 0.386 / 0.489 / 0.847; 4: 0.377 / 0.478 / 0.872; 5: 0.391 / 0.517 / 0.881; 6: 0.373 / 0.472 / 0.858; 7: 0.385 / 0.497 / 0.861; 8: 0.388 / 0.508 / 0.881; 9: 0.384 / 0.497 / 0.878; 10: 0.394 / 0.528 / 0.842; 11: 0.378 / 0.497 / 0.839; 12: 0.386 / 0.514 / 0.833; 13: 0.383 / 0.500 / 0.847; 14: 0.377 / 0.480 / 0.858; 15: 0.383 / 0.461 / 0.858
- 24h: 1: 0.372 / 0.541 / 0.896; 2: 0.359 / 0.496 / 0.903; 3: 0.362 / 0.516 / 0.894; 4: 0.354 / 0.488 / 0.898; 5: 0.360 / 0.504 / 0.901; 6: 0.352 / 0.485 / 0.900; 7: 0.352 / 0.492 / 0.900; 8: 0.357 / 0.500 / 0.907; 9: 0.358 / 0.507 / 0.912; 10: 0.353 / 0.507 / 0.900; 11: 0.356 / 0.507 / 0.903; 12: 0.355 / 0.512 / 0.903; 13: 0.352 / 0.484 / 0.913; 14: 0.357 / 0.519 / 0.917; 15: 0.353 / 0.490 / 0.915
- 7d: 1: 0.367 / 0.529 / 0.895; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.514 / 0.898; 4: 0.355 / 0.499 / 0.899; 5: 0.355 / 0.502 / 0.899; 6: 0.353 / 0.502 / 0.899; 7: 0.353 / 0.500 / 0.899; 8: 0.353 / 0.499 / 0.900; 9: 0.355 / 0.508 / 0.899; 10: 0.352 / 0.500 / 0.898; 11: 0.352 / 0.502 / 0.898; 12: 0.353 / 0.507 / 0.899; 13: 0.352 / 0.494 / 0.899; 14: 0.353 / 0.507 / 0.899; 15: 0.351 / 0.499 / 0.900
- 30d: 1: 0.364 / 0.530 / 0.897; 2: 0.352 / 0.494 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.499 / 0.900; 8: 0.349 / 0.504 / 0.900; 9: 0.350 / 0.503 / 0.900; 10: 0.350 / 0.504 / 0.900; 11: 0.347 / 0.499 / 0.899; 12: 0.349 / 0.504 / 0.899; 13: 0.347 / 0.499 / 0.900; 14: 0.347 / 0.501 / 0.900; 15: 0.348 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.166 (body 0.120, range 0.212); 'price stays where it was' would score 0.154; colour right 0.433; typical miss of the close 12.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.080, range 0.172); 'price stays where it was' would score 0.129; colour right 0.492; typical miss of the close 14.8 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.121 (body 0.082, range 0.161); 'price stays where it was' would score 0.131; colour right 0.493; typical miss of the close 8.6 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.124 (body 0.084, range 0.164); 'price stays where it was' would score 0.125; colour right 0.504; typical miss of the close 8.7 bp; chain ended on the right side 0.503 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.4 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.4; 2: 0.199 / 5.1; 3: 0.167 / 6.6; 4: 0.132 / 6.9; 5: 0.126 / 7.6; 6: 0.115 / 8.3; 7: 0.111 / 8.6; 8: 0.097 / 9.6; 9: 0.091 / 9.5; 10: 0.092 / 10.1; 11: 0.087 / 10.2; 12: 0.078 / 10.6; 13: 0.073 / 10.9; 14: 0.070 / 11.4; 15: 0.066 / 11.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 141486, probability skill vs chance 0.2186, widened contest next: False
  - now: threshold 0.8384, hit rate recent 0.9415 / long run 0.9301
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.301, naive rule 0.509, lift 3.32x
    - 24h: 56 calls (56 a day), hit rate 0.964, chance 0.292, naive rule 0.492, lift 3.30x
    - 7d: 404 calls (58 a day), hit rate 0.923, chance 0.296, naive rule 0.496, lift 3.12x
    - 30d: 1732 calls (58 a day), hit rate 0.934, chance 0.295, naive rule 0.497, lift 3.16x
  - next: threshold 0.5663, hit rate recent 0.6425 / long run 0.611
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.301, lift 2.28x
    - 24h: 53 calls (53 a day), hit rate 0.698, chance 0.292, lift 2.39x
    - 7d: 415 calls (59 a day), hit rate 0.617, chance 0.296, lift 2.08x
    - 30d: 2926 calls (98 a day), hit rate 0.593, chance 0.295, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.501; 0.35: 534, 0.526; 0.40: 474, 0.581; 0.45: 406, 0.651; 0.50: 355, 0.699; 0.55: 308, 0.743; 0.60: 260, 0.786; 0.65: 219, 0.812; 0.70: 173, 0.844; 0.75: 139, 0.875; 0.80: 92, 0.907; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.430; 0.35: 498, 0.464; 0.40: 401, 0.502; 0.45: 303, 0.537; 0.50: 196, 0.570; 0.55: 89, 0.581; 0.60: 12, 0.652; 0.65: 1, 0.619
- **K=5**: model 1792540800, labels learned 141484, probability skill vs chance 0.2041, widened contest next: True
  - now: threshold 0.6848, hit rate recent 0.7277 / long run 0.8079
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.169, naive rule 0.376, lift 3.65x
    - 24h: 51 calls (51 a day), hit rate 0.686, chance 0.175, naive rule 0.386, lift 3.93x
    - 7d: 370 calls (53 a day), hit rate 0.803, chance 0.186, naive rule 0.401, lift 4.32x
    - 30d: 1624 calls (54 a day), hit rate 0.817, chance 0.187, naive rule 0.408, lift 4.37x
  - next: threshold 0.4545, hit rate recent 0.5576 / long run 0.5202
    - 6h: 10 calls (41 a day), hit rate 0.500, chance 0.169, lift 2.97x
    - 24h: 62 calls (62 a day), hit rate 0.581, chance 0.175, lift 3.32x
    - 7d: 407 calls (58 a day), hit rate 0.526, chance 0.186, lift 2.83x
    - 30d: 2703 calls (90 a day), hit rate 0.488, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.423; 0.35: 350, 0.487; 0.40: 283, 0.558; 0.45: 232, 0.609; 0.50: 186, 0.658; 0.55: 150, 0.695; 0.60: 113, 0.744; 0.65: 76, 0.783; 0.70: 47, 0.821; 0.75: 28, 0.851; 0.80: 10, 0.864
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 349, 0.384; 0.35: 257, 0.423; 0.40: 161, 0.462; 0.45: 67, 0.495; 0.50: 11, 0.527; 0.55: 1, 0.421
- **K=8**: model 1794182400, labels learned 141481, probability skill vs chance 0.1926, widened contest next: False
  - now: threshold 0.5706, hit rate recent 0.6764 / long run 0.6913
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.120, naive rule 0.341, lift 5.95x
    - 24h: 50 calls (50 a day), hit rate 0.640, chance 0.118, naive rule 0.325, lift 5.42x
    - 7d: 358 calls (51 a day), hit rate 0.690, chance 0.122, naive rule 0.337, lift 5.67x
    - 30d: 1536 calls (51 a day), hit rate 0.687, chance 0.121, naive rule 0.335, lift 5.69x
  - next: threshold 0.3606, hit rate recent 0.3906 / long run 0.4128
    - 6h: 24 calls (99 a day), hit rate 0.417, chance 0.120, lift 3.47x
    - 24h: 89 calls (90 a day), hit rate 0.371, chance 0.118, lift 3.14x
    - 7d: 431 calls (62 a day), hit rate 0.415, chance 0.122, lift 3.42x
    - 30d: 2644 calls (88 a day), hit rate 0.393, chance 0.121, lift 3.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.430; 0.35: 192, 0.492; 0.40: 152, 0.538; 0.45: 118, 0.585; 0.50: 85, 0.638; 0.55: 60, 0.674; 0.60: 40, 0.712; 0.65: 24, 0.782; 0.70: 12, 0.807; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.362; 0.35: 88, 0.389; 0.40: 24, 0.423; 0.45: 4, 0.442; 0.50: 1, 0.727
- **K=13**: model 1794096000, labels learned 141476, probability skill vs chance 0.167, widened contest next: True
  - now: threshold 0.4407, hit rate recent 0.5197 / long run 0.5634
    - 6h: 9 calls (38 a day), hit rate 0.444, chance 0.091, naive rule 0.330, lift 4.87x
    - 24h: 58 calls (59 a day), hit rate 0.483, chance 0.076, naive rule 0.279, lift 6.34x
    - 7d: 370 calls (53 a day), hit rate 0.565, chance 0.079, naive rule 0.284, lift 7.13x
    - 30d: 1653 calls (55 a day), hit rate 0.558, chance 0.077, naive rule 0.281, lift 7.21x
  - next: threshold 0.2847, hit rate recent 0.2991 / long run 0.3229
    - 6h: 22 calls (92 a day), hit rate 0.318, chance 0.091, lift 3.48x
    - 24h: 101 calls (102 a day), hit rate 0.307, chance 0.076, lift 4.03x
    - 7d: 462 calls (66 a day), hit rate 0.327, chance 0.079, lift 4.13x
    - 30d: 1838 calls (61 a day), hit rate 0.321, chance 0.077, lift 4.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 132, 0.433; 0.35: 96, 0.479; 0.40: 67, 0.537; 0.45: 46, 0.580; 0.50: 31, 0.640; 0.55: 20, 0.665; 0.60: 12, 0.699; 0.65: 4, 0.667; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.326; 0.35: 13, 0.341; 0.40: 3, 0.412; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.944 | 0.73% | 0.950 | 0.550 | 0.249 | 0.550 | 0.053 |
| 6h | 21.627 | 4.64% | 0.911 | 0.492 | 0.250 | 0.500 | 0.510 |
| 24h | 18.548 | 11.38% | 0.901 | 0.501 | 0.251 | 0.497 | 0.678 |
| 7d | 16.057 | 6.35% | 0.900 | 0.500 | 0.250 | 0.503 | 0.729 |
| 30d | 15.156 | 4.73% | 0.900 | 0.500 | 0.250 | 0.500 | 0.707 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.069 | 16.975 | 17.124 | 17.325 | 17.263 | 17.122 | 17.015 | 17.030 | 16.987 | 16.944 |
| 6h | 22.679 | 21.653 | 21.773 | 21.843 | 21.885 | 22.053 | 21.597 | 21.575 | 21.564 | 21.627 |
| 24h | 20.929 | 18.668 | 18.660 | 18.976 | 18.748 | 19.043 | 18.464 | 18.441 | 18.499 | 18.548 |
| 7d | 17.146 | 16.183 | 16.159 | 16.165 | 16.312 | 16.472 | 16.030 | 16.022 | 16.026 | 16.057 |
| 30d | 15.909 | 15.309 | 15.255 | 15.199 | 15.433 | 15.412 | 15.144 | 15.124 | 15.127 | 15.156 |

## Next candle

- candle starting 2026-11-09 10:12 UTC, last close 2099.1
- P(up) 0.4991, return quantiles (bp): {'05': -15.285, '10': -10.523, '25': -5.186, '40': -1.707, '50': -0.05, '60': 2.51, '75': 5.591, '90': 10.317, '95': 13.283}
- changepoint probability 0.0454, regime age 69.7 min
- agent weights: empirical 0.003, ewma 0.065, garch 0.060, har 0.006, bocpd 0.034, hmm 0.004, online_qr 0.363, lgbm 0.465

## Learning log

- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- 2026-11-09 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.28, 5.65, 17.98], "stay": [0.986, 0.971, 0.95]}, "lgbm": {"challenger_loss": 0.25622, "champion_loss": 0.25616, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49957, "challengers": 1, "chance_loss": 0.61466, "widened": false, "champion_loss": 0.49809, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38152, "challengers": 3, "chance_loss": 0.48512, "widened": true, "champion_loss": 0.38142, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28752, "challengers": 3, "chance_loss": 0.37546, "widened": true, "champion_loss": 0.28781, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19596, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.19541, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.28, 5.65, 17.98], current probabilities: [0.0, 0.793, 0.207]
- live generator: {'versions': 60, 'latest_effective': '2026-11-09 10:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.306, 'l_abs': 0.674, 'l_hi': 0.741, 'l_lo': 0.689, 'b05': 0.664, 'b25': 0.648, 'b75': 0.61, 'b95': 0.645}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.426, 2.315, 2.107, 2.268, 2.696, 2.86, 2.559, 2.831, 3.801, 3.995, 4.098, 3.945, 4.021, 4.088]}
- calibration offsets (in sigma): {'05': -0.0545, '10': -0.049, '25': -0.0325, '40': -0.036, '50': -0.055, '60': -0.034, '75': -0.0575, '90': -0.041, '95': -0.0755}
