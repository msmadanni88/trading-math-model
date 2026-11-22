# ETH-USD 60s candle generator - report

- generated: 2026-11-22 05:59 UTC
- last closed candle: 2026-11-22 05:59 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.527 (672) [0.494, 0.558] | 0.520 (2879) [0.504, 0.536] | 0.516 (7769) [0.505, 0.527] | 0.519 (4797) [0.505, 0.533] | 0.522 (23) | 0.500 | flat -0.007 (noise 0.028) |
| colour_clear | 0.540 (705) | 0.549 (5561) [0.536, 0.562] | 0.541 (23851) [0.535, 0.547] | 0.526 (63754) [0.520, 0.531] | 0.544 (39516) [0.539, 0.548] | 0.544 (228) | 0.500 | flat +0.007 (noise 0.010) |
| colour_confident | 0.594 (224) | 0.563 (1286) [0.540, 0.586] | 0.577 (4508) [0.565, 0.588] | 0.586 (7230) [0.576, 0.596] | 0.586 (7230) [0.576, 0.596] | 0.513 (76) | 0.500 | flat +0.010 (noise 0.023) |
| colour_next | 0.519 (1437) | 0.531 (10048) [0.525, 0.537] | 0.530 (42898) [0.526, 0.534] | 0.519 (115789) [0.515, 0.522] | 0.530 (71440) [0.527, 0.533] | 0.521 (357) | 0.500 | flat -0.001 (noise 0.008) |
| colour_path | 0.503 (20118) | 0.504 (140672) [0.502, 0.506] | 0.502 (600572) [0.501, 0.504] | 0.501 (1621046) [0.500, 0.502] | 0.502 (1000160) [0.500, 0.502] | 0.497 (4998) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.586 (70) | 0.606 (355) [0.577, 0.642] | 0.611 (1213) [0.595, 0.627] | 0.624 (1897) [0.609, 0.639] | 0.624 (1897) [0.609, 0.639] | 0.550 (20) | 0.500 | flat -0.004 (noise 0.047) |
| reversal_k13_next | 0.469 (49) | 0.311 (495) [0.279, 0.355] | 0.332 (1868) [0.315, 0.351] | 0.316 (5354) [0.306, 0.325] | 0.326 (3249) [0.315, 0.337] | 0.417 (12) | 0.077 | flat -0.037 (noise 0.031) |
| reversal_k13_now | 0.638 (47) | 0.562 (370) [0.522, 0.607] | 0.573 (1634) [0.552, 0.594] | 0.574 (4176) [0.561, 0.586] | 0.570 (2704) [0.554, 0.587] | 0.571 (14) | 0.078 | flat -0.032 (noise 0.038) |
| reversal_k3_next | 0.634 (164) | 0.584 (663) [0.560, 0.609] | 0.600 (2447) [0.590, 0.612] | 0.589 (6892) [0.581, 0.597] | 0.590 (4452) [0.580, 0.601] | 0.649 (37) | 0.293 | flat -0.047 (noise 0.033) |
| reversal_k3_now | 0.936 (47) | 0.936 (373) [0.919, 0.954] | 0.931 (1721) [0.923, 0.941] | 0.935 (4632) [0.929, 0.941] | 0.931 (2869) [0.924, 0.938] | 1.000 (14) | 0.293 | flat +0.009 (noise 0.018) |
| reversal_k5_next | 0.719 (32) | 0.468 (376) [0.420, 0.531] | 0.510 (1986) [0.493, 0.528] | 0.486 (6035) [0.475, 0.497] | 0.482 (4045) [0.468, 0.497] | 0.667 (6) | 0.187 | flat -0.056 (noise 0.045) |
| reversal_k5_now | 0.760 (50) | 0.794 (422) [0.768, 0.817] | 0.794 (1760) [0.777, 0.809] | 0.816 (4418) [0.806, 0.826] | 0.804 (2807) [0.792, 0.815] | 0.929 (14) | 0.187 | up +0.059 (noise 0.029) |
| reversal_k8_next | 0.519 (77) | 0.397 (562) [0.369, 0.435] | 0.415 (2336) [0.400, 0.430] | 0.398 (6311) [0.388, 0.408] | 0.399 (4205) [0.387, 0.411] | 0.357 (14) | 0.121 | flat -0.036 (noise 0.033) |
| reversal_k8_now | 0.640 (50) | 0.655 (420) [0.627, 0.681] | 0.679 (1640) [0.659, 0.698] | 0.695 (4268) [0.683, 0.706] | 0.683 (2681) [0.668, 0.698] | 0.571 (14) | 0.122 | flat -0.021 (noise 0.034) |
| overall | 0.507 (22167) | 0.507 (155073) [0.505, 0.510] | 0.506 (661741) [0.505, 0.507] | 0.504 (1786690) [0.503, 0.505] | 0.505 (1103409) [0.504, 0.506] | 0.502 (5503) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0724, 0.103] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5316, 'levels': [{'threshold': 0.0724, 'calls_per_day': 150.0, 'win_rate': 0.5613}, {'threshold': 0.103, 'calls_per_day': 38.5, 'win_rate': 0.6111}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42898, 'rate': 0.5296}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15000 | 0.349 | 0.532 (14785) | 0.565 (2225) | 0.756 (2516) |
| volatility: normal | 14999 | 0.378 | 0.528 (14944) | 0.589 (1424) | 0.736 (2376) |
| volatility: wild | 15000 | 0.390 | 0.529 (14961) | 0.581 (1070) | 0.754 (2089) |
| session: Asia 00-08 | 15239 | 0.370 | 0.530 (15126) | 0.567 (1677) | 0.750 (2297) |
| session: Europe 08-13 | 9300 | 0.367 | 0.531 (9226) | 0.584 (1155) | 0.752 (1491) |
| session: US 13-21 | 14880 | 0.380 | 0.534 (14791) | 0.603 (1298) | 0.745 (2369) |
| session: late 21-24 | 5580 | 0.366 | 0.517 (5547) | 0.526 (589) | 0.751 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.392 | 0.337 | 0.282 | 0.282 | 0.567 | 0.305 | 0.479 | 1.459 |
| 6h | 360 | 0.383 | 0.367 | 0.265 | 0.285 | 0.520 | 0.273 | 0.493 | 1.245 |
| 24h | 1440 | 0.382 | 0.373 | 0.283 | 0.307 | 0.525 | 0.265 | 0.499 | 1.380 |
| 7d | 10080 | 0.386 | 0.377 | 0.303 | 0.337 | 0.531 | 0.269 | 0.504 | 1.199 |
| 30d | 43200 | 0.372 | 0.366 | 0.286 | 0.318 | 0.530 | 0.266 | 0.479 | 1.263 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.392 / 0.567 / 0.900; 2: 0.330 / 0.483 / 0.900; 3: 0.336 / 0.433 / 0.850; 4: 0.365 / 0.600 / 0.817; 5: 0.334 / 0.433 / 0.800; 6: 0.349 / 0.467 / 0.883; 7: 0.318 / 0.383 / 0.800; 8: 0.376 / 0.583 / 0.767; 9: 0.348 / 0.517 / 0.750; 10: 0.356 / 0.600 / 0.767; 11: 0.362 / 0.633 / 0.783; 12: 0.371 / 0.550 / 0.800; 13: 0.345 / 0.450 / 0.717; 14: 0.319 / 0.467 / 0.717; 15: 0.339 / 0.550 / 0.650
- 6h: 1: 0.383 / 0.520 / 0.886; 2: 0.350 / 0.450 / 0.914; 3: 0.363 / 0.469 / 0.908; 4: 0.365 / 0.494 / 0.889; 5: 0.367 / 0.489 / 0.867; 6: 0.364 / 0.506 / 0.886; 7: 0.363 / 0.483 / 0.853; 8: 0.375 / 0.531 / 0.822; 9: 0.364 / 0.500 / 0.814; 10: 0.363 / 0.517 / 0.822; 11: 0.364 / 0.517 / 0.853; 12: 0.372 / 0.520 / 0.856; 13: 0.352 / 0.489 / 0.803; 14: 0.352 / 0.506 / 0.775; 15: 0.356 / 0.492 / 0.744
- 24h: 1: 0.382 / 0.525 / 0.917; 2: 0.363 / 0.484 / 0.894; 3: 0.359 / 0.481 / 0.900; 4: 0.365 / 0.505 / 0.893; 5: 0.366 / 0.502 / 0.889; 6: 0.360 / 0.498 / 0.892; 7: 0.362 / 0.500 / 0.886; 8: 0.365 / 0.518 / 0.884; 9: 0.361 / 0.497 / 0.879; 10: 0.366 / 0.534 / 0.881; 11: 0.361 / 0.509 / 0.884; 12: 0.363 / 0.512 / 0.886; 13: 0.356 / 0.504 / 0.880; 14: 0.354 / 0.492 / 0.883; 15: 0.359 / 0.509 / 0.874
- 7d: 1: 0.386 / 0.531 / 0.901; 2: 0.374 / 0.495 / 0.900; 3: 0.375 / 0.506 / 0.900; 4: 0.373 / 0.499 / 0.899; 5: 0.375 / 0.507 / 0.898; 6: 0.374 / 0.507 / 0.899; 7: 0.372 / 0.503 / 0.899; 8: 0.374 / 0.512 / 0.898; 9: 0.369 / 0.497 / 0.898; 10: 0.373 / 0.511 / 0.898; 11: 0.371 / 0.506 / 0.899; 12: 0.372 / 0.505 / 0.899; 13: 0.370 / 0.504 / 0.898; 14: 0.369 / 0.501 / 0.897; 15: 0.369 / 0.500 / 0.896
- 30d: 1: 0.372 / 0.530 / 0.898; 2: 0.359 / 0.491 / 0.900; 3: 0.363 / 0.511 / 0.900; 4: 0.359 / 0.497 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.358 / 0.502 / 0.900; 7: 0.359 / 0.501 / 0.900; 8: 0.359 / 0.507 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.358 / 0.504 / 0.900; 11: 0.357 / 0.505 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.501 / 0.899; 14: 0.356 / 0.501 / 0.899; 15: 0.356 / 0.501 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.078 (body 0.046, range 0.109); 'price stays where it was' would score 0.039; colour right 0.367; typical miss of the close 26.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.131 (body 0.082, range 0.179); 'price stays where it was' would score 0.145; colour right 0.441; typical miss of the close 9.6 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.148 (body 0.101, range 0.195); 'price stays where it was' would score 0.154; colour right 0.510; typical miss of the close 11.1 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.132 (body 0.085, range 0.179); 'price stays where it was' would score 0.138; colour right 0.505; typical miss of the close 14.5 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.169); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.2 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.5; 2: 0.204 / 6.2; 3: 0.168 / 8.1; 4: 0.136 / 8.5; 5: 0.126 / 9.1; 6: 0.120 / 9.8; 7: 0.116 / 10.4; 8: 0.102 / 11.3; 9: 0.092 / 11.8; 10: 0.090 / 12.4; 11: 0.086 / 12.9; 12: 0.080 / 12.9; 13: 0.074 / 13.6; 14: 0.069 / 14.0; 15: 0.067 / 14.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 159953, probability skill vs chance 0.2335, widened contest next: False
  - now: threshold 0.8298, hit rate recent 0.9485 / long run 0.9318
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.303, naive rule 0.543, lift 3.30x
    - 24h: 48 calls (48 a day), hit rate 0.979, chance 0.303, naive rule 0.534, lift 3.23x
    - 7d: 379 calls (54 a day), hit rate 0.939, chance 0.292, naive rule 0.504, lift 3.21x
    - 30d: 1722 calls (57 a day), hit rate 0.931, chance 0.293, naive rule 0.501, lift 3.18x
  - next: threshold 0.5094, hit rate recent 0.6406 / long run 0.6029
    - 6h: 37 calls (150 a day), hit rate 0.649, chance 0.303, lift 2.14x
    - 24h: 164 calls (165 a day), hit rate 0.622, chance 0.303, lift 2.05x
    - 7d: 697 calls (100 a day), hit rate 0.587, chance 0.292, lift 2.01x
    - 30d: 2465 calls (82 a day), hit rate 0.602, chance 0.293, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 558, 0.502; 0.35: 529, 0.528; 0.40: 477, 0.576; 0.45: 413, 0.641; 0.50: 363, 0.686; 0.55: 315, 0.732; 0.60: 266, 0.778; 0.65: 224, 0.807; 0.70: 176, 0.838; 0.75: 141, 0.872; 0.80: 93, 0.903; 0.85: 44, 0.941; 0.90: 4, 0.965
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 580, 0.435; 0.35: 490, 0.469; 0.40: 388, 0.509; 0.45: 292, 0.543; 0.50: 187, 0.576; 0.55: 80, 0.588; 0.60: 10, 0.635; 0.65: 0, 0.533
- **K=5**: model 1794528000, labels learned 159951, probability skill vs chance 0.2257, widened contest next: False
  - now: threshold 0.6996, hit rate recent 0.815 / long run 0.7899
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.195, naive rule 0.457, lift 4.75x
    - 24h: 51 calls (51 a day), hit rate 0.804, chance 0.197, naive rule 0.457, lift 4.07x
    - 7d: 426 calls (61 a day), hit rate 0.800, chance 0.191, naive rule 0.422, lift 4.18x
    - 30d: 1760 calls (59 a day), hit rate 0.795, chance 0.187, naive rule 0.412, lift 4.25x
  - next: threshold 0.4616, hit rate recent 0.5954 / long run 0.5022
    - 6h: 6 calls (24 a day), hit rate 0.667, chance 0.195, lift 3.41x
    - 24h: 32 calls (32 a day), hit rate 0.688, chance 0.197, lift 3.48x
    - 7d: 370 calls (53 a day), hit rate 0.478, chance 0.191, lift 2.50x
    - 30d: 1955 calls (65 a day), hit rate 0.510, chance 0.187, lift 2.73x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.422; 0.35: 362, 0.474; 0.40: 293, 0.542; 0.45: 237, 0.602; 0.50: 186, 0.654; 0.55: 150, 0.686; 0.60: 114, 0.733; 0.65: 82, 0.770; 0.70: 51, 0.806; 0.75: 27, 0.841; 0.80: 7, 0.856
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 336, 0.392; 0.35: 250, 0.431; 0.40: 160, 0.462; 0.45: 64, 0.505; 0.50: 8, 0.553; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 159948, probability skill vs chance 0.2152, widened contest next: False
  - now: threshold 0.5799, hit rate recent 0.6475 / long run 0.6721
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.109, naive rule 0.308, lift 5.26x
    - 24h: 51 calls (51 a day), hit rate 0.627, chance 0.126, naive rule 0.388, lift 4.98x
    - 7d: 426 calls (61 a day), hit rate 0.655, chance 0.124, naive rule 0.352, lift 5.30x
    - 30d: 1643 calls (55 a day), hit rate 0.678, chance 0.123, naive rule 0.347, lift 5.53x
  - next: threshold 0.3547, hit rate recent 0.4659 / long run 0.4164
    - 6h: 14 calls (58 a day), hit rate 0.357, chance 0.109, lift 3.29x
    - 24h: 75 calls (76 a day), hit rate 0.453, chance 0.126, lift 3.60x
    - 7d: 563 calls (81 a day), hit rate 0.398, chance 0.124, lift 3.22x
    - 30d: 2313 calls (77 a day), hit rate 0.415, chance 0.123, lift 3.38x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.427; 0.35: 199, 0.487; 0.40: 157, 0.536; 0.45: 120, 0.577; 0.50: 86, 0.634; 0.55: 62, 0.670; 0.60: 41, 0.711; 0.65: 24, 0.766; 0.70: 9, 0.805; 0.75: 2, 0.727
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 161, 0.376; 0.35: 84, 0.405; 0.40: 26, 0.442; 0.45: 6, 0.473; 0.50: 1, 0.714
- **K=13**: model 1795132800, labels learned 159943, probability skill vs chance 0.1978, widened contest next: False
  - now: threshold 0.4528, hit rate recent 0.6099 / long run 0.5747
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.078, naive rule 0.283, lift 7.30x
    - 24h: 48 calls (49 a day), hit rate 0.625, chance 0.088, naive rule 0.358, lift 7.10x
    - 7d: 374 calls (54 a day), hit rate 0.564, chance 0.080, naive rule 0.297, lift 7.05x
    - 30d: 1637 calls (55 a day), hit rate 0.573, chance 0.079, naive rule 0.293, lift 7.25x
  - next: threshold 0.3076, hit rate recent 0.4181 / long run 0.3326
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.078, lift 5.32x
    - 24h: 51 calls (52 a day), hit rate 0.431, chance 0.088, lift 4.90x
    - 7d: 493 calls (71 a day), hit rate 0.318, chance 0.080, lift 3.98x
    - 30d: 1861 calls (62 a day), hit rate 0.332, chance 0.079, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 140, 0.423; 0.35: 102, 0.473; 0.40: 71, 0.532; 0.45: 49, 0.584; 0.50: 34, 0.622; 0.55: 21, 0.644; 0.60: 10, 0.674; 0.65: 2, 0.567; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.341; 0.35: 15, 0.373; 0.40: 3, 0.416

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.125 | -0.57% | 0.900 | 0.583 | 0.250 | 0.467 | 0.013 |
| 6h | 17.701 | 5.38% | 0.878 | 0.464 | 0.250 | 0.497 | 0.511 |
| 24h | 24.128 | 6.93% | 0.910 | 0.493 | 0.250 | 0.505 | 0.633 |
| 7d | 24.452 | 4.17% | 0.900 | 0.499 | 0.250 | 0.498 | 0.660 |
| 30d | 18.824 | 4.87% | 0.900 | 0.500 | 0.250 | 0.504 | 0.719 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.006 | 21.094 | 21.274 | 20.964 | 21.544 | 21.621 | 21.268 | 21.133 | 21.129 | 21.125 |
| 6h | 18.708 | 17.827 | 17.750 | 17.752 | 17.960 | 18.042 | 17.737 | 17.679 | 17.684 | 17.701 |
| 24h | 25.924 | 24.668 | 24.562 | 24.166 | 24.939 | 24.548 | 24.231 | 24.130 | 24.142 | 24.128 |
| 7d | 25.517 | 24.679 | 24.615 | 24.458 | 24.952 | 24.739 | 24.442 | 24.402 | 24.414 | 24.452 |
| 30d | 19.788 | 19.005 | 18.959 | 18.880 | 19.208 | 19.137 | 18.809 | 18.782 | 18.792 | 18.824 |

## Next candle

- candle starting 2026-11-22 05:59 UTC, last close 1653.2
- P(up) 0.4776, return quantiles (bp): {'05': -11.556, '10': -9.07, '25': -5.318, '40': -2.547, '50': -0.307, '60': 1.099, '75': 4.353, '90': 8.363, '95': 11.299}
- changepoint probability 0.0677, regime age 146.3 min
- agent weights: empirical 0.003, ewma 0.092, garch 0.108, har 0.218, bocpd 0.026, hmm 0.046, online_qr 0.205, lgbm 0.302

## Learning log

- 2026-11-20 00:00 UTC: {"garch": {"alpha": 0.0643, "beta": 0.9166}, "hmm": {"sd_bp": [5.69, 9.84, 21.45], "stay": [0.977, 0.948, 0.886]}, "lgbm": {"challenger_loss": 0.25634, "champion_loss": 0.25642, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47432, "challengers": 3, "chance_loss": 0.60517, "widened": true, "champion_loss": 0.47404, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38337, "challengers": 3, "chance_loss": 0.49066, "widened": true, "champion_loss": 0.38328, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27601, "challengers": 1, "chance_loss": 0.36654, "widened": false, "champion_loss": 0.27501, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20643, "challengers": 3, "chance_loss": 0.28016, "widened": true, "champion_loss": 0.20661, "promoted": true}}
- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- 2026-11-22 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9215}, "hmm": {"sd_bp": [5.69, 10.58, 28.33], "stay": [0.985, 0.953, 0.874]}, "lgbm": {"challenger_loss": 0.24557, "champion_loss": 0.24554, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48129, "challengers": 1, "chance_loss": 0.60807, "widened": false, "champion_loss": 0.47918, "promoted": false}, "reversal_k5": {"challenger_loss": 0.381, "challengers": 1, "chance_loss": 0.49754, "widened": false, "champion_loss": 0.37986, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28291, "challengers": 1, "chance_loss": 0.38778, "widened": false, "champion_loss": 0.28187, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20591, "challengers": 1, "chance_loss": 0.29298, "widened": false, "champion_loss": 0.20541, "promoted": false}}
- HMM volatility states (sd, bp per minute): [5.69, 10.58, 28.33], current probabilities: [0.661, 0.333, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-11-22 06:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.333, 'l_abs': 0.68, 'l_hi': 0.806, 'l_lo': 0.744, 'b05': 0.776, 'b25': 0.72, 'b75': 0.718, 'b95': 0.739}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.5], [1.3, 1.6], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [1.463, 1.657, 2.119, 2.677, 2.606, 3.244, 4.078, 4.335, 4.578, 4.353, 4.556, 6.04, 6.804, 8.794]}
- calibration offsets (in sigma): {'05': 0.069, '10': -0.012, '25': -0.065, '40': -0.088, '50': -0.02, '60': -0.062, '75': -0.025, '90': -0.088, '95': -0.109}
