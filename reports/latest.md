# ETH-USD 60s candle generator - report

- generated: 2026-10-19 01:33 UTC
- last closed candle: 2026-10-19 01:33 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.527 (672) [0.495, 0.561] | 0.522 (2875) [0.504, 0.542] | 0.512 (4506) [0.497, 0.527] | 0.514 (1534) [0.486, 0.543] | 0.667 (6) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.555 (785) | 0.545 (5567) [0.537, 0.555] | 0.522 (23331) [0.514, 0.530] | 0.513 (36607) [0.506, 0.519] | 0.544 (12369) [0.539, 0.550] | 0.646 (48) | 0.500 | flat +0.004 (noise 0.009) |
| colour_confident | 0.568 (139) | 0.584 (630) [0.568, 0.603] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 1.000 (1) | 0.500 | flat -0.018 (noise 0.025) |
| colour_next | 0.520 (1430) | 0.526 (10017) [0.519, 0.534] | 0.515 (42854) [0.509, 0.520] | 0.510 (67147) [0.505, 0.514] | 0.528 (22798) [0.523, 0.533] | 0.559 (93) | 0.500 | flat -0.001 (noise 0.007) |
| colour_path | 0.504 (20020) | 0.502 (140238) [0.499, 0.505] | 0.501 (599956) [0.500, 0.503] | 0.501 (940058) [0.500, 0.502] | 0.500 (319172) [0.498, 0.503] | 0.483 (1302) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.583 (36) | 0.616 (138) [0.574, 0.680] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | - | 0.500 | flat -0.044 (noise 0.050) |
| reversal_k13_next | 0.309 (81) | 0.296 (433) [0.281, 0.310] | 0.312 (2060) [0.298, 0.327] | 0.306 (3218) [0.294, 0.318] | 0.318 (1113) [0.305, 0.330] | 0.250 (4) | 0.077 | flat -0.034 (noise 0.030) |
| reversal_k13_now | 0.469 (64) | 0.543 (381) [0.510, 0.582] | 0.584 (1534) [0.564, 0.605] | 0.577 (2349) [0.561, 0.595] | 0.571 (877) [0.548, 0.599] | 0.500 (4) | 0.077 | flat -0.029 (noise 0.036) |
| reversal_k3_next | 0.584 (101) | 0.566 (737) [0.555, 0.578] | 0.578 (2604) [0.565, 0.592] | 0.582 (3964) [0.572, 0.594] | 0.574 (1524) [0.560, 0.590] | 0.571 (7) | 0.293 | flat -0.026 (noise 0.028) |
| reversal_k3_now | 0.946 (55) | 0.938 (373) [0.913, 0.964] | 0.938 (1718) [0.929, 0.947] | 0.937 (2681) [0.931, 0.945] | 0.929 (918) [0.918, 0.941] | 1.000 (5) | 0.293 | flat +0.016 (noise 0.018) |
| reversal_k5_next | 0.434 (152) | 0.458 (799) [0.439, 0.484] | 0.472 (2424) [0.457, 0.489] | 0.478 (3519) [0.464, 0.492] | 0.457 (1529) [0.440, 0.477] | 0.429 (7) | 0.187 | flat -0.012 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.810 (348) [0.784, 0.838] | 0.832 (1608) [0.816, 0.847] | 0.832 (2457) [0.819, 0.844] | 0.820 (846) [0.800, 0.840] | 0.667 (3) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k8_next | 0.393 (117) | 0.378 (667) [0.348, 0.403] | 0.400 (2238) [0.381, 0.419] | 0.391 (3547) [0.379, 0.405] | 0.385 (1441) [0.365, 0.404] | 0.500 (6) | 0.121 | flat -0.003 (noise 0.027) |
| reversal_k8_now | 0.651 (43) | 0.681 (335) [0.657, 0.706] | 0.719 (1571) [0.698, 0.739] | 0.707 (2450) [0.691, 0.723] | 0.695 (863) [0.670, 0.721] | 0.667 (3) | 0.122 | flat -0.004 (noise 0.034) |
| overall | 0.506 (22206) | 0.505 (155000) [0.502, 0.507] | 0.504 (661442) [0.503, 0.505] | 0.503 (1035896) [0.502, 0.504] | 0.504 (352615) [0.502, 0.506] | 0.491 (1440) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06582, 0.09886] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5264, 'levels': [{'threshold': 0.06582, 'calls_per_day': 138.8, 'win_rate': 0.5613}, {'threshold': 0.09886, 'calls_per_day': 34.1, 'win_rate': 0.6167}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 21753, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14911 | 0.336 | 0.523 (14663) | 0.592 (1401) | 0.773 (2450) |
| volatility: normal | 14911 | 0.362 | 0.515 (14847) | 0.604 (462) | 0.767 (2195) |
| volatility: wild | 14911 | 0.378 | 0.508 (14869) | 0.644 (188) | 0.772 (2023) |
| session: Asia 00-08 | 14973 | 0.357 | 0.519 (14871) | 0.603 (753) | 0.769 (2234) |
| session: Europe 08-13 | 9300 | 0.353 | 0.514 (9215) | 0.577 (523) | 0.777 (1464) |
| session: US 13-21 | 14880 | 0.367 | 0.511 (14777) | 0.588 (488) | 0.776 (2166) |
| session: late 21-24 | 5580 | 0.350 | 0.515 (5516) | 0.652 (287) | 0.752 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.400 | 0.407 | 0.286 | 0.286 | 0.533 | 0.295 | 0.505 | 1.048 |
| 6h | 360 | 0.392 | 0.378 | 0.296 | 0.321 | 0.539 | 0.286 | 0.499 | 1.246 |
| 24h | 1440 | 0.362 | 0.353 | 0.268 | 0.294 | 0.522 | 0.260 | 0.464 | 1.181 |
| 7d | 10080 | 0.367 | 0.358 | 0.280 | 0.311 | 0.526 | 0.263 | 0.472 | 1.205 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.464 | 1.296 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.400 / 0.533 / 0.917; 2: 0.375 / 0.450 / 0.933; 3: 0.397 / 0.567 / 0.933; 4: 0.362 / 0.417 / 0.950; 5: 0.370 / 0.450 / 1.000; 6: 0.410 / 0.633 / 0.967; 7: 0.357 / 0.400 / 0.967; 8: 0.362 / 0.500 / 1.000; 9: 0.371 / 0.550 / 1.000; 10: 0.372 / 0.533 / 1.000; 11: 0.363 / 0.517 / 1.000; 12: 0.343 / 0.483 / 1.000; 13: 0.361 / 0.517 / 1.000; 14: 0.345 / 0.450 / 1.000; 15: 0.368 / 0.483 / 1.000
- 6h: 1: 0.392 / 0.539 / 0.914; 2: 0.363 / 0.464 / 0.925; 3: 0.375 / 0.511 / 0.917; 4: 0.360 / 0.469 / 0.914; 5: 0.362 / 0.478 / 0.928; 6: 0.361 / 0.500 / 0.914; 7: 0.358 / 0.483 / 0.914; 8: 0.359 / 0.497 / 0.908; 9: 0.359 / 0.522 / 0.892; 10: 0.359 / 0.497 / 0.897; 11: 0.356 / 0.522 / 0.894; 12: 0.351 / 0.506 / 0.892; 13: 0.362 / 0.542 / 0.892; 14: 0.359 / 0.542 / 0.881; 15: 0.352 / 0.492 / 0.883
- 24h: 1: 0.362 / 0.522 / 0.895; 2: 0.344 / 0.476 / 0.903; 3: 0.358 / 0.508 / 0.900; 4: 0.347 / 0.495 / 0.904; 5: 0.339 / 0.472 / 0.902; 6: 0.347 / 0.507 / 0.895; 7: 0.345 / 0.499 / 0.893; 8: 0.349 / 0.512 / 0.893; 9: 0.341 / 0.499 / 0.887; 10: 0.348 / 0.506 / 0.886; 11: 0.343 / 0.511 / 0.887; 12: 0.346 / 0.517 / 0.885; 13: 0.345 / 0.508 / 0.884; 14: 0.347 / 0.516 / 0.885; 15: 0.345 / 0.506 / 0.885
- 7d: 1: 0.367 / 0.526 / 0.902; 2: 0.354 / 0.492 / 0.900; 3: 0.360 / 0.508 / 0.900; 4: 0.354 / 0.498 / 0.900; 5: 0.355 / 0.500 / 0.900; 6: 0.356 / 0.504 / 0.899; 7: 0.355 / 0.503 / 0.899; 8: 0.353 / 0.498 / 0.899; 9: 0.354 / 0.503 / 0.898; 10: 0.356 / 0.509 / 0.899; 11: 0.349 / 0.492 / 0.898; 12: 0.354 / 0.506 / 0.899; 13: 0.353 / 0.504 / 0.899; 14: 0.351 / 0.501 / 0.899; 15: 0.353 / 0.503 / 0.898
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.503 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.345 / 0.499 / 0.899; 15: 0.345 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.193 (body 0.159, range 0.226); 'price stays where it was' would score 0.198; colour right 0.567; typical miss of the close 9.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.137 (body 0.092, range 0.183); 'price stays where it was' would score 0.157; colour right 0.539; typical miss of the close 10.4 bp; chain ended on the right side 0.833 of 24 chains; n=360
- 24h: match 0.125 (body 0.089, range 0.162); 'price stays where it was' would score 0.126; colour right 0.522; typical miss of the close 8.8 bp; chain ended on the right side 0.615 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.165); 'price stays where it was' would score 0.130; colour right 0.499; typical miss of the close 9.3 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.522 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 3.9; 2: 0.195 / 4.4; 3: 0.164 / 6.0; 4: 0.134 / 6.5; 5: 0.122 / 7.1; 6: 0.111 / 7.7; 7: 0.102 / 8.0; 8: 0.097 / 8.4; 9: 0.086 / 8.5; 10: 0.085 / 9.3; 11: 0.081 / 9.9; 12: 0.075 / 10.3; 13: 0.064 / 10.5; 14: 0.065 / 10.6; 15: 0.058 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 110727, probability skill vs chance 0.2208, widened contest next: False
  - now: threshold 0.8359, hit rate recent 0.9356 / long run 0.9334
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.301, naive rule 0.481, lift 3.32x
    - 24h: 55 calls (55 a day), hit rate 0.945, chance 0.298, naive rule 0.494, lift 3.18x
    - 7d: 375 calls (54 a day), hit rate 0.939, chance 0.289, naive rule 0.480, lift 3.25x
    - 30d: 1715 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.484, lift 3.22x
  - next: threshold 0.5342, hit rate recent 0.5793 / long run 0.5733
    - 6h: 29 calls (118 a day), hit rate 0.586, chance 0.301, lift 1.94x
    - 24h: 107 calls (107 a day), hit rate 0.579, chance 0.298, lift 1.95x
    - 7d: 741 calls (106 a day), hit rate 0.565, chance 0.289, lift 1.96x
    - 30d: 2607 calls (87 a day), hit rate 0.578, chance 0.292, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 540, 0.514; 0.40: 483, 0.567; 0.45: 413, 0.636; 0.50: 360, 0.689; 0.55: 315, 0.731; 0.60: 269, 0.774; 0.65: 224, 0.803; 0.70: 178, 0.836; 0.75: 138, 0.872; 0.80: 94, 0.914; 0.85: 49, 0.953; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 499, 0.460; 0.40: 408, 0.490; 0.45: 313, 0.524; 0.50: 203, 0.556; 0.55: 92, 0.576; 0.60: 14, 0.609; 0.65: 1, 0.679
- **K=5**: model 1791590400, labels learned 110725, probability skill vs chance 0.2085, widened contest next: True
  - now: threshold 0.6856, hit rate recent 0.7921 / long run 0.8229
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.170, naive rule 0.365, lift 3.92x
    - 24h: 47 calls (47 a day), hit rate 0.766, chance 0.186, naive rule 0.387, lift 4.12x
    - 7d: 349 calls (50 a day), hit rate 0.808, chance 0.184, naive rule 0.395, lift 4.38x
    - 30d: 1604 calls (53 a day), hit rate 0.832, chance 0.188, naive rule 0.394, lift 4.43x
  - next: threshold 0.4035, hit rate recent 0.4404 / long run 0.4556
    - 6h: 32 calls (131 a day), hit rate 0.469, chance 0.170, lift 2.76x
    - 24h: 155 calls (156 a day), hit rate 0.419, chance 0.186, lift 2.25x
    - 7d: 806 calls (115 a day), hit rate 0.458, chance 0.184, lift 2.48x
    - 30d: 2427 calls (81 a day), hit rate 0.473, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.422; 0.35: 350, 0.487; 0.40: 281, 0.559; 0.45: 229, 0.615; 0.50: 180, 0.665; 0.55: 137, 0.710; 0.60: 107, 0.750; 0.65: 80, 0.792; 0.70: 59, 0.826; 0.75: 32, 0.870; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 251, 0.421; 0.40: 160, 0.447; 0.45: 76, 0.463; 0.50: 18, 0.504; 0.55: 2, 0.600
- **K=8**: model 1791936000, labels learned 110722, probability skill vs chance 0.1937, widened contest next: False
  - now: threshold 0.5738, hit rate recent 0.6776 / long run 0.6973
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.103, naive rule 0.282, lift 6.48x
    - 24h: 44 calls (44 a day), hit rate 0.636, chance 0.110, naive rule 0.292, lift 5.78x
    - 7d: 333 calls (48 a day), hit rate 0.682, chance 0.119, naive rule 0.324, lift 5.73x
    - 30d: 1566 calls (52 a day), hit rate 0.720, chance 0.122, naive rule 0.330, lift 5.89x
  - next: threshold 0.3411, hit rate recent 0.3847 / long run 0.3811
    - 6h: 32 calls (132 a day), hit rate 0.406, chance 0.103, lift 3.95x
    - 24h: 120 calls (121 a day), hit rate 0.383, chance 0.110, lift 3.48x
    - 7d: 671 calls (96 a day), hit rate 0.380, chance 0.119, lift 3.19x
    - 30d: 2239 calls (75 a day), hit rate 0.401, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 257, 0.421; 0.35: 194, 0.493; 0.40: 148, 0.553; 0.45: 116, 0.595; 0.50: 90, 0.636; 0.55: 65, 0.687; 0.60: 44, 0.733; 0.65: 24, 0.792; 0.70: 9, 0.844; 0.75: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.352; 0.35: 105, 0.385; 0.40: 42, 0.418; 0.45: 9, 0.446; 0.50: 1, 0.455
- **K=13**: model 1792022400, labels learned 110717, probability skill vs chance 0.1775, widened contest next: True
  - now: threshold 0.4143, hit rate recent 0.5013 / long run 0.5645
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.074, naive rule 0.234, lift 7.89x
    - 24h: 65 calls (66 a day), hit rate 0.462, chance 0.072, naive rule 0.245, lift 6.45x
    - 7d: 381 calls (55 a day), hit rate 0.543, chance 0.076, naive rule 0.272, lift 7.16x
    - 30d: 1532 calls (51 a day), hit rate 0.585, chance 0.078, naive rule 0.274, lift 7.48x
  - next: threshold 0.277, hit rate recent 0.284 / long run 0.3092
    - 6h: 23 calls (96 a day), hit rate 0.261, chance 0.074, lift 3.53x
    - 24h: 85 calls (86 a day), hit rate 0.306, chance 0.072, lift 4.27x
    - 7d: 434 calls (62 a day), hit rate 0.295, chance 0.076, lift 3.89x
    - 30d: 2062 calls (69 a day), hit rate 0.312, chance 0.078, lift 3.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.619; 0.50: 25, 0.664; 0.55: 14, 0.716; 0.60: 5, 0.760; 0.65: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.325; 0.35: 13, 0.357; 0.40: 2, 0.429; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.990 | 2.93% | 0.933 | 0.483 | 0.247 | 0.583 | 0.277 |
| 6h | 19.733 | 3.94% | 0.919 | 0.519 | 0.250 | 0.497 | 0.550 |
| 24h | 14.663 | 3.20% | 0.901 | 0.497 | 0.251 | 0.481 | 0.620 |
| 7d | 16.217 | 4.27% | 0.901 | 0.501 | 0.251 | 0.492 | 0.641 |
| 30d | 13.719 | 4.08% | 0.900 | 0.500 | 0.251 | 0.495 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.503 | 17.137 | 17.208 | 17.189 | 17.263 | 17.131 | 17.152 | 17.101 | 17.096 | 16.990 |
| 6h | 20.543 | 19.934 | 19.798 | 19.859 | 20.062 | 19.927 | 19.744 | 19.747 | 19.700 | 19.733 |
| 24h | 15.147 | 14.811 | 14.733 | 14.698 | 14.917 | 14.766 | 14.656 | 14.622 | 14.630 | 14.663 |
| 7d | 16.940 | 16.400 | 16.318 | 16.235 | 16.480 | 16.423 | 16.222 | 16.195 | 16.186 | 16.217 |
| 30d | 14.303 | 13.843 | 13.804 | 13.745 | 13.965 | 13.902 | 13.717 | 13.693 | 13.693 | 13.719 |

## Next candle

- candle starting 2026-10-19 01:33 UTC, last close 2422.43
- P(up) 0.5388, return quantiles (bp): {'05': -8.929, '10': -6.187, '25': -2.83, '40': -0.569, '50': 0.344, '60': 1.771, '75': 3.573, '90': 6.494, '95': 8.8}
- changepoint probability 0.0792, regime age 49.1 min
- agent weights: empirical 0.004, ewma 0.052, garch 0.124, har 0.173, bocpd 0.021, hmm 0.072, online_qr 0.257, lgbm 0.298

## Learning log

- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.31, 6.6, 20.94], current probabilities: [0.693, 0.303, 0.004]
- live generator: {'versions': 60, 'latest_effective': '2026-10-19 01:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.402, 'l_abs': 0.731, 'l_hi': 0.765, 'l_lo': 0.757, 'b05': 0.7, 'b25': 0.724, 'b75': 0.697, 'b95': 0.707}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.6], [1.4, 1.8], [1.3, 1.6], [1.3, 1.8]], 'cone_width': [1.262, 1.678, 1.941, 2.174, 2.691, 2.855, 2.997, 3.382, 3.645, 3.83, 4.09, 4.351, 4.525, 4.884]}
- calibration offsets (in sigma): {'05': 0.036, '10': 0.072, '25': 0.07, '40': 0.078, '50': 0.06, '60': 0.092, '75': 0.05, '90': -0.022, '95': -0.036}
