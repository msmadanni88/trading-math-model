# ETH-USD 60s candle generator - report

- generated: 2026-10-28 21:48 UTC
- last closed candle: 2026-10-28 21:48 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.537 (672) [0.501, 0.574] | 0.520 (2876) [0.500, 0.539] | 0.517 (5370) [0.503, 0.530] | 0.523 (2398) [0.501, 0.546] | 0.563 (87) | 0.500 | flat +0.003 (noise 0.032) |
| colour_clear | 0.556 (840) | 0.544 (5696) [0.540, 0.549] | 0.537 (23618) [0.530, 0.544] | 0.519 (43957) [0.512, 0.525] | 0.546 (19719) [0.542, 0.551] | 0.537 (726) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.596 (161) | 0.604 (1371) [0.591, 0.619] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.556 (115) | 0.500 | flat +0.010 (noise 0.021) |
| colour_next | 0.530 (1430) | 0.528 (10030) [0.525, 0.532] | 0.525 (42880) [0.521, 0.530] | 0.513 (80052) [0.509, 0.517] | 0.529 (35703) [0.525, 0.533] | 0.527 (1299) | 0.500 | flat -0.007 (noise 0.007) |
| colour_path | 0.506 (20020) | 0.502 (140420) [0.500, 0.504] | 0.501 (600320) [0.499, 0.503] | 0.501 (1120728) [0.500, 0.502] | 0.501 (499842) [0.499, 0.502] | 0.502 (18186) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.596 (47) | 0.614 (412) [0.596, 0.644] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.500 (32) | 0.500 | flat -0.015 (noise 0.041) |
| reversal_k13_next | 0.451 (51) | 0.321 (417) [0.287, 0.360] | 0.309 (2160) [0.297, 0.322] | 0.309 (3794) [0.298, 0.320] | 0.320 (1689) [0.308, 0.333] | 0.286 (49) | 0.077 | flat +0.007 (noise 0.032) |
| reversal_k13_now | 0.643 (56) | 0.565 (375) [0.516, 0.620] | 0.561 (1611) [0.541, 0.582] | 0.572 (2832) [0.557, 0.588] | 0.563 (1360) [0.541, 0.587] | 0.576 (59) | 0.077 | flat +0.046 (noise 0.036) |
| reversal_k3_next | 0.569 (123) | 0.607 (679) [0.587, 0.629] | 0.584 (2878) [0.572, 0.597] | 0.584 (4882) [0.574, 0.594] | 0.580 (2442) [0.567, 0.593] | 0.577 (104) | 0.293 | flat +0.045 (noise 0.026) |
| reversal_k3_now | 0.969 (65) | 0.955 (397) [0.931, 0.974] | 0.937 (1714) [0.927, 0.946] | 0.939 (3191) [0.932, 0.946] | 0.935 (1428) [0.924, 0.946] | 0.902 (61) | 0.293 | flat +0.025 (noise 0.019) |
| reversal_k5_next | 0.530 (66) | 0.499 (830) [0.489, 0.511] | 0.467 (3054) [0.453, 0.480] | 0.478 (4619) [0.466, 0.490] | 0.466 (2629) [0.451, 0.481] | 0.509 (57) | 0.187 | up +0.060 (noise 0.024) |
| reversal_k5_now | 0.845 (58) | 0.821 (369) [0.809, 0.833] | 0.826 (1581) [0.814, 0.837] | 0.830 (2932) [0.820, 0.841] | 0.821 (1321) [0.809, 0.834] | 0.824 (68) | 0.187 | flat -0.001 (noise 0.028) |
| reversal_k8_next | 0.396 (101) | 0.382 (747) [0.362, 0.400] | 0.381 (2684) [0.369, 0.394] | 0.388 (4517) [0.377, 0.399] | 0.381 (2411) [0.368, 0.394] | 0.435 (92) | 0.120 | flat +0.020 (noise 0.025) |
| reversal_k8_now | 0.732 (56) | 0.674 (356) [0.624, 0.726] | 0.686 (1533) [0.665, 0.705] | 0.700 (2898) [0.685, 0.715] | 0.683 (1311) [0.660, 0.706] | 0.759 (58) | 0.121 | flat +0.010 (noise 0.037) |
| overall | 0.510 (22122) | 0.506 (155292) [0.503, 0.508] | 0.504 (663291) [0.503, 0.506] | 0.503 (1235815) [0.502, 0.504] | 0.504 (552534) [0.503, 0.506] | 0.507 (20120) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08082, 0.1226] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5274, 'levels': [{'threshold': 0.08082, 'calls_per_day': 144.7, 'win_rate': 0.6071}, {'threshold': 0.1226, 'calls_per_day': 36.7, 'win_rate': 0.6085}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 35863, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15316 | 0.338 | 0.522 (15085) | 0.581 (1889) | 0.758 (2601) |
| volatility: normal | 15316 | 0.366 | 0.529 (15243) | 0.616 (1335) | 0.751 (2253) |
| volatility: wild | 15316 | 0.380 | 0.522 (15273) | 0.628 (673) | 0.769 (2020) |
| session: Asia 00-08 | 15360 | 0.360 | 0.531 (15250) | 0.603 (1379) | 0.762 (2261) |
| session: Europe 08-13 | 9600 | 0.357 | 0.529 (9515) | 0.593 (964) | 0.752 (1561) |
| session: US 13-21 | 15360 | 0.369 | 0.520 (15262) | 0.602 (1002) | 0.768 (2202) |
| session: late 21-24 | 5628 | 0.350 | 0.512 (5574) | 0.609 (552) | 0.740 (850) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.416 | 0.394 | 0.363 | 0.363 | 0.650 | 0.337 | 0.494 | 1.506 |
| 6h | 360 | 0.386 | 0.382 | 0.311 | 0.356 | 0.543 | 0.272 | 0.501 | 1.392 |
| 24h | 1440 | 0.368 | 0.363 | 0.278 | 0.314 | 0.531 | 0.270 | 0.466 | 1.302 |
| 7d | 10080 | 0.368 | 0.359 | 0.280 | 0.311 | 0.527 | 0.265 | 0.470 | 1.235 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.307 | 0.525 | 0.259 | 0.465 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.416 / 0.650 / 0.917; 2: 0.344 / 0.417 / 0.933; 3: 0.354 / 0.467 / 0.950; 4: 0.330 / 0.367 / 0.933; 5: 0.409 / 0.600 / 0.967; 6: 0.417 / 0.633 / 0.900; 7: 0.349 / 0.400 / 0.933; 8: 0.395 / 0.633 / 0.967; 9: 0.445 / 0.717 / 0.950; 10: 0.374 / 0.433 / 0.967; 11: 0.414 / 0.633 / 0.933; 12: 0.391 / 0.533 / 1.000; 13: 0.344 / 0.383 / 0.917; 14: 0.373 / 0.517 / 0.900; 15: 0.344 / 0.467 / 0.967
- 6h: 1: 0.386 / 0.543 / 0.908; 2: 0.372 / 0.482 / 0.894; 3: 0.368 / 0.513 / 0.939; 4: 0.370 / 0.482 / 0.931; 5: 0.364 / 0.499 / 0.933; 6: 0.369 / 0.515 / 0.919; 7: 0.366 / 0.476 / 0.939; 8: 0.373 / 0.546 / 0.953; 9: 0.375 / 0.524 / 0.944; 10: 0.372 / 0.479 / 0.950; 11: 0.365 / 0.501 / 0.931; 12: 0.366 / 0.490 / 0.944; 13: 0.351 / 0.462 / 0.897; 14: 0.376 / 0.532 / 0.881; 15: 0.366 / 0.529 / 0.900
- 24h: 1: 0.368 / 0.531 / 0.912; 2: 0.347 / 0.476 / 0.903; 3: 0.357 / 0.508 / 0.905; 4: 0.354 / 0.501 / 0.906; 5: 0.351 / 0.492 / 0.903; 6: 0.352 / 0.510 / 0.901; 7: 0.352 / 0.492 / 0.901; 8: 0.355 / 0.518 / 0.903; 9: 0.351 / 0.509 / 0.898; 10: 0.356 / 0.507 / 0.898; 11: 0.348 / 0.503 / 0.897; 12: 0.352 / 0.497 / 0.900; 13: 0.346 / 0.494 / 0.892; 14: 0.352 / 0.516 / 0.892; 15: 0.350 / 0.502 / 0.897
- 7d: 1: 0.368 / 0.527 / 0.898; 2: 0.355 / 0.495 / 0.900; 3: 0.358 / 0.511 / 0.900; 4: 0.353 / 0.498 / 0.900; 5: 0.353 / 0.503 / 0.900; 6: 0.352 / 0.504 / 0.899; 7: 0.352 / 0.498 / 0.900; 8: 0.354 / 0.510 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.352 / 0.503 / 0.900; 11: 0.350 / 0.501 / 0.900; 12: 0.352 / 0.505 / 0.900; 13: 0.348 / 0.496 / 0.900; 14: 0.350 / 0.499 / 0.899; 15: 0.350 / 0.500 / 0.900
- 30d: 1: 0.362 / 0.525 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.501 / 0.900; 9: 0.347 / 0.497 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.125 (body 0.086, range 0.164); 'price stays where it was' would score 0.171; colour right 0.400; typical miss of the close 10.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.144 (body 0.098, range 0.189); 'price stays where it was' would score 0.153; colour right 0.490; typical miss of the close 11.2 bp; chain ended on the right side 0.292 of 24 chains; n=360
- 24h: match 0.136 (body 0.095, range 0.178); 'price stays where it was' would score 0.139; colour right 0.490; typical miss of the close 8.0 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.137; colour right 0.494; typical miss of the close 8.5 bp; chain ended on the right side 0.534 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.128; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.198 / 4.6; 3: 0.169 / 6.1; 4: 0.133 / 6.5; 5: 0.126 / 7.2; 6: 0.113 / 7.8; 7: 0.108 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.086 / 9.7; 12: 0.077 / 10.0; 13: 0.067 / 10.2; 14: 0.072 / 10.5; 15: 0.062 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 124902, probability skill vs chance 0.2237, widened contest next: False
  - now: threshold 0.8347, hit rate recent 0.9246 / long run 0.9377
    - 6h: 21 calls (85 a day), hit rate 0.857, chance 0.273, naive rule 0.431, lift 3.14x
    - 24h: 64 calls (64 a day), hit rate 0.906, chance 0.288, naive rule 0.479, lift 3.15x
    - 7d: 401 calls (57 a day), hit rate 0.943, chance 0.295, naive rule 0.497, lift 3.20x
    - 30d: 1739 calls (58 a day), hit rate 0.935, chance 0.293, naive rule 0.491, lift 3.19x
  - next: threshold 0.5306, hit rate recent 0.5659 / long run 0.5846
    - 6h: 25 calls (101 a day), hit rate 0.560, chance 0.273, lift 2.05x
    - 24h: 116 calls (116 a day), hit rate 0.586, chance 0.288, lift 2.04x
    - 7d: 647 calls (92 a day), hit rate 0.589, chance 0.295, lift 2.00x
    - 30d: 2895 calls (97 a day), hit rate 0.583, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 537, 0.519; 0.40: 477, 0.576; 0.45: 408, 0.647; 0.50: 357, 0.698; 0.55: 312, 0.739; 0.60: 264, 0.784; 0.65: 221, 0.810; 0.70: 175, 0.842; 0.75: 137, 0.873; 0.80: 92, 0.913; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.427; 0.35: 500, 0.465; 0.40: 407, 0.499; 0.45: 310, 0.534; 0.50: 200, 0.569; 0.55: 89, 0.572; 0.60: 13, 0.636; 0.65: 1, 0.645
- **K=5**: model 1792540800, labels learned 124900, probability skill vs chance 0.2216, widened contest next: False
  - now: threshold 0.6736, hit rate recent 0.8265 / long run 0.824
    - 6h: 22 calls (90 a day), hit rate 0.773, chance 0.169, naive rule 0.361, lift 4.58x
    - 24h: 70 calls (70 a day), hit rate 0.829, chance 0.184, naive rule 0.393, lift 4.51x
    - 7d: 390 calls (56 a day), hit rate 0.826, chance 0.185, naive rule 0.406, lift 4.46x
    - 30d: 1611 calls (54 a day), hit rate 0.825, chance 0.188, naive rule 0.402, lift 4.40x
  - next: threshold 0.4563, hit rate recent 0.4992 / long run 0.4876
    - 6h: 10 calls (41 a day), hit rate 0.500, chance 0.169, lift 2.97x
    - 24h: 67 calls (67 a day), hit rate 0.507, chance 0.184, lift 2.76x
    - 7d: 769 calls (110 a day), hit rate 0.502, chance 0.185, lift 2.71x
    - 30d: 3068 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.425; 0.35: 345, 0.492; 0.40: 279, 0.565; 0.45: 227, 0.618; 0.50: 179, 0.667; 0.55: 139, 0.708; 0.60: 107, 0.751; 0.65: 76, 0.789; 0.70: 52, 0.828; 0.75: 30, 0.871; 0.80: 10, 0.901
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.390; 0.35: 254, 0.420; 0.40: 159, 0.456; 0.45: 70, 0.471; 0.50: 14, 0.492; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 124897, probability skill vs chance 0.2096, widened contest next: False
  - now: threshold 0.5597, hit rate recent 0.7387 / long run 0.6859
    - 6h: 20 calls (82 a day), hit rate 0.800, chance 0.127, naive rule 0.362, lift 6.29x
    - 24h: 60 calls (60 a day), hit rate 0.767, chance 0.126, naive rule 0.358, lift 6.11x
    - 7d: 370 calls (53 a day), hit rate 0.681, chance 0.119, naive rule 0.333, lift 5.73x
    - 30d: 1558 calls (52 a day), hit rate 0.688, chance 0.121, naive rule 0.332, lift 5.69x
  - next: threshold 0.3333, hit rate recent 0.4295 / long run 0.3864
    - 6h: 21 calls (86 a day), hit rate 0.476, chance 0.127, lift 3.75x
    - 24h: 101 calls (102 a day), hit rate 0.436, chance 0.126, lift 3.47x
    - 7d: 744 calls (106 a day), hit rate 0.384, chance 0.119, lift 3.23x
    - 30d: 2738 calls (91 a day), hit rate 0.383, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.429; 0.35: 188, 0.497; 0.40: 146, 0.547; 0.45: 112, 0.591; 0.50: 84, 0.633; 0.55: 61, 0.672; 0.60: 40, 0.712; 0.65: 23, 0.775; 0.70: 11, 0.814; 0.75: 2, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.356; 0.35: 94, 0.384; 0.40: 32, 0.406; 0.45: 7, 0.416; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 124892, probability skill vs chance 0.1897, widened contest next: False
  - now: threshold 0.4057, hit rate recent 0.5875 / long run 0.5603
    - 6h: 17 calls (71 a day), hit rate 0.647, chance 0.083, naive rule 0.298, lift 7.83x
    - 24h: 62 calls (63 a day), hit rate 0.597, chance 0.081, naive rule 0.303, lift 7.33x
    - 7d: 392 calls (56 a day), hit rate 0.564, chance 0.076, naive rule 0.278, lift 7.46x
    - 30d: 1630 calls (54 a day), hit rate 0.561, chance 0.077, naive rule 0.274, lift 7.30x
  - next: threshold 0.2947, hit rate recent 0.3306 / long run 0.3184
    - 6h: 13 calls (54 a day), hit rate 0.308, chance 0.083, lift 3.72x
    - 24h: 53 calls (54 a day), hit rate 0.302, chance 0.081, lift 3.71x
    - 7d: 411 calls (59 a day), hit rate 0.314, chance 0.076, lift 4.15x
    - 30d: 2120 calls (71 a day), hit rate 0.310, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 125, 0.440; 0.35: 89, 0.490; 0.40: 63, 0.546; 0.45: 42, 0.598; 0.50: 27, 0.656; 0.55: 16, 0.701; 0.60: 8, 0.746; 0.65: 2, 0.797
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.325; 0.35: 14, 0.357; 0.40: 2, 0.452; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.145 | 0.36% | 0.900 | 0.517 | 0.248 | 0.550 | 0.237 |
| 6h | 19.843 | 6.01% | 0.875 | 0.497 | 0.250 | 0.490 | 0.569 |
| 24h | 14.194 | 4.12% | 0.907 | 0.499 | 0.250 | 0.502 | 0.601 |
| 7d | 14.615 | 3.54% | 0.900 | 0.500 | 0.250 | 0.499 | 0.650 |
| 30d | 13.748 | 4.09% | 0.900 | 0.500 | 0.251 | 0.496 | 0.665 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.199 | 15.313 | 15.159 | 15.313 | 15.791 | 15.181 | 15.114 | 15.137 | 15.158 | 15.145 |
| 6h | 21.111 | 20.187 | 20.062 | 19.832 | 20.637 | 20.118 | 19.774 | 19.831 | 19.798 | 19.843 |
| 24h | 14.804 | 14.398 | 14.331 | 14.200 | 14.656 | 14.371 | 14.160 | 14.158 | 14.165 | 14.194 |
| 7d | 15.152 | 14.769 | 14.709 | 14.634 | 14.906 | 14.765 | 14.598 | 14.578 | 14.585 | 14.615 |
| 30d | 14.335 | 13.884 | 13.833 | 13.772 | 14.001 | 13.929 | 13.743 | 13.723 | 13.722 | 13.748 |

## Next candle

- candle starting 2026-10-28 21:48 UTC, last close 2361.92
- P(up) 0.5309, return quantiles (bp): {'05': -7.982, '10': -5.801, '25': -3.215, '40': -0.903, '50': 0.391, '60': 1.671, '75': 3.343, '90': 6.428, '95': 8.669}
- changepoint probability 0.0873, regime age 61.1 min
- agent weights: empirical 0.003, ewma 0.025, garch 0.062, har 0.232, bocpd 0.004, hmm 0.037, online_qr 0.327, lgbm 0.310

## Learning log

- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- HMM volatility states (sd, bp per minute): [3.47, 6.69, 18.19], current probabilities: [0.445, 0.55, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-28 22:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.329, 'l_abs': 0.713, 'l_hi': 0.741, 'l_lo': 0.764, 'b05': 0.711, 'b25': 0.733, 'b75': 0.658, 'b95': 0.684}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.437, 1.533, 1.846, 2.196, 2.664, 2.662, 2.795, 3.218, 3.331, 3.571, 3.45, 4.308, 4.853, 4.464]}
- calibration offsets (in sigma): {'05': 0.0635, '10': 0.077, '25': 0.0075, '40': 0.028, '50': 0.035, '60': 0.052, '75': 0.0125, '90': -0.007, '95': -0.0035}
