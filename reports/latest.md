# ETH-USD 60s candle generator - report

- generated: 2026-10-03 20:04 UTC
- last closed candle: 2026-10-03 20:04 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k13_next 0.267 in the last 7 days, -0.102 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.383 in the last 7 days, -0.088 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.547 (95) | 0.528 (670) [0.496, 0.561] | 0.511 (2876) [0.492, 0.530] | 0.511 (2972) [0.493, 0.529] | - | 0.550 (80) | 0.500 | flat -0.007 (noise 0.031) |
| colour_clear | 0.500 (720) | 0.496 (5390) [0.485, 0.504] | 0.496 (23409) [0.491, 0.501] | 0.496 (24238) [0.492, 0.501] | - | 0.525 (613) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | - | - | - | - | - | 0.556 (36) | - | - |
| colour_next | 0.504 (1432) | 0.505 (10008) [0.501, 0.509] | 0.501 (42916) [0.497, 0.504] | 0.501 (44349) [0.497, 0.504] | - | 0.507 (1181) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.497 (20048) | 0.502 (140112) [0.500, 0.505] | 0.501 (600824) [0.500, 0.502] | 0.501 (620886) [0.500, 0.502] | - | 0.493 (16534) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | - | - | - | - | - | 0.700 (10) | - | - |
| reversal_k13_next | 0.241 (58) | 0.267 (592) [0.253, 0.282] | 0.302 (2020) [0.287, 0.319] | 0.300 (2105) [0.285, 0.317] | - | 0.306 (85) | 0.076 | down -0.102 (noise 0.031) |
| reversal_k13_now | 0.615 (52) | 0.581 (341) [0.535, 0.626] | 0.582 (1425) [0.561, 0.603] | 0.581 (1472) [0.561, 0.602] | - | 0.743 (35) | 0.076 | flat -0.043 (noise 0.038) |
| reversal_k3_next | 0.583 (60) | 0.578 (609) [0.544, 0.613] | 0.587 (2357) [0.571, 0.601] | 0.587 (2440) [0.572, 0.602] | - | 0.541 (122) | 0.292 | flat -0.012 (noise 0.030) |
| reversal_k3_now | 0.926 (54) | 0.950 (379) [0.939, 0.962] | 0.942 (1712) [0.933, 0.950] | 0.942 (1763) [0.933, 0.950] | - | 0.933 (45) | 0.292 | flat +0.004 (noise 0.016) |
| reversal_k5_next | 0.483 (120) | 0.474 (498) [0.440, 0.498] | 0.492 (1936) [0.474, 0.510] | 0.494 (1990) [0.477, 0.511] | - | 0.418 (158) | 0.187 | flat -0.055 (noise 0.034) |
| reversal_k5_now | 0.848 (59) | 0.870 (354) [0.850, 0.895] | 0.835 (1570) [0.820, 0.851] | 0.837 (1611) [0.823, 0.852] | - | 0.837 (49) | 0.187 | flat +0.049 (noise 0.026) |
| reversal_k8_next | 0.404 (47) | 0.383 (389) [0.355, 0.410] | 0.399 (2020) [0.381, 0.418] | 0.396 (2106) [0.379, 0.415] | - | 0.369 (65) | 0.121 | down -0.088 (noise 0.035) |
| reversal_k8_now | 0.745 (51) | 0.739 (325) [0.700, 0.776] | 0.712 (1546) [0.692, 0.734] | 0.714 (1587) [0.695, 0.735] | - | 0.795 (39) | 0.121 | flat -0.016 (noise 0.033) |
| overall | 0.499 (22076) | 0.504 (154277) [0.502, 0.506] | 0.503 (661202) [0.502, 0.504] | 0.503 (683281) [0.502, 0.504] | - | 0.496 (18393) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.075, 0.1105] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5301, 'levels': [{'threshold': 0.075, 'calls_per_day': 142.8, 'win_rate': 0.5541}, {'threshold': 0.1105, 'calls_per_day': 35.3, 'win_rate': 0.6265}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 49, 'rate': 0.4694}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15282 | 0.335 | 0.504 (15077) | 0.556 (36) | 0.783 (2347) |
| volatility: normal | 15281 | 0.361 | 0.508 (15217) | - | 0.766 (2107) |
| volatility: wild | 15281 | 0.373 | 0.491 (15236) | - | 0.785 (2147) |
| session: Asia 00-08 | 15360 | 0.352 | 0.499 (15252) | - | 0.782 (2173) |
| session: Europe 08-13 | 9600 | 0.351 | 0.505 (9535) | - | 0.767 (1460) |
| session: US 13-21 | 15304 | 0.365 | 0.500 (15217) | - | 0.782 (2224) |
| session: late 21-24 | 5580 | 0.353 | 0.500 (5526) | - | 0.775 (744) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.300 | 0.276 | 0.236 | 0.236 | 0.571 | 0.274 | 0.326 | 1.439 |
| 6h | 360 | 0.315 | 0.308 | 0.229 | 0.231 | 0.540 | 0.245 | 0.386 | 1.297 |
| 24h | 1440 | 0.319 | 0.315 | 0.241 | 0.259 | 0.505 | 0.229 | 0.409 | 1.210 |
| 7d | 10080 | 0.358 | 0.358 | 0.286 | 0.312 | 0.506 | 0.244 | 0.472 | 1.347 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.309 | 0.501 | 0.245 | 0.466 | 1.281 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.300 / 0.571 / 0.883; 2: 0.242 / 0.411 / 0.867; 3: 0.280 / 0.500 / 0.800; 4: 0.259 / 0.536 / 0.817; 5: 0.240 / 0.393 / 0.850; 6: 0.247 / 0.375 / 0.867; 7: 0.249 / 0.500 / 0.867; 8: 0.243 / 0.411 / 0.883; 9: 0.260 / 0.518 / 0.883; 10: 0.276 / 0.482 / 0.867; 11: 0.245 / 0.464 / 0.883; 12: 0.264 / 0.518 / 0.883; 13: 0.254 / 0.464 / 0.883; 14: 0.285 / 0.518 / 0.900; 15: 0.249 / 0.518 / 0.933
- 6h: 1: 0.315 / 0.540 / 0.864; 2: 0.295 / 0.489 / 0.894; 3: 0.300 / 0.523 / 0.886; 4: 0.306 / 0.551 / 0.875; 5: 0.296 / 0.500 / 0.881; 6: 0.297 / 0.489 / 0.906; 7: 0.288 / 0.466 / 0.903; 8: 0.292 / 0.454 / 0.894; 9: 0.291 / 0.474 / 0.900; 10: 0.305 / 0.534 / 0.897; 11: 0.291 / 0.520 / 0.883; 12: 0.302 / 0.520 / 0.875; 13: 0.307 / 0.526 / 0.856; 14: 0.298 / 0.483 / 0.858; 15: 0.286 / 0.463 / 0.869
- 24h: 1: 0.319 / 0.505 / 0.884; 2: 0.317 / 0.499 / 0.890; 3: 0.317 / 0.495 / 0.888; 4: 0.318 / 0.516 / 0.894; 5: 0.312 / 0.490 / 0.894; 6: 0.311 / 0.476 / 0.892; 7: 0.316 / 0.496 / 0.894; 8: 0.308 / 0.469 / 0.894; 9: 0.311 / 0.486 / 0.897; 10: 0.316 / 0.495 / 0.897; 11: 0.318 / 0.531 / 0.894; 12: 0.317 / 0.501 / 0.892; 13: 0.316 / 0.499 / 0.890; 14: 0.313 / 0.486 / 0.892; 15: 0.306 / 0.468 / 0.893
- 7d: 1: 0.358 / 0.506 / 0.899; 2: 0.352 / 0.490 / 0.900; 3: 0.355 / 0.509 / 0.899; 4: 0.351 / 0.494 / 0.899; 5: 0.352 / 0.508 / 0.899; 6: 0.350 / 0.499 / 0.899; 7: 0.351 / 0.499 / 0.899; 8: 0.350 / 0.505 / 0.899; 9: 0.347 / 0.493 / 0.899; 10: 0.348 / 0.505 / 0.899; 11: 0.348 / 0.505 / 0.899; 12: 0.350 / 0.509 / 0.898; 13: 0.350 / 0.504 / 0.898; 14: 0.347 / 0.496 / 0.898; 15: 0.346 / 0.497 / 0.898
- 30d: 1: 0.356 / 0.501 / 0.899; 2: 0.352 / 0.497 / 0.900; 3: 0.354 / 0.505 / 0.900; 4: 0.351 / 0.500 / 0.900; 5: 0.351 / 0.501 / 0.900; 6: 0.351 / 0.505 / 0.900; 7: 0.350 / 0.506 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.499 / 0.900; 10: 0.348 / 0.504 / 0.900; 11: 0.348 / 0.503 / 0.900; 12: 0.347 / 0.501 / 0.900; 13: 0.346 / 0.500 / 0.900; 14: 0.346 / 0.495 / 0.900; 15: 0.345 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.120 (body 0.109, range 0.130); 'price stays where it was' would score 0.092; colour right 0.482; typical miss of the close 4.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.086 (body 0.059, range 0.113); 'price stays where it was' would score 0.068; colour right 0.497; typical miss of the close 4.1 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.105 (body 0.071, range 0.140); 'price stays where it was' would score 0.102; colour right 0.494; typical miss of the close 4.2 bp; chain ended on the right side 0.537 of 95 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.158); 'price stays where it was' would score 0.117; colour right 0.495; typical miss of the close 7.7 bp; chain ended on the right side 0.524 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.2 bp; chain ended on the right side 0.511 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.4; 2: 0.197 / 4.5; 3: 0.169 / 6.3; 4: 0.133 / 6.5; 5: 0.122 / 7.4; 6: 0.113 / 8.3; 7: 0.101 / 8.7; 8: 0.093 / 9.2; 9: 0.089 / 9.4; 10: 0.084 / 10.3; 11: 0.078 / 10.7; 12: 0.076 / 11.1; 13: 0.068 / 11.5; 14: 0.068 / 11.6; 15: 0.063 / 11.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 88798, probability skill vs chance 0.2319, widened contest next: False
  - now: threshold 0.839, hit rate recent 0.9237 / long run 0.941
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.306, naive rule 0.515, lift 2.94x
    - 24h: 55 calls (55 a day), hit rate 0.909, chance 0.294, naive rule 0.497, lift 3.09x
    - 7d: 381 calls (54 a day), hit rate 0.948, chance 0.288, naive rule 0.483, lift 3.28x
    - 30d: 1708 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5323, hit rate recent 0.5742 / long run 0.5777
    - 6h: 47 calls (191 a day), hit rate 0.596, chance 0.306, lift 1.95x
    - 24h: 138 calls (138 a day), hit rate 0.522, chance 0.294, lift 1.77x
    - 7d: 676 calls (97 a day), hit rate 0.581, chance 0.288, lift 2.02x
    - 30d: 2422 calls (81 a day), hit rate 0.583, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.493; 0.35: 538, 0.518; 0.40: 490, 0.559; 0.45: 423, 0.624; 0.50: 369, 0.679; 0.55: 322, 0.724; 0.60: 275, 0.765; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 140, 0.868; 0.80: 100, 0.906; 0.85: 49, 0.949; 0.90: 1, 0.971
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 496, 0.459; 0.40: 413, 0.487; 0.45: 318, 0.518; 0.50: 209, 0.550; 0.55: 94, 0.585; 0.60: 13, 0.604; 0.65: 0, 0.769
- **K=5**: model 1790208000, labels learned 88796, probability skill vs chance 0.2211, widened contest next: True
  - now: threshold 0.7082, hit rate recent 0.8382 / long run 0.8405
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.197, naive rule 0.399, lift 4.16x
    - 24h: 58 calls (58 a day), hit rate 0.810, chance 0.191, naive rule 0.390, lift 4.25x
    - 7d: 359 calls (51 a day), hit rate 0.861, chance 0.186, naive rule 0.393, lift 4.62x
    - 30d: 1582 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.48x
  - next: threshold 0.3873, hit rate recent 0.4432 / long run 0.4761
    - 6h: 50 calls (204 a day), hit rate 0.460, chance 0.197, lift 2.34x
    - 24h: 185 calls (186 a day), hit rate 0.416, chance 0.191, lift 2.18x
    - 7d: 632 calls (90 a day), hit rate 0.456, chance 0.186, lift 2.44x
    - 30d: 2051 calls (68 a day), hit rate 0.488, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 434, 0.410; 0.35: 374, 0.461; 0.40: 303, 0.529; 0.45: 248, 0.586; 0.50: 193, 0.646; 0.55: 148, 0.696; 0.60: 116, 0.737; 0.65: 88, 0.780; 0.70: 64, 0.818; 0.75: 35, 0.856; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.423; 0.40: 169, 0.447; 0.45: 89, 0.472; 0.50: 23, 0.511; 0.55: 3, 0.573
- **K=8**: model 1790553600, labels learned 88793, probability skill vs chance 0.2024, widened contest next: False
  - now: threshold 0.563, hit rate recent 0.7484 / long run 0.7281
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.114, naive rule 0.331, lift 5.00x
    - 24h: 49 calls (49 a day), hit rate 0.755, chance 0.117, naive rule 0.319, lift 6.47x
    - 7d: 322 calls (46 a day), hit rate 0.736, chance 0.122, naive rule 0.328, lift 6.05x
    - 30d: 1547 calls (52 a day), hit rate 0.718, chance 0.122, naive rule 0.327, lift 5.90x
  - next: threshold 0.3603, hit rate recent 0.3792 / long run 0.4025
    - 6h: 25 calls (103 a day), hit rate 0.360, chance 0.114, lift 3.15x
    - 24h: 71 calls (71 a day), hit rate 0.352, chance 0.117, lift 3.02x
    - 7d: 417 calls (60 a day), hit rate 0.372, chance 0.122, lift 3.06x
    - 30d: 2017 calls (67 a day), hit rate 0.399, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 279, 0.395; 0.35: 210, 0.470; 0.40: 162, 0.535; 0.45: 128, 0.583; 0.50: 98, 0.624; 0.55: 69, 0.678; 0.60: 46, 0.722; 0.65: 25, 0.755; 0.70: 9, 0.800; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 191, 0.342; 0.35: 120, 0.380; 0.40: 50, 0.405; 0.45: 10, 0.421; 0.50: 1, 0.452
- **K=13**: model 1790208000, labels learned 88788, probability skill vs chance 0.1815, widened contest next: False
  - now: threshold 0.4088, hit rate recent 0.6603 / long run 0.5924
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.080, naive rule 0.276, lift 8.96x
    - 24h: 45 calls (45 a day), hit rate 0.689, chance 0.078, naive rule 0.264, lift 8.80x
    - 7d: 340 calls (49 a day), hit rate 0.591, chance 0.078, naive rule 0.264, lift 7.55x
    - 30d: 1423 calls (47 a day), hit rate 0.587, chance 0.076, naive rule 0.266, lift 7.68x
  - next: threshold 0.2691, hit rate recent 0.2784 / long run 0.2936
    - 6h: 31 calls (129 a day), hit rate 0.290, chance 0.080, lift 3.64x
    - 24h: 92 calls (93 a day), hit rate 0.283, chance 0.078, lift 3.61x
    - 7d: 625 calls (89 a day), hit rate 0.270, chance 0.078, lift 3.45x
    - 30d: 1995 calls (67 a day), hit rate 0.306, chance 0.076, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.432; 0.35: 91, 0.490; 0.40: 65, 0.537; 0.45: 45, 0.595; 0.50: 29, 0.614; 0.55: 17, 0.655; 0.60: 7, 0.674; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.315; 0.35: 18, 0.345; 0.40: 4, 0.328; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.605 | 1.48% | 0.883 | 0.567 | 0.250 | 0.482 | -0.031 |
| 6h | 5.054 | 4.18% | 0.872 | 0.508 | 0.250 | 0.523 | 0.330 |
| 24h | 5.916 | 12.51% | 0.890 | 0.502 | 0.251 | 0.496 | 0.472 |
| 7d | 12.882 | 4.08% | 0.900 | 0.500 | 0.251 | 0.497 | 0.668 |
| 30d | 14.414 | 4.18% | 0.900 | 0.500 | 0.251 | 0.499 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 4.674 | 4.617 | 4.652 | 4.641 | 4.738 | 5.012 | 4.601 | 4.655 | 4.613 | 4.605 |
| 6h | 5.275 | 5.106 | 5.094 | 5.092 | 5.227 | 5.449 | 5.033 | 5.060 | 5.045 | 5.054 |
| 24h | 6.762 | 5.958 | 6.078 | 5.954 | 6.087 | 6.310 | 5.927 | 5.914 | 5.916 | 5.916 |
| 7d | 13.430 | 12.984 | 12.962 | 12.893 | 13.127 | 13.042 | 12.874 | 12.870 | 12.858 | 12.882 |
| 30d | 15.042 | 14.551 | 14.503 | 14.439 | 14.694 | 14.630 | 14.421 | 14.387 | 14.386 | 14.414 |

## Next candle

- candle starting 2026-10-03 20:04 UTC, last close 2687.61
- P(up) 0.5032, return quantiles (bp): {'05': -3.876, '10': -2.822, '25': -1.254, '40': -0.478, '50': 0.017, '60': 0.46, '75': 1.494, '90': 2.998, '95': 4.089}
- changepoint probability 0.0919, regime age 92.1 min
- agent weights: empirical 0.003, ewma 0.146, garch 0.089, har 0.150, bocpd 0.039, hmm 0.005, online_qr 0.299, lgbm 0.269

## Learning log

- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.66, 5.39, 13.26], current probabilities: [0.93, 0.069, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 20:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.166, 'l_abs': 0.647, 'l_hi': 0.769, 'l_lo': 0.723, 'b05': 0.65, 'b25': 0.665, 'b75': 0.655, 'b95': 0.661}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.569, 2.215, 2.563, 2.814, 3.089, 3.149, 3.441, 3.584, 3.862, 4.225, 4.164, 4.43, 4.426, 4.5]}
- calibration offsets (in sigma): {'05': -0.0185, '10': 0.033, '25': 0.0975, '40': 0.072, '50': 0.035, '60': -0.012, '75': 0.0225, '90': 0.017, '95': -0.0115}
