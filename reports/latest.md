# ETH-USD 60s candle generator - report

- generated: 2026-10-30 20:58 UTC
- last closed candle: 2026-10-30 20:58 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.539 (672) [0.504, 0.574] | 0.520 (2877) [0.502, 0.539] | 0.516 (5562) [0.503, 0.530] | 0.522 (2590) [0.501, 0.544] | 0.446 (83) | 0.500 | flat -0.003 (noise 0.032) |
| colour_clear | 0.522 (812) | 0.539 (5652) [0.533, 0.545] | 0.539 (23642) [0.532, 0.545] | 0.519 (45555) [0.513, 0.525] | 0.545 (21317) [0.541, 0.549] | 0.550 (682) | 0.500 | flat -0.016 (noise 0.009) |
| colour_confident | 0.588 (119) | 0.601 (1299) [0.586, 0.618] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.601 (4021) [0.589, 0.614] | 0.615 (65) | 0.500 | flat +0.003 (noise 0.020) |
| colour_next | 0.512 (1433) | 0.525 (10025) [0.521, 0.530] | 0.526 (42874) [0.522, 0.530] | 0.514 (82916) [0.510, 0.517] | 0.529 (38567) [0.525, 0.533] | 0.537 (1254) | 0.500 | flat -0.010 (noise 0.007) |
| colour_path | 0.497 (20062) | 0.502 (140350) [0.500, 0.504] | 0.501 (600236) [0.499, 0.502] | 0.501 (1160824) [0.500, 0.502] | 0.501 (539938) [0.499, 0.502] | 0.503 (17556) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.789 (19) | 0.610 (408) [0.584, 0.648] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.634 (1092) [0.612, 0.656] | 0.545 (11) | 0.500 | flat -0.017 (noise 0.040) |
| reversal_k13_next | 0.261 (46) | 0.319 (407) [0.286, 0.358] | 0.312 (2054) [0.300, 0.325] | 0.308 (3893) [0.298, 0.319] | 0.318 (1788) [0.307, 0.330] | 0.286 (49) | 0.077 | flat +0.004 (noise 0.032) |
| reversal_k13_now | 0.522 (67) | 0.557 (420) [0.510, 0.605] | 0.564 (1641) [0.544, 0.585] | 0.572 (2962) [0.557, 0.587] | 0.563 (1490) [0.542, 0.586] | 0.549 (51) | 0.077 | flat +0.019 (noise 0.036) |
| reversal_k3_next | 0.595 (121) | 0.591 (673) [0.583, 0.601] | 0.581 (2921) [0.569, 0.593] | 0.584 (5118) [0.575, 0.594] | 0.581 (2678) [0.569, 0.594] | 0.602 (93) | 0.293 | flat +0.010 (noise 0.026) |
| reversal_k3_now | 1.000 (65) | 0.954 (411) [0.927, 0.978] | 0.936 (1740) [0.927, 0.947] | 0.939 (3322) [0.933, 0.946] | 0.936 (1559) [0.925, 0.947] | 0.923 (39) | 0.293 | flat +0.021 (noise 0.021) |
| reversal_k5_next | 0.537 (41) | 0.507 (675) [0.496, 0.518] | 0.468 (3060) [0.455, 0.483] | 0.479 (4724) [0.467, 0.491] | 0.467 (2734) [0.453, 0.482] | 0.571 (28) | 0.187 | up +0.065 (noise 0.025) |
| reversal_k5_now | 0.841 (69) | 0.830 (417) [0.819, 0.839] | 0.826 (1628) [0.815, 0.836] | 0.831 (3075) [0.821, 0.841] | 0.823 (1464) [0.811, 0.834] | 0.769 (39) | 0.187 | flat +0.003 (noise 0.027) |
| reversal_k8_next | 0.394 (94) | 0.395 (737) [0.375, 0.412] | 0.384 (2774) [0.371, 0.396] | 0.389 (4712) [0.379, 0.400] | 0.384 (2606) [0.371, 0.397] | 0.400 (80) | 0.121 | flat +0.035 (noise 0.025) |
| reversal_k8_now | 0.754 (57) | 0.688 (388) [0.632, 0.741] | 0.692 (1568) [0.671, 0.712] | 0.702 (3016) [0.687, 0.718] | 0.689 (1429) [0.667, 0.712] | 0.600 (40) | 0.121 | flat +0.011 (noise 0.041) |
| overall | 0.500 (22151) | 0.506 (155175) [0.504, 0.508] | 0.504 (663373) [0.503, 0.506] | 0.503 (1280124) [0.502, 0.504] | 0.504 (596843) [0.503, 0.506] | 0.506 (19312) | - | flat +0.004 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0818, 0.1247] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.525, 'levels': [{'threshold': 0.0818, 'calls_per_day': 142.8, 'win_rate': 0.607}, {'threshold': 0.1247, 'calls_per_day': 35.7, 'win_rate': 0.5976}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 38679, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15300 | 0.341 | 0.523 (15073) | 0.585 (2010) | 0.751 (2596) |
| volatility: normal | 15299 | 0.366 | 0.532 (15233) | 0.612 (1355) | 0.752 (2307) |
| volatility: wild | 15299 | 0.381 | 0.522 (15258) | 0.627 (721) | 0.766 (2073) |
| session: Asia 00-08 | 15360 | 0.361 | 0.531 (15259) | 0.603 (1454) | 0.754 (2314) |
| session: Europe 08-13 | 9600 | 0.358 | 0.528 (9515) | 0.593 (1012) | 0.750 (1552) |
| session: US 13-21 | 15358 | 0.370 | 0.522 (15264) | 0.601 (1055) | 0.764 (2244) |
| session: late 21-24 | 5580 | 0.352 | 0.515 (5526) | 0.612 (565) | 0.749 (866) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.388 | 0.361 | 0.260 | 0.260 | 0.583 | 0.295 | 0.480 | 1.239 |
| 6h | 360 | 0.386 | 0.361 | 0.314 | 0.348 | 0.550 | 0.283 | 0.488 | 1.134 |
| 24h | 1440 | 0.387 | 0.376 | 0.301 | 0.340 | 0.526 | 0.268 | 0.505 | 1.167 |
| 7d | 10080 | 0.368 | 0.360 | 0.285 | 0.316 | 0.525 | 0.263 | 0.472 | 1.241 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.307 | 0.527 | 0.260 | 0.464 | 1.274 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.388 / 0.583 / 0.917; 2: 0.373 / 0.533 / 0.967; 3: 0.379 / 0.567 / 0.900; 4: 0.359 / 0.500 / 0.883; 5: 0.344 / 0.500 / 0.933; 6: 0.364 / 0.550 / 0.967; 7: 0.338 / 0.433 / 0.967; 8: 0.374 / 0.617 / 0.967; 9: 0.355 / 0.483 / 0.967; 10: 0.367 / 0.483 / 0.967; 11: 0.367 / 0.483 / 0.967; 12: 0.359 / 0.433 / 0.967; 13: 0.372 / 0.450 / 0.967; 14: 0.378 / 0.517 / 0.967; 15: 0.384 / 0.517 / 0.967
- 6h: 1: 0.386 / 0.550 / 0.903; 2: 0.374 / 0.511 / 0.942; 3: 0.370 / 0.511 / 0.900; 4: 0.372 / 0.506 / 0.847; 5: 0.369 / 0.514 / 0.900; 6: 0.363 / 0.489 / 0.919; 7: 0.354 / 0.455 / 0.936; 8: 0.364 / 0.508 / 0.936; 9: 0.358 / 0.469 / 0.936; 10: 0.370 / 0.494 / 0.942; 11: 0.366 / 0.489 / 0.939; 12: 0.372 / 0.525 / 0.917; 13: 0.376 / 0.514 / 0.908; 14: 0.377 / 0.545 / 0.917; 15: 0.379 / 0.542 / 0.900
- 24h: 1: 0.387 / 0.526 / 0.905; 2: 0.376 / 0.492 / 0.912; 3: 0.376 / 0.508 / 0.907; 4: 0.378 / 0.507 / 0.900; 5: 0.375 / 0.505 / 0.912; 6: 0.376 / 0.514 / 0.915; 7: 0.375 / 0.492 / 0.922; 8: 0.373 / 0.510 / 0.927; 9: 0.370 / 0.487 / 0.922; 10: 0.371 / 0.497 / 0.922; 11: 0.372 / 0.499 / 0.925; 12: 0.375 / 0.508 / 0.924; 13: 0.376 / 0.509 / 0.926; 14: 0.375 / 0.513 / 0.928; 15: 0.374 / 0.497 / 0.924
- 7d: 1: 0.368 / 0.525 / 0.899; 2: 0.355 / 0.490 / 0.900; 3: 0.358 / 0.509 / 0.899; 4: 0.356 / 0.501 / 0.898; 5: 0.355 / 0.504 / 0.900; 6: 0.352 / 0.503 / 0.899; 7: 0.355 / 0.501 / 0.900; 8: 0.354 / 0.507 / 0.899; 9: 0.353 / 0.498 / 0.899; 10: 0.354 / 0.505 / 0.899; 11: 0.351 / 0.503 / 0.899; 12: 0.353 / 0.503 / 0.898; 13: 0.352 / 0.503 / 0.898; 14: 0.352 / 0.503 / 0.899; 15: 0.351 / 0.500 / 0.898
- 30d: 1: 0.362 / 0.527 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.104 (body 0.053, range 0.154); 'price stays where it was' would score 0.141; colour right 0.517; typical miss of the close 11.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.105 (body 0.061, range 0.150); 'price stays where it was' would score 0.128; colour right 0.531; typical miss of the close 18.4 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.133 (body 0.089, range 0.178); 'price stays where it was' would score 0.141; colour right 0.523; typical miss of the close 15.6 bp; chain ended on the right side 0.438 of 96 chains; n=1440
- 7d: match 0.128 (body 0.086, range 0.169); 'price stays where it was' would score 0.136; colour right 0.500; typical miss of the close 9.3 bp; chain ended on the right side 0.521 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 7.9 bp; chain ended on the right side 0.519 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.1; 2: 0.200 / 4.7; 3: 0.167 / 6.2; 4: 0.132 / 6.6; 5: 0.126 / 7.3; 6: 0.113 / 7.8; 7: 0.111 / 8.1; 8: 0.098 / 8.7; 9: 0.088 / 8.8; 10: 0.088 / 9.3; 11: 0.086 / 9.8; 12: 0.076 / 10.2; 13: 0.069 / 10.4; 14: 0.070 / 10.7; 15: 0.062 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 127732, probability skill vs chance 0.2423, widened contest next: False
  - now: threshold 0.834, hit rate recent 0.9521 / long run 0.9432
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.289, naive rule 0.533, lift 3.17x
    - 24h: 50 calls (50 a day), hit rate 0.940, chance 0.295, naive rule 0.513, lift 3.19x
    - 7d: 395 calls (56 a day), hit rate 0.949, chance 0.292, naive rule 0.496, lift 3.25x
    - 30d: 1737 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.493, lift 3.19x
  - next: threshold 0.5291, hit rate recent 0.6291 / long run 0.5916
    - 6h: 30 calls (122 a day), hit rate 0.733, chance 0.289, lift 2.54x
    - 24h: 102 calls (102 a day), hit rate 0.608, chance 0.295, lift 2.06x
    - 7d: 708 calls (101 a day), hit rate 0.593, chance 0.292, lift 2.03x
    - 30d: 2930 calls (98 a day), hit rate 0.582, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.496; 0.35: 536, 0.521; 0.40: 475, 0.578; 0.45: 407, 0.649; 0.50: 356, 0.699; 0.55: 311, 0.741; 0.60: 263, 0.787; 0.65: 220, 0.813; 0.70: 174, 0.845; 0.75: 137, 0.879; 0.80: 92, 0.915; 0.85: 47, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.464; 0.40: 407, 0.497; 0.45: 310, 0.532; 0.50: 199, 0.568; 0.55: 88, 0.571; 0.60: 13, 0.633; 0.65: 1, 0.630
- **K=5**: model 1792540800, labels learned 127730, probability skill vs chance 0.2343, widened contest next: False
  - now: threshold 0.6781, hit rate recent 0.8162 / long run 0.8238
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.178, naive rule 0.459, lift 5.04x
    - 24h: 48 calls (48 a day), hit rate 0.792, chance 0.182, naive rule 0.427, lift 4.35x
    - 7d: 406 calls (58 a day), hit rate 0.825, chance 0.184, naive rule 0.408, lift 4.48x
    - 30d: 1626 calls (54 a day), hit rate 0.823, chance 0.188, naive rule 0.404, lift 4.38x
  - next: threshold 0.4552, hit rate recent 0.5375 / long run 0.494
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.178, lift 3.36x
    - 24h: 32 calls (32 a day), hit rate 0.531, chance 0.182, lift 2.92x
    - 7d: 590 calls (84 a day), hit rate 0.503, chance 0.184, lift 2.73x
    - 30d: 3042 calls (101 a day), hit rate 0.470, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.492; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 180, 0.669; 0.55: 141, 0.708; 0.60: 108, 0.754; 0.65: 76, 0.790; 0.70: 51, 0.828; 0.75: 30, 0.869; 0.80: 10, 0.891
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.388; 0.35: 254, 0.420; 0.40: 158, 0.457; 0.45: 68, 0.476; 0.50: 14, 0.493; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 127727, probability skill vs chance 0.2066, widened contest next: False
  - now: threshold 0.5648, hit rate recent 0.6944 / long run 0.6879
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.133, naive rule 0.421, lift 4.79x
    - 24h: 47 calls (47 a day), hit rate 0.660, chance 0.123, naive rule 0.359, lift 5.37x
    - 7d: 380 calls (54 a day), hit rate 0.692, chance 0.122, naive rule 0.344, lift 5.68x
    - 30d: 1575 calls (53 a day), hit rate 0.690, chance 0.122, naive rule 0.334, lift 5.67x
  - next: threshold 0.3307, hit rate recent 0.4309 / long run 0.3918
    - 6h: 25 calls (103 a day), hit rate 0.480, chance 0.133, lift 3.61x
    - 24h: 88 calls (89 a day), hit rate 0.409, chance 0.123, lift 3.33x
    - 7d: 709 calls (101 a day), hit rate 0.392, chance 0.122, lift 3.22x
    - 30d: 2797 calls (93 a day), hit rate 0.385, chance 0.122, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.432; 0.35: 190, 0.498; 0.40: 147, 0.549; 0.45: 112, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.676; 0.60: 40, 0.711; 0.65: 23, 0.776; 0.70: 11, 0.809; 0.75: 2, 0.746
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.358; 0.35: 92, 0.385; 0.40: 30, 0.408; 0.45: 6, 0.431; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 127722, probability skill vs chance 0.1833, widened contest next: False
  - now: threshold 0.4114, hit rate recent 0.5602 / long run 0.5584
    - 6h: 10 calls (42 a day), hit rate 0.500, chance 0.074, naive rule 0.341, lift 6.76x
    - 24h: 56 calls (57 a day), hit rate 0.571, chance 0.077, naive rule 0.295, lift 7.44x
    - 7d: 421 calls (60 a day), hit rate 0.563, chance 0.076, naive rule 0.281, lift 7.39x
    - 30d: 1654 calls (55 a day), hit rate 0.566, chance 0.077, naive rule 0.278, lift 7.32x
  - next: threshold 0.2935, hit rate recent 0.3029 / long run 0.3132
    - 6h: 18 calls (75 a day), hit rate 0.333, chance 0.074, lift 4.51x
    - 24h: 52 calls (53 a day), hit rate 0.288, chance 0.077, lift 3.75x
    - 7d: 397 calls (57 a day), hit rate 0.315, chance 0.076, lift 4.13x
    - 30d: 2009 calls (67 a day), hit rate 0.315, chance 0.077, lift 4.07x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 127, 0.442; 0.35: 91, 0.494; 0.40: 64, 0.549; 0.45: 42, 0.599; 0.50: 28, 0.655; 0.55: 17, 0.697; 0.60: 8, 0.737; 0.65: 2, 0.725; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.352; 0.40: 3, 0.438; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.940 | 6.70% | 0.917 | 0.550 | 0.250 | 0.483 | 0.445 |
| 6h | 24.348 | 2.45% | 0.897 | 0.497 | 0.251 | 0.444 | 0.538 |
| 24h | 26.343 | 4.67% | 0.906 | 0.500 | 0.251 | 0.483 | 0.688 |
| 7d | 16.678 | 4.46% | 0.900 | 0.500 | 0.251 | 0.497 | 0.728 |
| 30d | 14.275 | 4.25% | 0.900 | 0.500 | 0.251 | 0.496 | 0.691 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.085 | 15.881 | 15.905 | 15.987 | 16.294 | 15.983 | 16.009 | 15.877 | 15.918 | 15.940 |
| 6h | 24.960 | 24.505 | 24.487 | 24.304 | 24.612 | 24.824 | 24.339 | 24.265 | 24.295 | 24.348 |
| 24h | 27.634 | 26.675 | 26.501 | 26.435 | 26.954 | 26.788 | 26.296 | 26.267 | 26.296 | 26.343 |
| 7d | 17.457 | 16.892 | 16.784 | 16.709 | 17.018 | 16.926 | 16.666 | 16.635 | 16.646 | 16.678 |
| 30d | 14.909 | 14.427 | 14.365 | 14.301 | 14.541 | 14.477 | 14.270 | 14.249 | 14.249 | 14.275 |

## Next candle

- candle starting 2026-10-30 20:58 UTC, last close 2235.1
- P(up) 0.5173, return quantiles (bp): {'05': -8.959, '10': -6.686, '25': -3.556, '40': -1.082, '50': 0.221, '60': 1.341, '75': 3.439, '90': 6.295, '95': 7.998}
- changepoint probability 0.0344, regime age 58.5 min
- agent weights: empirical 0.004, ewma 0.059, garch 0.116, har 0.205, bocpd 0.029, hmm 0.029, online_qr 0.254, lgbm 0.304

## Learning log

- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- HMM volatility states (sd, bp per minute): [3.95, 7.23, 20.79], current probabilities: [0.854, 0.144, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-30 21:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.499, 'l_abs': 0.698, 'l_hi': 0.721, 'l_lo': 0.708, 'b05': 0.747, 'b25': 0.649, 'b75': 0.722, 'b95': 0.737}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.3, 1.764, 2.492, 2.068, 2.411, 2.314, 2.632, 2.911, 2.839, 2.983, 3.664, 3.821, 3.742, 4.554]}
- calibration offsets (in sigma): {'05': -0.0115, '10': -0.023, '25': -0.0475, '40': 0.008, '50': 0.025, '60': 0.012, '75': 0.0275, '90': -0.027, '95': -0.0885}
