# ETH-USD 60s candle generator - report

- generated: 2026-11-01 02:39 UTC
- last closed candle: 2026-11-01 02:39 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.524 (672) [0.491, 0.562] | 0.521 (2877) [0.502, 0.540] | 0.516 (5754) [0.503, 0.528] | 0.520 (2782) [0.502, 0.540] | 0.300 (10) | 0.500 | flat -0.019 (noise 0.030) |
| colour_clear | 0.569 (723) | 0.541 (5558) [0.533, 0.551] | 0.544 (23531) [0.539, 0.549] | 0.520 (47049) [0.514, 0.526] | 0.546 (22811) [0.541, 0.550] | 0.554 (101) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.582 (184) | 0.587 (1090) [0.579, 0.596] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.600 (4283) [0.589, 0.612] | 0.571 (35) | 0.500 | flat -0.021 (noise 0.020) |
| colour_next | 0.554 (1397) | 0.529 (9992) [0.522, 0.537] | 0.529 (42831) [0.525, 0.533] | 0.515 (85748) [0.510, 0.519] | 0.530 (41399) [0.526, 0.534] | 0.591 (159) | 0.500 | flat -0.005 (noise 0.007) |
| colour_path | 0.504 (19558) | 0.502 (139888) [0.500, 0.504] | 0.501 (599634) [0.499, 0.502] | 0.501 (1200472) [0.500, 0.502] | 0.501 (579586) [0.499, 0.502] | 0.500 (2226) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.654 (52) | 0.604 (323) [0.574, 0.638] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.633 (1157) [0.613, 0.654] | 0.545 (11) | 0.500 | flat -0.032 (noise 0.038) |
| reversal_k13_next | 0.431 (58) | 0.339 (386) [0.297, 0.384] | 0.318 (1957) [0.306, 0.332] | 0.310 (4004) [0.299, 0.321] | 0.321 (1899) [0.308, 0.333] | 0.500 (4) | 0.077 | flat +0.030 (noise 0.032) |
| reversal_k13_now | 0.645 (62) | 0.577 (430) [0.535, 0.618] | 0.569 (1661) [0.549, 0.589] | 0.574 (3081) [0.560, 0.589] | 0.567 (1609) [0.547, 0.590] | 0.600 (10) | 0.077 | flat +0.047 (noise 0.037) |
| reversal_k3_next | 0.586 (157) | 0.588 (829) [0.582, 0.592] | 0.582 (3011) [0.572, 0.593] | 0.584 (5391) [0.575, 0.594] | 0.582 (2951) [0.571, 0.594] | 0.588 (17) | 0.294 | flat -0.005 (noise 0.025) |
| reversal_k3_now | 0.932 (74) | 0.945 (418) [0.920, 0.968] | 0.936 (1732) [0.926, 0.946] | 0.939 (3441) [0.933, 0.946] | 0.936 (1678) [0.926, 0.946] | 1.000 (7) | 0.294 | flat +0.000 (noise 0.018) |
| reversal_k5_next | 0.551 (69) | 0.519 (524) [0.507, 0.537] | 0.471 (2960) [0.458, 0.486] | 0.480 (4830) [0.469, 0.492] | 0.471 (2840) [0.456, 0.486] | 0.429 (7) | 0.187 | up +0.059 (noise 0.027) |
| reversal_k5_now | 0.797 (64) | 0.826 (409) [0.812, 0.839] | 0.822 (1628) [0.811, 0.833] | 0.829 (3180) [0.819, 0.839] | 0.821 (1569) [0.810, 0.832] | 1.000 (9) | 0.187 | flat +0.015 (noise 0.028) |
| reversal_k8_next | 0.484 (97) | 0.408 (714) [0.381, 0.436] | 0.388 (2842) [0.376, 0.401] | 0.391 (4901) [0.381, 0.402] | 0.388 (2795) [0.374, 0.401] | 0.500 (6) | 0.121 | flat +0.031 (noise 0.025) |
| reversal_k8_now | 0.763 (59) | 0.705 (380) [0.649, 0.749] | 0.692 (1583) [0.671, 0.712] | 0.702 (3119) [0.687, 0.718] | 0.690 (1532) [0.667, 0.711] | 0.875 (8) | 0.121 | flat +0.052 (noise 0.038) |
| overall | 0.511 (21691) | 0.507 (154642) [0.504, 0.509] | 0.504 (662716) [0.503, 0.506] | 0.504 (1323921) [0.503, 0.504] | 0.504 (640640) [0.503, 0.506] | 0.510 (2463) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08146, 0.1251] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5288, 'levels': [{'threshold': 0.08146, 'calls_per_day': 144.8, 'win_rate': 0.5939}, {'threshold': 0.1251, 'calls_per_day': 36.3, 'win_rate': 0.6055}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 40415, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14933 | 0.336 | 0.526 (14677) | 0.580 (2106) | 0.757 (2624) |
| volatility: normal | 14933 | 0.366 | 0.532 (14860) | 0.612 (1460) | 0.748 (2211) |
| volatility: wild | 14933 | 0.381 | 0.526 (14890) | 0.630 (752) | 0.771 (2032) |
| session: Asia 00-08 | 15039 | 0.360 | 0.532 (14938) | 0.601 (1527) | 0.763 (2281) |
| session: Europe 08-13 | 9300 | 0.356 | 0.530 (9210) | 0.594 (1059) | 0.754 (1539) |
| session: US 13-21 | 14880 | 0.368 | 0.527 (14758) | 0.600 (1127) | 0.759 (2213) |
| session: late 21-24 | 5580 | 0.351 | 0.517 (5521) | 0.607 (605) | 0.749 (834) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.348 | 0.328 | 0.259 | 0.259 | 0.567 | 0.282 | 0.414 | 0.865 |
| 6h | 360 | 0.322 | 0.318 | 0.233 | 0.261 | 0.552 | 0.249 | 0.396 | 1.180 |
| 24h | 1440 | 0.327 | 0.320 | 0.234 | 0.249 | 0.568 | 0.262 | 0.393 | 1.277 |
| 7d | 10080 | 0.363 | 0.356 | 0.280 | 0.309 | 0.532 | 0.263 | 0.464 | 1.262 |
| 30d | 43200 | 0.361 | 0.353 | 0.275 | 0.304 | 0.529 | 0.260 | 0.461 | 1.279 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.348 / 0.567 / 0.850; 2: 0.318 / 0.433 / 0.850; 3: 0.329 / 0.483 / 0.817; 4: 0.318 / 0.467 / 0.850; 5: 0.346 / 0.567 / 0.833; 6: 0.299 / 0.417 / 0.817; 7: 0.328 / 0.517 / 0.750; 8: 0.317 / 0.483 / 0.800; 9: 0.340 / 0.550 / 0.733; 10: 0.351 / 0.600 / 0.783; 11: 0.322 / 0.467 / 0.800; 12: 0.320 / 0.467 / 0.833; 13: 0.356 / 0.583 / 0.833; 14: 0.312 / 0.417 / 0.883; 15: 0.353 / 0.583 / 0.900
- 6h: 1: 0.322 / 0.552 / 0.881; 2: 0.315 / 0.511 / 0.867; 3: 0.307 / 0.500 / 0.864; 4: 0.314 / 0.543 / 0.883; 5: 0.313 / 0.540 / 0.878; 6: 0.299 / 0.486 / 0.867; 7: 0.309 / 0.506 / 0.856; 8: 0.288 / 0.477 / 0.864; 9: 0.313 / 0.529 / 0.861; 10: 0.298 / 0.514 / 0.872; 11: 0.313 / 0.520 / 0.867; 12: 0.299 / 0.497 / 0.875; 13: 0.309 / 0.506 / 0.867; 14: 0.291 / 0.448 / 0.864; 15: 0.309 / 0.537 / 0.889
- 24h: 1: 0.327 / 0.568 / 0.878; 2: 0.306 / 0.487 / 0.897; 3: 0.307 / 0.508 / 0.894; 4: 0.306 / 0.514 / 0.897; 5: 0.313 / 0.540 / 0.895; 6: 0.299 / 0.487 / 0.888; 7: 0.303 / 0.489 / 0.889; 8: 0.302 / 0.511 / 0.888; 9: 0.313 / 0.537 / 0.888; 10: 0.298 / 0.483 / 0.890; 11: 0.300 / 0.496 / 0.890; 12: 0.301 / 0.490 / 0.890; 13: 0.304 / 0.507 / 0.888; 14: 0.296 / 0.468 / 0.885; 15: 0.307 / 0.520 / 0.890
- 7d: 1: 0.363 / 0.532 / 0.895; 2: 0.350 / 0.491 / 0.899; 3: 0.353 / 0.507 / 0.900; 4: 0.351 / 0.505 / 0.900; 5: 0.351 / 0.508 / 0.899; 6: 0.347 / 0.503 / 0.899; 7: 0.350 / 0.498 / 0.899; 8: 0.348 / 0.507 / 0.899; 9: 0.350 / 0.505 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.348 / 0.501 / 0.900; 13: 0.347 / 0.500 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.347 / 0.499 / 0.901
- 30d: 1: 0.361 / 0.529 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.351 / 0.508 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.346 / 0.498 / 0.900; 7: 0.346 / 0.500 / 0.900; 8: 0.346 / 0.501 / 0.900; 9: 0.345 / 0.498 / 0.900; 10: 0.346 / 0.504 / 0.900; 11: 0.344 / 0.497 / 0.900; 12: 0.345 / 0.503 / 0.900; 13: 0.345 / 0.501 / 0.900; 14: 0.344 / 0.500 / 0.900; 15: 0.344 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.095 (body 0.081, range 0.110); 'price stays where it was' would score 0.141; colour right 0.467; typical miss of the close 6.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.109 (body 0.075, range 0.142); 'price stays where it was' would score 0.136; colour right 0.511; typical miss of the close 4.8 bp; chain ended on the right side 0.292 of 24 chains; n=360
- 24h: match 0.112 (body 0.081, range 0.144); 'price stays where it was' would score 0.121; colour right 0.519; typical miss of the close 4.6 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.127 (body 0.086, range 0.168); 'price stays where it was' would score 0.132; colour right 0.504; typical miss of the close 8.6 bp; chain ended on the right side 0.516 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 7.7 bp; chain ended on the right side 0.520 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.9; 2: 0.198 / 4.6; 3: 0.168 / 6.1; 4: 0.132 / 6.5; 5: 0.125 / 7.2; 6: 0.113 / 7.6; 7: 0.111 / 8.0; 8: 0.098 / 8.5; 9: 0.089 / 8.5; 10: 0.088 / 9.1; 11: 0.085 / 9.6; 12: 0.076 / 9.9; 13: 0.068 / 10.0; 14: 0.070 / 10.4; 15: 0.063 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 129513, probability skill vs chance 0.2265, widened contest next: False
  - now: threshold 0.8348, hit rate recent 0.9468 / long run 0.9432
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.306, naive rule 0.535, lift 3.27x
    - 24h: 72 calls (72 a day), hit rate 0.944, chance 0.311, naive rule 0.530, lift 3.04x
    - 7d: 420 calls (60 a day), hit rate 0.945, chance 0.294, naive rule 0.497, lift 3.22x
    - 30d: 1729 calls (58 a day), hit rate 0.936, chance 0.294, naive rule 0.495, lift 3.18x
  - next: threshold 0.5302, hit rate recent 0.6058 / long run 0.5901
    - 6h: 35 calls (142 a day), hit rate 0.629, chance 0.306, lift 2.06x
    - 24h: 154 calls (155 a day), hit rate 0.584, chance 0.311, lift 1.88x
    - 7d: 842 calls (120 a day), hit rate 0.586, chance 0.294, lift 1.99x
    - 30d: 3023 calls (101 a day), hit rate 0.581, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 535, 0.523; 0.40: 474, 0.580; 0.45: 405, 0.652; 0.50: 355, 0.702; 0.55: 309, 0.744; 0.60: 261, 0.789; 0.65: 219, 0.815; 0.70: 173, 0.846; 0.75: 136, 0.879; 0.80: 92, 0.914; 0.85: 46, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.428; 0.35: 502, 0.463; 0.40: 407, 0.496; 0.45: 310, 0.532; 0.50: 200, 0.569; 0.55: 89, 0.571; 0.60: 13, 0.643; 0.65: 1, 0.654
- **K=5**: model 1792540800, labels learned 129511, probability skill vs chance 0.2249, widened contest next: False
  - now: threshold 0.6782, hit rate recent 0.8321 / long run 0.8242
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.205, naive rule 0.470, lift 4.87x
    - 24h: 65 calls (65 a day), hit rate 0.831, chance 0.200, naive rule 0.439, lift 4.16x
    - 7d: 413 calls (59 a day), hit rate 0.828, chance 0.188, naive rule 0.410, lift 4.41x
    - 30d: 1629 calls (54 a day), hit rate 0.823, chance 0.188, naive rule 0.405, lift 4.37x
  - next: threshold 0.4545, hit rate recent 0.5418 / long run 0.5002
    - 6h: 17 calls (69 a day), hit rate 0.588, chance 0.205, lift 2.86x
    - 24h: 65 calls (65 a day), hit rate 0.523, chance 0.200, lift 2.62x
    - 7d: 516 calls (74 a day), hit rate 0.512, chance 0.188, lift 2.72x
    - 30d: 2960 calls (99 a day), hit rate 0.471, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.428; 0.35: 345, 0.494; 0.40: 278, 0.568; 0.45: 227, 0.621; 0.50: 180, 0.668; 0.55: 141, 0.707; 0.60: 108, 0.751; 0.65: 76, 0.790; 0.70: 51, 0.826; 0.75: 30, 0.870; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.388; 0.35: 255, 0.420; 0.40: 160, 0.457; 0.45: 69, 0.477; 0.50: 13, 0.491; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 129508, probability skill vs chance 0.2086, widened contest next: False
  - now: threshold 0.5645, hit rate recent 0.7646 / long run 0.6978
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.113, naive rule 0.328, lift 8.12x
    - 24h: 58 calls (58 a day), hit rate 0.793, chance 0.124, naive rule 0.350, lift 6.37x
    - 7d: 383 calls (55 a day), hit rate 0.708, chance 0.122, naive rule 0.343, lift 5.78x
    - 30d: 1585 calls (53 a day), hit rate 0.693, chance 0.121, naive rule 0.334, lift 5.72x
  - next: threshold 0.3634, hit rate recent 0.4902 / long run 0.4073
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.113, lift 4.43x
    - 24h: 84 calls (85 a day), hit rate 0.500, chance 0.124, lift 4.02x
    - 7d: 707 calls (101 a day), hit rate 0.406, chance 0.122, lift 3.32x
    - 30d: 2843 calls (95 a day), hit rate 0.389, chance 0.121, lift 3.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 244, 0.433; 0.35: 189, 0.501; 0.40: 147, 0.548; 0.45: 112, 0.596; 0.50: 84, 0.639; 0.55: 61, 0.679; 0.60: 41, 0.716; 0.65: 24, 0.786; 0.70: 11, 0.812; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.357; 0.35: 92, 0.386; 0.40: 29, 0.409; 0.45: 6, 0.434; 0.50: 1, 0.630
- **K=13**: model 1793491200, labels learned 129503, probability skill vs chance 0.1974, widened contest next: False
  - now: threshold 0.413, hit rate recent 0.6282 / long run 0.5714
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.080, naive rule 0.312, lift 8.69x
    - 24h: 63 calls (64 a day), hit rate 0.635, chance 0.087, naive rule 0.321, lift 7.33x
    - 7d: 435 calls (62 a day), hit rate 0.579, chance 0.079, naive rule 0.288, lift 7.35x
    - 30d: 1665 calls (56 a day), hit rate 0.569, chance 0.078, naive rule 0.279, lift 7.33x
  - next: threshold 0.2935, hit rate recent 0.4019 / long run 0.325
    - 6h: 10 calls (42 a day), hit rate 0.600, chance 0.080, lift 7.53x
    - 24h: 53 calls (54 a day), hit rate 0.453, chance 0.087, lift 5.22x
    - 7d: 382 calls (55 a day), hit rate 0.338, chance 0.079, lift 4.29x
    - 30d: 1952 calls (65 a day), hit rate 0.319, chance 0.078, lift 4.11x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 127, 0.444; 0.35: 91, 0.496; 0.40: 64, 0.553; 0.45: 43, 0.598; 0.50: 29, 0.655; 0.55: 18, 0.694; 0.60: 9, 0.739; 0.65: 2, 0.733; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.327; 0.35: 14, 0.354; 0.40: 3, 0.446; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.333 | 5.10% | 0.883 | 0.350 | 0.254 | 0.517 | 0.371 |
| 6h | 8.166 | 2.23% | 0.892 | 0.458 | 0.249 | 0.534 | 0.364 |
| 24h | 7.463 | 10.68% | 0.893 | 0.502 | 0.248 | 0.545 | 0.353 |
| 7d | 15.790 | 4.97% | 0.899 | 0.499 | 0.250 | 0.504 | 0.743 |
| 30d | 14.062 | 4.47% | 0.900 | 0.500 | 0.251 | 0.498 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.942 | 11.512 | 11.354 | 11.215 | 11.533 | 11.371 | 11.308 | 11.254 | 11.252 | 11.333 |
| 6h | 8.352 | 8.284 | 8.262 | 8.212 | 8.427 | 8.484 | 8.158 | 8.150 | 8.149 | 8.166 |
| 24h | 8.355 | 7.541 | 7.681 | 7.514 | 7.728 | 7.924 | 7.452 | 7.447 | 7.458 | 7.463 |
| 7d | 16.615 | 15.973 | 15.918 | 15.823 | 16.128 | 16.072 | 15.772 | 15.750 | 15.760 | 15.790 |
| 30d | 14.720 | 14.214 | 14.159 | 14.091 | 14.329 | 14.275 | 14.058 | 14.035 | 14.037 | 14.062 |

## Next candle

- candle starting 2026-11-01 02:39 UTC, last close 2262.09
- P(up) 0.5217, return quantiles (bp): {'05': -5.788, '10': -4.61, '25': -1.916, '40': -0.498, '50': 0.134, '60': 0.948, '75': 2.447, '90': 4.695, '95': 6.101}
- changepoint probability 0.069, regime age 62.5 min
- agent weights: empirical 0.006, ewma 0.098, garch 0.073, har 0.186, bocpd 0.023, hmm 0.009, online_qr 0.294, lgbm 0.311

## Learning log

- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- HMM volatility states (sd, bp per minute): [3.03, 6.64, 20.06], current probabilities: [0.944, 0.054, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-01 02:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.352, 'l_abs': 0.541, 'l_hi': 0.662, 'l_lo': 0.715, 'b05': 0.641, 'b25': 0.549, 'b75': 0.576, 'b95': 0.638}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.717, 2.15, 2.25, 2.471, 2.998, 3.244, 3.475, 3.768, 3.98, 4.1, 3.806, 4.131, 4.382, 3.951]}
- calibration offsets (in sigma): {'05': 0.039, '10': -0.042, '25': 0.045, '40': 0.042, '50': 0.03, '60': 0.038, '75': 0.075, '90': 0.092, '95': 0.011}
