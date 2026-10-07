# ETH-USD 60s candle generator - report

- generated: 2026-10-07 20:51 UTC
- last closed candle: 2026-10-07 20:50 UTC (staleness 1.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.524 (670) [0.487, 0.563] | 0.510 (2875) [0.490, 0.530] | 0.515 (3355) [0.497, 0.531] | 0.540 (383) [0.482, 0.599] | 0.373 (83) | 0.500 | flat -0.007 (noise 0.035) |
| colour_clear | 0.523 (776) | 0.520 (5262) [0.498, 0.541] | 0.503 (23269) [0.497, 0.510] | 0.502 (27175) [0.496, 0.508] | 0.547 (2937) [0.534, 0.559] | 0.539 (645) | 0.500 | flat +0.025 (noise 0.013) |
| colour_confident | 0.518 (168) | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.614 (88) | 0.500 | - |
| colour_next | 0.511 (1423) | 0.519 (9981) [0.506, 0.532] | 0.505 (42883) [0.500, 0.510] | 0.504 (50023) [0.499, 0.509] | 0.533 (5674) [0.518, 0.549] | 0.530 (1245) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.498 (19922) | 0.502 (139734) [0.498, 0.506] | 0.501 (600362) [0.500, 0.503] | 0.501 (700322) [0.500, 0.502] | 0.501 (79436) [0.496, 0.506] | 0.491 (17430) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.513 (39) | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.762 (21) | 0.500 | - |
| reversal_k13_next | 0.324 (71) | 0.301 (598) [0.277, 0.324] | 0.308 (2033) [0.293, 0.324] | 0.303 (2437) [0.289, 0.318] | 0.325 (332) [0.306, 0.344] | 0.298 (57) | 0.077 | flat +0.016 (noise 0.028) |
| reversal_k13_now | 0.508 (63) | 0.587 (392) [0.546, 0.634] | 0.583 (1481) [0.560, 0.607] | 0.583 (1713) [0.563, 0.603] | 0.593 (241) [0.534, 0.664] | 0.600 (40) | 0.077 | flat -0.005 (noise 0.039) |
| reversal_k3_next | 0.689 (45) | 0.587 (605) [0.562, 0.621] | 0.586 (2414) [0.570, 0.602] | 0.588 (2802) [0.575, 0.602] | 0.591 (362) [0.563, 0.661] | 0.500 (44) | 0.292 | flat +0.022 (noise 0.032) |
| reversal_k3_now | 0.902 (61) | 0.929 (411) [0.920, 0.939] | 0.939 (1701) [0.930, 0.949] | 0.940 (1993) [0.932, 0.948] | 0.926 (230) [0.912, 0.943] | 0.944 (36) | 0.293 | flat -0.018 (noise 0.017) |
| reversal_k5_next | 0.490 (49) | 0.463 (723) [0.432, 0.495] | 0.486 (2101) [0.466, 0.507] | 0.487 (2387) [0.470, 0.505] | 0.453 (397) [0.424, 0.510] | 0.370 (46) | 0.187 | flat -0.046 (noise 0.036) |
| reversal_k5_now | 0.768 (56) | 0.843 (394) [0.816, 0.866] | 0.837 (1579) [0.822, 0.853] | 0.838 (1841) [0.823, 0.851] | 0.839 (230) [0.795, 0.879] | 0.825 (40) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.416 (89) | 0.400 (495) [0.367, 0.430] | 0.404 (2043) [0.387, 0.423] | 0.398 (2433) [0.383, 0.415] | 0.410 (327) [0.374, 0.448] | 0.317 (82) | 0.122 | flat +0.002 (noise 0.033) |
| reversal_k8_now | 0.651 (66) | 0.734 (376) [0.700, 0.766] | 0.726 (1570) [0.708, 0.745] | 0.718 (1824) [0.699, 0.736] | 0.743 (237) [0.707, 0.781] | 0.702 (47) | 0.122 | flat -0.018 (noise 0.033) |
| overall | 0.501 (21941) | 0.505 (154379) [0.501, 0.509] | 0.504 (661042) [0.502, 0.505] | 0.503 (771130) [0.502, 0.504] | 0.505 (87849) [0.500, 0.512] | 0.493 (19150) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07747, 0.1151] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5329, 'levels': [{'threshold': 0.07747, 'calls_per_day': 143.5, 'win_rate': 0.5951}, {'threshold': 0.1151, 'calls_per_day': 35.6, 'win_rate': 0.6508}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 5787, 'rate': 0.5372}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15297 | 0.335 | 0.514 (15078) | 0.612 (595) | 0.779 (2459) |
| volatility: normal | 15296 | 0.360 | 0.508 (15229) | 0.553 (76) | 0.772 (2150) |
| volatility: wild | 15297 | 0.373 | 0.494 (15250) | 0.688 (32) | 0.776 (2122) |
| session: Asia 00-08 | 15360 | 0.352 | 0.505 (15255) | 0.605 (253) | 0.775 (2200) |
| session: Europe 08-13 | 9600 | 0.349 | 0.502 (9538) | 0.575 (134) | 0.772 (1481) |
| session: US 13-21 | 15350 | 0.365 | 0.505 (15246) | 0.603 (204) | 0.784 (2265) |
| session: late 21-24 | 5580 | 0.351 | 0.510 (5518) | 0.670 (112) | 0.762 (785) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.369 | 0.365 | 0.268 | 0.268 | 0.542 | 0.291 | 0.447 | 1.550 |
| 6h | 360 | 0.373 | 0.375 | 0.298 | 0.336 | 0.521 | 0.264 | 0.482 | 1.409 |
| 24h | 1440 | 0.362 | 0.356 | 0.290 | 0.319 | 0.531 | 0.262 | 0.461 | 1.372 |
| 7d | 10080 | 0.350 | 0.346 | 0.274 | 0.298 | 0.521 | 0.247 | 0.452 | 1.243 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.369 / 0.542 / 0.917; 2: 0.366 / 0.576 / 0.983; 3: 0.379 / 0.593 / 0.950; 4: 0.368 / 0.508 / 0.950; 5: 0.356 / 0.542 / 0.917; 6: 0.335 / 0.458 / 0.883; 7: 0.359 / 0.542 / 0.867; 8: 0.362 / 0.492 / 0.817; 9: 0.346 / 0.424 / 0.817; 10: 0.367 / 0.542 / 0.800; 11: 0.339 / 0.492 / 0.800; 12: 0.354 / 0.458 / 0.817; 13: 0.352 / 0.508 / 0.750; 14: 0.345 / 0.390 / 0.667; 15: 0.372 / 0.492 / 0.583
- 6h: 1: 0.373 / 0.521 / 0.917; 2: 0.370 / 0.507 / 0.956; 3: 0.377 / 0.535 / 0.939; 4: 0.373 / 0.501 / 0.942; 5: 0.365 / 0.507 / 0.925; 6: 0.346 / 0.454 / 0.892; 7: 0.365 / 0.504 / 0.894; 8: 0.365 / 0.490 / 0.861; 9: 0.357 / 0.448 / 0.861; 10: 0.366 / 0.496 / 0.864; 11: 0.364 / 0.504 / 0.858; 12: 0.346 / 0.440 / 0.864; 13: 0.370 / 0.529 / 0.839; 14: 0.361 / 0.482 / 0.808; 15: 0.361 / 0.485 / 0.794
- 24h: 1: 0.362 / 0.531 / 0.906; 2: 0.349 / 0.484 / 0.893; 3: 0.357 / 0.520 / 0.899; 4: 0.350 / 0.509 / 0.898; 5: 0.348 / 0.506 / 0.895; 6: 0.340 / 0.488 / 0.888; 7: 0.343 / 0.481 / 0.899; 8: 0.337 / 0.474 / 0.894; 9: 0.341 / 0.489 / 0.899; 10: 0.342 / 0.499 / 0.887; 11: 0.339 / 0.484 / 0.891; 12: 0.338 / 0.482 / 0.891; 13: 0.339 / 0.498 / 0.883; 14: 0.344 / 0.506 / 0.879; 15: 0.338 / 0.489 / 0.875
- 7d: 1: 0.350 / 0.521 / 0.899; 2: 0.342 / 0.500 / 0.898; 3: 0.345 / 0.512 / 0.900; 4: 0.340 / 0.501 / 0.900; 5: 0.339 / 0.499 / 0.900; 6: 0.337 / 0.495 / 0.900; 7: 0.339 / 0.503 / 0.900; 8: 0.337 / 0.495 / 0.899; 9: 0.334 / 0.490 / 0.900; 10: 0.337 / 0.505 / 0.900; 11: 0.337 / 0.503 / 0.899; 12: 0.338 / 0.508 / 0.899; 13: 0.338 / 0.507 / 0.898; 14: 0.335 / 0.494 / 0.897; 15: 0.334 / 0.492 / 0.897
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.350 / 0.500 / 0.900; 5: 0.350 / 0.501 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.498 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.347 / 0.502 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.345 / 0.495 / 0.899; 15: 0.344 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.137; colour right 0.492; typical miss of the close 6.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.075, range 0.161); 'price stays where it was' would score 0.123; colour right 0.490; typical miss of the close 10.4 bp; chain ended on the right side 0.292 of 24 chains; n=360
- 24h: match 0.109 (body 0.070, range 0.148); 'price stays where it was' would score 0.125; colour right 0.481; typical miss of the close 8.3 bp; chain ended on the right side 0.406 of 96 chains; n=1440
- 7d: match 0.114 (body 0.076, range 0.152); 'price stays where it was' would score 0.120; colour right 0.497; typical miss of the close 6.1 bp; chain ended on the right side 0.509 of 670 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.2; 2: 0.197 / 4.5; 3: 0.167 / 6.1; 4: 0.131 / 6.6; 5: 0.120 / 7.4; 6: 0.110 / 8.2; 7: 0.097 / 8.6; 8: 0.090 / 9.0; 9: 0.085 / 9.2; 10: 0.080 / 10.1; 11: 0.075 / 10.6; 12: 0.072 / 10.9; 13: 0.063 / 11.3; 14: 0.065 / 11.4; 15: 0.061 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 94604, probability skill vs chance 0.2215, widened contest next: False
  - now: threshold 0.8423, hit rate recent 0.9294 / long run 0.9368
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.282, naive rule 0.459, lift 3.15x
    - 24h: 44 calls (44 a day), hit rate 0.955, chance 0.291, naive rule 0.483, lift 3.28x
    - 7d: 405 calls (58 a day), hit rate 0.928, chance 0.293, naive rule 0.489, lift 3.17x
    - 30d: 1691 calls (56 a day), hit rate 0.938, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5621, hit rate recent 0.5878 / long run 0.5861
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.282, lift 1.91x
    - 24h: 50 calls (50 a day), hit rate 0.520, chance 0.291, lift 1.79x
    - 7d: 565 calls (81 a day), hit rate 0.582, chance 0.293, lift 1.99x
    - 30d: 2378 calls (79 a day), hit rate 0.587, chance 0.292, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.494; 0.35: 537, 0.518; 0.40: 487, 0.561; 0.45: 420, 0.628; 0.50: 367, 0.680; 0.55: 322, 0.723; 0.60: 274, 0.766; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 138, 0.871; 0.80: 97, 0.909; 0.85: 48, 0.947; 0.90: 2, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.423; 0.35: 497, 0.458; 0.40: 412, 0.487; 0.45: 315, 0.519; 0.50: 206, 0.552; 0.55: 92, 0.586; 0.60: 13, 0.617; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 94602, probability skill vs chance 0.1988, widened contest next: False
  - now: threshold 0.7144, hit rate recent 0.8305 / long run 0.8388
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.196, naive rule 0.374, lift 4.32x
    - 24h: 50 calls (50 a day), hit rate 0.840, chance 0.190, naive rule 0.392, lift 4.43x
    - 7d: 393 calls (56 a day), hit rate 0.840, chance 0.192, naive rule 0.400, lift 4.38x
    - 30d: 1574 calls (52 a day), hit rate 0.837, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4558, hit rate recent 0.4494 / long run 0.4703
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.196, lift 2.27x
    - 24h: 54 calls (54 a day), hit rate 0.407, chance 0.190, lift 2.15x
    - 7d: 723 calls (103 a day), hit rate 0.462, chance 0.192, lift 2.41x
    - 30d: 2080 calls (69 a day), hit rate 0.488, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.412; 0.35: 368, 0.466; 0.40: 298, 0.536; 0.45: 243, 0.594; 0.50: 189, 0.651; 0.55: 144, 0.699; 0.60: 112, 0.741; 0.65: 86, 0.787; 0.70: 63, 0.821; 0.75: 34, 0.864; 0.80: 9, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.385; 0.35: 253, 0.422; 0.40: 166, 0.449; 0.45: 85, 0.475; 0.50: 21, 0.518; 0.55: 2, 0.592
- **K=8**: model 1791158400, labels learned 94599, probability skill vs chance 0.192, widened contest next: True
  - now: threshold 0.5691, hit rate recent 0.6903 / long run 0.7262
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.120, naive rule 0.281, lift 4.15x
    - 24h: 58 calls (58 a day), hit rate 0.690, chance 0.120, naive rule 0.326, lift 5.76x
    - 7d: 390 calls (56 a day), hit rate 0.733, chance 0.126, naive rule 0.337, lift 5.83x
    - 30d: 1567 calls (52 a day), hit rate 0.727, chance 0.121, naive rule 0.326, lift 5.99x
  - next: threshold 0.3473, hit rate recent 0.3484 / long run 0.3968
    - 6h: 28 calls (116 a day), hit rate 0.286, chance 0.120, lift 2.37x
    - 24h: 93 calls (94 a day), hit rate 0.333, chance 0.120, lift 2.79x
    - 7d: 520 calls (74 a day), hit rate 0.396, chance 0.126, lift 3.15x
    - 30d: 2054 calls (68 a day), hit rate 0.403, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 272, 0.401; 0.35: 205, 0.477; 0.40: 158, 0.538; 0.45: 125, 0.586; 0.50: 96, 0.629; 0.55: 68, 0.685; 0.60: 46, 0.732; 0.65: 24, 0.770; 0.70: 8, 0.810; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.347; 0.35: 115, 0.386; 0.40: 48, 0.415; 0.45: 10, 0.430; 0.50: 1, 0.421
- **K=13**: model 1791072000, labels learned 94594, probability skill vs chance 0.175, widened contest next: False
  - now: threshold 0.4226, hit rate recent 0.5688 / long run 0.5851
    - 6h: 12 calls (50 a day), hit rate 0.500, chance 0.068, naive rule 0.211, lift 7.32x
    - 24h: 49 calls (50 a day), hit rate 0.612, chance 0.080, naive rule 0.283, lift 7.65x
    - 7d: 394 calls (56 a day), hit rate 0.599, chance 0.079, naive rule 0.275, lift 7.60x
    - 30d: 1481 calls (49 a day), hit rate 0.585, chance 0.077, naive rule 0.267, lift 7.62x
  - next: threshold 0.2868, hit rate recent 0.3069 / long run 0.3055
    - 6h: 22 calls (92 a day), hit rate 0.182, chance 0.068, lift 2.66x
    - 24h: 66 calls (67 a day), hit rate 0.333, chance 0.080, lift 4.16x
    - 7d: 561 calls (80 a day), hit rate 0.312, chance 0.079, lift 3.96x
    - 30d: 2030 calls (68 a day), hit rate 0.310, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.439; 0.35: 89, 0.498; 0.40: 64, 0.547; 0.45: 44, 0.605; 0.50: 28, 0.626; 0.55: 15, 0.676; 0.60: 6, 0.701; 0.65: 2, 0.761
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.317; 0.35: 16, 0.353; 0.40: 3, 0.337; 0.45: 1, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.569 | 2.86% | 0.900 | 0.600 | 0.244 | 0.593 | 0.129 |
| 6h | 13.761 | 1.15% | 0.906 | 0.542 | 0.249 | 0.518 | 0.380 |
| 24h | 13.387 | 4.51% | 0.902 | 0.502 | 0.251 | 0.496 | 0.550 |
| 7d | 10.795 | 4.71% | 0.900 | 0.501 | 0.251 | 0.494 | 0.635 |
| 30d | 14.180 | 4.22% | 0.900 | 0.500 | 0.251 | 0.497 | 0.687 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.821 | 8.567 | 8.642 | 8.703 | 8.771 | 8.628 | 8.690 | 8.580 | 8.617 | 8.569 |
| 6h | 13.921 | 13.790 | 13.857 | 13.853 | 14.107 | 13.780 | 13.725 | 13.712 | 13.722 | 13.761 |
| 24h | 14.020 | 13.564 | 13.405 | 13.492 | 13.565 | 13.528 | 13.405 | 13.360 | 13.358 | 13.387 |
| 7d | 11.329 | 10.903 | 10.879 | 10.836 | 11.020 | 10.988 | 10.797 | 10.788 | 10.778 | 10.795 |
| 30d | 14.804 | 14.310 | 14.261 | 14.210 | 14.451 | 14.395 | 14.182 | 14.154 | 14.152 | 14.180 |

## Next candle

- candle starting 2026-10-07 20:50 UTC, last close 2571.33
- P(up) 0.5563, return quantiles (bp): {'05': -4.831, '10': -3.53, '25': -1.526, '40': -0.328, '50': 0.402, '60': 0.876, '75': 1.587, '90': 3.385, '95': 4.314}
- changepoint probability 0.0769, regime age 89.3 min
- agent weights: empirical 0.004, ewma 0.073, garch 0.139, har 0.099, bocpd 0.017, hmm 0.079, online_qr 0.240, lgbm 0.349

## Learning log

- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- HMM volatility states (sd, bp per minute): [1.68, 4.03, 11.85], current probabilities: [0.95, 0.049, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-07 21:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.223, 'l_abs': 0.673, 'l_hi': 0.707, 'l_lo': 0.725, 'b05': 0.682, 'b25': 0.59, 'b75': 0.583, 'b95': 0.603}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.2, 1.8], [1.3, 1.8]], 'cone_width': [1.68, 1.756, 2.073, 2.232, 2.818, 2.651, 3.332, 3.613, 3.741, 4.345, 4.369, 5.137, 5.903, 7.043]}
- calibration offsets (in sigma): {'05': 0.0045, '10': 0.009, '25': 0.0625, '40': 0.076, '50': 0.095, '60': 0.064, '75': -0.0225, '90': -0.059, '95': -0.1145}
