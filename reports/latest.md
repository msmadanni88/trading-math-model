# ETH-USD 60s candle generator - report

- generated: 2026-11-14 02:54 UTC
- last closed candle: 2026-11-14 02:54 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k5_now 0.738 in the last 7 days, -0.081 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.529 (671) [0.498, 0.560] | 0.520 (2879) [0.503, 0.538] | 0.514 (7001) [0.503, 0.526] | 0.516 (4029) [0.500, 0.531] | 0.545 (11) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.539 (838) | 0.541 (5538) [0.532, 0.551] | 0.542 (23911) [0.536, 0.548] | 0.523 (57392) [0.517, 0.528] | 0.542 (33154) [0.538, 0.547] | 0.513 (113) | 0.500 | flat +0.007 (noise 0.013) |
| colour_confident | 0.556 (72) | 0.559 (910) [0.529, 0.577] | 0.586 (4289) [0.576, 0.597] | 0.591 (5897) [0.581, 0.602] | 0.591 (5897) [0.581, 0.602] | 0.600 (5) | 0.500 | flat -0.018 (noise 0.023) |
| colour_next | 0.527 (1434) | 0.530 (9971) [0.520, 0.540] | 0.530 (42869) [0.525, 0.534] | 0.517 (104302) [0.513, 0.521] | 0.529 (59953) [0.526, 0.533] | 0.552 (174) | 0.500 | flat -0.000 (noise 0.009) |
| colour_path | 0.499 (20076) | 0.501 (139594) [0.499, 0.504] | 0.502 (600166) [0.500, 0.503] | 0.501 (1460228) [0.500, 0.502] | 0.501 (839342) [0.500, 0.502] | 0.497 (2436) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.533 (15) | 0.623 (236) [0.558, 0.646] | 0.619 (1107) [0.602, 0.636] | 0.628 (1539) [0.612, 0.645] | 0.628 (1539) [0.612, 0.645] | - | 0.500 | flat +0.012 (noise 0.047) |
| reversal_k13_next | 0.269 (52) | 0.326 (497) [0.300, 0.351] | 0.330 (1835) [0.316, 0.344] | 0.315 (4812) [0.305, 0.325] | 0.326 (2707) [0.315, 0.337] | 0.667 (3) | 0.077 | flat -0.045 (noise 0.033) |
| reversal_k13_now | 0.517 (58) | 0.561 (346) [0.535, 0.588] | 0.559 (1650) [0.540, 0.580] | 0.573 (3758) [0.560, 0.585] | 0.567 (2286) [0.551, 0.584] | 0.429 (7) | 0.077 | flat -0.025 (noise 0.036) |
| reversal_k3_next | 0.683 (41) | 0.617 (358) [0.584, 0.650] | 0.596 (2670) [0.584, 0.608] | 0.589 (6202) [0.580, 0.598] | 0.590 (3762) [0.579, 0.601] | 0.667 (3) | 0.293 | flat +0.006 (noise 0.032) |
| reversal_k3_now | 0.946 (56) | 0.920 (413) [0.909, 0.932] | 0.930 (1743) [0.920, 0.940] | 0.935 (4202) [0.929, 0.941] | 0.930 (2439) [0.922, 0.938] | 1.000 (7) | 0.293 | flat +0.005 (noise 0.019) |
| reversal_k5_next | 0.520 (75) | 0.500 (450) [0.465, 0.530] | 0.485 (2601) [0.469, 0.502] | 0.485 (5606) [0.474, 0.496] | 0.480 (3616) [0.466, 0.494] | 0.500 (4) | 0.186 | flat -0.039 (noise 0.034) |
| reversal_k5_now | 0.710 (69) | 0.738 (408) [0.699, 0.777] | 0.801 (1690) [0.783, 0.816] | 0.819 (3931) [0.808, 0.829] | 0.806 (2320) [0.792, 0.819] | 0.500 (10) | 0.187 | down -0.081 (noise 0.029) |
| reversal_k8_next | 0.364 (55) | 0.410 (475) [0.383, 0.438] | 0.398 (2596) [0.384, 0.412] | 0.397 (5693) [0.386, 0.407] | 0.397 (3587) [0.385, 0.408] | 0.500 (2) | 0.121 | flat -0.051 (noise 0.033) |
| reversal_k8_now | 0.597 (62) | 0.663 (371) [0.633, 0.694] | 0.680 (1545) [0.661, 0.699] | 0.698 (3802) [0.685, 0.710] | 0.686 (2215) [0.669, 0.702] | 0.429 (7) | 0.122 | flat -0.040 (noise 0.034) |
| overall | 0.503 (22074) | 0.505 (153554) [0.502, 0.507] | 0.505 (662244) [0.504, 0.507] | 0.504 (1609537) [0.503, 0.505] | 0.505 (926256) [0.504, 0.506] | 0.502 (2664) | - | flat -0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07436, 0.1143] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5295, 'levels': [{'threshold': 0.07436, 'calls_per_day': 141.6, 'win_rate': 0.5679}, {'threshold': 0.1143, 'calls_per_day': 35.2, 'win_rate': 0.6185}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42868, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14938 | 0.347 | 0.534 (14702) | 0.566 (2273) | 0.740 (2495) |
| volatility: normal | 14938 | 0.371 | 0.529 (14876) | 0.613 (1307) | 0.743 (2280) |
| volatility: wild | 14938 | 0.387 | 0.527 (14901) | 0.598 (781) | 0.758 (2048) |
| session: Asia 00-08 | 15054 | 0.368 | 0.535 (14931) | 0.588 (1535) | 0.749 (2255) |
| session: Europe 08-13 | 9300 | 0.362 | 0.532 (9220) | 0.588 (1130) | 0.745 (1536) |
| session: US 13-21 | 14880 | 0.375 | 0.530 (14782) | 0.597 (1162) | 0.748 (2249) |
| session: late 21-24 | 5580 | 0.361 | 0.516 (5546) | 0.549 (534) | 0.741 (783) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.389 | 0.383 | 0.312 | 0.312 | 0.517 | 0.285 | 0.492 | 0.997 |
| 6h | 360 | 0.373 | 0.374 | 0.282 | 0.298 | 0.515 | 0.267 | 0.479 | 1.008 |
| 24h | 1440 | 0.381 | 0.377 | 0.295 | 0.322 | 0.522 | 0.271 | 0.492 | 1.008 |
| 7d | 10080 | 0.368 | 0.364 | 0.282 | 0.312 | 0.530 | 0.266 | 0.469 | 1.292 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.530 | 0.265 | 0.471 | 1.254 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.389 / 0.517 / 0.800; 2: 0.389 / 0.517 / 0.883; 3: 0.383 / 0.533 / 0.900; 4: 0.353 / 0.483 / 0.800; 5: 0.365 / 0.483 / 0.833; 6: 0.328 / 0.383 / 0.817; 7: 0.388 / 0.583 / 0.767; 8: 0.380 / 0.583 / 0.800; 9: 0.326 / 0.400 / 0.783; 10: 0.384 / 0.567 / 0.733; 11: 0.339 / 0.483 / 0.750; 12: 0.346 / 0.500 / 0.800; 13: 0.345 / 0.517 / 0.783; 14: 0.326 / 0.500 / 0.750; 15: 0.319 / 0.467 / 0.750
- 6h: 1: 0.373 / 0.515 / 0.889; 2: 0.368 / 0.493 / 0.964; 3: 0.372 / 0.526 / 0.964; 4: 0.354 / 0.471 / 0.903; 5: 0.366 / 0.499 / 0.942; 6: 0.355 / 0.454 / 0.903; 7: 0.366 / 0.518 / 0.903; 8: 0.364 / 0.526 / 0.922; 9: 0.355 / 0.487 / 0.897; 10: 0.375 / 0.543 / 0.864; 11: 0.360 / 0.513 / 0.867; 12: 0.362 / 0.499 / 0.875; 13: 0.351 / 0.482 / 0.861; 14: 0.360 / 0.515 / 0.856; 15: 0.354 / 0.499 / 0.867
- 24h: 1: 0.381 / 0.522 / 0.894; 2: 0.372 / 0.499 / 0.913; 3: 0.375 / 0.512 / 0.908; 4: 0.366 / 0.488 / 0.896; 5: 0.371 / 0.501 / 0.902; 6: 0.362 / 0.476 / 0.901; 7: 0.371 / 0.503 / 0.904; 8: 0.373 / 0.517 / 0.901; 9: 0.358 / 0.465 / 0.908; 10: 0.367 / 0.499 / 0.899; 11: 0.370 / 0.531 / 0.890; 12: 0.363 / 0.483 / 0.889; 13: 0.369 / 0.511 / 0.889; 14: 0.362 / 0.496 / 0.885; 15: 0.367 / 0.502 / 0.888
- 7d: 1: 0.368 / 0.530 / 0.895; 2: 0.354 / 0.486 / 0.901; 3: 0.360 / 0.515 / 0.901; 4: 0.353 / 0.494 / 0.901; 5: 0.355 / 0.501 / 0.900; 6: 0.351 / 0.490 / 0.900; 7: 0.354 / 0.501 / 0.899; 8: 0.356 / 0.505 / 0.899; 9: 0.354 / 0.502 / 0.899; 10: 0.353 / 0.499 / 0.899; 11: 0.356 / 0.517 / 0.899; 12: 0.352 / 0.501 / 0.899; 13: 0.353 / 0.502 / 0.899; 14: 0.352 / 0.503 / 0.899; 15: 0.352 / 0.497 / 0.899
- 30d: 1: 0.368 / 0.530 / 0.897; 2: 0.355 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.498 / 0.900; 5: 0.355 / 0.504 / 0.900; 6: 0.352 / 0.499 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.503 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.503 / 0.900; 13: 0.351 / 0.499 / 0.900; 14: 0.351 / 0.502 / 0.900; 15: 0.351 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.096 (body 0.060, range 0.133); 'price stays where it was' would score 0.104; colour right 0.467; typical miss of the close 23.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.112 (body 0.075, range 0.150); 'price stays where it was' would score 0.121; colour right 0.526; typical miss of the close 15.6 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.124 (body 0.085, range 0.164); 'price stays where it was' would score 0.132; colour right 0.517; typical miss of the close 14.8 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.123 (body 0.082, range 0.163); 'price stays where it was' would score 0.123; colour right 0.504; typical miss of the close 9.1 bp; chain ended on the right side 0.528 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 9.0 bp; chain ended on the right side 0.521 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.204 / 5.5; 3: 0.168 / 7.2; 4: 0.134 / 7.3; 5: 0.126 / 8.1; 6: 0.117 / 8.9; 7: 0.110 / 9.2; 8: 0.097 / 10.2; 9: 0.092 / 10.4; 10: 0.093 / 10.6; 11: 0.089 / 10.8; 12: 0.080 / 11.2; 13: 0.074 / 11.8; 14: 0.069 / 12.3; 15: 0.065 / 12.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 148248, probability skill vs chance 0.2296, widened contest next: False
  - now: threshold 0.8391, hit rate recent 0.9271 / long run 0.9256
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.296, naive rule 0.498, lift 3.38x
    - 24h: 53 calls (53 a day), hit rate 0.943, chance 0.282, naive rule 0.484, lift 3.34x
    - 7d: 415 calls (59 a day), hit rate 0.920, chance 0.291, naive rule 0.498, lift 3.16x
    - 30d: 1741 calls (58 a day), hit rate 0.930, chance 0.293, naive rule 0.495, lift 3.17x
  - next: threshold 0.5674, hit rate recent 0.6557 / long run 0.6127
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.296, lift 2.63x
    - 24h: 39 calls (39 a day), hit rate 0.692, chance 0.282, lift 2.45x
    - 7d: 349 calls (50 a day), hit rate 0.616, chance 0.291, lift 2.11x
    - 30d: 2662 calls (89 a day), hit rate 0.596, chance 0.293, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.694; 0.55: 310, 0.738; 0.60: 260, 0.782; 0.65: 220, 0.810; 0.70: 173, 0.842; 0.75: 139, 0.872; 0.80: 92, 0.904; 0.85: 46, 0.944; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.431; 0.35: 497, 0.464; 0.40: 396, 0.502; 0.45: 298, 0.535; 0.50: 190, 0.569; 0.55: 84, 0.581; 0.60: 11, 0.661; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 148246, probability skill vs chance 0.2121, widened contest next: True
  - now: threshold 0.6913, hit rate recent 0.6798 / long run 0.774
    - 6h: 17 calls (69 a day), hit rate 0.588, chance 0.160, naive rule 0.369, lift 3.68x
    - 24h: 67 calls (67 a day), hit rate 0.672, chance 0.173, naive rule 0.382, lift 3.89x
    - 7d: 413 calls (59 a day), hit rate 0.736, chance 0.184, naive rule 0.402, lift 4.00x
    - 30d: 1692 calls (56 a day), hit rate 0.800, chance 0.186, naive rule 0.405, lift 4.31x
  - next: threshold 0.4505, hit rate recent 0.5027 / long run 0.5061
    - 6h: 14 calls (57 a day), hit rate 0.500, chance 0.160, lift 3.12x
    - 24h: 72 calls (72 a day), hit rate 0.528, chance 0.173, lift 3.06x
    - 7d: 443 calls (63 a day), hit rate 0.501, chance 0.184, lift 2.72x
    - 30d: 2592 calls (86 a day), hit rate 0.485, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.418; 0.35: 356, 0.477; 0.40: 288, 0.547; 0.45: 234, 0.604; 0.50: 187, 0.651; 0.55: 149, 0.689; 0.60: 112, 0.737; 0.65: 76, 0.774; 0.70: 48, 0.809; 0.75: 28, 0.843; 0.80: 9, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.383; 0.35: 256, 0.423; 0.40: 161, 0.456; 0.45: 65, 0.494; 0.50: 10, 0.531; 0.55: 1, 0.444
- **K=8**: model 1794614400, labels learned 148243, probability skill vs chance 0.2012, widened contest next: True
  - now: threshold 0.5697, hit rate recent 0.5905 / long run 0.6749
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.097, naive rule 0.311, lift 5.15x
    - 24h: 57 calls (57 a day), hit rate 0.579, chance 0.115, naive rule 0.328, lift 5.02x
    - 7d: 373 calls (53 a day), hit rate 0.662, chance 0.123, naive rule 0.341, lift 5.40x
    - 30d: 1545 calls (52 a day), hit rate 0.680, chance 0.120, naive rule 0.334, lift 5.65x
  - next: threshold 0.3699, hit rate recent 0.4053 / long run 0.4191
    - 6h: 10 calls (41 a day), hit rate 0.400, chance 0.097, lift 4.12x
    - 24h: 52 calls (52 a day), hit rate 0.385, chance 0.115, lift 3.33x
    - 7d: 470 calls (67 a day), hit rate 0.413, chance 0.123, lift 3.37x
    - 30d: 2584 calls (86 a day), hit rate 0.397, chance 0.120, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.426; 0.35: 193, 0.489; 0.40: 153, 0.532; 0.45: 118, 0.578; 0.50: 84, 0.634; 0.55: 59, 0.668; 0.60: 40, 0.707; 0.65: 24, 0.768; 0.70: 11, 0.813; 0.75: 2, 0.779
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 168, 0.364; 0.35: 85, 0.390; 0.40: 23, 0.420; 0.45: 4, 0.413; 0.50: 1, 0.783
- **K=13**: model 1794614400, labels learned 148238, probability skill vs chance 0.1779, widened contest next: True
  - now: threshold 0.4463, hit rate recent 0.533 / long run 0.5665
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.072, naive rule 0.278, lift 6.90x
    - 24h: 56 calls (57 a day), hit rate 0.500, chance 0.080, naive rule 0.303, lift 6.25x
    - 7d: 347 calls (50 a day), hit rate 0.559, chance 0.079, naive rule 0.291, lift 7.09x
    - 30d: 1651 calls (55 a day), hit rate 0.558, chance 0.078, naive rule 0.283, lift 7.19x
  - next: threshold 0.2978, hit rate recent 0.3209 / long run 0.334
    - 6h: 12 calls (50 a day), hit rate 0.333, chance 0.072, lift 4.60x
    - 24h: 52 calls (53 a day), hit rate 0.288, chance 0.080, lift 3.61x
    - 7d: 493 calls (71 a day), hit rate 0.329, chance 0.079, lift 4.17x
    - 30d: 1828 calls (61 a day), hit rate 0.330, chance 0.078, lift 4.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.429; 0.35: 97, 0.476; 0.40: 68, 0.532; 0.45: 47, 0.580; 0.50: 32, 0.629; 0.55: 20, 0.653; 0.60: 12, 0.697; 0.65: 3, 0.653; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.337; 0.35: 13, 0.333; 0.40: 2, 0.397; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 40.922 | 8.00% | 0.850 | 0.417 | 0.250 | 0.500 | 0.616 |
| 6h | 23.414 | 4.10% | 0.892 | 0.475 | 0.250 | 0.504 | 0.664 |
| 24h | 24.318 | 4.68% | 0.899 | 0.497 | 0.250 | 0.510 | 0.653 |
| 7d | 17.201 | 5.71% | 0.899 | 0.499 | 0.250 | 0.514 | 0.666 |
| 30d | 16.074 | 4.74% | 0.900 | 0.500 | 0.250 | 0.504 | 0.696 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 44.481 | 42.181 | 41.006 | 41.154 | 42.556 | 41.434 | 41.126 | 40.794 | 40.988 | 40.922 |
| 6h | 24.415 | 23.786 | 23.533 | 23.442 | 23.987 | 23.724 | 23.406 | 23.335 | 23.385 | 23.414 |
| 24h | 25.514 | 24.551 | 24.448 | 24.351 | 24.727 | 24.691 | 24.328 | 24.312 | 24.298 | 24.318 |
| 7d | 18.242 | 17.376 | 17.352 | 17.337 | 17.563 | 17.578 | 17.180 | 17.151 | 17.172 | 17.201 |
| 30d | 16.874 | 16.238 | 16.183 | 16.129 | 16.376 | 16.343 | 16.061 | 16.041 | 16.045 | 16.074 |

## Next candle

- candle starting 2026-11-14 02:54 UTC, last close 1911.16
- P(up) 0.503, return quantiles (bp): {'05': -25.261, '10': -19.256, '25': -10.224, '40': -3.659, '50': 0.104, '60': 4.105, '75': 8.865, '90': 16.315, '95': 22.652}
- changepoint probability 0.0322, regime age 33.7 min
- agent weights: empirical 0.003, ewma 0.042, garch 0.110, har 0.220, bocpd 0.016, hmm 0.049, online_qr 0.256, lgbm 0.304

## Learning log

- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- HMM volatility states (sd, bp per minute): [4.3, 7.03, 18.51], current probabilities: [0.001, 0.169, 0.829]
- live generator: {'versions': 60, 'latest_effective': '2026-11-14 03:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.279, 'l_abs': 0.604, 'l_hi': 0.768, 'l_lo': 0.713, 'b05': 0.719, 'b25': 0.672, 'b75': 0.646, 'b95': 0.705}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.234, 1.641, 2.141, 2.214, 2.43, 2.965, 3.113, 3.309, 4.101, 4.059, 4.334, 4.704, 5.515, 5.387]}
- calibration offsets (in sigma): {'05': -0.0435, '10': -0.027, '25': -0.0675, '40': -0.008, '50': 0.035, '60': 0.088, '75': 0.0175, '90': -0.063, '95': -0.0565}
