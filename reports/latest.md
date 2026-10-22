# ETH-USD 60s candle generator - report

- generated: 2026-10-22 09:42 UTC
- last closed candle: 2026-10-22 09:42 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k5_next 0.434 in the last 7 days, -0.055 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.543 (672) [0.507, 0.580] | 0.520 (2876) [0.500, 0.540] | 0.515 (4794) [0.500, 0.529] | 0.520 (1822) [0.492, 0.545] | 0.447 (38) | 0.500 | flat +0.038 (noise 0.027) |
| colour_clear | 0.550 (816) | 0.555 (5596) [0.546, 0.564] | 0.528 (23440) [0.519, 0.537] | 0.516 (39077) [0.509, 0.523] | 0.547 (14839) [0.541, 0.553] | 0.512 (328) | 0.500 | flat +0.014 (noise 0.009) |
| colour_confident | 0.602 (176) | 0.600 (979) [0.581, 0.622] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.571 (56) | 0.500 | flat +0.001 (noise 0.023) |
| colour_next | 0.533 (1434) | 0.534 (10023) [0.525, 0.542] | 0.519 (42861) [0.513, 0.525] | 0.512 (71456) [0.507, 0.516] | 0.530 (27107) [0.525, 0.535] | 0.528 (581) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.505 (20076) | 0.500 (140322) [0.497, 0.504] | 0.501 (600054) [0.499, 0.502] | 0.501 (1000384) [0.499, 0.502] | 0.500 (379498) [0.498, 0.502] | 0.490 (8134) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.590 (39) | 0.631 (236) [0.595, 0.671] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.800 (5) | 0.500 | flat -0.025 (noise 0.044) |
| reversal_k13_next | 0.333 (60) | 0.324 (460) [0.314, 0.335] | 0.307 (2133) [0.295, 0.319] | 0.308 (3437) [0.297, 0.319] | 0.321 (1332) [0.309, 0.331] | 0.130 (23) | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.596 (47) | 0.525 (396) [0.495, 0.560] | 0.571 (1555) [0.552, 0.591] | 0.574 (2504) [0.558, 0.591] | 0.564 (1032) [0.540, 0.591] | 0.500 (14) | 0.077 | flat -0.067 (noise 0.036) |
| reversal_k3_next | 0.657 (146) | 0.577 (817) [0.551, 0.607] | 0.575 (2745) [0.561, 0.589] | 0.582 (4349) [0.572, 0.594] | 0.576 (1909) [0.561, 0.593] | 0.558 (52) | 0.293 | flat +0.003 (noise 0.026) |
| reversal_k3_now | 0.984 (64) | 0.932 (399) [0.906, 0.959] | 0.934 (1701) [0.925, 0.943] | 0.937 (2858) [0.931, 0.944] | 0.931 (1095) [0.920, 0.942] | 0.864 (22) | 0.293 | flat +0.003 (noise 0.018) |
| reversal_k5_next | 0.484 (128) | 0.434 (912) [0.415, 0.453] | 0.463 (2571) [0.448, 0.478] | 0.474 (3917) [0.460, 0.488] | 0.453 (1927) [0.436, 0.471] | 0.458 (48) | 0.187 | down -0.055 (noise 0.027) |
| reversal_k5_now | 0.796 (54) | 0.817 (376) [0.792, 0.839] | 0.827 (1577) [0.813, 0.842] | 0.831 (2617) [0.819, 0.842] | 0.820 (1006) [0.804, 0.836] | 0.750 (16) | 0.187 | flat +0.006 (noise 0.029) |
| reversal_k8_next | 0.404 (104) | 0.365 (777) [0.341, 0.388] | 0.387 (2380) [0.373, 0.401] | 0.390 (3874) [0.377, 0.402] | 0.382 (1768) [0.366, 0.398] | 0.239 (46) | 0.121 | flat -0.032 (noise 0.027) |
| reversal_k8_now | 0.729 (48) | 0.667 (333) [0.631, 0.703] | 0.706 (1542) [0.686, 0.726] | 0.704 (2590) [0.688, 0.720] | 0.688 (1003) [0.663, 0.713] | 0.588 (17) | 0.121 | flat -0.007 (noise 0.035) |
| overall | 0.509 (22257) | 0.504 (155487) [0.501, 0.507] | 0.504 (661995) [0.502, 0.505] | 0.503 (1102780) [0.502, 0.504] | 0.504 (419499) [0.502, 0.506] | 0.492 (8991) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06839, 0.1029] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5332, 'levels': [{'threshold': 0.06839, 'calls_per_day': 147.6, 'win_rate': 0.5756}, {'threshold': 0.1029, 'calls_per_day': 35.9, 'win_rate': 0.6403}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 26550, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15074 | 0.337 | 0.523 (14828) | 0.588 (1512) | 0.765 (2466) |
| volatility: normal | 15074 | 0.365 | 0.521 (15012) | 0.620 (802) | 0.755 (2188) |
| volatility: wild | 15074 | 0.379 | 0.510 (15038) | 0.617 (329) | 0.771 (2018) |
| session: Asia 00-08 | 15360 | 0.359 | 0.524 (15264) | 0.609 (978) | 0.763 (2233) |
| session: Europe 08-13 | 9402 | 0.355 | 0.520 (9319) | 0.598 (641) | 0.765 (1488) |
| session: US 13-21 | 14880 | 0.368 | 0.513 (14778) | 0.578 (635) | 0.770 (2130) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5517) | 0.625 (389) | 0.743 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.332 | 0.385 | 0.252 | 0.252 | 0.467 | 0.209 | 0.455 | 1.397 |
| 6h | 360 | 0.352 | 0.351 | 0.255 | 0.278 | 0.528 | 0.238 | 0.465 | 1.199 |
| 24h | 1440 | 0.369 | 0.362 | 0.278 | 0.311 | 0.534 | 0.262 | 0.476 | 1.189 |
| 7d | 10080 | 0.368 | 0.359 | 0.275 | 0.306 | 0.534 | 0.266 | 0.471 | 1.217 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.519 | 0.254 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.332 / 0.467 / 0.917; 2: 0.364 / 0.583 / 0.900; 3: 0.322 / 0.400 / 0.917; 4: 0.356 / 0.600 / 0.883; 5: 0.329 / 0.450 / 0.883; 6: 0.346 / 0.483 / 0.917; 7: 0.355 / 0.517 / 0.933; 8: 0.332 / 0.433 / 0.967; 9: 0.374 / 0.633 / 0.983; 10: 0.335 / 0.433 / 0.983; 11: 0.359 / 0.550 / 0.967; 12: 0.343 / 0.483 / 0.983; 13: 0.325 / 0.467 / 0.950; 14: 0.329 / 0.500 / 0.983; 15: 0.352 / 0.517 / 0.983
- 6h: 1: 0.352 / 0.528 / 0.889; 2: 0.355 / 0.542 / 0.889; 3: 0.336 / 0.467 / 0.914; 4: 0.353 / 0.514 / 0.883; 5: 0.344 / 0.506 / 0.908; 6: 0.343 / 0.475 / 0.939; 7: 0.350 / 0.525 / 0.944; 8: 0.346 / 0.522 / 0.947; 9: 0.350 / 0.522 / 0.956; 10: 0.334 / 0.472 / 0.947; 11: 0.337 / 0.475 / 0.953; 12: 0.330 / 0.461 / 0.936; 13: 0.333 / 0.450 / 0.925; 14: 0.339 / 0.481 / 0.931; 15: 0.338 / 0.494 / 0.922
- 24h: 1: 0.369 / 0.534 / 0.902; 2: 0.363 / 0.502 / 0.901; 3: 0.355 / 0.493 / 0.905; 4: 0.356 / 0.499 / 0.902; 5: 0.355 / 0.501 / 0.907; 6: 0.358 / 0.496 / 0.914; 7: 0.363 / 0.519 / 0.913; 8: 0.356 / 0.507 / 0.912; 9: 0.358 / 0.510 / 0.912; 10: 0.352 / 0.498 / 0.908; 11: 0.349 / 0.480 / 0.911; 12: 0.347 / 0.484 / 0.910; 13: 0.347 / 0.481 / 0.906; 14: 0.354 / 0.496 / 0.907; 15: 0.349 / 0.510 / 0.900
- 7d: 1: 0.368 / 0.534 / 0.896; 2: 0.355 / 0.493 / 0.900; 3: 0.357 / 0.502 / 0.900; 4: 0.353 / 0.495 / 0.899; 5: 0.353 / 0.498 / 0.900; 6: 0.353 / 0.493 / 0.901; 7: 0.352 / 0.498 / 0.901; 8: 0.353 / 0.503 / 0.900; 9: 0.352 / 0.502 / 0.900; 10: 0.354 / 0.507 / 0.900; 11: 0.348 / 0.494 / 0.901; 12: 0.352 / 0.503 / 0.901; 13: 0.350 / 0.495 / 0.901; 14: 0.351 / 0.503 / 0.901; 15: 0.348 / 0.498 / 0.901
- 30d: 1: 0.360 / 0.519 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.901; 10: 0.348 / 0.506 / 0.901; 11: 0.346 / 0.499 / 0.901; 12: 0.347 / 0.502 / 0.901; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.143 (body 0.106, range 0.180); 'price stays where it was' would score 0.148; colour right 0.450; typical miss of the close 11.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.153 (body 0.110, range 0.196); 'price stays where it was' would score 0.167; colour right 0.494; typical miss of the close 7.9 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.135 (body 0.093, range 0.176); 'price stays where it was' would score 0.139; colour right 0.493; typical miss of the close 9.7 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.169); 'price stays where it was' would score 0.133; colour right 0.504; typical miss of the close 8.8 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.162); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 3.8; 2: 0.198 / 4.5; 3: 0.166 / 6.0; 4: 0.133 / 6.5; 5: 0.121 / 7.1; 6: 0.110 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.3; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.079 / 9.8; 13: 0.068 / 10.1; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 115536, probability skill vs chance 0.2126, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9344 / long run 0.9322
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.307, naive rule 0.535, lift 3.08x
    - 24h: 63 calls (63 a day), hit rate 0.952, chance 0.300, naive rule 0.499, lift 3.17x
    - 7d: 404 calls (58 a day), hit rate 0.931, chance 0.292, naive rule 0.484, lift 3.19x
    - 30d: 1704 calls (57 a day), hit rate 0.934, chance 0.293, naive rule 0.486, lift 3.19x
  - next: threshold 0.546, hit rate recent 0.5919 / long run 0.5801
    - 6h: 31 calls (126 a day), hit rate 0.645, chance 0.307, lift 2.10x
    - 24h: 135 calls (135 a day), hit rate 0.593, chance 0.300, lift 1.98x
    - 7d: 837 calls (120 a day), hit rate 0.577, chance 0.292, lift 1.98x
    - 30d: 2768 calls (92 a day), hit rate 0.575, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.492; 0.35: 541, 0.515; 0.40: 482, 0.569; 0.45: 412, 0.640; 0.50: 360, 0.692; 0.55: 314, 0.734; 0.60: 267, 0.777; 0.65: 223, 0.805; 0.70: 177, 0.838; 0.75: 137, 0.871; 0.80: 93, 0.911; 0.85: 48, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.425; 0.35: 499, 0.461; 0.40: 406, 0.494; 0.45: 310, 0.526; 0.50: 201, 0.558; 0.55: 91, 0.568; 0.60: 14, 0.614; 0.65: 1, 0.710
- **K=5**: model 1792540800, labels learned 115534, probability skill vs chance 0.2093, widened contest next: False
  - now: threshold 0.6841, hit rate recent 0.7958 / long run 0.8204
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.201, naive rule 0.422, lift 4.14x
    - 24h: 50 calls (50 a day), hit rate 0.800, chance 0.190, naive rule 0.401, lift 4.21x
    - 7d: 374 calls (53 a day), hit rate 0.818, chance 0.186, naive rule 0.396, lift 4.41x
    - 30d: 1567 calls (52 a day), hit rate 0.826, chance 0.188, naive rule 0.396, lift 4.40x
  - next: threshold 0.4015, hit rate recent 0.4605 / long run 0.4475
    - 6h: 29 calls (118 a day), hit rate 0.517, chance 0.201, lift 2.57x
    - 24h: 119 calls (120 a day), hit rate 0.445, chance 0.190, lift 2.34x
    - 7d: 910 calls (130 a day), hit rate 0.434, chance 0.186, lift 2.34x
    - 30d: 2598 calls (87 a day), hit rate 0.463, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 346, 0.491; 0.40: 278, 0.562; 0.45: 225, 0.619; 0.50: 177, 0.668; 0.55: 136, 0.711; 0.60: 105, 0.754; 0.65: 78, 0.789; 0.70: 56, 0.823; 0.75: 32, 0.867; 0.80: 10, 0.898
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 250, 0.419; 0.40: 157, 0.445; 0.45: 71, 0.462; 0.50: 16, 0.497; 0.55: 1, 0.488
- **K=8**: model 1792540800, labels learned 115531, probability skill vs chance 0.1961, widened contest next: True
  - now: threshold 0.5657, hit rate recent 0.6607 / long run 0.6841
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.111, naive rule 0.312, lift 5.98x
    - 24h: 45 calls (45 a day), hit rate 0.711, chance 0.107, naive rule 0.291, lift 6.67x
    - 7d: 333 calls (48 a day), hit rate 0.661, chance 0.116, naive rule 0.313, lift 5.69x
    - 30d: 1538 calls (51 a day), hit rate 0.704, chance 0.121, naive rule 0.327, lift 5.82x
  - next: threshold 0.3399, hit rate recent 0.3095 / long run 0.3668
    - 6h: 25 calls (103 a day), hit rate 0.240, chance 0.111, lift 2.15x
    - 24h: 102 calls (103 a day), hit rate 0.333, chance 0.107, lift 3.13x
    - 7d: 787 calls (113 a day), hit rate 0.357, chance 0.116, lift 3.07x
    - 30d: 2408 calls (80 a day), hit rate 0.383, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 253, 0.421; 0.35: 192, 0.491; 0.40: 147, 0.545; 0.45: 114, 0.592; 0.50: 87, 0.633; 0.55: 63, 0.677; 0.60: 42, 0.722; 0.65: 24, 0.787; 0.70: 10, 0.841; 0.75: 1, 0.818
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.349; 0.35: 102, 0.378; 0.40: 39, 0.402; 0.45: 8, 0.427; 0.50: 1, 0.531
- **K=13**: model 1792454400, labels learned 115526, probability skill vs chance 0.1813, widened contest next: True
  - now: threshold 0.4239, hit rate recent 0.543 / long run 0.5547
    - 6h: 9 calls (38 a day), hit rate 0.556, chance 0.065, naive rule 0.261, lift 8.52x
    - 24h: 44 calls (44 a day), hit rate 0.568, chance 0.067, naive rule 0.252, lift 8.52x
    - 7d: 387 calls (55 a day), hit rate 0.525, chance 0.075, naive rule 0.265, lift 6.99x
    - 30d: 1549 calls (52 a day), hit rate 0.570, chance 0.077, naive rule 0.271, lift 7.37x
  - next: threshold 0.2945, hit rate recent 0.2585 / long run 0.3097
    - 6h: 13 calls (54 a day), hit rate 0.154, chance 0.065, lift 2.36x
    - 24h: 51 calls (52 a day), hit rate 0.216, chance 0.067, lift 3.24x
    - 7d: 463 calls (66 a day), hit rate 0.315, chance 0.075, lift 4.20x
    - 30d: 2135 calls (71 a day), hit rate 0.305, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.449; 0.35: 86, 0.501; 0.40: 61, 0.552; 0.45: 41, 0.609; 0.50: 25, 0.659; 0.55: 14, 0.707; 0.60: 6, 0.751; 0.65: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.316; 0.35: 13, 0.352; 0.40: 2, 0.466; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 17.696 | 1.17% | 0.900 | 0.533 | 0.250 | 0.550 | 0.214 |
| 6h | 14.842 | 0.95% | 0.892 | 0.522 | 0.251 | 0.506 | 0.424 |
| 24h | 16.558 | 2.72% | 0.903 | 0.502 | 0.250 | 0.521 | 0.576 |
| 7d | 15.385 | 3.98% | 0.899 | 0.500 | 0.250 | 0.499 | 0.658 |
| 30d | 13.567 | 4.08% | 0.900 | 0.500 | 0.251 | 0.496 | 0.669 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.906 | 18.069 | 17.998 | 17.626 | 18.445 | 17.801 | 17.584 | 17.694 | 17.694 | 17.696 |
| 6h | 14.984 | 14.957 | 14.948 | 14.790 | 15.142 | 14.954 | 14.793 | 14.849 | 14.830 | 14.842 |
| 24h | 17.021 | 16.722 | 16.689 | 16.589 | 16.872 | 16.704 | 16.545 | 16.512 | 16.542 | 16.558 |
| 7d | 16.022 | 15.533 | 15.478 | 15.411 | 15.637 | 15.548 | 15.378 | 15.363 | 15.361 | 15.385 |
| 30d | 14.144 | 13.691 | 13.651 | 13.590 | 13.813 | 13.754 | 13.564 | 13.543 | 13.542 | 13.567 |

## Next candle

- candle starting 2026-10-22 09:42 UTC, last close 2397.13
- P(up) 0.4823, return quantiles (bp): {'05': -10.04, '10': -8.01, '25': -4.224, '40': -1.284, '50': -0.172, '60': 0.832, '75': 2.995, '90': 6.75, '95': 8.847}
- changepoint probability 0.0414, regime age 92.3 min
- agent weights: empirical 0.027, ewma 0.068, garch 0.084, har 0.212, bocpd 0.021, hmm 0.081, online_qr 0.263, lgbm 0.242

## Learning log

- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.56, 5.88, 15.56], current probabilities: [0.071, 0.909, 0.02]
- live generator: {'versions': 60, 'latest_effective': '2026-10-22 09:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.289, 'l_abs': 0.644, 'l_hi': 0.769, 'l_lo': 0.783, 'b05': 0.717, 'b25': 0.639, 'b75': 0.687, 'b95': 0.681}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.454, 1.491, 2.107, 2.093, 1.997, 2.119, 2.363, 2.412, 2.599, 2.625, 2.802, 3.103, 3.163, 3.414]}
- calibration offsets (in sigma): {'05': -0.0695, '10': -0.119, '25': -0.0775, '40': -0.016, '50': -0.035, '60': -0.064, '75': -0.0825, '90': -0.081, '95': -0.1005}
