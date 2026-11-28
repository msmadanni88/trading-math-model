# ETH-USD 60s candle generator - report

- generated: 2026-11-28 02:47 UTC
- last closed candle: 2026-11-28 02:47 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.487 (671) [0.469, 0.507] | 0.507 (2878) [0.492, 0.522] | 0.514 (8344) [0.504, 0.524] | 0.515 (5372) [0.502, 0.529] | 0.545 (11) | 0.500 | flat -0.051 (noise 0.027) |
| colour_clear | 0.578 (770) | 0.559 (5422) [0.547, 0.573] | 0.545 (23728) [0.538, 0.552] | 0.528 (68471) [0.523, 0.533] | 0.546 (44233) [0.541, 0.550] | 0.569 (102) | 0.500 | flat +0.008 (noise 0.011) |
| colour_confident | 0.542 (155) | 0.568 (1411) [0.553, 0.582] | 0.566 (4515) [0.557, 0.576] | 0.583 (8417) [0.574, 0.592] | 0.583 (8417) [0.574, 0.592] | 0.516 (31) | 0.500 | flat +0.012 (noise 0.020) |
| colour_next | 0.553 (1435) | 0.541 (10040) [0.531, 0.550] | 0.533 (42909) [0.529, 0.538] | 0.520 (124392) [0.517, 0.524] | 0.531 (80043) [0.528, 0.535] | 0.530 (166) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.506 (20090) | 0.500 (140560) [0.498, 0.503] | 0.502 (600726) [0.501, 0.503] | 0.501 (1741488) [0.500, 0.502] | 0.501 (1120602) [0.500, 0.502] | 0.482 (2324) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.500 (44) | 0.545 (437) [0.496, 0.585] | 0.591 (1191) [0.567, 0.614] | 0.610 (2264) [0.592, 0.626] | 0.610 (2264) [0.592, 0.626] | 0.750 (8) | 0.500 | flat -0.067 (noise 0.037) |
| reversal_k13_next | 0.245 (53) | 0.352 (366) [0.303, 0.407] | 0.333 (1824) [0.316, 0.353] | 0.317 (5671) [0.307, 0.326] | 0.327 (3566) [0.316, 0.338] | 0.333 (6) | 0.078 | flat +0.042 (noise 0.039) |
| reversal_k13_now | 0.491 (59) | 0.599 (357) [0.544, 0.656] | 0.579 (1591) [0.557, 0.602] | 0.575 (4486) [0.563, 0.587] | 0.572 (3014) [0.557, 0.588] | 0.833 (6) | 0.078 | flat +0.023 (noise 0.048) |
| reversal_k3_next | 0.653 (98) | 0.609 (984) [0.583, 0.633] | 0.603 (2715) [0.590, 0.617] | 0.591 (7712) [0.583, 0.598] | 0.592 (5272) [0.582, 0.602] | 0.778 (9) | 0.295 | flat +0.031 (noise 0.027) |
| reversal_k3_now | 0.933 (60) | 0.934 (407) [0.922, 0.946] | 0.929 (1735) [0.922, 0.937] | 0.935 (4992) [0.930, 0.940] | 0.931 (3229) [0.925, 0.938] | 1.000 (5) | 0.294 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.400 (55) | 0.503 (382) [0.454, 0.560] | 0.506 (1702) [0.485, 0.529] | 0.486 (6385) [0.475, 0.497] | 0.482 (4395) [0.469, 0.496] | 0.625 (8) | 0.187 | flat +0.026 (noise 0.051) |
| reversal_k5_now | 0.769 (52) | 0.817 (427) [0.789, 0.847] | 0.794 (1789) [0.777, 0.810] | 0.817 (4795) [0.807, 0.826] | 0.806 (3184) [0.795, 0.817] | 0.857 (7) | 0.188 | flat +0.023 (noise 0.027) |
| reversal_k8_next | 0.348 (66) | 0.419 (527) [0.368, 0.471] | 0.418 (2143) [0.401, 0.438] | 0.398 (6761) [0.388, 0.408] | 0.399 (4655) [0.387, 0.411] | 0.400 (5) | 0.121 | flat +0.022 (noise 0.038) |
| reversal_k8_now | 0.576 (59) | 0.675 (409) [0.634, 0.714] | 0.680 (1668) [0.662, 0.698] | 0.694 (4627) [0.681, 0.706] | 0.683 (3040) [0.668, 0.697] | 0.800 (5) | 0.122 | flat -0.001 (noise 0.035) |
| overall | 0.510 (22123) | 0.506 (155130) [0.504, 0.507] | 0.506 (661680) [0.505, 0.507] | 0.504 (1919653) [0.504, 0.505] | 0.505 (1236372) [0.504, 0.506] | 0.490 (2552) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08652, 0.1245] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5404, 'levels': [{'threshold': 0.08652, 'calls_per_day': 147.3, 'win_rate': 0.5623}, {'threshold': 0.1245, 'calls_per_day': 37.0, 'win_rate': 0.5538}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42908, 'rate': 0.5333}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14936 | 0.355 | 0.537 (14719) | 0.550 (1971) | 0.748 (2570) |
| volatility: normal | 14935 | 0.381 | 0.528 (14885) | 0.567 (1527) | 0.752 (2381) |
| volatility: wild | 14936 | 0.392 | 0.534 (14902) | 0.592 (1168) | 0.755 (2119) |
| session: Asia 00-08 | 15047 | 0.374 | 0.533 (14945) | 0.556 (1643) | 0.746 (2265) |
| session: Europe 08-13 | 9300 | 0.370 | 0.531 (9224) | 0.576 (1121) | 0.776 (1477) |
| session: US 13-21 | 14880 | 0.383 | 0.537 (14791) | 0.593 (1322) | 0.739 (2433) |
| session: late 21-24 | 5580 | 0.372 | 0.524 (5546) | 0.512 (580) | 0.760 (895) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.372 | 0.341 | 0.242 | 0.242 | 0.508 | 0.272 | 0.471 | 0.884 |
| 6h | 360 | 0.383 | 0.354 | 0.256 | 0.291 | 0.561 | 0.287 | 0.478 | 1.104 |
| 24h | 1440 | 0.390 | 0.371 | 0.279 | 0.316 | 0.550 | 0.286 | 0.494 | 1.209 |
| 7d | 10080 | 0.386 | 0.376 | 0.289 | 0.323 | 0.540 | 0.272 | 0.499 | 1.221 |
| 30d | 43200 | 0.376 | 0.369 | 0.288 | 0.320 | 0.533 | 0.268 | 0.485 | 1.264 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.372 / 0.508 / 0.900; 2: 0.331 / 0.441 / 0.950; 3: 0.365 / 0.525 / 1.000; 4: 0.333 / 0.508 / 0.950; 5: 0.328 / 0.458 / 1.000; 6: 0.327 / 0.407 / 1.000; 7: 0.350 / 0.525 / 1.000; 8: 0.316 / 0.390 / 1.000; 9: 0.328 / 0.407 / 1.000; 10: 0.348 / 0.525 / 1.000; 11: 0.344 / 0.492 / 1.000; 12: 0.344 / 0.492 / 1.000; 13: 0.376 / 0.559 / 1.000; 14: 0.347 / 0.407 / 1.000; 15: 0.352 / 0.458 / 1.000
- 6h: 1: 0.383 / 0.561 / 0.903; 2: 0.365 / 0.545 / 0.953; 3: 0.369 / 0.528 / 0.994; 4: 0.354 / 0.508 / 0.958; 5: 0.366 / 0.520 / 1.000; 6: 0.355 / 0.497 / 1.000; 7: 0.357 / 0.508 / 1.000; 8: 0.348 / 0.469 / 1.000; 9: 0.356 / 0.494 / 1.000; 10: 0.352 / 0.475 / 1.000; 11: 0.350 / 0.466 / 1.000; 12: 0.344 / 0.447 / 1.000; 13: 0.368 / 0.508 / 1.000; 14: 0.356 / 0.466 / 1.000; 15: 0.349 / 0.480 / 1.000
- 24h: 1: 0.390 / 0.550 / 0.906; 2: 0.368 / 0.510 / 0.910; 3: 0.369 / 0.516 / 0.915; 4: 0.369 / 0.513 / 0.934; 5: 0.366 / 0.497 / 0.912; 6: 0.360 / 0.492 / 0.917; 7: 0.368 / 0.526 / 0.904; 8: 0.361 / 0.501 / 0.900; 9: 0.361 / 0.499 / 0.901; 10: 0.358 / 0.484 / 0.900; 11: 0.356 / 0.482 / 0.903; 12: 0.357 / 0.486 / 0.901; 13: 0.368 / 0.530 / 0.910; 14: 0.359 / 0.498 / 0.892; 15: 0.362 / 0.513 / 0.903
- 7d: 1: 0.386 / 0.540 / 0.900; 2: 0.366 / 0.488 / 0.900; 3: 0.369 / 0.507 / 0.901; 4: 0.366 / 0.499 / 0.901; 5: 0.367 / 0.500 / 0.899; 6: 0.363 / 0.494 / 0.900; 7: 0.367 / 0.510 / 0.897; 8: 0.365 / 0.507 / 0.898; 9: 0.363 / 0.495 / 0.896; 10: 0.364 / 0.506 / 0.897; 11: 0.363 / 0.500 / 0.898; 12: 0.364 / 0.504 / 0.897; 13: 0.361 / 0.493 / 0.898; 14: 0.361 / 0.497 / 0.896; 15: 0.361 / 0.504 / 0.897
- 30d: 1: 0.376 / 0.533 / 0.898; 2: 0.362 / 0.491 / 0.900; 3: 0.366 / 0.512 / 0.900; 4: 0.362 / 0.497 / 0.900; 5: 0.363 / 0.505 / 0.900; 6: 0.360 / 0.500 / 0.900; 7: 0.362 / 0.503 / 0.900; 8: 0.361 / 0.507 / 0.900; 9: 0.360 / 0.499 / 0.900; 10: 0.360 / 0.504 / 0.900; 11: 0.360 / 0.505 / 0.900; 12: 0.360 / 0.503 / 0.900; 13: 0.359 / 0.500 / 0.900; 14: 0.358 / 0.501 / 0.900; 15: 0.358 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.093 (body 0.057, range 0.129); 'price stays where it was' would score 0.112; colour right 0.407; typical miss of the close 8.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.111 (body 0.067, range 0.156); 'price stays where it was' would score 0.130; colour right 0.466; typical miss of the close 8.8 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.135 (body 0.089, range 0.181); 'price stays where it was' would score 0.154; colour right 0.492; typical miss of the close 10.7 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.135 (body 0.088, range 0.182); 'price stays where it was' would score 0.145; colour right 0.495; typical miss of the close 12.3 bp; chain ended on the right side 0.492 of 671 chains; n=10080
- 30d: match 0.128 (body 0.085, range 0.171); 'price stays where it was' would score 0.132; colour right 0.503; typical miss of the close 11.1 bp; chain ended on the right side 0.509 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.372 / 6.0; 2: 0.206 / 6.8; 3: 0.168 / 8.8; 4: 0.136 / 9.2; 5: 0.124 / 10.0; 6: 0.120 / 10.7; 7: 0.118 / 11.1; 8: 0.105 / 12.2; 9: 0.093 / 13.0; 10: 0.090 / 13.3; 11: 0.086 / 13.8; 12: 0.083 / 14.1; 13: 0.077 / 15.0; 14: 0.070 / 15.3; 15: 0.067 / 15.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 168401, probability skill vs chance 0.2311, widened contest next: False
  - now: threshold 0.8294, hit rate recent 0.9384 / long run 0.9318
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.311, naive rule 0.549, lift 3.00x
    - 24h: 58 calls (58 a day), hit rate 0.931, chance 0.317, naive rule 0.542, lift 2.94x
    - 7d: 408 calls (58 a day), hit rate 0.934, chance 0.307, naive rule 0.531, lift 3.05x
    - 30d: 1731 calls (58 a day), hit rate 0.929, chance 0.296, naive rule 0.508, lift 3.14x
  - next: threshold 0.5429, hit rate recent 0.638 / long run 0.6078
    - 6h: 18 calls (73 a day), hit rate 0.611, chance 0.311, lift 1.96x
    - 24h: 94 calls (94 a day), hit rate 0.660, chance 0.317, lift 2.08x
    - 7d: 979 calls (140 a day), hit rate 0.609, chance 0.307, lift 1.99x
    - 30d: 2704 calls (90 a day), hit rate 0.605, chance 0.296, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.506; 0.35: 530, 0.531; 0.40: 484, 0.573; 0.45: 422, 0.634; 0.50: 370, 0.682; 0.55: 323, 0.727; 0.60: 274, 0.771; 0.65: 229, 0.801; 0.70: 180, 0.832; 0.75: 144, 0.870; 0.80: 95, 0.901; 0.85: 41, 0.944; 0.90: 3, 0.956
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.437; 0.35: 487, 0.473; 0.40: 382, 0.515; 0.45: 289, 0.548; 0.50: 186, 0.576; 0.55: 78, 0.596; 0.60: 9, 0.642; 0.65: 0, 0.538
- **K=5**: model 1795824000, labels learned 168399, probability skill vs chance 0.2188, widened contest next: True
  - now: threshold 0.7052, hit rate recent 0.797 / long run 0.8042
    - 6h: 15 calls (61 a day), hit rate 0.667, chance 0.203, naive rule 0.439, lift 3.29x
    - 24h: 50 calls (50 a day), hit rate 0.760, chance 0.201, naive rule 0.448, lift 3.78x
    - 7d: 430 calls (61 a day), hit rate 0.816, chance 0.197, naive rule 0.446, lift 4.15x
    - 30d: 1786 calls (60 a day), hit rate 0.795, chance 0.189, naive rule 0.420, lift 4.19x
  - next: threshold 0.445, hit rate recent 0.4585 / long run 0.4922
    - 6h: 15 calls (61 a day), hit rate 0.400, chance 0.203, lift 1.97x
    - 24h: 57 calls (57 a day), hit rate 0.421, chance 0.201, lift 2.10x
    - 7d: 388 calls (55 a day), hit rate 0.503, chance 0.197, lift 2.55x
    - 30d: 1701 calls (57 a day), hit rate 0.507, chance 0.189, lift 2.67x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.429; 0.35: 364, 0.478; 0.40: 295, 0.545; 0.45: 239, 0.605; 0.50: 186, 0.655; 0.55: 150, 0.686; 0.60: 117, 0.731; 0.65: 86, 0.766; 0.70: 55, 0.803; 0.75: 27, 0.841; 0.80: 6, 0.849
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 328, 0.399; 0.35: 243, 0.438; 0.40: 155, 0.463; 0.45: 62, 0.506; 0.50: 9, 0.561; 0.55: 1, 0.529
- **K=8**: model 1794960000, labels learned 168396, probability skill vs chance 0.196, widened contest next: True
  - now: threshold 0.5897, hit rate recent 0.6391 / long run 0.6771
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.133, naive rule 0.381, lift 4.63x
    - 24h: 57 calls (57 a day), hit rate 0.632, chance 0.134, naive rule 0.386, lift 4.70x
    - 7d: 410 calls (59 a day), hit rate 0.673, chance 0.128, naive rule 0.376, lift 5.28x
    - 30d: 1665 calls (56 a day), hit rate 0.680, chance 0.124, naive rule 0.353, lift 5.49x
  - next: threshold 0.3705, hit rate recent 0.3677 / long run 0.4065
    - 6h: 12 calls (49 a day), hit rate 0.333, chance 0.133, lift 2.51x
    - 24h: 65 calls (65 a day), hit rate 0.338, chance 0.134, lift 2.52x
    - 7d: 523 calls (75 a day), hit rate 0.413, chance 0.128, lift 3.24x
    - 30d: 2134 calls (71 a day), hit rate 0.419, chance 0.124, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 261, 0.425; 0.35: 206, 0.485; 0.40: 161, 0.535; 0.45: 122, 0.577; 0.50: 88, 0.632; 0.55: 65, 0.669; 0.60: 44, 0.710; 0.65: 25, 0.772; 0.70: 9, 0.814; 0.75: 1, 0.742
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 156, 0.377; 0.35: 84, 0.406; 0.40: 31, 0.437; 0.45: 7, 0.466; 0.50: 1, 0.605; 0.55: 0, 0.200
- **K=13**: model 1795478400, labels learned 168391, probability skill vs chance 0.1795, widened contest next: True
  - now: threshold 0.4574, hit rate recent 0.5622 / long run 0.5835
    - 6h: 15 calls (63 a day), hit rate 0.600, chance 0.087, naive rule 0.308, lift 6.90x
    - 24h: 58 calls (59 a day), hit rate 0.552, chance 0.078, naive rule 0.303, lift 7.08x
    - 7d: 358 calls (51 a day), hit rate 0.601, chance 0.084, naive rule 0.336, lift 7.17x
    - 30d: 1585 calls (53 a day), hit rate 0.582, chance 0.080, naive rule 0.303, lift 7.24x
  - next: threshold 0.2994, hit rate recent 0.2639 / long run 0.3285
    - 6h: 12 calls (50 a day), hit rate 0.250, chance 0.087, lift 2.88x
    - 24h: 53 calls (54 a day), hit rate 0.226, chance 0.078, lift 2.91x
    - 7d: 366 calls (52 a day), hit rate 0.350, chance 0.084, lift 4.18x
    - 30d: 1823 calls (61 a day), hit rate 0.335, chance 0.080, lift 4.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 144, 0.425; 0.35: 106, 0.473; 0.40: 73, 0.536; 0.45: 52, 0.584; 0.50: 36, 0.620; 0.55: 22, 0.644; 0.60: 10, 0.662; 0.65: 2, 0.527
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.338; 0.35: 15, 0.379; 0.40: 2, 0.435

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.122 | 6.27% | 0.900 | 0.383 | 0.251 | 0.407 | -0.009 |
| 6h | 11.872 | 6.30% | 0.911 | 0.458 | 0.251 | 0.455 | 0.239 |
| 24h | 19.276 | 6.01% | 0.904 | 0.500 | 0.250 | 0.489 | 0.749 |
| 7d | 23.080 | 4.97% | 0.901 | 0.500 | 0.250 | 0.509 | 0.661 |
| 30d | 20.328 | 4.92% | 0.900 | 0.500 | 0.250 | 0.507 | 0.705 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.867 | 11.108 | 11.092 | 11.296 | 11.215 | 11.286 | 11.274 | 11.071 | 11.129 | 11.122 |
| 6h | 12.670 | 11.907 | 11.917 | 11.882 | 12.139 | 12.179 | 11.880 | 11.840 | 11.851 | 11.872 |
| 24h | 20.507 | 19.526 | 19.370 | 19.285 | 19.640 | 19.459 | 19.232 | 19.235 | 19.234 | 19.276 |
| 7d | 24.285 | 23.374 | 23.262 | 23.101 | 23.703 | 23.456 | 23.058 | 23.016 | 23.042 | 23.080 |
| 30d | 21.381 | 20.522 | 20.470 | 20.383 | 20.761 | 20.675 | 20.307 | 20.281 | 20.293 | 20.328 |

## Next candle

- candle starting 2026-11-28 02:47 UTC, last close 1660.82
- P(up) 0.5191, return quantiles (bp): {'05': -8.005, '10': -5.688, '25': -2.949, '40': -0.824, '50': 0.19, '60': 1.491, '75': 2.846, '90': 5.158, '95': 6.803}
- changepoint probability 0.0397, regime age 96.4 min
- agent weights: empirical 0.003, ewma 0.085, garch 0.143, har 0.175, bocpd 0.035, hmm 0.052, online_qr 0.246, lgbm 0.261

## Learning log

- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- 2026-11-26 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.8951}, "hmm": {"sd_bp": [5.1, 9.79, 29.67], "stay": [0.964, 0.952, 0.897]}}
- 2026-11-27 00:00 UTC: {"garch": {"alpha": 0.086, "beta": 0.8972}, "hmm": {"sd_bp": [4.98, 9.67, 29.65], "stay": [0.967, 0.957, 0.909]}, "lgbm": {"challenger_loss": 0.24936, "champion_loss": 0.2495, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48669, "challengers": 1, "chance_loss": 0.61724, "widened": false, "champion_loss": 0.48438, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37811, "challengers": 1, "chance_loss": 0.49376, "widened": false, "champion_loss": 0.37659, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27446, "challengers": 1, "chance_loss": 0.3744, "widened": false, "champion_loss": 0.27383, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21177, "challengers": 1, "chance_loss": 0.29738, "widened": false, "champion_loss": 0.21069, "promoted": false}}
- 2026-11-27 12:00 UTC: {"garch": {"alpha": 0.0974, "beta": 0.8821}, "hmm": {"sd_bp": [5.02, 9.65, 29.47], "stay": [0.968, 0.955, 0.908]}}
- 2026-11-28 00:00 UTC: {"garch": {"alpha": 0.0767, "beta": 0.9088}, "hmm": {"sd_bp": [4.93, 9.34, 24.25], "stay": [0.971, 0.955, 0.925]}, "lgbm": {"challenger_loss": 0.24844, "champion_loss": 0.24848, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49387, "challengers": 1, "chance_loss": 0.6223, "widened": false, "champion_loss": 0.49186, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38744, "challengers": 3, "chance_loss": 0.50214, "widened": true, "champion_loss": 0.38761, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28933, "challengers": 3, "chance_loss": 0.38088, "widened": true, "champion_loss": 0.2893, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20501, "challengers": 3, "chance_loss": 0.27801, "widened": true, "champion_loss": 0.20422, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.93, 9.34, 24.25], current probabilities: [0.9, 0.097, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-11-28 02:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.46, 'l_abs': 0.695, 'l_hi': 0.727, 'l_lo': 0.71, 'b05': 0.709, 'b25': 0.692, 'b75': 0.679, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [1.156, 1.803, 1.545, 2.201, 2.368, 3.6, 4.014, 5.006, 4.689, 4.371, 4.857, 4.317, 7.254, 6.038]}
- calibration offsets (in sigma): {'05': 0.013, '10': 0.026, '25': -0.065, '40': -0.026, '50': -0.03, '60': 0.006, '75': -0.045, '90': -0.076, '95': -0.123}
