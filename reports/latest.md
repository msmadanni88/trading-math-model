# ETH-USD 60s candle generator - report

- generated: 2026-11-25 00:35 UTC
- last closed candle: 2026-11-25 00:35 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.515 (672) [0.492, 0.540] | 0.512 (2879) [0.496, 0.526] | 0.515 (8057) [0.505, 0.526] | 0.517 (5085) [0.503, 0.531] | 0.000 (2) | 0.500 | flat -0.017 (noise 0.027) |
| colour_clear | 0.546 (804) | 0.554 (5524) [0.542, 0.567] | 0.542 (23825) [0.536, 0.548] | 0.526 (66118) [0.521, 0.532] | 0.544 (41880) [0.540, 0.548] | 0.474 (19) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.532 (188) | 0.579 (1325) [0.561, 0.593] | 0.570 (4442) [0.559, 0.580] | 0.584 (7903) [0.575, 0.593] | 0.584 (7903) [0.575, 0.593] | 0.545 (11) | 0.500 | flat +0.042 (noise 0.021) |
| colour_next | 0.528 (1436) | 0.536 (10047) [0.529, 0.543] | 0.531 (42902) [0.527, 0.535] | 0.519 (120092) [0.516, 0.523] | 0.530 (75743) [0.527, 0.534] | 0.543 (35) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140658) [0.500, 0.505] | 0.502 (600628) [0.501, 0.503] | 0.501 (1681288) [0.500, 0.502] | 0.501 (1060402) [0.500, 0.502] | 0.490 (490) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.452 (62) | 0.598 (395) [0.542, 0.641] | 0.602 (1177) [0.580, 0.621] | 0.618 (2118) [0.602, 0.633] | 0.618 (2118) [0.602, 0.633] | 0.000 (2) | 0.500 | flat +0.035 (noise 0.042) |
| reversal_k13_next | 0.431 (51) | 0.361 (427) [0.321, 0.407] | 0.339 (1812) [0.320, 0.359] | 0.318 (5496) [0.308, 0.328] | 0.329 (3391) [0.318, 0.341] | 0.500 (2) | 0.078 | flat +0.046 (noise 0.037) |
| reversal_k13_now | 0.727 (55) | 0.588 (374) [0.543, 0.640] | 0.577 (1625) [0.554, 0.599] | 0.575 (4331) [0.563, 0.588] | 0.572 (2859) [0.555, 0.588] | 0.500 (2) | 0.078 | flat +0.013 (noise 0.045) |
| reversal_k3_next | 0.575 (146) | 0.594 (930) [0.564, 0.621] | 0.599 (2715) [0.587, 0.613] | 0.590 (7357) [0.581, 0.598] | 0.591 (4917) [0.580, 0.601] | 0.500 (2) | 0.294 | flat -0.019 (noise 0.031) |
| reversal_k3_now | 0.901 (71) | 0.930 (417) [0.913, 0.950] | 0.931 (1746) [0.922, 0.940] | 0.935 (4815) [0.929, 0.940] | 0.931 (3052) [0.924, 0.938] | 1.000 (1) | 0.294 | flat -0.003 (noise 0.018) |
| reversal_k5_next | 0.527 (74) | 0.508 (358) [0.457, 0.570] | 0.512 (1762) [0.492, 0.533] | 0.486 (6205) [0.476, 0.498] | 0.483 (4215) [0.469, 0.498] | 0.000 (1) | 0.187 | flat +0.032 (noise 0.049) |
| reversal_k5_now | 0.829 (70) | 0.816 (423) [0.794, 0.834] | 0.796 (1784) [0.779, 0.811] | 0.817 (4604) [0.807, 0.826] | 0.805 (2993) [0.794, 0.816] | 0.500 (2) | 0.187 | up +0.070 (noise 0.028) |
| reversal_k8_next | 0.520 (75) | 0.432 (567) [0.397, 0.472] | 0.420 (2234) [0.403, 0.438] | 0.400 (6540) [0.389, 0.409] | 0.401 (4434) [0.390, 0.414] | 0.000 (1) | 0.121 | flat +0.025 (noise 0.035) |
| reversal_k8_now | 0.765 (68) | 0.686 (430) [0.658, 0.714] | 0.681 (1666) [0.662, 0.700] | 0.694 (4453) [0.682, 0.706] | 0.683 (2866) [0.669, 0.698] | 0.500 (2) | 0.122 | flat +0.043 (noise 0.033) |
| overall | 0.507 (22246) | 0.507 (155303) [0.505, 0.510] | 0.506 (661753) [0.505, 0.507] | 0.504 (1853238) [0.504, 0.505] | 0.505 (1169957) [0.504, 0.506] | 0.491 (540) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0789, 0.1141] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5364, 'levels': [{'threshold': 0.0789, 'calls_per_day': 147.1, 'win_rate': 0.5799}, {'threshold': 0.1141, 'calls_per_day': 37.6, 'win_rate': 0.5909}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42901, 'rate': 0.531}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14892 | 0.350 | 0.532 (14678) | 0.557 (2069) | 0.750 (2484) |
| volatility: normal | 14891 | 0.380 | 0.528 (14836) | 0.577 (1491) | 0.745 (2452) |
| volatility: wild | 14892 | 0.391 | 0.532 (14857) | 0.586 (1161) | 0.756 (2090) |
| session: Asia 00-08 | 14915 | 0.372 | 0.531 (14808) | 0.558 (1651) | 0.746 (2264) |
| session: Europe 08-13 | 9300 | 0.367 | 0.530 (9225) | 0.577 (1159) | 0.762 (1472) |
| session: US 13-21 | 14880 | 0.381 | 0.535 (14790) | 0.600 (1316) | 0.744 (2431) |
| session: late 21-24 | 5580 | 0.368 | 0.519 (5548) | 0.524 (595) | 0.758 (859) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.388 | 0.379 | 0.281 | 0.281 | 0.550 | 0.247 | 0.528 | 1.207 |
| 6h | 360 | 0.388 | 0.378 | 0.293 | 0.340 | 0.534 | 0.258 | 0.519 | 1.245 |
| 24h | 1440 | 0.391 | 0.384 | 0.296 | 0.337 | 0.528 | 0.269 | 0.514 | 1.210 |
| 7d | 10080 | 0.387 | 0.380 | 0.297 | 0.332 | 0.536 | 0.269 | 0.505 | 1.198 |
| 30d | 43200 | 0.374 | 0.368 | 0.288 | 0.320 | 0.531 | 0.266 | 0.483 | 1.266 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.388 / 0.550 / 0.883; 2: 0.370 / 0.467 / 0.917; 3: 0.356 / 0.400 / 1.000; 4: 0.352 / 0.367 / 0.717; 5: 0.350 / 0.433 / 0.983; 6: 0.375 / 0.550 / 0.983; 7: 0.359 / 0.450 / 0.800; 8: 0.374 / 0.533 / 0.767; 9: 0.355 / 0.483 / 0.883; 10: 0.360 / 0.517 / 1.000; 11: 0.373 / 0.583 / 0.950; 12: 0.377 / 0.517 / 0.967; 13: 0.379 / 0.533 / 1.000; 14: 0.374 / 0.483 / 1.000; 15: 0.390 / 0.550 / 1.000
- 6h: 1: 0.388 / 0.534 / 0.903; 2: 0.380 / 0.492 / 0.944; 3: 0.380 / 0.506 / 1.000; 4: 0.370 / 0.453 / 0.778; 5: 0.373 / 0.486 / 0.986; 6: 0.381 / 0.520 / 0.981; 7: 0.379 / 0.494 / 0.872; 8: 0.373 / 0.494 / 0.814; 9: 0.379 / 0.508 / 0.956; 10: 0.381 / 0.525 / 1.000; 11: 0.383 / 0.520 / 0.992; 12: 0.380 / 0.497 / 0.992; 13: 0.377 / 0.494 / 0.997; 14: 0.377 / 0.480 / 1.000; 15: 0.375 / 0.492 / 1.000
- 24h: 1: 0.391 / 0.528 / 0.891; 2: 0.379 / 0.494 / 0.917; 3: 0.382 / 0.510 / 0.918; 4: 0.379 / 0.499 / 0.901; 5: 0.376 / 0.497 / 0.919; 6: 0.380 / 0.517 / 0.920; 7: 0.377 / 0.503 / 0.901; 8: 0.379 / 0.522 / 0.888; 9: 0.374 / 0.492 / 0.915; 10: 0.380 / 0.526 / 0.886; 11: 0.378 / 0.497 / 0.928; 12: 0.376 / 0.495 / 0.930; 13: 0.368 / 0.467 / 0.919; 14: 0.374 / 0.490 / 0.889; 15: 0.375 / 0.501 / 0.908
- 7d: 1: 0.387 / 0.536 / 0.900; 2: 0.373 / 0.493 / 0.903; 3: 0.373 / 0.504 / 0.904; 4: 0.371 / 0.496 / 0.898; 5: 0.375 / 0.508 / 0.902; 6: 0.370 / 0.499 / 0.905; 7: 0.370 / 0.503 / 0.900; 8: 0.372 / 0.513 / 0.899; 9: 0.369 / 0.500 / 0.902; 10: 0.371 / 0.514 / 0.900; 11: 0.370 / 0.505 / 0.904; 12: 0.370 / 0.503 / 0.903; 13: 0.366 / 0.494 / 0.900; 14: 0.367 / 0.501 / 0.897; 15: 0.366 / 0.500 / 0.900
- 30d: 1: 0.374 / 0.531 / 0.898; 2: 0.361 / 0.491 / 0.900; 3: 0.365 / 0.511 / 0.900; 4: 0.361 / 0.496 / 0.899; 5: 0.363 / 0.506 / 0.900; 6: 0.360 / 0.502 / 0.901; 7: 0.361 / 0.501 / 0.900; 8: 0.361 / 0.507 / 0.900; 9: 0.359 / 0.501 / 0.901; 10: 0.360 / 0.505 / 0.900; 11: 0.359 / 0.505 / 0.901; 12: 0.359 / 0.503 / 0.901; 13: 0.358 / 0.499 / 0.900; 14: 0.358 / 0.502 / 0.900; 15: 0.358 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.101 (body 0.060, range 0.143); 'price stays where it was' would score 0.125; colour right 0.417; typical miss of the close 13.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.148 (body 0.088, range 0.209); 'price stays where it was' would score 0.146; colour right 0.497; typical miss of the close 8.8 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.138 (body 0.086, range 0.189); 'price stays where it was' would score 0.139; colour right 0.492; typical miss of the close 14.2 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.136 (body 0.088, range 0.185); 'price stays where it was' would score 0.141; colour right 0.502; typical miss of the close 13.6 bp; chain ended on the right side 0.513 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.170); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.8 bp; chain ended on the right side 0.512 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 5.8; 2: 0.208 / 6.5; 3: 0.168 / 8.5; 4: 0.137 / 8.9; 5: 0.126 / 9.6; 6: 0.119 / 10.5; 7: 0.117 / 11.0; 8: 0.101 / 11.9; 9: 0.092 / 12.6; 10: 0.089 / 12.9; 11: 0.088 / 13.4; 12: 0.083 / 13.6; 13: 0.075 / 14.5; 14: 0.070 / 14.9; 15: 0.068 / 15.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 163949, probability skill vs chance 0.2197, widened contest next: False
  - now: threshold 0.831, hit rate recent 0.9078 / long run 0.9292
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.276, naive rule 0.477, lift 3.20x
    - 24h: 70 calls (70 a day), hit rate 0.900, chance 0.298, naive rule 0.501, lift 3.02x
    - 7d: 418 calls (60 a day), hit rate 0.931, chance 0.299, naive rule 0.519, lift 3.11x
    - 30d: 1746 calls (58 a day), hit rate 0.931, chance 0.294, naive rule 0.503, lift 3.17x
  - next: threshold 0.5261, hit rate recent 0.592 / long run 0.5944
    - 6h: 24 calls (97 a day), hit rate 0.583, chance 0.276, lift 2.11x
    - 24h: 144 calls (145 a day), hit rate 0.583, chance 0.298, lift 1.96x
    - 7d: 929 calls (133 a day), hit rate 0.592, chance 0.299, lift 1.98x
    - 30d: 2716 calls (91 a day), hit rate 0.599, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.503; 0.35: 530, 0.527; 0.40: 480, 0.572; 0.45: 417, 0.636; 0.50: 367, 0.682; 0.55: 319, 0.727; 0.60: 269, 0.773; 0.65: 226, 0.804; 0.70: 178, 0.835; 0.75: 143, 0.870; 0.80: 95, 0.901; 0.85: 43, 0.942; 0.90: 4, 0.962
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 487, 0.470; 0.40: 384, 0.510; 0.45: 290, 0.542; 0.50: 186, 0.572; 0.55: 78, 0.588; 0.60: 10, 0.634; 0.65: 0, 0.538
- **K=5**: model 1794528000, labels learned 163947, probability skill vs chance 0.2171, widened contest next: False
  - now: threshold 0.7014, hit rate recent 0.8217 / long run 0.7978
    - 6h: 18 calls (73 a day), hit rate 0.833, chance 0.198, naive rule 0.446, lift 4.20x
    - 24h: 70 calls (70 a day), hit rate 0.829, chance 0.185, naive rule 0.410, lift 4.47x
    - 7d: 424 calls (61 a day), hit rate 0.814, chance 0.195, naive rule 0.431, lift 4.18x
    - 30d: 1785 calls (60 a day), hit rate 0.796, chance 0.188, naive rule 0.415, lift 4.22x
  - next: threshold 0.455, hit rate recent 0.5209 / long run 0.5023
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.198, lift 3.15x
    - 24h: 71 calls (71 a day), hit rate 0.521, chance 0.185, lift 2.81x
    - 7d: 356 calls (51 a day), hit rate 0.508, chance 0.195, lift 2.61x
    - 30d: 1762 calls (59 a day), hit rate 0.512, chance 0.188, lift 2.72x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.425; 0.35: 364, 0.474; 0.40: 295, 0.542; 0.45: 239, 0.603; 0.50: 186, 0.654; 0.55: 150, 0.686; 0.60: 116, 0.730; 0.65: 84, 0.767; 0.70: 53, 0.803; 0.75: 27, 0.839; 0.80: 6, 0.853
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 332, 0.396; 0.35: 246, 0.434; 0.40: 157, 0.461; 0.45: 62, 0.510; 0.50: 8, 0.564; 0.55: 1, 0.471
- **K=8**: model 1794960000, labels learned 163944, probability skill vs chance 0.2211, widened contest next: False
  - now: threshold 0.586, hit rate recent 0.7382 / long run 0.6785
    - 6h: 17 calls (70 a day), hit rate 0.882, chance 0.126, naive rule 0.375, lift 7.02x
    - 24h: 67 calls (67 a day), hit rate 0.776, chance 0.130, naive rule 0.371, lift 5.95x
    - 7d: 431 calls (62 a day), hit rate 0.684, chance 0.125, naive rule 0.363, lift 5.46x
    - 30d: 1667 calls (56 a day), hit rate 0.681, chance 0.123, naive rule 0.349, lift 5.52x
  - next: threshold 0.3738, hit rate recent 0.4733 / long run 0.4267
    - 6h: 22 calls (91 a day), hit rate 0.455, chance 0.126, lift 3.62x
    - 24h: 74 calls (75 a day), hit rate 0.500, chance 0.130, lift 3.83x
    - 7d: 566 calls (81 a day), hit rate 0.433, chance 0.125, lift 3.45x
    - 30d: 2234 calls (74 a day), hit rate 0.420, chance 0.123, lift 3.40x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 257, 0.427; 0.35: 203, 0.486; 0.40: 159, 0.536; 0.45: 121, 0.578; 0.50: 87, 0.634; 0.55: 63, 0.670; 0.60: 42, 0.712; 0.65: 24, 0.770; 0.70: 10, 0.810; 0.75: 1, 0.737
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.376; 0.35: 83, 0.409; 0.40: 28, 0.448; 0.45: 6, 0.476; 0.50: 1, 0.656
- **K=13**: model 1795478400, labels learned 163939, probability skill vs chance 0.2056, widened contest next: False
  - now: threshold 0.4605, hit rate recent 0.6439 / long run 0.5827
    - 6h: 16 calls (67 a day), hit rate 0.562, chance 0.083, naive rule 0.279, lift 6.81x
    - 24h: 56 calls (57 a day), hit rate 0.714, chance 0.086, naive rule 0.321, lift 8.28x
    - 7d: 376 calls (54 a day), hit rate 0.588, chance 0.083, naive rule 0.316, lift 7.09x
    - 30d: 1626 calls (54 a day), hit rate 0.576, chance 0.080, naive rule 0.298, lift 7.20x
  - next: threshold 0.3031, hit rate recent 0.4138 / long run 0.3464
    - 6h: 16 calls (67 a day), hit rate 0.375, chance 0.083, lift 4.54x
    - 24h: 52 calls (53 a day), hit rate 0.442, chance 0.086, lift 5.12x
    - 7d: 426 calls (61 a day), hit rate 0.364, chance 0.083, lift 4.39x
    - 30d: 1814 calls (60 a day), hit rate 0.339, chance 0.080, lift 4.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 142, 0.424; 0.35: 104, 0.472; 0.40: 72, 0.535; 0.45: 51, 0.586; 0.50: 35, 0.622; 0.55: 21, 0.648; 0.60: 10, 0.675; 0.65: 2, 0.525
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.344; 0.35: 15, 0.388; 0.40: 2, 0.451

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 17.205 | 4.27% | 0.900 | 0.567 | 0.249 | 0.517 | 0.423 |
| 6h | 15.522 | 5.83% | 0.908 | 0.542 | 0.250 | 0.497 | 0.441 |
| 24h | 23.589 | 2.83% | 0.901 | 0.495 | 0.250 | 0.507 | 0.614 |
| 7d | 24.500 | 4.38% | 0.900 | 0.500 | 0.250 | 0.510 | 0.669 |
| 30d | 19.750 | 4.80% | 0.900 | 0.500 | 0.250 | 0.506 | 0.709 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.972 | 17.437 | 17.347 | 17.147 | 17.772 | 17.599 | 17.030 | 17.274 | 17.200 | 17.205 |
| 6h | 16.482 | 15.573 | 15.575 | 15.573 | 15.828 | 15.808 | 15.464 | 15.478 | 15.496 | 15.522 |
| 24h | 24.276 | 23.691 | 23.645 | 23.659 | 24.068 | 23.900 | 23.529 | 23.478 | 23.527 | 23.589 |
| 7d | 25.622 | 24.764 | 24.666 | 24.525 | 25.050 | 24.824 | 24.488 | 24.441 | 24.465 | 24.500 |
| 30d | 20.744 | 19.935 | 19.887 | 19.805 | 20.160 | 20.079 | 19.732 | 19.706 | 19.717 | 19.750 |

## Next candle

- candle starting 2026-11-25 00:35 UTC, last close 1669.4
- P(up) 0.4905, return quantiles (bp): {'05': -11.848, '10': -8.704, '25': -4.535, '40': -1.561, '50': -0.146, '60': 1.416, '75': 3.933, '90': 8.555, '95': 10.861}
- changepoint probability 0.074, regime age 30.0 min
- agent weights: empirical 0.004, ewma 0.105, garch 0.130, har 0.140, bocpd 0.019, hmm 0.043, online_qr 0.276, lgbm 0.283

## Learning log

- 2026-11-23 00:00 UTC: {"garch": {"alpha": 0.0752, "beta": 0.917}, "hmm": {"sd_bp": [5.28, 10.22, 28.39], "stay": [0.976, 0.946, 0.857]}, "lgbm": {"challenger_loss": 0.24364, "champion_loss": 0.24354, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.61601, "widened": false, "champion_loss": 0.4869, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38212, "challengers": 1, "chance_loss": 0.503, "widened": false, "champion_loss": 0.38113, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29091, "challengers": 1, "chance_loss": 0.3912, "widened": false, "champion_loss": 0.28935, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20987, "challengers": 1, "chance_loss": 0.29233, "widened": false, "champion_loss": 0.20927, "promoted": false}}
- 2026-11-23 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.9112}, "hmm": {"sd_bp": [5.07, 10.1, 28.28], "stay": [0.973, 0.946, 0.862]}}
- 2026-11-24 00:00 UTC: {"garch": {"alpha": 0.0886, "beta": 0.9021}, "hmm": {"sd_bp": [4.97, 10.02, 31.47], "stay": [0.968, 0.952, 0.875]}, "lgbm": {"challenger_loss": 0.25051, "champion_loss": 0.25047, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48498, "challengers": 3, "chance_loss": 0.6173, "widened": true, "champion_loss": 0.48458, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37971, "challengers": 1, "chance_loss": 0.49915, "widened": false, "champion_loss": 0.37928, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27848, "challengers": 3, "chance_loss": 0.37338, "widened": true, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20281, "challengers": 3, "chance_loss": 0.28057, "widened": true, "champion_loss": 0.20335, "promoted": true}}
- 2026-11-24 12:00 UTC: {"garch": {"alpha": 0.0937, "beta": 0.8962}, "hmm": {"sd_bp": [5.06, 10.1, 31.41], "stay": [0.968, 0.948, 0.887]}}
- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.92, 10.11, 34.59], current probabilities: [0.524, 0.472, 0.004]
- live generator: {'versions': 60, 'latest_effective': '2026-11-25 00:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.331, 'l_abs': 0.697, 'l_hi': 0.806, 'l_lo': 0.724, 'b05': 0.661, 'b25': 0.686, 'b75': 0.575, 'b95': 0.662}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.071, 1.341, 4.568, 1.67, 1.87, 2.843, 4.194, 2.085, 5.1, 2.179, 2.281, 2.964, 6.083, 4.063]}
- calibration offsets (in sigma): {'05': -0.033, '10': 0.034, '25': 0.015, '40': 0.026, '50': -0.01, '60': -0.016, '75': -0.075, '90': -0.044, '95': -0.087}
