# ETH-USD 60s candle generator - report

- generated: 2026-10-18 00:24 UTC
- last closed candle: 2026-10-18 00:24 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.000 (1) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.583 (12) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | - | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.542 (24) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.515 (336) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | - | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | - | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | - | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | - | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 1.000 (1) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | - | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | - | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | - | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | - | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.517 (362) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06935, 0.1076] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5274, 'levels': [{'threshold': 0.06935, 'calls_per_day': 137.5, 'win_rate': 0.5742}, {'threshold': 0.1076, 'calls_per_day': 33.9, 'win_rate': 0.636}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 20254, 'rate': 0.5293}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14888 | 0.336 | 0.522 (14645) | 0.593 (1341) | 0.778 (2436) |
| volatility: normal | 14888 | 0.362 | 0.515 (14823) | 0.612 (405) | 0.771 (2157) |
| volatility: wild | 14888 | 0.377 | 0.505 (14844) | 0.648 (165) | 0.767 (2028) |
| session: Asia 00-08 | 14904 | 0.357 | 0.520 (14806) | 0.607 (682) | 0.766 (2193) |
| session: Europe 08-13 | 9300 | 0.352 | 0.513 (9217) | 0.580 (486) | 0.778 (1451) |
| session: US 13-21 | 14880 | 0.367 | 0.509 (14775) | 0.586 (466) | 0.782 (2157) |
| session: late 21-24 | 5580 | 0.349 | 0.513 (5514) | 0.653 (277) | 0.756 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.364 | 0.369 | 0.214 | 0.214 | 0.576 | 0.258 | 0.471 | 1.502 |
| 6h | 360 | 0.338 | 0.334 | 0.243 | 0.261 | 0.543 | 0.247 | 0.428 | 1.310 |
| 24h | 1440 | 0.349 | 0.334 | 0.250 | 0.274 | 0.545 | 0.264 | 0.434 | 1.211 |
| 7d | 10080 | 0.363 | 0.354 | 0.277 | 0.308 | 0.527 | 0.261 | 0.466 | 1.256 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.465 | 1.304 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.364 / 0.576 / 0.900; 2: 0.333 / 0.424 / 0.967; 3: 0.364 / 0.508 / 0.983; 4: 0.363 / 0.559 / 1.000; 5: 0.314 / 0.424 / 0.983; 6: 0.364 / 0.542 / 1.000; 7: 0.354 / 0.492 / 1.000; 8: 0.342 / 0.424 / 0.983; 9: 0.364 / 0.542 / 0.967; 10: 0.353 / 0.508 / 1.000; 11: 0.351 / 0.559 / 0.983; 12: 0.363 / 0.542 / 0.983; 13: 0.322 / 0.373 / 1.000; 14: 0.346 / 0.508 / 1.000; 15: 0.363 / 0.593 / 1.000
- 6h: 1: 0.338 / 0.543 / 0.878; 2: 0.316 / 0.477 / 0.889; 3: 0.332 / 0.540 / 0.889; 4: 0.309 / 0.491 / 0.861; 5: 0.321 / 0.523 / 0.872; 6: 0.318 / 0.520 / 0.881; 7: 0.315 / 0.497 / 0.894; 8: 0.305 / 0.497 / 0.897; 9: 0.313 / 0.489 / 0.908; 10: 0.323 / 0.543 / 0.903; 11: 0.298 / 0.480 / 0.894; 12: 0.315 / 0.517 / 0.903; 13: 0.305 / 0.509 / 0.897; 14: 0.303 / 0.506 / 0.903; 15: 0.302 / 0.471 / 0.903
- 24h: 1: 0.349 / 0.545 / 0.874; 2: 0.329 / 0.480 / 0.897; 3: 0.335 / 0.505 / 0.895; 4: 0.324 / 0.483 / 0.890; 5: 0.332 / 0.502 / 0.894; 6: 0.329 / 0.495 / 0.895; 7: 0.331 / 0.502 / 0.896; 8: 0.327 / 0.491 / 0.894; 9: 0.329 / 0.480 / 0.897; 10: 0.333 / 0.513 / 0.897; 11: 0.319 / 0.476 / 0.892; 12: 0.326 / 0.495 / 0.897; 13: 0.328 / 0.507 / 0.899; 14: 0.323 / 0.495 / 0.897; 15: 0.324 / 0.490 / 0.896
- 7d: 1: 0.363 / 0.527 / 0.902; 2: 0.351 / 0.499 / 0.899; 3: 0.355 / 0.507 / 0.900; 4: 0.350 / 0.497 / 0.899; 5: 0.352 / 0.503 / 0.899; 6: 0.351 / 0.502 / 0.899; 7: 0.351 / 0.503 / 0.900; 8: 0.349 / 0.498 / 0.900; 9: 0.351 / 0.502 / 0.900; 10: 0.352 / 0.507 / 0.900; 11: 0.345 / 0.491 / 0.900; 12: 0.349 / 0.503 / 0.901; 13: 0.349 / 0.503 / 0.901; 14: 0.346 / 0.499 / 0.900; 15: 0.349 / 0.504 / 0.900
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.119 (body 0.075, range 0.164); 'price stays where it was' would score 0.140; colour right 0.458; typical miss of the close 9.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.087, range 0.165); 'price stays where it was' would score 0.144; colour right 0.514; typical miss of the close 6.9 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.136 (body 0.098, range 0.173); 'price stays where it was' would score 0.141; colour right 0.504; typical miss of the close 5.5 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.162); 'price stays where it was' would score 0.130; colour right 0.497; typical miss of the close 8.6 bp; chain ended on the right side 0.504 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.518 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.0; 2: 0.196 / 4.4; 3: 0.165 / 6.0; 4: 0.134 / 6.6; 5: 0.121 / 7.3; 6: 0.110 / 7.8; 7: 0.102 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.5; 10: 0.085 / 9.3; 11: 0.080 / 10.0; 12: 0.076 / 10.3; 13: 0.064 / 10.7; 14: 0.066 / 10.8; 15: 0.058 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 109218, probability skill vs chance 0.2198, widened contest next: True
  - now: threshold 0.8381, hit rate recent 0.9193 / long run 0.9318
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.268, naive rule 0.446, lift 3.50x
    - 24h: 61 calls (61 a day), hit rate 0.869, chance 0.302, naive rule 0.509, lift 2.87x
    - 7d: 387 calls (55 a day), hit rate 0.933, chance 0.292, naive rule 0.490, lift 3.19x
    - 30d: 1720 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5512, hit rate recent 0.5385 / long run 0.5712
    - 6h: 16 calls (65 a day), hit rate 0.562, chance 0.268, lift 2.10x
    - 24h: 113 calls (113 a day), hit rate 0.575, chance 0.302, lift 1.90x
    - 7d: 721 calls (103 a day), hit rate 0.569, chance 0.292, lift 1.95x
    - 30d: 2585 calls (86 a day), hit rate 0.580, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.564; 0.45: 414, 0.634; 0.50: 361, 0.687; 0.55: 316, 0.729; 0.60: 270, 0.773; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 139, 0.870; 0.80: 95, 0.911; 0.85: 49, 0.949; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.525; 0.50: 204, 0.558; 0.55: 92, 0.578; 0.60: 14, 0.606; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 109216, probability skill vs chance 0.2133, widened contest next: True
  - now: threshold 0.6911, hit rate recent 0.8394 / long run 0.8268
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.195, naive rule 0.422, lift 4.19x
    - 24h: 51 calls (51 a day), hit rate 0.824, chance 0.203, naive rule 0.444, lift 4.06x
    - 7d: 350 calls (50 a day), hit rate 0.820, chance 0.188, naive rule 0.406, lift 4.37x
    - 30d: 1614 calls (54 a day), hit rate 0.830, chance 0.188, naive rule 0.395, lift 4.42x
  - next: threshold 0.4052, hit rate recent 0.4194 / long run 0.462
    - 6h: 38 calls (155 a day), hit rate 0.368, chance 0.195, lift 1.88x
    - 24h: 142 calls (143 a day), hit rate 0.451, chance 0.203, lift 2.22x
    - 7d: 708 calls (101 a day), hit rate 0.466, chance 0.188, lift 2.48x
    - 30d: 2326 calls (78 a day), hit rate 0.477, chance 0.188, lift 2.54x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.421; 0.35: 352, 0.486; 0.40: 282, 0.559; 0.45: 231, 0.614; 0.50: 181, 0.666; 0.55: 138, 0.710; 0.60: 108, 0.750; 0.65: 81, 0.792; 0.70: 60, 0.823; 0.75: 33, 0.867; 0.80: 10, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 251, 0.425; 0.40: 160, 0.451; 0.45: 76, 0.466; 0.50: 18, 0.501; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 109213, probability skill vs chance 0.1973, widened contest next: True
  - now: threshold 0.5791, hit rate recent 0.724 / long run 0.701
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.129, naive rule 0.348, lift 6.48x
    - 24h: 48 calls (48 a day), hit rate 0.750, chance 0.129, naive rule 0.361, lift 5.80x
    - 7d: 351 calls (50 a day), hit rate 0.687, chance 0.121, naive rule 0.333, lift 5.66x
    - 30d: 1583 calls (53 a day), hit rate 0.717, chance 0.123, naive rule 0.332, lift 5.84x
  - next: threshold 0.3414, hit rate recent 0.3344 / long run 0.3773
    - 6h: 30 calls (123 a day), hit rate 0.267, chance 0.129, lift 2.07x
    - 24h: 120 calls (121 a day), hit rate 0.383, chance 0.129, lift 2.96x
    - 7d: 634 calls (91 a day), hit rate 0.372, chance 0.121, lift 3.07x
    - 30d: 2179 calls (73 a day), hit rate 0.402, chance 0.123, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.421; 0.35: 195, 0.494; 0.40: 149, 0.554; 0.45: 117, 0.597; 0.50: 90, 0.637; 0.55: 66, 0.687; 0.60: 44, 0.730; 0.65: 24, 0.785; 0.70: 9, 0.833; 0.75: 1, 0.760
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.355; 0.35: 106, 0.387; 0.40: 43, 0.420; 0.45: 9, 0.447; 0.50: 1, 0.406
- **K=13**: model 1792022400, labels learned 109208, probability skill vs chance 0.1816, widened contest next: False
  - now: threshold 0.4193, hit rate recent 0.5849 / long run 0.5759
    - 6h: 12 calls (50 a day), hit rate 0.667, chance 0.077, naive rule 0.272, lift 8.68x
    - 24h: 53 calls (54 a day), hit rate 0.623, chance 0.078, naive rule 0.311, lift 7.96x
    - 7d: 367 calls (53 a day), hit rate 0.564, chance 0.077, naive rule 0.277, lift 7.37x
    - 30d: 1528 calls (51 a day), hit rate 0.587, chance 0.078, naive rule 0.275, lift 7.50x
  - next: threshold 0.2829, hit rate recent 0.2919 / long run 0.3101
    - 6h: 14 calls (58 a day), hit rate 0.214, chance 0.077, lift 2.79x
    - 24h: 47 calls (47 a day), hit rate 0.319, chance 0.078, lift 4.08x
    - 7d: 419 calls (60 a day), hit rate 0.305, chance 0.077, lift 3.99x
    - 30d: 2034 calls (68 a day), hit rate 0.313, chance 0.078, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.513; 0.40: 62, 0.566; 0.45: 41, 0.621; 0.50: 26, 0.661; 0.55: 14, 0.705; 0.60: 5, 0.750; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.324; 0.35: 13, 0.358; 0.40: 2, 0.406

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.552 | -0.23% | 0.900 | 0.517 | 0.243 | 0.593 | -0.009 |
| 6h | 14.640 | 10.17% | 0.900 | 0.522 | 0.249 | 0.523 | 0.684 |
| 24h | 10.478 | 8.04% | 0.894 | 0.497 | 0.250 | 0.493 | 0.658 |
| 7d | 15.389 | 4.45% | 0.901 | 0.501 | 0.251 | 0.492 | 0.657 |
| 30d | 13.901 | 4.11% | 0.900 | 0.500 | 0.251 | 0.495 | 0.677 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.526 | 11.645 | 11.645 | 11.599 | 11.544 | 11.727 | 11.741 | 11.617 | 11.614 | 11.552 |
| 6h | 16.298 | 15.155 | 14.559 | 14.636 | 14.852 | 14.718 | 14.711 | 14.646 | 14.640 | 14.640 |
| 24h | 11.394 | 10.633 | 10.635 | 10.515 | 10.634 | 10.717 | 10.474 | 10.463 | 10.459 | 10.478 |
| 7d | 16.105 | 15.567 | 15.488 | 15.404 | 15.655 | 15.597 | 15.394 | 15.367 | 15.359 | 15.389 |
| 30d | 14.497 | 14.027 | 13.987 | 13.928 | 14.154 | 14.087 | 13.900 | 13.875 | 13.875 | 13.901 |

## Next candle

- candle starting 2026-10-18 00:24 UTC, last close 2400.25
- P(up) 0.5604, return quantiles (bp): {'05': -7.56, '10': -5.786, '25': -2.161, '40': -0.281, '50': 0.393, '60': 1.258, '75': 2.718, '90': 5.591, '95': 7.301}
- changepoint probability 0.0399, regime age 99.2 min
- agent weights: empirical 0.003, ewma 0.016, garch 0.205, har 0.213, bocpd 0.049, hmm 0.073, online_qr 0.196, lgbm 0.246

## Learning log

- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.41, 6.6, 20.67], current probabilities: [0.723, 0.275, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 00:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.274, 'l_abs': 0.674, 'l_hi': 0.719, 'l_lo': 0.716, 'b05': 0.673, 'b25': 0.649, 'b75': 0.652, 'b95': 0.662}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.538, 1.85, 2.414, 2.546, 2.58, 2.683, 2.761, 2.709, 2.805, 3.007, 3.085, 3.153, 3.413, 3.611]}
- calibration offsets (in sigma): {'05': -0.0085, '10': -0.017, '25': 0.0775, '40': 0.102, '50': 0.065, '60': 0.048, '75': 0.0025, '90': -0.003, '95': -0.0615}
