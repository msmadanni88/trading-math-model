# ETH-USD 60s candle generator - report

- generated: 2026-11-06 16:11 UTC
- last closed candle: 2026-11-06 16:11 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.482 in the last 7 days, -0.057 against the 7 before
- WIN RATE FALLING: reversal_k3_now 0.914 in the last 7 days, -0.040 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.482 (672) [0.452, 0.509] | 0.511 (2879) [0.493, 0.529] | 0.513 (6234) [0.500, 0.526] | 0.514 (3262) [0.495, 0.532] | 0.500 (64) | 0.500 | down -0.057 (noise 0.027) |
| colour_clear | 0.532 (840) | 0.528 (5492) [0.513, 0.542] | 0.541 (23872) [0.535, 0.546] | 0.520 (51047) [0.514, 0.526] | 0.542 (26809) [0.536, 0.546] | 0.595 (570) | 0.500 | flat -0.011 (noise 0.009) |
| colour_confident | 0.557 (88) | 0.571 (870) [0.558, 0.587] | 0.594 (4276) [0.584, 0.604] | 0.596 (4891) [0.584, 0.608] | 0.596 (4891) [0.584, 0.608] | 0.625 (48) | 0.500 | flat -0.030 (noise 0.022) |
| colour_next | 0.517 (1434) | 0.527 (9979) [0.518, 0.536] | 0.528 (42872) [0.524, 0.531] | 0.515 (92895) [0.511, 0.519] | 0.528 (48546) [0.525, 0.532] | 0.557 (970) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.507 (20076) | 0.504 (139706) [0.502, 0.505] | 0.501 (600208) [0.500, 0.503] | 0.501 (1300530) [0.500, 0.502] | 0.501 (679644) [0.500, 0.502] | 0.501 (13580) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.583 (12) | 0.613 (191) [0.577, 0.640] | 0.630 (1114) [0.611, 0.652] | 0.631 (1283) [0.612, 0.650] | 0.631 (1283) [0.612, 0.650] | 0.750 (8) | 0.500 | flat +0.002 (noise 0.043) |
| reversal_k13_next | 0.318 (66) | 0.360 (369) [0.325, 0.395] | 0.326 (1825) [0.312, 0.340] | 0.313 (4262) [0.302, 0.324] | 0.326 (2157) [0.313, 0.338] | 0.357 (42) | 0.077 | flat +0.041 (noise 0.034) |
| reversal_k13_now | 0.564 (55) | 0.581 (401) [0.546, 0.614] | 0.563 (1650) [0.545, 0.582] | 0.573 (3363) [0.560, 0.587] | 0.567 (1891) [0.547, 0.586] | 0.636 (33) | 0.077 | flat +0.024 (noise 0.035) |
| reversal_k3_next | 0.682 (63) | 0.609 (685) [0.586, 0.634] | 0.586 (3001) [0.575, 0.598] | 0.587 (5803) [0.578, 0.596] | 0.587 (3363) [0.575, 0.598] | 0.611 (36) | 0.293 | flat +0.017 (noise 0.027) |
| reversal_k3_now | 0.915 (59) | 0.914 (407) [0.905, 0.923] | 0.933 (1736) [0.922, 0.943] | 0.936 (3729) [0.930, 0.943] | 0.932 (1966) [0.923, 0.941] | 0.913 (46) | 0.293 | down -0.040 (noise 0.017) |
| reversal_k5_next | 0.574 (61) | 0.543 (396) [0.519, 0.565] | 0.480 (2733) [0.466, 0.496] | 0.484 (5120) [0.472, 0.495] | 0.477 (3130) [0.462, 0.493] | 0.559 (34) | 0.187 | flat +0.036 (noise 0.032) |
| reversal_k5_now | 0.837 (49) | 0.808 (390) [0.796, 0.820] | 0.817 (1624) [0.808, 0.827] | 0.828 (3465) [0.819, 0.837] | 0.820 (1854) [0.810, 0.830] | 0.837 (43) | 0.187 | flat -0.022 (noise 0.027) |
| reversal_k8_next | 0.484 (64) | 0.452 (458) [0.426, 0.478] | 0.392 (2737) [0.379, 0.406] | 0.395 (5170) [0.384, 0.406] | 0.394 (3064) [0.380, 0.407] | 0.452 (42) | 0.121 | flat +0.057 (noise 0.029) |
| reversal_k8_now | 0.717 (46) | 0.690 (358) [0.657, 0.719] | 0.681 (1550) [0.662, 0.700] | 0.701 (3374) [0.687, 0.715] | 0.689 (1787) [0.670, 0.708] | 0.705 (44) | 0.121 | flat +0.002 (noise 0.037) |
| overall | 0.510 (22069) | 0.507 (153821) [0.506, 0.509] | 0.505 (662815) [0.503, 0.506] | 0.504 (1433945) [0.503, 0.505] | 0.505 (750664) [0.503, 0.506] | 0.507 (14934) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07574, 0.1144] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.528, 'levels': [{'threshold': 0.07574, 'calls_per_day': 142.4, 'win_rate': 0.571}, {'threshold': 0.1144, 'calls_per_day': 35.5, 'win_rate': 0.6295}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42874, 'rate': 0.5284}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15204 | 0.343 | 0.527 (14968) | 0.572 (2254) | 0.735 (2580) |
| volatility: normal | 15203 | 0.367 | 0.533 (15134) | 0.608 (1423) | 0.752 (2267) |
| volatility: wild | 15204 | 0.383 | 0.523 (15163) | 0.617 (815) | 0.767 (2125) |
| session: Asia 00-08 | 15360 | 0.365 | 0.535 (15258) | 0.597 (1586) | 0.756 (2290) |
| session: Europe 08-13 | 9600 | 0.360 | 0.535 (9504) | 0.595 (1183) | 0.745 (1559) |
| session: US 13-21 | 15071 | 0.371 | 0.522 (14973) | 0.588 (1151) | 0.753 (2308) |
| session: late 21-24 | 5580 | 0.352 | 0.513 (5530) | 0.575 (572) | 0.741 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.379 | 0.408 | 0.264 | 0.264 | 0.500 | 0.240 | 0.518 | 1.111 |
| 6h | 360 | 0.408 | 0.391 | 0.266 | 0.300 | 0.582 | 0.307 | 0.510 | 1.011 |
| 24h | 1440 | 0.398 | 0.389 | 0.295 | 0.330 | 0.543 | 0.281 | 0.516 | 1.326 |
| 7d | 10080 | 0.362 | 0.358 | 0.275 | 0.305 | 0.529 | 0.260 | 0.464 | 1.264 |
| 30d | 43200 | 0.365 | 0.357 | 0.277 | 0.308 | 0.528 | 0.263 | 0.467 | 1.245 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.379 / 0.500 / 0.933; 2: 0.414 / 0.500 / 0.950; 3: 0.378 / 0.517 / 0.967; 4: 0.378 / 0.467 / 0.950; 5: 0.393 / 0.483 / 0.983; 6: 0.377 / 0.450 / 0.883; 7: 0.399 / 0.483 / 0.983; 8: 0.381 / 0.483 / 0.883; 9: 0.379 / 0.483 / 0.983; 10: 0.405 / 0.567 / 1.000; 11: 0.405 / 0.517 / 1.000; 12: 0.387 / 0.500 / 1.000; 13: 0.373 / 0.433 / 0.983; 14: 0.371 / 0.467 / 1.000; 15: 0.384 / 0.517 / 0.967
- 6h: 1: 0.408 / 0.582 / 0.897; 2: 0.364 / 0.423 / 0.911; 3: 0.382 / 0.526 / 0.903; 4: 0.362 / 0.443 / 0.883; 5: 0.393 / 0.546 / 0.897; 6: 0.360 / 0.457 / 0.772; 7: 0.388 / 0.540 / 0.939; 8: 0.371 / 0.465 / 0.814; 9: 0.382 / 0.524 / 0.947; 10: 0.391 / 0.554 / 0.969; 11: 0.382 / 0.521 / 0.981; 12: 0.363 / 0.462 / 0.942; 13: 0.365 / 0.448 / 0.889; 14: 0.379 / 0.521 / 0.961; 15: 0.371 / 0.501 / 0.889
- 24h: 1: 0.398 / 0.543 / 0.901; 2: 0.374 / 0.457 / 0.908; 3: 0.386 / 0.519 / 0.908; 4: 0.378 / 0.486 / 0.903; 5: 0.383 / 0.505 / 0.912; 6: 0.377 / 0.496 / 0.889; 7: 0.378 / 0.493 / 0.922; 8: 0.377 / 0.495 / 0.901; 9: 0.381 / 0.507 / 0.928; 10: 0.387 / 0.526 / 0.933; 11: 0.378 / 0.509 / 0.936; 12: 0.376 / 0.499 / 0.942; 13: 0.376 / 0.498 / 0.935; 14: 0.379 / 0.519 / 0.947; 15: 0.380 / 0.514 / 0.933
- 7d: 1: 0.362 / 0.529 / 0.896; 2: 0.351 / 0.493 / 0.902; 3: 0.354 / 0.512 / 0.900; 4: 0.351 / 0.500 / 0.899; 5: 0.352 / 0.510 / 0.900; 6: 0.349 / 0.506 / 0.899; 7: 0.349 / 0.498 / 0.902; 8: 0.348 / 0.506 / 0.900; 9: 0.351 / 0.510 / 0.904; 10: 0.348 / 0.498 / 0.903; 11: 0.347 / 0.500 / 0.904; 12: 0.348 / 0.504 / 0.904; 13: 0.349 / 0.503 / 0.902; 14: 0.347 / 0.500 / 0.904; 15: 0.349 / 0.511 / 0.903
- 30d: 1: 0.365 / 0.528 / 0.898; 2: 0.353 / 0.495 / 0.901; 3: 0.356 / 0.509 / 0.900; 4: 0.352 / 0.498 / 0.900; 5: 0.353 / 0.505 / 0.900; 6: 0.351 / 0.501 / 0.899; 7: 0.351 / 0.499 / 0.900; 8: 0.351 / 0.504 / 0.899; 9: 0.350 / 0.501 / 0.900; 10: 0.351 / 0.504 / 0.900; 11: 0.348 / 0.497 / 0.900; 12: 0.350 / 0.502 / 0.900; 13: 0.349 / 0.500 / 0.900; 14: 0.348 / 0.501 / 0.900; 15: 0.349 / 0.503 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.149 (body 0.096, range 0.201); 'price stays where it was' would score 0.150; colour right 0.517; typical miss of the close 17.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.134 (body 0.093, range 0.175); 'price stays where it was' would score 0.129; colour right 0.485; typical miss of the close 13.2 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.126 (body 0.082, range 0.170); 'price stays where it was' would score 0.130; colour right 0.511; typical miss of the close 14.9 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.119 (body 0.081, range 0.158); 'price stays where it was' would score 0.122; colour right 0.502; typical miss of the close 9.0 bp; chain ended on the right side 0.485 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.500; typical miss of the close 8.6 bp; chain ended on the right side 0.513 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.4; 2: 0.200 / 5.2; 3: 0.167 / 6.8; 4: 0.131 / 7.1; 5: 0.125 / 7.8; 6: 0.116 / 8.7; 7: 0.112 / 8.9; 8: 0.099 / 9.9; 9: 0.091 / 9.8; 10: 0.090 / 10.3; 11: 0.086 / 10.4; 12: 0.080 / 10.8; 13: 0.072 / 11.3; 14: 0.071 / 11.7; 15: 0.065 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 137525, probability skill vs chance 0.2299, widened contest next: False
  - now: threshold 0.8381, hit rate recent 0.9148 / long run 0.9281
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.325, naive rule 0.543, lift 2.85x
    - 24h: 68 calls (68 a day), hit rate 0.926, chance 0.315, naive rule 0.525, lift 2.94x
    - 7d: 423 calls (60 a day), hit rate 0.913, chance 0.295, naive rule 0.499, lift 3.09x
    - 30d: 1751 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.566, hit rate recent 0.6284 / long run 0.6065
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.325, lift 1.84x
    - 24h: 55 calls (55 a day), hit rate 0.618, chance 0.315, lift 1.96x
    - 7d: 652 calls (93 a day), hit rate 0.613, chance 0.295, lift 2.08x
    - 30d: 2999 calls (100 a day), hit rate 0.588, chance 0.294, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.498; 0.35: 533, 0.523; 0.40: 474, 0.579; 0.45: 405, 0.650; 0.50: 355, 0.700; 0.55: 309, 0.744; 0.60: 261, 0.788; 0.65: 219, 0.813; 0.70: 173, 0.844; 0.75: 139, 0.876; 0.80: 93, 0.908; 0.85: 47, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.430; 0.35: 499, 0.464; 0.40: 402, 0.500; 0.45: 305, 0.536; 0.50: 197, 0.570; 0.55: 89, 0.577; 0.60: 12, 0.641; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 137523, probability skill vs chance 0.2162, widened contest next: False
  - now: threshold 0.6858, hit rate recent 0.8178 / long run 0.8199
    - 6h: 18 calls (73 a day), hit rate 0.778, chance 0.161, naive rule 0.380, lift 4.82x
    - 24h: 60 calls (60 a day), hit rate 0.850, chance 0.192, naive rule 0.420, lift 4.43x
    - 7d: 400 calls (57 a day), hit rate 0.818, chance 0.188, naive rule 0.411, lift 4.36x
    - 30d: 1633 calls (54 a day), hit rate 0.818, chance 0.187, naive rule 0.406, lift 4.38x
  - next: threshold 0.4534, hit rate recent 0.5506 / long run 0.5175
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.161, lift 3.33x
    - 24h: 51 calls (51 a day), hit rate 0.549, chance 0.192, lift 2.86x
    - 7d: 411 calls (59 a day), hit rate 0.545, chance 0.188, lift 2.91x
    - 30d: 2726 calls (91 a day), hit rate 0.483, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.423; 0.35: 348, 0.489; 0.40: 282, 0.561; 0.45: 231, 0.612; 0.50: 185, 0.663; 0.55: 147, 0.699; 0.60: 112, 0.747; 0.65: 77, 0.786; 0.70: 48, 0.821; 0.75: 29, 0.859; 0.80: 10, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.386; 0.35: 256, 0.422; 0.40: 160, 0.462; 0.45: 67, 0.487; 0.50: 12, 0.504; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 137520, probability skill vs chance 0.214, widened contest next: False
  - now: threshold 0.5665, hit rate recent 0.6917 / long run 0.693
    - 6h: 19 calls (78 a day), hit rate 0.684, chance 0.107, naive rule 0.308, lift 6.39x
    - 24h: 60 calls (60 a day), hit rate 0.717, chance 0.119, naive rule 0.333, lift 6.01x
    - 7d: 369 calls (53 a day), hit rate 0.702, chance 0.122, naive rule 0.346, lift 5.73x
    - 30d: 1554 calls (52 a day), hit rate 0.680, chance 0.120, naive rule 0.335, lift 5.65x
  - next: threshold 0.3588, hit rate recent 0.4517 / long run 0.4262
    - 6h: 19 calls (78 a day), hit rate 0.421, chance 0.107, lift 3.93x
    - 24h: 61 calls (61 a day), hit rate 0.443, chance 0.119, lift 3.71x
    - 7d: 437 calls (62 a day), hit rate 0.465, chance 0.122, lift 3.79x
    - 30d: 2715 calls (91 a day), hit rate 0.394, chance 0.120, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 192, 0.494; 0.40: 152, 0.540; 0.45: 117, 0.588; 0.50: 85, 0.638; 0.55: 60, 0.671; 0.60: 40, 0.705; 0.65: 25, 0.776; 0.70: 12, 0.806; 0.75: 2, 0.768
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.362; 0.35: 90, 0.390; 0.40: 25, 0.418; 0.45: 5, 0.442; 0.50: 1, 0.692
- **K=13**: model 1793577600, labels learned 137515, probability skill vs chance 0.184, widened contest next: False
  - now: threshold 0.4402, hit rate recent 0.5937 / long run 0.572
    - 6h: 15 calls (63 a day), hit rate 0.667, chance 0.083, naive rule 0.287, lift 8.07x
    - 24h: 50 calls (51 a day), hit rate 0.660, chance 0.086, naive rule 0.318, lift 7.71x
    - 7d: 389 calls (56 a day), hit rate 0.591, chance 0.080, naive rule 0.295, lift 7.35x
    - 30d: 1649 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.281, lift 7.26x
  - next: threshold 0.2861, hit rate recent 0.3362 / long run 0.3366
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.083, lift 3.78x
    - 24h: 63 calls (64 a day), hit rate 0.349, chance 0.086, lift 4.08x
    - 7d: 373 calls (53 a day), hit rate 0.370, chance 0.080, lift 4.60x
    - 30d: 1823 calls (61 a day), hit rate 0.326, chance 0.078, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.436; 0.35: 94, 0.486; 0.40: 66, 0.544; 0.45: 45, 0.588; 0.50: 30, 0.644; 0.55: 20, 0.674; 0.60: 11, 0.713; 0.65: 3, 0.684; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.343; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 35.979 | 7.53% | 0.933 | 0.450 | 0.249 | 0.533 | 0.330 |
| 6h | 24.345 | 6.11% | 0.900 | 0.478 | 0.249 | 0.524 | 0.662 |
| 24h | 23.280 | 4.36% | 0.901 | 0.494 | 0.250 | 0.503 | 0.598 |
| 7d | 15.393 | 5.11% | 0.900 | 0.501 | 0.250 | 0.506 | 0.744 |
| 30d | 15.289 | 4.38% | 0.900 | 0.500 | 0.250 | 0.499 | 0.705 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 38.910 | 36.603 | 36.577 | 36.146 | 36.998 | 36.990 | 35.672 | 35.898 | 35.925 | 35.979 |
| 6h | 25.931 | 24.557 | 24.545 | 24.371 | 24.937 | 24.765 | 24.193 | 24.291 | 24.288 | 24.345 |
| 24h | 24.342 | 23.474 | 23.392 | 23.285 | 23.825 | 23.669 | 23.151 | 23.183 | 23.195 | 23.280 |
| 7d | 16.223 | 15.520 | 15.504 | 15.434 | 15.683 | 15.735 | 15.377 | 15.371 | 15.366 | 15.393 |
| 30d | 15.989 | 15.444 | 15.385 | 15.316 | 15.570 | 15.524 | 15.280 | 15.259 | 15.261 | 15.289 |

## Next candle

- candle starting 2026-11-06 16:11 UTC, last close 2219.68
- P(up) 0.5277, return quantiles (bp): {'05': -21.647, '10': -15.787, '25': -8.413, '40': -2.291, '50': 0.856, '60': 3.748, '75': 8.833, '90': 15.793, '95': 20.053}
- changepoint probability 0.0583, regime age 113.0 min
- agent weights: empirical 0.003, ewma 0.058, garch 0.078, har 0.181, bocpd 0.010, hmm 0.017, online_qr 0.390, lgbm 0.264

## Learning log

- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- HMM volatility states (sd, bp per minute): [3.63, 6.36, 16.62], current probabilities: [0.001, 0.462, 0.538]
- live generator: {'versions': 60, 'latest_effective': '2026-11-06 16:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.14, 'l_abs': 0.713, 'l_hi': 0.721, 'l_lo': 0.754, 'b05': 0.731, 'b25': 0.704, 'b75': 0.568, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.193, 1.524, 2.069, 2.015, 4.454, 2.166, 3.826, 2.144, 2.264, 2.241, 2.541, 3.577, 2.493, 3.935]}
- calibration offsets (in sigma): {'05': -0.005, '10': -0.01, '25': -0.045, '40': 0.01, '50': 0.03, '60': 0.04, '75': 0.045, '90': -0.0, '95': -0.045}
