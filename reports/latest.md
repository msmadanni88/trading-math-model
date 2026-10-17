# ETH-USD 60s candle generator - report

- generated: 2026-10-17 04:43 UTC
- last closed candle: 2026-10-17 04:43 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.444 (18) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.603 (161) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.630 (27) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.564 (280) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.499 (3920) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.600 (5) | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | 0.714 (7) | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | 0.500 (10) | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | 0.697 (33) | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 0.692 (13) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | 0.591 (22) | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 0.857 (7) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | 0.545 (22) | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | 0.714 (7) | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.507 (4339) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07348, 0.1157] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5252, 'levels': [{'threshold': 0.07348, 'calls_per_day': 141.7, 'win_rate': 0.5838}, {'threshold': 0.1157, 'calls_per_day': 35.6, 'win_rate': 0.6627}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 19095, 'rate': 0.5285}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14975 | 0.337 | 0.521 (14741) | 0.603 (1275) | 0.776 (2428) |
| volatility: normal | 14974 | 0.363 | 0.514 (14915) | 0.589 (372) | 0.769 (2138) |
| volatility: wild | 14974 | 0.376 | 0.503 (14933) | 0.650 (160) | 0.771 (2065) |
| session: Asia 00-08 | 15163 | 0.357 | 0.519 (15065) | 0.605 (664) | 0.767 (2217) |
| session: Europe 08-13 | 9300 | 0.352 | 0.511 (9224) | 0.589 (450) | 0.779 (1442) |
| session: US 13-21 | 14880 | 0.367 | 0.507 (14784) | 0.586 (427) | 0.780 (2157) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5516) | 0.658 (266) | 0.757 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.349 | 0.318 | 0.230 | 0.230 | 0.610 | 0.270 | 0.427 | 1.738 |
| 6h | 360 | 0.371 | 0.341 | 0.265 | 0.297 | 0.549 | 0.286 | 0.456 | 1.339 |
| 24h | 1440 | 0.377 | 0.358 | 0.289 | 0.318 | 0.528 | 0.269 | 0.484 | 1.272 |
| 7d | 10080 | 0.360 | 0.351 | 0.276 | 0.306 | 0.526 | 0.260 | 0.460 | 1.288 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.310 | 0.513 | 0.251 | 0.466 | 1.303 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.349 / 0.610 / 0.867; 2: 0.308 / 0.492 / 0.883; 3: 0.302 / 0.441 / 0.900; 4: 0.294 / 0.441 / 0.900; 5: 0.347 / 0.559 / 0.950; 6: 0.312 / 0.559 / 0.917; 7: 0.317 / 0.458 / 0.950; 8: 0.316 / 0.542 / 0.933; 9: 0.305 / 0.441 / 0.967; 10: 0.304 / 0.492 / 0.967; 11: 0.277 / 0.373 / 0.967; 12: 0.306 / 0.542 / 1.000; 13: 0.300 / 0.508 / 0.983; 14: 0.298 / 0.475 / 0.983; 15: 0.310 / 0.576 / 1.000
- 6h: 1: 0.371 / 0.549 / 0.883; 2: 0.338 / 0.471 / 0.875; 3: 0.344 / 0.482 / 0.850; 4: 0.326 / 0.443 / 0.858; 5: 0.357 / 0.546 / 0.861; 6: 0.353 / 0.543 / 0.867; 7: 0.333 / 0.448 / 0.864; 8: 0.346 / 0.518 / 0.850; 9: 0.345 / 0.485 / 0.864; 10: 0.346 / 0.527 / 0.867; 11: 0.332 / 0.479 / 0.850; 12: 0.350 / 0.521 / 0.889; 13: 0.342 / 0.504 / 0.886; 14: 0.342 / 0.490 / 0.894; 15: 0.344 / 0.515 / 0.892
- 24h: 1: 0.377 / 0.528 / 0.899; 2: 0.362 / 0.498 / 0.899; 3: 0.361 / 0.486 / 0.894; 4: 0.358 / 0.497 / 0.892; 5: 0.364 / 0.502 / 0.893; 6: 0.361 / 0.509 / 0.892; 7: 0.354 / 0.486 / 0.892; 8: 0.361 / 0.502 / 0.890; 9: 0.362 / 0.518 / 0.892; 10: 0.360 / 0.502 / 0.896; 11: 0.350 / 0.477 / 0.895; 12: 0.360 / 0.500 / 0.905; 13: 0.360 / 0.497 / 0.903; 14: 0.355 / 0.489 / 0.902; 15: 0.358 / 0.509 / 0.903
- 7d: 1: 0.360 / 0.526 / 0.903; 2: 0.348 / 0.497 / 0.900; 3: 0.352 / 0.510 / 0.899; 4: 0.347 / 0.497 / 0.899; 5: 0.351 / 0.509 / 0.898; 6: 0.349 / 0.504 / 0.898; 7: 0.347 / 0.501 / 0.898; 8: 0.346 / 0.501 / 0.897; 9: 0.348 / 0.505 / 0.898; 10: 0.349 / 0.509 / 0.898; 11: 0.344 / 0.493 / 0.898; 12: 0.347 / 0.505 / 0.899; 13: 0.346 / 0.503 / 0.898; 14: 0.344 / 0.499 / 0.899; 15: 0.347 / 0.505 / 0.899
- 30d: 1: 0.358 / 0.513 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.099 (body 0.064, range 0.134); 'price stays where it was' would score 0.128; colour right 0.458; typical miss of the close 3.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.129 (body 0.086, range 0.171); 'price stays where it was' would score 0.145; colour right 0.476; typical miss of the close 4.9 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.122 (body 0.078, range 0.165); 'price stays where it was' would score 0.133; colour right 0.493; typical miss of the close 8.7 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.120 (body 0.081, range 0.159); 'price stays where it was' would score 0.128; colour right 0.495; typical miss of the close 8.1 bp; chain ended on the right side 0.516 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 7.9 bp; chain ended on the right side 0.517 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.1; 2: 0.196 / 4.5; 3: 0.164 / 6.0; 4: 0.132 / 6.7; 5: 0.121 / 7.4; 6: 0.109 / 7.9; 7: 0.101 / 8.3; 8: 0.096 / 8.7; 9: 0.086 / 8.7; 10: 0.084 / 9.4; 11: 0.079 / 10.2; 12: 0.076 / 10.5; 13: 0.064 / 10.8; 14: 0.066 / 11.1; 15: 0.058 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 108037, probability skill vs chance 0.2262, widened contest next: False
  - now: threshold 0.8398, hit rate recent 0.9148 / long run 0.9328
    - 6h: 15 calls (61 a day), hit rate 0.733, chance 0.292, naive rule 0.473, lift 2.52x
    - 24h: 50 calls (50 a day), hit rate 0.920, chance 0.278, naive rule 0.456, lift 3.31x
    - 7d: 392 calls (56 a day), hit rate 0.934, chance 0.293, naive rule 0.490, lift 3.19x
    - 30d: 1721 calls (57 a day), hit rate 0.937, chance 0.290, naive rule 0.481, lift 3.23x
  - next: threshold 0.5266, hit rate recent 0.6168 / long run 0.579
    - 6h: 37 calls (150 a day), hit rate 0.676, chance 0.292, lift 2.32x
    - 24h: 135 calls (135 a day), hit rate 0.578, chance 0.278, lift 2.08x
    - 7d: 749 calls (107 a day), hit rate 0.582, chance 0.293, lift 1.99x
    - 30d: 2578 calls (86 a day), hit rate 0.581, chance 0.290, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.489; 0.35: 540, 0.512; 0.40: 484, 0.562; 0.45: 415, 0.632; 0.50: 362, 0.685; 0.55: 317, 0.728; 0.60: 270, 0.772; 0.65: 224, 0.800; 0.70: 180, 0.834; 0.75: 139, 0.871; 0.80: 95, 0.912; 0.85: 49, 0.950; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 498, 0.459; 0.40: 409, 0.489; 0.45: 314, 0.524; 0.50: 204, 0.559; 0.55: 92, 0.578; 0.60: 14, 0.598; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 108035, probability skill vs chance 0.2166, widened contest next: False
  - now: threshold 0.6957, hit rate recent 0.8542 / long run 0.8271
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.203, naive rule 0.411, lift 4.32x
    - 24h: 54 calls (54 a day), hit rate 0.870, chance 0.180, naive rule 0.380, lift 4.84x
    - 7d: 358 calls (51 a day), hit rate 0.832, chance 0.187, naive rule 0.405, lift 4.44x
    - 30d: 1600 calls (53 a day), hit rate 0.831, chance 0.187, naive rule 0.393, lift 4.44x
  - next: threshold 0.4148, hit rate recent 0.4799 / long run 0.4706
    - 6h: 25 calls (102 a day), hit rate 0.600, chance 0.203, lift 2.96x
    - 24h: 120 calls (121 a day), hit rate 0.442, chance 0.180, lift 2.46x
    - 7d: 651 calls (93 a day), hit rate 0.478, chance 0.187, lift 2.55x
    - 30d: 2267 calls (76 a day), hit rate 0.481, chance 0.187, lift 2.57x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 353, 0.483; 0.40: 283, 0.556; 0.45: 232, 0.612; 0.50: 182, 0.664; 0.55: 138, 0.708; 0.60: 108, 0.748; 0.65: 81, 0.792; 0.70: 60, 0.825; 0.75: 33, 0.868; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 251, 0.425; 0.40: 161, 0.453; 0.45: 77, 0.468; 0.50: 18, 0.507; 0.55: 2, 0.560
- **K=8**: model 1791936000, labels learned 108032, probability skill vs chance 0.1953, widened contest next: False
  - now: threshold 0.5822, hit rate recent 0.6849 / long run 0.6966
    - 6h: 8 calls (33 a day), hit rate 0.750, chance 0.134, naive rule 0.362, lift 5.59x
    - 24h: 51 calls (51 a day), hit rate 0.686, chance 0.115, naive rule 0.295, lift 5.95x
    - 7d: 361 calls (52 a day), hit rate 0.695, chance 0.123, naive rule 0.338, lift 5.67x
    - 30d: 1576 calls (53 a day), hit rate 0.714, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.341, hit rate recent 0.3713 / long run 0.3831
    - 6h: 25 calls (103 a day), hit rate 0.560, chance 0.134, lift 4.17x
    - 24h: 120 calls (121 a day), hit rate 0.325, chance 0.115, lift 2.82x
    - 7d: 593 calls (85 a day), hit rate 0.381, chance 0.123, lift 3.11x
    - 30d: 2148 calls (72 a day), hit rate 0.405, chance 0.122, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.419; 0.35: 196, 0.492; 0.40: 149, 0.552; 0.45: 118, 0.594; 0.50: 90, 0.635; 0.55: 65, 0.685; 0.60: 44, 0.727; 0.65: 24, 0.782; 0.70: 9, 0.837; 0.75: 1, 0.792
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.354; 0.35: 107, 0.388; 0.40: 43, 0.420; 0.45: 9, 0.447; 0.50: 1, 0.382
- **K=13**: model 1792022400, labels learned 108027, probability skill vs chance 0.1801, widened contest next: True
  - now: threshold 0.4335, hit rate recent 0.5398 / long run 0.5714
    - 6h: 11 calls (46 a day), hit rate 0.545, chance 0.083, naive rule 0.333, lift 6.60x
    - 24h: 66 calls (67 a day), hit rate 0.515, chance 0.074, naive rule 0.240, lift 6.96x
    - 7d: 371 calls (53 a day), hit rate 0.563, chance 0.079, naive rule 0.282, lift 7.13x
    - 30d: 1517 calls (51 a day), hit rate 0.585, chance 0.078, naive rule 0.273, lift 7.51x
  - next: threshold 0.301, hit rate recent 0.3401 / long run 0.3143
    - 6h: 9 calls (38 a day), hit rate 0.778, chance 0.083, lift 9.42x
    - 24h: 60 calls (61 a day), hit rate 0.317, chance 0.074, lift 4.28x
    - 7d: 433 calls (62 a day), hit rate 0.316, chance 0.079, lift 4.00x
    - 30d: 2039 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.451; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.620; 0.50: 25, 0.659; 0.55: 14, 0.707; 0.60: 4, 0.761; 0.65: 1, 0.941
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.325; 0.35: 13, 0.361; 0.40: 2, 0.385

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.747 | 16.76% | 0.917 | 0.600 | 0.251 | 0.508 | 0.186 |
| 6h | 8.500 | 10.77% | 0.908 | 0.517 | 0.251 | 0.473 | 0.307 |
| 24h | 15.508 | 5.25% | 0.899 | 0.507 | 0.251 | 0.477 | 0.687 |
| 7d | 14.870 | 4.19% | 0.901 | 0.500 | 0.251 | 0.490 | 0.669 |
| 30d | 14.017 | 4.01% | 0.900 | 0.500 | 0.251 | 0.495 | 0.675 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.106 | 6.763 | 7.222 | 6.734 | 6.952 | 7.244 | 6.662 | 6.678 | 6.721 | 6.747 |
| 6h | 9.526 | 8.535 | 8.836 | 8.532 | 8.624 | 8.761 | 8.481 | 8.440 | 8.488 | 8.500 |
| 24h | 16.368 | 15.710 | 15.632 | 15.539 | 15.786 | 15.636 | 15.505 | 15.498 | 15.485 | 15.508 |
| 7d | 15.521 | 15.034 | 14.962 | 14.886 | 15.131 | 15.067 | 14.877 | 14.846 | 14.842 | 14.870 |
| 30d | 14.604 | 14.142 | 14.102 | 14.043 | 14.272 | 14.202 | 14.016 | 13.990 | 13.991 | 14.017 |

## Next candle

- candle starting 2026-10-17 04:43 UTC, last close 2425.05
- P(up) 0.5015, return quantiles (bp): {'05': -4.753, '10': -3.615, '25': -1.785, '40': -0.61, '50': 0.006, '60': 0.694, '75': 1.815, '90': 3.733, '95': 4.999}
- changepoint probability 0.0289, regime age 380.6 min
- agent weights: empirical 0.003, ewma 0.094, garch 0.062, har 0.183, bocpd 0.055, hmm 0.070, online_qr 0.249, lgbm 0.285

## Learning log

- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.98, 7.01, 21.66], current probabilities: [0.952, 0.047, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 04:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.171, 'l_abs': 0.742, 'l_hi': 0.756, 'l_lo': 0.745, 'b05': 0.72, 'b25': 0.699, 'b75': 0.691, 'b95': 0.686}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.451, 2.133, 2.324, 2.656, 2.915, 3.284, 3.81, 3.814, 3.87, 4.067, 3.775, 4.098, 4.013, 4.162]}
- calibration offsets (in sigma): {'05': 0.081, '10': 0.062, '25': 0.045, '40': 0.028, '50': 0.01, '60': 0.002, '75': -0.025, '90': -0.032, '95': -0.071}
