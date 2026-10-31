# ETH-USD 60s candle generator - report

- generated: 2026-10-31 00:40 UTC
- last closed candle: 2026-10-31 00:40 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.525 (672) [0.493, 0.564] | 0.520 (2877) [0.501, 0.539] | 0.516 (5658) [0.502, 0.529] | 0.521 (2686) [0.500, 0.541] | 0.500 (2) | 0.500 | flat -0.013 (noise 0.030) |
| colour_clear | 0.537 (771) | 0.538 (5578) [0.532, 0.544] | 0.541 (23615) [0.534, 0.547] | 0.519 (46326) [0.513, 0.525] | 0.545 (22088) [0.540, 0.549] | 0.417 (24) | 0.500 | flat -0.018 (noise 0.009) |
| colour_confident | 0.590 (78) | 0.592 (1175) [0.583, 0.602] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.250 (4) | 0.500 | flat -0.013 (noise 0.020) |
| colour_next | 0.532 (1435) | 0.525 (10026) [0.520, 0.528] | 0.527 (42871) [0.523, 0.531] | 0.514 (84351) [0.510, 0.518] | 0.529 (40002) [0.525, 0.533] | 0.400 (40) | 0.500 | flat -0.013 (noise 0.007) |
| colour_path | 0.503 (20090) | 0.502 (140364) [0.500, 0.504] | 0.501 (600194) [0.499, 0.502] | 0.501 (1180914) [0.500, 0.502] | 0.501 (560028) [0.499, 0.502] | 0.479 (560) | 0.500 | flat +0.003 (noise 0.002) |
| colour_strong | 0.538 (13) | 0.596 (369) [0.574, 0.625] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.000 (1) | 0.500 | flat -0.046 (noise 0.039) |
| reversal_k13_next | 0.283 (53) | 0.317 (391) [0.282, 0.359] | 0.315 (2003) [0.303, 0.327] | 0.308 (3946) [0.297, 0.319] | 0.317 (1841) [0.306, 0.329] | - | 0.077 | flat +0.003 (noise 0.032) |
| reversal_k13_now | 0.597 (57) | 0.575 (419) [0.531, 0.618] | 0.567 (1653) [0.547, 0.587] | 0.572 (3019) [0.558, 0.587] | 0.564 (1547) [0.543, 0.587] | 0.333 (3) | 0.077 | flat +0.050 (noise 0.035) |
| reversal_k3_next | 0.595 (116) | 0.591 (726) [0.583, 0.599] | 0.583 (2939) [0.571, 0.595] | 0.584 (5234) [0.575, 0.594] | 0.582 (2794) [0.570, 0.593] | 0.500 (4) | 0.293 | flat +0.005 (noise 0.025) |
| reversal_k3_now | 0.933 (45) | 0.952 (393) [0.924, 0.977] | 0.936 (1731) [0.926, 0.946] | 0.939 (3367) [0.933, 0.946] | 0.936 (1604) [0.925, 0.947] | 0.800 (5) | 0.293 | flat +0.022 (noise 0.021) |
| reversal_k5_next | 0.568 (37) | 0.507 (580) [0.495, 0.524] | 0.471 (3038) [0.457, 0.485] | 0.479 (4761) [0.467, 0.492] | 0.469 (2771) [0.455, 0.484] | 0.333 (3) | 0.187 | flat +0.051 (noise 0.026) |
| reversal_k5_now | 0.780 (41) | 0.830 (400) [0.817, 0.839] | 0.824 (1619) [0.812, 0.835] | 0.830 (3116) [0.820, 0.840] | 0.822 (1505) [0.810, 0.833] | 0.333 (3) | 0.187 | flat +0.017 (noise 0.028) |
| reversal_k8_next | 0.402 (92) | 0.394 (703) [0.375, 0.412] | 0.386 (2799) [0.374, 0.398] | 0.390 (4804) [0.379, 0.400] | 0.384 (2698) [0.372, 0.397] | 0.500 (2) | 0.121 | flat +0.017 (noise 0.025) |
| reversal_k8_now | 0.614 (44) | 0.697 (376) [0.643, 0.740] | 0.689 (1571) [0.668, 0.709] | 0.701 (3060) [0.685, 0.717] | 0.687 (1473) [0.664, 0.709] | 0.333 (3) | 0.121 | flat +0.037 (noise 0.040) |
| overall | 0.506 (22106) | 0.506 (155050) [0.504, 0.508] | 0.504 (663295) [0.503, 0.506] | 0.503 (1302230) [0.502, 0.504] | 0.504 (618949) [0.503, 0.506] | 0.474 (625) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08157, 0.1245] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.525, 'levels': [{'threshold': 0.08157, 'calls_per_day': 143.0, 'win_rate': 0.6024}, {'threshold': 0.1245, 'calls_per_day': 35.7, 'win_rate': 0.5936}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 38900, 'rate': 0.5295}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14894 | 0.340 | 0.522 (14670) | 0.581 (1993) | 0.749 (2540) |
| volatility: normal | 14893 | 0.366 | 0.532 (14827) | 0.615 (1380) | 0.756 (2213) |
| volatility: wild | 14893 | 0.381 | 0.524 (14852) | 0.627 (730) | 0.765 (2025) |
| session: Asia 00-08 | 14920 | 0.361 | 0.532 (14820) | 0.602 (1458) | 0.758 (2238) |
| session: Europe 08-13 | 9300 | 0.357 | 0.528 (9215) | 0.593 (1012) | 0.750 (1510) |
| session: US 13-21 | 14880 | 0.370 | 0.523 (14788) | 0.601 (1055) | 0.762 (2172) |
| session: late 21-24 | 5580 | 0.352 | 0.514 (5526) | 0.609 (578) | 0.749 (858) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.348 | 0.367 | 0.266 | 0.266 | 0.517 | 0.231 | 0.464 | 1.027 |
| 6h | 360 | 0.359 | 0.361 | 0.284 | 0.294 | 0.510 | 0.245 | 0.473 | 1.267 |
| 24h | 1440 | 0.380 | 0.373 | 0.294 | 0.331 | 0.529 | 0.266 | 0.494 | 1.244 |
| 7d | 10080 | 0.368 | 0.361 | 0.285 | 0.316 | 0.524 | 0.263 | 0.473 | 1.236 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.307 | 0.527 | 0.260 | 0.464 | 1.273 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.348 / 0.517 / 0.967; 2: 0.336 / 0.450 / 0.933; 3: 0.332 / 0.450 / 0.983; 4: 0.347 / 0.533 / 1.000; 5: 0.367 / 0.567 / 0.950; 6: 0.328 / 0.433 / 0.950; 7: 0.347 / 0.433 / 0.967; 8: 0.341 / 0.517 / 0.983; 9: 0.333 / 0.433 / 0.967; 10: 0.363 / 0.567 / 0.983; 11: 0.341 / 0.500 / 0.983; 12: 0.356 / 0.533 / 0.983; 13: 0.362 / 0.583 / 1.000; 14: 0.328 / 0.433 / 1.000; 15: 0.330 / 0.450 / 1.000
- 6h: 1: 0.359 / 0.510 / 0.911; 2: 0.361 / 0.513 / 0.922; 3: 0.360 / 0.499 / 0.903; 4: 0.352 / 0.479 / 0.886; 5: 0.341 / 0.485 / 0.867; 6: 0.359 / 0.513 / 0.922; 7: 0.344 / 0.440 / 0.911; 8: 0.360 / 0.557 / 0.922; 9: 0.352 / 0.490 / 0.933; 10: 0.368 / 0.549 / 0.917; 11: 0.348 / 0.479 / 0.919; 12: 0.359 / 0.501 / 0.958; 13: 0.359 / 0.510 / 0.961; 14: 0.356 / 0.493 / 0.950; 15: 0.353 / 0.473 / 0.975
- 24h: 1: 0.380 / 0.529 / 0.909; 2: 0.370 / 0.491 / 0.905; 3: 0.371 / 0.505 / 0.903; 4: 0.369 / 0.493 / 0.900; 5: 0.368 / 0.501 / 0.899; 6: 0.371 / 0.516 / 0.908; 7: 0.370 / 0.489 / 0.906; 8: 0.369 / 0.516 / 0.911; 9: 0.366 / 0.486 / 0.912; 10: 0.370 / 0.510 / 0.907; 11: 0.366 / 0.495 / 0.910; 12: 0.373 / 0.514 / 0.919; 13: 0.370 / 0.514 / 0.919; 14: 0.370 / 0.514 / 0.919; 15: 0.367 / 0.489 / 0.922
- 7d: 1: 0.368 / 0.524 / 0.899; 2: 0.355 / 0.490 / 0.901; 3: 0.359 / 0.509 / 0.901; 4: 0.356 / 0.500 / 0.900; 5: 0.355 / 0.505 / 0.901; 6: 0.353 / 0.503 / 0.901; 7: 0.355 / 0.500 / 0.902; 8: 0.354 / 0.507 / 0.902; 9: 0.353 / 0.499 / 0.902; 10: 0.355 / 0.506 / 0.902; 11: 0.352 / 0.502 / 0.902; 12: 0.354 / 0.504 / 0.902; 13: 0.352 / 0.503 / 0.903; 14: 0.352 / 0.504 / 0.902; 15: 0.351 / 0.497 / 0.903
- 30d: 1: 0.362 / 0.527 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.126 (body 0.073, range 0.180); 'price stays where it was' would score 0.128; colour right 0.600; typical miss of the close 5.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.108 (body 0.065, range 0.150); 'price stays where it was' would score 0.130; colour right 0.524; typical miss of the close 10.0 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.133; colour right 0.530; typical miss of the close 13.0 bp; chain ended on the right side 0.469 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.170); 'price stays where it was' would score 0.136; colour right 0.500; typical miss of the close 9.2 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.164); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 7.9 bp; chain ended on the right side 0.520 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.0; 2: 0.200 / 4.7; 3: 0.168 / 6.2; 4: 0.132 / 6.6; 5: 0.126 / 7.4; 6: 0.113 / 7.8; 7: 0.111 / 8.1; 8: 0.098 / 8.7; 9: 0.089 / 8.8; 10: 0.088 / 9.3; 11: 0.086 / 9.8; 12: 0.076 / 10.2; 13: 0.068 / 10.4; 14: 0.070 / 10.7; 15: 0.062 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 127954, probability skill vs chance 0.2405, widened contest next: False
  - now: threshold 0.8334, hit rate recent 0.9446 / long run 0.9426
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.280, naive rule 0.470, lift 3.15x
    - 24h: 48 calls (48 a day), hit rate 0.938, chance 0.292, naive rule 0.506, lift 3.21x
    - 7d: 398 calls (57 a day), hit rate 0.950, chance 0.293, naive rule 0.498, lift 3.24x
    - 30d: 1731 calls (58 a day), hit rate 0.936, chance 0.294, naive rule 0.493, lift 3.19x
  - next: threshold 0.529, hit rate recent 0.6027 / long run 0.59
    - 6h: 36 calls (146 a day), hit rate 0.611, chance 0.280, lift 2.18x
    - 24h: 116 calls (116 a day), hit rate 0.595, chance 0.292, lift 2.04x
    - 7d: 729 calls (104 a day), hit rate 0.591, chance 0.293, lift 2.01x
    - 30d: 2939 calls (98 a day), hit rate 0.583, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.496; 0.35: 536, 0.521; 0.40: 475, 0.578; 0.45: 407, 0.650; 0.50: 356, 0.700; 0.55: 311, 0.742; 0.60: 263, 0.788; 0.65: 220, 0.813; 0.70: 174, 0.845; 0.75: 136, 0.879; 0.80: 91, 0.915; 0.85: 47, 0.948; 0.90: 5, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.464; 0.40: 407, 0.498; 0.45: 310, 0.532; 0.50: 199, 0.569; 0.55: 88, 0.571; 0.60: 13, 0.643; 0.65: 1, 0.630
- **K=5**: model 1792540800, labels learned 127952, probability skill vs chance 0.229, widened contest next: False
  - now: threshold 0.6777, hit rate recent 0.7986 / long run 0.822
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.183, naive rule 0.378, lift 4.26x
    - 24h: 40 calls (40 a day), hit rate 0.775, chance 0.181, naive rule 0.410, lift 4.28x
    - 7d: 403 calls (58 a day), hit rate 0.826, chance 0.185, naive rule 0.409, lift 4.47x
    - 30d: 1620 calls (54 a day), hit rate 0.823, chance 0.188, naive rule 0.404, lift 4.38x
  - next: threshold 0.4552, hit rate recent 0.5299 / long run 0.4941
    - 6h: 18 calls (73 a day), hit rate 0.556, chance 0.183, lift 3.04x
    - 24h: 38 calls (38 a day), hit rate 0.553, chance 0.181, lift 3.05x
    - 7d: 580 calls (83 a day), hit rate 0.507, chance 0.185, lift 2.74x
    - 30d: 3034 calls (101 a day), hit rate 0.471, chance 0.188, lift 2.51x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.492; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 180, 0.668; 0.55: 141, 0.707; 0.60: 108, 0.753; 0.65: 76, 0.790; 0.70: 51, 0.828; 0.75: 30, 0.870; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.389; 0.35: 254, 0.421; 0.40: 158, 0.457; 0.45: 68, 0.476; 0.50: 13, 0.494; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 127949, probability skill vs chance 0.2082, widened contest next: False
  - now: threshold 0.5639, hit rate recent 0.6803 / long run 0.6865
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.134, naive rule 0.381, lift 5.21x
    - 24h: 43 calls (43 a day), hit rate 0.651, chance 0.123, naive rule 0.348, lift 5.29x
    - 7d: 379 calls (54 a day), hit rate 0.694, chance 0.122, naive rule 0.344, lift 5.70x
    - 30d: 1573 calls (52 a day), hit rate 0.688, chance 0.121, naive rule 0.334, lift 5.67x
  - next: threshold 0.3302, hit rate recent 0.4289 / long run 0.3926
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.134, lift 3.35x
    - 24h: 91 calls (92 a day), hit rate 0.418, chance 0.123, lift 3.39x
    - 7d: 702 calls (100 a day), hit rate 0.395, chance 0.122, lift 3.24x
    - 30d: 2798 calls (93 a day), hit rate 0.386, chance 0.121, lift 3.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 189, 0.499; 0.40: 147, 0.548; 0.45: 112, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.676; 0.60: 40, 0.710; 0.65: 23, 0.774; 0.70: 11, 0.809; 0.75: 2, 0.746
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.359; 0.35: 92, 0.386; 0.40: 29, 0.408; 0.45: 6, 0.436; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 127944, probability skill vs chance 0.1891, widened contest next: False
  - now: threshold 0.4107, hit rate recent 0.5894 / long run 0.5617
    - 6h: 11 calls (46 a day), hit rate 0.818, chance 0.083, naive rule 0.337, lift 9.90x
    - 24h: 56 calls (57 a day), hit rate 0.625, chance 0.077, naive rule 0.291, lift 8.13x
    - 7d: 422 calls (60 a day), hit rate 0.573, chance 0.077, naive rule 0.284, lift 7.47x
    - 30d: 1655 calls (55 a day), hit rate 0.567, chance 0.077, naive rule 0.278, lift 7.33x
  - next: threshold 0.2932, hit rate recent 0.2993 / long run 0.3127
    - 6h: 9 calls (38 a day), hit rate 0.222, chance 0.083, lift 2.69x
    - 24h: 50 calls (51 a day), hit rate 0.300, chance 0.077, lift 3.90x
    - 7d: 388 calls (56 a day), hit rate 0.320, chance 0.077, lift 4.16x
    - 30d: 1998 calls (67 a day), hit rate 0.315, chance 0.077, lift 4.07x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.443; 0.35: 90, 0.495; 0.40: 64, 0.550; 0.45: 42, 0.599; 0.50: 28, 0.654; 0.55: 17, 0.695; 0.60: 8, 0.736; 0.65: 2, 0.725; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.325; 0.35: 14, 0.351; 0.40: 3, 0.438; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.694 | 26.79% | 0.983 | 0.517 | 0.251 | 0.517 | 0.232 |
| 6h | 14.275 | 9.65% | 0.919 | 0.539 | 0.251 | 0.490 | 0.664 |
| 24h | 21.280 | 4.03% | 0.911 | 0.499 | 0.251 | 0.487 | 0.628 |
| 7d | 16.545 | 4.63% | 0.900 | 0.500 | 0.251 | 0.497 | 0.731 |
| 30d | 14.291 | 4.30% | 0.900 | 0.500 | 0.251 | 0.496 | 0.691 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.510 | 7.746 | 7.989 | 7.728 | 7.947 | 8.026 | 7.642 | 7.694 | 7.718 | 7.694 |
| 6h | 15.799 | 14.310 | 14.410 | 14.251 | 14.551 | 14.449 | 14.275 | 14.225 | 14.248 | 14.275 |
| 24h | 22.173 | 21.534 | 21.390 | 21.369 | 21.712 | 21.579 | 21.261 | 21.206 | 21.247 | 21.280 |
| 7d | 17.348 | 16.750 | 16.655 | 16.580 | 16.883 | 16.796 | 16.531 | 16.501 | 16.514 | 16.545 |
| 30d | 14.933 | 14.443 | 14.382 | 14.317 | 14.559 | 14.493 | 14.286 | 14.264 | 14.265 | 14.291 |

## Next candle

- candle starting 2026-10-31 00:40 UTC, last close 2244.27
- P(up) 0.5163, return quantiles (bp): {'05': -5.548, '10': -4.202, '25': -1.969, '40': -0.602, '50': 0.115, '60': 0.867, '75': 2.217, '90': 3.917, '95': 5.174}
- changepoint probability 0.0211, regime age 127.5 min
- agent weights: empirical 0.003, ewma 0.086, garch 0.099, har 0.208, bocpd 0.035, hmm 0.039, online_qr 0.247, lgbm 0.285

## Learning log

- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.94, 7.31, 20.82], current probabilities: [0.934, 0.064, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-31 00:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.501, 'l_abs': 0.677, 'l_hi': 0.732, 'l_lo': 0.714, 'b05': 0.733, 'b25': 0.642, 'b75': 0.699, 'b95': 0.735}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8]], 'cone_width': [1.295, 1.589, 2.158, 2.417, 2.449, 2.651, 2.84, 2.9, 3.188, 3.284, 3.048, 3.116, 3.305, 3.36]}
- calibration offsets (in sigma): {'05': 0.0495, '10': 0.029, '25': 0.0475, '40': 0.046, '50': 0.035, '60': 0.034, '75': 0.0325, '90': -0.079, '95': -0.1195}
