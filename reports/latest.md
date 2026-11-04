# ETH-USD 60s candle generator - report

- generated: 2026-11-04 11:12 UTC
- last closed candle: 2026-11-04 11:12 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.478 in the last 7 days, -0.059 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.396 (96) | 0.478 (672) [0.449, 0.504] | 0.509 (2878) [0.490, 0.528] | 0.512 (6042) [0.499, 0.525] | 0.513 (3070) [0.494, 0.532] | 0.500 (44) | 0.500 | down -0.059 (noise 0.028) |
| colour_clear | 0.518 (819) | 0.534 (5467) [0.525, 0.544] | 0.543 (23791) [0.539, 0.548] | 0.521 (49424) [0.515, 0.527] | 0.544 (25186) [0.539, 0.548] | 0.491 (373) | 0.500 | flat -0.010 (noise 0.009) |
| colour_confident | 0.621 (95) | 0.576 (913) [0.564, 0.593] | 0.596 (4351) [0.584, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.581 (43) | 0.500 | flat -0.028 (noise 0.021) |
| colour_next | 0.526 (1436) | 0.531 (9974) [0.524, 0.537] | 0.529 (42856) [0.526, 0.533] | 0.515 (90026) [0.511, 0.519] | 0.530 (45677) [0.526, 0.533] | 0.507 (669) | 0.500 | flat +0.003 (noise 0.007) |
| colour_path | 0.505 (20104) | 0.502 (139636) [0.500, 0.504] | 0.501 (599984) [0.500, 0.502] | 0.501 (1260364) [0.500, 0.502] | 0.501 (639478) [0.499, 0.502] | 0.503 (9366) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.571 (14) | 0.621 (203) [0.570, 0.671] | 0.631 (1129) [0.610, 0.652] | 0.633 (1244) [0.613, 0.652] | 0.633 (1244) [0.613, 0.652] | 0.667 (9) | 0.500 | flat +0.007 (noise 0.042) |
| reversal_k13_next | 0.409 (66) | 0.352 (358) [0.311, 0.391] | 0.324 (1859) [0.310, 0.339] | 0.313 (4152) [0.303, 0.324] | 0.326 (2047) [0.313, 0.339] | 0.333 (15) | 0.077 | flat +0.031 (noise 0.034) |
| reversal_k13_now | 0.649 (57) | 0.582 (423) [0.544, 0.615] | 0.561 (1673) [0.543, 0.580] | 0.574 (3255) [0.560, 0.588] | 0.568 (1783) [0.547, 0.589] | 0.630 (27) | 0.077 | flat +0.016 (noise 0.036) |
| reversal_k3_next | 0.523 (65) | 0.597 (819) [0.580, 0.614] | 0.586 (2993) [0.575, 0.598] | 0.586 (5701) [0.577, 0.595] | 0.584 (3261) [0.574, 0.596] | 0.632 (19) | 0.293 | flat -0.010 (noise 0.025) |
| reversal_k3_now | 0.904 (52) | 0.925 (428) [0.905, 0.949] | 0.933 (1735) [0.922, 0.944] | 0.937 (3619) [0.931, 0.943] | 0.933 (1856) [0.923, 0.942] | 0.880 (25) | 0.293 | flat -0.029 (noise 0.018) |
| reversal_k5_next | 0.476 (63) | 0.535 (389) [0.511, 0.556] | 0.479 (2709) [0.464, 0.495] | 0.482 (5008) [0.471, 0.494] | 0.474 (3018) [0.460, 0.490] | 0.500 (24) | 0.187 | flat +0.036 (noise 0.031) |
| reversal_k5_now | 0.784 (51) | 0.814 (436) [0.799, 0.827] | 0.816 (1628) [0.806, 0.826] | 0.828 (3368) [0.819, 0.837] | 0.820 (1757) [0.809, 0.830] | 0.875 (24) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.409 (66) | 0.439 (540) [0.414, 0.465] | 0.389 (2787) [0.376, 0.403] | 0.393 (5057) [0.383, 0.404] | 0.391 (2951) [0.378, 0.405] | 0.429 (21) | 0.121 | up +0.057 (noise 0.028) |
| reversal_k8_now | 0.714 (49) | 0.714 (384) [0.676, 0.744] | 0.683 (1585) [0.664, 0.702] | 0.701 (3282) [0.687, 0.716] | 0.690 (1695) [0.669, 0.709] | 0.692 (26) | 0.121 | flat +0.039 (noise 0.036) |
| overall | 0.507 (22105) | 0.506 (154059) [0.504, 0.509] | 0.505 (662687) [0.503, 0.506] | 0.504 (1389874) [0.503, 0.505] | 0.505 (706593) [0.503, 0.506] | 0.506 (10260) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07816, 0.1175] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5291, 'levels': [{'threshold': 0.07816, 'calls_per_day': 142.5, 'win_rate': 0.5754}, {'threshold': 0.1175, 'calls_per_day': 35.2, 'win_rate': 0.6345}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42855, 'rate': 0.5286}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15104 | 0.338 | 0.528 (14847) | 0.576 (2332) | 0.749 (2619) |
| volatility: normal | 15104 | 0.366 | 0.534 (15036) | 0.613 (1497) | 0.748 (2270) |
| volatility: wild | 15104 | 0.381 | 0.526 (15059) | 0.627 (825) | 0.763 (2091) |
| session: Asia 00-08 | 15360 | 0.362 | 0.537 (15249) | 0.602 (1670) | 0.755 (2295) |
| session: Europe 08-13 | 9492 | 0.356 | 0.533 (9391) | 0.596 (1184) | 0.741 (1575) |
| session: US 13-21 | 14880 | 0.369 | 0.526 (14772) | 0.595 (1196) | 0.760 (2275) |
| session: late 21-24 | 5580 | 0.351 | 0.512 (5530) | 0.589 (604) | 0.749 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.350 | 0.420 | 0.283 | 0.283 | 0.433 | 0.220 | 0.480 | 1.186 |
| 6h | 360 | 0.368 | 0.379 | 0.295 | 0.339 | 0.508 | 0.259 | 0.477 | 1.330 |
| 24h | 1440 | 0.366 | 0.368 | 0.274 | 0.308 | 0.516 | 0.254 | 0.478 | 1.287 |
| 7d | 10080 | 0.361 | 0.357 | 0.274 | 0.305 | 0.530 | 0.260 | 0.461 | 1.286 |
| 30d | 43200 | 0.363 | 0.356 | 0.277 | 0.307 | 0.529 | 0.262 | 0.464 | 1.255 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.350 / 0.433 / 0.900; 2: 0.387 / 0.550 / 0.900; 3: 0.397 / 0.600 / 0.917; 4: 0.320 / 0.333 / 0.967; 5: 0.377 / 0.567 / 0.967; 6: 0.387 / 0.600 / 1.000; 7: 0.363 / 0.517 / 0.967; 8: 0.406 / 0.633 / 1.000; 9: 0.366 / 0.550 / 1.000; 10: 0.366 / 0.533 / 1.000; 11: 0.381 / 0.567 / 0.983; 12: 0.377 / 0.617 / 1.000; 13: 0.386 / 0.567 / 0.983; 14: 0.396 / 0.650 / 1.000; 15: 0.348 / 0.400 / 1.000
- 6h: 1: 0.368 / 0.508 / 0.931; 2: 0.365 / 0.489 / 0.928; 3: 0.380 / 0.542 / 0.925; 4: 0.343 / 0.439 / 0.939; 5: 0.354 / 0.478 / 0.931; 6: 0.371 / 0.561 / 0.956; 7: 0.356 / 0.472 / 0.931; 8: 0.356 / 0.511 / 0.953; 9: 0.358 / 0.511 / 0.953; 10: 0.364 / 0.525 / 0.958; 11: 0.364 / 0.536 / 0.944; 12: 0.364 / 0.536 / 0.972; 13: 0.378 / 0.528 / 0.956; 14: 0.372 / 0.561 / 0.961; 15: 0.361 / 0.497 / 0.972
- 24h: 1: 0.366 / 0.516 / 0.908; 2: 0.367 / 0.512 / 0.894; 3: 0.366 / 0.524 / 0.909; 4: 0.357 / 0.483 / 0.907; 5: 0.355 / 0.487 / 0.892; 6: 0.354 / 0.501 / 0.916; 7: 0.356 / 0.489 / 0.892; 8: 0.349 / 0.479 / 0.899; 9: 0.359 / 0.520 / 0.898; 10: 0.354 / 0.492 / 0.898; 11: 0.356 / 0.505 / 0.892; 12: 0.359 / 0.517 / 0.903; 13: 0.359 / 0.493 / 0.895; 14: 0.360 / 0.515 / 0.899; 15: 0.359 / 0.502 / 0.901
- 7d: 1: 0.361 / 0.530 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.351 / 0.510 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.349 / 0.511 / 0.899; 6: 0.346 / 0.505 / 0.900; 7: 0.348 / 0.499 / 0.900; 8: 0.345 / 0.505 / 0.901; 9: 0.347 / 0.505 / 0.901; 10: 0.345 / 0.495 / 0.901; 11: 0.346 / 0.501 / 0.901; 12: 0.345 / 0.497 / 0.901; 13: 0.347 / 0.503 / 0.902; 14: 0.345 / 0.499 / 0.902; 15: 0.347 / 0.507 / 0.903
- 30d: 1: 0.363 / 0.529 / 0.899; 2: 0.352 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.349 / 0.499 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.348 / 0.500 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.346 / 0.497 / 0.900; 12: 0.348 / 0.501 / 0.900; 13: 0.348 / 0.501 / 0.900; 14: 0.347 / 0.500 / 0.900; 15: 0.348 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.198 (body 0.133, range 0.263); 'price stays where it was' would score 0.191; colour right 0.483; typical miss of the close 5.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.139 (body 0.103, range 0.175); 'price stays where it was' would score 0.138; colour right 0.506; typical miss of the close 9.9 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.121 (body 0.080, range 0.162); 'price stays where it was' would score 0.121; colour right 0.496; typical miss of the close 10.9 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.123 (body 0.084, range 0.161); 'price stays where it was' would score 0.124; colour right 0.503; typical miss of the close 8.7 bp; chain ended on the right side 0.470 of 672 chains; n=10080
- 30d: match 0.124 (body 0.085, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.2 bp; chain ended on the right side 0.510 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.2; 2: 0.201 / 4.8; 3: 0.169 / 6.4; 4: 0.131 / 6.8; 5: 0.124 / 7.6; 6: 0.114 / 8.2; 7: 0.111 / 8.5; 8: 0.098 / 9.2; 9: 0.090 / 9.3; 10: 0.088 / 9.7; 11: 0.085 / 10.1; 12: 0.076 / 10.5; 13: 0.069 / 10.8; 14: 0.070 / 11.2; 15: 0.063 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 134346, probability skill vs chance 0.2289, widened contest next: False
  - now: threshold 0.8389, hit rate recent 0.9 / long run 0.9294
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.293, naive rule 0.480, lift 2.73x
    - 24h: 49 calls (49 a day), hit rate 0.918, chance 0.297, naive rule 0.493, lift 3.10x
    - 7d: 419 calls (60 a day), hit rate 0.924, chance 0.293, naive rule 0.496, lift 3.15x
    - 30d: 1736 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.5658, hit rate recent 0.5735 / long run 0.5961
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.293, lift 2.10x
    - 24h: 47 calls (47 a day), hit rate 0.574, chance 0.297, lift 1.94x
    - 7d: 782 calls (112 a day), hit rate 0.600, chance 0.293, lift 2.05x
    - 30d: 2987 calls (100 a day), hit rate 0.586, chance 0.294, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 534, 0.523; 0.40: 473, 0.580; 0.45: 405, 0.651; 0.50: 355, 0.701; 0.55: 309, 0.744; 0.60: 262, 0.788; 0.65: 220, 0.813; 0.70: 174, 0.844; 0.75: 138, 0.877; 0.80: 92, 0.909; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 500, 0.463; 0.40: 404, 0.499; 0.45: 306, 0.535; 0.50: 198, 0.570; 0.55: 89, 0.572; 0.60: 12, 0.636; 0.65: 1, 0.636
- **K=5**: model 1792540800, labels learned 134344, probability skill vs chance 0.2252, widened contest next: False
  - now: threshold 0.6891, hit rate recent 0.8331 / long run 0.8201
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.194, naive rule 0.432, lift 5.15x
    - 24h: 46 calls (46 a day), hit rate 0.870, chance 0.183, naive rule 0.404, lift 4.75x
    - 7d: 426 calls (61 a day), hit rate 0.817, chance 0.186, naive rule 0.412, lift 4.38x
    - 30d: 1633 calls (54 a day), hit rate 0.817, chance 0.188, naive rule 0.406, lift 4.36x
  - next: threshold 0.4484, hit rate recent 0.5062 / long run 0.5085
    - 6h: 14 calls (57 a day), hit rate 0.500, chance 0.194, lift 2.58x
    - 24h: 54 calls (54 a day), hit rate 0.500, chance 0.183, lift 2.73x
    - 7d: 377 calls (54 a day), hit rate 0.533, chance 0.186, lift 2.86x
    - 30d: 2715 calls (91 a day), hit rate 0.478, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 346, 0.493; 0.40: 280, 0.566; 0.45: 230, 0.617; 0.50: 183, 0.665; 0.55: 145, 0.702; 0.60: 110, 0.750; 0.65: 77, 0.788; 0.70: 49, 0.820; 0.75: 29, 0.863; 0.80: 10, 0.880
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.386; 0.35: 255, 0.421; 0.40: 159, 0.459; 0.45: 67, 0.481; 0.50: 12, 0.493; 0.55: 1, 0.457
- **K=8**: model 1793059200, labels learned 134341, probability skill vs chance 0.2103, widened contest next: False
  - now: threshold 0.5744, hit rate recent 0.7048 / long run 0.6934
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.136, naive rule 0.379, lift 5.67x
    - 24h: 45 calls (45 a day), hit rate 0.756, chance 0.117, naive rule 0.333, lift 6.45x
    - 7d: 384 calls (55 a day), hit rate 0.714, chance 0.124, naive rule 0.348, lift 5.77x
    - 30d: 1583 calls (53 a day), hit rate 0.683, chance 0.121, naive rule 0.335, lift 5.66x
  - next: threshold 0.3604, hit rate recent 0.4263 / long run 0.4171
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.136, lift 4.61x
    - 24h: 54 calls (54 a day), hit rate 0.389, chance 0.117, lift 3.32x
    - 7d: 510 calls (73 a day), hit rate 0.441, chance 0.124, lift 3.57x
    - 30d: 2772 calls (92 a day), hit rate 0.390, chance 0.121, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 191, 0.496; 0.40: 150, 0.542; 0.45: 115, 0.591; 0.50: 84, 0.638; 0.55: 61, 0.672; 0.60: 41, 0.702; 0.65: 24, 0.775; 0.70: 12, 0.809; 0.75: 2, 0.766
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.361; 0.35: 90, 0.387; 0.40: 26, 0.415; 0.45: 5, 0.452; 0.50: 1, 0.667
- **K=13**: model 1793577600, labels learned 134336, probability skill vs chance 0.1941, widened contest next: False
  - now: threshold 0.4545, hit rate recent 0.619 / long run 0.5736
    - 6h: 12 calls (50 a day), hit rate 0.750, chance 0.099, naive rule 0.370, lift 7.61x
    - 24h: 57 calls (58 a day), hit rate 0.649, chance 0.084, naive rule 0.304, lift 7.71x
    - 7d: 422 calls (60 a day), hit rate 0.585, chance 0.080, naive rule 0.296, lift 7.29x
    - 30d: 1667 calls (56 a day), hit rate 0.563, chance 0.077, naive rule 0.280, lift 7.29x
  - next: threshold 0.2872, hit rate recent 0.3711 / long run 0.3386
    - 6h: 5 calls (21 a day), hit rate 0.400, chance 0.099, lift 4.06x
    - 24h: 47 calls (47 a day), hit rate 0.319, chance 0.084, lift 3.79x
    - 7d: 345 calls (49 a day), hit rate 0.357, chance 0.080, lift 4.44x
    - 30d: 1836 calls (61 a day), hit rate 0.326, chance 0.077, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.440; 0.35: 93, 0.492; 0.40: 66, 0.546; 0.45: 44, 0.588; 0.50: 30, 0.647; 0.55: 19, 0.677; 0.60: 10, 0.714; 0.65: 3, 0.694; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.332; 0.35: 13, 0.356; 0.40: 3, 0.415; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.414 | 1.08% | 0.883 | 0.433 | 0.247 | 0.600 | 0.384 |
| 6h | 15.831 | 0.82% | 0.925 | 0.519 | 0.250 | 0.517 | 0.445 |
| 24h | 17.228 | 3.43% | 0.910 | 0.506 | 0.250 | 0.512 | 0.567 |
| 7d | 15.549 | 5.03% | 0.900 | 0.500 | 0.250 | 0.510 | 0.738 |
| 30d | 14.544 | 4.27% | 0.900 | 0.500 | 0.250 | 0.499 | 0.685 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.571 | 14.527 | 14.565 | 14.543 | 14.672 | 14.662 | 14.470 | 14.413 | 14.461 | 14.414 |
| 6h | 15.962 | 15.951 | 15.887 | 15.937 | 16.181 | 15.945 | 15.866 | 15.833 | 15.835 | 15.831 |
| 24h | 17.839 | 17.393 | 17.321 | 17.253 | 17.563 | 17.391 | 17.196 | 17.203 | 17.195 | 17.228 |
| 7d | 16.372 | 15.725 | 15.678 | 15.594 | 15.886 | 15.879 | 15.534 | 15.521 | 15.525 | 15.549 |
| 30d | 15.192 | 14.696 | 14.637 | 14.575 | 14.812 | 14.756 | 14.536 | 14.515 | 14.517 | 14.544 |

## Next candle

- candle starting 2026-11-04 11:12 UTC, last close 2329.76
- P(up) 0.5017, return quantiles (bp): {'05': -7.618, '10': -5.846, '25': -3.157, '40': -1.25, '50': 0.019, '60': 1.354, '75': 3.047, '90': 6.225, '95': 8.326}
- changepoint probability 0.0534, regime age 108.1 min
- agent weights: empirical 0.006, ewma 0.067, garch 0.121, har 0.171, bocpd 0.022, hmm 0.063, online_qr 0.255, lgbm 0.294

## Learning log

- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.34, 4.65, 10.51], current probabilities: [0.007, 0.958, 0.035]
- live generator: {'versions': 60, 'latest_effective': '2026-11-04 11:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.241, 'l_abs': 0.708, 'l_hi': 0.789, 'l_lo': 0.81, 'b05': 0.745, 'b25': 0.719, 'b75': 0.655, 'b95': 0.705}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.239, 1.615, 1.76, 2.136, 2.038, 2.64, 2.27, 2.511, 2.548, 3.019, 2.859, 3.166, 3.426, 3.152]}
- calibration offsets (in sigma): {'05': 0.0955, '10': 0.111, '25': 0.0775, '40': 0.054, '50': 0.055, '60': 0.096, '75': 0.0525, '90': 0.029, '95': -0.0155}
