# ETH-USD 60s candle generator - report

- generated: 2026-10-10 08:32 UTC
- last closed candle: 2026-10-10 08:32 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.499 (671) [0.449, 0.550] | 0.503 (2875) [0.483, 0.524] | 0.509 (3643) [0.492, 0.526] | 0.499 (671) [0.449, 0.550] | 0.588 (34) | 0.500 | flat -0.029 (noise 0.036) |
| colour_clear | 0.544 (796) | 0.546 (5306) [0.538, 0.554] | 0.508 (23193) [0.502, 0.516] | 0.505 (29544) [0.499, 0.512] | 0.546 (5306) [0.538, 0.554] | 0.553 (291) | 0.500 | up +0.051 (noise 0.010) |
| colour_confident | 0.687 (134) | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (105) | 0.500 | - |
| colour_next | 0.516 (1433) | 0.529 (9975) [0.520, 0.538] | 0.507 (42879) [0.502, 0.512] | 0.506 (54324) [0.501, 0.510] | 0.529 (9975) [0.520, 0.538] | 0.541 (503) | 0.500 | up +0.024 (noise 0.007) |
| colour_path | 0.501 (20062) | 0.499 (139650) [0.495, 0.503] | 0.501 (600306) [0.499, 0.502] | 0.500 (760536) [0.499, 0.501] | 0.499 (139650) [0.495, 0.503] | 0.502 (7042) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.880 (25) | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.725 (40) | 0.500 | - |
| reversal_k13_next | 0.338 (74) | 0.324 (541) [0.309, 0.337] | 0.311 (2040) [0.297, 0.327] | 0.305 (2646) [0.291, 0.319] | 0.324 (541) [0.309, 0.337] | 0.387 (31) | 0.077 | up +0.057 (noise 0.027) |
| reversal_k13_now | 0.660 (47) | 0.596 (386) [0.555, 0.647] | 0.588 (1486) [0.565, 0.611] | 0.584 (1858) [0.566, 0.604] | 0.596 (386) [0.555, 0.647] | 0.550 (20) | 0.077 | flat +0.015 (noise 0.038) |
| reversal_k3_next | 0.565 (85) | 0.570 (572) [0.541, 0.607] | 0.584 (2351) [0.569, 0.599] | 0.584 (3012) [0.572, 0.598] | 0.570 (572) [0.541, 0.607] | 0.525 (40) | 0.292 | flat -0.008 (noise 0.029) |
| reversal_k3_now | 0.921 (63) | 0.926 (408) [0.917, 0.939] | 0.940 (1711) [0.932, 0.948] | 0.939 (2171) [0.931, 0.946] | 0.926 (408) [0.917, 0.939] | 0.885 (26) | 0.292 | flat -0.023 (noise 0.017) |
| reversal_k5_next | 0.486 (74) | 0.446 (596) [0.419, 0.481] | 0.488 (2110) [0.468, 0.508] | 0.483 (2586) [0.467, 0.500] | 0.446 (596) [0.419, 0.481] | 0.440 (25) | 0.187 | flat -0.028 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.818 (385) [0.787, 0.851] | 0.835 (1578) [0.819, 0.850] | 0.834 (1996) [0.820, 0.848] | 0.818 (385) [0.787, 0.851] | 0.773 (22) | 0.187 | flat -0.052 (noise 0.027) |
| reversal_k8_next | 0.407 (81) | 0.388 (621) [0.361, 0.417] | 0.405 (2121) [0.388, 0.424] | 0.394 (2727) [0.380, 0.410] | 0.388 (621) [0.361, 0.417] | 0.560 (25) | 0.121 | flat +0.005 (noise 0.032) |
| reversal_k8_now | 0.596 (47) | 0.698 (407) [0.656, 0.740] | 0.720 (1585) [0.700, 0.740] | 0.711 (1994) [0.693, 0.729] | 0.698 (407) [0.656, 0.740] | 0.650 (20) | 0.122 | flat -0.041 (noise 0.035) |
| overall | 0.503 (22109) | 0.503 (154212) [0.498, 0.507] | 0.503 (661042) [0.502, 0.505] | 0.503 (837493) [0.501, 0.504] | 0.503 (154212) [0.498, 0.507] | 0.507 (7788) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07902, 0.1187] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.533, 'levels': [{'threshold': 0.07902, 'calls_per_day': 147.8, 'win_rate': 0.6182}, {'threshold': 0.1187, 'calls_per_day': 38.2, 'win_rate': 0.6667}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 9345, 'rate': 0.5317}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15051 | 0.334 | 0.516 (14831) | 0.614 (818) | 0.775 (2418) |
| volatility: normal | 15050 | 0.360 | 0.510 (14981) | 0.624 (170) | 0.772 (2124) |
| volatility: wild | 15051 | 0.374 | 0.496 (15007) | 0.667 (66) | 0.777 (2078) |
| session: Asia 00-08 | 15360 | 0.352 | 0.509 (15252) | 0.596 (421) | 0.779 (2185) |
| session: Europe 08-13 | 9332 | 0.351 | 0.506 (9270) | 0.605 (205) | 0.762 (1478) |
| session: US 13-21 | 14880 | 0.366 | 0.505 (14783) | 0.630 (249) | 0.783 (2165) |
| session: late 21-24 | 5580 | 0.349 | 0.510 (5514) | 0.670 (179) | 0.761 (792) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.366 | 0.284 | 0.185 | 0.185 | 0.649 | 0.339 | 0.394 | 1.103 |
| 6h | 360 | 0.332 | 0.314 | 0.220 | 0.241 | 0.541 | 0.269 | 0.395 | 1.236 |
| 24h | 1440 | 0.349 | 0.340 | 0.255 | 0.287 | 0.526 | 0.260 | 0.438 | 1.167 |
| 7d | 10080 | 0.351 | 0.344 | 0.270 | 0.295 | 0.531 | 0.256 | 0.446 | 1.225 |
| 30d | 43200 | 0.356 | 0.354 | 0.278 | 0.307 | 0.508 | 0.248 | 0.464 | 1.289 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.366 / 0.649 / 0.900; 2: 0.322 / 0.526 / 0.883; 3: 0.307 / 0.491 / 0.917; 4: 0.337 / 0.596 / 0.967; 5: 0.330 / 0.596 / 0.900; 6: 0.319 / 0.474 / 0.950; 7: 0.302 / 0.421 / 0.933; 8: 0.349 / 0.579 / 0.917; 9: 0.316 / 0.474 / 0.917; 10: 0.324 / 0.474 / 0.933; 11: 0.325 / 0.544 / 0.983; 12: 0.354 / 0.526 / 0.983; 13: 0.339 / 0.561 / 0.950; 14: 0.343 / 0.579 / 0.950; 15: 0.345 / 0.596 / 0.983
- 6h: 1: 0.332 / 0.541 / 0.889; 2: 0.311 / 0.510 / 0.892; 3: 0.300 / 0.490 / 0.900; 4: 0.307 / 0.510 / 0.906; 5: 0.317 / 0.541 / 0.886; 6: 0.322 / 0.544 / 0.919; 7: 0.306 / 0.490 / 0.925; 8: 0.317 / 0.530 / 0.908; 9: 0.302 / 0.467 / 0.917; 10: 0.319 / 0.527 / 0.936; 11: 0.312 / 0.504 / 0.944; 12: 0.321 / 0.521 / 0.953; 13: 0.309 / 0.482 / 0.950; 14: 0.320 / 0.550 / 0.936; 15: 0.303 / 0.462 / 0.939
- 24h: 1: 0.349 / 0.526 / 0.896; 2: 0.337 / 0.507 / 0.895; 3: 0.336 / 0.498 / 0.897; 4: 0.336 / 0.504 / 0.906; 5: 0.336 / 0.497 / 0.900; 6: 0.338 / 0.509 / 0.912; 7: 0.328 / 0.485 / 0.916; 8: 0.337 / 0.516 / 0.909; 9: 0.326 / 0.472 / 0.910; 10: 0.336 / 0.507 / 0.916; 11: 0.336 / 0.511 / 0.921; 12: 0.337 / 0.502 / 0.928; 13: 0.332 / 0.491 / 0.924; 14: 0.335 / 0.521 / 0.917; 15: 0.333 / 0.497 / 0.910
- 7d: 1: 0.351 / 0.531 / 0.896; 2: 0.340 / 0.502 / 0.900; 3: 0.341 / 0.509 / 0.900; 4: 0.340 / 0.506 / 0.901; 5: 0.337 / 0.498 / 0.900; 6: 0.336 / 0.496 / 0.902; 7: 0.336 / 0.501 / 0.902; 8: 0.336 / 0.493 / 0.901; 9: 0.332 / 0.486 / 0.901; 10: 0.336 / 0.506 / 0.902; 11: 0.334 / 0.496 / 0.901; 12: 0.335 / 0.501 / 0.901; 13: 0.337 / 0.506 / 0.900; 14: 0.335 / 0.501 / 0.900; 15: 0.335 / 0.494 / 0.901
- 30d: 1: 0.356 / 0.508 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.349 / 0.500 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.502 / 0.901; 7: 0.348 / 0.504 / 0.901; 8: 0.348 / 0.503 / 0.901; 9: 0.345 / 0.496 / 0.901; 10: 0.347 / 0.504 / 0.901; 11: 0.346 / 0.501 / 0.901; 12: 0.346 / 0.501 / 0.901; 13: 0.345 / 0.501 / 0.901; 14: 0.344 / 0.497 / 0.901; 15: 0.344 / 0.496 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.104 (body 0.082, range 0.125); 'price stays where it was' would score 0.106; colour right 0.526; typical miss of the close 3.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.097, range 0.160); 'price stays where it was' would score 0.122; colour right 0.504; typical miss of the close 3.2 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.131 (body 0.093, range 0.169); 'price stays where it was' would score 0.131; colour right 0.498; typical miss of the close 5.1 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.117 (body 0.080, range 0.153); 'price stays where it was' would score 0.120; colour right 0.498; typical miss of the close 6.0 bp; chain ended on the right side 0.502 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.0 bp; chain ended on the right side 0.506 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.1; 2: 0.200 / 4.4; 3: 0.167 / 6.0; 4: 0.131 / 6.6; 5: 0.120 / 7.3; 6: 0.111 / 7.9; 7: 0.101 / 8.4; 8: 0.092 / 8.6; 9: 0.086 / 9.0; 10: 0.080 / 9.6; 11: 0.076 / 10.3; 12: 0.075 / 10.7; 13: 0.063 / 11.0; 14: 0.065 / 11.1; 15: 0.061 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 98186, probability skill vs chance 0.2248, widened contest next: True
  - now: threshold 0.8418, hit rate recent 0.9017 / long run 0.9314
    - 6h: 17 calls (69 a day), hit rate 0.941, chance 0.287, naive rule 0.464, lift 3.28x
    - 24h: 68 calls (68 a day), hit rate 0.882, chance 0.312, naive rule 0.530, lift 2.83x
    - 7d: 410 calls (59 a day), hit rate 0.922, chance 0.294, naive rule 0.490, lift 3.13x
    - 30d: 1715 calls (57 a day), hit rate 0.939, chance 0.291, naive rule 0.482, lift 3.22x
  - next: threshold 0.5544, hit rate recent 0.5387 / long run 0.5725
    - 6h: 29 calls (118 a day), hit rate 0.483, chance 0.287, lift 1.68x
    - 24h: 95 calls (95 a day), hit rate 0.558, chance 0.312, lift 1.79x
    - 7d: 570 calls (81 a day), hit rate 0.567, chance 0.294, lift 1.92x
    - 30d: 2360 calls (79 a day), hit rate 0.584, chance 0.291, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.517; 0.40: 485, 0.562; 0.45: 418, 0.629; 0.50: 366, 0.683; 0.55: 321, 0.725; 0.60: 273, 0.768; 0.65: 226, 0.802; 0.70: 181, 0.834; 0.75: 138, 0.872; 0.80: 97, 0.912; 0.85: 49, 0.947; 0.90: 2, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.458; 0.40: 412, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.552; 0.55: 91, 0.582; 0.60: 13, 0.600; 0.65: 1, 0.682
- **K=5**: model 1791590400, labels learned 98184, probability skill vs chance 0.2042, widened contest next: True
  - now: threshold 0.7128, hit rate recent 0.7882 / long run 0.8256
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.183, naive rule 0.372, lift 5.08x
    - 24h: 52 calls (52 a day), hit rate 0.788, chance 0.198, naive rule 0.412, lift 3.99x
    - 7d: 384 calls (55 a day), hit rate 0.812, chance 0.189, naive rule 0.393, lift 4.29x
    - 30d: 1580 calls (53 a day), hit rate 0.833, chance 0.187, naive rule 0.391, lift 4.46x
  - next: threshold 0.4609, hit rate recent 0.4646 / long run 0.4655
    - 6h: 21 calls (86 a day), hit rate 0.381, chance 0.183, lift 2.08x
    - 24h: 74 calls (74 a day), hit rate 0.486, chance 0.198, lift 2.46x
    - 7d: 549 calls (78 a day), hit rate 0.446, chance 0.189, lift 2.36x
    - 30d: 2100 calls (70 a day), hit rate 0.487, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 429, 0.414; 0.35: 365, 0.470; 0.40: 294, 0.539; 0.45: 240, 0.599; 0.50: 186, 0.657; 0.55: 141, 0.703; 0.60: 109, 0.746; 0.65: 84, 0.791; 0.70: 62, 0.823; 0.75: 34, 0.861; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.385; 0.35: 252, 0.423; 0.40: 164, 0.451; 0.45: 83, 0.474; 0.50: 20, 0.513; 0.55: 2, 0.548
- **K=8**: model 1791417600, labels learned 98181, probability skill vs chance 0.2059, widened contest next: True
  - now: threshold 0.5804, hit rate recent 0.6332 / long run 0.7029
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.139, naive rule 0.383, lift 6.01x
    - 24h: 54 calls (54 a day), hit rate 0.611, chance 0.126, naive rule 0.357, lift 4.85x
    - 7d: 407 calls (58 a day), hit rate 0.686, chance 0.122, naive rule 0.329, lift 5.60x
    - 30d: 1584 calls (53 a day), hit rate 0.718, chance 0.121, naive rule 0.327, lift 5.91x
  - next: threshold 0.3687, hit rate recent 0.45 / long run 0.3993
    - 6h: 21 calls (86 a day), hit rate 0.476, chance 0.139, lift 3.44x
    - 24h: 76 calls (77 a day), hit rate 0.474, chance 0.126, lift 3.76x
    - 7d: 621 calls (89 a day), hit rate 0.393, chance 0.122, lift 3.21x
    - 30d: 2109 calls (70 a day), hit rate 0.407, chance 0.121, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 269, 0.405; 0.35: 203, 0.480; 0.40: 156, 0.540; 0.45: 123, 0.588; 0.50: 93, 0.631; 0.55: 67, 0.685; 0.60: 46, 0.726; 0.65: 24, 0.768; 0.70: 9, 0.819; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 184, 0.349; 0.35: 113, 0.388; 0.40: 47, 0.415; 0.45: 10, 0.440; 0.50: 1, 0.429
- **K=13**: model 1791504000, labels learned 98176, probability skill vs chance 0.185, widened contest next: False
  - now: threshold 0.429, hit rate recent 0.6085 / long run 0.587
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.103, naive rule 0.361, lift 6.73x
    - 24h: 52 calls (53 a day), hit rate 0.615, chance 0.084, naive rule 0.302, lift 7.31x
    - 7d: 389 calls (56 a day), hit rate 0.586, chance 0.079, naive rule 0.274, lift 7.46x
    - 30d: 1492 calls (50 a day), hit rate 0.586, chance 0.077, naive rule 0.269, lift 7.59x
  - next: threshold 0.2839, hit rate recent 0.3576 / long run 0.3148
    - 6h: 21 calls (88 a day), hit rate 0.333, chance 0.103, lift 3.24x
    - 24h: 77 calls (78 a day), hit rate 0.377, chance 0.084, lift 4.47x
    - 7d: 536 calls (77 a day), hit rate 0.323, chance 0.079, lift 4.11x
    - 30d: 2047 calls (68 a day), hit rate 0.312, chance 0.077, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.443; 0.35: 87, 0.504; 0.40: 62, 0.554; 0.45: 44, 0.609; 0.50: 27, 0.630; 0.55: 15, 0.680; 0.60: 5, 0.706; 0.65: 1, 0.757
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.323; 0.35: 15, 0.352; 0.40: 3, 0.348; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.863 | 13.14% | 0.933 | 0.433 | 0.252 | 0.386 | -0.073 |
| 6h | 5.628 | 10.80% | 0.897 | 0.511 | 0.250 | 0.482 | 0.204 |
| 24h | 10.189 | 5.75% | 0.899 | 0.508 | 0.251 | 0.495 | 0.656 |
| 7d | 10.884 | 5.15% | 0.899 | 0.500 | 0.251 | 0.496 | 0.678 |
| 30d | 14.135 | 4.49% | 0.900 | 0.500 | 0.251 | 0.498 | 0.697 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.598 | 4.851 | 4.950 | 4.873 | 4.961 | 5.036 | 4.836 | 4.851 | 4.842 | 4.863 |
| 6h | 6.309 | 5.671 | 5.745 | 5.635 | 5.758 | 5.796 | 5.621 | 5.604 | 5.621 | 5.628 |
| 24h | 10.810 | 10.311 | 10.297 | 10.229 | 10.462 | 10.380 | 10.186 | 10.139 | 10.170 | 10.189 |
| 7d | 11.475 | 10.986 | 10.963 | 10.934 | 11.080 | 11.120 | 10.880 | 10.866 | 10.866 | 10.884 |
| 30d | 14.799 | 14.266 | 14.218 | 14.166 | 14.406 | 14.365 | 14.137 | 14.109 | 14.108 | 14.135 |

## Next candle

- candle starting 2026-10-10 08:32 UTC, last close 2491.69
- P(up) 0.4965, return quantiles (bp): {'05': -2.848, '10': -2.026, '25': -1.049, '40': -0.365, '50': -0.009, '60': 0.309, '75': 1.006, '90': 2.272, '95': 3.121}
- changepoint probability 0.0313, regime age 440.0 min
- agent weights: empirical 0.003, ewma 0.116, garch 0.076, har 0.186, bocpd 0.041, hmm 0.041, online_qr 0.240, lgbm 0.298

## Learning log

- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.35, 4.9, 15.58], current probabilities: [0.952, 0.048, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-10 08:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.466, 'l_abs': 0.714, 'l_hi': 0.761, 'l_lo': 0.719, 'b05': 0.676, 'b25': 0.68, 'b75': 0.629, 'b95': 0.652}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.454, 1.715, 1.795, 2.052, 1.881, 1.956, 2.27, 2.412, 2.26, 2.328, 2.204, 2.345, 2.59, 2.686]}
- calibration offsets (in sigma): {'05': 0.0655, '10': 0.061, '25': -0.0125, '40': -0.016, '50': -0.005, '60': -0.034, '75': -0.0475, '90': -0.001, '95': 0.0045}
