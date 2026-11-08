# ETH-USD 60s candle generator - report

- generated: 2026-11-08 14:51 UTC
- last closed candle: 2026-11-08 14:51 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.542 (96) | 0.490 (672) [0.455, 0.518] | 0.517 (2879) [0.501, 0.534] | 0.513 (6426) [0.501, 0.525] | 0.514 (3454) [0.497, 0.532] | 0.576 (59) | 0.500 | flat -0.034 (noise 0.029) |
| colour_clear | 0.556 (741) | 0.532 (5546) [0.515, 0.550] | 0.542 (23847) [0.536, 0.548] | 0.522 (52595) [0.516, 0.527] | 0.543 (28357) [0.538, 0.548] | 0.566 (486) | 0.500 | flat -0.009 (noise 0.012) |
| colour_confident | 0.577 (253) | 0.577 (957) [0.561, 0.598] | 0.594 (4425) [0.584, 0.604] | 0.596 (5240) [0.585, 0.607] | 0.596 (5240) [0.585, 0.607] | 0.564 (234) | 0.500 | flat -0.010 (noise 0.022) |
| colour_next | 0.531 (1402) | 0.527 (9985) [0.517, 0.536] | 0.529 (42842) [0.525, 0.533] | 0.516 (95733) [0.512, 0.520] | 0.529 (51384) [0.526, 0.533] | 0.559 (848) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.496 (19628) | 0.502 (139790) [0.500, 0.504] | 0.501 (599788) [0.500, 0.503] | 0.501 (1340262) [0.500, 0.502] | 0.501 (719376) [0.500, 0.502] | 0.504 (11872) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.650 (80) | 0.615 (226) [0.577, 0.640] | 0.630 (1164) [0.612, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.630 (1383) [0.613, 0.649] | 0.635 (85) | 0.500 | flat +0.011 (noise 0.042) |
| reversal_k13_next | 0.269 (67) | 0.344 (378) [0.311, 0.376] | 0.325 (1810) [0.311, 0.340] | 0.313 (4382) [0.302, 0.323] | 0.325 (2277) [0.313, 0.337] | 0.250 (60) | 0.077 | flat +0.004 (noise 0.034) |
| reversal_k13_now | 0.511 (47) | 0.566 (378) [0.529, 0.602] | 0.563 (1648) [0.544, 0.583] | 0.573 (3459) [0.560, 0.586] | 0.567 (1987) [0.549, 0.585] | 0.559 (34) | 0.077 | flat -0.011 (noise 0.035) |
| reversal_k3_next | 0.618 (55) | 0.620 (508) [0.590, 0.645] | 0.590 (2972) [0.579, 0.602] | 0.587 (5899) [0.578, 0.596] | 0.588 (3459) [0.577, 0.598] | 0.596 (47) | 0.294 | flat +0.033 (noise 0.028) |
| reversal_k3_now | 0.900 (60) | 0.909 (408) [0.902, 0.918] | 0.932 (1741) [0.921, 0.942] | 0.936 (3849) [0.930, 0.942] | 0.931 (2086) [0.922, 0.940] | 0.944 (36) | 0.294 | flat -0.036 (noise 0.018) |
| reversal_k5_next | 0.484 (64) | 0.528 (390) [0.502, 0.553] | 0.485 (2708) [0.471, 0.500] | 0.484 (5220) [0.473, 0.495] | 0.478 (3230) [0.464, 0.493] | 0.510 (51) | 0.187 | flat +0.009 (noise 0.033) |
| reversal_k5_now | 0.808 (47) | 0.821 (390) [0.806, 0.836] | 0.821 (1621) [0.811, 0.829] | 0.828 (3570) [0.820, 0.837] | 0.821 (1959) [0.811, 0.830] | 0.697 (33) | 0.187 | flat -0.006 (noise 0.027) |
| reversal_k8_next | 0.383 (60) | 0.443 (377) [0.416, 0.469] | 0.396 (2632) [0.383, 0.410] | 0.395 (5278) [0.384, 0.406] | 0.394 (3172) [0.382, 0.407] | 0.333 (54) | 0.121 | flat +0.035 (noise 0.032) |
| reversal_k8_now | 0.720 (50) | 0.696 (362) [0.674, 0.716] | 0.686 (1534) [0.667, 0.705] | 0.702 (3481) [0.688, 0.715] | 0.691 (1894) [0.673, 0.709] | 0.618 (34) | 0.122 | flat -0.009 (noise 0.034) |
| overall | 0.500 (21576) | 0.506 (153638) [0.504, 0.508] | 0.505 (662175) [0.504, 0.506] | 0.504 (1477559) [0.503, 0.505] | 0.505 (794278) [0.503, 0.506] | 0.509 (13128) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07794, 0.1176] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5259, 'levels': [{'threshold': 0.07794, 'calls_per_day': 146.9, 'win_rate': 0.5731}, {'threshold': 0.1176, 'calls_per_day': 37.4, 'win_rate': 0.6189}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42799, 'rate': 0.5297}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15177 | 0.339 | 0.528 (14880) | 0.570 (2453) | 0.738 (2527) |
| volatility: normal | 15177 | 0.367 | 0.536 (15106) | 0.618 (1464) | 0.756 (2275) |
| volatility: wild | 15177 | 0.384 | 0.524 (15138) | 0.613 (831) | 0.765 (2126) |
| session: Asia 00-08 | 15360 | 0.363 | 0.535 (15224) | 0.598 (1684) | 0.761 (2275) |
| session: Europe 08-13 | 9600 | 0.356 | 0.534 (9489) | 0.591 (1280) | 0.744 (1570) |
| session: US 13-21 | 14991 | 0.371 | 0.525 (14881) | 0.594 (1210) | 0.751 (2290) |
| session: late 21-24 | 5580 | 0.355 | 0.516 (5530) | 0.575 (574) | 0.749 (793) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.398 | 0.340 | 0.281 | 0.281 | 0.593 | 0.317 | 0.479 | 1.166 |
| 6h | 360 | 0.328 | 0.316 | 0.222 | 0.259 | 0.541 | 0.254 | 0.402 | 1.074 |
| 24h | 1440 | 0.332 | 0.317 | 0.232 | 0.253 | 0.561 | 0.265 | 0.399 | 1.209 |
| 7d | 10080 | 0.364 | 0.359 | 0.274 | 0.306 | 0.527 | 0.261 | 0.467 | 1.317 |
| 30d | 43200 | 0.363 | 0.355 | 0.274 | 0.305 | 0.530 | 0.262 | 0.463 | 1.276 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.398 / 0.593 / 0.900; 2: 0.368 / 0.542 / 0.933; 3: 0.403 / 0.610 / 1.000; 4: 0.363 / 0.525 / 0.967; 5: 0.414 / 0.593 / 1.000; 6: 0.377 / 0.542 / 1.000; 7: 0.382 / 0.576 / 1.000; 8: 0.391 / 0.576 / 1.000; 9: 0.396 / 0.576 / 1.000; 10: 0.350 / 0.492 / 1.000; 11: 0.389 / 0.593 / 1.000; 12: 0.389 / 0.576 / 1.000; 13: 0.390 / 0.559 / 1.000; 14: 0.402 / 0.627 / 1.000; 15: 0.409 / 0.644 / 1.000
- 6h: 1: 0.328 / 0.541 / 0.861; 2: 0.314 / 0.504 / 0.919; 3: 0.319 / 0.493 / 0.950; 4: 0.317 / 0.513 / 0.917; 5: 0.327 / 0.516 / 0.961; 6: 0.315 / 0.484 / 0.972; 7: 0.320 / 0.501 / 0.958; 8: 0.320 / 0.482 / 0.964; 9: 0.329 / 0.521 / 0.975; 10: 0.314 / 0.504 / 0.969; 11: 0.331 / 0.547 / 0.961; 12: 0.330 / 0.533 / 0.964; 13: 0.321 / 0.510 / 0.983; 14: 0.323 / 0.524 / 0.986; 15: 0.324 / 0.501 / 0.983
- 24h: 1: 0.332 / 0.561 / 0.885; 2: 0.312 / 0.485 / 0.905; 3: 0.313 / 0.507 / 0.907; 4: 0.309 / 0.501 / 0.901; 5: 0.314 / 0.505 / 0.915; 6: 0.304 / 0.481 / 0.907; 7: 0.310 / 0.494 / 0.911; 8: 0.312 / 0.482 / 0.909; 9: 0.315 / 0.504 / 0.917; 10: 0.313 / 0.505 / 0.924; 11: 0.313 / 0.510 / 0.906; 12: 0.318 / 0.524 / 0.918; 13: 0.309 / 0.488 / 0.905; 14: 0.317 / 0.512 / 0.908; 15: 0.309 / 0.498 / 0.901
- 7d: 1: 0.364 / 0.527 / 0.895; 2: 0.353 / 0.492 / 0.900; 3: 0.356 / 0.511 / 0.900; 4: 0.353 / 0.503 / 0.899; 5: 0.353 / 0.503 / 0.900; 6: 0.351 / 0.505 / 0.900; 7: 0.351 / 0.501 / 0.900; 8: 0.350 / 0.499 / 0.899; 9: 0.352 / 0.506 / 0.899; 10: 0.350 / 0.498 / 0.899; 11: 0.351 / 0.504 / 0.898; 12: 0.351 / 0.506 / 0.899; 13: 0.349 / 0.494 / 0.898; 14: 0.351 / 0.505 / 0.898; 15: 0.350 / 0.503 / 0.899
- 30d: 1: 0.363 / 0.530 / 0.897; 2: 0.351 / 0.495 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.348 / 0.501 / 0.900; 7: 0.349 / 0.499 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.349 / 0.502 / 0.900; 10: 0.349 / 0.504 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.348 / 0.504 / 0.900; 13: 0.347 / 0.499 / 0.900; 14: 0.347 / 0.501 / 0.900; 15: 0.347 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.109 (body 0.061, range 0.158); 'price stays where it was' would score 0.127; colour right 0.576; typical miss of the close 6.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.127 (body 0.093, range 0.161); 'price stays where it was' would score 0.118; colour right 0.487; typical miss of the close 3.9 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.117 (body 0.083, range 0.151); 'price stays where it was' would score 0.113; colour right 0.492; typical miss of the close 3.9 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.123 (body 0.084, range 0.163); 'price stays where it was' would score 0.124; colour right 0.503; typical miss of the close 8.3 bp; chain ended on the right side 0.499 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.129; colour right 0.501; typical miss of the close 8.2 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.3; 2: 0.198 / 5.0; 3: 0.167 / 6.4; 4: 0.131 / 6.7; 5: 0.127 / 7.4; 6: 0.115 / 8.1; 7: 0.111 / 8.3; 8: 0.098 / 9.3; 9: 0.091 / 9.3; 10: 0.092 / 9.7; 11: 0.087 / 9.9; 12: 0.079 / 10.4; 13: 0.074 / 10.6; 14: 0.072 / 11.1; 15: 0.066 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 140325, probability skill vs chance 0.2095, widened contest next: False
  - now: threshold 0.8385, hit rate recent 0.9183 / long run 0.9278
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.296, naive rule 0.502, lift 3.10x
    - 24h: 59 calls (59 a day), hit rate 0.898, chance 0.298, naive rule 0.511, lift 3.01x
    - 7d: 403 calls (58 a day), hit rate 0.918, chance 0.297, naive rule 0.500, lift 3.09x
    - 30d: 1739 calls (58 a day), hit rate 0.931, chance 0.296, naive rule 0.499, lift 3.15x
  - next: threshold 0.5661, hit rate recent 0.6159 / long run 0.6067
    - 6h: 20 calls (81 a day), hit rate 0.700, chance 0.296, lift 2.37x
    - 24h: 61 calls (61 a day), hit rate 0.590, chance 0.298, lift 1.98x
    - 7d: 481 calls (69 a day), hit rate 0.622, chance 0.297, lift 2.09x
    - 30d: 2968 calls (99 a day), hit rate 0.592, chance 0.296, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.502; 0.35: 533, 0.527; 0.40: 474, 0.582; 0.45: 406, 0.652; 0.50: 356, 0.700; 0.55: 309, 0.743; 0.60: 260, 0.786; 0.65: 219, 0.811; 0.70: 173, 0.843; 0.75: 139, 0.874; 0.80: 92, 0.906; 0.85: 46, 0.945; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 590, 0.430; 0.35: 499, 0.465; 0.40: 402, 0.502; 0.45: 304, 0.537; 0.50: 196, 0.570; 0.55: 89, 0.579; 0.60: 12, 0.658; 0.65: 1, 0.600
- **K=5**: model 1792540800, labels learned 140323, probability skill vs chance 0.2009, widened contest next: True
  - now: threshold 0.686, hit rate recent 0.7643 / long run 0.8149
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.180, naive rule 0.387, lift 3.42x
    - 24h: 48 calls (48 a day), hit rate 0.750, chance 0.193, naive rule 0.417, lift 3.89x
    - 7d: 383 calls (55 a day), hit rate 0.809, chance 0.187, naive rule 0.406, lift 4.32x
    - 30d: 1624 calls (54 a day), hit rate 0.818, chance 0.188, naive rule 0.408, lift 4.36x
  - next: threshold 0.4506, hit rate recent 0.5026 / long run 0.5124
    - 6h: 22 calls (90 a day), hit rate 0.409, chance 0.180, lift 2.27x
    - 24h: 69 calls (69 a day), hit rate 0.522, chance 0.193, lift 2.71x
    - 7d: 407 calls (58 a day), hit rate 0.533, chance 0.187, lift 2.85x
    - 30d: 2711 calls (90 a day), hit rate 0.486, chance 0.188, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 350, 0.489; 0.40: 282, 0.560; 0.45: 232, 0.610; 0.50: 186, 0.659; 0.55: 149, 0.697; 0.60: 113, 0.745; 0.65: 76, 0.785; 0.70: 47, 0.824; 0.75: 28, 0.856; 0.80: 11, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.383; 0.35: 256, 0.422; 0.40: 160, 0.462; 0.45: 67, 0.491; 0.50: 11, 0.527; 0.55: 1, 0.421
- **K=8**: model 1794096000, labels learned 140320, probability skill vs chance 0.1782, widened contest next: True
  - now: threshold 0.5724, hit rate recent 0.6731 / long run 0.6924
    - 6h: 15 calls (62 a day), hit rate 0.533, chance 0.084, naive rule 0.214, lift 6.33x
    - 24h: 50 calls (50 a day), hit rate 0.680, chance 0.117, naive rule 0.310, lift 5.82x
    - 7d: 359 calls (51 a day), hit rate 0.685, chance 0.122, naive rule 0.339, lift 5.64x
    - 30d: 1543 calls (51 a day), hit rate 0.686, chance 0.121, naive rule 0.336, lift 5.68x
  - next: threshold 0.3583, hit rate recent 0.3537 / long run 0.4136
    - 6h: 29 calls (119 a day), hit rate 0.241, chance 0.084, lift 2.86x
    - 24h: 69 calls (69 a day), hit rate 0.377, chance 0.117, lift 3.23x
    - 7d: 406 calls (58 a day), hit rate 0.429, chance 0.122, lift 3.52x
    - 30d: 2630 calls (88 a day), hit rate 0.395, chance 0.121, lift 3.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.431; 0.35: 192, 0.492; 0.40: 152, 0.538; 0.45: 118, 0.585; 0.50: 85, 0.637; 0.55: 60, 0.674; 0.60: 40, 0.712; 0.65: 24, 0.782; 0.70: 12, 0.807; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.363; 0.35: 88, 0.390; 0.40: 24, 0.424; 0.45: 4, 0.452; 0.50: 1, 0.714
- **K=13**: model 1794096000, labels learned 140315, probability skill vs chance 0.1674, widened contest next: True
  - now: threshold 0.4307, hit rate recent 0.5516 / long run 0.5681
    - 6h: 21 calls (88 a day), hit rate 0.476, chance 0.071, naive rule 0.207, lift 6.71x
    - 24h: 46 calls (46 a day), hit rate 0.565, chance 0.080, naive rule 0.272, lift 7.07x
    - 7d: 373 calls (53 a day), hit rate 0.560, chance 0.078, naive rule 0.283, lift 7.14x
    - 30d: 1651 calls (55 a day), hit rate 0.561, chance 0.078, naive rule 0.282, lift 7.22x
  - next: threshold 0.2818, hit rate recent 0.2714 / long run 0.3223
    - 6h: 29 calls (121 a day), hit rate 0.241, chance 0.071, lift 3.40x
    - 24h: 81 calls (82 a day), hit rate 0.272, chance 0.080, lift 3.40x
    - 7d: 420 calls (60 a day), hit rate 0.331, chance 0.078, lift 4.22x
    - 30d: 1822 calls (61 a day), hit rate 0.323, chance 0.078, lift 4.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.435; 0.35: 95, 0.482; 0.40: 67, 0.542; 0.45: 46, 0.585; 0.50: 30, 0.645; 0.55: 20, 0.675; 0.60: 11, 0.711; 0.65: 4, 0.673; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.329; 0.35: 12, 0.340; 0.40: 3, 0.405; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.883 | -0.29% | 0.917 | 0.517 | 0.251 | 0.441 | 0.153 |
| 6h | 6.230 | 0.40% | 0.878 | 0.475 | 0.250 | 0.490 | 0.376 |
| 24h | 6.398 | 1.27% | 0.897 | 0.492 | 0.251 | 0.497 | 0.399 |
| 7d | 14.945 | 5.05% | 0.899 | 0.499 | 0.250 | 0.504 | 0.753 |
| 30d | 14.786 | 4.45% | 0.900 | 0.500 | 0.250 | 0.500 | 0.713 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.863 | 6.871 | 6.878 | 6.937 | 7.097 | 6.963 | 6.882 | 6.868 | 6.855 | 6.883 |
| 6h | 6.255 | 6.232 | 6.231 | 6.336 | 6.372 | 6.471 | 6.226 | 6.214 | 6.213 | 6.230 |
| 24h | 6.480 | 6.459 | 6.434 | 6.445 | 6.575 | 6.762 | 6.392 | 6.376 | 6.382 | 6.398 |
| 7d | 15.741 | 15.062 | 15.041 | 15.001 | 15.211 | 15.320 | 14.929 | 14.922 | 14.918 | 14.945 |
| 30d | 15.474 | 14.937 | 14.884 | 14.816 | 15.063 | 15.031 | 14.776 | 14.756 | 14.758 | 14.786 |

## Next candle

- candle starting 2026-11-08 14:51 UTC, last close 2238.46
- P(up) 0.4972, return quantiles (bp): {'05': -4.223, '10': -2.99, '25': -1.468, '40': -0.496, '50': -0.017, '60': 0.514, '75': 1.593, '90': 3.159, '95': 4.284}
- changepoint probability 0.0413, regime age 59.9 min
- agent weights: empirical 0.055, ewma 0.164, garch 0.162, har 0.080, bocpd 0.026, hmm 0.005, online_qr 0.228, lgbm 0.281

## Learning log

- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- 2026-11-08 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9325}, "hmm": {"sd_bp": [2.87, 6.46, 18.11], "stay": [0.987, 0.977, 0.934]}, "lgbm": {"challenger_loss": 0.24743, "champion_loss": 0.24746, "promoted": true}, "reversal_k3": {"challenger_loss": 0.5073, "challengers": 1, "chance_loss": 0.62519, "widened": false, "champion_loss": 0.50718, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38737, "challengers": 1, "chance_loss": 0.49224, "widened": false, "champion_loss": 0.38666, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28686, "challengers": 1, "chance_loss": 0.3801, "widened": false, "champion_loss": 0.28694, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20249, "challengers": 3, "chance_loss": 0.27804, "widened": true, "champion_loss": 0.20269, "promoted": true}}
- 2026-11-08 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9332}, "hmm": {"sd_bp": [2.33, 5.88, 17.3], "stay": [0.988, 0.978, 0.945]}}
- HMM volatility states (sd, bp per minute): [2.33, 5.88, 17.3], current probabilities: [0.983, 0.016, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-08 15:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.218, 'l_abs': 0.591, 'l_hi': 0.738, 'l_lo': 0.716, 'b05': 0.626, 'b25': 0.62, 'b75': 0.578, 'b95': 0.637}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.6, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.4, 1.435, 1.835, 1.752, 1.885, 2.21, 2.274, 2.725, 2.711, 3.343, 3.295, 3.723, 4.11, 4.096]}
- calibration offsets (in sigma): {'05': -0.015, '10': 0.05, '25': 0.035, '40': 0.01, '50': 0.0, '60': 0.01, '75': 0.055, '90': 0.03, '95': 0.025}
