# ETH-USD 60s candle generator - report

- generated: 2026-11-13 17:40 UTC
- last closed candle: 2026-11-13 17:40 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.526 (95) | 0.528 (671) [0.495, 0.559] | 0.520 (2879) [0.503, 0.537] | 0.514 (6905) [0.502, 0.527] | 0.516 (3933) [0.501, 0.533] | 0.500 (70) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.536 (785) | 0.547 (5507) [0.534, 0.559] | 0.543 (23916) [0.537, 0.549] | 0.523 (56554) [0.517, 0.528] | 0.542 (32316) [0.538, 0.547] | 0.534 (625) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.573 (75) | 0.569 (934) [0.537, 0.594] | 0.586 (4284) [0.576, 0.596] | 0.591 (5825) [0.581, 0.602] | 0.591 (5825) [0.581, 0.602] | 0.527 (55) | 0.500 | flat -0.003 (noise 0.023) |
| colour_next | 0.532 (1435) | 0.533 (9973) [0.522, 0.545] | 0.530 (42871) [0.526, 0.534] | 0.517 (102868) [0.513, 0.521] | 0.529 (58519) [0.526, 0.533] | 0.522 (1056) | 0.500 | flat +0.007 (noise 0.009) |
| colour_path | 0.503 (20090) | 0.502 (139622) [0.499, 0.504] | 0.502 (600194) [0.500, 0.503] | 0.501 (1440152) [0.500, 0.502] | 0.501 (819266) [0.500, 0.502] | 0.497 (14784) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.455 (11) | 0.622 (241) [0.569, 0.645] | 0.618 (1105) [0.601, 0.635] | 0.629 (1524) [0.612, 0.646] | 0.629 (1524) [0.612, 0.646] | 0.538 (13) | 0.500 | flat +0.010 (noise 0.047) |
| reversal_k13_next | 0.344 (64) | 0.335 (498) [0.313, 0.359] | 0.329 (1828) [0.315, 0.344] | 0.315 (4760) [0.305, 0.325] | 0.327 (2655) [0.316, 0.338] | 0.294 (34) | 0.077 | flat -0.025 (noise 0.033) |
| reversal_k13_now | 0.571 (42) | 0.579 (337) [0.552, 0.608] | 0.561 (1634) [0.542, 0.579] | 0.574 (3700) [0.561, 0.586] | 0.569 (2228) [0.552, 0.585] | 0.511 (45) | 0.077 | flat -0.002 (noise 0.036) |
| reversal_k3_next | 0.576 (59) | 0.609 (358) [0.580, 0.639] | 0.594 (2695) [0.582, 0.606] | 0.588 (6161) [0.580, 0.597] | 0.589 (3721) [0.578, 0.600] | 0.655 (29) | 0.293 | flat +0.000 (noise 0.032) |
| reversal_k3_now | 0.906 (64) | 0.918 (417) [0.909, 0.929] | 0.931 (1736) [0.921, 0.941] | 0.935 (4146) [0.929, 0.941] | 0.929 (2383) [0.922, 0.938] | 0.956 (45) | 0.294 | flat +0.004 (noise 0.019) |
| reversal_k5_next | 0.460 (74) | 0.499 (411) [0.463, 0.532] | 0.486 (2620) [0.471, 0.503] | 0.485 (5531) [0.474, 0.496] | 0.479 (3541) [0.465, 0.494] | 0.549 (51) | 0.187 | flat -0.044 (noise 0.035) |
| reversal_k5_now | 0.737 (57) | 0.761 (397) [0.712, 0.804] | 0.805 (1654) [0.789, 0.820] | 0.821 (3862) [0.811, 0.831] | 0.809 (2251) [0.796, 0.822] | 0.717 (53) | 0.187 | flat -0.047 (noise 0.030) |
| reversal_k8_next | 0.455 (66) | 0.419 (468) [0.392, 0.445] | 0.398 (2598) [0.384, 0.413] | 0.397 (5638) [0.386, 0.407] | 0.397 (3532) [0.385, 0.409] | 0.389 (36) | 0.121 | flat -0.033 (noise 0.033) |
| reversal_k8_now | 0.622 (45) | 0.683 (366) [0.656, 0.708] | 0.685 (1523) [0.666, 0.703] | 0.699 (3740) [0.686, 0.712] | 0.688 (2153) [0.671, 0.704] | 0.625 (48) | 0.122 | flat -0.007 (noise 0.035) |
| overall | 0.507 (22091) | 0.506 (153518) [0.503, 0.508] | 0.506 (662232) [0.504, 0.507] | 0.504 (1587463) [0.503, 0.505] | 0.505 (904182) [0.504, 0.506] | 0.501 (16251) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07468, 0.1144] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5326, 'levels': [{'threshold': 0.07468, 'calls_per_day': 144.3, 'win_rate': 0.573}, {'threshold': 0.1144, 'calls_per_day': 36.2, 'win_rate': 0.6172}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42870, 'rate': 0.5295}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15234 | 0.347 | 0.533 (14995) | 0.566 (2295) | 0.740 (2545) |
| volatility: normal | 15233 | 0.371 | 0.528 (15169) | 0.614 (1325) | 0.745 (2265) |
| volatility: wild | 15233 | 0.387 | 0.527 (15196) | 0.600 (779) | 0.764 (2107) |
| session: Asia 00-08 | 15360 | 0.368 | 0.534 (15236) | 0.590 (1548) | 0.752 (2291) |
| session: Europe 08-13 | 9600 | 0.362 | 0.531 (9519) | 0.587 (1146) | 0.745 (1567) |
| session: US 13-21 | 15160 | 0.375 | 0.528 (15061) | 0.595 (1159) | 0.751 (2271) |
| session: late 21-24 | 5580 | 0.360 | 0.515 (5544) | 0.553 (546) | 0.741 (788) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.383 | 0.379 | 0.309 | 0.309 | 0.517 | 0.240 | 0.525 | 1.388 |
| 6h | 360 | 0.388 | 0.386 | 0.324 | 0.346 | 0.501 | 0.267 | 0.509 | 1.055 |
| 24h | 1440 | 0.383 | 0.377 | 0.302 | 0.331 | 0.517 | 0.270 | 0.496 | 1.064 |
| 7d | 10080 | 0.368 | 0.364 | 0.282 | 0.312 | 0.530 | 0.267 | 0.469 | 1.312 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.530 | 0.265 | 0.471 | 1.257 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.383 / 0.517 / 0.917; 2: 0.363 / 0.517 / 0.850; 3: 0.394 / 0.550 / 0.850; 4: 0.382 / 0.517 / 0.867; 5: 0.395 / 0.533 / 0.833; 6: 0.369 / 0.467 / 0.867; 7: 0.360 / 0.450 / 0.850; 8: 0.377 / 0.483 / 0.850; 9: 0.350 / 0.400 / 0.900; 10: 0.362 / 0.450 / 0.983; 11: 0.381 / 0.583 / 1.000; 12: 0.358 / 0.450 / 0.983; 13: 0.377 / 0.483 / 0.967; 14: 0.379 / 0.533 / 0.967; 15: 0.369 / 0.450 / 0.933
- 6h: 1: 0.388 / 0.501 / 0.886; 2: 0.366 / 0.465 / 0.806; 3: 0.388 / 0.521 / 0.786; 4: 0.371 / 0.465 / 0.842; 5: 0.385 / 0.504 / 0.808; 6: 0.381 / 0.490 / 0.856; 7: 0.375 / 0.487 / 0.828; 8: 0.381 / 0.496 / 0.806; 9: 0.366 / 0.460 / 0.839; 10: 0.377 / 0.496 / 0.864; 11: 0.384 / 0.549 / 0.903; 12: 0.381 / 0.526 / 0.908; 13: 0.380 / 0.496 / 0.928; 14: 0.369 / 0.493 / 0.914; 15: 0.376 / 0.496 / 0.886
- 24h: 1: 0.383 / 0.517 / 0.890; 2: 0.369 / 0.487 / 0.883; 3: 0.376 / 0.506 / 0.881; 4: 0.367 / 0.485 / 0.883; 5: 0.373 / 0.504 / 0.872; 6: 0.365 / 0.492 / 0.886; 7: 0.371 / 0.492 / 0.887; 8: 0.373 / 0.508 / 0.883; 9: 0.361 / 0.476 / 0.892; 10: 0.367 / 0.492 / 0.896; 11: 0.375 / 0.526 / 0.920; 12: 0.366 / 0.486 / 0.925; 13: 0.368 / 0.491 / 0.924; 14: 0.361 / 0.482 / 0.924; 15: 0.366 / 0.487 / 0.922
- 7d: 1: 0.368 / 0.530 / 0.896; 2: 0.353 / 0.486 / 0.897; 3: 0.360 / 0.515 / 0.896; 4: 0.354 / 0.497 / 0.898; 5: 0.355 / 0.502 / 0.897; 6: 0.352 / 0.494 / 0.901; 7: 0.353 / 0.498 / 0.897; 8: 0.356 / 0.503 / 0.899; 9: 0.354 / 0.503 / 0.897; 10: 0.353 / 0.498 / 0.898; 11: 0.357 / 0.516 / 0.898; 12: 0.353 / 0.502 / 0.898; 13: 0.353 / 0.501 / 0.900; 14: 0.352 / 0.504 / 0.899; 15: 0.352 / 0.496 / 0.899
- 30d: 1: 0.368 / 0.530 / 0.897; 2: 0.355 / 0.493 / 0.899; 3: 0.358 / 0.510 / 0.899; 4: 0.354 / 0.498 / 0.899; 5: 0.355 / 0.504 / 0.899; 6: 0.352 / 0.500 / 0.900; 7: 0.353 / 0.499 / 0.899; 8: 0.353 / 0.504 / 0.899; 9: 0.353 / 0.503 / 0.900; 10: 0.353 / 0.502 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.503 / 0.900; 13: 0.351 / 0.500 / 0.900; 14: 0.351 / 0.501 / 0.900; 15: 0.351 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.156 (body 0.097, range 0.215); 'price stays where it was' would score 0.186; colour right 0.533; typical miss of the close 12.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.080, range 0.169); 'price stays where it was' would score 0.118; colour right 0.485; typical miss of the close 14.6 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.128 (body 0.086, range 0.170); 'price stays where it was' would score 0.130; colour right 0.506; typical miss of the close 12.9 bp; chain ended on the right side 0.505 of 95 chains; n=1440
- 7d: match 0.125 (body 0.084, range 0.165); 'price stays where it was' would score 0.125; colour right 0.503; typical miss of the close 8.7 bp; chain ended on the right side 0.528 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.502; typical miss of the close 9.0 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.204 / 5.5; 3: 0.168 / 7.2; 4: 0.134 / 7.3; 5: 0.125 / 8.1; 6: 0.116 / 9.0; 7: 0.110 / 9.2; 8: 0.098 / 10.1; 9: 0.092 / 10.3; 10: 0.093 / 10.6; 11: 0.090 / 10.9; 12: 0.080 / 11.2; 13: 0.074 / 11.8; 14: 0.069 / 12.3; 15: 0.066 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 147694, probability skill vs chance 0.2304, widened contest next: False
  - now: threshold 0.8379, hit rate recent 0.9201 / long run 0.925
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.290, naive rule 0.482, lift 2.92x
    - 24h: 64 calls (64 a day), hit rate 0.922, chance 0.279, naive rule 0.482, lift 3.30x
    - 7d: 415 calls (59 a day), hit rate 0.923, chance 0.293, naive rule 0.500, lift 3.15x
    - 30d: 1745 calls (58 a day), hit rate 0.931, chance 0.293, naive rule 0.495, lift 3.17x
  - next: threshold 0.567, hit rate recent 0.6331 / long run 0.6097
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.290, lift 2.07x
    - 24h: 39 calls (39 a day), hit rate 0.692, chance 0.279, lift 2.48x
    - 7d: 351 calls (50 a day), hit rate 0.613, chance 0.293, lift 2.09x
    - 30d: 2667 calls (89 a day), hit rate 0.595, chance 0.293, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.694; 0.55: 310, 0.739; 0.60: 260, 0.783; 0.65: 220, 0.810; 0.70: 173, 0.842; 0.75: 139, 0.873; 0.80: 92, 0.904; 0.85: 46, 0.944; 0.90: 5, 0.993
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.431; 0.35: 497, 0.465; 0.40: 396, 0.503; 0.45: 298, 0.536; 0.50: 191, 0.569; 0.55: 84, 0.579; 0.60: 11, 0.657; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 147692, probability skill vs chance 0.2136, widened contest next: True
  - now: threshold 0.6902, hit rate recent 0.7228 / long run 0.7811
    - 6h: 16 calls (65 a day), hit rate 0.750, chance 0.169, naive rule 0.381, lift 4.45x
    - 24h: 72 calls (72 a day), hit rate 0.750, chance 0.179, naive rule 0.383, lift 4.18x
    - 7d: 405 calls (58 a day), hit rate 0.746, chance 0.185, naive rule 0.403, lift 4.04x
    - 30d: 1684 calls (56 a day), hit rate 0.803, chance 0.186, naive rule 0.406, lift 4.31x
  - next: threshold 0.4453, hit rate recent 0.5233 / long run 0.508
    - 6h: 21 calls (86 a day), hit rate 0.571, chance 0.169, lift 3.39x
    - 24h: 76 calls (76 a day), hit rate 0.553, chance 0.179, lift 3.08x
    - 7d: 428 calls (61 a day), hit rate 0.500, chance 0.185, lift 2.71x
    - 30d: 2594 calls (86 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.419; 0.35: 355, 0.479; 0.40: 288, 0.550; 0.45: 234, 0.605; 0.50: 187, 0.653; 0.55: 149, 0.692; 0.60: 112, 0.740; 0.65: 76, 0.776; 0.70: 48, 0.812; 0.75: 28, 0.844; 0.80: 9, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.383; 0.35: 256, 0.424; 0.40: 160, 0.457; 0.45: 65, 0.495; 0.50: 10, 0.533; 0.55: 1, 0.444
- **K=8**: model 1794182400, labels learned 147689, probability skill vs chance 0.2028, widened contest next: True
  - now: threshold 0.5687, hit rate recent 0.6395 / long run 0.6819
    - 6h: 16 calls (66 a day), hit rate 0.625, chance 0.127, naive rule 0.322, lift 4.92x
    - 24h: 63 calls (63 a day), hit rate 0.635, chance 0.125, naive rule 0.342, lift 5.07x
    - 7d: 370 calls (53 a day), hit rate 0.673, chance 0.124, naive rule 0.344, lift 5.42x
    - 30d: 1541 calls (51 a day), hit rate 0.683, chance 0.121, naive rule 0.335, lift 5.66x
  - next: threshold 0.368, hit rate recent 0.4345 / long run 0.4221
    - 6h: 18 calls (74 a day), hit rate 0.444, chance 0.127, lift 3.50x
    - 24h: 52 calls (52 a day), hit rate 0.462, chance 0.125, lift 3.69x
    - 7d: 460 calls (66 a day), hit rate 0.413, chance 0.124, lift 3.33x
    - 30d: 2586 calls (86 a day), hit rate 0.398, chance 0.121, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 193, 0.490; 0.40: 153, 0.534; 0.45: 118, 0.580; 0.50: 84, 0.636; 0.55: 59, 0.671; 0.60: 40, 0.711; 0.65: 24, 0.771; 0.70: 11, 0.815; 0.75: 2, 0.783
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 169, 0.365; 0.35: 85, 0.391; 0.40: 23, 0.418; 0.45: 4, 0.412; 0.50: 1, 0.783
- **K=13**: model 1794355200, labels learned 147684, probability skill vs chance 0.1833, widened contest next: False
  - now: threshold 0.4464, hit rate recent 0.547 / long run 0.5688
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.080, naive rule 0.290, lift 6.27x
    - 24h: 58 calls (59 a day), hit rate 0.552, chance 0.081, naive rule 0.311, lift 6.78x
    - 7d: 347 calls (50 a day), hit rate 0.565, chance 0.079, naive rule 0.292, lift 7.16x
    - 30d: 1647 calls (55 a day), hit rate 0.561, chance 0.078, naive rule 0.284, lift 7.21x
  - next: threshold 0.2966, hit rate recent 0.3321 / long run 0.3357
    - 6h: 18 calls (75 a day), hit rate 0.333, chance 0.080, lift 4.18x
    - 24h: 50 calls (51 a day), hit rate 0.340, chance 0.081, lift 4.18x
    - 7d: 487 calls (70 a day), hit rate 0.329, chance 0.079, lift 4.16x
    - 30d: 1821 calls (61 a day), hit rate 0.331, chance 0.078, lift 4.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.431; 0.35: 97, 0.478; 0.40: 67, 0.535; 0.45: 46, 0.583; 0.50: 32, 0.634; 0.55: 20, 0.656; 0.60: 12, 0.693; 0.65: 3, 0.657; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.339; 0.35: 13, 0.337; 0.40: 2, 0.400; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.296 | 0.09% | 0.900 | 0.650 | 0.251 | 0.467 | 0.063 |
| 6h | 26.758 | 4.57% | 0.886 | 0.500 | 0.250 | 0.513 | 0.646 |
| 24h | 23.315 | 4.29% | 0.892 | 0.494 | 0.250 | 0.510 | 0.653 |
| 7d | 16.635 | 6.05% | 0.900 | 0.499 | 0.250 | 0.514 | 0.668 |
| 30d | 16.113 | 4.77% | 0.900 | 0.500 | 0.250 | 0.504 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.314 | 19.646 | 19.355 | 19.229 | 19.618 | 19.284 | 18.946 | 19.256 | 19.135 | 19.296 |
| 6h | 28.039 | 27.016 | 26.949 | 26.548 | 27.092 | 27.004 | 26.671 | 26.796 | 26.678 | 26.758 |
| 24h | 24.361 | 23.514 | 23.428 | 23.360 | 23.672 | 23.636 | 23.347 | 23.302 | 23.291 | 23.315 |
| 7d | 17.705 | 16.801 | 16.787 | 16.777 | 16.980 | 17.009 | 16.614 | 16.585 | 16.606 | 16.635 |
| 30d | 16.921 | 16.281 | 16.222 | 16.168 | 16.415 | 16.390 | 16.099 | 16.079 | 16.084 | 16.113 |

## Next candle

- candle starting 2026-11-13 17:40 UTC, last close 1936.56
- P(up) 0.5063, return quantiles (bp): {'05': -13.09, '10': -9.435, '25': -5.049, '40': -2.33, '50': 0.158, '60': 2.181, '75': 5.271, '90': 9.633, '95': 12.435}
- changepoint probability 0.0528, regime age 50.5 min
- agent weights: empirical 0.003, ewma 0.057, garch 0.097, har 0.311, bocpd 0.027, hmm 0.038, online_qr 0.251, lgbm 0.216

## Learning log

- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- HMM volatility states (sd, bp per minute): [3.98, 6.75, 18.41], current probabilities: [0.081, 0.899, 0.02]
- live generator: {'versions': 60, 'latest_effective': '2026-11-13 17:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.226, 'l_abs': 0.619, 'l_hi': 0.794, 'l_lo': 0.73, 'b05': 0.709, 'b25': 0.667, 'b75': 0.626, 'b95': 0.687}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [2.506, 3.609, 2.855, 3.986, 3.177, 3.877, 4.682, 3.837, 3.741, 3.777, 3.506, 3.513, 3.727, 4.272]}
- calibration offsets (in sigma): {'05': 0.0095, '10': 0.019, '25': -0.0125, '40': -0.024, '50': 0.045, '60': 0.054, '75': 0.0325, '90': 0.001, '95': -0.0395}
