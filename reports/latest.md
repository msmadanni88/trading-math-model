# ETH-USD 60s candle generator - report

- generated: 2026-10-03 18:36 UTC
- last closed candle: 2026-10-03 18:36 UTC (staleness 0.9 min)
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
| chain_end_side | 0.547 (95) | 0.528 (670) [0.496, 0.561] | 0.511 (2876) [0.492, 0.530] | 0.511 (2972) [0.493, 0.529] | - | 0.554 (74) | 0.500 | flat -0.007 (noise 0.031) |
| colour_clear | 0.500 (720) | 0.496 (5390) [0.485, 0.504] | 0.496 (23409) [0.491, 0.501] | 0.496 (24238) [0.492, 0.501] | - | 0.515 (575) | 0.500 | flat -0.001 (noise 0.010) |
| colour_confident | - | - | - | - | - | 0.536 (28) | - | - |
| colour_next | 0.504 (1432) | 0.505 (10008) [0.501, 0.509] | 0.501 (42916) [0.497, 0.504] | 0.501 (44349) [0.497, 0.504] | - | 0.502 (1099) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.497 (20048) | 0.502 (140112) [0.500, 0.505] | 0.501 (600824) [0.500, 0.502] | 0.501 (620886) [0.500, 0.502] | - | 0.494 (15386) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | - | - | - | - | - | 0.667 (6) | - | - |
| reversal_k13_next | 0.241 (58) | 0.267 (592) [0.253, 0.282] | 0.302 (2020) [0.287, 0.319] | 0.300 (2105) [0.285, 0.317] | - | 0.317 (79) | 0.076 | down -0.102 (noise 0.031) |
| reversal_k13_now | 0.615 (52) | 0.581 (341) [0.535, 0.626] | 0.582 (1425) [0.561, 0.603] | 0.581 (1472) [0.561, 0.602] | - | 0.727 (33) | 0.076 | flat -0.043 (noise 0.038) |
| reversal_k3_next | 0.583 (60) | 0.578 (609) [0.544, 0.613] | 0.587 (2357) [0.571, 0.601] | 0.587 (2440) [0.572, 0.602] | - | 0.505 (105) | 0.292 | flat -0.012 (noise 0.030) |
| reversal_k3_now | 0.926 (54) | 0.950 (379) [0.939, 0.962] | 0.942 (1712) [0.933, 0.950] | 0.942 (1763) [0.933, 0.950] | - | 0.929 (42) | 0.292 | flat +0.004 (noise 0.016) |
| reversal_k5_next | 0.483 (120) | 0.474 (498) [0.440, 0.498] | 0.492 (1936) [0.474, 0.510] | 0.494 (1990) [0.477, 0.511] | - | 0.401 (142) | 0.187 | flat -0.055 (noise 0.034) |
| reversal_k5_now | 0.848 (59) | 0.870 (354) [0.850, 0.895] | 0.835 (1570) [0.820, 0.851] | 0.837 (1611) [0.823, 0.852] | - | 0.826 (46) | 0.187 | flat +0.049 (noise 0.026) |
| reversal_k8_next | 0.404 (47) | 0.383 (389) [0.355, 0.410] | 0.399 (2020) [0.381, 0.418] | 0.396 (2106) [0.379, 0.415] | - | 0.367 (60) | 0.121 | down -0.088 (noise 0.035) |
| reversal_k8_now | 0.745 (51) | 0.739 (325) [0.700, 0.776] | 0.712 (1546) [0.692, 0.734] | 0.714 (1587) [0.695, 0.735] | - | 0.784 (37) | 0.121 | flat -0.016 (noise 0.033) |
| overall | 0.499 (22076) | 0.504 (154277) [0.502, 0.506] | 0.503 (661202) [0.502, 0.504] | 0.503 (683281) [0.502, 0.504] | - | 0.496 (17103) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.04436, 0.06576] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5075, 'levels': [{'threshold': 0.04436, 'calls_per_day': 140.7, 'win_rate': 0.503}, {'threshold': 0.06576, 'calls_per_day': 35.2, 'win_rate': 0.5484}]}

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15252 | 0.335 | 0.503 (15053) | - | 0.782 (2339) |
| volatility: normal | 15253 | 0.361 | 0.508 (15189) | - | 0.767 (2112) |
| volatility: wild | 15251 | 0.373 | 0.491 (15206) | - | 0.784 (2140) |
| session: Asia 00-08 | 15360 | 0.352 | 0.499 (15252) | - | 0.782 (2173) |
| session: Europe 08-13 | 9600 | 0.351 | 0.505 (9535) | - | 0.767 (1460) |
| session: US 13-21 | 15216 | 0.366 | 0.499 (15135) | - | 0.781 (2214) |
| session: late 21-24 | 5580 | 0.353 | 0.500 (5526) | - | 0.775 (744) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.315 | 0.297 | 0.158 | 0.158 | 0.567 | 0.260 | 0.370 | 1.317 |
| 6h | 360 | 0.315 | 0.309 | 0.228 | 0.237 | 0.531 | 0.230 | 0.400 | 1.292 |
| 24h | 1440 | 0.322 | 0.320 | 0.244 | 0.264 | 0.502 | 0.225 | 0.419 | 1.192 |
| 7d | 10080 | 0.357 | 0.358 | 0.286 | 0.312 | 0.505 | 0.243 | 0.472 | 1.347 |
| 30d | 43200 | 0.356 | 0.356 | 0.279 | 0.310 | 0.501 | 0.245 | 0.466 | 1.280 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.315 / 0.567 / 0.850; 2: 0.276 / 0.533 / 0.900; 3: 0.289 / 0.467 / 0.917; 4: 0.274 / 0.467 / 0.950; 5: 0.257 / 0.450 / 0.917; 6: 0.302 / 0.500 / 0.983; 7: 0.286 / 0.433 / 0.967; 8: 0.286 / 0.500 / 0.950; 9: 0.277 / 0.400 / 0.983; 10: 0.284 / 0.533 / 0.983; 11: 0.275 / 0.467 / 0.967; 12: 0.305 / 0.550 / 0.983; 13: 0.317 / 0.600 / 0.967; 14: 0.295 / 0.517 / 0.950; 15: 0.273 / 0.467 / 0.950
- 6h: 1: 0.315 / 0.531 / 0.864; 2: 0.298 / 0.466 / 0.900; 3: 0.306 / 0.528 / 0.906; 4: 0.309 / 0.528 / 0.900; 5: 0.307 / 0.517 / 0.894; 6: 0.301 / 0.494 / 0.911; 7: 0.304 / 0.466 / 0.908; 8: 0.303 / 0.480 / 0.900; 9: 0.298 / 0.458 / 0.911; 10: 0.314 / 0.548 / 0.908; 11: 0.304 / 0.551 / 0.889; 12: 0.302 / 0.500 / 0.872; 13: 0.317 / 0.534 / 0.853; 14: 0.302 / 0.469 / 0.850; 15: 0.298 / 0.460 / 0.856
- 24h: 1: 0.322 / 0.502 / 0.888; 2: 0.323 / 0.500 / 0.894; 3: 0.324 / 0.500 / 0.896; 4: 0.323 / 0.511 / 0.901; 5: 0.318 / 0.499 / 0.897; 6: 0.316 / 0.480 / 0.894; 7: 0.320 / 0.489 / 0.894; 8: 0.313 / 0.477 / 0.893; 9: 0.315 / 0.486 / 0.895; 10: 0.317 / 0.493 / 0.896; 11: 0.323 / 0.536 / 0.891; 12: 0.320 / 0.502 / 0.888; 13: 0.320 / 0.499 / 0.885; 14: 0.317 / 0.486 / 0.886; 15: 0.312 / 0.468 / 0.886
- 7d: 1: 0.357 / 0.505 / 0.899; 2: 0.352 / 0.491 / 0.900; 3: 0.356 / 0.509 / 0.899; 4: 0.351 / 0.494 / 0.900; 5: 0.352 / 0.508 / 0.899; 6: 0.350 / 0.500 / 0.898; 7: 0.351 / 0.499 / 0.898; 8: 0.350 / 0.506 / 0.898; 9: 0.347 / 0.493 / 0.899; 10: 0.349 / 0.505 / 0.899; 11: 0.349 / 0.506 / 0.898; 12: 0.351 / 0.509 / 0.898; 13: 0.350 / 0.504 / 0.897; 14: 0.347 / 0.496 / 0.897; 15: 0.347 / 0.498 / 0.897
- 30d: 1: 0.356 / 0.501 / 0.899; 2: 0.353 / 0.497 / 0.900; 3: 0.354 / 0.506 / 0.900; 4: 0.351 / 0.499 / 0.900; 5: 0.351 / 0.501 / 0.900; 6: 0.351 / 0.505 / 0.900; 7: 0.350 / 0.506 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.499 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.348 / 0.502 / 0.900; 12: 0.347 / 0.501 / 0.900; 13: 0.347 / 0.500 / 0.900; 14: 0.346 / 0.495 / 0.900; 15: 0.345 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.102 (body 0.076, range 0.129); 'price stays where it was' would score 0.119; colour right 0.517; typical miss of the close 3.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.090 (body 0.059, range 0.121); 'price stays where it was' would score 0.066; colour right 0.508; typical miss of the close 4.2 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.108 (body 0.070, range 0.145); 'price stays where it was' would score 0.109; colour right 0.501; typical miss of the close 4.4 bp; chain ended on the right side 0.526 of 95 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.158); 'price stays where it was' would score 0.118; colour right 0.495; typical miss of the close 7.7 bp; chain ended on the right side 0.525 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.3 bp; chain ended on the right side 0.510 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.4; 2: 0.197 / 4.5; 3: 0.169 / 6.3; 4: 0.133 / 6.6; 5: 0.122 / 7.4; 6: 0.113 / 8.3; 7: 0.102 / 8.7; 8: 0.093 / 9.3; 9: 0.089 / 9.4; 10: 0.084 / 10.3; 11: 0.078 / 10.8; 12: 0.076 / 11.2; 13: 0.068 / 11.6; 14: 0.068 / 11.6; 15: 0.063 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 88710, probability skill vs chance 0.2278, widened contest next: True
  - now: threshold 0.839, hit rate recent 0.9197 / long run 0.9407
    - 6h: 8 calls (32 a day), hit rate 0.875, chance 0.292, naive rule 0.493, lift 3.00x
    - 24h: 53 calls (53 a day), hit rate 0.906, chance 0.293, naive rule 0.498, lift 3.09x
    - 7d: 381 calls (54 a day), hit rate 0.948, chance 0.289, naive rule 0.483, lift 3.28x
    - 30d: 1707 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.481, lift 3.22x
  - next: threshold 0.5323, hit rate recent 0.5151 / long run 0.5724
    - 6h: 39 calls (158 a day), hit rate 0.513, chance 0.292, lift 1.76x
    - 24h: 121 calls (121 a day), hit rate 0.488, chance 0.293, lift 1.66x
    - 7d: 666 calls (95 a day), hit rate 0.574, chance 0.289, lift 1.99x
    - 30d: 2410 calls (80 a day), hit rate 0.582, chance 0.292, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.493; 0.35: 538, 0.518; 0.40: 490, 0.559; 0.45: 423, 0.624; 0.50: 369, 0.679; 0.55: 322, 0.724; 0.60: 275, 0.765; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 140, 0.868; 0.80: 100, 0.906; 0.85: 49, 0.949; 0.90: 1, 0.971
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 496, 0.459; 0.40: 413, 0.487; 0.45: 317, 0.518; 0.50: 209, 0.549; 0.55: 94, 0.585; 0.60: 13, 0.607; 0.65: 0, 0.769
- **K=5**: model 1790208000, labels learned 88708, probability skill vs chance 0.2187, widened contest next: True
  - now: threshold 0.7082, hit rate recent 0.8298 / long run 0.8397
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.184, naive rule 0.371, lift 3.95x
    - 24h: 57 calls (57 a day), hit rate 0.807, chance 0.191, naive rule 0.395, lift 4.22x
    - 7d: 360 calls (51 a day), hit rate 0.861, chance 0.186, naive rule 0.392, lift 4.63x
    - 30d: 1582 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.48x
  - next: threshold 0.3873, hit rate recent 0.4057 / long run 0.4738
    - 6h: 45 calls (184 a day), hit rate 0.378, chance 0.184, lift 2.05x
    - 24h: 178 calls (179 a day), hit rate 0.399, chance 0.191, lift 2.09x
    - 7d: 619 calls (88 a day), hit rate 0.452, chance 0.186, lift 2.43x
    - 30d: 2040 calls (68 a day), hit rate 0.487, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 434, 0.410; 0.35: 374, 0.461; 0.40: 303, 0.530; 0.45: 248, 0.587; 0.50: 193, 0.647; 0.55: 148, 0.696; 0.60: 116, 0.737; 0.65: 88, 0.780; 0.70: 64, 0.818; 0.75: 35, 0.856; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.423; 0.40: 169, 0.447; 0.45: 89, 0.472; 0.50: 23, 0.512; 0.55: 3, 0.578
- **K=8**: model 1790553600, labels learned 88705, probability skill vs chance 0.1996, widened contest next: False
  - now: threshold 0.563, hit rate recent 0.7398 / long run 0.7272
    - 6h: 7 calls (29 a day), hit rate 0.429, chance 0.100, naive rule 0.292, lift 4.29x
    - 24h: 48 calls (48 a day), hit rate 0.750, chance 0.114, naive rule 0.312, lift 6.56x
    - 7d: 322 calls (46 a day), hit rate 0.736, chance 0.121, naive rule 0.326, lift 6.07x
    - 30d: 1546 calls (52 a day), hit rate 0.717, chance 0.122, naive rule 0.327, lift 5.90x
  - next: threshold 0.3603, hit rate recent 0.3774 / long run 0.4026
    - 6h: 22 calls (91 a day), hit rate 0.364, chance 0.100, lift 3.64x
    - 24h: 67 calls (67 a day), hit rate 0.358, chance 0.114, lift 3.13x
    - 7d: 415 calls (59 a day), hit rate 0.369, chance 0.121, lift 3.04x
    - 30d: 2019 calls (67 a day), hit rate 0.399, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 279, 0.395; 0.35: 210, 0.470; 0.40: 163, 0.534; 0.45: 129, 0.584; 0.50: 98, 0.625; 0.55: 69, 0.678; 0.60: 46, 0.722; 0.65: 25, 0.755; 0.70: 9, 0.799; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 191, 0.342; 0.35: 120, 0.380; 0.40: 50, 0.406; 0.45: 10, 0.427; 0.50: 1, 0.452
- **K=13**: model 1790208000, labels learned 88700, probability skill vs chance 0.1864, widened contest next: False
  - now: threshold 0.4088, hit rate recent 0.6487 / long run 0.591
    - 6h: 6 calls (25 a day), hit rate 0.667, chance 0.088, naive rule 0.324, lift 7.54x
    - 24h: 45 calls (45 a day), hit rate 0.689, chance 0.081, naive rule 0.277, lift 8.46x
    - 7d: 340 calls (49 a day), hit rate 0.591, chance 0.078, naive rule 0.265, lift 7.54x
    - 30d: 1423 calls (47 a day), hit rate 0.587, chance 0.077, naive rule 0.267, lift 7.66x
  - next: threshold 0.2691, hit rate recent 0.2904 / long run 0.2949
    - 6h: 30 calls (125 a day), hit rate 0.300, chance 0.088, lift 3.39x
    - 24h: 89 calls (90 a day), hit rate 0.292, chance 0.081, lift 3.59x
    - 7d: 625 calls (89 a day), hit rate 0.269, chance 0.078, lift 3.43x
    - 30d: 1997 calls (67 a day), hit rate 0.307, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.433; 0.35: 91, 0.490; 0.40: 65, 0.537; 0.45: 45, 0.595; 0.50: 29, 0.615; 0.55: 17, 0.655; 0.60: 7, 0.674; 0.65: 2, 0.754; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.316; 0.35: 18, 0.348; 0.40: 4, 0.328; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.546 | 0.03% | 0.883 | 0.517 | 0.249 | 0.550 | 0.219 |
| 6h | 5.136 | 6.46% | 0.872 | 0.511 | 0.250 | 0.520 | 0.341 |
| 24h | 7.145 | 11.72% | 0.892 | 0.501 | 0.250 | 0.499 | 0.647 |
| 7d | 12.878 | 4.10% | 0.900 | 0.501 | 0.251 | 0.498 | 0.668 |
| 30d | 14.448 | 4.18% | 0.900 | 0.500 | 0.251 | 0.499 | 0.678 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.548 | 7.706 | 7.540 | 7.564 | 7.824 | 7.611 | 7.529 | 7.553 | 7.548 | 7.546 |
| 6h | 5.491 | 5.186 | 5.181 | 5.179 | 5.309 | 5.509 | 5.120 | 5.128 | 5.126 | 5.136 |
| 24h | 8.094 | 7.272 | 7.304 | 7.172 | 7.405 | 7.545 | 7.152 | 7.133 | 7.141 | 7.145 |
| 7d | 13.428 | 12.979 | 12.957 | 12.888 | 13.123 | 13.043 | 12.870 | 12.865 | 12.854 | 12.878 |
| 30d | 15.078 | 14.587 | 14.538 | 14.474 | 14.731 | 14.665 | 14.456 | 14.421 | 14.421 | 14.448 |

## Next candle

- candle starting 2026-10-03 18:36 UTC, last close 2684.87
- P(up) 0.5384, return quantiles (bp): {'05': -2.676, '10': -1.917, '25': -0.727, '40': -0.15, '50': 0.087, '60': 0.281, '75': 0.984, '90': 2.101, '95': 2.848}
- changepoint probability 0.0286, regime age 36.3 min
- agent weights: empirical 0.003, ewma 0.131, garch 0.074, har 0.167, bocpd 0.033, hmm 0.005, online_qr 0.298, lgbm 0.289

## Learning log

- 2026-10-01 12:00 UTC: {"garch": {"alpha": 0.0765, "beta": 0.9081}, "hmm": {"sd_bp": [2.71, 5.1, 11.27], "stay": [0.946, 0.958, 0.953]}}
- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.66, 5.39, 13.26], current probabilities: [0.966, 0.033, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-03 18:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.173, 'l_abs': 0.642, 'l_hi': 0.767, 'l_lo': 0.721, 'b05': 0.645, 'b25': 0.675, 'b75': 0.649, 'b95': 0.663}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.532, 1.957, 2.31, 2.693, 3.016, 3.199, 3.567, 3.716, 3.925, 4.38, 4.317, 4.593, 4.681, 4.855]}
- calibration offsets (in sigma): {'05': -0.0025, '10': 0.035, '25': 0.0775, '40': 0.08, '50': 0.045, '60': -0.03, '75': 0.0025, '90': 0.015, '95': -0.0075}
