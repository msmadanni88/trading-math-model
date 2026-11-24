# ETH-USD 60s candle generator - report

- generated: 2026-11-24 16:04 UTC
- last closed candle: 2026-11-24 16:04 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.525 (672) [0.504, 0.548] | 0.517 (2879) [0.501, 0.533] | 0.516 (7961) [0.505, 0.526] | 0.518 (4989) [0.504, 0.532] | 0.484 (64) | 0.500 | flat +0.008 (noise 0.027) |
| colour_clear | 0.568 (780) | 0.551 (5516) [0.537, 0.565] | 0.541 (23823) [0.535, 0.548] | 0.526 (65314) [0.521, 0.531] | 0.544 (41076) [0.539, 0.548] | 0.546 (551) | 0.500 | flat +0.011 (noise 0.010) |
| colour_confident | 0.568 (213) | 0.577 (1326) [0.557, 0.593] | 0.572 (4522) [0.562, 0.581] | 0.585 (7715) [0.576, 0.595] | 0.585 (7715) [0.576, 0.595] | 0.534 (118) | 0.500 | flat +0.044 (noise 0.022) |
| colour_next | 0.556 (1432) | 0.534 (10047) [0.526, 0.542] | 0.531 (42900) [0.527, 0.535] | 0.519 (118656) [0.516, 0.523] | 0.530 (74307) [0.527, 0.534] | 0.527 (962) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.499 (20048) | 0.503 (140658) [0.500, 0.505] | 0.502 (600600) [0.501, 0.503] | 0.501 (1661184) [0.500, 0.502] | 0.501 (1040298) [0.500, 0.502] | 0.504 (13468) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.571 (63) | 0.622 (376) [0.597, 0.648] | 0.608 (1222) [0.593, 0.622] | 0.623 (2056) [0.609, 0.638] | 0.623 (2056) [0.609, 0.638] | 0.529 (34) | 0.500 | flat +0.056 (noise 0.044) |
| reversal_k13_next | 0.319 (47) | 0.332 (449) [0.290, 0.383] | 0.337 (1827) [0.320, 0.355] | 0.317 (5445) [0.307, 0.326] | 0.328 (3340) [0.316, 0.339] | 0.433 (30) | 0.078 | flat -0.007 (noise 0.035) |
| reversal_k13_now | 0.500 (48) | 0.549 (379) [0.513, 0.588] | 0.572 (1625) [0.552, 0.592] | 0.573 (4276) [0.561, 0.585] | 0.569 (2804) [0.554, 0.584] | 0.743 (35) | 0.078 | flat -0.056 (noise 0.037) |
| reversal_k3_next | 0.547 (150) | 0.593 (865) [0.559, 0.624] | 0.600 (2649) [0.588, 0.613] | 0.590 (7211) [0.581, 0.598] | 0.591 (4771) [0.580, 0.602] | 0.574 (108) | 0.294 | flat -0.020 (noise 0.032) |
| reversal_k3_now | 0.942 (52) | 0.938 (388) [0.921, 0.956] | 0.930 (1721) [0.922, 0.939] | 0.935 (4744) [0.930, 0.940] | 0.932 (2981) [0.925, 0.939] | 0.902 (51) | 0.294 | flat +0.009 (noise 0.018) |
| reversal_k5_next | 0.417 (60) | 0.477 (346) [0.418, 0.556] | 0.511 (1825) [0.491, 0.531] | 0.486 (6131) [0.475, 0.498] | 0.482 (4141) [0.468, 0.497] | 0.500 (62) | 0.187 | flat -0.024 (noise 0.049) |
| reversal_k5_now | 0.807 (57) | 0.814 (413) [0.794, 0.833] | 0.796 (1763) [0.779, 0.811] | 0.817 (4534) [0.806, 0.826] | 0.805 (2923) [0.793, 0.816] | 0.812 (48) | 0.188 | up +0.064 (noise 0.028) |
| reversal_k8_next | 0.354 (79) | 0.411 (577) [0.380, 0.448] | 0.416 (2278) [0.401, 0.432] | 0.398 (6465) [0.388, 0.408] | 0.399 (4359) [0.388, 0.411] | 0.558 (43) | 0.121 | flat -0.010 (noise 0.031) |
| reversal_k8_now | 0.625 (56) | 0.667 (423) [0.647, 0.685] | 0.679 (1646) [0.661, 0.698] | 0.693 (4385) [0.682, 0.706] | 0.682 (2798) [0.667, 0.696] | 0.717 (46) | 0.122 | flat +0.009 (noise 0.033) |
| overall | 0.504 (22125) | 0.507 (155217) [0.505, 0.509] | 0.506 (661713) [0.505, 0.507] | 0.504 (1830992) [0.503, 0.505] | 0.505 (1147711) [0.504, 0.506] | 0.510 (14917) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07769, 0.1119] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5353, 'levels': [{'threshold': 0.07769, 'calls_per_day': 145.1, 'win_rate': 0.578}, {'threshold': 0.1119, 'calls_per_day': 37.2, 'win_rate': 0.6015}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42900, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15202 | 0.349 | 0.532 (14983) | 0.561 (2199) | 0.749 (2526) |
| volatility: normal | 15202 | 0.379 | 0.528 (15148) | 0.577 (1534) | 0.750 (2482) |
| volatility: wild | 15200 | 0.390 | 0.531 (15162) | 0.590 (1176) | 0.752 (2137) |
| session: Asia 00-08 | 15360 | 0.371 | 0.531 (15248) | 0.560 (1719) | 0.750 (2328) |
| session: Europe 08-13 | 9600 | 0.367 | 0.530 (9523) | 0.576 (1229) | 0.762 (1523) |
| session: US 13-21 | 15064 | 0.381 | 0.535 (14974) | 0.604 (1355) | 0.743 (2444) |
| session: late 21-24 | 5580 | 0.367 | 0.517 (5548) | 0.533 (606) | 0.752 (850) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.453 | 0.440 | 0.319 | 0.319 | 0.567 | 0.357 | 0.548 | 1.121 |
| 6h | 360 | 0.402 | 0.394 | 0.291 | 0.339 | 0.508 | 0.276 | 0.528 | 1.180 |
| 24h | 1440 | 0.390 | 0.385 | 0.297 | 0.336 | 0.532 | 0.271 | 0.509 | 1.182 |
| 7d | 10080 | 0.386 | 0.379 | 0.297 | 0.331 | 0.536 | 0.269 | 0.503 | 1.194 |
| 30d | 43200 | 0.374 | 0.368 | 0.288 | 0.320 | 0.531 | 0.266 | 0.482 | 1.265 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.453 / 0.567 / 0.850; 2: 0.422 / 0.467 / 0.867; 3: 0.432 / 0.567 / 0.883; 4: 0.435 / 0.567 / 0.967; 5: 0.394 / 0.417 / 0.833; 6: 0.428 / 0.500 / 0.867; 7: 0.410 / 0.533 / 0.950; 8: 0.421 / 0.533 / 1.000; 9: 0.412 / 0.433 / 0.933; 10: 0.425 / 0.550 / 0.817; 11: 0.390 / 0.417 / 0.917; 12: 0.408 / 0.483 / 0.950; 13: 0.422 / 0.483 / 0.883; 14: 0.416 / 0.517 / 0.767; 15: 0.441 / 0.583 / 0.850
- 6h: 1: 0.402 / 0.508 / 0.889; 2: 0.390 / 0.478 / 0.889; 3: 0.399 / 0.536 / 0.850; 4: 0.398 / 0.522 / 0.950; 5: 0.389 / 0.481 / 0.856; 6: 0.391 / 0.494 / 0.856; 7: 0.391 / 0.533 / 0.917; 8: 0.389 / 0.522 / 0.933; 9: 0.380 / 0.486 / 0.886; 10: 0.385 / 0.522 / 0.767; 11: 0.386 / 0.494 / 0.864; 12: 0.383 / 0.511 / 0.856; 13: 0.376 / 0.486 / 0.825; 14: 0.380 / 0.497 / 0.758; 15: 0.398 / 0.564 / 0.803
- 24h: 1: 0.390 / 0.532 / 0.888; 2: 0.376 / 0.492 / 0.905; 3: 0.382 / 0.517 / 0.894; 4: 0.376 / 0.504 / 0.937; 5: 0.377 / 0.499 / 0.889; 6: 0.373 / 0.504 / 0.894; 7: 0.379 / 0.513 / 0.903; 8: 0.379 / 0.518 / 0.910; 9: 0.373 / 0.495 / 0.892; 10: 0.378 / 0.530 / 0.855; 11: 0.376 / 0.506 / 0.897; 12: 0.372 / 0.493 / 0.895; 13: 0.363 / 0.463 / 0.886; 14: 0.375 / 0.506 / 0.860; 15: 0.372 / 0.508 / 0.878
- 7d: 1: 0.386 / 0.536 / 0.899; 2: 0.371 / 0.492 / 0.900; 3: 0.372 / 0.505 / 0.898; 4: 0.370 / 0.495 / 0.903; 5: 0.374 / 0.510 / 0.899; 6: 0.369 / 0.498 / 0.900; 7: 0.370 / 0.506 / 0.902; 8: 0.371 / 0.513 / 0.903; 9: 0.368 / 0.499 / 0.901; 10: 0.370 / 0.513 / 0.895; 11: 0.368 / 0.504 / 0.900; 12: 0.369 / 0.503 / 0.899; 13: 0.365 / 0.496 / 0.898; 14: 0.367 / 0.502 / 0.894; 15: 0.365 / 0.499 / 0.900
- 30d: 1: 0.374 / 0.531 / 0.898; 2: 0.361 / 0.491 / 0.900; 3: 0.365 / 0.512 / 0.899; 4: 0.360 / 0.497 / 0.901; 5: 0.362 / 0.506 / 0.899; 6: 0.359 / 0.502 / 0.899; 7: 0.360 / 0.502 / 0.900; 8: 0.360 / 0.507 / 0.900; 9: 0.359 / 0.501 / 0.900; 10: 0.359 / 0.504 / 0.899; 11: 0.359 / 0.506 / 0.900; 12: 0.359 / 0.503 / 0.900; 13: 0.357 / 0.499 / 0.899; 14: 0.358 / 0.502 / 0.899; 15: 0.357 / 0.501 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.081 (body 0.041, range 0.122); 'price stays where it was' would score 0.079; colour right 0.483; typical miss of the close 34.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.127 (body 0.073, range 0.180); 'price stays where it was' would score 0.140; colour right 0.503; typical miss of the close 19.5 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.134 (body 0.083, range 0.184); 'price stays where it was' would score 0.131; colour right 0.492; typical miss of the close 16.1 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.136 (body 0.088, range 0.183); 'price stays where it was' would score 0.141; colour right 0.503; typical miss of the close 13.8 bp; chain ended on the right side 0.519 of 672 chains; n=10080
- 30d: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.8 bp; chain ended on the right side 0.514 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 5.8; 2: 0.207 / 6.5; 3: 0.167 / 8.5; 4: 0.137 / 8.9; 5: 0.126 / 9.6; 6: 0.118 / 10.4; 7: 0.116 / 11.0; 8: 0.100 / 11.8; 9: 0.092 / 12.5; 10: 0.089 / 12.9; 11: 0.087 / 13.4; 12: 0.082 / 13.5; 13: 0.075 / 14.4; 14: 0.070 / 14.7; 15: 0.067 / 15.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 163438, probability skill vs chance 0.2247, widened contest next: False
  - now: threshold 0.8298, hit rate recent 0.9078 / long run 0.93
    - 6h: 23 calls (93 a day), hit rate 0.870, chance 0.303, naive rule 0.488, lift 2.87x
    - 24h: 72 calls (72 a day), hit rate 0.889, chance 0.306, naive rule 0.519, lift 2.90x
    - 7d: 413 calls (59 a day), hit rate 0.932, chance 0.299, naive rule 0.520, lift 3.12x
    - 30d: 1741 calls (58 a day), hit rate 0.930, chance 0.294, naive rule 0.503, lift 3.16x
  - next: threshold 0.5253, hit rate recent 0.5974 / long run 0.5956
    - 6h: 33 calls (134 a day), hit rate 0.576, chance 0.303, lift 1.90x
    - 24h: 157 calls (158 a day), hit rate 0.573, chance 0.306, lift 1.87x
    - 7d: 910 calls (130 a day), hit rate 0.592, chance 0.299, lift 1.98x
    - 30d: 2714 calls (90 a day), hit rate 0.599, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.503; 0.35: 529, 0.528; 0.40: 480, 0.573; 0.45: 416, 0.637; 0.50: 366, 0.683; 0.55: 318, 0.728; 0.60: 269, 0.774; 0.65: 226, 0.805; 0.70: 178, 0.835; 0.75: 143, 0.870; 0.80: 94, 0.901; 0.85: 43, 0.941; 0.90: 4, 0.962
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.436; 0.35: 487, 0.470; 0.40: 384, 0.511; 0.45: 291, 0.543; 0.50: 186, 0.573; 0.55: 78, 0.586; 0.60: 10, 0.637; 0.65: 0, 0.538
- **K=5**: model 1794528000, labels learned 163436, probability skill vs chance 0.2207, widened contest next: False
  - now: threshold 0.7007, hit rate recent 0.8171 / long run 0.7964
    - 6h: 19 calls (78 a day), hit rate 0.842, chance 0.171, naive rule 0.377, lift 4.91x
    - 24h: 68 calls (68 a day), hit rate 0.809, chance 0.179, naive rule 0.395, lift 4.52x
    - 7d: 419 calls (60 a day), hit rate 0.819, chance 0.195, naive rule 0.431, lift 4.21x
    - 30d: 1779 calls (59 a day), hit rate 0.795, chance 0.188, naive rule 0.415, lift 4.22x
  - next: threshold 0.4525, hit rate recent 0.4972 / long run 0.4998
    - 6h: 15 calls (61 a day), hit rate 0.400, chance 0.171, lift 2.33x
    - 24h: 93 calls (93 a day), hit rate 0.452, chance 0.179, lift 2.52x
    - 7d: 365 calls (52 a day), hit rate 0.499, chance 0.195, lift 2.56x
    - 30d: 1795 calls (60 a day), hit rate 0.512, chance 0.188, lift 2.72x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.425; 0.35: 364, 0.474; 0.40: 295, 0.542; 0.45: 239, 0.603; 0.50: 187, 0.654; 0.55: 150, 0.685; 0.60: 116, 0.731; 0.65: 84, 0.767; 0.70: 52, 0.803; 0.75: 27, 0.837; 0.80: 6, 0.849
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 332, 0.396; 0.35: 247, 0.434; 0.40: 157, 0.462; 0.45: 63, 0.509; 0.50: 8, 0.564; 0.55: 1, 0.471
- **K=8**: model 1794960000, labels learned 163433, probability skill vs chance 0.2167, widened contest next: False
  - now: threshold 0.5851, hit rate recent 0.6883 / long run 0.6722
    - 6h: 20 calls (82 a day), hit rate 0.700, chance 0.136, naive rule 0.362, lift 5.16x
    - 24h: 67 calls (67 a day), hit rate 0.687, chance 0.124, naive rule 0.346, lift 5.53x
    - 7d: 427 calls (61 a day), hit rate 0.679, chance 0.125, naive rule 0.363, lift 5.41x
    - 30d: 1660 calls (55 a day), hit rate 0.679, chance 0.124, naive rule 0.349, lift 5.50x
  - next: threshold 0.3514, hit rate recent 0.4778 / long run 0.4251
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.136, lift 3.68x
    - 24h: 72 calls (73 a day), hit rate 0.472, chance 0.124, lift 3.80x
    - 7d: 560 calls (80 a day), hit rate 0.429, chance 0.125, lift 3.42x
    - 30d: 2237 calls (75 a day), hit rate 0.421, chance 0.124, lift 3.41x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.427; 0.35: 202, 0.486; 0.40: 159, 0.536; 0.45: 121, 0.578; 0.50: 87, 0.634; 0.55: 63, 0.669; 0.60: 42, 0.709; 0.65: 24, 0.769; 0.70: 9, 0.807; 0.75: 1, 0.718
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.377; 0.35: 83, 0.410; 0.40: 28, 0.447; 0.45: 6, 0.478; 0.50: 1, 0.645
- **K=13**: model 1795478400, labels learned 163428, probability skill vs chance 0.2075, widened contest next: False
  - now: threshold 0.4589, hit rate recent 0.6335 / long run 0.579
    - 6h: 14 calls (58 a day), hit rate 0.786, chance 0.090, naive rule 0.337, lift 8.74x
    - 24h: 54 calls (55 a day), hit rate 0.630, chance 0.083, naive rule 0.314, lift 7.57x
    - 7d: 374 calls (54 a day), hit rate 0.578, chance 0.082, naive rule 0.315, lift 7.02x
    - 30d: 1623 calls (54 a day), hit rate 0.576, chance 0.080, naive rule 0.298, lift 7.21x
  - next: threshold 0.3039, hit rate recent 0.4031 / long run 0.3429
    - 6h: 12 calls (50 a day), hit rate 0.250, chance 0.090, lift 2.78x
    - 24h: 49 calls (50 a day), hit rate 0.429, chance 0.083, lift 5.15x
    - 7d: 431 calls (62 a day), hit rate 0.355, chance 0.082, lift 4.31x
    - 30d: 1805 calls (60 a day), hit rate 0.338, chance 0.080, lift 4.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 142, 0.424; 0.35: 104, 0.472; 0.40: 72, 0.535; 0.45: 50, 0.585; 0.50: 35, 0.623; 0.55: 21, 0.649; 0.60: 10, 0.673; 0.65: 2, 0.532
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.343; 0.35: 15, 0.389; 0.40: 2, 0.449

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 47.833 | 8.81% | 0.867 | 0.383 | 0.247 | 0.583 | 0.294 |
| 6h | 30.549 | 3.92% | 0.900 | 0.486 | 0.250 | 0.506 | 0.562 |
| 24h | 25.715 | 2.22% | 0.894 | 0.497 | 0.250 | 0.516 | 0.547 |
| 7d | 24.849 | 4.29% | 0.899 | 0.499 | 0.250 | 0.510 | 0.662 |
| 30d | 19.703 | 4.81% | 0.900 | 0.500 | 0.250 | 0.506 | 0.709 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 52.454 | 48.492 | 48.446 | 48.685 | 48.756 | 48.737 | 47.762 | 47.438 | 47.795 | 47.833 |
| 6h | 31.795 | 30.775 | 30.675 | 30.707 | 31.591 | 30.932 | 30.404 | 30.371 | 30.466 | 30.549 |
| 24h | 26.299 | 25.885 | 25.830 | 25.806 | 26.299 | 26.013 | 25.705 | 25.625 | 25.673 | 25.715 |
| 7d | 25.963 | 25.117 | 25.013 | 24.869 | 25.400 | 25.176 | 24.838 | 24.786 | 24.812 | 24.849 |
| 30d | 20.699 | 19.891 | 19.841 | 19.758 | 20.116 | 20.030 | 19.686 | 19.659 | 19.670 | 19.703 |

## Next candle

- candle starting 2026-11-24 16:04 UTC, last close 1671.95
- P(up) 0.5003, return quantiles (bp): {'05': -24.924, '10': -18.018, '25': -10.053, '40': -4.075, '50': -0.001, '60': 4.409, '75': 10.208, '90': 17.051, '95': 23.402}
- changepoint probability 0.0463, regime age 56.5 min
- agent weights: empirical 0.004, ewma 0.073, garch 0.119, har 0.105, bocpd 0.007, hmm 0.032, online_qr 0.274, lgbm 0.387

## Learning log

- 2026-11-22 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.9173}, "hmm": {"sd_bp": [5.55, 10.36, 28.43], "stay": [0.982, 0.95, 0.859]}}
- 2026-11-23 00:00 UTC: {"garch": {"alpha": 0.0752, "beta": 0.917}, "hmm": {"sd_bp": [5.28, 10.22, 28.39], "stay": [0.976, 0.946, 0.857]}, "lgbm": {"challenger_loss": 0.24364, "champion_loss": 0.24354, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.61601, "widened": false, "champion_loss": 0.4869, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38212, "challengers": 1, "chance_loss": 0.503, "widened": false, "champion_loss": 0.38113, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29091, "challengers": 1, "chance_loss": 0.3912, "widened": false, "champion_loss": 0.28935, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20987, "challengers": 1, "chance_loss": 0.29233, "widened": false, "champion_loss": 0.20927, "promoted": false}}
- 2026-11-23 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.9112}, "hmm": {"sd_bp": [5.07, 10.1, 28.28], "stay": [0.973, 0.946, 0.862]}}
- 2026-11-24 00:00 UTC: {"garch": {"alpha": 0.0886, "beta": 0.9021}, "hmm": {"sd_bp": [4.97, 10.02, 31.47], "stay": [0.968, 0.952, 0.875]}, "lgbm": {"challenger_loss": 0.25051, "champion_loss": 0.25047, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48498, "challengers": 3, "chance_loss": 0.6173, "widened": true, "champion_loss": 0.48458, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37971, "challengers": 1, "chance_loss": 0.49915, "widened": false, "champion_loss": 0.37928, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27848, "challengers": 3, "chance_loss": 0.37338, "widened": true, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20281, "challengers": 3, "chance_loss": 0.28057, "widened": true, "champion_loss": 0.20335, "promoted": true}}
- 2026-11-24 12:00 UTC: {"garch": {"alpha": 0.0937, "beta": 0.8962}, "hmm": {"sd_bp": [5.06, 10.1, 31.41], "stay": [0.968, 0.948, 0.887]}}
- HMM volatility states (sd, bp per minute): [5.06, 10.1, 31.41], current probabilities: [0.008, 0.919, 0.073]
- live generator: {'versions': 60, 'latest_effective': '2026-11-24 16:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.155, 'l_abs': 0.751, 'l_hi': 0.8, 'l_lo': 0.734, 'b05': 0.679, 'b25': 0.703, 'b75': 0.584, 'b95': 0.666}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6]], 'cone_width': [1.734, 3.652, 1.407, 4.115, 4.254, 2.527, 2.172, 3.883, 13.617, 5.703, 5.968, 8.073, 16.904, 11.291]}
- calibration offsets (in sigma): {'05': -0.0485, '10': 0.013, '25': -0.0325, '40': -0.048, '50': -0.025, '60': 0.038, '75': 0.0325, '90': -0.043, '95': -0.0315}
