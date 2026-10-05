# ETH-USD 60s candle generator - report

- generated: 2026-10-05 02:21 UTC
- last closed candle: 2026-10-05 02:21 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.635 (96) | 0.527 (670) [0.492, 0.566] | 0.512 (2876) [0.492, 0.531] | 0.516 (3164) [0.498, 0.533] | 0.583 (192) | 0.556 (9) | 0.500 | flat -0.015 (noise 0.031) |
| colour_clear | 0.558 (674) | 0.507 (5294) [0.489, 0.527] | 0.500 (23246) [0.495, 0.506] | 0.499 (25633) [0.494, 0.505] | 0.552 (1395) | 0.607 (84) | 0.500 | flat +0.010 (noise 0.012) |
| colour_confident | 0.623 (260) | 0.619 (344) | 0.619 (344) | 0.619 (344) | 0.619 (344) | 0.750 (8) | 0.500 | - |
| colour_next | 0.548 (1417) | 0.512 (9998) [0.503, 0.524] | 0.503 (42868) [0.499, 0.508] | 0.503 (47170) [0.498, 0.507] | 0.535 (2821) | 0.575 (141) | 0.500 | up +0.017 (noise 0.008) |
| colour_path | 0.506 (19838) | 0.502 (139972) [0.499, 0.505] | 0.501 (600152) [0.500, 0.502] | 0.501 (660380) [0.499, 0.502] | 0.499 (39494) | 0.517 (1974) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.648 (88) | 0.652 (115) | 0.652 (115) | 0.652 (115) | 0.652 (115) | - | 0.500 | - |
| reversal_k13_next | 0.360 (86) | 0.290 (659) [0.266, 0.315] | 0.308 (2007) [0.293, 0.324] | 0.303 (2293) [0.288, 0.319] | 0.340 (188) | 0.333 (9) | 0.077 | flat -0.024 (noise 0.030) |
| reversal_k13_now | 0.600 (65) | 0.585 (361) [0.534, 0.636] | 0.589 (1448) [0.566, 0.612] | 0.587 (1582) [0.567, 0.608] | 0.664 (110) | 0.800 (5) | 0.077 | flat -0.028 (noise 0.038) |
| reversal_k3_next | 0.597 (124) | 0.590 (704) [0.563, 0.617] | 0.584 (2492) [0.569, 0.598] | 0.585 (2708) [0.571, 0.599] | 0.563 (268) | 0.714 (7) | 0.292 | flat +0.044 (noise 0.030) |
| reversal_k3_now | 0.922 (64) | 0.941 (407) [0.931, 0.953] | 0.942 (1718) [0.933, 0.951] | 0.941 (1884) [0.932, 0.949] | 0.926 (121) | 1.000 (3) | 0.292 | flat +0.001 (noise 0.017) |
| reversal_k5_next | 0.483 (120) | 0.458 (734) [0.427, 0.488] | 0.486 (2147) [0.465, 0.505] | 0.486 (2299) [0.469, 0.504] | 0.437 (309) | 0.000 (2) | 0.187 | flat -0.060 (noise 0.035) |
| reversal_k5_now | 0.897 (68) | 0.854 (389) [0.838, 0.870] | 0.839 (1601) [0.824, 0.855] | 0.839 (1740) [0.824, 0.853] | 0.861 (129) | 0.500 (2) | 0.186 | flat +0.028 (noise 0.027) |
| reversal_k8_next | 0.471 (87) | 0.401 (437) [0.365, 0.435] | 0.403 (2028) [0.385, 0.423] | 0.398 (2270) [0.382, 0.416] | 0.427 (164) | 0.400 (5) | 0.122 | flat -0.014 (noise 0.034) |
| reversal_k8_now | 0.783 (60) | 0.729 (332) [0.698, 0.756] | 0.724 (1555) [0.704, 0.743] | 0.718 (1697) [0.700, 0.738] | 0.782 (110) | 0.500 (4) | 0.122 | flat -0.024 (noise 0.033) |
| overall | 0.512 (22025) | 0.505 (154663) [0.501, 0.508] | 0.503 (660892) [0.502, 0.504] | 0.503 (727187) [0.501, 0.504] | 0.504 (43906) | 0.521 (2161) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07571, 0.1135] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5321, 'levels': [{'threshold': 0.07571, 'calls_per_day': 145.4, 'win_rate': 0.5692}, {'threshold': 0.1135, 'calls_per_day': 36.7, 'win_rate': 0.6371}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 1830, 'rate': 0.5536}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14927 | 0.330 | 0.510 (14695) | 0.617 (342) | 0.787 (2356) |
| volatility: normal | 14927 | 0.359 | 0.508 (14864) | - | 0.779 (2118) |
| volatility: wild | 14927 | 0.373 | 0.492 (14883) | - | 0.773 (2073) |
| session: Asia 00-08 | 15021 | 0.351 | 0.502 (14912) | 0.642 (123) | 0.786 (2155) |
| session: Europe 08-13 | 9300 | 0.347 | 0.503 (9233) | 0.562 (64) | 0.769 (1422) |
| session: US 13-21 | 14880 | 0.363 | 0.504 (14778) | 0.625 (112) | 0.786 (2211) |
| session: late 21-24 | 5580 | 0.351 | 0.504 (5519) | 0.641 (53) | 0.765 (759) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.377 | 0.385 | 0.285 | 0.285 | 0.533 | 0.260 | 0.495 | 1.038 |
| 6h | 360 | 0.372 | 0.363 | 0.282 | 0.311 | 0.539 | 0.275 | 0.469 | 0.918 |
| 24h | 1440 | 0.326 | 0.316 | 0.246 | 0.260 | 0.552 | 0.244 | 0.407 | 1.194 |
| 7d | 10080 | 0.354 | 0.352 | 0.281 | 0.305 | 0.513 | 0.243 | 0.465 | 1.398 |
| 30d | 43200 | 0.354 | 0.353 | 0.277 | 0.307 | 0.504 | 0.245 | 0.463 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.377 / 0.533 / 0.933; 2: 0.359 / 0.450 / 0.967; 3: 0.372 / 0.517 / 0.950; 4: 0.334 / 0.400 / 0.950; 5: 0.355 / 0.550 / 0.950; 6: 0.373 / 0.583 / 0.950; 7: 0.378 / 0.533 / 0.983; 8: 0.346 / 0.500 / 0.983; 9: 0.360 / 0.500 / 1.000; 10: 0.390 / 0.617 / 1.000; 11: 0.344 / 0.433 / 1.000; 12: 0.340 / 0.467 / 1.000; 13: 0.343 / 0.467 / 0.967; 14: 0.330 / 0.467 / 0.967; 15: 0.372 / 0.600 / 0.967
- 6h: 1: 0.372 / 0.539 / 0.886; 2: 0.363 / 0.547 / 0.919; 3: 0.364 / 0.503 / 0.878; 4: 0.353 / 0.492 / 0.886; 5: 0.367 / 0.525 / 0.875; 6: 0.365 / 0.525 / 0.881; 7: 0.362 / 0.553 / 0.878; 8: 0.360 / 0.525 / 0.878; 9: 0.351 / 0.494 / 0.889; 10: 0.357 / 0.547 / 0.875; 11: 0.350 / 0.500 / 0.889; 12: 0.356 / 0.528 / 0.903; 13: 0.354 / 0.528 / 0.894; 14: 0.348 / 0.522 / 0.881; 15: 0.358 / 0.539 / 0.889
- 24h: 1: 0.326 / 0.552 / 0.883; 2: 0.310 / 0.517 / 0.903; 3: 0.313 / 0.527 / 0.894; 4: 0.303 / 0.494 / 0.899; 5: 0.308 / 0.495 / 0.898; 6: 0.307 / 0.505 / 0.899; 7: 0.307 / 0.511 / 0.897; 8: 0.311 / 0.514 / 0.900; 9: 0.304 / 0.495 / 0.897; 10: 0.308 / 0.522 / 0.894; 11: 0.304 / 0.495 / 0.896; 12: 0.310 / 0.539 / 0.898; 13: 0.301 / 0.499 / 0.901; 14: 0.303 / 0.502 / 0.901; 15: 0.307 / 0.520 / 0.903
- 7d: 1: 0.354 / 0.513 / 0.897; 2: 0.348 / 0.497 / 0.901; 3: 0.350 / 0.511 / 0.900; 4: 0.347 / 0.498 / 0.901; 5: 0.346 / 0.505 / 0.901; 6: 0.345 / 0.496 / 0.901; 7: 0.345 / 0.504 / 0.901; 8: 0.345 / 0.503 / 0.901; 9: 0.342 / 0.492 / 0.902; 10: 0.344 / 0.509 / 0.902; 11: 0.345 / 0.506 / 0.902; 12: 0.346 / 0.515 / 0.902; 13: 0.344 / 0.502 / 0.902; 14: 0.342 / 0.495 / 0.902; 15: 0.342 / 0.498 / 0.902
- 30d: 1: 0.354 / 0.504 / 0.898; 2: 0.350 / 0.498 / 0.900; 3: 0.352 / 0.506 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.348 / 0.504 / 0.900; 7: 0.348 / 0.506 / 0.900; 8: 0.347 / 0.504 / 0.900; 9: 0.345 / 0.499 / 0.900; 10: 0.346 / 0.504 / 0.900; 11: 0.346 / 0.503 / 0.900; 12: 0.345 / 0.502 / 0.900; 13: 0.344 / 0.500 / 0.899; 14: 0.344 / 0.495 / 0.900; 15: 0.343 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.057 (body 0.036, range 0.079); 'price stays where it was' would score 0.095; colour right 0.533; typical miss of the close 11.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.110 (body 0.074, range 0.145); 'price stays where it was' would score 0.123; colour right 0.547; typical miss of the close 8.7 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.108 (body 0.074, range 0.142); 'price stays where it was' would score 0.109; colour right 0.509; typical miss of the close 3.8 bp; chain ended on the right side 0.635 of 96 chains; n=1440
- 7d: match 0.119 (body 0.078, range 0.160); 'price stays where it was' would score 0.120; colour right 0.493; typical miss of the close 7.0 bp; chain ended on the right side 0.528 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.511 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.2; 2: 0.197 / 4.3; 3: 0.169 / 6.1; 4: 0.133 / 6.4; 5: 0.123 / 7.1; 6: 0.112 / 8.1; 7: 0.099 / 8.4; 8: 0.092 / 8.8; 9: 0.088 / 9.0; 10: 0.083 / 9.9; 11: 0.076 / 10.4; 12: 0.075 / 10.8; 13: 0.067 / 11.1; 14: 0.067 / 11.2; 15: 0.062 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 90615, probability skill vs chance 0.2272, widened contest next: False
  - now: threshold 0.8408, hit rate recent 0.9201 / long run 0.9388
    - 6h: 15 calls (61 a day), hit rate 0.867, chance 0.317, naive rule 0.537, lift 2.73x
    - 24h: 60 calls (60 a day), hit rate 0.917, chance 0.285, naive rule 0.473, lift 3.22x
    - 7d: 406 calls (58 a day), hit rate 0.941, chance 0.289, naive rule 0.486, lift 3.25x
    - 30d: 1716 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5572, hit rate recent 0.6147 / long run 0.5807
    - 6h: 21 calls (85 a day), hit rate 0.714, chance 0.317, lift 2.25x
    - 24h: 119 calls (119 a day), hit rate 0.597, chance 0.285, lift 2.10x
    - 7d: 697 calls (100 a day), hit rate 0.590, chance 0.289, lift 2.04x
    - 30d: 2495 calls (83 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.518; 0.40: 488, 0.560; 0.45: 421, 0.626; 0.50: 368, 0.680; 0.55: 321, 0.725; 0.60: 274, 0.766; 0.65: 224, 0.803; 0.70: 182, 0.835; 0.75: 139, 0.870; 0.80: 99, 0.909; 0.85: 49, 0.950; 0.90: 1, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 497, 0.459; 0.40: 414, 0.487; 0.45: 318, 0.518; 0.50: 210, 0.550; 0.55: 95, 0.586; 0.60: 13, 0.614; 0.65: 0, 0.733
- **K=5**: model 1790208000, labels learned 90613, probability skill vs chance 0.2169, widened contest next: False
  - now: threshold 0.7125, hit rate recent 0.8493 / long run 0.8436
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.197, naive rule 0.408, lift 3.52x
    - 24h: 63 calls (63 a day), hit rate 0.873, chance 0.180, naive rule 0.364, lift 4.86x
    - 7d: 388 calls (55 a day), hit rate 0.851, chance 0.187, naive rule 0.394, lift 4.55x
    - 30d: 1598 calls (53 a day), hit rate 0.838, chance 0.186, naive rule 0.390, lift 4.50x
  - next: threshold 0.4509, hit rate recent 0.4773 / long run 0.4712
    - 6h: 18 calls (73 a day), hit rate 0.556, chance 0.197, lift 2.82x
    - 24h: 105 calls (106 a day), hit rate 0.476, chance 0.180, lift 2.65x
    - 7d: 724 calls (104 a day), hit rate 0.457, chance 0.187, lift 2.45x
    - 30d: 2142 calls (71 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 433, 0.410; 0.35: 372, 0.462; 0.40: 301, 0.530; 0.45: 246, 0.588; 0.50: 192, 0.648; 0.55: 146, 0.697; 0.60: 115, 0.739; 0.65: 87, 0.783; 0.70: 65, 0.820; 0.75: 35, 0.860; 0.80: 10, 0.884
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.385; 0.35: 255, 0.422; 0.40: 169, 0.447; 0.45: 89, 0.471; 0.50: 22, 0.518; 0.55: 3, 0.580
- **K=8**: model 1791158400, labels learned 90610, probability skill vs chance 0.2099, widened contest next: False
  - now: threshold 0.5597, hit rate recent 0.7449 / long run 0.7317
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.133, naive rule 0.369, lift 4.70x
    - 24h: 58 calls (58 a day), hit rate 0.776, chance 0.128, naive rule 0.319, lift 6.08x
    - 7d: 332 calls (47 a day), hit rate 0.726, chance 0.124, naive rule 0.332, lift 5.85x
    - 30d: 1557 calls (52 a day), hit rate 0.723, chance 0.121, naive rule 0.326, lift 5.95x
  - next: threshold 0.3535, hit rate recent 0.4656 / long run 0.4122
    - 6h: 17 calls (70 a day), hit rate 0.588, chance 0.133, lift 4.43x
    - 24h: 84 calls (85 a day), hit rate 0.464, chance 0.128, lift 3.64x
    - 7d: 435 calls (62 a day), hit rate 0.400, chance 0.124, lift 3.22x
    - 30d: 2026 calls (68 a day), hit rate 0.403, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 276, 0.397; 0.35: 208, 0.473; 0.40: 161, 0.537; 0.45: 127, 0.585; 0.50: 97, 0.626; 0.55: 69, 0.681; 0.60: 46, 0.729; 0.65: 25, 0.765; 0.70: 9, 0.805; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 189, 0.343; 0.35: 119, 0.382; 0.40: 49, 0.410; 0.45: 10, 0.420; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 90605, probability skill vs chance 0.1992, widened contest next: False
  - now: threshold 0.4103, hit rate recent 0.6407 / long run 0.5979
    - 6h: 15 calls (63 a day), hit rate 0.533, chance 0.099, naive rule 0.369, lift 5.41x
    - 24h: 63 calls (64 a day), hit rate 0.619, chance 0.088, naive rule 0.277, lift 7.00x
    - 7d: 362 calls (52 a day), hit rate 0.588, chance 0.078, naive rule 0.267, lift 7.51x
    - 30d: 1450 calls (48 a day), hit rate 0.589, chance 0.077, naive rule 0.267, lift 7.66x
  - next: threshold 0.266, hit rate recent 0.3654 / long run 0.3062
    - 6h: 23 calls (96 a day), hit rate 0.391, chance 0.099, lift 3.97x
    - 24h: 87 calls (88 a day), hit rate 0.379, chance 0.088, lift 4.29x
    - 7d: 655 calls (94 a day), hit rate 0.287, chance 0.078, lift 3.66x
    - 30d: 2012 calls (67 a day), hit rate 0.309, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.437; 0.35: 90, 0.493; 0.40: 65, 0.541; 0.45: 45, 0.602; 0.50: 29, 0.619; 0.55: 16, 0.667; 0.60: 7, 0.689; 0.65: 2, 0.767; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.317; 0.35: 18, 0.351; 0.40: 4, 0.336; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.268 | 5.77% | 0.917 | 0.533 | 0.249 | 0.567 | 0.461 |
| 6h | 13.341 | 10.07% | 0.911 | 0.453 | 0.251 | 0.489 | 0.551 |
| 24h | 7.303 | 6.09% | 0.895 | 0.482 | 0.251 | 0.488 | 0.697 |
| 7d | 12.314 | 4.24% | 0.900 | 0.500 | 0.251 | 0.495 | 0.696 |
| 30d | 14.071 | 4.19% | 0.899 | 0.499 | 0.251 | 0.499 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.018 | 12.438 | 12.578 | 12.485 | 12.427 | 12.556 | 12.187 | 12.244 | 12.248 | 12.268 |
| 6h | 14.834 | 13.461 | 13.669 | 13.445 | 13.532 | 13.479 | 13.325 | 13.317 | 13.323 | 13.341 |
| 24h | 7.776 | 7.375 | 7.419 | 7.333 | 7.497 | 7.517 | 7.300 | 7.290 | 7.294 | 7.303 |
| 7d | 12.859 | 12.416 | 12.400 | 12.328 | 12.562 | 12.494 | 12.307 | 12.303 | 12.292 | 12.314 |
| 30d | 14.686 | 14.201 | 14.159 | 14.097 | 14.342 | 14.291 | 14.074 | 14.044 | 14.044 | 14.071 |

## Next candle

- candle starting 2026-10-05 02:21 UTC, last close 2734.0
- P(up) 0.5047, return quantiles (bp): {'05': -9.539, '10': -6.607, '25': -3.691, '40': -1.197, '50': 0.052, '60': 1.723, '75': 3.667, '90': 7.415, '95': 10.235}
- changepoint probability 0.044, regime age 183.6 min
- agent weights: empirical 0.003, ewma 0.076, garch 0.014, har 0.099, bocpd 0.015, hmm 0.014, online_qr 0.347, lgbm 0.434

## Learning log

- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.75, 4.48, 11.78], current probabilities: [0.017, 0.923, 0.061]
- live generator: {'versions': 60, 'latest_effective': '2026-10-05 02:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.259, 'l_abs': 0.664, 'l_hi': 0.77, 'l_lo': 0.744, 'b05': 0.717, 'b25': 0.655, 'b75': 0.543, 'b95': 0.632}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.5, 1.6], [1.5, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.4, 1.976, 2.154, 2.511, 2.596, 2.754, 2.891, 2.894, 3.181, 3.086, 3.166, 3.11, 3.233, 3.158]}
- calibration offsets (in sigma): {'05': -0.04, '10': 0.05, '25': -0.05, '40': 0.0, '50': 0.03, '60': 0.11, '75': 0.05, '90': 0.08, '95': 0.1}
