# ETH-USD 60s candle generator - report

- generated: 2026-10-22 00:10 UTC
- last closed candle: 2026-10-22 00:10 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_next 0.434 in the last 7 days, -0.055 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.543 (672) [0.507, 0.580] | 0.520 (2876) [0.500, 0.540] | 0.515 (4794) [0.500, 0.529] | 0.520 (1822) [0.492, 0.545] | - | 0.500 | flat +0.038 (noise 0.027) |
| colour_clear | 0.550 (816) | 0.555 (5596) [0.546, 0.564] | 0.528 (23440) [0.519, 0.537] | 0.516 (39077) [0.509, 0.523] | 0.547 (14839) [0.541, 0.553] | 0.333 (6) | 0.500 | flat +0.014 (noise 0.009) |
| colour_confident | 0.602 (176) | 0.600 (979) [0.581, 0.622] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.602 (2587) [0.585, 0.620] | 0.667 (6) | 0.500 | flat +0.001 (noise 0.023) |
| colour_next | 0.533 (1434) | 0.534 (10023) [0.525, 0.542] | 0.519 (42861) [0.513, 0.525] | 0.512 (71456) [0.507, 0.516] | 0.530 (27107) [0.525, 0.535] | 0.500 (10) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.505 (20076) | 0.500 (140322) [0.497, 0.504] | 0.501 (600054) [0.499, 0.502] | 0.501 (1000384) [0.499, 0.502] | 0.500 (379498) [0.498, 0.502] | 0.414 (140) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.590 (39) | 0.631 (236) [0.595, 0.671] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | 0.645 (668) [0.618, 0.674] | - | 0.500 | flat -0.025 (noise 0.044) |
| reversal_k13_next | 0.333 (60) | 0.324 (460) [0.314, 0.335] | 0.307 (2133) [0.295, 0.319] | 0.308 (3437) [0.297, 0.319] | 0.321 (1332) [0.309, 0.331] | - | 0.077 | flat +0.008 (noise 0.031) |
| reversal_k13_now | 0.596 (47) | 0.525 (396) [0.495, 0.560] | 0.571 (1555) [0.552, 0.591] | 0.574 (2504) [0.558, 0.591] | 0.564 (1032) [0.540, 0.591] | - | 0.077 | flat -0.067 (noise 0.036) |
| reversal_k3_next | 0.657 (146) | 0.577 (817) [0.551, 0.607] | 0.575 (2745) [0.561, 0.589] | 0.582 (4349) [0.572, 0.594] | 0.576 (1909) [0.561, 0.593] | 0.000 (1) | 0.293 | flat +0.003 (noise 0.026) |
| reversal_k3_now | 0.984 (64) | 0.932 (399) [0.906, 0.959] | 0.934 (1701) [0.925, 0.943] | 0.937 (2858) [0.931, 0.944] | 0.931 (1095) [0.920, 0.942] | - | 0.293 | flat +0.003 (noise 0.018) |
| reversal_k5_next | 0.484 (128) | 0.434 (912) [0.415, 0.453] | 0.463 (2571) [0.448, 0.478] | 0.474 (3917) [0.460, 0.488] | 0.453 (1927) [0.436, 0.471] | - | 0.187 | down -0.055 (noise 0.027) |
| reversal_k5_now | 0.796 (54) | 0.817 (376) [0.792, 0.839] | 0.827 (1577) [0.813, 0.842] | 0.831 (2617) [0.819, 0.842] | 0.820 (1006) [0.804, 0.836] | - | 0.187 | flat +0.006 (noise 0.029) |
| reversal_k8_next | 0.404 (104) | 0.365 (777) [0.341, 0.388] | 0.387 (2380) [0.373, 0.401] | 0.390 (3874) [0.377, 0.402] | 0.382 (1768) [0.366, 0.398] | - | 0.121 | flat -0.032 (noise 0.027) |
| reversal_k8_now | 0.729 (48) | 0.667 (333) [0.631, 0.703] | 0.706 (1542) [0.686, 0.726] | 0.704 (2590) [0.688, 0.720] | 0.688 (1003) [0.663, 0.713] | - | 0.121 | flat -0.007 (noise 0.035) |
| overall | 0.509 (22257) | 0.504 (155487) [0.501, 0.507] | 0.504 (661995) [0.502, 0.505] | 0.503 (1102780) [0.502, 0.504] | 0.504 (419499) [0.502, 0.506] | 0.417 (151) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06792, 0.1027] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5335, 'levels': [{'threshold': 0.06792, 'calls_per_day': 146.9, 'win_rate': 0.5764}, {'threshold': 0.1027, 'calls_per_day': 36.4, 'win_rate': 0.6406}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 25979, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14884 | 0.337 | 0.524 (14638) | 0.588 (1498) | 0.763 (2443) |
| volatility: normal | 14883 | 0.365 | 0.520 (14822) | 0.623 (774) | 0.755 (2170) |
| volatility: wild | 14883 | 0.379 | 0.510 (14847) | 0.617 (321) | 0.775 (1990) |
| session: Asia 00-08 | 14890 | 0.359 | 0.524 (14795) | 0.612 (934) | 0.764 (2183) |
| session: Europe 08-13 | 9300 | 0.356 | 0.520 (9217) | 0.597 (635) | 0.768 (1469) |
| session: US 13-21 | 14880 | 0.368 | 0.513 (14778) | 0.578 (635) | 0.770 (2130) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5517) | 0.625 (389) | 0.743 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.378 | 0.383 | 0.274 | 0.274 | 0.517 | 0.263 | 0.492 | 0.950 |
| 6h | 360 | 0.372 | 0.363 | 0.279 | 0.301 | 0.522 | 0.260 | 0.483 | 1.154 |
| 24h | 1440 | 0.373 | 0.365 | 0.285 | 0.323 | 0.533 | 0.266 | 0.480 | 1.209 |
| 7d | 10080 | 0.369 | 0.360 | 0.276 | 0.308 | 0.533 | 0.266 | 0.472 | 1.220 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.519 | 0.254 | 0.466 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.378 / 0.517 / 0.867; 2: 0.342 / 0.350 / 0.900; 3: 0.367 / 0.500 / 0.917; 4: 0.400 / 0.600 / 0.850; 5: 0.362 / 0.500 / 0.883; 6: 0.381 / 0.533 / 0.883; 7: 0.357 / 0.467 / 0.850; 8: 0.337 / 0.367 / 0.883; 9: 0.378 / 0.450 / 0.917; 10: 0.366 / 0.450 / 0.900; 11: 0.362 / 0.450 / 0.917; 12: 0.341 / 0.450 / 0.967; 13: 0.365 / 0.483 / 0.967; 14: 0.399 / 0.550 / 0.967; 15: 0.369 / 0.533 / 0.983
- 6h: 1: 0.372 / 0.522 / 0.903; 2: 0.363 / 0.478 / 0.897; 3: 0.367 / 0.528 / 0.886; 4: 0.358 / 0.494 / 0.878; 5: 0.360 / 0.503 / 0.864; 6: 0.361 / 0.494 / 0.861; 7: 0.361 / 0.511 / 0.872; 8: 0.358 / 0.489 / 0.861; 9: 0.360 / 0.483 / 0.872; 10: 0.359 / 0.522 / 0.867; 11: 0.343 / 0.439 / 0.872; 12: 0.348 / 0.486 / 0.892; 13: 0.350 / 0.483 / 0.897; 14: 0.369 / 0.536 / 0.908; 15: 0.356 / 0.528 / 0.919
- 24h: 1: 0.373 / 0.533 / 0.893; 2: 0.358 / 0.482 / 0.901; 3: 0.360 / 0.515 / 0.899; 4: 0.360 / 0.504 / 0.896; 5: 0.366 / 0.530 / 0.894; 6: 0.360 / 0.493 / 0.894; 7: 0.363 / 0.510 / 0.894; 8: 0.362 / 0.517 / 0.890; 9: 0.357 / 0.495 / 0.892; 10: 0.359 / 0.513 / 0.896; 11: 0.352 / 0.478 / 0.894; 12: 0.353 / 0.490 / 0.898; 13: 0.358 / 0.512 / 0.899; 14: 0.359 / 0.508 / 0.903; 15: 0.357 / 0.522 / 0.906
- 7d: 1: 0.369 / 0.533 / 0.896; 2: 0.355 / 0.494 / 0.900; 3: 0.358 / 0.505 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.354 / 0.500 / 0.899; 6: 0.353 / 0.495 / 0.899; 7: 0.353 / 0.498 / 0.899; 8: 0.353 / 0.502 / 0.898; 9: 0.353 / 0.501 / 0.898; 10: 0.355 / 0.511 / 0.898; 11: 0.349 / 0.496 / 0.898; 12: 0.352 / 0.505 / 0.898; 13: 0.351 / 0.499 / 0.898; 14: 0.351 / 0.505 / 0.898; 15: 0.349 / 0.500 / 0.898
- 30d: 1: 0.360 / 0.519 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.347 / 0.502 / 0.899; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.092 (body 0.056, range 0.128); 'price stays where it was' would score 0.083; colour right 0.383; typical miss of the close 10.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.122 (body 0.085, range 0.160); 'price stays where it was' would score 0.122; colour right 0.483; typical miss of the close 9.8 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.138 (body 0.092, range 0.183); 'price stays where it was' would score 0.137; colour right 0.523; typical miss of the close 8.6 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.133; colour right 0.506; typical miss of the close 9.1 bp; chain ended on the right side 0.543 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.500; typical miss of the close 7.7 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 3.8; 2: 0.198 / 4.5; 3: 0.165 / 6.0; 4: 0.133 / 6.5; 5: 0.119 / 7.2; 6: 0.109 / 7.7; 7: 0.104 / 8.1; 8: 0.096 / 8.4; 9: 0.088 / 8.3; 10: 0.086 / 9.1; 11: 0.082 / 9.6; 12: 0.079 / 9.9; 13: 0.068 / 10.2; 14: 0.068 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 114964, probability skill vs chance 0.2194, widened contest next: False
  - now: threshold 0.8357, hit rate recent 0.9634 / long run 0.9347
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.307, naive rule 0.474, lift 3.26x
    - 24h: 64 calls (64 a day), hit rate 0.984, chance 0.309, naive rule 0.511, lift 3.18x
    - 7d: 399 calls (57 a day), hit rate 0.932, chance 0.291, naive rule 0.482, lift 3.20x
    - 30d: 1699 calls (57 a day), hit rate 0.933, chance 0.293, naive rule 0.485, lift 3.19x
  - next: threshold 0.528, hit rate recent 0.5997 / long run 0.581
    - 6h: 34 calls (138 a day), hit rate 0.618, chance 0.307, lift 2.01x
    - 24h: 147 calls (148 a day), hit rate 0.653, chance 0.309, lift 2.11x
    - 7d: 817 calls (117 a day), hit rate 0.575, chance 0.291, lift 1.97x
    - 30d: 2745 calls (92 a day), hit rate 0.574, chance 0.293, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.492; 0.35: 541, 0.515; 0.40: 482, 0.568; 0.45: 412, 0.639; 0.50: 360, 0.691; 0.55: 314, 0.733; 0.60: 268, 0.777; 0.65: 224, 0.805; 0.70: 178, 0.838; 0.75: 138, 0.871; 0.80: 93, 0.911; 0.85: 48, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.425; 0.35: 499, 0.461; 0.40: 406, 0.493; 0.45: 310, 0.525; 0.50: 201, 0.558; 0.55: 91, 0.568; 0.60: 14, 0.611; 0.65: 1, 0.700
- **K=5**: model 1792540800, labels learned 114962, probability skill vs chance 0.2112, widened contest next: False
  - now: threshold 0.6838, hit rate recent 0.81 / long run 0.8223
    - 6h: 14 calls (57 a day), hit rate 0.714, chance 0.207, naive rule 0.406, lift 3.45x
    - 24h: 53 calls (53 a day), hit rate 0.792, chance 0.192, naive rule 0.411, lift 4.14x
    - 7d: 376 calls (54 a day), hit rate 0.816, chance 0.186, naive rule 0.396, lift 4.39x
    - 30d: 1576 calls (53 a day), hit rate 0.827, chance 0.188, naive rule 0.395, lift 4.40x
  - next: threshold 0.4195, hit rate recent 0.4529 / long run 0.4465
    - 6h: 28 calls (114 a day), hit rate 0.500, chance 0.207, lift 2.42x
    - 24h: 128 calls (129 a day), hit rate 0.484, chance 0.192, lift 2.53x
    - 7d: 911 calls (130 a day), hit rate 0.434, chance 0.186, lift 2.33x
    - 30d: 2570 calls (86 a day), hit rate 0.462, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 347, 0.491; 0.40: 278, 0.562; 0.45: 226, 0.618; 0.50: 178, 0.668; 0.55: 136, 0.711; 0.60: 106, 0.755; 0.65: 78, 0.790; 0.70: 56, 0.824; 0.75: 32, 0.867; 0.80: 10, 0.896
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 250, 0.419; 0.40: 157, 0.446; 0.45: 72, 0.461; 0.50: 16, 0.494; 0.55: 1, 0.488
- **K=8**: model 1792540800, labels learned 114959, probability skill vs chance 0.2038, widened contest next: False
  - now: threshold 0.5661, hit rate recent 0.6853 / long run 0.6869
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.101, naive rule 0.279, lift 6.57x
    - 24h: 48 calls (48 a day), hit rate 0.729, chance 0.116, naive rule 0.324, lift 6.28x
    - 7d: 333 calls (48 a day), hit rate 0.667, chance 0.117, naive rule 0.314, lift 5.72x
    - 30d: 1541 calls (51 a day), hit rate 0.705, chance 0.121, naive rule 0.328, lift 5.82x
  - next: threshold 0.3407, hit rate recent 0.3911 / long run 0.377
    - 6h: 20 calls (82 a day), hit rate 0.350, chance 0.101, lift 3.45x
    - 24h: 104 calls (105 a day), hit rate 0.404, chance 0.116, lift 3.48x
    - 7d: 776 calls (111 a day), hit rate 0.365, chance 0.117, lift 3.13x
    - 30d: 2379 calls (79 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.422; 0.35: 193, 0.492; 0.40: 147, 0.547; 0.45: 114, 0.593; 0.50: 88, 0.633; 0.55: 64, 0.678; 0.60: 42, 0.724; 0.65: 23, 0.788; 0.70: 10, 0.839; 0.75: 1, 0.800
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 102, 0.380; 0.40: 40, 0.405; 0.45: 8, 0.429; 0.50: 1, 0.531
- **K=13**: model 1792454400, labels learned 114954, probability skill vs chance 0.1844, widened contest next: False
  - now: threshold 0.4356, hit rate recent 0.5552 / long run 0.556
    - 6h: 11 calls (46 a day), hit rate 0.545, chance 0.075, naive rule 0.275, lift 7.24x
    - 24h: 46 calls (46 a day), hit rate 0.587, chance 0.072, naive rule 0.270, lift 8.16x
    - 7d: 396 calls (57 a day), hit rate 0.525, chance 0.076, naive rule 0.266, lift 6.93x
    - 30d: 1554 calls (52 a day), hit rate 0.571, chance 0.077, naive rule 0.271, lift 7.37x
  - next: threshold 0.294, hit rate recent 0.3203 / long run 0.3167
    - 6h: 10 calls (42 a day), hit rate 0.200, chance 0.075, lift 2.65x
    - 24h: 60 calls (61 a day), hit rate 0.333, chance 0.072, lift 4.63x
    - 7d: 459 calls (66 a day), hit rate 0.322, chance 0.076, lift 4.26x
    - 30d: 2132 calls (71 a day), hit rate 0.307, chance 0.077, lift 3.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.449; 0.35: 86, 0.502; 0.40: 61, 0.551; 0.45: 41, 0.609; 0.50: 25, 0.656; 0.55: 14, 0.706; 0.60: 6, 0.750; 0.65: 1, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.318; 0.35: 13, 0.351; 0.40: 2, 0.441; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.362 | 0.46% | 0.867 | 0.450 | 0.250 | 0.533 | 0.307 |
| 6h | 13.622 | 1.99% | 0.908 | 0.492 | 0.251 | 0.500 | 0.616 |
| 24h | 15.491 | 3.05% | 0.900 | 0.497 | 0.250 | 0.510 | 0.607 |
| 7d | 16.017 | 4.14% | 0.900 | 0.500 | 0.251 | 0.499 | 0.658 |
| 30d | 13.600 | 4.09% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.425 | 13.478 | 13.459 | 13.220 | 13.484 | 13.486 | 13.378 | 13.315 | 13.335 | 13.362 |
| 6h | 13.898 | 13.725 | 13.660 | 13.613 | 13.823 | 13.750 | 13.605 | 13.572 | 13.584 | 13.622 |
| 24h | 15.978 | 15.617 | 15.580 | 15.547 | 15.759 | 15.625 | 15.481 | 15.436 | 15.469 | 15.491 |
| 7d | 16.709 | 16.201 | 16.097 | 16.039 | 16.265 | 16.212 | 16.014 | 15.993 | 15.986 | 16.017 |
| 30d | 14.179 | 13.723 | 13.682 | 13.622 | 13.845 | 13.786 | 13.596 | 13.575 | 13.574 | 13.600 |

## Next candle

- candle starting 2026-10-22 00:10 UTC, last close 2479.11
- P(up) 0.4709, return quantiles (bp): {'05': -7.376, '10': -5.996, '25': -3.286, '40': -1.281, '50': -0.342, '60': 0.854, '75': 2.788, '90': 5.735, '95': 7.63}
- changepoint probability 0.0763, regime age 171.3 min
- agent weights: empirical 0.008, ewma 0.072, garch 0.099, har 0.163, bocpd 0.027, hmm 0.066, online_qr 0.230, lgbm 0.336

## Learning log

- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.56, 5.88, 15.56], current probabilities: [0.174, 0.818, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-10-22 00:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.402, 'l_abs': 0.675, 'l_hi': 0.746, 'l_lo': 0.782, 'b05': 0.699, 'b25': 0.674, 'b75': 0.661, 'b95': 0.686}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.348, 1.688, 2.115, 2.466, 2.933, 3.174, 3.683, 3.761, 3.893, 4.011, 3.649, 3.882, 3.802, 3.64]}
- calibration offsets (in sigma): {'05': 0.0245, '10': -0.051, '25': -0.0575, '40': -0.034, '50': -0.065, '60': -0.026, '75': -0.0325, '90': -0.019, '95': -0.0145}
