# ETH-USD 60s candle generator - report

- generated: 2026-10-16 19:00 UTC
- last closed candle: 2026-10-16 19:00 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.507 (671) [0.482, 0.535] | 0.514 (2875) [0.495, 0.533] | 0.509 (4218) [0.493, 0.524] | 0.503 (1246) [0.474, 0.534] | 0.553 (76) | 0.500 | flat +0.001 (noise 0.035) |
| colour_clear | 0.545 (791) | 0.540 (5524) [0.534, 0.546] | 0.516 (23376) [0.508, 0.525] | 0.510 (34272) [0.504, 0.516] | 0.543 (10034) [0.537, 0.549] | 0.525 (648) | 0.500 | flat -0.000 (noise 0.010) |
| colour_confident | 0.595 (84) | 0.599 (877) [0.574, 0.634] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.618 (68) | 0.500 | flat -0.009 (noise 0.030) |
| colour_next | 0.517 (1436) | 0.524 (9978) [0.519, 0.530] | 0.512 (42876) [0.507, 0.518] | 0.508 (62869) [0.504, 0.512] | 0.527 (18520) [0.522, 0.533] | 0.517 (1138) | 0.500 | flat -0.003 (noise 0.007) |
| colour_path | 0.511 (20104) | 0.503 (139692) [0.501, 0.505] | 0.501 (600264) [0.500, 0.503] | 0.501 (880166) [0.500, 0.502] | 0.501 (259280) [0.498, 0.503] | 0.496 (15932) | 0.500 | flat +0.005 (noise 0.003) |
| colour_strong | 0.846 (13) | 0.681 (226) [0.638, 0.761] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.588 (17) | 0.500 | flat +0.047 (noise 0.051) |
| reversal_k13_next | 0.327 (52) | 0.317 (457) [0.291, 0.344] | 0.315 (2025) [0.300, 0.331] | 0.306 (3029) [0.293, 0.319] | 0.319 (924) [0.303, 0.334] | 0.286 (56) | 0.077 | flat +0.005 (noise 0.030) |
| reversal_k13_now | 0.490 (51) | 0.575 (348) [0.539, 0.611] | 0.588 (1478) [0.570, 0.609] | 0.581 (2159) [0.564, 0.598] | 0.581 (687) [0.552, 0.612] | 0.500 (64) | 0.077 | flat -0.016 (noise 0.036) |
| reversal_k3_next | 0.563 (87) | 0.578 (692) [0.558, 0.599] | 0.582 (2499) [0.567, 0.597] | 0.583 (3619) [0.572, 0.596] | 0.575 (1179) [0.557, 0.596] | 0.560 (116) | 0.293 | flat +0.006 (noise 0.028) |
| reversal_k3_now | 0.915 (47) | 0.930 (398) [0.915, 0.948] | 0.938 (1716) [0.930, 0.946] | 0.938 (2506) [0.931, 0.945] | 0.929 (743) [0.919, 0.940] | 0.979 (48) | 0.293 | flat +0.002 (noise 0.018) |
| reversal_k5_next | 0.434 (106) | 0.487 (599) [0.467, 0.509] | 0.484 (2200) [0.467, 0.501] | 0.484 (3111) [0.469, 0.499] | 0.466 (1121) [0.444, 0.490] | 0.390 (100) | 0.187 | flat +0.039 (noise 0.028) |
| reversal_k5_now | 0.755 (53) | 0.812 (345) [0.785, 0.839] | 0.828 (1579) [0.812, 0.844] | 0.831 (2294) [0.818, 0.844] | 0.817 (683) [0.794, 0.840] | 0.852 (54) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.383 (94) | 0.402 (545) [0.384, 0.420] | 0.407 (2132) [0.391, 0.424] | 0.395 (3191) [0.383, 0.409] | 0.394 (1085) [0.376, 0.412] | 0.294 (102) | 0.121 | flat +0.015 (noise 0.029) |
| reversal_k8_now | 0.651 (43) | 0.680 (353) [0.645, 0.714] | 0.714 (1569) [0.694, 0.736] | 0.708 (2300) [0.691, 0.725] | 0.696 (713) [0.666, 0.726] | 0.654 (52) | 0.122 | flat -0.035 (noise 0.033) |
| overall | 0.512 (22169) | 0.506 (154078) [0.504, 0.508] | 0.504 (661213) [0.503, 0.505] | 0.503 (969462) [0.502, 0.504] | 0.504 (286181) [0.502, 0.507] | 0.499 (17738) | - | flat +0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07393, 0.1158] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5241, 'levels': [{'threshold': 0.07393, 'calls_per_day': 140.9, 'win_rate': 0.5914}, {'threshold': 0.1158, 'calls_per_day': 35.8, 'win_rate': 0.668}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 18520, 'rate': 0.5278}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15260 | 0.337 | 0.518 (15026) | 0.602 (1245) | 0.775 (2482) |
| volatility: normal | 15260 | 0.363 | 0.514 (15200) | 0.590 (361) | 0.775 (2190) |
| volatility: wild | 15260 | 0.376 | 0.502 (15221) | 0.643 (154) | 0.762 (2098) |
| session: Asia 00-08 | 15360 | 0.356 | 0.518 (15263) | 0.604 (637) | 0.768 (2249) |
| session: Europe 08-13 | 9600 | 0.352 | 0.510 (9521) | 0.589 (450) | 0.778 (1490) |
| session: US 13-21 | 15240 | 0.367 | 0.506 (15145) | 0.585 (426) | 0.776 (2210) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.660 (247) | 0.750 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.397 | 0.384 | 0.264 | 0.264 | 0.600 | 0.281 | 0.513 | 1.594 |
| 6h | 360 | 0.385 | 0.378 | 0.315 | 0.350 | 0.517 | 0.263 | 0.507 | 1.192 |
| 24h | 1440 | 0.373 | 0.366 | 0.295 | 0.324 | 0.513 | 0.256 | 0.489 | 1.196 |
| 7d | 10080 | 0.358 | 0.350 | 0.274 | 0.304 | 0.524 | 0.258 | 0.458 | 1.305 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.310 | 0.513 | 0.251 | 0.466 | 1.304 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.397 / 0.600 / 0.967; 2: 0.361 / 0.450 / 0.950; 3: 0.387 / 0.583 / 0.950; 4: 0.344 / 0.417 / 0.917; 5: 0.373 / 0.483 / 0.917; 6: 0.357 / 0.483 / 0.900; 7: 0.361 / 0.517 / 0.883; 8: 0.361 / 0.517 / 0.933; 9: 0.389 / 0.650 / 0.917; 10: 0.361 / 0.483 / 0.950; 11: 0.349 / 0.517 / 0.950; 12: 0.393 / 0.683 / 0.933; 13: 0.338 / 0.400 / 0.933; 14: 0.350 / 0.483 / 0.917; 15: 0.346 / 0.433 / 0.917
- 6h: 1: 0.385 / 0.517 / 0.903; 2: 0.383 / 0.517 / 0.908; 3: 0.375 / 0.489 / 0.883; 4: 0.387 / 0.539 / 0.889; 5: 0.374 / 0.494 / 0.878; 6: 0.370 / 0.492 / 0.875; 7: 0.375 / 0.514 / 0.869; 8: 0.379 / 0.528 / 0.881; 9: 0.379 / 0.547 / 0.861; 10: 0.358 / 0.456 / 0.867; 11: 0.364 / 0.492 / 0.883; 12: 0.368 / 0.506 / 0.856; 13: 0.373 / 0.478 / 0.853; 14: 0.367 / 0.503 / 0.853; 15: 0.377 / 0.528 / 0.856
- 24h: 1: 0.373 / 0.513 / 0.897; 2: 0.363 / 0.503 / 0.894; 3: 0.364 / 0.498 / 0.892; 4: 0.368 / 0.526 / 0.893; 5: 0.363 / 0.485 / 0.892; 6: 0.362 / 0.491 / 0.890; 7: 0.361 / 0.497 / 0.888; 8: 0.363 / 0.497 / 0.887; 9: 0.368 / 0.542 / 0.887; 10: 0.358 / 0.477 / 0.887; 11: 0.359 / 0.487 / 0.892; 12: 0.360 / 0.497 / 0.889; 13: 0.360 / 0.485 / 0.890; 14: 0.358 / 0.501 / 0.893; 15: 0.358 / 0.494 / 0.895
- 7d: 1: 0.358 / 0.524 / 0.902; 2: 0.348 / 0.499 / 0.900; 3: 0.350 / 0.510 / 0.902; 4: 0.346 / 0.498 / 0.899; 5: 0.349 / 0.506 / 0.899; 6: 0.348 / 0.502 / 0.898; 7: 0.346 / 0.503 / 0.898; 8: 0.346 / 0.502 / 0.897; 9: 0.346 / 0.504 / 0.897; 10: 0.347 / 0.506 / 0.897; 11: 0.343 / 0.494 / 0.898; 12: 0.345 / 0.504 / 0.897; 13: 0.345 / 0.503 / 0.896; 14: 0.343 / 0.501 / 0.897; 15: 0.346 / 0.504 / 0.897
- 30d: 1: 0.358 / 0.513 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.504 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.350 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.503 / 0.899; 13: 0.347 / 0.502 / 0.899; 14: 0.346 / 0.498 / 0.899; 15: 0.346 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.141 (body 0.082, range 0.201); 'price stays where it was' would score 0.270; colour right 0.433; typical miss of the close 16.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.103 (body 0.056, range 0.149); 'price stays where it was' would score 0.131; colour right 0.500; typical miss of the close 19.4 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.114 (body 0.073, range 0.155); 'price stays where it was' would score 0.124; colour right 0.480; typical miss of the close 11.6 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.120 (body 0.082, range 0.159); 'price stays where it was' would score 0.127; colour right 0.494; typical miss of the close 7.9 bp; chain ended on the right side 0.513 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 8.0 bp; chain ended on the right side 0.517 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.1; 2: 0.196 / 4.5; 3: 0.165 / 6.1; 4: 0.133 / 6.8; 5: 0.120 / 7.5; 6: 0.109 / 8.1; 7: 0.101 / 8.3; 8: 0.096 / 8.8; 9: 0.086 / 8.8; 10: 0.084 / 9.5; 11: 0.079 / 10.3; 12: 0.076 / 10.6; 13: 0.063 / 10.9; 14: 0.065 / 11.3; 15: 0.058 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 107454, probability skill vs chance 0.2206, widened contest next: True
  - now: threshold 0.8406, hit rate recent 0.963 / long run 0.937
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.268, naive rule 0.439, lift 3.74x
    - 24h: 60 calls (60 a day), hit rate 0.983, chance 0.282, naive rule 0.465, lift 3.48x
    - 7d: 395 calls (56 a day), hit rate 0.937, chance 0.295, naive rule 0.496, lift 3.17x
    - 30d: 1715 calls (57 a day), hit rate 0.938, chance 0.290, naive rule 0.481, lift 3.23x
  - next: threshold 0.5542, hit rate recent 0.5288 / long run 0.5722
    - 6h: 32 calls (130 a day), hit rate 0.500, chance 0.268, lift 1.87x
    - 24h: 139 calls (139 a day), hit rate 0.576, chance 0.282, lift 2.04x
    - 7d: 738 calls (105 a day), hit rate 0.576, chance 0.295, lift 1.95x
    - 30d: 2556 calls (85 a day), hit rate 0.579, chance 0.290, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.489; 0.35: 540, 0.513; 0.40: 484, 0.562; 0.45: 415, 0.632; 0.50: 362, 0.685; 0.55: 317, 0.727; 0.60: 270, 0.772; 0.65: 224, 0.800; 0.70: 179, 0.834; 0.75: 139, 0.870; 0.80: 95, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 498, 0.459; 0.40: 409, 0.489; 0.45: 314, 0.524; 0.50: 204, 0.558; 0.55: 92, 0.577; 0.60: 14, 0.596; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 107452, probability skill vs chance 0.2022, widened contest next: True
  - now: threshold 0.6961, hit rate recent 0.8264 / long run 0.8239
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.184, naive rule 0.376, lift 4.94x
    - 24h: 66 calls (66 a day), hit rate 0.864, chance 0.174, naive rule 0.373, lift 4.96x
    - 7d: 360 calls (51 a day), hit rate 0.819, chance 0.186, naive rule 0.403, lift 4.40x
    - 30d: 1593 calls (53 a day), hit rate 0.830, chance 0.187, naive rule 0.392, lift 4.45x
  - next: threshold 0.4257, hit rate recent 0.3883 / long run 0.4636
    - 6h: 33 calls (135 a day), hit rate 0.364, chance 0.184, lift 1.97x
    - 24h: 115 calls (116 a day), hit rate 0.426, chance 0.174, lift 2.45x
    - 7d: 636 calls (91 a day), hit rate 0.472, chance 0.186, lift 2.53x
    - 30d: 2260 calls (75 a day), hit rate 0.479, chance 0.187, lift 2.56x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.418; 0.35: 354, 0.481; 0.40: 284, 0.554; 0.45: 232, 0.610; 0.50: 182, 0.663; 0.55: 138, 0.707; 0.60: 108, 0.748; 0.65: 82, 0.792; 0.70: 60, 0.824; 0.75: 33, 0.866; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.388; 0.35: 251, 0.422; 0.40: 161, 0.451; 0.45: 78, 0.467; 0.50: 18, 0.502; 0.55: 2, 0.549
- **K=8**: model 1791936000, labels learned 107449, probability skill vs chance 0.1858, widened contest next: True
  - now: threshold 0.5821, hit rate recent 0.6649 / long run 0.695
    - 6h: 16 calls (66 a day), hit rate 0.750, chance 0.104, naive rule 0.265, lift 7.19x
    - 24h: 64 calls (64 a day), hit rate 0.641, chance 0.114, naive rule 0.298, lift 5.62x
    - 7d: 369 calls (53 a day), hit rate 0.683, chance 0.122, naive rule 0.338, lift 5.60x
    - 30d: 1578 calls (53 a day), hit rate 0.713, chance 0.122, naive rule 0.329, lift 5.84x
  - next: threshold 0.3408, hit rate recent 0.2888 / long run 0.3794
    - 6h: 31 calls (128 a day), hit rate 0.258, chance 0.104, lift 2.47x
    - 24h: 122 calls (123 a day), hit rate 0.328, chance 0.114, lift 2.88x
    - 7d: 577 calls (83 a day), hit rate 0.380, chance 0.122, lift 3.11x
    - 30d: 2151 calls (72 a day), hit rate 0.401, chance 0.122, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.417; 0.35: 196, 0.490; 0.40: 150, 0.551; 0.45: 118, 0.594; 0.50: 90, 0.635; 0.55: 65, 0.685; 0.60: 44, 0.725; 0.65: 24, 0.778; 0.70: 9, 0.837; 0.75: 1, 0.783
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.352; 0.35: 107, 0.386; 0.40: 44, 0.416; 0.45: 9, 0.444; 0.50: 1, 0.382
- **K=13**: model 1792022400, labels learned 107444, probability skill vs chance 0.165, widened contest next: True
  - now: threshold 0.427, hit rate recent 0.5001 / long run 0.5685
    - 6h: 19 calls (79 a day), hit rate 0.526, chance 0.078, naive rule 0.230, lift 6.73x
    - 24h: 76 calls (77 a day), hit rate 0.474, chance 0.073, naive rule 0.236, lift 6.52x
    - 7d: 373 calls (53 a day), hit rate 0.550, chance 0.079, naive rule 0.281, lift 6.95x
    - 30d: 1510 calls (50 a day), hit rate 0.584, chance 0.078, naive rule 0.272, lift 7.50x
  - next: threshold 0.3008, hit rate recent 0.2669 / long run 0.3072
    - 6h: 21 calls (88 a day), hit rate 0.143, chance 0.078, lift 1.83x
    - 24h: 69 calls (70 a day), hit rate 0.319, chance 0.073, lift 4.39x
    - 7d: 453 calls (65 a day), hit rate 0.309, chance 0.079, lift 3.91x
    - 30d: 2043 calls (68 a day), hit rate 0.312, chance 0.078, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.452; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.617; 0.50: 25, 0.655; 0.55: 13, 0.705; 0.60: 4, 0.766; 0.65: 0, 0.938
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.322; 0.35: 13, 0.356; 0.40: 2, 0.385

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 24.544 | 4.97% | 0.917 | 0.533 | 0.255 | 0.483 | 0.401 |
| 6h | 25.009 | 5.53% | 0.889 | 0.486 | 0.251 | 0.489 | 0.475 |
| 24h | 16.698 | 4.83% | 0.890 | 0.496 | 0.251 | 0.492 | 0.615 |
| 7d | 14.635 | 4.22% | 0.900 | 0.499 | 0.251 | 0.490 | 0.674 |
| 30d | 14.126 | 3.96% | 0.900 | 0.500 | 0.251 | 0.496 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 25.828 | 25.329 | 24.312 | 24.741 | 25.646 | 24.505 | 24.451 | 24.387 | 24.392 | 24.544 |
| 6h | 26.473 | 25.453 | 24.991 | 25.110 | 25.451 | 25.109 | 25.099 | 25.136 | 24.998 | 25.009 |
| 24h | 17.546 | 16.917 | 16.762 | 16.719 | 16.967 | 16.781 | 16.697 | 16.715 | 16.673 | 16.698 |
| 7d | 15.279 | 14.799 | 14.719 | 14.651 | 14.893 | 14.827 | 14.643 | 14.613 | 14.607 | 14.635 |
| 30d | 14.708 | 14.253 | 14.208 | 14.152 | 14.382 | 14.308 | 14.124 | 14.098 | 14.099 | 14.126 |

## Next candle

- candle starting 2026-10-16 19:00 UTC, last close 2403.19
- P(up) 0.4657, return quantiles (bp): {'05': -18.534, '10': -14.593, '25': -7.767, '40': -3.755, '50': -0.871, '60': 1.716, '75': 6.825, '90': 13.135, '95': 17.704}
- changepoint probability 0.1328, regime age 16.1 min
- agent weights: empirical 0.003, ewma 0.026, garch 0.230, har 0.169, bocpd 0.024, hmm 0.172, online_qr 0.202, lgbm 0.173

## Learning log

- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- HMM volatility states (sd, bp per minute): [3.83, 6.59, 20.28], current probabilities: [0.008, 0.828, 0.165]
- live generator: {'versions': 60, 'latest_effective': '2026-10-16 19:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.249, 'l_abs': 0.782, 'l_hi': 0.737, 'l_lo': 0.726, 'b05': 0.78, 'b25': 0.701, 'b75': 0.728, 'b95': 0.776}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.55, 2.061, 2.385, 2.837, 3.441, 3.8, 4.07, 4.593, 4.661, 4.432, 5.444, 5.792, 6.023, 6.123]}
- calibration offsets (in sigma): {'05': 0.0395, '10': -0.021, '25': -0.0425, '40': -0.084, '50': -0.065, '60': -0.056, '75': -0.0075, '90': -0.039, '95': -0.0295}
