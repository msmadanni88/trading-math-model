# ETH-USD 60s candle generator - report

- generated: 2026-10-18 13:24 UTC
- last closed candle: 2026-10-18 13:24 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.566 (53) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.554 (446) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.564 (110) | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.505 (794) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.501 (11116) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.562 (32) | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | 0.372 (43) | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | 0.526 (38) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | 0.571 (56) | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 0.950 (40) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | 0.433 (90) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | 0.828 (29) | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | 0.400 (65) | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | 0.667 (27) | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.503 (12351) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06762, 0.1031] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5247, 'levels': [{'threshold': 0.06762, 'calls_per_day': 137.6, 'win_rate': 0.568}, {'threshold': 0.1031, 'calls_per_day': 33.3, 'win_rate': 0.6298}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 21024, 'rate': 0.5283}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15148 | 0.336 | 0.522 (14898) | 0.591 (1409) | 0.775 (2477) |
| volatility: normal | 15148 | 0.362 | 0.514 (15080) | 0.608 (444) | 0.772 (2217) |
| volatility: wild | 15148 | 0.377 | 0.506 (15104) | 0.649 (168) | 0.768 (2060) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15256) | 0.602 (752) | 0.766 (2261) |
| session: Europe 08-13 | 9600 | 0.352 | 0.513 (9513) | 0.577 (523) | 0.776 (1511) |
| session: US 13-21 | 14904 | 0.367 | 0.509 (14799) | 0.589 (469) | 0.781 (2162) |
| session: late 21-24 | 5580 | 0.349 | 0.513 (5514) | 0.653 (277) | 0.756 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.363 | 0.313 | 0.236 | 0.236 | 0.617 | 0.303 | 0.423 | 0.875 |
| 6h | 360 | 0.346 | 0.345 | 0.273 | 0.298 | 0.503 | 0.247 | 0.445 | 1.030 |
| 24h | 1440 | 0.345 | 0.342 | 0.256 | 0.283 | 0.522 | 0.250 | 0.440 | 1.169 |
| 7d | 10080 | 0.366 | 0.357 | 0.280 | 0.311 | 0.525 | 0.261 | 0.470 | 1.205 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.465 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.363 / 0.617 / 0.883; 2: 0.321 / 0.450 / 0.933; 3: 0.339 / 0.483 / 0.983; 4: 0.343 / 0.517 / 0.967; 5: 0.304 / 0.450 / 0.967; 6: 0.318 / 0.433 / 0.967; 7: 0.324 / 0.533 / 1.000; 8: 0.340 / 0.550 / 0.983; 9: 0.336 / 0.517 / 0.967; 10: 0.307 / 0.433 / 0.967; 11: 0.331 / 0.467 / 0.983; 12: 0.347 / 0.533 / 0.967; 13: 0.326 / 0.500 / 0.983; 14: 0.369 / 0.567 / 0.967; 15: 0.350 / 0.483 / 0.967
- 6h: 1: 0.346 / 0.503 / 0.881; 2: 0.345 / 0.528 / 0.903; 3: 0.356 / 0.514 / 0.914; 4: 0.338 / 0.461 / 0.897; 5: 0.332 / 0.483 / 0.914; 6: 0.345 / 0.517 / 0.919; 7: 0.337 / 0.517 / 0.931; 8: 0.349 / 0.525 / 0.933; 9: 0.327 / 0.503 / 0.914; 10: 0.332 / 0.480 / 0.914; 11: 0.336 / 0.492 / 0.931; 12: 0.344 / 0.528 / 0.917; 13: 0.344 / 0.508 / 0.933; 14: 0.345 / 0.511 / 0.917; 15: 0.351 / 0.497 / 0.931
- 24h: 1: 0.345 / 0.522 / 0.879; 2: 0.329 / 0.476 / 0.901; 3: 0.343 / 0.514 / 0.899; 4: 0.330 / 0.481 / 0.900; 5: 0.332 / 0.499 / 0.902; 6: 0.337 / 0.511 / 0.902; 7: 0.335 / 0.512 / 0.904; 8: 0.334 / 0.505 / 0.910; 9: 0.328 / 0.487 / 0.907; 10: 0.334 / 0.504 / 0.903; 11: 0.328 / 0.492 / 0.910; 12: 0.331 / 0.503 / 0.910; 13: 0.328 / 0.496 / 0.906; 14: 0.330 / 0.504 / 0.910; 15: 0.330 / 0.491 / 0.911
- 7d: 1: 0.366 / 0.525 / 0.902; 2: 0.353 / 0.496 / 0.899; 3: 0.358 / 0.509 / 0.899; 4: 0.353 / 0.495 / 0.899; 5: 0.355 / 0.502 / 0.899; 6: 0.355 / 0.504 / 0.899; 7: 0.354 / 0.504 / 0.900; 8: 0.352 / 0.500 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.354 / 0.507 / 0.900; 11: 0.348 / 0.492 / 0.901; 12: 0.352 / 0.505 / 0.900; 13: 0.351 / 0.501 / 0.900; 14: 0.349 / 0.499 / 0.901; 15: 0.353 / 0.505 / 0.902
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.350 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.503 / 0.900; 8: 0.348 / 0.502 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.345 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.082 (body 0.057, range 0.108); 'price stays where it was' would score 0.103; colour right 0.517; typical miss of the close 8.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.135 (body 0.093, range 0.177); 'price stays where it was' would score 0.113; colour right 0.537; typical miss of the close 6.2 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.127 (body 0.092, range 0.162); 'price stays where it was' would score 0.121; colour right 0.515; typical miss of the close 6.9 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.498; typical miss of the close 9.0 bp; chain ended on the right side 0.507 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.520 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 3.9; 2: 0.196 / 4.4; 3: 0.165 / 6.0; 4: 0.134 / 6.6; 5: 0.120 / 7.2; 6: 0.110 / 7.7; 7: 0.102 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.080 / 9.9; 12: 0.076 / 10.2; 13: 0.064 / 10.5; 14: 0.066 / 10.6; 15: 0.058 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 109998, probability skill vs chance 0.2207, widened contest next: False
  - now: threshold 0.837, hit rate recent 0.9299 / long run 0.9328
    - 6h: 19 calls (77 a day), hit rate 0.895, chance 0.323, naive rule 0.534, lift 2.77x
    - 24h: 67 calls (67 a day), hit rate 0.955, chance 0.294, naive rule 0.490, lift 3.25x
    - 7d: 378 calls (54 a day), hit rate 0.942, chance 0.289, naive rule 0.485, lift 3.26x
    - 30d: 1728 calls (58 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5378, hit rate recent 0.5666 / long run 0.5713
    - 6h: 30 calls (122 a day), hit rate 0.633, chance 0.323, lift 1.96x
    - 24h: 86 calls (86 a day), hit rate 0.570, chance 0.294, lift 1.94x
    - 7d: 715 calls (102 a day), hit rate 0.571, chance 0.289, lift 1.97x
    - 30d: 2592 calls (86 a day), hit rate 0.579, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.514; 0.40: 483, 0.565; 0.45: 413, 0.635; 0.50: 361, 0.688; 0.55: 316, 0.730; 0.60: 270, 0.774; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 139, 0.870; 0.80: 95, 0.912; 0.85: 49, 0.951; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 499, 0.459; 0.40: 408, 0.491; 0.45: 313, 0.524; 0.50: 204, 0.557; 0.55: 92, 0.577; 0.60: 14, 0.608; 0.65: 1, 0.654
- **K=5**: model 1791590400, labels learned 109996, probability skill vs chance 0.213, widened contest next: True
  - now: threshold 0.6882, hit rate recent 0.8298 / long run 0.8268
    - 6h: 16 calls (65 a day), hit rate 0.750, chance 0.187, naive rule 0.392, lift 4.01x
    - 24h: 54 calls (54 a day), hit rate 0.852, chance 0.194, naive rule 0.409, lift 4.40x
    - 7d: 346 calls (49 a day), hit rate 0.821, chance 0.187, naive rule 0.404, lift 4.39x
    - 30d: 1610 calls (54 a day), hit rate 0.831, chance 0.188, naive rule 0.394, lift 4.43x
  - next: threshold 0.4038, hit rate recent 0.4259 / long run 0.4579
    - 6h: 43 calls (175 a day), hit rate 0.442, chance 0.187, lift 2.36x
    - 24h: 157 calls (158 a day), hit rate 0.439, chance 0.194, lift 2.27x
    - 7d: 760 calls (109 a day), hit rate 0.463, chance 0.187, lift 2.48x
    - 30d: 2385 calls (80 a day), hit rate 0.474, chance 0.188, lift 2.53x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.421; 0.35: 351, 0.486; 0.40: 282, 0.559; 0.45: 230, 0.614; 0.50: 181, 0.664; 0.55: 137, 0.710; 0.60: 108, 0.750; 0.65: 81, 0.790; 0.70: 60, 0.824; 0.75: 33, 0.869; 0.80: 10, 0.883
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.388; 0.35: 251, 0.422; 0.40: 160, 0.448; 0.45: 76, 0.464; 0.50: 18, 0.501; 0.55: 2, 0.549
- **K=8**: model 1791936000, labels learned 109993, probability skill vs chance 0.1953, widened contest next: False
  - now: threshold 0.5756, hit rate recent 0.6951 / long run 0.6994
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.129, naive rule 0.341, lift 4.86x
    - 24h: 51 calls (51 a day), hit rate 0.706, chance 0.117, naive rule 0.315, lift 6.04x
    - 7d: 342 calls (49 a day), hit rate 0.687, chance 0.120, naive rule 0.332, lift 5.71x
    - 30d: 1577 calls (53 a day), hit rate 0.718, chance 0.122, naive rule 0.330, lift 5.87x
  - next: threshold 0.3407, hit rate recent 0.3723 / long run 0.3795
    - 6h: 33 calls (136 a day), hit rate 0.394, chance 0.129, lift 3.06x
    - 24h: 119 calls (120 a day), hit rate 0.370, chance 0.117, lift 3.17x
    - 7d: 650 calls (93 a day), hit rate 0.382, chance 0.120, lift 3.17x
    - 30d: 2210 calls (74 a day), hit rate 0.401, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.421; 0.35: 195, 0.492; 0.40: 149, 0.552; 0.45: 117, 0.595; 0.50: 90, 0.636; 0.55: 66, 0.686; 0.60: 44, 0.732; 0.65: 24, 0.788; 0.70: 9, 0.839; 0.75: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.353; 0.35: 105, 0.385; 0.40: 42, 0.420; 0.45: 9, 0.441; 0.50: 1, 0.419
- **K=13**: model 1792022400, labels learned 109988, probability skill vs chance 0.1846, widened contest next: False
  - now: threshold 0.4144, hit rate recent 0.557 / long run 0.5728
    - 6h: 20 calls (83 a day), hit rate 0.550, chance 0.078, naive rule 0.308, lift 7.03x
    - 24h: 64 calls (65 a day), hit rate 0.547, chance 0.076, naive rule 0.282, lift 7.18x
    - 7d: 372 calls (53 a day), hit rate 0.559, chance 0.076, naive rule 0.279, lift 7.31x
    - 30d: 1531 calls (51 a day), hit rate 0.586, chance 0.078, naive rule 0.274, lift 7.49x
  - next: threshold 0.2779, hit rate recent 0.3304 / long run 0.3143
    - 6h: 20 calls (83 a day), hit rate 0.350, chance 0.078, lift 4.47x
    - 24h: 67 calls (68 a day), hit rate 0.328, chance 0.076, lift 4.31x
    - 7d: 417 calls (60 a day), hit rate 0.305, chance 0.076, lift 3.98x
    - 30d: 2050 calls (68 a day), hit rate 0.315, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.511; 0.40: 61, 0.565; 0.45: 42, 0.619; 0.50: 25, 0.660; 0.55: 14, 0.710; 0.60: 5, 0.761; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 13, 0.357; 0.40: 2, 0.406

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.431 | -0.07% | 0.900 | 0.433 | 0.251 | 0.500 | 0.008 |
| 6h | 10.892 | 1.41% | 0.894 | 0.467 | 0.251 | 0.492 | 0.472 |
| 24h | 11.630 | 4.18% | 0.894 | 0.495 | 0.250 | 0.504 | 0.631 |
| 7d | 15.714 | 4.38% | 0.900 | 0.499 | 0.251 | 0.491 | 0.645 |
| 30d | 13.791 | 4.12% | 0.900 | 0.500 | 0.251 | 0.496 | 0.679 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.423 | 10.476 | 10.502 | 10.484 | 10.402 | 10.431 | 10.455 | 10.452 | 10.447 | 10.431 |
| 6h | 11.047 | 10.961 | 10.929 | 10.938 | 11.029 | 10.920 | 10.870 | 10.866 | 10.874 | 10.892 |
| 24h | 12.138 | 11.795 | 11.637 | 11.657 | 11.782 | 11.695 | 11.633 | 11.616 | 11.612 | 11.630 |
| 7d | 16.434 | 15.892 | 15.813 | 15.733 | 15.978 | 15.918 | 15.720 | 15.692 | 15.684 | 15.714 |
| 30d | 14.384 | 13.914 | 13.876 | 13.818 | 14.037 | 13.976 | 13.789 | 13.765 | 13.765 | 13.791 |

## Next candle

- candle starting 2026-10-18 13:24 UTC, last close 2406.5
- P(up) 0.5155, return quantiles (bp): {'05': -8.449, '10': -6.26, '25': -3.287, '40': -1.184, '50': 0.214, '60': 1.255, '75': 2.954, '90': 6.094, '95': 8.216}
- changepoint probability 0.102, regime age 141.1 min
- agent weights: empirical 0.011, ewma 0.073, garch 0.148, har 0.142, bocpd 0.058, hmm 0.121, online_qr 0.203, lgbm 0.244

## Learning log

- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- HMM volatility states (sd, bp per minute): [3.34, 6.61, 20.42], current probabilities: [0.413, 0.565, 0.022]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 13:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.351, 'l_abs': 0.661, 'l_hi': 0.729, 'l_lo': 0.725, 'b05': 0.664, 'b25': 0.655, 'b75': 0.62, 'b95': 0.659}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.42, 1.742, 2.098, 2.127, 2.243, 2.286, 2.261, 2.551, 2.749, 2.462, 2.848, 2.853, 3.088, 3.016]}
- calibration offsets (in sigma): {'05': 0.0015, '10': -0.027, '25': -0.1225, '40': -0.068, '50': 0.025, '60': -0.002, '75': -0.0275, '90': -0.003, '95': 0.0185}
