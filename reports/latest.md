# ETH-USD 60s candle generator - report

- generated: 2026-11-27 20:15 UTC
- last closed candle: 2026-11-27 20:15 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.526 (95) | 0.504 (671) [0.475, 0.534] | 0.510 (2878) [0.495, 0.524] | 0.514 (8248) [0.505, 0.525] | 0.516 (5276) [0.502, 0.529] | 0.469 (81) | 0.500 | flat -0.022 (noise 0.027) |
| colour_clear | 0.596 (796) | 0.559 (5474) [0.547, 0.573] | 0.544 (23744) [0.537, 0.551] | 0.528 (67701) [0.522, 0.533] | 0.545 (43463) [0.541, 0.549] | 0.572 (652) | 0.500 | flat +0.013 (noise 0.010) |
| colour_confident | 0.550 (191) | 0.571 (1352) [0.556, 0.584] | 0.567 (4480) [0.557, 0.577] | 0.583 (8262) [0.574, 0.592] | 0.583 (8262) [0.574, 0.592] | 0.518 (135) | 0.500 | flat +0.015 (noise 0.020) |
| colour_next | 0.563 (1431) | 0.539 (10043) [0.531, 0.548] | 0.532 (42905) [0.528, 0.537] | 0.520 (122957) [0.517, 0.524] | 0.531 (78608) [0.528, 0.534] | 0.545 (1212) | 0.500 | flat +0.006 (noise 0.007) |
| colour_path | 0.492 (20034) | 0.501 (140602) [0.498, 0.504] | 0.502 (600670) [0.501, 0.503] | 0.501 (1721398) [0.500, 0.502] | 0.501 (1100512) [0.500, 0.502] | 0.505 (16968) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.463 (54) | 0.553 (407) [0.502, 0.596] | 0.592 (1179) [0.567, 0.614] | 0.612 (2220) [0.594, 0.628] | 0.612 (2220) [0.594, 0.628] | 0.475 (40) | 0.500 | flat -0.053 (noise 0.038) |
| reversal_k13_next | 0.292 (48) | 0.369 (371) [0.327, 0.414] | 0.335 (1824) [0.318, 0.353] | 0.317 (5618) [0.308, 0.327] | 0.328 (3513) [0.317, 0.340] | 0.244 (45) | 0.078 | up +0.070 (noise 0.033) |
| reversal_k13_now | 0.569 (51) | 0.624 (343) [0.576, 0.672] | 0.583 (1595) [0.563, 0.605] | 0.576 (4427) [0.564, 0.589] | 0.574 (2955) [0.558, 0.590] | 0.500 (48) | 0.078 | flat +0.064 (noise 0.043) |
| reversal_k3_next | 0.611 (126) | 0.598 (1046) [0.573, 0.622] | 0.601 (2732) [0.588, 0.615] | 0.590 (7614) [0.582, 0.598] | 0.591 (5174) [0.581, 0.601] | 0.670 (88) | 0.294 | flat +0.003 (noise 0.029) |
| reversal_k3_now | 0.962 (52) | 0.932 (411) [0.920, 0.945] | 0.928 (1741) [0.920, 0.936] | 0.935 (4932) [0.930, 0.940] | 0.931 (3169) [0.925, 0.938] | 0.936 (47) | 0.294 | flat -0.009 (noise 0.017) |
| reversal_k5_next | 0.507 (69) | 0.524 (374) [0.479, 0.579] | 0.510 (1711) [0.490, 0.531] | 0.486 (6330) [0.475, 0.498] | 0.483 (4340) [0.469, 0.497] | 0.425 (47) | 0.187 | flat +0.049 (noise 0.045) |
| reversal_k5_now | 0.892 (65) | 0.825 (440) [0.799, 0.851] | 0.796 (1811) [0.779, 0.812] | 0.817 (4743) [0.808, 0.827] | 0.807 (3132) [0.795, 0.818] | 0.833 (42) | 0.188 | flat +0.050 (noise 0.027) |
| reversal_k8_next | 0.431 (72) | 0.423 (546) [0.376, 0.471] | 0.421 (2178) [0.405, 0.440] | 0.399 (6695) [0.389, 0.409] | 0.400 (4589) [0.389, 0.412] | 0.351 (57) | 0.121 | flat +0.028 (noise 0.037) |
| reversal_k8_now | 0.729 (59) | 0.694 (409) [0.662, 0.724] | 0.687 (1670) [0.670, 0.704] | 0.695 (4568) [0.683, 0.707] | 0.685 (2981) [0.671, 0.699] | 0.592 (49) | 0.122 | flat +0.036 (noise 0.033) |
| overall | 0.500 (22102) | 0.506 (155256) [0.504, 0.509] | 0.506 (661715) [0.505, 0.507] | 0.504 (1897530) [0.504, 0.505] | 0.505 (1214249) [0.504, 0.506] | 0.509 (18684) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08589, 0.1239] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5401, 'levels': [{'threshold': 0.08589, 'calls_per_day': 148.7, 'win_rate': 0.5656}, {'threshold': 0.1239, 'calls_per_day': 37.7, 'win_rate': 0.5509}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42910, 'rate': 0.5332}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15285 | 0.355 | 0.536 (15067) | 0.555 (2001) | 0.754 (2625) |
| volatility: normal | 15285 | 0.381 | 0.528 (15229) | 0.563 (1564) | 0.751 (2438) |
| volatility: wild | 15285 | 0.392 | 0.534 (15251) | 0.592 (1211) | 0.757 (2175) |
| session: Asia 00-08 | 15360 | 0.374 | 0.534 (15253) | 0.559 (1664) | 0.748 (2329) |
| session: Europe 08-13 | 9600 | 0.370 | 0.531 (9523) | 0.575 (1159) | 0.773 (1529) |
| session: US 13-21 | 15315 | 0.383 | 0.536 (15225) | 0.593 (1366) | 0.743 (2498) |
| session: late 21-24 | 5580 | 0.370 | 0.522 (5546) | 0.511 (587) | 0.766 (882) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.390 | 0.367 | 0.296 | 0.296 | 0.533 | 0.260 | 0.520 | 1.943 |
| 6h | 360 | 0.393 | 0.376 | 0.303 | 0.338 | 0.540 | 0.281 | 0.504 | 1.505 |
| 24h | 1440 | 0.387 | 0.372 | 0.285 | 0.321 | 0.542 | 0.280 | 0.494 | 1.181 |
| 7d | 10080 | 0.386 | 0.376 | 0.291 | 0.323 | 0.539 | 0.271 | 0.500 | 1.219 |
| 30d | 43200 | 0.376 | 0.369 | 0.288 | 0.320 | 0.533 | 0.267 | 0.485 | 1.267 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.390 / 0.533 / 0.900; 2: 0.345 / 0.467 / 0.850; 3: 0.390 / 0.533 / 0.800; 4: 0.384 / 0.533 / 0.900; 5: 0.372 / 0.483 / 0.783; 6: 0.370 / 0.517 / 0.800; 7: 0.391 / 0.567 / 0.767; 8: 0.367 / 0.433 / 0.750; 9: 0.372 / 0.500 / 0.767; 10: 0.372 / 0.550 / 0.767; 11: 0.353 / 0.400 / 0.783; 12: 0.388 / 0.600 / 0.783; 13: 0.375 / 0.517 / 0.800; 14: 0.377 / 0.500 / 0.750; 15: 0.350 / 0.467 / 0.717
- 6h: 1: 0.393 / 0.540 / 0.889; 2: 0.372 / 0.499 / 0.872; 3: 0.371 / 0.515 / 0.792; 4: 0.380 / 0.513 / 0.867; 5: 0.380 / 0.526 / 0.806; 6: 0.360 / 0.474 / 0.797; 7: 0.370 / 0.513 / 0.753; 8: 0.364 / 0.499 / 0.744; 9: 0.364 / 0.499 / 0.731; 10: 0.363 / 0.501 / 0.750; 11: 0.359 / 0.468 / 0.744; 12: 0.365 / 0.515 / 0.728; 13: 0.369 / 0.543 / 0.744; 14: 0.350 / 0.485 / 0.689; 15: 0.354 / 0.485 / 0.706
- 24h: 1: 0.387 / 0.542 / 0.899; 2: 0.367 / 0.497 / 0.895; 3: 0.366 / 0.508 / 0.871; 4: 0.369 / 0.508 / 0.883; 5: 0.361 / 0.487 / 0.872; 6: 0.358 / 0.492 / 0.869; 7: 0.367 / 0.529 / 0.857; 8: 0.363 / 0.508 / 0.864; 9: 0.357 / 0.495 / 0.854; 10: 0.359 / 0.496 / 0.865; 11: 0.355 / 0.489 / 0.865; 12: 0.360 / 0.508 / 0.867; 13: 0.363 / 0.520 / 0.871; 14: 0.358 / 0.503 / 0.856; 15: 0.364 / 0.520 / 0.856
- 7d: 1: 0.386 / 0.539 / 0.901; 2: 0.367 / 0.486 / 0.901; 3: 0.370 / 0.506 / 0.901; 4: 0.367 / 0.498 / 0.900; 5: 0.367 / 0.498 / 0.898; 6: 0.364 / 0.494 / 0.897; 7: 0.367 / 0.508 / 0.897; 8: 0.366 / 0.507 / 0.898; 9: 0.363 / 0.494 / 0.896; 10: 0.365 / 0.509 / 0.897; 11: 0.364 / 0.501 / 0.896; 12: 0.365 / 0.505 / 0.895; 13: 0.360 / 0.492 / 0.896; 14: 0.361 / 0.498 / 0.894; 15: 0.362 / 0.505 / 0.895
- 30d: 1: 0.376 / 0.533 / 0.898; 2: 0.362 / 0.491 / 0.900; 3: 0.366 / 0.511 / 0.899; 4: 0.362 / 0.497 / 0.900; 5: 0.363 / 0.505 / 0.899; 6: 0.360 / 0.500 / 0.899; 7: 0.362 / 0.503 / 0.899; 8: 0.361 / 0.507 / 0.899; 9: 0.360 / 0.500 / 0.899; 10: 0.360 / 0.504 / 0.899; 11: 0.360 / 0.505 / 0.899; 12: 0.360 / 0.503 / 0.899; 13: 0.359 / 0.499 / 0.899; 14: 0.359 / 0.501 / 0.899; 15: 0.358 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.059 (body 0.024, range 0.095); 'price stays where it was' would score 0.057; colour right 0.550; typical miss of the close 9.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.145 (body 0.100, range 0.190); 'price stays where it was' would score 0.160; colour right 0.526; typical miss of the close 13.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.140 (body 0.094, range 0.186); 'price stays where it was' would score 0.154; colour right 0.506; typical miss of the close 10.6 bp; chain ended on the right side 0.484 of 95 chains; n=1440
- 7d: match 0.136 (body 0.089, range 0.184); 'price stays where it was' would score 0.145; colour right 0.497; typical miss of the close 12.6 bp; chain ended on the right side 0.490 of 671 chains; n=10080
- 30d: match 0.128 (body 0.085, range 0.171); 'price stays where it was' would score 0.132; colour right 0.503; typical miss of the close 11.1 bp; chain ended on the right side 0.506 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.372 / 6.0; 2: 0.206 / 6.8; 3: 0.168 / 8.8; 4: 0.136 / 9.2; 5: 0.124 / 9.9; 6: 0.120 / 10.8; 7: 0.118 / 11.1; 8: 0.104 / 12.2; 9: 0.093 / 13.1; 10: 0.089 / 13.3; 11: 0.086 / 13.9; 12: 0.082 / 14.1; 13: 0.077 / 15.0; 14: 0.070 / 15.3; 15: 0.067 / 15.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 168009, probability skill vs chance 0.2325, widened contest next: False
  - now: threshold 0.8295, hit rate recent 0.9364 / long run 0.9314
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.289, naive rule 0.502, lift 3.15x
    - 24h: 60 calls (60 a day), hit rate 0.950, chance 0.311, naive rule 0.518, lift 3.05x
    - 7d: 403 calls (58 a day), hit rate 0.933, chance 0.306, naive rule 0.530, lift 3.05x
    - 30d: 1733 calls (58 a day), hit rate 0.930, chance 0.296, naive rule 0.507, lift 3.15x
  - next: threshold 0.541, hit rate recent 0.6403 / long run 0.6071
    - 6h: 29 calls (118 a day), hit rate 0.586, chance 0.289, lift 2.03x
    - 24h: 103 calls (103 a day), hit rate 0.641, chance 0.311, lift 2.06x
    - 7d: 998 calls (143 a day), hit rate 0.609, chance 0.306, lift 1.99x
    - 30d: 2725 calls (91 a day), hit rate 0.603, chance 0.296, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.505; 0.35: 530, 0.530; 0.40: 483, 0.572; 0.45: 421, 0.634; 0.50: 370, 0.682; 0.55: 323, 0.727; 0.60: 273, 0.771; 0.65: 228, 0.802; 0.70: 179, 0.832; 0.75: 143, 0.870; 0.80: 95, 0.902; 0.85: 42, 0.944; 0.90: 3, 0.956
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.436; 0.35: 487, 0.472; 0.40: 382, 0.514; 0.45: 290, 0.547; 0.50: 187, 0.575; 0.55: 78, 0.595; 0.60: 10, 0.636; 0.65: 0, 0.538
- **K=5**: model 1794528000, labels learned 168007, probability skill vs chance 0.224, widened contest next: False
  - now: threshold 0.7058, hit rate recent 0.841 / long run 0.8087
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.197, naive rule 0.425, lift 2.54x
    - 24h: 56 calls (56 a day), hit rate 0.857, chance 0.202, naive rule 0.445, lift 4.24x
    - 7d: 426 calls (61 a day), hit rate 0.826, chance 0.196, naive rule 0.445, lift 4.22x
    - 30d: 1790 calls (60 a day), hit rate 0.797, chance 0.189, naive rule 0.419, lift 4.21x
  - next: threshold 0.4455, hit rate recent 0.4638 / long run 0.4936
    - 6h: 19 calls (78 a day), hit rate 0.368, chance 0.197, lift 1.87x
    - 24h: 58 calls (58 a day), hit rate 0.431, chance 0.202, lift 2.13x
    - 7d: 381 calls (54 a day), hit rate 0.512, chance 0.196, lift 2.61x
    - 30d: 1703 calls (57 a day), hit rate 0.507, chance 0.189, lift 2.68x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.428; 0.35: 364, 0.476; 0.40: 295, 0.544; 0.45: 239, 0.604; 0.50: 186, 0.655; 0.55: 149, 0.687; 0.60: 116, 0.731; 0.65: 86, 0.768; 0.70: 55, 0.804; 0.75: 27, 0.841; 0.80: 6, 0.839
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 328, 0.398; 0.35: 244, 0.437; 0.40: 156, 0.461; 0.45: 63, 0.506; 0.50: 9, 0.552; 0.55: 1, 0.529
- **K=8**: model 1794960000, labels learned 168004, probability skill vs chance 0.1993, widened contest next: True
  - now: threshold 0.5895, hit rate recent 0.646 / long run 0.6791
    - 6h: 20 calls (82 a day), hit rate 0.350, chance 0.116, naive rule 0.314, lift 3.02x
    - 24h: 62 calls (62 a day), hit rate 0.661, chance 0.133, naive rule 0.373, lift 4.98x
    - 7d: 405 calls (58 a day), hit rate 0.684, chance 0.127, naive rule 0.376, lift 5.37x
    - 30d: 1665 calls (56 a day), hit rate 0.682, chance 0.124, naive rule 0.352, lift 5.51x
  - next: threshold 0.378, hit rate recent 0.3691 / long run 0.4076
    - 6h: 23 calls (95 a day), hit rate 0.217, chance 0.116, lift 1.88x
    - 24h: 64 calls (64 a day), hit rate 0.328, chance 0.133, lift 2.47x
    - 7d: 531 calls (76 a day), hit rate 0.424, chance 0.127, lift 3.32x
    - 30d: 2151 calls (72 a day), hit rate 0.419, chance 0.124, lift 3.38x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 261, 0.425; 0.35: 206, 0.485; 0.40: 161, 0.536; 0.45: 122, 0.578; 0.50: 88, 0.634; 0.55: 64, 0.671; 0.60: 44, 0.711; 0.65: 25, 0.772; 0.70: 9, 0.814; 0.75: 1, 0.719
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 156, 0.376; 0.35: 84, 0.407; 0.40: 31, 0.437; 0.45: 7, 0.473; 0.50: 1, 0.605; 0.55: 0, 0.200
- **K=13**: model 1795478400, labels learned 167999, probability skill vs chance 0.1837, widened contest next: True
  - now: threshold 0.4569, hit rate recent 0.5469 / long run 0.5833
    - 6h: 17 calls (71 a day), hit rate 0.294, chance 0.061, naive rule 0.213, lift 4.83x
    - 24h: 57 calls (58 a day), hit rate 0.526, chance 0.078, naive rule 0.298, lift 6.76x
    - 7d: 351 calls (50 a day), hit rate 0.610, chance 0.084, naive rule 0.337, lift 7.27x
    - 30d: 1587 calls (53 a day), hit rate 0.582, chance 0.080, naive rule 0.302, lift 7.23x
  - next: threshold 0.2994, hit rate recent 0.2577 / long run 0.3295
    - 6h: 19 calls (79 a day), hit rate 0.053, chance 0.061, lift 0.86x
    - 24h: 53 calls (54 a day), hit rate 0.264, chance 0.078, lift 3.39x
    - 7d: 362 calls (52 a day), hit rate 0.356, chance 0.084, lift 4.25x
    - 30d: 1822 calls (61 a day), hit rate 0.334, chance 0.080, lift 4.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 144, 0.425; 0.35: 106, 0.474; 0.40: 72, 0.537; 0.45: 52, 0.584; 0.50: 36, 0.620; 0.55: 22, 0.644; 0.60: 10, 0.661; 0.65: 2, 0.509
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.337; 0.35: 15, 0.375; 0.40: 2, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.146 | 10.04% | 0.950 | 0.600 | 0.251 | 0.417 | 0.038 |
| 6h | 31.115 | 10.77% | 0.897 | 0.553 | 0.250 | 0.490 | 0.755 |
| 24h | 20.817 | 5.68% | 0.897 | 0.506 | 0.250 | 0.492 | 0.710 |
| 7d | 23.607 | 4.91% | 0.902 | 0.502 | 0.250 | 0.509 | 0.656 |
| 30d | 20.376 | 4.91% | 0.900 | 0.500 | 0.250 | 0.507 | 0.705 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.278 | 10.236 | 10.267 | 10.368 | 10.311 | 10.507 | 10.117 | 10.118 | 10.192 | 10.146 |
| 6h | 34.870 | 31.649 | 31.269 | 31.172 | 31.467 | 31.244 | 30.999 | 31.097 | 31.040 | 31.115 |
| 24h | 22.071 | 21.084 | 20.916 | 20.826 | 21.238 | 21.002 | 20.757 | 20.784 | 20.769 | 20.817 |
| 7d | 24.825 | 23.904 | 23.784 | 23.631 | 24.228 | 23.970 | 23.582 | 23.540 | 23.567 | 23.607 |
| 30d | 21.428 | 20.571 | 20.518 | 20.430 | 20.810 | 20.722 | 20.356 | 20.330 | 20.342 | 20.376 |

## Next candle

- candle starting 2026-11-27 20:15 UTC, last close 1667.44
- P(up) 0.4945, return quantiles (bp): {'05': -9.337, '10': -6.805, '25': -3.334, '40': -1.058, '50': -0.076, '60': 1.248, '75': 3.1, '90': 6.463, '95': 8.456}
- changepoint probability 0.0359, regime age 117.3 min
- agent weights: empirical 0.003, ewma 0.036, garch 0.115, har 0.159, bocpd 0.028, hmm 0.080, online_qr 0.326, lgbm 0.256

## Learning log

- 2026-11-25 12:00 UTC: {"garch": {"alpha": 0.091, "beta": 0.8903}, "hmm": {"sd_bp": [4.89, 9.77, 34.58], "stay": [0.96, 0.954, 0.849]}}
- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- 2026-11-26 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.8951}, "hmm": {"sd_bp": [5.1, 9.79, 29.67], "stay": [0.964, 0.952, 0.897]}}
- 2026-11-27 00:00 UTC: {"garch": {"alpha": 0.086, "beta": 0.8972}, "hmm": {"sd_bp": [4.98, 9.67, 29.65], "stay": [0.967, 0.957, 0.909]}, "lgbm": {"challenger_loss": 0.24936, "champion_loss": 0.2495, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48669, "challengers": 1, "chance_loss": 0.61724, "widened": false, "champion_loss": 0.48438, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37811, "challengers": 1, "chance_loss": 0.49376, "widened": false, "champion_loss": 0.37659, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27446, "challengers": 1, "chance_loss": 0.3744, "widened": false, "champion_loss": 0.27383, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21177, "challengers": 1, "chance_loss": 0.29738, "widened": false, "champion_loss": 0.21069, "promoted": false}}
- 2026-11-27 12:00 UTC: {"garch": {"alpha": 0.0974, "beta": 0.8821}, "hmm": {"sd_bp": [5.02, 9.65, 29.47], "stay": [0.968, 0.955, 0.908]}}
- HMM volatility states (sd, bp per minute): [5.02, 9.65, 29.47], current probabilities: [0.912, 0.087, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-27 20:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.451, 'l_abs': 0.691, 'l_hi': 0.707, 'l_lo': 0.715, 'b05': 0.711, 'b25': 0.728, 'b75': 0.675, 'b95': 0.69}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5]], 'cone_width': [1.697, 3.433, 2.361, 4.361, 4.884, 7.135, 8.115, 9.921, 8.752, 8.662, 9.435, 8.219, 13.008, 11.496]}
- calibration offsets (in sigma): {'05': 0.007, '10': 0.024, '25': 0.045, '40': 0.046, '50': -0.02, '60': -0.026, '75': -0.095, '90': -0.084, '95': -0.097}
