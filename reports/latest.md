# ETH-USD 60s candle generator - report

- generated: 2026-10-19 06:45 UTC
- last closed candle: 2026-10-19 06:44 UTC (staleness 1.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.527 (672) [0.495, 0.561] | 0.522 (2875) [0.504, 0.542] | 0.512 (4506) [0.497, 0.527] | 0.514 (1534) [0.486, 0.543] | 0.538 (26) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.555 (785) | 0.545 (5567) [0.537, 0.555] | 0.522 (23331) [0.514, 0.530] | 0.513 (36607) [0.506, 0.519] | 0.544 (12369) [0.539, 0.550] | 0.613 (222) | 0.500 | flat +0.004 (noise 0.009) |
| colour_confident | 0.568 (139) | 0.584 (630) [0.568, 0.603] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.718 (39) | 0.500 | flat -0.018 (noise 0.025) |
| colour_next | 0.520 (1430) | 0.526 (10017) [0.519, 0.534] | 0.515 (42854) [0.509, 0.520] | 0.510 (67147) [0.505, 0.514] | 0.528 (22798) [0.523, 0.533] | 0.562 (402) | 0.500 | flat -0.001 (noise 0.007) |
| colour_path | 0.504 (20020) | 0.502 (140238) [0.499, 0.505] | 0.501 (599956) [0.500, 0.503] | 0.501 (940058) [0.500, 0.502] | 0.500 (319172) [0.498, 0.503] | 0.505 (5628) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.583 (36) | 0.616 (138) [0.574, 0.680] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.750 (8) | 0.500 | flat -0.044 (noise 0.050) |
| reversal_k13_next | 0.309 (81) | 0.296 (433) [0.281, 0.310] | 0.312 (2060) [0.298, 0.327] | 0.306 (3218) [0.294, 0.318] | 0.318 (1113) [0.305, 0.330] | 0.364 (22) | 0.077 | flat -0.034 (noise 0.030) |
| reversal_k13_now | 0.469 (64) | 0.543 (381) [0.510, 0.582] | 0.584 (1534) [0.564, 0.605] | 0.577 (2349) [0.561, 0.595] | 0.571 (877) [0.548, 0.599] | 0.615 (13) | 0.077 | flat -0.029 (noise 0.036) |
| reversal_k3_next | 0.584 (101) | 0.566 (737) [0.555, 0.578] | 0.578 (2604) [0.565, 0.592] | 0.582 (3964) [0.572, 0.594] | 0.574 (1524) [0.560, 0.590] | 0.540 (37) | 0.293 | flat -0.026 (noise 0.028) |
| reversal_k3_now | 0.946 (55) | 0.938 (373) [0.913, 0.964] | 0.938 (1718) [0.929, 0.947] | 0.937 (2681) [0.931, 0.945] | 0.929 (918) [0.918, 0.941] | 1.000 (16) | 0.293 | flat +0.016 (noise 0.018) |
| reversal_k5_next | 0.434 (152) | 0.458 (799) [0.439, 0.484] | 0.472 (2424) [0.457, 0.489] | 0.478 (3519) [0.464, 0.492] | 0.457 (1529) [0.440, 0.477] | 0.429 (35) | 0.187 | flat -0.012 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.810 (348) [0.784, 0.838] | 0.832 (1608) [0.816, 0.847] | 0.832 (2457) [0.819, 0.844] | 0.820 (846) [0.800, 0.840] | 0.882 (17) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k8_next | 0.393 (117) | 0.378 (667) [0.348, 0.403] | 0.400 (2238) [0.381, 0.419] | 0.391 (3547) [0.379, 0.405] | 0.385 (1441) [0.365, 0.404] | 0.429 (28) | 0.121 | flat -0.003 (noise 0.027) |
| reversal_k8_now | 0.651 (43) | 0.681 (335) [0.657, 0.706] | 0.719 (1571) [0.698, 0.739] | 0.707 (2450) [0.691, 0.723] | 0.695 (863) [0.670, 0.721] | 0.818 (11) | 0.122 | flat -0.004 (noise 0.034) |
| overall | 0.506 (22206) | 0.505 (155000) [0.502, 0.507] | 0.504 (661442) [0.503, 0.505] | 0.503 (1035896) [0.502, 0.504] | 0.504 (352615) [0.502, 0.506] | 0.511 (6235) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06523, 0.09791] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5271, 'levels': [{'threshold': 0.06523, 'calls_per_day': 140.8, 'win_rate': 0.5675}, {'threshold': 0.09791, 'calls_per_day': 34.4, 'win_rate': 0.6322}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 22062, 'rate': 0.5293}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15015 | 0.336 | 0.522 (14767) | 0.593 (1413) | 0.772 (2466) |
| volatility: normal | 15014 | 0.363 | 0.516 (14949) | 0.607 (484) | 0.770 (2209) |
| volatility: wild | 15015 | 0.378 | 0.508 (14972) | 0.651 (192) | 0.772 (2035) |
| session: Asia 00-08 | 15284 | 0.357 | 0.520 (15180) | 0.608 (791) | 0.771 (2276) |
| session: Europe 08-13 | 9300 | 0.353 | 0.514 (9215) | 0.577 (523) | 0.777 (1464) |
| session: US 13-21 | 14880 | 0.367 | 0.511 (14777) | 0.588 (488) | 0.776 (2166) |
| session: late 21-24 | 5580 | 0.350 | 0.515 (5516) | 0.652 (287) | 0.752 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.346 | 0.367 | 0.227 | 0.227 | 0.483 | 0.237 | 0.456 | 1.033 |
| 6h | 360 | 0.380 | 0.362 | 0.270 | 0.300 | 0.559 | 0.281 | 0.478 | 1.126 |
| 24h | 1440 | 0.370 | 0.357 | 0.271 | 0.299 | 0.532 | 0.269 | 0.471 | 1.148 |
| 7d | 10080 | 0.368 | 0.358 | 0.279 | 0.311 | 0.526 | 0.263 | 0.472 | 1.195 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.307 | 0.515 | 0.252 | 0.465 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.346 / 0.483 / 0.900; 2: 0.383 / 0.583 / 0.917; 3: 0.341 / 0.483 / 0.950; 4: 0.353 / 0.517 / 0.933; 5: 0.349 / 0.550 / 0.917; 6: 0.356 / 0.567 / 0.983; 7: 0.317 / 0.417 / 1.000; 8: 0.360 / 0.450 / 0.967; 9: 0.352 / 0.483 / 0.983; 10: 0.340 / 0.467 / 1.000; 11: 0.328 / 0.417 / 1.000; 12: 0.355 / 0.500 / 1.000; 13: 0.334 / 0.433 / 1.000; 14: 0.354 / 0.483 / 1.000; 15: 0.359 / 0.550 / 1.000
- 6h: 1: 0.380 / 0.559 / 0.917; 2: 0.363 / 0.494 / 0.911; 3: 0.368 / 0.542 / 0.908; 4: 0.350 / 0.461 / 0.903; 5: 0.361 / 0.514 / 0.917; 6: 0.373 / 0.542 / 0.942; 7: 0.350 / 0.472 / 0.933; 8: 0.361 / 0.497 / 0.936; 9: 0.359 / 0.525 / 0.956; 10: 0.361 / 0.534 / 0.950; 11: 0.354 / 0.503 / 0.950; 12: 0.366 / 0.528 / 0.958; 13: 0.363 / 0.522 / 0.964; 14: 0.356 / 0.486 / 0.969; 15: 0.361 / 0.506 / 0.975
- 24h: 1: 0.370 / 0.532 / 0.902; 2: 0.352 / 0.486 / 0.903; 3: 0.364 / 0.518 / 0.903; 4: 0.352 / 0.491 / 0.897; 5: 0.346 / 0.482 / 0.903; 6: 0.353 / 0.512 / 0.907; 7: 0.348 / 0.498 / 0.905; 8: 0.355 / 0.508 / 0.906; 9: 0.347 / 0.508 / 0.906; 10: 0.351 / 0.508 / 0.906; 11: 0.347 / 0.508 / 0.904; 12: 0.355 / 0.525 / 0.906; 13: 0.354 / 0.519 / 0.909; 14: 0.353 / 0.516 / 0.908; 15: 0.351 / 0.505 / 0.909
- 7d: 1: 0.368 / 0.526 / 0.902; 2: 0.354 / 0.492 / 0.901; 3: 0.360 / 0.508 / 0.901; 4: 0.354 / 0.498 / 0.901; 5: 0.356 / 0.501 / 0.902; 6: 0.356 / 0.506 / 0.902; 7: 0.355 / 0.502 / 0.902; 8: 0.353 / 0.498 / 0.902; 9: 0.354 / 0.502 / 0.903; 10: 0.355 / 0.508 / 0.902; 11: 0.349 / 0.493 / 0.903; 12: 0.354 / 0.505 / 0.902; 13: 0.353 / 0.505 / 0.903; 14: 0.351 / 0.502 / 0.903; 15: 0.354 / 0.506 / 0.903
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.502 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.345 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.118 (body 0.053, range 0.183); 'price stays where it was' would score 0.105; colour right 0.417; typical miss of the close 5.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.141 (body 0.096, range 0.185); 'price stays where it was' would score 0.132; colour right 0.494; typical miss of the close 7.1 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.130 (body 0.090, range 0.171); 'price stays where it was' would score 0.129; colour right 0.511; typical miss of the close 8.6 bp; chain ended on the right side 0.594 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.131; colour right 0.499; typical miss of the close 9.2 bp; chain ended on the right side 0.522 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.7 bp; chain ended on the right side 0.521 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 3.9; 2: 0.196 / 4.4; 3: 0.164 / 6.0; 4: 0.134 / 6.5; 5: 0.122 / 7.1; 6: 0.111 / 7.6; 7: 0.103 / 8.0; 8: 0.096 / 8.4; 9: 0.087 / 8.4; 10: 0.086 / 9.2; 11: 0.082 / 9.8; 12: 0.076 / 10.2; 13: 0.064 / 10.5; 14: 0.065 / 10.6; 15: 0.058 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 111038, probability skill vs chance 0.2229, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9464 / long run 0.9346
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.298, naive rule 0.470, lift 3.36x
    - 24h: 51 calls (51 a day), hit rate 0.941, chance 0.302, naive rule 0.497, lift 3.12x
    - 7d: 376 calls (54 a day), hit rate 0.941, chance 0.290, naive rule 0.483, lift 3.24x
    - 30d: 1714 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.484, lift 3.21x
  - next: threshold 0.5338, hit rate recent 0.5515 / long run 0.5713
    - 6h: 33 calls (134 a day), hit rate 0.515, chance 0.298, lift 1.73x
    - 24h: 115 calls (115 a day), hit rate 0.583, chance 0.302, lift 1.93x
    - 7d: 759 calls (108 a day), hit rate 0.563, chance 0.290, lift 1.94x
    - 30d: 2620 calls (87 a day), hit rate 0.579, chance 0.292, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 540, 0.515; 0.40: 483, 0.567; 0.45: 413, 0.636; 0.50: 360, 0.689; 0.55: 315, 0.731; 0.60: 269, 0.774; 0.65: 224, 0.803; 0.70: 178, 0.836; 0.75: 138, 0.872; 0.80: 94, 0.914; 0.85: 49, 0.953; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 499, 0.460; 0.40: 408, 0.491; 0.45: 313, 0.524; 0.50: 203, 0.556; 0.55: 92, 0.576; 0.60: 14, 0.609; 0.65: 1, 0.679
- **K=5**: model 1791590400, labels learned 111036, probability skill vs chance 0.2148, widened contest next: False
  - now: threshold 0.6843, hit rate recent 0.8198 / long run 0.8253
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.199, naive rule 0.411, lift 4.71x
    - 24h: 51 calls (51 a day), hit rate 0.784, chance 0.191, naive rule 0.404, lift 4.11x
    - 7d: 353 calls (50 a day), hit rate 0.810, chance 0.185, naive rule 0.397, lift 4.37x
    - 30d: 1607 calls (54 a day), hit rate 0.832, chance 0.188, naive rule 0.394, lift 4.44x
  - next: threshold 0.4036, hit rate recent 0.4314 / long run 0.4543
    - 6h: 32 calls (131 a day), hit rate 0.438, chance 0.199, lift 2.20x
    - 24h: 146 calls (147 a day), hit rate 0.438, chance 0.191, lift 2.30x
    - 7d: 819 calls (117 a day), hit rate 0.457, chance 0.185, lift 2.46x
    - 30d: 2446 calls (82 a day), hit rate 0.473, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.422; 0.35: 349, 0.488; 0.40: 280, 0.560; 0.45: 228, 0.616; 0.50: 180, 0.666; 0.55: 137, 0.711; 0.60: 107, 0.751; 0.65: 80, 0.793; 0.70: 59, 0.826; 0.75: 32, 0.871; 0.80: 10, 0.894
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 251, 0.421; 0.40: 159, 0.447; 0.45: 75, 0.462; 0.50: 18, 0.503; 0.55: 2, 0.600
- **K=8**: model 1791936000, labels learned 111033, probability skill vs chance 0.2036, widened contest next: False
  - now: threshold 0.5715, hit rate recent 0.7023 / long run 0.6996
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.133, naive rule 0.388, lift 6.75x
    - 24h: 43 calls (43 a day), hit rate 0.674, chance 0.122, naive rule 0.337, lift 5.52x
    - 7d: 327 calls (47 a day), hit rate 0.685, chance 0.119, naive rule 0.326, lift 5.74x
    - 30d: 1566 calls (52 a day), hit rate 0.720, chance 0.122, naive rule 0.330, lift 5.88x
  - next: threshold 0.3414, hit rate recent 0.3934 / long run 0.3821
    - 6h: 25 calls (103 a day), hit rate 0.440, chance 0.133, lift 3.30x
    - 24h: 117 calls (118 a day), hit rate 0.393, chance 0.122, lift 3.22x
    - 7d: 677 calls (97 a day), hit rate 0.378, chance 0.119, lift 3.17x
    - 30d: 2252 calls (75 a day), hit rate 0.400, chance 0.122, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.422; 0.35: 194, 0.494; 0.40: 148, 0.554; 0.45: 116, 0.596; 0.50: 89, 0.637; 0.55: 65, 0.687; 0.60: 44, 0.733; 0.65: 24, 0.791; 0.70: 9, 0.845; 0.75: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.353; 0.35: 105, 0.385; 0.40: 42, 0.418; 0.45: 9, 0.444; 0.50: 1, 0.455
- **K=13**: model 1792022400, labels learned 111028, probability skill vs chance 0.1838, widened contest next: True
  - now: threshold 0.4136, hit rate recent 0.5232 / long run 0.566
    - 6h: 10 calls (42 a day), hit rate 0.600, chance 0.089, naive rule 0.333, lift 6.77x
    - 24h: 59 calls (60 a day), hit rate 0.492, chance 0.078, naive rule 0.280, lift 6.33x
    - 7d: 375 calls (54 a day), hit rate 0.549, chance 0.077, naive rule 0.275, lift 7.18x
    - 30d: 1535 calls (51 a day), hit rate 0.584, chance 0.078, naive rule 0.274, lift 7.47x
  - next: threshold 0.2768, hit rate recent 0.3084 / long run 0.3115
    - 6h: 19 calls (80 a day), hit rate 0.368, chance 0.089, lift 4.16x
    - 24h: 85 calls (86 a day), hit rate 0.294, chance 0.078, lift 3.79x
    - 7d: 437 calls (63 a day), hit rate 0.300, chance 0.077, lift 3.92x
    - 30d: 2070 calls (69 a day), hit rate 0.312, chance 0.078, lift 3.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.511; 0.40: 61, 0.563; 0.45: 41, 0.619; 0.50: 25, 0.664; 0.55: 14, 0.715; 0.60: 5, 0.762; 0.65: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.325; 0.35: 13, 0.356; 0.40: 2, 0.422; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.754 | 3.71% | 0.900 | 0.467 | 0.250 | 0.500 | 0.203 |
| 6h | 12.787 | 1.91% | 0.914 | 0.478 | 0.250 | 0.478 | 0.393 |
| 24h | 15.233 | 3.32% | 0.906 | 0.494 | 0.250 | 0.479 | 0.594 |
| 7d | 16.158 | 4.22% | 0.901 | 0.500 | 0.251 | 0.492 | 0.642 |
| 30d | 13.722 | 4.05% | 0.900 | 0.500 | 0.251 | 0.495 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.168 | 10.913 | 10.907 | 10.820 | 10.891 | 11.075 | 10.685 | 10.715 | 10.754 | 10.754 |
| 6h | 13.036 | 12.929 | 12.897 | 12.885 | 13.011 | 12.930 | 12.757 | 12.722 | 12.773 | 12.787 |
| 24h | 15.756 | 15.409 | 15.331 | 15.279 | 15.513 | 15.371 | 15.222 | 15.189 | 15.207 | 15.233 |
| 7d | 16.869 | 16.340 | 16.258 | 16.176 | 16.419 | 16.361 | 16.159 | 16.135 | 16.126 | 16.158 |
| 30d | 14.301 | 13.846 | 13.808 | 13.748 | 13.969 | 13.905 | 13.719 | 13.696 | 13.696 | 13.722 |

## Next candle

- candle starting 2026-10-19 06:44 UTC, last close 2429.52
- P(up) 0.4983, return quantiles (bp): {'05': -6.42, '10': -4.454, '25': -2.353, '40': -0.837, '50': -0.034, '60': 1.184, '75': 2.879, '90': 5.047, '95': 6.665}
- changepoint probability 0.0517, regime age 186.6 min
- agent weights: empirical 0.007, ewma 0.057, garch 0.100, har 0.138, bocpd 0.028, hmm 0.060, online_qr 0.273, lgbm 0.338

## Learning log

- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.31, 6.6, 20.94], current probabilities: [0.439, 0.558, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-10-19 06:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.419, 'l_abs': 0.735, 'l_hi': 0.758, 'l_lo': 0.747, 'b05': 0.709, 'b25': 0.749, 'b75': 0.695, 'b95': 0.705}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.234, 1.674, 2.016, 2.127, 2.113, 2.38, 2.549, 2.501, 2.805, 2.947, 2.964, 3.03, 3.027, 3.139]}
- calibration offsets (in sigma): {'05': 0.0615, '10': 0.113, '25': 0.0175, '40': 0.012, '50': -0.005, '60': 0.058, '75': 0.0825, '90': -0.013, '95': -0.0315}
