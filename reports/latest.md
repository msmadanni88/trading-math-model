# ETH-USD 60s candle generator - report

- generated: 2026-10-27 20:47 UTC
- last closed candle: 2026-10-27 20:47 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.530 (672) [0.494, 0.569] | 0.522 (2876) [0.503, 0.542] | 0.516 (5274) [0.503, 0.530] | 0.523 (2302) [0.499, 0.546] | 0.542 (83) | 0.500 | flat -0.009 (noise 0.032) |
| colour_clear | 0.538 (824) | 0.548 (5704) [0.540, 0.558] | 0.536 (23552) [0.528, 0.543] | 0.518 (43117) [0.512, 0.524] | 0.546 (18879) [0.541, 0.550] | 0.558 (736) | 0.500 | flat -0.001 (noise 0.009) |
| colour_confident | 0.613 (160) | 0.601 (1419) [0.588, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.600 (145) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.522 (1432) | 0.531 (10039) [0.525, 0.537] | 0.524 (42872) [0.520, 0.529] | 0.513 (78622) [0.509, 0.517] | 0.529 (34273) [0.525, 0.533] | 0.534 (1238) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.499 (20048) | 0.500 (140546) [0.498, 0.503] | 0.501 (600208) [0.499, 0.502] | 0.501 (1100708) [0.500, 0.502] | 0.500 (479822) [0.499, 0.502] | 0.507 (17332) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.604 (53) | 0.626 (420) [0.602, 0.667] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.614 (44) | 0.500 | flat +0.015 (noise 0.045) |
| reversal_k13_next | 0.271 (59) | 0.312 (442) [0.287, 0.336] | 0.304 (2171) [0.292, 0.316] | 0.307 (3743) [0.297, 0.318] | 0.316 (1638) [0.305, 0.327] | 0.463 (41) | 0.076 | flat +0.012 (noise 0.031) |
| reversal_k13_now | 0.457 (70) | 0.546 (370) [0.500, 0.594] | 0.561 (1601) [0.541, 0.583] | 0.571 (2776) [0.555, 0.587] | 0.560 (1304) [0.537, 0.585] | 0.625 (48) | 0.076 | flat +0.011 (noise 0.036) |
| reversal_k3_next | 0.590 (117) | 0.600 (678) [0.572, 0.628] | 0.582 (2864) [0.570, 0.595] | 0.584 (4759) [0.574, 0.595] | 0.580 (2319) [0.567, 0.595] | 0.563 (103) | 0.293 | flat +0.039 (noise 0.026) |
| reversal_k3_now | 0.983 (57) | 0.946 (389) [0.921, 0.968] | 0.936 (1694) [0.927, 0.946] | 0.938 (3126) [0.931, 0.945] | 0.933 (1363) [0.922, 0.944] | 0.967 (60) | 0.293 | flat +0.008 (noise 0.021) |
| reversal_k5_next | 0.509 (110) | 0.479 (893) [0.448, 0.502] | 0.465 (3032) [0.451, 0.478] | 0.477 (4553) [0.465, 0.490] | 0.464 (2563) [0.449, 0.480] | 0.551 (49) | 0.187 | flat +0.027 (noise 0.024) |
| reversal_k5_now | 0.833 (54) | 0.820 (361) [0.808, 0.831] | 0.829 (1568) [0.816, 0.842] | 0.830 (2874) [0.819, 0.840] | 0.820 (1263) [0.807, 0.833] | 0.852 (54) | 0.187 | flat +0.002 (noise 0.029) |
| reversal_k8_next | 0.336 (110) | 0.379 (755) [0.359, 0.396] | 0.380 (2651) [0.368, 0.392] | 0.388 (4416) [0.377, 0.399] | 0.380 (2310) [0.367, 0.394] | 0.388 (85) | 0.120 | flat +0.014 (noise 0.025) |
| reversal_k8_now | 0.545 (55) | 0.658 (342) [0.608, 0.707] | 0.689 (1530) [0.667, 0.710] | 0.699 (2842) [0.683, 0.715] | 0.680 (1255) [0.657, 0.705] | 0.726 (51) | 0.121 | flat -0.014 (noise 0.036) |
| overall | 0.501 (22208) | 0.504 (155487) [0.501, 0.507] | 0.504 (663067) [0.503, 0.505] | 0.503 (1213693) [0.502, 0.504] | 0.504 (530412) [0.502, 0.506] | 0.512 (19144) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08007, 0.1205] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5285, 'levels': [{'threshold': 0.08007, 'calls_per_day': 145.9, 'win_rate': 0.6043}, {'threshold': 0.1205, 'calls_per_day': 37.4, 'win_rate': 0.6236}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 34372, 'rate': 0.5303}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15296 | 0.336 | 0.523 (15045) | 0.589 (1758) | 0.762 (2559) |
| volatility: normal | 15295 | 0.365 | 0.527 (15223) | 0.607 (1336) | 0.753 (2260) |
| volatility: wild | 15296 | 0.379 | 0.522 (15251) | 0.629 (672) | 0.767 (1978) |
| session: Asia 00-08 | 15360 | 0.359 | 0.531 (15249) | 0.609 (1324) | 0.764 (2239) |
| session: Europe 08-13 | 9600 | 0.356 | 0.528 (9511) | 0.596 (931) | 0.755 (1534) |
| session: US 13-21 | 15347 | 0.367 | 0.519 (15241) | 0.597 (976) | 0.770 (2193) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.609 (535) | 0.737 (831) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.359 | 0.384 | 0.318 | 0.318 | 0.500 | 0.248 | 0.470 | 1.253 |
| 6h | 360 | 0.365 | 0.370 | 0.293 | 0.331 | 0.506 | 0.244 | 0.486 | 1.263 |
| 24h | 1440 | 0.368 | 0.362 | 0.291 | 0.321 | 0.531 | 0.259 | 0.477 | 1.210 |
| 7d | 10080 | 0.369 | 0.359 | 0.280 | 0.312 | 0.529 | 0.265 | 0.472 | 1.223 |
| 30d | 43200 | 0.362 | 0.355 | 0.278 | 0.307 | 0.525 | 0.258 | 0.466 | 1.275 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.359 / 0.500 / 0.900; 2: 0.343 / 0.450 / 0.900; 3: 0.381 / 0.517 / 0.933; 4: 0.378 / 0.550 / 0.967; 5: 0.368 / 0.517 / 0.983; 6: 0.355 / 0.517 / 0.950; 7: 0.362 / 0.517 / 0.967; 8: 0.363 / 0.500 / 0.967; 9: 0.353 / 0.483 / 1.000; 10: 0.365 / 0.483 / 1.000; 11: 0.354 / 0.450 / 1.000; 12: 0.367 / 0.467 / 1.000; 13: 0.370 / 0.500 / 1.000; 14: 0.388 / 0.650 / 0.983; 15: 0.353 / 0.483 / 0.967
- 6h: 1: 0.365 / 0.506 / 0.900; 2: 0.364 / 0.506 / 0.886; 3: 0.376 / 0.528 / 0.928; 4: 0.363 / 0.508 / 0.919; 5: 0.372 / 0.517 / 0.928; 6: 0.366 / 0.534 / 0.922; 7: 0.370 / 0.534 / 0.936; 8: 0.372 / 0.522 / 0.922; 9: 0.354 / 0.480 / 0.942; 10: 0.372 / 0.528 / 0.964; 11: 0.375 / 0.542 / 0.953; 12: 0.367 / 0.520 / 0.956; 13: 0.374 / 0.536 / 0.958; 14: 0.361 / 0.494 / 0.958; 15: 0.366 / 0.500 / 0.950
- 24h: 1: 0.368 / 0.531 / 0.892; 2: 0.358 / 0.493 / 0.899; 3: 0.365 / 0.512 / 0.897; 4: 0.359 / 0.494 / 0.896; 5: 0.359 / 0.518 / 0.901; 6: 0.357 / 0.513 / 0.898; 7: 0.359 / 0.514 / 0.901; 8: 0.359 / 0.510 / 0.901; 9: 0.356 / 0.495 / 0.908; 10: 0.360 / 0.510 / 0.911; 11: 0.355 / 0.503 / 0.908; 12: 0.357 / 0.498 / 0.912; 13: 0.360 / 0.515 / 0.911; 14: 0.358 / 0.504 / 0.908; 15: 0.356 / 0.488 / 0.910
- 7d: 1: 0.369 / 0.529 / 0.895; 2: 0.357 / 0.497 / 0.899; 3: 0.358 / 0.510 / 0.900; 4: 0.355 / 0.499 / 0.899; 5: 0.355 / 0.507 / 0.900; 6: 0.353 / 0.500 / 0.900; 7: 0.353 / 0.500 / 0.900; 8: 0.355 / 0.509 / 0.900; 9: 0.353 / 0.501 / 0.901; 10: 0.353 / 0.505 / 0.901; 11: 0.350 / 0.497 / 0.901; 12: 0.352 / 0.503 / 0.901; 13: 0.350 / 0.498 / 0.901; 14: 0.351 / 0.497 / 0.901; 15: 0.352 / 0.503 / 0.901
- 30d: 1: 0.362 / 0.525 / 0.898; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.499 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.347 / 0.496 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.347 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.138 (body 0.072, range 0.204); 'price stays where it was' would score 0.163; colour right 0.600; typical miss of the close 5.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.120 (body 0.072, range 0.169); 'price stays where it was' would score 0.141; colour right 0.506; typical miss of the close 8.7 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.132 (body 0.086, range 0.177); 'price stays where it was' would score 0.139; colour right 0.497; typical miss of the close 8.6 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.130 (body 0.088, range 0.171); 'price stays where it was' would score 0.138; colour right 0.501; typical miss of the close 8.6 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.162); 'price stays where it was' would score 0.128; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.1; 2: 0.198 / 4.6; 3: 0.169 / 6.1; 4: 0.132 / 6.6; 5: 0.125 / 7.3; 6: 0.112 / 7.8; 7: 0.107 / 8.2; 8: 0.096 / 8.6; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.086 / 9.8; 12: 0.077 / 10.1; 13: 0.067 / 10.4; 14: 0.070 / 10.7; 15: 0.061 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 123401, probability skill vs chance 0.2421, widened contest next: True
  - now: threshold 0.8345, hit rate recent 0.9643 / long run 0.9411
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.279, naive rule 0.470, lift 3.59x
    - 24h: 64 calls (64 a day), hit rate 0.969, chance 0.292, naive rule 0.487, lift 3.32x
    - 7d: 398 calls (57 a day), hit rate 0.955, chance 0.298, naive rule 0.505, lift 3.20x
    - 30d: 1713 calls (57 a day), hit rate 0.937, chance 0.293, naive rule 0.491, lift 3.20x
  - next: threshold 0.5349, hit rate recent 0.5499 / long run 0.5857
    - 6h: 29 calls (118 a day), hit rate 0.517, chance 0.279, lift 1.85x
    - 24h: 122 calls (122 a day), hit rate 0.574, chance 0.292, lift 1.97x
    - 7d: 673 calls (96 a day), hit rate 0.606, chance 0.298, lift 2.03x
    - 30d: 2874 calls (96 a day), hit rate 0.582, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.519; 0.40: 477, 0.576; 0.45: 408, 0.646; 0.50: 356, 0.698; 0.55: 312, 0.740; 0.60: 264, 0.785; 0.65: 221, 0.811; 0.70: 174, 0.843; 0.75: 136, 0.875; 0.80: 91, 0.915; 0.85: 47, 0.952; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 501, 0.465; 0.40: 407, 0.499; 0.45: 310, 0.533; 0.50: 200, 0.570; 0.55: 89, 0.574; 0.60: 13, 0.643; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 123399, probability skill vs chance 0.2266, widened contest next: False
  - now: threshold 0.6717, hit rate recent 0.8447 / long run 0.8246
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.184, naive rule 0.402, lift 5.43x
    - 24h: 60 calls (60 a day), hit rate 0.833, chance 0.191, naive rule 0.415, lift 4.37x
    - 7d: 369 calls (53 a day), hit rate 0.824, chance 0.185, naive rule 0.408, lift 4.44x
    - 30d: 1583 calls (53 a day), hit rate 0.826, chance 0.187, naive rule 0.400, lift 4.41x
  - next: threshold 0.4376, hit rate recent 0.5246 / long run 0.4861
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.184, lift 3.39x
    - 24h: 62 calls (62 a day), hit rate 0.565, chance 0.191, lift 2.96x
    - 7d: 827 calls (118 a day), hit rate 0.495, chance 0.185, lift 2.67x
    - 30d: 3047 calls (102 a day), hit rate 0.466, chance 0.187, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.425; 0.35: 345, 0.491; 0.40: 278, 0.564; 0.45: 226, 0.618; 0.50: 178, 0.667; 0.55: 138, 0.709; 0.60: 106, 0.751; 0.65: 76, 0.788; 0.70: 52, 0.828; 0.75: 30, 0.872; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.390; 0.35: 253, 0.420; 0.40: 158, 0.453; 0.45: 70, 0.469; 0.50: 15, 0.488; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 123396, probability skill vs chance 0.2037, widened contest next: False
  - now: threshold 0.5571, hit rate recent 0.6782 / long run 0.6774
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.113, naive rule 0.321, lift 7.97x
    - 24h: 57 calls (57 a day), hit rate 0.702, chance 0.124, naive rule 0.346, lift 5.67x
    - 7d: 357 calls (51 a day), hit rate 0.669, chance 0.117, naive rule 0.326, lift 5.73x
    - 30d: 1534 calls (51 a day), hit rate 0.686, chance 0.121, naive rule 0.330, lift 5.68x
  - next: threshold 0.335, hit rate recent 0.3704 / long run 0.3766
    - 6h: 23 calls (95 a day), hit rate 0.391, chance 0.113, lift 3.47x
    - 24h: 99 calls (100 a day), hit rate 0.384, chance 0.124, lift 3.10x
    - 7d: 744 calls (106 a day), hit rate 0.378, chance 0.117, lift 3.23x
    - 30d: 2682 calls (89 a day), hit rate 0.380, chance 0.121, lift 3.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 188, 0.496; 0.40: 145, 0.546; 0.45: 111, 0.591; 0.50: 84, 0.634; 0.55: 60, 0.670; 0.60: 40, 0.712; 0.65: 23, 0.780; 0.70: 10, 0.825; 0.75: 2, 0.818
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.354; 0.35: 94, 0.381; 0.40: 33, 0.404; 0.45: 7, 0.428; 0.50: 1, 0.613
- **K=13**: model 1793059200, labels learned 123391, probability skill vs chance 0.2009, widened contest next: False
  - now: threshold 0.4056, hit rate recent 0.573 / long run 0.556
    - 6h: 11 calls (46 a day), hit rate 0.818, chance 0.083, naive rule 0.317, lift 9.90x
    - 24h: 57 calls (58 a day), hit rate 0.614, chance 0.082, naive rule 0.314, lift 7.51x
    - 7d: 373 calls (53 a day), hit rate 0.560, chance 0.074, naive rule 0.272, lift 7.56x
    - 30d: 1608 calls (54 a day), hit rate 0.560, chance 0.077, naive rule 0.273, lift 7.28x
  - next: threshold 0.2948, hit rate recent 0.3754 / long run 0.3198
    - 6h: 6 calls (25 a day), hit rate 0.333, chance 0.083, lift 4.04x
    - 24h: 49 calls (50 a day), hit rate 0.408, chance 0.082, lift 4.99x
    - 7d: 418 calls (60 a day), hit rate 0.316, chance 0.074, lift 4.26x
    - 30d: 2159 calls (72 a day), hit rate 0.308, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.440; 0.35: 89, 0.490; 0.40: 63, 0.545; 0.45: 42, 0.596; 0.50: 27, 0.656; 0.55: 16, 0.706; 0.60: 7, 0.749; 0.65: 2, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.323; 0.35: 14, 0.360; 0.40: 2, 0.451; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.971 | 5.67% | 0.933 | 0.550 | 0.249 | 0.583 | 0.352 |
| 6h | 13.335 | 1.89% | 0.903 | 0.511 | 0.250 | 0.514 | 0.572 |
| 24h | 13.850 | 1.99% | 0.897 | 0.503 | 0.250 | 0.501 | 0.508 |
| 7d | 14.740 | 3.45% | 0.900 | 0.500 | 0.250 | 0.500 | 0.652 |
| 30d | 13.851 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.666 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.510 | 8.904 | 9.029 | 8.942 | 9.069 | 9.085 | 8.959 | 8.893 | 8.936 | 8.971 |
| 6h | 13.592 | 13.403 | 13.419 | 13.402 | 13.601 | 13.413 | 13.294 | 13.249 | 13.301 | 13.335 |
| 24h | 14.132 | 13.929 | 13.905 | 13.889 | 14.067 | 13.919 | 13.833 | 13.799 | 13.819 | 13.850 |
| 7d | 15.267 | 14.881 | 14.826 | 14.768 | 15.002 | 14.886 | 14.725 | 14.699 | 14.711 | 14.740 |
| 30d | 14.445 | 13.984 | 13.936 | 13.877 | 14.098 | 14.030 | 13.846 | 13.826 | 13.825 | 13.851 |

## Next candle

- candle starting 2026-10-27 20:47 UTC, last close 2338.91
- P(up) 0.4831, return quantiles (bp): {'05': -5.009, '10': -4.001, '25': -2.031, '40': -0.734, '50': -0.126, '60': 0.634, '75': 1.941, '90': 3.743, '95': 5.403}
- changepoint probability 0.038, regime age 106.7 min
- agent weights: empirical 0.020, ewma 0.106, garch 0.107, har 0.132, bocpd 0.035, hmm 0.093, online_qr 0.226, lgbm 0.282

## Learning log

- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- HMM volatility states (sd, bp per minute): [3.43, 6.6, 17.85], current probabilities: [0.969, 0.03, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-27 20:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.267, 'l_abs': 0.713, 'l_hi': 0.773, 'l_lo': 0.792, 'b05': 0.735, 'b25': 0.782, 'b75': 0.602, 'b95': 0.727}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.469, 1.664, 2.128, 2.201, 2.415, 2.512, 2.745, 2.587, 2.679, 2.705, 2.83, 2.78, 3.009, 3.121]}
- calibration offsets (in sigma): {'05': 0.053, '10': 0.006, '25': -0.015, '40': -0.026, '50': -0.05, '60': -0.044, '75': -0.005, '90': -0.026, '95': 0.057}
