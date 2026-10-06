# ETH-USD 60s candle generator - report

- generated: 2026-10-06 06:34 UTC
- last closed candle: 2026-10-06 06:34 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.432 (95) | 0.508 (669) [0.470, 0.551] | 0.506 (2875) [0.488, 0.526] | 0.513 (3259) [0.495, 0.531] | 0.533 (287) [0.465, 0.601] | 0.462 (26) | 0.500 | flat -0.030 (noise 0.033) |
| colour_clear | 0.563 (766) | 0.515 (5282) [0.493, 0.538] | 0.503 (23277) [0.496, 0.510] | 0.501 (26399) [0.495, 0.507] | 0.556 (2161) [0.550, 0.561] | 0.578 (230) | 0.500 | flat +0.018 (noise 0.014) |
| colour_confident | 0.718 (103) | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.532 (47) | 0.500 | - |
| colour_next | 0.552 (1430) | 0.518 (9994) [0.504, 0.532] | 0.504 (42889) [0.499, 0.510] | 0.504 (48600) [0.499, 0.509] | 0.541 (4251) [0.530, 0.551] | 0.554 (390) | 0.500 | flat +0.019 (noise 0.010) |
| colour_path | 0.508 (20020) | 0.502 (139916) [0.499, 0.506] | 0.501 (600446) [0.500, 0.503] | 0.501 (680400) [0.500, 0.502] | 0.502 (59514) [0.497, 0.507] | 0.495 (5460) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.800 (15) | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.600 (10) | 0.500 | - |
| reversal_k13_next | 0.288 (73) | 0.291 (635) [0.267, 0.316] | 0.308 (2020) [0.293, 0.324] | 0.303 (2366) [0.288, 0.318] | 0.326 (261) [0.302, 0.347] | 0.188 (16) | 0.077 | flat -0.009 (noise 0.029) |
| reversal_k13_now | 0.559 (68) | 0.581 (387) [0.535, 0.631] | 0.587 (1468) [0.564, 0.610] | 0.586 (1650) [0.566, 0.606] | 0.624 (178) [0.572, 0.690] | 0.333 (18) | 0.077 | flat -0.030 (noise 0.037) |
| reversal_k3_next | 0.653 (49) | 0.590 (656) [0.564, 0.621] | 0.584 (2457) [0.569, 0.599] | 0.586 (2757) [0.573, 0.601] | 0.577 (317) [0.552, 0.622] | 0.600 (10) | 0.292 | flat +0.039 (noise 0.029) |
| reversal_k3_now | 0.958 (48) | 0.940 (417) [0.930, 0.952] | 0.941 (1702) [0.933, 0.950] | 0.941 (1932) [0.933, 0.949] | 0.935 (169) [0.924, 0.948] | 0.895 (19) | 0.292 | flat +0.004 (noise 0.017) |
| reversal_k5_next | 0.538 (39) | 0.466 (726) [0.435, 0.498] | 0.486 (2120) [0.466, 0.506] | 0.487 (2338) [0.470, 0.505] | 0.448 (348) [0.420, 0.505] | 0.333 (12) | 0.187 | flat -0.042 (noise 0.036) |
| reversal_k5_now | 0.867 (45) | 0.853 (395) [0.839, 0.870] | 0.838 (1583) [0.823, 0.852] | 0.840 (1785) [0.825, 0.854] | 0.862 (174) [0.832, 0.889] | 0.667 (12) | 0.187 | flat +0.019 (noise 0.027) |
| reversal_k8_next | 0.365 (74) | 0.400 (468) [0.365, 0.433] | 0.401 (2030) [0.383, 0.421] | 0.397 (2344) [0.381, 0.415] | 0.408 (238) [0.369, 0.442] | 0.360 (25) | 0.122 | flat -0.009 (noise 0.034) |
| reversal_k8_now | 0.770 (61) | 0.740 (358) [0.711, 0.764] | 0.724 (1569) [0.705, 0.743] | 0.720 (1758) [0.701, 0.739] | 0.778 (171) [0.773, 0.782] | 0.526 (19) | 0.122 | flat -0.015 (noise 0.033) |
| overall | 0.512 (22002) | 0.505 (154621) [0.502, 0.509] | 0.503 (661159) [0.502, 0.505] | 0.503 (749189) [0.502, 0.504] | 0.507 (65908) [0.502, 0.512] | 0.498 (6007) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07679, 0.1146] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.535, 'levels': [{'threshold': 0.07679, 'calls_per_day': 146.9, 'win_rate': 0.5931}, {'threshold': 0.1146, 'calls_per_day': 36.3, 'win_rate': 0.6445}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 3509, 'rate': 0.5523}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15012 | 0.332 | 0.513 (14776) | 0.625 (458) | 0.784 (2408) |
| volatility: normal | 15011 | 0.359 | 0.509 (14945) | 0.700 (30) | 0.774 (2113) |
| volatility: wild | 15011 | 0.373 | 0.494 (14967) | - | 0.778 (2091) |
| session: Asia 00-08 | 15274 | 0.351 | 0.505 (15162) | 0.624 (186) | 0.780 (2213) |
| session: Europe 08-13 | 9300 | 0.347 | 0.503 (9229) | 0.557 (79) | 0.773 (1416) |
| session: US 13-21 | 14880 | 0.364 | 0.506 (14776) | 0.655 (142) | 0.786 (2208) |
| session: late 21-24 | 5580 | 0.351 | 0.507 (5521) | 0.678 (87) | 0.764 (775) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.355 | 0.381 | 0.326 | 0.326 | 0.567 | 0.246 | 0.465 | 1.359 |
| 6h | 360 | 0.369 | 0.357 | 0.276 | 0.296 | 0.552 | 0.289 | 0.450 | 1.106 |
| 24h | 1440 | 0.370 | 0.362 | 0.278 | 0.305 | 0.550 | 0.272 | 0.467 | 1.115 |
| 7d | 10080 | 0.353 | 0.351 | 0.276 | 0.301 | 0.520 | 0.246 | 0.460 | 1.317 |
| 30d | 43200 | 0.356 | 0.355 | 0.278 | 0.308 | 0.505 | 0.247 | 0.465 | 1.284 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.355 / 0.567 / 0.917; 2: 0.331 / 0.417 / 0.967; 3: 0.341 / 0.600 / 0.883; 4: 0.330 / 0.450 / 0.917; 5: 0.309 / 0.500 / 0.900; 6: 0.320 / 0.517 / 0.900; 7: 0.326 / 0.500 / 0.867; 8: 0.290 / 0.400 / 0.900; 9: 0.312 / 0.433 / 0.867; 10: 0.336 / 0.567 / 0.783; 11: 0.331 / 0.583 / 0.817; 12: 0.329 / 0.467 / 0.800; 13: 0.355 / 0.600 / 0.817; 14: 0.307 / 0.383 / 0.800; 15: 0.318 / 0.517 / 0.783
- 6h: 1: 0.369 / 0.552 / 0.911; 2: 0.347 / 0.471 / 0.953; 3: 0.353 / 0.510 / 0.878; 4: 0.347 / 0.487 / 0.944; 5: 0.341 / 0.518 / 0.925; 6: 0.336 / 0.501 / 0.933; 7: 0.337 / 0.496 / 0.864; 8: 0.318 / 0.426 / 0.978; 9: 0.335 / 0.479 / 0.964; 10: 0.344 / 0.515 / 0.803; 11: 0.336 / 0.510 / 0.942; 12: 0.345 / 0.490 / 0.897; 13: 0.367 / 0.571 / 0.950; 14: 0.338 / 0.468 / 0.953; 15: 0.343 / 0.482 / 0.922
- 24h: 1: 0.370 / 0.550 / 0.912; 2: 0.358 / 0.512 / 0.908; 3: 0.356 / 0.511 / 0.903; 4: 0.355 / 0.504 / 0.911; 5: 0.350 / 0.510 / 0.907; 6: 0.346 / 0.489 / 0.908; 7: 0.355 / 0.525 / 0.896; 8: 0.344 / 0.471 / 0.906; 9: 0.350 / 0.508 / 0.910; 10: 0.347 / 0.496 / 0.883; 11: 0.342 / 0.492 / 0.906; 12: 0.347 / 0.495 / 0.895; 13: 0.357 / 0.525 / 0.901; 14: 0.345 / 0.483 / 0.899; 15: 0.351 / 0.504 / 0.898
- 7d: 1: 0.353 / 0.520 / 0.899; 2: 0.347 / 0.500 / 0.901; 3: 0.348 / 0.511 / 0.901; 4: 0.346 / 0.503 / 0.902; 5: 0.343 / 0.502 / 0.902; 6: 0.343 / 0.496 / 0.902; 7: 0.345 / 0.509 / 0.900; 8: 0.342 / 0.496 / 0.901; 9: 0.340 / 0.494 / 0.902; 10: 0.342 / 0.505 / 0.899; 11: 0.342 / 0.505 / 0.901; 12: 0.343 / 0.513 / 0.900; 13: 0.343 / 0.507 / 0.900; 14: 0.340 / 0.493 / 0.901; 15: 0.340 / 0.497 / 0.901
- 30d: 1: 0.356 / 0.505 / 0.899; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.504 / 0.900; 7: 0.349 / 0.506 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.499 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.347 / 0.503 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.344 / 0.494 / 0.900; 15: 0.345 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.112 (body 0.068, range 0.156); 'price stays where it was' would score 0.105; colour right 0.483; typical miss of the close 6.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.120 (body 0.084, range 0.155); 'price stays where it was' would score 0.137; colour right 0.527; typical miss of the close 5.4 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.120 (body 0.086, range 0.154); 'price stays where it was' would score 0.125; colour right 0.529; typical miss of the close 6.4 bp; chain ended on the right side 0.474 of 95 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.157); 'price stays where it was' would score 0.120; colour right 0.497; typical miss of the close 6.5 bp; chain ended on the right side 0.508 of 669 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 8.1 bp; chain ended on the right side 0.507 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.2; 2: 0.199 / 4.4; 3: 0.169 / 6.1; 4: 0.133 / 6.5; 5: 0.123 / 7.3; 6: 0.112 / 8.2; 7: 0.099 / 8.5; 8: 0.091 / 9.0; 9: 0.087 / 9.2; 10: 0.082 / 10.1; 11: 0.075 / 10.6; 12: 0.074 / 11.0; 13: 0.065 / 11.3; 14: 0.066 / 11.4; 15: 0.062 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 92308, probability skill vs chance 0.2356, widened contest next: False
  - now: threshold 0.8428, hit rate recent 0.9224 / long run 0.9385
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.277, naive rule 0.458, lift 3.05x
    - 24h: 50 calls (50 a day), hit rate 0.940, chance 0.305, naive rule 0.508, lift 3.09x
    - 7d: 416 calls (59 a day), hit rate 0.938, chance 0.292, naive rule 0.490, lift 3.21x
    - 30d: 1710 calls (57 a day), hit rate 0.941, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5702, hit rate recent 0.6265 / long run 0.5852
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.277, lift 2.00x
    - 24h: 45 calls (45 a day), hit rate 0.667, chance 0.305, lift 2.19x
    - 7d: 636 calls (91 a day), hit rate 0.586, chance 0.292, lift 2.01x
    - 30d: 2448 calls (82 a day), hit rate 0.585, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.495; 0.35: 538, 0.518; 0.40: 487, 0.561; 0.45: 421, 0.627; 0.50: 368, 0.681; 0.55: 322, 0.725; 0.60: 275, 0.767; 0.65: 225, 0.803; 0.70: 182, 0.835; 0.75: 140, 0.870; 0.80: 98, 0.909; 0.85: 49, 0.949; 0.90: 2, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.425; 0.35: 497, 0.460; 0.40: 413, 0.489; 0.45: 316, 0.519; 0.50: 207, 0.553; 0.55: 93, 0.588; 0.60: 13, 0.621; 0.65: 0, 0.750
- **K=5**: model 1790208000, labels learned 92306, probability skill vs chance 0.2173, widened contest next: False
  - now: threshold 0.7138, hit rate recent 0.8321 / long run 0.8429
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.187, naive rule 0.374, lift 3.82x
    - 24h: 44 calls (44 a day), hit rate 0.841, chance 0.206, naive rule 0.433, lift 4.08x
    - 7d: 389 calls (56 a day), hit rate 0.853, chance 0.191, naive rule 0.403, lift 4.46x
    - 30d: 1581 calls (53 a day), hit rate 0.839, chance 0.186, naive rule 0.390, lift 4.50x
  - next: threshold 0.4562, hit rate recent 0.4809 / long run 0.4741
    - 6h: 11 calls (45 a day), hit rate 0.273, chance 0.187, lift 1.46x
    - 24h: 43 calls (43 a day), hit rate 0.512, chance 0.206, lift 2.48x
    - 7d: 719 calls (103 a day), hit rate 0.463, chance 0.191, lift 2.42x
    - 30d: 2114 calls (70 a day), hit rate 0.487, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 432, 0.411; 0.35: 371, 0.464; 0.40: 300, 0.532; 0.45: 246, 0.590; 0.50: 191, 0.649; 0.55: 146, 0.699; 0.60: 114, 0.739; 0.65: 87, 0.784; 0.70: 64, 0.821; 0.75: 35, 0.863; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 254, 0.422; 0.40: 167, 0.449; 0.45: 87, 0.472; 0.50: 22, 0.519; 0.55: 2, 0.592
- **K=8**: model 1791158400, labels learned 92303, probability skill vs chance 0.195, widened contest next: False
  - now: threshold 0.5628, hit rate recent 0.7146 / long run 0.7305
    - 6h: 15 calls (62 a day), hit rate 0.533, chance 0.111, naive rule 0.295, lift 4.79x
    - 24h: 64 calls (64 a day), hit rate 0.734, chance 0.130, naive rule 0.358, lift 5.63x
    - 7d: 357 calls (51 a day), hit rate 0.737, chance 0.126, naive rule 0.340, lift 5.84x
    - 30d: 1574 calls (52 a day), hit rate 0.723, chance 0.121, naive rule 0.325, lift 5.97x
  - next: threshold 0.3485, hit rate recent 0.3927 / long run 0.4051
    - 6h: 23 calls (95 a day), hit rate 0.304, chance 0.111, lift 2.73x
    - 24h: 80 calls (81 a day), hit rate 0.400, chance 0.130, lift 3.07x
    - 7d: 476 calls (68 a day), hit rate 0.401, chance 0.126, lift 3.18x
    - 30d: 2036 calls (68 a day), hit rate 0.401, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 275, 0.398; 0.35: 207, 0.474; 0.40: 160, 0.537; 0.45: 126, 0.584; 0.50: 97, 0.626; 0.55: 69, 0.681; 0.60: 46, 0.729; 0.65: 24, 0.769; 0.70: 9, 0.807; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 188, 0.344; 0.35: 117, 0.383; 0.40: 48, 0.408; 0.45: 10, 0.425; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 92298, probability skill vs chance 0.1726, widened contest next: True
  - now: threshold 0.419, hit rate recent 0.5223 / long run 0.5847
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.065, naive rule 0.206, lift 5.11x
    - 24h: 67 calls (68 a day), hit rate 0.522, chance 0.077, naive rule 0.286, lift 6.77x
    - 7d: 381 calls (55 a day), hit rate 0.585, chance 0.078, naive rule 0.273, lift 7.48x
    - 30d: 1474 calls (49 a day), hit rate 0.585, chance 0.077, naive rule 0.266, lift 7.63x
  - next: threshold 0.2771, hit rate recent 0.2862 / long run 0.3008
    - 6h: 16 calls (67 a day), hit rate 0.188, chance 0.065, lift 2.88x
    - 24h: 61 calls (62 a day), hit rate 0.279, chance 0.077, lift 3.61x
    - 7d: 609 calls (87 a day), hit rate 0.294, chance 0.078, lift 3.76x
    - 30d: 2023 calls (67 a day), hit rate 0.306, chance 0.077, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.435; 0.35: 90, 0.491; 0.40: 65, 0.540; 0.45: 45, 0.600; 0.50: 28, 0.622; 0.55: 16, 0.673; 0.60: 7, 0.701; 0.65: 2, 0.768; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.312; 0.35: 17, 0.352; 0.40: 4, 0.333; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.390 | 5.59% | 0.917 | 0.567 | 0.249 | 0.567 | 0.547 |
| 6h | 7.804 | 3.22% | 0.908 | 0.494 | 0.250 | 0.496 | 0.388 |
| 24h | 10.270 | 5.12% | 0.912 | 0.502 | 0.251 | 0.498 | 0.621 |
| 7d | 11.350 | 4.56% | 0.902 | 0.500 | 0.251 | 0.496 | 0.693 |
| 30d | 14.153 | 4.17% | 0.900 | 0.500 | 0.251 | 0.498 | 0.693 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.769 | 6.428 | 6.416 | 6.449 | 6.478 | 6.472 | 6.394 | 6.499 | 6.417 | 6.390 |
| 6h | 8.064 | 7.884 | 7.867 | 7.835 | 7.994 | 7.882 | 7.779 | 7.786 | 7.789 | 7.804 |
| 24h | 10.824 | 10.360 | 10.356 | 10.355 | 10.504 | 10.436 | 10.240 | 10.253 | 10.248 | 10.270 |
| 7d | 11.892 | 11.443 | 11.436 | 11.378 | 11.590 | 11.538 | 11.343 | 11.337 | 11.330 | 11.350 |
| 30d | 14.769 | 14.283 | 14.238 | 14.180 | 14.424 | 14.368 | 14.155 | 14.127 | 14.126 | 14.153 |

## Next candle

- candle starting 2026-10-06 06:34 UTC, last close 2694.4
- P(up) 0.4755, return quantiles (bp): {'05': -4.291, '10': -3.19, '25': -1.839, '40': -0.707, '50': -0.143, '60': 0.453, '75': 1.409, '90': 3.038, '95': 4.348}
- changepoint probability 0.0653, regime age 112.8 min
- agent weights: empirical 0.003, ewma 0.096, garch 0.106, har 0.108, bocpd 0.025, hmm 0.053, online_qr 0.327, lgbm 0.283

## Learning log

- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.76, 4.58, 12.58], current probabilities: [0.617, 0.378, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-10-06 06:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.294, 'l_abs': 0.605, 'l_hi': 0.776, 'l_lo': 0.761, 'b05': 0.718, 'b25': 0.597, 'b75': 0.675, 'b95': 0.682}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.234, 1.708, 1.684, 2.044, 2.243, 3.025, 2.601, 2.764, 5.009, 3.13, 3.844, 3.555, 3.848, 3.991]}
- calibration offsets (in sigma): {'05': 0.0365, '10': -0.007, '25': -0.0775, '40': -0.038, '50': -0.045, '60': -0.042, '75': -0.0625, '90': -0.053, '95': -0.0265}
