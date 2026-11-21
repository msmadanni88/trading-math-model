# ETH-USD 60s candle generator - report

- generated: 2026-11-21 03:59 UTC
- last closed candle: 2026-11-21 03:59 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.539 (672) [0.506, 0.567] | 0.519 (2879) [0.502, 0.535] | 0.516 (7673) [0.505, 0.528] | 0.519 (4701) [0.505, 0.534] | 0.333 (15) | 0.500 | flat +0.010 (noise 0.027) |
| colour_clear | 0.577 (822) | 0.551 (5657) [0.538, 0.565] | 0.541 (23972) [0.535, 0.548] | 0.525 (63049) [0.520, 0.531] | 0.544 (38811) [0.539, 0.548] | 0.526 (135) | 0.500 | flat +0.010 (noise 0.010) |
| colour_confident | 0.562 (96) | 0.556 (1109) [0.533, 0.583] | 0.576 (4419) [0.564, 0.587] | 0.586 (7006) [0.576, 0.596] | 0.586 (7006) [0.576, 0.596] | 0.625 (48) | 0.500 | flat -0.003 (noise 0.022) |
| colour_next | 0.542 (1438) | 0.536 (10050) [0.529, 0.541] | 0.530 (42896) [0.526, 0.534] | 0.519 (114352) [0.515, 0.522] | 0.530 (70003) [0.527, 0.533] | 0.532 (237) | 0.500 | flat +0.006 (noise 0.007) |
| colour_path | 0.509 (20132) | 0.503 (140700) [0.501, 0.506] | 0.502 (600544) [0.501, 0.503] | 0.501 (1600928) [0.500, 0.502] | 0.501 (980042) [0.500, 0.503] | 0.495 (3318) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.643 (14) | 0.611 (288) [0.576, 0.657] | 0.614 (1159) [0.598, 0.631] | 0.626 (1827) [0.610, 0.641] | 0.626 (1827) [0.610, 0.641] | 0.615 (13) | 0.500 | flat -0.012 (noise 0.043) |
| reversal_k13_next | 0.362 (58) | 0.310 (493) [0.278, 0.352] | 0.326 (1868) [0.310, 0.343] | 0.314 (5305) [0.305, 0.323] | 0.324 (3200) [0.313, 0.335] | 0.571 (7) | 0.077 | flat -0.016 (noise 0.030) |
| reversal_k13_now | 0.644 (45) | 0.577 (371) [0.526, 0.637] | 0.572 (1625) [0.552, 0.593] | 0.573 (4129) [0.561, 0.586] | 0.569 (2657) [0.553, 0.585] | 0.667 (9) | 0.077 | flat +0.016 (noise 0.038) |
| reversal_k3_next | 0.562 (160) | 0.578 (526) [0.560, 0.609] | 0.598 (2379) [0.587, 0.610] | 0.588 (6728) [0.580, 0.596] | 0.588 (4288) [0.579, 0.599] | 0.636 (22) | 0.293 | flat -0.039 (noise 0.034) |
| reversal_k3_now | 0.922 (64) | 0.937 (383) [0.920, 0.954] | 0.931 (1727) [0.922, 0.940] | 0.935 (4585) [0.930, 0.940] | 0.931 (2822) [0.924, 0.938] | 0.714 (7) | 0.293 | flat +0.017 (noise 0.018) |
| reversal_k5_next | 0.553 (47) | 0.476 (397) [0.423, 0.542] | 0.505 (2086) [0.490, 0.522] | 0.485 (6003) [0.474, 0.496] | 0.480 (4013) [0.466, 0.494] | 1.000 (3) | 0.187 | flat -0.024 (noise 0.041) |
| reversal_k5_now | 0.831 (65) | 0.794 (437) [0.770, 0.816] | 0.795 (1751) [0.779, 0.810] | 0.817 (4368) [0.806, 0.826] | 0.804 (2757) [0.792, 0.816] | 0.667 (9) | 0.187 | flat +0.056 (noise 0.029) |
| reversal_k8_next | 0.388 (85) | 0.397 (541) [0.369, 0.441] | 0.408 (2360) [0.394, 0.423] | 0.397 (6234) [0.387, 0.406] | 0.397 (4128) [0.385, 0.408] | 0.727 (11) | 0.121 | flat -0.013 (noise 0.031) |
| reversal_k8_now | 0.712 (59) | 0.675 (416) [0.636, 0.718] | 0.682 (1628) [0.662, 0.701] | 0.695 (4218) [0.683, 0.708] | 0.684 (2631) [0.669, 0.699] | 0.667 (9) | 0.122 | flat +0.012 (noise 0.034) |
| overall | 0.514 (22249) | 0.507 (154986) [0.505, 0.510] | 0.506 (661743) [0.505, 0.507] | 0.504 (1764523) [0.503, 0.505] | 0.505 (1081242) [0.504, 0.506] | 0.500 (3647) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06938, 0.09988] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5353, 'levels': [{'threshold': 0.06938, 'calls_per_day': 143.3, 'win_rate': 0.5547}, {'threshold': 0.09988, 'calls_per_day': 35.9, 'win_rate': 0.631}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42894, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14960 | 0.348 | 0.532 (14744) | 0.566 (2209) | 0.753 (2474) |
| volatility: normal | 14959 | 0.377 | 0.527 (14902) | 0.592 (1383) | 0.740 (2379) |
| volatility: wild | 14960 | 0.391 | 0.532 (14921) | 0.582 (1051) | 0.757 (2125) |
| session: Asia 00-08 | 15119 | 0.370 | 0.531 (15007) | 0.571 (1640) | 0.748 (2263) |
| session: Europe 08-13 | 9300 | 0.365 | 0.530 (9225) | 0.578 (1149) | 0.758 (1511) |
| session: US 13-21 | 14880 | 0.380 | 0.534 (14790) | 0.604 (1276) | 0.747 (2384) |
| session: late 21-24 | 5580 | 0.366 | 0.518 (5545) | 0.536 (578) | 0.750 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.365 | 0.348 | 0.335 | 0.335 | 0.517 | 0.259 | 0.471 | 0.880 |
| 6h | 360 | 0.388 | 0.363 | 0.308 | 0.323 | 0.538 | 0.273 | 0.502 | 1.127 |
| 24h | 1440 | 0.397 | 0.384 | 0.316 | 0.348 | 0.539 | 0.276 | 0.518 | 1.159 |
| 7d | 10080 | 0.389 | 0.378 | 0.305 | 0.341 | 0.536 | 0.272 | 0.505 | 1.180 |
| 30d | 43200 | 0.372 | 0.365 | 0.286 | 0.317 | 0.530 | 0.266 | 0.478 | 1.261 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.365 / 0.517 / 0.850; 2: 0.340 / 0.467 / 0.817; 3: 0.372 / 0.533 / 0.917; 4: 0.353 / 0.533 / 0.800; 5: 0.347 / 0.500 / 0.767; 6: 0.343 / 0.483 / 0.817; 7: 0.344 / 0.583 / 0.783; 8: 0.329 / 0.500 / 0.750; 9: 0.323 / 0.550 / 0.733; 10: 0.305 / 0.467 / 0.717; 11: 0.333 / 0.617 / 0.717; 12: 0.288 / 0.383 / 0.667; 13: 0.295 / 0.483 / 0.617; 14: 0.308 / 0.467 / 0.550; 15: 0.289 / 0.500 / 0.533
- 6h: 1: 0.388 / 0.538 / 0.917; 2: 0.367 / 0.473 / 0.947; 3: 0.380 / 0.510 / 0.986; 4: 0.368 / 0.499 / 0.928; 5: 0.373 / 0.507 / 0.919; 6: 0.377 / 0.524 / 0.950; 7: 0.365 / 0.487 / 0.950; 8: 0.369 / 0.487 / 0.950; 9: 0.359 / 0.482 / 0.939; 10: 0.369 / 0.510 / 0.931; 11: 0.368 / 0.541 / 0.911; 12: 0.354 / 0.454 / 0.903; 13: 0.356 / 0.490 / 0.892; 14: 0.357 / 0.499 / 0.856; 15: 0.359 / 0.507 / 0.858
- 24h: 1: 0.397 / 0.539 / 0.897; 2: 0.383 / 0.507 / 0.903; 3: 0.386 / 0.513 / 0.899; 4: 0.382 / 0.499 / 0.901; 5: 0.385 / 0.511 / 0.904; 6: 0.383 / 0.503 / 0.903; 7: 0.376 / 0.490 / 0.908; 8: 0.379 / 0.490 / 0.903; 9: 0.379 / 0.501 / 0.905; 10: 0.382 / 0.518 / 0.916; 11: 0.379 / 0.513 / 0.919; 12: 0.380 / 0.495 / 0.896; 13: 0.378 / 0.510 / 0.893; 14: 0.375 / 0.498 / 0.889; 15: 0.382 / 0.522 / 0.891
- 7d: 1: 0.389 / 0.536 / 0.900; 2: 0.375 / 0.494 / 0.899; 3: 0.379 / 0.512 / 0.899; 4: 0.375 / 0.494 / 0.900; 5: 0.377 / 0.508 / 0.900; 6: 0.376 / 0.506 / 0.900; 7: 0.375 / 0.504 / 0.901; 8: 0.376 / 0.511 / 0.900; 9: 0.370 / 0.494 / 0.901; 10: 0.375 / 0.511 / 0.901; 11: 0.373 / 0.504 / 0.901; 12: 0.373 / 0.504 / 0.901; 13: 0.372 / 0.503 / 0.900; 14: 0.372 / 0.502 / 0.900; 15: 0.370 / 0.498 / 0.900
- 30d: 1: 0.372 / 0.530 / 0.897; 2: 0.359 / 0.493 / 0.900; 3: 0.363 / 0.512 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.500 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.357 / 0.503 / 0.900; 11: 0.357 / 0.505 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.501 / 0.900; 14: 0.356 / 0.501 / 0.900; 15: 0.356 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.068 (body 0.049, range 0.088); 'price stays where it was' would score 0.049; colour right 0.517; typical miss of the close 45.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.151 (body 0.095, range 0.207); 'price stays where it was' would score 0.143; colour right 0.532; typical miss of the close 11.8 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.137 (body 0.088, range 0.186); 'price stays where it was' would score 0.150; colour right 0.518; typical miss of the close 17.5 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.130 (body 0.084, range 0.176); 'price stays where it was' would score 0.134; colour right 0.506; typical miss of the close 15.3 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.168); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.2 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.4; 2: 0.205 / 6.1; 3: 0.168 / 8.0; 4: 0.135 / 8.3; 5: 0.127 / 9.0; 6: 0.121 / 9.7; 7: 0.114 / 10.4; 8: 0.101 / 11.3; 9: 0.092 / 11.6; 10: 0.089 / 12.3; 11: 0.086 / 12.7; 12: 0.078 / 12.8; 13: 0.073 / 13.5; 14: 0.068 / 14.0; 15: 0.066 / 14.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 158393, probability skill vs chance 0.2291, widened contest next: True
  - now: threshold 0.8317, hit rate recent 0.8942 / long run 0.927
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.272, naive rule 0.490, lift 2.94x
    - 24h: 56 calls (56 a day), hit rate 0.893, chance 0.289, naive rule 0.491, lift 3.09x
    - 7d: 381 calls (54 a day), hit rate 0.932, chance 0.290, naive rule 0.502, lift 3.21x
    - 30d: 1730 calls (58 a day), hit rate 0.931, chance 0.293, naive rule 0.500, lift 3.18x
  - next: threshold 0.5078, hit rate recent 0.588 / long run 0.591
    - 6h: 35 calls (142 a day), hit rate 0.571, chance 0.272, lift 2.10x
    - 24h: 160 calls (161 a day), hit rate 0.575, chance 0.289, lift 1.99x
    - 7d: 545 calls (78 a day), hit rate 0.580, chance 0.290, lift 2.00x
    - 30d: 2377 calls (79 a day), hit rate 0.600, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.502; 0.35: 529, 0.527; 0.40: 477, 0.575; 0.45: 412, 0.641; 0.50: 363, 0.686; 0.55: 315, 0.732; 0.60: 265, 0.779; 0.65: 223, 0.808; 0.70: 175, 0.839; 0.75: 141, 0.873; 0.80: 93, 0.904; 0.85: 44, 0.941; 0.90: 4, 0.966
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 579, 0.436; 0.35: 489, 0.469; 0.40: 388, 0.509; 0.45: 293, 0.544; 0.50: 187, 0.575; 0.55: 81, 0.586; 0.60: 10, 0.633; 0.65: 0, 0.500
- **K=5**: model 1794528000, labels learned 158391, probability skill vs chance 0.2144, widened contest next: False
  - now: threshold 0.7006, hit rate recent 0.7947 / long run 0.7871
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.186, naive rule 0.437, lift 4.15x
    - 24h: 60 calls (60 a day), hit rate 0.783, chance 0.193, naive rule 0.415, lift 4.05x
    - 7d: 433 calls (62 a day), hit rate 0.797, chance 0.189, naive rule 0.417, lift 4.21x
    - 30d: 1756 calls (59 a day), hit rate 0.796, chance 0.187, naive rule 0.411, lift 4.26x
  - next: threshold 0.4625, hit rate recent 0.5191 / long run 0.4911
    - 6h: 6 calls (24 a day), hit rate 0.833, chance 0.186, lift 4.49x
    - 24h: 43 calls (43 a day), hit rate 0.581, chance 0.193, lift 3.01x
    - 7d: 393 calls (56 a day), hit rate 0.476, chance 0.189, lift 2.52x
    - 30d: 2069 calls (69 a day), hit rate 0.507, chance 0.187, lift 2.71x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.421; 0.35: 362, 0.473; 0.40: 294, 0.541; 0.45: 238, 0.601; 0.50: 187, 0.653; 0.55: 150, 0.687; 0.60: 115, 0.735; 0.65: 81, 0.771; 0.70: 50, 0.806; 0.75: 27, 0.840; 0.80: 7, 0.861
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 337, 0.392; 0.35: 251, 0.430; 0.40: 161, 0.460; 0.45: 64, 0.500; 0.50: 8, 0.552; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 158388, probability skill vs chance 0.2086, widened contest next: False
  - now: threshold 0.5782, hit rate recent 0.6878 / long run 0.6772
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.144, naive rule 0.410, lift 5.33x
    - 24h: 57 calls (57 a day), hit rate 0.667, chance 0.130, naive rule 0.362, lift 5.13x
    - 7d: 416 calls (59 a day), hit rate 0.678, chance 0.123, naive rule 0.351, lift 5.49x
    - 30d: 1632 calls (54 a day), hit rate 0.683, chance 0.122, naive rule 0.344, lift 5.58x
  - next: threshold 0.3616, hit rate recent 0.4476 / long run 0.4097
    - 6h: 18 calls (74 a day), hit rate 0.611, chance 0.144, lift 4.24x
    - 24h: 89 calls (90 a day), hit rate 0.427, chance 0.130, lift 3.28x
    - 7d: 548 calls (78 a day), hit rate 0.401, chance 0.123, lift 3.25x
    - 30d: 2349 calls (78 a day), hit rate 0.411, chance 0.122, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.426; 0.35: 199, 0.486; 0.40: 157, 0.536; 0.45: 120, 0.580; 0.50: 85, 0.638; 0.55: 61, 0.674; 0.60: 41, 0.714; 0.65: 23, 0.775; 0.70: 9, 0.816; 0.75: 2, 0.745
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 162, 0.374; 0.35: 84, 0.402; 0.40: 26, 0.436; 0.45: 6, 0.469; 0.50: 1, 0.692
- **K=13**: model 1795132800, labels learned 158383, probability skill vs chance 0.1861, widened contest next: False
  - now: threshold 0.4522, hit rate recent 0.5905 / long run 0.5709
    - 6h: 12 calls (50 a day), hit rate 0.750, chance 0.090, naive rule 0.326, lift 8.35x
    - 24h: 47 calls (47 a day), hit rate 0.638, chance 0.083, naive rule 0.295, lift 7.68x
    - 7d: 371 calls (53 a day), hit rate 0.580, chance 0.080, naive rule 0.294, lift 7.28x
    - 30d: 1629 calls (54 a day), hit rate 0.573, chance 0.079, naive rule 0.290, lift 7.28x
  - next: threshold 0.3059, hit rate recent 0.3589 / long run 0.3219
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.090, lift 6.96x
    - 24h: 55 calls (56 a day), hit rate 0.382, chance 0.083, lift 4.59x
    - 7d: 495 calls (71 a day), hit rate 0.309, chance 0.080, lift 3.88x
    - 30d: 1863 calls (62 a day), hit rate 0.328, chance 0.079, lift 4.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 139, 0.424; 0.35: 101, 0.474; 0.40: 70, 0.535; 0.45: 49, 0.584; 0.50: 34, 0.625; 0.55: 21, 0.649; 0.60: 10, 0.685; 0.65: 2, 0.592; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.338; 0.35: 15, 0.364; 0.40: 2, 0.425; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 65.977 | 6.73% | 0.850 | 0.450 | 0.253 | 0.433 | 0.483 |
| 6h | 26.099 | 7.15% | 0.922 | 0.511 | 0.252 | 0.468 | 0.671 |
| 24h | 31.721 | 4.74% | 0.900 | 0.503 | 0.250 | 0.507 | 0.691 |
| 7d | 25.637 | 4.04% | 0.900 | 0.501 | 0.250 | 0.499 | 0.679 |
| 30d | 18.439 | 4.69% | 0.900 | 0.500 | 0.250 | 0.504 | 0.720 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 70.738 | 67.241 | 66.272 | 65.652 | 68.981 | 67.525 | 66.113 | 65.801 | 65.909 | 65.977 |
| 6h | 28.110 | 26.429 | 26.051 | 26.215 | 26.801 | 26.241 | 26.111 | 26.010 | 26.057 | 26.099 |
| 24h | 33.299 | 31.949 | 31.846 | 31.744 | 32.154 | 32.013 | 31.769 | 31.662 | 31.681 | 31.721 |
| 7d | 26.716 | 25.788 | 25.767 | 25.655 | 26.110 | 25.907 | 25.617 | 25.587 | 25.592 | 25.637 |
| 30d | 19.347 | 18.602 | 18.560 | 18.493 | 18.799 | 18.736 | 18.420 | 18.399 | 18.406 | 18.439 |

## Next candle

- candle starting 2026-11-21 03:59 UTC, last close 1568.59
- P(up) 0.5123, return quantiles (bp): {'05': -34.344, '10': -23.655, '25': -13.351, '40': -4.72, '50': 0.647, '60': 5.31, '75': 10.942, '90': 21.294, '95': 30.508}
- changepoint probability 0.1512, regime age 19.3 min
- agent weights: empirical 0.003, ewma 0.067, garch 0.135, har 0.205, bocpd 0.018, hmm 0.049, online_qr 0.195, lgbm 0.330

## Learning log

- 2026-11-19 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9149}, "hmm": {"sd_bp": [5.82, 10.34, 24.91], "stay": [0.973, 0.95, 0.93]}, "lgbm": {"challenger_loss": 0.25579, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47263, "challengers": 1, "chance_loss": 0.6006, "widened": false, "champion_loss": 0.47066, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37657, "challengers": 3, "chance_loss": 0.48758, "widened": true, "champion_loss": 0.37568, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27842, "challengers": 1, "chance_loss": 0.37356, "widened": false, "champion_loss": 0.27745, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2019, "challengers": 3, "chance_loss": 0.2763, "widened": true, "champion_loss": 0.20153, "promoted": false}}
- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- HMM volatility states (sd, bp per minute): [5.81, 9.88, 20.94], current probabilities: [0.046, 0.529, 0.425]
- live generator: {'versions': 60, 'latest_effective': '2026-11-21 04:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.285, 'l_abs': 0.668, 'l_hi': 0.786, 'l_lo': 0.725, 'b05': 0.687, 'b25': 0.669, 'b75': 0.664, 'b95': 0.738}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6]], 'cone_width': [1.351, 2.024, 1.918, 2.064, 2.311, 2.404, 2.962, 2.848, 3.008, 3.225, 3.584, 3.969, 4.747, 4.73]}
- calibration offsets (in sigma): {'05': -0.051, '10': 0.018, '25': -0.025, '40': -0.018, '50': 0.01, '60': 0.018, '75': -0.055, '90': -0.078, '95': -0.039}
