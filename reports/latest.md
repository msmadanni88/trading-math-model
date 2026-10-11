# ETH-USD 60s candle generator - report

- generated: 2026-10-11 22:31 UTC
- last closed candle: 2026-10-11 22:31 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.508 (671) [0.454, 0.562] | 0.508 (2875) [0.488, 0.529] | 0.511 (3739) [0.494, 0.528] | 0.511 (767) [0.465, 0.557] | 0.444 (90) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.537 (778) | 0.545 (5363) [0.536, 0.553] | 0.510 (23183) [0.502, 0.518] | 0.506 (30322) [0.500, 0.512] | 0.545 (6084) [0.538, 0.552] | 0.533 (677) | 0.500 | up +0.044 (noise 0.010) |
| colour_confident | 0.567 (275) | 0.607 (1140) [0.574, 0.646] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.603 (189) | 0.500 | flat -0.000 (noise 0.055) |
| colour_next | 0.529 (1387) | 0.530 (9958) [0.521, 0.539] | 0.508 (42835) [0.502, 0.513] | 0.506 (55711) [0.501, 0.511] | 0.529 (11362) [0.521, 0.537] | 0.528 (1332) | 0.500 | up +0.023 (noise 0.007) |
| colour_path | 0.500 (19418) | 0.500 (139412) [0.497, 0.503] | 0.501 (599690) [0.500, 0.502] | 0.500 (779954) [0.499, 0.502] | 0.499 (159068) [0.496, 0.502] | 0.499 (18648) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.648 (88) | 0.656 (305) [0.602, 0.720] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.672 (64) | 0.500 | - |
| reversal_k13_next | 0.361 (72) | 0.329 (511) [0.312, 0.345] | 0.312 (2046) [0.297, 0.328] | 0.306 (2718) [0.293, 0.320] | 0.328 (613) [0.314, 0.341] | 0.385 (65) | 0.077 | flat +0.053 (noise 0.027) |
| reversal_k13_now | 0.576 (59) | 0.575 (400) [0.548, 0.604] | 0.587 (1490) [0.565, 0.612] | 0.584 (1917) [0.566, 0.602] | 0.593 (445) [0.559, 0.637] | 0.571 (49) | 0.077 | flat -0.019 (noise 0.039) |
| reversal_k3_next | 0.620 (129) | 0.591 (557) [0.559, 0.621] | 0.586 (2386) [0.571, 0.602] | 0.586 (3141) [0.573, 0.598] | 0.579 (701) [0.550, 0.610] | 0.595 (84) | 0.293 | flat +0.013 (noise 0.028) |
| reversal_k3_now | 0.910 (67) | 0.923 (418) [0.914, 0.936] | 0.940 (1718) [0.931, 0.947] | 0.938 (2238) [0.931, 0.945] | 0.924 (475) [0.916, 0.935] | 0.910 (67) | 0.293 | flat -0.022 (noise 0.017) |
| reversal_k5_next | 0.507 (73) | 0.471 (480) [0.441, 0.496] | 0.485 (2092) [0.467, 0.503] | 0.484 (2659) [0.467, 0.501] | 0.453 (669) [0.425, 0.487] | 0.483 (60) | 0.187 | flat +0.019 (noise 0.030) |
| reversal_k5_now | 0.873 (63) | 0.827 (387) [0.791, 0.861] | 0.838 (1590) [0.823, 0.853] | 0.835 (2059) [0.821, 0.849] | 0.826 (448) [0.795, 0.855] | 0.833 (48) | 0.187 | flat -0.031 (noise 0.026) |
| reversal_k8_next | 0.449 (69) | 0.396 (613) [0.367, 0.429] | 0.407 (2098) [0.389, 0.427] | 0.396 (2796) [0.382, 0.411] | 0.394 (690) [0.369, 0.422] | 0.361 (83) | 0.122 | flat +0.016 (noise 0.031) |
| reversal_k8_now | 0.770 (61) | 0.699 (418) [0.654, 0.741] | 0.722 (1585) [0.703, 0.742] | 0.712 (2055) [0.694, 0.731] | 0.707 (468) [0.665, 0.745] | 0.672 (58) | 0.122 | flat -0.037 (noise 0.034) |
| overall | 0.506 (21494) | 0.504 (153825) [0.500, 0.508] | 0.504 (660405) [0.502, 0.505] | 0.503 (858987) [0.501, 0.504] | 0.503 (175706) [0.499, 0.507] | 0.503 (20584) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08086, 0.1222] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5293, 'levels': [{'threshold': 0.08086, 'calls_per_day': 143.0, 'win_rate': 0.6012}, {'threshold': 0.1222, 'calls_per_day': 35.7, 'win_rate': 0.6719}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 11560, 'rate': 0.5306}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15331 | 0.331 | 0.519 (15057) | 0.597 (1133) | 0.779 (2507) |
| volatility: normal | 15330 | 0.358 | 0.508 (15256) | 0.636 (206) | 0.776 (2206) |
| volatility: wild | 15330 | 0.373 | 0.496 (15285) | 0.676 (74) | 0.774 (2119) |
| session: Asia 00-08 | 15360 | 0.351 | 0.511 (15243) | 0.600 (502) | 0.777 (2221) |
| session: Europe 08-13 | 9600 | 0.348 | 0.507 (9506) | 0.594 (345) | 0.769 (1532) |
| session: US 13-21 | 15360 | 0.364 | 0.504 (15249) | 0.590 (366) | 0.785 (2252) |
| session: late 21-24 | 5671 | 0.348 | 0.513 (5600) | 0.675 (200) | 0.765 (827) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.384 | 0.387 | 0.260 | 0.260 | 0.533 | 0.277 | 0.491 | 1.625 |
| 6h | 360 | 0.361 | 0.356 | 0.275 | 0.290 | 0.518 | 0.253 | 0.469 | 1.432 |
| 24h | 1440 | 0.330 | 0.325 | 0.248 | 0.267 | 0.530 | 0.245 | 0.415 | 1.222 |
| 7d | 10080 | 0.354 | 0.348 | 0.273 | 0.300 | 0.527 | 0.258 | 0.450 | 1.201 |
| 30d | 43200 | 0.354 | 0.352 | 0.276 | 0.305 | 0.509 | 0.248 | 0.460 | 1.309 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.384 / 0.533 / 0.933; 2: 0.357 / 0.483 / 1.000; 3: 0.365 / 0.567 / 0.983; 4: 0.338 / 0.400 / 0.983; 5: 0.352 / 0.450 / 1.000; 6: 0.338 / 0.433 / 1.000; 7: 0.341 / 0.483 / 1.000; 8: 0.348 / 0.500 / 1.000; 9: 0.339 / 0.417 / 1.000; 10: 0.356 / 0.500 / 1.000; 11: 0.360 / 0.550 / 1.000; 12: 0.343 / 0.500 / 1.000; 13: 0.341 / 0.467 / 1.000; 14: 0.337 / 0.467 / 1.000; 15: 0.343 / 0.483 / 1.000
- 6h: 1: 0.361 / 0.518 / 0.908; 2: 0.346 / 0.507 / 0.919; 3: 0.348 / 0.518 / 0.894; 4: 0.335 / 0.468 / 0.914; 5: 0.346 / 0.490 / 0.903; 6: 0.344 / 0.499 / 0.911; 7: 0.333 / 0.485 / 0.900; 8: 0.346 / 0.532 / 0.886; 9: 0.329 / 0.465 / 0.897; 10: 0.341 / 0.510 / 0.894; 11: 0.336 / 0.510 / 0.906; 12: 0.339 / 0.513 / 0.869; 13: 0.330 / 0.460 / 0.875; 14: 0.331 / 0.504 / 0.906; 15: 0.340 / 0.521 / 0.939
- 24h: 1: 0.330 / 0.530 / 0.897; 2: 0.323 / 0.514 / 0.904; 3: 0.317 / 0.505 / 0.899; 4: 0.315 / 0.489 / 0.901; 5: 0.315 / 0.500 / 0.896; 6: 0.317 / 0.501 / 0.898; 7: 0.315 / 0.495 / 0.903; 8: 0.322 / 0.523 / 0.892; 9: 0.313 / 0.480 / 0.896; 10: 0.317 / 0.498 / 0.899; 11: 0.317 / 0.502 / 0.902; 12: 0.314 / 0.495 / 0.899; 13: 0.318 / 0.497 / 0.896; 14: 0.312 / 0.488 / 0.895; 15: 0.315 / 0.510 / 0.897
- 7d: 1: 0.354 / 0.527 / 0.900; 2: 0.344 / 0.500 / 0.902; 3: 0.345 / 0.508 / 0.902; 4: 0.343 / 0.502 / 0.902; 5: 0.343 / 0.505 / 0.901; 6: 0.340 / 0.496 / 0.901; 7: 0.340 / 0.500 / 0.901; 8: 0.340 / 0.497 / 0.901; 9: 0.336 / 0.488 / 0.901; 10: 0.340 / 0.502 / 0.901; 11: 0.338 / 0.494 / 0.901; 12: 0.338 / 0.494 / 0.899; 13: 0.341 / 0.506 / 0.899; 14: 0.338 / 0.501 / 0.899; 15: 0.339 / 0.498 / 0.900
- 30d: 1: 0.354 / 0.509 / 0.898; 2: 0.348 / 0.497 / 0.900; 3: 0.350 / 0.509 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.347 / 0.505 / 0.900; 6: 0.346 / 0.502 / 0.900; 7: 0.346 / 0.504 / 0.900; 8: 0.345 / 0.503 / 0.900; 9: 0.342 / 0.495 / 0.900; 10: 0.344 / 0.504 / 0.900; 11: 0.343 / 0.501 / 0.900; 12: 0.344 / 0.503 / 0.900; 13: 0.343 / 0.501 / 0.900; 14: 0.342 / 0.497 / 0.900; 15: 0.342 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.062 (body 0.044, range 0.079); 'price stays where it was' would score 0.136; colour right 0.467; typical miss of the close 11.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.105 (body 0.066, range 0.144); 'price stays where it was' would score 0.131; colour right 0.493; typical miss of the close 8.3 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.111 (body 0.076, range 0.147); 'price stays where it was' would score 0.126; colour right 0.512; typical miss of the close 4.8 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.118 (body 0.081, range 0.155); 'price stays where it was' would score 0.126; colour right 0.500; typical miss of the close 6.5 bp; chain ended on the right side 0.481 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.6 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 3.8; 2: 0.199 / 4.2; 3: 0.165 / 5.7; 4: 0.133 / 6.3; 5: 0.119 / 7.0; 6: 0.109 / 7.5; 7: 0.101 / 7.9; 8: 0.093 / 8.2; 9: 0.087 / 8.5; 10: 0.081 / 9.2; 11: 0.076 / 9.7; 12: 0.075 / 10.3; 13: 0.063 / 10.5; 14: 0.065 / 10.6; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 100465, probability skill vs chance 0.2306, widened contest next: False
  - now: threshold 0.8375, hit rate recent 0.919 / long run 0.929
    - 6h: 8 calls (32 a day), hit rate 1.000, chance 0.287, naive rule 0.579, lift 3.48x
    - 24h: 70 calls (70 a day), hit rate 0.900, chance 0.322, naive rule 0.558, lift 2.80x
    - 7d: 423 calls (60 a day), hit rate 0.922, chance 0.302, naive rule 0.506, lift 3.06x
    - 30d: 1737 calls (58 a day), hit rate 0.938, chance 0.293, naive rule 0.486, lift 3.20x
  - next: threshold 0.5687, hit rate recent 0.6391 / long run 0.5869
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.287, lift 2.71x
    - 24h: 91 calls (91 a day), hit rate 0.593, chance 0.322, lift 1.85x
    - 7d: 520 calls (74 a day), hit rate 0.590, chance 0.302, lift 1.96x
    - 30d: 2389 calls (80 a day), hit rate 0.589, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.496; 0.35: 538, 0.519; 0.40: 485, 0.565; 0.45: 417, 0.632; 0.50: 364, 0.686; 0.55: 320, 0.727; 0.60: 272, 0.770; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 139, 0.874; 0.80: 97, 0.913; 0.85: 49, 0.948; 0.90: 3, 0.975
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.426; 0.35: 498, 0.460; 0.40: 412, 0.490; 0.45: 317, 0.523; 0.50: 206, 0.557; 0.55: 92, 0.583; 0.60: 14, 0.607; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 100463, probability skill vs chance 0.2214, widened contest next: False
  - now: threshold 0.713, hit rate recent 0.8537 / long run 0.8326
    - 6h: 7 calls (29 a day), hit rate 1.000, chance 0.197, naive rule 0.519, lift 5.08x
    - 24h: 53 calls (53 a day), hit rate 0.849, chance 0.201, naive rule 0.443, lift 4.23x
    - 7d: 369 calls (53 a day), hit rate 0.816, chance 0.194, naive rule 0.411, lift 4.20x
    - 30d: 1602 calls (53 a day), hit rate 0.837, chance 0.188, naive rule 0.394, lift 4.45x
  - next: threshold 0.4503, hit rate recent 0.5035 / long run 0.4727
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.197, lift 2.77x
    - 24h: 60 calls (60 a day), hit rate 0.483, chance 0.201, lift 2.41x
    - 7d: 423 calls (60 a day), hit rate 0.468, chance 0.194, lift 2.41x
    - 30d: 2079 calls (69 a day), hit rate 0.486, chance 0.188, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 427, 0.418; 0.35: 362, 0.475; 0.40: 292, 0.545; 0.45: 238, 0.604; 0.50: 185, 0.660; 0.55: 140, 0.707; 0.60: 109, 0.750; 0.65: 84, 0.796; 0.70: 63, 0.826; 0.75: 34, 0.866; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 252, 0.425; 0.40: 164, 0.454; 0.45: 83, 0.476; 0.50: 20, 0.516; 0.55: 2, 0.550
- **K=8**: model 1791417600, labels learned 100460, probability skill vs chance 0.2091, widened contest next: False
  - now: threshold 0.5601, hit rate recent 0.7073 / long run 0.7079
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.126, naive rule 0.429, lift 5.30x
    - 24h: 63 calls (63 a day), hit rate 0.698, chance 0.124, naive rule 0.348, lift 5.64x
    - 7d: 420 calls (60 a day), hit rate 0.683, chance 0.123, naive rule 0.342, lift 5.54x
    - 30d: 1602 calls (53 a day), hit rate 0.721, chance 0.122, naive rule 0.330, lift 5.89x
  - next: threshold 0.3608, hit rate recent 0.4087 / long run 0.3942
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.126, lift 3.58x
    - 24h: 85 calls (86 a day), hit rate 0.365, chance 0.124, lift 2.95x
    - 7d: 611 calls (87 a day), hit rate 0.381, chance 0.123, lift 3.09x
    - 30d: 2115 calls (71 a day), hit rate 0.407, chance 0.122, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 266, 0.410; 0.35: 201, 0.485; 0.40: 155, 0.545; 0.45: 122, 0.591; 0.50: 93, 0.636; 0.55: 67, 0.690; 0.60: 46, 0.730; 0.65: 25, 0.773; 0.70: 9, 0.822; 0.75: 1, 0.857
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 183, 0.351; 0.35: 112, 0.390; 0.40: 47, 0.416; 0.45: 10, 0.446; 0.50: 1, 0.390
- **K=13**: model 1791504000, labels learned 100455, probability skill vs chance 0.1837, widened contest next: False
  - now: threshold 0.4361, hit rate recent 0.5888 / long run 0.586
    - 6h: 8 calls (33 a day), hit rate 0.500, chance 0.090, naive rule 0.407, lift 5.56x
    - 24h: 53 calls (54 a day), hit rate 0.585, chance 0.079, naive rule 0.295, lift 7.38x
    - 7d: 387 calls (55 a day), hit rate 0.568, chance 0.079, naive rule 0.284, lift 7.19x
    - 30d: 1499 calls (50 a day), hit rate 0.585, chance 0.078, naive rule 0.272, lift 7.52x
  - next: threshold 0.2865, hit rate recent 0.381 / long run 0.3237
    - 6h: 9 calls (38 a day), hit rate 0.444, chance 0.090, lift 4.95x
    - 24h: 67 calls (68 a day), hit rate 0.388, chance 0.079, lift 4.89x
    - 7d: 493 calls (71 a day), hit rate 0.329, chance 0.079, lift 4.16x
    - 30d: 2059 calls (69 a day), hit rate 0.314, chance 0.078, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.449; 0.35: 86, 0.510; 0.40: 62, 0.557; 0.45: 43, 0.612; 0.50: 27, 0.635; 0.55: 14, 0.688; 0.60: 5, 0.726; 0.65: 1, 0.769
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.328; 0.35: 14, 0.349; 0.40: 3, 0.325; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.925 | 4.54% | 0.933 | 0.533 | 0.249 | 0.567 | 0.416 |
| 6h | 12.714 | 5.64% | 0.900 | 0.514 | 0.251 | 0.476 | 0.503 |
| 24h | 8.630 | 4.67% | 0.901 | 0.510 | 0.251 | 0.500 | 0.592 |
| 7d | 11.407 | 5.08% | 0.902 | 0.500 | 0.251 | 0.494 | 0.658 |
| 30d | 13.572 | 4.29% | 0.900 | 0.500 | 0.251 | 0.497 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.492 | 12.430 | 12.169 | 12.135 | 12.350 | 12.125 | 11.773 | 11.881 | 11.897 | 11.925 |
| 6h | 13.474 | 12.954 | 12.803 | 12.701 | 13.114 | 12.828 | 12.686 | 12.688 | 12.674 | 12.714 |
| 24h | 9.053 | 8.738 | 8.685 | 8.652 | 8.908 | 8.767 | 8.631 | 8.598 | 8.613 | 8.630 |
| 7d | 12.018 | 11.519 | 11.481 | 11.459 | 11.613 | 11.598 | 11.404 | 11.384 | 11.387 | 11.407 |
| 30d | 14.180 | 13.693 | 13.656 | 13.600 | 13.830 | 13.780 | 13.569 | 13.545 | 13.546 | 13.572 |

## Next candle

- candle starting 2026-10-11 22:31 UTC, last close 2530.58
- P(up) 0.5289, return quantiles (bp): {'05': -6.459, '10': -4.248, '25': -1.815, '40': -0.366, '50': 0.14, '60': 0.853, '75': 1.932, '90': 4.232, '95': 6.264}
- changepoint probability 0.0875, regime age 22.2 min
- agent weights: empirical 0.003, ewma 0.021, garch 0.063, har 0.175, bocpd 0.003, hmm 0.032, online_qr 0.271, lgbm 0.432

## Learning log

- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- HMM volatility states (sd, bp per minute): [2.07, 4.68, 13.59], current probabilities: [0.838, 0.16, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-11 22:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.283, 'l_abs': 0.655, 'l_hi': 0.712, 'l_lo': 0.661, 'b05': 0.656, 'b25': 0.608, 'b75': 0.631, 'b95': 0.622}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.292, 1.861, 1.949, 2.461, 2.596, 2.866, 3.462, 3.329, 3.659, 3.622, 4.916, 5.025, 4.921, 4.618]}
- calibration offsets (in sigma): {'05': -0.055, '10': 0.02, '25': 0.035, '40': 0.03, '50': 0.02, '60': 0.02, '75': -0.025, '90': -0.03, '95': -0.015}
