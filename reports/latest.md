# ETH-USD 60s candle generator - report

- generated: 2026-10-14 17:38 UTC
- last closed candle: 2026-10-14 17:38 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.489 (671) [0.448, 0.530] | 0.509 (2875) [0.489, 0.530] | 0.510 (4026) [0.494, 0.526] | 0.508 (1054) [0.473, 0.542] | 0.543 (70) | 0.500 | flat -0.035 (noise 0.034) |
| colour_clear | 0.526 (780) | 0.538 (5463) [0.532, 0.544] | 0.512 (23311) [0.504, 0.520] | 0.508 (32638) [0.502, 0.514] | 0.541 (8400) [0.535, 0.547] | 0.568 (623) | 0.500 | flat +0.018 (noise 0.013) |
| colour_confident | 0.633 (60) | 0.605 (926) [0.583, 0.636] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.517 (60) | 0.500 | flat -0.003 (noise 0.038) |
| colour_next | 0.514 (1433) | 0.523 (9974) [0.519, 0.527] | 0.510 (42868) [0.504, 0.515] | 0.507 (59997) [0.503, 0.512] | 0.527 (15648) [0.521, 0.533] | 0.548 (1054) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.504 (20062) | 0.499 (139636) [0.496, 0.501] | 0.501 (600152) [0.500, 0.503] | 0.500 (839958) [0.499, 0.501] | 0.500 (219072) [0.497, 0.502] | 0.506 (14756) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.714 (7) | 0.676 (250) [0.633, 0.740] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.462 (13) | 0.500 | flat +0.043 (noise 0.052) |
| reversal_k13_next | 0.270 (74) | 0.321 (495) [0.299, 0.343] | 0.316 (2093) [0.302, 0.331] | 0.306 (2932) [0.294, 0.319] | 0.323 (827) [0.307, 0.338] | 0.220 (41) | 0.077 | flat +0.020 (noise 0.028) |
| reversal_k13_now | 0.651 (43) | 0.589 (353) [0.560, 0.621] | 0.592 (1488) [0.572, 0.614] | 0.584 (2066) [0.567, 0.601] | 0.591 (594) [0.562, 0.625] | 0.484 (31) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.539 (165) | 0.566 (664) [0.541, 0.592] | 0.585 (2478) [0.570, 0.600] | 0.584 (3466) [0.571, 0.597] | 0.575 (1026) [0.555, 0.599] | 0.597 (57) | 0.293 | flat -0.021 (noise 0.028) |
| reversal_k3_now | 0.977 (44) | 0.926 (417) [0.915, 0.941] | 0.939 (1717) [0.931, 0.947] | 0.937 (2410) [0.930, 0.945] | 0.926 (647) [0.917, 0.936] | 0.972 (36) | 0.293 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.481 (104) | 0.468 (524) [0.440, 0.488] | 0.484 (2110) [0.466, 0.502] | 0.484 (2911) [0.469, 0.500] | 0.462 (921) [0.439, 0.486] | 0.519 (77) | 0.187 | flat +0.004 (noise 0.029) |
| reversal_k5_now | 0.804 (46) | 0.809 (367) [0.784, 0.836] | 0.832 (1586) [0.816, 0.848] | 0.833 (2208) [0.819, 0.846] | 0.821 (597) [0.796, 0.845] | 0.783 (23) | 0.188 | flat -0.033 (noise 0.028) |
| reversal_k8_next | 0.407 (81) | 0.387 (607) [0.363, 0.414] | 0.411 (2117) [0.394, 0.429] | 0.396 (3040) [0.383, 0.410] | 0.395 (934) [0.375, 0.416] | 0.375 (48) | 0.122 | flat -0.013 (noise 0.030) |
| reversal_k8_now | 0.674 (46) | 0.669 (393) [0.639, 0.703] | 0.717 (1590) [0.696, 0.738] | 0.709 (2217) [0.692, 0.726] | 0.697 (630) [0.665, 0.730] | 0.655 (29) | 0.122 | flat -0.065 (noise 0.033) |
| overall | 0.506 (22194) | 0.502 (154101) [0.499, 0.505] | 0.504 (661074) [0.503, 0.505] | 0.503 (925231) [0.502, 0.504] | 0.503 (241950) [0.501, 0.506] | 0.510 (16222) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07641, 0.1185] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5253, 'levels': [{'threshold': 0.07641, 'calls_per_day': 142.1, 'win_rate': 0.6}, {'threshold': 0.1185, 'calls_per_day': 35.6, 'win_rate': 0.6627}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 15565, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15233 | 0.334 | 0.519 (14984) | 0.597 (1218) | 0.778 (2447) |
| volatility: normal | 15232 | 0.361 | 0.511 (15168) | 0.606 (279) | 0.775 (2135) |
| volatility: wild | 15233 | 0.374 | 0.501 (15188) | 0.663 (104) | 0.771 (2115) |
| session: Asia 00-08 | 15360 | 0.353 | 0.515 (15251) | 0.605 (575) | 0.777 (2211) |
| session: Europe 08-13 | 9600 | 0.350 | 0.509 (9517) | 0.582 (407) | 0.778 (1470) |
| session: US 13-21 | 15158 | 0.366 | 0.508 (15057) | 0.583 (391) | 0.779 (2181) |
| session: late 21-24 | 5580 | 0.349 | 0.509 (5515) | 0.667 (228) | 0.751 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.368 | 0.377 | 0.322 | 0.322 | 0.433 | 0.242 | 0.493 | 1.024 |
| 6h | 360 | 0.387 | 0.374 | 0.302 | 0.345 | 0.524 | 0.272 | 0.502 | 1.303 |
| 24h | 1440 | 0.375 | 0.357 | 0.288 | 0.325 | 0.534 | 0.271 | 0.479 | 1.062 |
| 7d | 10080 | 0.357 | 0.349 | 0.273 | 0.302 | 0.525 | 0.259 | 0.455 | 1.251 |
| 30d | 43200 | 0.357 | 0.355 | 0.279 | 0.309 | 0.511 | 0.249 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.368 / 0.433 / 0.967; 2: 0.408 / 0.583 / 1.000; 3: 0.383 / 0.467 / 0.967; 4: 0.353 / 0.433 / 0.933; 5: 0.405 / 0.550 / 0.983; 6: 0.400 / 0.550 / 1.000; 7: 0.373 / 0.483 / 1.000; 8: 0.388 / 0.517 / 1.000; 9: 0.409 / 0.533 / 1.000; 10: 0.401 / 0.550 / 1.000; 11: 0.403 / 0.583 / 1.000; 12: 0.380 / 0.450 / 1.000; 13: 0.365 / 0.433 / 1.000; 14: 0.402 / 0.500 / 1.000; 15: 0.424 / 0.600 / 1.000
- 6h: 1: 0.387 / 0.524 / 0.928; 2: 0.370 / 0.504 / 0.944; 3: 0.375 / 0.487 / 0.922; 4: 0.374 / 0.496 / 0.919; 5: 0.373 / 0.487 / 0.925; 6: 0.380 / 0.543 / 0.931; 7: 0.368 / 0.485 / 0.931; 8: 0.376 / 0.493 / 0.922; 9: 0.382 / 0.504 / 0.922; 10: 0.390 / 0.538 / 0.919; 11: 0.376 / 0.518 / 0.925; 12: 0.366 / 0.471 / 0.922; 13: 0.356 / 0.454 / 0.922; 14: 0.365 / 0.485 / 0.925; 15: 0.393 / 0.552 / 0.922
- 24h: 1: 0.375 / 0.534 / 0.909; 2: 0.360 / 0.502 / 0.903; 3: 0.362 / 0.494 / 0.905; 4: 0.365 / 0.503 / 0.912; 5: 0.364 / 0.516 / 0.908; 6: 0.364 / 0.516 / 0.901; 7: 0.359 / 0.493 / 0.901; 8: 0.359 / 0.494 / 0.897; 9: 0.362 / 0.499 / 0.896; 10: 0.365 / 0.520 / 0.894; 11: 0.358 / 0.501 / 0.897; 12: 0.358 / 0.491 / 0.896; 13: 0.360 / 0.509 / 0.896; 14: 0.359 / 0.497 / 0.898; 15: 0.365 / 0.521 / 0.901
- 7d: 1: 0.357 / 0.525 / 0.901; 2: 0.346 / 0.499 / 0.903; 3: 0.348 / 0.511 / 0.902; 4: 0.345 / 0.496 / 0.902; 5: 0.347 / 0.507 / 0.901; 6: 0.345 / 0.501 / 0.901; 7: 0.344 / 0.501 / 0.900; 8: 0.344 / 0.500 / 0.900; 9: 0.342 / 0.493 / 0.900; 10: 0.345 / 0.507 / 0.900; 11: 0.341 / 0.492 / 0.900; 12: 0.343 / 0.501 / 0.900; 13: 0.343 / 0.501 / 0.900; 14: 0.342 / 0.502 / 0.899; 15: 0.345 / 0.502 / 0.900
- 30d: 1: 0.357 / 0.511 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.157 (body 0.102, range 0.213); 'price stays where it was' would score 0.165; colour right 0.467; typical miss of the close 8.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.136 (body 0.091, range 0.181); 'price stays where it was' would score 0.141; colour right 0.493; typical miss of the close 17.8 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.128 (body 0.085, range 0.170); 'price stays where it was' would score 0.134; colour right 0.505; typical miss of the close 9.1 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.2 bp; chain ended on the right side 0.505 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.124; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.512 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.0; 2: 0.198 / 4.5; 3: 0.165 / 6.0; 4: 0.133 / 6.7; 5: 0.120 / 7.4; 6: 0.108 / 8.0; 7: 0.101 / 8.3; 8: 0.094 / 8.6; 9: 0.086 / 8.8; 10: 0.082 / 9.6; 11: 0.077 / 10.3; 12: 0.074 / 10.8; 13: 0.062 / 10.9; 14: 0.064 / 11.2; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 104492, probability skill vs chance 0.2303, widened contest next: False
  - now: threshold 0.8423, hit rate recent 0.9514 / long run 0.9336
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.276, naive rule 0.473, lift 3.26x
    - 24h: 47 calls (47 a day), hit rate 0.957, chance 0.295, naive rule 0.489, lift 3.24x
    - 7d: 420 calls (60 a day), hit rate 0.929, chance 0.295, naive rule 0.498, lift 3.15x
    - 30d: 1719 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.482, lift 3.23x
  - next: threshold 0.5649, hit rate recent 0.5725 / long run 0.5775
    - 6h: 15 calls (61 a day), hit rate 0.600, chance 0.276, lift 2.17x
    - 24h: 82 calls (82 a day), hit rate 0.573, chance 0.295, lift 1.94x
    - 7d: 682 calls (97 a day), hit rate 0.575, chance 0.295, lift 1.95x
    - 30d: 2479 calls (83 a day), hit rate 0.584, chance 0.290, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.491; 0.35: 539, 0.514; 0.40: 484, 0.562; 0.45: 415, 0.630; 0.50: 362, 0.684; 0.55: 318, 0.726; 0.60: 271, 0.770; 0.65: 224, 0.801; 0.70: 180, 0.834; 0.75: 139, 0.872; 0.80: 96, 0.913; 0.85: 49, 0.949; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.460; 0.40: 410, 0.489; 0.45: 315, 0.524; 0.50: 204, 0.560; 0.55: 92, 0.583; 0.60: 14, 0.600; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 104490, probability skill vs chance 0.2161, widened contest next: True
  - now: threshold 0.7036, hit rate recent 0.7917 / long run 0.8244
    - 6h: 6 calls (24 a day), hit rate 0.833, chance 0.183, naive rule 0.376, lift 4.56x
    - 24h: 33 calls (33 a day), hit rate 0.758, chance 0.176, naive rule 0.379, lift 4.31x
    - 7d: 354 calls (51 a day), hit rate 0.808, chance 0.188, naive rule 0.404, lift 4.29x
    - 30d: 1576 calls (53 a day), hit rate 0.829, chance 0.187, naive rule 0.392, lift 4.44x
  - next: threshold 0.4276, hit rate recent 0.5161 / long run 0.4808
    - 6h: 37 calls (151 a day), hit rate 0.541, chance 0.183, lift 2.96x
    - 24h: 95 calls (95 a day), hit rate 0.495, chance 0.176, lift 2.81x
    - 7d: 560 calls (80 a day), hit rate 0.480, chance 0.188, lift 2.55x
    - 30d: 2146 calls (72 a day), hit rate 0.486, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 425, 0.417; 0.35: 356, 0.478; 0.40: 287, 0.550; 0.45: 235, 0.606; 0.50: 183, 0.659; 0.55: 139, 0.705; 0.60: 109, 0.747; 0.65: 82, 0.789; 0.70: 60, 0.820; 0.75: 33, 0.865; 0.80: 9, 0.894
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.388; 0.35: 251, 0.425; 0.40: 162, 0.455; 0.45: 79, 0.474; 0.50: 19, 0.510; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 104487, probability skill vs chance 0.2056, widened contest next: True
  - now: threshold 0.5846, hit rate recent 0.6545 / long run 0.6984
    - 6h: 6 calls (25 a day), hit rate 0.333, chance 0.106, naive rule 0.278, lift 3.15x
    - 24h: 42 calls (42 a day), hit rate 0.619, chance 0.123, naive rule 0.327, lift 5.02x
    - 7d: 379 calls (54 a day), hit rate 0.665, chance 0.123, naive rule 0.343, lift 5.39x
    - 30d: 1579 calls (53 a day), hit rate 0.712, chance 0.122, naive rule 0.330, lift 5.83x
  - next: threshold 0.3721, hit rate recent 0.3832 / long run 0.3971
    - 6h: 20 calls (82 a day), hit rate 0.350, chance 0.106, lift 3.31x
    - 24h: 63 calls (63 a day), hit rate 0.365, chance 0.123, lift 2.96x
    - 7d: 587 calls (84 a day), hit rate 0.394, chance 0.123, lift 3.19x
    - 30d: 2115 calls (71 a day), hit rate 0.409, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 262, 0.413; 0.35: 198, 0.487; 0.40: 152, 0.547; 0.45: 120, 0.590; 0.50: 92, 0.633; 0.55: 66, 0.683; 0.60: 45, 0.724; 0.65: 24, 0.775; 0.70: 9, 0.832; 0.75: 1, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 181, 0.352; 0.35: 109, 0.390; 0.40: 45, 0.423; 0.45: 10, 0.461; 0.50: 1, 0.378
- **K=13**: model 1791849600, labels learned 104482, probability skill vs chance 0.18, widened contest next: True
  - now: threshold 0.4363, hit rate recent 0.5433 / long run 0.5815
    - 6h: 9 calls (38 a day), hit rate 0.222, chance 0.065, naive rule 0.191, lift 3.41x
    - 24h: 42 calls (42 a day), hit rate 0.476, chance 0.076, naive rule 0.267, lift 6.25x
    - 7d: 349 calls (50 a day), hit rate 0.579, chance 0.079, naive rule 0.284, lift 7.36x
    - 30d: 1479 calls (49 a day), hit rate 0.585, chance 0.078, naive rule 0.272, lift 7.53x
  - next: threshold 0.3007, hit rate recent 0.2471 / long run 0.3068
    - 6h: 16 calls (67 a day), hit rate 0.125, chance 0.065, lift 1.92x
    - 24h: 55 calls (56 a day), hit rate 0.218, chance 0.076, lift 2.87x
    - 7d: 490 calls (70 a day), hit rate 0.312, chance 0.079, lift 3.97x
    - 30d: 2075 calls (69 a day), hit rate 0.312, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.450; 0.35: 85, 0.509; 0.40: 61, 0.561; 0.45: 41, 0.613; 0.50: 25, 0.647; 0.55: 14, 0.704; 0.60: 4, 0.756; 0.65: 1, 0.882
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.326; 0.35: 13, 0.361; 0.40: 2, 0.414; 0.45: 0, 0.333

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.928 | 1.03% | 0.967 | 0.433 | 0.252 | 0.433 | 0.167 |
| 6h | 26.310 | 8.19% | 0.919 | 0.481 | 0.251 | 0.485 | 0.460 |
| 24h | 15.513 | 5.13% | 0.903 | 0.499 | 0.251 | 0.462 | 0.615 |
| 7d | 13.184 | 4.41% | 0.900 | 0.500 | 0.251 | 0.491 | 0.681 |
| 30d | 14.037 | 4.07% | 0.900 | 0.500 | 0.251 | 0.496 | 0.686 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.104 | 16.847 | 16.855 | 17.028 | 16.967 | 17.093 | 16.940 | 16.859 | 16.909 | 16.928 |
| 6h | 28.658 | 26.404 | 26.541 | 26.208 | 26.725 | 26.794 | 26.322 | 26.319 | 26.255 | 26.310 |
| 24h | 16.352 | 15.608 | 15.612 | 15.502 | 15.743 | 15.665 | 15.502 | 15.483 | 15.480 | 15.513 |
| 7d | 13.792 | 13.295 | 13.278 | 13.209 | 13.440 | 13.381 | 13.186 | 13.150 | 13.162 | 13.184 |
| 30d | 14.633 | 14.160 | 14.121 | 14.064 | 14.298 | 14.230 | 14.035 | 14.009 | 14.010 | 14.037 |

## Next candle

- candle starting 2026-10-14 17:38 UTC, last close 2435.06
- P(up) 0.4899, return quantiles (bp): {'05': -9.809, '10': -7.178, '25': -4.133, '40': -1.632, '50': -0.151, '60': 1.364, '75': 3.736, '90': 7.561, '95': 9.694}
- changepoint probability 0.0682, regime age 82.4 min
- agent weights: empirical 0.003, ewma 0.094, garch 0.068, har 0.297, bocpd 0.022, hmm 0.025, online_qr 0.226, lgbm 0.265

## Learning log

- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- HMM volatility states (sd, bp per minute): [2.03, 4.75, 13.0], current probabilities: [0.112, 0.875, 0.013]
- live generator: {'versions': 60, 'latest_effective': '2026-10-14 17:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.403, 'l_abs': 0.697, 'l_hi': 0.729, 'l_lo': 0.709, 'b05': 0.756, 'b25': 0.626, 'b75': 0.713, 'b95': 0.75}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.225, 1.564, 1.81, 2.153, 2.316, 2.361, 2.685, 2.97, 3.014, 3.043, 3.185, 3.527, 3.742, 3.729]}
- calibration offsets (in sigma): {'05': 0.0685, '10': 0.047, '25': -0.0375, '40': -0.032, '50': -0.025, '60': -0.008, '75': -0.0125, '90': -0.007, '95': -0.0585}
