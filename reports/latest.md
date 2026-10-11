# ETH-USD 60s candle generator - report

- generated: 2026-10-11 13:58 UTC
- last closed candle: 2026-10-11 13:58 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.508 (671) [0.454, 0.562] | 0.508 (2875) [0.488, 0.529] | 0.511 (3739) [0.494, 0.528] | 0.511 (767) [0.465, 0.557] | 0.509 (55) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.537 (778) | 0.545 (5363) [0.536, 0.553] | 0.510 (23183) [0.502, 0.518] | 0.506 (30322) [0.500, 0.512] | 0.545 (6084) [0.538, 0.552] | 0.534 (431) | 0.500 | up +0.044 (noise 0.010) |
| colour_confident | 0.567 (275) | 0.607 (1140) [0.574, 0.646] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.581 (155) | 0.500 | flat -0.000 (noise 0.055) |
| colour_next | 0.529 (1387) | 0.530 (9958) [0.521, 0.539] | 0.508 (42835) [0.502, 0.513] | 0.506 (55711) [0.501, 0.511] | 0.529 (11362) [0.521, 0.537] | 0.536 (823) | 0.500 | up +0.023 (noise 0.007) |
| colour_path | 0.500 (19418) | 0.500 (139412) [0.497, 0.503] | 0.501 (599690) [0.500, 0.502] | 0.500 (779954) [0.499, 0.502] | 0.499 (159068) [0.496, 0.502] | 0.500 (11522) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.648 (88) | 0.656 (305) [0.602, 0.720] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.636 (55) | 0.500 | - |
| reversal_k13_next | 0.361 (72) | 0.329 (511) [0.312, 0.345] | 0.312 (2046) [0.297, 0.328] | 0.306 (2718) [0.293, 0.320] | 0.328 (613) [0.314, 0.341] | 0.378 (45) | 0.077 | flat +0.053 (noise 0.027) |
| reversal_k13_now | 0.576 (59) | 0.575 (400) [0.548, 0.604] | 0.587 (1490) [0.565, 0.612] | 0.584 (1917) [0.566, 0.602] | 0.593 (445) [0.559, 0.637] | 0.559 (34) | 0.077 | flat -0.019 (noise 0.039) |
| reversal_k3_next | 0.620 (129) | 0.591 (557) [0.559, 0.621] | 0.586 (2386) [0.571, 0.602] | 0.586 (3141) [0.573, 0.598] | 0.579 (701) [0.550, 0.610] | 0.552 (67) | 0.293 | flat +0.013 (noise 0.028) |
| reversal_k3_now | 0.910 (67) | 0.923 (418) [0.914, 0.936] | 0.940 (1718) [0.931, 0.947] | 0.938 (2238) [0.931, 0.945] | 0.924 (475) [0.916, 0.935] | 0.885 (52) | 0.293 | flat -0.022 (noise 0.017) |
| reversal_k5_next | 0.507 (73) | 0.471 (480) [0.441, 0.496] | 0.485 (2092) [0.467, 0.503] | 0.484 (2659) [0.467, 0.501] | 0.453 (669) [0.425, 0.487] | 0.436 (39) | 0.187 | flat +0.019 (noise 0.030) |
| reversal_k5_now | 0.873 (63) | 0.827 (387) [0.791, 0.861] | 0.838 (1590) [0.823, 0.853] | 0.835 (2059) [0.821, 0.849] | 0.826 (448) [0.795, 0.855] | 0.800 (35) | 0.187 | flat -0.031 (noise 0.026) |
| reversal_k8_next | 0.449 (69) | 0.396 (613) [0.367, 0.429] | 0.407 (2098) [0.389, 0.427] | 0.396 (2796) [0.382, 0.411] | 0.394 (690) [0.369, 0.422] | 0.280 (50) | 0.122 | flat +0.016 (noise 0.031) |
| reversal_k8_now | 0.770 (61) | 0.699 (418) [0.654, 0.741] | 0.722 (1585) [0.703, 0.742] | 0.712 (2055) [0.694, 0.731] | 0.707 (468) [0.665, 0.745] | 0.658 (38) | 0.122 | flat -0.037 (noise 0.034) |
| overall | 0.506 (21494) | 0.504 (153825) [0.500, 0.508] | 0.504 (660405) [0.502, 0.505] | 0.503 (858987) [0.501, 0.504] | 0.503 (175706) [0.499, 0.507] | 0.504 (12760) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08112, 0.1224] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5301, 'levels': [{'threshold': 0.08112, 'calls_per_day': 143.9, 'win_rate': 0.598}, {'threshold': 0.1224, 'calls_per_day': 35.7, 'win_rate': 0.668}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 11051, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15160 | 0.331 | 0.519 (14890) | 0.594 (1112) | 0.778 (2477) |
| volatility: normal | 15159 | 0.358 | 0.508 (15085) | 0.633 (199) | 0.777 (2198) |
| volatility: wild | 15159 | 0.374 | 0.496 (15114) | 0.676 (68) | 0.774 (2094) |
| session: Asia 00-08 | 15360 | 0.351 | 0.511 (15243) | 0.600 (502) | 0.777 (2221) |
| session: Europe 08-13 | 9600 | 0.348 | 0.507 (9506) | 0.594 (345) | 0.769 (1532) |
| session: US 13-21 | 14938 | 0.364 | 0.504 (14831) | 0.577 (336) | 0.784 (2205) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5509) | 0.679 (196) | 0.767 (811) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.269 | 0.306 | 0.256 | 0.256 | 0.383 | 0.149 | 0.389 | 1.265 |
| 6h | 360 | 0.321 | 0.309 | 0.240 | 0.270 | 0.535 | 0.237 | 0.404 | 1.315 |
| 24h | 1440 | 0.322 | 0.316 | 0.239 | 0.263 | 0.532 | 0.244 | 0.401 | 1.222 |
| 7d | 10080 | 0.353 | 0.346 | 0.271 | 0.299 | 0.530 | 0.259 | 0.448 | 1.195 |
| 30d | 43200 | 0.354 | 0.352 | 0.276 | 0.305 | 0.508 | 0.247 | 0.461 | 1.305 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.269 / 0.383 / 0.883; 2: 0.328 / 0.533 / 0.933; 3: 0.316 / 0.517 / 0.950; 4: 0.347 / 0.617 / 0.950; 5: 0.313 / 0.533 / 0.967; 6: 0.295 / 0.467 / 1.000; 7: 0.276 / 0.450 / 1.000; 8: 0.304 / 0.517 / 1.000; 9: 0.314 / 0.500 / 1.000; 10: 0.301 / 0.500 / 1.000; 11: 0.282 / 0.417 / 1.000; 12: 0.311 / 0.450 / 1.000; 13: 0.318 / 0.467 / 0.983; 14: 0.316 / 0.467 / 1.000; 15: 0.304 / 0.433 / 1.000
- 6h: 1: 0.321 / 0.535 / 0.886; 2: 0.303 / 0.496 / 0.947; 3: 0.308 / 0.493 / 0.953; 4: 0.318 / 0.535 / 0.947; 5: 0.294 / 0.459 / 0.975; 6: 0.301 / 0.462 / 0.994; 7: 0.314 / 0.499 / 0.994; 8: 0.310 / 0.493 / 0.986; 9: 0.318 / 0.518 / 0.994; 10: 0.308 / 0.470 / 0.994; 11: 0.303 / 0.459 / 0.997; 12: 0.311 / 0.499 / 0.992; 13: 0.328 / 0.532 / 0.997; 14: 0.317 / 0.487 / 1.000; 15: 0.307 / 0.482 / 1.000
- 24h: 1: 0.322 / 0.532 / 0.888; 2: 0.314 / 0.499 / 0.913; 3: 0.312 / 0.506 / 0.922; 4: 0.312 / 0.501 / 0.924; 5: 0.314 / 0.518 / 0.927; 6: 0.308 / 0.489 / 0.928; 7: 0.311 / 0.504 / 0.931; 8: 0.311 / 0.500 / 0.923; 9: 0.309 / 0.488 / 0.918; 10: 0.311 / 0.500 / 0.925; 11: 0.312 / 0.497 / 0.922; 12: 0.308 / 0.496 / 0.935; 13: 0.315 / 0.515 / 0.927; 14: 0.311 / 0.495 / 0.921; 15: 0.308 / 0.497 / 0.909
- 7d: 1: 0.353 / 0.530 / 0.898; 2: 0.343 / 0.500 / 0.901; 3: 0.344 / 0.509 / 0.902; 4: 0.342 / 0.504 / 0.902; 5: 0.341 / 0.505 / 0.903; 6: 0.338 / 0.496 / 0.904; 7: 0.339 / 0.502 / 0.903; 8: 0.338 / 0.497 / 0.903; 9: 0.336 / 0.491 / 0.903; 10: 0.339 / 0.505 / 0.903; 11: 0.337 / 0.493 / 0.903; 12: 0.338 / 0.497 / 0.905; 13: 0.340 / 0.508 / 0.904; 14: 0.337 / 0.501 / 0.903; 15: 0.338 / 0.498 / 0.902
- 30d: 1: 0.354 / 0.508 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.351 / 0.509 / 0.901; 4: 0.347 / 0.500 / 0.901; 5: 0.348 / 0.504 / 0.901; 6: 0.346 / 0.502 / 0.901; 7: 0.346 / 0.504 / 0.901; 8: 0.346 / 0.503 / 0.901; 9: 0.343 / 0.496 / 0.901; 10: 0.345 / 0.504 / 0.901; 11: 0.344 / 0.501 / 0.901; 12: 0.344 / 0.502 / 0.901; 13: 0.344 / 0.501 / 0.901; 14: 0.343 / 0.497 / 0.901; 15: 0.342 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.068 (body 0.033, range 0.103); 'price stays where it was' would score 0.140; colour right 0.450; typical miss of the close 4.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.107 (body 0.070, range 0.144); 'price stays where it was' would score 0.144; colour right 0.524; typical miss of the close 4.1 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.112 (body 0.079, range 0.146); 'price stays where it was' would score 0.133; colour right 0.508; typical miss of the close 4.4 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.117 (body 0.080, range 0.153); 'price stays where it was' would score 0.124; colour right 0.500; typical miss of the close 6.2 bp; chain ended on the right side 0.495 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.7 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 3.9; 2: 0.199 / 4.3; 3: 0.166 / 5.8; 4: 0.132 / 6.4; 5: 0.120 / 7.0; 6: 0.109 / 7.6; 7: 0.102 / 8.0; 8: 0.092 / 8.3; 9: 0.086 / 8.6; 10: 0.081 / 9.3; 11: 0.077 / 9.8; 12: 0.075 / 10.3; 13: 0.063 / 10.7; 14: 0.065 / 10.7; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 99952, probability skill vs chance 0.2211, widened contest next: True
  - now: threshold 0.8309, hit rate recent 0.8958 / long run 0.9272
    - 6h: 24 calls (97 a day), hit rate 0.875, chance 0.352, naive rule 0.614, lift 2.49x
    - 24h: 81 calls (81 a day), hit rate 0.901, chance 0.325, naive rule 0.544, lift 2.77x
    - 7d: 435 calls (62 a day), hit rate 0.917, chance 0.300, naive rule 0.498, lift 3.06x
    - 30d: 1737 calls (58 a day), hit rate 0.938, chance 0.293, naive rule 0.485, lift 3.21x
  - next: threshold 0.5666, hit rate recent 0.5959 / long run 0.5818
    - 6h: 24 calls (97 a day), hit rate 0.667, chance 0.352, lift 1.89x
    - 24h: 129 calls (129 a day), hit rate 0.605, chance 0.325, lift 1.86x
    - 7d: 563 calls (80 a day), hit rate 0.586, chance 0.300, lift 1.96x
    - 30d: 2393 calls (80 a day), hit rate 0.588, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.495; 0.35: 538, 0.518; 0.40: 485, 0.564; 0.45: 418, 0.631; 0.50: 364, 0.685; 0.55: 320, 0.726; 0.60: 273, 0.769; 0.65: 225, 0.802; 0.70: 181, 0.835; 0.75: 139, 0.874; 0.80: 98, 0.912; 0.85: 49, 0.948; 0.90: 3, 0.975
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.426; 0.35: 498, 0.460; 0.40: 412, 0.489; 0.45: 316, 0.521; 0.50: 206, 0.556; 0.55: 92, 0.583; 0.60: 14, 0.607; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 99950, probability skill vs chance 0.2106, widened contest next: False
  - now: threshold 0.7134, hit rate recent 0.8355 / long run 0.8306
    - 6h: 16 calls (65 a day), hit rate 0.750, chance 0.181, naive rule 0.411, lift 4.14x
    - 24h: 66 calls (66 a day), hit rate 0.864, chance 0.199, naive rule 0.422, lift 4.34x
    - 7d: 383 calls (55 a day), hit rate 0.815, chance 0.192, naive rule 0.401, lift 4.24x
    - 30d: 1601 calls (53 a day), hit rate 0.838, chance 0.188, naive rule 0.393, lift 4.47x
  - next: threshold 0.4648, hit rate recent 0.4732 / long run 0.4692
    - 6h: 20 calls (82 a day), hit rate 0.450, chance 0.181, lift 2.48x
    - 24h: 67 calls (67 a day), hit rate 0.448, chance 0.199, lift 2.25x
    - 7d: 453 calls (65 a day), hit rate 0.470, chance 0.192, lift 2.44x
    - 30d: 2073 calls (69 a day), hit rate 0.484, chance 0.188, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 428, 0.416; 0.35: 362, 0.474; 0.40: 293, 0.543; 0.45: 239, 0.603; 0.50: 185, 0.659; 0.55: 140, 0.706; 0.60: 110, 0.749; 0.65: 84, 0.795; 0.70: 63, 0.826; 0.75: 34, 0.867; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 252, 0.424; 0.40: 164, 0.453; 0.45: 83, 0.475; 0.50: 20, 0.514; 0.55: 2, 0.548
- **K=8**: model 1791417600, labels learned 99947, probability skill vs chance 0.1989, widened contest next: True
  - now: threshold 0.5623, hit rate recent 0.713 / long run 0.7082
    - 6h: 15 calls (62 a day), hit rate 0.867, chance 0.126, naive rule 0.333, lift 6.89x
    - 24h: 65 calls (65 a day), hit rate 0.723, chance 0.129, naive rule 0.342, lift 5.59x
    - 7d: 426 calls (61 a day), hit rate 0.690, chance 0.124, naive rule 0.337, lift 5.56x
    - 30d: 1595 calls (53 a day), hit rate 0.721, chance 0.122, naive rule 0.329, lift 5.90x
  - next: threshold 0.3518, hit rate recent 0.3542 / long run 0.3891
    - 6h: 20 calls (82 a day), hit rate 0.400, chance 0.126, lift 3.18x
    - 24h: 76 calls (77 a day), hit rate 0.289, chance 0.129, lift 2.24x
    - 7d: 620 calls (89 a day), hit rate 0.385, chance 0.124, lift 3.11x
    - 30d: 2101 calls (70 a day), hit rate 0.406, chance 0.122, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 267, 0.408; 0.35: 202, 0.484; 0.40: 155, 0.544; 0.45: 122, 0.591; 0.50: 93, 0.636; 0.55: 67, 0.690; 0.60: 46, 0.729; 0.65: 25, 0.772; 0.70: 9, 0.822; 0.75: 1, 0.864
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 183, 0.351; 0.35: 112, 0.390; 0.40: 47, 0.415; 0.45: 10, 0.449; 0.50: 1, 0.390
- **K=13**: model 1791504000, labels learned 99942, probability skill vs chance 0.1774, widened contest next: False
  - now: threshold 0.4357, hit rate recent 0.5878 / long run 0.5857
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.083, naive rule 0.308, lift 7.45x
    - 24h: 61 calls (62 a day), hit rate 0.574, chance 0.085, naive rule 0.286, lift 6.73x
    - 7d: 397 calls (57 a day), hit rate 0.574, chance 0.080, naive rule 0.282, lift 7.16x
    - 30d: 1494 calls (50 a day), hit rate 0.586, chance 0.078, naive rule 0.271, lift 7.54x
  - next: threshold 0.2864, hit rate recent 0.3733 / long run 0.3211
    - 6h: 17 calls (71 a day), hit rate 0.471, chance 0.083, lift 5.70x
    - 24h: 69 calls (70 a day), hit rate 0.348, chance 0.085, lift 4.08x
    - 7d: 513 calls (73 a day), hit rate 0.339, chance 0.080, lift 4.23x
    - 30d: 2054 calls (68 a day), hit rate 0.315, chance 0.078, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.449; 0.35: 86, 0.511; 0.40: 62, 0.558; 0.45: 43, 0.613; 0.50: 27, 0.639; 0.55: 14, 0.694; 0.60: 5, 0.733; 0.65: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 14, 0.352; 0.40: 2, 0.329; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.280 | 1.29% | 0.950 | 0.483 | 0.250 | 0.450 | 0.075 |
| 6h | 6.500 | 1.32% | 0.908 | 0.489 | 0.250 | 0.473 | 0.261 |
| 24h | 6.749 | 1.43% | 0.897 | 0.497 | 0.250 | 0.492 | 0.441 |
| 7d | 11.112 | 4.91% | 0.901 | 0.499 | 0.251 | 0.495 | 0.669 |
| 30d | 13.753 | 4.41% | 0.900 | 0.500 | 0.251 | 0.498 | 0.705 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.350 | 5.312 | 5.254 | 5.265 | 5.307 | 5.318 | 5.294 | 5.252 | 5.256 | 5.280 |
| 6h | 6.587 | 6.591 | 6.556 | 6.511 | 6.673 | 6.620 | 6.475 | 6.462 | 6.481 | 6.500 |
| 24h | 6.848 | 6.817 | 6.772 | 6.770 | 6.889 | 6.836 | 6.754 | 6.723 | 6.739 | 6.749 |
| 7d | 11.686 | 11.214 | 11.184 | 11.163 | 11.298 | 11.300 | 11.109 | 11.090 | 11.093 | 11.112 |
| 30d | 14.388 | 13.881 | 13.835 | 13.787 | 14.015 | 13.976 | 13.755 | 13.725 | 13.727 | 13.753 |

## Next candle

- candle starting 2026-10-11 13:58 UTC, last close 2499.92
- P(up) 0.5039, return quantiles (bp): {'05': -4.366, '10': -3.228, '25': -1.442, '40': -0.518, '50': 0.021, '60': 0.541, '75': 1.56, '90': 3.31, '95': 4.321}
- changepoint probability 0.5042, regime age 26.8 min
- agent weights: empirical 0.039, ewma 0.068, garch 0.117, har 0.165, bocpd 0.021, hmm 0.040, online_qr 0.233, lgbm 0.317

## Learning log

- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- HMM volatility states (sd, bp per minute): [2.07, 4.68, 13.59], current probabilities: [0.326, 0.67, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-11 14:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.262, 'l_abs': 0.651, 'l_hi': 0.705, 'l_lo': 0.647, 'b05': 0.642, 'b25': 0.605, 'b75': 0.616, 'b95': 0.576}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.249, 1.333, 1.671, 1.595, 1.716, 2.012, 1.989, 2.336, 2.419, 2.699, 2.456, 2.775, 3.253, 4.204]}
- calibration offsets (in sigma): {'05': -0.0515, '10': -0.053, '25': 0.0125, '40': -0.032, '50': -0.015, '60': -0.018, '75': -0.0025, '90': 0.033, '95': 0.0015}
