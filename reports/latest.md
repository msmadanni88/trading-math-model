# ETH-USD 60s candle generator - report

- generated: 2026-10-03 07:03 UTC
- last closed candle: 2026-10-03 07:03 UTC (staleness 0.2 min)

## Goal keeper alerts

- none: on track

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.321 | 0.328 | 0.232 | 0.232 | 0.467 | 0.223 | 0.419 | 0.985 |
| 6h | 360 | 0.320 | 0.323 | 0.254 | 0.271 | 0.483 | 0.224 | 0.416 | 1.193 |
| 24h | 1440 | 0.348 | 0.353 | 0.277 | 0.306 | 0.494 | 0.231 | 0.465 | 1.430 |
| 7d | 10080 | 0.358 | 0.357 | 0.286 | 0.314 | 0.503 | 0.243 | 0.473 | 1.334 |
| 30d | 43200 | 0.357 | 0.356 | 0.280 | 0.311 | 0.500 | 0.245 | 0.468 | 1.273 |

## Candles generated further ahead (score / colour right / 90% cone held the close)

- 1h: 1 min ahead 0.321 / 0.467 / -; 2 min ahead 0.339 / 0.517 / 0.917; 3 min ahead 0.346 / 0.567 / 0.917; 4 min ahead 0.366 / 0.600 / 0.933; 5 min ahead 0.338 / 0.583 / 0.967
- 6h: 1 min ahead 0.320 / 0.483 / -; 2 min ahead 0.334 / 0.480 / 0.906; 3 min ahead 0.330 / 0.480 / 0.917; 4 min ahead 0.339 / 0.503 / 0.922; 5 min ahead 0.331 / 0.508 / 0.939
- 24h: 1 min ahead 0.348 / 0.494 / -; 2 min ahead 0.351 / 0.491 / 0.901; 3 min ahead 0.349 / 0.497 / 0.898; 4 min ahead 0.349 / 0.496 / 0.899; 5 min ahead 0.346 / 0.500 / 0.903
- 7d: 1 min ahead 0.358 / 0.503 / -; 2 min ahead 0.358 / 0.509 / 0.900; 3 min ahead 0.357 / 0.511 / 0.900; 4 min ahead 0.355 / 0.506 / 0.900; 5 min ahead 0.353 / 0.510 / 0.901
- 30d: 1 min ahead 0.357 / 0.500 / -; 2 min ahead 0.357 / 0.509 / 0.900; 3 min ahead 0.355 / 0.506 / 0.900; 4 min ahead 0.353 / 0.505 / 0.900; 5 min ahead 0.353 / 0.503 / 0.900

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.146 | 13.83% | 0.883 | 0.433 | 0.250 | 0.517 | 0.240 |
| 6h | 6.362 | 15.79% | 0.889 | 0.450 | 0.252 | 0.472 | 0.302 |
| 24h | 13.019 | 6.51% | 0.910 | 0.503 | 0.250 | 0.495 | 0.641 |
| 7d | 12.957 | 4.05% | 0.900 | 0.500 | 0.251 | 0.493 | 0.662 |
| 30d | 14.663 | 4.09% | 0.900 | 0.500 | 0.251 | 0.499 | 0.675 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.133 | 6.205 | 6.426 | 6.152 | 6.291 | 6.597 | 6.102 | 6.136 | 6.112 | 6.146 |
| 6h | 7.555 | 6.398 | 6.673 | 6.376 | 6.628 | 6.811 | 6.350 | 6.327 | 6.339 | 6.362 |
| 24h | 13.927 | 13.238 | 13.197 | 13.037 | 13.398 | 13.256 | 13.093 | 13.024 | 13.022 | 13.019 |
| 7d | 13.504 | 13.063 | 13.039 | 12.966 | 13.208 | 13.136 | 12.951 | 12.942 | 12.933 | 12.957 |
| 30d | 15.288 | 14.801 | 14.755 | 14.689 | 14.949 | 14.876 | 14.671 | 14.636 | 14.635 | 14.663 |

## Next candle

- candle starting 2026-10-03 07:03 UTC, last close 2679.63
- P(up) 0.4794, return quantiles (bp): {'05': -3.846, '10': -2.759, '25': -1.335, '40': -0.561, '50': -0.122, '60': 0.48, '75': 1.391, '90': 2.822, '95': 3.741}
- changepoint probability 0.3427, regime age 35.1 min
- agent weights: empirical 0.003, ewma 0.105, garch 0.038, har 0.250, bocpd 0.024, hmm 0.015, online_qr 0.242, lgbm 0.323

## Learning log

- 2026-09-30 22:49 UTC: {"garch": {"alpha": 0.0806, "beta": 0.9066}, "hmm": {"sd_bp": [2.34, 4.92, 11.18], "stay": [0.963, 0.967, 0.949]}}
- 2026-10-01 10:49 UTC: {"garch": {"alpha": 0.078, "beta": 0.9062}, "hmm": {"sd_bp": [2.67, 5.06, 11.24], "stay": [0.948, 0.96, 0.953]}}
- 2026-10-01 22:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8986}, "hmm": {"sd_bp": [2.92, 5.28, 11.17], "stay": [0.943, 0.952, 0.951]}, "lgbm": {"challenger_loss": 0.25503, "champion_loss": 0.25511, "promoted": true}}
- 2026-10-02 10:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8964}, "hmm": {"sd_bp": [3.09, 5.46, 12.16], "stay": [0.948, 0.95, 0.933]}}
- 2026-10-02 22:49 UTC: {"garch": {"alpha": 0.1051, "beta": 0.8596}, "hmm": {"sd_bp": [3.17, 5.67, 12.93], "stay": [0.957, 0.947, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.67, 12.93], current probabilities: [0.9, 0.098, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 07:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.219, 'l_abs': 0.717, 'l_hi': 0.781, 'l_lo': 0.736, 'b05': 0.681, 'b25': 0.72, 'b75': 0.677, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6]], 'cone_width': [1.367, 1.678, 1.865, 1.853]}
- calibration offsets (in sigma): {'05': 0.0765, '10': 0.093, '25': 0.0625, '40': 0.002, '50': -0.035, '60': -0.002, '75': -0.0125, '90': -0.053, '95': -0.0865}
