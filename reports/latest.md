# ETH-USD 60s candle generator - report

- generated: 2026-10-13 23:05 UTC
- last closed candle: 2026-10-13 23:05 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k8_now 0.666 in the last 7 days, -0.074 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.495 (671) [0.453, 0.537] | 0.509 (2874) [0.488, 0.531] | 0.510 (3930) [0.494, 0.526] | 0.506 (958) [0.470, 0.545] | 0.533 (92) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.535 (818) | 0.537 (5459) [0.532, 0.543] | 0.512 (23268) [0.504, 0.520] | 0.507 (31858) [0.501, 0.514] | 0.543 (7620) [0.536, 0.549] | 0.531 (744) | 0.500 | flat +0.022 (noise 0.014) |
| colour_confident | 0.574 (61) | 0.589 (1034) [0.561, 0.625] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 0.633 (60) | 0.500 | flat -0.053 (noise 0.033) |
| colour_next | 0.523 (1434) | 0.523 (9964) [0.518, 0.527] | 0.510 (42853) [0.504, 0.515] | 0.507 (58564) [0.503, 0.511] | 0.528 (14215) [0.522, 0.535] | 0.518 (1379) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.502 (20076) | 0.498 (139496) [0.496, 0.500] | 0.501 (599942) [0.500, 0.502] | 0.500 (819896) [0.499, 0.501] | 0.499 (199010) [0.497, 0.502] | 0.504 (19306) | 0.500 | flat -0.004 (noise 0.003) |
| colour_strong | 0.667 (15) | 0.652 (282) [0.598, 0.712] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 0.714 (7) | 0.500 | flat -0.017 (noise 0.051) |
| reversal_k13_next | 0.288 (73) | 0.329 (492) [0.312, 0.347] | 0.315 (2092) [0.300, 0.330] | 0.307 (2858) [0.294, 0.321] | 0.328 (753) [0.314, 0.342] | 0.282 (71) | 0.077 | flat +0.038 (noise 0.028) |
| reversal_k13_now | 0.527 (55) | 0.568 (373) [0.540, 0.601] | 0.586 (1493) [0.565, 0.608] | 0.582 (2023) [0.565, 0.601] | 0.586 (551) [0.555, 0.622] | 0.683 (41) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.581 (74) | 0.585 (544) [0.553, 0.613] | 0.588 (2388) [0.573, 0.603] | 0.586 (3301) [0.574, 0.599] | 0.582 (861) [0.559, 0.606] | 0.540 (163) | 0.294 | flat -0.005 (noise 0.029) |
| reversal_k3_now | 0.914 (58) | 0.917 (434) [0.910, 0.926] | 0.939 (1726) [0.931, 0.947] | 0.937 (2366) [0.929, 0.944] | 0.922 (603) [0.915, 0.930] | 0.977 (43) | 0.293 | flat -0.023 (noise 0.018) |
| reversal_k5_next | 0.483 (87) | 0.467 (469) [0.439, 0.491] | 0.483 (2085) [0.466, 0.502] | 0.484 (2807) [0.469, 0.500] | 0.459 (817) [0.435, 0.487] | 0.480 (102) | 0.188 | flat +0.001 (noise 0.030) |
| reversal_k5_now | 0.774 (53) | 0.804 (377) [0.777, 0.832] | 0.834 (1588) [0.819, 0.851] | 0.834 (2162) [0.820, 0.847] | 0.822 (551) [0.796, 0.848] | 0.800 (45) | 0.188 | flat -0.050 (noise 0.027) |
| reversal_k8_next | 0.430 (79) | 0.389 (615) [0.365, 0.415] | 0.409 (2131) [0.393, 0.426] | 0.395 (2959) [0.382, 0.410] | 0.394 (853) [0.373, 0.417] | 0.423 (78) | 0.122 | flat -0.011 (noise 0.030) |
| reversal_k8_now | 0.643 (56) | 0.666 (413) [0.636, 0.698] | 0.718 (1592) [0.698, 0.739] | 0.710 (2171) [0.692, 0.727] | 0.699 (584) [0.663, 0.733] | 0.689 (45) | 0.122 | down -0.074 (noise 0.033) |
| overall | 0.505 (22141) | 0.502 (153848) [0.499, 0.504] | 0.504 (660764) [0.503, 0.505] | 0.503 (903037) [0.502, 0.504] | 0.503 (219756) [0.500, 0.506] | 0.507 (21365) | - | flat -0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07784, 0.1203] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5238, 'levels': [{'threshold': 0.07784, 'calls_per_day': 140.8, 'win_rate': 0.6044}, {'threshold': 0.1203, 'calls_per_day': 35.3, 'win_rate': 0.66}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 14458, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15342 | 0.331 | 0.519 (15065) | 0.597 (1170) | 0.772 (2518) |
| volatility: normal | 15341 | 0.359 | 0.509 (15273) | 0.614 (267) | 0.782 (2168) |
| volatility: wild | 15342 | 0.374 | 0.501 (15297) | 0.692 (104) | 0.771 (2148) |
| session: Asia 00-08 | 15360 | 0.352 | 0.514 (15243) | 0.606 (548) | 0.774 (2234) |
| session: Europe 08-13 | 9600 | 0.348 | 0.507 (9509) | 0.589 (377) | 0.779 (1487) |
| session: US 13-21 | 15360 | 0.364 | 0.507 (15250) | 0.588 (388) | 0.780 (2265) |
| session: late 21-24 | 5705 | 0.348 | 0.511 (5633) | 0.667 (228) | 0.757 (848) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.324 | 0.339 | 0.279 | 0.279 | 0.433 | 0.186 | 0.461 | 1.348 |
| 6h | 360 | 0.364 | 0.352 | 0.290 | 0.310 | 0.496 | 0.251 | 0.477 | 1.106 |
| 24h | 1440 | 0.370 | 0.366 | 0.290 | 0.319 | 0.515 | 0.256 | 0.485 | 1.230 |
| 7d | 10080 | 0.355 | 0.348 | 0.273 | 0.301 | 0.525 | 0.257 | 0.453 | 1.257 |
| 30d | 43200 | 0.357 | 0.355 | 0.279 | 0.308 | 0.510 | 0.249 | 0.465 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.324 / 0.433 / 0.867; 2: 0.332 / 0.483 / 0.867; 3: 0.350 / 0.467 / 0.867; 4: 0.366 / 0.517 / 0.917; 5: 0.337 / 0.517 / 0.950; 6: 0.355 / 0.500 / 0.917; 7: 0.337 / 0.500 / 0.917; 8: 0.346 / 0.467 / 0.933; 9: 0.365 / 0.617 / 0.933; 10: 0.347 / 0.567 / 0.933; 11: 0.344 / 0.483 / 0.900; 12: 0.328 / 0.450 / 0.917; 13: 0.327 / 0.400 / 0.933; 14: 0.365 / 0.583 / 0.917; 15: 0.342 / 0.433 / 0.950
- 6h: 1: 0.364 / 0.496 / 0.911; 2: 0.348 / 0.482 / 0.886; 3: 0.361 / 0.496 / 0.914; 4: 0.357 / 0.482 / 0.933; 5: 0.368 / 0.535 / 0.931; 6: 0.360 / 0.507 / 0.917; 7: 0.361 / 0.487 / 0.919; 8: 0.362 / 0.524 / 0.914; 9: 0.353 / 0.482 / 0.906; 10: 0.368 / 0.549 / 0.900; 11: 0.343 / 0.476 / 0.906; 12: 0.358 / 0.490 / 0.897; 13: 0.363 / 0.518 / 0.908; 14: 0.359 / 0.485 / 0.914; 15: 0.357 / 0.479 / 0.928
- 24h: 1: 0.370 / 0.515 / 0.917; 2: 0.356 / 0.487 / 0.907; 3: 0.370 / 0.524 / 0.916; 4: 0.363 / 0.499 / 0.912; 5: 0.365 / 0.505 / 0.923; 6: 0.368 / 0.521 / 0.923; 7: 0.365 / 0.499 / 0.932; 8: 0.364 / 0.517 / 0.930; 9: 0.357 / 0.492 / 0.926; 10: 0.362 / 0.508 / 0.926; 11: 0.353 / 0.487 / 0.926; 12: 0.364 / 0.505 / 0.928; 13: 0.362 / 0.512 / 0.933; 14: 0.359 / 0.497 / 0.930; 15: 0.365 / 0.507 / 0.930
- 7d: 1: 0.355 / 0.525 / 0.900; 2: 0.344 / 0.494 / 0.899; 3: 0.348 / 0.513 / 0.899; 4: 0.343 / 0.497 / 0.899; 5: 0.345 / 0.506 / 0.900; 6: 0.342 / 0.497 / 0.899; 7: 0.342 / 0.499 / 0.900; 8: 0.342 / 0.500 / 0.900; 9: 0.339 / 0.491 / 0.900; 10: 0.343 / 0.504 / 0.899; 11: 0.339 / 0.491 / 0.900; 12: 0.341 / 0.500 / 0.899; 13: 0.341 / 0.499 / 0.899; 14: 0.340 / 0.502 / 0.899; 15: 0.341 / 0.497 / 0.899
- 30d: 1: 0.357 / 0.510 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.511 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.504 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.121 (body 0.091, range 0.151); 'price stays where it was' would score 0.156; colour right 0.483; typical miss of the close 6.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.146 (body 0.098, range 0.193); 'price stays where it was' would score 0.134; colour right 0.513; typical miss of the close 5.5 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.119; colour right 0.490; typical miss of the close 10.6 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.120 (body 0.082, range 0.158); 'price stays where it was' would score 0.124; colour right 0.495; typical miss of the close 7.1 bp; chain ended on the right side 0.492 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.124; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.509 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.198 / 4.4; 3: 0.165 / 6.0; 4: 0.133 / 6.7; 5: 0.119 / 7.4; 6: 0.109 / 7.9; 7: 0.101 / 8.4; 8: 0.094 / 8.7; 9: 0.087 / 8.8; 10: 0.082 / 9.6; 11: 0.077 / 10.3; 12: 0.074 / 10.8; 13: 0.062 / 11.0; 14: 0.063 / 11.2; 15: 0.060 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 103379, probability skill vs chance 0.2323, widened contest next: True
  - now: threshold 0.8424, hit rate recent 0.9385 / long run 0.9311
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.313, naive rule 0.504, lift 2.88x
    - 24h: 44 calls (44 a day), hit rate 0.977, chance 0.291, naive rule 0.484, lift 3.36x
    - 7d: 420 calls (60 a day), hit rate 0.926, chance 0.295, naive rule 0.497, lift 3.14x
    - 30d: 1717 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.482, lift 3.23x
  - next: threshold 0.5558, hit rate recent 0.54 / long run 0.5759
    - 6h: 28 calls (114 a day), hit rate 0.536, chance 0.313, lift 1.71x
    - 24h: 165 calls (166 a day), hit rate 0.545, chance 0.291, lift 1.87x
    - 7d: 665 calls (95 a day), hit rate 0.567, chance 0.295, lift 1.92x
    - 30d: 2477 calls (83 a day), hit rate 0.585, chance 0.290, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.491; 0.35: 539, 0.514; 0.40: 484, 0.561; 0.45: 416, 0.629; 0.50: 363, 0.683; 0.55: 318, 0.725; 0.60: 271, 0.769; 0.65: 224, 0.801; 0.70: 180, 0.833; 0.75: 139, 0.871; 0.80: 96, 0.913; 0.85: 48, 0.949; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.460; 0.40: 411, 0.489; 0.45: 316, 0.523; 0.50: 205, 0.558; 0.55: 91, 0.584; 0.60: 14, 0.603; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 103377, probability skill vs chance 0.2199, widened contest next: True
  - now: threshold 0.7053, hit rate recent 0.7905 / long run 0.8257
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.170, naive rule 0.349, lift 3.92x
    - 24h: 46 calls (46 a day), hit rate 0.804, chance 0.179, naive rule 0.383, lift 4.48x
    - 7d: 369 calls (53 a day), hit rate 0.810, chance 0.189, naive rule 0.403, lift 4.29x
    - 30d: 1586 calls (53 a day), hit rate 0.832, chance 0.187, naive rule 0.391, lift 4.46x
  - next: threshold 0.4422, hit rate recent 0.4573 / long run 0.4751
    - 6h: 19 calls (78 a day), hit rate 0.368, chance 0.170, lift 2.17x
    - 24h: 103 calls (104 a day), hit rate 0.485, chance 0.179, lift 2.71x
    - 7d: 525 calls (75 a day), hit rate 0.469, chance 0.189, lift 2.48x
    - 30d: 2109 calls (70 a day), hit rate 0.484, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 425, 0.416; 0.35: 357, 0.477; 0.40: 288, 0.548; 0.45: 236, 0.604; 0.50: 184, 0.658; 0.55: 139, 0.706; 0.60: 109, 0.747; 0.65: 83, 0.791; 0.70: 61, 0.824; 0.75: 33, 0.867; 0.80: 10, 0.896
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.389; 0.35: 251, 0.426; 0.40: 162, 0.454; 0.45: 80, 0.474; 0.50: 19, 0.513; 0.55: 2, 0.577
- **K=8**: model 1791849600, labels learned 103374, probability skill vs chance 0.2133, widened contest next: True
  - now: threshold 0.5812, hit rate recent 0.6715 / long run 0.7017
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.133, naive rule 0.331, lift 4.39x
    - 24h: 46 calls (46 a day), hit rate 0.674, chance 0.122, naive rule 0.330, lift 5.51x
    - 7d: 396 calls (57 a day), hit rate 0.672, chance 0.123, naive rule 0.343, lift 5.46x
    - 30d: 1590 calls (53 a day), hit rate 0.718, chance 0.122, naive rule 0.329, lift 5.88x
  - next: threshold 0.3717, hit rate recent 0.4132 / long run 0.4009
    - 6h: 12 calls (49 a day), hit rate 0.417, chance 0.133, lift 3.14x
    - 24h: 80 calls (81 a day), hit rate 0.425, chance 0.122, lift 3.47x
    - 7d: 607 calls (87 a day), hit rate 0.390, chance 0.123, lift 3.17x
    - 30d: 2115 calls (71 a day), hit rate 0.411, chance 0.122, lift 3.37x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 264, 0.411; 0.35: 199, 0.486; 0.40: 153, 0.547; 0.45: 120, 0.591; 0.50: 92, 0.635; 0.55: 66, 0.688; 0.60: 45, 0.730; 0.65: 24, 0.779; 0.70: 9, 0.835; 0.75: 1, 0.789
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 181, 0.353; 0.35: 110, 0.392; 0.40: 46, 0.424; 0.45: 10, 0.462; 0.50: 1, 0.378
- **K=13**: model 1791849600, labels learned 103369, probability skill vs chance 0.1938, widened contest next: False
  - now: threshold 0.4361, hit rate recent 0.6142 / long run 0.5887
    - 6h: 9 calls (38 a day), hit rate 0.556, chance 0.087, naive rule 0.287, lift 6.39x
    - 24h: 43 calls (43 a day), hit rate 0.674, chance 0.075, naive rule 0.278, lift 8.94x
    - 7d: 354 calls (51 a day), hit rate 0.593, chance 0.079, naive rule 0.287, lift 7.46x
    - 30d: 1487 calls (50 a day), hit rate 0.593, chance 0.078, naive rule 0.273, lift 7.61x
  - next: threshold 0.2989, hit rate recent 0.2956 / long run 0.3146
    - 6h: 11 calls (46 a day), hit rate 0.273, chance 0.087, lift 3.14x
    - 24h: 74 calls (75 a day), hit rate 0.284, chance 0.075, lift 3.76x
    - 7d: 496 calls (71 a day), hit rate 0.327, chance 0.079, lift 4.11x
    - 30d: 2092 calls (70 a day), hit rate 0.316, chance 0.078, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 86, 0.514; 0.40: 61, 0.568; 0.45: 42, 0.623; 0.50: 26, 0.653; 0.55: 14, 0.715; 0.60: 4, 0.782; 0.65: 1, 0.900
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.331; 0.35: 14, 0.366; 0.40: 2, 0.408; 0.45: 0, 0.300

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.942 | 7.14% | 0.833 | 0.550 | 0.251 | 0.417 | 0.316 |
| 6h | 10.998 | 5.93% | 0.897 | 0.497 | 0.251 | 0.462 | 0.444 |
| 24h | 17.332 | 3.16% | 0.901 | 0.503 | 0.250 | 0.497 | 0.617 |
| 7d | 12.933 | 4.41% | 0.899 | 0.499 | 0.251 | 0.493 | 0.659 |
| 30d | 14.028 | 4.06% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.707 | 9.979 | 10.033 | 9.992 | 9.942 | 10.163 | 9.967 | 9.860 | 9.919 | 9.942 |
| 6h | 11.692 | 11.037 | 11.030 | 11.056 | 11.151 | 11.014 | 10.985 | 10.946 | 10.975 | 10.998 |
| 24h | 17.898 | 17.479 | 17.479 | 17.356 | 17.760 | 17.482 | 17.345 | 17.276 | 17.295 | 17.332 |
| 7d | 13.529 | 13.058 | 13.015 | 12.972 | 13.179 | 13.129 | 12.937 | 12.899 | 12.910 | 12.933 |
| 30d | 14.623 | 14.152 | 14.115 | 14.056 | 14.291 | 14.227 | 14.027 | 14.000 | 14.002 | 14.028 |

## Next candle

- candle starting 2026-10-13 23:05 UTC, last close 2500.66
- P(up) 0.5083, return quantiles (bp): {'05': -8.114, '10': -5.724, '25': -2.961, '40': -1.063, '50': 0.095, '60': 1.052, '75': 3.044, '90': 5.854, '95': 7.691}
- changepoint probability 0.2714, regime age 170.4 min
- agent weights: empirical 0.005, ewma 0.102, garch 0.088, har 0.172, bocpd 0.025, hmm 0.064, online_qr 0.244, lgbm 0.301

## Learning log

- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- HMM volatility states (sd, bp per minute): [2.04, 4.71, 13.13], current probabilities: [0.031, 0.92, 0.049]
- live generator: {'versions': 60, 'latest_effective': '2026-10-13 23:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.565, 'l_abs': 0.769, 'l_hi': 0.774, 'l_lo': 0.718, 'b05': 0.766, 'b25': 0.765, 'b75': 0.74, 'b95': 0.724}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.2, 1.8], [1.3, 1.6], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.505, 1.705, 2.012, 2.123, 2.194, 2.149, 2.302, 2.598, 2.584, 2.77, 2.958, 2.964, 3.208, 3.133]}
- calibration offsets (in sigma): {'05': 0.022, '10': -0.006, '25': -0.06, '40': -0.044, '50': -0.02, '60': -0.046, '75': -0.03, '90': -0.034, '95': -0.032}
