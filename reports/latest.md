# ETH-USD 60s candle generator - report

- generated: 2026-11-03 03:39 UTC
- last closed candle: 2026-11-03 03:39 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.498 (672) [0.476, 0.521] | 0.517 (2878) [0.498, 0.536] | 0.514 (5946) [0.501, 0.527] | 0.517 (2974) [0.499, 0.536] | 0.429 (14) | 0.500 | flat -0.031 (noise 0.027) |
| colour_clear | 0.524 (809) | 0.540 (5488) [0.531, 0.550] | 0.544 (23646) [0.540, 0.549] | 0.521 (48605) [0.515, 0.527] | 0.545 (24367) [0.540, 0.548] | 0.515 (132) | 0.500 | flat -0.008 (noise 0.009) |
| colour_confident | 0.568 (88) | 0.575 (979) [0.564, 0.587] | 0.597 (4516) [0.585, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.682 (22) | 0.500 | flat -0.026 (noise 0.021) |
| colour_next | 0.530 (1434) | 0.531 (9968) [0.525, 0.538] | 0.530 (42837) [0.526, 0.534] | 0.515 (88590) [0.511, 0.519] | 0.530 (44241) [0.526, 0.533] | 0.530 (219) | 0.500 | flat +0.000 (noise 0.007) |
| colour_path | 0.498 (20076) | 0.502 (139552) [0.500, 0.504] | 0.501 (599718) [0.500, 0.502] | 0.501 (1240260) [0.500, 0.502] | 0.501 (619374) [0.499, 0.502] | 0.500 (3066) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.706 (17) | 0.619 (236) [0.577, 0.663] | 0.633 (1203) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.500 (4) | 0.500 | flat -0.008 (noise 0.040) |
| reversal_k13_next | 0.404 (47) | 0.356 (343) [0.308, 0.402] | 0.323 (1879) [0.310, 0.337] | 0.311 (4086) [0.301, 0.323] | 0.323 (1981) [0.311, 0.336] | 0.467 (15) | 0.077 | flat +0.043 (noise 0.034) |
| reversal_k13_now | 0.471 (51) | 0.581 (422) [0.543, 0.614] | 0.560 (1681) [0.541, 0.579] | 0.572 (3198) [0.558, 0.586] | 0.565 (1726) [0.545, 0.585] | 0.667 (9) | 0.077 | flat +0.035 (noise 0.035) |
| reversal_k3_next | 0.646 (113) | 0.599 (877) [0.587, 0.614] | 0.588 (3052) [0.577, 0.598] | 0.586 (5636) [0.578, 0.596] | 0.585 (3196) [0.575, 0.597] | 0.400 (20) | 0.293 | flat -0.002 (noise 0.025) |
| reversal_k3_now | 0.898 (59) | 0.934 (441) [0.912, 0.958] | 0.934 (1747) [0.924, 0.944] | 0.938 (3567) [0.931, 0.944] | 0.933 (1804) [0.923, 0.943] | 0.833 (12) | 0.293 | flat -0.012 (noise 0.020) |
| reversal_k5_next | 0.564 (55) | 0.543 (392) [0.528, 0.558] | 0.479 (2766) [0.464, 0.494] | 0.482 (4945) [0.471, 0.494] | 0.474 (2955) [0.460, 0.490] | 0.400 (15) | 0.187 | up +0.064 (noise 0.030) |
| reversal_k5_now | 0.803 (66) | 0.822 (443) [0.808, 0.834] | 0.821 (1645) [0.809, 0.832] | 0.829 (3317) [0.820, 0.838] | 0.821 (1706) [0.810, 0.831] | 0.818 (11) | 0.187 | flat +0.002 (noise 0.027) |
| reversal_k8_next | 0.475 (40) | 0.435 (575) [0.411, 0.461] | 0.391 (2808) [0.377, 0.405] | 0.393 (4991) [0.382, 0.404] | 0.391 (2885) [0.378, 0.404] | 0.400 (15) | 0.121 | up +0.056 (noise 0.027) |
| reversal_k8_now | 0.635 (52) | 0.716 (391) [0.680, 0.746] | 0.686 (1596) [0.665, 0.706] | 0.701 (3233) [0.687, 0.716] | 0.689 (1646) [0.667, 0.709] | 0.625 (8) | 0.122 | flat +0.058 (noise 0.036) |
| overall | 0.503 (22089) | 0.507 (154076) [0.504, 0.509] | 0.505 (662607) [0.503, 0.506] | 0.504 (1367769) [0.503, 0.505] | 0.505 (684488) [0.503, 0.506] | 0.503 (3404) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08033, 0.1223] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5308, 'levels': [{'threshold': 0.08033, 'calls_per_day': 141.7, 'win_rate': 0.5783}, {'threshold': 0.1223, 'calls_per_day': 35.3, 'win_rate': 0.616}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42840, 'rate': 0.53}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14953 | 0.334 | 0.527 (14671) | 0.578 (2235) | 0.760 (2608) |
| volatility: normal | 14953 | 0.366 | 0.533 (14880) | 0.607 (1567) | 0.741 (2251) |
| volatility: wild | 14953 | 0.381 | 0.529 (14909) | 0.633 (820) | 0.763 (2063) |
| session: Asia 00-08 | 15099 | 0.360 | 0.536 (14984) | 0.602 (1626) | 0.759 (2260) |
| session: Europe 08-13 | 9300 | 0.354 | 0.533 (9197) | 0.594 (1164) | 0.747 (1549) |
| session: US 13-21 | 14880 | 0.367 | 0.527 (14758) | 0.596 (1199) | 0.759 (2271) |
| session: late 21-24 | 5580 | 0.351 | 0.516 (5521) | 0.596 (633) | 0.744 (842) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.389 | 0.427 | 0.308 | 0.308 | 0.517 | 0.286 | 0.492 | 1.150 |
| 6h | 360 | 0.375 | 0.370 | 0.283 | 0.333 | 0.538 | 0.287 | 0.464 | 1.199 |
| 24h | 1440 | 0.367 | 0.367 | 0.283 | 0.323 | 0.524 | 0.263 | 0.471 | 1.141 |
| 7d | 10080 | 0.360 | 0.355 | 0.275 | 0.305 | 0.531 | 0.261 | 0.459 | 1.289 |
| 30d | 43200 | 0.362 | 0.354 | 0.275 | 0.305 | 0.530 | 0.262 | 0.462 | 1.258 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.389 / 0.517 / 0.900; 2: 0.378 / 0.467 / 0.817; 3: 0.381 / 0.517 / 1.000; 4: 0.390 / 0.500 / 1.000; 5: 0.389 / 0.517 / 1.000; 6: 0.397 / 0.550 / 1.000; 7: 0.412 / 0.583 / 1.000; 8: 0.423 / 0.617 / 1.000; 9: 0.398 / 0.583 / 1.000; 10: 0.390 / 0.550 / 1.000; 11: 0.368 / 0.433 / 1.000; 12: 0.390 / 0.483 / 0.983; 13: 0.369 / 0.417 / 1.000; 14: 0.383 / 0.450 / 1.000; 15: 0.371 / 0.433 / 1.000
- 6h: 1: 0.375 / 0.538 / 0.875; 2: 0.355 / 0.482 / 0.844; 3: 0.355 / 0.487 / 0.958; 4: 0.364 / 0.510 / 0.964; 5: 0.359 / 0.507 / 0.956; 6: 0.358 / 0.493 / 0.969; 7: 0.364 / 0.518 / 0.961; 8: 0.360 / 0.510 / 0.958; 9: 0.351 / 0.482 / 0.953; 10: 0.351 / 0.485 / 0.950; 11: 0.354 / 0.479 / 0.944; 12: 0.358 / 0.485 / 0.936; 13: 0.352 / 0.468 / 0.944; 14: 0.350 / 0.485 / 0.942; 15: 0.363 / 0.513 / 0.933
- 24h: 1: 0.367 / 0.524 / 0.898; 2: 0.362 / 0.506 / 0.890; 3: 0.359 / 0.505 / 0.903; 4: 0.357 / 0.500 / 0.904; 5: 0.359 / 0.510 / 0.899; 6: 0.363 / 0.518 / 0.910; 7: 0.361 / 0.514 / 0.894; 8: 0.357 / 0.506 / 0.897; 9: 0.355 / 0.497 / 0.896; 10: 0.352 / 0.480 / 0.894; 11: 0.353 / 0.490 / 0.903; 12: 0.355 / 0.487 / 0.906; 13: 0.354 / 0.483 / 0.906; 14: 0.353 / 0.495 / 0.909; 15: 0.355 / 0.496 / 0.908
- 7d: 1: 0.360 / 0.531 / 0.897; 2: 0.348 / 0.493 / 0.899; 3: 0.350 / 0.508 / 0.900; 4: 0.347 / 0.500 / 0.900; 5: 0.349 / 0.515 / 0.899; 6: 0.345 / 0.504 / 0.900; 7: 0.347 / 0.500 / 0.898; 8: 0.346 / 0.510 / 0.898; 9: 0.345 / 0.501 / 0.899; 10: 0.345 / 0.497 / 0.898; 11: 0.343 / 0.499 / 0.899; 12: 0.344 / 0.497 / 0.899; 13: 0.345 / 0.503 / 0.899; 14: 0.344 / 0.500 / 0.899; 15: 0.344 / 0.502 / 0.899
- 30d: 1: 0.362 / 0.530 / 0.898; 2: 0.350 / 0.496 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.349 / 0.505 / 0.900; 6: 0.347 / 0.500 / 0.900; 7: 0.347 / 0.500 / 0.899; 8: 0.347 / 0.503 / 0.899; 9: 0.346 / 0.499 / 0.899; 10: 0.347 / 0.504 / 0.899; 11: 0.344 / 0.496 / 0.899; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.501 / 0.899; 14: 0.345 / 0.500 / 0.899; 15: 0.346 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.175 (body 0.140, range 0.211); 'price stays where it was' would score 0.152; colour right 0.600; typical miss of the close 7.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.138 (body 0.105, range 0.171); 'price stays where it was' would score 0.122; colour right 0.518; typical miss of the close 8.2 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.121 (body 0.083, range 0.160); 'price stays where it was' would score 0.121; colour right 0.500; typical miss of the close 10.6 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.124 (body 0.085, range 0.163); 'price stays where it was' would score 0.127; colour right 0.502; typical miss of the close 8.2 bp; chain ended on the right side 0.493 of 672 chains; n=10080
- 30d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 7.9 bp; chain ended on the right side 0.515 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.200 / 4.7; 3: 0.169 / 6.2; 4: 0.131 / 6.6; 5: 0.124 / 7.4; 6: 0.113 / 7.9; 7: 0.111 / 8.2; 8: 0.098 / 8.9; 9: 0.090 / 8.8; 10: 0.089 / 9.4; 11: 0.085 / 9.8; 12: 0.076 / 10.1; 13: 0.068 / 10.2; 14: 0.069 / 10.8; 15: 0.062 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 132453, probability skill vs chance 0.2177, widened contest next: True
  - now: threshold 0.8391, hit rate recent 0.8916 / long run 0.9319
    - 6h: 19 calls (77 a day), hit rate 0.842, chance 0.275, naive rule 0.398, lift 3.07x
    - 24h: 65 calls (65 a day), hit rate 0.908, chance 0.287, naive rule 0.465, lift 3.16x
    - 7d: 440 calls (63 a day), hit rate 0.932, chance 0.292, naive rule 0.496, lift 3.19x
    - 30d: 1745 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.494, lift 3.17x
  - next: threshold 0.5582, hit rate recent 0.5469 / long run 0.5965
    - 6h: 31 calls (126 a day), hit rate 0.387, chance 0.275, lift 1.41x
    - 24h: 119 calls (119 a day), hit rate 0.613, chance 0.287, lift 2.13x
    - 7d: 877 calls (125 a day), hit rate 0.594, chance 0.292, lift 2.04x
    - 30d: 3055 calls (102 a day), hit rate 0.586, chance 0.294, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.497; 0.35: 535, 0.522; 0.40: 474, 0.580; 0.45: 405, 0.652; 0.50: 354, 0.700; 0.55: 309, 0.743; 0.60: 262, 0.786; 0.65: 220, 0.812; 0.70: 174, 0.843; 0.75: 138, 0.877; 0.80: 92, 0.910; 0.85: 47, 0.946; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.427; 0.35: 501, 0.463; 0.40: 405, 0.498; 0.45: 308, 0.533; 0.50: 199, 0.569; 0.55: 90, 0.573; 0.60: 12, 0.650; 0.65: 1, 0.652
- **K=5**: model 1792540800, labels learned 132451, probability skill vs chance 0.22, widened contest next: False
  - now: threshold 0.6895, hit rate recent 0.8166 / long run 0.8206
    - 6h: 17 calls (69 a day), hit rate 0.824, chance 0.157, naive rule 0.279, lift 5.24x
    - 24h: 70 calls (70 a day), hit rate 0.814, chance 0.183, naive rule 0.379, lift 4.45x
    - 7d: 444 calls (63 a day), hit rate 0.824, chance 0.188, naive rule 0.415, lift 4.38x
    - 30d: 1643 calls (55 a day), hit rate 0.819, chance 0.188, naive rule 0.405, lift 4.37x
  - next: threshold 0.4505, hit rate recent 0.5232 / long run 0.5096
    - 6h: 19 calls (78 a day), hit rate 0.368, chance 0.157, lift 2.34x
    - 24h: 62 calls (62 a day), hit rate 0.548, chance 0.183, lift 3.00x
    - 7d: 398 calls (57 a day), hit rate 0.535, chance 0.188, lift 2.84x
    - 30d: 2759 calls (92 a day), hit rate 0.478, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.425; 0.35: 347, 0.491; 0.40: 279, 0.566; 0.45: 229, 0.619; 0.50: 182, 0.666; 0.55: 144, 0.702; 0.60: 110, 0.750; 0.65: 77, 0.788; 0.70: 50, 0.821; 0.75: 29, 0.865; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.386; 0.35: 256, 0.420; 0.40: 160, 0.459; 0.45: 68, 0.481; 0.50: 13, 0.500; 0.55: 1, 0.486
- **K=8**: model 1793059200, labels learned 132448, probability skill vs chance 0.2056, widened contest next: True
  - now: threshold 0.572, hit rate recent 0.6578 / long run 0.6905
    - 6h: 16 calls (66 a day), hit rate 0.562, chance 0.120, naive rule 0.272, lift 4.69x
    - 24h: 55 calls (55 a day), hit rate 0.636, chance 0.128, naive rule 0.339, lift 4.99x
    - 7d: 388 calls (55 a day), hit rate 0.719, chance 0.126, naive rule 0.353, lift 5.71x
    - 30d: 1594 calls (53 a day), hit rate 0.685, chance 0.121, naive rule 0.334, lift 5.65x
  - next: threshold 0.3634, hit rate recent 0.4609 / long run 0.4173
    - 6h: 16 calls (66 a day), hit rate 0.375, chance 0.120, lift 3.12x
    - 24h: 48 calls (48 a day), hit rate 0.458, chance 0.128, lift 3.59x
    - 7d: 577 calls (83 a day), hit rate 0.435, chance 0.126, lift 3.45x
    - 30d: 2812 calls (94 a day), hit rate 0.390, chance 0.121, lift 3.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.434; 0.35: 190, 0.500; 0.40: 149, 0.545; 0.45: 114, 0.593; 0.50: 85, 0.638; 0.55: 61, 0.673; 0.60: 41, 0.707; 0.65: 24, 0.782; 0.70: 12, 0.812; 0.75: 2, 0.767
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.359; 0.35: 92, 0.387; 0.40: 27, 0.424; 0.45: 5, 0.460; 0.50: 1, 0.680
- **K=13**: model 1793577600, labels learned 132443, probability skill vs chance 0.1855, widened contest next: False
  - now: threshold 0.4469, hit rate recent 0.5407 / long run 0.5646
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.091, naive rule 0.250, lift 7.04x
    - 24h: 55 calls (56 a day), hit rate 0.509, chance 0.082, naive rule 0.283, lift 6.23x
    - 7d: 422 calls (60 a day), hit rate 0.585, chance 0.080, naive rule 0.299, lift 7.28x
    - 30d: 1678 calls (56 a day), hit rate 0.560, chance 0.077, naive rule 0.279, lift 7.24x
  - next: threshold 0.288, hit rate recent 0.4053 / long run 0.3342
    - 6h: 18 calls (75 a day), hit rate 0.444, chance 0.091, lift 4.87x
    - 24h: 53 calls (54 a day), hit rate 0.396, chance 0.082, lift 4.85x
    - 7d: 349 calls (50 a day), hit rate 0.361, chance 0.080, lift 4.49x
    - 30d: 1884 calls (63 a day), hit rate 0.325, chance 0.077, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.440; 0.35: 93, 0.492; 0.40: 66, 0.545; 0.45: 44, 0.588; 0.50: 29, 0.648; 0.55: 19, 0.680; 0.60: 10, 0.723; 0.65: 3, 0.713; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.331; 0.35: 13, 0.359; 0.40: 3, 0.427; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.786 | 0.40% | 0.883 | 0.467 | 0.245 | 0.633 | 0.325 |
| 6h | 12.586 | 2.05% | 0.869 | 0.492 | 0.250 | 0.510 | 0.313 |
| 24h | 15.727 | 3.45% | 0.892 | 0.496 | 0.250 | 0.508 | 0.582 |
| 7d | 14.935 | 4.92% | 0.899 | 0.500 | 0.250 | 0.507 | 0.745 |
| 30d | 14.238 | 4.34% | 0.900 | 0.499 | 0.251 | 0.498 | 0.690 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.849 | 16.063 | 16.167 | 15.902 | 16.271 | 16.134 | 15.973 | 15.825 | 15.924 | 15.786 |
| 6h | 12.850 | 12.692 | 12.699 | 12.663 | 12.784 | 12.866 | 12.595 | 12.541 | 12.578 | 12.586 |
| 24h | 16.290 | 15.829 | 15.882 | 15.885 | 15.970 | 16.070 | 15.724 | 15.695 | 15.709 | 15.727 |
| 7d | 15.708 | 15.105 | 15.065 | 14.982 | 15.267 | 15.245 | 14.921 | 14.905 | 14.912 | 14.935 |
| 30d | 14.884 | 14.387 | 14.334 | 14.271 | 14.503 | 14.451 | 14.232 | 14.209 | 14.212 | 14.238 |

## Next candle

- candle starting 2026-11-03 03:39 UTC, last close 2244.68
- P(up) 0.4646, return quantiles (bp): {'05': -9.96, '10': -7.729, '25': -4.722, '40': -2.197, '50': -0.691, '60': 1.283, '75': 3.516, '90': 7.371, '95': 10.089}
- changepoint probability 0.0412, regime age 75.8 min
- agent weights: empirical 0.006, ewma 0.116, garch 0.072, har 0.085, bocpd 0.034, hmm 0.019, online_qr 0.276, lgbm 0.393

## Learning log

- 2026-11-01 00:00 UTC: {"garch": {"alpha": 0.0921, "beta": 0.9006}, "hmm": {"sd_bp": [3.03, 6.64, 20.06], "stay": [0.979, 0.96, 0.916]}, "lgbm": {"challenger_loss": 0.24492, "champion_loss": 0.24505, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48767, "challengers": 1, "chance_loss": 0.61239, "widened": false, "champion_loss": 0.48648, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37405, "challengers": 1, "chance_loss": 0.48524, "widened": false, "champion_loss": 0.37258, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27721, "challengers": 1, "chance_loss": 0.37271, "widened": false, "champion_loss": 0.2771, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20067, "challengers": 1, "chance_loss": 0.28106, "widened": false, "champion_loss": 0.20131, "promoted": true}}
- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.67, 6.48, 20.04], current probabilities: [0.003, 0.981, 0.016]
- live generator: {'versions': 60, 'latest_effective': '2026-11-03 03:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.323, 'l_abs': 0.594, 'l_hi': 0.719, 'l_lo': 0.759, 'b05': 0.647, 'b25': 0.592, 'b75': 0.601, 'b95': 0.649}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.898, 1.691, 2.036, 2.731, 2.311, 3.884, 3.998, 3.922, 4.765, 4.1, 3.961, 4.386, 4.471, 4.73]}
- calibration offsets (in sigma): {'05': -0.011, '10': -0.012, '25': -0.125, '40': -0.128, '50': -0.1, '60': -0.022, '75': -0.035, '90': -0.008, '95': 0.071}
