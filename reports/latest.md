# ETH-USD 60s candle generator - report

- generated: 2026-11-13 22:54 UTC
- last closed candle: 2026-11-13 22:54 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.526 (95) | 0.528 (671) [0.495, 0.559] | 0.520 (2879) [0.503, 0.537] | 0.514 (6905) [0.502, 0.527] | 0.516 (3933) [0.501, 0.533] | 0.494 (91) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.536 (785) | 0.547 (5507) [0.534, 0.559] | 0.543 (23916) [0.537, 0.549] | 0.523 (56554) [0.517, 0.528] | 0.542 (32316) [0.538, 0.547] | 0.538 (807) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.573 (75) | 0.569 (934) [0.537, 0.594] | 0.586 (4284) [0.576, 0.596] | 0.591 (5825) [0.581, 0.602] | 0.591 (5825) [0.581, 0.602] | 0.549 (71) | 0.500 | flat -0.003 (noise 0.023) |
| colour_next | 0.532 (1435) | 0.533 (9973) [0.522, 0.545] | 0.530 (42871) [0.526, 0.534] | 0.517 (102868) [0.513, 0.521] | 0.529 (58519) [0.526, 0.533] | 0.530 (1369) | 0.500 | flat +0.007 (noise 0.009) |
| colour_path | 0.503 (20090) | 0.502 (139622) [0.499, 0.504] | 0.502 (600194) [0.500, 0.503] | 0.501 (1440152) [0.500, 0.502] | 0.501 (819266) [0.500, 0.502] | 0.500 (19166) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.455 (11) | 0.622 (241) [0.569, 0.645] | 0.618 (1105) [0.601, 0.635] | 0.629 (1524) [0.612, 0.646] | 0.629 (1524) [0.612, 0.646] | 0.533 (15) | 0.500 | flat +0.010 (noise 0.047) |
| reversal_k13_next | 0.344 (64) | 0.335 (498) [0.313, 0.359] | 0.329 (1828) [0.315, 0.344] | 0.315 (4760) [0.305, 0.325] | 0.327 (2655) [0.316, 0.338] | 0.286 (49) | 0.077 | flat -0.025 (noise 0.033) |
| reversal_k13_now | 0.571 (42) | 0.579 (337) [0.552, 0.608] | 0.561 (1634) [0.542, 0.579] | 0.574 (3700) [0.561, 0.586] | 0.569 (2228) [0.552, 0.585] | 0.509 (55) | 0.077 | flat -0.002 (noise 0.036) |
| reversal_k3_next | 0.576 (59) | 0.609 (358) [0.580, 0.639] | 0.594 (2695) [0.582, 0.606] | 0.588 (6161) [0.580, 0.597] | 0.589 (3721) [0.578, 0.600] | 0.700 (40) | 0.293 | flat +0.000 (noise 0.032) |
| reversal_k3_now | 0.906 (64) | 0.918 (417) [0.909, 0.929] | 0.931 (1736) [0.921, 0.941] | 0.935 (4146) [0.929, 0.941] | 0.929 (2383) [0.922, 0.938] | 0.946 (55) | 0.294 | flat +0.004 (noise 0.019) |
| reversal_k5_next | 0.460 (74) | 0.499 (411) [0.463, 0.532] | 0.486 (2620) [0.471, 0.503] | 0.485 (5531) [0.474, 0.496] | 0.479 (3541) [0.465, 0.494] | 0.528 (72) | 0.187 | flat -0.044 (noise 0.035) |
| reversal_k5_now | 0.737 (57) | 0.761 (397) [0.712, 0.804] | 0.805 (1654) [0.789, 0.820] | 0.821 (3862) [0.811, 0.831] | 0.809 (2251) [0.796, 0.822] | 0.716 (67) | 0.187 | flat -0.047 (noise 0.030) |
| reversal_k8_next | 0.455 (66) | 0.419 (468) [0.392, 0.445] | 0.398 (2598) [0.384, 0.413] | 0.397 (5638) [0.386, 0.407] | 0.397 (3532) [0.385, 0.409] | 0.377 (53) | 0.121 | flat -0.033 (noise 0.033) |
| reversal_k8_now | 0.622 (45) | 0.683 (366) [0.656, 0.708] | 0.685 (1523) [0.666, 0.703] | 0.699 (3740) [0.686, 0.712] | 0.688 (2153) [0.671, 0.704] | 0.600 (60) | 0.122 | flat -0.007 (noise 0.035) |
| overall | 0.507 (22091) | 0.506 (153518) [0.503, 0.508] | 0.506 (662232) [0.504, 0.507] | 0.504 (1587463) [0.503, 0.505] | 0.505 (904182) [0.504, 0.506] | 0.503 (21077) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07467, 0.1148] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5301, 'levels': [{'threshold': 0.07467, 'calls_per_day': 143.9, 'win_rate': 0.5697}, {'threshold': 0.1148, 'calls_per_day': 36.0, 'win_rate': 0.6157}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42869, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15338 | 0.347 | 0.533 (15099) | 0.566 (2304) | 0.741 (2566) |
| volatility: normal | 15338 | 0.371 | 0.528 (15273) | 0.616 (1325) | 0.745 (2290) |
| volatility: wild | 15338 | 0.387 | 0.527 (15301) | 0.597 (786) | 0.761 (2107) |
| session: Asia 00-08 | 15360 | 0.368 | 0.534 (15236) | 0.590 (1548) | 0.752 (2291) |
| session: Europe 08-13 | 9600 | 0.362 | 0.531 (9519) | 0.587 (1146) | 0.745 (1567) |
| session: US 13-21 | 15360 | 0.375 | 0.529 (15260) | 0.596 (1171) | 0.749 (2301) |
| session: late 21-24 | 5694 | 0.360 | 0.514 (5658) | 0.553 (550) | 0.740 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.384 | 0.363 | 0.273 | 0.273 | 0.483 | 0.278 | 0.490 | 1.070 |
| 6h | 360 | 0.380 | 0.374 | 0.286 | 0.318 | 0.546 | 0.272 | 0.488 | 1.110 |
| 24h | 1440 | 0.387 | 0.381 | 0.296 | 0.324 | 0.531 | 0.277 | 0.496 | 1.030 |
| 7d | 10080 | 0.368 | 0.363 | 0.281 | 0.311 | 0.530 | 0.267 | 0.468 | 1.307 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.530 | 0.265 | 0.471 | 1.255 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.384 / 0.483 / 0.917; 2: 0.371 / 0.450 / 0.983; 3: 0.348 / 0.400 / 1.000; 4: 0.395 / 0.567 / 0.983; 5: 0.383 / 0.483 / 1.000; 6: 0.404 / 0.583 / 1.000; 7: 0.401 / 0.517 / 1.000; 8: 0.388 / 0.567 / 1.000; 9: 0.416 / 0.617 / 1.000; 10: 0.412 / 0.617 / 1.000; 11: 0.400 / 0.550 / 1.000; 12: 0.386 / 0.517 / 0.967; 13: 0.355 / 0.417 / 0.967; 14: 0.402 / 0.550 / 0.950; 15: 0.381 / 0.467 / 0.967
- 6h: 1: 0.380 / 0.546 / 0.883; 2: 0.373 / 0.529 / 0.956; 3: 0.366 / 0.504 / 0.967; 4: 0.360 / 0.490 / 0.947; 5: 0.368 / 0.507 / 0.950; 6: 0.359 / 0.482 / 0.947; 7: 0.374 / 0.524 / 0.944; 8: 0.370 / 0.526 / 0.944; 9: 0.364 / 0.482 / 0.931; 10: 0.369 / 0.504 / 0.944; 11: 0.369 / 0.532 / 0.942; 12: 0.354 / 0.462 / 0.894; 13: 0.363 / 0.510 / 0.889; 14: 0.368 / 0.521 / 0.872; 15: 0.369 / 0.507 / 0.889
- 24h: 1: 0.387 / 0.531 / 0.890; 2: 0.373 / 0.496 / 0.892; 3: 0.375 / 0.505 / 0.890; 4: 0.370 / 0.494 / 0.905; 5: 0.373 / 0.504 / 0.896; 6: 0.367 / 0.494 / 0.902; 7: 0.376 / 0.505 / 0.890; 8: 0.373 / 0.509 / 0.884; 9: 0.362 / 0.473 / 0.887; 10: 0.367 / 0.496 / 0.890; 11: 0.374 / 0.528 / 0.906; 12: 0.365 / 0.483 / 0.899; 13: 0.368 / 0.499 / 0.898; 14: 0.365 / 0.497 / 0.893; 15: 0.368 / 0.497 / 0.897
- 7d: 1: 0.368 / 0.530 / 0.895; 2: 0.353 / 0.487 / 0.900; 3: 0.359 / 0.514 / 0.898; 4: 0.353 / 0.496 / 0.899; 5: 0.355 / 0.502 / 0.899; 6: 0.351 / 0.493 / 0.901; 7: 0.354 / 0.500 / 0.900; 8: 0.355 / 0.504 / 0.899; 9: 0.354 / 0.504 / 0.901; 10: 0.353 / 0.500 / 0.902; 11: 0.356 / 0.517 / 0.902; 12: 0.352 / 0.502 / 0.901; 13: 0.352 / 0.500 / 0.899; 14: 0.352 / 0.504 / 0.901; 15: 0.352 / 0.497 / 0.899
- 30d: 1: 0.368 / 0.530 / 0.897; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.498 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.352 / 0.500 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.353 / 0.505 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.353 / 0.502 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.503 / 0.900; 13: 0.351 / 0.499 / 0.900; 14: 0.351 / 0.502 / 0.899; 15: 0.351 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.117 (body 0.071, range 0.163); 'price stays where it was' would score 0.103; colour right 0.583; typical miss of the close 19.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.105 (body 0.067, range 0.143); 'price stays where it was' would score 0.126; colour right 0.540; typical miss of the close 15.0 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.128; colour right 0.520; typical miss of the close 14.8 bp; chain ended on the right side 0.495 of 95 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.123; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.529 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.0 bp; chain ended on the right side 0.520 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.7; 2: 0.204 / 5.5; 3: 0.168 / 7.1; 4: 0.135 / 7.3; 5: 0.125 / 8.2; 6: 0.116 / 9.0; 7: 0.110 / 9.3; 8: 0.098 / 10.2; 9: 0.092 / 10.3; 10: 0.093 / 10.6; 11: 0.090 / 10.9; 12: 0.080 / 11.3; 13: 0.074 / 11.8; 14: 0.069 / 12.3; 15: 0.066 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 148008, probability skill vs chance 0.2327, widened contest next: False
  - now: threshold 0.8388, hit rate recent 0.9166 / long run 0.9246
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.263, naive rule 0.450, lift 3.45x
    - 24h: 59 calls (59 a day), hit rate 0.949, chance 0.279, naive rule 0.487, lift 3.40x
    - 7d: 414 calls (59 a day), hit rate 0.920, chance 0.291, naive rule 0.499, lift 3.16x
    - 30d: 1743 calls (58 a day), hit rate 0.930, chance 0.293, naive rule 0.495, lift 3.17x
  - next: threshold 0.5672, hit rate recent 0.6659 / long run 0.6135
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.263, lift 3.16x
    - 24h: 40 calls (40 a day), hit rate 0.700, chance 0.279, lift 2.50x
    - 7d: 358 calls (51 a day), hit rate 0.620, chance 0.291, lift 2.13x
    - 30d: 2670 calls (89 a day), hit rate 0.596, chance 0.293, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.694; 0.55: 310, 0.738; 0.60: 261, 0.783; 0.65: 220, 0.811; 0.70: 173, 0.842; 0.75: 139, 0.873; 0.80: 92, 0.904; 0.85: 46, 0.943; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.431; 0.35: 497, 0.464; 0.40: 396, 0.502; 0.45: 298, 0.536; 0.50: 190, 0.569; 0.55: 84, 0.579; 0.60: 12, 0.660; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 148006, probability skill vs chance 0.2149, widened contest next: True
  - now: threshold 0.6906, hit rate recent 0.7218 / long run 0.7796
    - 6h: 15 calls (61 a day), hit rate 0.733, chance 0.186, naive rule 0.391, lift 3.95x
    - 24h: 71 calls (71 a day), hit rate 0.718, chance 0.179, naive rule 0.384, lift 4.02x
    - 7d: 408 calls (58 a day), hit rate 0.740, chance 0.184, naive rule 0.402, lift 4.02x
    - 30d: 1688 calls (56 a day), hit rate 0.801, chance 0.186, naive rule 0.405, lift 4.31x
  - next: threshold 0.4455, hit rate recent 0.5126 / long run 0.507
    - 6h: 23 calls (94 a day), hit rate 0.478, chance 0.186, lift 2.58x
    - 24h: 74 calls (74 a day), hit rate 0.527, chance 0.179, lift 2.95x
    - 7d: 447 calls (64 a day), hit rate 0.501, chance 0.184, lift 2.72x
    - 30d: 2599 calls (87 a day), hit rate 0.485, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.419; 0.35: 356, 0.478; 0.40: 288, 0.549; 0.45: 234, 0.604; 0.50: 187, 0.652; 0.55: 149, 0.690; 0.60: 112, 0.738; 0.65: 76, 0.775; 0.70: 48, 0.810; 0.75: 28, 0.843; 0.80: 9, 0.869
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.383; 0.35: 256, 0.423; 0.40: 161, 0.456; 0.45: 65, 0.493; 0.50: 10, 0.533; 0.55: 1, 0.444
- **K=8**: model 1794182400, labels learned 148003, probability skill vs chance 0.2004, widened contest next: True
  - now: threshold 0.5689, hit rate recent 0.6152 / long run 0.6784
    - 6h: 13 calls (53 a day), hit rate 0.538, chance 0.097, naive rule 0.254, lift 5.54x
    - 24h: 64 calls (64 a day), hit rate 0.609, chance 0.114, naive rule 0.312, lift 5.35x
    - 7d: 371 calls (53 a day), hit rate 0.666, chance 0.123, naive rule 0.342, lift 5.42x
    - 30d: 1543 calls (51 a day), hit rate 0.680, chance 0.121, naive rule 0.335, lift 5.65x
  - next: threshold 0.3683, hit rate recent 0.416 / long run 0.4202
    - 6h: 18 calls (74 a day), hit rate 0.389, chance 0.097, lift 4.00x
    - 24h: 56 calls (56 a day), hit rate 0.393, chance 0.114, lift 3.45x
    - 7d: 473 calls (68 a day), hit rate 0.412, chance 0.123, lift 3.35x
    - 30d: 2595 calls (87 a day), hit rate 0.398, chance 0.121, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.426; 0.35: 193, 0.489; 0.40: 153, 0.533; 0.45: 118, 0.578; 0.50: 84, 0.634; 0.55: 59, 0.669; 0.60: 40, 0.708; 0.65: 24, 0.767; 0.70: 11, 0.812; 0.75: 2, 0.779
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 169, 0.364; 0.35: 85, 0.390; 0.40: 23, 0.421; 0.45: 4, 0.417; 0.50: 1, 0.783
- **K=13**: model 1794355200, labels learned 147998, probability skill vs chance 0.1787, widened contest next: False
  - now: threshold 0.446, hit rate recent 0.5404 / long run 0.5677
    - 6h: 11 calls (46 a day), hit rate 0.545, chance 0.071, naive rule 0.266, lift 7.68x
    - 24h: 58 calls (59 a day), hit rate 0.517, chance 0.080, naive rule 0.297, lift 6.49x
    - 7d: 347 calls (50 a day), hit rate 0.562, chance 0.079, naive rule 0.292, lift 7.13x
    - 30d: 1647 calls (55 a day), hit rate 0.559, chance 0.078, naive rule 0.283, lift 7.20x
  - next: threshold 0.2972, hit rate recent 0.3187 / long run 0.334
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.071, lift 4.40x
    - 24h: 51 calls (52 a day), hit rate 0.294, chance 0.080, lift 3.69x
    - 7d: 496 calls (71 a day), hit rate 0.327, chance 0.079, lift 4.15x
    - 30d: 1832 calls (61 a day), hit rate 0.330, chance 0.078, lift 4.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.429; 0.35: 97, 0.477; 0.40: 67, 0.533; 0.45: 46, 0.581; 0.50: 32, 0.630; 0.55: 20, 0.654; 0.60: 12, 0.693; 0.65: 3, 0.653; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.338; 0.35: 13, 0.335; 0.40: 2, 0.400; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.165 | 2.28% | 0.917 | 0.483 | 0.251 | 0.433 | 0.470 |
| 6h | 18.857 | 2.00% | 0.894 | 0.517 | 0.251 | 0.499 | 0.406 |
| 24h | 24.021 | 4.44% | 0.897 | 0.494 | 0.250 | 0.520 | 0.632 |
| 7d | 16.819 | 5.88% | 0.899 | 0.500 | 0.250 | 0.514 | 0.667 |
| 30d | 16.122 | 4.78% | 0.900 | 0.500 | 0.250 | 0.504 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.658 | 21.689 | 21.571 | 21.156 | 21.940 | 21.542 | 20.978 | 20.911 | 21.126 | 21.165 |
| 6h | 19.243 | 19.024 | 19.005 | 18.819 | 19.137 | 19.125 | 18.711 | 18.820 | 18.804 | 18.857 |
| 24h | 25.137 | 24.255 | 24.162 | 24.048 | 24.415 | 24.392 | 24.040 | 24.013 | 24.000 | 24.021 |
| 7d | 17.869 | 16.983 | 16.971 | 16.953 | 17.166 | 17.202 | 16.796 | 16.771 | 16.790 | 16.819 |
| 30d | 16.931 | 16.290 | 16.232 | 16.177 | 16.425 | 16.400 | 16.107 | 16.089 | 16.093 | 16.122 |

## Next candle

- candle starting 2026-11-13 22:54 UTC, last close 1928.64
- P(up) 0.4993, return quantiles (bp): {'05': -9.451, '10': -6.599, '25': -3.88, '40': -1.638, '50': 0.014, '60': 1.256, '75': 3.411, '90': 6.362, '95': 8.738}
- changepoint probability 0.0548, regime age 39.1 min
- agent weights: empirical 0.005, ewma 0.065, garch 0.089, har 0.272, bocpd 0.031, hmm 0.037, online_qr 0.282, lgbm 0.219

## Learning log

- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- HMM volatility states (sd, bp per minute): [3.98, 6.75, 18.41], current probabilities: [0.196, 0.788, 0.016]
- live generator: {'versions': 60, 'latest_effective': '2026-11-13 23:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.275, 'l_abs': 0.599, 'l_hi': 0.782, 'l_lo': 0.727, 'b05': 0.698, 'b25': 0.66, 'b75': 0.626, 'b95': 0.689}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.601, 2.086, 1.899, 2.496, 2.113, 2.578, 3.113, 2.994, 2.919, 3.068, 3.921, 4.009, 4.795, 4.683]}
- calibration offsets (in sigma): {'05': 0.0065, '10': 0.043, '25': -0.0375, '40': -0.018, '50': 0.025, '60': 0.028, '75': 0.0175, '90': -0.023, '95': -0.0265}
