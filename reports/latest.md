# ETH-USD 60s candle generator - report

- generated: 2026-10-07 15:50 UTC
- last closed candle: 2026-10-07 15:50 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.524 (670) [0.487, 0.563] | 0.510 (2875) [0.490, 0.530] | 0.515 (3355) [0.497, 0.531] | 0.540 (383) [0.482, 0.599] | 0.397 (63) | 0.500 | flat -0.007 (noise 0.035) |
| colour_clear | 0.523 (776) | 0.520 (5262) [0.498, 0.541] | 0.503 (23269) [0.497, 0.510] | 0.502 (27175) [0.496, 0.508] | 0.547 (2937) [0.534, 0.559] | 0.533 (501) | 0.500 | flat +0.025 (noise 0.013) |
| colour_confident | 0.518 (168) | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.645 (76) | 0.500 | - |
| colour_next | 0.511 (1423) | 0.519 (9981) [0.506, 0.532] | 0.505 (42883) [0.500, 0.510] | 0.504 (50023) [0.499, 0.509] | 0.533 (5674) [0.518, 0.549] | 0.532 (946) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.498 (19922) | 0.502 (139734) [0.498, 0.506] | 0.501 (600362) [0.500, 0.503] | 0.501 (700322) [0.500, 0.502] | 0.501 (79436) [0.496, 0.506] | 0.492 (13244) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.513 (39) | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.789 (19) | 0.500 | - |
| reversal_k13_next | 0.324 (71) | 0.301 (598) [0.277, 0.324] | 0.308 (2033) [0.293, 0.324] | 0.303 (2437) [0.289, 0.318] | 0.325 (332) [0.306, 0.344] | 0.342 (38) | 0.077 | flat +0.016 (noise 0.028) |
| reversal_k13_now | 0.508 (63) | 0.587 (392) [0.546, 0.634] | 0.583 (1481) [0.560, 0.607] | 0.583 (1713) [0.563, 0.603] | 0.593 (241) [0.534, 0.664] | 0.645 (31) | 0.077 | flat -0.005 (noise 0.039) |
| reversal_k3_next | 0.689 (45) | 0.587 (605) [0.562, 0.621] | 0.586 (2414) [0.570, 0.602] | 0.588 (2802) [0.575, 0.602] | 0.591 (362) [0.563, 0.661] | 0.500 (34) | 0.292 | flat +0.022 (noise 0.032) |
| reversal_k3_now | 0.902 (61) | 0.929 (411) [0.920, 0.939] | 0.939 (1701) [0.930, 0.949] | 0.940 (1993) [0.932, 0.948] | 0.926 (230) [0.912, 0.943] | 0.967 (30) | 0.293 | flat -0.018 (noise 0.017) |
| reversal_k5_next | 0.490 (49) | 0.463 (723) [0.432, 0.495] | 0.486 (2101) [0.466, 0.507] | 0.487 (2387) [0.470, 0.505] | 0.453 (397) [0.424, 0.510] | 0.385 (39) | 0.187 | flat -0.046 (noise 0.036) |
| reversal_k5_now | 0.768 (56) | 0.843 (394) [0.816, 0.866] | 0.837 (1579) [0.822, 0.853] | 0.838 (1841) [0.823, 0.851] | 0.839 (230) [0.795, 0.879] | 0.812 (32) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.416 (89) | 0.400 (495) [0.367, 0.430] | 0.404 (2043) [0.387, 0.423] | 0.398 (2433) [0.383, 0.415] | 0.410 (327) [0.374, 0.448] | 0.339 (59) | 0.122 | flat +0.002 (noise 0.033) |
| reversal_k8_now | 0.651 (66) | 0.734 (376) [0.700, 0.766] | 0.726 (1570) [0.708, 0.745] | 0.718 (1824) [0.699, 0.736] | 0.743 (237) [0.707, 0.781] | 0.789 (38) | 0.122 | flat -0.018 (noise 0.033) |
| overall | 0.501 (21941) | 0.505 (154379) [0.501, 0.509] | 0.504 (661042) [0.502, 0.505] | 0.503 (771130) [0.502, 0.504] | 0.505 (87849) [0.500, 0.512] | 0.496 (14554) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07752, 0.1152] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5334, 'levels': [{'threshold': 0.07752, 'calls_per_day': 142.9, 'win_rate': 0.5941}, {'threshold': 0.1152, 'calls_per_day': 35.6, 'win_rate': 0.6429}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 5488, 'rate': 0.5379}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15197 | 0.334 | 0.514 (14978) | 0.612 (595) | 0.779 (2449) |
| volatility: normal | 15196 | 0.359 | 0.508 (15130) | 0.588 (68) | 0.775 (2132) |
| volatility: wild | 15197 | 0.373 | 0.494 (15150) | - | 0.776 (2118) |
| session: Asia 00-08 | 15360 | 0.352 | 0.505 (15255) | 0.605 (253) | 0.775 (2200) |
| session: Europe 08-13 | 9600 | 0.349 | 0.502 (9538) | 0.575 (134) | 0.772 (1481) |
| session: US 13-21 | 15050 | 0.365 | 0.505 (14947) | 0.615 (192) | 0.786 (2233) |
| session: late 21-24 | 5580 | 0.351 | 0.510 (5518) | 0.670 (112) | 0.762 (785) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.358 | 0.356 | 0.316 | 0.316 | 0.500 | 0.233 | 0.484 | 1.342 |
| 6h | 360 | 0.377 | 0.378 | 0.313 | 0.339 | 0.524 | 0.262 | 0.493 | 1.201 |
| 24h | 1440 | 0.358 | 0.354 | 0.292 | 0.314 | 0.522 | 0.256 | 0.460 | 1.166 |
| 7d | 10080 | 0.350 | 0.347 | 0.274 | 0.298 | 0.520 | 0.247 | 0.453 | 1.243 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.506 | 0.247 | 0.465 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.358 / 0.500 / 0.917; 2: 0.367 / 0.450 / 0.833; 3: 0.406 / 0.633 / 0.900; 4: 0.376 / 0.500 / 0.867; 5: 0.404 / 0.650 / 0.950; 6: 0.352 / 0.433 / 0.983; 7: 0.390 / 0.550 / 1.000; 8: 0.393 / 0.567 / 1.000; 9: 0.350 / 0.400 / 1.000; 10: 0.412 / 0.617 / 1.000; 11: 0.364 / 0.500 / 1.000; 12: 0.362 / 0.500 / 1.000; 13: 0.367 / 0.517 / 1.000; 14: 0.365 / 0.483 / 1.000; 15: 0.346 / 0.483 / 1.000
- 6h: 1: 0.377 / 0.524 / 0.922; 2: 0.347 / 0.401 / 0.775; 3: 0.381 / 0.540 / 0.842; 4: 0.365 / 0.479 / 0.831; 5: 0.376 / 0.543 / 0.881; 6: 0.359 / 0.457 / 0.917; 7: 0.373 / 0.504 / 0.942; 8: 0.363 / 0.496 / 0.956; 9: 0.369 / 0.507 / 0.944; 10: 0.373 / 0.538 / 0.964; 11: 0.359 / 0.496 / 0.933; 12: 0.352 / 0.474 / 0.931; 13: 0.363 / 0.521 / 0.947; 14: 0.365 / 0.526 / 0.975; 15: 0.355 / 0.496 / 0.967
- 24h: 1: 0.358 / 0.522 / 0.907; 2: 0.346 / 0.475 / 0.880; 3: 0.356 / 0.520 / 0.893; 4: 0.349 / 0.506 / 0.888; 5: 0.347 / 0.501 / 0.893; 6: 0.345 / 0.499 / 0.899; 7: 0.341 / 0.477 / 0.903; 8: 0.336 / 0.473 / 0.906; 9: 0.340 / 0.492 / 0.908; 10: 0.342 / 0.501 / 0.905; 11: 0.338 / 0.484 / 0.905; 12: 0.343 / 0.499 / 0.901; 13: 0.337 / 0.499 / 0.903; 14: 0.344 / 0.513 / 0.908; 15: 0.338 / 0.487 / 0.905
- 7d: 1: 0.350 / 0.520 / 0.900; 2: 0.343 / 0.499 / 0.897; 3: 0.345 / 0.511 / 0.899; 4: 0.340 / 0.501 / 0.899; 5: 0.339 / 0.500 / 0.900; 6: 0.338 / 0.496 / 0.900; 7: 0.339 / 0.503 / 0.900; 8: 0.337 / 0.496 / 0.901; 9: 0.334 / 0.492 / 0.902; 10: 0.338 / 0.506 / 0.902; 11: 0.338 / 0.503 / 0.901; 12: 0.339 / 0.510 / 0.901; 13: 0.338 / 0.506 / 0.901; 14: 0.336 / 0.495 / 0.901; 15: 0.335 / 0.493 / 0.901
- 30d: 1: 0.356 / 0.506 / 0.899; 2: 0.351 / 0.497 / 0.899; 3: 0.353 / 0.507 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.349 / 0.505 / 0.901; 8: 0.348 / 0.503 / 0.901; 9: 0.346 / 0.498 / 0.901; 10: 0.347 / 0.505 / 0.901; 11: 0.346 / 0.501 / 0.901; 12: 0.347 / 0.503 / 0.901; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.495 / 0.901; 15: 0.344 / 0.496 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.106 (body 0.068, range 0.143); 'price stays where it was' would score 0.084; colour right 0.467; typical miss of the close 12.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.087, range 0.171); 'price stays where it was' would score 0.131; colour right 0.465; typical miss of the close 11.5 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.106 (body 0.068, range 0.144); 'price stays where it was' would score 0.121; colour right 0.481; typical miss of the close 7.3 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.114 (body 0.076, range 0.153); 'price stays where it was' would score 0.120; colour right 0.497; typical miss of the close 6.1 bp; chain ended on the right side 0.516 of 670 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.509 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.2; 2: 0.198 / 4.4; 3: 0.168 / 6.1; 4: 0.132 / 6.6; 5: 0.121 / 7.3; 6: 0.110 / 8.2; 7: 0.097 / 8.6; 8: 0.090 / 9.0; 9: 0.085 / 9.2; 10: 0.080 / 10.1; 11: 0.075 / 10.6; 12: 0.072 / 10.9; 13: 0.064 / 11.3; 14: 0.066 / 11.4; 15: 0.061 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 94304, probability skill vs chance 0.2247, widened contest next: False
  - now: threshold 0.8422, hit rate recent 0.9389 / long run 0.9379
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.299, naive rule 0.502, lift 3.14x
    - 24h: 49 calls (49 a day), hit rate 0.980, chance 0.300, naive rule 0.499, lift 3.27x
    - 7d: 412 calls (59 a day), hit rate 0.930, chance 0.293, naive rule 0.488, lift 3.17x
    - 30d: 1694 calls (56 a day), hit rate 0.939, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5626, hit rate recent 0.6012 / long run 0.5875
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.299, lift 2.06x
    - 24h: 56 calls (56 a day), hit rate 0.589, chance 0.300, lift 1.96x
    - 7d: 579 calls (83 a day), hit rate 0.573, chance 0.293, lift 1.96x
    - 30d: 2383 calls (79 a day), hit rate 0.587, chance 0.292, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.494; 0.35: 537, 0.518; 0.40: 487, 0.562; 0.45: 420, 0.627; 0.50: 367, 0.680; 0.55: 322, 0.723; 0.60: 275, 0.766; 0.65: 225, 0.803; 0.70: 182, 0.834; 0.75: 139, 0.871; 0.80: 97, 0.909; 0.85: 48, 0.948; 0.90: 2, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.423; 0.35: 497, 0.458; 0.40: 412, 0.488; 0.45: 315, 0.520; 0.50: 206, 0.553; 0.55: 92, 0.586; 0.60: 13, 0.615; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 94302, probability skill vs chance 0.2036, widened contest next: False
  - now: threshold 0.7135, hit rate recent 0.8233 / long run 0.8383
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.195, naive rule 0.437, lift 4.48x
    - 24h: 53 calls (53 a day), hit rate 0.849, chance 0.192, naive rule 0.406, lift 4.42x
    - 7d: 395 calls (56 a day), hit rate 0.841, chance 0.192, naive rule 0.400, lift 4.38x
    - 30d: 1573 calls (52 a day), hit rate 0.837, chance 0.186, naive rule 0.391, lift 4.49x
  - next: threshold 0.4559, hit rate recent 0.4696 / long run 0.4725
    - 6h: 14 calls (57 a day), hit rate 0.643, chance 0.195, lift 3.29x
    - 24h: 57 calls (57 a day), hit rate 0.456, chance 0.192, lift 2.38x
    - 7d: 733 calls (105 a day), hit rate 0.460, chance 0.192, lift 2.40x
    - 30d: 2087 calls (70 a day), hit rate 0.488, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 430, 0.412; 0.35: 369, 0.466; 0.40: 298, 0.536; 0.45: 244, 0.594; 0.50: 190, 0.651; 0.55: 144, 0.699; 0.60: 112, 0.740; 0.65: 86, 0.786; 0.70: 63, 0.821; 0.75: 34, 0.864; 0.80: 9, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 253, 0.422; 0.40: 166, 0.449; 0.45: 85, 0.476; 0.50: 21, 0.520; 0.55: 2, 0.592
- **K=8**: model 1791158400, labels learned 94299, probability skill vs chance 0.2023, widened contest next: False
  - now: threshold 0.5675, hit rate recent 0.7461 / long run 0.7321
    - 6h: 17 calls (70 a day), hit rate 0.824, chance 0.133, naive rule 0.409, lift 6.20x
    - 24h: 61 calls (61 a day), hit rate 0.738, chance 0.116, naive rule 0.330, lift 6.34x
    - 7d: 388 calls (55 a day), hit rate 0.742, chance 0.126, naive rule 0.337, lift 5.90x
    - 30d: 1569 calls (52 a day), hit rate 0.728, chance 0.121, naive rule 0.326, lift 6.01x
  - next: threshold 0.3472, hit rate recent 0.3875 / long run 0.4021
    - 6h: 19 calls (78 a day), hit rate 0.526, chance 0.133, lift 3.96x
    - 24h: 93 calls (94 a day), hit rate 0.355, chance 0.116, lift 3.05x
    - 7d: 508 calls (73 a day), hit rate 0.400, chance 0.126, lift 3.17x
    - 30d: 2048 calls (68 a day), hit rate 0.404, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 273, 0.401; 0.35: 206, 0.476; 0.40: 158, 0.537; 0.45: 125, 0.586; 0.50: 96, 0.629; 0.55: 68, 0.687; 0.60: 46, 0.734; 0.65: 24, 0.774; 0.70: 8, 0.809; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.346; 0.35: 116, 0.386; 0.40: 48, 0.415; 0.45: 10, 0.428; 0.50: 1, 0.421
- **K=13**: model 1791072000, labels learned 94294, probability skill vs chance 0.1835, widened contest next: False
  - now: threshold 0.422, hit rate recent 0.5881 / long run 0.5872
    - 6h: 12 calls (50 a day), hit rate 0.667, chance 0.096, naive rule 0.380, lift 6.97x
    - 24h: 54 calls (55 a day), hit rate 0.611, chance 0.078, naive rule 0.275, lift 7.81x
    - 7d: 393 calls (56 a day), hit rate 0.603, chance 0.079, naive rule 0.274, lift 7.65x
    - 30d: 1482 calls (49 a day), hit rate 0.586, chance 0.077, naive rule 0.267, lift 7.63x
  - next: threshold 0.2835, hit rate recent 0.3447 / long run 0.3085
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.096, lift 6.10x
    - 24h: 67 calls (68 a day), hit rate 0.328, chance 0.078, lift 4.20x
    - 7d: 563 calls (81 a day), hit rate 0.311, chance 0.079, lift 3.94x
    - 30d: 2026 calls (68 a day), hit rate 0.311, chance 0.077, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.439; 0.35: 89, 0.498; 0.40: 64, 0.547; 0.45: 44, 0.605; 0.50: 28, 0.625; 0.55: 15, 0.681; 0.60: 6, 0.705; 0.65: 2, 0.761
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.318; 0.35: 16, 0.352; 0.40: 3, 0.343; 0.45: 1, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.364 | 3.20% | 0.900 | 0.517 | 0.252 | 0.450 | 0.253 |
| 6h | 18.084 | 5.58% | 0.917 | 0.494 | 0.250 | 0.510 | 0.322 |
| 24h | 12.253 | 4.90% | 0.903 | 0.495 | 0.251 | 0.489 | 0.573 |
| 7d | 10.728 | 4.74% | 0.901 | 0.499 | 0.251 | 0.492 | 0.640 |
| 30d | 14.152 | 4.23% | 0.900 | 0.500 | 0.251 | 0.497 | 0.689 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.839 | 14.469 | 14.510 | 14.372 | 14.815 | 14.415 | 14.123 | 14.314 | 14.262 | 14.364 |
| 6h | 19.153 | 18.256 | 18.177 | 18.118 | 18.627 | 18.339 | 18.005 | 18.011 | 18.054 | 18.084 |
| 24h | 12.884 | 12.429 | 12.256 | 12.341 | 12.377 | 12.407 | 12.273 | 12.239 | 12.228 | 12.253 |
| 7d | 11.263 | 10.838 | 10.810 | 10.770 | 10.947 | 10.923 | 10.729 | 10.721 | 10.711 | 10.728 |
| 30d | 14.777 | 14.283 | 14.233 | 14.182 | 14.422 | 14.369 | 14.155 | 14.127 | 14.125 | 14.152 |

## Next candle

- candle starting 2026-10-07 15:50 UTC, last close 2563.32
- P(up) 0.4995, return quantiles (bp): {'05': -7.922, '10': -5.968, '25': -3.218, '40': -1.143, '50': -0.006, '60': 1.141, '75': 2.8, '90': 4.849, '95': 6.78}
- changepoint probability 0.1775, regime age 52.1 min
- agent weights: empirical 0.003, ewma 0.031, garch 0.164, har 0.113, bocpd 0.018, hmm 0.036, online_qr 0.288, lgbm 0.349

## Learning log

- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- HMM volatility states (sd, bp per minute): [1.68, 4.03, 11.85], current probabilities: [0.545, 0.451, 0.004]
- live generator: {'versions': 60, 'latest_effective': '2026-10-07 16:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.252, 'l_abs': 0.663, 'l_hi': 0.71, 'l_lo': 0.722, 'b05': 0.673, 'b25': 0.59, 'b75': 0.591, 'b95': 0.623}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [2.714, 2.324, 2.913, 2.516, 2.401, 2.259, 2.234, 2.422, 2.558, 2.855, 2.988, 2.934, 2.706, 2.921]}
- calibration offsets (in sigma): {'05': -0.0255, '10': -0.061, '25': -0.0575, '40': -0.014, '50': -0.005, '60': 0.014, '75': -0.0025, '90': -0.109, '95': -0.1245}
