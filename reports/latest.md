# ETH-USD 60s candle generator - report

- generated: 2026-10-24 13:37 UTC
- last closed candle: 2026-10-24 13:37 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.500 (54) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.550 (429) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.599 (157) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.535 (810) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.503 (11340) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.574 (54) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.257 (35) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | 0.667 (30) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.683 (41) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 0.969 (32) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.479 (71) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | 0.867 (30) | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.346 (52) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | 0.750 (32) | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.507 (12527) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07184, 0.1057] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5359, 'levels': [{'threshold': 0.07184, 'calls_per_day': 148.1, 'win_rate': 0.5998}, {'threshold': 0.1057, 'calls_per_day': 37.2, 'win_rate': 0.6412}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 29648, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15153 | 0.337 | 0.525 (14901) | 0.590 (1622) | 0.765 (2500) |
| volatility: normal | 15152 | 0.365 | 0.521 (15087) | 0.622 (1010) | 0.752 (2243) |
| volatility: wild | 15152 | 0.378 | 0.515 (15117) | 0.615 (449) | 0.775 (1943) |
| session: Asia 00-08 | 15360 | 0.358 | 0.526 (15258) | 0.613 (1120) | 0.767 (2224) |
| session: Europe 08-13 | 9600 | 0.355 | 0.521 (9513) | 0.597 (780) | 0.763 (1543) |
| session: US 13-21 | 14917 | 0.368 | 0.516 (14816) | 0.591 (734) | 0.769 (2105) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5518) | 0.615 (447) | 0.741 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.348 | 0.348 | 0.240 | 0.240 | 0.650 | 0.266 | 0.430 | 1.521 |
| 6h | 360 | 0.373 | 0.349 | 0.257 | 0.300 | 0.559 | 0.288 | 0.458 | 1.383 |
| 24h | 1440 | 0.367 | 0.350 | 0.267 | 0.307 | 0.538 | 0.272 | 0.463 | 1.261 |
| 7d | 10080 | 0.370 | 0.360 | 0.272 | 0.305 | 0.536 | 0.268 | 0.472 | 1.215 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.523 | 0.256 | 0.464 | 1.289 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.348 / 0.650 / 0.850; 2: 0.287 / 0.433 / 0.883; 3: 0.353 / 0.617 / 0.900; 4: 0.308 / 0.500 / 0.950; 5: 0.315 / 0.483 / 0.933; 6: 0.303 / 0.433 / 0.967; 7: 0.305 / 0.467 / 0.967; 8: 0.329 / 0.533 / 0.983; 9: 0.316 / 0.500 / 1.000; 10: 0.322 / 0.517 / 1.000; 11: 0.326 / 0.550 / 1.000; 12: 0.355 / 0.617 / 0.983; 13: 0.293 / 0.417 / 0.983; 14: 0.320 / 0.467 / 1.000; 15: 0.306 / 0.417 / 1.000
- 6h: 1: 0.373 / 0.559 / 0.892; 2: 0.340 / 0.480 / 0.903; 3: 0.349 / 0.536 / 0.914; 4: 0.335 / 0.453 / 0.911; 5: 0.346 / 0.511 / 0.917; 6: 0.342 / 0.503 / 0.917; 7: 0.341 / 0.478 / 0.906; 8: 0.350 / 0.511 / 0.903; 9: 0.344 / 0.514 / 0.911; 10: 0.351 / 0.514 / 0.897; 11: 0.341 / 0.497 / 0.908; 12: 0.350 / 0.508 / 0.872; 13: 0.347 / 0.520 / 0.867; 14: 0.334 / 0.494 / 0.875; 15: 0.349 / 0.528 / 0.872
- 24h: 1: 0.367 / 0.538 / 0.900; 2: 0.351 / 0.499 / 0.895; 3: 0.357 / 0.523 / 0.900; 4: 0.346 / 0.485 / 0.899; 5: 0.350 / 0.499 / 0.900; 6: 0.343 / 0.497 / 0.900; 7: 0.346 / 0.490 / 0.898; 8: 0.351 / 0.520 / 0.901; 9: 0.350 / 0.510 / 0.902; 10: 0.349 / 0.502 / 0.895; 11: 0.343 / 0.498 / 0.899; 12: 0.348 / 0.492 / 0.895; 13: 0.348 / 0.515 / 0.892; 14: 0.344 / 0.489 / 0.891; 15: 0.354 / 0.536 / 0.892
- 7d: 1: 0.370 / 0.536 / 0.897; 2: 0.357 / 0.499 / 0.900; 3: 0.359 / 0.510 / 0.900; 4: 0.352 / 0.491 / 0.900; 5: 0.353 / 0.499 / 0.900; 6: 0.353 / 0.497 / 0.900; 7: 0.351 / 0.494 / 0.900; 8: 0.354 / 0.509 / 0.900; 9: 0.351 / 0.499 / 0.901; 10: 0.353 / 0.507 / 0.900; 11: 0.350 / 0.498 / 0.900; 12: 0.351 / 0.502 / 0.900; 13: 0.349 / 0.495 / 0.899; 14: 0.351 / 0.500 / 0.900; 15: 0.350 / 0.502 / 0.900
- 30d: 1: 0.360 / 0.523 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.347 / 0.499 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.503 / 0.900; 14: 0.344 / 0.497 / 0.900; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.089 (body 0.032, range 0.146); 'price stays where it was' would score 0.167; colour right 0.467; typical miss of the close 5.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.134 (body 0.091, range 0.178); 'price stays where it was' would score 0.143; colour right 0.475; typical miss of the close 6.0 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.131 (body 0.092, range 0.169); 'price stays where it was' would score 0.141; colour right 0.507; typical miss of the close 7.2 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.132; colour right 0.506; typical miss of the close 8.8 bp; chain ended on the right side 0.543 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.198 / 4.4; 3: 0.167 / 5.8; 4: 0.130 / 6.4; 5: 0.122 / 7.1; 6: 0.110 / 7.6; 7: 0.104 / 7.9; 8: 0.097 / 8.2; 9: 0.088 / 8.2; 10: 0.086 / 9.0; 11: 0.083 / 9.4; 12: 0.077 / 9.7; 13: 0.068 / 9.9; 14: 0.069 / 10.3; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 118651, probability skill vs chance 0.2336, widened contest next: False
  - now: threshold 0.8357, hit rate recent 0.9523 / long run 0.9374
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.328, naive rule 0.563, lift 2.83x
    - 24h: 59 calls (59 a day), hit rate 0.932, chance 0.297, naive rule 0.524, lift 3.14x
    - 7d: 407 calls (58 a day), hit rate 0.943, chance 0.295, naive rule 0.495, lift 3.20x
    - 30d: 1690 calls (56 a day), hit rate 0.936, chance 0.293, naive rule 0.490, lift 3.19x
  - next: threshold 0.5646, hit rate recent 0.6587 / long run 0.594
    - 6h: 21 calls (85 a day), hit rate 0.762, chance 0.328, lift 2.32x
    - 24h: 59 calls (59 a day), hit rate 0.695, chance 0.297, lift 2.34x
    - 7d: 716 calls (102 a day), hit rate 0.594, chance 0.295, lift 2.02x
    - 30d: 2799 calls (93 a day), hit rate 0.580, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.517; 0.40: 480, 0.573; 0.45: 410, 0.643; 0.50: 358, 0.696; 0.55: 313, 0.738; 0.60: 265, 0.783; 0.65: 222, 0.809; 0.70: 176, 0.840; 0.75: 136, 0.875; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.426; 0.35: 500, 0.463; 0.40: 406, 0.498; 0.45: 310, 0.532; 0.50: 201, 0.564; 0.55: 91, 0.573; 0.60: 14, 0.622; 0.65: 1, 0.710
- **K=5**: model 1792540800, labels learned 118649, probability skill vs chance 0.2231, widened contest next: False
  - now: threshold 0.6754, hit rate recent 0.8206 / long run 0.8222
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.183, naive rule 0.455, lift 4.21x
    - 24h: 52 calls (52 a day), hit rate 0.788, chance 0.188, naive rule 0.424, lift 4.20x
    - 7d: 361 calls (52 a day), hit rate 0.820, chance 0.187, naive rule 0.404, lift 4.39x
    - 30d: 1553 calls (52 a day), hit rate 0.829, chance 0.188, naive rule 0.399, lift 4.42x
  - next: threshold 0.4199, hit rate recent 0.5094 / long run 0.4692
    - 6h: 33 calls (135 a day), hit rate 0.545, chance 0.183, lift 2.99x
    - 24h: 123 calls (124 a day), hit rate 0.504, chance 0.188, lift 2.69x
    - 7d: 951 calls (136 a day), hit rate 0.457, chance 0.187, lift 2.45x
    - 30d: 2792 calls (93 a day), hit rate 0.464, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 344, 0.495; 0.40: 276, 0.566; 0.45: 223, 0.623; 0.50: 176, 0.671; 0.55: 135, 0.711; 0.60: 104, 0.755; 0.65: 76, 0.792; 0.70: 54, 0.829; 0.75: 31, 0.870; 0.80: 10, 0.906
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 251, 0.422; 0.40: 157, 0.450; 0.45: 70, 0.461; 0.50: 15, 0.492; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 118646, probability skill vs chance 0.1929, widened contest next: False
  - now: threshold 0.5604, hit rate recent 0.6672 / long run 0.6829
    - 6h: 17 calls (70 a day), hit rate 0.647, chance 0.116, naive rule 0.361, lift 5.59x
    - 24h: 55 calls (55 a day), hit rate 0.655, chance 0.124, naive rule 0.350, lift 5.26x
    - 7d: 333 calls (48 a day), hit rate 0.661, chance 0.116, naive rule 0.318, lift 5.69x
    - 30d: 1526 calls (51 a day), hit rate 0.701, chance 0.121, naive rule 0.329, lift 5.79x
  - next: threshold 0.3492, hit rate recent 0.3757 / long run 0.375
    - 6h: 27 calls (111 a day), hit rate 0.407, chance 0.116, lift 3.52x
    - 24h: 96 calls (97 a day), hit rate 0.375, chance 0.124, lift 3.01x
    - 7d: 776 calls (111 a day), hit rate 0.370, chance 0.116, lift 3.19x
    - 30d: 2508 calls (84 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 250, 0.424; 0.35: 190, 0.494; 0.40: 145, 0.549; 0.45: 112, 0.594; 0.50: 85, 0.634; 0.55: 62, 0.676; 0.60: 41, 0.722; 0.65: 23, 0.790; 0.70: 10, 0.840; 0.75: 1, 0.821
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.351; 0.35: 99, 0.378; 0.40: 37, 0.402; 0.45: 8, 0.441; 0.50: 1, 0.548
- **K=13**: model 1792800000, labels learned 118641, probability skill vs chance 0.1723, widened contest next: False
  - now: threshold 0.4187, hit rate recent 0.5601 / long run 0.5559
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.067, naive rule 0.269, lift 9.23x
    - 24h: 51 calls (52 a day), hit rate 0.549, chance 0.073, naive rule 0.269, lift 7.49x
    - 7d: 371 calls (53 a day), hit rate 0.528, chance 0.074, naive rule 0.268, lift 7.11x
    - 30d: 1558 calls (52 a day), hit rate 0.569, chance 0.077, naive rule 0.272, lift 7.36x
  - next: threshold 0.2867, hit rate recent 0.2774 / long run 0.3073
    - 6h: 20 calls (83 a day), hit rate 0.350, chance 0.067, lift 5.25x
    - 24h: 58 calls (59 a day), hit rate 0.224, chance 0.073, lift 3.06x
    - 7d: 477 calls (68 a day), hit rate 0.306, chance 0.074, lift 4.12x
    - 30d: 2160 calls (72 a day), hit rate 0.305, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.445; 0.35: 87, 0.497; 0.40: 61, 0.553; 0.45: 41, 0.608; 0.50: 25, 0.661; 0.55: 14, 0.711; 0.60: 6, 0.758; 0.65: 2, 0.851
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.316; 0.35: 13, 0.353; 0.40: 2, 0.435; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.883 | 0.33% | 0.850 | 0.567 | 0.249 | 0.567 | 0.009 |
| 6h | 10.020 | 2.44% | 0.894 | 0.511 | 0.251 | 0.478 | 0.309 |
| 24h | 12.764 | 4.38% | 0.906 | 0.515 | 0.251 | 0.487 | 0.703 |
| 7d | 14.890 | 3.26% | 0.901 | 0.501 | 0.250 | 0.501 | 0.637 |
| 30d | 13.419 | 4.14% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.916 | 9.843 | 9.865 | 9.846 | 9.928 | 9.898 | 9.931 | 9.878 | 9.874 | 9.883 |
| 6h | 10.271 | 10.072 | 10.075 | 10.016 | 10.195 | 10.219 | 10.025 | 10.004 | 10.005 | 10.020 |
| 24h | 13.348 | 12.908 | 12.844 | 12.731 | 13.031 | 12.998 | 12.739 | 12.756 | 12.737 | 12.764 |
| 7d | 15.392 | 15.032 | 14.962 | 14.897 | 15.147 | 15.027 | 14.875 | 14.862 | 14.863 | 14.890 |
| 30d | 13.999 | 13.542 | 13.502 | 13.439 | 13.662 | 13.610 | 13.414 | 13.397 | 13.394 | 13.419 |

## Next candle

- candle starting 2026-10-24 13:37 UTC, last close 2363.58
- P(up) 0.4763, return quantiles (bp): {'05': -6.221, '10': -4.734, '25': -2.253, '40': -0.855, '50': -0.164, '60': 0.543, '75': 2.252, '90': 4.549, '95': 5.684}
- changepoint probability 0.0397, regime age 157.3 min
- agent weights: empirical 0.007, ewma 0.093, garch 0.109, har 0.266, bocpd 0.037, hmm 0.026, online_qr 0.230, lgbm 0.233

## Learning log

- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- HMM volatility states (sd, bp per minute): [4.1, 7.07, 17.69], current probabilities: [0.969, 0.03, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 13:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.341, 'l_abs': 0.688, 'l_hi': 0.787, 'l_lo': 0.798, 'b05': 0.725, 'b25': 0.735, 'b75': 0.613, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.6, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.591, 1.732, 2.004, 2.072, 2.23, 2.413, 2.69, 2.693, 3.143, 2.989, 3.598, 3.678, 3.902, 3.967]}
- calibration offsets (in sigma): {'05': 0.018, '10': -0.004, '25': 0.04, '40': -0.006, '50': -0.04, '60': -0.084, '75': -0.05, '90': -0.066, '95': -0.138}
