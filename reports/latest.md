# ETH-USD 60s candle generator - report

- generated: 2026-10-17 18:13 UTC
- last closed candle: 2026-10-17 18:13 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.500 (72) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.577 (615) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.576 (99) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.547 (1078) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.491 (15092) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.615 (26) | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | 0.375 (32) | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | 0.610 (41) | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | 0.577 (97) | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 0.848 (46) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | 0.480 (102) | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 0.829 (41) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | 0.432 (88) | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | 0.750 (36) | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.497 (16725) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07037, 0.1095] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.07037, 'calls_per_day': 136.2, 'win_rate': 0.5734}, {'threshold': 0.1095, 'calls_per_day': 33.2, 'win_rate': 0.6453}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 19893, 'rate': 0.529}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15245 | 0.337 | 0.522 (15004) | 0.596 (1332) | 0.776 (2474) |
| volatility: normal | 15244 | 0.362 | 0.514 (15181) | 0.606 (386) | 0.769 (2187) |
| volatility: wild | 15244 | 0.376 | 0.503 (15202) | 0.646 (161) | 0.772 (2097) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15260) | 0.607 (682) | 0.768 (2238) |
| session: Europe 08-13 | 9600 | 0.352 | 0.512 (9517) | 0.580 (486) | 0.777 (1499) |
| session: US 13-21 | 15193 | 0.367 | 0.508 (15094) | 0.587 (445) | 0.780 (2206) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5516) | 0.658 (266) | 0.757 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.351 | 0.329 | 0.212 | 0.212 | 0.567 | 0.286 | 0.416 | 1.277 |
| 6h | 360 | 0.350 | 0.331 | 0.245 | 0.284 | 0.557 | 0.265 | 0.435 | 1.125 |
| 24h | 1440 | 0.360 | 0.338 | 0.255 | 0.287 | 0.547 | 0.273 | 0.447 | 1.193 |
| 7d | 10080 | 0.363 | 0.353 | 0.277 | 0.308 | 0.527 | 0.261 | 0.465 | 1.253 |
| 30d | 43200 | 0.359 | 0.355 | 0.280 | 0.309 | 0.515 | 0.252 | 0.466 | 1.302 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.351 / 0.567 / 0.867; 2: 0.299 / 0.433 / 0.883; 3: 0.315 / 0.483 / 0.883; 4: 0.310 / 0.433 / 0.917; 5: 0.315 / 0.500 / 0.933; 6: 0.330 / 0.517 / 0.933; 7: 0.348 / 0.633 / 0.933; 8: 0.317 / 0.450 / 0.900; 9: 0.333 / 0.533 / 0.917; 10: 0.287 / 0.367 / 0.933; 11: 0.337 / 0.550 / 0.950; 12: 0.294 / 0.383 / 0.933; 13: 0.312 / 0.450 / 0.917; 14: 0.295 / 0.367 / 0.933; 15: 0.300 / 0.467 / 0.900
- 6h: 1: 0.350 / 0.557 / 0.861; 2: 0.333 / 0.468 / 0.897; 3: 0.336 / 0.493 / 0.886; 4: 0.343 / 0.499 / 0.897; 5: 0.339 / 0.510 / 0.886; 6: 0.331 / 0.476 / 0.892; 7: 0.350 / 0.555 / 0.881; 8: 0.324 / 0.448 / 0.894; 9: 0.337 / 0.485 / 0.892; 10: 0.331 / 0.476 / 0.903; 11: 0.333 / 0.476 / 0.906; 12: 0.324 / 0.465 / 0.911; 13: 0.336 / 0.510 / 0.894; 14: 0.331 / 0.501 / 0.894; 15: 0.332 / 0.490 / 0.892
- 24h: 1: 0.360 / 0.547 / 0.885; 2: 0.340 / 0.485 / 0.903; 3: 0.340 / 0.487 / 0.907; 4: 0.334 / 0.480 / 0.908; 5: 0.341 / 0.502 / 0.910; 6: 0.337 / 0.485 / 0.913; 7: 0.341 / 0.504 / 0.911; 8: 0.338 / 0.486 / 0.914; 9: 0.341 / 0.487 / 0.915; 10: 0.345 / 0.515 / 0.917; 11: 0.330 / 0.480 / 0.915; 12: 0.341 / 0.498 / 0.919; 13: 0.342 / 0.511 / 0.922; 14: 0.336 / 0.493 / 0.919; 15: 0.336 / 0.496 / 0.917
- 7d: 1: 0.363 / 0.527 / 0.902; 2: 0.351 / 0.498 / 0.900; 3: 0.354 / 0.507 / 0.901; 4: 0.350 / 0.497 / 0.902; 5: 0.352 / 0.504 / 0.902; 6: 0.351 / 0.502 / 0.902; 7: 0.351 / 0.504 / 0.903; 8: 0.349 / 0.499 / 0.902; 9: 0.351 / 0.502 / 0.902; 10: 0.351 / 0.506 / 0.903; 11: 0.346 / 0.492 / 0.903; 12: 0.349 / 0.503 / 0.905; 13: 0.349 / 0.503 / 0.904; 14: 0.346 / 0.498 / 0.903; 15: 0.350 / 0.505 / 0.902
- 30d: 1: 0.359 / 0.515 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.348 / 0.502 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.089 (body 0.065, range 0.112); 'price stays where it was' would score 0.111; colour right 0.483; typical miss of the close 10.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.107 (body 0.075, range 0.139); 'price stays where it was' would score 0.111; colour right 0.513; typical miss of the close 8.4 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.139 (body 0.098, range 0.180); 'price stays where it was' would score 0.153; colour right 0.504; typical miss of the close 5.5 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.162); 'price stays where it was' would score 0.131; colour right 0.497; typical miss of the close 8.4 bp; chain ended on the right side 0.511 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.9 bp; chain ended on the right side 0.518 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.0; 2: 0.197 / 4.4; 3: 0.165 / 6.0; 4: 0.133 / 6.6; 5: 0.121 / 7.3; 6: 0.109 / 7.8; 7: 0.102 / 8.2; 8: 0.095 / 8.6; 9: 0.086 / 8.6; 10: 0.086 / 9.3; 11: 0.080 / 10.0; 12: 0.076 / 10.3; 13: 0.064 / 10.7; 14: 0.066 / 10.9; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 108847, probability skill vs chance 0.2162, widened contest next: True
  - now: threshold 0.8384, hit rate recent 0.9133 / long run 0.9316
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.303, naive rule 0.537, lift 3.07x
    - 24h: 56 calls (56 a day), hit rate 0.875, chance 0.308, naive rule 0.516, lift 2.84x
    - 7d: 388 calls (55 a day), hit rate 0.930, chance 0.294, naive rule 0.493, lift 3.17x
    - 30d: 1719 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5676, hit rate recent 0.5393 / long run 0.5723
    - 6h: 18 calls (73 a day), hit rate 0.444, chance 0.303, lift 1.47x
    - 24h: 111 calls (111 a day), hit rate 0.577, chance 0.308, lift 1.87x
    - 7d: 744 calls (106 a day), hit rate 0.574, chance 0.294, lift 1.95x
    - 30d: 2592 calls (86 a day), hit rate 0.580, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.564; 0.45: 414, 0.634; 0.50: 362, 0.687; 0.55: 317, 0.729; 0.60: 270, 0.773; 0.65: 225, 0.801; 0.70: 179, 0.834; 0.75: 139, 0.870; 0.80: 95, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.525; 0.50: 203, 0.559; 0.55: 92, 0.578; 0.60: 14, 0.604; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 108845, probability skill vs chance 0.2092, widened contest next: False
  - now: threshold 0.6923, hit rate recent 0.844 / long run 0.827
    - 6h: 18 calls (73 a day), hit rate 0.833, chance 0.190, naive rule 0.465, lift 4.39x
    - 24h: 52 calls (52 a day), hit rate 0.865, chance 0.207, naive rule 0.449, lift 4.18x
    - 7d: 356 calls (51 a day), hit rate 0.823, chance 0.188, naive rule 0.407, lift 4.38x
    - 30d: 1616 calls (54 a day), hit rate 0.831, chance 0.188, naive rule 0.395, lift 4.43x
  - next: threshold 0.407, hit rate recent 0.4631 / long run 0.468
    - 6h: 35 calls (143 a day), hit rate 0.457, chance 0.190, lift 2.41x
    - 24h: 116 calls (117 a day), hit rate 0.491, chance 0.207, lift 2.37x
    - 7d: 683 calls (98 a day), hit rate 0.476, chance 0.188, lift 2.53x
    - 30d: 2308 calls (77 a day), hit rate 0.479, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 353, 0.485; 0.40: 283, 0.557; 0.45: 231, 0.613; 0.50: 182, 0.665; 0.55: 138, 0.709; 0.60: 108, 0.749; 0.65: 82, 0.792; 0.70: 60, 0.823; 0.75: 33, 0.868; 0.80: 10, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 251, 0.425; 0.40: 161, 0.452; 0.45: 77, 0.468; 0.50: 18, 0.503; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 108842, probability skill vs chance 0.1895, widened contest next: False
  - now: threshold 0.5798, hit rate recent 0.7121 / long run 0.6995
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.133, naive rule 0.395, lift 5.38x
    - 24h: 43 calls (43 a day), hit rate 0.744, chance 0.133, naive rule 0.361, lift 5.59x
    - 7d: 355 calls (51 a day), hit rate 0.690, chance 0.122, naive rule 0.336, lift 5.65x
    - 30d: 1582 calls (53 a day), hit rate 0.717, chance 0.123, naive rule 0.332, lift 5.84x
  - next: threshold 0.3412, hit rate recent 0.3891 / long run 0.3842
    - 6h: 30 calls (123 a day), hit rate 0.433, chance 0.133, lift 3.26x
    - 24h: 106 calls (107 a day), hit rate 0.406, chance 0.133, lift 3.05x
    - 7d: 619 calls (89 a day), hit rate 0.380, chance 0.122, lift 3.11x
    - 30d: 2172 calls (72 a day), hit rate 0.405, chance 0.123, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.420; 0.35: 196, 0.492; 0.40: 149, 0.553; 0.45: 118, 0.595; 0.50: 90, 0.637; 0.55: 66, 0.687; 0.60: 44, 0.730; 0.65: 24, 0.785; 0.70: 9, 0.832; 0.75: 1, 0.750
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.355; 0.35: 106, 0.388; 0.40: 43, 0.422; 0.45: 9, 0.445; 0.50: 1, 0.406
- **K=13**: model 1792022400, labels learned 108837, probability skill vs chance 0.1813, widened contest next: False
  - now: threshold 0.4256, hit rate recent 0.5772 / long run 0.575
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.088, naive rule 0.405, lift 6.46x
    - 24h: 50 calls (51 a day), hit rate 0.640, chance 0.083, naive rule 0.324, lift 7.70x
    - 7d: 369 calls (53 a day), hit rate 0.561, chance 0.078, naive rule 0.281, lift 7.23x
    - 30d: 1526 calls (51 a day), hit rate 0.588, chance 0.078, naive rule 0.275, lift 7.51x
  - next: threshold 0.2887, hit rate recent 0.3172 / long run 0.3129
    - 6h: 13 calls (54 a day), hit rate 0.231, chance 0.088, lift 2.61x
    - 24h: 38 calls (38 a day), hit rate 0.395, chance 0.083, lift 4.75x
    - 7d: 419 calls (60 a day), hit rate 0.310, chance 0.078, lift 4.00x
    - 30d: 2036 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.514; 0.40: 62, 0.567; 0.45: 41, 0.622; 0.50: 25, 0.662; 0.55: 14, 0.704; 0.60: 5, 0.748; 0.65: 1, 0.818
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.325; 0.35: 13, 0.357; 0.40: 2, 0.391

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.629 | -1.01% | 0.883 | 0.550 | 0.251 | 0.483 | 0.229 |
| 6h | 11.666 | 0.82% | 0.883 | 0.483 | 0.250 | 0.485 | 0.418 |
| 24h | 10.407 | 6.50% | 0.900 | 0.501 | 0.251 | 0.477 | 0.666 |
| 7d | 15.127 | 4.18% | 0.901 | 0.499 | 0.251 | 0.492 | 0.660 |
| 30d | 13.875 | 4.05% | 0.900 | 0.500 | 0.251 | 0.495 | 0.676 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 10.523 | 10.566 | 10.644 | 10.409 | 10.679 | 10.721 | 10.504 | 10.446 | 10.486 | 10.629 |
| 6h | 11.762 | 11.666 | 11.694 | 11.729 | 11.830 | 11.749 | 11.620 | 11.673 | 11.633 | 11.666 |
| 24h | 11.131 | 10.463 | 10.619 | 10.452 | 10.613 | 10.670 | 10.374 | 10.367 | 10.382 | 10.407 |
| 7d | 15.788 | 15.289 | 15.229 | 15.145 | 15.389 | 15.334 | 15.130 | 15.104 | 15.097 | 15.127 |
| 30d | 14.460 | 13.997 | 13.962 | 13.901 | 14.128 | 14.061 | 13.872 | 13.848 | 13.848 | 13.875 |

## Next candle

- candle starting 2026-10-17 18:13 UTC, last close 2413.19
- P(up) 0.5009, return quantiles (bp): {'05': -5.379, '10': -4.099, '25': -2.273, '40': -0.865, '50': 0.021, '60': 0.65, '75': 1.899, '90': 4.125, '95': 5.33}
- changepoint probability 0.0547, regime age 74.1 min
- agent weights: empirical 0.005, ewma 0.153, garch 0.055, har 0.148, bocpd 0.051, hmm 0.029, online_qr 0.320, lgbm 0.239

## Learning log

- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.62, 6.89, 21.68], current probabilities: [0.973, 0.027, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 18:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.188, 'l_abs': 0.729, 'l_hi': 0.749, 'l_lo': 0.747, 'b05': 0.673, 'b25': 0.668, 'b75': 0.666, 'b95': 0.655}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.451, 1.746, 1.865, 2.131, 2.293, 2.635, 2.767, 2.941, 2.925, 2.953, 3.217, 3.16, 3.489, 3.691]}
- calibration offsets (in sigma): {'05': 0.026, '10': -0.018, '25': -0.04, '40': -0.022, '50': 0.01, '60': -0.008, '75': -0.02, '90': 0.028, '95': -0.026}
