# ETH-USD 60s candle generator - report

- generated: 2026-10-24 21:42 UTC
- last closed candle: 2026-10-24 21:42 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.500 (86) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.548 (672) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.617 (227) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.527 (1295) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.499 (18130) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.584 (77) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.241 (54) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | 0.630 (46) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.640 (50) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 0.978 (46) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.477 (109) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | 0.827 (52) | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.365 (74) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | 0.726 (51) | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.503 (19993) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0725, 0.1066] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5352, 'levels': [{'threshold': 0.0725, 'calls_per_day': 147.6, 'win_rate': 0.6031}, {'threshold': 0.1066, 'calls_per_day': 37.3, 'win_rate': 0.6412}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 30133, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15314 | 0.337 | 0.525 (15061) | 0.591 (1639) | 0.766 (2531) |
| volatility: normal | 15314 | 0.365 | 0.521 (15250) | 0.620 (1038) | 0.750 (2263) |
| volatility: wild | 15314 | 0.378 | 0.515 (15279) | 0.625 (474) | 0.775 (1963) |
| session: Asia 00-08 | 15360 | 0.358 | 0.526 (15258) | 0.613 (1120) | 0.767 (2224) |
| session: Europe 08-13 | 9600 | 0.355 | 0.521 (9513) | 0.597 (780) | 0.763 (1543) |
| session: US 13-21 | 15360 | 0.368 | 0.516 (15259) | 0.597 (798) | 0.768 (2171) |
| session: late 21-24 | 5622 | 0.351 | 0.514 (5560) | 0.616 (453) | 0.741 (819) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.353 | 0.358 | 0.306 | 0.306 | 0.483 | 0.251 | 0.454 | 1.452 |
| 6h | 360 | 0.372 | 0.358 | 0.290 | 0.303 | 0.511 | 0.273 | 0.472 | 1.142 |
| 24h | 1440 | 0.363 | 0.349 | 0.274 | 0.301 | 0.527 | 0.268 | 0.458 | 1.206 |
| 7d | 10080 | 0.371 | 0.362 | 0.274 | 0.307 | 0.535 | 0.269 | 0.474 | 1.203 |
| 30d | 43200 | 0.360 | 0.353 | 0.277 | 0.305 | 0.523 | 0.256 | 0.464 | 1.287 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.353 / 0.483 / 0.900; 2: 0.351 / 0.483 / 0.867; 3: 0.335 / 0.467 / 0.817; 4: 0.343 / 0.467 / 0.900; 5: 0.343 / 0.550 / 0.900; 6: 0.369 / 0.567 / 0.867; 7: 0.338 / 0.483 / 0.833; 8: 0.337 / 0.483 / 0.817; 9: 0.343 / 0.467 / 0.850; 10: 0.345 / 0.500 / 0.833; 11: 0.350 / 0.550 / 0.833; 12: 0.327 / 0.467 / 0.833; 13: 0.379 / 0.650 / 0.800; 14: 0.363 / 0.600 / 0.817; 15: 0.331 / 0.433 / 0.833
- 6h: 1: 0.372 / 0.511 / 0.931; 2: 0.356 / 0.469 / 0.928; 3: 0.359 / 0.519 / 0.928; 4: 0.348 / 0.478 / 0.944; 5: 0.352 / 0.506 / 0.936; 6: 0.346 / 0.472 / 0.919; 7: 0.356 / 0.514 / 0.908; 8: 0.338 / 0.458 / 0.906; 9: 0.355 / 0.497 / 0.897; 10: 0.341 / 0.461 / 0.903; 11: 0.356 / 0.497 / 0.894; 12: 0.352 / 0.506 / 0.906; 13: 0.365 / 0.536 / 0.903; 14: 0.362 / 0.514 / 0.922; 15: 0.351 / 0.500 / 0.931
- 24h: 1: 0.363 / 0.527 / 0.908; 2: 0.347 / 0.486 / 0.896; 3: 0.348 / 0.508 / 0.896; 4: 0.341 / 0.473 / 0.898; 5: 0.346 / 0.506 / 0.893; 6: 0.338 / 0.487 / 0.890; 7: 0.342 / 0.497 / 0.890; 8: 0.345 / 0.513 / 0.884; 9: 0.343 / 0.501 / 0.881; 10: 0.341 / 0.494 / 0.879; 11: 0.342 / 0.502 / 0.876; 12: 0.343 / 0.491 / 0.878; 13: 0.346 / 0.527 / 0.878; 14: 0.339 / 0.491 / 0.876; 15: 0.347 / 0.527 / 0.878
- 7d: 1: 0.371 / 0.535 / 0.900; 2: 0.358 / 0.498 / 0.901; 3: 0.360 / 0.511 / 0.901; 4: 0.353 / 0.491 / 0.902; 5: 0.354 / 0.499 / 0.901; 6: 0.354 / 0.495 / 0.901; 7: 0.352 / 0.493 / 0.901; 8: 0.356 / 0.510 / 0.900; 9: 0.353 / 0.500 / 0.899; 10: 0.354 / 0.506 / 0.900; 11: 0.351 / 0.498 / 0.899; 12: 0.353 / 0.503 / 0.899; 13: 0.351 / 0.495 / 0.899; 14: 0.352 / 0.500 / 0.899; 15: 0.351 / 0.503 / 0.900
- 30d: 1: 0.360 / 0.523 / 0.899; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.497 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.502 / 0.900; 9: 0.345 / 0.497 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.899; 12: 0.346 / 0.503 / 0.899; 13: 0.346 / 0.502 / 0.899; 14: 0.344 / 0.498 / 0.899; 15: 0.345 / 0.500 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.166 (body 0.131, range 0.200); 'price stays where it was' would score 0.116; colour right 0.483; typical miss of the close 6.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.082, range 0.153); 'price stays where it was' would score 0.145; colour right 0.478; typical miss of the close 11.0 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.118 (body 0.083, range 0.154); 'price stays where it was' would score 0.140; colour right 0.489; typical miss of the close 8.1 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.168); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 9.1 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.517 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.197 / 4.4; 3: 0.168 / 5.8; 4: 0.130 / 6.4; 5: 0.122 / 7.1; 6: 0.110 / 7.6; 7: 0.105 / 7.9; 8: 0.097 / 8.2; 9: 0.088 / 8.2; 10: 0.087 / 8.9; 11: 0.083 / 9.4; 12: 0.077 / 9.8; 13: 0.068 / 9.9; 14: 0.068 / 10.3; 15: 0.059 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 119136, probability skill vs chance 0.2295, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9623 / long run 0.9389
    - 6h: 7 calls (28 a day), hit rate 1.000, chance 0.318, naive rule 0.562, lift 3.14x
    - 24h: 49 calls (49 a day), hit rate 0.980, chance 0.297, naive rule 0.519, lift 3.30x
    - 7d: 396 calls (57 a day), hit rate 0.944, chance 0.296, naive rule 0.499, lift 3.19x
    - 30d: 1691 calls (56 a day), hit rate 0.937, chance 0.294, naive rule 0.491, lift 3.19x
  - next: threshold 0.5681, hit rate recent 0.6286 / long run 0.5918
    - 6h: 5 calls (20 a day), hit rate 0.600, chance 0.318, lift 1.88x
    - 24h: 54 calls (54 a day), hit rate 0.667, chance 0.297, lift 2.25x
    - 7d: 696 calls (99 a day), hit rate 0.593, chance 0.296, lift 2.01x
    - 30d: 2791 calls (93 a day), hit rate 0.580, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.494; 0.35: 539, 0.518; 0.40: 479, 0.574; 0.45: 409, 0.645; 0.50: 357, 0.698; 0.55: 312, 0.739; 0.60: 264, 0.784; 0.65: 222, 0.809; 0.70: 175, 0.841; 0.75: 136, 0.875; 0.80: 92, 0.914; 0.85: 47, 0.953; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.426; 0.35: 500, 0.464; 0.40: 406, 0.499; 0.45: 310, 0.532; 0.50: 202, 0.565; 0.55: 91, 0.573; 0.60: 14, 0.617; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 119134, probability skill vs chance 0.2246, widened contest next: False
  - now: threshold 0.6751, hit rate recent 0.8047 / long run 0.8204
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.159, naive rule 0.408, lift 5.16x
    - 24h: 57 calls (57 a day), hit rate 0.789, chance 0.173, naive rule 0.408, lift 4.56x
    - 7d: 358 calls (51 a day), hit rate 0.813, chance 0.185, naive rule 0.403, lift 4.39x
    - 30d: 1561 calls (52 a day), hit rate 0.830, chance 0.188, naive rule 0.400, lift 4.42x
  - next: threshold 0.4197, hit rate recent 0.4844 / long run 0.4694
    - 6h: 27 calls (110 a day), hit rate 0.481, chance 0.159, lift 3.04x
    - 24h: 124 calls (125 a day), hit rate 0.476, chance 0.173, lift 2.75x
    - 7d: 934 calls (134 a day), hit rate 0.458, chance 0.185, lift 2.48x
    - 30d: 2827 calls (94 a day), hit rate 0.464, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 343, 0.495; 0.40: 276, 0.567; 0.45: 223, 0.623; 0.50: 176, 0.673; 0.55: 135, 0.712; 0.60: 104, 0.756; 0.65: 76, 0.792; 0.70: 53, 0.832; 0.75: 31, 0.875; 0.80: 10, 0.907
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 252, 0.422; 0.40: 157, 0.451; 0.45: 70, 0.462; 0.50: 15, 0.491; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 119131, probability skill vs chance 0.2017, widened contest next: False
  - now: threshold 0.5598, hit rate recent 0.6759 / long run 0.683
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.109, naive rule 0.339, lift 8.19x
    - 24h: 56 calls (56 a day), hit rate 0.696, chance 0.120, naive rule 0.340, lift 5.81x
    - 7d: 328 calls (47 a day), hit rate 0.655, chance 0.115, naive rule 0.318, lift 5.68x
    - 30d: 1523 calls (51 a day), hit rate 0.701, chance 0.121, naive rule 0.330, lift 5.79x
  - next: threshold 0.3433, hit rate recent 0.3852 / long run 0.3762
    - 6h: 10 calls (41 a day), hit rate 0.400, chance 0.109, lift 3.68x
    - 24h: 89 calls (90 a day), hit rate 0.360, chance 0.120, lift 3.00x
    - 7d: 754 calls (108 a day), hit rate 0.374, chance 0.115, lift 3.24x
    - 30d: 2511 calls (84 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 250, 0.426; 0.35: 189, 0.496; 0.40: 145, 0.551; 0.45: 111, 0.596; 0.50: 84, 0.637; 0.55: 62, 0.677; 0.60: 41, 0.724; 0.65: 23, 0.791; 0.70: 10, 0.838; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.351; 0.35: 98, 0.378; 0.40: 36, 0.401; 0.45: 8, 0.436; 0.50: 1, 0.567
- **K=13**: model 1792800000, labels learned 119126, probability skill vs chance 0.1768, widened contest next: True
  - now: threshold 0.4112, hit rate recent 0.5651 / long run 0.5561
    - 6h: 7 calls (29 a day), hit rate 0.857, chance 0.078, naive rule 0.307, lift 10.95x
    - 24h: 52 calls (53 a day), hit rate 0.577, chance 0.070, naive rule 0.257, lift 8.26x
    - 7d: 362 calls (52 a day), hit rate 0.528, chance 0.074, naive rule 0.268, lift 7.11x
    - 30d: 1559 calls (52 a day), hit rate 0.568, chance 0.077, naive rule 0.273, lift 7.35x
  - next: threshold 0.2903, hit rate recent 0.261 / long run 0.3043
    - 6h: 11 calls (46 a day), hit rate 0.273, chance 0.078, lift 3.48x
    - 24h: 63 calls (64 a day), hit rate 0.238, chance 0.070, lift 3.41x
    - 7d: 476 calls (68 a day), hit rate 0.305, chance 0.074, lift 4.11x
    - 30d: 2165 calls (72 a day), hit rate 0.303, chance 0.077, lift 3.92x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.446; 0.35: 87, 0.498; 0.40: 61, 0.553; 0.45: 41, 0.607; 0.50: 25, 0.660; 0.55: 15, 0.706; 0.60: 6, 0.754; 0.65: 2, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.315; 0.35: 13, 0.352; 0.40: 2, 0.429; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.134 | 0.30% | 0.867 | 0.500 | 0.250 | 0.517 | 0.381 |
| 6h | 14.880 | 1.26% | 0.900 | 0.492 | 0.253 | 0.483 | 0.597 |
| 24h | 14.142 | 6.01% | 0.904 | 0.506 | 0.251 | 0.493 | 0.698 |
| 7d | 15.267 | 3.39% | 0.902 | 0.500 | 0.250 | 0.502 | 0.640 |
| 30d | 13.419 | 4.20% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.167 | 11.144 | 11.100 | 11.143 | 11.215 | 11.126 | 11.121 | 11.075 | 11.093 | 11.134 |
| 6h | 15.069 | 15.080 | 14.752 | 15.026 | 14.886 | 14.759 | 14.841 | 14.746 | 14.768 | 14.880 |
| 24h | 15.046 | 14.409 | 14.215 | 14.168 | 14.423 | 14.334 | 14.165 | 14.097 | 14.118 | 14.142 |
| 7d | 15.803 | 15.422 | 15.342 | 15.281 | 15.542 | 15.403 | 15.257 | 15.232 | 15.239 | 15.267 |
| 30d | 14.008 | 13.545 | 13.502 | 13.441 | 13.661 | 13.609 | 13.415 | 13.396 | 13.394 | 13.419 |

## Next candle

- candle starting 2026-10-24 21:42 UTC, last close 2337.13
- P(up) 0.5269, return quantiles (bp): {'05': -5.69, '10': -4.22, '25': -1.958, '40': -0.689, '50': 0.248, '60': 0.908, '75': 2.158, '90': 4.114, '95': 5.412}
- changepoint probability 0.0522, regime age 135.1 min
- agent weights: empirical 0.003, ewma 0.029, garch 0.153, har 0.104, bocpd 0.023, hmm 0.087, online_qr 0.180, lgbm 0.421

## Learning log

- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- HMM volatility states (sd, bp per minute): [4.1, 7.07, 17.69], current probabilities: [0.978, 0.022, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 21:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.369, 'l_abs': 0.643, 'l_hi': 0.779, 'l_lo': 0.781, 'b05': 0.727, 'b25': 0.693, 'b75': 0.609, 'b95': 0.692}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.397, 1.749, 1.869, 2.268, 2.591, 2.918, 3.319, 3.899, 4.201, 4.879, 5.005, 5.433, 5.428, 5.302]}
- calibration offsets (in sigma): {'05': 0.0505, '10': 0.031, '25': 0.0325, '40': 0.014, '50': 0.055, '60': 0.026, '75': -0.0025, '90': -0.061, '95': -0.1005}
