# ETH-USD 60s candle generator - report

- generated: 2026-10-17 15:55 UTC
- last closed candle: 2026-10-17 15:55 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.460 (63) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.577 (539) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.553 (94) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.543 (941) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.491 (13174) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.600 (25) | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | 0.357 (28) | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | 0.571 (35) | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | 0.554 (92) | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 0.829 (41) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | 0.460 (87) | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 0.800 (35) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | 0.416 (77) | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | 0.710 (31) | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.496 (14604) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07187, 0.1127] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5255, 'levels': [{'threshold': 0.07187, 'calls_per_day': 138.7, 'win_rate': 0.5765}, {'threshold': 0.1127, 'calls_per_day': 34.0, 'win_rate': 0.6292}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 19756, 'rate': 0.5287}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15199 | 0.337 | 0.522 (14958) | 0.596 (1330) | 0.776 (2470) |
| volatility: normal | 15198 | 0.362 | 0.514 (15136) | 0.603 (383) | 0.767 (2171) |
| volatility: wild | 15198 | 0.376 | 0.503 (15156) | 0.646 (161) | 0.772 (2095) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15260) | 0.607 (682) | 0.768 (2238) |
| session: Europe 08-13 | 9600 | 0.352 | 0.512 (9517) | 0.580 (486) | 0.777 (1499) |
| session: US 13-21 | 15055 | 0.367 | 0.507 (14957) | 0.582 (440) | 0.778 (2184) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5516) | 0.658 (266) | 0.757 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.346 | 0.319 | 0.245 | 0.245 | 0.500 | 0.249 | 0.443 | 1.229 |
| 6h | 360 | 0.346 | 0.325 | 0.245 | 0.270 | 0.537 | 0.266 | 0.426 | 1.150 |
| 24h | 1440 | 0.362 | 0.342 | 0.266 | 0.289 | 0.541 | 0.272 | 0.451 | 1.120 |
| 7d | 10080 | 0.363 | 0.353 | 0.277 | 0.308 | 0.526 | 0.261 | 0.464 | 1.255 |
| 30d | 43200 | 0.359 | 0.355 | 0.280 | 0.309 | 0.514 | 0.252 | 0.466 | 1.302 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.346 / 0.500 / 0.833; 2: 0.316 / 0.345 / 0.867; 3: 0.323 / 0.431 / 0.867; 4: 0.349 / 0.431 / 0.800; 5: 0.342 / 0.534 / 0.800; 6: 0.337 / 0.466 / 0.767; 7: 0.353 / 0.517 / 0.767; 8: 0.323 / 0.466 / 0.783; 9: 0.341 / 0.483 / 0.750; 10: 0.349 / 0.603 / 0.717; 11: 0.335 / 0.500 / 0.717; 12: 0.322 / 0.517 / 0.733; 13: 0.319 / 0.448 / 0.700; 14: 0.336 / 0.603 / 0.733; 15: 0.348 / 0.466 / 0.733
- 6h: 1: 0.346 / 0.537 / 0.864; 2: 0.337 / 0.489 / 0.908; 3: 0.327 / 0.463 / 0.889; 4: 0.348 / 0.545 / 0.878; 5: 0.330 / 0.486 / 0.875; 6: 0.321 / 0.458 / 0.883; 7: 0.340 / 0.520 / 0.869; 8: 0.324 / 0.469 / 0.875; 9: 0.332 / 0.489 / 0.875; 10: 0.320 / 0.466 / 0.881; 11: 0.319 / 0.475 / 0.878; 12: 0.315 / 0.472 / 0.861; 13: 0.327 / 0.489 / 0.875; 14: 0.317 / 0.492 / 0.847; 15: 0.327 / 0.494 / 0.850
- 24h: 1: 0.362 / 0.541 / 0.889; 2: 0.346 / 0.490 / 0.899; 3: 0.341 / 0.481 / 0.901; 4: 0.341 / 0.492 / 0.897; 5: 0.344 / 0.499 / 0.906; 6: 0.340 / 0.485 / 0.907; 7: 0.344 / 0.498 / 0.903; 8: 0.341 / 0.490 / 0.905; 9: 0.344 / 0.492 / 0.902; 10: 0.347 / 0.511 / 0.906; 11: 0.331 / 0.477 / 0.906; 12: 0.345 / 0.504 / 0.903; 13: 0.345 / 0.509 / 0.907; 14: 0.337 / 0.488 / 0.901; 15: 0.341 / 0.503 / 0.905
- 7d: 1: 0.363 / 0.526 / 0.903; 2: 0.351 / 0.498 / 0.901; 3: 0.354 / 0.506 / 0.901; 4: 0.350 / 0.497 / 0.903; 5: 0.352 / 0.504 / 0.902; 6: 0.351 / 0.501 / 0.903; 7: 0.350 / 0.502 / 0.904; 8: 0.349 / 0.499 / 0.903; 9: 0.350 / 0.503 / 0.902; 10: 0.351 / 0.506 / 0.904; 11: 0.345 / 0.492 / 0.904; 12: 0.349 / 0.504 / 0.905; 13: 0.349 / 0.503 / 0.905; 14: 0.346 / 0.498 / 0.904; 15: 0.349 / 0.505 / 0.903
- 30d: 1: 0.359 / 0.514 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.348 / 0.502 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.071 (body 0.038, range 0.103); 'price stays where it was' would score 0.067; colour right 0.483; typical miss of the close 10.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.132 (body 0.098, range 0.167); 'price stays where it was' would score 0.124; colour right 0.542; typical miss of the close 6.6 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.137 (body 0.095, range 0.179); 'price stays where it was' would score 0.150; colour right 0.508; typical miss of the close 5.9 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.132; colour right 0.497; typical miss of the close 8.3 bp; chain ended on the right side 0.510 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.9 bp; chain ended on the right side 0.516 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.0; 2: 0.197 / 4.4; 3: 0.165 / 6.0; 4: 0.133 / 6.6; 5: 0.121 / 7.3; 6: 0.109 / 7.8; 7: 0.102 / 8.2; 8: 0.095 / 8.6; 9: 0.086 / 8.6; 10: 0.085 / 9.3; 11: 0.081 / 10.0; 12: 0.076 / 10.3; 13: 0.064 / 10.7; 14: 0.066 / 10.9; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 108709, probability skill vs chance 0.216, widened contest next: True
  - now: threshold 0.8387, hit rate recent 0.9057 / long run 0.931
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.301, naive rule 0.533, lift 2.84x
    - 24h: 54 calls (54 a day), hit rate 0.870, chance 0.298, naive rule 0.490, lift 2.93x
    - 7d: 390 calls (56 a day), hit rate 0.931, chance 0.294, naive rule 0.493, lift 3.17x
    - 30d: 1718 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5615, hit rate recent 0.4989 / long run 0.5688
    - 6h: 28 calls (114 a day), hit rate 0.321, chance 0.301, lift 1.07x
    - 24h: 119 calls (119 a day), hit rate 0.538, chance 0.298, lift 1.81x
    - 7d: 753 calls (108 a day), hit rate 0.575, chance 0.294, lift 1.96x
    - 30d: 2597 calls (87 a day), hit rate 0.580, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.564; 0.45: 414, 0.634; 0.50: 362, 0.687; 0.55: 317, 0.729; 0.60: 270, 0.773; 0.65: 224, 0.801; 0.70: 179, 0.834; 0.75: 139, 0.870; 0.80: 95, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.525; 0.50: 203, 0.558; 0.55: 92, 0.577; 0.60: 14, 0.603; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 108707, probability skill vs chance 0.2064, widened contest next: True
  - now: threshold 0.6927, hit rate recent 0.8275 / long run 0.8252
    - 6h: 18 calls (73 a day), hit rate 0.722, chance 0.194, naive rule 0.436, lift 3.72x
    - 24h: 48 calls (48 a day), hit rate 0.854, chance 0.200, naive rule 0.422, lift 4.26x
    - 7d: 360 calls (51 a day), hit rate 0.822, chance 0.188, naive rule 0.406, lift 4.38x
    - 30d: 1612 calls (54 a day), hit rate 0.831, chance 0.188, naive rule 0.394, lift 4.43x
  - next: threshold 0.411, hit rate recent 0.4242 / long run 0.4647
    - 6h: 37 calls (151 a day), hit rate 0.351, chance 0.194, lift 1.81x
    - 24h: 116 calls (117 a day), hit rate 0.457, chance 0.200, lift 2.28x
    - 7d: 673 calls (96 a day), hit rate 0.470, chance 0.188, lift 2.50x
    - 30d: 2300 calls (77 a day), hit rate 0.479, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 352, 0.485; 0.40: 283, 0.557; 0.45: 231, 0.612; 0.50: 181, 0.665; 0.55: 138, 0.709; 0.60: 108, 0.748; 0.65: 81, 0.792; 0.70: 60, 0.823; 0.75: 33, 0.868; 0.80: 10, 0.884
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.389; 0.35: 251, 0.424; 0.40: 161, 0.452; 0.45: 77, 0.468; 0.50: 18, 0.503; 0.55: 2, 0.549
- **K=8**: model 1791936000, labels learned 108704, probability skill vs chance 0.1853, widened contest next: False
  - now: threshold 0.5801, hit rate recent 0.6869 / long run 0.697
    - 6h: 15 calls (62 a day), hit rate 0.600, chance 0.130, naive rule 0.357, lift 4.62x
    - 24h: 44 calls (44 a day), hit rate 0.705, chance 0.127, naive rule 0.331, lift 5.54x
    - 7d: 358 calls (51 a day), hit rate 0.690, chance 0.122, naive rule 0.336, lift 5.64x
    - 30d: 1579 calls (53 a day), hit rate 0.716, chance 0.123, naive rule 0.331, lift 5.83x
  - next: threshold 0.3412, hit rate recent 0.3574 / long run 0.3812
    - 6h: 34 calls (140 a day), hit rate 0.324, chance 0.130, lift 2.49x
    - 24h: 109 calls (110 a day), hit rate 0.358, chance 0.127, lift 2.81x
    - 7d: 612 calls (88 a day), hit rate 0.374, chance 0.122, lift 3.06x
    - 30d: 2171 calls (72 a day), hit rate 0.404, chance 0.123, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.420; 0.35: 196, 0.492; 0.40: 149, 0.552; 0.45: 118, 0.595; 0.50: 90, 0.636; 0.55: 65, 0.686; 0.60: 44, 0.729; 0.65: 24, 0.784; 0.70: 9, 0.832; 0.75: 1, 0.760
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.355; 0.35: 106, 0.387; 0.40: 43, 0.421; 0.45: 9, 0.446; 0.50: 1, 0.406
- **K=13**: model 1792022400, labels learned 108699, probability skill vs chance 0.1741, widened contest next: False
  - now: threshold 0.4381, hit rate recent 0.5507 / long run 0.5724
    - 6h: 16 calls (67 a day), hit rate 0.438, chance 0.080, naive rule 0.310, lift 5.49x
    - 24h: 52 calls (53 a day), hit rate 0.577, chance 0.080, naive rule 0.286, lift 7.24x
    - 7d: 370 calls (53 a day), hit rate 0.562, chance 0.078, naive rule 0.281, lift 7.20x
    - 30d: 1521 calls (51 a day), hit rate 0.587, chance 0.078, naive rule 0.274, lift 7.51x
  - next: threshold 0.3005, hit rate recent 0.3045 / long run 0.3116
    - 6h: 14 calls (58 a day), hit rate 0.071, chance 0.080, lift 0.90x
    - 24h: 45 calls (45 a day), hit rate 0.311, chance 0.080, lift 3.91x
    - 7d: 418 calls (60 a day), hit rate 0.309, chance 0.078, lift 3.95x
    - 30d: 2037 calls (68 a day), hit rate 0.313, chance 0.078, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.513; 0.40: 61, 0.566; 0.45: 41, 0.621; 0.50: 25, 0.662; 0.55: 14, 0.704; 0.60: 4, 0.750; 0.65: 1, 0.857
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.324; 0.35: 13, 0.357; 0.40: 2, 0.391

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.941 | 2.01% | 0.883 | 0.500 | 0.252 | 0.397 | 0.442 |
| 6h | 9.741 | 3.90% | 0.886 | 0.461 | 0.251 | 0.475 | 0.464 |
| 24h | 11.762 | 7.44% | 0.899 | 0.497 | 0.251 | 0.476 | 0.749 |
| 7d | 15.048 | 4.20% | 0.901 | 0.498 | 0.251 | 0.490 | 0.662 |
| 30d | 13.888 | 4.05% | 0.900 | 0.500 | 0.251 | 0.495 | 0.676 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.206 | 13.088 | 13.022 | 12.945 | 13.103 | 13.145 | 13.016 | 13.192 | 13.029 | 12.941 |
| 6h | 10.136 | 9.807 | 9.852 | 9.798 | 9.929 | 9.973 | 9.697 | 9.770 | 9.728 | 9.741 |
| 24h | 12.707 | 11.899 | 11.967 | 11.833 | 11.982 | 11.982 | 11.763 | 11.764 | 11.752 | 11.762 |
| 7d | 15.708 | 15.210 | 15.150 | 15.066 | 15.310 | 15.255 | 15.052 | 15.025 | 15.019 | 15.048 |
| 30d | 14.474 | 14.010 | 13.975 | 13.914 | 14.141 | 14.074 | 13.886 | 13.861 | 13.862 | 13.888 |

## Next candle

- candle starting 2026-10-17 15:55 UTC, last close 2404.31
- P(up) 0.5011, return quantiles (bp): {'05': -8.448, '10': -6.327, '25': -3.403, '40': -1.288, '50': 0.019, '60': 1.206, '75': 2.89, '90': 5.805, '95': 7.699}
- changepoint probability 0.0462, regime age 34.5 min
- agent weights: empirical 0.003, ewma 0.142, garch 0.052, har 0.155, bocpd 0.057, hmm 0.025, online_qr 0.318, lgbm 0.248

## Learning log

- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.62, 6.89, 21.68], current probabilities: [0.348, 0.643, 0.009]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 16:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.164, 'l_abs': 0.733, 'l_hi': 0.751, 'l_lo': 0.748, 'b05': 0.681, 'b25': 0.678, 'b75': 0.684, 'b95': 0.651}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.446, 1.81, 2.18, 2.393, 2.474, 2.787, 2.985, 3.302, 3.419, 3.593, 3.914, 3.768, 4.244, 4.229]}
- calibration offsets (in sigma): {'05': 0.017, '10': -0.026, '25': -0.115, '40': -0.094, '50': -0.06, '60': -0.046, '75': -0.055, '90': -0.034, '95': -0.067}
