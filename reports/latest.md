# ETH-USD 60s candle generator - report

- generated: 2026-10-17 20:41 UTC
- last closed candle: 2026-10-17 20:41 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.488 (82) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.572 (678) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.576 (118) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.551 (1218) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.492 (17052) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.607 (28) | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | 0.361 (36) | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | 0.625 (48) | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | 0.579 (107) | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 0.873 (55) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | 0.471 (123) | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 0.830 (47) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | 0.408 (103) | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | 0.756 (45) | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.499 (18916) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07037, 0.1095] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.07037, 'calls_per_day': 136.2, 'win_rate': 0.5734}, {'threshold': 0.1095, 'calls_per_day': 33.2, 'win_rate': 0.6453}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 20033, 'rate': 0.5294}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15295 | 0.337 | 0.522 (15046) | 0.596 (1346) | 0.779 (2486) |
| volatility: normal | 15292 | 0.362 | 0.515 (15229) | 0.606 (391) | 0.767 (2194) |
| volatility: wild | 15294 | 0.376 | 0.503 (15252) | 0.646 (161) | 0.772 (2109) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15260) | 0.607 (682) | 0.768 (2238) |
| session: Europe 08-13 | 9600 | 0.352 | 0.512 (9517) | 0.580 (486) | 0.777 (1499) |
| session: US 13-21 | 15341 | 0.367 | 0.509 (15234) | 0.586 (464) | 0.781 (2237) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5516) | 0.658 (266) | 0.757 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.318 | 0.322 | 0.152 | 0.152 | 0.509 | 0.245 | 0.392 | 1.243 |
| 6h | 360 | 0.339 | 0.330 | 0.225 | 0.276 | 0.559 | 0.248 | 0.430 | 1.453 |
| 24h | 1440 | 0.353 | 0.332 | 0.248 | 0.279 | 0.550 | 0.269 | 0.437 | 1.305 |
| 7d | 10080 | 0.363 | 0.354 | 0.277 | 0.308 | 0.528 | 0.261 | 0.465 | 1.255 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.309 | 0.515 | 0.252 | 0.465 | 1.302 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.318 / 0.509 / 0.833; 2: 0.330 / 0.404 / 0.933; 3: 0.346 / 0.632 / 0.917; 4: 0.309 / 0.456 / 0.917; 5: 0.357 / 0.632 / 0.933; 6: 0.343 / 0.526 / 0.933; 7: 0.339 / 0.579 / 0.950; 8: 0.301 / 0.421 / 0.917; 9: 0.289 / 0.421 / 0.933; 10: 0.348 / 0.544 / 0.900; 11: 0.324 / 0.509 / 0.917; 12: 0.315 / 0.439 / 0.900; 13: 0.291 / 0.386 / 0.883; 14: 0.313 / 0.491 / 0.933; 15: 0.319 / 0.474 / 0.917
- 6h: 1: 0.339 / 0.559 / 0.864; 2: 0.318 / 0.441 / 0.900; 3: 0.334 / 0.530 / 0.911; 4: 0.321 / 0.458 / 0.914; 5: 0.337 / 0.533 / 0.917; 6: 0.331 / 0.513 / 0.900; 7: 0.343 / 0.567 / 0.911; 8: 0.315 / 0.450 / 0.914; 9: 0.321 / 0.470 / 0.914; 10: 0.335 / 0.527 / 0.900; 11: 0.329 / 0.513 / 0.908; 12: 0.319 / 0.479 / 0.908; 13: 0.309 / 0.470 / 0.900; 14: 0.322 / 0.496 / 0.914; 15: 0.322 / 0.473 / 0.906
- 24h: 1: 0.353 / 0.550 / 0.876; 2: 0.335 / 0.482 / 0.897; 3: 0.336 / 0.499 / 0.902; 4: 0.329 / 0.482 / 0.904; 5: 0.340 / 0.515 / 0.906; 6: 0.334 / 0.493 / 0.910; 7: 0.338 / 0.511 / 0.912; 8: 0.331 / 0.482 / 0.911; 9: 0.334 / 0.480 / 0.913; 10: 0.340 / 0.519 / 0.910; 11: 0.325 / 0.484 / 0.909; 12: 0.334 / 0.494 / 0.912; 13: 0.332 / 0.503 / 0.915; 14: 0.330 / 0.493 / 0.915; 15: 0.331 / 0.494 / 0.913
- 7d: 1: 0.363 / 0.528 / 0.902; 2: 0.352 / 0.499 / 0.900; 3: 0.354 / 0.509 / 0.901; 4: 0.350 / 0.496 / 0.901; 5: 0.352 / 0.505 / 0.901; 6: 0.351 / 0.502 / 0.902; 7: 0.352 / 0.505 / 0.903; 8: 0.349 / 0.499 / 0.902; 9: 0.350 / 0.501 / 0.902; 10: 0.352 / 0.507 / 0.902; 11: 0.346 / 0.493 / 0.903; 12: 0.349 / 0.503 / 0.903; 13: 0.349 / 0.502 / 0.903; 14: 0.346 / 0.498 / 0.902; 15: 0.349 / 0.505 / 0.902
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.504 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.347 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.166 (body 0.141, range 0.192); 'price stays where it was' would score 0.152; colour right 0.491; typical miss of the close 3.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.091, range 0.158); 'price stays where it was' would score 0.120; colour right 0.470; typical miss of the close 7.0 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.142 (body 0.102, range 0.181); 'price stays where it was' would score 0.148; colour right 0.504; typical miss of the close 5.0 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.124 (body 0.084, range 0.163); 'price stays where it was' would score 0.131; colour right 0.498; typical miss of the close 8.4 bp; chain ended on the right side 0.510 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 7.8 bp; chain ended on the right side 0.518 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 4.0; 2: 0.196 / 4.4; 3: 0.165 / 6.0; 4: 0.134 / 6.6; 5: 0.121 / 7.3; 6: 0.110 / 7.8; 7: 0.102 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.5; 10: 0.085 / 9.3; 11: 0.080 / 10.0; 12: 0.076 / 10.3; 13: 0.064 / 10.7; 14: 0.066 / 10.8; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 108995, probability skill vs chance 0.2181, widened contest next: False
  - now: threshold 0.8384, hit rate recent 0.9255 / long run 0.9326
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.304, naive rule 0.493, lift 3.29x
    - 24h: 62 calls (62 a day), hit rate 0.887, chance 0.312, naive rule 0.521, lift 2.84x
    - 7d: 390 calls (56 a day), hit rate 0.931, chance 0.294, naive rule 0.492, lift 3.17x
    - 30d: 1722 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.483, lift 3.22x
  - next: threshold 0.5676, hit rate recent 0.5511 / long run 0.5728
    - 6h: 20 calls (81 a day), hit rate 0.650, chance 0.304, lift 2.14x
    - 24h: 113 calls (113 a day), hit rate 0.584, chance 0.312, lift 1.87x
    - 7d: 733 calls (105 a day), hit rate 0.572, chance 0.294, lift 1.95x
    - 30d: 2591 calls (86 a day), hit rate 0.580, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 484, 0.564; 0.45: 414, 0.634; 0.50: 362, 0.687; 0.55: 317, 0.729; 0.60: 270, 0.773; 0.65: 225, 0.801; 0.70: 180, 0.834; 0.75: 139, 0.870; 0.80: 95, 0.911; 0.85: 49, 0.950; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 408, 0.490; 0.45: 313, 0.525; 0.50: 204, 0.559; 0.55: 92, 0.578; 0.60: 14, 0.607; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 108993, probability skill vs chance 0.2106, widened contest next: False
  - now: threshold 0.6923, hit rate recent 0.8431 / long run 0.827
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.214, naive rule 0.476, lift 4.36x
    - 24h: 54 calls (54 a day), hit rate 0.852, chance 0.207, naive rule 0.452, lift 4.12x
    - 7d: 355 calls (51 a day), hit rate 0.823, chance 0.188, naive rule 0.407, lift 4.38x
    - 30d: 1618 calls (54 a day), hit rate 0.831, chance 0.188, naive rule 0.395, lift 4.42x
  - next: threshold 0.407, hit rate recent 0.4558 / long run 0.4667
    - 6h: 41 calls (167 a day), hit rate 0.512, chance 0.214, lift 2.39x
    - 24h: 130 calls (131 a day), hit rate 0.485, chance 0.207, lift 2.35x
    - 7d: 694 calls (99 a day), hit rate 0.473, chance 0.188, lift 2.52x
    - 30d: 2319 calls (77 a day), hit rate 0.479, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 423, 0.421; 0.35: 352, 0.486; 0.40: 283, 0.558; 0.45: 231, 0.614; 0.50: 182, 0.666; 0.55: 138, 0.710; 0.60: 108, 0.750; 0.65: 82, 0.793; 0.70: 60, 0.823; 0.75: 33, 0.868; 0.80: 10, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.390; 0.35: 251, 0.425; 0.40: 161, 0.452; 0.45: 77, 0.467; 0.50: 18, 0.500; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 108990, probability skill vs chance 0.1928, widened contest next: False
  - now: threshold 0.5798, hit rate recent 0.7224 / long run 0.7007
    - 6h: 17 calls (70 a day), hit rate 0.765, chance 0.121, naive rule 0.347, lift 6.30x
    - 24h: 51 calls (51 a day), hit rate 0.765, chance 0.128, naive rule 0.356, lift 5.96x
    - 7d: 358 calls (51 a day), hit rate 0.690, chance 0.122, naive rule 0.334, lift 5.67x
    - 30d: 1586 calls (53 a day), hit rate 0.717, chance 0.123, naive rule 0.332, lift 5.84x
  - next: threshold 0.3412, hit rate recent 0.3636 / long run 0.3813
    - 6h: 30 calls (123 a day), hit rate 0.367, chance 0.121, lift 3.02x
    - 24h: 112 calls (113 a day), hit rate 0.393, chance 0.128, lift 3.06x
    - 7d: 623 calls (89 a day), hit rate 0.377, chance 0.122, lift 3.10x
    - 30d: 2174 calls (72 a day), hit rate 0.404, chance 0.123, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.420; 0.35: 196, 0.493; 0.40: 149, 0.553; 0.45: 118, 0.596; 0.50: 90, 0.636; 0.55: 66, 0.687; 0.60: 45, 0.730; 0.65: 24, 0.785; 0.70: 9, 0.832; 0.75: 1, 0.750
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 179, 0.355; 0.35: 106, 0.388; 0.40: 43, 0.421; 0.45: 9, 0.449; 0.50: 1, 0.406
- **K=13**: model 1792022400, labels learned 108985, probability skill vs chance 0.1842, widened contest next: False
  - now: threshold 0.4256, hit rate recent 0.5932 / long run 0.5766
    - 6h: 16 calls (67 a day), hit rate 0.625, chance 0.080, naive rule 0.318, lift 7.84x
    - 24h: 53 calls (54 a day), hit rate 0.642, chance 0.082, naive rule 0.324, lift 7.81x
    - 7d: 369 calls (53 a day), hit rate 0.566, chance 0.078, naive rule 0.281, lift 7.30x
    - 30d: 1529 calls (51 a day), hit rate 0.588, chance 0.078, naive rule 0.275, lift 7.51x
  - next: threshold 0.2887, hit rate recent 0.3127 / long run 0.3124
    - 6h: 9 calls (38 a day), hit rate 0.333, chance 0.080, lift 4.18x
    - 24h: 39 calls (39 a day), hit rate 0.385, chance 0.082, lift 4.68x
    - 7d: 413 calls (59 a day), hit rate 0.310, chance 0.078, lift 4.00x
    - 30d: 2032 calls (68 a day), hit rate 0.313, chance 0.078, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.453; 0.35: 85, 0.514; 0.40: 62, 0.567; 0.45: 42, 0.622; 0.50: 26, 0.662; 0.55: 14, 0.705; 0.60: 5, 0.748; 0.65: 1, 0.818
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.324; 0.35: 13, 0.357; 0.40: 2, 0.397

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.264 | 0.79% | 0.883 | 0.417 | 0.251 | 0.526 | 0.263 |
| 6h | 9.998 | 1.43% | 0.889 | 0.536 | 0.250 | 0.496 | 0.581 |
| 24h | 8.894 | 6.88% | 0.897 | 0.508 | 0.251 | 0.477 | 0.513 |
| 7d | 15.119 | 4.21% | 0.901 | 0.501 | 0.251 | 0.492 | 0.660 |
| 30d | 13.855 | 4.05% | 0.900 | 0.500 | 0.251 | 0.495 | 0.677 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.322 | 7.290 | 7.300 | 7.234 | 7.347 | 7.498 | 7.265 | 7.254 | 7.232 | 7.264 |
| 6h | 10.143 | 10.032 | 10.065 | 9.988 | 10.147 | 10.231 | 9.956 | 10.016 | 9.976 | 9.998 |
| 24h | 9.551 | 8.924 | 9.116 | 8.936 | 9.035 | 9.175 | 8.862 | 8.863 | 8.874 | 8.894 |
| 7d | 15.783 | 15.282 | 15.223 | 15.136 | 15.383 | 15.332 | 15.121 | 15.097 | 15.090 | 15.119 |
| 30d | 14.440 | 13.977 | 13.942 | 13.882 | 14.107 | 14.042 | 13.852 | 13.828 | 13.829 | 13.855 |

## Next candle

- candle starting 2026-10-17 20:41 UTC, last close 2416.62
- P(up) 0.5143, return quantiles (bp): {'05': -4.235, '10': -3.236, '25': -1.427, '40': -0.359, '50': 0.058, '60': 0.637, '75': 1.461, '90': 3.196, '95': 4.128}
- changepoint probability 0.0292, regime age 141.4 min
- agent weights: empirical 0.008, ewma 0.145, garch 0.065, har 0.175, bocpd 0.053, hmm 0.019, online_qr 0.305, lgbm 0.229

## Learning log

- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- HMM volatility states (sd, bp per minute): [3.62, 6.89, 21.68], current probabilities: [0.979, 0.02, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 20:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.223, 'l_abs': 0.698, 'l_hi': 0.744, 'l_lo': 0.748, 'b05': 0.674, 'b25': 0.657, 'b75': 0.632, 'b95': 0.656}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.4, 1.618, 1.763, 1.936, 2.125, 2.255, 2.415, 2.567, 2.822, 2.793, 3.103, 3.048, 3.233, 3.421]}
- calibration offsets (in sigma): {'05': 0.01, '10': -0.02, '25': 0.03, '40': 0.06, '50': 0.02, '60': 0.02, '75': -0.03, '90': -0.0, '95': -0.04}
