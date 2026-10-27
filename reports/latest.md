# ETH-USD 60s candle generator - report

- generated: 2026-10-27 10:56 UTC
- last closed candle: 2026-10-27 10:56 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.530 (672) [0.494, 0.569] | 0.522 (2876) [0.503, 0.542] | 0.516 (5274) [0.503, 0.530] | 0.523 (2302) [0.499, 0.546] | 0.535 (43) | 0.500 | flat -0.009 (noise 0.032) |
| colour_clear | 0.538 (824) | 0.548 (5704) [0.540, 0.558] | 0.536 (23552) [0.528, 0.543] | 0.518 (43117) [0.512, 0.524] | 0.546 (18879) [0.541, 0.550] | 0.572 (397) | 0.500 | flat -0.001 (noise 0.009) |
| colour_confident | 0.613 (160) | 0.601 (1419) [0.588, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.629 (70) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.522 (1432) | 0.531 (10039) [0.525, 0.537] | 0.524 (42872) [0.520, 0.529] | 0.513 (78622) [0.509, 0.517] | 0.529 (34273) [0.525, 0.533] | 0.544 (649) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.499 (20048) | 0.500 (140546) [0.498, 0.503] | 0.501 (600208) [0.499, 0.502] | 0.501 (1100708) [0.500, 0.502] | 0.500 (479822) [0.499, 0.502] | 0.497 (9086) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.604 (53) | 0.626 (420) [0.602, 0.667] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.700 (20) | 0.500 | flat +0.015 (noise 0.045) |
| reversal_k13_next | 0.271 (59) | 0.312 (442) [0.287, 0.336] | 0.304 (2171) [0.292, 0.316] | 0.307 (3743) [0.297, 0.318] | 0.316 (1638) [0.305, 0.327] | 0.400 (20) | 0.076 | flat +0.012 (noise 0.031) |
| reversal_k13_now | 0.457 (70) | 0.546 (370) [0.500, 0.594] | 0.561 (1601) [0.541, 0.583] | 0.571 (2776) [0.555, 0.587] | 0.560 (1304) [0.537, 0.585] | 0.667 (21) | 0.076 | flat +0.011 (noise 0.036) |
| reversal_k3_next | 0.590 (117) | 0.600 (678) [0.572, 0.628] | 0.582 (2864) [0.570, 0.595] | 0.584 (4759) [0.574, 0.595] | 0.580 (2319) [0.567, 0.595] | 0.550 (60) | 0.293 | flat +0.039 (noise 0.026) |
| reversal_k3_now | 0.983 (57) | 0.946 (389) [0.921, 0.968] | 0.936 (1694) [0.927, 0.946] | 0.938 (3126) [0.931, 0.945] | 0.933 (1363) [0.922, 0.944] | 0.971 (34) | 0.293 | flat +0.008 (noise 0.021) |
| reversal_k5_next | 0.509 (110) | 0.479 (893) [0.448, 0.502] | 0.465 (3032) [0.451, 0.478] | 0.477 (4553) [0.465, 0.490] | 0.464 (2563) [0.449, 0.480] | 0.571 (28) | 0.187 | flat +0.027 (noise 0.024) |
| reversal_k5_now | 0.833 (54) | 0.820 (361) [0.808, 0.831] | 0.829 (1568) [0.816, 0.842] | 0.830 (2874) [0.819, 0.840] | 0.820 (1263) [0.807, 0.833] | 0.844 (32) | 0.187 | flat +0.002 (noise 0.029) |
| reversal_k8_next | 0.336 (110) | 0.379 (755) [0.359, 0.396] | 0.380 (2651) [0.368, 0.392] | 0.388 (4416) [0.377, 0.399] | 0.380 (2310) [0.367, 0.394] | 0.405 (42) | 0.120 | flat +0.014 (noise 0.025) |
| reversal_k8_now | 0.545 (55) | 0.658 (342) [0.608, 0.707] | 0.689 (1530) [0.667, 0.710] | 0.699 (2842) [0.683, 0.715] | 0.680 (1255) [0.657, 0.705] | 0.808 (26) | 0.121 | flat -0.014 (noise 0.036) |
| overall | 0.501 (22208) | 0.504 (155487) [0.501, 0.507] | 0.504 (663067) [0.503, 0.505] | 0.503 (1213693) [0.502, 0.504] | 0.504 (530412) [0.502, 0.506] | 0.504 (10041) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07944, 0.1188] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5298, 'levels': [{'threshold': 0.07944, 'calls_per_day': 145.8, 'win_rate': 0.6098}, {'threshold': 0.1188, 'calls_per_day': 36.4, 'win_rate': 0.6367}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 33783, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15099 | 0.336 | 0.523 (14852) | 0.588 (1742) | 0.763 (2515) |
| volatility: normal | 15098 | 0.365 | 0.527 (15025) | 0.608 (1310) | 0.755 (2254) |
| volatility: wild | 15099 | 0.379 | 0.522 (15053) | 0.635 (639) | 0.763 (1928) |
| session: Asia 00-08 | 15360 | 0.359 | 0.531 (15249) | 0.609 (1324) | 0.764 (2239) |
| session: Europe 08-13 | 9476 | 0.356 | 0.528 (9387) | 0.599 (911) | 0.759 (1508) |
| session: US 13-21 | 14880 | 0.367 | 0.519 (14776) | 0.596 (921) | 0.767 (2119) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.609 (535) | 0.737 (831) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.389 | 0.369 | 0.324 | 0.324 | 0.678 | 0.264 | 0.514 | 1.278 |
| 6h | 360 | 0.374 | 0.364 | 0.299 | 0.310 | 0.551 | 0.267 | 0.480 | 1.236 |
| 24h | 1440 | 0.367 | 0.360 | 0.292 | 0.320 | 0.526 | 0.257 | 0.477 | 1.167 |
| 7d | 10080 | 0.369 | 0.359 | 0.280 | 0.311 | 0.529 | 0.266 | 0.472 | 1.218 |
| 30d | 43200 | 0.361 | 0.355 | 0.278 | 0.307 | 0.525 | 0.258 | 0.465 | 1.275 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.389 / 0.678 / 0.900; 2: 0.360 / 0.576 / 0.833; 3: 0.378 / 0.559 / 0.833; 4: 0.309 / 0.407 / 0.800; 5: 0.352 / 0.542 / 0.700; 6: 0.325 / 0.508 / 0.633; 7: 0.370 / 0.610 / 0.633; 8: 0.343 / 0.542 / 0.583; 9: 0.356 / 0.559 / 0.650; 10: 0.333 / 0.424 / 0.650; 11: 0.337 / 0.542 / 0.617; 12: 0.349 / 0.475 / 0.583; 13: 0.335 / 0.508 / 0.567; 14: 0.351 / 0.542 / 0.550; 15: 0.335 / 0.458 / 0.567
- 6h: 1: 0.374 / 0.551 / 0.875; 2: 0.345 / 0.458 / 0.886; 3: 0.375 / 0.548 / 0.881; 4: 0.339 / 0.449 / 0.892; 5: 0.365 / 0.559 / 0.847; 6: 0.351 / 0.489 / 0.836; 7: 0.354 / 0.503 / 0.842; 8: 0.360 / 0.525 / 0.833; 9: 0.349 / 0.489 / 0.856; 10: 0.348 / 0.452 / 0.861; 11: 0.349 / 0.480 / 0.831; 12: 0.358 / 0.483 / 0.839; 13: 0.358 / 0.514 / 0.836; 14: 0.360 / 0.517 / 0.825; 15: 0.346 / 0.444 / 0.822
- 24h: 1: 0.367 / 0.526 / 0.883; 2: 0.353 / 0.472 / 0.897; 3: 0.361 / 0.500 / 0.896; 4: 0.358 / 0.500 / 0.902; 5: 0.358 / 0.514 / 0.888; 6: 0.354 / 0.494 / 0.890; 7: 0.354 / 0.492 / 0.896; 8: 0.354 / 0.491 / 0.894; 9: 0.362 / 0.517 / 0.899; 10: 0.354 / 0.492 / 0.903; 11: 0.351 / 0.486 / 0.899; 12: 0.357 / 0.504 / 0.895; 13: 0.351 / 0.490 / 0.899; 14: 0.356 / 0.499 / 0.900; 15: 0.354 / 0.488 / 0.894
- 7d: 1: 0.369 / 0.529 / 0.896; 2: 0.357 / 0.497 / 0.900; 3: 0.358 / 0.510 / 0.899; 4: 0.354 / 0.498 / 0.899; 5: 0.355 / 0.506 / 0.899; 6: 0.353 / 0.498 / 0.898; 7: 0.353 / 0.498 / 0.898; 8: 0.354 / 0.507 / 0.898; 9: 0.353 / 0.499 / 0.898; 10: 0.352 / 0.505 / 0.898; 11: 0.350 / 0.498 / 0.897; 12: 0.352 / 0.501 / 0.897; 13: 0.349 / 0.494 / 0.898; 14: 0.350 / 0.494 / 0.898; 15: 0.350 / 0.502 / 0.897
- 30d: 1: 0.361 / 0.525 / 0.898; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.347 / 0.497 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.899; 14: 0.346 / 0.499 / 0.899; 15: 0.346 / 0.499 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.073 (body 0.049, range 0.098); 'price stays where it was' would score 0.085; colour right 0.492; typical miss of the close 15.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.134 (body 0.090, range 0.178); 'price stays where it was' would score 0.147; colour right 0.497; typical miss of the close 8.4 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.129 (body 0.084, range 0.174); 'price stays where it was' would score 0.138; colour right 0.482; typical miss of the close 9.3 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.129 (body 0.089, range 0.170); 'price stays where it was' would score 0.137; colour right 0.499; typical miss of the close 8.8 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.162); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.198 / 4.6; 3: 0.169 / 6.1; 4: 0.131 / 6.6; 5: 0.124 / 7.3; 6: 0.112 / 7.8; 7: 0.107 / 8.1; 8: 0.095 / 8.5; 9: 0.087 / 8.6; 10: 0.086 / 9.3; 11: 0.086 / 9.7; 12: 0.077 / 10.0; 13: 0.067 / 10.3; 14: 0.069 / 10.7; 15: 0.061 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 122810, probability skill vs chance 0.2444, widened contest next: True
  - now: threshold 0.8339, hit rate recent 0.964 / long run 0.9402
    - 6h: 18 calls (73 a day), hit rate 1.000, chance 0.292, naive rule 0.500, lift 3.43x
    - 24h: 69 calls (69 a day), hit rate 0.971, chance 0.297, naive rule 0.490, lift 3.27x
    - 7d: 394 calls (56 a day), hit rate 0.949, chance 0.299, naive rule 0.505, lift 3.17x
    - 30d: 1707 calls (57 a day), hit rate 0.937, chance 0.293, naive rule 0.491, lift 3.19x
  - next: threshold 0.5504, hit rate recent 0.55 / long run 0.5862
    - 6h: 34 calls (138 a day), hit rate 0.529, chance 0.292, lift 1.82x
    - 24h: 132 calls (132 a day), hit rate 0.561, chance 0.297, lift 1.89x
    - 7d: 680 calls (97 a day), hit rate 0.603, chance 0.299, lift 2.02x
    - 30d: 2883 calls (96 a day), hit rate 0.580, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 538, 0.519; 0.40: 477, 0.576; 0.45: 408, 0.647; 0.50: 357, 0.699; 0.55: 312, 0.741; 0.60: 264, 0.786; 0.65: 221, 0.812; 0.70: 175, 0.844; 0.75: 137, 0.875; 0.80: 92, 0.915; 0.85: 47, 0.952; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.465; 0.40: 407, 0.500; 0.45: 310, 0.533; 0.50: 200, 0.569; 0.55: 90, 0.572; 0.60: 14, 0.630; 0.65: 1, 0.677
- **K=5**: model 1792540800, labels learned 122808, probability skill vs chance 0.2259, widened contest next: False
  - now: threshold 0.6713, hit rate recent 0.8299 / long run 0.8231
    - 6h: 20 calls (82 a day), hit rate 0.900, chance 0.200, naive rule 0.449, lift 4.51x
    - 24h: 65 calls (65 a day), hit rate 0.800, chance 0.196, naive rule 0.420, lift 4.09x
    - 7d: 368 calls (53 a day), hit rate 0.823, chance 0.186, naive rule 0.410, lift 4.42x
    - 30d: 1583 calls (53 a day), hit rate 0.828, chance 0.188, naive rule 0.401, lift 4.41x
  - next: threshold 0.4539, hit rate recent 0.522 / long run 0.4848
    - 6h: 17 calls (69 a day), hit rate 0.529, chance 0.200, lift 2.65x
    - 24h: 89 calls (89 a day), hit rate 0.517, chance 0.196, lift 2.64x
    - 7d: 862 calls (123 a day), hit rate 0.490, chance 0.186, lift 2.63x
    - 30d: 3048 calls (102 a day), hit rate 0.465, chance 0.188, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 345, 0.493; 0.40: 278, 0.565; 0.45: 225, 0.620; 0.50: 178, 0.668; 0.55: 138, 0.710; 0.60: 106, 0.753; 0.65: 76, 0.790; 0.70: 52, 0.830; 0.75: 30, 0.873; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.391; 0.35: 253, 0.422; 0.40: 159, 0.454; 0.45: 70, 0.467; 0.50: 15, 0.487; 0.55: 1, 0.540
- **K=8**: model 1793059200, labels learned 122805, probability skill vs chance 0.1998, widened contest next: False
  - now: threshold 0.5551, hit rate recent 0.6858 / long run 0.6789
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.139, naive rule 0.417, lift 7.22x
    - 24h: 62 calls (62 a day), hit rate 0.629, chance 0.121, naive rule 0.342, lift 5.20x
    - 7d: 348 calls (50 a day), hit rate 0.672, chance 0.117, naive rule 0.327, lift 5.76x
    - 30d: 1531 calls (51 a day), hit rate 0.690, chance 0.121, naive rule 0.331, lift 5.70x
  - next: threshold 0.3355, hit rate recent 0.3666 / long run 0.377
    - 6h: 27 calls (111 a day), hit rate 0.407, chance 0.139, lift 2.94x
    - 24h: 107 calls (108 a day), hit rate 0.346, chance 0.121, lift 2.86x
    - 7d: 743 calls (106 a day), hit rate 0.385, chance 0.117, lift 3.30x
    - 30d: 2672 calls (89 a day), hit rate 0.381, chance 0.121, lift 3.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.428; 0.35: 189, 0.496; 0.40: 146, 0.547; 0.45: 111, 0.592; 0.50: 84, 0.635; 0.55: 61, 0.672; 0.60: 40, 0.716; 0.65: 23, 0.788; 0.70: 10, 0.831; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.355; 0.35: 95, 0.381; 0.40: 34, 0.403; 0.45: 7, 0.422; 0.50: 1, 0.600
- **K=13**: model 1793059200, labels learned 122800, probability skill vs chance 0.1865, widened contest next: False
  - now: threshold 0.4099, hit rate recent 0.5486 / long run 0.5543
    - 6h: 11 calls (46 a day), hit rate 0.818, chance 0.074, naive rule 0.319, lift 11.07x
    - 24h: 62 calls (63 a day), hit rate 0.500, chance 0.072, naive rule 0.266, lift 6.99x
    - 7d: 363 calls (52 a day), hit rate 0.559, chance 0.074, naive rule 0.270, lift 7.60x
    - 30d: 1600 calls (53 a day), hit rate 0.561, chance 0.077, naive rule 0.273, lift 7.28x
  - next: threshold 0.2948, hit rate recent 0.3176 / long run 0.3125
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.074, lift 6.15x
    - 24h: 54 calls (55 a day), hit rate 0.315, chance 0.072, lift 4.40x
    - 7d: 431 calls (62 a day), hit rate 0.311, chance 0.074, lift 4.22x
    - 30d: 2170 calls (72 a day), hit rate 0.305, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.439; 0.35: 89, 0.489; 0.40: 62, 0.546; 0.45: 41, 0.598; 0.50: 26, 0.656; 0.55: 16, 0.708; 0.60: 7, 0.750; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.316; 0.35: 14, 0.351; 0.40: 2, 0.449; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 17.760 | 0.80% | 0.900 | 0.567 | 0.251 | 0.492 | 0.473 |
| 6h | 13.756 | 0.70% | 0.883 | 0.514 | 0.250 | 0.508 | 0.440 |
| 24h | 15.571 | 2.73% | 0.896 | 0.501 | 0.251 | 0.497 | 0.643 |
| 7d | 15.163 | 3.63% | 0.899 | 0.502 | 0.250 | 0.500 | 0.664 |
| 30d | 13.782 | 4.13% | 0.900 | 0.500 | 0.251 | 0.496 | 0.667 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.904 | 17.950 | 17.965 | 17.621 | 18.400 | 17.983 | 17.697 | 17.742 | 17.728 | 17.760 |
| 6h | 13.853 | 13.833 | 13.830 | 13.772 | 13.968 | 13.860 | 13.731 | 13.681 | 13.723 | 13.756 |
| 24h | 16.007 | 15.657 | 15.616 | 15.627 | 15.742 | 15.643 | 15.574 | 15.509 | 15.533 | 15.571 |
| 7d | 15.735 | 15.306 | 15.244 | 15.184 | 15.426 | 15.318 | 15.151 | 15.121 | 15.132 | 15.163 |
| 30d | 14.375 | 13.914 | 13.867 | 13.807 | 14.027 | 13.962 | 13.776 | 13.757 | 13.756 | 13.782 |

## Next candle

- candle starting 2026-10-27 10:56 UTC, last close 2311.41
- P(up) 0.4836, return quantiles (bp): {'05': -10.094, '10': -8.226, '25': -4.128, '40': -1.751, '50': -0.225, '60': 1.172, '75': 3.518, '90': 7.92, '95': 10.661}
- changepoint probability 0.3653, regime age 15.1 min
- agent weights: empirical 0.022, ewma 0.101, garch 0.112, har 0.140, bocpd 0.033, hmm 0.086, online_qr 0.208, lgbm 0.298

## Learning log

- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- HMM volatility states (sd, bp per minute): [3.4, 6.54, 17.69], current probabilities: [0.301, 0.691, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-10-27 11:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.336, 'l_abs': 0.75, 'l_hi': 0.778, 'l_lo': 0.786, 'b05': 0.759, 'b25': 0.803, 'b75': 0.64, 'b95': 0.749}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.532, 1.918, 2.09, 2.86, 3.267, 3.397, 3.788, 3.642, 3.696, 4.558, 4.676, 4.877, 5.173, 5.585]}
- calibration offsets (in sigma): {'05': -0.0025, '10': -0.085, '25': -0.0325, '40': -0.02, '50': -0.005, '60': -0.0, '75': -0.0375, '90': 0.035, '95': 0.0425}
