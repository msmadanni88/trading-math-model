# ETH-USD 60s candle generator - report

- generated: 2026-10-25 16:45 UTC
- last closed candle: 2026-10-25 16:45 UTC (staleness 1.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.543 (672) [0.509, 0.577] | 0.517 (2876) [0.498, 0.536] | 0.515 (5082) [0.500, 0.528] | 0.519 (2110) [0.495, 0.543] | 0.627 (67) | 0.500 | flat +0.040 (noise 0.027) |
| colour_clear | 0.544 (743) | 0.553 (5669) [0.547, 0.562] | 0.533 (23412) [0.525, 0.541] | 0.517 (41491) [0.511, 0.524] | 0.547 (17253) [0.542, 0.552] | 0.552 (560) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.606 (269) | 0.608 (1282) [0.589, 0.628] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.559 (220) | 0.500 | flat +0.016 (noise 0.023) |
| colour_next | 0.522 (1431) | 0.534 (10039) [0.527, 0.541] | 0.523 (42853) [0.517, 0.528] | 0.513 (75756) [0.508, 0.517] | 0.530 (31407) [0.525, 0.534] | 0.530 (1002) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.501 (140546) [0.498, 0.503] | 0.501 (599942) [0.499, 0.502] | 0.501 (1060584) [0.500, 0.501] | 0.500 (439698) [0.498, 0.502] | 0.507 (14028) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.602 (98) | 0.636 (335) [0.607, 0.672] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.609 (92) | 0.500 | flat -0.005 (noise 0.045) |
| reversal_k13_next | 0.286 (63) | 0.310 (481) [0.291, 0.327] | 0.305 (2173) [0.292, 0.317] | 0.306 (3618) [0.296, 0.318] | 0.316 (1513) [0.305, 0.327] | 0.358 (53) | 0.077 | flat +0.004 (noise 0.031) |
| reversal_k13_now | 0.647 (51) | 0.530 (366) [0.490, 0.576] | 0.570 (1560) [0.549, 0.591] | 0.573 (2651) [0.557, 0.590] | 0.564 (1179) [0.540, 0.590] | 0.590 (39) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.630 (54) | 0.592 (699) [0.564, 0.624] | 0.580 (2792) [0.566, 0.594] | 0.584 (4562) [0.573, 0.594] | 0.580 (2122) [0.565, 0.596] | 0.609 (46) | 0.293 | flat +0.024 (noise 0.026) |
| reversal_k3_now | 0.980 (49) | 0.945 (397) [0.928, 0.962] | 0.938 (1690) [0.929, 0.947] | 0.938 (3023) [0.932, 0.945] | 0.933 (1260) [0.923, 0.944] | 0.906 (32) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.480 (125) | 0.460 (939) [0.433, 0.486] | 0.464 (2842) [0.449, 0.479] | 0.476 (4306) [0.463, 0.489] | 0.460 (2316) [0.445, 0.476] | 0.500 (96) | 0.187 | flat -0.006 (noise 0.025) |
| reversal_k5_now | 0.818 (55) | 0.812 (361) [0.800, 0.823] | 0.831 (1561) [0.818, 0.844] | 0.830 (2771) [0.819, 0.841] | 0.819 (1160) [0.804, 0.833] | 0.849 (33) | 0.187 | flat -0.006 (noise 0.029) |
| reversal_k8_next | 0.384 (86) | 0.377 (757) [0.359, 0.394] | 0.383 (2519) [0.370, 0.396] | 0.389 (4187) [0.377, 0.400] | 0.381 (2081) [0.367, 0.395] | 0.384 (86) | 0.120 | flat +0.004 (noise 0.026) |
| reversal_k8_now | 0.709 (55) | 0.654 (332) [0.613, 0.693] | 0.701 (1523) [0.681, 0.722] | 0.702 (2739) [0.686, 0.718] | 0.685 (1152) [0.662, 0.708] | 0.758 (33) | 0.121 | flat -0.031 (noise 0.036) |
| overall | 0.505 (22099) | 0.504 (155589) [0.501, 0.507] | 0.504 (662331) [0.502, 0.505] | 0.503 (1169279) [0.502, 0.504] | 0.504 (485998) [0.502, 0.506] | 0.510 (15515) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07526, 0.1116] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5362, 'levels': [{'threshold': 0.07526, 'calls_per_day': 148.3, 'win_rate': 0.6104}, {'threshold': 0.1116, 'calls_per_day': 38.2, 'win_rate': 0.6679}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 31270, 'rate': 0.5309}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15215 | 0.336 | 0.524 (14966) | 0.587 (1720) | 0.761 (2511) |
| volatility: normal | 15215 | 0.364 | 0.522 (15148) | 0.607 (1174) | 0.760 (2246) |
| volatility: wild | 15215 | 0.378 | 0.519 (15177) | 0.636 (519) | 0.771 (1915) |
| session: Asia 00-08 | 15360 | 0.357 | 0.527 (15256) | 0.607 (1220) | 0.766 (2206) |
| session: Europe 08-13 | 9600 | 0.355 | 0.524 (9513) | 0.598 (858) | 0.761 (1524) |
| session: US 13-21 | 15105 | 0.368 | 0.518 (15005) | 0.593 (840) | 0.772 (2128) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5517) | 0.610 (495) | 0.737 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.355 | 0.351 | 0.264 | 0.264 | 0.483 | 0.261 | 0.449 | 0.974 |
| 6h | 360 | 0.352 | 0.345 | 0.264 | 0.293 | 0.542 | 0.261 | 0.442 | 1.114 |
| 24h | 1440 | 0.352 | 0.341 | 0.264 | 0.287 | 0.523 | 0.263 | 0.441 | 1.299 |
| 7d | 10080 | 0.371 | 0.360 | 0.274 | 0.307 | 0.536 | 0.269 | 0.472 | 1.205 |
| 30d | 43200 | 0.359 | 0.353 | 0.276 | 0.304 | 0.524 | 0.257 | 0.462 | 1.288 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.355 / 0.483 / 0.917; 2: 0.361 / 0.600 / 0.950; 3: 0.320 / 0.433 / 0.850; 4: 0.342 / 0.550 / 0.900; 5: 0.336 / 0.533 / 0.900; 6: 0.316 / 0.417 / 0.967; 7: 0.339 / 0.500 / 0.983; 8: 0.306 / 0.450 / 0.967; 9: 0.331 / 0.467 / 1.000; 10: 0.347 / 0.517 / 0.983; 11: 0.342 / 0.583 / 1.000; 12: 0.347 / 0.583 / 1.000; 13: 0.350 / 0.617 / 0.983; 14: 0.322 / 0.483 / 1.000; 15: 0.361 / 0.617 / 1.000
- 6h: 1: 0.352 / 0.542 / 0.869; 2: 0.330 / 0.486 / 0.892; 3: 0.336 / 0.506 / 0.869; 4: 0.330 / 0.506 / 0.886; 5: 0.331 / 0.519 / 0.886; 6: 0.342 / 0.547 / 0.906; 7: 0.319 / 0.489 / 0.914; 8: 0.337 / 0.550 / 0.900; 9: 0.325 / 0.483 / 0.911; 10: 0.340 / 0.542 / 0.900; 11: 0.332 / 0.528 / 0.894; 12: 0.321 / 0.517 / 0.883; 13: 0.327 / 0.514 / 0.875; 14: 0.316 / 0.503 / 0.872; 15: 0.334 / 0.503 / 0.875
- 24h: 1: 0.352 / 0.523 / 0.891; 2: 0.336 / 0.498 / 0.899; 3: 0.338 / 0.504 / 0.896; 4: 0.341 / 0.522 / 0.899; 5: 0.334 / 0.502 / 0.901; 6: 0.337 / 0.510 / 0.905; 7: 0.335 / 0.505 / 0.905; 8: 0.335 / 0.503 / 0.902; 9: 0.334 / 0.488 / 0.904; 10: 0.335 / 0.503 / 0.902; 11: 0.336 / 0.520 / 0.906; 12: 0.339 / 0.528 / 0.904; 13: 0.337 / 0.510 / 0.903; 14: 0.337 / 0.514 / 0.908; 15: 0.334 / 0.495 / 0.908
- 7d: 1: 0.371 / 0.536 / 0.899; 2: 0.358 / 0.502 / 0.900; 3: 0.358 / 0.509 / 0.900; 4: 0.353 / 0.495 / 0.900; 5: 0.354 / 0.501 / 0.900; 6: 0.353 / 0.495 / 0.901; 7: 0.351 / 0.494 / 0.901; 8: 0.355 / 0.509 / 0.901; 9: 0.352 / 0.497 / 0.900; 10: 0.353 / 0.507 / 0.901; 11: 0.351 / 0.500 / 0.901; 12: 0.352 / 0.505 / 0.900; 13: 0.349 / 0.496 / 0.900; 14: 0.351 / 0.499 / 0.900; 15: 0.350 / 0.502 / 0.901
- 30d: 1: 0.359 / 0.524 / 0.899; 2: 0.349 / 0.498 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.347 / 0.498 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.346 / 0.500 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.344 / 0.496 / 0.900; 10: 0.346 / 0.505 / 0.900; 11: 0.344 / 0.499 / 0.900; 12: 0.346 / 0.504 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.344 / 0.498 / 0.900; 15: 0.344 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.170 (body 0.115, range 0.225); 'price stays where it was' would score 0.118; colour right 0.433; typical miss of the close 4.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.083, range 0.153); 'price stays where it was' would score 0.121; colour right 0.453; typical miss of the close 8.9 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.126 (body 0.091, range 0.162); 'price stays where it was' would score 0.135; colour right 0.489; typical miss of the close 6.9 bp; chain ended on the right side 0.604 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.169); 'price stays where it was' would score 0.135; colour right 0.501; typical miss of the close 8.8 bp; chain ended on the right side 0.548 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.5 bp; chain ended on the right side 0.522 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.195 / 4.4; 3: 0.168 / 5.7; 4: 0.131 / 6.3; 5: 0.123 / 6.9; 6: 0.111 / 7.5; 7: 0.106 / 7.8; 8: 0.097 / 8.2; 9: 0.087 / 8.2; 10: 0.088 / 8.8; 11: 0.084 / 9.3; 12: 0.077 / 9.6; 13: 0.068 / 9.8; 14: 0.068 / 10.2; 15: 0.059 / 10.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 120279, probability skill vs chance 0.224, widened contest next: False
  - now: threshold 0.8345, hit rate recent 0.9421 / long run 0.9375
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.282, naive rule 0.485, lift 3.55x
    - 24h: 42 calls (42 a day), hit rate 0.929, chance 0.298, naive rule 0.519, lift 3.12x
    - 7d: 383 calls (55 a day), hit rate 0.940, chance 0.295, naive rule 0.499, lift 3.18x
    - 30d: 1685 calls (56 a day), hit rate 0.936, chance 0.294, naive rule 0.492, lift 3.18x
  - next: threshold 0.5434, hit rate recent 0.5995 / long run 0.5922
    - 6h: 21 calls (85 a day), hit rate 0.476, chance 0.282, lift 1.69x
    - 24h: 55 calls (55 a day), hit rate 0.600, chance 0.298, lift 2.01x
    - 7d: 678 calls (97 a day), hit rate 0.596, chance 0.295, lift 2.02x
    - 30d: 2792 calls (93 a day), hit rate 0.580, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 538, 0.520; 0.40: 478, 0.576; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 312, 0.741; 0.60: 264, 0.785; 0.65: 221, 0.810; 0.70: 174, 0.841; 0.75: 135, 0.875; 0.80: 91, 0.914; 0.85: 47, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.426; 0.35: 502, 0.464; 0.40: 408, 0.498; 0.45: 310, 0.533; 0.50: 202, 0.568; 0.55: 90, 0.576; 0.60: 14, 0.617; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 120277, probability skill vs chance 0.2093, widened contest next: False
  - now: threshold 0.6733, hit rate recent 0.8235 / long run 0.8213
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.133, naive rule 0.301, lift 7.51x
    - 24h: 47 calls (47 a day), hit rate 0.830, chance 0.168, naive rule 0.394, lift 4.94x
    - 7d: 358 calls (51 a day), hit rate 0.810, chance 0.183, naive rule 0.402, lift 4.44x
    - 30d: 1558 calls (52 a day), hit rate 0.831, chance 0.187, naive rule 0.400, lift 4.44x
  - next: threshold 0.4195, hit rate recent 0.479 / long run 0.4742
    - 6h: 34 calls (139 a day), hit rate 0.412, chance 0.133, lift 3.09x
    - 24h: 135 calls (136 a day), hit rate 0.481, chance 0.168, lift 2.87x
    - 7d: 922 calls (132 a day), hit rate 0.470, chance 0.183, lift 2.57x
    - 30d: 2914 calls (97 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.426; 0.35: 343, 0.494; 0.40: 276, 0.566; 0.45: 223, 0.621; 0.50: 175, 0.671; 0.55: 135, 0.711; 0.60: 104, 0.755; 0.65: 75, 0.793; 0.70: 53, 0.832; 0.75: 31, 0.878; 0.80: 10, 0.903
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.388; 0.35: 252, 0.421; 0.40: 158, 0.453; 0.45: 70, 0.465; 0.50: 15, 0.489; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 120274, probability skill vs chance 0.1973, widened contest next: False
  - now: threshold 0.5563, hit rate recent 0.7079 / long run 0.6859
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.101, naive rule 0.252, lift 8.87x
    - 24h: 46 calls (46 a day), hit rate 0.761, chance 0.107, naive rule 0.318, lift 7.13x
    - 7d: 332 calls (47 a day), hit rate 0.660, chance 0.115, naive rule 0.318, lift 5.75x
    - 30d: 1522 calls (51 a day), hit rate 0.698, chance 0.121, naive rule 0.330, lift 5.79x
  - next: threshold 0.3372, hit rate recent 0.3782 / long run 0.3791
    - 6h: 32 calls (132 a day), hit rate 0.312, chance 0.101, lift 3.08x
    - 24h: 106 calls (107 a day), hit rate 0.387, chance 0.107, lift 3.63x
    - 7d: 762 calls (109 a day), hit rate 0.374, chance 0.115, lift 3.26x
    - 30d: 2568 calls (86 a day), hit rate 0.382, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.426; 0.35: 189, 0.496; 0.40: 144, 0.548; 0.45: 110, 0.595; 0.50: 84, 0.638; 0.55: 61, 0.675; 0.60: 41, 0.722; 0.65: 23, 0.788; 0.70: 10, 0.830; 0.75: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.351; 0.35: 98, 0.379; 0.40: 36, 0.398; 0.45: 8, 0.424; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 120269, probability skill vs chance 0.179, widened contest next: False
  - now: threshold 0.4075, hit rate recent 0.5978 / long run 0.5603
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.074, naive rule 0.209, lift 9.66x
    - 24h: 50 calls (51 a day), hit rate 0.640, chance 0.072, naive rule 0.262, lift 8.90x
    - 7d: 356 calls (51 a day), hit rate 0.542, chance 0.073, naive rule 0.265, lift 7.38x
    - 30d: 1567 calls (52 a day), hit rate 0.568, chance 0.077, naive rule 0.273, lift 7.36x
  - next: threshold 0.294, hit rate recent 0.3256 / long run 0.3121
    - 6h: 22 calls (92 a day), hit rate 0.273, chance 0.074, lift 3.69x
    - 24h: 73 calls (74 a day), hit rate 0.370, chance 0.072, lift 5.14x
    - 7d: 481 calls (69 a day), hit rate 0.310, chance 0.073, lift 4.22x
    - 30d: 2173 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.94x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.445; 0.35: 87, 0.496; 0.40: 62, 0.552; 0.45: 41, 0.603; 0.50: 26, 0.658; 0.55: 15, 0.703; 0.60: 7, 0.745; 0.65: 2, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.316; 0.35: 14, 0.347; 0.40: 2, 0.420; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.981 | 1.05% | 0.933 | 0.467 | 0.251 | 0.433 | 0.356 |
| 6h | 13.096 | 0.99% | 0.875 | 0.483 | 0.249 | 0.503 | 0.357 |
| 24h | 11.483 | 1.82% | 0.890 | 0.489 | 0.251 | 0.487 | 0.541 |
| 7d | 15.016 | 3.22% | 0.900 | 0.500 | 0.250 | 0.500 | 0.648 |
| 30d | 13.281 | 4.19% | 0.900 | 0.500 | 0.251 | 0.495 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.097 | 11.175 | 11.047 | 10.962 | 11.358 | 11.128 | 10.898 | 10.963 | 10.947 | 10.981 |
| 6h | 13.227 | 13.279 | 13.228 | 13.099 | 13.483 | 13.235 | 13.045 | 13.004 | 13.047 | 13.096 |
| 24h | 11.696 | 11.599 | 11.539 | 11.549 | 11.715 | 11.655 | 11.477 | 11.428 | 11.457 | 11.483 |
| 7d | 15.516 | 15.162 | 15.094 | 15.032 | 15.287 | 15.169 | 15.002 | 14.980 | 14.988 | 15.016 |
| 30d | 13.862 | 13.409 | 13.364 | 13.304 | 13.521 | 13.474 | 13.277 | 13.258 | 13.257 | 13.281 |

## Next candle

- candle starting 2026-10-25 16:45 UTC, last close 2340.57
- P(up) 0.4995, return quantiles (bp): {'05': -7.262, '10': -5.44, '25': -2.843, '40': -0.764, '50': -0.02, '60': 1.022, '75': 2.933, '90': 5.476, '95': 7.04}
- changepoint probability 0.052, regime age 174.9 min
- agent weights: empirical 0.018, ewma 0.041, garch 0.080, har 0.163, bocpd 0.012, hmm 0.042, online_qr 0.255, lgbm 0.390

## Learning log

- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.8, 19.68], current probabilities: [0.765, 0.233, 0.002]
- live generator: {'versions': 60, 'latest_effective': '2026-10-25 16:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.485, 'l_abs': 0.713, 'l_hi': 0.77, 'l_lo': 0.767, 'b05': 0.722, 'b25': 0.697, 'b75': 0.693, 'b95': 0.682}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6]], 'cone_width': [1.566, 2.167, 2.361, 2.645, 2.474, 2.522, 2.985, 3.173, 3.558, 3.665, 4.073, 4.421, 4.507, 4.581]}
- calibration offsets (in sigma): {'05': 0.012, '10': -0.026, '25': -0.04, '40': -0.004, '50': -0.01, '60': 0.004, '75': 0.06, '90': 0.016, '95': -0.002}
