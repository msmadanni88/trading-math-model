# ETH-USD 60s candle generator - report

- generated: 2026-11-14 16:11 UTC
- last closed candle: 2026-11-14 16:11 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_now 0.738 in the last 7 days, -0.081 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.529 (671) [0.498, 0.560] | 0.520 (2879) [0.503, 0.538] | 0.514 (7001) [0.503, 0.526] | 0.516 (4029) [0.500, 0.531] | 0.594 (64) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.539 (838) | 0.541 (5538) [0.532, 0.551] | 0.542 (23911) [0.536, 0.548] | 0.523 (57392) [0.517, 0.528] | 0.542 (33154) [0.538, 0.547] | 0.551 (543) | 0.500 | flat +0.007 (noise 0.013) |
| colour_confident | 0.556 (72) | 0.559 (910) [0.529, 0.577] | 0.586 (4289) [0.576, 0.597] | 0.591 (5897) [0.581, 0.602] | 0.591 (5897) [0.581, 0.602] | 0.704 (27) | 0.500 | flat -0.018 (noise 0.023) |
| colour_next | 0.527 (1434) | 0.530 (9971) [0.520, 0.540] | 0.530 (42869) [0.525, 0.534] | 0.517 (104302) [0.513, 0.521] | 0.529 (59953) [0.526, 0.533] | 0.544 (970) | 0.500 | flat -0.000 (noise 0.009) |
| colour_path | 0.499 (20076) | 0.501 (139594) [0.499, 0.504] | 0.502 (600166) [0.500, 0.503] | 0.501 (1460228) [0.500, 0.502] | 0.501 (839342) [0.500, 0.502] | 0.500 (13580) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.533 (15) | 0.623 (236) [0.558, 0.646] | 0.619 (1107) [0.602, 0.636] | 0.628 (1539) [0.612, 0.645] | 0.628 (1539) [0.612, 0.645] | 0.667 (3) | 0.500 | flat +0.012 (noise 0.047) |
| reversal_k13_next | 0.269 (52) | 0.326 (497) [0.300, 0.351] | 0.330 (1835) [0.316, 0.344] | 0.315 (4812) [0.305, 0.325] | 0.326 (2707) [0.315, 0.337] | 0.533 (30) | 0.077 | flat -0.045 (noise 0.033) |
| reversal_k13_now | 0.517 (58) | 0.561 (346) [0.535, 0.588] | 0.559 (1650) [0.540, 0.580] | 0.573 (3758) [0.560, 0.585] | 0.567 (2286) [0.551, 0.584] | 0.767 (30) | 0.077 | flat -0.025 (noise 0.036) |
| reversal_k3_next | 0.683 (41) | 0.617 (358) [0.584, 0.650] | 0.596 (2670) [0.584, 0.608] | 0.589 (6202) [0.580, 0.598] | 0.590 (3762) [0.579, 0.601] | 0.800 (20) | 0.293 | flat +0.006 (noise 0.032) |
| reversal_k3_now | 0.946 (56) | 0.920 (413) [0.909, 0.932] | 0.930 (1743) [0.920, 0.940] | 0.935 (4202) [0.929, 0.941] | 0.930 (2439) [0.922, 0.938] | 0.956 (45) | 0.293 | flat +0.005 (noise 0.019) |
| reversal_k5_next | 0.520 (75) | 0.500 (450) [0.465, 0.530] | 0.485 (2601) [0.469, 0.502] | 0.485 (5606) [0.474, 0.496] | 0.480 (3616) [0.466, 0.494] | 0.703 (37) | 0.186 | flat -0.039 (noise 0.034) |
| reversal_k5_now | 0.710 (69) | 0.738 (408) [0.699, 0.777] | 0.801 (1690) [0.783, 0.816] | 0.819 (3931) [0.808, 0.829] | 0.806 (2320) [0.792, 0.819] | 0.783 (46) | 0.187 | down -0.081 (noise 0.029) |
| reversal_k8_next | 0.364 (55) | 0.410 (475) [0.383, 0.438] | 0.398 (2596) [0.384, 0.412] | 0.397 (5693) [0.386, 0.407] | 0.397 (3587) [0.385, 0.408] | 0.611 (36) | 0.121 | flat -0.051 (noise 0.033) |
| reversal_k8_now | 0.597 (62) | 0.663 (371) [0.633, 0.694] | 0.680 (1545) [0.661, 0.699] | 0.698 (3802) [0.685, 0.710] | 0.686 (2215) [0.669, 0.702] | 0.788 (33) | 0.122 | flat -0.040 (noise 0.034) |
| overall | 0.503 (22074) | 0.505 (153554) [0.502, 0.507] | 0.505 (662244) [0.504, 0.507] | 0.504 (1609537) [0.503, 0.505] | 0.505 (926256) [0.504, 0.506] | 0.508 (14891) | - | flat -0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07226, 0.1111] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5314, 'levels': [{'threshold': 0.07226, 'calls_per_day': 136.3, 'win_rate': 0.5732}, {'threshold': 0.1111, 'calls_per_day': 33.0, 'win_rate': 0.618}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42869, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15204 | 0.347 | 0.535 (14967) | 0.566 (2306) | 0.742 (2547) |
| volatility: normal | 15203 | 0.371 | 0.528 (15141) | 0.612 (1298) | 0.744 (2316) |
| volatility: wild | 15204 | 0.387 | 0.529 (15167) | 0.603 (779) | 0.763 (2083) |
| session: Asia 00-08 | 15360 | 0.368 | 0.535 (15237) | 0.589 (1541) | 0.752 (2296) |
| session: Europe 08-13 | 9600 | 0.362 | 0.533 (9519) | 0.588 (1141) | 0.749 (1583) |
| session: US 13-21 | 15071 | 0.375 | 0.530 (14973) | 0.598 (1167) | 0.749 (2284) |
| session: late 21-24 | 5580 | 0.361 | 0.516 (5546) | 0.549 (534) | 0.741 (783) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.386 | 0.413 | 0.337 | 0.337 | 0.450 | 0.256 | 0.516 | 1.206 |
| 6h | 360 | 0.388 | 0.380 | 0.297 | 0.305 | 0.536 | 0.278 | 0.499 | 1.157 |
| 24h | 1440 | 0.386 | 0.377 | 0.292 | 0.315 | 0.545 | 0.277 | 0.496 | 1.115 |
| 7d | 10080 | 0.374 | 0.368 | 0.287 | 0.316 | 0.532 | 0.269 | 0.478 | 1.241 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.530 | 0.265 | 0.471 | 1.254 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.386 / 0.450 / 0.917; 2: 0.358 / 0.383 / 0.917; 3: 0.444 / 0.617 / 0.917; 4: 0.411 / 0.517 / 0.900; 5: 0.401 / 0.500 / 0.950; 6: 0.394 / 0.450 / 0.967; 7: 0.421 / 0.500 / 0.917; 8: 0.415 / 0.517 / 0.883; 9: 0.414 / 0.533 / 0.917; 10: 0.395 / 0.500 / 0.917; 11: 0.422 / 0.533 / 0.917; 12: 0.393 / 0.517 / 0.883; 13: 0.370 / 0.383 / 0.850; 14: 0.413 / 0.550 / 0.867; 15: 0.346 / 0.367 / 0.800
- 6h: 1: 0.388 / 0.536 / 0.897; 2: 0.354 / 0.453 / 0.894; 3: 0.381 / 0.536 / 0.886; 4: 0.371 / 0.492 / 0.872; 5: 0.364 / 0.500 / 0.906; 6: 0.377 / 0.522 / 0.922; 7: 0.370 / 0.497 / 0.872; 8: 0.373 / 0.522 / 0.881; 9: 0.357 / 0.475 / 0.869; 10: 0.377 / 0.569 / 0.858; 11: 0.360 / 0.481 / 0.828; 12: 0.356 / 0.475 / 0.828; 13: 0.356 / 0.472 / 0.806; 14: 0.366 / 0.497 / 0.814; 15: 0.348 / 0.461 / 0.806
- 24h: 1: 0.386 / 0.545 / 0.901; 2: 0.366 / 0.485 / 0.917; 3: 0.377 / 0.522 / 0.920; 4: 0.363 / 0.474 / 0.908; 5: 0.370 / 0.506 / 0.920; 6: 0.365 / 0.483 / 0.913; 7: 0.373 / 0.519 / 0.910; 8: 0.373 / 0.521 / 0.912; 9: 0.361 / 0.482 / 0.905; 10: 0.373 / 0.518 / 0.908; 11: 0.365 / 0.507 / 0.904; 12: 0.365 / 0.492 / 0.898; 13: 0.363 / 0.496 / 0.893; 14: 0.367 / 0.510 / 0.895; 15: 0.364 / 0.497 / 0.895
- 7d: 1: 0.374 / 0.532 / 0.898; 2: 0.358 / 0.487 / 0.900; 3: 0.365 / 0.517 / 0.900; 4: 0.357 / 0.492 / 0.899; 5: 0.359 / 0.500 / 0.901; 6: 0.356 / 0.492 / 0.901; 7: 0.359 / 0.501 / 0.901; 8: 0.361 / 0.506 / 0.901; 9: 0.358 / 0.499 / 0.902; 10: 0.358 / 0.502 / 0.902; 11: 0.360 / 0.516 / 0.901; 12: 0.357 / 0.502 / 0.901; 13: 0.357 / 0.501 / 0.900; 14: 0.357 / 0.506 / 0.900; 15: 0.356 / 0.497 / 0.899
- 30d: 1: 0.368 / 0.530 / 0.897; 2: 0.355 / 0.492 / 0.900; 3: 0.358 / 0.511 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.503 / 0.900; 6: 0.352 / 0.499 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.502 / 0.900; 10: 0.353 / 0.502 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.351 / 0.499 / 0.900; 14: 0.351 / 0.502 / 0.900; 15: 0.351 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.202 (body 0.152, range 0.252); 'price stays where it was' would score 0.149; colour right 0.550; typical miss of the close 21.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.165 (body 0.120, range 0.210); 'price stays where it was' would score 0.133; colour right 0.494; typical miss of the close 11.6 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.130 (body 0.089, range 0.172); 'price stays where it was' would score 0.133; colour right 0.511; typical miss of the close 13.6 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.125 (body 0.084, range 0.166); 'price stays where it was' would score 0.124; colour right 0.502; typical miss of the close 10.3 bp; chain ended on the right side 0.537 of 671 chains; n=10080
- 30d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.0 bp; chain ended on the right side 0.522 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.7; 2: 0.205 / 5.5; 3: 0.168 / 7.2; 4: 0.134 / 7.3; 5: 0.125 / 8.1; 6: 0.118 / 9.0; 7: 0.109 / 9.2; 8: 0.097 / 10.2; 9: 0.091 / 10.5; 10: 0.091 / 10.7; 11: 0.089 / 10.8; 12: 0.080 / 11.3; 13: 0.074 / 11.8; 14: 0.070 / 12.2; 15: 0.067 / 12.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 149045, probability skill vs chance 0.2428, widened contest next: False
  - now: threshold 0.8396, hit rate recent 0.9333 / long run 0.9269
    - 6h: 20 calls (81 a day), hit rate 0.900, chance 0.297, naive rule 0.560, lift 3.03x
    - 24h: 57 calls (57 a day), hit rate 0.947, chance 0.287, naive rule 0.508, lift 3.30x
    - 7d: 417 calls (60 a day), hit rate 0.923, chance 0.289, naive rule 0.498, lift 3.20x
    - 30d: 1757 calls (59 a day), hit rate 0.931, chance 0.293, naive rule 0.497, lift 3.17x
  - next: threshold 0.5665, hit rate recent 0.7 / long run 0.6187
    - 6h: 8 calls (32 a day), hit rate 0.875, chance 0.297, lift 2.94x
    - 24h: 34 calls (34 a day), hit rate 0.794, chance 0.287, lift 2.77x
    - 7d: 334 calls (48 a day), hit rate 0.623, chance 0.289, lift 2.16x
    - 30d: 2633 calls (88 a day), hit rate 0.598, chance 0.293, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.579; 0.45: 406, 0.649; 0.50: 357, 0.694; 0.55: 310, 0.738; 0.60: 260, 0.783; 0.65: 220, 0.812; 0.70: 172, 0.844; 0.75: 139, 0.875; 0.80: 92, 0.906; 0.85: 46, 0.943; 0.90: 5, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.431; 0.35: 496, 0.465; 0.40: 395, 0.504; 0.45: 297, 0.538; 0.50: 190, 0.571; 0.55: 84, 0.584; 0.60: 11, 0.668; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 149043, probability skill vs chance 0.2326, widened contest next: False
  - now: threshold 0.6929, hit rate recent 0.7631 / long run 0.7791
    - 6h: 20 calls (82 a day), hit rate 0.900, chance 0.218, naive rule 0.558, lift 4.13x
    - 24h: 65 calls (65 a day), hit rate 0.754, chance 0.183, naive rule 0.423, lift 4.12x
    - 7d: 420 calls (60 a day), hit rate 0.738, chance 0.183, naive rule 0.405, lift 4.03x
    - 30d: 1699 calls (57 a day), hit rate 0.802, chance 0.186, naive rule 0.406, lift 4.31x
  - next: threshold 0.4514, hit rate recent 0.5988 / long run 0.5179
    - 6h: 18 calls (73 a day), hit rate 0.778, chance 0.218, lift 3.57x
    - 24h: 65 calls (65 a day), hit rate 0.600, chance 0.183, lift 3.28x
    - 7d: 438 calls (63 a day), hit rate 0.521, chance 0.183, lift 2.84x
    - 30d: 2556 calls (85 a day), hit rate 0.490, chance 0.186, lift 2.63x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.419; 0.35: 356, 0.478; 0.40: 288, 0.548; 0.45: 234, 0.604; 0.50: 187, 0.652; 0.55: 149, 0.690; 0.60: 112, 0.739; 0.65: 77, 0.777; 0.70: 48, 0.812; 0.75: 28, 0.844; 0.80: 9, 0.876
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.385; 0.35: 255, 0.425; 0.40: 161, 0.458; 0.45: 65, 0.502; 0.50: 9, 0.537; 0.55: 1, 0.441
- **K=8**: model 1794614400, labels learned 149040, probability skill vs chance 0.2244, widened contest next: False
  - now: threshold 0.571, hit rate recent 0.6874 / long run 0.6837
    - 6h: 14 calls (58 a day), hit rate 0.786, chance 0.141, naive rule 0.509, lift 5.56x
    - 24h: 48 calls (48 a day), hit rate 0.708, chance 0.120, naive rule 0.362, lift 5.92x
    - 7d: 367 calls (52 a day), hit rate 0.670, chance 0.123, naive rule 0.346, lift 5.46x
    - 30d: 1550 calls (52 a day), hit rate 0.683, chance 0.121, naive rule 0.336, lift 5.65x
  - next: threshold 0.3711, hit rate recent 0.4993 / long run 0.43
    - 6h: 16 calls (66 a day), hit rate 0.688, chance 0.141, lift 4.86x
    - 24h: 57 calls (57 a day), hit rate 0.526, chance 0.120, lift 4.40x
    - 7d: 462 calls (66 a day), hit rate 0.429, chance 0.123, lift 3.49x
    - 30d: 2568 calls (86 a day), hit rate 0.401, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 193, 0.490; 0.40: 153, 0.533; 0.45: 118, 0.580; 0.50: 84, 0.638; 0.55: 59, 0.671; 0.60: 40, 0.712; 0.65: 24, 0.771; 0.70: 11, 0.814; 0.75: 2, 0.779
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 168, 0.367; 0.35: 85, 0.393; 0.40: 23, 0.431; 0.45: 4, 0.430; 0.50: 1, 0.792
- **K=13**: model 1794614400, labels learned 149035, probability skill vs chance 0.2033, widened contest next: False
  - now: threshold 0.4467, hit rate recent 0.6346 / long run 0.5779
    - 6h: 11 calls (46 a day), hit rate 0.727, chance 0.091, naive rule 0.427, lift 7.97x
    - 24h: 45 calls (45 a day), hit rate 0.711, chance 0.084, naive rule 0.343, lift 8.44x
    - 7d: 338 calls (48 a day), hit rate 0.586, chance 0.081, naive rule 0.303, lift 7.27x
    - 30d: 1644 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.284, lift 7.24x
  - next: threshold 0.2982, hit rate recent 0.388 / long run 0.3421
    - 6h: 13 calls (54 a day), hit rate 0.462, chance 0.091, lift 5.05x
    - 24h: 51 calls (52 a day), hit rate 0.431, chance 0.084, lift 5.12x
    - 7d: 475 calls (68 a day), hit rate 0.345, chance 0.081, lift 4.28x
    - 30d: 1830 calls (61 a day), hit rate 0.333, chance 0.078, lift 4.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.431; 0.35: 97, 0.478; 0.40: 68, 0.536; 0.45: 47, 0.586; 0.50: 32, 0.635; 0.55: 21, 0.659; 0.60: 12, 0.699; 0.65: 3, 0.646; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.342; 0.35: 13, 0.342; 0.40: 2, 0.413; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 41.174 | 10.16% | 0.950 | 0.483 | 0.249 | 0.550 | 0.415 |
| 6h | 27.722 | 7.31% | 0.911 | 0.508 | 0.250 | 0.508 | 0.657 |
| 24h | 22.863 | 4.18% | 0.908 | 0.509 | 0.250 | 0.507 | 0.657 |
| 7d | 18.606 | 5.33% | 0.901 | 0.500 | 0.250 | 0.511 | 0.658 |
| 30d | 16.067 | 4.80% | 0.900 | 0.500 | 0.250 | 0.504 | 0.699 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 45.830 | 41.214 | 41.643 | 41.389 | 41.523 | 41.828 | 41.297 | 41.838 | 41.347 | 41.174 |
| 6h | 29.909 | 27.909 | 28.163 | 27.812 | 28.843 | 27.941 | 27.718 | 27.836 | 27.759 | 27.722 |
| 24h | 23.860 | 23.080 | 23.031 | 22.942 | 23.498 | 23.104 | 22.834 | 22.861 | 22.847 | 22.863 |
| 7d | 19.654 | 18.792 | 18.756 | 18.746 | 19.015 | 18.937 | 18.585 | 18.559 | 18.578 | 18.606 |
| 30d | 16.877 | 16.228 | 16.182 | 16.126 | 16.383 | 16.335 | 16.050 | 16.033 | 16.039 | 16.067 |

## Next candle

- candle starting 2026-11-14 16:11 UTC, last close 1824.85
- P(up) 0.4989, return quantiles (bp): {'05': -30.46, '10': -21.71, '25': -11.543, '40': -4.016, '50': -0.051, '60': 4.057, '75': 10.192, '90': 20.034, '95': 26.745}
- changepoint probability 0.0416, regime age 84.6 min
- agent weights: empirical 0.003, ewma 0.102, garch 0.068, har 0.180, bocpd 0.005, hmm 0.094, online_qr 0.318, lgbm 0.230

## Learning log

- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- HMM volatility states (sd, bp per minute): [4.77, 7.88, 20.15], current probabilities: [0.0, 0.45, 0.55]
- live generator: {'versions': 60, 'latest_effective': '2026-11-14 16:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.162, 'l_abs': 0.664, 'l_hi': 0.778, 'l_lo': 0.714, 'b05': 0.719, 'b25': 0.743, 'b75': 0.654, 'b95': 0.706}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.428, 1.753, 2.069, 1.936, 2.042, 2.593, 2.669, 3.073, 3.181, 3.923, 4.274, 4.926, 4.921, 5.42]}
- calibration offsets (in sigma): {'05': 0.005, '10': -0.01, '25': -0.065, '40': -0.04, '50': -0.04, '60': -0.05, '75': -0.095, '90': -0.13, '95': -0.125}
