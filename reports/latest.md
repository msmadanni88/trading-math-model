# ETH-USD 60s candle generator - report

- generated: 2026-11-25 09:08 UTC
- last closed candle: 2026-11-25 09:08 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.515 (672) [0.492, 0.540] | 0.512 (2879) [0.496, 0.526] | 0.515 (8057) [0.505, 0.526] | 0.517 (5085) [0.503, 0.531] | 0.472 (36) | 0.500 | flat -0.017 (noise 0.027) |
| colour_clear | 0.546 (804) | 0.554 (5524) [0.542, 0.567] | 0.542 (23825) [0.536, 0.548] | 0.526 (66118) [0.521, 0.532] | 0.544 (41880) [0.540, 0.548] | 0.604 (308) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.532 (188) | 0.579 (1325) [0.561, 0.593] | 0.570 (4442) [0.559, 0.580] | 0.584 (7903) [0.575, 0.593] | 0.584 (7903) [0.575, 0.593] | 0.574 (68) | 0.500 | flat +0.042 (noise 0.021) |
| colour_next | 0.528 (1436) | 0.536 (10047) [0.529, 0.543] | 0.531 (42902) [0.527, 0.535] | 0.519 (120092) [0.516, 0.523] | 0.530 (75743) [0.527, 0.534] | 0.557 (544) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140658) [0.500, 0.505] | 0.502 (600628) [0.501, 0.503] | 0.501 (1681288) [0.500, 0.502] | 0.501 (1060402) [0.500, 0.502] | 0.502 (7616) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.452 (62) | 0.598 (395) [0.542, 0.641] | 0.602 (1177) [0.580, 0.621] | 0.618 (2118) [0.602, 0.633] | 0.618 (2118) [0.602, 0.633] | 0.471 (17) | 0.500 | flat +0.035 (noise 0.042) |
| reversal_k13_next | 0.431 (51) | 0.361 (427) [0.321, 0.407] | 0.339 (1812) [0.320, 0.359] | 0.318 (5496) [0.308, 0.328] | 0.329 (3391) [0.318, 0.341] | 0.320 (25) | 0.078 | flat +0.046 (noise 0.037) |
| reversal_k13_now | 0.727 (55) | 0.588 (374) [0.543, 0.640] | 0.577 (1625) [0.554, 0.599] | 0.575 (4331) [0.563, 0.588] | 0.572 (2859) [0.555, 0.588] | 0.643 (14) | 0.078 | flat +0.013 (noise 0.045) |
| reversal_k3_next | 0.575 (146) | 0.594 (930) [0.564, 0.621] | 0.599 (2715) [0.587, 0.613] | 0.590 (7357) [0.581, 0.598] | 0.591 (4917) [0.580, 0.601] | 0.643 (42) | 0.294 | flat -0.019 (noise 0.031) |
| reversal_k3_now | 0.901 (71) | 0.930 (417) [0.913, 0.950] | 0.931 (1746) [0.922, 0.940] | 0.935 (4815) [0.929, 0.940] | 0.931 (3052) [0.924, 0.938] | 1.000 (21) | 0.294 | flat -0.003 (noise 0.018) |
| reversal_k5_next | 0.527 (74) | 0.508 (358) [0.457, 0.570] | 0.512 (1762) [0.492, 0.533] | 0.486 (6205) [0.476, 0.498] | 0.483 (4215) [0.469, 0.498] | 0.385 (13) | 0.187 | flat +0.032 (noise 0.049) |
| reversal_k5_now | 0.829 (70) | 0.816 (423) [0.794, 0.834] | 0.796 (1784) [0.779, 0.811] | 0.817 (4604) [0.807, 0.826] | 0.805 (2993) [0.794, 0.816] | 0.769 (26) | 0.187 | up +0.070 (noise 0.028) |
| reversal_k8_next | 0.520 (75) | 0.432 (567) [0.397, 0.472] | 0.420 (2234) [0.403, 0.438] | 0.400 (6540) [0.389, 0.409] | 0.401 (4434) [0.390, 0.414] | 0.348 (23) | 0.121 | flat +0.025 (noise 0.035) |
| reversal_k8_now | 0.765 (68) | 0.686 (430) [0.658, 0.714] | 0.681 (1666) [0.662, 0.700] | 0.694 (4453) [0.682, 0.706] | 0.683 (2866) [0.669, 0.698] | 0.750 (20) | 0.122 | flat +0.043 (noise 0.033) |
| overall | 0.507 (22246) | 0.507 (155303) [0.505, 0.510] | 0.506 (661753) [0.505, 0.507] | 0.504 (1853238) [0.504, 0.505] | 0.505 (1169957) [0.504, 0.506] | 0.508 (8380) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07957, 0.1153] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5367, 'levels': [{'threshold': 0.07957, 'calls_per_day': 147.6, 'win_rate': 0.5796}, {'threshold': 0.1153, 'calls_per_day': 37.9, 'win_rate': 0.5827}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42902, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15063 | 0.351 | 0.532 (14849) | 0.557 (2081) | 0.748 (2513) |
| volatility: normal | 15062 | 0.380 | 0.528 (15006) | 0.577 (1524) | 0.748 (2457) |
| volatility: wild | 15063 | 0.391 | 0.532 (15025) | 0.584 (1173) | 0.758 (2130) |
| session: Asia 00-08 | 15360 | 0.373 | 0.532 (15249) | 0.560 (1705) | 0.748 (2331) |
| session: Europe 08-13 | 9368 | 0.367 | 0.530 (9293) | 0.576 (1162) | 0.763 (1479) |
| session: US 13-21 | 14880 | 0.381 | 0.535 (14790) | 0.600 (1316) | 0.744 (2431) |
| session: late 21-24 | 5580 | 0.368 | 0.519 (5548) | 0.524 (595) | 0.758 (859) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.384 | 0.376 | 0.288 | 0.288 | 0.533 | 0.238 | 0.531 | 1.666 |
| 6h | 360 | 0.390 | 0.381 | 0.295 | 0.347 | 0.542 | 0.272 | 0.508 | 1.194 |
| 24h | 1440 | 0.393 | 0.386 | 0.298 | 0.343 | 0.531 | 0.269 | 0.518 | 1.203 |
| 7d | 10080 | 0.387 | 0.380 | 0.296 | 0.331 | 0.536 | 0.269 | 0.505 | 1.195 |
| 30d | 43200 | 0.374 | 0.368 | 0.288 | 0.320 | 0.531 | 0.266 | 0.483 | 1.267 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.384 / 0.533 / 0.933; 2: 0.371 / 0.533 / 0.917; 3: 0.400 / 0.533 / 0.900; 4: 0.388 / 0.533 / 1.000; 5: 0.377 / 0.550 / 0.833; 6: 0.383 / 0.600 / 0.833; 7: 0.377 / 0.517 / 0.900; 8: 0.382 / 0.467 / 0.983; 9: 0.386 / 0.567 / 0.833; 10: 0.374 / 0.500 / 1.000; 11: 0.374 / 0.467 / 0.833; 12: 0.372 / 0.567 / 0.850; 13: 0.393 / 0.550 / 0.900; 14: 0.367 / 0.417 / 1.000; 15: 0.368 / 0.483 / 0.967
- 6h: 1: 0.390 / 0.542 / 0.906; 2: 0.373 / 0.486 / 0.814; 3: 0.379 / 0.522 / 0.775; 4: 0.376 / 0.525 / 0.989; 5: 0.374 / 0.525 / 0.753; 6: 0.357 / 0.466 / 0.775; 7: 0.369 / 0.520 / 0.894; 8: 0.371 / 0.522 / 0.961; 9: 0.362 / 0.475 / 0.711; 10: 0.369 / 0.508 / 0.964; 11: 0.366 / 0.494 / 0.694; 12: 0.369 / 0.547 / 0.700; 13: 0.372 / 0.522 / 0.786; 14: 0.359 / 0.478 / 0.969; 15: 0.363 / 0.480 / 0.908
- 24h: 1: 0.393 / 0.531 / 0.897; 2: 0.377 / 0.482 / 0.874; 3: 0.383 / 0.515 / 0.875; 4: 0.381 / 0.506 / 0.906; 5: 0.376 / 0.490 / 0.870; 6: 0.375 / 0.490 / 0.877; 7: 0.378 / 0.510 / 0.908; 8: 0.375 / 0.508 / 0.912; 9: 0.375 / 0.487 / 0.871; 10: 0.379 / 0.520 / 0.922; 11: 0.377 / 0.494 / 0.868; 12: 0.377 / 0.515 / 0.872; 13: 0.373 / 0.489 / 0.888; 14: 0.372 / 0.481 / 0.921; 15: 0.378 / 0.508 / 0.915
- 7d: 1: 0.387 / 0.536 / 0.900; 2: 0.372 / 0.492 / 0.896; 3: 0.373 / 0.504 / 0.895; 4: 0.371 / 0.497 / 0.901; 5: 0.375 / 0.509 / 0.897; 6: 0.369 / 0.496 / 0.896; 7: 0.370 / 0.503 / 0.904; 8: 0.371 / 0.512 / 0.905; 9: 0.368 / 0.498 / 0.898; 10: 0.370 / 0.515 / 0.903; 11: 0.369 / 0.505 / 0.897; 12: 0.369 / 0.505 / 0.898; 13: 0.366 / 0.495 / 0.900; 14: 0.366 / 0.500 / 0.904; 15: 0.366 / 0.500 / 0.904
- 30d: 1: 0.374 / 0.531 / 0.898; 2: 0.361 / 0.491 / 0.899; 3: 0.365 / 0.511 / 0.899; 4: 0.361 / 0.497 / 0.900; 5: 0.362 / 0.506 / 0.899; 6: 0.359 / 0.501 / 0.899; 7: 0.361 / 0.501 / 0.900; 8: 0.361 / 0.507 / 0.901; 9: 0.359 / 0.501 / 0.899; 10: 0.360 / 0.505 / 0.901; 11: 0.359 / 0.505 / 0.899; 12: 0.359 / 0.503 / 0.899; 13: 0.358 / 0.499 / 0.900; 14: 0.358 / 0.502 / 0.901; 15: 0.358 / 0.501 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.082 (body 0.039, range 0.125); 'price stays where it was' would score 0.135; colour right 0.550; typical miss of the close 21.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.113 (body 0.070, range 0.157); 'price stays where it was' would score 0.117; colour right 0.478; typical miss of the close 15.3 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.134 (body 0.082, range 0.187); 'price stays where it was' would score 0.138; colour right 0.497; typical miss of the close 13.9 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.137 (body 0.088, range 0.186); 'price stays where it was' would score 0.142; colour right 0.503; typical miss of the close 13.7 bp; chain ended on the right side 0.512 of 672 chains; n=10080
- 30d: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.8 bp; chain ended on the right side 0.512 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 5.8; 2: 0.208 / 6.6; 3: 0.167 / 8.5; 4: 0.137 / 8.9; 5: 0.125 / 9.7; 6: 0.117 / 10.7; 7: 0.116 / 11.0; 8: 0.101 / 11.8; 9: 0.093 / 12.6; 10: 0.089 / 13.0; 11: 0.088 / 13.5; 12: 0.083 / 13.6; 13: 0.076 / 14.5; 14: 0.070 / 14.9; 15: 0.068 / 15.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 164462, probability skill vs chance 0.2277, widened contest next: False
  - now: threshold 0.8314, hit rate recent 0.9341 / long run 0.9315
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.317, naive rule 0.555, lift 3.16x
    - 24h: 67 calls (67 a day), hit rate 0.925, chance 0.294, naive rule 0.501, lift 3.15x
    - 7d: 418 calls (60 a day), hit rate 0.931, chance 0.300, naive rule 0.522, lift 3.10x
    - 30d: 1749 calls (58 a day), hit rate 0.931, chance 0.294, naive rule 0.504, lift 3.17x
  - next: threshold 0.5255, hit rate recent 0.6339 / long run 0.5981
    - 6h: 29 calls (118 a day), hit rate 0.759, chance 0.317, lift 2.39x
    - 24h: 120 calls (120 a day), hit rate 0.617, chance 0.294, lift 2.10x
    - 7d: 946 calls (135 a day), hit rate 0.595, chance 0.300, lift 1.98x
    - 30d: 2716 calls (91 a day), hit rate 0.600, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.503; 0.35: 530, 0.528; 0.40: 481, 0.572; 0.45: 418, 0.636; 0.50: 367, 0.682; 0.55: 320, 0.727; 0.60: 270, 0.773; 0.65: 227, 0.803; 0.70: 178, 0.835; 0.75: 143, 0.870; 0.80: 95, 0.902; 0.85: 43, 0.942; 0.90: 3, 0.961
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 486, 0.470; 0.40: 384, 0.511; 0.45: 290, 0.542; 0.50: 185, 0.572; 0.55: 77, 0.588; 0.60: 10, 0.635; 0.65: 0, 0.538
- **K=5**: model 1794528000, labels learned 164460, probability skill vs chance 0.2202, widened contest next: False
  - now: threshold 0.7019, hit rate recent 0.8155 / long run 0.7976
    - 6h: 16 calls (65 a day), hit rate 0.875, chance 0.203, naive rule 0.449, lift 4.32x
    - 24h: 68 calls (68 a day), hit rate 0.824, chance 0.195, naive rule 0.432, lift 4.21x
    - 7d: 428 calls (61 a day), hit rate 0.813, chance 0.196, naive rule 0.436, lift 4.16x
    - 30d: 1791 calls (60 a day), hit rate 0.794, chance 0.189, naive rule 0.416, lift 4.21x
  - next: threshold 0.455, hit rate recent 0.5026 / long run 0.5006
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.203, lift 2.19x
    - 24h: 44 calls (44 a day), hit rate 0.523, chance 0.195, lift 2.68x
    - 7d: 347 calls (50 a day), hit rate 0.507, chance 0.196, lift 2.59x
    - 30d: 1731 calls (58 a day), hit rate 0.511, chance 0.189, lift 2.71x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.426; 0.35: 364, 0.475; 0.40: 295, 0.543; 0.45: 239, 0.603; 0.50: 187, 0.653; 0.55: 150, 0.685; 0.60: 116, 0.730; 0.65: 84, 0.767; 0.70: 53, 0.802; 0.75: 27, 0.836; 0.80: 6, 0.848
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 331, 0.396; 0.35: 246, 0.434; 0.40: 156, 0.461; 0.45: 62, 0.509; 0.50: 8, 0.563; 0.55: 1, 0.500
- **K=8**: model 1794960000, labels learned 164457, probability skill vs chance 0.226, widened contest next: False
  - now: threshold 0.5868, hit rate recent 0.7505 / long run 0.6815
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.121, naive rule 0.328, lift 6.74x
    - 24h: 63 calls (63 a day), hit rate 0.778, chance 0.131, naive rule 0.374, lift 5.92x
    - 7d: 426 calls (61 a day), hit rate 0.688, chance 0.126, naive rule 0.365, lift 5.47x
    - 30d: 1668 calls (56 a day), hit rate 0.682, chance 0.123, naive rule 0.350, lift 5.53x
  - next: threshold 0.3607, hit rate recent 0.4438 / long run 0.4245
    - 6h: 16 calls (66 a day), hit rate 0.438, chance 0.121, lift 3.60x
    - 24h: 73 calls (74 a day), hit rate 0.452, chance 0.131, lift 3.44x
    - 7d: 556 calls (80 a day), hit rate 0.432, chance 0.126, lift 3.43x
    - 30d: 2217 calls (74 a day), hit rate 0.420, chance 0.123, lift 3.40x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 257, 0.427; 0.35: 203, 0.486; 0.40: 159, 0.536; 0.45: 121, 0.579; 0.50: 87, 0.635; 0.55: 63, 0.671; 0.60: 43, 0.712; 0.65: 24, 0.766; 0.70: 10, 0.810; 0.75: 1, 0.737
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.376; 0.35: 83, 0.410; 0.40: 28, 0.445; 0.45: 6, 0.478; 0.50: 1, 0.667
- **K=13**: model 1795478400, labels learned 164452, probability skill vs chance 0.2116, widened contest next: False
  - now: threshold 0.4609, hit rate recent 0.6486 / long run 0.5844
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.100, naive rule 0.375, lift 7.14x
    - 24h: 49 calls (50 a day), hit rate 0.714, chance 0.092, naive rule 0.349, lift 7.74x
    - 7d: 368 calls (53 a day), hit rate 0.592, chance 0.083, naive rule 0.321, lift 7.11x
    - 30d: 1612 calls (54 a day), hit rate 0.578, chance 0.080, naive rule 0.299, lift 7.21x
  - next: threshold 0.3027, hit rate recent 0.3806 / long run 0.3448
    - 6h: 18 calls (75 a day), hit rate 0.333, chance 0.100, lift 3.33x
    - 24h: 61 calls (62 a day), hit rate 0.361, chance 0.092, lift 3.91x
    - 7d: 416 calls (60 a day), hit rate 0.363, chance 0.083, lift 4.35x
    - 30d: 1815 calls (61 a day), hit rate 0.339, chance 0.080, lift 4.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 142, 0.425; 0.35: 104, 0.473; 0.40: 72, 0.537; 0.45: 51, 0.585; 0.50: 35, 0.621; 0.55: 21, 0.645; 0.60: 10, 0.674; 0.65: 2, 0.532
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.345; 0.35: 15, 0.387; 0.40: 2, 0.451; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 23.758 | 0.08% | 0.917 | 0.550 | 0.249 | 0.500 | 0.272 |
| 6h | 20.981 | 0.49% | 0.903 | 0.522 | 0.250 | 0.508 | 0.384 |
| 24h | 23.364 | 2.68% | 0.901 | 0.507 | 0.250 | 0.512 | 0.575 |
| 7d | 24.848 | 4.24% | 0.899 | 0.501 | 0.250 | 0.511 | 0.660 |
| 30d | 19.778 | 4.74% | 0.900 | 0.500 | 0.250 | 0.506 | 0.707 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 23.778 | 24.290 | 24.132 | 23.829 | 24.170 | 24.128 | 23.623 | 23.388 | 23.605 | 23.758 |
| 6h | 21.085 | 21.233 | 21.297 | 20.938 | 21.658 | 21.255 | 20.932 | 20.841 | 20.918 | 20.981 |
| 24h | 24.008 | 23.544 | 23.525 | 23.446 | 23.984 | 23.662 | 23.276 | 23.241 | 23.308 | 23.364 |
| 7d | 25.948 | 25.122 | 25.024 | 24.876 | 25.420 | 25.176 | 24.834 | 24.784 | 24.812 | 24.848 |
| 30d | 20.762 | 19.966 | 19.915 | 19.833 | 20.194 | 20.104 | 19.759 | 19.732 | 19.744 | 19.778 |

## Next candle

- candle starting 2026-11-25 09:08 UTC, last close 1646.6
- P(up) 0.5091, return quantiles (bp): {'05': -15.696, '10': -11.81, '25': -5.47, '40': -2.183, '50': 0.216, '60': 1.946, '75': 4.994, '90': 10.827, '95': 14.479}
- changepoint probability 0.0967, regime age 75.7 min
- agent weights: empirical 0.025, ewma 0.053, garch 0.052, har 0.159, bocpd 0.009, hmm 0.047, online_qr 0.293, lgbm 0.361

## Learning log

- 2026-11-23 00:00 UTC: {"garch": {"alpha": 0.0752, "beta": 0.917}, "hmm": {"sd_bp": [5.28, 10.22, 28.39], "stay": [0.976, 0.946, 0.857]}, "lgbm": {"challenger_loss": 0.24364, "champion_loss": 0.24354, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.61601, "widened": false, "champion_loss": 0.4869, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38212, "challengers": 1, "chance_loss": 0.503, "widened": false, "champion_loss": 0.38113, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29091, "challengers": 1, "chance_loss": 0.3912, "widened": false, "champion_loss": 0.28935, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20987, "challengers": 1, "chance_loss": 0.29233, "widened": false, "champion_loss": 0.20927, "promoted": false}}
- 2026-11-23 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.9112}, "hmm": {"sd_bp": [5.07, 10.1, 28.28], "stay": [0.973, 0.946, 0.862]}}
- 2026-11-24 00:00 UTC: {"garch": {"alpha": 0.0886, "beta": 0.9021}, "hmm": {"sd_bp": [4.97, 10.02, 31.47], "stay": [0.968, 0.952, 0.875]}, "lgbm": {"challenger_loss": 0.25051, "champion_loss": 0.25047, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48498, "challengers": 3, "chance_loss": 0.6173, "widened": true, "champion_loss": 0.48458, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37971, "challengers": 1, "chance_loss": 0.49915, "widened": false, "champion_loss": 0.37928, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27848, "challengers": 3, "chance_loss": 0.37338, "widened": true, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20281, "challengers": 3, "chance_loss": 0.28057, "widened": true, "champion_loss": 0.20335, "promoted": true}}
- 2026-11-24 12:00 UTC: {"garch": {"alpha": 0.0937, "beta": 0.8962}, "hmm": {"sd_bp": [5.06, 10.1, 31.41], "stay": [0.968, 0.948, 0.887]}}
- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.92, 10.11, 34.59], current probabilities: [0.705, 0.292, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-11-25 09:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.363, 'l_abs': 0.653, 'l_hi': 0.785, 'l_lo': 0.693, 'b05': 0.691, 'b25': 0.665, 'b75': 0.556, 'b95': 0.647}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [3.396, 4.891, 1.774, 6.598, 5.584, 2.408, 2.029, 8.237, 2.371, 10.517, 9.568, 5.933, 2.717, 2.992]}
- calibration offsets (in sigma): {'05': -0.0565, '10': -0.023, '25': 0.0475, '40': 0.028, '50': 0.025, '60': 0.002, '75': -0.0375, '90': -0.037, '95': -0.0635}
