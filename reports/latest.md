# ETH-USD 60s candle generator - report

- generated: 2026-10-08 14:01 UTC
- last closed candle: 2026-10-08 14:01 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.375 (96) | 0.509 (670) [0.457, 0.558] | 0.507 (2875) [0.486, 0.526] | 0.511 (3451) [0.493, 0.528] | 0.507 (479) [0.438, 0.579] | 0.500 (56) | 0.500 | flat -0.008 (noise 0.040) |
| colour_clear | 0.535 (746) | 0.526 (5210) [0.504, 0.545] | 0.505 (23206) [0.499, 0.512] | 0.503 (27921) [0.497, 0.509] | 0.545 (3683) [0.534, 0.555] | 0.549 (512) | 0.500 | up +0.030 (noise 0.013) |
| colour_confident | 0.613 (111) | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.585 (53) | 0.500 | - |
| colour_next | 0.524 (1434) | 0.522 (9977) [0.510, 0.534] | 0.506 (42883) [0.501, 0.512] | 0.505 (51457) [0.500, 0.509] | 0.531 (7108) [0.519, 0.544] | 0.524 (836) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.490 (20076) | 0.500 (139678) [0.495, 0.504] | 0.501 (600362) [0.500, 0.502] | 0.500 (720398) [0.499, 0.502] | 0.499 (99512) [0.494, 0.504] | 0.497 (11704) | 0.500 | flat -0.002 (noise 0.003) |
| colour_strong | 0.733 (30) | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.385 (13) | 0.500 | - |
| reversal_k13_next | 0.304 (69) | 0.311 (563) [0.291, 0.329] | 0.309 (2032) [0.294, 0.324] | 0.303 (2506) [0.290, 0.318] | 0.322 (401) [0.304, 0.340] | 0.342 (41) | 0.077 | flat +0.034 (noise 0.027) |
| reversal_k13_now | 0.531 (49) | 0.588 (396) [0.553, 0.635] | 0.582 (1484) [0.559, 0.604] | 0.581 (1762) [0.562, 0.601] | 0.583 (290) [0.534, 0.648] | 0.571 (28) | 0.077 | flat +0.010 (noise 0.038) |
| reversal_k3_next | 0.500 (54) | 0.585 (561) [0.555, 0.620] | 0.587 (2373) [0.572, 0.602] | 0.586 (2856) [0.573, 0.600] | 0.579 (416) [0.542, 0.631] | 0.632 (38) | 0.292 | flat +0.014 (noise 0.029) |
| reversal_k3_now | 0.954 (43) | 0.930 (400) [0.920, 0.940] | 0.939 (1691) [0.930, 0.947] | 0.940 (2036) [0.933, 0.948] | 0.930 (273) [0.915, 0.946] | 0.935 (46) | 0.293 | flat -0.025 (noise 0.017) |
| reversal_k5_next | 0.370 (54) | 0.462 (718) [0.431, 0.494] | 0.486 (2077) [0.466, 0.507] | 0.485 (2441) [0.467, 0.503] | 0.444 (451) [0.409, 0.491] | 0.441 (34) | 0.187 | flat -0.011 (noise 0.036) |
| reversal_k5_now | 0.826 (46) | 0.841 (390) [0.815, 0.866] | 0.836 (1570) [0.821, 0.852] | 0.837 (1887) [0.823, 0.851] | 0.837 (276) [0.800, 0.871] | 0.744 (39) | 0.187 | flat -0.018 (noise 0.026) |
| reversal_k8_next | 0.323 (93) | 0.397 (521) [0.365, 0.430] | 0.401 (2054) [0.383, 0.421] | 0.395 (2526) [0.380, 0.412] | 0.391 (420) [0.351, 0.431] | 0.409 (66) | 0.121 | flat +0.017 (noise 0.033) |
| reversal_k8_now | 0.678 (59) | 0.726 (394) [0.692, 0.760] | 0.725 (1572) [0.706, 0.743] | 0.716 (1883) [0.698, 0.735] | 0.730 (296) [0.685, 0.777] | 0.600 (35) | 0.122 | flat -0.029 (noise 0.033) |
| overall | 0.493 (22073) | 0.503 (154268) [0.498, 0.507] | 0.503 (660973) [0.502, 0.505] | 0.503 (793203) [0.501, 0.504] | 0.503 (109922) [0.497, 0.509] | 0.501 (12923) | - | flat -0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07674, 0.115] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5335, 'levels': [{'threshold': 0.07674, 'calls_per_day': 143.2, 'win_rate': 0.6051}, {'threshold': 0.115, 'calls_per_day': 36.3, 'win_rate': 0.6459}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 6812, 'rate': 0.5342}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15161 | 0.334 | 0.513 (14947) | 0.608 (630) | 0.777 (2419) |
| volatility: normal | 15160 | 0.361 | 0.510 (15094) | 0.566 (106) | 0.773 (2147) |
| volatility: wild | 15160 | 0.373 | 0.495 (15112) | 0.698 (43) | 0.777 (2110) |
| session: Asia 00-08 | 15360 | 0.353 | 0.507 (15256) | 0.600 (280) | 0.778 (2212) |
| session: Europe 08-13 | 9600 | 0.350 | 0.504 (9538) | 0.577 (156) | 0.769 (1489) |
| session: US 13-21 | 14941 | 0.365 | 0.504 (14841) | 0.606 (208) | 0.780 (2191) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5518) | 0.659 (135) | 0.770 (784) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.334 | 0.367 | 0.281 | 0.281 | 0.424 | 0.202 | 0.467 | 1.001 |
| 6h | 360 | 0.368 | 0.368 | 0.282 | 0.313 | 0.528 | 0.252 | 0.485 | 1.126 |
| 24h | 1440 | 0.369 | 0.362 | 0.295 | 0.325 | 0.519 | 0.260 | 0.479 | 1.188 |
| 7d | 10080 | 0.350 | 0.346 | 0.274 | 0.297 | 0.525 | 0.249 | 0.452 | 1.236 |
| 30d | 43200 | 0.356 | 0.354 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.334 / 0.424 / 0.867; 2: 0.339 / 0.458 / 0.933; 3: 0.321 / 0.356 / 0.917; 4: 0.345 / 0.475 / 0.950; 5: 0.320 / 0.424 / 0.950; 6: 0.375 / 0.593 / 0.850; 7: 0.336 / 0.492 / 0.817; 8: 0.315 / 0.407 / 0.933; 9: 0.351 / 0.525 / 0.850; 10: 0.317 / 0.441 / 0.850; 11: 0.333 / 0.441 / 0.850; 12: 0.320 / 0.390 / 0.900; 13: 0.339 / 0.458 / 0.833; 14: 0.323 / 0.492 / 0.750; 15: 0.320 / 0.475 / 0.767
- 6h: 1: 0.368 / 0.528 / 0.869; 2: 0.351 / 0.480 / 0.906; 3: 0.365 / 0.494 / 0.894; 4: 0.368 / 0.522 / 0.936; 5: 0.360 / 0.489 / 0.953; 6: 0.364 / 0.514 / 0.914; 7: 0.357 / 0.522 / 0.892; 8: 0.362 / 0.528 / 0.981; 9: 0.353 / 0.483 / 0.964; 10: 0.361 / 0.503 / 0.964; 11: 0.350 / 0.472 / 0.967; 12: 0.351 / 0.475 / 0.983; 13: 0.363 / 0.483 / 0.967; 14: 0.348 / 0.480 / 0.925; 15: 0.345 / 0.466 / 0.897
- 24h: 1: 0.369 / 0.519 / 0.897; 2: 0.359 / 0.494 / 0.919; 3: 0.363 / 0.512 / 0.908; 4: 0.363 / 0.494 / 0.916; 5: 0.357 / 0.496 / 0.912; 6: 0.354 / 0.492 / 0.903; 7: 0.359 / 0.506 / 0.895; 8: 0.355 / 0.485 / 0.908; 9: 0.350 / 0.478 / 0.906; 10: 0.357 / 0.494 / 0.906; 11: 0.357 / 0.503 / 0.904; 12: 0.350 / 0.473 / 0.904; 13: 0.361 / 0.515 / 0.903; 14: 0.355 / 0.500 / 0.897; 15: 0.355 / 0.490 / 0.895
- 7d: 1: 0.350 / 0.525 / 0.899; 2: 0.342 / 0.502 / 0.900; 3: 0.344 / 0.509 / 0.900; 4: 0.340 / 0.501 / 0.901; 5: 0.338 / 0.496 / 0.901; 6: 0.337 / 0.494 / 0.899; 7: 0.338 / 0.502 / 0.899; 8: 0.337 / 0.492 / 0.901; 9: 0.333 / 0.487 / 0.902; 10: 0.337 / 0.502 / 0.902; 11: 0.337 / 0.503 / 0.901; 12: 0.338 / 0.505 / 0.900; 13: 0.338 / 0.506 / 0.900; 14: 0.336 / 0.495 / 0.900; 15: 0.334 / 0.490 / 0.900
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.501 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.079 (body 0.042, range 0.115); 'price stays where it was' would score 0.113; colour right 0.458; typical miss of the close 26.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.120 (body 0.073, range 0.166); 'price stays where it was' would score 0.107; colour right 0.483; typical miss of the close 10.3 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.125 (body 0.083, range 0.166); 'price stays where it was' would score 0.121; colour right 0.495; typical miss of the close 9.2 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.115 (body 0.077, range 0.153); 'price stays where it was' would score 0.119; colour right 0.498; typical miss of the close 6.2 bp; chain ended on the right side 0.515 of 670 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.506 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.2; 2: 0.197 / 4.5; 3: 0.167 / 6.1; 4: 0.131 / 6.7; 5: 0.119 / 7.4; 6: 0.110 / 8.1; 7: 0.098 / 8.6; 8: 0.090 / 9.0; 9: 0.086 / 9.2; 10: 0.080 / 10.0; 11: 0.075 / 10.6; 12: 0.074 / 10.9; 13: 0.063 / 11.2; 14: 0.065 / 11.4; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 95635, probability skill vs chance 0.2226, widened contest next: False
  - now: threshold 0.8367, hit rate recent 0.9301 / long run 0.9373
    - 6h: 20 calls (81 a day), hit rate 0.900, chance 0.273, naive rule 0.482, lift 3.29x
    - 24h: 62 calls (62 a day), hit rate 0.935, chance 0.263, naive rule 0.433, lift 3.55x
    - 7d: 397 calls (57 a day), hit rate 0.932, chance 0.290, naive rule 0.484, lift 3.21x
    - 30d: 1692 calls (56 a day), hit rate 0.940, chance 0.291, naive rule 0.481, lift 3.23x
  - next: threshold 0.5615, hit rate recent 0.6012 / long run 0.5876
    - 6h: 14 calls (57 a day), hit rate 0.643, chance 0.273, lift 2.35x
    - 24h: 61 calls (61 a day), hit rate 0.590, chance 0.263, lift 2.24x
    - 7d: 544 calls (78 a day), hit rate 0.586, chance 0.290, lift 2.02x
    - 30d: 2348 calls (78 a day), hit rate 0.591, chance 0.291, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.517; 0.40: 486, 0.561; 0.45: 419, 0.627; 0.50: 366, 0.681; 0.55: 322, 0.724; 0.60: 274, 0.766; 0.65: 226, 0.802; 0.70: 181, 0.834; 0.75: 138, 0.872; 0.80: 96, 0.911; 0.85: 48, 0.949; 0.90: 2, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 497, 0.458; 0.40: 412, 0.488; 0.45: 316, 0.519; 0.50: 206, 0.553; 0.55: 91, 0.588; 0.60: 13, 0.615; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 95633, probability skill vs chance 0.1965, widened contest next: True
  - now: threshold 0.7132, hit rate recent 0.7886 / long run 0.8327
    - 6h: 18 calls (73 a day), hit rate 0.722, chance 0.178, naive rule 0.385, lift 4.05x
    - 24h: 59 calls (59 a day), hit rate 0.780, chance 0.177, naive rule 0.350, lift 4.40x
    - 7d: 392 calls (56 a day), hit rate 0.829, chance 0.190, naive rule 0.395, lift 4.36x
    - 30d: 1570 calls (52 a day), hit rate 0.834, chance 0.186, naive rule 0.389, lift 4.49x
  - next: threshold 0.4546, hit rate recent 0.4349 / long run 0.4674
    - 6h: 14 calls (57 a day), hit rate 0.429, chance 0.178, lift 2.40x
    - 24h: 53 calls (53 a day), hit rate 0.434, chance 0.177, lift 2.45x
    - 7d: 664 calls (95 a day), hit rate 0.453, chance 0.190, lift 2.39x
    - 30d: 2078 calls (69 a day), hit rate 0.489, chance 0.186, lift 2.63x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.411; 0.35: 367, 0.466; 0.40: 297, 0.535; 0.45: 243, 0.594; 0.50: 188, 0.651; 0.55: 143, 0.699; 0.60: 111, 0.740; 0.65: 85, 0.786; 0.70: 63, 0.819; 0.75: 34, 0.863; 0.80: 9, 0.884
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.385; 0.35: 253, 0.423; 0.40: 166, 0.449; 0.45: 84, 0.476; 0.50: 21, 0.517; 0.55: 2, 0.580
- **K=8**: model 1791417600, labels learned 95630, probability skill vs chance 0.1931, widened contest next: True
  - now: threshold 0.5728, hit rate recent 0.6372 / long run 0.7164
    - 6h: 17 calls (70 a day), hit rate 0.588, chance 0.110, naive rule 0.311, lift 5.35x
    - 24h: 62 calls (62 a day), hit rate 0.565, chance 0.113, naive rule 0.287, lift 4.98x
    - 7d: 399 calls (57 a day), hit rate 0.722, chance 0.124, naive rule 0.330, lift 5.84x
    - 30d: 1575 calls (53 a day), hit rate 0.724, chance 0.121, naive rule 0.325, lift 5.98x
  - next: threshold 0.3484, hit rate recent 0.374 / long run 0.3973
    - 6h: 30 calls (123 a day), hit rate 0.333, chance 0.110, lift 3.03x
    - 24h: 107 calls (108 a day), hit rate 0.374, chance 0.113, lift 3.30x
    - 7d: 553 calls (79 a day), hit rate 0.396, chance 0.124, lift 3.21x
    - 30d: 2069 calls (69 a day), hit rate 0.404, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 272, 0.402; 0.35: 205, 0.477; 0.40: 158, 0.538; 0.45: 124, 0.586; 0.50: 95, 0.629; 0.55: 68, 0.686; 0.60: 46, 0.731; 0.65: 24, 0.770; 0.70: 8, 0.815; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.347; 0.35: 115, 0.387; 0.40: 48, 0.414; 0.45: 10, 0.428; 0.50: 1, 0.421
- **K=13**: model 1791072000, labels learned 95625, probability skill vs chance 0.1797, widened contest next: True
  - now: threshold 0.4231, hit rate recent 0.5334 / long run 0.5793
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.078, naive rule 0.290, lift 5.48x
    - 24h: 49 calls (50 a day), hit rate 0.490, chance 0.072, naive rule 0.240, lift 6.84x
    - 7d: 387 calls (55 a day), hit rate 0.592, chance 0.078, naive rule 0.271, lift 7.58x
    - 30d: 1480 calls (49 a day), hit rate 0.583, chance 0.077, naive rule 0.267, lift 7.60x
  - next: threshold 0.2886, hit rate recent 0.328 / long run 0.3084
    - 6h: 19 calls (79 a day), hit rate 0.316, chance 0.078, lift 4.04x
    - 24h: 76 calls (77 a day), hit rate 0.303, chance 0.072, lift 4.23x
    - 7d: 546 calls (78 a day), hit rate 0.311, chance 0.078, lift 3.99x
    - 30d: 2038 calls (68 a day), hit rate 0.309, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.439; 0.35: 89, 0.499; 0.40: 63, 0.546; 0.45: 44, 0.604; 0.50: 27, 0.626; 0.55: 15, 0.680; 0.60: 6, 0.708; 0.65: 1, 0.786
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.317; 0.35: 16, 0.349; 0.40: 3, 0.337; 0.45: 1, 0.368

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 26.794 | 8.43% | 0.867 | 0.450 | 0.252 | 0.525 | 0.577 |
| 6h | 17.502 | 2.80% | 0.869 | 0.514 | 0.251 | 0.508 | 0.551 |
| 24h | 13.858 | 2.27% | 0.892 | 0.501 | 0.251 | 0.492 | 0.550 |
| 7d | 10.956 | 4.64% | 0.900 | 0.500 | 0.251 | 0.494 | 0.639 |
| 30d | 14.207 | 4.24% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 29.260 | 27.259 | 27.123 | 26.373 | 27.537 | 27.629 | 26.826 | 26.968 | 26.798 | 26.794 |
| 6h | 18.006 | 17.589 | 17.604 | 17.394 | 17.732 | 17.913 | 17.517 | 17.529 | 17.486 | 17.502 |
| 24h | 14.181 | 13.927 | 13.911 | 13.850 | 14.092 | 14.031 | 13.844 | 13.855 | 13.831 | 13.858 |
| 7d | 11.489 | 11.062 | 11.040 | 10.994 | 11.176 | 11.161 | 10.958 | 10.948 | 10.939 | 10.956 |
| 30d | 14.836 | 14.338 | 14.288 | 14.236 | 14.479 | 14.424 | 14.209 | 14.181 | 14.179 | 14.207 |

## Next candle

- candle starting 2026-10-08 14:01 UTC, last close 2520.42
- P(up) 0.4788, return quantiles (bp): {'05': -20.784, '10': -16.101, '25': -8.353, '40': -3.71, '50': -0.552, '60': 2.09, '75': 6.746, '90': 13.472, '95': 17.953}
- changepoint probability 0.0769, regime age 21.2 min
- agent weights: empirical 0.005, ewma 0.090, garch 0.103, har 0.363, bocpd 0.025, hmm 0.015, online_qr 0.210, lgbm 0.189

## Learning log

- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- HMM volatility states (sd, bp per minute): [2.0, 4.45, 12.64], current probabilities: [0.01, 0.394, 0.596]
- live generator: {'versions': 60, 'latest_effective': '2026-10-08 14:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.368, 'l_abs': 0.699, 'l_hi': 0.719, 'l_lo': 0.731, 'b05': 0.687, 'b25': 0.639, 'b75': 0.531, 'b95': 0.624}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.3, 1.8], [1.5, 1.8]], 'cone_width': [1.487, 1.976, 1.872, 2.015, 2.702, 3.232, 2.229, 2.567, 2.657, 3.149, 3.295, 3.369, 3.719, 4.179]}
- calibration offsets (in sigma): {'05': -0.1, '10': -0.12, '25': -0.1, '40': -0.1, '50': -0.05, '60': -0.05, '75': -0.01, '90': -0.02, '95': -0.04}
