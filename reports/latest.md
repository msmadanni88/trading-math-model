# ETH-USD 60s candle generator - report

- generated: 2026-10-08 06:36 UTC
- last closed candle: 2026-10-08 06:36 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.375 (96) | 0.509 (670) [0.457, 0.558] | 0.507 (2875) [0.486, 0.526] | 0.511 (3451) [0.493, 0.528] | 0.507 (479) [0.438, 0.579] | 0.500 (26) | 0.500 | flat -0.008 (noise 0.040) |
| colour_clear | 0.535 (746) | 0.526 (5210) [0.504, 0.545] | 0.505 (23206) [0.499, 0.512] | 0.503 (27921) [0.497, 0.509] | 0.545 (3683) [0.534, 0.555] | 0.550 (251) | 0.500 | up +0.030 (noise 0.013) |
| colour_confident | 0.613 (111) | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.520 (25) | 0.500 | - |
| colour_next | 0.524 (1434) | 0.522 (9977) [0.510, 0.534] | 0.506 (42883) [0.501, 0.512] | 0.505 (51457) [0.500, 0.509] | 0.531 (7108) [0.519, 0.544] | 0.510 (394) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.490 (20076) | 0.500 (139678) [0.495, 0.504] | 0.501 (600362) [0.500, 0.502] | 0.500 (720398) [0.499, 0.502] | 0.499 (99512) [0.494, 0.504] | 0.499 (5516) | 0.500 | flat -0.002 (noise 0.003) |
| colour_strong | 0.733 (30) | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.333 (3) | 0.500 | - |
| reversal_k13_next | 0.304 (69) | 0.311 (563) [0.291, 0.329] | 0.309 (2032) [0.294, 0.324] | 0.303 (2506) [0.290, 0.318] | 0.322 (401) [0.304, 0.340] | 0.294 (17) | 0.077 | flat +0.034 (noise 0.027) |
| reversal_k13_now | 0.531 (49) | 0.588 (396) [0.553, 0.635] | 0.582 (1484) [0.559, 0.604] | 0.581 (1762) [0.562, 0.601] | 0.583 (290) [0.534, 0.648] | 0.667 (9) | 0.077 | flat +0.010 (noise 0.038) |
| reversal_k3_next | 0.500 (54) | 0.585 (561) [0.555, 0.620] | 0.587 (2373) [0.572, 0.602] | 0.586 (2856) [0.573, 0.600] | 0.579 (416) [0.542, 0.631] | 0.591 (22) | 0.292 | flat +0.014 (noise 0.029) |
| reversal_k3_now | 0.954 (43) | 0.930 (400) [0.920, 0.940] | 0.939 (1691) [0.930, 0.947] | 0.940 (2036) [0.933, 0.948] | 0.930 (273) [0.915, 0.946] | 1.000 (18) | 0.293 | flat -0.025 (noise 0.017) |
| reversal_k5_next | 0.370 (54) | 0.462 (718) [0.431, 0.494] | 0.486 (2077) [0.466, 0.507] | 0.485 (2441) [0.467, 0.503] | 0.444 (451) [0.409, 0.491] | 0.421 (19) | 0.187 | flat -0.011 (noise 0.036) |
| reversal_k5_now | 0.826 (46) | 0.841 (390) [0.815, 0.866] | 0.836 (1570) [0.821, 0.852] | 0.837 (1887) [0.823, 0.851] | 0.837 (276) [0.800, 0.871] | 0.765 (17) | 0.187 | flat -0.018 (noise 0.026) |
| reversal_k8_next | 0.323 (93) | 0.397 (521) [0.365, 0.430] | 0.401 (2054) [0.383, 0.421] | 0.395 (2526) [0.380, 0.412] | 0.391 (420) [0.351, 0.431] | 0.481 (27) | 0.121 | flat +0.017 (noise 0.033) |
| reversal_k8_now | 0.678 (59) | 0.726 (394) [0.692, 0.760] | 0.725 (1572) [0.706, 0.743] | 0.716 (1883) [0.698, 0.735] | 0.730 (296) [0.685, 0.777] | 0.667 (12) | 0.122 | flat -0.029 (noise 0.033) |
| overall | 0.493 (22073) | 0.503 (154268) [0.498, 0.507] | 0.503 (660973) [0.502, 0.505] | 0.503 (793203) [0.501, 0.504] | 0.503 (109922) [0.497, 0.509] | 0.502 (6077) | - | flat -0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07691, 0.1147] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5336, 'levels': [{'threshold': 0.07691, 'calls_per_day': 142.6, 'win_rate': 0.6012}, {'threshold': 0.1147, 'calls_per_day': 35.4, 'win_rate': 0.652}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 6370, 'rate': 0.5341}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15012 | 0.334 | 0.514 (14799) | 0.608 (630) | 0.779 (2403) |
| volatility: normal | 15012 | 0.360 | 0.510 (14947) | 0.570 (86) | 0.773 (2105) |
| volatility: wild | 15012 | 0.373 | 0.494 (14965) | 0.657 (35) | 0.777 (2076) |
| session: Asia 00-08 | 15276 | 0.352 | 0.507 (15173) | 0.597 (278) | 0.778 (2189) |
| session: Europe 08-13 | 9300 | 0.349 | 0.503 (9239) | 0.575 (134) | 0.771 (1433) |
| session: US 13-21 | 14880 | 0.365 | 0.505 (14781) | 0.603 (204) | 0.781 (2178) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5518) | 0.659 (135) | 0.770 (784) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.354 | 0.376 | 0.347 | 0.347 | 0.517 | 0.259 | 0.450 | 1.099 |
| 6h | 360 | 0.372 | 0.355 | 0.307 | 0.335 | 0.520 | 0.271 | 0.473 | 1.087 |
| 24h | 1440 | 0.371 | 0.362 | 0.296 | 0.327 | 0.521 | 0.268 | 0.475 | 1.248 |
| 7d | 10080 | 0.350 | 0.346 | 0.275 | 0.299 | 0.523 | 0.249 | 0.452 | 1.237 |
| 30d | 43200 | 0.356 | 0.354 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.354 / 0.517 / 0.917; 2: 0.371 / 0.500 / 0.917; 3: 0.335 / 0.483 / 0.850; 4: 0.361 / 0.500 / 0.833; 5: 0.350 / 0.517 / 0.817; 6: 0.353 / 0.569 / 0.800; 7: 0.363 / 0.448 / 0.850; 8: 0.368 / 0.500 / 0.700; 9: 0.339 / 0.397 / 0.700; 10: 0.368 / 0.534 / 0.683; 11: 0.352 / 0.517 / 0.683; 12: 0.367 / 0.517 / 0.650; 13: 0.363 / 0.552 / 0.700; 14: 0.366 / 0.517 / 0.783; 15: 0.360 / 0.500 / 0.833
- 6h: 1: 0.372 / 0.520 / 0.886; 2: 0.360 / 0.489 / 0.878; 3: 0.355 / 0.517 / 0.892; 4: 0.355 / 0.489 / 0.853; 5: 0.357 / 0.514 / 0.839; 6: 0.347 / 0.489 / 0.861; 7: 0.353 / 0.483 / 0.900; 8: 0.345 / 0.450 / 0.828; 9: 0.346 / 0.506 / 0.847; 10: 0.349 / 0.483 / 0.844; 11: 0.361 / 0.550 / 0.828; 12: 0.346 / 0.483 / 0.806; 13: 0.354 / 0.520 / 0.833; 14: 0.359 / 0.534 / 0.881; 15: 0.354 / 0.497 / 0.911
- 24h: 1: 0.371 / 0.521 / 0.899; 2: 0.355 / 0.476 / 0.890; 3: 0.363 / 0.518 / 0.897; 4: 0.360 / 0.492 / 0.892; 5: 0.356 / 0.498 / 0.892; 6: 0.350 / 0.478 / 0.902; 7: 0.359 / 0.493 / 0.909; 8: 0.350 / 0.473 / 0.896; 9: 0.351 / 0.488 / 0.897; 10: 0.354 / 0.493 / 0.902; 11: 0.353 / 0.499 / 0.893; 12: 0.345 / 0.465 / 0.887; 13: 0.357 / 0.522 / 0.894; 14: 0.356 / 0.509 / 0.907; 15: 0.354 / 0.494 / 0.908
- 7d: 1: 0.350 / 0.523 / 0.899; 2: 0.343 / 0.502 / 0.899; 3: 0.344 / 0.510 / 0.899; 4: 0.340 / 0.501 / 0.900; 5: 0.338 / 0.496 / 0.899; 6: 0.337 / 0.495 / 0.899; 7: 0.338 / 0.501 / 0.899; 8: 0.336 / 0.491 / 0.897; 9: 0.333 / 0.488 / 0.898; 10: 0.337 / 0.502 / 0.898; 11: 0.337 / 0.504 / 0.897; 12: 0.337 / 0.504 / 0.896; 13: 0.338 / 0.507 / 0.897; 14: 0.335 / 0.493 / 0.898; 15: 0.335 / 0.491 / 0.899
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.498 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.500 / 0.900; 5: 0.350 / 0.501 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.502 / 0.899; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.899; 12: 0.346 / 0.502 / 0.899; 13: 0.346 / 0.502 / 0.899; 14: 0.345 / 0.495 / 0.899; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.082 (body 0.055, range 0.109); 'price stays where it was' would score 0.096; colour right 0.569; typical miss of the close 15.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.122 (body 0.084, range 0.160); 'price stays where it was' would score 0.124; colour right 0.531; typical miss of the close 10.4 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.118 (body 0.077, range 0.158); 'price stays where it was' would score 0.127; colour right 0.486; typical miss of the close 8.8 bp; chain ended on the right side 0.438 of 96 chains; n=1440
- 7d: match 0.115 (body 0.077, range 0.153); 'price stays where it was' would score 0.121; colour right 0.497; typical miss of the close 6.2 bp; chain ended on the right side 0.512 of 670 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.1 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.2; 2: 0.197 / 4.5; 3: 0.167 / 6.1; 4: 0.131 / 6.6; 5: 0.120 / 7.4; 6: 0.110 / 8.2; 7: 0.098 / 8.6; 8: 0.090 / 9.0; 9: 0.085 / 9.2; 10: 0.080 / 10.0; 11: 0.075 / 10.7; 12: 0.073 / 10.9; 13: 0.063 / 11.3; 14: 0.066 / 11.4; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 95190, probability skill vs chance 0.219, widened contest next: False
  - now: threshold 0.833, hit rate recent 0.9537 / long run 0.9394
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.244, naive rule 0.380, lift 4.10x
    - 24h: 55 calls (55 a day), hit rate 0.964, chance 0.282, naive rule 0.456, lift 3.42x
    - 7d: 391 calls (56 a day), hit rate 0.936, chance 0.292, naive rule 0.485, lift 3.21x
    - 30d: 1685 calls (56 a day), hit rate 0.941, chance 0.291, naive rule 0.481, lift 3.23x
  - next: threshold 0.5616, hit rate recent 0.5786 / long run 0.5849
    - 6h: 18 calls (73 a day), hit rate 0.556, chance 0.244, lift 2.28x
    - 24h: 58 calls (58 a day), hit rate 0.569, chance 0.282, lift 2.02x
    - 7d: 555 calls (79 a day), hit rate 0.582, chance 0.292, lift 1.99x
    - 30d: 2374 calls (79 a day), hit rate 0.588, chance 0.291, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.517; 0.40: 487, 0.561; 0.45: 420, 0.627; 0.50: 367, 0.680; 0.55: 322, 0.723; 0.60: 274, 0.765; 0.65: 225, 0.802; 0.70: 181, 0.834; 0.75: 138, 0.873; 0.80: 96, 0.911; 0.85: 48, 0.950; 0.90: 2, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.423; 0.35: 497, 0.457; 0.40: 412, 0.486; 0.45: 316, 0.518; 0.50: 206, 0.552; 0.55: 92, 0.586; 0.60: 13, 0.613; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 95188, probability skill vs chance 0.1955, widened contest next: True
  - now: threshold 0.7126, hit rate recent 0.8148 / long run 0.8367
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.169, naive rule 0.325, lift 4.66x
    - 24h: 56 calls (56 a day), hit rate 0.839, chance 0.184, naive rule 0.369, lift 4.57x
    - 7d: 386 calls (55 a day), hit rate 0.839, chance 0.191, naive rule 0.398, lift 4.40x
    - 30d: 1564 calls (52 a day), hit rate 0.836, chance 0.186, naive rule 0.389, lift 4.50x
  - next: threshold 0.4552, hit rate recent 0.4292 / long run 0.4675
    - 6h: 17 calls (69 a day), hit rate 0.353, chance 0.169, lift 2.09x
    - 24h: 54 calls (54 a day), hit rate 0.444, chance 0.184, lift 2.42x
    - 7d: 698 calls (100 a day), hit rate 0.460, chance 0.191, lift 2.41x
    - 30d: 2082 calls (69 a day), hit rate 0.487, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.411; 0.35: 368, 0.465; 0.40: 298, 0.535; 0.45: 243, 0.594; 0.50: 188, 0.651; 0.55: 143, 0.698; 0.60: 111, 0.740; 0.65: 85, 0.788; 0.70: 63, 0.821; 0.75: 34, 0.864; 0.80: 9, 0.883
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.384; 0.35: 253, 0.422; 0.40: 166, 0.447; 0.45: 85, 0.473; 0.50: 21, 0.514; 0.55: 2, 0.580
- **K=8**: model 1791417600, labels learned 95185, probability skill vs chance 0.1912, widened contest next: True
  - now: threshold 0.5704, hit rate recent 0.6723 / long run 0.7223
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.110, naive rule 0.277, lift 6.36x
    - 24h: 61 calls (61 a day), hit rate 0.672, chance 0.120, naive rule 0.313, lift 5.60x
    - 7d: 393 calls (56 a day), hit rate 0.733, chance 0.124, naive rule 0.334, lift 5.89x
    - 30d: 1563 calls (52 a day), hit rate 0.727, chance 0.121, naive rule 0.325, lift 6.00x
  - next: threshold 0.3473, hit rate recent 0.3945 / long run 0.3999
    - 6h: 25 calls (103 a day), hit rate 0.440, chance 0.110, lift 4.00x
    - 24h: 90 calls (91 a day), hit rate 0.389, chance 0.120, lift 3.24x
    - 7d: 530 calls (76 a day), hit rate 0.400, chance 0.124, lift 3.21x
    - 30d: 2061 calls (69 a day), hit rate 0.402, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 272, 0.401; 0.35: 205, 0.477; 0.40: 158, 0.538; 0.45: 124, 0.586; 0.50: 95, 0.629; 0.55: 67, 0.686; 0.60: 45, 0.731; 0.65: 24, 0.771; 0.70: 8, 0.812; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.347; 0.35: 115, 0.386; 0.40: 48, 0.413; 0.45: 10, 0.427; 0.50: 1, 0.421
- **K=13**: model 1791072000, labels learned 95180, probability skill vs chance 0.1771, widened contest next: True
  - now: threshold 0.4228, hit rate recent 0.5429 / long run 0.581
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.067, naive rule 0.223, lift 10.71x
    - 24h: 48 calls (49 a day), hit rate 0.542, chance 0.074, naive rule 0.256, lift 7.35x
    - 7d: 388 calls (56 a day), hit rate 0.595, chance 0.078, naive rule 0.272, lift 7.67x
    - 30d: 1469 calls (49 a day), hit rate 0.583, chance 0.077, naive rule 0.266, lift 7.61x
  - next: threshold 0.2866, hit rate recent 0.3068 / long run 0.3057
    - 6h: 15 calls (63 a day), hit rate 0.267, chance 0.067, lift 4.00x
    - 24h: 67 calls (68 a day), hit rate 0.313, chance 0.074, lift 4.25x
    - 7d: 548 calls (78 a day), hit rate 0.312, chance 0.078, lift 4.02x
    - 30d: 2035 calls (68 a day), hit rate 0.307, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.438; 0.35: 88, 0.498; 0.40: 63, 0.546; 0.45: 43, 0.604; 0.50: 27, 0.625; 0.55: 14, 0.681; 0.60: 6, 0.704; 0.65: 1, 0.767
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.314; 0.35: 16, 0.347; 0.40: 3, 0.337; 0.45: 1, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.971 | 0.02% | 0.917 | 0.450 | 0.250 | 0.534 | -0.042 |
| 6h | 14.439 | 1.34% | 0.886 | 0.472 | 0.251 | 0.483 | 0.420 |
| 24h | 13.496 | 3.18% | 0.900 | 0.489 | 0.251 | 0.491 | 0.481 |
| 7d | 10.933 | 4.62% | 0.900 | 0.498 | 0.251 | 0.493 | 0.638 |
| 30d | 14.181 | 4.24% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.974 | 12.994 | 13.049 | 12.970 | 13.133 | 13.117 | 13.066 | 13.051 | 12.998 | 12.971 |
| 6h | 14.635 | 14.493 | 14.468 | 14.407 | 14.635 | 14.645 | 14.446 | 14.463 | 14.423 | 14.439 |
| 24h | 13.939 | 13.575 | 13.545 | 13.524 | 13.784 | 13.614 | 13.470 | 13.464 | 13.471 | 13.496 |
| 7d | 11.463 | 11.040 | 11.015 | 10.971 | 11.156 | 11.127 | 10.933 | 10.924 | 10.914 | 10.933 |
| 30d | 14.808 | 14.311 | 14.261 | 14.210 | 14.452 | 14.397 | 14.183 | 14.155 | 14.153 | 14.181 |

## Next candle

- candle starting 2026-10-08 06:36 UTC, last close 2556.43
- P(up) 0.4818, return quantiles (bp): {'05': -9.557, '10': -7.372, '25': -3.908, '40': -1.703, '50': -0.25, '60': 1.147, '75': 3.677, '90': 6.861, '95': 8.731}
- changepoint probability 0.0395, regime age 95.2 min
- agent weights: empirical 0.009, ewma 0.105, garch 0.164, har 0.209, bocpd 0.029, hmm 0.051, online_qr 0.216, lgbm 0.217

## Learning log

- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.75, 4.19, 12.48], current probabilities: [0.0, 0.845, 0.155]
- live generator: {'versions': 60, 'latest_effective': '2026-10-08 06:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.289, 'l_abs': 0.679, 'l_hi': 0.719, 'l_lo': 0.741, 'b05': 0.684, 'b25': 0.613, 'b75': 0.581, 'b95': 0.603}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.66, 1.918, 2.657, 3.356, 3.202, 3.136, 4.626, 4.539, 4.794, 5.457, 6.44, 5.839, 4.872, 4.482]}
- calibration offsets (in sigma): {'05': -0.0425, '10': -0.075, '25': -0.0825, '40': -0.08, '50': -0.055, '60': -0.03, '75': 0.0425, '90': -0.015, '95': -0.0875}
