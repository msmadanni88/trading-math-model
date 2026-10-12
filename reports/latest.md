# ETH-USD 60s candle generator - report

- generated: 2026-10-12 23:50 UTC
- last closed candle: 2026-10-12 23:50 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.453 (95) | 0.482 (670) [0.439, 0.525] | 0.508 (2874) [0.487, 0.527] | 0.510 (3834) [0.493, 0.526] | 0.505 (862) [0.462, 0.548] | 0.526 (95) | 0.500 | flat -0.045 (noise 0.036) |
| colour_clear | 0.531 (718) | 0.541 (5407) [0.533, 0.549] | 0.511 (23135) [0.503, 0.519] | 0.507 (31040) [0.500, 0.513] | 0.543 (6802) [0.536, 0.550] | 0.536 (814) | 0.500 | up +0.034 (noise 0.012) |
| colour_confident | 0.602 (196) | 0.602 (1076) [0.569, 0.646] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.574 (61) | 0.500 | flat -0.017 (noise 0.030) |
| colour_next | 0.529 (1419) | 0.527 (9960) [0.520, 0.535] | 0.509 (42822) [0.504, 0.515] | 0.507 (57130) [0.502, 0.511] | 0.529 (12781) [0.522, 0.536] | 0.524 (1424) | 0.500 | flat +0.015 (noise 0.008) |
| colour_path | 0.499 (19866) | 0.499 (139440) [0.496, 0.502] | 0.501 (599508) [0.500, 0.502] | 0.500 (799820) [0.499, 0.501] | 0.499 (178934) [0.496, 0.502] | 0.502 (19936) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.661 (65) | 0.660 (282) [0.605, 0.725] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 0.667 (15) | 0.500 | flat +0.007 (noise 0.053) |
| reversal_k13_next | 0.373 (67) | 0.329 (492) [0.312, 0.347] | 0.314 (2061) [0.300, 0.331] | 0.308 (2785) [0.295, 0.321] | 0.332 (680) [0.319, 0.346] | 0.292 (72) | 0.077 | flat +0.040 (noise 0.028) |
| reversal_k13_now | 0.588 (51) | 0.573 (386) [0.546, 0.601] | 0.585 (1499) [0.564, 0.609] | 0.584 (1968) [0.566, 0.602] | 0.593 (496) [0.562, 0.632] | 0.527 (55) | 0.077 | flat -0.012 (noise 0.036) |
| reversal_k3_next | 0.605 (86) | 0.592 (519) [0.557, 0.624] | 0.589 (2389) [0.574, 0.604] | 0.586 (3227) [0.574, 0.599] | 0.582 (787) [0.556, 0.609] | 0.581 (74) | 0.294 | flat +0.002 (noise 0.028) |
| reversal_k3_now | 0.914 (70) | 0.922 (424) [0.913, 0.934] | 0.938 (1738) [0.930, 0.946] | 0.937 (2308) [0.930, 0.944] | 0.923 (545) [0.915, 0.932] | 0.914 (58) | 0.294 | flat -0.019 (noise 0.018) |
| reversal_k5_next | 0.492 (61) | 0.470 (421) [0.438, 0.500] | 0.485 (2076) [0.467, 0.504] | 0.484 (2720) [0.468, 0.501] | 0.456 (730) [0.430, 0.489] | 0.483 (87) | 0.188 | flat +0.013 (noise 0.030) |
| reversal_k5_now | 0.840 (50) | 0.816 (369) [0.787, 0.845] | 0.837 (1601) [0.822, 0.852] | 0.835 (2109) [0.821, 0.848] | 0.827 (498) [0.800, 0.853] | 0.774 (53) | 0.188 | flat -0.038 (noise 0.027) |
| reversal_k8_next | 0.357 (84) | 0.380 (610) [0.357, 0.404] | 0.406 (2114) [0.388, 0.426] | 0.394 (2880) [0.381, 0.410] | 0.390 (774) [0.367, 0.415] | 0.430 (79) | 0.122 | flat -0.020 (noise 0.031) |
| reversal_k8_now | 0.683 (60) | 0.684 (418) [0.648, 0.724] | 0.721 (1600) [0.700, 0.741] | 0.712 (2115) [0.694, 0.729] | 0.705 (528) [0.667, 0.742] | 0.643 (56) | 0.122 | flat -0.045 (noise 0.033) |
| overall | 0.503 (21909) | 0.503 (153709) [0.499, 0.506] | 0.504 (660282) [0.502, 0.505] | 0.503 (880896) [0.502, 0.504] | 0.503 (197615) [0.500, 0.506] | 0.505 (21989) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08029, 0.1221] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.526, 'levels': [{'threshold': 0.08029, 'calls_per_day': 143.9, 'win_rate': 0.5927}, {'threshold': 0.1221, 'calls_per_day': 36.0, 'win_rate': 0.6588}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 13070, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15357 | 0.331 | 0.520 (15080) | 0.595 (1150) | 0.775 (2515) |
| volatility: normal | 15356 | 0.358 | 0.508 (15286) | 0.625 (248) | 0.780 (2206) |
| volatility: wild | 15357 | 0.374 | 0.499 (15312) | 0.687 (83) | 0.772 (2115) |
| session: Asia 00-08 | 15360 | 0.352 | 0.513 (15241) | 0.602 (530) | 0.773 (2223) |
| session: Europe 08-13 | 9600 | 0.347 | 0.506 (9508) | 0.590 (361) | 0.777 (1509) |
| session: US 13-21 | 15360 | 0.364 | 0.506 (15250) | 0.591 (379) | 0.781 (2264) |
| session: late 21-24 | 5750 | 0.349 | 0.511 (5679) | 0.663 (211) | 0.762 (840) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.358 | 0.371 | 0.339 | 0.339 | 0.467 | 0.220 | 0.497 | 1.231 |
| 6h | 360 | 0.359 | 0.353 | 0.297 | 0.300 | 0.479 | 0.243 | 0.475 | 1.031 |
| 24h | 1440 | 0.364 | 0.355 | 0.280 | 0.308 | 0.525 | 0.258 | 0.470 | 1.090 |
| 7d | 10080 | 0.353 | 0.346 | 0.273 | 0.300 | 0.523 | 0.256 | 0.450 | 1.223 |
| 30d | 43200 | 0.355 | 0.353 | 0.278 | 0.307 | 0.510 | 0.248 | 0.462 | 1.299 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.358 / 0.467 / 0.900; 2: 0.394 / 0.567 / 0.750; 3: 0.361 / 0.517 / 0.750; 4: 0.374 / 0.483 / 0.717; 5: 0.353 / 0.433 / 0.717; 6: 0.386 / 0.567 / 0.800; 7: 0.368 / 0.517 / 0.717; 8: 0.342 / 0.467 / 0.733; 9: 0.330 / 0.417 / 0.767; 10: 0.352 / 0.467 / 0.733; 11: 0.341 / 0.467 / 0.717; 12: 0.338 / 0.467 / 0.650; 13: 0.360 / 0.517 / 0.567; 14: 0.346 / 0.533 / 0.550; 15: 0.359 / 0.533 / 0.633
- 6h: 1: 0.359 / 0.479 / 0.911; 2: 0.363 / 0.529 / 0.806; 3: 0.357 / 0.496 / 0.769; 4: 0.350 / 0.504 / 0.789; 5: 0.352 / 0.482 / 0.733; 6: 0.357 / 0.535 / 0.772; 7: 0.357 / 0.499 / 0.731; 8: 0.347 / 0.504 / 0.747; 9: 0.354 / 0.493 / 0.764; 10: 0.346 / 0.479 / 0.778; 11: 0.344 / 0.462 / 0.767; 12: 0.353 / 0.521 / 0.739; 13: 0.343 / 0.485 / 0.700; 14: 0.339 / 0.490 / 0.708; 15: 0.346 / 0.493 / 0.742
- 24h: 1: 0.364 / 0.525 / 0.910; 2: 0.357 / 0.502 / 0.882; 3: 0.362 / 0.523 / 0.880; 4: 0.348 / 0.479 / 0.879; 5: 0.358 / 0.500 / 0.874; 6: 0.355 / 0.501 / 0.880; 7: 0.360 / 0.514 / 0.870; 8: 0.352 / 0.493 / 0.876; 9: 0.358 / 0.517 / 0.875; 10: 0.357 / 0.518 / 0.878; 11: 0.350 / 0.482 / 0.873; 12: 0.357 / 0.525 / 0.877; 13: 0.352 / 0.499 / 0.870; 14: 0.347 / 0.491 / 0.869; 15: 0.352 / 0.481 / 0.871
- 7d: 1: 0.353 / 0.523 / 0.899; 2: 0.343 / 0.497 / 0.899; 3: 0.345 / 0.510 / 0.897; 4: 0.341 / 0.496 / 0.898; 5: 0.343 / 0.504 / 0.897; 6: 0.339 / 0.495 / 0.898; 7: 0.339 / 0.497 / 0.896; 8: 0.339 / 0.495 / 0.898; 9: 0.337 / 0.490 / 0.898; 10: 0.340 / 0.504 / 0.896; 11: 0.338 / 0.493 / 0.897; 12: 0.339 / 0.498 / 0.896; 13: 0.339 / 0.502 / 0.896; 14: 0.338 / 0.502 / 0.896; 15: 0.338 / 0.494 / 0.896
- 30d: 1: 0.355 / 0.510 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.510 / 0.899; 4: 0.348 / 0.498 / 0.899; 5: 0.349 / 0.504 / 0.899; 6: 0.347 / 0.501 / 0.899; 7: 0.347 / 0.504 / 0.899; 8: 0.347 / 0.503 / 0.899; 9: 0.344 / 0.495 / 0.899; 10: 0.346 / 0.504 / 0.899; 11: 0.345 / 0.501 / 0.899; 12: 0.345 / 0.504 / 0.899; 13: 0.345 / 0.502 / 0.898; 14: 0.344 / 0.497 / 0.898; 15: 0.343 / 0.496 / 0.898

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.111 (body 0.076, range 0.146); 'price stays where it was' would score 0.119; colour right 0.400; typical miss of the close 20.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.105 (body 0.074, range 0.135); 'price stays where it was' would score 0.102; colour right 0.496; typical miss of the close 9.8 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.121 (body 0.082, range 0.159); 'price stays where it was' would score 0.119; colour right 0.494; typical miss of the close 8.9 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.118 (body 0.081, range 0.156); 'price stays where it was' would score 0.125; colour right 0.494; typical miss of the close 6.5 bp; chain ended on the right side 0.496 of 671 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.124; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.510 of 2874 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 3.9; 2: 0.197 / 4.4; 3: 0.164 / 5.9; 4: 0.132 / 6.5; 5: 0.119 / 7.2; 6: 0.108 / 7.7; 7: 0.101 / 8.2; 8: 0.093 / 8.4; 9: 0.087 / 8.6; 10: 0.082 / 9.4; 11: 0.076 / 10.0; 12: 0.074 / 10.5; 13: 0.063 / 10.8; 14: 0.063 / 11.0; 15: 0.059 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 101984, probability skill vs chance 0.2341, widened contest next: False
  - now: threshold 0.8418, hit rate recent 0.907 / long run 0.9277
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.263, naive rule 0.463, lift 2.66x
    - 24h: 58 calls (58 a day), hit rate 0.914, chance 0.277, naive rule 0.471, lift 3.30x
    - 7d: 434 calls (62 a day), hit rate 0.917, chance 0.297, naive rule 0.500, lift 3.09x
    - 30d: 1726 calls (58 a day), hit rate 0.939, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5178, hit rate recent 0.6087 / long run 0.5875
    - 6h: 33 calls (134 a day), hit rate 0.606, chance 0.263, lift 2.30x
    - 24h: 75 calls (75 a day), hit rate 0.587, chance 0.277, lift 2.12x
    - 7d: 544 calls (78 a day), hit rate 0.585, chance 0.297, lift 1.97x
    - 30d: 2388 calls (80 a day), hit rate 0.588, chance 0.291, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.493; 0.35: 538, 0.516; 0.40: 484, 0.562; 0.45: 416, 0.630; 0.50: 363, 0.684; 0.55: 318, 0.726; 0.60: 271, 0.769; 0.65: 224, 0.801; 0.70: 180, 0.833; 0.75: 139, 0.873; 0.80: 97, 0.913; 0.85: 49, 0.949; 0.90: 3, 0.976
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 497, 0.460; 0.40: 412, 0.489; 0.45: 316, 0.524; 0.50: 206, 0.558; 0.55: 91, 0.583; 0.60: 14, 0.605; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 101982, probability skill vs chance 0.2264, widened contest next: True
  - now: threshold 0.6844, hit rate recent 0.7835 / long run 0.8277
    - 6h: 13 calls (53 a day), hit rate 0.462, chance 0.180, naive rule 0.397, lift 2.57x
    - 24h: 53 calls (53 a day), hit rate 0.774, chance 0.179, naive rule 0.393, lift 4.33x
    - 7d: 378 calls (54 a day), hit rate 0.804, chance 0.191, naive rule 0.408, lift 4.20x
    - 30d: 1588 calls (53 a day), hit rate 0.834, chance 0.187, naive rule 0.392, lift 4.46x
  - next: threshold 0.4356, hit rate recent 0.4784 / long run 0.4746
    - 6h: 23 calls (94 a day), hit rate 0.435, chance 0.180, lift 2.42x
    - 24h: 87 calls (87 a day), hit rate 0.483, chance 0.179, lift 2.70x
    - 7d: 469 calls (67 a day), hit rate 0.467, chance 0.191, lift 2.44x
    - 30d: 2086 calls (70 a day), hit rate 0.483, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 426, 0.417; 0.35: 359, 0.476; 0.40: 290, 0.546; 0.45: 237, 0.604; 0.50: 184, 0.659; 0.55: 139, 0.705; 0.60: 109, 0.748; 0.65: 84, 0.793; 0.70: 62, 0.824; 0.75: 34, 0.868; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 252, 0.426; 0.40: 163, 0.454; 0.45: 81, 0.475; 0.50: 19, 0.518; 0.55: 2, 0.544
- **K=8**: model 1791417600, labels learned 101979, probability skill vs chance 0.2126, widened contest next: True
  - now: threshold 0.5862, hit rate recent 0.6544 / long run 0.7028
    - 6h: 13 calls (53 a day), hit rate 0.462, chance 0.123, naive rule 0.336, lift 3.76x
    - 24h: 56 calls (56 a day), hit rate 0.643, chance 0.120, naive rule 0.344, lift 5.36x
    - 7d: 413 calls (59 a day), hit rate 0.666, chance 0.123, naive rule 0.343, lift 5.43x
    - 30d: 1592 calls (53 a day), hit rate 0.718, chance 0.122, naive rule 0.330, lift 5.88x
  - next: threshold 0.3689, hit rate recent 0.4207 / long run 0.3981
    - 6h: 22 calls (91 a day), hit rate 0.455, chance 0.123, lift 3.70x
    - 24h: 79 calls (80 a day), hit rate 0.430, chance 0.120, lift 3.59x
    - 7d: 615 calls (88 a day), hit rate 0.389, chance 0.123, lift 3.17x
    - 30d: 2132 calls (71 a day), hit rate 0.409, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 265, 0.410; 0.35: 200, 0.485; 0.40: 154, 0.544; 0.45: 121, 0.590; 0.50: 92, 0.636; 0.55: 66, 0.688; 0.60: 45, 0.730; 0.65: 24, 0.775; 0.70: 9, 0.825; 0.75: 1, 0.850
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 182, 0.352; 0.35: 111, 0.389; 0.40: 47, 0.419; 0.45: 10, 0.445; 0.50: 1, 0.357
- **K=13**: model 1791504000, labels learned 101974, probability skill vs chance 0.1816, widened contest next: True
  - now: threshold 0.4355, hit rate recent 0.5507 / long run 0.582
    - 6h: 15 calls (63 a day), hit rate 0.467, chance 0.077, naive rule 0.301, lift 6.08x
    - 24h: 55 calls (56 a day), hit rate 0.527, chance 0.074, naive rule 0.281, lift 7.12x
    - 7d: 373 calls (53 a day), hit rate 0.568, chance 0.078, naive rule 0.281, lift 7.27x
    - 30d: 1493 calls (50 a day), hit rate 0.586, chance 0.078, naive rule 0.271, lift 7.55x
  - next: threshold 0.2869, hit rate recent 0.3201 / long run 0.3192
    - 6h: 20 calls (83 a day), hit rate 0.350, chance 0.077, lift 4.56x
    - 24h: 72 calls (73 a day), hit rate 0.292, chance 0.074, lift 3.94x
    - 7d: 491 calls (70 a day), hit rate 0.330, chance 0.078, lift 4.22x
    - 30d: 2091 calls (70 a day), hit rate 0.315, chance 0.078, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.448; 0.35: 86, 0.509; 0.40: 61, 0.559; 0.45: 42, 0.614; 0.50: 26, 0.641; 0.55: 14, 0.695; 0.60: 5, 0.741; 0.65: 1, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.329; 0.35: 14, 0.349; 0.40: 3, 0.333; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 30.398 | 10.21% | 0.900 | 0.467 | 0.251 | 0.467 | 0.443 |
| 6h | 15.716 | 5.21% | 0.908 | 0.489 | 0.250 | 0.507 | 0.625 |
| 24h | 14.820 | 3.38% | 0.904 | 0.491 | 0.251 | 0.486 | 0.551 |
| 7d | 11.819 | 4.57% | 0.900 | 0.499 | 0.251 | 0.491 | 0.655 |
| 30d | 13.787 | 4.13% | 0.900 | 0.499 | 0.251 | 0.497 | 0.690 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 33.854 | 30.960 | 30.592 | 30.734 | 31.462 | 31.334 | 30.688 | 30.382 | 30.543 | 30.398 |
| 6h | 16.579 | 15.903 | 15.821 | 15.730 | 16.186 | 15.974 | 15.757 | 15.705 | 15.723 | 15.716 |
| 24h | 15.339 | 14.947 | 14.948 | 14.860 | 15.087 | 15.023 | 14.842 | 14.778 | 14.805 | 14.820 |
| 7d | 12.385 | 11.935 | 11.886 | 11.855 | 12.031 | 12.013 | 11.824 | 11.793 | 11.800 | 11.819 |
| 30d | 14.381 | 13.911 | 13.871 | 13.815 | 14.045 | 13.992 | 13.785 | 13.760 | 13.761 | 13.787 |

## Next candle

- candle starting 2026-10-12 23:50 UTC, last close 2445.56
- P(up) 0.486, return quantiles (bp): {'05': -16.45, '10': -12.602, '25': -6.615, '40': -2.461, '50': -0.255, '60': 1.611, '75': 4.923, '90': 9.558, '95': 12.601}
- changepoint probability 0.0275, regime age 36.4 min
- agent weights: empirical 0.003, ewma 0.059, garch 0.077, har 0.218, bocpd 0.009, hmm 0.025, online_qr 0.225, lgbm 0.385

## Learning log

- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- HMM volatility states (sd, bp per minute): [2.02, 4.61, 13.8], current probabilities: [0.005, 0.294, 0.701]
- live generator: {'versions': 60, 'latest_effective': '2026-10-13 00:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.36, 'l_abs': 0.67, 'l_hi': 0.745, 'l_lo': 0.638, 'b05': 0.688, 'b25': 0.625, 'b75': 0.7, 'b95': 0.676}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [2.011, 3.014, 3.219, 4.677, 4.203, 5.9, 5.834, 5.839, 5.926, 6.746, 8.121, 10.14, 10.13, 9.134]}
- calibration offsets (in sigma): {'05': -0.0855, '10': -0.081, '25': -0.1075, '40': -0.064, '50': -0.045, '60': -0.046, '75': -0.0325, '90': -0.089, '95': -0.1445}
