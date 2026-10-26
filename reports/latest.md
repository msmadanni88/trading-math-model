# ETH-USD 60s candle generator - report

- generated: 2026-10-26 04:22 UTC
- last closed candle: 2026-10-26 04:22 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.646 (96) | 0.548 (672) [0.509, 0.588] | 0.525 (2876) [0.506, 0.545] | 0.517 (5178) [0.503, 0.532] | 0.524 (2206) [0.501, 0.548] | 0.471 (17) | 0.500 | flat +0.021 (noise 0.030) |
| colour_clear | 0.534 (802) | 0.550 (5686) [0.543, 0.559] | 0.535 (23445) [0.527, 0.542] | 0.518 (42293) [0.511, 0.524] | 0.546 (18055) [0.541, 0.551] | 0.518 (164) | 0.500 | flat +0.005 (noise 0.009) |
| colour_confident | 0.578 (268) | 0.607 (1411) [0.590, 0.627] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.613 (31) | 0.500 | flat +0.023 (noise 0.024) |
| colour_next | 0.523 (1434) | 0.535 (10043) [0.528, 0.541] | 0.524 (42849) [0.520, 0.529] | 0.513 (77190) [0.509, 0.517] | 0.530 (32841) [0.525, 0.534] | 0.511 (260) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.506 (20076) | 0.501 (140602) [0.498, 0.503] | 0.501 (599886) [0.499, 0.502] | 0.501 (1080660) [0.500, 0.502] | 0.500 (459774) [0.499, 0.502] | 0.507 (3640) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.589 (107) | 0.628 (406) [0.603, 0.666] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.700 (10) | 0.500 | flat +0.012 (noise 0.048) |
| reversal_k13_next | 0.364 (66) | 0.318 (466) [0.295, 0.338] | 0.304 (2171) [0.292, 0.315] | 0.307 (3684) [0.297, 0.318] | 0.318 (1579) [0.307, 0.329] | 0.300 (10) | 0.077 | flat +0.022 (noise 0.031) |
| reversal_k13_now | 0.600 (55) | 0.552 (357) [0.510, 0.599] | 0.569 (1575) [0.549, 0.590] | 0.574 (2706) [0.558, 0.590] | 0.566 (1234) [0.543, 0.590] | 0.615 (13) | 0.077 | flat +0.009 (noise 0.037) |
| reversal_k3_next | 0.588 (80) | 0.593 (678) [0.563, 0.626] | 0.580 (2811) [0.566, 0.594] | 0.584 (4642) [0.573, 0.595] | 0.580 (2202) [0.566, 0.595] | 0.647 (17) | 0.293 | flat +0.027 (noise 0.026) |
| reversal_k3_now | 0.870 (46) | 0.936 (388) [0.911, 0.958] | 0.935 (1685) [0.926, 0.945] | 0.937 (3069) [0.930, 0.944] | 0.931 (1306) [0.920, 0.942] | 1.000 (7) | 0.293 | flat -0.003 (noise 0.021) |
| reversal_k5_next | 0.496 (137) | 0.470 (924) [0.441, 0.494] | 0.464 (2951) [0.450, 0.478] | 0.476 (4443) [0.464, 0.489] | 0.462 (2453) [0.447, 0.477] | 0.450 (20) | 0.186 | flat +0.012 (noise 0.024) |
| reversal_k5_now | 0.837 (49) | 0.818 (363) [0.807, 0.829] | 0.831 (1563) [0.817, 0.844] | 0.830 (2820) [0.819, 0.841] | 0.820 (1209) [0.806, 0.833] | 1.000 (7) | 0.187 | flat +0.008 (noise 0.029) |
| reversal_k8_next | 0.403 (119) | 0.378 (759) [0.359, 0.396] | 0.382 (2589) [0.370, 0.395] | 0.389 (4306) [0.378, 0.401] | 0.382 (2200) [0.368, 0.396] | 0.467 (15) | 0.120 | flat +0.000 (noise 0.026) |
| reversal_k8_now | 0.729 (48) | 0.665 (337) [0.621, 0.710] | 0.698 (1525) [0.677, 0.718] | 0.702 (2787) [0.686, 0.717] | 0.687 (1200) [0.665, 0.710] | 0.750 (8) | 0.121 | flat -0.016 (noise 0.036) |
| overall | 0.509 (22206) | 0.504 (155589) [0.502, 0.507] | 0.504 (662481) [0.503, 0.506] | 0.503 (1191485) [0.502, 0.504] | 0.504 (508204) [0.502, 0.506] | 0.509 (4014) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07718, 0.1147] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5349, 'levels': [{'threshold': 0.07718, 'calls_per_day': 149.0, 'win_rate': 0.616}, {'threshold': 0.1147, 'calls_per_day': 38.6, 'win_rate': 0.6458}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 31962, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14968 | 0.336 | 0.524 (14725) | 0.587 (1715) | 0.764 (2480) |
| volatility: normal | 14967 | 0.364 | 0.524 (14896) | 0.608 (1207) | 0.753 (2212) |
| volatility: wild | 14967 | 0.379 | 0.519 (14926) | 0.637 (570) | 0.776 (1875) |
| session: Asia 00-08 | 15142 | 0.358 | 0.528 (15038) | 0.607 (1251) | 0.763 (2177) |
| session: Europe 08-13 | 9300 | 0.355 | 0.524 (9213) | 0.598 (858) | 0.762 (1471) |
| session: US 13-21 | 14880 | 0.367 | 0.519 (14778) | 0.599 (867) | 0.775 (2095) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5518) | 0.607 (516) | 0.740 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.383 | 0.369 | 0.245 | 0.245 | 0.593 | 0.308 | 0.458 | 1.199 |
| 6h | 360 | 0.382 | 0.381 | 0.306 | 0.347 | 0.507 | 0.268 | 0.496 | 1.145 |
| 24h | 1440 | 0.356 | 0.345 | 0.272 | 0.298 | 0.530 | 0.263 | 0.450 | 1.150 |
| 7d | 10080 | 0.369 | 0.360 | 0.275 | 0.307 | 0.533 | 0.268 | 0.471 | 1.201 |
| 30d | 43200 | 0.359 | 0.353 | 0.276 | 0.304 | 0.524 | 0.257 | 0.462 | 1.284 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.383 / 0.593 / 0.850; 2: 0.359 / 0.492 / 0.950; 3: 0.360 / 0.525 / 0.967; 4: 0.345 / 0.542 / 1.000; 5: 0.335 / 0.356 / 0.967; 6: 0.358 / 0.441 / 0.967; 7: 0.320 / 0.441 / 1.000; 8: 0.357 / 0.475 / 0.967; 9: 0.353 / 0.525 / 0.967; 10: 0.338 / 0.458 / 0.983; 11: 0.375 / 0.525 / 1.000; 12: 0.382 / 0.593 / 1.000; 13: 0.363 / 0.542 / 0.983; 14: 0.340 / 0.508 / 0.967; 15: 0.355 / 0.508 / 0.967
- 6h: 1: 0.382 / 0.507 / 0.897; 2: 0.372 / 0.482 / 0.953; 3: 0.385 / 0.541 / 0.944; 4: 0.373 / 0.510 / 0.944; 5: 0.372 / 0.462 / 0.917; 6: 0.372 / 0.507 / 0.925; 7: 0.373 / 0.524 / 0.939; 8: 0.376 / 0.527 / 0.928; 9: 0.377 / 0.518 / 0.936; 10: 0.370 / 0.513 / 0.947; 11: 0.374 / 0.518 / 0.958; 12: 0.380 / 0.510 / 0.942; 13: 0.378 / 0.535 / 0.953; 14: 0.366 / 0.485 / 0.947; 15: 0.364 / 0.487 / 0.944
- 24h: 1: 0.356 / 0.530 / 0.884; 2: 0.341 / 0.490 / 0.906; 3: 0.346 / 0.509 / 0.907; 4: 0.347 / 0.522 / 0.907; 5: 0.339 / 0.479 / 0.900; 6: 0.346 / 0.519 / 0.901; 7: 0.340 / 0.501 / 0.906; 8: 0.344 / 0.521 / 0.903; 9: 0.341 / 0.495 / 0.905; 10: 0.341 / 0.509 / 0.907; 11: 0.344 / 0.525 / 0.907; 12: 0.339 / 0.510 / 0.905; 13: 0.340 / 0.512 / 0.909; 14: 0.333 / 0.491 / 0.909; 15: 0.334 / 0.486 / 0.908
- 7d: 1: 0.369 / 0.533 / 0.898; 2: 0.358 / 0.503 / 0.900; 3: 0.357 / 0.509 / 0.900; 4: 0.353 / 0.497 / 0.900; 5: 0.353 / 0.500 / 0.900; 6: 0.352 / 0.496 / 0.900; 7: 0.351 / 0.495 / 0.901; 8: 0.354 / 0.510 / 0.900; 9: 0.352 / 0.497 / 0.900; 10: 0.353 / 0.506 / 0.901; 11: 0.351 / 0.501 / 0.901; 12: 0.352 / 0.504 / 0.901; 13: 0.349 / 0.495 / 0.901; 14: 0.350 / 0.494 / 0.901; 15: 0.349 / 0.500 / 0.901
- 30d: 1: 0.359 / 0.524 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.352 / 0.510 / 0.900; 4: 0.347 / 0.498 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.346 / 0.500 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.344 / 0.496 / 0.900; 10: 0.346 / 0.505 / 0.900; 11: 0.344 / 0.499 / 0.900; 12: 0.346 / 0.504 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.344 / 0.498 / 0.900; 15: 0.344 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.086 (body 0.051, range 0.121); 'price stays where it was' would score 0.122; colour right 0.627; typical miss of the close 16.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.127 (body 0.074, range 0.179); 'price stays where it was' would score 0.127; colour right 0.524; typical miss of the close 14.2 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.125 (body 0.087, range 0.164); 'price stays where it was' would score 0.126; colour right 0.495; typical miss of the close 8.3 bp; chain ended on the right side 0.594 of 96 chains; n=1440
- 7d: match 0.127 (body 0.087, range 0.168); 'price stays where it was' would score 0.133; colour right 0.502; typical miss of the close 8.8 bp; chain ended on the right side 0.545 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.5 bp; chain ended on the right side 0.525 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.195 / 4.4; 3: 0.167 / 5.8; 4: 0.132 / 6.4; 5: 0.123 / 7.0; 6: 0.112 / 7.5; 7: 0.106 / 7.8; 8: 0.097 / 8.2; 9: 0.087 / 8.2; 10: 0.088 / 8.9; 11: 0.084 / 9.4; 12: 0.076 / 9.7; 13: 0.067 / 9.9; 14: 0.069 / 10.3; 15: 0.059 / 10.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 120976, probability skill vs chance 0.2279, widened contest next: False
  - now: threshold 0.8341, hit rate recent 0.9192 / long run 0.9347
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.268, naive rule 0.406, lift 3.40x
    - 24h: 44 calls (44 a day), hit rate 0.886, chance 0.288, naive rule 0.485, lift 3.08x
    - 7d: 385 calls (55 a day), hit rate 0.935, chance 0.295, naive rule 0.498, lift 3.17x
    - 30d: 1684 calls (56 a day), hit rate 0.935, chance 0.294, naive rule 0.492, lift 3.18x
  - next: threshold 0.5336, hit rate recent 0.5957 / long run 0.592
    - 6h: 23 calls (93 a day), hit rate 0.652, chance 0.268, lift 2.44x
    - 24h: 90 calls (90 a day), hit rate 0.578, chance 0.288, lift 2.01x
    - 7d: 674 calls (96 a day), hit rate 0.591, chance 0.295, lift 2.00x
    - 30d: 2818 calls (94 a day), hit rate 0.581, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 538, 0.520; 0.40: 478, 0.576; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 311, 0.741; 0.60: 263, 0.785; 0.65: 220, 0.811; 0.70: 174, 0.843; 0.75: 135, 0.875; 0.80: 90, 0.913; 0.85: 46, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.426; 0.35: 502, 0.464; 0.40: 408, 0.498; 0.45: 310, 0.534; 0.50: 202, 0.569; 0.55: 91, 0.576; 0.60: 14, 0.625; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 120974, probability skill vs chance 0.215, widened contest next: False
  - now: threshold 0.6726, hit rate recent 0.8402 / long run 0.8231
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.170, naive rule 0.332, lift 5.29x
    - 24h: 49 calls (49 a day), hit rate 0.857, chance 0.169, naive rule 0.370, lift 5.08x
    - 7d: 361 calls (52 a day), hit rate 0.820, chance 0.182, naive rule 0.400, lift 4.50x
    - 30d: 1560 calls (52 a day), hit rate 0.831, chance 0.187, naive rule 0.400, lift 4.44x
  - next: threshold 0.4196, hit rate recent 0.4648 / long run 0.4742
    - 6h: 32 calls (131 a day), hit rate 0.469, chance 0.170, lift 2.76x
    - 24h: 133 calls (134 a day), hit rate 0.466, chance 0.169, lift 2.76x
    - 7d: 926 calls (132 a day), hit rate 0.468, chance 0.182, lift 2.57x
    - 30d: 2966 calls (99 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.426; 0.35: 343, 0.493; 0.40: 276, 0.565; 0.45: 224, 0.620; 0.50: 176, 0.670; 0.55: 136, 0.711; 0.60: 104, 0.755; 0.65: 75, 0.792; 0.70: 52, 0.831; 0.75: 31, 0.877; 0.80: 10, 0.900
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.388; 0.35: 253, 0.420; 0.40: 158, 0.452; 0.45: 70, 0.463; 0.50: 15, 0.488; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 120971, probability skill vs chance 0.2068, widened contest next: False
  - now: threshold 0.5558, hit rate recent 0.7042 / long run 0.6863
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.124, naive rule 0.295, lift 5.85x
    - 24h: 48 calls (48 a day), hit rate 0.729, chance 0.116, naive rule 0.322, lift 6.30x
    - 7d: 339 calls (48 a day), hit rate 0.664, chance 0.116, naive rule 0.320, lift 5.74x
    - 30d: 1521 calls (51 a day), hit rate 0.696, chance 0.121, naive rule 0.330, lift 5.76x
  - next: threshold 0.3363, hit rate recent 0.4167 / long run 0.3851
    - 6h: 24 calls (99 a day), hit rate 0.417, chance 0.124, lift 3.35x
    - 24h: 113 calls (114 a day), hit rate 0.407, chance 0.116, lift 3.52x
    - 7d: 757 calls (108 a day), hit rate 0.378, chance 0.116, lift 3.27x
    - 30d: 2594 calls (86 a day), hit rate 0.383, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.428; 0.35: 188, 0.497; 0.40: 144, 0.549; 0.45: 111, 0.596; 0.50: 84, 0.636; 0.55: 61, 0.673; 0.60: 40, 0.721; 0.65: 23, 0.789; 0.70: 10, 0.829; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.352; 0.35: 97, 0.380; 0.40: 36, 0.399; 0.45: 8, 0.425; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 120966, probability skill vs chance 0.1841, widened contest next: False
  - now: threshold 0.4046, hit rate recent 0.6051 / long run 0.5631
    - 6h: 17 calls (71 a day), hit rate 0.588, chance 0.083, naive rule 0.265, lift 7.12x
    - 24h: 59 calls (60 a day), hit rate 0.610, chance 0.073, naive rule 0.254, lift 8.36x
    - 7d: 363 calls (52 a day), hit rate 0.551, chance 0.074, naive rule 0.267, lift 7.48x
    - 30d: 1578 calls (53 a day), hit rate 0.567, chance 0.077, naive rule 0.272, lift 7.36x
  - next: threshold 0.2944, hit rate recent 0.3321 / long run 0.3135
    - 6h: 13 calls (54 a day), hit rate 0.308, chance 0.083, lift 3.72x
    - 24h: 66 calls (67 a day), hit rate 0.333, chance 0.073, lift 4.57x
    - 7d: 465 calls (67 a day), hit rate 0.314, chance 0.074, lift 4.26x
    - 30d: 2173 calls (72 a day), hit rate 0.305, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.444; 0.35: 87, 0.495; 0.40: 62, 0.551; 0.45: 41, 0.604; 0.50: 26, 0.661; 0.55: 15, 0.704; 0.60: 7, 0.748; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.315; 0.35: 14, 0.349; 0.40: 2, 0.429; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 23.554 | 5.43% | 0.850 | 0.483 | 0.249 | 0.593 | 0.166 |
| 6h | 23.888 | 8.77% | 0.894 | 0.483 | 0.250 | 0.529 | 0.478 |
| 24h | 15.218 | 4.80% | 0.884 | 0.486 | 0.250 | 0.495 | 0.681 |
| 7d | 15.106 | 3.59% | 0.899 | 0.499 | 0.250 | 0.503 | 0.659 |
| 30d | 13.422 | 4.22% | 0.900 | 0.500 | 0.251 | 0.496 | 0.672 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 24.906 | 23.611 | 24.209 | 23.464 | 23.518 | 24.433 | 23.488 | 23.431 | 23.465 | 23.554 |
| 6h | 26.186 | 24.081 | 24.355 | 23.965 | 24.241 | 24.556 | 23.875 | 23.871 | 23.870 | 23.888 |
| 24h | 15.986 | 15.389 | 15.395 | 15.260 | 15.578 | 15.508 | 15.204 | 15.169 | 15.188 | 15.218 |
| 7d | 15.668 | 15.252 | 15.197 | 15.122 | 15.384 | 15.275 | 15.093 | 15.069 | 15.078 | 15.106 |
| 30d | 14.014 | 13.553 | 13.508 | 13.446 | 13.666 | 13.616 | 13.418 | 13.399 | 13.398 | 13.422 |

## Next candle

- candle starting 2026-10-26 04:22 UTC, last close 2310.48
- P(up) 0.4779, return quantiles (bp): {'05': -11.884, '10': -9.881, '25': -5.495, '40': -2.237, '50': -0.464, '60': 1.671, '75': 4.305, '90': 8.885, '95': 12.616}
- changepoint probability 0.0219, regime age 263.3 min
- agent weights: empirical 0.003, ewma 0.059, garch 0.027, har 0.189, bocpd 0.015, hmm 0.009, online_qr 0.315, lgbm 0.384

## Learning log

- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.48, 6.3, 19.28], current probabilities: [0.009, 0.935, 0.056]
- live generator: {'versions': 60, 'latest_effective': '2026-10-26 04:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.387, 'l_abs': 0.722, 'l_hi': 0.796, 'l_lo': 0.77, 'b05': 0.73, 'b25': 0.705, 'b75': 0.662, 'b95': 0.702}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.264, 1.552, 1.725, 2.136, 2.208, 2.25, 2.41, 2.511, 2.599, 2.678, 2.917, 2.865, 2.979, 3.09]}
- calibration offsets (in sigma): {'05': -0.0295, '10': -0.119, '25': -0.1175, '40': -0.046, '50': -0.035, '60': 0.016, '75': -0.0125, '90': -0.001, '95': 0.0095}
