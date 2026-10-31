# ETH-USD 60s candle generator - report

- generated: 2026-10-31 12:50 UTC
- last closed candle: 2026-10-31 12:50 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.525 (672) [0.493, 0.564] | 0.520 (2877) [0.501, 0.539] | 0.516 (5658) [0.502, 0.529] | 0.521 (2686) [0.500, 0.541] | 0.451 (51) | 0.500 | flat -0.013 (noise 0.030) |
| colour_clear | 0.537 (771) | 0.538 (5578) [0.532, 0.544] | 0.541 (23615) [0.534, 0.547] | 0.519 (46326) [0.513, 0.525] | 0.545 (22088) [0.540, 0.549] | 0.551 (403) | 0.500 | flat -0.018 (noise 0.009) |
| colour_confident | 0.590 (78) | 0.592 (1175) [0.583, 0.602] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.583 (84) | 0.500 | flat -0.013 (noise 0.020) |
| colour_next | 0.532 (1435) | 0.525 (10026) [0.520, 0.528] | 0.527 (42871) [0.523, 0.531] | 0.514 (84351) [0.510, 0.518] | 0.529 (40002) [0.525, 0.533] | 0.537 (764) | 0.500 | flat -0.013 (noise 0.007) |
| colour_path | 0.503 (20090) | 0.502 (140364) [0.500, 0.504] | 0.501 (600194) [0.499, 0.502] | 0.501 (1180914) [0.500, 0.502] | 0.501 (560028) [0.499, 0.502] | 0.500 (10696) | 0.500 | flat +0.003 (noise 0.002) |
| colour_strong | 0.538 (13) | 0.596 (369) [0.574, 0.625] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.645 (31) | 0.500 | flat -0.046 (noise 0.039) |
| reversal_k13_next | 0.283 (53) | 0.317 (391) [0.282, 0.359] | 0.315 (2003) [0.303, 0.327] | 0.308 (3946) [0.297, 0.319] | 0.317 (1841) [0.306, 0.329] | 0.367 (30) | 0.077 | flat +0.003 (noise 0.032) |
| reversal_k13_now | 0.597 (57) | 0.575 (419) [0.531, 0.618] | 0.567 (1653) [0.547, 0.587] | 0.572 (3019) [0.558, 0.587] | 0.564 (1547) [0.543, 0.587] | 0.676 (34) | 0.077 | flat +0.050 (noise 0.035) |
| reversal_k3_next | 0.595 (116) | 0.591 (726) [0.583, 0.599] | 0.583 (2939) [0.571, 0.595] | 0.584 (5234) [0.575, 0.594] | 0.582 (2794) [0.570, 0.593] | 0.568 (88) | 0.293 | flat +0.005 (noise 0.025) |
| reversal_k3_now | 0.933 (45) | 0.952 (393) [0.924, 0.977] | 0.936 (1731) [0.926, 0.946] | 0.939 (3367) [0.933, 0.946] | 0.936 (1604) [0.925, 0.947] | 0.950 (40) | 0.293 | flat +0.022 (noise 0.021) |
| reversal_k5_next | 0.568 (37) | 0.507 (580) [0.495, 0.524] | 0.471 (3038) [0.457, 0.485] | 0.479 (4761) [0.467, 0.492] | 0.469 (2771) [0.455, 0.484] | 0.543 (35) | 0.187 | flat +0.051 (noise 0.026) |
| reversal_k5_now | 0.780 (41) | 0.830 (400) [0.817, 0.839] | 0.824 (1619) [0.812, 0.835] | 0.830 (3116) [0.820, 0.840] | 0.822 (1505) [0.810, 0.833] | 0.833 (36) | 0.187 | flat +0.017 (noise 0.028) |
| reversal_k8_next | 0.402 (92) | 0.394 (703) [0.375, 0.412] | 0.386 (2799) [0.374, 0.398] | 0.390 (4804) [0.379, 0.400] | 0.384 (2698) [0.372, 0.397] | 0.469 (64) | 0.121 | flat +0.017 (noise 0.025) |
| reversal_k8_now | 0.614 (44) | 0.697 (376) [0.643, 0.740] | 0.689 (1571) [0.668, 0.709] | 0.701 (3060) [0.685, 0.717] | 0.687 (1473) [0.664, 0.709] | 0.758 (33) | 0.121 | flat +0.037 (noise 0.040) |
| overall | 0.506 (22106) | 0.506 (155050) [0.504, 0.508] | 0.504 (663295) [0.503, 0.506] | 0.503 (1302230) [0.502, 0.504] | 0.504 (618949) [0.503, 0.506] | 0.506 (11871) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08118, 0.1248] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5253, 'levels': [{'threshold': 0.08118, 'calls_per_day': 142.7, 'win_rate': 0.6006}, {'threshold': 0.1248, 'calls_per_day': 36.2, 'win_rate': 0.6118}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 39624, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15137 | 0.338 | 0.522 (14912) | 0.580 (2013) | 0.756 (2616) |
| volatility: normal | 15136 | 0.366 | 0.532 (15067) | 0.613 (1426) | 0.751 (2247) |
| volatility: wild | 15137 | 0.381 | 0.525 (15094) | 0.632 (744) | 0.767 (2044) |
| session: Asia 00-08 | 15360 | 0.360 | 0.532 (15259) | 0.602 (1492) | 0.763 (2306) |
| session: Europe 08-13 | 9590 | 0.356 | 0.530 (9500) | 0.594 (1058) | 0.750 (1571) |
| session: US 13-21 | 14880 | 0.370 | 0.523 (14788) | 0.601 (1055) | 0.762 (2172) |
| session: late 21-24 | 5580 | 0.352 | 0.514 (5526) | 0.609 (578) | 0.749 (858) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.356 | 0.312 | 0.275 | 0.275 | 0.600 | 0.303 | 0.409 | 1.016 |
| 6h | 360 | 0.312 | 0.302 | 0.227 | 0.215 | 0.545 | 0.249 | 0.375 | 1.408 |
| 24h | 1440 | 0.353 | 0.346 | 0.266 | 0.291 | 0.538 | 0.263 | 0.444 | 0.994 |
| 7d | 10080 | 0.366 | 0.359 | 0.283 | 0.313 | 0.525 | 0.262 | 0.469 | 1.242 |
| 30d | 43200 | 0.361 | 0.354 | 0.276 | 0.305 | 0.528 | 0.260 | 0.463 | 1.275 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.356 / 0.600 / 0.883; 2: 0.311 / 0.400 / 0.933; 3: 0.325 / 0.500 / 0.917; 4: 0.311 / 0.483 / 0.850; 5: 0.339 / 0.567 / 0.750; 6: 0.298 / 0.400 / 0.717; 7: 0.322 / 0.500 / 0.750; 8: 0.322 / 0.533 / 0.783; 9: 0.316 / 0.583 / 0.817; 10: 0.317 / 0.517 / 0.817; 11: 0.310 / 0.517 / 0.817; 12: 0.313 / 0.533 / 0.833; 13: 0.335 / 0.567 / 0.833; 14: 0.310 / 0.483 / 0.767; 15: 0.301 / 0.500 / 0.733
- 6h: 1: 0.312 / 0.545 / 0.867; 2: 0.306 / 0.517 / 0.944; 3: 0.287 / 0.466 / 0.931; 4: 0.301 / 0.545 / 0.894; 5: 0.297 / 0.517 / 0.847; 6: 0.276 / 0.460 / 0.828; 7: 0.302 / 0.506 / 0.833; 8: 0.295 / 0.523 / 0.833; 9: 0.297 / 0.514 / 0.828; 10: 0.292 / 0.463 / 0.842; 11: 0.286 / 0.500 / 0.819; 12: 0.292 / 0.458 / 0.831; 13: 0.293 / 0.508 / 0.856; 14: 0.289 / 0.477 / 0.803; 15: 0.295 / 0.497 / 0.772
- 24h: 1: 0.353 / 0.538 / 0.886; 2: 0.343 / 0.501 / 0.906; 3: 0.343 / 0.496 / 0.908; 4: 0.342 / 0.510 / 0.899; 5: 0.339 / 0.509 / 0.892; 6: 0.332 / 0.484 / 0.888; 7: 0.340 / 0.496 / 0.889; 8: 0.338 / 0.514 / 0.892; 9: 0.341 / 0.513 / 0.891; 10: 0.338 / 0.492 / 0.892; 11: 0.333 / 0.483 / 0.886; 12: 0.340 / 0.502 / 0.889; 13: 0.341 / 0.506 / 0.896; 14: 0.337 / 0.494 / 0.885; 15: 0.343 / 0.519 / 0.881
- 7d: 1: 0.366 / 0.525 / 0.897; 2: 0.354 / 0.491 / 0.901; 3: 0.356 / 0.506 / 0.900; 4: 0.355 / 0.505 / 0.900; 5: 0.353 / 0.506 / 0.899; 6: 0.350 / 0.501 / 0.898; 7: 0.354 / 0.503 / 0.898; 8: 0.352 / 0.507 / 0.899; 9: 0.352 / 0.500 / 0.898; 10: 0.353 / 0.504 / 0.899; 11: 0.350 / 0.500 / 0.898; 12: 0.352 / 0.504 / 0.899; 13: 0.350 / 0.500 / 0.900; 14: 0.351 / 0.502 / 0.899; 15: 0.349 / 0.496 / 0.898
- 30d: 1: 0.361 / 0.528 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.508 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.502 / 0.900; 6: 0.347 / 0.498 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.347 / 0.502 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.899; 12: 0.347 / 0.503 / 0.899; 13: 0.346 / 0.501 / 0.899; 14: 0.345 / 0.500 / 0.899; 15: 0.345 / 0.498 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.205 (body 0.164, range 0.245); 'price stays where it was' would score 0.171; colour right 0.550; typical miss of the close 2.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.104 (body 0.074, range 0.134); 'price stays where it was' would score 0.112; colour right 0.511; typical miss of the close 4.5 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.113 (body 0.074, range 0.152); 'price stays where it was' would score 0.120; colour right 0.522; typical miss of the close 7.4 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.127 (body 0.086, range 0.168); 'price stays where it was' would score 0.133; colour right 0.500; typical miss of the close 9.0 bp; chain ended on the right side 0.521 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.9 bp; chain ended on the right side 0.520 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.0; 2: 0.200 / 4.6; 3: 0.168 / 6.1; 4: 0.132 / 6.6; 5: 0.126 / 7.3; 6: 0.113 / 7.7; 7: 0.111 / 8.1; 8: 0.098 / 8.6; 9: 0.089 / 8.7; 10: 0.088 / 9.3; 11: 0.085 / 9.7; 12: 0.076 / 10.1; 13: 0.068 / 10.2; 14: 0.070 / 10.6; 15: 0.062 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 128684, probability skill vs chance 0.233, widened contest next: False
  - now: threshold 0.8339, hit rate recent 0.9561 / long run 0.9442
    - 6h: 20 calls (81 a day), hit rate 0.950, chance 0.315, naive rule 0.551, lift 3.01x
    - 24h: 63 calls (63 a day), hit rate 0.952, chance 0.301, naive rule 0.529, lift 3.16x
    - 7d: 402 calls (57 a day), hit rate 0.950, chance 0.293, naive rule 0.497, lift 3.24x
    - 30d: 1729 calls (58 a day), hit rate 0.937, chance 0.294, naive rule 0.494, lift 3.19x
  - next: threshold 0.5294, hit rate recent 0.5847 / long run 0.5876
    - 6h: 39 calls (158 a day), hit rate 0.590, chance 0.315, lift 1.87x
    - 24h: 150 calls (151 a day), hit rate 0.593, chance 0.301, lift 1.97x
    - 7d: 774 calls (111 a day), hit rate 0.584, chance 0.293, lift 1.99x
    - 30d: 2976 calls (99 a day), hit rate 0.582, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.497; 0.35: 536, 0.522; 0.40: 475, 0.579; 0.45: 406, 0.650; 0.50: 355, 0.700; 0.55: 310, 0.743; 0.60: 262, 0.788; 0.65: 220, 0.813; 0.70: 173, 0.845; 0.75: 136, 0.879; 0.80: 92, 0.914; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.428; 0.35: 501, 0.464; 0.40: 406, 0.497; 0.45: 309, 0.532; 0.50: 200, 0.569; 0.55: 89, 0.571; 0.60: 13, 0.649; 0.65: 1, 0.630
- **K=5**: model 1792540800, labels learned 128682, probability skill vs chance 0.2314, widened contest next: False
  - now: threshold 0.6783, hit rate recent 0.8246 / long run 0.8249
    - 6h: 18 calls (73 a day), hit rate 0.778, chance 0.210, naive rule 0.479, lift 3.71x
    - 24h: 52 calls (52 a day), hit rate 0.846, chance 0.194, naive rule 0.445, lift 4.36x
    - 7d: 407 calls (58 a day), hit rate 0.828, chance 0.186, naive rule 0.411, lift 4.45x
    - 30d: 1623 calls (54 a day), hit rate 0.823, chance 0.188, naive rule 0.405, lift 4.37x
  - next: threshold 0.4553, hit rate recent 0.5357 / long run 0.4975
    - 6h: 15 calls (61 a day), hit rate 0.467, chance 0.210, lift 2.23x
    - 24h: 57 calls (57 a day), hit rate 0.544, chance 0.194, lift 2.80x
    - 7d: 546 calls (78 a day), hit rate 0.515, chance 0.186, lift 2.77x
    - 30d: 2993 calls (100 a day), hit rate 0.471, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.493; 0.40: 278, 0.567; 0.45: 227, 0.620; 0.50: 180, 0.668; 0.55: 142, 0.707; 0.60: 108, 0.753; 0.65: 76, 0.790; 0.70: 51, 0.827; 0.75: 29, 0.871; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.389; 0.35: 255, 0.421; 0.40: 159, 0.458; 0.45: 68, 0.478; 0.50: 13, 0.495; 0.55: 1, 0.486
- **K=8**: model 1793059200, labels learned 128679, probability skill vs chance 0.2167, widened contest next: False
  - now: threshold 0.5645, hit rate recent 0.7255 / long run 0.692
    - 6h: 16 calls (66 a day), hit rate 0.750, chance 0.129, naive rule 0.375, lift 5.83x
    - 24h: 53 calls (53 a day), hit rate 0.736, chance 0.133, naive rule 0.395, lift 5.55x
    - 7d: 377 calls (54 a day), hit rate 0.698, chance 0.123, naive rule 0.348, lift 5.68x
    - 30d: 1580 calls (53 a day), hit rate 0.691, chance 0.121, naive rule 0.334, lift 5.69x
  - next: threshold 0.352, hit rate recent 0.4579 / long run 0.4001
    - 6h: 27 calls (111 a day), hit rate 0.444, chance 0.129, lift 3.46x
    - 24h: 109 calls (110 a day), hit rate 0.468, chance 0.133, lift 3.53x
    - 7d: 717 calls (103 a day), hit rate 0.404, chance 0.123, lift 3.29x
    - 30d: 2831 calls (94 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 189, 0.499; 0.40: 147, 0.547; 0.45: 112, 0.595; 0.50: 84, 0.639; 0.55: 61, 0.677; 0.60: 41, 0.713; 0.65: 23, 0.782; 0.70: 11, 0.814; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.359; 0.35: 92, 0.385; 0.40: 29, 0.408; 0.45: 6, 0.435; 0.50: 1, 0.643
- **K=13**: model 1793059200, labels learned 128674, probability skill vs chance 0.1976, widened contest next: False
  - now: threshold 0.4124, hit rate recent 0.6302 / long run 0.5691
    - 6h: 16 calls (67 a day), hit rate 0.562, chance 0.083, naive rule 0.296, lift 6.81x
    - 24h: 57 calls (58 a day), hit rate 0.667, chance 0.082, naive rule 0.326, lift 8.15x
    - 7d: 423 calls (61 a day), hit rate 0.577, chance 0.078, naive rule 0.288, lift 7.43x
    - 30d: 1656 calls (55 a day), hit rate 0.569, chance 0.077, naive rule 0.278, lift 7.36x
  - next: threshold 0.2929, hit rate recent 0.3181 / long run 0.3153
    - 6h: 13 calls (54 a day), hit rate 0.154, chance 0.083, lift 1.86x
    - 24h: 56 calls (57 a day), hit rate 0.339, chance 0.082, lift 4.15x
    - 7d: 387 calls (55 a day), hit rate 0.326, chance 0.078, lift 4.20x
    - 30d: 1980 calls (66 a day), hit rate 0.314, chance 0.077, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.443; 0.35: 91, 0.496; 0.40: 64, 0.553; 0.45: 43, 0.599; 0.50: 28, 0.656; 0.55: 17, 0.698; 0.60: 9, 0.740; 0.65: 2, 0.726; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.326; 0.35: 14, 0.351; 0.40: 3, 0.439; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.212 | 9.02% | 0.850 | 0.383 | 0.252 | 0.467 | 0.322 |
| 6h | 6.959 | 17.82% | 0.881 | 0.517 | 0.248 | 0.554 | 0.321 |
| 24h | 14.396 | 8.69% | 0.897 | 0.513 | 0.250 | 0.515 | 0.790 |
| 7d | 16.424 | 5.09% | 0.899 | 0.501 | 0.250 | 0.502 | 0.734 |
| 30d | 14.206 | 4.47% | 0.900 | 0.500 | 0.251 | 0.497 | 0.693 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.026 | 8.216 | 8.293 | 8.297 | 8.360 | 8.372 | 8.177 | 8.119 | 8.153 | 8.212 |
| 6h | 8.469 | 7.020 | 7.291 | 7.017 | 7.209 | 7.558 | 6.958 | 6.921 | 6.950 | 6.959 |
| 24h | 15.767 | 14.510 | 14.607 | 14.414 | 14.677 | 14.798 | 14.373 | 14.349 | 14.369 | 14.396 |
| 7d | 17.305 | 16.625 | 16.546 | 16.464 | 16.763 | 16.683 | 16.412 | 16.378 | 16.393 | 16.424 |
| 30d | 14.870 | 14.357 | 14.300 | 14.233 | 14.472 | 14.414 | 14.201 | 14.178 | 14.180 | 14.206 |

## Next candle

- candle starting 2026-10-31 12:50 UTC, last close 2249.2
- P(up) 0.5056, return quantiles (bp): {'05': -4.989, '10': -3.782, '25': -1.693, '40': -0.462, '50': 0.024, '60': 0.575, '75': 1.725, '90': 3.739, '95': 5.049}
- changepoint probability 0.0526, regime age 271.4 min
- agent weights: empirical 0.003, ewma 0.148, garch 0.039, har 0.168, bocpd 0.042, hmm 0.010, online_qr 0.256, lgbm 0.334

## Learning log

- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- HMM volatility states (sd, bp per minute): [3.53, 7.0, 20.69], current probabilities: [0.942, 0.057, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-31 13:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.414, 'l_abs': 0.606, 'l_hi': 0.709, 'l_lo': 0.698, 'b05': 0.651, 'b25': 0.656, 'b75': 0.569, 'b95': 0.652}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.2, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.375, 1.722, 1.992, 2.726, 3.441, 3.725, 3.833, 4.24, 4.134, 4.998, 4.828, 4.291, 5.787, 6.633]}
- calibration offsets (in sigma): {'05': 0.0645, '10': 0.019, '25': 0.0925, '40': 0.096, '50': 0.035, '60': -0.006, '75': -0.0325, '90': 0.001, '95': -0.0245}
