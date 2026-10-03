# ETH-USD 60s candle generator - report

- generated: 2026-10-03 19:25 UTC
- last closed candle: 2026-10-03 19:25 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 18:36 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k13_next 0.267 in the last 7 days, -0.102 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.383 in the last 7 days, -0.088 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.547 (95) | 0.528 (670) [0.496, 0.561] | 0.511 (2876) [0.492, 0.530] | 0.511 (2972) [0.493, 0.529] | - | 0.545 (77) | 0.500 | flat -0.007 (noise 0.031) |
| colour_clear | 0.500 (720) | 0.496 (5390) [0.485, 0.504] | 0.496 (23409) [0.491, 0.501] | 0.496 (24238) [0.492, 0.501] | - | 0.518 (596) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | - | - | - | - | - | 0.517 (29) | - | - |
| colour_next | 0.504 (1432) | 0.505 (10008) [0.501, 0.509] | 0.501 (42916) [0.497, 0.504] | 0.501 (44349) [0.497, 0.504] | - | 0.506 (1143) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.497 (20048) | 0.502 (140112) [0.500, 0.505] | 0.501 (600824) [0.500, 0.502] | 0.501 (620886) [0.500, 0.502] | - | 0.494 (16002) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | - | - | - | - | - | 0.667 (6) | - | - |
| reversal_k13_next | 0.241 (58) | 0.267 (592) [0.253, 0.282] | 0.302 (2020) [0.287, 0.319] | 0.300 (2105) [0.285, 0.317] | - | 0.317 (82) | 0.076 | down -0.102 (noise 0.031) |
| reversal_k13_now | 0.615 (52) | 0.581 (341) [0.535, 0.626] | 0.582 (1425) [0.561, 0.603] | 0.581 (1472) [0.561, 0.602] | - | 0.727 (33) | 0.076 | flat -0.043 (noise 0.038) |
| reversal_k3_next | 0.583 (60) | 0.578 (609) [0.544, 0.613] | 0.587 (2357) [0.571, 0.601] | 0.587 (2440) [0.572, 0.602] | - | 0.540 (113) | 0.292 | flat -0.012 (noise 0.030) |
| reversal_k3_now | 0.926 (54) | 0.950 (379) [0.939, 0.962] | 0.942 (1712) [0.933, 0.950] | 0.942 (1763) [0.933, 0.950] | - | 0.932 (44) | 0.292 | flat +0.004 (noise 0.016) |
| reversal_k5_next | 0.483 (120) | 0.474 (498) [0.440, 0.498] | 0.492 (1936) [0.474, 0.510] | 0.494 (1990) [0.477, 0.511] | - | 0.417 (151) | 0.187 | flat -0.055 (noise 0.034) |
| reversal_k5_now | 0.848 (59) | 0.870 (354) [0.850, 0.895] | 0.835 (1570) [0.820, 0.851] | 0.837 (1611) [0.823, 0.852] | - | 0.833 (48) | 0.187 | flat +0.049 (noise 0.026) |
| reversal_k8_next | 0.404 (47) | 0.383 (389) [0.355, 0.410] | 0.399 (2020) [0.381, 0.418] | 0.396 (2106) [0.379, 0.415] | - | 0.371 (62) | 0.121 | down -0.088 (noise 0.035) |
| reversal_k8_now | 0.745 (51) | 0.739 (325) [0.700, 0.776] | 0.712 (1546) [0.692, 0.734] | 0.714 (1587) [0.695, 0.735] | - | 0.784 (37) | 0.121 | flat -0.016 (noise 0.033) |
| overall | 0.499 (22076) | 0.504 (154277) [0.502, 0.506] | 0.503 (661202) [0.502, 0.504] | 0.503 (683281) [0.502, 0.504] | - | 0.496 (17792) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.04436, 0.06576] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5075, 'levels': [{'threshold': 0.04436, 'calls_per_day': 140.7, 'win_rate': 0.503}, {'threshold': 0.06576, 'calls_per_day': 35.2, 'win_rate': 0.5484}]}

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15269 | 0.335 | 0.504 (15065) | - | 0.782 (2342) |
| volatility: normal | 15268 | 0.361 | 0.508 (15204) | - | 0.767 (2113) |
| volatility: wild | 15268 | 0.373 | 0.491 (15223) | - | 0.784 (2140) |
| session: Asia 00-08 | 15360 | 0.352 | 0.499 (15252) | - | 0.782 (2173) |
| session: Europe 08-13 | 9600 | 0.351 | 0.505 (9535) | - | 0.767 (1460) |
| session: US 13-21 | 15265 | 0.366 | 0.500 (15179) | - | 0.782 (2218) |
| session: late 21-24 | 5580 | 0.353 | 0.500 (5526) | - | 0.775 (744) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.282 | 0.257 | 0.226 | 0.226 | 0.600 | 0.255 | 0.309 | 1.340 |
| 6h | 360 | 0.311 | 0.306 | 0.227 | 0.240 | 0.539 | 0.233 | 0.389 | 1.338 |
| 24h | 1440 | 0.319 | 0.316 | 0.243 | 0.263 | 0.503 | 0.226 | 0.413 | 1.202 |
| 7d | 10080 | 0.357 | 0.357 | 0.286 | 0.313 | 0.505 | 0.243 | 0.471 | 1.347 |
| 30d | 43200 | 0.356 | 0.356 | 0.279 | 0.309 | 0.501 | 0.245 | 0.466 | 1.281 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.282 / 0.600 / 0.900; 2: 0.260 / 0.545 / 0.917; 3: 0.260 / 0.473 / 0.883; 4: 0.269 / 0.600 / 0.883; 5: 0.232 / 0.436 / 0.933; 6: 0.252 / 0.418 / 0.983; 7: 0.262 / 0.545 / 1.000; 8: 0.246 / 0.400 / 1.000; 9: 0.256 / 0.509 / 1.000; 10: 0.273 / 0.473 / 1.000; 11: 0.276 / 0.564 / 1.000; 12: 0.279 / 0.491 / 1.000; 13: 0.273 / 0.527 / 1.000; 14: 0.277 / 0.527 / 1.000; 15: 0.220 / 0.436 / 0.983
- 6h: 1: 0.311 / 0.539 / 0.867; 2: 0.295 / 0.490 / 0.897; 3: 0.298 / 0.519 / 0.894; 4: 0.306 / 0.559 / 0.886; 5: 0.298 / 0.501 / 0.889; 6: 0.296 / 0.487 / 0.914; 7: 0.293 / 0.467 / 0.911; 8: 0.292 / 0.458 / 0.906; 9: 0.290 / 0.467 / 0.911; 10: 0.307 / 0.539 / 0.911; 11: 0.294 / 0.536 / 0.892; 12: 0.299 / 0.501 / 0.881; 13: 0.311 / 0.542 / 0.864; 14: 0.297 / 0.476 / 0.861; 15: 0.288 / 0.461 / 0.869
- 24h: 1: 0.319 / 0.503 / 0.887; 2: 0.319 / 0.500 / 0.894; 3: 0.320 / 0.498 / 0.894; 4: 0.320 / 0.515 / 0.899; 5: 0.315 / 0.496 / 0.899; 6: 0.313 / 0.477 / 0.898; 7: 0.318 / 0.493 / 0.899; 8: 0.309 / 0.471 / 0.899; 9: 0.312 / 0.485 / 0.901; 10: 0.317 / 0.497 / 0.903; 11: 0.320 / 0.537 / 0.899; 12: 0.318 / 0.502 / 0.897; 13: 0.318 / 0.501 / 0.894; 14: 0.314 / 0.483 / 0.896; 15: 0.307 / 0.466 / 0.896
- 7d: 1: 0.357 / 0.505 / 0.899; 2: 0.352 / 0.491 / 0.900; 3: 0.355 / 0.509 / 0.900; 4: 0.351 / 0.494 / 0.900; 5: 0.352 / 0.508 / 0.900; 6: 0.350 / 0.500 / 0.900; 7: 0.350 / 0.499 / 0.900; 8: 0.350 / 0.505 / 0.900; 9: 0.347 / 0.493 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.348 / 0.506 / 0.899; 12: 0.350 / 0.509 / 0.899; 13: 0.349 / 0.504 / 0.898; 14: 0.347 / 0.496 / 0.898; 15: 0.346 / 0.498 / 0.898
- 30d: 1: 0.356 / 0.501 / 0.899; 2: 0.352 / 0.497 / 0.900; 3: 0.354 / 0.505 / 0.900; 4: 0.351 / 0.500 / 0.900; 5: 0.351 / 0.501 / 0.900; 6: 0.351 / 0.505 / 0.900; 7: 0.350 / 0.506 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.499 / 0.900; 10: 0.348 / 0.504 / 0.900; 11: 0.348 / 0.502 / 0.900; 12: 0.347 / 0.501 / 0.900; 13: 0.347 / 0.500 / 0.900; 14: 0.346 / 0.495 / 0.900; 15: 0.345 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.058 (body 0.041, range 0.074); 'price stays where it was' would score 0.042; colour right 0.436; typical miss of the close 4.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.074 (body 0.045, range 0.102); 'price stays where it was' would score 0.060; colour right 0.499; typical miss of the close 4.4 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.105 (body 0.069, range 0.141); 'price stays where it was' would score 0.106; colour right 0.498; typical miss of the close 4.4 bp; chain ended on the right side 0.516 of 95 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.158); 'price stays where it was' would score 0.117; colour right 0.495; typical miss of the close 7.7 bp; chain ended on the right side 0.524 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.2 bp; chain ended on the right side 0.510 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.4; 2: 0.197 / 4.5; 3: 0.169 / 6.3; 4: 0.133 / 6.6; 5: 0.122 / 7.4; 6: 0.113 / 8.3; 7: 0.102 / 8.7; 8: 0.093 / 9.2; 9: 0.089 / 9.4; 10: 0.084 / 10.2; 11: 0.078 / 10.8; 12: 0.076 / 11.2; 13: 0.068 / 11.6; 14: 0.068 / 11.6; 15: 0.063 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 88759, probability skill vs chance 0.231, widened contest next: False
  - now: threshold 0.839, hit rate recent 0.9224 / long run 0.9409
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.300, naive rule 0.511, lift 2.96x
    - 24h: 55 calls (55 a day), hit rate 0.909, chance 0.298, naive rule 0.505, lift 3.05x
    - 7d: 382 calls (55 a day), hit rate 0.948, chance 0.289, naive rule 0.484, lift 3.28x
    - 30d: 1708 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5323, hit rate recent 0.5761 / long run 0.5781
    - 6h: 41 calls (166 a day), hit rate 0.585, chance 0.300, lift 1.95x
    - 24h: 129 calls (129 a day), hit rate 0.519, chance 0.298, lift 1.74x
    - 7d: 668 calls (95 a day), hit rate 0.582, chance 0.289, lift 2.01x
    - 30d: 2414 calls (80 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.494; 0.35: 538, 0.519; 0.40: 490, 0.559; 0.45: 423, 0.624; 0.50: 369, 0.680; 0.55: 322, 0.724; 0.60: 275, 0.766; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 140, 0.868; 0.80: 100, 0.906; 0.85: 49, 0.949; 0.90: 1, 0.971
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 496, 0.459; 0.40: 413, 0.487; 0.45: 317, 0.518; 0.50: 209, 0.550; 0.55: 94, 0.585; 0.60: 13, 0.605; 0.65: 0, 0.750
- **K=5**: model 1790208000, labels learned 88757, probability skill vs chance 0.2203, widened contest next: True
  - now: threshold 0.7082, hit rate recent 0.8354 / long run 0.8402
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.197, naive rule 0.406, lift 4.16x
    - 24h: 58 calls (58 a day), hit rate 0.810, chance 0.194, naive rule 0.399, lift 4.18x
    - 7d: 360 calls (51 a day), hit rate 0.861, chance 0.186, naive rule 0.393, lift 4.62x
    - 30d: 1583 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.48x
  - next: threshold 0.3873, hit rate recent 0.4444 / long run 0.4767
    - 6h: 47 calls (192 a day), hit rate 0.447, chance 0.197, lift 2.27x
    - 24h: 180 calls (181 a day), hit rate 0.417, chance 0.194, lift 2.15x
    - 7d: 625 calls (89 a day), hit rate 0.456, chance 0.186, lift 2.45x
    - 30d: 2045 calls (68 a day), hit rate 0.488, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 434, 0.410; 0.35: 374, 0.462; 0.40: 303, 0.530; 0.45: 248, 0.587; 0.50: 193, 0.647; 0.55: 148, 0.696; 0.60: 116, 0.737; 0.65: 88, 0.781; 0.70: 64, 0.818; 0.75: 35, 0.856; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.423; 0.40: 169, 0.447; 0.45: 89, 0.472; 0.50: 22, 0.512; 0.55: 3, 0.573
- **K=8**: model 1790553600, labels learned 88754, probability skill vs chance 0.2005, widened contest next: False
  - now: threshold 0.563, hit rate recent 0.7398 / long run 0.7272
    - 6h: 6 calls (25 a day), hit rate 0.500, chance 0.107, naive rule 0.336, lift 4.67x
    - 24h: 47 calls (47 a day), hit rate 0.745, chance 0.116, naive rule 0.320, lift 6.42x
    - 7d: 321 calls (46 a day), hit rate 0.735, chance 0.122, naive rule 0.328, lift 6.05x
    - 30d: 1545 calls (52 a day), hit rate 0.717, chance 0.122, naive rule 0.327, lift 5.90x
  - next: threshold 0.3603, hit rate recent 0.3813 / long run 0.4029
    - 6h: 22 calls (91 a day), hit rate 0.364, chance 0.107, lift 3.39x
    - 24h: 68 calls (68 a day), hit rate 0.353, chance 0.116, lift 3.04x
    - 7d: 414 calls (59 a day), hit rate 0.372, chance 0.122, lift 3.06x
    - 30d: 2015 calls (67 a day), hit rate 0.399, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 279, 0.395; 0.35: 210, 0.470; 0.40: 163, 0.534; 0.45: 129, 0.584; 0.50: 98, 0.625; 0.55: 69, 0.678; 0.60: 46, 0.722; 0.65: 25, 0.755; 0.70: 9, 0.799; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 191, 0.343; 0.35: 120, 0.380; 0.40: 50, 0.406; 0.45: 10, 0.424; 0.50: 1, 0.452
- **K=13**: model 1790208000, labels learned 88749, probability skill vs chance 0.1853, widened contest next: False
  - now: threshold 0.4088, hit rate recent 0.6487 / long run 0.591
    - 6h: 6 calls (25 a day), hit rate 0.667, chance 0.080, naive rule 0.299, lift 8.36x
    - 24h: 43 calls (43 a day), hit rate 0.674, chance 0.078, naive rule 0.267, lift 8.62x
    - 7d: 339 calls (49 a day), hit rate 0.590, chance 0.078, naive rule 0.265, lift 7.55x
    - 30d: 1422 calls (47 a day), hit rate 0.586, chance 0.076, naive rule 0.267, lift 7.67x
  - next: threshold 0.2691, hit rate recent 0.2928 / long run 0.2951
    - 6h: 28 calls (117 a day), hit rate 0.321, chance 0.080, lift 4.03x
    - 24h: 89 calls (90 a day), hit rate 0.292, chance 0.078, lift 3.73x
    - 7d: 623 calls (89 a day), hit rate 0.271, chance 0.078, lift 3.47x
    - 30d: 1994 calls (66 a day), hit rate 0.307, chance 0.076, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.432; 0.35: 91, 0.490; 0.40: 65, 0.536; 0.45: 45, 0.595; 0.50: 29, 0.614; 0.55: 17, 0.655; 0.60: 7, 0.674; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.316; 0.35: 18, 0.347; 0.40: 4, 0.328; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.119 | 3.65% | 0.917 | 0.500 | 0.257 | 0.436 | -0.002 |
| 6h | 4.983 | 5.59% | 0.875 | 0.517 | 0.250 | 0.516 | 0.350 |
| 24h | 6.103 | 12.15% | 0.892 | 0.504 | 0.251 | 0.496 | 0.534 |
| 7d | 12.878 | 4.09% | 0.900 | 0.500 | 0.251 | 0.497 | 0.669 |
| 30d | 14.428 | 4.18% | 0.900 | 0.500 | 0.251 | 0.499 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 4.275 | 4.185 | 4.162 | 4.133 | 4.247 | 4.595 | 4.082 | 4.129 | 4.093 | 4.119 |
| 6h | 5.278 | 5.034 | 5.028 | 5.013 | 5.159 | 5.391 | 4.965 | 4.984 | 4.972 | 4.983 |
| 24h | 6.947 | 6.179 | 6.258 | 6.138 | 6.277 | 6.482 | 6.119 | 6.106 | 6.104 | 6.103 |
| 7d | 13.428 | 12.980 | 12.958 | 12.889 | 13.123 | 13.041 | 12.870 | 12.866 | 12.854 | 12.878 |
| 30d | 15.056 | 14.566 | 14.517 | 14.454 | 14.710 | 14.645 | 14.435 | 14.401 | 14.400 | 14.428 |

## Next candle

- candle starting 2026-10-03 19:25 UTC, last close 2682.99
- P(up) 0.5124, return quantiles (bp): {'05': -2.559, '10': -1.902, '25': -0.748, '40': -0.156, '50': 0.018, '60': 0.245, '75': 0.927, '90': 1.931, '95': 2.666}
- changepoint probability 0.0218, regime age 78.5 min
- agent weights: empirical 0.003, ewma 0.135, garch 0.081, har 0.157, bocpd 0.035, hmm 0.004, online_qr 0.305, lgbm 0.280

## Learning log

- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.66, 5.39, 13.26], current probabilities: [0.965, 0.034, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 19:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.165, 'l_abs': 0.645, 'l_hi': 0.769, 'l_lo': 0.723, 'b05': 0.648, 'b25': 0.67, 'b75': 0.652, 'b95': 0.662}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.535, 2.041, 2.409, 2.645, 2.79, 2.901, 3.234, 3.369, 3.558, 3.971, 3.914, 4.164, 4.244, 4.491]}
- calibration offsets (in sigma): {'05': -0.018, '10': 0.014, '25': 0.07, '40': 0.066, '50': 0.01, '60': -0.046, '75': -0.0, '90': -0.014, '95': -0.022}
