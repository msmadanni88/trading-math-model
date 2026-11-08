# ETH-USD 60s candle generator - report

- generated: 2026-11-08 07:55 UTC
- last closed candle: 2026-11-08 07:55 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.490 (672) [0.455, 0.518] | 0.517 (2879) [0.501, 0.534] | 0.513 (6426) [0.501, 0.525] | 0.514 (3454) [0.497, 0.532] | 0.581 (31) | 0.500 | flat -0.034 (noise 0.029) |
| colour_clear | 0.556 (741) | 0.532 (5546) [0.515, 0.550] | 0.542 (23847) [0.536, 0.548] | 0.522 (52595) [0.516, 0.527] | 0.543 (28357) [0.538, 0.548] | 0.572 (250) | 0.500 | flat -0.009 (noise 0.012) |
| colour_confident | 0.577 (253) | 0.577 (957) [0.561, 0.598] | 0.594 (4425) [0.584, 0.604] | 0.596 (5240) [0.585, 0.607] | 0.596 (5240) [0.585, 0.607] | 0.592 (125) | 0.500 | flat -0.010 (noise 0.022) |
| colour_next | 0.531 (1402) | 0.527 (9985) [0.517, 0.536] | 0.529 (42842) [0.525, 0.533] | 0.516 (95733) [0.512, 0.520] | 0.529 (51384) [0.526, 0.533] | 0.565 (444) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.496 (19628) | 0.502 (139790) [0.500, 0.504] | 0.501 (599788) [0.500, 0.503] | 0.501 (1340262) [0.500, 0.502] | 0.501 (719376) [0.500, 0.502] | 0.500 (6216) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.650 (80) | 0.615 (226) [0.577, 0.640] | 0.630 (1164) [0.612, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.608 (51) | 0.500 | flat +0.011 (noise 0.042) |
| reversal_k13_next | 0.269 (67) | 0.344 (378) [0.311, 0.376] | 0.325 (1810) [0.311, 0.340] | 0.313 (4382) [0.302, 0.323] | 0.325 (2277) [0.313, 0.337] | 0.250 (28) | 0.077 | flat +0.004 (noise 0.034) |
| reversal_k13_now | 0.511 (47) | 0.566 (378) [0.529, 0.602] | 0.563 (1648) [0.544, 0.583] | 0.573 (3459) [0.560, 0.586] | 0.567 (1987) [0.549, 0.585] | 0.727 (11) | 0.077 | flat -0.011 (noise 0.035) |
| reversal_k3_next | 0.618 (55) | 0.620 (508) [0.590, 0.645] | 0.590 (2972) [0.579, 0.602] | 0.587 (5899) [0.578, 0.596] | 0.588 (3459) [0.577, 0.598] | 0.538 (26) | 0.294 | flat +0.033 (noise 0.028) |
| reversal_k3_now | 0.900 (60) | 0.909 (408) [0.902, 0.918] | 0.932 (1741) [0.921, 0.942] | 0.936 (3849) [0.930, 0.942] | 0.931 (2086) [0.922, 0.940] | 0.955 (22) | 0.294 | flat -0.036 (noise 0.018) |
| reversal_k5_next | 0.484 (64) | 0.528 (390) [0.502, 0.553] | 0.485 (2708) [0.471, 0.500] | 0.484 (5220) [0.473, 0.495] | 0.478 (3230) [0.464, 0.493] | 0.556 (27) | 0.187 | flat +0.009 (noise 0.033) |
| reversal_k5_now | 0.808 (47) | 0.821 (390) [0.806, 0.836] | 0.821 (1621) [0.811, 0.829] | 0.828 (3570) [0.820, 0.837] | 0.821 (1959) [0.811, 0.830] | 0.789 (19) | 0.187 | flat -0.006 (noise 0.027) |
| reversal_k8_next | 0.383 (60) | 0.443 (377) [0.416, 0.469] | 0.396 (2632) [0.383, 0.410] | 0.395 (5278) [0.384, 0.406] | 0.394 (3172) [0.382, 0.407] | 0.391 (23) | 0.121 | flat +0.035 (noise 0.032) |
| reversal_k8_now | 0.720 (50) | 0.696 (362) [0.674, 0.716] | 0.686 (1534) [0.667, 0.705] | 0.702 (3481) [0.688, 0.715] | 0.691 (1894) [0.673, 0.709] | 0.706 (17) | 0.122 | flat -0.009 (noise 0.034) |
| overall | 0.500 (21576) | 0.506 (153638) [0.504, 0.508] | 0.505 (662175) [0.504, 0.506] | 0.504 (1477559) [0.503, 0.505] | 0.505 (794278) [0.503, 0.506] | 0.507 (6864) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0774, 0.1167] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5261, 'levels': [{'threshold': 0.0774, 'calls_per_day': 145.7, 'win_rate': 0.5804}, {'threshold': 0.1167, 'calls_per_day': 36.6, 'win_rate': 0.6178}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42811, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15039 | 0.339 | 0.526 (14753) | 0.572 (2381) | 0.743 (2514) |
| volatility: normal | 15038 | 0.368 | 0.537 (14967) | 0.617 (1440) | 0.757 (2251) |
| volatility: wild | 15038 | 0.384 | 0.524 (15000) | 0.615 (818) | 0.764 (2095) |
| session: Asia 00-08 | 15355 | 0.363 | 0.535 (15219) | 0.598 (1683) | 0.761 (2273) |
| session: Europe 08-13 | 9300 | 0.358 | 0.534 (9199) | 0.593 (1197) | 0.746 (1530) |
| session: US 13-21 | 14880 | 0.371 | 0.525 (14772) | 0.598 (1185) | 0.754 (2264) |
| session: late 21-24 | 5580 | 0.355 | 0.516 (5530) | 0.575 (574) | 0.749 (793) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.287 | 0.305 | 0.217 | 0.217 | 0.596 | 0.229 | 0.344 | 1.100 |
| 6h | 360 | 0.311 | 0.291 | 0.233 | 0.233 | 0.580 | 0.265 | 0.357 | 1.239 |
| 24h | 1440 | 0.329 | 0.321 | 0.235 | 0.258 | 0.544 | 0.260 | 0.398 | 1.297 |
| 7d | 10080 | 0.364 | 0.360 | 0.275 | 0.307 | 0.526 | 0.261 | 0.467 | 1.313 |
| 30d | 43200 | 0.363 | 0.356 | 0.275 | 0.305 | 0.530 | 0.262 | 0.464 | 1.271 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.287 / 0.596 / 0.800; 2: 0.272 / 0.561 / 0.817; 3: 0.256 / 0.526 / 0.833; 4: 0.268 / 0.526 / 0.900; 5: 0.255 / 0.509 / 0.783; 6: 0.246 / 0.421 / 0.783; 7: 0.228 / 0.404 / 0.750; 8: 0.250 / 0.474 / 0.767; 9: 0.288 / 0.596 / 0.650; 10: 0.250 / 0.474 / 0.700; 11: 0.267 / 0.561 / 0.700; 12: 0.261 / 0.526 / 0.700; 13: 0.261 / 0.474 / 0.633; 14: 0.252 / 0.439 / 0.667; 15: 0.239 / 0.386 / 0.683
- 6h: 1: 0.311 / 0.580 / 0.875; 2: 0.294 / 0.524 / 0.869; 3: 0.289 / 0.518 / 0.861; 4: 0.286 / 0.515 / 0.889; 5: 0.282 / 0.503 / 0.842; 6: 0.280 / 0.479 / 0.836; 7: 0.283 / 0.485 / 0.836; 8: 0.287 / 0.494 / 0.842; 9: 0.283 / 0.512 / 0.811; 10: 0.296 / 0.518 / 0.825; 11: 0.287 / 0.524 / 0.814; 12: 0.295 / 0.518 / 0.819; 13: 0.278 / 0.464 / 0.786; 14: 0.296 / 0.527 / 0.775; 15: 0.271 / 0.455 / 0.786
- 24h: 1: 0.329 / 0.544 / 0.882; 2: 0.312 / 0.482 / 0.898; 3: 0.310 / 0.506 / 0.894; 4: 0.308 / 0.503 / 0.899; 5: 0.310 / 0.498 / 0.884; 6: 0.304 / 0.482 / 0.885; 7: 0.307 / 0.496 / 0.882; 8: 0.309 / 0.484 / 0.880; 9: 0.311 / 0.512 / 0.872; 10: 0.312 / 0.500 / 0.874; 11: 0.309 / 0.503 / 0.874; 12: 0.314 / 0.515 / 0.874; 13: 0.307 / 0.491 / 0.869; 14: 0.313 / 0.497 / 0.865; 15: 0.308 / 0.490 / 0.870
- 7d: 1: 0.364 / 0.526 / 0.896; 2: 0.353 / 0.492 / 0.899; 3: 0.356 / 0.512 / 0.900; 4: 0.353 / 0.501 / 0.901; 5: 0.353 / 0.504 / 0.899; 6: 0.351 / 0.507 / 0.898; 7: 0.351 / 0.501 / 0.898; 8: 0.350 / 0.500 / 0.898; 9: 0.352 / 0.507 / 0.897; 10: 0.350 / 0.496 / 0.897; 11: 0.350 / 0.502 / 0.897; 12: 0.350 / 0.504 / 0.898; 13: 0.349 / 0.495 / 0.896; 14: 0.350 / 0.503 / 0.896; 15: 0.349 / 0.502 / 0.897
- 30d: 1: 0.363 / 0.530 / 0.897; 2: 0.351 / 0.495 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.499 / 0.900; 8: 0.349 / 0.504 / 0.900; 9: 0.349 / 0.502 / 0.900; 10: 0.349 / 0.504 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.499 / 0.900; 14: 0.347 / 0.501 / 0.899; 15: 0.347 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.051 (body 0.025, range 0.078); 'price stays where it was' would score 0.046; colour right 0.386; typical miss of the close 4.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.080 (body 0.049, range 0.112); 'price stays where it was' would score 0.080; colour right 0.500; typical miss of the close 3.9 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.118 (body 0.082, range 0.153); 'price stays where it was' would score 0.114; colour right 0.507; typical miss of the close 3.9 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.124; colour right 0.501; typical miss of the close 8.4 bp; chain ended on the right side 0.493 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.3 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.3; 2: 0.198 / 5.0; 3: 0.167 / 6.5; 4: 0.131 / 6.8; 5: 0.127 / 7.5; 6: 0.115 / 8.2; 7: 0.111 / 8.5; 8: 0.099 / 9.5; 9: 0.092 / 9.3; 10: 0.092 / 9.8; 11: 0.087 / 10.0; 12: 0.079 / 10.4; 13: 0.074 / 10.7; 14: 0.072 / 11.1; 15: 0.066 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 139909, probability skill vs chance 0.2156, widened contest next: False
  - now: threshold 0.8385, hit rate recent 0.9151 / long run 0.9277
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.279, naive rule 0.502, lift 3.36x
    - 24h: 70 calls (70 a day), hit rate 0.900, chance 0.313, naive rule 0.535, lift 2.88x
    - 7d: 414 calls (59 a day), hit rate 0.908, chance 0.298, naive rule 0.502, lift 3.05x
    - 30d: 1744 calls (58 a day), hit rate 0.931, chance 0.296, naive rule 0.499, lift 3.15x
  - next: threshold 0.5656, hit rate recent 0.5878 / long run 0.6045
    - 6h: 21 calls (85 a day), hit rate 0.571, chance 0.279, lift 2.05x
    - 24h: 57 calls (57 a day), hit rate 0.561, chance 0.313, lift 1.79x
    - 7d: 489 calls (70 a day), hit rate 0.624, chance 0.298, lift 2.09x
    - 30d: 2973 calls (99 a day), hit rate 0.590, chance 0.296, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.502; 0.35: 533, 0.527; 0.40: 474, 0.583; 0.45: 406, 0.653; 0.50: 355, 0.701; 0.55: 308, 0.744; 0.60: 260, 0.788; 0.65: 219, 0.812; 0.70: 173, 0.844; 0.75: 139, 0.875; 0.80: 92, 0.907; 0.85: 46, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.431; 0.35: 499, 0.465; 0.40: 401, 0.502; 0.45: 303, 0.537; 0.50: 196, 0.570; 0.55: 89, 0.577; 0.60: 12, 0.658; 0.65: 1, 0.565
- **K=5**: model 1792540800, labels learned 139907, probability skill vs chance 0.2061, widened contest next: False
  - now: threshold 0.6861, hit rate recent 0.8172 / long run 0.8207
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.203, naive rule 0.425, lift 4.23x
    - 24h: 56 calls (56 a day), hit rate 0.821, chance 0.200, naive rule 0.427, lift 4.12x
    - 7d: 389 calls (56 a day), hit rate 0.817, chance 0.188, naive rule 0.410, lift 4.34x
    - 30d: 1625 calls (54 a day), hit rate 0.820, chance 0.188, naive rule 0.409, lift 4.37x
  - next: threshold 0.4527, hit rate recent 0.5218 / long run 0.5146
    - 6h: 22 calls (90 a day), hit rate 0.545, chance 0.203, lift 2.69x
    - 24h: 69 calls (69 a day), hit rate 0.536, chance 0.200, lift 2.69x
    - 7d: 398 calls (57 a day), hit rate 0.538, chance 0.188, lift 2.86x
    - 30d: 2713 calls (90 a day), hit rate 0.486, chance 0.188, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.425; 0.35: 349, 0.490; 0.40: 282, 0.562; 0.45: 231, 0.612; 0.50: 186, 0.661; 0.55: 149, 0.698; 0.60: 113, 0.747; 0.65: 76, 0.786; 0.70: 48, 0.824; 0.75: 29, 0.856; 0.80: 11, 0.873
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.384; 0.35: 257, 0.422; 0.40: 160, 0.463; 0.45: 67, 0.491; 0.50: 11, 0.518; 0.55: 1, 0.436
- **K=8**: model 1794096000, labels learned 139904, probability skill vs chance 0.1931, widened contest next: False
  - now: threshold 0.5718, hit rate recent 0.7209 / long run 0.6971
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.114, naive rule 0.284, lift 6.25x
    - 24h: 58 calls (58 a day), hit rate 0.741, chance 0.129, naive rule 0.340, lift 5.76x
    - 7d: 360 calls (51 a day), hit rate 0.694, chance 0.123, naive rule 0.345, lift 5.65x
    - 30d: 1539 calls (51 a day), hit rate 0.687, chance 0.121, naive rule 0.337, lift 5.67x
  - next: threshold 0.3575, hit rate recent 0.3985 / long run 0.4201
    - 6h: 20 calls (82 a day), hit rate 0.350, chance 0.114, lift 3.06x
    - 24h: 65 calls (65 a day), hit rate 0.385, chance 0.129, lift 2.99x
    - 7d: 387 calls (55 a day), hit rate 0.439, chance 0.123, lift 3.57x
    - 30d: 2629 calls (88 a day), hit rate 0.396, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 191, 0.494; 0.40: 152, 0.540; 0.45: 117, 0.588; 0.50: 85, 0.639; 0.55: 60, 0.676; 0.60: 40, 0.713; 0.65: 24, 0.780; 0.70: 12, 0.805; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.363; 0.35: 88, 0.391; 0.40: 24, 0.422; 0.45: 4, 0.449; 0.50: 1, 0.708
- **K=13**: model 1794096000, labels learned 139899, probability skill vs chance 0.1798, widened contest next: True
  - now: threshold 0.4347, hit rate recent 0.5902 / long run 0.5717
    - 6h: 10 calls (42 a day), hit rate 0.700, chance 0.088, naive rule 0.293, lift 7.92x
    - 24h: 46 calls (46 a day), hit rate 0.587, chance 0.078, naive rule 0.274, lift 7.50x
    - 7d: 367 calls (53 a day), hit rate 0.569, chance 0.079, naive rule 0.288, lift 7.23x
    - 30d: 1645 calls (55 a day), hit rate 0.564, chance 0.078, naive rule 0.282, lift 7.25x
  - next: threshold 0.2849, hit rate recent 0.2816 / long run 0.3263
    - 6h: 22 calls (92 a day), hit rate 0.273, chance 0.088, lift 3.08x
    - 24h: 74 calls (75 a day), hit rate 0.257, chance 0.078, lift 3.28x
    - 7d: 392 calls (56 a day), hit rate 0.337, chance 0.079, lift 4.27x
    - 30d: 1814 calls (60 a day), hit rate 0.324, chance 0.078, lift 4.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.436; 0.35: 94, 0.485; 0.40: 66, 0.545; 0.45: 45, 0.587; 0.50: 30, 0.646; 0.55: 20, 0.674; 0.60: 11, 0.713; 0.65: 4, 0.673; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.340; 0.40: 3, 0.400; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.338 | 1.02% | 0.800 | 0.517 | 0.246 | 0.684 | 0.320 |
| 6h | 5.477 | 1.74% | 0.889 | 0.508 | 0.251 | 0.500 | 0.457 |
| 24h | 6.339 | 5.15% | 0.895 | 0.500 | 0.250 | 0.519 | 0.379 |
| 7d | 15.036 | 5.04% | 0.900 | 0.500 | 0.250 | 0.506 | 0.748 |
| 30d | 14.884 | 4.46% | 0.900 | 0.500 | 0.250 | 0.500 | 0.710 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.393 | 5.366 | 5.326 | 5.491 | 5.423 | 5.709 | 5.379 | 5.327 | 5.340 | 5.338 |
| 6h | 5.575 | 5.499 | 5.489 | 5.520 | 5.559 | 5.832 | 5.497 | 5.477 | 5.468 | 5.477 |
| 24h | 6.683 | 6.403 | 6.434 | 6.382 | 6.503 | 6.878 | 6.339 | 6.323 | 6.328 | 6.339 |
| 7d | 15.834 | 15.159 | 15.136 | 15.088 | 15.306 | 15.410 | 15.019 | 15.013 | 15.009 | 15.036 |
| 30d | 15.579 | 15.037 | 14.983 | 14.914 | 15.163 | 15.129 | 14.874 | 14.854 | 14.856 | 14.884 |

## Next candle

- candle starting 2026-11-08 07:55 UTC, last close 2238.1
- P(up) 0.4995, return quantiles (bp): {'05': -3.96, '10': -2.865, '25': -1.483, '40': -0.407, '50': -0.004, '60': 0.433, '75': 1.356, '90': 3.034, '95': 4.258}
- changepoint probability 0.6047, regime age 13.9 min
- agent weights: empirical 0.026, ewma 0.146, garch 0.147, har 0.137, bocpd 0.054, hmm 0.004, online_qr 0.214, lgbm 0.273

## Learning log

- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.87, 6.46, 18.11], current probabilities: [0.973, 0.026, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-08 08:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.189, 'l_abs': 0.625, 'l_hi': 0.73, 'l_lo': 0.707, 'b05': 0.617, 'b25': 0.604, 'b75': 0.579, 'b95': 0.637}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.697, 2.211, 2.224, 3.043, 3.546, 3.762, 4.03, 5.026, 4.803, 5.36, 5.283, 7.004, 7.58, 7.554]}
- calibration offsets (in sigma): {'05': 0.017, '10': 0.034, '25': 0.055, '40': 0.096, '50': 0.06, '60': 0.034, '75': 0.005, '90': 0.016, '95': -0.007}
