# ETH-USD 60s candle generator - report

- generated: 2026-10-28 17:22 UTC
- last closed candle: 2026-10-28 17:22 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.537 (672) [0.501, 0.574] | 0.520 (2876) [0.500, 0.539] | 0.517 (5370) [0.503, 0.530] | 0.523 (2398) [0.501, 0.546] | 0.652 (69) | 0.500 | flat +0.003 (noise 0.032) |
| colour_clear | 0.556 (840) | 0.544 (5696) [0.540, 0.549] | 0.537 (23618) [0.530, 0.544] | 0.519 (43957) [0.512, 0.525] | 0.546 (19719) [0.542, 0.551] | 0.542 (583) | 0.500 | flat -0.012 (noise 0.009) |
| colour_confident | 0.596 (161) | 0.604 (1371) [0.591, 0.619] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.603 (3782) [0.590, 0.616] | 0.526 (95) | 0.500 | flat +0.010 (noise 0.021) |
| colour_next | 0.530 (1430) | 0.528 (10030) [0.525, 0.532] | 0.525 (42880) [0.521, 0.530] | 0.513 (80052) [0.509, 0.517] | 0.529 (35703) [0.525, 0.533] | 0.529 (1033) | 0.500 | flat -0.007 (noise 0.007) |
| colour_path | 0.506 (20020) | 0.502 (140420) [0.500, 0.504] | 0.501 (600320) [0.499, 0.503] | 0.501 (1120728) [0.500, 0.502] | 0.501 (499842) [0.499, 0.502] | 0.502 (14462) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.596 (47) | 0.614 (412) [0.596, 0.644] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.635 (1041) [0.615, 0.657] | 0.448 (29) | 0.500 | flat -0.015 (noise 0.041) |
| reversal_k13_next | 0.451 (51) | 0.321 (417) [0.287, 0.360] | 0.309 (2160) [0.297, 0.322] | 0.309 (3794) [0.298, 0.320] | 0.320 (1689) [0.308, 0.333] | 0.263 (38) | 0.077 | flat +0.007 (noise 0.032) |
| reversal_k13_now | 0.643 (56) | 0.565 (375) [0.516, 0.620] | 0.561 (1611) [0.541, 0.582] | 0.572 (2832) [0.557, 0.588] | 0.563 (1360) [0.541, 0.587] | 0.578 (45) | 0.077 | flat +0.046 (noise 0.036) |
| reversal_k3_next | 0.569 (123) | 0.607 (679) [0.587, 0.629] | 0.584 (2878) [0.572, 0.597] | 0.584 (4882) [0.574, 0.594] | 0.580 (2442) [0.567, 0.593] | 0.588 (85) | 0.293 | flat +0.045 (noise 0.026) |
| reversal_k3_now | 0.969 (65) | 0.955 (397) [0.931, 0.974] | 0.937 (1714) [0.927, 0.946] | 0.939 (3191) [0.932, 0.946] | 0.935 (1428) [0.924, 0.946] | 0.932 (44) | 0.293 | flat +0.025 (noise 0.019) |
| reversal_k5_next | 0.530 (66) | 0.499 (830) [0.489, 0.511] | 0.467 (3054) [0.453, 0.480] | 0.478 (4619) [0.466, 0.490] | 0.466 (2629) [0.451, 0.481] | 0.490 (49) | 0.187 | up +0.060 (noise 0.024) |
| reversal_k5_now | 0.845 (58) | 0.821 (369) [0.809, 0.833] | 0.826 (1581) [0.814, 0.837] | 0.830 (2932) [0.820, 0.841] | 0.821 (1321) [0.809, 0.834] | 0.843 (51) | 0.187 | flat -0.001 (noise 0.028) |
| reversal_k8_next | 0.396 (101) | 0.382 (747) [0.362, 0.400] | 0.381 (2684) [0.369, 0.394] | 0.388 (4517) [0.377, 0.399] | 0.381 (2411) [0.368, 0.394] | 0.419 (74) | 0.120 | flat +0.020 (noise 0.025) |
| reversal_k8_now | 0.732 (56) | 0.674 (356) [0.624, 0.726] | 0.686 (1533) [0.665, 0.705] | 0.700 (2898) [0.685, 0.715] | 0.683 (1311) [0.660, 0.706] | 0.762 (42) | 0.121 | flat +0.010 (noise 0.037) |
| overall | 0.510 (22122) | 0.506 (155292) [0.503, 0.508] | 0.504 (663291) [0.503, 0.506] | 0.503 (1235815) [0.502, 0.504] | 0.504 (552534) [0.503, 0.506] | 0.507 (15992) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0807, 0.1221] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5276, 'levels': [{'threshold': 0.0807, 'calls_per_day': 145.1, 'win_rate': 0.6024}, {'threshold': 0.1221, 'calls_per_day': 36.9, 'win_rate': 0.6077}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 35597, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15229 | 0.338 | 0.522 (14998) | 0.582 (1881) | 0.758 (2580) |
| volatility: normal | 15226 | 0.366 | 0.529 (15153) | 0.614 (1328) | 0.752 (2246) |
| volatility: wild | 15227 | 0.380 | 0.522 (15184) | 0.627 (668) | 0.769 (1984) |
| session: Asia 00-08 | 15360 | 0.360 | 0.531 (15250) | 0.603 (1379) | 0.762 (2261) |
| session: Europe 08-13 | 9600 | 0.357 | 0.529 (9515) | 0.593 (964) | 0.752 (1561) |
| session: US 13-21 | 15142 | 0.369 | 0.520 (15044) | 0.600 (983) | 0.771 (2151) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5526) | 0.608 (551) | 0.736 (837) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.387 | 0.377 | 0.270 | 0.270 | 0.593 | 0.291 | 0.482 | 1.247 |
| 6h | 360 | 0.377 | 0.378 | 0.267 | 0.310 | 0.563 | 0.271 | 0.484 | 1.317 |
| 24h | 1440 | 0.361 | 0.357 | 0.273 | 0.309 | 0.525 | 0.264 | 0.458 | 1.326 |
| 7d | 10080 | 0.367 | 0.358 | 0.278 | 0.309 | 0.528 | 0.265 | 0.470 | 1.234 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.307 | 0.525 | 0.258 | 0.465 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.387 / 0.593 / 0.933; 2: 0.343 / 0.441 / 0.883; 3: 0.319 / 0.441 / 0.917; 4: 0.342 / 0.492 / 0.900; 5: 0.351 / 0.508 / 0.867; 6: 0.355 / 0.508 / 0.867; 7: 0.347 / 0.475 / 0.900; 8: 0.350 / 0.525 / 0.867; 9: 0.324 / 0.407 / 0.867; 10: 0.355 / 0.559 / 0.867; 11: 0.355 / 0.525 / 0.900; 12: 0.349 / 0.508 / 0.900; 13: 0.336 / 0.508 / 0.967; 14: 0.385 / 0.576 / 0.983; 15: 0.336 / 0.458 / 1.000
- 6h: 1: 0.377 / 0.563 / 0.919; 2: 0.350 / 0.476 / 0.872; 3: 0.360 / 0.513 / 0.858; 4: 0.358 / 0.518 / 0.861; 5: 0.358 / 0.518 / 0.836; 6: 0.356 / 0.510 / 0.850; 7: 0.360 / 0.526 / 0.878; 8: 0.357 / 0.518 / 0.839; 9: 0.350 / 0.487 / 0.858; 10: 0.359 / 0.540 / 0.853; 11: 0.352 / 0.518 / 0.889; 12: 0.351 / 0.487 / 0.881; 13: 0.352 / 0.501 / 0.928; 14: 0.350 / 0.487 / 0.942; 15: 0.347 / 0.468 / 0.956
- 24h: 1: 0.361 / 0.525 / 0.909; 2: 0.342 / 0.483 / 0.897; 3: 0.353 / 0.508 / 0.897; 4: 0.350 / 0.505 / 0.902; 5: 0.350 / 0.499 / 0.893; 6: 0.347 / 0.511 / 0.892; 7: 0.350 / 0.501 / 0.894; 8: 0.352 / 0.511 / 0.887; 9: 0.344 / 0.503 / 0.887; 10: 0.353 / 0.520 / 0.892; 11: 0.344 / 0.504 / 0.894; 12: 0.347 / 0.496 / 0.893; 13: 0.346 / 0.503 / 0.900; 14: 0.348 / 0.517 / 0.904; 15: 0.346 / 0.494 / 0.901
- 7d: 1: 0.367 / 0.528 / 0.898; 2: 0.354 / 0.495 / 0.900; 3: 0.358 / 0.512 / 0.899; 4: 0.353 / 0.497 / 0.899; 5: 0.353 / 0.504 / 0.898; 6: 0.351 / 0.503 / 0.899; 7: 0.352 / 0.499 / 0.899; 8: 0.354 / 0.508 / 0.899; 9: 0.352 / 0.502 / 0.899; 10: 0.352 / 0.505 / 0.898; 11: 0.349 / 0.500 / 0.899; 12: 0.352 / 0.505 / 0.899; 13: 0.349 / 0.497 / 0.901; 14: 0.350 / 0.499 / 0.901; 15: 0.350 / 0.500 / 0.901
- 30d: 1: 0.362 / 0.525 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.501 / 0.900; 9: 0.347 / 0.497 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.178 (body 0.143, range 0.212); 'price stays where it was' would score 0.146; colour right 0.576; typical miss of the close 6.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.157 (body 0.117, range 0.197); 'price stays where it was' would score 0.136; colour right 0.529; typical miss of the close 9.2 bp; chain ended on the right side 0.708 of 24 chains; n=360
- 24h: match 0.132 (body 0.092, range 0.173); 'price stays where it was' would score 0.135; colour right 0.502; typical miss of the close 7.2 bp; chain ended on the right side 0.646 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.137; colour right 0.495; typical miss of the close 8.4 bp; chain ended on the right side 0.542 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.128; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.522 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.0; 2: 0.198 / 4.6; 3: 0.169 / 6.1; 4: 0.132 / 6.5; 5: 0.126 / 7.2; 6: 0.113 / 7.7; 7: 0.107 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.085 / 9.7; 12: 0.077 / 10.0; 13: 0.067 / 10.2; 14: 0.072 / 10.5; 15: 0.061 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 124636, probability skill vs chance 0.2294, widened contest next: False
  - now: threshold 0.8349, hit rate recent 0.9538 / long run 0.941
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.304, naive rule 0.486, lift 3.29x
    - 24h: 54 calls (54 a day), hit rate 0.944, chance 0.286, naive rule 0.477, lift 3.30x
    - 7d: 396 calls (57 a day), hit rate 0.949, chance 0.295, naive rule 0.500, lift 3.22x
    - 30d: 1729 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5308, hit rate recent 0.5901 / long run 0.5865
    - 6h: 29 calls (118 a day), hit rate 0.621, chance 0.304, lift 2.04x
    - 24h: 123 calls (123 a day), hit rate 0.569, chance 0.286, lift 1.99x
    - 7d: 657 calls (94 a day), hit rate 0.591, chance 0.295, lift 2.00x
    - 30d: 2895 calls (97 a day), hit rate 0.583, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 537, 0.520; 0.40: 477, 0.577; 0.45: 408, 0.647; 0.50: 357, 0.698; 0.55: 312, 0.739; 0.60: 264, 0.784; 0.65: 221, 0.810; 0.70: 174, 0.843; 0.75: 136, 0.874; 0.80: 92, 0.914; 0.85: 47, 0.950; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.465; 0.40: 407, 0.499; 0.45: 311, 0.533; 0.50: 200, 0.569; 0.55: 89, 0.573; 0.60: 13, 0.640; 0.65: 1, 0.656
- **K=5**: model 1792540800, labels learned 124634, probability skill vs chance 0.2223, widened contest next: False
  - now: threshold 0.6731, hit rate recent 0.8421 / long run 0.8256
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.178, naive rule 0.388, lift 4.90x
    - 24h: 59 calls (59 a day), hit rate 0.847, chance 0.191, naive rule 0.400, lift 4.45x
    - 7d: 381 calls (54 a day), hit rate 0.824, chance 0.186, naive rule 0.407, lift 4.43x
    - 30d: 1601 calls (53 a day), hit rate 0.826, chance 0.188, naive rule 0.402, lift 4.40x
  - next: threshold 0.455, hit rate recent 0.4834 / long run 0.4858
    - 6h: 13 calls (53 a day), hit rate 0.385, chance 0.178, lift 2.16x
    - 24h: 71 calls (71 a day), hit rate 0.493, chance 0.191, lift 2.59x
    - 7d: 785 calls (112 a day), hit rate 0.498, chance 0.186, lift 2.68x
    - 30d: 3065 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 345, 0.492; 0.40: 279, 0.565; 0.45: 226, 0.618; 0.50: 179, 0.668; 0.55: 139, 0.708; 0.60: 106, 0.751; 0.65: 76, 0.790; 0.70: 51, 0.829; 0.75: 30, 0.871; 0.80: 10, 0.901
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.390; 0.35: 254, 0.420; 0.40: 159, 0.455; 0.45: 70, 0.470; 0.50: 14, 0.494; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 124631, probability skill vs chance 0.2096, widened contest next: False
  - now: threshold 0.5592, hit rate recent 0.731 / long run 0.6842
    - 6h: 15 calls (62 a day), hit rate 0.867, chance 0.129, naive rule 0.382, lift 6.74x
    - 24h: 50 calls (50 a day), hit rate 0.780, chance 0.124, naive rule 0.347, lift 6.28x
    - 7d: 360 calls (51 a day), hit rate 0.678, chance 0.118, naive rule 0.330, lift 5.74x
    - 30d: 1547 calls (52 a day), hit rate 0.688, chance 0.121, naive rule 0.331, lift 5.69x
  - next: threshold 0.3337, hit rate recent 0.4078 / long run 0.3829
    - 6h: 23 calls (95 a day), hit rate 0.435, chance 0.129, lift 3.38x
    - 24h: 103 calls (104 a day), hit rate 0.417, chance 0.124, lift 3.36x
    - 7d: 737 calls (105 a day), hit rate 0.381, chance 0.118, lift 3.23x
    - 30d: 2727 calls (91 a day), hit rate 0.383, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.429; 0.35: 188, 0.497; 0.40: 146, 0.547; 0.45: 111, 0.592; 0.50: 84, 0.634; 0.55: 60, 0.672; 0.60: 40, 0.713; 0.65: 23, 0.776; 0.70: 10, 0.813; 0.75: 2, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.355; 0.35: 94, 0.383; 0.40: 32, 0.406; 0.45: 7, 0.424; 0.50: 1, 0.633
- **K=13**: model 1793059200, labels learned 124626, probability skill vs chance 0.1943, widened contest next: False
  - now: threshold 0.4056, hit rate recent 0.5866 / long run 0.56
    - 6h: 16 calls (67 a day), hit rate 0.562, chance 0.078, naive rule 0.321, lift 7.19x
    - 24h: 56 calls (57 a day), hit rate 0.625, chance 0.082, naive rule 0.301, lift 7.61x
    - 7d: 386 calls (55 a day), hit rate 0.565, chance 0.076, naive rule 0.278, lift 7.47x
    - 30d: 1622 calls (54 a day), hit rate 0.563, chance 0.077, naive rule 0.274, lift 7.33x
  - next: threshold 0.2947, hit rate recent 0.3214 / long run 0.3175
    - 6h: 10 calls (42 a day), hit rate 0.200, chance 0.078, lift 2.56x
    - 24h: 52 calls (53 a day), hit rate 0.288, chance 0.082, lift 3.51x
    - 7d: 406 calls (58 a day), hit rate 0.313, chance 0.076, lift 4.14x
    - 30d: 2122 calls (71 a day), hit rate 0.309, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.440; 0.35: 89, 0.492; 0.40: 63, 0.547; 0.45: 42, 0.599; 0.50: 27, 0.658; 0.55: 16, 0.701; 0.60: 8, 0.743; 0.65: 2, 0.793
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.325; 0.35: 14, 0.356; 0.40: 2, 0.451; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.152 | 2.52% | 0.900 | 0.517 | 0.252 | 0.492 | 0.181 |
| 6h | 15.949 | 3.98% | 0.911 | 0.508 | 0.250 | 0.526 | 0.442 |
| 24h | 12.195 | 2.96% | 0.912 | 0.507 | 0.251 | 0.501 | 0.483 |
| 7d | 14.398 | 3.37% | 0.901 | 0.501 | 0.251 | 0.499 | 0.647 |
| 30d | 13.704 | 4.04% | 0.901 | 0.500 | 0.251 | 0.495 | 0.664 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.543 | 15.646 | 15.747 | 15.126 | 16.615 | 15.437 | 15.103 | 15.092 | 15.136 | 15.152 |
| 6h | 16.610 | 16.237 | 16.149 | 15.959 | 16.646 | 16.216 | 15.979 | 15.892 | 15.944 | 15.949 |
| 24h | 12.567 | 12.339 | 12.305 | 12.208 | 12.547 | 12.308 | 12.168 | 12.158 | 12.167 | 12.195 |
| 7d | 14.900 | 14.547 | 14.487 | 14.419 | 14.675 | 14.543 | 14.382 | 14.360 | 14.368 | 14.398 |
| 30d | 14.281 | 13.839 | 13.789 | 13.728 | 13.954 | 13.884 | 13.699 | 13.679 | 13.678 | 13.704 |

## Next candle

- candle starting 2026-10-28 17:22 UTC, last close 2331.67
- P(up) 0.4642, return quantiles (bp): {'05': -9.217, '10': -7.405, '25': -4.079, '40': -1.799, '50': -0.424, '60': 0.787, '75': 3.231, '90': 7.324, '95': 9.718}
- changepoint probability 0.0676, regime age 22.9 min
- agent weights: empirical 0.006, ewma 0.034, garch 0.057, har 0.216, bocpd 0.004, hmm 0.046, online_qr 0.263, lgbm 0.374

## Learning log

- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- HMM volatility states (sd, bp per minute): [3.47, 6.69, 18.19], current probabilities: [0.303, 0.677, 0.02]
- live generator: {'versions': 60, 'latest_effective': '2026-10-28 17:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.311, 'l_abs': 0.701, 'l_hi': 0.739, 'l_lo': 0.761, 'b05': 0.711, 'b25': 0.724, 'b75': 0.658, 'b95': 0.678}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.426, 1.973, 2.237, 2.883, 2.98, 3.29, 3.974, 4.309, 4.643, 4.158, 4.439, 3.642, 3.566, 3.699]}
- calibration offsets (in sigma): {'05': 0.0905, '10': 0.031, '25': -0.0275, '40': -0.026, '50': -0.045, '60': -0.054, '75': -0.0625, '90': -0.001, '95': -0.0505}
