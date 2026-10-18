# ETH-USD 60s candle generator - report

- generated: 2026-10-18 23:27 UTC
- last closed candle: 2026-10-18 23:27 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.602 (93) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.551 (768) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.566 (136) | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.517 (1397) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.505 (19558) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.583 (36) | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | 0.304 (79) | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | 0.460 (63) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | 0.580 (100) | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 0.946 (55) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | 0.433 (150) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | 0.783 (46) | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | 0.391 (115) | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | 0.643 (42) | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.507 (21698) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06657, 0.1003] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5257, 'levels': [{'threshold': 0.06657, 'calls_per_day': 137.8, 'win_rate': 0.5582}, {'threshold': 0.1003, 'calls_per_day': 33.1, 'win_rate': 0.6223}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 21627, 'rate': 0.5285}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15349 | 0.336 | 0.522 (15099) | 0.591 (1416) | 0.773 (2515) |
| volatility: normal | 15349 | 0.362 | 0.514 (15281) | 0.609 (447) | 0.770 (2237) |
| volatility: wild | 15349 | 0.377 | 0.507 (15305) | 0.641 (184) | 0.767 (2074) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15256) | 0.602 (752) | 0.766 (2261) |
| session: Europe 08-13 | 9600 | 0.352 | 0.513 (9513) | 0.577 (523) | 0.776 (1511) |
| session: US 13-21 | 15360 | 0.367 | 0.510 (15255) | 0.588 (488) | 0.776 (2224) |
| session: late 21-24 | 5727 | 0.350 | 0.514 (5661) | 0.651 (284) | 0.754 (830) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.352 | 0.353 | 0.306 | 0.306 | 0.483 | 0.225 | 0.479 | 1.268 |
| 6h | 360 | 0.371 | 0.360 | 0.286 | 0.307 | 0.517 | 0.261 | 0.481 | 1.206 |
| 24h | 1440 | 0.360 | 0.354 | 0.266 | 0.294 | 0.519 | 0.258 | 0.461 | 1.136 |
| 7d | 10080 | 0.367 | 0.357 | 0.280 | 0.311 | 0.526 | 0.263 | 0.472 | 1.200 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.464 | 1.296 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.352 / 0.483 / 0.917; 2: 0.353 / 0.467 / 0.917; 3: 0.353 / 0.550 / 0.933; 4: 0.357 / 0.533 / 0.900; 5: 0.378 / 0.583 / 0.917; 6: 0.368 / 0.550 / 0.933; 7: 0.363 / 0.583 / 0.933; 8: 0.368 / 0.567 / 0.933; 9: 0.365 / 0.583 / 0.950; 10: 0.352 / 0.533 / 0.967; 11: 0.393 / 0.633 / 0.967; 12: 0.354 / 0.550 / 0.983; 13: 0.363 / 0.567 / 0.967; 14: 0.342 / 0.500 / 0.983; 15: 0.375 / 0.583 / 0.983
- 6h: 1: 0.371 / 0.517 / 0.908; 2: 0.360 / 0.478 / 0.906; 3: 0.363 / 0.511 / 0.908; 4: 0.362 / 0.519 / 0.906; 5: 0.348 / 0.472 / 0.903; 6: 0.345 / 0.486 / 0.894; 7: 0.358 / 0.508 / 0.903; 8: 0.353 / 0.478 / 0.894; 9: 0.350 / 0.514 / 0.878; 10: 0.354 / 0.508 / 0.892; 11: 0.350 / 0.514 / 0.889; 12: 0.350 / 0.522 / 0.881; 13: 0.350 / 0.533 / 0.886; 14: 0.357 / 0.564 / 0.878; 15: 0.348 / 0.506 / 0.886
- 24h: 1: 0.360 / 0.519 / 0.896; 2: 0.342 / 0.473 / 0.906; 3: 0.358 / 0.516 / 0.903; 4: 0.348 / 0.497 / 0.907; 5: 0.340 / 0.481 / 0.901; 6: 0.347 / 0.507 / 0.897; 7: 0.347 / 0.504 / 0.898; 8: 0.352 / 0.513 / 0.894; 9: 0.340 / 0.497 / 0.890; 10: 0.347 / 0.503 / 0.891; 11: 0.344 / 0.514 / 0.890; 12: 0.348 / 0.521 / 0.889; 13: 0.344 / 0.500 / 0.889; 14: 0.350 / 0.522 / 0.890; 15: 0.348 / 0.516 / 0.890
- 7d: 1: 0.367 / 0.526 / 0.902; 2: 0.354 / 0.492 / 0.899; 3: 0.360 / 0.509 / 0.900; 4: 0.354 / 0.498 / 0.899; 5: 0.356 / 0.502 / 0.899; 6: 0.355 / 0.504 / 0.899; 7: 0.355 / 0.505 / 0.899; 8: 0.353 / 0.498 / 0.899; 9: 0.354 / 0.504 / 0.899; 10: 0.356 / 0.509 / 0.899; 11: 0.349 / 0.493 / 0.899; 12: 0.354 / 0.506 / 0.900; 13: 0.353 / 0.504 / 0.900; 14: 0.351 / 0.502 / 0.899; 15: 0.354 / 0.504 / 0.899
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.348 / 0.503 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.899; 12: 0.347 / 0.503 / 0.899; 13: 0.347 / 0.503 / 0.899; 14: 0.345 / 0.499 / 0.899; 15: 0.345 / 0.498 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.139 (body 0.086, range 0.193); 'price stays where it was' would score 0.154; colour right 0.583; typical miss of the close 8.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.112 (body 0.070, range 0.155); 'price stays where it was' would score 0.134; colour right 0.531; typical miss of the close 10.6 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.127 (body 0.091, range 0.162); 'price stays where it was' would score 0.122; colour right 0.521; typical miss of the close 8.4 bp; chain ended on the right side 0.594 of 96 chains; n=1440
- 7d: match 0.125 (body 0.086, range 0.165); 'price stays where it was' would score 0.130; colour right 0.499; typical miss of the close 9.2 bp; chain ended on the right side 0.526 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.522 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 3.9; 2: 0.195 / 4.4; 3: 0.164 / 6.0; 4: 0.134 / 6.5; 5: 0.121 / 7.2; 6: 0.110 / 7.7; 7: 0.103 / 8.0; 8: 0.096 / 8.4; 9: 0.086 / 8.5; 10: 0.085 / 9.3; 11: 0.081 / 9.9; 12: 0.075 / 10.3; 13: 0.064 / 10.5; 14: 0.065 / 10.6; 15: 0.058 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 110601, probability skill vs chance 0.2198, widened contest next: False
  - now: threshold 0.8362, hit rate recent 0.9299 / long run 0.9328
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.293, naive rule 0.479, lift 3.03x
    - 24h: 57 calls (57 a day), hit rate 0.947, chance 0.298, naive rule 0.498, lift 3.18x
    - 7d: 374 calls (53 a day), hit rate 0.939, chance 0.288, naive rule 0.481, lift 3.25x
    - 30d: 1718 calls (57 a day), hit rate 0.938, chance 0.292, naive rule 0.484, lift 3.21x
  - next: threshold 0.5352, hit rate recent 0.5747 / long run 0.5727
    - 6h: 32 calls (130 a day), hit rate 0.594, chance 0.293, lift 2.03x
    - 24h: 100 calls (100 a day), hit rate 0.580, chance 0.298, lift 1.95x
    - 7d: 737 calls (105 a day), hit rate 0.566, chance 0.288, lift 1.96x
    - 30d: 2604 calls (87 a day), hit rate 0.578, chance 0.292, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 540, 0.514; 0.40: 483, 0.566; 0.45: 413, 0.636; 0.50: 360, 0.689; 0.55: 315, 0.731; 0.60: 269, 0.774; 0.65: 224, 0.802; 0.70: 178, 0.836; 0.75: 138, 0.871; 0.80: 95, 0.913; 0.85: 49, 0.951; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 499, 0.460; 0.40: 408, 0.490; 0.45: 312, 0.523; 0.50: 203, 0.556; 0.55: 92, 0.576; 0.60: 14, 0.610; 0.65: 1, 0.679
- **K=5**: model 1791590400, labels learned 110599, probability skill vs chance 0.2082, widened contest next: False
  - now: threshold 0.6864, hit rate recent 0.7949 / long run 0.8234
    - 6h: 10 calls (41 a day), hit rate 0.500, chance 0.166, naive rule 0.364, lift 3.02x
    - 24h: 46 calls (46 a day), hit rate 0.783, chance 0.187, naive rule 0.390, lift 4.18x
    - 7d: 347 calls (50 a day), hit rate 0.810, chance 0.185, naive rule 0.397, lift 4.38x
    - 30d: 1608 calls (54 a day), hit rate 0.831, chance 0.188, naive rule 0.394, lift 4.43x
  - next: threshold 0.4034, hit rate recent 0.44 / long run 0.4558
    - 6h: 33 calls (135 a day), hit rate 0.515, chance 0.166, lift 3.11x
    - 24h: 154 calls (155 a day), hit rate 0.429, chance 0.187, lift 2.29x
    - 7d: 797 calls (114 a day), hit rate 0.458, chance 0.185, lift 2.48x
    - 30d: 2422 calls (81 a day), hit rate 0.472, chance 0.188, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.421; 0.35: 350, 0.487; 0.40: 281, 0.559; 0.45: 229, 0.615; 0.50: 180, 0.665; 0.55: 137, 0.710; 0.60: 107, 0.750; 0.65: 80, 0.791; 0.70: 59, 0.824; 0.75: 33, 0.870; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 251, 0.421; 0.40: 160, 0.447; 0.45: 76, 0.463; 0.50: 18, 0.502; 0.55: 2, 0.588
- **K=8**: model 1791936000, labels learned 110596, probability skill vs chance 0.1918, widened contest next: False
  - now: threshold 0.5744, hit rate recent 0.6725 / long run 0.6969
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.103, naive rule 0.265, lift 4.32x
    - 24h: 42 calls (42 a day), hit rate 0.643, chance 0.112, naive rule 0.297, lift 5.73x
    - 7d: 334 calls (48 a day), hit rate 0.680, chance 0.119, naive rule 0.326, lift 5.69x
    - 30d: 1571 calls (52 a day), hit rate 0.719, chance 0.122, naive rule 0.330, lift 5.87x
  - next: threshold 0.3405, hit rate recent 0.3678 / long run 0.3795
    - 6h: 33 calls (136 a day), hit rate 0.364, chance 0.103, lift 3.54x
    - 24h: 119 calls (120 a day), hit rate 0.387, chance 0.112, lift 3.44x
    - 7d: 665 calls (95 a day), hit rate 0.377, chance 0.119, lift 3.16x
    - 30d: 2236 calls (75 a day), hit rate 0.400, chance 0.122, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 257, 0.421; 0.35: 194, 0.493; 0.40: 148, 0.553; 0.45: 116, 0.594; 0.50: 90, 0.635; 0.55: 65, 0.686; 0.60: 44, 0.732; 0.65: 24, 0.789; 0.70: 9, 0.842; 0.75: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.352; 0.35: 105, 0.384; 0.40: 42, 0.417; 0.45: 9, 0.446; 0.50: 1, 0.455
- **K=13**: model 1792022400, labels learned 110591, probability skill vs chance 0.175, widened contest next: True
  - now: threshold 0.4138, hit rate recent 0.4933 / long run 0.5642
    - 6h: 13 calls (54 a day), hit rate 0.385, chance 0.074, naive rule 0.226, lift 5.20x
    - 24h: 64 calls (65 a day), hit rate 0.469, chance 0.075, naive rule 0.259, lift 6.27x
    - 7d: 380 calls (54 a day), hit rate 0.542, chance 0.076, naive rule 0.273, lift 7.15x
    - 30d: 1534 calls (51 a day), hit rate 0.584, chance 0.078, naive rule 0.274, lift 7.47x
  - next: threshold 0.2768, hit rate recent 0.2794 / long run 0.3089
    - 6h: 23 calls (96 a day), hit rate 0.217, chance 0.074, lift 2.94x
    - 24h: 80 calls (81 a day), hit rate 0.300, chance 0.075, lift 4.01x
    - 7d: 432 calls (62 a day), hit rate 0.294, chance 0.076, lift 3.88x
    - 30d: 2058 calls (69 a day), hit rate 0.312, chance 0.078, lift 3.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.511; 0.40: 61, 0.563; 0.45: 41, 0.618; 0.50: 25, 0.663; 0.55: 14, 0.712; 0.60: 5, 0.759; 0.65: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.325; 0.35: 13, 0.358; 0.40: 2, 0.429; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 20.151 | 1.82% | 0.883 | 0.467 | 0.255 | 0.383 | 0.286 |
| 6h | 18.740 | 3.64% | 0.911 | 0.519 | 0.251 | 0.478 | 0.576 |
| 24h | 14.140 | 3.11% | 0.900 | 0.495 | 0.251 | 0.488 | 0.625 |
| 7d | 16.132 | 4.27% | 0.901 | 0.499 | 0.251 | 0.491 | 0.642 |
| 30d | 13.712 | 4.08% | 0.900 | 0.500 | 0.251 | 0.495 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 20.525 | 19.960 | 20.196 | 19.939 | 20.174 | 20.325 | 20.221 | 20.199 | 20.064 | 20.151 |
| 6h | 19.448 | 18.896 | 18.810 | 18.769 | 18.994 | 18.949 | 18.756 | 18.783 | 18.710 | 18.740 |
| 24h | 14.594 | 14.275 | 14.210 | 14.166 | 14.366 | 14.246 | 14.144 | 14.105 | 14.113 | 14.140 |
| 7d | 16.852 | 16.313 | 16.232 | 16.148 | 16.391 | 16.335 | 16.138 | 16.109 | 16.101 | 16.132 |
| 30d | 14.295 | 13.835 | 13.796 | 13.737 | 13.958 | 13.894 | 13.710 | 13.685 | 13.686 | 13.712 |

## Next candle

- candle starting 2026-10-18 23:27 UTC, last close 2402.29
- P(up) 0.4977, return quantiles (bp): {'05': -16.766, '10': -12.761, '25': -6.341, '40': -2.303, '50': -0.058, '60': 2.345, '75': 5.846, '90': 11.209, '95': 16.064}
- changepoint probability 0.1385, regime age 65.6 min
- agent weights: empirical 0.003, ewma 0.052, garch 0.130, har 0.204, bocpd 0.022, hmm 0.071, online_qr 0.228, lgbm 0.290

## Learning log

- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- HMM volatility states (sd, bp per minute): [3.34, 6.61, 20.42], current probabilities: [0.007, 0.85, 0.143]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 23:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.383, 'l_abs': 0.715, 'l_hi': 0.753, 'l_lo': 0.743, 'b05': 0.69, 'b25': 0.714, 'b75': 0.682, 'b95': 0.676}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.6], [1.4, 1.8], [1.3, 1.6], [1.3, 1.8]], 'cone_width': [1.411, 1.839, 2.215, 2.688, 3.133, 3.193, 3.56, 3.938, 4.077, 4.371, 4.667, 4.867, 5.061, 5.463]}
- calibration offsets (in sigma): {'05': 0.013, '10': 0.056, '25': 0.045, '40': 0.034, '50': 0.04, '60': 0.066, '75': 0.035, '90': -0.036, '95': -0.043}
