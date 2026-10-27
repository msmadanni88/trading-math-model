# ETH-USD 60s candle generator - report

- generated: 2026-10-27 16:15 UTC
- last closed candle: 2026-10-27 16:15 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.530 (672) [0.494, 0.569] | 0.522 (2876) [0.503, 0.542] | 0.516 (5274) [0.503, 0.530] | 0.523 (2302) [0.499, 0.546] | 0.508 (65) | 0.500 | flat -0.009 (noise 0.032) |
| colour_clear | 0.538 (824) | 0.548 (5704) [0.540, 0.558] | 0.536 (23552) [0.528, 0.543] | 0.518 (43117) [0.512, 0.524] | 0.546 (18879) [0.541, 0.550] | 0.573 (586) | 0.500 | flat -0.001 (noise 0.009) |
| colour_confident | 0.613 (160) | 0.601 (1419) [0.588, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.603 (3621) [0.590, 0.617] | 0.578 (116) | 0.500 | flat -0.001 (noise 0.022) |
| colour_next | 0.522 (1432) | 0.531 (10039) [0.525, 0.537] | 0.524 (42872) [0.520, 0.529] | 0.513 (78622) [0.509, 0.517] | 0.529 (34273) [0.525, 0.533] | 0.545 (968) | 0.500 | flat +0.001 (noise 0.007) |
| colour_path | 0.499 (20048) | 0.500 (140546) [0.498, 0.503] | 0.501 (600208) [0.499, 0.502] | 0.501 (1100708) [0.500, 0.502] | 0.500 (479822) [0.499, 0.502] | 0.503 (13552) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.604 (53) | 0.626 (420) [0.602, 0.667] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.637 (994) [0.616, 0.659] | 0.571 (35) | 0.500 | flat +0.015 (noise 0.045) |
| reversal_k13_next | 0.271 (59) | 0.312 (442) [0.287, 0.336] | 0.304 (2171) [0.292, 0.316] | 0.307 (3743) [0.297, 0.318] | 0.316 (1638) [0.305, 0.327] | 0.500 (36) | 0.076 | flat +0.012 (noise 0.031) |
| reversal_k13_now | 0.457 (70) | 0.546 (370) [0.500, 0.594] | 0.561 (1601) [0.541, 0.583] | 0.571 (2776) [0.555, 0.587] | 0.560 (1304) [0.537, 0.585] | 0.600 (40) | 0.076 | flat +0.011 (noise 0.036) |
| reversal_k3_next | 0.590 (117) | 0.600 (678) [0.572, 0.628] | 0.582 (2864) [0.570, 0.595] | 0.584 (4759) [0.574, 0.595] | 0.580 (2319) [0.567, 0.595] | 0.571 (77) | 0.293 | flat +0.039 (noise 0.026) |
| reversal_k3_now | 0.983 (57) | 0.946 (389) [0.921, 0.968] | 0.936 (1694) [0.927, 0.946] | 0.938 (3126) [0.931, 0.945] | 0.933 (1363) [0.922, 0.944] | 0.961 (51) | 0.293 | flat +0.008 (noise 0.021) |
| reversal_k5_next | 0.509 (110) | 0.479 (893) [0.448, 0.502] | 0.465 (3032) [0.451, 0.478] | 0.477 (4553) [0.465, 0.490] | 0.464 (2563) [0.449, 0.480] | 0.535 (43) | 0.187 | flat +0.027 (noise 0.024) |
| reversal_k5_now | 0.833 (54) | 0.820 (361) [0.808, 0.831] | 0.829 (1568) [0.816, 0.842] | 0.830 (2874) [0.819, 0.840] | 0.820 (1263) [0.807, 0.833] | 0.830 (47) | 0.187 | flat +0.002 (noise 0.029) |
| reversal_k8_next | 0.336 (110) | 0.379 (755) [0.359, 0.396] | 0.380 (2651) [0.368, 0.392] | 0.388 (4416) [0.377, 0.399] | 0.380 (2310) [0.367, 0.394] | 0.379 (66) | 0.120 | flat +0.014 (noise 0.025) |
| reversal_k8_now | 0.545 (55) | 0.658 (342) [0.608, 0.707] | 0.689 (1530) [0.667, 0.710] | 0.699 (2842) [0.683, 0.715] | 0.680 (1255) [0.657, 0.705] | 0.711 (45) | 0.121 | flat -0.014 (noise 0.036) |
| overall | 0.501 (22208) | 0.504 (155487) [0.501, 0.507] | 0.504 (663067) [0.503, 0.505] | 0.503 (1213693) [0.502, 0.504] | 0.504 (530412) [0.502, 0.506] | 0.509 (14990) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07963, 0.1193] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5294, 'levels': [{'threshold': 0.07963, 'calls_per_day': 146.0, 'win_rate': 0.6047}, {'threshold': 0.1193, 'calls_per_day': 37.3, 'win_rate': 0.6374}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 34102, 'rate': 0.5306}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15205 | 0.336 | 0.523 (14955) | 0.589 (1747) | 0.763 (2540) |
| volatility: normal | 15206 | 0.365 | 0.527 (15135) | 0.605 (1328) | 0.750 (2267) |
| volatility: wild | 15204 | 0.380 | 0.523 (15159) | 0.630 (662) | 0.766 (1960) |
| session: Asia 00-08 | 15360 | 0.359 | 0.531 (15249) | 0.609 (1324) | 0.764 (2239) |
| session: Europe 08-13 | 9600 | 0.356 | 0.528 (9511) | 0.596 (931) | 0.755 (1534) |
| session: US 13-21 | 15075 | 0.368 | 0.520 (14971) | 0.595 (947) | 0.768 (2163) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5518) | 0.609 (535) | 0.737 (831) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.371 | 0.397 | 0.264 | 0.264 | 0.500 | 0.256 | 0.486 | 1.264 |
| 6h | 360 | 0.396 | 0.380 | 0.305 | 0.335 | 0.565 | 0.278 | 0.515 | 1.208 |
| 24h | 1440 | 0.372 | 0.362 | 0.290 | 0.318 | 0.537 | 0.264 | 0.480 | 1.178 |
| 7d | 10080 | 0.369 | 0.359 | 0.280 | 0.311 | 0.530 | 0.266 | 0.472 | 1.226 |
| 30d | 43200 | 0.362 | 0.355 | 0.278 | 0.307 | 0.525 | 0.258 | 0.465 | 1.276 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.371 / 0.500 / 0.917; 2: 0.333 / 0.433 / 0.933; 3: 0.401 / 0.550 / 0.900; 4: 0.335 / 0.450 / 0.917; 5: 0.370 / 0.500 / 0.917; 6: 0.351 / 0.433 / 0.917; 7: 0.362 / 0.533 / 0.900; 8: 0.357 / 0.483 / 0.900; 9: 0.365 / 0.550 / 0.867; 10: 0.370 / 0.533 / 0.850; 11: 0.408 / 0.700 / 0.850; 12: 0.371 / 0.600 / 0.883; 13: 0.368 / 0.550 / 0.867; 14: 0.352 / 0.433 / 0.867; 15: 0.359 / 0.533 / 0.900
- 6h: 1: 0.396 / 0.565 / 0.903; 2: 0.389 / 0.521 / 0.928; 3: 0.383 / 0.515 / 0.892; 4: 0.377 / 0.496 / 0.875; 5: 0.376 / 0.538 / 0.906; 6: 0.372 / 0.518 / 0.911; 7: 0.372 / 0.513 / 0.892; 8: 0.379 / 0.524 / 0.911; 9: 0.372 / 0.499 / 0.894; 10: 0.376 / 0.513 / 0.861; 11: 0.373 / 0.546 / 0.897; 12: 0.372 / 0.518 / 0.889; 13: 0.369 / 0.513 / 0.889; 14: 0.371 / 0.507 / 0.878; 15: 0.374 / 0.515 / 0.892
- 24h: 1: 0.372 / 0.537 / 0.894; 2: 0.359 / 0.485 / 0.906; 3: 0.366 / 0.508 / 0.900; 4: 0.362 / 0.493 / 0.900; 5: 0.361 / 0.521 / 0.910; 6: 0.357 / 0.501 / 0.906; 7: 0.361 / 0.506 / 0.897; 8: 0.360 / 0.505 / 0.895; 9: 0.362 / 0.507 / 0.887; 10: 0.358 / 0.496 / 0.881; 11: 0.357 / 0.502 / 0.886; 12: 0.360 / 0.505 / 0.885; 13: 0.358 / 0.503 / 0.886; 14: 0.358 / 0.498 / 0.885; 15: 0.357 / 0.484 / 0.887
- 7d: 1: 0.369 / 0.530 / 0.896; 2: 0.357 / 0.497 / 0.902; 3: 0.358 / 0.510 / 0.900; 4: 0.355 / 0.500 / 0.901; 5: 0.354 / 0.505 / 0.901; 6: 0.353 / 0.499 / 0.901; 7: 0.353 / 0.500 / 0.901; 8: 0.355 / 0.507 / 0.901; 9: 0.354 / 0.501 / 0.901; 10: 0.353 / 0.504 / 0.900; 11: 0.350 / 0.498 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.350 / 0.497 / 0.901; 14: 0.351 / 0.496 / 0.901; 15: 0.351 / 0.503 / 0.901
- 30d: 1: 0.362 / 0.525 / 0.898; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.348 / 0.500 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.347 / 0.496 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.160 (body 0.115, range 0.205); 'price stays where it was' would score 0.123; colour right 0.417; typical miss of the close 10.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.082, range 0.170); 'price stays where it was' would score 0.123; colour right 0.510; typical miss of the close 11.4 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.132 (body 0.087, range 0.178); 'price stays where it was' would score 0.137; colour right 0.493; typical miss of the close 9.1 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.129 (body 0.088, range 0.171); 'price stays where it was' would score 0.137; colour right 0.500; typical miss of the close 8.7 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.162); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.1; 2: 0.198 / 4.6; 3: 0.169 / 6.1; 4: 0.132 / 6.6; 5: 0.125 / 7.3; 6: 0.112 / 7.8; 7: 0.107 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.086 / 9.8; 12: 0.078 / 10.0; 13: 0.067 / 10.3; 14: 0.069 / 10.7; 15: 0.061 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 123129, probability skill vs chance 0.2442, widened contest next: False
  - now: threshold 0.8341, hit rate recent 0.9584 / long run 0.9402
    - 6h: 19 calls (77 a day), hit rate 0.947, chance 0.258, naive rule 0.459, lift 3.68x
    - 24h: 70 calls (70 a day), hit rate 0.971, chance 0.292, naive rule 0.491, lift 3.32x
    - 7d: 399 calls (57 a day), hit rate 0.950, chance 0.298, naive rule 0.505, lift 3.18x
    - 30d: 1711 calls (57 a day), hit rate 0.937, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5402, hit rate recent 0.5738 / long run 0.5879
    - 6h: 19 calls (77 a day), hit rate 0.632, chance 0.258, lift 2.45x
    - 24h: 120 calls (120 a day), hit rate 0.583, chance 0.292, lift 2.00x
    - 7d: 666 calls (95 a day), hit rate 0.608, chance 0.298, lift 2.04x
    - 30d: 2869 calls (96 a day), hit rate 0.583, chance 0.293, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 537, 0.519; 0.40: 477, 0.576; 0.45: 408, 0.647; 0.50: 357, 0.699; 0.55: 312, 0.741; 0.60: 264, 0.785; 0.65: 221, 0.812; 0.70: 175, 0.843; 0.75: 136, 0.875; 0.80: 91, 0.915; 0.85: 47, 0.952; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 501, 0.466; 0.40: 407, 0.500; 0.45: 310, 0.534; 0.50: 200, 0.570; 0.55: 89, 0.575; 0.60: 14, 0.642; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 123127, probability skill vs chance 0.2243, widened contest next: False
  - now: threshold 0.6714, hit rate recent 0.8253 / long run 0.8225
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.153, naive rule 0.330, lift 5.31x
    - 24h: 64 calls (64 a day), hit rate 0.812, chance 0.188, naive rule 0.406, lift 4.31x
    - 7d: 370 calls (53 a day), hit rate 0.819, chance 0.185, naive rule 0.406, lift 4.43x
    - 30d: 1582 calls (53 a day), hit rate 0.826, chance 0.187, naive rule 0.400, lift 4.41x
  - next: threshold 0.4559, hit rate recent 0.5107 / long run 0.4843
    - 6h: 17 calls (69 a day), hit rate 0.471, chance 0.153, lift 3.08x
    - 24h: 78 calls (78 a day), hit rate 0.500, chance 0.188, lift 2.65x
    - 7d: 840 calls (120 a day), hit rate 0.490, chance 0.185, lift 2.65x
    - 30d: 3048 calls (102 a day), hit rate 0.466, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.425; 0.35: 345, 0.492; 0.40: 278, 0.564; 0.45: 226, 0.618; 0.50: 178, 0.667; 0.55: 138, 0.708; 0.60: 106, 0.750; 0.65: 76, 0.788; 0.70: 52, 0.828; 0.75: 30, 0.872; 0.80: 10, 0.904
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.390; 0.35: 253, 0.421; 0.40: 158, 0.452; 0.45: 70, 0.468; 0.50: 15, 0.488; 0.55: 1, 0.526
- **K=8**: model 1793059200, labels learned 123124, probability skill vs chance 0.2029, widened contest next: False
  - now: threshold 0.555, hit rate recent 0.6613 / long run 0.6759
    - 6h: 19 calls (78 a day), hit rate 0.579, chance 0.120, naive rule 0.295, lift 4.82x
    - 24h: 63 calls (63 a day), hit rate 0.698, chance 0.127, naive rule 0.350, lift 5.50x
    - 7d: 356 calls (51 a day), hit rate 0.666, chance 0.117, naive rule 0.325, lift 5.71x
    - 30d: 1534 calls (51 a day), hit rate 0.686, chance 0.121, naive rule 0.331, lift 5.68x
  - next: threshold 0.3353, hit rate recent 0.3544 / long run 0.3752
    - 6h: 27 calls (111 a day), hit rate 0.333, chance 0.120, lift 2.78x
    - 24h: 104 calls (105 a day), hit rate 0.365, chance 0.127, lift 2.88x
    - 7d: 736 calls (105 a day), hit rate 0.375, chance 0.117, lift 3.21x
    - 30d: 2672 calls (89 a day), hit rate 0.379, chance 0.121, lift 3.14x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 189, 0.495; 0.40: 146, 0.547; 0.45: 111, 0.591; 0.50: 84, 0.634; 0.55: 61, 0.670; 0.60: 40, 0.714; 0.65: 23, 0.781; 0.70: 10, 0.825; 0.75: 2, 0.818
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.354; 0.35: 95, 0.381; 0.40: 34, 0.403; 0.45: 7, 0.424; 0.50: 1, 0.613
- **K=13**: model 1793059200, labels learned 123119, probability skill vs chance 0.198, widened contest next: False
  - now: threshold 0.4067, hit rate recent 0.5463 / long run 0.5534
    - 6h: 20 calls (83 a day), hit rate 0.500, chance 0.091, naive rule 0.324, lift 5.48x
    - 24h: 61 calls (62 a day), hit rate 0.541, chance 0.079, naive rule 0.293, lift 6.85x
    - 7d: 370 calls (53 a day), hit rate 0.554, chance 0.074, naive rule 0.271, lift 7.48x
    - 30d: 1606 calls (54 a day), hit rate 0.560, chance 0.077, naive rule 0.273, lift 7.27x
  - next: threshold 0.2951, hit rate recent 0.3908 / long run 0.3208
    - 6h: 18 calls (75 a day), hit rate 0.556, chance 0.091, lift 6.08x
    - 24h: 54 calls (55 a day), hit rate 0.389, chance 0.079, lift 4.93x
    - 7d: 423 calls (61 a day), hit rate 0.319, chance 0.074, lift 4.31x
    - 30d: 2168 calls (72 a day), hit rate 0.309, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.439; 0.35: 89, 0.489; 0.40: 63, 0.545; 0.45: 41, 0.597; 0.50: 26, 0.657; 0.55: 16, 0.707; 0.60: 7, 0.749; 0.65: 2, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.322; 0.35: 14, 0.358; 0.40: 2, 0.458; 0.45: 0, 0.625

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 20.797 | 3.14% | 0.900 | 0.517 | 0.248 | 0.567 | 0.476 |
| 6h | 16.866 | 2.04% | 0.911 | 0.506 | 0.251 | 0.479 | 0.510 |
| 24h | 14.497 | 2.12% | 0.901 | 0.499 | 0.250 | 0.494 | 0.501 |
| 7d | 14.837 | 3.41% | 0.900 | 0.501 | 0.250 | 0.500 | 0.649 |
| 30d | 13.827 | 4.11% | 0.900 | 0.500 | 0.251 | 0.495 | 0.667 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.472 | 21.146 | 20.989 | 21.057 | 21.780 | 20.811 | 20.685 | 20.546 | 20.751 | 20.797 |
| 6h | 17.216 | 17.037 | 16.967 | 16.907 | 17.283 | 16.964 | 16.803 | 16.804 | 16.815 | 16.866 |
| 24h | 14.810 | 14.578 | 14.546 | 14.572 | 14.710 | 14.562 | 14.488 | 14.446 | 14.466 | 14.497 |
| 7d | 15.361 | 14.978 | 14.920 | 14.867 | 15.099 | 14.986 | 14.821 | 14.796 | 14.807 | 14.837 |
| 30d | 14.420 | 13.961 | 13.912 | 13.853 | 14.074 | 14.007 | 13.822 | 13.802 | 13.801 | 13.827 |

## Next candle

- candle starting 2026-10-27 16:15 UTC, last close 2340.41
- P(up) 0.5199, return quantiles (bp): {'05': -8.795, '10': -6.893, '25': -3.283, '40': -0.981, '50': 0.236, '60': 1.773, '75': 3.731, '90': 6.894, '95': 9.03}
- changepoint probability 0.2314, regime age 40.1 min
- agent weights: empirical 0.016, ewma 0.073, garch 0.112, har 0.120, bocpd 0.019, hmm 0.099, online_qr 0.240, lgbm 0.322

## Learning log

- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- 2026-10-26 12:00 UTC: {"garch": {"alpha": 0.1011, "beta": 0.8821}, "hmm": {"sd_bp": [3.43, 6.5, 17.71], "stay": [0.976, 0.954, 0.833]}}
- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- HMM volatility states (sd, bp per minute): [3.43, 6.6, 17.85], current probabilities: [0.887, 0.112, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-27 16:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.27, 'l_abs': 0.734, 'l_hi': 0.769, 'l_lo': 0.784, 'b05': 0.747, 'b25': 0.795, 'b75': 0.609, 'b95': 0.751}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.232, 1.922, 2.409, 2.491, 2.627, 3.142, 3.046, 3.437, 4.26, 3.971, 4.073, 4.164, 4.507, 4.229]}
- calibration offsets (in sigma): {'05': 0.027, '10': -0.036, '25': 0.025, '40': 0.026, '50': 0.03, '60': 0.064, '75': 0.045, '90': 0.036, '95': 0.033}
