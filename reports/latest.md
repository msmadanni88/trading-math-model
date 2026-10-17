# ETH-USD 60s candle generator - report

- generated: 2026-10-17 08:51 UTC
- last closed candle: 2026-10-17 08:51 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.429 (35) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.572 (292) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (48) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.545 (523) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.496 (7322) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.500 (8) | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | 0.727 (11) | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | 0.625 (16) | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | 0.691 (55) | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 0.800 (25) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | 0.548 (42) | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 0.846 (13) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | 0.528 (36) | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | 0.833 (12) | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.503 (8090) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07276, 0.1145] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5254, 'levels': [{'threshold': 0.07276, 'calls_per_day': 139.6, 'win_rate': 0.5755}, {'threshold': 0.1145, 'calls_per_day': 34.6, 'win_rate': 0.649}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 19338, 'rate': 0.5284}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15057 | 0.337 | 0.521 (14819) | 0.601 (1291) | 0.777 (2429) |
| volatility: normal | 15057 | 0.363 | 0.514 (14998) | 0.596 (376) | 0.769 (2155) |
| volatility: wild | 15057 | 0.376 | 0.503 (15015) | 0.646 (161) | 0.772 (2076) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15260) | 0.607 (682) | 0.768 (2238) |
| session: Europe 08-13 | 9351 | 0.352 | 0.511 (9272) | 0.585 (453) | 0.779 (1450) |
| session: US 13-21 | 14880 | 0.367 | 0.507 (14784) | 0.586 (427) | 0.780 (2157) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5516) | 0.658 (266) | 0.757 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.300 | 0.275 | 0.203 | 0.203 | 0.526 | 0.257 | 0.343 | 1.619 |
| 6h | 360 | 0.343 | 0.325 | 0.256 | 0.283 | 0.531 | 0.257 | 0.429 | 1.311 |
| 24h | 1440 | 0.370 | 0.352 | 0.285 | 0.310 | 0.528 | 0.268 | 0.473 | 1.226 |
| 7d | 10080 | 0.360 | 0.351 | 0.277 | 0.307 | 0.525 | 0.259 | 0.461 | 1.280 |
| 30d | 43200 | 0.358 | 0.355 | 0.280 | 0.309 | 0.513 | 0.251 | 0.466 | 1.303 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.300 / 0.526 / 0.867; 2: 0.271 / 0.509 / 0.917; 3: 0.290 / 0.526 / 0.950; 4: 0.270 / 0.561 / 1.000; 5: 0.267 / 0.456 / 0.983; 6: 0.259 / 0.368 / 1.000; 7: 0.280 / 0.526 / 1.000; 8: 0.261 / 0.404 / 1.000; 9: 0.267 / 0.421 / 1.000; 10: 0.274 / 0.421 / 1.000; 11: 0.254 / 0.439 / 1.000; 12: 0.284 / 0.509 / 1.000; 13: 0.279 / 0.526 / 1.000; 14: 0.227 / 0.386 / 1.000; 15: 0.278 / 0.491 / 1.000
- 6h: 1: 0.343 / 0.531 / 0.883; 2: 0.325 / 0.486 / 0.886; 3: 0.328 / 0.500 / 0.919; 4: 0.304 / 0.444 / 0.922; 5: 0.329 / 0.497 / 0.933; 6: 0.321 / 0.463 / 0.925; 7: 0.329 / 0.494 / 0.942; 8: 0.332 / 0.492 / 0.936; 9: 0.326 / 0.475 / 0.931; 10: 0.335 / 0.503 / 0.914; 11: 0.316 / 0.466 / 0.914; 12: 0.336 / 0.514 / 0.931; 13: 0.333 / 0.525 / 0.919; 14: 0.327 / 0.500 / 0.936; 15: 0.325 / 0.503 / 0.936
- 24h: 1: 0.370 / 0.528 / 0.896; 2: 0.358 / 0.500 / 0.899; 3: 0.355 / 0.484 / 0.900; 4: 0.351 / 0.495 / 0.901; 5: 0.357 / 0.499 / 0.900; 6: 0.353 / 0.496 / 0.900; 7: 0.353 / 0.494 / 0.905; 8: 0.357 / 0.506 / 0.900; 9: 0.356 / 0.504 / 0.897; 10: 0.358 / 0.505 / 0.898; 11: 0.345 / 0.477 / 0.899; 12: 0.360 / 0.516 / 0.906; 13: 0.359 / 0.507 / 0.902; 14: 0.351 / 0.491 / 0.906; 15: 0.353 / 0.506 / 0.905
- 7d: 1: 0.360 / 0.525 / 0.903; 2: 0.349 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.347 / 0.495 / 0.900; 5: 0.351 / 0.507 / 0.900; 6: 0.349 / 0.501 / 0.899; 7: 0.348 / 0.502 / 0.899; 8: 0.347 / 0.499 / 0.899; 9: 0.348 / 0.504 / 0.899; 10: 0.350 / 0.508 / 0.898; 11: 0.344 / 0.492 / 0.898; 12: 0.348 / 0.505 / 0.899; 13: 0.347 / 0.505 / 0.898; 14: 0.344 / 0.498 / 0.899; 15: 0.348 / 0.506 / 0.899
- 30d: 1: 0.358 / 0.513 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.189 (body 0.162, range 0.217); 'price stays where it was' would score 0.155; colour right 0.421; typical miss of the close 2.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.139 (body 0.105, range 0.173); 'price stays where it was' would score 0.152; colour right 0.486; typical miss of the close 3.8 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.126 (body 0.084, range 0.168); 'price stays where it was' would score 0.144; colour right 0.492; typical miss of the close 7.4 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.121 (body 0.082, range 0.160); 'price stays where it was' would score 0.130; colour right 0.495; typical miss of the close 8.1 bp; chain ended on the right side 0.513 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.160); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 7.9 bp; chain ended on the right side 0.517 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.0; 2: 0.196 / 4.5; 3: 0.164 / 6.0; 4: 0.132 / 6.7; 5: 0.121 / 7.4; 6: 0.109 / 7.9; 7: 0.102 / 8.2; 8: 0.096 / 8.6; 9: 0.087 / 8.6; 10: 0.085 / 9.4; 11: 0.080 / 10.1; 12: 0.076 / 10.4; 13: 0.064 / 10.7; 14: 0.066 / 11.0; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 108285, probability skill vs chance 0.22, widened contest next: False
  - now: threshold 0.8393, hit rate recent 0.9145 / long run 0.9325
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.327, naive rule 0.553, lift 2.86x
    - 24h: 52 calls (52 a day), hit rate 0.904, chance 0.285, naive rule 0.468, lift 3.17x
    - 7d: 391 calls (56 a day), hit rate 0.934, chance 0.294, naive rule 0.493, lift 3.17x
    - 30d: 1725 calls (58 a day), hit rate 0.937, chance 0.291, naive rule 0.482, lift 3.22x
  - next: threshold 0.5498, hit rate recent 0.6394 / long run 0.5827
    - 6h: 34 calls (138 a day), hit rate 0.706, chance 0.327, lift 2.16x
    - 24h: 127 calls (127 a day), hit rate 0.583, chance 0.285, lift 2.04x
    - 7d: 751 calls (107 a day), hit rate 0.589, chance 0.294, lift 2.00x
    - 30d: 2589 calls (86 a day), hit rate 0.582, chance 0.291, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 485, 0.563; 0.45: 415, 0.632; 0.50: 362, 0.685; 0.55: 317, 0.728; 0.60: 270, 0.772; 0.65: 224, 0.800; 0.70: 180, 0.833; 0.75: 139, 0.870; 0.80: 95, 0.910; 0.85: 49, 0.950; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 409, 0.489; 0.45: 314, 0.524; 0.50: 204, 0.559; 0.55: 92, 0.580; 0.60: 14, 0.601; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 108283, probability skill vs chance 0.2124, widened contest next: False
  - now: threshold 0.6941, hit rate recent 0.8521 / long run 0.8272
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.208, naive rule 0.459, lift 4.27x
    - 24h: 45 calls (45 a day), hit rate 0.867, chance 0.189, naive rule 0.397, lift 4.59x
    - 7d: 352 calls (50 a day), hit rate 0.830, chance 0.188, naive rule 0.408, lift 4.41x
    - 30d: 1603 calls (53 a day), hit rate 0.831, chance 0.187, naive rule 0.394, lift 4.43x
  - next: threshold 0.4184, hit rate recent 0.4842 / long run 0.4715
    - 6h: 29 calls (118 a day), hit rate 0.517, chance 0.208, lift 2.48x
    - 24h: 114 calls (115 a day), hit rate 0.456, chance 0.189, lift 2.42x
    - 7d: 656 calls (94 a day), hit rate 0.480, chance 0.188, lift 2.55x
    - 30d: 2280 calls (76 a day), hit rate 0.481, chance 0.187, lift 2.56x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.420; 0.35: 353, 0.484; 0.40: 284, 0.556; 0.45: 232, 0.612; 0.50: 182, 0.664; 0.55: 138, 0.708; 0.60: 108, 0.748; 0.65: 81, 0.792; 0.70: 60, 0.824; 0.75: 33, 0.868; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 251, 0.425; 0.40: 161, 0.453; 0.45: 77, 0.469; 0.50: 18, 0.508; 0.55: 2, 0.560
- **K=8**: model 1791936000, labels learned 108280, probability skill vs chance 0.1929, widened contest next: False
  - now: threshold 0.5819, hit rate recent 0.7103 / long run 0.6991
    - 6h: 7 calls (29 a day), hit rate 1.000, chance 0.137, naive rule 0.402, lift 7.29x
    - 24h: 44 calls (44 a day), hit rate 0.750, chance 0.116, naive rule 0.302, lift 6.44x
    - 7d: 354 calls (51 a day), hit rate 0.695, chance 0.122, naive rule 0.339, lift 5.67x
    - 30d: 1575 calls (53 a day), hit rate 0.716, chance 0.123, naive rule 0.331, lift 5.84x
  - next: threshold 0.3412, hit rate recent 0.3963 / long run 0.3858
    - 6h: 24 calls (99 a day), hit rate 0.542, chance 0.137, lift 3.95x
    - 24h: 111 calls (112 a day), hit rate 0.360, chance 0.116, lift 3.09x
    - 7d: 594 calls (85 a day), hit rate 0.380, chance 0.122, lift 3.11x
    - 30d: 2155 calls (72 a day), hit rate 0.406, chance 0.123, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.419; 0.35: 196, 0.491; 0.40: 149, 0.551; 0.45: 118, 0.595; 0.50: 90, 0.636; 0.55: 65, 0.686; 0.60: 44, 0.728; 0.65: 24, 0.783; 0.70: 9, 0.839; 0.75: 1, 0.792
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.355; 0.35: 106, 0.389; 0.40: 43, 0.421; 0.45: 9, 0.447; 0.50: 1, 0.382
- **K=13**: model 1792022400, labels learned 108275, probability skill vs chance 0.18, widened contest next: False
  - now: threshold 0.4366, hit rate recent 0.5675 / long run 0.574
    - 6h: 10 calls (42 a day), hit rate 0.700, chance 0.078, naive rule 0.382, lift 8.94x
    - 24h: 59 calls (60 a day), hit rate 0.576, chance 0.075, naive rule 0.253, lift 7.67x
    - 7d: 367 calls (53 a day), hit rate 0.559, chance 0.078, naive rule 0.282, lift 7.13x
    - 30d: 1515 calls (51 a day), hit rate 0.586, chance 0.078, naive rule 0.273, lift 7.52x
  - next: threshold 0.3009, hit rate recent 0.3669 / long run 0.3172
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.078, lift 7.99x
    - 24h: 55 calls (56 a day), hit rate 0.364, chance 0.075, lift 4.84x
    - 7d: 424 calls (61 a day), hit rate 0.318, chance 0.078, lift 4.06x
    - 30d: 2038 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.451; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.620; 0.50: 25, 0.661; 0.55: 14, 0.708; 0.60: 4, 0.763; 0.65: 1, 0.941
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.326; 0.35: 13, 0.359; 0.40: 2, 0.385

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.120 | 25.22% | 0.967 | 0.600 | 0.251 | 0.439 | 0.367 |
| 6h | 7.247 | 13.48% | 0.908 | 0.519 | 0.250 | 0.480 | 0.389 |
| 24h | 14.420 | 6.32% | 0.901 | 0.503 | 0.251 | 0.474 | 0.727 |
| 7d | 14.906 | 4.26% | 0.901 | 0.501 | 0.251 | 0.489 | 0.668 |
| 30d | 13.986 | 4.04% | 0.900 | 0.500 | 0.251 | 0.495 | 0.676 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.847 | 5.193 | 5.837 | 5.116 | 5.444 | 6.189 | 5.094 | 5.105 | 5.133 | 5.120 |
| 6h | 8.375 | 7.279 | 7.653 | 7.302 | 7.378 | 7.710 | 7.229 | 7.202 | 7.236 | 7.247 |
| 24h | 15.392 | 14.601 | 14.580 | 14.466 | 14.674 | 14.598 | 14.427 | 14.421 | 14.400 | 14.420 |
| 7d | 15.569 | 15.069 | 15.005 | 14.923 | 15.166 | 15.110 | 14.913 | 14.881 | 14.877 | 14.906 |
| 30d | 14.575 | 14.110 | 14.073 | 14.011 | 14.239 | 14.173 | 13.984 | 13.959 | 13.959 | 13.986 |

## Next candle

- candle starting 2026-10-17 08:51 UTC, last close 2429.93
- P(up) 0.5007, return quantiles (bp): {'05': -3.355, '10': -2.462, '25': -1.102, '40': -0.396, '50': 0.0, '60': 0.444, '75': 1.27, '90': 2.74, '95': 3.663}
- changepoint probability 0.0287, regime age 186.0 min
- agent weights: empirical 0.003, ewma 0.132, garch 0.026, har 0.175, bocpd 0.063, hmm 0.021, online_qr 0.263, lgbm 0.318

## Learning log

- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.98, 7.01, 21.66], current probabilities: [0.962, 0.037, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 09:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.205, 'l_abs': 0.727, 'l_hi': 0.754, 'l_lo': 0.747, 'b05': 0.691, 'b25': 0.681, 'b75': 0.681, 'b95': 0.655}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.547, 1.684, 1.763, 1.975, 2.257, 2.3, 2.564, 2.725, 2.996, 3.149, 2.865, 3.236, 2.868, 2.974]}
- calibration offsets (in sigma): {'05': 0.105, '10': 0.09, '25': 0.055, '40': 0.0, '50': -0.01, '60': -0.04, '75': -0.045, '90': -0.04, '95': -0.065}
