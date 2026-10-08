# ETH-USD 60s candle generator - report

- generated: 2026-10-08 00:32 UTC
- last closed candle: 2026-10-08 00:32 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.375 (96) | 0.509 (670) [0.457, 0.558] | 0.507 (2875) [0.486, 0.526] | 0.511 (3451) [0.493, 0.528] | 0.507 (479) [0.438, 0.579] | 0.500 (2) | 0.500 | flat -0.008 (noise 0.040) |
| colour_clear | 0.535 (746) | 0.526 (5210) [0.504, 0.545] | 0.505 (23206) [0.499, 0.512] | 0.503 (27921) [0.497, 0.509] | 0.545 (3683) [0.534, 0.555] | 0.391 (23) | 0.500 | up +0.030 (noise 0.013) |
| colour_confident | 0.613 (111) | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.000 (4) | 0.500 | - |
| colour_next | 0.524 (1434) | 0.522 (9977) [0.510, 0.534] | 0.506 (42883) [0.501, 0.512] | 0.505 (51457) [0.500, 0.509] | 0.531 (7108) [0.519, 0.544] | 0.438 (32) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.490 (20076) | 0.500 (139678) [0.495, 0.504] | 0.501 (600362) [0.500, 0.502] | 0.500 (720398) [0.499, 0.502] | 0.499 (99512) [0.494, 0.504] | 0.502 (448) | 0.500 | flat -0.002 (noise 0.003) |
| colour_strong | 0.733 (30) | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.000 (1) | 0.500 | - |
| reversal_k13_next | 0.304 (69) | 0.311 (563) [0.291, 0.329] | 0.309 (2032) [0.294, 0.324] | 0.303 (2506) [0.290, 0.318] | 0.322 (401) [0.304, 0.340] | 0.000 (1) | 0.077 | flat +0.034 (noise 0.027) |
| reversal_k13_now | 0.531 (49) | 0.588 (396) [0.553, 0.635] | 0.582 (1484) [0.559, 0.604] | 0.581 (1762) [0.562, 0.601] | 0.583 (290) [0.534, 0.648] | 0.000 (1) | 0.077 | flat +0.010 (noise 0.038) |
| reversal_k3_next | 0.500 (54) | 0.585 (561) [0.555, 0.620] | 0.587 (2373) [0.572, 0.602] | 0.586 (2856) [0.573, 0.600] | 0.579 (416) [0.542, 0.631] | 0.667 (3) | 0.292 | flat +0.014 (noise 0.029) |
| reversal_k3_now | 0.954 (43) | 0.930 (400) [0.920, 0.940] | 0.939 (1691) [0.930, 0.947] | 0.940 (2036) [0.933, 0.948] | 0.930 (273) [0.915, 0.946] | 1.000 (4) | 0.293 | flat -0.025 (noise 0.017) |
| reversal_k5_next | 0.370 (54) | 0.462 (718) [0.431, 0.494] | 0.486 (2077) [0.466, 0.507] | 0.485 (2441) [0.467, 0.503] | 0.444 (451) [0.409, 0.491] | 1.000 (1) | 0.187 | flat -0.011 (noise 0.036) |
| reversal_k5_now | 0.826 (46) | 0.841 (390) [0.815, 0.866] | 0.836 (1570) [0.821, 0.852] | 0.837 (1887) [0.823, 0.851] | 0.837 (276) [0.800, 0.871] | 0.667 (3) | 0.187 | flat -0.018 (noise 0.026) |
| reversal_k8_next | 0.323 (93) | 0.397 (521) [0.365, 0.430] | 0.401 (2054) [0.383, 0.421] | 0.395 (2526) [0.380, 0.412] | 0.391 (420) [0.351, 0.431] | 1.000 (1) | 0.121 | flat +0.017 (noise 0.033) |
| reversal_k8_now | 0.678 (59) | 0.726 (394) [0.692, 0.760] | 0.725 (1572) [0.706, 0.743] | 0.716 (1883) [0.698, 0.735] | 0.730 (296) [0.685, 0.777] | 0.500 (2) | 0.122 | flat -0.029 (noise 0.033) |
| overall | 0.493 (22073) | 0.503 (154268) [0.498, 0.507] | 0.503 (660973) [0.502, 0.505] | 0.503 (793203) [0.501, 0.504] | 0.503 (109922) [0.497, 0.509] | 0.504 (498) | - | flat -0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07732, 0.1151] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5337, 'levels': [{'threshold': 0.07732, 'calls_per_day': 142.4, 'win_rate': 0.6008}, {'threshold': 0.1151, 'calls_per_day': 35.8, 'win_rate': 0.6561}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 6008, 'rate': 0.5351}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14891 | 0.334 | 0.514 (14678) | 0.608 (623) | 0.779 (2378) |
| volatility: normal | 14890 | 0.360 | 0.509 (14826) | 0.553 (76) | 0.773 (2093) |
| volatility: wild | 14891 | 0.373 | 0.494 (14845) | 0.677 (31) | 0.776 (2067) |
| session: Asia 00-08 | 14912 | 0.352 | 0.507 (14811) | 0.595 (257) | 0.777 (2143) |
| session: Europe 08-13 | 9300 | 0.349 | 0.503 (9239) | 0.575 (134) | 0.771 (1433) |
| session: US 13-21 | 14880 | 0.365 | 0.505 (14781) | 0.603 (204) | 0.781 (2178) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5518) | 0.659 (135) | 0.770 (784) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.365 | 0.340 | 0.276 | 0.276 | 0.483 | 0.252 | 0.477 | 1.025 |
| 6h | 360 | 0.354 | 0.344 | 0.275 | 0.302 | 0.503 | 0.261 | 0.446 | 1.263 |
| 24h | 1440 | 0.363 | 0.357 | 0.292 | 0.321 | 0.522 | 0.261 | 0.465 | 1.272 |
| 7d | 10080 | 0.350 | 0.346 | 0.273 | 0.298 | 0.522 | 0.248 | 0.452 | 1.240 |
| 30d | 43200 | 0.356 | 0.354 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.365 / 0.483 / 0.900; 2: 0.375 / 0.550 / 0.950; 3: 0.347 / 0.433 / 0.900; 4: 0.363 / 0.500 / 0.867; 5: 0.352 / 0.467 / 0.867; 6: 0.354 / 0.483 / 0.883; 7: 0.370 / 0.517 / 0.817; 8: 0.355 / 0.517 / 0.933; 9: 0.338 / 0.483 / 0.933; 10: 0.350 / 0.500 / 0.917; 11: 0.320 / 0.383 / 0.983; 12: 0.333 / 0.400 / 0.967; 13: 0.337 / 0.500 / 1.000; 14: 0.345 / 0.533 / 1.000; 15: 0.341 / 0.467 / 1.000
- 6h: 1: 0.354 / 0.503 / 0.903; 2: 0.355 / 0.550 / 0.958; 3: 0.349 / 0.517 / 0.922; 4: 0.353 / 0.500 / 0.942; 5: 0.335 / 0.469 / 0.925; 6: 0.338 / 0.483 / 0.931; 7: 0.356 / 0.531 / 0.881; 8: 0.343 / 0.472 / 0.914; 9: 0.342 / 0.483 / 0.906; 10: 0.348 / 0.511 / 0.906; 11: 0.332 / 0.461 / 0.928; 12: 0.338 / 0.472 / 0.933; 13: 0.342 / 0.503 / 0.931; 14: 0.339 / 0.486 / 0.906; 15: 0.351 / 0.511 / 0.903
- 24h: 1: 0.363 / 0.522 / 0.903; 2: 0.348 / 0.478 / 0.899; 3: 0.356 / 0.512 / 0.900; 4: 0.355 / 0.510 / 0.906; 5: 0.347 / 0.493 / 0.909; 6: 0.344 / 0.490 / 0.910; 7: 0.349 / 0.493 / 0.903; 8: 0.342 / 0.477 / 0.910; 9: 0.342 / 0.483 / 0.909; 10: 0.344 / 0.493 / 0.910; 11: 0.341 / 0.482 / 0.906; 12: 0.339 / 0.477 / 0.904; 13: 0.342 / 0.499 / 0.901; 14: 0.344 / 0.501 / 0.897; 15: 0.341 / 0.487 / 0.890
- 7d: 1: 0.350 / 0.522 / 0.899; 2: 0.342 / 0.501 / 0.900; 3: 0.344 / 0.511 / 0.900; 4: 0.340 / 0.501 / 0.901; 5: 0.338 / 0.497 / 0.901; 6: 0.337 / 0.495 / 0.901; 7: 0.338 / 0.503 / 0.900; 8: 0.337 / 0.494 / 0.901; 9: 0.333 / 0.489 / 0.900; 10: 0.337 / 0.504 / 0.901; 11: 0.337 / 0.503 / 0.901; 12: 0.337 / 0.506 / 0.900; 13: 0.338 / 0.507 / 0.900; 14: 0.335 / 0.493 / 0.899; 15: 0.334 / 0.491 / 0.899
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.103 (body 0.065, range 0.142); 'price stays where it was' would score 0.094; colour right 0.467; typical miss of the close 6.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.110 (body 0.074, range 0.146); 'price stays where it was' would score 0.115; colour right 0.500; typical miss of the close 6.3 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.110 (body 0.073, range 0.148); 'price stays where it was' would score 0.124; colour right 0.478; typical miss of the close 9.1 bp; chain ended on the right side 0.385 of 96 chains; n=1440
- 7d: match 0.115 (body 0.076, range 0.153); 'price stays where it was' would score 0.120; colour right 0.496; typical miss of the close 6.1 bp; chain ended on the right side 0.507 of 670 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.1 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.2; 2: 0.197 / 4.5; 3: 0.167 / 6.1; 4: 0.131 / 6.6; 5: 0.120 / 7.3; 6: 0.110 / 8.2; 7: 0.097 / 8.6; 8: 0.090 / 8.9; 9: 0.085 / 9.1; 10: 0.080 / 10.0; 11: 0.075 / 10.7; 12: 0.073 / 10.9; 13: 0.063 / 11.3; 14: 0.066 / 11.4; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 94826, probability skill vs chance 0.2179, widened contest next: False
  - now: threshold 0.8418, hit rate recent 0.9414 / long run 0.938
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.280, naive rule 0.447, lift 3.57x
    - 24h: 47 calls (47 a day), hit rate 0.957, chance 0.289, naive rule 0.478, lift 3.31x
    - 7d: 400 calls (57 a day), hit rate 0.932, chance 0.294, naive rule 0.490, lift 3.17x
    - 30d: 1691 calls (56 a day), hit rate 0.938, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5616, hit rate recent 0.5793 / long run 0.5851
    - 6h: 16 calls (65 a day), hit rate 0.562, chance 0.280, lift 2.01x
    - 24h: 53 calls (53 a day), hit rate 0.528, chance 0.289, lift 1.83x
    - 7d: 560 calls (80 a day), hit rate 0.586, chance 0.294, lift 1.99x
    - 30d: 2376 calls (79 a day), hit rate 0.587, chance 0.292, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.494; 0.35: 537, 0.518; 0.40: 486, 0.561; 0.45: 420, 0.628; 0.50: 367, 0.680; 0.55: 322, 0.723; 0.60: 275, 0.765; 0.65: 225, 0.802; 0.70: 181, 0.833; 0.75: 138, 0.871; 0.80: 97, 0.910; 0.85: 48, 0.947; 0.90: 2, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.423; 0.35: 497, 0.457; 0.40: 412, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.552; 0.55: 92, 0.585; 0.60: 13, 0.613; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 94824, probability skill vs chance 0.1902, widened contest next: False
  - now: threshold 0.7134, hit rate recent 0.8231 / long run 0.8379
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.171, naive rule 0.324, lift 4.77x
    - 24h: 48 calls (48 a day), hit rate 0.812, chance 0.185, naive rule 0.376, lift 4.40x
    - 7d: 392 calls (56 a day), hit rate 0.842, chance 0.191, naive rule 0.400, lift 4.40x
    - 30d: 1570 calls (52 a day), hit rate 0.836, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4556, hit rate recent 0.4487 / long run 0.4699
    - 6h: 13 calls (53 a day), hit rate 0.385, chance 0.171, lift 2.24x
    - 24h: 50 calls (50 a day), hit rate 0.420, chance 0.185, lift 2.28x
    - 7d: 712 calls (102 a day), hit rate 0.463, chance 0.191, lift 2.42x
    - 30d: 2078 calls (69 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.411; 0.35: 368, 0.466; 0.40: 298, 0.535; 0.45: 244, 0.593; 0.50: 189, 0.650; 0.55: 144, 0.698; 0.60: 112, 0.740; 0.65: 85, 0.786; 0.70: 63, 0.821; 0.75: 34, 0.863; 0.80: 9, 0.884
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.384; 0.35: 253, 0.421; 0.40: 166, 0.447; 0.45: 85, 0.474; 0.50: 21, 0.513; 0.55: 2, 0.580
- **K=8**: model 1791417600, labels learned 94821, probability skill vs chance 0.185, widened contest next: True
  - now: threshold 0.57, hit rate recent 0.6668 / long run 0.7227
    - 6h: 17 calls (70 a day), hit rate 0.588, chance 0.116, naive rule 0.262, lift 5.08x
    - 24h: 60 calls (60 a day), hit rate 0.667, chance 0.116, naive rule 0.313, lift 5.73x
    - 7d: 395 calls (56 a day), hit rate 0.727, chance 0.126, naive rule 0.336, lift 5.78x
    - 30d: 1571 calls (52 a day), hit rate 0.724, chance 0.121, naive rule 0.325, lift 5.98x
  - next: threshold 0.3472, hit rate recent 0.3616 / long run 0.3972
    - 6h: 25 calls (103 a day), hit rate 0.320, chance 0.116, lift 2.77x
    - 24h: 87 calls (88 a day), hit rate 0.333, chance 0.116, lift 2.86x
    - 7d: 519 calls (74 a day), hit rate 0.399, chance 0.126, lift 3.17x
    - 30d: 2053 calls (68 a day), hit rate 0.401, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 272, 0.401; 0.35: 206, 0.476; 0.40: 158, 0.537; 0.45: 125, 0.585; 0.50: 96, 0.628; 0.55: 68, 0.683; 0.60: 46, 0.729; 0.65: 24, 0.768; 0.70: 8, 0.812; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.346; 0.35: 115, 0.385; 0.40: 48, 0.413; 0.45: 10, 0.428; 0.50: 1, 0.421
- **K=13**: model 1791072000, labels learned 94816, probability skill vs chance 0.1677, widened contest next: True
  - now: threshold 0.4231, hit rate recent 0.5127 / long run 0.5787
    - 6h: 14 calls (58 a day), hit rate 0.286, chance 0.061, naive rule 0.190, lift 4.69x
    - 24h: 48 calls (49 a day), hit rate 0.500, chance 0.075, naive rule 0.264, lift 6.69x
    - 7d: 396 calls (57 a day), hit rate 0.588, chance 0.079, naive rule 0.274, lift 7.49x
    - 30d: 1481 calls (49 a day), hit rate 0.581, chance 0.077, naive rule 0.266, lift 7.58x
  - next: threshold 0.283, hit rate recent 0.3061 / long run 0.3055
    - 6h: 24 calls (100 a day), hit rate 0.250, chance 0.061, lift 4.11x
    - 24h: 64 calls (65 a day), hit rate 0.297, chance 0.075, lift 3.97x
    - 7d: 559 calls (80 a day), hit rate 0.311, chance 0.079, lift 3.96x
    - 30d: 2032 calls (68 a day), hit rate 0.308, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.437; 0.35: 89, 0.495; 0.40: 64, 0.543; 0.45: 44, 0.601; 0.50: 28, 0.621; 0.55: 15, 0.675; 0.60: 6, 0.704; 0.65: 2, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.315; 0.35: 16, 0.348; 0.40: 3, 0.337; 0.45: 1, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.114 | 5.40% | 0.867 | 0.400 | 0.252 | 0.417 | 0.396 |
| 6h | 8.415 | 4.17% | 0.897 | 0.497 | 0.250 | 0.497 | 0.389 |
| 24h | 13.702 | 4.62% | 0.901 | 0.497 | 0.251 | 0.493 | 0.538 |
| 7d | 10.796 | 4.69% | 0.900 | 0.500 | 0.251 | 0.493 | 0.636 |
| 30d | 14.162 | 4.24% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.577 | 8.164 | 8.094 | 8.148 | 8.250 | 8.115 | 8.055 | 8.092 | 8.062 | 8.114 |
| 6h | 8.781 | 8.457 | 8.416 | 8.427 | 8.531 | 8.430 | 8.435 | 8.406 | 8.395 | 8.415 |
| 24h | 14.366 | 13.886 | 13.716 | 13.800 | 13.874 | 13.830 | 13.717 | 13.679 | 13.669 | 13.702 |
| 7d | 11.326 | 10.905 | 10.880 | 10.835 | 11.022 | 10.988 | 10.796 | 10.788 | 10.778 | 10.796 |
| 30d | 14.789 | 14.293 | 14.243 | 14.192 | 14.433 | 14.378 | 14.164 | 14.137 | 14.135 | 14.162 |

## Next candle

- candle starting 2026-10-08 00:32 UTC, last close 2571.71
- P(up) 0.4969, return quantiles (bp): {'05': -5.482, '10': -4.289, '25': -2.068, '40': -0.714, '50': -0.027, '60': 0.766, '75': 1.997, '90': 3.932, '95': 5.04}
- changepoint probability 0.0418, regime age 141.9 min
- agent weights: empirical 0.004, ewma 0.083, garch 0.153, har 0.135, bocpd 0.025, hmm 0.095, online_qr 0.233, lgbm 0.272

## Learning log

- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.75, 4.19, 12.48], current probabilities: [0.121, 0.87, 0.009]
- live generator: {'versions': 60, 'latest_effective': '2026-10-08 00:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.248, 'l_abs': 0.676, 'l_hi': 0.703, 'l_lo': 0.722, 'b05': 0.679, 'b25': 0.605, 'b75': 0.581, 'b95': 0.606}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.426, 1.821, 1.906, 2.179, 2.44, 3.161, 2.772, 3.129, 3.239, 3.271, 3.289, 3.642, 4.27, 4.894]}
- calibration offsets (in sigma): {'05': 0.0055, '10': -0.049, '25': -0.0025, '40': 0.014, '50': 0.005, '60': 0.016, '75': 0.0125, '90': -0.011, '95': -0.0855}
