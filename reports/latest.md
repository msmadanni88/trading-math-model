# ETH-USD 60s candle generator - report

- generated: 2026-10-03 01:30 UTC
- last closed candle: 2026-10-03 01:30 UTC (staleness 0.0 min)

## Goal keeper alerts

- none: on track

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.318 | 0.357 | 0.202 | 0.202 | 0.424 | 0.189 | 0.446 | 1.190 |
| 6h | 360 | 0.329 | 0.335 | 0.251 | 0.276 | 0.475 | 0.203 | 0.455 | 1.439 |
| 24h | 1440 | 0.359 | 0.363 | 0.284 | 0.314 | 0.495 | 0.232 | 0.485 | 1.377 |
| 7d | 10080 | 0.358 | 0.357 | 0.286 | 0.314 | 0.505 | 0.243 | 0.474 | 1.327 |
| 30d | 43200 | 0.357 | 0.357 | 0.281 | 0.311 | 0.500 | 0.245 | 0.469 | 1.271 |

## Candles generated further ahead (score / colour right / 90% cone held the close)

- 1h: 1 min ahead 0.318 / 0.424 / -; 2 min ahead 0.316 / 0.356 / 0.850; 3 min ahead 0.317 / 0.407 / 0.783; 4 min ahead 0.309 / 0.390 / 0.717; 5 min ahead 0.322 / 0.373 / 0.750
- 6h: 1 min ahead 0.329 / 0.475 / -; 2 min ahead 0.325 / 0.466 / 0.883; 3 min ahead 0.335 / 0.477 / 0.872; 4 min ahead 0.329 / 0.483 / 0.881; 5 min ahead 0.328 / 0.486 / 0.881
- 24h: 1 min ahead 0.359 / 0.495 / -; 2 min ahead 0.356 / 0.487 / 0.898; 3 min ahead 0.358 / 0.512 / 0.892; 4 min ahead 0.355 / 0.498 / 0.890; 5 min ahead 0.353 / 0.502 / 0.891
- 7d: 1 min ahead 0.358 / 0.505 / -; 2 min ahead 0.358 / 0.510 / 0.900; 3 min ahead 0.357 / 0.511 / 0.900; 4 min ahead 0.354 / 0.506 / 0.899; 5 min ahead 0.353 / 0.509 / 0.900
- 30d: 1 min ahead 0.357 / 0.500 / -; 2 min ahead 0.357 / 0.509 / 0.900; 3 min ahead 0.355 / 0.506 / 0.900; 4 min ahead 0.354 / 0.504 / 0.900; 5 min ahead 0.353 / 0.503 / 0.900

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.959 | 8.41% | 0.867 | 0.383 | 0.236 | 0.644 | 0.245 |
| 6h | 8.037 | 11.40% | 0.922 | 0.567 | 0.248 | 0.517 | 0.484 |
| 24h | 15.227 | 4.09% | 0.910 | 0.519 | 0.250 | 0.505 | 0.576 |
| 7d | 12.982 | 3.99% | 0.901 | 0.502 | 0.251 | 0.494 | 0.660 |
| 30d | 14.726 | 4.03% | 0.901 | 0.501 | 0.250 | 0.499 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.783 | 9.126 | 9.231 | 8.926 | 9.440 | 9.216 | 9.097 | 8.981 | 8.993 | 8.959 |
| 6h | 9.072 | 8.281 | 8.220 | 8.055 | 8.296 | 8.258 | 8.165 | 8.099 | 8.099 | 8.037 |
| 24h | 15.876 | 15.477 | 15.351 | 15.249 | 15.661 | 15.345 | 15.291 | 15.217 | 15.225 | 15.227 |
| 7d | 13.521 | 13.086 | 13.062 | 12.992 | 13.230 | 13.169 | 12.977 | 12.966 | 12.959 | 12.982 |
| 30d | 15.344 | 14.866 | 14.816 | 14.752 | 15.013 | 14.936 | 14.734 | 14.700 | 14.698 | 14.726 |

## Next candle

- candle starting 2026-10-03 01:30 UTC, last close 2678.78
- P(up) 0.5972, return quantiles (bp): {'05': -5.092, '10': -3.629, '25': -1.345, '40': 0.021, '50': 0.249, '60': 0.708, '75': 1.711, '90': 3.493, '95': 4.918}
- changepoint probability 0.3244, regime age 17.1 min
- agent weights: empirical 0.003, ewma 0.055, garch 0.093, har 0.281, bocpd 0.016, hmm 0.058, online_qr 0.185, lgbm 0.309

## Learning log

- 2026-09-30 22:49 UTC: {"garch": {"alpha": 0.0806, "beta": 0.9066}, "hmm": {"sd_bp": [2.34, 4.92, 11.18], "stay": [0.963, 0.967, 0.949]}}
- 2026-10-01 10:49 UTC: {"garch": {"alpha": 0.078, "beta": 0.9062}, "hmm": {"sd_bp": [2.67, 5.06, 11.24], "stay": [0.948, 0.96, 0.953]}}
- 2026-10-01 22:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8986}, "hmm": {"sd_bp": [2.92, 5.28, 11.17], "stay": [0.943, 0.952, 0.951]}, "lgbm": {"challenger_loss": 0.25503, "champion_loss": 0.25511, "promoted": true}}
- 2026-10-02 10:49 UTC: {"garch": {"alpha": 0.0819, "beta": 0.8964}, "hmm": {"sd_bp": [3.09, 5.46, 12.16], "stay": [0.948, 0.95, 0.933]}}
- 2026-10-02 22:49 UTC: {"garch": {"alpha": 0.1051, "beta": 0.8596}, "hmm": {"sd_bp": [3.17, 5.67, 12.93], "stay": [0.957, 0.947, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.67, 12.93], current probabilities: [0.914, 0.084, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 01:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.308, 'l_abs': 0.691, 'l_hi': 0.769, 'l_lo': 0.712, 'b05': 0.692, 'b25': 0.689, 'b75': 0.669, 'b95': 0.704}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6]], 'cone_width': [1.46, 1.98, 2.338, 2.567]}
- calibration offsets (in sigma): {'05': 0.06, '10': 0.1, '25': 0.17, '40': 0.19, '50': 0.08, '60': 0.01, '75': -0.07, '90': -0.14, '95': -0.14}
