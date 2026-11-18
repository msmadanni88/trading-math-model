# ETH-USD 60s candle generator - report

- generated: 2026-11-18 20:42 UTC
- last closed candle: 2026-11-18 20:42 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.532 (671) [0.501, 0.559] | 0.519 (2879) [0.502, 0.536] | 0.515 (7385) [0.504, 0.527] | 0.518 (4413) [0.502, 0.532] | 0.549 (82) | 0.500 | flat +0.010 (noise 0.027) |
| colour_clear | 0.521 (796) | 0.536 (5667) [0.528, 0.545] | 0.541 (23987) [0.535, 0.547] | 0.524 (60594) [0.519, 0.529] | 0.542 (36356) [0.538, 0.547] | 0.590 (690) | 0.500 | flat -0.005 (noise 0.012) |
| colour_confident | 0.518 (189) | 0.537 (895) [0.521, 0.556] | 0.579 (4528) [0.566, 0.591] | 0.585 (6578) [0.575, 0.596] | 0.585 (6578) [0.575, 0.596] | 0.641 (145) | 0.500 | flat -0.032 (noise 0.023) |
| colour_next | 0.516 (1436) | 0.528 (10051) [0.520, 0.536] | 0.531 (42898) [0.526, 0.535] | 0.518 (110045) [0.514, 0.521] | 0.530 (65696) [0.526, 0.533] | 0.544 (1236) | 0.500 | flat -0.002 (noise 0.009) |
| colour_path | 0.503 (20104) | 0.503 (140714) [0.501, 0.505] | 0.502 (600572) [0.501, 0.503] | 0.501 (1540630) [0.500, 0.502] | 0.501 (919744) [0.500, 0.502] | 0.509 (17304) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.605 (43) | 0.563 (215) [0.532, 0.585] | 0.612 (1188) [0.595, 0.629] | 0.623 (1723) [0.607, 0.638] | 0.623 (1723) [0.607, 0.638] | 0.696 (46) | 0.500 | flat -0.062 (noise 0.045) |
| reversal_k13_next | 0.233 (73) | 0.315 (445) [0.279, 0.358] | 0.329 (1851) [0.312, 0.345] | 0.314 (5069) [0.304, 0.324] | 0.325 (2964) [0.314, 0.336] | 0.317 (79) | 0.077 | flat -0.014 (noise 0.031) |
| reversal_k13_now | 0.467 (60) | 0.576 (351) [0.524, 0.634] | 0.568 (1608) [0.547, 0.590] | 0.574 (3957) [0.561, 0.587] | 0.569 (2485) [0.553, 0.587] | 0.542 (48) | 0.077 | flat +0.003 (noise 0.037) |
| reversal_k3_next | 0.556 (81) | 0.612 (374) [0.578, 0.666] | 0.600 (2463) [0.586, 0.613] | 0.589 (6427) [0.580, 0.597] | 0.590 (3987) [0.580, 0.601] | 0.621 (58) | 0.293 | flat -0.007 (noise 0.036) |
| reversal_k3_now | 0.952 (42) | 0.933 (373) [0.922, 0.945] | 0.932 (1717) [0.922, 0.942] | 0.935 (4398) [0.930, 0.941] | 0.931 (2635) [0.924, 0.938] | 1.000 (48) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.355 (62) | 0.476 (447) [0.425, 0.534] | 0.496 (2328) [0.478, 0.514] | 0.485 (5847) [0.474, 0.497] | 0.481 (3857) [0.467, 0.495] | 0.420 (50) | 0.186 | flat -0.057 (noise 0.036) |
| reversal_k5_now | 0.817 (60) | 0.746 (445) [0.714, 0.776] | 0.796 (1724) [0.779, 0.811] | 0.817 (4181) [0.806, 0.827] | 0.804 (2570) [0.791, 0.817] | 0.760 (50) | 0.187 | flat -0.053 (noise 0.030) |
| reversal_k8_next | 0.365 (85) | 0.408 (471) [0.369, 0.455] | 0.404 (2426) [0.389, 0.421] | 0.397 (5973) [0.386, 0.407] | 0.397 (3867) [0.385, 0.409] | 0.388 (80) | 0.121 | flat -0.015 (noise 0.033) |
| reversal_k8_now | 0.639 (61) | 0.643 (384) [0.608, 0.692] | 0.676 (1573) [0.656, 0.697] | 0.695 (4023) [0.683, 0.708] | 0.683 (2436) [0.667, 0.699] | 0.702 (57) | 0.122 | flat -0.051 (noise 0.035) |
| overall | 0.504 (22160) | 0.506 (154726) [0.505, 0.508] | 0.506 (662039) [0.504, 0.507] | 0.504 (1697935) [0.503, 0.505] | 0.505 (1014654) [0.504, 0.506] | 0.512 (19092) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0674, 0.09768] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5322, 'levels': [{'threshold': 0.0674, 'calls_per_day': 145.2, 'win_rate': 0.55}, {'threshold': 0.09768, 'calls_per_day': 37.2, 'win_rate': 0.5824}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42895, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15294 | 0.348 | 0.532 (15075) | 0.567 (2321) | 0.746 (2557) |
| volatility: normal | 15294 | 0.374 | 0.530 (15233) | 0.603 (1392) | 0.733 (2354) |
| volatility: wild | 15294 | 0.390 | 0.530 (15256) | 0.578 (1099) | 0.761 (2123) |
| session: Asia 00-08 | 15360 | 0.369 | 0.534 (15242) | 0.579 (1681) | 0.746 (2279) |
| session: Europe 08-13 | 9600 | 0.364 | 0.530 (9521) | 0.589 (1183) | 0.749 (1560) |
| session: US 13-21 | 15342 | 0.379 | 0.533 (15253) | 0.596 (1333) | 0.747 (2352) |
| session: late 21-24 | 5580 | 0.365 | 0.516 (5548) | 0.532 (615) | 0.740 (843) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.416 | 0.421 | 0.367 | 0.367 | 0.533 | 0.288 | 0.545 | 1.053 |
| 6h | 360 | 0.411 | 0.398 | 0.306 | 0.361 | 0.550 | 0.294 | 0.529 | 1.354 |
| 24h | 1440 | 0.392 | 0.381 | 0.303 | 0.348 | 0.544 | 0.278 | 0.506 | 1.150 |
| 7d | 10080 | 0.386 | 0.377 | 0.300 | 0.334 | 0.534 | 0.273 | 0.498 | 1.159 |
| 30d | 43200 | 0.371 | 0.364 | 0.284 | 0.315 | 0.530 | 0.266 | 0.476 | 1.251 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.416 / 0.533 / 0.983; 2: 0.437 / 0.567 / 0.983; 3: 0.415 / 0.533 / 0.933; 4: 0.450 / 0.583 / 0.983; 5: 0.433 / 0.600 / 1.000; 6: 0.422 / 0.467 / 0.883; 7: 0.418 / 0.533 / 1.000; 8: 0.394 / 0.467 / 1.000; 9: 0.409 / 0.483 / 1.000; 10: 0.423 / 0.500 / 1.000; 11: 0.425 / 0.550 / 1.000; 12: 0.419 / 0.467 / 1.000; 13: 0.441 / 0.583 / 1.000; 14: 0.426 / 0.517 / 1.000; 15: 0.409 / 0.483 / 1.000
- 6h: 1: 0.411 / 0.550 / 0.936; 2: 0.402 / 0.528 / 0.944; 3: 0.389 / 0.500 / 0.897; 4: 0.391 / 0.514 / 0.936; 5: 0.398 / 0.544 / 0.989; 6: 0.371 / 0.456 / 0.839; 7: 0.396 / 0.544 / 0.997; 8: 0.395 / 0.542 / 0.997; 9: 0.394 / 0.528 / 0.994; 10: 0.375 / 0.489 / 0.928; 11: 0.389 / 0.517 / 0.978; 12: 0.397 / 0.542 / 0.994; 13: 0.396 / 0.539 / 0.992; 14: 0.384 / 0.514 / 0.986; 15: 0.376 / 0.494 / 0.978
- 24h: 1: 0.392 / 0.544 / 0.905; 2: 0.380 / 0.488 / 0.915; 3: 0.377 / 0.523 / 0.919; 4: 0.376 / 0.494 / 0.921; 5: 0.376 / 0.517 / 0.909; 6: 0.371 / 0.484 / 0.909; 7: 0.378 / 0.525 / 0.900; 8: 0.382 / 0.530 / 0.908; 9: 0.375 / 0.500 / 0.904; 10: 0.372 / 0.504 / 0.915; 11: 0.375 / 0.500 / 0.918; 12: 0.382 / 0.524 / 0.903; 13: 0.376 / 0.516 / 0.895; 14: 0.374 / 0.512 / 0.893; 15: 0.364 / 0.487 / 0.913
- 7d: 1: 0.386 / 0.534 / 0.899; 2: 0.370 / 0.487 / 0.900; 3: 0.378 / 0.518 / 0.899; 4: 0.370 / 0.494 / 0.900; 5: 0.372 / 0.502 / 0.900; 6: 0.371 / 0.504 / 0.898; 7: 0.373 / 0.509 / 0.900; 8: 0.373 / 0.512 / 0.900; 9: 0.366 / 0.489 / 0.899; 10: 0.371 / 0.506 / 0.899; 11: 0.370 / 0.507 / 0.900; 12: 0.371 / 0.508 / 0.898; 13: 0.369 / 0.503 / 0.899; 14: 0.369 / 0.503 / 0.899; 15: 0.367 / 0.499 / 0.899
- 30d: 1: 0.371 / 0.530 / 0.897; 2: 0.358 / 0.493 / 0.900; 3: 0.362 / 0.513 / 0.900; 4: 0.357 / 0.497 / 0.900; 5: 0.358 / 0.505 / 0.900; 6: 0.356 / 0.501 / 0.900; 7: 0.357 / 0.501 / 0.900; 8: 0.357 / 0.507 / 0.900; 9: 0.356 / 0.501 / 0.900; 10: 0.356 / 0.503 / 0.900; 11: 0.356 / 0.504 / 0.900; 12: 0.355 / 0.503 / 0.900; 13: 0.354 / 0.500 / 0.900; 14: 0.354 / 0.501 / 0.900; 15: 0.354 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.208 (body 0.122, range 0.295); 'price stays where it was' would score 0.179; colour right 0.650; typical miss of the close 8.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.158 (body 0.107, range 0.210); 'price stays where it was' would score 0.152; colour right 0.558; typical miss of the close 16.6 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.133 (body 0.088, range 0.178); 'price stays where it was' would score 0.127; colour right 0.519; typical miss of the close 12.6 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.128 (body 0.084, range 0.171); 'price stays where it was' would score 0.130; colour right 0.507; typical miss of the close 14.3 bp; chain ended on the right side 0.526 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.128; colour right 0.503; typical miss of the close 9.8 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.1; 2: 0.204 / 6.0; 3: 0.166 / 7.7; 4: 0.135 / 8.1; 5: 0.125 / 8.8; 6: 0.119 / 9.6; 7: 0.111 / 10.1; 8: 0.099 / 11.0; 9: 0.092 / 11.3; 10: 0.090 / 11.6; 11: 0.085 / 12.1; 12: 0.079 / 12.5; 13: 0.073 / 13.1; 14: 0.068 / 13.5; 15: 0.067 / 13.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 155076, probability skill vs chance 0.2341, widened contest next: False
  - now: threshold 0.8318, hit rate recent 0.975 / long run 0.9355
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.297, naive rule 0.526, lift 3.36x
    - 24h: 53 calls (53 a day), hit rate 1.000, chance 0.295, naive rule 0.516, lift 3.39x
    - 7d: 374 calls (53 a day), hit rate 0.941, chance 0.290, naive rule 0.500, lift 3.25x
    - 30d: 1723 calls (57 a day), hit rate 0.934, chance 0.294, naive rule 0.500, lift 3.18x
  - next: threshold 0.5628, hit rate recent 0.5905 / long run 0.6054
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.297, lift 2.07x
    - 24h: 62 calls (62 a day), hit rate 0.613, chance 0.295, lift 2.08x
    - 7d: 395 calls (56 a day), hit rate 0.608, chance 0.290, lift 2.10x
    - 30d: 2418 calls (81 a day), hit rate 0.604, chance 0.294, lift 2.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.502; 0.35: 530, 0.527; 0.40: 476, 0.578; 0.45: 409, 0.646; 0.50: 360, 0.691; 0.55: 312, 0.736; 0.60: 262, 0.782; 0.65: 222, 0.810; 0.70: 173, 0.842; 0.75: 139, 0.873; 0.80: 92, 0.906; 0.85: 45, 0.942; 0.90: 4, 0.968
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.434; 0.35: 492, 0.467; 0.40: 390, 0.508; 0.45: 293, 0.544; 0.50: 187, 0.575; 0.55: 81, 0.587; 0.60: 11, 0.648; 0.65: 1, 0.556
- **K=5**: model 1794528000, labels learned 155074, probability skill vs chance 0.2074, widened contest next: True
  - now: threshold 0.698, hit rate recent 0.7785 / long run 0.7782
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.178, naive rule 0.395, lift 4.48x
    - 24h: 59 calls (59 a day), hit rate 0.797, chance 0.189, naive rule 0.401, lift 4.22x
    - 7d: 438 calls (63 a day), hit rate 0.751, chance 0.185, naive rule 0.407, lift 4.07x
    - 30d: 1729 calls (58 a day), hit rate 0.794, chance 0.186, naive rule 0.409, lift 4.26x
  - next: threshold 0.4625, hit rate recent 0.408 / long run 0.4895
    - 6h: 11 calls (45 a day), hit rate 0.455, chance 0.178, lift 2.55x
    - 24h: 52 calls (52 a day), hit rate 0.404, chance 0.189, lift 2.14x
    - 7d: 451 calls (64 a day), hit rate 0.472, chance 0.185, lift 2.56x
    - 30d: 2246 calls (75 a day), hit rate 0.498, chance 0.186, lift 2.68x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.420; 0.35: 360, 0.474; 0.40: 291, 0.543; 0.45: 236, 0.601; 0.50: 187, 0.651; 0.55: 150, 0.686; 0.60: 113, 0.734; 0.65: 79, 0.770; 0.70: 49, 0.804; 0.75: 27, 0.839; 0.80: 8, 0.868
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.387; 0.35: 253, 0.427; 0.40: 161, 0.458; 0.45: 64, 0.502; 0.50: 9, 0.554; 0.55: 1, 0.476
- **K=8**: model 1794960000, labels learned 155071, probability skill vs chance 0.1965, widened contest next: False
  - now: threshold 0.5705, hit rate recent 0.6811 / long run 0.6728
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.129, naive rule 0.331, lift 5.56x
    - 24h: 67 calls (67 a day), hit rate 0.716, chance 0.124, naive rule 0.335, lift 5.79x
    - 7d: 397 calls (57 a day), hit rate 0.645, chance 0.122, naive rule 0.343, lift 5.27x
    - 30d: 1592 calls (53 a day), hit rate 0.680, chance 0.121, naive rule 0.340, lift 5.60x
  - next: threshold 0.3662, hit rate recent 0.3881 / long run 0.4066
    - 6h: 26 calls (107 a day), hit rate 0.423, chance 0.129, lift 3.29x
    - 24h: 87 calls (88 a day), hit rate 0.391, chance 0.124, lift 3.16x
    - 7d: 492 calls (70 a day), hit rate 0.396, chance 0.122, lift 3.24x
    - 30d: 2402 calls (80 a day), hit rate 0.407, chance 0.121, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.426; 0.35: 196, 0.487; 0.40: 155, 0.533; 0.45: 119, 0.578; 0.50: 84, 0.635; 0.55: 60, 0.671; 0.60: 40, 0.709; 0.65: 23, 0.770; 0.70: 10, 0.814; 0.75: 2, 0.759
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 163, 0.369; 0.35: 84, 0.399; 0.40: 25, 0.436; 0.45: 5, 0.461; 0.50: 1, 0.731
- **K=13**: model 1794960000, labels learned 155066, probability skill vs chance 0.1747, widened contest next: True
  - now: threshold 0.4456, hit rate recent 0.532 / long run 0.5703
    - 6h: 13 calls (54 a day), hit rate 0.462, chance 0.078, naive rule 0.272, lift 5.90x
    - 24h: 58 calls (59 a day), hit rate 0.552, chance 0.084, naive rule 0.305, lift 6.55x
    - 7d: 357 calls (51 a day), hit rate 0.566, chance 0.079, naive rule 0.295, lift 7.20x
    - 30d: 1614 calls (54 a day), hit rate 0.569, chance 0.078, naive rule 0.288, lift 7.30x
  - next: threshold 0.2899, hit rate recent 0.2934 / long run 0.3206
    - 6h: 24 calls (100 a day), hit rate 0.208, chance 0.078, lift 2.66x
    - 24h: 86 calls (87 a day), hit rate 0.326, chance 0.084, lift 3.87x
    - 7d: 464 calls (66 a day), hit rate 0.308, chance 0.079, lift 3.92x
    - 30d: 1856 calls (62 a day), hit rate 0.329, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 137, 0.426; 0.35: 100, 0.473; 0.40: 69, 0.533; 0.45: 47, 0.584; 0.50: 33, 0.626; 0.55: 21, 0.647; 0.60: 11, 0.692; 0.65: 3, 0.626; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.336; 0.35: 14, 0.350; 0.40: 2, 0.414; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.676 | 0.97% | 0.983 | 0.450 | 0.249 | 0.567 | 0.165 |
| 6h | 29.135 | 4.36% | 0.928 | 0.522 | 0.250 | 0.525 | 0.575 |
| 24h | 20.481 | 3.80% | 0.909 | 0.500 | 0.250 | 0.506 | 0.637 |
| 7d | 24.066 | 4.32% | 0.900 | 0.500 | 0.250 | 0.504 | 0.674 |
| 30d | 17.628 | 4.69% | 0.900 | 0.500 | 0.250 | 0.504 | 0.711 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 16.838 | 16.727 | 16.679 | 17.126 | 16.798 | 16.777 | 16.719 | 16.707 | 16.727 | 16.676 |
| 6h | 30.464 | 29.446 | 29.248 | 29.307 | 30.096 | 29.370 | 28.977 | 28.971 | 29.074 | 29.135 |
| 24h | 21.290 | 20.692 | 20.618 | 20.521 | 20.861 | 20.642 | 20.413 | 20.391 | 20.441 | 20.481 |
| 7d | 25.152 | 24.256 | 24.213 | 24.087 | 24.566 | 24.373 | 24.046 | 24.019 | 24.027 | 24.066 |
| 30d | 18.496 | 17.788 | 17.745 | 17.682 | 17.977 | 17.914 | 17.609 | 17.587 | 17.596 | 17.628 |

## Next candle

- candle starting 2026-11-18 20:42 UTC, last close 1747.92
- P(up) 0.4935, return quantiles (bp): {'05': -9.805, '10': -7.649, '25': -3.914, '40': -2.033, '50': -0.07, '60': 1.22, '75': 3.59, '90': 7.027, '95': 9.534}
- changepoint probability 0.0548, regime age 87.9 min
- agent weights: empirical 0.003, ewma 0.043, garch 0.087, har 0.111, bocpd 0.016, hmm 0.091, online_qr 0.316, lgbm 0.332

## Learning log

- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- 2026-11-18 12:00 UTC: {"garch": {"alpha": 0.0494, "beta": 0.944}, "hmm": {"sd_bp": [5.62, 10.24, 24.94], "stay": [0.973, 0.954, 0.932]}}
- HMM volatility states (sd, bp per minute): [5.62, 10.24, 24.94], current probabilities: [0.955, 0.044, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-11-18 20:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.299, 'l_abs': 0.716, 'l_hi': 0.811, 'l_lo': 0.729, 'b05': 0.723, 'b25': 0.738, 'b75': 0.671, 'b95': 0.715}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.239, 1.858, 1.795, 2.136, 3.497, 2.86, 2.611, 3.322, 3.305, 3.019, 4.098, 4.36, 4.534, 4.428]}
- calibration offsets (in sigma): {'05': 0.0405, '10': 0.001, '25': -0.0175, '40': -0.096, '50': -0.025, '60': -0.054, '75': -0.0625, '90': -0.101, '95': -0.0805}
