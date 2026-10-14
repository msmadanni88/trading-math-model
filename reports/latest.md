# ETH-USD 60s candle generator - report

- generated: 2026-10-14 20:58 UTC
- last closed candle: 2026-10-14 20:58 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.489 (671) [0.448, 0.530] | 0.509 (2875) [0.489, 0.530] | 0.510 (4026) [0.494, 0.526] | 0.508 (1054) [0.473, 0.542] | 0.494 (83) | 0.500 | flat -0.035 (noise 0.034) |
| colour_clear | 0.526 (780) | 0.538 (5463) [0.532, 0.544] | 0.512 (23311) [0.504, 0.520] | 0.508 (32638) [0.502, 0.514] | 0.541 (8400) [0.535, 0.547] | 0.554 (743) | 0.500 | flat +0.018 (noise 0.013) |
| colour_confident | 0.633 (60) | 0.605 (926) [0.583, 0.636] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.523 (65) | 0.500 | flat -0.003 (noise 0.038) |
| colour_next | 0.514 (1433) | 0.523 (9974) [0.519, 0.527] | 0.510 (42868) [0.504, 0.515] | 0.507 (59997) [0.503, 0.512] | 0.527 (15648) [0.521, 0.533] | 0.540 (1254) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.504 (20062) | 0.499 (139636) [0.496, 0.501] | 0.501 (600152) [0.500, 0.503] | 0.500 (839958) [0.499, 0.501] | 0.500 (219072) [0.497, 0.502] | 0.503 (17556) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.714 (7) | 0.676 (250) [0.633, 0.740] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.462 (13) | 0.500 | flat +0.043 (noise 0.052) |
| reversal_k13_next | 0.270 (74) | 0.321 (495) [0.299, 0.343] | 0.316 (2093) [0.302, 0.331] | 0.306 (2932) [0.294, 0.319] | 0.323 (827) [0.307, 0.338] | 0.250 (44) | 0.077 | flat +0.020 (noise 0.028) |
| reversal_k13_now | 0.651 (43) | 0.589 (353) [0.560, 0.621] | 0.592 (1488) [0.572, 0.614] | 0.584 (2066) [0.567, 0.601] | 0.591 (594) [0.562, 0.625] | 0.513 (39) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.539 (165) | 0.566 (664) [0.541, 0.592] | 0.585 (2478) [0.570, 0.600] | 0.584 (3466) [0.571, 0.597] | 0.575 (1026) [0.555, 0.599] | 0.600 (65) | 0.293 | flat -0.021 (noise 0.028) |
| reversal_k3_now | 0.977 (44) | 0.926 (417) [0.915, 0.941] | 0.939 (1717) [0.931, 0.947] | 0.937 (2410) [0.930, 0.945] | 0.926 (647) [0.917, 0.936] | 0.978 (46) | 0.293 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.481 (104) | 0.468 (524) [0.440, 0.488] | 0.484 (2110) [0.466, 0.502] | 0.484 (2911) [0.469, 0.500] | 0.462 (921) [0.439, 0.486] | 0.556 (90) | 0.187 | flat +0.004 (noise 0.029) |
| reversal_k5_now | 0.804 (46) | 0.809 (367) [0.784, 0.836] | 0.832 (1586) [0.816, 0.848] | 0.833 (2208) [0.819, 0.846] | 0.821 (597) [0.796, 0.845] | 0.839 (31) | 0.188 | flat -0.033 (noise 0.028) |
| reversal_k8_next | 0.407 (81) | 0.387 (607) [0.363, 0.414] | 0.411 (2117) [0.394, 0.429] | 0.396 (3040) [0.383, 0.410] | 0.395 (934) [0.375, 0.416] | 0.407 (54) | 0.122 | flat -0.013 (noise 0.030) |
| reversal_k8_now | 0.674 (46) | 0.669 (393) [0.639, 0.703] | 0.717 (1590) [0.696, 0.738] | 0.709 (2217) [0.692, 0.726] | 0.697 (630) [0.665, 0.730] | 0.711 (38) | 0.122 | flat -0.065 (noise 0.033) |
| overall | 0.506 (22194) | 0.502 (154101) [0.499, 0.505] | 0.504 (661074) [0.503, 0.505] | 0.503 (925231) [0.502, 0.504] | 0.503 (241950) [0.501, 0.506] | 0.507 (19300) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07622, 0.1181] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5249, 'levels': [{'threshold': 0.07622, 'calls_per_day': 142.4, 'win_rate': 0.5929}, {'threshold': 0.1181, 'calls_per_day': 35.9, 'win_rate': 0.6535}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 15765, 'rate': 0.5293}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15300 | 0.334 | 0.520 (15051) | 0.598 (1220) | 0.778 (2460) |
| volatility: normal | 15299 | 0.361 | 0.510 (15234) | 0.604 (280) | 0.776 (2142) |
| volatility: wild | 15299 | 0.374 | 0.502 (15255) | 0.660 (106) | 0.772 (2130) |
| session: Asia 00-08 | 15360 | 0.353 | 0.515 (15251) | 0.605 (575) | 0.777 (2211) |
| session: Europe 08-13 | 9600 | 0.350 | 0.509 (9517) | 0.582 (407) | 0.778 (1470) |
| session: US 13-21 | 15358 | 0.366 | 0.507 (15257) | 0.583 (396) | 0.781 (2216) |
| session: late 21-24 | 5580 | 0.349 | 0.509 (5515) | 0.667 (228) | 0.751 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.346 | 0.391 | 0.315 | 0.315 | 0.400 | 0.211 | 0.480 | 1.232 |
| 6h | 360 | 0.378 | 0.383 | 0.297 | 0.364 | 0.489 | 0.262 | 0.493 | 1.073 |
| 24h | 1440 | 0.374 | 0.363 | 0.289 | 0.333 | 0.529 | 0.267 | 0.481 | 1.095 |
| 7d | 10080 | 0.357 | 0.349 | 0.273 | 0.303 | 0.524 | 0.258 | 0.455 | 1.239 |
| 30d | 43200 | 0.357 | 0.355 | 0.279 | 0.309 | 0.511 | 0.249 | 0.465 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.346 / 0.400 / 0.900; 2: 0.350 / 0.517 / 0.817; 3: 0.357 / 0.517 / 0.800; 4: 0.334 / 0.517 / 0.850; 5: 0.364 / 0.517 / 0.850; 6: 0.369 / 0.500 / 0.900; 7: 0.328 / 0.483 / 0.917; 8: 0.318 / 0.350 / 0.950; 9: 0.363 / 0.517 / 0.950; 10: 0.319 / 0.350 / 0.933; 11: 0.347 / 0.500 / 0.883; 12: 0.334 / 0.467 / 0.833; 13: 0.370 / 0.583 / 0.883; 14: 0.330 / 0.433 / 0.883; 15: 0.355 / 0.500 / 0.850
- 6h: 1: 0.378 / 0.489 / 0.917; 2: 0.372 / 0.494 / 0.911; 3: 0.382 / 0.517 / 0.889; 4: 0.365 / 0.486 / 0.914; 5: 0.372 / 0.492 / 0.933; 6: 0.380 / 0.522 / 0.947; 7: 0.368 / 0.503 / 0.939; 8: 0.367 / 0.464 / 0.953; 9: 0.388 / 0.525 / 0.953; 10: 0.380 / 0.514 / 0.944; 11: 0.373 / 0.506 / 0.931; 12: 0.369 / 0.478 / 0.933; 13: 0.364 / 0.486 / 0.950; 14: 0.369 / 0.464 / 0.958; 15: 0.385 / 0.522 / 0.956
- 24h: 1: 0.374 / 0.529 / 0.909; 2: 0.361 / 0.499 / 0.899; 3: 0.363 / 0.498 / 0.894; 4: 0.365 / 0.502 / 0.907; 5: 0.364 / 0.511 / 0.906; 6: 0.367 / 0.520 / 0.904; 7: 0.358 / 0.494 / 0.901; 8: 0.357 / 0.478 / 0.902; 9: 0.367 / 0.510 / 0.903; 10: 0.364 / 0.510 / 0.901; 11: 0.360 / 0.495 / 0.898; 12: 0.357 / 0.489 / 0.900; 13: 0.362 / 0.509 / 0.901; 14: 0.360 / 0.501 / 0.903; 15: 0.367 / 0.523 / 0.903
- 7d: 1: 0.357 / 0.524 / 0.901; 2: 0.346 / 0.497 / 0.900; 3: 0.349 / 0.511 / 0.899; 4: 0.345 / 0.496 / 0.900; 5: 0.347 / 0.507 / 0.900; 6: 0.346 / 0.502 / 0.901; 7: 0.344 / 0.500 / 0.900; 8: 0.344 / 0.500 / 0.901; 9: 0.343 / 0.494 / 0.901; 10: 0.345 / 0.505 / 0.901; 11: 0.342 / 0.492 / 0.901; 12: 0.344 / 0.501 / 0.901; 13: 0.344 / 0.501 / 0.902; 14: 0.342 / 0.501 / 0.903; 15: 0.345 / 0.501 / 0.904
- 30d: 1: 0.357 / 0.511 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.139 (body 0.097, range 0.180); 'price stays where it was' would score 0.168; colour right 0.400; typical miss of the close 8.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.146; colour right 0.472; typical miss of the close 12.5 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.120 (body 0.080, range 0.160); 'price stays where it was' would score 0.134; colour right 0.494; typical miss of the close 10.3 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.159); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 7.3 bp; chain ended on the right side 0.504 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.124; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.512 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.0; 2: 0.197 / 4.5; 3: 0.164 / 6.1; 4: 0.132 / 6.7; 5: 0.120 / 7.4; 6: 0.108 / 8.0; 7: 0.100 / 8.3; 8: 0.095 / 8.6; 9: 0.086 / 8.8; 10: 0.082 / 9.6; 11: 0.077 / 10.3; 12: 0.074 / 10.7; 13: 0.062 / 10.9; 14: 0.064 / 11.2; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 104692, probability skill vs chance 0.2323, widened contest next: False
  - now: threshold 0.8422, hit rate recent 0.9589 / long run 0.9347
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.275, naive rule 0.474, lift 3.40x
    - 24h: 53 calls (53 a day), hit rate 0.962, chance 0.292, naive rule 0.485, lift 3.29x
    - 7d: 427 calls (61 a day), hit rate 0.930, chance 0.295, naive rule 0.498, lift 3.15x
    - 30d: 1723 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.482, lift 3.23x
  - next: threshold 0.5631, hit rate recent 0.5798 / long run 0.5782
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.275, lift 2.24x
    - 24h: 74 calls (74 a day), hit rate 0.595, chance 0.292, lift 2.03x
    - 7d: 685 calls (98 a day), hit rate 0.574, chance 0.295, lift 1.94x
    - 30d: 2483 calls (83 a day), hit rate 0.584, chance 0.290, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.491; 0.35: 539, 0.514; 0.40: 484, 0.562; 0.45: 415, 0.631; 0.50: 362, 0.685; 0.55: 318, 0.727; 0.60: 271, 0.771; 0.65: 224, 0.801; 0.70: 180, 0.834; 0.75: 139, 0.871; 0.80: 96, 0.913; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 497, 0.460; 0.40: 410, 0.490; 0.45: 315, 0.525; 0.50: 204, 0.560; 0.55: 92, 0.583; 0.60: 14, 0.601; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 104690, probability skill vs chance 0.2173, widened contest next: False
  - now: threshold 0.702, hit rate recent 0.8179 / long run 0.8267
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.203, naive rule 0.426, lift 4.49x
    - 24h: 37 calls (37 a day), hit rate 0.838, chance 0.185, naive rule 0.401, lift 4.54x
    - 7d: 358 calls (51 a day), hit rate 0.810, chance 0.189, naive rule 0.406, lift 4.29x
    - 30d: 1578 calls (53 a day), hit rate 0.831, chance 0.187, naive rule 0.393, lift 4.44x
  - next: threshold 0.4261, hit rate recent 0.567 / long run 0.487
    - 6h: 27 calls (110 a day), hit rate 0.630, chance 0.203, lift 3.11x
    - 24h: 96 calls (96 a day), hit rate 0.552, chance 0.185, lift 2.99x
    - 7d: 568 calls (81 a day), hit rate 0.489, chance 0.189, lift 2.59x
    - 30d: 2151 calls (72 a day), hit rate 0.489, chance 0.187, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 425, 0.418; 0.35: 356, 0.480; 0.40: 286, 0.551; 0.45: 235, 0.607; 0.50: 183, 0.661; 0.55: 139, 0.706; 0.60: 109, 0.748; 0.65: 82, 0.790; 0.70: 60, 0.822; 0.75: 33, 0.866; 0.80: 9, 0.894
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 251, 0.426; 0.40: 162, 0.456; 0.45: 79, 0.476; 0.50: 19, 0.511; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 104687, probability skill vs chance 0.2111, widened contest next: False
  - now: threshold 0.5842, hit rate recent 0.6877 / long run 0.7012
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.114, naive rule 0.344, lift 7.00x
    - 24h: 46 calls (46 a day), hit rate 0.696, chance 0.125, naive rule 0.340, lift 5.56x
    - 7d: 384 calls (55 a day), hit rate 0.669, chance 0.124, naive rule 0.345, lift 5.41x
    - 30d: 1580 calls (53 a day), hit rate 0.714, chance 0.122, naive rule 0.330, lift 5.84x
  - next: threshold 0.3578, hit rate recent 0.411 / long run 0.3998
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.114, lift 4.71x
    - 24h: 61 calls (61 a day), hit rate 0.393, chance 0.125, lift 3.14x
    - 7d: 579 calls (83 a day), hit rate 0.399, chance 0.124, lift 3.22x
    - 30d: 2112 calls (70 a day), hit rate 0.411, chance 0.122, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 262, 0.414; 0.35: 198, 0.488; 0.40: 152, 0.548; 0.45: 120, 0.592; 0.50: 92, 0.634; 0.55: 66, 0.684; 0.60: 45, 0.726; 0.65: 24, 0.777; 0.70: 9, 0.832; 0.75: 1, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.352; 0.35: 109, 0.390; 0.40: 45, 0.424; 0.45: 9, 0.465; 0.50: 1, 0.378
- **K=13**: model 1791849600, labels learned 104682, probability skill vs chance 0.182, widened contest next: True
  - now: threshold 0.4365, hit rate recent 0.5553 / long run 0.5821
    - 6h: 9 calls (38 a day), hit rate 0.556, chance 0.072, naive rule 0.265, lift 7.67x
    - 24h: 47 calls (47 a day), hit rate 0.511, chance 0.075, naive rule 0.274, lift 6.80x
    - 7d: 352 calls (50 a day), hit rate 0.580, chance 0.079, naive rule 0.285, lift 7.37x
    - 30d: 1481 calls (49 a day), hit rate 0.585, chance 0.078, naive rule 0.272, lift 7.54x
  - next: threshold 0.3013, hit rate recent 0.268 / long run 0.3086
    - 6h: 9 calls (38 a day), hit rate 0.333, chance 0.072, lift 4.60x
    - 24h: 51 calls (52 a day), hit rate 0.235, chance 0.075, lift 3.13x
    - 7d: 481 calls (69 a day), hit rate 0.316, chance 0.079, lift 4.02x
    - 30d: 2063 calls (69 a day), hit rate 0.314, chance 0.078, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.450; 0.35: 85, 0.511; 0.40: 61, 0.562; 0.45: 41, 0.613; 0.50: 25, 0.647; 0.55: 14, 0.702; 0.60: 4, 0.752; 0.65: 1, 0.882
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 13, 0.366; 0.40: 2, 0.420; 0.45: 0, 0.333

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.974 | 2.58% | 0.900 | 0.500 | 0.247 | 0.600 | 0.367 |
| 6h | 19.184 | 4.00% | 0.908 | 0.472 | 0.250 | 0.517 | 0.393 |
| 24h | 16.157 | 4.64% | 0.904 | 0.498 | 0.251 | 0.474 | 0.591 |
| 7d | 13.274 | 4.40% | 0.900 | 0.499 | 0.251 | 0.491 | 0.681 |
| 30d | 14.010 | 4.06% | 0.900 | 0.500 | 0.251 | 0.496 | 0.685 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 20.503 | 20.183 | 20.264 | 20.146 | 20.663 | 20.374 | 20.128 | 20.083 | 20.065 | 19.974 |
| 6h | 19.983 | 19.172 | 19.260 | 19.249 | 19.386 | 19.563 | 19.127 | 19.117 | 19.143 | 19.184 |
| 24h | 16.944 | 16.250 | 16.273 | 16.157 | 16.393 | 16.354 | 16.156 | 16.141 | 16.131 | 16.157 |
| 7d | 13.884 | 13.386 | 13.369 | 13.297 | 13.528 | 13.477 | 13.275 | 13.241 | 13.252 | 13.274 |
| 30d | 14.603 | 14.133 | 14.095 | 14.037 | 14.271 | 14.203 | 14.010 | 13.982 | 13.984 | 14.010 |

## Next candle

- candle starting 2026-10-14 20:58 UTC, last close 2414.07
- P(up) 0.4742, return quantiles (bp): {'05': -15.589, '10': -11.216, '25': -6.557, '40': -2.916, '50': -0.694, '60': 2.024, '75': 5.595, '90': 11.44, '95': 14.751}
- changepoint probability 0.0251, regime age 28.0 min
- agent weights: empirical 0.003, ewma 0.128, garch 0.078, har 0.234, bocpd 0.029, hmm 0.033, online_qr 0.230, lgbm 0.265

## Learning log

- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- HMM volatility states (sd, bp per minute): [2.03, 4.75, 13.0], current probabilities: [0.0, 0.096, 0.904]
- live generator: {'versions': 60, 'latest_effective': '2026-10-14 21:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.404, 'l_abs': 0.698, 'l_hi': 0.734, 'l_lo': 0.717, 'b05': 0.76, 'b25': 0.633, 'b75': 0.718, 'b95': 0.751}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.496, 2.029, 1.922, 2.153, 2.181, 2.408, 2.529, 2.797, 2.954, 3.363, 3.45, 3.389, 3.386, 3.442]}
- calibration offsets (in sigma): {'05': 0.0685, '10': 0.037, '25': -0.0875, '40': -0.092, '50': -0.095, '60': -0.028, '75': -0.0425, '90': 0.003, '95': -0.0585}
