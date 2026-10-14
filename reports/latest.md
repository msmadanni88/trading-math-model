# ETH-USD 60s candle generator - report

- generated: 2026-10-14 06:57 UTC
- last closed candle: 2026-10-14 06:57 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.489 (671) [0.448, 0.530] | 0.509 (2875) [0.489, 0.530] | 0.510 (4026) [0.494, 0.526] | 0.508 (1054) [0.473, 0.542] | 0.593 (27) | 0.500 | flat -0.035 (noise 0.034) |
| colour_clear | 0.526 (780) | 0.538 (5463) [0.532, 0.544] | 0.512 (23311) [0.504, 0.520] | 0.508 (32638) [0.502, 0.514] | 0.541 (8400) [0.535, 0.547] | 0.573 (262) | 0.500 | flat +0.018 (noise 0.013) |
| colour_confident | 0.633 (60) | 0.605 (926) [0.583, 0.636] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.556 (18) | 0.500 | flat -0.003 (noise 0.038) |
| colour_next | 0.514 (1433) | 0.523 (9974) [0.519, 0.527] | 0.510 (42868) [0.504, 0.515] | 0.507 (59997) [0.503, 0.512] | 0.527 (15648) [0.521, 0.533] | 0.565 (416) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.504 (20062) | 0.499 (139636) [0.496, 0.501] | 0.501 (600152) [0.500, 0.503] | 0.500 (839958) [0.499, 0.501] | 0.500 (219072) [0.497, 0.502] | 0.510 (5824) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.714 (7) | 0.676 (250) [0.633, 0.740] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.667 (3) | 0.500 | flat +0.043 (noise 0.052) |
| reversal_k13_next | 0.270 (74) | 0.321 (495) [0.299, 0.343] | 0.316 (2093) [0.302, 0.331] | 0.306 (2932) [0.294, 0.319] | 0.323 (827) [0.307, 0.338] | 0.250 (16) | 0.077 | flat +0.020 (noise 0.028) |
| reversal_k13_now | 0.651 (43) | 0.589 (353) [0.560, 0.621] | 0.592 (1488) [0.572, 0.614] | 0.584 (2066) [0.567, 0.601] | 0.591 (594) [0.562, 0.625] | 0.615 (13) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.539 (165) | 0.566 (664) [0.541, 0.592] | 0.585 (2478) [0.570, 0.600] | 0.584 (3466) [0.571, 0.597] | 0.575 (1026) [0.555, 0.599] | 0.613 (31) | 0.293 | flat -0.021 (noise 0.028) |
| reversal_k3_now | 0.977 (44) | 0.926 (417) [0.915, 0.941] | 0.939 (1717) [0.931, 0.947] | 0.937 (2410) [0.930, 0.945] | 0.926 (647) [0.917, 0.936] | 1.000 (13) | 0.293 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.481 (104) | 0.468 (524) [0.440, 0.488] | 0.484 (2110) [0.466, 0.502] | 0.484 (2911) [0.469, 0.500] | 0.462 (921) [0.439, 0.486] | 0.381 (21) | 0.187 | flat +0.004 (noise 0.029) |
| reversal_k5_now | 0.804 (46) | 0.809 (367) [0.784, 0.836] | 0.832 (1586) [0.816, 0.848] | 0.833 (2208) [0.819, 0.846] | 0.821 (597) [0.796, 0.845] | 0.857 (7) | 0.188 | flat -0.033 (noise 0.028) |
| reversal_k8_next | 0.407 (81) | 0.387 (607) [0.363, 0.414] | 0.411 (2117) [0.394, 0.429] | 0.396 (3040) [0.383, 0.410] | 0.395 (934) [0.375, 0.416] | 0.389 (18) | 0.122 | flat -0.013 (noise 0.030) |
| reversal_k8_now | 0.674 (46) | 0.669 (393) [0.639, 0.703] | 0.717 (1590) [0.696, 0.738] | 0.709 (2217) [0.692, 0.726] | 0.697 (630) [0.665, 0.730] | 0.750 (12) | 0.122 | flat -0.065 (noise 0.033) |
| overall | 0.506 (22194) | 0.502 (154101) [0.499, 0.505] | 0.504 (661074) [0.503, 0.505] | 0.503 (925231) [0.502, 0.504] | 0.503 (241950) [0.501, 0.506] | 0.515 (6398) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07668, 0.1188] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.525, 'levels': [{'threshold': 0.07668, 'calls_per_day': 140.4, 'win_rate': 0.6022}, {'threshold': 0.1188, 'calls_per_day': 34.9, 'win_rate': 0.668}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 14927, 'rate': 0.5294}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15019 | 0.334 | 0.519 (14771) | 0.598 (1200) | 0.779 (2413) |
| volatility: normal | 15019 | 0.361 | 0.511 (14956) | 0.609 (258) | 0.775 (2102) |
| volatility: wild | 15019 | 0.374 | 0.501 (14975) | 0.683 (101) | 0.773 (2108) |
| session: Asia 00-08 | 15297 | 0.353 | 0.515 (15189) | 0.604 (566) | 0.777 (2200) |
| session: Europe 08-13 | 9300 | 0.349 | 0.506 (9218) | 0.589 (377) | 0.781 (1423) |
| session: US 13-21 | 14880 | 0.366 | 0.508 (14780) | 0.588 (388) | 0.781 (2165) |
| session: late 21-24 | 5580 | 0.349 | 0.509 (5515) | 0.667 (228) | 0.751 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.357 | 0.368 | 0.305 | 0.305 | 0.467 | 0.234 | 0.480 | 0.974 |
| 6h | 360 | 0.391 | 0.372 | 0.296 | 0.351 | 0.571 | 0.292 | 0.489 | 1.038 |
| 24h | 1440 | 0.372 | 0.363 | 0.291 | 0.324 | 0.525 | 0.263 | 0.481 | 1.082 |
| 7d | 10080 | 0.357 | 0.350 | 0.274 | 0.302 | 0.525 | 0.258 | 0.455 | 1.249 |
| 30d | 43200 | 0.357 | 0.355 | 0.279 | 0.308 | 0.511 | 0.249 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.357 / 0.467 / 0.900; 2: 0.380 / 0.550 / 0.950; 3: 0.378 / 0.500 / 0.917; 4: 0.370 / 0.483 / 0.950; 5: 0.381 / 0.550 / 0.967; 6: 0.381 / 0.517 / 0.983; 7: 0.362 / 0.517 / 0.967; 8: 0.364 / 0.517 / 1.000; 9: 0.386 / 0.550 / 0.983; 10: 0.341 / 0.383 / 0.983; 11: 0.371 / 0.483 / 1.000; 12: 0.351 / 0.400 / 1.000; 13: 0.383 / 0.500 / 1.000; 14: 0.374 / 0.500 / 1.000; 15: 0.361 / 0.517 / 1.000
- 6h: 1: 0.391 / 0.571 / 0.911; 2: 0.379 / 0.526 / 0.939; 3: 0.370 / 0.487 / 0.903; 4: 0.380 / 0.493 / 0.919; 5: 0.377 / 0.535 / 0.919; 6: 0.378 / 0.504 / 0.942; 7: 0.381 / 0.521 / 0.917; 8: 0.364 / 0.476 / 0.969; 9: 0.381 / 0.532 / 0.964; 10: 0.376 / 0.499 / 0.961; 11: 0.369 / 0.490 / 0.967; 12: 0.374 / 0.501 / 0.964; 13: 0.379 / 0.529 / 0.964; 14: 0.374 / 0.515 / 0.953; 15: 0.375 / 0.524 / 0.953
- 24h: 1: 0.372 / 0.525 / 0.906; 2: 0.359 / 0.488 / 0.899; 3: 0.365 / 0.505 / 0.898; 4: 0.366 / 0.504 / 0.897; 5: 0.366 / 0.518 / 0.900; 6: 0.365 / 0.508 / 0.899; 7: 0.367 / 0.507 / 0.902; 8: 0.361 / 0.507 / 0.903; 9: 0.366 / 0.518 / 0.901; 10: 0.363 / 0.503 / 0.899; 11: 0.352 / 0.480 / 0.903; 12: 0.363 / 0.498 / 0.906; 13: 0.363 / 0.510 / 0.915; 14: 0.358 / 0.483 / 0.908; 15: 0.365 / 0.501 / 0.905
- 7d: 1: 0.357 / 0.525 / 0.901; 2: 0.345 / 0.494 / 0.900; 3: 0.349 / 0.513 / 0.900; 4: 0.345 / 0.496 / 0.900; 5: 0.348 / 0.507 / 0.901; 6: 0.344 / 0.497 / 0.902; 7: 0.345 / 0.502 / 0.902; 8: 0.344 / 0.500 / 0.902; 9: 0.342 / 0.494 / 0.902; 10: 0.345 / 0.505 / 0.902; 11: 0.341 / 0.490 / 0.902; 12: 0.343 / 0.499 / 0.901; 13: 0.344 / 0.503 / 0.902; 14: 0.342 / 0.503 / 0.902; 15: 0.344 / 0.499 / 0.901
- 30d: 1: 0.357 / 0.511 / 0.900; 2: 0.351 / 0.498 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.156 (body 0.089, range 0.223); 'price stays where it was' would score 0.175; colour right 0.583; typical miss of the close 5.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.124 (body 0.079, range 0.169); 'price stays where it was' would score 0.158; colour right 0.526; typical miss of the close 7.8 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.124 (body 0.082, range 0.166); 'price stays where it was' would score 0.125; colour right 0.503; typical miss of the close 8.9 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.121 (body 0.082, range 0.160); 'price stays where it was' would score 0.125; colour right 0.495; typical miss of the close 7.1 bp; chain ended on the right side 0.502 of 671 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.124; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.510 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.197 / 4.4; 3: 0.165 / 6.0; 4: 0.133 / 6.7; 5: 0.119 / 7.4; 6: 0.107 / 8.0; 7: 0.101 / 8.4; 8: 0.094 / 8.7; 9: 0.086 / 8.8; 10: 0.081 / 9.6; 11: 0.077 / 10.3; 12: 0.074 / 10.8; 13: 0.062 / 10.9; 14: 0.064 / 11.2; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 103851, probability skill vs chance 0.2279, widened contest next: False
  - now: threshold 0.842, hit rate recent 0.9514 / long run 0.9327
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.301, naive rule 0.491, lift 3.32x
    - 24h: 44 calls (44 a day), hit rate 0.977, chance 0.291, naive rule 0.475, lift 3.35x
    - 7d: 424 calls (61 a day), hit rate 0.927, chance 0.296, naive rule 0.498, lift 3.13x
    - 30d: 1719 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.24x
  - next: threshold 0.5686, hit rate recent 0.5686 / long run 0.5775
    - 6h: 25 calls (101 a day), hit rate 0.600, chance 0.301, lift 1.99x
    - 24h: 154 calls (155 a day), hit rate 0.545, chance 0.291, lift 1.87x
    - 7d: 677 calls (97 a day), hit rate 0.573, chance 0.296, lift 1.94x
    - 30d: 2495 calls (83 a day), hit rate 0.585, chance 0.290, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.490; 0.35: 539, 0.513; 0.40: 485, 0.561; 0.45: 416, 0.629; 0.50: 363, 0.683; 0.55: 318, 0.725; 0.60: 271, 0.769; 0.65: 224, 0.800; 0.70: 180, 0.832; 0.75: 139, 0.871; 0.80: 96, 0.912; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.459; 0.40: 411, 0.488; 0.45: 316, 0.523; 0.50: 205, 0.558; 0.55: 92, 0.583; 0.60: 14, 0.601; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 103849, probability skill vs chance 0.2152, widened contest next: True
  - now: threshold 0.7039, hit rate recent 0.8018 / long run 0.8264
    - 6h: 7 calls (29 a day), hit rate 0.857, chance 0.186, naive rule 0.406, lift 4.62x
    - 24h: 37 calls (37 a day), hit rate 0.838, chance 0.175, naive rule 0.368, lift 4.78x
    - 7d: 367 calls (52 a day), hit rate 0.815, chance 0.189, naive rule 0.404, lift 4.32x
    - 30d: 1586 calls (53 a day), hit rate 0.832, chance 0.187, naive rule 0.392, lift 4.46x
  - next: threshold 0.4314, hit rate recent 0.4405 / long run 0.472
    - 6h: 17 calls (69 a day), hit rate 0.412, chance 0.186, lift 2.22x
    - 24h: 105 calls (106 a day), hit rate 0.457, chance 0.175, lift 2.61x
    - 7d: 525 calls (75 a day), hit rate 0.472, chance 0.189, lift 2.50x
    - 30d: 2116 calls (71 a day), hit rate 0.482, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 425, 0.416; 0.35: 357, 0.478; 0.40: 287, 0.549; 0.45: 236, 0.605; 0.50: 183, 0.658; 0.55: 139, 0.706; 0.60: 109, 0.748; 0.65: 83, 0.790; 0.70: 61, 0.822; 0.75: 33, 0.866; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 251, 0.425; 0.40: 162, 0.453; 0.45: 79, 0.472; 0.50: 19, 0.516; 0.55: 2, 0.577
- **K=8**: model 1791936000, labels learned 103846, probability skill vs chance 0.2094, widened contest next: False
  - now: threshold 0.584, hit rate recent 0.6801 / long run 0.7016
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.134, naive rule 0.350, lift 6.09x
    - 24h: 43 calls (43 a day), hit rate 0.698, chance 0.125, naive rule 0.321, lift 5.57x
    - 7d: 395 calls (56 a day), hit rate 0.671, chance 0.124, naive rule 0.343, lift 5.42x
    - 30d: 1589 calls (53 a day), hit rate 0.715, chance 0.122, naive rule 0.330, lift 5.85x
  - next: threshold 0.3719, hit rate recent 0.3954 / long run 0.3987
    - 6h: 13 calls (53 a day), hit rate 0.462, chance 0.134, lift 3.44x
    - 24h: 80 calls (81 a day), hit rate 0.388, chance 0.125, lift 3.10x
    - 7d: 594 calls (85 a day), hit rate 0.392, chance 0.124, lift 3.17x
    - 30d: 2115 calls (71 a day), hit rate 0.410, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 263, 0.413; 0.35: 199, 0.486; 0.40: 153, 0.547; 0.45: 120, 0.592; 0.50: 92, 0.635; 0.55: 66, 0.686; 0.60: 45, 0.728; 0.65: 24, 0.777; 0.70: 9, 0.835; 0.75: 1, 0.789
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 181, 0.352; 0.35: 109, 0.390; 0.40: 46, 0.423; 0.45: 10, 0.464; 0.50: 1, 0.378
- **K=13**: model 1791849600, labels learned 103841, probability skill vs chance 0.1942, widened contest next: True
  - now: threshold 0.4358, hit rate recent 0.6014 / long run 0.5874
    - 6h: 12 calls (50 a day), hit rate 0.667, chance 0.080, naive rule 0.308, lift 8.36x
    - 24h: 41 calls (41 a day), hit rate 0.634, chance 0.079, naive rule 0.283, lift 8.00x
    - 7d: 356 calls (51 a day), hit rate 0.590, chance 0.079, naive rule 0.286, lift 7.47x
    - 30d: 1488 calls (50 a day), hit rate 0.591, chance 0.078, naive rule 0.273, lift 7.58x
  - next: threshold 0.3002, hit rate recent 0.2757 / long run 0.3114
    - 6h: 9 calls (38 a day), hit rate 0.333, chance 0.080, lift 4.18x
    - 24h: 69 calls (70 a day), hit rate 0.275, chance 0.079, lift 3.47x
    - 7d: 491 calls (70 a day), hit rate 0.320, chance 0.079, lift 4.05x
    - 30d: 2085 calls (70 a day), hit rate 0.316, chance 0.078, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.514; 0.40: 61, 0.566; 0.45: 42, 0.620; 0.50: 26, 0.652; 0.55: 14, 0.712; 0.60: 4, 0.777; 0.65: 1, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.331; 0.35: 14, 0.368; 0.40: 2, 0.417; 0.45: 0, 0.333

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.146 | 2.58% | 0.883 | 0.500 | 0.251 | 0.433 | 0.120 |
| 6h | 12.010 | 0.87% | 0.903 | 0.494 | 0.251 | 0.460 | 0.346 |
| 24h | 14.485 | 2.23% | 0.894 | 0.487 | 0.251 | 0.480 | 0.580 |
| 7d | 12.877 | 4.20% | 0.900 | 0.498 | 0.251 | 0.492 | 0.670 |
| 30d | 14.002 | 4.04% | 0.900 | 0.500 | 0.251 | 0.496 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.414 | 10.148 | 10.164 | 10.146 | 10.263 | 10.303 | 10.082 | 10.067 | 10.121 | 10.146 |
| 6h | 12.115 | 12.051 | 12.068 | 11.995 | 12.135 | 12.101 | 11.983 | 11.991 | 11.992 | 12.010 |
| 24h | 14.816 | 14.582 | 14.587 | 14.481 | 14.756 | 14.629 | 14.456 | 14.450 | 14.453 | 14.485 |
| 7d | 13.441 | 12.989 | 12.964 | 12.909 | 13.136 | 13.065 | 12.875 | 12.841 | 12.856 | 12.877 |
| 30d | 14.592 | 14.126 | 14.087 | 14.030 | 14.263 | 14.200 | 14.000 | 13.974 | 13.976 | 14.002 |

## Next candle

- candle starting 2026-10-14 06:57 UTC, last close 2502.95
- P(up) 0.4946, return quantiles (bp): {'05': -6.165, '10': -4.486, '25': -2.719, '40': -1.042, '50': -0.051, '60': 0.915, '75': 2.537, '90': 4.601, '95': 6.077}
- changepoint probability 0.0412, regime age 162.8 min
- agent weights: empirical 0.017, ewma 0.108, garch 0.121, har 0.164, bocpd 0.045, hmm 0.086, online_qr 0.219, lgbm 0.238

## Learning log

- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.05, 4.75, 12.9], current probabilities: [0.14, 0.847, 0.014]
- live generator: {'versions': 60, 'latest_effective': '2026-10-14 07:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.505, 'l_abs': 0.69, 'l_hi': 0.747, 'l_lo': 0.703, 'b05': 0.751, 'b25': 0.649, 'b75': 0.706, 'b95': 0.724}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.203, 1.767, 1.925, 2.157, 2.186, 2.721, 2.534, 2.64, 3.02, 3.049, 3.322, 3.198, 3.981, 4.047]}
- calibration offsets (in sigma): {'05': 0.018, '10': 0.036, '25': -0.07, '40': -0.026, '50': -0.01, '60': 0.026, '75': 0.06, '90': -0.016, '95': -0.028}
