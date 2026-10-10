# ETH-USD 60s candle generator - report

- generated: 2026-10-10 22:13 UTC
- last closed candle: 2026-10-10 22:13 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.499 (671) [0.449, 0.550] | 0.503 (2875) [0.483, 0.524] | 0.509 (3643) [0.492, 0.526] | 0.499 (671) [0.449, 0.550] | 0.580 (88) | 0.500 | flat -0.029 (noise 0.036) |
| colour_clear | 0.544 (796) | 0.546 (5306) [0.538, 0.554] | 0.508 (23193) [0.502, 0.516] | 0.505 (29544) [0.499, 0.512] | 0.546 (5306) [0.538, 0.554] | 0.539 (735) | 0.500 | up +0.051 (noise 0.010) |
| colour_confident | 0.687 (134) | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.559 (263) | 0.500 | - |
| colour_next | 0.516 (1433) | 0.529 (9975) [0.520, 0.538] | 0.507 (42879) [0.502, 0.512] | 0.506 (54324) [0.501, 0.510] | 0.529 (9975) [0.520, 0.538] | 0.527 (1285) | 0.500 | up +0.024 (noise 0.007) |
| colour_path | 0.501 (20062) | 0.499 (139650) [0.495, 0.503] | 0.501 (600306) [0.499, 0.502] | 0.500 (760536) [0.499, 0.501] | 0.499 (139650) [0.495, 0.503] | 0.499 (17990) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.880 (25) | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.643 (84) | 0.500 | - |
| reversal_k13_next | 0.338 (74) | 0.324 (541) [0.309, 0.337] | 0.311 (2040) [0.297, 0.327] | 0.305 (2646) [0.291, 0.319] | 0.324 (541) [0.309, 0.337] | 0.357 (70) | 0.077 | up +0.057 (noise 0.027) |
| reversal_k13_now | 0.660 (47) | 0.596 (386) [0.555, 0.647] | 0.588 (1486) [0.565, 0.611] | 0.584 (1858) [0.566, 0.604] | 0.596 (386) [0.555, 0.647] | 0.556 (54) | 0.077 | flat +0.015 (noise 0.038) |
| reversal_k3_next | 0.565 (85) | 0.570 (572) [0.541, 0.607] | 0.584 (2351) [0.569, 0.599] | 0.584 (3012) [0.572, 0.598] | 0.570 (572) [0.541, 0.607] | 0.628 (121) | 0.292 | flat -0.008 (noise 0.029) |
| reversal_k3_now | 0.921 (63) | 0.926 (408) [0.917, 0.939] | 0.940 (1711) [0.932, 0.948] | 0.939 (2171) [0.931, 0.946] | 0.926 (408) [0.917, 0.939] | 0.921 (63) | 0.292 | flat -0.023 (noise 0.017) |
| reversal_k5_next | 0.486 (74) | 0.446 (596) [0.419, 0.481] | 0.488 (2110) [0.468, 0.508] | 0.483 (2586) [0.467, 0.500] | 0.446 (596) [0.419, 0.481] | 0.507 (73) | 0.187 | flat -0.028 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.818 (385) [0.787, 0.851] | 0.835 (1578) [0.819, 0.850] | 0.834 (1996) [0.820, 0.848] | 0.818 (385) [0.787, 0.851] | 0.862 (58) | 0.187 | flat -0.052 (noise 0.027) |
| reversal_k8_next | 0.407 (81) | 0.388 (621) [0.361, 0.417] | 0.405 (2121) [0.388, 0.424] | 0.394 (2727) [0.380, 0.410] | 0.388 (621) [0.361, 0.417] | 0.448 (67) | 0.121 | flat +0.005 (noise 0.032) |
| reversal_k8_now | 0.596 (47) | 0.698 (407) [0.656, 0.740] | 0.720 (1585) [0.700, 0.740] | 0.711 (1994) [0.693, 0.729] | 0.698 (407) [0.656, 0.740] | 0.746 (55) | 0.122 | flat -0.041 (noise 0.035) |
| overall | 0.503 (22109) | 0.503 (154212) [0.498, 0.507] | 0.503 (661042) [0.502, 0.505] | 0.503 (837493) [0.501, 0.504] | 0.503 (154212) [0.498, 0.507] | 0.504 (19924) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08077, 0.1218] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5306, 'levels': [{'threshold': 0.08077, 'calls_per_day': 146.8, 'win_rate': 0.6004}, {'threshold': 0.1218, 'calls_per_day': 37.2, 'win_rate': 0.6515}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 10127, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15325 | 0.332 | 0.516 (15068) | 0.598 (966) | 0.778 (2470) |
| volatility: normal | 15325 | 0.360 | 0.511 (15254) | 0.622 (180) | 0.769 (2181) |
| volatility: wild | 15323 | 0.373 | 0.495 (15279) | 0.667 (66) | 0.778 (2111) |
| session: Asia 00-08 | 15360 | 0.352 | 0.509 (15252) | 0.596 (421) | 0.779 (2185) |
| session: Europe 08-13 | 9600 | 0.349 | 0.506 (9511) | 0.596 (282) | 0.766 (1513) |
| session: US 13-21 | 15360 | 0.365 | 0.505 (15252) | 0.588 (325) | 0.783 (2261) |
| session: late 21-24 | 5653 | 0.349 | 0.511 (5586) | 0.674 (184) | 0.761 (803) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.355 | 0.390 | 0.290 | 0.290 | 0.567 | 0.291 | 0.419 | 0.890 |
| 6h | 360 | 0.329 | 0.326 | 0.241 | 0.256 | 0.527 | 0.252 | 0.405 | 1.067 |
| 24h | 1440 | 0.320 | 0.306 | 0.231 | 0.252 | 0.528 | 0.253 | 0.388 | 1.245 |
| 7d | 10080 | 0.351 | 0.345 | 0.271 | 0.296 | 0.530 | 0.257 | 0.446 | 1.214 |
| 30d | 43200 | 0.355 | 0.353 | 0.277 | 0.306 | 0.508 | 0.248 | 0.462 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.355 / 0.567 / 0.850; 2: 0.335 / 0.467 / 0.833; 3: 0.354 / 0.550 / 0.883; 4: 0.345 / 0.483 / 0.950; 5: 0.346 / 0.550 / 0.983; 6: 0.323 / 0.483 / 1.000; 7: 0.328 / 0.517 / 1.000; 8: 0.303 / 0.450 / 1.000; 9: 0.326 / 0.483 / 1.000; 10: 0.349 / 0.583 / 1.000; 11: 0.347 / 0.567 / 1.000; 12: 0.328 / 0.550 / 1.000; 13: 0.313 / 0.483 / 1.000; 14: 0.333 / 0.600 / 1.000; 15: 0.321 / 0.517 / 1.000
- 6h: 1: 0.329 / 0.527 / 0.883; 2: 0.312 / 0.450 / 0.925; 3: 0.316 / 0.493 / 0.933; 4: 0.323 / 0.504 / 0.975; 5: 0.322 / 0.507 / 0.972; 6: 0.312 / 0.476 / 0.989; 7: 0.307 / 0.493 / 0.997; 8: 0.305 / 0.470 / 0.975; 9: 0.316 / 0.496 / 0.975; 10: 0.319 / 0.510 / 0.986; 11: 0.316 / 0.504 / 0.981; 12: 0.318 / 0.516 / 1.000; 13: 0.315 / 0.504 / 0.994; 14: 0.315 / 0.499 / 0.989; 15: 0.313 / 0.487 / 0.978
- 24h: 1: 0.320 / 0.528 / 0.877; 2: 0.307 / 0.483 / 0.894; 3: 0.305 / 0.506 / 0.907; 4: 0.304 / 0.495 / 0.893; 5: 0.314 / 0.529 / 0.894; 6: 0.302 / 0.483 / 0.891; 7: 0.302 / 0.497 / 0.886; 8: 0.302 / 0.493 / 0.893; 9: 0.303 / 0.494 / 0.891; 10: 0.308 / 0.513 / 0.888; 11: 0.302 / 0.487 / 0.887; 12: 0.306 / 0.503 / 0.881; 13: 0.304 / 0.503 / 0.886; 14: 0.307 / 0.516 / 0.889; 15: 0.303 / 0.489 / 0.892
- 7d: 1: 0.351 / 0.530 / 0.896; 2: 0.340 / 0.499 / 0.901; 3: 0.342 / 0.510 / 0.900; 4: 0.339 / 0.504 / 0.900; 5: 0.339 / 0.502 / 0.901; 6: 0.336 / 0.496 / 0.900; 7: 0.336 / 0.502 / 0.900; 8: 0.336 / 0.493 / 0.901; 9: 0.333 / 0.489 / 0.901; 10: 0.336 / 0.504 / 0.900; 11: 0.334 / 0.493 / 0.899; 12: 0.335 / 0.501 / 0.898; 13: 0.336 / 0.504 / 0.899; 14: 0.335 / 0.503 / 0.900; 15: 0.336 / 0.497 / 0.900
- 30d: 1: 0.355 / 0.508 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.500 / 0.900; 5: 0.349 / 0.504 / 0.900; 6: 0.347 / 0.501 / 0.900; 7: 0.347 / 0.504 / 0.899; 8: 0.347 / 0.503 / 0.900; 9: 0.344 / 0.496 / 0.900; 10: 0.346 / 0.504 / 0.900; 11: 0.345 / 0.501 / 0.900; 12: 0.345 / 0.502 / 0.899; 13: 0.344 / 0.501 / 0.899; 14: 0.343 / 0.497 / 0.899; 15: 0.343 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.148 (body 0.117, range 0.180); 'price stays where it was' would score 0.217; colour right 0.617; typical miss of the close 4.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.122 (body 0.090, range 0.155); 'price stays where it was' would score 0.142; colour right 0.513; typical miss of the close 4.4 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.118 (body 0.088, range 0.149); 'price stays where it was' would score 0.120; colour right 0.494; typical miss of the close 3.8 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.117 (body 0.081, range 0.154); 'price stays where it was' would score 0.122; colour right 0.497; typical miss of the close 6.1 bp; chain ended on the right side 0.504 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 3.9; 2: 0.200 / 4.3; 3: 0.167 / 5.9; 4: 0.133 / 6.5; 5: 0.121 / 7.1; 6: 0.111 / 7.7; 7: 0.101 / 8.2; 8: 0.093 / 8.5; 9: 0.086 / 8.8; 10: 0.080 / 9.4; 11: 0.076 / 10.0; 12: 0.075 / 10.5; 13: 0.063 / 10.8; 14: 0.065 / 10.9; 15: 0.060 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 99007, probability skill vs chance 0.2314, widened contest next: False
  - now: threshold 0.8423, hit rate recent 0.92 / long run 0.9322
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.311, naive rule 0.539, lift 3.03x
    - 24h: 69 calls (69 a day), hit rate 0.913, chance 0.314, naive rule 0.532, lift 2.91x
    - 7d: 417 calls (60 a day), hit rate 0.926, chance 0.296, naive rule 0.494, lift 3.13x
    - 30d: 1717 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.483, lift 3.22x
  - next: threshold 0.5426, hit rate recent 0.6585 / long run 0.5862
    - 6h: 43 calls (174 a day), hit rate 0.721, chance 0.311, lift 2.32x
    - 24h: 126 calls (126 a day), hit rate 0.635, chance 0.314, lift 2.02x
    - 7d: 557 calls (80 a day), hit rate 0.592, chance 0.296, lift 2.00x
    - 30d: 2382 calls (79 a day), hit rate 0.586, chance 0.292, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 537, 0.517; 0.40: 485, 0.563; 0.45: 418, 0.629; 0.50: 365, 0.683; 0.55: 320, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 138, 0.873; 0.80: 97, 0.913; 0.85: 49, 0.948; 0.90: 2, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.458; 0.40: 412, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.553; 0.55: 92, 0.582; 0.60: 14, 0.603; 0.65: 1, 0.682
- **K=5**: model 1791590400, labels learned 99005, probability skill vs chance 0.2202, widened contest next: False
  - now: threshold 0.7129, hit rate recent 0.8464 / long run 0.8309
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.214, naive rule 0.460, lift 4.42x
    - 24h: 61 calls (61 a day), hit rate 0.852, chance 0.197, naive rule 0.436, lift 4.33x
    - 7d: 385 calls (55 a day), hit rate 0.826, chance 0.191, naive rule 0.400, lift 4.33x
    - 30d: 1587 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.47x
  - next: threshold 0.4642, hit rate recent 0.507 / long run 0.4714
    - 6h: 19 calls (78 a day), hit rate 0.526, chance 0.214, lift 2.46x
    - 24h: 76 calls (76 a day), hit rate 0.500, chance 0.197, lift 2.54x
    - 7d: 493 calls (70 a day), hit rate 0.471, chance 0.191, lift 2.46x
    - 30d: 2096 calls (70 a day), hit rate 0.484, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 428, 0.415; 0.35: 364, 0.471; 0.40: 294, 0.541; 0.45: 240, 0.601; 0.50: 186, 0.659; 0.55: 140, 0.705; 0.60: 109, 0.748; 0.65: 84, 0.795; 0.70: 62, 0.825; 0.75: 34, 0.864; 0.80: 10, 0.880
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 253, 0.423; 0.40: 165, 0.451; 0.45: 83, 0.473; 0.50: 20, 0.514; 0.55: 2, 0.540
- **K=8**: model 1791417600, labels learned 99002, probability skill vs chance 0.2143, widened contest next: False
  - now: threshold 0.5678, hit rate recent 0.706 / long run 0.7084
    - 6h: 15 calls (62 a day), hit rate 0.867, chance 0.140, naive rule 0.403, lift 6.19x
    - 24h: 59 calls (59 a day), hit rate 0.712, chance 0.132, naive rule 0.387, lift 5.39x
    - 7d: 416 calls (59 a day), hit rate 0.692, chance 0.124, naive rule 0.338, lift 5.57x
    - 30d: 1583 calls (53 a day), hit rate 0.720, chance 0.122, naive rule 0.328, lift 5.91x
  - next: threshold 0.3693, hit rate recent 0.4088 / long run 0.398
    - 6h: 18 calls (74 a day), hit rate 0.333, chance 0.140, lift 2.38x
    - 24h: 71 calls (71 a day), hit rate 0.451, chance 0.132, lift 3.41x
    - 7d: 614 calls (88 a day), hit rate 0.397, chance 0.124, lift 3.20x
    - 30d: 2100 calls (70 a day), hit rate 0.407, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 268, 0.406; 0.35: 202, 0.481; 0.40: 155, 0.543; 0.45: 122, 0.589; 0.50: 93, 0.633; 0.55: 67, 0.688; 0.60: 46, 0.728; 0.65: 24, 0.767; 0.70: 9, 0.812; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 184, 0.350; 0.35: 112, 0.388; 0.40: 47, 0.415; 0.45: 10, 0.441; 0.50: 1, 0.405
- **K=13**: model 1791504000, labels learned 98997, probability skill vs chance 0.1837, widened contest next: False
  - now: threshold 0.4322, hit rate recent 0.5867 / long run 0.5854
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.103, naive rule 0.354, lift 6.25x
    - 24h: 58 calls (59 a day), hit rate 0.534, chance 0.096, naive rule 0.340, lift 5.58x
    - 7d: 398 calls (57 a day), hit rate 0.573, chance 0.080, naive rule 0.280, lift 7.18x
    - 30d: 1490 calls (50 a day), hit rate 0.585, chance 0.077, naive rule 0.269, lift 7.55x
  - next: threshold 0.2874, hit rate recent 0.3426 / long run 0.3159
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.103, lift 3.24x
    - 24h: 76 calls (77 a day), hit rate 0.355, chance 0.096, lift 3.71x
    - 7d: 511 calls (73 a day), hit rate 0.329, chance 0.080, lift 4.12x
    - 30d: 2049 calls (68 a day), hit rate 0.311, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.445; 0.35: 87, 0.506; 0.40: 62, 0.554; 0.45: 43, 0.608; 0.50: 27, 0.632; 0.55: 14, 0.683; 0.60: 5, 0.705; 0.65: 1, 0.735
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.324; 0.35: 15, 0.350; 0.40: 3, 0.341; 0.45: 0, 0.286

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.328 | 6.99% | 0.867 | 0.350 | 0.241 | 0.650 | 0.462 |
| 6h | 7.435 | 1.35% | 0.883 | 0.431 | 0.250 | 0.481 | 0.334 |
| 24h | 6.384 | 7.44% | 0.889 | 0.486 | 0.251 | 0.469 | 0.487 |
| 7d | 11.026 | 5.02% | 0.900 | 0.498 | 0.251 | 0.494 | 0.673 |
| 30d | 13.970 | 4.53% | 0.900 | 0.500 | 0.251 | 0.497 | 0.701 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.105 | 10.525 | 10.466 | 10.659 | 10.552 | 10.355 | 10.295 | 10.480 | 10.432 | 10.328 |
| 6h | 7.537 | 7.450 | 7.438 | 7.512 | 7.514 | 7.472 | 7.435 | 7.440 | 7.430 | 7.435 |
| 24h | 6.897 | 6.434 | 6.465 | 6.426 | 6.507 | 6.523 | 6.385 | 6.364 | 6.377 | 6.384 |
| 7d | 11.610 | 11.130 | 11.101 | 11.077 | 11.221 | 11.236 | 11.024 | 11.007 | 11.008 | 11.026 |
| 30d | 14.633 | 14.101 | 14.054 | 14.002 | 14.240 | 14.201 | 13.973 | 13.943 | 13.944 | 13.970 |

## Next candle

- candle starting 2026-10-10 22:13 UTC, last close 2507.11
- P(up) 0.5332, return quantiles (bp): {'05': -6.654, '10': -5.047, '25': -2.612, '40': -0.586, '50': 0.283, '60': 1.216, '75': 2.669, '90': 4.845, '95': 6.478}
- changepoint probability 0.03, regime age 36.4 min
- agent weights: empirical 0.005, ewma 0.119, garch 0.132, har 0.101, bocpd 0.052, hmm 0.064, online_qr 0.240, lgbm 0.287

## Learning log

- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.22, 4.82, 15.52], current probabilities: [0.028, 0.963, 0.01]
- live generator: {'versions': 60, 'latest_effective': '2026-10-10 22:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.224, 'l_abs': 0.661, 'l_hi': 0.722, 'l_lo': 0.681, 'b05': 0.639, 'b25': 0.625, 'b75': 0.598, 'b95': 0.517}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.511, 1.891, 2.061, 2.263, 2.534, 3.284, 2.823, 3.061, 3.718, 3.987, 4.995, 4.62, 4.435, 4.332]}
- calibration offsets (in sigma): {'05': -0.034, '10': -0.048, '25': -0.04, '40': 0.078, '50': 0.09, '60': 0.122, '75': 0.1, '90': 0.038, '95': 0.044}
