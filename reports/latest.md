# ETH-USD 60s candle generator - report

- generated: 2026-10-28 05:33 UTC
- last closed candle: 2026-10-28 05:33 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.537 (672) [0.501, 0.574] | 0.520 (2876) [0.500, 0.539] | 0.517 (5370) [0.503, 0.530] | 0.523 (2398) [0.501, 0.546] | 0.636 (22) | 0.500 | flat +0.003 (noise 0.032) |
| colour_clear | 0.556 (840) | 0.544 (5696) [0.540, 0.549] | 0.537 (23618) [0.530, 0.544] | 0.519 (43957) [0.512, 0.525] | 0.546 (19719) [0.542, 0.551] | 0.572 (201) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.596 (161) | 0.604 (1371) [0.591, 0.619] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.500 (32) | 0.500 | flat +0.010 (noise 0.021) |
| colour_next | 0.530 (1430) | 0.528 (10030) [0.525, 0.532] | 0.525 (42880) [0.521, 0.530] | 0.513 (80052) [0.509, 0.517] | 0.529 (35703) [0.525, 0.533] | 0.530 (332) | 0.500 | flat -0.007 (noise 0.007) |
| colour_path | 0.506 (20020) | 0.502 (140420) [0.500, 0.504] | 0.501 (600320) [0.499, 0.503] | 0.501 (1120728) [0.500, 0.502] | 0.501 (499842) [0.499, 0.502] | 0.498 (4648) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.596 (47) | 0.614 (412) [0.596, 0.644] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.667 (6) | 0.500 | flat -0.015 (noise 0.041) |
| reversal_k13_next | 0.451 (51) | 0.321 (417) [0.287, 0.360] | 0.309 (2160) [0.297, 0.322] | 0.309 (3794) [0.298, 0.320] | 0.320 (1689) [0.308, 0.333] | 0.250 (12) | 0.077 | flat +0.007 (noise 0.032) |
| reversal_k13_now | 0.643 (56) | 0.565 (375) [0.516, 0.620] | 0.561 (1611) [0.541, 0.582] | 0.572 (2832) [0.557, 0.588] | 0.563 (1360) [0.541, 0.587] | 0.611 (18) | 0.077 | flat +0.046 (noise 0.036) |
| reversal_k3_next | 0.569 (123) | 0.607 (679) [0.587, 0.629] | 0.584 (2878) [0.572, 0.597] | 0.584 (4882) [0.574, 0.594] | 0.580 (2442) [0.567, 0.593] | 0.583 (24) | 0.293 | flat +0.045 (noise 0.026) |
| reversal_k3_now | 0.969 (65) | 0.955 (397) [0.931, 0.974] | 0.937 (1714) [0.927, 0.946] | 0.939 (3191) [0.932, 0.946] | 0.935 (1428) [0.924, 0.946] | 0.846 (13) | 0.293 | flat +0.025 (noise 0.019) |
| reversal_k5_next | 0.530 (66) | 0.499 (830) [0.489, 0.511] | 0.467 (3054) [0.453, 0.480] | 0.478 (4619) [0.466, 0.490] | 0.466 (2629) [0.451, 0.481] | 0.667 (15) | 0.187 | up +0.060 (noise 0.024) |
| reversal_k5_now | 0.845 (58) | 0.821 (369) [0.809, 0.833] | 0.826 (1581) [0.814, 0.837] | 0.830 (2932) [0.820, 0.841] | 0.821 (1321) [0.809, 0.834] | 0.824 (17) | 0.187 | flat -0.001 (noise 0.028) |
| reversal_k8_next | 0.396 (101) | 0.382 (747) [0.362, 0.400] | 0.381 (2684) [0.369, 0.394] | 0.388 (4517) [0.377, 0.399] | 0.381 (2411) [0.368, 0.394] | 0.421 (19) | 0.120 | flat +0.020 (noise 0.025) |
| reversal_k8_now | 0.732 (56) | 0.674 (356) [0.624, 0.726] | 0.686 (1533) [0.665, 0.705] | 0.700 (2898) [0.685, 0.715] | 0.683 (1311) [0.660, 0.706] | 0.833 (12) | 0.121 | flat +0.010 (noise 0.037) |
| overall | 0.510 (22122) | 0.506 (155292) [0.503, 0.508] | 0.504 (663291) [0.503, 0.506] | 0.503 (1235815) [0.502, 0.504] | 0.504 (552534) [0.503, 0.506] | 0.504 (5132) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08028, 0.121] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5277, 'levels': [{'threshold': 0.08028, 'calls_per_day': 145.3, 'win_rate': 0.6086}, {'threshold': 0.121, 'calls_per_day': 36.4, 'win_rate': 0.6133}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 34896, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14991 | 0.338 | 0.523 (14765) | 0.586 (1840) | 0.760 (2535) |
| volatility: normal | 14991 | 0.366 | 0.528 (14922) | 0.612 (1313) | 0.751 (2204) |
| volatility: wild | 14991 | 0.380 | 0.522 (14947) | 0.625 (661) | 0.765 (1949) |
| session: Asia 00-08 | 15213 | 0.360 | 0.531 (15108) | 0.606 (1356) | 0.760 (2232) |
| session: Europe 08-13 | 9300 | 0.357 | 0.529 (9217) | 0.596 (931) | 0.754 (1508) |
| session: US 13-21 | 14880 | 0.369 | 0.520 (14783) | 0.597 (976) | 0.769 (2111) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5526) | 0.608 (551) | 0.736 (837) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.330 | 0.331 | 0.233 | 0.233 | 0.400 | 0.225 | 0.434 | 1.263 |
| 6h | 360 | 0.376 | 0.359 | 0.283 | 0.297 | 0.535 | 0.293 | 0.459 | 1.239 |
| 24h | 1440 | 0.371 | 0.363 | 0.294 | 0.322 | 0.528 | 0.266 | 0.475 | 1.267 |
| 7d | 10080 | 0.368 | 0.359 | 0.280 | 0.311 | 0.529 | 0.266 | 0.471 | 1.231 |
| 30d | 43200 | 0.362 | 0.355 | 0.278 | 0.307 | 0.525 | 0.258 | 0.465 | 1.278 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.330 / 0.400 / 0.917; 2: 0.336 / 0.467 / 0.950; 3: 0.343 / 0.550 / 0.950; 4: 0.360 / 0.517 / 0.950; 5: 0.305 / 0.333 / 0.983; 6: 0.335 / 0.500 / 0.933; 7: 0.313 / 0.400 / 0.917; 8: 0.321 / 0.433 / 0.900; 9: 0.357 / 0.517 / 0.950; 10: 0.323 / 0.433 / 0.917; 11: 0.357 / 0.617 / 0.933; 12: 0.312 / 0.367 / 0.983; 13: 0.354 / 0.517 / 0.967; 14: 0.351 / 0.517 / 0.967; 15: 0.340 / 0.500 / 0.967
- 6h: 1: 0.376 / 0.535 / 0.906; 2: 0.349 / 0.479 / 0.914; 3: 0.366 / 0.518 / 0.906; 4: 0.350 / 0.487 / 0.911; 5: 0.354 / 0.476 / 0.917; 6: 0.356 / 0.510 / 0.900; 7: 0.356 / 0.490 / 0.889; 8: 0.358 / 0.496 / 0.875; 9: 0.355 / 0.504 / 0.889; 10: 0.357 / 0.479 / 0.861; 11: 0.353 / 0.510 / 0.853; 12: 0.357 / 0.513 / 0.869; 13: 0.351 / 0.479 / 0.858; 14: 0.363 / 0.543 / 0.858; 15: 0.360 / 0.524 / 0.847
- 24h: 1: 0.371 / 0.528 / 0.892; 2: 0.358 / 0.493 / 0.902; 3: 0.370 / 0.523 / 0.902; 4: 0.357 / 0.490 / 0.905; 5: 0.363 / 0.523 / 0.902; 6: 0.356 / 0.504 / 0.897; 7: 0.360 / 0.505 / 0.895; 8: 0.365 / 0.518 / 0.892; 9: 0.353 / 0.490 / 0.897; 10: 0.361 / 0.499 / 0.892; 11: 0.356 / 0.510 / 0.887; 12: 0.359 / 0.502 / 0.891; 13: 0.358 / 0.502 / 0.889; 14: 0.362 / 0.529 / 0.885; 15: 0.358 / 0.494 / 0.883
- 7d: 1: 0.368 / 0.529 / 0.896; 2: 0.356 / 0.496 / 0.900; 3: 0.359 / 0.512 / 0.899; 4: 0.354 / 0.498 / 0.900; 5: 0.355 / 0.507 / 0.900; 6: 0.353 / 0.502 / 0.900; 7: 0.353 / 0.500 / 0.899; 8: 0.355 / 0.508 / 0.899; 9: 0.353 / 0.501 / 0.899; 10: 0.352 / 0.504 / 0.899; 11: 0.350 / 0.499 / 0.898; 12: 0.352 / 0.505 / 0.899; 13: 0.350 / 0.497 / 0.899; 14: 0.351 / 0.500 / 0.899; 15: 0.351 / 0.502 / 0.898
- 30d: 1: 0.362 / 0.525 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.347 / 0.497 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.347 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.091 (body 0.059, range 0.124); 'price stays where it was' would score 0.122; colour right 0.467; typical miss of the close 7.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.133 (body 0.094, range 0.172); 'price stays where it was' would score 0.134; colour right 0.524; typical miss of the close 6.8 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.128 (body 0.084, range 0.172); 'price stays where it was' would score 0.140; colour right 0.505; typical miss of the close 8.2 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.138; colour right 0.498; typical miss of the close 8.6 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.128; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.1; 2: 0.198 / 4.6; 3: 0.170 / 6.1; 4: 0.132 / 6.6; 5: 0.125 / 7.2; 6: 0.112 / 7.8; 7: 0.107 / 8.1; 8: 0.095 / 8.5; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.086 / 9.7; 12: 0.077 / 10.0; 13: 0.068 / 10.2; 14: 0.070 / 10.6; 15: 0.061 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 123927, probability skill vs chance 0.2425, widened contest next: False
  - now: threshold 0.8347, hit rate recent 0.9429 / long run 0.9395
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.283, naive rule 0.486, lift 2.99x
    - 24h: 60 calls (60 a day), hit rate 0.950, chance 0.279, naive rule 0.474, lift 3.40x
    - 7d: 395 calls (56 a day), hit rate 0.952, chance 0.297, naive rule 0.503, lift 3.21x
    - 30d: 1719 calls (57 a day), hit rate 0.936, chance 0.293, naive rule 0.491, lift 3.19x
  - next: threshold 0.5326, hit rate recent 0.5663 / long run 0.586
    - 6h: 25 calls (101 a day), hit rate 0.560, chance 0.283, lift 1.98x
    - 24h: 115 calls (115 a day), hit rate 0.557, chance 0.279, lift 1.99x
    - 7d: 666 calls (95 a day), hit rate 0.598, chance 0.297, lift 2.01x
    - 30d: 2879 calls (96 a day), hit rate 0.582, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 538, 0.519; 0.40: 477, 0.576; 0.45: 408, 0.647; 0.50: 357, 0.698; 0.55: 312, 0.740; 0.60: 264, 0.785; 0.65: 221, 0.811; 0.70: 175, 0.843; 0.75: 137, 0.875; 0.80: 92, 0.914; 0.85: 47, 0.950; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 501, 0.466; 0.40: 407, 0.500; 0.45: 310, 0.534; 0.50: 200, 0.570; 0.55: 89, 0.573; 0.60: 14, 0.642; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 123925, probability skill vs chance 0.2299, widened contest next: False
  - now: threshold 0.6717, hit rate recent 0.834 / long run 0.8241
    - 6h: 17 calls (69 a day), hit rate 0.824, chance 0.201, naive rule 0.419, lift 4.09x
    - 24h: 62 calls (62 a day), hit rate 0.855, chance 0.196, naive rule 0.414, lift 4.37x
    - 7d: 373 calls (53 a day), hit rate 0.823, chance 0.187, naive rule 0.410, lift 4.40x
    - 30d: 1592 calls (53 a day), hit rate 0.825, chance 0.188, naive rule 0.402, lift 4.39x
  - next: threshold 0.4475, hit rate recent 0.5455 / long run 0.4902
    - 6h: 16 calls (65 a day), hit rate 0.625, chance 0.201, lift 3.11x
    - 24h: 68 calls (68 a day), hit rate 0.529, chance 0.196, lift 2.70x
    - 7d: 815 calls (117 a day), hit rate 0.499, chance 0.187, lift 2.67x
    - 30d: 3056 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 345, 0.493; 0.40: 278, 0.566; 0.45: 226, 0.620; 0.50: 178, 0.669; 0.55: 138, 0.709; 0.60: 106, 0.752; 0.65: 76, 0.788; 0.70: 51, 0.828; 0.75: 30, 0.872; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.391; 0.35: 254, 0.422; 0.40: 159, 0.455; 0.45: 70, 0.472; 0.50: 15, 0.492; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 123922, probability skill vs chance 0.207, widened contest next: False
  - now: threshold 0.5577, hit rate recent 0.7151 / long run 0.6815
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.117, naive rule 0.328, lift 7.11x
    - 24h: 54 calls (54 a day), hit rate 0.778, chance 0.126, naive rule 0.350, lift 6.20x
    - 7d: 356 calls (51 a day), hit rate 0.683, chance 0.118, naive rule 0.329, lift 5.80x
    - 30d: 1539 calls (51 a day), hit rate 0.686, chance 0.121, naive rule 0.331, lift 5.68x
  - next: threshold 0.3349, hit rate recent 0.3937 / long run 0.3796
    - 6h: 20 calls (82 a day), hit rate 0.400, chance 0.117, lift 3.41x
    - 24h: 100 calls (101 a day), hit rate 0.390, chance 0.126, lift 3.11x
    - 7d: 739 calls (106 a day), hit rate 0.382, chance 0.118, lift 3.24x
    - 30d: 2695 calls (90 a day), hit rate 0.381, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.428; 0.35: 188, 0.496; 0.40: 146, 0.546; 0.45: 111, 0.591; 0.50: 84, 0.633; 0.55: 60, 0.671; 0.60: 40, 0.711; 0.65: 23, 0.779; 0.70: 10, 0.821; 0.75: 2, 0.818
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.355; 0.35: 94, 0.383; 0.40: 33, 0.405; 0.45: 7, 0.430; 0.50: 1, 0.621
- **K=13**: model 1793059200, labels learned 123917, probability skill vs chance 0.1994, widened contest next: False
  - now: threshold 0.4049, hit rate recent 0.5974 / long run 0.5601
    - 6h: 18 calls (75 a day), hit rate 0.611, chance 0.078, naive rule 0.271, lift 7.81x
    - 24h: 63 calls (64 a day), hit rate 0.651, chance 0.083, naive rule 0.314, lift 7.83x
    - 7d: 384 calls (55 a day), hit rate 0.570, chance 0.075, naive rule 0.275, lift 7.64x
    - 30d: 1621 calls (54 a day), hit rate 0.563, chance 0.077, naive rule 0.273, lift 7.32x
  - next: threshold 0.2947, hit rate recent 0.3533 / long run 0.3197
    - 6h: 12 calls (50 a day), hit rate 0.250, chance 0.078, lift 3.19x
    - 24h: 53 calls (54 a day), hit rate 0.415, chance 0.083, lift 4.99x
    - 7d: 413 calls (59 a day), hit rate 0.312, chance 0.075, lift 4.18x
    - 30d: 2154 calls (72 a day), hit rate 0.308, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.440; 0.35: 89, 0.491; 0.40: 63, 0.547; 0.45: 42, 0.598; 0.50: 27, 0.659; 0.55: 16, 0.707; 0.60: 7, 0.752; 0.65: 2, 0.804
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.361; 0.40: 2, 0.451; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.809 | 4.25% | 0.933 | 0.467 | 0.251 | 0.383 | 0.170 |
| 6h | 11.063 | 1.44% | 0.906 | 0.478 | 0.250 | 0.482 | 0.306 |
| 24h | 13.142 | 1.61% | 0.899 | 0.503 | 0.251 | 0.493 | 0.542 |
| 7d | 14.750 | 3.36% | 0.900 | 0.500 | 0.250 | 0.500 | 0.651 |
| 30d | 13.801 | 4.06% | 0.900 | 0.500 | 0.251 | 0.495 | 0.666 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.200 | 8.853 | 8.936 | 8.775 | 8.982 | 8.939 | 8.752 | 8.761 | 8.790 | 8.809 |
| 6h | 11.224 | 11.107 | 11.109 | 11.085 | 11.228 | 11.116 | 11.036 | 11.027 | 11.033 | 11.063 |
| 24h | 13.357 | 13.220 | 13.209 | 13.188 | 13.360 | 13.203 | 13.112 | 13.103 | 13.110 | 13.142 |
| 7d | 15.263 | 14.894 | 14.840 | 14.778 | 15.015 | 14.894 | 14.735 | 14.709 | 14.721 | 14.750 |
| 30d | 14.385 | 13.934 | 13.884 | 13.826 | 14.047 | 13.979 | 13.795 | 13.775 | 13.774 | 13.801 |

## Next candle

- candle starting 2026-10-28 05:33 UTC, last close 2351.34
- P(up) 0.4982, return quantiles (bp): {'05': -6.182, '10': -4.862, '25': -2.419, '40': -0.872, '50': -0.013, '60': 0.802, '75': 2.328, '90': 4.615, '95': 6.528}
- changepoint probability 0.0487, regime age 122.0 min
- agent weights: empirical 0.027, ewma 0.103, garch 0.106, har 0.138, bocpd 0.034, hmm 0.116, online_qr 0.235, lgbm 0.241

## Learning log

- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.41, 6.59, 17.7], current probabilities: [0.753, 0.237, 0.009]
- live generator: {'versions': 60, 'latest_effective': '2026-10-28 05:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.302, 'l_abs': 0.695, 'l_hi': 0.749, 'l_lo': 0.767, 'b05': 0.726, 'b25': 0.772, 'b75': 0.652, 'b95': 0.684}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.367, 1.644, 1.902, 2.007, 2.387, 2.583, 2.997, 2.941, 3.573, 3.987, 3.775, 4.017, 4.261, 4.884]}
- calibration offsets (in sigma): {'05': 0.046, '10': -0.028, '25': -0.03, '40': -0.012, '50': -0.01, '60': -0.018, '75': -0.0, '90': -0.032, '95': 0.044}
