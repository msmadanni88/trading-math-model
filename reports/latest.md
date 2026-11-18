# ETH-USD 60s candle generator - report

- generated: 2026-11-18 03:39 UTC
- last closed candle: 2026-11-18 03:39 UTC (staleness 0.8 min)
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
| chain_end_side | 0.542 (96) | 0.532 (671) [0.501, 0.559] | 0.519 (2879) [0.502, 0.536] | 0.515 (7385) [0.504, 0.527] | 0.518 (4413) [0.502, 0.532] | 0.500 (14) | 0.500 | flat +0.010 (noise 0.027) |
| colour_clear | 0.521 (796) | 0.536 (5667) [0.528, 0.545] | 0.541 (23987) [0.535, 0.547] | 0.524 (60594) [0.519, 0.529] | 0.542 (36356) [0.538, 0.547] | 0.564 (117) | 0.500 | flat -0.005 (noise 0.012) |
| colour_confident | 0.518 (189) | 0.537 (895) [0.521, 0.556] | 0.579 (4528) [0.566, 0.591] | 0.585 (6578) [0.575, 0.596] | 0.585 (6578) [0.575, 0.596] | 0.692 (26) | 0.500 | flat -0.032 (noise 0.023) |
| colour_next | 0.516 (1436) | 0.528 (10051) [0.520, 0.536] | 0.531 (42898) [0.526, 0.535] | 0.518 (110045) [0.514, 0.521] | 0.530 (65696) [0.526, 0.533] | 0.539 (219) | 0.500 | flat -0.002 (noise 0.009) |
| colour_path | 0.503 (20104) | 0.503 (140714) [0.501, 0.505] | 0.502 (600572) [0.501, 0.503] | 0.501 (1540630) [0.500, 0.502] | 0.501 (919744) [0.500, 0.502] | 0.506 (3066) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.605 (43) | 0.563 (215) [0.532, 0.585] | 0.612 (1188) [0.595, 0.629] | 0.623 (1723) [0.607, 0.638] | 0.623 (1723) [0.607, 0.638] | 0.500 (8) | 0.500 | flat -0.062 (noise 0.045) |
| reversal_k13_next | 0.233 (73) | 0.315 (445) [0.279, 0.358] | 0.329 (1851) [0.312, 0.345] | 0.314 (5069) [0.304, 0.324] | 0.325 (2964) [0.314, 0.336] | 0.214 (14) | 0.077 | flat -0.014 (noise 0.031) |
| reversal_k13_now | 0.467 (60) | 0.576 (351) [0.524, 0.634] | 0.568 (1608) [0.547, 0.590] | 0.574 (3957) [0.561, 0.587] | 0.569 (2485) [0.553, 0.587] | 0.333 (6) | 0.077 | flat +0.003 (noise 0.037) |
| reversal_k3_next | 0.556 (81) | 0.612 (374) [0.578, 0.666] | 0.600 (2463) [0.586, 0.613] | 0.589 (6427) [0.580, 0.597] | 0.590 (3987) [0.580, 0.601] | 0.615 (13) | 0.293 | flat -0.007 (noise 0.036) |
| reversal_k3_now | 0.952 (42) | 0.933 (373) [0.922, 0.945] | 0.932 (1717) [0.922, 0.942] | 0.935 (4398) [0.930, 0.941] | 0.931 (2635) [0.924, 0.938] | 1.000 (6) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.355 (62) | 0.476 (447) [0.425, 0.534] | 0.496 (2328) [0.478, 0.514] | 0.485 (5847) [0.474, 0.497] | 0.481 (3857) [0.467, 0.495] | 0.444 (9) | 0.186 | flat -0.057 (noise 0.036) |
| reversal_k5_now | 0.817 (60) | 0.746 (445) [0.714, 0.776] | 0.796 (1724) [0.779, 0.811] | 0.817 (4181) [0.806, 0.827] | 0.804 (2570) [0.791, 0.817] | 0.714 (7) | 0.187 | flat -0.053 (noise 0.030) |
| reversal_k8_next | 0.365 (85) | 0.408 (471) [0.369, 0.455] | 0.404 (2426) [0.389, 0.421] | 0.397 (5973) [0.386, 0.407] | 0.397 (3867) [0.385, 0.409] | 0.250 (12) | 0.121 | flat -0.015 (noise 0.033) |
| reversal_k8_now | 0.639 (61) | 0.643 (384) [0.608, 0.692] | 0.676 (1573) [0.656, 0.697] | 0.695 (4023) [0.683, 0.708] | 0.683 (2436) [0.667, 0.699] | 0.571 (7) | 0.122 | flat -0.051 (noise 0.035) |
| overall | 0.504 (22160) | 0.506 (154726) [0.505, 0.508] | 0.506 (662039) [0.504, 0.507] | 0.504 (1697935) [0.503, 0.505] | 0.505 (1014654) [0.504, 0.506] | 0.508 (3373) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06656, 0.09611] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5283, 'levels': [{'threshold': 0.06656, 'calls_per_day': 145.0, 'win_rate': 0.5383}, {'threshold': 0.09611, 'calls_per_day': 36.0, 'win_rate': 0.5692}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42898, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14954 | 0.348 | 0.532 (14737) | 0.567 (2280) | 0.744 (2500) |
| volatility: normal | 14952 | 0.373 | 0.530 (14895) | 0.599 (1353) | 0.731 (2282) |
| volatility: wild | 14953 | 0.389 | 0.529 (14915) | 0.580 (1060) | 0.764 (2075) |
| session: Asia 00-08 | 15099 | 0.369 | 0.534 (14983) | 0.579 (1647) | 0.746 (2234) |
| session: Europe 08-13 | 9300 | 0.363 | 0.530 (9224) | 0.585 (1141) | 0.747 (1499) |
| session: US 13-21 | 14880 | 0.378 | 0.533 (14792) | 0.597 (1290) | 0.748 (2281) |
| session: late 21-24 | 5580 | 0.365 | 0.516 (5548) | 0.532 (615) | 0.740 (843) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.374 | 0.360 | 0.301 | 0.301 | 0.533 | 0.249 | 0.499 | 1.620 |
| 6h | 360 | 0.376 | 0.372 | 0.300 | 0.339 | 0.540 | 0.257 | 0.495 | 1.364 |
| 24h | 1440 | 0.379 | 0.369 | 0.305 | 0.340 | 0.523 | 0.265 | 0.493 | 1.178 |
| 7d | 10080 | 0.383 | 0.377 | 0.300 | 0.332 | 0.529 | 0.271 | 0.496 | 1.168 |
| 30d | 43200 | 0.370 | 0.364 | 0.283 | 0.314 | 0.531 | 0.266 | 0.475 | 1.251 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.374 / 0.533 / 0.933; 2: 0.377 / 0.467 / 1.000; 3: 0.352 / 0.467 / 1.000; 4: 0.371 / 0.550 / 1.000; 5: 0.343 / 0.450 / 0.983; 6: 0.390 / 0.567 / 1.000; 7: 0.377 / 0.533 / 0.983; 8: 0.407 / 0.617 / 0.950; 9: 0.387 / 0.567 / 0.983; 10: 0.366 / 0.483 / 1.000; 11: 0.378 / 0.517 / 1.000; 12: 0.372 / 0.467 / 1.000; 13: 0.370 / 0.500 / 0.950; 14: 0.345 / 0.400 / 0.883; 15: 0.376 / 0.483 / 1.000
- 6h: 1: 0.376 / 0.540 / 0.908; 2: 0.367 / 0.485 / 0.967; 3: 0.360 / 0.487 / 0.983; 4: 0.358 / 0.476 / 0.978; 5: 0.361 / 0.499 / 0.972; 6: 0.360 / 0.476 / 0.983; 7: 0.386 / 0.582 / 0.961; 8: 0.368 / 0.513 / 0.958; 9: 0.367 / 0.515 / 0.967; 10: 0.361 / 0.482 / 0.981; 11: 0.364 / 0.493 / 0.986; 12: 0.367 / 0.493 / 0.978; 13: 0.372 / 0.543 / 0.928; 14: 0.362 / 0.504 / 0.917; 15: 0.359 / 0.496 / 0.981
- 24h: 1: 0.379 / 0.523 / 0.899; 2: 0.369 / 0.493 / 0.920; 3: 0.372 / 0.518 / 0.909; 4: 0.367 / 0.493 / 0.922; 5: 0.373 / 0.525 / 0.934; 6: 0.366 / 0.502 / 0.908; 7: 0.377 / 0.532 / 0.921; 8: 0.368 / 0.502 / 0.926; 9: 0.361 / 0.487 / 0.919; 10: 0.367 / 0.503 / 0.921; 11: 0.366 / 0.507 / 0.922; 12: 0.369 / 0.511 / 0.924; 13: 0.368 / 0.505 / 0.922; 14: 0.366 / 0.505 / 0.917; 15: 0.363 / 0.493 / 0.908
- 7d: 1: 0.383 / 0.529 / 0.898; 2: 0.368 / 0.488 / 0.900; 3: 0.377 / 0.516 / 0.899; 4: 0.369 / 0.495 / 0.900; 5: 0.371 / 0.501 / 0.901; 6: 0.370 / 0.506 / 0.899; 7: 0.372 / 0.509 / 0.901; 8: 0.372 / 0.509 / 0.901; 9: 0.365 / 0.491 / 0.902; 10: 0.370 / 0.503 / 0.900; 11: 0.371 / 0.511 / 0.901; 12: 0.368 / 0.501 / 0.902; 13: 0.369 / 0.507 / 0.901; 14: 0.368 / 0.501 / 0.901; 15: 0.368 / 0.501 / 0.901
- 30d: 1: 0.370 / 0.531 / 0.897; 2: 0.358 / 0.493 / 0.900; 3: 0.361 / 0.512 / 0.900; 4: 0.357 / 0.497 / 0.900; 5: 0.358 / 0.504 / 0.900; 6: 0.355 / 0.501 / 0.900; 7: 0.356 / 0.500 / 0.900; 8: 0.357 / 0.506 / 0.900; 9: 0.355 / 0.501 / 0.900; 10: 0.356 / 0.503 / 0.900; 11: 0.355 / 0.504 / 0.900; 12: 0.355 / 0.503 / 0.900; 13: 0.354 / 0.499 / 0.900; 14: 0.354 / 0.501 / 0.900; 15: 0.354 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.031 (body 0.017, range 0.045); 'price stays where it was' would score 0.040; colour right 0.500; typical miss of the close 19.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.108 (body 0.067, range 0.149); 'price stays where it was' would score 0.118; colour right 0.507; typical miss of the close 14.9 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.118 (body 0.077, range 0.159); 'price stays where it was' would score 0.122; colour right 0.500; typical miss of the close 15.1 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.127 (body 0.084, range 0.171); 'price stays where it was' would score 0.130; colour right 0.506; typical miss of the close 14.0 bp; chain ended on the right side 0.529 of 671 chains; n=10080
- 30d: match 0.125 (body 0.084, range 0.166); 'price stays where it was' would score 0.128; colour right 0.502; typical miss of the close 9.8 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 5.1; 2: 0.204 / 5.9; 3: 0.167 / 7.7; 4: 0.133 / 8.1; 5: 0.125 / 8.7; 6: 0.118 / 9.6; 7: 0.110 / 10.1; 8: 0.099 / 11.0; 9: 0.092 / 11.3; 10: 0.090 / 11.6; 11: 0.085 / 12.0; 12: 0.078 / 12.4; 13: 0.073 / 12.9; 14: 0.067 / 13.4; 15: 0.067 / 13.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 154053, probability skill vs chance 0.2309, widened contest next: True
  - now: threshold 0.8332, hit rate recent 0.9494 / long run 0.9308
    - 6h: 8 calls (32 a day), hit rate 1.000, chance 0.283, naive rule 0.500, lift 3.53x
    - 24h: 42 calls (42 a day), hit rate 0.952, chance 0.276, naive rule 0.479, lift 3.46x
    - 7d: 366 calls (52 a day), hit rate 0.934, chance 0.288, naive rule 0.500, lift 3.25x
    - 30d: 1715 calls (57 a day), hit rate 0.932, chance 0.293, naive rule 0.499, lift 3.18x
  - next: threshold 0.5559, hit rate recent 0.5541 / long run 0.6041
    - 6h: 15 calls (61 a day), hit rate 0.600, chance 0.283, lift 2.12x
    - 24h: 80 calls (80 a day), hit rate 0.550, chance 0.276, lift 2.00x
    - 7d: 379 calls (54 a day), hit rate 0.612, chance 0.288, lift 2.13x
    - 30d: 2458 calls (82 a day), hit rate 0.599, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.500; 0.35: 530, 0.526; 0.40: 475, 0.577; 0.45: 408, 0.646; 0.50: 359, 0.691; 0.55: 311, 0.736; 0.60: 261, 0.781; 0.65: 221, 0.810; 0.70: 172, 0.841; 0.75: 138, 0.873; 0.80: 91, 0.905; 0.85: 45, 0.941; 0.90: 4, 0.969
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.433; 0.35: 492, 0.466; 0.40: 391, 0.506; 0.45: 293, 0.542; 0.50: 186, 0.573; 0.55: 81, 0.584; 0.60: 11, 0.642; 0.65: 1, 0.579
- **K=5**: model 1794528000, labels learned 154051, probability skill vs chance 0.2202, widened contest next: True
  - now: threshold 0.6987, hit rate recent 0.7967 / long run 0.7791
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.191, naive rule 0.418, lift 4.28x
    - 24h: 57 calls (57 a day), hit rate 0.825, chance 0.188, naive rule 0.423, lift 4.39x
    - 7d: 436 calls (62 a day), hit rate 0.752, chance 0.185, naive rule 0.413, lift 4.08x
    - 30d: 1724 calls (57 a day), hit rate 0.795, chance 0.186, naive rule 0.408, lift 4.28x
  - next: threshold 0.4577, hit rate recent 0.4084 / long run 0.4949
    - 6h: 11 calls (45 a day), hit rate 0.364, chance 0.191, lift 1.90x
    - 24h: 59 calls (59 a day), hit rate 0.373, chance 0.188, lift 1.99x
    - 7d: 446 calls (64 a day), hit rate 0.480, chance 0.185, lift 2.60x
    - 30d: 2322 calls (77 a day), hit rate 0.496, chance 0.186, lift 2.67x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.419; 0.35: 359, 0.474; 0.40: 291, 0.543; 0.45: 236, 0.602; 0.50: 188, 0.651; 0.55: 150, 0.686; 0.60: 114, 0.735; 0.65: 78, 0.771; 0.70: 48, 0.806; 0.75: 27, 0.837; 0.80: 8, 0.868
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.387; 0.35: 253, 0.426; 0.40: 161, 0.458; 0.45: 65, 0.503; 0.50: 9, 0.547; 0.55: 1, 0.391
- **K=8**: model 1794960000, labels learned 154048, probability skill vs chance 0.1982, widened contest next: True
  - now: threshold 0.5696, hit rate recent 0.6306 / long run 0.6687
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.124, naive rule 0.354, lift 4.69x
    - 24h: 61 calls (61 a day), hit rate 0.639, chance 0.121, naive rule 0.342, lift 5.30x
    - 7d: 377 calls (54 a day), hit rate 0.645, chance 0.123, naive rule 0.352, lift 5.22x
    - 30d: 1575 calls (53 a day), hit rate 0.676, chance 0.121, naive rule 0.340, lift 5.57x
  - next: threshold 0.3694, hit rate recent 0.3521 / long run 0.4061
    - 6h: 18 calls (74 a day), hit rate 0.278, chance 0.124, lift 2.23x
    - 24h: 84 calls (85 a day), hit rate 0.357, chance 0.121, lift 2.96x
    - 7d: 470 calls (67 a day), hit rate 0.404, chance 0.123, lift 3.28x
    - 30d: 2423 calls (81 a day), hit rate 0.403, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 251, 0.426; 0.35: 196, 0.488; 0.40: 155, 0.533; 0.45: 119, 0.577; 0.50: 84, 0.633; 0.55: 59, 0.666; 0.60: 40, 0.708; 0.65: 23, 0.768; 0.70: 10, 0.812; 0.75: 2, 0.776
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 164, 0.369; 0.35: 84, 0.396; 0.40: 24, 0.430; 0.45: 5, 0.447; 0.50: 1, 0.739
- **K=13**: model 1794960000, labels learned 154043, probability skill vs chance 0.1655, widened contest next: True
  - now: threshold 0.4445, hit rate recent 0.5078 / long run 0.5703
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.074, naive rule 0.297, lift 5.64x
    - 24h: 59 calls (60 a day), hit rate 0.458, chance 0.072, naive rule 0.262, lift 6.39x
    - 7d: 345 calls (49 a day), hit rate 0.577, chance 0.078, naive rule 0.300, lift 7.35x
    - 30d: 1607 calls (54 a day), hit rate 0.567, chance 0.078, naive rule 0.287, lift 7.28x
  - next: threshold 0.2896, hit rate recent 0.2647 / long run 0.3188
    - 6h: 18 calls (75 a day), hit rate 0.222, chance 0.074, lift 3.01x
    - 24h: 77 calls (78 a day), hit rate 0.260, chance 0.072, lift 3.63x
    - 7d: 444 calls (64 a day), hit rate 0.309, chance 0.078, lift 3.93x
    - 30d: 1857 calls (62 a day), hit rate 0.327, chance 0.078, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 137, 0.427; 0.35: 99, 0.473; 0.40: 68, 0.532; 0.45: 47, 0.584; 0.50: 32, 0.625; 0.55: 20, 0.651; 0.60: 11, 0.692; 0.65: 3, 0.635; 0.70: 0, 0.286
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.334; 0.35: 13, 0.350; 0.40: 2, 0.420; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 17.553 | 1.32% | 0.933 | 0.550 | 0.252 | 0.467 | 0.313 |
| 6h | 18.676 | 1.60% | 0.919 | 0.517 | 0.251 | 0.532 | 0.322 |
| 24h | 22.640 | 3.27% | 0.904 | 0.507 | 0.251 | 0.487 | 0.607 |
| 7d | 23.719 | 4.22% | 0.900 | 0.501 | 0.250 | 0.508 | 0.674 |
| 30d | 17.513 | 4.65% | 0.900 | 0.500 | 0.250 | 0.505 | 0.711 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.788 | 17.592 | 17.610 | 17.539 | 17.905 | 17.752 | 17.474 | 17.468 | 17.503 | 17.553 |
| 6h | 18.980 | 18.814 | 18.756 | 18.654 | 19.014 | 18.771 | 18.650 | 18.619 | 18.628 | 18.676 |
| 24h | 23.407 | 22.735 | 22.699 | 22.621 | 22.986 | 22.868 | 22.595 | 22.570 | 22.583 | 22.640 |
| 7d | 24.763 | 23.913 | 23.872 | 23.748 | 24.222 | 24.026 | 23.707 | 23.672 | 23.681 | 23.719 |
| 30d | 18.367 | 17.671 | 17.630 | 17.566 | 17.861 | 17.801 | 17.495 | 17.474 | 17.481 | 17.513 |

## Next candle

- candle starting 2026-11-18 03:39 UTC, last close 1806.43
- P(up) 0.4901, return quantiles (bp): {'05': -8.979, '10': -7.112, '25': -3.069, '40': -1.344, '50': -0.124, '60': 1.149, '75': 3.302, '90': 6.821, '95': 8.994}
- changepoint probability 0.0526, regime age 62.9 min
- agent weights: empirical 0.009, ewma 0.099, garch 0.130, har 0.187, bocpd 0.035, hmm 0.068, online_qr 0.220, lgbm 0.253

## Learning log

- 2026-11-16 00:00 UTC: {"garch": {"alpha": 0.0649, "beta": 0.9281}, "hmm": {"sd_bp": [5.12, 9.52, 24.14], "stay": [0.982, 0.963, 0.92]}, "lgbm": {"challenger_loss": 0.24944, "champion_loss": 0.2494, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47719, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47655, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3653, "challengers": 1, "chance_loss": 0.4822, "widened": false, "champion_loss": 0.36306, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2714, "challengers": 1, "chance_loss": 0.37579, "widened": false, "champion_loss": 0.27207, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19602, "challengers": 1, "chance_loss": 0.28273, "widened": false, "champion_loss": 0.19594, "promoted": false}}
- 2026-11-16 12:00 UTC: {"garch": {"alpha": 0.0677, "beta": 0.9218}, "hmm": {"sd_bp": [5.34, 9.7, 24.34], "stay": [0.978, 0.963, 0.917]}}
- 2026-11-17 00:00 UTC: {"garch": {"alpha": 0.054, "beta": 0.9382}, "hmm": {"sd_bp": [5.66, 9.83, 24.07], "stay": [0.978, 0.962, 0.923]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24949, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47935, "challengers": 3, "chance_loss": 0.60685, "widened": true, "champion_loss": 0.48028, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37063, "challengers": 3, "chance_loss": 0.48182, "widened": true, "champion_loss": 0.36993, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27709, "challengers": 3, "chance_loss": 0.36722, "widened": true, "champion_loss": 0.2774, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20238, "challengers": 3, "chance_loss": 0.27203, "widened": true, "champion_loss": 0.20242, "promoted": true}}
- 2026-11-17 12:00 UTC: {"garch": {"alpha": 0.0538, "beta": 0.9373}, "hmm": {"sd_bp": [5.63, 9.77, 23.96], "stay": [0.974, 0.957, 0.927]}}
- 2026-11-18 00:00 UTC: {"garch": {"alpha": 0.0549, "beta": 0.9354}, "hmm": {"sd_bp": [5.68, 10.09, 24.73], "stay": [0.967, 0.954, 0.925]}, "lgbm": {"challenger_loss": 0.25592, "champion_loss": 0.25593, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4696, "challengers": 3, "chance_loss": 0.59688, "widened": true, "champion_loss": 0.47016, "promoted": true}, "reversal_k5": {"challenger_loss": 0.36288, "challengers": 3, "chance_loss": 0.47529, "widened": true, "champion_loss": 0.3627, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27789, "challengers": 3, "chance_loss": 0.37099, "widened": true, "champion_loss": 0.27841, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20128, "challengers": 3, "chance_loss": 0.2669, "widened": true, "champion_loss": 0.20138, "promoted": true}}
- HMM volatility states (sd, bp per minute): [5.68, 10.09, 24.73], current probabilities: [0.94, 0.059, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-11-18 03:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.274, 'l_abs': 0.738, 'l_hi': 0.821, 'l_lo': 0.729, 'b05': 0.719, 'b25': 0.753, 'b75': 0.726, 'b95': 0.709}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.406, 2.193, 2.206, 1.944, 3.247, 2.264, 2.524, 2.629, 3.392, 3.225, 2.934, 3.0, 3.182, 3.235]}
- calibration offsets (in sigma): {'05': 0.029, '10': -0.022, '25': 0.055, '40': 0.002, '50': -0.01, '60': -0.012, '75': -0.025, '90': -0.018, '95': -0.029}
