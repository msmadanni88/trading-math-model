# ETH-USD 60s candle generator - report

- generated: 2026-10-29 07:16 UTC
- last closed candle: 2026-10-29 07:16 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.537 (672) [0.501, 0.573] | 0.520 (2876) [0.501, 0.539] | 0.517 (5466) [0.503, 0.531] | 0.524 (2494) [0.504, 0.546] | 0.379 (29) | 0.500 | flat -0.006 (noise 0.031) |
| colour_clear | 0.537 (786) | 0.542 (5666) [0.539, 0.547] | 0.538 (23626) [0.531, 0.545] | 0.519 (44743) [0.513, 0.525] | 0.546 (20505) [0.541, 0.550] | 0.508 (238) | 0.500 | flat -0.013 (noise 0.009) |
| colour_confident | 0.567 (120) | 0.601 (1315) [0.586, 0.617] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.625 (40) | 0.500 | flat +0.001 (noise 0.021) |
| colour_next | 0.531 (1431) | 0.528 (10027) [0.525, 0.531] | 0.526 (42877) [0.521, 0.530] | 0.514 (81483) [0.510, 0.518] | 0.529 (37134) [0.526, 0.533] | 0.524 (433) | 0.500 | flat -0.006 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.502 (140378) [0.500, 0.504] | 0.501 (600278) [0.499, 0.502] | 0.501 (1140762) [0.500, 0.502] | 0.501 (519876) [0.499, 0.502] | 0.498 (6062) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.500 (32) | 0.607 (405) [0.583, 0.639] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 1.000 (7) | 0.500 | flat -0.024 (noise 0.040) |
| reversal_k13_next | 0.302 (53) | 0.317 (410) [0.283, 0.357] | 0.310 (2116) [0.298, 0.323] | 0.309 (3847) [0.299, 0.320] | 0.320 (1742) [0.308, 0.332] | 0.167 (12) | 0.077 | flat -0.007 (noise 0.032) |
| reversal_k13_now | 0.603 (63) | 0.568 (391) [0.519, 0.620] | 0.562 (1632) [0.542, 0.584] | 0.573 (2895) [0.558, 0.589] | 0.565 (1423) [0.543, 0.589] | 0.333 (18) | 0.077 | flat +0.043 (noise 0.036) |
| reversal_k3_next | 0.591 (115) | 0.593 (648) [0.584, 0.603] | 0.583 (2896) [0.572, 0.596] | 0.584 (4997) [0.574, 0.594] | 0.580 (2557) [0.568, 0.594] | 0.524 (42) | 0.293 | flat +0.016 (noise 0.026) |
| reversal_k3_now | 0.909 (66) | 0.942 (399) [0.918, 0.964] | 0.935 (1742) [0.926, 0.945] | 0.938 (3257) [0.931, 0.945] | 0.934 (1494) [0.923, 0.944] | 1.000 (19) | 0.293 | flat +0.010 (noise 0.021) |
| reversal_k5_next | 0.500 (64) | 0.501 (766) [0.491, 0.512] | 0.468 (3071) [0.455, 0.482] | 0.478 (4683) [0.466, 0.491] | 0.466 (2693) [0.452, 0.481] | 0.471 (17) | 0.187 | up +0.067 (noise 0.024) |
| reversal_k5_now | 0.838 (74) | 0.828 (389) [0.816, 0.837] | 0.826 (1616) [0.814, 0.837] | 0.830 (3006) [0.820, 0.840] | 0.822 (1395) [0.810, 0.834] | 0.812 (16) | 0.187 | flat +0.011 (noise 0.028) |
| reversal_k8_next | 0.446 (101) | 0.387 (744) [0.364, 0.410] | 0.384 (2742) [0.371, 0.397] | 0.389 (4618) [0.378, 0.400] | 0.383 (2512) [0.369, 0.396] | 0.250 (32) | 0.120 | flat +0.022 (noise 0.025) |
| reversal_k8_now | 0.770 (61) | 0.683 (369) [0.628, 0.736] | 0.689 (1559) [0.667, 0.709] | 0.701 (2959) [0.686, 0.716] | 0.687 (1372) [0.663, 0.710] | 0.533 (15) | 0.121 | flat +0.016 (noise 0.038) |
| overall | 0.508 (22158) | 0.506 (155193) [0.503, 0.508] | 0.504 (663405) [0.503, 0.506] | 0.503 (1257973) [0.502, 0.504] | 0.504 (574692) [0.503, 0.506] | 0.500 (6695) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08101, 0.1231] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5273, 'levels': [{'threshold': 0.08101, 'calls_per_day': 144.8, 'win_rate': 0.6094}, {'threshold': 0.1231, 'calls_per_day': 36.4, 'win_rate': 0.6133}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 36428, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15026 | 0.340 | 0.523 (14801) | 0.583 (1977) | 0.751 (2560) |
| volatility: normal | 15025 | 0.366 | 0.530 (14959) | 0.613 (1314) | 0.750 (2232) |
| volatility: wild | 15025 | 0.380 | 0.523 (14984) | 0.634 (651) | 0.770 (1979) |
| session: Asia 00-08 | 15316 | 0.361 | 0.531 (15213) | 0.604 (1419) | 0.758 (2281) |
| session: Europe 08-13 | 9300 | 0.358 | 0.530 (9217) | 0.593 (964) | 0.747 (1501) |
| session: US 13-21 | 14880 | 0.370 | 0.521 (14788) | 0.602 (1002) | 0.765 (2142) |
| session: late 21-24 | 5580 | 0.351 | 0.516 (5526) | 0.610 (557) | 0.744 (847) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.361 | 0.364 | 0.264 | 0.264 | 0.576 | 0.264 | 0.458 | 1.260 |
| 6h | 360 | 0.357 | 0.360 | 0.270 | 0.295 | 0.541 | 0.240 | 0.474 | 1.230 |
| 24h | 1440 | 0.367 | 0.367 | 0.276 | 0.308 | 0.534 | 0.258 | 0.475 | 1.337 |
| 7d | 10080 | 0.367 | 0.359 | 0.279 | 0.311 | 0.527 | 0.264 | 0.470 | 1.251 |
| 30d | 43200 | 0.361 | 0.355 | 0.277 | 0.306 | 0.526 | 0.258 | 0.464 | 1.279 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.361 / 0.576 / 0.933; 2: 0.378 / 0.644 / 0.850; 3: 0.361 / 0.542 / 0.933; 4: 0.358 / 0.542 / 0.950; 5: 0.357 / 0.492 / 0.950; 6: 0.320 / 0.424 / 0.983; 7: 0.370 / 0.508 / 0.983; 8: 0.353 / 0.492 / 0.967; 9: 0.352 / 0.475 / 0.967; 10: 0.339 / 0.492 / 0.917; 11: 0.328 / 0.508 / 0.917; 12: 0.335 / 0.424 / 0.900; 13: 0.297 / 0.407 / 0.967; 14: 0.318 / 0.441 / 0.983; 15: 0.334 / 0.424 / 0.917
- 6h: 1: 0.357 / 0.541 / 0.917; 2: 0.359 / 0.538 / 0.886; 3: 0.351 / 0.499 / 0.894; 4: 0.363 / 0.518 / 0.892; 5: 0.351 / 0.501 / 0.903; 6: 0.337 / 0.465 / 0.925; 7: 0.361 / 0.504 / 0.922; 8: 0.356 / 0.524 / 0.875; 9: 0.361 / 0.527 / 0.903; 10: 0.353 / 0.501 / 0.867; 11: 0.337 / 0.459 / 0.881; 12: 0.347 / 0.482 / 0.861; 13: 0.339 / 0.473 / 0.903; 14: 0.357 / 0.518 / 0.911; 15: 0.345 / 0.490 / 0.875
- 24h: 1: 0.367 / 0.534 / 0.918; 2: 0.354 / 0.498 / 0.895; 3: 0.355 / 0.501 / 0.897; 4: 0.359 / 0.504 / 0.894; 5: 0.350 / 0.498 / 0.893; 6: 0.347 / 0.494 / 0.899; 7: 0.356 / 0.499 / 0.900; 8: 0.354 / 0.520 / 0.893; 9: 0.355 / 0.517 / 0.898; 10: 0.355 / 0.507 / 0.892; 11: 0.348 / 0.497 / 0.895; 12: 0.352 / 0.501 / 0.889; 13: 0.342 / 0.487 / 0.895; 14: 0.354 / 0.510 / 0.897; 15: 0.348 / 0.501 / 0.895
- 7d: 1: 0.367 / 0.527 / 0.899; 2: 0.355 / 0.497 / 0.900; 3: 0.358 / 0.511 / 0.900; 4: 0.354 / 0.500 / 0.900; 5: 0.353 / 0.504 / 0.900; 6: 0.351 / 0.503 / 0.900; 7: 0.352 / 0.499 / 0.900; 8: 0.354 / 0.510 / 0.899; 9: 0.353 / 0.504 / 0.900; 10: 0.353 / 0.504 / 0.899; 11: 0.350 / 0.502 / 0.899; 12: 0.353 / 0.505 / 0.898; 13: 0.349 / 0.497 / 0.899; 14: 0.350 / 0.501 / 0.899; 15: 0.351 / 0.500 / 0.899
- 30d: 1: 0.361 / 0.526 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.901; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.347 / 0.498 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.505 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.097 (body 0.058, range 0.136); 'price stays where it was' would score 0.131; colour right 0.559; typical miss of the close 8.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.082, range 0.171); 'price stays where it was' would score 0.111; colour right 0.524; typical miss of the close 11.0 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.131 (body 0.089, range 0.172); 'price stays where it was' would score 0.132; colour right 0.502; typical miss of the close 9.7 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.136; colour right 0.497; typical miss of the close 8.6 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.129; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.519 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.198 / 4.6; 3: 0.169 / 6.0; 4: 0.134 / 6.5; 5: 0.127 / 7.2; 6: 0.113 / 7.7; 7: 0.108 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.6; 10: 0.087 / 9.3; 11: 0.085 / 9.7; 12: 0.077 / 9.9; 13: 0.067 / 10.2; 14: 0.072 / 10.5; 15: 0.062 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 125470, probability skill vs chance 0.2253, widened contest next: False
  - now: threshold 0.8347, hit rate recent 0.9496 / long run 0.9402
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.275, naive rule 0.474, lift 3.64x
    - 24h: 64 calls (64 a day), hit rate 0.938, chance 0.282, naive rule 0.467, lift 3.32x
    - 7d: 404 calls (58 a day), hit rate 0.948, chance 0.294, naive rule 0.498, lift 3.22x
    - 30d: 1741 calls (58 a day), hit rate 0.936, chance 0.293, naive rule 0.492, lift 3.19x
  - next: threshold 0.5302, hit rate recent 0.5612 / long run 0.5829
    - 6h: 31 calls (126 a day), hit rate 0.516, chance 0.275, lift 1.88x
    - 24h: 124 calls (124 a day), hit rate 0.581, chance 0.282, lift 2.06x
    - 7d: 644 calls (92 a day), hit rate 0.589, chance 0.294, lift 2.00x
    - 30d: 2903 calls (97 a day), hit rate 0.581, chance 0.293, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 537, 0.520; 0.40: 477, 0.577; 0.45: 408, 0.647; 0.50: 357, 0.698; 0.55: 312, 0.739; 0.60: 264, 0.784; 0.65: 221, 0.810; 0.70: 174, 0.843; 0.75: 137, 0.875; 0.80: 92, 0.915; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.428; 0.35: 500, 0.465; 0.40: 407, 0.499; 0.45: 310, 0.534; 0.50: 200, 0.568; 0.55: 89, 0.572; 0.60: 13, 0.634; 0.65: 1, 0.633
- **K=5**: model 1792540800, labels learned 125468, probability skill vs chance 0.2189, widened contest next: False
  - now: threshold 0.6752, hit rate recent 0.8364 / long run 0.8254
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.161, naive rule 0.352, lift 4.95x
    - 24h: 68 calls (68 a day), hit rate 0.838, chance 0.168, naive rule 0.366, lift 4.98x
    - 7d: 394 calls (56 a day), hit rate 0.827, chance 0.185, naive rule 0.406, lift 4.48x
    - 30d: 1614 calls (54 a day), hit rate 0.827, chance 0.188, naive rule 0.402, lift 4.40x
  - next: threshold 0.457, hit rate recent 0.4852 / long run 0.4865
    - 6h: 10 calls (41 a day), hit rate 0.400, chance 0.161, lift 2.48x
    - 24h: 60 calls (60 a day), hit rate 0.433, chance 0.168, lift 2.58x
    - 7d: 740 calls (106 a day), hit rate 0.503, chance 0.185, lift 2.72x
    - 30d: 3066 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 346, 0.492; 0.40: 279, 0.565; 0.45: 227, 0.618; 0.50: 179, 0.669; 0.55: 139, 0.709; 0.60: 107, 0.753; 0.65: 76, 0.791; 0.70: 51, 0.830; 0.75: 30, 0.870; 0.80: 10, 0.897
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.390; 0.35: 254, 0.421; 0.40: 159, 0.456; 0.45: 70, 0.471; 0.50: 14, 0.492; 0.55: 1, 0.513
- **K=8**: model 1793059200, labels learned 125465, probability skill vs chance 0.2004, widened contest next: False
  - now: threshold 0.5616, hit rate recent 0.7018 / long run 0.6837
    - 6h: 11 calls (45 a day), hit rate 0.455, chance 0.106, naive rule 0.261, lift 4.30x
    - 24h: 60 calls (60 a day), hit rate 0.700, chance 0.123, naive rule 0.335, lift 5.70x
    - 7d: 373 calls (53 a day), hit rate 0.678, chance 0.120, naive rule 0.336, lift 5.66x
    - 30d: 1554 calls (52 a day), hit rate 0.689, chance 0.121, naive rule 0.333, lift 5.68x
  - next: threshold 0.3325, hit rate recent 0.3686 / long run 0.3817
    - 6h: 30 calls (123 a day), hit rate 0.267, chance 0.106, lift 2.52x
    - 24h: 105 calls (106 a day), hit rate 0.390, chance 0.123, lift 3.18x
    - 7d: 739 calls (106 a day), hit rate 0.388, chance 0.120, lift 3.24x
    - 30d: 2755 calls (92 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.430; 0.35: 188, 0.498; 0.40: 146, 0.547; 0.45: 111, 0.593; 0.50: 84, 0.635; 0.55: 60, 0.674; 0.60: 40, 0.711; 0.65: 23, 0.775; 0.70: 11, 0.812; 0.75: 2, 0.800
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.355; 0.35: 93, 0.384; 0.40: 31, 0.407; 0.45: 6, 0.423; 0.50: 1, 0.655
- **K=13**: model 1793059200, labels learned 125460, probability skill vs chance 0.1824, widened contest next: False
  - now: threshold 0.4069, hit rate recent 0.541 / long run 0.5564
    - 6h: 14 calls (58 a day), hit rate 0.214, chance 0.065, naive rule 0.232, lift 3.29x
    - 24h: 59 calls (60 a day), hit rate 0.508, chance 0.078, naive rule 0.285, lift 6.56x
    - 7d: 400 calls (57 a day), hit rate 0.557, chance 0.076, naive rule 0.280, lift 7.35x
    - 30d: 1626 calls (54 a day), hit rate 0.563, chance 0.077, naive rule 0.276, lift 7.31x
  - next: threshold 0.2945, hit rate recent 0.3119 / long run 0.3166
    - 6h: 12 calls (50 a day), hit rate 0.167, chance 0.065, lift 2.56x
    - 24h: 49 calls (50 a day), hit rate 0.265, chance 0.078, lift 3.42x
    - 7d: 403 calls (58 a day), hit rate 0.320, chance 0.076, lift 4.22x
    - 30d: 2082 calls (69 a day), hit rate 0.312, chance 0.077, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 125, 0.441; 0.35: 89, 0.493; 0.40: 63, 0.548; 0.45: 42, 0.598; 0.50: 27, 0.655; 0.55: 16, 0.699; 0.60: 8, 0.744; 0.65: 2, 0.770
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.326; 0.35: 14, 0.353; 0.40: 2, 0.446; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.130 | 2.75% | 0.933 | 0.500 | 0.250 | 0.559 | 0.359 |
| 6h | 17.543 | 3.40% | 0.892 | 0.494 | 0.251 | 0.513 | 0.616 |
| 24h | 16.215 | 4.08% | 0.904 | 0.506 | 0.251 | 0.513 | 0.586 |
| 7d | 14.699 | 3.61% | 0.901 | 0.501 | 0.251 | 0.499 | 0.651 |
| 30d | 13.765 | 4.10% | 0.900 | 0.500 | 0.251 | 0.496 | 0.665 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.473 | 12.302 | 12.177 | 12.119 | 12.389 | 12.186 | 12.078 | 12.192 | 12.128 | 12.130 |
| 6h | 18.161 | 17.688 | 17.618 | 17.487 | 17.825 | 17.707 | 17.550 | 17.605 | 17.519 | 17.543 |
| 24h | 16.905 | 16.456 | 16.353 | 16.202 | 16.723 | 16.424 | 16.202 | 16.210 | 16.192 | 16.215 |
| 7d | 15.249 | 14.854 | 14.792 | 14.716 | 14.995 | 14.852 | 14.681 | 14.666 | 14.668 | 14.699 |
| 30d | 14.352 | 13.901 | 13.850 | 13.789 | 14.019 | 13.945 | 13.760 | 13.739 | 13.739 | 13.765 |

## Next candle

- candle starting 2026-10-29 07:16 UTC, last close 2307.15
- P(up) 0.468, return quantiles (bp): {'05': -7.309, '10': -5.562, '25': -2.993, '40': -1.099, '50': -0.28, '60': 0.616, '75': 2.602, '90': 5.552, '95': 7.497}
- changepoint probability 0.0687, regime age 57.6 min
- agent weights: empirical 0.004, ewma 0.056, garch 0.106, har 0.289, bocpd 0.013, hmm 0.064, online_qr 0.260, lgbm 0.209

## Learning log

- 2026-10-27 00:00 UTC: {"garch": {"alpha": 0.1043, "beta": 0.8782}, "hmm": {"sd_bp": [3.4, 6.54, 17.69], "stay": [0.975, 0.955, 0.859]}, "lgbm": {"challenger_loss": 0.25388, "champion_loss": 0.25402, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47709, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47468, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36742, "challengers": 1, "chance_loss": 0.47624, "widened": false, "champion_loss": 0.36596, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26268, "challengers": 3, "chance_loss": 0.35446, "widened": true, "champion_loss": 0.26288, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18101, "challengers": 3, "chance_loss": 0.25307, "widened": true, "champion_loss": 0.18142, "promoted": true}}
- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.53, 6.59, 15.41], current probabilities: [0.816, 0.174, 0.011]
- live generator: {'versions': 60, 'latest_effective': '2026-10-29 07:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.276, 'l_abs': 0.71, 'l_hi': 0.723, 'l_lo': 0.755, 'b05': 0.699, 'b25': 0.725, 'b75': 0.604, 'b95': 0.692}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.443, 1.634, 1.929, 2.035, 2.022, 2.277, 3.101, 2.865, 3.696, 3.884, 4.317, 3.836, 3.833, 4.665]}
- calibration offsets (in sigma): {'05': 0.0575, '10': 0.035, '25': -0.0225, '40': 0.0, '50': -0.045, '60': -0.08, '75': -0.0375, '90': -0.035, '95': -0.0475}
