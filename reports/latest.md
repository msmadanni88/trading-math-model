# ETH-USD 60s candle generator - report

- generated: 2026-11-22 20:48 UTC
- last closed candle: 2026-11-22 20:48 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.527 (672) [0.494, 0.558] | 0.520 (2879) [0.504, 0.536] | 0.516 (7769) [0.505, 0.527] | 0.519 (4797) [0.505, 0.533] | 0.494 (83) | 0.500 | flat -0.007 (noise 0.028) |
| colour_clear | 0.540 (705) | 0.549 (5561) [0.536, 0.562] | 0.541 (23851) [0.535, 0.547] | 0.526 (63754) [0.520, 0.531] | 0.544 (39516) [0.539, 0.548] | 0.529 (664) | 0.500 | flat +0.007 (noise 0.010) |
| colour_confident | 0.594 (224) | 0.563 (1286) [0.540, 0.586] | 0.577 (4508) [0.565, 0.588] | 0.586 (7230) [0.576, 0.596] | 0.586 (7230) [0.576, 0.596] | 0.575 (214) | 0.500 | flat +0.010 (noise 0.023) |
| colour_next | 0.519 (1437) | 0.531 (10048) [0.525, 0.537] | 0.530 (42898) [0.526, 0.534] | 0.519 (115789) [0.515, 0.522] | 0.530 (71440) [0.527, 0.533] | 0.530 (1243) | 0.500 | flat -0.001 (noise 0.008) |
| colour_path | 0.503 (20118) | 0.504 (140672) [0.502, 0.506] | 0.502 (600572) [0.501, 0.504] | 0.501 (1621046) [0.500, 0.502] | 0.502 (1000160) [0.500, 0.502] | 0.496 (17402) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.586 (70) | 0.606 (355) [0.577, 0.642] | 0.611 (1213) [0.595, 0.627] | 0.624 (1897) [0.609, 0.639] | 0.624 (1897) [0.609, 0.639] | 0.672 (67) | 0.500 | flat -0.004 (noise 0.047) |
| reversal_k13_next | 0.469 (49) | 0.311 (495) [0.279, 0.355] | 0.332 (1868) [0.315, 0.351] | 0.316 (5354) [0.306, 0.325] | 0.326 (3249) [0.315, 0.337] | 0.417 (36) | 0.077 | flat -0.037 (noise 0.031) |
| reversal_k13_now | 0.638 (47) | 0.562 (370) [0.522, 0.607] | 0.573 (1634) [0.552, 0.594] | 0.574 (4176) [0.561, 0.586] | 0.570 (2704) [0.554, 0.587] | 0.571 (42) | 0.078 | flat -0.032 (noise 0.038) |
| reversal_k3_next | 0.634 (164) | 0.584 (663) [0.560, 0.609] | 0.600 (2447) [0.590, 0.612] | 0.589 (6892) [0.581, 0.597] | 0.590 (4452) [0.580, 0.601] | 0.675 (151) | 0.293 | flat -0.047 (noise 0.033) |
| reversal_k3_now | 0.936 (47) | 0.936 (373) [0.919, 0.954] | 0.931 (1721) [0.923, 0.941] | 0.935 (4632) [0.929, 0.941] | 0.931 (2869) [0.924, 0.938] | 0.980 (49) | 0.293 | flat +0.009 (noise 0.018) |
| reversal_k5_next | 0.719 (32) | 0.468 (376) [0.420, 0.531] | 0.510 (1986) [0.493, 0.528] | 0.486 (6035) [0.475, 0.497] | 0.482 (4045) [0.468, 0.497] | 0.655 (29) | 0.187 | flat -0.056 (noise 0.045) |
| reversal_k5_now | 0.760 (50) | 0.794 (422) [0.768, 0.817] | 0.794 (1760) [0.777, 0.809] | 0.816 (4418) [0.806, 0.826] | 0.804 (2807) [0.792, 0.815] | 0.878 (49) | 0.187 | up +0.059 (noise 0.029) |
| reversal_k8_next | 0.519 (77) | 0.397 (562) [0.369, 0.435] | 0.415 (2336) [0.400, 0.430] | 0.398 (6311) [0.388, 0.408] | 0.399 (4205) [0.387, 0.411] | 0.448 (67) | 0.121 | flat -0.036 (noise 0.033) |
| reversal_k8_now | 0.640 (50) | 0.655 (420) [0.627, 0.681] | 0.679 (1640) [0.659, 0.698] | 0.695 (4268) [0.683, 0.706] | 0.683 (2681) [0.668, 0.698] | 0.653 (49) | 0.122 | flat -0.021 (noise 0.034) |
| overall | 0.507 (22167) | 0.507 (155073) [0.505, 0.510] | 0.506 (661741) [0.505, 0.507] | 0.504 (1786690) [0.503, 0.505] | 0.505 (1103409) [0.504, 0.506] | 0.503 (19200) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07428, 0.1053] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5304, 'levels': [{'threshold': 0.07428, 'calls_per_day': 148.2, 'win_rate': 0.5716}, {'threshold': 0.1053, 'calls_per_day': 37.7, 'win_rate': 0.6189}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42897, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15296 | 0.349 | 0.532 (15077) | 0.567 (2274) | 0.757 (2550) |
| volatility: normal | 15296 | 0.378 | 0.527 (15243) | 0.580 (1468) | 0.736 (2423) |
| volatility: wild | 15296 | 0.390 | 0.530 (15256) | 0.592 (1115) | 0.755 (2141) |
| session: Asia 00-08 | 15360 | 0.370 | 0.529 (15247) | 0.566 (1699) | 0.750 (2299) |
| session: Europe 08-13 | 9600 | 0.367 | 0.532 (9525) | 0.584 (1205) | 0.753 (1536) |
| session: US 13-21 | 15348 | 0.380 | 0.534 (15257) | 0.606 (1364) | 0.746 (2455) |
| session: late 21-24 | 5580 | 0.366 | 0.517 (5547) | 0.526 (589) | 0.751 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.385 | 0.375 | 0.309 | 0.309 | 0.517 | 0.270 | 0.500 | 1.131 |
| 6h | 360 | 0.383 | 0.381 | 0.278 | 0.314 | 0.542 | 0.260 | 0.506 | 1.386 |
| 24h | 1440 | 0.375 | 0.372 | 0.269 | 0.295 | 0.527 | 0.257 | 0.492 | 1.267 |
| 7d | 10080 | 0.385 | 0.377 | 0.301 | 0.336 | 0.530 | 0.267 | 0.503 | 1.197 |
| 30d | 43200 | 0.372 | 0.366 | 0.286 | 0.317 | 0.530 | 0.265 | 0.479 | 1.269 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.385 / 0.517 / 0.950; 2: 0.384 / 0.517 / 0.883; 3: 0.369 / 0.500 / 0.850; 4: 0.384 / 0.500 / 0.917; 5: 0.388 / 0.583 / 0.933; 6: 0.366 / 0.467 / 0.950; 7: 0.352 / 0.433 / 0.967; 8: 0.360 / 0.450 / 0.967; 9: 0.371 / 0.483 / 0.967; 10: 0.359 / 0.483 / 0.933; 11: 0.350 / 0.400 / 0.933; 12: 0.374 / 0.467 / 0.917; 13: 0.373 / 0.483 / 0.967; 14: 0.350 / 0.417 / 0.983; 15: 0.354 / 0.433 / 1.000
- 6h: 1: 0.383 / 0.542 / 0.911; 2: 0.379 / 0.506 / 0.897; 3: 0.368 / 0.517 / 0.900; 4: 0.365 / 0.466 / 0.925; 5: 0.366 / 0.500 / 0.947; 6: 0.360 / 0.497 / 0.958; 7: 0.363 / 0.494 / 0.972; 8: 0.352 / 0.464 / 0.961; 9: 0.369 / 0.494 / 0.956; 10: 0.363 / 0.517 / 0.944; 11: 0.363 / 0.483 / 0.942; 12: 0.362 / 0.494 / 0.942; 13: 0.366 / 0.503 / 0.956; 14: 0.373 / 0.531 / 0.956; 15: 0.359 / 0.489 / 0.958
- 24h: 1: 0.375 / 0.527 / 0.902; 2: 0.359 / 0.479 / 0.904; 3: 0.363 / 0.506 / 0.906; 4: 0.355 / 0.482 / 0.903; 5: 0.363 / 0.500 / 0.903; 6: 0.359 / 0.499 / 0.901; 7: 0.355 / 0.498 / 0.906; 8: 0.361 / 0.511 / 0.908; 9: 0.354 / 0.478 / 0.901; 10: 0.355 / 0.504 / 0.900; 11: 0.354 / 0.497 / 0.897; 12: 0.355 / 0.498 / 0.897; 13: 0.352 / 0.498 / 0.897; 14: 0.354 / 0.508 / 0.897; 15: 0.353 / 0.500 / 0.896
- 7d: 1: 0.385 / 0.530 / 0.902; 2: 0.373 / 0.494 / 0.901; 3: 0.374 / 0.506 / 0.901; 4: 0.372 / 0.496 / 0.901; 5: 0.375 / 0.509 / 0.902; 6: 0.372 / 0.505 / 0.902; 7: 0.371 / 0.503 / 0.903; 8: 0.373 / 0.511 / 0.902; 9: 0.368 / 0.495 / 0.902; 10: 0.371 / 0.509 / 0.902; 11: 0.369 / 0.504 / 0.902; 12: 0.370 / 0.504 / 0.902; 13: 0.368 / 0.502 / 0.902; 14: 0.368 / 0.501 / 0.902; 15: 0.367 / 0.500 / 0.902
- 30d: 1: 0.372 / 0.530 / 0.898; 2: 0.359 / 0.491 / 0.900; 3: 0.363 / 0.511 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.501 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.358 / 0.504 / 0.900; 11: 0.357 / 0.506 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.502 / 0.900; 14: 0.356 / 0.502 / 0.900; 15: 0.356 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.147 (body 0.084, range 0.210); 'price stays where it was' would score 0.181; colour right 0.450; typical miss of the close 4.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.143 (body 0.080, range 0.206); 'price stays where it was' would score 0.158; colour right 0.500; typical miss of the close 7.1 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.143 (body 0.091, range 0.194); 'price stays where it was' would score 0.156; colour right 0.480; typical miss of the close 8.9 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.133 (body 0.086, range 0.181); 'price stays where it was' would score 0.139; colour right 0.506; typical miss of the close 13.8 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.169); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 10.3 bp; chain ended on the right side 0.517 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 5.5; 2: 0.204 / 6.2; 3: 0.168 / 8.2; 4: 0.135 / 8.5; 5: 0.126 / 9.2; 6: 0.120 / 9.9; 7: 0.116 / 10.4; 8: 0.101 / 11.4; 9: 0.093 / 11.9; 10: 0.090 / 12.5; 11: 0.087 / 12.9; 12: 0.081 / 12.9; 13: 0.074 / 13.7; 14: 0.069 / 14.1; 15: 0.067 / 14.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 160842, probability skill vs chance 0.2415, widened contest next: False
  - now: threshold 0.8296, hit rate recent 0.9584 / long run 0.934
    - 6h: 21 calls (85 a day), hit rate 0.952, chance 0.344, naive rule 0.603, lift 2.77x
    - 24h: 61 calls (61 a day), hit rate 0.984, chance 0.317, naive rule 0.569, lift 3.10x
    - 7d: 386 calls (55 a day), hit rate 0.943, chance 0.294, naive rule 0.510, lift 3.21x
    - 30d: 1715 calls (57 a day), hit rate 0.932, chance 0.294, naive rule 0.502, lift 3.17x
  - next: threshold 0.511, hit rate recent 0.7094 / long run 0.6175
    - 6h: 46 calls (187 a day), hit rate 0.761, chance 0.344, lift 2.21x
    - 24h: 179 calls (180 a day), hit rate 0.682, chance 0.317, lift 2.15x
    - 7d: 782 calls (112 a day), hit rate 0.601, chance 0.294, lift 2.04x
    - 30d: 2540 calls (85 a day), hit rate 0.605, chance 0.294, lift 2.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 558, 0.503; 0.35: 529, 0.528; 0.40: 478, 0.575; 0.45: 413, 0.641; 0.50: 363, 0.686; 0.55: 315, 0.732; 0.60: 265, 0.778; 0.65: 223, 0.807; 0.70: 175, 0.838; 0.75: 141, 0.872; 0.80: 93, 0.904; 0.85: 43, 0.940; 0.90: 4, 0.963
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.435; 0.35: 490, 0.468; 0.40: 387, 0.509; 0.45: 292, 0.543; 0.50: 187, 0.577; 0.55: 79, 0.588; 0.60: 10, 0.638; 0.65: 0, 0.533
- **K=5**: model 1794528000, labels learned 160840, probability skill vs chance 0.2304, widened contest next: False
  - now: threshold 0.6999, hit rate recent 0.8343 / long run 0.7937
    - 6h: 18 calls (73 a day), hit rate 0.833, chance 0.238, naive rule 0.503, lift 3.50x
    - 24h: 59 calls (59 a day), hit rate 0.864, chance 0.208, naive rule 0.479, lift 4.15x
    - 7d: 420 calls (60 a day), hit rate 0.805, chance 0.193, naive rule 0.425, lift 4.17x
    - 30d: 1759 calls (59 a day), hit rate 0.795, chance 0.187, naive rule 0.413, lift 4.24x
  - next: threshold 0.4606, hit rate recent 0.6145 / long run 0.5078
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.238, lift 2.80x
    - 24h: 37 calls (37 a day), hit rate 0.676, chance 0.208, lift 3.24x
    - 7d: 354 calls (51 a day), hit rate 0.486, chance 0.193, lift 2.52x
    - 30d: 1903 calls (63 a day), hit rate 0.511, chance 0.187, lift 2.72x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.423; 0.35: 362, 0.475; 0.40: 293, 0.542; 0.45: 237, 0.603; 0.50: 186, 0.655; 0.55: 149, 0.688; 0.60: 114, 0.734; 0.65: 82, 0.771; 0.70: 51, 0.805; 0.75: 27, 0.840; 0.80: 6, 0.857
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 336, 0.392; 0.35: 250, 0.432; 0.40: 160, 0.463; 0.45: 64, 0.506; 0.50: 8, 0.557; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 160837, probability skill vs chance 0.2105, widened contest next: False
  - now: threshold 0.5808, hit rate recent 0.6696 / long run 0.6729
    - 6h: 20 calls (82 a day), hit rate 0.700, chance 0.149, naive rule 0.409, lift 4.71x
    - 24h: 59 calls (59 a day), hit rate 0.661, chance 0.127, naive rule 0.372, lift 5.22x
    - 7d: 422 calls (60 a day), hit rate 0.664, chance 0.124, naive rule 0.354, lift 5.33x
    - 30d: 1641 calls (55 a day), hit rate 0.681, chance 0.123, naive rule 0.348, lift 5.54x
  - next: threshold 0.3533, hit rate recent 0.4667 / long run 0.4211
    - 6h: 21 calls (86 a day), hit rate 0.476, chance 0.149, lift 3.21x
    - 24h: 82 calls (83 a day), hit rate 0.488, chance 0.127, lift 3.85x
    - 7d: 568 calls (81 a day), hit rate 0.408, chance 0.124, lift 3.28x
    - 30d: 2296 calls (77 a day), hit rate 0.416, chance 0.123, lift 3.38x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.429; 0.35: 199, 0.489; 0.40: 157, 0.538; 0.45: 120, 0.579; 0.50: 86, 0.639; 0.55: 62, 0.674; 0.60: 41, 0.710; 0.65: 24, 0.763; 0.70: 9, 0.809; 0.75: 1, 0.738
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 160, 0.376; 0.35: 84, 0.406; 0.40: 27, 0.442; 0.45: 6, 0.471; 0.50: 1, 0.690
- **K=13**: model 1795132800, labels learned 160832, probability skill vs chance 0.1974, widened contest next: False
  - now: threshold 0.4554, hit rate recent 0.5975 / long run 0.5746
    - 6h: 11 calls (46 a day), hit rate 0.545, chance 0.093, naive rule 0.422, lift 5.88x
    - 24h: 49 calls (50 a day), hit rate 0.592, chance 0.084, naive rule 0.342, lift 7.09x
    - 7d: 373 calls (53 a day), hit rate 0.558, chance 0.081, naive rule 0.299, lift 6.92x
    - 30d: 1626 calls (54 a day), hit rate 0.575, chance 0.079, naive rule 0.294, lift 7.26x
  - next: threshold 0.3065, hit rate recent 0.4179 / long run 0.3359
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.093, lift 4.90x
    - 24h: 44 calls (44 a day), hit rate 0.477, chance 0.084, lift 5.72x
    - 7d: 477 calls (68 a day), hit rate 0.323, chance 0.081, lift 4.00x
    - 30d: 1846 calls (62 a day), hit rate 0.334, chance 0.079, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 140, 0.425; 0.35: 102, 0.474; 0.40: 71, 0.535; 0.45: 49, 0.585; 0.50: 34, 0.622; 0.55: 21, 0.648; 0.60: 10, 0.679; 0.65: 2, 0.552; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.342; 0.35: 15, 0.380; 0.40: 2, 0.434

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.814 | 16.70% | 0.950 | 0.467 | 0.251 | 0.467 | 0.378 |
| 6h | 13.774 | 3.63% | 0.911 | 0.519 | 0.250 | 0.522 | 0.470 |
| 24h | 18.281 | 4.99% | 0.897 | 0.499 | 0.250 | 0.518 | 0.549 |
| 7d | 23.903 | 4.09% | 0.901 | 0.501 | 0.250 | 0.500 | 0.667 |
| 30d | 18.923 | 4.88% | 0.900 | 0.501 | 0.250 | 0.505 | 0.716 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.380 | 7.917 | 8.022 | 7.780 | 8.036 | 9.077 | 7.743 | 7.787 | 7.811 | 7.814 |
| 6h | 14.292 | 13.843 | 13.906 | 13.826 | 14.315 | 14.309 | 13.752 | 13.747 | 13.782 | 13.774 |
| 24h | 19.241 | 18.540 | 18.469 | 18.308 | 18.894 | 18.655 | 18.249 | 18.239 | 18.260 | 18.281 |
| 7d | 24.922 | 24.129 | 24.064 | 23.916 | 24.406 | 24.192 | 23.895 | 23.858 | 23.869 | 23.903 |
| 30d | 19.893 | 19.109 | 19.061 | 18.979 | 19.317 | 19.241 | 18.908 | 18.882 | 18.891 | 18.923 |

## Next candle

- candle starting 2026-11-22 20:48 UTC, last close 1713.39
- P(up) 0.5156, return quantiles (bp): {'05': -4.616, '10': -3.467, '25': -1.424, '40': -0.428, '50': 0.077, '60': 0.677, '75': 1.702, '90': 3.377, '95': 4.579}
- changepoint probability 0.0121, regime age 122.0 min
- agent weights: empirical 0.007, ewma 0.074, garch 0.094, har 0.218, bocpd 0.012, hmm 0.026, online_qr 0.282, lgbm 0.286

## Learning log

- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- 2026-11-22 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9215}, "hmm": {"sd_bp": [5.69, 10.58, 28.33], "stay": [0.985, 0.953, 0.874]}, "lgbm": {"challenger_loss": 0.24557, "champion_loss": 0.24554, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48129, "challengers": 1, "chance_loss": 0.60807, "widened": false, "champion_loss": 0.47918, "promoted": false}, "reversal_k5": {"challenger_loss": 0.381, "challengers": 1, "chance_loss": 0.49754, "widened": false, "champion_loss": 0.37986, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28291, "challengers": 1, "chance_loss": 0.38778, "widened": false, "champion_loss": 0.28187, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20591, "challengers": 1, "chance_loss": 0.29298, "widened": false, "champion_loss": 0.20541, "promoted": false}}
- 2026-11-22 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.9173}, "hmm": {"sd_bp": [5.55, 10.36, 28.43], "stay": [0.982, 0.95, 0.859]}}
- HMM volatility states (sd, bp per minute): [5.55, 10.36, 28.43], current probabilities: [0.982, 0.017, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-22 21:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.302, 'l_abs': 0.784, 'l_hi': 0.805, 'l_lo': 0.745, 'b05': 0.787, 'b25': 0.794, 'b75': 0.722, 'b95': 0.752}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.5]], 'cone_width': [1.275, 1.628, 1.637, 1.627, 1.75, 1.749, 1.989, 2.157, 2.278, 2.492, 2.556, 2.666, 2.559, 2.654]}
- calibration offsets (in sigma): {'05': 0.1035, '10': 0.077, '25': 0.1175, '40': 0.058, '50': 0.015, '60': 0.002, '75': -0.0375, '90': -0.087, '95': -0.1135}
