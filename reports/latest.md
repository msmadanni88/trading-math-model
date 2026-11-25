# ETH-USD 60s candle generator - report

- generated: 2026-11-25 19:13 UTC
- last closed candle: 2026-11-25 19:13 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.469 (96) | 0.515 (672) [0.492, 0.540] | 0.512 (2879) [0.496, 0.526] | 0.515 (8057) [0.505, 0.526] | 0.517 (5085) [0.503, 0.531] | 0.447 (76) | 0.500 | flat -0.017 (noise 0.027) |
| colour_clear | 0.546 (804) | 0.554 (5524) [0.542, 0.567] | 0.542 (23825) [0.536, 0.548] | 0.526 (66118) [0.521, 0.532] | 0.544 (41880) [0.540, 0.548] | 0.558 (642) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.532 (188) | 0.579 (1325) [0.561, 0.593] | 0.570 (4442) [0.559, 0.580] | 0.584 (7903) [0.575, 0.593] | 0.584 (7903) [0.575, 0.593] | 0.592 (152) | 0.500 | flat +0.042 (noise 0.021) |
| colour_next | 0.528 (1436) | 0.536 (10047) [0.529, 0.543] | 0.531 (42902) [0.527, 0.535] | 0.519 (120092) [0.516, 0.523] | 0.530 (75743) [0.527, 0.534] | 0.534 (1148) | 0.500 | flat +0.008 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140658) [0.500, 0.505] | 0.502 (600628) [0.501, 0.503] | 0.501 (1681288) [0.500, 0.502] | 0.501 (1060402) [0.500, 0.502] | 0.503 (16072) | 0.500 | flat -0.001 (noise 0.002) |
| colour_strong | 0.452 (62) | 0.598 (395) [0.542, 0.641] | 0.602 (1177) [0.580, 0.621] | 0.618 (2118) [0.602, 0.633] | 0.618 (2118) [0.602, 0.633] | 0.523 (44) | 0.500 | flat +0.035 (noise 0.042) |
| reversal_k13_next | 0.431 (51) | 0.361 (427) [0.321, 0.407] | 0.339 (1812) [0.320, 0.359] | 0.318 (5496) [0.308, 0.328] | 0.329 (3391) [0.318, 0.341] | 0.333 (57) | 0.078 | flat +0.046 (noise 0.037) |
| reversal_k13_now | 0.727 (55) | 0.588 (374) [0.543, 0.640] | 0.577 (1625) [0.554, 0.599] | 0.575 (4331) [0.563, 0.588] | 0.572 (2859) [0.555, 0.588] | 0.703 (37) | 0.078 | flat +0.013 (noise 0.045) |
| reversal_k3_next | 0.575 (146) | 0.594 (930) [0.564, 0.621] | 0.599 (2715) [0.587, 0.613] | 0.590 (7357) [0.581, 0.598] | 0.591 (4917) [0.580, 0.601] | 0.556 (108) | 0.294 | flat -0.019 (noise 0.031) |
| reversal_k3_now | 0.901 (71) | 0.930 (417) [0.913, 0.950] | 0.931 (1746) [0.922, 0.940] | 0.935 (4815) [0.929, 0.940] | 0.931 (3052) [0.924, 0.938] | 0.940 (50) | 0.294 | flat -0.003 (noise 0.018) |
| reversal_k5_next | 0.527 (74) | 0.508 (358) [0.457, 0.570] | 0.512 (1762) [0.492, 0.533] | 0.486 (6205) [0.476, 0.498] | 0.483 (4215) [0.469, 0.498] | 0.435 (46) | 0.187 | flat +0.032 (noise 0.049) |
| reversal_k5_now | 0.829 (70) | 0.816 (423) [0.794, 0.834] | 0.796 (1784) [0.779, 0.811] | 0.817 (4604) [0.807, 0.826] | 0.805 (2993) [0.794, 0.816] | 0.767 (60) | 0.187 | up +0.070 (noise 0.028) |
| reversal_k8_next | 0.520 (75) | 0.432 (567) [0.397, 0.472] | 0.420 (2234) [0.403, 0.438] | 0.400 (6540) [0.389, 0.409] | 0.401 (4434) [0.390, 0.414] | 0.317 (60) | 0.121 | flat +0.025 (noise 0.035) |
| reversal_k8_now | 0.765 (68) | 0.686 (430) [0.658, 0.714] | 0.681 (1666) [0.662, 0.700] | 0.694 (4453) [0.682, 0.706] | 0.683 (2866) [0.669, 0.698] | 0.729 (48) | 0.122 | flat +0.043 (noise 0.033) |
| overall | 0.507 (22246) | 0.507 (155303) [0.505, 0.510] | 0.506 (661753) [0.505, 0.507] | 0.504 (1853238) [0.504, 0.505] | 0.505 (1169957) [0.504, 0.506] | 0.506 (17762) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08062, 0.1171] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5342, 'levels': [{'threshold': 0.08062, 'calls_per_day': 148.1, 'win_rate': 0.5837}, {'threshold': 0.1171, 'calls_per_day': 37.2, 'win_rate': 0.5785}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42902, 'rate': 0.5311}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15265 | 0.351 | 0.532 (15049) | 0.557 (2095) | 0.750 (2543) |
| volatility: normal | 15264 | 0.380 | 0.527 (15209) | 0.578 (1552) | 0.747 (2490) |
| volatility: wild | 15264 | 0.391 | 0.532 (15226) | 0.586 (1215) | 0.758 (2181) |
| session: Asia 00-08 | 15360 | 0.373 | 0.532 (15249) | 0.560 (1705) | 0.748 (2331) |
| session: Europe 08-13 | 9600 | 0.368 | 0.530 (9525) | 0.579 (1186) | 0.765 (1526) |
| session: US 13-21 | 15253 | 0.381 | 0.534 (15162) | 0.597 (1376) | 0.744 (2498) |
| session: late 21-24 | 5580 | 0.368 | 0.519 (5548) | 0.524 (595) | 0.758 (859) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.391 | 0.356 | 0.313 | 0.313 | 0.600 | 0.282 | 0.501 | 1.429 |
| 6h | 360 | 0.383 | 0.381 | 0.306 | 0.343 | 0.501 | 0.254 | 0.512 | 1.393 |
| 24h | 1440 | 0.388 | 0.382 | 0.299 | 0.341 | 0.536 | 0.265 | 0.511 | 1.219 |
| 7d | 10080 | 0.387 | 0.380 | 0.297 | 0.331 | 0.535 | 0.267 | 0.506 | 1.204 |
| 30d | 43200 | 0.375 | 0.369 | 0.288 | 0.320 | 0.531 | 0.266 | 0.483 | 1.267 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.391 / 0.600 / 0.900; 2: 0.384 / 0.600 / 1.000; 3: 0.373 / 0.567 / 1.000; 4: 0.349 / 0.483 / 0.833; 5: 0.347 / 0.450 / 1.000; 6: 0.335 / 0.450 / 1.000; 7: 0.338 / 0.467 / 0.867; 8: 0.367 / 0.567 / 0.833; 9: 0.361 / 0.483 / 1.000; 10: 0.328 / 0.417 / 0.900; 11: 0.354 / 0.467 / 1.000; 12: 0.375 / 0.567 / 1.000; 13: 0.342 / 0.433 / 1.000; 14: 0.350 / 0.533 / 0.917; 15: 0.361 / 0.533 / 0.883
- 6h: 1: 0.383 / 0.501 / 0.894; 2: 0.384 / 0.526 / 0.992; 3: 0.373 / 0.496 / 0.992; 4: 0.375 / 0.501 / 0.833; 5: 0.377 / 0.510 / 0.992; 6: 0.372 / 0.487 / 0.983; 7: 0.374 / 0.504 / 0.833; 8: 0.380 / 0.529 / 0.747; 9: 0.375 / 0.513 / 0.997; 10: 0.375 / 0.507 / 0.761; 11: 0.375 / 0.515 / 0.997; 12: 0.380 / 0.521 / 0.994; 13: 0.368 / 0.485 / 0.944; 14: 0.364 / 0.482 / 0.747; 15: 0.367 / 0.485 / 0.769
- 24h: 1: 0.388 / 0.536 / 0.897; 2: 0.376 / 0.502 / 0.906; 3: 0.377 / 0.521 / 0.915; 4: 0.373 / 0.499 / 0.885; 5: 0.371 / 0.498 / 0.908; 6: 0.369 / 0.486 / 0.915; 7: 0.372 / 0.505 / 0.878; 8: 0.372 / 0.508 / 0.851; 9: 0.372 / 0.499 / 0.903; 10: 0.373 / 0.514 / 0.908; 11: 0.374 / 0.512 / 0.903; 12: 0.374 / 0.518 / 0.907; 13: 0.371 / 0.499 / 0.922; 14: 0.368 / 0.487 / 0.906; 15: 0.369 / 0.490 / 0.897
- 7d: 1: 0.387 / 0.535 / 0.900; 2: 0.372 / 0.495 / 0.901; 3: 0.372 / 0.504 / 0.901; 4: 0.371 / 0.497 / 0.898; 5: 0.374 / 0.507 / 0.900; 6: 0.370 / 0.497 / 0.903; 7: 0.370 / 0.502 / 0.899; 8: 0.371 / 0.510 / 0.895; 9: 0.369 / 0.499 / 0.902; 10: 0.371 / 0.513 / 0.897; 11: 0.369 / 0.505 / 0.900; 12: 0.369 / 0.502 / 0.902; 13: 0.366 / 0.494 / 0.903; 14: 0.366 / 0.499 / 0.897; 15: 0.367 / 0.500 / 0.898
- 30d: 1: 0.375 / 0.531 / 0.898; 2: 0.361 / 0.491 / 0.900; 3: 0.365 / 0.512 / 0.900; 4: 0.361 / 0.497 / 0.900; 5: 0.363 / 0.506 / 0.900; 6: 0.360 / 0.501 / 0.900; 7: 0.361 / 0.502 / 0.900; 8: 0.361 / 0.507 / 0.899; 9: 0.359 / 0.500 / 0.900; 10: 0.360 / 0.505 / 0.899; 11: 0.360 / 0.506 / 0.900; 12: 0.359 / 0.503 / 0.900; 13: 0.358 / 0.500 / 0.900; 14: 0.358 / 0.502 / 0.899; 15: 0.358 / 0.501 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.086 (body 0.035, range 0.137); 'price stays where it was' would score 0.139; colour right 0.550; typical miss of the close 23.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.080 (body 0.048, range 0.112); 'price stays where it was' would score 0.130; colour right 0.543; typical miss of the close 41.7 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.114 (body 0.068, range 0.160); 'price stays where it was' would score 0.136; colour right 0.499; typical miss of the close 16.3 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.134 (body 0.085, range 0.182); 'price stays where it was' would score 0.143; colour right 0.502; typical miss of the close 14.4 bp; chain ended on the right side 0.503 of 672 chains; n=10080
- 30d: match 0.127 (body 0.084, range 0.170); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.9 bp; chain ended on the right side 0.512 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 5.8; 2: 0.207 / 6.7; 3: 0.165 / 8.7; 4: 0.136 / 9.0; 5: 0.124 / 9.9; 6: 0.118 / 10.7; 7: 0.116 / 11.1; 8: 0.101 / 12.1; 9: 0.092 / 12.8; 10: 0.088 / 13.1; 11: 0.088 / 13.6; 12: 0.083 / 13.8; 13: 0.076 / 14.7; 14: 0.070 / 15.0; 15: 0.068 / 15.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 165067, probability skill vs chance 0.2252, widened contest next: True
  - now: threshold 0.8316, hit rate recent 0.9159 / long run 0.9298
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.282, naive rule 0.477, lift 3.04x
    - 24h: 63 calls (63 a day), hit rate 0.921, chance 0.297, naive rule 0.506, lift 3.10x
    - 7d: 423 calls (60 a day), hit rate 0.924, chance 0.300, naive rule 0.520, lift 3.08x
    - 30d: 1747 calls (58 a day), hit rate 0.930, chance 0.294, naive rule 0.504, lift 3.16x
  - next: threshold 0.533, hit rate recent 0.5514 / long run 0.588
    - 6h: 43 calls (174 a day), hit rate 0.465, chance 0.282, lift 1.65x
    - 24h: 126 calls (126 a day), hit rate 0.563, chance 0.297, lift 1.90x
    - 7d: 980 calls (140 a day), hit rate 0.588, chance 0.300, lift 1.96x
    - 30d: 2734 calls (91 a day), hit rate 0.598, chance 0.294, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 559, 0.503; 0.35: 530, 0.528; 0.40: 481, 0.572; 0.45: 419, 0.635; 0.50: 368, 0.681; 0.55: 320, 0.725; 0.60: 271, 0.771; 0.65: 227, 0.802; 0.70: 178, 0.833; 0.75: 143, 0.869; 0.80: 95, 0.901; 0.85: 42, 0.941; 0.90: 3, 0.959
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 486, 0.470; 0.40: 383, 0.511; 0.45: 290, 0.542; 0.50: 186, 0.570; 0.55: 78, 0.587; 0.60: 10, 0.638; 0.65: 0, 0.538
- **K=5**: model 1794528000, labels learned 165065, probability skill vs chance 0.2237, widened contest next: False
  - now: threshold 0.7032, hit rate recent 0.7967 / long run 0.7958
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.170, naive rule 0.423, lift 4.78x
    - 24h: 74 calls (74 a day), hit rate 0.784, chance 0.196, naive rule 0.455, lift 4.00x
    - 7d: 437 calls (62 a day), hit rate 0.817, chance 0.195, naive rule 0.437, lift 4.18x
    - 30d: 1800 calls (60 a day), hit rate 0.794, chance 0.189, naive rule 0.416, lift 4.21x
  - next: threshold 0.4543, hit rate recent 0.4818 / long run 0.4981
    - 6h: 24 calls (98 a day), hit rate 0.417, chance 0.170, lift 2.45x
    - 24h: 52 calls (52 a day), hit rate 0.481, chance 0.196, lift 2.45x
    - 7d: 354 calls (51 a day), hit rate 0.511, chance 0.195, lift 2.62x
    - 30d: 1721 calls (57 a day), hit rate 0.510, chance 0.189, lift 2.71x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.426; 0.35: 364, 0.475; 0.40: 295, 0.542; 0.45: 239, 0.603; 0.50: 186, 0.653; 0.55: 150, 0.685; 0.60: 116, 0.729; 0.65: 85, 0.767; 0.70: 54, 0.801; 0.75: 27, 0.840; 0.80: 6, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 331, 0.397; 0.35: 246, 0.434; 0.40: 157, 0.461; 0.45: 63, 0.507; 0.50: 8, 0.567; 0.55: 1, 0.529
- **K=8**: model 1794960000, labels learned 165062, probability skill vs chance 0.2245, widened contest next: True
  - now: threshold 0.5875, hit rate recent 0.7338 / long run 0.6829
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.133, naive rule 0.375, lift 4.84x
    - 24h: 61 calls (61 a day), hit rate 0.770, chance 0.131, naive rule 0.378, lift 5.86x
    - 7d: 426 calls (61 a day), hit rate 0.692, chance 0.127, naive rule 0.369, lift 5.45x
    - 30d: 1669 calls (56 a day), hit rate 0.687, chance 0.124, naive rule 0.351, lift 5.55x
  - next: threshold 0.3507, hit rate recent 0.381 / long run 0.417
    - 6h: 27 calls (111 a day), hit rate 0.333, chance 0.133, lift 2.51x
    - 24h: 77 calls (78 a day), hit rate 0.351, chance 0.131, lift 2.67x
    - 7d: 550 calls (79 a day), hit rate 0.425, chance 0.127, lift 3.35x
    - 30d: 2207 calls (74 a day), hit rate 0.421, chance 0.124, lift 3.40x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.428; 0.35: 203, 0.487; 0.40: 159, 0.538; 0.45: 121, 0.581; 0.50: 87, 0.637; 0.55: 64, 0.675; 0.60: 43, 0.716; 0.65: 25, 0.767; 0.70: 10, 0.805; 0.75: 1, 0.737
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 157, 0.378; 0.35: 83, 0.411; 0.40: 29, 0.444; 0.45: 7, 0.482; 0.50: 1, 0.676
- **K=13**: model 1795478400, labels learned 165057, probability skill vs chance 0.2149, widened contest next: False
  - now: threshold 0.4598, hit rate recent 0.6739 / long run 0.5901
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.091, naive rule 0.413, lift 7.58x
    - 24h: 49 calls (50 a day), hit rate 0.673, chance 0.093, naive rule 0.372, lift 7.27x
    - 7d: 367 calls (53 a day), hit rate 0.605, chance 0.084, naive rule 0.325, lift 7.22x
    - 30d: 1606 calls (54 a day), hit rate 0.584, chance 0.081, naive rule 0.302, lift 7.25x
  - next: threshold 0.302, hit rate recent 0.3633 / long run 0.3447
    - 6h: 23 calls (96 a day), hit rate 0.304, chance 0.091, lift 3.33x
    - 24h: 67 calls (68 a day), hit rate 0.343, chance 0.093, lift 3.71x
    - 7d: 409 calls (59 a day), hit rate 0.362, chance 0.084, lift 4.32x
    - 30d: 1822 calls (61 a day), hit rate 0.340, chance 0.081, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 142, 0.427; 0.35: 104, 0.477; 0.40: 72, 0.540; 0.45: 51, 0.590; 0.50: 35, 0.627; 0.55: 22, 0.650; 0.60: 10, 0.671; 0.65: 2, 0.532
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 55, 0.345; 0.35: 15, 0.387; 0.40: 2, 0.451; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 33.413 | 3.40% | 0.917 | 0.500 | 0.249 | 0.467 | 0.422 |
| 6h | 45.522 | 8.02% | 0.894 | 0.472 | 0.251 | 0.490 | 0.395 |
| 24h | 26.212 | 4.76% | 0.897 | 0.503 | 0.250 | 0.509 | 0.619 |
| 7d | 25.491 | 4.37% | 0.899 | 0.500 | 0.250 | 0.511 | 0.657 |
| 30d | 20.014 | 4.80% | 0.900 | 0.500 | 0.250 | 0.507 | 0.708 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 34.588 | 33.836 | 33.882 | 33.585 | 34.249 | 34.682 | 33.512 | 33.225 | 33.421 | 33.413 |
| 6h | 49.492 | 45.806 | 45.880 | 45.539 | 46.703 | 47.231 | 45.599 | 45.443 | 45.451 | 45.522 |
| 24h | 27.522 | 26.399 | 26.434 | 26.253 | 26.840 | 26.836 | 26.175 | 26.130 | 26.163 | 26.212 |
| 7d | 26.655 | 25.754 | 25.670 | 25.516 | 26.078 | 25.879 | 25.485 | 25.432 | 25.455 | 25.491 |
| 30d | 21.022 | 20.202 | 20.154 | 20.068 | 20.438 | 20.355 | 19.996 | 19.968 | 19.980 | 20.014 |

## Next candle

- candle starting 2026-11-25 19:13 UTC, last close 1685.38
- P(up) 0.51, return quantiles (bp): {'05': -17.538, '10': -12.207, '25': -5.846, '40': -1.954, '50': 0.209, '60': 2.555, '75': 6.939, '90': 13.756, '95': 17.644}
- changepoint probability 0.0462, regime age 49.2 min
- agent weights: empirical 0.003, ewma 0.084, garch 0.065, har 0.215, bocpd 0.008, hmm 0.005, online_qr 0.243, lgbm 0.377

## Learning log

- 2026-11-23 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.9112}, "hmm": {"sd_bp": [5.07, 10.1, 28.28], "stay": [0.973, 0.946, 0.862]}}
- 2026-11-24 00:00 UTC: {"garch": {"alpha": 0.0886, "beta": 0.9021}, "hmm": {"sd_bp": [4.97, 10.02, 31.47], "stay": [0.968, 0.952, 0.875]}, "lgbm": {"challenger_loss": 0.25051, "champion_loss": 0.25047, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48498, "challengers": 3, "chance_loss": 0.6173, "widened": true, "champion_loss": 0.48458, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37971, "challengers": 1, "chance_loss": 0.49915, "widened": false, "champion_loss": 0.37928, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27848, "challengers": 3, "chance_loss": 0.37338, "widened": true, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20281, "challengers": 3, "chance_loss": 0.28057, "widened": true, "champion_loss": 0.20335, "promoted": true}}
- 2026-11-24 12:00 UTC: {"garch": {"alpha": 0.0937, "beta": 0.8962}, "hmm": {"sd_bp": [5.06, 10.1, 31.41], "stay": [0.968, 0.948, 0.887]}}
- 2026-11-25 00:00 UTC: {"garch": {"alpha": 0.1003, "beta": 0.8874}, "hmm": {"sd_bp": [4.92, 10.11, 34.59], "stay": [0.965, 0.949, 0.856]}, "lgbm": {"challenger_loss": 0.24916, "champion_loss": 0.24908, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48879, "challengers": 1, "chance_loss": 0.61057, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37287, "challengers": 1, "chance_loss": 0.48385, "widened": false, "champion_loss": 0.37277, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27415, "challengers": 1, "chance_loss": 0.37509, "widened": false, "champion_loss": 0.27282, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19964, "challengers": 1, "chance_loss": 0.28525, "widened": false, "champion_loss": 0.19929, "promoted": false}}
- 2026-11-25 12:00 UTC: {"garch": {"alpha": 0.091, "beta": 0.8903}, "hmm": {"sd_bp": [4.89, 9.77, 34.58], "stay": [0.96, 0.954, 0.849]}}
- HMM volatility states (sd, bp per minute): [4.89, 9.77, 34.58], current probabilities: [0.13, 0.866, 0.004]
- live generator: {'versions': 60, 'latest_effective': '2026-11-25 19:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.453, 'l_abs': 0.639, 'l_hi': 0.803, 'l_lo': 0.699, 'b05': 0.721, 'b25': 0.684, 'b75': 0.66, 'b95': 0.728}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.165, 1.678, 3.014, 2.309, 1.993, 4.092, 9.004, 2.608, 7.794, 3.536, 3.348, 2.976, 9.675, 8.381]}
- calibration offsets (in sigma): {'05': 0.016, '10': 0.032, '25': 0.07, '40': 0.068, '50': 0.05, '60': 0.032, '75': 0.07, '90': 0.098, '95': 0.024}
