# ETH-USD 60s candle generator - report

- generated: 2026-10-16 15:33 UTC
- last closed candle: 2026-10-16 15:33 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.507 (671) [0.482, 0.535] | 0.514 (2875) [0.495, 0.533] | 0.509 (4218) [0.493, 0.524] | 0.503 (1246) [0.474, 0.534] | 0.532 (62) | 0.500 | flat +0.001 (noise 0.035) |
| colour_clear | 0.545 (791) | 0.540 (5524) [0.534, 0.546] | 0.516 (23376) [0.508, 0.525] | 0.510 (34272) [0.504, 0.516] | 0.543 (10034) [0.537, 0.549] | 0.520 (536) | 0.500 | flat -0.000 (noise 0.010) |
| colour_confident | 0.595 (84) | 0.599 (877) [0.574, 0.634] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.612 (67) | 0.500 | flat -0.009 (noise 0.030) |
| colour_next | 0.517 (1436) | 0.524 (9978) [0.519, 0.530] | 0.512 (42876) [0.507, 0.518] | 0.508 (62869) [0.504, 0.512] | 0.527 (18520) [0.522, 0.533] | 0.516 (931) | 0.500 | flat -0.003 (noise 0.007) |
| colour_path | 0.511 (20104) | 0.503 (139692) [0.501, 0.505] | 0.501 (600264) [0.500, 0.503] | 0.501 (880166) [0.500, 0.502] | 0.501 (259280) [0.498, 0.503] | 0.494 (13034) | 0.500 | flat +0.005 (noise 0.003) |
| colour_strong | 0.846 (13) | 0.681 (226) [0.638, 0.761] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.588 (17) | 0.500 | flat +0.047 (noise 0.051) |
| reversal_k13_next | 0.327 (52) | 0.317 (457) [0.291, 0.344] | 0.315 (2025) [0.300, 0.331] | 0.306 (3029) [0.293, 0.319] | 0.319 (924) [0.303, 0.334] | 0.349 (43) | 0.077 | flat +0.005 (noise 0.030) |
| reversal_k13_now | 0.490 (51) | 0.575 (348) [0.539, 0.611] | 0.588 (1478) [0.570, 0.609] | 0.581 (2159) [0.564, 0.598] | 0.581 (687) [0.552, 0.612] | 0.528 (53) | 0.077 | flat -0.016 (noise 0.036) |
| reversal_k3_next | 0.563 (87) | 0.578 (692) [0.558, 0.599] | 0.582 (2499) [0.567, 0.597] | 0.583 (3619) [0.572, 0.596] | 0.575 (1179) [0.557, 0.596] | 0.574 (101) | 0.293 | flat +0.006 (noise 0.028) |
| reversal_k3_now | 0.915 (47) | 0.930 (398) [0.915, 0.948] | 0.938 (1716) [0.930, 0.946] | 0.938 (2506) [0.931, 0.945] | 0.929 (743) [0.919, 0.940] | 0.978 (45) | 0.293 | flat +0.002 (noise 0.018) |
| reversal_k5_next | 0.434 (106) | 0.487 (599) [0.467, 0.509] | 0.484 (2200) [0.467, 0.501] | 0.484 (3111) [0.469, 0.499] | 0.466 (1121) [0.444, 0.490] | 0.398 (83) | 0.187 | flat +0.039 (noise 0.028) |
| reversal_k5_now | 0.755 (53) | 0.812 (345) [0.785, 0.839] | 0.828 (1579) [0.812, 0.844] | 0.831 (2294) [0.818, 0.844] | 0.817 (683) [0.794, 0.840] | 0.843 (51) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.383 (94) | 0.402 (545) [0.384, 0.420] | 0.407 (2132) [0.391, 0.424] | 0.395 (3191) [0.383, 0.409] | 0.394 (1085) [0.376, 0.412] | 0.321 (84) | 0.121 | flat +0.015 (noise 0.029) |
| reversal_k8_now | 0.651 (43) | 0.680 (353) [0.645, 0.714] | 0.714 (1569) [0.694, 0.736] | 0.708 (2300) [0.691, 0.725] | 0.696 (713) [0.666, 0.726] | 0.667 (45) | 0.122 | flat -0.035 (noise 0.033) |
| overall | 0.512 (22169) | 0.506 (154078) [0.504, 0.508] | 0.504 (661213) [0.503, 0.505] | 0.503 (969462) [0.502, 0.504] | 0.504 (286181) [0.502, 0.507] | 0.498 (14532) | - | flat +0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07437, 0.1158] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5239, 'levels': [{'threshold': 0.07437, 'calls_per_day': 142.7, 'win_rate': 0.5927}, {'threshold': 0.1158, 'calls_per_day': 35.9, 'win_rate': 0.6654}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 18314, 'rate': 0.5279}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15192 | 0.336 | 0.518 (14958) | 0.602 (1244) | 0.775 (2474) |
| volatility: normal | 15191 | 0.363 | 0.514 (15131) | 0.589 (360) | 0.772 (2175) |
| volatility: wild | 15190 | 0.376 | 0.502 (15151) | 0.645 (155) | 0.766 (2097) |
| session: Asia 00-08 | 15360 | 0.356 | 0.518 (15263) | 0.604 (637) | 0.768 (2249) |
| session: Europe 08-13 | 9600 | 0.352 | 0.510 (9521) | 0.589 (450) | 0.778 (1490) |
| session: US 13-21 | 15033 | 0.367 | 0.506 (14938) | 0.584 (425) | 0.779 (2186) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.660 (247) | 0.750 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.387 | 0.359 | 0.307 | 0.307 | 0.517 | 0.270 | 0.504 | 1.323 |
| 6h | 360 | 0.382 | 0.354 | 0.307 | 0.315 | 0.514 | 0.266 | 0.498 | 1.120 |
| 24h | 1440 | 0.374 | 0.365 | 0.290 | 0.318 | 0.516 | 0.262 | 0.486 | 1.214 |
| 7d | 10080 | 0.358 | 0.349 | 0.274 | 0.303 | 0.524 | 0.258 | 0.458 | 1.301 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.310 | 0.512 | 0.250 | 0.466 | 1.304 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.387 / 0.517 / 0.933; 2: 0.351 / 0.417 / 0.933; 3: 0.373 / 0.483 / 0.883; 4: 0.402 / 0.600 / 0.883; 5: 0.359 / 0.467 / 0.783; 6: 0.360 / 0.433 / 0.833; 7: 0.379 / 0.467 / 0.833; 8: 0.401 / 0.583 / 0.817; 9: 0.381 / 0.517 / 0.783; 10: 0.344 / 0.417 / 0.750; 11: 0.354 / 0.467 / 0.767; 12: 0.343 / 0.417 / 0.750; 13: 0.374 / 0.483 / 0.733; 14: 0.394 / 0.567 / 0.783; 15: 0.384 / 0.567 / 0.767
- 6h: 1: 0.382 / 0.514 / 0.881; 2: 0.376 / 0.522 / 0.908; 3: 0.369 / 0.475 / 0.883; 4: 0.380 / 0.553 / 0.883; 5: 0.367 / 0.469 / 0.847; 6: 0.366 / 0.500 / 0.853; 7: 0.368 / 0.503 / 0.872; 8: 0.376 / 0.531 / 0.847; 9: 0.373 / 0.539 / 0.836; 10: 0.357 / 0.456 / 0.833; 11: 0.357 / 0.456 / 0.833; 12: 0.365 / 0.508 / 0.853; 13: 0.375 / 0.486 / 0.842; 14: 0.363 / 0.489 / 0.850; 15: 0.365 / 0.497 / 0.833
- 24h: 1: 0.374 / 0.516 / 0.902; 2: 0.360 / 0.491 / 0.907; 3: 0.367 / 0.501 / 0.903; 4: 0.365 / 0.511 / 0.905; 5: 0.364 / 0.490 / 0.897; 6: 0.363 / 0.492 / 0.897; 7: 0.360 / 0.497 / 0.899; 8: 0.363 / 0.503 / 0.899; 9: 0.364 / 0.527 / 0.899; 10: 0.360 / 0.485 / 0.896; 11: 0.359 / 0.490 / 0.895; 12: 0.359 / 0.492 / 0.898; 13: 0.357 / 0.485 / 0.899; 14: 0.358 / 0.503 / 0.903; 15: 0.356 / 0.485 / 0.899
- 7d: 1: 0.358 / 0.524 / 0.902; 2: 0.347 / 0.500 / 0.900; 3: 0.350 / 0.511 / 0.900; 4: 0.346 / 0.497 / 0.899; 5: 0.349 / 0.506 / 0.898; 6: 0.347 / 0.501 / 0.898; 7: 0.346 / 0.502 / 0.898; 8: 0.346 / 0.503 / 0.898; 9: 0.345 / 0.502 / 0.898; 10: 0.347 / 0.507 / 0.898; 11: 0.343 / 0.495 / 0.898; 12: 0.345 / 0.504 / 0.898; 13: 0.345 / 0.502 / 0.898; 14: 0.343 / 0.502 / 0.898; 15: 0.345 / 0.503 / 0.898
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.350 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.347 / 0.502 / 0.899; 14: 0.346 / 0.498 / 0.899; 15: 0.346 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.084 (body 0.043, range 0.125); 'price stays where it was' would score 0.124; colour right 0.533; typical miss of the close 21.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.093 (body 0.063, range 0.124); 'price stays where it was' would score 0.116; colour right 0.486; typical miss of the close 16.1 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.127; colour right 0.488; typical miss of the close 10.9 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.121 (body 0.082, range 0.160); 'price stays where it was' would score 0.127; colour right 0.495; typical miss of the close 7.8 bp; chain ended on the right side 0.507 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 8.0 bp; chain ended on the right side 0.515 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.1; 2: 0.197 / 4.6; 3: 0.164 / 6.1; 4: 0.134 / 6.8; 5: 0.120 / 7.5; 6: 0.109 / 8.0; 7: 0.101 / 8.3; 8: 0.096 / 8.8; 9: 0.087 / 8.8; 10: 0.084 / 9.5; 11: 0.078 / 10.3; 12: 0.076 / 10.6; 13: 0.063 / 10.9; 14: 0.066 / 11.2; 15: 0.058 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 107247, probability skill vs chance 0.2248, widened contest next: False
  - now: threshold 0.8408, hit rate recent 0.9611 / long run 0.9367
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.261, naive rule 0.451, lift 3.84x
    - 24h: 61 calls (61 a day), hit rate 0.967, chance 0.282, naive rule 0.468, lift 3.44x
    - 7d: 405 calls (58 a day), hit rate 0.931, chance 0.297, naive rule 0.499, lift 3.14x
    - 30d: 1723 calls (57 a day), hit rate 0.938, chance 0.290, naive rule 0.482, lift 3.23x
  - next: threshold 0.5425, hit rate recent 0.5498 / long run 0.5749
    - 6h: 41 calls (166 a day), hit rate 0.463, chance 0.261, lift 1.78x
    - 24h: 133 calls (133 a day), hit rate 0.579, chance 0.282, lift 2.06x
    - 7d: 739 calls (106 a day), hit rate 0.581, chance 0.297, lift 1.96x
    - 30d: 2554 calls (85 a day), hit rate 0.580, chance 0.290, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.562; 0.45: 415, 0.632; 0.50: 362, 0.685; 0.55: 317, 0.727; 0.60: 270, 0.771; 0.65: 224, 0.800; 0.70: 180, 0.833; 0.75: 139, 0.870; 0.80: 96, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 497, 0.459; 0.40: 409, 0.489; 0.45: 314, 0.524; 0.50: 204, 0.559; 0.55: 92, 0.578; 0.60: 14, 0.594; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 107245, probability skill vs chance 0.2074, widened contest next: True
  - now: threshold 0.696, hit rate recent 0.8174 / long run 0.823
    - 6h: 18 calls (73 a day), hit rate 0.778, chance 0.164, naive rule 0.370, lift 4.73x
    - 24h: 67 calls (67 a day), hit rate 0.851, chance 0.174, naive rule 0.373, lift 4.89x
    - 7d: 365 calls (52 a day), hit rate 0.816, chance 0.187, naive rule 0.407, lift 4.36x
    - 30d: 1598 calls (53 a day), hit rate 0.829, chance 0.187, naive rule 0.393, lift 4.44x
  - next: threshold 0.429, hit rate recent 0.4025 / long run 0.4668
    - 6h: 39 calls (159 a day), hit rate 0.385, chance 0.164, lift 2.34x
    - 24h: 114 calls (115 a day), hit rate 0.412, chance 0.174, lift 2.37x
    - 7d: 632 calls (90 a day), hit rate 0.476, chance 0.187, lift 2.55x
    - 30d: 2250 calls (75 a day), hit rate 0.480, chance 0.187, lift 2.57x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.418; 0.35: 354, 0.482; 0.40: 284, 0.554; 0.45: 232, 0.610; 0.50: 182, 0.663; 0.55: 139, 0.707; 0.60: 109, 0.747; 0.65: 82, 0.791; 0.70: 60, 0.822; 0.75: 33, 0.865; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.389; 0.35: 251, 0.424; 0.40: 162, 0.453; 0.45: 78, 0.468; 0.50: 18, 0.500; 0.55: 2, 0.547
- **K=8**: model 1791936000, labels learned 107242, probability skill vs chance 0.1954, widened contest next: True
  - now: threshold 0.5801, hit rate recent 0.6775 / long run 0.6964
    - 6h: 18 calls (74 a day), hit rate 0.778, chance 0.103, naive rule 0.270, lift 7.56x
    - 24h: 60 calls (60 a day), hit rate 0.650, chance 0.117, naive rule 0.305, lift 5.57x
    - 7d: 372 calls (53 a day), hit rate 0.685, chance 0.123, naive rule 0.342, lift 5.58x
    - 30d: 1582 calls (53 a day), hit rate 0.713, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.3402, hit rate recent 0.334 / long run 0.3859
    - 6h: 38 calls (156 a day), hit rate 0.316, chance 0.103, lift 3.07x
    - 24h: 117 calls (118 a day), hit rate 0.333, chance 0.117, lift 2.85x
    - 7d: 572 calls (82 a day), hit rate 0.390, chance 0.123, lift 3.18x
    - 30d: 2150 calls (72 a day), hit rate 0.405, chance 0.122, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.418; 0.35: 196, 0.491; 0.40: 150, 0.551; 0.45: 119, 0.594; 0.50: 91, 0.635; 0.55: 66, 0.684; 0.60: 44, 0.725; 0.65: 24, 0.777; 0.70: 9, 0.835; 0.75: 1, 0.783
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.354; 0.35: 107, 0.388; 0.40: 44, 0.420; 0.45: 9, 0.448; 0.50: 1, 0.382
- **K=13**: model 1792022400, labels learned 107237, probability skill vs chance 0.1739, widened contest next: True
  - now: threshold 0.4125, hit rate recent 0.5284 / long run 0.5723
    - 6h: 23 calls (96 a day), hit rate 0.565, chance 0.070, naive rule 0.211, lift 8.12x
    - 24h: 69 calls (70 a day), hit rate 0.493, chance 0.072, naive rule 0.237, lift 6.88x
    - 7d: 370 calls (53 a day), hit rate 0.562, chance 0.079, naive rule 0.285, lift 7.09x
    - 30d: 1508 calls (50 a day), hit rate 0.585, chance 0.078, naive rule 0.273, lift 7.50x
  - next: threshold 0.3, hit rate recent 0.3148 / long run 0.3122
    - 6h: 26 calls (109 a day), hit rate 0.308, chance 0.070, lift 4.42x
    - 24h: 63 calls (64 a day), hit rate 0.365, chance 0.072, lift 5.10x
    - 7d: 451 calls (65 a day), hit rate 0.322, chance 0.079, lift 4.06x
    - 30d: 2043 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.452; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.617; 0.50: 25, 0.654; 0.55: 14, 0.705; 0.60: 4, 0.760; 0.65: 0, 0.938
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.325; 0.35: 13, 0.361; 0.40: 2, 0.397

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 24.735 | 3.36% | 0.933 | 0.500 | 0.251 | 0.450 | 0.385 |
| 6h | 19.505 | 2.92% | 0.881 | 0.467 | 0.251 | 0.442 | 0.556 |
| 24h | 15.574 | 4.04% | 0.898 | 0.500 | 0.250 | 0.498 | 0.578 |
| 7d | 14.347 | 4.07% | 0.900 | 0.500 | 0.251 | 0.490 | 0.670 |
| 30d | 14.159 | 4.01% | 0.900 | 0.500 | 0.251 | 0.495 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 25.595 | 24.700 | 24.830 | 24.659 | 25.283 | 25.322 | 24.760 | 24.710 | 24.660 | 24.735 |
| 6h | 20.092 | 19.742 | 19.505 | 19.499 | 19.795 | 19.679 | 19.481 | 19.507 | 19.453 | 19.505 |
| 24h | 16.231 | 15.728 | 15.661 | 15.591 | 15.808 | 15.722 | 15.552 | 15.575 | 15.554 | 15.574 |
| 7d | 14.956 | 14.498 | 14.432 | 14.359 | 14.601 | 14.545 | 14.351 | 14.319 | 14.318 | 14.347 |
| 30d | 14.750 | 14.286 | 14.243 | 14.183 | 14.416 | 14.350 | 14.158 | 14.131 | 14.132 | 14.159 |

## Next candle

- candle starting 2026-10-16 15:33 UTC, last close 2440.58
- P(up) 0.4904, return quantiles (bp): {'05': -13.033, '10': -10.588, '25': -5.569, '40': -2.28, '50': -0.193, '60': 1.852, '75': 5.549, '90': 10.662, '95': 13.678}
- changepoint probability 0.0376, regime age 82.1 min
- agent weights: empirical 0.005, ewma 0.065, garch 0.136, har 0.226, bocpd 0.036, hmm 0.052, online_qr 0.251, lgbm 0.229

## Learning log

- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- HMM volatility states (sd, bp per minute): [3.83, 6.59, 20.28], current probabilities: [0.017, 0.927, 0.056]
- live generator: {'versions': 60, 'latest_effective': '2026-10-16 15:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.213, 'l_abs': 0.787, 'l_hi': 0.735, 'l_lo': 0.735, 'b05': 0.778, 'b25': 0.686, 'b75': 0.722, 'b95': 0.777}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.395, 1.817, 1.98, 2.764, 2.974, 3.031, 3.517, 3.664, 4.192, 4.495, 4.43, 4.809, 4.525, 5.084]}
- calibration offsets (in sigma): {'05': 0.066, '10': -0.008, '25': -0.04, '40': -0.042, '50': -0.03, '60': -0.018, '75': 0.02, '90': 0.018, '95': -0.026}
