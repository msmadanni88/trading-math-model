# ETH-USD 60s candle generator - report

- generated: 2026-10-29 14:28 UTC
- last closed candle: 2026-10-29 14:28 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.552 (96) | 0.537 (672) [0.501, 0.573] | 0.520 (2876) [0.501, 0.539] | 0.517 (5466) [0.503, 0.531] | 0.524 (2494) [0.504, 0.546] | 0.456 (57) | 0.500 | flat -0.006 (noise 0.031) |
| colour_clear | 0.537 (786) | 0.542 (5666) [0.539, 0.547] | 0.538 (23626) [0.531, 0.545] | 0.519 (44743) [0.513, 0.525] | 0.546 (20505) [0.541, 0.550] | 0.531 (490) | 0.500 | flat -0.013 (noise 0.009) |
| colour_confident | 0.567 (120) | 0.601 (1315) [0.586, 0.617] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.602 (3902) [0.589, 0.614] | 0.580 (88) | 0.500 | flat +0.001 (noise 0.021) |
| colour_next | 0.531 (1431) | 0.528 (10027) [0.525, 0.531] | 0.526 (42877) [0.521, 0.530] | 0.514 (81483) [0.510, 0.518] | 0.529 (37134) [0.526, 0.533] | 0.524 (862) | 0.500 | flat -0.006 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.502 (140378) [0.500, 0.504] | 0.501 (600278) [0.499, 0.502] | 0.501 (1140762) [0.500, 0.502] | 0.501 (519876) [0.499, 0.502] | 0.496 (12068) | 0.500 | flat +0.002 (noise 0.003) |
| colour_strong | 0.500 (32) | 0.607 (405) [0.583, 0.639] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.631 (1073) [0.610, 0.652] | 0.733 (15) | 0.500 | flat -0.024 (noise 0.040) |
| reversal_k13_next | 0.302 (53) | 0.317 (410) [0.283, 0.357] | 0.310 (2116) [0.298, 0.323] | 0.309 (3847) [0.299, 0.320] | 0.320 (1742) [0.308, 0.332] | 0.214 (28) | 0.077 | flat -0.007 (noise 0.032) |
| reversal_k13_now | 0.603 (63) | 0.568 (391) [0.519, 0.620] | 0.562 (1632) [0.542, 0.584] | 0.573 (2895) [0.558, 0.589] | 0.565 (1423) [0.543, 0.589] | 0.462 (39) | 0.077 | flat +0.043 (noise 0.036) |
| reversal_k3_next | 0.591 (115) | 0.593 (648) [0.584, 0.603] | 0.583 (2896) [0.572, 0.596] | 0.584 (4997) [0.574, 0.594] | 0.580 (2557) [0.568, 0.594] | 0.553 (85) | 0.293 | flat +0.016 (noise 0.026) |
| reversal_k3_now | 0.909 (66) | 0.942 (399) [0.918, 0.964] | 0.935 (1742) [0.926, 0.945] | 0.938 (3257) [0.931, 0.945] | 0.934 (1494) [0.923, 0.944] | 1.000 (36) | 0.293 | flat +0.010 (noise 0.021) |
| reversal_k5_next | 0.500 (64) | 0.501 (766) [0.491, 0.512] | 0.468 (3071) [0.455, 0.482] | 0.478 (4683) [0.466, 0.491] | 0.466 (2693) [0.452, 0.481] | 0.518 (27) | 0.187 | up +0.067 (noise 0.024) |
| reversal_k5_now | 0.838 (74) | 0.828 (389) [0.816, 0.837] | 0.826 (1616) [0.814, 0.837] | 0.830 (3006) [0.820, 0.840] | 0.822 (1395) [0.810, 0.834] | 0.857 (35) | 0.187 | flat +0.011 (noise 0.028) |
| reversal_k8_next | 0.446 (101) | 0.387 (744) [0.364, 0.410] | 0.384 (2742) [0.371, 0.397] | 0.389 (4618) [0.378, 0.400] | 0.383 (2512) [0.369, 0.396] | 0.350 (60) | 0.120 | flat +0.022 (noise 0.025) |
| reversal_k8_now | 0.770 (61) | 0.683 (369) [0.628, 0.736] | 0.689 (1559) [0.667, 0.709] | 0.701 (2959) [0.686, 0.716] | 0.687 (1372) [0.663, 0.710] | 0.710 (31) | 0.121 | flat +0.016 (noise 0.038) |
| overall | 0.508 (22158) | 0.506 (155193) [0.503, 0.508] | 0.504 (663405) [0.503, 0.506] | 0.503 (1257973) [0.502, 0.504] | 0.504 (574692) [0.503, 0.506] | 0.500 (13328) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08155, 0.1238] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5287, 'levels': [{'threshold': 0.08155, 'calls_per_day': 145.9, 'win_rate': 0.6095}, {'threshold': 0.1238, 'calls_per_day': 36.6, 'win_rate': 0.6163}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 36856, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15170 | 0.341 | 0.522 (14943) | 0.582 (1994) | 0.751 (2581) |
| volatility: normal | 15169 | 0.366 | 0.530 (15103) | 0.613 (1325) | 0.751 (2252) |
| volatility: wild | 15169 | 0.380 | 0.523 (15127) | 0.635 (671) | 0.770 (2011) |
| session: Asia 00-08 | 15360 | 0.361 | 0.531 (15257) | 0.605 (1425) | 0.759 (2293) |
| session: Europe 08-13 | 9600 | 0.358 | 0.529 (9514) | 0.590 (996) | 0.749 (1541) |
| session: US 13-21 | 14968 | 0.370 | 0.520 (14876) | 0.601 (1012) | 0.766 (2163) |
| session: late 21-24 | 5580 | 0.351 | 0.516 (5526) | 0.610 (557) | 0.744 (847) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.384 | 0.408 | 0.296 | 0.296 | 0.500 | 0.226 | 0.541 | 1.173 |
| 6h | 360 | 0.373 | 0.369 | 0.285 | 0.314 | 0.520 | 0.269 | 0.478 | 1.151 |
| 24h | 1440 | 0.372 | 0.369 | 0.285 | 0.315 | 0.537 | 0.262 | 0.482 | 1.268 |
| 7d | 10080 | 0.367 | 0.359 | 0.280 | 0.310 | 0.527 | 0.265 | 0.469 | 1.244 |
| 30d | 43200 | 0.361 | 0.354 | 0.277 | 0.306 | 0.526 | 0.259 | 0.464 | 1.277 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.384 / 0.500 / 0.867; 2: 0.405 / 0.550 / 0.850; 3: 0.382 / 0.500 / 0.867; 4: 0.393 / 0.583 / 0.900; 5: 0.366 / 0.500 / 0.883; 6: 0.347 / 0.400 / 0.883; 7: 0.393 / 0.567 / 0.900; 8: 0.387 / 0.483 / 0.967; 9: 0.369 / 0.500 / 0.967; 10: 0.403 / 0.600 / 0.950; 11: 0.386 / 0.500 / 0.950; 12: 0.373 / 0.467 / 0.950; 13: 0.385 / 0.500 / 0.933; 14: 0.368 / 0.483 / 0.933; 15: 0.380 / 0.467 / 0.933
- 6h: 1: 0.373 / 0.520 / 0.886; 2: 0.357 / 0.497 / 0.897; 3: 0.364 / 0.514 / 0.878; 4: 0.351 / 0.500 / 0.875; 5: 0.356 / 0.508 / 0.869; 6: 0.344 / 0.489 / 0.853; 7: 0.365 / 0.534 / 0.872; 8: 0.355 / 0.514 / 0.944; 9: 0.338 / 0.447 / 0.919; 10: 0.359 / 0.525 / 0.950; 11: 0.357 / 0.497 / 0.950; 12: 0.347 / 0.475 / 0.967; 13: 0.356 / 0.508 / 0.947; 14: 0.345 / 0.483 / 0.944; 15: 0.347 / 0.483 / 0.958
- 24h: 1: 0.372 / 0.537 / 0.908; 2: 0.361 / 0.502 / 0.899; 3: 0.358 / 0.496 / 0.897; 4: 0.361 / 0.500 / 0.897; 5: 0.356 / 0.501 / 0.901; 6: 0.350 / 0.491 / 0.901; 7: 0.363 / 0.507 / 0.910; 8: 0.359 / 0.521 / 0.924; 9: 0.354 / 0.498 / 0.923; 10: 0.360 / 0.505 / 0.926; 11: 0.352 / 0.487 / 0.924; 12: 0.353 / 0.487 / 0.928; 13: 0.347 / 0.481 / 0.922; 14: 0.359 / 0.507 / 0.921; 15: 0.352 / 0.500 / 0.922
- 7d: 1: 0.367 / 0.527 / 0.899; 2: 0.355 / 0.497 / 0.900; 3: 0.358 / 0.511 / 0.900; 4: 0.353 / 0.499 / 0.899; 5: 0.353 / 0.506 / 0.899; 6: 0.351 / 0.504 / 0.898; 7: 0.352 / 0.499 / 0.899; 8: 0.354 / 0.509 / 0.900; 9: 0.352 / 0.500 / 0.900; 10: 0.353 / 0.505 / 0.900; 11: 0.350 / 0.502 / 0.900; 12: 0.353 / 0.505 / 0.901; 13: 0.349 / 0.499 / 0.900; 14: 0.350 / 0.501 / 0.900; 15: 0.350 / 0.499 / 0.900
- 30d: 1: 0.361 / 0.526 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.348 / 0.498 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.501 / 0.900; 9: 0.346 / 0.497 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.346 / 0.499 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.117 (body 0.057, range 0.178); 'price stays where it was' would score 0.174; colour right 0.517; typical miss of the close 20.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.081, range 0.176); 'price stays where it was' would score 0.133; colour right 0.469; typical miss of the close 7.7 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.128 (body 0.085, range 0.171); 'price stays where it was' would score 0.134; colour right 0.502; typical miss of the close 9.6 bp; chain ended on the right side 0.417 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.169); 'price stays where it was' would score 0.136; colour right 0.496; typical miss of the close 8.5 bp; chain ended on the right side 0.537 of 672 chains; n=10080
- 30d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.129; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2877 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.0; 2: 0.199 / 4.6; 3: 0.168 / 6.1; 4: 0.133 / 6.5; 5: 0.126 / 7.2; 6: 0.113 / 7.7; 7: 0.108 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.6; 10: 0.088 / 9.2; 11: 0.085 / 9.6; 12: 0.077 / 9.9; 13: 0.068 / 10.1; 14: 0.072 / 10.5; 15: 0.062 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 125902, probability skill vs chance 0.236, widened contest next: False
  - now: threshold 0.8348, hit rate recent 0.9621 / long run 0.9418
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.304, naive rule 0.516, lift 3.29x
    - 24h: 63 calls (63 a day), hit rate 0.952, chance 0.285, naive rule 0.480, lift 3.34x
    - 7d: 399 calls (57 a day), hit rate 0.952, chance 0.294, naive rule 0.498, lift 3.24x
    - 30d: 1737 calls (58 a day), hit rate 0.936, chance 0.294, naive rule 0.492, lift 3.19x
  - next: threshold 0.5304, hit rate recent 0.5797 / long run 0.5829
    - 6h: 36 calls (146 a day), hit rate 0.583, chance 0.304, lift 1.92x
    - 24h: 127 calls (127 a day), hit rate 0.583, chance 0.285, lift 2.04x
    - 7d: 664 calls (95 a day), hit rate 0.587, chance 0.294, lift 2.00x
    - 30d: 2920 calls (97 a day), hit rate 0.580, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 537, 0.520; 0.40: 476, 0.577; 0.45: 407, 0.649; 0.50: 357, 0.699; 0.55: 312, 0.740; 0.60: 264, 0.786; 0.65: 221, 0.811; 0.70: 174, 0.844; 0.75: 137, 0.876; 0.80: 92, 0.915; 0.85: 47, 0.949; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.429; 0.35: 500, 0.466; 0.40: 407, 0.499; 0.45: 310, 0.534; 0.50: 200, 0.569; 0.55: 89, 0.571; 0.60: 13, 0.635; 0.65: 1, 0.621
- **K=5**: model 1792540800, labels learned 125900, probability skill vs chance 0.2308, widened contest next: False
  - now: threshold 0.6759, hit rate recent 0.851 / long run 0.8275
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.217, naive rule 0.503, lift 4.04x
    - 24h: 65 calls (65 a day), hit rate 0.846, chance 0.184, naive rule 0.406, lift 4.61x
    - 7d: 395 calls (56 a day), hit rate 0.835, chance 0.186, naive rule 0.408, lift 4.50x
    - 30d: 1614 calls (54 a day), hit rate 0.827, chance 0.188, naive rule 0.403, lift 4.40x
  - next: threshold 0.4571, hit rate recent 0.5048 / long run 0.4884
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.217, lift 2.88x
    - 24h: 48 calls (48 a day), hit rate 0.521, chance 0.184, lift 2.84x
    - 7d: 715 calls (102 a day), hit rate 0.503, chance 0.186, lift 2.71x
    - 30d: 3064 calls (102 a day), hit rate 0.468, chance 0.188, lift 2.49x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.427; 0.35: 346, 0.493; 0.40: 279, 0.566; 0.45: 227, 0.619; 0.50: 179, 0.669; 0.55: 140, 0.709; 0.60: 107, 0.754; 0.65: 76, 0.792; 0.70: 51, 0.832; 0.75: 30, 0.872; 0.80: 10, 0.900
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 344, 0.391; 0.35: 254, 0.421; 0.40: 159, 0.456; 0.45: 70, 0.471; 0.50: 14, 0.489; 0.55: 1, 0.500
- **K=8**: model 1793059200, labels learned 125897, probability skill vs chance 0.2071, widened contest next: False
  - now: threshold 0.5622, hit rate recent 0.7439 / long run 0.6887
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.139, naive rule 0.398, lift 6.56x
    - 24h: 58 calls (58 a day), hit rate 0.776, chance 0.128, naive rule 0.355, lift 6.05x
    - 7d: 373 calls (53 a day), hit rate 0.686, chance 0.121, naive rule 0.337, lift 5.69x
    - 30d: 1554 calls (52 a day), hit rate 0.690, chance 0.121, naive rule 0.333, lift 5.69x
  - next: threshold 0.3321, hit rate recent 0.4064 / long run 0.3855
    - 6h: 22 calls (91 a day), hit rate 0.455, chance 0.139, lift 3.28x
    - 24h: 97 calls (98 a day), hit rate 0.402, chance 0.128, lift 3.13x
    - 7d: 737 calls (105 a day), hit rate 0.389, chance 0.121, lift 3.23x
    - 30d: 2763 calls (92 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.430; 0.35: 189, 0.498; 0.40: 146, 0.547; 0.45: 111, 0.594; 0.50: 84, 0.636; 0.55: 60, 0.676; 0.60: 40, 0.711; 0.65: 23, 0.777; 0.70: 10, 0.813; 0.75: 2, 0.800
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.355; 0.35: 93, 0.383; 0.40: 31, 0.406; 0.45: 6, 0.420; 0.50: 1, 0.655
- **K=13**: model 1793059200, labels learned 125892, probability skill vs chance 0.1894, widened contest next: False
  - now: threshold 0.4072, hit rate recent 0.5521 / long run 0.557
    - 6h: 15 calls (63 a day), hit rate 0.600, chance 0.075, naive rule 0.341, lift 7.96x
    - 24h: 63 calls (64 a day), hit rate 0.540, chance 0.078, naive rule 0.299, lift 6.93x
    - 7d: 404 calls (58 a day), hit rate 0.557, chance 0.076, naive rule 0.281, lift 7.32x
    - 30d: 1628 calls (54 a day), hit rate 0.564, chance 0.077, naive rule 0.276, lift 7.32x
  - next: threshold 0.2947, hit rate recent 0.2999 / long run 0.3148
    - 6h: 12 calls (50 a day), hit rate 0.250, chance 0.075, lift 3.32x
    - 24h: 48 calls (49 a day), hit rate 0.250, chance 0.078, lift 3.21x
    - 7d: 408 calls (58 a day), hit rate 0.316, chance 0.076, lift 4.15x
    - 30d: 2073 calls (69 a day), hit rate 0.312, chance 0.077, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 125, 0.441; 0.35: 89, 0.493; 0.40: 63, 0.548; 0.45: 42, 0.599; 0.50: 27, 0.657; 0.55: 16, 0.699; 0.60: 8, 0.749; 0.65: 2, 0.774
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.324; 0.35: 14, 0.352; 0.40: 2, 0.447; 0.45: 0, 0.571

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 26.573 | 4.93% | 0.867 | 0.450 | 0.250 | 0.500 | 0.143 |
| 6h | 15.277 | 3.69% | 0.886 | 0.489 | 0.250 | 0.511 | 0.596 |
| 24h | 16.433 | 3.76% | 0.893 | 0.498 | 0.251 | 0.509 | 0.603 |
| 7d | 14.645 | 3.61% | 0.900 | 0.500 | 0.251 | 0.500 | 0.652 |
| 30d | 13.757 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.665 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 27.950 | 26.826 | 26.795 | 26.596 | 27.161 | 26.891 | 26.455 | 26.565 | 26.520 | 26.573 |
| 6h | 15.861 | 15.475 | 15.344 | 15.302 | 15.658 | 15.400 | 15.245 | 15.235 | 15.251 | 15.277 |
| 24h | 17.074 | 16.641 | 16.539 | 16.422 | 16.882 | 16.608 | 16.401 | 16.419 | 16.401 | 16.433 |
| 7d | 15.194 | 14.796 | 14.735 | 14.668 | 14.938 | 14.800 | 14.629 | 14.608 | 14.615 | 14.645 |
| 30d | 14.346 | 13.893 | 13.841 | 13.782 | 14.011 | 13.937 | 13.752 | 13.731 | 13.731 | 13.757 |

## Next candle

- candle starting 2026-10-29 14:28 UTC, last close 2321.66
- P(up) 0.5125, return quantiles (bp): {'05': -15.07, '10': -10.911, '25': -5.328, '40': -1.533, '50': 0.215, '60': 2.473, '75': 6.34, '90': 11.709, '95': 14.807}
- changepoint probability 0.0251, regime age 98.3 min
- agent weights: empirical 0.005, ewma 0.046, garch 0.103, har 0.210, bocpd 0.010, hmm 0.063, online_qr 0.281, lgbm 0.282

## Learning log

- 2026-10-27 12:00 UTC: {"garch": {"alpha": 0.1124, "beta": 0.8678}, "hmm": {"sd_bp": [3.43, 6.6, 17.85], "stay": [0.973, 0.954, 0.865]}}
- 2026-10-28 00:00 UTC: {"garch": {"alpha": 0.1115, "beta": 0.8666}, "hmm": {"sd_bp": [3.41, 6.59, 17.7], "stay": [0.974, 0.952, 0.857]}, "lgbm": {"challenger_loss": 0.25326, "champion_loss": 0.25326, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46702, "challengers": 1, "chance_loss": 0.60184, "widened": false, "champion_loss": 0.46372, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37097, "challengers": 1, "chance_loss": 0.48944, "widened": false, "champion_loss": 0.3688, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27476, "challengers": 1, "chance_loss": 0.37151, "widened": false, "champion_loss": 0.2742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19368, "challengers": 1, "chance_loss": 0.27677, "widened": false, "champion_loss": 0.19219, "promoted": false}}
- 2026-10-28 12:00 UTC: {"garch": {"alpha": 0.12, "beta": 0.8461}, "hmm": {"sd_bp": [3.47, 6.69, 18.19], "stay": [0.973, 0.949, 0.844]}}
- 2026-10-29 00:00 UTC: {"garch": {"alpha": 0.1191, "beta": 0.8375}, "hmm": {"sd_bp": [3.53, 6.59, 15.41], "stay": [0.97, 0.942, 0.83]}, "lgbm": {"challenger_loss": 0.25176, "champion_loss": 0.2517, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47626, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47258, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36923, "challengers": 1, "chance_loss": 0.4841, "widened": false, "champion_loss": 0.36643, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28012, "challengers": 1, "chance_loss": 0.38136, "widened": false, "champion_loss": 0.27953, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20228, "challengers": 1, "chance_loss": 0.28671, "widened": false, "champion_loss": 0.20115, "promoted": false}}
- 2026-10-29 12:00 UTC: {"garch": {"alpha": 0.1174, "beta": 0.8337}, "hmm": {"sd_bp": [3.72, 6.69, 15.08], "stay": [0.968, 0.938, 0.852]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.69, 15.08], current probabilities: [0.0, 0.389, 0.611]
- live generator: {'versions': 60, 'latest_effective': '2026-10-29 14:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.247, 'l_abs': 0.716, 'l_hi': 0.73, 'l_lo': 0.757, 'b05': 0.707, 'b25': 0.726, 'b75': 0.606, 'b95': 0.697}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8]], 'cone_width': [1.466, 2.111, 2.443, 2.526, 2.829, 2.77, 2.07, 2.432, 2.371, 2.492, 2.407, 2.561, 2.717, 2.818]}
- calibration offsets (in sigma): {'05': 0.0335, '10': 0.037, '25': 0.0175, '40': 0.038, '50': 0.015, '60': 0.032, '75': 0.0725, '90': 0.043, '95': 0.0065}
