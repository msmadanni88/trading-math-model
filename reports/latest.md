# ETH-USD 60s candle generator - report

- generated: 2026-10-24 19:22 UTC
- last closed candle: 2026-10-24 19:22 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.506 (77) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.553 (606) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.629 (202) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.530 (1155) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.499 (16170) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.578 (71) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.239 (46) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | 0.614 (44) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.660 (47) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 0.976 (42) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.511 (94) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | 0.848 (46) | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.373 (67) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | 0.702 (47) | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.503 (17835) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0725, 0.1066] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5352, 'levels': [{'threshold': 0.0725, 'calls_per_day': 147.6, 'win_rate': 0.6031}, {'threshold': 0.1066, 'calls_per_day': 37.3, 'win_rate': 0.6412}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 29993, 'rate': 0.5313}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15268 | 0.337 | 0.525 (15016) | 0.590 (1638) | 0.766 (2528) |
| volatility: normal | 15267 | 0.365 | 0.522 (15202) | 0.623 (1016) | 0.749 (2253) |
| volatility: wild | 15267 | 0.378 | 0.515 (15232) | 0.623 (472) | 0.776 (1960) |
| session: Asia 00-08 | 15360 | 0.358 | 0.526 (15258) | 0.613 (1120) | 0.767 (2224) |
| session: Europe 08-13 | 9600 | 0.355 | 0.521 (9513) | 0.597 (780) | 0.763 (1543) |
| session: US 13-21 | 15262 | 0.368 | 0.516 (15161) | 0.600 (779) | 0.768 (2160) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5518) | 0.615 (447) | 0.741 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.399 | 0.353 | 0.246 | 0.246 | 0.650 | 0.323 | 0.475 | 1.130 |
| 6h | 360 | 0.375 | 0.366 | 0.289 | 0.313 | 0.531 | 0.273 | 0.476 | 1.357 |
| 24h | 1440 | 0.365 | 0.350 | 0.269 | 0.302 | 0.530 | 0.270 | 0.460 | 1.173 |
| 7d | 10080 | 0.371 | 0.361 | 0.273 | 0.306 | 0.535 | 0.268 | 0.473 | 1.208 |
| 30d | 43200 | 0.360 | 0.353 | 0.277 | 0.305 | 0.523 | 0.256 | 0.464 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.399 / 0.650 / 0.917; 2: 0.376 / 0.517 / 0.900; 3: 0.387 / 0.617 / 0.917; 4: 0.379 / 0.550 / 0.917; 5: 0.342 / 0.467 / 0.900; 6: 0.367 / 0.567 / 0.900; 7: 0.359 / 0.483 / 0.883; 8: 0.327 / 0.433 / 0.900; 9: 0.371 / 0.583 / 0.900; 10: 0.343 / 0.467 / 0.883; 11: 0.349 / 0.483 / 0.900; 12: 0.354 / 0.533 / 0.933; 13: 0.364 / 0.533 / 0.950; 14: 0.372 / 0.533 / 1.000; 15: 0.356 / 0.517 / 1.000
- 6h: 1: 0.375 / 0.531 / 0.922; 2: 0.354 / 0.467 / 0.925; 3: 0.364 / 0.519 / 0.911; 4: 0.343 / 0.461 / 0.903; 5: 0.364 / 0.528 / 0.883; 6: 0.340 / 0.447 / 0.883; 7: 0.360 / 0.536 / 0.886; 8: 0.347 / 0.497 / 0.889; 9: 0.344 / 0.469 / 0.861; 10: 0.344 / 0.489 / 0.875; 11: 0.351 / 0.483 / 0.847; 12: 0.349 / 0.503 / 0.872; 13: 0.349 / 0.506 / 0.872; 14: 0.342 / 0.467 / 0.869; 15: 0.336 / 0.481 / 0.869
- 24h: 1: 0.365 / 0.530 / 0.906; 2: 0.348 / 0.490 / 0.893; 3: 0.353 / 0.518 / 0.894; 4: 0.342 / 0.473 / 0.891; 5: 0.350 / 0.509 / 0.889; 6: 0.340 / 0.484 / 0.890; 7: 0.345 / 0.494 / 0.888; 8: 0.348 / 0.516 / 0.890; 9: 0.347 / 0.505 / 0.883; 10: 0.345 / 0.497 / 0.881; 11: 0.345 / 0.501 / 0.876; 12: 0.346 / 0.495 / 0.878; 13: 0.346 / 0.522 / 0.878; 14: 0.338 / 0.480 / 0.878; 15: 0.349 / 0.529 / 0.878
- 7d: 1: 0.371 / 0.535 / 0.899; 2: 0.358 / 0.499 / 0.900; 3: 0.360 / 0.511 / 0.900; 4: 0.353 / 0.490 / 0.899; 5: 0.354 / 0.500 / 0.899; 6: 0.353 / 0.496 / 0.899; 7: 0.352 / 0.494 / 0.899; 8: 0.355 / 0.511 / 0.899; 9: 0.352 / 0.498 / 0.899; 10: 0.354 / 0.507 / 0.899; 11: 0.350 / 0.497 / 0.898; 12: 0.352 / 0.503 / 0.898; 13: 0.350 / 0.495 / 0.898; 14: 0.351 / 0.499 / 0.898; 15: 0.350 / 0.502 / 0.898
- 30d: 1: 0.360 / 0.523 / 0.899; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.497 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.347 / 0.499 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.497 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.346 / 0.503 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.344 / 0.497 / 0.900; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.146 (body 0.103, range 0.189); 'price stays where it was' would score 0.166; colour right 0.617; typical miss of the close 9.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.114 (body 0.078, range 0.150); 'price stays where it was' would score 0.142; colour right 0.464; typical miss of the close 14.5 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.122 (body 0.084, range 0.159); 'price stays where it was' would score 0.143; colour right 0.497; typical miss of the close 7.7 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.168); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 9.0 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.198 / 4.4; 3: 0.167 / 5.8; 4: 0.130 / 6.4; 5: 0.122 / 7.1; 6: 0.110 / 7.6; 7: 0.105 / 7.9; 8: 0.097 / 8.2; 9: 0.088 / 8.2; 10: 0.087 / 8.9; 11: 0.083 / 9.4; 12: 0.077 / 9.7; 13: 0.068 / 9.9; 14: 0.068 / 10.3; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 118996, probability skill vs chance 0.2314, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9597 / long run 0.9384
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.317, naive rule 0.521, lift 3.16x
    - 24h: 54 calls (54 a day), hit rate 0.963, chance 0.301, naive rule 0.521, lift 3.20x
    - 7d: 403 calls (58 a day), hit rate 0.943, chance 0.295, naive rule 0.496, lift 3.19x
    - 30d: 1691 calls (56 a day), hit rate 0.936, chance 0.294, naive rule 0.490, lift 3.19x
  - next: threshold 0.5681, hit rate recent 0.6442 / long run 0.5931
    - 6h: 6 calls (24 a day), hit rate 0.500, chance 0.317, lift 1.58x
    - 24h: 55 calls (55 a day), hit rate 0.673, chance 0.301, lift 2.23x
    - 7d: 705 calls (101 a day), hit rate 0.594, chance 0.295, lift 2.01x
    - 30d: 2794 calls (93 a day), hit rate 0.581, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.494; 0.35: 539, 0.518; 0.40: 479, 0.574; 0.45: 410, 0.644; 0.50: 357, 0.698; 0.55: 312, 0.739; 0.60: 264, 0.784; 0.65: 222, 0.809; 0.70: 175, 0.840; 0.75: 136, 0.874; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.426; 0.35: 500, 0.464; 0.40: 406, 0.499; 0.45: 310, 0.532; 0.50: 201, 0.565; 0.55: 91, 0.573; 0.60: 14, 0.623; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 118994, probability skill vs chance 0.231, widened contest next: False
  - now: threshold 0.6751, hit rate recent 0.8196 / long run 0.822
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.170, naive rule 0.435, lift 4.78x
    - 24h: 56 calls (56 a day), hit rate 0.821, chance 0.178, naive rule 0.419, lift 4.62x
    - 7d: 363 calls (52 a day), hit rate 0.815, chance 0.186, naive rule 0.403, lift 4.39x
    - 30d: 1557 calls (52 a day), hit rate 0.830, chance 0.188, naive rule 0.400, lift 4.42x
  - next: threshold 0.4197, hit rate recent 0.5445 / long run 0.4745
    - 6h: 23 calls (94 a day), hit rate 0.609, chance 0.170, lift 3.58x
    - 24h: 121 calls (122 a day), hit rate 0.504, chance 0.178, lift 2.83x
    - 7d: 939 calls (134 a day), hit rate 0.459, chance 0.186, lift 2.47x
    - 30d: 2813 calls (94 a day), hit rate 0.465, chance 0.188, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 344, 0.495; 0.40: 276, 0.567; 0.45: 223, 0.623; 0.50: 176, 0.672; 0.55: 135, 0.713; 0.60: 104, 0.756; 0.65: 76, 0.792; 0.70: 53, 0.830; 0.75: 31, 0.873; 0.80: 10, 0.907
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.391; 0.35: 251, 0.423; 0.40: 157, 0.451; 0.45: 69, 0.463; 0.50: 15, 0.492; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 118991, probability skill vs chance 0.2033, widened contest next: False
  - now: threshold 0.5598, hit rate recent 0.6534 / long run 0.6809
    - 6h: 15 calls (62 a day), hit rate 0.600, chance 0.124, naive rule 0.383, lift 4.83x
    - 24h: 57 calls (57 a day), hit rate 0.667, chance 0.124, naive rule 0.353, lift 5.39x
    - 7d: 335 calls (48 a day), hit rate 0.657, chance 0.116, naive rule 0.318, lift 5.65x
    - 30d: 1524 calls (51 a day), hit rate 0.700, chance 0.121, naive rule 0.330, lift 5.78x
  - next: threshold 0.3433, hit rate recent 0.397 / long run 0.3772
    - 6h: 15 calls (62 a day), hit rate 0.467, chance 0.124, lift 3.75x
    - 24h: 93 calls (94 a day), hit rate 0.366, chance 0.124, lift 2.95x
    - 7d: 765 calls (109 a day), hit rate 0.371, chance 0.116, lift 3.19x
    - 30d: 2506 calls (84 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 250, 0.425; 0.35: 190, 0.496; 0.40: 145, 0.551; 0.45: 111, 0.596; 0.50: 84, 0.636; 0.55: 62, 0.676; 0.60: 41, 0.722; 0.65: 23, 0.788; 0.70: 10, 0.838; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.352; 0.35: 99, 0.379; 0.40: 36, 0.402; 0.45: 8, 0.438; 0.50: 1, 0.567
- **K=13**: model 1792800000, labels learned 118986, probability skill vs chance 0.175, widened contest next: True
  - now: threshold 0.4112, hit rate recent 0.5502 / long run 0.5546
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.070, naive rule 0.292, lift 7.19x
    - 24h: 53 calls (54 a day), hit rate 0.566, chance 0.069, naive rule 0.262, lift 8.15x
    - 7d: 370 calls (53 a day), hit rate 0.527, chance 0.074, naive rule 0.267, lift 7.11x
    - 30d: 1559 calls (52 a day), hit rate 0.568, chance 0.077, naive rule 0.273, lift 7.35x
  - next: threshold 0.2903, hit rate recent 0.2623 / long run 0.305
    - 6h: 11 calls (46 a day), hit rate 0.182, chance 0.070, lift 2.61x
    - 24h: 60 calls (61 a day), hit rate 0.233, chance 0.069, lift 3.36x
    - 7d: 477 calls (68 a day), hit rate 0.302, chance 0.074, lift 4.07x
    - 30d: 2160 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.93x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.446; 0.35: 87, 0.498; 0.40: 61, 0.553; 0.45: 41, 0.607; 0.50: 25, 0.660; 0.55: 15, 0.706; 0.60: 6, 0.753; 0.65: 2, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.314; 0.35: 13, 0.352; 0.40: 2, 0.429; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.013 | 0.70% | 0.917 | 0.350 | 0.250 | 0.517 | 0.344 |
| 6h | 22.656 | 8.10% | 0.903 | 0.475 | 0.251 | 0.508 | 0.643 |
| 24h | 13.999 | 6.19% | 0.906 | 0.502 | 0.251 | 0.487 | 0.701 |
| 7d | 15.324 | 3.57% | 0.901 | 0.499 | 0.250 | 0.502 | 0.645 |
| 30d | 13.422 | 4.21% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.111 | 14.017 | 14.048 | 14.329 | 13.921 | 14.097 | 14.006 | 13.983 | 13.975 | 14.013 |
| 6h | 24.654 | 23.257 | 22.721 | 22.885 | 23.049 | 22.705 | 22.754 | 22.497 | 22.624 | 22.656 |
| 24h | 14.922 | 14.266 | 14.077 | 14.022 | 14.264 | 14.197 | 14.018 | 13.959 | 13.975 | 13.999 |
| 7d | 15.891 | 15.485 | 15.396 | 15.339 | 15.589 | 15.456 | 15.315 | 15.289 | 15.296 | 15.324 |
| 30d | 14.012 | 13.549 | 13.506 | 13.445 | 13.665 | 13.613 | 13.418 | 13.399 | 13.397 | 13.422 |

## Next candle

- candle starting 2026-10-24 19:22 UTC, last close 2333.89
- P(up) 0.5127, return quantiles (bp): {'05': -7.144, '10': -5.062, '25': -2.454, '40': -0.914, '50': 0.129, '60': 1.015, '75': 3.178, '90': 5.283, '95': 6.713}
- changepoint probability 0.0548, regime age 120.0 min
- agent weights: empirical 0.003, ewma 0.017, garch 0.140, har 0.096, bocpd 0.025, hmm 0.071, online_qr 0.169, lgbm 0.480

## Learning log

- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- HMM volatility states (sd, bp per minute): [4.1, 7.07, 17.69], current probabilities: [0.953, 0.046, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 19:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.38, 'l_abs': 0.648, 'l_hi': 0.79, 'l_lo': 0.786, 'b05': 0.734, 'b25': 0.697, 'b75': 0.625, 'b95': 0.698}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.343, 1.648, 2.024, 2.408, 2.591, 2.748, 3.003, 3.672, 3.878, 4.504, 4.529, 4.63, 5.01, 5.094]}
- calibration offsets (in sigma): {'05': 0.0605, '10': 0.071, '25': 0.0425, '40': 0.004, '50': 0.025, '60': 0.006, '75': 0.0675, '90': -0.061, '95': -0.1105}
