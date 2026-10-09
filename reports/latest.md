# ETH-USD 60s candle generator - report

- generated: 2026-10-09 00:02 UTC
- last closed candle: 2026-10-09 00:02 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.506 (670) [0.454, 0.558] | 0.505 (2875) [0.485, 0.526] | 0.509 (3547) [0.492, 0.526] | 0.499 (575) [0.443, 0.557] | - | 0.500 | flat -0.002 (noise 0.040) |
| colour_clear | 0.555 (827) | 0.540 (5230) [0.526, 0.552] | 0.507 (23188) [0.500, 0.514] | 0.504 (28748) [0.498, 0.510] | 0.547 (4510) [0.536, 0.556] | 1.000 (2) | 0.500 | up +0.048 (noise 0.010) |
| colour_confident | 0.596 (89) | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 1.000 (1) | 0.500 | - |
| colour_next | 0.528 (1434) | 0.527 (9974) [0.517, 0.538] | 0.507 (42883) [0.501, 0.512] | 0.505 (52891) [0.501, 0.510] | 0.531 (8542) [0.521, 0.541] | 1.000 (2) | 0.500 | up +0.025 (noise 0.007) |
| colour_path | 0.497 (20076) | 0.498 (139636) [0.495, 0.502] | 0.501 (600362) [0.499, 0.502] | 0.500 (740474) [0.499, 0.502] | 0.499 (119588) [0.494, 0.503] | 0.357 (28) | 0.500 | flat -0.005 (noise 0.003) |
| colour_strong | 0.500 (20) | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | - | 0.500 | - |
| reversal_k13_next | 0.318 (66) | 0.312 (525) [0.291, 0.331] | 0.308 (2040) [0.294, 0.324] | 0.304 (2572) [0.290, 0.318] | 0.321 (467) [0.306, 0.336] | - | 0.077 | flat +0.030 (noise 0.027) |
| reversal_k13_now | 0.612 (49) | 0.591 (391) [0.553, 0.636] | 0.585 (1481) [0.563, 0.609] | 0.582 (1811) [0.564, 0.602] | 0.587 (339) [0.544, 0.641] | - | 0.077 | flat +0.007 (noise 0.038) |
| reversal_k3_next | 0.521 (71) | 0.572 (547) [0.542, 0.609] | 0.588 (2352) [0.572, 0.603] | 0.585 (2927) [0.572, 0.599] | 0.571 (487) [0.538, 0.613] | - | 0.292 | flat -0.006 (noise 0.029) |
| reversal_k3_now | 0.917 (72) | 0.927 (399) [0.918, 0.939] | 0.940 (1692) [0.932, 0.948] | 0.939 (2108) [0.932, 0.947] | 0.927 (345) [0.917, 0.941] | - | 0.292 | flat -0.028 (noise 0.017) |
| reversal_k5_next | 0.422 (71) | 0.449 (642) [0.420, 0.481] | 0.488 (2100) [0.468, 0.506] | 0.483 (2512) [0.466, 0.501] | 0.441 (522) [0.412, 0.480] | - | 0.187 | flat -0.034 (noise 0.032) |
| reversal_k5_now | 0.758 (62) | 0.826 (397) [0.795, 0.858] | 0.833 (1573) [0.817, 0.849] | 0.835 (1949) [0.821, 0.850] | 0.823 (338) [0.788, 0.858] | - | 0.187 | flat -0.042 (noise 0.026) |
| reversal_k8_next | 0.367 (120) | 0.387 (587) [0.359, 0.418] | 0.402 (2096) [0.385, 0.421] | 0.394 (2646) [0.379, 0.411] | 0.385 (540) [0.355, 0.418] | - | 0.121 | flat -0.005 (noise 0.032) |
| reversal_k8_now | 0.625 (64) | 0.715 (411) [0.677, 0.756] | 0.723 (1582) [0.703, 0.742] | 0.713 (1947) [0.695, 0.732] | 0.711 (360) [0.670, 0.756] | - | 0.121 | flat -0.038 (noise 0.036) |
| overall | 0.500 (22181) | 0.502 (154179) [0.498, 0.507] | 0.503 (661036) [0.502, 0.505] | 0.503 (815384) [0.501, 0.504] | 0.502 (132103) [0.497, 0.508] | 0.400 (30) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07651, 0.1151] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5339, 'levels': [{'threshold': 0.07651, 'calls_per_day': 143.8, 'win_rate': 0.6106}, {'threshold': 0.1151, 'calls_per_day': 36.2, 'win_rate': 0.6484}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 7412, 'rate': 0.5343}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14881 | 0.334 | 0.515 (14670) | 0.608 (633) | 0.777 (2382) |
| volatility: normal | 14880 | 0.361 | 0.511 (14814) | 0.591 (132) | 0.770 (2092) |
| volatility: wild | 14881 | 0.374 | 0.496 (14835) | 0.647 (51) | 0.777 (2090) |
| session: Asia 00-08 | 14882 | 0.353 | 0.509 (14781) | 0.601 (281) | 0.777 (2139) |
| session: Europe 08-13 | 9300 | 0.351 | 0.505 (9240) | 0.577 (156) | 0.766 (1458) |
| session: US 13-21 | 14880 | 0.367 | 0.506 (14781) | 0.600 (220) | 0.782 (2176) |
| session: late 21-24 | 5580 | 0.350 | 0.511 (5517) | 0.660 (159) | 0.764 (791) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.342 | 0.340 | 0.233 | 0.233 | 0.517 | 0.249 | 0.435 | 0.935 |
| 6h | 360 | 0.374 | 0.368 | 0.280 | 0.319 | 0.529 | 0.264 | 0.484 | 0.997 |
| 24h | 1440 | 0.378 | 0.370 | 0.300 | 0.333 | 0.528 | 0.267 | 0.489 | 1.064 |
| 7d | 10080 | 0.351 | 0.346 | 0.274 | 0.298 | 0.527 | 0.251 | 0.452 | 1.245 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.342 / 0.517 / 0.883; 2: 0.315 / 0.417 / 0.800; 3: 0.353 / 0.517 / 0.867; 4: 0.361 / 0.533 / 0.933; 5: 0.364 / 0.567 / 0.967; 6: 0.337 / 0.500 / 0.967; 7: 0.358 / 0.583 / 0.950; 8: 0.344 / 0.533 / 1.000; 9: 0.328 / 0.483 / 1.000; 10: 0.311 / 0.383 / 1.000; 11: 0.327 / 0.450 / 0.983; 12: 0.351 / 0.550 / 0.967; 13: 0.362 / 0.583 / 0.967; 14: 0.323 / 0.417 / 0.983; 15: 0.328 / 0.467 / 1.000
- 6h: 1: 0.374 / 0.529 / 0.906; 2: 0.361 / 0.468 / 0.867; 3: 0.385 / 0.543 / 0.886; 4: 0.376 / 0.496 / 0.919; 5: 0.381 / 0.524 / 0.928; 6: 0.363 / 0.471 / 0.931; 7: 0.384 / 0.554 / 0.947; 8: 0.373 / 0.510 / 0.939; 9: 0.364 / 0.482 / 0.939; 10: 0.371 / 0.521 / 0.939; 11: 0.360 / 0.479 / 0.947; 12: 0.361 / 0.479 / 0.947; 13: 0.377 / 0.510 / 0.942; 14: 0.367 / 0.510 / 0.953; 15: 0.380 / 0.521 / 0.958
- 24h: 1: 0.378 / 0.528 / 0.897; 2: 0.363 / 0.486 / 0.897; 3: 0.371 / 0.511 / 0.899; 4: 0.367 / 0.495 / 0.899; 5: 0.368 / 0.510 / 0.903; 6: 0.361 / 0.489 / 0.905; 7: 0.365 / 0.510 / 0.910; 8: 0.360 / 0.487 / 0.906; 9: 0.356 / 0.482 / 0.908; 10: 0.360 / 0.497 / 0.909; 11: 0.358 / 0.490 / 0.910; 12: 0.360 / 0.493 / 0.911; 13: 0.363 / 0.499 / 0.912; 14: 0.362 / 0.510 / 0.916; 15: 0.362 / 0.496 / 0.919
- 7d: 1: 0.351 / 0.527 / 0.898; 2: 0.342 / 0.502 / 0.899; 3: 0.344 / 0.510 / 0.899; 4: 0.341 / 0.502 / 0.900; 5: 0.338 / 0.497 / 0.901; 6: 0.336 / 0.490 / 0.901; 7: 0.339 / 0.503 / 0.900; 8: 0.336 / 0.489 / 0.900; 9: 0.333 / 0.486 / 0.900; 10: 0.336 / 0.499 / 0.900; 11: 0.337 / 0.500 / 0.900; 12: 0.338 / 0.504 / 0.900; 13: 0.338 / 0.505 / 0.900; 14: 0.337 / 0.498 / 0.900; 15: 0.335 / 0.491 / 0.900
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.148 (body 0.114, range 0.182); 'price stays where it was' would score 0.187; colour right 0.467; typical miss of the close 5.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.133 (body 0.085, range 0.182); 'price stays where it was' would score 0.141; colour right 0.482; typical miss of the close 8.5 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.128 (body 0.085, range 0.172); 'price stays where it was' would score 0.125; colour right 0.494; typical miss of the close 10.7 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.115 (body 0.077, range 0.153); 'price stays where it was' would score 0.120; colour right 0.497; typical miss of the close 6.3 bp; chain ended on the right side 0.506 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.505 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.2; 2: 0.199 / 4.5; 3: 0.167 / 6.1; 4: 0.132 / 6.7; 5: 0.118 / 7.5; 6: 0.110 / 8.2; 7: 0.099 / 8.6; 8: 0.092 / 8.9; 9: 0.085 / 9.2; 10: 0.080 / 10.1; 11: 0.075 / 10.6; 12: 0.074 / 10.9; 13: 0.063 / 11.3; 14: 0.065 / 11.4; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 96236, probability skill vs chance 0.2278, widened contest next: True
  - now: threshold 0.8394, hit rate recent 0.9135 / long run 0.935
    - 6h: 18 calls (73 a day), hit rate 0.889, chance 0.277, naive rule 0.438, lift 3.20x
    - 24h: 71 calls (71 a day), hit rate 0.915, chance 0.267, naive rule 0.442, lift 3.43x
    - 7d: 399 calls (57 a day), hit rate 0.927, chance 0.291, naive rule 0.486, lift 3.18x
    - 30d: 1692 calls (56 a day), hit rate 0.940, chance 0.291, naive rule 0.481, lift 3.23x
  - next: threshold 0.5577, hit rate recent 0.5225 / long run 0.5773
    - 6h: 24 calls (97 a day), hit rate 0.417, chance 0.277, lift 1.50x
    - 24h: 71 calls (71 a day), hit rate 0.521, chance 0.267, lift 1.95x
    - 7d: 547 calls (78 a day), hit rate 0.572, chance 0.291, lift 1.96x
    - 30d: 2352 calls (78 a day), hit rate 0.588, chance 0.291, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.517; 0.40: 486, 0.561; 0.45: 419, 0.628; 0.50: 366, 0.681; 0.55: 322, 0.724; 0.60: 274, 0.767; 0.65: 225, 0.803; 0.70: 181, 0.834; 0.75: 138, 0.872; 0.80: 96, 0.912; 0.85: 48, 0.948; 0.90: 2, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 497, 0.458; 0.40: 412, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.553; 0.55: 92, 0.586; 0.60: 14, 0.604; 0.65: 1, 0.737
- **K=5**: model 1790208000, labels learned 96234, probability skill vs chance 0.2022, widened contest next: True
  - now: threshold 0.7144, hit rate recent 0.7851 / long run 0.8308
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.195, naive rule 0.397, lift 4.02x
    - 24h: 61 calls (61 a day), hit rate 0.754, chance 0.183, naive rule 0.371, lift 4.12x
    - 7d: 397 calls (57 a day), hit rate 0.826, chance 0.190, naive rule 0.395, lift 4.34x
    - 30d: 1573 calls (52 a day), hit rate 0.833, chance 0.186, naive rule 0.389, lift 4.48x
  - next: threshold 0.4454, hit rate recent 0.4317 / long run 0.4638
    - 6h: 22 calls (90 a day), hit rate 0.455, chance 0.195, lift 2.33x
    - 24h: 71 calls (71 a day), hit rate 0.423, chance 0.183, lift 2.31x
    - 7d: 642 calls (92 a day), hit rate 0.449, chance 0.190, lift 2.36x
    - 30d: 2100 calls (70 a day), hit rate 0.488, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.411; 0.35: 367, 0.467; 0.40: 297, 0.536; 0.45: 242, 0.596; 0.50: 187, 0.653; 0.55: 142, 0.700; 0.60: 110, 0.742; 0.65: 85, 0.788; 0.70: 63, 0.820; 0.75: 34, 0.864; 0.80: 9, 0.881
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.385; 0.35: 253, 0.423; 0.40: 166, 0.448; 0.45: 85, 0.475; 0.50: 21, 0.513; 0.55: 2, 0.574
- **K=8**: model 1791417600, labels learned 96231, probability skill vs chance 0.1963, widened contest next: True
  - now: threshold 0.5772, hit rate recent 0.6471 / long run 0.7135
    - 6h: 16 calls (66 a day), hit rate 0.688, chance 0.119, naive rule 0.315, lift 5.80x
    - 24h: 64 calls (64 a day), hit rate 0.625, chance 0.115, naive rule 0.306, lift 5.45x
    - 7d: 411 calls (59 a day), hit rate 0.715, chance 0.123, naive rule 0.328, lift 5.83x
    - 30d: 1582 calls (53 a day), hit rate 0.723, chance 0.121, naive rule 0.325, lift 5.97x
  - next: threshold 0.3542, hit rate recent 0.3444 / long run 0.3902
    - 6h: 30 calls (123 a day), hit rate 0.267, chance 0.119, lift 2.25x
    - 24h: 120 calls (121 a day), hit rate 0.367, chance 0.115, lift 3.20x
    - 7d: 587 calls (84 a day), hit rate 0.387, chance 0.123, lift 3.15x
    - 30d: 2096 calls (70 a day), hit rate 0.402, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 271, 0.402; 0.35: 204, 0.477; 0.40: 157, 0.538; 0.45: 124, 0.585; 0.50: 94, 0.629; 0.55: 67, 0.684; 0.60: 46, 0.730; 0.65: 24, 0.770; 0.70: 9, 0.816; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.347; 0.35: 115, 0.386; 0.40: 48, 0.411; 0.45: 10, 0.428; 0.50: 1, 0.410
- **K=13**: model 1791504000, labels learned 96226, probability skill vs chance 0.1872, widened contest next: False
  - now: threshold 0.4253, hit rate recent 0.5752 / long run 0.5823
    - 6h: 12 calls (50 a day), hit rate 0.667, chance 0.078, naive rule 0.298, lift 8.52x
    - 24h: 49 calls (50 a day), hit rate 0.612, chance 0.077, naive rule 0.273, lift 7.97x
    - 7d: 391 calls (56 a day), hit rate 0.591, chance 0.078, naive rule 0.273, lift 7.57x
    - 30d: 1481 calls (49 a day), hit rate 0.585, chance 0.077, naive rule 0.267, lift 7.62x
  - next: threshold 0.2908, hit rate recent 0.3158 / long run 0.3073
    - 6h: 12 calls (50 a day), hit rate 0.333, chance 0.078, lift 4.26x
    - 24h: 66 calls (67 a day), hit rate 0.318, chance 0.077, lift 4.14x
    - 7d: 525 calls (75 a day), hit rate 0.312, chance 0.078, lift 4.01x
    - 30d: 2040 calls (68 a day), hit rate 0.308, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.439; 0.35: 88, 0.499; 0.40: 63, 0.548; 0.45: 44, 0.606; 0.50: 27, 0.631; 0.55: 15, 0.683; 0.60: 6, 0.708; 0.65: 1, 0.780
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.317; 0.35: 16, 0.343; 0.40: 3, 0.344; 0.45: 1, 0.368

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.539 | 4.09% | 0.917 | 0.333 | 0.252 | 0.450 | 0.182 |
| 6h | 14.566 | 2.53% | 0.919 | 0.486 | 0.251 | 0.490 | 0.547 |
| 24h | 18.065 | 5.60% | 0.899 | 0.496 | 0.251 | 0.502 | 0.699 |
| 7d | 11.371 | 5.12% | 0.900 | 0.500 | 0.251 | 0.496 | 0.676 |
| 30d | 14.308 | 4.37% | 0.900 | 0.500 | 0.251 | 0.497 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.032 | 11.591 | 11.594 | 11.476 | 11.526 | 11.549 | 11.566 | 11.552 | 11.525 | 11.539 |
| 6h | 14.944 | 14.527 | 14.550 | 14.684 | 14.531 | 14.578 | 14.420 | 14.465 | 14.479 | 14.566 |
| 24h | 19.136 | 18.199 | 18.127 | 18.076 | 18.265 | 18.539 | 18.052 | 18.071 | 18.043 | 18.065 |
| 7d | 11.985 | 11.487 | 11.455 | 11.417 | 11.591 | 11.609 | 11.375 | 11.362 | 11.355 | 11.371 |
| 30d | 14.963 | 14.442 | 14.389 | 14.339 | 14.581 | 14.534 | 14.310 | 14.283 | 14.281 | 14.308 |

## Next candle

- candle starting 2026-10-09 00:02 UTC, last close 2475.8
- P(up) 0.5101, return quantiles (bp): {'05': -7.958, '10': -5.696, '25': -2.685, '40': -0.855, '50': 0.094, '60': 1.157, '75': 3.102, '90': 5.514, '95': 7.377}
- changepoint probability 0.042, regime age 234.8 min
- agent weights: empirical 0.003, ewma 0.087, garch 0.151, har 0.169, bocpd 0.061, hmm 0.010, online_qr 0.270, lgbm 0.250

## Learning log

- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.22, 4.81, 14.65], current probabilities: [0.011, 0.971, 0.018]
- live generator: {'versions': 60, 'latest_effective': '2026-10-09 00:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.409, 'l_abs': 0.712, 'l_hi': 0.717, 'l_lo': 0.74, 'b05': 0.691, 'b25': 0.647, 'b75': 0.544, 'b95': 0.68}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.576, 1.821, 1.869, 1.894, 2.038, 2.162, 2.363, 2.511, 2.548, 2.625, 2.536, 2.752, 2.862, 3.028]}
- calibration offsets (in sigma): {'05': 0.0205, '10': 0.031, '25': 0.0125, '40': 0.024, '50': 0.015, '60': 0.026, '75': 0.0575, '90': -0.041, '95': -0.0605}
