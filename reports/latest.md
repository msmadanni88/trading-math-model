# ETH-USD 60s candle generator - report

- generated: 2026-10-27 05:33 UTC
- last closed candle: 2026-10-27 05:29 UTC (staleness 5.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.530 (672) [0.494, 0.569] | 0.522 (2876) [0.503, 0.542] | 0.516 (5274) [0.503, 0.530] | 0.523 (2302) [0.499, 0.546] | 0.524 (21) | 0.500 | flat -0.009 (noise 0.032) |
| colour_clear | 0.538 (824) | 0.548 (5704) [0.540, 0.558] | 0.536 (23552) [0.528, 0.543] | 0.518 (43117) [0.512, 0.524] | 0.546 (18879) [0.541, 0.550] | 0.562 (203) | 0.500 | flat -0.001 (noise 0.009) |
| colour_confident | 0.613 (160) | 0.601 (1419) [0.588, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.667 (30) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.522 (1432) | 0.531 (10039) [0.525, 0.537] | 0.524 (42872) [0.520, 0.529] | 0.513 (78622) [0.509, 0.517] | 0.529 (34273) [0.525, 0.533] | 0.532 (325) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.499 (20048) | 0.500 (140546) [0.498, 0.503] | 0.501 (600208) [0.499, 0.502] | 0.501 (1100708) [0.500, 0.502] | 0.500 (479822) [0.499, 0.502] | 0.498 (4550) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.604 (53) | 0.626 (420) [0.602, 0.667] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.500 (6) | 0.500 | flat +0.015 (noise 0.045) |
| reversal_k13_next | 0.271 (59) | 0.312 (442) [0.287, 0.336] | 0.304 (2171) [0.292, 0.316] | 0.307 (3743) [0.297, 0.318] | 0.316 (1638) [0.305, 0.327] | 0.333 (9) | 0.076 | flat +0.012 (noise 0.031) |
| reversal_k13_now | 0.457 (70) | 0.546 (370) [0.500, 0.594] | 0.561 (1601) [0.541, 0.583] | 0.571 (2776) [0.555, 0.587] | 0.560 (1304) [0.537, 0.585] | 0.500 (10) | 0.076 | flat +0.011 (noise 0.036) |
| reversal_k3_next | 0.590 (117) | 0.600 (678) [0.572, 0.628] | 0.582 (2864) [0.570, 0.595] | 0.584 (4759) [0.574, 0.595] | 0.580 (2319) [0.567, 0.595] | 0.613 (31) | 0.293 | flat +0.039 (noise 0.026) |
| reversal_k3_now | 0.983 (57) | 0.946 (389) [0.921, 0.968] | 0.936 (1694) [0.927, 0.946] | 0.938 (3126) [0.931, 0.945] | 0.933 (1363) [0.922, 0.944] | 0.941 (17) | 0.293 | flat +0.008 (noise 0.021) |
| reversal_k5_next | 0.509 (110) | 0.479 (893) [0.448, 0.502] | 0.465 (3032) [0.451, 0.478] | 0.477 (4553) [0.465, 0.490] | 0.464 (2563) [0.449, 0.480] | 0.692 (13) | 0.187 | flat +0.027 (noise 0.024) |
| reversal_k5_now | 0.833 (54) | 0.820 (361) [0.808, 0.831] | 0.829 (1568) [0.816, 0.842] | 0.830 (2874) [0.819, 0.840] | 0.820 (1263) [0.807, 0.833] | 0.750 (12) | 0.187 | flat +0.002 (noise 0.029) |
| reversal_k8_next | 0.336 (110) | 0.379 (755) [0.359, 0.396] | 0.380 (2651) [0.368, 0.392] | 0.388 (4416) [0.377, 0.399] | 0.380 (2310) [0.367, 0.394] | 0.444 (18) | 0.120 | flat +0.014 (noise 0.025) |
| reversal_k8_now | 0.545 (55) | 0.658 (342) [0.608, 0.707] | 0.689 (1530) [0.667, 0.710] | 0.699 (2842) [0.683, 0.715] | 0.680 (1255) [0.657, 0.705] | 0.615 (13) | 0.121 | flat -0.014 (noise 0.036) |
| overall | 0.501 (22208) | 0.504 (155487) [0.501, 0.507] | 0.504 (663067) [0.503, 0.505] | 0.503 (1213693) [0.502, 0.504] | 0.504 (530412) [0.502, 0.506] | 0.504 (5019) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07923, 0.1183] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5303, 'levels': [{'threshold': 0.07923, 'calls_per_day': 146.4, 'win_rate': 0.6064}, {'threshold': 0.1183, 'calls_per_day': 37.0, 'win_rate': 0.6346}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 33459, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14990 | 0.336 | 0.523 (14745) | 0.589 (1736) | 0.765 (2498) |
| volatility: normal | 14990 | 0.365 | 0.526 (14916) | 0.608 (1280) | 0.748 (2221) |
| volatility: wild | 14989 | 0.379 | 0.522 (14945) | 0.635 (635) | 0.764 (1917) |
| session: Asia 00-08 | 15209 | 0.359 | 0.530 (15100) | 0.609 (1302) | 0.761 (2204) |
| session: Europe 08-13 | 9300 | 0.355 | 0.528 (9212) | 0.599 (893) | 0.757 (1482) |
| session: US 13-21 | 14880 | 0.367 | 0.519 (14776) | 0.596 (921) | 0.767 (2119) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.609 (535) | 0.737 (831) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.355 | 0.328 | 0.270 | 0.270 | 0.525 | 0.233 | 0.478 | 1.290 |
| 6h | 360 | 0.362 | 0.358 | 0.276 | 0.318 | 0.513 | 0.250 | 0.475 | 1.190 |
| 24h | 1440 | 0.369 | 0.360 | 0.295 | 0.328 | 0.523 | 0.257 | 0.481 | 1.191 |
| 7d | 10080 | 0.369 | 0.359 | 0.278 | 0.310 | 0.529 | 0.266 | 0.471 | 1.211 |
| 30d | 43200 | 0.361 | 0.355 | 0.278 | 0.306 | 0.525 | 0.258 | 0.465 | 1.272 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.355 / 0.525 / 0.917; 2: 0.319 / 0.373 / 0.850; 3: 0.361 / 0.542 / 0.900; 4: 0.346 / 0.475 / 0.800; 5: 0.364 / 0.559 / 0.867; 6: 0.343 / 0.559 / 0.867; 7: 0.328 / 0.475 / 0.917; 8: 0.367 / 0.576 / 0.917; 9: 0.350 / 0.508 / 0.883; 10: 0.336 / 0.492 / 0.917; 11: 0.348 / 0.492 / 0.950; 12: 0.349 / 0.525 / 0.967; 13: 0.336 / 0.475 / 0.983; 14: 0.337 / 0.475 / 1.000; 15: 0.364 / 0.475 / 1.000
- 6h: 1: 0.362 / 0.513 / 0.903; 2: 0.361 / 0.487 / 0.903; 3: 0.356 / 0.473 / 0.914; 4: 0.361 / 0.501 / 0.889; 5: 0.349 / 0.479 / 0.917; 6: 0.361 / 0.538 / 0.917; 7: 0.351 / 0.493 / 0.931; 8: 0.352 / 0.485 / 0.936; 9: 0.359 / 0.518 / 0.928; 10: 0.358 / 0.532 / 0.944; 11: 0.356 / 0.515 / 0.950; 12: 0.348 / 0.470 / 0.953; 13: 0.356 / 0.504 / 0.958; 14: 0.353 / 0.468 / 0.958; 15: 0.349 / 0.482 / 0.953
- 24h: 1: 0.369 / 0.523 / 0.893; 2: 0.357 / 0.471 / 0.894; 3: 0.360 / 0.500 / 0.895; 4: 0.360 / 0.499 / 0.892; 5: 0.360 / 0.512 / 0.899; 6: 0.355 / 0.497 / 0.899; 7: 0.355 / 0.496 / 0.899; 8: 0.352 / 0.476 / 0.898; 9: 0.364 / 0.522 / 0.895; 10: 0.356 / 0.506 / 0.894; 11: 0.353 / 0.491 / 0.899; 12: 0.356 / 0.508 / 0.898; 13: 0.348 / 0.477 / 0.897; 14: 0.355 / 0.497 / 0.901; 15: 0.356 / 0.500 / 0.901
- 7d: 1: 0.369 / 0.529 / 0.896; 2: 0.357 / 0.499 / 0.899; 3: 0.357 / 0.509 / 0.899; 4: 0.355 / 0.499 / 0.899; 5: 0.354 / 0.503 / 0.900; 6: 0.352 / 0.497 / 0.900; 7: 0.352 / 0.498 / 0.900; 8: 0.354 / 0.507 / 0.900; 9: 0.353 / 0.500 / 0.899; 10: 0.352 / 0.505 / 0.899; 11: 0.350 / 0.499 / 0.900; 12: 0.351 / 0.502 / 0.900; 13: 0.349 / 0.494 / 0.900; 14: 0.349 / 0.494 / 0.900; 15: 0.350 / 0.502 / 0.900
- 30d: 1: 0.361 / 0.525 / 0.898; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.501 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.499 / 0.900; 15: 0.346 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.094 (body 0.048, range 0.139); 'price stays where it was' would score 0.094; colour right 0.458; typical miss of the close 8.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.130 (body 0.081, range 0.180); 'price stays where it was' would score 0.135; colour right 0.456; typical miss of the close 8.2 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.130 (body 0.085, range 0.175); 'price stays where it was' would score 0.139; colour right 0.473; typical miss of the close 9.4 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.135; colour right 0.498; typical miss of the close 8.8 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.162); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.0; 2: 0.197 / 4.6; 3: 0.169 / 6.0; 4: 0.131 / 6.6; 5: 0.124 / 7.3; 6: 0.112 / 7.7; 7: 0.107 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.087 / 9.2; 11: 0.085 / 9.7; 12: 0.076 / 10.0; 13: 0.067 / 10.3; 14: 0.069 / 10.6; 15: 0.060 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 122483, probability skill vs chance 0.2357, widened contest next: False
  - now: threshold 0.8339, hit rate recent 0.9522 / long run 0.9385
    - 6h: 17 calls (70 a day), hit rate 0.941, chance 0.325, naive rule 0.509, lift 2.90x
    - 24h: 64 calls (64 a day), hit rate 0.969, chance 0.302, naive rule 0.497, lift 3.21x
    - 7d: 389 calls (56 a day), hit rate 0.949, chance 0.299, naive rule 0.504, lift 3.17x
    - 30d: 1703 calls (57 a day), hit rate 0.937, chance 0.294, naive rule 0.492, lift 3.19x
  - next: threshold 0.5304, hit rate recent 0.5978 / long run 0.5914
    - 6h: 32 calls (131 a day), hit rate 0.625, chance 0.325, lift 1.92x
    - 24h: 123 calls (124 a day), hit rate 0.585, chance 0.302, lift 1.94x
    - 7d: 681 calls (97 a day), hit rate 0.605, chance 0.299, lift 2.02x
    - 30d: 2873 calls (96 a day), hit rate 0.582, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 538, 0.519; 0.40: 478, 0.575; 0.45: 408, 0.646; 0.50: 357, 0.698; 0.55: 312, 0.741; 0.60: 264, 0.785; 0.65: 221, 0.812; 0.70: 175, 0.844; 0.75: 136, 0.875; 0.80: 91, 0.914; 0.85: 47, 0.951; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.427; 0.35: 502, 0.465; 0.40: 408, 0.500; 0.45: 310, 0.534; 0.50: 200, 0.570; 0.55: 90, 0.573; 0.60: 14, 0.632; 0.65: 1, 0.677
- **K=5**: model 1792540800, labels learned 122481, probability skill vs chance 0.2164, widened contest next: False
  - now: threshold 0.6716, hit rate recent 0.8051 / long run 0.8205
    - 6h: 12 calls (50 a day), hit rate 0.750, chance 0.209, naive rule 0.447, lift 3.59x
    - 24h: 54 calls (54 a day), hit rate 0.778, chance 0.196, naive rule 0.415, lift 3.97x
    - 7d: 358 calls (51 a day), hit rate 0.818, chance 0.186, naive rule 0.408, lift 4.40x
    - 30d: 1574 calls (52 a day), hit rate 0.828, chance 0.188, naive rule 0.401, lift 4.41x
  - next: threshold 0.449, hit rate recent 0.5376 / long run 0.4852
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.209, lift 3.41x
    - 24h: 94 calls (95 a day), hit rate 0.553, chance 0.196, lift 2.82x
    - 7d: 878 calls (126 a day), hit rate 0.485, chance 0.186, lift 2.61x
    - 30d: 3037 calls (101 a day), hit rate 0.465, chance 0.188, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 344, 0.492; 0.40: 278, 0.565; 0.45: 225, 0.619; 0.50: 177, 0.669; 0.55: 137, 0.710; 0.60: 106, 0.753; 0.65: 76, 0.790; 0.70: 52, 0.830; 0.75: 30, 0.874; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.390; 0.35: 252, 0.422; 0.40: 158, 0.454; 0.45: 70, 0.467; 0.50: 15, 0.487; 0.55: 1, 0.528
- **K=8**: model 1793059200, labels learned 122478, probability skill vs chance 0.1925, widened contest next: True
  - now: threshold 0.5555, hit rate recent 0.6091 / long run 0.6719
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.132, naive rule 0.383, lift 4.68x
    - 24h: 56 calls (57 a day), hit rate 0.518, chance 0.115, naive rule 0.322, lift 4.49x
    - 7d: 343 calls (49 a day), hit rate 0.656, chance 0.116, naive rule 0.325, lift 5.64x
    - 30d: 1533 calls (51 a day), hit rate 0.688, chance 0.121, naive rule 0.330, lift 5.69x
  - next: threshold 0.3357, hit rate recent 0.368 / long run 0.3771
    - 6h: 19 calls (79 a day), hit rate 0.421, chance 0.132, lift 3.20x
    - 24h: 107 calls (108 a day), hit rate 0.336, chance 0.115, lift 2.92x
    - 7d: 747 calls (107 a day), hit rate 0.384, chance 0.116, lift 3.31x
    - 30d: 2656 calls (89 a day), hit rate 0.380, chance 0.121, lift 3.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 189, 0.496; 0.40: 145, 0.547; 0.45: 111, 0.592; 0.50: 84, 0.634; 0.55: 61, 0.670; 0.60: 40, 0.716; 0.65: 23, 0.789; 0.70: 10, 0.833; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.355; 0.35: 96, 0.381; 0.40: 34, 0.400; 0.45: 7, 0.421; 0.50: 1, 0.600
- **K=13**: model 1793059200, labels learned 122473, probability skill vs chance 0.1766, widened contest next: True
  - now: threshold 0.4161, hit rate recent 0.4949 / long run 0.5494
    - 6h: 10 calls (42 a day), hit rate 0.500, chance 0.087, naive rule 0.308, lift 5.78x
    - 24h: 63 calls (64 a day), hit rate 0.413, chance 0.071, naive rule 0.249, lift 5.84x
    - 7d: 366 calls (52 a day), hit rate 0.544, chance 0.073, naive rule 0.267, lift 7.41x
    - 30d: 1602 calls (53 a day), hit rate 0.560, chance 0.077, naive rule 0.273, lift 7.27x
  - next: threshold 0.2947, hit rate recent 0.2929 / long run 0.3099
    - 6h: 10 calls (42 a day), hit rate 0.300, chance 0.087, lift 3.47x
    - 24h: 56 calls (57 a day), hit rate 0.268, chance 0.071, lift 3.79x
    - 7d: 435 calls (62 a day), hit rate 0.310, chance 0.073, lift 4.23x
    - 30d: 2169 calls (72 a day), hit rate 0.303, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.440; 0.35: 89, 0.491; 0.40: 62, 0.546; 0.45: 41, 0.598; 0.50: 26, 0.656; 0.55: 16, 0.708; 0.60: 7, 0.750; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.315; 0.35: 14, 0.349; 0.40: 2, 0.457; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.184 | 2.90% | 0.933 | 0.500 | 0.252 | 0.390 | -0.028 |
| 6h | 12.951 | 2.58% | 0.908 | 0.511 | 0.250 | 0.490 | 0.344 |
| 24h | 15.810 | 3.02% | 0.905 | 0.502 | 0.251 | 0.490 | 0.635 |
| 7d | 15.178 | 3.62% | 0.899 | 0.500 | 0.250 | 0.500 | 0.665 |
| 30d | 13.743 | 4.14% | 0.900 | 0.500 | 0.251 | 0.496 | 0.668 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.519 | 11.129 | 11.210 | 11.146 | 11.174 | 11.295 | 11.237 | 11.098 | 11.153 | 11.184 |
| 6h | 13.294 | 12.970 | 12.962 | 12.982 | 13.087 | 13.003 | 12.956 | 12.900 | 12.921 | 12.951 |
| 24h | 16.302 | 15.918 | 15.848 | 15.860 | 16.003 | 15.882 | 15.804 | 15.759 | 15.768 | 15.810 |
| 7d | 15.748 | 15.318 | 15.256 | 15.200 | 15.436 | 15.331 | 15.167 | 15.137 | 15.147 | 15.178 |
| 30d | 14.338 | 13.876 | 13.828 | 13.768 | 13.988 | 13.922 | 13.738 | 13.719 | 13.718 | 13.743 |

## Next candle

- candle starting 2026-10-27 05:29 UTC, last close 2306.46
- P(up) 0.5083, return quantiles (bp): {'05': -8.115, '10': -6.118, '25': -3.215, '40': -0.943, '50': 0.083, '60': 1.337, '75': 3.14, '90': 5.967, '95': 7.546}
- changepoint probability 0.049, regime age 129.8 min
- agent weights: empirical 0.007, ewma 0.114, garch 0.136, har 0.127, bocpd 0.051, hmm 0.102, online_qr 0.183, lgbm 0.281

## Learning log

- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- HMM volatility states (sd, bp per minute): [3.4, 6.54, 17.69], current probabilities: [0.658, 0.326, 0.016]
- live generator: {'versions': 60, 'latest_effective': '2026-10-27 05:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.276, 'l_abs': 0.738, 'l_hi': 0.806, 'l_lo': 0.795, 'b05': 0.772, 'b25': 0.772, 'b75': 0.668, 'b95': 0.739}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.463, 1.725, 2.162, 2.106, 2.177, 2.264, 2.377, 2.736, 2.833, 2.748, 2.934, 2.94, 2.822, 2.986]}
- calibration offsets (in sigma): {'05': -0.036, '10': -0.062, '25': -0.07, '40': 0.022, '50': 0.0, '60': 0.018, '75': -0.0, '90': 0.012, '95': -0.064}
