# ETH-USD 60s candle generator - report

- generated: 2026-10-13 18:32 UTC
- last closed candle: 2026-10-13 18:32 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k8_now 0.666 in the last 7 days, -0.074 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.495 (671) [0.453, 0.537] | 0.509 (2874) [0.488, 0.531] | 0.510 (3930) [0.494, 0.526] | 0.506 (958) [0.470, 0.545] | 0.500 (74) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.535 (818) | 0.537 (5459) [0.532, 0.543] | 0.512 (23268) [0.504, 0.520] | 0.507 (31858) [0.501, 0.514] | 0.543 (7620) [0.536, 0.549] | 0.527 (596) | 0.500 | flat +0.022 (noise 0.014) |
| colour_confident | 0.574 (61) | 0.589 (1034) [0.561, 0.625] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 0.625 (40) | 0.500 | flat -0.053 (noise 0.033) |
| colour_next | 0.523 (1434) | 0.523 (9964) [0.518, 0.527] | 0.510 (42853) [0.504, 0.515] | 0.507 (58564) [0.503, 0.511] | 0.528 (14215) [0.522, 0.535] | 0.518 (1108) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.502 (20076) | 0.498 (139496) [0.496, 0.500] | 0.501 (599942) [0.500, 0.502] | 0.500 (819896) [0.499, 0.501] | 0.499 (199010) [0.497, 0.502] | 0.507 (15512) | 0.500 | flat -0.004 (noise 0.003) |
| colour_strong | 0.667 (15) | 0.652 (282) [0.598, 0.712] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 0.800 (5) | 0.500 | flat -0.017 (noise 0.051) |
| reversal_k13_next | 0.288 (73) | 0.329 (492) [0.312, 0.347] | 0.315 (2092) [0.300, 0.330] | 0.307 (2858) [0.294, 0.321] | 0.328 (753) [0.314, 0.342] | 0.302 (63) | 0.077 | flat +0.038 (noise 0.028) |
| reversal_k13_now | 0.527 (55) | 0.568 (373) [0.540, 0.601] | 0.586 (1493) [0.565, 0.608] | 0.582 (2023) [0.565, 0.601] | 0.586 (551) [0.555, 0.622] | 0.727 (33) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.581 (74) | 0.585 (544) [0.553, 0.613] | 0.588 (2388) [0.573, 0.603] | 0.586 (3301) [0.574, 0.599] | 0.582 (861) [0.559, 0.606] | 0.540 (148) | 0.294 | flat -0.005 (noise 0.029) |
| reversal_k3_now | 0.914 (58) | 0.917 (434) [0.910, 0.926] | 0.939 (1726) [0.931, 0.947] | 0.937 (2366) [0.929, 0.944] | 0.922 (603) [0.915, 0.930] | 1.000 (34) | 0.293 | flat -0.023 (noise 0.018) |
| reversal_k5_next | 0.483 (87) | 0.467 (469) [0.439, 0.491] | 0.483 (2085) [0.466, 0.502] | 0.484 (2807) [0.469, 0.500] | 0.459 (817) [0.435, 0.487] | 0.500 (90) | 0.188 | flat +0.001 (noise 0.030) |
| reversal_k5_now | 0.774 (53) | 0.804 (377) [0.777, 0.832] | 0.834 (1588) [0.819, 0.851] | 0.834 (2162) [0.820, 0.847] | 0.822 (551) [0.796, 0.848] | 0.816 (38) | 0.188 | flat -0.050 (noise 0.027) |
| reversal_k8_next | 0.430 (79) | 0.389 (615) [0.365, 0.415] | 0.409 (2131) [0.393, 0.426] | 0.395 (2959) [0.382, 0.410] | 0.394 (853) [0.373, 0.417] | 0.435 (69) | 0.122 | flat -0.011 (noise 0.030) |
| reversal_k8_now | 0.643 (56) | 0.666 (413) [0.636, 0.698] | 0.718 (1592) [0.698, 0.739] | 0.710 (2171) [0.692, 0.727] | 0.699 (584) [0.663, 0.733] | 0.714 (35) | 0.122 | down -0.074 (noise 0.033) |
| overall | 0.505 (22141) | 0.502 (153848) [0.499, 0.504] | 0.504 (660764) [0.503, 0.505] | 0.503 (903037) [0.502, 0.504] | 0.503 (219756) [0.500, 0.506] | 0.509 (17204) | - | flat -0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07784, 0.1203] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5238, 'levels': [{'threshold': 0.07784, 'calls_per_day': 140.8, 'win_rate': 0.6044}, {'threshold': 0.1203, 'calls_per_day': 35.3, 'win_rate': 0.66}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 14187, 'rate': 0.5291}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15251 | 0.331 | 0.520 (14976) | 0.595 (1154) | 0.773 (2504) |
| volatility: normal | 15250 | 0.359 | 0.509 (15181) | 0.620 (263) | 0.781 (2160) |
| volatility: wild | 15251 | 0.374 | 0.501 (15207) | 0.692 (104) | 0.772 (2136) |
| session: Asia 00-08 | 15360 | 0.352 | 0.514 (15243) | 0.606 (548) | 0.774 (2234) |
| session: Europe 08-13 | 9600 | 0.348 | 0.507 (9509) | 0.589 (377) | 0.779 (1487) |
| session: US 13-21 | 15212 | 0.364 | 0.507 (15102) | 0.590 (385) | 0.781 (2255) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5510) | 0.663 (211) | 0.757 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.366 | 0.382 | 0.309 | 0.309 | 0.458 | 0.248 | 0.485 | 0.934 |
| 6h | 360 | 0.382 | 0.385 | 0.296 | 0.342 | 0.514 | 0.258 | 0.506 | 1.257 |
| 24h | 1440 | 0.368 | 0.368 | 0.292 | 0.318 | 0.507 | 0.252 | 0.483 | 1.225 |
| 7d | 10080 | 0.354 | 0.348 | 0.273 | 0.301 | 0.524 | 0.257 | 0.452 | 1.260 |
| 30d | 43200 | 0.357 | 0.355 | 0.279 | 0.308 | 0.510 | 0.249 | 0.465 | 1.299 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.366 / 0.458 / 0.900; 2: 0.363 / 0.492 / 0.850; 3: 0.404 / 0.508 / 0.850; 4: 0.360 / 0.458 / 0.817; 5: 0.393 / 0.542 / 0.733; 6: 0.351 / 0.441 / 0.717; 7: 0.397 / 0.525 / 0.733; 8: 0.358 / 0.542 / 0.700; 9: 0.380 / 0.492 / 0.683; 10: 0.403 / 0.610 / 0.717; 11: 0.374 / 0.576 / 0.767; 12: 0.380 / 0.475 / 0.750; 13: 0.400 / 0.627 / 0.750; 14: 0.383 / 0.542 / 0.767; 15: 0.373 / 0.475 / 0.767
- 6h: 1: 0.382 / 0.514 / 0.911; 2: 0.368 / 0.480 / 0.881; 3: 0.386 / 0.528 / 0.856; 4: 0.362 / 0.458 / 0.819; 5: 0.385 / 0.545 / 0.819; 6: 0.370 / 0.497 / 0.842; 7: 0.386 / 0.520 / 0.858; 8: 0.378 / 0.545 / 0.858; 9: 0.376 / 0.497 / 0.850; 10: 0.387 / 0.536 / 0.867; 11: 0.372 / 0.531 / 0.869; 12: 0.383 / 0.520 / 0.867; 13: 0.378 / 0.539 / 0.856; 14: 0.373 / 0.483 / 0.844; 15: 0.385 / 0.534 / 0.836
- 24h: 1: 0.368 / 0.507 / 0.915; 2: 0.359 / 0.494 / 0.886; 3: 0.368 / 0.519 / 0.882; 4: 0.360 / 0.506 / 0.874; 5: 0.362 / 0.498 / 0.870; 6: 0.366 / 0.525 / 0.878; 7: 0.366 / 0.506 / 0.880; 8: 0.360 / 0.516 / 0.882; 9: 0.358 / 0.495 / 0.883; 10: 0.358 / 0.496 / 0.888; 11: 0.353 / 0.486 / 0.889; 12: 0.363 / 0.511 / 0.887; 13: 0.358 / 0.506 / 0.881; 14: 0.355 / 0.495 / 0.880; 15: 0.363 / 0.508 / 0.882
- 7d: 1: 0.354 / 0.524 / 0.900; 2: 0.343 / 0.495 / 0.900; 3: 0.347 / 0.514 / 0.900; 4: 0.343 / 0.497 / 0.898; 5: 0.345 / 0.505 / 0.897; 6: 0.342 / 0.498 / 0.898; 7: 0.342 / 0.498 / 0.900; 8: 0.341 / 0.497 / 0.900; 9: 0.339 / 0.491 / 0.900; 10: 0.342 / 0.503 / 0.899; 11: 0.339 / 0.491 / 0.901; 12: 0.340 / 0.499 / 0.900; 13: 0.340 / 0.501 / 0.899; 14: 0.340 / 0.504 / 0.899; 15: 0.340 / 0.496 / 0.898
- 30d: 1: 0.357 / 0.510 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.511 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.122 (body 0.090, range 0.154); 'price stays where it was' would score 0.111; colour right 0.593; typical miss of the close 10.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.119 (body 0.076, range 0.162); 'price stays where it was' would score 0.120; colour right 0.478; typical miss of the close 11.2 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.109 (body 0.074, range 0.145); 'price stays where it was' would score 0.108; colour right 0.491; typical miss of the close 12.1 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.118 (body 0.080, range 0.156); 'price stays where it was' would score 0.123; colour right 0.495; typical miss of the close 7.1 bp; chain ended on the right side 0.487 of 671 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.124; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.508 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.198 / 4.4; 3: 0.164 / 6.0; 4: 0.133 / 6.7; 5: 0.119 / 7.4; 6: 0.108 / 8.0; 7: 0.101 / 8.4; 8: 0.094 / 8.7; 9: 0.086 / 8.8; 10: 0.081 / 9.6; 11: 0.076 / 10.3; 12: 0.074 / 10.8; 13: 0.062 / 11.0; 14: 0.063 / 11.2; 15: 0.060 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 103106, probability skill vs chance 0.2352, widened contest next: True
  - now: threshold 0.8424, hit rate recent 0.9475 / long run 0.9317
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.268, naive rule 0.434, lift 3.74x
    - 24h: 44 calls (44 a day), hit rate 0.932, chance 0.277, naive rule 0.466, lift 3.37x
    - 7d: 422 calls (60 a day), hit rate 0.929, chance 0.295, naive rule 0.497, lift 3.15x
    - 30d: 1719 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.24x
  - next: threshold 0.5558, hit rate recent 0.5411 / long run 0.577
    - 6h: 58 calls (235 a day), hit rate 0.534, chance 0.268, lift 2.00x
    - 24h: 178 calls (179 a day), hit rate 0.551, chance 0.277, lift 1.99x
    - 7d: 662 calls (95 a day), hit rate 0.569, chance 0.295, lift 1.93x
    - 30d: 2470 calls (82 a day), hit rate 0.585, chance 0.290, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.490; 0.35: 538, 0.513; 0.40: 484, 0.561; 0.45: 416, 0.628; 0.50: 363, 0.682; 0.55: 318, 0.724; 0.60: 271, 0.768; 0.65: 224, 0.800; 0.70: 180, 0.832; 0.75: 139, 0.871; 0.80: 96, 0.912; 0.85: 49, 0.949; 0.90: 3, 0.976
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 496, 0.459; 0.40: 411, 0.489; 0.45: 316, 0.524; 0.50: 205, 0.558; 0.55: 91, 0.584; 0.60: 14, 0.602; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 103104, probability skill vs chance 0.2274, widened contest next: False
  - now: threshold 0.7053, hit rate recent 0.8 / long run 0.827
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.174, naive rule 0.328, lift 4.86x
    - 24h: 51 calls (51 a day), hit rate 0.725, chance 0.178, naive rule 0.380, lift 4.08x
    - 7d: 375 calls (54 a day), hit rate 0.816, chance 0.190, naive rule 0.406, lift 4.30x
    - 30d: 1587 calls (53 a day), hit rate 0.833, chance 0.187, naive rule 0.391, lift 4.46x
  - next: threshold 0.4422, hit rate recent 0.4843 / long run 0.4779
    - 6h: 39 calls (159 a day), hit rate 0.462, chance 0.174, lift 2.65x
    - 24h: 112 calls (113 a day), hit rate 0.491, chance 0.178, lift 2.76x
    - 7d: 524 calls (75 a day), hit rate 0.473, chance 0.190, lift 2.50x
    - 30d: 2113 calls (70 a day), hit rate 0.485, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 426, 0.416; 0.35: 358, 0.477; 0.40: 288, 0.547; 0.45: 236, 0.603; 0.50: 184, 0.658; 0.55: 140, 0.706; 0.60: 109, 0.748; 0.65: 83, 0.791; 0.70: 61, 0.824; 0.75: 34, 0.867; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.389; 0.35: 252, 0.426; 0.40: 163, 0.454; 0.45: 80, 0.474; 0.50: 19, 0.513; 0.55: 2, 0.574
- **K=8**: model 1791849600, labels learned 103101, probability skill vs chance 0.2228, widened contest next: False
  - now: threshold 0.5812, hit rate recent 0.6833 / long run 0.7034
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.120, naive rule 0.311, lift 6.82x
    - 24h: 47 calls (47 a day), hit rate 0.638, chance 0.119, naive rule 0.325, lift 5.37x
    - 7d: 398 calls (57 a day), hit rate 0.671, chance 0.122, naive rule 0.342, lift 5.48x
    - 30d: 1589 calls (53 a day), hit rate 0.719, chance 0.122, naive rule 0.329, lift 5.89x
  - next: threshold 0.3717, hit rate recent 0.426 / long run 0.402
    - 6h: 26 calls (107 a day), hit rate 0.423, chance 0.120, lift 3.53x
    - 24h: 89 calls (90 a day), hit rate 0.438, chance 0.119, lift 3.69x
    - 7d: 615 calls (88 a day), hit rate 0.389, chance 0.122, lift 3.18x
    - 30d: 2126 calls (71 a day), hit rate 0.411, chance 0.122, lift 3.37x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 264, 0.411; 0.35: 199, 0.485; 0.40: 153, 0.546; 0.45: 121, 0.591; 0.50: 92, 0.636; 0.55: 66, 0.688; 0.60: 45, 0.731; 0.65: 24, 0.778; 0.70: 9, 0.832; 0.75: 1, 0.789
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 182, 0.353; 0.35: 110, 0.392; 0.40: 46, 0.424; 0.45: 10, 0.460; 0.50: 1, 0.375
- **K=13**: model 1791849600, labels learned 103096, probability skill vs chance 0.1986, widened contest next: False
  - now: threshold 0.4361, hit rate recent 0.6294 / long run 0.5899
    - 6h: 9 calls (38 a day), hit rate 0.889, chance 0.087, naive rule 0.309, lift 10.22x
    - 24h: 48 calls (49 a day), hit rate 0.646, chance 0.073, naive rule 0.279, lift 8.81x
    - 7d: 359 calls (51 a day), hit rate 0.591, chance 0.079, naive rule 0.285, lift 7.51x
    - 30d: 1489 calls (50 a day), hit rate 0.592, chance 0.078, naive rule 0.272, lift 7.60x
  - next: threshold 0.2989, hit rate recent 0.3201 / long run 0.3171
    - 6h: 19 calls (79 a day), hit rate 0.421, chance 0.087, lift 4.84x
    - 24h: 84 calls (85 a day), hit rate 0.310, chance 0.073, lift 4.22x
    - 7d: 503 calls (72 a day), hit rate 0.326, chance 0.079, lift 4.15x
    - 30d: 2103 calls (70 a day), hit rate 0.316, chance 0.078, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.450; 0.35: 86, 0.512; 0.40: 61, 0.565; 0.45: 42, 0.621; 0.50: 26, 0.650; 0.55: 14, 0.705; 0.60: 5, 0.761; 0.65: 1, 0.857
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.331; 0.35: 14, 0.363; 0.40: 2, 0.392; 0.45: 0, 0.300

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.459 | 1.55% | 0.900 | 0.433 | 0.247 | 0.576 | 0.346 |
| 6h | 18.406 | 1.58% | 0.900 | 0.506 | 0.251 | 0.508 | 0.504 |
| 24h | 18.303 | 2.75% | 0.901 | 0.495 | 0.250 | 0.516 | 0.582 |
| 7d | 12.828 | 4.34% | 0.900 | 0.499 | 0.251 | 0.496 | 0.662 |
| 30d | 14.034 | 4.06% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.702 | 15.773 | 15.653 | 15.500 | 16.070 | 15.287 | 15.471 | 15.424 | 15.475 | 15.459 |
| 6h | 18.701 | 18.457 | 18.564 | 18.362 | 18.780 | 18.733 | 18.344 | 18.363 | 18.364 | 18.406 |
| 24h | 18.821 | 18.485 | 18.479 | 18.312 | 18.793 | 18.488 | 18.328 | 18.263 | 18.276 | 18.303 |
| 7d | 13.411 | 12.955 | 12.912 | 12.867 | 13.076 | 13.026 | 12.833 | 12.796 | 12.807 | 12.828 |
| 30d | 14.627 | 14.158 | 14.121 | 14.062 | 14.297 | 14.234 | 14.032 | 14.006 | 14.007 | 14.034 |

## Next candle

- candle starting 2026-10-13 18:32 UTC, last close 2501.12
- P(up) 0.4673, return quantiles (bp): {'05': -8.39, '10': -6.058, '25': -3.434, '40': -1.677, '50': -0.39, '60': 0.828, '75': 2.939, '90': 6.027, '95': 8.12}
- changepoint probability 0.0537, regime age 47.4 min
- agent weights: empirical 0.015, ewma 0.068, garch 0.057, har 0.229, bocpd 0.009, hmm 0.047, online_qr 0.259, lgbm 0.316

## Learning log

- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- HMM volatility states (sd, bp per minute): [2.04, 4.71, 13.13], current probabilities: [0.003, 0.965, 0.032]
- live generator: {'versions': 60, 'latest_effective': '2026-10-13 18:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.475, 'l_abs': 0.767, 'l_hi': 0.777, 'l_lo': 0.723, 'b05': 0.772, 'b25': 0.737, 'b75': 0.757, 'b95': 0.726}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.8], [1.3, 1.6], [1.2, 1.8], [1.2, 1.8], [1.3, 1.6], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.426, 1.933, 2.788, 3.186, 2.98, 2.918, 3.064, 3.389, 3.175, 3.271, 3.423, 3.79, 4.185, 4.518]}
- calibration offsets (in sigma): {'05': 0.0155, '10': 0.021, '25': -0.0725, '40': -0.086, '50': -0.065, '60': -0.044, '75': -0.0175, '90': -0.041, '95': -0.0655}
