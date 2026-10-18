# ETH-USD 60s candle generator - report

- generated: 2026-10-18 04:55 UTC
- last closed candle: 2026-10-18 04:55 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.632 (19) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.553 (150) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.611 (36) | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.515 (291) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.507 (4074) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.625 (8) | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | 0.444 (9) | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | 0.500 (12) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | 0.364 (11) | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 1.000 (14) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | 0.500 (22) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | 0.889 (9) | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | 0.389 (18) | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | 0.750 (8) | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.510 (4487) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06935, 0.1076] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5274, 'levels': [{'threshold': 0.06935, 'calls_per_day': 137.5, 'win_rate': 0.5742}, {'threshold': 0.1076, 'calls_per_day': 33.9, 'win_rate': 0.636}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 20521, 'rate': 0.5291}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14979 | 0.336 | 0.522 (14733) | 0.594 (1359) | 0.777 (2448) |
| volatility: normal | 14978 | 0.362 | 0.514 (14912) | 0.609 (422) | 0.771 (2178) |
| volatility: wild | 14978 | 0.377 | 0.506 (14934) | 0.651 (166) | 0.768 (2037) |
| session: Asia 00-08 | 15175 | 0.357 | 0.520 (15073) | 0.607 (718) | 0.766 (2235) |
| session: Europe 08-13 | 9300 | 0.352 | 0.513 (9217) | 0.580 (486) | 0.778 (1451) |
| session: US 13-21 | 14880 | 0.367 | 0.509 (14775) | 0.586 (466) | 0.782 (2157) |
| session: late 21-24 | 5580 | 0.349 | 0.513 (5514) | 0.653 (277) | 0.756 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.296 | 0.274 | 0.175 | 0.175 | 0.525 | 0.188 | 0.404 | 1.717 |
| 6h | 360 | 0.350 | 0.354 | 0.256 | 0.299 | 0.524 | 0.250 | 0.451 | 1.310 |
| 24h | 1440 | 0.344 | 0.334 | 0.248 | 0.275 | 0.538 | 0.257 | 0.432 | 1.227 |
| 7d | 10080 | 0.364 | 0.355 | 0.278 | 0.309 | 0.528 | 0.261 | 0.468 | 1.235 |
| 30d | 43200 | 0.358 | 0.355 | 0.279 | 0.308 | 0.515 | 0.252 | 0.465 | 1.302 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.296 / 0.525 / 0.883; 2: 0.259 / 0.424 / 0.917; 3: 0.277 / 0.458 / 0.883; 4: 0.278 / 0.525 / 0.983; 5: 0.273 / 0.458 / 0.917; 6: 0.286 / 0.458 / 0.900; 7: 0.275 / 0.441 / 0.900; 8: 0.285 / 0.576 / 0.867; 9: 0.274 / 0.559 / 0.867; 10: 0.283 / 0.458 / 0.850; 11: 0.278 / 0.475 / 0.833; 12: 0.250 / 0.508 / 0.833; 13: 0.284 / 0.576 / 0.817; 14: 0.244 / 0.424 / 0.817; 15: 0.290 / 0.593 / 0.833
- 6h: 1: 0.350 / 0.524 / 0.906; 2: 0.324 / 0.442 / 0.939; 3: 0.353 / 0.544 / 0.933; 4: 0.333 / 0.490 / 0.978; 5: 0.336 / 0.501 / 0.953; 6: 0.356 / 0.546 / 0.933; 7: 0.344 / 0.485 / 0.936; 8: 0.349 / 0.535 / 0.911; 9: 0.333 / 0.487 / 0.903; 10: 0.346 / 0.521 / 0.897; 11: 0.335 / 0.504 / 0.889; 12: 0.336 / 0.518 / 0.894; 13: 0.330 / 0.456 / 0.878; 14: 0.335 / 0.499 / 0.900; 15: 0.344 / 0.541 / 0.900
- 24h: 1: 0.344 / 0.538 / 0.878; 2: 0.326 / 0.475 / 0.905; 3: 0.334 / 0.513 / 0.909; 4: 0.325 / 0.494 / 0.912; 5: 0.329 / 0.499 / 0.909; 6: 0.329 / 0.492 / 0.907; 7: 0.334 / 0.517 / 0.910; 8: 0.326 / 0.493 / 0.909; 9: 0.325 / 0.479 / 0.908; 10: 0.332 / 0.508 / 0.906; 11: 0.319 / 0.479 / 0.903; 12: 0.324 / 0.495 / 0.900; 13: 0.325 / 0.496 / 0.898; 14: 0.322 / 0.495 / 0.899; 15: 0.324 / 0.493 / 0.899
- 7d: 1: 0.364 / 0.528 / 0.902; 2: 0.352 / 0.496 / 0.901; 3: 0.356 / 0.508 / 0.901; 4: 0.351 / 0.496 / 0.902; 5: 0.353 / 0.503 / 0.901; 6: 0.353 / 0.502 / 0.901; 7: 0.352 / 0.503 / 0.902; 8: 0.350 / 0.499 / 0.901; 9: 0.351 / 0.502 / 0.902; 10: 0.353 / 0.507 / 0.902; 11: 0.346 / 0.490 / 0.902; 12: 0.351 / 0.505 / 0.901; 13: 0.350 / 0.502 / 0.901; 14: 0.347 / 0.499 / 0.902; 15: 0.350 / 0.504 / 0.903
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.088 (body 0.073, range 0.104); 'price stays where it was' would score 0.108; colour right 0.559; typical miss of the close 6.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.147 (body 0.112, range 0.183); 'price stays where it was' would score 0.141; colour right 0.513; typical miss of the close 6.8 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.140 (body 0.105, range 0.176); 'price stays where it was' would score 0.141; colour right 0.514; typical miss of the close 5.7 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.124 (body 0.085, range 0.164); 'price stays where it was' would score 0.131; colour right 0.497; typical miss of the close 8.7 bp; chain ended on the right side 0.507 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.519 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.0; 2: 0.196 / 4.4; 3: 0.165 / 6.0; 4: 0.134 / 6.6; 5: 0.121 / 7.3; 6: 0.111 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.080 / 9.9; 12: 0.075 / 10.3; 13: 0.064 / 10.7; 14: 0.066 / 10.8; 15: 0.059 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 109489, probability skill vs chance 0.2226, widened contest next: True
  - now: threshold 0.8381, hit rate recent 0.9351 / long run 0.9333
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.279, naive rule 0.483, lift 3.59x
    - 24h: 61 calls (61 a day), hit rate 0.934, chance 0.302, naive rule 0.512, lift 3.09x
    - 7d: 385 calls (55 a day), hit rate 0.938, chance 0.291, naive rule 0.488, lift 3.22x
    - 30d: 1720 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5512, hit rate recent 0.5078 / long run 0.5674
    - 6h: 11 calls (45 a day), hit rate 0.364, chance 0.279, lift 1.30x
    - 24h: 91 calls (91 a day), hit rate 0.505, chance 0.302, lift 1.67x
    - 7d: 706 calls (101 a day), hit rate 0.568, chance 0.291, lift 1.95x
    - 30d: 2578 calls (86 a day), hit rate 0.580, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.564; 0.45: 414, 0.634; 0.50: 361, 0.687; 0.55: 316, 0.730; 0.60: 270, 0.774; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 139, 0.871; 0.80: 95, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 499, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.524; 0.50: 204, 0.558; 0.55: 92, 0.578; 0.60: 14, 0.607; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 109487, probability skill vs chance 0.2148, widened contest next: False
  - now: threshold 0.6911, hit rate recent 0.8458 / long run 0.8277
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.193, naive rule 0.389, lift 4.61x
    - 24h: 54 calls (54 a day), hit rate 0.833, chance 0.200, naive rule 0.434, lift 4.16x
    - 7d: 351 calls (50 a day), hit rate 0.823, chance 0.187, naive rule 0.405, lift 4.40x
    - 30d: 1608 calls (54 a day), hit rate 0.830, chance 0.188, naive rule 0.395, lift 4.42x
  - next: threshold 0.4052, hit rate recent 0.4399 / long run 0.4633
    - 6h: 27 calls (110 a day), hit rate 0.481, chance 0.193, lift 2.50x
    - 24h: 142 calls (143 a day), hit rate 0.437, chance 0.200, lift 2.18x
    - 7d: 723 calls (103 a day), hit rate 0.470, chance 0.187, lift 2.51x
    - 30d: 2337 calls (78 a day), hit rate 0.477, chance 0.188, lift 2.54x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.421; 0.35: 351, 0.486; 0.40: 282, 0.559; 0.45: 230, 0.615; 0.50: 181, 0.666; 0.55: 138, 0.710; 0.60: 108, 0.750; 0.65: 81, 0.792; 0.70: 60, 0.823; 0.75: 33, 0.867; 0.80: 10, 0.882
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 250, 0.424; 0.40: 160, 0.450; 0.45: 76, 0.465; 0.50: 18, 0.499; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 109484, probability skill vs chance 0.1952, widened contest next: True
  - now: threshold 0.5791, hit rate recent 0.727 / long run 0.7016
    - 6h: 8 calls (33 a day), hit rate 0.750, chance 0.091, naive rule 0.242, lift 8.20x
    - 24h: 50 calls (50 a day), hit rate 0.760, chance 0.122, naive rule 0.335, lift 6.25x
    - 7d: 346 calls (49 a day), hit rate 0.691, chance 0.121, naive rule 0.334, lift 5.70x
    - 30d: 1580 calls (53 a day), hit rate 0.717, chance 0.122, naive rule 0.331, lift 5.85x
  - next: threshold 0.3414, hit rate recent 0.344 / long run 0.3776
    - 6h: 23 calls (95 a day), hit rate 0.391, chance 0.091, lift 4.28x
    - 24h: 115 calls (116 a day), hit rate 0.348, chance 0.122, lift 2.86x
    - 7d: 634 calls (91 a day), hit rate 0.380, chance 0.121, lift 3.14x
    - 30d: 2181 calls (73 a day), hit rate 0.403, chance 0.122, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.421; 0.35: 195, 0.493; 0.40: 149, 0.554; 0.45: 117, 0.597; 0.50: 90, 0.638; 0.55: 66, 0.687; 0.60: 44, 0.731; 0.65: 24, 0.787; 0.70: 9, 0.835; 0.75: 1, 0.760
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.354; 0.35: 105, 0.386; 0.40: 42, 0.421; 0.45: 9, 0.447; 0.50: 1, 0.419
- **K=13**: model 1792022400, labels learned 109479, probability skill vs chance 0.1827, widened contest next: False
  - now: threshold 0.4193, hit rate recent 0.5684 / long run 0.5744
    - 6h: 13 calls (54 a day), hit rate 0.538, chance 0.078, naive rule 0.261, lift 6.88x
    - 24h: 56 calls (57 a day), hit rate 0.607, chance 0.078, naive rule 0.296, lift 7.76x
    - 7d: 367 calls (53 a day), hit rate 0.561, chance 0.077, naive rule 0.279, lift 7.33x
    - 30d: 1525 calls (51 a day), hit rate 0.586, chance 0.078, naive rule 0.275, lift 7.49x
  - next: threshold 0.2829, hit rate recent 0.313 / long run 0.3121
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.078, lift 5.32x
    - 24h: 48 calls (49 a day), hit rate 0.271, chance 0.078, lift 3.46x
    - 7d: 411 calls (59 a day), hit rate 0.309, chance 0.077, lift 4.03x
    - 30d: 2030 calls (68 a day), hit rate 0.315, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.513; 0.40: 61, 0.565; 0.45: 41, 0.620; 0.50: 25, 0.658; 0.55: 14, 0.705; 0.60: 5, 0.752; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 47, 0.326; 0.35: 13, 0.358; 0.40: 2, 0.397

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.732 | 1.51% | 0.900 | 0.617 | 0.262 | 0.390 | 0.148 |
| 6h | 10.565 | 1.00% | 0.906 | 0.508 | 0.250 | 0.532 | 0.328 |
| 24h | 10.764 | 6.70% | 0.894 | 0.501 | 0.250 | 0.497 | 0.650 |
| 7d | 15.511 | 4.42% | 0.901 | 0.501 | 0.251 | 0.490 | 0.652 |
| 30d | 13.876 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.677 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.834 | 6.653 | 6.608 | 6.620 | 6.744 | 6.798 | 6.647 | 6.668 | 6.637 | 6.732 |
| 6h | 10.672 | 10.692 | 10.602 | 10.588 | 10.691 | 10.668 | 10.618 | 10.565 | 10.556 | 10.565 |
| 24h | 11.537 | 10.925 | 10.872 | 10.799 | 10.934 | 10.982 | 10.755 | 10.750 | 10.746 | 10.764 |
| 7d | 16.229 | 15.690 | 15.610 | 15.528 | 15.778 | 15.719 | 15.515 | 15.488 | 15.481 | 15.511 |
| 30d | 14.470 | 14.001 | 13.962 | 13.902 | 14.128 | 14.062 | 13.874 | 13.849 | 13.850 | 13.876 |

## Next candle

- candle starting 2026-10-18 04:55 UTC, last close 2412.73
- P(up) 0.5222, return quantiles (bp): {'05': -4.753, '10': -3.461, '25': -1.595, '40': -0.468, '50': 0.13, '60': 0.696, '75': 1.622, '90': 3.527, '95': 4.739}
- changepoint probability 0.0249, regime age 65.1 min
- agent weights: empirical 0.003, ewma 0.034, garch 0.176, har 0.180, bocpd 0.050, hmm 0.074, online_qr 0.217, lgbm 0.267

## Learning log

- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.41, 6.6, 20.67], current probabilities: [0.978, 0.021, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 05:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.381, 'l_abs': 0.671, 'l_hi': 0.716, 'l_lo': 0.713, 'b05': 0.664, 'b25': 0.658, 'b75': 0.639, 'b95': 0.648}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.282, 1.671, 1.647, 2.04, 2.425, 2.472, 2.985, 3.048, 3.419, 3.815, 3.76, 4.421, 4.078, 4.315]}
- calibration offsets (in sigma): {'05': 0.027, '10': 0.024, '25': 0.045, '40': 0.036, '50': 0.03, '60': -0.006, '75': -0.045, '90': -0.034, '95': -0.027}
