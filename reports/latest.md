# ETH-USD 60s candle generator - report

- generated: 2026-10-02 23:53 UTC
- last closed candle: 2026-10-02 23:53 UTC (staleness 0.5 min)

## Goal keeper alerts

- none: on track

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.303 | 0.289 | 0.198 | 0.198 | 0.466 | 0.191 | 0.415 | 1.984 |
| 6h | 360 | 0.350 | 0.351 | 0.272 | 0.297 | 0.513 | 0.231 | 0.469 | 1.660 |
| 24h | 1440 | 0.364 | 0.366 | 0.290 | 0.320 | 0.506 | 0.239 | 0.489 | 1.318 |
| 7d | 10080 | 0.359 | 0.357 | 0.287 | 0.315 | 0.505 | 0.244 | 0.474 | 1.324 |
| 30d | 43200 | 0.357 | 0.357 | 0.281 | 0.311 | 0.501 | 0.246 | 0.469 | 1.270 |

## Candles generated further ahead (score / colour right / 90% cone held the close)

- 1h: 1 min ahead 0.303 / 0.466 / -; 2 min ahead 0.315 / 0.517 / 0.933; 3 min ahead 0.301 / 0.397 / 0.950; 4 min ahead 0.300 / 0.483 / 0.917; 5 min ahead 0.285 / 0.448 / 0.933
- 6h: 1 min ahead 0.350 / 0.513 / -; 2 min ahead 0.344 / 0.476 / 0.914; 3 min ahead 0.358 / 0.504 / 0.922; 4 min ahead 0.350 / 0.515 / 0.936; 5 min ahead 0.344 / 0.521 / 0.931
- 24h: 1 min ahead 0.364 / 0.506 / -; 2 min ahead 0.361 / 0.498 / 0.902; 3 min ahead 0.363 / 0.522 / 0.901; 4 min ahead 0.359 / 0.507 / 0.902; 5 min ahead 0.356 / 0.506 / 0.902
- 7d: 1 min ahead 0.359 / 0.505 / -; 2 min ahead 0.358 / 0.510 / 0.900; 3 min ahead 0.357 / 0.512 / 0.901; 4 min ahead 0.355 / 0.507 / 0.901; 5 min ahead 0.354 / 0.510 / 0.900
- 30d: 1 min ahead 0.357 / 0.501 / -; 2 min ahead 0.357 / 0.510 / 0.900; 3 min ahead 0.355 / 0.506 / 0.900; 4 min ahead 0.354 / 0.505 / 0.900; 5 min ahead 0.353 / 0.503 / 0.900

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.980 | 29.54% | 0.967 | 0.617 | 0.251 | 0.466 | 0.140 |
| 6h | 12.389 | 8.80% | 0.939 | 0.564 | 0.250 | 0.513 | 0.596 |
| 24h | 15.458 | 3.63% | 0.913 | 0.519 | 0.250 | 0.502 | 0.561 |
| 7d | 13.002 | 3.93% | 0.901 | 0.501 | 0.251 | 0.492 | 0.659 |
| 30d | 14.744 | 4.01% | 0.900 | 0.501 | 0.251 | 0.499 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.068 | 4.977 | 5.487 | 5.047 | 5.302 | 5.676 | 4.996 | 4.974 | 5.111 | 4.980 |
| 6h | 13.584 | 12.815 | 12.515 | 12.423 | 12.932 | 12.687 | 12.462 | 12.397 | 12.429 | 12.389 |
| 24h | 16.040 | 15.703 | 15.562 | 15.480 | 15.891 | 15.562 | 15.513 | 15.445 | 15.452 | 15.458 |
| 7d | 13.534 | 13.106 | 13.080 | 13.012 | 13.249 | 13.187 | 12.997 | 12.987 | 12.978 | 13.002 |
| 30d | 15.360 | 14.884 | 14.833 | 14.770 | 15.031 | 14.953 | 14.752 | 14.718 | 14.716 | 14.744 |

## Next candle

- candle starting 2026-10-02 23:53 UTC, last close 2668.83
- P(up) 0.5192, return quantiles (bp): {'05': -3.66, '10': -2.673, '25': -1.043, '40': -0.262, '50': 0.06, '60': 0.525, '75': 1.125, '90': 2.492, '95': 3.457}
- changepoint probability 0.0127, regime age 133.8 min
- agent weights: empirical 0.003, ewma 0.045, garch 0.121, har 0.260, bocpd 0.015, hmm 0.071, online_qr 0.184, lgbm 0.301

## Learning log

- 2026-09-30 22:49 UTC: {"garch": {"alpha": 0.0806, "beta": 0.9066}, "hmm": {"sd_bp": [2.34, 4.92, 11.18], "stay": [0.963, 0.967, 0.949]}}
- 2026-10-01 10:49 UTC: {"garch": {"alpha": 0.078, "beta": 0.9062}, "hmm": {"sd_bp": [2.67, 5.06, 11.24], "stay": [0.948, 0.96, 0.953]}}
- 2026-10-01 22:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8986}, "hmm": {"sd_bp": [2.92, 5.28, 11.17], "stay": [0.943, 0.952, 0.951]}, "lgbm": {"challenger_loss": 0.25503, "champion_loss": 0.25511, "promoted": true}}
- 2026-10-02 10:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8964}, "hmm": {"sd_bp": [3.09, 5.46, 12.16], "stay": [0.948, 0.95, 0.933]}}
- 2026-10-02 22:49 UTC: {"garch": {"alpha": 0.1051, "beta": 0.8596}, "hmm": {"sd_bp": [3.17, 5.67, 12.93], "stay": [0.957, 0.947, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.67, 12.93], current probabilities: [0.943, 0.056, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 00:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.34, 'l_abs': 0.708, 'l_hi': 0.781, 'l_lo': 0.736, 'b05': 0.711, 'b25': 0.707, 'b75': 0.684, 'b95': 0.709}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.237, 1.458, 1.621, 1.816]}
- calibration offsets (in sigma): {'05': 0.0715, '10': 0.083, '25': 0.1475, '40': 0.092, '50': 0.025, '60': 0.008, '75': -0.1175, '90': -0.173, '95': -0.1715}
