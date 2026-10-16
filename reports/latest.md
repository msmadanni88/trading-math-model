# ETH-USD 60s candle generator - report

- generated: 2026-10-16 22:01 UTC
- last closed candle: 2026-10-16 22:01 UTC (staleness 0.0 min)
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
| chain_end_side | 0.469 (96) | 0.507 (671) [0.482, 0.535] | 0.514 (2875) [0.495, 0.533] | 0.509 (4218) [0.493, 0.524] | 0.503 (1246) [0.474, 0.534] | 0.568 (88) | 0.500 | flat +0.001 (noise 0.035) |
| colour_clear | 0.545 (791) | 0.540 (5524) [0.534, 0.546] | 0.516 (23376) [0.508, 0.525] | 0.510 (34272) [0.504, 0.516] | 0.543 (10034) [0.537, 0.549] | 0.530 (738) | 0.500 | flat -0.000 (noise 0.010) |
| colour_confident | 0.595 (84) | 0.599 (877) [0.574, 0.634] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.618 (76) | 0.500 | flat -0.009 (noise 0.030) |
| colour_next | 0.517 (1436) | 0.524 (9978) [0.519, 0.530] | 0.512 (42876) [0.507, 0.518] | 0.508 (62869) [0.504, 0.512] | 0.527 (18520) [0.522, 0.533] | 0.521 (1315) | 0.500 | flat -0.003 (noise 0.007) |
| colour_path | 0.511 (20104) | 0.503 (139692) [0.501, 0.505] | 0.501 (600264) [0.500, 0.503] | 0.501 (880166) [0.500, 0.502] | 0.501 (259280) [0.498, 0.503] | 0.496 (18410) | 0.500 | flat +0.005 (noise 0.003) |
| colour_strong | 0.846 (13) | 0.681 (226) [0.638, 0.761] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.588 (17) | 0.500 | flat +0.047 (noise 0.051) |
| reversal_k13_next | 0.327 (52) | 0.317 (457) [0.291, 0.344] | 0.315 (2025) [0.300, 0.331] | 0.306 (3029) [0.293, 0.319] | 0.319 (924) [0.303, 0.334] | 0.293 (58) | 0.077 | flat +0.005 (noise 0.030) |
| reversal_k13_now | 0.490 (51) | 0.575 (348) [0.539, 0.611] | 0.588 (1478) [0.570, 0.609] | 0.581 (2159) [0.564, 0.598] | 0.581 (687) [0.552, 0.612] | 0.536 (69) | 0.077 | flat -0.016 (noise 0.036) |
| reversal_k3_next | 0.563 (87) | 0.578 (692) [0.558, 0.599] | 0.582 (2499) [0.567, 0.597] | 0.583 (3619) [0.572, 0.596] | 0.575 (1179) [0.557, 0.596] | 0.564 (126) | 0.293 | flat +0.006 (noise 0.028) |
| reversal_k3_now | 0.915 (47) | 0.930 (398) [0.915, 0.948] | 0.938 (1716) [0.930, 0.946] | 0.938 (2506) [0.931, 0.945] | 0.929 (743) [0.919, 0.940] | 0.982 (54) | 0.293 | flat +0.002 (noise 0.018) |
| reversal_k5_next | 0.434 (106) | 0.487 (599) [0.467, 0.509] | 0.484 (2200) [0.467, 0.501] | 0.484 (3111) [0.469, 0.499] | 0.466 (1121) [0.444, 0.490] | 0.400 (110) | 0.187 | flat +0.039 (noise 0.028) |
| reversal_k5_now | 0.755 (53) | 0.812 (345) [0.785, 0.839] | 0.828 (1579) [0.812, 0.844] | 0.831 (2294) [0.818, 0.844] | 0.817 (683) [0.794, 0.840] | 0.867 (60) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.383 (94) | 0.402 (545) [0.384, 0.420] | 0.407 (2132) [0.391, 0.424] | 0.395 (3191) [0.383, 0.409] | 0.394 (1085) [0.376, 0.412] | 0.292 (113) | 0.121 | flat +0.015 (noise 0.029) |
| reversal_k8_now | 0.651 (43) | 0.680 (353) [0.645, 0.714] | 0.714 (1569) [0.694, 0.736] | 0.708 (2300) [0.691, 0.725] | 0.696 (713) [0.666, 0.726] | 0.667 (54) | 0.122 | flat -0.035 (noise 0.033) |
| overall | 0.512 (22169) | 0.506 (154078) [0.504, 0.508] | 0.504 (661213) [0.503, 0.505] | 0.503 (969462) [0.502, 0.504] | 0.504 (286181) [0.502, 0.507] | 0.499 (20457) | - | flat +0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07393, 0.1158] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5241, 'levels': [{'threshold': 0.07393, 'calls_per_day': 140.9, 'win_rate': 0.5914}, {'threshold': 0.1158, 'calls_per_day': 35.8, 'win_rate': 0.668}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 18697, 'rate': 0.528}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15321 | 0.337 | 0.518 (15087) | 0.602 (1246) | 0.775 (2484) |
| volatility: normal | 15320 | 0.363 | 0.515 (15258) | 0.594 (367) | 0.776 (2195) |
| volatility: wild | 15320 | 0.376 | 0.503 (15279) | 0.639 (155) | 0.763 (2110) |
| session: Asia 00-08 | 15360 | 0.356 | 0.518 (15263) | 0.604 (637) | 0.768 (2249) |
| session: Europe 08-13 | 9600 | 0.352 | 0.510 (9521) | 0.589 (450) | 0.778 (1490) |
| session: US 13-21 | 15360 | 0.367 | 0.507 (15263) | 0.586 (427) | 0.778 (2223) |
| session: late 21-24 | 5641 | 0.351 | 0.513 (5577) | 0.657 (254) | 0.752 (827) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.416 | 0.344 | 0.269 | 0.269 | 0.569 | 0.333 | 0.500 | 1.429 |
| 6h | 360 | 0.389 | 0.374 | 0.298 | 0.319 | 0.545 | 0.282 | 0.496 | 1.262 |
| 24h | 1440 | 0.376 | 0.364 | 0.294 | 0.323 | 0.515 | 0.260 | 0.491 | 1.222 |
| 7d | 10080 | 0.359 | 0.350 | 0.275 | 0.305 | 0.525 | 0.259 | 0.459 | 1.306 |
| 30d | 43200 | 0.359 | 0.355 | 0.280 | 0.310 | 0.513 | 0.251 | 0.466 | 1.304 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.416 / 0.569 / 0.950; 2: 0.411 / 0.621 / 0.983; 3: 0.388 / 0.500 / 1.000; 4: 0.373 / 0.517 / 1.000; 5: 0.387 / 0.569 / 1.000; 6: 0.389 / 0.586 / 1.000; 7: 0.379 / 0.552 / 1.000; 8: 0.373 / 0.534 / 1.000; 9: 0.368 / 0.483 / 1.000; 10: 0.381 / 0.534 / 1.000; 11: 0.340 / 0.534 / 1.000; 12: 0.381 / 0.500 / 1.000; 13: 0.364 / 0.569 / 1.000; 14: 0.370 / 0.569 / 1.000; 15: 0.358 / 0.534 / 1.000
- 6h: 1: 0.389 / 0.545 / 0.931; 2: 0.377 / 0.500 / 0.931; 3: 0.370 / 0.483 / 0.931; 4: 0.374 / 0.511 / 0.922; 5: 0.362 / 0.480 / 0.950; 6: 0.364 / 0.489 / 0.931; 7: 0.366 / 0.511 / 0.917; 8: 0.364 / 0.492 / 0.931; 9: 0.367 / 0.506 / 0.919; 10: 0.369 / 0.508 / 0.933; 11: 0.355 / 0.492 / 0.950; 12: 0.375 / 0.520 / 0.922; 13: 0.369 / 0.508 / 0.925; 14: 0.355 / 0.461 / 0.908; 15: 0.363 / 0.517 / 0.919
- 24h: 1: 0.376 / 0.515 / 0.906; 2: 0.367 / 0.506 / 0.910; 3: 0.365 / 0.486 / 0.906; 4: 0.369 / 0.525 / 0.908; 5: 0.364 / 0.487 / 0.906; 6: 0.360 / 0.486 / 0.903; 7: 0.362 / 0.497 / 0.899; 8: 0.362 / 0.498 / 0.896; 9: 0.365 / 0.531 / 0.894; 10: 0.360 / 0.481 / 0.895; 11: 0.357 / 0.485 / 0.901; 12: 0.361 / 0.491 / 0.896; 13: 0.362 / 0.488 / 0.897; 14: 0.355 / 0.484 / 0.898; 15: 0.358 / 0.492 / 0.899
- 7d: 1: 0.359 / 0.525 / 0.903; 2: 0.348 / 0.499 / 0.900; 3: 0.350 / 0.509 / 0.902; 4: 0.347 / 0.498 / 0.900; 5: 0.349 / 0.508 / 0.900; 6: 0.347 / 0.502 / 0.899; 7: 0.347 / 0.503 / 0.899; 8: 0.345 / 0.501 / 0.899; 9: 0.346 / 0.503 / 0.898; 10: 0.347 / 0.507 / 0.898; 11: 0.343 / 0.493 / 0.899; 12: 0.346 / 0.504 / 0.898; 13: 0.345 / 0.503 / 0.898; 14: 0.343 / 0.500 / 0.898; 15: 0.346 / 0.504 / 0.898
- 30d: 1: 0.359 / 0.513 / 0.900; 2: 0.352 / 0.498 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.351 / 0.500 / 0.900; 5: 0.351 / 0.504 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.350 / 0.505 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.502 / 0.899; 13: 0.348 / 0.502 / 0.899; 14: 0.346 / 0.498 / 0.899; 15: 0.346 / 0.497 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.188 (body 0.124, range 0.252); 'price stays where it was' would score 0.215; colour right 0.483; typical miss of the close 5.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.078, range 0.180); 'price stays where it was' would score 0.161; colour right 0.494; typical miss of the close 13.3 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.118 (body 0.075, range 0.161); 'price stays where it was' would score 0.129; colour right 0.484; typical miss of the close 11.4 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.120 (body 0.082, range 0.159); 'price stays where it was' would score 0.128; colour right 0.495; typical miss of the close 8.0 bp; chain ended on the right side 0.517 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.516 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.196 / 4.5; 3: 0.164 / 6.1; 4: 0.133 / 6.8; 5: 0.120 / 7.4; 6: 0.109 / 8.0; 7: 0.101 / 8.3; 8: 0.095 / 8.8; 9: 0.086 / 8.8; 10: 0.084 / 9.5; 11: 0.079 / 10.3; 12: 0.076 / 10.6; 13: 0.063 / 10.9; 14: 0.065 / 11.2; 15: 0.058 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 107635, probability skill vs chance 0.2224, widened contest next: True
  - now: threshold 0.8406, hit rate recent 0.9665 / long run 0.9377
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.262, naive rule 0.405, lift 3.82x
    - 24h: 56 calls (56 a day), hit rate 0.982, chance 0.273, naive rule 0.448, lift 3.60x
    - 7d: 396 calls (57 a day), hit rate 0.937, chance 0.294, naive rule 0.493, lift 3.19x
    - 30d: 1715 calls (57 a day), hit rate 0.938, chance 0.290, naive rule 0.481, lift 3.23x
  - next: threshold 0.5542, hit rate recent 0.5414 / long run 0.5726
    - 6h: 22 calls (89 a day), hit rate 0.500, chance 0.262, lift 1.91x
    - 24h: 133 calls (133 a day), hit rate 0.556, chance 0.273, lift 2.04x
    - 7d: 739 calls (106 a day), hit rate 0.579, chance 0.294, lift 1.97x
    - 30d: 2561 calls (85 a day), hit rate 0.579, chance 0.290, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.489; 0.35: 540, 0.512; 0.40: 484, 0.562; 0.45: 415, 0.631; 0.50: 362, 0.685; 0.55: 317, 0.727; 0.60: 270, 0.772; 0.65: 224, 0.800; 0.70: 179, 0.834; 0.75: 139, 0.871; 0.80: 95, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 498, 0.458; 0.40: 409, 0.488; 0.45: 314, 0.523; 0.50: 204, 0.558; 0.55: 92, 0.577; 0.60: 14, 0.596; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 107633, probability skill vs chance 0.2091, widened contest next: True
  - now: threshold 0.6961, hit rate recent 0.8431 / long run 0.8256
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.197, naive rule 0.389, lift 5.08x
    - 24h: 63 calls (63 a day), hit rate 0.873, chance 0.174, naive rule 0.367, lift 5.02x
    - 7d: 362 calls (52 a day), hit rate 0.823, chance 0.187, naive rule 0.406, lift 4.41x
    - 30d: 1597 calls (53 a day), hit rate 0.830, chance 0.187, naive rule 0.392, lift 4.44x
  - next: threshold 0.4257, hit rate recent 0.4065 / long run 0.4642
    - 6h: 24 calls (98 a day), hit rate 0.417, chance 0.197, lift 2.12x
    - 24h: 115 calls (116 a day), hit rate 0.400, chance 0.174, lift 2.30x
    - 7d: 639 calls (91 a day), hit rate 0.473, chance 0.187, lift 2.53x
    - 30d: 2263 calls (75 a day), hit rate 0.479, chance 0.187, lift 2.56x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.418; 0.35: 353, 0.482; 0.40: 284, 0.555; 0.45: 232, 0.610; 0.50: 182, 0.663; 0.55: 138, 0.707; 0.60: 108, 0.748; 0.65: 82, 0.792; 0.70: 60, 0.824; 0.75: 33, 0.866; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.388; 0.35: 251, 0.423; 0.40: 161, 0.451; 0.45: 78, 0.467; 0.50: 18, 0.503; 0.55: 2, 0.549
- **K=8**: model 1791936000, labels learned 107630, probability skill vs chance 0.1872, widened contest next: True
  - now: threshold 0.5821, hit rate recent 0.676 / long run 0.696
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.109, naive rule 0.244, lift 6.14x
    - 24h: 58 calls (58 a day), hit rate 0.655, chance 0.114, naive rule 0.289, lift 5.77x
    - 7d: 365 calls (52 a day), hit rate 0.685, chance 0.122, naive rule 0.338, lift 5.62x
    - 30d: 1577 calls (53 a day), hit rate 0.713, chance 0.122, naive rule 0.329, lift 5.84x
  - next: threshold 0.3408, hit rate recent 0.285 / long run 0.3774
    - 6h: 24 calls (99 a day), hit rate 0.208, chance 0.109, lift 1.92x
    - 24h: 122 calls (123 a day), hit rate 0.295, chance 0.114, lift 2.60x
    - 7d: 582 calls (83 a day), hit rate 0.381, chance 0.122, lift 3.13x
    - 30d: 2146 calls (72 a day), hit rate 0.402, chance 0.122, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.417; 0.35: 196, 0.491; 0.40: 150, 0.551; 0.45: 118, 0.594; 0.50: 90, 0.635; 0.55: 65, 0.684; 0.60: 44, 0.724; 0.65: 24, 0.779; 0.70: 9, 0.837; 0.75: 1, 0.783
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.353; 0.35: 107, 0.386; 0.40: 44, 0.416; 0.45: 9, 0.444; 0.50: 1, 0.382
- **K=13**: model 1792022400, labels learned 107625, probability skill vs chance 0.1699, widened contest next: True
  - now: threshold 0.427, hit rate recent 0.5404 / long run 0.5721
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.078, naive rule 0.216, lift 7.30x
    - 24h: 75 calls (76 a day), hit rate 0.507, chance 0.073, naive rule 0.236, lift 6.91x
    - 7d: 375 calls (54 a day), hit rate 0.555, chance 0.079, naive rule 0.283, lift 6.99x
    - 30d: 1512 calls (50 a day), hit rate 0.585, chance 0.078, naive rule 0.272, lift 7.51x
  - next: threshold 0.3008, hit rate recent 0.2747 / long run 0.3078
    - 6h: 14 calls (58 a day), hit rate 0.143, chance 0.078, lift 1.83x
    - 24h: 68 calls (69 a day), hit rate 0.294, chance 0.073, lift 4.01x
    - 7d: 449 calls (64 a day), hit rate 0.314, chance 0.079, lift 3.96x
    - 30d: 2039 calls (68 a day), hit rate 0.311, chance 0.078, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.452; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.618; 0.50: 25, 0.656; 0.55: 14, 0.706; 0.60: 4, 0.766; 0.65: 0, 0.938
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.321; 0.35: 13, 0.355; 0.40: 2, 0.385

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.246 | 5.82% | 0.950 | 0.533 | 0.252 | 0.448 | 0.605 |
| 6h | 21.309 | 5.97% | 0.908 | 0.497 | 0.251 | 0.494 | 0.619 |
| 24h | 16.871 | 4.55% | 0.896 | 0.497 | 0.251 | 0.483 | 0.623 |
| 7d | 14.776 | 4.16% | 0.900 | 0.499 | 0.251 | 0.490 | 0.672 |
| 30d | 14.093 | 3.96% | 0.900 | 0.500 | 0.251 | 0.496 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.879 | 10.301 | 10.324 | 10.305 | 10.527 | 10.256 | 10.144 | 10.135 | 10.207 | 10.246 |
| 6h | 22.660 | 21.751 | 21.311 | 21.418 | 21.807 | 21.272 | 21.360 | 21.374 | 21.297 | 21.309 |
| 24h | 17.675 | 17.091 | 16.922 | 16.884 | 17.176 | 16.960 | 16.851 | 16.872 | 16.837 | 16.871 |
| 7d | 15.417 | 14.941 | 14.859 | 14.790 | 15.038 | 14.968 | 14.782 | 14.753 | 14.747 | 14.776 |
| 30d | 14.674 | 14.219 | 14.176 | 14.119 | 14.350 | 14.277 | 14.092 | 14.066 | 14.067 | 14.093 |

## Next candle

- candle starting 2026-10-16 22:01 UTC, last close 2414.73
- P(up) 0.4871, return quantiles (bp): {'05': -6.852, '10': -5.386, '25': -2.719, '40': -0.946, '50': -0.118, '60': 0.817, '75': 2.748, '90': 5.358, '95': 7.107}
- changepoint probability 0.0588, regime age 52.5 min
- agent weights: empirical 0.003, ewma 0.037, garch 0.194, har 0.179, bocpd 0.022, hmm 0.136, online_qr 0.228, lgbm 0.200

## Learning log

- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- HMM volatility states (sd, bp per minute): [3.83, 6.59, 20.28], current probabilities: [0.753, 0.242, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-16 22:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.213, 'l_abs': 0.772, 'l_hi': 0.735, 'l_lo': 0.721, 'b05': 0.777, 'b25': 0.701, 'b75': 0.721, 'b95': 0.77}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.124, 1.464, 1.694, 1.975, 2.396, 2.699, 2.834, 3.198, 3.246, 3.086, 3.79, 4.033, 4.193, 4.263]}
- calibration offsets (in sigma): {'05': 0.09, '10': 0.03, '25': -0.01, '40': 0.0, '50': -0.02, '60': -0.02, '75': 0.02, '90': -0.03, '95': -0.04}
