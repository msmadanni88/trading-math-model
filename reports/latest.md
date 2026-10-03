# ETH-USD 60s candle generator - report

- generated: 2026-10-03 07:04 UTC
- last closed candle: 2026-10-03 07:04 UTC (staleness 0.2 min)

## Goal keeper alerts

- none: on track

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site dir acc | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.328 | 0.329 | 0.227 | 0.227 | 0.483 | 0.235 | 0.421 | 0.985 |
| 6h | 360 | 0.320 | 0.321 | 0.254 | 0.269 | 0.483 | 0.223 | 0.417 | 1.211 |
| 24h | 1440 | 0.348 | 0.352 | 0.277 | 0.305 | 0.495 | 0.232 | 0.465 | 1.439 |
| 7d | 10080 | 0.358 | 0.358 | 0.286 | 0.314 | 0.503 | 0.243 | 0.473 | 1.335 |
| 30d | 43200 | 0.357 | 0.357 | 0.280 | 0.311 | 0.500 | 0.245 | 0.468 | 1.273 |

## Candles generated further ahead (score / colour right / 90% cone held the close)

- 1h: 1 min ahead 0.328 / 0.483 / -; 2 min ahead 0.346 / 0.533 / 0.917; 3 min ahead 0.348 / 0.567 / 0.917; 4 min ahead 0.363 / 0.583 / 0.933; 5 min ahead 0.341 / 0.583 / 0.967
- 6h: 1 min ahead 0.320 / 0.483 / -; 2 min ahead 0.334 / 0.480 / 0.906; 3 min ahead 0.329 / 0.477 / 0.917; 4 min ahead 0.337 / 0.500 / 0.922; 5 min ahead 0.330 / 0.506 / 0.939
- 24h: 1 min ahead 0.348 / 0.495 / -; 2 min ahead 0.351 / 0.491 / 0.901; 3 min ahead 0.349 / 0.497 / 0.898; 4 min ahead 0.349 / 0.496 / 0.899; 5 min ahead 0.346 / 0.500 / 0.903
- 7d: 1 min ahead 0.358 / 0.503 / -; 2 min ahead 0.358 / 0.509 / 0.900; 3 min ahead 0.357 / 0.511 / 0.900; 4 min ahead 0.355 / 0.506 / 0.900; 5 min ahead 0.353 / 0.510 / 0.901
- 30d: 1 min ahead 0.357 / 0.500 / -; 2 min ahead 0.357 / 0.509 / 0.900; 3 min ahead 0.355 / 0.506 / 0.900; 4 min ahead 0.353 / 0.504 / 0.900; 5 min ahead 0.353 / 0.503 / 0.900

## The fixed record: candles locked 5 minutes ahead, compared at their real price level

- 1h: match 0.113 (body 0.080, range 0.146), typical miss of the close 3.7 bp, n=60
- 6h: match 0.089 (body 0.059, range 0.120), typical miss of the close 4.7 bp, n=360
- 24h: match 0.088 (body 0.056, range 0.121), typical miss of the close 9.6 bp, n=1440
- 7d: match 0.086 (body 0.054, range 0.118), typical miss of the close 10.1 bp, n=10080
- 30d: match 0.092 (body 0.058, range 0.126), typical miss of the close 10.5 bp, n=43200

## Reversal agent

- a swing point = highest high / lowest low of 5 candles on each side; a call is a hit if one forms within one candle of the minute it names
- model mix: {'base': 0.01, 'logit': 0.01, 'trees': 0.98}, probability skill vs chance (Brier): 0.1083, call threshold 0.45, labels learned 88013
- 6h: 29 calls (15 tops, 14 bottoms), hit rate 0.414, chance 0.200, naive rule 0.430 on 172 calls, lift 2.07x
- 24h: 128 calls (63 tops, 65 bottoms), hit rate 0.438, chance 0.194, naive rule 0.421 on 710 calls, lift 2.25x
- 7d: 838 calls (441 tops, 397 bottoms), hit rate 0.451, chance 0.187, naive rule 0.395 on 5044 calls, lift 2.41x
- 30d: 3711 calls (1912 tops, 1799 bottoms), hit rate 0.456, chance 0.186, naive rule 0.391 on 21625 calls, lift 2.45x

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.152 | 13.88% | 0.883 | 0.433 | 0.251 | 0.517 | 0.238 |
| 6h | 6.357 | 15.81% | 0.892 | 0.453 | 0.252 | 0.469 | 0.299 |
| 24h | 13.005 | 6.50% | 0.910 | 0.503 | 0.250 | 0.494 | 0.641 |
| 7d | 12.957 | 4.04% | 0.901 | 0.500 | 0.251 | 0.497 | 0.661 |
| 30d | 14.663 | 4.09% | 0.900 | 0.500 | 0.251 | 0.500 | 0.675 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.143 | 6.221 | 6.376 | 6.159 | 6.309 | 6.581 | 6.116 | 6.135 | 6.119 | 6.152 |
| 6h | 7.551 | 6.395 | 6.618 | 6.373 | 6.626 | 6.782 | 6.346 | 6.322 | 6.337 | 6.357 |
| 24h | 13.909 | 13.218 | 13.160 | 13.019 | 13.378 | 13.233 | 13.073 | 13.017 | 13.007 | 13.005 |
| 7d | 13.502 | 13.060 | 13.036 | 12.964 | 13.206 | 13.133 | 12.949 | 12.943 | 12.933 | 12.957 |
| 30d | 15.288 | 14.801 | 14.752 | 14.689 | 14.949 | 14.875 | 14.671 | 14.637 | 14.636 | 14.663 |

## Next candle

- candle starting 2026-10-03 07:04 UTC, last close 2679.96
- P(up) 0.4846, return quantiles (bp): {'05': -3.494, '10': -2.507, '25': -1.119, '40': -0.433, '50': -0.083, '60': 0.465, '75': 1.266, '90': 2.574, '95': 3.421}
- changepoint probability 0.1003, regime age 45.4 min
- agent weights: empirical 0.003, ewma 0.104, garch 0.051, har 0.249, bocpd 0.024, hmm 0.017, online_qr 0.242, lgbm 0.309

## Learning log

- 2026-10-01 00:00 UTC: {"garch": {"alpha": 0.0515, "beta": 0.9433}, "hmm": {"sd_bp": [2.41, 4.95, 11.19], "stay": [0.96, 0.965, 0.949]}}
- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal": {"challenger_loss": 0.424, "chance_loss": 0.47934, "champion_loss": 0.42129, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- HMM volatility states (sd, bp per minute): [3.13, 5.67, 13.01], current probabilities: [0.921, 0.078, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 07:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.222, 'l_abs': 0.667, 'l_hi': 0.776, 'l_lo': 0.738, 'b05': 0.672, 'b25': 0.723, 'b75': 0.68, 'b95': 0.693}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6]], 'cone_width': [1.337, 1.742, 2.141, 2.127]}
- calibration offsets (in sigma): {'05': 0.0715, '10': 0.083, '25': 0.0675, '40': 0.002, '50': -0.035, '60': 0.008, '75': -0.0075, '90': -0.053, '95': -0.0915}
