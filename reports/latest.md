# ETH-USD 60s candle generator - report

- generated: 2026-11-16 04:05 UTC
- last closed candle: 2026-11-16 04:05 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: colour_confident 0.530 in the last 7 days, -0.051 against the 7 before
- WIN RATE FALLING: reversal_k5_now 0.743 in the last 7 days, -0.065 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.438 (96) | 0.522 (671) [0.482, 0.560] | 0.518 (2879) [0.501, 0.536] | 0.514 (7193) [0.502, 0.525] | 0.515 (4221) [0.500, 0.531] | 0.625 (16) | 0.500 | flat +0.022 (noise 0.030) |
| colour_clear | 0.549 (780) | 0.539 (5614) [0.531, 0.547] | 0.543 (23916) [0.538, 0.549] | 0.524 (58973) [0.519, 0.529] | 0.543 (34735) [0.538, 0.547] | 0.558 (156) | 0.500 | flat +0.003 (noise 0.012) |
| colour_confident | 0.512 (207) | 0.530 (606) [0.505, 0.566] | 0.582 (4371) [0.570, 0.593] | 0.588 (6151) [0.577, 0.599] | 0.588 (6151) [0.577, 0.599] | 0.645 (31) | 0.500 | down -0.051 (noise 0.025) |
| colour_next | 0.540 (1436) | 0.529 (10053) [0.521, 0.536] | 0.531 (42875) [0.527, 0.535] | 0.518 (107177) [0.514, 0.522] | 0.530 (62828) [0.526, 0.533] | 0.576 (245) | 0.500 | flat -0.003 (noise 0.009) |
| colour_path | 0.505 (20104) | 0.502 (140742) [0.499, 0.504] | 0.501 (600250) [0.500, 0.503] | 0.501 (1500478) [0.500, 0.502] | 0.501 (879592) [0.500, 0.502] | 0.519 (3430) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.589 (56) | 0.579 (107) [0.500, 0.632] | 0.615 (1133) [0.600, 0.631] | 0.627 (1598) [0.611, 0.643] | 0.627 (1598) [0.611, 0.643] | 0.692 (13) | 0.500 | flat -0.043 (noise 0.056) |
| reversal_k13_next | 0.302 (63) | 0.352 (438) [0.323, 0.384] | 0.333 (1832) [0.318, 0.349] | 0.316 (4922) [0.306, 0.326] | 0.328 (2817) [0.317, 0.339] | 0.167 (12) | 0.077 | flat +0.017 (noise 0.032) |
| reversal_k13_now | 0.633 (49) | 0.604 (338) [0.560, 0.655] | 0.570 (1624) [0.549, 0.591] | 0.576 (3855) [0.563, 0.588] | 0.572 (2383) [0.556, 0.589] | 0.667 (6) | 0.077 | flat +0.039 (noise 0.037) |
| reversal_k3_next | 0.571 (35) | 0.623 (300) [0.580, 0.673] | 0.600 (2515) [0.588, 0.613] | 0.590 (6264) [0.581, 0.598] | 0.591 (3824) [0.580, 0.602] | 0.571 (14) | 0.293 | flat -0.000 (noise 0.036) |
| reversal_k3_now | 0.933 (45) | 0.924 (396) [0.914, 0.935] | 0.929 (1740) [0.920, 0.939] | 0.935 (4304) [0.929, 0.941] | 0.930 (2541) [0.923, 0.938] | 0.889 (9) | 0.293 | flat +0.007 (noise 0.019) |
| reversal_k5_next | 0.456 (57) | 0.506 (415) [0.461, 0.557] | 0.494 (2491) [0.477, 0.512] | 0.487 (5716) [0.476, 0.498] | 0.483 (3726) [0.469, 0.498] | 0.462 (13) | 0.187 | flat -0.024 (noise 0.035) |
| reversal_k5_now | 0.809 (63) | 0.743 (432) [0.701, 0.783] | 0.798 (1701) [0.782, 0.813] | 0.818 (4059) [0.808, 0.828] | 0.806 (2448) [0.792, 0.818] | 0.727 (11) | 0.187 | down -0.065 (noise 0.029) |
| reversal_k8_next | 0.353 (68) | 0.438 (450) [0.401, 0.479] | 0.406 (2507) [0.392, 0.421] | 0.398 (5817) [0.388, 0.408] | 0.399 (3711) [0.386, 0.411] | 0.455 (11) | 0.121 | flat +0.022 (noise 0.034) |
| reversal_k8_now | 0.603 (58) | 0.667 (372) [0.627, 0.720] | 0.683 (1548) [0.662, 0.702] | 0.698 (3906) [0.684, 0.711] | 0.686 (2319) [0.669, 0.703] | 0.625 (8) | 0.122 | flat -0.022 (noise 0.035) |
| overall | 0.508 (22074) | 0.506 (154607) [0.504, 0.508] | 0.505 (661962) [0.504, 0.507] | 0.504 (1653691) [0.503, 0.505] | 0.505 (970410) [0.504, 0.506] | 0.524 (3775) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06386, 0.09354] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5283, 'levels': [{'threshold': 0.06386, 'calls_per_day': 139.5, 'win_rate': 0.5455}, {'threshold': 0.09354, 'calls_per_day': 32.3, 'win_rate': 0.5683}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42876, 'rate': 0.5314}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14962 | 0.347 | 0.534 (14726) | 0.564 (2273) | 0.743 (2503) |
| volatility: normal | 14961 | 0.372 | 0.529 (14901) | 0.614 (1322) | 0.745 (2308) |
| volatility: wild | 14962 | 0.389 | 0.531 (14926) | 0.584 (895) | 0.764 (2088) |
| session: Asia 00-08 | 15125 | 0.368 | 0.534 (15005) | 0.582 (1609) | 0.749 (2279) |
| session: Europe 08-13 | 9300 | 0.362 | 0.530 (9220) | 0.588 (1116) | 0.747 (1523) |
| session: US 13-21 | 14880 | 0.376 | 0.534 (14783) | 0.600 (1203) | 0.754 (2276) |
| session: late 21-24 | 5580 | 0.363 | 0.517 (5545) | 0.537 (562) | 0.748 (821) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.368 | 0.372 | 0.345 | 0.345 | 0.517 | 0.258 | 0.477 | 1.117 |
| 6h | 360 | 0.391 | 0.380 | 0.319 | 0.368 | 0.546 | 0.277 | 0.505 | 1.185 |
| 24h | 1440 | 0.388 | 0.377 | 0.295 | 0.333 | 0.551 | 0.277 | 0.499 | 1.276 |
| 7d | 10080 | 0.383 | 0.378 | 0.297 | 0.328 | 0.529 | 0.272 | 0.495 | 1.164 |
| 30d | 43200 | 0.369 | 0.362 | 0.280 | 0.311 | 0.531 | 0.266 | 0.472 | 1.243 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.368 / 0.517 / 0.900; 2: 0.360 / 0.483 / 0.933; 3: 0.356 / 0.500 / 0.933; 4: 0.372 / 0.550 / 0.933; 5: 0.333 / 0.417 / 1.000; 6: 0.365 / 0.517 / 1.000; 7: 0.380 / 0.550 / 1.000; 8: 0.327 / 0.350 / 0.967; 9: 0.368 / 0.567 / 0.983; 10: 0.368 / 0.550 / 1.000; 11: 0.369 / 0.550 / 1.000; 12: 0.378 / 0.567 / 1.000; 13: 0.350 / 0.500 / 1.000; 14: 0.364 / 0.500 / 1.000; 15: 0.376 / 0.483 / 1.000
- 6h: 1: 0.391 / 0.546 / 0.906; 2: 0.393 / 0.518 / 0.919; 3: 0.395 / 0.532 / 0.922; 4: 0.386 / 0.499 / 0.906; 5: 0.377 / 0.460 / 0.933; 6: 0.391 / 0.532 / 0.933; 7: 0.393 / 0.526 / 0.939; 8: 0.379 / 0.482 / 0.922; 9: 0.390 / 0.535 / 0.939; 10: 0.389 / 0.535 / 0.939; 11: 0.388 / 0.529 / 0.936; 12: 0.387 / 0.524 / 0.933; 13: 0.380 / 0.504 / 0.933; 14: 0.389 / 0.535 / 0.942; 15: 0.390 / 0.535 / 0.936
- 24h: 1: 0.388 / 0.551 / 0.906; 2: 0.374 / 0.500 / 0.902; 3: 0.378 / 0.522 / 0.904; 4: 0.371 / 0.496 / 0.901; 5: 0.369 / 0.490 / 0.903; 6: 0.377 / 0.529 / 0.900; 7: 0.369 / 0.499 / 0.902; 8: 0.372 / 0.510 / 0.903; 9: 0.369 / 0.507 / 0.906; 10: 0.373 / 0.519 / 0.908; 11: 0.371 / 0.502 / 0.908; 12: 0.370 / 0.513 / 0.904; 13: 0.367 / 0.503 / 0.906; 14: 0.372 / 0.512 / 0.907; 15: 0.371 / 0.506 / 0.901
- 7d: 1: 0.383 / 0.529 / 0.901; 2: 0.368 / 0.489 / 0.899; 3: 0.376 / 0.517 / 0.900; 4: 0.368 / 0.491 / 0.899; 5: 0.370 / 0.500 / 0.900; 6: 0.368 / 0.498 / 0.899; 7: 0.370 / 0.503 / 0.899; 8: 0.371 / 0.509 / 0.899; 9: 0.367 / 0.498 / 0.899; 10: 0.370 / 0.507 / 0.899; 11: 0.371 / 0.515 / 0.899; 12: 0.367 / 0.500 / 0.898; 13: 0.368 / 0.505 / 0.898; 14: 0.366 / 0.502 / 0.899; 15: 0.367 / 0.500 / 0.898
- 30d: 1: 0.369 / 0.531 / 0.897; 2: 0.355 / 0.492 / 0.900; 3: 0.359 / 0.512 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.503 / 0.900; 6: 0.353 / 0.500 / 0.900; 7: 0.354 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.501 / 0.900; 10: 0.354 / 0.503 / 0.900; 11: 0.353 / 0.504 / 0.900; 12: 0.353 / 0.503 / 0.900; 13: 0.352 / 0.499 / 0.900; 14: 0.352 / 0.502 / 0.900; 15: 0.352 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.063 (body 0.024, range 0.103); 'price stays where it was' would score 0.140; colour right 0.467; typical miss of the close 18.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.110 (body 0.064, range 0.157); 'price stays where it was' would score 0.126; colour right 0.515; typical miss of the close 17.5 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.122 (body 0.074, range 0.169); 'price stays where it was' would score 0.131; colour right 0.498; typical miss of the close 16.8 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.126 (body 0.083, range 0.169); 'price stays where it was' would score 0.127; colour right 0.504; typical miss of the close 13.5 bp; chain ended on the right side 0.522 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.3 bp; chain ended on the right side 0.519 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.8; 2: 0.203 / 5.6; 3: 0.169 / 7.5; 4: 0.133 / 7.6; 5: 0.126 / 8.3; 6: 0.119 / 9.2; 7: 0.110 / 9.5; 8: 0.098 / 10.4; 9: 0.092 / 10.8; 10: 0.092 / 11.1; 11: 0.087 / 11.2; 12: 0.078 / 11.7; 13: 0.074 / 12.2; 14: 0.069 / 12.6; 15: 0.068 / 13.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 151199, probability skill vs chance 0.2297, widened contest next: False
  - now: threshold 0.8372, hit rate recent 0.9291 / long run 0.9266
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.279, naive rule 0.478, lift 3.33x
    - 24h: 47 calls (47 a day), hit rate 0.936, chance 0.293, naive rule 0.502, lift 3.20x
    - 7d: 396 calls (57 a day), hit rate 0.924, chance 0.288, naive rule 0.499, lift 3.21x
    - 30d: 1736 calls (58 a day), hit rate 0.931, chance 0.294, naive rule 0.499, lift 3.17x
  - next: threshold 0.553, hit rate recent 0.628 / long run 0.616
    - 6h: 17 calls (69 a day), hit rate 0.529, chance 0.279, lift 1.90x
    - 24h: 46 calls (46 a day), hit rate 0.565, chance 0.293, lift 1.93x
    - 7d: 309 calls (44 a day), hit rate 0.621, chance 0.288, lift 2.16x
    - 30d: 2499 calls (83 a day), hit rate 0.599, chance 0.294, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.501; 0.35: 531, 0.526; 0.40: 474, 0.580; 0.45: 406, 0.649; 0.50: 357, 0.694; 0.55: 310, 0.738; 0.60: 260, 0.783; 0.65: 220, 0.812; 0.70: 172, 0.844; 0.75: 138, 0.875; 0.80: 91, 0.906; 0.85: 46, 0.940; 0.90: 4, 0.970
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.433; 0.35: 495, 0.466; 0.40: 394, 0.505; 0.45: 295, 0.539; 0.50: 188, 0.572; 0.55: 82, 0.585; 0.60: 11, 0.655; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 151197, probability skill vs chance 0.2243, widened contest next: False
  - now: threshold 0.6948, hit rate recent 0.7958 / long run 0.7803
    - 6h: 18 calls (73 a day), hit rate 0.778, chance 0.178, naive rule 0.366, lift 4.36x
    - 24h: 64 calls (64 a day), hit rate 0.812, chance 0.190, naive rule 0.420, lift 4.28x
    - 7d: 438 calls (63 a day), hit rate 0.747, chance 0.184, naive rule 0.407, lift 4.07x
    - 30d: 1706 calls (57 a day), hit rate 0.798, chance 0.186, naive rule 0.408, lift 4.28x
  - next: threshold 0.4561, hit rate recent 0.5221 / long run 0.5141
    - 6h: 18 calls (73 a day), hit rate 0.500, chance 0.178, lift 2.80x
    - 24h: 61 calls (61 a day), hit rate 0.492, chance 0.190, lift 2.59x
    - 7d: 422 calls (60 a day), hit rate 0.502, chance 0.184, lift 2.74x
    - 30d: 2485 calls (83 a day), hit rate 0.493, chance 0.186, lift 2.65x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.421; 0.35: 357, 0.477; 0.40: 289, 0.547; 0.45: 234, 0.605; 0.50: 186, 0.652; 0.55: 149, 0.691; 0.60: 112, 0.739; 0.65: 77, 0.776; 0.70: 48, 0.809; 0.75: 28, 0.843; 0.80: 8, 0.870
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 343, 0.385; 0.35: 255, 0.425; 0.40: 161, 0.458; 0.45: 65, 0.505; 0.50: 9, 0.554; 0.55: 1, 0.433
- **K=8**: model 1794787200, labels learned 151194, probability skill vs chance 0.2161, widened contest next: False
  - now: threshold 0.5675, hit rate recent 0.6672 / long run 0.6805
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.133, naive rule 0.371, lift 5.38x
    - 24h: 59 calls (59 a day), hit rate 0.610, chance 0.127, naive rule 0.373, lift 4.79x
    - 7d: 373 calls (53 a day), hit rate 0.670, chance 0.124, naive rule 0.355, lift 5.42x
    - 30d: 1550 calls (52 a day), hit rate 0.683, chance 0.121, naive rule 0.340, lift 5.63x
  - next: threshold 0.3703, hit rate recent 0.4214 / long run 0.4246
    - 6h: 17 calls (70 a day), hit rate 0.471, chance 0.133, lift 3.54x
    - 24h: 71 calls (71 a day), hit rate 0.380, chance 0.127, lift 2.99x
    - 7d: 451 calls (64 a day), hit rate 0.437, chance 0.124, lift 3.53x
    - 30d: 2499 calls (83 a day), hit rate 0.405, chance 0.121, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.428; 0.35: 194, 0.491; 0.40: 153, 0.536; 0.45: 117, 0.580; 0.50: 83, 0.640; 0.55: 59, 0.672; 0.60: 40, 0.713; 0.65: 23, 0.770; 0.70: 11, 0.813; 0.75: 2, 0.766
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 165, 0.369; 0.35: 84, 0.398; 0.40: 24, 0.431; 0.45: 5, 0.449; 0.50: 1, 0.783
- **K=13**: model 1794700800, labels learned 151189, probability skill vs chance 0.1995, widened contest next: False
  - now: threshold 0.4441, hit rate recent 0.6563 / long run 0.5871
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.091, naive rule 0.347, lift 7.58x
    - 24h: 46 calls (46 a day), hit rate 0.674, chance 0.083, naive rule 0.336, lift 8.10x
    - 7d: 335 calls (48 a day), hit rate 0.612, chance 0.081, naive rule 0.315, lift 7.51x
    - 30d: 1621 calls (54 a day), hit rate 0.571, chance 0.078, naive rule 0.289, lift 7.31x
  - next: threshold 0.2979, hit rate recent 0.3138 / long run 0.3352
    - 6h: 19 calls (79 a day), hit rate 0.316, chance 0.091, lift 3.46x
    - 24h: 66 calls (67 a day), hit rate 0.288, chance 0.083, lift 3.46x
    - 7d: 435 calls (62 a day), hit rate 0.352, chance 0.081, lift 4.32x
    - 30d: 1837 calls (61 a day), hit rate 0.330, chance 0.078, lift 4.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.432; 0.35: 97, 0.480; 0.40: 67, 0.541; 0.45: 46, 0.591; 0.50: 32, 0.635; 0.55: 20, 0.658; 0.60: 11, 0.699; 0.65: 3, 0.638; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.338; 0.35: 13, 0.344; 0.40: 2, 0.432; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 22.521 | -0.31% | 0.883 | 0.500 | 0.251 | 0.483 | -0.028 |
| 6h | 24.239 | 1.33% | 0.883 | 0.458 | 0.251 | 0.479 | 0.461 |
| 24h | 24.581 | 4.02% | 0.899 | 0.494 | 0.250 | 0.499 | 0.467 |
| 7d | 22.892 | 4.58% | 0.901 | 0.499 | 0.250 | 0.512 | 0.655 |
| 30d | 16.894 | 4.81% | 0.900 | 0.500 | 0.250 | 0.505 | 0.714 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 22.451 | 22.430 | 22.343 | 22.477 | 22.712 | 22.676 | 22.557 | 22.484 | 22.449 | 22.521 |
| 6h | 24.564 | 24.232 | 24.226 | 24.178 | 24.609 | 24.433 | 24.269 | 24.220 | 24.171 | 24.239 |
| 24h | 25.610 | 24.801 | 24.747 | 24.528 | 25.191 | 24.850 | 24.551 | 24.530 | 24.535 | 24.581 |
| 7d | 23.992 | 23.098 | 23.074 | 22.973 | 23.417 | 23.216 | 22.881 | 22.844 | 22.855 | 22.892 |
| 30d | 17.748 | 17.057 | 17.015 | 16.951 | 17.232 | 17.179 | 16.878 | 16.857 | 16.864 | 16.894 |

## Next candle

- candle starting 2026-11-16 04:05 UTC, last close 1819.58
- P(up) 0.4949, return quantiles (bp): {'05': -14.957, '10': -11.366, '25': -6.158, '40': -2.009, '50': -0.136, '60': 2.392, '75': 6.445, '90': 10.965, '95': 14.575}
- changepoint probability 0.0573, regime age 226.2 min
- agent weights: empirical 0.007, ewma 0.131, garch 0.134, har 0.216, bocpd 0.027, hmm 0.066, online_qr 0.188, lgbm 0.231

## Learning log

- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- 2026-11-15 00:00 UTC: {"garch": {"alpha": 0.0722, "beta": 0.9208}, "hmm": {"sd_bp": [5.05, 9.08, 23.18], "stay": [0.988, 0.959, 0.927]}, "lgbm": {"challenger_loss": 0.2563, "champion_loss": 0.25627, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46882, "challengers": 1, "chance_loss": 0.59699, "widened": false, "champion_loss": 0.46615, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35622, "challengers": 1, "chance_loss": 0.46954, "widened": false, "champion_loss": 0.35476, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2677, "challengers": 1, "chance_loss": 0.36962, "widened": false, "champion_loss": 0.26742, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19834, "challengers": 1, "chance_loss": 0.28444, "widened": false, "champion_loss": 0.19917, "promoted": true}}
- 2026-11-15 12:00 UTC: {"garch": {"alpha": 0.0709, "beta": 0.9226}, "hmm": {"sd_bp": [5.18, 9.59, 24.41], "stay": [0.986, 0.96, 0.919]}}
- 2026-11-16 00:00 UTC: {"garch": {"alpha": 0.0649, "beta": 0.9281}, "hmm": {"sd_bp": [5.12, 9.52, 24.14], "stay": [0.982, 0.963, 0.92]}, "lgbm": {"challenger_loss": 0.24944, "champion_loss": 0.2494, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47719, "challengers": 1, "chance_loss": 0.60563, "widened": false, "champion_loss": 0.47655, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3653, "challengers": 1, "chance_loss": 0.4822, "widened": false, "champion_loss": 0.36306, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2714, "challengers": 1, "chance_loss": 0.37579, "widened": false, "champion_loss": 0.27207, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19602, "challengers": 1, "chance_loss": 0.28273, "widened": false, "champion_loss": 0.19594, "promoted": false}}
- HMM volatility states (sd, bp per minute): [5.12, 9.52, 24.14], current probabilities: [0.001, 0.892, 0.107]
- live generator: {'versions': 60, 'latest_effective': '2026-11-16 04:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.34, 'l_abs': 0.764, 'l_hi': 0.746, 'l_lo': 0.712, 'b05': 0.748, 'b25': 0.767, 'b75': 0.71, 'b95': 0.752}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.389, 1.671, 2.012, 2.081, 2.377, 2.678, 2.756, 2.929, 3.093, 3.251, 3.836, 3.768, 3.764, 4.315]}
- calibration offsets (in sigma): {'05': 0.052, '10': 0.004, '25': -0.03, '40': 0.016, '50': -0.02, '60': 0.014, '75': 0.05, '90': -0.024, '95': -0.052}
