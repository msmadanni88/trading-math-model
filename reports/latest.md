# ETH-USD 60s candle generator - report

- generated: 2026-10-16 01:28 UTC
- last closed candle: 2026-10-16 01:28 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.507 (671) [0.482, 0.535] | 0.514 (2875) [0.495, 0.533] | 0.509 (4218) [0.493, 0.524] | 0.503 (1246) [0.474, 0.534] | 0.800 (5) | 0.500 | flat +0.001 (noise 0.035) |
| colour_clear | 0.545 (791) | 0.540 (5524) [0.534, 0.546] | 0.516 (23376) [0.508, 0.525] | 0.510 (34272) [0.504, 0.516] | 0.543 (10034) [0.537, 0.549] | 0.566 (53) | 0.500 | flat -0.000 (noise 0.010) |
| colour_confident | 0.595 (84) | 0.599 (877) [0.574, 0.634] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.603 (1692) [0.579, 0.628] | 0.714 (7) | 0.500 | flat -0.009 (noise 0.030) |
| colour_next | 0.517 (1436) | 0.524 (9978) [0.519, 0.530] | 0.512 (42876) [0.507, 0.518] | 0.508 (62869) [0.504, 0.512] | 0.527 (18520) [0.522, 0.533] | 0.563 (87) | 0.500 | flat -0.003 (noise 0.007) |
| colour_path | 0.511 (20104) | 0.503 (139692) [0.501, 0.505] | 0.501 (600264) [0.500, 0.503] | 0.501 (880166) [0.500, 0.502] | 0.501 (259280) [0.498, 0.503] | 0.490 (1218) | 0.500 | flat +0.005 (noise 0.003) |
| colour_strong | 0.846 (13) | 0.681 (226) [0.638, 0.761] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 0.658 (445) [0.620, 0.702] | 1.000 (1) | 0.500 | flat +0.047 (noise 0.051) |
| reversal_k13_next | 0.327 (52) | 0.317 (457) [0.291, 0.344] | 0.315 (2025) [0.300, 0.331] | 0.306 (3029) [0.293, 0.319] | 0.319 (924) [0.303, 0.334] | 1.000 (1) | 0.077 | flat +0.005 (noise 0.030) |
| reversal_k13_now | 0.490 (51) | 0.575 (348) [0.539, 0.611] | 0.588 (1478) [0.570, 0.609] | 0.581 (2159) [0.564, 0.598] | 0.581 (687) [0.552, 0.612] | 0.600 (5) | 0.077 | flat -0.016 (noise 0.036) |
| reversal_k3_next | 0.563 (87) | 0.578 (692) [0.558, 0.599] | 0.582 (2499) [0.567, 0.597] | 0.583 (3619) [0.572, 0.596] | 0.575 (1179) [0.557, 0.596] | 0.700 (10) | 0.293 | flat +0.006 (noise 0.028) |
| reversal_k3_now | 0.915 (47) | 0.930 (398) [0.915, 0.948] | 0.938 (1716) [0.930, 0.946] | 0.938 (2506) [0.931, 0.945] | 0.929 (743) [0.919, 0.940] | 1.000 (8) | 0.293 | flat +0.002 (noise 0.018) |
| reversal_k5_next | 0.434 (106) | 0.487 (599) [0.467, 0.509] | 0.484 (2200) [0.467, 0.501] | 0.484 (3111) [0.469, 0.499] | 0.466 (1121) [0.444, 0.490] | 0.600 (5) | 0.187 | flat +0.039 (noise 0.028) |
| reversal_k5_now | 0.755 (53) | 0.812 (345) [0.785, 0.839] | 0.828 (1579) [0.812, 0.844] | 0.831 (2294) [0.818, 0.844] | 0.817 (683) [0.794, 0.840] | 1.000 (8) | 0.187 | flat -0.015 (noise 0.028) |
| reversal_k8_next | 0.383 (94) | 0.402 (545) [0.384, 0.420] | 0.407 (2132) [0.391, 0.424] | 0.395 (3191) [0.383, 0.409] | 0.394 (1085) [0.376, 0.412] | 0.667 (6) | 0.121 | flat +0.015 (noise 0.029) |
| reversal_k8_now | 0.651 (43) | 0.680 (353) [0.645, 0.714] | 0.714 (1569) [0.694, 0.736] | 0.708 (2300) [0.691, 0.725] | 0.696 (713) [0.666, 0.726] | 0.667 (6) | 0.122 | flat -0.035 (noise 0.033) |
| overall | 0.512 (22169) | 0.506 (154078) [0.504, 0.508] | 0.504 (661213) [0.503, 0.505] | 0.503 (969462) [0.502, 0.504] | 0.504 (286181) [0.502, 0.507] | 0.506 (1359) | - | flat +0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0747, 0.116] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5241, 'levels': [{'threshold': 0.0747, 'calls_per_day': 144.4, 'win_rate': 0.5945}, {'threshold': 0.116, 'calls_per_day': 35.9, 'win_rate': 0.685}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 17470, 'rate': 0.5287}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14910 | 0.336 | 0.519 (14676) | 0.602 (1236) | 0.776 (2430) |
| volatility: normal | 14909 | 0.363 | 0.514 (14850) | 0.585 (316) | 0.776 (2092) |
| volatility: wild | 14909 | 0.375 | 0.501 (14870) | 0.653 (147) | 0.765 (2057) |
| session: Asia 00-08 | 14968 | 0.356 | 0.518 (14872) | 0.605 (605) | 0.770 (2179) |
| session: Europe 08-13 | 9300 | 0.351 | 0.510 (9221) | 0.589 (423) | 0.782 (1425) |
| session: US 13-21 | 14880 | 0.367 | 0.506 (14785) | 0.583 (424) | 0.777 (2154) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.660 (247) | 0.750 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.388 | 0.390 | 0.309 | 0.309 | 0.542 | 0.271 | 0.506 | 1.224 |
| 6h | 360 | 0.364 | 0.365 | 0.280 | 0.308 | 0.526 | 0.256 | 0.473 | 1.366 |
| 24h | 1440 | 0.374 | 0.367 | 0.290 | 0.324 | 0.518 | 0.264 | 0.485 | 1.164 |
| 7d | 10080 | 0.357 | 0.349 | 0.272 | 0.303 | 0.524 | 0.258 | 0.455 | 1.268 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.512 | 0.250 | 0.466 | 1.299 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.388 / 0.542 / 0.883; 2: 0.347 / 0.458 / 0.867; 3: 0.360 / 0.525 / 0.850; 4: 0.378 / 0.593 / 0.867; 5: 0.337 / 0.441 / 0.917; 6: 0.332 / 0.441 / 0.933; 7: 0.337 / 0.458 / 0.933; 8: 0.349 / 0.542 / 0.917; 9: 0.331 / 0.458 / 0.917; 10: 0.347 / 0.508 / 0.950; 11: 0.331 / 0.441 / 0.950; 12: 0.321 / 0.424 / 0.983; 13: 0.340 / 0.458 / 0.967; 14: 0.343 / 0.475 / 0.983; 15: 0.326 / 0.441 / 0.983
- 6h: 1: 0.364 / 0.526 / 0.886; 2: 0.349 / 0.515 / 0.883; 3: 0.353 / 0.518 / 0.897; 4: 0.364 / 0.549 / 0.894; 5: 0.345 / 0.465 / 0.903; 6: 0.350 / 0.476 / 0.906; 7: 0.348 / 0.496 / 0.911; 8: 0.345 / 0.476 / 0.906; 9: 0.357 / 0.549 / 0.906; 10: 0.352 / 0.504 / 0.900; 11: 0.359 / 0.535 / 0.894; 12: 0.344 / 0.490 / 0.900; 13: 0.341 / 0.482 / 0.903; 14: 0.357 / 0.540 / 0.922; 15: 0.347 / 0.499 / 0.931
- 24h: 1: 0.374 / 0.518 / 0.908; 2: 0.363 / 0.500 / 0.902; 3: 0.369 / 0.516 / 0.902; 4: 0.366 / 0.507 / 0.899; 5: 0.366 / 0.516 / 0.899; 6: 0.365 / 0.503 / 0.899; 7: 0.361 / 0.502 / 0.899; 8: 0.356 / 0.495 / 0.901; 9: 0.360 / 0.507 / 0.896; 10: 0.366 / 0.523 / 0.898; 11: 0.360 / 0.511 / 0.895; 12: 0.361 / 0.520 / 0.893; 13: 0.357 / 0.504 / 0.890; 14: 0.362 / 0.532 / 0.894; 15: 0.357 / 0.509 / 0.895
- 7d: 1: 0.357 / 0.524 / 0.902; 2: 0.346 / 0.498 / 0.900; 3: 0.349 / 0.511 / 0.901; 4: 0.345 / 0.498 / 0.900; 5: 0.348 / 0.508 / 0.900; 6: 0.347 / 0.503 / 0.900; 7: 0.344 / 0.501 / 0.900; 8: 0.344 / 0.501 / 0.900; 9: 0.344 / 0.497 / 0.900; 10: 0.346 / 0.509 / 0.899; 11: 0.342 / 0.496 / 0.899; 12: 0.344 / 0.503 / 0.899; 13: 0.344 / 0.503 / 0.898; 14: 0.342 / 0.504 / 0.899; 15: 0.345 / 0.505 / 0.898
- 30d: 1: 0.358 / 0.512 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.078 (body 0.040, range 0.116); 'price stays where it was' would score 0.161; colour right 0.441; typical miss of the close 12.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.117 (body 0.075, range 0.159); 'price stays where it was' would score 0.144; colour right 0.471; typical miss of the close 9.3 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.131 (body 0.088, range 0.174); 'price stays where it was' would score 0.146; colour right 0.494; typical miss of the close 13.0 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.160); 'price stays where it was' would score 0.129; colour right 0.496; typical miss of the close 7.6 bp; chain ended on the right side 0.510 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.515 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.196 / 4.5; 3: 0.165 / 6.1; 4: 0.134 / 6.8; 5: 0.121 / 7.4; 6: 0.109 / 8.0; 7: 0.102 / 8.3; 8: 0.096 / 8.8; 9: 0.086 / 8.7; 10: 0.084 / 9.5; 11: 0.078 / 10.3; 12: 0.075 / 10.6; 13: 0.063 / 10.9; 14: 0.065 / 11.2; 15: 0.058 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 106402, probability skill vs chance 0.2228, widened contest next: False
  - now: threshold 0.8407, hit rate recent 0.9469 / long run 0.9344
    - 6h: 18 calls (73 a day), hit rate 1.000, chance 0.289, naive rule 0.463, lift 3.46x
    - 24h: 49 calls (49 a day), hit rate 0.939, chance 0.279, naive rule 0.458, lift 3.36x
    - 7d: 403 calls (58 a day), hit rate 0.931, chance 0.298, naive rule 0.501, lift 3.13x
    - 30d: 1718 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.24x
  - next: threshold 0.5198, hit rate recent 0.5959 / long run 0.5776
    - 6h: 28 calls (114 a day), hit rate 0.679, chance 0.289, lift 2.35x
    - 24h: 88 calls (88 a day), hit rate 0.580, chance 0.279, lift 2.08x
    - 7d: 698 calls (100 a day), hit rate 0.579, chance 0.298, lift 1.94x
    - 30d: 2508 calls (84 a day), hit rate 0.583, chance 0.290, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.489; 0.35: 540, 0.512; 0.40: 484, 0.561; 0.45: 414, 0.631; 0.50: 361, 0.685; 0.55: 317, 0.727; 0.60: 270, 0.771; 0.65: 224, 0.800; 0.70: 179, 0.834; 0.75: 138, 0.870; 0.80: 96, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 497, 0.459; 0.40: 410, 0.488; 0.45: 314, 0.523; 0.50: 204, 0.558; 0.55: 92, 0.581; 0.60: 14, 0.600; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 106400, probability skill vs chance 0.2114, widened contest next: False
  - now: threshold 0.6954, hit rate recent 0.8198 / long run 0.8237
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.201, naive rule 0.421, lift 4.70x
    - 24h: 56 calls (56 a day), hit rate 0.786, chance 0.179, naive rule 0.378, lift 4.39x
    - 7d: 350 calls (50 a day), hit rate 0.817, chance 0.190, naive rule 0.411, lift 4.31x
    - 30d: 1584 calls (53 a day), hit rate 0.828, chance 0.187, naive rule 0.393, lift 4.43x
  - next: threshold 0.4227, hit rate recent 0.4765 / long run 0.4783
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.201, lift 3.42x
    - 24h: 101 calls (101 a day), hit rate 0.436, chance 0.179, lift 2.43x
    - 7d: 600 calls (86 a day), hit rate 0.487, chance 0.190, lift 2.57x
    - 30d: 2204 calls (73 a day), hit rate 0.484, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.418; 0.35: 354, 0.482; 0.40: 284, 0.554; 0.45: 233, 0.611; 0.50: 182, 0.665; 0.55: 138, 0.709; 0.60: 109, 0.749; 0.65: 82, 0.790; 0.70: 60, 0.821; 0.75: 33, 0.865; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 251, 0.425; 0.40: 161, 0.454; 0.45: 78, 0.471; 0.50: 18, 0.504; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 106397, probability skill vs chance 0.1986, widened contest next: False
  - now: threshold 0.5731, hit rate recent 0.6685 / long run 0.6983
    - 6h: 16 calls (66 a day), hit rate 0.562, chance 0.129, naive rule 0.362, lift 4.38x
    - 24h: 45 calls (45 a day), hit rate 0.644, chance 0.115, naive rule 0.312, lift 5.62x
    - 7d: 356 calls (51 a day), hit rate 0.683, chance 0.123, naive rule 0.347, lift 5.53x
    - 30d: 1572 calls (52 a day), hit rate 0.714, chance 0.123, naive rule 0.331, lift 5.83x
  - next: threshold 0.3421, hit rate recent 0.4164 / long run 0.3984
    - 6h: 22 calls (91 a day), hit rate 0.545, chance 0.129, lift 4.24x
    - 24h: 91 calls (92 a day), hit rate 0.385, chance 0.115, lift 3.35x
    - 7d: 547 calls (78 a day), hit rate 0.404, chance 0.123, lift 3.27x
    - 30d: 2133 calls (71 a day), hit rate 0.408, chance 0.123, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.418; 0.35: 196, 0.492; 0.40: 150, 0.552; 0.45: 119, 0.595; 0.50: 91, 0.635; 0.55: 65, 0.685; 0.60: 44, 0.726; 0.65: 24, 0.774; 0.70: 9, 0.829; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.353; 0.35: 108, 0.389; 0.40: 44, 0.422; 0.45: 9, 0.461; 0.50: 1, 0.364
- **K=13**: model 1792022400, labels learned 106392, probability skill vs chance 0.1739, widened contest next: True
  - now: threshold 0.4181, hit rate recent 0.5216 / long run 0.5765
    - 6h: 15 calls (63 a day), hit rate 0.400, chance 0.070, naive rule 0.270, lift 5.75x
    - 24h: 53 calls (54 a day), hit rate 0.472, chance 0.077, naive rule 0.265, lift 6.14x
    - 7d: 350 calls (50 a day), hit rate 0.577, chance 0.079, naive rule 0.287, lift 7.30x
    - 30d: 1482 calls (49 a day), hit rate 0.588, chance 0.078, naive rule 0.273, lift 7.53x
  - next: threshold 0.3006, hit rate recent 0.3142 / long run 0.3108
    - 6h: 13 calls (54 a day), hit rate 0.462, chance 0.070, lift 6.63x
    - 24h: 46 calls (46 a day), hit rate 0.304, chance 0.077, lift 3.96x
    - 7d: 455 calls (65 a day), hit rate 0.319, chance 0.079, lift 4.03x
    - 30d: 2025 calls (68 a day), hit rate 0.315, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.455; 0.35: 84, 0.516; 0.40: 60, 0.565; 0.45: 41, 0.618; 0.50: 25, 0.652; 0.55: 14, 0.703; 0.60: 4, 0.746; 0.65: 0, 0.929
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.327; 0.35: 13, 0.368; 0.40: 2, 0.406

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.742 | 3.16% | 0.900 | 0.450 | 0.249 | 0.559 | 0.280 |
| 6h | 13.088 | 7.00% | 0.889 | 0.511 | 0.250 | 0.521 | 0.310 |
| 24h | 22.514 | 4.93% | 0.912 | 0.512 | 0.251 | 0.507 | 0.621 |
| 7d | 14.163 | 4.21% | 0.901 | 0.502 | 0.251 | 0.493 | 0.669 |
| 30d | 14.145 | 4.00% | 0.900 | 0.500 | 0.251 | 0.496 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.223 | 14.818 | 14.757 | 14.680 | 14.801 | 14.725 | 14.830 | 14.832 | 14.720 | 14.742 |
| 6h | 14.072 | 13.149 | 13.178 | 13.033 | 13.229 | 13.165 | 13.081 | 13.105 | 13.062 | 13.088 |
| 24h | 23.681 | 22.909 | 22.511 | 22.477 | 22.711 | 22.940 | 22.548 | 22.512 | 22.447 | 22.514 |
| 7d | 14.785 | 14.315 | 14.253 | 14.180 | 14.422 | 14.365 | 14.170 | 14.130 | 14.135 | 14.163 |
| 30d | 14.734 | 14.270 | 14.228 | 14.168 | 14.402 | 14.337 | 14.144 | 14.117 | 14.117 | 14.145 |

## Next candle

- candle starting 2026-10-16 01:28 UTC, last close 2430.65
- P(up) 0.4881, return quantiles (bp): {'05': -11.293, '10': -8.32, '25': -4.208, '40': -1.545, '50': -0.204, '60': 1.523, '75': 4.316, '90': 8.541, '95': 10.7}
- changepoint probability 0.0929, regime age 259.2 min
- agent weights: empirical 0.003, ewma 0.086, garch 0.143, har 0.246, bocpd 0.076, hmm 0.059, online_qr 0.200, lgbm 0.187

## Learning log

- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.23, 6.04, 18.9], current probabilities: [0.03, 0.952, 0.017]
- live generator: {'versions': 60, 'latest_effective': '2026-10-16 01:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.243, 'l_abs': 0.732, 'l_hi': 0.723, 'l_lo': 0.731, 'b05': 0.779, 'b25': 0.663, 'b75': 0.669, 'b95': 0.786}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.496, 1.764, 2.124, 2.286, 2.509, 2.557, 2.795, 3.091, 3.331, 3.644, 3.738, 4.057, 3.973, 4.039]}
- calibration offsets (in sigma): {'05': 0.0735, '10': 0.037, '25': 0.0075, '40': -0.022, '50': -0.065, '60': -0.048, '75': -0.0475, '90': -0.017, '95': -0.1035}
