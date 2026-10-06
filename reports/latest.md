# ETH-USD 60s candle generator - report

- generated: 2026-10-06 00:19 UTC
- last closed candle: 2026-10-06 00:19 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.432 (95) | 0.508 (669) [0.470, 0.551] | 0.506 (2875) [0.488, 0.526] | 0.513 (3259) [0.495, 0.531] | 0.533 (287) [0.465, 0.601] | 1.000 (1) | 0.500 | flat -0.030 (noise 0.033) |
| colour_clear | 0.563 (766) | 0.515 (5282) [0.493, 0.538] | 0.503 (23277) [0.496, 0.510] | 0.501 (26399) [0.495, 0.507] | 0.556 (2161) [0.550, 0.561] | 0.600 (15) | 0.500 | flat +0.018 (noise 0.014) |
| colour_confident | 0.718 (103) | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.667 (3) | 0.500 | - |
| colour_next | 0.552 (1430) | 0.518 (9994) [0.504, 0.532] | 0.504 (42889) [0.499, 0.510] | 0.504 (48600) [0.499, 0.509] | 0.541 (4251) [0.530, 0.551] | 0.526 (19) | 0.500 | flat +0.019 (noise 0.010) |
| colour_path | 0.508 (20020) | 0.502 (139916) [0.499, 0.506] | 0.501 (600446) [0.500, 0.503] | 0.501 (680400) [0.500, 0.502] | 0.502 (59514) [0.497, 0.507] | 0.489 (266) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.800 (15) | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | - | 0.500 | - |
| reversal_k13_next | 0.288 (73) | 0.291 (635) [0.267, 0.316] | 0.308 (2020) [0.293, 0.324] | 0.303 (2366) [0.288, 0.318] | 0.326 (261) [0.302, 0.347] | - | 0.077 | flat -0.009 (noise 0.029) |
| reversal_k13_now | 0.559 (68) | 0.581 (387) [0.535, 0.631] | 0.587 (1468) [0.564, 0.610] | 0.586 (1650) [0.566, 0.606] | 0.624 (178) [0.572, 0.690] | 0.000 (1) | 0.077 | flat -0.030 (noise 0.037) |
| reversal_k3_next | 0.653 (49) | 0.590 (656) [0.564, 0.621] | 0.584 (2457) [0.569, 0.599] | 0.586 (2757) [0.573, 0.601] | 0.577 (317) [0.552, 0.622] | - | 0.292 | flat +0.039 (noise 0.029) |
| reversal_k3_now | 0.958 (48) | 0.940 (417) [0.930, 0.952] | 0.941 (1702) [0.933, 0.950] | 0.941 (1932) [0.933, 0.949] | 0.935 (169) [0.924, 0.948] | 1.000 (2) | 0.292 | flat +0.004 (noise 0.017) |
| reversal_k5_next | 0.538 (39) | 0.466 (726) [0.435, 0.498] | 0.486 (2120) [0.466, 0.506] | 0.487 (2338) [0.470, 0.505] | 0.448 (348) [0.420, 0.505] | - | 0.187 | flat -0.042 (noise 0.036) |
| reversal_k5_now | 0.867 (45) | 0.853 (395) [0.839, 0.870] | 0.838 (1583) [0.823, 0.852] | 0.840 (1785) [0.825, 0.854] | 0.862 (174) [0.832, 0.889] | 0.000 (1) | 0.187 | flat +0.019 (noise 0.027) |
| reversal_k8_next | 0.365 (74) | 0.400 (468) [0.365, 0.433] | 0.401 (2030) [0.383, 0.421] | 0.397 (2344) [0.381, 0.415] | 0.408 (238) [0.369, 0.442] | - | 0.122 | flat -0.009 (noise 0.034) |
| reversal_k8_now | 0.770 (61) | 0.740 (358) [0.711, 0.764] | 0.724 (1569) [0.705, 0.743] | 0.720 (1758) [0.701, 0.739] | 0.778 (171) [0.773, 0.782] | 0.000 (1) | 0.122 | flat -0.015 (noise 0.033) |
| overall | 0.512 (22002) | 0.505 (154621) [0.502, 0.509] | 0.503 (661159) [0.502, 0.505] | 0.503 (749189) [0.502, 0.504] | 0.507 (65908) [0.502, 0.512] | 0.491 (291) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07624, 0.1141] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5332, 'levels': [{'threshold': 0.07624, 'calls_per_day': 146.1, 'win_rate': 0.5887}, {'threshold': 0.1141, 'calls_per_day': 36.1, 'win_rate': 0.6431}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 3138, 'rate': 0.5519}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14888 | 0.331 | 0.511 (14654) | 0.635 (414) | 0.786 (2384) |
| volatility: normal | 14885 | 0.359 | 0.509 (14821) | 0.700 (30) | 0.778 (2087) |
| volatility: wild | 14886 | 0.373 | 0.494 (14842) | - | 0.777 (2078) |
| session: Asia 00-08 | 14899 | 0.351 | 0.504 (14791) | 0.655 (142) | 0.785 (2150) |
| session: Europe 08-13 | 9300 | 0.347 | 0.503 (9229) | 0.557 (79) | 0.773 (1416) |
| session: US 13-21 | 14880 | 0.364 | 0.506 (14776) | 0.655 (142) | 0.786 (2208) |
| session: late 21-24 | 5580 | 0.351 | 0.507 (5521) | 0.678 (87) | 0.764 (775) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.376 | 0.367 | 0.307 | 0.307 | 0.483 | 0.295 | 0.456 | 1.205 |
| 6h | 360 | 0.375 | 0.354 | 0.280 | 0.302 | 0.568 | 0.285 | 0.464 | 1.274 |
| 24h | 1440 | 0.369 | 0.366 | 0.282 | 0.307 | 0.550 | 0.266 | 0.472 | 1.146 |
| 7d | 10080 | 0.353 | 0.351 | 0.277 | 0.302 | 0.518 | 0.245 | 0.462 | 1.344 |
| 30d | 43200 | 0.355 | 0.355 | 0.278 | 0.308 | 0.504 | 0.246 | 0.464 | 1.283 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.376 / 0.483 / 0.900; 2: 0.347 / 0.450 / 0.767; 3: 0.334 / 0.483 / 0.900; 4: 0.354 / 0.483 / 0.817; 5: 0.337 / 0.450 / 0.833; 6: 0.344 / 0.433 / 0.783; 7: 0.361 / 0.583 / 0.867; 8: 0.356 / 0.533 / 0.650; 9: 0.352 / 0.583 / 0.683; 10: 0.347 / 0.567 / 0.917; 11: 0.334 / 0.483 / 0.750; 12: 0.334 / 0.517 / 0.750; 13: 0.330 / 0.533 / 0.683; 14: 0.332 / 0.467 / 0.650; 15: 0.347 / 0.583 / 0.683
- 6h: 1: 0.375 / 0.568 / 0.925; 2: 0.352 / 0.499 / 0.831; 3: 0.353 / 0.515 / 0.922; 4: 0.356 / 0.499 / 0.853; 5: 0.355 / 0.515 / 0.867; 6: 0.340 / 0.451 / 0.844; 7: 0.364 / 0.540 / 0.911; 8: 0.348 / 0.499 / 0.783; 9: 0.355 / 0.515 / 0.797; 10: 0.346 / 0.515 / 0.958; 11: 0.353 / 0.518 / 0.831; 12: 0.348 / 0.504 / 0.856; 13: 0.354 / 0.499 / 0.800; 14: 0.346 / 0.501 / 0.783; 15: 0.356 / 0.540 / 0.825
- 24h: 1: 0.369 / 0.550 / 0.915; 2: 0.362 / 0.518 / 0.898; 3: 0.357 / 0.512 / 0.913; 4: 0.359 / 0.514 / 0.901; 5: 0.351 / 0.506 / 0.903; 6: 0.353 / 0.494 / 0.899; 7: 0.360 / 0.530 / 0.910; 8: 0.356 / 0.504 / 0.889; 9: 0.351 / 0.504 / 0.892; 10: 0.351 / 0.505 / 0.915; 11: 0.347 / 0.485 / 0.895; 12: 0.349 / 0.497 / 0.897; 13: 0.357 / 0.520 / 0.885; 14: 0.348 / 0.494 / 0.883; 15: 0.355 / 0.515 / 0.890
- 7d: 1: 0.353 / 0.518 / 0.898; 2: 0.348 / 0.503 / 0.899; 3: 0.348 / 0.511 / 0.901; 4: 0.347 / 0.504 / 0.900; 5: 0.344 / 0.501 / 0.900; 6: 0.343 / 0.495 / 0.899; 7: 0.346 / 0.510 / 0.901; 8: 0.343 / 0.499 / 0.898; 9: 0.341 / 0.495 / 0.899; 10: 0.342 / 0.504 / 0.902; 11: 0.343 / 0.504 / 0.899; 12: 0.344 / 0.513 / 0.899; 13: 0.343 / 0.504 / 0.897; 14: 0.340 / 0.493 / 0.897; 15: 0.341 / 0.497 / 0.899
- 30d: 1: 0.355 / 0.504 / 0.899; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.349 / 0.506 / 0.900; 8: 0.348 / 0.504 / 0.899; 9: 0.346 / 0.500 / 0.899; 10: 0.347 / 0.504 / 0.900; 11: 0.347 / 0.503 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.501 / 0.899; 14: 0.344 / 0.494 / 0.899; 15: 0.345 / 0.497 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.054 (body 0.045, range 0.064); 'price stays where it was' would score 0.048; colour right 0.517; typical miss of the close 7.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.108 (body 0.075, range 0.140); 'price stays where it was' would score 0.112; colour right 0.535; typical miss of the close 4.8 bp; chain ended on the right side 0.391 of 23 chains; n=360
- 24h: match 0.112 (body 0.079, range 0.145); 'price stays where it was' would score 0.119; colour right 0.524; typical miss of the close 7.5 bp; chain ended on the right side 0.432 of 95 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.157); 'price stays where it was' would score 0.120; colour right 0.495; typical miss of the close 6.7 bp; chain ended on the right side 0.510 of 669 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.2; 2: 0.199 / 4.4; 3: 0.170 / 6.1; 4: 0.134 / 6.5; 5: 0.123 / 7.3; 6: 0.113 / 8.2; 7: 0.099 / 8.6; 8: 0.091 / 9.1; 9: 0.087 / 9.2; 10: 0.081 / 10.1; 11: 0.076 / 10.7; 12: 0.073 / 11.0; 13: 0.065 / 11.4; 14: 0.066 / 11.5; 15: 0.062 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 91933, probability skill vs chance 0.2378, widened contest next: False
  - now: threshold 0.8426, hit rate recent 0.9383 / long run 0.9402
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.318, naive rule 0.548, lift 2.93x
    - 24h: 49 calls (49 a day), hit rate 0.959, chance 0.308, naive rule 0.510, lift 3.11x
    - 7d: 416 calls (59 a day), hit rate 0.940, chance 0.291, naive rule 0.487, lift 3.23x
    - 30d: 1704 calls (57 a day), hit rate 0.941, chance 0.293, naive rule 0.482, lift 3.22x
  - next: threshold 0.5701, hit rate recent 0.6316 / long run 0.585
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.318, lift 2.20x
    - 24h: 49 calls (49 a day), hit rate 0.653, chance 0.308, lift 2.12x
    - 7d: 654 calls (93 a day), hit rate 0.589, chance 0.291, lift 2.02x
    - 30d: 2457 calls (82 a day), hit rate 0.584, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.495; 0.35: 538, 0.519; 0.40: 488, 0.561; 0.45: 421, 0.627; 0.50: 368, 0.681; 0.55: 322, 0.725; 0.60: 275, 0.767; 0.65: 225, 0.804; 0.70: 182, 0.835; 0.75: 139, 0.870; 0.80: 98, 0.909; 0.85: 49, 0.950; 0.90: 2, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 497, 0.460; 0.40: 413, 0.489; 0.45: 316, 0.520; 0.50: 208, 0.553; 0.55: 93, 0.587; 0.60: 13, 0.619; 0.65: 0, 0.750
- **K=5**: model 1790208000, labels learned 91931, probability skill vs chance 0.2216, widened contest next: False
  - now: threshold 0.7145, hit rate recent 0.8543 / long run 0.845
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.218, naive rule 0.476, lift 3.72x
    - 24h: 45 calls (45 a day), hit rate 0.867, chance 0.204, naive rule 0.426, lift 4.25x
    - 7d: 393 calls (56 a day), hit rate 0.852, chance 0.190, naive rule 0.400, lift 4.48x
    - 30d: 1584 calls (53 a day), hit rate 0.837, chance 0.186, naive rule 0.390, lift 4.50x
  - next: threshold 0.4565, hit rate recent 0.5139 / long run 0.477
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.218, lift 2.29x
    - 24h: 39 calls (39 a day), hit rate 0.538, chance 0.204, lift 2.64x
    - 7d: 725 calls (104 a day), hit rate 0.466, chance 0.190, lift 2.45x
    - 30d: 2120 calls (71 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 432, 0.410; 0.35: 372, 0.463; 0.40: 300, 0.531; 0.45: 246, 0.590; 0.50: 191, 0.648; 0.55: 146, 0.698; 0.60: 114, 0.738; 0.65: 87, 0.783; 0.70: 64, 0.821; 0.75: 35, 0.860; 0.80: 10, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 254, 0.421; 0.40: 167, 0.448; 0.45: 87, 0.471; 0.50: 22, 0.518; 0.55: 3, 0.597
- **K=8**: model 1791158400, labels learned 91928, probability skill vs chance 0.2003, widened contest next: False
  - now: threshold 0.5625, hit rate recent 0.7714 / long run 0.7359
    - 6h: 15 calls (62 a day), hit rate 0.800, chance 0.150, naive rule 0.432, lift 5.33x
    - 24h: 61 calls (61 a day), hit rate 0.770, chance 0.128, naive rule 0.344, lift 6.02x
    - 7d: 355 calls (51 a day), hit rate 0.741, chance 0.126, naive rule 0.338, lift 5.88x
    - 30d: 1570 calls (52 a day), hit rate 0.724, chance 0.121, naive rule 0.325, lift 5.98x
  - next: threshold 0.3499, hit rate recent 0.4122 / long run 0.4071
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.150, lift 3.64x
    - 24h: 74 calls (75 a day), hit rate 0.365, chance 0.128, lift 2.85x
    - 7d: 467 calls (67 a day), hit rate 0.400, chance 0.126, lift 3.18x
    - 30d: 2030 calls (68 a day), hit rate 0.401, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 275, 0.398; 0.35: 207, 0.473; 0.40: 160, 0.536; 0.45: 126, 0.584; 0.50: 97, 0.627; 0.55: 69, 0.682; 0.60: 46, 0.730; 0.65: 24, 0.769; 0.70: 9, 0.803; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 188, 0.343; 0.35: 117, 0.382; 0.40: 48, 0.409; 0.45: 10, 0.424; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 91923, probability skill vs chance 0.182, widened contest next: False
  - now: threshold 0.4181, hit rate recent 0.5796 / long run 0.5914
    - 6h: 15 calls (63 a day), hit rate 0.533, chance 0.078, naive rule 0.329, lift 6.81x
    - 24h: 69 calls (70 a day), hit rate 0.551, chance 0.080, naive rule 0.294, lift 6.88x
    - 7d: 385 calls (55 a day), hit rate 0.584, chance 0.079, naive rule 0.273, lift 7.41x
    - 30d: 1469 calls (49 a day), hit rate 0.586, chance 0.077, naive rule 0.267, lift 7.63x
  - next: threshold 0.2766, hit rate recent 0.3178 / long run 0.3038
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.078, lift 3.99x
    - 24h: 72 calls (73 a day), hit rate 0.292, chance 0.080, lift 3.65x
    - 7d: 632 calls (90 a day), hit rate 0.291, chance 0.079, lift 3.69x
    - 30d: 2019 calls (67 a day), hit rate 0.308, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.436; 0.35: 90, 0.493; 0.40: 65, 0.541; 0.45: 45, 0.600; 0.50: 28, 0.621; 0.55: 16, 0.669; 0.60: 7, 0.688; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.314; 0.35: 17, 0.353; 0.40: 4, 0.339; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.893 | 6.28% | 0.850 | 0.483 | 0.251 | 0.533 | 0.333 |
| 6h | 6.329 | 11.51% | 0.906 | 0.489 | 0.252 | 0.479 | 0.342 |
| 24h | 11.471 | 5.52% | 0.917 | 0.506 | 0.250 | 0.509 | 0.584 |
| 7d | 11.641 | 4.43% | 0.901 | 0.500 | 0.251 | 0.496 | 0.691 |
| 30d | 14.186 | 4.18% | 0.900 | 0.500 | 0.251 | 0.498 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.355 | 6.940 | 6.908 | 6.867 | 6.967 | 7.199 | 6.891 | 6.868 | 6.865 | 6.893 |
| 6h | 7.153 | 6.366 | 6.350 | 6.473 | 6.481 | 6.496 | 6.305 | 6.306 | 6.312 | 6.329 |
| 24h | 12.141 | 11.567 | 11.616 | 11.614 | 11.676 | 11.652 | 11.434 | 11.456 | 11.448 | 11.471 |
| 7d | 12.180 | 11.735 | 11.729 | 11.665 | 11.880 | 11.833 | 11.634 | 11.632 | 11.621 | 11.641 |
| 30d | 14.805 | 14.317 | 14.271 | 14.214 | 14.458 | 14.400 | 14.189 | 14.159 | 14.159 | 14.186 |

## Next candle

- candle starting 2026-10-06 00:19 UTC, last close 2713.67
- P(up) 0.5133, return quantiles (bp): {'05': -4.174, '10': -2.93, '25': -1.534, '40': -0.483, '50': 0.073, '60': 0.659, '75': 1.63, '90': 3.137, '95': 4.292}
- changepoint probability 0.0403, regime age 108.2 min
- agent weights: empirical 0.003, ewma 0.093, garch 0.093, har 0.066, bocpd 0.028, hmm 0.033, online_qr 0.354, lgbm 0.331

## Learning log

- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.76, 4.58, 12.58], current probabilities: [0.177, 0.813, 0.01]
- live generator: {'versions': 60, 'latest_effective': '2026-10-06 00:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.274, 'l_abs': 0.588, 'l_hi': 0.776, 'l_lo': 0.747, 'b05': 0.701, 'b25': 0.577, 'b75': 0.648, 'b95': 0.685}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.8], [1.3, 1.6], [1.3, 1.8], [1.4, 1.6], [1.4, 1.6], [1.3, 1.8], [1.4, 1.6], [1.3, 1.6], [1.4, 1.8]], 'cone_width': [1.752, 1.5, 2.342, 2.521, 2.938, 2.404, 4.598, 4.511, 2.563, 4.353, 3.882, 5.251, 5.798, 4.73]}
- calibration offsets (in sigma): {'05': 0.019, '10': 0.078, '25': 0.025, '40': 0.042, '50': 0.03, '60': 0.028, '75': 0.015, '90': -0.028, '95': -0.039}
