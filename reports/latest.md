# ETH-USD 60s candle generator - report

- generated: 2026-11-05 05:57 UTC
- last closed candle: 2026-11-05 05:57 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.470 in the last 7 days, -0.067 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.470 (672) [0.448, 0.490] | 0.511 (2879) [0.494, 0.530] | 0.512 (6138) [0.500, 0.525] | 0.513 (3166) [0.494, 0.532] | 0.565 (23) | 0.500 | down -0.067 (noise 0.027) |
| colour_clear | 0.483 (783) | 0.526 (5464) [0.511, 0.541] | 0.541 (23808) [0.535, 0.546] | 0.520 (50207) [0.514, 0.526] | 0.542 (25969) [0.537, 0.547] | 0.547 (221) | 0.500 | flat -0.016 (noise 0.009) |
| colour_confident | 0.556 (108) | 0.575 (901) [0.562, 0.591] | 0.592 (4356) [0.581, 0.603] | 0.597 (4803) [0.585, 0.608] | 0.597 (4803) [0.585, 0.608] | 0.562 (16) | 0.500 | flat -0.026 (noise 0.021) |
| colour_next | 0.500 (1435) | 0.526 (9978) [0.516, 0.536] | 0.528 (42861) [0.524, 0.531] | 0.515 (91461) [0.511, 0.519] | 0.529 (47112) [0.525, 0.532] | 0.501 (357) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.504 (20090) | 0.502 (139692) [0.500, 0.504] | 0.501 (600054) [0.500, 0.502] | 0.501 (1280454) [0.500, 0.502] | 0.501 (659568) [0.500, 0.502] | 0.510 (4998) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.556 (27) | 0.631 (198) [0.592, 0.675] | 0.627 (1141) [0.608, 0.648] | 0.631 (1271) [0.612, 0.650] | 0.631 (1271) [0.612, 0.650] | 1.000 (2) | 0.500 | flat +0.024 (noise 0.042) |
| reversal_k13_next | 0.318 (44) | 0.355 (349) [0.312, 0.394] | 0.326 (1830) [0.312, 0.340] | 0.313 (4196) [0.302, 0.324] | 0.326 (2091) [0.314, 0.339] | 0.438 (16) | 0.077 | flat +0.038 (noise 0.034) |
| reversal_k13_now | 0.547 (53) | 0.574 (413) [0.538, 0.610] | 0.561 (1658) [0.541, 0.580] | 0.573 (3308) [0.559, 0.587] | 0.567 (1836) [0.548, 0.587] | 0.750 (12) | 0.077 | flat +0.006 (noise 0.036) |
| reversal_k3_next | 0.641 (39) | 0.600 (743) [0.581, 0.618] | 0.586 (2983) [0.574, 0.597] | 0.586 (5740) [0.577, 0.595] | 0.585 (3300) [0.573, 0.596] | 0.706 (17) | 0.293 | flat +0.008 (noise 0.026) |
| reversal_k3_now | 0.922 (51) | 0.927 (413) [0.908, 0.951] | 0.932 (1738) [0.922, 0.943] | 0.937 (3670) [0.930, 0.943] | 0.932 (1907) [0.923, 0.942] | 0.900 (10) | 0.293 | flat -0.015 (noise 0.020) |
| reversal_k5_next | 0.510 (51) | 0.537 (376) [0.514, 0.557] | 0.478 (2721) [0.464, 0.494] | 0.482 (5059) [0.471, 0.494] | 0.475 (3069) [0.461, 0.490] | 0.571 (14) | 0.187 | flat +0.036 (noise 0.031) |
| reversal_k5_now | 0.812 (48) | 0.810 (410) [0.796, 0.823] | 0.815 (1631) [0.805, 0.825] | 0.828 (3416) [0.819, 0.837] | 0.819 (1805) [0.810, 0.829] | 0.800 (10) | 0.187 | flat -0.018 (noise 0.027) |
| reversal_k8_next | 0.429 (49) | 0.436 (488) [0.411, 0.465] | 0.391 (2762) [0.378, 0.405] | 0.394 (5106) [0.383, 0.404] | 0.392 (3000) [0.379, 0.405] | 0.600 (10) | 0.121 | flat +0.049 (noise 0.029) |
| reversal_k8_now | 0.652 (46) | 0.697 (369) [0.663, 0.729] | 0.679 (1570) [0.660, 0.698] | 0.701 (3328) [0.687, 0.715] | 0.689 (1741) [0.669, 0.707] | 0.800 (10) | 0.121 | flat +0.014 (noise 0.037) |
| overall | 0.505 (22002) | 0.506 (153903) [0.504, 0.508] | 0.504 (662687) [0.503, 0.506] | 0.504 (1411876) [0.503, 0.505] | 0.505 (728595) [0.503, 0.506] | 0.513 (5477) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07731, 0.1162] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5264, 'levels': [{'threshold': 0.07731, 'calls_per_day': 143.4, 'win_rate': 0.573}, {'threshold': 0.1162, 'calls_per_day': 35.9, 'win_rate': 0.6378}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42864, 'rate': 0.5272}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14999 | 0.343 | 0.528 (14760) | 0.576 (2212) | 0.736 (2574) |
| volatility: normal | 14999 | 0.366 | 0.533 (14930) | 0.612 (1431) | 0.755 (2227) |
| volatility: wild | 14999 | 0.381 | 0.524 (14958) | 0.615 (832) | 0.763 (2060) |
| session: Asia 00-08 | 15237 | 0.364 | 0.535 (15134) | 0.599 (1572) | 0.753 (2262) |
| session: Europe 08-13 | 9300 | 0.358 | 0.534 (9203) | 0.598 (1146) | 0.743 (1538) |
| session: US 13-21 | 14880 | 0.371 | 0.523 (14782) | 0.592 (1151) | 0.756 (2235) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5529) | 0.584 (606) | 0.743 (826) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.378 | 0.383 | 0.307 | 0.307 | 0.433 | 0.253 | 0.503 | 1.122 |
| 6h | 360 | 0.380 | 0.362 | 0.317 | 0.346 | 0.503 | 0.263 | 0.497 | 1.140 |
| 24h | 1440 | 0.370 | 0.365 | 0.294 | 0.327 | 0.499 | 0.252 | 0.488 | 1.203 |
| 7d | 10080 | 0.361 | 0.356 | 0.276 | 0.306 | 0.526 | 0.259 | 0.462 | 1.274 |
| 30d | 43200 | 0.363 | 0.356 | 0.277 | 0.308 | 0.527 | 0.262 | 0.465 | 1.252 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.378 / 0.433 / 0.883; 2: 0.389 / 0.533 / 0.833; 3: 0.382 / 0.500 / 0.867; 4: 0.414 / 0.567 / 0.900; 5: 0.370 / 0.517 / 0.950; 6: 0.370 / 0.533 / 0.950; 7: 0.375 / 0.550 / 0.967; 8: 0.360 / 0.483 / 0.933; 9: 0.409 / 0.633 / 0.967; 10: 0.352 / 0.400 / 0.983; 11: 0.367 / 0.467 / 0.983; 12: 0.362 / 0.417 / 0.983; 13: 0.381 / 0.517 / 1.000; 14: 0.374 / 0.517 / 1.000; 15: 0.381 / 0.517 / 1.000
- 6h: 1: 0.380 / 0.503 / 0.881; 2: 0.367 / 0.500 / 0.814; 3: 0.375 / 0.519 / 0.836; 4: 0.367 / 0.486 / 0.833; 5: 0.375 / 0.517 / 0.906; 6: 0.369 / 0.522 / 0.892; 7: 0.385 / 0.572 / 0.944; 8: 0.370 / 0.517 / 0.897; 9: 0.382 / 0.539 / 0.944; 10: 0.368 / 0.514 / 0.942; 11: 0.365 / 0.472 / 0.975; 12: 0.368 / 0.508 / 0.964; 13: 0.371 / 0.500 / 0.989; 14: 0.367 / 0.506 / 0.983; 15: 0.360 / 0.483 / 0.989
- 24h: 1: 0.370 / 0.499 / 0.906; 2: 0.364 / 0.503 / 0.885; 3: 0.370 / 0.508 / 0.890; 4: 0.364 / 0.499 / 0.889; 5: 0.363 / 0.497 / 0.901; 6: 0.365 / 0.526 / 0.901; 7: 0.363 / 0.503 / 0.910; 8: 0.361 / 0.518 / 0.901; 9: 0.364 / 0.508 / 0.909; 10: 0.361 / 0.505 / 0.910; 11: 0.358 / 0.498 / 0.915; 12: 0.369 / 0.537 / 0.919; 13: 0.365 / 0.511 / 0.919; 14: 0.360 / 0.508 / 0.921; 15: 0.356 / 0.497 / 0.917
- 7d: 1: 0.361 / 0.526 / 0.896; 2: 0.351 / 0.499 / 0.897; 3: 0.352 / 0.509 / 0.898; 4: 0.349 / 0.500 / 0.898; 5: 0.350 / 0.510 / 0.899; 6: 0.347 / 0.506 / 0.899; 7: 0.349 / 0.499 / 0.900; 8: 0.345 / 0.504 / 0.900; 9: 0.348 / 0.504 / 0.900; 10: 0.345 / 0.494 / 0.901; 11: 0.346 / 0.500 / 0.901; 12: 0.346 / 0.502 / 0.902; 13: 0.348 / 0.505 / 0.902; 14: 0.345 / 0.496 / 0.902; 15: 0.347 / 0.506 / 0.902
- 30d: 1: 0.363 / 0.527 / 0.898; 2: 0.352 / 0.496 / 0.899; 3: 0.354 / 0.509 / 0.899; 4: 0.350 / 0.498 / 0.899; 5: 0.351 / 0.504 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.499 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.349 / 0.500 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.346 / 0.497 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.348 / 0.501 / 0.900; 14: 0.347 / 0.500 / 0.900; 15: 0.348 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.166 (body 0.102, range 0.229); 'price stays where it was' would score 0.119; colour right 0.500; typical miss of the close 7.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.128 (body 0.083, range 0.174); 'price stays where it was' would score 0.119; colour right 0.517; typical miss of the close 10.2 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.130 (body 0.088, range 0.171); 'price stays where it was' would score 0.122; colour right 0.508; typical miss of the close 11.3 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.160); 'price stays where it was' would score 0.122; colour right 0.504; typical miss of the close 8.8 bp; chain ended on the right side 0.478 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.164); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 8.4 bp; chain ended on the right side 0.512 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.3; 2: 0.199 / 5.0; 3: 0.169 / 6.6; 4: 0.131 / 6.9; 5: 0.125 / 7.7; 6: 0.114 / 8.4; 7: 0.111 / 8.6; 8: 0.098 / 9.6; 9: 0.090 / 9.5; 10: 0.089 / 10.0; 11: 0.085 / 10.2; 12: 0.077 / 10.6; 13: 0.071 / 10.8; 14: 0.071 / 11.4; 15: 0.064 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 135471, probability skill vs chance 0.2306, widened contest next: False
  - now: threshold 0.8376, hit rate recent 0.9191 / long run 0.9303
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.263, naive rule 0.424, lift 3.42x
    - 24h: 45 calls (45 a day), hit rate 0.933, chance 0.283, naive rule 0.479, lift 3.30x
    - 7d: 409 calls (58 a day), hit rate 0.924, chance 0.292, naive rule 0.498, lift 3.16x
    - 30d: 1731 calls (58 a day), hit rate 0.932, chance 0.293, naive rule 0.494, lift 3.18x
  - next: threshold 0.5653, hit rate recent 0.6251 / long run 0.6009
    - 6h: 17 calls (69 a day), hit rate 0.706, chance 0.263, lift 2.68x
    - 24h: 49 calls (49 a day), hit rate 0.673, chance 0.283, lift 2.38x
    - 7d: 723 calls (103 a day), hit rate 0.609, chance 0.292, lift 2.08x
    - 30d: 2991 calls (100 a day), hit rate 0.586, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.497; 0.35: 533, 0.523; 0.40: 473, 0.579; 0.45: 404, 0.651; 0.50: 354, 0.700; 0.55: 308, 0.742; 0.60: 260, 0.786; 0.65: 219, 0.811; 0.70: 173, 0.843; 0.75: 138, 0.876; 0.80: 92, 0.909; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 499, 0.462; 0.40: 403, 0.498; 0.45: 306, 0.534; 0.50: 197, 0.569; 0.55: 89, 0.572; 0.60: 12, 0.629; 0.65: 1, 0.619
- **K=5**: model 1792540800, labels learned 135469, probability skill vs chance 0.218, widened contest next: False
  - now: threshold 0.6891, hit rate recent 0.7993 / long run 0.817
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.164, naive rule 0.323, lift 4.87x
    - 24h: 44 calls (44 a day), hit rate 0.818, chance 0.185, naive rule 0.404, lift 4.42x
    - 7d: 407 calls (58 a day), hit rate 0.811, chance 0.187, naive rule 0.414, lift 4.32x
    - 30d: 1630 calls (54 a day), hit rate 0.815, chance 0.187, naive rule 0.405, lift 4.36x
  - next: threshold 0.4526, hit rate recent 0.5231 / long run 0.5104
    - 6h: 14 calls (57 a day), hit rate 0.571, chance 0.164, lift 3.48x
    - 24h: 53 calls (53 a day), hit rate 0.547, chance 0.185, lift 2.96x
    - 7d: 378 calls (54 a day), hit rate 0.540, chance 0.187, lift 2.88x
    - 30d: 2725 calls (91 a day), hit rate 0.479, chance 0.187, lift 2.56x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.424; 0.35: 346, 0.491; 0.40: 280, 0.563; 0.45: 230, 0.615; 0.50: 184, 0.663; 0.55: 146, 0.699; 0.60: 111, 0.748; 0.65: 76, 0.786; 0.70: 49, 0.818; 0.75: 29, 0.860; 0.80: 10, 0.877
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.385; 0.35: 256, 0.420; 0.40: 160, 0.459; 0.45: 67, 0.482; 0.50: 12, 0.493; 0.55: 1, 0.444
- **K=8**: model 1793059200, labels learned 135466, probability skill vs chance 0.2138, widened contest next: False
  - now: threshold 0.5739, hit rate recent 0.6891 / long run 0.6921
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.123, naive rule 0.320, lift 6.51x
    - 24h: 40 calls (40 a day), hit rate 0.725, chance 0.124, naive rule 0.354, lift 5.82x
    - 7d: 366 calls (52 a day), hit rate 0.705, chance 0.123, naive rule 0.347, lift 5.72x
    - 30d: 1564 calls (52 a day), hit rate 0.681, chance 0.121, naive rule 0.334, lift 5.65x
  - next: threshold 0.3601, hit rate recent 0.4611 / long run 0.4207
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.123, lift 4.88x
    - 24h: 42 calls (42 a day), hit rate 0.500, chance 0.124, lift 4.02x
    - 7d: 472 calls (67 a day), hit rate 0.451, chance 0.123, lift 3.66x
    - 30d: 2749 calls (92 a day), hit rate 0.391, chance 0.121, lift 3.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.431; 0.35: 191, 0.495; 0.40: 151, 0.542; 0.45: 116, 0.591; 0.50: 84, 0.638; 0.55: 61, 0.671; 0.60: 41, 0.703; 0.65: 24, 0.778; 0.70: 12, 0.811; 0.75: 2, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.361; 0.35: 90, 0.388; 0.40: 26, 0.417; 0.45: 5, 0.438; 0.50: 1, 0.640
- **K=13**: model 1793577600, labels learned 135461, probability skill vs chance 0.185, widened contest next: False
  - now: threshold 0.4572, hit rate recent 0.5957 / long run 0.5724
    - 6h: 12 calls (50 a day), hit rate 0.750, chance 0.090, naive rule 0.278, lift 8.35x
    - 24h: 46 calls (46 a day), hit rate 0.609, chance 0.082, naive rule 0.289, lift 7.45x
    - 7d: 409 calls (59 a day), hit rate 0.589, chance 0.080, naive rule 0.293, lift 7.34x
    - 30d: 1654 calls (55 a day), hit rate 0.564, chance 0.077, naive rule 0.280, lift 7.28x
  - next: threshold 0.286, hit rate recent 0.3723 / long run 0.3399
    - 6h: 16 calls (67 a day), hit rate 0.438, chance 0.090, lift 4.87x
    - 24h: 48 calls (49 a day), hit rate 0.375, chance 0.082, lift 4.59x
    - 7d: 356 calls (51 a day), hit rate 0.365, chance 0.080, lift 4.55x
    - 30d: 1832 calls (61 a day), hit rate 0.328, chance 0.077, lift 4.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 130, 0.439; 0.35: 93, 0.490; 0.40: 66, 0.547; 0.45: 45, 0.590; 0.50: 30, 0.648; 0.55: 19, 0.676; 0.60: 10, 0.714; 0.65: 3, 0.692; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.332; 0.35: 13, 0.346; 0.40: 3, 0.415; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.926 | 3.00% | 0.883 | 0.467 | 0.251 | 0.467 | 0.230 |
| 6h | 13.454 | 2.16% | 0.883 | 0.478 | 0.251 | 0.486 | 0.395 |
| 24h | 18.008 | 3.38% | 0.905 | 0.499 | 0.251 | 0.481 | 0.712 |
| 7d | 15.725 | 4.96% | 0.900 | 0.500 | 0.250 | 0.505 | 0.750 |
| 30d | 14.782 | 4.23% | 0.900 | 0.500 | 0.250 | 0.498 | 0.687 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.294 | 11.957 | 11.952 | 12.071 | 11.866 | 11.904 | 11.897 | 11.856 | 11.891 | 11.926 |
| 6h | 13.751 | 13.466 | 13.457 | 13.460 | 13.499 | 13.503 | 13.415 | 13.400 | 13.403 | 13.454 |
| 24h | 18.638 | 18.107 | 18.010 | 18.021 | 18.253 | 18.260 | 18.074 | 17.996 | 17.976 | 18.008 |
| 7d | 16.546 | 15.885 | 15.838 | 15.769 | 16.028 | 16.062 | 15.718 | 15.696 | 15.699 | 15.725 |
| 30d | 15.435 | 14.934 | 14.874 | 14.811 | 15.051 | 14.998 | 14.778 | 14.754 | 14.755 | 14.782 |

## Next candle

- candle starting 2026-11-05 05:57 UTC, last close 2417.23
- P(up) 0.4916, return quantiles (bp): {'05': -6.676, '10': -5.055, '25': -2.523, '40': -0.977, '50': -0.08, '60': 0.891, '75': 2.65, '90': 5.05, '95': 6.238}
- changepoint probability 0.0413, regime age 220.7 min
- agent weights: empirical 0.007, ewma 0.126, garch 0.173, har 0.171, bocpd 0.062, hmm 0.066, online_qr 0.168, lgbm 0.228

## Learning log

- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.25, 4.78, 12.71], current probabilities: [0.335, 0.657, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-11-05 06:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.272, 'l_abs': 0.722, 'l_hi': 0.739, 'l_lo': 0.795, 'b05': 0.744, 'b25': 0.687, 'b75': 0.648, 'b95': 0.717}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8]], 'cone_width': [2.327, 2.636, 3.174, 2.531, 2.835, 2.462, 3.286, 2.803, 2.902, 2.872, 2.774, 2.836, 3.009, 3.121]}
- calibration offsets (in sigma): {'05': 0.008, '10': -0.014, '25': -0.01, '40': -0.036, '50': -0.03, '60': -0.024, '75': -0.0, '90': 0.004, '95': -0.088}
