# ETH-USD 60s candle generator - report

- generated: 2026-11-13 02:43 UTC
- last closed candle: 2026-11-13 02:43 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.526 (95) | 0.528 (671) [0.495, 0.559] | 0.520 (2879) [0.503, 0.537] | 0.514 (6905) [0.502, 0.527] | 0.516 (3933) [0.501, 0.533] | 0.600 (10) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.536 (785) | 0.547 (5507) [0.534, 0.559] | 0.543 (23916) [0.537, 0.549] | 0.523 (56554) [0.517, 0.528] | 0.542 (32316) [0.538, 0.547] | 0.608 (102) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.573 (75) | 0.569 (934) [0.537, 0.594] | 0.586 (4284) [0.576, 0.596] | 0.591 (5825) [0.581, 0.602] | 0.591 (5825) [0.581, 0.602] | 0.750 (4) | 0.500 | flat -0.003 (noise 0.023) |
| colour_next | 0.532 (1435) | 0.533 (9973) [0.522, 0.545] | 0.530 (42871) [0.526, 0.534] | 0.517 (102868) [0.513, 0.521] | 0.529 (58519) [0.526, 0.533] | 0.601 (163) | 0.500 | flat +0.007 (noise 0.009) |
| colour_path | 0.503 (20090) | 0.502 (139622) [0.499, 0.504] | 0.502 (600194) [0.500, 0.503] | 0.501 (1440152) [0.500, 0.502] | 0.501 (819266) [0.500, 0.502] | 0.496 (2282) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.455 (11) | 0.622 (241) [0.569, 0.645] | 0.618 (1105) [0.601, 0.635] | 0.629 (1524) [0.612, 0.646] | 0.629 (1524) [0.612, 0.646] | 0.667 (3) | 0.500 | flat +0.010 (noise 0.047) |
| reversal_k13_next | 0.344 (64) | 0.335 (498) [0.313, 0.359] | 0.329 (1828) [0.315, 0.344] | 0.315 (4760) [0.305, 0.325] | 0.327 (2655) [0.316, 0.338] | 0.500 (2) | 0.077 | flat -0.025 (noise 0.033) |
| reversal_k13_now | 0.571 (42) | 0.579 (337) [0.552, 0.608] | 0.561 (1634) [0.542, 0.579] | 0.574 (3700) [0.561, 0.586] | 0.569 (2228) [0.552, 0.585] | 0.667 (6) | 0.077 | flat -0.002 (noise 0.036) |
| reversal_k3_next | 0.576 (59) | 0.609 (358) [0.580, 0.639] | 0.594 (2695) [0.582, 0.606] | 0.588 (6161) [0.580, 0.597] | 0.589 (3721) [0.578, 0.600] | 0.500 (4) | 0.293 | flat +0.000 (noise 0.032) |
| reversal_k3_now | 0.906 (64) | 0.918 (417) [0.909, 0.929] | 0.931 (1736) [0.921, 0.941] | 0.935 (4146) [0.929, 0.941] | 0.929 (2383) [0.922, 0.938] | 1.000 (8) | 0.294 | flat +0.004 (noise 0.019) |
| reversal_k5_next | 0.460 (74) | 0.499 (411) [0.463, 0.532] | 0.486 (2620) [0.471, 0.503] | 0.485 (5531) [0.474, 0.496] | 0.479 (3541) [0.465, 0.494] | 0.200 (5) | 0.187 | flat -0.044 (noise 0.035) |
| reversal_k5_now | 0.737 (57) | 0.761 (397) [0.712, 0.804] | 0.805 (1654) [0.789, 0.820] | 0.821 (3862) [0.811, 0.831] | 0.809 (2251) [0.796, 0.822] | 0.700 (10) | 0.187 | flat -0.047 (noise 0.030) |
| reversal_k8_next | 0.455 (66) | 0.419 (468) [0.392, 0.445] | 0.398 (2598) [0.384, 0.413] | 0.397 (5638) [0.386, 0.407] | 0.397 (3532) [0.385, 0.409] | 0.333 (3) | 0.121 | flat -0.033 (noise 0.033) |
| reversal_k8_now | 0.622 (45) | 0.683 (366) [0.656, 0.708] | 0.685 (1523) [0.666, 0.703] | 0.699 (3740) [0.686, 0.712] | 0.688 (2153) [0.671, 0.704] | 0.667 (9) | 0.122 | flat -0.007 (noise 0.035) |
| overall | 0.507 (22091) | 0.506 (153518) [0.503, 0.508] | 0.506 (662232) [0.504, 0.507] | 0.504 (1587463) [0.503, 0.505] | 0.505 (904182) [0.504, 0.506] | 0.506 (2502) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07469, 0.1144] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5327, 'levels': [{'threshold': 0.07469, 'calls_per_day': 143.3, 'win_rate': 0.575}, {'threshold': 0.1144, 'calls_per_day': 36.0, 'win_rate': 0.6157}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42870, 'rate': 0.5301}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14935 | 0.346 | 0.533 (14698) | 0.567 (2266) | 0.738 (2509) |
| volatility: normal | 14934 | 0.370 | 0.529 (14872) | 0.610 (1328) | 0.748 (2221) |
| volatility: wild | 14934 | 0.386 | 0.528 (14897) | 0.606 (754) | 0.768 (2029) |
| session: Asia 00-08 | 15043 | 0.367 | 0.535 (14921) | 0.591 (1527) | 0.752 (2235) |
| session: Europe 08-13 | 9300 | 0.361 | 0.532 (9221) | 0.588 (1130) | 0.748 (1513) |
| session: US 13-21 | 14880 | 0.374 | 0.528 (14781) | 0.597 (1145) | 0.753 (2223) |
| session: late 21-24 | 5580 | 0.360 | 0.515 (5544) | 0.553 (546) | 0.741 (788) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.408 | 0.418 | 0.291 | 0.291 | 0.617 | 0.310 | 0.505 | 1.091 |
| 6h | 360 | 0.387 | 0.377 | 0.289 | 0.306 | 0.556 | 0.282 | 0.492 | 1.065 |
| 24h | 1440 | 0.378 | 0.376 | 0.293 | 0.322 | 0.539 | 0.274 | 0.482 | 1.039 |
| 7d | 10080 | 0.369 | 0.365 | 0.281 | 0.311 | 0.534 | 0.268 | 0.471 | 1.343 |
| 30d | 43200 | 0.367 | 0.361 | 0.279 | 0.310 | 0.530 | 0.265 | 0.470 | 1.256 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.408 / 0.617 / 0.850; 2: 0.348 / 0.450 / 0.817; 3: 0.387 / 0.550 / 0.833; 4: 0.347 / 0.450 / 0.967; 5: 0.367 / 0.500 / 0.900; 6: 0.344 / 0.500 / 0.933; 7: 0.358 / 0.533 / 0.817; 8: 0.342 / 0.417 / 0.817; 9: 0.360 / 0.533 / 0.800; 10: 0.341 / 0.450 / 0.833; 11: 0.358 / 0.500 / 0.933; 12: 0.357 / 0.467 / 0.933; 13: 0.333 / 0.450 / 0.900; 14: 0.368 / 0.517 / 0.900; 15: 0.321 / 0.467 / 0.900
- 6h: 1: 0.387 / 0.556 / 0.875; 2: 0.363 / 0.475 / 0.858; 3: 0.364 / 0.486 / 0.875; 4: 0.364 / 0.481 / 0.914; 5: 0.370 / 0.514 / 0.883; 6: 0.365 / 0.500 / 0.892; 7: 0.374 / 0.503 / 0.858; 8: 0.367 / 0.506 / 0.867; 9: 0.367 / 0.511 / 0.839; 10: 0.368 / 0.508 / 0.853; 11: 0.370 / 0.500 / 0.958; 12: 0.360 / 0.486 / 0.964; 13: 0.342 / 0.425 / 0.953; 14: 0.354 / 0.481 / 0.950; 15: 0.349 / 0.456 / 0.950
- 24h: 1: 0.378 / 0.539 / 0.897; 2: 0.352 / 0.467 / 0.893; 3: 0.365 / 0.509 / 0.894; 4: 0.360 / 0.501 / 0.899; 5: 0.363 / 0.496 / 0.895; 6: 0.361 / 0.505 / 0.897; 7: 0.367 / 0.504 / 0.889; 8: 0.367 / 0.520 / 0.891; 9: 0.362 / 0.504 / 0.885; 10: 0.362 / 0.492 / 0.890; 11: 0.365 / 0.511 / 0.902; 12: 0.365 / 0.517 / 0.901; 13: 0.358 / 0.493 / 0.901; 14: 0.364 / 0.514 / 0.901; 15: 0.359 / 0.497 / 0.900
- 7d: 1: 0.369 / 0.534 / 0.896; 2: 0.354 / 0.483 / 0.899; 3: 0.360 / 0.515 / 0.899; 4: 0.354 / 0.495 / 0.900; 5: 0.356 / 0.504 / 0.899; 6: 0.353 / 0.496 / 0.900; 7: 0.354 / 0.499 / 0.898; 8: 0.355 / 0.500 / 0.900; 9: 0.356 / 0.507 / 0.897; 10: 0.355 / 0.502 / 0.897; 11: 0.357 / 0.515 / 0.899; 12: 0.353 / 0.503 / 0.899; 13: 0.353 / 0.498 / 0.899; 14: 0.354 / 0.506 / 0.899; 15: 0.352 / 0.497 / 0.899
- 30d: 1: 0.367 / 0.530 / 0.897; 2: 0.354 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.498 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.501 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.353 / 0.504 / 0.900; 9: 0.353 / 0.504 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.351 / 0.503 / 0.900; 12: 0.352 / 0.503 / 0.901; 13: 0.351 / 0.500 / 0.900; 14: 0.351 / 0.502 / 0.901; 15: 0.351 / 0.502 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.122 (body 0.072, range 0.171); 'price stays where it was' would score 0.138; colour right 0.517; typical miss of the close 16.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.124 (body 0.076, range 0.171); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 10.0 bp; chain ended on the right side 0.609 of 23 chains; n=360
- 24h: match 0.127 (body 0.085, range 0.169); 'price stays where it was' would score 0.132; colour right 0.505; typical miss of the close 10.2 bp; chain ended on the right side 0.547 of 95 chains; n=1440
- 7d: match 0.124 (body 0.083, range 0.165); 'price stays where it was' would score 0.125; colour right 0.503; typical miss of the close 8.5 bp; chain ended on the right side 0.531 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 8.9 bp; chain ended on the right side 0.520 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.202 / 5.5; 3: 0.168 / 7.1; 4: 0.133 / 7.2; 5: 0.127 / 8.0; 6: 0.116 / 8.9; 7: 0.110 / 9.2; 8: 0.098 / 10.1; 9: 0.091 / 10.2; 10: 0.093 / 10.5; 11: 0.089 / 10.8; 12: 0.079 / 11.1; 13: 0.073 / 11.7; 14: 0.069 / 12.2; 15: 0.065 / 12.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 146797, probability skill vs chance 0.2305, widened contest next: False
  - now: threshold 0.8323, hit rate recent 0.9098 / long run 0.9238
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.294, naive rule 0.523, lift 3.21x
    - 24h: 66 calls (66 a day), hit rate 0.909, chance 0.291, naive rule 0.480, lift 3.12x
    - 7d: 415 calls (59 a day), hit rate 0.920, chance 0.296, naive rule 0.503, lift 3.11x
    - 30d: 1741 calls (58 a day), hit rate 0.931, chance 0.294, naive rule 0.496, lift 3.17x
  - next: threshold 0.5673, hit rate recent 0.6107 / long run 0.6067
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.294, lift 2.47x
    - 24h: 55 calls (55 a day), hit rate 0.582, chance 0.291, lift 2.00x
    - 7d: 352 calls (50 a day), hit rate 0.605, chance 0.296, lift 2.05x
    - 30d: 2684 calls (89 a day), hit rate 0.593, chance 0.294, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.579; 0.45: 406, 0.649; 0.50: 357, 0.695; 0.55: 310, 0.740; 0.60: 261, 0.783; 0.65: 220, 0.811; 0.70: 173, 0.843; 0.75: 139, 0.874; 0.80: 92, 0.904; 0.85: 46, 0.943; 0.90: 4, 0.993
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.431; 0.35: 496, 0.465; 0.40: 397, 0.503; 0.45: 298, 0.536; 0.50: 192, 0.568; 0.55: 85, 0.578; 0.60: 11, 0.654; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 146795, probability skill vs chance 0.2122, widened contest next: True
  - now: threshold 0.688, hit rate recent 0.7306 / long run 0.7856
    - 6h: 20 calls (82 a day), hit rate 0.750, chance 0.195, naive rule 0.406, lift 3.84x
    - 24h: 61 calls (61 a day), hit rate 0.721, chance 0.186, naive rule 0.379, lift 3.88x
    - 7d: 399 calls (57 a day), hit rate 0.754, chance 0.186, naive rule 0.406, lift 4.05x
    - 30d: 1662 calls (55 a day), hit rate 0.805, chance 0.187, naive rule 0.406, lift 4.32x
  - next: threshold 0.4456, hit rate recent 0.4441 / long run 0.5017
    - 6h: 18 calls (73 a day), hit rate 0.500, chance 0.195, lift 2.56x
    - 24h: 73 calls (73 a day), hit rate 0.425, chance 0.186, lift 2.28x
    - 7d: 406 calls (58 a day), hit rate 0.498, chance 0.186, lift 2.67x
    - 30d: 2618 calls (87 a day), hit rate 0.486, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.420; 0.35: 355, 0.480; 0.40: 287, 0.551; 0.45: 234, 0.606; 0.50: 187, 0.655; 0.55: 150, 0.692; 0.60: 112, 0.741; 0.65: 76, 0.777; 0.70: 47, 0.813; 0.75: 28, 0.846; 0.80: 9, 0.873
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.384; 0.35: 256, 0.424; 0.40: 161, 0.458; 0.45: 65, 0.493; 0.50: 10, 0.518; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 146792, probability skill vs chance 0.2029, widened contest next: False
  - now: threshold 0.5673, hit rate recent 0.6593 / long run 0.6864
    - 6h: 17 calls (70 a day), hit rate 0.706, chance 0.121, naive rule 0.326, lift 5.81x
    - 24h: 50 calls (50 a day), hit rate 0.600, chance 0.125, naive rule 0.326, lift 4.79x
    - 7d: 369 calls (53 a day), hit rate 0.678, chance 0.124, naive rule 0.343, lift 5.48x
    - 30d: 1526 calls (51 a day), hit rate 0.685, chance 0.121, naive rule 0.335, lift 5.68x
  - next: threshold 0.3666, hit rate recent 0.4552 / long run 0.4236
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.121, lift 5.49x
    - 24h: 60 calls (60 a day), hit rate 0.433, chance 0.125, lift 3.46x
    - 7d: 466 calls (67 a day), hit rate 0.416, chance 0.124, lift 3.37x
    - 30d: 2593 calls (86 a day), hit rate 0.398, chance 0.121, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 193, 0.490; 0.40: 153, 0.535; 0.45: 118, 0.581; 0.50: 84, 0.637; 0.55: 59, 0.673; 0.60: 39, 0.712; 0.65: 24, 0.775; 0.70: 11, 0.813; 0.75: 2, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 170, 0.365; 0.35: 86, 0.393; 0.40: 23, 0.418; 0.45: 4, 0.413; 0.50: 1, 0.773
- **K=13**: model 1794355200, labels learned 146787, probability skill vs chance 0.192, widened contest next: False
  - now: threshold 0.4454, hit rate recent 0.6015 / long run 0.5743
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.084, naive rule 0.319, lift 7.65x
    - 24h: 43 calls (43 a day), hit rate 0.605, chance 0.074, naive rule 0.270, lift 8.17x
    - 7d: 338 calls (48 a day), hit rate 0.577, chance 0.079, naive rule 0.293, lift 7.29x
    - 30d: 1635 calls (55 a day), hit rate 0.561, chance 0.078, naive rule 0.282, lift 7.24x
  - next: threshold 0.2964, hit rate recent 0.3628 / long run 0.3387
    - 6h: 9 calls (38 a day), hit rate 0.667, chance 0.084, lift 7.93x
    - 24h: 57 calls (58 a day), hit rate 0.351, chance 0.074, lift 4.74x
    - 7d: 494 calls (71 a day), hit rate 0.334, chance 0.079, lift 4.22x
    - 30d: 1821 calls (61 a day), hit rate 0.330, chance 0.078, lift 4.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.430; 0.35: 97, 0.478; 0.40: 67, 0.535; 0.45: 46, 0.584; 0.50: 31, 0.638; 0.55: 20, 0.660; 0.60: 12, 0.691; 0.65: 3, 0.660; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.337; 0.35: 13, 0.337; 0.40: 2, 0.392; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.834 | 3.10% | 0.850 | 0.517 | 0.242 | 0.667 | 0.481 |
| 6h | 17.378 | 2.66% | 0.889 | 0.486 | 0.248 | 0.519 | 0.547 |
| 24h | 18.795 | 5.15% | 0.903 | 0.498 | 0.249 | 0.532 | 0.673 |
| 7d | 16.083 | 5.92% | 0.901 | 0.500 | 0.250 | 0.514 | 0.657 |
| 30d | 15.921 | 4.77% | 0.900 | 0.500 | 0.250 | 0.503 | 0.689 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.660 | 26.317 | 26.234 | 25.947 | 27.123 | 26.005 | 26.378 | 25.684 | 25.948 | 25.834 |
| 6h | 17.854 | 17.596 | 17.506 | 17.448 | 17.815 | 17.618 | 17.430 | 17.307 | 17.369 | 17.378 |
| 24h | 19.815 | 19.080 | 19.005 | 18.847 | 19.305 | 19.140 | 18.784 | 18.744 | 18.770 | 18.795 |
| 7d | 17.095 | 16.239 | 16.234 | 16.222 | 16.438 | 16.448 | 16.049 | 16.027 | 16.051 | 16.083 |
| 30d | 16.719 | 16.086 | 16.030 | 15.974 | 16.221 | 16.194 | 15.905 | 15.886 | 15.891 | 15.921 |

## Next candle

- candle starting 2026-11-13 02:43 UTC, last close 1991.03
- P(up) 0.4827, return quantiles (bp): {'05': -18.144, '10': -13.117, '25': -7.01, '40': -2.717, '50': -0.565, '60': 2.733, '75': 7.068, '90': 13.203, '95': 17.688}
- changepoint probability 0.0715, regime age 25.9 min
- agent weights: empirical 0.004, ewma 0.044, garch 0.078, har 0.180, bocpd 0.011, hmm 0.040, online_qr 0.229, lgbm 0.414

## Learning log

- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.37, 6.31, 18.97], current probabilities: [0.008, 0.498, 0.494]
- live generator: {'versions': 60, 'latest_effective': '2026-11-13 02:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.189, 'l_abs': 0.692, 'l_hi': 0.773, 'l_lo': 0.722, 'b05': 0.712, 'b25': 0.71, 'b75': 0.704, 'b95': 0.702}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.703, 1.891, 1.828, 2.218, 2.387, 3.155, 3.058, 3.891, 3.794, 3.074, 3.153, 3.355, 3.559, 3.842]}
- calibration offsets (in sigma): {'05': 0.041, '10': 0.032, '25': -0.065, '40': -0.072, '50': -0.1, '60': -0.038, '75': -0.045, '90': -0.042, '95': -0.031}
