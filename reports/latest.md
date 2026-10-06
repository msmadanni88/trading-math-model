# ETH-USD 60s candle generator - report

- generated: 2026-10-06 13:35 UTC
- last closed candle: 2026-10-06 13:35 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.432 (95) | 0.508 (669) [0.470, 0.551] | 0.506 (2875) [0.488, 0.526] | 0.513 (3259) [0.495, 0.531] | 0.533 (287) [0.465, 0.601] | 0.537 (54) | 0.500 | flat -0.030 (noise 0.033) |
| colour_clear | 0.563 (766) | 0.515 (5282) [0.493, 0.538] | 0.503 (23277) [0.496, 0.510] | 0.501 (26399) [0.495, 0.507] | 0.556 (2161) [0.550, 0.561] | 0.556 (441) | 0.500 | flat +0.018 (noise 0.014) |
| colour_confident | 0.718 (103) | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.505 (101) | 0.500 | - |
| colour_next | 0.552 (1430) | 0.518 (9994) [0.504, 0.532] | 0.504 (42889) [0.499, 0.510] | 0.504 (48600) [0.499, 0.509] | 0.541 (4251) [0.530, 0.551] | 0.529 (807) | 0.500 | flat +0.019 (noise 0.010) |
| colour_path | 0.508 (20020) | 0.502 (139916) [0.499, 0.506] | 0.501 (600446) [0.500, 0.503] | 0.501 (680400) [0.500, 0.502] | 0.502 (59514) [0.497, 0.507] | 0.494 (11298) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.800 (15) | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.593 (27) | 0.500 | - |
| reversal_k13_next | 0.288 (73) | 0.291 (635) [0.267, 0.316] | 0.308 (2020) [0.293, 0.324] | 0.303 (2366) [0.288, 0.318] | 0.326 (261) [0.302, 0.347] | 0.343 (35) | 0.077 | flat -0.009 (noise 0.029) |
| reversal_k13_now | 0.559 (68) | 0.581 (387) [0.535, 0.631] | 0.587 (1468) [0.564, 0.610] | 0.586 (1650) [0.566, 0.606] | 0.624 (178) [0.572, 0.690] | 0.457 (35) | 0.077 | flat -0.030 (noise 0.037) |
| reversal_k3_next | 0.653 (49) | 0.590 (656) [0.564, 0.621] | 0.584 (2457) [0.569, 0.599] | 0.586 (2757) [0.573, 0.601] | 0.577 (317) [0.552, 0.622] | 0.647 (17) | 0.292 | flat +0.039 (noise 0.029) |
| reversal_k3_now | 0.958 (48) | 0.940 (417) [0.930, 0.952] | 0.941 (1702) [0.933, 0.950] | 0.941 (1932) [0.933, 0.949] | 0.935 (169) [0.924, 0.948] | 0.833 (36) | 0.292 | flat +0.004 (noise 0.017) |
| reversal_k5_next | 0.538 (39) | 0.466 (726) [0.435, 0.498] | 0.486 (2120) [0.466, 0.506] | 0.487 (2338) [0.470, 0.505] | 0.448 (348) [0.420, 0.505] | 0.478 (23) | 0.187 | flat -0.042 (noise 0.036) |
| reversal_k5_now | 0.867 (45) | 0.853 (395) [0.839, 0.870] | 0.838 (1583) [0.823, 0.852] | 0.840 (1785) [0.825, 0.854] | 0.862 (174) [0.832, 0.889] | 0.667 (30) | 0.187 | flat +0.019 (noise 0.027) |
| reversal_k8_next | 0.365 (74) | 0.400 (468) [0.365, 0.433] | 0.401 (2030) [0.383, 0.421] | 0.397 (2344) [0.381, 0.415] | 0.408 (238) [0.369, 0.442] | 0.438 (48) | 0.122 | flat -0.009 (noise 0.034) |
| reversal_k8_now | 0.770 (61) | 0.740 (358) [0.711, 0.764] | 0.724 (1569) [0.705, 0.743] | 0.720 (1758) [0.701, 0.739] | 0.778 (171) [0.773, 0.782] | 0.622 (37) | 0.122 | flat -0.015 (noise 0.033) |
| overall | 0.512 (22002) | 0.505 (154621) [0.502, 0.509] | 0.503 (661159) [0.502, 0.505] | 0.503 (749189) [0.502, 0.504] | 0.507 (65908) [0.502, 0.512] | 0.498 (12420) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07744, 0.1154] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5348, 'levels': [{'threshold': 0.07744, 'calls_per_day': 146.7, 'win_rate': 0.5888}, {'threshold': 0.1154, 'calls_per_day': 37.2, 'win_rate': 0.6464}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 3926, 'rate': 0.5474}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15152 | 0.332 | 0.513 (14913) | 0.608 (502) | 0.782 (2435) |
| volatility: normal | 15151 | 0.359 | 0.509 (15085) | 0.686 (35) | 0.773 (2144) |
| volatility: wild | 15152 | 0.373 | 0.494 (15107) | - | 0.778 (2103) |
| session: Asia 00-08 | 15360 | 0.351 | 0.505 (15248) | 0.604 (207) | 0.780 (2230) |
| session: Europe 08-13 | 9600 | 0.347 | 0.503 (9525) | 0.549 (111) | 0.770 (1465) |
| session: US 13-21 | 14915 | 0.364 | 0.506 (14811) | 0.650 (143) | 0.786 (2212) |
| session: late 21-24 | 5580 | 0.351 | 0.507 (5521) | 0.678 (87) | 0.764 (775) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.373 | 0.343 | 0.294 | 0.294 | 0.533 | 0.267 | 0.479 | 0.911 |
| 6h | 360 | 0.346 | 0.339 | 0.277 | 0.313 | 0.489 | 0.237 | 0.455 | 1.268 |
| 24h | 1440 | 0.367 | 0.356 | 0.283 | 0.307 | 0.539 | 0.269 | 0.465 | 1.163 |
| 7d | 10080 | 0.352 | 0.349 | 0.276 | 0.300 | 0.519 | 0.246 | 0.459 | 1.297 |
| 30d | 43200 | 0.356 | 0.355 | 0.278 | 0.308 | 0.506 | 0.247 | 0.465 | 1.285 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.373 / 0.533 / 0.917; 2: 0.390 / 0.567 / 0.867; 3: 0.343 / 0.417 / 0.833; 4: 0.355 / 0.533 / 0.833; 5: 0.382 / 0.533 / 0.817; 6: 0.343 / 0.483 / 0.850; 7: 0.361 / 0.550 / 0.933; 8: 0.353 / 0.550 / 0.900; 9: 0.314 / 0.417 / 0.917; 10: 0.360 / 0.567 / 1.000; 11: 0.370 / 0.517 / 0.917; 12: 0.343 / 0.417 / 0.967; 13: 0.349 / 0.433 / 0.933; 14: 0.344 / 0.467 / 0.933; 15: 0.342 / 0.517 / 0.967
- 6h: 1: 0.346 / 0.489 / 0.919; 2: 0.349 / 0.537 / 0.883; 3: 0.329 / 0.447 / 0.906; 4: 0.341 / 0.528 / 0.881; 5: 0.343 / 0.489 / 0.883; 6: 0.339 / 0.514 / 0.867; 7: 0.335 / 0.489 / 0.931; 8: 0.342 / 0.508 / 0.897; 9: 0.327 / 0.469 / 0.900; 10: 0.341 / 0.508 / 0.950; 11: 0.347 / 0.511 / 0.892; 12: 0.342 / 0.492 / 0.922; 13: 0.339 / 0.520 / 0.892; 14: 0.333 / 0.472 / 0.897; 15: 0.338 / 0.528 / 0.897
- 24h: 1: 0.367 / 0.539 / 0.913; 2: 0.356 / 0.513 / 0.899; 3: 0.350 / 0.495 / 0.902; 4: 0.352 / 0.508 / 0.900; 5: 0.348 / 0.498 / 0.897; 6: 0.342 / 0.497 / 0.892; 7: 0.348 / 0.505 / 0.901; 8: 0.342 / 0.485 / 0.899; 9: 0.343 / 0.494 / 0.904; 10: 0.344 / 0.501 / 0.896; 11: 0.343 / 0.495 / 0.901; 12: 0.345 / 0.482 / 0.902; 13: 0.354 / 0.523 / 0.900; 14: 0.342 / 0.474 / 0.897; 15: 0.348 / 0.510 / 0.899
- 7d: 1: 0.352 / 0.519 / 0.899; 2: 0.347 / 0.503 / 0.900; 3: 0.347 / 0.509 / 0.901; 4: 0.344 / 0.504 / 0.901; 5: 0.343 / 0.503 / 0.901; 6: 0.341 / 0.496 / 0.900; 7: 0.343 / 0.507 / 0.901; 8: 0.341 / 0.497 / 0.901; 9: 0.338 / 0.492 / 0.902; 10: 0.340 / 0.503 / 0.900; 11: 0.341 / 0.506 / 0.901; 12: 0.342 / 0.511 / 0.900; 13: 0.342 / 0.507 / 0.900; 14: 0.338 / 0.492 / 0.900; 15: 0.339 / 0.496 / 0.900
- 30d: 1: 0.356 / 0.506 / 0.899; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.346 / 0.499 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.347 / 0.502 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.344 / 0.494 / 0.900; 15: 0.345 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.097 (body 0.063, range 0.132); 'price stays where it was' would score 0.158; colour right 0.467; typical miss of the close 7.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.110 (body 0.073, range 0.147); 'price stays where it was' would score 0.126; colour right 0.469; typical miss of the close 6.2 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.115 (body 0.080, range 0.150); 'price stays where it was' would score 0.123; colour right 0.512; typical miss of the close 5.9 bp; chain ended on the right side 0.505 of 95 chains; n=1440
- 7d: match 0.117 (body 0.077, range 0.156); 'price stays where it was' would score 0.121; colour right 0.497; typical miss of the close 6.3 bp; chain ended on the right side 0.518 of 670 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 8.1 bp; chain ended on the right side 0.509 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.2; 2: 0.198 / 4.4; 3: 0.168 / 6.1; 4: 0.133 / 6.5; 5: 0.123 / 7.4; 6: 0.112 / 8.2; 7: 0.099 / 8.6; 8: 0.091 / 9.0; 9: 0.086 / 9.2; 10: 0.081 / 10.1; 11: 0.075 / 10.7; 12: 0.073 / 11.0; 13: 0.065 / 11.3; 14: 0.066 / 11.5; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 92729, probability skill vs chance 0.2313, widened contest next: True
  - now: threshold 0.8429, hit rate recent 0.8853 / long run 0.9337
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.330, naive rule 0.523, lift 2.48x
    - 24h: 53 calls (53 a day), hit rate 0.868, chance 0.308, naive rule 0.505, lift 2.81x
    - 7d: 416 calls (59 a day), hit rate 0.930, chance 0.294, naive rule 0.491, lift 3.16x
    - 30d: 1702 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.482, lift 3.21x
  - next: threshold 0.5655, hit rate recent 0.637 / long run 0.5867
    - 6h: 7 calls (28 a day), hit rate 0.714, chance 0.330, lift 2.17x
    - 24h: 36 calls (36 a day), hit rate 0.639, chance 0.308, lift 2.07x
    - 7d: 616 calls (88 a day), hit rate 0.584, chance 0.294, lift 1.99x
    - 30d: 2423 calls (81 a day), hit rate 0.585, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.495; 0.35: 538, 0.518; 0.40: 487, 0.562; 0.45: 421, 0.627; 0.50: 368, 0.681; 0.55: 322, 0.724; 0.60: 275, 0.767; 0.65: 225, 0.803; 0.70: 182, 0.834; 0.75: 139, 0.870; 0.80: 98, 0.908; 0.85: 49, 0.947; 0.90: 2, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.425; 0.35: 497, 0.460; 0.40: 413, 0.489; 0.45: 316, 0.520; 0.50: 207, 0.553; 0.55: 93, 0.587; 0.60: 13, 0.622; 0.65: 0, 0.750
- **K=5**: model 1790208000, labels learned 92727, probability skill vs chance 0.2165, widened contest next: True
  - now: threshold 0.714, hit rate recent 0.7899 / long run 0.8377
    - 6h: 15 calls (61 a day), hit rate 0.667, chance 0.205, naive rule 0.431, lift 3.25x
    - 24h: 49 calls (49 a day), hit rate 0.755, chance 0.203, naive rule 0.425, lift 3.72x
    - 7d: 392 calls (56 a day), hit rate 0.847, chance 0.192, naive rule 0.405, lift 4.40x
    - 30d: 1580 calls (53 a day), hit rate 0.836, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4559, hit rate recent 0.51 / long run 0.4771
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.205, lift 3.10x
    - 24h: 38 calls (38 a day), hit rate 0.500, chance 0.203, lift 2.46x
    - 7d: 719 calls (103 a day), hit rate 0.462, chance 0.192, lift 2.40x
    - 30d: 2112 calls (70 a day), hit rate 0.488, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 431, 0.411; 0.35: 370, 0.464; 0.40: 299, 0.533; 0.45: 245, 0.591; 0.50: 190, 0.650; 0.55: 145, 0.699; 0.60: 114, 0.739; 0.65: 87, 0.784; 0.70: 64, 0.820; 0.75: 34, 0.861; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 254, 0.423; 0.40: 166, 0.450; 0.45: 86, 0.474; 0.50: 21, 0.520; 0.55: 2, 0.587
- **K=8**: model 1791158400, labels learned 92724, probability skill vs chance 0.1973, widened contest next: False
  - now: threshold 0.5632, hit rate recent 0.7169 / long run 0.7303
    - 6h: 15 calls (62 a day), hit rate 0.733, chance 0.137, naive rule 0.389, lift 5.35x
    - 24h: 60 calls (60 a day), hit rate 0.733, chance 0.131, naive rule 0.361, lift 5.59x
    - 7d: 361 calls (52 a day), hit rate 0.737, chance 0.127, naive rule 0.342, lift 5.82x
    - 30d: 1575 calls (53 a day), hit rate 0.722, chance 0.121, naive rule 0.325, lift 5.97x
  - next: threshold 0.3476, hit rate recent 0.4381 / long run 0.4096
    - 6h: 20 calls (82 a day), hit rate 0.500, chance 0.137, lift 3.65x
    - 24h: 73 calls (74 a day), hit rate 0.452, chance 0.131, lift 3.45x
    - 7d: 480 calls (69 a day), hit rate 0.404, chance 0.127, lift 3.19x
    - 30d: 2042 calls (68 a day), hit rate 0.403, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 274, 0.398; 0.35: 207, 0.474; 0.40: 160, 0.535; 0.45: 126, 0.582; 0.50: 97, 0.626; 0.55: 69, 0.680; 0.60: 46, 0.726; 0.65: 24, 0.767; 0.70: 9, 0.801; 0.75: 1, 0.800
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 187, 0.344; 0.35: 117, 0.384; 0.40: 48, 0.412; 0.45: 10, 0.428; 0.50: 1, 0.425
- **K=13**: model 1791072000, labels learned 92719, probability skill vs chance 0.1793, widened contest next: True
  - now: threshold 0.4193, hit rate recent 0.5361 / long run 0.5848
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.074, naive rule 0.286, lift 7.73x
    - 24h: 60 calls (61 a day), hit rate 0.517, chance 0.074, naive rule 0.270, lift 7.01x
    - 7d: 381 calls (55 a day), hit rate 0.591, chance 0.079, naive rule 0.275, lift 7.51x
    - 30d: 1479 calls (49 a day), hit rate 0.584, chance 0.077, naive rule 0.266, lift 7.62x
  - next: threshold 0.2775, hit rate recent 0.3418 / long run 0.3062
    - 6h: 16 calls (67 a day), hit rate 0.500, chance 0.074, lift 6.76x
    - 24h: 61 calls (62 a day), hit rate 0.344, chance 0.074, lift 4.67x
    - 7d: 603 calls (86 a day), hit rate 0.300, chance 0.079, lift 3.82x
    - 30d: 2035 calls (68 a day), hit rate 0.308, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.435; 0.35: 90, 0.492; 0.40: 65, 0.541; 0.45: 45, 0.598; 0.50: 28, 0.617; 0.55: 15, 0.669; 0.60: 6, 0.700; 0.65: 2, 0.764; 0.70: 0, 0.600
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.313; 0.35: 17, 0.353; 0.40: 4, 0.333; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.366 | 2.08% | 0.883 | 0.417 | 0.252 | 0.433 | 0.357 |
| 6h | 10.696 | 1.32% | 0.919 | 0.514 | 0.252 | 0.452 | 0.326 |
| 24h | 9.677 | 5.18% | 0.912 | 0.506 | 0.251 | 0.491 | 0.593 |
| 7d | 11.146 | 4.61% | 0.902 | 0.500 | 0.251 | 0.494 | 0.688 |
| 30d | 14.159 | 4.18% | 0.900 | 0.500 | 0.251 | 0.498 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.607 | 11.483 | 11.460 | 11.172 | 11.597 | 11.573 | 11.357 | 11.360 | 11.315 | 11.366 |
| 6h | 10.839 | 10.856 | 10.766 | 10.661 | 10.927 | 10.790 | 10.761 | 10.723 | 10.696 | 10.696 |
| 24h | 10.206 | 9.799 | 9.747 | 9.739 | 9.883 | 9.807 | 9.676 | 9.672 | 9.665 | 9.677 |
| 7d | 11.685 | 11.238 | 11.231 | 11.177 | 11.382 | 11.335 | 11.141 | 11.134 | 11.127 | 11.146 |
| 30d | 14.776 | 14.289 | 14.244 | 14.186 | 14.430 | 14.374 | 14.161 | 14.133 | 14.132 | 14.159 |

## Next candle

- candle starting 2026-10-06 13:35 UTC, last close 2717.73
- P(up) 0.49, return quantiles (bp): {'05': -9.528, '10': -7.112, '25': -3.681, '40': -1.176, '50': -0.106, '60': 0.973, '75': 3.247, '90': 7.327, '95': 10.354}
- changepoint probability 0.171, regime age 65.0 min
- agent weights: empirical 0.009, ewma 0.063, garch 0.117, har 0.271, bocpd 0.022, hmm 0.061, online_qr 0.215, lgbm 0.242

## Learning log

- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- HMM volatility states (sd, bp per minute): [1.78, 4.45, 12.43], current probabilities: [0.0, 0.788, 0.212]
- live generator: {'versions': 60, 'latest_effective': '2026-10-06 13:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.291, 'l_abs': 0.663, 'l_hi': 0.759, 'l_lo': 0.769, 'b05': 0.712, 'b25': 0.686, 'b75': 0.713, 'b95': 0.703}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8]], 'cone_width': [1.335, 1.671, 1.895, 2.254, 2.627, 2.282, 2.396, 2.446, 3.419, 2.942, 2.899, 3.342, 3.475, 3.604]}
- calibration offsets (in sigma): {'05': 0.107, '10': 0.074, '25': 0.005, '40': 0.036, '50': 0.0, '60': -0.026, '75': -0.045, '90': -0.004, '95': -0.007}
