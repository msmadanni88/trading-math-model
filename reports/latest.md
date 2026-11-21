# ETH-USD 60s candle generator - report

- generated: 2026-11-21 23:57 UTC
- last closed candle: 2026-11-21 23:57 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.539 (672) [0.506, 0.567] | 0.519 (2879) [0.502, 0.535] | 0.516 (7673) [0.505, 0.528] | 0.519 (4701) [0.505, 0.534] | 0.495 (95) | 0.500 | flat +0.010 (noise 0.027) |
| colour_clear | 0.577 (822) | 0.551 (5657) [0.538, 0.565] | 0.541 (23972) [0.535, 0.548] | 0.525 (63049) [0.520, 0.531] | 0.544 (38811) [0.539, 0.548] | 0.540 (705) | 0.500 | flat +0.010 (noise 0.010) |
| colour_confident | 0.562 (96) | 0.556 (1109) [0.533, 0.583] | 0.576 (4419) [0.564, 0.587] | 0.586 (7006) [0.576, 0.596] | 0.586 (7006) [0.576, 0.596] | 0.596 (223) | 0.500 | flat -0.003 (noise 0.022) |
| colour_next | 0.542 (1438) | 0.536 (10050) [0.529, 0.541] | 0.530 (42896) [0.526, 0.534] | 0.519 (114352) [0.515, 0.522] | 0.530 (70003) [0.527, 0.533] | 0.520 (1434) | 0.500 | flat +0.006 (noise 0.007) |
| colour_path | 0.509 (20132) | 0.503 (140700) [0.501, 0.506] | 0.502 (600544) [0.501, 0.503] | 0.501 (1600928) [0.500, 0.502] | 0.501 (980042) [0.500, 0.503] | 0.503 (20076) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.643 (14) | 0.611 (288) [0.576, 0.657] | 0.614 (1159) [0.598, 0.631] | 0.626 (1827) [0.610, 0.641] | 0.626 (1827) [0.610, 0.641] | 0.586 (70) | 0.500 | flat -0.012 (noise 0.043) |
| reversal_k13_next | 0.362 (58) | 0.310 (493) [0.278, 0.352] | 0.326 (1868) [0.310, 0.343] | 0.314 (5305) [0.305, 0.323] | 0.324 (3200) [0.313, 0.335] | 0.489 (47) | 0.077 | flat -0.016 (noise 0.030) |
| reversal_k13_now | 0.644 (45) | 0.577 (371) [0.526, 0.637] | 0.572 (1625) [0.552, 0.593] | 0.573 (4129) [0.561, 0.586] | 0.569 (2657) [0.553, 0.585] | 0.638 (47) | 0.077 | flat +0.016 (noise 0.038) |
| reversal_k3_next | 0.562 (160) | 0.578 (526) [0.560, 0.609] | 0.598 (2379) [0.587, 0.610] | 0.588 (6728) [0.580, 0.596] | 0.588 (4288) [0.579, 0.599] | 0.632 (163) | 0.293 | flat -0.039 (noise 0.034) |
| reversal_k3_now | 0.922 (64) | 0.937 (383) [0.920, 0.954] | 0.931 (1727) [0.922, 0.940] | 0.935 (4585) [0.930, 0.940] | 0.931 (2822) [0.924, 0.938] | 0.935 (46) | 0.293 | flat +0.017 (noise 0.018) |
| reversal_k5_next | 0.553 (47) | 0.476 (397) [0.423, 0.542] | 0.505 (2086) [0.490, 0.522] | 0.485 (6003) [0.474, 0.496] | 0.480 (4013) [0.466, 0.494] | 0.719 (32) | 0.187 | flat -0.024 (noise 0.041) |
| reversal_k5_now | 0.831 (65) | 0.794 (437) [0.770, 0.816] | 0.795 (1751) [0.779, 0.810] | 0.817 (4368) [0.806, 0.826] | 0.804 (2757) [0.792, 0.816] | 0.760 (50) | 0.187 | flat +0.056 (noise 0.029) |
| reversal_k8_next | 0.388 (85) | 0.397 (541) [0.369, 0.441] | 0.408 (2360) [0.394, 0.423] | 0.397 (6234) [0.387, 0.406] | 0.397 (4128) [0.385, 0.408] | 0.520 (75) | 0.121 | flat -0.013 (noise 0.031) |
| reversal_k8_now | 0.712 (59) | 0.675 (416) [0.636, 0.718] | 0.682 (1628) [0.662, 0.701] | 0.695 (4218) [0.683, 0.708] | 0.684 (2631) [0.669, 0.699] | 0.640 (50) | 0.122 | flat +0.012 (noise 0.034) |
| overall | 0.514 (22249) | 0.507 (154986) [0.505, 0.510] | 0.506 (661743) [0.505, 0.507] | 0.504 (1764523) [0.503, 0.505] | 0.505 (1081242) [0.504, 0.506] | 0.508 (22115) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07136, 0.1017] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5331, 'levels': [{'threshold': 0.07136, 'calls_per_day': 148.1, 'win_rate': 0.5567}, {'threshold': 0.1017, 'calls_per_day': 36.9, 'win_rate': 0.6293}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42898, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15359 | 0.349 | 0.532 (15141) | 0.567 (2263) | 0.756 (2559) |
| volatility: normal | 15359 | 0.378 | 0.528 (15303) | 0.591 (1448) | 0.740 (2415) |
| volatility: wild | 15359 | 0.390 | 0.530 (15320) | 0.585 (1107) | 0.754 (2163) |
| session: Asia 00-08 | 15360 | 0.370 | 0.530 (15247) | 0.570 (1665) | 0.748 (2300) |
| session: Europe 08-13 | 9600 | 0.366 | 0.531 (9525) | 0.584 (1192) | 0.756 (1540) |
| session: US 13-21 | 15360 | 0.380 | 0.534 (15270) | 0.603 (1346) | 0.747 (2443) |
| session: late 21-24 | 5757 | 0.366 | 0.517 (5722) | 0.533 (615) | 0.752 (854) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.373 | 0.359 | 0.277 | 0.277 | 0.533 | 0.240 | 0.506 | 1.393 |
| 6h | 360 | 0.381 | 0.375 | 0.281 | 0.299 | 0.522 | 0.253 | 0.508 | 1.232 |
| 24h | 1440 | 0.380 | 0.375 | 0.293 | 0.316 | 0.521 | 0.258 | 0.501 | 1.451 |
| 7d | 10080 | 0.386 | 0.377 | 0.304 | 0.339 | 0.532 | 0.269 | 0.504 | 1.198 |
| 30d | 43200 | 0.372 | 0.366 | 0.286 | 0.318 | 0.530 | 0.266 | 0.479 | 1.263 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.373 / 0.533 / 0.917; 2: 0.362 / 0.533 / 0.950; 3: 0.377 / 0.550 / 0.917; 4: 0.350 / 0.450 / 0.900; 5: 0.355 / 0.500 / 0.867; 6: 0.340 / 0.400 / 0.850; 7: 0.350 / 0.533 / 0.900; 8: 0.343 / 0.467 / 0.917; 9: 0.329 / 0.433 / 0.900; 10: 0.349 / 0.517 / 0.850; 11: 0.333 / 0.433 / 0.800; 12: 0.326 / 0.483 / 0.833; 13: 0.327 / 0.383 / 0.883; 14: 0.329 / 0.433 / 0.900; 15: 0.363 / 0.567 / 0.883
- 6h: 1: 0.381 / 0.522 / 0.917; 2: 0.370 / 0.478 / 0.881; 3: 0.363 / 0.489 / 0.900; 4: 0.376 / 0.528 / 0.886; 5: 0.367 / 0.489 / 0.875; 6: 0.375 / 0.508 / 0.858; 7: 0.365 / 0.503 / 0.878; 8: 0.372 / 0.514 / 0.903; 9: 0.356 / 0.464 / 0.894; 10: 0.368 / 0.544 / 0.889; 11: 0.364 / 0.506 / 0.869; 12: 0.356 / 0.472 / 0.864; 13: 0.374 / 0.550 / 0.892; 14: 0.359 / 0.481 / 0.917; 15: 0.371 / 0.542 / 0.914
- 24h: 1: 0.380 / 0.521 / 0.923; 2: 0.368 / 0.495 / 0.898; 3: 0.360 / 0.482 / 0.918; 4: 0.364 / 0.502 / 0.899; 5: 0.365 / 0.502 / 0.898; 6: 0.360 / 0.500 / 0.906; 7: 0.362 / 0.504 / 0.906; 8: 0.361 / 0.507 / 0.912; 9: 0.362 / 0.504 / 0.908; 10: 0.365 / 0.528 / 0.904; 11: 0.362 / 0.520 / 0.896; 12: 0.358 / 0.494 / 0.895; 13: 0.357 / 0.503 / 0.899; 14: 0.354 / 0.482 / 0.899; 15: 0.360 / 0.519 / 0.899
- 7d: 1: 0.386 / 0.532 / 0.902; 2: 0.375 / 0.498 / 0.900; 3: 0.375 / 0.507 / 0.900; 4: 0.373 / 0.498 / 0.901; 5: 0.375 / 0.508 / 0.901; 6: 0.374 / 0.507 / 0.901; 7: 0.373 / 0.504 / 0.901; 8: 0.374 / 0.511 / 0.902; 9: 0.369 / 0.497 / 0.902; 10: 0.373 / 0.512 / 0.902; 11: 0.371 / 0.504 / 0.901; 12: 0.372 / 0.505 / 0.901; 13: 0.370 / 0.503 / 0.902; 14: 0.370 / 0.500 / 0.903; 15: 0.369 / 0.502 / 0.903
- 30d: 1: 0.372 / 0.530 / 0.898; 2: 0.359 / 0.492 / 0.900; 3: 0.363 / 0.512 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.501 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.357 / 0.502 / 0.900; 10: 0.358 / 0.504 / 0.900; 11: 0.357 / 0.506 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.502 / 0.901; 14: 0.356 / 0.501 / 0.901; 15: 0.356 / 0.501 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.171 (body 0.099, range 0.242); 'price stays where it was' would score 0.217; colour right 0.500; typical miss of the close 6.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.170 (body 0.117, range 0.224); 'price stays where it was' would score 0.166; colour right 0.506; typical miss of the close 5.7 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.149 (body 0.101, range 0.198); 'price stays where it was' would score 0.153; colour right 0.520; typical miss of the close 13.4 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.132 (body 0.085, range 0.178); 'price stays where it was' would score 0.137; colour right 0.508; typical miss of the close 15.0 bp; chain ended on the right side 0.527 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.168); 'price stays where it was' would score 0.130; colour right 0.504; typical miss of the close 10.2 bp; chain ended on the right side 0.520 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.5; 2: 0.204 / 6.2; 3: 0.168 / 8.1; 4: 0.135 / 8.5; 5: 0.126 / 9.1; 6: 0.121 / 9.8; 7: 0.116 / 10.4; 8: 0.102 / 11.4; 9: 0.092 / 11.8; 10: 0.089 / 12.5; 11: 0.086 / 12.9; 12: 0.080 / 12.9; 13: 0.074 / 13.6; 14: 0.069 / 14.1; 15: 0.067 / 14.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 159591, probability skill vs chance 0.2339, widened contest next: False
  - now: threshold 0.8301, hit rate recent 0.9337 / long run 0.93
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.309, naive rule 0.519, lift 3.24x
    - 24h: 46 calls (46 a day), hit rate 0.935, chance 0.297, naive rule 0.532, lift 3.14x
    - 7d: 372 calls (53 a day), hit rate 0.935, chance 0.292, naive rule 0.504, lift 3.20x
    - 30d: 1720 calls (57 a day), hit rate 0.931, chance 0.293, naive rule 0.500, lift 3.18x
  - next: threshold 0.5084, hit rate recent 0.628 / long run 0.5993
    - 6h: 47 calls (190 a day), hit rate 0.617, chance 0.309, lift 2.00x
    - 24h: 163 calls (163 a day), hit rate 0.632, chance 0.297, lift 2.13x
    - 7d: 662 calls (95 a day), hit rate 0.583, chance 0.292, lift 1.99x
    - 30d: 2446 calls (82 a day), hit rate 0.600, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.502; 0.35: 529, 0.527; 0.40: 477, 0.575; 0.45: 412, 0.641; 0.50: 363, 0.685; 0.55: 315, 0.731; 0.60: 265, 0.778; 0.65: 223, 0.807; 0.70: 175, 0.838; 0.75: 141, 0.871; 0.80: 93, 0.903; 0.85: 44, 0.941; 0.90: 4, 0.965
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 490, 0.468; 0.40: 388, 0.508; 0.45: 293, 0.543; 0.50: 187, 0.575; 0.55: 80, 0.586; 0.60: 10, 0.633; 0.65: 0, 0.533
- **K=5**: model 1794528000, labels learned 159589, probability skill vs chance 0.2204, widened contest next: False
  - now: threshold 0.6998, hit rate recent 0.7857 / long run 0.7866
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.205, naive rule 0.426, lift 3.66x
    - 24h: 50 calls (50 a day), hit rate 0.760, chance 0.197, naive rule 0.463, lift 3.85x
    - 7d: 422 calls (60 a day), hit rate 0.794, chance 0.192, naive rule 0.421, lift 4.14x
    - 30d: 1760 calls (59 a day), hit rate 0.794, chance 0.187, naive rule 0.411, lift 4.25x
  - next: threshold 0.4616, hit rate recent 0.5875 / long run 0.5005
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.205, lift 3.76x
    - 24h: 32 calls (32 a day), hit rate 0.719, chance 0.197, lift 3.64x
    - 7d: 376 calls (54 a day), hit rate 0.468, chance 0.192, lift 2.44x
    - 30d: 1986 calls (66 a day), hit rate 0.510, chance 0.187, lift 2.73x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.421; 0.35: 362, 0.473; 0.40: 293, 0.541; 0.45: 237, 0.601; 0.50: 186, 0.653; 0.55: 149, 0.685; 0.60: 114, 0.731; 0.65: 81, 0.768; 0.70: 51, 0.804; 0.75: 27, 0.841; 0.80: 7, 0.856
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 336, 0.392; 0.35: 251, 0.431; 0.40: 160, 0.461; 0.45: 65, 0.504; 0.50: 8, 0.554; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 159586, probability skill vs chance 0.2213, widened contest next: False
  - now: threshold 0.5797, hit rate recent 0.665 / long run 0.6744
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.125, naive rule 0.351, lift 5.52x
    - 24h: 50 calls (50 a day), hit rate 0.640, chance 0.136, naive rule 0.433, lift 4.71x
    - 7d: 420 calls (60 a day), hit rate 0.655, chance 0.124, naive rule 0.353, lift 5.29x
    - 30d: 1640 calls (55 a day), hit rate 0.679, chance 0.123, naive rule 0.346, lift 5.54x
  - next: threshold 0.355, hit rate recent 0.4902 / long run 0.4175
    - 6h: 24 calls (98 a day), hit rate 0.583, chance 0.125, lift 4.65x
    - 24h: 75 calls (75 a day), hit rate 0.520, chance 0.136, lift 3.83x
    - 7d: 560 calls (80 a day), hit rate 0.396, chance 0.124, lift 3.21x
    - 30d: 2334 calls (78 a day), hit rate 0.415, chance 0.123, lift 3.38x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.427; 0.35: 199, 0.487; 0.40: 157, 0.537; 0.45: 120, 0.579; 0.50: 85, 0.636; 0.55: 62, 0.671; 0.60: 41, 0.714; 0.65: 24, 0.770; 0.70: 9, 0.812; 0.75: 2, 0.727
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 162, 0.376; 0.35: 84, 0.405; 0.40: 27, 0.440; 0.45: 6, 0.470; 0.50: 1, 0.704
- **K=13**: model 1795132800, labels learned 159581, probability skill vs chance 0.2041, widened contest next: False
  - now: threshold 0.4533, hit rate recent 0.6195 / long run 0.5748
    - 6h: 10 calls (42 a day), hit rate 0.800, chance 0.092, naive rule 0.327, lift 8.65x
    - 24h: 47 calls (47 a day), hit rate 0.638, chance 0.088, naive rule 0.382, lift 7.25x
    - 7d: 370 calls (53 a day), hit rate 0.562, chance 0.080, naive rule 0.296, lift 7.03x
    - 30d: 1634 calls (54 a day), hit rate 0.573, chance 0.079, naive rule 0.293, lift 7.25x
  - next: threshold 0.3073, hit rate recent 0.4299 / long run 0.3319
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.092, lift 6.31x
    - 24h: 47 calls (47 a day), hit rate 0.489, chance 0.088, lift 5.56x
    - 7d: 493 calls (71 a day), hit rate 0.312, chance 0.080, lift 3.91x
    - 30d: 1866 calls (62 a day), hit rate 0.332, chance 0.079, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 140, 0.424; 0.35: 102, 0.474; 0.40: 70, 0.534; 0.45: 49, 0.584; 0.50: 34, 0.624; 0.55: 21, 0.649; 0.60: 10, 0.682; 0.65: 2, 0.567; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.341; 0.35: 15, 0.373; 0.40: 2, 0.421; 0.45: 0, 0.600

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.076 | 11.98% | 0.917 | 0.500 | 0.249 | 0.517 | 0.471 |
| 6h | 12.292 | 18.11% | 0.922 | 0.492 | 0.250 | 0.506 | 0.221 |
| 24h | 28.677 | 7.42% | 0.919 | 0.502 | 0.250 | 0.500 | 0.664 |
| 7d | 25.287 | 4.16% | 0.901 | 0.500 | 0.250 | 0.498 | 0.669 |
| 30d | 18.800 | 4.84% | 0.900 | 0.500 | 0.250 | 0.504 | 0.719 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.992 | 14.470 | 14.510 | 14.113 | 15.387 | 14.854 | 14.110 | 13.997 | 14.086 | 14.076 |
| 6h | 15.011 | 12.404 | 12.546 | 12.350 | 12.843 | 12.809 | 12.303 | 12.260 | 12.306 | 12.292 |
| 24h | 30.976 | 29.375 | 29.172 | 28.717 | 29.776 | 29.240 | 28.783 | 28.636 | 28.681 | 28.677 |
| 7d | 26.386 | 25.506 | 25.441 | 25.295 | 25.786 | 25.572 | 25.283 | 25.234 | 25.247 | 25.287 |
| 30d | 19.757 | 18.981 | 18.935 | 18.856 | 19.183 | 19.111 | 18.785 | 18.759 | 18.768 | 18.800 |

## Next candle

- candle starting 2026-11-21 23:57 UTC, last close 1682.66
- P(up) 0.5011, return quantiles (bp): {'05': -6.349, '10': -4.675, '25': -2.385, '40': -0.893, '50': 0.011, '60': 0.884, '75': 2.446, '90': 4.557, '95': 6.056}
- changepoint probability 0.0143, regime age 65.3 min
- agent weights: empirical 0.003, ewma 0.063, garch 0.064, har 0.248, bocpd 0.013, hmm 0.045, online_qr 0.227, lgbm 0.338

## Learning log

- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- HMM volatility states (sd, bp per minute): [5.86, 10.53, 26.19], current probabilities: [0.976, 0.023, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-22 00:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.211, 'l_abs': 0.661, 'l_hi': 0.791, 'l_lo': 0.728, 'b05': 0.752, 'b25': 0.702, 'b75': 0.695, 'b95': 0.738}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.5], [1.2, 1.5]], 'cone_width': [1.623, 1.767, 1.964, 2.114, 2.368, 2.319, 2.339, 2.341, 2.626, 3.111, 3.322, 3.012, 2.777, 2.881]}
- calibration offsets (in sigma): {'05': 0.128, '10': 0.116, '25': 0.07, '40': 0.024, '50': 0.02, '60': 0.006, '75': -0.01, '90': -0.076, '95': -0.128}
