# ETH-USD 60s candle generator - report

- generated: 2026-11-06 21:31 UTC
- last closed candle: 2026-11-06 21:31 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.482 in the last 7 days, -0.057 against the 7 before
- WIN RATE FALLING: reversal_k3_now 0.914 in the last 7 days, -0.040 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.482 (672) [0.452, 0.509] | 0.511 (2879) [0.493, 0.529] | 0.513 (6234) [0.500, 0.526] | 0.514 (3262) [0.495, 0.532] | 0.477 (86) | 0.500 | down -0.057 (noise 0.027) |
| colour_clear | 0.532 (840) | 0.528 (5492) [0.513, 0.542] | 0.541 (23872) [0.535, 0.546] | 0.520 (51047) [0.514, 0.526] | 0.542 (26809) [0.536, 0.546] | 0.590 (732) | 0.500 | flat -0.011 (noise 0.009) |
| colour_confident | 0.557 (88) | 0.571 (870) [0.558, 0.587] | 0.594 (4276) [0.584, 0.604] | 0.596 (4891) [0.584, 0.608] | 0.596 (4891) [0.584, 0.608] | 0.683 (79) | 0.500 | flat -0.030 (noise 0.022) |
| colour_next | 0.517 (1434) | 0.527 (9979) [0.518, 0.536] | 0.528 (42872) [0.524, 0.531] | 0.515 (92895) [0.511, 0.519] | 0.528 (48546) [0.525, 0.532] | 0.563 (1289) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.507 (20076) | 0.504 (139706) [0.502, 0.505] | 0.501 (600208) [0.500, 0.503] | 0.501 (1300530) [0.500, 0.502] | 0.501 (679644) [0.500, 0.502] | 0.502 (18046) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.583 (12) | 0.613 (191) [0.577, 0.640] | 0.630 (1114) [0.611, 0.652] | 0.631 (1283) [0.612, 0.650] | 0.631 (1283) [0.612, 0.650] | 0.769 (13) | 0.500 | flat +0.002 (noise 0.043) |
| reversal_k13_next | 0.318 (66) | 0.360 (369) [0.325, 0.395] | 0.326 (1825) [0.312, 0.340] | 0.313 (4262) [0.302, 0.324] | 0.326 (2157) [0.313, 0.338] | 0.375 (48) | 0.077 | flat +0.041 (noise 0.034) |
| reversal_k13_now | 0.564 (55) | 0.581 (401) [0.546, 0.614] | 0.563 (1650) [0.545, 0.582] | 0.573 (3363) [0.560, 0.587] | 0.567 (1891) [0.547, 0.586] | 0.595 (42) | 0.077 | flat +0.024 (noise 0.035) |
| reversal_k3_next | 0.682 (63) | 0.609 (685) [0.586, 0.634] | 0.586 (3001) [0.575, 0.598] | 0.587 (5803) [0.578, 0.596] | 0.587 (3363) [0.575, 0.598] | 0.615 (39) | 0.293 | flat +0.017 (noise 0.027) |
| reversal_k3_now | 0.915 (59) | 0.914 (407) [0.905, 0.923] | 0.933 (1736) [0.922, 0.943] | 0.936 (3729) [0.930, 0.943] | 0.932 (1966) [0.923, 0.941] | 0.929 (56) | 0.293 | down -0.040 (noise 0.017) |
| reversal_k5_next | 0.574 (61) | 0.543 (396) [0.519, 0.565] | 0.480 (2733) [0.466, 0.496] | 0.484 (5120) [0.472, 0.495] | 0.477 (3130) [0.462, 0.493] | 0.559 (34) | 0.187 | flat +0.036 (noise 0.032) |
| reversal_k5_now | 0.837 (49) | 0.808 (390) [0.796, 0.820] | 0.817 (1624) [0.808, 0.827] | 0.828 (3465) [0.819, 0.837] | 0.820 (1854) [0.810, 0.830] | 0.852 (54) | 0.187 | flat -0.022 (noise 0.027) |
| reversal_k8_next | 0.484 (64) | 0.452 (458) [0.426, 0.478] | 0.392 (2737) [0.379, 0.406] | 0.395 (5170) [0.384, 0.406] | 0.394 (3064) [0.380, 0.407] | 0.444 (45) | 0.121 | flat +0.057 (noise 0.029) |
| reversal_k8_now | 0.717 (46) | 0.690 (358) [0.657, 0.719] | 0.681 (1550) [0.662, 0.700] | 0.701 (3374) [0.687, 0.715] | 0.689 (1787) [0.670, 0.708] | 0.692 (52) | 0.121 | flat +0.002 (noise 0.037) |
| overall | 0.510 (22069) | 0.507 (153821) [0.506, 0.509] | 0.505 (662815) [0.503, 0.506] | 0.504 (1433945) [0.503, 0.505] | 0.505 (750664) [0.503, 0.506] | 0.508 (19791) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07556, 0.114] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5301, 'levels': [{'threshold': 0.07556, 'calls_per_day': 142.7, 'win_rate': 0.5748}, {'threshold': 0.114, 'calls_per_day': 35.4, 'win_rate': 0.632}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42875, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15311 | 0.344 | 0.527 (15075) | 0.573 (2271) | 0.736 (2587) |
| volatility: normal | 15310 | 0.368 | 0.534 (15240) | 0.610 (1434) | 0.753 (2296) |
| volatility: wild | 15310 | 0.383 | 0.524 (15269) | 0.617 (818) | 0.767 (2127) |
| session: Asia 00-08 | 15360 | 0.365 | 0.535 (15258) | 0.597 (1586) | 0.756 (2290) |
| session: Europe 08-13 | 9600 | 0.360 | 0.535 (9504) | 0.595 (1183) | 0.745 (1559) |
| session: US 13-21 | 15360 | 0.372 | 0.522 (15261) | 0.591 (1173) | 0.753 (2339) |
| session: late 21-24 | 5611 | 0.353 | 0.514 (5561) | 0.580 (581) | 0.741 (822) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.445 | 0.396 | 0.296 | 0.296 | 0.683 | 0.353 | 0.537 | 1.353 |
| 6h | 360 | 0.406 | 0.393 | 0.304 | 0.347 | 0.577 | 0.278 | 0.535 | 1.306 |
| 24h | 1440 | 0.402 | 0.388 | 0.297 | 0.331 | 0.562 | 0.288 | 0.517 | 1.287 |
| 7d | 10080 | 0.363 | 0.359 | 0.275 | 0.306 | 0.530 | 0.261 | 0.466 | 1.266 |
| 30d | 43200 | 0.365 | 0.358 | 0.277 | 0.308 | 0.529 | 0.263 | 0.468 | 1.242 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.445 / 0.683 / 0.950; 2: 0.413 / 0.550 / 0.883; 3: 0.395 / 0.517 / 0.950; 4: 0.396 / 0.600 / 0.950; 5: 0.368 / 0.500 / 0.900; 6: 0.382 / 0.517 / 1.000; 7: 0.373 / 0.467 / 0.833; 8: 0.377 / 0.483 / 0.983; 9: 0.383 / 0.483 / 0.800; 10: 0.386 / 0.500 / 0.850; 11: 0.362 / 0.467 / 0.783; 12: 0.377 / 0.483 / 0.850; 13: 0.399 / 0.517 / 0.983; 14: 0.381 / 0.483 / 0.800; 15: 0.361 / 0.433 / 0.983
- 6h: 1: 0.406 / 0.577 / 0.939; 2: 0.395 / 0.490 / 0.894; 3: 0.399 / 0.538 / 0.939; 4: 0.389 / 0.513 / 0.956; 5: 0.386 / 0.521 / 0.925; 6: 0.397 / 0.540 / 0.981; 7: 0.381 / 0.482 / 0.892; 8: 0.382 / 0.490 / 0.978; 9: 0.375 / 0.482 / 0.861; 10: 0.384 / 0.504 / 0.858; 11: 0.396 / 0.532 / 0.847; 12: 0.377 / 0.479 / 0.869; 13: 0.394 / 0.513 / 0.953; 14: 0.375 / 0.462 / 0.825; 15: 0.384 / 0.501 / 0.964
- 24h: 1: 0.402 / 0.562 / 0.909; 2: 0.375 / 0.465 / 0.915; 3: 0.388 / 0.531 / 0.922; 4: 0.377 / 0.492 / 0.921; 5: 0.383 / 0.514 / 0.916; 6: 0.378 / 0.504 / 0.917; 7: 0.375 / 0.490 / 0.902; 8: 0.376 / 0.488 / 0.928; 9: 0.375 / 0.493 / 0.898; 10: 0.385 / 0.525 / 0.898; 11: 0.380 / 0.510 / 0.900; 12: 0.374 / 0.490 / 0.909; 13: 0.379 / 0.504 / 0.924; 14: 0.374 / 0.499 / 0.903; 15: 0.377 / 0.504 / 0.925
- 7d: 1: 0.363 / 0.530 / 0.896; 2: 0.352 / 0.493 / 0.900; 3: 0.355 / 0.512 / 0.902; 4: 0.351 / 0.500 / 0.903; 5: 0.353 / 0.509 / 0.901; 6: 0.350 / 0.508 / 0.899; 7: 0.350 / 0.499 / 0.899; 8: 0.349 / 0.505 / 0.901; 9: 0.352 / 0.510 / 0.899; 10: 0.348 / 0.497 / 0.899; 11: 0.348 / 0.501 / 0.899; 12: 0.348 / 0.503 / 0.900; 13: 0.350 / 0.503 / 0.902; 14: 0.347 / 0.498 / 0.899; 15: 0.350 / 0.510 / 0.902
- 30d: 1: 0.365 / 0.529 / 0.898; 2: 0.353 / 0.495 / 0.900; 3: 0.356 / 0.509 / 0.900; 4: 0.352 / 0.498 / 0.900; 5: 0.353 / 0.505 / 0.900; 6: 0.351 / 0.502 / 0.900; 7: 0.351 / 0.499 / 0.900; 8: 0.351 / 0.504 / 0.900; 9: 0.350 / 0.501 / 0.900; 10: 0.351 / 0.504 / 0.900; 11: 0.348 / 0.498 / 0.900; 12: 0.350 / 0.502 / 0.900; 13: 0.349 / 0.500 / 0.901; 14: 0.349 / 0.501 / 0.900; 15: 0.349 / 0.503 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.124 (body 0.058, range 0.189); 'price stays where it was' would score 0.188; colour right 0.450; typical miss of the close 6.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.153 (body 0.095, range 0.210); 'price stays where it was' would score 0.172; colour right 0.529; typical miss of the close 10.1 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.131 (body 0.084, range 0.178); 'price stays where it was' would score 0.138; colour right 0.511; typical miss of the close 12.4 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.121 (body 0.082, range 0.160); 'price stays where it was' would score 0.123; colour right 0.502; typical miss of the close 8.8 bp; chain ended on the right side 0.485 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.6 bp; chain ended on the right side 0.514 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.5; 2: 0.201 / 5.2; 3: 0.167 / 6.9; 4: 0.131 / 7.1; 5: 0.125 / 7.9; 6: 0.116 / 8.7; 7: 0.112 / 9.0; 8: 0.099 / 9.9; 9: 0.091 / 9.8; 10: 0.090 / 10.3; 11: 0.086 / 10.4; 12: 0.080 / 10.8; 13: 0.073 / 11.2; 14: 0.072 / 11.7; 15: 0.065 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 137845, probability skill vs chance 0.2312, widened contest next: False
  - now: threshold 0.8386, hit rate recent 0.928 / long run 0.9293
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.354, naive rule 0.580, lift 2.83x
    - 24h: 61 calls (61 a day), hit rate 0.934, chance 0.322, naive rule 0.537, lift 2.90x
    - 7d: 422 calls (60 a day), hit rate 0.915, chance 0.297, naive rule 0.500, lift 3.08x
    - 30d: 1756 calls (59 a day), hit rate 0.932, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.5662, hit rate recent 0.63 / long run 0.6068
    - 24h: 44 calls (44 a day), hit rate 0.614, chance 0.322, lift 1.90x
    - 7d: 626 calls (89 a day), hit rate 0.610, chance 0.297, lift 2.06x
    - 30d: 2995 calls (100 a day), hit rate 0.588, chance 0.294, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.498; 0.35: 534, 0.524; 0.40: 474, 0.580; 0.45: 406, 0.650; 0.50: 356, 0.700; 0.55: 309, 0.744; 0.60: 262, 0.788; 0.65: 220, 0.813; 0.70: 174, 0.844; 0.75: 139, 0.876; 0.80: 93, 0.908; 0.85: 47, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.431; 0.35: 498, 0.465; 0.40: 402, 0.501; 0.45: 305, 0.537; 0.50: 197, 0.570; 0.55: 89, 0.578; 0.60: 12, 0.641; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 137843, probability skill vs chance 0.2193, widened contest next: False
  - now: threshold 0.6867, hit rate recent 0.8324 / long run 0.8215
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.222, naive rule 0.497, lift 3.46x
    - 24h: 57 calls (57 a day), hit rate 0.842, chance 0.203, naive rule 0.444, lift 4.15x
    - 7d: 404 calls (58 a day), hit rate 0.817, chance 0.189, naive rule 0.412, lift 4.33x
    - 30d: 1638 calls (55 a day), hit rate 0.818, chance 0.187, naive rule 0.407, lift 4.37x
  - next: threshold 0.4547, hit rate recent 0.5506 / long run 0.5175
    - 24h: 40 calls (40 a day), hit rate 0.550, chance 0.203, lift 2.71x
    - 7d: 400 calls (57 a day), hit rate 0.542, chance 0.189, lift 2.87x
    - 30d: 2721 calls (91 a day), hit rate 0.483, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 349, 0.489; 0.40: 282, 0.562; 0.45: 232, 0.613; 0.50: 185, 0.664; 0.55: 148, 0.700; 0.60: 112, 0.748; 0.65: 77, 0.787; 0.70: 48, 0.821; 0.75: 29, 0.858; 0.80: 10, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.386; 0.35: 256, 0.423; 0.40: 160, 0.463; 0.45: 67, 0.488; 0.50: 12, 0.504; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 137840, probability skill vs chance 0.2063, widened contest next: False
  - now: threshold 0.5692, hit rate recent 0.6824 / long run 0.6921
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.130, naive rule 0.365, lift 4.27x
    - 24h: 55 calls (55 a day), hit rate 0.691, chance 0.121, naive rule 0.337, lift 5.73x
    - 7d: 368 calls (53 a day), hit rate 0.698, chance 0.122, naive rule 0.343, lift 5.72x
    - 30d: 1555 calls (52 a day), hit rate 0.681, chance 0.121, naive rule 0.336, lift 5.64x
  - next: threshold 0.3588, hit rate recent 0.4459 / long run 0.4257
    - 6h: 7 calls (29 a day), hit rate 0.286, chance 0.130, lift 2.20x
    - 24h: 52 calls (52 a day), hit rate 0.404, chance 0.121, lift 3.35x
    - 7d: 422 calls (60 a day), hit rate 0.460, chance 0.122, lift 3.77x
    - 30d: 2698 calls (90 a day), hit rate 0.395, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.432; 0.35: 192, 0.494; 0.40: 152, 0.541; 0.45: 117, 0.588; 0.50: 85, 0.638; 0.55: 60, 0.672; 0.60: 40, 0.705; 0.65: 25, 0.779; 0.70: 12, 0.805; 0.75: 2, 0.768
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.362; 0.35: 90, 0.391; 0.40: 25, 0.419; 0.45: 5, 0.442; 0.50: 1, 0.692
- **K=13**: model 1793577600, labels learned 137835, probability skill vs chance 0.1843, widened contest next: False
  - now: threshold 0.4499, hit rate recent 0.5725 / long run 0.5701
    - 6h: 9 calls (38 a day), hit rate 0.444, chance 0.074, naive rule 0.306, lift 6.01x
    - 24h: 45 calls (45 a day), hit rate 0.600, chance 0.081, naive rule 0.312, lift 7.37x
    - 7d: 390 calls (56 a day), hit rate 0.585, chance 0.080, naive rule 0.292, lift 7.31x
    - 30d: 1652 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.282, lift 7.25x
  - next: threshold 0.2857, hit rate recent 0.3515 / long run 0.3382
    - 6h: 8 calls (33 a day), hit rate 0.375, chance 0.074, lift 5.07x
    - 24h: 54 calls (55 a day), hit rate 0.352, chance 0.081, lift 4.32x
    - 7d: 368 calls (53 a day), hit rate 0.372, chance 0.080, lift 4.65x
    - 30d: 1815 calls (61 a day), hit rate 0.327, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.436; 0.35: 94, 0.486; 0.40: 66, 0.543; 0.45: 45, 0.587; 0.50: 30, 0.643; 0.55: 20, 0.675; 0.60: 11, 0.713; 0.65: 3, 0.684; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.330; 0.35: 13, 0.344; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.948 | 17.86% | 0.967 | 0.533 | 0.251 | 0.483 | 0.446 |
| 6h | 17.259 | 4.73% | 0.942 | 0.522 | 0.250 | 0.496 | 0.681 |
| 24h | 20.416 | 3.99% | 0.912 | 0.500 | 0.250 | 0.499 | 0.607 |
| 7d | 15.224 | 5.20% | 0.900 | 0.500 | 0.250 | 0.507 | 0.745 |
| 30d | 15.315 | 4.40% | 0.900 | 0.500 | 0.250 | 0.499 | 0.706 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.894 | 8.890 | 9.025 | 9.445 | 9.101 | 9.062 | 8.942 | 8.936 | 8.972 | 8.948 |
| 6h | 18.117 | 17.319 | 17.326 | 17.572 | 17.627 | 17.553 | 17.165 | 17.183 | 17.214 | 17.259 |
| 24h | 21.264 | 20.571 | 20.504 | 20.492 | 20.869 | 20.725 | 20.320 | 20.342 | 20.355 | 20.416 |
| 7d | 16.059 | 15.344 | 15.330 | 15.275 | 15.510 | 15.564 | 15.205 | 15.202 | 15.197 | 15.224 |
| 30d | 16.020 | 15.470 | 15.411 | 15.344 | 15.596 | 15.552 | 15.306 | 15.285 | 15.287 | 15.315 |

## Next candle

- candle starting 2026-11-06 21:31 UTC, last close 2224.21
- P(up) 0.5071, return quantiles (bp): {'05': -6.424, '10': -4.784, '25': -2.47, '40': -0.646, '50': 0.045, '60': 0.88, '75': 2.377, '90': 4.611, '95': 6.161}
- changepoint probability 0.0292, regime age 126.1 min
- agent weights: empirical 0.003, ewma 0.114, garch 0.122, har 0.084, bocpd 0.023, hmm 0.035, online_qr 0.346, lgbm 0.273

## Learning log

- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- HMM volatility states (sd, bp per minute): [3.63, 6.36, 16.62], current probabilities: [0.763, 0.233, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-11-06 21:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.178, 'l_abs': 0.696, 'l_hi': 0.744, 'l_lo': 0.749, 'b05': 0.726, 'b25': 0.706, 'b75': 0.579, 'b95': 0.705}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.345, 1.248, 1.473, 1.823, 2.544, 2.492, 2.229, 3.073, 3.311, 3.55, 3.43, 2.597, 4.635, 2.638]}
- calibration offsets (in sigma): {'05': 0.075, '10': 0.03, '25': -0.035, '40': 0.02, '50': 0.0, '60': -0.01, '75': -0.025, '90': -0.08, '95': -0.075}
