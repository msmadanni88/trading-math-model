# ETH-USD 60s candle generator - report

- generated: 2026-10-16 06:18 UTC
- last closed candle: 2026-10-16 06:18 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.507 (671) [0.482, 0.535] | 0.514 (2875) [0.495, 0.533] | 0.509 (4218) [0.493, 0.524] | 0.503 (1246) [0.474, 0.534] | 0.480 (25) | 0.500 | flat +0.001 (noise 0.035) |
| colour_clear | 0.545 (791) | 0.540 (5524) [0.534, 0.546] | 0.516 (23376) [0.508, 0.525] | 0.510 (34272) [0.504, 0.516] | 0.543 (10034) [0.537, 0.549] | 0.542 (216) | 0.500 | flat -0.000 (noise 0.010) |
| colour_confident | 0.595 (84) | 0.599 (877) [0.574, 0.634] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.607 (28) | 0.500 | flat -0.009 (noise 0.030) |
| colour_next | 0.517 (1436) | 0.524 (9978) [0.519, 0.530] | 0.512 (42876) [0.507, 0.518] | 0.508 (62869) [0.504, 0.512] | 0.527 (18520) [0.522, 0.533] | 0.521 (376) | 0.500 | flat -0.003 (noise 0.007) |
| colour_path | 0.511 (20104) | 0.503 (139692) [0.501, 0.505] | 0.501 (600264) [0.500, 0.503] | 0.501 (880166) [0.500, 0.502] | 0.501 (259280) [0.498, 0.503] | 0.490 (5264) | 0.500 | flat +0.005 (noise 0.003) |
| colour_strong | 0.846 (13) | 0.681 (226) [0.638, 0.761] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.667 (6) | 0.500 | flat +0.047 (noise 0.051) |
| reversal_k13_next | 0.327 (52) | 0.317 (457) [0.291, 0.344] | 0.315 (2025) [0.300, 0.331] | 0.306 (3029) [0.293, 0.319] | 0.319 (924) [0.303, 0.334] | 0.455 (11) | 0.077 | flat +0.005 (noise 0.030) |
| reversal_k13_now | 0.490 (51) | 0.575 (348) [0.539, 0.611] | 0.588 (1478) [0.570, 0.609] | 0.581 (2159) [0.564, 0.598] | 0.581 (687) [0.552, 0.612] | 0.579 (19) | 0.077 | flat -0.016 (noise 0.036) |
| reversal_k3_next | 0.563 (87) | 0.578 (692) [0.558, 0.599] | 0.582 (2499) [0.567, 0.597] | 0.583 (3619) [0.572, 0.596] | 0.575 (1179) [0.557, 0.596] | 0.641 (39) | 0.293 | flat +0.006 (noise 0.028) |
| reversal_k3_now | 0.915 (47) | 0.930 (398) [0.915, 0.948] | 0.938 (1716) [0.930, 0.946] | 0.938 (2506) [0.931, 0.945] | 0.929 (743) [0.919, 0.940] | 0.955 (22) | 0.293 | flat +0.002 (noise 0.018) |
| reversal_k5_next | 0.434 (106) | 0.487 (599) [0.467, 0.509] | 0.484 (2200) [0.467, 0.501] | 0.484 (3111) [0.469, 0.499] | 0.466 (1121) [0.444, 0.490] | 0.429 (28) | 0.187 | flat +0.039 (noise 0.028) |
| reversal_k5_now | 0.755 (53) | 0.812 (345) [0.785, 0.839] | 0.828 (1579) [0.812, 0.844] | 0.831 (2294) [0.818, 0.844] | 0.817 (683) [0.794, 0.840] | 0.895 (19) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.383 (94) | 0.402 (545) [0.384, 0.420] | 0.407 (2132) [0.391, 0.424] | 0.395 (3191) [0.383, 0.409] | 0.394 (1085) [0.376, 0.412] | 0.333 (30) | 0.121 | flat +0.015 (noise 0.029) |
| reversal_k8_now | 0.651 (43) | 0.680 (353) [0.645, 0.714] | 0.714 (1569) [0.694, 0.736] | 0.708 (2300) [0.691, 0.725] | 0.696 (713) [0.666, 0.726] | 0.611 (18) | 0.122 | flat -0.035 (noise 0.033) |
| overall | 0.512 (22169) | 0.506 (154078) [0.504, 0.508] | 0.504 (661213) [0.503, 0.505] | 0.503 (969462) [0.502, 0.504] | 0.504 (286181) [0.502, 0.507] | 0.495 (5851) | - | flat +0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07466, 0.1159] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5247, 'levels': [{'threshold': 0.07466, 'calls_per_day': 143.7, 'win_rate': 0.5925}, {'threshold': 0.1159, 'calls_per_day': 35.8, 'win_rate': 0.6759}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 17759, 'rate': 0.5284}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15006 | 0.336 | 0.519 (14772) | 0.602 (1237) | 0.775 (2441) |
| volatility: normal | 15006 | 0.363 | 0.514 (14947) | 0.586 (333) | 0.776 (2119) |
| volatility: wild | 15006 | 0.375 | 0.502 (14966) | 0.647 (150) | 0.765 (2070) |
| session: Asia 00-08 | 15258 | 0.356 | 0.517 (15161) | 0.604 (626) | 0.769 (2230) |
| session: Europe 08-13 | 9300 | 0.351 | 0.510 (9221) | 0.589 (423) | 0.782 (1425) |
| session: US 13-21 | 14880 | 0.367 | 0.506 (14785) | 0.583 (424) | 0.777 (2154) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.660 (247) | 0.750 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.356 | 0.342 | 0.273 | 0.273 | 0.525 | 0.247 | 0.465 | 1.444 |
| 6h | 360 | 0.372 | 0.367 | 0.286 | 0.323 | 0.520 | 0.255 | 0.488 | 1.265 |
| 24h | 1440 | 0.375 | 0.367 | 0.287 | 0.324 | 0.519 | 0.266 | 0.483 | 1.143 |
| 7d | 10080 | 0.357 | 0.350 | 0.272 | 0.303 | 0.525 | 0.258 | 0.456 | 1.281 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.512 | 0.250 | 0.466 | 1.301 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.356 / 0.525 / 0.900; 2: 0.347 / 0.475 / 0.967; 3: 0.353 / 0.508 / 0.967; 4: 0.329 / 0.390 / 0.983; 5: 0.349 / 0.475 / 0.983; 6: 0.374 / 0.525 / 0.967; 7: 0.323 / 0.508 / 0.983; 8: 0.355 / 0.475 / 1.000; 9: 0.322 / 0.424 / 0.983; 10: 0.369 / 0.576 / 0.983; 11: 0.357 / 0.525 / 0.967; 12: 0.314 / 0.390 / 1.000; 13: 0.359 / 0.508 / 0.967; 14: 0.348 / 0.542 / 0.967; 15: 0.322 / 0.424 / 1.000
- 6h: 1: 0.372 / 0.520 / 0.897; 2: 0.356 / 0.494 / 0.914; 3: 0.363 / 0.503 / 0.897; 4: 0.358 / 0.503 / 0.922; 5: 0.360 / 0.508 / 0.914; 6: 0.350 / 0.464 / 0.919; 7: 0.353 / 0.478 / 0.908; 8: 0.355 / 0.508 / 0.906; 9: 0.360 / 0.528 / 0.906; 10: 0.357 / 0.480 / 0.903; 11: 0.355 / 0.494 / 0.908; 12: 0.351 / 0.480 / 0.894; 13: 0.355 / 0.494 / 0.894; 14: 0.344 / 0.489 / 0.897; 15: 0.337 / 0.436 / 0.897
- 24h: 1: 0.375 / 0.519 / 0.903; 2: 0.363 / 0.495 / 0.897; 3: 0.370 / 0.510 / 0.894; 4: 0.365 / 0.493 / 0.897; 5: 0.370 / 0.517 / 0.897; 6: 0.366 / 0.494 / 0.896; 7: 0.364 / 0.502 / 0.901; 8: 0.360 / 0.488 / 0.898; 9: 0.363 / 0.513 / 0.897; 10: 0.367 / 0.499 / 0.895; 11: 0.363 / 0.503 / 0.896; 12: 0.364 / 0.509 / 0.894; 13: 0.362 / 0.507 / 0.894; 14: 0.366 / 0.533 / 0.898; 15: 0.359 / 0.491 / 0.899
- 7d: 1: 0.357 / 0.525 / 0.903; 2: 0.346 / 0.499 / 0.900; 3: 0.349 / 0.511 / 0.901; 4: 0.345 / 0.496 / 0.902; 5: 0.348 / 0.508 / 0.901; 6: 0.346 / 0.502 / 0.902; 7: 0.345 / 0.501 / 0.902; 8: 0.344 / 0.500 / 0.902; 9: 0.344 / 0.497 / 0.902; 10: 0.346 / 0.507 / 0.901; 11: 0.343 / 0.497 / 0.902; 12: 0.344 / 0.503 / 0.902; 13: 0.343 / 0.502 / 0.901; 14: 0.342 / 0.504 / 0.901; 15: 0.345 / 0.503 / 0.900
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.899; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.094 (body 0.057, range 0.132); 'price stays where it was' would score 0.083; colour right 0.508; typical miss of the close 7.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.119 (body 0.079, range 0.159); 'price stays where it was' would score 0.119; colour right 0.483; typical miss of the close 10.1 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.128 (body 0.086, range 0.169); 'price stays where it was' would score 0.141; colour right 0.496; typical miss of the close 11.3 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.122 (body 0.084, range 0.161); 'price stays where it was' would score 0.128; colour right 0.496; typical miss of the close 7.6 bp; chain ended on the right side 0.508 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 8.0 bp; chain ended on the right side 0.514 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.197 / 4.5; 3: 0.164 / 6.1; 4: 0.134 / 6.8; 5: 0.121 / 7.4; 6: 0.109 / 8.0; 7: 0.102 / 8.3; 8: 0.096 / 8.8; 9: 0.087 / 8.7; 10: 0.084 / 9.5; 11: 0.078 / 10.3; 12: 0.075 / 10.6; 13: 0.063 / 10.9; 14: 0.065 / 11.2; 15: 0.058 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 106692, probability skill vs chance 0.2214, widened contest next: False
  - now: threshold 0.8409, hit rate recent 0.9427 / long run 0.9343
    - 6h: 20 calls (81 a day), hit rate 0.950, chance 0.285, naive rule 0.461, lift 3.33x
    - 24h: 56 calls (56 a day), hit rate 0.946, chance 0.279, naive rule 0.464, lift 3.39x
    - 7d: 407 calls (58 a day), hit rate 0.929, chance 0.298, naive rule 0.502, lift 3.12x
    - 30d: 1725 calls (58 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.24x
  - next: threshold 0.5195, hit rate recent 0.6112 / long run 0.5797
    - 6h: 37 calls (150 a day), hit rate 0.649, chance 0.285, lift 2.28x
    - 24h: 107 calls (107 a day), hit rate 0.607, chance 0.279, lift 2.18x
    - 7d: 711 calls (102 a day), hit rate 0.584, chance 0.298, lift 1.96x
    - 30d: 2527 calls (84 a day), hit rate 0.583, chance 0.290, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.489; 0.35: 540, 0.512; 0.40: 484, 0.561; 0.45: 415, 0.631; 0.50: 361, 0.685; 0.55: 317, 0.726; 0.60: 270, 0.771; 0.65: 224, 0.800; 0.70: 180, 0.833; 0.75: 139, 0.870; 0.80: 96, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 498, 0.458; 0.40: 409, 0.488; 0.45: 314, 0.523; 0.50: 204, 0.559; 0.55: 92, 0.580; 0.60: 14, 0.600; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 106690, probability skill vs chance 0.2092, widened contest next: False
  - now: threshold 0.6958, hit rate recent 0.8205 / long run 0.8236
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.175, naive rule 0.358, lift 5.04x
    - 24h: 60 calls (60 a day), hit rate 0.817, chance 0.181, naive rule 0.385, lift 4.51x
    - 7d: 355 calls (51 a day), hit rate 0.814, chance 0.190, naive rule 0.411, lift 4.29x
    - 30d: 1587 calls (53 a day), hit rate 0.827, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.4221, hit rate recent 0.4493 / long run 0.475
    - 6h: 28 calls (114 a day), hit rate 0.429, chance 0.175, lift 2.45x
    - 24h: 105 calls (105 a day), hit rate 0.448, chance 0.181, lift 2.47x
    - 7d: 609 calls (87 a day), hit rate 0.486, chance 0.190, lift 2.56x
    - 30d: 2218 calls (74 a day), hit rate 0.482, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 354, 0.482; 0.40: 284, 0.554; 0.45: 232, 0.611; 0.50: 182, 0.665; 0.55: 139, 0.709; 0.60: 109, 0.749; 0.65: 82, 0.790; 0.70: 60, 0.821; 0.75: 33, 0.863; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 251, 0.425; 0.40: 161, 0.455; 0.45: 78, 0.471; 0.50: 18, 0.499; 0.55: 2, 0.560
- **K=8**: model 1791936000, labels learned 106687, probability skill vs chance 0.1977, widened contest next: True
  - now: threshold 0.5777, hit rate recent 0.6518 / long run 0.696
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.132, naive rule 0.329, lift 4.72x
    - 24h: 50 calls (50 a day), hit rate 0.640, chance 0.119, naive rule 0.319, lift 5.39x
    - 7d: 364 calls (52 a day), hit rate 0.679, chance 0.124, naive rule 0.347, lift 5.48x
    - 30d: 1577 calls (53 a day), hit rate 0.712, chance 0.122, naive rule 0.331, lift 5.81x
  - next: threshold 0.341, hit rate recent 0.3635 / long run 0.3926
    - 6h: 29 calls (119 a day), hit rate 0.310, chance 0.132, lift 2.34x
    - 24h: 98 calls (99 a day), hit rate 0.367, chance 0.119, lift 3.09x
    - 7d: 556 calls (79 a day), hit rate 0.399, chance 0.124, lift 3.22x
    - 30d: 2137 calls (71 a day), hit rate 0.407, chance 0.122, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.418; 0.35: 196, 0.492; 0.40: 150, 0.552; 0.45: 119, 0.594; 0.50: 91, 0.635; 0.55: 66, 0.683; 0.60: 44, 0.725; 0.65: 24, 0.773; 0.70: 9, 0.829; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.353; 0.35: 107, 0.389; 0.40: 44, 0.421; 0.45: 9, 0.457; 0.50: 1, 0.364
- **K=13**: model 1792022400, labels learned 106682, probability skill vs chance 0.1772, widened contest next: True
  - now: threshold 0.4141, hit rate recent 0.53 / long run 0.5764
    - 6h: 17 calls (71 a day), hit rate 0.588, chance 0.087, naive rule 0.303, lift 6.78x
    - 24h: 57 calls (58 a day), hit rate 0.509, chance 0.081, naive rule 0.283, lift 6.28x
    - 7d: 358 calls (51 a day), hit rate 0.573, chance 0.080, naive rule 0.289, lift 7.19x
    - 30d: 1492 calls (50 a day), hit rate 0.586, chance 0.078, naive rule 0.274, lift 7.51x
  - next: threshold 0.3006, hit rate recent 0.3249 / long run 0.3123
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.087, lift 5.24x
    - 24h: 49 calls (49 a day), hit rate 0.347, chance 0.081, lift 4.28x
    - 7d: 450 calls (64 a day), hit rate 0.320, chance 0.080, lift 4.02x
    - 30d: 2026 calls (68 a day), hit rate 0.315, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.454; 0.35: 84, 0.514; 0.40: 60, 0.565; 0.45: 41, 0.617; 0.50: 25, 0.651; 0.55: 14, 0.702; 0.60: 4, 0.748; 0.65: 0, 0.929
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.327; 0.35: 13, 0.368; 0.40: 2, 0.413

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.336 | 4.81% | 0.883 | 0.533 | 0.251 | 0.492 | -0.000 |
| 6h | 14.350 | 3.35% | 0.886 | 0.489 | 0.250 | 0.514 | 0.447 |
| 24h | 18.610 | 4.33% | 0.906 | 0.497 | 0.251 | 0.503 | 0.656 |
| 7d | 14.236 | 4.17% | 0.901 | 0.501 | 0.251 | 0.493 | 0.668 |
| 30d | 14.149 | 4.00% | 0.900 | 0.500 | 0.251 | 0.496 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.959 | 12.427 | 12.532 | 12.265 | 12.680 | 12.462 | 12.160 | 12.265 | 12.266 | 12.336 |
| 6h | 14.848 | 14.508 | 14.454 | 14.322 | 14.612 | 14.485 | 14.294 | 14.314 | 14.311 | 14.350 |
| 24h | 19.452 | 18.735 | 18.714 | 18.622 | 18.823 | 18.871 | 18.603 | 18.618 | 18.590 | 18.610 |
| 7d | 14.855 | 14.391 | 14.326 | 14.252 | 14.498 | 14.443 | 14.242 | 14.205 | 14.208 | 14.236 |
| 30d | 14.740 | 14.276 | 14.234 | 14.173 | 14.408 | 14.342 | 14.148 | 14.121 | 14.122 | 14.149 |

## Next candle

- candle starting 2026-10-16 06:18 UTC, last close 2440.44
- P(up) 0.5119, return quantiles (bp): {'05': -8.163, '10': -6.51, '25': -3.273, '40': -1.165, '50': 0.154, '60': 1.366, '75': 3.166, '90': 6.729, '95': 8.512}
- changepoint probability 0.0392, regime age 176.6 min
- agent weights: empirical 0.004, ewma 0.074, garch 0.110, har 0.234, bocpd 0.043, hmm 0.059, online_qr 0.250, lgbm 0.225

## Learning log

- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.23, 6.04, 18.9], current probabilities: [0.165, 0.828, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-10-16 06:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.196, 'l_abs': 0.742, 'l_hi': 0.733, 'l_lo': 0.734, 'b05': 0.78, 'b25': 0.661, 'b75': 0.688, 'b95': 0.786}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.3, 1.661, 1.739, 2.11, 2.316, 2.557, 2.739, 3.03, 3.537, 3.717, 4.386, 4.667, 4.57, 4.646]}
- calibration offsets (in sigma): {'05': 0.0685, '10': 0.007, '25': 0.0025, '40': 0.008, '50': 0.025, '60': 0.022, '75': -0.0325, '90': 0.003, '95': -0.0785}
