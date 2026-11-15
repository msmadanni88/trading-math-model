# ETH-USD 60s candle generator - report

- generated: 2026-11-15 14:37 UTC
- last closed candle: 2026-11-15 14:37 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k5_now 0.735 in the last 7 days, -0.086 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.533 (671) [0.500, 0.566] | 0.523 (2879) [0.507, 0.541] | 0.515 (7097) [0.504, 0.527] | 0.517 (4125) [0.501, 0.533] | 0.397 (58) | 0.500 | flat +0.044 (noise 0.028) |
| colour_clear | 0.560 (801) | 0.542 (5598) [0.532, 0.552] | 0.543 (23921) [0.537, 0.549] | 0.523 (58193) [0.518, 0.529] | 0.543 (33955) [0.538, 0.547] | 0.529 (480) | 0.500 | flat +0.009 (noise 0.012) |
| colour_confident | 0.553 (47) | 0.553 (704) [0.516, 0.576] | 0.586 (4252) [0.575, 0.597] | 0.591 (5944) [0.580, 0.602] | 0.591 (5944) [0.580, 0.602] | 0.487 (117) | 0.500 | flat -0.024 (noise 0.025) |
| colour_next | 0.548 (1439) | 0.532 (10008) [0.522, 0.544] | 0.531 (42872) [0.527, 0.535] | 0.517 (105741) [0.514, 0.521] | 0.530 (61392) [0.526, 0.533] | 0.528 (876) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.499 (20146) | 0.502 (140112) [0.499, 0.504] | 0.501 (600208) [0.500, 0.502] | 0.501 (1480374) [0.500, 0.502] | 0.501 (859488) [0.500, 0.502] | 0.504 (12264) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.667 (3) | 0.610 (159) [0.508, 0.642] | 0.616 (1097) [0.601, 0.632] | 0.628 (1542) [0.611, 0.645] | 0.628 (1542) [0.611, 0.645] | 0.515 (33) | 0.500 | flat -0.005 (noise 0.050) |
| reversal_k13_next | 0.468 (47) | 0.348 (477) [0.320, 0.382] | 0.333 (1830) [0.318, 0.349] | 0.316 (4859) [0.306, 0.326] | 0.329 (2754) [0.317, 0.340] | 0.256 (39) | 0.077 | flat +0.004 (noise 0.033) |
| reversal_k13_now | 0.750 (48) | 0.594 (347) [0.552, 0.644] | 0.567 (1647) [0.546, 0.588] | 0.575 (3806) [0.562, 0.588] | 0.571 (2334) [0.553, 0.589] | 0.583 (24) | 0.077 | flat +0.028 (noise 0.037) |
| reversal_k3_next | 0.778 (27) | 0.630 (330) [0.591, 0.677] | 0.599 (2610) [0.586, 0.612] | 0.590 (6229) [0.581, 0.598] | 0.591 (3789) [0.580, 0.602] | 0.500 (20) | 0.293 | flat +0.010 (noise 0.034) |
| reversal_k3_now | 0.947 (57) | 0.927 (410) [0.916, 0.938] | 0.931 (1753) [0.921, 0.942] | 0.935 (4259) [0.929, 0.941] | 0.930 (2496) [0.923, 0.938] | 0.909 (22) | 0.293 | flat +0.018 (noise 0.019) |
| reversal_k5_next | 0.679 (53) | 0.524 (439) [0.480, 0.576] | 0.491 (2548) [0.474, 0.509] | 0.487 (5659) [0.476, 0.499] | 0.483 (3669) [0.469, 0.498] | 0.375 (40) | 0.186 | flat -0.004 (noise 0.035) |
| reversal_k5_now | 0.769 (65) | 0.735 (426) [0.698, 0.771] | 0.801 (1702) [0.784, 0.816] | 0.818 (3996) [0.808, 0.829] | 0.805 (2385) [0.792, 0.818] | 0.706 (34) | 0.187 | down -0.086 (noise 0.029) |
| reversal_k8_next | 0.571 (56) | 0.433 (471) [0.395, 0.477] | 0.402 (2558) [0.386, 0.420] | 0.398 (5749) [0.388, 0.409] | 0.399 (3643) [0.387, 0.412] | 0.293 (41) | 0.121 | flat -0.010 (noise 0.034) |
| reversal_k8_now | 0.826 (46) | 0.676 (367) [0.635, 0.724] | 0.685 (1548) [0.664, 0.705] | 0.699 (3848) [0.687, 0.712] | 0.689 (2261) [0.672, 0.705] | 0.500 (30) | 0.122 | flat -0.020 (noise 0.034) |
| overall | 0.506 (22080) | 0.506 (154058) [0.503, 0.508] | 0.505 (662155) [0.504, 0.506] | 0.504 (1631617) [0.503, 0.505] | 0.505 (948336) [0.504, 0.506] | 0.505 (13448) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06651, 0.09879] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.529, 'levels': [{'threshold': 0.06651, 'calls_per_day': 134.4, 'win_rate': 0.5413}, {'threshold': 0.09879, 'calls_per_day': 30.2, 'win_rate': 0.5755}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42872, 'rate': 0.531}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15173 | 0.347 | 0.534 (14936) | 0.565 (2294) | 0.740 (2529) |
| volatility: normal | 15172 | 0.371 | 0.529 (15112) | 0.616 (1319) | 0.748 (2341) |
| volatility: wild | 15172 | 0.388 | 0.528 (15136) | 0.585 (840) | 0.757 (2084) |
| session: Asia 00-08 | 15360 | 0.368 | 0.533 (15239) | 0.581 (1601) | 0.747 (2300) |
| session: Europe 08-13 | 9600 | 0.362 | 0.531 (9519) | 0.590 (1132) | 0.749 (1570) |
| session: US 13-21 | 14977 | 0.376 | 0.532 (14880) | 0.600 (1179) | 0.750 (2284) |
| session: late 21-24 | 5580 | 0.363 | 0.516 (5546) | 0.542 (541) | 0.740 (800) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.409 | 0.387 | 0.339 | 0.339 | 0.567 | 0.303 | 0.514 | 1.126 |
| 6h | 360 | 0.387 | 0.379 | 0.280 | 0.308 | 0.546 | 0.278 | 0.496 | 1.339 |
| 24h | 1440 | 0.396 | 0.389 | 0.299 | 0.330 | 0.533 | 0.280 | 0.511 | 1.236 |
| 7d | 10080 | 0.383 | 0.378 | 0.296 | 0.326 | 0.529 | 0.272 | 0.493 | 1.171 |
| 30d | 43200 | 0.369 | 0.362 | 0.279 | 0.310 | 0.531 | 0.266 | 0.472 | 1.245 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.409 / 0.567 / 0.933; 2: 0.397 / 0.533 / 0.867; 3: 0.420 / 0.700 / 0.883; 4: 0.349 / 0.400 / 0.800; 5: 0.400 / 0.583 / 0.767; 6: 0.365 / 0.400 / 0.767; 7: 0.400 / 0.550 / 0.767; 8: 0.391 / 0.617 / 0.767; 9: 0.365 / 0.450 / 0.817; 10: 0.389 / 0.550 / 0.833; 11: 0.347 / 0.417 / 0.800; 12: 0.369 / 0.467 / 0.800; 13: 0.402 / 0.583 / 0.783; 14: 0.405 / 0.567 / 0.783; 15: 0.406 / 0.583 / 0.767
- 6h: 1: 0.387 / 0.546 / 0.914; 2: 0.372 / 0.501 / 0.911; 3: 0.387 / 0.582 / 0.922; 4: 0.362 / 0.493 / 0.878; 5: 0.366 / 0.501 / 0.872; 6: 0.357 / 0.476 / 0.878; 7: 0.359 / 0.496 / 0.900; 8: 0.369 / 0.540 / 0.889; 9: 0.347 / 0.460 / 0.908; 10: 0.370 / 0.532 / 0.914; 11: 0.363 / 0.499 / 0.906; 12: 0.357 / 0.474 / 0.908; 13: 0.363 / 0.515 / 0.900; 14: 0.368 / 0.507 / 0.894; 15: 0.365 / 0.487 / 0.897
- 24h: 1: 0.396 / 0.533 / 0.910; 2: 0.377 / 0.495 / 0.901; 3: 0.389 / 0.532 / 0.906; 4: 0.376 / 0.489 / 0.892; 5: 0.380 / 0.502 / 0.888; 6: 0.377 / 0.499 / 0.886; 7: 0.376 / 0.498 / 0.895; 8: 0.376 / 0.510 / 0.891; 9: 0.372 / 0.490 / 0.903; 10: 0.377 / 0.521 / 0.902; 11: 0.378 / 0.498 / 0.905; 12: 0.371 / 0.495 / 0.903; 13: 0.370 / 0.499 / 0.903; 14: 0.374 / 0.497 / 0.903; 15: 0.370 / 0.496 / 0.899
- 7d: 1: 0.383 / 0.529 / 0.901; 2: 0.367 / 0.488 / 0.900; 3: 0.375 / 0.519 / 0.900; 4: 0.366 / 0.490 / 0.898; 5: 0.369 / 0.501 / 0.897; 6: 0.366 / 0.495 / 0.897; 7: 0.368 / 0.502 / 0.898; 8: 0.369 / 0.510 / 0.898; 9: 0.365 / 0.497 / 0.900; 10: 0.367 / 0.504 / 0.899; 11: 0.369 / 0.514 / 0.900; 12: 0.364 / 0.498 / 0.899; 13: 0.366 / 0.504 / 0.899; 14: 0.365 / 0.504 / 0.900; 15: 0.364 / 0.498 / 0.899
- 30d: 1: 0.369 / 0.531 / 0.897; 2: 0.355 / 0.492 / 0.900; 3: 0.359 / 0.511 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.353 / 0.500 / 0.900; 7: 0.354 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.501 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.352 / 0.500 / 0.900; 14: 0.352 / 0.501 / 0.900; 15: 0.351 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.109 (body 0.064, range 0.154); 'price stays where it was' would score 0.137; colour right 0.500; typical miss of the close 17.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.146 (body 0.095, range 0.197); 'price stays where it was' would score 0.135; colour right 0.496; typical miss of the close 14.3 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.131 (body 0.085, range 0.176); 'price stays where it was' would score 0.136; colour right 0.511; typical miss of the close 22.4 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.126 (body 0.083, range 0.168); 'price stays where it was' would score 0.127; colour right 0.505; typical miss of the close 12.9 bp; chain ended on the right side 0.519 of 671 chains; n=10080
- 30d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.2 bp; chain ended on the right side 0.521 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 4.7; 2: 0.204 / 5.6; 3: 0.170 / 7.3; 4: 0.133 / 7.6; 5: 0.127 / 8.2; 6: 0.119 / 9.1; 7: 0.110 / 9.4; 8: 0.097 / 10.4; 9: 0.091 / 10.7; 10: 0.091 / 11.0; 11: 0.088 / 11.0; 12: 0.079 / 11.5; 13: 0.074 / 12.1; 14: 0.069 / 12.5; 15: 0.068 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 150391, probability skill vs chance 0.2273, widened contest next: False
  - now: threshold 0.8378, hit rate recent 0.9239 / long run 0.9261
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.318, naive rule 0.535, lift 2.79x
    - 24h: 37 calls (37 a day), hit rate 0.919, chance 0.291, naive rule 0.514, lift 3.15x
    - 7d: 396 calls (57 a day), hit rate 0.924, chance 0.288, naive rule 0.498, lift 3.21x
    - 30d: 1730 calls (58 a day), hit rate 0.929, chance 0.294, naive rule 0.498, lift 3.16x
  - next: threshold 0.5637, hit rate recent 0.6425 / long run 0.6158
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.318, lift 1.40x
    - 24h: 27 calls (27 a day), hit rate 0.556, chance 0.291, lift 1.91x
    - 7d: 304 calls (43 a day), hit rate 0.628, chance 0.288, lift 2.18x
    - 30d: 2536 calls (85 a day), hit rate 0.599, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.500; 0.35: 532, 0.525; 0.40: 474, 0.579; 0.45: 406, 0.649; 0.50: 357, 0.694; 0.55: 310, 0.738; 0.60: 260, 0.784; 0.65: 219, 0.813; 0.70: 171, 0.843; 0.75: 138, 0.874; 0.80: 91, 0.904; 0.85: 46, 0.940; 0.90: 4, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.432; 0.35: 496, 0.465; 0.40: 394, 0.504; 0.45: 296, 0.539; 0.50: 188, 0.571; 0.55: 82, 0.584; 0.60: 11, 0.658; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 150389, probability skill vs chance 0.2226, widened contest next: True
  - now: threshold 0.6937, hit rate recent 0.7357 / long run 0.7738
    - 6h: 14 calls (57 a day), hit rate 0.714, chance 0.195, naive rule 0.450, lift 3.65x
    - 24h: 57 calls (57 a day), hit rate 0.719, chance 0.187, naive rule 0.427, lift 3.85x
    - 7d: 427 calls (61 a day), hit rate 0.735, chance 0.183, naive rule 0.406, lift 4.03x
    - 30d: 1685 calls (56 a day), hit rate 0.798, chance 0.186, naive rule 0.408, lift 4.28x
  - next: threshold 0.4528, hit rate recent 0.5018 / long run 0.5115
    - 6h: 16 calls (65 a day), hit rate 0.500, chance 0.195, lift 2.56x
    - 24h: 57 calls (57 a day), hit rate 0.439, chance 0.187, lift 2.35x
    - 7d: 429 calls (61 a day), hit rate 0.513, chance 0.183, lift 2.81x
    - 30d: 2510 calls (84 a day), hit rate 0.492, chance 0.186, lift 2.64x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.421; 0.35: 356, 0.478; 0.40: 288, 0.548; 0.45: 234, 0.605; 0.50: 186, 0.653; 0.55: 148, 0.691; 0.60: 112, 0.739; 0.65: 76, 0.776; 0.70: 47, 0.808; 0.75: 27, 0.844; 0.80: 8, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.385; 0.35: 255, 0.426; 0.40: 160, 0.459; 0.45: 65, 0.503; 0.50: 9, 0.551; 0.55: 1, 0.419
- **K=8**: model 1794614400, labels learned 150386, probability skill vs chance 0.2154, widened contest next: True
  - now: threshold 0.5675, hit rate recent 0.6455 / long run 0.6796
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.126, naive rule 0.439, lift 5.06x
    - 24h: 45 calls (45 a day), hit rate 0.600, chance 0.123, naive rule 0.374, lift 4.87x
    - 7d: 363 calls (52 a day), hit rate 0.667, chance 0.123, naive rule 0.354, lift 5.40x
    - 30d: 1535 calls (51 a day), hit rate 0.683, chance 0.121, naive rule 0.338, lift 5.64x
  - next: threshold 0.3669, hit rate recent 0.3956 / long run 0.4231
    - 6h: 16 calls (66 a day), hit rate 0.250, chance 0.126, lift 1.99x
    - 24h: 63 calls (63 a day), hit rate 0.365, chance 0.123, lift 2.97x
    - 7d: 459 calls (66 a day), hit rate 0.431, chance 0.123, lift 3.49x
    - 30d: 2518 calls (84 a day), hit rate 0.403, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.428; 0.35: 193, 0.491; 0.40: 152, 0.535; 0.45: 117, 0.580; 0.50: 83, 0.639; 0.55: 59, 0.672; 0.60: 39, 0.710; 0.65: 23, 0.770; 0.70: 11, 0.812; 0.75: 2, 0.769
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 166, 0.368; 0.35: 84, 0.396; 0.40: 24, 0.427; 0.45: 5, 0.438; 0.50: 1, 0.783
- **K=13**: model 1794700800, labels learned 150381, probability skill vs chance 0.1999, widened contest next: False
  - now: threshold 0.4451, hit rate recent 0.6392 / long run 0.5823
    - 6h: 7 calls (29 a day), hit rate 0.857, chance 0.078, naive rule 0.413, lift 10.95x
    - 24h: 44 calls (44 a day), hit rate 0.614, chance 0.080, naive rule 0.329, lift 7.67x
    - 7d: 337 calls (48 a day), hit rate 0.596, chance 0.081, naive rule 0.312, lift 7.40x
    - 30d: 1620 calls (54 a day), hit rate 0.569, chance 0.078, naive rule 0.287, lift 7.29x
  - next: threshold 0.2993, hit rate recent 0.3274 / long run 0.3371
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.078, lift 5.32x
    - 24h: 58 calls (59 a day), hit rate 0.276, chance 0.080, lift 3.45x
    - 7d: 456 calls (65 a day), hit rate 0.353, chance 0.081, lift 4.38x
    - 30d: 1828 calls (61 a day), hit rate 0.331, chance 0.078, lift 4.24x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.432; 0.35: 97, 0.480; 0.40: 67, 0.539; 0.45: 46, 0.590; 0.50: 31, 0.634; 0.55: 20, 0.658; 0.60: 11, 0.698; 0.65: 3, 0.642; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.339; 0.35: 13, 0.339; 0.40: 2, 0.421; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 26.171 | 4.17% | 0.917 | 0.450 | 0.250 | 0.517 | 0.542 |
| 6h | 26.582 | 4.75% | 0.908 | 0.508 | 0.250 | 0.504 | 0.525 |
| 24h | 37.192 | 5.82% | 0.905 | 0.497 | 0.250 | 0.516 | 0.631 |
| 7d | 22.711 | 5.51% | 0.902 | 0.500 | 0.250 | 0.513 | 0.663 |
| 30d | 16.753 | 4.86% | 0.900 | 0.500 | 0.250 | 0.505 | 0.716 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 27.312 | 26.840 | 26.678 | 25.881 | 26.911 | 26.958 | 26.127 | 26.097 | 26.115 | 26.171 |
| 6h | 27.908 | 27.110 | 26.950 | 26.488 | 27.282 | 26.824 | 26.451 | 26.504 | 26.520 | 26.582 |
| 24h | 39.491 | 37.461 | 37.489 | 37.213 | 37.991 | 37.736 | 37.204 | 37.156 | 37.139 | 37.192 |
| 7d | 24.036 | 22.925 | 22.896 | 22.846 | 23.205 | 23.064 | 22.690 | 22.656 | 22.676 | 22.711 |
| 30d | 17.609 | 16.918 | 16.874 | 16.811 | 17.085 | 17.034 | 16.737 | 16.717 | 16.724 | 16.753 |

## Next candle

- candle starting 2026-11-15 14:37 UTC, last close 1812.23
- P(up) 0.496, return quantiles (bp): {'05': -18.666, '10': -13.97, '25': -7.863, '40': -2.647, '50': -0.112, '60': 2.648, '75': 7.339, '90': 13.892, '95': 18.099}
- changepoint probability 0.0775, regime age 176.7 min
- agent weights: empirical 0.003, ewma 0.066, garch 0.081, har 0.241, bocpd 0.015, hmm 0.050, online_qr 0.267, lgbm 0.278

## Learning log

- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- HMM volatility states (sd, bp per minute): [5.18, 9.59, 24.41], current probabilities: [0.091, 0.78, 0.129]
- live generator: {'versions': 60, 'latest_effective': '2026-11-15 14:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.277, 'l_abs': 0.747, 'l_hi': 0.805, 'l_lo': 0.744, 'b05': 0.756, 'b25': 0.762, 'b75': 0.63, 'b95': 0.755}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.499, 1.599, 2.76, 3.092, 3.462, 3.13, 3.632, 3.098, 3.272, 3.725, 4.139, 4.584, 4.672, 5.043]}
- calibration offsets (in sigma): {'05': 0.098, '10': 0.076, '25': -0.04, '40': -0.016, '50': -0.03, '60': -0.034, '75': -0.03, '90': -0.046, '95': -0.058}
