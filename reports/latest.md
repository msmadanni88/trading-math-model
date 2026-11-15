# ETH-USD 60s candle generator - report

- generated: 2026-11-15 23:52 UTC
- last closed candle: 2026-11-15 23:52 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_now 0.735 in the last 7 days, -0.086 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.533 (671) [0.500, 0.566] | 0.523 (2879) [0.507, 0.541] | 0.515 (7097) [0.504, 0.527] | 0.517 (4125) [0.501, 0.533] | 0.432 (95) | 0.500 | flat +0.044 (noise 0.028) |
| colour_clear | 0.560 (801) | 0.542 (5598) [0.532, 0.552] | 0.543 (23921) [0.537, 0.549] | 0.523 (58193) [0.518, 0.529] | 0.543 (33955) [0.538, 0.547] | 0.549 (774) | 0.500 | flat +0.009 (noise 0.012) |
| colour_confident | 0.553 (47) | 0.553 (704) [0.516, 0.576] | 0.586 (4252) [0.575, 0.597] | 0.591 (5944) [0.580, 0.602] | 0.591 (5944) [0.580, 0.602] | 0.515 (206) | 0.500 | flat -0.024 (noise 0.025) |
| colour_next | 0.548 (1439) | 0.532 (10008) [0.522, 0.544] | 0.531 (42872) [0.527, 0.535] | 0.517 (105741) [0.514, 0.521] | 0.530 (61392) [0.526, 0.533] | 0.541 (1428) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.499 (20146) | 0.502 (140112) [0.499, 0.504] | 0.501 (600208) [0.500, 0.502] | 0.501 (1480374) [0.500, 0.502] | 0.501 (859488) [0.500, 0.502] | 0.505 (19992) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.667 (3) | 0.610 (159) [0.508, 0.642] | 0.616 (1097) [0.601, 0.632] | 0.628 (1542) [0.611, 0.645] | 0.628 (1542) [0.611, 0.645] | 0.589 (56) | 0.500 | flat -0.005 (noise 0.050) |
| reversal_k13_next | 0.468 (47) | 0.348 (477) [0.320, 0.382] | 0.333 (1830) [0.318, 0.349] | 0.316 (4859) [0.306, 0.326] | 0.329 (2754) [0.317, 0.340] | 0.290 (62) | 0.077 | flat +0.004 (noise 0.033) |
| reversal_k13_now | 0.750 (48) | 0.594 (347) [0.552, 0.644] | 0.567 (1647) [0.546, 0.588] | 0.575 (3806) [0.562, 0.588] | 0.571 (2334) [0.553, 0.589] | 0.625 (48) | 0.077 | flat +0.028 (noise 0.037) |
| reversal_k3_next | 0.778 (27) | 0.630 (330) [0.591, 0.677] | 0.599 (2610) [0.586, 0.612] | 0.590 (6229) [0.581, 0.598] | 0.591 (3789) [0.580, 0.602] | 0.571 (35) | 0.293 | flat +0.010 (noise 0.034) |
| reversal_k3_now | 0.947 (57) | 0.927 (410) [0.916, 0.938] | 0.931 (1753) [0.921, 0.942] | 0.935 (4259) [0.929, 0.941] | 0.930 (2496) [0.923, 0.938] | 0.933 (45) | 0.293 | flat +0.018 (noise 0.019) |
| reversal_k5_next | 0.679 (53) | 0.524 (439) [0.480, 0.576] | 0.491 (2548) [0.474, 0.509] | 0.487 (5659) [0.476, 0.499] | 0.483 (3669) [0.469, 0.498] | 0.456 (57) | 0.186 | flat -0.004 (noise 0.035) |
| reversal_k5_now | 0.769 (65) | 0.735 (426) [0.698, 0.771] | 0.801 (1702) [0.784, 0.816] | 0.818 (3996) [0.808, 0.829] | 0.805 (2385) [0.792, 0.818] | 0.809 (63) | 0.187 | down -0.086 (noise 0.029) |
| reversal_k8_next | 0.571 (56) | 0.433 (471) [0.395, 0.477] | 0.402 (2558) [0.386, 0.420] | 0.398 (5749) [0.388, 0.409] | 0.399 (3643) [0.387, 0.412] | 0.343 (67) | 0.121 | flat -0.010 (noise 0.034) |
| reversal_k8_now | 0.826 (46) | 0.676 (367) [0.635, 0.724] | 0.685 (1548) [0.664, 0.705] | 0.699 (3848) [0.687, 0.712] | 0.689 (2261) [0.672, 0.705] | 0.603 (58) | 0.122 | flat -0.020 (noise 0.034) |
| overall | 0.506 (22080) | 0.506 (154058) [0.503, 0.508] | 0.505 (662155) [0.504, 0.506] | 0.504 (1631617) [0.503, 0.505] | 0.505 (948336) [0.504, 0.506] | 0.508 (21950) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06471, 0.09561] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5286, 'levels': [{'threshold': 0.06471, 'calls_per_day': 134.5, 'win_rate': 0.5466}, {'threshold': 0.09561, 'calls_per_day': 30.1, 'win_rate': 0.5735}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42874, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15358 | 0.347 | 0.533 (15121) | 0.564 (2314) | 0.739 (2562) |
| volatility: normal | 15357 | 0.372 | 0.530 (15296) | 0.616 (1339) | 0.749 (2364) |
| volatility: wild | 15357 | 0.388 | 0.528 (15319) | 0.580 (889) | 0.760 (2132) |
| session: Asia 00-08 | 15360 | 0.368 | 0.533 (15239) | 0.581 (1601) | 0.747 (2300) |
| session: Europe 08-13 | 9600 | 0.362 | 0.531 (9519) | 0.590 (1132) | 0.749 (1570) |
| session: US 13-21 | 15360 | 0.376 | 0.533 (15261) | 0.600 (1231) | 0.752 (2347) |
| session: late 21-24 | 5752 | 0.363 | 0.517 (5717) | 0.538 (578) | 0.744 (841) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.355 | 0.369 | 0.285 | 0.285 | 0.467 | 0.230 | 0.480 | 1.213 |
| 6h | 360 | 0.391 | 0.378 | 0.296 | 0.334 | 0.566 | 0.282 | 0.500 | 1.209 |
| 24h | 1440 | 0.385 | 0.375 | 0.290 | 0.324 | 0.542 | 0.274 | 0.497 | 1.248 |
| 7d | 10080 | 0.384 | 0.379 | 0.296 | 0.328 | 0.529 | 0.272 | 0.495 | 1.162 |
| 30d | 43200 | 0.369 | 0.362 | 0.279 | 0.310 | 0.531 | 0.266 | 0.472 | 1.245 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.355 / 0.467 / 0.900; 2: 0.398 / 0.550 / 0.850; 3: 0.379 / 0.483 / 0.833; 4: 0.380 / 0.483 / 0.783; 5: 0.355 / 0.417 / 0.750; 6: 0.390 / 0.583 / 0.750; 7: 0.386 / 0.550 / 0.717; 8: 0.373 / 0.483 / 0.733; 9: 0.344 / 0.450 / 0.750; 10: 0.370 / 0.500 / 0.750; 11: 0.369 / 0.517 / 0.683; 12: 0.368 / 0.483 / 0.717; 13: 0.380 / 0.567 / 0.717; 14: 0.354 / 0.533 / 0.700; 15: 0.364 / 0.600 / 0.700
- 6h: 1: 0.391 / 0.566 / 0.906; 2: 0.369 / 0.504 / 0.872; 3: 0.372 / 0.499 / 0.878; 4: 0.368 / 0.473 / 0.883; 5: 0.366 / 0.507 / 0.889; 6: 0.375 / 0.532 / 0.881; 7: 0.366 / 0.487 / 0.850; 8: 0.380 / 0.515 / 0.872; 9: 0.362 / 0.482 / 0.850; 10: 0.378 / 0.518 / 0.836; 11: 0.370 / 0.493 / 0.833; 12: 0.371 / 0.527 / 0.814; 13: 0.374 / 0.507 / 0.822; 14: 0.364 / 0.507 / 0.822; 15: 0.370 / 0.513 / 0.817
- 24h: 1: 0.385 / 0.542 / 0.909; 2: 0.371 / 0.508 / 0.895; 3: 0.373 / 0.514 / 0.895; 4: 0.367 / 0.493 / 0.896; 5: 0.369 / 0.501 / 0.896; 6: 0.372 / 0.522 / 0.893; 7: 0.365 / 0.496 / 0.889; 8: 0.370 / 0.513 / 0.894; 9: 0.363 / 0.491 / 0.891; 10: 0.370 / 0.519 / 0.893; 11: 0.368 / 0.491 / 0.890; 12: 0.367 / 0.511 / 0.885; 13: 0.363 / 0.497 / 0.888; 14: 0.367 / 0.503 / 0.888; 15: 0.366 / 0.509 / 0.883
- 7d: 1: 0.384 / 0.529 / 0.902; 2: 0.368 / 0.488 / 0.900; 3: 0.376 / 0.516 / 0.900; 4: 0.368 / 0.491 / 0.900; 5: 0.370 / 0.500 / 0.900; 6: 0.368 / 0.497 / 0.899; 7: 0.370 / 0.502 / 0.899; 8: 0.371 / 0.511 / 0.900; 9: 0.366 / 0.496 / 0.899; 10: 0.369 / 0.505 / 0.899; 11: 0.371 / 0.514 / 0.899; 12: 0.366 / 0.499 / 0.898; 13: 0.368 / 0.505 / 0.899; 14: 0.366 / 0.500 / 0.899; 15: 0.367 / 0.500 / 0.898
- 30d: 1: 0.369 / 0.531 / 0.897; 2: 0.355 / 0.492 / 0.900; 3: 0.359 / 0.512 / 0.900; 4: 0.354 / 0.496 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.353 / 0.500 / 0.900; 7: 0.354 / 0.499 / 0.899; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.501 / 0.899; 10: 0.354 / 0.503 / 0.899; 11: 0.352 / 0.503 / 0.899; 12: 0.352 / 0.503 / 0.899; 13: 0.352 / 0.499 / 0.899; 14: 0.352 / 0.501 / 0.899; 15: 0.351 / 0.501 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.129 (body 0.091, range 0.168); 'price stays where it was' would score 0.163; colour right 0.500; typical miss of the close 12.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.122 (body 0.082, range 0.163); 'price stays where it was' would score 0.131; colour right 0.493; typical miss of the close 14.6 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.124 (body 0.080, range 0.169); 'price stays where it was' would score 0.133; colour right 0.494; typical miss of the close 18.3 bp; chain ended on the right side 0.427 of 96 chains; n=1440
- 7d: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.128; colour right 0.503; typical miss of the close 13.4 bp; chain ended on the right side 0.520 of 671 chains; n=10080
- 30d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.2 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.204 / 5.6; 3: 0.169 / 7.4; 4: 0.133 / 7.6; 5: 0.126 / 8.3; 6: 0.119 / 9.1; 7: 0.111 / 9.4; 8: 0.098 / 10.4; 9: 0.092 / 10.7; 10: 0.092 / 11.0; 11: 0.088 / 11.1; 12: 0.078 / 11.6; 13: 0.074 / 12.1; 14: 0.069 / 12.5; 15: 0.068 / 12.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 150946, probability skill vs chance 0.2296, widened contest next: False
  - now: threshold 0.8374, hit rate recent 0.9345 / long run 0.9272
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.277, naive rule 0.488, lift 3.38x
    - 24h: 45 calls (45 a day), hit rate 0.933, chance 0.300, naive rule 0.522, lift 3.11x
    - 7d: 396 calls (57 a day), hit rate 0.924, chance 0.288, naive rule 0.500, lift 3.21x
    - 30d: 1740 calls (58 a day), hit rate 0.929, chance 0.294, naive rule 0.499, lift 3.16x
  - next: threshold 0.5628, hit rate recent 0.6446 / long run 0.617
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.277, lift 2.16x
    - 24h: 36 calls (36 a day), hit rate 0.583, chance 0.300, lift 1.95x
    - 7d: 300 calls (43 a day), hit rate 0.623, chance 0.288, lift 2.16x
    - 30d: 2515 calls (84 a day), hit rate 0.600, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.501; 0.35: 531, 0.526; 0.40: 474, 0.580; 0.45: 406, 0.650; 0.50: 357, 0.695; 0.55: 310, 0.738; 0.60: 260, 0.784; 0.65: 220, 0.812; 0.70: 171, 0.843; 0.75: 138, 0.874; 0.80: 91, 0.905; 0.85: 46, 0.940; 0.90: 4, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.432; 0.35: 495, 0.466; 0.40: 394, 0.505; 0.45: 295, 0.540; 0.50: 188, 0.572; 0.55: 82, 0.586; 0.60: 11, 0.656; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 150944, probability skill vs chance 0.2277, widened contest next: False
  - now: threshold 0.6942, hit rate recent 0.809 / long run 0.7812
    - 6h: 21 calls (86 a day), hit rate 0.905, chance 0.180, naive rule 0.395, lift 5.03x
    - 24h: 63 calls (63 a day), hit rate 0.810, chance 0.196, naive rule 0.438, lift 4.14x
    - 7d: 432 calls (62 a day), hit rate 0.743, chance 0.184, naive rule 0.408, lift 4.05x
    - 30d: 1701 calls (57 a day), hit rate 0.798, chance 0.187, naive rule 0.409, lift 4.28x
  - next: threshold 0.4521, hit rate recent 0.5363 / long run 0.5152
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.180, lift 2.99x
    - 24h: 58 calls (58 a day), hit rate 0.466, chance 0.196, lift 2.38x
    - 7d: 416 calls (59 a day), hit rate 0.505, chance 0.184, lift 2.75x
    - 30d: 2491 calls (83 a day), hit rate 0.494, chance 0.187, lift 2.65x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.421; 0.35: 357, 0.478; 0.40: 288, 0.548; 0.45: 234, 0.606; 0.50: 186, 0.652; 0.55: 148, 0.690; 0.60: 112, 0.739; 0.65: 77, 0.776; 0.70: 48, 0.809; 0.75: 28, 0.843; 0.80: 8, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.386; 0.35: 254, 0.426; 0.40: 160, 0.459; 0.45: 64, 0.506; 0.50: 9, 0.553; 0.55: 1, 0.433
- **K=8**: model 1794614400, labels learned 150941, probability skill vs chance 0.2141, widened contest next: False
  - now: threshold 0.5669, hit rate recent 0.6728 / long run 0.6812
    - 6h: 19 calls (78 a day), hit rate 0.684, chance 0.119, naive rule 0.353, lift 5.77x
    - 24h: 58 calls (58 a day), hit rate 0.603, chance 0.121, naive rule 0.363, lift 4.97x
    - 7d: 372 calls (53 a day), hit rate 0.667, chance 0.123, naive rule 0.355, lift 5.41x
    - 30d: 1548 calls (52 a day), hit rate 0.683, chance 0.121, naive rule 0.340, lift 5.63x
  - next: threshold 0.3691, hit rate recent 0.4032 / long run 0.4231
    - 6h: 16 calls (66 a day), hit rate 0.375, chance 0.119, lift 3.16x
    - 24h: 68 calls (68 a day), hit rate 0.353, chance 0.121, lift 2.91x
    - 7d: 450 calls (64 a day), hit rate 0.436, chance 0.123, lift 3.53x
    - 30d: 2506 calls (84 a day), hit rate 0.405, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.428; 0.35: 194, 0.490; 0.40: 153, 0.534; 0.45: 117, 0.580; 0.50: 83, 0.639; 0.55: 59, 0.672; 0.60: 40, 0.713; 0.65: 23, 0.771; 0.70: 11, 0.814; 0.75: 2, 0.769
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 165, 0.369; 0.35: 84, 0.398; 0.40: 24, 0.431; 0.45: 5, 0.449; 0.50: 1, 0.783
- **K=13**: model 1794700800, labels learned 150936, probability skill vs chance 0.2033, widened contest next: False
  - now: threshold 0.4439, hit rate recent 0.6491 / long run 0.5856
    - 6h: 16 calls (67 a day), hit rate 0.625, chance 0.070, naive rule 0.282, lift 8.98x
    - 24h: 48 calls (49 a day), hit rate 0.625, chance 0.076, naive rule 0.311, lift 8.17x
    - 7d: 337 calls (48 a day), hit rate 0.602, chance 0.081, naive rule 0.313, lift 7.46x
    - 30d: 1623 calls (54 a day), hit rate 0.570, chance 0.078, naive rule 0.288, lift 7.31x
  - next: threshold 0.2987, hit rate recent 0.3347 / long run 0.3375
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.070, lift 4.49x
    - 24h: 63 calls (64 a day), hit rate 0.302, chance 0.076, lift 3.94x
    - 7d: 438 calls (63 a day), hit rate 0.349, chance 0.081, lift 4.33x
    - 30d: 1831 calls (61 a day), hit rate 0.333, chance 0.078, lift 4.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.432; 0.35: 97, 0.480; 0.40: 67, 0.540; 0.45: 46, 0.591; 0.50: 32, 0.635; 0.55: 20, 0.657; 0.60: 11, 0.697; 0.65: 3, 0.642; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.341; 0.35: 13, 0.343; 0.40: 2, 0.432; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 27.956 | 1.14% | 0.883 | 0.400 | 0.252 | 0.483 | 0.370 |
| 6h | 18.963 | 8.81% | 0.911 | 0.492 | 0.251 | 0.507 | 0.407 |
| 24h | 28.831 | 4.79% | 0.904 | 0.499 | 0.250 | 0.504 | 0.642 |
| 7d | 22.880 | 5.01% | 0.903 | 0.500 | 0.250 | 0.513 | 0.655 |
| 30d | 16.797 | 4.87% | 0.900 | 0.500 | 0.250 | 0.505 | 0.714 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 28.279 | 28.141 | 27.917 | 27.580 | 29.305 | 28.439 | 28.094 | 27.972 | 27.891 | 27.956 |
| 6h | 20.796 | 19.079 | 19.125 | 18.968 | 19.533 | 19.354 | 18.930 | 18.908 | 18.946 | 18.963 |
| 24h | 30.283 | 29.057 | 28.978 | 28.806 | 29.483 | 29.160 | 28.828 | 28.753 | 28.775 | 28.831 |
| 7d | 24.087 | 23.088 | 23.073 | 22.992 | 23.413 | 23.221 | 22.867 | 22.831 | 22.844 | 22.880 |
| 30d | 17.658 | 16.961 | 16.920 | 16.854 | 17.135 | 17.083 | 16.781 | 16.760 | 16.768 | 16.797 |

## Next candle

- candle starting 2026-11-15 23:52 UTC, last close 1833.2
- P(up) 0.5074, return quantiles (bp): {'05': -10.637, '10': -7.956, '25': -3.896, '40': -1.516, '50': 0.119, '60': 1.7, '75': 4.374, '90': 8.121, '95': 11.169}
- changepoint probability 0.0731, regime age 31.3 min
- agent weights: empirical 0.003, ewma 0.091, garch 0.094, har 0.250, bocpd 0.012, hmm 0.045, online_qr 0.235, lgbm 0.270

## Learning log

- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- HMM volatility states (sd, bp per minute): [5.18, 9.59, 24.41], current probabilities: [0.39, 0.595, 0.015]
- live generator: {'versions': 60, 'latest_effective': '2026-11-16 00:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.267, 'l_abs': 0.768, 'l_hi': 0.766, 'l_lo': 0.709, 'b05': 0.757, 'b25': 0.768, 'b75': 0.723, 'b95': 0.751}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.741, 2.094, 2.522, 3.0, 3.497, 4.267, 3.818, 4.484, 4.736, 5.181, 6.237, 6.004, 6.243, 7.157]}
- calibration offsets (in sigma): {'05': 0.1255, '10': 0.081, '25': 0.0575, '40': 0.034, '50': 0.025, '60': 0.026, '75': 0.0225, '90': -0.051, '95': -0.0555}
