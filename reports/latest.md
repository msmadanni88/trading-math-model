# ETH-USD 60s candle generator - report

- generated: 2026-10-04 13:23 UTC
- last closed candle: 2026-10-04 13:22 UTC (staleness 1.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k13_next 0.276 in the last 7 days, -0.063 against the 7 before
- WIN RATE FALLING: reversal_k5_next 0.451 in the last 7 days, -0.094 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.380 in the last 7 days, -0.071 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.521 (670) [0.491, 0.551] | 0.510 (2876) [0.491, 0.528] | 0.512 (3068) [0.495, 0.530] | 0.531 (96) | 0.679 (53) | 0.500 | flat -0.024 (noise 0.030) |
| colour_clear | 0.546 (721) | 0.501 (5394) [0.487, 0.516] | 0.499 (23299) [0.494, 0.504] | 0.498 (24959) [0.493, 0.503] | 0.546 (721) | 0.562 (340) | 0.500 | flat +0.001 (noise 0.010) |
| colour_confident | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.629 (167) | 0.500 | - |
| colour_next | 0.521 (1404) | 0.507 (10003) [0.501, 0.512] | 0.502 (42884) [0.498, 0.505] | 0.501 (45753) [0.497, 0.505] | 0.521 (1404) | 0.534 (789) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.493 (19656) | 0.501 (140042) [0.498, 0.504] | 0.501 (600376) [0.500, 0.502] | 0.500 (640542) [0.499, 0.502] | 0.493 (19656) | 0.495 (11046) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.594 (64) | 0.500 | - |
| reversal_k13_next | 0.324 (102) | 0.276 (635) [0.256, 0.295] | 0.307 (1993) [0.292, 0.323] | 0.301 (2207) [0.287, 0.318] | 0.324 (102) | 0.244 (41) | 0.076 | down -0.063 (noise 0.031) |
| reversal_k13_now | 0.756 (45) | 0.594 (342) [0.539, 0.654] | 0.588 (1428) [0.566, 0.613] | 0.586 (1517) [0.564, 0.608] | 0.756 (45) | 0.571 (35) | 0.076 | flat -0.026 (noise 0.040) |
| reversal_k3_next | 0.535 (144) | 0.578 (689) [0.549, 0.610] | 0.584 (2430) [0.568, 0.599] | 0.584 (2584) [0.570, 0.599] | 0.535 (144) | 0.582 (55) | 0.292 | flat +0.006 (noise 0.031) |
| reversal_k3_now | 0.930 (57) | 0.946 (388) [0.936, 0.958] | 0.942 (1710) [0.933, 0.950] | 0.941 (1820) [0.933, 0.949] | 0.930 (57) | 0.935 (31) | 0.292 | flat +0.003 (noise 0.016) |
| reversal_k5_next | 0.407 (189) | 0.451 (658) [0.418, 0.484] | 0.486 (2076) [0.466, 0.506] | 0.486 (2179) [0.469, 0.506] | 0.407 (189) | 0.435 (62) | 0.187 | down -0.094 (noise 0.034) |
| reversal_k5_now | 0.820 (61) | 0.858 (366) [0.838, 0.886] | 0.836 (1587) [0.821, 0.851] | 0.837 (1672) [0.823, 0.851] | 0.820 (61) | 0.917 (36) | 0.187 | flat +0.041 (noise 0.027) |
| reversal_k8_next | 0.377 (77) | 0.380 (418) [0.355, 0.406] | 0.400 (2018) [0.382, 0.419] | 0.395 (2183) [0.379, 0.414] | 0.377 (77) | 0.425 (40) | 0.121 | down -0.071 (noise 0.035) |
| reversal_k8_now | 0.780 (50) | 0.735 (325) [0.700, 0.772] | 0.718 (1551) [0.698, 0.738] | 0.716 (1637) [0.697, 0.736] | 0.780 (50) | 0.786 (28) | 0.121 | flat -0.013 (noise 0.033) |
| overall | 0.496 (21881) | 0.503 (154536) [0.500, 0.506] | 0.503 (660929) [0.502, 0.504] | 0.502 (705162) [0.501, 0.504] | 0.496 (21881) | 0.501 (12216) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07527, 0.1121] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5311, 'levels': [{'threshold': 0.07527, 'calls_per_day': 145.8, 'win_rate': 0.5574}, {'threshold': 0.1121, 'calls_per_day': 36.7, 'win_rate': 0.6216}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 1061, 'rate': 0.5429}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15148 | 0.332 | 0.507 (14925) | 0.622 (251) | 0.781 (2356) |
| volatility: normal | 15147 | 0.360 | 0.507 (15081) | - | 0.775 (2116) |
| volatility: wild | 15147 | 0.373 | 0.492 (15103) | - | 0.778 (2124) |
| session: Asia 00-08 | 15360 | 0.350 | 0.500 (15249) | 0.635 (115) | 0.784 (2200) |
| session: Europe 08-13 | 9600 | 0.348 | 0.505 (9531) | 0.562 (64) | 0.768 (1459) |
| session: US 13-21 | 14902 | 0.365 | 0.501 (14810) | 0.700 (30) | 0.782 (2192) |
| session: late 21-24 | 5580 | 0.351 | 0.503 (5519) | 0.619 (42) | 0.770 (745) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.321 | 0.325 | 0.233 | 0.233 | 0.492 | 0.229 | 0.414 | 1.048 |
| 6h | 360 | 0.294 | 0.289 | 0.234 | 0.233 | 0.511 | 0.210 | 0.378 | 1.368 |
| 24h | 1440 | 0.306 | 0.298 | 0.228 | 0.234 | 0.545 | 0.231 | 0.381 | 1.407 |
| 7d | 10080 | 0.355 | 0.354 | 0.283 | 0.308 | 0.508 | 0.241 | 0.468 | 1.395 |
| 30d | 43200 | 0.354 | 0.354 | 0.277 | 0.307 | 0.502 | 0.245 | 0.464 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.321 / 0.492 / 0.900; 2: 0.299 / 0.508 / 0.900; 3: 0.301 / 0.424 / 0.900; 4: 0.324 / 0.593 / 0.883; 5: 0.288 / 0.424 / 0.850; 6: 0.300 / 0.492 / 0.850; 7: 0.333 / 0.542 / 0.800; 8: 0.345 / 0.458 / 0.783; 9: 0.311 / 0.508 / 0.733; 10: 0.304 / 0.475 / 0.767; 11: 0.305 / 0.475 / 0.733; 12: 0.348 / 0.627 / 0.650; 13: 0.306 / 0.508 / 0.633; 14: 0.322 / 0.492 / 0.717; 15: 0.344 / 0.610 / 0.733
- 6h: 1: 0.294 / 0.511 / 0.869; 2: 0.281 / 0.500 / 0.897; 3: 0.284 / 0.497 / 0.886; 4: 0.276 / 0.472 / 0.853; 5: 0.278 / 0.497 / 0.847; 6: 0.270 / 0.466 / 0.839; 7: 0.282 / 0.514 / 0.858; 8: 0.288 / 0.514 / 0.864; 9: 0.269 / 0.460 / 0.842; 10: 0.271 / 0.449 / 0.844; 11: 0.281 / 0.489 / 0.850; 12: 0.280 / 0.531 / 0.800; 13: 0.280 / 0.520 / 0.806; 14: 0.274 / 0.486 / 0.836; 15: 0.286 / 0.523 / 0.822
- 24h: 1: 0.306 / 0.545 / 0.872; 2: 0.288 / 0.505 / 0.897; 3: 0.292 / 0.518 / 0.897; 4: 0.286 / 0.507 / 0.893; 5: 0.285 / 0.482 / 0.889; 6: 0.283 / 0.478 / 0.893; 7: 0.283 / 0.498 / 0.894; 8: 0.287 / 0.481 / 0.894; 9: 0.282 / 0.474 / 0.890; 10: 0.289 / 0.506 / 0.890; 11: 0.287 / 0.504 / 0.887; 12: 0.287 / 0.520 / 0.875; 13: 0.289 / 0.496 / 0.874; 14: 0.288 / 0.490 / 0.878; 15: 0.284 / 0.474 / 0.881
- 7d: 1: 0.355 / 0.508 / 0.897; 2: 0.349 / 0.492 / 0.900; 3: 0.352 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.348 / 0.506 / 0.899; 6: 0.346 / 0.497 / 0.899; 7: 0.347 / 0.502 / 0.899; 8: 0.346 / 0.503 / 0.899; 9: 0.343 / 0.491 / 0.898; 10: 0.345 / 0.504 / 0.898; 11: 0.346 / 0.505 / 0.898; 12: 0.347 / 0.510 / 0.897; 13: 0.346 / 0.500 / 0.897; 14: 0.344 / 0.496 / 0.898; 15: 0.344 / 0.495 / 0.899
- 30d: 1: 0.354 / 0.502 / 0.898; 2: 0.351 / 0.497 / 0.900; 3: 0.352 / 0.506 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.349 / 0.503 / 0.899; 7: 0.348 / 0.506 / 0.899; 8: 0.347 / 0.503 / 0.899; 9: 0.345 / 0.498 / 0.899; 10: 0.347 / 0.503 / 0.899; 11: 0.346 / 0.503 / 0.899; 12: 0.345 / 0.501 / 0.899; 13: 0.345 / 0.500 / 0.899; 14: 0.344 / 0.495 / 0.899; 15: 0.343 / 0.495 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.174 (body 0.137, range 0.211); 'price stays where it was' would score 0.134; colour right 0.424; typical miss of the close 2.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.113 (body 0.078, range 0.149); 'price stays where it was' would score 0.095; colour right 0.458; typical miss of the close 3.5 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.108 (body 0.076, range 0.139); 'price stays where it was' would score 0.103; colour right 0.492; typical miss of the close 3.1 bp; chain ended on the right side 0.615 of 96 chains; n=1440
- 7d: match 0.119 (body 0.077, range 0.160); 'price stays where it was' would score 0.119; colour right 0.493; typical miss of the close 7.4 bp; chain ended on the right side 0.525 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.0 bp; chain ended on the right side 0.511 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.3; 2: 0.197 / 4.3; 3: 0.169 / 6.1; 4: 0.134 / 6.4; 5: 0.122 / 7.2; 6: 0.112 / 8.1; 7: 0.100 / 8.4; 8: 0.093 / 8.8; 9: 0.089 / 9.1; 10: 0.083 / 9.9; 11: 0.077 / 10.5; 12: 0.076 / 10.8; 13: 0.068 / 11.1; 14: 0.068 / 11.2; 15: 0.063 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 89836, probability skill vs chance 0.2202, widened contest next: False
  - now: threshold 0.8399, hit rate recent 0.926 / long run 0.9402
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.264, naive rule 0.446, lift 3.47x
    - 24h: 53 calls (53 a day), hit rate 0.925, chance 0.300, naive rule 0.503, lift 3.09x
    - 7d: 390 calls (56 a day), hit rate 0.946, chance 0.289, naive rule 0.484, lift 3.28x
    - 30d: 1704 calls (57 a day), hit rate 0.942, chance 0.293, naive rule 0.483, lift 3.22x
  - next: threshold 0.5294, hit rate recent 0.5632 / long run 0.5754
    - 6h: 27 calls (110 a day), hit rate 0.444, chance 0.264, lift 1.68x
    - 24h: 127 calls (128 a day), hit rate 0.567, chance 0.300, lift 1.89x
    - 7d: 687 calls (98 a day), hit rate 0.579, chance 0.289, lift 2.01x
    - 30d: 2447 calls (82 a day), hit rate 0.584, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.519; 0.40: 489, 0.560; 0.45: 422, 0.626; 0.50: 368, 0.681; 0.55: 322, 0.725; 0.60: 274, 0.767; 0.65: 224, 0.803; 0.70: 182, 0.835; 0.75: 140, 0.870; 0.80: 99, 0.909; 0.85: 49, 0.951; 0.90: 1, 0.974
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 497, 0.459; 0.40: 414, 0.487; 0.45: 318, 0.518; 0.50: 209, 0.551; 0.55: 94, 0.586; 0.60: 13, 0.613; 0.65: 0, 0.714
- **K=5**: model 1790208000, labels learned 89834, probability skill vs chance 0.2177, widened contest next: True
  - now: threshold 0.7106, hit rate recent 0.8607 / long run 0.8432
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.155, naive rule 0.343, lift 5.65x
    - 24h: 60 calls (60 a day), hit rate 0.867, chance 0.181, naive rule 0.384, lift 4.78x
    - 7d: 378 calls (54 a day), hit rate 0.854, chance 0.187, naive rule 0.393, lift 4.58x
    - 30d: 1590 calls (53 a day), hit rate 0.838, chance 0.186, naive rule 0.391, lift 4.50x
  - next: threshold 0.4426, hit rate recent 0.4175 / long run 0.4665
    - 6h: 31 calls (127 a day), hit rate 0.323, chance 0.155, lift 2.08x
    - 24h: 147 calls (148 a day), hit rate 0.422, chance 0.181, lift 2.33x
    - 7d: 701 calls (100 a day), hit rate 0.448, chance 0.187, lift 2.40x
    - 30d: 2105 calls (70 a day), hit rate 0.485, chance 0.186, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 433, 0.410; 0.35: 373, 0.462; 0.40: 301, 0.531; 0.45: 246, 0.588; 0.50: 192, 0.649; 0.55: 147, 0.699; 0.60: 115, 0.740; 0.65: 88, 0.783; 0.70: 65, 0.821; 0.75: 35, 0.860; 0.80: 9, 0.879
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.385; 0.35: 254, 0.422; 0.40: 169, 0.447; 0.45: 89, 0.471; 0.50: 22, 0.513; 0.55: 3, 0.570
- **K=8**: model 1791072000, labels learned 89831, probability skill vs chance 0.2037, widened contest next: False
  - now: threshold 0.5605, hit rate recent 0.7579 / long run 0.7307
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.117, naive rule 0.289, lift 5.89x
    - 24h: 47 calls (47 a day), hit rate 0.745, chance 0.123, naive rule 0.330, lift 6.06x
    - 7d: 320 calls (46 a day), hit rate 0.734, chance 0.124, naive rule 0.332, lift 5.94x
    - 30d: 1543 calls (51 a day), hit rate 0.723, chance 0.122, naive rule 0.327, lift 5.94x
  - next: threshold 0.3669, hit rate recent 0.3958 / long run 0.4041
    - 6h: 20 calls (83 a day), hit rate 0.250, chance 0.117, lift 2.13x
    - 24h: 77 calls (78 a day), hit rate 0.403, chance 0.123, lift 3.28x
    - 7d: 422 calls (60 a day), hit rate 0.382, chance 0.124, lift 3.09x
    - 30d: 2012 calls (67 a day), hit rate 0.403, chance 0.122, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 277, 0.397; 0.35: 208, 0.473; 0.40: 161, 0.538; 0.45: 128, 0.586; 0.50: 97, 0.628; 0.55: 69, 0.682; 0.60: 46, 0.730; 0.65: 25, 0.765; 0.70: 9, 0.807; 0.75: 1, 0.812
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 190, 0.344; 0.35: 119, 0.381; 0.40: 49, 0.410; 0.45: 11, 0.423; 0.50: 1, 0.439
- **K=13**: model 1791072000, labels learned 89826, probability skill vs chance 0.1865, widened contest next: False
  - now: threshold 0.4078, hit rate recent 0.633 / long run 0.5944
    - 6h: 18 calls (75 a day), hit rate 0.556, chance 0.083, naive rule 0.239, lift 6.71x
    - 24h: 53 calls (54 a day), hit rate 0.642, chance 0.080, naive rule 0.265, lift 8.05x
    - 7d: 349 calls (50 a day), hit rate 0.585, chance 0.078, naive rule 0.265, lift 7.46x
    - 30d: 1437 calls (48 a day), hit rate 0.589, chance 0.076, naive rule 0.266, lift 7.72x
  - next: threshold 0.2682, hit rate recent 0.2743 / long run 0.2934
    - 6h: 20 calls (84 a day), hit rate 0.200, chance 0.083, lift 2.41x
    - 24h: 89 calls (90 a day), hit rate 0.292, chance 0.080, lift 3.67x
    - 7d: 645 calls (92 a day), hit rate 0.276, chance 0.078, lift 3.52x
    - 30d: 1990 calls (66 a day), hit rate 0.306, chance 0.076, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.435; 0.35: 90, 0.491; 0.40: 65, 0.539; 0.45: 45, 0.601; 0.50: 29, 0.620; 0.55: 16, 0.663; 0.60: 7, 0.683; 0.65: 2, 0.774; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.314; 0.35: 18, 0.344; 0.40: 4, 0.330; 0.45: 1, 0.435

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.997 | 0.74% | 0.900 | 0.417 | 0.249 | 0.542 | 0.187 |
| 6h | 6.086 | 3.16% | 0.878 | 0.469 | 0.251 | 0.475 | 0.481 |
| 24h | 5.045 | 3.32% | 0.886 | 0.508 | 0.251 | 0.497 | 0.404 |
| 7d | 12.591 | 4.17% | 0.900 | 0.501 | 0.251 | 0.496 | 0.687 |
| 30d | 14.113 | 4.20% | 0.900 | 0.500 | 0.251 | 0.499 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.041 | 5.986 | 6.000 | 6.008 | 6.104 | 6.274 | 5.951 | 5.973 | 5.973 | 5.997 |
| 6h | 6.284 | 6.176 | 6.141 | 6.068 | 6.269 | 6.253 | 6.077 | 6.077 | 6.072 | 6.086 |
| 24h | 5.218 | 5.105 | 5.093 | 5.059 | 5.247 | 5.402 | 5.043 | 5.042 | 5.042 | 5.045 |
| 7d | 13.139 | 12.691 | 12.673 | 12.600 | 12.838 | 12.772 | 12.581 | 12.581 | 12.568 | 12.591 |
| 30d | 14.732 | 14.246 | 14.202 | 14.141 | 14.386 | 14.335 | 14.120 | 14.086 | 14.087 | 14.113 |

## Next candle

- candle starting 2026-10-04 13:22 UTC, last close 2697.97
- P(up) 0.4677, return quantiles (bp): {'05': -3.071, '10': -2.093, '25': -0.938, '40': -0.298, '50': -0.074, '60': 0.163, '75': 0.771, '90': 2.074, '95': 3.247}
- changepoint probability 0.062, regime age 67.0 min
- agent weights: empirical 0.015, ewma 0.081, garch 0.105, har 0.252, bocpd 0.009, hmm 0.004, online_qr 0.263, lgbm 0.271

## Learning log

- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- HMM volatility states (sd, bp per minute): [1.75, 4.62, 12.53], current probabilities: [0.967, 0.033, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-04 13:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.304, 'l_abs': 0.696, 'l_hi': 0.764, 'l_lo': 0.721, 'b05': 0.669, 'b25': 0.698, 'b75': 0.559, 'b95': 0.607}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.5], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.64, 2.18, 2.678, 3.383, 3.788, 3.785, 3.974, 4.858, 5.131, 5.501, 6.893, 6.636, 5.999, 6.347]}
- calibration offsets (in sigma): {'05': -0.0095, '10': 0.041, '25': 0.0225, '40': 0.004, '50': -0.045, '60': -0.084, '75': -0.1125, '90': -0.021, '95': 0.0995}
