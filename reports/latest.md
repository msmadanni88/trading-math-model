# ETH-USD 60s candle generator - report

- generated: 2026-10-18 21:23 UTC
- last closed candle: 2026-10-18 21:23 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.577 (85) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.553 (711) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.566 (129) | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.518 (1273) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.502 (17822) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.600 (35) | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | 0.319 (69) | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | 0.467 (60) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | 0.586 (87) | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 0.942 (52) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | 0.431 (137) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | 0.795 (44) | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | 0.410 (100) | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | 0.650 (40) | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.504 (19769) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06657, 0.1003] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5257, 'levels': [{'threshold': 0.06657, 'calls_per_day': 137.8, 'win_rate': 0.5582}, {'threshold': 0.1003, 'calls_per_day': 33.1, 'win_rate': 0.6223}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 21503, 'rate': 0.5286}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15308 | 0.336 | 0.521 (15058) | 0.591 (1415) | 0.773 (2515) |
| volatility: normal | 15307 | 0.362 | 0.514 (15239) | 0.609 (445) | 0.770 (2230) |
| volatility: wild | 15308 | 0.377 | 0.506 (15264) | 0.644 (180) | 0.768 (2071) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15256) | 0.602 (752) | 0.766 (2261) |
| session: Europe 08-13 | 9600 | 0.352 | 0.513 (9513) | 0.577 (523) | 0.776 (1511) |
| session: US 13-21 | 15360 | 0.367 | 0.510 (15255) | 0.588 (488) | 0.776 (2224) |
| session: late 21-24 | 5603 | 0.350 | 0.514 (5537) | 0.653 (277) | 0.756 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.391 | 0.342 | 0.290 | 0.290 | 0.533 | 0.295 | 0.487 | 1.430 |
| 6h | 360 | 0.383 | 0.350 | 0.259 | 0.292 | 0.558 | 0.292 | 0.475 | 1.178 |
| 24h | 1440 | 0.357 | 0.350 | 0.261 | 0.291 | 0.523 | 0.258 | 0.456 | 1.142 |
| 7d | 10080 | 0.367 | 0.357 | 0.279 | 0.311 | 0.526 | 0.263 | 0.471 | 1.199 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.464 | 1.296 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.391 / 0.533 / 0.900; 2: 0.367 / 0.500 / 0.900; 3: 0.373 / 0.517 / 0.883; 4: 0.388 / 0.583 / 0.900; 5: 0.373 / 0.483 / 0.917; 6: 0.354 / 0.450 / 0.900; 7: 0.355 / 0.483 / 0.917; 8: 0.343 / 0.400 / 0.883; 9: 0.356 / 0.483 / 0.850; 10: 0.360 / 0.483 / 0.883; 11: 0.358 / 0.517 / 0.883; 12: 0.358 / 0.483 / 0.900; 13: 0.376 / 0.583 / 0.933; 14: 0.399 / 0.583 / 0.883; 15: 0.356 / 0.483 / 0.917
- 6h: 1: 0.383 / 0.558 / 0.906; 2: 0.355 / 0.469 / 0.903; 3: 0.363 / 0.486 / 0.894; 4: 0.369 / 0.553 / 0.906; 5: 0.345 / 0.450 / 0.894; 6: 0.346 / 0.481 / 0.886; 7: 0.351 / 0.483 / 0.894; 8: 0.356 / 0.481 / 0.892; 9: 0.357 / 0.500 / 0.883; 10: 0.359 / 0.503 / 0.900; 11: 0.342 / 0.467 / 0.897; 12: 0.362 / 0.533 / 0.897; 13: 0.357 / 0.528 / 0.906; 14: 0.369 / 0.558 / 0.908; 15: 0.362 / 0.533 / 0.908
- 24h: 1: 0.357 / 0.523 / 0.891; 2: 0.337 / 0.475 / 0.899; 3: 0.354 / 0.509 / 0.894; 4: 0.343 / 0.505 / 0.897; 5: 0.335 / 0.475 / 0.892; 6: 0.343 / 0.508 / 0.890; 7: 0.340 / 0.496 / 0.890; 8: 0.345 / 0.513 / 0.887; 9: 0.337 / 0.499 / 0.884; 10: 0.342 / 0.505 / 0.885; 11: 0.335 / 0.497 / 0.885; 12: 0.343 / 0.520 / 0.883; 13: 0.340 / 0.509 / 0.884; 14: 0.343 / 0.518 / 0.885; 15: 0.340 / 0.508 / 0.886
- 7d: 1: 0.367 / 0.526 / 0.902; 2: 0.354 / 0.493 / 0.900; 3: 0.360 / 0.509 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.501 / 0.900; 6: 0.355 / 0.503 / 0.900; 7: 0.355 / 0.504 / 0.900; 8: 0.353 / 0.498 / 0.900; 9: 0.354 / 0.503 / 0.900; 10: 0.355 / 0.508 / 0.900; 11: 0.349 / 0.491 / 0.900; 12: 0.354 / 0.506 / 0.901; 13: 0.352 / 0.504 / 0.901; 14: 0.351 / 0.501 / 0.900; 15: 0.353 / 0.504 / 0.900
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.503 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.899; 12: 0.347 / 0.504 / 0.899; 13: 0.347 / 0.503 / 0.899; 14: 0.345 / 0.498 / 0.899; 15: 0.345 / 0.498 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.097 (body 0.060, range 0.134); 'price stays where it was' would score 0.134; colour right 0.567; typical miss of the close 13.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.130 (body 0.093, range 0.167); 'price stays where it was' would score 0.143; colour right 0.494; typical miss of the close 11.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.127 (body 0.092, range 0.162); 'price stays where it was' would score 0.123; colour right 0.517; typical miss of the close 8.6 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.125 (body 0.086, range 0.165); 'price stays where it was' would score 0.130; colour right 0.497; typical miss of the close 9.2 bp; chain ended on the right side 0.517 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.7 bp; chain ended on the right side 0.520 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 3.9; 2: 0.196 / 4.4; 3: 0.164 / 6.0; 4: 0.134 / 6.5; 5: 0.121 / 7.2; 6: 0.110 / 7.7; 7: 0.103 / 8.0; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.085 / 9.3; 11: 0.081 / 9.9; 12: 0.076 / 10.3; 13: 0.064 / 10.5; 14: 0.066 / 10.6; 15: 0.058 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 110477, probability skill vs chance 0.2217, widened contest next: False
  - now: threshold 0.8362, hit rate recent 0.9263 / long run 0.9325
    - 6h: 8 calls (32 a day), hit rate 0.875, chance 0.303, naive rule 0.510, lift 2.89x
    - 24h: 56 calls (56 a day), hit rate 0.929, chance 0.293, naive rule 0.499, lift 3.17x
    - 7d: 375 calls (54 a day), hit rate 0.939, chance 0.289, naive rule 0.482, lift 3.25x
    - 30d: 1719 calls (57 a day), hit rate 0.938, chance 0.292, naive rule 0.484, lift 3.21x
  - next: threshold 0.5352, hit rate recent 0.5861 / long run 0.5734
    - 6h: 23 calls (93 a day), hit rate 0.652, chance 0.303, lift 2.15x
    - 24h: 91 calls (91 a day), hit rate 0.582, chance 0.293, lift 1.99x
    - 7d: 725 calls (104 a day), hit rate 0.567, chance 0.289, lift 1.96x
    - 30d: 2598 calls (87 a day), hit rate 0.578, chance 0.292, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 540, 0.514; 0.40: 483, 0.566; 0.45: 413, 0.636; 0.50: 360, 0.689; 0.55: 315, 0.731; 0.60: 269, 0.774; 0.65: 224, 0.803; 0.70: 179, 0.836; 0.75: 138, 0.871; 0.80: 95, 0.913; 0.85: 49, 0.952; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 499, 0.460; 0.40: 408, 0.490; 0.45: 312, 0.524; 0.50: 203, 0.556; 0.55: 92, 0.576; 0.60: 14, 0.611; 0.65: 1, 0.679
- **K=5**: model 1791590400, labels learned 110475, probability skill vs chance 0.2127, widened contest next: False
  - now: threshold 0.6864, hit rate recent 0.8051 / long run 0.8245
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.190, naive rule 0.425, lift 3.51x
    - 24h: 46 calls (46 a day), hit rate 0.783, chance 0.189, naive rule 0.401, lift 4.13x
    - 7d: 349 calls (50 a day), hit rate 0.814, chance 0.186, naive rule 0.400, lift 4.38x
    - 30d: 1610 calls (54 a day), hit rate 0.832, chance 0.188, naive rule 0.394, lift 4.43x
  - next: threshold 0.4034, hit rate recent 0.4363 / long run 0.4556
    - 6h: 32 calls (131 a day), hit rate 0.469, chance 0.190, lift 2.47x
    - 24h: 150 calls (151 a day), hit rate 0.427, chance 0.189, lift 2.25x
    - 7d: 786 calls (112 a day), hit rate 0.459, chance 0.186, lift 2.47x
    - 30d: 2413 calls (80 a day), hit rate 0.473, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.422; 0.35: 350, 0.487; 0.40: 281, 0.560; 0.45: 229, 0.616; 0.50: 180, 0.665; 0.55: 137, 0.710; 0.60: 107, 0.750; 0.65: 81, 0.792; 0.70: 59, 0.825; 0.75: 33, 0.871; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.388; 0.35: 251, 0.421; 0.40: 160, 0.447; 0.45: 76, 0.463; 0.50: 18, 0.502; 0.55: 2, 0.588
- **K=8**: model 1791936000, labels learned 110472, probability skill vs chance 0.1968, widened contest next: False
  - now: threshold 0.5744, hit rate recent 0.6785 / long run 0.6976
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.127, naive rule 0.364, lift 4.72x
    - 24h: 42 calls (42 a day), hit rate 0.643, chance 0.114, naive rule 0.312, lift 5.62x
    - 7d: 337 calls (48 a day), hit rate 0.682, chance 0.120, naive rule 0.329, lift 5.68x
    - 30d: 1572 calls (52 a day), hit rate 0.718, chance 0.122, naive rule 0.330, lift 5.87x
  - next: threshold 0.3405, hit rate recent 0.4003 / long run 0.3823
    - 6h: 25 calls (103 a day), hit rate 0.440, chance 0.127, lift 3.46x
    - 24h: 112 calls (113 a day), hit rate 0.402, chance 0.114, lift 3.51x
    - 7d: 653 calls (93 a day), hit rate 0.380, chance 0.120, lift 3.16x
    - 30d: 2224 calls (74 a day), hit rate 0.401, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 257, 0.421; 0.35: 195, 0.493; 0.40: 148, 0.553; 0.45: 117, 0.594; 0.50: 90, 0.635; 0.55: 65, 0.686; 0.60: 44, 0.732; 0.65: 24, 0.788; 0.70: 9, 0.841; 0.75: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.352; 0.35: 105, 0.385; 0.40: 42, 0.418; 0.45: 9, 0.446; 0.50: 1, 0.455
- **K=13**: model 1792022400, labels learned 110467, probability skill vs chance 0.1787, widened contest next: True
  - now: threshold 0.4138, hit rate recent 0.5012 / long run 0.5654
    - 6h: 15 calls (63 a day), hit rate 0.400, chance 0.061, naive rule 0.218, lift 6.57x
    - 24h: 64 calls (65 a day), hit rate 0.469, chance 0.073, naive rule 0.263, lift 6.45x
    - 7d: 382 calls (55 a day), hit rate 0.545, chance 0.076, naive rule 0.274, lift 7.18x
    - 30d: 1534 calls (51 a day), hit rate 0.584, chance 0.078, naive rule 0.274, lift 7.47x
  - next: threshold 0.2768, hit rate recent 0.2951 / long run 0.3108
    - 6h: 17 calls (71 a day), hit rate 0.176, chance 0.061, lift 2.90x
    - 24h: 77 calls (78 a day), hit rate 0.312, chance 0.073, lift 4.29x
    - 7d: 423 calls (61 a day), hit rate 0.296, chance 0.076, lift 3.90x
    - 30d: 2052 calls (68 a day), hit rate 0.313, chance 0.078, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.511; 0.40: 61, 0.564; 0.45: 41, 0.619; 0.50: 25, 0.662; 0.55: 14, 0.711; 0.60: 5, 0.759; 0.65: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.326; 0.35: 13, 0.358; 0.40: 2, 0.429; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.209 | -1.40% | 0.917 | 0.567 | 0.253 | 0.433 | 0.124 |
| 6h | 17.415 | 3.34% | 0.914 | 0.522 | 0.251 | 0.447 | 0.588 |
| 24h | 14.784 | 5.03% | 0.899 | 0.494 | 0.251 | 0.490 | 0.638 |
| 7d | 16.008 | 4.27% | 0.901 | 0.500 | 0.251 | 0.490 | 0.644 |
| 30d | 13.696 | 4.08% | 0.900 | 0.500 | 0.251 | 0.495 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 15.985 | 16.055 | 16.076 | 16.200 | 15.833 | 15.985 | 16.022 | 15.954 | 15.982 | 16.209 |
| 6h | 18.017 | 17.559 | 17.544 | 17.455 | 17.559 | 17.646 | 17.366 | 17.404 | 17.378 | 17.415 |
| 24h | 15.566 | 15.030 | 14.820 | 14.809 | 15.004 | 14.844 | 14.795 | 14.744 | 14.758 | 14.784 |
| 7d | 16.723 | 16.193 | 16.110 | 16.026 | 16.267 | 16.212 | 16.012 | 15.984 | 15.977 | 16.008 |
| 30d | 14.278 | 13.819 | 13.781 | 13.721 | 13.941 | 13.878 | 13.693 | 13.669 | 13.670 | 13.696 |

## Next candle

- candle starting 2026-10-18 21:23 UTC, last close 2358.85
- P(up) 0.4909, return quantiles (bp): {'05': -8.398, '10': -5.955, '25': -3.248, '40': -1.192, '50': -0.102, '60': 1.034, '75': 2.79, '90': 5.636, '95': 8.149}
- changepoint probability 0.0713, regime age 72.7 min
- agent weights: empirical 0.003, ewma 0.039, garch 0.102, har 0.180, bocpd 0.031, hmm 0.059, online_qr 0.259, lgbm 0.325

## Learning log

- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- HMM volatility states (sd, bp per minute): [3.34, 6.61, 20.42], current probabilities: [0.266, 0.731, 0.004]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 21:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.333, 'l_abs': 0.674, 'l_hi': 0.752, 'l_lo': 0.739, 'b05': 0.69, 'b25': 0.68, 'b75': 0.651, 'b95': 0.662}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.511, 2.008, 2.278, 2.82, 3.287, 3.284, 3.588, 3.969, 4.109, 4.319, 4.611, 4.62, 4.804, 5.084]}
- calibration offsets (in sigma): {'05': -0.019, '10': 0.012, '25': -0.035, '40': -0.012, '50': 0.0, '60': 0.012, '75': -0.025, '90': -0.062, '95': -0.051}
