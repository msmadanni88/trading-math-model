# ETH-USD 60s candle generator - report

- generated: 2026-11-15 06:56 UTC
- last closed candle: 2026-11-15 06:56 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_now 0.735 in the last 7 days, -0.086 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.533 (671) [0.500, 0.566] | 0.523 (2879) [0.507, 0.541] | 0.515 (7097) [0.504, 0.527] | 0.517 (4125) [0.501, 0.533] | 0.259 (27) | 0.500 | flat +0.044 (noise 0.028) |
| colour_clear | 0.560 (801) | 0.542 (5598) [0.532, 0.552] | 0.543 (23921) [0.537, 0.549] | 0.523 (58193) [0.518, 0.529] | 0.543 (33955) [0.538, 0.547] | 0.522 (226) | 0.500 | flat +0.009 (noise 0.012) |
| colour_confident | 0.553 (47) | 0.553 (704) [0.516, 0.576] | 0.586 (4252) [0.575, 0.597] | 0.591 (5944) [0.580, 0.602] | 0.591 (5944) [0.580, 0.602] | 0.456 (79) | 0.500 | flat -0.024 (noise 0.025) |
| colour_next | 0.548 (1439) | 0.532 (10008) [0.522, 0.544] | 0.531 (42872) [0.527, 0.535] | 0.517 (105741) [0.514, 0.521] | 0.530 (61392) [0.526, 0.533] | 0.517 (416) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.499 (20146) | 0.502 (140112) [0.499, 0.504] | 0.501 (600208) [0.500, 0.502] | 0.501 (1480374) [0.500, 0.502] | 0.501 (859488) [0.500, 0.502] | 0.503 (5824) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.667 (3) | 0.610 (159) [0.508, 0.642] | 0.616 (1097) [0.601, 0.632] | 0.628 (1542) [0.611, 0.645] | 0.628 (1542) [0.611, 0.645] | 0.478 (23) | 0.500 | flat -0.005 (noise 0.050) |
| reversal_k13_next | 0.468 (47) | 0.348 (477) [0.320, 0.382] | 0.333 (1830) [0.318, 0.349] | 0.316 (4859) [0.306, 0.326] | 0.329 (2754) [0.317, 0.340] | 0.167 (18) | 0.077 | flat +0.004 (noise 0.033) |
| reversal_k13_now | 0.750 (48) | 0.594 (347) [0.552, 0.644] | 0.567 (1647) [0.546, 0.588] | 0.575 (3806) [0.562, 0.588] | 0.571 (2334) [0.553, 0.589] | 0.500 (12) | 0.077 | flat +0.028 (noise 0.037) |
| reversal_k3_next | 0.778 (27) | 0.630 (330) [0.591, 0.677] | 0.599 (2610) [0.586, 0.612] | 0.590 (6229) [0.581, 0.598] | 0.591 (3789) [0.580, 0.602] | 0.400 (5) | 0.293 | flat +0.010 (noise 0.034) |
| reversal_k3_now | 0.947 (57) | 0.927 (410) [0.916, 0.938] | 0.931 (1753) [0.921, 0.942] | 0.935 (4259) [0.929, 0.941] | 0.930 (2496) [0.923, 0.938] | 0.909 (11) | 0.293 | flat +0.018 (noise 0.019) |
| reversal_k5_next | 0.679 (53) | 0.524 (439) [0.480, 0.576] | 0.491 (2548) [0.474, 0.509] | 0.487 (5659) [0.476, 0.499] | 0.483 (3669) [0.469, 0.498] | 0.250 (16) | 0.186 | flat -0.004 (noise 0.035) |
| reversal_k5_now | 0.769 (65) | 0.735 (426) [0.698, 0.771] | 0.801 (1702) [0.784, 0.816] | 0.818 (3996) [0.808, 0.829] | 0.805 (2385) [0.792, 0.818] | 0.786 (14) | 0.187 | down -0.086 (noise 0.029) |
| reversal_k8_next | 0.571 (56) | 0.433 (471) [0.395, 0.477] | 0.402 (2558) [0.386, 0.420] | 0.398 (5749) [0.388, 0.409] | 0.399 (3643) [0.387, 0.412] | 0.312 (16) | 0.121 | flat -0.010 (noise 0.034) |
| reversal_k8_now | 0.826 (46) | 0.676 (367) [0.635, 0.724] | 0.685 (1548) [0.664, 0.705] | 0.699 (3848) [0.687, 0.712] | 0.689 (2261) [0.672, 0.705] | 0.500 (12) | 0.122 | flat -0.020 (noise 0.034) |
| overall | 0.506 (22080) | 0.506 (154058) [0.503, 0.508] | 0.505 (662155) [0.504, 0.506] | 0.504 (1631617) [0.503, 0.505] | 0.505 (948336) [0.504, 0.506] | 0.502 (6371) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06818, 0.103] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5309, 'levels': [{'threshold': 0.06818, 'calls_per_day': 139.2, 'win_rate': 0.5536}, {'threshold': 0.103, 'calls_per_day': 33.3, 'win_rate': 0.5556}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42873, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15020 | 0.347 | 0.533 (14784) | 0.564 (2281) | 0.742 (2506) |
| volatility: normal | 15017 | 0.371 | 0.529 (14956) | 0.615 (1309) | 0.746 (2322) |
| volatility: wild | 15019 | 0.388 | 0.528 (14984) | 0.588 (825) | 0.759 (2065) |
| session: Asia 00-08 | 15296 | 0.368 | 0.534 (15175) | 0.583 (1593) | 0.749 (2289) |
| session: Europe 08-13 | 9300 | 0.362 | 0.531 (9220) | 0.591 (1111) | 0.751 (1536) |
| session: US 13-21 | 14880 | 0.376 | 0.531 (14783) | 0.598 (1170) | 0.749 (2268) |
| session: late 21-24 | 5580 | 0.363 | 0.516 (5546) | 0.542 (541) | 0.740 (800) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.373 | 0.423 | 0.326 | 0.326 | 0.417 | 0.254 | 0.492 | 0.915 |
| 6h | 360 | 0.378 | 0.364 | 0.292 | 0.324 | 0.503 | 0.265 | 0.491 | 1.161 |
| 24h | 1440 | 0.398 | 0.385 | 0.298 | 0.324 | 0.543 | 0.284 | 0.512 | 1.294 |
| 7d | 10080 | 0.379 | 0.374 | 0.293 | 0.323 | 0.530 | 0.271 | 0.488 | 1.181 |
| 30d | 43200 | 0.368 | 0.362 | 0.279 | 0.310 | 0.531 | 0.265 | 0.472 | 1.245 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.373 / 0.417 / 0.917; 2: 0.400 / 0.500 / 0.917; 3: 0.391 / 0.467 / 0.900; 4: 0.391 / 0.517 / 0.933; 5: 0.389 / 0.467 / 0.933; 6: 0.416 / 0.583 / 0.883; 7: 0.413 / 0.517 / 0.867; 8: 0.382 / 0.483 / 0.850; 9: 0.401 / 0.500 / 0.850; 10: 0.381 / 0.450 / 0.833; 11: 0.400 / 0.533 / 0.833; 12: 0.398 / 0.533 / 0.833; 13: 0.385 / 0.533 / 0.833; 14: 0.403 / 0.583 / 0.867; 15: 0.367 / 0.450 / 0.833
- 6h: 1: 0.378 / 0.503 / 0.917; 2: 0.368 / 0.533 / 0.906; 3: 0.365 / 0.475 / 0.900; 4: 0.365 / 0.494 / 0.919; 5: 0.374 / 0.500 / 0.944; 6: 0.371 / 0.503 / 0.928; 7: 0.370 / 0.522 / 0.919; 8: 0.361 / 0.467 / 0.911; 9: 0.369 / 0.522 / 0.906; 10: 0.363 / 0.511 / 0.911; 11: 0.372 / 0.489 / 0.906; 12: 0.369 / 0.517 / 0.903; 13: 0.349 / 0.478 / 0.908; 14: 0.368 / 0.511 / 0.928; 15: 0.361 / 0.519 / 0.922
- 24h: 1: 0.398 / 0.543 / 0.906; 2: 0.372 / 0.482 / 0.893; 3: 0.385 / 0.515 / 0.893; 4: 0.373 / 0.476 / 0.899; 5: 0.380 / 0.502 / 0.901; 6: 0.378 / 0.500 / 0.901; 7: 0.377 / 0.506 / 0.898; 8: 0.374 / 0.504 / 0.895; 9: 0.370 / 0.486 / 0.892; 10: 0.378 / 0.526 / 0.892; 11: 0.375 / 0.498 / 0.890; 12: 0.372 / 0.502 / 0.891; 13: 0.371 / 0.501 / 0.890; 14: 0.372 / 0.496 / 0.896; 15: 0.368 / 0.499 / 0.895
- 7d: 1: 0.379 / 0.530 / 0.899; 2: 0.363 / 0.488 / 0.900; 3: 0.371 / 0.517 / 0.901; 4: 0.363 / 0.489 / 0.901; 5: 0.366 / 0.502 / 0.902; 6: 0.362 / 0.493 / 0.902; 7: 0.365 / 0.502 / 0.901; 8: 0.366 / 0.508 / 0.901; 9: 0.363 / 0.499 / 0.901; 10: 0.363 / 0.503 / 0.900; 11: 0.367 / 0.517 / 0.901; 12: 0.362 / 0.501 / 0.900; 13: 0.363 / 0.503 / 0.901; 14: 0.362 / 0.504 / 0.902; 15: 0.361 / 0.498 / 0.902
- 30d: 1: 0.368 / 0.531 / 0.897; 2: 0.355 / 0.492 / 0.900; 3: 0.359 / 0.511 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.353 / 0.500 / 0.900; 7: 0.354 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.502 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.503 / 0.900; 13: 0.352 / 0.499 / 0.900; 14: 0.351 / 0.501 / 0.900; 15: 0.351 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.073 (body 0.044, range 0.102); 'price stays where it was' would score 0.049; colour right 0.517; typical miss of the close 29.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.102 (body 0.064, range 0.141); 'price stays where it was' would score 0.108; colour right 0.489; typical miss of the close 28.9 bp; chain ended on the right side 0.208 of 24 chains; n=360
- 24h: match 0.133 (body 0.090, range 0.175); 'price stays where it was' would score 0.125; colour right 0.506; typical miss of the close 20.1 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.125 (body 0.083, range 0.166); 'price stays where it was' would score 0.125; colour right 0.502; typical miss of the close 12.1 bp; chain ended on the right side 0.522 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.2 bp; chain ended on the right side 0.521 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 4.7; 2: 0.204 / 5.6; 3: 0.169 / 7.3; 4: 0.133 / 7.5; 5: 0.126 / 8.2; 6: 0.118 / 9.1; 7: 0.110 / 9.4; 8: 0.097 / 10.4; 9: 0.091 / 10.6; 10: 0.091 / 10.9; 11: 0.088 / 11.0; 12: 0.079 / 11.4; 13: 0.074 / 12.0; 14: 0.070 / 12.4; 15: 0.068 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 149930, probability skill vs chance 0.231, widened contest next: False
  - now: threshold 0.8385, hit rate recent 0.9272 / long run 0.9264
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.304, naive rule 0.550, lift 2.96x
    - 24h: 52 calls (52 a day), hit rate 0.923, chance 0.286, naive rule 0.523, lift 3.22x
    - 7d: 402 calls (57 a day), hit rate 0.925, chance 0.287, naive rule 0.497, lift 3.22x
    - 30d: 1740 calls (58 a day), hit rate 0.930, chance 0.294, naive rule 0.498, lift 3.17x
  - next: threshold 0.5648, hit rate recent 0.6762 / long run 0.6179
    - 24h: 28 calls (28 a day), hit rate 0.750, chance 0.286, lift 2.62x
    - 7d: 313 calls (45 a day), hit rate 0.633, chance 0.287, lift 2.20x
    - 30d: 2569 calls (86 a day), hit rate 0.598, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.500; 0.35: 532, 0.525; 0.40: 474, 0.579; 0.45: 406, 0.649; 0.50: 357, 0.694; 0.55: 310, 0.738; 0.60: 260, 0.783; 0.65: 220, 0.812; 0.70: 172, 0.844; 0.75: 138, 0.874; 0.80: 91, 0.905; 0.85: 46, 0.941; 0.90: 5, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.432; 0.35: 496, 0.465; 0.40: 394, 0.505; 0.45: 296, 0.539; 0.50: 188, 0.571; 0.55: 83, 0.583; 0.60: 11, 0.656; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 149928, probability skill vs chance 0.2195, widened contest next: False
  - now: threshold 0.6938, hit rate recent 0.7638 / long run 0.778
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.208, naive rule 0.464, lift 3.69x
    - 24h: 61 calls (61 a day), hit rate 0.803, chance 0.187, naive rule 0.437, lift 4.30x
    - 7d: 424 calls (61 a day), hit rate 0.733, chance 0.182, naive rule 0.404, lift 4.03x
    - 30d: 1693 calls (56 a day), hit rate 0.800, chance 0.186, naive rule 0.407, lift 4.30x
  - next: threshold 0.4534, hit rate recent 0.5214 / long run 0.5136
    - 6h: 14 calls (57 a day), hit rate 0.286, chance 0.208, lift 1.37x
    - 24h: 60 calls (60 a day), hit rate 0.583, chance 0.187, lift 3.12x
    - 7d: 433 calls (62 a day), hit rate 0.513, chance 0.182, lift 2.81x
    - 30d: 2531 calls (84 a day), hit rate 0.490, chance 0.186, lift 2.63x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 356, 0.477; 0.40: 288, 0.547; 0.45: 234, 0.604; 0.50: 186, 0.651; 0.55: 148, 0.689; 0.60: 112, 0.738; 0.65: 76, 0.776; 0.70: 48, 0.810; 0.75: 28, 0.843; 0.80: 9, 0.873
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.385; 0.35: 255, 0.426; 0.40: 160, 0.458; 0.45: 65, 0.503; 0.50: 10, 0.538; 0.55: 1, 0.441
- **K=8**: model 1794614400, labels learned 149925, probability skill vs chance 0.2144, widened contest next: False
  - now: threshold 0.5678, hit rate recent 0.6905 / long run 0.6851
    - 6h: 11 calls (45 a day), hit rate 0.455, chance 0.116, naive rule 0.342, lift 3.93x
    - 24h: 45 calls (45 a day), hit rate 0.778, chance 0.125, naive rule 0.382, lift 6.23x
    - 7d: 363 calls (52 a day), hit rate 0.667, chance 0.122, naive rule 0.348, lift 5.46x
    - 30d: 1540 calls (51 a day), hit rate 0.685, chance 0.121, naive rule 0.337, lift 5.67x
  - next: threshold 0.3732, hit rate recent 0.4588 / long run 0.4292
    - 6h: 14 calls (58 a day), hit rate 0.357, chance 0.116, lift 3.09x
    - 24h: 66 calls (66 a day), hit rate 0.500, chance 0.125, lift 4.01x
    - 7d: 467 calls (67 a day), hit rate 0.428, chance 0.122, lift 3.50x
    - 30d: 2539 calls (85 a day), hit rate 0.403, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 194, 0.489; 0.40: 153, 0.534; 0.45: 118, 0.580; 0.50: 83, 0.639; 0.55: 59, 0.673; 0.60: 40, 0.712; 0.65: 23, 0.775; 0.70: 11, 0.815; 0.75: 2, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 166, 0.367; 0.35: 85, 0.396; 0.40: 24, 0.427; 0.45: 5, 0.427; 0.50: 1, 0.792
- **K=13**: model 1794700800, labels learned 149920, probability skill vs chance 0.196, widened contest next: False
  - now: threshold 0.4456, hit rate recent 0.629 / long run 0.5805
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.074, naive rule 0.253, lift 6.15x
    - 24h: 47 calls (47 a day), hit rate 0.702, chance 0.083, naive rule 0.333, lift 8.44x
    - 7d: 348 calls (50 a day), hit rate 0.586, chance 0.080, naive rule 0.303, lift 7.32x
    - 30d: 1637 calls (55 a day), hit rate 0.567, chance 0.078, naive rule 0.286, lift 7.27x
  - next: threshold 0.2991, hit rate recent 0.3233 / long run 0.3372
    - 6h: 16 calls (67 a day), hit rate 0.188, chance 0.074, lift 2.54x
    - 24h: 57 calls (58 a day), hit rate 0.351, chance 0.083, lift 4.22x
    - 7d: 470 calls (67 a day), hit rate 0.345, chance 0.080, lift 4.31x
    - 30d: 1835 calls (61 a day), hit rate 0.331, chance 0.078, lift 4.24x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 135, 0.431; 0.35: 97, 0.478; 0.40: 68, 0.538; 0.45: 47, 0.590; 0.50: 32, 0.639; 0.55: 20, 0.663; 0.60: 11, 0.702; 0.65: 3, 0.649; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.339; 0.35: 13, 0.338; 0.40: 3, 0.416; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.611 | 3.44% | 0.900 | 0.383 | 0.247 | 0.583 | 0.381 |
| 6h | 38.895 | 4.79% | 0.908 | 0.478 | 0.251 | 0.492 | 0.687 |
| 24h | 35.094 | 5.96% | 0.905 | 0.499 | 0.250 | 0.511 | 0.664 |
| 7d | 21.725 | 5.54% | 0.901 | 0.500 | 0.250 | 0.513 | 0.678 |
| 30d | 16.633 | 4.86% | 0.900 | 0.500 | 0.250 | 0.504 | 0.716 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.522 | 26.120 | 25.817 | 25.411 | 25.970 | 26.081 | 25.655 | 25.725 | 25.665 | 25.611 |
| 6h | 40.850 | 38.825 | 38.643 | 38.930 | 38.977 | 38.913 | 38.993 | 38.696 | 38.735 | 38.895 |
| 24h | 37.316 | 35.269 | 35.372 | 35.169 | 35.889 | 35.552 | 35.131 | 35.075 | 35.051 | 35.094 |
| 7d | 22.999 | 21.919 | 21.895 | 21.868 | 22.191 | 22.078 | 21.709 | 21.673 | 21.691 | 21.725 |
| 30d | 17.483 | 16.796 | 16.751 | 16.693 | 16.960 | 16.913 | 16.619 | 16.598 | 16.604 | 16.633 |

## Next candle

- candle starting 2026-11-15 06:56 UTC, last close 1790.47
- P(up) 0.4619, return quantiles (bp): {'05': -12.03, '10': -8.897, '25': -5.185, '40': -2.461, '50': -0.598, '60': 1.006, '75': 4.346, '90': 8.333, '95': 11.548}
- changepoint probability 0.0355, regime age 147.2 min
- agent weights: empirical 0.003, ewma 0.130, garch 0.118, har 0.217, bocpd 0.016, hmm 0.040, online_qr 0.195, lgbm 0.282

## Learning log

- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- HMM volatility states (sd, bp per minute): [5.05, 9.08, 23.18], current probabilities: [0.503, 0.488, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-11-15 07:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.272, 'l_abs': 0.717, 'l_hi': 0.787, 'l_lo': 0.729, 'b05': 0.744, 'b25': 0.737, 'b75': 0.6, 'b95': 0.721}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.386, 1.771, 1.817, 1.842, 2.062, 2.517, 2.696, 3.104, 3.623, 3.732, 3.985, 4.073, 3.91, 3.896]}
- calibration offsets (in sigma): {'05': 0.0675, '10': 0.055, '25': -0.0425, '40': -0.08, '50': -0.065, '60': -0.08, '75': -0.0375, '90': -0.085, '95': -0.0775}
