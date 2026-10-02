# ETH-USD 60s candle generator - report

- generated: 2026-10-02 22:59 UTC
- last closed candle: 2026-10-02 22:59 UTC (staleness 0.7 min)

## Goal keeper alerts

- none: on track

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.345 | 0.344 | 0.264 | 0.264 | 0.467 | 0.225 | 0.465 | 1.364 |
| 6h | 360 | 0.358 | 0.362 | 0.286 | 0.310 | 0.510 | 0.238 | 0.478 | 1.450 |
| 24h | 1440 | 0.365 | 0.368 | 0.294 | 0.324 | 0.507 | 0.239 | 0.490 | 1.290 |
| 7d | 10080 | 0.359 | 0.358 | 0.287 | 0.315 | 0.505 | 0.244 | 0.474 | 1.319 |
| 30d | 43200 | 0.357 | 0.357 | 0.281 | 0.311 | 0.501 | 0.246 | 0.469 | 1.268 |

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.929 | 11.32% | 0.883 | 0.583 | 0.252 | 0.450 | 0.313 |
| 6h | 14.024 | 5.76% | 0.928 | 0.528 | 0.250 | 0.513 | 0.558 |
| 24h | 15.585 | 3.25% | 0.911 | 0.512 | 0.250 | 0.501 | 0.552 |
| 7d | 13.008 | 3.91% | 0.901 | 0.501 | 0.251 | 0.492 | 0.659 |
| 30d | 14.752 | 3.99% | 0.900 | 0.500 | 0.251 | 0.499 | 0.672 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.941 | 7.991 | 8.059 | 7.933 | 8.078 | 8.123 | 7.971 | 7.891 | 7.948 | 7.929 |
| 6h | 14.881 | 14.464 | 14.074 | 14.048 | 14.529 | 14.214 | 14.104 | 14.020 | 14.035 | 14.024 |
| 24h | 16.108 | 15.830 | 15.670 | 15.602 | 16.007 | 15.663 | 15.637 | 15.570 | 15.571 | 15.585 |
| 7d | 13.537 | 13.112 | 13.085 | 13.017 | 13.254 | 13.194 | 13.002 | 12.993 | 12.983 | 13.008 |
| 30d | 15.365 | 14.892 | 14.841 | 14.777 | 15.038 | 14.960 | 14.760 | 14.725 | 14.724 | 14.752 |

## Next candle

- candle starting 2026-10-02 22:59 UTC, last close 2668.0
- P(up) 0.4909, return quantiles (bp): {'05': -5.286, '10': -3.934, '25': -1.612, '40': -0.577, '50': -0.069, '60': 0.703, '75': 1.747, '90': 3.598, '95': 4.784}
- changepoint probability 0.0486, regime age 117.6 min
- agent weights: empirical 0.003, ewma 0.032, garch 0.166, har 0.248, bocpd 0.014, hmm 0.111, online_qr 0.158, lgbm 0.268

## Learning log

- 2026-09-30 22:49 UTC: {"garch": {"alpha": 0.0806, "beta": 0.9066}, "hmm": {"sd_bp": [2.34, 4.92, 11.18], "stay": [0.963, 0.967, 0.949]}}
- 2026-10-01 10:49 UTC: {"garch": {"alpha": 0.078, "beta": 0.9062}, "hmm": {"sd_bp": [2.67, 5.06, 11.24], "stay": [0.948, 0.96, 0.953]}}
- 2026-10-01 22:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8986}, "hmm": {"sd_bp": [2.92, 5.28, 11.17], "stay": [0.943, 0.952, 0.951]}, "lgbm": {"challenger_loss": 0.25503, "champion_loss": 0.25511, "promoted": true}}
- 2026-10-02 10:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8964}, "hmm": {"sd_bp": [3.09, 5.46, 12.16], "stay": [0.948, 0.95, 0.933]}}
- 2026-10-02 22:49 UTC: {"garch": {"alpha": 0.1051, "beta": 0.8596}, "hmm": {"sd_bp": [3.17, 5.67, 12.93], "stay": [0.957, 0.947, 0.919]}, "lgbm": {"challenger_loss": 0.24913, "champion_loss": 0.249, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.17, 5.67, 12.93], current probabilities: [0.751, 0.244, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-02 23:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.339, 'l_abs': 0.713, 'l_hi': 0.787, 'l_lo': 0.745, 'b05': 0.756, 'b25': 0.71, 'b75': 0.692, 'b95': 0.727}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4}
- calibration offsets (in sigma): {'05': 0.0445, '10': 0.029, '25': 0.1125, '40': 0.046, '50': -0.005, '60': 0.004, '75': -0.0625, '90': -0.139, '95': -0.1545}
