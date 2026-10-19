# ETH-USD 60s candle generator - report

- generated: 2026-10-19 23:11 UTC
- last closed candle: 2026-10-19 23:11 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.527 (672) [0.495, 0.561] | 0.522 (2875) [0.504, 0.542] | 0.512 (4506) [0.497, 0.527] | 0.514 (1534) [0.486, 0.543] | 0.598 (92) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.555 (785) | 0.545 (5567) [0.537, 0.555] | 0.522 (23331) [0.514, 0.530] | 0.513 (36607) [0.506, 0.519] | 0.544 (12369) [0.539, 0.550] | 0.565 (779) | 0.500 | flat +0.004 (noise 0.009) |
| colour_confident | 0.568 (139) | 0.584 (630) [0.568, 0.603] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.693 (137) | 0.500 | flat -0.018 (noise 0.025) |
| colour_next | 0.520 (1430) | 0.526 (10017) [0.519, 0.534] | 0.515 (42854) [0.509, 0.520] | 0.510 (67147) [0.505, 0.514] | 0.528 (22798) [0.523, 0.533] | 0.552 (1387) | 0.500 | flat -0.001 (noise 0.007) |
| colour_path | 0.504 (20020) | 0.502 (140238) [0.499, 0.505] | 0.501 (599956) [0.500, 0.503] | 0.501 (940058) [0.500, 0.502] | 0.500 (319172) [0.498, 0.503] | 0.501 (19418) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.583 (36) | 0.616 (138) [0.574, 0.680] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.629 (35) | 0.500 | flat -0.044 (noise 0.050) |
| reversal_k13_next | 0.309 (81) | 0.296 (433) [0.281, 0.310] | 0.312 (2060) [0.298, 0.327] | 0.306 (3218) [0.294, 0.318] | 0.318 (1113) [0.305, 0.330] | 0.317 (82) | 0.077 | flat -0.034 (noise 0.030) |
| reversal_k13_now | 0.469 (64) | 0.543 (381) [0.510, 0.582] | 0.584 (1534) [0.564, 0.605] | 0.577 (2349) [0.561, 0.595] | 0.571 (877) [0.548, 0.599] | 0.480 (50) | 0.077 | flat -0.029 (noise 0.036) |
| reversal_k3_next | 0.584 (101) | 0.566 (737) [0.555, 0.578] | 0.578 (2604) [0.565, 0.592] | 0.582 (3964) [0.572, 0.594] | 0.574 (1524) [0.560, 0.590] | 0.540 (113) | 0.293 | flat -0.026 (noise 0.028) |
| reversal_k3_now | 0.946 (55) | 0.938 (373) [0.913, 0.964] | 0.938 (1718) [0.929, 0.947] | 0.937 (2681) [0.931, 0.945] | 0.929 (918) [0.918, 0.941] | 0.942 (52) | 0.293 | flat +0.016 (noise 0.018) |
| reversal_k5_next | 0.434 (152) | 0.458 (799) [0.439, 0.484] | 0.472 (2424) [0.457, 0.489] | 0.478 (3519) [0.464, 0.492] | 0.457 (1529) [0.440, 0.477] | 0.432 (139) | 0.187 | flat -0.012 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.810 (348) [0.784, 0.838] | 0.832 (1608) [0.816, 0.847] | 0.832 (2457) [0.819, 0.844] | 0.820 (846) [0.800, 0.840] | 0.843 (51) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k8_next | 0.393 (117) | 0.378 (667) [0.348, 0.403] | 0.400 (2238) [0.381, 0.419] | 0.391 (3547) [0.379, 0.405] | 0.385 (1441) [0.365, 0.404] | 0.330 (112) | 0.121 | flat -0.003 (noise 0.027) |
| reversal_k8_now | 0.651 (43) | 0.681 (335) [0.657, 0.706] | 0.719 (1571) [0.698, 0.739] | 0.707 (2450) [0.691, 0.723] | 0.695 (863) [0.670, 0.721] | 0.578 (45) | 0.122 | flat -0.004 (noise 0.034) |
| overall | 0.506 (22206) | 0.505 (155000) [0.502, 0.507] | 0.504 (661442) [0.503, 0.505] | 0.503 (1035896) [0.502, 0.504] | 0.504 (352615) [0.502, 0.506] | 0.505 (21541) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06498, 0.09758] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.529, 'levels': [{'threshold': 0.06498, 'calls_per_day': 144.0, 'win_rate': 0.572}, {'threshold': 0.09758, 'calls_per_day': 35.8, 'win_rate': 0.623}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 23047, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15344 | 0.336 | 0.523 (15096) | 0.592 (1444) | 0.771 (2514) |
| volatility: normal | 15343 | 0.363 | 0.517 (15276) | 0.624 (527) | 0.766 (2253) |
| volatility: wild | 15344 | 0.378 | 0.509 (15301) | 0.648 (216) | 0.772 (2084) |
| session: Asia 00-08 | 15360 | 0.357 | 0.521 (15256) | 0.612 (804) | 0.770 (2288) |
| session: Europe 08-13 | 9600 | 0.353 | 0.516 (9514) | 0.586 (555) | 0.773 (1496) |
| session: US 13-21 | 15360 | 0.367 | 0.512 (15256) | 0.591 (523) | 0.773 (2232) |
| session: late 21-24 | 5711 | 0.350 | 0.515 (5647) | 0.649 (305) | 0.751 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.347 | 0.383 | 0.279 | 0.279 | 0.450 | 0.225 | 0.470 | 1.206 |
| 6h | 360 | 0.358 | 0.368 | 0.284 | 0.318 | 0.514 | 0.247 | 0.469 | 1.191 |
| 24h | 1440 | 0.375 | 0.368 | 0.274 | 0.309 | 0.555 | 0.271 | 0.478 | 1.181 |
| 7d | 10080 | 0.369 | 0.359 | 0.279 | 0.312 | 0.530 | 0.264 | 0.473 | 1.219 |
| 30d | 43200 | 0.359 | 0.355 | 0.279 | 0.308 | 0.517 | 0.253 | 0.465 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.347 / 0.450 / 0.917; 2: 0.353 / 0.517 / 0.883; 3: 0.383 / 0.550 / 0.850; 4: 0.336 / 0.517 / 0.833; 5: 0.367 / 0.550 / 0.883; 6: 0.354 / 0.450 / 0.933; 7: 0.340 / 0.467 / 0.917; 8: 0.402 / 0.683 / 0.950; 9: 0.370 / 0.600 / 0.983; 10: 0.362 / 0.467 / 0.917; 11: 0.337 / 0.500 / 0.900; 12: 0.334 / 0.500 / 0.917; 13: 0.331 / 0.483 / 0.867; 14: 0.337 / 0.500 / 0.917; 15: 0.353 / 0.483 / 0.867
- 6h: 1: 0.358 / 0.514 / 0.917; 2: 0.361 / 0.522 / 0.936; 3: 0.363 / 0.514 / 0.903; 4: 0.343 / 0.478 / 0.889; 5: 0.336 / 0.439 / 0.931; 6: 0.351 / 0.475 / 0.956; 7: 0.341 / 0.483 / 0.939; 8: 0.366 / 0.561 / 0.958; 9: 0.357 / 0.494 / 0.972; 10: 0.363 / 0.528 / 0.953; 11: 0.353 / 0.511 / 0.947; 12: 0.353 / 0.517 / 0.956; 13: 0.349 / 0.486 / 0.944; 14: 0.358 / 0.514 / 0.972; 15: 0.341 / 0.458 / 0.953
- 24h: 1: 0.375 / 0.555 / 0.907; 2: 0.361 / 0.495 / 0.901; 3: 0.363 / 0.506 / 0.898; 4: 0.349 / 0.472 / 0.900; 5: 0.357 / 0.494 / 0.906; 6: 0.360 / 0.506 / 0.908; 7: 0.349 / 0.478 / 0.905; 8: 0.360 / 0.514 / 0.907; 9: 0.359 / 0.510 / 0.909; 10: 0.362 / 0.522 / 0.911; 11: 0.358 / 0.513 / 0.910; 12: 0.357 / 0.515 / 0.911; 13: 0.354 / 0.492 / 0.910; 14: 0.359 / 0.513 / 0.911; 15: 0.351 / 0.490 / 0.915
- 7d: 1: 0.369 / 0.530 / 0.902; 2: 0.355 / 0.491 / 0.902; 3: 0.360 / 0.507 / 0.902; 4: 0.355 / 0.497 / 0.902; 5: 0.356 / 0.501 / 0.903; 6: 0.356 / 0.505 / 0.903; 7: 0.354 / 0.499 / 0.904; 8: 0.354 / 0.500 / 0.903; 9: 0.354 / 0.503 / 0.903; 10: 0.356 / 0.509 / 0.903; 11: 0.350 / 0.497 / 0.903; 12: 0.354 / 0.505 / 0.904; 13: 0.353 / 0.504 / 0.904; 14: 0.352 / 0.505 / 0.904; 15: 0.354 / 0.505 / 0.904
- 30d: 1: 0.359 / 0.517 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.349 / 0.497 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.502 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.348 / 0.504 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.130 (body 0.087, range 0.174); 'price stays where it was' would score 0.159; colour right 0.567; typical miss of the close 6.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.119 (body 0.076, range 0.162); 'price stays where it was' would score 0.108; colour right 0.533; typical miss of the close 7.7 bp; chain ended on the right side 0.792 of 24 chains; n=360
- 24h: match 0.130 (body 0.086, range 0.174); 'price stays where it was' would score 0.133; colour right 0.492; typical miss of the close 9.0 bp; chain ended on the right side 0.615 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.167); 'price stays where it was' would score 0.132; colour right 0.498; typical miss of the close 9.3 bp; chain ended on the right side 0.534 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.525 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.196 / 4.5; 3: 0.163 / 6.1; 4: 0.132 / 6.6; 5: 0.121 / 7.2; 6: 0.109 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.076 / 10.2; 13: 0.065 / 10.5; 14: 0.066 / 10.6; 15: 0.058 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 112025, probability skill vs chance 0.2183, widened contest next: False
  - now: threshold 0.8348, hit rate recent 0.9365 / long run 0.9336
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.245, naive rule 0.416, lift 4.08x
    - 24h: 52 calls (52 a day), hit rate 0.942, chance 0.276, naive rule 0.456, lift 3.41x
    - 7d: 368 calls (53 a day), hit rate 0.943, chance 0.288, naive rule 0.479, lift 3.27x
    - 30d: 1704 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5332, hit rate recent 0.558 / long run 0.5677
    - 6h: 27 calls (110 a day), hit rate 0.556, chance 0.245, lift 2.27x
    - 24h: 115 calls (115 a day), hit rate 0.539, chance 0.276, lift 1.95x
    - 7d: 777 calls (111 a day), hit rate 0.561, chance 0.288, lift 1.95x
    - 30d: 2618 calls (87 a day), hit rate 0.575, chance 0.291, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 483, 0.566; 0.45: 413, 0.635; 0.50: 360, 0.687; 0.55: 315, 0.729; 0.60: 269, 0.773; 0.65: 224, 0.801; 0.70: 178, 0.834; 0.75: 138, 0.870; 0.80: 94, 0.912; 0.85: 48, 0.952; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.424; 0.35: 499, 0.459; 0.40: 407, 0.490; 0.45: 311, 0.522; 0.50: 202, 0.554; 0.55: 91, 0.573; 0.60: 14, 0.606; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 112023, probability skill vs chance 0.208, widened contest next: False
  - now: threshold 0.6827, hit rate recent 0.8238 / long run 0.8252
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.160, naive rule 0.326, lift 5.21x
    - 24h: 52 calls (52 a day), hit rate 0.846, chance 0.177, naive rule 0.374, lift 4.77x
    - 7d: 347 calls (50 a day), hit rate 0.821, chance 0.185, naive rule 0.394, lift 4.45x
    - 30d: 1602 calls (53 a day), hit rate 0.829, chance 0.187, naive rule 0.393, lift 4.44x
  - next: threshold 0.4038, hit rate recent 0.4265 / long run 0.4508
    - 6h: 30 calls (122 a day), hit rate 0.400, chance 0.160, lift 2.50x
    - 24h: 141 calls (142 a day), hit rate 0.433, chance 0.177, lift 2.44x
    - 7d: 852 calls (122 a day), hit rate 0.452, chance 0.185, lift 2.45x
    - 30d: 2469 calls (82 a day), hit rate 0.470, chance 0.187, lift 2.51x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.421; 0.35: 348, 0.486; 0.40: 280, 0.557; 0.45: 228, 0.614; 0.50: 180, 0.663; 0.55: 137, 0.708; 0.60: 107, 0.748; 0.65: 80, 0.790; 0.70: 58, 0.823; 0.75: 32, 0.867; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 250, 0.419; 0.40: 158, 0.446; 0.45: 74, 0.460; 0.50: 18, 0.499; 0.55: 2, 0.549
- **K=8**: model 1791936000, labels learned 112020, probability skill vs chance 0.1852, widened contest next: True
  - now: threshold 0.5696, hit rate recent 0.6226 / long run 0.6887
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.103, naive rule 0.261, lift 5.98x
    - 24h: 46 calls (46 a day), hit rate 0.587, chance 0.115, naive rule 0.309, lift 5.10x
    - 7d: 325 calls (46 a day), hit rate 0.671, chance 0.118, naive rule 0.320, lift 5.66x
    - 30d: 1563 calls (52 a day), hit rate 0.711, chance 0.122, naive rule 0.329, lift 5.83x
  - next: threshold 0.3418, hit rate recent 0.3032 / long run 0.3707
    - 6h: 25 calls (103 a day), hit rate 0.240, chance 0.103, lift 2.33x
    - 24h: 114 calls (115 a day), hit rate 0.333, chance 0.115, lift 2.90x
    - 7d: 701 calls (100 a day), hit rate 0.364, chance 0.118, lift 3.07x
    - 30d: 2287 calls (76 a day), hit rate 0.393, chance 0.122, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.420; 0.35: 194, 0.491; 0.40: 148, 0.549; 0.45: 116, 0.591; 0.50: 89, 0.632; 0.55: 65, 0.681; 0.60: 43, 0.727; 0.65: 24, 0.788; 0.70: 9, 0.836; 0.75: 1, 0.786
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.352; 0.35: 104, 0.382; 0.40: 41, 0.411; 0.45: 9, 0.440; 0.50: 1, 0.471
- **K=13**: model 1792022400, labels learned 112015, probability skill vs chance 0.1802, widened contest next: True
  - now: threshold 0.413, hit rate recent 0.4806 / long run 0.558
    - 6h: 16 calls (67 a day), hit rate 0.375, chance 0.087, naive rule 0.279, lift 4.31x
    - 24h: 51 calls (52 a day), hit rate 0.490, chance 0.078, naive rule 0.276, lift 6.29x
    - 7d: 377 calls (54 a day), hit rate 0.536, chance 0.076, naive rule 0.272, lift 7.02x
    - 30d: 1546 calls (52 a day), hit rate 0.578, chance 0.078, naive rule 0.273, lift 7.42x
  - next: threshold 0.2768, hit rate recent 0.3099 / long run 0.3105
    - 6h: 19 calls (79 a day), hit rate 0.368, chance 0.087, lift 4.24x
    - 24h: 84 calls (85 a day), hit rate 0.321, chance 0.078, lift 4.13x
    - 7d: 444 calls (64 a day), hit rate 0.300, chance 0.076, lift 3.92x
    - 30d: 2092 calls (70 a day), hit rate 0.309, chance 0.078, lift 3.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.451; 0.35: 85, 0.508; 0.40: 61, 0.557; 0.45: 41, 0.614; 0.50: 25, 0.659; 0.55: 14, 0.712; 0.60: 5, 0.750; 0.65: 1, 0.828
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.322; 0.35: 13, 0.355; 0.40: 2, 0.419; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.780 | 6.01% | 0.917 | 0.533 | 0.246 | 0.583 | 0.318 |
| 6h | 12.845 | 2.72% | 0.914 | 0.506 | 0.249 | 0.536 | 0.486 |
| 24h | 15.336 | 2.74% | 0.906 | 0.499 | 0.250 | 0.510 | 0.595 |
| 7d | 16.239 | 4.19% | 0.901 | 0.501 | 0.251 | 0.494 | 0.645 |
| 30d | 13.797 | 4.04% | 0.900 | 0.500 | 0.251 | 0.496 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.405 | 9.975 | 9.931 | 9.910 | 10.287 | 10.008 | 9.784 | 9.779 | 9.810 | 9.780 |
| 6h | 13.204 | 12.973 | 12.980 | 12.927 | 13.125 | 13.030 | 12.847 | 12.842 | 12.854 | 12.845 |
| 24h | 15.768 | 15.514 | 15.492 | 15.369 | 15.692 | 15.561 | 15.316 | 15.314 | 15.325 | 15.336 |
| 7d | 16.949 | 16.429 | 16.344 | 16.255 | 16.517 | 16.448 | 16.240 | 16.218 | 16.209 | 16.239 |
| 30d | 14.378 | 13.923 | 13.885 | 13.822 | 14.046 | 13.985 | 13.794 | 13.771 | 13.772 | 13.797 |

## Next candle

- candle starting 2026-10-19 23:11 UTC, last close 2403.69
- P(up) 0.4692, return quantiles (bp): {'05': -5.986, '10': -4.658, '25': -2.405, '40': -1.17, '50': -0.317, '60': 0.727, '75': 2.404, '90': 4.772, '95': 6.554}
- changepoint probability 0.0472, regime age 79.5 min
- agent weights: empirical 0.007, ewma 0.064, garch 0.081, har 0.195, bocpd 0.016, hmm 0.049, online_qr 0.291, lgbm 0.296

## Learning log

- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- HMM volatility states (sd, bp per minute): [3.26, 6.11, 16.29], current probabilities: [0.935, 0.064, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-19 23:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.334, 'l_abs': 0.728, 'l_hi': 0.766, 'l_lo': 0.751, 'b05': 0.719, 'b25': 0.744, 'b75': 0.678, 'b95': 0.687}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.345, 1.899, 2.111, 2.183, 2.396, 2.646, 2.778, 2.952, 2.937, 3.277, 3.43, 3.649, 3.719, 3.633]}
- calibration offsets (in sigma): {'05': 0.115, '10': 0.04, '25': 0.005, '40': -0.06, '50': -0.07, '60': -0.05, '75': -0.005, '90': -0.04, '95': -0.025}
