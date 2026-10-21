# ETH-USD 60s candle generator - report

- generated: 2026-10-21 18:00 UTC
- last closed candle: 2026-10-21 17:59 UTC (staleness 1.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.534 (672) [0.497, 0.571] | 0.521 (2876) [0.502, 0.539] | 0.514 (4698) [0.498, 0.528] | 0.518 (1726) [0.491, 0.545] | 0.620 (71) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.579 (848) | 0.556 (5623) [0.548, 0.565] | 0.526 (23426) [0.517, 0.535] | 0.515 (38261) [0.508, 0.522] | 0.547 (14023) [0.541, 0.553] | 0.555 (616) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.579 (209) | 0.594 (870) [0.572, 0.620] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.594 (128) | 0.500 | flat -0.011 (noise 0.023) |
| colour_next | 0.548 (1439) | 0.535 (10025) [0.526, 0.543] | 0.517 (42863) [0.512, 0.524] | 0.511 (70022) [0.507, 0.516] | 0.530 (25673) [0.525, 0.535] | 0.539 (1075) | 0.500 | flat +0.012 (noise 0.007) |
| colour_path | 0.493 (20146) | 0.500 (140350) [0.496, 0.504] | 0.501 (600082) [0.499, 0.502] | 0.500 (980308) [0.499, 0.501] | 0.500 (359422) [0.498, 0.502] | 0.507 (15050) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.691 (55) | 0.629 (210) [0.581, 0.672] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.600 (30) | 0.500 | flat -0.047 (noise 0.045) |
| reversal_k13_next | 0.355 (76) | 0.315 (445) [0.298, 0.330] | 0.308 (2119) [0.296, 0.320] | 0.307 (3377) [0.296, 0.319] | 0.320 (1272) [0.308, 0.332] | 0.360 (50) | 0.077 | flat -0.007 (noise 0.030) |
| reversal_k13_now | 0.510 (51) | 0.519 (391) [0.491, 0.550] | 0.571 (1553) [0.551, 0.591] | 0.574 (2457) [0.557, 0.590] | 0.562 (985) [0.538, 0.588] | 0.600 (35) | 0.077 | flat -0.070 (noise 0.036) |
| reversal_k3_next | 0.533 (122) | 0.562 (737) [0.550, 0.573] | 0.571 (2652) [0.559, 0.584] | 0.580 (4203) [0.570, 0.591] | 0.570 (1763) [0.557, 0.585] | 0.670 (112) | 0.292 | flat -0.005 (noise 0.026) |
| reversal_k3_now | 0.912 (57) | 0.930 (384) [0.906, 0.954] | 0.933 (1700) [0.925, 0.943] | 0.936 (2794) [0.929, 0.944] | 0.927 (1031) [0.917, 0.938] | 0.978 (46) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.380 (129) | 0.439 (878) [0.415, 0.464] | 0.462 (2498) [0.447, 0.478] | 0.473 (3789) [0.460, 0.488] | 0.450 (1799) [0.434, 0.469] | 0.480 (100) | 0.187 | flat -0.029 (noise 0.028) |
| reversal_k5_now | 0.840 (50) | 0.823 (355) [0.796, 0.846] | 0.827 (1584) [0.813, 0.841] | 0.831 (2563) [0.819, 0.843] | 0.821 (952) [0.804, 0.838] | 0.821 (39) | 0.187 | flat +0.013 (noise 0.029) |
| reversal_k8_next | 0.376 (109) | 0.362 (730) [0.337, 0.384] | 0.387 (2335) [0.372, 0.401] | 0.389 (3770) [0.377, 0.402] | 0.380 (1664) [0.363, 0.398] | 0.417 (84) | 0.121 | flat -0.025 (noise 0.027) |
| reversal_k8_now | 0.619 (42) | 0.665 (325) [0.629, 0.701] | 0.704 (1553) [0.685, 0.724] | 0.703 (2542) [0.687, 0.720] | 0.686 (955) [0.661, 0.710] | 0.737 (38) | 0.122 | flat -0.005 (noise 0.035) |
| overall | 0.497 (22317) | 0.504 (155292) [0.501, 0.507] | 0.503 (661815) [0.502, 0.505] | 0.503 (1080523) [0.502, 0.504] | 0.503 (397242) [0.501, 0.506] | 0.512 (16700) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06728, 0.102] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5328, 'levels': [{'threshold': 0.06728, 'calls_per_day': 145.4, 'win_rate': 0.5699}, {'threshold': 0.102, 'calls_per_day': 36.5, 'win_rate': 0.642}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 25610, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15240 | 0.337 | 0.523 (14994) | 0.588 (1509) | 0.766 (2488) |
| volatility: normal | 15239 | 0.365 | 0.521 (15176) | 0.624 (720) | 0.757 (2235) |
| volatility: wild | 15240 | 0.379 | 0.511 (15201) | 0.616 (310) | 0.778 (2064) |
| session: Asia 00-08 | 15360 | 0.359 | 0.524 (15261) | 0.612 (928) | 0.767 (2259) |
| session: Europe 08-13 | 9600 | 0.354 | 0.520 (9515) | 0.597 (635) | 0.774 (1512) |
| session: US 13-21 | 15179 | 0.368 | 0.513 (15076) | 0.578 (614) | 0.770 (2191) |
| session: late 21-24 | 5580 | 0.351 | 0.515 (5519) | 0.622 (362) | 0.744 (825) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.343 | 0.344 | 0.253 | 0.253 | 0.633 | 0.224 | 0.462 | 1.897 |
| 6h | 360 | 0.387 | 0.374 | 0.295 | 0.334 | 0.564 | 0.280 | 0.494 | 1.426 |
| 24h | 1440 | 0.372 | 0.364 | 0.283 | 0.321 | 0.536 | 0.266 | 0.478 | 1.205 |
| 7d | 10080 | 0.369 | 0.360 | 0.277 | 0.309 | 0.534 | 0.267 | 0.472 | 1.229 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.519 | 0.254 | 0.466 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.343 / 0.633 / 0.967; 2: 0.339 / 0.483 / 1.000; 3: 0.350 / 0.617 / 1.000; 4: 0.311 / 0.450 / 1.000; 5: 0.335 / 0.567 / 1.000; 6: 0.330 / 0.483 / 1.000; 7: 0.339 / 0.533 / 1.000; 8: 0.344 / 0.533 / 1.000; 9: 0.338 / 0.567 / 1.000; 10: 0.320 / 0.500 / 1.000; 11: 0.343 / 0.567 / 1.000; 12: 0.312 / 0.517 / 1.000; 13: 0.358 / 0.617 / 1.000; 14: 0.324 / 0.533 / 1.000; 15: 0.330 / 0.533 / 1.000
- 6h: 1: 0.387 / 0.564 / 0.911; 2: 0.369 / 0.503 / 0.933; 3: 0.366 / 0.506 / 0.931; 4: 0.359 / 0.500 / 0.931; 5: 0.367 / 0.522 / 0.950; 6: 0.371 / 0.503 / 0.942; 7: 0.381 / 0.550 / 0.950; 8: 0.368 / 0.525 / 0.944; 9: 0.359 / 0.492 / 0.944; 10: 0.360 / 0.494 / 0.928; 11: 0.371 / 0.520 / 0.939; 12: 0.356 / 0.486 / 0.942; 13: 0.363 / 0.508 / 0.928; 14: 0.367 / 0.511 / 0.936; 15: 0.354 / 0.503 / 0.900
- 24h: 1: 0.372 / 0.536 / 0.892; 2: 0.359 / 0.495 / 0.908; 3: 0.355 / 0.496 / 0.906; 4: 0.364 / 0.522 / 0.909; 5: 0.361 / 0.510 / 0.911; 6: 0.356 / 0.481 / 0.912; 7: 0.361 / 0.506 / 0.908; 8: 0.359 / 0.512 / 0.906; 9: 0.354 / 0.492 / 0.905; 10: 0.359 / 0.513 / 0.905; 11: 0.353 / 0.493 / 0.906; 12: 0.350 / 0.479 / 0.908; 13: 0.357 / 0.507 / 0.904; 14: 0.355 / 0.498 / 0.903; 15: 0.356 / 0.515 / 0.905
- 7d: 1: 0.369 / 0.534 / 0.896; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.505 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.354 / 0.499 / 0.900; 6: 0.353 / 0.495 / 0.900; 7: 0.353 / 0.500 / 0.899; 8: 0.353 / 0.501 / 0.900; 9: 0.353 / 0.501 / 0.900; 10: 0.355 / 0.509 / 0.900; 11: 0.350 / 0.498 / 0.899; 12: 0.352 / 0.504 / 0.899; 13: 0.352 / 0.501 / 0.899; 14: 0.351 / 0.503 / 0.899; 15: 0.350 / 0.500 / 0.899
- 30d: 1: 0.360 / 0.519 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.350 / 0.500 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.078 (body 0.033, range 0.123); 'price stays where it was' would score 0.078; colour right 0.550; typical miss of the close 10.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.121 (body 0.072, range 0.170); 'price stays where it was' would score 0.122; colour right 0.494; typical miss of the close 13.0 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.136 (body 0.090, range 0.182); 'price stays where it was' would score 0.138; colour right 0.532; typical miss of the close 8.5 bp; chain ended on the right side 0.604 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 9.1 bp; chain ended on the right side 0.543 of 672 chains; n=10080
- 30d: match 0.121 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.523 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 3.9; 2: 0.197 / 4.5; 3: 0.165 / 6.0; 4: 0.132 / 6.5; 5: 0.119 / 7.2; 6: 0.109 / 7.7; 7: 0.104 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.3; 10: 0.086 / 9.1; 11: 0.082 / 9.6; 12: 0.079 / 9.9; 13: 0.067 / 10.2; 14: 0.068 / 10.5; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 114593, probability skill vs chance 0.2214, widened contest next: False
  - now: threshold 0.8355, hit rate recent 0.9505 / long run 0.9327
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.298, naive rule 0.505, lift 3.36x
    - 24h: 59 calls (59 a day), hit rate 0.949, chance 0.308, naive rule 0.515, lift 3.09x
    - 7d: 393 calls (56 a day), hit rate 0.931, chance 0.291, naive rule 0.483, lift 3.20x
    - 30d: 1696 calls (57 a day), hit rate 0.933, chance 0.292, naive rule 0.485, lift 3.19x
  - next: threshold 0.517, hit rate recent 0.611 / long run 0.5799
    - 6h: 35 calls (142 a day), hit rate 0.571, chance 0.298, lift 1.92x
    - 24h: 140 calls (141 a day), hit rate 0.650, chance 0.308, lift 2.11x
    - 7d: 791 calls (113 a day), hit rate 0.575, chance 0.291, lift 1.98x
    - 30d: 2718 calls (91 a day), hit rate 0.574, chance 0.292, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.491; 0.35: 541, 0.515; 0.40: 482, 0.568; 0.45: 413, 0.638; 0.50: 360, 0.690; 0.55: 315, 0.732; 0.60: 268, 0.776; 0.65: 224, 0.804; 0.70: 178, 0.837; 0.75: 138, 0.871; 0.80: 93, 0.911; 0.85: 47, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 499, 0.461; 0.40: 406, 0.492; 0.45: 310, 0.524; 0.50: 201, 0.556; 0.55: 91, 0.569; 0.60: 14, 0.610; 0.65: 1, 0.690
- **K=5**: model 1792540800, labels learned 114591, probability skill vs chance 0.211, widened contest next: False
  - now: threshold 0.6822, hit rate recent 0.8313 / long run 0.8246
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.193, naive rule 0.433, lift 4.53x
    - 24h: 48 calls (48 a day), hit rate 0.812, chance 0.181, naive rule 0.395, lift 4.48x
    - 7d: 370 calls (53 a day), hit rate 0.824, chance 0.186, naive rule 0.399, lift 4.43x
    - 30d: 1575 calls (53 a day), hit rate 0.828, chance 0.187, naive rule 0.394, lift 4.42x
  - next: threshold 0.4196, hit rate recent 0.4278 / long run 0.444
    - 6h: 30 calls (123 a day), hit rate 0.400, chance 0.193, lift 2.07x
    - 24h: 128 calls (129 a day), hit rate 0.445, chance 0.181, lift 2.46x
    - 7d: 899 calls (129 a day), hit rate 0.436, chance 0.186, lift 2.34x
    - 30d: 2556 calls (85 a day), hit rate 0.462, chance 0.187, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 347, 0.488; 0.40: 279, 0.560; 0.45: 226, 0.616; 0.50: 178, 0.666; 0.55: 136, 0.710; 0.60: 106, 0.755; 0.65: 78, 0.792; 0.70: 56, 0.824; 0.75: 32, 0.867; 0.80: 10, 0.895
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 250, 0.418; 0.40: 157, 0.442; 0.45: 72, 0.458; 0.50: 17, 0.497; 0.55: 2, 0.477
- **K=8**: model 1792540800, labels learned 114588, probability skill vs chance 0.205, widened contest next: False
  - now: threshold 0.5664, hit rate recent 0.6831 / long run 0.6867
    - 6h: 15 calls (62 a day), hit rate 0.800, chance 0.129, naive rule 0.357, lift 6.20x
    - 24h: 48 calls (48 a day), hit rate 0.688, chance 0.113, naive rule 0.310, lift 6.08x
    - 7d: 332 calls (47 a day), hit rate 0.672, chance 0.117, naive rule 0.319, lift 5.72x
    - 30d: 1546 calls (52 a day), hit rate 0.706, chance 0.121, naive rule 0.327, lift 5.83x
  - next: threshold 0.3449, hit rate recent 0.406 / long run 0.3779
    - 6h: 25 calls (103 a day), hit rate 0.440, chance 0.129, lift 3.41x
    - 24h: 105 calls (106 a day), hit rate 0.381, chance 0.113, lift 3.37x
    - 7d: 766 calls (110 a day), hit rate 0.367, chance 0.117, lift 3.12x
    - 30d: 2375 calls (79 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.421; 0.35: 193, 0.492; 0.40: 147, 0.548; 0.45: 114, 0.593; 0.50: 88, 0.635; 0.55: 64, 0.679; 0.60: 43, 0.723; 0.65: 23, 0.788; 0.70: 10, 0.837; 0.75: 1, 0.828
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.350; 0.35: 102, 0.379; 0.40: 40, 0.404; 0.45: 8, 0.431; 0.50: 1, 0.515
- **K=13**: model 1792454400, labels learned 114583, probability skill vs chance 0.1865, widened contest next: False
  - now: threshold 0.4341, hit rate recent 0.5487 / long run 0.5554
    - 6h: 15 calls (63 a day), hit rate 0.667, chance 0.070, naive rule 0.280, lift 9.56x
    - 24h: 44 calls (44 a day), hit rate 0.568, chance 0.070, naive rule 0.248, lift 8.17x
    - 7d: 393 calls (56 a day), hit rate 0.532, chance 0.076, naive rule 0.269, lift 6.98x
    - 30d: 1554 calls (52 a day), hit rate 0.570, chance 0.077, naive rule 0.270, lift 7.37x
  - next: threshold 0.2916, hit rate recent 0.3411 / long run 0.3187
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.070, lift 5.97x
    - 24h: 68 calls (69 a day), hit rate 0.338, chance 0.070, lift 4.87x
    - 7d: 453 calls (65 a day), hit rate 0.329, chance 0.076, lift 4.32x
    - 30d: 2134 calls (71 a day), hit rate 0.307, chance 0.077, lift 3.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.449; 0.35: 86, 0.502; 0.40: 61, 0.552; 0.45: 41, 0.608; 0.50: 25, 0.656; 0.55: 14, 0.707; 0.60: 5, 0.755; 0.65: 1, 0.838
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.318; 0.35: 13, 0.351; 0.40: 2, 0.441; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.650 | -1.23% | 0.933 | 0.617 | 0.250 | 0.517 | 0.295 |
| 6h | 22.544 | 5.36% | 0.908 | 0.511 | 0.249 | 0.542 | 0.498 |
| 24h | 14.884 | 3.49% | 0.899 | 0.501 | 0.250 | 0.509 | 0.601 |
| 7d | 16.138 | 4.10% | 0.899 | 0.501 | 0.250 | 0.499 | 0.653 |
| 30d | 13.648 | 4.08% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.495 | 13.079 | 12.646 | 12.795 | 12.788 | 12.637 | 12.628 | 12.622 | 12.606 | 12.650 |
| 6h | 23.819 | 22.867 | 22.830 | 22.653 | 23.115 | 22.833 | 22.534 | 22.420 | 22.529 | 22.544 |
| 24h | 15.423 | 14.993 | 14.971 | 14.971 | 15.132 | 15.017 | 14.867 | 14.836 | 14.866 | 14.884 |
| 7d | 16.827 | 16.320 | 16.220 | 16.161 | 16.388 | 16.334 | 16.135 | 16.113 | 16.107 | 16.138 |
| 30d | 14.228 | 13.772 | 13.731 | 13.672 | 13.894 | 13.834 | 13.644 | 13.622 | 13.622 | 13.648 |

## Next candle

- candle starting 2026-10-21 17:59 UTC, last close 2514.68
- P(up) 0.5378, return quantiles (bp): {'05': -7.031, '10': -4.94, '25': -2.206, '40': -0.475, '50': 0.273, '60': 1.095, '75': 2.988, '90': 5.884, '95': 7.736}
- changepoint probability 0.0523, regime age 62.8 min
- agent weights: empirical 0.003, ewma 0.054, garch 0.072, har 0.117, bocpd 0.016, hmm 0.058, online_qr 0.258, lgbm 0.422

## Learning log

- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- HMM volatility states (sd, bp per minute): [3.23, 5.7, 16.21], current probabilities: [0.589, 0.408, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-10-21 18:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.296, 'l_abs': 0.703, 'l_hi': 0.755, 'l_lo': 0.793, 'b05': 0.697, 'b25': 0.637, 'b75': 0.649, 'b95': 0.688}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.324, 1.561, 1.843, 1.944, 2.266, 2.656, 2.845, 3.148, 3.131, 3.357, 3.513, 3.89, 4.127, 4.28]}
- calibration offsets (in sigma): {'05': 0.059, '10': 0.068, '25': 0.055, '40': 0.062, '50': 0.03, '60': -0.002, '75': 0.045, '90': 0.052, '95': 0.051}
