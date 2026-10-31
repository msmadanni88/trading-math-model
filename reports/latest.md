# ETH-USD 60s candle generator - report

- generated: 2026-10-31 17:25 UTC
- last closed candle: 2026-10-31 17:25 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.525 (672) [0.493, 0.564] | 0.520 (2877) [0.501, 0.539] | 0.516 (5658) [0.502, 0.529] | 0.521 (2686) [0.500, 0.541] | 0.522 (69) | 0.500 | flat -0.013 (noise 0.030) |
| colour_clear | 0.537 (771) | 0.538 (5578) [0.532, 0.544] | 0.541 (23615) [0.534, 0.547] | 0.519 (46326) [0.513, 0.525] | 0.545 (22088) [0.540, 0.549] | 0.558 (539) | 0.500 | flat -0.018 (noise 0.009) |
| colour_confident | 0.590 (78) | 0.592 (1175) [0.583, 0.602] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.548 (124) | 0.500 | flat -0.013 (noise 0.020) |
| colour_next | 0.532 (1435) | 0.525 (10026) [0.520, 0.528] | 0.527 (42871) [0.523, 0.531] | 0.514 (84351) [0.510, 0.518] | 0.529 (40002) [0.525, 0.533] | 0.545 (1030) | 0.500 | flat -0.013 (noise 0.007) |
| colour_path | 0.503 (20090) | 0.502 (140364) [0.500, 0.504] | 0.501 (600194) [0.499, 0.502] | 0.501 (1180914) [0.500, 0.502] | 0.501 (560028) [0.499, 0.502] | 0.501 (14420) | 0.500 | flat +0.003 (noise 0.002) |
| colour_strong | 0.538 (13) | 0.596 (369) [0.574, 0.625] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.625 (40) | 0.500 | flat -0.046 (noise 0.039) |
| reversal_k13_next | 0.283 (53) | 0.317 (391) [0.282, 0.359] | 0.315 (2003) [0.303, 0.327] | 0.308 (3946) [0.297, 0.319] | 0.317 (1841) [0.306, 0.329] | 0.356 (45) | 0.077 | flat +0.003 (noise 0.032) |
| reversal_k13_now | 0.597 (57) | 0.575 (419) [0.531, 0.618] | 0.567 (1653) [0.547, 0.587] | 0.572 (3019) [0.558, 0.587] | 0.564 (1547) [0.543, 0.587] | 0.620 (50) | 0.077 | flat +0.050 (noise 0.035) |
| reversal_k3_next | 0.595 (116) | 0.591 (726) [0.583, 0.599] | 0.583 (2939) [0.571, 0.595] | 0.584 (5234) [0.575, 0.594] | 0.582 (2794) [0.570, 0.593] | 0.555 (119) | 0.293 | flat +0.005 (noise 0.025) |
| reversal_k3_now | 0.933 (45) | 0.952 (393) [0.924, 0.977] | 0.936 (1731) [0.926, 0.946] | 0.939 (3367) [0.933, 0.946] | 0.936 (1604) [0.925, 0.947] | 0.912 (57) | 0.293 | flat +0.022 (noise 0.021) |
| reversal_k5_next | 0.568 (37) | 0.507 (580) [0.495, 0.524] | 0.471 (3038) [0.457, 0.485] | 0.479 (4761) [0.467, 0.492] | 0.469 (2771) [0.455, 0.484] | 0.500 (50) | 0.187 | flat +0.051 (noise 0.026) |
| reversal_k5_now | 0.780 (41) | 0.830 (400) [0.817, 0.839] | 0.824 (1619) [0.812, 0.835] | 0.830 (3116) [0.820, 0.840] | 0.822 (1505) [0.810, 0.833] | 0.760 (50) | 0.187 | flat +0.017 (noise 0.028) |
| reversal_k8_next | 0.402 (92) | 0.394 (703) [0.375, 0.412] | 0.386 (2799) [0.374, 0.398] | 0.390 (4804) [0.379, 0.400] | 0.384 (2698) [0.372, 0.397] | 0.463 (82) | 0.121 | flat +0.017 (noise 0.025) |
| reversal_k8_now | 0.614 (44) | 0.697 (376) [0.643, 0.740] | 0.689 (1571) [0.668, 0.709] | 0.701 (3060) [0.685, 0.717] | 0.687 (1473) [0.664, 0.709] | 0.723 (47) | 0.121 | flat +0.037 (noise 0.040) |
| overall | 0.506 (22106) | 0.506 (155050) [0.504, 0.508] | 0.504 (663295) [0.503, 0.506] | 0.503 (1302230) [0.502, 0.504] | 0.504 (618949) [0.503, 0.506] | 0.507 (16019) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08118, 0.1248] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5253, 'levels': [{'threshold': 0.08118, 'calls_per_day': 142.7, 'win_rate': 0.6006}, {'threshold': 0.1248, 'calls_per_day': 36.2, 'win_rate': 0.6118}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 39889, 'rate': 0.53}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15229 | 0.338 | 0.523 (14997) | 0.577 (2035) | 0.753 (2652) |
| volatility: normal | 15228 | 0.366 | 0.532 (15157) | 0.614 (1436) | 0.750 (2255) |
| volatility: wild | 15228 | 0.381 | 0.525 (15185) | 0.630 (752) | 0.769 (2061) |
| session: Asia 00-08 | 15360 | 0.360 | 0.532 (15259) | 0.602 (1492) | 0.763 (2306) |
| session: Europe 08-13 | 9600 | 0.356 | 0.530 (9510) | 0.594 (1059) | 0.750 (1577) |
| session: US 13-21 | 15145 | 0.370 | 0.524 (15044) | 0.596 (1094) | 0.758 (2227) |
| session: late 21-24 | 5580 | 0.352 | 0.514 (5526) | 0.609 (578) | 0.749 (858) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.305 | 0.291 | 0.223 | 0.223 | 0.473 | 0.236 | 0.373 | 1.096 |
| 6h | 360 | 0.336 | 0.330 | 0.248 | 0.267 | 0.569 | 0.263 | 0.410 | 1.297 |
| 24h | 1440 | 0.344 | 0.338 | 0.261 | 0.277 | 0.539 | 0.261 | 0.427 | 1.091 |
| 7d | 10080 | 0.365 | 0.358 | 0.282 | 0.312 | 0.527 | 0.262 | 0.468 | 1.256 |
| 30d | 43200 | 0.361 | 0.354 | 0.276 | 0.305 | 0.528 | 0.260 | 0.462 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.305 / 0.473 / 0.867; 2: 0.275 / 0.436 / 0.833; 3: 0.293 / 0.491 / 0.817; 4: 0.317 / 0.618 / 0.767; 5: 0.318 / 0.564 / 0.867; 6: 0.309 / 0.509 / 0.867; 7: 0.303 / 0.473 / 0.867; 8: 0.304 / 0.491 / 0.900; 9: 0.322 / 0.564 / 0.917; 10: 0.305 / 0.545 / 0.933; 11: 0.329 / 0.636 / 0.933; 12: 0.291 / 0.527 / 0.933; 13: 0.274 / 0.418 / 0.883; 14: 0.289 / 0.491 / 0.950; 15: 0.282 / 0.509 / 0.967
- 6h: 1: 0.336 / 0.569 / 0.881; 2: 0.307 / 0.469 / 0.889; 3: 0.325 / 0.546 / 0.914; 4: 0.305 / 0.474 / 0.875; 5: 0.329 / 0.560 / 0.889; 6: 0.313 / 0.503 / 0.889; 7: 0.295 / 0.457 / 0.889; 8: 0.317 / 0.537 / 0.894; 9: 0.322 / 0.543 / 0.903; 10: 0.305 / 0.474 / 0.894; 11: 0.299 / 0.486 / 0.897; 12: 0.306 / 0.514 / 0.886; 13: 0.312 / 0.514 / 0.869; 14: 0.304 / 0.489 / 0.883; 15: 0.303 / 0.497 / 0.881
- 24h: 1: 0.344 / 0.539 / 0.887; 2: 0.331 / 0.497 / 0.905; 3: 0.333 / 0.499 / 0.901; 4: 0.329 / 0.504 / 0.892; 5: 0.332 / 0.523 / 0.898; 6: 0.323 / 0.487 / 0.908; 7: 0.325 / 0.485 / 0.904; 8: 0.330 / 0.526 / 0.909; 9: 0.335 / 0.521 / 0.910; 10: 0.327 / 0.488 / 0.908; 11: 0.323 / 0.484 / 0.904; 12: 0.329 / 0.500 / 0.911; 13: 0.329 / 0.506 / 0.910; 14: 0.325 / 0.483 / 0.907; 15: 0.332 / 0.518 / 0.910
- 7d: 1: 0.365 / 0.527 / 0.896; 2: 0.353 / 0.492 / 0.900; 3: 0.356 / 0.507 / 0.901; 4: 0.354 / 0.505 / 0.901; 5: 0.352 / 0.506 / 0.901; 6: 0.350 / 0.504 / 0.900; 7: 0.353 / 0.501 / 0.900; 8: 0.351 / 0.507 / 0.901; 9: 0.352 / 0.503 / 0.901; 10: 0.351 / 0.502 / 0.901; 11: 0.348 / 0.500 / 0.901; 12: 0.351 / 0.503 / 0.901; 13: 0.349 / 0.501 / 0.901; 14: 0.350 / 0.503 / 0.902; 15: 0.349 / 0.497 / 0.901
- 30d: 1: 0.361 / 0.528 / 0.898; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.347 / 0.498 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.502 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.344 / 0.497 / 0.900; 12: 0.346 / 0.503 / 0.900; 13: 0.345 / 0.501 / 0.900; 14: 0.345 / 0.500 / 0.900; 15: 0.345 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.127 (body 0.087, range 0.166); 'price stays where it was' would score 0.163; colour right 0.564; typical miss of the close 3.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.137 (body 0.100, range 0.174); 'price stays where it was' would score 0.140; colour right 0.534; typical miss of the close 4.0 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.114 (body 0.078, range 0.150); 'price stays where it was' would score 0.124; colour right 0.522; typical miss of the close 6.0 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.127 (body 0.086, range 0.169); 'price stays where it was' would score 0.133; colour right 0.503; typical miss of the close 8.7 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.0; 2: 0.199 / 4.6; 3: 0.168 / 6.1; 4: 0.132 / 6.5; 5: 0.125 / 7.2; 6: 0.113 / 7.6; 7: 0.111 / 8.0; 8: 0.098 / 8.6; 9: 0.089 / 8.6; 10: 0.088 / 9.2; 11: 0.086 / 9.6; 12: 0.076 / 10.0; 13: 0.068 / 10.1; 14: 0.070 / 10.5; 15: 0.062 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 128959, probability skill vs chance 0.2249, widened contest next: False
  - now: threshold 0.8339, hit rate recent 0.9204 / long run 0.9408
    - 6h: 22 calls (89 a day), hit rate 0.864, chance 0.307, naive rule 0.472, lift 2.81x
    - 24h: 71 calls (71 a day), hit rate 0.915, chance 0.302, naive rule 0.508, lift 3.03x
    - 7d: 411 calls (59 a day), hit rate 0.944, chance 0.293, naive rule 0.496, lift 3.22x
    - 30d: 1730 calls (58 a day), hit rate 0.935, chance 0.294, naive rule 0.494, lift 3.18x
  - next: threshold 0.5294, hit rate recent 0.5637 / long run 0.5841
    - 6h: 39 calls (158 a day), hit rate 0.564, chance 0.307, lift 1.84x
    - 24h: 159 calls (160 a day), hit rate 0.579, chance 0.302, lift 1.91x
    - 7d: 799 calls (114 a day), hit rate 0.582, chance 0.293, lift 1.99x
    - 30d: 2990 calls (100 a day), hit rate 0.581, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.497; 0.35: 535, 0.522; 0.40: 474, 0.580; 0.45: 406, 0.650; 0.50: 355, 0.700; 0.55: 310, 0.742; 0.60: 262, 0.788; 0.65: 219, 0.813; 0.70: 173, 0.844; 0.75: 136, 0.878; 0.80: 92, 0.913; 0.85: 47, 0.948; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.427; 0.35: 502, 0.464; 0.40: 406, 0.496; 0.45: 309, 0.532; 0.50: 200, 0.569; 0.55: 89, 0.570; 0.60: 13, 0.645; 0.65: 1, 0.630
- **K=5**: model 1792540800, labels learned 128957, probability skill vs chance 0.2211, widened contest next: True
  - now: threshold 0.6783, hit rate recent 0.7704 / long run 0.819
    - 6h: 20 calls (82 a day), hit rate 0.600, chance 0.201, naive rule 0.382, lift 2.98x
    - 24h: 58 calls (58 a day), hit rate 0.793, chance 0.195, naive rule 0.421, lift 4.07x
    - 7d: 409 calls (58 a day), hit rate 0.822, chance 0.186, naive rule 0.408, lift 4.41x
    - 30d: 1624 calls (54 a day), hit rate 0.821, chance 0.188, naive rule 0.404, lift 4.37x
  - next: threshold 0.4553, hit rate recent 0.5057 / long run 0.4951
    - 6h: 18 calls (73 a day), hit rate 0.389, chance 0.201, lift 1.93x
    - 24h: 67 calls (67 a day), hit rate 0.522, chance 0.195, lift 2.68x
    - 7d: 541 calls (77 a day), hit rate 0.505, chance 0.186, lift 2.71x
    - 30d: 2971 calls (99 a day), hit rate 0.469, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.492; 0.40: 278, 0.566; 0.45: 227, 0.620; 0.50: 180, 0.668; 0.55: 141, 0.706; 0.60: 108, 0.750; 0.65: 76, 0.788; 0.70: 50, 0.824; 0.75: 29, 0.868; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.388; 0.35: 255, 0.420; 0.40: 160, 0.456; 0.45: 68, 0.476; 0.50: 13, 0.492; 0.55: 1, 0.472
- **K=8**: model 1793059200, labels learned 128954, probability skill vs chance 0.2108, widened contest next: False
  - now: threshold 0.5645, hit rate recent 0.7086 / long run 0.6909
    - 6h: 20 calls (82 a day), hit rate 0.650, chance 0.130, naive rule 0.317, lift 5.00x
    - 24h: 57 calls (57 a day), hit rate 0.737, chance 0.134, naive rule 0.374, lift 5.50x
    - 7d: 380 calls (54 a day), hit rate 0.703, chance 0.122, naive rule 0.345, lift 5.74x
    - 30d: 1580 calls (53 a day), hit rate 0.690, chance 0.121, naive rule 0.334, lift 5.69x
  - next: threshold 0.352, hit rate recent 0.4609 / long run 0.4015
    - 6h: 23 calls (95 a day), hit rate 0.478, chance 0.130, lift 3.68x
    - 24h: 105 calls (106 a day), hit rate 0.467, chance 0.134, lift 3.48x
    - 7d: 718 calls (103 a day), hit rate 0.404, chance 0.122, lift 3.30x
    - 30d: 2841 calls (95 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 189, 0.500; 0.40: 147, 0.547; 0.45: 112, 0.595; 0.50: 84, 0.637; 0.55: 61, 0.677; 0.60: 41, 0.712; 0.65: 23, 0.782; 0.70: 11, 0.812; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.358; 0.35: 92, 0.385; 0.40: 29, 0.406; 0.45: 6, 0.429; 0.50: 1, 0.630
- **K=13**: model 1793059200, labels learned 128949, probability skill vs chance 0.192, widened contest next: False
  - now: threshold 0.4124, hit rate recent 0.6013 / long run 0.5673
    - 6h: 20 calls (83 a day), hit rate 0.500, chance 0.093, naive rule 0.288, lift 5.39x
    - 24h: 61 calls (62 a day), hit rate 0.672, chance 0.086, naive rule 0.324, lift 7.79x
    - 7d: 428 calls (61 a day), hit rate 0.579, chance 0.079, naive rule 0.289, lift 7.38x
    - 30d: 1656 calls (55 a day), hit rate 0.568, chance 0.077, naive rule 0.278, lift 7.34x
  - next: threshold 0.2929, hit rate recent 0.3228 / long run 0.3157
    - 6h: 18 calls (75 a day), hit rate 0.278, chance 0.093, lift 2.99x
    - 24h: 56 calls (57 a day), hit rate 0.339, chance 0.086, lift 3.93x
    - 7d: 392 calls (56 a day), hit rate 0.332, chance 0.079, lift 4.22x
    - 30d: 1973 calls (66 a day), hit rate 0.315, chance 0.077, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.443; 0.35: 91, 0.496; 0.40: 64, 0.552; 0.45: 43, 0.597; 0.50: 28, 0.653; 0.55: 17, 0.692; 0.60: 9, 0.734; 0.65: 2, 0.726; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.350; 0.40: 3, 0.451; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.328 | 3.33% | 0.867 | 0.467 | 0.260 | 0.436 | 0.273 |
| 6h | 7.852 | 7.43% | 0.883 | 0.481 | 0.249 | 0.540 | 0.371 |
| 24h | 10.083 | 11.53% | 0.899 | 0.515 | 0.249 | 0.525 | 0.700 |
| 7d | 15.944 | 4.92% | 0.899 | 0.501 | 0.250 | 0.503 | 0.740 |
| 30d | 14.120 | 4.47% | 0.900 | 0.501 | 0.251 | 0.497 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.616 | 8.365 | 8.519 | 8.360 | 8.743 | 8.990 | 8.284 | 8.276 | 8.282 | 8.328 |
| 6h | 8.482 | 7.926 | 8.000 | 7.890 | 8.135 | 8.242 | 7.819 | 7.860 | 7.846 | 7.852 |
| 24h | 11.398 | 10.141 | 10.287 | 10.111 | 10.328 | 10.451 | 10.079 | 10.063 | 10.073 | 10.083 |
| 7d | 16.769 | 16.127 | 16.067 | 15.980 | 16.277 | 16.213 | 15.928 | 15.905 | 15.915 | 15.944 |
| 30d | 14.780 | 14.272 | 14.216 | 14.148 | 14.387 | 14.329 | 14.115 | 14.093 | 14.095 | 14.120 |

## Next candle

- candle starting 2026-10-31 17:25 UTC, last close 2248.73
- P(up) 0.5379, return quantiles (bp): {'05': -5.073, '10': -3.727, '25': -1.51, '40': -0.332, '50': 0.193, '60': 0.677, '75': 1.514, '90': 3.325, '95': 4.78}
- changepoint probability 0.0718, regime age 17.8 min
- agent weights: empirical 0.003, ewma 0.139, garch 0.046, har 0.202, bocpd 0.029, hmm 0.008, online_qr 0.306, lgbm 0.268

## Learning log

- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- 2026-10-31 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.9037}, "hmm": {"sd_bp": [3.53, 7.0, 20.69], "stay": [0.977, 0.956, 0.901]}}
- HMM volatility states (sd, bp per minute): [3.53, 7.0, 20.69], current probabilities: [0.969, 0.03, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-31 17:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.41, 'l_abs': 0.58, 'l_hi': 0.707, 'l_lo': 0.69, 'b05': 0.644, 'b25': 0.627, 'b75': 0.585, 'b95': 0.644}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.505, 1.512, 2.053, 2.209, 2.627, 2.959, 2.985, 3.237, 3.285, 3.892, 3.914, 4.164, 4.507, 4.963]}
- calibration offsets (in sigma): {'05': 0.022, '10': 0.004, '25': 0.08, '40': 0.076, '50': 0.03, '60': 0.004, '75': -0.07, '90': -0.054, '95': -0.042}
