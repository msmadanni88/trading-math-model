# ETH-USD 60s candle generator - report

- generated: 2026-10-04 23:32 UTC
- last closed candle: 2026-10-04 23:32 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k13_next 0.276 in the last 7 days, -0.063 against the 7 before
- WIN RATE FALLING: reversal_k5_next 0.451 in the last 7 days, -0.094 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.380 in the last 7 days, -0.071 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.521 (670) [0.491, 0.551] | 0.510 (2876) [0.491, 0.528] | 0.512 (3068) [0.495, 0.530] | 0.531 (96) | 0.638 (94) | 0.500 | flat -0.024 (noise 0.030) |
| colour_clear | 0.546 (721) | 0.501 (5394) [0.487, 0.516] | 0.499 (23299) [0.494, 0.504] | 0.498 (24959) [0.493, 0.503] | 0.546 (721) | 0.558 (661) | 0.500 | flat +0.001 (noise 0.010) |
| colour_confident | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.623 (260) | 0.500 | - |
| colour_next | 0.521 (1404) | 0.507 (10003) [0.501, 0.512] | 0.502 (42884) [0.498, 0.505] | 0.501 (45753) [0.497, 0.505] | 0.521 (1404) | 0.549 (1389) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.493 (19656) | 0.501 (140042) [0.498, 0.504] | 0.501 (600376) [0.500, 0.502] | 0.500 (640542) [0.499, 0.502] | 0.493 (19656) | 0.505 (19446) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.648 (88) | 0.500 | - |
| reversal_k13_next | 0.324 (102) | 0.276 (635) [0.256, 0.295] | 0.307 (1993) [0.292, 0.323] | 0.301 (2207) [0.287, 0.318] | 0.324 (102) | 0.369 (84) | 0.076 | down -0.063 (noise 0.031) |
| reversal_k13_now | 0.756 (45) | 0.594 (342) [0.539, 0.654] | 0.588 (1428) [0.566, 0.613] | 0.586 (1517) [0.564, 0.608] | 0.756 (45) | 0.594 (64) | 0.076 | flat -0.026 (noise 0.040) |
| reversal_k3_next | 0.535 (144) | 0.578 (689) [0.549, 0.610] | 0.584 (2430) [0.568, 0.599] | 0.584 (2584) [0.570, 0.599] | 0.535 (144) | 0.602 (123) | 0.292 | flat +0.006 (noise 0.031) |
| reversal_k3_now | 0.930 (57) | 0.946 (388) [0.936, 0.958] | 0.942 (1710) [0.933, 0.950] | 0.941 (1820) [0.933, 0.949] | 0.930 (57) | 0.921 (63) | 0.292 | flat +0.003 (noise 0.016) |
| reversal_k5_next | 0.407 (189) | 0.451 (658) [0.418, 0.484] | 0.486 (2076) [0.466, 0.506] | 0.486 (2179) [0.469, 0.506] | 0.407 (189) | 0.487 (119) | 0.187 | down -0.094 (noise 0.034) |
| reversal_k5_now | 0.820 (61) | 0.858 (366) [0.838, 0.886] | 0.836 (1587) [0.821, 0.851] | 0.837 (1672) [0.823, 0.851] | 0.820 (61) | 0.895 (67) | 0.187 | flat +0.041 (noise 0.027) |
| reversal_k8_next | 0.377 (77) | 0.380 (418) [0.355, 0.406] | 0.400 (2018) [0.382, 0.419] | 0.395 (2183) [0.379, 0.414] | 0.377 (77) | 0.465 (86) | 0.121 | down -0.071 (noise 0.035) |
| reversal_k8_now | 0.780 (50) | 0.735 (325) [0.700, 0.772] | 0.718 (1551) [0.698, 0.738] | 0.716 (1637) [0.697, 0.736] | 0.780 (50) | 0.780 (59) | 0.121 | flat -0.013 (noise 0.033) |
| overall | 0.496 (21881) | 0.503 (154536) [0.500, 0.506] | 0.503 (660929) [0.502, 0.504] | 0.502 (705162) [0.501, 0.504] | 0.496 (21881) | 0.512 (21594) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07548, 0.1127] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5306, 'levels': [{'threshold': 0.07548, 'calls_per_day': 144.9, 'win_rate': 0.5616}, {'threshold': 0.1127, 'calls_per_day': 36.7, 'win_rate': 0.6255}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 1661, 'rate': 0.5527}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15351 | 0.331 | 0.510 (15118) | 0.617 (342) | 0.783 (2426) |
| volatility: normal | 15351 | 0.359 | 0.507 (15285) | - | 0.774 (2149) |
| volatility: wild | 15350 | 0.373 | 0.492 (15306) | - | 0.778 (2144) |
| session: Asia 00-08 | 15360 | 0.350 | 0.500 (15249) | 0.635 (115) | 0.784 (2200) |
| session: Europe 08-13 | 9600 | 0.348 | 0.505 (9531) | 0.562 (64) | 0.768 (1459) |
| session: US 13-21 | 15360 | 0.364 | 0.504 (15258) | 0.625 (112) | 0.785 (2284) |
| session: late 21-24 | 5732 | 0.351 | 0.502 (5671) | 0.641 (53) | 0.764 (776) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.367 | 0.359 | 0.302 | 0.302 | 0.467 | 0.257 | 0.478 | 0.876 |
| 6h | 360 | 0.339 | 0.315 | 0.254 | 0.262 | 0.573 | 0.266 | 0.412 | 1.014 |
| 24h | 1440 | 0.314 | 0.304 | 0.238 | 0.248 | 0.550 | 0.237 | 0.392 | 1.260 |
| 7d | 10080 | 0.354 | 0.352 | 0.281 | 0.305 | 0.512 | 0.242 | 0.465 | 1.405 |
| 30d | 43200 | 0.354 | 0.353 | 0.277 | 0.307 | 0.503 | 0.245 | 0.463 | 1.298 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.367 / 0.467 / 0.950; 2: 0.410 / 0.633 / 0.983; 3: 0.352 / 0.400 / 0.983; 4: 0.367 / 0.500 / 0.967; 5: 0.396 / 0.550 / 0.983; 6: 0.393 / 0.583 / 1.000; 7: 0.383 / 0.550 / 0.983; 8: 0.381 / 0.517 / 0.983; 9: 0.362 / 0.483 / 0.983; 10: 0.344 / 0.417 / 0.967; 11: 0.372 / 0.550 / 1.000; 12: 0.345 / 0.383 / 1.000; 13: 0.362 / 0.517 / 1.000; 14: 0.366 / 0.467 / 0.983; 15: 0.380 / 0.567 / 0.983
- 6h: 1: 0.339 / 0.573 / 0.875; 2: 0.327 / 0.545 / 0.869; 3: 0.322 / 0.500 / 0.867; 4: 0.322 / 0.500 / 0.878; 5: 0.320 / 0.477 / 0.872; 6: 0.328 / 0.514 / 0.881; 7: 0.323 / 0.525 / 0.872; 8: 0.329 / 0.531 / 0.872; 9: 0.320 / 0.500 / 0.894; 10: 0.309 / 0.503 / 0.883; 11: 0.317 / 0.500 / 0.889; 12: 0.320 / 0.525 / 0.922; 13: 0.314 / 0.511 / 0.917; 14: 0.320 / 0.508 / 0.903; 15: 0.323 / 0.542 / 0.908
- 24h: 1: 0.314 / 0.550 / 0.877; 2: 0.299 / 0.519 / 0.893; 3: 0.300 / 0.521 / 0.890; 4: 0.293 / 0.501 / 0.893; 5: 0.293 / 0.480 / 0.892; 6: 0.296 / 0.503 / 0.894; 7: 0.294 / 0.511 / 0.892; 8: 0.297 / 0.501 / 0.892; 9: 0.290 / 0.490 / 0.892; 10: 0.293 / 0.509 / 0.891; 11: 0.295 / 0.501 / 0.890; 12: 0.296 / 0.535 / 0.894; 13: 0.290 / 0.496 / 0.898; 14: 0.293 / 0.497 / 0.899; 15: 0.294 / 0.506 / 0.899
- 7d: 1: 0.354 / 0.512 / 0.896; 2: 0.348 / 0.495 / 0.899; 3: 0.350 / 0.511 / 0.900; 4: 0.347 / 0.500 / 0.900; 5: 0.346 / 0.505 / 0.900; 6: 0.344 / 0.497 / 0.900; 7: 0.345 / 0.503 / 0.900; 8: 0.344 / 0.502 / 0.900; 9: 0.341 / 0.492 / 0.901; 10: 0.344 / 0.507 / 0.901; 11: 0.344 / 0.507 / 0.901; 12: 0.345 / 0.515 / 0.901; 13: 0.344 / 0.502 / 0.901; 14: 0.342 / 0.496 / 0.901; 15: 0.342 / 0.497 / 0.901
- 30d: 1: 0.354 / 0.503 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.506 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.348 / 0.501 / 0.900; 6: 0.348 / 0.503 / 0.900; 7: 0.348 / 0.506 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.499 / 0.900; 10: 0.346 / 0.504 / 0.900; 11: 0.346 / 0.503 / 0.900; 12: 0.345 / 0.502 / 0.900; 13: 0.344 / 0.500 / 0.900; 14: 0.344 / 0.495 / 0.900; 15: 0.343 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.228 (body 0.161, range 0.296); 'price stays where it was' would score 0.257; colour right 0.617; typical miss of the close 4.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.084, range 0.152); 'price stays where it was' would score 0.124; colour right 0.506; typical miss of the close 4.3 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.111 (body 0.078, range 0.144); 'price stays where it was' would score 0.111; colour right 0.504; typical miss of the close 3.4 bp; chain ended on the right side 0.625 of 96 chains; n=1440
- 7d: match 0.119 (body 0.078, range 0.160); 'price stays where it was' would score 0.120; colour right 0.493; typical miss of the close 7.0 bp; chain ended on the right side 0.527 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.512 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.2; 2: 0.197 / 4.3; 3: 0.169 / 6.0; 4: 0.133 / 6.3; 5: 0.123 / 7.1; 6: 0.112 / 8.0; 7: 0.099 / 8.3; 8: 0.092 / 8.7; 9: 0.088 / 9.0; 10: 0.083 / 9.7; 11: 0.077 / 10.3; 12: 0.075 / 10.7; 13: 0.067 / 11.0; 14: 0.067 / 11.1; 15: 0.063 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 90446, probability skill vs chance 0.2222, widened contest next: False
  - now: threshold 0.8398, hit rate recent 0.9146 / long run 0.9384
    - 6h: 20 calls (81 a day), hit rate 0.850, chance 0.311, naive rule 0.498, lift 2.73x
    - 24h: 64 calls (64 a day), hit rate 0.922, chance 0.284, naive rule 0.475, lift 3.24x
    - 7d: 408 calls (58 a day), hit rate 0.941, chance 0.288, naive rule 0.483, lift 3.26x
    - 30d: 1717 calls (57 a day), hit rate 0.942, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5503, hit rate recent 0.6119 / long run 0.5801
    - 6h: 35 calls (142 a day), hit rate 0.629, chance 0.311, lift 2.02x
    - 24h: 127 calls (127 a day), hit rate 0.606, chance 0.284, lift 2.13x
    - 7d: 705 calls (101 a day), hit rate 0.589, chance 0.288, lift 2.04x
    - 30d: 2493 calls (83 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.518; 0.40: 489, 0.560; 0.45: 421, 0.626; 0.50: 368, 0.681; 0.55: 321, 0.725; 0.60: 274, 0.766; 0.65: 224, 0.804; 0.70: 182, 0.835; 0.75: 139, 0.870; 0.80: 99, 0.909; 0.85: 50, 0.950; 0.90: 1, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 414, 0.487; 0.45: 318, 0.518; 0.50: 210, 0.550; 0.55: 95, 0.586; 0.60: 13, 0.614; 0.65: 0, 0.733
- **K=5**: model 1790208000, labels learned 90444, probability skill vs chance 0.2191, widened contest next: False
  - now: threshold 0.7106, hit rate recent 0.8588 / long run 0.8445
    - 6h: 19 calls (78 a day), hit rate 0.789, chance 0.195, naive rule 0.383, lift 4.04x
    - 24h: 68 calls (68 a day), hit rate 0.897, chance 0.180, naive rule 0.372, lift 4.99x
    - 7d: 391 calls (56 a day), hit rate 0.852, chance 0.187, naive rule 0.392, lift 4.57x
    - 30d: 1600 calls (53 a day), hit rate 0.839, chance 0.186, naive rule 0.390, lift 4.51x
  - next: threshold 0.4504, hit rate recent 0.502 / long run 0.4736
    - 6h: 30 calls (122 a day), hit rate 0.600, chance 0.195, lift 3.07x
    - 24h: 123 calls (124 a day), hit rate 0.496, chance 0.180, lift 2.76x
    - 7d: 734 calls (105 a day), hit rate 0.458, chance 0.187, lift 2.45x
    - 30d: 2147 calls (72 a day), hit rate 0.487, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 433, 0.410; 0.35: 373, 0.462; 0.40: 301, 0.530; 0.45: 246, 0.588; 0.50: 192, 0.648; 0.55: 147, 0.697; 0.60: 115, 0.739; 0.65: 88, 0.783; 0.70: 65, 0.821; 0.75: 35, 0.861; 0.80: 10, 0.884
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.384; 0.35: 255, 0.421; 0.40: 170, 0.447; 0.45: 90, 0.471; 0.50: 23, 0.518; 0.55: 3, 0.580
- **K=8**: model 1791072000, labels learned 90441, probability skill vs chance 0.2106, widened contest next: False
  - now: threshold 0.5589, hit rate recent 0.7576 / long run 0.7328
    - 6h: 20 calls (82 a day), hit rate 0.700, chance 0.147, naive rule 0.380, lift 4.76x
    - 24h: 60 calls (60 a day), hit rate 0.783, chance 0.132, naive rule 0.331, lift 5.94x
    - 7d: 333 calls (48 a day), hit rate 0.727, chance 0.124, naive rule 0.332, lift 5.84x
    - 30d: 1554 calls (52 a day), hit rate 0.723, chance 0.122, naive rule 0.326, lift 5.95x
  - next: threshold 0.3583, hit rate recent 0.4629 / long run 0.4114
    - 6h: 25 calls (103 a day), hit rate 0.560, chance 0.147, lift 3.81x
    - 24h: 86 calls (87 a day), hit rate 0.465, chance 0.132, lift 3.53x
    - 7d: 437 calls (62 a day), hit rate 0.398, chance 0.124, lift 3.20x
    - 30d: 2029 calls (68 a day), hit rate 0.403, chance 0.122, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 276, 0.397; 0.35: 208, 0.474; 0.40: 161, 0.537; 0.45: 127, 0.586; 0.50: 97, 0.627; 0.55: 69, 0.681; 0.60: 46, 0.730; 0.65: 25, 0.765; 0.70: 9, 0.806; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 190, 0.344; 0.35: 119, 0.382; 0.40: 49, 0.410; 0.45: 10, 0.420; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 90436, probability skill vs chance 0.1967, widened contest next: False
  - now: threshold 0.4081, hit rate recent 0.6205 / long run 0.5956
    - 6h: 17 calls (71 a day), hit rate 0.588, chance 0.101, naive rule 0.345, lift 5.80x
    - 24h: 65 calls (66 a day), hit rate 0.600, chance 0.087, naive rule 0.275, lift 6.92x
    - 7d: 362 calls (52 a day), hit rate 0.583, chance 0.079, naive rule 0.266, lift 7.42x
    - 30d: 1448 calls (48 a day), hit rate 0.588, chance 0.077, naive rule 0.267, lift 7.67x
  - next: threshold 0.2667, hit rate recent 0.3837 / long run 0.3068
    - 6h: 23 calls (96 a day), hit rate 0.478, chance 0.101, lift 4.71x
    - 24h: 84 calls (85 a day), hit rate 0.369, chance 0.087, lift 4.26x
    - 7d: 658 calls (94 a day), hit rate 0.290, chance 0.079, lift 3.69x
    - 30d: 2005 calls (67 a day), hit rate 0.309, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.436; 0.35: 90, 0.492; 0.40: 65, 0.540; 0.45: 45, 0.602; 0.50: 29, 0.619; 0.55: 16, 0.667; 0.60: 7, 0.689; 0.65: 2, 0.770; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.316; 0.35: 18, 0.350; 0.40: 4, 0.333; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.256 | 15.57% | 0.983 | 0.417 | 0.251 | 0.417 | 0.222 |
| 6h | 9.490 | 8.78% | 0.892 | 0.469 | 0.251 | 0.466 | 0.717 |
| 24h | 6.473 | 4.99% | 0.889 | 0.490 | 0.251 | 0.492 | 0.665 |
| 7d | 12.449 | 4.33% | 0.899 | 0.500 | 0.251 | 0.495 | 0.696 |
| 30d | 14.047 | 4.19% | 0.899 | 0.499 | 0.251 | 0.499 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 18.068 | 15.335 | 15.632 | 15.335 | 15.607 | 15.439 | 15.251 | 15.177 | 15.211 | 15.256 |
| 6h | 10.403 | 9.522 | 9.621 | 9.518 | 9.704 | 9.663 | 9.518 | 9.483 | 9.481 | 9.490 |
| 24h | 6.814 | 6.533 | 6.550 | 6.489 | 6.687 | 6.719 | 6.481 | 6.464 | 6.469 | 6.473 |
| 7d | 13.013 | 12.551 | 12.533 | 12.461 | 12.700 | 12.630 | 12.441 | 12.439 | 12.427 | 12.449 |
| 30d | 14.662 | 14.177 | 14.135 | 14.072 | 14.318 | 14.268 | 14.051 | 14.020 | 14.020 | 14.047 |

## Next candle

- candle starting 2026-10-04 23:32 UTC, last close 2731.22
- P(up) 0.5112, return quantiles (bp): {'05': -11.306, '10': -7.516, '25': -3.745, '40': -1.124, '50': 0.138, '60': 1.663, '75': 3.851, '90': 8.383, '95': 11.678}
- changepoint probability 0.0141, regime age 80.5 min
- agent weights: empirical 0.003, ewma 0.128, garch 0.041, har 0.193, bocpd 0.011, hmm 0.011, online_qr 0.239, lgbm 0.376

## Learning log

- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- HMM volatility states (sd, bp per minute): [1.75, 4.62, 12.53], current probabilities: [0.0, 0.933, 0.067]
- live generator: {'versions': 60, 'latest_effective': '2026-10-04 23:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.243, 'l_abs': 0.709, 'l_hi': 0.747, 'l_lo': 0.712, 'b05': 0.706, 'b25': 0.692, 'b75': 0.552, 'b95': 0.615}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6]], 'cone_width': [1.812, 2.315, 2.573, 2.883, 2.98, 3.29, 3.524, 3.672, 3.956, 4.075, 3.783, 3.715, 3.863, 3.85]}
- calibration offsets (in sigma): {'05': -0.0545, '10': 0.041, '25': -0.0125, '40': 0.024, '50': 0.045, '60': 0.076, '75': 0.0325, '90': 0.089, '95': 0.1345}
