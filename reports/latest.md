# ETH-USD 60s candle generator - report

- generated: 2026-11-15 19:57 UTC
- last closed candle: 2026-11-15 19:57 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_now 0.735 in the last 7 days, -0.086 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.533 (671) [0.500, 0.566] | 0.523 (2879) [0.507, 0.541] | 0.515 (7097) [0.504, 0.527] | 0.517 (4125) [0.501, 0.533] | 0.392 (79) | 0.500 | flat +0.044 (noise 0.028) |
| colour_clear | 0.560 (801) | 0.542 (5598) [0.532, 0.552] | 0.543 (23921) [0.537, 0.549] | 0.523 (58193) [0.518, 0.529] | 0.543 (33955) [0.538, 0.547] | 0.541 (638) | 0.500 | flat +0.009 (noise 0.012) |
| colour_confident | 0.553 (47) | 0.553 (704) [0.516, 0.576] | 0.586 (4252) [0.575, 0.597] | 0.591 (5944) [0.580, 0.602] | 0.591 (5944) [0.580, 0.602] | 0.516 (153) | 0.500 | flat -0.024 (noise 0.025) |
| colour_next | 0.548 (1439) | 0.532 (10008) [0.522, 0.544] | 0.531 (42872) [0.527, 0.535] | 0.517 (105741) [0.514, 0.521] | 0.530 (61392) [0.526, 0.533] | 0.534 (1194) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.499 (20146) | 0.502 (140112) [0.499, 0.504] | 0.501 (600208) [0.500, 0.502] | 0.501 (1480374) [0.500, 0.502] | 0.501 (859488) [0.500, 0.502] | 0.505 (16716) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.667 (3) | 0.610 (159) [0.508, 0.642] | 0.616 (1097) [0.601, 0.632] | 0.628 (1542) [0.611, 0.645] | 0.628 (1542) [0.611, 0.645] | 0.581 (43) | 0.500 | flat -0.005 (noise 0.050) |
| reversal_k13_next | 0.468 (47) | 0.348 (477) [0.320, 0.382] | 0.333 (1830) [0.318, 0.349] | 0.316 (4859) [0.306, 0.326] | 0.329 (2754) [0.317, 0.340] | 0.280 (50) | 0.077 | flat +0.004 (noise 0.033) |
| reversal_k13_now | 0.750 (48) | 0.594 (347) [0.552, 0.644] | 0.567 (1647) [0.546, 0.588] | 0.575 (3806) [0.562, 0.588] | 0.571 (2334) [0.553, 0.589] | 0.622 (37) | 0.077 | flat +0.028 (noise 0.037) |
| reversal_k3_next | 0.778 (27) | 0.630 (330) [0.591, 0.677] | 0.599 (2610) [0.586, 0.612] | 0.590 (6229) [0.581, 0.598] | 0.591 (3789) [0.580, 0.602] | 0.600 (30) | 0.293 | flat +0.010 (noise 0.034) |
| reversal_k3_now | 0.947 (57) | 0.927 (410) [0.916, 0.938] | 0.931 (1753) [0.921, 0.942] | 0.935 (4259) [0.929, 0.941] | 0.930 (2496) [0.923, 0.938] | 0.914 (35) | 0.293 | flat +0.018 (noise 0.019) |
| reversal_k5_next | 0.679 (53) | 0.524 (439) [0.480, 0.576] | 0.491 (2548) [0.474, 0.509] | 0.487 (5659) [0.476, 0.499] | 0.483 (3669) [0.469, 0.498] | 0.440 (50) | 0.186 | flat -0.004 (noise 0.035) |
| reversal_k5_now | 0.769 (65) | 0.735 (426) [0.698, 0.771] | 0.801 (1702) [0.784, 0.816] | 0.818 (3996) [0.808, 0.829] | 0.805 (2385) [0.792, 0.818] | 0.775 (49) | 0.187 | down -0.086 (noise 0.029) |
| reversal_k8_next | 0.571 (56) | 0.433 (471) [0.395, 0.477] | 0.402 (2558) [0.386, 0.420] | 0.398 (5749) [0.388, 0.409] | 0.399 (3643) [0.387, 0.412] | 0.345 (58) | 0.121 | flat -0.010 (noise 0.034) |
| reversal_k8_now | 0.826 (46) | 0.676 (367) [0.635, 0.724] | 0.685 (1548) [0.664, 0.705] | 0.699 (3848) [0.687, 0.712] | 0.689 (2261) [0.672, 0.705] | 0.578 (45) | 0.122 | flat -0.020 (noise 0.034) |
| overall | 0.506 (22080) | 0.506 (154058) [0.503, 0.508] | 0.505 (662155) [0.504, 0.506] | 0.504 (1631617) [0.503, 0.505] | 0.505 (948336) [0.504, 0.506] | 0.507 (18343) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06471, 0.09561] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5286, 'levels': [{'threshold': 0.06471, 'calls_per_day': 134.5, 'win_rate': 0.5466}, {'threshold': 0.09561, 'calls_per_day': 30.1, 'win_rate': 0.5735}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42871, 'rate': 0.5313}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15279 | 0.347 | 0.533 (15042) | 0.564 (2307) | 0.740 (2543) |
| volatility: normal | 15279 | 0.372 | 0.529 (15219) | 0.618 (1318) | 0.747 (2347) |
| volatility: wild | 15279 | 0.388 | 0.528 (15241) | 0.583 (864) | 0.760 (2120) |
| session: Asia 00-08 | 15360 | 0.368 | 0.533 (15239) | 0.581 (1601) | 0.747 (2300) |
| session: Europe 08-13 | 9600 | 0.362 | 0.531 (9519) | 0.590 (1132) | 0.749 (1570) |
| session: US 13-21 | 15297 | 0.376 | 0.532 (15198) | 0.600 (1215) | 0.752 (2340) |
| session: late 21-24 | 5580 | 0.363 | 0.516 (5546) | 0.542 (541) | 0.740 (800) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.384 | 0.361 | 0.260 | 0.260 | 0.525 | 0.282 | 0.486 | 1.185 |
| 6h | 360 | 0.386 | 0.359 | 0.296 | 0.327 | 0.561 | 0.275 | 0.497 | 1.438 |
| 24h | 1440 | 0.390 | 0.380 | 0.294 | 0.327 | 0.537 | 0.278 | 0.503 | 1.175 |
| 7d | 10080 | 0.383 | 0.378 | 0.296 | 0.327 | 0.528 | 0.271 | 0.495 | 1.168 |
| 30d | 43200 | 0.369 | 0.362 | 0.279 | 0.310 | 0.531 | 0.266 | 0.471 | 1.246 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.384 / 0.525 / 0.850; 2: 0.350 / 0.576 / 0.883; 3: 0.379 / 0.458 / 0.867; 4: 0.378 / 0.458 / 0.967; 5: 0.345 / 0.576 / 0.933; 6: 0.370 / 0.458 / 0.967; 7: 0.332 / 0.492 / 0.950; 8: 0.377 / 0.441 / 0.950; 9: 0.343 / 0.559 / 0.883; 10: 0.373 / 0.458 / 0.850; 11: 0.363 / 0.542 / 0.883; 12: 0.349 / 0.475 / 0.917; 13: 0.364 / 0.424 / 0.933; 14: 0.355 / 0.559 / 0.917; 15: 0.350 / 0.475 / 0.933
- 6h: 1: 0.386 / 0.561 / 0.908; 2: 0.364 / 0.494 / 0.892; 3: 0.369 / 0.511 / 0.867; 4: 0.365 / 0.500 / 0.931; 5: 0.368 / 0.517 / 0.914; 6: 0.372 / 0.514 / 0.922; 7: 0.360 / 0.506 / 0.903; 8: 0.368 / 0.517 / 0.917; 9: 0.365 / 0.522 / 0.892; 10: 0.371 / 0.525 / 0.903; 11: 0.364 / 0.503 / 0.911; 12: 0.371 / 0.536 / 0.925; 13: 0.370 / 0.494 / 0.936; 14: 0.366 / 0.506 / 0.931; 15: 0.363 / 0.500 / 0.931
- 24h: 1: 0.390 / 0.537 / 0.911; 2: 0.371 / 0.495 / 0.897; 3: 0.379 / 0.516 / 0.896; 4: 0.371 / 0.494 / 0.903; 5: 0.376 / 0.509 / 0.897; 6: 0.374 / 0.507 / 0.899; 7: 0.367 / 0.497 / 0.900; 8: 0.370 / 0.506 / 0.903; 9: 0.367 / 0.495 / 0.900; 10: 0.374 / 0.523 / 0.902; 11: 0.372 / 0.500 / 0.906; 12: 0.369 / 0.507 / 0.907; 13: 0.368 / 0.502 / 0.912; 14: 0.369 / 0.500 / 0.910; 15: 0.368 / 0.507 / 0.908
- 7d: 1: 0.383 / 0.528 / 0.902; 2: 0.368 / 0.488 / 0.900; 3: 0.376 / 0.516 / 0.901; 4: 0.367 / 0.491 / 0.901; 5: 0.370 / 0.500 / 0.901; 6: 0.367 / 0.496 / 0.901; 7: 0.369 / 0.501 / 0.901; 8: 0.370 / 0.509 / 0.901; 9: 0.366 / 0.496 / 0.901; 10: 0.368 / 0.504 / 0.901; 11: 0.370 / 0.515 / 0.900; 12: 0.365 / 0.499 / 0.901; 13: 0.367 / 0.504 / 0.901; 14: 0.365 / 0.501 / 0.901; 15: 0.366 / 0.498 / 0.901
- 30d: 1: 0.369 / 0.531 / 0.897; 2: 0.355 / 0.492 / 0.900; 3: 0.359 / 0.512 / 0.900; 4: 0.354 / 0.496 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.353 / 0.500 / 0.900; 7: 0.354 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.501 / 0.900; 10: 0.353 / 0.504 / 0.900; 11: 0.352 / 0.504 / 0.900; 12: 0.352 / 0.503 / 0.901; 13: 0.351 / 0.500 / 0.901; 14: 0.352 / 0.501 / 0.901; 15: 0.351 / 0.501 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.145 (body 0.100, range 0.189); 'price stays where it was' would score 0.200; colour right 0.475; typical miss of the close 10.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.079, range 0.180); 'price stays where it was' would score 0.158; colour right 0.469; typical miss of the close 17.2 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.122 (body 0.078, range 0.167); 'price stays where it was' would score 0.135; colour right 0.495; typical miss of the close 21.1 bp; chain ended on the right side 0.417 of 96 chains; n=1440
- 7d: match 0.126 (body 0.083, range 0.168); 'price stays where it was' would score 0.128; colour right 0.502; typical miss of the close 13.5 bp; chain ended on the right side 0.511 of 671 chains; n=10080
- 30d: match 0.126 (body 0.086, range 0.167); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.2 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.204 / 5.6; 3: 0.169 / 7.3; 4: 0.134 / 7.5; 5: 0.127 / 8.2; 6: 0.119 / 9.1; 7: 0.111 / 9.4; 8: 0.098 / 10.4; 9: 0.092 / 10.6; 10: 0.091 / 10.9; 11: 0.088 / 11.0; 12: 0.079 / 11.5; 13: 0.074 / 12.0; 14: 0.070 / 12.5; 15: 0.068 / 12.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 150711, probability skill vs chance 0.2298, widened contest next: False
  - now: threshold 0.8374, hit rate recent 0.9225 / long run 0.926
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.298, naive rule 0.511, lift 3.13x
    - 24h: 44 calls (44 a day), hit rate 0.909, chance 0.299, naive rule 0.520, lift 3.04x
    - 7d: 395 calls (56 a day), hit rate 0.922, chance 0.288, naive rule 0.499, lift 3.20x
    - 30d: 1739 calls (58 a day), hit rate 0.929, chance 0.294, naive rule 0.499, lift 3.16x
  - next: threshold 0.5628, hit rate recent 0.6661 / long run 0.6189
    - 6h: 11 calls (44 a day), hit rate 0.818, chance 0.298, lift 2.75x
    - 24h: 35 calls (35 a day), hit rate 0.600, chance 0.299, lift 2.01x
    - 7d: 302 calls (43 a day), hit rate 0.632, chance 0.288, lift 2.19x
    - 30d: 2520 calls (84 a day), hit rate 0.601, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.501; 0.35: 532, 0.526; 0.40: 474, 0.580; 0.45: 406, 0.650; 0.50: 357, 0.695; 0.55: 310, 0.739; 0.60: 260, 0.784; 0.65: 219, 0.812; 0.70: 171, 0.843; 0.75: 138, 0.874; 0.80: 91, 0.904; 0.85: 46, 0.940; 0.90: 4, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.432; 0.35: 496, 0.466; 0.40: 394, 0.505; 0.45: 295, 0.540; 0.50: 188, 0.572; 0.55: 82, 0.587; 0.60: 11, 0.657; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 150709, probability skill vs chance 0.2283, widened contest next: False
  - now: threshold 0.6942, hit rate recent 0.7788 / long run 0.7778
    - 6h: 17 calls (69 a day), hit rate 0.941, chance 0.212, naive rule 0.471, lift 4.44x
    - 24h: 59 calls (59 a day), hit rate 0.763, chance 0.194, naive rule 0.436, lift 3.93x
    - 7d: 430 calls (61 a day), hit rate 0.737, chance 0.183, naive rule 0.407, lift 4.03x
    - 30d: 1695 calls (57 a day), hit rate 0.798, chance 0.187, naive rule 0.409, lift 4.27x
  - next: threshold 0.4521, hit rate recent 0.5316 / long run 0.5146
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.212, lift 3.27x
    - 24h: 59 calls (59 a day), hit rate 0.475, chance 0.194, lift 2.45x
    - 7d: 420 calls (60 a day), hit rate 0.512, chance 0.183, lift 2.80x
    - 30d: 2494 calls (83 a day), hit rate 0.494, chance 0.187, lift 2.65x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.422; 0.35: 356, 0.479; 0.40: 288, 0.548; 0.45: 234, 0.606; 0.50: 186, 0.653; 0.55: 148, 0.691; 0.60: 112, 0.739; 0.65: 76, 0.777; 0.70: 48, 0.809; 0.75: 28, 0.844; 0.80: 9, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.386; 0.35: 254, 0.428; 0.40: 160, 0.460; 0.45: 64, 0.507; 0.50: 9, 0.553; 0.55: 1, 0.433
- **K=8**: model 1794614400, labels learned 150706, probability skill vs chance 0.218, widened contest next: False
  - now: threshold 0.5669, hit rate recent 0.6656 / long run 0.681
    - 6h: 17 calls (70 a day), hit rate 0.765, chance 0.137, naive rule 0.398, lift 5.59x
    - 24h: 53 calls (53 a day), hit rate 0.623, chance 0.124, naive rule 0.370, lift 5.02x
    - 7d: 366 calls (52 a day), hit rate 0.667, chance 0.123, naive rule 0.354, lift 5.41x
    - 30d: 1541 calls (51 a day), hit rate 0.683, chance 0.121, naive rule 0.340, lift 5.63x
  - next: threshold 0.3691, hit rate recent 0.414 / long run 0.4244
    - 6h: 19 calls (78 a day), hit rate 0.474, chance 0.137, lift 3.46x
    - 24h: 68 calls (68 a day), hit rate 0.382, chance 0.124, lift 3.08x
    - 7d: 453 calls (65 a day), hit rate 0.437, chance 0.123, lift 3.55x
    - 30d: 2509 calls (84 a day), hit rate 0.405, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.429; 0.35: 194, 0.491; 0.40: 153, 0.535; 0.45: 117, 0.581; 0.50: 83, 0.640; 0.55: 59, 0.673; 0.60: 40, 0.712; 0.65: 23, 0.770; 0.70: 11, 0.813; 0.75: 2, 0.769
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 166, 0.370; 0.35: 84, 0.398; 0.40: 24, 0.431; 0.45: 4, 0.449; 0.50: 1, 0.783
- **K=13**: model 1794700800, labels learned 150701, probability skill vs chance 0.2009, widened contest next: False
  - now: threshold 0.4439, hit rate recent 0.6501 / long run 0.5846
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.087, naive rule 0.372, lift 8.24x
    - 24h: 47 calls (47 a day), hit rate 0.638, chance 0.080, naive rule 0.325, lift 7.98x
    - 7d: 335 calls (48 a day), hit rate 0.597, chance 0.081, naive rule 0.312, lift 7.41x
    - 30d: 1618 calls (54 a day), hit rate 0.570, chance 0.078, naive rule 0.289, lift 7.30x
  - next: threshold 0.2987, hit rate recent 0.3328 / long run 0.3375
    - 6h: 13 calls (54 a day), hit rate 0.385, chance 0.087, lift 4.44x
    - 24h: 60 calls (61 a day), hit rate 0.283, chance 0.080, lift 3.54x
    - 7d: 441 calls (63 a day), hit rate 0.351, chance 0.081, lift 4.36x
    - 30d: 1822 calls (61 a day), hit rate 0.333, chance 0.078, lift 4.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.433; 0.35: 97, 0.481; 0.40: 67, 0.541; 0.45: 46, 0.591; 0.50: 32, 0.636; 0.55: 20, 0.659; 0.60: 11, 0.699; 0.65: 3, 0.642; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.342; 0.35: 13, 0.345; 0.40: 2, 0.425; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 17.570 | 11.23% | 0.883 | 0.500 | 0.251 | 0.475 | 0.235 |
| 6h | 25.226 | 4.48% | 0.903 | 0.514 | 0.251 | 0.478 | 0.430 |
| 24h | 34.293 | 5.58% | 0.905 | 0.501 | 0.250 | 0.509 | 0.655 |
| 7d | 23.248 | 5.53% | 0.902 | 0.500 | 0.250 | 0.512 | 0.653 |
| 30d | 16.752 | 4.86% | 0.900 | 0.500 | 0.250 | 0.505 | 0.715 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.792 | 17.698 | 17.778 | 17.726 | 17.779 | 17.837 | 17.465 | 17.420 | 17.552 | 17.570 |
| 6h | 26.410 | 25.506 | 25.458 | 25.134 | 26.091 | 25.622 | 25.192 | 25.110 | 25.162 | 25.226 |
| 24h | 36.322 | 34.585 | 34.537 | 34.255 | 35.169 | 34.787 | 34.317 | 34.244 | 34.241 | 34.293 |
| 7d | 24.609 | 23.468 | 23.438 | 23.382 | 23.762 | 23.605 | 23.227 | 23.191 | 23.212 | 23.248 |
| 30d | 17.607 | 16.916 | 16.875 | 16.810 | 17.088 | 17.036 | 16.736 | 16.715 | 16.723 | 16.752 |

## Next candle

- candle starting 2026-11-15 19:57 UTC, last close 1824.38
- P(up) 0.4982, return quantiles (bp): {'05': -8.755, '10': -6.519, '25': -3.398, '40': -1.257, '50': -0.005, '60': 1.003, '75': 3.251, '90': 6.855, '95': 9.151}
- changepoint probability 0.0322, regime age 125.5 min
- agent weights: empirical 0.003, ewma 0.076, garch 0.083, har 0.240, bocpd 0.012, hmm 0.052, online_qr 0.252, lgbm 0.283

## Learning log

- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- HMM volatility states (sd, bp per minute): [5.18, 9.59, 24.41], current probabilities: [0.942, 0.056, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-11-15 20:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.254, 'l_abs': 0.77, 'l_hi': 0.794, 'l_lo': 0.736, 'b05': 0.763, 'b25': 0.776, 'b75': 0.705, 'b95': 0.762}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.499, 1.914, 1.887, 2.337, 2.464, 2.512, 2.637, 2.859, 2.844, 2.93, 2.946, 2.952, 3.132, 3.314]}
- calibration offsets (in sigma): {'05': 0.118, '10': 0.076, '25': 0.05, '40': 0.024, '50': 0.02, '60': -0.024, '75': -0.03, '90': -0.006, '95': -0.048}
