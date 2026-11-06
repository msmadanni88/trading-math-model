# ETH-USD 60s candle generator - report

- generated: 2026-11-06 01:34 UTC
- last closed candle: 2026-11-06 01:34 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.482 in the last 7 days, -0.057 against the 7 before
- WIN RATE FALLING: reversal_k3_now 0.914 in the last 7 days, -0.040 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.482 (672) [0.452, 0.509] | 0.511 (2879) [0.493, 0.529] | 0.513 (6234) [0.500, 0.526] | 0.514 (3262) [0.495, 0.532] | 0.500 (6) | 0.500 | down -0.057 (noise 0.027) |
| colour_clear | 0.532 (840) | 0.528 (5492) [0.513, 0.542] | 0.541 (23872) [0.535, 0.546] | 0.520 (51047) [0.514, 0.526] | 0.542 (26809) [0.536, 0.546] | 0.673 (55) | 0.500 | flat -0.011 (noise 0.009) |
| colour_confident | 0.557 (88) | 0.571 (870) [0.558, 0.587] | 0.594 (4276) [0.584, 0.604] | 0.596 (4891) [0.584, 0.608] | 0.596 (4891) [0.584, 0.608] | 0.667 (3) | 0.500 | flat -0.030 (noise 0.022) |
| colour_next | 0.517 (1434) | 0.527 (9979) [0.518, 0.536] | 0.528 (42872) [0.524, 0.531] | 0.515 (92895) [0.511, 0.519] | 0.528 (48546) [0.525, 0.532] | 0.564 (94) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.507 (20076) | 0.504 (139706) [0.502, 0.505] | 0.501 (600208) [0.500, 0.503] | 0.501 (1300530) [0.500, 0.502] | 0.501 (679644) [0.500, 0.502] | 0.539 (1316) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.583 (12) | 0.613 (191) [0.577, 0.640] | 0.630 (1114) [0.611, 0.652] | 0.631 (1283) [0.612, 0.650] | 0.631 (1283) [0.612, 0.650] | - | 0.500 | flat +0.002 (noise 0.043) |
| reversal_k13_next | 0.318 (66) | 0.360 (369) [0.325, 0.395] | 0.326 (1825) [0.312, 0.340] | 0.313 (4262) [0.302, 0.324] | 0.326 (2157) [0.313, 0.338] | 0.500 (4) | 0.077 | flat +0.041 (noise 0.034) |
| reversal_k13_now | 0.564 (55) | 0.581 (401) [0.546, 0.614] | 0.563 (1650) [0.545, 0.582] | 0.573 (3363) [0.560, 0.587] | 0.567 (1891) [0.547, 0.586] | 0.667 (3) | 0.077 | flat +0.024 (noise 0.035) |
| reversal_k3_next | 0.682 (63) | 0.609 (685) [0.586, 0.634] | 0.586 (3001) [0.575, 0.598] | 0.587 (5803) [0.578, 0.596] | 0.587 (3363) [0.575, 0.598] | 0.667 (9) | 0.293 | flat +0.017 (noise 0.027) |
| reversal_k3_now | 0.915 (59) | 0.914 (407) [0.905, 0.923] | 0.933 (1736) [0.922, 0.943] | 0.936 (3729) [0.930, 0.943] | 0.932 (1966) [0.923, 0.941] | 0.857 (7) | 0.293 | down -0.040 (noise 0.017) |
| reversal_k5_next | 0.574 (61) | 0.543 (396) [0.519, 0.565] | 0.480 (2733) [0.466, 0.496] | 0.484 (5120) [0.472, 0.495] | 0.477 (3130) [0.462, 0.493] | 0.333 (9) | 0.187 | flat +0.036 (noise 0.032) |
| reversal_k5_now | 0.837 (49) | 0.808 (390) [0.796, 0.820] | 0.817 (1624) [0.808, 0.827] | 0.828 (3465) [0.819, 0.837] | 0.820 (1854) [0.810, 0.830] | 1.000 (6) | 0.187 | flat -0.022 (noise 0.027) |
| reversal_k8_next | 0.484 (64) | 0.452 (458) [0.426, 0.478] | 0.392 (2737) [0.379, 0.406] | 0.395 (5170) [0.384, 0.406] | 0.394 (3064) [0.380, 0.407] | 0.500 (4) | 0.121 | flat +0.057 (noise 0.029) |
| reversal_k8_now | 0.717 (46) | 0.690 (358) [0.657, 0.719] | 0.681 (1550) [0.662, 0.700] | 0.701 (3374) [0.687, 0.715] | 0.689 (1787) [0.670, 0.708] | 1.000 (3) | 0.121 | flat +0.002 (noise 0.037) |
| overall | 0.510 (22069) | 0.507 (153821) [0.506, 0.509] | 0.505 (662815) [0.503, 0.506] | 0.504 (1433945) [0.503, 0.505] | 0.505 (750664) [0.503, 0.506] | 0.545 (1461) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07622, 0.115] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5258, 'levels': [{'threshold': 0.07622, 'calls_per_day': 142.3, 'win_rate': 0.5746}, {'threshold': 0.115, 'calls_per_day': 35.4, 'win_rate': 0.632}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42871, 'rate': 0.5279}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14912 | 0.343 | 0.526 (14678) | 0.570 (2218) | 0.735 (2545) |
| volatility: normal | 14911 | 0.367 | 0.533 (14841) | 0.611 (1421) | 0.755 (2197) |
| volatility: wild | 14911 | 0.382 | 0.523 (14870) | 0.614 (808) | 0.764 (2083) |
| session: Asia 00-08 | 14974 | 0.364 | 0.535 (14872) | 0.596 (1566) | 0.755 (2224) |
| session: Europe 08-13 | 9300 | 0.358 | 0.534 (9205) | 0.597 (1165) | 0.742 (1526) |
| session: US 13-21 | 14880 | 0.371 | 0.521 (14782) | 0.587 (1144) | 0.755 (2260) |
| session: late 21-24 | 5580 | 0.352 | 0.513 (5530) | 0.575 (572) | 0.741 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.420 | 0.422 | 0.308 | 0.308 | 0.550 | 0.324 | 0.516 | 1.121 |
| 6h | 360 | 0.397 | 0.386 | 0.306 | 0.341 | 0.529 | 0.285 | 0.508 | 1.278 |
| 24h | 1440 | 0.382 | 0.379 | 0.298 | 0.329 | 0.517 | 0.260 | 0.504 | 1.369 |
| 7d | 10080 | 0.361 | 0.357 | 0.275 | 0.306 | 0.527 | 0.259 | 0.464 | 1.263 |
| 30d | 43200 | 0.364 | 0.357 | 0.277 | 0.308 | 0.528 | 0.262 | 0.466 | 1.243 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.420 / 0.550 / 0.867; 2: 0.405 / 0.550 / 0.967; 3: 0.396 / 0.583 / 0.983; 4: 0.386 / 0.533 / 0.983; 5: 0.413 / 0.567 / 0.967; 6: 0.372 / 0.483 / 1.000; 7: 0.412 / 0.567 / 0.983; 8: 0.418 / 0.667 / 1.000; 9: 0.395 / 0.483 / 0.933; 10: 0.410 / 0.633 / 0.967; 11: 0.402 / 0.600 / 0.983; 12: 0.355 / 0.450 / 1.000; 13: 0.383 / 0.550 / 1.000; 14: 0.381 / 0.550 / 1.000; 15: 0.394 / 0.500 / 1.000
- 6h: 1: 0.397 / 0.529 / 0.897; 2: 0.377 / 0.474 / 0.917; 3: 0.383 / 0.524 / 0.922; 4: 0.393 / 0.549 / 0.942; 5: 0.376 / 0.487 / 0.939; 6: 0.377 / 0.504 / 0.939; 7: 0.377 / 0.485 / 0.958; 8: 0.382 / 0.535 / 0.939; 9: 0.380 / 0.496 / 0.958; 10: 0.388 / 0.532 / 0.978; 11: 0.378 / 0.501 / 0.981; 12: 0.377 / 0.501 / 0.992; 13: 0.379 / 0.524 / 0.994; 14: 0.374 / 0.513 / 0.994; 15: 0.384 / 0.521 / 0.994
- 24h: 1: 0.382 / 0.517 / 0.892; 2: 0.373 / 0.488 / 0.904; 3: 0.378 / 0.521 / 0.908; 4: 0.382 / 0.526 / 0.913; 5: 0.372 / 0.492 / 0.912; 6: 0.376 / 0.513 / 0.903; 7: 0.378 / 0.517 / 0.915; 8: 0.380 / 0.536 / 0.902; 9: 0.378 / 0.521 / 0.917; 10: 0.374 / 0.508 / 0.917; 11: 0.367 / 0.483 / 0.919; 12: 0.369 / 0.507 / 0.911; 13: 0.367 / 0.492 / 0.910; 14: 0.371 / 0.517 / 0.912; 15: 0.369 / 0.505 / 0.912
- 7d: 1: 0.361 / 0.527 / 0.896; 2: 0.351 / 0.495 / 0.900; 3: 0.354 / 0.511 / 0.900; 4: 0.351 / 0.502 / 0.901; 5: 0.351 / 0.508 / 0.900; 6: 0.349 / 0.508 / 0.900; 7: 0.350 / 0.499 / 0.902; 8: 0.348 / 0.509 / 0.901; 9: 0.350 / 0.509 / 0.903; 10: 0.346 / 0.495 / 0.902; 11: 0.347 / 0.498 / 0.903; 12: 0.348 / 0.505 / 0.903; 13: 0.349 / 0.504 / 0.902; 14: 0.347 / 0.500 / 0.902; 15: 0.349 / 0.509 / 0.902
- 30d: 1: 0.364 / 0.528 / 0.898; 2: 0.352 / 0.495 / 0.900; 3: 0.355 / 0.510 / 0.900; 4: 0.352 / 0.499 / 0.900; 5: 0.352 / 0.505 / 0.901; 6: 0.350 / 0.501 / 0.901; 7: 0.350 / 0.499 / 0.901; 8: 0.350 / 0.504 / 0.901; 9: 0.350 / 0.501 / 0.901; 10: 0.350 / 0.503 / 0.901; 11: 0.347 / 0.497 / 0.901; 12: 0.349 / 0.502 / 0.901; 13: 0.348 / 0.500 / 0.901; 14: 0.348 / 0.501 / 0.901; 15: 0.348 / 0.502 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.099 (body 0.059, range 0.138); 'price stays where it was' would score 0.048; colour right 0.533; typical miss of the close 19.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.119 (body 0.076, range 0.161); 'price stays where it was' would score 0.105; colour right 0.507; typical miss of the close 18.5 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.124 (body 0.081, range 0.167); 'price stays where it was' would score 0.125; colour right 0.504; typical miss of the close 13.3 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.121 (body 0.082, range 0.159); 'price stays where it was' would score 0.122; colour right 0.505; typical miss of the close 9.0 bp; chain ended on the right side 0.481 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.6 bp; chain ended on the right side 0.511 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.4; 2: 0.199 / 5.1; 3: 0.168 / 6.7; 4: 0.131 / 7.1; 5: 0.124 / 7.9; 6: 0.115 / 8.7; 7: 0.111 / 8.9; 8: 0.099 / 9.8; 9: 0.091 / 9.8; 10: 0.089 / 10.3; 11: 0.086 / 10.4; 12: 0.079 / 10.8; 13: 0.071 / 11.2; 14: 0.071 / 11.8; 15: 0.064 / 11.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 136648, probability skill vs chance 0.2333, widened contest next: False
  - now: threshold 0.8369, hit rate recent 0.9134 / long run 0.9285
    - 6h: 19 calls (77 a day), hit rate 0.895, chance 0.321, naive rule 0.529, lift 2.79x
    - 24h: 62 calls (62 a day), hit rate 0.903, chance 0.300, naive rule 0.499, lift 3.01x
    - 7d: 410 calls (59 a day), hit rate 0.915, chance 0.293, naive rule 0.497, lift 3.12x
    - 30d: 1742 calls (58 a day), hit rate 0.932, chance 0.293, naive rule 0.494, lift 3.18x
  - next: threshold 0.5652, hit rate recent 0.6492 / long run 0.6072
    - 6h: 21 calls (85 a day), hit rate 0.571, chance 0.321, lift 1.78x
    - 24h: 69 calls (69 a day), hit rate 0.696, chance 0.300, lift 2.32x
    - 7d: 687 calls (98 a day), hit rate 0.608, chance 0.293, lift 2.08x
    - 30d: 3003 calls (100 a day), hit rate 0.587, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.498; 0.35: 533, 0.523; 0.40: 473, 0.579; 0.45: 405, 0.650; 0.50: 354, 0.700; 0.55: 308, 0.744; 0.60: 260, 0.787; 0.65: 218, 0.812; 0.70: 173, 0.843; 0.75: 138, 0.875; 0.80: 92, 0.908; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 499, 0.463; 0.40: 402, 0.499; 0.45: 305, 0.534; 0.50: 197, 0.569; 0.55: 89, 0.574; 0.60: 12, 0.637; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 136646, probability skill vs chance 0.2158, widened contest next: False
  - now: threshold 0.6858, hit rate recent 0.8376 / long run 0.8206
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.201, naive rule 0.412, lift 4.26x
    - 24h: 51 calls (51 a day), hit rate 0.843, chance 0.189, naive rule 0.399, lift 4.47x
    - 7d: 391 calls (56 a day), hit rate 0.813, chance 0.187, naive rule 0.409, lift 4.36x
    - 30d: 1626 calls (54 a day), hit rate 0.818, chance 0.187, naive rule 0.405, lift 4.38x
  - next: threshold 0.4543, hit rate recent 0.5152 / long run 0.5124
    - 6h: 21 calls (86 a day), hit rate 0.381, chance 0.201, lift 1.89x
    - 24h: 68 calls (68 a day), hit rate 0.544, chance 0.189, lift 2.88x
    - 7d: 400 calls (57 a day), hit rate 0.535, chance 0.187, lift 2.87x
    - 30d: 2733 calls (91 a day), hit rate 0.481, chance 0.187, lift 2.57x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.424; 0.35: 347, 0.490; 0.40: 281, 0.562; 0.45: 230, 0.614; 0.50: 184, 0.664; 0.55: 146, 0.700; 0.60: 111, 0.748; 0.65: 76, 0.787; 0.70: 48, 0.821; 0.75: 29, 0.860; 0.80: 10, 0.877
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.385; 0.35: 256, 0.421; 0.40: 160, 0.460; 0.45: 68, 0.484; 0.50: 12, 0.497; 0.55: 1, 0.421
- **K=8**: model 1793059200, labels learned 136643, probability skill vs chance 0.2133, widened contest next: False
  - now: threshold 0.5525, hit rate recent 0.7053 / long run 0.6937
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.104, naive rule 0.273, lift 6.64x
    - 24h: 45 calls (45 a day), hit rate 0.711, chance 0.120, naive rule 0.343, lift 5.93x
    - 7d: 355 calls (51 a day), hit rate 0.699, chance 0.122, naive rule 0.344, lift 5.71x
    - 30d: 1550 calls (52 a day), hit rate 0.682, chance 0.121, naive rule 0.335, lift 5.66x
  - next: threshold 0.3584, hit rate recent 0.4578 / long run 0.4248
    - 6h: 16 calls (66 a day), hit rate 0.375, chance 0.104, lift 3.60x
    - 24h: 65 calls (65 a day), hit rate 0.492, chance 0.120, lift 4.10x
    - 7d: 458 calls (65 a day), hit rate 0.454, chance 0.122, lift 3.72x
    - 30d: 2728 calls (91 a day), hit rate 0.393, chance 0.121, lift 3.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 191, 0.495; 0.40: 151, 0.543; 0.45: 116, 0.591; 0.50: 84, 0.639; 0.55: 60, 0.672; 0.60: 40, 0.707; 0.65: 24, 0.783; 0.70: 12, 0.815; 0.75: 2, 0.779
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.362; 0.35: 90, 0.389; 0.40: 25, 0.414; 0.45: 5, 0.441; 0.50: 1, 0.667
- **K=13**: model 1793577600, labels learned 136638, probability skill vs chance 0.1819, widened contest next: False
  - now: threshold 0.4549, hit rate recent 0.5676 / long run 0.5688
    - 6h: 13 calls (54 a day), hit rate 0.538, chance 0.075, naive rule 0.262, lift 7.14x
    - 24h: 52 calls (53 a day), hit rate 0.558, chance 0.075, naive rule 0.280, lift 7.43x
    - 7d: 397 calls (57 a day), hit rate 0.584, chance 0.079, naive rule 0.288, lift 7.39x
    - 30d: 1649 calls (55 a day), hit rate 0.563, chance 0.077, naive rule 0.281, lift 7.26x
  - next: threshold 0.2862, hit rate recent 0.3317 / long run 0.3362
    - 6h: 18 calls (75 a day), hit rate 0.278, chance 0.075, lift 3.69x
    - 24h: 65 calls (66 a day), hit rate 0.323, chance 0.075, lift 4.30x
    - 7d: 370 calls (53 a day), hit rate 0.365, chance 0.079, lift 4.61x
    - 30d: 1817 calls (61 a day), hit rate 0.326, chance 0.077, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 130, 0.438; 0.35: 94, 0.488; 0.40: 66, 0.545; 0.45: 45, 0.587; 0.50: 30, 0.647; 0.55: 20, 0.679; 0.60: 10, 0.714; 0.65: 3, 0.688; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.338; 0.40: 3, 0.410; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 26.875 | 1.62% | 0.883 | 0.400 | 0.250 | 0.550 | 0.330 |
| 6h | 26.876 | 3.95% | 0.894 | 0.458 | 0.250 | 0.493 | 0.441 |
| 24h | 22.060 | 7.34% | 0.892 | 0.499 | 0.251 | 0.497 | 0.781 |
| 7d | 15.533 | 4.93% | 0.900 | 0.499 | 0.250 | 0.505 | 0.743 |
| 30d | 15.195 | 4.42% | 0.900 | 0.500 | 0.250 | 0.499 | 0.698 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 27.319 | 26.891 | 26.966 | 26.911 | 27.251 | 27.516 | 26.916 | 26.829 | 26.841 | 26.875 |
| 6h | 27.982 | 27.302 | 27.031 | 26.900 | 27.433 | 27.467 | 26.819 | 26.738 | 26.793 | 26.876 |
| 24h | 23.808 | 22.298 | 22.148 | 22.117 | 22.365 | 22.660 | 22.020 | 22.042 | 22.024 | 22.060 |
| 7d | 16.339 | 15.665 | 15.637 | 15.588 | 15.815 | 15.869 | 15.525 | 15.508 | 15.508 | 15.533 |
| 30d | 15.898 | 15.353 | 15.289 | 15.226 | 15.470 | 15.428 | 15.189 | 15.166 | 15.168 | 15.195 |

## Next candle

- candle starting 2026-11-06 01:34 UTC, last close 2238.54
- P(up) 0.4908, return quantiles (bp): {'05': -17.933, '10': -14.172, '25': -7.715, '40': -3.194, '50': -0.197, '60': 1.998, '75': 6.131, '90': 12.748, '95': 16.832}
- changepoint probability 0.0496, regime age 45.6 min
- agent weights: empirical 0.003, ewma 0.034, garch 0.126, har 0.168, bocpd 0.021, hmm 0.006, online_qr 0.330, lgbm 0.314

## Learning log

- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.92, 5.43, 14.8], current probabilities: [0.0, 0.003, 0.997]
- live generator: {'versions': 60, 'latest_effective': '2026-11-06 01:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.415, 'l_abs': 0.709, 'l_hi': 0.728, 'l_lo': 0.78, 'b05': 0.748, 'b25': 0.703, 'b75': 0.567, 'b95': 0.702}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.449, 1.641, 1.753, 2.003, 2.632, 1.988, 3.176, 2.218, 2.251, 2.413, 2.905, 3.282, 3.214, 3.47]}
- calibration offsets (in sigma): {'05': -0.0435, '10': -0.077, '25': -0.0475, '40': -0.028, '50': 0.025, '60': 0.028, '75': 0.0275, '90': -0.013, '95': -0.0365}
