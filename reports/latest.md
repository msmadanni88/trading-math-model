# ETH-USD 60s candle generator - report

- generated: 2026-11-16 12:40 UTC
- last closed candle: 2026-11-16 12:40 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: colour_confident 0.530 in the last 7 days, -0.051 against the 7 before
- WIN RATE FALLING: reversal_k5_now 0.743 in the last 7 days, -0.065 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.522 (671) [0.482, 0.560] | 0.518 (2879) [0.501, 0.536] | 0.514 (7193) [0.502, 0.525] | 0.515 (4221) [0.500, 0.531] | 0.640 (50) | 0.500 | flat +0.022 (noise 0.030) |
| colour_clear | 0.549 (780) | 0.539 (5614) [0.531, 0.547] | 0.543 (23916) [0.538, 0.549] | 0.524 (58973) [0.519, 0.529] | 0.543 (34735) [0.538, 0.547] | 0.534 (446) | 0.500 | flat +0.003 (noise 0.012) |
| colour_confident | 0.512 (207) | 0.530 (606) [0.505, 0.566] | 0.582 (4371) [0.570, 0.593] | 0.588 (6151) [0.577, 0.599] | 0.588 (6151) [0.577, 0.599] | 0.560 (100) | 0.500 | down -0.051 (noise 0.025) |
| colour_next | 0.540 (1436) | 0.529 (10053) [0.521, 0.536] | 0.531 (42875) [0.527, 0.535] | 0.518 (107177) [0.514, 0.522] | 0.530 (62828) [0.526, 0.533] | 0.549 (756) | 0.500 | flat -0.003 (noise 0.009) |
| colour_path | 0.505 (20104) | 0.502 (140742) [0.499, 0.504] | 0.501 (600250) [0.500, 0.503] | 0.501 (1500478) [0.500, 0.502] | 0.501 (879592) [0.500, 0.502] | 0.506 (10584) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.589 (56) | 0.579 (107) [0.500, 0.632] | 0.615 (1133) [0.600, 0.631] | 0.627 (1598) [0.611, 0.643] | 0.627 (1598) [0.611, 0.643] | 0.571 (35) | 0.500 | flat -0.043 (noise 0.056) |
| reversal_k13_next | 0.302 (63) | 0.352 (438) [0.323, 0.384] | 0.333 (1832) [0.318, 0.349] | 0.316 (4922) [0.306, 0.326] | 0.328 (2817) [0.317, 0.339] | 0.188 (32) | 0.077 | flat +0.017 (noise 0.032) |
| reversal_k13_now | 0.633 (49) | 0.604 (338) [0.560, 0.655] | 0.570 (1624) [0.549, 0.591] | 0.576 (3855) [0.563, 0.588] | 0.572 (2383) [0.556, 0.589] | 0.438 (16) | 0.077 | flat +0.039 (noise 0.037) |
| reversal_k3_next | 0.571 (35) | 0.623 (300) [0.580, 0.673] | 0.600 (2515) [0.588, 0.613] | 0.590 (6264) [0.581, 0.598] | 0.591 (3824) [0.580, 0.602] | 0.600 (40) | 0.293 | flat -0.000 (noise 0.036) |
| reversal_k3_now | 0.933 (45) | 0.924 (396) [0.914, 0.935] | 0.929 (1740) [0.920, 0.939] | 0.935 (4304) [0.929, 0.941] | 0.930 (2541) [0.923, 0.938] | 0.926 (27) | 0.293 | flat +0.007 (noise 0.019) |
| reversal_k5_next | 0.456 (57) | 0.506 (415) [0.461, 0.557] | 0.494 (2491) [0.477, 0.512] | 0.487 (5716) [0.476, 0.498] | 0.483 (3726) [0.469, 0.498] | 0.538 (39) | 0.187 | flat -0.024 (noise 0.035) |
| reversal_k5_now | 0.809 (63) | 0.743 (432) [0.701, 0.783] | 0.798 (1701) [0.782, 0.813] | 0.818 (4059) [0.808, 0.828] | 0.806 (2448) [0.792, 0.818] | 0.750 (28) | 0.187 | down -0.065 (noise 0.029) |
| reversal_k8_next | 0.353 (68) | 0.438 (450) [0.401, 0.479] | 0.406 (2507) [0.392, 0.421] | 0.398 (5817) [0.388, 0.408] | 0.399 (3711) [0.386, 0.411] | 0.368 (38) | 0.121 | flat +0.022 (noise 0.034) |
| reversal_k8_now | 0.603 (58) | 0.667 (372) [0.627, 0.720] | 0.683 (1548) [0.662, 0.702] | 0.698 (3906) [0.684, 0.711] | 0.686 (2319) [0.669, 0.703] | 0.600 (25) | 0.122 | flat -0.022 (noise 0.035) |
| overall | 0.508 (22074) | 0.506 (154607) [0.504, 0.508] | 0.505 (661962) [0.504, 0.507] | 0.504 (1653691) [0.503, 0.505] | 0.505 (970410) [0.504, 0.506] | 0.510 (11635) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06355, 0.0927] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5318, 'levels': [{'threshold': 0.06355, 'calls_per_day': 143.2, 'win_rate': 0.5502}, {'threshold': 0.0927, 'calls_per_day': 35.2, 'win_rate': 0.5668}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42882, 'rate': 0.5316}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15135 | 0.347 | 0.534 (14898) | 0.565 (2287) | 0.740 (2528) |
| volatility: normal | 15132 | 0.372 | 0.530 (15073) | 0.611 (1342) | 0.747 (2331) |
| volatility: wild | 15133 | 0.389 | 0.530 (15093) | 0.583 (930) | 0.764 (2102) |
| session: Asia 00-08 | 15360 | 0.369 | 0.534 (15238) | 0.582 (1641) | 0.749 (2302) |
| session: Europe 08-13 | 9580 | 0.362 | 0.531 (9498) | 0.585 (1153) | 0.745 (1562) |
| session: US 13-21 | 14880 | 0.376 | 0.534 (14783) | 0.600 (1203) | 0.754 (2276) |
| session: late 21-24 | 5580 | 0.363 | 0.517 (5545) | 0.537 (562) | 0.748 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.385 | 0.387 | 0.356 | 0.356 | 0.483 | 0.275 | 0.494 | 0.906 |
| 6h | 360 | 0.381 | 0.368 | 0.326 | 0.374 | 0.542 | 0.262 | 0.500 | 1.253 |
| 24h | 1440 | 0.390 | 0.373 | 0.310 | 0.348 | 0.558 | 0.278 | 0.503 | 1.264 |
| 7d | 10080 | 0.384 | 0.378 | 0.298 | 0.329 | 0.531 | 0.272 | 0.495 | 1.169 |
| 30d | 43200 | 0.369 | 0.363 | 0.280 | 0.312 | 0.532 | 0.266 | 0.473 | 1.242 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.385 / 0.483 / 0.900; 2: 0.419 / 0.567 / 0.767; 3: 0.393 / 0.500 / 0.800; 4: 0.388 / 0.483 / 0.733; 5: 0.399 / 0.567 / 0.733; 6: 0.420 / 0.583 / 0.783; 7: 0.384 / 0.500 / 0.800; 8: 0.414 / 0.617 / 0.750; 9: 0.385 / 0.467 / 0.750; 10: 0.400 / 0.550 / 0.700; 11: 0.405 / 0.517 / 0.717; 12: 0.391 / 0.533 / 0.750; 13: 0.360 / 0.417 / 0.750; 14: 0.384 / 0.500 / 0.717; 15: 0.383 / 0.483 / 0.783
- 6h: 1: 0.381 / 0.542 / 0.897; 2: 0.368 / 0.492 / 0.861; 3: 0.378 / 0.503 / 0.864; 4: 0.360 / 0.466 / 0.869; 5: 0.367 / 0.486 / 0.861; 6: 0.381 / 0.570 / 0.875; 7: 0.372 / 0.511 / 0.878; 8: 0.377 / 0.520 / 0.858; 9: 0.367 / 0.503 / 0.864; 10: 0.375 / 0.511 / 0.850; 11: 0.362 / 0.466 / 0.844; 12: 0.373 / 0.528 / 0.869; 13: 0.365 / 0.506 / 0.861; 14: 0.368 / 0.472 / 0.842; 15: 0.370 / 0.517 / 0.864
- 24h: 1: 0.390 / 0.558 / 0.902; 2: 0.375 / 0.499 / 0.892; 3: 0.382 / 0.521 / 0.889; 4: 0.371 / 0.485 / 0.897; 5: 0.373 / 0.494 / 0.897; 6: 0.378 / 0.528 / 0.903; 7: 0.376 / 0.504 / 0.899; 8: 0.377 / 0.509 / 0.898; 9: 0.372 / 0.501 / 0.897; 10: 0.378 / 0.515 / 0.894; 11: 0.373 / 0.504 / 0.894; 12: 0.380 / 0.529 / 0.899; 13: 0.372 / 0.500 / 0.901; 14: 0.374 / 0.498 / 0.896; 15: 0.376 / 0.514 / 0.903
- 7d: 1: 0.384 / 0.531 / 0.900; 2: 0.368 / 0.488 / 0.898; 3: 0.376 / 0.517 / 0.899; 4: 0.368 / 0.491 / 0.898; 5: 0.369 / 0.499 / 0.898; 6: 0.368 / 0.501 / 0.899; 7: 0.370 / 0.504 / 0.899; 8: 0.370 / 0.508 / 0.898; 9: 0.366 / 0.497 / 0.899; 10: 0.369 / 0.504 / 0.899; 11: 0.371 / 0.515 / 0.899; 12: 0.367 / 0.500 / 0.900; 13: 0.367 / 0.506 / 0.899; 14: 0.366 / 0.503 / 0.899; 15: 0.367 / 0.502 / 0.900
- 30d: 1: 0.369 / 0.532 / 0.897; 2: 0.356 / 0.492 / 0.900; 3: 0.360 / 0.512 / 0.900; 4: 0.355 / 0.496 / 0.900; 5: 0.356 / 0.503 / 0.900; 6: 0.354 / 0.501 / 0.900; 7: 0.355 / 0.499 / 0.900; 8: 0.355 / 0.506 / 0.900; 9: 0.354 / 0.501 / 0.900; 10: 0.354 / 0.503 / 0.900; 11: 0.353 / 0.504 / 0.900; 12: 0.353 / 0.503 / 0.900; 13: 0.352 / 0.499 / 0.900; 14: 0.353 / 0.501 / 0.900; 15: 0.352 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.104 (body 0.078, range 0.130); 'price stays where it was' would score 0.128; colour right 0.533; typical miss of the close 13.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.115 (body 0.076, range 0.155); 'price stays where it was' would score 0.127; colour right 0.508; typical miss of the close 13.6 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.117 (body 0.073, range 0.162); 'price stays where it was' would score 0.132; colour right 0.493; typical miss of the close 15.7 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.125 (body 0.082, range 0.167); 'price stays where it was' would score 0.127; colour right 0.504; typical miss of the close 13.5 bp; chain ended on the right side 0.523 of 671 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.166); 'price stays where it was' would score 0.128; colour right 0.503; typical miss of the close 9.5 bp; chain ended on the right side 0.522 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.9; 2: 0.203 / 5.7; 3: 0.168 / 7.6; 4: 0.132 / 7.8; 5: 0.125 / 8.5; 6: 0.118 / 9.4; 7: 0.110 / 9.7; 8: 0.098 / 10.6; 9: 0.091 / 10.9; 10: 0.091 / 11.2; 11: 0.085 / 11.4; 12: 0.078 / 12.0; 13: 0.073 / 12.4; 14: 0.069 / 12.8; 15: 0.068 / 13.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 151714, probability skill vs chance 0.2306, widened contest next: False
  - now: threshold 0.8365, hit rate recent 0.9349 / long run 0.9272
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.339, naive rule 0.592, lift 2.95x
    - 24h: 55 calls (55 a day), hit rate 0.927, chance 0.297, naive rule 0.509, lift 3.13x
    - 7d: 390 calls (56 a day), hit rate 0.921, chance 0.289, naive rule 0.500, lift 3.19x
    - 30d: 1734 calls (58 a day), hit rate 0.931, chance 0.294, naive rule 0.499, lift 3.17x
  - next: threshold 0.5457, hit rate recent 0.629 / long run 0.616
    - 6h: 16 calls (65 a day), hit rate 0.750, chance 0.339, lift 2.21x
    - 24h: 58 calls (58 a day), hit rate 0.621, chance 0.297, lift 2.09x
    - 7d: 318 calls (45 a day), hit rate 0.619, chance 0.289, lift 2.14x
    - 30d: 2474 calls (82 a day), hit rate 0.600, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 561, 0.501; 0.35: 531, 0.526; 0.40: 474, 0.579; 0.45: 406, 0.649; 0.50: 357, 0.693; 0.55: 310, 0.737; 0.60: 260, 0.783; 0.65: 220, 0.812; 0.70: 171, 0.845; 0.75: 138, 0.875; 0.80: 91, 0.907; 0.85: 46, 0.942; 0.90: 4, 0.970
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.433; 0.35: 494, 0.467; 0.40: 393, 0.506; 0.45: 294, 0.540; 0.50: 187, 0.572; 0.55: 82, 0.586; 0.60: 11, 0.658; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 151712, probability skill vs chance 0.2234, widened contest next: False
  - now: threshold 0.6959, hit rate recent 0.7878 / long run 0.7798
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.200, naive rule 0.455, lift 3.76x
    - 24h: 65 calls (65 a day), hit rate 0.831, chance 0.190, naive rule 0.416, lift 4.37x
    - 7d: 437 calls (62 a day), hit rate 0.751, chance 0.184, naive rule 0.408, lift 4.08x
    - 30d: 1704 calls (57 a day), hit rate 0.798, chance 0.186, naive rule 0.408, lift 4.29x
  - next: threshold 0.4599, hit rate recent 0.5367 / long run 0.5167
    - 6h: 19 calls (78 a day), hit rate 0.526, chance 0.200, lift 2.64x
    - 24h: 61 calls (61 a day), hit rate 0.574, chance 0.190, lift 3.02x
    - 7d: 434 calls (62 a day), hit rate 0.507, chance 0.184, lift 2.76x
    - 30d: 2460 calls (82 a day), hit rate 0.495, chance 0.186, lift 2.66x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 357, 0.476; 0.40: 289, 0.546; 0.45: 234, 0.605; 0.50: 186, 0.653; 0.55: 149, 0.690; 0.60: 112, 0.739; 0.65: 77, 0.776; 0.70: 48, 0.809; 0.75: 28, 0.841; 0.80: 8, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.386; 0.35: 254, 0.425; 0.40: 160, 0.458; 0.45: 64, 0.505; 0.50: 9, 0.564; 0.55: 1, 0.464
- **K=8**: model 1794787200, labels learned 151709, probability skill vs chance 0.2011, widened contest next: True
  - now: threshold 0.5674, hit rate recent 0.6453 / long run 0.6779
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.097, naive rule 0.261, lift 5.61x
    - 24h: 59 calls (59 a day), hit rate 0.661, chance 0.119, naive rule 0.334, lift 5.56x
    - 7d: 370 calls (53 a day), hit rate 0.665, chance 0.123, naive rule 0.351, lift 5.41x
    - 30d: 1549 calls (52 a day), hit rate 0.680, chance 0.121, naive rule 0.339, lift 5.63x
  - next: threshold 0.3717, hit rate recent 0.3866 / long run 0.4205
    - 6h: 18 calls (74 a day), hit rate 0.278, chance 0.097, lift 2.86x
    - 24h: 70 calls (70 a day), hit rate 0.386, chance 0.119, lift 3.24x
    - 7d: 448 calls (64 a day), hit rate 0.433, chance 0.123, lift 3.53x
    - 30d: 2482 calls (83 a day), hit rate 0.405, chance 0.121, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 194, 0.489; 0.40: 153, 0.535; 0.45: 117, 0.580; 0.50: 83, 0.637; 0.55: 59, 0.670; 0.60: 40, 0.710; 0.65: 23, 0.768; 0.70: 11, 0.814; 0.75: 2, 0.766
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 164, 0.369; 0.35: 84, 0.396; 0.40: 24, 0.431; 0.45: 5, 0.453; 0.50: 1, 0.783
- **K=13**: model 1794700800, labels learned 151704, probability skill vs chance 0.1814, widened contest next: True
  - now: threshold 0.4425, hit rate recent 0.6013 / long run 0.5823
    - 6h: 8 calls (33 a day), hit rate 0.375, chance 0.065, naive rule 0.216, lift 5.75x
    - 24h: 44 calls (44 a day), hit rate 0.614, chance 0.078, naive rule 0.296, lift 7.88x
    - 7d: 331 calls (47 a day), hit rate 0.601, chance 0.081, naive rule 0.310, lift 7.45x
    - 30d: 1613 calls (54 a day), hit rate 0.568, chance 0.078, naive rule 0.288, lift 7.29x
  - next: threshold 0.2969, hit rate recent 0.2743 / long run 0.3307
    - 6h: 15 calls (63 a day), hit rate 0.000, chance 0.065, lift 0.00x
    - 24h: 60 calls (61 a day), hit rate 0.267, chance 0.078, lift 3.42x
    - 7d: 432 calls (62 a day), hit rate 0.345, chance 0.081, lift 4.27x
    - 30d: 1844 calls (61 a day), hit rate 0.329, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 135, 0.430; 0.35: 97, 0.476; 0.40: 67, 0.536; 0.45: 46, 0.587; 0.50: 32, 0.629; 0.55: 20, 0.654; 0.60: 11, 0.701; 0.65: 3, 0.641; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.337; 0.35: 13, 0.345; 0.40: 2, 0.432; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.526 | -0.60% | 0.900 | 0.367 | 0.251 | 0.533 | 0.321 |
| 6h | 19.130 | 0.69% | 0.889 | 0.517 | 0.251 | 0.489 | 0.356 |
| 24h | 22.061 | 3.00% | 0.892 | 0.500 | 0.251 | 0.489 | 0.425 |
| 7d | 22.798 | 4.48% | 0.900 | 0.500 | 0.250 | 0.511 | 0.656 |
| 30d | 17.036 | 4.72% | 0.900 | 0.500 | 0.250 | 0.505 | 0.711 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.397 | 21.679 | 21.329 | 21.439 | 21.694 | 21.427 | 21.611 | 21.634 | 21.453 | 21.526 |
| 6h | 19.263 | 19.180 | 19.114 | 19.180 | 19.440 | 19.248 | 19.119 | 19.119 | 19.094 | 19.130 |
| 24h | 22.744 | 22.162 | 22.147 | 22.040 | 22.547 | 22.330 | 22.033 | 22.011 | 22.011 | 22.061 |
| 7d | 23.866 | 23.003 | 22.974 | 22.863 | 23.322 | 23.120 | 22.788 | 22.753 | 22.763 | 22.798 |
| 30d | 17.881 | 17.200 | 17.153 | 17.092 | 17.377 | 17.318 | 17.020 | 16.999 | 17.006 | 17.036 |

## Next candle

- candle starting 2026-11-16 12:40 UTC, last close 1794.57
- P(up) 0.47, return quantiles (bp): {'05': -14.126, '10': -10.611, '25': -6.112, '40': -2.66, '50': -0.685, '60': 1.629, '75': 4.667, '90': 9.672, '95': 13.707}
- changepoint probability 0.0696, regime age 47.0 min
- agent weights: empirical 0.033, ewma 0.131, garch 0.154, har 0.191, bocpd 0.031, hmm 0.071, online_qr 0.191, lgbm 0.199

## Learning log

- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- 2026-11-16 00:00 UTC: {"garch": {"alpha": 0.0649, "beta": 0.9281}, "hmm": {"sd_bp": [5.12, 9.52, 24.14], "stay": [0.982, 0.963, 0.92]}, "lgbm": {"challenger_loss": 0.24944, "champion_loss": 0.2494, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47719, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47655, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3653, "challengers": 1, "chance_loss": 0.4822, "widened": false, "champion_loss": 0.36306, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2714, "challengers": 1, "chance_loss": 0.37579, "widened": false, "champion_loss": 0.27207, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19602, "challengers": 1, "chance_loss": 0.28273, "widened": false, "champion_loss": 0.19594, "promoted": false}}
- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- HMM volatility states (sd, bp per minute): [5.34, 9.7, 24.34], current probabilities: [0.018, 0.943, 0.039]
- live generator: {'versions': 60, 'latest_effective': '2026-11-16 12:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.321, 'l_abs': 0.767, 'l_hi': 0.751, 'l_lo': 0.712, 'b05': 0.779, 'b25': 0.778, 'b75': 0.706, 'b95': 0.755}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.82, 2.189, 2.532, 3.073, 2.818, 3.049, 3.539, 3.472, 4.052, 4.432, 4.282, 4.291, 5.132, 4.446]}
- calibration offsets (in sigma): {'05': -0.0005, '10': 0.029, '25': -0.0425, '40': -0.044, '50': -0.045, '60': -0.006, '75': -0.0575, '90': -0.079, '95': -0.0595}
