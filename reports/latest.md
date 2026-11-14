# ETH-USD 60s candle generator - report

- generated: 2026-11-14 09:50 UTC
- last closed candle: 2026-11-14 09:50 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k5_now 0.738 in the last 7 days, -0.081 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.529 (671) [0.498, 0.560] | 0.520 (2879) [0.503, 0.538] | 0.514 (7001) [0.503, 0.526] | 0.516 (4029) [0.500, 0.531] | 0.590 (39) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.539 (838) | 0.541 (5538) [0.532, 0.551] | 0.542 (23911) [0.536, 0.548] | 0.523 (57392) [0.517, 0.528] | 0.542 (33154) [0.538, 0.547] | 0.534 (339) | 0.500 | flat +0.007 (noise 0.013) |
| colour_confident | 0.556 (72) | 0.559 (910) [0.529, 0.577] | 0.586 (4289) [0.576, 0.597] | 0.591 (5897) [0.581, 0.602] | 0.591 (5897) [0.581, 0.602] | 0.692 (13) | 0.500 | flat -0.018 (noise 0.023) |
| colour_next | 0.527 (1434) | 0.530 (9971) [0.520, 0.540] | 0.530 (42869) [0.525, 0.534] | 0.517 (104302) [0.513, 0.521] | 0.529 (59953) [0.526, 0.533] | 0.547 (589) | 0.500 | flat -0.000 (noise 0.009) |
| colour_path | 0.499 (20076) | 0.501 (139594) [0.499, 0.504] | 0.502 (600166) [0.500, 0.503] | 0.501 (1460228) [0.500, 0.502] | 0.501 (839342) [0.500, 0.502] | 0.501 (8246) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.533 (15) | 0.623 (236) [0.558, 0.646] | 0.619 (1107) [0.602, 0.636] | 0.628 (1539) [0.612, 0.645] | 0.628 (1539) [0.612, 0.645] | 1.000 (1) | 0.500 | flat +0.012 (noise 0.047) |
| reversal_k13_next | 0.269 (52) | 0.326 (497) [0.300, 0.351] | 0.330 (1835) [0.316, 0.344] | 0.315 (4812) [0.305, 0.325] | 0.326 (2707) [0.315, 0.337] | 0.600 (15) | 0.077 | flat -0.045 (noise 0.033) |
| reversal_k13_now | 0.517 (58) | 0.561 (346) [0.535, 0.588] | 0.559 (1650) [0.540, 0.580] | 0.573 (3758) [0.560, 0.585] | 0.567 (2286) [0.551, 0.584] | 0.778 (18) | 0.077 | flat -0.025 (noise 0.036) |
| reversal_k3_next | 0.683 (41) | 0.617 (358) [0.584, 0.650] | 0.596 (2670) [0.584, 0.608] | 0.589 (6202) [0.580, 0.598] | 0.590 (3762) [0.579, 0.601] | 0.750 (12) | 0.293 | flat +0.006 (noise 0.032) |
| reversal_k3_now | 0.946 (56) | 0.920 (413) [0.909, 0.932] | 0.930 (1743) [0.920, 0.940] | 0.935 (4202) [0.929, 0.941] | 0.930 (2439) [0.922, 0.938] | 1.000 (24) | 0.293 | flat +0.005 (noise 0.019) |
| reversal_k5_next | 0.520 (75) | 0.500 (450) [0.465, 0.530] | 0.485 (2601) [0.469, 0.502] | 0.485 (5606) [0.474, 0.496] | 0.480 (3616) [0.466, 0.494] | 0.611 (18) | 0.186 | flat -0.039 (noise 0.034) |
| reversal_k5_now | 0.710 (69) | 0.738 (408) [0.699, 0.777] | 0.801 (1690) [0.783, 0.816] | 0.819 (3931) [0.808, 0.829] | 0.806 (2320) [0.792, 0.819] | 0.680 (25) | 0.187 | down -0.081 (noise 0.029) |
| reversal_k8_next | 0.364 (55) | 0.410 (475) [0.383, 0.438] | 0.398 (2596) [0.384, 0.412] | 0.397 (5693) [0.386, 0.407] | 0.397 (3587) [0.385, 0.408] | 0.556 (18) | 0.121 | flat -0.051 (noise 0.033) |
| reversal_k8_now | 0.597 (62) | 0.663 (371) [0.633, 0.694] | 0.680 (1545) [0.661, 0.699] | 0.698 (3802) [0.685, 0.710] | 0.686 (2215) [0.669, 0.702] | 0.778 (18) | 0.122 | flat -0.040 (noise 0.034) |
| overall | 0.503 (22074) | 0.505 (153554) [0.502, 0.507] | 0.505 (662244) [0.504, 0.507] | 0.504 (1609537) [0.503, 0.505] | 0.505 (926256) [0.504, 0.506] | 0.508 (9022) | - | flat -0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07366, 0.1135] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.529, 'levels': [{'threshold': 0.07366, 'calls_per_day': 140.7, 'win_rate': 0.5698}, {'threshold': 0.1135, 'calls_per_day': 34.9, 'win_rate': 0.6356}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42868, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15077 | 0.347 | 0.534 (14841) | 0.565 (2287) | 0.742 (2526) |
| volatility: normal | 15076 | 0.371 | 0.528 (15013) | 0.614 (1306) | 0.742 (2293) |
| volatility: wild | 15077 | 0.387 | 0.528 (15040) | 0.599 (776) | 0.762 (2058) |
| session: Asia 00-08 | 15360 | 0.368 | 0.535 (15237) | 0.589 (1541) | 0.752 (2296) |
| session: Europe 08-13 | 9410 | 0.362 | 0.532 (9329) | 0.588 (1132) | 0.746 (1549) |
| session: US 13-21 | 14880 | 0.375 | 0.530 (14782) | 0.597 (1162) | 0.748 (2249) |
| session: late 21-24 | 5580 | 0.361 | 0.516 (5546) | 0.549 (534) | 0.741 (783) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.379 | 0.362 | 0.259 | 0.259 | 0.583 | 0.283 | 0.476 | 0.974 |
| 6h | 360 | 0.394 | 0.372 | 0.296 | 0.334 | 0.557 | 0.280 | 0.509 | 1.184 |
| 24h | 1440 | 0.383 | 0.375 | 0.296 | 0.321 | 0.533 | 0.272 | 0.494 | 1.046 |
| 7d | 10080 | 0.371 | 0.366 | 0.285 | 0.315 | 0.531 | 0.268 | 0.474 | 1.266 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.530 | 0.265 | 0.471 | 1.254 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.379 / 0.583 / 0.850; 2: 0.375 / 0.567 / 0.783; 3: 0.340 / 0.417 / 0.850; 4: 0.342 / 0.433 / 0.917; 5: 0.330 / 0.400 / 0.867; 6: 0.355 / 0.483 / 0.867; 7: 0.398 / 0.633 / 0.933; 8: 0.365 / 0.533 / 0.917; 9: 0.363 / 0.550 / 0.917; 10: 0.386 / 0.550 / 0.967; 11: 0.381 / 0.583 / 0.933; 12: 0.383 / 0.567 / 0.950; 13: 0.363 / 0.500 / 0.933; 14: 0.353 / 0.500 / 0.967; 15: 0.382 / 0.583 / 0.950
- 6h: 1: 0.394 / 0.557 / 0.919; 2: 0.374 / 0.485 / 0.875; 3: 0.377 / 0.490 / 0.903; 4: 0.369 / 0.454 / 0.931; 5: 0.375 / 0.510 / 0.914; 6: 0.369 / 0.479 / 0.906; 7: 0.384 / 0.546 / 0.944; 8: 0.379 / 0.513 / 0.936; 9: 0.372 / 0.493 / 0.942; 10: 0.383 / 0.518 / 0.972; 11: 0.371 / 0.504 / 0.969; 12: 0.380 / 0.518 / 0.969; 13: 0.378 / 0.526 / 0.975; 14: 0.373 / 0.515 / 0.983; 15: 0.373 / 0.515 / 0.975
- 24h: 1: 0.383 / 0.533 / 0.892; 2: 0.368 / 0.489 / 0.892; 3: 0.377 / 0.520 / 0.894; 4: 0.361 / 0.467 / 0.903; 5: 0.371 / 0.508 / 0.897; 6: 0.363 / 0.477 / 0.897; 7: 0.371 / 0.518 / 0.903; 8: 0.372 / 0.518 / 0.899; 9: 0.362 / 0.483 / 0.900; 10: 0.370 / 0.502 / 0.903; 11: 0.368 / 0.522 / 0.909; 12: 0.367 / 0.500 / 0.906; 13: 0.367 / 0.505 / 0.913; 14: 0.364 / 0.507 / 0.911; 15: 0.366 / 0.505 / 0.908
- 7d: 1: 0.371 / 0.531 / 0.897; 2: 0.356 / 0.487 / 0.900; 3: 0.362 / 0.516 / 0.901; 4: 0.355 / 0.492 / 0.901; 5: 0.358 / 0.501 / 0.900; 6: 0.353 / 0.490 / 0.899; 7: 0.357 / 0.501 / 0.900; 8: 0.358 / 0.505 / 0.899; 9: 0.356 / 0.501 / 0.900; 10: 0.356 / 0.499 / 0.900; 11: 0.359 / 0.518 / 0.900; 12: 0.355 / 0.503 / 0.900; 13: 0.356 / 0.503 / 0.900; 14: 0.355 / 0.506 / 0.900; 15: 0.355 / 0.499 / 0.900
- 30d: 1: 0.368 / 0.530 / 0.897; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.352 / 0.499 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.353 / 0.502 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.503 / 0.900; 13: 0.351 / 0.499 / 0.901; 14: 0.351 / 0.502 / 0.900; 15: 0.351 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.123 (body 0.096, range 0.149); 'price stays where it was' would score 0.050; colour right 0.533; typical miss of the close 15.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.116; colour right 0.504; typical miss of the close 13.9 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.120 (body 0.080, range 0.160); 'price stays where it was' would score 0.128; colour right 0.507; typical miss of the close 14.2 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.123 (body 0.082, range 0.164); 'price stays where it was' would score 0.124; colour right 0.503; typical miss of the close 9.8 bp; chain ended on the right side 0.534 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.0 bp; chain ended on the right side 0.521 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.204 / 5.5; 3: 0.168 / 7.2; 4: 0.134 / 7.3; 5: 0.125 / 8.1; 6: 0.117 / 9.0; 7: 0.109 / 9.2; 8: 0.097 / 10.2; 9: 0.091 / 10.5; 10: 0.091 / 10.7; 11: 0.089 / 10.9; 12: 0.079 / 11.3; 13: 0.073 / 11.8; 14: 0.069 / 12.3; 15: 0.066 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 148664, probability skill vs chance 0.2372, widened contest next: False
  - now: threshold 0.8394, hit rate recent 0.9452 / long run 0.9277
    - 6h: 15 calls (61 a day), hit rate 1.000, chance 0.300, naive rule 0.542, lift 3.33x
    - 24h: 55 calls (55 a day), hit rate 0.945, chance 0.295, naive rule 0.508, lift 3.21x
    - 7d: 417 calls (60 a day), hit rate 0.921, chance 0.290, naive rule 0.498, lift 3.17x
    - 30d: 1750 calls (58 a day), hit rate 0.931, chance 0.293, naive rule 0.496, lift 3.17x
  - next: threshold 0.567, hit rate recent 0.6746 / long run 0.6152
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.300, lift 2.59x
    - 24h: 36 calls (36 a day), hit rate 0.722, chance 0.295, lift 2.45x
    - 7d: 342 calls (49 a day), hit rate 0.617, chance 0.290, lift 2.13x
    - 30d: 2649 calls (88 a day), hit rate 0.597, chance 0.293, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.694; 0.55: 310, 0.738; 0.60: 260, 0.783; 0.65: 220, 0.811; 0.70: 172, 0.843; 0.75: 139, 0.873; 0.80: 92, 0.905; 0.85: 46, 0.944; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.431; 0.35: 496, 0.465; 0.40: 396, 0.503; 0.45: 298, 0.537; 0.50: 190, 0.570; 0.55: 84, 0.583; 0.60: 11, 0.661; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 148662, probability skill vs chance 0.217, widened contest next: True
  - now: threshold 0.6922, hit rate recent 0.7051 / long run 0.7746
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.166, naive rule 0.380, lift 4.53x
    - 24h: 64 calls (64 a day), hit rate 0.672, chance 0.174, naive rule 0.391, lift 3.86x
    - 7d: 418 calls (60 a day), hit rate 0.732, chance 0.183, naive rule 0.400, lift 4.01x
    - 30d: 1697 calls (57 a day), hit rate 0.800, chance 0.186, naive rule 0.405, lift 4.31x
  - next: threshold 0.4483, hit rate recent 0.5309 / long run 0.5092
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.166, lift 3.29x
    - 24h: 69 calls (69 a day), hit rate 0.580, chance 0.174, lift 3.33x
    - 7d: 440 calls (63 a day), hit rate 0.505, chance 0.183, lift 2.76x
    - 30d: 2569 calls (86 a day), hit rate 0.486, chance 0.186, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.418; 0.35: 356, 0.477; 0.40: 288, 0.547; 0.45: 234, 0.603; 0.50: 187, 0.650; 0.55: 149, 0.689; 0.60: 112, 0.737; 0.65: 77, 0.774; 0.70: 48, 0.809; 0.75: 28, 0.842; 0.80: 9, 0.874
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.383; 0.35: 256, 0.423; 0.40: 161, 0.456; 0.45: 65, 0.496; 0.50: 10, 0.529; 0.55: 1, 0.444
- **K=8**: model 1794614400, labels learned 148659, probability skill vs chance 0.2122, widened contest next: False
  - now: threshold 0.5711, hit rate recent 0.6596 / long run 0.6808
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.124, naive rule 0.348, lift 8.05x
    - 24h: 53 calls (53 a day), hit rate 0.623, chance 0.119, naive rule 0.330, lift 5.25x
    - 7d: 373 calls (53 a day), hit rate 0.673, chance 0.123, naive rule 0.341, lift 5.49x
    - 30d: 1546 calls (52 a day), hit rate 0.681, chance 0.121, naive rule 0.335, lift 5.65x
  - next: threshold 0.3705, hit rate recent 0.4406 / long run 0.4228
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.124, lift 4.02x
    - 24h: 59 calls (59 a day), hit rate 0.441, chance 0.119, lift 3.72x
    - 7d: 470 calls (67 a day), hit rate 0.417, chance 0.123, lift 3.40x
    - 30d: 2578 calls (86 a day), hit rate 0.399, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.426; 0.35: 194, 0.488; 0.40: 154, 0.532; 0.45: 118, 0.579; 0.50: 84, 0.636; 0.55: 59, 0.669; 0.60: 40, 0.709; 0.65: 24, 0.769; 0.70: 11, 0.814; 0.75: 2, 0.779
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 168, 0.365; 0.35: 85, 0.391; 0.40: 23, 0.424; 0.45: 4, 0.413; 0.50: 1, 0.783
- **K=13**: model 1794614400, labels learned 148654, probability skill vs chance 0.1947, widened contest next: False
  - now: threshold 0.4477, hit rate recent 0.6118 / long run 0.5744
    - 6h: 9 calls (38 a day), hit rate 1.000, chance 0.091, naive rule 0.356, lift 10.95x
    - 24h: 52 calls (53 a day), hit rate 0.577, chance 0.082, naive rule 0.315, lift 7.00x
    - 7d: 346 calls (50 a day), hit rate 0.584, chance 0.080, naive rule 0.299, lift 7.28x
    - 30d: 1645 calls (55 a day), hit rate 0.562, chance 0.078, naive rule 0.284, lift 7.23x
  - next: threshold 0.2981, hit rate recent 0.3674 / long run 0.339
    - 6h: 10 calls (42 a day), hit rate 0.500, chance 0.091, lift 5.48x
    - 24h: 54 calls (55 a day), hit rate 0.370, chance 0.082, lift 4.49x
    - 7d: 484 calls (69 a day), hit rate 0.341, chance 0.080, lift 4.25x
    - 30d: 1830 calls (61 a day), hit rate 0.332, chance 0.078, lift 4.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.430; 0.35: 97, 0.477; 0.40: 68, 0.536; 0.45: 47, 0.583; 0.50: 32, 0.632; 0.55: 21, 0.655; 0.60: 12, 0.696; 0.65: 3, 0.650; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.340; 0.35: 13, 0.335; 0.40: 2, 0.397; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 19.416 | -1.81% | 0.850 | 0.500 | 0.250 | 0.533 | -0.015 |
| 6h | 19.665 | 0.54% | 0.914 | 0.517 | 0.250 | 0.504 | 0.499 |
| 24h | 22.362 | 3.43% | 0.896 | 0.503 | 0.250 | 0.507 | 0.653 |
| 7d | 17.838 | 5.27% | 0.900 | 0.499 | 0.250 | 0.512 | 0.660 |
| 30d | 16.084 | 4.76% | 0.900 | 0.500 | 0.250 | 0.504 | 0.698 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.071 | 19.261 | 19.148 | 19.564 | 19.066 | 19.061 | 19.361 | 19.464 | 19.291 | 19.416 |
| 6h | 19.772 | 19.714 | 19.629 | 19.861 | 19.932 | 19.730 | 19.658 | 19.647 | 19.629 | 19.665 |
| 24h | 23.157 | 22.603 | 22.465 | 22.356 | 22.800 | 22.598 | 22.328 | 22.334 | 22.319 | 22.362 |
| 7d | 18.831 | 18.017 | 17.976 | 17.977 | 18.214 | 18.186 | 17.816 | 17.786 | 17.808 | 17.838 |
| 30d | 16.889 | 16.246 | 16.196 | 16.142 | 16.392 | 16.356 | 16.069 | 16.050 | 16.056 | 16.084 |

## Next candle

- candle starting 2026-11-14 09:50 UTC, last close 1912.76
- P(up) 0.4982, return quantiles (bp): {'05': -13.965, '10': -10.398, '25': -5.518, '40': -2.241, '50': -0.038, '60': 2.146, '75': 5.232, '90': 9.774, '95': 13.805}
- changepoint probability 0.0559, regime age 203.1 min
- agent weights: empirical 0.009, ewma 0.076, garch 0.172, har 0.134, bocpd 0.024, hmm 0.082, online_qr 0.238, lgbm 0.265

## Learning log

- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.3, 7.03, 18.51], current probabilities: [0.035, 0.871, 0.095]
- live generator: {'versions': 60, 'latest_effective': '2026-11-14 10:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.219, 'l_abs': 0.63, 'l_hi': 0.774, 'l_lo': 0.715, 'b05': 0.729, 'b25': 0.723, 'b75': 0.669, 'b95': 0.72}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.431, 1.589, 1.697, 2.06, 2.401, 2.17, 2.372, 2.471, 2.458, 2.433, 2.65, 2.551, 2.761, 2.863]}
- calibration offsets (in sigma): {'05': 0.0245, '10': -0.001, '25': 0.0025, '40': 0.026, '50': 0.055, '60': 0.054, '75': 0.0275, '90': -0.059, '95': -0.0545}
