# ETH-USD 60s candle generator - report

- generated: 2026-10-03 22:19 UTC
- last closed candle: 2026-10-03 22:19 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k13_next 0.267 in the last 7 days, -0.102 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.383 in the last 7 days, -0.088 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.547 (95) | 0.528 (670) [0.496, 0.561] | 0.511 (2876) [0.492, 0.530] | 0.511 (2972) [0.493, 0.529] | - | 0.539 (89) | 0.500 | flat -0.007 (noise 0.031) |
| colour_clear | 0.500 (720) | 0.496 (5390) [0.485, 0.504] | 0.496 (23409) [0.491, 0.501] | 0.496 (24238) [0.492, 0.501] | - | 0.532 (678) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | - | - | - | - | - | 0.600 (50) | - | - |
| colour_next | 0.504 (1432) | 0.505 (10008) [0.501, 0.509] | 0.501 (42916) [0.497, 0.504] | 0.501 (44349) [0.497, 0.504] | - | 0.515 (1308) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.497 (20048) | 0.502 (140112) [0.500, 0.505] | 0.501 (600824) [0.500, 0.502] | 0.501 (620886) [0.500, 0.502] | - | 0.492 (18312) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | - | - | - | - | - | 0.615 (13) | - | - |
| reversal_k13_next | 0.241 (58) | 0.267 (592) [0.253, 0.282] | 0.302 (2020) [0.287, 0.319] | 0.300 (2105) [0.285, 0.317] | - | 0.327 (98) | 0.076 | down -0.102 (noise 0.031) |
| reversal_k13_now | 0.615 (52) | 0.581 (341) [0.535, 0.626] | 0.582 (1425) [0.561, 0.603] | 0.581 (1472) [0.561, 0.602] | - | 0.762 (42) | 0.076 | flat -0.043 (noise 0.038) |
| reversal_k3_next | 0.583 (60) | 0.578 (609) [0.544, 0.613] | 0.587 (2357) [0.571, 0.601] | 0.587 (2440) [0.572, 0.602] | - | 0.529 (136) | 0.292 | flat -0.012 (noise 0.030) |
| reversal_k3_now | 0.926 (54) | 0.950 (379) [0.939, 0.962] | 0.942 (1712) [0.933, 0.950] | 0.942 (1763) [0.933, 0.950] | - | 0.926 (54) | 0.292 | flat +0.004 (noise 0.016) |
| reversal_k5_next | 0.483 (120) | 0.474 (498) [0.440, 0.498] | 0.492 (1936) [0.474, 0.510] | 0.494 (1990) [0.477, 0.511] | - | 0.403 (176) | 0.187 | flat -0.055 (noise 0.034) |
| reversal_k5_now | 0.848 (59) | 0.870 (354) [0.850, 0.895] | 0.835 (1570) [0.820, 0.851] | 0.837 (1611) [0.823, 0.852] | - | 0.810 (58) | 0.187 | flat +0.049 (noise 0.026) |
| reversal_k8_next | 0.404 (47) | 0.383 (389) [0.355, 0.410] | 0.399 (2020) [0.381, 0.418] | 0.396 (2106) [0.379, 0.415] | - | 0.370 (73) | 0.121 | down -0.088 (noise 0.035) |
| reversal_k8_now | 0.745 (51) | 0.739 (325) [0.700, 0.776] | 0.712 (1546) [0.692, 0.734] | 0.714 (1587) [0.695, 0.735] | - | 0.804 (46) | 0.121 | flat -0.016 (noise 0.033) |
| overall | 0.499 (22076) | 0.504 (154277) [0.502, 0.506] | 0.503 (661202) [0.502, 0.504] | 0.503 (683281) [0.502, 0.504] | - | 0.496 (20392) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.075, 0.1105] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5301, 'levels': [{'threshold': 0.075, 'calls_per_day': 142.8, 'win_rate': 0.5541}, {'threshold': 0.1105, 'calls_per_day': 35.3, 'win_rate': 0.6265}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 176, 'rate': 0.5568}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15327 | 0.335 | 0.504 (15114) | 0.600 (50) | 0.782 (2363) |
| volatility: normal | 15326 | 0.361 | 0.508 (15262) | - | 0.767 (2117) |
| volatility: wild | 15326 | 0.373 | 0.490 (15281) | - | 0.785 (2153) |
| session: Asia 00-08 | 15360 | 0.352 | 0.499 (15252) | - | 0.782 (2173) |
| session: Europe 08-13 | 9600 | 0.351 | 0.505 (9535) | - | 0.767 (1460) |
| session: US 13-21 | 15360 | 0.365 | 0.500 (15269) | - | 0.784 (2239) |
| session: late 21-24 | 5659 | 0.352 | 0.501 (5601) | - | 0.773 (761) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.347 | 0.306 | 0.283 | 0.283 | 0.552 | 0.273 | 0.421 | 1.216 |
| 6h | 360 | 0.310 | 0.298 | 0.223 | 0.225 | 0.558 | 0.247 | 0.374 | 1.298 |
| 24h | 1440 | 0.315 | 0.309 | 0.236 | 0.251 | 0.510 | 0.230 | 0.401 | 1.230 |
| 7d | 10080 | 0.357 | 0.357 | 0.286 | 0.311 | 0.506 | 0.243 | 0.471 | 1.346 |
| 30d | 43200 | 0.355 | 0.355 | 0.279 | 0.309 | 0.501 | 0.245 | 0.466 | 1.281 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.347 / 0.552 / 0.850; 2: 0.335 / 0.552 / 0.883; 3: 0.325 / 0.448 / 0.933; 4: 0.316 / 0.431 / 0.950; 5: 0.342 / 0.517 / 0.967; 6: 0.320 / 0.448 / 0.983; 7: 0.301 / 0.414 / 0.967; 8: 0.334 / 0.500 / 0.950; 9: 0.334 / 0.534 / 0.917; 10: 0.348 / 0.517 / 0.917; 11: 0.339 / 0.534 / 0.950; 12: 0.345 / 0.483 / 0.950; 13: 0.377 / 0.707 / 0.933; 14: 0.302 / 0.466 / 0.900; 15: 0.328 / 0.448 / 0.900
- 6h: 1: 0.310 / 0.558 / 0.856; 2: 0.295 / 0.520 / 0.881; 3: 0.297 / 0.506 / 0.900; 4: 0.290 / 0.523 / 0.903; 5: 0.285 / 0.468 / 0.897; 6: 0.280 / 0.433 / 0.911; 7: 0.281 / 0.471 / 0.908; 8: 0.285 / 0.462 / 0.903; 9: 0.285 / 0.480 / 0.903; 10: 0.300 / 0.520 / 0.900; 11: 0.281 / 0.483 / 0.911; 12: 0.295 / 0.503 / 0.911; 13: 0.301 / 0.526 / 0.900; 14: 0.289 / 0.480 / 0.889; 15: 0.275 / 0.433 / 0.883
- 24h: 1: 0.315 / 0.510 / 0.873; 2: 0.313 / 0.507 / 0.887; 3: 0.312 / 0.493 / 0.892; 4: 0.311 / 0.513 / 0.895; 5: 0.306 / 0.483 / 0.895; 6: 0.305 / 0.471 / 0.894; 7: 0.308 / 0.488 / 0.892; 8: 0.303 / 0.463 / 0.892; 9: 0.306 / 0.483 / 0.895; 10: 0.313 / 0.501 / 0.896; 11: 0.313 / 0.527 / 0.894; 12: 0.311 / 0.496 / 0.893; 13: 0.313 / 0.505 / 0.888; 14: 0.308 / 0.483 / 0.886; 15: 0.301 / 0.465 / 0.888
- 7d: 1: 0.357 / 0.506 / 0.898; 2: 0.352 / 0.491 / 0.899; 3: 0.355 / 0.509 / 0.900; 4: 0.352 / 0.496 / 0.900; 5: 0.351 / 0.507 / 0.900; 6: 0.350 / 0.498 / 0.900; 7: 0.350 / 0.499 / 0.900; 8: 0.349 / 0.505 / 0.900; 9: 0.347 / 0.493 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.349 / 0.505 / 0.900; 12: 0.350 / 0.509 / 0.900; 13: 0.350 / 0.504 / 0.899; 14: 0.347 / 0.496 / 0.899; 15: 0.346 / 0.497 / 0.899
- 30d: 1: 0.355 / 0.501 / 0.899; 2: 0.352 / 0.497 / 0.900; 3: 0.353 / 0.505 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.350 / 0.504 / 0.900; 7: 0.350 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.499 / 0.900; 10: 0.348 / 0.504 / 0.900; 11: 0.347 / 0.503 / 0.900; 12: 0.347 / 0.501 / 0.900; 13: 0.346 / 0.500 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.345 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.155 (body 0.109, range 0.202); 'price stays where it was' would score 0.171; colour right 0.569; typical miss of the close 2.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.108 (body 0.078, range 0.138); 'price stays where it was' would score 0.107; colour right 0.515; typical miss of the close 3.2 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.106 (body 0.074, range 0.139); 'price stays where it was' would score 0.100; colour right 0.502; typical miss of the close 3.9 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.118 (body 0.077, range 0.158); 'price stays where it was' would score 0.118; colour right 0.497; typical miss of the close 7.6 bp; chain ended on the right side 0.522 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.2 bp; chain ended on the right side 0.510 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.4; 2: 0.197 / 4.5; 3: 0.169 / 6.3; 4: 0.133 / 6.5; 5: 0.122 / 7.3; 6: 0.113 / 8.3; 7: 0.101 / 8.7; 8: 0.093 / 9.2; 9: 0.089 / 9.3; 10: 0.083 / 10.2; 11: 0.078 / 10.7; 12: 0.076 / 11.1; 13: 0.068 / 11.5; 14: 0.068 / 11.5; 15: 0.063 / 11.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 88933, probability skill vs chance 0.226, widened contest next: True
  - now: threshold 0.839, hit rate recent 0.918 / long run 0.9402
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.323, naive rule 0.526, lift 2.89x
    - 24h: 59 calls (59 a day), hit rate 0.898, chance 0.294, naive rule 0.498, lift 3.05x
    - 7d: 387 calls (55 a day), hit rate 0.946, chance 0.289, naive rule 0.482, lift 3.28x
    - 30d: 1711 calls (57 a day), hit rate 0.942, chance 0.293, naive rule 0.482, lift 3.22x
  - next: threshold 0.5323, hit rate recent 0.5426 / long run 0.5743
    - 6h: 43 calls (174 a day), hit rate 0.605, chance 0.323, lift 1.87x
    - 24h: 142 calls (142 a day), hit rate 0.521, chance 0.294, lift 1.77x
    - 7d: 686 calls (98 a day), hit rate 0.580, chance 0.289, lift 2.01x
    - 30d: 2429 calls (81 a day), hit rate 0.583, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.494; 0.35: 538, 0.519; 0.40: 490, 0.559; 0.45: 423, 0.624; 0.50: 369, 0.680; 0.55: 322, 0.725; 0.60: 275, 0.766; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 140, 0.868; 0.80: 100, 0.906; 0.85: 49, 0.949; 0.90: 1, 0.971
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 496, 0.460; 0.40: 414, 0.487; 0.45: 318, 0.518; 0.50: 209, 0.550; 0.55: 94, 0.585; 0.60: 13, 0.605; 0.65: 0, 0.714
- **K=5**: model 1790208000, labels learned 88931, probability skill vs chance 0.2161, widened contest next: True
  - now: threshold 0.7082, hit rate recent 0.8123 / long run 0.8379
    - 6h: 15 calls (61 a day), hit rate 0.733, chance 0.197, naive rule 0.389, lift 3.72x
    - 24h: 63 calls (63 a day), hit rate 0.794, chance 0.188, naive rule 0.387, lift 4.21x
    - 7d: 364 calls (52 a day), hit rate 0.857, chance 0.187, naive rule 0.392, lift 4.59x
    - 30d: 1587 calls (53 a day), hit rate 0.835, chance 0.187, naive rule 0.391, lift 4.47x
  - next: threshold 0.3873, hit rate recent 0.3968 / long run 0.4702
    - 6h: 49 calls (200 a day), hit rate 0.429, chance 0.197, lift 2.18x
    - 24h: 188 calls (189 a day), hit rate 0.399, chance 0.188, lift 2.12x
    - 7d: 646 calls (92 a day), hit rate 0.450, chance 0.187, lift 2.41x
    - 30d: 2066 calls (69 a day), hit rate 0.486, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 434, 0.410; 0.35: 374, 0.461; 0.40: 303, 0.529; 0.45: 248, 0.586; 0.50: 193, 0.647; 0.55: 148, 0.696; 0.60: 116, 0.737; 0.65: 88, 0.780; 0.70: 65, 0.817; 0.75: 35, 0.856; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.423; 0.40: 169, 0.446; 0.45: 89, 0.472; 0.50: 23, 0.513; 0.55: 3, 0.573
- **K=8**: model 1790553600, labels learned 88928, probability skill vs chance 0.2008, widened contest next: False
  - now: threshold 0.563, hit rate recent 0.7597 / long run 0.7296
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.119, naive rule 0.322, lift 5.62x
    - 24h: 51 calls (51 a day), hit rate 0.784, chance 0.118, naive rule 0.321, lift 6.66x
    - 7d: 322 calls (46 a day), hit rate 0.739, chance 0.122, naive rule 0.329, lift 6.04x
    - 30d: 1549 calls (52 a day), hit rate 0.719, chance 0.122, naive rule 0.327, lift 5.91x
  - next: threshold 0.3603, hit rate recent 0.3788 / long run 0.4022
    - 6h: 22 calls (91 a day), hit rate 0.318, chance 0.119, lift 2.68x
    - 24h: 77 calls (78 a day), hit rate 0.364, chance 0.118, lift 3.09x
    - 7d: 419 calls (60 a day), hit rate 0.377, chance 0.122, lift 3.08x
    - 30d: 2019 calls (67 a day), hit rate 0.399, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 279, 0.395; 0.35: 210, 0.470; 0.40: 163, 0.534; 0.45: 128, 0.583; 0.50: 98, 0.624; 0.55: 69, 0.678; 0.60: 47, 0.723; 0.65: 25, 0.757; 0.70: 9, 0.801; 0.75: 1, 0.812
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 191, 0.342; 0.35: 120, 0.380; 0.40: 50, 0.405; 0.45: 11, 0.422; 0.50: 1, 0.452
- **K=13**: model 1790208000, labels learned 88923, probability skill vs chance 0.1851, widened contest next: False
  - now: threshold 0.4088, hit rate recent 0.6816 / long run 0.5954
    - 6h: 11 calls (46 a day), hit rate 0.727, chance 0.078, naive rule 0.259, lift 9.29x
    - 24h: 47 calls (47 a day), hit rate 0.723, chance 0.082, naive rule 0.278, lift 8.81x
    - 7d: 340 calls (49 a day), hit rate 0.594, chance 0.079, naive rule 0.266, lift 7.55x
    - 30d: 1427 calls (48 a day), hit rate 0.588, chance 0.077, naive rule 0.266, lift 7.68x
  - next: threshold 0.2691, hit rate recent 0.315 / long run 0.2972
    - 6h: 33 calls (138 a day), hit rate 0.303, chance 0.078, lift 3.87x
    - 24h: 103 calls (104 a day), hit rate 0.311, chance 0.082, lift 3.78x
    - 7d: 632 calls (90 a day), hit rate 0.275, chance 0.079, lift 3.50x
    - 30d: 1998 calls (67 a day), hit rate 0.306, chance 0.077, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.433; 0.35: 91, 0.491; 0.40: 65, 0.538; 0.45: 45, 0.598; 0.50: 29, 0.616; 0.55: 17, 0.657; 0.60: 7, 0.674; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.316; 0.35: 18, 0.346; 0.40: 4, 0.333; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.448 | 0.48% | 0.933 | 0.433 | 0.254 | 0.397 | 0.230 |
| 6h | 5.094 | 1.78% | 0.878 | 0.494 | 0.251 | 0.503 | 0.324 |
| 24h | 5.516 | 12.40% | 0.883 | 0.494 | 0.251 | 0.490 | 0.323 |
| 7d | 12.796 | 4.07% | 0.899 | 0.500 | 0.251 | 0.497 | 0.674 |
| 30d | 14.378 | 4.19% | 0.900 | 0.500 | 0.251 | 0.499 | 0.680 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 4.469 | 4.469 | 4.486 | 4.460 | 4.501 | 4.859 | 4.451 | 4.425 | 4.429 | 4.448 |
| 6h | 5.186 | 5.142 | 5.113 | 5.142 | 5.225 | 5.449 | 5.085 | 5.098 | 5.087 | 5.094 |
| 24h | 6.297 | 5.544 | 5.675 | 5.558 | 5.678 | 5.937 | 5.509 | 5.505 | 5.512 | 5.516 |
| 7d | 13.339 | 12.894 | 12.874 | 12.806 | 13.035 | 12.957 | 12.788 | 12.784 | 12.772 | 12.796 |
| 30d | 15.006 | 14.515 | 14.467 | 14.404 | 14.658 | 14.596 | 14.386 | 14.351 | 14.351 | 14.378 |

## Next candle

- candle starting 2026-10-03 22:19 UTC, last close 2688.78
- P(up) 0.4845, return quantiles (bp): {'05': -3.559, '10': -2.572, '25': -1.101, '40': -0.39, '50': -0.071, '60': 0.392, '75': 1.269, '90': 2.597, '95': 3.537}
- changepoint probability 0.0267, regime age 227.2 min
- agent weights: empirical 0.005, ewma 0.144, garch 0.102, har 0.147, bocpd 0.041, hmm 0.004, online_qr 0.279, lgbm 0.277

## Learning log

- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.66, 5.39, 13.26], current probabilities: [0.962, 0.037, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 22:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.168, 'l_abs': 0.651, 'l_hi': 0.763, 'l_lo': 0.718, 'b05': 0.646, 'b25': 0.654, 'b75': 0.663, 'b95': 0.651}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.683, 1.984, 2.296, 2.572, 2.767, 2.995, 3.145, 3.41, 3.53, 3.564, 3.584, 3.89, 4.21, 4.28]}
- calibration offsets (in sigma): {'05': -0.031, '10': 0.018, '25': 0.095, '40': 0.072, '50': 0.0, '60': -0.002, '75': 0.025, '90': 0.012, '95': 0.011}
