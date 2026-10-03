# ETH-USD 60s candle generator - report

- generated: 2026-10-03 16:37 UTC
- last closed candle: 2026-10-03 16:37 UTC (staleness 0.8 min)
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
| 1h | 60 | 0.300 | 0.319 | 0.230 | 0.230 | 0.450 | 0.199 | 0.401 | 2.028 |
| 6h | 360 | 0.307 | 0.305 | 0.236 | 0.245 | 0.506 | 0.222 | 0.392 | 1.258 |
| 24h | 1440 | 0.328 | 0.326 | 0.252 | 0.271 | 0.504 | 0.229 | 0.427 | 1.152 |
| 7d | 10080 | 0.357 | 0.357 | 0.286 | 0.313 | 0.504 | 0.243 | 0.472 | 1.346 |
| 30d | 43200 | 0.356 | 0.356 | 0.280 | 0.310 | 0.501 | 0.245 | 0.467 | 1.280 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.300 / 0.450 / 0.900; 2: 0.304 / 0.517 / 0.933; 3: 0.283 / 0.517 / 0.900; 4: 0.309 / 0.567 / 0.883; 5: 0.291 / 0.533 / 0.867; 6: 0.265 / 0.500 / 0.867; 7: 0.253 / 0.367 / 0.850; 8: 0.265 / 0.417 / 0.850; 9: 0.290 / 0.467 / 0.850; 10: 0.305 / 0.617 / 0.883; 11: 0.286 / 0.533 / 0.867; 12: 0.284 / 0.567 / 0.850; 13: 0.298 / 0.550 / 0.850; 14: 0.295 / 0.517 / 0.967; 15: 0.282 / 0.483 / 0.933
- 6h: 1: 0.307 / 0.506 / 0.864; 2: 0.308 / 0.500 / 0.894; 3: 0.300 / 0.514 / 0.894; 4: 0.317 / 0.534 / 0.889; 5: 0.305 / 0.508 / 0.889; 6: 0.302 / 0.508 / 0.889; 7: 0.311 / 0.483 / 0.886; 8: 0.298 / 0.472 / 0.894; 9: 0.301 / 0.483 / 0.900; 10: 0.319 / 0.554 / 0.906; 11: 0.315 / 0.551 / 0.883; 12: 0.305 / 0.497 / 0.872; 13: 0.318 / 0.525 / 0.856; 14: 0.307 / 0.469 / 0.867; 15: 0.298 / 0.452 / 0.886
- 24h: 1: 0.328 / 0.504 / 0.894; 2: 0.327 / 0.492 / 0.896; 3: 0.329 / 0.498 / 0.897; 4: 0.329 / 0.510 / 0.899; 5: 0.325 / 0.507 / 0.899; 6: 0.321 / 0.476 / 0.892; 7: 0.327 / 0.490 / 0.892; 8: 0.321 / 0.486 / 0.896; 9: 0.320 / 0.483 / 0.897; 10: 0.323 / 0.489 / 0.900; 11: 0.332 / 0.546 / 0.897; 12: 0.324 / 0.502 / 0.894; 13: 0.327 / 0.506 / 0.894; 14: 0.325 / 0.491 / 0.897; 15: 0.316 / 0.466 / 0.900
- 7d: 1: 0.357 / 0.504 / 0.899; 2: 0.352 / 0.491 / 0.900; 3: 0.355 / 0.508 / 0.900; 4: 0.352 / 0.494 / 0.900; 5: 0.352 / 0.508 / 0.900; 6: 0.350 / 0.501 / 0.899; 7: 0.351 / 0.498 / 0.899; 8: 0.350 / 0.506 / 0.899; 9: 0.347 / 0.494 / 0.899; 10: 0.349 / 0.504 / 0.900; 11: 0.349 / 0.506 / 0.899; 12: 0.351 / 0.509 / 0.899; 13: 0.350 / 0.504 / 0.898; 14: 0.347 / 0.496 / 0.899; 15: 0.347 / 0.499 / 0.899
- 30d: 1: 0.356 / 0.501 / 0.899; 2: 0.353 / 0.497 / 0.900; 3: 0.354 / 0.506 / 0.900; 4: 0.351 / 0.499 / 0.900; 5: 0.351 / 0.502 / 0.900; 6: 0.351 / 0.505 / 0.900; 7: 0.351 / 0.506 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.499 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.348 / 0.502 / 0.900; 12: 0.348 / 0.501 / 0.900; 13: 0.347 / 0.500 / 0.900; 14: 0.346 / 0.495 / 0.900; 15: 0.345 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.067 (body 0.036, range 0.098); 'price stays where it was' would score 0.050; colour right 0.567; typical miss of the close 3.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.087 (body 0.061, range 0.113); 'price stays where it was' would score 0.073; colour right 0.489; typical miss of the close 3.9 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.112 (body 0.072, range 0.152); 'price stays where it was' would score 0.112; colour right 0.505; typical miss of the close 4.7 bp; chain ended on the right side 0.558 of 95 chains; n=1440
- 7d: match 0.118 (body 0.077, range 0.158); 'price stays where it was' would score 0.118; colour right 0.495; typical miss of the close 7.7 bp; chain ended on the right side 0.527 of 670 chains; n=10080
- 30d: match 0.122 (body 0.081, range 0.162); 'price stays where it was' would score 0.128; colour right 0.498; typical miss of the close 8.3 bp; chain ended on the right side 0.511 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.4; 2: 0.197 / 4.5; 3: 0.169 / 6.3; 4: 0.133 / 6.6; 5: 0.122 / 7.4; 6: 0.113 / 8.3; 7: 0.102 / 8.7; 8: 0.093 / 9.3; 9: 0.089 / 9.4; 10: 0.085 / 10.3; 11: 0.078 / 10.8; 12: 0.077 / 11.2; 13: 0.068 / 11.6; 14: 0.068 / 11.6; 15: 0.063 / 12.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 88591, probability skill vs chance 0.2276, widened contest next: True
  - now: threshold 0.8393, hit rate recent 0.9156 / long run 0.9404
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.286, naive rule 0.458, lift 2.91x
    - 24h: 53 calls (53 a day), hit rate 0.887, chance 0.289, naive rule 0.491, lift 3.07x
    - 7d: 386 calls (55 a day), hit rate 0.948, chance 0.289, naive rule 0.483, lift 3.28x
    - 30d: 1710 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.481, lift 3.22x
  - next: threshold 0.533, hit rate recent 0.5074 / long run 0.5729
    - 6h: 43 calls (174 a day), hit rate 0.488, chance 0.286, lift 1.71x
    - 24h: 117 calls (117 a day), hit rate 0.496, chance 0.289, lift 1.71x
    - 7d: 659 calls (94 a day), hit rate 0.574, chance 0.289, lift 1.99x
    - 30d: 2405 calls (80 a day), hit rate 0.583, chance 0.292, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.493; 0.35: 538, 0.518; 0.40: 490, 0.558; 0.45: 424, 0.624; 0.50: 370, 0.679; 0.55: 323, 0.724; 0.60: 275, 0.765; 0.65: 225, 0.801; 0.70: 183, 0.833; 0.75: 141, 0.867; 0.80: 100, 0.906; 0.85: 49, 0.949; 0.90: 1, 0.971
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 496, 0.459; 0.40: 413, 0.487; 0.45: 317, 0.519; 0.50: 209, 0.549; 0.55: 94, 0.585; 0.60: 13, 0.607; 0.65: 0, 0.750
- **K=5**: model 1790208000, labels learned 88589, probability skill vs chance 0.2203, widened contest next: True
  - now: threshold 0.7087, hit rate recent 0.8379 / long run 0.8405
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.184, naive rule 0.369, lift 4.41x
    - 24h: 58 calls (58 a day), hit rate 0.810, chance 0.191, naive rule 0.400, lift 4.25x
    - 7d: 363 calls (52 a day), hit rate 0.862, chance 0.186, naive rule 0.391, lift 4.64x
    - 30d: 1582 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.48x
  - next: threshold 0.3966, hit rate recent 0.3858 / long run 0.474
    - 6h: 43 calls (175 a day), hit rate 0.372, chance 0.184, lift 2.02x
    - 24h: 176 calls (177 a day), hit rate 0.409, chance 0.191, lift 2.14x
    - 7d: 606 calls (87 a day), hit rate 0.452, chance 0.186, lift 2.43x
    - 30d: 2029 calls (68 a day), hit rate 0.487, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 434, 0.410; 0.35: 375, 0.461; 0.40: 303, 0.529; 0.45: 248, 0.586; 0.50: 194, 0.646; 0.55: 148, 0.696; 0.60: 116, 0.738; 0.65: 88, 0.780; 0.70: 65, 0.819; 0.75: 35, 0.855; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.423; 0.40: 169, 0.447; 0.45: 89, 0.472; 0.50: 23, 0.513; 0.55: 3, 0.578
- **K=8**: model 1790553600, labels learned 88586, probability skill vs chance 0.2063, widened contest next: False
  - now: threshold 0.5638, hit rate recent 0.7781 / long run 0.7308
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.123, naive rule 0.336, lift 5.92x
    - 24h: 48 calls (48 a day), hit rate 0.792, chance 0.120, naive rule 0.329, lift 6.60x
    - 7d: 324 calls (46 a day), hit rate 0.741, chance 0.122, naive rule 0.327, lift 6.09x
    - 30d: 1548 calls (52 a day), hit rate 0.718, chance 0.122, naive rule 0.327, lift 5.90x
  - next: threshold 0.3658, hit rate recent 0.4018 / long run 0.4053
    - 6h: 21 calls (86 a day), hit rate 0.429, chance 0.123, lift 3.49x
    - 24h: 62 calls (62 a day), hit rate 0.403, chance 0.120, lift 3.36x
    - 7d: 408 calls (58 a day), hit rate 0.373, chance 0.122, lift 3.06x
    - 30d: 2016 calls (67 a day), hit rate 0.399, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 279, 0.395; 0.35: 210, 0.470; 0.40: 163, 0.534; 0.45: 129, 0.584; 0.50: 98, 0.625; 0.55: 69, 0.679; 0.60: 46, 0.722; 0.65: 25, 0.755; 0.70: 9, 0.796; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 191, 0.343; 0.35: 120, 0.380; 0.40: 50, 0.407; 0.45: 10, 0.430; 0.50: 1, 0.452
- **K=13**: model 1790208000, labels learned 88581, probability skill vs chance 0.1921, widened contest next: False
  - now: threshold 0.4103, hit rate recent 0.6708 / long run 0.593
    - 6h: 11 calls (46 a day), hit rate 0.727, chance 0.094, naive rule 0.318, lift 7.72x
    - 24h: 48 calls (49 a day), hit rate 0.708, chance 0.081, naive rule 0.285, lift 8.70x
    - 7d: 342 calls (49 a day), hit rate 0.591, chance 0.078, naive rule 0.265, lift 7.53x
    - 30d: 1425 calls (48 a day), hit rate 0.587, chance 0.077, naive rule 0.267, lift 7.66x
  - next: threshold 0.2608, hit rate recent 0.3111 / long run 0.2968
    - 6h: 24 calls (100 a day), hit rate 0.333, chance 0.094, lift 3.54x
    - 24h: 81 calls (82 a day), hit rate 0.321, chance 0.081, lift 3.94x
    - 7d: 614 calls (88 a day), hit rate 0.270, chance 0.078, lift 3.45x
    - 30d: 1993 calls (66 a day), hit rate 0.307, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.432; 0.35: 91, 0.489; 0.40: 65, 0.536; 0.45: 46, 0.594; 0.50: 29, 0.615; 0.55: 17, 0.654; 0.60: 7, 0.671; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.316; 0.35: 18, 0.348; 0.40: 4, 0.328; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.130 | 9.07% | 0.900 | 0.617 | 0.246 | 0.617 | 0.204 |
| 6h | 4.843 | 10.56% | 0.872 | 0.519 | 0.250 | 0.523 | 0.205 |
| 24h | 7.782 | 10.81% | 0.897 | 0.504 | 0.250 | 0.500 | 0.659 |
| 7d | 12.879 | 4.09% | 0.900 | 0.502 | 0.251 | 0.496 | 0.668 |
| 30d | 14.473 | 4.16% | 0.900 | 0.500 | 0.251 | 0.499 | 0.678 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 4.542 | 4.221 | 4.301 | 4.110 | 4.375 | 4.767 | 4.102 | 4.134 | 4.135 | 4.130 |
| 6h | 5.414 | 4.873 | 4.972 | 4.889 | 4.995 | 5.313 | 4.830 | 4.820 | 4.831 | 4.843 |
| 24h | 8.725 | 7.907 | 7.948 | 7.820 | 8.038 | 8.166 | 7.802 | 7.777 | 7.785 | 7.782 |
| 7d | 13.428 | 12.979 | 12.959 | 12.890 | 13.122 | 13.045 | 12.871 | 12.866 | 12.855 | 12.879 |
| 30d | 15.102 | 14.612 | 14.563 | 14.500 | 14.756 | 14.689 | 14.481 | 14.446 | 14.446 | 14.473 |

## Next candle

- candle starting 2026-10-03 16:37 UTC, last close 2681.11
- P(up) 0.5272, return quantiles (bp): {'05': -2.361, '10': -1.651, '25': -0.757, '40': -0.179, '50': 0.064, '60': 0.209, '75': 0.726, '90': 1.703, '95': 2.322}
- changepoint probability 0.0222, regime age 547.8 min
- agent weights: empirical 0.003, ewma 0.151, garch 0.050, har 0.173, bocpd 0.035, hmm 0.004, online_qr 0.282, lgbm 0.302

## Learning log

- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.66, 5.39, 13.26], current probabilities: [0.966, 0.034, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 16:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.18, 'l_abs': 0.633, 'l_hi': 0.768, 'l_lo': 0.725, 'b05': 0.645, 'b25': 0.681, 'b75': 0.637, 'b95': 0.664}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.469, 1.992, 2.448, 2.742, 3.133, 3.39, 3.489, 3.635, 3.544, 4.116, 4.574, 5.066, 4.672, 4.384]}
- calibration offsets (in sigma): {'05': 0.008, '10': 0.046, '25': 0.06, '40': 0.044, '50': 0.04, '60': -0.044, '75': -0.06, '90': -0.016, '95': -0.028}
