# ETH-USD 60s candle generator - report

- generated: 2026-10-25 12:30 UTC
- last closed candle: 2026-10-25 12:30 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.510 (96) | 0.543 (672) [0.509, 0.577] | 0.517 (2876) [0.498, 0.536] | 0.515 (5082) [0.500, 0.528] | 0.519 (2110) [0.495, 0.543] | 0.620 (50) | 0.500 | flat +0.040 (noise 0.027) |
| colour_clear | 0.544 (743) | 0.553 (5669) [0.547, 0.562] | 0.533 (23412) [0.525, 0.541] | 0.517 (41491) [0.511, 0.524] | 0.547 (17253) [0.542, 0.552] | 0.547 (408) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.606 (269) | 0.608 (1282) [0.589, 0.628] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.604 (3193) [0.590, 0.619] | 0.551 (165) | 0.500 | flat +0.016 (noise 0.023) |
| colour_next | 0.522 (1431) | 0.534 (10039) [0.527, 0.541] | 0.523 (42853) [0.517, 0.528] | 0.513 (75756) [0.508, 0.517] | 0.530 (31407) [0.525, 0.534] | 0.525 (747) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.502 (20034) | 0.501 (140546) [0.498, 0.503] | 0.501 (599942) [0.499, 0.502] | 0.501 (1060584) [0.500, 0.501] | 0.500 (439698) [0.498, 0.502] | 0.502 (10458) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.602 (98) | 0.636 (335) [0.607, 0.672] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.645 (834) [0.622, 0.671] | 0.643 (70) | 0.500 | flat -0.005 (noise 0.045) |
| reversal_k13_next | 0.286 (63) | 0.310 (481) [0.291, 0.327] | 0.305 (2173) [0.292, 0.317] | 0.306 (3618) [0.296, 0.318] | 0.316 (1513) [0.305, 0.327] | 0.436 (39) | 0.077 | flat +0.004 (noise 0.031) |
| reversal_k13_now | 0.647 (51) | 0.530 (366) [0.490, 0.576] | 0.570 (1560) [0.549, 0.591] | 0.573 (2651) [0.557, 0.590] | 0.564 (1179) [0.540, 0.590] | 0.517 (29) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.630 (54) | 0.592 (699) [0.564, 0.624] | 0.580 (2792) [0.566, 0.594] | 0.584 (4562) [0.573, 0.594] | 0.580 (2122) [0.565, 0.596] | 0.688 (32) | 0.293 | flat +0.024 (noise 0.026) |
| reversal_k3_now | 0.980 (49) | 0.945 (397) [0.928, 0.962] | 0.938 (1690) [0.929, 0.947] | 0.938 (3023) [0.932, 0.945] | 0.933 (1260) [0.923, 0.944] | 0.875 (24) | 0.293 | flat +0.012 (noise 0.019) |
| reversal_k5_next | 0.480 (125) | 0.460 (939) [0.433, 0.486] | 0.464 (2842) [0.449, 0.479] | 0.476 (4306) [0.463, 0.489] | 0.460 (2316) [0.445, 0.476] | 0.520 (75) | 0.187 | flat -0.006 (noise 0.025) |
| reversal_k5_now | 0.818 (55) | 0.812 (361) [0.800, 0.823] | 0.831 (1561) [0.818, 0.844] | 0.830 (2771) [0.819, 0.841] | 0.819 (1160) [0.804, 0.833] | 0.783 (23) | 0.187 | flat -0.006 (noise 0.029) |
| reversal_k8_next | 0.384 (86) | 0.377 (757) [0.359, 0.394] | 0.383 (2519) [0.370, 0.396] | 0.389 (4187) [0.377, 0.400] | 0.381 (2081) [0.367, 0.395] | 0.412 (68) | 0.120 | flat +0.004 (noise 0.026) |
| reversal_k8_now | 0.709 (55) | 0.654 (332) [0.613, 0.693] | 0.701 (1523) [0.681, 0.722] | 0.702 (2739) [0.686, 0.718] | 0.685 (1152) [0.662, 0.708] | 0.708 (24) | 0.121 | flat -0.031 (noise 0.036) |
| overall | 0.505 (22099) | 0.504 (155589) [0.501, 0.507] | 0.504 (662331) [0.502, 0.505] | 0.503 (1169279) [0.502, 0.504] | 0.504 (485998) [0.502, 0.506] | 0.505 (11569) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07526, 0.1116] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5362, 'levels': [{'threshold': 0.07526, 'calls_per_day': 148.3, 'win_rate': 0.6104}, {'threshold': 0.1116, 'calls_per_day': 38.2, 'win_rate': 0.6679}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 31015, 'rate': 0.5308}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15130 | 0.336 | 0.524 (14883) | 0.587 (1717) | 0.763 (2499) |
| volatility: normal | 15130 | 0.364 | 0.522 (15060) | 0.609 (1124) | 0.754 (2225) |
| volatility: wild | 15130 | 0.378 | 0.519 (15093) | 0.634 (517) | 0.771 (1911) |
| session: Asia 00-08 | 15360 | 0.357 | 0.527 (15256) | 0.607 (1220) | 0.766 (2206) |
| session: Europe 08-13 | 9570 | 0.355 | 0.524 (9483) | 0.595 (845) | 0.760 (1519) |
| session: US 13-21 | 14880 | 0.368 | 0.518 (14780) | 0.597 (798) | 0.770 (2096) |
| session: late 21-24 | 5580 | 0.351 | 0.514 (5517) | 0.610 (495) | 0.737 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.349 | 0.391 | 0.288 | 0.288 | 0.517 | 0.235 | 0.464 | 1.500 |
| 6h | 360 | 0.350 | 0.329 | 0.256 | 0.270 | 0.564 | 0.269 | 0.430 | 1.218 |
| 24h | 1440 | 0.353 | 0.345 | 0.270 | 0.293 | 0.522 | 0.262 | 0.445 | 1.256 |
| 7d | 10080 | 0.371 | 0.360 | 0.274 | 0.306 | 0.536 | 0.270 | 0.472 | 1.211 |
| 30d | 43200 | 0.360 | 0.353 | 0.276 | 0.305 | 0.524 | 0.256 | 0.463 | 1.286 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.349 / 0.517 / 0.883; 2: 0.336 / 0.500 / 0.933; 3: 0.317 / 0.450 / 0.933; 4: 0.342 / 0.517 / 0.950; 5: 0.327 / 0.500 / 0.933; 6: 0.345 / 0.567 / 0.883; 7: 0.288 / 0.350 / 0.900; 8: 0.346 / 0.550 / 0.867; 9: 0.306 / 0.467 / 0.867; 10: 0.341 / 0.550 / 0.883; 11: 0.309 / 0.450 / 0.833; 12: 0.316 / 0.517 / 0.833; 13: 0.318 / 0.483 / 0.817; 14: 0.347 / 0.567 / 0.833; 15: 0.326 / 0.433 / 0.833
- 6h: 1: 0.350 / 0.564 / 0.889; 2: 0.325 / 0.497 / 0.906; 3: 0.328 / 0.500 / 0.922; 4: 0.337 / 0.525 / 0.933; 5: 0.321 / 0.478 / 0.908; 6: 0.330 / 0.489 / 0.908; 7: 0.319 / 0.475 / 0.922; 8: 0.326 / 0.494 / 0.911; 9: 0.317 / 0.472 / 0.903; 10: 0.329 / 0.514 / 0.925; 11: 0.326 / 0.539 / 0.925; 12: 0.323 / 0.506 / 0.928; 13: 0.316 / 0.497 / 0.936; 14: 0.329 / 0.522 / 0.936; 15: 0.321 / 0.486 / 0.942
- 24h: 1: 0.353 / 0.522 / 0.897; 2: 0.337 / 0.494 / 0.902; 3: 0.340 / 0.502 / 0.901; 4: 0.340 / 0.512 / 0.902; 5: 0.337 / 0.506 / 0.896; 6: 0.333 / 0.487 / 0.895; 7: 0.337 / 0.507 / 0.897; 8: 0.336 / 0.499 / 0.898; 9: 0.331 / 0.478 / 0.894; 10: 0.335 / 0.505 / 0.901; 11: 0.335 / 0.508 / 0.897; 12: 0.343 / 0.529 / 0.903; 13: 0.334 / 0.497 / 0.903; 14: 0.337 / 0.506 / 0.906; 15: 0.331 / 0.490 / 0.906
- 7d: 1: 0.371 / 0.536 / 0.900; 2: 0.358 / 0.501 / 0.900; 3: 0.358 / 0.508 / 0.900; 4: 0.354 / 0.496 / 0.900; 5: 0.354 / 0.500 / 0.900; 6: 0.352 / 0.494 / 0.899; 7: 0.352 / 0.494 / 0.899; 8: 0.355 / 0.508 / 0.899; 9: 0.352 / 0.498 / 0.899; 10: 0.353 / 0.507 / 0.899; 11: 0.351 / 0.500 / 0.898; 12: 0.353 / 0.505 / 0.899; 13: 0.350 / 0.495 / 0.899; 14: 0.352 / 0.501 / 0.899; 15: 0.350 / 0.502 / 0.899
- 30d: 1: 0.360 / 0.524 / 0.899; 2: 0.349 / 0.498 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.498 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.344 / 0.499 / 0.900; 12: 0.346 / 0.504 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.344 / 0.498 / 0.900; 15: 0.344 / 0.500 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.131 (body 0.098, range 0.164); 'price stays where it was' would score 0.127; colour right 0.433; typical miss of the close 8.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.131 (body 0.100, range 0.163); 'price stays where it was' would score 0.118; colour right 0.497; typical miss of the close 8.2 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.121 (body 0.086, range 0.155); 'price stays where it was' would score 0.135; colour right 0.485; typical miss of the close 7.5 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.127 (body 0.087, range 0.167); 'price stays where it was' would score 0.134; colour right 0.502; typical miss of the close 9.0 bp; chain ended on the right side 0.546 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.127; colour right 0.499; typical miss of the close 7.5 bp; chain ended on the right side 0.520 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.195 / 4.4; 3: 0.168 / 5.7; 4: 0.131 / 6.4; 5: 0.123 / 7.0; 6: 0.111 / 7.5; 7: 0.106 / 7.8; 8: 0.097 / 8.2; 9: 0.087 / 8.2; 10: 0.087 / 8.8; 11: 0.084 / 9.3; 12: 0.077 / 9.7; 13: 0.068 / 9.9; 14: 0.069 / 10.3; 15: 0.059 / 10.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 120024, probability skill vs chance 0.2221, widened contest next: False
  - now: threshold 0.8345, hit rate recent 0.9337 / long run 0.9366
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.287, naive rule 0.484, lift 2.78x
    - 24h: 44 calls (44 a day), hit rate 0.932, chance 0.301, naive rule 0.522, lift 3.10x
    - 7d: 382 calls (55 a day), hit rate 0.940, chance 0.295, naive rule 0.499, lift 3.18x
    - 30d: 1687 calls (56 a day), hit rate 0.936, chance 0.294, naive rule 0.492, lift 3.18x
  - next: threshold 0.5434, hit rate recent 0.6438 / long run 0.5961
    - 6h: 19 calls (77 a day), hit rate 0.632, chance 0.287, lift 2.20x
    - 24h: 49 calls (49 a day), hit rate 0.633, chance 0.301, lift 2.10x
    - 7d: 681 calls (97 a day), hit rate 0.598, chance 0.295, lift 2.02x
    - 30d: 2788 calls (93 a day), hit rate 0.581, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 539, 0.519; 0.40: 478, 0.576; 0.45: 409, 0.646; 0.50: 357, 0.699; 0.55: 312, 0.740; 0.60: 264, 0.784; 0.65: 221, 0.809; 0.70: 175, 0.841; 0.75: 136, 0.875; 0.80: 91, 0.914; 0.85: 47, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.426; 0.35: 501, 0.464; 0.40: 407, 0.498; 0.45: 310, 0.533; 0.50: 202, 0.568; 0.55: 90, 0.576; 0.60: 14, 0.617; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 120022, probability skill vs chance 0.2114, widened contest next: False
  - now: threshold 0.6733, hit rate recent 0.7912 / long run 0.8183
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.153, naive rule 0.350, lift 3.92x
    - 24h: 53 calls (53 a day), hit rate 0.792, chance 0.175, naive rule 0.418, lift 4.53x
    - 7d: 356 calls (51 a day), hit rate 0.806, chance 0.184, naive rule 0.404, lift 4.39x
    - 30d: 1560 calls (52 a day), hit rate 0.831, chance 0.188, naive rule 0.401, lift 4.43x
  - next: threshold 0.4195, hit rate recent 0.4945 / long run 0.4758
    - 6h: 34 calls (139 a day), hit rate 0.471, chance 0.153, lift 3.08x
    - 24h: 134 calls (135 a day), hit rate 0.515, chance 0.175, lift 2.95x
    - 7d: 932 calls (133 a day), hit rate 0.467, chance 0.184, lift 2.54x
    - 30d: 2900 calls (97 a day), hit rate 0.465, chance 0.188, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.427; 0.35: 343, 0.495; 0.40: 276, 0.566; 0.45: 223, 0.622; 0.50: 175, 0.672; 0.55: 135, 0.712; 0.60: 104, 0.755; 0.65: 76, 0.792; 0.70: 53, 0.832; 0.75: 31, 0.877; 0.80: 10, 0.901
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 341, 0.389; 0.35: 252, 0.422; 0.40: 158, 0.454; 0.45: 70, 0.465; 0.50: 15, 0.490; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 120019, probability skill vs chance 0.1977, widened contest next: False
  - now: threshold 0.5563, hit rate recent 0.6786 / long run 0.6828
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.090, naive rule 0.264, lift 6.67x
    - 24h: 50 calls (50 a day), hit rate 0.680, chance 0.113, naive rule 0.344, lift 6.04x
    - 7d: 332 calls (47 a day), hit rate 0.651, chance 0.115, naive rule 0.321, lift 5.64x
    - 30d: 1525 calls (51 a day), hit rate 0.699, chance 0.121, naive rule 0.330, lift 5.78x
  - next: threshold 0.3372, hit rate recent 0.4074 / long run 0.3822
    - 6h: 33 calls (136 a day), hit rate 0.424, chance 0.090, lift 4.71x
    - 24h: 107 calls (108 a day), hit rate 0.421, chance 0.113, lift 3.74x
    - 7d: 765 calls (109 a day), hit rate 0.378, chance 0.115, lift 3.28x
    - 30d: 2559 calls (85 a day), hit rate 0.384, chance 0.121, lift 3.17x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 249, 0.427; 0.35: 189, 0.497; 0.40: 144, 0.550; 0.45: 110, 0.596; 0.50: 84, 0.638; 0.55: 61, 0.677; 0.60: 41, 0.722; 0.65: 23, 0.788; 0.70: 10, 0.830; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.352; 0.35: 98, 0.380; 0.40: 36, 0.401; 0.45: 8, 0.433; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 120014, probability skill vs chance 0.1832, widened contest next: False
  - now: threshold 0.4075, hit rate recent 0.5595 / long run 0.5562
    - 6h: 12 calls (50 a day), hit rate 0.500, chance 0.070, naive rule 0.250, lift 7.19x
    - 24h: 51 calls (52 a day), hit rate 0.569, chance 0.069, naive rule 0.269, lift 8.18x
    - 7d: 360 calls (52 a day), hit rate 0.528, chance 0.074, naive rule 0.267, lift 7.17x
    - 30d: 1567 calls (52 a day), hit rate 0.566, chance 0.077, naive rule 0.273, lift 7.33x
  - next: threshold 0.294, hit rate recent 0.3709 / long run 0.3161
    - 6h: 20 calls (83 a day), hit rate 0.500, chance 0.070, lift 7.19x
    - 24h: 71 calls (72 a day), hit rate 0.380, chance 0.069, lift 5.47x
    - 7d: 479 calls (69 a day), hit rate 0.315, chance 0.074, lift 4.28x
    - 30d: 2171 calls (72 a day), hit rate 0.306, chance 0.077, lift 3.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.446; 0.35: 87, 0.496; 0.40: 61, 0.551; 0.45: 41, 0.602; 0.50: 26, 0.657; 0.55: 15, 0.700; 0.60: 7, 0.746; 0.65: 2, 0.824
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.318; 0.35: 14, 0.352; 0.40: 2, 0.420; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.355 | -0.15% | 0.883 | 0.550 | 0.242 | 0.633 | 0.328 |
| 6h | 13.122 | 0.80% | 0.883 | 0.494 | 0.249 | 0.472 | 0.437 |
| 24h | 13.667 | 4.72% | 0.892 | 0.495 | 0.250 | 0.500 | 0.698 |
| 7d | 15.188 | 3.35% | 0.901 | 0.500 | 0.250 | 0.500 | 0.644 |
| 30d | 13.357 | 4.21% | 0.900 | 0.500 | 0.251 | 0.495 | 0.673 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.336 | 12.472 | 12.444 | 12.375 | 12.301 | 12.395 | 12.488 | 12.373 | 12.378 | 12.355 |
| 6h | 13.229 | 13.275 | 13.214 | 13.181 | 13.514 | 13.280 | 13.107 | 13.074 | 13.113 | 13.122 |
| 24h | 14.344 | 13.897 | 13.730 | 13.758 | 13.949 | 13.846 | 13.693 | 13.598 | 13.649 | 13.667 |
| 7d | 15.713 | 15.339 | 15.268 | 15.205 | 15.463 | 15.341 | 15.177 | 15.151 | 15.160 | 15.188 |
| 30d | 13.944 | 13.484 | 13.441 | 13.380 | 13.598 | 13.550 | 13.353 | 13.334 | 13.332 | 13.357 |

## Next candle

- candle starting 2026-10-25 12:30 UTC, last close 2325.13
- P(up) 0.4661, return quantiles (bp): {'05': -9.488, '10': -6.856, '25': -3.478, '40': -1.639, '50': -0.489, '60': 0.974, '75': 3.287, '90': 5.98, '95': 8.183}
- changepoint probability 0.0847, regime age 33.5 min
- agent weights: empirical 0.015, ewma 0.058, garch 0.117, har 0.137, bocpd 0.017, hmm 0.032, online_qr 0.237, lgbm 0.386

## Learning log

- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- HMM volatility states (sd, bp per minute): [3.72, 6.8, 19.68], current probabilities: [0.6, 0.394, 0.006]
- live generator: {'versions': 60, 'latest_effective': '2026-10-25 12:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.458, 'l_abs': 0.693, 'l_hi': 0.765, 'l_lo': 0.768, 'b05': 0.722, 'b25': 0.694, 'b75': 0.664, 'b95': 0.695}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.46, 1.722, 2.032, 2.466, 2.818, 2.872, 3.202, 3.686, 3.523, 3.702, 3.723, 3.73, 3.727, 3.789]}
- calibration offsets (in sigma): {'05': 0.0045, '10': -0.041, '25': -0.0375, '40': -0.104, '50': -0.095, '60': -0.066, '75': -0.0225, '90': -0.109, '95': -0.0645}
