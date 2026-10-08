# ETH-USD 60s candle generator - report

- generated: 2026-10-08 19:51 UTC
- last closed candle: 2026-10-08 19:51 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.375 (96) | 0.509 (670) [0.457, 0.558] | 0.507 (2875) [0.486, 0.526] | 0.511 (3451) [0.493, 0.528] | 0.507 (479) [0.438, 0.579] | 0.494 (79) | 0.500 | flat -0.008 (noise 0.040) |
| colour_clear | 0.535 (746) | 0.526 (5210) [0.504, 0.545] | 0.505 (23206) [0.499, 0.512] | 0.503 (27921) [0.497, 0.509] | 0.545 (3683) [0.534, 0.555] | 0.552 (694) | 0.500 | up +0.030 (noise 0.013) |
| colour_confident | 0.613 (111) | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.609 (726) [0.561, 0.654] | 0.576 (59) | 0.500 | - |
| colour_next | 0.524 (1434) | 0.522 (9977) [0.510, 0.534] | 0.506 (42883) [0.501, 0.512] | 0.505 (51457) [0.500, 0.509] | 0.531 (7108) [0.519, 0.544] | 0.525 (1186) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.490 (20076) | 0.500 (139678) [0.495, 0.504] | 0.501 (600362) [0.500, 0.502] | 0.500 (720398) [0.499, 0.502] | 0.499 (99512) [0.494, 0.504] | 0.498 (16604) | 0.500 | flat -0.002 (noise 0.003) |
| colour_strong | 0.733 (30) | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.648 (199) [0.592, 0.713] | 0.385 (13) | 0.500 | - |
| reversal_k13_next | 0.304 (69) | 0.311 (563) [0.291, 0.329] | 0.309 (2032) [0.294, 0.324] | 0.303 (2506) [0.290, 0.318] | 0.322 (401) [0.304, 0.340] | 0.305 (59) | 0.077 | flat +0.034 (noise 0.027) |
| reversal_k13_now | 0.531 (49) | 0.588 (396) [0.553, 0.635] | 0.582 (1484) [0.559, 0.604] | 0.581 (1762) [0.562, 0.601] | 0.583 (290) [0.534, 0.648] | 0.590 (39) | 0.077 | flat +0.010 (noise 0.038) |
| reversal_k3_next | 0.500 (54) | 0.585 (561) [0.555, 0.620] | 0.587 (2373) [0.572, 0.602] | 0.586 (2856) [0.573, 0.600] | 0.579 (416) [0.542, 0.631] | 0.518 (56) | 0.292 | flat +0.014 (noise 0.029) |
| reversal_k3_now | 0.954 (43) | 0.930 (400) [0.920, 0.940] | 0.939 (1691) [0.930, 0.947] | 0.940 (2036) [0.933, 0.948] | 0.930 (273) [0.915, 0.946] | 0.929 (56) | 0.293 | flat -0.025 (noise 0.017) |
| reversal_k5_next | 0.370 (54) | 0.462 (718) [0.431, 0.494] | 0.486 (2077) [0.466, 0.507] | 0.485 (2441) [0.467, 0.503] | 0.444 (451) [0.409, 0.491] | 0.386 (57) | 0.187 | flat -0.011 (noise 0.036) |
| reversal_k5_now | 0.826 (46) | 0.841 (390) [0.815, 0.866] | 0.836 (1570) [0.821, 0.852] | 0.837 (1887) [0.823, 0.851] | 0.837 (276) [0.800, 0.871] | 0.755 (49) | 0.187 | flat -0.018 (noise 0.026) |
| reversal_k8_next | 0.323 (93) | 0.397 (521) [0.365, 0.430] | 0.401 (2054) [0.383, 0.421] | 0.395 (2526) [0.380, 0.412] | 0.391 (420) [0.351, 0.431] | 0.372 (102) | 0.121 | flat +0.017 (noise 0.033) |
| reversal_k8_now | 0.678 (59) | 0.726 (394) [0.692, 0.760] | 0.725 (1572) [0.706, 0.743] | 0.716 (1883) [0.698, 0.735] | 0.730 (296) [0.685, 0.777] | 0.608 (51) | 0.122 | flat -0.029 (noise 0.033) |
| overall | 0.493 (22073) | 0.503 (154268) [0.498, 0.507] | 0.503 (660973) [0.502, 0.505] | 0.503 (793203) [0.501, 0.504] | 0.503 (109922) [0.497, 0.509] | 0.501 (18338) | - | flat -0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07652, 0.1149] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5347, 'levels': [{'threshold': 0.07652, 'calls_per_day': 142.7, 'win_rate': 0.6095}, {'threshold': 0.1149, 'calls_per_day': 35.8, 'win_rate': 0.6482}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 7162, 'rate': 0.5339}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15277 | 0.335 | 0.514 (15063) | 0.608 (630) | 0.778 (2437) |
| volatility: normal | 15277 | 0.361 | 0.509 (15211) | 0.566 (106) | 0.773 (2153) |
| volatility: wild | 15277 | 0.374 | 0.496 (15229) | 0.673 (49) | 0.774 (2133) |
| session: Asia 00-08 | 15360 | 0.353 | 0.507 (15256) | 0.600 (280) | 0.778 (2212) |
| session: Europe 08-13 | 9600 | 0.350 | 0.504 (9538) | 0.577 (156) | 0.769 (1489) |
| session: US 13-21 | 15291 | 0.366 | 0.505 (15191) | 0.603 (214) | 0.779 (2238) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5518) | 0.659 (135) | 0.770 (784) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.411 | 0.401 | 0.346 | 0.346 | 0.567 | 0.308 | 0.514 | 1.286 |
| 6h | 360 | 0.401 | 0.398 | 0.330 | 0.371 | 0.528 | 0.281 | 0.521 | 1.222 |
| 24h | 1440 | 0.376 | 0.367 | 0.301 | 0.332 | 0.521 | 0.267 | 0.484 | 1.110 |
| 7d | 10080 | 0.351 | 0.346 | 0.274 | 0.298 | 0.526 | 0.250 | 0.452 | 1.234 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.290 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.411 / 0.567 / 0.917; 2: 0.395 / 0.500 / 0.967; 3: 0.398 / 0.517 / 0.983; 4: 0.402 / 0.517 / 0.917; 5: 0.440 / 0.650 / 0.883; 6: 0.410 / 0.533 / 0.967; 7: 0.437 / 0.650 / 1.000; 8: 0.384 / 0.500 / 0.933; 9: 0.388 / 0.517 / 0.967; 10: 0.412 / 0.600 / 0.933; 11: 0.373 / 0.450 / 0.983; 12: 0.377 / 0.500 / 1.000; 13: 0.405 / 0.533 / 0.983; 14: 0.431 / 0.650 / 0.983; 15: 0.429 / 0.617 / 0.983
- 6h: 1: 0.401 / 0.528 / 0.922; 2: 0.387 / 0.503 / 0.933; 3: 0.387 / 0.494 / 0.939; 4: 0.382 / 0.497 / 0.881; 5: 0.387 / 0.506 / 0.867; 6: 0.378 / 0.483 / 0.908; 7: 0.387 / 0.514 / 0.922; 8: 0.373 / 0.475 / 0.839; 9: 0.378 / 0.492 / 0.853; 10: 0.376 / 0.500 / 0.850; 11: 0.368 / 0.453 / 0.878; 12: 0.383 / 0.525 / 0.889; 13: 0.372 / 0.492 / 0.883; 14: 0.390 / 0.539 / 0.881; 15: 0.379 / 0.511 / 0.881
- 24h: 1: 0.376 / 0.521 / 0.895; 2: 0.364 / 0.502 / 0.915; 3: 0.365 / 0.505 / 0.907; 4: 0.365 / 0.495 / 0.900; 5: 0.361 / 0.498 / 0.895; 6: 0.360 / 0.497 / 0.902; 7: 0.363 / 0.509 / 0.897; 8: 0.357 / 0.483 / 0.894; 9: 0.354 / 0.483 / 0.896; 10: 0.359 / 0.499 / 0.894; 11: 0.356 / 0.492 / 0.901; 12: 0.357 / 0.493 / 0.903; 13: 0.359 / 0.502 / 0.903; 14: 0.360 / 0.506 / 0.901; 15: 0.359 / 0.496 / 0.899
- 7d: 1: 0.351 / 0.526 / 0.898; 2: 0.343 / 0.504 / 0.900; 3: 0.344 / 0.509 / 0.900; 4: 0.341 / 0.502 / 0.900; 5: 0.338 / 0.496 / 0.900; 6: 0.337 / 0.492 / 0.900; 7: 0.339 / 0.504 / 0.900; 8: 0.336 / 0.490 / 0.898; 9: 0.333 / 0.487 / 0.899; 10: 0.336 / 0.500 / 0.899; 11: 0.337 / 0.501 / 0.899; 12: 0.338 / 0.506 / 0.899; 13: 0.338 / 0.505 / 0.899; 14: 0.337 / 0.499 / 0.898; 15: 0.335 / 0.491 / 0.898
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.148 (body 0.083, range 0.213); 'price stays where it was' would score 0.111; colour right 0.500; typical miss of the close 12.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.080, range 0.170); 'price stays where it was' would score 0.124; colour right 0.478; typical miss of the close 18.9 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.124 (body 0.083, range 0.164); 'price stays where it was' would score 0.120; colour right 0.495; typical miss of the close 10.5 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.115 (body 0.077, range 0.152); 'price stays where it was' would score 0.119; colour right 0.498; typical miss of the close 6.3 bp; chain ended on the right side 0.510 of 670 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.506 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.1; 2: 0.198 / 4.5; 3: 0.167 / 6.1; 4: 0.131 / 6.8; 5: 0.118 / 7.5; 6: 0.110 / 8.2; 7: 0.099 / 8.6; 8: 0.091 / 9.0; 9: 0.086 / 9.2; 10: 0.080 / 10.1; 11: 0.075 / 10.6; 12: 0.074 / 10.9; 13: 0.063 / 11.3; 14: 0.065 / 11.4; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 95985, probability skill vs chance 0.222, widened contest next: True
  - now: threshold 0.8385, hit rate recent 0.9253 / long run 0.9367
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.285, naive rule 0.468, lift 3.16x
    - 24h: 64 calls (64 a day), hit rate 0.938, chance 0.261, naive rule 0.431, lift 3.59x
    - 7d: 395 calls (56 a day), hit rate 0.929, chance 0.291, naive rule 0.485, lift 3.19x
    - 30d: 1686 calls (56 a day), hit rate 0.940, chance 0.291, naive rule 0.481, lift 3.23x
  - next: threshold 0.5613, hit rate recent 0.5167 / long run 0.5784
    - 6h: 18 calls (73 a day), hit rate 0.278, chance 0.285, lift 0.98x
    - 24h: 67 calls (67 a day), hit rate 0.522, chance 0.261, lift 2.00x
    - 7d: 545 calls (78 a day), hit rate 0.574, chance 0.291, lift 1.97x
    - 30d: 2349 calls (78 a day), hit rate 0.589, chance 0.291, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.517; 0.40: 486, 0.561; 0.45: 419, 0.627; 0.50: 367, 0.681; 0.55: 322, 0.724; 0.60: 274, 0.767; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 138, 0.873; 0.80: 96, 0.912; 0.85: 48, 0.949; 0.90: 2, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 497, 0.458; 0.40: 412, 0.488; 0.45: 316, 0.519; 0.50: 206, 0.553; 0.55: 91, 0.587; 0.60: 13, 0.604; 0.65: 1, 0.737
- **K=5**: model 1790208000, labels learned 95983, probability skill vs chance 0.1916, widened contest next: True
  - now: threshold 0.7134, hit rate recent 0.7898 / long run 0.8322
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.181, naive rule 0.349, lift 4.41x
    - 24h: 57 calls (57 a day), hit rate 0.772, chance 0.172, naive rule 0.342, lift 4.48x
    - 7d: 393 calls (56 a day), hit rate 0.830, chance 0.189, naive rule 0.392, lift 4.38x
    - 30d: 1567 calls (52 a day), hit rate 0.833, chance 0.186, naive rule 0.388, lift 4.49x
  - next: threshold 0.4441, hit rate recent 0.3914 / long run 0.4613
    - 6h: 23 calls (94 a day), hit rate 0.304, chance 0.181, lift 1.68x
    - 24h: 67 calls (67 a day), hit rate 0.388, chance 0.172, lift 2.25x
    - 7d: 649 calls (93 a day), hit rate 0.444, chance 0.189, lift 2.35x
    - 30d: 2090 calls (70 a day), hit rate 0.488, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.411; 0.35: 367, 0.466; 0.40: 297, 0.535; 0.45: 242, 0.595; 0.50: 188, 0.652; 0.55: 142, 0.699; 0.60: 110, 0.741; 0.65: 85, 0.787; 0.70: 63, 0.819; 0.75: 34, 0.864; 0.80: 9, 0.884
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 253, 0.423; 0.40: 166, 0.448; 0.45: 85, 0.475; 0.50: 21, 0.514; 0.55: 2, 0.574
- **K=8**: model 1791417600, labels learned 95980, probability skill vs chance 0.1882, widened contest next: True
  - now: threshold 0.5753, hit rate recent 0.6349 / long run 0.714
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.113, naive rule 0.277, lift 5.54x
    - 24h: 66 calls (66 a day), hit rate 0.606, chance 0.112, naive rule 0.284, lift 5.43x
    - 7d: 406 calls (58 a day), hit rate 0.714, chance 0.122, naive rule 0.326, lift 5.83x
    - 30d: 1577 calls (53 a day), hit rate 0.722, chance 0.121, naive rule 0.325, lift 5.96x
  - next: threshold 0.3561, hit rate recent 0.3415 / long run 0.3919
    - 6h: 36 calls (148 a day), hit rate 0.306, chance 0.113, lift 2.71x
    - 24h: 119 calls (120 a day), hit rate 0.370, chance 0.112, lift 3.31x
    - 7d: 580 calls (83 a day), hit rate 0.386, chance 0.122, lift 3.15x
    - 30d: 2087 calls (70 a day), hit rate 0.404, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 272, 0.401; 0.35: 205, 0.477; 0.40: 157, 0.538; 0.45: 124, 0.586; 0.50: 95, 0.629; 0.55: 67, 0.685; 0.60: 46, 0.730; 0.65: 24, 0.770; 0.70: 9, 0.814; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.347; 0.35: 115, 0.387; 0.40: 48, 0.412; 0.45: 10, 0.426; 0.50: 1, 0.410
- **K=13**: model 1791072000, labels learned 95975, probability skill vs chance 0.1772, widened contest next: False
  - now: threshold 0.424, hit rate recent 0.5514 / long run 0.5803
    - 6h: 11 calls (46 a day), hit rate 0.636, chance 0.075, naive rule 0.252, lift 8.44x
    - 24h: 51 calls (52 a day), hit rate 0.529, chance 0.072, naive rule 0.245, lift 7.36x
    - 7d: 386 calls (55 a day), hit rate 0.588, chance 0.078, naive rule 0.270, lift 7.56x
    - 30d: 1476 calls (49 a day), hit rate 0.585, chance 0.077, naive rule 0.266, lift 7.61x
  - next: threshold 0.2899, hit rate recent 0.3017 / long run 0.3059
    - 6h: 18 calls (75 a day), hit rate 0.222, chance 0.075, lift 2.95x
    - 24h: 75 calls (76 a day), hit rate 0.307, chance 0.072, lift 4.26x
    - 7d: 536 calls (77 a day), hit rate 0.310, chance 0.078, lift 3.98x
    - 30d: 2039 calls (68 a day), hit rate 0.308, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.438; 0.35: 88, 0.499; 0.40: 63, 0.547; 0.45: 44, 0.605; 0.50: 27, 0.629; 0.55: 15, 0.680; 0.60: 6, 0.706; 0.65: 1, 0.780
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.317; 0.35: 16, 0.345; 0.40: 3, 0.344; 0.45: 1, 0.368

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 18.057 | 0.69% | 0.917 | 0.517 | 0.250 | 0.517 | 0.298 |
| 6h | 29.128 | 10.34% | 0.925 | 0.519 | 0.249 | 0.528 | 0.643 |
| 24h | 17.328 | 5.96% | 0.894 | 0.498 | 0.251 | 0.500 | 0.723 |
| 7d | 11.307 | 5.18% | 0.900 | 0.501 | 0.251 | 0.495 | 0.677 |
| 30d | 14.301 | 4.37% | 0.900 | 0.500 | 0.251 | 0.497 | 0.693 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 18.182 | 18.165 | 18.147 | 18.147 | 18.108 | 18.436 | 17.801 | 17.980 | 17.964 | 18.057 |
| 6h | 32.487 | 29.513 | 29.263 | 29.140 | 29.568 | 30.402 | 29.099 | 29.132 | 29.091 | 29.128 |
| 24h | 18.426 | 17.473 | 17.393 | 17.303 | 17.559 | 17.810 | 17.321 | 17.343 | 17.307 | 17.328 |
| 7d | 11.924 | 11.426 | 11.393 | 11.346 | 11.533 | 11.548 | 11.311 | 11.300 | 11.290 | 11.307 |
| 30d | 14.954 | 14.434 | 14.382 | 14.330 | 14.574 | 14.527 | 14.302 | 14.275 | 14.273 | 14.301 |

## Next candle

- candle starting 2026-10-08 19:51 UTC, last close 2460.59
- P(up) 0.5169, return quantiles (bp): {'05': -11.263, '10': -7.674, '25': -3.851, '40': -1.277, '50': 0.253, '60': 1.76, '75': 3.781, '90': 6.999, '95': 9.929}
- changepoint probability 0.0545, regime age 53.0 min
- agent weights: empirical 0.003, ewma 0.043, garch 0.119, har 0.292, bocpd 0.028, hmm 0.003, online_qr 0.296, lgbm 0.216

## Learning log

- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- HMM volatility states (sd, bp per minute): [2.0, 4.45, 12.64], current probabilities: [0.013, 0.874, 0.112]
- live generator: {'versions': 60, 'latest_effective': '2026-10-08 20:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.37, 'l_abs': 0.716, 'l_hi': 0.733, 'l_lo': 0.749, 'b05': 0.7, 'b25': 0.647, 'b75': 0.546, 'b95': 0.665}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.193, 1.524, 2.197, 2.614, 2.596, 2.809, 3.531, 3.679, 3.886, 3.77, 3.642, 3.875, 4.365, 4.904]}
- calibration offsets (in sigma): {'05': -0.035, '10': 0.01, '25': -0.015, '40': 0.01, '50': 0.02, '60': 0.04, '75': -0.005, '90': -0.09, '95': -0.055}
