# ETH-USD 60s candle generator - report

- generated: 2026-10-24 09:41 UTC
- last closed candle: 2026-10-24 09:41 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.447 (38) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.543 (313) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.571 (112) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.524 (576) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.502 (8064) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.568 (44) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.200 (20) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | 0.636 (22) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.680 (25) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 1.000 (22) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.429 (49) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | 0.857 (21) | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.286 (35) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | 0.727 (22) | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.505 (8894) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07112, 0.1047] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5364, 'levels': [{'threshold': 0.07112, 'calls_per_day': 146.7, 'win_rate': 0.6012}, {'threshold': 0.1047, 'calls_per_day': 36.9, 'win_rate': 0.6462}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 29414, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15074 | 0.337 | 0.524 (14824) | 0.588 (1596) | 0.765 (2484) |
| volatility: normal | 15073 | 0.365 | 0.521 (15008) | 0.622 (995) | 0.751 (2234) |
| volatility: wild | 15074 | 0.378 | 0.515 (15039) | 0.614 (445) | 0.775 (1931) |
| session: Asia 00-08 | 15360 | 0.358 | 0.526 (15258) | 0.613 (1120) | 0.767 (2224) |
| session: Europe 08-13 | 9401 | 0.355 | 0.521 (9316) | 0.598 (743) | 0.762 (1508) |
| session: US 13-21 | 14880 | 0.368 | 0.516 (14779) | 0.587 (726) | 0.769 (2103) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5518) | 0.615 (447) | 0.741 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.391 | 0.397 | 0.290 | 0.290 | 0.517 | 0.300 | 0.482 | 1.266 |
| 6h | 360 | 0.361 | 0.348 | 0.274 | 0.310 | 0.522 | 0.268 | 0.455 | 1.194 |
| 24h | 1440 | 0.369 | 0.356 | 0.270 | 0.310 | 0.529 | 0.270 | 0.469 | 1.252 |
| 7d | 10080 | 0.369 | 0.360 | 0.272 | 0.305 | 0.537 | 0.268 | 0.471 | 1.215 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.522 | 0.256 | 0.464 | 1.291 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.391 / 0.517 / 0.883; 2: 0.388 / 0.500 / 0.900; 3: 0.375 / 0.567 / 0.883; 4: 0.384 / 0.450 / 0.833; 5: 0.374 / 0.550 / 0.883; 6: 0.370 / 0.500 / 0.883; 7: 0.391 / 0.500 / 0.917; 8: 0.373 / 0.483 / 0.917; 9: 0.378 / 0.450 / 0.900; 10: 0.387 / 0.517 / 0.833; 11: 0.356 / 0.383 / 0.917; 12: 0.370 / 0.500 / 0.900; 13: 0.381 / 0.500 / 0.850; 14: 0.371 / 0.533 / 0.850; 15: 0.374 / 0.517 / 0.917
- 6h: 1: 0.361 / 0.522 / 0.892; 2: 0.352 / 0.503 / 0.864; 3: 0.349 / 0.517 / 0.867; 4: 0.348 / 0.466 / 0.853; 5: 0.345 / 0.525 / 0.897; 6: 0.347 / 0.503 / 0.883; 7: 0.347 / 0.489 / 0.917; 8: 0.360 / 0.536 / 0.914; 9: 0.347 / 0.511 / 0.917; 10: 0.345 / 0.480 / 0.886; 11: 0.345 / 0.500 / 0.906; 12: 0.341 / 0.455 / 0.919; 13: 0.349 / 0.531 / 0.908; 14: 0.347 / 0.508 / 0.900; 15: 0.363 / 0.573 / 0.931
- 24h: 1: 0.369 / 0.529 / 0.899; 2: 0.358 / 0.505 / 0.897; 3: 0.362 / 0.520 / 0.897; 4: 0.352 / 0.484 / 0.894; 5: 0.356 / 0.505 / 0.901; 6: 0.353 / 0.505 / 0.899; 7: 0.354 / 0.495 / 0.903; 8: 0.357 / 0.523 / 0.899; 9: 0.355 / 0.507 / 0.903; 10: 0.352 / 0.495 / 0.898; 11: 0.347 / 0.486 / 0.903; 12: 0.351 / 0.487 / 0.908; 13: 0.352 / 0.511 / 0.903; 14: 0.351 / 0.491 / 0.903; 15: 0.359 / 0.527 / 0.910
- 7d: 1: 0.369 / 0.537 / 0.896; 2: 0.357 / 0.500 / 0.899; 3: 0.358 / 0.509 / 0.899; 4: 0.353 / 0.494 / 0.898; 5: 0.353 / 0.499 / 0.899; 6: 0.353 / 0.496 / 0.899; 7: 0.352 / 0.496 / 0.899; 8: 0.354 / 0.509 / 0.899; 9: 0.351 / 0.498 / 0.900; 10: 0.353 / 0.506 / 0.899; 11: 0.349 / 0.496 / 0.899; 12: 0.350 / 0.500 / 0.899; 13: 0.348 / 0.493 / 0.899; 14: 0.351 / 0.499 / 0.898; 15: 0.350 / 0.502 / 0.899
- 30d: 1: 0.360 / 0.522 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.129 (body 0.089, range 0.169); 'price stays where it was' would score 0.093; colour right 0.433; typical miss of the close 8.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.123 (body 0.086, range 0.160); 'price stays where it was' would score 0.145; colour right 0.525; typical miss of the close 5.9 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.132 (body 0.093, range 0.171); 'price stays where it was' would score 0.140; colour right 0.512; typical miss of the close 7.6 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.128 (body 0.089, range 0.168); 'price stays where it was' would score 0.132; colour right 0.509; typical miss of the close 8.9 bp; chain ended on the right side 0.539 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.8; 2: 0.198 / 4.4; 3: 0.168 / 5.9; 4: 0.130 / 6.4; 5: 0.122 / 7.1; 6: 0.110 / 7.6; 7: 0.104 / 8.0; 8: 0.097 / 8.3; 9: 0.088 / 8.2; 10: 0.086 / 9.0; 11: 0.083 / 9.5; 12: 0.078 / 9.7; 13: 0.068 / 9.9; 14: 0.069 / 10.4; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 118415, probability skill vs chance 0.2328, widened contest next: False
  - now: threshold 0.8357, hit rate recent 0.9611 / long run 0.938
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.313, naive rule 0.540, lift 3.20x
    - 24h: 60 calls (60 a day), hit rate 0.950, chance 0.294, naive rule 0.520, lift 3.23x
    - 7d: 406 calls (58 a day), hit rate 0.941, chance 0.294, naive rule 0.495, lift 3.20x
    - 30d: 1691 calls (56 a day), hit rate 0.936, chance 0.293, naive rule 0.490, lift 3.20x
  - next: threshold 0.5654, hit rate recent 0.6502 / long run 0.5915
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.313, lift 2.51x
    - 24h: 53 calls (53 a day), hit rate 0.679, chance 0.294, lift 2.31x
    - 7d: 724 calls (103 a day), hit rate 0.581, chance 0.294, lift 1.98x
    - 30d: 2790 calls (93 a day), hit rate 0.580, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.493; 0.35: 540, 0.517; 0.40: 480, 0.572; 0.45: 410, 0.642; 0.50: 358, 0.695; 0.55: 313, 0.737; 0.60: 265, 0.783; 0.65: 222, 0.808; 0.70: 176, 0.840; 0.75: 136, 0.875; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.425; 0.35: 500, 0.463; 0.40: 406, 0.498; 0.45: 309, 0.532; 0.50: 201, 0.564; 0.55: 91, 0.571; 0.60: 14, 0.621; 0.65: 1, 0.710
- **K=5**: model 1792540800, labels learned 118413, probability skill vs chance 0.2169, widened contest next: False
  - now: threshold 0.6761, hit rate recent 0.8085 / long run 0.8212
    - 6h: 15 calls (61 a day), hit rate 0.800, chance 0.173, naive rule 0.388, lift 4.63x
    - 24h: 52 calls (52 a day), hit rate 0.788, chance 0.188, naive rule 0.418, lift 4.19x
    - 7d: 363 calls (52 a day), hit rate 0.813, chance 0.187, naive rule 0.403, lift 4.35x
    - 30d: 1555 calls (52 a day), hit rate 0.830, chance 0.188, naive rule 0.399, lift 4.42x
  - next: threshold 0.4201, hit rate recent 0.4707 / long run 0.4647
    - 6h: 30 calls (122 a day), hit rate 0.433, chance 0.173, lift 2.51x
    - 24h: 122 calls (123 a day), hit rate 0.492, chance 0.188, lift 2.62x
    - 7d: 959 calls (137 a day), hit rate 0.449, chance 0.187, lift 2.41x
    - 30d: 2771 calls (92 a day), hit rate 0.463, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 344, 0.495; 0.40: 276, 0.566; 0.45: 223, 0.623; 0.50: 176, 0.672; 0.55: 135, 0.712; 0.60: 104, 0.756; 0.65: 76, 0.792; 0.70: 54, 0.830; 0.75: 31, 0.872; 0.80: 10, 0.906
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 251, 0.422; 0.40: 157, 0.449; 0.45: 69, 0.460; 0.50: 15, 0.491; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 118410, probability skill vs chance 0.1869, widened contest next: True
  - now: threshold 0.5602, hit rate recent 0.6438 / long run 0.681
    - 6h: 17 calls (70 a day), hit rate 0.706, chance 0.119, naive rule 0.317, lift 5.95x
    - 24h: 55 calls (55 a day), hit rate 0.564, chance 0.119, naive rule 0.331, lift 4.76x
    - 7d: 333 calls (48 a day), hit rate 0.658, chance 0.116, naive rule 0.316, lift 5.67x
    - 30d: 1523 calls (51 a day), hit rate 0.701, chance 0.121, naive rule 0.329, lift 5.79x
  - next: threshold 0.361, hit rate recent 0.3447 / long run 0.3722
    - 6h: 23 calls (95 a day), hit rate 0.304, chance 0.119, lift 2.57x
    - 24h: 102 calls (103 a day), hit rate 0.353, chance 0.119, lift 2.98x
    - 7d: 787 calls (113 a day), hit rate 0.366, chance 0.116, lift 3.16x
    - 30d: 2499 calls (83 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.424; 0.35: 190, 0.494; 0.40: 146, 0.549; 0.45: 112, 0.594; 0.50: 85, 0.634; 0.55: 62, 0.676; 0.60: 41, 0.723; 0.65: 23, 0.792; 0.70: 10, 0.840; 0.75: 1, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.351; 0.35: 99, 0.378; 0.40: 37, 0.404; 0.45: 8, 0.439; 0.50: 1, 0.548
- **K=13**: model 1792800000, labels learned 118405, probability skill vs chance 0.1646, widened contest next: True
  - now: threshold 0.4064, hit rate recent 0.5312 / long run 0.5533
    - 6h: 16 calls (67 a day), hit rate 0.562, chance 0.070, naive rule 0.244, lift 8.09x
    - 24h: 54 calls (55 a day), hit rate 0.463, chance 0.072, naive rule 0.256, lift 6.47x
    - 7d: 373 calls (53 a day), hit rate 0.525, chance 0.075, naive rule 0.269, lift 7.04x
    - 30d: 1554 calls (52 a day), hit rate 0.567, chance 0.077, naive rule 0.272, lift 7.34x
  - next: threshold 0.2884, hit rate recent 0.2613 / long run 0.3066
    - 6h: 15 calls (63 a day), hit rate 0.267, chance 0.070, lift 3.83x
    - 24h: 57 calls (58 a day), hit rate 0.211, chance 0.072, lift 2.94x
    - 7d: 473 calls (68 a day), hit rate 0.300, chance 0.075, lift 4.02x
    - 30d: 2148 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.445; 0.35: 86, 0.497; 0.40: 61, 0.551; 0.45: 41, 0.606; 0.50: 25, 0.660; 0.55: 14, 0.710; 0.60: 6, 0.755; 0.65: 2, 0.848
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.316; 0.35: 13, 0.357; 0.40: 2, 0.450; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.348 | 1.22% | 0.900 | 0.517 | 0.250 | 0.533 | 0.202 |
| 6h | 9.157 | 5.46% | 0.894 | 0.483 | 0.251 | 0.489 | 0.415 |
| 24h | 13.640 | 3.90% | 0.905 | 0.506 | 0.250 | 0.494 | 0.684 |
| 7d | 14.884 | 3.29% | 0.900 | 0.499 | 0.250 | 0.502 | 0.638 |
| 30d | 13.450 | 4.12% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.488 | 11.436 | 11.397 | 11.389 | 11.421 | 11.430 | 11.478 | 11.399 | 11.390 | 11.348 |
| 6h | 9.686 | 9.243 | 9.245 | 9.163 | 9.304 | 9.495 | 9.169 | 9.182 | 9.158 | 9.157 |
| 24h | 14.193 | 13.790 | 13.718 | 13.618 | 13.905 | 13.839 | 13.610 | 13.618 | 13.612 | 13.640 |
| 7d | 15.389 | 15.025 | 14.957 | 14.894 | 15.139 | 15.021 | 14.868 | 14.856 | 14.856 | 14.884 |
| 30d | 14.029 | 13.573 | 13.533 | 13.470 | 13.693 | 13.640 | 13.445 | 13.428 | 13.425 | 13.450 |

## Next candle

- candle starting 2026-10-24 09:41 UTC, last close 2361.55
- P(up) 0.4655, return quantiles (bp): {'05': -12.464, '10': -9.987, '25': -5.472, '40': -2.714, '50': -0.571, '60': 1.107, '75': 3.726, '90': 8.133, '95': 10.911}
- changepoint probability 0.9063, regime age 7.5 min
- agent weights: empirical 0.005, ewma 0.074, garch 0.124, har 0.258, bocpd 0.045, hmm 0.035, online_qr 0.236, lgbm 0.221

## Learning log

- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.32, 7.07, 17.63], current probabilities: [0.006, 0.646, 0.347]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 09:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.333, 'l_abs': 0.71, 'l_hi': 0.781, 'l_lo': 0.797, 'b05': 0.723, 'b25': 0.748, 'b75': 0.621, 'b95': 0.687}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.6, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.71, 2.057, 2.527, 2.272, 2.702, 2.442, 2.723, 2.837, 3.587, 3.343, 3.166, 3.506, 3.871, 3.49]}
- calibration offsets (in sigma): {'05': 0.0, '10': -0.04, '25': -0.07, '40': -0.1, '50': -0.04, '60': -0.02, '75': -0.06, '90': -0.07, '95': -0.14}
