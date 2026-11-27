# ETH-USD 60s candle generator - report

- generated: 2026-11-27 02:49 UTC
- last closed candle: 2026-11-27 02:49 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.526 (95) | 0.504 (671) [0.475, 0.534] | 0.510 (2878) [0.495, 0.524] | 0.514 (8248) [0.505, 0.525] | 0.516 (5276) [0.502, 0.529] | 0.364 (11) | 0.500 | flat -0.022 (noise 0.027) |
| colour_clear | 0.596 (796) | 0.559 (5474) [0.547, 0.573] | 0.544 (23744) [0.537, 0.551] | 0.528 (67701) [0.522, 0.533] | 0.545 (43463) [0.541, 0.549] | 0.566 (106) | 0.500 | flat +0.013 (noise 0.010) |
| colour_confident | 0.550 (191) | 0.571 (1352) [0.556, 0.584] | 0.567 (4480) [0.557, 0.577] | 0.583 (8262) [0.574, 0.592] | 0.583 (8262) [0.574, 0.592] | 0.526 (38) | 0.500 | flat +0.015 (noise 0.020) |
| colour_next | 0.563 (1431) | 0.539 (10043) [0.531, 0.548] | 0.532 (42905) [0.528, 0.537] | 0.520 (122957) [0.517, 0.524] | 0.531 (78608) [0.528, 0.534] | 0.556 (169) | 0.500 | flat +0.006 (noise 0.007) |
| colour_path | 0.492 (20034) | 0.501 (140602) [0.498, 0.504] | 0.502 (600670) [0.501, 0.503] | 0.501 (1721398) [0.500, 0.502] | 0.501 (1100512) [0.500, 0.502] | 0.503 (2366) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.463 (54) | 0.553 (407) [0.502, 0.596] | 0.592 (1179) [0.567, 0.614] | 0.612 (2220) [0.594, 0.628] | 0.612 (2220) [0.594, 0.628] | 0.444 (18) | 0.500 | flat -0.053 (noise 0.038) |
| reversal_k13_next | 0.292 (48) | 0.369 (371) [0.327, 0.414] | 0.335 (1824) [0.318, 0.353] | 0.317 (5618) [0.308, 0.327] | 0.328 (3513) [0.317, 0.340] | 0.400 (5) | 0.078 | up +0.070 (noise 0.033) |
| reversal_k13_now | 0.569 (51) | 0.624 (343) [0.576, 0.672] | 0.583 (1595) [0.563, 0.605] | 0.576 (4427) [0.564, 0.589] | 0.574 (2955) [0.558, 0.590] | 0.286 (7) | 0.078 | flat +0.064 (noise 0.043) |
| reversal_k3_next | 0.611 (126) | 0.598 (1046) [0.573, 0.622] | 0.601 (2732) [0.588, 0.615] | 0.590 (7614) [0.582, 0.598] | 0.591 (5174) [0.581, 0.601] | 0.692 (13) | 0.294 | flat +0.003 (noise 0.029) |
| reversal_k3_now | 0.962 (52) | 0.932 (411) [0.920, 0.945] | 0.928 (1741) [0.920, 0.936] | 0.935 (4932) [0.930, 0.940] | 0.931 (3169) [0.925, 0.938] | 1.000 (7) | 0.294 | flat -0.009 (noise 0.017) |
| reversal_k5_next | 0.507 (69) | 0.524 (374) [0.479, 0.579] | 0.510 (1711) [0.490, 0.531] | 0.486 (6330) [0.475, 0.498] | 0.483 (4340) [0.469, 0.497] | 0.500 (6) | 0.187 | flat +0.049 (noise 0.045) |
| reversal_k5_now | 0.892 (65) | 0.825 (440) [0.799, 0.851] | 0.796 (1811) [0.779, 0.812] | 0.817 (4743) [0.808, 0.827] | 0.807 (3132) [0.795, 0.818] | 0.889 (9) | 0.188 | flat +0.050 (noise 0.027) |
| reversal_k8_next | 0.431 (72) | 0.423 (546) [0.376, 0.471] | 0.421 (2178) [0.405, 0.440] | 0.399 (6695) [0.389, 0.409] | 0.400 (4589) [0.389, 0.412] | 0.600 (5) | 0.121 | flat +0.028 (noise 0.037) |
| reversal_k8_now | 0.729 (59) | 0.694 (409) [0.662, 0.724] | 0.687 (1670) [0.670, 0.704] | 0.695 (4568) [0.683, 0.707] | 0.685 (2981) [0.671, 0.699] | 0.286 (7) | 0.122 | flat +0.036 (noise 0.033) |
| overall | 0.500 (22102) | 0.506 (155256) [0.504, 0.509] | 0.506 (661715) [0.505, 0.507] | 0.504 (1897530) [0.504, 0.505] | 0.505 (1214249) [0.504, 0.506] | 0.509 (2605) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08348, 0.1203] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5398, 'levels': [{'threshold': 0.08348, 'calls_per_day': 148.3, 'win_rate': 0.571}, {'threshold': 0.1203, 'calls_per_day': 37.7, 'win_rate': 0.566}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42904, 'rate': 0.5324}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14937 | 0.354 | 0.537 (14719) | 0.557 (1963) | 0.753 (2546) |
| volatility: normal | 14936 | 0.380 | 0.526 (14883) | 0.565 (1526) | 0.751 (2413) |
| volatility: wild | 14936 | 0.392 | 0.534 (14902) | 0.590 (1190) | 0.760 (2123) |
| session: Asia 00-08 | 15049 | 0.374 | 0.534 (14943) | 0.559 (1641) | 0.747 (2283) |
| session: Europe 08-13 | 9300 | 0.370 | 0.531 (9224) | 0.577 (1126) | 0.769 (1485) |
| session: US 13-21 | 14880 | 0.382 | 0.536 (14791) | 0.596 (1325) | 0.748 (2432) |
| session: late 21-24 | 5580 | 0.370 | 0.522 (5546) | 0.511 (587) | 0.766 (882) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.383 | 0.342 | 0.293 | 0.293 | 0.550 | 0.288 | 0.478 | 1.401 |
| 6h | 360 | 0.369 | 0.351 | 0.280 | 0.310 | 0.546 | 0.263 | 0.476 | 1.183 |
| 24h | 1440 | 0.388 | 0.367 | 0.287 | 0.317 | 0.568 | 0.284 | 0.492 | 1.196 |
| 7d | 10080 | 0.387 | 0.378 | 0.294 | 0.327 | 0.539 | 0.271 | 0.503 | 1.216 |
| 30d | 43200 | 0.375 | 0.369 | 0.288 | 0.320 | 0.532 | 0.267 | 0.484 | 1.269 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.383 / 0.550 / 0.850; 2: 0.342 / 0.417 / 0.817; 3: 0.353 / 0.533 / 0.783; 4: 0.336 / 0.483 / 0.700; 5: 0.351 / 0.517 / 0.750; 6: 0.342 / 0.533 / 0.717; 7: 0.325 / 0.483 / 0.700; 8: 0.316 / 0.450 / 0.717; 9: 0.329 / 0.483 / 0.617; 10: 0.316 / 0.467 / 0.650; 11: 0.314 / 0.450 / 0.650; 12: 0.328 / 0.517 / 0.650; 13: 0.317 / 0.467 / 0.633; 14: 0.333 / 0.517 / 0.633; 15: 0.328 / 0.517 / 0.600
- 6h: 1: 0.369 / 0.546 / 0.861; 2: 0.353 / 0.490 / 0.883; 3: 0.348 / 0.487 / 0.808; 4: 0.346 / 0.493 / 0.750; 5: 0.337 / 0.476 / 0.822; 6: 0.343 / 0.493 / 0.803; 7: 0.348 / 0.527 / 0.800; 8: 0.347 / 0.493 / 0.844; 9: 0.340 / 0.499 / 0.797; 10: 0.342 / 0.499 / 0.839; 11: 0.346 / 0.513 / 0.833; 12: 0.347 / 0.524 / 0.844; 13: 0.344 / 0.479 / 0.825; 14: 0.346 / 0.499 / 0.828; 15: 0.351 / 0.527 / 0.794
- 24h: 1: 0.388 / 0.568 / 0.893; 2: 0.359 / 0.465 / 0.897; 3: 0.364 / 0.495 / 0.876; 4: 0.361 / 0.493 / 0.868; 5: 0.357 / 0.493 / 0.876; 6: 0.357 / 0.486 / 0.879; 7: 0.361 / 0.503 / 0.876; 8: 0.359 / 0.491 / 0.902; 9: 0.358 / 0.491 / 0.872; 10: 0.355 / 0.488 / 0.895; 11: 0.360 / 0.506 / 0.873; 12: 0.360 / 0.505 / 0.874; 13: 0.357 / 0.493 / 0.875; 14: 0.358 / 0.497 / 0.894; 15: 0.358 / 0.508 / 0.887
- 7d: 1: 0.387 / 0.539 / 0.900; 2: 0.369 / 0.488 / 0.900; 3: 0.372 / 0.507 / 0.899; 4: 0.368 / 0.496 / 0.896; 5: 0.370 / 0.502 / 0.899; 6: 0.367 / 0.495 / 0.898; 7: 0.368 / 0.505 / 0.899; 8: 0.368 / 0.506 / 0.899; 9: 0.366 / 0.496 / 0.898; 10: 0.368 / 0.513 / 0.901; 11: 0.367 / 0.504 / 0.901; 12: 0.368 / 0.506 / 0.898; 13: 0.363 / 0.491 / 0.897; 14: 0.363 / 0.497 / 0.898; 15: 0.364 / 0.505 / 0.897
- 30d: 1: 0.375 / 0.532 / 0.898; 2: 0.361 / 0.490 / 0.900; 3: 0.365 / 0.511 / 0.899; 4: 0.361 / 0.497 / 0.899; 5: 0.362 / 0.505 / 0.900; 6: 0.360 / 0.500 / 0.900; 7: 0.361 / 0.502 / 0.900; 8: 0.361 / 0.507 / 0.900; 9: 0.359 / 0.500 / 0.899; 10: 0.360 / 0.504 / 0.900; 11: 0.360 / 0.505 / 0.900; 12: 0.359 / 0.503 / 0.900; 13: 0.358 / 0.499 / 0.900; 14: 0.358 / 0.501 / 0.900; 15: 0.358 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.132 (body 0.101, range 0.164); 'price stays where it was' would score 0.150; colour right 0.533; typical miss of the close 23.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.117 (body 0.077, range 0.156); 'price stays where it was' would score 0.121; colour right 0.529; typical miss of the close 9.6 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.142 (body 0.095, range 0.188); 'price stays where it was' would score 0.147; colour right 0.491; typical miss of the close 9.0 bp; chain ended on the right side 0.484 of 95 chains; n=1440
- 7d: match 0.136 (body 0.088, range 0.183); 'price stays where it was' would score 0.145; colour right 0.498; typical miss of the close 13.3 bp; chain ended on the right side 0.502 of 671 chains; n=10080
- 30d: match 0.128 (body 0.085, range 0.170); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 11.0 bp; chain ended on the right side 0.509 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.372 / 5.9; 2: 0.206 / 6.7; 3: 0.167 / 8.8; 4: 0.137 / 9.0; 5: 0.125 / 9.9; 6: 0.119 / 10.7; 7: 0.117 / 11.1; 8: 0.104 / 12.2; 9: 0.093 / 12.9; 10: 0.090 / 13.2; 11: 0.087 / 13.8; 12: 0.082 / 14.0; 13: 0.076 / 14.9; 14: 0.071 / 15.3; 15: 0.068 / 15.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 166963, probability skill vs chance 0.2339, widened contest next: False
  - now: threshold 0.8303, hit rate recent 0.9451 / long run 0.9318
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.286, naive rule 0.455, lift 3.50x
    - 24h: 56 calls (56 a day), hit rate 0.964, chance 0.313, naive rule 0.528, lift 3.09x
    - 7d: 404 calls (58 a day), hit rate 0.933, chance 0.303, naive rule 0.523, lift 3.08x
    - 30d: 1740 calls (58 a day), hit rate 0.929, chance 0.295, naive rule 0.505, lift 3.15x
  - next: threshold 0.5435, hit rate recent 0.6364 / long run 0.5995
    - 6h: 27 calls (110 a day), hit rate 0.593, chance 0.286, lift 2.07x
    - 24h: 117 calls (117 a day), hit rate 0.658, chance 0.313, lift 2.11x
    - 7d: 1041 calls (149 a day), hit rate 0.599, chance 0.303, lift 1.98x
    - 30d: 2734 calls (91 a day), hit rate 0.601, chance 0.295, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.504; 0.35: 530, 0.529; 0.40: 482, 0.572; 0.45: 420, 0.634; 0.50: 369, 0.681; 0.55: 322, 0.726; 0.60: 272, 0.771; 0.65: 228, 0.801; 0.70: 179, 0.832; 0.75: 143, 0.869; 0.80: 95, 0.900; 0.85: 42, 0.942; 0.90: 3, 0.957
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.435; 0.35: 486, 0.470; 0.40: 383, 0.512; 0.45: 290, 0.544; 0.50: 187, 0.574; 0.55: 78, 0.592; 0.60: 10, 0.636; 0.65: 0, 0.500
- **K=5**: model 1794528000, labels learned 166961, probability skill vs chance 0.2314, widened contest next: False
  - now: threshold 0.705, hit rate recent 0.8655 / long run 0.8082
    - 6h: 21 calls (86 a day), hit rate 0.905, chance 0.203, naive rule 0.424, lift 4.47x
    - 24h: 70 calls (70 a day), hit rate 0.886, chance 0.205, naive rule 0.458, lift 4.32x
    - 7d: 439 calls (63 a day), hit rate 0.825, chance 0.195, naive rule 0.441, lift 4.22x
    - 30d: 1808 calls (60 a day), hit rate 0.796, chance 0.188, naive rule 0.417, lift 4.23x
  - next: threshold 0.449, hit rate recent 0.4976 / long run 0.4991
    - 6h: 15 calls (61 a day), hit rate 0.467, chance 0.203, lift 2.30x
    - 24h: 70 calls (70 a day), hit rate 0.529, chance 0.205, lift 2.58x
    - 7d: 375 calls (54 a day), hit rate 0.525, chance 0.195, lift 2.69x
    - 30d: 1710 calls (57 a day), hit rate 0.509, chance 0.188, lift 2.70x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.427; 0.35: 364, 0.475; 0.40: 295, 0.542; 0.45: 239, 0.602; 0.50: 186, 0.654; 0.55: 149, 0.685; 0.60: 116, 0.731; 0.65: 86, 0.768; 0.70: 55, 0.804; 0.75: 28, 0.839; 0.80: 6, 0.841
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 329, 0.397; 0.35: 245, 0.435; 0.40: 156, 0.461; 0.45: 63, 0.507; 0.50: 9, 0.558; 0.55: 0, 0.562
- **K=8**: model 1794960000, labels learned 166958, probability skill vs chance 0.2109, widened contest next: False
  - now: threshold 0.5874, hit rate recent 0.6837 / long run 0.6819
    - 6h: 18 calls (74 a day), hit rate 0.667, chance 0.131, naive rule 0.356, lift 5.07x
    - 24h: 64 calls (64 a day), hit rate 0.672, chance 0.121, naive rule 0.368, lift 5.54x
    - 7d: 409 calls (58 a day), hit rate 0.685, chance 0.126, naive rule 0.372, lift 5.41x
    - 30d: 1668 calls (56 a day), hit rate 0.685, chance 0.124, naive rule 0.352, lift 5.54x
  - next: threshold 0.3778, hit rate recent 0.4259 / long run 0.415
    - 6h: 11 calls (45 a day), hit rate 0.364, chance 0.131, lift 2.77x
    - 24h: 63 calls (63 a day), hit rate 0.460, chance 0.121, lift 3.79x
    - 7d: 546 calls (78 a day), hit rate 0.425, chance 0.126, lift 3.36x
    - 30d: 2174 calls (72 a day), hit rate 0.422, chance 0.124, lift 3.41x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 260, 0.425; 0.35: 205, 0.485; 0.40: 160, 0.537; 0.45: 121, 0.580; 0.50: 87, 0.635; 0.55: 64, 0.673; 0.60: 44, 0.713; 0.65: 25, 0.769; 0.70: 10, 0.807; 0.75: 1, 0.722
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.377; 0.35: 84, 0.410; 0.40: 30, 0.443; 0.45: 7, 0.484; 0.50: 1, 0.684
- **K=13**: model 1795478400, labels learned 166953, probability skill vs chance 0.1924, widened contest next: False
  - now: threshold 0.4551, hit rate recent 0.5805 / long run 0.5868
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.086, naive rule 0.301, lift 5.01x
    - 24h: 56 calls (57 a day), hit rate 0.518, chance 0.081, naive rule 0.325, lift 6.42x
    - 7d: 344 calls (49 a day), hit rate 0.616, chance 0.085, naive rule 0.336, lift 7.27x
    - 30d: 1593 calls (53 a day), hit rate 0.581, chance 0.081, naive rule 0.302, lift 7.22x
  - next: threshold 0.3016, hit rate recent 0.3147 / long run 0.3369
    - 6h: 11 calls (46 a day), hit rate 0.364, chance 0.086, lift 4.25x
    - 24h: 46 calls (46 a day), hit rate 0.326, chance 0.081, lift 4.04x
    - 7d: 369 calls (53 a day), hit rate 0.369, chance 0.085, lift 4.35x
    - 30d: 1822 calls (61 a day), hit rate 0.335, chance 0.081, lift 4.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 143, 0.426; 0.35: 106, 0.473; 0.40: 72, 0.537; 0.45: 51, 0.585; 0.50: 36, 0.619; 0.55: 22, 0.642; 0.60: 10, 0.658; 0.65: 2, 0.517
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.340; 0.35: 15, 0.379; 0.40: 2, 0.438

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 40.750 | 9.41% | 0.883 | 0.450 | 0.251 | 0.433 | 0.286 |
| 6h | 18.464 | 4.15% | 0.872 | 0.486 | 0.251 | 0.471 | 0.532 |
| 24h | 16.384 | 5.25% | 0.899 | 0.497 | 0.250 | 0.503 | 0.533 |
| 7d | 24.650 | 4.73% | 0.901 | 0.500 | 0.250 | 0.511 | 0.664 |
| 30d | 20.197 | 4.88% | 0.900 | 0.500 | 0.250 | 0.507 | 0.704 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 44.982 | 41.285 | 40.894 | 40.778 | 42.774 | 41.303 | 40.591 | 40.722 | 40.683 | 40.750 |
| 6h | 19.262 | 18.600 | 18.509 | 18.462 | 18.981 | 18.695 | 18.405 | 18.470 | 18.412 | 18.464 |
| 24h | 17.292 | 16.525 | 16.477 | 16.392 | 16.810 | 16.583 | 16.354 | 16.337 | 16.346 | 16.384 |
| 7d | 25.875 | 24.934 | 24.834 | 24.673 | 25.270 | 25.033 | 24.641 | 24.584 | 24.612 | 24.650 |
| 30d | 21.234 | 20.391 | 20.341 | 20.252 | 20.635 | 20.545 | 20.178 | 20.151 | 20.164 | 20.197 |

## Next candle

- candle starting 2026-11-27 02:49 UTC, last close 1722.4
- P(up) 0.5119, return quantiles (bp): {'05': -17.588, '10': -13.169, '25': -6.43, '40': -2.052, '50': 0.266, '60': 2.896, '75': 7.289, '90': 13.991, '95': 17.809}
- changepoint probability 0.1297, regime age 21.6 min
- agent weights: empirical 0.003, ewma 0.081, garch 0.124, har 0.191, bocpd 0.010, hmm 0.048, online_qr 0.290, lgbm 0.253

## Learning log

- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- 2026-11-25 12:00 UTC: {"garch": {"alpha": 0.091, "beta": 0.8903}, "hmm": {"sd_bp": [4.89, 9.77, 34.58], "stay": [0.96, 0.954, 0.849]}}
- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- 2026-11-26 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.8951}, "hmm": {"sd_bp": [5.1, 9.79, 29.67], "stay": [0.964, 0.952, 0.897]}}
- 2026-11-27 00:00 UTC: {"garch": {"alpha": 0.086, "beta": 0.8972}, "hmm": {"sd_bp": [4.98, 9.67, 29.65], "stay": [0.967, 0.957, 0.909]}, "lgbm": {"challenger_loss": 0.24936, "champion_loss": 0.2495, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48669, "challengers": 1, "chance_loss": 0.61724, "widened": false, "champion_loss": 0.48438, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37811, "challengers": 1, "chance_loss": 0.49376, "widened": false, "champion_loss": 0.37659, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27446, "challengers": 1, "chance_loss": 0.3744, "widened": false, "champion_loss": 0.27383, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21177, "challengers": 1, "chance_loss": 0.29738, "widened": false, "champion_loss": 0.21069, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.98, 9.67, 29.65], current probabilities: [0.219, 0.772, 0.009]
- live generator: {'versions': 60, 'latest_effective': '2026-11-27 03:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.516, 'l_abs': 0.686, 'l_hi': 0.747, 'l_lo': 0.733, 'b05': 0.706, 'b25': 0.688, 'b75': 0.643, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.5], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.554, 2.733, 4.101, 3.142, 3.811, 4.043, 3.998, 5.189, 4.671, 4.811, 5.035, 5.689, 5.683, 6.514]}
- calibration offsets (in sigma): {'05': 0.024, '10': 0.018, '25': 0.03, '40': 0.042, '50': 0.03, '60': 0.038, '75': 0.04, '90': 0.022, '95': -0.054}
