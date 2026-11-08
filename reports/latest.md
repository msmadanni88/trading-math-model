# ETH-USD 60s candle generator - report

- generated: 2026-11-08 19:14 UTC
- last closed candle: 2026-11-08 19:14 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.490 (672) [0.455, 0.518] | 0.517 (2879) [0.501, 0.534] | 0.513 (6426) [0.501, 0.525] | 0.514 (3454) [0.497, 0.532] | 0.579 (76) | 0.500 | flat -0.034 (noise 0.029) |
| colour_clear | 0.556 (741) | 0.532 (5546) [0.515, 0.550] | 0.542 (23847) [0.536, 0.548] | 0.522 (52595) [0.516, 0.527] | 0.543 (28357) [0.538, 0.548] | 0.570 (614) | 0.500 | flat -0.009 (noise 0.012) |
| colour_confident | 0.577 (253) | 0.577 (957) [0.561, 0.598] | 0.594 (4425) [0.584, 0.604] | 0.596 (5240) [0.585, 0.607] | 0.596 (5240) [0.585, 0.607] | 0.563 (263) | 0.500 | flat -0.010 (noise 0.022) |
| colour_next | 0.531 (1402) | 0.527 (9985) [0.517, 0.536] | 0.529 (42842) [0.525, 0.533] | 0.516 (95733) [0.512, 0.520] | 0.529 (51384) [0.526, 0.533] | 0.573 (1109) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.496 (19628) | 0.502 (139790) [0.500, 0.504] | 0.501 (599788) [0.500, 0.503] | 0.501 (1340262) [0.500, 0.502] | 0.501 (719376) [0.500, 0.502] | 0.505 (15526) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.650 (80) | 0.615 (226) [0.577, 0.640] | 0.630 (1164) [0.612, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.634 (93) | 0.500 | flat +0.011 (noise 0.042) |
| reversal_k13_next | 0.269 (67) | 0.344 (378) [0.311, 0.376] | 0.325 (1810) [0.311, 0.340] | 0.313 (4382) [0.302, 0.323] | 0.325 (2277) [0.313, 0.337] | 0.272 (81) | 0.077 | flat +0.004 (noise 0.034) |
| reversal_k13_now | 0.511 (47) | 0.566 (378) [0.529, 0.602] | 0.563 (1648) [0.544, 0.583] | 0.573 (3459) [0.560, 0.586] | 0.567 (1987) [0.549, 0.585] | 0.575 (47) | 0.077 | flat -0.011 (noise 0.035) |
| reversal_k3_next | 0.618 (55) | 0.620 (508) [0.590, 0.645] | 0.590 (2972) [0.579, 0.602] | 0.587 (5899) [0.578, 0.596] | 0.588 (3459) [0.577, 0.598] | 0.614 (57) | 0.294 | flat +0.033 (noise 0.028) |
| reversal_k3_now | 0.900 (60) | 0.909 (408) [0.902, 0.918] | 0.932 (1741) [0.921, 0.942] | 0.936 (3849) [0.930, 0.942] | 0.931 (2086) [0.922, 0.940] | 0.957 (47) | 0.294 | flat -0.036 (noise 0.018) |
| reversal_k5_next | 0.484 (64) | 0.528 (390) [0.502, 0.553] | 0.485 (2708) [0.471, 0.500] | 0.484 (5220) [0.473, 0.495] | 0.478 (3230) [0.464, 0.493] | 0.537 (67) | 0.187 | flat +0.009 (noise 0.033) |
| reversal_k5_now | 0.808 (47) | 0.821 (390) [0.806, 0.836] | 0.821 (1621) [0.811, 0.829] | 0.828 (3570) [0.820, 0.837] | 0.821 (1959) [0.811, 0.830] | 0.744 (43) | 0.187 | flat -0.006 (noise 0.027) |
| reversal_k8_next | 0.383 (60) | 0.443 (377) [0.416, 0.469] | 0.396 (2632) [0.383, 0.410] | 0.395 (5278) [0.384, 0.406] | 0.394 (3172) [0.382, 0.407] | 0.329 (73) | 0.121 | flat +0.035 (noise 0.032) |
| reversal_k8_now | 0.720 (50) | 0.696 (362) [0.674, 0.716] | 0.686 (1534) [0.667, 0.705] | 0.702 (3481) [0.688, 0.715] | 0.691 (1894) [0.673, 0.709] | 0.636 (44) | 0.122 | flat -0.009 (noise 0.034) |
| overall | 0.500 (21576) | 0.506 (153638) [0.504, 0.508] | 0.505 (662175) [0.504, 0.506] | 0.504 (1477559) [0.503, 0.505] | 0.505 (794278) [0.503, 0.506] | 0.510 (17170) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07808, 0.118] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.53, 'levels': [{'threshold': 0.07808, 'calls_per_day': 144.9, 'win_rate': 0.5712}, {'threshold': 0.118, 'calls_per_day': 36.7, 'win_rate': 0.6308}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42798, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15265 | 0.339 | 0.529 (14967) | 0.571 (2469) | 0.740 (2551) |
| volatility: normal | 15264 | 0.368 | 0.536 (15193) | 0.617 (1472) | 0.756 (2293) |
| volatility: wild | 15265 | 0.384 | 0.524 (15225) | 0.611 (836) | 0.765 (2128) |
| session: Asia 00-08 | 15360 | 0.363 | 0.535 (15224) | 0.598 (1684) | 0.761 (2275) |
| session: Europe 08-13 | 9600 | 0.356 | 0.534 (9489) | 0.591 (1280) | 0.744 (1570) |
| session: US 13-21 | 15254 | 0.371 | 0.526 (15142) | 0.593 (1239) | 0.752 (2334) |
| session: late 21-24 | 5580 | 0.355 | 0.516 (5530) | 0.575 (574) | 0.749 (793) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.360 | 0.356 | 0.281 | 0.281 | 0.517 | 0.273 | 0.447 | 1.234 |
| 6h | 360 | 0.368 | 0.342 | 0.276 | 0.309 | 0.598 | 0.291 | 0.445 | 1.291 |
| 24h | 1440 | 0.334 | 0.318 | 0.234 | 0.255 | 0.571 | 0.269 | 0.399 | 1.190 |
| 7d | 10080 | 0.365 | 0.360 | 0.275 | 0.306 | 0.531 | 0.262 | 0.467 | 1.316 |
| 30d | 43200 | 0.363 | 0.355 | 0.274 | 0.305 | 0.530 | 0.263 | 0.463 | 1.276 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.360 / 0.517 / 0.883; 2: 0.374 / 0.517 / 0.867; 3: 0.347 / 0.517 / 0.867; 4: 0.365 / 0.533 / 0.883; 5: 0.339 / 0.467 / 0.833; 6: 0.339 / 0.450 / 0.783; 7: 0.362 / 0.550 / 0.817; 8: 0.374 / 0.567 / 0.833; 9: 0.355 / 0.550 / 0.850; 10: 0.336 / 0.467 / 0.833; 11: 0.355 / 0.417 / 0.883; 12: 0.347 / 0.483 / 0.850; 13: 0.359 / 0.450 / 0.900; 14: 0.389 / 0.567 / 0.883; 15: 0.343 / 0.467 / 0.883
- 6h: 1: 0.368 / 0.598 / 0.886; 2: 0.348 / 0.514 / 0.872; 3: 0.355 / 0.559 / 0.842; 4: 0.331 / 0.463 / 0.839; 5: 0.352 / 0.539 / 0.836; 6: 0.336 / 0.486 / 0.831; 7: 0.342 / 0.522 / 0.844; 8: 0.344 / 0.514 / 0.850; 9: 0.350 / 0.553 / 0.872; 10: 0.330 / 0.500 / 0.878; 11: 0.337 / 0.492 / 0.903; 12: 0.344 / 0.511 / 0.883; 13: 0.338 / 0.478 / 0.922; 14: 0.359 / 0.573 / 0.931; 15: 0.342 / 0.522 / 0.917
- 24h: 1: 0.334 / 0.571 / 0.879; 2: 0.318 / 0.506 / 0.892; 3: 0.315 / 0.512 / 0.885; 4: 0.311 / 0.497 / 0.885; 5: 0.314 / 0.504 / 0.889; 6: 0.304 / 0.475 / 0.886; 7: 0.311 / 0.499 / 0.890; 8: 0.313 / 0.488 / 0.889; 9: 0.315 / 0.511 / 0.897; 10: 0.311 / 0.502 / 0.901; 11: 0.315 / 0.512 / 0.899; 12: 0.317 / 0.520 / 0.900; 13: 0.310 / 0.479 / 0.899; 14: 0.320 / 0.527 / 0.899; 15: 0.309 / 0.488 / 0.896
- 7d: 1: 0.365 / 0.531 / 0.895; 2: 0.354 / 0.493 / 0.900; 3: 0.356 / 0.513 / 0.899; 4: 0.353 / 0.501 / 0.899; 5: 0.353 / 0.503 / 0.899; 6: 0.351 / 0.504 / 0.899; 7: 0.352 / 0.502 / 0.900; 8: 0.350 / 0.499 / 0.900; 9: 0.352 / 0.508 / 0.900; 10: 0.350 / 0.499 / 0.900; 11: 0.350 / 0.501 / 0.901; 12: 0.351 / 0.506 / 0.900; 13: 0.349 / 0.493 / 0.901; 14: 0.351 / 0.507 / 0.901; 15: 0.350 / 0.501 / 0.900
- 30d: 1: 0.363 / 0.530 / 0.897; 2: 0.351 / 0.495 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.348 / 0.501 / 0.899; 7: 0.349 / 0.499 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.349 / 0.503 / 0.900; 10: 0.349 / 0.504 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.504 / 0.900; 13: 0.346 / 0.499 / 0.900; 14: 0.347 / 0.501 / 0.900; 15: 0.347 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.059 (body 0.028, range 0.089); 'price stays where it was' would score 0.089; colour right 0.483; typical miss of the close 7.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.127 (body 0.082, range 0.172); 'price stays where it was' would score 0.128; colour right 0.531; typical miss of the close 5.4 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.115 (body 0.080, range 0.150); 'price stays where it was' would score 0.112; colour right 0.498; typical miss of the close 4.1 bp; chain ended on the right side 0.594 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.124; colour right 0.505; typical miss of the close 8.4 bp; chain ended on the right side 0.499 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.2 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.3; 2: 0.198 / 4.9; 3: 0.167 / 6.4; 4: 0.131 / 6.7; 5: 0.127 / 7.4; 6: 0.115 / 8.1; 7: 0.111 / 8.3; 8: 0.099 / 9.2; 9: 0.091 / 9.2; 10: 0.093 / 9.7; 11: 0.087 / 9.9; 12: 0.079 / 10.4; 13: 0.074 / 10.6; 14: 0.072 / 11.0; 15: 0.066 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 140588, probability skill vs chance 0.2149, widened contest next: False
  - now: threshold 0.8382, hit rate recent 0.9321 / long run 0.9291
    - 6h: 15 calls (61 a day), hit rate 1.000, chance 0.313, naive rule 0.522, lift 3.20x
    - 24h: 60 calls (60 a day), hit rate 0.917, chance 0.297, naive rule 0.506, lift 3.09x
    - 7d: 401 calls (57 a day), hit rate 0.918, chance 0.297, naive rule 0.498, lift 3.09x
    - 30d: 1737 calls (58 a day), hit rate 0.933, chance 0.296, naive rule 0.498, lift 3.15x
  - next: threshold 0.5665, hit rate recent 0.6283 / long run 0.6082
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.313, lift 2.51x
    - 24h: 65 calls (65 a day), hit rate 0.600, chance 0.297, lift 2.02x
    - 7d: 461 calls (66 a day), hit rate 0.618, chance 0.297, lift 2.08x
    - 30d: 2958 calls (99 a day), hit rate 0.591, chance 0.296, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.501; 0.35: 534, 0.526; 0.40: 474, 0.582; 0.45: 406, 0.652; 0.50: 356, 0.699; 0.55: 308, 0.743; 0.60: 260, 0.786; 0.65: 219, 0.811; 0.70: 173, 0.843; 0.75: 139, 0.874; 0.80: 92, 0.906; 0.85: 46, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.430; 0.35: 499, 0.464; 0.40: 402, 0.501; 0.45: 304, 0.537; 0.50: 196, 0.569; 0.55: 89, 0.579; 0.60: 12, 0.654; 0.65: 1, 0.619
- **K=5**: model 1792540800, labels learned 140586, probability skill vs chance 0.2056, widened contest next: True
  - now: threshold 0.6855, hit rate recent 0.785 / long run 0.8163
    - 6h: 16 calls (65 a day), hit rate 0.688, chance 0.197, naive rule 0.428, lift 3.49x
    - 24h: 53 calls (53 a day), hit rate 0.755, chance 0.191, naive rule 0.414, lift 3.96x
    - 7d: 378 calls (54 a day), hit rate 0.807, chance 0.187, naive rule 0.405, lift 4.31x
    - 30d: 1625 calls (54 a day), hit rate 0.819, chance 0.187, naive rule 0.408, lift 4.37x
  - next: threshold 0.4498, hit rate recent 0.5318 / long run 0.5153
    - 6h: 21 calls (86 a day), hit rate 0.619, chance 0.197, lift 3.14x
    - 24h: 78 calls (78 a day), hit rate 0.513, chance 0.191, lift 2.69x
    - 7d: 412 calls (59 a day), hit rate 0.527, chance 0.187, lift 2.81x
    - 30d: 2711 calls (90 a day), hit rate 0.486, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.424; 0.35: 350, 0.488; 0.40: 282, 0.560; 0.45: 232, 0.610; 0.50: 186, 0.659; 0.55: 149, 0.696; 0.60: 113, 0.745; 0.65: 76, 0.785; 0.70: 47, 0.824; 0.75: 28, 0.856; 0.80: 11, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.383; 0.35: 257, 0.422; 0.40: 161, 0.461; 0.45: 67, 0.491; 0.50: 11, 0.524; 0.55: 1, 0.421
- **K=8**: model 1794096000, labels learned 140583, probability skill vs chance 0.1863, widened contest next: True
  - now: threshold 0.5723, hit rate recent 0.6787 / long run 0.6925
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.124, naive rule 0.341, lift 5.03x
    - 24h: 54 calls (54 a day), hit rate 0.648, chance 0.118, naive rule 0.311, lift 5.48x
    - 7d: 357 calls (51 a day), hit rate 0.683, chance 0.122, naive rule 0.338, lift 5.62x
    - 30d: 1542 calls (51 a day), hit rate 0.687, chance 0.121, naive rule 0.336, lift 5.68x
  - next: threshold 0.3597, hit rate recent 0.3418 / long run 0.4105
    - 6h: 26 calls (107 a day), hit rate 0.346, chance 0.124, lift 2.79x
    - 24h: 82 calls (83 a day), hit rate 0.329, chance 0.118, lift 2.79x
    - 7d: 416 calls (59 a day), hit rate 0.418, chance 0.122, lift 3.44x
    - 30d: 2635 calls (88 a day), hit rate 0.394, chance 0.121, lift 3.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 192, 0.493; 0.40: 152, 0.539; 0.45: 118, 0.586; 0.50: 85, 0.638; 0.55: 60, 0.675; 0.60: 40, 0.712; 0.65: 24, 0.781; 0.70: 12, 0.806; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.362; 0.35: 88, 0.388; 0.40: 24, 0.420; 0.45: 4, 0.448; 0.50: 1, 0.714
- **K=13**: model 1794096000, labels learned 140578, probability skill vs chance 0.1723, widened contest next: True
  - now: threshold 0.4451, hit rate recent 0.566 / long run 0.5692
    - 6h: 22 calls (92 a day), hit rate 0.500, chance 0.078, naive rule 0.298, lift 6.39x
    - 24h: 53 calls (54 a day), hit rate 0.566, chance 0.076, naive rule 0.263, lift 7.43x
    - 7d: 375 calls (54 a day), hit rate 0.563, chance 0.078, naive rule 0.283, lift 7.17x
    - 30d: 1656 calls (55 a day), hit rate 0.560, chance 0.078, naive rule 0.281, lift 7.21x
  - next: threshold 0.2854, hit rate recent 0.2879 / long run 0.3227
    - 6h: 28 calls (117 a day), hit rate 0.357, chance 0.078, lift 4.56x
    - 24h: 92 calls (93 a day), hit rate 0.261, chance 0.076, lift 3.43x
    - 7d: 436 calls (62 a day), hit rate 0.333, chance 0.078, lift 4.24x
    - 30d: 1831 calls (61 a day), hit rate 0.322, chance 0.078, lift 4.15x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 132, 0.436; 0.35: 95, 0.483; 0.40: 67, 0.542; 0.45: 46, 0.584; 0.50: 31, 0.643; 0.55: 20, 0.672; 0.60: 12, 0.712; 0.65: 4, 0.676; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.342; 0.40: 3, 0.405; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 8.068 | 3.26% | 0.883 | 0.467 | 0.249 | 0.500 | 0.413 |
| 6h | 8.154 | 2.38% | 0.889 | 0.508 | 0.250 | 0.489 | 0.380 |
| 24h | 6.400 | 1.60% | 0.892 | 0.491 | 0.250 | 0.499 | 0.453 |
| 7d | 14.956 | 5.08% | 0.899 | 0.500 | 0.250 | 0.504 | 0.753 |
| 30d | 14.760 | 4.46% | 0.900 | 0.500 | 0.250 | 0.499 | 0.714 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.340 | 8.140 | 8.262 | 8.029 | 8.278 | 8.393 | 8.001 | 8.013 | 8.047 | 8.068 |
| 6h | 8.353 | 8.221 | 8.220 | 8.134 | 8.429 | 8.384 | 8.137 | 8.113 | 8.129 | 8.154 |
| 24h | 6.504 | 6.434 | 6.425 | 6.440 | 6.559 | 6.713 | 6.394 | 6.379 | 6.382 | 6.400 |
| 7d | 15.756 | 15.074 | 15.053 | 15.010 | 15.228 | 15.335 | 14.940 | 14.933 | 14.929 | 14.956 |
| 30d | 15.449 | 14.910 | 14.858 | 14.790 | 15.036 | 15.006 | 14.750 | 14.730 | 14.732 | 14.760 |

## Next candle

- candle starting 2026-11-08 19:14 UTC, last close 2229.7
- P(up) 0.5263, return quantiles (bp): {'05': -4.709, '10': -3.345, '25': -1.451, '40': -0.43, '50': 0.149, '60': 0.699, '75': 1.736, '90': 3.371, '95': 4.365}
- changepoint probability 0.0543, regime age 87.1 min
- agent weights: empirical 0.021, ewma 0.105, garch 0.106, har 0.150, bocpd 0.010, hmm 0.005, online_qr 0.267, lgbm 0.336

## Learning log

- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- HMM volatility states (sd, bp per minute): [2.33, 5.88, 17.3], current probabilities: [0.982, 0.018, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-08 19:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.223, 'l_abs': 0.612, 'l_hi': 0.74, 'l_lo': 0.714, 'b05': 0.647, 'b25': 0.627, 'b75': 0.605, 'b95': 0.652}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.6, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.7, 2.352, 2.668, 2.988, 3.346, 3.277, 3.51, 3.731, 3.495, 3.459, 3.921, 3.701, 3.926, 4.238]}
- calibration offsets (in sigma): {'05': -0.0535, '10': 0.003, '25': 0.0225, '40': -0.008, '50': 0.015, '60': -0.002, '75': 0.0075, '90': 0.017, '95': 0.0035}
