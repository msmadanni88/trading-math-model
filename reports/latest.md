# ETH-USD 60s candle generator - report

- generated: 2026-10-10 18:54 UTC
- last closed candle: 2026-10-10 18:54 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.499 (671) [0.449, 0.550] | 0.503 (2875) [0.483, 0.524] | 0.509 (3643) [0.492, 0.526] | 0.499 (671) [0.449, 0.550] | 0.587 (75) | 0.500 | flat -0.029 (noise 0.036) |
| colour_clear | 0.544 (796) | 0.546 (5306) [0.538, 0.554] | 0.508 (23193) [0.502, 0.516] | 0.505 (29544) [0.499, 0.512] | 0.546 (5306) [0.538, 0.554] | 0.535 (613) | 0.500 | up +0.051 (noise 0.010) |
| colour_confident | 0.687 (134) | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.554 (240) | 0.500 | - |
| colour_next | 0.516 (1433) | 0.529 (9975) [0.520, 0.538] | 0.507 (42879) [0.502, 0.512] | 0.506 (54324) [0.501, 0.510] | 0.529 (9975) [0.520, 0.538] | 0.527 (1092) | 0.500 | up +0.024 (noise 0.007) |
| colour_path | 0.501 (20062) | 0.499 (139650) [0.495, 0.503] | 0.501 (600306) [0.499, 0.502] | 0.500 (760536) [0.499, 0.501] | 0.499 (139650) [0.495, 0.503] | 0.499 (15288) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.880 (25) | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.639 (83) | 0.500 | - |
| reversal_k13_next | 0.338 (74) | 0.324 (541) [0.309, 0.337] | 0.311 (2040) [0.297, 0.327] | 0.305 (2646) [0.291, 0.319] | 0.324 (541) [0.309, 0.337] | 0.362 (58) | 0.077 | up +0.057 (noise 0.027) |
| reversal_k13_now | 0.660 (47) | 0.596 (386) [0.555, 0.647] | 0.588 (1486) [0.565, 0.611] | 0.584 (1858) [0.566, 0.604] | 0.596 (386) [0.555, 0.647] | 0.565 (46) | 0.077 | flat +0.015 (noise 0.038) |
| reversal_k3_next | 0.565 (85) | 0.570 (572) [0.541, 0.607] | 0.584 (2351) [0.569, 0.599] | 0.584 (3012) [0.572, 0.598] | 0.570 (572) [0.541, 0.607] | 0.598 (97) | 0.292 | flat -0.008 (noise 0.029) |
| reversal_k3_now | 0.921 (63) | 0.926 (408) [0.917, 0.939] | 0.940 (1711) [0.932, 0.948] | 0.939 (2171) [0.931, 0.946] | 0.926 (408) [0.917, 0.939] | 0.926 (54) | 0.292 | flat -0.023 (noise 0.017) |
| reversal_k5_next | 0.486 (74) | 0.446 (596) [0.419, 0.481] | 0.488 (2110) [0.468, 0.508] | 0.483 (2586) [0.467, 0.500] | 0.446 (596) [0.419, 0.481] | 0.475 (59) | 0.187 | flat -0.028 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.818 (385) [0.787, 0.851] | 0.835 (1578) [0.819, 0.850] | 0.834 (1996) [0.820, 0.848] | 0.818 (385) [0.787, 0.851] | 0.857 (49) | 0.187 | flat -0.052 (noise 0.027) |
| reversal_k8_next | 0.407 (81) | 0.388 (621) [0.361, 0.417] | 0.405 (2121) [0.388, 0.424] | 0.394 (2727) [0.380, 0.410] | 0.388 (621) [0.361, 0.417] | 0.444 (54) | 0.121 | flat +0.005 (noise 0.032) |
| reversal_k8_now | 0.596 (47) | 0.698 (407) [0.656, 0.740] | 0.720 (1585) [0.700, 0.740] | 0.711 (1994) [0.693, 0.729] | 0.698 (407) [0.656, 0.740] | 0.717 (46) | 0.122 | flat -0.041 (noise 0.035) |
| overall | 0.503 (22109) | 0.503 (154212) [0.498, 0.507] | 0.503 (661042) [0.502, 0.505] | 0.503 (837493) [0.501, 0.504] | 0.503 (154212) [0.498, 0.507] | 0.505 (16918) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08077, 0.1218] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5306, 'levels': [{'threshold': 0.08077, 'calls_per_day': 146.8, 'win_rate': 0.6004}, {'threshold': 0.1218, 'calls_per_day': 37.2, 'win_rate': 0.6515}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 9934, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15258 | 0.333 | 0.515 (15007) | 0.597 (945) | 0.780 (2458) |
| volatility: normal | 15258 | 0.360 | 0.511 (15187) | 0.629 (178) | 0.767 (2169) |
| volatility: wild | 15258 | 0.374 | 0.495 (15214) | 0.667 (66) | 0.779 (2100) |
| session: Asia 00-08 | 15360 | 0.352 | 0.509 (15252) | 0.596 (421) | 0.779 (2185) |
| session: Europe 08-13 | 9600 | 0.349 | 0.506 (9511) | 0.596 (282) | 0.766 (1513) |
| session: US 13-21 | 15234 | 0.365 | 0.506 (15131) | 0.590 (307) | 0.782 (2237) |
| session: late 21-24 | 5580 | 0.349 | 0.510 (5514) | 0.670 (179) | 0.761 (792) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.357 | 0.349 | 0.234 | 0.234 | 0.552 | 0.273 | 0.441 | 1.001 |
| 6h | 360 | 0.324 | 0.307 | 0.254 | 0.268 | 0.507 | 0.235 | 0.413 | 1.288 |
| 24h | 1440 | 0.326 | 0.311 | 0.234 | 0.256 | 0.523 | 0.253 | 0.399 | 1.265 |
| 7d | 10080 | 0.351 | 0.344 | 0.271 | 0.296 | 0.531 | 0.257 | 0.446 | 1.227 |
| 30d | 43200 | 0.355 | 0.353 | 0.277 | 0.306 | 0.508 | 0.248 | 0.462 | 1.296 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.357 / 0.552 / 0.900; 2: 0.305 / 0.362 / 1.000; 3: 0.330 / 0.466 / 1.000; 4: 0.342 / 0.534 / 1.000; 5: 0.330 / 0.500 / 1.000; 6: 0.350 / 0.569 / 1.000; 7: 0.340 / 0.517 / 1.000; 8: 0.352 / 0.603 / 1.000; 9: 0.328 / 0.483 / 1.000; 10: 0.361 / 0.621 / 1.000; 11: 0.353 / 0.569 / 1.000; 12: 0.362 / 0.586 / 1.000; 13: 0.341 / 0.483 / 1.000; 14: 0.311 / 0.379 / 1.000; 15: 0.323 / 0.431 / 1.000
- 6h: 1: 0.324 / 0.507 / 0.883; 2: 0.303 / 0.456 / 0.928; 3: 0.321 / 0.524 / 0.925; 4: 0.313 / 0.501 / 0.917; 5: 0.323 / 0.542 / 0.906; 6: 0.305 / 0.473 / 0.886; 7: 0.307 / 0.490 / 0.875; 8: 0.297 / 0.458 / 0.886; 9: 0.308 / 0.507 / 0.883; 10: 0.304 / 0.501 / 0.867; 11: 0.312 / 0.504 / 0.861; 12: 0.308 / 0.504 / 0.828; 13: 0.306 / 0.504 / 0.839; 14: 0.310 / 0.499 / 0.850; 15: 0.308 / 0.484 / 0.856
- 24h: 1: 0.326 / 0.523 / 0.885; 2: 0.313 / 0.490 / 0.906; 3: 0.312 / 0.508 / 0.921; 4: 0.309 / 0.493 / 0.890; 5: 0.317 / 0.515 / 0.892; 6: 0.311 / 0.488 / 0.883; 7: 0.309 / 0.493 / 0.876; 8: 0.311 / 0.504 / 0.885; 9: 0.308 / 0.497 / 0.886; 10: 0.313 / 0.515 / 0.877; 11: 0.310 / 0.496 / 0.878; 12: 0.311 / 0.497 / 0.865; 13: 0.312 / 0.509 / 0.870; 14: 0.314 / 0.515 / 0.878; 15: 0.310 / 0.485 / 0.880
- 7d: 1: 0.351 / 0.531 / 0.896; 2: 0.340 / 0.500 / 0.900; 3: 0.342 / 0.511 / 0.900; 4: 0.339 / 0.503 / 0.899; 5: 0.338 / 0.501 / 0.900; 6: 0.335 / 0.494 / 0.899; 7: 0.335 / 0.501 / 0.898; 8: 0.335 / 0.493 / 0.900; 9: 0.332 / 0.489 / 0.900; 10: 0.336 / 0.505 / 0.899; 11: 0.334 / 0.494 / 0.899; 12: 0.335 / 0.500 / 0.897; 13: 0.336 / 0.505 / 0.898; 14: 0.334 / 0.502 / 0.899; 15: 0.335 / 0.496 / 0.899
- 30d: 1: 0.355 / 0.508 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.500 / 0.900; 5: 0.349 / 0.504 / 0.900; 6: 0.347 / 0.501 / 0.900; 7: 0.347 / 0.504 / 0.899; 8: 0.347 / 0.503 / 0.900; 9: 0.344 / 0.496 / 0.900; 10: 0.346 / 0.504 / 0.900; 11: 0.345 / 0.501 / 0.900; 12: 0.345 / 0.502 / 0.899; 13: 0.345 / 0.501 / 0.899; 14: 0.344 / 0.497 / 0.899; 15: 0.343 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.164 (body 0.152, range 0.177); 'price stays where it was' would score 0.196; colour right 0.552; typical miss of the close 4.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.112 (body 0.081, range 0.144); 'price stays where it was' would score 0.133; colour right 0.476; typical miss of the close 5.0 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.122 (body 0.088, range 0.157); 'price stays where it was' would score 0.123; colour right 0.488; typical miss of the close 3.8 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.117 (body 0.081, range 0.154); 'price stays where it was' would score 0.122; colour right 0.497; typical miss of the close 6.0 bp; chain ended on the right side 0.502 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.200 / 4.3; 3: 0.167 / 5.9; 4: 0.133 / 6.5; 5: 0.120 / 7.1; 6: 0.110 / 7.8; 7: 0.101 / 8.2; 8: 0.093 / 8.5; 9: 0.086 / 8.8; 10: 0.080 / 9.5; 11: 0.075 / 10.0; 12: 0.074 / 10.5; 13: 0.063 / 10.9; 14: 0.065 / 11.0; 15: 0.061 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 98808, probability skill vs chance 0.2283, widened contest next: False
  - now: threshold 0.8423, hit rate recent 0.9263 / long run 0.9329
    - 6h: 20 calls (81 a day), hit rate 0.950, chance 0.324, naive rule 0.567, lift 2.93x
    - 24h: 66 calls (66 a day), hit rate 0.924, chance 0.315, naive rule 0.533, lift 2.94x
    - 7d: 419 calls (60 a day), hit rate 0.926, chance 0.296, naive rule 0.494, lift 3.12x
    - 30d: 1715 calls (57 a day), hit rate 0.940, chance 0.292, naive rule 0.483, lift 3.22x
  - next: threshold 0.5426, hit rate recent 0.6102 / long run 0.5795
    - 6h: 37 calls (150 a day), hit rate 0.676, chance 0.324, lift 2.09x
    - 24h: 113 calls (113 a day), hit rate 0.593, chance 0.315, lift 1.88x
    - 7d: 560 calls (80 a day), hit rate 0.584, chance 0.296, lift 1.97x
    - 30d: 2364 calls (79 a day), hit rate 0.585, chance 0.292, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 537, 0.517; 0.40: 485, 0.563; 0.45: 418, 0.630; 0.50: 365, 0.684; 0.55: 320, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 138, 0.873; 0.80: 97, 0.913; 0.85: 49, 0.948; 0.90: 2, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.458; 0.40: 412, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.553; 0.55: 91, 0.581; 0.60: 13, 0.598; 0.65: 1, 0.682
- **K=5**: model 1791590400, labels learned 98806, probability skill vs chance 0.2162, widened contest next: False
  - now: threshold 0.7129, hit rate recent 0.8395 / long run 0.8301
    - 6h: 20 calls (82 a day), hit rate 0.900, chance 0.224, naive rule 0.484, lift 4.02x
    - 24h: 57 calls (57 a day), hit rate 0.842, chance 0.196, naive rule 0.426, lift 4.29x
    - 7d: 388 calls (55 a day), hit rate 0.822, chance 0.191, naive rule 0.399, lift 4.31x
    - 30d: 1582 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.47x
  - next: threshold 0.4642, hit rate recent 0.4694 / long run 0.4673
    - 6h: 20 calls (82 a day), hit rate 0.400, chance 0.224, lift 1.79x
    - 24h: 71 calls (71 a day), hit rate 0.479, chance 0.196, lift 2.44x
    - 7d: 508 calls (73 a day), hit rate 0.463, chance 0.191, lift 2.42x
    - 30d: 2093 calls (70 a day), hit rate 0.484, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 428, 0.415; 0.35: 364, 0.471; 0.40: 294, 0.541; 0.45: 240, 0.600; 0.50: 186, 0.658; 0.55: 140, 0.705; 0.60: 109, 0.748; 0.65: 84, 0.795; 0.70: 62, 0.825; 0.75: 34, 0.864; 0.80: 10, 0.884
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 253, 0.423; 0.40: 165, 0.451; 0.45: 83, 0.472; 0.50: 20, 0.510; 0.55: 2, 0.540
- **K=8**: model 1791417600, labels learned 98803, probability skill vs chance 0.2065, widened contest next: False
  - now: threshold 0.5678, hit rate recent 0.6771 / long run 0.7057
    - 6h: 15 calls (62 a day), hit rate 0.600, chance 0.137, naive rule 0.397, lift 4.38x
    - 24h: 57 calls (57 a day), hit rate 0.684, chance 0.131, naive rule 0.376, lift 5.23x
    - 7d: 416 calls (59 a day), hit rate 0.692, chance 0.124, naive rule 0.337, lift 5.58x
    - 30d: 1580 calls (53 a day), hit rate 0.720, chance 0.122, naive rule 0.328, lift 5.91x
  - next: threshold 0.3693, hit rate recent 0.3969 / long run 0.3966
    - 6h: 16 calls (66 a day), hit rate 0.188, chance 0.137, lift 1.37x
    - 24h: 66 calls (66 a day), hit rate 0.424, chance 0.131, lift 3.24x
    - 7d: 614 calls (88 a day), hit rate 0.394, chance 0.124, lift 3.18x
    - 30d: 2102 calls (70 a day), hit rate 0.406, chance 0.122, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 268, 0.406; 0.35: 203, 0.481; 0.40: 156, 0.542; 0.45: 122, 0.589; 0.50: 93, 0.633; 0.55: 67, 0.688; 0.60: 46, 0.728; 0.65: 24, 0.767; 0.70: 9, 0.815; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 184, 0.349; 0.35: 112, 0.387; 0.40: 47, 0.414; 0.45: 10, 0.437; 0.50: 1, 0.405
- **K=13**: model 1791504000, labels learned 98798, probability skill vs chance 0.1837, widened contest next: False
  - now: threshold 0.4322, hit rate recent 0.598 / long run 0.5865
    - 6h: 17 calls (71 a day), hit rate 0.529, chance 0.094, naive rule 0.320, lift 5.62x
    - 24h: 54 calls (55 a day), hit rate 0.556, chance 0.092, naive rule 0.320, lift 6.04x
    - 7d: 399 calls (57 a day), hit rate 0.581, chance 0.080, naive rule 0.280, lift 7.29x
    - 30d: 1489 calls (50 a day), hit rate 0.586, chance 0.077, naive rule 0.269, lift 7.57x
  - next: threshold 0.2874, hit rate recent 0.3434 / long run 0.3155
    - 6h: 13 calls (54 a day), hit rate 0.231, chance 0.094, lift 2.45x
    - 24h: 72 calls (73 a day), hit rate 0.347, chance 0.092, lift 3.78x
    - 7d: 518 calls (74 a day), hit rate 0.330, chance 0.080, lift 4.14x
    - 30d: 2045 calls (68 a day), hit rate 0.311, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.445; 0.35: 87, 0.506; 0.40: 62, 0.554; 0.45: 43, 0.610; 0.50: 27, 0.634; 0.55: 14, 0.686; 0.60: 5, 0.709; 0.65: 1, 0.750
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.323; 0.35: 15, 0.348; 0.40: 3, 0.341; 0.45: 0, 0.286

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.558 | -0.46% | 0.900 | 0.367 | 0.250 | 0.517 | 0.089 |
| 6h | 7.379 | 2.44% | 0.897 | 0.492 | 0.253 | 0.401 | 0.552 |
| 24h | 6.361 | 7.98% | 0.893 | 0.497 | 0.251 | 0.463 | 0.509 |
| 7d | 10.961 | 5.02% | 0.900 | 0.500 | 0.251 | 0.492 | 0.675 |
| 30d | 13.982 | 4.53% | 0.900 | 0.500 | 0.251 | 0.497 | 0.700 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.528 | 6.562 | 6.513 | 6.587 | 6.526 | 6.511 | 6.569 | 6.565 | 6.543 | 6.558 |
| 6h | 7.563 | 7.471 | 7.411 | 7.399 | 7.530 | 7.469 | 7.413 | 7.346 | 7.371 | 7.379 |
| 24h | 6.912 | 6.412 | 6.449 | 6.384 | 6.505 | 6.513 | 6.361 | 6.336 | 6.351 | 6.361 |
| 7d | 11.540 | 11.064 | 11.036 | 11.011 | 11.156 | 11.177 | 10.959 | 10.942 | 10.943 | 10.961 |
| 30d | 14.646 | 14.113 | 14.066 | 14.013 | 14.252 | 14.213 | 13.985 | 13.955 | 13.956 | 13.982 |

## Next candle

- candle starting 2026-10-10 18:54 UTC, last close 2509.72
- P(up) 0.5214, return quantiles (bp): {'05': -3.702, '10': -2.67, '25': -1.204, '40': -0.288, '50': 0.076, '60': 0.608, '75': 1.352, '90': 2.874, '95': 3.868}
- changepoint probability 0.0508, regime age 132.9 min
- agent weights: empirical 0.005, ewma 0.109, garch 0.111, har 0.167, bocpd 0.044, hmm 0.046, online_qr 0.193, lgbm 0.325

## Learning log

- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.22, 4.82, 15.52], current probabilities: [0.794, 0.205, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-10 19:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.261, 'l_abs': 0.67, 'l_hi': 0.729, 'l_lo': 0.681, 'b05': 0.63, 'b25': 0.604, 'b75': 0.62, 'b95': 0.53}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.5, 1.8]], 'cone_width': [1.392, 1.814, 2.563, 2.759, 3.483, 4.792, 3.581, 3.883, 5.009, 5.16, 7.437, 6.609, 6.095, 5.496]}
- calibration offsets (in sigma): {'05': 0.0165, '10': 0.043, '25': 0.0525, '40': 0.062, '50': 0.035, '60': 0.058, '75': 0.0175, '90': 0.037, '95': 0.0435}
