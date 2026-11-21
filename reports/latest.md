# ETH-USD 60s candle generator - report

- generated: 2026-11-21 12:27 UTC
- last closed candle: 2026-11-21 12:27 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.539 (672) [0.506, 0.567] | 0.519 (2879) [0.502, 0.535] | 0.516 (7673) [0.505, 0.528] | 0.519 (4701) [0.505, 0.534] | 0.449 (49) | 0.500 | flat +0.010 (noise 0.027) |
| colour_clear | 0.577 (822) | 0.551 (5657) [0.538, 0.565] | 0.541 (23972) [0.535, 0.548] | 0.525 (63049) [0.520, 0.531] | 0.544 (38811) [0.539, 0.548] | 0.527 (364) | 0.500 | flat +0.010 (noise 0.010) |
| colour_confident | 0.562 (96) | 0.556 (1109) [0.533, 0.583] | 0.576 (4419) [0.564, 0.587] | 0.586 (7006) [0.576, 0.596] | 0.586 (7006) [0.576, 0.596] | 0.634 (112) | 0.500 | flat -0.003 (noise 0.022) |
| colour_next | 0.542 (1438) | 0.536 (10050) [0.529, 0.541] | 0.530 (42896) [0.526, 0.534] | 0.519 (114352) [0.515, 0.522] | 0.530 (70003) [0.527, 0.533] | 0.516 (744) | 0.500 | flat +0.006 (noise 0.007) |
| colour_path | 0.509 (20132) | 0.503 (140700) [0.501, 0.506] | 0.502 (600544) [0.501, 0.503] | 0.501 (1600928) [0.500, 0.502] | 0.501 (980042) [0.500, 0.503] | 0.503 (10416) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.643 (14) | 0.611 (288) [0.576, 0.657] | 0.614 (1159) [0.598, 0.631] | 0.626 (1827) [0.610, 0.641] | 0.626 (1827) [0.610, 0.641] | 0.657 (35) | 0.500 | flat -0.012 (noise 0.043) |
| reversal_k13_next | 0.362 (58) | 0.310 (493) [0.278, 0.352] | 0.326 (1868) [0.310, 0.343] | 0.314 (5305) [0.305, 0.323] | 0.324 (3200) [0.313, 0.335] | 0.417 (24) | 0.077 | flat -0.016 (noise 0.030) |
| reversal_k13_now | 0.644 (45) | 0.577 (371) [0.526, 0.637] | 0.572 (1625) [0.552, 0.593] | 0.573 (4129) [0.561, 0.586] | 0.569 (2657) [0.553, 0.585] | 0.600 (25) | 0.077 | flat +0.016 (noise 0.038) |
| reversal_k3_next | 0.562 (160) | 0.578 (526) [0.560, 0.609] | 0.598 (2379) [0.587, 0.610] | 0.588 (6728) [0.580, 0.596] | 0.588 (4288) [0.579, 0.599] | 0.646 (82) | 0.293 | flat -0.039 (noise 0.034) |
| reversal_k3_now | 0.922 (64) | 0.937 (383) [0.920, 0.954] | 0.931 (1727) [0.922, 0.940] | 0.935 (4585) [0.930, 0.940] | 0.931 (2822) [0.924, 0.938] | 0.870 (23) | 0.293 | flat +0.017 (noise 0.018) |
| reversal_k5_next | 0.553 (47) | 0.476 (397) [0.423, 0.542] | 0.505 (2086) [0.490, 0.522] | 0.485 (6003) [0.474, 0.496] | 0.480 (4013) [0.466, 0.494] | 0.714 (14) | 0.187 | flat -0.024 (noise 0.041) |
| reversal_k5_now | 0.831 (65) | 0.794 (437) [0.770, 0.816] | 0.795 (1751) [0.779, 0.810] | 0.817 (4368) [0.806, 0.826] | 0.804 (2757) [0.792, 0.816] | 0.750 (24) | 0.187 | flat +0.056 (noise 0.029) |
| reversal_k8_next | 0.388 (85) | 0.397 (541) [0.369, 0.441] | 0.408 (2360) [0.394, 0.423] | 0.397 (6234) [0.387, 0.406] | 0.397 (4128) [0.385, 0.408] | 0.545 (33) | 0.121 | flat -0.013 (noise 0.031) |
| reversal_k8_now | 0.712 (59) | 0.675 (416) [0.636, 0.718] | 0.682 (1628) [0.662, 0.701] | 0.695 (4218) [0.683, 0.708] | 0.684 (2631) [0.669, 0.699] | 0.625 (24) | 0.122 | flat +0.012 (noise 0.034) |
| overall | 0.514 (22249) | 0.507 (154986) [0.505, 0.510] | 0.506 (661743) [0.505, 0.507] | 0.504 (1764523) [0.503, 0.505] | 0.505 (1081242) [0.504, 0.506] | 0.506 (11458) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07066, 0.101] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5332, 'levels': [{'threshold': 0.07066, 'calls_per_day': 147.8, 'win_rate': 0.5539}, {'threshold': 0.101, 'calls_per_day': 37.0, 'win_rate': 0.6308}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42893, 'rate': 0.53}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15129 | 0.349 | 0.532 (14912) | 0.568 (2226) | 0.754 (2509) |
| volatility: normal | 15129 | 0.377 | 0.528 (15072) | 0.590 (1408) | 0.741 (2401) |
| volatility: wild | 15129 | 0.391 | 0.530 (15090) | 0.585 (1073) | 0.753 (2130) |
| session: Asia 00-08 | 15360 | 0.370 | 0.530 (15247) | 0.570 (1665) | 0.748 (2300) |
| session: Europe 08-13 | 9567 | 0.366 | 0.531 (9492) | 0.583 (1188) | 0.756 (1536) |
| session: US 13-21 | 14880 | 0.380 | 0.534 (14790) | 0.604 (1276) | 0.747 (2384) |
| session: late 21-24 | 5580 | 0.366 | 0.518 (5545) | 0.536 (578) | 0.750 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.385 | 0.387 | 0.286 | 0.286 | 0.550 | 0.289 | 0.480 | 2.053 |
| 6h | 360 | 0.384 | 0.376 | 0.294 | 0.321 | 0.538 | 0.266 | 0.501 | 1.794 |
| 24h | 1440 | 0.391 | 0.380 | 0.311 | 0.336 | 0.532 | 0.271 | 0.511 | 1.523 |
| 7d | 10080 | 0.388 | 0.379 | 0.305 | 0.341 | 0.533 | 0.271 | 0.505 | 1.189 |
| 30d | 43200 | 0.372 | 0.366 | 0.286 | 0.318 | 0.530 | 0.266 | 0.479 | 1.264 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.385 / 0.550 / 0.933; 2: 0.348 / 0.500 / 0.933; 3: 0.343 / 0.583 / 0.933; 4: 0.346 / 0.417 / 0.917; 5: 0.332 / 0.467 / 0.900; 6: 0.325 / 0.550 / 0.900; 7: 0.333 / 0.550 / 0.883; 8: 0.316 / 0.533 / 0.867; 9: 0.333 / 0.533 / 0.833; 10: 0.343 / 0.600 / 0.817; 11: 0.337 / 0.483 / 0.817; 12: 0.333 / 0.500 / 0.800; 13: 0.331 / 0.500 / 0.783; 14: 0.317 / 0.483 / 0.783; 15: 0.343 / 0.550 / 0.767
- 6h: 1: 0.384 / 0.538 / 0.939; 2: 0.373 / 0.538 / 0.922; 3: 0.359 / 0.499 / 0.953; 4: 0.359 / 0.504 / 0.919; 5: 0.363 / 0.515 / 0.906; 6: 0.351 / 0.493 / 0.903; 7: 0.357 / 0.513 / 0.903; 8: 0.355 / 0.507 / 0.922; 9: 0.360 / 0.510 / 0.911; 10: 0.363 / 0.529 / 0.908; 11: 0.356 / 0.487 / 0.906; 12: 0.355 / 0.513 / 0.908; 13: 0.352 / 0.482 / 0.911; 14: 0.343 / 0.468 / 0.914; 15: 0.364 / 0.557 / 0.908
- 24h: 1: 0.391 / 0.532 / 0.909; 2: 0.379 / 0.509 / 0.917; 3: 0.376 / 0.504 / 0.929; 4: 0.372 / 0.495 / 0.915; 5: 0.375 / 0.502 / 0.909; 6: 0.373 / 0.505 / 0.903; 7: 0.369 / 0.495 / 0.912; 8: 0.370 / 0.497 / 0.917; 9: 0.372 / 0.516 / 0.915; 10: 0.374 / 0.523 / 0.910; 11: 0.369 / 0.508 / 0.907; 12: 0.369 / 0.498 / 0.911; 13: 0.366 / 0.496 / 0.915; 14: 0.363 / 0.489 / 0.906; 15: 0.373 / 0.532 / 0.910
- 7d: 1: 0.388 / 0.533 / 0.900; 2: 0.376 / 0.497 / 0.901; 3: 0.378 / 0.511 / 0.901; 4: 0.374 / 0.497 / 0.901; 5: 0.376 / 0.508 / 0.900; 6: 0.375 / 0.507 / 0.900; 7: 0.374 / 0.502 / 0.899; 8: 0.375 / 0.510 / 0.900; 9: 0.370 / 0.497 / 0.900; 10: 0.374 / 0.511 / 0.899; 11: 0.373 / 0.504 / 0.899; 12: 0.373 / 0.504 / 0.899; 13: 0.371 / 0.502 / 0.899; 14: 0.371 / 0.499 / 0.898; 15: 0.370 / 0.500 / 0.898
- 30d: 1: 0.372 / 0.530 / 0.898; 2: 0.360 / 0.493 / 0.900; 3: 0.363 / 0.512 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.358 / 0.503 / 0.900; 7: 0.358 / 0.500 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.357 / 0.502 / 0.900; 10: 0.358 / 0.503 / 0.900; 11: 0.357 / 0.505 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.501 / 0.900; 14: 0.356 / 0.501 / 0.900; 15: 0.356 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.167 (body 0.143, range 0.192); 'price stays where it was' would score 0.191; colour right 0.583; typical miss of the close 21.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.151 (body 0.110, range 0.192); 'price stays where it was' would score 0.151; colour right 0.529; typical miss of the close 17.7 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.140 (body 0.093, range 0.188); 'price stays where it was' would score 0.145; colour right 0.517; typical miss of the close 21.4 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.131 (body 0.085, range 0.177); 'price stays where it was' would score 0.136; colour right 0.506; typical miss of the close 15.8 bp; chain ended on the right side 0.528 of 672 chains; n=10080
- 30d: match 0.126 (body 0.084, range 0.168); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.3 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.5; 2: 0.204 / 6.1; 3: 0.168 / 8.1; 4: 0.135 / 8.4; 5: 0.126 / 9.1; 6: 0.120 / 9.8; 7: 0.115 / 10.4; 8: 0.101 / 11.4; 9: 0.093 / 11.8; 10: 0.089 / 12.4; 11: 0.085 / 12.9; 12: 0.079 / 12.9; 13: 0.073 / 13.6; 14: 0.067 / 14.1; 15: 0.066 / 14.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 158901, probability skill vs chance 0.2323, widened contest next: False
  - now: threshold 0.8308, hit rate recent 0.9024 / long run 0.9273
    - 6h: 7 calls (28 a day), hit rate 0.857, chance 0.276, naive rule 0.498, lift 3.10x
    - 24h: 51 calls (51 a day), hit rate 0.902, chance 0.289, naive rule 0.504, lift 3.12x
    - 7d: 374 calls (53 a day), hit rate 0.928, chance 0.290, naive rule 0.501, lift 3.20x
    - 30d: 1723 calls (57 a day), hit rate 0.932, chance 0.293, naive rule 0.500, lift 3.18x
  - next: threshold 0.5081, hit rate recent 0.6301 / long run 0.5966
    - 6h: 42 calls (170 a day), hit rate 0.595, chance 0.276, lift 2.16x
    - 24h: 162 calls (163 a day), hit rate 0.611, chance 0.289, lift 2.12x
    - 7d: 591 calls (84 a day), hit rate 0.582, chance 0.290, lift 2.01x
    - 30d: 2402 calls (80 a day), hit rate 0.601, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.502; 0.35: 529, 0.527; 0.40: 477, 0.575; 0.45: 412, 0.641; 0.50: 363, 0.686; 0.55: 314, 0.732; 0.60: 264, 0.778; 0.65: 222, 0.808; 0.70: 175, 0.840; 0.75: 141, 0.873; 0.80: 93, 0.904; 0.85: 44, 0.941; 0.90: 4, 0.966
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.436; 0.35: 489, 0.469; 0.40: 388, 0.510; 0.45: 292, 0.544; 0.50: 187, 0.576; 0.55: 80, 0.587; 0.60: 10, 0.631; 0.65: 0, 0.500
- **K=5**: model 1794528000, labels learned 158899, probability skill vs chance 0.2206, widened contest next: False
  - now: threshold 0.7004, hit rate recent 0.7934 / long run 0.7874
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.191, naive rule 0.435, lift 3.66x
    - 24h: 57 calls (57 a day), hit rate 0.754, chance 0.197, naive rule 0.436, lift 3.83x
    - 7d: 428 calls (61 a day), hit rate 0.794, chance 0.191, naive rule 0.420, lift 4.17x
    - 30d: 1752 calls (58 a day), hit rate 0.796, chance 0.187, naive rule 0.411, lift 4.26x
  - next: threshold 0.462, hit rate recent 0.5397 / long run 0.4938
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.191, lift 3.27x
    - 24h: 38 calls (38 a day), hit rate 0.605, chance 0.197, lift 3.08x
    - 7d: 384 calls (55 a day), hit rate 0.469, chance 0.191, lift 2.46x
    - 30d: 2036 calls (68 a day), hit rate 0.508, chance 0.187, lift 2.72x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.421; 0.35: 362, 0.473; 0.40: 293, 0.542; 0.45: 237, 0.602; 0.50: 187, 0.654; 0.55: 150, 0.687; 0.60: 114, 0.734; 0.65: 81, 0.772; 0.70: 50, 0.806; 0.75: 27, 0.841; 0.80: 7, 0.861
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 336, 0.392; 0.35: 251, 0.431; 0.40: 160, 0.461; 0.45: 65, 0.501; 0.50: 8, 0.550; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 158896, probability skill vs chance 0.2156, widened contest next: False
  - now: threshold 0.5794, hit rate recent 0.6679 / long run 0.6753
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.141, naive rule 0.434, lift 3.93x
    - 24h: 55 calls (55 a day), hit rate 0.618, chance 0.134, naive rule 0.395, lift 4.63x
    - 7d: 414 calls (59 a day), hit rate 0.662, chance 0.124, naive rule 0.353, lift 5.34x
    - 30d: 1632 calls (54 a day), hit rate 0.682, chance 0.123, naive rule 0.345, lift 5.56x
  - next: threshold 0.3561, hit rate recent 0.4527 / long run 0.4113
    - 6h: 16 calls (66 a day), hit rate 0.438, chance 0.141, lift 3.09x
    - 24h: 81 calls (82 a day), hit rate 0.444, chance 0.134, lift 3.33x
    - 7d: 548 calls (78 a day), hit rate 0.396, chance 0.124, lift 3.19x
    - 30d: 2337 calls (78 a day), hit rate 0.413, chance 0.123, lift 3.37x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.427; 0.35: 199, 0.487; 0.40: 156, 0.537; 0.45: 120, 0.580; 0.50: 85, 0.637; 0.55: 61, 0.673; 0.60: 41, 0.714; 0.65: 24, 0.772; 0.70: 9, 0.812; 0.75: 2, 0.739
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 162, 0.375; 0.35: 84, 0.404; 0.40: 26, 0.436; 0.45: 6, 0.473; 0.50: 1, 0.679
- **K=13**: model 1795132800, labels learned 158891, probability skill vs chance 0.1907, widened contest next: False
  - now: threshold 0.4538, hit rate recent 0.5858 / long run 0.5707
    - 6h: 11 calls (46 a day), hit rate 0.545, chance 0.109, naive rule 0.434, lift 5.02x
    - 24h: 50 calls (51 a day), hit rate 0.580, chance 0.087, naive rule 0.333, lift 6.69x
    - 7d: 373 calls (53 a day), hit rate 0.563, chance 0.080, naive rule 0.296, lift 7.05x
    - 30d: 1631 calls (54 a day), hit rate 0.573, chance 0.079, naive rule 0.292, lift 7.25x
  - next: threshold 0.3073, hit rate recent 0.3581 / long run 0.3227
    - 6h: 14 calls (58 a day), hit rate 0.286, chance 0.109, lift 2.63x
    - 24h: 49 calls (50 a day), hit rate 0.388, chance 0.087, lift 4.47x
    - 7d: 496 calls (71 a day), hit rate 0.302, chance 0.080, lift 3.79x
    - 30d: 1867 calls (62 a day), hit rate 0.330, chance 0.079, lift 4.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 139, 0.424; 0.35: 102, 0.474; 0.40: 70, 0.534; 0.45: 49, 0.584; 0.50: 34, 0.625; 0.55: 21, 0.650; 0.60: 10, 0.687; 0.65: 2, 0.592; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.339; 0.35: 15, 0.370; 0.40: 2, 0.425; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 38.410 | 2.17% | 0.917 | 0.467 | 0.246 | 0.550 | 0.241 |
| 6h | 33.038 | 6.55% | 0.933 | 0.525 | 0.250 | 0.513 | 0.623 |
| 24h | 37.786 | 6.14% | 0.910 | 0.508 | 0.250 | 0.502 | 0.647 |
| 7d | 26.697 | 4.26% | 0.900 | 0.500 | 0.250 | 0.499 | 0.676 |
| 30d | 18.727 | 4.77% | 0.900 | 0.500 | 0.250 | 0.504 | 0.721 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 39.262 | 40.691 | 41.448 | 38.717 | 41.952 | 38.445 | 38.157 | 38.199 | 38.493 | 38.410 |
| 6h | 35.352 | 34.178 | 33.704 | 33.079 | 33.883 | 33.512 | 33.192 | 33.054 | 33.071 | 33.038 |
| 24h | 40.256 | 38.474 | 38.195 | 37.791 | 38.591 | 38.345 | 37.859 | 37.697 | 37.755 | 37.786 |
| 7d | 27.885 | 26.912 | 26.864 | 26.706 | 27.218 | 27.002 | 26.683 | 26.644 | 26.653 | 26.697 |
| 30d | 19.664 | 18.904 | 18.856 | 18.781 | 19.098 | 19.032 | 18.709 | 18.686 | 18.694 | 18.727 |

## Next candle

- candle starting 2026-11-21 12:27 UTC, last close 1656.24
- P(up) 0.4655, return quantiles (bp): {'05': -16.166, '10': -10.398, '25': -5.8, '40': -2.619, '50': -0.888, '60': 1.741, '75': 5.365, '90': 11.96, '95': 17.249}
- changepoint probability 0.0567, regime age 41.4 min
- agent weights: empirical 0.003, ewma 0.014, garch 0.039, har 0.254, bocpd 0.009, hmm 0.048, online_qr 0.241, lgbm 0.394

## Learning log

- 2026-11-19 12:00 UTC: {"garch": {"alpha": 0.0611, "beta": 0.9214}, "hmm": {"sd_bp": [5.66, 9.9, 23.56], "stay": [0.974, 0.948, 0.868]}}
- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- HMM volatility states (sd, bp per minute): [5.86, 10.53, 26.19], current probabilities: [0.019, 0.931, 0.05]
- live generator: {'versions': 60, 'latest_effective': '2026-11-21 12:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.224, 'l_abs': 0.667, 'l_hi': 0.801, 'l_lo': 0.747, 'b05': 0.726, 'b25': 0.72, 'b75': 0.697, 'b95': 0.745}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.5], [1.3, 1.6], [1.3, 1.6], [1.3, 1.5], [1.2, 1.6], [1.2, 1.6], [1.2, 1.5], [1.2, 1.5], [1.2, 1.6], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [1.088, 1.138, 1.515, 1.952, 2.1, 2.228, 2.116, 2.249, 2.473, 2.599, 2.774, 2.952, 3.602, 3.662]}
- calibration offsets (in sigma): {'05': 0.083, '10': 0.166, '25': 0.085, '40': 0.024, '50': -0.02, '60': -0.004, '75': -0.035, '90': -0.066, '95': -0.043}
