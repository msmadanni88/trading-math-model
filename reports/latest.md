# ETH-USD 60s candle generator - report

- generated: 2026-11-13 10:04 UTC
- last closed candle: 2026-11-13 10:04 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.526 (95) | 0.528 (671) [0.495, 0.559] | 0.520 (2879) [0.503, 0.537] | 0.514 (6905) [0.502, 0.527] | 0.516 (3933) [0.501, 0.533] | 0.450 (40) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.536 (785) | 0.547 (5507) [0.534, 0.559] | 0.543 (23916) [0.537, 0.549] | 0.523 (56554) [0.517, 0.528] | 0.542 (32316) [0.538, 0.547] | 0.531 (358) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.573 (75) | 0.569 (934) [0.537, 0.594] | 0.586 (4284) [0.576, 0.596] | 0.591 (5825) [0.581, 0.602] | 0.591 (5825) [0.581, 0.602] | 0.500 (26) | 0.500 | flat -0.003 (noise 0.023) |
| colour_next | 0.532 (1435) | 0.533 (9973) [0.522, 0.545] | 0.530 (42871) [0.526, 0.534] | 0.517 (102868) [0.513, 0.521] | 0.529 (58519) [0.526, 0.533] | 0.535 (602) | 0.500 | flat +0.007 (noise 0.009) |
| colour_path | 0.503 (20090) | 0.502 (139622) [0.499, 0.504] | 0.502 (600194) [0.500, 0.503] | 0.501 (1440152) [0.500, 0.502] | 0.501 (819266) [0.500, 0.502] | 0.495 (8428) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.455 (11) | 0.622 (241) [0.569, 0.645] | 0.618 (1105) [0.601, 0.635] | 0.629 (1524) [0.612, 0.646] | 0.629 (1524) [0.612, 0.646] | 0.750 (4) | 0.500 | flat +0.010 (noise 0.047) |
| reversal_k13_next | 0.344 (64) | 0.335 (498) [0.313, 0.359] | 0.329 (1828) [0.315, 0.344] | 0.315 (4760) [0.305, 0.325] | 0.327 (2655) [0.316, 0.338] | 0.231 (13) | 0.077 | flat -0.025 (noise 0.033) |
| reversal_k13_now | 0.571 (42) | 0.579 (337) [0.552, 0.608] | 0.561 (1634) [0.542, 0.579] | 0.574 (3700) [0.561, 0.586] | 0.569 (2228) [0.552, 0.585] | 0.583 (24) | 0.077 | flat -0.002 (noise 0.036) |
| reversal_k3_next | 0.576 (59) | 0.609 (358) [0.580, 0.639] | 0.594 (2695) [0.582, 0.606] | 0.588 (6161) [0.580, 0.597] | 0.589 (3721) [0.578, 0.600] | 0.667 (18) | 0.293 | flat +0.000 (noise 0.032) |
| reversal_k3_now | 0.906 (64) | 0.918 (417) [0.909, 0.929] | 0.931 (1736) [0.921, 0.941] | 0.935 (4146) [0.929, 0.941] | 0.929 (2383) [0.922, 0.938] | 1.000 (25) | 0.294 | flat +0.004 (noise 0.019) |
| reversal_k5_next | 0.460 (74) | 0.499 (411) [0.463, 0.532] | 0.486 (2620) [0.471, 0.503] | 0.485 (5531) [0.474, 0.496] | 0.479 (3541) [0.465, 0.494] | 0.440 (25) | 0.187 | flat -0.044 (noise 0.035) |
| reversal_k5_now | 0.737 (57) | 0.761 (397) [0.712, 0.804] | 0.805 (1654) [0.789, 0.820] | 0.821 (3862) [0.811, 0.831] | 0.809 (2251) [0.796, 0.822] | 0.767 (30) | 0.187 | flat -0.047 (noise 0.030) |
| reversal_k8_next | 0.455 (66) | 0.419 (468) [0.392, 0.445] | 0.398 (2598) [0.384, 0.413] | 0.397 (5638) [0.386, 0.407] | 0.397 (3532) [0.385, 0.409] | 0.286 (14) | 0.121 | flat -0.033 (noise 0.033) |
| reversal_k8_now | 0.622 (45) | 0.683 (366) [0.656, 0.708] | 0.685 (1523) [0.666, 0.703] | 0.699 (3740) [0.686, 0.712] | 0.688 (2153) [0.671, 0.704] | 0.667 (27) | 0.122 | flat -0.007 (noise 0.035) |
| overall | 0.507 (22091) | 0.506 (153518) [0.503, 0.508] | 0.506 (662232) [0.504, 0.507] | 0.504 (1587463) [0.503, 0.505] | 0.505 (904182) [0.504, 0.506] | 0.500 (9246) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07462, 0.1143] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5334, 'levels': [{'threshold': 0.07462, 'calls_per_day': 143.5, 'win_rate': 0.5724}, {'threshold': 0.1143, 'calls_per_day': 35.9, 'win_rate': 0.6142}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42871, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15082 | 0.346 | 0.533 (14844) | 0.567 (2278) | 0.738 (2523) |
| volatility: normal | 15081 | 0.371 | 0.529 (15019) | 0.610 (1327) | 0.748 (2230) |
| volatility: wild | 15081 | 0.386 | 0.527 (15043) | 0.603 (765) | 0.767 (2079) |
| session: Asia 00-08 | 15360 | 0.368 | 0.534 (15236) | 0.590 (1548) | 0.752 (2291) |
| session: Europe 08-13 | 9424 | 0.362 | 0.532 (9345) | 0.587 (1131) | 0.748 (1530) |
| session: US 13-21 | 14880 | 0.374 | 0.528 (14781) | 0.597 (1145) | 0.753 (2223) |
| session: late 21-24 | 5580 | 0.360 | 0.515 (5544) | 0.553 (546) | 0.741 (788) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.404 | 0.363 | 0.311 | 0.311 | 0.567 | 0.317 | 0.492 | 1.229 |
| 6h | 360 | 0.388 | 0.372 | 0.297 | 0.340 | 0.513 | 0.280 | 0.496 | 1.103 |
| 24h | 1440 | 0.384 | 0.382 | 0.297 | 0.326 | 0.527 | 0.274 | 0.493 | 1.141 |
| 7d | 10080 | 0.369 | 0.364 | 0.280 | 0.311 | 0.533 | 0.268 | 0.470 | 1.319 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.530 | 0.265 | 0.470 | 1.258 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.404 / 0.567 / 0.883; 2: 0.404 / 0.600 / 0.950; 3: 0.378 / 0.467 / 0.933; 4: 0.357 / 0.467 / 0.850; 5: 0.371 / 0.467 / 0.883; 6: 0.350 / 0.467 / 0.883; 7: 0.388 / 0.550 / 0.983; 8: 0.368 / 0.517 / 0.983; 9: 0.391 / 0.583 / 0.983; 10: 0.358 / 0.533 / 0.967; 11: 0.369 / 0.533 / 0.933; 12: 0.331 / 0.333 / 0.933; 13: 0.396 / 0.617 / 0.950; 14: 0.358 / 0.433 / 0.983; 15: 0.398 / 0.567 / 0.983
- 6h: 1: 0.388 / 0.513 / 0.936; 2: 0.381 / 0.513 / 0.958; 3: 0.372 / 0.474 / 0.958; 4: 0.377 / 0.518 / 0.911; 5: 0.374 / 0.493 / 0.936; 6: 0.362 / 0.482 / 0.931; 7: 0.375 / 0.487 / 0.969; 8: 0.381 / 0.515 / 0.967; 9: 0.363 / 0.460 / 0.981; 10: 0.355 / 0.465 / 0.969; 11: 0.374 / 0.529 / 0.917; 12: 0.367 / 0.468 / 0.925; 13: 0.384 / 0.546 / 0.919; 14: 0.368 / 0.474 / 0.928; 15: 0.383 / 0.507 / 0.944
- 24h: 1: 0.384 / 0.527 / 0.899; 2: 0.369 / 0.490 / 0.907; 3: 0.372 / 0.505 / 0.909; 4: 0.370 / 0.509 / 0.905; 5: 0.370 / 0.499 / 0.909; 6: 0.365 / 0.498 / 0.904; 7: 0.373 / 0.502 / 0.906; 8: 0.373 / 0.513 / 0.909; 9: 0.362 / 0.484 / 0.910; 10: 0.367 / 0.498 / 0.906; 11: 0.368 / 0.505 / 0.901; 12: 0.368 / 0.503 / 0.902; 13: 0.364 / 0.495 / 0.898; 14: 0.366 / 0.502 / 0.899; 15: 0.366 / 0.500 / 0.900
- 7d: 1: 0.369 / 0.533 / 0.897; 2: 0.354 / 0.484 / 0.901; 3: 0.360 / 0.515 / 0.901; 4: 0.354 / 0.496 / 0.900; 5: 0.356 / 0.503 / 0.900; 6: 0.352 / 0.493 / 0.899; 7: 0.354 / 0.500 / 0.901; 8: 0.355 / 0.501 / 0.900; 9: 0.355 / 0.505 / 0.901; 10: 0.354 / 0.501 / 0.902; 11: 0.357 / 0.516 / 0.901; 12: 0.352 / 0.500 / 0.900; 13: 0.353 / 0.499 / 0.899; 14: 0.353 / 0.504 / 0.900; 15: 0.352 / 0.497 / 0.900
- 30d: 1: 0.368 / 0.530 / 0.897; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.499 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.500 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.353 / 0.504 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.351 / 0.503 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.351 / 0.499 / 0.900; 14: 0.351 / 0.501 / 0.900; 15: 0.351 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.099 (body 0.091, range 0.107); 'price stays where it was' would score 0.150; colour right 0.583; typical miss of the close 15.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.137 (body 0.101, range 0.174); 'price stays where it was' would score 0.141; colour right 0.535; typical miss of the close 15.7 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 13.8 bp; chain ended on the right side 0.495 of 95 chains; n=1440
- 7d: match 0.125 (body 0.084, range 0.166); 'price stays where it was' would score 0.125; colour right 0.504; typical miss of the close 8.6 bp; chain ended on the right side 0.531 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.502; typical miss of the close 9.0 bp; chain ended on the right side 0.518 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.203 / 5.5; 3: 0.168 / 7.2; 4: 0.134 / 7.3; 5: 0.126 / 8.1; 6: 0.116 / 9.0; 7: 0.110 / 9.2; 8: 0.098 / 10.2; 9: 0.092 / 10.3; 10: 0.093 / 10.6; 11: 0.089 / 10.9; 12: 0.079 / 11.2; 13: 0.074 / 11.8; 14: 0.069 / 12.3; 15: 0.065 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 147238, probability skill vs chance 0.2289, widened contest next: False
  - now: threshold 0.8361, hit rate recent 0.9322 / long run 0.9259
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.249, naive rule 0.440, lift 4.01x
    - 24h: 62 calls (62 a day), hit rate 0.919, chance 0.279, naive rule 0.487, lift 3.30x
    - 7d: 410 calls (59 a day), hit rate 0.924, chance 0.294, naive rule 0.502, lift 3.14x
    - 30d: 1738 calls (58 a day), hit rate 0.931, chance 0.293, naive rule 0.495, lift 3.18x
  - next: threshold 0.5671, hit rate recent 0.633 / long run 0.6092
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.249, lift 2.67x
    - 24h: 41 calls (41 a day), hit rate 0.683, chance 0.279, lift 2.45x
    - 7d: 350 calls (50 a day), hit rate 0.611, chance 0.294, lift 2.08x
    - 30d: 2674 calls (89 a day), hit rate 0.595, chance 0.293, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.523; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.694; 0.55: 310, 0.739; 0.60: 260, 0.783; 0.65: 220, 0.810; 0.70: 173, 0.842; 0.75: 139, 0.873; 0.80: 92, 0.904; 0.85: 46, 0.943; 0.90: 5, 0.993
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.431; 0.35: 496, 0.464; 0.40: 396, 0.502; 0.45: 298, 0.536; 0.50: 191, 0.568; 0.55: 85, 0.579; 0.60: 11, 0.656; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 147236, probability skill vs chance 0.2106, widened contest next: True
  - now: threshold 0.6888, hit rate recent 0.7518 / long run 0.7861
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.166, naive rule 0.366, lift 5.11x
    - 24h: 67 calls (67 a day), hit rate 0.776, chance 0.180, naive rule 0.387, lift 4.31x
    - 7d: 402 calls (57 a day), hit rate 0.754, chance 0.185, naive rule 0.404, lift 4.08x
    - 30d: 1670 calls (56 a day), hit rate 0.805, chance 0.186, naive rule 0.406, lift 4.32x
  - next: threshold 0.4452, hit rate recent 0.459 / long run 0.5016
    - 6h: 16 calls (65 a day), hit rate 0.375, chance 0.166, lift 2.26x
    - 24h: 69 calls (69 a day), hit rate 0.464, chance 0.180, lift 2.58x
    - 7d: 415 calls (59 a day), hit rate 0.492, chance 0.185, lift 2.66x
    - 30d: 2611 calls (87 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.420; 0.35: 355, 0.480; 0.40: 287, 0.551; 0.45: 234, 0.606; 0.50: 187, 0.654; 0.55: 149, 0.692; 0.60: 112, 0.741; 0.65: 76, 0.779; 0.70: 47, 0.815; 0.75: 28, 0.846; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.383; 0.35: 256, 0.424; 0.40: 161, 0.458; 0.45: 65, 0.493; 0.50: 10, 0.522; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 147233, probability skill vs chance 0.2078, widened contest next: False
  - now: threshold 0.5681, hit rate recent 0.6657 / long run 0.6859
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.133, naive rule 0.398, lift 6.16x
    - 24h: 56 calls (56 a day), hit rate 0.661, chance 0.124, naive rule 0.347, lift 5.31x
    - 7d: 368 calls (53 a day), hit rate 0.679, chance 0.123, naive rule 0.344, lift 5.51x
    - 30d: 1528 calls (51 a day), hit rate 0.684, chance 0.121, naive rule 0.335, lift 5.67x
  - next: threshold 0.3675, hit rate recent 0.4238 / long run 0.4209
    - 6h: 8 calls (33 a day), hit rate 0.250, chance 0.133, lift 1.88x
    - 24h: 46 calls (46 a day), hit rate 0.457, chance 0.124, lift 3.67x
    - 7d: 459 calls (66 a day), hit rate 0.412, chance 0.123, lift 3.34x
    - 30d: 2586 calls (86 a day), hit rate 0.398, chance 0.121, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 193, 0.491; 0.40: 153, 0.534; 0.45: 118, 0.580; 0.50: 84, 0.636; 0.55: 59, 0.671; 0.60: 39, 0.713; 0.65: 24, 0.775; 0.70: 11, 0.815; 0.75: 2, 0.786
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 169, 0.365; 0.35: 86, 0.392; 0.40: 23, 0.419; 0.45: 4, 0.414; 0.50: 1, 0.783
- **K=13**: model 1794355200, labels learned 147228, probability skill vs chance 0.1932, widened contest next: False
  - now: threshold 0.4455, hit rate recent 0.5911 / long run 0.5737
    - 6h: 11 calls (46 a day), hit rate 0.636, chance 0.087, naive rule 0.353, lift 7.32x
    - 24h: 50 calls (51 a day), hit rate 0.620, chance 0.076, naive rule 0.303, lift 8.11x
    - 7d: 343 calls (49 a day), hit rate 0.577, chance 0.079, naive rule 0.293, lift 7.31x
    - 30d: 1637 calls (55 a day), hit rate 0.561, chance 0.078, naive rule 0.283, lift 7.23x
  - next: threshold 0.2965, hit rate recent 0.3304 / long run 0.3358
    - 6h: 9 calls (38 a day), hit rate 0.111, chance 0.087, lift 1.28x
    - 24h: 45 calls (45 a day), hit rate 0.333, chance 0.076, lift 4.36x
    - 7d: 485 calls (69 a day), hit rate 0.330, chance 0.079, lift 4.18x
    - 30d: 1819 calls (61 a day), hit rate 0.329, chance 0.078, lift 4.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.430; 0.35: 97, 0.478; 0.40: 67, 0.535; 0.45: 46, 0.583; 0.50: 31, 0.637; 0.55: 20, 0.658; 0.60: 12, 0.692; 0.65: 3, 0.660; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.337; 0.35: 13, 0.335; 0.40: 2, 0.400; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.388 | 3.63% | 0.883 | 0.517 | 0.252 | 0.450 | 0.345 |
| 6h | 24.148 | 2.01% | 0.925 | 0.497 | 0.251 | 0.490 | 0.564 |
| 24h | 24.262 | 5.58% | 0.902 | 0.497 | 0.249 | 0.523 | 0.636 |
| 7d | 16.596 | 6.08% | 0.901 | 0.500 | 0.250 | 0.514 | 0.666 |
| 30d | 16.098 | 4.82% | 0.900 | 0.500 | 0.250 | 0.504 | 0.691 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.005 | 16.541 | 16.558 | 16.323 | 16.625 | 16.521 | 16.285 | 16.286 | 16.357 | 16.388 |
| 6h | 24.644 | 24.137 | 24.127 | 24.372 | 24.387 | 24.653 | 24.073 | 24.097 | 24.081 | 24.148 |
| 24h | 25.695 | 24.588 | 24.495 | 24.400 | 24.820 | 24.706 | 24.304 | 24.221 | 24.251 | 24.262 |
| 7d | 17.671 | 16.756 | 16.748 | 16.749 | 16.949 | 16.979 | 16.571 | 16.543 | 16.568 | 16.596 |
| 30d | 16.914 | 16.264 | 16.208 | 16.154 | 16.401 | 16.376 | 16.084 | 16.064 | 16.069 | 16.098 |

## Next candle

- candle starting 2026-11-13 10:04 UTC, last close 1944.96
- P(up) 0.4742, return quantiles (bp): {'05': -11.871, '10': -8.537, '25': -5.217, '40': -2.146, '50': -0.412, '60': 1.213, '75': 4.38, '90': 8.663, '95': 12.364}
- changepoint probability 0.0616, regime age 118.1 min
- agent weights: empirical 0.003, ewma 0.091, garch 0.138, har 0.123, bocpd 0.029, hmm 0.030, online_qr 0.215, lgbm 0.371

## Learning log

- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.37, 6.31, 18.97], current probabilities: [0.0, 0.936, 0.064]
- live generator: {'versions': 60, 'latest_effective': '2026-11-13 10:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.188, 'l_abs': 0.701, 'l_hi': 0.762, 'l_lo': 0.723, 'b05': 0.722, 'b25': 0.697, 'b75': 0.654, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.139, 1.344, 1.899, 1.925, 2.288, 2.333, 2.261, 2.451, 2.749, 3.323, 3.342, 3.852, 3.772, 3.54]}
- calibration offsets (in sigma): {'05': 0.0415, '10': 0.063, '25': -0.0125, '40': 0.032, '50': 0.045, '60': 0.038, '75': 0.0425, '90': -0.053, '95': -0.0815}
