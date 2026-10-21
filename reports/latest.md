# ETH-USD 60s candle generator - report

- generated: 2026-10-21 13:04 UTC
- last closed candle: 2026-10-21 13:04 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.534 (672) [0.497, 0.571] | 0.521 (2876) [0.502, 0.539] | 0.514 (4698) [0.498, 0.528] | 0.518 (1726) [0.491, 0.545] | 0.654 (52) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.579 (848) | 0.556 (5623) [0.548, 0.565] | 0.526 (23426) [0.517, 0.535] | 0.515 (38261) [0.508, 0.522] | 0.547 (14023) [0.541, 0.553] | 0.546 (456) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.579 (209) | 0.594 (870) [0.572, 0.620] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.584 (101) | 0.500 | flat -0.011 (noise 0.023) |
| colour_next | 0.548 (1439) | 0.535 (10025) [0.526, 0.543] | 0.517 (42863) [0.512, 0.524] | 0.511 (70022) [0.507, 0.516] | 0.530 (25673) [0.525, 0.535] | 0.529 (781) | 0.500 | flat +0.012 (noise 0.007) |
| colour_path | 0.493 (20146) | 0.500 (140350) [0.496, 0.504] | 0.501 (600082) [0.499, 0.502] | 0.500 (980308) [0.499, 0.501] | 0.500 (359422) [0.498, 0.502] | 0.503 (10934) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.691 (55) | 0.629 (210) [0.581, 0.672] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.615 (26) | 0.500 | flat -0.047 (noise 0.045) |
| reversal_k13_next | 0.355 (76) | 0.315 (445) [0.298, 0.330] | 0.308 (2119) [0.296, 0.320] | 0.307 (3377) [0.296, 0.319] | 0.320 (1272) [0.308, 0.332] | 0.359 (39) | 0.077 | flat -0.007 (noise 0.030) |
| reversal_k13_now | 0.510 (51) | 0.519 (391) [0.491, 0.550] | 0.571 (1553) [0.551, 0.591] | 0.574 (2457) [0.557, 0.590] | 0.562 (985) [0.538, 0.588] | 0.565 (23) | 0.077 | flat -0.070 (noise 0.036) |
| reversal_k3_next | 0.533 (122) | 0.562 (737) [0.550, 0.573] | 0.571 (2652) [0.559, 0.584] | 0.580 (4203) [0.570, 0.591] | 0.570 (1763) [0.557, 0.585] | 0.707 (82) | 0.292 | flat -0.005 (noise 0.026) |
| reversal_k3_now | 0.912 (57) | 0.930 (384) [0.906, 0.954] | 0.933 (1700) [0.925, 0.943] | 0.936 (2794) [0.929, 0.944] | 0.927 (1031) [0.917, 0.938] | 0.969 (32) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.380 (129) | 0.439 (878) [0.415, 0.464] | 0.462 (2498) [0.447, 0.478] | 0.473 (3789) [0.460, 0.488] | 0.450 (1799) [0.434, 0.469] | 0.528 (72) | 0.187 | flat -0.029 (noise 0.028) |
| reversal_k5_now | 0.840 (50) | 0.823 (355) [0.796, 0.846] | 0.827 (1584) [0.813, 0.841] | 0.831 (2563) [0.819, 0.843] | 0.821 (952) [0.804, 0.838] | 0.815 (27) | 0.187 | flat +0.013 (noise 0.029) |
| reversal_k8_next | 0.376 (109) | 0.362 (730) [0.337, 0.384] | 0.387 (2335) [0.372, 0.401] | 0.389 (3770) [0.377, 0.402] | 0.380 (1664) [0.363, 0.398] | 0.426 (61) | 0.121 | flat -0.025 (noise 0.027) |
| reversal_k8_now | 0.619 (42) | 0.665 (325) [0.629, 0.701] | 0.704 (1553) [0.685, 0.724] | 0.703 (2542) [0.687, 0.720] | 0.686 (955) [0.661, 0.710] | 0.731 (26) | 0.122 | flat -0.005 (noise 0.035) |
| overall | 0.497 (22317) | 0.504 (155292) [0.501, 0.507] | 0.503 (661815) [0.502, 0.505] | 0.503 (1080523) [0.502, 0.504] | 0.503 (397242) [0.501, 0.506] | 0.509 (12129) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06728, 0.102] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5328, 'levels': [{'threshold': 0.06728, 'calls_per_day': 145.4, 'win_rate': 0.5699}, {'threshold': 0.102, 'calls_per_day': 36.5, 'win_rate': 0.642}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 25316, 'rate': 0.531}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15142 | 0.337 | 0.523 (14896) | 0.588 (1499) | 0.766 (2479) |
| volatility: normal | 15141 | 0.365 | 0.521 (15078) | 0.622 (727) | 0.760 (2211) |
| volatility: wild | 15141 | 0.379 | 0.510 (15103) | 0.615 (286) | 0.774 (2047) |
| session: Asia 00-08 | 15360 | 0.359 | 0.524 (15261) | 0.612 (928) | 0.767 (2259) |
| session: Europe 08-13 | 9600 | 0.354 | 0.520 (9515) | 0.597 (635) | 0.774 (1512) |
| session: US 13-21 | 14884 | 0.368 | 0.512 (14782) | 0.576 (587) | 0.769 (2141) |
| session: late 21-24 | 5580 | 0.351 | 0.515 (5519) | 0.622 (362) | 0.744 (825) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.380 | 0.363 | 0.294 | 0.294 | 0.542 | 0.287 | 0.474 | 1.400 |
| 6h | 360 | 0.359 | 0.359 | 0.278 | 0.314 | 0.526 | 0.261 | 0.457 | 1.269 |
| 24h | 1440 | 0.371 | 0.363 | 0.283 | 0.321 | 0.524 | 0.264 | 0.477 | 1.189 |
| 7d | 10080 | 0.369 | 0.360 | 0.277 | 0.310 | 0.532 | 0.266 | 0.472 | 1.221 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.518 | 0.253 | 0.466 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.380 / 0.542 / 0.933; 2: 0.359 / 0.458 / 0.933; 3: 0.358 / 0.508 / 0.900; 4: 0.371 / 0.475 / 0.917; 5: 0.352 / 0.441 / 0.933; 6: 0.362 / 0.576 / 0.933; 7: 0.356 / 0.525 / 0.950; 8: 0.338 / 0.424 / 0.950; 9: 0.341 / 0.492 / 0.983; 10: 0.347 / 0.441 / 1.000; 11: 0.361 / 0.492 / 1.000; 12: 0.348 / 0.441 / 1.000; 13: 0.334 / 0.458 / 1.000; 14: 0.364 / 0.475 / 1.000; 15: 0.327 / 0.492 / 1.000
- 6h: 1: 0.359 / 0.526 / 0.878; 2: 0.352 / 0.474 / 0.881; 3: 0.344 / 0.499 / 0.858; 4: 0.358 / 0.504 / 0.878; 5: 0.355 / 0.524 / 0.867; 6: 0.342 / 0.476 / 0.872; 7: 0.353 / 0.504 / 0.836; 8: 0.338 / 0.482 / 0.856; 9: 0.339 / 0.504 / 0.847; 10: 0.354 / 0.529 / 0.878; 11: 0.337 / 0.485 / 0.861; 12: 0.348 / 0.515 / 0.853; 13: 0.346 / 0.526 / 0.853; 14: 0.340 / 0.479 / 0.836; 15: 0.344 / 0.515 / 0.875
- 24h: 1: 0.371 / 0.524 / 0.892; 2: 0.360 / 0.500 / 0.915; 3: 0.355 / 0.495 / 0.903; 4: 0.362 / 0.509 / 0.910; 5: 0.361 / 0.513 / 0.908; 6: 0.353 / 0.475 / 0.899; 7: 0.356 / 0.495 / 0.899; 8: 0.356 / 0.499 / 0.897; 9: 0.350 / 0.484 / 0.898; 10: 0.356 / 0.511 / 0.901; 11: 0.351 / 0.494 / 0.892; 12: 0.351 / 0.479 / 0.887; 13: 0.351 / 0.493 / 0.893; 14: 0.349 / 0.486 / 0.885; 15: 0.352 / 0.516 / 0.892
- 7d: 1: 0.369 / 0.532 / 0.897; 2: 0.356 / 0.494 / 0.901; 3: 0.359 / 0.505 / 0.900; 4: 0.355 / 0.497 / 0.900; 5: 0.355 / 0.499 / 0.901; 6: 0.354 / 0.496 / 0.901; 7: 0.353 / 0.498 / 0.901; 8: 0.353 / 0.500 / 0.901; 9: 0.354 / 0.502 / 0.901; 10: 0.356 / 0.510 / 0.902; 11: 0.350 / 0.498 / 0.901; 12: 0.353 / 0.504 / 0.901; 13: 0.351 / 0.499 / 0.902; 14: 0.351 / 0.501 / 0.901; 15: 0.351 / 0.501 / 0.903
- 30d: 1: 0.360 / 0.518 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.350 / 0.500 / 0.900; 7: 0.349 / 0.500 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.198 (body 0.127, range 0.269); 'price stays where it was' would score 0.193; colour right 0.492; typical miss of the close 6.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.160 (body 0.115, range 0.205); 'price stays where it was' would score 0.157; colour right 0.560; typical miss of the close 6.8 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.140 (body 0.096, range 0.184); 'price stays where it was' would score 0.142; colour right 0.533; typical miss of the close 8.4 bp; chain ended on the right side 0.604 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.134; colour right 0.506; typical miss of the close 9.1 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.121 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.7 bp; chain ended on the right side 0.524 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.9; 2: 0.197 / 4.5; 3: 0.165 / 6.0; 4: 0.133 / 6.5; 5: 0.119 / 7.2; 6: 0.110 / 7.7; 7: 0.104 / 8.1; 8: 0.096 / 8.4; 9: 0.088 / 8.3; 10: 0.087 / 9.1; 11: 0.082 / 9.6; 12: 0.079 / 10.0; 13: 0.068 / 10.2; 14: 0.068 / 10.5; 15: 0.059 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 114298, probability skill vs chance 0.2259, widened contest next: False
  - now: threshold 0.8355, hit rate recent 0.9373 / long run 0.9311
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.320, naive rule 0.542, lift 3.13x
    - 24h: 53 calls (53 a day), hit rate 0.943, chance 0.311, naive rule 0.514, lift 3.03x
    - 7d: 387 calls (55 a day), hit rate 0.928, chance 0.290, naive rule 0.482, lift 3.20x
    - 30d: 1696 calls (57 a day), hit rate 0.933, chance 0.292, naive rule 0.485, lift 3.19x
  - next: threshold 0.517, hit rate recent 0.6534 / long run 0.5807
    - 6h: 37 calls (150 a day), hit rate 0.622, chance 0.320, lift 1.94x
    - 24h: 130 calls (130 a day), hit rate 0.631, chance 0.311, lift 2.03x
    - 7d: 773 calls (110 a day), hit rate 0.574, chance 0.290, lift 1.98x
    - 30d: 2702 calls (90 a day), hit rate 0.575, chance 0.292, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 570, 0.491; 0.35: 541, 0.515; 0.40: 482, 0.568; 0.45: 413, 0.638; 0.50: 360, 0.690; 0.55: 315, 0.732; 0.60: 268, 0.776; 0.65: 224, 0.805; 0.70: 178, 0.837; 0.75: 138, 0.872; 0.80: 93, 0.911; 0.85: 48, 0.949; 0.90: 4, 0.983
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 498, 0.461; 0.40: 406, 0.493; 0.45: 310, 0.525; 0.50: 201, 0.556; 0.55: 91, 0.570; 0.60: 14, 0.610; 0.65: 1, 0.690
- **K=5**: model 1792540800, labels learned 114296, probability skill vs chance 0.2157, widened contest next: False
  - now: threshold 0.6822, hit rate recent 0.8293 / long run 0.8244
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.180, naive rule 0.395, lift 4.76x
    - 24h: 45 calls (45 a day), hit rate 0.844, chance 0.185, naive rule 0.401, lift 4.56x
    - 7d: 363 calls (52 a day), hit rate 0.824, chance 0.186, naive rule 0.399, lift 4.42x
    - 30d: 1574 calls (52 a day), hit rate 0.829, chance 0.187, naive rule 0.394, lift 4.43x
  - next: threshold 0.4196, hit rate recent 0.4697 / long run 0.4481
    - 6h: 35 calls (143 a day), hit rate 0.457, chance 0.180, lift 2.54x
    - 24h: 127 calls (128 a day), hit rate 0.433, chance 0.185, lift 2.34x
    - 7d: 902 calls (129 a day), hit rate 0.442, chance 0.186, lift 2.38x
    - 30d: 2542 calls (85 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.423; 0.35: 347, 0.489; 0.40: 279, 0.560; 0.45: 226, 0.617; 0.50: 178, 0.666; 0.55: 136, 0.712; 0.60: 106, 0.755; 0.65: 78, 0.792; 0.70: 56, 0.825; 0.75: 32, 0.869; 0.80: 10, 0.894
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.418; 0.40: 157, 0.444; 0.45: 73, 0.461; 0.50: 17, 0.503; 0.55: 2, 0.511
- **K=8**: model 1792540800, labels learned 114293, probability skill vs chance 0.205, widened contest next: False
  - now: threshold 0.5664, hit rate recent 0.6658 / long run 0.6854
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.124, naive rule 0.348, lift 6.81x
    - 24h: 43 calls (43 a day), hit rate 0.674, chance 0.112, naive rule 0.309, lift 6.01x
    - 7d: 324 calls (46 a day), hit rate 0.667, chance 0.117, naive rule 0.317, lift 5.71x
    - 30d: 1545 calls (52 a day), hit rate 0.707, chance 0.121, naive rule 0.328, lift 5.83x
  - next: threshold 0.3449, hit rate recent 0.4086 / long run 0.3774
    - 6h: 28 calls (115 a day), hit rate 0.429, chance 0.124, lift 3.45x
    - 24h: 102 calls (103 a day), hit rate 0.373, chance 0.112, lift 3.32x
    - 7d: 758 calls (108 a day), hit rate 0.365, chance 0.117, lift 3.13x
    - 30d: 2366 calls (79 a day), hit rate 0.389, chance 0.121, lift 3.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.421; 0.35: 193, 0.492; 0.40: 147, 0.548; 0.45: 115, 0.593; 0.50: 88, 0.636; 0.55: 64, 0.681; 0.60: 43, 0.725; 0.65: 23, 0.788; 0.70: 10, 0.835; 0.75: 1, 0.821
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.351; 0.35: 102, 0.381; 0.40: 40, 0.408; 0.45: 8, 0.433; 0.50: 1, 0.500
- **K=13**: model 1792454400, labels learned 114288, probability skill vs chance 0.1823, widened contest next: True
  - now: threshold 0.4341, hit rate recent 0.5202 / long run 0.5532
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.070, naive rule 0.250, lift 8.85x
    - 24h: 41 calls (41 a day), hit rate 0.537, chance 0.072, naive rule 0.257, lift 7.50x
    - 7d: 386 calls (55 a day), hit rate 0.521, chance 0.076, naive rule 0.267, lift 6.86x
    - 30d: 1550 calls (52 a day), hit rate 0.571, chance 0.078, naive rule 0.271, lift 7.36x
  - next: threshold 0.2916, hit rate recent 0.3368 / long run 0.3179
    - 6h: 19 calls (79 a day), hit rate 0.263, chance 0.070, lift 3.78x
    - 24h: 76 calls (77 a day), hit rate 0.303, chance 0.072, lift 4.23x
    - 7d: 455 calls (65 a day), hit rate 0.323, chance 0.076, lift 4.26x
    - 30d: 2137 calls (71 a day), hit rate 0.309, chance 0.078, lift 3.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.450; 0.35: 86, 0.504; 0.40: 61, 0.554; 0.45: 41, 0.609; 0.50: 25, 0.656; 0.55: 14, 0.710; 0.60: 5, 0.761; 0.65: 1, 0.853
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.321; 0.35: 13, 0.353; 0.40: 2, 0.448

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.027 | 0.14% | 0.950 | 0.533 | 0.247 | 0.559 | 0.304 |
| 6h | 14.452 | 0.26% | 0.894 | 0.517 | 0.249 | 0.529 | 0.262 |
| 24h | 15.808 | 3.77% | 0.899 | 0.512 | 0.251 | 0.499 | 0.689 |
| 7d | 16.156 | 4.20% | 0.899 | 0.500 | 0.251 | 0.498 | 0.659 |
| 30d | 13.675 | 4.01% | 0.900 | 0.500 | 0.251 | 0.495 | 0.672 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.045 | 13.090 | 13.132 | 13.033 | 13.147 | 13.111 | 12.971 | 13.014 | 13.011 | 13.027 |
| 6h | 14.490 | 14.538 | 14.540 | 14.549 | 14.653 | 14.540 | 14.435 | 14.416 | 14.447 | 14.452 |
| 24h | 16.428 | 15.876 | 15.813 | 15.829 | 15.993 | 15.938 | 15.803 | 15.767 | 15.769 | 15.808 |
| 7d | 16.863 | 16.324 | 16.227 | 16.176 | 16.384 | 16.356 | 16.154 | 16.135 | 16.125 | 16.156 |
| 30d | 14.247 | 13.796 | 13.757 | 13.698 | 13.917 | 13.860 | 13.670 | 13.650 | 13.649 | 13.675 |

## Next candle

- candle starting 2026-10-21 13:04 UTC, last close 2470.29
- P(up) 0.5292, return quantiles (bp): {'05': -8.734, '10': -6.66, '25': -3.508, '40': -0.98, '50': 0.396, '60': 1.357, '75': 3.711, '90': 7.429, '95': 9.56}
- changepoint probability 0.0492, regime age 208.8 min
- agent weights: empirical 0.031, ewma 0.122, garch 0.139, har 0.116, bocpd 0.051, hmm 0.096, online_qr 0.212, lgbm 0.233

## Learning log

- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- 2026-10-21 12:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9094}, "hmm": {"sd_bp": [3.23, 5.7, 16.21], "stay": [0.979, 0.975, 0.917]}}
- HMM volatility states (sd, bp per minute): [3.23, 5.7, 16.21], current probabilities: [0.099, 0.884, 0.017]
- live generator: {'versions': 60, 'latest_effective': '2026-10-21 13:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.173, 'l_abs': 0.675, 'l_hi': 0.768, 'l_lo': 0.805, 'b05': 0.702, 'b25': 0.657, 'b75': 0.607, 'b95': 0.689}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.601, 1.926, 2.228, 2.65, 2.909, 3.55, 3.654, 3.883, 3.358, 3.9, 4.164, 4.257, 4.795, 3.834]}
- calibration offsets (in sigma): {'05': 0.0415, '10': 0.033, '25': 0.0375, '40': 0.082, '50': 0.095, '60': 0.038, '75': 0.0425, '90': 0.087, '95': 0.0485}
