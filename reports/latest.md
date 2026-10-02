# ETH-USD 60s candle generator - report

- generated: 2026-10-02 22:49 UTC
- last closed candle: 2026-10-02 22:49 UTC (staleness 0.4 min)

## Goal keeper alerts

- none: on track

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.359 | 0.366 | 0.266 | 0.266 | 0.483 | 0.222 | 0.497 | 1.908 |
| 6h | 360 | 0.366 | 0.369 | 0.290 | 0.313 | 0.518 | 0.245 | 0.487 | 1.546 |
| 24h | 1440 | 0.365 | 0.369 | 0.295 | 0.325 | 0.507 | 0.239 | 0.491 | 1.302 |
| 7d | 10080 | 0.359 | 0.358 | 0.287 | 0.315 | 0.505 | 0.244 | 0.474 | 1.320 |
| 30d | 43200 | 0.357 | 0.357 | 0.281 | 0.311 | 0.501 | 0.246 | 0.469 | 1.269 |

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.387 | 13.46% | 0.917 | 0.683 | 0.252 | 0.483 | 0.349 |
| 6h | 13.957 | 5.80% | 0.936 | 0.542 | 0.250 | 0.521 | 0.554 |
| 24h | 15.583 | 3.23% | 0.912 | 0.515 | 0.250 | 0.502 | 0.552 |
| 7d | 13.003 | 3.92% | 0.901 | 0.501 | 0.251 | 0.493 | 0.659 |
| 30d | 14.751 | 4.00% | 0.900 | 0.501 | 0.251 | 0.499 | 0.672 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.536 | 7.395 | 7.586 | 7.389 | 7.587 | 7.669 | 7.424 | 7.343 | 7.436 | 7.387 |
| 6h | 14.817 | 14.400 | 14.013 | 13.997 | 14.477 | 14.154 | 14.045 | 13.970 | 13.981 | 13.957 |
| 24h | 16.104 | 15.827 | 15.670 | 15.601 | 16.007 | 15.664 | 15.636 | 15.570 | 15.570 | 15.583 |
| 7d | 13.533 | 13.106 | 13.080 | 13.012 | 13.250 | 13.190 | 12.997 | 12.987 | 12.978 | 13.003 |
| 30d | 15.365 | 14.892 | 14.840 | 14.777 | 15.038 | 14.959 | 14.759 | 14.725 | 14.723 | 14.751 |

## Next candle

- candle starting 2026-10-02 22:49 UTC, last close 2667.0
- P(up) 0.4889, return quantiles (bp): {'05': -4.445, '10': -3.349, '25': -1.312, '40': -0.49, '50': -0.064, '60': 0.525, '75': 1.382, '90': 2.942, '95': 4.035}
- changepoint probability 0.0185, regime age 105.8 min
- agent weights: empirical 0.003, ewma 0.032, garch 0.161, har 0.246, bocpd 0.013, hmm 0.107, online_qr 0.162, lgbm 0.275

## Learning log

- 2026-09-30 10:49 UTC: {"garch": {"alpha": 0.0696, "beta": 0.9212}, "hmm": {"sd_bp": [2.21, 4.77, 10.43], "stay": [0.968, 0.964, 0.941]}}
- 2026-09-30 22:49 UTC: {"garch": {"alpha": 0.0806, "beta": 0.9066}, "hmm": {"sd_bp": [2.34, 4.92, 11.18], "stay": [0.963, 0.967, 0.949]}}
- 2026-10-01 10:49 UTC: {"garch": {"alpha": 0.078, "beta": 0.9062}, "hmm": {"sd_bp": [2.67, 5.06, 11.24], "stay": [0.948, 0.96, 0.953]}}
- 2026-10-01 22:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8986}, "hmm": {"sd_bp": [2.92, 5.28, 11.17], "stay": [0.943, 0.952, 0.951]}, "lgbm": {"challenger_loss": 0.25503, "champion_loss": 0.25511, "promoted": true}}
- 2026-10-02 10:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8964}, "hmm": {"sd_bp": [3.09, 5.46, 12.16], "stay": [0.948, 0.95, 0.933]}}
- HMM volatility states (sd, bp per minute): [3.09, 5.46, 12.16], current probabilities: [0.904, 0.093, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-02 23:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.337, 'l_abs': 0.717, 'l_hi': 0.788, 'l_lo': 0.748, 'b05': 0.757, 'b25': 0.711, 'b75': 0.695, 'b95': 0.729}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4}
- calibration offsets (in sigma): {'05': 0.0595, '10': 0.039, '25': 0.1175, '40': 0.036, '50': -0.015, '60': -0.016, '75': -0.0875, '90': -0.159, '95': -0.1595}
