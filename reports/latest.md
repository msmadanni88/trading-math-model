# ETH-USD 60s candle generator - report

- generated: 2026-10-04 17:45 UTC
- last closed candle: 2026-10-04 17:45 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k13_next 0.276 in the last 7 days, -0.063 against the 7 before
- WIN RATE FALLING: reversal_k5_next 0.451 in the last 7 days, -0.094 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.380 in the last 7 days, -0.071 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.521 (670) [0.491, 0.551] | 0.510 (2876) [0.491, 0.528] | 0.512 (3068) [0.495, 0.530] | 0.531 (96) | 0.676 (71) | 0.500 | flat -0.024 (noise 0.030) |
| colour_clear | 0.546 (721) | 0.501 (5394) [0.487, 0.516] | 0.499 (23299) [0.494, 0.504] | 0.498 (24959) [0.493, 0.503] | 0.546 (721) | 0.554 (471) | 0.500 | flat +0.001 (noise 0.010) |
| colour_confident | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.612 (209) | 0.500 | - |
| colour_next | 0.521 (1404) | 0.507 (10003) [0.501, 0.512] | 0.502 (42884) [0.498, 0.505] | 0.501 (45753) [0.497, 0.505] | 0.521 (1404) | 0.541 (1047) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.493 (19656) | 0.501 (140042) [0.498, 0.504] | 0.501 (600376) [0.500, 0.502] | 0.500 (640542) [0.499, 0.502] | 0.493 (19656) | 0.502 (14658) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.605 (76) | 0.500 | - |
| reversal_k13_next | 0.324 (102) | 0.276 (635) [0.256, 0.295] | 0.307 (1993) [0.292, 0.323] | 0.301 (2207) [0.287, 0.318] | 0.324 (102) | 0.328 (61) | 0.076 | down -0.063 (noise 0.031) |
| reversal_k13_now | 0.756 (45) | 0.594 (342) [0.539, 0.654] | 0.588 (1428) [0.566, 0.613] | 0.586 (1517) [0.564, 0.608] | 0.756 (45) | 0.596 (47) | 0.076 | flat -0.026 (noise 0.040) |
| reversal_k3_next | 0.535 (144) | 0.578 (689) [0.549, 0.610] | 0.584 (2430) [0.568, 0.599] | 0.584 (2584) [0.570, 0.599] | 0.535 (144) | 0.589 (90) | 0.292 | flat +0.006 (noise 0.031) |
| reversal_k3_now | 0.930 (57) | 0.946 (388) [0.936, 0.958] | 0.942 (1710) [0.933, 0.950] | 0.941 (1820) [0.933, 0.949] | 0.930 (57) | 0.954 (43) | 0.292 | flat +0.003 (noise 0.016) |
| reversal_k5_next | 0.407 (189) | 0.451 (658) [0.418, 0.484] | 0.486 (2076) [0.466, 0.506] | 0.486 (2179) [0.469, 0.506] | 0.407 (189) | 0.456 (90) | 0.187 | down -0.094 (noise 0.034) |
| reversal_k5_now | 0.820 (61) | 0.858 (366) [0.838, 0.886] | 0.836 (1587) [0.821, 0.851] | 0.837 (1672) [0.823, 0.851] | 0.820 (61) | 0.938 (48) | 0.187 | flat +0.041 (noise 0.027) |
| reversal_k8_next | 0.377 (77) | 0.380 (418) [0.355, 0.406] | 0.400 (2018) [0.382, 0.419] | 0.395 (2183) [0.379, 0.414] | 0.377 (77) | 0.426 (61) | 0.121 | down -0.071 (noise 0.035) |
| reversal_k8_now | 0.780 (50) | 0.735 (325) [0.700, 0.772] | 0.718 (1551) [0.698, 0.738] | 0.716 (1637) [0.697, 0.736] | 0.780 (50) | 0.821 (39) | 0.121 | flat -0.013 (noise 0.033) |
| overall | 0.496 (21881) | 0.503 (154536) [0.500, 0.506] | 0.503 (660929) [0.502, 0.504] | 0.502 (705162) [0.501, 0.504] | 0.496 (21881) | 0.508 (16255) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07527, 0.1121] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5311, 'levels': [{'threshold': 0.07527, 'calls_per_day': 145.8, 'win_rate': 0.5574}, {'threshold': 0.1121, 'calls_per_day': 36.7, 'win_rate': 0.6216}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 1319, 'rate': 0.5474}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15235 | 0.331 | 0.508 (15007) | 0.611 (293) | 0.782 (2388) |
| volatility: normal | 15235 | 0.360 | 0.507 (15169) | - | 0.776 (2125) |
| volatility: wild | 15235 | 0.373 | 0.491 (15191) | - | 0.778 (2130) |
| session: Asia 00-08 | 15360 | 0.350 | 0.500 (15249) | 0.635 (115) | 0.784 (2200) |
| session: Europe 08-13 | 9600 | 0.348 | 0.505 (9531) | 0.562 (64) | 0.768 (1459) |
| session: US 13-21 | 15165 | 0.364 | 0.502 (15068) | 0.611 (72) | 0.784 (2239) |
| session: late 21-24 | 5580 | 0.351 | 0.503 (5519) | 0.619 (42) | 0.770 (745) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.378 | 0.342 | 0.265 | 0.265 | 0.610 | 0.274 | 0.482 | 1.501 |
| 6h | 360 | 0.323 | 0.319 | 0.239 | 0.251 | 0.558 | 0.245 | 0.401 | 1.274 |
| 24h | 1440 | 0.307 | 0.298 | 0.228 | 0.237 | 0.551 | 0.234 | 0.379 | 1.368 |
| 7d | 10080 | 0.353 | 0.353 | 0.281 | 0.306 | 0.509 | 0.241 | 0.466 | 1.398 |
| 30d | 43200 | 0.354 | 0.354 | 0.277 | 0.307 | 0.503 | 0.245 | 0.463 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.378 / 0.610 / 0.883; 2: 0.358 / 0.525 / 0.950; 3: 0.362 / 0.559 / 0.967; 4: 0.337 / 0.508 / 0.967; 5: 0.337 / 0.475 / 0.983; 6: 0.364 / 0.593 / 0.983; 7: 0.332 / 0.458 / 1.000; 8: 0.339 / 0.390 / 1.000; 9: 0.357 / 0.559 / 1.000; 10: 0.360 / 0.593 / 1.000; 11: 0.332 / 0.475 / 1.000; 12: 0.349 / 0.593 / 1.000; 13: 0.356 / 0.542 / 1.000; 14: 0.353 / 0.542 / 1.000; 15: 0.355 / 0.559 / 1.000
- 6h: 1: 0.323 / 0.558 / 0.875; 2: 0.307 / 0.493 / 0.906; 3: 0.311 / 0.527 / 0.914; 4: 0.310 / 0.547 / 0.911; 5: 0.301 / 0.476 / 0.931; 6: 0.308 / 0.533 / 0.942; 7: 0.302 / 0.473 / 0.931; 8: 0.309 / 0.484 / 0.931; 9: 0.307 / 0.530 / 0.922; 10: 0.313 / 0.541 / 0.939; 11: 0.309 / 0.513 / 0.936; 12: 0.317 / 0.584 / 0.931; 13: 0.302 / 0.527 / 0.931; 14: 0.298 / 0.493 / 0.936; 15: 0.308 / 0.527 / 0.936
- 24h: 1: 0.307 / 0.551 / 0.873; 2: 0.290 / 0.511 / 0.902; 3: 0.293 / 0.521 / 0.903; 4: 0.284 / 0.502 / 0.904; 5: 0.282 / 0.474 / 0.906; 6: 0.284 / 0.488 / 0.910; 7: 0.282 / 0.498 / 0.909; 8: 0.287 / 0.486 / 0.910; 9: 0.282 / 0.485 / 0.906; 10: 0.289 / 0.510 / 0.908; 11: 0.288 / 0.499 / 0.909; 12: 0.290 / 0.535 / 0.903; 13: 0.286 / 0.496 / 0.907; 14: 0.286 / 0.497 / 0.908; 15: 0.283 / 0.482 / 0.908
- 7d: 1: 0.353 / 0.509 / 0.896; 2: 0.348 / 0.493 / 0.900; 3: 0.351 / 0.512 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.347 / 0.506 / 0.900; 6: 0.345 / 0.498 / 0.900; 7: 0.345 / 0.501 / 0.900; 8: 0.345 / 0.503 / 0.900; 9: 0.342 / 0.492 / 0.900; 10: 0.344 / 0.507 / 0.900; 11: 0.345 / 0.505 / 0.899; 12: 0.346 / 0.514 / 0.899; 13: 0.345 / 0.500 / 0.898; 14: 0.343 / 0.495 / 0.899; 15: 0.342 / 0.497 / 0.900
- 30d: 1: 0.354 / 0.503 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.506 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.348 / 0.504 / 0.900; 7: 0.348 / 0.506 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.499 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.503 / 0.900; 12: 0.345 / 0.501 / 0.900; 13: 0.345 / 0.500 / 0.900; 14: 0.344 / 0.495 / 0.900; 15: 0.343 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.164 (body 0.111, range 0.216); 'price stays where it was' would score 0.150; colour right 0.559; typical miss of the close 1.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.120 (body 0.085, range 0.154); 'price stays where it was' would score 0.105; colour right 0.524; typical miss of the close 3.3 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.114 (body 0.082, range 0.146); 'price stays where it was' would score 0.111; colour right 0.500; typical miss of the close 3.0 bp; chain ended on the right side 0.615 of 96 chains; n=1440
- 7d: match 0.118 (body 0.077, range 0.159); 'price stays where it was' would score 0.118; colour right 0.493; typical miss of the close 7.2 bp; chain ended on the right side 0.530 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.513 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.2; 2: 0.197 / 4.3; 3: 0.169 / 6.0; 4: 0.133 / 6.4; 5: 0.122 / 7.2; 6: 0.112 / 8.0; 7: 0.099 / 8.4; 8: 0.092 / 8.7; 9: 0.089 / 9.0; 10: 0.083 / 9.8; 11: 0.076 / 10.3; 12: 0.075 / 10.7; 13: 0.068 / 11.0; 14: 0.068 / 11.1; 15: 0.063 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 90099, probability skill vs chance 0.2232, widened contest next: False
  - now: threshold 0.8399, hit rate recent 0.9395 / long run 0.9414
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.252, naive rule 0.419, lift 3.97x
    - 24h: 59 calls (59 a day), hit rate 0.949, chance 0.293, naive rule 0.491, lift 3.24x
    - 7d: 394 calls (56 a day), hit rate 0.947, chance 0.286, naive rule 0.480, lift 3.31x
    - 30d: 1707 calls (57 a day), hit rate 0.943, chance 0.292, naive rule 0.482, lift 3.23x
  - next: threshold 0.5294, hit rate recent 0.5815 / long run 0.5768
    - 6h: 43 calls (174 a day), hit rate 0.628, chance 0.252, lift 2.49x
    - 24h: 130 calls (130 a day), hit rate 0.600, chance 0.293, lift 2.05x
    - 7d: 701 calls (100 a day), hit rate 0.579, chance 0.286, lift 2.02x
    - 30d: 2470 calls (82 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.518; 0.40: 489, 0.560; 0.45: 421, 0.626; 0.50: 368, 0.681; 0.55: 321, 0.725; 0.60: 274, 0.767; 0.65: 224, 0.803; 0.70: 182, 0.835; 0.75: 140, 0.870; 0.80: 99, 0.909; 0.85: 49, 0.951; 0.90: 1, 0.974
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 497, 0.459; 0.40: 414, 0.487; 0.45: 318, 0.518; 0.50: 210, 0.550; 0.55: 95, 0.586; 0.60: 13, 0.609; 0.65: 0, 0.714
- **K=5**: model 1790208000, labels learned 90097, probability skill vs chance 0.2209, widened contest next: False
  - now: threshold 0.7106, hit rate recent 0.8861 / long run 0.8463
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.170, naive rule 0.330, lift 5.56x
    - 24h: 64 calls (64 a day), hit rate 0.906, chance 0.179, naive rule 0.377, lift 5.05x
    - 7d: 379 calls (54 a day), hit rate 0.858, chance 0.185, naive rule 0.389, lift 4.63x
    - 30d: 1592 calls (53 a day), hit rate 0.839, chance 0.186, naive rule 0.390, lift 4.51x
  - next: threshold 0.4426, hit rate recent 0.4424 / long run 0.468
    - 6h: 38 calls (155 a day), hit rate 0.500, chance 0.170, lift 2.94x
    - 24h: 140 calls (141 a day), hit rate 0.457, chance 0.179, lift 2.55x
    - 7d: 721 calls (103 a day), hit rate 0.451, chance 0.185, lift 2.43x
    - 30d: 2127 calls (71 a day), hit rate 0.485, chance 0.186, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 433, 0.410; 0.35: 373, 0.462; 0.40: 301, 0.531; 0.45: 246, 0.588; 0.50: 192, 0.649; 0.55: 147, 0.698; 0.60: 115, 0.740; 0.65: 88, 0.784; 0.70: 65, 0.822; 0.75: 35, 0.861; 0.80: 9, 0.883
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.385; 0.35: 255, 0.422; 0.40: 169, 0.447; 0.45: 89, 0.471; 0.50: 22, 0.513; 0.55: 3, 0.570
- **K=8**: model 1791072000, labels learned 90094, probability skill vs chance 0.2066, widened contest next: False
  - now: threshold 0.5605, hit rate recent 0.7846 / long run 0.7339
    - 6h: 16 calls (66 a day), hit rate 0.875, chance 0.121, naive rule 0.272, lift 7.21x
    - 24h: 53 calls (53 a day), hit rate 0.792, chance 0.128, naive rule 0.324, lift 6.19x
    - 7d: 320 calls (46 a day), hit rate 0.734, chance 0.123, naive rule 0.328, lift 5.96x
    - 30d: 1545 calls (52 a day), hit rate 0.724, chance 0.122, naive rule 0.327, lift 5.95x
  - next: threshold 0.3669, hit rate recent 0.4073 / long run 0.405
    - 6h: 27 calls (111 a day), hit rate 0.444, chance 0.121, lift 3.66x
    - 24h: 78 calls (79 a day), hit rate 0.423, chance 0.128, lift 3.31x
    - 7d: 433 calls (62 a day), hit rate 0.383, chance 0.123, lift 3.11x
    - 30d: 2018 calls (67 a day), hit rate 0.402, chance 0.122, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 277, 0.398; 0.35: 208, 0.474; 0.40: 161, 0.538; 0.45: 127, 0.587; 0.50: 97, 0.628; 0.55: 68, 0.682; 0.60: 46, 0.731; 0.65: 25, 0.767; 0.70: 9, 0.807; 0.75: 1, 0.812
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 190, 0.344; 0.35: 119, 0.382; 0.40: 49, 0.408; 0.45: 10, 0.417; 0.50: 1, 0.410
- **K=13**: model 1791072000, labels learned 90089, probability skill vs chance 0.193, widened contest next: False
  - now: threshold 0.4078, hit rate recent 0.6396 / long run 0.5958
    - 6h: 18 calls (75 a day), hit rate 0.667, chance 0.088, naive rule 0.262, lift 7.54x
    - 24h: 60 calls (61 a day), hit rate 0.633, chance 0.080, naive rule 0.252, lift 7.95x
    - 7d: 350 calls (50 a day), hit rate 0.586, chance 0.078, naive rule 0.264, lift 7.50x
    - 30d: 1440 calls (48 a day), hit rate 0.590, chance 0.077, naive rule 0.266, lift 7.70x
  - next: threshold 0.2682, hit rate recent 0.3403 / long run 0.3002
    - 6h: 25 calls (104 a day), hit rate 0.440, chance 0.088, lift 4.98x
    - 24h: 87 calls (88 a day), hit rate 0.322, chance 0.080, lift 4.04x
    - 7d: 655 calls (94 a day), hit rate 0.284, chance 0.078, lift 3.63x
    - 30d: 1999 calls (67 a day), hit rate 0.307, chance 0.077, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.436; 0.35: 90, 0.492; 0.40: 65, 0.540; 0.45: 45, 0.602; 0.50: 29, 0.622; 0.55: 16, 0.666; 0.60: 7, 0.686; 0.65: 2, 0.774; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.313; 0.35: 18, 0.344; 0.40: 4, 0.333; 0.45: 1, 0.435

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.492 | 1.19% | 0.900 | 0.483 | 0.252 | 0.458 | 0.292 |
| 6h | 6.133 | 1.43% | 0.883 | 0.456 | 0.250 | 0.535 | 0.323 |
| 24h | 5.364 | 2.26% | 0.889 | 0.500 | 0.251 | 0.498 | 0.409 |
| 7d | 12.459 | 4.13% | 0.899 | 0.500 | 0.251 | 0.496 | 0.693 |
| 30d | 14.034 | 4.20% | 0.899 | 0.500 | 0.251 | 0.499 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.558 | 5.536 | 5.557 | 5.491 | 5.648 | 5.631 | 5.481 | 5.419 | 5.465 | 5.492 |
| 6h | 6.222 | 6.169 | 6.186 | 6.156 | 6.247 | 6.294 | 6.121 | 6.103 | 6.116 | 6.133 |
| 24h | 5.488 | 5.426 | 5.415 | 5.381 | 5.559 | 5.659 | 5.363 | 5.356 | 5.360 | 5.364 |
| 7d | 12.997 | 12.560 | 12.541 | 12.469 | 12.707 | 12.639 | 12.450 | 12.449 | 12.437 | 12.459 |
| 30d | 14.650 | 14.164 | 14.123 | 14.061 | 14.306 | 14.257 | 14.038 | 14.008 | 14.008 | 14.034 |

## Next candle

- candle starting 2026-10-04 17:45 UTC, last close 2704.69
- P(up) 0.506, return quantiles (bp): {'05': -5.0, '10': -3.637, '25': -1.751, '40': -0.543, '50': 0.034, '60': 0.607, '75': 1.625, '90': 3.544, '95': 5.523}
- changepoint probability 0.8332, regime age 22.5 min
- agent weights: empirical 0.021, ewma 0.091, garch 0.090, har 0.178, bocpd 0.014, hmm 0.007, online_qr 0.265, lgbm 0.334

## Learning log

- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- HMM volatility states (sd, bp per minute): [1.75, 4.62, 12.53], current probabilities: [0.001, 0.957, 0.043]
- live generator: {'versions': 60, 'latest_effective': '2026-10-04 17:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.249, 'l_abs': 0.688, 'l_hi': 0.755, 'l_lo': 0.717, 'b05': 0.679, 'b25': 0.685, 'b75': 0.549, 'b95': 0.599}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.446, 1.81, 2.18, 2.346, 2.575, 2.625, 2.812, 3.437, 3.419, 3.665, 4.325, 4.082, 3.84, 3.983]}
- calibration offsets (in sigma): {'05': -0.048, '10': 0.024, '25': 0.04, '40': 0.036, '50': 0.01, '60': 0.024, '75': -0.01, '90': 0.006, '95': 0.108}
