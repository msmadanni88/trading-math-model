# ETH-USD 60s candle generator - report

- generated: 2026-11-15 00:23 UTC
- last closed candle: 2026-11-15 00:23 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_now 0.735 in the last 7 days, -0.086 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.533 (671) [0.500, 0.566] | 0.523 (2879) [0.507, 0.541] | 0.515 (7097) [0.504, 0.527] | 0.517 (4125) [0.501, 0.533] | 0.000 (1) | 0.500 | flat +0.044 (noise 0.028) |
| colour_clear | 0.560 (801) | 0.542 (5598) [0.532, 0.552] | 0.543 (23921) [0.537, 0.549] | 0.523 (58193) [0.518, 0.529] | 0.543 (33955) [0.538, 0.547] | 0.462 (13) | 0.500 | flat +0.009 (noise 0.012) |
| colour_confident | 0.553 (47) | 0.553 (704) [0.516, 0.576] | 0.586 (4252) [0.575, 0.597] | 0.591 (5944) [0.580, 0.602] | 0.591 (5944) [0.580, 0.602] | 1.000 (1) | 0.500 | flat -0.024 (noise 0.025) |
| colour_next | 0.548 (1439) | 0.532 (10008) [0.522, 0.544] | 0.531 (42872) [0.527, 0.535] | 0.517 (105741) [0.514, 0.521] | 0.530 (61392) [0.526, 0.533] | 0.565 (23) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.499 (20146) | 0.502 (140112) [0.499, 0.504] | 0.501 (600208) [0.500, 0.502] | 0.501 (1480374) [0.500, 0.502] | 0.501 (859488) [0.500, 0.502] | 0.484 (322) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.667 (3) | 0.610 (159) [0.508, 0.642] | 0.616 (1097) [0.601, 0.632] | 0.628 (1542) [0.611, 0.645] | 0.628 (1542) [0.611, 0.645] | - | 0.500 | flat -0.005 (noise 0.050) |
| reversal_k13_next | 0.468 (47) | 0.348 (477) [0.320, 0.382] | 0.333 (1830) [0.318, 0.349] | 0.316 (4859) [0.306, 0.326] | 0.329 (2754) [0.317, 0.340] | - | 0.077 | flat +0.004 (noise 0.033) |
| reversal_k13_now | 0.750 (48) | 0.594 (347) [0.552, 0.644] | 0.567 (1647) [0.546, 0.588] | 0.575 (3806) [0.562, 0.588] | 0.571 (2334) [0.553, 0.589] | - | 0.077 | flat +0.028 (noise 0.037) |
| reversal_k3_next | 0.778 (27) | 0.630 (330) [0.591, 0.677] | 0.599 (2610) [0.586, 0.612] | 0.590 (6229) [0.581, 0.598] | 0.591 (3789) [0.580, 0.602] | - | 0.293 | flat +0.010 (noise 0.034) |
| reversal_k3_now | 0.947 (57) | 0.927 (410) [0.916, 0.938] | 0.931 (1753) [0.921, 0.942] | 0.935 (4259) [0.929, 0.941] | 0.930 (2496) [0.923, 0.938] | - | 0.293 | flat +0.018 (noise 0.019) |
| reversal_k5_next | 0.679 (53) | 0.524 (439) [0.480, 0.576] | 0.491 (2548) [0.474, 0.509] | 0.487 (5659) [0.476, 0.499] | 0.483 (3669) [0.469, 0.498] | - | 0.186 | flat -0.004 (noise 0.035) |
| reversal_k5_now | 0.769 (65) | 0.735 (426) [0.698, 0.771] | 0.801 (1702) [0.784, 0.816] | 0.818 (3996) [0.808, 0.829] | 0.805 (2385) [0.792, 0.818] | 1.000 (1) | 0.187 | down -0.086 (noise 0.029) |
| reversal_k8_next | 0.571 (56) | 0.433 (471) [0.395, 0.477] | 0.402 (2558) [0.386, 0.420] | 0.398 (5749) [0.388, 0.409] | 0.399 (3643) [0.387, 0.412] | - | 0.121 | flat -0.010 (noise 0.034) |
| reversal_k8_now | 0.826 (46) | 0.676 (367) [0.635, 0.724] | 0.685 (1548) [0.664, 0.705] | 0.699 (3848) [0.687, 0.712] | 0.689 (2261) [0.672, 0.705] | 1.000 (1) | 0.122 | flat -0.020 (noise 0.034) |
| overall | 0.506 (22080) | 0.506 (154058) [0.503, 0.508] | 0.505 (662155) [0.504, 0.506] | 0.504 (1631617) [0.503, 0.505] | 0.505 (948336) [0.504, 0.506] | 0.491 (348) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0692, 0.1049] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5327, 'levels': [{'threshold': 0.0692, 'calls_per_day': 135.9, 'win_rate': 0.5668}, {'threshold': 0.1049, 'calls_per_day': 32.6, 'win_rate': 0.5826}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42871, 'rate': 0.5308}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14888 | 0.346 | 0.534 (14652) | 0.565 (2271) | 0.742 (2495) |
| volatility: normal | 14887 | 0.371 | 0.527 (14826) | 0.614 (1290) | 0.744 (2288) |
| volatility: wild | 14888 | 0.388 | 0.530 (14853) | 0.602 (776) | 0.763 (2063) |
| session: Asia 00-08 | 14903 | 0.368 | 0.534 (14782) | 0.589 (1515) | 0.751 (2242) |
| session: Europe 08-13 | 9300 | 0.362 | 0.531 (9220) | 0.591 (1111) | 0.751 (1536) |
| session: US 13-21 | 14880 | 0.376 | 0.531 (14783) | 0.598 (1170) | 0.749 (2268) |
| session: late 21-24 | 5580 | 0.363 | 0.516 (5546) | 0.542 (541) | 0.740 (800) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.390 | 0.366 | 0.326 | 0.326 | 0.550 | 0.275 | 0.506 | 1.454 |
| 6h | 360 | 0.414 | 0.406 | 0.312 | 0.347 | 0.564 | 0.297 | 0.531 | 1.232 |
| 24h | 1440 | 0.396 | 0.385 | 0.299 | 0.322 | 0.548 | 0.282 | 0.511 | 1.270 |
| 7d | 10080 | 0.377 | 0.371 | 0.290 | 0.319 | 0.532 | 0.271 | 0.482 | 1.202 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.531 | 0.265 | 0.471 | 1.249 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.390 / 0.550 / 0.917; 2: 0.347 / 0.383 / 0.900; 3: 0.386 / 0.567 / 0.917; 4: 0.343 / 0.367 / 0.900; 5: 0.375 / 0.633 / 0.867; 6: 0.373 / 0.567 / 0.900; 7: 0.364 / 0.433 / 0.883; 8: 0.371 / 0.583 / 0.867; 9: 0.332 / 0.350 / 0.850; 10: 0.383 / 0.617 / 0.833; 11: 0.337 / 0.400 / 0.817; 12: 0.369 / 0.567 / 0.800; 13: 0.339 / 0.450 / 0.783; 14: 0.332 / 0.433 / 0.767; 15: 0.348 / 0.533 / 0.783
- 6h: 1: 0.414 / 0.564 / 0.914; 2: 0.374 / 0.439 / 0.900; 3: 0.399 / 0.525 / 0.903; 4: 0.382 / 0.475 / 0.903; 5: 0.394 / 0.525 / 0.872; 6: 0.379 / 0.483 / 0.881; 7: 0.380 / 0.483 / 0.889; 8: 0.375 / 0.497 / 0.889; 9: 0.375 / 0.472 / 0.886; 10: 0.382 / 0.528 / 0.872; 11: 0.382 / 0.517 / 0.900; 12: 0.375 / 0.503 / 0.903; 13: 0.386 / 0.514 / 0.914; 14: 0.371 / 0.486 / 0.906; 15: 0.377 / 0.503 / 0.908
- 24h: 1: 0.396 / 0.548 / 0.906; 2: 0.369 / 0.466 / 0.898; 3: 0.386 / 0.523 / 0.902; 4: 0.371 / 0.473 / 0.897; 5: 0.377 / 0.504 / 0.896; 6: 0.372 / 0.488 / 0.897; 7: 0.376 / 0.509 / 0.899; 8: 0.376 / 0.513 / 0.900; 9: 0.365 / 0.477 / 0.897; 10: 0.378 / 0.525 / 0.897; 11: 0.371 / 0.502 / 0.897; 12: 0.371 / 0.503 / 0.903; 13: 0.371 / 0.503 / 0.902; 14: 0.370 / 0.500 / 0.905; 15: 0.366 / 0.494 / 0.903
- 7d: 1: 0.377 / 0.532 / 0.898; 2: 0.361 / 0.487 / 0.900; 3: 0.369 / 0.518 / 0.900; 4: 0.360 / 0.491 / 0.900; 5: 0.362 / 0.501 / 0.899; 6: 0.359 / 0.492 / 0.899; 7: 0.362 / 0.501 / 0.899; 8: 0.364 / 0.509 / 0.899; 9: 0.360 / 0.498 / 0.899; 10: 0.361 / 0.503 / 0.899; 11: 0.364 / 0.518 / 0.899; 12: 0.359 / 0.501 / 0.899; 13: 0.360 / 0.504 / 0.899; 14: 0.359 / 0.505 / 0.898; 15: 0.358 / 0.496 / 0.899
- 30d: 1: 0.368 / 0.531 / 0.897; 2: 0.355 / 0.492 / 0.900; 3: 0.359 / 0.511 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.353 / 0.499 / 0.900; 7: 0.354 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.502 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.352 / 0.499 / 0.900; 14: 0.351 / 0.501 / 0.900; 15: 0.351 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.135 (body 0.103, range 0.167); 'price stays where it was' would score 0.156; colour right 0.567; typical miss of the close 28.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.131 (body 0.089, range 0.172); 'price stays where it was' would score 0.153; colour right 0.519; typical miss of the close 28.3 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.138 (body 0.094, range 0.182); 'price stays where it was' would score 0.134; colour right 0.509; typical miss of the close 16.2 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.124 (body 0.083, range 0.166); 'price stays where it was' would score 0.125; colour right 0.504; typical miss of the close 11.2 bp; chain ended on the right side 0.532 of 671 chains; n=10080
- 30d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.1 bp; chain ended on the right side 0.523 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 4.7; 2: 0.205 / 5.6; 3: 0.168 / 7.3; 4: 0.134 / 7.5; 5: 0.126 / 8.2; 6: 0.118 / 9.0; 7: 0.110 / 9.3; 8: 0.097 / 10.2; 9: 0.091 / 10.6; 10: 0.091 / 10.8; 11: 0.088 / 10.9; 12: 0.079 / 11.3; 13: 0.074 / 11.9; 14: 0.070 / 12.3; 15: 0.067 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 149537, probability skill vs chance 0.235, widened contest next: False
  - now: threshold 0.8393, hit rate recent 0.9297 / long run 0.9267
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.262, naive rule 0.495, lift 3.39x
    - 24h: 56 calls (56 a day), hit rate 0.946, chance 0.288, naive rule 0.526, lift 3.28x
    - 7d: 409 calls (58 a day), hit rate 0.927, chance 0.287, naive rule 0.495, lift 3.23x
    - 30d: 1750 calls (58 a day), hit rate 0.931, chance 0.293, naive rule 0.497, lift 3.17x
  - next: threshold 0.5657, hit rate recent 0.7008 / long run 0.6198
    - 6h: 5 calls (20 a day), hit rate 0.600, chance 0.262, lift 2.29x
    - 24h: 27 calls (27 a day), hit rate 0.778, chance 0.288, lift 2.70x
    - 7d: 330 calls (47 a day), hit rate 0.630, chance 0.287, lift 2.20x
    - 30d: 2607 calls (87 a day), hit rate 0.599, chance 0.293, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.579; 0.45: 406, 0.648; 0.50: 357, 0.693; 0.55: 310, 0.738; 0.60: 260, 0.783; 0.65: 220, 0.812; 0.70: 172, 0.844; 0.75: 138, 0.874; 0.80: 91, 0.906; 0.85: 46, 0.942; 0.90: 5, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.432; 0.35: 496, 0.465; 0.40: 395, 0.504; 0.45: 296, 0.539; 0.50: 189, 0.572; 0.55: 83, 0.585; 0.60: 11, 0.663; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 149535, probability skill vs chance 0.232, widened contest next: False
  - now: threshold 0.694, hit rate recent 0.7593 / long run 0.7782
    - 6h: 15 calls (61 a day), hit rate 0.733, chance 0.178, naive rule 0.425, lift 4.11x
    - 24h: 65 calls (65 a day), hit rate 0.769, chance 0.179, naive rule 0.436, lift 4.29x
    - 7d: 426 calls (61 a day), hit rate 0.735, chance 0.182, naive rule 0.404, lift 4.03x
    - 30d: 1700 calls (57 a day), hit rate 0.801, chance 0.186, naive rule 0.407, lift 4.31x
  - next: threshold 0.4535, hit rate recent 0.6042 / long run 0.5207
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.178, lift 3.06x
    - 24h: 52 calls (52 a day), hit rate 0.673, chance 0.179, lift 3.75x
    - 7d: 439 calls (63 a day), hit rate 0.524, chance 0.182, lift 2.88x
    - 30d: 2547 calls (85 a day), hit rate 0.491, chance 0.186, lift 2.64x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 356, 0.477; 0.40: 288, 0.547; 0.45: 234, 0.604; 0.50: 187, 0.651; 0.55: 149, 0.689; 0.60: 112, 0.738; 0.65: 77, 0.777; 0.70: 48, 0.811; 0.75: 28, 0.842; 0.80: 9, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.385; 0.35: 255, 0.426; 0.40: 161, 0.459; 0.45: 65, 0.504; 0.50: 10, 0.539; 0.55: 1, 0.441
- **K=8**: model 1794614400, labels learned 149532, probability skill vs chance 0.2292, widened contest next: False
  - now: threshold 0.5692, hit rate recent 0.7381 / long run 0.6893
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.133, naive rule 0.398, lift 6.84x
    - 24h: 47 calls (47 a day), hit rate 0.830, chance 0.128, naive rule 0.403, lift 6.48x
    - 7d: 368 calls (53 a day), hit rate 0.677, chance 0.123, naive rule 0.347, lift 5.52x
    - 30d: 1547 calls (52 a day), hit rate 0.686, chance 0.121, naive rule 0.338, lift 5.67x
  - next: threshold 0.3727, hit rate recent 0.5006 / long run 0.4323
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.133, lift 3.23x
    - 24h: 56 calls (56 a day), hit rate 0.571, chance 0.128, lift 4.47x
    - 7d: 470 calls (67 a day), hit rate 0.432, chance 0.123, lift 3.52x
    - 30d: 2556 calls (85 a day), hit rate 0.402, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.428; 0.35: 194, 0.491; 0.40: 153, 0.534; 0.45: 118, 0.580; 0.50: 84, 0.640; 0.55: 59, 0.674; 0.60: 40, 0.713; 0.65: 23, 0.773; 0.70: 11, 0.816; 0.75: 2, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 167, 0.368; 0.35: 85, 0.395; 0.40: 24, 0.431; 0.45: 5, 0.436; 0.50: 1, 0.792
- **K=13**: model 1794700800, labels learned 149527, probability skill vs chance 0.2115, widened contest next: False
  - now: threshold 0.4457, hit rate recent 0.6578 / long run 0.5821
    - 6h: 12 calls (50 a day), hit rate 0.750, chance 0.087, naive rule 0.362, lift 8.62x
    - 24h: 48 calls (49 a day), hit rate 0.750, chance 0.086, naive rule 0.372, lift 8.69x
    - 7d: 347 calls (50 a day), hit rate 0.594, chance 0.081, naive rule 0.306, lift 7.37x
    - 30d: 1645 calls (55 a day), hit rate 0.567, chance 0.078, naive rule 0.286, lift 7.27x
  - next: threshold 0.2989, hit rate recent 0.3772 / long run 0.3424
    - 6h: 13 calls (54 a day), hit rate 0.231, chance 0.087, lift 2.65x
    - 24h: 47 calls (47 a day), hit rate 0.468, chance 0.086, lift 5.42x
    - 7d: 476 calls (68 a day), hit rate 0.349, chance 0.081, lift 4.33x
    - 30d: 1830 calls (61 a day), hit rate 0.333, chance 0.078, lift 4.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 135, 0.432; 0.35: 97, 0.479; 0.40: 68, 0.540; 0.45: 47, 0.589; 0.50: 32, 0.639; 0.55: 21, 0.661; 0.60: 11, 0.703; 0.65: 3, 0.653; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.342; 0.35: 13, 0.342; 0.40: 3, 0.416; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 39.402 | -1.24% | 0.900 | 0.533 | 0.253 | 0.500 | 0.159 |
| 6h | 44.771 | 7.07% | 0.903 | 0.503 | 0.250 | 0.544 | 0.580 |
| 24h | 31.185 | 6.02% | 0.907 | 0.506 | 0.250 | 0.513 | 0.674 |
| 7d | 20.417 | 5.58% | 0.901 | 0.500 | 0.250 | 0.513 | 0.677 |
| 30d | 16.409 | 4.86% | 0.900 | 0.500 | 0.250 | 0.504 | 0.710 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 38.919 | 39.528 | 39.477 | 38.715 | 40.686 | 39.556 | 39.085 | 39.527 | 39.040 | 39.402 |
| 6h | 48.179 | 45.143 | 45.358 | 44.775 | 46.327 | 45.887 | 44.828 | 44.867 | 44.744 | 44.771 |
| 24h | 33.184 | 31.451 | 31.525 | 31.278 | 32.141 | 31.665 | 31.185 | 31.177 | 31.162 | 31.185 |
| 7d | 21.624 | 20.613 | 20.594 | 20.559 | 20.880 | 20.775 | 20.395 | 20.369 | 20.386 | 20.417 |
| 30d | 17.247 | 16.573 | 16.530 | 16.468 | 16.737 | 16.688 | 16.393 | 16.374 | 16.381 | 16.409 |

## Next candle

- candle starting 2026-11-15 00:23 UTC, last close 1762.08
- P(up) 0.4773, return quantiles (bp): {'05': -23.492, '10': -17.586, '25': -8.377, '40': -4.605, '50': -0.771, '60': 2.692, '75': 7.555, '90': 15.124, '95': 20.856}
- changepoint probability 0.0553, regime age 77.0 min
- agent weights: empirical 0.003, ewma 0.079, garch 0.035, har 0.263, bocpd 0.004, hmm 0.015, online_qr 0.321, lgbm 0.282

## Learning log

- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- HMM volatility states (sd, bp per minute): [5.05, 9.08, 23.18], current probabilities: [0.018, 0.409, 0.573]
- live generator: {'versions': 60, 'latest_effective': '2026-11-15 00:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.294, 'l_abs': 0.719, 'l_hi': 0.777, 'l_lo': 0.727, 'b05': 0.753, 'b25': 0.749, 'b75': 0.617, 'b95': 0.73}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.6], [1.3, 1.6], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.6], [1.4, 1.6], [1.3, 1.8], [1.3, 1.6]], 'cone_width': [1.511, 1.781, 2.145, 2.603, 2.691, 2.912, 3.12, 3.382, 3.87, 3.987, 4.172, 4.529, 4.804, 4.788]}
- calibration offsets (in sigma): {'05': 0.021, '10': -0.008, '25': -0.005, '40': -0.102, '50': -0.06, '60': -0.028, '75': -0.045, '90': -0.082, '95': -0.091}
