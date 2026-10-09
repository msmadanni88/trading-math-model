# ETH-USD 60s candle generator - report

- generated: 2026-10-09 13:06 UTC
- last closed candle: 2026-10-09 13:06 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.506 (670) [0.454, 0.558] | 0.505 (2875) [0.485, 0.526] | 0.509 (3547) [0.492, 0.526] | 0.499 (575) [0.443, 0.557] | 0.500 (52) | 0.500 | flat -0.002 (noise 0.040) |
| colour_clear | 0.555 (827) | 0.540 (5230) [0.526, 0.552] | 0.507 (23188) [0.500, 0.514] | 0.504 (28748) [0.498, 0.510] | 0.547 (4510) [0.536, 0.556] | 0.533 (465) | 0.500 | up +0.048 (noise 0.010) |
| colour_confident | 0.596 (89) | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.612 (85) | 0.500 | - |
| colour_next | 0.528 (1434) | 0.527 (9974) [0.517, 0.538] | 0.507 (42883) [0.501, 0.512] | 0.505 (52891) [0.501, 0.510] | 0.531 (8542) [0.521, 0.541] | 0.510 (785) | 0.500 | up +0.025 (noise 0.007) |
| colour_path | 0.497 (20076) | 0.498 (139636) [0.495, 0.502] | 0.501 (600362) [0.499, 0.502] | 0.500 (740474) [0.499, 0.502] | 0.499 (119588) [0.494, 0.503] | 0.501 (10990) | 0.500 | flat -0.005 (noise 0.003) |
| colour_strong | 0.500 (20) | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.812 (16) | 0.500 | - |
| reversal_k13_next | 0.318 (66) | 0.312 (525) [0.291, 0.331] | 0.308 (2040) [0.294, 0.324] | 0.304 (2572) [0.290, 0.318] | 0.321 (467) [0.306, 0.336] | 0.286 (42) | 0.077 | flat +0.030 (noise 0.027) |
| reversal_k13_now | 0.612 (49) | 0.591 (391) [0.553, 0.636] | 0.585 (1481) [0.563, 0.609] | 0.582 (1811) [0.564, 0.602] | 0.587 (339) [0.544, 0.641] | 0.593 (27) | 0.077 | flat +0.007 (noise 0.038) |
| reversal_k3_next | 0.521 (71) | 0.572 (547) [0.542, 0.609] | 0.588 (2352) [0.572, 0.603] | 0.585 (2927) [0.572, 0.599] | 0.571 (487) [0.538, 0.613] | 0.512 (41) | 0.292 | flat -0.006 (noise 0.029) |
| reversal_k3_now | 0.917 (72) | 0.927 (399) [0.918, 0.939] | 0.940 (1692) [0.932, 0.948] | 0.939 (2108) [0.932, 0.947] | 0.927 (345) [0.917, 0.941] | 0.971 (34) | 0.292 | flat -0.028 (noise 0.017) |
| reversal_k5_next | 0.422 (71) | 0.449 (642) [0.420, 0.481] | 0.488 (2100) [0.468, 0.506] | 0.483 (2512) [0.466, 0.501] | 0.441 (522) [0.412, 0.480] | 0.400 (40) | 0.187 | flat -0.034 (noise 0.032) |
| reversal_k5_now | 0.758 (62) | 0.826 (397) [0.795, 0.858] | 0.833 (1573) [0.817, 0.849] | 0.835 (1949) [0.821, 0.850] | 0.823 (338) [0.788, 0.858] | 0.769 (26) | 0.187 | flat -0.042 (noise 0.026) |
| reversal_k8_next | 0.367 (120) | 0.387 (587) [0.359, 0.418] | 0.402 (2096) [0.385, 0.421] | 0.394 (2646) [0.379, 0.411] | 0.385 (540) [0.355, 0.418] | 0.370 (46) | 0.121 | flat -0.005 (noise 0.032) |
| reversal_k8_now | 0.625 (64) | 0.715 (411) [0.677, 0.756] | 0.723 (1582) [0.703, 0.742] | 0.713 (1947) [0.695, 0.732] | 0.711 (360) [0.670, 0.756] | 0.545 (22) | 0.121 | flat -0.038 (noise 0.036) |
| overall | 0.500 (22181) | 0.502 (154179) [0.498, 0.507] | 0.503 (661036) [0.502, 0.505] | 0.503 (815384) [0.501, 0.504] | 0.502 (132103) [0.497, 0.508] | 0.503 (12105) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07733, 0.1162] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5331, 'levels': [{'threshold': 0.07733, 'calls_per_day': 147.0, 'win_rate': 0.6077}, {'threshold': 0.1162, 'calls_per_day': 36.8, 'win_rate': 0.6577}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 8195, 'rate': 0.5318}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15142 | 0.335 | 0.515 (14931) | 0.607 (690) | 0.776 (2432) |
| volatility: normal | 15142 | 0.361 | 0.511 (15075) | 0.597 (154) | 0.771 (2127) |
| volatility: wild | 15142 | 0.374 | 0.496 (15096) | 0.643 (56) | 0.775 (2114) |
| session: Asia 00-08 | 15360 | 0.353 | 0.508 (15258) | 0.593 (327) | 0.778 (2199) |
| session: Europe 08-13 | 9600 | 0.351 | 0.506 (9540) | 0.598 (194) | 0.764 (1507) |
| session: US 13-21 | 14886 | 0.367 | 0.506 (14787) | 0.600 (220) | 0.782 (2176) |
| session: late 21-24 | 5580 | 0.350 | 0.511 (5517) | 0.660 (159) | 0.764 (791) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.357 | 0.385 | 0.277 | 0.277 | 0.467 | 0.266 | 0.448 | 1.269 |
| 6h | 360 | 0.356 | 0.359 | 0.273 | 0.306 | 0.503 | 0.264 | 0.448 | 1.061 |
| 24h | 1440 | 0.368 | 0.368 | 0.286 | 0.321 | 0.516 | 0.264 | 0.473 | 1.029 |
| 7d | 10080 | 0.351 | 0.346 | 0.273 | 0.297 | 0.528 | 0.253 | 0.449 | 1.234 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.507 | 0.248 | 0.465 | 1.282 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.357 / 0.467 / 0.967; 2: 0.331 / 0.417 / 1.000; 3: 0.379 / 0.567 / 1.000; 4: 0.376 / 0.567 / 1.000; 5: 0.337 / 0.400 / 1.000; 6: 0.370 / 0.550 / 1.000; 7: 0.361 / 0.517 / 1.000; 8: 0.322 / 0.367 / 1.000; 9: 0.365 / 0.517 / 1.000; 10: 0.372 / 0.567 / 1.000; 11: 0.350 / 0.550 / 1.000; 12: 0.357 / 0.483 / 1.000; 13: 0.350 / 0.483 / 1.000; 14: 0.355 / 0.483 / 1.000; 15: 0.360 / 0.567 / 1.000
- 6h: 1: 0.356 / 0.503 / 0.889; 2: 0.336 / 0.467 / 0.914; 3: 0.340 / 0.486 / 0.947; 4: 0.350 / 0.514 / 0.950; 5: 0.345 / 0.508 / 0.939; 6: 0.352 / 0.522 / 0.956; 7: 0.339 / 0.497 / 0.975; 8: 0.341 / 0.500 / 0.961; 9: 0.339 / 0.467 / 0.958; 10: 0.346 / 0.497 / 0.964; 11: 0.346 / 0.486 / 0.978; 12: 0.340 / 0.492 / 0.989; 13: 0.339 / 0.481 / 0.981; 14: 0.341 / 0.508 / 0.972; 15: 0.354 / 0.544 / 0.936
- 24h: 1: 0.368 / 0.516 / 0.902; 2: 0.355 / 0.482 / 0.908; 3: 0.359 / 0.500 / 0.915; 4: 0.363 / 0.511 / 0.906; 5: 0.363 / 0.517 / 0.906; 6: 0.358 / 0.491 / 0.906; 7: 0.359 / 0.507 / 0.910; 8: 0.355 / 0.490 / 0.901; 9: 0.357 / 0.490 / 0.898; 10: 0.357 / 0.500 / 0.897; 11: 0.354 / 0.473 / 0.901; 12: 0.356 / 0.497 / 0.901; 13: 0.356 / 0.489 / 0.900; 14: 0.357 / 0.513 / 0.901; 15: 0.359 / 0.506 / 0.903
- 7d: 1: 0.351 / 0.528 / 0.897; 2: 0.341 / 0.501 / 0.900; 3: 0.343 / 0.508 / 0.902; 4: 0.341 / 0.506 / 0.902; 5: 0.338 / 0.499 / 0.902; 6: 0.337 / 0.492 / 0.901; 7: 0.338 / 0.503 / 0.902; 8: 0.336 / 0.489 / 0.902; 9: 0.333 / 0.488 / 0.901; 10: 0.336 / 0.500 / 0.901; 11: 0.336 / 0.499 / 0.901; 12: 0.337 / 0.503 / 0.900; 13: 0.338 / 0.505 / 0.900; 14: 0.336 / 0.499 / 0.900; 15: 0.335 / 0.493 / 0.900
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.500 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.901; 9: 0.346 / 0.497 / 0.900; 10: 0.347 / 0.504 / 0.901; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.496 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.180 (body 0.115, range 0.245); 'price stays where it was' would score 0.212; colour right 0.483; typical miss of the close 8.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.136 (body 0.099, range 0.173); 'price stays where it was' would score 0.140; colour right 0.506; typical miss of the close 6.8 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.132; colour right 0.492; typical miss of the close 9.3 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.115 (body 0.078, range 0.153); 'price stays where it was' would score 0.120; colour right 0.500; typical miss of the close 6.2 bp; chain ended on the right side 0.499 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.1 bp; chain ended on the right side 0.503 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.1; 2: 0.200 / 4.4; 3: 0.167 / 6.1; 4: 0.131 / 6.8; 5: 0.118 / 7.5; 6: 0.110 / 8.1; 7: 0.100 / 8.6; 8: 0.092 / 8.9; 9: 0.085 / 9.2; 10: 0.079 / 10.0; 11: 0.075 / 10.6; 12: 0.074 / 10.9; 13: 0.062 / 11.3; 14: 0.065 / 11.4; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 97020, probability skill vs chance 0.2325, widened contest next: True
  - now: threshold 0.8406, hit rate recent 0.935 / long run 0.937
    - 6h: 19 calls (77 a day), hit rate 0.947, chance 0.308, naive rule 0.543, lift 3.07x
    - 24h: 63 calls (63 a day), hit rate 0.921, chance 0.289, naive rule 0.487, lift 3.19x
    - 7d: 401 calls (57 a day), hit rate 0.928, chance 0.292, naive rule 0.486, lift 3.18x
    - 30d: 1702 calls (57 a day), hit rate 0.941, chance 0.291, naive rule 0.481, lift 3.24x
  - next: threshold 0.5382, hit rate recent 0.5129 / long run 0.5729
    - 6h: 18 calls (73 a day), hit rate 0.444, chance 0.308, lift 1.44x
    - 24h: 80 calls (80 a day), hit rate 0.463, chance 0.289, lift 1.60x
    - 7d: 560 calls (80 a day), hit rate 0.559, chance 0.292, lift 1.92x
    - 30d: 2347 calls (78 a day), hit rate 0.585, chance 0.291, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.493; 0.35: 537, 0.516; 0.40: 486, 0.561; 0.45: 418, 0.628; 0.50: 366, 0.682; 0.55: 321, 0.724; 0.60: 274, 0.768; 0.65: 225, 0.803; 0.70: 181, 0.834; 0.75: 138, 0.873; 0.80: 96, 0.912; 0.85: 49, 0.949; 0.90: 2, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 497, 0.458; 0.40: 413, 0.487; 0.45: 317, 0.518; 0.50: 206, 0.552; 0.55: 92, 0.584; 0.60: 13, 0.600; 0.65: 1, 0.714
- **K=5**: model 1790208000, labels learned 97018, probability skill vs chance 0.2118, widened contest next: True
  - now: threshold 0.7136, hit rate recent 0.7779 / long run 0.8282
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.204, naive rule 0.426, lift 3.37x
    - 24h: 51 calls (51 a day), hit rate 0.765, chance 0.187, naive rule 0.398, lift 4.09x
    - 7d: 389 calls (56 a day), hit rate 0.820, chance 0.189, naive rule 0.394, lift 4.34x
    - 30d: 1575 calls (53 a day), hit rate 0.834, chance 0.186, naive rule 0.390, lift 4.47x
  - next: threshold 0.4383, hit rate recent 0.414 / long run 0.4597
    - 6h: 21 calls (86 a day), hit rate 0.381, chance 0.204, lift 1.87x
    - 24h: 84 calls (84 a day), hit rate 0.393, chance 0.187, lift 2.10x
    - 7d: 636 calls (91 a day), hit rate 0.440, chance 0.189, lift 2.33x
    - 30d: 2109 calls (70 a day), hit rate 0.487, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 429, 0.413; 0.35: 366, 0.468; 0.40: 296, 0.538; 0.45: 242, 0.598; 0.50: 187, 0.656; 0.55: 141, 0.702; 0.60: 110, 0.745; 0.65: 84, 0.791; 0.70: 62, 0.823; 0.75: 34, 0.863; 0.80: 9, 0.886
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.386; 0.35: 253, 0.424; 0.40: 166, 0.449; 0.45: 84, 0.473; 0.50: 20, 0.511; 0.55: 2, 0.554
- **K=8**: model 1791417600, labels learned 97015, probability skill vs chance 0.2018, widened contest next: True
  - now: threshold 0.5785, hit rate recent 0.6157 / long run 0.7075
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.133, naive rule 0.380, lift 4.39x
    - 24h: 54 calls (54 a day), hit rate 0.593, chance 0.122, naive rule 0.338, lift 4.87x
    - 7d: 406 calls (58 a day), hit rate 0.704, chance 0.123, naive rule 0.330, lift 5.73x
    - 30d: 1580 calls (53 a day), hit rate 0.720, chance 0.121, naive rule 0.325, lift 5.94x
  - next: threshold 0.364, hit rate recent 0.3601 / long run 0.3887
    - 6h: 23 calls (95 a day), hit rate 0.391, chance 0.133, lift 2.95x
    - 24h: 107 calls (108 a day), hit rate 0.336, chance 0.122, lift 2.77x
    - 7d: 605 calls (87 a day), hit rate 0.388, chance 0.123, lift 3.16x
    - 30d: 2116 calls (71 a day), hit rate 0.401, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 270, 0.403; 0.35: 204, 0.478; 0.40: 156, 0.540; 0.45: 123, 0.586; 0.50: 94, 0.630; 0.55: 67, 0.684; 0.60: 46, 0.727; 0.65: 24, 0.768; 0.70: 9, 0.816; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 185, 0.347; 0.35: 114, 0.386; 0.40: 48, 0.410; 0.45: 10, 0.425; 0.50: 1, 0.415
- **K=13**: model 1791504000, labels learned 97010, probability skill vs chance 0.1809, widened contest next: False
  - now: threshold 0.4274, hit rate recent 0.579 / long run 0.5827
    - 6h: 15 calls (63 a day), hit rate 0.600, chance 0.067, naive rule 0.215, lift 9.00x
    - 24h: 51 calls (52 a day), hit rate 0.608, chance 0.074, naive rule 0.263, lift 8.17x
    - 7d: 393 calls (56 a day), hit rate 0.585, chance 0.077, naive rule 0.269, lift 7.58x
    - 30d: 1483 calls (49 a day), hit rate 0.587, chance 0.077, naive rule 0.267, lift 7.63x
  - next: threshold 0.2741, hit rate recent 0.2984 / long run 0.3058
    - 6h: 20 calls (83 a day), hit rate 0.250, chance 0.067, lift 3.75x
    - 24h: 72 calls (73 a day), hit rate 0.292, chance 0.074, lift 3.92x
    - 7d: 536 calls (77 a day), hit rate 0.312, chance 0.077, lift 4.04x
    - 30d: 2044 calls (68 a day), hit rate 0.308, chance 0.077, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.440; 0.35: 88, 0.501; 0.40: 62, 0.551; 0.45: 43, 0.609; 0.50: 27, 0.632; 0.55: 15, 0.682; 0.60: 6, 0.709; 0.65: 1, 0.775
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.317; 0.35: 16, 0.342; 0.40: 3, 0.348; 0.45: 1, 0.294

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.556 | 0.50% | 0.950 | 0.533 | 0.250 | 0.533 | 0.090 |
| 6h | 13.444 | 4.12% | 0.894 | 0.497 | 0.250 | 0.506 | 0.457 |
| 24h | 17.039 | 7.06% | 0.907 | 0.498 | 0.250 | 0.517 | 0.724 |
| 7d | 11.157 | 5.44% | 0.900 | 0.499 | 0.251 | 0.498 | 0.680 |
| 30d | 14.299 | 4.42% | 0.900 | 0.500 | 0.251 | 0.497 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.634 | 16.202 | 15.831 | 15.653 | 15.741 | 15.802 | 15.666 | 15.442 | 15.515 | 15.556 |
| 6h | 14.021 | 13.672 | 13.612 | 13.524 | 13.840 | 13.603 | 13.453 | 13.352 | 13.416 | 13.444 |
| 24h | 18.334 | 17.229 | 17.146 | 17.097 | 17.308 | 17.430 | 17.034 | 16.999 | 17.017 | 17.039 |
| 7d | 11.800 | 11.270 | 11.245 | 11.210 | 11.365 | 11.402 | 11.161 | 11.146 | 11.142 | 11.157 |
| 30d | 14.960 | 14.432 | 14.381 | 14.330 | 14.572 | 14.526 | 14.302 | 14.273 | 14.272 | 14.299 |

## Next candle

- candle starting 2026-10-09 13:06 UTC, last close 2498.34
- P(up) 0.4944, return quantiles (bp): {'05': -9.874, '10': -7.277, '25': -3.979, '40': -1.834, '50': -0.086, '60': 1.519, '75': 4.471, '90': 7.366, '95': 10.072}
- changepoint probability 0.07, regime age 63.9 min
- agent weights: empirical 0.003, ewma 0.053, garch 0.079, har 0.144, bocpd 0.019, hmm 0.052, online_qr 0.236, lgbm 0.413

## Learning log

- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- HMM volatility states (sd, bp per minute): [2.34, 4.79, 15.13], current probabilities: [0.001, 0.952, 0.048]
- live generator: {'versions': 60, 'latest_effective': '2026-10-09 13:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.459, 'l_abs': 0.75, 'l_hi': 0.733, 'l_lo': 0.694, 'b05': 0.719, 'b25': 0.679, 'b75': 0.691, 'b95': 0.694}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.205, 1.286, 1.677, 1.805, 2.104, 2.145, 2.252, 2.541, 2.684, 2.878, 3.134, 3.079, 3.015, 3.254]}
- calibration offsets (in sigma): {'05': 0.0325, '10': 0.045, '25': -0.0175, '40': -0.04, '50': 0.005, '60': 0.03, '75': 0.0775, '90': 0.005, '95': -0.0325}
