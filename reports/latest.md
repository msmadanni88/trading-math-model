# ETH-USD 60s candle generator - report

- generated: 2026-11-27 11:29 UTC
- last closed candle: 2026-11-27 11:29 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.526 (95) | 0.504 (671) [0.475, 0.534] | 0.510 (2878) [0.495, 0.524] | 0.514 (8248) [0.505, 0.525] | 0.516 (5276) [0.502, 0.529] | 0.467 (45) | 0.500 | flat -0.022 (noise 0.027) |
| colour_clear | 0.596 (796) | 0.559 (5474) [0.547, 0.573] | 0.544 (23744) [0.537, 0.551] | 0.528 (67701) [0.522, 0.533] | 0.545 (43463) [0.541, 0.549] | 0.571 (373) | 0.500 | flat +0.013 (noise 0.010) |
| colour_confident | 0.550 (191) | 0.571 (1352) [0.556, 0.584] | 0.567 (4480) [0.557, 0.577] | 0.583 (8262) [0.574, 0.592] | 0.583 (8262) [0.574, 0.592] | 0.531 (81) | 0.500 | flat +0.015 (noise 0.020) |
| colour_next | 0.563 (1431) | 0.539 (10043) [0.531, 0.548] | 0.532 (42905) [0.528, 0.537] | 0.520 (122957) [0.517, 0.524] | 0.531 (78608) [0.528, 0.534] | 0.543 (687) | 0.500 | flat +0.006 (noise 0.007) |
| colour_path | 0.492 (20034) | 0.501 (140602) [0.498, 0.504] | 0.502 (600670) [0.501, 0.503] | 0.501 (1721398) [0.500, 0.502] | 0.501 (1100512) [0.500, 0.502] | 0.509 (9618) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.463 (54) | 0.553 (407) [0.502, 0.596] | 0.592 (1179) [0.567, 0.614] | 0.612 (2220) [0.594, 0.628] | 0.612 (2220) [0.594, 0.628] | 0.500 (26) | 0.500 | flat -0.053 (noise 0.038) |
| reversal_k13_next | 0.292 (48) | 0.369 (371) [0.327, 0.414] | 0.335 (1824) [0.318, 0.353] | 0.317 (5618) [0.308, 0.327] | 0.328 (3513) [0.317, 0.340] | 0.333 (24) | 0.078 | up +0.070 (noise 0.033) |
| reversal_k13_now | 0.569 (51) | 0.624 (343) [0.576, 0.672] | 0.583 (1595) [0.563, 0.605] | 0.576 (4427) [0.564, 0.589] | 0.574 (2955) [0.558, 0.590] | 0.560 (25) | 0.078 | flat +0.064 (noise 0.043) |
| reversal_k3_next | 0.611 (126) | 0.598 (1046) [0.573, 0.622] | 0.601 (2732) [0.588, 0.615] | 0.590 (7614) [0.582, 0.598] | 0.591 (5174) [0.581, 0.601] | 0.714 (42) | 0.294 | flat +0.003 (noise 0.029) |
| reversal_k3_now | 0.962 (52) | 0.932 (411) [0.920, 0.945] | 0.928 (1741) [0.920, 0.936] | 0.935 (4932) [0.930, 0.940] | 0.931 (3169) [0.925, 0.938] | 0.963 (27) | 0.294 | flat -0.009 (noise 0.017) |
| reversal_k5_next | 0.507 (69) | 0.524 (374) [0.479, 0.579] | 0.510 (1711) [0.490, 0.531] | 0.486 (6330) [0.475, 0.498] | 0.483 (4340) [0.469, 0.497] | 0.423 (26) | 0.187 | flat +0.049 (noise 0.045) |
| reversal_k5_now | 0.892 (65) | 0.825 (440) [0.799, 0.851] | 0.796 (1811) [0.779, 0.812] | 0.817 (4743) [0.808, 0.827] | 0.807 (3132) [0.795, 0.818] | 0.893 (28) | 0.188 | flat +0.050 (noise 0.027) |
| reversal_k8_next | 0.431 (72) | 0.423 (546) [0.376, 0.471] | 0.421 (2178) [0.405, 0.440] | 0.399 (6695) [0.389, 0.409] | 0.400 (4589) [0.389, 0.412] | 0.379 (29) | 0.121 | flat +0.028 (noise 0.037) |
| reversal_k8_now | 0.729 (59) | 0.694 (409) [0.662, 0.724] | 0.687 (1670) [0.670, 0.704] | 0.695 (4568) [0.683, 0.707] | 0.685 (2981) [0.671, 0.699] | 0.720 (25) | 0.122 | flat +0.036 (noise 0.033) |
| overall | 0.500 (22102) | 0.506 (155256) [0.504, 0.509] | 0.506 (661715) [0.505, 0.507] | 0.504 (1897530) [0.504, 0.505] | 0.505 (1214249) [0.504, 0.506] | 0.513 (10576) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0846, 0.122] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5399, 'levels': [{'threshold': 0.0846, 'calls_per_day': 148.6, 'win_rate': 0.567}, {'threshold': 0.122, 'calls_per_day': 37.3, 'win_rate': 0.5611}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42910, 'rate': 0.533}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15110 | 0.355 | 0.537 (14892) | 0.558 (1976) | 0.755 (2578) |
| volatility: normal | 15109 | 0.380 | 0.526 (15055) | 0.563 (1541) | 0.750 (2436) |
| volatility: wild | 15110 | 0.392 | 0.535 (15075) | 0.589 (1205) | 0.762 (2143) |
| session: Asia 00-08 | 15360 | 0.374 | 0.534 (15253) | 0.559 (1664) | 0.748 (2329) |
| session: Europe 08-13 | 9509 | 0.370 | 0.531 (9432) | 0.576 (1146) | 0.772 (1514) |
| session: US 13-21 | 14880 | 0.382 | 0.536 (14791) | 0.596 (1325) | 0.748 (2432) |
| session: late 21-24 | 5580 | 0.370 | 0.522 (5546) | 0.511 (587) | 0.766 (882) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.416 | 0.384 | 0.333 | 0.333 | 0.525 | 0.323 | 0.509 | 1.073 |
| 6h | 360 | 0.379 | 0.372 | 0.279 | 0.326 | 0.525 | 0.264 | 0.495 | 1.247 |
| 24h | 1440 | 0.383 | 0.366 | 0.282 | 0.318 | 0.555 | 0.278 | 0.489 | 1.235 |
| 7d | 10080 | 0.387 | 0.377 | 0.292 | 0.326 | 0.540 | 0.271 | 0.502 | 1.213 |
| 30d | 43200 | 0.376 | 0.369 | 0.288 | 0.321 | 0.533 | 0.267 | 0.485 | 1.269 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.416 / 0.525 / 0.950; 2: 0.361 / 0.424 / 0.883; 3: 0.379 / 0.424 / 0.967; 4: 0.393 / 0.492 / 1.000; 5: 0.396 / 0.576 / 0.950; 6: 0.388 / 0.492 / 0.950; 7: 0.397 / 0.542 / 0.983; 8: 0.405 / 0.542 / 0.933; 9: 0.376 / 0.424 / 1.000; 10: 0.393 / 0.525 / 0.983; 11: 0.371 / 0.424 / 0.983; 12: 0.388 / 0.458 / 1.000; 13: 0.371 / 0.441 / 1.000; 14: 0.376 / 0.525 / 1.000; 15: 0.396 / 0.492 / 1.000
- 6h: 1: 0.379 / 0.525 / 0.914; 2: 0.360 / 0.472 / 0.931; 3: 0.374 / 0.520 / 0.983; 4: 0.368 / 0.492 / 0.994; 5: 0.358 / 0.472 / 0.972; 6: 0.370 / 0.517 / 0.978; 7: 0.374 / 0.531 / 0.989; 8: 0.368 / 0.511 / 0.986; 9: 0.361 / 0.489 / 0.997; 10: 0.363 / 0.492 / 0.989; 11: 0.350 / 0.453 / 0.992; 12: 0.357 / 0.472 / 0.997; 13: 0.364 / 0.517 / 0.997; 14: 0.365 / 0.506 / 1.000; 15: 0.374 / 0.545 / 1.000
- 24h: 1: 0.383 / 0.555 / 0.896; 2: 0.360 / 0.479 / 0.905; 3: 0.365 / 0.510 / 0.938; 4: 0.359 / 0.494 / 0.915; 5: 0.354 / 0.490 / 0.935; 6: 0.354 / 0.488 / 0.914; 7: 0.364 / 0.514 / 0.920; 8: 0.360 / 0.507 / 0.906; 9: 0.355 / 0.496 / 0.924; 10: 0.356 / 0.500 / 0.905; 11: 0.356 / 0.505 / 0.937; 12: 0.358 / 0.508 / 0.933; 13: 0.359 / 0.514 / 0.924; 14: 0.359 / 0.516 / 0.910; 15: 0.362 / 0.533 / 0.911
- 7d: 1: 0.387 / 0.540 / 0.900; 2: 0.368 / 0.487 / 0.901; 3: 0.371 / 0.507 / 0.903; 4: 0.367 / 0.497 / 0.902; 5: 0.368 / 0.499 / 0.902; 6: 0.365 / 0.495 / 0.901; 7: 0.368 / 0.507 / 0.902; 8: 0.367 / 0.507 / 0.903; 9: 0.364 / 0.495 / 0.902; 10: 0.367 / 0.511 / 0.902; 11: 0.365 / 0.503 / 0.901; 12: 0.367 / 0.506 / 0.902; 13: 0.362 / 0.492 / 0.903; 14: 0.363 / 0.499 / 0.903; 15: 0.364 / 0.506 / 0.903
- 30d: 1: 0.376 / 0.533 / 0.898; 2: 0.362 / 0.491 / 0.900; 3: 0.366 / 0.511 / 0.900; 4: 0.362 / 0.497 / 0.900; 5: 0.363 / 0.505 / 0.900; 6: 0.360 / 0.500 / 0.900; 7: 0.362 / 0.502 / 0.901; 8: 0.361 / 0.507 / 0.900; 9: 0.360 / 0.500 / 0.901; 10: 0.360 / 0.504 / 0.901; 11: 0.360 / 0.505 / 0.901; 12: 0.360 / 0.503 / 0.901; 13: 0.358 / 0.499 / 0.901; 14: 0.359 / 0.501 / 0.901; 15: 0.358 / 0.502 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.166 (body 0.116, range 0.216); 'price stays where it was' would score 0.124; colour right 0.441; typical miss of the close 6.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.150 (body 0.100, range 0.199); 'price stays where it was' would score 0.172; colour right 0.472; typical miss of the close 10.0 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.139 (body 0.092, range 0.186); 'price stays where it was' would score 0.157; colour right 0.486; typical miss of the close 9.6 bp; chain ended on the right side 0.463 of 95 chains; n=1440
- 7d: match 0.136 (body 0.088, range 0.183); 'price stays where it was' would score 0.145; colour right 0.497; typical miss of the close 13.1 bp; chain ended on the right side 0.501 of 671 chains; n=10080
- 30d: match 0.128 (body 0.085, range 0.171); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 11.1 bp; chain ended on the right side 0.507 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.372 / 6.0; 2: 0.206 / 6.8; 3: 0.168 / 8.9; 4: 0.136 / 9.2; 5: 0.125 / 9.9; 6: 0.119 / 10.8; 7: 0.118 / 11.1; 8: 0.104 / 12.2; 9: 0.093 / 13.0; 10: 0.090 / 13.3; 11: 0.087 / 13.8; 12: 0.082 / 14.0; 13: 0.077 / 14.9; 14: 0.071 / 15.4; 15: 0.068 / 15.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 167483, probability skill vs chance 0.2309, widened contest next: False
  - now: threshold 0.8299, hit rate recent 0.9482 / long run 0.9324
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.338, naive rule 0.567, lift 2.96x
    - 24h: 59 calls (59 a day), hit rate 0.949, chance 0.312, naive rule 0.525, lift 3.04x
    - 7d: 406 calls (58 a day), hit rate 0.933, chance 0.305, naive rule 0.527, lift 3.06x
    - 30d: 1733 calls (58 a day), hit rate 0.929, chance 0.295, naive rule 0.506, lift 3.15x
  - next: threshold 0.5392, hit rate recent 0.6712 / long run 0.6054
    - 6h: 25 calls (101 a day), hit rate 0.720, chance 0.338, lift 2.13x
    - 24h: 98 calls (98 a day), hit rate 0.694, chance 0.312, lift 2.22x
    - 7d: 1017 calls (145 a day), hit rate 0.606, chance 0.305, lift 1.99x
    - 30d: 2718 calls (91 a day), hit rate 0.603, chance 0.295, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.504; 0.35: 531, 0.529; 0.40: 483, 0.572; 0.45: 421, 0.634; 0.50: 370, 0.681; 0.55: 322, 0.727; 0.60: 272, 0.771; 0.65: 228, 0.801; 0.70: 179, 0.832; 0.75: 143, 0.869; 0.80: 95, 0.901; 0.85: 42, 0.943; 0.90: 3, 0.957
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.436; 0.35: 487, 0.471; 0.40: 382, 0.513; 0.45: 289, 0.545; 0.50: 186, 0.575; 0.55: 78, 0.595; 0.60: 10, 0.637; 0.65: 0, 0.545
- **K=5**: model 1794528000, labels learned 167481, probability skill vs chance 0.2272, widened contest next: False
  - now: threshold 0.7059, hit rate recent 0.8764 / long run 0.8109
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.204, naive rule 0.475, lift 4.90x
    - 24h: 66 calls (66 a day), hit rate 0.879, chance 0.206, naive rule 0.468, lift 4.27x
    - 7d: 441 calls (63 a day), hit rate 0.821, chance 0.196, naive rule 0.444, lift 4.19x
    - 30d: 1804 calls (60 a day), hit rate 0.797, chance 0.189, naive rule 0.418, lift 4.22x
  - next: threshold 0.447, hit rate recent 0.4732 / long run 0.4959
    - 6h: 18 calls (73 a day), hit rate 0.389, chance 0.204, lift 1.91x
    - 24h: 60 calls (60 a day), hit rate 0.483, chance 0.206, lift 2.35x
    - 7d: 380 calls (54 a day), hit rate 0.516, chance 0.196, lift 2.63x
    - 30d: 1701 calls (57 a day), hit rate 0.508, chance 0.189, lift 2.69x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.428; 0.35: 364, 0.476; 0.40: 295, 0.543; 0.45: 239, 0.603; 0.50: 186, 0.654; 0.55: 150, 0.686; 0.60: 116, 0.731; 0.65: 86, 0.768; 0.70: 55, 0.805; 0.75: 28, 0.841; 0.80: 6, 0.843
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 328, 0.397; 0.35: 244, 0.436; 0.40: 155, 0.462; 0.45: 63, 0.507; 0.50: 9, 0.551; 0.55: 0, 0.562
- **K=8**: model 1794960000, labels learned 167478, probability skill vs chance 0.2085, widened contest next: False
  - now: threshold 0.5884, hit rate recent 0.7385 / long run 0.6881
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.151, naive rule 0.447, lift 6.10x
    - 24h: 59 calls (59 a day), hit rate 0.729, chance 0.131, naive rule 0.391, lift 5.56x
    - 7d: 409 calls (58 a day), hit rate 0.687, chance 0.127, naive rule 0.375, lift 5.39x
    - 30d: 1668 calls (56 a day), hit rate 0.687, chance 0.124, naive rule 0.352, lift 5.54x
  - next: threshold 0.3776, hit rate recent 0.3977 / long run 0.4118
    - 6h: 18 calls (74 a day), hit rate 0.278, chance 0.151, lift 1.83x
    - 24h: 59 calls (59 a day), hit rate 0.458, chance 0.131, lift 3.49x
    - 7d: 542 calls (78 a day), hit rate 0.424, chance 0.127, lift 3.33x
    - 30d: 2156 calls (72 a day), hit rate 0.421, chance 0.124, lift 3.40x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.426; 0.35: 205, 0.486; 0.40: 160, 0.537; 0.45: 121, 0.580; 0.50: 87, 0.637; 0.55: 64, 0.675; 0.60: 44, 0.715; 0.65: 26, 0.774; 0.70: 9, 0.816; 0.75: 1, 0.727
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 156, 0.377; 0.35: 84, 0.410; 0.40: 30, 0.441; 0.45: 7, 0.481; 0.50: 1, 0.667
- **K=13**: model 1795478400, labels learned 167473, probability skill vs chance 0.1919, widened contest next: False
  - now: threshold 0.4558, hit rate recent 0.6061 / long run 0.5892
    - 6h: 11 calls (46 a day), hit rate 0.818, chance 0.077, naive rule 0.319, lift 10.65x
    - 24h: 57 calls (58 a day), hit rate 0.544, chance 0.081, naive rule 0.329, lift 6.71x
    - 7d: 349 calls (50 a day), hit rate 0.610, chance 0.084, naive rule 0.336, lift 7.23x
    - 30d: 1591 calls (53 a day), hit rate 0.583, chance 0.081, naive rule 0.303, lift 7.23x
  - next: threshold 0.3003, hit rate recent 0.3125 / long run 0.3362
    - 6h: 13 calls (54 a day), hit rate 0.154, chance 0.077, lift 2.00x
    - 24h: 45 calls (45 a day), hit rate 0.333, chance 0.081, lift 4.11x
    - 7d: 364 calls (52 a day), hit rate 0.368, chance 0.084, lift 4.36x
    - 30d: 1820 calls (61 a day), hit rate 0.336, chance 0.081, lift 4.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 144, 0.426; 0.35: 106, 0.475; 0.40: 72, 0.539; 0.45: 51, 0.586; 0.50: 36, 0.621; 0.55: 22, 0.644; 0.60: 10, 0.661; 0.65: 2, 0.517
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.339; 0.35: 16, 0.376; 0.40: 2, 0.432

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.926 | 1.94% | 0.950 | 0.400 | 0.250 | 0.458 | 0.381 |
| 6h | 16.519 | 1.08% | 0.897 | 0.489 | 0.250 | 0.494 | 0.443 |
| 24h | 17.466 | 2.99% | 0.897 | 0.496 | 0.250 | 0.496 | 0.522 |
| 7d | 24.437 | 4.78% | 0.901 | 0.500 | 0.250 | 0.511 | 0.667 |
| 30d | 20.280 | 4.86% | 0.900 | 0.500 | 0.250 | 0.507 | 0.702 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.202 | 14.007 | 14.003 | 14.024 | 14.160 | 14.311 | 13.823 | 13.897 | 13.910 | 13.926 |
| 6h | 16.699 | 16.671 | 16.609 | 16.486 | 16.933 | 16.687 | 16.446 | 16.458 | 16.469 | 16.519 |
| 24h | 18.005 | 17.673 | 17.569 | 17.462 | 17.958 | 17.653 | 17.420 | 17.412 | 17.424 | 17.466 |
| 7d | 25.663 | 24.736 | 24.631 | 24.456 | 25.074 | 24.825 | 24.426 | 24.369 | 24.400 | 24.437 |
| 30d | 21.315 | 20.475 | 20.424 | 20.334 | 20.720 | 20.629 | 20.261 | 20.234 | 20.246 | 20.280 |

## Next candle

- candle starting 2026-11-27 11:29 UTC, last close 1725.53
- P(up) 0.5022, return quantiles (bp): {'05': -8.08, '10': -5.768, '25': -3.048, '40': -0.738, '50': -0.017, '60': 1.404, '75': 3.18, '90': 6.116, '95': 7.746}
- changepoint probability 0.0404, regime age 144.2 min
- agent weights: empirical 0.015, ewma 0.065, garch 0.113, har 0.199, bocpd 0.012, hmm 0.056, online_qr 0.277, lgbm 0.265

## Learning log

- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- 2026-11-25 12:00 UTC: {"garch": {"alpha": 0.091, "beta": 0.8903}, "hmm": {"sd_bp": [4.89, 9.77, 34.58], "stay": [0.96, 0.954, 0.849]}}
- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- 2026-11-26 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.8951}, "hmm": {"sd_bp": [5.1, 9.79, 29.67], "stay": [0.964, 0.952, 0.897]}}
- 2026-11-27 00:00 UTC: {"garch": {"alpha": 0.086, "beta": 0.8972}, "hmm": {"sd_bp": [4.98, 9.67, 29.65], "stay": [0.967, 0.957, 0.909]}, "lgbm": {"challenger_loss": 0.24936, "champion_loss": 0.2495, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48669, "challengers": 1, "chance_loss": 0.61724, "widened": false, "champion_loss": 0.48438, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37811, "challengers": 1, "chance_loss": 0.49376, "widened": false, "champion_loss": 0.37659, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27446, "challengers": 1, "chance_loss": 0.3744, "widened": false, "champion_loss": 0.27383, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21177, "challengers": 1, "chance_loss": 0.29738, "widened": false, "champion_loss": 0.21069, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.98, 9.67, 29.65], current probabilities: [0.82, 0.178, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-27 11:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.508, 'l_abs': 0.685, 'l_hi': 0.707, 'l_lo': 0.731, 'b05': 0.701, 'b25': 0.689, 'b75': 0.688, 'b95': 0.706}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.6], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.5]], 'cone_width': [1.128, 1.111, 1.57, 1.469, 1.747, 1.711, 1.761, 1.987, 2.057, 2.162, 2.174, 2.36, 2.176, 2.445]}
- calibration offsets (in sigma): {'05': 0.004, '10': 0.048, '25': -0.01, '40': 0.032, '50': -0.02, '60': 0.018, '75': -0.0, '90': -0.018, '95': -0.084}
