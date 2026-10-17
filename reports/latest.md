# ETH-USD 60s candle generator - report

- generated: 2026-10-17 12:34 UTC
- last closed candle: 2026-10-17 12:34 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.440 (50) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.572 (416) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.571 (77) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.540 (742) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.493 (10388) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.625 (16) | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | 0.450 (20) | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | 0.630 (27) | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | 0.600 (80) | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 0.812 (32) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | 0.485 (68) | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 0.826 (23) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | 0.426 (61) | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | 0.773 (22) | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.498 (11513) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07187, 0.1127] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5255, 'levels': [{'threshold': 0.07187, 'calls_per_day': 138.7, 'win_rate': 0.5765}, {'threshold': 0.1127, 'calls_per_day': 34.0, 'win_rate': 0.6292}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 19557, 'rate': 0.5285}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15132 | 0.337 | 0.522 (14892) | 0.598 (1316) | 0.778 (2453) |
| volatility: normal | 15131 | 0.362 | 0.514 (15070) | 0.600 (380) | 0.768 (2160) |
| volatility: wild | 15131 | 0.376 | 0.503 (15089) | 0.646 (161) | 0.772 (2085) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15260) | 0.607 (682) | 0.768 (2238) |
| session: Europe 08-13 | 9574 | 0.352 | 0.512 (9491) | 0.581 (482) | 0.778 (1488) |
| session: US 13-21 | 14880 | 0.367 | 0.507 (14784) | 0.586 (427) | 0.780 (2157) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5516) | 0.658 (266) | 0.757 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.313 | 0.337 | 0.215 | 0.215 | 0.448 | 0.215 | 0.410 | 1.130 |
| 6h | 360 | 0.340 | 0.322 | 0.234 | 0.256 | 0.536 | 0.261 | 0.418 | 1.235 |
| 24h | 1440 | 0.368 | 0.348 | 0.273 | 0.303 | 0.536 | 0.272 | 0.463 | 1.107 |
| 7d | 10080 | 0.362 | 0.352 | 0.278 | 0.308 | 0.525 | 0.260 | 0.464 | 1.270 |
| 30d | 43200 | 0.359 | 0.355 | 0.280 | 0.309 | 0.514 | 0.251 | 0.466 | 1.305 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.313 / 0.448 / 0.867; 2: 0.348 / 0.517 / 0.883; 3: 0.344 / 0.500 / 0.850; 4: 0.355 / 0.603 / 0.850; 5: 0.315 / 0.362 / 0.867; 6: 0.310 / 0.414 / 0.883; 7: 0.376 / 0.603 / 0.900; 8: 0.334 / 0.448 / 0.867; 9: 0.356 / 0.569 / 0.917; 10: 0.312 / 0.466 / 0.967; 11: 0.323 / 0.483 / 0.933; 12: 0.334 / 0.466 / 0.867; 13: 0.343 / 0.483 / 0.917; 14: 0.344 / 0.517 / 0.800; 15: 0.361 / 0.603 / 0.850
- 6h: 1: 0.340 / 0.536 / 0.869; 2: 0.328 / 0.501 / 0.897; 3: 0.325 / 0.510 / 0.911; 4: 0.325 / 0.524 / 0.903; 5: 0.317 / 0.467 / 0.914; 6: 0.315 / 0.447 / 0.925; 7: 0.329 / 0.519 / 0.931; 8: 0.325 / 0.479 / 0.925; 9: 0.328 / 0.487 / 0.928; 10: 0.325 / 0.499 / 0.936; 11: 0.314 / 0.479 / 0.936; 12: 0.318 / 0.470 / 0.900; 13: 0.327 / 0.493 / 0.931; 14: 0.314 / 0.484 / 0.889; 15: 0.326 / 0.510 / 0.892
- 24h: 1: 0.368 / 0.536 / 0.894; 2: 0.353 / 0.498 / 0.906; 3: 0.349 / 0.483 / 0.903; 4: 0.347 / 0.497 / 0.903; 5: 0.349 / 0.496 / 0.904; 6: 0.347 / 0.488 / 0.909; 7: 0.349 / 0.498 / 0.910; 8: 0.351 / 0.505 / 0.909; 9: 0.352 / 0.503 / 0.907; 10: 0.351 / 0.506 / 0.908; 11: 0.339 / 0.481 / 0.908; 12: 0.352 / 0.503 / 0.903; 13: 0.353 / 0.507 / 0.908; 14: 0.347 / 0.495 / 0.903; 15: 0.349 / 0.511 / 0.903
- 7d: 1: 0.362 / 0.525 / 0.903; 2: 0.351 / 0.499 / 0.901; 3: 0.354 / 0.508 / 0.901; 4: 0.349 / 0.497 / 0.901; 5: 0.352 / 0.505 / 0.901; 6: 0.350 / 0.501 / 0.901; 7: 0.350 / 0.502 / 0.902; 8: 0.348 / 0.499 / 0.900; 9: 0.350 / 0.503 / 0.900; 10: 0.350 / 0.506 / 0.901; 11: 0.345 / 0.493 / 0.901; 12: 0.349 / 0.504 / 0.900; 13: 0.348 / 0.503 / 0.901; 14: 0.345 / 0.498 / 0.900; 15: 0.349 / 0.506 / 0.900
- 30d: 1: 0.359 / 0.514 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.498 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.218 (body 0.179, range 0.258); 'price stays where it was' would score 0.174; colour right 0.552; typical miss of the close 2.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.174 (body 0.135, range 0.214); 'price stays where it was' would score 0.171; colour right 0.524; typical miss of the close 3.4 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.138 (body 0.095, range 0.182); 'price stays where it was' would score 0.152; colour right 0.509; typical miss of the close 6.2 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.162); 'price stays where it was' would score 0.131; colour right 0.496; typical miss of the close 8.2 bp; chain ended on the right side 0.511 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.496; typical miss of the close 7.9 bp; chain ended on the right side 0.515 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.0; 2: 0.197 / 4.5; 3: 0.165 / 6.0; 4: 0.133 / 6.7; 5: 0.121 / 7.3; 6: 0.109 / 7.9; 7: 0.102 / 8.2; 8: 0.096 / 8.6; 9: 0.087 / 8.6; 10: 0.086 / 9.4; 11: 0.081 / 10.0; 12: 0.076 / 10.3; 13: 0.064 / 10.7; 14: 0.066 / 11.0; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 108508, probability skill vs chance 0.219, widened contest next: False
  - now: threshold 0.8387, hit rate recent 0.9076 / long run 0.9316
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.341, naive rule 0.586, lift 2.44x
    - 24h: 53 calls (53 a day), hit rate 0.887, chance 0.297, naive rule 0.485, lift 2.99x
    - 7d: 391 calls (56 a day), hit rate 0.931, chance 0.295, naive rule 0.494, lift 3.16x
    - 30d: 1721 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.482, lift 3.22x
  - next: threshold 0.5615, hit rate recent 0.5519 / long run 0.5752
    - 6h: 38 calls (154 a day), hit rate 0.526, chance 0.341, lift 1.54x
    - 24h: 131 calls (131 a day), hit rate 0.573, chance 0.297, lift 1.93x
    - 7d: 760 calls (109 a day), hit rate 0.582, chance 0.295, lift 1.97x
    - 30d: 2598 calls (87 a day), hit rate 0.580, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 541, 0.513; 0.40: 484, 0.563; 0.45: 415, 0.633; 0.50: 362, 0.686; 0.55: 317, 0.729; 0.60: 270, 0.773; 0.65: 224, 0.801; 0.70: 180, 0.834; 0.75: 139, 0.870; 0.80: 95, 0.910; 0.85: 49, 0.949; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 409, 0.490; 0.45: 313, 0.524; 0.50: 204, 0.558; 0.55: 92, 0.579; 0.60: 14, 0.603; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 108506, probability skill vs chance 0.2059, widened contest next: False
  - now: threshold 0.6927, hit rate recent 0.8425 / long run 0.8267
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.214, naive rule 0.467, lift 3.67x
    - 24h: 45 calls (45 a day), hit rate 0.889, chance 0.201, naive rule 0.417, lift 4.42x
    - 7d: 356 calls (51 a day), hit rate 0.826, chance 0.189, naive rule 0.407, lift 4.38x
    - 30d: 1607 calls (54 a day), hit rate 0.831, chance 0.188, naive rule 0.394, lift 4.43x
  - next: threshold 0.411, hit rate recent 0.4401 / long run 0.4677
    - 6h: 36 calls (147 a day), hit rate 0.417, chance 0.214, lift 1.95x
    - 24h: 120 calls (121 a day), hit rate 0.450, chance 0.201, lift 2.24x
    - 7d: 671 calls (96 a day), hit rate 0.474, chance 0.189, lift 2.51x
    - 30d: 2291 calls (76 a day), hit rate 0.479, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 353, 0.484; 0.40: 283, 0.557; 0.45: 232, 0.612; 0.50: 182, 0.664; 0.55: 138, 0.708; 0.60: 108, 0.748; 0.65: 81, 0.792; 0.70: 60, 0.823; 0.75: 33, 0.867; 0.80: 10, 0.883
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.389; 0.35: 251, 0.424; 0.40: 161, 0.452; 0.45: 77, 0.469; 0.50: 18, 0.504; 0.55: 2, 0.560
- **K=8**: model 1791936000, labels learned 108503, probability skill vs chance 0.1866, widened contest next: False
  - now: threshold 0.5801, hit rate recent 0.7083 / long run 0.6991
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.126, naive rule 0.354, lift 6.12x
    - 24h: 45 calls (45 a day), hit rate 0.778, chance 0.124, naive rule 0.323, lift 6.28x
    - 7d: 355 calls (51 a day), hit rate 0.687, chance 0.122, naive rule 0.336, lift 5.61x
    - 30d: 1577 calls (53 a day), hit rate 0.716, chance 0.123, naive rule 0.331, lift 5.84x
  - next: threshold 0.3412, hit rate recent 0.3545 / long run 0.3814
    - 6h: 33 calls (136 a day), hit rate 0.333, chance 0.126, lift 2.65x
    - 24h: 115 calls (116 a day), hit rate 0.348, chance 0.124, lift 2.81x
    - 7d: 607 calls (87 a day), hit rate 0.374, chance 0.122, lift 3.05x
    - 30d: 2166 calls (72 a day), hit rate 0.404, chance 0.123, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.419; 0.35: 196, 0.491; 0.40: 149, 0.552; 0.45: 118, 0.595; 0.50: 90, 0.636; 0.55: 65, 0.686; 0.60: 44, 0.729; 0.65: 24, 0.783; 0.70: 9, 0.835; 0.75: 1, 0.783
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.355; 0.35: 106, 0.388; 0.40: 43, 0.420; 0.45: 9, 0.446; 0.50: 1, 0.394
- **K=13**: model 1792022400, labels learned 108498, probability skill vs chance 0.1748, widened contest next: False
  - now: threshold 0.4381, hit rate recent 0.5774 / long run 0.5751
    - 6h: 15 calls (63 a day), hit rate 0.667, chance 0.080, naive rule 0.298, lift 8.36x
    - 24h: 55 calls (56 a day), hit rate 0.636, chance 0.078, naive rule 0.273, lift 8.13x
    - 7d: 372 calls (53 a day), hit rate 0.559, chance 0.078, naive rule 0.279, lift 7.18x
    - 30d: 1519 calls (51 a day), hit rate 0.587, chance 0.078, naive rule 0.273, lift 7.53x
  - next: threshold 0.3005, hit rate recent 0.3305 / long run 0.3141
    - 6h: 10 calls (42 a day), hit rate 0.200, chance 0.080, lift 2.51x
    - 24h: 50 calls (51 a day), hit rate 0.320, chance 0.078, lift 4.09x
    - 7d: 421 calls (60 a day), hit rate 0.311, chance 0.078, lift 3.99x
    - 30d: 2036 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.513; 0.40: 61, 0.565; 0.45: 41, 0.621; 0.50: 25, 0.663; 0.55: 14, 0.707; 0.60: 4, 0.754; 0.65: 1, 0.895
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.325; 0.35: 13, 0.361; 0.40: 2, 0.391

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.114 | 11.97% | 0.917 | 0.483 | 0.251 | 0.483 | 0.401 |
| 6h | 7.325 | 11.27% | 0.886 | 0.492 | 0.251 | 0.467 | 0.379 |
| 24h | 13.315 | 7.06% | 0.900 | 0.501 | 0.251 | 0.478 | 0.758 |
| 7d | 14.970 | 4.26% | 0.901 | 0.500 | 0.251 | 0.489 | 0.665 |
| 30d | 13.952 | 4.05% | 0.900 | 0.500 | 0.251 | 0.495 | 0.677 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.081 | 7.227 | 7.557 | 7.092 | 7.469 | 7.850 | 7.079 | 7.145 | 7.119 | 7.114 |
| 6h | 8.255 | 7.381 | 7.678 | 7.380 | 7.521 | 7.850 | 7.288 | 7.291 | 7.307 | 7.325 |
| 24h | 14.327 | 13.457 | 13.520 | 13.360 | 13.551 | 13.577 | 13.313 | 13.314 | 13.296 | 13.315 |
| 7d | 15.636 | 15.135 | 15.073 | 14.987 | 15.233 | 15.179 | 14.976 | 14.946 | 14.942 | 14.970 |
| 30d | 14.541 | 14.075 | 14.040 | 13.977 | 14.208 | 14.139 | 13.949 | 13.924 | 13.925 | 13.952 |

## Next candle

- candle starting 2026-10-17 12:34 UTC, last close 2427.77
- P(up) 0.4894, return quantiles (bp): {'05': -4.523, '10': -3.327, '25': -1.84, '40': -0.692, '50': -0.065, '60': 0.566, '75': 1.529, '90': 3.24, '95': 4.59}
- changepoint probability 0.0695, regime age 31.4 min
- agent weights: empirical 0.003, ewma 0.128, garch 0.023, har 0.178, bocpd 0.048, hmm 0.012, online_qr 0.304, lgbm 0.305

## Learning log

- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.62, 6.89, 21.68], current probabilities: [0.976, 0.023, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 12:45 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.201, 'l_abs': 0.728, 'l_hi': 0.751, 'l_lo': 0.751, 'b05': 0.691, 'b25': 0.681, 'b75': 0.682, 'b95': 0.651}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.449, 1.708, 2.016, 2.127, 2.288, 2.38, 2.817, 2.877, 2.978, 3.13, 3.693, 3.217, 3.926, 3.991]}
- calibration offsets (in sigma): {'05': 0.0765, '10': 0.073, '25': -0.0175, '40': -0.028, '50': -0.035, '60': -0.032, '75': -0.0525, '90': -0.063, '95': -0.0365}
