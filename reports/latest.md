# ETH-USD 60s candle generator - report

- generated: 2026-10-03 12:14 UTC
- last closed candle: 2026-10-03 12:14 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 12:14 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k13_next 0.267 in the last 7 days, -0.102 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.383 in the last 7 days, -0.088 against the 7 before

## Win-rate ledger (complete UTC days only; archived in ledger/winrate.csv)

| layer | last day | 7 days | 30 days | all | since go-live | chance | trend |
|---|---|---|---|---|---|---|---|
| chain_end_side | 0.547 (95) | 0.528 (670) | 0.511 (2876) | 0.511 (2972) | - | 0.500 | flat -0.007 |
| colour_next | 0.504 (1432) | 0.505 (10008) | 0.501 (42916) | 0.501 (44349) | - | 0.500 | flat +0.009 |
| colour_path | 0.497 (20048) | 0.502 (140112) | 0.501 (600824) | 0.501 (620886) | - | 0.500 | flat +0.001 |
| reversal_k13_next | 0.241 (58) | 0.267 (592) | 0.302 (2020) | 0.300 (2105) | - | 0.076 | down -0.102 |
| reversal_k13_now | 0.615 (52) | 0.581 (341) | 0.582 (1425) | 0.581 (1472) | - | 0.076 | flat -0.043 |
| reversal_k3_next | 0.583 (60) | 0.578 (609) | 0.587 (2357) | 0.587 (2440) | - | 0.292 | flat -0.012 |
| reversal_k3_now | 0.926 (54) | 0.950 (379) | 0.942 (1712) | 0.942 (1763) | - | 0.292 | flat +0.004 |
| reversal_k5_next | 0.483 (120) | 0.474 (498) | 0.492 (1936) | 0.494 (1990) | - | 0.187 | flat -0.055 |
| reversal_k5_now | 0.848 (59) | 0.870 (354) | 0.835 (1570) | 0.837 (1611) | - | 0.187 | flat +0.049 |
| reversal_k8_next | 0.404 (47) | 0.383 (389) | 0.399 (2020) | 0.396 (2106) | - | 0.121 | down -0.088 |
| reversal_k8_now | 0.745 (51) | 0.739 (325) | 0.712 (1546) | 0.714 (1587) | - | 0.121 | flat -0.016 |
| overall | 0.499 (22076) | 0.504 (154277) | 0.503 (661202) | 0.503 (683281) | - | - | flat -0.000 |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.284 | 0.299 | 0.248 | 0.248 | 0.383 | 0.194 | 0.373 | 1.355 |
| 6h | 360 | 0.328 | 0.314 | 0.239 | 0.265 | 0.515 | 0.254 | 0.403 | 1.095 |
| 24h | 1440 | 0.341 | 0.340 | 0.262 | 0.291 | 0.500 | 0.234 | 0.447 | 1.082 |
| 7d | 10080 | 0.358 | 0.358 | 0.286 | 0.314 | 0.504 | 0.244 | 0.473 | 1.337 |
| 30d | 43200 | 0.356 | 0.356 | 0.280 | 0.311 | 0.500 | 0.245 | 0.468 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.284 / 0.383 / 0.900; 2: 0.346 / 0.617 / 0.917; 3: 0.280 / 0.450 / 0.883; 4: 0.311 / 0.483 / 0.917; 5: 0.300 / 0.433 / 0.933; 6: 0.307 / 0.483 / 0.917; 7: 0.349 / 0.600 / 0.900; 8: 0.293 / 0.433 / 0.900; 9: 0.314 / 0.517 / 0.917; 10: 0.336 / 0.567 / 0.900; 11: 0.320 / 0.467 / 0.900; 12: 0.322 / 0.500 / 0.900; 13: 0.318 / 0.500 / 0.867; 14: 0.317 / 0.483 / 0.867; 15: 0.319 / 0.467 / 0.900
- 6h: 1: 0.328 / 0.515 / 0.878; 2: 0.322 / 0.504 / 0.892; 3: 0.320 / 0.493 / 0.889; 4: 0.320 / 0.527 / 0.903; 5: 0.318 / 0.496 / 0.892; 6: 0.312 / 0.465 / 0.869; 7: 0.324 / 0.524 / 0.872; 8: 0.303 / 0.459 / 0.872; 9: 0.306 / 0.468 / 0.872; 10: 0.320 / 0.501 / 0.875; 11: 0.318 / 0.501 / 0.878; 12: 0.320 / 0.499 / 0.883; 13: 0.314 / 0.487 / 0.892; 14: 0.314 / 0.490 / 0.894; 15: 0.315 / 0.473 / 0.897
- 24h: 1: 0.341 / 0.500 / 0.903; 2: 0.341 / 0.504 / 0.896; 3: 0.340 / 0.488 / 0.898; 4: 0.338 / 0.507 / 0.904; 5: 0.335 / 0.493 / 0.903; 6: 0.334 / 0.472 / 0.896; 7: 0.341 / 0.511 / 0.898; 8: 0.331 / 0.480 / 0.897; 9: 0.332 / 0.490 / 0.899; 10: 0.331 / 0.479 / 0.899; 11: 0.341 / 0.527 / 0.899; 12: 0.337 / 0.509 / 0.899; 13: 0.333 / 0.490 / 0.899; 14: 0.337 / 0.501 / 0.900; 15: 0.328 / 0.473 / 0.901
- 7d: 1: 0.358 / 0.504 / 0.899; 2: 0.353 / 0.493 / 0.900; 3: 0.356 / 0.508 / 0.900; 4: 0.352 / 0.493 / 0.900; 5: 0.353 / 0.507 / 0.900; 6: 0.351 / 0.501 / 0.899; 7: 0.351 / 0.499 / 0.899; 8: 0.351 / 0.508 / 0.900; 9: 0.348 / 0.495 / 0.900; 10: 0.349 / 0.504 / 0.900; 11: 0.350 / 0.505 / 0.900; 12: 0.351 / 0.507 / 0.900; 13: 0.350 / 0.502 / 0.901; 14: 0.348 / 0.498 / 0.901; 15: 0.348 / 0.500 / 0.901
- 30d: 1: 0.356 / 0.500 / 0.899; 2: 0.353 / 0.497 / 0.900; 3: 0.355 / 0.505 / 0.900; 4: 0.352 / 0.499 / 0.900; 5: 0.352 / 0.501 / 0.900; 6: 0.352 / 0.505 / 0.900; 7: 0.351 / 0.506 / 0.900; 8: 0.350 / 0.503 / 0.900; 9: 0.348 / 0.499 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.348 / 0.502 / 0.900; 12: 0.348 / 0.501 / 0.900; 13: 0.347 / 0.500 / 0.900; 14: 0.346 / 0.495 / 0.900; 15: 0.346 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.096 (body 0.075, range 0.116); 'price stays where it was' would score 0.109; colour right 0.400; typical miss of the close 3.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.085, range 0.152); 'price stays where it was' would score 0.118; colour right 0.476; typical miss of the close 3.5 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.118 (body 0.075, range 0.161); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 5.7 bp; chain ended on the right side 0.526 of 95 chains; n=1440
- 7d: match 0.119 (body 0.078, range 0.160); 'price stays where it was' would score 0.120; colour right 0.494; typical miss of the close 7.7 bp; chain ended on the right side 0.522 of 670 chains; n=10080
- 30d: match 0.122 (body 0.081, range 0.162); 'price stays where it was' would score 0.128; colour right 0.498; typical miss of the close 8.4 bp; chain ended on the right side 0.511 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.4; 2: 0.198 / 4.5; 3: 0.170 / 6.4; 4: 0.133 / 6.7; 5: 0.122 / 7.5; 6: 0.113 / 8.4; 7: 0.102 / 8.9; 8: 0.093 / 9.4; 9: 0.089 / 9.5; 10: 0.085 / 10.4; 11: 0.078 / 11.0; 12: 0.076 / 11.4; 13: 0.069 / 11.8; 14: 0.068 / 11.8; 15: 0.062 / 12.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 88328, probability skill vs chance 0.2317, widened contest next: True
  - now: threshold 0.8393, hit rate recent 0.9394 / long run 0.9429
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.282, naive rule 0.495, lift 3.31x
    - 24h: 56 calls (56 a day), hit rate 0.929, chance 0.289, naive rule 0.496, lift 3.22x
    - 7d: 389 calls (56 a day), hit rate 0.954, chance 0.290, naive rule 0.485, lift 3.28x
    - 30d: 1715 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.481, lift 3.23x
  - next: threshold 0.533, hit rate recent 0.5366 / long run 0.5792
    - 6h: 36 calls (146 a day), hit rate 0.528, chance 0.282, lift 1.87x
    - 24h: 96 calls (96 a day), hit rate 0.500, chance 0.289, lift 1.73x
    - 7d: 640 calls (91 a day), hit rate 0.580, chance 0.290, lift 2.00x
    - 30d: 2385 calls (80 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.493; 0.35: 538, 0.518; 0.40: 490, 0.558; 0.45: 424, 0.623; 0.50: 370, 0.678; 0.55: 323, 0.723; 0.60: 276, 0.764; 0.65: 225, 0.800; 0.70: 183, 0.832; 0.75: 141, 0.867; 0.80: 100, 0.906; 0.85: 49, 0.949; 0.90: 1, 0.970
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 496, 0.459; 0.40: 412, 0.488; 0.45: 317, 0.519; 0.50: 208, 0.550; 0.55: 94, 0.587; 0.60: 12, 0.613; 0.65: 0, 0.750
- **K=5**: model 1790208000, labels learned 88326, probability skill vs chance 0.2221, widened contest next: True
  - now: threshold 0.7087, hit rate recent 0.8595 / long run 0.8426
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.191, naive rule 0.406, lift 4.59x
    - 24h: 60 calls (60 a day), hit rate 0.867, chance 0.196, naive rule 0.421, lift 4.41x
    - 7d: 363 calls (52 a day), hit rate 0.868, chance 0.187, naive rule 0.394, lift 4.64x
    - 30d: 1582 calls (53 a day), hit rate 0.838, chance 0.187, naive rule 0.391, lift 4.49x
  - next: threshold 0.3966, hit rate recent 0.4207 / long run 0.4819
    - 6h: 38 calls (155 a day), hit rate 0.395, chance 0.191, lift 2.07x
    - 24h: 171 calls (172 a day), hit rate 0.444, chance 0.196, lift 2.26x
    - 7d: 578 calls (83 a day), hit rate 0.460, chance 0.187, lift 2.46x
    - 30d: 2006 calls (67 a day), hit rate 0.491, chance 0.187, lift 2.63x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 434, 0.410; 0.35: 375, 0.460; 0.40: 304, 0.528; 0.45: 249, 0.585; 0.50: 194, 0.645; 0.55: 148, 0.695; 0.60: 116, 0.738; 0.65: 88, 0.781; 0.70: 65, 0.819; 0.75: 35, 0.857; 0.80: 9, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.424; 0.40: 169, 0.447; 0.45: 89, 0.473; 0.50: 22, 0.514; 0.55: 3, 0.588
- **K=8**: model 1790553600, labels learned 88323, probability skill vs chance 0.2039, widened contest next: False
  - now: threshold 0.5638, hit rate recent 0.7854 / long run 0.731
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.123, naive rule 0.322, lift 7.53x
    - 24h: 52 calls (52 a day), hit rate 0.827, chance 0.128, naive rule 0.351, lift 6.47x
    - 7d: 326 calls (47 a day), hit rate 0.739, chance 0.122, naive rule 0.328, lift 6.06x
    - 30d: 1552 calls (52 a day), hit rate 0.718, chance 0.122, naive rule 0.327, lift 5.90x
  - next: threshold 0.3658, hit rate recent 0.3982 / long run 0.4054
    - 6h: 21 calls (86 a day), hit rate 0.476, chance 0.123, lift 3.89x
    - 24h: 56 calls (56 a day), hit rate 0.429, chance 0.128, lift 3.35x
    - 7d: 402 calls (57 a day), hit rate 0.378, chance 0.122, lift 3.10x
    - 30d: 2016 calls (67 a day), hit rate 0.400, chance 0.122, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 280, 0.394; 0.35: 211, 0.469; 0.40: 163, 0.534; 0.45: 129, 0.583; 0.50: 99, 0.625; 0.55: 70, 0.680; 0.60: 47, 0.723; 0.65: 25, 0.755; 0.70: 9, 0.796; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 191, 0.343; 0.35: 120, 0.380; 0.40: 49, 0.408; 0.45: 10, 0.431; 0.50: 1, 0.476
- **K=13**: model 1790208000, labels learned 88318, probability skill vs chance 0.186, widened contest next: False
  - now: threshold 0.4103, hit rate recent 0.6639 / long run 0.5915
    - 6h: 11 calls (46 a day), hit rate 0.909, chance 0.094, naive rule 0.312, lift 9.68x
    - 24h: 52 calls (53 a day), hit rate 0.673, chance 0.077, naive rule 0.271, lift 8.77x
    - 7d: 344 calls (49 a day), hit rate 0.584, chance 0.078, naive rule 0.263, lift 7.53x
    - 30d: 1429 calls (48 a day), hit rate 0.586, chance 0.076, naive rule 0.266, lift 7.67x
  - next: threshold 0.2608, hit rate recent 0.2838 / long run 0.2944
    - 6h: 21 calls (87 a day), hit rate 0.333, chance 0.094, lift 3.55x
    - 24h: 75 calls (76 a day), hit rate 0.267, chance 0.077, lift 3.47x
    - 7d: 606 calls (87 a day), hit rate 0.271, chance 0.078, lift 3.49x
    - 30d: 2003 calls (67 a day), hit rate 0.306, chance 0.076, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 125, 0.431; 0.35: 92, 0.488; 0.40: 66, 0.535; 0.45: 46, 0.593; 0.50: 30, 0.615; 0.55: 17, 0.655; 0.60: 7, 0.668; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.315; 0.35: 18, 0.350; 0.40: 4, 0.331; 0.45: 1, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 3.957 | 22.04% | 0.917 | 0.533 | 0.252 | 0.467 | -0.030 |
| 6h | 5.205 | 15.40% | 0.892 | 0.486 | 0.251 | 0.487 | 0.306 |
| 24h | 11.031 | 9.09% | 0.902 | 0.499 | 0.250 | 0.497 | 0.709 |
| 7d | 12.921 | 4.06% | 0.900 | 0.499 | 0.251 | 0.497 | 0.665 |
| 30d | 14.593 | 4.15% | 0.900 | 0.500 | 0.251 | 0.500 | 0.677 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.075 | 3.945 | 4.301 | 3.969 | 4.099 | 4.818 | 3.969 | 3.937 | 3.947 | 3.957 |
| 6h | 6.153 | 5.201 | 5.434 | 5.262 | 5.292 | 5.748 | 5.194 | 5.196 | 5.191 | 5.205 |
| 24h | 12.133 | 11.204 | 11.211 | 11.068 | 11.346 | 11.378 | 11.073 | 11.052 | 11.037 | 11.031 |
| 7d | 13.468 | 13.022 | 13.000 | 12.931 | 13.164 | 13.088 | 12.914 | 12.908 | 12.897 | 12.921 |
| 30d | 15.224 | 14.731 | 14.683 | 14.619 | 14.877 | 14.808 | 14.601 | 14.567 | 14.566 | 14.593 |

## Next candle

- candle starting 2026-10-03 12:14 UTC, last close 2683.31
- P(up) 0.4984, return quantiles (bp): {'05': -2.456, '10': -1.777, '25': -0.85, '40': -0.291, '50': -0.007, '60': 0.321, '75': 0.94, '90': 1.882, '95': 2.511}
- changepoint probability 0.0153, regime age 373.3 min
- agent weights: empirical 0.003, ewma 0.168, garch 0.031, har 0.189, bocpd 0.045, hmm 0.005, online_qr 0.261, lgbm 0.299

## Learning log

- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.66, 5.39, 13.26], current probabilities: [0.964, 0.036, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 12:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.192, 'l_abs': 0.656, 'l_hi': 0.777, 'l_lo': 0.738, 'b05': 0.651, 'b25': 0.714, 'b75': 0.649, 'b95': 0.668}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6]], 'cone_width': [1.449, 1.926, 2.141, 2.398, 2.852, 3.025, 3.24, 3.376, 3.426, 3.529, 3.548, 3.701, 3.697, 3.912]}
- calibration offsets (in sigma): {'05': 0.0665, '10': 0.073, '25': 0.0125, '40': -0.008, '50': -0.025, '60': -0.042, '75': -0.0225, '90': -0.063, '95': -0.0765}
