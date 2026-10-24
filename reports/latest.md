# ETH-USD 60s candle generator - report

- generated: 2026-10-24 05:22 UTC
- last closed candle: 2026-10-24 05:22 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.429 (21) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.536 (153) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.667 (45) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.538 (318) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.499 (4452) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.600 (15) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.000 (8) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | 0.875 (8) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.588 (17) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 1.000 (10) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.407 (27) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | 1.000 (9) | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.278 (18) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | 0.875 (8) | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.503 (4896) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07055, 0.1039] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5373, 'levels': [{'threshold': 0.07055, 'calls_per_day': 148.0, 'win_rate': 0.5998}, {'threshold': 0.1039, 'calls_per_day': 36.8, 'win_rate': 0.6486}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 29156, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14988 | 0.337 | 0.524 (14738) | 0.592 (1544) | 0.768 (2457) |
| volatility: normal | 14987 | 0.365 | 0.521 (14923) | 0.622 (982) | 0.748 (2219) |
| volatility: wild | 14987 | 0.378 | 0.515 (14952) | 0.614 (443) | 0.777 (1921) |
| session: Asia 00-08 | 15202 | 0.358 | 0.527 (15101) | 0.616 (1086) | 0.767 (2188) |
| session: Europe 08-13 | 9300 | 0.355 | 0.520 (9215) | 0.601 (710) | 0.763 (1492) |
| session: US 13-21 | 14880 | 0.368 | 0.516 (14779) | 0.587 (726) | 0.769 (2103) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5518) | 0.615 (447) | 0.741 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.358 | 0.359 | 0.319 | 0.319 | 0.525 | 0.261 | 0.455 | 1.428 |
| 6h | 360 | 0.357 | 0.335 | 0.263 | 0.300 | 0.551 | 0.272 | 0.442 | 1.352 |
| 24h | 1440 | 0.371 | 0.359 | 0.272 | 0.309 | 0.531 | 0.271 | 0.472 | 1.249 |
| 7d | 10080 | 0.369 | 0.359 | 0.271 | 0.304 | 0.537 | 0.268 | 0.470 | 1.227 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.522 | 0.255 | 0.464 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.358 / 0.525 / 0.950; 2: 0.332 / 0.475 / 0.950; 3: 0.317 / 0.458 / 0.950; 4: 0.354 / 0.475 / 0.967; 5: 0.331 / 0.492 / 0.950; 6: 0.348 / 0.525 / 0.983; 7: 0.307 / 0.407 / 1.000; 8: 0.377 / 0.627 / 1.000; 9: 0.339 / 0.525 / 1.000; 10: 0.333 / 0.458 / 1.000; 11: 0.334 / 0.475 / 1.000; 12: 0.366 / 0.508 / 1.000; 13: 0.354 / 0.593 / 1.000; 14: 0.353 / 0.492 / 1.000; 15: 0.358 / 0.576 / 1.000
- 6h: 1: 0.357 / 0.551 / 0.922; 2: 0.337 / 0.486 / 0.919; 3: 0.340 / 0.508 / 0.931; 4: 0.332 / 0.475 / 0.944; 5: 0.339 / 0.503 / 0.942; 6: 0.322 / 0.472 / 0.944; 7: 0.325 / 0.478 / 0.958; 8: 0.336 / 0.514 / 0.950; 9: 0.344 / 0.522 / 0.950; 10: 0.335 / 0.489 / 0.953; 11: 0.334 / 0.494 / 0.956; 12: 0.336 / 0.486 / 0.964; 13: 0.335 / 0.522 / 0.969; 14: 0.328 / 0.480 / 0.947; 15: 0.346 / 0.553 / 0.942
- 24h: 1: 0.371 / 0.531 / 0.904; 2: 0.359 / 0.503 / 0.906; 3: 0.363 / 0.516 / 0.905; 4: 0.353 / 0.484 / 0.910; 5: 0.359 / 0.507 / 0.910; 6: 0.356 / 0.510 / 0.912; 7: 0.353 / 0.491 / 0.911; 8: 0.358 / 0.520 / 0.908; 9: 0.356 / 0.502 / 0.910; 10: 0.354 / 0.496 / 0.910; 11: 0.349 / 0.483 / 0.901; 12: 0.357 / 0.506 / 0.903; 13: 0.352 / 0.499 / 0.906; 14: 0.352 / 0.487 / 0.905; 15: 0.359 / 0.509 / 0.904
- 7d: 1: 0.369 / 0.537 / 0.896; 2: 0.356 / 0.499 / 0.901; 3: 0.357 / 0.509 / 0.901; 4: 0.352 / 0.494 / 0.901; 5: 0.352 / 0.497 / 0.901; 6: 0.352 / 0.495 / 0.901; 7: 0.351 / 0.496 / 0.901; 8: 0.353 / 0.508 / 0.902; 9: 0.351 / 0.498 / 0.902; 10: 0.352 / 0.507 / 0.902; 11: 0.348 / 0.496 / 0.902; 12: 0.350 / 0.502 / 0.901; 13: 0.348 / 0.493 / 0.902; 14: 0.350 / 0.499 / 0.901; 15: 0.349 / 0.500 / 0.901
- 30d: 1: 0.360 / 0.522 / 0.899; 2: 0.350 / 0.498 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.502 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.347 / 0.499 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.093 (body 0.070, range 0.117); 'price stays where it was' would score 0.150; colour right 0.542; typical miss of the close 5.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.109 (body 0.080, range 0.138); 'price stays where it was' would score 0.129; colour right 0.537; typical miss of the close 7.2 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.128 (body 0.090, range 0.166); 'price stays where it was' would score 0.137; colour right 0.514; typical miss of the close 8.1 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.129 (body 0.090, range 0.169); 'price stays where it was' would score 0.132; colour right 0.508; typical miss of the close 8.7 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 3.8; 2: 0.198 / 4.4; 3: 0.168 / 5.9; 4: 0.130 / 6.5; 5: 0.121 / 7.1; 6: 0.110 / 7.6; 7: 0.104 / 8.0; 8: 0.097 / 8.3; 9: 0.088 / 8.3; 10: 0.086 / 9.1; 11: 0.083 / 9.5; 12: 0.077 / 9.8; 13: 0.068 / 10.0; 14: 0.069 / 10.4; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 118156, probability skill vs chance 0.2284, widened contest next: False
  - now: threshold 0.8358, hit rate recent 0.9524 / long run 0.9368
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.254, naive rule 0.449, lift 3.94x
    - 24h: 62 calls (62 a day), hit rate 0.952, chance 0.290, naive rule 0.500, lift 3.29x
    - 7d: 404 calls (58 a day), hit rate 0.938, chance 0.295, naive rule 0.496, lift 3.18x
    - 30d: 1692 calls (56 a day), hit rate 0.936, chance 0.293, naive rule 0.489, lift 3.20x
  - next: threshold 0.5668, hit rate recent 0.6168 / long run 0.5876
    - 6h: 17 calls (69 a day), hit rate 0.588, chance 0.254, lift 2.32x
    - 24h: 62 calls (62 a day), hit rate 0.645, chance 0.290, lift 2.23x
    - 7d: 741 calls (106 a day), hit rate 0.582, chance 0.295, lift 1.97x
    - 30d: 2788 calls (93 a day), hit rate 0.578, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.492; 0.35: 540, 0.516; 0.40: 480, 0.571; 0.45: 410, 0.642; 0.50: 358, 0.695; 0.55: 313, 0.736; 0.60: 265, 0.782; 0.65: 222, 0.808; 0.70: 176, 0.840; 0.75: 136, 0.875; 0.80: 92, 0.913; 0.85: 47, 0.951; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.425; 0.35: 499, 0.463; 0.40: 406, 0.497; 0.45: 309, 0.530; 0.50: 201, 0.562; 0.55: 91, 0.571; 0.60: 14, 0.619; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 118154, probability skill vs chance 0.2188, widened contest next: False
  - now: threshold 0.6766, hit rate recent 0.8239 / long run 0.8227
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.170, naive rule 0.374, lift 5.88x
    - 24h: 55 calls (55 a day), hit rate 0.818, chance 0.188, naive rule 0.412, lift 4.35x
    - 7d: 360 calls (51 a day), hit rate 0.817, chance 0.188, naive rule 0.405, lift 4.35x
    - 30d: 1552 calls (52 a day), hit rate 0.831, chance 0.188, naive rule 0.398, lift 4.42x
  - next: threshold 0.4198, hit rate recent 0.4765 / long run 0.465
    - 6h: 32 calls (131 a day), hit rate 0.438, chance 0.170, lift 2.57x
    - 24h: 123 calls (124 a day), hit rate 0.504, chance 0.188, lift 2.68x
    - 7d: 958 calls (137 a day), hit rate 0.452, chance 0.188, lift 2.41x
    - 30d: 2752 calls (92 a day), hit rate 0.463, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 344, 0.495; 0.40: 276, 0.566; 0.45: 223, 0.623; 0.50: 176, 0.672; 0.55: 134, 0.713; 0.60: 104, 0.756; 0.65: 76, 0.793; 0.70: 54, 0.831; 0.75: 31, 0.872; 0.80: 10, 0.906
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 250, 0.422; 0.40: 157, 0.448; 0.45: 69, 0.461; 0.50: 15, 0.490; 0.55: 1, 0.513
- **K=8**: model 1792800000, labels learned 118151, probability skill vs chance 0.1902, widened contest next: True
  - now: threshold 0.5605, hit rate recent 0.6487 / long run 0.6819
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.113, naive rule 0.277, lift 7.75x
    - 24h: 55 calls (55 a day), hit rate 0.582, chance 0.118, naive rule 0.326, lift 4.92x
    - 7d: 327 calls (47 a day), hit rate 0.664, chance 0.116, naive rule 0.317, lift 5.71x
    - 30d: 1521 calls (51 a day), hit rate 0.702, chance 0.121, naive rule 0.328, lift 5.80x
  - next: threshold 0.3399, hit rate recent 0.3613 / long run 0.3745
    - 6h: 21 calls (86 a day), hit rate 0.286, chance 0.113, lift 2.53x
    - 24h: 108 calls (109 a day), hit rate 0.389, chance 0.118, lift 3.29x
    - 7d: 785 calls (112 a day), hit rate 0.369, chance 0.116, lift 3.18x
    - 30d: 2495 calls (83 a day), hit rate 0.383, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.424; 0.35: 190, 0.494; 0.40: 146, 0.548; 0.45: 112, 0.594; 0.50: 85, 0.633; 0.55: 62, 0.676; 0.60: 41, 0.722; 0.65: 23, 0.791; 0.70: 10, 0.840; 0.75: 1, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.350; 0.35: 99, 0.377; 0.40: 38, 0.402; 0.45: 8, 0.436; 0.50: 1, 0.531
- **K=13**: model 1792800000, labels learned 118146, probability skill vs chance 0.1657, widened contest next: True
  - now: threshold 0.4071, hit rate recent 0.5419 / long run 0.5545
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.065, naive rule 0.188, lift 13.42x
    - 24h: 57 calls (58 a day), hit rate 0.509, chance 0.074, naive rule 0.258, lift 6.87x
    - 7d: 367 calls (53 a day), hit rate 0.534, chance 0.075, naive rule 0.270, lift 7.13x
    - 30d: 1551 calls (52 a day), hit rate 0.567, chance 0.077, naive rule 0.271, lift 7.35x
  - next: threshold 0.2926, hit rate recent 0.244 / long run 0.306
    - 6h: 10 calls (42 a day), hit rate 0.000, chance 0.065, lift 0.00x
    - 24h: 59 calls (60 a day), hit rate 0.254, chance 0.074, lift 3.43x
    - 7d: 464 calls (66 a day), hit rate 0.302, chance 0.075, lift 4.03x
    - 30d: 2149 calls (72 a day), hit rate 0.303, chance 0.077, lift 3.93x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.445; 0.35: 86, 0.497; 0.40: 61, 0.552; 0.45: 41, 0.606; 0.50: 25, 0.657; 0.55: 14, 0.706; 0.60: 6, 0.751; 0.65: 2, 0.848
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.316; 0.35: 13, 0.351; 0.40: 2, 0.443; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.738 | 20.14% | 0.967 | 0.567 | 0.250 | 0.542 | 0.061 |
| 6h | 10.001 | 5.45% | 0.928 | 0.542 | 0.250 | 0.492 | 0.617 |
| 24h | 14.007 | 3.73% | 0.910 | 0.508 | 0.250 | 0.498 | 0.677 |
| 7d | 14.801 | 3.44% | 0.900 | 0.500 | 0.250 | 0.501 | 0.644 |
| 30d | 13.489 | 4.12% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.185 | 5.748 | 6.029 | 5.738 | 5.864 | 6.781 | 5.730 | 5.757 | 5.775 | 5.738 |
| 6h | 10.578 | 10.307 | 10.186 | 9.955 | 10.253 | 10.394 | 9.961 | 10.010 | 9.996 | 10.001 |
| 24h | 14.550 | 14.154 | 14.091 | 13.984 | 14.273 | 14.185 | 13.973 | 13.977 | 13.977 | 14.007 |
| 7d | 15.329 | 14.941 | 14.885 | 14.813 | 15.057 | 14.949 | 14.785 | 14.772 | 14.774 | 14.801 |
| 30d | 14.068 | 13.612 | 13.572 | 13.509 | 13.732 | 13.678 | 13.485 | 13.466 | 13.464 | 13.489 |

## Next candle

- candle starting 2026-10-24 05:22 UTC, last close 2374.66
- P(up) 0.4814, return quantiles (bp): {'05': -4.397, '10': -3.314, '25': -1.564, '40': -0.664, '50': -0.102, '60': 0.455, '75': 1.435, '90': 3.199, '95': 4.136}
- changepoint probability 0.0262, regime age 97.2 min
- agent weights: empirical 0.003, ewma 0.053, garch 0.088, har 0.316, bocpd 0.028, hmm 0.022, online_qr 0.259, lgbm 0.230

## Learning log

- 2026-10-22 00:00 UTC: {"garch": {"alpha": 0.0893, "beta": 0.891}, "hmm": {"sd_bp": [3.56, 5.88, 15.56], "stay": [0.977, 0.969, 0.925]}, "lgbm": {"challenger_loss": 0.25808, "champion_loss": 0.25805, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49006, "challengers": 1, "chance_loss": 0.61235, "widened": false, "champion_loss": 0.48841, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37552, "challengers": 1, "chance_loss": 0.4836, "widened": false, "champion_loss": 0.37335, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26273, "challengers": 1, "chance_loss": 0.35828, "widened": false, "champion_loss": 0.26192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18608, "challengers": 1, "chance_loss": 0.25933, "widened": false, "champion_loss": 0.18543, "promoted": false}}
- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.32, 7.07, 17.63], current probabilities: [0.973, 0.027, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 05:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.321, 'l_abs': 0.709, 'l_hi': 0.782, 'l_lo': 0.797, 'b05': 0.722, 'b25': 0.743, 'b75': 0.623, 'b95': 0.698}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.316, 1.648, 1.76, 2.268, 2.344, 2.64, 2.828, 2.888, 2.873, 3.019, 3.036, 3.042, 3.227, 3.554]}
- calibration offsets (in sigma): {'05': 0.0705, '10': 0.011, '25': 0.0125, '40': -0.046, '50': -0.045, '60': -0.064, '75': -0.1025, '90': -0.091, '95': -0.1205}
