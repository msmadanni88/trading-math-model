# ETH-USD 60s candle generator - report

- generated: 2026-10-17 00:20 UTC
- last closed candle: 2026-10-17 00:20 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.520 (671) [0.489, 0.555] | 0.517 (2875) [0.499, 0.536] | 0.511 (4314) [0.495, 0.526] | 0.510 (1342) [0.480, 0.539] | 0.000 (1) | 0.500 | flat +0.021 (noise 0.035) |
| colour_clear | 0.531 (785) | 0.538 (5513) [0.532, 0.545] | 0.517 (23374) [0.510, 0.526] | 0.510 (35057) [0.504, 0.516] | 0.542 (10819) [0.537, 0.547] | 0.500 (12) | 0.500 | flat -0.008 (noise 0.010) |
| colour_confident | 0.625 (88) | 0.587 (831) [0.572, 0.607] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 0.604 (1780) [0.582, 0.628] | 1.000 (2) | 0.500 | flat -0.031 (noise 0.027) |
| colour_next | 0.521 (1433) | 0.525 (9978) [0.520, 0.531] | 0.513 (42873) [0.507, 0.519] | 0.509 (64302) [0.504, 0.513] | 0.527 (19953) [0.522, 0.533] | 0.650 (20) | 0.500 | flat -0.004 (noise 0.007) |
| colour_path | 0.496 (20062) | 0.502 (139692) [0.500, 0.505] | 0.501 (600222) [0.500, 0.503] | 0.501 (900228) [0.500, 0.502] | 0.501 (279342) [0.498, 0.503] | 0.493 (280) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.600 (20) | 0.652 (221) [0.618, 0.688] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | 0.656 (465) [0.619, 0.698] | - | 0.500 | flat -0.008 (noise 0.050) |
| reversal_k13_next | 0.311 (61) | 0.313 (444) [0.287, 0.340] | 0.313 (2038) [0.299, 0.328] | 0.306 (3090) [0.293, 0.319] | 0.319 (985) [0.304, 0.333] | - | 0.077 | flat -0.010 (noise 0.030) |
| reversal_k13_now | 0.542 (72) | 0.558 (373) [0.532, 0.587] | 0.585 (1512) [0.565, 0.606] | 0.580 (2231) [0.564, 0.596] | 0.577 (759) [0.552, 0.607] | - | 0.077 | flat -0.038 (noise 0.036) |
| reversal_k3_next | 0.561 (130) | 0.577 (737) [0.558, 0.598] | 0.579 (2556) [0.565, 0.593] | 0.583 (3749) [0.571, 0.595] | 0.574 (1309) [0.557, 0.592] | - | 0.292 | flat +0.007 (noise 0.028) |
| reversal_k3_now | 0.983 (58) | 0.939 (393) [0.920, 0.959] | 0.939 (1715) [0.931, 0.947] | 0.939 (2564) [0.932, 0.946] | 0.933 (801) [0.922, 0.944] | 1.000 (2) | 0.293 | flat +0.012 (noise 0.018) |
| reversal_k5_next | 0.412 (114) | 0.474 (639) [0.446, 0.502] | 0.480 (2259) [0.463, 0.498] | 0.481 (3225) [0.467, 0.496] | 0.461 (1235) [0.440, 0.486] | - | 0.187 | flat +0.028 (noise 0.028) |
| reversal_k5_now | 0.875 (64) | 0.826 (362) [0.794, 0.855] | 0.831 (1599) [0.816, 0.847] | 0.833 (2358) [0.819, 0.845] | 0.822 (747) [0.800, 0.844] | 1.000 (1) | 0.187 | flat +0.008 (noise 0.028) |
| reversal_k8_next | 0.294 (119) | 0.379 (583) [0.344, 0.414] | 0.403 (2141) [0.384, 0.423] | 0.392 (3310) [0.378, 0.406] | 0.384 (1204) [0.362, 0.406] | - | 0.121 | flat -0.009 (noise 0.028) |
| reversal_k8_now | 0.672 (58) | 0.690 (364) [0.664, 0.719] | 0.713 (1577) [0.692, 0.734] | 0.707 (2358) [0.691, 0.724] | 0.694 (771) [0.667, 0.721] | - | 0.122 | flat -0.008 (noise 0.033) |
| overall | 0.500 (22267) | 0.506 (154236) [0.503, 0.508] | 0.504 (661367) [0.503, 0.505] | 0.503 (991729) [0.502, 0.504] | 0.504 (308448) [0.502, 0.506] | 0.507 (304) | - | flat +0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07348, 0.1157] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5252, 'levels': [{'threshold': 0.07348, 'calls_per_day': 141.7, 'win_rate': 0.5838}, {'threshold': 0.1157, 'calls_per_day': 35.6, 'win_rate': 0.6627}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 18835, 'rate': 0.5281}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14887 | 0.336 | 0.520 (14654) | 0.604 (1251) | 0.779 (2421) |
| volatility: normal | 14886 | 0.363 | 0.515 (14828) | 0.589 (372) | 0.770 (2130) |
| volatility: wild | 14887 | 0.376 | 0.502 (14847) | 0.648 (159) | 0.769 (2046) |
| session: Asia 00-08 | 14900 | 0.356 | 0.518 (14805) | 0.606 (639) | 0.769 (2183) |
| session: Europe 08-13 | 9300 | 0.352 | 0.511 (9224) | 0.589 (450) | 0.779 (1442) |
| session: US 13-21 | 14880 | 0.367 | 0.507 (14784) | 0.586 (427) | 0.780 (2157) |
| session: late 21-24 | 5580 | 0.350 | 0.512 (5516) | 0.658 (266) | 0.757 (815) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.338 | 0.309 | 0.218 | 0.218 | 0.500 | 0.253 | 0.423 | 1.820 |
| 6h | 360 | 0.380 | 0.351 | 0.263 | 0.308 | 0.552 | 0.284 | 0.476 | 1.540 |
| 24h | 1440 | 0.376 | 0.362 | 0.292 | 0.322 | 0.523 | 0.263 | 0.489 | 1.243 |
| 7d | 10080 | 0.359 | 0.350 | 0.275 | 0.305 | 0.525 | 0.259 | 0.459 | 1.304 |
| 30d | 43200 | 0.359 | 0.355 | 0.280 | 0.310 | 0.513 | 0.251 | 0.466 | 1.304 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.338 / 0.500 / 0.917; 2: 0.317 / 0.483 / 0.833; 3: 0.294 / 0.417 / 0.933; 4: 0.319 / 0.517 / 0.967; 5: 0.338 / 0.600 / 0.967; 6: 0.298 / 0.467 / 0.983; 7: 0.336 / 0.583 / 1.000; 8: 0.301 / 0.450 / 1.000; 9: 0.327 / 0.500 / 1.000; 10: 0.317 / 0.483 / 1.000; 11: 0.286 / 0.433 / 1.000; 12: 0.345 / 0.517 / 1.000; 13: 0.305 / 0.467 / 1.000; 14: 0.335 / 0.500 / 1.000; 15: 0.329 / 0.550 / 1.000
- 6h: 1: 0.380 / 0.552 / 0.922; 2: 0.360 / 0.496 / 0.917; 3: 0.348 / 0.465 / 0.939; 4: 0.351 / 0.485 / 0.936; 5: 0.354 / 0.513 / 0.936; 6: 0.346 / 0.479 / 0.956; 7: 0.350 / 0.499 / 0.956; 8: 0.346 / 0.470 / 0.975; 9: 0.358 / 0.518 / 0.981; 10: 0.369 / 0.546 / 0.986; 11: 0.337 / 0.485 / 0.989; 12: 0.368 / 0.524 / 0.989; 13: 0.356 / 0.521 / 0.986; 14: 0.352 / 0.490 / 0.986; 15: 0.350 / 0.499 / 0.986
- 24h: 1: 0.376 / 0.523 / 0.903; 2: 0.365 / 0.500 / 0.901; 3: 0.362 / 0.486 / 0.901; 4: 0.366 / 0.517 / 0.904; 5: 0.363 / 0.498 / 0.903; 6: 0.358 / 0.487 / 0.906; 7: 0.360 / 0.497 / 0.904; 8: 0.361 / 0.499 / 0.906; 9: 0.365 / 0.529 / 0.908; 10: 0.361 / 0.492 / 0.912; 11: 0.352 / 0.475 / 0.917; 12: 0.362 / 0.496 / 0.913; 13: 0.362 / 0.495 / 0.912; 14: 0.354 / 0.483 / 0.912; 15: 0.357 / 0.494 / 0.912
- 7d: 1: 0.359 / 0.525 / 0.903; 2: 0.348 / 0.500 / 0.900; 3: 0.350 / 0.509 / 0.901; 4: 0.347 / 0.499 / 0.900; 5: 0.350 / 0.509 / 0.900; 6: 0.348 / 0.502 / 0.900; 7: 0.347 / 0.503 / 0.901; 8: 0.345 / 0.499 / 0.901; 9: 0.347 / 0.504 / 0.901; 10: 0.348 / 0.507 / 0.901; 11: 0.343 / 0.493 / 0.902; 12: 0.346 / 0.504 / 0.901; 13: 0.346 / 0.502 / 0.901; 14: 0.343 / 0.500 / 0.901; 15: 0.346 / 0.504 / 0.901
- 30d: 1: 0.359 / 0.513 / 0.900; 2: 0.352 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.351 / 0.500 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.350 / 0.504 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.496 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.502 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.110 (body 0.062, range 0.159); 'price stays where it was' would score 0.149; colour right 0.450; typical miss of the close 4.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.141 (body 0.089, range 0.194); 'price stays where it was' would score 0.185; colour right 0.518; typical miss of the close 7.0 bp; chain ended on the right side 0.708 of 24 chains; n=360
- 24h: match 0.120 (body 0.077, range 0.163); 'price stays where it was' would score 0.131; colour right 0.494; typical miss of the close 10.7 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.121 (body 0.082, range 0.160); 'price stays where it was' would score 0.129; colour right 0.496; typical miss of the close 8.0 bp; chain ended on the right side 0.519 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.517 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.1; 2: 0.196 / 4.5; 3: 0.164 / 6.1; 4: 0.133 / 6.8; 5: 0.121 / 7.4; 6: 0.109 / 8.0; 7: 0.101 / 8.3; 8: 0.096 / 8.8; 9: 0.086 / 8.8; 10: 0.084 / 9.5; 11: 0.079 / 10.3; 12: 0.076 / 10.6; 13: 0.063 / 10.9; 14: 0.066 / 11.2; 15: 0.058 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 107774, probability skill vs chance 0.2234, widened contest next: True
  - now: threshold 0.8398, hit rate recent 0.9697 / long run 0.9383
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.289, naive rule 0.460, lift 3.46x
    - 24h: 57 calls (57 a day), hit rate 0.982, chance 0.281, naive rule 0.459, lift 3.50x
    - 7d: 393 calls (56 a day), hit rate 0.941, chance 0.294, naive rule 0.493, lift 3.20x
    - 30d: 1717 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.23x
  - next: threshold 0.5266, hit rate recent 0.5384 / long run 0.5721
    - 6h: 14 calls (57 a day), hit rate 0.571, chance 0.289, lift 1.98x
    - 24h: 128 calls (128 a day), hit rate 0.562, chance 0.281, lift 2.00x
    - 7d: 735 calls (105 a day), hit rate 0.577, chance 0.294, lift 1.96x
    - 30d: 2555 calls (85 a day), hit rate 0.579, chance 0.290, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.489; 0.35: 540, 0.512; 0.40: 484, 0.562; 0.45: 415, 0.631; 0.50: 362, 0.685; 0.55: 317, 0.727; 0.60: 270, 0.772; 0.65: 224, 0.800; 0.70: 179, 0.834; 0.75: 138, 0.871; 0.80: 95, 0.912; 0.85: 49, 0.951; 0.90: 3, 0.979
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 498, 0.458; 0.40: 409, 0.489; 0.45: 314, 0.523; 0.50: 204, 0.558; 0.55: 92, 0.576; 0.60: 14, 0.597; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 107772, probability skill vs chance 0.2121, widened contest next: True
  - now: threshold 0.6957, hit rate recent 0.8557 / long run 0.8271
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.214, naive rule 0.443, lift 4.68x
    - 24h: 62 calls (62 a day), hit rate 0.871, chance 0.177, naive rule 0.376, lift 4.91x
    - 7d: 362 calls (52 a day), hit rate 0.829, chance 0.187, naive rule 0.405, lift 4.43x
    - 30d: 1600 calls (53 a day), hit rate 0.831, chance 0.187, naive rule 0.393, lift 4.45x
  - next: threshold 0.4148, hit rate recent 0.4287 / long run 0.4661
    - 6h: 14 calls (57 a day), hit rate 0.571, chance 0.214, lift 2.67x
    - 24h: 114 calls (115 a day), hit rate 0.412, chance 0.177, lift 2.33x
    - 7d: 638 calls (91 a day), hit rate 0.475, chance 0.187, lift 2.54x
    - 30d: 2258 calls (75 a day), hit rate 0.480, chance 0.187, lift 2.57x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.418; 0.35: 353, 0.482; 0.40: 284, 0.555; 0.45: 232, 0.611; 0.50: 181, 0.664; 0.55: 138, 0.708; 0.60: 108, 0.749; 0.65: 82, 0.792; 0.70: 60, 0.825; 0.75: 33, 0.867; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.389; 0.35: 251, 0.424; 0.40: 161, 0.452; 0.45: 78, 0.467; 0.50: 18, 0.504; 0.55: 2, 0.549
- **K=8**: model 1791936000, labels learned 107769, probability skill vs chance 0.1904, widened contest next: True
  - now: threshold 0.5822, hit rate recent 0.6812 / long run 0.6964
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.134, naive rule 0.331, lift 5.32x
    - 24h: 56 calls (56 a day), hit rate 0.679, chance 0.115, naive rule 0.292, lift 5.90x
    - 7d: 362 calls (52 a day), hit rate 0.693, chance 0.122, naive rule 0.338, lift 5.67x
    - 30d: 1577 calls (53 a day), hit rate 0.713, chance 0.122, naive rule 0.330, lift 5.84x
  - next: threshold 0.341, hit rate recent 0.2905 / long run 0.377
    - 6h: 18 calls (74 a day), hit rate 0.278, chance 0.134, lift 2.07x
    - 24h: 118 calls (119 a day), hit rate 0.288, chance 0.115, lift 2.50x
    - 7d: 582 calls (83 a day), hit rate 0.378, chance 0.122, lift 3.09x
    - 30d: 2140 calls (71 a day), hit rate 0.403, chance 0.122, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 259, 0.418; 0.35: 196, 0.491; 0.40: 149, 0.551; 0.45: 118, 0.594; 0.50: 90, 0.635; 0.55: 65, 0.684; 0.60: 44, 0.724; 0.65: 24, 0.779; 0.70: 9, 0.837; 0.75: 1, 0.783
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.353; 0.35: 106, 0.387; 0.40: 44, 0.418; 0.45: 9, 0.445; 0.50: 1, 0.382
- **K=13**: model 1792022400, labels learned 107764, probability skill vs chance 0.1728, widened contest next: False
  - now: threshold 0.4335, hit rate recent 0.5466 / long run 0.5726
    - 6h: 9 calls (38 a day), hit rate 0.778, chance 0.090, naive rule 0.296, lift 8.66x
    - 24h: 70 calls (71 a day), hit rate 0.543, chance 0.077, naive rule 0.245, lift 7.03x
    - 7d: 371 calls (53 a day), hit rate 0.561, chance 0.079, naive rule 0.283, lift 7.06x
    - 30d: 1512 calls (50 a day), hit rate 0.585, chance 0.078, naive rule 0.272, lift 7.51x
  - next: threshold 0.301, hit rate recent 0.2943 / long run 0.3096
    - 6h: 6 calls (25 a day), hit rate 0.500, chance 0.090, lift 5.56x
    - 24h: 61 calls (62 a day), hit rate 0.311, chance 0.077, lift 4.04x
    - 7d: 442 calls (63 a day), hit rate 0.312, chance 0.079, lift 3.93x
    - 30d: 2036 calls (68 a day), hit rate 0.312, chance 0.078, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 117, 0.452; 0.35: 85, 0.512; 0.40: 61, 0.564; 0.45: 41, 0.618; 0.50: 25, 0.656; 0.55: 14, 0.706; 0.60: 4, 0.766; 0.65: 0, 0.938
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.323; 0.35: 13, 0.360; 0.40: 2, 0.385

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.829 | 18.96% | 0.950 | 0.633 | 0.251 | 0.433 | 0.264 |
| 6h | 14.092 | 5.81% | 0.925 | 0.544 | 0.252 | 0.468 | 0.675 |
| 24h | 16.611 | 4.41% | 0.897 | 0.503 | 0.251 | 0.481 | 0.642 |
| 7d | 14.801 | 4.17% | 0.900 | 0.500 | 0.251 | 0.489 | 0.671 |
| 30d | 14.059 | 3.98% | 0.900 | 0.500 | 0.251 | 0.495 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 8.426 | 6.803 | 7.344 | 6.830 | 7.113 | 7.328 | 6.706 | 6.713 | 6.885 | 6.829 |
| 6h | 14.961 | 14.205 | 14.211 | 14.114 | 14.485 | 14.260 | 14.035 | 14.003 | 14.061 | 14.092 |
| 24h | 17.377 | 16.826 | 16.686 | 16.640 | 16.904 | 16.712 | 16.599 | 16.609 | 16.585 | 16.611 |
| 7d | 15.445 | 14.964 | 14.886 | 14.816 | 15.061 | 14.994 | 14.807 | 14.777 | 14.773 | 14.801 |
| 30d | 14.643 | 14.184 | 14.143 | 14.085 | 14.315 | 14.243 | 14.058 | 14.032 | 14.033 | 14.059 |

## Next candle

- candle starting 2026-10-17 00:20 UTC, last close 2417.66
- P(up) 0.5127, return quantiles (bp): {'05': -6.403, '10': -4.687, '25': -2.101, '40': -0.534, '50': 0.076, '60': 0.988, '75': 2.347, '90': 4.913, '95': 6.725}
- changepoint probability 0.1978, regime age 141.6 min
- agent weights: empirical 0.003, ewma 0.062, garch 0.123, har 0.180, bocpd 0.033, hmm 0.108, online_qr 0.249, lgbm 0.241

## Learning log

- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- 2026-10-15 12:00 UTC: {"garch": {"alpha": 0.1654, "beta": 0.8078}, "hmm": {"sd_bp": [2.37, 5.56, 18.85], "stay": [0.953, 0.968, 0.861]}}
- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.98, 7.01, 21.66], current probabilities: [0.758, 0.227, 0.015]
- live generator: {'versions': 60, 'latest_effective': '2026-10-17 00:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.22, 'l_abs': 0.762, 'l_hi': 0.734, 'l_lo': 0.718, 'b05': 0.743, 'b25': 0.7, 'b75': 0.725, 'b95': 0.718}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.2, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.403, 1.589, 1.802, 2.144, 2.216, 2.399, 2.372, 2.521, 2.558, 2.384, 2.87, 3.116, 3.176, 3.229]}
- calibration offsets (in sigma): {'05': 0.0795, '10': 0.059, '25': 0.0675, '40': 0.066, '50': 0.005, '60': 0.024, '75': -0.0575, '90': -0.079, '95': -0.0595}
