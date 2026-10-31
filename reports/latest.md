# ETH-USD 60s candle generator - report

- generated: 2026-10-31 06:19 UTC
- last closed candle: 2026-10-31 06:19 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.525 (672) [0.493, 0.564] | 0.520 (2877) [0.501, 0.539] | 0.516 (5658) [0.502, 0.529] | 0.521 (2686) [0.500, 0.541] | 0.480 (25) | 0.500 | flat -0.013 (noise 0.030) |
| colour_clear | 0.537 (771) | 0.538 (5578) [0.532, 0.544] | 0.541 (23615) [0.534, 0.547] | 0.519 (46326) [0.513, 0.525] | 0.545 (22088) [0.540, 0.549] | 0.533 (212) | 0.500 | flat -0.018 (noise 0.009) |
| colour_confident | 0.590 (78) | 0.592 (1175) [0.583, 0.602] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.601 (4099) [0.589, 0.613] | 0.500 (28) | 0.500 | flat -0.013 (noise 0.020) |
| colour_next | 0.532 (1435) | 0.525 (10026) [0.520, 0.528] | 0.527 (42871) [0.523, 0.531] | 0.514 (84351) [0.510, 0.518] | 0.529 (40002) [0.525, 0.533] | 0.533 (379) | 0.500 | flat -0.013 (noise 0.007) |
| colour_path | 0.503 (20090) | 0.502 (140364) [0.500, 0.504] | 0.501 (600194) [0.499, 0.502] | 0.501 (1180914) [0.500, 0.502] | 0.501 (560028) [0.499, 0.502] | 0.504 (5306) | 0.500 | flat +0.003 (noise 0.002) |
| colour_strong | 0.538 (13) | 0.596 (369) [0.574, 0.625] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.633 (1105) [0.612, 0.654] | 0.600 (10) | 0.500 | flat -0.046 (noise 0.039) |
| reversal_k13_next | 0.283 (53) | 0.317 (391) [0.282, 0.359] | 0.315 (2003) [0.303, 0.327] | 0.308 (3946) [0.297, 0.319] | 0.317 (1841) [0.306, 0.329] | 0.600 (15) | 0.077 | flat +0.003 (noise 0.032) |
| reversal_k13_now | 0.597 (57) | 0.575 (419) [0.531, 0.618] | 0.567 (1653) [0.547, 0.587] | 0.572 (3019) [0.558, 0.587] | 0.564 (1547) [0.543, 0.587] | 0.765 (17) | 0.077 | flat +0.050 (noise 0.035) |
| reversal_k3_next | 0.595 (116) | 0.591 (726) [0.583, 0.599] | 0.583 (2939) [0.571, 0.595] | 0.584 (5234) [0.575, 0.594] | 0.582 (2794) [0.570, 0.593] | 0.578 (45) | 0.293 | flat +0.005 (noise 0.025) |
| reversal_k3_now | 0.933 (45) | 0.952 (393) [0.924, 0.977] | 0.936 (1731) [0.926, 0.946] | 0.939 (3367) [0.933, 0.946] | 0.936 (1604) [0.925, 0.947] | 0.944 (18) | 0.293 | flat +0.022 (noise 0.021) |
| reversal_k5_next | 0.568 (37) | 0.507 (580) [0.495, 0.524] | 0.471 (3038) [0.457, 0.485] | 0.479 (4761) [0.467, 0.492] | 0.469 (2771) [0.455, 0.484] | 0.667 (18) | 0.187 | flat +0.051 (noise 0.026) |
| reversal_k5_now | 0.780 (41) | 0.830 (400) [0.817, 0.839] | 0.824 (1619) [0.812, 0.835] | 0.830 (3116) [0.820, 0.840] | 0.822 (1505) [0.810, 0.833] | 0.882 (17) | 0.187 | flat +0.017 (noise 0.028) |
| reversal_k8_next | 0.402 (92) | 0.394 (703) [0.375, 0.412] | 0.386 (2799) [0.374, 0.398] | 0.390 (4804) [0.379, 0.400] | 0.384 (2698) [0.372, 0.397] | 0.514 (35) | 0.121 | flat +0.017 (noise 0.025) |
| reversal_k8_now | 0.614 (44) | 0.697 (376) [0.643, 0.740] | 0.689 (1571) [0.668, 0.709] | 0.701 (3060) [0.685, 0.717] | 0.687 (1473) [0.664, 0.709] | 0.750 (16) | 0.121 | flat +0.037 (noise 0.040) |
| overall | 0.506 (22106) | 0.506 (155050) [0.504, 0.508] | 0.504 (663295) [0.503, 0.506] | 0.503 (1302230) [0.502, 0.504] | 0.504 (618949) [0.503, 0.506] | 0.511 (5891) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08136, 0.1245] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5243, 'levels': [{'threshold': 0.08136, 'calls_per_day': 142.5, 'win_rate': 0.5978}, {'threshold': 0.1245, 'calls_per_day': 36.0, 'win_rate': 0.5929}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 39239, 'rate': 0.5297}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15007 | 0.340 | 0.522 (14785) | 0.580 (1989) | 0.753 (2573) |
| volatility: normal | 15006 | 0.366 | 0.532 (14940) | 0.614 (1401) | 0.756 (2233) |
| volatility: wild | 15006 | 0.381 | 0.525 (14963) | 0.630 (737) | 0.765 (2026) |
| session: Asia 00-08 | 15259 | 0.361 | 0.532 (15159) | 0.601 (1482) | 0.762 (2292) |
| session: Europe 08-13 | 9300 | 0.357 | 0.528 (9215) | 0.593 (1012) | 0.750 (1510) |
| session: US 13-21 | 14880 | 0.370 | 0.523 (14788) | 0.601 (1055) | 0.762 (2172) |
| session: late 21-24 | 5580 | 0.352 | 0.514 (5526) | 0.609 (578) | 0.749 (858) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.340 | 0.333 | 0.180 | 0.180 | 0.600 | 0.293 | 0.388 | 1.168 |
| 6h | 360 | 0.354 | 0.349 | 0.253 | 0.290 | 0.547 | 0.271 | 0.438 | 1.069 |
| 24h | 1440 | 0.373 | 0.365 | 0.281 | 0.309 | 0.531 | 0.270 | 0.475 | 1.331 |
| 7d | 10080 | 0.368 | 0.361 | 0.285 | 0.316 | 0.526 | 0.264 | 0.473 | 1.229 |
| 30d | 43200 | 0.362 | 0.355 | 0.277 | 0.306 | 0.527 | 0.260 | 0.464 | 1.273 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.340 / 0.600 / 0.833; 2: 0.317 / 0.533 / 0.867; 3: 0.300 / 0.483 / 0.817; 4: 0.300 / 0.517 / 0.900; 5: 0.298 / 0.450 / 0.900; 6: 0.302 / 0.500 / 0.900; 7: 0.304 / 0.467 / 0.883; 8: 0.302 / 0.483 / 0.917; 9: 0.325 / 0.567 / 0.900; 10: 0.293 / 0.450 / 0.900; 11: 0.298 / 0.467 / 0.917; 12: 0.291 / 0.500 / 0.933; 13: 0.298 / 0.467 / 0.917; 14: 0.310 / 0.533 / 0.933; 15: 0.287 / 0.467 / 0.967
- 6h: 1: 0.354 / 0.547 / 0.875; 2: 0.339 / 0.481 / 0.853; 3: 0.348 / 0.500 / 0.861; 4: 0.340 / 0.508 / 0.925; 5: 0.350 / 0.531 / 0.944; 6: 0.335 / 0.467 / 0.931; 7: 0.353 / 0.547 / 0.933; 8: 0.339 / 0.508 / 0.939; 9: 0.353 / 0.539 / 0.928; 10: 0.333 / 0.475 / 0.928; 11: 0.341 / 0.481 / 0.925; 12: 0.340 / 0.514 / 0.914; 13: 0.337 / 0.478 / 0.908; 14: 0.335 / 0.478 / 0.931; 15: 0.357 / 0.578 / 0.939
- 24h: 1: 0.373 / 0.531 / 0.894; 2: 0.359 / 0.488 / 0.884; 3: 0.366 / 0.509 / 0.893; 4: 0.360 / 0.495 / 0.901; 5: 0.363 / 0.514 / 0.901; 6: 0.363 / 0.513 / 0.903; 7: 0.361 / 0.493 / 0.903; 8: 0.359 / 0.516 / 0.907; 9: 0.360 / 0.500 / 0.903; 10: 0.360 / 0.508 / 0.904; 11: 0.356 / 0.484 / 0.903; 12: 0.364 / 0.519 / 0.903; 13: 0.363 / 0.516 / 0.903; 14: 0.359 / 0.497 / 0.908; 15: 0.362 / 0.511 / 0.909
- 7d: 1: 0.368 / 0.526 / 0.898; 2: 0.355 / 0.491 / 0.899; 3: 0.359 / 0.508 / 0.899; 4: 0.356 / 0.501 / 0.900; 5: 0.355 / 0.506 / 0.901; 6: 0.353 / 0.503 / 0.901; 7: 0.356 / 0.503 / 0.901; 8: 0.354 / 0.507 / 0.901; 9: 0.354 / 0.500 / 0.901; 10: 0.355 / 0.505 / 0.900; 11: 0.352 / 0.502 / 0.900; 12: 0.354 / 0.504 / 0.900; 13: 0.352 / 0.501 / 0.900; 14: 0.352 / 0.503 / 0.900; 15: 0.352 / 0.498 / 0.901
- 30d: 1: 0.362 / 0.527 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.502 / 0.900; 6: 0.348 / 0.499 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.501 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.078 (body 0.059, range 0.096); 'price stays where it was' would score 0.110; colour right 0.517; typical miss of the close 5.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.128 (body 0.092, range 0.165); 'price stays where it was' would score 0.122; colour right 0.531; typical miss of the close 5.5 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.126 (body 0.084, range 0.169); 'price stays where it was' would score 0.129; colour right 0.528; typical miss of the close 9.8 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.170); 'price stays where it was' would score 0.135; colour right 0.499; typical miss of the close 9.2 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.164); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 7.9 bp; chain ended on the right side 0.521 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.0; 2: 0.200 / 4.7; 3: 0.169 / 6.2; 4: 0.132 / 6.6; 5: 0.126 / 7.3; 6: 0.113 / 7.8; 7: 0.111 / 8.1; 8: 0.098 / 8.7; 9: 0.088 / 8.8; 10: 0.088 / 9.3; 11: 0.086 / 9.8; 12: 0.076 / 10.2; 13: 0.069 / 10.3; 14: 0.070 / 10.7; 15: 0.062 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 128293, probability skill vs chance 0.2349, widened contest next: False
  - now: threshold 0.8335, hit rate recent 0.9555 / long run 0.9439
    - 6h: 15 calls (61 a day), hit rate 1.000, chance 0.296, naive rule 0.496, lift 3.38x
    - 24h: 53 calls (53 a day), hit rate 0.962, chance 0.297, naive rule 0.519, lift 3.24x
    - 7d: 395 calls (56 a day), hit rate 0.949, chance 0.294, naive rule 0.498, lift 3.23x
    - 30d: 1723 calls (57 a day), hit rate 0.937, chance 0.294, naive rule 0.493, lift 3.19x
  - next: threshold 0.5291, hit rate recent 0.5948 / long run 0.5897
    - 6h: 43 calls (174 a day), hit rate 0.605, chance 0.296, lift 2.04x
    - 24h: 141 calls (141 a day), hit rate 0.603, chance 0.297, lift 2.03x
    - 7d: 752 calls (107 a day), hit rate 0.590, chance 0.294, lift 2.01x
    - 30d: 2956 calls (99 a day), hit rate 0.582, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.496; 0.35: 536, 0.521; 0.40: 475, 0.578; 0.45: 406, 0.650; 0.50: 356, 0.700; 0.55: 310, 0.742; 0.60: 262, 0.788; 0.65: 220, 0.813; 0.70: 173, 0.845; 0.75: 136, 0.879; 0.80: 91, 0.915; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.464; 0.40: 407, 0.497; 0.45: 310, 0.532; 0.50: 199, 0.569; 0.55: 88, 0.570; 0.60: 13, 0.643; 0.65: 1, 0.630
- **K=5**: model 1792540800, labels learned 128291, probability skill vs chance 0.2321, widened contest next: False
  - now: threshold 0.6779, hit rate recent 0.8408 / long run 0.8261
    - 6h: 15 calls (61 a day), hit rate 1.000, chance 0.195, naive rule 0.422, lift 5.12x
    - 24h: 46 calls (46 a day), hit rate 0.848, chance 0.193, naive rule 0.437, lift 4.39x
    - 7d: 403 calls (58 a day), hit rate 0.826, chance 0.185, naive rule 0.410, lift 4.46x
    - 30d: 1616 calls (54 a day), hit rate 0.825, chance 0.188, naive rule 0.404, lift 4.39x
  - next: threshold 0.4553, hit rate recent 0.5757 / long run 0.5
    - 6h: 16 calls (65 a day), hit rate 0.750, chance 0.195, lift 3.84x
    - 24h: 48 calls (48 a day), hit rate 0.583, chance 0.193, lift 3.02x
    - 7d: 564 calls (81 a day), hit rate 0.520, chance 0.185, lift 2.80x
    - 30d: 3017 calls (101 a day), hit rate 0.472, chance 0.188, lift 2.51x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.493; 0.40: 279, 0.566; 0.45: 227, 0.620; 0.50: 180, 0.668; 0.55: 141, 0.707; 0.60: 108, 0.753; 0.65: 76, 0.790; 0.70: 50, 0.829; 0.75: 29, 0.873; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.389; 0.35: 255, 0.421; 0.40: 159, 0.458; 0.45: 68, 0.478; 0.50: 13, 0.495; 0.55: 1, 0.486
- **K=8**: model 1793059200, labels learned 128288, probability skill vs chance 0.2142, widened contest next: False
  - now: threshold 0.5643, hit rate recent 0.7139 / long run 0.6899
    - 6h: 14 calls (58 a day), hit rate 0.857, chance 0.143, naive rule 0.393, lift 6.00x
    - 24h: 48 calls (48 a day), hit rate 0.688, chance 0.131, naive rule 0.384, lift 5.23x
    - 7d: 380 calls (54 a day), hit rate 0.692, chance 0.123, naive rule 0.347, lift 5.65x
    - 30d: 1574 calls (52 a day), hit rate 0.691, chance 0.121, naive rule 0.335, lift 5.69x
  - next: threshold 0.3447, hit rate recent 0.4737 / long run 0.3993
    - 6h: 34 calls (140 a day), hit rate 0.529, chance 0.143, lift 3.71x
    - 24h: 113 calls (114 a day), hit rate 0.460, chance 0.131, lift 3.50x
    - 7d: 716 calls (102 a day), hit rate 0.405, chance 0.123, lift 3.31x
    - 30d: 2816 calls (94 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 189, 0.500; 0.40: 147, 0.548; 0.45: 112, 0.595; 0.50: 84, 0.639; 0.55: 61, 0.678; 0.60: 40, 0.714; 0.65: 23, 0.780; 0.70: 11, 0.813; 0.75: 2, 0.750
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.360; 0.35: 92, 0.387; 0.40: 29, 0.409; 0.45: 6, 0.434; 0.50: 1, 0.621
- **K=13**: model 1793059200, labels learned 128283, probability skill vs chance 0.2008, widened contest next: False
  - now: threshold 0.4116, hit rate recent 0.6468 / long run 0.5685
    - 6h: 15 calls (63 a day), hit rate 0.867, chance 0.087, naive rule 0.315, lift 9.97x
    - 24h: 57 calls (58 a day), hit rate 0.667, chance 0.081, naive rule 0.317, lift 8.26x
    - 7d: 423 calls (61 a day), hit rate 0.574, chance 0.077, naive rule 0.287, lift 7.46x
    - 30d: 1654 calls (55 a day), hit rate 0.570, chance 0.077, naive rule 0.278, lift 7.37x
  - next: threshold 0.2931, hit rate recent 0.3718 / long run 0.3199
    - 6h: 15 calls (63 a day), hit rate 0.600, chance 0.087, lift 6.90x
    - 24h: 60 calls (61 a day), hit rate 0.383, chance 0.081, lift 4.75x
    - 7d: 393 calls (56 a day), hit rate 0.336, chance 0.077, lift 4.36x
    - 30d: 1988 calls (66 a day), hit rate 0.317, chance 0.077, lift 4.11x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 126, 0.443; 0.35: 90, 0.496; 0.40: 64, 0.553; 0.45: 43, 0.602; 0.50: 28, 0.658; 0.55: 17, 0.700; 0.60: 8, 0.740; 0.65: 2, 0.736; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.328; 0.35: 14, 0.353; 0.40: 3, 0.438; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.431 | 19.07% | 0.867 | 0.550 | 0.246 | 0.583 | 0.014 |
| 6h | 8.802 | 15.66% | 0.900 | 0.503 | 0.250 | 0.517 | 0.284 |
| 24h | 17.471 | 5.72% | 0.903 | 0.491 | 0.251 | 0.496 | 0.718 |
| 7d | 16.536 | 4.80% | 0.900 | 0.500 | 0.251 | 0.499 | 0.731 |
| 30d | 14.279 | 4.37% | 0.900 | 0.500 | 0.251 | 0.496 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.182 | 7.405 | 7.671 | 7.660 | 7.523 | 7.779 | 7.481 | 7.404 | 7.440 | 7.431 |
| 6h | 10.436 | 8.821 | 8.997 | 8.849 | 8.935 | 9.038 | 8.816 | 8.777 | 8.786 | 8.802 |
| 24h | 18.531 | 17.597 | 17.616 | 17.470 | 17.760 | 17.746 | 17.439 | 17.421 | 17.433 | 17.471 |
| 7d | 17.369 | 16.737 | 16.647 | 16.574 | 16.871 | 16.780 | 16.524 | 16.491 | 16.505 | 16.536 |
| 30d | 14.931 | 14.430 | 14.371 | 14.305 | 14.545 | 14.482 | 14.273 | 14.251 | 14.253 | 14.279 |

## Next candle

- candle starting 2026-10-31 06:19 UTC, last close 2240.06
- P(up) 0.5381, return quantiles (bp): {'05': -4.305, '10': -3.393, '25': -1.378, '40': -0.348, '50': 0.207, '60': 0.758, '75': 1.698, '90': 2.953, '95': 3.98}
- changepoint probability 0.0161, regime age 410.2 min
- agent weights: empirical 0.003, ewma 0.135, garch 0.077, har 0.179, bocpd 0.059, hmm 0.041, online_qr 0.232, lgbm 0.275

## Learning log

- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- 2026-10-30 00:00 UTC: {"garch": {"alpha": 0.1133, "beta": 0.8586}, "hmm": {"sd_bp": [3.9, 7.28, 18.78], "stay": [0.971, 0.949, 0.901]}, "lgbm": {"challenger_loss": 0.25405, "champion_loss": 0.25401, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47823, "challengers": 1, "chance_loss": 0.60191, "widened": false, "champion_loss": 0.47515, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36645, "challengers": 1, "chance_loss": 0.48258, "widened": false, "champion_loss": 0.36419, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27973, "challengers": 1, "chance_loss": 0.3791, "widened": false, "champion_loss": 0.27864, "promoted": false}, "reversal_k13": {"challenger_loss": 0.206, "challengers": 1, "chance_loss": 0.28151, "widened": false, "champion_loss": 0.20501, "promoted": false}}
- 2026-10-30 12:00 UTC: {"garch": {"alpha": 0.1079, "beta": 0.8723}, "hmm": {"sd_bp": [3.95, 7.23, 20.79], "stay": [0.971, 0.948, 0.921]}}
- 2026-10-31 00:00 UTC: {"garch": {"alpha": 0.0992, "beta": 0.8845}, "hmm": {"sd_bp": [3.94, 7.31, 20.82], "stay": [0.972, 0.947, 0.905]}, "lgbm": {"challenger_loss": 0.25174, "champion_loss": 0.25184, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4707, "challengers": 1, "chance_loss": 0.6032, "widened": false, "champion_loss": 0.46768, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3626, "challengers": 1, "chance_loss": 0.48093, "widened": false, "champion_loss": 0.362, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27899, "challengers": 1, "chance_loss": 0.37599, "widened": false, "champion_loss": 0.27843, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19949, "challengers": 1, "chance_loss": 0.27503, "widened": false, "champion_loss": 0.19894, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.94, 7.31, 20.82], current probabilities: [0.964, 0.036, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-31 06:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.417, 'l_abs': 0.634, 'l_hi': 0.748, 'l_lo': 0.728, 'b05': 0.713, 'b25': 0.664, 'b75': 0.604, 'b95': 0.703}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.898, 2.193, 1.88, 1.794, 1.97, 2.175, 2.238, 2.427, 2.668, 2.804, 2.876, 3.06, 2.766, 2.649]}
- calibration offsets (in sigma): {'05': 0.029, '10': -0.042, '25': 0.065, '40': 0.072, '50': 0.06, '60': 0.048, '75': 0.025, '90': -0.098, '95': -0.129}
