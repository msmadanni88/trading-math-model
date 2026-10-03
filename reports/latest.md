# ETH-USD 60s candle generator - report

- generated: 2026-10-03 00:12 UTC
- last closed candle: 2026-10-03 00:12 UTC (staleness 0.8 min)

## Goal keeper alerts

- none: on track

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.297 | 0.277 | 0.214 | 0.214 | 0.456 | 0.161 | 0.433 | 2.318 |
| 6h | 360 | 0.342 | 0.342 | 0.267 | 0.291 | 0.515 | 0.222 | 0.461 | 1.656 |
| 24h | 1440 | 0.362 | 0.364 | 0.289 | 0.318 | 0.505 | 0.236 | 0.487 | 1.324 |
| 7d | 10080 | 0.359 | 0.357 | 0.287 | 0.315 | 0.505 | 0.244 | 0.474 | 1.325 |
| 30d | 43200 | 0.357 | 0.357 | 0.281 | 0.311 | 0.501 | 0.246 | 0.469 | 1.270 |

## Candles generated further ahead (score / colour right / 90% cone held the close)

- 1h: 1 min ahead 0.297 / 0.456 / -; 2 min ahead 0.296 / 0.509 / 0.867; 3 min ahead 0.288 / 0.386 / 0.817; 4 min ahead 0.285 / 0.439 / 0.850; 5 min ahead 0.281 / 0.421 / 0.850
- 6h: 1 min ahead 0.342 / 0.515 / -; 2 min ahead 0.340 / 0.499 / 0.900; 3 min ahead 0.351 / 0.504 / 0.903; 4 min ahead 0.342 / 0.513 / 0.925; 5 min ahead 0.335 / 0.515 / 0.914
- 24h: 1 min ahead 0.362 / 0.505 / -; 2 min ahead 0.359 / 0.497 / 0.900; 3 min ahead 0.361 / 0.520 / 0.897; 4 min ahead 0.358 / 0.507 / 0.900; 5 min ahead 0.355 / 0.508 / 0.900
- 7d: 1 min ahead 0.359 / 0.505 / -; 2 min ahead 0.358 / 0.511 / 0.900; 3 min ahead 0.357 / 0.512 / 0.900; 4 min ahead 0.355 / 0.507 / 0.900; 5 min ahead 0.353 / 0.510 / 0.900
- 30d: 1 min ahead 0.357 / 0.501 / -; 2 min ahead 0.357 / 0.510 / 0.900; 3 min ahead 0.355 / 0.506 / 0.900; 4 min ahead 0.354 / 0.505 / 0.900; 5 min ahead 0.353 / 0.503 / 0.900

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.530 | 33.27% | 0.933 | 0.700 | 0.252 | 0.404 | -0.023 |
| 6h | 12.112 | 9.47% | 0.933 | 0.575 | 0.250 | 0.507 | 0.606 |
| 24h | 15.411 | 3.74% | 0.912 | 0.522 | 0.250 | 0.501 | 0.564 |
| 7d | 12.998 | 3.94% | 0.901 | 0.502 | 0.251 | 0.493 | 0.659 |
| 30d | 14.741 | 4.02% | 0.900 | 0.501 | 0.251 | 0.499 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.789 | 4.529 | 5.084 | 4.651 | 4.905 | 5.344 | 4.585 | 4.534 | 4.690 | 4.530 |
| 6h | 13.379 | 12.533 | 12.255 | 12.152 | 12.654 | 12.431 | 12.196 | 12.121 | 12.157 | 12.112 |
| 24h | 16.010 | 15.655 | 15.520 | 15.436 | 15.847 | 15.521 | 15.465 | 15.398 | 15.406 | 15.411 |
| 7d | 13.532 | 13.102 | 13.077 | 13.008 | 13.246 | 13.184 | 12.993 | 12.983 | 12.975 | 12.998 |
| 30d | 15.358 | 14.881 | 14.831 | 14.767 | 15.028 | 14.950 | 14.749 | 14.715 | 14.713 | 14.741 |

## Next candle

- candle starting 2026-10-03 00:12 UTC, last close 2667.29
- P(up) 0.485, return quantiles (bp): {'05': -4.498, '10': -3.283, '25': -1.322, '40': -0.352, '50': -0.078, '60': 0.453, '75': 1.232, '90': 2.932, '95': 4.167}
- changepoint probability 0.193, regime age 136.7 min
- agent weights: empirical 0.003, ewma 0.049, garch 0.112, har 0.256, bocpd 0.016, hmm 0.064, online_qr 0.189, lgbm 0.311

## Learning log

- 2026-09-30 22:49 UTC: {"garch": {"alpha": 0.0806, "beta": 0.9066}, "hmm": {"sd_bp": [2.34, 4.92, 11.18], "stay": [0.963, 0.967, 0.949]}}
- 2026-10-01 10:49 UTC: {"garch": {"alpha": 0.078, "beta": 0.9062}, "hmm": {"sd_bp": [2.67, 5.06, 11.24], "stay": [0.948, 0.96, 0.953]}}
- 2026-10-01 22:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8986}, "hmm": {"sd_bp": [2.92, 5.28, 11.17], "stay": [0.943, 0.952, 0.951]}, "lgbm": {"challenger_loss": 0.25503, "champion_loss": 0.25511, "promoted": true}}
- 2026-10-02 10:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8964}, "hmm": {"sd_bp": [3.09, 5.46, 12.16], "stay": [0.948, 0.95, 0.933]}}
- 2026-10-02 22:49 UTC: {"garch": {"alpha": 0.1051, "beta": 0.8596}, "hmm": {"sd_bp": [3.17, 5.67, 12.93], "stay": [0.957, 0.947, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.67, 12.93], current probabilities: [0.729, 0.263, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 00:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.345, 'l_abs': 0.704, 'l_hi': 0.774, 'l_lo': 0.73, 'b05': 0.696, 'b25': 0.706, 'b75': 0.681, 'b95': 0.702}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.343, 1.648, 1.725, 1.971]}
- calibration offsets (in sigma): {'05': 0.061, '10': 0.072, '25': 0.145, '40': 0.108, '50': -0.01, '60': -0.048, '75': -0.155, '90': -0.182, '95': -0.171}
