# ETH-USD 60s candle generator - report

- generated: 2026-10-21 21:34 UTC
- last closed candle: 2026-10-21 21:34 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.534 (672) [0.497, 0.571] | 0.521 (2876) [0.502, 0.539] | 0.514 (4698) [0.498, 0.528] | 0.518 (1726) [0.491, 0.545] | 0.581 (86) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.579 (848) | 0.556 (5623) [0.548, 0.565] | 0.526 (23426) [0.517, 0.535] | 0.515 (38261) [0.508, 0.522] | 0.547 (14023) [0.541, 0.553] | 0.552 (733) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.579 (209) | 0.594 (870) [0.572, 0.620] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.599 (157) | 0.500 | flat -0.011 (noise 0.023) |
| colour_next | 0.548 (1439) | 0.535 (10025) [0.526, 0.543] | 0.517 (42863) [0.512, 0.524] | 0.511 (70022) [0.507, 0.516] | 0.530 (25673) [0.525, 0.535] | 0.534 (1290) | 0.500 | flat +0.012 (noise 0.007) |
| colour_path | 0.493 (20146) | 0.500 (140350) [0.496, 0.504] | 0.501 (600082) [0.499, 0.502] | 0.500 (980308) [0.499, 0.501] | 0.500 (359422) [0.498, 0.502] | 0.506 (18060) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.691 (55) | 0.629 (210) [0.581, 0.672] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.618 (34) | 0.500 | flat -0.047 (noise 0.045) |
| reversal_k13_next | 0.355 (76) | 0.315 (445) [0.298, 0.330] | 0.308 (2119) [0.296, 0.320] | 0.307 (3377) [0.296, 0.319] | 0.320 (1272) [0.308, 0.332] | 0.345 (55) | 0.077 | flat -0.007 (noise 0.030) |
| reversal_k13_now | 0.510 (51) | 0.519 (391) [0.491, 0.550] | 0.571 (1553) [0.551, 0.591] | 0.574 (2457) [0.557, 0.590] | 0.562 (985) [0.538, 0.588] | 0.595 (42) | 0.077 | flat -0.070 (noise 0.036) |
| reversal_k3_next | 0.533 (122) | 0.562 (737) [0.550, 0.573] | 0.571 (2652) [0.559, 0.584] | 0.580 (4203) [0.570, 0.591] | 0.570 (1763) [0.557, 0.585] | 0.667 (132) | 0.292 | flat -0.005 (noise 0.026) |
| reversal_k3_now | 0.912 (57) | 0.930 (384) [0.906, 0.954] | 0.933 (1700) [0.925, 0.943] | 0.936 (2794) [0.929, 0.944] | 0.927 (1031) [0.917, 0.938] | 0.982 (55) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.380 (129) | 0.439 (878) [0.415, 0.464] | 0.462 (2498) [0.447, 0.478] | 0.473 (3789) [0.460, 0.488] | 0.450 (1799) [0.434, 0.469] | 0.487 (113) | 0.187 | flat -0.029 (noise 0.028) |
| reversal_k5_now | 0.840 (50) | 0.823 (355) [0.796, 0.846] | 0.827 (1584) [0.813, 0.841] | 0.831 (2563) [0.819, 0.843] | 0.821 (952) [0.804, 0.838] | 0.787 (47) | 0.187 | flat +0.013 (noise 0.029) |
| reversal_k8_next | 0.376 (109) | 0.362 (730) [0.337, 0.384] | 0.387 (2335) [0.372, 0.401] | 0.389 (3770) [0.377, 0.402] | 0.380 (1664) [0.363, 0.398] | 0.409 (93) | 0.121 | flat -0.025 (noise 0.027) |
| reversal_k8_now | 0.619 (42) | 0.665 (325) [0.629, 0.701] | 0.704 (1553) [0.685, 0.724] | 0.703 (2542) [0.687, 0.720] | 0.686 (955) [0.661, 0.710] | 0.727 (44) | 0.122 | flat -0.005 (noise 0.035) |
| overall | 0.497 (22317) | 0.504 (155292) [0.501, 0.507] | 0.503 (661815) [0.502, 0.505] | 0.503 (1080523) [0.502, 0.504] | 0.503 (397242) [0.501, 0.506] | 0.511 (20017) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06744, 0.1022] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5331, 'levels': [{'threshold': 0.06744, 'calls_per_day': 145.1, 'win_rate': 0.571}, {'threshold': 0.1022, 'calls_per_day': 36.0, 'win_rate': 0.6443}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 25825, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15312 | 0.337 | 0.523 (15066) | 0.588 (1511) | 0.766 (2501) |
| volatility: normal | 15311 | 0.365 | 0.521 (15248) | 0.624 (739) | 0.756 (2239) |
| volatility: wild | 15311 | 0.379 | 0.511 (15272) | 0.616 (318) | 0.779 (2077) |
| session: Asia 00-08 | 15360 | 0.359 | 0.524 (15261) | 0.612 (928) | 0.767 (2259) |
| session: Europe 08-13 | 9600 | 0.354 | 0.520 (9515) | 0.597 (635) | 0.774 (1512) |
| session: US 13-21 | 15360 | 0.368 | 0.513 (15257) | 0.578 (635) | 0.771 (2215) |
| session: late 21-24 | 5614 | 0.351 | 0.516 (5553) | 0.624 (370) | 0.743 (831) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.388 | 0.314 | 0.231 | 0.231 | 0.650 | 0.333 | 0.443 | 1.376 |
| 6h | 360 | 0.375 | 0.364 | 0.282 | 0.318 | 0.533 | 0.259 | 0.492 | 1.365 |
| 24h | 1440 | 0.372 | 0.364 | 0.286 | 0.320 | 0.528 | 0.265 | 0.480 | 1.229 |
| 7d | 10080 | 0.369 | 0.360 | 0.276 | 0.309 | 0.534 | 0.267 | 0.472 | 1.229 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.519 | 0.254 | 0.466 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.388 / 0.650 / 0.950; 2: 0.358 / 0.583 / 0.967; 3: 0.356 / 0.567 / 0.933; 4: 0.341 / 0.517 / 0.950; 5: 0.339 / 0.583 / 0.950; 6: 0.337 / 0.500 / 0.933; 7: 0.351 / 0.550 / 0.950; 8: 0.340 / 0.567 / 0.917; 9: 0.343 / 0.450 / 0.950; 10: 0.363 / 0.567 / 0.917; 11: 0.323 / 0.350 / 0.933; 12: 0.357 / 0.533 / 0.917; 13: 0.345 / 0.533 / 0.933; 14: 0.339 / 0.533 / 0.983; 15: 0.354 / 0.583 / 0.983
- 6h: 1: 0.375 / 0.533 / 0.928; 2: 0.366 / 0.489 / 0.925; 3: 0.370 / 0.522 / 0.919; 4: 0.349 / 0.467 / 0.936; 5: 0.370 / 0.533 / 0.931; 6: 0.367 / 0.503 / 0.928; 7: 0.376 / 0.533 / 0.942; 8: 0.366 / 0.511 / 0.931; 9: 0.370 / 0.511 / 0.933; 10: 0.367 / 0.525 / 0.919; 11: 0.351 / 0.461 / 0.925; 12: 0.353 / 0.478 / 0.922; 13: 0.367 / 0.522 / 0.922; 14: 0.368 / 0.533 / 0.933; 15: 0.363 / 0.522 / 0.928
- 24h: 1: 0.372 / 0.528 / 0.891; 2: 0.359 / 0.487 / 0.898; 3: 0.358 / 0.506 / 0.899; 4: 0.362 / 0.507 / 0.899; 5: 0.364 / 0.525 / 0.899; 6: 0.359 / 0.488 / 0.899; 7: 0.362 / 0.507 / 0.899; 8: 0.362 / 0.517 / 0.896; 9: 0.355 / 0.494 / 0.894; 10: 0.361 / 0.522 / 0.894; 11: 0.350 / 0.477 / 0.894; 12: 0.353 / 0.485 / 0.894; 13: 0.359 / 0.514 / 0.892; 14: 0.356 / 0.501 / 0.894; 15: 0.358 / 0.522 / 0.893
- 7d: 1: 0.369 / 0.534 / 0.897; 2: 0.356 / 0.494 / 0.900; 3: 0.358 / 0.505 / 0.901; 4: 0.354 / 0.497 / 0.901; 5: 0.355 / 0.500 / 0.900; 6: 0.353 / 0.494 / 0.900; 7: 0.353 / 0.500 / 0.900; 8: 0.353 / 0.502 / 0.899; 9: 0.353 / 0.501 / 0.899; 10: 0.355 / 0.511 / 0.899; 11: 0.349 / 0.497 / 0.899; 12: 0.352 / 0.504 / 0.899; 13: 0.351 / 0.500 / 0.899; 14: 0.351 / 0.504 / 0.899; 15: 0.350 / 0.501 / 0.899
- 30d: 1: 0.360 / 0.519 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.118 (body 0.078, range 0.157); 'price stays where it was' would score 0.080; colour right 0.467; typical miss of the close 7.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.080, range 0.170); 'price stays where it was' would score 0.137; colour right 0.500; typical miss of the close 10.5 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.139 (body 0.093, range 0.184); 'price stays where it was' would score 0.141; colour right 0.531; typical miss of the close 8.5 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.133; colour right 0.506; typical miss of the close 9.1 bp; chain ended on the right side 0.548 of 672 chains; n=10080
- 30d: match 0.121 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.500; typical miss of the close 7.7 bp; chain ended on the right side 0.522 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 3.8; 2: 0.197 / 4.5; 3: 0.165 / 6.0; 4: 0.133 / 6.5; 5: 0.119 / 7.2; 6: 0.109 / 7.7; 7: 0.104 / 8.1; 8: 0.096 / 8.4; 9: 0.088 / 8.3; 10: 0.086 / 9.1; 11: 0.082 / 9.6; 12: 0.079 / 9.9; 13: 0.067 / 10.2; 14: 0.068 / 10.5; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 114808, probability skill vs chance 0.226, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9574 / long run 0.9337
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.287, naive rule 0.498, lift 3.48x
    - 24h: 61 calls (61 a day), hit rate 0.984, chance 0.309, naive rule 0.528, lift 3.18x
    - 7d: 391 calls (56 a day), hit rate 0.931, chance 0.291, naive rule 0.483, lift 3.20x
    - 30d: 1697 calls (57 a day), hit rate 0.933, chance 0.292, naive rule 0.485, lift 3.19x
  - next: threshold 0.5401, hit rate recent 0.6219 / long run 0.5822
    - 6h: 32 calls (130 a day), hit rate 0.594, chance 0.287, lift 2.07x
    - 24h: 142 calls (142 a day), hit rate 0.669, chance 0.309, lift 2.16x
    - 7d: 804 calls (115 a day), hit rate 0.576, chance 0.291, lift 1.98x
    - 30d: 2733 calls (91 a day), hit rate 0.575, chance 0.292, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.491; 0.35: 541, 0.515; 0.40: 482, 0.568; 0.45: 412, 0.638; 0.50: 360, 0.691; 0.55: 314, 0.733; 0.60: 268, 0.777; 0.65: 223, 0.805; 0.70: 178, 0.838; 0.75: 138, 0.872; 0.80: 93, 0.911; 0.85: 48, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.425; 0.35: 499, 0.461; 0.40: 406, 0.493; 0.45: 310, 0.525; 0.50: 201, 0.557; 0.55: 91, 0.568; 0.60: 14, 0.610; 0.65: 1, 0.700
- **K=5**: model 1792540800, labels learned 114806, probability skill vs chance 0.2146, widened contest next: False
  - now: threshold 0.6825, hit rate recent 0.8047 / long run 0.8219
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.210, naive rule 0.436, lift 3.47x
    - 24h: 51 calls (51 a day), hit rate 0.804, chance 0.192, naive rule 0.418, lift 4.19x
    - 7d: 369 calls (53 a day), hit rate 0.816, chance 0.186, naive rule 0.398, lift 4.38x
    - 30d: 1575 calls (53 a day), hit rate 0.827, chance 0.188, naive rule 0.395, lift 4.41x
  - next: threshold 0.4192, hit rate recent 0.4489 / long run 0.446
    - 6h: 23 calls (94 a day), hit rate 0.522, chance 0.210, lift 2.49x
    - 24h: 121 calls (122 a day), hit rate 0.471, chance 0.192, lift 2.45x
    - 7d: 899 calls (129 a day), hit rate 0.433, chance 0.186, lift 2.32x
    - 30d: 2564 calls (85 a day), hit rate 0.462, chance 0.188, lift 2.46x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 347, 0.490; 0.40: 278, 0.562; 0.45: 226, 0.619; 0.50: 178, 0.669; 0.55: 136, 0.712; 0.60: 106, 0.756; 0.65: 78, 0.791; 0.70: 56, 0.824; 0.75: 32, 0.867; 0.80: 10, 0.895
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.419; 0.40: 157, 0.444; 0.45: 72, 0.459; 0.50: 16, 0.496; 0.55: 1, 0.488
- **K=8**: model 1792540800, labels learned 114803, probability skill vs chance 0.2018, widened contest next: False
  - now: threshold 0.5662, hit rate recent 0.681 / long run 0.6865
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.116, naive rule 0.318, lift 6.72x
    - 24h: 49 calls (49 a day), hit rate 0.714, chance 0.116, naive rule 0.326, lift 6.13x
    - 7d: 330 calls (47 a day), hit rate 0.667, chance 0.117, naive rule 0.317, lift 5.70x
    - 30d: 1542 calls (51 a day), hit rate 0.706, chance 0.121, naive rule 0.328, lift 5.82x
  - next: threshold 0.342, hit rate recent 0.3957 / long run 0.3773
    - 6h: 16 calls (66 a day), hit rate 0.438, chance 0.116, lift 3.78x
    - 24h: 102 calls (103 a day), hit rate 0.402, chance 0.116, lift 3.45x
    - 7d: 768 calls (110 a day), hit rate 0.365, chance 0.117, lift 3.12x
    - 30d: 2376 calls (79 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.422; 0.35: 193, 0.493; 0.40: 147, 0.548; 0.45: 114, 0.594; 0.50: 88, 0.635; 0.55: 64, 0.679; 0.60: 42, 0.724; 0.65: 23, 0.788; 0.70: 10, 0.838; 0.75: 1, 0.800
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 102, 0.379; 0.40: 40, 0.404; 0.45: 8, 0.429; 0.50: 1, 0.531
- **K=13**: model 1792454400, labels learned 114798, probability skill vs chance 0.1851, widened contest next: False
  - now: threshold 0.4348, hit rate recent 0.5507 / long run 0.5556
    - 6h: 11 calls (46 a day), hit rate 0.727, chance 0.078, naive rule 0.305, lift 9.29x
    - 24h: 47 calls (47 a day), hit rate 0.596, chance 0.073, naive rule 0.273, lift 8.20x
    - 7d: 392 calls (56 a day), hit rate 0.526, chance 0.076, naive rule 0.268, lift 6.91x
    - 30d: 1551 calls (52 a day), hit rate 0.571, chance 0.078, naive rule 0.271, lift 7.37x
  - next: threshold 0.2931, hit rate recent 0.3303 / long run 0.3177
    - 6h: 8 calls (33 a day), hit rate 0.250, chance 0.078, lift 3.19x
    - 24h: 63 calls (64 a day), hit rate 0.333, chance 0.073, lift 4.59x
    - 7d: 455 calls (65 a day), hit rate 0.325, chance 0.076, lift 4.28x
    - 30d: 2131 calls (71 a day), hit rate 0.307, chance 0.078, lift 3.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.451; 0.35: 86, 0.503; 0.40: 61, 0.552; 0.45: 41, 0.610; 0.50: 25, 0.657; 0.55: 14, 0.708; 0.60: 5, 0.753; 0.65: 1, 0.816
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.318; 0.35: 13, 0.350; 0.40: 2, 0.441; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.366 | 2.75% | 0.950 | 0.550 | 0.252 | 0.450 | 0.242 |
| 6h | 15.984 | 1.80% | 0.928 | 0.511 | 0.252 | 0.492 | 0.528 |
| 24h | 15.277 | 3.38% | 0.900 | 0.499 | 0.250 | 0.505 | 0.607 |
| 7d | 16.064 | 4.11% | 0.900 | 0.501 | 0.250 | 0.499 | 0.657 |
| 30d | 13.619 | 4.08% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.658 | 10.401 | 10.372 | 10.295 | 10.525 | 10.449 | 10.279 | 10.308 | 10.307 | 10.366 |
| 6h | 16.276 | 16.189 | 16.065 | 16.014 | 16.373 | 16.115 | 15.896 | 15.850 | 15.899 | 15.984 |
| 24h | 15.812 | 15.394 | 15.357 | 15.344 | 15.539 | 15.405 | 15.265 | 15.225 | 15.254 | 15.277 |
| 7d | 16.752 | 16.247 | 16.144 | 16.089 | 16.313 | 16.260 | 16.061 | 16.040 | 16.034 | 16.064 |
| 30d | 14.199 | 13.742 | 13.702 | 13.642 | 13.865 | 13.805 | 13.615 | 13.594 | 13.594 | 13.619 |

## Next candle

- candle starting 2026-10-21 21:34 UTC, last close 2499.09
- P(up) 0.5006, return quantiles (bp): {'05': -5.984, '10': -4.677, '25': -2.347, '40': -0.656, '50': -0.01, '60': 0.87, '75': 2.487, '90': 4.89, '95': 6.143}
- changepoint probability 0.0414, regime age 70.1 min
- agent weights: empirical 0.005, ewma 0.068, garch 0.101, har 0.131, bocpd 0.023, hmm 0.068, online_qr 0.243, lgbm 0.361

## Learning log

- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- HMM volatility states (sd, bp per minute): [3.23, 5.7, 16.21], current probabilities: [0.915, 0.084, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-21 21:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.37, 'l_abs': 0.703, 'l_hi': 0.757, 'l_lo': 0.792, 'b05': 0.703, 'b25': 0.669, 'b75': 0.667, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.42, 1.708, 1.788, 2.044, 2.382, 2.578, 2.991, 3.243, 3.495, 3.673, 3.921, 4.257, 4.338, 4.5]}
- calibration offsets (in sigma): {'05': 0.0565, '10': 0.003, '25': 0.0125, '40': 0.042, '50': -0.015, '60': -0.002, '75': 0.0175, '90': 0.037, '95': 0.0135}
