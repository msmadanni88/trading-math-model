# ETH-USD 60s candle generator - report

- generated: 2026-10-05 09:17 UTC
- last closed candle: 2026-10-05 09:17 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.635 (96) | 0.527 (670) [0.492, 0.566] | 0.512 (2876) [0.492, 0.531] | 0.516 (3164) [0.498, 0.533] | 0.583 (192) | 0.405 (37) | 0.500 | flat -0.015 (noise 0.031) |
| colour_clear | 0.558 (674) | 0.507 (5294) [0.489, 0.527] | 0.500 (23246) [0.495, 0.506] | 0.499 (25633) [0.494, 0.505] | 0.552 (1395) | 0.546 (304) | 0.500 | flat +0.010 (noise 0.012) |
| colour_confident | 0.623 (260) | 0.619 (344) | 0.619 (344) | 0.619 (344) | 0.619 (344) | 0.692 (26) | 0.500 | - |
| colour_next | 0.548 (1417) | 0.512 (9998) [0.503, 0.524] | 0.503 (42868) [0.499, 0.508] | 0.503 (47170) [0.498, 0.507] | 0.535 (2821) | 0.549 (554) | 0.500 | up +0.017 (noise 0.008) |
| colour_path | 0.506 (19838) | 0.502 (139972) [0.499, 0.505] | 0.501 (600152) [0.500, 0.502] | 0.501 (660380) [0.499, 0.502] | 0.499 (39494) | 0.516 (7756) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.648 (88) | 0.652 (115) | 0.652 (115) | 0.652 (115) | 0.652 (115) | 0.800 (5) | 0.500 | - |
| reversal_k13_next | 0.360 (86) | 0.290 (659) [0.266, 0.315] | 0.308 (2007) [0.293, 0.324] | 0.303 (2293) [0.288, 0.319] | 0.340 (188) | 0.294 (34) | 0.077 | flat -0.024 (noise 0.030) |
| reversal_k13_now | 0.600 (65) | 0.585 (361) [0.534, 0.636] | 0.589 (1448) [0.566, 0.612] | 0.587 (1582) [0.567, 0.608] | 0.664 (110) | 0.481 (27) | 0.077 | flat -0.028 (noise 0.038) |
| reversal_k3_next | 0.597 (124) | 0.590 (704) [0.563, 0.617] | 0.584 (2492) [0.569, 0.598] | 0.585 (2708) [0.571, 0.599] | 0.563 (268) | 0.632 (19) | 0.292 | flat +0.044 (noise 0.030) |
| reversal_k3_now | 0.922 (64) | 0.941 (407) [0.931, 0.953] | 0.942 (1718) [0.933, 0.951] | 0.941 (1884) [0.932, 0.949] | 0.926 (121) | 0.952 (21) | 0.292 | flat +0.001 (noise 0.017) |
| reversal_k5_next | 0.483 (120) | 0.458 (734) [0.427, 0.488] | 0.486 (2147) [0.465, 0.505] | 0.486 (2299) [0.469, 0.504] | 0.437 (309) | 0.533 (15) | 0.187 | flat -0.060 (noise 0.035) |
| reversal_k5_now | 0.897 (68) | 0.854 (389) [0.838, 0.870] | 0.839 (1601) [0.824, 0.855] | 0.839 (1740) [0.824, 0.853] | 0.861 (129) | 0.812 (16) | 0.186 | flat +0.028 (noise 0.027) |
| reversal_k8_next | 0.471 (87) | 0.401 (437) [0.365, 0.435] | 0.403 (2028) [0.385, 0.423] | 0.398 (2270) [0.382, 0.416] | 0.427 (164) | 0.333 (27) | 0.122 | flat -0.014 (noise 0.034) |
| reversal_k8_now | 0.783 (60) | 0.729 (332) [0.698, 0.756] | 0.724 (1555) [0.704, 0.743] | 0.718 (1697) [0.700, 0.738] | 0.782 (110) | 0.696 (23) | 0.122 | flat -0.024 (noise 0.033) |
| overall | 0.512 (22025) | 0.505 (154663) [0.501, 0.508] | 0.503 (660892) [0.502, 0.504] | 0.503 (727187) [0.501, 0.504] | 0.504 (43906) | 0.519 (8529) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07583, 0.1139] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5319, 'levels': [{'threshold': 0.07583, 'calls_per_day': 144.4, 'win_rate': 0.5721}, {'threshold': 0.1139, 'calls_per_day': 36.4, 'win_rate': 0.6381}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 2243, 'rate': 0.551}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15066 | 0.330 | 0.509 (14833) | 0.615 (343) | 0.786 (2382) |
| volatility: normal | 15065 | 0.359 | 0.509 (15001) | - | 0.777 (2144) |
| volatility: wild | 15066 | 0.373 | 0.493 (15021) | - | 0.774 (2094) |
| session: Asia 00-08 | 15360 | 0.351 | 0.503 (15249) | 0.655 (139) | 0.784 (2219) |
| session: Europe 08-13 | 9377 | 0.347 | 0.503 (9309) | 0.545 (66) | 0.769 (1431) |
| session: US 13-21 | 14880 | 0.363 | 0.504 (14778) | 0.625 (112) | 0.786 (2211) |
| session: late 21-24 | 5580 | 0.351 | 0.504 (5519) | 0.641 (53) | 0.765 (759) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.339 | 0.354 | 0.219 | 0.219 | 0.433 | 0.219 | 0.458 | 1.192 |
| 6h | 360 | 0.346 | 0.358 | 0.278 | 0.296 | 0.527 | 0.236 | 0.456 | 1.002 |
| 24h | 1440 | 0.340 | 0.334 | 0.257 | 0.278 | 0.551 | 0.253 | 0.428 | 1.138 |
| 7d | 10080 | 0.353 | 0.352 | 0.280 | 0.304 | 0.514 | 0.243 | 0.464 | 1.370 |
| 30d | 43200 | 0.354 | 0.354 | 0.277 | 0.307 | 0.503 | 0.245 | 0.463 | 1.283 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.339 / 0.433 / 0.883; 2: 0.341 / 0.517 / 0.933; 3: 0.334 / 0.450 / 0.933; 4: 0.350 / 0.583 / 0.900; 5: 0.326 / 0.450 / 0.933; 6: 0.346 / 0.533 / 0.950; 7: 0.337 / 0.533 / 0.967; 8: 0.354 / 0.567 / 0.967; 9: 0.328 / 0.533 / 0.967; 10: 0.355 / 0.567 / 1.000; 11: 0.337 / 0.517 / 0.967; 12: 0.318 / 0.433 / 0.950; 13: 0.312 / 0.467 / 0.933; 14: 0.321 / 0.517 / 0.950; 15: 0.341 / 0.517 / 0.933
- 6h: 1: 0.346 / 0.527 / 0.911; 2: 0.348 / 0.501 / 0.883; 3: 0.343 / 0.504 / 0.914; 4: 0.358 / 0.580 / 0.889; 5: 0.338 / 0.499 / 0.911; 6: 0.361 / 0.541 / 0.903; 7: 0.355 / 0.543 / 0.911; 8: 0.355 / 0.549 / 0.894; 9: 0.335 / 0.487 / 0.872; 10: 0.339 / 0.493 / 0.917; 11: 0.342 / 0.490 / 0.872; 12: 0.338 / 0.479 / 0.875; 13: 0.342 / 0.510 / 0.847; 14: 0.345 / 0.504 / 0.856; 15: 0.353 / 0.538 / 0.842
- 24h: 1: 0.340 / 0.551 / 0.889; 2: 0.330 / 0.513 / 0.900; 3: 0.329 / 0.512 / 0.905; 4: 0.328 / 0.519 / 0.894; 5: 0.325 / 0.496 / 0.903; 6: 0.331 / 0.523 / 0.901; 7: 0.330 / 0.518 / 0.907; 8: 0.334 / 0.527 / 0.904; 9: 0.321 / 0.496 / 0.900; 10: 0.324 / 0.511 / 0.915; 11: 0.323 / 0.492 / 0.908; 12: 0.328 / 0.531 / 0.906; 13: 0.324 / 0.518 / 0.901; 14: 0.321 / 0.496 / 0.906; 15: 0.329 / 0.527 / 0.904
- 7d: 1: 0.353 / 0.514 / 0.898; 2: 0.348 / 0.499 / 0.900; 3: 0.349 / 0.510 / 0.901; 4: 0.347 / 0.502 / 0.901; 5: 0.345 / 0.502 / 0.901; 6: 0.345 / 0.499 / 0.901; 7: 0.345 / 0.505 / 0.901; 8: 0.345 / 0.503 / 0.901; 9: 0.341 / 0.492 / 0.900; 10: 0.344 / 0.507 / 0.902; 11: 0.344 / 0.505 / 0.900; 12: 0.345 / 0.514 / 0.900; 13: 0.344 / 0.501 / 0.899; 14: 0.342 / 0.496 / 0.899; 15: 0.342 / 0.498 / 0.899
- 30d: 1: 0.354 / 0.503 / 0.898; 2: 0.351 / 0.498 / 0.900; 3: 0.352 / 0.506 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.349 / 0.504 / 0.900; 7: 0.348 / 0.506 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.345 / 0.499 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.502 / 0.900; 12: 0.345 / 0.501 / 0.900; 13: 0.345 / 0.501 / 0.900; 14: 0.344 / 0.495 / 0.900; 15: 0.343 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.099 (body 0.083, range 0.115); 'price stays where it was' would score 0.114; colour right 0.350; typical miss of the close 11.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.108 (body 0.073, range 0.144); 'price stays where it was' would score 0.124; colour right 0.471; typical miss of the close 9.9 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.108 (body 0.075, range 0.142); 'price stays where it was' would score 0.112; colour right 0.497; typical miss of the close 5.6 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.118 (body 0.077, range 0.158); 'price stays where it was' would score 0.119; colour right 0.492; typical miss of the close 7.0 bp; chain ended on the right side 0.518 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.509 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.3; 2: 0.197 / 4.3; 3: 0.170 / 6.1; 4: 0.133 / 6.5; 5: 0.123 / 7.2; 6: 0.113 / 8.2; 7: 0.100 / 8.5; 8: 0.093 / 9.0; 9: 0.088 / 9.1; 10: 0.083 / 10.0; 11: 0.077 / 10.6; 12: 0.074 / 10.9; 13: 0.066 / 11.3; 14: 0.066 / 11.4; 15: 0.062 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 91031, probability skill vs chance 0.2287, widened contest next: False
  - now: threshold 0.8418, hit rate recent 0.9254 / long run 0.939
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.307, naive rule 0.489, lift 3.05x
    - 24h: 65 calls (65 a day), hit rate 0.923, chance 0.289, naive rule 0.467, lift 3.20x
    - 7d: 414 calls (59 a day), hit rate 0.940, chance 0.290, naive rule 0.484, lift 3.25x
    - 30d: 1715 calls (57 a day), hit rate 0.941, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5642, hit rate recent 0.6099 / long run 0.5808
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.307, lift 1.78x
    - 24h: 111 calls (111 a day), hit rate 0.595, chance 0.289, lift 2.06x
    - 7d: 684 calls (98 a day), hit rate 0.591, chance 0.290, lift 2.04x
    - 30d: 2485 calls (83 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.518; 0.40: 488, 0.560; 0.45: 421, 0.626; 0.50: 368, 0.681; 0.55: 322, 0.725; 0.60: 274, 0.767; 0.65: 224, 0.803; 0.70: 182, 0.835; 0.75: 139, 0.870; 0.80: 99, 0.909; 0.85: 49, 0.949; 0.90: 2, 0.978
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.425; 0.35: 498, 0.459; 0.40: 414, 0.488; 0.45: 318, 0.519; 0.50: 209, 0.553; 0.55: 94, 0.587; 0.60: 13, 0.613; 0.65: 0, 0.733
- **K=5**: model 1790208000, labels learned 91029, probability skill vs chance 0.2171, widened contest next: False
  - now: threshold 0.7145, hit rate recent 0.8522 / long run 0.8439
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.197, naive rule 0.420, lift 4.66x
    - 24h: 60 calls (60 a day), hit rate 0.850, chance 0.185, naive rule 0.369, lift 4.61x
    - 7d: 392 calls (56 a day), hit rate 0.849, chance 0.187, naive rule 0.393, lift 4.54x
    - 30d: 1596 calls (53 a day), hit rate 0.836, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4547, hit rate recent 0.5057 / long run 0.4744
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.197, lift 3.39x
    - 24h: 97 calls (97 a day), hit rate 0.495, chance 0.185, lift 2.68x
    - 7d: 728 calls (104 a day), hit rate 0.464, chance 0.187, lift 2.48x
    - 30d: 2146 calls (72 a day), hit rate 0.487, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 432, 0.410; 0.35: 372, 0.462; 0.40: 301, 0.531; 0.45: 246, 0.589; 0.50: 191, 0.648; 0.55: 146, 0.698; 0.60: 114, 0.738; 0.65: 87, 0.782; 0.70: 64, 0.820; 0.75: 35, 0.859; 0.80: 10, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.385; 0.35: 255, 0.422; 0.40: 169, 0.448; 0.45: 89, 0.471; 0.50: 22, 0.520; 0.55: 3, 0.580
- **K=8**: model 1791158400, labels learned 91026, probability skill vs chance 0.2053, widened contest next: False
  - now: threshold 0.5611, hit rate recent 0.7459 / long run 0.7319
    - 6h: 18 calls (74 a day), hit rate 0.778, chance 0.121, naive rule 0.326, lift 6.41x
    - 24h: 66 calls (66 a day), hit rate 0.727, chance 0.126, naive rule 0.310, lift 5.78x
    - 7d: 342 calls (49 a day), hit rate 0.728, chance 0.124, naive rule 0.330, lift 5.89x
    - 30d: 1562 calls (52 a day), hit rate 0.722, chance 0.121, naive rule 0.325, lift 5.95x
  - next: threshold 0.3507, hit rate recent 0.4268 / long run 0.4089
    - 6h: 21 calls (86 a day), hit rate 0.333, chance 0.121, lift 2.75x
    - 24h: 91 calls (92 a day), hit rate 0.418, chance 0.126, lift 3.32x
    - 7d: 448 calls (64 a day), hit rate 0.400, chance 0.124, lift 3.23x
    - 30d: 2030 calls (68 a day), hit rate 0.402, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 276, 0.397; 0.35: 208, 0.473; 0.40: 161, 0.536; 0.45: 127, 0.584; 0.50: 97, 0.626; 0.55: 68, 0.680; 0.60: 46, 0.729; 0.65: 25, 0.767; 0.70: 9, 0.805; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 189, 0.343; 0.35: 118, 0.382; 0.40: 49, 0.411; 0.45: 10, 0.423; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 91021, probability skill vs chance 0.1914, widened contest next: False
  - now: threshold 0.4124, hit rate recent 0.5718 / long run 0.5911
    - 6h: 19 calls (79 a day), hit rate 0.421, chance 0.071, naive rule 0.266, lift 5.93x
    - 24h: 70 calls (71 a day), hit rate 0.571, chance 0.087, naive rule 0.281, lift 6.59x
    - 7d: 372 calls (53 a day), hit rate 0.583, chance 0.077, naive rule 0.264, lift 7.54x
    - 30d: 1460 calls (49 a day), hit rate 0.586, chance 0.077, naive rule 0.267, lift 7.63x
  - next: threshold 0.2781, hit rate recent 0.3422 / long run 0.3052
    - 6h: 20 calls (83 a day), hit rate 0.300, chance 0.071, lift 4.22x
    - 24h: 96 calls (97 a day), hit rate 0.354, chance 0.087, lift 4.09x
    - 7d: 657 calls (94 a day), hit rate 0.286, chance 0.077, lift 3.70x
    - 30d: 2023 calls (67 a day), hit rate 0.309, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.435; 0.35: 90, 0.492; 0.40: 65, 0.541; 0.45: 45, 0.600; 0.50: 29, 0.618; 0.55: 16, 0.668; 0.60: 7, 0.694; 0.65: 2, 0.767; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.316; 0.35: 18, 0.349; 0.40: 4, 0.336; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.609 | 1.93% | 0.900 | 0.600 | 0.250 | 0.483 | 0.246 |
| 6h | 13.662 | 4.02% | 0.908 | 0.503 | 0.251 | 0.496 | 0.245 |
| 24h | 9.793 | 5.42% | 0.898 | 0.485 | 0.251 | 0.499 | 0.634 |
| 7d | 12.284 | 4.31% | 0.900 | 0.501 | 0.251 | 0.495 | 0.693 |
| 30d | 14.145 | 4.15% | 0.899 | 0.500 | 0.251 | 0.499 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.877 | 13.616 | 13.662 | 13.623 | 13.879 | 13.727 | 13.513 | 13.533 | 13.526 | 13.609 |
| 6h | 14.234 | 13.711 | 13.869 | 13.757 | 13.985 | 13.875 | 13.626 | 13.648 | 13.634 | 13.662 |
| 24h | 10.354 | 9.851 | 9.946 | 9.875 | 9.985 | 9.965 | 9.775 | 9.771 | 9.773 | 9.793 |
| 7d | 12.837 | 12.384 | 12.371 | 12.301 | 12.535 | 12.472 | 12.277 | 12.272 | 12.261 | 12.284 |
| 30d | 14.757 | 14.276 | 14.231 | 14.172 | 14.418 | 14.362 | 14.148 | 14.118 | 14.118 | 14.145 |

## Next candle

- candle starting 2026-10-05 09:17 UTC, last close 2717.2
- P(up) 0.5052, return quantiles (bp): {'05': -7.717, '10': -5.541, '25': -2.782, '40': -0.91, '50': 0.05, '60': 0.982, '75': 2.735, '90': 6.251, '95': 8.58}
- changepoint probability 0.0691, regime age 43.0 min
- agent weights: empirical 0.003, ewma 0.093, garch 0.017, har 0.067, bocpd 0.009, hmm 0.016, online_qr 0.413, lgbm 0.383

## Learning log

- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.75, 4.48, 11.78], current probabilities: [0.005, 0.97, 0.026]
- live generator: {'versions': 60, 'latest_effective': '2026-10-05 09:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.29, 'l_abs': 0.585, 'l_hi': 0.773, 'l_lo': 0.745, 'b05': 0.72, 'b25': 0.606, 'b75': 0.592, 'b95': 0.682}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.499, 1.698, 2.305, 2.245, 2.514, 2.365, 2.857, 3.423, 2.523, 3.438, 3.389, 4.065, 3.981, 4.297]}
- calibration offsets (in sigma): {'05': -0.012, '10': 0.006, '25': -0.05, '40': -0.006, '50': -0.01, '60': -0.034, '75': -0.04, '90': 0.074, '95': 0.082}
