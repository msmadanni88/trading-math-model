# ETH-USD 60s candle generator - report

- generated: 2026-11-08 01:32 UTC
- last closed candle: 2026-11-08 01:32 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.490 (672) [0.455, 0.518] | 0.517 (2879) [0.501, 0.534] | 0.513 (6426) [0.501, 0.525] | 0.514 (3454) [0.497, 0.532] | 0.667 (6) | 0.500 | flat -0.034 (noise 0.029) |
| colour_clear | 0.556 (741) | 0.532 (5546) [0.515, 0.550] | 0.542 (23847) [0.536, 0.548] | 0.522 (52595) [0.516, 0.527] | 0.543 (28357) [0.538, 0.548] | 0.549 (51) | 0.500 | flat -0.009 (noise 0.012) |
| colour_confident | 0.577 (253) | 0.577 (957) [0.561, 0.598] | 0.594 (4425) [0.584, 0.604] | 0.596 (5240) [0.585, 0.607] | 0.596 (5240) [0.585, 0.607] | 0.562 (16) | 0.500 | flat -0.010 (noise 0.022) |
| colour_next | 0.531 (1402) | 0.527 (9985) [0.517, 0.536] | 0.529 (42842) [0.525, 0.533] | 0.516 (95733) [0.512, 0.520] | 0.529 (51384) [0.526, 0.533] | 0.541 (85) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.496 (19628) | 0.502 (139790) [0.500, 0.504] | 0.501 (599788) [0.500, 0.503] | 0.501 (1340262) [0.500, 0.502] | 0.501 (719376) [0.500, 0.502] | 0.482 (1190) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.650 (80) | 0.615 (226) [0.577, 0.640] | 0.630 (1164) [0.612, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.500 (4) | 0.500 | flat +0.011 (noise 0.042) |
| reversal_k13_next | 0.269 (67) | 0.344 (378) [0.311, 0.376] | 0.325 (1810) [0.311, 0.340] | 0.313 (4382) [0.302, 0.323] | 0.325 (2277) [0.313, 0.337] | 0.000 (5) | 0.077 | flat +0.004 (noise 0.034) |
| reversal_k13_now | 0.511 (47) | 0.566 (378) [0.529, 0.602] | 0.563 (1648) [0.544, 0.583] | 0.573 (3459) [0.560, 0.586] | 0.567 (1987) [0.549, 0.585] | 1.000 (1) | 0.077 | flat -0.011 (noise 0.035) |
| reversal_k3_next | 0.618 (55) | 0.620 (508) [0.590, 0.645] | 0.590 (2972) [0.579, 0.602] | 0.587 (5899) [0.578, 0.596] | 0.588 (3459) [0.577, 0.598] | 0.500 (4) | 0.294 | flat +0.033 (noise 0.028) |
| reversal_k3_now | 0.900 (60) | 0.909 (408) [0.902, 0.918] | 0.932 (1741) [0.921, 0.942] | 0.936 (3849) [0.930, 0.942] | 0.931 (2086) [0.922, 0.940] | 1.000 (3) | 0.294 | flat -0.036 (noise 0.018) |
| reversal_k5_next | 0.484 (64) | 0.528 (390) [0.502, 0.553] | 0.485 (2708) [0.471, 0.500] | 0.484 (5220) [0.473, 0.495] | 0.478 (3230) [0.464, 0.493] | 0.600 (5) | 0.187 | flat +0.009 (noise 0.033) |
| reversal_k5_now | 0.808 (47) | 0.821 (390) [0.806, 0.836] | 0.821 (1621) [0.811, 0.829] | 0.828 (3570) [0.820, 0.837] | 0.821 (1959) [0.811, 0.830] | 0.667 (3) | 0.187 | flat -0.006 (noise 0.027) |
| reversal_k8_next | 0.383 (60) | 0.443 (377) [0.416, 0.469] | 0.396 (2632) [0.383, 0.410] | 0.395 (5278) [0.384, 0.406] | 0.394 (3172) [0.382, 0.407] | 0.667 (3) | 0.121 | flat +0.035 (noise 0.032) |
| reversal_k8_now | 0.720 (50) | 0.696 (362) [0.674, 0.716] | 0.686 (1534) [0.667, 0.705] | 0.702 (3481) [0.688, 0.715] | 0.691 (1894) [0.673, 0.709] | 0.500 (2) | 0.122 | flat -0.009 (noise 0.034) |
| overall | 0.500 (21576) | 0.506 (153638) [0.504, 0.508] | 0.505 (662175) [0.504, 0.506] | 0.504 (1477559) [0.503, 0.505] | 0.505 (794278) [0.503, 0.506] | 0.488 (1307) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07704, 0.1163] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.07704, 'calls_per_day': 144.5, 'win_rate': 0.5769}, {'threshold': 0.1163, 'calls_per_day': 35.8, 'win_rate': 0.6285}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42834, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14911 | 0.341 | 0.526 (14648) | 0.572 (2316) | 0.741 (2492) |
| volatility: normal | 14910 | 0.368 | 0.536 (14840) | 0.616 (1402) | 0.754 (2232) |
| volatility: wild | 14911 | 0.384 | 0.524 (14873) | 0.617 (812) | 0.768 (2076) |
| session: Asia 00-08 | 14972 | 0.364 | 0.534 (14860) | 0.598 (1574) | 0.759 (2213) |
| session: Europe 08-13 | 9300 | 0.358 | 0.534 (9199) | 0.593 (1197) | 0.746 (1530) |
| session: US 13-21 | 14880 | 0.371 | 0.525 (14772) | 0.598 (1185) | 0.754 (2264) |
| session: late 21-24 | 5580 | 0.355 | 0.516 (5530) | 0.575 (574) | 0.749 (793) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.336 | 0.332 | 0.208 | 0.208 | 0.545 | 0.285 | 0.387 | 1.173 |
| 6h | 360 | 0.348 | 0.337 | 0.232 | 0.261 | 0.555 | 0.276 | 0.420 | 1.214 |
| 24h | 1440 | 0.333 | 0.332 | 0.237 | 0.267 | 0.532 | 0.254 | 0.411 | 1.317 |
| 7d | 10080 | 0.364 | 0.360 | 0.275 | 0.308 | 0.526 | 0.260 | 0.468 | 1.294 |
| 30d | 43200 | 0.364 | 0.356 | 0.275 | 0.306 | 0.529 | 0.262 | 0.465 | 1.264 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.336 / 0.545 / 0.900; 2: 0.348 / 0.582 / 0.917; 3: 0.319 / 0.582 / 0.917; 4: 0.330 / 0.582 / 0.883; 5: 0.296 / 0.491 / 0.950; 6: 0.282 / 0.418 / 0.917; 7: 0.288 / 0.400 / 0.867; 8: 0.303 / 0.455 / 0.867; 9: 0.343 / 0.545 / 0.883; 10: 0.297 / 0.473 / 0.900; 11: 0.343 / 0.509 / 0.933; 12: 0.308 / 0.509 / 0.950; 13: 0.340 / 0.509 / 0.917; 14: 0.284 / 0.436 / 0.933; 15: 0.311 / 0.455 / 0.917
- 6h: 1: 0.348 / 0.555 / 0.881; 2: 0.335 / 0.497 / 0.892; 3: 0.319 / 0.477 / 0.878; 4: 0.327 / 0.520 / 0.864; 5: 0.322 / 0.474 / 0.900; 6: 0.309 / 0.474 / 0.892; 7: 0.319 / 0.486 / 0.894; 8: 0.318 / 0.460 / 0.883; 9: 0.326 / 0.480 / 0.928; 10: 0.317 / 0.471 / 0.925; 11: 0.329 / 0.506 / 0.911; 12: 0.321 / 0.500 / 0.928; 13: 0.321 / 0.454 / 0.911; 14: 0.327 / 0.494 / 0.919; 15: 0.325 / 0.506 / 0.906
- 24h: 1: 0.333 / 0.532 / 0.879; 2: 0.318 / 0.468 / 0.901; 3: 0.319 / 0.501 / 0.901; 4: 0.320 / 0.507 / 0.899; 5: 0.322 / 0.504 / 0.906; 6: 0.313 / 0.484 / 0.901; 7: 0.316 / 0.497 / 0.901; 8: 0.319 / 0.486 / 0.899; 9: 0.323 / 0.514 / 0.908; 10: 0.318 / 0.491 / 0.908; 11: 0.319 / 0.494 / 0.908; 12: 0.320 / 0.505 / 0.906; 13: 0.314 / 0.481 / 0.909; 14: 0.316 / 0.483 / 0.912; 15: 0.319 / 0.498 / 0.912
- 7d: 1: 0.364 / 0.526 / 0.896; 2: 0.353 / 0.489 / 0.900; 3: 0.356 / 0.513 / 0.900; 4: 0.353 / 0.500 / 0.900; 5: 0.354 / 0.506 / 0.900; 6: 0.352 / 0.508 / 0.900; 7: 0.351 / 0.500 / 0.900; 8: 0.350 / 0.500 / 0.900; 9: 0.352 / 0.506 / 0.900; 10: 0.350 / 0.497 / 0.901; 11: 0.350 / 0.501 / 0.901; 12: 0.350 / 0.503 / 0.901; 13: 0.350 / 0.497 / 0.901; 14: 0.350 / 0.501 / 0.901; 15: 0.350 / 0.506 / 0.901
- 30d: 1: 0.364 / 0.529 / 0.898; 2: 0.352 / 0.494 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.349 / 0.499 / 0.900; 8: 0.349 / 0.504 / 0.900; 9: 0.349 / 0.502 / 0.900; 10: 0.350 / 0.504 / 0.900; 11: 0.347 / 0.498 / 0.900; 12: 0.349 / 0.503 / 0.900; 13: 0.348 / 0.499 / 0.900; 14: 0.347 / 0.501 / 0.900; 15: 0.348 / 0.503 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.125 (body 0.097, range 0.153); 'price stays where it was' would score 0.138; colour right 0.527; typical miss of the close 4.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.141 (body 0.103, range 0.180); 'price stays where it was' would score 0.129; colour right 0.486; typical miss of the close 3.9 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.125 (body 0.089, range 0.162); 'price stays where it was' would score 0.118; colour right 0.512; typical miss of the close 4.0 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.124 (body 0.084, range 0.163); 'price stays where it was' would score 0.124; colour right 0.501; typical miss of the close 8.6 bp; chain ended on the right side 0.493 of 672 chains; n=10080
- 30d: match 0.125 (body 0.086, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.3 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.3; 2: 0.198 / 5.0; 3: 0.167 / 6.6; 4: 0.131 / 6.8; 5: 0.128 / 7.5; 6: 0.115 / 8.3; 7: 0.112 / 8.5; 8: 0.099 / 9.6; 9: 0.092 / 9.4; 10: 0.092 / 9.9; 11: 0.087 / 10.1; 12: 0.079 / 10.5; 13: 0.073 / 10.8; 14: 0.072 / 11.2; 15: 0.066 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 139526, probability skill vs chance 0.2126, widened contest next: False
  - now: threshold 0.8377, hit rate recent 0.9035 / long run 0.9271
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.311, naive rule 0.531, lift 2.52x
    - 24h: 61 calls (61 a day), hit rate 0.902, chance 0.321, naive rule 0.544, lift 2.81x
    - 7d: 406 calls (58 a day), hit rate 0.909, chance 0.297, naive rule 0.501, lift 3.06x
    - 30d: 1741 calls (58 a day), hit rate 0.932, chance 0.296, naive rule 0.499, lift 3.15x
  - next: threshold 0.5653, hit rate recent 0.6062 / long run 0.6067
    - 6h: 12 calls (49 a day), hit rate 0.500, chance 0.311, lift 1.61x
    - 24h: 54 calls (54 a day), hit rate 0.611, chance 0.321, lift 1.91x
    - 7d: 503 calls (72 a day), hit rate 0.616, chance 0.297, lift 2.07x
    - 30d: 2972 calls (99 a day), hit rate 0.590, chance 0.296, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.502; 0.35: 534, 0.527; 0.40: 474, 0.583; 0.45: 406, 0.653; 0.50: 355, 0.702; 0.55: 308, 0.745; 0.60: 260, 0.788; 0.65: 219, 0.814; 0.70: 173, 0.845; 0.75: 139, 0.876; 0.80: 92, 0.907; 0.85: 46, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.431; 0.35: 499, 0.465; 0.40: 402, 0.501; 0.45: 304, 0.537; 0.50: 196, 0.570; 0.55: 88, 0.577; 0.60: 12, 0.663; 0.65: 1, 0.600
- **K=5**: model 1792540800, labels learned 139524, probability skill vs chance 0.2085, widened contest next: False
  - now: threshold 0.6861, hit rate recent 0.8182 / long run 0.8209
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.183, naive rule 0.436, lift 4.21x
    - 24h: 47 calls (47 a day), hit rate 0.809, chance 0.193, naive rule 0.426, lift 4.18x
    - 7d: 387 calls (55 a day), hit rate 0.817, chance 0.187, naive rule 0.410, lift 4.36x
    - 30d: 1621 calls (54 a day), hit rate 0.820, chance 0.188, naive rule 0.409, lift 4.37x
  - next: threshold 0.4507, hit rate recent 0.5115 / long run 0.5134
    - 6h: 16 calls (65 a day), hit rate 0.438, chance 0.183, lift 2.39x
    - 24h: 63 calls (63 a day), hit rate 0.492, chance 0.193, lift 2.55x
    - 7d: 393 calls (56 a day), hit rate 0.529, chance 0.187, lift 2.83x
    - 30d: 2709 calls (90 a day), hit rate 0.485, chance 0.188, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.425; 0.35: 349, 0.490; 0.40: 282, 0.563; 0.45: 231, 0.613; 0.50: 186, 0.663; 0.55: 148, 0.699; 0.60: 113, 0.747; 0.65: 76, 0.786; 0.70: 48, 0.824; 0.75: 29, 0.855; 0.80: 11, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.384; 0.35: 256, 0.422; 0.40: 160, 0.463; 0.45: 67, 0.490; 0.50: 11, 0.517; 0.55: 1, 0.432
- **K=8**: model 1794096000, labels learned 139521, probability skill vs chance 0.1958, widened contest next: False
  - now: threshold 0.5711, hit rate recent 0.7158 / long run 0.6961
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.134, naive rule 0.370, lift 4.96x
    - 24h: 49 calls (49 a day), hit rate 0.714, chance 0.132, naive rule 0.363, lift 5.42x
    - 7d: 359 calls (51 a day), hit rate 0.694, chance 0.123, naive rule 0.346, lift 5.62x
    - 30d: 1533 calls (51 a day), hit rate 0.687, chance 0.121, naive rule 0.338, lift 5.67x
  - next: threshold 0.3573, hit rate recent 0.4227 / long run 0.4226
    - 6h: 12 calls (49 a day), hit rate 0.417, chance 0.134, lift 3.10x
    - 24h: 61 calls (61 a day), hit rate 0.393, chance 0.132, lift 2.98x
    - 7d: 377 calls (54 a day), hit rate 0.443, chance 0.123, lift 3.59x
    - 30d: 2631 calls (88 a day), hit rate 0.396, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.434; 0.35: 191, 0.496; 0.40: 152, 0.541; 0.45: 117, 0.589; 0.50: 85, 0.639; 0.55: 60, 0.676; 0.60: 40, 0.712; 0.65: 24, 0.782; 0.70: 12, 0.805; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.363; 0.35: 88, 0.391; 0.40: 24, 0.423; 0.45: 4, 0.448; 0.50: 1, 0.708
- **K=13**: model 1794096000, labels learned 139516, probability skill vs chance 0.1734, widened contest next: True
  - now: threshold 0.4431, hit rate recent 0.5675 / long run 0.5695
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.071, naive rule 0.258, lift 8.05x
    - 24h: 45 calls (45 a day), hit rate 0.511, chance 0.073, naive rule 0.264, lift 6.97x
    - 7d: 372 calls (53 a day), hit rate 0.570, chance 0.079, naive rule 0.286, lift 7.26x
    - 30d: 1646 calls (55 a day), hit rate 0.564, chance 0.078, naive rule 0.282, lift 7.26x
  - next: threshold 0.2843, hit rate recent 0.2726 / long run 0.3272
    - 6h: 16 calls (67 a day), hit rate 0.125, chance 0.071, lift 1.76x
    - 24h: 69 calls (70 a day), hit rate 0.246, chance 0.073, lift 3.36x
    - 7d: 380 calls (54 a day), hit rate 0.339, chance 0.079, lift 4.32x
    - 30d: 1812 calls (60 a day), hit rate 0.325, chance 0.078, lift 4.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.437; 0.35: 94, 0.485; 0.40: 66, 0.544; 0.45: 45, 0.588; 0.50: 30, 0.646; 0.55: 20, 0.676; 0.60: 11, 0.712; 0.65: 4, 0.673; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.329; 0.35: 12, 0.346; 0.40: 3, 0.420; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.082 | 1.68% | 0.900 | 0.467 | 0.248 | 0.618 | -0.005 |
| 6h | 6.839 | 1.03% | 0.897 | 0.456 | 0.250 | 0.506 | 0.401 |
| 24h | 6.700 | 9.79% | 0.892 | 0.498 | 0.249 | 0.533 | 0.350 |
| 7d | 15.108 | 5.02% | 0.900 | 0.499 | 0.250 | 0.505 | 0.746 |
| 30d | 14.935 | 4.48% | 0.900 | 0.500 | 0.250 | 0.500 | 0.709 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.168 | 5.071 | 5.097 | 5.143 | 5.208 | 5.395 | 5.084 | 5.045 | 5.068 | 5.082 |
| 6h | 6.911 | 6.883 | 6.855 | 6.861 | 6.971 | 7.146 | 6.830 | 6.815 | 6.816 | 6.839 |
| 24h | 7.427 | 6.765 | 6.853 | 6.748 | 6.873 | 7.337 | 6.698 | 6.683 | 6.691 | 6.700 |
| 7d | 15.907 | 15.233 | 15.209 | 15.159 | 15.382 | 15.476 | 15.091 | 15.085 | 15.081 | 15.108 |
| 30d | 15.636 | 15.089 | 15.036 | 14.966 | 15.216 | 15.178 | 14.926 | 14.904 | 14.908 | 14.935 |

## Next candle

- candle starting 2026-11-08 01:32 UTC, last close 2232.09
- P(up) 0.5038, return quantiles (bp): {'05': -3.457, '10': -2.594, '25': -1.181, '40': -0.328, '50': 0.014, '60': 0.321, '75': 1.2, '90': 2.511, '95': 3.363}
- changepoint probability 0.0259, regime age 128.6 min
- agent weights: empirical 0.011, ewma 0.107, garch 0.102, har 0.171, bocpd 0.035, hmm 0.004, online_qr 0.253, lgbm 0.317

## Learning log

- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.87, 6.46, 18.11], current probabilities: [0.987, 0.012, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-08 01:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.217, 'l_abs': 0.644, 'l_hi': 0.727, 'l_lo': 0.687, 'b05': 0.643, 'b25': 0.612, 'b75': 0.596, 'b95': 0.655}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.397, 1.749, 2.149, 2.093, 2.298, 2.487, 2.772, 2.666, 2.873, 3.019, 3.097, 3.23, 3.227, 3.483]}
- calibration offsets (in sigma): {'05': -0.0045, '10': -0.029, '25': 0.0175, '40': 0.044, '50': -0.005, '60': -0.044, '75': 0.0125, '90': -0.021, '95': -0.0555}
