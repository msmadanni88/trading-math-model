# ETH-USD 60s candle generator - report

- generated: 2026-10-11 18:45 UTC
- last closed candle: 2026-10-11 18:45 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.508 (671) [0.454, 0.562] | 0.508 (2875) [0.488, 0.529] | 0.511 (3739) [0.494, 0.528] | 0.511 (767) [0.465, 0.557] | 0.453 (75) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.537 (778) | 0.545 (5363) [0.536, 0.553] | 0.510 (23183) [0.502, 0.518] | 0.506 (30322) [0.500, 0.512] | 0.545 (6084) [0.538, 0.552] | 0.530 (573) | 0.500 | up +0.044 (noise 0.010) |
| colour_confident | 0.567 (275) | 0.607 (1140) [0.574, 0.646] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.606 (175) | 0.500 | flat -0.000 (noise 0.055) |
| colour_next | 0.529 (1387) | 0.530 (9958) [0.521, 0.539] | 0.508 (42835) [0.502, 0.513] | 0.506 (55711) [0.501, 0.511] | 0.529 (11362) [0.521, 0.537] | 0.530 (1107) | 0.500 | up +0.023 (noise 0.007) |
| colour_path | 0.500 (19418) | 0.500 (139412) [0.497, 0.503] | 0.501 (599690) [0.500, 0.502] | 0.500 (779954) [0.499, 0.502] | 0.499 (159068) [0.496, 0.502] | 0.498 (15498) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.648 (88) | 0.656 (305) [0.602, 0.720] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.667 (60) | 0.500 | - |
| reversal_k13_next | 0.361 (72) | 0.329 (511) [0.312, 0.345] | 0.312 (2046) [0.297, 0.328] | 0.306 (2718) [0.293, 0.320] | 0.328 (613) [0.314, 0.341] | 0.373 (59) | 0.077 | flat +0.053 (noise 0.027) |
| reversal_k13_now | 0.576 (59) | 0.575 (400) [0.548, 0.604] | 0.587 (1490) [0.565, 0.612] | 0.584 (1917) [0.566, 0.602] | 0.593 (445) [0.559, 0.637] | 0.571 (42) | 0.077 | flat -0.019 (noise 0.039) |
| reversal_k3_next | 0.620 (129) | 0.591 (557) [0.559, 0.621] | 0.586 (2386) [0.571, 0.602] | 0.586 (3141) [0.573, 0.598] | 0.579 (701) [0.550, 0.610] | 0.582 (79) | 0.293 | flat +0.013 (noise 0.028) |
| reversal_k3_now | 0.910 (67) | 0.923 (418) [0.914, 0.936] | 0.940 (1718) [0.931, 0.947] | 0.938 (2238) [0.931, 0.945] | 0.924 (475) [0.916, 0.935] | 0.905 (63) | 0.293 | flat -0.022 (noise 0.017) |
| reversal_k5_next | 0.507 (73) | 0.471 (480) [0.441, 0.496] | 0.485 (2092) [0.467, 0.503] | 0.484 (2659) [0.467, 0.501] | 0.453 (669) [0.425, 0.487] | 0.453 (53) | 0.187 | flat +0.019 (noise 0.030) |
| reversal_k5_now | 0.873 (63) | 0.827 (387) [0.791, 0.861] | 0.838 (1590) [0.823, 0.853] | 0.835 (2059) [0.821, 0.849] | 0.826 (448) [0.795, 0.855] | 0.814 (43) | 0.187 | flat -0.031 (noise 0.026) |
| reversal_k8_next | 0.449 (69) | 0.396 (613) [0.367, 0.429] | 0.407 (2098) [0.389, 0.427] | 0.396 (2796) [0.382, 0.411] | 0.394 (690) [0.369, 0.422] | 0.338 (71) | 0.122 | flat +0.016 (noise 0.031) |
| reversal_k8_now | 0.770 (61) | 0.699 (418) [0.654, 0.741] | 0.722 (1585) [0.703, 0.742] | 0.712 (2055) [0.694, 0.731] | 0.707 (468) [0.665, 0.745] | 0.688 (48) | 0.122 | flat -0.037 (noise 0.034) |
| overall | 0.506 (21494) | 0.504 (153825) [0.500, 0.508] | 0.504 (660405) [0.502, 0.505] | 0.503 (858987) [0.501, 0.504] | 0.503 (175706) [0.499, 0.507] | 0.502 (17138) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08086, 0.1222] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5293, 'levels': [{'threshold': 0.08086, 'calls_per_day': 143.0, 'win_rate': 0.6012}, {'threshold': 0.1222, 'calls_per_day': 35.7, 'win_rate': 0.6719}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 11335, 'rate': 0.5309}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15255 | 0.331 | 0.519 (14982) | 0.597 (1127) | 0.779 (2496) |
| volatility: normal | 15255 | 0.358 | 0.508 (15181) | 0.635 (200) | 0.776 (2206) |
| volatility: wild | 15255 | 0.374 | 0.497 (15210) | 0.681 (72) | 0.775 (2104) |
| session: Asia 00-08 | 15360 | 0.351 | 0.511 (15243) | 0.600 (502) | 0.777 (2221) |
| session: Europe 08-13 | 9600 | 0.348 | 0.507 (9506) | 0.594 (345) | 0.769 (1532) |
| session: US 13-21 | 15225 | 0.364 | 0.504 (15115) | 0.590 (356) | 0.785 (2242) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5509) | 0.679 (196) | 0.767 (811) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.338 | 0.315 | 0.264 | 0.264 | 0.433 | 0.210 | 0.467 | 1.638 |
| 6h | 360 | 0.336 | 0.337 | 0.267 | 0.280 | 0.494 | 0.229 | 0.443 | 1.392 |
| 24h | 1440 | 0.324 | 0.321 | 0.244 | 0.266 | 0.532 | 0.244 | 0.405 | 1.178 |
| 7d | 10080 | 0.353 | 0.347 | 0.272 | 0.300 | 0.528 | 0.258 | 0.449 | 1.197 |
| 30d | 43200 | 0.354 | 0.352 | 0.276 | 0.305 | 0.509 | 0.247 | 0.460 | 1.309 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.338 / 0.433 / 0.950; 2: 0.359 / 0.583 / 0.983; 3: 0.308 / 0.417 / 0.917; 4: 0.339 / 0.517 / 0.917; 5: 0.316 / 0.483 / 0.900; 6: 0.335 / 0.550 / 0.900; 7: 0.304 / 0.483 / 0.883; 8: 0.327 / 0.517 / 0.883; 9: 0.271 / 0.350 / 0.933; 10: 0.300 / 0.417 / 0.933; 11: 0.298 / 0.433 / 0.950; 12: 0.315 / 0.500 / 0.917; 13: 0.302 / 0.400 / 0.950; 14: 0.330 / 0.550 / 0.983; 15: 0.317 / 0.550 / 1.000
- 6h: 1: 0.336 / 0.494 / 0.919; 2: 0.346 / 0.522 / 0.897; 3: 0.327 / 0.483 / 0.853; 4: 0.345 / 0.525 / 0.869; 5: 0.317 / 0.466 / 0.833; 6: 0.331 / 0.500 / 0.839; 7: 0.320 / 0.494 / 0.856; 8: 0.335 / 0.522 / 0.833; 9: 0.321 / 0.455 / 0.864; 10: 0.315 / 0.452 / 0.858; 11: 0.322 / 0.489 / 0.881; 12: 0.318 / 0.466 / 0.828; 13: 0.331 / 0.469 / 0.856; 14: 0.327 / 0.503 / 0.872; 15: 0.327 / 0.506 / 0.906
- 24h: 1: 0.324 / 0.532 / 0.894; 2: 0.321 / 0.511 / 0.902; 3: 0.311 / 0.498 / 0.897; 4: 0.315 / 0.500 / 0.906; 5: 0.311 / 0.501 / 0.899; 6: 0.313 / 0.500 / 0.905; 7: 0.312 / 0.507 / 0.915; 8: 0.318 / 0.520 / 0.899; 9: 0.310 / 0.480 / 0.904; 10: 0.311 / 0.488 / 0.910; 11: 0.313 / 0.495 / 0.913; 12: 0.309 / 0.493 / 0.916; 13: 0.316 / 0.504 / 0.915; 14: 0.311 / 0.497 / 0.910; 15: 0.310 / 0.509 / 0.906
- 7d: 1: 0.353 / 0.528 / 0.899; 2: 0.344 / 0.501 / 0.900; 3: 0.344 / 0.507 / 0.899; 4: 0.343 / 0.503 / 0.900; 5: 0.341 / 0.504 / 0.899; 6: 0.339 / 0.496 / 0.899; 7: 0.339 / 0.502 / 0.899; 8: 0.339 / 0.498 / 0.898; 9: 0.336 / 0.488 / 0.899; 10: 0.339 / 0.501 / 0.899; 11: 0.337 / 0.492 / 0.900; 12: 0.337 / 0.495 / 0.899; 13: 0.340 / 0.507 / 0.899; 14: 0.338 / 0.503 / 0.899; 15: 0.338 / 0.498 / 0.899
- 30d: 1: 0.354 / 0.509 / 0.898; 2: 0.348 / 0.497 / 0.900; 3: 0.350 / 0.509 / 0.900; 4: 0.347 / 0.500 / 0.900; 5: 0.347 / 0.504 / 0.900; 6: 0.346 / 0.502 / 0.900; 7: 0.346 / 0.504 / 0.900; 8: 0.346 / 0.503 / 0.900; 9: 0.342 / 0.495 / 0.900; 10: 0.344 / 0.504 / 0.900; 11: 0.344 / 0.501 / 0.900; 12: 0.344 / 0.502 / 0.900; 13: 0.344 / 0.501 / 0.900; 14: 0.342 / 0.497 / 0.900; 15: 0.342 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.174 (body 0.095, range 0.252); 'price stays where it was' would score 0.176; colour right 0.367; typical miss of the close 5.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.119 (body 0.074, range 0.165); 'price stays where it was' would score 0.123; colour right 0.478; typical miss of the close 6.1 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.114 (body 0.078, range 0.149); 'price stays where it was' would score 0.127; colour right 0.514; typical miss of the close 4.5 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.117 (body 0.081, range 0.154); 'price stays where it was' would score 0.124; colour right 0.499; typical miss of the close 6.4 bp; chain ended on the right side 0.484 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.6 bp; chain ended on the right side 0.506 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 3.8; 2: 0.199 / 4.3; 3: 0.165 / 5.7; 4: 0.132 / 6.3; 5: 0.120 / 7.0; 6: 0.109 / 7.5; 7: 0.101 / 8.0; 8: 0.092 / 8.3; 9: 0.087 / 8.5; 10: 0.081 / 9.3; 11: 0.077 / 9.8; 12: 0.075 / 10.3; 13: 0.063 / 10.6; 14: 0.065 / 10.6; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 100239, probability skill vs chance 0.2248, widened contest next: False
  - now: threshold 0.8375, hit rate recent 0.9134 / long run 0.9285
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.306, naive rule 0.553, lift 3.27x
    - 24h: 77 calls (77 a day), hit rate 0.896, chance 0.327, naive rule 0.548, lift 2.74x
    - 7d: 436 calls (62 a day), hit rate 0.917, chance 0.302, naive rule 0.504, lift 3.04x
    - 30d: 1743 calls (58 a day), hit rate 0.938, chance 0.293, naive rule 0.485, lift 3.21x
  - next: threshold 0.5687, hit rate recent 0.6244 / long run 0.5852
    - 6h: 20 calls (81 a day), hit rate 0.700, chance 0.306, lift 2.29x
    - 24h: 113 calls (113 a day), hit rate 0.611, chance 0.327, lift 1.87x
    - 7d: 540 calls (77 a day), hit rate 0.591, chance 0.302, lift 1.96x
    - 30d: 2392 calls (80 a day), hit rate 0.588, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.495; 0.35: 538, 0.518; 0.40: 485, 0.565; 0.45: 417, 0.631; 0.50: 364, 0.685; 0.55: 320, 0.726; 0.60: 273, 0.770; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 139, 0.874; 0.80: 98, 0.912; 0.85: 49, 0.948; 0.90: 3, 0.975
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 498, 0.460; 0.40: 412, 0.489; 0.45: 316, 0.522; 0.50: 206, 0.556; 0.55: 92, 0.583; 0.60: 14, 0.608; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 100237, probability skill vs chance 0.2145, widened contest next: False
  - now: threshold 0.713, hit rate recent 0.8409 / long run 0.8312
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.208, naive rule 0.487, lift 4.27x
    - 24h: 58 calls (58 a day), hit rate 0.845, chance 0.199, naive rule 0.428, lift 4.26x
    - 7d: 380 calls (54 a day), hit rate 0.811, chance 0.194, naive rule 0.407, lift 4.18x
    - 30d: 1603 calls (53 a day), hit rate 0.837, chance 0.188, naive rule 0.393, lift 4.46x
  - next: threshold 0.4503, hit rate recent 0.477 / long run 0.4699
    - 6h: 18 calls (73 a day), hit rate 0.444, chance 0.208, lift 2.13x
    - 24h: 67 calls (67 a day), hit rate 0.493, chance 0.199, lift 2.48x
    - 7d: 438 calls (63 a day), hit rate 0.473, chance 0.194, lift 2.44x
    - 30d: 2080 calls (69 a day), hit rate 0.485, chance 0.188, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 427, 0.417; 0.35: 362, 0.474; 0.40: 292, 0.544; 0.45: 239, 0.603; 0.50: 185, 0.660; 0.55: 140, 0.706; 0.60: 110, 0.749; 0.65: 84, 0.796; 0.70: 63, 0.826; 0.75: 34, 0.866; 0.80: 10, 0.890
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 252, 0.425; 0.40: 164, 0.453; 0.45: 83, 0.475; 0.50: 20, 0.517; 0.55: 2, 0.557
- **K=8**: model 1791417600, labels learned 100234, probability skill vs chance 0.206, widened contest next: False
  - now: threshold 0.5601, hit rate recent 0.726 / long run 0.7097
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.137, naive rule 0.442, lift 6.08x
    - 24h: 63 calls (63 a day), hit rate 0.746, chance 0.128, naive rule 0.350, lift 5.85x
    - 7d: 425 calls (61 a day), hit rate 0.685, chance 0.124, naive rule 0.341, lift 5.53x
    - 30d: 1600 calls (53 a day), hit rate 0.721, chance 0.122, naive rule 0.330, lift 5.90x
  - next: threshold 0.3608, hit rate recent 0.3892 / long run 0.3921
    - 6h: 24 calls (99 a day), hit rate 0.458, chance 0.137, lift 3.34x
    - 24h: 86 calls (87 a day), hit rate 0.360, chance 0.128, lift 2.82x
    - 7d: 617 calls (88 a day), hit rate 0.387, chance 0.124, lift 3.13x
    - 30d: 2108 calls (70 a day), hit rate 0.406, chance 0.122, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 267, 0.409; 0.35: 201, 0.485; 0.40: 155, 0.545; 0.45: 122, 0.591; 0.50: 93, 0.636; 0.55: 67, 0.690; 0.60: 46, 0.729; 0.65: 25, 0.773; 0.70: 9, 0.823; 0.75: 1, 0.864
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 183, 0.351; 0.35: 112, 0.389; 0.40: 47, 0.416; 0.45: 10, 0.448; 0.50: 1, 0.390
- **K=13**: model 1791504000, labels learned 100229, probability skill vs chance 0.1819, widened contest next: False
  - now: threshold 0.4361, hit rate recent 0.5916 / long run 0.5862
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.070, naive rule 0.321, lift 8.98x
    - 24h: 55 calls (56 a day), hit rate 0.582, chance 0.080, naive rule 0.287, lift 7.27x
    - 7d: 394 calls (56 a day), hit rate 0.571, chance 0.079, naive rule 0.283, lift 7.20x
    - 30d: 1498 calls (50 a day), hit rate 0.585, chance 0.078, naive rule 0.271, lift 7.53x
  - next: threshold 0.2865, hit rate recent 0.3688 / long run 0.3219
    - 6h: 18 calls (75 a day), hit rate 0.389, chance 0.070, lift 5.59x
    - 24h: 72 calls (73 a day), hit rate 0.375, chance 0.080, lift 4.69x
    - 7d: 506 calls (72 a day), hit rate 0.332, chance 0.079, lift 4.19x
    - 30d: 2060 calls (69 a day), hit rate 0.315, chance 0.078, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.449; 0.35: 87, 0.511; 0.40: 62, 0.558; 0.45: 43, 0.613; 0.50: 27, 0.637; 0.55: 14, 0.691; 0.60: 5, 0.732; 0.65: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 14, 0.353; 0.40: 3, 0.325; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.409 | 3.13% | 0.933 | 0.500 | 0.254 | 0.400 | 0.520 |
| 6h | 12.554 | 8.07% | 0.928 | 0.511 | 0.251 | 0.463 | 0.574 |
| 24h | 8.027 | 4.12% | 0.902 | 0.500 | 0.250 | 0.508 | 0.595 |
| 7d | 11.358 | 5.10% | 0.901 | 0.500 | 0.251 | 0.494 | 0.662 |
| 30d | 13.608 | 4.27% | 0.900 | 0.500 | 0.251 | 0.498 | 0.693 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.746 | 10.583 | 10.447 | 10.302 | 10.521 | 10.405 | 10.469 | 10.315 | 10.353 | 10.409 |
| 6h | 13.656 | 12.617 | 12.563 | 12.620 | 13.048 | 12.818 | 12.583 | 12.495 | 12.526 | 12.554 |
| 24h | 8.372 | 8.090 | 8.050 | 8.064 | 8.255 | 8.167 | 8.032 | 7.996 | 8.014 | 8.027 |
| 7d | 11.969 | 11.462 | 11.430 | 11.411 | 11.558 | 11.551 | 11.357 | 11.336 | 11.339 | 11.358 |
| 30d | 14.214 | 13.728 | 13.691 | 13.637 | 13.867 | 13.817 | 13.606 | 13.581 | 13.582 | 13.608 |

## Next candle

- candle starting 2026-10-11 18:45 UTC, last close 2535.49
- P(up) 0.5094, return quantiles (bp): {'05': -7.608, '10': -5.064, '25': -2.322, '40': -0.698, '50': 0.065, '60': 1.106, '75': 2.558, '90': 5.478, '95': 7.294}
- changepoint probability 0.1189, regime age 40.7 min
- agent weights: empirical 0.003, ewma 0.074, garch 0.149, har 0.112, bocpd 0.004, hmm 0.013, online_qr 0.182, lgbm 0.464

## Learning log

- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- HMM volatility states (sd, bp per minute): [2.07, 4.68, 13.59], current probabilities: [0.013, 0.967, 0.021]
- live generator: {'versions': 60, 'latest_effective': '2026-10-11 18:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.202, 'l_abs': 0.663, 'l_hi': 0.707, 'l_lo': 0.656, 'b05': 0.649, 'b25': 0.598, 'b75': 0.643, 'b95': 0.612}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.335, 2.0, 2.224, 2.865, 3.083, 3.206, 3.72, 3.506, 3.778, 3.593, 4.78, 4.334, 4.598, 4.674]}
- calibration offsets (in sigma): {'05': 0.032, '10': 0.054, '25': 0.02, '40': -0.014, '50': -0.01, '60': -0.036, '75': -0.04, '90': 0.006, '95': 0.018}
