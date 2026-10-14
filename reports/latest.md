# ETH-USD 60s candle generator - report

- generated: 2026-10-14 23:51 UTC
- last closed candle: 2026-10-14 23:51 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.489 (671) [0.448, 0.530] | 0.509 (2875) [0.489, 0.530] | 0.510 (4026) [0.494, 0.526] | 0.508 (1054) [0.473, 0.542] | 0.484 (95) | 0.500 | flat -0.035 (noise 0.034) |
| colour_clear | 0.526 (780) | 0.538 (5463) [0.532, 0.544] | 0.512 (23311) [0.504, 0.520] | 0.508 (32638) [0.502, 0.514] | 0.541 (8400) [0.535, 0.547] | 0.557 (839) | 0.500 | flat +0.018 (noise 0.013) |
| colour_confident | 0.633 (60) | 0.605 (926) [0.583, 0.636] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.537 (67) | 0.500 | flat -0.003 (noise 0.038) |
| colour_next | 0.514 (1433) | 0.523 (9974) [0.519, 0.527] | 0.510 (42868) [0.504, 0.515] | 0.507 (59997) [0.503, 0.512] | 0.527 (15648) [0.521, 0.533] | 0.541 (1427) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.504 (20062) | 0.499 (139636) [0.496, 0.501] | 0.501 (600152) [0.500, 0.503] | 0.500 (839958) [0.499, 0.501] | 0.500 (219072) [0.497, 0.502] | 0.503 (19978) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.714 (7) | 0.676 (250) [0.633, 0.740] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.462 (13) | 0.500 | flat +0.043 (noise 0.052) |
| reversal_k13_next | 0.270 (74) | 0.321 (495) [0.299, 0.343] | 0.316 (2093) [0.302, 0.331] | 0.306 (2932) [0.294, 0.319] | 0.323 (827) [0.307, 0.338] | 0.244 (45) | 0.077 | flat +0.020 (noise 0.028) |
| reversal_k13_now | 0.651 (43) | 0.589 (353) [0.560, 0.621] | 0.592 (1488) [0.572, 0.614] | 0.584 (2066) [0.567, 0.601] | 0.591 (594) [0.562, 0.625] | 0.548 (42) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.539 (165) | 0.566 (664) [0.541, 0.592] | 0.585 (2478) [0.570, 0.600] | 0.584 (3466) [0.571, 0.597] | 0.575 (1026) [0.555, 0.599] | 0.591 (66) | 0.293 | flat -0.021 (noise 0.028) |
| reversal_k3_now | 0.977 (44) | 0.926 (417) [0.915, 0.941] | 0.939 (1717) [0.931, 0.947] | 0.937 (2410) [0.930, 0.945] | 0.926 (647) [0.917, 0.936] | 0.980 (49) | 0.293 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.481 (104) | 0.468 (524) [0.440, 0.488] | 0.484 (2110) [0.466, 0.502] | 0.484 (2911) [0.469, 0.500] | 0.462 (921) [0.439, 0.486] | 0.543 (94) | 0.187 | flat +0.004 (noise 0.029) |
| reversal_k5_now | 0.804 (46) | 0.809 (367) [0.784, 0.836] | 0.832 (1586) [0.816, 0.848] | 0.833 (2208) [0.819, 0.846] | 0.821 (597) [0.796, 0.845] | 0.849 (33) | 0.188 | flat -0.033 (noise 0.028) |
| reversal_k8_next | 0.407 (81) | 0.387 (607) [0.363, 0.414] | 0.411 (2117) [0.394, 0.429] | 0.396 (3040) [0.383, 0.410] | 0.395 (934) [0.375, 0.416] | 0.386 (57) | 0.122 | flat -0.013 (noise 0.030) |
| reversal_k8_now | 0.674 (46) | 0.669 (393) [0.639, 0.703] | 0.717 (1590) [0.696, 0.738] | 0.709 (2217) [0.692, 0.726] | 0.697 (630) [0.665, 0.730] | 0.725 (40) | 0.122 | flat -0.065 (noise 0.033) |
| overall | 0.506 (22194) | 0.502 (154101) [0.499, 0.505] | 0.504 (661074) [0.503, 0.505] | 0.503 (925231) [0.502, 0.504] | 0.503 (241950) [0.501, 0.506] | 0.507 (21926) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07622, 0.1181] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5249, 'levels': [{'threshold': 0.07622, 'calls_per_day': 142.4, 'win_rate': 0.5929}, {'threshold': 0.1181, 'calls_per_day': 35.9, 'win_rate': 0.6535}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 15938, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15357 | 0.334 | 0.520 (15108) | 0.598 (1222) | 0.777 (2474) |
| volatility: normal | 15358 | 0.361 | 0.511 (15293) | 0.601 (278) | 0.775 (2151) |
| volatility: wild | 15356 | 0.374 | 0.502 (15312) | 0.667 (108) | 0.774 (2117) |
| session: Asia 00-08 | 15360 | 0.353 | 0.515 (15251) | 0.605 (575) | 0.777 (2211) |
| session: Europe 08-13 | 9600 | 0.350 | 0.509 (9517) | 0.582 (407) | 0.778 (1470) |
| session: US 13-21 | 15360 | 0.366 | 0.507 (15259) | 0.583 (396) | 0.781 (2219) |
| session: late 21-24 | 5751 | 0.350 | 0.511 (5686) | 0.670 (230) | 0.753 (842) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.363 | 0.365 | 0.267 | 0.267 | 0.500 | 0.253 | 0.472 | 1.207 |
| 6h | 360 | 0.371 | 0.374 | 0.303 | 0.352 | 0.519 | 0.262 | 0.481 | 1.178 |
| 24h | 1440 | 0.378 | 0.365 | 0.294 | 0.341 | 0.540 | 0.273 | 0.482 | 1.116 |
| 7d | 10080 | 0.357 | 0.350 | 0.274 | 0.304 | 0.526 | 0.259 | 0.456 | 1.240 |
| 30d | 43200 | 0.357 | 0.355 | 0.280 | 0.309 | 0.511 | 0.250 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.363 / 0.500 / 0.917; 2: 0.356 / 0.483 / 0.950; 3: 0.350 / 0.483 / 0.967; 4: 0.355 / 0.483 / 0.967; 5: 0.349 / 0.500 / 0.967; 6: 0.342 / 0.417 / 0.917; 7: 0.393 / 0.683 / 0.983; 8: 0.350 / 0.533 / 0.950; 9: 0.388 / 0.567 / 0.983; 10: 0.336 / 0.500 / 0.983; 11: 0.347 / 0.500 / 0.983; 12: 0.349 / 0.450 / 1.000; 13: 0.325 / 0.400 / 1.000; 14: 0.359 / 0.483 / 0.983; 15: 0.388 / 0.550 / 1.000
- 6h: 1: 0.371 / 0.519 / 0.894; 2: 0.360 / 0.478 / 0.883; 3: 0.371 / 0.525 / 0.886; 4: 0.358 / 0.494 / 0.892; 5: 0.360 / 0.497 / 0.906; 6: 0.362 / 0.489 / 0.897; 7: 0.366 / 0.544 / 0.897; 8: 0.356 / 0.472 / 0.903; 9: 0.366 / 0.492 / 0.919; 10: 0.354 / 0.483 / 0.919; 11: 0.355 / 0.478 / 0.911; 12: 0.356 / 0.467 / 0.925; 13: 0.367 / 0.528 / 0.933; 14: 0.356 / 0.464 / 0.939; 15: 0.371 / 0.519 / 0.939
- 24h: 1: 0.378 / 0.540 / 0.906; 2: 0.364 / 0.499 / 0.903; 3: 0.365 / 0.502 / 0.899; 4: 0.365 / 0.502 / 0.900; 5: 0.363 / 0.509 / 0.900; 6: 0.367 / 0.512 / 0.898; 7: 0.362 / 0.510 / 0.897; 8: 0.358 / 0.479 / 0.897; 9: 0.366 / 0.496 / 0.903; 10: 0.364 / 0.508 / 0.902; 11: 0.362 / 0.501 / 0.903; 12: 0.358 / 0.485 / 0.907; 13: 0.364 / 0.514 / 0.906; 14: 0.360 / 0.494 / 0.909; 15: 0.371 / 0.534 / 0.908
- 7d: 1: 0.357 / 0.526 / 0.901; 2: 0.346 / 0.497 / 0.900; 3: 0.349 / 0.511 / 0.900; 4: 0.345 / 0.497 / 0.900; 5: 0.348 / 0.508 / 0.900; 6: 0.346 / 0.501 / 0.900; 7: 0.345 / 0.502 / 0.901; 8: 0.345 / 0.500 / 0.900; 9: 0.343 / 0.493 / 0.901; 10: 0.346 / 0.505 / 0.901; 11: 0.342 / 0.493 / 0.901; 12: 0.344 / 0.500 / 0.902; 13: 0.344 / 0.502 / 0.902; 14: 0.343 / 0.502 / 0.903; 15: 0.346 / 0.503 / 0.903
- 30d: 1: 0.357 / 0.511 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.182 (body 0.114, range 0.250); 'price stays where it was' would score 0.158; colour right 0.433; typical miss of the close 7.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.115 (body 0.076, range 0.154); 'price stays where it was' would score 0.131; colour right 0.464; typical miss of the close 12.0 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.119 (body 0.078, range 0.159); 'price stays where it was' would score 0.133; colour right 0.494; typical miss of the close 11.0 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.160); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 7.4 bp; chain ended on the right side 0.505 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.512 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.198 / 4.5; 3: 0.164 / 6.1; 4: 0.132 / 6.7; 5: 0.120 / 7.4; 6: 0.108 / 8.0; 7: 0.101 / 8.3; 8: 0.095 / 8.6; 9: 0.086 / 8.8; 10: 0.082 / 9.6; 11: 0.077 / 10.3; 12: 0.075 / 10.7; 13: 0.062 / 10.9; 14: 0.065 / 11.2; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 104865, probability skill vs chance 0.234, widened contest next: False
  - now: threshold 0.8422, hit rate recent 0.9609 / long run 0.935
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.294, naive rule 0.511, lift 3.40x
    - 24h: 49 calls (49 a day), hit rate 0.980, chance 0.291, naive rule 0.488, lift 3.37x
    - 7d: 423 calls (60 a day), hit rate 0.929, chance 0.296, naive rule 0.500, lift 3.14x
    - 30d: 1724 calls (57 a day), hit rate 0.939, chance 0.291, naive rule 0.483, lift 3.23x
  - next: threshold 0.5631, hit rate recent 0.5701 / long run 0.5772
    - 6h: 8 calls (32 a day), hit rate 0.625, chance 0.294, lift 2.12x
    - 24h: 66 calls (66 a day), hit rate 0.591, chance 0.291, lift 2.03x
    - 7d: 676 calls (97 a day), hit rate 0.574, chance 0.296, lift 1.94x
    - 30d: 2478 calls (83 a day), hit rate 0.584, chance 0.291, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.491; 0.35: 539, 0.514; 0.40: 484, 0.562; 0.45: 415, 0.631; 0.50: 362, 0.685; 0.55: 317, 0.728; 0.60: 271, 0.772; 0.65: 224, 0.802; 0.70: 180, 0.834; 0.75: 139, 0.872; 0.80: 96, 0.912; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 497, 0.460; 0.40: 410, 0.490; 0.45: 315, 0.525; 0.50: 204, 0.560; 0.55: 92, 0.582; 0.60: 14, 0.601; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 104863, probability skill vs chance 0.2217, widened contest next: False
  - now: threshold 0.702, hit rate recent 0.824 / long run 0.8273
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.221, naive rule 0.506, lift 4.53x
    - 24h: 33 calls (33 a day), hit rate 0.848, chance 0.190, naive rule 0.418, lift 4.47x
    - 7d: 354 calls (51 a day), hit rate 0.811, chance 0.190, naive rule 0.410, lift 4.27x
    - 30d: 1578 calls (53 a day), hit rate 0.831, chance 0.187, naive rule 0.393, lift 4.44x
  - next: threshold 0.4261, hit rate recent 0.5463 / long run 0.4854
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.221, lift 3.11x
    - 24h: 94 calls (94 a day), hit rate 0.543, chance 0.190, lift 2.86x
    - 7d: 564 calls (81 a day), hit rate 0.489, chance 0.190, lift 2.58x
    - 30d: 2147 calls (72 a day), hit rate 0.489, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.418; 0.35: 356, 0.481; 0.40: 286, 0.553; 0.45: 234, 0.609; 0.50: 183, 0.662; 0.55: 139, 0.708; 0.60: 109, 0.749; 0.65: 82, 0.792; 0.70: 60, 0.822; 0.75: 33, 0.866; 0.80: 10, 0.895
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.390; 0.35: 251, 0.426; 0.40: 162, 0.456; 0.45: 79, 0.476; 0.50: 18, 0.513; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 104860, probability skill vs chance 0.2142, widened contest next: False
  - now: threshold 0.5842, hit rate recent 0.698 / long run 0.7022
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.129, naive rule 0.417, lift 7.00x
    - 24h: 40 calls (40 a day), hit rate 0.725, chance 0.122, naive rule 0.347, lift 5.94x
    - 7d: 374 calls (53 a day), hit rate 0.674, chance 0.124, naive rule 0.348, lift 5.45x
    - 30d: 1579 calls (53 a day), hit rate 0.714, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.3578, hit rate recent 0.3908 / long run 0.3978
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.129, lift 3.46x
    - 24h: 57 calls (57 a day), hit rate 0.386, chance 0.122, lift 3.16x
    - 7d: 571 calls (82 a day), hit rate 0.398, chance 0.124, lift 3.21x
    - 30d: 2107 calls (70 a day), hit rate 0.411, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 262, 0.416; 0.35: 198, 0.490; 0.40: 152, 0.550; 0.45: 120, 0.594; 0.50: 92, 0.636; 0.55: 66, 0.685; 0.60: 45, 0.727; 0.65: 24, 0.778; 0.70: 9, 0.832; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.353; 0.35: 109, 0.390; 0.40: 45, 0.424; 0.45: 9, 0.466; 0.50: 1, 0.371
- **K=13**: model 1791849600, labels learned 104855, probability skill vs chance 0.186, widened contest next: True
  - now: threshold 0.4365, hit rate recent 0.5772 / long run 0.5842
    - 6h: 10 calls (42 a day), hit rate 0.800, chance 0.083, naive rule 0.369, lift 9.68x
    - 24h: 42 calls (42 a day), hit rate 0.548, chance 0.075, naive rule 0.283, lift 7.29x
    - 7d: 346 calls (50 a day), hit rate 0.592, chance 0.079, naive rule 0.289, lift 7.51x
    - 30d: 1481 calls (49 a day), hit rate 0.587, chance 0.078, naive rule 0.273, lift 7.54x
  - next: threshold 0.3013, hit rate recent 0.2635 / long run 0.3081
    - 24h: 46 calls (46 a day), hit rate 0.239, chance 0.075, lift 3.18x
    - 7d: 471 calls (67 a day), hit rate 0.316, chance 0.079, lift 4.01x
    - 30d: 2054 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.513; 0.40: 61, 0.563; 0.45: 41, 0.615; 0.50: 25, 0.649; 0.55: 14, 0.703; 0.60: 4, 0.758; 0.65: 1, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.328; 0.35: 13, 0.370; 0.40: 2, 0.426; 0.45: 0, 0.375

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.280 | -0.21% | 0.883 | 0.500 | 0.251 | 0.517 | 0.240 |
| 6h | 17.151 | 1.19% | 0.875 | 0.497 | 0.250 | 0.519 | 0.381 |
| 24h | 17.139 | 3.93% | 0.899 | 0.499 | 0.251 | 0.478 | 0.563 |
| 7d | 13.450 | 4.31% | 0.900 | 0.499 | 0.251 | 0.491 | 0.678 |
| 30d | 14.006 | 4.05% | 0.900 | 0.500 | 0.251 | 0.496 | 0.686 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.249 | 14.227 | 14.371 | 14.362 | 14.356 | 14.331 | 14.174 | 14.185 | 14.237 | 14.280 |
| 6h | 17.357 | 17.188 | 17.244 | 17.171 | 17.379 | 17.318 | 17.157 | 17.089 | 17.105 | 17.151 |
| 24h | 17.840 | 17.227 | 17.252 | 17.121 | 17.381 | 17.332 | 17.138 | 17.107 | 17.102 | 17.139 |
| 7d | 14.055 | 13.562 | 13.546 | 13.473 | 13.705 | 13.654 | 13.451 | 13.415 | 13.427 | 13.450 |
| 30d | 14.598 | 14.129 | 14.091 | 14.031 | 14.267 | 14.197 | 14.005 | 13.977 | 13.979 | 14.006 |

## Next candle

- candle starting 2026-10-14 23:51 UTC, last close 2418.52
- P(up) 0.4774, return quantiles (bp): {'05': -8.493, '10': -6.109, '25': -3.539, '40': -1.406, '50': -0.269, '60': 0.944, '75': 3.01, '90': 6.478, '95': 8.082}
- changepoint probability 0.0463, regime age 120.5 min
- agent weights: empirical 0.003, ewma 0.123, garch 0.085, har 0.223, bocpd 0.031, hmm 0.040, online_qr 0.204, lgbm 0.291

## Learning log

- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- HMM volatility states (sd, bp per minute): [2.03, 4.75, 13.0], current probabilities: [0.01, 0.968, 0.022]
- live generator: {'versions': 60, 'latest_effective': '2026-10-15 00:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.417, 'l_abs': 0.702, 'l_hi': 0.716, 'l_lo': 0.716, 'b05': 0.747, 'b25': 0.65, 'b75': 0.708, 'b95': 0.752}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.345, 1.684, 1.872, 2.015, 2.302, 2.347, 2.564, 2.516, 2.553, 2.737, 2.592, 2.703, 2.755, 2.746]}
- calibration offsets (in sigma): {'05': 0.005, '10': 0.03, '25': -0.055, '40': -0.03, '50': -0.04, '60': -0.02, '75': 0.005, '90': 0.05, '95': -0.045}
