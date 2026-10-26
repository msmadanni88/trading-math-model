# ETH-USD 60s candle generator - report

- generated: 2026-10-26 16:51 UTC
- last closed candle: 2026-10-26 16:51 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.646 (96) | 0.548 (672) [0.509, 0.588] | 0.525 (2876) [0.506, 0.545] | 0.517 (5178) [0.503, 0.532] | 0.524 (2206) [0.501, 0.548] | 0.403 (67) | 0.500 | flat +0.021 (noise 0.030) |
| colour_clear | 0.534 (802) | 0.550 (5686) [0.543, 0.559] | 0.535 (23445) [0.527, 0.542] | 0.518 (42293) [0.511, 0.524] | 0.546 (18055) [0.541, 0.551] | 0.540 (583) | 0.500 | flat +0.005 (noise 0.009) |
| colour_confident | 0.578 (268) | 0.607 (1411) [0.590, 0.627] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.620 (108) | 0.500 | flat +0.023 (noise 0.024) |
| colour_next | 0.523 (1434) | 0.535 (10043) [0.528, 0.541] | 0.524 (42849) [0.520, 0.529] | 0.513 (77190) [0.509, 0.517] | 0.530 (32841) [0.525, 0.534] | 0.526 (1005) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.506 (20076) | 0.501 (140602) [0.498, 0.503] | 0.501 (599886) [0.499, 0.502] | 0.501 (1080660) [0.500, 0.502] | 0.500 (459774) [0.499, 0.502] | 0.499 (14070) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.589 (107) | 0.628 (406) [0.603, 0.666] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.639 (36) | 0.500 | flat +0.012 (noise 0.048) |
| reversal_k13_next | 0.364 (66) | 0.318 (466) [0.295, 0.338] | 0.304 (2171) [0.292, 0.315] | 0.307 (3684) [0.297, 0.318] | 0.318 (1579) [0.307, 0.329] | 0.317 (41) | 0.077 | flat +0.022 (noise 0.031) |
| reversal_k13_now | 0.600 (55) | 0.552 (357) [0.510, 0.599] | 0.569 (1575) [0.549, 0.590] | 0.574 (2706) [0.558, 0.590] | 0.566 (1234) [0.543, 0.590] | 0.451 (51) | 0.077 | flat +0.009 (noise 0.037) |
| reversal_k3_next | 0.588 (80) | 0.593 (678) [0.563, 0.626] | 0.580 (2811) [0.566, 0.594] | 0.584 (4642) [0.573, 0.595] | 0.580 (2202) [0.566, 0.595] | 0.584 (77) | 0.293 | flat +0.027 (noise 0.026) |
| reversal_k3_now | 0.870 (46) | 0.936 (388) [0.911, 0.958] | 0.935 (1685) [0.926, 0.945] | 0.937 (3069) [0.930, 0.944] | 0.931 (1306) [0.920, 0.942] | 0.976 (42) | 0.293 | flat -0.003 (noise 0.021) |
| reversal_k5_next | 0.496 (137) | 0.470 (924) [0.441, 0.494] | 0.464 (2951) [0.450, 0.478] | 0.476 (4443) [0.464, 0.489] | 0.462 (2453) [0.447, 0.477] | 0.526 (76) | 0.186 | flat +0.012 (noise 0.024) |
| reversal_k5_now | 0.837 (49) | 0.818 (363) [0.807, 0.829] | 0.831 (1563) [0.817, 0.844] | 0.830 (2820) [0.819, 0.841] | 0.820 (1209) [0.806, 0.833] | 0.850 (40) | 0.187 | flat +0.008 (noise 0.029) |
| reversal_k8_next | 0.403 (119) | 0.378 (759) [0.359, 0.396] | 0.382 (2589) [0.370, 0.395] | 0.389 (4306) [0.378, 0.401] | 0.382 (2200) [0.368, 0.396] | 0.329 (73) | 0.120 | flat +0.000 (noise 0.026) |
| reversal_k8_now | 0.729 (48) | 0.665 (337) [0.621, 0.710] | 0.698 (1525) [0.677, 0.718] | 0.702 (2787) [0.686, 0.717] | 0.687 (1200) [0.665, 0.710] | 0.500 (40) | 0.121 | flat -0.016 (noise 0.036) |
| overall | 0.509 (22206) | 0.504 (155589) [0.502, 0.507] | 0.504 (662481) [0.503, 0.506] | 0.503 (1191485) [0.502, 0.504] | 0.504 (508204) [0.502, 0.506] | 0.502 (15582) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07837, 0.1166] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5328, 'levels': [{'threshold': 0.07837, 'calls_per_day': 146.3, 'win_rate': 0.6099}, {'threshold': 0.1166, 'calls_per_day': 38.0, 'win_rate': 0.6479}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 32707, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15217 | 0.336 | 0.524 (14970) | 0.588 (1739) | 0.764 (2519) |
| volatility: normal | 15217 | 0.365 | 0.525 (15148) | 0.608 (1224) | 0.752 (2253) |
| volatility: wild | 15217 | 0.379 | 0.520 (15174) | 0.635 (606) | 0.770 (1933) |
| session: Asia 00-08 | 15360 | 0.358 | 0.529 (15254) | 0.608 (1272) | 0.765 (2214) |
| session: Europe 08-13 | 9600 | 0.355 | 0.525 (9512) | 0.599 (893) | 0.759 (1519) |
| session: US 13-21 | 15111 | 0.368 | 0.519 (15008) | 0.598 (888) | 0.768 (2148) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5518) | 0.607 (516) | 0.740 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.416 | 0.412 | 0.276 | 0.276 | 0.567 | 0.281 | 0.550 | 1.180 |
| 6h | 360 | 0.377 | 0.376 | 0.308 | 0.351 | 0.513 | 0.250 | 0.504 | 1.146 |
| 24h | 1440 | 0.374 | 0.366 | 0.297 | 0.333 | 0.520 | 0.263 | 0.484 | 1.272 |
| 7d | 10080 | 0.370 | 0.360 | 0.278 | 0.310 | 0.531 | 0.268 | 0.472 | 1.212 |
| 30d | 43200 | 0.360 | 0.354 | 0.277 | 0.306 | 0.524 | 0.257 | 0.463 | 1.282 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.416 / 0.567 / 0.900; 2: 0.393 / 0.450 / 0.950; 3: 0.379 / 0.417 / 0.917; 4: 0.409 / 0.533 / 0.950; 5: 0.419 / 0.550 / 0.900; 6: 0.386 / 0.467 / 0.917; 7: 0.441 / 0.617 / 0.917; 8: 0.384 / 0.450 / 0.933; 9: 0.409 / 0.517 / 0.950; 10: 0.382 / 0.467 / 0.983; 11: 0.380 / 0.417 / 0.983; 12: 0.423 / 0.567 / 0.950; 13: 0.356 / 0.350 / 0.983; 14: 0.408 / 0.600 / 0.983; 15: 0.398 / 0.500 / 0.950
- 6h: 1: 0.377 / 0.513 / 0.858; 2: 0.366 / 0.454 / 0.900; 3: 0.363 / 0.465 / 0.883; 4: 0.375 / 0.540 / 0.897; 5: 0.365 / 0.504 / 0.836; 6: 0.365 / 0.482 / 0.872; 7: 0.350 / 0.454 / 0.908; 8: 0.352 / 0.443 / 0.931; 9: 0.379 / 0.546 / 0.961; 10: 0.363 / 0.504 / 0.983; 11: 0.349 / 0.457 / 0.981; 12: 0.368 / 0.532 / 0.967; 13: 0.341 / 0.432 / 0.983; 14: 0.369 / 0.524 / 0.989; 15: 0.369 / 0.524 / 0.978
- 24h: 1: 0.374 / 0.520 / 0.891; 2: 0.362 / 0.475 / 0.903; 3: 0.365 / 0.517 / 0.903; 4: 0.361 / 0.510 / 0.901; 5: 0.359 / 0.491 / 0.892; 6: 0.358 / 0.505 / 0.892; 7: 0.358 / 0.500 / 0.895; 8: 0.354 / 0.488 / 0.905; 9: 0.366 / 0.523 / 0.911; 10: 0.358 / 0.508 / 0.915; 11: 0.357 / 0.500 / 0.913; 12: 0.359 / 0.513 / 0.916; 13: 0.352 / 0.486 / 0.918; 14: 0.355 / 0.498 / 0.917; 15: 0.353 / 0.498 / 0.917
- 7d: 1: 0.370 / 0.531 / 0.897; 2: 0.358 / 0.501 / 0.901; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.498 / 0.899; 5: 0.354 / 0.500 / 0.899; 6: 0.353 / 0.495 / 0.901; 7: 0.352 / 0.497 / 0.901; 8: 0.354 / 0.508 / 0.903; 9: 0.353 / 0.499 / 0.904; 10: 0.353 / 0.506 / 0.903; 11: 0.351 / 0.498 / 0.903; 12: 0.352 / 0.504 / 0.904; 13: 0.349 / 0.494 / 0.903; 14: 0.350 / 0.495 / 0.904; 15: 0.350 / 0.500 / 0.903
- 30d: 1: 0.360 / 0.524 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.347 / 0.499 / 0.900; 8: 0.347 / 0.502 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.506 / 0.901; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.505 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.499 / 0.900; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.080 (body 0.037, range 0.123); 'price stays where it was' would score 0.119; colour right 0.433; typical miss of the close 19.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.117 (body 0.071, range 0.162); 'price stays where it was' would score 0.140; colour right 0.451; typical miss of the close 14.8 bp; chain ended on the right side 0.250 of 24 chains; n=360
- 24h: match 0.124 (body 0.080, range 0.167); 'price stays where it was' would score 0.136; colour right 0.495; typical miss of the close 10.4 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.168); 'price stays where it was' would score 0.134; colour right 0.502; typical miss of the close 8.9 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 7.7 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.9; 2: 0.195 / 4.5; 3: 0.168 / 5.9; 4: 0.131 / 6.5; 5: 0.123 / 7.1; 6: 0.112 / 7.7; 7: 0.106 / 7.9; 8: 0.096 / 8.3; 9: 0.087 / 8.3; 10: 0.087 / 9.1; 11: 0.084 / 9.6; 12: 0.076 / 9.9; 13: 0.067 / 10.1; 14: 0.069 / 10.5; 15: 0.059 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 121725, probability skill vs chance 0.2381, widened contest next: False
  - now: threshold 0.8341, hit rate recent 0.9426 / long run 0.9368
    - 6h: 20 calls (81 a day), hit rate 0.950, chance 0.293, naive rule 0.472, lift 3.24x
    - 24h: 56 calls (56 a day), hit rate 0.929, chance 0.296, naive rule 0.488, lift 3.14x
    - 7d: 395 calls (56 a day), hit rate 0.942, chance 0.297, naive rule 0.501, lift 3.17x
    - 30d: 1694 calls (56 a day), hit rate 0.936, chance 0.294, naive rule 0.492, lift 3.19x
  - next: threshold 0.5309, hit rate recent 0.5768 / long run 0.5895
    - 6h: 33 calls (134 a day), hit rate 0.545, chance 0.293, lift 1.86x
    - 24h: 110 calls (110 a day), hit rate 0.573, chance 0.296, lift 1.94x
    - 7d: 671 calls (96 a day), hit rate 0.599, chance 0.297, lift 2.02x
    - 30d: 2844 calls (95 a day), hit rate 0.581, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 538, 0.519; 0.40: 478, 0.576; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 311, 0.741; 0.60: 263, 0.786; 0.65: 220, 0.812; 0.70: 174, 0.844; 0.75: 136, 0.876; 0.80: 91, 0.914; 0.85: 46, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.427; 0.35: 502, 0.464; 0.40: 408, 0.499; 0.45: 310, 0.534; 0.50: 201, 0.570; 0.55: 90, 0.574; 0.60: 14, 0.629; 0.65: 1, 0.677
- **K=5**: model 1792540800, labels learned 121723, probability skill vs chance 0.2252, widened contest next: False
  - now: threshold 0.6725, hit rate recent 0.8225 / long run 0.8227
    - 6h: 19 calls (78 a day), hit rate 0.737, chance 0.193, naive rule 0.407, lift 3.83x
    - 24h: 56 calls (56 a day), hit rate 0.839, chance 0.193, naive rule 0.406, lift 4.35x
    - 7d: 365 calls (52 a day), hit rate 0.819, chance 0.184, naive rule 0.405, lift 4.44x
    - 30d: 1569 calls (52 a day), hit rate 0.830, chance 0.187, naive rule 0.400, lift 4.43x
  - next: threshold 0.4195, hit rate recent 0.5111 / long run 0.4812
    - 6h: 27 calls (110 a day), hit rate 0.519, chance 0.193, lift 2.69x
    - 24h: 117 calls (118 a day), hit rate 0.513, chance 0.193, lift 2.66x
    - 7d: 895 calls (128 a day), hit rate 0.478, chance 0.184, lift 2.59x
    - 30d: 3008 calls (100 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.425; 0.35: 343, 0.493; 0.40: 276, 0.565; 0.45: 224, 0.620; 0.50: 176, 0.671; 0.55: 136, 0.711; 0.60: 105, 0.756; 0.65: 76, 0.791; 0.70: 52, 0.831; 0.75: 30, 0.875; 0.80: 10, 0.900
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.389; 0.35: 253, 0.421; 0.40: 158, 0.453; 0.45: 70, 0.464; 0.50: 15, 0.487; 0.55: 1, 0.513
- **K=8**: model 1792800000, labels learned 121720, probability skill vs chance 0.201, widened contest next: True
  - now: threshold 0.5558, hit rate recent 0.5872 / long run 0.6733
    - 6h: 21 calls (86 a day), hit rate 0.381, chance 0.110, naive rule 0.290, lift 3.46x
    - 24h: 55 calls (55 a day), hit rate 0.545, chance 0.123, naive rule 0.330, lift 4.44x
    - 7d: 346 calls (49 a day), hit rate 0.656, chance 0.115, naive rule 0.320, lift 5.68x
    - 30d: 1530 calls (51 a day), hit rate 0.690, chance 0.121, naive rule 0.329, lift 5.72x
  - next: threshold 0.3356, hit rate recent 0.3317 / long run 0.3765
    - 6h: 29 calls (119 a day), hit rate 0.276, chance 0.110, lift 2.51x
    - 24h: 105 calls (106 a day), hit rate 0.362, chance 0.123, lift 2.95x
    - 7d: 748 calls (107 a day), hit rate 0.374, chance 0.115, lift 3.24x
    - 30d: 2630 calls (88 a day), hit rate 0.379, chance 0.121, lift 3.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.426; 0.35: 188, 0.496; 0.40: 145, 0.548; 0.45: 110, 0.594; 0.50: 84, 0.634; 0.55: 61, 0.670; 0.60: 40, 0.718; 0.65: 23, 0.788; 0.70: 10, 0.832; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.352; 0.35: 96, 0.378; 0.40: 35, 0.396; 0.45: 8, 0.418; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 121715, probability skill vs chance 0.181, widened contest next: True
  - now: threshold 0.4042, hit rate recent 0.498 / long run 0.5526
    - 6h: 22 calls (92 a day), hit rate 0.364, chance 0.062, naive rule 0.234, lift 5.84x
    - 24h: 67 calls (68 a day), hit rate 0.493, chance 0.074, naive rule 0.268, lift 6.62x
    - 7d: 375 calls (54 a day), hit rate 0.541, chance 0.074, naive rule 0.266, lift 7.35x
    - 30d: 1596 calls (53 a day), hit rate 0.563, chance 0.077, naive rule 0.272, lift 7.31x
  - next: threshold 0.294, hit rate recent 0.3284 / long run 0.3139
    - 6h: 16 calls (67 a day), hit rate 0.375, chance 0.062, lift 6.02x
    - 24h: 53 calls (54 a day), hit rate 0.340, chance 0.074, lift 4.57x
    - 7d: 444 calls (64 a day), hit rate 0.320, chance 0.074, lift 4.34x
    - 30d: 2169 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.442; 0.35: 88, 0.493; 0.40: 62, 0.548; 0.45: 41, 0.601; 0.50: 26, 0.655; 0.55: 15, 0.702; 0.60: 7, 0.745; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.315; 0.35: 14, 0.345; 0.40: 2, 0.437; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 18.266 | -0.26% | 0.933 | 0.483 | 0.250 | 0.533 | 0.146 |
| 6h | 21.155 | 3.85% | 0.894 | 0.500 | 0.251 | 0.499 | 0.658 |
| 24h | 18.255 | 4.98% | 0.899 | 0.506 | 0.250 | 0.507 | 0.662 |
| 7d | 15.235 | 3.57% | 0.899 | 0.500 | 0.250 | 0.502 | 0.663 |
| 30d | 13.625 | 4.15% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 18.218 | 18.289 | 18.458 | 18.517 | 18.380 | 18.388 | 18.370 | 18.320 | 18.255 | 18.266 |
| 6h | 22.003 | 21.340 | 21.243 | 21.176 | 21.322 | 21.268 | 21.192 | 21.075 | 21.092 | 21.155 |
| 24h | 19.212 | 18.434 | 18.426 | 18.283 | 18.586 | 18.510 | 18.240 | 18.209 | 18.210 | 18.255 |
| 7d | 15.799 | 15.380 | 15.319 | 15.253 | 15.502 | 15.391 | 15.223 | 15.195 | 15.204 | 15.235 |
| 30d | 14.214 | 13.758 | 13.710 | 13.649 | 13.870 | 13.809 | 13.620 | 13.601 | 13.599 | 13.625 |

## Next candle

- candle starting 2026-10-26 16:51 UTC, last close 2312.24
- P(up) 0.4904, return quantiles (bp): {'05': -12.018, '10': -9.237, '25': -4.944, '40': -2.198, '50': -0.18, '60': 1.719, '75': 4.383, '90': 8.862, '95': 11.522}
- changepoint probability 0.0424, regime age 101.8 min
- agent weights: empirical 0.003, ewma 0.056, garch 0.081, har 0.188, bocpd 0.031, hmm 0.054, online_qr 0.232, lgbm 0.355

## Learning log

- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- HMM volatility states (sd, bp per minute): [3.43, 6.5, 17.71], current probabilities: [0.035, 0.93, 0.035]
- live generator: {'versions': 60, 'latest_effective': '2026-10-26 17:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.346, 'l_abs': 0.726, 'l_hi': 0.811, 'l_lo': 0.794, 'b05': 0.742, 'b25': 0.723, 'b75': 0.672, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.4, 1.937, 2.287, 3.257, 3.046, 2.866, 2.564, 2.276, 2.264, 2.477, 2.541, 2.597, 2.755, 2.746]}
- calibration offsets (in sigma): {'05': -0.015, '10': -0.04, '25': -0.035, '40': -0.07, '50': -0.03, '60': -0.0, '75': -0.015, '90': -0.0, '95': -0.005}
