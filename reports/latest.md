# ETH-USD 60s candle generator - report

- generated: 2026-10-28 11:35 UTC
- last closed candle: 2026-10-28 11:34 UTC (staleness 1.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.537 (672) [0.501, 0.574] | 0.520 (2876) [0.500, 0.539] | 0.517 (5370) [0.503, 0.530] | 0.523 (2398) [0.501, 0.546] | 0.630 (46) | 0.500 | flat +0.003 (noise 0.032) |
| colour_clear | 0.556 (840) | 0.544 (5696) [0.540, 0.549] | 0.537 (23618) [0.530, 0.544] | 0.519 (43957) [0.512, 0.525] | 0.546 (19719) [0.542, 0.551] | 0.537 (395) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.596 (161) | 0.604 (1371) [0.591, 0.619] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.450 (80) | 0.500 | flat +0.010 (noise 0.021) |
| colour_next | 0.530 (1430) | 0.528 (10030) [0.525, 0.532] | 0.525 (42880) [0.521, 0.530] | 0.513 (80052) [0.509, 0.517] | 0.529 (35703) [0.525, 0.533] | 0.509 (686) | 0.500 | flat -0.007 (noise 0.007) |
| colour_path | 0.506 (20020) | 0.502 (140420) [0.500, 0.504] | 0.501 (600320) [0.499, 0.503] | 0.501 (1120728) [0.500, 0.502] | 0.501 (499842) [0.499, 0.502] | 0.501 (9604) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.596 (47) | 0.614 (412) [0.596, 0.644] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.407 (27) | 0.500 | flat -0.015 (noise 0.041) |
| reversal_k13_next | 0.451 (51) | 0.321 (417) [0.287, 0.360] | 0.309 (2160) [0.297, 0.322] | 0.309 (3794) [0.298, 0.320] | 0.320 (1689) [0.308, 0.333] | 0.286 (28) | 0.077 | flat +0.007 (noise 0.032) |
| reversal_k13_now | 0.643 (56) | 0.565 (375) [0.516, 0.620] | 0.561 (1611) [0.541, 0.582] | 0.572 (2832) [0.557, 0.588] | 0.563 (1360) [0.541, 0.587] | 0.586 (29) | 0.077 | flat +0.046 (noise 0.036) |
| reversal_k3_next | 0.569 (123) | 0.607 (679) [0.587, 0.629] | 0.584 (2878) [0.572, 0.597] | 0.584 (4882) [0.574, 0.594] | 0.580 (2442) [0.567, 0.593] | 0.571 (56) | 0.293 | flat +0.045 (noise 0.026) |
| reversal_k3_now | 0.969 (65) | 0.955 (397) [0.931, 0.974] | 0.937 (1714) [0.927, 0.946] | 0.939 (3191) [0.932, 0.946] | 0.935 (1428) [0.924, 0.946] | 0.914 (35) | 0.293 | flat +0.025 (noise 0.019) |
| reversal_k5_next | 0.530 (66) | 0.499 (830) [0.489, 0.511] | 0.467 (3054) [0.453, 0.480] | 0.478 (4619) [0.466, 0.490] | 0.466 (2629) [0.451, 0.481] | 0.528 (36) | 0.187 | up +0.060 (noise 0.024) |
| reversal_k5_now | 0.845 (58) | 0.821 (369) [0.809, 0.833] | 0.826 (1581) [0.814, 0.837] | 0.830 (2932) [0.820, 0.841] | 0.821 (1321) [0.809, 0.834] | 0.829 (35) | 0.187 | flat -0.001 (noise 0.028) |
| reversal_k8_next | 0.396 (101) | 0.382 (747) [0.362, 0.400] | 0.381 (2684) [0.369, 0.394] | 0.388 (4517) [0.377, 0.399] | 0.381 (2411) [0.368, 0.394] | 0.412 (51) | 0.120 | flat +0.020 (noise 0.025) |
| reversal_k8_now | 0.732 (56) | 0.674 (356) [0.624, 0.726] | 0.686 (1533) [0.665, 0.705] | 0.700 (2898) [0.685, 0.715] | 0.683 (1311) [0.660, 0.706] | 0.704 (27) | 0.121 | flat +0.010 (noise 0.037) |
| overall | 0.510 (22122) | 0.506 (155292) [0.503, 0.508] | 0.504 (663291) [0.503, 0.506] | 0.503 (1235815) [0.502, 0.504] | 0.504 (552534) [0.503, 0.506] | 0.504 (10633) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08047, 0.1212] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5289, 'levels': [{'threshold': 0.08047, 'calls_per_day': 145.1, 'win_rate': 0.6102}, {'threshold': 0.1212, 'calls_per_day': 36.4, 'win_rate': 0.625}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 35250, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15113 | 0.338 | 0.522 (14882) | 0.582 (1871) | 0.759 (2570) |
| volatility: normal | 15110 | 0.366 | 0.529 (15039) | 0.611 (1321) | 0.753 (2223) |
| volatility: wild | 15111 | 0.380 | 0.522 (15067) | 0.625 (670) | 0.765 (1961) |
| session: Asia 00-08 | 15360 | 0.360 | 0.531 (15250) | 0.603 (1379) | 0.762 (2261) |
| session: Europe 08-13 | 9514 | 0.357 | 0.528 (9429) | 0.591 (956) | 0.753 (1545) |
| session: US 13-21 | 14880 | 0.369 | 0.520 (14783) | 0.597 (976) | 0.769 (2111) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5526) | 0.608 (551) | 0.736 (837) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.350 | 0.334 | 0.227 | 0.227 | 0.593 | 0.279 | 0.421 | 1.232 |
| 6h | 360 | 0.344 | 0.345 | 0.251 | 0.295 | 0.490 | 0.253 | 0.434 | 1.296 |
| 24h | 1440 | 0.361 | 0.357 | 0.281 | 0.317 | 0.512 | 0.260 | 0.463 | 1.311 |
| 7d | 10080 | 0.368 | 0.358 | 0.279 | 0.311 | 0.527 | 0.265 | 0.470 | 1.232 |
| 30d | 43200 | 0.362 | 0.355 | 0.278 | 0.307 | 0.525 | 0.258 | 0.465 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.350 / 0.593 / 0.883; 2: 0.306 / 0.441 / 0.900; 3: 0.316 / 0.508 / 0.933; 4: 0.319 / 0.458 / 0.933; 5: 0.337 / 0.576 / 0.950; 6: 0.332 / 0.559 / 0.950; 7: 0.351 / 0.576 / 0.900; 8: 0.360 / 0.593 / 0.933; 9: 0.323 / 0.542 / 0.900; 10: 0.321 / 0.576 / 0.933; 11: 0.325 / 0.475 / 0.917; 12: 0.344 / 0.610 / 0.883; 13: 0.324 / 0.559 / 0.883; 14: 0.348 / 0.610 / 0.883; 15: 0.323 / 0.525 / 0.900
- 6h: 1: 0.344 / 0.490 / 0.919; 2: 0.327 / 0.476 / 0.922; 3: 0.335 / 0.493 / 0.917; 4: 0.334 / 0.499 / 0.917; 5: 0.332 / 0.470 / 0.917; 6: 0.334 / 0.513 / 0.922; 7: 0.333 / 0.490 / 0.892; 8: 0.334 / 0.510 / 0.925; 9: 0.339 / 0.535 / 0.892; 10: 0.342 / 0.530 / 0.914; 11: 0.328 / 0.496 / 0.908; 12: 0.342 / 0.518 / 0.900; 13: 0.331 / 0.518 / 0.889; 14: 0.331 / 0.507 / 0.886; 15: 0.334 / 0.490 / 0.886
- 24h: 1: 0.361 / 0.512 / 0.901; 2: 0.351 / 0.492 / 0.908; 3: 0.358 / 0.509 / 0.909; 4: 0.354 / 0.504 / 0.907; 5: 0.355 / 0.504 / 0.916; 6: 0.351 / 0.512 / 0.915; 7: 0.354 / 0.503 / 0.908; 8: 0.358 / 0.513 / 0.913; 9: 0.348 / 0.499 / 0.904; 10: 0.357 / 0.515 / 0.903; 11: 0.350 / 0.514 / 0.905; 12: 0.353 / 0.504 / 0.906; 13: 0.351 / 0.505 / 0.902; 14: 0.353 / 0.523 / 0.902; 15: 0.354 / 0.506 / 0.899
- 7d: 1: 0.368 / 0.527 / 0.897; 2: 0.355 / 0.496 / 0.902; 3: 0.358 / 0.511 / 0.901; 4: 0.353 / 0.497 / 0.901; 5: 0.353 / 0.504 / 0.902; 6: 0.352 / 0.503 / 0.902; 7: 0.352 / 0.500 / 0.901; 8: 0.354 / 0.508 / 0.902; 9: 0.352 / 0.502 / 0.901; 10: 0.352 / 0.503 / 0.900; 11: 0.350 / 0.500 / 0.900; 12: 0.352 / 0.505 / 0.900; 13: 0.349 / 0.497 / 0.900; 14: 0.350 / 0.500 / 0.900; 15: 0.350 / 0.501 / 0.898
- 30d: 1: 0.362 / 0.525 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.501 / 0.900; 9: 0.347 / 0.497 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.899; 14: 0.346 / 0.499 / 0.899; 15: 0.346 / 0.499 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.113 (body 0.078, range 0.148); 'price stays where it was' would score 0.098; colour right 0.458; typical miss of the close 7.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.130 (body 0.089, range 0.171); 'price stays where it was' would score 0.127; colour right 0.476; typical miss of the close 6.3 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.133; colour right 0.497; typical miss of the close 7.6 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.136; colour right 0.494; typical miss of the close 8.6 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.128; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.522 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.1; 2: 0.198 / 4.6; 3: 0.169 / 6.1; 4: 0.132 / 6.6; 5: 0.126 / 7.2; 6: 0.113 / 7.8; 7: 0.107 / 8.1; 8: 0.095 / 8.5; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.085 / 9.7; 12: 0.078 / 10.0; 13: 0.068 / 10.2; 14: 0.071 / 10.6; 15: 0.061 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 124288, probability skill vs chance 0.2381, widened contest next: False
  - now: threshold 0.8346, hit rate recent 0.9462 / long run 0.9401
    - 6h: 21 calls (85 a day), hit rate 0.952, chance 0.287, naive rule 0.512, lift 3.32x
    - 24h: 64 calls (64 a day), hit rate 0.938, chance 0.280, naive rule 0.476, lift 3.35x
    - 7d: 404 calls (58 a day), hit rate 0.950, chance 0.295, naive rule 0.501, lift 3.22x
    - 30d: 1734 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5313, hit rate recent 0.5676 / long run 0.5848
    - 6h: 31 calls (126 a day), hit rate 0.581, chance 0.287, lift 2.03x
    - 24h: 117 calls (117 a day), hit rate 0.573, chance 0.280, lift 2.05x
    - 7d: 661 calls (94 a day), hit rate 0.592, chance 0.295, lift 2.00x
    - 30d: 2886 calls (96 a day), hit rate 0.583, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 537, 0.519; 0.40: 477, 0.576; 0.45: 408, 0.647; 0.50: 357, 0.697; 0.55: 312, 0.739; 0.60: 264, 0.785; 0.65: 221, 0.811; 0.70: 175, 0.843; 0.75: 137, 0.874; 0.80: 92, 0.913; 0.85: 47, 0.950; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.466; 0.40: 407, 0.499; 0.45: 310, 0.534; 0.50: 200, 0.569; 0.55: 89, 0.573; 0.60: 14, 0.640; 0.65: 1, 0.667
- **K=5**: model 1792540800, labels learned 124286, probability skill vs chance 0.2256, widened contest next: False
  - now: threshold 0.672, hit rate recent 0.8335 / long run 0.8243
    - 6h: 17 calls (70 a day), hit rate 0.824, chance 0.172, naive rule 0.386, lift 4.79x
    - 24h: 60 calls (60 a day), hit rate 0.833, chance 0.188, naive rule 0.392, lift 4.44x
    - 7d: 382 calls (55 a day), hit rate 0.825, chance 0.187, naive rule 0.409, lift 4.41x
    - 30d: 1601 calls (53 a day), hit rate 0.825, chance 0.188, naive rule 0.402, lift 4.39x
  - next: threshold 0.4525, hit rate recent 0.5073 / long run 0.488
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.172, lift 2.62x
    - 24h: 71 calls (71 a day), hit rate 0.507, chance 0.188, lift 2.70x
    - 7d: 800 calls (114 a day), hit rate 0.497, chance 0.187, lift 2.66x
    - 30d: 3064 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 345, 0.492; 0.40: 279, 0.565; 0.45: 226, 0.618; 0.50: 178, 0.668; 0.55: 138, 0.709; 0.60: 107, 0.752; 0.65: 76, 0.789; 0.70: 52, 0.827; 0.75: 30, 0.870; 0.80: 10, 0.901
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.391; 0.35: 254, 0.421; 0.40: 159, 0.455; 0.45: 70, 0.472; 0.50: 14, 0.494; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 124283, probability skill vs chance 0.2058, widened contest next: False
  - now: threshold 0.5582, hit rate recent 0.6895 / long run 0.6795
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.125, naive rule 0.348, lift 4.58x
    - 24h: 56 calls (56 a day), hit rate 0.679, chance 0.120, naive rule 0.327, lift 5.64x
    - 7d: 361 calls (52 a day), hit rate 0.676, chance 0.118, naive rule 0.330, lift 5.71x
    - 30d: 1546 calls (52 a day), hit rate 0.686, chance 0.121, naive rule 0.331, lift 5.67x
  - next: threshold 0.3344, hit rate recent 0.3973 / long run 0.3809
    - 6h: 31 calls (128 a day), hit rate 0.419, chance 0.125, lift 3.36x
    - 24h: 108 calls (109 a day), hit rate 0.389, chance 0.120, lift 3.23x
    - 7d: 742 calls (106 a day), hit rate 0.381, chance 0.118, lift 3.22x
    - 30d: 2716 calls (91 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.428; 0.35: 188, 0.497; 0.40: 146, 0.547; 0.45: 111, 0.591; 0.50: 84, 0.634; 0.55: 60, 0.671; 0.60: 40, 0.712; 0.65: 23, 0.778; 0.70: 10, 0.815; 0.75: 2, 0.812
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.355; 0.35: 94, 0.383; 0.40: 32, 0.406; 0.45: 7, 0.424; 0.50: 1, 0.621
- **K=13**: model 1793059200, labels learned 124278, probability skill vs chance 0.1967, widened contest next: False
  - now: threshold 0.4049, hit rate recent 0.5887 / long run 0.5599
    - 6h: 10 calls (42 a day), hit rate 0.500, chance 0.087, naive rule 0.321, lift 5.73x
    - 24h: 61 calls (62 a day), hit rate 0.607, chance 0.084, naive rule 0.301, lift 7.20x
    - 7d: 385 calls (55 a day), hit rate 0.569, chance 0.075, naive rule 0.278, lift 7.54x
    - 30d: 1622 calls (54 a day), hit rate 0.563, chance 0.077, naive rule 0.274, lift 7.32x
  - next: threshold 0.2947, hit rate recent 0.3451 / long run 0.3195
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.087, lift 3.58x
    - 24h: 56 calls (57 a day), hit rate 0.357, chance 0.084, lift 4.24x
    - 7d: 408 calls (58 a day), hit rate 0.316, chance 0.075, lift 4.19x
    - 30d: 2141 calls (71 a day), hit rate 0.309, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.440; 0.35: 89, 0.491; 0.40: 63, 0.547; 0.45: 42, 0.599; 0.50: 27, 0.657; 0.55: 16, 0.702; 0.60: 8, 0.746; 0.65: 2, 0.793
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.357; 0.40: 2, 0.451; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.408 | 0.68% | 0.883 | 0.467 | 0.250 | 0.525 | 0.327 |
| 6h | 10.750 | 3.39% | 0.928 | 0.511 | 0.252 | 0.504 | 0.440 |
| 24h | 12.412 | 2.28% | 0.908 | 0.501 | 0.251 | 0.494 | 0.545 |
| 7d | 14.645 | 3.45% | 0.901 | 0.500 | 0.250 | 0.500 | 0.653 |
| 30d | 13.773 | 4.08% | 0.900 | 0.500 | 0.251 | 0.495 | 0.666 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.480 | 10.512 | 10.468 | 10.447 | 10.510 | 10.497 | 10.330 | 10.362 | 10.360 | 10.408 |
| 6h | 11.128 | 10.939 | 10.884 | 10.750 | 11.135 | 10.882 | 10.701 | 10.713 | 10.714 | 10.750 |
| 24h | 12.702 | 12.517 | 12.497 | 12.449 | 12.671 | 12.483 | 12.375 | 12.384 | 12.381 | 12.412 |
| 7d | 15.168 | 14.793 | 14.738 | 14.669 | 14.917 | 14.790 | 14.628 | 14.605 | 14.615 | 14.645 |
| 30d | 14.358 | 13.907 | 13.857 | 13.798 | 14.021 | 13.952 | 13.768 | 13.747 | 13.747 | 13.773 |

## Next candle

- candle starting 2026-10-28 11:34 UTC, last close 2363.2
- P(up) 0.496, return quantiles (bp): {'05': -5.803, '10': -4.621, '25': -2.263, '40': -0.756, '50': -0.038, '60': 0.81, '75': 2.469, '90': 4.814, '95': 6.313}
- changepoint probability 0.0622, regime age 141.8 min
- agent weights: empirical 0.018, ewma 0.058, garch 0.083, har 0.168, bocpd 0.015, hmm 0.087, online_qr 0.289, lgbm 0.281

## Learning log

- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.41, 6.59, 17.7], current probabilities: [0.861, 0.134, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-28 11:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.289, 'l_abs': 0.683, 'l_hi': 0.743, 'l_lo': 0.771, 'b05': 0.708, 'b25': 0.723, 'b75': 0.635, 'b95': 0.668}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.163, 1.455, 1.684, 1.777, 2.03, 2.737, 2.499, 3.116, 3.226, 3.747, 3.768, 4.343, 4.7, 5.387]}
- calibration offsets (in sigma): {'05': 0.0765, '10': 0.023, '25': 0.0225, '40': 0.012, '50': -0.035, '60': -0.042, '75': 0.0075, '90': -0.003, '95': -0.0265}
