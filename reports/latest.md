# ETH-USD 60s candle generator - report

- generated: 2026-10-06 19:02 UTC
- last closed candle: 2026-10-06 19:02 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.432 (95) | 0.508 (669) [0.470, 0.551] | 0.506 (2875) [0.488, 0.526] | 0.513 (3259) [0.495, 0.531] | 0.533 (287) [0.465, 0.601] | 0.579 (76) | 0.500 | flat -0.030 (noise 0.033) |
| colour_clear | 0.563 (766) | 0.515 (5282) [0.493, 0.538] | 0.503 (23277) [0.496, 0.510] | 0.501 (26399) [0.495, 0.507] | 0.556 (2161) [0.550, 0.561] | 0.525 (625) | 0.500 | flat +0.018 (noise 0.014) |
| colour_confident | 0.718 (103) | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.496 (125) | 0.500 | - |
| colour_next | 0.552 (1430) | 0.518 (9994) [0.504, 0.532] | 0.504 (42889) [0.499, 0.510] | 0.504 (48600) [0.499, 0.509] | 0.541 (4251) [0.530, 0.551] | 0.509 (1131) | 0.500 | flat +0.019 (noise 0.010) |
| colour_path | 0.508 (20020) | 0.502 (139916) [0.499, 0.506] | 0.501 (600446) [0.500, 0.503] | 0.501 (680400) [0.500, 0.502] | 0.502 (59514) [0.497, 0.507] | 0.499 (15834) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.800 (15) | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.548 (31) | 0.500 | - |
| reversal_k13_next | 0.288 (73) | 0.291 (635) [0.267, 0.316] | 0.308 (2020) [0.293, 0.324] | 0.303 (2366) [0.288, 0.318] | 0.326 (261) [0.302, 0.347] | 0.327 (52) | 0.077 | flat -0.009 (noise 0.029) |
| reversal_k13_now | 0.559 (68) | 0.581 (387) [0.535, 0.631] | 0.587 (1468) [0.564, 0.610] | 0.586 (1650) [0.566, 0.606] | 0.624 (178) [0.572, 0.690] | 0.511 (47) | 0.077 | flat -0.030 (noise 0.037) |
| reversal_k3_next | 0.653 (49) | 0.590 (656) [0.564, 0.621] | 0.584 (2457) [0.569, 0.599] | 0.586 (2757) [0.573, 0.601] | 0.577 (317) [0.552, 0.622] | 0.710 (31) | 0.292 | flat +0.039 (noise 0.029) |
| reversal_k3_now | 0.958 (48) | 0.940 (417) [0.930, 0.952] | 0.941 (1702) [0.933, 0.950] | 0.941 (1932) [0.933, 0.949] | 0.935 (169) [0.924, 0.948] | 0.875 (48) | 0.292 | flat +0.004 (noise 0.017) |
| reversal_k5_next | 0.538 (39) | 0.466 (726) [0.435, 0.498] | 0.486 (2120) [0.466, 0.506] | 0.487 (2338) [0.470, 0.505] | 0.448 (348) [0.420, 0.505] | 0.444 (36) | 0.187 | flat -0.042 (noise 0.036) |
| reversal_k5_now | 0.867 (45) | 0.853 (395) [0.839, 0.870] | 0.838 (1583) [0.823, 0.852] | 0.840 (1785) [0.825, 0.854] | 0.862 (174) [0.832, 0.889] | 0.714 (42) | 0.187 | flat +0.019 (noise 0.027) |
| reversal_k8_next | 0.365 (74) | 0.400 (468) [0.365, 0.433] | 0.401 (2030) [0.383, 0.421] | 0.397 (2344) [0.381, 0.415] | 0.408 (238) [0.369, 0.442] | 0.429 (70) | 0.122 | flat -0.009 (noise 0.034) |
| reversal_k8_now | 0.770 (61) | 0.740 (358) [0.711, 0.764] | 0.724 (1569) [0.705, 0.743] | 0.720 (1758) [0.701, 0.739] | 0.778 (171) [0.773, 0.782] | 0.667 (51) | 0.122 | flat -0.015 (noise 0.033) |
| overall | 0.512 (22002) | 0.505 (154621) [0.502, 0.509] | 0.503 (661159) [0.502, 0.505] | 0.503 (749189) [0.502, 0.504] | 0.507 (65908) [0.502, 0.512] | 0.502 (17418) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07772, 0.1158] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5339, 'levels': [{'threshold': 0.07772, 'calls_per_day': 144.7, 'win_rate': 0.5841}, {'threshold': 0.1158, 'calls_per_day': 36.5, 'win_rate': 0.6395}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 4250, 'rate': 0.5407}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15261 | 0.332 | 0.512 (15021) | 0.611 (506) | 0.783 (2452) |
| volatility: normal | 15260 | 0.359 | 0.508 (15192) | 0.564 (55) | 0.776 (2157) |
| volatility: wild | 15261 | 0.373 | 0.495 (15216) | - | 0.776 (2123) |
| session: Asia 00-08 | 15360 | 0.351 | 0.505 (15248) | 0.604 (207) | 0.780 (2230) |
| session: Europe 08-13 | 9600 | 0.347 | 0.503 (9525) | 0.549 (111) | 0.770 (1465) |
| session: US 13-21 | 15242 | 0.364 | 0.505 (15135) | 0.623 (167) | 0.787 (2262) |
| session: late 21-24 | 5580 | 0.351 | 0.507 (5521) | 0.678 (87) | 0.764 (775) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.335 | 0.343 | 0.325 | 0.325 | 0.483 | 0.209 | 0.461 | 1.808 |
| 6h | 360 | 0.362 | 0.367 | 0.313 | 0.340 | 0.462 | 0.230 | 0.494 | 1.182 |
| 24h | 1440 | 0.362 | 0.352 | 0.286 | 0.309 | 0.522 | 0.261 | 0.463 | 1.183 |
| 7d | 10080 | 0.351 | 0.349 | 0.276 | 0.300 | 0.518 | 0.245 | 0.457 | 1.301 |
| 30d | 43200 | 0.356 | 0.355 | 0.278 | 0.308 | 0.505 | 0.247 | 0.465 | 1.287 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.335 / 0.483 / 0.967; 2: 0.331 / 0.467 / 0.883; 3: 0.337 / 0.500 / 0.933; 4: 0.345 / 0.500 / 0.933; 5: 0.345 / 0.533 / 0.917; 6: 0.350 / 0.533 / 0.933; 7: 0.339 / 0.567 / 0.850; 8: 0.335 / 0.533 / 0.867; 9: 0.326 / 0.483 / 0.850; 10: 0.318 / 0.400 / 0.950; 11: 0.325 / 0.517 / 0.883; 12: 0.313 / 0.400 / 0.817; 13: 0.325 / 0.583 / 0.883; 14: 0.328 / 0.550 / 0.867; 15: 0.323 / 0.483 / 0.833
- 6h: 1: 0.362 / 0.462 / 0.908; 2: 0.371 / 0.501 / 0.878; 3: 0.374 / 0.524 / 0.883; 4: 0.371 / 0.499 / 0.900; 5: 0.363 / 0.473 / 0.933; 6: 0.373 / 0.521 / 0.947; 7: 0.365 / 0.521 / 0.875; 8: 0.381 / 0.555 / 0.872; 9: 0.369 / 0.510 / 0.844; 10: 0.372 / 0.521 / 0.942; 11: 0.370 / 0.510 / 0.872; 12: 0.376 / 0.515 / 0.869; 13: 0.361 / 0.493 / 0.908; 14: 0.369 / 0.529 / 0.914; 15: 0.373 / 0.499 / 0.911
- 24h: 1: 0.362 / 0.522 / 0.911; 2: 0.352 / 0.500 / 0.886; 3: 0.350 / 0.499 / 0.896; 4: 0.349 / 0.494 / 0.894; 5: 0.348 / 0.500 / 0.901; 6: 0.344 / 0.492 / 0.899; 7: 0.346 / 0.507 / 0.894; 8: 0.346 / 0.499 / 0.884; 9: 0.344 / 0.491 / 0.878; 10: 0.346 / 0.508 / 0.910; 11: 0.347 / 0.512 / 0.885; 12: 0.350 / 0.499 / 0.886; 13: 0.352 / 0.520 / 0.887; 14: 0.344 / 0.487 / 0.887; 15: 0.350 / 0.507 / 0.888
- 7d: 1: 0.351 / 0.518 / 0.899; 2: 0.346 / 0.502 / 0.899; 3: 0.347 / 0.511 / 0.899; 4: 0.343 / 0.501 / 0.900; 5: 0.342 / 0.503 / 0.901; 6: 0.341 / 0.497 / 0.901; 7: 0.342 / 0.507 / 0.899; 8: 0.341 / 0.500 / 0.899; 9: 0.337 / 0.491 / 0.899; 10: 0.340 / 0.505 / 0.901; 11: 0.341 / 0.506 / 0.899; 12: 0.342 / 0.512 / 0.899; 13: 0.342 / 0.507 / 0.899; 14: 0.338 / 0.492 / 0.900; 15: 0.339 / 0.498 / 0.900
- 30d: 1: 0.356 / 0.505 / 0.899; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.501 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.349 / 0.506 / 0.900; 8: 0.349 / 0.504 / 0.900; 9: 0.346 / 0.499 / 0.900; 10: 0.348 / 0.504 / 0.900; 11: 0.347 / 0.502 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.345 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.064 (body 0.026, range 0.102); 'price stays where it was' would score 0.045; colour right 0.583; typical miss of the close 6.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.116 (body 0.078, range 0.155); 'price stays where it was' would score 0.130; colour right 0.493; typical miss of the close 7.1 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.112 (body 0.075, range 0.148); 'price stays where it was' would score 0.124; colour right 0.501; typical miss of the close 5.7 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.116 (body 0.077, range 0.155); 'price stays where it was' would score 0.120; colour right 0.496; typical miss of the close 6.2 bp; chain ended on the right side 0.528 of 670 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.511 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.2; 2: 0.199 / 4.4; 3: 0.169 / 6.1; 4: 0.133 / 6.5; 5: 0.123 / 7.3; 6: 0.112 / 8.2; 7: 0.099 / 8.6; 8: 0.090 / 9.0; 9: 0.085 / 9.3; 10: 0.080 / 10.1; 11: 0.075 / 10.7; 12: 0.073 / 11.0; 13: 0.065 / 11.3; 14: 0.065 / 11.5; 15: 0.061 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 93056, probability skill vs chance 0.2331, widened contest next: False
  - now: threshold 0.8427, hit rate recent 0.9063 / long run 0.935
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.299, naive rule 0.520, lift 3.35x
    - 24h: 59 calls (59 a day), hit rate 0.881, chance 0.303, naive rule 0.503, lift 2.90x
    - 7d: 411 calls (59 a day), hit rate 0.929, chance 0.293, naive rule 0.491, lift 3.17x
    - 30d: 1697 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.481, lift 3.22x
  - next: threshold 0.5633, hit rate recent 0.6681 / long run 0.5913
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.299, lift 2.63x
    - 24h: 39 calls (39 a day), hit rate 0.692, chance 0.303, lift 2.28x
    - 7d: 608 calls (87 a day), hit rate 0.590, chance 0.293, lift 2.01x
    - 30d: 2416 calls (81 a day), hit rate 0.585, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 538, 0.517; 0.40: 487, 0.560; 0.45: 421, 0.626; 0.50: 368, 0.680; 0.55: 322, 0.723; 0.60: 275, 0.766; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 139, 0.869; 0.80: 98, 0.908; 0.85: 49, 0.947; 0.90: 2, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 497, 0.459; 0.40: 413, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.552; 0.55: 92, 0.586; 0.60: 13, 0.621; 0.65: 0, 0.750
- **K=5**: model 1790208000, labels learned 93054, probability skill vs chance 0.2143, widened contest next: True
  - now: threshold 0.7138, hit rate recent 0.7984 / long run 0.8376
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.183, naive rule 0.382, lift 4.69x
    - 24h: 55 calls (55 a day), hit rate 0.745, chance 0.196, naive rule 0.411, lift 3.80x
    - 7d: 389 calls (56 a day), hit rate 0.843, chance 0.191, naive rule 0.403, lift 4.41x
    - 30d: 1576 calls (53 a day), hit rate 0.835, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4558, hit rate recent 0.4852 / long run 0.4751
    - 6h: 13 calls (53 a day), hit rate 0.385, chance 0.183, lift 2.10x
    - 24h: 44 calls (44 a day), hit rate 0.455, chance 0.196, lift 2.32x
    - 7d: 719 calls (103 a day), hit rate 0.462, chance 0.191, lift 2.41x
    - 30d: 2108 calls (70 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 431, 0.411; 0.35: 370, 0.464; 0.40: 300, 0.533; 0.45: 245, 0.590; 0.50: 191, 0.649; 0.55: 145, 0.698; 0.60: 113, 0.738; 0.65: 87, 0.783; 0.70: 64, 0.820; 0.75: 34, 0.860; 0.80: 9, 0.886
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 254, 0.422; 0.40: 166, 0.449; 0.45: 86, 0.473; 0.50: 21, 0.519; 0.55: 2, 0.587
- **K=8**: model 1791158400, labels learned 93051, probability skill vs chance 0.2001, widened contest next: False
  - now: threshold 0.5645, hit rate recent 0.7318 / long run 0.7316
    - 6h: 15 calls (62 a day), hit rate 0.800, chance 0.120, naive rule 0.319, lift 6.67x
    - 24h: 63 calls (63 a day), hit rate 0.698, chance 0.127, naive rule 0.348, lift 5.52x
    - 7d: 368 calls (53 a day), hit rate 0.739, chance 0.127, naive rule 0.341, lift 5.84x
    - 30d: 1572 calls (52 a day), hit rate 0.724, chance 0.121, naive rule 0.325, lift 5.98x
  - next: threshold 0.3474, hit rate recent 0.427 / long run 0.4095
    - 6h: 23 calls (95 a day), hit rate 0.391, chance 0.120, lift 3.26x
    - 24h: 80 calls (81 a day), hit rate 0.438, chance 0.127, lift 3.46x
    - 7d: 489 calls (70 a day), hit rate 0.407, chance 0.127, lift 3.22x
    - 30d: 2042 calls (68 a day), hit rate 0.403, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 274, 0.398; 0.35: 207, 0.474; 0.40: 159, 0.535; 0.45: 126, 0.583; 0.50: 96, 0.626; 0.55: 68, 0.682; 0.60: 46, 0.727; 0.65: 24, 0.769; 0.70: 9, 0.801; 0.75: 1, 0.800
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 187, 0.344; 0.35: 116, 0.384; 0.40: 48, 0.413; 0.45: 10, 0.429; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 93046, probability skill vs chance 0.1802, widened contest next: False
  - now: threshold 0.4197, hit rate recent 0.5602 / long run 0.5864
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.065, naive rule 0.222, lift 9.44x
    - 24h: 59 calls (60 a day), hit rate 0.508, chance 0.070, naive rule 0.251, lift 7.25x
    - 7d: 383 calls (55 a day), hit rate 0.593, chance 0.079, naive rule 0.275, lift 7.54x
    - 30d: 1479 calls (49 a day), hit rate 0.583, chance 0.076, naive rule 0.265, lift 7.62x
  - next: threshold 0.2777, hit rate recent 0.3298 / long run 0.3059
    - 6h: 17 calls (71 a day), hit rate 0.294, chance 0.065, lift 4.51x
    - 24h: 67 calls (68 a day), hit rate 0.313, chance 0.070, lift 4.47x
    - 7d: 598 calls (86 a day), hit rate 0.303, chance 0.079, lift 3.85x
    - 30d: 2036 calls (68 a day), hit rate 0.307, chance 0.076, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.434; 0.35: 90, 0.492; 0.40: 65, 0.541; 0.45: 45, 0.598; 0.50: 28, 0.616; 0.55: 15, 0.669; 0.60: 6, 0.698; 0.65: 2, 0.759; 0.70: 0, 0.600
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.312; 0.35: 17, 0.351; 0.40: 4, 0.333; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.791 | 3.15% | 0.933 | 0.650 | 0.249 | 0.533 | 0.153 |
| 6h | 11.065 | 3.43% | 0.900 | 0.483 | 0.251 | 0.471 | 0.505 |
| 24h | 8.881 | 4.24% | 0.903 | 0.497 | 0.251 | 0.478 | 0.460 |
| 7d | 10.881 | 4.71% | 0.901 | 0.500 | 0.251 | 0.494 | 0.678 |
| 30d | 14.152 | 4.18% | 0.900 | 0.500 | 0.251 | 0.497 | 0.693 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.980 | 5.911 | 5.832 | 5.934 | 5.867 | 5.849 | 5.884 | 5.831 | 5.848 | 5.791 |
| 6h | 11.458 | 11.099 | 11.083 | 11.059 | 11.163 | 11.242 | 11.099 | 11.084 | 11.046 | 11.065 |
| 24h | 9.274 | 8.956 | 8.922 | 8.905 | 9.041 | 9.009 | 8.890 | 8.884 | 8.868 | 8.881 |
| 7d | 11.420 | 10.974 | 10.967 | 10.912 | 11.114 | 11.072 | 10.876 | 10.872 | 10.864 | 10.881 |
| 30d | 14.769 | 14.281 | 14.236 | 14.179 | 14.422 | 14.366 | 14.154 | 14.127 | 14.125 | 14.152 |

## Next candle

- candle starting 2026-10-06 19:02 UTC, last close 2690.04
- P(up) 0.4615, return quantiles (bp): {'05': -3.674, '10': -2.796, '25': -1.566, '40': -0.66, '50': -0.147, '60': 0.246, '75': 1.193, '90': 2.84, '95': 3.782}
- changepoint probability 0.059, regime age 50.6 min
- agent weights: empirical 0.007, ewma 0.108, garch 0.162, har 0.223, bocpd 0.043, hmm 0.051, online_qr 0.191, lgbm 0.215

## Learning log

- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- HMM volatility states (sd, bp per minute): [1.78, 4.45, 12.43], current probabilities: [0.946, 0.053, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-06 19:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.213, 'l_abs': 0.643, 'l_hi': 0.766, 'l_lo': 0.769, 'b05': 0.718, 'b25': 0.651, 'b75': 0.712, 'b95': 0.714}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6]], 'cone_width': [1.544, 1.858, 1.906, 1.82, 1.919, 2.86, 3.064, 3.899, 2.706, 3.762, 3.859, 3.362, 3.359, 3.554]}
- calibration offsets (in sigma): {'05': 0.0605, '10': 0.021, '25': -0.0475, '40': -0.066, '50': -0.055, '60': -0.084, '75': -0.0725, '90': -0.031, '95': -0.0505}
