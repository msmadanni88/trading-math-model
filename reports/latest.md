# ETH-USD 60s candle generator - report

- generated: 2026-11-17 04:45 UTC
- last closed candle: 2026-11-17 04:45 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: colour_confident 0.533 in the last 7 days, -0.052 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.583 (96) | 0.517 (671) [0.480, 0.551] | 0.522 (2879) [0.503, 0.539] | 0.515 (7289) [0.503, 0.526] | 0.517 (4317) [0.502, 0.533] | 0.579 (19) | 0.500 | flat +0.001 (noise 0.032) |
| colour_clear | 0.533 (825) | 0.539 (5648) [0.531, 0.547] | 0.542 (23976) [0.536, 0.548] | 0.524 (59798) [0.519, 0.529] | 0.543 (35560) [0.538, 0.547] | 0.479 (165) | 0.500 | flat +0.002 (noise 0.012) |
| colour_confident | 0.563 (238) | 0.533 (794) [0.506, 0.555] | 0.581 (4478) [0.569, 0.592] | 0.587 (6389) [0.577, 0.598] | 0.587 (6389) [0.577, 0.598] | 0.476 (42) | 0.500 | down -0.052 (noise 0.024) |
| colour_next | 0.529 (1432) | 0.529 (10049) [0.521, 0.536] | 0.531 (42892) [0.527, 0.535] | 0.518 (108609) [0.514, 0.522] | 0.530 (64260) [0.526, 0.533] | 0.511 (284) | 0.500 | flat -0.003 (noise 0.009) |
| colour_path | 0.502 (20048) | 0.502 (140686) [0.499, 0.504] | 0.502 (600488) [0.501, 0.503] | 0.501 (1520526) [0.500, 0.502] | 0.501 (899640) [0.500, 0.502] | 0.498 (3976) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.549 (82) | 0.567 (187) [0.531, 0.610] | 0.611 (1181) [0.595, 0.628] | 0.623 (1680) [0.606, 0.639] | 0.623 (1680) [0.606, 0.639] | 0.400 (10) | 0.500 | flat -0.049 (noise 0.047) |
| reversal_k13_next | 0.284 (74) | 0.339 (445) [0.306, 0.376] | 0.331 (1859) [0.316, 0.348] | 0.316 (4996) [0.305, 0.325] | 0.327 (2891) [0.316, 0.338] | 0.000 (12) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.548 (42) | 0.605 (339) [0.562, 0.653] | 0.568 (1612) [0.547, 0.590] | 0.575 (3897) [0.563, 0.588] | 0.572 (2425) [0.555, 0.588] | 0.429 (7) | 0.077 | flat +0.030 (noise 0.037) |
| reversal_k3_next | 0.573 (82) | 0.613 (341) [0.574, 0.662] | 0.601 (2483) [0.589, 0.613] | 0.589 (6346) [0.580, 0.598] | 0.591 (3906) [0.580, 0.602] | 0.706 (17) | 0.293 | flat -0.002 (noise 0.037) |
| reversal_k3_now | 0.942 (52) | 0.929 (393) [0.919, 0.939] | 0.932 (1730) [0.922, 0.941] | 0.935 (4356) [0.929, 0.941] | 0.931 (2593) [0.924, 0.938] | 1.000 (7) | 0.293 | flat +0.010 (noise 0.019) |
| reversal_k5_next | 0.478 (69) | 0.501 (447) [0.460, 0.549] | 0.496 (2418) [0.479, 0.514] | 0.487 (5785) [0.476, 0.498] | 0.483 (3795) [0.468, 0.497] | 0.385 (13) | 0.186 | flat -0.023 (noise 0.035) |
| reversal_k5_now | 0.726 (62) | 0.750 (455) [0.716, 0.784] | 0.795 (1711) [0.777, 0.810] | 0.817 (4121) [0.806, 0.827] | 0.804 (2510) [0.790, 0.816] | 0.750 (12) | 0.187 | flat -0.041 (noise 0.032) |
| reversal_k8_next | 0.352 (71) | 0.421 (456) [0.381, 0.465] | 0.405 (2458) [0.391, 0.421] | 0.397 (5888) [0.387, 0.407] | 0.398 (3782) [0.386, 0.410] | 0.400 (15) | 0.121 | flat +0.004 (noise 0.033) |
| reversal_k8_now | 0.589 (56) | 0.658 (380) [0.612, 0.709] | 0.677 (1555) [0.656, 0.698] | 0.696 (3962) [0.683, 0.709] | 0.684 (2375) [0.667, 0.701] | 0.625 (8) | 0.122 | flat -0.033 (noise 0.035) |
| overall | 0.505 (22084) | 0.506 (154662) [0.503, 0.507] | 0.506 (662085) [0.505, 0.507] | 0.504 (1675775) [0.503, 0.505] | 0.505 (992494) [0.504, 0.506] | 0.500 (4370) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0651, 0.09478] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5289, 'levels': [{'threshold': 0.0651, 'calls_per_day': 150.7, 'win_rate': 0.5388}, {'threshold': 0.09478, 'calls_per_day': 38.3, 'win_rate': 0.5613}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42894, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14975 | 0.347 | 0.534 (14739) | 0.562 (2272) | 0.740 (2495) |
| volatility: normal | 14975 | 0.372 | 0.530 (14916) | 0.605 (1361) | 0.744 (2260) |
| volatility: wild | 14975 | 0.389 | 0.529 (14936) | 0.584 (1018) | 0.763 (2104) |
| session: Asia 00-08 | 15165 | 0.369 | 0.534 (15044) | 0.579 (1644) | 0.748 (2239) |
| session: Europe 08-13 | 9300 | 0.362 | 0.531 (9217) | 0.585 (1127) | 0.749 (1503) |
| session: US 13-21 | 14880 | 0.376 | 0.534 (14783) | 0.599 (1288) | 0.752 (2285) |
| session: late 21-24 | 5580 | 0.363 | 0.516 (5547) | 0.532 (592) | 0.737 (832) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.370 | 0.342 | 0.334 | 0.334 | 0.533 | 0.257 | 0.482 | 1.246 |
| 6h | 360 | 0.371 | 0.346 | 0.318 | 0.348 | 0.520 | 0.254 | 0.489 | 1.189 |
| 24h | 1440 | 0.379 | 0.373 | 0.310 | 0.349 | 0.517 | 0.259 | 0.499 | 1.184 |
| 7d | 10080 | 0.383 | 0.377 | 0.298 | 0.329 | 0.527 | 0.270 | 0.495 | 1.170 |
| 30d | 43200 | 0.370 | 0.363 | 0.282 | 0.313 | 0.531 | 0.266 | 0.474 | 1.244 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.370 / 0.533 / 0.950; 2: 0.380 / 0.500 / 0.817; 3: 0.384 / 0.550 / 0.817; 4: 0.382 / 0.483 / 0.850; 5: 0.381 / 0.583 / 0.767; 6: 0.387 / 0.517 / 0.867; 7: 0.378 / 0.550 / 0.867; 8: 0.369 / 0.483 / 0.883; 9: 0.390 / 0.550 / 0.917; 10: 0.377 / 0.533 / 0.900; 11: 0.412 / 0.600 / 0.917; 12: 0.371 / 0.483 / 0.933; 13: 0.393 / 0.550 / 0.950; 14: 0.360 / 0.517 / 0.983; 15: 0.367 / 0.517 / 1.000
- 6h: 1: 0.371 / 0.520 / 0.881; 2: 0.379 / 0.503 / 0.775; 3: 0.382 / 0.525 / 0.800; 4: 0.369 / 0.478 / 0.761; 5: 0.369 / 0.480 / 0.717; 6: 0.385 / 0.542 / 0.806; 7: 0.371 / 0.492 / 0.822; 8: 0.373 / 0.506 / 0.778; 9: 0.376 / 0.489 / 0.828; 10: 0.373 / 0.503 / 0.781; 11: 0.378 / 0.536 / 0.789; 12: 0.369 / 0.483 / 0.811; 13: 0.374 / 0.508 / 0.822; 14: 0.370 / 0.494 / 0.847; 15: 0.366 / 0.478 / 0.933
- 24h: 1: 0.379 / 0.517 / 0.890; 2: 0.369 / 0.477 / 0.875; 3: 0.380 / 0.513 / 0.878; 4: 0.370 / 0.488 / 0.872; 5: 0.371 / 0.491 / 0.864; 6: 0.377 / 0.523 / 0.880; 7: 0.371 / 0.503 / 0.883; 8: 0.376 / 0.512 / 0.875; 9: 0.366 / 0.479 / 0.883; 10: 0.374 / 0.498 / 0.874; 11: 0.372 / 0.502 / 0.877; 12: 0.372 / 0.502 / 0.885; 13: 0.373 / 0.508 / 0.885; 14: 0.371 / 0.491 / 0.889; 15: 0.371 / 0.499 / 0.904
- 7d: 1: 0.383 / 0.527 / 0.898; 2: 0.367 / 0.487 / 0.899; 3: 0.377 / 0.516 / 0.900; 4: 0.369 / 0.494 / 0.898; 5: 0.370 / 0.497 / 0.896; 6: 0.370 / 0.505 / 0.899; 7: 0.370 / 0.503 / 0.901; 8: 0.372 / 0.510 / 0.898; 9: 0.365 / 0.491 / 0.899; 10: 0.370 / 0.504 / 0.900; 11: 0.370 / 0.512 / 0.900; 12: 0.367 / 0.499 / 0.900; 13: 0.368 / 0.507 / 0.900; 14: 0.367 / 0.501 / 0.900; 15: 0.367 / 0.501 / 0.901
- 30d: 1: 0.370 / 0.531 / 0.897; 2: 0.357 / 0.492 / 0.899; 3: 0.361 / 0.512 / 0.899; 4: 0.356 / 0.497 / 0.899; 5: 0.357 / 0.503 / 0.899; 6: 0.355 / 0.501 / 0.899; 7: 0.355 / 0.499 / 0.899; 8: 0.356 / 0.506 / 0.899; 9: 0.355 / 0.501 / 0.900; 10: 0.355 / 0.503 / 0.899; 11: 0.355 / 0.505 / 0.900; 12: 0.354 / 0.503 / 0.900; 13: 0.353 / 0.500 / 0.900; 14: 0.354 / 0.501 / 0.900; 15: 0.353 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.092 (body 0.051, range 0.133); 'price stays where it was' would score 0.137; colour right 0.483; typical miss of the close 9.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.119 (body 0.071, range 0.167); 'price stays where it was' would score 0.125; colour right 0.492; typical miss of the close 12.3 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.128 (body 0.082, range 0.173); 'price stays where it was' would score 0.128; colour right 0.501; typical miss of the close 13.9 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.127 (body 0.083, range 0.170); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 13.7 bp; chain ended on the right side 0.520 of 671 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.166); 'price stays where it was' would score 0.128; colour right 0.503; typical miss of the close 9.6 bp; chain ended on the right side 0.521 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.0; 2: 0.203 / 5.8; 3: 0.167 / 7.7; 4: 0.132 / 8.0; 5: 0.125 / 8.6; 6: 0.117 / 9.5; 7: 0.110 / 9.8; 8: 0.100 / 10.7; 9: 0.092 / 11.0; 10: 0.091 / 11.3; 11: 0.086 / 11.7; 12: 0.078 / 12.1; 13: 0.074 / 12.7; 14: 0.068 / 13.1; 15: 0.067 / 13.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794873600, labels learned 152679, probability skill vs chance 0.2347, widened contest next: False
  - now: threshold 0.8365, hit rate recent 0.9476 / long run 0.9293
    - 6h: 8 calls (32 a day), hit rate 1.000, chance 0.287, naive rule 0.473, lift 3.48x
    - 24h: 49 calls (49 a day), hit rate 0.959, chance 0.301, naive rule 0.518, lift 3.19x
    - 7d: 383 calls (55 a day), hit rate 0.930, chance 0.288, naive rule 0.499, lift 3.23x
    - 30d: 1723 calls (57 a day), hit rate 0.932, chance 0.294, naive rule 0.499, lift 3.17x
  - next: threshold 0.5542, hit rate recent 0.6097 / long run 0.6139
    - 6h: 25 calls (101 a day), hit rate 0.600, chance 0.287, lift 2.09x
    - 24h: 83 calls (83 a day), hit rate 0.602, chance 0.301, lift 2.00x
    - 7d: 346 calls (49 a day), hit rate 0.621, chance 0.288, lift 2.16x
    - 30d: 2489 calls (83 a day), hit rate 0.602, chance 0.294, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 561, 0.501; 0.35: 531, 0.526; 0.40: 474, 0.580; 0.45: 406, 0.649; 0.50: 358, 0.694; 0.55: 310, 0.738; 0.60: 261, 0.783; 0.65: 220, 0.811; 0.70: 172, 0.843; 0.75: 138, 0.874; 0.80: 91, 0.906; 0.85: 45, 0.942; 0.90: 4, 0.970
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.434; 0.35: 493, 0.467; 0.40: 392, 0.506; 0.45: 294, 0.541; 0.50: 186, 0.573; 0.55: 81, 0.588; 0.60: 11, 0.658; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 152677, probability skill vs chance 0.2181, widened contest next: True
  - now: threshold 0.6988, hit rate recent 0.7492 / long run 0.7752
    - 6h: 15 calls (61 a day), hit rate 0.667, chance 0.178, naive rule 0.386, lift 3.74x
    - 24h: 62 calls (62 a day), hit rate 0.726, chance 0.185, naive rule 0.418, lift 3.93x
    - 7d: 451 calls (64 a day), hit rate 0.745, chance 0.182, naive rule 0.406, lift 4.09x
    - 30d: 1714 calls (57 a day), hit rate 0.794, chance 0.186, naive rule 0.408, lift 4.27x
  - next: threshold 0.4619, hit rate recent 0.4538 / long run 0.5081
    - 6h: 18 calls (73 a day), hit rate 0.278, chance 0.178, lift 1.56x
    - 24h: 68 calls (68 a day), hit rate 0.456, chance 0.185, lift 2.47x
    - 7d: 445 calls (64 a day), hit rate 0.494, chance 0.182, lift 2.71x
    - 30d: 2409 calls (80 a day), hit rate 0.495, chance 0.186, lift 2.67x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.419; 0.35: 358, 0.475; 0.40: 290, 0.544; 0.45: 235, 0.603; 0.50: 187, 0.651; 0.55: 149, 0.687; 0.60: 113, 0.735; 0.65: 77, 0.771; 0.70: 48, 0.805; 0.75: 27, 0.838; 0.80: 8, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 254, 0.425; 0.40: 161, 0.458; 0.45: 65, 0.507; 0.50: 9, 0.557; 0.55: 1, 0.462
- **K=8**: model 1794873600, labels learned 152674, probability skill vs chance 0.1991, widened contest next: True
  - now: threshold 0.5685, hit rate recent 0.6187 / long run 0.6723
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.129, naive rule 0.348, lift 4.79x
    - 24h: 54 calls (54 a day), hit rate 0.574, chance 0.122, naive rule 0.335, lift 4.70x
    - 7d: 374 calls (53 a day), hit rate 0.660, chance 0.124, naive rule 0.352, lift 5.34x
    - 30d: 1555 calls (52 a day), hit rate 0.677, chance 0.121, naive rule 0.340, lift 5.58x
  - next: threshold 0.3638, hit rate recent 0.3665 / long run 0.4154
    - 6h: 19 calls (78 a day), hit rate 0.316, chance 0.129, lift 2.46x
    - 24h: 72 calls (73 a day), hit rate 0.347, chance 0.122, lift 2.85x
    - 7d: 459 calls (66 a day), hit rate 0.420, chance 0.124, lift 3.40x
    - 30d: 2455 calls (82 a day), hit rate 0.405, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 249, 0.427; 0.35: 195, 0.489; 0.40: 154, 0.534; 0.45: 118, 0.579; 0.50: 83, 0.635; 0.55: 59, 0.667; 0.60: 39, 0.707; 0.65: 23, 0.765; 0.70: 10, 0.812; 0.75: 2, 0.770
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 164, 0.369; 0.35: 84, 0.397; 0.40: 24, 0.431; 0.45: 4, 0.463; 0.50: 1, 0.783
- **K=13**: model 1794873600, labels learned 152669, probability skill vs chance 0.1681, widened contest next: True
  - now: threshold 0.4428, hit rate recent 0.5807 / long run 0.5819
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.075, naive rule 0.248, lift 6.03x
    - 24h: 43 calls (43 a day), hit rate 0.512, chance 0.073, naive rule 0.254, lift 6.98x
    - 7d: 333 calls (48 a day), hit rate 0.607, chance 0.080, naive rule 0.307, lift 7.55x
    - 30d: 1606 calls (54 a day), hit rate 0.568, chance 0.078, naive rule 0.287, lift 7.29x
  - next: threshold 0.2985, hit rate recent 0.246 / long run 0.3257
    - 6h: 16 calls (67 a day), hit rate 0.000, chance 0.075, lift 0.00x
    - 24h: 72 calls (73 a day), hit rate 0.236, chance 0.073, lift 3.22x
    - 7d: 442 calls (63 a day), hit rate 0.333, chance 0.080, lift 4.14x
    - 30d: 1861 calls (62 a day), hit rate 0.329, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 135, 0.430; 0.35: 98, 0.476; 0.40: 67, 0.535; 0.45: 46, 0.587; 0.50: 32, 0.630; 0.55: 20, 0.654; 0.60: 11, 0.697; 0.65: 3, 0.644; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.338; 0.35: 13, 0.347; 0.40: 2, 0.437; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.403 | 9.41% | 1.000 | 0.500 | 0.252 | 0.383 | -0.114 |
| 6h | 16.833 | 1.95% | 0.911 | 0.486 | 0.252 | 0.397 | 0.341 |
| 24h | 21.535 | 2.58% | 0.897 | 0.503 | 0.251 | 0.482 | 0.628 |
| 7d | 23.321 | 4.40% | 0.899 | 0.500 | 0.250 | 0.507 | 0.655 |
| 30d | 17.263 | 4.67% | 0.900 | 0.500 | 0.250 | 0.504 | 0.711 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.587 | 11.389 | 11.481 | 11.308 | 11.554 | 11.575 | 11.391 | 11.357 | 11.369 | 11.403 |
| 6h | 17.167 | 16.852 | 16.810 | 16.865 | 16.939 | 16.921 | 16.772 | 16.775 | 16.774 | 16.833 |
| 24h | 22.106 | 21.624 | 21.570 | 21.511 | 21.926 | 21.740 | 21.506 | 21.506 | 21.495 | 21.535 |
| 7d | 24.395 | 23.524 | 23.488 | 23.367 | 23.849 | 23.636 | 23.311 | 23.277 | 23.286 | 23.321 |
| 30d | 18.109 | 17.424 | 17.381 | 17.318 | 17.608 | 17.547 | 17.246 | 17.225 | 17.232 | 17.263 |

## Next candle

- candle starting 2026-11-17 04:45 UTC, last close 1830.24
- P(up) 0.5032, return quantiles (bp): {'05': -8.499, '10': -6.571, '25': -3.27, '40': -1.301, '50': 0.044, '60': 1.342, '75': 3.585, '90': 7.032, '95': 8.738}
- changepoint probability 0.0329, regime age 63.2 min
- agent weights: empirical 0.014, ewma 0.127, garch 0.150, har 0.171, bocpd 0.045, hmm 0.073, online_qr 0.206, lgbm 0.212

## Learning log

- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- 2026-11-16 00:00 UTC: {"garch": {"alpha": 0.0649, "beta": 0.9281}, "hmm": {"sd_bp": [5.12, 9.52, 24.14], "stay": [0.982, 0.963, 0.92]}, "lgbm": {"challenger_loss": 0.24944, "champion_loss": 0.2494, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47719, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47655, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3653, "challengers": 1, "chance_loss": 0.4822, "widened": false, "champion_loss": 0.36306, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2714, "challengers": 1, "chance_loss": 0.37579, "widened": false, "champion_loss": 0.27207, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19602, "challengers": 1, "chance_loss": 0.28273, "widened": false, "champion_loss": 0.19594, "promoted": false}}
- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- HMM volatility states (sd, bp per minute): [5.66, 9.83, 24.07], current probabilities: [0.955, 0.042, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-11-17 04:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.206, 'l_abs': 0.778, 'l_hi': 0.817, 'l_lo': 0.779, 'b05': 0.742, 'b25': 0.798, 'b75': 0.745, 'b95': 0.729}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [2.797, 3.106, 4.478, 6.251, 4.246, 4.242, 5.44, 4.458, 6.106, 5.806, 5.498, 5.293, 4.785, 3.533]}
- calibration offsets (in sigma): {'05': 0.042, '10': 0.004, '25': 0.04, '40': 0.016, '50': 0.02, '60': 0.034, '75': 0.06, '90': 0.086, '95': -0.022}
