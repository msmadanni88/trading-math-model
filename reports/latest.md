# ETH-USD 60s candle generator - report

- generated: 2026-10-31 23:43 UTC
- last closed candle: 2026-10-31 23:43 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.525 (672) [0.493, 0.564] | 0.520 (2877) [0.501, 0.539] | 0.516 (5658) [0.502, 0.529] | 0.521 (2686) [0.500, 0.541] | 0.511 (94) | 0.500 | flat -0.013 (noise 0.030) |
| colour_clear | 0.537 (771) | 0.538 (5578) [0.532, 0.544] | 0.541 (23615) [0.534, 0.547] | 0.519 (46326) [0.513, 0.525] | 0.545 (22088) [0.540, 0.549] | 0.568 (717) | 0.500 | flat -0.018 (noise 0.009) |
| colour_confident | 0.590 (78) | 0.592 (1175) [0.583, 0.602] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.582 (184) | 0.500 | flat -0.013 (noise 0.020) |
| colour_next | 0.532 (1435) | 0.525 (10026) [0.520, 0.528] | 0.527 (42871) [0.523, 0.531] | 0.514 (84351) [0.510, 0.518] | 0.529 (40002) [0.525, 0.533] | 0.555 (1381) | 0.500 | flat -0.013 (noise 0.007) |
| colour_path | 0.503 (20090) | 0.502 (140364) [0.500, 0.504] | 0.501 (600194) [0.499, 0.502] | 0.501 (1180914) [0.500, 0.502] | 0.501 (560028) [0.499, 0.502] | 0.504 (19334) | 0.500 | flat +0.003 (noise 0.002) |
| colour_strong | 0.538 (13) | 0.596 (369) [0.574, 0.625] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.654 (52) | 0.500 | flat -0.046 (noise 0.039) |
| reversal_k13_next | 0.283 (53) | 0.317 (391) [0.282, 0.359] | 0.315 (2003) [0.303, 0.327] | 0.308 (3946) [0.297, 0.319] | 0.317 (1841) [0.306, 0.329] | 0.421 (57) | 0.077 | flat +0.003 (noise 0.032) |
| reversal_k13_now | 0.597 (57) | 0.575 (419) [0.531, 0.618] | 0.567 (1653) [0.547, 0.587] | 0.572 (3019) [0.558, 0.587] | 0.564 (1547) [0.543, 0.587] | 0.639 (61) | 0.077 | flat +0.050 (noise 0.035) |
| reversal_k3_next | 0.595 (116) | 0.591 (726) [0.583, 0.599] | 0.583 (2939) [0.571, 0.595] | 0.584 (5234) [0.575, 0.594] | 0.582 (2794) [0.570, 0.593] | 0.583 (156) | 0.293 | flat +0.005 (noise 0.025) |
| reversal_k3_now | 0.933 (45) | 0.952 (393) [0.924, 0.977] | 0.936 (1731) [0.926, 0.946] | 0.939 (3367) [0.933, 0.946] | 0.936 (1604) [0.925, 0.947] | 0.932 (74) | 0.293 | flat +0.022 (noise 0.021) |
| reversal_k5_next | 0.568 (37) | 0.507 (580) [0.495, 0.524] | 0.471 (3038) [0.457, 0.485] | 0.479 (4761) [0.467, 0.492] | 0.469 (2771) [0.455, 0.484] | 0.544 (68) | 0.187 | flat +0.051 (noise 0.026) |
| reversal_k5_now | 0.780 (41) | 0.830 (400) [0.817, 0.839] | 0.824 (1619) [0.812, 0.835] | 0.830 (3116) [0.820, 0.840] | 0.822 (1505) [0.810, 0.833] | 0.797 (64) | 0.187 | flat +0.017 (noise 0.028) |
| reversal_k8_next | 0.402 (92) | 0.394 (703) [0.375, 0.412] | 0.386 (2799) [0.374, 0.398] | 0.390 (4804) [0.379, 0.400] | 0.384 (2698) [0.372, 0.397] | 0.484 (95) | 0.121 | flat +0.017 (noise 0.025) |
| reversal_k8_now | 0.614 (44) | 0.697 (376) [0.643, 0.740] | 0.689 (1571) [0.668, 0.709] | 0.701 (3060) [0.685, 0.717] | 0.687 (1473) [0.664, 0.709] | 0.759 (58) | 0.121 | flat +0.037 (noise 0.040) |
| overall | 0.506 (22106) | 0.506 (155050) [0.504, 0.508] | 0.504 (663295) [0.503, 0.506] | 0.503 (1302230) [0.502, 0.504] | 0.504 (618949) [0.503, 0.506] | 0.511 (21442) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08123, 0.125] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.08123, 'calls_per_day': 144.1, 'win_rate': 0.5921}, {'threshold': 0.125, 'calls_per_day': 36.3, 'win_rate': 0.6055}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 40240, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15355 | 0.337 | 0.524 (15098) | 0.580 (2073) | 0.757 (2669) |
| volatility: normal | 15354 | 0.366 | 0.532 (15281) | 0.612 (1453) | 0.750 (2276) |
| volatility: wild | 15354 | 0.381 | 0.525 (15311) | 0.631 (757) | 0.769 (2076) |
| session: Asia 00-08 | 15360 | 0.360 | 0.532 (15259) | 0.602 (1492) | 0.763 (2306) |
| session: Europe 08-13 | 9600 | 0.356 | 0.530 (9510) | 0.594 (1059) | 0.750 (1577) |
| session: US 13-21 | 15360 | 0.369 | 0.525 (15237) | 0.600 (1127) | 0.761 (2270) |
| session: late 21-24 | 5743 | 0.350 | 0.514 (5684) | 0.607 (605) | 0.752 (868) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.287 | 0.296 | 0.230 | 0.230 | 0.448 | 0.166 | 0.409 | 1.535 |
| 6h | 360 | 0.310 | 0.297 | 0.218 | 0.237 | 0.587 | 0.254 | 0.366 | 1.352 |
| 24h | 1440 | 0.328 | 0.321 | 0.237 | 0.256 | 0.557 | 0.258 | 0.398 | 1.282 |
| 7d | 10080 | 0.363 | 0.356 | 0.280 | 0.310 | 0.529 | 0.262 | 0.464 | 1.264 |
| 30d | 43200 | 0.361 | 0.353 | 0.275 | 0.304 | 0.529 | 0.260 | 0.461 | 1.279 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.287 / 0.448 / 0.917; 2: 0.345 / 0.603 / 0.933; 3: 0.303 / 0.500 / 0.900; 4: 0.312 / 0.534 / 0.883; 5: 0.302 / 0.517 / 0.883; 6: 0.343 / 0.638 / 0.850; 7: 0.332 / 0.552 / 0.883; 8: 0.303 / 0.552 / 0.867; 9: 0.327 / 0.569 / 0.917; 10: 0.297 / 0.448 / 0.900; 11: 0.325 / 0.552 / 0.883; 12: 0.299 / 0.431 / 0.850; 13: 0.299 / 0.466 / 0.867; 14: 0.299 / 0.448 / 0.867; 15: 0.305 / 0.534 / 0.900
- 6h: 1: 0.310 / 0.587 / 0.889; 2: 0.285 / 0.473 / 0.919; 3: 0.284 / 0.515 / 0.889; 4: 0.285 / 0.506 / 0.908; 5: 0.288 / 0.539 / 0.903; 6: 0.291 / 0.512 / 0.906; 7: 0.278 / 0.470 / 0.928; 8: 0.280 / 0.509 / 0.908; 9: 0.293 / 0.557 / 0.914; 10: 0.274 / 0.497 / 0.897; 11: 0.286 / 0.527 / 0.914; 12: 0.279 / 0.488 / 0.911; 13: 0.285 / 0.506 / 0.917; 14: 0.273 / 0.470 / 0.917; 15: 0.287 / 0.527 / 0.922
- 24h: 1: 0.328 / 0.557 / 0.882; 2: 0.310 / 0.489 / 0.901; 3: 0.310 / 0.501 / 0.903; 4: 0.308 / 0.509 / 0.908; 5: 0.317 / 0.539 / 0.906; 6: 0.303 / 0.487 / 0.902; 7: 0.307 / 0.494 / 0.907; 8: 0.307 / 0.518 / 0.905; 9: 0.317 / 0.538 / 0.903; 10: 0.302 / 0.482 / 0.903; 11: 0.304 / 0.495 / 0.902; 12: 0.306 / 0.495 / 0.899; 13: 0.308 / 0.506 / 0.899; 14: 0.301 / 0.474 / 0.899; 15: 0.312 / 0.527 / 0.897
- 7d: 1: 0.363 / 0.529 / 0.896; 2: 0.350 / 0.491 / 0.901; 3: 0.353 / 0.506 / 0.901; 4: 0.351 / 0.505 / 0.901; 5: 0.351 / 0.508 / 0.900; 6: 0.348 / 0.503 / 0.901; 7: 0.350 / 0.500 / 0.901; 8: 0.349 / 0.508 / 0.901; 9: 0.350 / 0.505 / 0.901; 10: 0.349 / 0.503 / 0.901; 11: 0.346 / 0.500 / 0.902; 12: 0.348 / 0.503 / 0.902; 13: 0.347 / 0.500 / 0.902; 14: 0.347 / 0.501 / 0.902; 15: 0.347 / 0.498 / 0.901
- 30d: 1: 0.361 / 0.529 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.346 / 0.498 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.346 / 0.502 / 0.900; 9: 0.345 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.344 / 0.497 / 0.900; 12: 0.346 / 0.503 / 0.900; 13: 0.345 / 0.501 / 0.900; 14: 0.344 / 0.500 / 0.900; 15: 0.344 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.095 (body 0.077, range 0.114); 'price stays where it was' would score 0.122; colour right 0.310; typical miss of the close 5.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.105 (body 0.080, range 0.130); 'price stays where it was' would score 0.115; colour right 0.488; typical miss of the close 4.4 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.117 (body 0.085, range 0.149); 'price stays where it was' would score 0.121; colour right 0.517; typical miss of the close 4.6 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.127 (body 0.086, range 0.168); 'price stays where it was' would score 0.132; colour right 0.503; typical miss of the close 8.5 bp; chain ended on the right side 0.525 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.7 bp; chain ended on the right side 0.521 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.9; 2: 0.199 / 4.6; 3: 0.168 / 6.1; 4: 0.132 / 6.5; 5: 0.125 / 7.2; 6: 0.113 / 7.6; 7: 0.112 / 8.0; 8: 0.098 / 8.5; 9: 0.089 / 8.5; 10: 0.088 / 9.1; 11: 0.085 / 9.6; 12: 0.076 / 9.9; 13: 0.068 / 10.0; 14: 0.070 / 10.4; 15: 0.063 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 129337, probability skill vs chance 0.226, widened contest next: False
  - now: threshold 0.8341, hit rate recent 0.9402 / long run 0.9425
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.334, naive rule 0.597, lift 3.00x
    - 24h: 74 calls (74 a day), hit rate 0.932, chance 0.314, naive rule 0.533, lift 2.97x
    - 7d: 418 calls (60 a day), hit rate 0.945, chance 0.294, naive rule 0.498, lift 3.21x
    - 30d: 1733 calls (58 a day), hit rate 0.936, chance 0.295, naive rule 0.495, lift 3.18x
  - next: threshold 0.5299, hit rate recent 0.6071 / long run 0.5895
    - 6h: 36 calls (146 a day), hit rate 0.667, chance 0.334, lift 2.00x
    - 24h: 156 calls (157 a day), hit rate 0.583, chance 0.314, lift 1.86x
    - 7d: 828 calls (118 a day), hit rate 0.587, chance 0.294, lift 2.00x
    - 30d: 3010 calls (100 a day), hit rate 0.582, chance 0.295, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 535, 0.523; 0.40: 474, 0.580; 0.45: 405, 0.652; 0.50: 355, 0.701; 0.55: 309, 0.744; 0.60: 261, 0.789; 0.65: 219, 0.815; 0.70: 173, 0.846; 0.75: 136, 0.880; 0.80: 92, 0.913; 0.85: 47, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.428; 0.35: 501, 0.464; 0.40: 407, 0.497; 0.45: 309, 0.532; 0.50: 200, 0.569; 0.55: 89, 0.571; 0.60: 13, 0.644; 0.65: 1, 0.654
- **K=5**: model 1792540800, labels learned 129335, probability skill vs chance 0.2215, widened contest next: False
  - now: threshold 0.6782, hit rate recent 0.8047 / long run 0.8216
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.208, naive rule 0.481, lift 4.46x
    - 24h: 64 calls (64 a day), hit rate 0.797, chance 0.199, naive rule 0.431, lift 4.01x
    - 7d: 409 calls (58 a day), hit rate 0.826, chance 0.188, naive rule 0.410, lift 4.40x
    - 30d: 1629 calls (54 a day), hit rate 0.822, chance 0.188, naive rule 0.405, lift 4.37x
  - next: threshold 0.4521, hit rate recent 0.5484 / long run 0.5002
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.208, lift 3.30x
    - 24h: 68 calls (68 a day), hit rate 0.544, chance 0.199, lift 2.74x
    - 7d: 524 calls (75 a day), hit rate 0.519, chance 0.188, lift 2.77x
    - 30d: 2959 calls (99 a day), hit rate 0.471, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.494; 0.40: 278, 0.567; 0.45: 227, 0.620; 0.50: 180, 0.668; 0.55: 141, 0.707; 0.60: 108, 0.751; 0.65: 76, 0.790; 0.70: 51, 0.825; 0.75: 29, 0.870; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.388; 0.35: 255, 0.420; 0.40: 160, 0.457; 0.45: 68, 0.477; 0.50: 13, 0.492; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 129332, probability skill vs chance 0.2085, widened contest next: False
  - now: threshold 0.5644, hit rate recent 0.7434 / long run 0.6949
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.100, naive rule 0.274, lift 9.09x
    - 24h: 58 calls (58 a day), hit rate 0.759, chance 0.122, naive rule 0.339, lift 6.20x
    - 7d: 379 calls (54 a day), hit rate 0.704, chance 0.122, naive rule 0.342, lift 5.78x
    - 30d: 1583 calls (53 a day), hit rate 0.692, chance 0.121, naive rule 0.334, lift 5.71x
  - next: threshold 0.3596, hit rate recent 0.4891 / long run 0.406
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.100, lift 6.36x
    - 24h: 95 calls (96 a day), hit rate 0.484, chance 0.122, lift 3.96x
    - 7d: 713 calls (102 a day), hit rate 0.408, chance 0.122, lift 3.35x
    - 30d: 2841 calls (95 a day), hit rate 0.388, chance 0.121, lift 3.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 244, 0.433; 0.35: 189, 0.501; 0.40: 147, 0.548; 0.45: 112, 0.595; 0.50: 84, 0.639; 0.55: 61, 0.679; 0.60: 41, 0.715; 0.65: 24, 0.785; 0.70: 11, 0.814; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.357; 0.35: 92, 0.385; 0.40: 29, 0.408; 0.45: 6, 0.431; 0.50: 1, 0.630
- **K=13**: model 1793059200, labels learned 129327, probability skill vs chance 0.195, widened contest next: False
  - now: threshold 0.4125, hit rate recent 0.6249 / long run 0.5702
    - 6h: 11 calls (46 a day), hit rate 0.727, chance 0.080, naive rule 0.287, lift 9.12x
    - 24h: 61 calls (62 a day), hit rate 0.639, chance 0.085, naive rule 0.303, lift 7.56x
    - 7d: 429 calls (61 a day), hit rate 0.576, chance 0.078, naive rule 0.287, lift 7.37x
    - 30d: 1660 calls (55 a day), hit rate 0.569, chance 0.078, naive rule 0.279, lift 7.34x
  - next: threshold 0.2935, hit rate recent 0.3846 / long run 0.3227
    - 6h: 10 calls (42 a day), hit rate 0.700, chance 0.080, lift 8.78x
    - 24h: 57 calls (58 a day), hit rate 0.421, chance 0.085, lift 4.98x
    - 7d: 385 calls (55 a day), hit rate 0.338, chance 0.078, lift 4.32x
    - 30d: 1956 calls (65 a day), hit rate 0.318, chance 0.078, lift 4.10x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.444; 0.35: 91, 0.497; 0.40: 64, 0.553; 0.45: 43, 0.598; 0.50: 29, 0.654; 0.55: 18, 0.695; 0.60: 9, 0.737; 0.65: 2, 0.730; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.326; 0.35: 14, 0.353; 0.40: 3, 0.446; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.286 | -0.68% | 0.883 | 0.517 | 0.255 | 0.431 | 0.053 |
| 6h | 7.125 | 2.52% | 0.906 | 0.500 | 0.249 | 0.527 | 0.345 |
| 24h | 7.600 | 12.35% | 0.897 | 0.509 | 0.249 | 0.539 | 0.367 |
| 7d | 15.775 | 4.98% | 0.899 | 0.501 | 0.250 | 0.504 | 0.744 |
| 30d | 14.078 | 4.46% | 0.900 | 0.500 | 0.251 | 0.498 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.236 | 7.214 | 7.253 | 7.393 | 7.373 | 7.486 | 7.297 | 7.313 | 7.264 | 7.286 |
| 6h | 7.309 | 7.214 | 7.302 | 7.210 | 7.484 | 7.643 | 7.112 | 7.102 | 7.116 | 7.125 |
| 24h | 8.671 | 7.666 | 7.829 | 7.657 | 7.862 | 8.055 | 7.592 | 7.585 | 7.595 | 7.600 |
| 7d | 16.602 | 15.959 | 15.905 | 15.809 | 16.113 | 16.060 | 15.758 | 15.736 | 15.746 | 15.775 |
| 30d | 14.736 | 14.230 | 14.175 | 14.108 | 14.346 | 14.290 | 14.074 | 14.051 | 14.053 | 14.078 |

## Next candle

- candle starting 2026-10-31 23:43 UTC, last close 2250.62
- P(up) 0.5315, return quantiles (bp): {'05': -4.088, '10': -3.068, '25': -1.008, '40': -0.117, '50': 0.039, '60': 0.477, '75': 1.472, '90': 2.978, '95': 3.817}
- changepoint probability 0.0284, regime age 81.0 min
- agent weights: empirical 0.005, ewma 0.133, garch 0.051, har 0.150, bocpd 0.016, hmm 0.005, online_qr 0.313, lgbm 0.327

## Learning log

- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- HMM volatility states (sd, bp per minute): [3.53, 7.0, 20.69], current probabilities: [0.974, 0.026, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-31 23:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.387, 'l_abs': 0.544, 'l_hi': 0.663, 'l_lo': 0.699, 'b05': 0.637, 'b25': 0.555, 'b75': 0.563, 'b95': 0.631}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.313, 1.612, 1.941, 2.131, 2.435, 2.337, 2.712, 2.825, 3.233, 3.397, 3.485, 3.563, 3.856, 4.08]}
- calibration offsets (in sigma): {'05': 0.041, '10': -0.008, '25': 0.085, '40': 0.058, '50': -0.03, '60': -0.078, '75': -0.045, '90': -0.002, '95': -0.031}
