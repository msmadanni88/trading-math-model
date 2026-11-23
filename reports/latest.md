# ETH-USD 60s candle generator - report

- generated: 2026-11-23 21:16 UTC
- last closed candle: 2026-11-23 21:16 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.533 (672) [0.507, 0.558] | 0.517 (2879) [0.501, 0.533] | 0.515 (7865) [0.505, 0.526] | 0.518 (4893) [0.504, 0.532] | 0.518 (85) | 0.500 | flat +0.011 (noise 0.029) |
| colour_clear | 0.529 (780) | 0.546 (5561) [0.532, 0.561] | 0.541 (23786) [0.535, 0.547] | 0.526 (64534) [0.520, 0.531] | 0.543 (40296) [0.539, 0.548] | 0.564 (697) | 0.500 | flat +0.007 (noise 0.010) |
| colour_confident | 0.588 (272) | 0.576 (1351) [0.556, 0.593] | 0.574 (4578) [0.563, 0.584] | 0.586 (7502) [0.577, 0.595] | 0.586 (7502) [0.577, 0.595] | 0.577 (194) | 0.500 | flat +0.046 (noise 0.024) |
| colour_next | 0.532 (1435) | 0.530 (10047) [0.524, 0.536] | 0.530 (42899) [0.526, 0.534] | 0.519 (117224) [0.515, 0.522] | 0.530 (72875) [0.527, 0.533] | 0.559 (1269) | 0.500 | flat +0.002 (noise 0.007) |
| colour_path | 0.499 (20090) | 0.503 (140658) [0.501, 0.505] | 0.502 (600586) [0.501, 0.503] | 0.501 (1641136) [0.500, 0.502] | 0.501 (1020250) [0.500, 0.502] | 0.499 (17766) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.635 (96) | 0.615 (395) [0.584, 0.647] | 0.609 (1257) [0.594, 0.623] | 0.625 (1993) [0.610, 0.638] | 0.625 (1993) [0.610, 0.638] | 0.583 (60) | 0.500 | flat +0.036 (noise 0.054) |
| reversal_k13_next | 0.455 (44) | 0.326 (476) [0.286, 0.376] | 0.336 (1843) [0.318, 0.355] | 0.317 (5398) [0.307, 0.326] | 0.328 (3293) [0.317, 0.340] | 0.318 (44) | 0.078 | flat -0.026 (noise 0.033) |
| reversal_k13_now | 0.577 (52) | 0.555 (373) [0.520, 0.595] | 0.577 (1628) [0.557, 0.596] | 0.574 (4228) [0.561, 0.586] | 0.570 (2756) [0.555, 0.586] | 0.538 (39) | 0.078 | flat -0.049 (noise 0.037) |
| reversal_k3_next | 0.657 (169) | 0.600 (797) [0.568, 0.628] | 0.604 (2553) [0.592, 0.617] | 0.591 (7061) [0.582, 0.599] | 0.593 (4621) [0.582, 0.603] | 0.541 (135) | 0.294 | flat -0.024 (noise 0.033) |
| reversal_k3_now | 0.950 (60) | 0.938 (388) [0.921, 0.956] | 0.931 (1718) [0.922, 0.941] | 0.935 (4692) [0.930, 0.941] | 0.931 (2929) [0.925, 0.938] | 0.954 (43) | 0.293 | flat +0.014 (noise 0.018) |
| reversal_k5_next | 0.639 (36) | 0.487 (355) [0.429, 0.558] | 0.512 (1890) [0.493, 0.531] | 0.487 (6071) [0.476, 0.498] | 0.483 (4081) [0.469, 0.498] | 0.451 (51) | 0.187 | flat -0.019 (noise 0.048) |
| reversal_k5_now | 0.864 (59) | 0.801 (418) [0.772, 0.828] | 0.796 (1761) [0.780, 0.812] | 0.817 (4477) [0.807, 0.826] | 0.805 (2866) [0.793, 0.816] | 0.808 (47) | 0.187 | flat +0.058 (noise 0.029) |
| reversal_k8_next | 0.467 (75) | 0.411 (569) [0.381, 0.446] | 0.417 (2285) [0.402, 0.434] | 0.399 (6386) [0.389, 0.409] | 0.400 (4280) [0.388, 0.412] | 0.352 (71) | 0.121 | flat -0.027 (noise 0.031) |
| reversal_k8_now | 0.656 (61) | 0.662 (423) [0.637, 0.684] | 0.682 (1645) [0.664, 0.700] | 0.694 (4329) [0.682, 0.707] | 0.683 (2742) [0.668, 0.697] | 0.630 (46) | 0.122 | flat -0.005 (noise 0.034) |
| overall | 0.505 (22177) | 0.507 (155176) [0.505, 0.509] | 0.506 (661687) [0.505, 0.507] | 0.504 (1808867) [0.503, 0.505] | 0.505 (1125586) [0.504, 0.506] | 0.504 (19596) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07711, 0.1097] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5313, 'levels': [{'threshold': 0.07711, 'calls_per_day': 146.7, 'win_rate': 0.5854}, {'threshold': 0.1097, 'calls_per_day': 37.7, 'win_rate': 0.6113}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42898, 'rate': 0.5306}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15306 | 0.350 | 0.532 (15087) | 0.565 (2276) | 0.754 (2576) |
| volatility: normal | 15305 | 0.379 | 0.527 (15249) | 0.585 (1535) | 0.739 (2424) |
| volatility: wild | 15305 | 0.390 | 0.532 (15266) | 0.591 (1163) | 0.751 (2162) |
| session: Asia 00-08 | 15360 | 0.371 | 0.530 (15245) | 0.564 (1724) | 0.750 (2311) |
| session: Europe 08-13 | 9600 | 0.367 | 0.532 (9523) | 0.584 (1241) | 0.757 (1537) |
| session: US 13-21 | 15360 | 0.380 | 0.535 (15270) | 0.605 (1396) | 0.740 (2470) |
| session: late 21-24 | 5596 | 0.366 | 0.517 (5564) | 0.535 (613) | 0.749 (844) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.396 | 0.413 | 0.301 | 0.301 | 0.550 | 0.251 | 0.540 | 1.453 |
| 6h | 360 | 0.395 | 0.394 | 0.319 | 0.360 | 0.563 | 0.279 | 0.512 | 1.211 |
| 24h | 1440 | 0.387 | 0.380 | 0.299 | 0.333 | 0.559 | 0.277 | 0.498 | 1.122 |
| 7d | 10080 | 0.385 | 0.377 | 0.299 | 0.332 | 0.533 | 0.268 | 0.502 | 1.178 |
| 30d | 43200 | 0.373 | 0.367 | 0.287 | 0.318 | 0.531 | 0.266 | 0.480 | 1.262 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.396 / 0.550 / 0.917; 2: 0.397 / 0.550 / 0.883; 3: 0.378 / 0.417 / 0.917; 4: 0.384 / 0.500 / 0.917; 5: 0.401 / 0.517 / 0.917; 6: 0.369 / 0.467 / 0.933; 7: 0.406 / 0.550 / 0.983; 8: 0.382 / 0.450 / 0.983; 9: 0.417 / 0.600 / 0.983; 10: 0.379 / 0.483 / 0.950; 11: 0.400 / 0.483 / 0.967; 12: 0.413 / 0.567 / 0.967; 13: 0.415 / 0.533 / 0.983; 14: 0.395 / 0.450 / 0.983; 15: 0.395 / 0.450 / 1.000
- 6h: 1: 0.395 / 0.563 / 0.931; 2: 0.380 / 0.496 / 0.900; 3: 0.395 / 0.532 / 0.906; 4: 0.367 / 0.474 / 0.839; 5: 0.388 / 0.504 / 0.878; 6: 0.369 / 0.490 / 0.881; 7: 0.393 / 0.532 / 0.919; 8: 0.379 / 0.490 / 0.914; 9: 0.392 / 0.563 / 0.906; 10: 0.374 / 0.515 / 0.886; 11: 0.378 / 0.521 / 0.881; 12: 0.382 / 0.518 / 0.867; 13: 0.365 / 0.454 / 0.867; 14: 0.382 / 0.499 / 0.886; 15: 0.374 / 0.504 / 0.872
- 24h: 1: 0.387 / 0.559 / 0.894; 2: 0.363 / 0.480 / 0.887; 3: 0.374 / 0.518 / 0.881; 4: 0.360 / 0.481 / 0.857; 5: 0.375 / 0.512 / 0.876; 6: 0.360 / 0.482 / 0.874; 7: 0.371 / 0.516 / 0.893; 8: 0.364 / 0.498 / 0.897; 9: 0.365 / 0.511 / 0.894; 10: 0.364 / 0.508 / 0.885; 11: 0.366 / 0.508 / 0.874; 12: 0.371 / 0.525 / 0.873; 13: 0.360 / 0.477 / 0.871; 14: 0.365 / 0.505 / 0.879; 15: 0.362 / 0.497 / 0.873
- 7d: 1: 0.385 / 0.533 / 0.900; 2: 0.372 / 0.494 / 0.898; 3: 0.372 / 0.506 / 0.897; 4: 0.369 / 0.494 / 0.894; 5: 0.374 / 0.513 / 0.897; 6: 0.369 / 0.498 / 0.897; 7: 0.370 / 0.505 / 0.900; 8: 0.370 / 0.509 / 0.900; 9: 0.367 / 0.499 / 0.900; 10: 0.368 / 0.509 / 0.898; 11: 0.367 / 0.505 / 0.896; 12: 0.369 / 0.507 / 0.896; 13: 0.365 / 0.498 / 0.896; 14: 0.366 / 0.502 / 0.898; 15: 0.365 / 0.499 / 0.898
- 30d: 1: 0.373 / 0.531 / 0.898; 2: 0.360 / 0.491 / 0.900; 3: 0.363 / 0.511 / 0.899; 4: 0.359 / 0.498 / 0.899; 5: 0.361 / 0.506 / 0.899; 6: 0.358 / 0.502 / 0.899; 7: 0.359 / 0.502 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.358 / 0.501 / 0.900; 10: 0.358 / 0.504 / 0.900; 11: 0.358 / 0.506 / 0.900; 12: 0.358 / 0.504 / 0.900; 13: 0.357 / 0.500 / 0.900; 14: 0.356 / 0.502 / 0.900; 15: 0.356 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.140 (body 0.084, range 0.195); 'price stays where it was' would score 0.132; colour right 0.533; typical miss of the close 14.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.134 (body 0.084, range 0.183); 'price stays where it was' would score 0.137; colour right 0.507; typical miss of the close 17.9 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.128 (body 0.084, range 0.172); 'price stays where it was' would score 0.129; colour right 0.492; typical miss of the close 14.3 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.134 (body 0.087, range 0.181); 'price stays where it was' would score 0.139; colour right 0.504; typical miss of the close 13.7 bp; chain ended on the right side 0.521 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.169); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.5 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.6; 2: 0.206 / 6.4; 3: 0.167 / 8.2; 4: 0.136 / 8.7; 5: 0.126 / 9.4; 6: 0.120 / 10.1; 7: 0.117 / 10.7; 8: 0.100 / 11.5; 9: 0.093 / 12.2; 10: 0.090 / 12.6; 11: 0.087 / 13.2; 12: 0.081 / 13.2; 13: 0.074 / 14.0; 14: 0.070 / 14.4; 15: 0.067 / 14.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 162310, probability skill vs chance 0.2421, widened contest next: True
  - now: threshold 0.8291, hit rate recent 0.9383 / long run 0.9333
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.306, naive rule 0.533, lift 2.80x
    - 24h: 48 calls (48 a day), hit rate 0.938, chance 0.301, naive rule 0.539, lift 3.11x
    - 7d: 384 calls (55 a day), hit rate 0.938, chance 0.295, naive rule 0.514, lift 3.18x
    - 30d: 1717 calls (57 a day), hit rate 0.931, chance 0.294, naive rule 0.503, lift 3.17x
  - next: threshold 0.5118, hit rate recent 0.5588 / long run 0.5992
    - 6h: 39 calls (158 a day), hit rate 0.590, chance 0.306, lift 1.93x
    - 24h: 145 calls (146 a day), hit rate 0.538, chance 0.301, lift 1.78x
    - 7d: 861 calls (123 a day), hit rate 0.590, chance 0.295, lift 2.00x
    - 30d: 2638 calls (88 a day), hit rate 0.600, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 558, 0.503; 0.35: 529, 0.528; 0.40: 478, 0.574; 0.45: 414, 0.640; 0.50: 364, 0.685; 0.55: 316, 0.731; 0.60: 266, 0.776; 0.65: 224, 0.806; 0.70: 176, 0.837; 0.75: 141, 0.873; 0.80: 93, 0.904; 0.85: 43, 0.939; 0.90: 4, 0.962
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.436; 0.35: 488, 0.470; 0.40: 386, 0.510; 0.45: 291, 0.543; 0.50: 186, 0.574; 0.55: 78, 0.585; 0.60: 10, 0.637; 0.65: 0, 0.571
- **K=5**: model 1794528000, labels learned 162308, probability skill vs chance 0.2242, widened contest next: False
  - now: threshold 0.7005, hit rate recent 0.8104 / long run 0.7948
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.195, naive rule 0.426, lift 4.19x
    - 24h: 53 calls (53 a day), hit rate 0.811, chance 0.195, naive rule 0.449, lift 4.16x
    - 7d: 410 calls (59 a day), hit rate 0.810, chance 0.195, naive rule 0.433, lift 4.15x
    - 30d: 1758 calls (59 a day), hit rate 0.795, chance 0.188, naive rule 0.415, lift 4.23x
  - next: threshold 0.4188, hit rate recent 0.5166 / long run 0.5038
    - 6h: 25 calls (102 a day), hit rate 0.480, chance 0.195, lift 2.46x
    - 24h: 55 calls (55 a day), hit rate 0.455, chance 0.195, lift 2.33x
    - 7d: 346 calls (49 a day), hit rate 0.471, chance 0.195, lift 2.41x
    - 30d: 1834 calls (61 a day), hit rate 0.512, chance 0.188, lift 2.72x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.425; 0.35: 362, 0.476; 0.40: 293, 0.543; 0.45: 237, 0.603; 0.50: 186, 0.654; 0.55: 149, 0.686; 0.60: 115, 0.732; 0.65: 82, 0.770; 0.70: 51, 0.803; 0.75: 27, 0.838; 0.80: 6, 0.847
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 334, 0.394; 0.35: 249, 0.432; 0.40: 158, 0.462; 0.45: 64, 0.509; 0.50: 8, 0.564; 0.55: 1, 0.471
- **K=8**: model 1794960000, labels learned 162305, probability skill vs chance 0.209, widened contest next: False
  - now: threshold 0.5831, hit rate recent 0.6405 / long run 0.6696
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.117, naive rule 0.318, lift 4.98x
    - 24h: 53 calls (53 a day), hit rate 0.660, chance 0.120, naive rule 0.359, lift 5.51x
    - 7d: 422 calls (60 a day), hit rate 0.666, chance 0.124, naive rule 0.358, lift 5.36x
    - 30d: 1641 calls (55 a day), hit rate 0.679, chance 0.123, naive rule 0.348, lift 5.53x
  - next: threshold 0.3607, hit rate recent 0.3942 / long run 0.4158
    - 6h: 25 calls (103 a day), hit rate 0.400, chance 0.117, lift 3.41x
    - 24h: 76 calls (77 a day), hit rate 0.382, chance 0.120, lift 3.18x
    - 7d: 577 calls (83 a day), hit rate 0.406, chance 0.124, lift 3.27x
    - 30d: 2282 calls (76 a day), hit rate 0.417, chance 0.123, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 255, 0.428; 0.35: 201, 0.486; 0.40: 158, 0.536; 0.45: 120, 0.577; 0.50: 86, 0.636; 0.55: 62, 0.670; 0.60: 42, 0.709; 0.65: 24, 0.764; 0.70: 9, 0.801; 0.75: 1, 0.725
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 159, 0.377; 0.35: 84, 0.406; 0.40: 28, 0.440; 0.45: 6, 0.469; 0.50: 1, 0.656
- **K=13**: model 1795132800, labels learned 162300, probability skill vs chance 0.1954, widened contest next: False
  - now: threshold 0.4571, hit rate recent 0.5647 / long run 0.5726
    - 6h: 10 calls (42 a day), hit rate 0.500, chance 0.087, naive rule 0.348, lift 5.75x
    - 24h: 45 calls (45 a day), hit rate 0.578, chance 0.080, naive rule 0.333, lift 7.22x
    - 7d: 379 calls (54 a day), hit rate 0.549, chance 0.081, naive rule 0.305, lift 6.81x
    - 30d: 1621 calls (54 a day), hit rate 0.574, chance 0.079, naive rule 0.296, lift 7.23x
  - next: threshold 0.3054, hit rate recent 0.3906 / long run 0.3383
    - 6h: 18 calls (75 a day), hit rate 0.500, chance 0.087, lift 5.75x
    - 24h: 48 calls (49 a day), hit rate 0.375, chance 0.080, lift 4.69x
    - 7d: 454 calls (65 a day), hit rate 0.326, chance 0.081, lift 4.05x
    - 30d: 1833 calls (61 a day), hit rate 0.338, chance 0.079, lift 4.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 141, 0.424; 0.35: 103, 0.472; 0.40: 71, 0.534; 0.45: 50, 0.583; 0.50: 34, 0.621; 0.55: 21, 0.646; 0.60: 10, 0.665; 0.65: 2, 0.530; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.344; 0.35: 15, 0.388; 0.40: 2, 0.447; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.064 | 0.49% | 0.900 | 0.617 | 0.243 | 0.600 | 0.092 |
| 6h | 28.764 | 3.32% | 0.917 | 0.553 | 0.248 | 0.543 | 0.430 |
| 24h | 26.148 | 5.46% | 0.897 | 0.498 | 0.250 | 0.525 | 0.666 |
| 7d | 24.294 | 4.48% | 0.901 | 0.501 | 0.250 | 0.504 | 0.671 |
| 30d | 19.329 | 4.87% | 0.900 | 0.500 | 0.250 | 0.506 | 0.713 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.168 | 21.275 | 21.415 | 21.496 | 21.868 | 21.877 | 21.350 | 21.108 | 21.278 | 21.064 |
| 6h | 29.751 | 29.273 | 29.042 | 28.830 | 29.597 | 29.109 | 28.928 | 28.851 | 28.769 | 28.764 |
| 24h | 27.657 | 26.479 | 26.218 | 26.093 | 26.813 | 26.561 | 26.126 | 26.066 | 26.105 | 26.148 |
| 7d | 25.433 | 24.557 | 24.457 | 24.306 | 24.822 | 24.605 | 24.284 | 24.240 | 24.259 | 24.294 |
| 30d | 20.318 | 19.518 | 19.467 | 19.383 | 19.736 | 19.655 | 19.313 | 19.287 | 19.297 | 19.329 |

## Next candle

- candle starting 2026-11-23 21:16 UTC, last close 1723.42
- P(up) 0.446, return quantiles (bp): {'05': -12.541, '10': -9.989, '25': -5.143, '40': -2.738, '50': -0.898, '60': 0.801, '75': 4.26, '90': 9.151, '95': 12.919}
- changepoint probability 0.0582, regime age 79.6 min
- agent weights: empirical 0.003, ewma 0.030, garch 0.150, har 0.279, bocpd 0.007, hmm 0.020, online_qr 0.199, lgbm 0.313

## Learning log

- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- 2026-11-22 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9215}, "hmm": {"sd_bp": [5.69, 10.58, 28.33], "stay": [0.985, 0.953, 0.874]}, "lgbm": {"challenger_loss": 0.24557, "champion_loss": 0.24554, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48129, "challengers": 1, "chance_loss": 0.60807, "widened": false, "champion_loss": 0.47918, "promoted": false}, "reversal_k5": {"challenger_loss": 0.381, "challengers": 1, "chance_loss": 0.49754, "widened": false, "champion_loss": 0.37986, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28291, "challengers": 1, "chance_loss": 0.38778, "widened": false, "champion_loss": 0.28187, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20591, "challengers": 1, "chance_loss": 0.29298, "widened": false, "champion_loss": 0.20541, "promoted": false}}
- 2026-11-22 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.9173}, "hmm": {"sd_bp": [5.55, 10.36, 28.43], "stay": [0.982, 0.95, 0.859]}}
- 2026-11-23 00:00 UTC: {"garch": {"alpha": 0.0752, "beta": 0.917}, "hmm": {"sd_bp": [5.28, 10.22, 28.39], "stay": [0.976, 0.946, 0.857]}, "lgbm": {"challenger_loss": 0.24364, "champion_loss": 0.24354, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.61601, "widened": false, "champion_loss": 0.4869, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38212, "challengers": 1, "chance_loss": 0.503, "widened": false, "champion_loss": 0.38113, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29091, "challengers": 1, "chance_loss": 0.3912, "widened": false, "champion_loss": 0.28935, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20987, "challengers": 1, "chance_loss": 0.29233, "widened": false, "champion_loss": 0.20927, "promoted": false}}
- 2026-11-23 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.9112}, "hmm": {"sd_bp": [5.07, 10.1, 28.28], "stay": [0.973, 0.946, 0.862]}}
- HMM volatility states (sd, bp per minute): [5.07, 10.1, 28.28], current probabilities: [0.635, 0.359, 0.006]
- live generator: {'versions': 60, 'latest_effective': '2026-11-23 21:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.184, 'l_abs': 0.663, 'l_hi': 0.804, 'l_lo': 0.766, 'b05': 0.731, 'b25': 0.656, 'b75': 0.58, 'b95': 0.699}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [1.987, 3.038, 6.154, 3.784, 4.41, 2.568, 2.75, 3.166, 4.337, 6.666, 7.261, 7.422, 6.194, 7.539]}
- calibration offsets (in sigma): {'05': 0.0875, '10': 0.025, '25': 0.0075, '40': -0.07, '50': -0.095, '60': -0.12, '75': -0.0975, '90': -0.075, '95': -0.0375}
