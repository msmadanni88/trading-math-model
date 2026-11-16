# ETH-USD 60s candle generator - report

- generated: 2026-11-16 22:32 UTC
- last closed candle: 2026-11-16 22:32 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: colour_confident 0.530 in the last 7 days, -0.051 against the 7 before
- WIN RATE FALLING: reversal_k5_now 0.743 in the last 7 days, -0.065 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.522 (671) [0.482, 0.560] | 0.518 (2879) [0.501, 0.536] | 0.514 (7193) [0.502, 0.525] | 0.515 (4221) [0.500, 0.531] | 0.589 (90) | 0.500 | flat +0.022 (noise 0.030) |
| colour_clear | 0.549 (780) | 0.539 (5614) [0.531, 0.547] | 0.543 (23916) [0.538, 0.549] | 0.524 (58973) [0.519, 0.529] | 0.543 (34735) [0.538, 0.547] | 0.532 (770) | 0.500 | flat +0.003 (noise 0.012) |
| colour_confident | 0.512 (207) | 0.530 (606) [0.505, 0.566] | 0.582 (4371) [0.570, 0.593] | 0.588 (6151) [0.577, 0.599] | 0.588 (6151) [0.577, 0.599] | 0.565 (223) | 0.500 | down -0.051 (noise 0.025) |
| colour_next | 0.540 (1436) | 0.529 (10053) [0.521, 0.536] | 0.531 (42875) [0.527, 0.535] | 0.518 (107177) [0.514, 0.522] | 0.530 (62828) [0.526, 0.533] | 0.529 (1345) | 0.500 | flat -0.003 (noise 0.009) |
| colour_path | 0.505 (20104) | 0.502 (140742) [0.499, 0.504] | 0.501 (600250) [0.500, 0.503] | 0.501 (1500478) [0.500, 0.502] | 0.501 (879592) [0.500, 0.502] | 0.502 (18830) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.589 (56) | 0.579 (107) [0.500, 0.632] | 0.615 (1133) [0.600, 0.631] | 0.627 (1598) [0.611, 0.643] | 0.627 (1598) [0.611, 0.643] | 0.553 (76) | 0.500 | flat -0.043 (noise 0.056) |
| reversal_k13_next | 0.302 (63) | 0.352 (438) [0.323, 0.384] | 0.333 (1832) [0.318, 0.349] | 0.316 (4922) [0.306, 0.326] | 0.328 (2817) [0.317, 0.339] | 0.304 (69) | 0.077 | flat +0.017 (noise 0.032) |
| reversal_k13_now | 0.633 (49) | 0.604 (338) [0.560, 0.655] | 0.570 (1624) [0.549, 0.591] | 0.576 (3855) [0.563, 0.588] | 0.572 (2383) [0.556, 0.589] | 0.553 (38) | 0.077 | flat +0.039 (noise 0.037) |
| reversal_k3_next | 0.571 (35) | 0.623 (300) [0.580, 0.673] | 0.600 (2515) [0.588, 0.613] | 0.590 (6264) [0.581, 0.598] | 0.591 (3824) [0.580, 0.602] | 0.595 (74) | 0.293 | flat -0.000 (noise 0.036) |
| reversal_k3_now | 0.933 (45) | 0.924 (396) [0.914, 0.935] | 0.929 (1740) [0.920, 0.939] | 0.935 (4304) [0.929, 0.941] | 0.930 (2541) [0.923, 0.938] | 0.941 (51) | 0.293 | flat +0.007 (noise 0.019) |
| reversal_k5_next | 0.456 (57) | 0.506 (415) [0.461, 0.557] | 0.494 (2491) [0.477, 0.512] | 0.487 (5716) [0.476, 0.498] | 0.483 (3726) [0.469, 0.498] | 0.524 (63) | 0.187 | flat -0.024 (noise 0.035) |
| reversal_k5_now | 0.809 (63) | 0.743 (432) [0.701, 0.783] | 0.798 (1701) [0.782, 0.813] | 0.818 (4059) [0.808, 0.828] | 0.806 (2448) [0.792, 0.818] | 0.746 (59) | 0.187 | down -0.065 (noise 0.029) |
| reversal_k8_next | 0.353 (68) | 0.438 (450) [0.401, 0.479] | 0.406 (2507) [0.392, 0.421] | 0.398 (5817) [0.388, 0.408] | 0.399 (3711) [0.386, 0.411] | 0.379 (66) | 0.121 | flat +0.022 (noise 0.034) |
| reversal_k8_now | 0.603 (58) | 0.667 (372) [0.627, 0.720] | 0.683 (1548) [0.662, 0.702] | 0.698 (3906) [0.684, 0.711] | 0.686 (2319) [0.669, 0.703] | 0.588 (51) | 0.122 | flat -0.022 (noise 0.035) |
| overall | 0.508 (22074) | 0.506 (154607) [0.504, 0.508] | 0.505 (661962) [0.504, 0.507] | 0.504 (1653691) [0.503, 0.505] | 0.505 (970410) [0.504, 0.506] | 0.506 (20736) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06425, 0.09361] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5312, 'levels': [{'threshold': 0.06425, 'calls_per_day': 146.6, 'win_rate': 0.5491}, {'threshold': 0.09361, 'calls_per_day': 37.9, 'win_rate': 0.5639}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42890, 'rate': 0.5308}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15331 | 0.347 | 0.534 (15094) | 0.564 (2310) | 0.740 (2567) |
| volatility: normal | 15330 | 0.373 | 0.531 (15269) | 0.610 (1373) | 0.745 (2344) |
| volatility: wild | 15331 | 0.388 | 0.529 (15290) | 0.584 (999) | 0.764 (2153) |
| session: Asia 00-08 | 15360 | 0.369 | 0.534 (15238) | 0.582 (1641) | 0.749 (2302) |
| session: Europe 08-13 | 9600 | 0.362 | 0.530 (9517) | 0.585 (1154) | 0.746 (1568) |
| session: US 13-21 | 15360 | 0.377 | 0.533 (15261) | 0.600 (1291) | 0.754 (2354) |
| session: late 21-24 | 5672 | 0.363 | 0.516 (5637) | 0.535 (596) | 0.744 (840) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.341 | 0.379 | 0.305 | 0.305 | 0.467 | 0.230 | 0.452 | 0.877 |
| 6h | 360 | 0.368 | 0.384 | 0.295 | 0.337 | 0.478 | 0.240 | 0.496 | 1.161 |
| 24h | 1440 | 0.385 | 0.380 | 0.312 | 0.355 | 0.528 | 0.267 | 0.504 | 1.178 |
| 7d | 10080 | 0.383 | 0.378 | 0.298 | 0.329 | 0.529 | 0.271 | 0.495 | 1.174 |
| 30d | 43200 | 0.370 | 0.363 | 0.281 | 0.313 | 0.531 | 0.266 | 0.474 | 1.243 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.341 / 0.467 / 0.833; 2: 0.354 / 0.500 / 0.933; 3: 0.320 / 0.417 / 0.933; 4: 0.327 / 0.433 / 0.967; 5: 0.362 / 0.583 / 0.983; 6: 0.331 / 0.417 / 0.933; 7: 0.353 / 0.550 / 0.950; 8: 0.315 / 0.400 / 1.000; 9: 0.314 / 0.467 / 0.983; 10: 0.319 / 0.350 / 0.983; 11: 0.322 / 0.417 / 1.000; 12: 0.360 / 0.617 / 0.967; 13: 0.337 / 0.450 / 0.967; 14: 0.340 / 0.483 / 1.000; 15: 0.344 / 0.517 / 0.900
- 6h: 1: 0.368 / 0.478 / 0.897; 2: 0.363 / 0.461 / 0.953; 3: 0.370 / 0.494 / 0.950; 4: 0.371 / 0.489 / 0.958; 5: 0.368 / 0.492 / 0.978; 6: 0.367 / 0.492 / 0.950; 7: 0.371 / 0.506 / 0.947; 8: 0.372 / 0.506 / 0.972; 9: 0.347 / 0.425 / 0.961; 10: 0.378 / 0.511 / 0.983; 11: 0.369 / 0.494 / 0.989; 12: 0.368 / 0.508 / 0.978; 13: 0.374 / 0.525 / 0.975; 14: 0.369 / 0.492 / 0.983; 15: 0.376 / 0.517 / 0.950
- 24h: 1: 0.385 / 0.528 / 0.897; 2: 0.373 / 0.479 / 0.911; 3: 0.385 / 0.517 / 0.908; 4: 0.376 / 0.495 / 0.908; 5: 0.373 / 0.486 / 0.915; 6: 0.379 / 0.523 / 0.911; 7: 0.377 / 0.510 / 0.912; 8: 0.378 / 0.504 / 0.912; 9: 0.370 / 0.488 / 0.912; 10: 0.380 / 0.507 / 0.915; 11: 0.376 / 0.505 / 0.915; 12: 0.378 / 0.515 / 0.919; 13: 0.375 / 0.503 / 0.917; 14: 0.377 / 0.502 / 0.915; 15: 0.377 / 0.509 / 0.908
- 7d: 1: 0.383 / 0.529 / 0.899; 2: 0.367 / 0.485 / 0.900; 3: 0.376 / 0.515 / 0.900; 4: 0.368 / 0.493 / 0.901; 5: 0.369 / 0.498 / 0.901; 6: 0.369 / 0.502 / 0.900; 7: 0.370 / 0.504 / 0.900; 8: 0.371 / 0.510 / 0.901; 9: 0.365 / 0.494 / 0.900; 10: 0.370 / 0.504 / 0.900; 11: 0.370 / 0.513 / 0.900; 12: 0.367 / 0.500 / 0.900; 13: 0.368 / 0.507 / 0.900; 14: 0.366 / 0.500 / 0.899; 15: 0.367 / 0.501 / 0.898
- 30d: 1: 0.370 / 0.531 / 0.898; 2: 0.356 / 0.492 / 0.900; 3: 0.361 / 0.512 / 0.900; 4: 0.356 / 0.497 / 0.901; 5: 0.356 / 0.503 / 0.901; 6: 0.355 / 0.501 / 0.900; 7: 0.355 / 0.499 / 0.900; 8: 0.356 / 0.507 / 0.900; 9: 0.354 / 0.501 / 0.900; 10: 0.355 / 0.503 / 0.900; 11: 0.354 / 0.505 / 0.900; 12: 0.354 / 0.503 / 0.900; 13: 0.353 / 0.499 / 0.900; 14: 0.353 / 0.502 / 0.900; 15: 0.353 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.119 (body 0.081, range 0.157); 'price stays where it was' would score 0.076; colour right 0.367; typical miss of the close 13.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.157 (body 0.109, range 0.205); 'price stays where it was' would score 0.136; colour right 0.500; typical miss of the close 12.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.124 (body 0.079, range 0.169); 'price stays where it was' would score 0.129; colour right 0.507; typical miss of the close 15.3 bp; chain ended on the right side 0.594 of 96 chains; n=1440
- 7d: match 0.125 (body 0.083, range 0.168); 'price stays where it was' would score 0.128; colour right 0.505; typical miss of the close 13.7 bp; chain ended on the right side 0.520 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.5 bp; chain ended on the right side 0.521 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.0; 2: 0.203 / 5.8; 3: 0.167 / 7.7; 4: 0.133 / 7.9; 5: 0.125 / 8.6; 6: 0.118 / 9.5; 7: 0.111 / 9.8; 8: 0.100 / 10.6; 9: 0.092 / 10.9; 10: 0.091 / 11.3; 11: 0.086 / 11.6; 12: 0.078 / 12.0; 13: 0.073 / 12.6; 14: 0.068 / 13.0; 15: 0.068 / 13.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 152306, probability skill vs chance 0.2334, widened contest next: False
  - now: threshold 0.8365, hit rate recent 0.9401 / long run 0.9284
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.275, naive rule 0.505, lift 3.36x
    - 24h: 55 calls (55 a day), hit rate 0.945, chance 0.292, naive rule 0.506, lift 3.23x
    - 7d: 396 calls (57 a day), hit rate 0.924, chance 0.288, naive rule 0.500, lift 3.20x
    - 30d: 1731 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.499, lift 3.17x
  - next: threshold 0.5448, hit rate recent 0.6038 / long run 0.6144
    - 6h: 26 calls (105 a day), hit rate 0.577, chance 0.275, lift 2.10x
    - 24h: 77 calls (77 a day), hit rate 0.584, chance 0.292, lift 2.00x
    - 7d: 336 calls (48 a day), hit rate 0.616, chance 0.288, lift 2.14x
    - 30d: 2476 calls (83 a day), hit rate 0.601, chance 0.294, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 561, 0.501; 0.35: 531, 0.526; 0.40: 474, 0.579; 0.45: 406, 0.649; 0.50: 358, 0.693; 0.55: 310, 0.737; 0.60: 260, 0.783; 0.65: 220, 0.811; 0.70: 172, 0.844; 0.75: 138, 0.874; 0.80: 91, 0.907; 0.85: 45, 0.942; 0.90: 4, 0.970
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.433; 0.35: 494, 0.467; 0.40: 392, 0.506; 0.45: 294, 0.540; 0.50: 186, 0.573; 0.55: 81, 0.587; 0.60: 11, 0.657; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 152304, probability skill vs chance 0.2234, widened contest next: False
  - now: threshold 0.6971, hit rate recent 0.7713 / long run 0.7779
    - 6h: 18 calls (73 a day), hit rate 0.778, chance 0.193, naive rule 0.435, lift 4.04x
    - 24h: 65 calls (65 a day), hit rate 0.754, chance 0.185, naive rule 0.407, lift 4.08x
    - 7d: 455 calls (65 a day), hit rate 0.752, chance 0.183, naive rule 0.407, lift 4.10x
    - 30d: 1708 calls (57 a day), hit rate 0.796, chance 0.186, naive rule 0.408, lift 4.28x
  - next: threshold 0.4609, hit rate recent 0.5193 / long run 0.516
    - 6h: 16 calls (65 a day), hit rate 0.438, chance 0.193, lift 2.27x
    - 24h: 67 calls (67 a day), hit rate 0.537, chance 0.185, lift 2.91x
    - 7d: 444 calls (63 a day), hit rate 0.507, chance 0.183, lift 2.76x
    - 30d: 2420 calls (81 a day), hit rate 0.496, chance 0.186, lift 2.67x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 358, 0.475; 0.40: 289, 0.545; 0.45: 235, 0.604; 0.50: 187, 0.651; 0.55: 149, 0.688; 0.60: 113, 0.736; 0.65: 77, 0.773; 0.70: 48, 0.807; 0.75: 27, 0.840; 0.80: 8, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 253, 0.425; 0.40: 160, 0.459; 0.45: 64, 0.509; 0.50: 9, 0.566; 0.55: 1, 0.462
- **K=8**: model 1794787200, labels learned 152301, probability skill vs chance 0.1992, widened contest next: True
  - now: threshold 0.5674, hit rate recent 0.6192 / long run 0.6736
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.124, naive rule 0.320, lift 4.02x
    - 24h: 56 calls (56 a day), hit rate 0.607, chance 0.123, naive rule 0.334, lift 4.95x
    - 7d: 378 calls (54 a day), hit rate 0.659, chance 0.123, naive rule 0.350, lift 5.34x
    - 30d: 1550 calls (52 a day), hit rate 0.677, chance 0.121, naive rule 0.338, lift 5.61x
  - next: threshold 0.3658, hit rate recent 0.3864 / long run 0.4192
    - 6h: 19 calls (78 a day), hit rate 0.368, chance 0.124, lift 2.96x
    - 24h: 71 calls (71 a day), hit rate 0.394, chance 0.123, lift 3.21x
    - 7d: 452 calls (65 a day), hit rate 0.427, chance 0.123, lift 3.46x
    - 30d: 2461 calls (82 a day), hit rate 0.406, chance 0.121, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 249, 0.426; 0.35: 195, 0.488; 0.40: 154, 0.533; 0.45: 118, 0.578; 0.50: 83, 0.634; 0.55: 59, 0.666; 0.60: 39, 0.707; 0.65: 23, 0.766; 0.70: 10, 0.813; 0.75: 2, 0.770
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 164, 0.369; 0.35: 84, 0.398; 0.40: 23, 0.433; 0.45: 5, 0.460; 0.50: 1, 0.783
- **K=13**: model 1794700800, labels learned 152296, probability skill vs chance 0.178, widened contest next: False
  - now: threshold 0.4422, hit rate recent 0.6076 / long run 0.5842
    - 6h: 13 calls (54 a day), hit rate 0.538, chance 0.080, naive rule 0.267, lift 6.76x
    - 24h: 44 calls (44 a day), hit rate 0.591, chance 0.079, naive rule 0.282, lift 7.45x
    - 7d: 337 calls (48 a day), hit rate 0.608, chance 0.080, naive rule 0.307, lift 7.57x
    - 30d: 1609 calls (54 a day), hit rate 0.569, chance 0.078, naive rule 0.287, lift 7.29x
  - next: threshold 0.2972, hit rate recent 0.3273 / long run 0.335
    - 6h: 22 calls (92 a day), hit rate 0.364, chance 0.080, lift 4.56x
    - 24h: 75 calls (76 a day), hit rate 0.333, chance 0.079, lift 4.20x
    - 7d: 444 calls (64 a day), hit rate 0.342, chance 0.080, lift 4.26x
    - 30d: 1858 calls (62 a day), hit rate 0.332, chance 0.078, lift 4.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 135, 0.430; 0.35: 98, 0.476; 0.40: 67, 0.535; 0.45: 46, 0.588; 0.50: 32, 0.630; 0.55: 20, 0.656; 0.60: 11, 0.700; 0.65: 3, 0.644; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.341; 0.35: 13, 0.348; 0.40: 2, 0.431; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.896 | 2.11% | 0.867 | 0.417 | 0.250 | 0.533 | 0.077 |
| 6h | 19.905 | 1.05% | 0.906 | 0.486 | 0.250 | 0.514 | 0.279 |
| 24h | 23.526 | 2.09% | 0.890 | 0.494 | 0.251 | 0.498 | 0.598 |
| 7d | 23.180 | 4.47% | 0.899 | 0.500 | 0.250 | 0.512 | 0.658 |
| 30d | 17.213 | 4.67% | 0.900 | 0.500 | 0.250 | 0.505 | 0.712 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.260 | 17.033 | 16.970 | 16.906 | 16.802 | 17.012 | 17.055 | 16.947 | 16.933 | 16.896 |
| 6h | 20.116 | 20.018 | 19.950 | 19.940 | 20.190 | 20.110 | 19.864 | 19.869 | 19.883 | 19.905 |
| 24h | 24.030 | 23.603 | 23.551 | 23.473 | 23.973 | 23.748 | 23.522 | 23.504 | 23.479 | 23.526 |
| 7d | 24.266 | 23.383 | 23.349 | 23.225 | 23.713 | 23.502 | 23.173 | 23.138 | 23.146 | 23.180 |
| 30d | 18.056 | 17.375 | 17.331 | 17.267 | 17.558 | 17.497 | 17.197 | 17.175 | 17.182 | 17.213 |

## Next candle

- candle starting 2026-11-16 22:32 UTC, last close 1830.59
- P(up) 0.5272, return quantiles (bp): {'05': -9.482, '10': -6.841, '25': -3.527, '40': -1.2, '50': 0.439, '60': 1.502, '75': 3.836, '90': 7.851, '95': 9.959}
- changepoint probability 0.0438, regime age 169.7 min
- agent weights: empirical 0.010, ewma 0.117, garch 0.152, har 0.219, bocpd 0.026, hmm 0.065, online_qr 0.196, lgbm 0.213

## Learning log

- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- 2026-11-16 00:00 UTC: {"garch": {"alpha": 0.0649, "beta": 0.9281}, "hmm": {"sd_bp": [5.12, 9.52, 24.14], "stay": [0.982, 0.963, 0.92]}, "lgbm": {"challenger_loss": 0.24944, "champion_loss": 0.2494, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47719, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47655, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3653, "challengers": 1, "chance_loss": 0.4822, "widened": false, "champion_loss": 0.36306, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2714, "challengers": 1, "chance_loss": 0.37579, "widened": false, "champion_loss": 0.27207, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19602, "challengers": 1, "chance_loss": 0.28273, "widened": false, "champion_loss": 0.19594, "promoted": false}}
- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- HMM volatility states (sd, bp per minute): [5.34, 9.7, 24.34], current probabilities: [0.922, 0.074, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-11-16 22:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.197, 'l_abs': 0.766, 'l_hi': 0.731, 'l_lo': 0.718, 'b05': 0.753, 'b25': 0.8, 'b75': 0.671, 'b95': 0.733}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6]], 'cone_width': [1.144, 1.521, 1.691, 1.68, 2.208, 2.487, 2.316, 2.72, 2.652, 2.678, 2.976, 3.103, 3.359, 4.609]}
- calibration offsets (in sigma): {'05': 0.0355, '10': 0.071, '25': 0.0475, '40': 0.034, '50': 0.085, '60': 0.046, '75': 0.0425, '90': 0.089, '95': 0.0145}
