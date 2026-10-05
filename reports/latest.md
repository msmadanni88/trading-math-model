# ETH-USD 60s candle generator - report

- generated: 2026-10-05 18:35 UTC
- last closed candle: 2026-10-05 18:35 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.635 (96) | 0.527 (670) [0.492, 0.566] | 0.512 (2876) [0.492, 0.531] | 0.516 (3164) [0.498, 0.533] | 0.583 (192) | 0.446 (74) | 0.500 | flat -0.015 (noise 0.031) |
| colour_clear | 0.558 (674) | 0.507 (5294) [0.489, 0.527] | 0.500 (23246) [0.495, 0.506] | 0.499 (25633) [0.494, 0.505] | 0.552 (1395) | 0.557 (601) | 0.500 | flat +0.010 (noise 0.012) |
| colour_confident | 0.623 (260) | 0.619 (344) | 0.619 (344) | 0.619 (344) | 0.619 (344) | 0.692 (52) | 0.500 | - |
| colour_next | 0.548 (1417) | 0.512 (9998) [0.503, 0.524] | 0.503 (42868) [0.499, 0.508] | 0.503 (47170) [0.498, 0.507] | 0.535 (2821) | 0.547 (1106) | 0.500 | up +0.017 (noise 0.008) |
| colour_path | 0.506 (19838) | 0.502 (139972) [0.499, 0.505] | 0.501 (600152) [0.500, 0.502] | 0.501 (660380) [0.499, 0.502] | 0.499 (39494) | 0.508 (15484) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.648 (88) | 0.652 (115) | 0.652 (115) | 0.652 (115) | 0.652 (115) | 0.833 (6) | 0.500 | - |
| reversal_k13_next | 0.360 (86) | 0.290 (659) [0.266, 0.315] | 0.308 (2007) [0.293, 0.324] | 0.303 (2293) [0.288, 0.319] | 0.340 (188) | 0.281 (57) | 0.077 | flat -0.024 (noise 0.030) |
| reversal_k13_now | 0.600 (65) | 0.585 (361) [0.534, 0.636] | 0.589 (1448) [0.566, 0.612] | 0.587 (1582) [0.567, 0.608] | 0.664 (110) | 0.556 (54) | 0.077 | flat -0.028 (noise 0.038) |
| reversal_k3_next | 0.597 (124) | 0.590 (704) [0.563, 0.617] | 0.584 (2492) [0.569, 0.598] | 0.585 (2708) [0.571, 0.599] | 0.563 (268) | 0.641 (39) | 0.292 | flat +0.044 (noise 0.030) |
| reversal_k3_now | 0.922 (64) | 0.941 (407) [0.931, 0.953] | 0.942 (1718) [0.933, 0.951] | 0.941 (1884) [0.932, 0.949] | 0.926 (121) | 0.972 (36) | 0.292 | flat +0.001 (noise 0.017) |
| reversal_k5_next | 0.483 (120) | 0.458 (734) [0.427, 0.488] | 0.486 (2147) [0.465, 0.505] | 0.486 (2299) [0.469, 0.504] | 0.437 (309) | 0.548 (31) | 0.187 | flat -0.060 (noise 0.035) |
| reversal_k5_now | 0.897 (68) | 0.854 (389) [0.838, 0.870] | 0.839 (1601) [0.824, 0.855] | 0.839 (1740) [0.824, 0.853] | 0.861 (129) | 0.867 (30) | 0.186 | flat +0.028 (noise 0.027) |
| reversal_k8_next | 0.471 (87) | 0.401 (437) [0.365, 0.435] | 0.403 (2028) [0.385, 0.423] | 0.398 (2270) [0.382, 0.416] | 0.427 (164) | 0.333 (63) | 0.122 | flat -0.014 (noise 0.034) |
| reversal_k8_now | 0.783 (60) | 0.729 (332) [0.698, 0.756] | 0.724 (1555) [0.704, 0.743] | 0.718 (1697) [0.700, 0.738] | 0.782 (110) | 0.745 (47) | 0.122 | flat -0.024 (noise 0.033) |
| overall | 0.512 (22025) | 0.505 (154663) [0.501, 0.508] | 0.503 (660892) [0.502, 0.504] | 0.503 (727187) [0.501, 0.504] | 0.504 (43906) | 0.511 (17021) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07573, 0.1139] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5327, 'levels': [{'threshold': 0.07573, 'calls_per_day': 143.9, 'win_rate': 0.5758}, {'threshold': 0.1139, 'calls_per_day': 35.6, 'win_rate': 0.6335}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 2795, 'rate': 0.5499}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15252 | 0.331 | 0.509 (15015) | 0.619 (360) | 0.787 (2424) |
| volatility: normal | 15251 | 0.359 | 0.509 (15186) | 0.700 (30) | 0.776 (2162) |
| volatility: wild | 15252 | 0.373 | 0.494 (15206) | - | 0.774 (2114) |
| session: Asia 00-08 | 15360 | 0.351 | 0.503 (15249) | 0.655 (139) | 0.784 (2219) |
| session: Europe 08-13 | 9600 | 0.348 | 0.504 (9529) | 0.557 (79) | 0.769 (1474) |
| session: US 13-21 | 15215 | 0.363 | 0.505 (15110) | 0.640 (125) | 0.786 (2248) |
| session: late 21-24 | 5580 | 0.351 | 0.504 (5519) | 0.641 (53) | 0.765 (759) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.386 | 0.403 | 0.276 | 0.276 | 0.559 | 0.285 | 0.488 | 1.155 |
| 6h | 360 | 0.379 | 0.387 | 0.298 | 0.314 | 0.525 | 0.255 | 0.503 | 1.423 |
| 24h | 1440 | 0.363 | 0.361 | 0.274 | 0.304 | 0.550 | 0.264 | 0.463 | 1.084 |
| 7d | 10080 | 0.353 | 0.352 | 0.278 | 0.303 | 0.516 | 0.243 | 0.463 | 1.361 |
| 30d | 43200 | 0.355 | 0.354 | 0.278 | 0.308 | 0.504 | 0.246 | 0.464 | 1.280 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.386 / 0.559 / 0.950; 2: 0.408 / 0.627 / 0.967; 3: 0.374 / 0.458 / 0.967; 4: 0.393 / 0.593 / 0.983; 5: 0.347 / 0.390 / 0.967; 6: 0.395 / 0.576 / 0.983; 7: 0.359 / 0.441 / 0.917; 8: 0.381 / 0.525 / 0.983; 9: 0.372 / 0.525 / 0.983; 10: 0.384 / 0.542 / 0.883; 11: 0.384 / 0.525 / 0.950; 12: 0.376 / 0.508 / 0.950; 13: 0.407 / 0.559 / 0.967; 14: 0.375 / 0.492 / 0.967; 15: 0.376 / 0.525 / 0.967
- 6h: 1: 0.379 / 0.525 / 0.903; 2: 0.383 / 0.553 / 0.919; 3: 0.375 / 0.514 / 0.883; 4: 0.378 / 0.539 / 0.922; 5: 0.360 / 0.469 / 0.900; 6: 0.367 / 0.528 / 0.914; 7: 0.361 / 0.489 / 0.881; 8: 0.364 / 0.475 / 0.925; 9: 0.372 / 0.539 / 0.936; 10: 0.360 / 0.483 / 0.839; 11: 0.351 / 0.463 / 0.911; 12: 0.356 / 0.469 / 0.897; 13: 0.365 / 0.506 / 0.933; 14: 0.363 / 0.486 / 0.928; 15: 0.364 / 0.506 / 0.922
- 24h: 1: 0.363 / 0.550 / 0.901; 2: 0.360 / 0.535 / 0.910; 3: 0.354 / 0.506 / 0.900; 4: 0.353 / 0.516 / 0.910; 5: 0.348 / 0.498 / 0.906; 6: 0.352 / 0.509 / 0.909; 7: 0.354 / 0.531 / 0.899; 8: 0.356 / 0.516 / 0.911; 9: 0.346 / 0.501 / 0.914; 10: 0.344 / 0.502 / 0.893; 11: 0.341 / 0.477 / 0.909; 12: 0.346 / 0.507 / 0.912; 13: 0.351 / 0.525 / 0.914; 14: 0.343 / 0.497 / 0.912; 15: 0.348 / 0.512 / 0.910
- 7d: 1: 0.353 / 0.516 / 0.898; 2: 0.349 / 0.504 / 0.901; 3: 0.349 / 0.511 / 0.900; 4: 0.347 / 0.505 / 0.902; 5: 0.344 / 0.500 / 0.901; 6: 0.344 / 0.497 / 0.902; 7: 0.346 / 0.508 / 0.900; 8: 0.344 / 0.501 / 0.902; 9: 0.341 / 0.494 / 0.902; 10: 0.343 / 0.506 / 0.899; 11: 0.344 / 0.505 / 0.901; 12: 0.344 / 0.513 / 0.901; 13: 0.344 / 0.504 / 0.901; 14: 0.341 / 0.493 / 0.902; 15: 0.341 / 0.495 / 0.902
- 30d: 1: 0.355 / 0.504 / 0.898; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.506 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.349 / 0.504 / 0.900; 7: 0.349 / 0.506 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.346 / 0.499 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.347 / 0.502 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.344 / 0.495 / 0.900; 15: 0.344 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.137 (body 0.106, range 0.168); 'price stays where it was' would score 0.131; colour right 0.525; typical miss of the close 5.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.121 (body 0.088, range 0.153); 'price stays where it was' would score 0.114; colour right 0.553; typical miss of the close 11.0 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.112 (body 0.080, range 0.144); 'price stays where it was' would score 0.120; colour right 0.517; typical miss of the close 7.9 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.157); 'price stays where it was' would score 0.119; colour right 0.496; typical miss of the close 6.9 bp; chain ended on the right side 0.510 of 670 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.509 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.3; 2: 0.198 / 4.4; 3: 0.170 / 6.1; 4: 0.133 / 6.5; 5: 0.123 / 7.3; 6: 0.113 / 8.2; 7: 0.099 / 8.6; 8: 0.092 / 9.1; 9: 0.088 / 9.3; 10: 0.082 / 10.1; 11: 0.076 / 10.7; 12: 0.074 / 11.1; 13: 0.065 / 11.4; 14: 0.066 / 11.5; 15: 0.062 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 91589, probability skill vs chance 0.2295, widened contest next: False
  - now: threshold 0.8423, hit rate recent 0.942 / long run 0.9405
    - 6h: 8 calls (32 a day), hit rate 1.000, chance 0.311, naive rule 0.505, lift 3.21x
    - 24h: 55 calls (55 a day), hit rate 0.927, chance 0.307, naive rule 0.502, lift 3.02x
    - 7d: 413 calls (59 a day), hit rate 0.942, chance 0.290, naive rule 0.484, lift 3.24x
    - 30d: 1704 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5694, hit rate recent 0.6186 / long run 0.583
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.311, lift 1.87x
    - 24h: 68 calls (68 a day), hit rate 0.632, chance 0.307, lift 2.06x
    - 7d: 670 calls (96 a day), hit rate 0.590, chance 0.290, lift 2.03x
    - 30d: 2461 calls (82 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 538, 0.518; 0.40: 488, 0.560; 0.45: 421, 0.626; 0.50: 368, 0.681; 0.55: 322, 0.725; 0.60: 274, 0.767; 0.65: 225, 0.804; 0.70: 182, 0.835; 0.75: 139, 0.871; 0.80: 98, 0.910; 0.85: 49, 0.950; 0.90: 2, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.425; 0.35: 497, 0.460; 0.40: 413, 0.488; 0.45: 317, 0.519; 0.50: 208, 0.553; 0.55: 93, 0.587; 0.60: 13, 0.615; 0.65: 0, 0.733
- **K=5**: model 1790208000, labels learned 91587, probability skill vs chance 0.2155, widened contest next: False
  - now: threshold 0.7137, hit rate recent 0.8691 / long run 0.8459
    - 6h: 8 calls (33 a day), hit rate 1.000, chance 0.200, naive rule 0.392, lift 5.01x
    - 24h: 48 calls (48 a day), hit rate 0.833, chance 0.198, naive rule 0.403, lift 4.21x
    - 7d: 387 calls (55 a day), hit rate 0.853, chance 0.188, naive rule 0.394, lift 4.54x
    - 30d: 1584 calls (53 a day), hit rate 0.838, chance 0.186, naive rule 0.389, lift 4.51x
  - next: threshold 0.4565, hit rate recent 0.5168 / long run 0.4766
    - 6h: 10 calls (41 a day), hit rate 0.400, chance 0.200, lift 2.00x
    - 24h: 56 calls (56 a day), hit rate 0.571, chance 0.198, lift 2.89x
    - 7d: 727 calls (104 a day), hit rate 0.465, chance 0.188, lift 2.48x
    - 30d: 2127 calls (71 a day), hit rate 0.488, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 432, 0.410; 0.35: 372, 0.462; 0.40: 300, 0.531; 0.45: 246, 0.589; 0.50: 191, 0.648; 0.55: 146, 0.698; 0.60: 114, 0.739; 0.65: 87, 0.783; 0.70: 64, 0.821; 0.75: 35, 0.860; 0.80: 10, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.385; 0.35: 254, 0.422; 0.40: 168, 0.449; 0.45: 87, 0.473; 0.50: 22, 0.520; 0.55: 3, 0.582
- **K=8**: model 1791158400, labels learned 91584, probability skill vs chance 0.198, widened contest next: False
  - now: threshold 0.562, hit rate recent 0.7652 / long run 0.7343
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.120, naive rule 0.325, lift 7.69x
    - 24h: 66 calls (66 a day), hit rate 0.727, chance 0.126, naive rule 0.331, lift 5.79x
    - 7d: 351 calls (50 a day), hit rate 0.735, chance 0.124, naive rule 0.331, lift 5.93x
    - 30d: 1567 calls (52 a day), hit rate 0.724, chance 0.121, naive rule 0.325, lift 5.98x
  - next: threshold 0.3527, hit rate recent 0.387 / long run 0.4045
    - 6h: 19 calls (78 a day), hit rate 0.368, chance 0.120, lift 3.07x
    - 24h: 84 calls (85 a day), hit rate 0.405, chance 0.126, lift 3.22x
    - 7d: 468 calls (67 a day), hit rate 0.397, chance 0.124, lift 3.21x
    - 30d: 2036 calls (68 a day), hit rate 0.403, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 276, 0.397; 0.35: 207, 0.473; 0.40: 160, 0.537; 0.45: 126, 0.585; 0.50: 97, 0.627; 0.55: 69, 0.682; 0.60: 46, 0.730; 0.65: 24, 0.770; 0.70: 9, 0.807; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 188, 0.343; 0.35: 118, 0.383; 0.40: 49, 0.411; 0.45: 10, 0.424; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 91579, probability skill vs chance 0.1857, widened contest next: False
  - now: threshold 0.4162, hit rate recent 0.5922 / long run 0.5928
    - 6h: 15 calls (63 a day), hit rate 0.667, chance 0.078, naive rule 0.274, lift 8.52x
    - 24h: 71 calls (72 a day), hit rate 0.563, chance 0.085, naive rule 0.302, lift 6.63x
    - 7d: 380 calls (54 a day), hit rate 0.587, chance 0.078, naive rule 0.268, lift 7.50x
    - 30d: 1467 calls (49 a day), hit rate 0.587, chance 0.077, naive rule 0.267, lift 7.64x
  - next: threshold 0.275, hit rate recent 0.3188 / long run 0.3036
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.078, lift 3.99x
    - 24h: 79 calls (80 a day), hit rate 0.316, chance 0.085, lift 3.73x
    - 7d: 638 calls (91 a day), hit rate 0.290, chance 0.078, lift 3.71x
    - 30d: 2019 calls (67 a day), hit rate 0.310, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.437; 0.35: 90, 0.493; 0.40: 65, 0.541; 0.45: 45, 0.601; 0.50: 29, 0.620; 0.55: 16, 0.668; 0.60: 7, 0.692; 0.65: 2, 0.759; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.316; 0.35: 17, 0.356; 0.40: 4, 0.336; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.868 | 5.67% | 0.950 | 0.500 | 0.243 | 0.593 | 0.158 |
| 6h | 14.828 | 5.34% | 0.922 | 0.519 | 0.249 | 0.534 | 0.609 |
| 24h | 12.589 | 5.60% | 0.912 | 0.500 | 0.250 | 0.508 | 0.578 |
| 7d | 11.845 | 4.23% | 0.901 | 0.500 | 0.251 | 0.496 | 0.686 |
| 30d | 14.211 | 4.14% | 0.900 | 0.500 | 0.251 | 0.499 | 0.691 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.341 | 7.923 | 7.796 | 8.344 | 7.843 | 7.989 | 7.956 | 7.908 | 7.944 | 7.868 |
| 6h | 15.664 | 15.030 | 14.958 | 14.947 | 15.122 | 15.008 | 14.806 | 14.827 | 14.810 | 14.828 |
| 24h | 13.336 | 12.693 | 12.779 | 12.709 | 12.813 | 12.770 | 12.563 | 12.571 | 12.566 | 12.589 |
| 7d | 12.369 | 11.939 | 11.933 | 11.865 | 12.085 | 12.035 | 11.839 | 11.837 | 11.825 | 11.845 |
| 30d | 14.824 | 14.342 | 14.295 | 14.238 | 14.483 | 14.425 | 14.214 | 14.184 | 14.184 | 14.211 |

## Next candle

- candle starting 2026-10-05 18:35 UTC, last close 2708.66
- P(up) 0.556, return quantiles (bp): {'05': -5.414, '10': -3.807, '25': -1.804, '40': -0.226, '50': 0.267, '60': 0.829, '75': 1.785, '90': 3.841, '95': 5.479}
- changepoint probability 0.0467, regime age 99.2 min
- agent weights: empirical 0.003, ewma 0.066, garch 0.051, har 0.066, bocpd 0.018, hmm 0.032, online_qr 0.401, lgbm 0.362

## Learning log

- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- HMM volatility states (sd, bp per minute): [1.73, 4.67, 11.81], current probabilities: [0.515, 0.478, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-10-05 18:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.302, 'l_abs': 0.574, 'l_hi': 0.768, 'l_lo': 0.745, 'b05': 0.699, 'b25': 0.572, 'b75': 0.627, 'b95': 0.683}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.05, 1.739, 1.615, 1.921, 1.908, 2.573, 1.923, 2.085, 3.778, 2.557, 2.73, 2.476, 2.424, 2.67]}
- calibration offsets (in sigma): {'05': 0.027, '10': 0.074, '25': 0.035, '40': 0.116, '50': 0.08, '60': 0.054, '75': -0.015, '90': -0.044, '95': -0.007}
