# ETH-USD 60s candle generator - report

- generated: 2026-10-16 11:38 UTC
- last closed candle: 2026-10-16 11:38 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.507 (671) [0.482, 0.535] | 0.514 (2875) [0.495, 0.533] | 0.509 (4218) [0.493, 0.524] | 0.503 (1246) [0.474, 0.534] | 0.457 (46) | 0.500 | flat +0.001 (noise 0.035) |
| colour_clear | 0.545 (791) | 0.540 (5524) [0.534, 0.546] | 0.516 (23376) [0.508, 0.525] | 0.510 (34272) [0.504, 0.516] | 0.543 (10034) [0.537, 0.549] | 0.504 (393) | 0.500 | flat -0.000 (noise 0.010) |
| colour_confident | 0.595 (84) | 0.599 (877) [0.574, 0.634] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.594 (64) | 0.500 | flat -0.009 (noise 0.030) |
| colour_next | 0.517 (1436) | 0.524 (9978) [0.519, 0.530] | 0.512 (42876) [0.507, 0.518] | 0.508 (62869) [0.504, 0.512] | 0.527 (18520) [0.522, 0.533] | 0.504 (696) | 0.500 | flat -0.003 (noise 0.007) |
| colour_path | 0.511 (20104) | 0.503 (139692) [0.501, 0.505] | 0.501 (600264) [0.500, 0.503] | 0.501 (880166) [0.500, 0.502] | 0.501 (259280) [0.498, 0.503] | 0.489 (9744) | 0.500 | flat +0.005 (noise 0.003) |
| colour_strong | 0.846 (13) | 0.681 (226) [0.638, 0.761] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.562 (16) | 0.500 | flat +0.047 (noise 0.051) |
| reversal_k13_next | 0.327 (52) | 0.317 (457) [0.291, 0.344] | 0.315 (2025) [0.300, 0.331] | 0.306 (3029) [0.293, 0.319] | 0.319 (924) [0.303, 0.334] | 0.440 (25) | 0.077 | flat +0.005 (noise 0.030) |
| reversal_k13_now | 0.490 (51) | 0.575 (348) [0.539, 0.611] | 0.588 (1478) [0.570, 0.609] | 0.581 (2159) [0.564, 0.598] | 0.581 (687) [0.552, 0.612] | 0.452 (42) | 0.077 | flat -0.016 (noise 0.036) |
| reversal_k3_next | 0.563 (87) | 0.578 (692) [0.558, 0.599] | 0.582 (2499) [0.567, 0.597] | 0.583 (3619) [0.572, 0.596] | 0.575 (1179) [0.557, 0.596] | 0.625 (72) | 0.293 | flat +0.006 (noise 0.028) |
| reversal_k3_now | 0.915 (47) | 0.930 (398) [0.915, 0.948] | 0.938 (1716) [0.930, 0.946] | 0.938 (2506) [0.931, 0.945] | 0.929 (743) [0.919, 0.940] | 0.972 (36) | 0.293 | flat +0.002 (noise 0.018) |
| reversal_k5_next | 0.434 (106) | 0.487 (599) [0.467, 0.509] | 0.484 (2200) [0.467, 0.501] | 0.484 (3111) [0.469, 0.499] | 0.466 (1121) [0.444, 0.490] | 0.442 (52) | 0.187 | flat +0.039 (noise 0.028) |
| reversal_k5_now | 0.755 (53) | 0.812 (345) [0.785, 0.839] | 0.828 (1579) [0.812, 0.844] | 0.831 (2294) [0.818, 0.844] | 0.817 (683) [0.794, 0.840] | 0.829 (41) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.383 (94) | 0.402 (545) [0.384, 0.420] | 0.407 (2132) [0.391, 0.424] | 0.395 (3191) [0.383, 0.409] | 0.394 (1085) [0.376, 0.412] | 0.345 (55) | 0.121 | flat +0.015 (noise 0.029) |
| reversal_k8_now | 0.651 (43) | 0.680 (353) [0.645, 0.714] | 0.714 (1569) [0.694, 0.736] | 0.708 (2300) [0.691, 0.725] | 0.696 (713) [0.666, 0.726] | 0.588 (34) | 0.122 | flat -0.035 (noise 0.033) |
| overall | 0.512 (22169) | 0.506 (154078) [0.504, 0.508] | 0.504 (661213) [0.503, 0.505] | 0.503 (969462) [0.502, 0.504] | 0.504 (286181) [0.502, 0.507] | 0.493 (10843) | - | flat +0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07466, 0.1159] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5247, 'levels': [{'threshold': 0.07466, 'calls_per_day': 143.7, 'win_rate': 0.5925}, {'threshold': 0.1159, 'calls_per_day': 35.8, 'win_rate': 0.6759}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 18079, 'rate': 0.5276}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15113 | 0.336 | 0.519 (14879) | 0.603 (1242) | 0.775 (2461) |
| volatility: normal | 15112 | 0.363 | 0.514 (15054) | 0.586 (360) | 0.770 (2157) |
| volatility: wild | 15113 | 0.375 | 0.502 (15072) | 0.636 (154) | 0.767 (2087) |
| session: Asia 00-08 | 15360 | 0.356 | 0.518 (15263) | 0.604 (637) | 0.768 (2249) |
| session: Europe 08-13 | 9518 | 0.352 | 0.509 (9439) | 0.587 (448) | 0.776 (1481) |
| session: US 13-21 | 14880 | 0.367 | 0.506 (14785) | 0.583 (424) | 0.777 (2154) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.660 (247) | 0.750 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.354 | 0.315 | 0.292 | 0.292 | 0.467 | 0.236 | 0.472 | 1.042 |
| 6h | 360 | 0.362 | 0.355 | 0.290 | 0.314 | 0.494 | 0.244 | 0.480 | 1.228 |
| 24h | 1440 | 0.369 | 0.366 | 0.289 | 0.323 | 0.505 | 0.255 | 0.484 | 1.150 |
| 7d | 10080 | 0.357 | 0.350 | 0.273 | 0.304 | 0.524 | 0.257 | 0.457 | 1.299 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.310 | 0.512 | 0.250 | 0.466 | 1.303 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.354 / 0.467 / 0.833; 2: 0.391 / 0.600 / 0.833; 3: 0.336 / 0.467 / 0.867; 4: 0.384 / 0.600 / 0.850; 5: 0.352 / 0.517 / 0.817; 6: 0.340 / 0.467 / 0.767; 7: 0.354 / 0.533 / 0.800; 8: 0.339 / 0.483 / 0.717; 9: 0.362 / 0.517 / 0.733; 10: 0.330 / 0.467 / 0.733; 11: 0.347 / 0.483 / 0.700; 12: 0.353 / 0.567 / 0.733; 13: 0.359 / 0.533 / 0.733; 14: 0.339 / 0.500 / 0.683; 15: 0.323 / 0.483 / 0.667
- 6h: 1: 0.362 / 0.494 / 0.886; 2: 0.356 / 0.483 / 0.853; 3: 0.364 / 0.514 / 0.881; 4: 0.361 / 0.519 / 0.867; 5: 0.358 / 0.475 / 0.894; 6: 0.358 / 0.497 / 0.869; 7: 0.358 / 0.500 / 0.872; 8: 0.357 / 0.475 / 0.864; 9: 0.356 / 0.508 / 0.889; 10: 0.358 / 0.494 / 0.911; 11: 0.349 / 0.450 / 0.903; 12: 0.353 / 0.464 / 0.919; 13: 0.357 / 0.478 / 0.928; 14: 0.349 / 0.453 / 0.917; 15: 0.355 / 0.494 / 0.925
- 24h: 1: 0.369 / 0.505 / 0.899; 2: 0.363 / 0.492 / 0.899; 3: 0.366 / 0.505 / 0.902; 4: 0.363 / 0.499 / 0.904; 5: 0.366 / 0.503 / 0.906; 6: 0.361 / 0.488 / 0.895; 7: 0.362 / 0.500 / 0.895; 8: 0.359 / 0.489 / 0.893; 9: 0.362 / 0.516 / 0.895; 10: 0.363 / 0.494 / 0.897; 11: 0.359 / 0.495 / 0.893; 12: 0.363 / 0.504 / 0.891; 13: 0.356 / 0.489 / 0.894; 14: 0.360 / 0.516 / 0.892; 15: 0.355 / 0.484 / 0.891
- 7d: 1: 0.357 / 0.524 / 0.903; 2: 0.347 / 0.499 / 0.898; 3: 0.350 / 0.512 / 0.898; 4: 0.346 / 0.498 / 0.899; 5: 0.348 / 0.506 / 0.899; 6: 0.347 / 0.502 / 0.899; 7: 0.345 / 0.501 / 0.898; 8: 0.344 / 0.499 / 0.898; 9: 0.344 / 0.500 / 0.899; 10: 0.347 / 0.508 / 0.899; 11: 0.343 / 0.496 / 0.899; 12: 0.344 / 0.503 / 0.899; 13: 0.344 / 0.502 / 0.899; 14: 0.342 / 0.501 / 0.899; 15: 0.345 / 0.503 / 0.898
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.089 (body 0.071, range 0.108); 'price stays where it was' would score 0.131; colour right 0.333; typical miss of the close 15.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.109 (body 0.073, range 0.145); 'price stays where it was' would score 0.103; colour right 0.456; typical miss of the close 9.5 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.132; colour right 0.480; typical miss of the close 11.2 bp; chain ended on the right side 0.417 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.160); 'price stays where it was' would score 0.128; colour right 0.494; typical miss of the close 7.7 bp; chain ended on the right side 0.504 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 8.0 bp; chain ended on the right side 0.513 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.1; 2: 0.196 / 4.6; 3: 0.164 / 6.1; 4: 0.134 / 6.8; 5: 0.120 / 7.5; 6: 0.109 / 8.0; 7: 0.102 / 8.3; 8: 0.096 / 8.8; 9: 0.087 / 8.8; 10: 0.084 / 9.5; 11: 0.078 / 10.3; 12: 0.075 / 10.6; 13: 0.063 / 10.9; 14: 0.065 / 11.2; 15: 0.058 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 107012, probability skill vs chance 0.2252, widened contest next: False
  - now: threshold 0.8409, hit rate recent 0.9547 / long run 0.9358
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.304, naive rule 0.540, lift 3.29x
    - 24h: 64 calls (64 a day), hit rate 0.953, chance 0.287, naive rule 0.480, lift 3.32x
    - 7d: 402 calls (57 a day), hit rate 0.930, chance 0.298, naive rule 0.502, lift 3.12x
    - 30d: 1731 calls (58 a day), hit rate 0.939, chance 0.290, naive rule 0.482, lift 3.23x
  - next: threshold 0.5195, hit rate recent 0.6044 / long run 0.5811
    - 6h: 38 calls (154 a day), hit rate 0.632, chance 0.304, lift 2.08x
    - 24h: 119 calls (119 a day), hit rate 0.597, chance 0.287, lift 2.08x
    - 7d: 725 calls (104 a day), hit rate 0.588, chance 0.298, lift 1.97x
    - 30d: 2537 calls (85 a day), hit rate 0.582, chance 0.290, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.562; 0.45: 415, 0.632; 0.50: 362, 0.686; 0.55: 317, 0.727; 0.60: 271, 0.771; 0.65: 225, 0.800; 0.70: 180, 0.833; 0.75: 139, 0.870; 0.80: 96, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.459; 0.40: 409, 0.489; 0.45: 313, 0.524; 0.50: 204, 0.560; 0.55: 92, 0.580; 0.60: 14, 0.598; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 107010, probability skill vs chance 0.2067, widened contest next: False
  - now: threshold 0.6958, hit rate recent 0.8034 / long run 0.8217
    - 6h: 22 calls (90 a day), hit rate 0.773, chance 0.152, naive rule 0.370, lift 5.10x
    - 24h: 71 calls (71 a day), hit rate 0.817, chance 0.174, naive rule 0.377, lift 4.69x
    - 7d: 362 calls (52 a day), hit rate 0.818, chance 0.188, naive rule 0.409, lift 4.34x
    - 30d: 1600 calls (53 a day), hit rate 0.829, chance 0.187, naive rule 0.394, lift 4.43x
  - next: threshold 0.4221, hit rate recent 0.4542 / long run 0.4744
    - 6h: 28 calls (114 a day), hit rate 0.429, chance 0.152, lift 2.83x
    - 24h: 100 calls (100 a day), hit rate 0.430, chance 0.174, lift 2.47x
    - 7d: 615 calls (88 a day), hit rate 0.491, chance 0.188, lift 2.61x
    - 30d: 2227 calls (74 a day), hit rate 0.482, chance 0.187, lift 2.57x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 354, 0.482; 0.40: 285, 0.554; 0.45: 233, 0.611; 0.50: 182, 0.664; 0.55: 139, 0.708; 0.60: 109, 0.748; 0.65: 82, 0.790; 0.70: 60, 0.822; 0.75: 33, 0.864; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 251, 0.425; 0.40: 161, 0.454; 0.45: 78, 0.471; 0.50: 18, 0.504; 0.55: 2, 0.560
- **K=8**: model 1791936000, labels learned 107007, probability skill vs chance 0.1963, widened contest next: True
  - now: threshold 0.5777, hit rate recent 0.6311 / long run 0.6925
    - 6h: 17 calls (70 a day), hit rate 0.529, chance 0.111, naive rule 0.316, lift 4.75x
    - 24h: 58 calls (58 a day), hit rate 0.586, chance 0.117, naive rule 0.314, lift 5.02x
    - 7d: 366 calls (52 a day), hit rate 0.680, chance 0.124, naive rule 0.346, lift 5.50x
    - 30d: 1583 calls (53 a day), hit rate 0.711, chance 0.123, naive rule 0.331, lift 5.80x
  - next: threshold 0.341, hit rate recent 0.3645 / long run 0.3913
    - 6h: 28 calls (115 a day), hit rate 0.357, chance 0.111, lift 3.21x
    - 24h: 107 calls (108 a day), hit rate 0.364, chance 0.117, lift 3.12x
    - 7d: 558 calls (80 a day), hit rate 0.401, chance 0.124, lift 3.25x
    - 30d: 2138 calls (71 a day), hit rate 0.407, chance 0.123, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.419; 0.35: 196, 0.492; 0.40: 150, 0.551; 0.45: 119, 0.594; 0.50: 91, 0.634; 0.55: 66, 0.682; 0.60: 44, 0.724; 0.65: 24, 0.774; 0.70: 9, 0.830; 0.75: 1, 0.783
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.354; 0.35: 107, 0.389; 0.40: 44, 0.423; 0.45: 9, 0.459; 0.50: 1, 0.364
- **K=13**: model 1792022400, labels learned 107002, probability skill vs chance 0.1754, widened contest next: True
  - now: threshold 0.4141, hit rate recent 0.4714 / long run 0.5678
    - 6h: 24 calls (100 a day), hit rate 0.333, chance 0.070, naive rule 0.238, lift 4.79x
    - 24h: 67 calls (68 a day), hit rate 0.448, chance 0.074, naive rule 0.255, lift 6.08x
    - 7d: 364 calls (52 a day), hit rate 0.560, chance 0.080, naive rule 0.289, lift 7.04x
    - 30d: 1508 calls (50 a day), hit rate 0.584, chance 0.078, naive rule 0.274, lift 7.48x
  - next: threshold 0.3006, hit rate recent 0.3476 / long run 0.315
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.070, lift 6.16x
    - 24h: 54 calls (55 a day), hit rate 0.389, chance 0.074, lift 5.28x
    - 7d: 443 calls (63 a day), hit rate 0.327, chance 0.080, lift 4.11x
    - 30d: 2031 calls (68 a day), hit rate 0.316, chance 0.078, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.453; 0.35: 85, 0.512; 0.40: 61, 0.563; 0.45: 41, 0.615; 0.50: 25, 0.652; 0.55: 14, 0.705; 0.60: 4, 0.754; 0.65: 0, 0.938
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.328; 0.35: 13, 0.365; 0.40: 2, 0.413

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 22.586 | 2.03% | 0.850 | 0.433 | 0.253 | 0.333 | 0.481 |
| 6h | 14.257 | 3.15% | 0.881 | 0.492 | 0.251 | 0.469 | 0.562 |
| 24h | 17.909 | 4.99% | 0.897 | 0.503 | 0.250 | 0.503 | 0.670 |
| 7d | 14.356 | 4.10% | 0.901 | 0.501 | 0.251 | 0.492 | 0.667 |
| 30d | 14.164 | 4.00% | 0.900 | 0.500 | 0.251 | 0.496 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 23.054 | 23.105 | 22.403 | 22.813 | 23.047 | 22.285 | 22.716 | 22.525 | 22.554 | 22.586 |
| 6h | 14.720 | 14.406 | 14.340 | 14.339 | 14.465 | 14.292 | 14.249 | 14.207 | 14.231 | 14.257 |
| 24h | 18.851 | 18.093 | 18.006 | 17.925 | 18.170 | 18.118 | 17.918 | 17.930 | 17.894 | 17.909 |
| 7d | 14.970 | 14.514 | 14.447 | 14.372 | 14.621 | 14.559 | 14.361 | 14.325 | 14.328 | 14.356 |
| 30d | 14.753 | 14.291 | 14.248 | 14.187 | 14.422 | 14.356 | 14.163 | 14.136 | 14.136 | 14.164 |

## Next candle

- candle starting 2026-10-16 11:38 UTC, last close 2477.25
- P(up) 0.5017, return quantiles (bp): {'05': -10.42, '10': -7.882, '25': -3.764, '40': -1.621, '50': 0.018, '60': 1.903, '75': 4.502, '90': 9.443, '95': 11.857}
- changepoint probability 0.1885, regime age 21.4 min
- agent weights: empirical 0.005, ewma 0.062, garch 0.131, har 0.166, bocpd 0.041, hmm 0.113, online_qr 0.229, lgbm 0.254

## Learning log

- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.23, 6.04, 18.9], current probabilities: [0.013, 0.963, 0.024]
- live generator: {'versions': 60, 'latest_effective': '2026-10-16 11:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.184, 'l_abs': 0.771, 'l_hi': 0.734, 'l_lo': 0.736, 'b05': 0.773, 'b25': 0.673, 'b75': 0.716, 'b95': 0.772}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.901, 1.988, 2.347, 2.332, 3.004, 3.317, 3.849, 3.486, 3.467, 3.792, 4.131, 3.977, 4.219, 4.204]}
- calibration offsets (in sigma): {'05': 0.0885, '10': 0.047, '25': 0.0525, '40': -0.012, '50': 0.005, '60': 0.052, '75': 0.0275, '90': 0.083, '95': 0.0015}
