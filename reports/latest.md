# ETH-USD 60s candle generator - report

- generated: 2026-10-03 18:56 UTC
- last closed candle: 2026-10-03 18:56 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 18:36 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k13_next 0.267 in the last 7 days, -0.102 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.383 in the last 7 days, -0.088 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.547 (95) | 0.528 (670) [0.496, 0.561] | 0.511 (2876) [0.492, 0.530] | 0.511 (2972) [0.493, 0.529] | - | 0.560 (75) | 0.500 | flat -0.007 (noise 0.031) |
| colour_clear | 0.500 (720) | 0.496 (5390) [0.485, 0.504] | 0.496 (23409) [0.491, 0.501] | 0.496 (24238) [0.492, 0.501] | - | 0.517 (582) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | - | - | - | - | - | 0.536 (28) | - | - |
| colour_next | 0.504 (1432) | 0.505 (10008) [0.501, 0.509] | 0.501 (42916) [0.497, 0.504] | 0.501 (44349) [0.497, 0.504] | - | 0.505 (1117) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.497 (20048) | 0.502 (140112) [0.500, 0.505] | 0.501 (600824) [0.500, 0.502] | 0.501 (620886) [0.500, 0.502] | - | 0.494 (15638) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | - | - | - | - | - | 0.667 (6) | - | - |
| reversal_k13_next | 0.241 (58) | 0.267 (592) [0.253, 0.282] | 0.302 (2020) [0.287, 0.319] | 0.300 (2105) [0.285, 0.317] | - | 0.312 (80) | 0.076 | down -0.102 (noise 0.031) |
| reversal_k13_now | 0.615 (52) | 0.581 (341) [0.535, 0.626] | 0.582 (1425) [0.561, 0.603] | 0.581 (1472) [0.561, 0.602] | - | 0.727 (33) | 0.076 | flat -0.043 (noise 0.038) |
| reversal_k3_next | 0.583 (60) | 0.578 (609) [0.544, 0.613] | 0.587 (2357) [0.571, 0.601] | 0.587 (2440) [0.572, 0.602] | - | 0.518 (108) | 0.292 | flat -0.012 (noise 0.030) |
| reversal_k3_now | 0.926 (54) | 0.950 (379) [0.939, 0.962] | 0.942 (1712) [0.933, 0.950] | 0.942 (1763) [0.933, 0.950] | - | 0.930 (43) | 0.292 | flat +0.004 (noise 0.016) |
| reversal_k5_next | 0.483 (120) | 0.474 (498) [0.440, 0.498] | 0.492 (1936) [0.474, 0.510] | 0.494 (1990) [0.477, 0.511] | - | 0.397 (146) | 0.187 | flat -0.055 (noise 0.034) |
| reversal_k5_now | 0.848 (59) | 0.870 (354) [0.850, 0.895] | 0.835 (1570) [0.820, 0.851] | 0.837 (1611) [0.823, 0.852] | - | 0.826 (46) | 0.187 | flat +0.049 (noise 0.026) |
| reversal_k8_next | 0.404 (47) | 0.383 (389) [0.355, 0.410] | 0.399 (2020) [0.381, 0.418] | 0.396 (2106) [0.379, 0.415] | - | 0.367 (60) | 0.121 | down -0.088 (noise 0.035) |
| reversal_k8_now | 0.745 (51) | 0.739 (325) [0.700, 0.776] | 0.712 (1546) [0.692, 0.734] | 0.714 (1587) [0.695, 0.735] | - | 0.784 (37) | 0.121 | flat -0.016 (noise 0.033) |
| overall | 0.499 (22076) | 0.504 (154277) [0.502, 0.506] | 0.503 (661202) [0.502, 0.504] | 0.503 (683281) [0.502, 0.504] | - | 0.496 (17383) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.04436, 0.06576] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5075, 'levels': [{'threshold': 0.04436, 'calls_per_day': 140.7, 'win_rate': 0.503}, {'threshold': 0.06576, 'calls_per_day': 35.2, 'win_rate': 0.5484}]}

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15259 | 0.335 | 0.504 (15058) | - | 0.782 (2340) |
| volatility: normal | 15258 | 0.361 | 0.508 (15194) | - | 0.767 (2112) |
| volatility: wild | 15259 | 0.373 | 0.491 (15214) | - | 0.784 (2140) |
| session: Asia 00-08 | 15360 | 0.352 | 0.499 (15252) | - | 0.782 (2173) |
| session: Europe 08-13 | 9600 | 0.351 | 0.505 (9535) | - | 0.767 (1460) |
| session: US 13-21 | 15236 | 0.366 | 0.500 (15153) | - | 0.781 (2215) |
| session: late 21-24 | 5580 | 0.353 | 0.500 (5526) | - | 0.775 (744) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.302 | 0.281 | 0.182 | 0.182 | 0.534 | 0.251 | 0.352 | 1.509 |
| 6h | 360 | 0.312 | 0.308 | 0.223 | 0.239 | 0.531 | 0.229 | 0.395 | 1.313 |
| 24h | 1440 | 0.321 | 0.318 | 0.243 | 0.264 | 0.503 | 0.226 | 0.416 | 1.186 |
| 7d | 10080 | 0.357 | 0.358 | 0.286 | 0.313 | 0.505 | 0.243 | 0.472 | 1.348 |
| 30d | 43200 | 0.356 | 0.356 | 0.279 | 0.309 | 0.501 | 0.245 | 0.466 | 1.281 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.302 / 0.534 / 0.917; 2: 0.281 / 0.534 / 0.933; 3: 0.277 / 0.448 / 0.967; 4: 0.295 / 0.517 / 0.967; 5: 0.251 / 0.448 / 0.967; 6: 0.296 / 0.448 / 0.983; 7: 0.286 / 0.483 / 1.000; 8: 0.298 / 0.517 / 0.983; 9: 0.275 / 0.431 / 1.000; 10: 0.286 / 0.500 / 1.000; 11: 0.287 / 0.483 / 1.000; 12: 0.324 / 0.603 / 1.000; 13: 0.308 / 0.586 / 1.000; 14: 0.297 / 0.534 / 0.983; 15: 0.249 / 0.397 / 0.967
- 6h: 1: 0.312 / 0.531 / 0.867; 2: 0.299 / 0.477 / 0.903; 3: 0.301 / 0.520 / 0.908; 4: 0.313 / 0.545 / 0.900; 5: 0.301 / 0.506 / 0.892; 6: 0.301 / 0.494 / 0.908; 7: 0.302 / 0.474 / 0.908; 8: 0.300 / 0.477 / 0.903; 9: 0.297 / 0.466 / 0.911; 10: 0.309 / 0.543 / 0.911; 11: 0.298 / 0.534 / 0.889; 12: 0.305 / 0.520 / 0.875; 13: 0.315 / 0.540 / 0.861; 14: 0.300 / 0.472 / 0.861; 15: 0.290 / 0.449 / 0.869
- 24h: 1: 0.321 / 0.503 / 0.889; 2: 0.322 / 0.500 / 0.897; 3: 0.322 / 0.499 / 0.897; 4: 0.322 / 0.512 / 0.903; 5: 0.317 / 0.496 / 0.900; 6: 0.317 / 0.481 / 0.898; 7: 0.320 / 0.491 / 0.899; 8: 0.312 / 0.476 / 0.899; 9: 0.314 / 0.484 / 0.901; 10: 0.317 / 0.494 / 0.903; 11: 0.322 / 0.537 / 0.899; 12: 0.320 / 0.506 / 0.897; 13: 0.320 / 0.500 / 0.894; 14: 0.317 / 0.485 / 0.896; 15: 0.311 / 0.468 / 0.897
- 7d: 1: 0.357 / 0.505 / 0.899; 2: 0.352 / 0.491 / 0.900; 3: 0.355 / 0.509 / 0.900; 4: 0.351 / 0.494 / 0.900; 5: 0.352 / 0.508 / 0.900; 6: 0.350 / 0.500 / 0.899; 7: 0.351 / 0.499 / 0.899; 8: 0.350 / 0.506 / 0.899; 9: 0.347 / 0.493 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.349 / 0.506 / 0.899; 12: 0.351 / 0.509 / 0.899; 13: 0.349 / 0.503 / 0.898; 14: 0.347 / 0.496 / 0.898; 15: 0.347 / 0.497 / 0.898
- 30d: 1: 0.356 / 0.501 / 0.899; 2: 0.353 / 0.497 / 0.900; 3: 0.354 / 0.505 / 0.900; 4: 0.351 / 0.500 / 0.900; 5: 0.351 / 0.501 / 0.900; 6: 0.351 / 0.505 / 0.900; 7: 0.350 / 0.506 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.499 / 0.900; 10: 0.348 / 0.503 / 0.900; 11: 0.348 / 0.502 / 0.900; 12: 0.347 / 0.501 / 0.900; 13: 0.347 / 0.500 / 0.900; 14: 0.346 / 0.495 / 0.900; 15: 0.345 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.110 (body 0.079, range 0.142); 'price stays where it was' would score 0.115; colour right 0.466; typical miss of the close 3.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.078 (body 0.047, range 0.109); 'price stays where it was' would score 0.060; colour right 0.506; typical miss of the close 4.3 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.107 (body 0.070, range 0.144); 'price stays where it was' would score 0.108; colour right 0.500; typical miss of the close 4.4 bp; chain ended on the right side 0.537 of 95 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.158); 'price stays where it was' would score 0.117; colour right 0.495; typical miss of the close 7.7 bp; chain ended on the right side 0.527 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.2 bp; chain ended on the right side 0.511 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.4; 2: 0.197 / 4.5; 3: 0.169 / 6.3; 4: 0.133 / 6.6; 5: 0.122 / 7.4; 6: 0.113 / 8.3; 7: 0.102 / 8.7; 8: 0.093 / 9.2; 9: 0.089 / 9.4; 10: 0.084 / 10.3; 11: 0.078 / 10.8; 12: 0.076 / 11.2; 13: 0.068 / 11.6; 14: 0.068 / 11.6; 15: 0.063 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 88730, probability skill vs chance 0.2286, widened contest next: True
  - now: threshold 0.839, hit rate recent 0.9211 / long run 0.9408
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.293, naive rule 0.504, lift 3.03x
    - 24h: 54 calls (54 a day), hit rate 0.907, chance 0.293, naive rule 0.496, lift 3.10x
    - 7d: 382 calls (55 a day), hit rate 0.948, chance 0.289, naive rule 0.484, lift 3.28x
    - 30d: 1708 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5323, hit rate recent 0.5389 / long run 0.5745
    - 6h: 41 calls (166 a day), hit rate 0.537, chance 0.293, lift 1.83x
    - 24h: 124 calls (124 a day), hit rate 0.500, chance 0.293, lift 1.71x
    - 7d: 665 calls (95 a day), hit rate 0.579, chance 0.289, lift 2.00x
    - 30d: 2411 calls (80 a day), hit rate 0.583, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.494; 0.35: 538, 0.518; 0.40: 490, 0.559; 0.45: 423, 0.624; 0.50: 369, 0.679; 0.55: 322, 0.724; 0.60: 275, 0.766; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 140, 0.868; 0.80: 100, 0.906; 0.85: 49, 0.949; 0.90: 1, 0.971
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 496, 0.459; 0.40: 413, 0.487; 0.45: 317, 0.518; 0.50: 209, 0.550; 0.55: 94, 0.586; 0.60: 13, 0.607; 0.65: 0, 0.769
- **K=5**: model 1790208000, labels learned 88728, probability skill vs chance 0.2178, widened contest next: True
  - now: threshold 0.7082, hit rate recent 0.8298 / long run 0.8397
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.184, naive rule 0.375, lift 3.80x
    - 24h: 56 calls (56 a day), hit rate 0.804, chance 0.191, naive rule 0.389, lift 4.21x
    - 7d: 359 calls (51 a day), hit rate 0.861, chance 0.186, naive rule 0.392, lift 4.62x
    - 30d: 1582 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.48x
  - next: threshold 0.3873, hit rate recent 0.3957 / long run 0.4723
    - 6h: 47 calls (192 a day), hit rate 0.362, chance 0.184, lift 1.96x
    - 24h: 178 calls (179 a day), hit rate 0.393, chance 0.191, lift 2.06x
    - 7d: 621 calls (89 a day), hit rate 0.452, chance 0.186, lift 2.43x
    - 30d: 2043 calls (68 a day), hit rate 0.487, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 434, 0.410; 0.35: 374, 0.461; 0.40: 303, 0.530; 0.45: 248, 0.587; 0.50: 193, 0.647; 0.55: 148, 0.696; 0.60: 116, 0.737; 0.65: 88, 0.780; 0.70: 64, 0.818; 0.75: 35, 0.856; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.423; 0.40: 169, 0.447; 0.45: 89, 0.473; 0.50: 23, 0.513; 0.55: 3, 0.578
- **K=8**: model 1790553600, labels learned 88725, probability skill vs chance 0.1984, widened contest next: False
  - now: threshold 0.563, hit rate recent 0.7398 / long run 0.7272
    - 6h: 7 calls (29 a day), hit rate 0.429, chance 0.099, naive rule 0.290, lift 4.35x
    - 24h: 47 calls (47 a day), hit rate 0.745, chance 0.114, naive rule 0.308, lift 6.51x
    - 7d: 321 calls (46 a day), hit rate 0.735, chance 0.121, naive rule 0.327, lift 6.06x
    - 30d: 1546 calls (52 a day), hit rate 0.717, chance 0.122, naive rule 0.327, lift 5.90x
  - next: threshold 0.3603, hit rate recent 0.3774 / long run 0.4026
    - 6h: 22 calls (91 a day), hit rate 0.364, chance 0.099, lift 3.69x
    - 24h: 66 calls (66 a day), hit rate 0.348, chance 0.114, lift 3.05x
    - 7d: 412 calls (59 a day), hit rate 0.371, chance 0.121, lift 3.06x
    - 30d: 2018 calls (67 a day), hit rate 0.399, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 279, 0.395; 0.35: 210, 0.470; 0.40: 163, 0.534; 0.45: 129, 0.584; 0.50: 98, 0.625; 0.55: 69, 0.678; 0.60: 46, 0.722; 0.65: 25, 0.755; 0.70: 9, 0.799; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 191, 0.343; 0.35: 120, 0.380; 0.40: 50, 0.406; 0.45: 10, 0.427; 0.50: 1, 0.452
- **K=13**: model 1790208000, labels learned 88720, probability skill vs chance 0.1858, widened contest next: False
  - now: threshold 0.4088, hit rate recent 0.6487 / long run 0.591
    - 6h: 6 calls (25 a day), hit rate 0.667, chance 0.083, naive rule 0.295, lift 8.07x
    - 24h: 43 calls (43 a day), hit rate 0.674, chance 0.079, naive rule 0.266, lift 8.50x
    - 7d: 339 calls (49 a day), hit rate 0.590, chance 0.078, naive rule 0.265, lift 7.54x
    - 30d: 1423 calls (47 a day), hit rate 0.587, chance 0.077, naive rule 0.267, lift 7.67x
  - next: threshold 0.2691, hit rate recent 0.2855 / long run 0.2944
    - 6h: 30 calls (125 a day), hit rate 0.300, chance 0.083, lift 3.63x
    - 24h: 87 calls (88 a day), hit rate 0.287, chance 0.079, lift 3.62x
    - 7d: 622 calls (89 a day), hit rate 0.270, chance 0.078, lift 3.45x
    - 30d: 1996 calls (67 a day), hit rate 0.307, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.433; 0.35: 91, 0.490; 0.40: 65, 0.537; 0.45: 45, 0.595; 0.50: 29, 0.615; 0.55: 17, 0.655; 0.60: 7, 0.674; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.316; 0.35: 18, 0.348; 0.40: 4, 0.328; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.815 | 0.63% | 0.950 | 0.567 | 0.254 | 0.500 | 0.436 |
| 6h | 5.081 | 5.99% | 0.872 | 0.514 | 0.250 | 0.523 | 0.355 |
| 24h | 6.381 | 11.62% | 0.893 | 0.504 | 0.251 | 0.497 | 0.621 |
| 7d | 12.876 | 4.10% | 0.900 | 0.501 | 0.251 | 0.497 | 0.668 |
| 30d | 14.444 | 4.18% | 0.900 | 0.500 | 0.251 | 0.499 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 4.845 | 4.864 | 4.883 | 4.683 | 5.199 | 5.274 | 4.833 | 4.813 | 4.801 | 4.815 |
| 6h | 5.405 | 5.132 | 5.121 | 5.116 | 5.248 | 5.467 | 5.065 | 5.079 | 5.071 | 5.081 |
| 24h | 7.221 | 6.493 | 6.545 | 6.410 | 6.572 | 6.749 | 6.392 | 6.384 | 6.381 | 6.381 |
| 7d | 13.426 | 12.977 | 12.956 | 12.886 | 13.121 | 13.041 | 12.868 | 12.863 | 12.852 | 12.876 |
| 30d | 15.073 | 14.582 | 14.533 | 14.470 | 14.726 | 14.661 | 14.451 | 14.417 | 14.416 | 14.444 |

## Next candle

- candle starting 2026-10-03 18:56 UTC, last close 2683.68
- P(up) 0.5281, return quantiles (bp): {'05': -2.656, '10': -1.896, '25': -0.717, '40': -0.147, '50': 0.054, '60': 0.259, '75': 0.959, '90': 2.007, '95': 2.732}
- changepoint probability 0.02, regime age 51.2 min
- agent weights: empirical 0.003, ewma 0.131, garch 0.078, har 0.171, bocpd 0.033, hmm 0.005, online_qr 0.296, lgbm 0.283

## Learning log

- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.66, 5.39, 13.26], current probabilities: [0.965, 0.034, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 19:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.175, 'l_abs': 0.644, 'l_hi': 0.77, 'l_lo': 0.723, 'b05': 0.647, 'b25': 0.675, 'b75': 0.652, 'b95': 0.664}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.502, 1.918, 2.264, 2.64, 2.956, 3.074, 3.427, 3.57, 3.771, 4.208, 4.147, 4.413, 4.498, 4.665]}
- calibration offsets (in sigma): {'05': -0.0125, '10': 0.025, '25': 0.0775, '40': 0.06, '50': 0.015, '60': -0.04, '75': 0.0025, '90': -0.005, '95': -0.0175}
