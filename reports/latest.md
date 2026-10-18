# ETH-USD 60s candle generator - report

- generated: 2026-10-18 16:41 UTC
- last closed candle: 2026-10-18 16:41 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.576 (66) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.552 (558) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.564 (117) | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.513 (991) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.504 (13874) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.576 (33) | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | 0.358 (53) | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | 0.479 (48) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | 0.567 (67) | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 0.957 (46) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | 0.420 (112) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | 0.853 (34) | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | 0.407 (81) | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | 0.688 (32) | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.506 (15404) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06762, 0.1031] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5247, 'levels': [{'threshold': 0.06762, 'calls_per_day': 137.6, 'win_rate': 0.568}, {'threshold': 0.1031, 'calls_per_day': 33.3, 'win_rate': 0.6298}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 21221, 'rate': 0.5285}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15214 | 0.336 | 0.521 (14964) | 0.592 (1410) | 0.774 (2488) |
| volatility: normal | 15213 | 0.362 | 0.515 (15145) | 0.607 (445) | 0.771 (2224) |
| volatility: wild | 15214 | 0.377 | 0.506 (15170) | 0.647 (173) | 0.770 (2068) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15256) | 0.602 (752) | 0.766 (2261) |
| session: Europe 08-13 | 9600 | 0.352 | 0.513 (9513) | 0.577 (523) | 0.776 (1511) |
| session: US 13-21 | 15101 | 0.367 | 0.510 (14996) | 0.588 (476) | 0.780 (2188) |
| session: late 21-24 | 5580 | 0.349 | 0.513 (5514) | 0.653 (277) | 0.756 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.413 | 0.338 | 0.249 | 0.249 | 0.617 | 0.353 | 0.472 | 1.285 |
| 6h | 360 | 0.368 | 0.350 | 0.260 | 0.277 | 0.541 | 0.271 | 0.464 | 1.311 |
| 24h | 1440 | 0.350 | 0.347 | 0.257 | 0.283 | 0.521 | 0.253 | 0.446 | 1.141 |
| 7d | 10080 | 0.367 | 0.357 | 0.280 | 0.311 | 0.525 | 0.262 | 0.471 | 1.200 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.464 | 1.296 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.413 / 0.617 / 0.933; 2: 0.343 / 0.467 / 0.917; 3: 0.347 / 0.467 / 0.867; 4: 0.389 / 0.650 / 0.883; 5: 0.365 / 0.550 / 0.867; 6: 0.351 / 0.500 / 0.850; 7: 0.326 / 0.417 / 0.850; 8: 0.344 / 0.517 / 0.850; 9: 0.382 / 0.583 / 0.883; 10: 0.351 / 0.533 / 0.867; 11: 0.355 / 0.517 / 0.850; 12: 0.374 / 0.567 / 0.933; 13: 0.389 / 0.583 / 0.933; 14: 0.374 / 0.533 / 0.950; 15: 0.376 / 0.583 / 0.900
- 6h: 1: 0.368 / 0.541 / 0.906; 2: 0.343 / 0.493 / 0.903; 3: 0.360 / 0.493 / 0.917; 4: 0.358 / 0.524 / 0.922; 5: 0.338 / 0.471 / 0.894; 6: 0.347 / 0.504 / 0.872; 7: 0.347 / 0.518 / 0.886; 8: 0.346 / 0.521 / 0.867; 9: 0.348 / 0.507 / 0.872; 10: 0.349 / 0.521 / 0.856; 11: 0.346 / 0.515 / 0.844; 12: 0.349 / 0.518 / 0.867; 13: 0.347 / 0.499 / 0.861; 14: 0.359 / 0.535 / 0.858; 15: 0.344 / 0.496 / 0.847
- 24h: 1: 0.350 / 0.521 / 0.885; 2: 0.331 / 0.475 / 0.898; 3: 0.347 / 0.519 / 0.894; 4: 0.334 / 0.489 / 0.894; 5: 0.334 / 0.495 / 0.892; 6: 0.339 / 0.514 / 0.890; 7: 0.337 / 0.510 / 0.893; 8: 0.338 / 0.517 / 0.891; 9: 0.332 / 0.496 / 0.895; 10: 0.336 / 0.507 / 0.890; 11: 0.330 / 0.500 / 0.890; 12: 0.335 / 0.507 / 0.894; 13: 0.332 / 0.498 / 0.891; 14: 0.334 / 0.503 / 0.894; 15: 0.333 / 0.497 / 0.890
- 7d: 1: 0.367 / 0.525 / 0.902; 2: 0.353 / 0.494 / 0.900; 3: 0.359 / 0.509 / 0.900; 4: 0.353 / 0.496 / 0.900; 5: 0.355 / 0.503 / 0.900; 6: 0.355 / 0.504 / 0.900; 7: 0.354 / 0.504 / 0.899; 8: 0.352 / 0.500 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.355 / 0.509 / 0.899; 11: 0.348 / 0.492 / 0.899; 12: 0.353 / 0.506 / 0.900; 13: 0.352 / 0.502 / 0.900; 14: 0.350 / 0.500 / 0.901; 15: 0.353 / 0.504 / 0.901
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.503 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.502 / 0.899; 14: 0.345 / 0.498 / 0.899; 15: 0.345 / 0.497 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.091 (body 0.071, range 0.111); 'price stays where it was' would score 0.093; colour right 0.533; typical miss of the close 21.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.113 (body 0.078, range 0.147); 'price stays where it was' would score 0.106; colour right 0.501; typical miss of the close 10.1 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.128 (body 0.094, range 0.162); 'price stays where it was' would score 0.122; colour right 0.518; typical miss of the close 7.5 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.164); 'price stays where it was' would score 0.130; colour right 0.497; typical miss of the close 9.2 bp; chain ended on the right side 0.513 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.520 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 3.9; 2: 0.196 / 4.4; 3: 0.164 / 6.0; 4: 0.134 / 6.5; 5: 0.121 / 7.2; 6: 0.110 / 7.7; 7: 0.102 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.080 / 9.9; 12: 0.076 / 10.2; 13: 0.064 / 10.4; 14: 0.066 / 10.6; 15: 0.058 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 110195, probability skill vs chance 0.2213, widened contest next: False
  - now: threshold 0.837, hit rate recent 0.9366 / long run 0.9335
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.306, naive rule 0.542, lift 3.04x
    - 24h: 66 calls (66 a day), hit rate 0.955, chance 0.294, naive rule 0.493, lift 3.25x
    - 7d: 374 calls (53 a day), hit rate 0.941, chance 0.289, naive rule 0.485, lift 3.26x
    - 30d: 1723 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.484, lift 3.22x
  - next: threshold 0.5378, hit rate recent 0.5651 / long run 0.5709
    - 6h: 27 calls (110 a day), hit rate 0.519, chance 0.306, lift 1.70x
    - 24h: 87 calls (87 a day), hit rate 0.575, chance 0.294, lift 1.96x
    - 7d: 713 calls (102 a day), hit rate 0.568, chance 0.289, lift 1.97x
    - 30d: 2590 calls (86 a day), hit rate 0.578, chance 0.291, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.514; 0.40: 483, 0.565; 0.45: 413, 0.635; 0.50: 361, 0.688; 0.55: 316, 0.731; 0.60: 269, 0.774; 0.65: 224, 0.802; 0.70: 179, 0.836; 0.75: 138, 0.871; 0.80: 95, 0.913; 0.85: 49, 0.952; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 499, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.524; 0.50: 204, 0.556; 0.55: 92, 0.577; 0.60: 14, 0.609; 0.65: 1, 0.667
- **K=5**: model 1791590400, labels learned 110193, probability skill vs chance 0.2122, widened contest next: True
  - now: threshold 0.6882, hit rate recent 0.8435 / long run 0.8282
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.187, naive rule 0.413, lift 4.28x
    - 24h: 49 calls (49 a day), hit rate 0.857, chance 0.193, naive rule 0.406, lift 4.43x
    - 7d: 343 calls (49 a day), hit rate 0.822, chance 0.186, naive rule 0.403, lift 4.41x
    - 30d: 1608 calls (54 a day), hit rate 0.832, chance 0.188, naive rule 0.394, lift 4.44x
  - next: threshold 0.4038, hit rate recent 0.4097 / long run 0.4546
    - 6h: 40 calls (163 a day), hit rate 0.350, chance 0.187, lift 1.87x
    - 24h: 161 calls (162 a day), hit rate 0.422, chance 0.193, lift 2.18x
    - 7d: 770 calls (110 a day), hit rate 0.460, chance 0.186, lift 2.47x
    - 30d: 2399 calls (80 a day), hit rate 0.473, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.421; 0.35: 351, 0.486; 0.40: 281, 0.559; 0.45: 230, 0.615; 0.50: 181, 0.665; 0.55: 137, 0.711; 0.60: 107, 0.751; 0.65: 81, 0.792; 0.70: 59, 0.825; 0.75: 33, 0.870; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.388; 0.35: 251, 0.421; 0.40: 160, 0.447; 0.45: 76, 0.464; 0.50: 18, 0.500; 0.55: 2, 0.580
- **K=8**: model 1791936000, labels learned 110190, probability skill vs chance 0.1994, widened contest next: False
  - now: threshold 0.5756, hit rate recent 0.7041 / long run 0.7002
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.120, naive rule 0.353, lift 4.49x
    - 24h: 48 calls (48 a day), hit rate 0.729, chance 0.115, naive rule 0.315, lift 6.32x
    - 7d: 337 calls (48 a day), hit rate 0.685, chance 0.120, naive rule 0.331, lift 5.69x
    - 30d: 1574 calls (52 a day), hit rate 0.719, chance 0.122, naive rule 0.330, lift 5.87x
  - next: threshold 0.3407, hit rate recent 0.391 / long run 0.3811
    - 6h: 30 calls (123 a day), hit rate 0.367, chance 0.120, lift 3.06x
    - 24h: 118 calls (119 a day), hit rate 0.373, chance 0.115, lift 3.23x
    - 7d: 651 calls (93 a day), hit rate 0.381, chance 0.120, lift 3.16x
    - 30d: 2215 calls (74 a day), hit rate 0.401, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 257, 0.421; 0.35: 195, 0.493; 0.40: 148, 0.553; 0.45: 117, 0.595; 0.50: 90, 0.636; 0.55: 65, 0.686; 0.60: 44, 0.732; 0.65: 24, 0.790; 0.70: 9, 0.846; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.353; 0.35: 105, 0.386; 0.40: 42, 0.419; 0.45: 9, 0.446; 0.50: 1, 0.438
- **K=13**: model 1792022400, labels learned 110185, probability skill vs chance 0.1847, widened contest next: True
  - now: threshold 0.4144, hit rate recent 0.5186 / long run 0.5683
    - 6h: 19 calls (79 a day), hit rate 0.368, chance 0.070, naive rule 0.273, lift 5.30x
    - 24h: 64 calls (65 a day), hit rate 0.516, chance 0.075, naive rule 0.271, lift 6.90x
    - 7d: 374 calls (54 a day), hit rate 0.551, chance 0.077, naive rule 0.279, lift 7.17x
    - 30d: 1532 calls (51 a day), hit rate 0.584, chance 0.078, naive rule 0.274, lift 7.46x
  - next: threshold 0.2779, hit rate recent 0.3269 / long run 0.3141
    - 6h: 17 calls (71 a day), hit rate 0.294, chance 0.070, lift 4.23x
    - 24h: 69 calls (70 a day), hit rate 0.319, chance 0.075, lift 4.27x
    - 7d: 416 calls (60 a day), hit rate 0.303, chance 0.077, lift 3.94x
    - 30d: 2050 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 42, 0.618; 0.50: 25, 0.661; 0.55: 14, 0.713; 0.60: 5, 0.768; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 13, 0.358; 0.40: 2, 0.419; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.908 | 2.77% | 0.933 | 0.517 | 0.251 | 0.383 | 0.239 |
| 6h | 16.061 | 5.12% | 0.908 | 0.494 | 0.250 | 0.468 | 0.589 |
| 24h | 12.940 | 5.07% | 0.896 | 0.496 | 0.250 | 0.499 | 0.645 |
| 7d | 15.876 | 4.33% | 0.900 | 0.499 | 0.251 | 0.490 | 0.644 |
| 30d | 13.734 | 4.07% | 0.900 | 0.500 | 0.251 | 0.495 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 16.361 | 16.064 | 16.165 | 16.062 | 16.037 | 16.018 | 15.878 | 15.765 | 15.842 | 15.908 |
| 6h | 16.927 | 16.328 | 16.196 | 16.072 | 16.447 | 16.111 | 16.100 | 15.964 | 16.034 | 16.061 |
| 24h | 13.632 | 13.161 | 12.972 | 12.954 | 13.157 | 13.005 | 12.957 | 12.893 | 12.916 | 12.940 |
| 7d | 16.595 | 16.062 | 15.978 | 15.892 | 16.139 | 16.075 | 15.882 | 15.852 | 15.845 | 15.876 |
| 30d | 14.317 | 13.857 | 13.818 | 13.759 | 13.980 | 13.915 | 13.731 | 13.706 | 13.707 | 13.734 |

## Next candle

- candle starting 2026-10-18 16:41 UTC, last close 2362.5
- P(up) 0.4984, return quantiles (bp): {'05': -10.913, '10': -7.926, '25': -4.352, '40': -1.904, '50': -0.007, '60': 1.446, '75': 3.79, '90': 7.35, '95': 9.982}
- changepoint probability 0.0264, regime age 111.9 min
- agent weights: empirical 0.003, ewma 0.029, garch 0.084, har 0.160, bocpd 0.015, hmm 0.114, online_qr 0.182, lgbm 0.414

## Learning log

- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- HMM volatility states (sd, bp per minute): [3.34, 6.61, 20.42], current probabilities: [0.011, 0.975, 0.014]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 16:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.295, 'l_abs': 0.666, 'l_hi': 0.734, 'l_lo': 0.724, 'b05': 0.66, 'b25': 0.666, 'b75': 0.645, 'b95': 0.661}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.547, 2.016, 2.333, 2.72, 3.108, 3.297, 3.531, 3.465, 4.126, 4.424, 4.189, 4.457, 4.635, 5.207]}
- calibration offsets (in sigma): {'05': -0.05, '10': -0.03, '25': -0.1, '40': -0.1, '50': -0.03, '60': -0.03, '75': -0.01, '90': -0.06, '95': -0.04}
