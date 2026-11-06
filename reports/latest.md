# ETH-USD 60s candle generator - report

- generated: 2026-11-06 08:29 UTC
- last closed candle: 2026-11-06 08:29 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.482 in the last 7 days, -0.057 against the 7 before
- WIN RATE FALLING: reversal_k3_now 0.914 in the last 7 days, -0.040 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.482 (672) [0.452, 0.509] | 0.511 (2879) [0.493, 0.529] | 0.513 (6234) [0.500, 0.526] | 0.514 (3262) [0.495, 0.532] | 0.394 (33) | 0.500 | down -0.057 (noise 0.027) |
| colour_clear | 0.532 (840) | 0.528 (5492) [0.513, 0.542] | 0.541 (23872) [0.535, 0.546] | 0.520 (51047) [0.514, 0.526] | 0.542 (26809) [0.536, 0.546] | 0.606 (289) | 0.500 | flat -0.011 (noise 0.009) |
| colour_confident | 0.557 (88) | 0.571 (870) [0.558, 0.587] | 0.594 (4276) [0.584, 0.604] | 0.596 (4891) [0.584, 0.608] | 0.596 (4891) [0.584, 0.608] | 0.652 (23) | 0.500 | flat -0.030 (noise 0.022) |
| colour_next | 0.517 (1434) | 0.527 (9979) [0.518, 0.536] | 0.528 (42872) [0.524, 0.531] | 0.515 (92895) [0.511, 0.519] | 0.528 (48546) [0.525, 0.532] | 0.550 (509) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.507 (20076) | 0.504 (139706) [0.502, 0.505] | 0.501 (600208) [0.500, 0.503] | 0.501 (1300530) [0.500, 0.502] | 0.501 (679644) [0.500, 0.502] | 0.504 (7126) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.583 (12) | 0.613 (191) [0.577, 0.640] | 0.630 (1114) [0.611, 0.652] | 0.631 (1283) [0.612, 0.650] | 0.631 (1283) [0.612, 0.650] | 1.000 (3) | 0.500 | flat +0.002 (noise 0.043) |
| reversal_k13_next | 0.318 (66) | 0.360 (369) [0.325, 0.395] | 0.326 (1825) [0.312, 0.340] | 0.313 (4262) [0.302, 0.324] | 0.326 (2157) [0.313, 0.338] | 0.389 (18) | 0.077 | flat +0.041 (noise 0.034) |
| reversal_k13_now | 0.564 (55) | 0.581 (401) [0.546, 0.614] | 0.563 (1650) [0.545, 0.582] | 0.573 (3363) [0.560, 0.587] | 0.567 (1891) [0.547, 0.586] | 0.647 (17) | 0.077 | flat +0.024 (noise 0.035) |
| reversal_k3_next | 0.682 (63) | 0.609 (685) [0.586, 0.634] | 0.586 (3001) [0.575, 0.598] | 0.587 (5803) [0.578, 0.596] | 0.587 (3363) [0.575, 0.598] | 0.652 (23) | 0.293 | flat +0.017 (noise 0.027) |
| reversal_k3_now | 0.915 (59) | 0.914 (407) [0.905, 0.923] | 0.933 (1736) [0.922, 0.943] | 0.936 (3729) [0.930, 0.943] | 0.932 (1966) [0.923, 0.941] | 0.929 (28) | 0.293 | down -0.040 (noise 0.017) |
| reversal_k5_next | 0.574 (61) | 0.543 (396) [0.519, 0.565] | 0.480 (2733) [0.466, 0.496] | 0.484 (5120) [0.472, 0.495] | 0.477 (3130) [0.462, 0.493] | 0.611 (18) | 0.187 | flat +0.036 (noise 0.032) |
| reversal_k5_now | 0.837 (49) | 0.808 (390) [0.796, 0.820] | 0.817 (1624) [0.808, 0.827] | 0.828 (3465) [0.819, 0.837] | 0.820 (1854) [0.810, 0.830] | 0.913 (23) | 0.187 | flat -0.022 (noise 0.027) |
| reversal_k8_next | 0.484 (64) | 0.452 (458) [0.426, 0.478] | 0.392 (2737) [0.379, 0.406] | 0.395 (5170) [0.384, 0.406] | 0.394 (3064) [0.380, 0.407] | 0.444 (18) | 0.121 | flat +0.057 (noise 0.029) |
| reversal_k8_now | 0.717 (46) | 0.690 (358) [0.657, 0.719] | 0.681 (1550) [0.662, 0.700] | 0.701 (3374) [0.687, 0.715] | 0.689 (1787) [0.670, 0.708] | 0.727 (22) | 0.121 | flat +0.002 (noise 0.037) |
| overall | 0.510 (22069) | 0.507 (153821) [0.506, 0.509] | 0.505 (662815) [0.503, 0.506] | 0.504 (1433945) [0.503, 0.505] | 0.505 (750664) [0.503, 0.506] | 0.510 (7835) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07594, 0.1147] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5277, 'levels': [{'threshold': 0.07594, 'calls_per_day': 142.3, 'win_rate': 0.5746}, {'threshold': 0.1147, 'calls_per_day': 35.4, 'win_rate': 0.636}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42874, 'rate': 0.528}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15050 | 0.343 | 0.527 (14815) | 0.572 (2236) | 0.736 (2563) |
| volatility: normal | 15049 | 0.367 | 0.533 (14979) | 0.608 (1422) | 0.753 (2231) |
| volatility: wild | 15050 | 0.383 | 0.523 (15010) | 0.617 (809) | 0.767 (2102) |
| session: Asia 00-08 | 15360 | 0.365 | 0.535 (15258) | 0.597 (1586) | 0.756 (2290) |
| session: Europe 08-13 | 9329 | 0.358 | 0.534 (9234) | 0.597 (1165) | 0.743 (1531) |
| session: US 13-21 | 14880 | 0.371 | 0.521 (14782) | 0.587 (1144) | 0.755 (2260) |
| session: late 21-24 | 5580 | 0.352 | 0.513 (5530) | 0.575 (572) | 0.741 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.421 | 0.419 | 0.311 | 0.311 | 0.567 | 0.292 | 0.551 | 1.509 |
| 6h | 360 | 0.395 | 0.394 | 0.320 | 0.349 | 0.533 | 0.267 | 0.524 | 1.245 |
| 24h | 1440 | 0.387 | 0.384 | 0.299 | 0.331 | 0.524 | 0.264 | 0.511 | 1.350 |
| 7d | 10080 | 0.362 | 0.358 | 0.276 | 0.305 | 0.527 | 0.259 | 0.464 | 1.264 |
| 30d | 43200 | 0.365 | 0.357 | 0.277 | 0.308 | 0.528 | 0.262 | 0.467 | 1.244 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.421 / 0.567 / 0.900; 2: 0.374 / 0.433 / 0.917; 3: 0.412 / 0.583 / 0.933; 4: 0.396 / 0.533 / 0.900; 5: 0.404 / 0.567 / 0.883; 6: 0.416 / 0.600 / 0.900; 7: 0.374 / 0.450 / 0.817; 8: 0.394 / 0.517 / 0.867; 9: 0.371 / 0.483 / 0.783; 10: 0.374 / 0.417 / 0.733; 11: 0.361 / 0.433 / 0.750; 12: 0.372 / 0.483 / 0.767; 13: 0.358 / 0.417 / 0.783; 14: 0.379 / 0.517 / 0.767; 15: 0.373 / 0.483 / 0.750
- 6h: 1: 0.395 / 0.533 / 0.900; 2: 0.382 / 0.483 / 0.903; 3: 0.385 / 0.494 / 0.889; 4: 0.379 / 0.478 / 0.881; 5: 0.382 / 0.497 / 0.894; 6: 0.385 / 0.522 / 0.947; 7: 0.372 / 0.458 / 0.844; 8: 0.373 / 0.464 / 0.944; 9: 0.382 / 0.494 / 0.842; 10: 0.383 / 0.500 / 0.822; 11: 0.373 / 0.508 / 0.806; 12: 0.386 / 0.514 / 0.867; 13: 0.388 / 0.525 / 0.897; 14: 0.383 / 0.517 / 0.869; 15: 0.385 / 0.514 / 0.897
- 24h: 1: 0.387 / 0.524 / 0.894; 2: 0.374 / 0.480 / 0.910; 3: 0.381 / 0.516 / 0.910; 4: 0.381 / 0.514 / 0.912; 5: 0.374 / 0.491 / 0.905; 6: 0.379 / 0.515 / 0.916; 7: 0.372 / 0.489 / 0.901; 8: 0.378 / 0.517 / 0.915; 9: 0.376 / 0.506 / 0.906; 10: 0.376 / 0.504 / 0.903; 11: 0.369 / 0.494 / 0.899; 12: 0.372 / 0.502 / 0.910; 13: 0.372 / 0.502 / 0.919; 14: 0.374 / 0.514 / 0.912; 15: 0.373 / 0.507 / 0.920
- 7d: 1: 0.362 / 0.527 / 0.895; 2: 0.351 / 0.495 / 0.900; 3: 0.354 / 0.512 / 0.902; 4: 0.351 / 0.502 / 0.901; 5: 0.352 / 0.509 / 0.900; 6: 0.350 / 0.509 / 0.901; 7: 0.349 / 0.497 / 0.899; 8: 0.348 / 0.507 / 0.901; 9: 0.351 / 0.510 / 0.899; 10: 0.347 / 0.495 / 0.899; 11: 0.347 / 0.498 / 0.898; 12: 0.349 / 0.506 / 0.899; 13: 0.349 / 0.505 / 0.900; 14: 0.347 / 0.500 / 0.899; 15: 0.349 / 0.511 / 0.900
- 30d: 1: 0.365 / 0.528 / 0.898; 2: 0.353 / 0.495 / 0.900; 3: 0.356 / 0.510 / 0.900; 4: 0.352 / 0.498 / 0.900; 5: 0.352 / 0.505 / 0.900; 6: 0.351 / 0.501 / 0.901; 7: 0.351 / 0.499 / 0.900; 8: 0.350 / 0.504 / 0.901; 9: 0.350 / 0.501 / 0.900; 10: 0.351 / 0.503 / 0.900; 11: 0.348 / 0.497 / 0.900; 12: 0.349 / 0.502 / 0.900; 13: 0.349 / 0.501 / 0.900; 14: 0.348 / 0.501 / 0.900; 15: 0.349 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.138 (body 0.058, range 0.217); 'price stays where it was' would score 0.186; colour right 0.567; typical miss of the close 11.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.115 (body 0.068, range 0.161); 'price stays where it was' would score 0.132; colour right 0.511; typical miss of the close 13.6 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.126 (body 0.082, range 0.170); 'price stays where it was' would score 0.134; colour right 0.505; typical miss of the close 14.5 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.120 (body 0.081, range 0.159); 'price stays where it was' would score 0.122; colour right 0.503; typical miss of the close 9.0 bp; chain ended on the right side 0.482 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.6 bp; chain ended on the right side 0.511 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.4; 2: 0.199 / 5.2; 3: 0.168 / 6.8; 4: 0.132 / 7.1; 5: 0.125 / 7.9; 6: 0.116 / 8.7; 7: 0.112 / 8.9; 8: 0.099 / 9.9; 9: 0.092 / 9.8; 10: 0.089 / 10.3; 11: 0.086 / 10.4; 12: 0.079 / 10.8; 13: 0.072 / 11.2; 14: 0.072 / 11.8; 15: 0.064 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 137063, probability skill vs chance 0.2379, widened contest next: False
  - now: threshold 0.8376, hit rate recent 0.9244 / long run 0.9293
    - 6h: 19 calls (77 a day), hit rate 0.947, chance 0.290, naive rule 0.485, lift 3.27x
    - 24h: 71 calls (71 a day), hit rate 0.915, chance 0.305, naive rule 0.512, lift 3.01x
    - 7d: 421 calls (60 a day), hit rate 0.917, chance 0.294, naive rule 0.499, lift 3.12x
    - 30d: 1752 calls (58 a day), hit rate 0.932, chance 0.293, naive rule 0.494, lift 3.18x
  - next: threshold 0.5657, hit rate recent 0.6489 / long run 0.608
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.290, lift 2.12x
    - 24h: 60 calls (60 a day), hit rate 0.667, chance 0.305, lift 2.19x
    - 7d: 677 calls (97 a day), hit rate 0.612, chance 0.294, lift 2.08x
    - 30d: 3004 calls (100 a day), hit rate 0.588, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.498; 0.35: 533, 0.523; 0.40: 473, 0.579; 0.45: 405, 0.650; 0.50: 355, 0.700; 0.55: 308, 0.744; 0.60: 260, 0.788; 0.65: 219, 0.813; 0.70: 173, 0.843; 0.75: 139, 0.876; 0.80: 93, 0.908; 0.85: 47, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.430; 0.35: 498, 0.463; 0.40: 402, 0.500; 0.45: 305, 0.536; 0.50: 197, 0.571; 0.55: 89, 0.576; 0.60: 12, 0.639; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 137061, probability skill vs chance 0.2227, widened contest next: False
  - now: threshold 0.6859, hit rate recent 0.8493 / long run 0.8223
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.217, naive rule 0.460, lift 4.04x
    - 24h: 56 calls (56 a day), hit rate 0.875, chance 0.199, naive rule 0.430, lift 4.40x
    - 7d: 397 calls (57 a day), hit rate 0.821, chance 0.189, naive rule 0.414, lift 4.35x
    - 30d: 1635 calls (55 a day), hit rate 0.820, chance 0.187, naive rule 0.406, lift 4.38x
  - next: threshold 0.4514, hit rate recent 0.5677 / long run 0.518
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.217, lift 4.04x
    - 24h: 55 calls (55 a day), hit rate 0.582, chance 0.199, lift 2.93x
    - 7d: 404 calls (58 a day), hit rate 0.545, chance 0.189, lift 2.88x
    - 30d: 2728 calls (91 a day), hit rate 0.484, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 348, 0.490; 0.40: 281, 0.562; 0.45: 231, 0.615; 0.50: 184, 0.665; 0.55: 147, 0.701; 0.60: 112, 0.750; 0.65: 77, 0.787; 0.70: 49, 0.823; 0.75: 29, 0.861; 0.80: 10, 0.874
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.386; 0.35: 256, 0.423; 0.40: 160, 0.462; 0.45: 67, 0.487; 0.50: 12, 0.503; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 137058, probability skill vs chance 0.2158, widened contest next: False
  - now: threshold 0.562, hit rate recent 0.7004 / long run 0.6934
    - 6h: 17 calls (70 a day), hit rate 0.647, chance 0.121, naive rule 0.348, lift 5.33x
    - 24h: 54 calls (54 a day), hit rate 0.704, chance 0.122, naive rule 0.356, lift 5.77x
    - 7d: 363 calls (52 a day), hit rate 0.700, chance 0.122, naive rule 0.348, lift 5.71x
    - 30d: 1556 calls (52 a day), hit rate 0.681, chance 0.121, naive rule 0.336, lift 5.65x
  - next: threshold 0.3587, hit rate recent 0.454 / long run 0.4249
    - 6h: 13 calls (53 a day), hit rate 0.385, chance 0.121, lift 3.17x
    - 24h: 64 calls (64 a day), hit rate 0.453, chance 0.122, lift 3.71x
    - 7d: 453 calls (65 a day), hit rate 0.461, chance 0.122, lift 3.77x
    - 30d: 2719 calls (91 a day), hit rate 0.394, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.432; 0.35: 191, 0.496; 0.40: 151, 0.543; 0.45: 116, 0.591; 0.50: 85, 0.640; 0.55: 60, 0.672; 0.60: 41, 0.708; 0.65: 24, 0.783; 0.70: 12, 0.811; 0.75: 2, 0.779
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.363; 0.35: 90, 0.390; 0.40: 25, 0.418; 0.45: 5, 0.450; 0.50: 1, 0.692
- **K=13**: model 1793577600, labels learned 137053, probability skill vs chance 0.1877, widened contest next: False
  - now: threshold 0.4572, hit rate recent 0.5836 / long run 0.5706
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.083, naive rule 0.327, lift 7.06x
    - 24h: 54 calls (55 a day), hit rate 0.574, chance 0.078, naive rule 0.307, lift 7.34x
    - 7d: 395 calls (57 a day), hit rate 0.585, chance 0.080, naive rule 0.295, lift 7.31x
    - 30d: 1653 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.282, lift 7.26x
  - next: threshold 0.2865, hit rate recent 0.3387 / long run 0.3367
    - 6h: 12 calls (50 a day), hit rate 0.333, chance 0.083, lift 4.04x
    - 24h: 60 calls (61 a day), hit rate 0.300, chance 0.078, lift 3.83x
    - 7d: 375 calls (54 a day), hit rate 0.368, chance 0.080, lift 4.60x
    - 30d: 1820 calls (61 a day), hit rate 0.327, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 130, 0.438; 0.35: 94, 0.488; 0.40: 66, 0.546; 0.45: 45, 0.587; 0.50: 30, 0.646; 0.55: 20, 0.676; 0.60: 11, 0.713; 0.65: 3, 0.688; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.340; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.674 | -0.39% | 0.900 | 0.617 | 0.244 | 0.567 | 0.091 |
| 6h | 17.845 | 1.65% | 0.908 | 0.506 | 0.249 | 0.511 | 0.260 |
| 24h | 23.765 | 6.71% | 0.895 | 0.502 | 0.250 | 0.505 | 0.745 |
| 7d | 15.455 | 4.91% | 0.899 | 0.500 | 0.250 | 0.505 | 0.745 |
| 30d | 15.229 | 4.37% | 0.900 | 0.500 | 0.250 | 0.499 | 0.701 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.590 | 21.609 | 22.144 | 21.492 | 23.060 | 22.240 | 21.430 | 21.494 | 21.573 | 21.674 |
| 6h | 18.145 | 17.921 | 17.921 | 17.843 | 18.263 | 18.060 | 17.804 | 17.815 | 17.819 | 17.845 |
| 24h | 25.475 | 24.024 | 23.876 | 23.813 | 24.181 | 24.431 | 23.711 | 23.747 | 23.729 | 23.765 |
| 7d | 16.254 | 15.582 | 15.563 | 15.498 | 15.736 | 15.797 | 15.443 | 15.431 | 15.429 | 15.455 |
| 30d | 15.924 | 15.383 | 15.324 | 15.256 | 15.509 | 15.461 | 15.220 | 15.198 | 15.201 | 15.229 |

## Next candle

- candle starting 2026-11-06 08:29 UTC, last close 2224.23
- P(up) 0.4434, return quantiles (bp): {'05': -10.382, '10': -7.694, '25': -3.983, '40': -1.976, '50': -0.716, '60': 0.581, '75': 3.281, '90': 7.384, '95': 9.848}
- changepoint probability 0.054, regime age 43.2 min
- agent weights: empirical 0.003, ewma 0.076, garch 0.123, har 0.186, bocpd 0.018, hmm 0.018, online_qr 0.301, lgbm 0.274

## Learning log

- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.92, 5.43, 14.8], current probabilities: [0.051, 0.925, 0.024]
- live generator: {'versions': 60, 'latest_effective': '2026-11-06 08:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.27, 'l_abs': 0.704, 'l_hi': 0.723, 'l_lo': 0.77, 'b05': 0.738, 'b25': 0.704, 'b75': 0.555, 'b95': 0.689}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.378, 1.657, 1.918, 2.064, 1.678, 2.878, 2.066, 3.148, 3.674, 4.267, 3.375, 3.122, 3.734, 3.171]}
- calibration offsets (in sigma): {'05': -0.026, '10': -0.012, '25': -0.03, '40': -0.068, '50': -0.08, '60': -0.072, '75': -0.04, '90': -0.018, '95': -0.034}
