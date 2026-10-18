# ETH-USD 60s candle generator - report

- generated: 2026-10-18 18:58 UTC
- last closed candle: 2026-10-18 18:58 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.560 (75) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.556 (629) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.554 (121) | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.518 (1128) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.504 (15792) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.576 (33) | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | 0.339 (59) | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | 0.481 (52) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | 0.587 (75) | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 0.959 (49) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | 0.418 (122) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | 0.842 (38) | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | 0.398 (88) | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | 0.686 (35) | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.506 (17513) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06657, 0.1003] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5257, 'levels': [{'threshold': 0.06657, 'calls_per_day': 137.8, 'win_rate': 0.5582}, {'threshold': 0.1003, 'calls_per_day': 33.1, 'win_rate': 0.6223}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 21358, 'rate': 0.5287}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15260 | 0.336 | 0.521 (15010) | 0.591 (1413) | 0.773 (2502) |
| volatility: normal | 15259 | 0.362 | 0.515 (15191) | 0.606 (444) | 0.771 (2220) |
| volatility: wild | 15259 | 0.377 | 0.506 (15215) | 0.646 (175) | 0.770 (2072) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15256) | 0.602 (752) | 0.766 (2261) |
| session: Europe 08-13 | 9600 | 0.352 | 0.513 (9513) | 0.577 (523) | 0.776 (1511) |
| session: US 13-21 | 15238 | 0.367 | 0.510 (15133) | 0.585 (480) | 0.779 (2202) |
| session: late 21-24 | 5580 | 0.349 | 0.513 (5514) | 0.653 (277) | 0.756 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.344 | 0.316 | 0.207 | 0.207 | 0.517 | 0.240 | 0.448 | 1.144 |
| 6h | 360 | 0.368 | 0.338 | 0.245 | 0.287 | 0.553 | 0.277 | 0.459 | 1.218 |
| 24h | 1440 | 0.351 | 0.345 | 0.257 | 0.284 | 0.521 | 0.254 | 0.447 | 1.136 |
| 7d | 10080 | 0.367 | 0.357 | 0.279 | 0.311 | 0.526 | 0.263 | 0.471 | 1.197 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.464 | 1.297 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.344 / 0.517 / 0.883; 2: 0.333 / 0.450 / 0.950; 3: 0.359 / 0.533 / 0.967; 4: 0.354 / 0.633 / 0.983; 5: 0.321 / 0.433 / 0.983; 6: 0.347 / 0.533 / 0.967; 7: 0.364 / 0.567 / 0.983; 8: 0.328 / 0.417 / 1.000; 9: 0.335 / 0.483 / 0.983; 10: 0.344 / 0.533 / 1.000; 11: 0.337 / 0.483 / 1.000; 12: 0.354 / 0.633 / 0.967; 13: 0.330 / 0.533 / 0.983; 14: 0.328 / 0.517 / 1.000; 15: 0.335 / 0.450 / 1.000
- 6h: 1: 0.368 / 0.553 / 0.911; 2: 0.333 / 0.450 / 0.908; 3: 0.365 / 0.531 / 0.903; 4: 0.357 / 0.553 / 0.908; 5: 0.333 / 0.464 / 0.883; 6: 0.341 / 0.511 / 0.881; 7: 0.345 / 0.506 / 0.878; 8: 0.346 / 0.514 / 0.872; 9: 0.346 / 0.506 / 0.889; 10: 0.356 / 0.542 / 0.881; 11: 0.343 / 0.514 / 0.861; 12: 0.357 / 0.558 / 0.872; 13: 0.345 / 0.511 / 0.867; 14: 0.352 / 0.531 / 0.881; 15: 0.346 / 0.525 / 0.858
- 24h: 1: 0.351 / 0.521 / 0.888; 2: 0.332 / 0.474 / 0.899; 3: 0.351 / 0.521 / 0.897; 4: 0.335 / 0.494 / 0.894; 5: 0.333 / 0.489 / 0.892; 6: 0.340 / 0.515 / 0.892; 7: 0.337 / 0.504 / 0.894; 8: 0.340 / 0.518 / 0.896; 9: 0.330 / 0.487 / 0.898; 10: 0.341 / 0.515 / 0.894; 11: 0.331 / 0.497 / 0.892; 12: 0.340 / 0.522 / 0.894; 13: 0.333 / 0.496 / 0.891; 14: 0.336 / 0.508 / 0.897; 15: 0.337 / 0.505 / 0.894
- 7d: 1: 0.367 / 0.526 / 0.902; 2: 0.353 / 0.493 / 0.900; 3: 0.360 / 0.510 / 0.901; 4: 0.353 / 0.496 / 0.901; 5: 0.355 / 0.502 / 0.901; 6: 0.355 / 0.504 / 0.901; 7: 0.355 / 0.504 / 0.901; 8: 0.352 / 0.498 / 0.902; 9: 0.353 / 0.504 / 0.902; 10: 0.355 / 0.510 / 0.902; 11: 0.348 / 0.492 / 0.901; 12: 0.354 / 0.507 / 0.902; 13: 0.352 / 0.502 / 0.902; 14: 0.350 / 0.499 / 0.902; 15: 0.353 / 0.505 / 0.901
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.503 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.347 / 0.504 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.345 / 0.498 / 0.900; 15: 0.345 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.076 (body 0.051, range 0.101); 'price stays where it was' would score 0.104; colour right 0.533; typical miss of the close 11.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.113 (body 0.086, range 0.141); 'price stays where it was' would score 0.118; colour right 0.508; typical miss of the close 12.6 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.127 (body 0.094, range 0.160); 'price stays where it was' would score 0.122; colour right 0.518; typical miss of the close 7.8 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.125 (body 0.086, range 0.164); 'price stays where it was' would score 0.130; colour right 0.499; typical miss of the close 9.1 bp; chain ended on the right side 0.516 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.519 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 3.9; 2: 0.196 / 4.4; 3: 0.165 / 6.0; 4: 0.134 / 6.5; 5: 0.121 / 7.2; 6: 0.111 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.080 / 9.9; 12: 0.076 / 10.3; 13: 0.064 / 10.5; 14: 0.066 / 10.6; 15: 0.058 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 110332, probability skill vs chance 0.222, widened contest next: False
  - now: threshold 0.8362, hit rate recent 0.9397 / long run 0.9338
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.311, naive rule 0.538, lift 3.21x
    - 24h: 63 calls (63 a day), hit rate 0.952, chance 0.294, naive rule 0.493, lift 3.23x
    - 7d: 374 calls (53 a day), hit rate 0.941, chance 0.290, naive rule 0.485, lift 3.25x
    - 30d: 1720 calls (57 a day), hit rate 0.938, chance 0.292, naive rule 0.484, lift 3.22x
  - next: threshold 0.5352, hit rate recent 0.5876 / long run 0.5732
    - 6h: 20 calls (81 a day), hit rate 0.600, chance 0.311, lift 1.93x
    - 24h: 89 calls (89 a day), hit rate 0.584, chance 0.294, lift 1.98x
    - 7d: 718 calls (103 a day), hit rate 0.568, chance 0.290, lift 1.96x
    - 30d: 2590 calls (86 a day), hit rate 0.578, chance 0.292, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 540, 0.514; 0.40: 483, 0.566; 0.45: 413, 0.636; 0.50: 360, 0.689; 0.55: 316, 0.731; 0.60: 269, 0.774; 0.65: 224, 0.803; 0.70: 179, 0.836; 0.75: 138, 0.871; 0.80: 95, 0.913; 0.85: 49, 0.952; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 499, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.524; 0.50: 204, 0.557; 0.55: 92, 0.576; 0.60: 14, 0.609; 0.65: 1, 0.667
- **K=5**: model 1791590400, labels learned 110330, probability skill vs chance 0.2128, widened contest next: True
  - now: threshold 0.6864, hit rate recent 0.837 / long run 0.8277
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.194, naive rule 0.444, lift 4.12x
    - 24h: 49 calls (49 a day), hit rate 0.837, chance 0.194, naive rule 0.404, lift 4.32x
    - 7d: 346 calls (49 a day), hit rate 0.821, chance 0.187, naive rule 0.404, lift 4.39x
    - 30d: 1608 calls (54 a day), hit rate 0.832, chance 0.188, naive rule 0.395, lift 4.43x
  - next: threshold 0.4034, hit rate recent 0.4094 / long run 0.4537
    - 6h: 34 calls (139 a day), hit rate 0.353, chance 0.194, lift 1.82x
    - 24h: 156 calls (157 a day), hit rate 0.404, chance 0.194, lift 2.09x
    - 7d: 777 calls (111 a day), hit rate 0.459, chance 0.187, lift 2.45x
    - 30d: 2403 calls (80 a day), hit rate 0.472, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.422; 0.35: 350, 0.487; 0.40: 281, 0.560; 0.45: 229, 0.616; 0.50: 180, 0.665; 0.55: 137, 0.711; 0.60: 107, 0.750; 0.65: 81, 0.792; 0.70: 59, 0.825; 0.75: 33, 0.871; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.388; 0.35: 251, 0.421; 0.40: 160, 0.446; 0.45: 76, 0.463; 0.50: 18, 0.501; 0.55: 2, 0.580
- **K=8**: model 1791936000, labels learned 110327, probability skill vs chance 0.1989, widened contest next: False
  - now: threshold 0.5744, hit rate recent 0.702 / long run 0.7001
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.124, naive rule 0.373, lift 4.83x
    - 24h: 47 calls (47 a day), hit rate 0.723, chance 0.117, naive rule 0.315, lift 6.16x
    - 7d: 337 calls (48 a day), hit rate 0.685, chance 0.120, naive rule 0.331, lift 5.69x
    - 30d: 1571 calls (52 a day), hit rate 0.719, chance 0.122, naive rule 0.330, lift 5.87x
  - next: threshold 0.3405, hit rate recent 0.3785 / long run 0.38
    - 6h: 23 calls (95 a day), hit rate 0.391, chance 0.124, lift 3.15x
    - 24h: 117 calls (118 a day), hit rate 0.359, chance 0.117, lift 3.06x
    - 7d: 649 calls (93 a day), hit rate 0.379, chance 0.120, lift 3.15x
    - 30d: 2216 calls (74 a day), hit rate 0.400, chance 0.122, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 257, 0.421; 0.35: 195, 0.493; 0.40: 148, 0.553; 0.45: 117, 0.595; 0.50: 90, 0.636; 0.55: 65, 0.686; 0.60: 44, 0.732; 0.65: 24, 0.791; 0.70: 9, 0.847; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.352; 0.35: 105, 0.385; 0.40: 42, 0.418; 0.45: 9, 0.446; 0.50: 1, 0.438
- **K=13**: model 1792022400, labels learned 110322, probability skill vs chance 0.186, widened contest next: True
  - now: threshold 0.4138, hit rate recent 0.5171 / long run 0.5679
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.070, naive rule 0.299, lift 4.79x
    - 24h: 64 calls (65 a day), hit rate 0.516, chance 0.075, naive rule 0.273, lift 6.90x
    - 7d: 377 calls (54 a day), hit rate 0.549, chance 0.077, naive rule 0.278, lift 7.17x
    - 30d: 1531 calls (51 a day), hit rate 0.584, chance 0.078, naive rule 0.275, lift 7.46x
  - next: threshold 0.2768, hit rate recent 0.3116 / long run 0.3126
    - 6h: 16 calls (67 a day), hit rate 0.250, chance 0.070, lift 3.59x
    - 24h: 73 calls (74 a day), hit rate 0.315, chance 0.075, lift 4.22x
    - 7d: 418 calls (60 a day), hit rate 0.299, chance 0.077, lift 3.91x
    - 30d: 2051 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.619; 0.50: 25, 0.663; 0.55: 14, 0.716; 0.60: 5, 0.769; 0.65: 1, 0.840
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.326; 0.35: 13, 0.357; 0.40: 2, 0.419; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.327 | -0.56% | 0.900 | 0.533 | 0.251 | 0.400 | 0.075 |
| 6h | 17.665 | 4.59% | 0.914 | 0.517 | 0.251 | 0.433 | 0.510 |
| 24h | 13.342 | 4.84% | 0.898 | 0.493 | 0.251 | 0.491 | 0.636 |
| 7d | 15.863 | 4.27% | 0.900 | 0.499 | 0.251 | 0.490 | 0.644 |
| 30d | 13.699 | 4.07% | 0.900 | 0.500 | 0.251 | 0.495 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.253 | 13.271 | 13.462 | 13.170 | 13.482 | 13.605 | 13.236 | 13.289 | 13.262 | 13.327 |
| 6h | 18.514 | 17.939 | 17.823 | 17.653 | 18.103 | 17.826 | 17.666 | 17.551 | 17.625 | 17.665 |
| 24h | 14.020 | 13.564 | 13.375 | 13.358 | 13.566 | 13.404 | 13.357 | 13.296 | 13.320 | 13.342 |
| 7d | 16.571 | 16.048 | 15.966 | 15.878 | 16.125 | 16.063 | 15.867 | 15.838 | 15.832 | 15.863 |
| 30d | 14.279 | 13.821 | 13.783 | 13.724 | 13.945 | 13.881 | 13.696 | 13.672 | 13.673 | 13.699 |

## Next candle

- candle starting 2026-10-18 18:58 UTC, last close 2364.81
- P(up) 0.5, return quantiles (bp): {'05': -7.033, '10': -5.263, '25': -2.734, '40': -1.035, '50': 0.015, '60': 0.791, '75': 2.396, '90': 4.807, '95': 6.579}
- changepoint probability 0.1092, regime age 117.4 min
- agent weights: empirical 0.004, ewma 0.040, garch 0.086, har 0.188, bocpd 0.016, hmm 0.068, online_qr 0.219, lgbm 0.379

## Learning log

- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- HMM volatility states (sd, bp per minute): [3.34, 6.61, 20.42], current probabilities: [0.815, 0.184, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 19:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.279, 'l_abs': 0.665, 'l_hi': 0.742, 'l_lo': 0.735, 'b05': 0.663, 'b25': 0.667, 'b75': 0.649, 'b95': 0.664}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.353, 1.764, 2.0, 2.427, 2.664, 2.826, 2.851, 2.854, 3.2, 3.363, 3.52, 3.745, 3.595, 4.121]}
- calibration offsets (in sigma): {'05': -0.0215, '10': -0.023, '25': -0.0575, '40': -0.042, '50': -0.015, '60': -0.028, '75': -0.0325, '90': -0.067, '95': -0.0585}
