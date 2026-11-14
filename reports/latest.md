# ETH-USD 60s candle generator - report

- generated: 2026-11-14 20:44 UTC
- last closed candle: 2026-11-14 20:44 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k5_now 0.738 in the last 7 days, -0.081 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.529 (671) [0.498, 0.560] | 0.520 (2879) [0.503, 0.538] | 0.514 (7001) [0.503, 0.526] | 0.516 (4029) [0.500, 0.531] | 0.585 (82) | 0.500 | flat +0.045 (noise 0.027) |
| colour_clear | 0.539 (838) | 0.541 (5538) [0.532, 0.551] | 0.542 (23911) [0.536, 0.548] | 0.523 (57392) [0.517, 0.528] | 0.542 (33154) [0.538, 0.547] | 0.559 (687) | 0.500 | flat +0.007 (noise 0.013) |
| colour_confident | 0.556 (72) | 0.559 (910) [0.529, 0.577] | 0.586 (4289) [0.576, 0.597] | 0.591 (5897) [0.581, 0.602] | 0.591 (5897) [0.581, 0.602] | 0.622 (37) | 0.500 | flat -0.018 (noise 0.023) |
| colour_next | 0.527 (1434) | 0.530 (9971) [0.520, 0.540] | 0.530 (42869) [0.525, 0.534] | 0.517 (104302) [0.513, 0.521] | 0.529 (59953) [0.526, 0.533] | 0.548 (1243) | 0.500 | flat -0.000 (noise 0.009) |
| colour_path | 0.499 (20076) | 0.501 (139594) [0.499, 0.504] | 0.502 (600166) [0.500, 0.503] | 0.501 (1460228) [0.500, 0.502] | 0.501 (839342) [0.500, 0.502] | 0.499 (17402) | 0.500 | flat -0.002 (noise 0.002) |
| colour_strong | 0.533 (15) | 0.623 (236) [0.558, 0.646] | 0.619 (1107) [0.602, 0.636] | 0.628 (1539) [0.612, 0.645] | 0.628 (1539) [0.612, 0.645] | 0.667 (3) | 0.500 | flat +0.012 (noise 0.047) |
| reversal_k13_next | 0.269 (52) | 0.326 (497) [0.300, 0.351] | 0.330 (1835) [0.316, 0.344] | 0.315 (4812) [0.305, 0.325] | 0.326 (2707) [0.315, 0.337] | 0.500 (38) | 0.077 | flat -0.045 (noise 0.033) |
| reversal_k13_now | 0.517 (58) | 0.561 (346) [0.535, 0.588] | 0.559 (1650) [0.540, 0.580] | 0.573 (3758) [0.560, 0.585] | 0.567 (2286) [0.551, 0.584] | 0.763 (38) | 0.077 | flat -0.025 (noise 0.036) |
| reversal_k3_next | 0.683 (41) | 0.617 (358) [0.584, 0.650] | 0.596 (2670) [0.584, 0.608] | 0.589 (6202) [0.580, 0.598] | 0.590 (3762) [0.579, 0.601] | 0.826 (23) | 0.293 | flat +0.006 (noise 0.032) |
| reversal_k3_now | 0.946 (56) | 0.920 (413) [0.909, 0.932] | 0.930 (1743) [0.920, 0.940] | 0.935 (4202) [0.929, 0.941] | 0.930 (2439) [0.922, 0.938] | 0.959 (49) | 0.293 | flat +0.005 (noise 0.019) |
| reversal_k5_next | 0.520 (75) | 0.500 (450) [0.465, 0.530] | 0.485 (2601) [0.469, 0.502] | 0.485 (5606) [0.474, 0.496] | 0.480 (3616) [0.466, 0.494] | 0.667 (45) | 0.186 | flat -0.039 (noise 0.034) |
| reversal_k5_now | 0.710 (69) | 0.738 (408) [0.699, 0.777] | 0.801 (1690) [0.783, 0.816] | 0.819 (3931) [0.808, 0.829] | 0.806 (2320) [0.792, 0.819] | 0.789 (57) | 0.187 | down -0.081 (noise 0.029) |
| reversal_k8_next | 0.364 (55) | 0.410 (475) [0.383, 0.438] | 0.398 (2596) [0.384, 0.412] | 0.397 (5693) [0.386, 0.407] | 0.397 (3587) [0.385, 0.408] | 0.553 (47) | 0.121 | flat -0.051 (noise 0.033) |
| reversal_k8_now | 0.597 (62) | 0.663 (371) [0.633, 0.694] | 0.680 (1545) [0.661, 0.699] | 0.698 (3802) [0.685, 0.710] | 0.686 (2215) [0.669, 0.702] | 0.821 (39) | 0.122 | flat -0.040 (noise 0.034) |
| overall | 0.503 (22074) | 0.505 (153554) [0.502, 0.507] | 0.505 (662244) [0.504, 0.507] | 0.504 (1609537) [0.503, 0.505] | 0.505 (926256) [0.504, 0.506] | 0.506 (19063) | - | flat -0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0706, 0.1077] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5317, 'levels': [{'threshold': 0.0706, 'calls_per_day': 135.2, 'win_rate': 0.5702}, {'threshold': 0.1077, 'calls_per_day': 32.5, 'win_rate': 0.607}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42871, 'rate': 0.5305}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15295 | 0.347 | 0.534 (15058) | 0.566 (2314) | 0.742 (2560) |
| volatility: normal | 15294 | 0.371 | 0.528 (15232) | 0.614 (1299) | 0.745 (2320) |
| volatility: wild | 15295 | 0.388 | 0.530 (15258) | 0.599 (780) | 0.764 (2095) |
| session: Asia 00-08 | 15360 | 0.368 | 0.535 (15237) | 0.589 (1541) | 0.752 (2296) |
| session: Europe 08-13 | 9600 | 0.362 | 0.533 (9519) | 0.588 (1141) | 0.749 (1583) |
| session: US 13-21 | 15344 | 0.376 | 0.530 (15246) | 0.596 (1177) | 0.750 (2313) |
| session: late 21-24 | 5580 | 0.361 | 0.516 (5546) | 0.549 (534) | 0.741 (783) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.414 | 0.390 | 0.306 | 0.306 | 0.600 | 0.307 | 0.521 | 1.007 |
| 6h | 360 | 0.406 | 0.397 | 0.307 | 0.337 | 0.536 | 0.284 | 0.529 | 1.239 |
| 24h | 1440 | 0.390 | 0.379 | 0.293 | 0.316 | 0.540 | 0.277 | 0.503 | 1.150 |
| 7d | 10080 | 0.375 | 0.369 | 0.288 | 0.317 | 0.533 | 0.270 | 0.481 | 1.217 |
| 30d | 43200 | 0.368 | 0.361 | 0.279 | 0.310 | 0.531 | 0.265 | 0.471 | 1.251 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.414 / 0.600 / 0.867; 2: 0.368 / 0.433 / 0.933; 3: 0.409 / 0.567 / 0.867; 4: 0.355 / 0.383 / 0.850; 5: 0.377 / 0.500 / 0.833; 6: 0.351 / 0.417 / 0.833; 7: 0.388 / 0.550 / 0.900; 8: 0.378 / 0.517 / 0.917; 9: 0.371 / 0.433 / 0.933; 10: 0.396 / 0.533 / 0.917; 11: 0.393 / 0.533 / 0.983; 12: 0.366 / 0.433 / 0.983; 13: 0.415 / 0.583 / 1.000; 14: 0.378 / 0.500 / 1.000; 15: 0.420 / 0.600 / 1.000
- 6h: 1: 0.406 / 0.536 / 0.897; 2: 0.385 / 0.486 / 0.917; 3: 0.407 / 0.556 / 0.908; 4: 0.385 / 0.475 / 0.897; 5: 0.386 / 0.483 / 0.892; 6: 0.380 / 0.467 / 0.883; 7: 0.395 / 0.514 / 0.908; 8: 0.390 / 0.517 / 0.897; 9: 0.380 / 0.483 / 0.925; 10: 0.390 / 0.519 / 0.919; 11: 0.392 / 0.506 / 0.939; 12: 0.379 / 0.481 / 0.939; 13: 0.385 / 0.483 / 0.936; 14: 0.384 / 0.492 / 0.939; 15: 0.378 / 0.475 / 0.939
- 24h: 1: 0.390 / 0.540 / 0.900; 2: 0.370 / 0.481 / 0.913; 3: 0.382 / 0.526 / 0.915; 4: 0.365 / 0.471 / 0.901; 5: 0.371 / 0.498 / 0.910; 6: 0.369 / 0.486 / 0.899; 7: 0.374 / 0.515 / 0.907; 8: 0.373 / 0.517 / 0.910; 9: 0.363 / 0.483 / 0.906; 10: 0.376 / 0.523 / 0.903; 11: 0.368 / 0.502 / 0.901; 12: 0.369 / 0.498 / 0.903; 13: 0.366 / 0.493 / 0.899; 14: 0.369 / 0.505 / 0.903; 15: 0.364 / 0.492 / 0.904
- 7d: 1: 0.375 / 0.533 / 0.897; 2: 0.360 / 0.489 / 0.900; 3: 0.367 / 0.517 / 0.900; 4: 0.359 / 0.491 / 0.899; 5: 0.361 / 0.499 / 0.900; 6: 0.357 / 0.492 / 0.899; 7: 0.361 / 0.501 / 0.900; 8: 0.362 / 0.507 / 0.899; 9: 0.359 / 0.498 / 0.900; 10: 0.360 / 0.502 / 0.900; 11: 0.362 / 0.517 / 0.900; 12: 0.358 / 0.500 / 0.900; 13: 0.359 / 0.502 / 0.900; 14: 0.358 / 0.506 / 0.900; 15: 0.358 / 0.497 / 0.900
- 30d: 1: 0.368 / 0.531 / 0.896; 2: 0.355 / 0.492 / 0.900; 3: 0.359 / 0.511 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.355 / 0.503 / 0.900; 6: 0.352 / 0.499 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.354 / 0.506 / 0.900; 9: 0.353 / 0.502 / 0.900; 10: 0.353 / 0.502 / 0.900; 11: 0.352 / 0.503 / 0.900; 12: 0.352 / 0.502 / 0.900; 13: 0.351 / 0.499 / 0.900; 14: 0.351 / 0.501 / 0.900; 15: 0.351 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.093 (body 0.045, range 0.141); 'price stays where it was' would score 0.059; colour right 0.567; typical miss of the close 18.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.161 (body 0.104, range 0.218); 'price stays where it was' would score 0.155; colour right 0.525; typical miss of the close 19.5 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.135 (body 0.091, range 0.179); 'price stays where it was' would score 0.128; colour right 0.512; typical miss of the close 14.8 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.125 (body 0.083, range 0.166); 'price stays where it was' would score 0.124; colour right 0.503; typical miss of the close 10.8 bp; chain ended on the right side 0.537 of 671 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.129; colour right 0.503; typical miss of the close 9.0 bp; chain ended on the right side 0.522 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 4.7; 2: 0.205 / 5.6; 3: 0.168 / 7.2; 4: 0.134 / 7.4; 5: 0.126 / 8.1; 6: 0.118 / 9.0; 7: 0.109 / 9.2; 8: 0.097 / 10.2; 9: 0.091 / 10.5; 10: 0.091 / 10.7; 11: 0.089 / 10.9; 12: 0.079 / 11.3; 13: 0.074 / 11.8; 14: 0.070 / 12.2; 15: 0.067 / 12.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 149318, probability skill vs chance 0.2385, widened contest next: False
  - now: threshold 0.8395, hit rate recent 0.9377 / long run 0.9274
    - 6h: 7 calls (28 a day), hit rate 1.000, chance 0.276, naive rule 0.510, lift 3.62x
    - 24h: 54 calls (54 a day), hit rate 0.944, chance 0.289, naive rule 0.521, lift 3.27x
    - 7d: 409 calls (58 a day), hit rate 0.927, chance 0.288, naive rule 0.497, lift 3.22x
    - 30d: 1752 calls (58 a day), hit rate 0.932, chance 0.293, naive rule 0.497, lift 3.18x
  - next: threshold 0.5662, hit rate recent 0.7147 / long run 0.6206
    - 24h: 30 calls (30 a day), hit rate 0.833, chance 0.289, lift 2.89x
    - 7d: 333 calls (48 a day), hit rate 0.628, chance 0.288, lift 2.18x
    - 30d: 2618 calls (87 a day), hit rate 0.599, chance 0.293, lift 2.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 562, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.578; 0.45: 406, 0.648; 0.50: 357, 0.693; 0.55: 310, 0.738; 0.60: 260, 0.782; 0.65: 220, 0.812; 0.70: 172, 0.843; 0.75: 139, 0.874; 0.80: 92, 0.906; 0.85: 46, 0.943; 0.90: 5, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 586, 0.431; 0.35: 496, 0.465; 0.40: 395, 0.504; 0.45: 297, 0.538; 0.50: 189, 0.571; 0.55: 84, 0.585; 0.60: 11, 0.668; 0.65: 1, 0.667
- **K=5**: model 1794528000, labels learned 149316, probability skill vs chance 0.2326, widened contest next: False
  - now: threshold 0.6934, hit rate recent 0.7729 / long run 0.7798
    - 6h: 15 calls (61 a day), hit rate 0.800, chance 0.183, naive rule 0.458, lift 4.38x
    - 24h: 66 calls (66 a day), hit rate 0.773, chance 0.182, naive rule 0.440, lift 4.24x
    - 7d: 425 calls (61 a day), hit rate 0.739, chance 0.183, naive rule 0.406, lift 4.04x
    - 30d: 1700 calls (57 a day), hit rate 0.802, chance 0.186, naive rule 0.407, lift 4.31x
  - next: threshold 0.453, hit rate recent 0.5845 / long run 0.5177
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.183, lift 2.43x
    - 24h: 56 calls (56 a day), hit rate 0.643, chance 0.182, lift 3.53x
    - 7d: 441 calls (63 a day), hit rate 0.515, chance 0.183, lift 2.82x
    - 30d: 2549 calls (85 a day), hit rate 0.491, chance 0.186, lift 2.64x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.420; 0.35: 356, 0.478; 0.40: 288, 0.548; 0.45: 234, 0.604; 0.50: 187, 0.651; 0.55: 149, 0.689; 0.60: 112, 0.738; 0.65: 77, 0.777; 0.70: 48, 0.811; 0.75: 28, 0.843; 0.80: 9, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 345, 0.385; 0.35: 255, 0.426; 0.40: 160, 0.459; 0.45: 65, 0.503; 0.50: 10, 0.539; 0.55: 1, 0.441
- **K=8**: model 1794614400, labels learned 149313, probability skill vs chance 0.2275, widened contest next: False
  - now: threshold 0.5702, hit rate recent 0.7173 / long run 0.6868
    - 6h: 8 calls (33 a day), hit rate 0.750, chance 0.137, naive rule 0.430, lift 5.47x
    - 24h: 48 calls (48 a day), hit rate 0.771, chance 0.124, naive rule 0.393, lift 6.19x
    - 7d: 369 calls (53 a day), hit rate 0.672, chance 0.123, naive rule 0.347, lift 5.48x
    - 30d: 1549 calls (52 a day), hit rate 0.684, chance 0.121, naive rule 0.337, lift 5.65x
  - next: threshold 0.3718, hit rate recent 0.4741 / long run 0.4288
    - 6h: 12 calls (49 a day), hit rate 0.333, chance 0.137, lift 2.43x
    - 24h: 56 calls (56 a day), hit rate 0.536, chance 0.124, lift 4.30x
    - 7d: 471 calls (67 a day), hit rate 0.427, chance 0.123, lift 3.48x
    - 30d: 2562 calls (85 a day), hit rate 0.401, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 194, 0.490; 0.40: 153, 0.533; 0.45: 118, 0.580; 0.50: 84, 0.639; 0.55: 59, 0.673; 0.60: 40, 0.712; 0.65: 24, 0.772; 0.70: 11, 0.813; 0.75: 2, 0.776
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 167, 0.368; 0.35: 85, 0.394; 0.40: 24, 0.431; 0.45: 5, 0.431; 0.50: 1, 0.792
- **K=13**: model 1794614400, labels learned 149308, probability skill vs chance 0.2081, widened contest next: False
  - now: threshold 0.4458, hit rate recent 0.6502 / long run 0.5802
    - 6h: 10 calls (42 a day), hit rate 0.600, chance 0.088, naive rule 0.392, lift 6.79x
    - 24h: 45 calls (45 a day), hit rate 0.733, chance 0.084, naive rule 0.357, lift 8.71x
    - 7d: 343 calls (49 a day), hit rate 0.589, chance 0.080, naive rule 0.303, lift 7.36x
    - 30d: 1645 calls (55 a day), hit rate 0.565, chance 0.078, naive rule 0.286, lift 7.25x
  - next: threshold 0.2987, hit rate recent 0.3849 / long run 0.3425
    - 6h: 9 calls (38 a day), hit rate 0.333, chance 0.088, lift 3.77x
    - 24h: 47 calls (47 a day), hit rate 0.447, chance 0.084, lift 5.31x
    - 7d: 478 calls (68 a day), hit rate 0.345, chance 0.080, lift 4.31x
    - 30d: 1833 calls (61 a day), hit rate 0.334, chance 0.078, lift 4.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 135, 0.431; 0.35: 97, 0.479; 0.40: 68, 0.538; 0.45: 47, 0.587; 0.50: 32, 0.637; 0.55: 21, 0.661; 0.60: 11, 0.702; 0.65: 3, 0.646; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.342; 0.35: 13, 0.344; 0.40: 2, 0.413; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 28.564 | 1.11% | 0.867 | 0.450 | 0.248 | 0.550 | 0.337 |
| 6h | 36.365 | 6.08% | 0.897 | 0.500 | 0.249 | 0.525 | 0.468 |
| 24h | 26.043 | 4.33% | 0.902 | 0.502 | 0.250 | 0.508 | 0.650 |
| 7d | 19.365 | 5.32% | 0.900 | 0.499 | 0.250 | 0.511 | 0.660 |
| 30d | 16.188 | 4.79% | 0.900 | 0.500 | 0.250 | 0.504 | 0.702 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 28.886 | 28.840 | 29.033 | 28.525 | 28.650 | 29.545 | 28.515 | 28.513 | 28.501 | 28.564 |
| 6h | 38.718 | 36.525 | 36.886 | 36.574 | 36.847 | 37.070 | 36.265 | 36.279 | 36.310 | 36.365 |
| 24h | 27.223 | 26.258 | 26.289 | 26.156 | 26.685 | 26.356 | 26.014 | 25.996 | 26.014 | 26.043 |
| 7d | 20.452 | 19.550 | 19.526 | 19.508 | 19.778 | 19.697 | 19.340 | 19.312 | 19.334 | 19.365 |
| 30d | 17.003 | 16.349 | 16.305 | 16.246 | 16.504 | 16.460 | 16.170 | 16.152 | 16.159 | 16.188 |

## Next candle

- candle starting 2026-11-14 20:44 UTC, last close 1820.8
- P(up) 0.4877, return quantiles (bp): {'05': -18.48, '10': -14.106, '25': -7.289, '40': -2.839, '50': -0.309, '60': 2.24, '75': 6.213, '90': 12.451, '95': 17.157}
- changepoint probability 0.0365, regime age 143.2 min
- agent weights: empirical 0.003, ewma 0.106, garch 0.043, har 0.131, bocpd 0.011, hmm 0.038, online_qr 0.334, lgbm 0.335

## Learning log

- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- 2026-11-13 00:00 UTC: {"garch": {"alpha": 0.1395, "beta": 0.8287}, "hmm": {"sd_bp": [3.37, 6.31, 18.97], "stay": [0.945, 0.973, 0.95]}, "lgbm": {"challenger_loss": 0.25303, "champion_loss": 0.25299, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48037, "challengers": 1, "chance_loss": 0.60343, "widened": false, "champion_loss": 0.47856, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36587, "challengers": 3, "chance_loss": 0.47582, "widened": true, "champion_loss": 0.36602, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28086, "challengers": 3, "chance_loss": 0.37973, "widened": true, "champion_loss": 0.28083, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19409, "challengers": 1, "chance_loss": 0.27459, "widened": false, "champion_loss": 0.194, "promoted": false}}
- 2026-11-13 12:00 UTC: {"garch": {"alpha": 0.1234, "beta": 0.8453}, "hmm": {"sd_bp": [3.98, 6.75, 18.41], "stay": [0.961, 0.968, 0.943]}}
- 2026-11-14 00:00 UTC: {"garch": {"alpha": 0.1099, "beta": 0.8654}, "hmm": {"sd_bp": [4.3, 7.03, 18.51], "stay": [0.971, 0.963, 0.944]}, "lgbm": {"challenger_loss": 0.25214, "champion_loss": 0.25208, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.59904, "widened": false, "champion_loss": 0.47584, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36782, "challengers": 3, "chance_loss": 0.47542, "widened": true, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28073, "challengers": 3, "chance_loss": 0.37236, "widened": true, "champion_loss": 0.28079, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19484, "challengers": 1, "chance_loss": 0.26989, "widened": false, "champion_loss": 0.19506, "promoted": true}}
- 2026-11-14 12:00 UTC: {"garch": {"alpha": 0.1228, "beta": 0.848}, "hmm": {"sd_bp": [4.77, 7.88, 20.15], "stay": [0.979, 0.958, 0.928]}}
- HMM volatility states (sd, bp per minute): [4.77, 7.88, 20.15], current probabilities: [0.005, 0.414, 0.581]
- live generator: {'versions': 60, 'latest_effective': '2026-11-14 20:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.29, 'l_abs': 0.705, 'l_hi': 0.79, 'l_lo': 0.726, 'b05': 0.736, 'b25': 0.737, 'b75': 0.601, 'b95': 0.713}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.6], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.337, 1.742, 2.184, 2.304, 2.58, 2.527, 2.817, 2.764, 2.978, 3.193, 3.342, 3.775, 3.772, 3.834]}
- calibration offsets (in sigma): {'05': 0.0215, '10': -0.007, '25': -0.0425, '40': -0.048, '50': -0.045, '60': -0.052, '75': -0.0875, '90': -0.093, '95': -0.0615}
