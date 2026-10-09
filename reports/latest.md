# ETH-USD 60s candle generator - report

- generated: 2026-10-09 18:47 UTC
- last closed candle: 2026-10-09 18:47 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.458 (96) | 0.506 (670) [0.454, 0.558] | 0.505 (2875) [0.485, 0.526] | 0.509 (3547) [0.492, 0.526] | 0.499 (575) [0.443, 0.557] | 0.507 (75) | 0.500 | flat -0.002 (noise 0.040) |
| colour_clear | 0.555 (827) | 0.540 (5230) [0.526, 0.552] | 0.507 (23188) [0.500, 0.514] | 0.504 (28748) [0.498, 0.510] | 0.547 (4510) [0.536, 0.556] | 0.545 (635) | 0.500 | up +0.048 (noise 0.010) |
| colour_confident | 0.596 (89) | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.607 (815) [0.566, 0.644] | 0.667 (108) | 0.500 | - |
| colour_next | 0.528 (1434) | 0.527 (9974) [0.517, 0.538] | 0.507 (42883) [0.501, 0.512] | 0.505 (52891) [0.501, 0.510] | 0.531 (8542) [0.521, 0.541] | 0.516 (1125) | 0.500 | up +0.025 (noise 0.007) |
| colour_path | 0.497 (20076) | 0.498 (139636) [0.495, 0.502] | 0.501 (600362) [0.499, 0.502] | 0.500 (740474) [0.499, 0.502] | 0.499 (119588) [0.494, 0.503] | 0.500 (15750) | 0.500 | flat -0.005 (noise 0.003) |
| colour_strong | 0.500 (20) | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.635 (219) [0.577, 0.688] | 0.833 (18) | 0.500 | - |
| reversal_k13_next | 0.318 (66) | 0.312 (525) [0.291, 0.331] | 0.308 (2040) [0.294, 0.324] | 0.304 (2572) [0.290, 0.318] | 0.321 (467) [0.306, 0.336] | 0.333 (57) | 0.077 | flat +0.030 (noise 0.027) |
| reversal_k13_now | 0.612 (49) | 0.591 (391) [0.553, 0.636] | 0.585 (1481) [0.563, 0.609] | 0.582 (1811) [0.564, 0.602] | 0.587 (339) [0.544, 0.641] | 0.676 (37) | 0.077 | flat +0.007 (noise 0.038) |
| reversal_k3_next | 0.521 (71) | 0.572 (547) [0.542, 0.609] | 0.588 (2352) [0.572, 0.603] | 0.585 (2927) [0.572, 0.599] | 0.571 (487) [0.538, 0.613] | 0.559 (68) | 0.292 | flat -0.006 (noise 0.029) |
| reversal_k3_now | 0.917 (72) | 0.927 (399) [0.918, 0.939] | 0.940 (1692) [0.932, 0.948] | 0.939 (2108) [0.932, 0.947] | 0.927 (345) [0.917, 0.941] | 0.957 (47) | 0.292 | flat -0.028 (noise 0.017) |
| reversal_k5_next | 0.422 (71) | 0.449 (642) [0.420, 0.481] | 0.488 (2100) [0.468, 0.506] | 0.483 (2512) [0.466, 0.501] | 0.441 (522) [0.412, 0.480] | 0.475 (61) | 0.187 | flat -0.034 (noise 0.032) |
| reversal_k5_now | 0.758 (62) | 0.826 (397) [0.795, 0.858] | 0.833 (1573) [0.817, 0.849] | 0.835 (1949) [0.821, 0.850] | 0.823 (338) [0.788, 0.858] | 0.811 (37) | 0.187 | flat -0.042 (noise 0.026) |
| reversal_k8_next | 0.367 (120) | 0.387 (587) [0.359, 0.418] | 0.402 (2096) [0.385, 0.421] | 0.394 (2646) [0.379, 0.411] | 0.385 (540) [0.355, 0.418] | 0.420 (69) | 0.121 | flat -0.005 (noise 0.032) |
| reversal_k8_now | 0.625 (64) | 0.715 (411) [0.677, 0.756] | 0.723 (1582) [0.703, 0.742] | 0.713 (1947) [0.695, 0.732] | 0.711 (360) [0.670, 0.756] | 0.618 (34) | 0.121 | flat -0.038 (noise 0.036) |
| overall | 0.500 (22181) | 0.502 (154179) [0.498, 0.507] | 0.503 (661036) [0.502, 0.505] | 0.503 (815384) [0.501, 0.504] | 0.502 (132103) [0.497, 0.508] | 0.503 (17360) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07771, 0.1166] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5323, 'levels': [{'threshold': 0.07771, 'calls_per_day': 145.3, 'win_rate': 0.6148}, {'threshold': 0.1166, 'calls_per_day': 36.3, 'win_rate': 0.6537}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 8535, 'rate': 0.5317}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15256 | 0.335 | 0.515 (15045) | 0.610 (697) | 0.776 (2448) |
| volatility: normal | 15255 | 0.361 | 0.511 (15187) | 0.613 (160) | 0.770 (2151) |
| volatility: wild | 15256 | 0.374 | 0.496 (15210) | 0.667 (66) | 0.778 (2120) |
| session: Asia 00-08 | 15360 | 0.353 | 0.508 (15258) | 0.593 (327) | 0.778 (2199) |
| session: Europe 08-13 | 9600 | 0.351 | 0.506 (9540) | 0.598 (194) | 0.764 (1507) |
| session: US 13-21 | 15227 | 0.367 | 0.506 (15127) | 0.625 (243) | 0.783 (2222) |
| session: late 21-24 | 5580 | 0.350 | 0.511 (5517) | 0.660 (159) | 0.764 (791) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.350 | 0.361 | 0.277 | 0.277 | 0.542 | 0.222 | 0.478 | 1.389 |
| 6h | 360 | 0.374 | 0.376 | 0.293 | 0.332 | 0.526 | 0.250 | 0.498 | 1.288 |
| 24h | 1440 | 0.364 | 0.363 | 0.279 | 0.312 | 0.521 | 0.259 | 0.469 | 1.100 |
| 7d | 10080 | 0.351 | 0.345 | 0.272 | 0.297 | 0.528 | 0.253 | 0.448 | 1.241 |
| 30d | 43200 | 0.356 | 0.355 | 0.279 | 0.308 | 0.507 | 0.247 | 0.465 | 1.281 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.350 / 0.542 / 0.917; 2: 0.323 / 0.424 / 0.900; 3: 0.357 / 0.542 / 0.850; 4: 0.363 / 0.542 / 0.917; 5: 0.365 / 0.525 / 0.933; 6: 0.323 / 0.441 / 0.917; 7: 0.316 / 0.441 / 0.917; 8: 0.353 / 0.559 / 0.950; 9: 0.337 / 0.441 / 0.967; 10: 0.342 / 0.559 / 0.950; 11: 0.343 / 0.475 / 0.950; 12: 0.353 / 0.542 / 0.933; 13: 0.337 / 0.441 / 0.933; 14: 0.336 / 0.475 / 0.917; 15: 0.332 / 0.475 / 0.917
- 6h: 1: 0.374 / 0.526 / 0.911; 2: 0.365 / 0.515 / 0.869; 3: 0.374 / 0.526 / 0.786; 4: 0.366 / 0.513 / 0.889; 5: 0.366 / 0.499 / 0.881; 6: 0.359 / 0.515 / 0.911; 7: 0.344 / 0.454 / 0.897; 8: 0.355 / 0.496 / 0.911; 9: 0.344 / 0.437 / 0.911; 10: 0.363 / 0.507 / 0.919; 11: 0.360 / 0.515 / 0.922; 12: 0.353 / 0.490 / 0.931; 13: 0.352 / 0.476 / 0.925; 14: 0.351 / 0.490 / 0.908; 15: 0.356 / 0.504 / 0.919
- 24h: 1: 0.364 / 0.521 / 0.902; 2: 0.351 / 0.485 / 0.894; 3: 0.359 / 0.514 / 0.880; 4: 0.362 / 0.517 / 0.906; 5: 0.363 / 0.527 / 0.906; 6: 0.355 / 0.497 / 0.912; 7: 0.353 / 0.500 / 0.912; 8: 0.354 / 0.499 / 0.919; 9: 0.351 / 0.481 / 0.917; 10: 0.358 / 0.507 / 0.918; 11: 0.354 / 0.488 / 0.917; 12: 0.352 / 0.495 / 0.916; 13: 0.354 / 0.491 / 0.917; 14: 0.352 / 0.510 / 0.917; 15: 0.358 / 0.508 / 0.922
- 7d: 1: 0.351 / 0.528 / 0.897; 2: 0.341 / 0.502 / 0.899; 3: 0.343 / 0.509 / 0.897; 4: 0.341 / 0.506 / 0.901; 5: 0.338 / 0.498 / 0.901; 6: 0.336 / 0.493 / 0.902; 7: 0.337 / 0.501 / 0.901; 8: 0.335 / 0.490 / 0.902; 9: 0.333 / 0.488 / 0.902; 10: 0.336 / 0.502 / 0.902; 11: 0.336 / 0.499 / 0.902; 12: 0.336 / 0.501 / 0.901; 13: 0.337 / 0.504 / 0.901; 14: 0.335 / 0.498 / 0.901; 15: 0.335 / 0.493 / 0.901
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.899; 4: 0.350 / 0.500 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.496 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.163 (body 0.098, range 0.228); 'price stays where it was' would score 0.157; colour right 0.492; typical miss of the close 6.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.138 (body 0.096, range 0.181); 'price stays where it was' would score 0.138; colour right 0.479; typical miss of the close 8.8 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.131 (body 0.090, range 0.172); 'price stays where it was' would score 0.134; colour right 0.493; typical miss of the close 7.9 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.115 (body 0.078, range 0.152); 'price stays where it was' would score 0.120; colour right 0.499; typical miss of the close 6.1 bp; chain ended on the right side 0.499 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.1 bp; chain ended on the right side 0.504 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.1; 2: 0.200 / 4.4; 3: 0.167 / 6.1; 4: 0.132 / 6.7; 5: 0.119 / 7.5; 6: 0.110 / 8.1; 7: 0.100 / 8.6; 8: 0.091 / 8.9; 9: 0.085 / 9.2; 10: 0.079 / 9.9; 11: 0.075 / 10.6; 12: 0.074 / 10.9; 13: 0.062 / 11.3; 14: 0.064 / 11.3; 15: 0.061 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 97361, probability skill vs chance 0.2418, widened contest next: False
  - now: threshold 0.841, hit rate recent 0.9327 / long run 0.9367
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.324, naive rule 0.558, lift 2.87x
    - 24h: 65 calls (65 a day), hit rate 0.938, chance 0.299, naive rule 0.509, lift 3.14x
    - 7d: 403 calls (58 a day), hit rate 0.928, chance 0.293, naive rule 0.489, lift 3.16x
    - 30d: 1702 calls (57 a day), hit rate 0.941, chance 0.291, naive rule 0.481, lift 3.24x
  - next: threshold 0.5474, hit rate recent 0.5559 / long run 0.5755
    - 6h: 27 calls (110 a day), hit rate 0.630, chance 0.324, lift 1.94x
    - 24h: 88 calls (88 a day), hit rate 0.534, chance 0.299, lift 1.79x
    - 7d: 571 calls (82 a day), hit rate 0.564, chance 0.293, lift 1.92x
    - 30d: 2351 calls (78 a day), hit rate 0.584, chance 0.291, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.492; 0.35: 537, 0.516; 0.40: 486, 0.561; 0.45: 418, 0.629; 0.50: 366, 0.683; 0.55: 321, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 138, 0.873; 0.80: 96, 0.913; 0.85: 49, 0.949; 0.90: 2, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.458; 0.40: 412, 0.487; 0.45: 316, 0.518; 0.50: 206, 0.551; 0.55: 91, 0.583; 0.60: 13, 0.599; 0.65: 1, 0.682
- **K=5**: model 1790208000, labels learned 97359, probability skill vs chance 0.2174, widened contest next: False
  - now: threshold 0.7131, hit rate recent 0.7998 / long run 0.8297
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.222, naive rule 0.466, lift 4.12x
    - 24h: 51 calls (51 a day), hit rate 0.804, chance 0.198, naive rule 0.431, lift 4.06x
    - 7d: 385 calls (55 a day), hit rate 0.818, chance 0.190, naive rule 0.394, lift 4.30x
    - 30d: 1576 calls (53 a day), hit rate 0.835, chance 0.187, naive rule 0.390, lift 4.47x
  - next: threshold 0.4475, hit rate recent 0.4707 / long run 0.4651
    - 6h: 22 calls (90 a day), hit rate 0.636, chance 0.222, lift 2.86x
    - 24h: 80 calls (80 a day), hit rate 0.475, chance 0.198, lift 2.40x
    - 7d: 617 calls (88 a day), hit rate 0.441, chance 0.190, lift 2.32x
    - 30d: 2115 calls (71 a day), hit rate 0.488, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 429, 0.413; 0.35: 366, 0.469; 0.40: 295, 0.539; 0.45: 241, 0.599; 0.50: 186, 0.658; 0.55: 141, 0.704; 0.60: 110, 0.746; 0.65: 84, 0.792; 0.70: 62, 0.824; 0.75: 34, 0.866; 0.80: 9, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 252, 0.425; 0.40: 165, 0.450; 0.45: 84, 0.474; 0.50: 20, 0.512; 0.55: 2, 0.547
- **K=8**: model 1791417600, labels learned 97356, probability skill vs chance 0.2086, widened contest next: True
  - now: threshold 0.5787, hit rate recent 0.6396 / long run 0.7083
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.130, naive rule 0.395, lift 5.77x
    - 24h: 49 calls (49 a day), hit rate 0.653, chance 0.124, naive rule 0.366, lift 5.26x
    - 7d: 404 calls (58 a day), hit rate 0.700, chance 0.122, naive rule 0.328, lift 5.75x
    - 30d: 1581 calls (53 a day), hit rate 0.720, chance 0.121, naive rule 0.326, lift 5.94x
  - next: threshold 0.366, hit rate recent 0.4096 / long run 0.3937
    - 6h: 24 calls (99 a day), hit rate 0.542, chance 0.130, lift 4.17x
    - 24h: 94 calls (95 a day), hit rate 0.394, chance 0.124, lift 3.17x
    - 7d: 615 calls (88 a day), hit rate 0.387, chance 0.122, lift 3.18x
    - 30d: 2123 calls (71 a day), hit rate 0.403, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 270, 0.404; 0.35: 203, 0.480; 0.40: 156, 0.541; 0.45: 123, 0.587; 0.50: 94, 0.631; 0.55: 67, 0.686; 0.60: 46, 0.728; 0.65: 24, 0.772; 0.70: 9, 0.821; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 185, 0.349; 0.35: 114, 0.388; 0.40: 48, 0.412; 0.45: 10, 0.432; 0.50: 1, 0.429
- **K=13**: model 1791504000, labels learned 97351, probability skill vs chance 0.1886, widened contest next: False
  - now: threshold 0.4281, hit rate recent 0.6283 / long run 0.588
    - 6h: 10 calls (42 a day), hit rate 0.900, chance 0.084, naive rule 0.363, lift 10.71x
    - 24h: 48 calls (49 a day), hit rate 0.688, chance 0.076, naive rule 0.295, lift 8.99x
    - 7d: 386 calls (55 a day), hit rate 0.593, chance 0.078, naive rule 0.271, lift 7.64x
    - 30d: 1485 calls (50 a day), hit rate 0.587, chance 0.077, naive rule 0.268, lift 7.63x
  - next: threshold 0.2791, hit rate recent 0.3351 / long run 0.3098
    - 6h: 15 calls (63 a day), hit rate 0.467, chance 0.084, lift 5.55x
    - 24h: 65 calls (66 a day), hit rate 0.354, chance 0.076, lift 4.63x
    - 7d: 532 calls (76 a day), hit rate 0.318, chance 0.078, lift 4.09x
    - 30d: 2042 calls (68 a day), hit rate 0.310, chance 0.077, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.441; 0.35: 88, 0.502; 0.40: 62, 0.552; 0.45: 43, 0.609; 0.50: 27, 0.632; 0.55: 15, 0.684; 0.60: 6, 0.709; 0.65: 1, 0.769
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.321; 0.35: 15, 0.346; 0.40: 3, 0.341; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.396 | 3.35% | 0.900 | 0.567 | 0.251 | 0.508 | -0.031 |
| 6h | 15.414 | 3.16% | 0.911 | 0.547 | 0.250 | 0.515 | 0.578 |
| 24h | 13.314 | 3.62% | 0.906 | 0.509 | 0.251 | 0.511 | 0.496 |
| 7d | 10.976 | 5.37% | 0.900 | 0.501 | 0.251 | 0.497 | 0.676 |
| 30d | 14.256 | 4.40% | 0.900 | 0.500 | 0.251 | 0.498 | 0.693 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.721 | 9.466 | 9.455 | 9.520 | 9.630 | 9.533 | 9.421 | 9.323 | 9.391 | 9.396 |
| 6h | 15.917 | 15.570 | 15.475 | 15.494 | 15.750 | 15.759 | 15.431 | 15.350 | 15.395 | 15.414 |
| 24h | 13.814 | 13.429 | 13.393 | 13.409 | 13.547 | 13.451 | 13.306 | 13.240 | 13.290 | 13.314 |
| 7d | 11.599 | 11.087 | 11.062 | 11.028 | 11.183 | 11.224 | 10.976 | 10.961 | 10.959 | 10.976 |
| 30d | 14.913 | 14.389 | 14.338 | 14.288 | 14.527 | 14.483 | 14.260 | 14.230 | 14.230 | 14.256 |

## Next candle

- candle starting 2026-10-09 18:47 UTC, last close 2481.24
- P(up) 0.4718, return quantiles (bp): {'05': -8.551, '10': -6.257, '25': -3.105, '40': -1.378, '50': -0.272, '60': 0.71, '75': 2.818, '90': 6.299, '95': 7.857}
- changepoint probability 0.0785, regime age 114.0 min
- agent weights: empirical 0.005, ewma 0.069, garch 0.118, har 0.132, bocpd 0.021, hmm 0.035, online_qr 0.218, lgbm 0.402

## Learning log

- 2026-10-07 12:00 UTC: {"garch": {"alpha": 0.079, "beta": 0.9134}, "hmm": {"sd_bp": [1.68, 4.03, 11.85], "stay": [0.96, 0.943, 0.883]}}
- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- HMM volatility states (sd, bp per minute): [2.34, 4.79, 15.13], current probabilities: [0.002, 0.956, 0.041]
- live generator: {'versions': 60, 'latest_effective': '2026-10-09 18:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.48, 'l_abs': 0.755, 'l_hi': 0.735, 'l_lo': 0.693, 'b05': 0.7, 'b25': 0.669, 'b75': 0.659, 'b95': 0.682}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.56, 3.032, 1.887, 2.157, 2.018, 2.273, 2.159, 2.437, 2.424, 2.547, 2.613, 2.671, 2.949, 2.939]}
- calibration offsets (in sigma): {'05': 0.063, '10': 0.036, '25': 0.025, '40': -0.036, '50': -0.06, '60': -0.084, '75': -0.065, '90': 0.034, '95': -0.033}
