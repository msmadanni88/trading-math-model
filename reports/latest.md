# ETH-USD 60s candle generator - report

- generated: 2026-10-17 22:41 UTC
- last closed candle: 2026-10-17 22:41 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.489 (90) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.568 (738) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.569 (130) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.547 (1337) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.493 (18718) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.576 (33) | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | 0.326 (43) | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | 0.604 (53) | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | 0.566 (113) | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 0.867 (60) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | 0.463 (134) | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 0.827 (52) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | 0.393 (112) | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | 0.755 (49) | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.499 (20761) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07037, 0.1095] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.07037, 'calls_per_day': 136.2, 'win_rate': 0.5734}, {'threshold': 0.1095, 'calls_per_day': 33.2, 'win_rate': 0.6453}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 20152, 'rate': 0.5292}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15334 | 0.336 | 0.522 (15085) | 0.594 (1356) | 0.780 (2496) |
| volatility: normal | 15333 | 0.362 | 0.514 (15270) | 0.608 (393) | 0.767 (2204) |
| volatility: wild | 15334 | 0.376 | 0.504 (15291) | 0.646 (161) | 0.770 (2108) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15260) | 0.607 (682) | 0.768 (2238) |
| session: Europe 08-13 | 9600 | 0.352 | 0.512 (9517) | 0.580 (486) | 0.777 (1499) |
| session: US 13-21 | 15360 | 0.367 | 0.509 (15253) | 0.586 (466) | 0.781 (2239) |
| session: late 21-24 | 5681 | 0.349 | 0.513 (5616) | 0.652 (276) | 0.755 (832) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.363 | 0.348 | 0.246 | 0.246 | 0.593 | 0.283 | 0.443 | 1.762 |
| 6h | 360 | 0.336 | 0.334 | 0.242 | 0.256 | 0.541 | 0.247 | 0.424 | 1.237 |
| 24h | 1440 | 0.348 | 0.331 | 0.250 | 0.274 | 0.544 | 0.265 | 0.432 | 1.246 |
| 7d | 10080 | 0.363 | 0.353 | 0.277 | 0.308 | 0.527 | 0.261 | 0.465 | 1.255 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.465 | 1.302 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.363 / 0.593 / 0.917; 2: 0.317 / 0.508 / 0.933; 3: 0.336 / 0.542 / 0.883; 4: 0.303 / 0.492 / 0.883; 5: 0.320 / 0.559 / 0.900; 6: 0.311 / 0.475 / 0.917; 7: 0.284 / 0.407 / 0.900; 8: 0.303 / 0.559 / 0.917; 9: 0.343 / 0.627 / 0.967; 10: 0.321 / 0.492 / 0.967; 11: 0.285 / 0.424 / 0.950; 12: 0.329 / 0.593 / 0.950; 13: 0.307 / 0.559 / 0.933; 14: 0.310 / 0.559 / 0.933; 15: 0.293 / 0.475 / 0.950
- 6h: 1: 0.336 / 0.541 / 0.861; 2: 0.322 / 0.484 / 0.878; 3: 0.328 / 0.527 / 0.867; 4: 0.309 / 0.467 / 0.847; 5: 0.329 / 0.538 / 0.853; 6: 0.316 / 0.501 / 0.858; 7: 0.323 / 0.536 / 0.872; 8: 0.311 / 0.499 / 0.872; 9: 0.316 / 0.484 / 0.892; 10: 0.318 / 0.504 / 0.886; 11: 0.304 / 0.467 / 0.886; 12: 0.310 / 0.484 / 0.894; 13: 0.303 / 0.507 / 0.883; 14: 0.307 / 0.490 / 0.889; 15: 0.305 / 0.470 / 0.881
- 24h: 1: 0.348 / 0.544 / 0.870; 2: 0.330 / 0.483 / 0.888; 3: 0.332 / 0.498 / 0.887; 4: 0.323 / 0.480 / 0.882; 5: 0.334 / 0.513 / 0.885; 6: 0.327 / 0.489 / 0.889; 7: 0.331 / 0.506 / 0.891; 8: 0.326 / 0.489 / 0.892; 9: 0.328 / 0.476 / 0.897; 10: 0.332 / 0.510 / 0.896; 11: 0.318 / 0.471 / 0.892; 12: 0.327 / 0.496 / 0.898; 13: 0.327 / 0.507 / 0.899; 14: 0.324 / 0.494 / 0.897; 15: 0.325 / 0.491 / 0.896
- 7d: 1: 0.363 / 0.527 / 0.902; 2: 0.351 / 0.499 / 0.899; 3: 0.354 / 0.508 / 0.899; 4: 0.349 / 0.496 / 0.898; 5: 0.352 / 0.505 / 0.898; 6: 0.351 / 0.502 / 0.899; 7: 0.351 / 0.503 / 0.900; 8: 0.349 / 0.499 / 0.899; 9: 0.350 / 0.501 / 0.900; 10: 0.351 / 0.508 / 0.900; 11: 0.345 / 0.492 / 0.900; 12: 0.349 / 0.504 / 0.901; 13: 0.349 / 0.503 / 0.901; 14: 0.346 / 0.498 / 0.900; 15: 0.349 / 0.504 / 0.900
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.509 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.094 (body 0.066, range 0.122); 'price stays where it was' would score 0.126; colour right 0.559; typical miss of the close 16.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.128 (body 0.096, range 0.160); 'price stays where it was' would score 0.136; colour right 0.510; typical miss of the close 6.5 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.135 (body 0.098, range 0.172); 'price stays where it was' would score 0.142; colour right 0.506; typical miss of the close 5.2 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.123 (body 0.083, range 0.163); 'price stays where it was' would score 0.130; colour right 0.497; typical miss of the close 8.5 bp; chain ended on the right side 0.507 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.518 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.0; 2: 0.196 / 4.4; 3: 0.165 / 6.0; 4: 0.133 / 6.6; 5: 0.121 / 7.3; 6: 0.110 / 7.8; 7: 0.102 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.5; 10: 0.085 / 9.3; 11: 0.080 / 10.0; 12: 0.076 / 10.3; 13: 0.064 / 10.7; 14: 0.066 / 10.8; 15: 0.058 / 11.0

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 109115, probability skill vs chance 0.2191, widened contest next: True
  - now: threshold 0.8384, hit rate recent 0.9151 / long run 0.9315
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.289, naive rule 0.464, lift 3.27x
    - 24h: 63 calls (63 a day), hit rate 0.873, chance 0.306, naive rule 0.509, lift 2.85x
    - 7d: 389 calls (56 a day), hit rate 0.931, chance 0.292, naive rule 0.489, lift 3.18x
    - 30d: 1719 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5676, hit rate recent 0.5307 / long run 0.5704
    - 6h: 19 calls (77 a day), hit rate 0.579, chance 0.289, lift 2.01x
    - 24h: 117 calls (117 a day), hit rate 0.564, chance 0.306, lift 1.84x
    - 7d: 728 calls (104 a day), hit rate 0.567, chance 0.292, lift 1.94x
    - 30d: 2590 calls (86 a day), hit rate 0.580, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.564; 0.45: 414, 0.634; 0.50: 361, 0.687; 0.55: 317, 0.729; 0.60: 270, 0.773; 0.65: 224, 0.801; 0.70: 179, 0.834; 0.75: 139, 0.870; 0.80: 95, 0.911; 0.85: 49, 0.949; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.525; 0.50: 204, 0.558; 0.55: 92, 0.577; 0.60: 14, 0.606; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 109113, probability skill vs chance 0.2141, widened contest next: False
  - now: threshold 0.6923, hit rate recent 0.8394 / long run 0.8268
    - 6h: 15 calls (61 a day), hit rate 0.867, chance 0.205, naive rule 0.449, lift 4.22x
    - 24h: 54 calls (54 a day), hit rate 0.833, chance 0.204, naive rule 0.442, lift 4.08x
    - 7d: 356 calls (51 a day), hit rate 0.820, chance 0.188, naive rule 0.406, lift 4.37x
    - 30d: 1616 calls (54 a day), hit rate 0.830, chance 0.188, naive rule 0.395, lift 4.42x
  - next: threshold 0.407, hit rate recent 0.4429 / long run 0.4648
    - 6h: 41 calls (167 a day), hit rate 0.463, chance 0.205, lift 2.26x
    - 24h: 137 calls (138 a day), hit rate 0.467, chance 0.204, lift 2.28x
    - 7d: 700 calls (100 a day), hit rate 0.469, chance 0.188, lift 2.50x
    - 30d: 2321 calls (77 a day), hit rate 0.478, chance 0.188, lift 2.54x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.421; 0.35: 352, 0.486; 0.40: 282, 0.559; 0.45: 231, 0.614; 0.50: 181, 0.666; 0.55: 138, 0.710; 0.60: 108, 0.750; 0.65: 81, 0.792; 0.70: 60, 0.823; 0.75: 33, 0.868; 0.80: 10, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 251, 0.425; 0.40: 160, 0.452; 0.45: 77, 0.466; 0.50: 18, 0.500; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 109110, probability skill vs chance 0.1981, widened contest next: True
  - now: threshold 0.5798, hit rate recent 0.724 / long run 0.701
    - 6h: 16 calls (66 a day), hit rate 0.812, chance 0.131, naive rule 0.383, lift 6.18x
    - 24h: 50 calls (50 a day), hit rate 0.760, chance 0.133, naive rule 0.371, lift 5.72x
    - 7d: 357 calls (51 a day), hit rate 0.689, chance 0.122, naive rule 0.335, lift 5.66x
    - 30d: 1584 calls (53 a day), hit rate 0.717, chance 0.123, naive rule 0.332, lift 5.84x
  - next: threshold 0.3412, hit rate recent 0.3456 / long run 0.379
    - 6h: 29 calls (119 a day), hit rate 0.310, chance 0.131, lift 2.36x
    - 24h: 115 calls (116 a day), hit rate 0.400, chance 0.133, lift 3.01x
    - 7d: 628 calls (90 a day), hit rate 0.374, chance 0.122, lift 3.07x
    - 30d: 2175 calls (73 a day), hit rate 0.403, chance 0.123, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.421; 0.35: 195, 0.494; 0.40: 149, 0.554; 0.45: 117, 0.597; 0.50: 90, 0.637; 0.55: 66, 0.687; 0.60: 44, 0.731; 0.65: 24, 0.786; 0.70: 9, 0.833; 0.75: 1, 0.760
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.355; 0.35: 106, 0.387; 0.40: 43, 0.420; 0.45: 9, 0.447; 0.50: 1, 0.406
- **K=13**: model 1792022400, labels learned 109105, probability skill vs chance 0.1816, widened contest next: False
  - now: threshold 0.4256, hit rate recent 0.5779 / long run 0.5752
    - 6h: 15 calls (63 a day), hit rate 0.600, chance 0.070, naive rule 0.264, lift 8.62x
    - 24h: 54 calls (55 a day), hit rate 0.611, chance 0.080, naive rule 0.321, lift 7.67x
    - 7d: 371 calls (53 a day), hit rate 0.563, chance 0.077, naive rule 0.278, lift 7.34x
    - 30d: 1528 calls (51 a day), hit rate 0.587, chance 0.078, naive rule 0.275, lift 7.50x
  - next: threshold 0.2887, hit rate recent 0.2946 / long run 0.3105
    - 6h: 12 calls (50 a day), hit rate 0.167, chance 0.070, lift 2.40x
    - 24h: 45 calls (45 a day), hit rate 0.356, chance 0.080, lift 4.46x
    - 7d: 417 calls (60 a day), hit rate 0.307, chance 0.077, lift 4.00x
    - 30d: 2036 calls (68 a day), hit rate 0.313, chance 0.078, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.513; 0.40: 62, 0.566; 0.45: 41, 0.621; 0.50: 26, 0.661; 0.55: 14, 0.705; 0.60: 5, 0.750; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.324; 0.35: 13, 0.357; 0.40: 2, 0.406

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.509 | 14.99% | 0.967 | 0.567 | 0.248 | 0.559 | 0.537 |
| 6h | 14.268 | 10.35% | 0.894 | 0.522 | 0.250 | 0.504 | 0.693 |
| 24h | 10.198 | 8.95% | 0.894 | 0.503 | 0.251 | 0.482 | 0.665 |
| 7d | 15.331 | 4.46% | 0.901 | 0.501 | 0.251 | 0.491 | 0.659 |
| 30d | 13.897 | 4.12% | 0.900 | 0.500 | 0.251 | 0.495 | 0.677 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 30.008 | 26.600 | 25.379 | 25.375 | 27.719 | 25.734 | 25.597 | 25.308 | 25.500 | 25.509 |
| 6h | 15.915 | 14.663 | 14.201 | 14.258 | 14.498 | 14.349 | 14.260 | 14.207 | 14.238 | 14.268 |
| 24h | 11.200 | 10.323 | 10.383 | 10.243 | 10.364 | 10.451 | 10.174 | 10.168 | 10.180 | 10.198 |
| 7d | 16.047 | 15.505 | 15.430 | 15.348 | 15.598 | 15.539 | 15.335 | 15.307 | 15.301 | 15.331 |
| 30d | 14.493 | 14.022 | 13.983 | 13.924 | 14.150 | 14.083 | 13.894 | 13.870 | 13.871 | 13.897 |

## Next candle

- candle starting 2026-10-17 22:41 UTC, last close 2390.56
- P(up) 0.5478, return quantiles (bp): {'05': -11.752, '10': -9.025, '25': -3.414, '40': -0.485, '50': 0.404, '60': 1.819, '75': 3.79, '90': 7.984, '95': 10.689}
- changepoint probability 0.207, regime age 29.9 min
- agent weights: empirical 0.003, ewma 0.016, garch 0.178, har 0.156, bocpd 0.033, hmm 0.066, online_qr 0.262, lgbm 0.285

## Learning log

- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.62, 6.89, 21.68], current probabilities: [0.604, 0.393, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 22:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.241, 'l_abs': 0.689, 'l_hi': 0.744, 'l_lo': 0.741, 'b05': 0.672, 'b25': 0.663, 'b75': 0.657, 'b95': 0.666}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.71, 2.184, 2.907, 3.067, 3.17, 3.297, 3.326, 3.198, 3.446, 3.622, 3.715, 3.875, 4.193, 4.437]}
- calibration offsets (in sigma): {'05': -0.02, '10': -0.07, '25': 0.03, '40': 0.08, '50': 0.03, '60': 0.03, '75': -0.02, '90': -0.0, '95': -0.05}
