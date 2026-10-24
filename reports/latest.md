# ETH-USD 60s candle generator - report

- generated: 2026-10-24 16:57 UTC
- last closed candle: 2026-10-24 16:57 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.492 (67) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.542 (533) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.603 (179) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.525 (1010) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.500 (14140) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.571 (63) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.233 (43) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | 0.600 (40) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.652 (46) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 0.974 (39) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.506 (87) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | 0.829 (41) | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.379 (66) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | 0.691 (42) | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.503 (15621) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07184, 0.1057] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5359, 'levels': [{'threshold': 0.07184, 'calls_per_day': 148.1, 'win_rate': 0.5998}, {'threshold': 0.1057, 'calls_per_day': 37.2, 'win_rate': 0.6412}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 29848, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15220 | 0.337 | 0.525 (14968) | 0.590 (1636) | 0.765 (2513) |
| volatility: normal | 15218 | 0.365 | 0.521 (15153) | 0.623 (1012) | 0.752 (2255) |
| volatility: wild | 15219 | 0.378 | 0.514 (15184) | 0.615 (455) | 0.772 (1956) |
| session: Asia 00-08 | 15360 | 0.358 | 0.526 (15258) | 0.613 (1120) | 0.767 (2224) |
| session: Europe 08-13 | 9600 | 0.355 | 0.521 (9513) | 0.597 (780) | 0.763 (1543) |
| session: US 13-21 | 15117 | 0.368 | 0.516 (15016) | 0.593 (756) | 0.767 (2143) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5518) | 0.615 (447) | 0.741 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.344 | 0.349 | 0.345 | 0.345 | 0.400 | 0.229 | 0.460 | 1.509 |
| 6h | 360 | 0.364 | 0.354 | 0.291 | 0.320 | 0.525 | 0.266 | 0.462 | 0.947 |
| 24h | 1440 | 0.364 | 0.350 | 0.272 | 0.308 | 0.525 | 0.268 | 0.460 | 1.191 |
| 7d | 10080 | 0.370 | 0.361 | 0.273 | 0.306 | 0.535 | 0.268 | 0.473 | 1.206 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.523 | 0.256 | 0.464 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.344 / 0.400 / 0.950; 2: 0.362 / 0.483 / 0.967; 3: 0.340 / 0.400 / 0.933; 4: 0.333 / 0.433 / 0.917; 5: 0.390 / 0.600 / 0.900; 6: 0.334 / 0.417 / 0.850; 7: 0.385 / 0.583 / 0.850; 8: 0.346 / 0.467 / 0.850; 9: 0.332 / 0.400 / 0.783; 10: 0.376 / 0.567 / 0.867; 11: 0.332 / 0.383 / 0.817; 12: 0.357 / 0.550 / 0.867; 13: 0.351 / 0.500 / 0.883; 14: 0.323 / 0.350 / 0.867; 15: 0.361 / 0.550 / 0.867
- 6h: 1: 0.364 / 0.525 / 0.908; 2: 0.339 / 0.480 / 0.917; 3: 0.350 / 0.514 / 0.906; 4: 0.332 / 0.466 / 0.906; 5: 0.355 / 0.542 / 0.883; 6: 0.327 / 0.447 / 0.886; 7: 0.340 / 0.511 / 0.886; 8: 0.344 / 0.522 / 0.881; 9: 0.323 / 0.450 / 0.858; 10: 0.346 / 0.550 / 0.883; 11: 0.336 / 0.492 / 0.856; 12: 0.342 / 0.525 / 0.856; 13: 0.331 / 0.486 / 0.858; 14: 0.323 / 0.458 / 0.847; 15: 0.333 / 0.486 / 0.836
- 24h: 1: 0.364 / 0.525 / 0.902; 2: 0.349 / 0.494 / 0.894; 3: 0.353 / 0.515 / 0.892; 4: 0.341 / 0.472 / 0.889; 5: 0.351 / 0.508 / 0.887; 6: 0.340 / 0.490 / 0.888; 7: 0.345 / 0.494 / 0.890; 8: 0.350 / 0.522 / 0.892; 9: 0.347 / 0.506 / 0.887; 10: 0.346 / 0.503 / 0.885; 11: 0.342 / 0.497 / 0.879; 12: 0.344 / 0.490 / 0.880; 13: 0.345 / 0.517 / 0.880; 14: 0.338 / 0.481 / 0.876; 15: 0.350 / 0.533 / 0.876
- 7d: 1: 0.370 / 0.535 / 0.898; 2: 0.357 / 0.499 / 0.900; 3: 0.359 / 0.511 / 0.899; 4: 0.352 / 0.490 / 0.899; 5: 0.354 / 0.500 / 0.899; 6: 0.353 / 0.496 / 0.899; 7: 0.352 / 0.495 / 0.899; 8: 0.355 / 0.511 / 0.899; 9: 0.351 / 0.498 / 0.898; 10: 0.353 / 0.508 / 0.898; 11: 0.350 / 0.497 / 0.898; 12: 0.351 / 0.502 / 0.898; 13: 0.349 / 0.494 / 0.898; 14: 0.350 / 0.498 / 0.897; 15: 0.350 / 0.502 / 0.897
- 30d: 1: 0.360 / 0.523 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.497 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.347 / 0.499 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.346 / 0.503 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.344 / 0.497 / 0.900; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.108 (body 0.071, range 0.145); 'price stays where it was' would score 0.132; colour right 0.467; typical miss of the close 21.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.088, range 0.165); 'price stays where it was' would score 0.150; colour right 0.447; typical miss of the close 9.0 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.123 (body 0.085, range 0.160); 'price stays where it was' would score 0.139; colour right 0.498; typical miss of the close 7.3 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 8.9 bp; chain ended on the right side 0.539 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.517 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.198 / 4.4; 3: 0.167 / 5.8; 4: 0.130 / 6.4; 5: 0.122 / 7.1; 6: 0.110 / 7.6; 7: 0.104 / 7.9; 8: 0.097 / 8.3; 9: 0.087 / 8.2; 10: 0.087 / 9.0; 11: 0.083 / 9.4; 12: 0.077 / 9.8; 13: 0.068 / 9.9; 14: 0.068 / 10.3; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 118851, probability skill vs chance 0.231, widened contest next: False
  - now: threshold 0.8357, hit rate recent 0.9576 / long run 0.9381
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.325, naive rule 0.528, lift 2.88x
    - 24h: 57 calls (57 a day), hit rate 0.947, chance 0.299, naive rule 0.520, lift 3.17x
    - 7d: 407 calls (58 a day), hit rate 0.943, chance 0.295, naive rule 0.495, lift 3.20x
    - 30d: 1690 calls (56 a day), hit rate 0.936, chance 0.293, naive rule 0.490, lift 3.19x
  - next: threshold 0.5646, hit rate recent 0.6381 / long run 0.5924
    - 6h: 16 calls (65 a day), hit rate 0.562, chance 0.325, lift 1.73x
    - 24h: 60 calls (60 a day), hit rate 0.667, chance 0.299, lift 2.23x
    - 7d: 711 calls (102 a day), hit rate 0.594, chance 0.295, lift 2.01x
    - 30d: 2798 calls (93 a day), hit rate 0.580, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.517; 0.40: 479, 0.573; 0.45: 410, 0.644; 0.50: 357, 0.697; 0.55: 312, 0.739; 0.60: 265, 0.783; 0.65: 222, 0.809; 0.70: 175, 0.840; 0.75: 136, 0.874; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.426; 0.35: 500, 0.463; 0.40: 406, 0.498; 0.45: 310, 0.532; 0.50: 201, 0.564; 0.55: 91, 0.573; 0.60: 14, 0.623; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 118849, probability skill vs chance 0.2276, widened contest next: False
  - now: threshold 0.6754, hit rate recent 0.8038 / long run 0.8205
    - 6h: 20 calls (82 a day), hit rate 0.800, chance 0.184, naive rule 0.462, lift 4.34x
    - 24h: 57 calls (57 a day), hit rate 0.789, chance 0.182, naive rule 0.416, lift 4.33x
    - 7d: 361 calls (52 a day), hit rate 0.814, chance 0.186, naive rule 0.404, lift 4.37x
    - 30d: 1556 calls (52 a day), hit rate 0.829, chance 0.188, naive rule 0.399, lift 4.41x
  - next: threshold 0.4199, hit rate recent 0.5423 / long run 0.4734
    - 6h: 30 calls (122 a day), hit rate 0.600, chance 0.184, lift 3.26x
    - 24h: 125 calls (126 a day), hit rate 0.504, chance 0.182, lift 2.77x
    - 7d: 948 calls (136 a day), hit rate 0.459, chance 0.186, lift 2.46x
    - 30d: 2806 calls (94 a day), hit rate 0.465, chance 0.188, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 344, 0.495; 0.40: 276, 0.566; 0.45: 223, 0.623; 0.50: 176, 0.672; 0.55: 135, 0.712; 0.60: 104, 0.755; 0.65: 76, 0.792; 0.70: 54, 0.829; 0.75: 31, 0.872; 0.80: 10, 0.907
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.391; 0.35: 251, 0.423; 0.40: 157, 0.450; 0.45: 70, 0.462; 0.50: 15, 0.492; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 118846, probability skill vs chance 0.198, widened contest next: True
  - now: threshold 0.5604, hit rate recent 0.6399 / long run 0.6799
    - 6h: 17 calls (70 a day), hit rate 0.588, chance 0.136, naive rule 0.400, lift 4.33x
    - 24h: 59 calls (59 a day), hit rate 0.627, chance 0.127, naive rule 0.353, lift 4.93x
    - 7d: 334 calls (48 a day), hit rate 0.656, chance 0.116, naive rule 0.317, lift 5.66x
    - 30d: 1524 calls (51 a day), hit rate 0.699, chance 0.121, naive rule 0.329, lift 5.78x
  - next: threshold 0.3492, hit rate recent 0.4037 / long run 0.3779
    - 6h: 23 calls (95 a day), hit rate 0.478, chance 0.136, lift 3.52x
    - 24h: 97 calls (98 a day), hit rate 0.381, chance 0.127, lift 3.00x
    - 7d: 772 calls (110 a day), hit rate 0.370, chance 0.116, lift 3.20x
    - 30d: 2513 calls (84 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 250, 0.425; 0.35: 190, 0.495; 0.40: 145, 0.550; 0.45: 111, 0.594; 0.50: 85, 0.634; 0.55: 62, 0.675; 0.60: 41, 0.721; 0.65: 23, 0.787; 0.70: 10, 0.838; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.351; 0.35: 99, 0.378; 0.40: 37, 0.401; 0.45: 8, 0.435; 0.50: 1, 0.567
- **K=13**: model 1792800000, labels learned 118841, probability skill vs chance 0.1661, widened contest next: True
  - now: threshold 0.4187, hit rate recent 0.5359 / long run 0.5533
    - 6h: 13 calls (54 a day), hit rate 0.538, chance 0.058, naive rule 0.247, lift 9.29x
    - 24h: 55 calls (56 a day), hit rate 0.527, chance 0.070, naive rule 0.262, lift 7.55x
    - 7d: 370 calls (53 a day), hit rate 0.524, chance 0.074, naive rule 0.266, lift 7.11x
    - 30d: 1559 calls (52 a day), hit rate 0.567, chance 0.077, naive rule 0.272, lift 7.35x
  - next: threshold 0.2867, hit rate recent 0.2586 / long run 0.3048
    - 6h: 16 calls (67 a day), hit rate 0.250, chance 0.058, lift 4.31x
    - 24h: 58 calls (59 a day), hit rate 0.224, chance 0.070, lift 3.21x
    - 7d: 477 calls (68 a day), hit rate 0.302, chance 0.074, lift 4.10x
    - 30d: 2162 calls (72 a day), hit rate 0.303, chance 0.077, lift 3.93x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.445; 0.35: 87, 0.497; 0.40: 61, 0.552; 0.45: 41, 0.605; 0.50: 25, 0.657; 0.55: 14, 0.704; 0.60: 6, 0.751; 0.65: 2, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.314; 0.35: 13, 0.350; 0.40: 2, 0.429; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 23.054 | 3.94% | 0.883 | 0.467 | 0.259 | 0.417 | 0.267 |
| 6h | 20.595 | 9.41% | 0.900 | 0.514 | 0.252 | 0.492 | 0.692 |
| 24h | 13.840 | 6.27% | 0.904 | 0.508 | 0.251 | 0.488 | 0.704 |
| 7d | 15.253 | 3.59% | 0.901 | 0.501 | 0.250 | 0.502 | 0.648 |
| 30d | 13.436 | 4.20% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 24.001 | 23.258 | 22.732 | 23.163 | 22.359 | 22.623 | 23.134 | 22.755 | 22.815 | 23.054 |
| 6h | 22.735 | 21.133 | 20.706 | 20.668 | 20.984 | 20.771 | 20.676 | 20.443 | 20.564 | 20.595 |
| 24h | 14.766 | 14.094 | 13.928 | 13.831 | 14.106 | 14.042 | 13.846 | 13.808 | 13.815 | 13.840 |
| 7d | 15.822 | 15.413 | 15.327 | 15.262 | 15.519 | 15.390 | 15.241 | 15.217 | 15.224 | 15.253 |
| 30d | 14.025 | 13.562 | 13.519 | 13.457 | 13.678 | 13.626 | 13.431 | 13.413 | 13.411 | 13.436 |

## Next candle

- candle starting 2026-10-24 16:57 UTC, last close 2316.22
- P(up) 0.4664, return quantiles (bp): {'05': -14.112, '10': -10.639, '25': -5.064, '40': -2.782, '50': -0.663, '60': 1.357, '75': 4.957, '90': 8.867, '95': 11.872}
- changepoint probability 0.0906, regime age 80.7 min
- agent weights: empirical 0.003, ewma 0.010, garch 0.092, har 0.162, bocpd 0.014, hmm 0.042, online_qr 0.166, lgbm 0.512

## Learning log

- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- HMM volatility states (sd, bp per minute): [4.1, 7.07, 17.69], current probabilities: [0.125, 0.831, 0.044]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 17:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.38, 'l_abs': 0.648, 'l_hi': 0.792, 'l_lo': 0.792, 'b05': 0.733, 'b25': 0.704, 'b75': 0.625, 'b95': 0.7}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6]], 'cone_width': [1.529, 1.992, 2.448, 2.854, 3.071, 3.193, 3.56, 4.266, 4.329, 5.028, 5.262, 5.488, 6.434, 6.673]}
- calibration offsets (in sigma): {'05': 0.008, '10': 0.006, '25': 0.06, '40': -0.026, '50': -0.03, '60': -0.024, '75': -0.01, '90': -0.096, '95': -0.138}
