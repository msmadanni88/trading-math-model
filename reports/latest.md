# ETH-USD 60s candle generator - report

- generated: 2026-10-10 14:41 UTC
- last closed candle: 2026-10-10 14:41 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.499 (671) [0.449, 0.550] | 0.503 (2875) [0.483, 0.524] | 0.509 (3643) [0.492, 0.526] | 0.499 (671) [0.449, 0.550] | 0.569 (58) | 0.500 | flat -0.029 (noise 0.036) |
| colour_clear | 0.544 (796) | 0.546 (5306) [0.538, 0.554] | 0.508 (23193) [0.502, 0.516] | 0.505 (29544) [0.499, 0.512] | 0.546 (5306) [0.538, 0.554] | 0.534 (487) | 0.500 | up +0.051 (noise 0.010) |
| colour_confident | 0.687 (134) | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.567 (210) | 0.500 | - |
| colour_next | 0.516 (1433) | 0.529 (9975) [0.520, 0.538] | 0.507 (42879) [0.502, 0.512] | 0.506 (54324) [0.501, 0.510] | 0.529 (9975) [0.520, 0.538] | 0.527 (844) | 0.500 | up +0.024 (noise 0.007) |
| colour_path | 0.501 (20062) | 0.499 (139650) [0.495, 0.503] | 0.501 (600306) [0.499, 0.502] | 0.500 (760536) [0.499, 0.501] | 0.499 (139650) [0.495, 0.503] | 0.499 (11816) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.880 (25) | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.635 (74) | 0.500 | - |
| reversal_k13_next | 0.338 (74) | 0.324 (541) [0.309, 0.337] | 0.311 (2040) [0.297, 0.327] | 0.305 (2646) [0.291, 0.319] | 0.324 (541) [0.309, 0.337] | 0.392 (51) | 0.077 | up +0.057 (noise 0.027) |
| reversal_k13_now | 0.660 (47) | 0.596 (386) [0.555, 0.647] | 0.588 (1486) [0.565, 0.611] | 0.584 (1858) [0.566, 0.604] | 0.596 (386) [0.555, 0.647] | 0.576 (33) | 0.077 | flat +0.015 (noise 0.038) |
| reversal_k3_next | 0.565 (85) | 0.570 (572) [0.541, 0.607] | 0.584 (2351) [0.569, 0.599] | 0.584 (3012) [0.572, 0.598] | 0.570 (572) [0.541, 0.607] | 0.549 (71) | 0.292 | flat -0.008 (noise 0.029) |
| reversal_k3_now | 0.921 (63) | 0.926 (408) [0.917, 0.939] | 0.940 (1711) [0.932, 0.948] | 0.939 (2171) [0.931, 0.946] | 0.926 (408) [0.917, 0.939] | 0.897 (39) | 0.292 | flat -0.023 (noise 0.017) |
| reversal_k5_next | 0.486 (74) | 0.446 (596) [0.419, 0.481] | 0.488 (2110) [0.468, 0.508] | 0.483 (2586) [0.467, 0.500] | 0.446 (596) [0.419, 0.481] | 0.500 (50) | 0.187 | flat -0.028 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.818 (385) [0.787, 0.851] | 0.835 (1578) [0.819, 0.850] | 0.834 (1996) [0.820, 0.848] | 0.818 (385) [0.787, 0.851] | 0.818 (33) | 0.187 | flat -0.052 (noise 0.027) |
| reversal_k8_next | 0.407 (81) | 0.388 (621) [0.361, 0.417] | 0.405 (2121) [0.388, 0.424] | 0.394 (2727) [0.380, 0.410] | 0.388 (621) [0.361, 0.417] | 0.500 (48) | 0.121 | flat +0.005 (noise 0.032) |
| reversal_k8_now | 0.596 (47) | 0.698 (407) [0.656, 0.740] | 0.720 (1585) [0.700, 0.740] | 0.711 (1994) [0.693, 0.729] | 0.698 (407) [0.656, 0.740] | 0.714 (35) | 0.122 | flat -0.041 (noise 0.035) |
| overall | 0.503 (22109) | 0.503 (154212) [0.498, 0.507] | 0.503 (661042) [0.502, 0.505] | 0.503 (837493) [0.501, 0.504] | 0.503 (154212) [0.498, 0.507] | 0.504 (13078) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08018, 0.1206] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5316, 'levels': [{'threshold': 0.08018, 'calls_per_day': 149.1, 'win_rate': 0.6098}, {'threshold': 0.1206, 'calls_per_day': 38.3, 'win_rate': 0.6753}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 9686, 'rate': 0.5309}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15174 | 0.333 | 0.516 (14928) | 0.600 (917) | 0.777 (2436) |
| volatility: normal | 15173 | 0.360 | 0.510 (15102) | 0.636 (176) | 0.769 (2140) |
| volatility: wild | 15174 | 0.374 | 0.496 (15130) | 0.667 (66) | 0.779 (2096) |
| session: Asia 00-08 | 15360 | 0.352 | 0.509 (15252) | 0.596 (421) | 0.779 (2185) |
| session: Europe 08-13 | 9600 | 0.349 | 0.506 (9511) | 0.596 (282) | 0.766 (1513) |
| session: US 13-21 | 14981 | 0.366 | 0.505 (14883) | 0.603 (277) | 0.781 (2182) |
| session: late 21-24 | 5580 | 0.349 | 0.510 (5514) | 0.670 (179) | 0.761 (792) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.297 | 0.306 | 0.209 | 0.209 | 0.450 | 0.202 | 0.393 | 1.025 |
| 6h | 360 | 0.287 | 0.273 | 0.216 | 0.230 | 0.506 | 0.235 | 0.338 | 1.245 |
| 24h | 1440 | 0.330 | 0.319 | 0.241 | 0.265 | 0.523 | 0.251 | 0.409 | 1.200 |
| 7d | 10080 | 0.350 | 0.343 | 0.270 | 0.295 | 0.531 | 0.256 | 0.445 | 1.228 |
| 30d | 43200 | 0.355 | 0.353 | 0.278 | 0.306 | 0.507 | 0.248 | 0.463 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.297 / 0.450 / 0.767; 2: 0.294 / 0.433 / 0.817; 3: 0.310 / 0.483 / 0.817; 4: 0.290 / 0.483 / 0.700; 5: 0.320 / 0.550 / 0.650; 6: 0.287 / 0.417 / 0.533; 7: 0.298 / 0.500 / 0.450; 8: 0.280 / 0.400 / 0.533; 9: 0.277 / 0.533 / 0.533; 10: 0.271 / 0.483 / 0.483; 11: 0.283 / 0.433 / 0.450; 12: 0.294 / 0.533 / 0.383; 13: 0.293 / 0.517 / 0.450; 14: 0.281 / 0.467 / 0.533; 15: 0.286 / 0.417 / 0.567
- 6h: 1: 0.287 / 0.506 / 0.833; 2: 0.272 / 0.455 / 0.853; 3: 0.282 / 0.530 / 0.831; 4: 0.268 / 0.485 / 0.781; 5: 0.283 / 0.530 / 0.792; 6: 0.267 / 0.461 / 0.750; 7: 0.270 / 0.473 / 0.708; 8: 0.265 / 0.479 / 0.772; 9: 0.275 / 0.521 / 0.772; 10: 0.282 / 0.539 / 0.728; 11: 0.262 / 0.449 / 0.728; 12: 0.267 / 0.509 / 0.672; 13: 0.272 / 0.509 / 0.697; 14: 0.266 / 0.488 / 0.725; 15: 0.272 / 0.491 / 0.744
- 24h: 1: 0.330 / 0.523 / 0.883; 2: 0.321 / 0.508 / 0.887; 3: 0.317 / 0.503 / 0.885; 4: 0.314 / 0.492 / 0.872; 5: 0.321 / 0.504 / 0.874; 6: 0.315 / 0.487 / 0.869; 7: 0.310 / 0.481 / 0.858; 8: 0.318 / 0.508 / 0.870; 9: 0.311 / 0.487 / 0.874; 10: 0.319 / 0.515 / 0.867; 11: 0.314 / 0.494 / 0.867; 12: 0.318 / 0.503 / 0.857; 13: 0.317 / 0.502 / 0.861; 14: 0.318 / 0.518 / 0.867; 15: 0.315 / 0.485 / 0.872
- 7d: 1: 0.350 / 0.531 / 0.895; 2: 0.339 / 0.501 / 0.898; 3: 0.341 / 0.510 / 0.898; 4: 0.338 / 0.505 / 0.897; 5: 0.337 / 0.500 / 0.897; 6: 0.335 / 0.495 / 0.897; 7: 0.334 / 0.500 / 0.896; 8: 0.335 / 0.493 / 0.897; 9: 0.331 / 0.489 / 0.897; 10: 0.335 / 0.506 / 0.896; 11: 0.333 / 0.493 / 0.896; 12: 0.334 / 0.502 / 0.894; 13: 0.335 / 0.505 / 0.895; 14: 0.334 / 0.502 / 0.896; 15: 0.334 / 0.495 / 0.896
- 30d: 1: 0.355 / 0.507 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.349 / 0.500 / 0.899; 5: 0.349 / 0.504 / 0.899; 6: 0.348 / 0.502 / 0.899; 7: 0.347 / 0.504 / 0.899; 8: 0.347 / 0.503 / 0.899; 9: 0.344 / 0.495 / 0.899; 10: 0.346 / 0.504 / 0.899; 11: 0.345 / 0.500 / 0.899; 12: 0.345 / 0.502 / 0.899; 13: 0.345 / 0.501 / 0.899; 14: 0.344 / 0.497 / 0.899; 15: 0.343 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.038 (body 0.021, range 0.055); 'price stays where it was' would score 0.035; colour right 0.350; typical miss of the close 6.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.091 (body 0.067, range 0.115); 'price stays where it was' would score 0.079; colour right 0.464; typical miss of the close 3.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.124 (body 0.088, range 0.160); 'price stays where it was' would score 0.118; colour right 0.486; typical miss of the close 4.1 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.116 (body 0.080, range 0.152); 'price stays where it was' would score 0.120; colour right 0.497; typical miss of the close 6.0 bp; chain ended on the right side 0.501 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.9 bp; chain ended on the right side 0.506 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.200 / 4.4; 3: 0.167 / 6.0; 4: 0.131 / 6.5; 5: 0.120 / 7.2; 6: 0.111 / 7.8; 7: 0.101 / 8.3; 8: 0.093 / 8.5; 9: 0.086 / 8.9; 10: 0.080 / 9.5; 11: 0.075 / 10.2; 12: 0.075 / 10.6; 13: 0.063 / 10.9; 14: 0.065 / 11.0; 15: 0.061 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 98555, probability skill vs chance 0.2213, widened contest next: False
  - now: threshold 0.8419, hit rate recent 0.9051 / long run 0.9312
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.321, naive rule 0.532, lift 2.87x
    - 24h: 64 calls (64 a day), hit rate 0.875, chance 0.318, naive rule 0.536, lift 2.75x
    - 7d: 412 calls (59 a day), hit rate 0.922, chance 0.296, naive rule 0.492, lift 3.11x
    - 30d: 1708 calls (57 a day), hit rate 0.940, chance 0.291, naive rule 0.482, lift 3.23x
  - next: threshold 0.5284, hit rate recent 0.5521 / long run 0.5728
    - 6h: 30 calls (122 a day), hit rate 0.600, chance 0.321, lift 1.87x
    - 24h: 106 calls (106 a day), hit rate 0.585, chance 0.318, lift 1.84x
    - 7d: 562 calls (80 a day), hit rate 0.578, chance 0.296, lift 1.95x
    - 30d: 2356 calls (79 a day), hit rate 0.584, chance 0.291, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.493; 0.35: 537, 0.516; 0.40: 485, 0.562; 0.45: 418, 0.629; 0.50: 365, 0.683; 0.55: 320, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.802; 0.70: 181, 0.834; 0.75: 138, 0.873; 0.80: 96, 0.913; 0.85: 49, 0.948; 0.90: 2, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.423; 0.35: 498, 0.457; 0.40: 412, 0.486; 0.45: 316, 0.518; 0.50: 206, 0.552; 0.55: 91, 0.582; 0.60: 13, 0.597; 0.65: 1, 0.682
- **K=5**: model 1791590400, labels learned 98553, probability skill vs chance 0.2104, widened contest next: False
  - now: threshold 0.7127, hit rate recent 0.8081 / long run 0.8272
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.203, naive rule 0.463, lift 4.49x
    - 24h: 50 calls (50 a day), hit rate 0.800, chance 0.196, naive rule 0.422, lift 4.08x
    - 7d: 380 calls (54 a day), hit rate 0.816, chance 0.190, naive rule 0.396, lift 4.29x
    - 30d: 1573 calls (52 a day), hit rate 0.835, chance 0.187, naive rule 0.391, lift 4.47x
  - next: threshold 0.4633, hit rate recent 0.4919 / long run 0.4693
    - 6h: 25 calls (102 a day), hit rate 0.560, chance 0.203, lift 2.76x
    - 24h: 77 calls (77 a day), hit rate 0.506, chance 0.196, lift 2.58x
    - 7d: 531 calls (76 a day), hit rate 0.463, chance 0.190, lift 2.43x
    - 30d: 2097 calls (70 a day), hit rate 0.486, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 429, 0.414; 0.35: 364, 0.470; 0.40: 294, 0.540; 0.45: 240, 0.600; 0.50: 186, 0.658; 0.55: 140, 0.704; 0.60: 109, 0.748; 0.65: 84, 0.793; 0.70: 62, 0.825; 0.75: 34, 0.865; 0.80: 9, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.385; 0.35: 252, 0.423; 0.40: 165, 0.451; 0.45: 83, 0.473; 0.50: 20, 0.511; 0.55: 2, 0.540
- **K=8**: model 1791417600, labels learned 98550, probability skill vs chance 0.2046, widened contest next: True
  - now: threshold 0.5817, hit rate recent 0.6663 / long run 0.7053
    - 6h: 14 calls (58 a day), hit rate 0.786, chance 0.136, naive rule 0.394, lift 5.79x
    - 24h: 57 calls (57 a day), hit rate 0.667, chance 0.128, naive rule 0.363, lift 5.22x
    - 7d: 410 calls (59 a day), hit rate 0.688, chance 0.123, naive rule 0.334, lift 5.59x
    - 30d: 1580 calls (53 a day), hit rate 0.720, chance 0.122, naive rule 0.327, lift 5.92x
  - next: threshold 0.3694, hit rate recent 0.439 / long run 0.4006
    - 6h: 23 calls (95 a day), hit rate 0.435, chance 0.136, lift 3.20x
    - 24h: 74 calls (75 a day), hit rate 0.473, chance 0.128, lift 3.71x
    - 7d: 625 calls (89 a day), hit rate 0.398, chance 0.123, lift 3.24x
    - 30d: 2109 calls (70 a day), hit rate 0.408, chance 0.122, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 268, 0.406; 0.35: 203, 0.481; 0.40: 156, 0.542; 0.45: 122, 0.590; 0.50: 93, 0.634; 0.55: 67, 0.688; 0.60: 45, 0.729; 0.65: 24, 0.769; 0.70: 9, 0.819; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 184, 0.350; 0.35: 113, 0.389; 0.40: 47, 0.415; 0.45: 10, 0.436; 0.50: 1, 0.405
- **K=13**: model 1791504000, labels learned 98545, probability skill vs chance 0.1857, widened contest next: False
  - now: threshold 0.4298, hit rate recent 0.6089 / long run 0.5876
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.101, naive rule 0.343, lift 5.75x
    - 24h: 49 calls (50 a day), hit rate 0.612, chance 0.091, naive rule 0.323, lift 6.74x
    - 7d: 391 calls (56 a day), hit rate 0.583, chance 0.079, naive rule 0.278, lift 7.35x
    - 30d: 1485 calls (50 a day), hit rate 0.587, chance 0.077, naive rule 0.269, lift 7.58x
  - next: threshold 0.2896, hit rate recent 0.3678 / long run 0.3176
    - 6h: 20 calls (83 a day), hit rate 0.400, chance 0.101, lift 3.94x
    - 24h: 77 calls (78 a day), hit rate 0.390, chance 0.091, lift 4.29x
    - 7d: 533 calls (76 a day), hit rate 0.332, chance 0.079, lift 4.19x
    - 30d: 2052 calls (68 a day), hit rate 0.313, chance 0.077, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.444; 0.35: 87, 0.506; 0.40: 62, 0.556; 0.45: 43, 0.611; 0.50: 27, 0.634; 0.55: 14, 0.687; 0.60: 5, 0.717; 0.65: 1, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.326; 0.35: 15, 0.351; 0.40: 3, 0.341; 0.45: 0, 0.267

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.170 | 5.87% | 0.850 | 0.483 | 0.252 | 0.433 | 0.723 |
| 6h | 5.584 | 9.89% | 0.864 | 0.508 | 0.251 | 0.458 | 0.661 |
| 24h | 7.382 | 7.22% | 0.891 | 0.511 | 0.251 | 0.485 | 0.654 |
| 7d | 10.912 | 5.07% | 0.899 | 0.500 | 0.251 | 0.496 | 0.677 |
| 30d | 14.036 | 4.52% | 0.900 | 0.500 | 0.251 | 0.497 | 0.699 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.803 | 10.317 | 10.178 | 10.379 | 9.802 | 10.283 | 10.464 | 10.185 | 10.213 | 10.170 |
| 6h | 6.197 | 5.624 | 5.675 | 5.673 | 5.596 | 5.804 | 5.628 | 5.570 | 5.587 | 5.584 |
| 24h | 7.956 | 7.430 | 7.466 | 7.427 | 7.528 | 7.553 | 7.391 | 7.355 | 7.373 | 7.382 |
| 7d | 11.496 | 11.015 | 10.988 | 10.963 | 11.105 | 11.136 | 10.910 | 10.894 | 10.894 | 10.912 |
| 30d | 14.701 | 14.167 | 14.121 | 14.068 | 14.306 | 14.268 | 14.039 | 14.010 | 14.010 | 14.036 |

## Next candle

- candle starting 2026-10-10 14:41 UTC, last close 2513.55
- P(up) 0.5132, return quantiles (bp): {'05': -12.257, '10': -9.159, '25': -4.59, '40': -1.192, '50': 0.178, '60': 1.763, '75': 4.798, '90': 9.448, '95': 13.525}
- changepoint probability 0.0139, regime age 14.8 min
- agent weights: empirical 0.003, ewma 0.134, garch 0.087, har 0.123, bocpd 0.130, hmm 0.027, online_qr 0.172, lgbm 0.324

## Learning log

- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- HMM volatility states (sd, bp per minute): [2.22, 4.82, 15.52], current probabilities: [0.0, 0.535, 0.465]
- live generator: {'versions': 60, 'latest_effective': '2026-10-10 14:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.435, 'l_abs': 0.678, 'l_hi': 0.739, 'l_lo': 0.696, 'b05': 0.62, 'b25': 0.635, 'b75': 0.599, 'b95': 0.536}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [2.047, 2.777, 4.167, 4.396, 5.441, 7.637, 5.594, 5.945, 7.67, 7.901, 11.161, 9.919, 8.967, 8.085]}
- calibration offsets (in sigma): {'05': 0.02, '10': 0.04, '25': 0.06, '40': 0.13, '50': 0.04, '60': 0.03, '75': 0.01, '90': 0.03, '95': 0.08}
