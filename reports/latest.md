# ETH-USD 60s candle generator - report

- generated: 2026-11-17 13:54 UTC
- last closed candle: 2026-11-17 13:54 UTC (staleness 0.5 min)
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
| chain_end_side | 0.583 (96) | 0.517 (671) [0.480, 0.551] | 0.522 (2879) [0.503, 0.539] | 0.515 (7289) [0.503, 0.526] | 0.517 (4317) [0.502, 0.533] | 0.509 (55) | 0.500 | flat +0.001 (noise 0.032) |
| colour_clear | 0.533 (825) | 0.539 (5648) [0.531, 0.547] | 0.542 (23976) [0.536, 0.548] | 0.524 (59798) [0.519, 0.529] | 0.543 (35560) [0.538, 0.547] | 0.498 (478) | 0.500 | flat +0.002 (noise 0.012) |
| colour_confident | 0.563 (238) | 0.533 (794) [0.506, 0.555] | 0.581 (4478) [0.569, 0.592] | 0.587 (6389) [0.577, 0.598] | 0.587 (6389) [0.577, 0.598] | 0.496 (121) | 0.500 | down -0.052 (noise 0.024) |
| colour_next | 0.529 (1432) | 0.529 (10049) [0.521, 0.536] | 0.531 (42892) [0.527, 0.535] | 0.518 (108609) [0.514, 0.522] | 0.530 (64260) [0.526, 0.533] | 0.507 (833) | 0.500 | flat -0.003 (noise 0.009) |
| colour_path | 0.502 (20048) | 0.502 (140686) [0.499, 0.504] | 0.502 (600488) [0.501, 0.503] | 0.501 (1520526) [0.500, 0.502] | 0.501 (899640) [0.500, 0.502] | 0.503 (11662) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.549 (82) | 0.567 (187) [0.531, 0.610] | 0.611 (1181) [0.595, 0.628] | 0.623 (1680) [0.606, 0.639] | 0.623 (1680) [0.606, 0.639] | 0.552 (29) | 0.500 | flat -0.049 (noise 0.047) |
| reversal_k13_next | 0.284 (74) | 0.339 (445) [0.306, 0.376] | 0.331 (1859) [0.316, 0.348] | 0.316 (4996) [0.305, 0.325] | 0.327 (2891) [0.316, 0.338] | 0.189 (37) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.548 (42) | 0.605 (339) [0.562, 0.653] | 0.568 (1612) [0.547, 0.590] | 0.575 (3897) [0.563, 0.588] | 0.572 (2425) [0.555, 0.588] | 0.419 (31) | 0.077 | flat +0.030 (noise 0.037) |
| reversal_k3_next | 0.573 (82) | 0.613 (341) [0.574, 0.662] | 0.601 (2483) [0.589, 0.613] | 0.589 (6346) [0.580, 0.598] | 0.591 (3906) [0.580, 0.602] | 0.600 (50) | 0.293 | flat -0.002 (noise 0.037) |
| reversal_k3_now | 0.942 (52) | 0.929 (393) [0.919, 0.939] | 0.932 (1730) [0.922, 0.941] | 0.935 (4356) [0.929, 0.941] | 0.931 (2593) [0.924, 0.938] | 1.000 (22) | 0.293 | flat +0.010 (noise 0.019) |
| reversal_k5_next | 0.478 (69) | 0.501 (447) [0.460, 0.549] | 0.496 (2418) [0.479, 0.514] | 0.487 (5785) [0.476, 0.498] | 0.483 (3795) [0.468, 0.497] | 0.312 (32) | 0.186 | flat -0.023 (noise 0.035) |
| reversal_k5_now | 0.726 (62) | 0.750 (455) [0.716, 0.784] | 0.795 (1711) [0.777, 0.810] | 0.817 (4121) [0.806, 0.827] | 0.804 (2510) [0.790, 0.816] | 0.765 (34) | 0.187 | flat -0.041 (noise 0.032) |
| reversal_k8_next | 0.352 (71) | 0.421 (456) [0.381, 0.465] | 0.405 (2458) [0.391, 0.421] | 0.397 (5888) [0.387, 0.407] | 0.398 (3782) [0.386, 0.410] | 0.333 (45) | 0.121 | flat +0.004 (noise 0.033) |
| reversal_k8_now | 0.589 (56) | 0.658 (380) [0.612, 0.709] | 0.677 (1555) [0.656, 0.698] | 0.696 (3962) [0.683, 0.709] | 0.684 (2375) [0.667, 0.701] | 0.636 (33) | 0.122 | flat -0.033 (noise 0.035) |
| overall | 0.505 (22084) | 0.506 (154662) [0.503, 0.507] | 0.506 (662085) [0.505, 0.507] | 0.504 (1675775) [0.503, 0.505] | 0.505 (992494) [0.504, 0.506] | 0.503 (12834) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0661, 0.09598] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5251, 'levels': [{'threshold': 0.0661, 'calls_per_day': 145.6, 'win_rate': 0.5382}, {'threshold': 0.09598, 'calls_per_day': 37.0, 'win_rate': 0.5538}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42900, 'rate': 0.5308}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15158 | 0.347 | 0.534 (14922) | 0.563 (2290) | 0.740 (2527) |
| volatility: normal | 15158 | 0.372 | 0.530 (15099) | 0.604 (1390) | 0.742 (2286) |
| volatility: wild | 15158 | 0.389 | 0.529 (15119) | 0.578 (1050) | 0.762 (2132) |
| session: Asia 00-08 | 15360 | 0.369 | 0.534 (15239) | 0.579 (1666) | 0.747 (2266) |
| session: Europe 08-13 | 9600 | 0.362 | 0.530 (9517) | 0.581 (1177) | 0.746 (1556) |
| session: US 13-21 | 14934 | 0.376 | 0.534 (14837) | 0.597 (1295) | 0.752 (2291) |
| session: late 21-24 | 5580 | 0.363 | 0.516 (5547) | 0.532 (592) | 0.737 (832) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.417 | 0.410 | 0.374 | 0.374 | 0.550 | 0.277 | 0.556 | 1.068 |
| 6h | 360 | 0.373 | 0.367 | 0.312 | 0.348 | 0.506 | 0.253 | 0.492 | 1.163 |
| 24h | 1440 | 0.374 | 0.366 | 0.307 | 0.342 | 0.504 | 0.254 | 0.494 | 1.144 |
| 7d | 10080 | 0.382 | 0.377 | 0.299 | 0.331 | 0.525 | 0.269 | 0.496 | 1.164 |
| 30d | 43200 | 0.370 | 0.363 | 0.282 | 0.314 | 0.531 | 0.266 | 0.475 | 1.249 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.417 / 0.550 / 0.867; 2: 0.400 / 0.450 / 1.000; 3: 0.375 / 0.417 / 0.983; 4: 0.398 / 0.500 / 1.000; 5: 0.408 / 0.550 / 1.000; 6: 0.381 / 0.433 / 0.983; 7: 0.424 / 0.550 / 0.983; 8: 0.381 / 0.467 / 1.000; 9: 0.401 / 0.517 / 1.000; 10: 0.409 / 0.517 / 1.000; 11: 0.412 / 0.533 / 1.000; 12: 0.411 / 0.550 / 1.000; 13: 0.400 / 0.483 / 1.000; 14: 0.377 / 0.517 / 1.000; 15: 0.389 / 0.483 / 0.967
- 6h: 1: 0.373 / 0.506 / 0.889; 2: 0.369 / 0.511 / 0.989; 3: 0.372 / 0.506 / 0.983; 4: 0.375 / 0.514 / 0.997; 5: 0.371 / 0.522 / 0.997; 6: 0.365 / 0.500 / 0.981; 7: 0.370 / 0.497 / 0.950; 8: 0.361 / 0.486 / 0.983; 9: 0.363 / 0.494 / 0.939; 10: 0.367 / 0.503 / 0.983; 11: 0.376 / 0.517 / 0.975; 12: 0.368 / 0.525 / 0.961; 13: 0.363 / 0.478 / 0.931; 14: 0.364 / 0.494 / 0.894; 15: 0.372 / 0.506 / 0.772
- 24h: 1: 0.374 / 0.504 / 0.890; 2: 0.371 / 0.490 / 0.914; 3: 0.375 / 0.511 / 0.916; 4: 0.374 / 0.510 / 0.914; 5: 0.372 / 0.502 / 0.906; 6: 0.371 / 0.511 / 0.910; 7: 0.369 / 0.498 / 0.903; 8: 0.371 / 0.505 / 0.905; 9: 0.362 / 0.472 / 0.899; 10: 0.372 / 0.509 / 0.908; 11: 0.371 / 0.512 / 0.908; 12: 0.369 / 0.506 / 0.903; 13: 0.367 / 0.492 / 0.896; 14: 0.368 / 0.497 / 0.895; 15: 0.369 / 0.494 / 0.856
- 7d: 1: 0.382 / 0.525 / 0.898; 2: 0.368 / 0.489 / 0.901; 3: 0.377 / 0.515 / 0.901; 4: 0.370 / 0.497 / 0.901; 5: 0.371 / 0.499 / 0.900; 6: 0.371 / 0.506 / 0.901; 7: 0.371 / 0.503 / 0.900; 8: 0.372 / 0.510 / 0.900; 9: 0.365 / 0.490 / 0.900; 10: 0.370 / 0.504 / 0.901; 11: 0.371 / 0.513 / 0.901; 12: 0.368 / 0.501 / 0.900; 13: 0.369 / 0.505 / 0.900; 14: 0.367 / 0.501 / 0.899; 15: 0.368 / 0.500 / 0.894
- 30d: 1: 0.370 / 0.531 / 0.898; 2: 0.357 / 0.493 / 0.900; 3: 0.361 / 0.512 / 0.900; 4: 0.356 / 0.497 / 0.900; 5: 0.357 / 0.503 / 0.900; 6: 0.355 / 0.501 / 0.900; 7: 0.356 / 0.499 / 0.900; 8: 0.356 / 0.506 / 0.900; 9: 0.355 / 0.501 / 0.900; 10: 0.356 / 0.504 / 0.900; 11: 0.355 / 0.505 / 0.900; 12: 0.355 / 0.503 / 0.900; 13: 0.354 / 0.499 / 0.900; 14: 0.354 / 0.502 / 0.900; 15: 0.354 / 0.501 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.154 (body 0.088, range 0.220); 'price stays where it was' would score 0.147; colour right 0.417; typical miss of the close 11.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.108 (body 0.069, range 0.146); 'price stays where it was' would score 0.120; colour right 0.492; typical miss of the close 15.7 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.129 (body 0.084, range 0.173); 'price stays where it was' would score 0.126; colour right 0.502; typical miss of the close 13.9 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.127 (body 0.084, range 0.171); 'price stays where it was' would score 0.130; colour right 0.504; typical miss of the close 13.8 bp; chain ended on the right side 0.520 of 671 chains; n=10080
- 30d: match 0.125 (body 0.084, range 0.166); 'price stays where it was' would score 0.129; colour right 0.502; typical miss of the close 9.7 bp; chain ended on the right side 0.520 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.1; 2: 0.203 / 5.8; 3: 0.167 / 7.7; 4: 0.133 / 8.1; 5: 0.126 / 8.7; 6: 0.117 / 9.5; 7: 0.111 / 9.9; 8: 0.099 / 10.8; 9: 0.092 / 11.1; 10: 0.091 / 11.4; 11: 0.086 / 11.8; 12: 0.079 / 12.2; 13: 0.073 / 12.8; 14: 0.067 / 13.2; 15: 0.067 / 13.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794873600, labels learned 153228, probability skill vs chance 0.2319, widened contest next: False
  - now: threshold 0.8342, hit rate recent 0.9593 / long run 0.9311
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.270, naive rule 0.452, lift 3.70x
    - 24h: 44 calls (44 a day), hit rate 0.977, chance 0.284, naive rule 0.493, lift 3.44x
    - 7d: 374 calls (53 a day), hit rate 0.930, chance 0.288, naive rule 0.499, lift 3.23x
    - 30d: 1710 calls (57 a day), hit rate 0.932, chance 0.293, naive rule 0.499, lift 3.18x
  - next: threshold 0.5518, hit rate recent 0.5835 / long run 0.6102
    - 6h: 25 calls (101 a day), hit rate 0.560, chance 0.270, lift 2.07x
    - 24h: 88 calls (88 a day), hit rate 0.568, chance 0.284, lift 2.00x
    - 7d: 358 calls (51 a day), hit rate 0.615, chance 0.288, lift 2.13x
    - 30d: 2474 calls (82 a day), hit rate 0.601, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 561, 0.501; 0.35: 530, 0.526; 0.40: 474, 0.579; 0.45: 407, 0.648; 0.50: 358, 0.693; 0.55: 310, 0.737; 0.60: 261, 0.782; 0.65: 221, 0.811; 0.70: 172, 0.843; 0.75: 138, 0.874; 0.80: 91, 0.906; 0.85: 45, 0.941; 0.90: 4, 0.970
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.434; 0.35: 493, 0.467; 0.40: 391, 0.506; 0.45: 293, 0.541; 0.50: 186, 0.573; 0.55: 81, 0.586; 0.60: 11, 0.649; 0.65: 1, 0.632
- **K=5**: model 1794528000, labels learned 153226, probability skill vs chance 0.2223, widened contest next: True
  - now: threshold 0.6988, hit rate recent 0.7576 / long run 0.7751
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.183, naive rule 0.415, lift 4.45x
    - 24h: 64 calls (64 a day), hit rate 0.734, chance 0.185, naive rule 0.427, lift 3.98x
    - 7d: 445 calls (64 a day), hit rate 0.739, chance 0.183, naive rule 0.408, lift 4.05x
    - 30d: 1715 calls (57 a day), hit rate 0.794, chance 0.186, naive rule 0.409, lift 4.27x
  - next: threshold 0.4415, hit rate recent 0.4067 / long run 0.5006
    - 6h: 16 calls (65 a day), hit rate 0.312, chance 0.183, lift 1.71x
    - 24h: 60 calls (60 a day), hit rate 0.333, chance 0.185, lift 1.81x
    - 7d: 439 calls (63 a day), hit rate 0.483, chance 0.183, lift 2.65x
    - 30d: 2354 calls (78 a day), hit rate 0.496, chance 0.186, lift 2.67x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 358, 0.475; 0.40: 290, 0.544; 0.45: 235, 0.604; 0.50: 186, 0.652; 0.55: 149, 0.688; 0.60: 113, 0.736; 0.65: 78, 0.772; 0.70: 48, 0.804; 0.75: 27, 0.837; 0.80: 8, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.387; 0.35: 253, 0.426; 0.40: 160, 0.458; 0.45: 64, 0.504; 0.50: 9, 0.551; 0.55: 1, 0.417
- **K=8**: model 1794873600, labels learned 153223, probability skill vs chance 0.1984, widened contest next: True
  - now: threshold 0.5687, hit rate recent 0.6261 / long run 0.671
    - 6h: 17 calls (70 a day), hit rate 0.588, chance 0.107, naive rule 0.296, lift 5.49x
    - 24h: 61 calls (61 a day), hit rate 0.590, chance 0.120, naive rule 0.334, lift 4.94x
    - 7d: 375 calls (54 a day), hit rate 0.651, chance 0.123, naive rule 0.350, lift 5.30x
    - 30d: 1559 calls (52 a day), hit rate 0.677, chance 0.121, naive rule 0.340, lift 5.59x
  - next: threshold 0.3624, hit rate recent 0.3466 / long run 0.4098
    - 6h: 23 calls (95 a day), hit rate 0.304, chance 0.107, lift 2.84x
    - 24h: 77 calls (78 a day), hit rate 0.325, chance 0.120, lift 2.72x
    - 7d: 458 calls (65 a day), hit rate 0.410, chance 0.123, lift 3.34x
    - 30d: 2433 calls (81 a day), hit rate 0.404, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 250, 0.427; 0.35: 195, 0.489; 0.40: 154, 0.534; 0.45: 118, 0.578; 0.50: 83, 0.636; 0.55: 59, 0.668; 0.60: 40, 0.705; 0.65: 23, 0.764; 0.70: 10, 0.810; 0.75: 2, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 164, 0.369; 0.35: 84, 0.396; 0.40: 24, 0.428; 0.45: 4, 0.452; 0.50: 1, 0.762
- **K=13**: model 1794873600, labels learned 153218, probability skill vs chance 0.1671, widened contest next: True
  - now: threshold 0.443, hit rate recent 0.5283 / long run 0.5754
    - 6h: 16 calls (67 a day), hit rate 0.375, chance 0.061, naive rule 0.212, lift 6.16x
    - 24h: 54 calls (55 a day), hit rate 0.481, chance 0.071, naive rule 0.246, lift 6.83x
    - 7d: 337 calls (48 a day), hit rate 0.588, chance 0.079, naive rule 0.302, lift 7.46x
    - 30d: 1599 calls (53 a day), hit rate 0.568, chance 0.078, naive rule 0.287, lift 7.30x
  - next: threshold 0.2929, hit rate recent 0.2615 / long run 0.3239
    - 6h: 21 calls (88 a day), hit rate 0.286, chance 0.061, lift 4.69x
    - 24h: 74 calls (75 a day), hit rate 0.243, chance 0.071, lift 3.45x
    - 7d: 440 calls (63 a day), hit rate 0.327, chance 0.079, lift 4.15x
    - 30d: 1848 calls (62 a day), hit rate 0.328, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 136, 0.429; 0.35: 98, 0.475; 0.40: 67, 0.534; 0.45: 46, 0.586; 0.50: 32, 0.627; 0.55: 20, 0.651; 0.60: 11, 0.691; 0.65: 3, 0.636; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.335; 0.35: 13, 0.347; 0.40: 2, 0.414; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.239 | 0.31% | 0.867 | 0.467 | 0.250 | 0.517 | 0.258 |
| 6h | 19.750 | 0.17% | 0.897 | 0.494 | 0.251 | 0.483 | 0.330 |
| 24h | 21.049 | 2.57% | 0.901 | 0.500 | 0.251 | 0.467 | 0.635 |
| 7d | 23.298 | 4.31% | 0.900 | 0.500 | 0.250 | 0.505 | 0.684 |
| 30d | 17.356 | 4.64% | 0.900 | 0.500 | 0.250 | 0.504 | 0.709 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.299 | 19.376 | 19.310 | 19.280 | 19.455 | 19.143 | 19.195 | 19.117 | 19.193 | 19.239 |
| 6h | 19.783 | 19.810 | 19.774 | 19.768 | 20.007 | 19.941 | 19.706 | 19.690 | 19.698 | 19.750 |
| 24h | 21.604 | 21.121 | 21.073 | 21.026 | 21.429 | 21.239 | 21.028 | 21.012 | 21.004 | 21.049 |
| 7d | 24.348 | 23.496 | 23.455 | 23.336 | 23.799 | 23.618 | 23.288 | 23.257 | 23.264 | 23.298 |
| 30d | 18.200 | 17.515 | 17.474 | 17.410 | 17.704 | 17.643 | 17.338 | 17.318 | 17.325 | 17.356 |

## Next candle

- candle starting 2026-11-17 13:54 UTC, last close 1823.41
- P(up) 0.5082, return quantiles (bp): {'05': -11.981, '10': -9.206, '25': -4.802, '40': -1.739, '50': 0.153, '60': 1.473, '75': 4.408, '90': 9.659, '95': 12.339}
- changepoint probability 0.0455, regime age 166.1 min
- agent weights: empirical 0.052, ewma 0.125, garch 0.138, har 0.157, bocpd 0.031, hmm 0.057, online_qr 0.212, lgbm 0.228

## Learning log

- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- 2026-11-16 00:00 UTC: {"garch": {"alpha": 0.0649, "beta": 0.9281}, "hmm": {"sd_bp": [5.12, 9.52, 24.14], "stay": [0.982, 0.963, 0.92]}, "lgbm": {"challenger_loss": 0.24944, "champion_loss": 0.2494, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47719, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47655, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3653, "challengers": 1, "chance_loss": 0.4822, "widened": false, "champion_loss": 0.36306, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2714, "challengers": 1, "chance_loss": 0.37579, "widened": false, "champion_loss": 0.27207, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19602, "challengers": 1, "chance_loss": 0.28273, "widened": false, "champion_loss": 0.19594, "promoted": false}}
- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- HMM volatility states (sd, bp per minute): [5.63, 9.77, 23.96], current probabilities: [0.43, 0.562, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-11-17 14:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.3, 'l_abs': 0.752, 'l_hi': 0.833, 'l_lo': 0.759, 'b05': 0.725, 'b25': 0.764, 'b75': 0.74, 'b95': 0.693}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.6, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.163, 1.344, 1.684, 2.398, 1.989, 2.63, 2.761, 3.116, 2.861, 3.068, 3.478, 4.257, 5.299, 13.791]}
- calibration offsets (in sigma): {'05': 0.0365, '10': 0.013, '25': 0.0025, '40': 0.012, '50': 0.035, '60': -0.012, '75': -0.0125, '90': 0.037, '95': -0.0265}
