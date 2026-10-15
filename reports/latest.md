# ETH-USD 60s candle generator - report

- generated: 2026-10-15 02:15 UTC
- last closed candle: 2026-10-15 02:15 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.505 (671) [0.479, 0.535] | 0.513 (2875) [0.493, 0.531] | 0.510 (4122) [0.494, 0.525] | 0.506 (1150) [0.475, 0.538] | 0.333 (9) | 0.500 | flat -0.004 (noise 0.035) |
| colour_clear | 0.559 (843) | 0.541 (5560) [0.534, 0.549] | 0.515 (23376) [0.507, 0.523] | 0.509 (33481) [0.503, 0.515] | 0.543 (9243) [0.536, 0.549] | 0.522 (92) | 0.500 | flat +0.015 (noise 0.013) |
| colour_confident | 0.537 (67) | 0.599 (882) [0.574, 0.634] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.603 (1608) [0.577, 0.631] | 0.600 (10) | 0.500 | flat -0.010 (noise 0.033) |
| colour_next | 0.542 (1436) | 0.526 (9976) [0.520, 0.532] | 0.511 (42873) [0.506, 0.517] | 0.508 (61433) [0.504, 0.512] | 0.528 (17084) [0.522, 0.534] | 0.496 (135) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.503 (20104) | 0.501 (139664) [0.500, 0.502] | 0.501 (600222) [0.500, 0.502] | 0.501 (860062) [0.499, 0.502] | 0.500 (239176) [0.498, 0.502] | 0.504 (1890) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.462 (13) | 0.657 (233) [0.603, 0.720] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 0.653 (432) [0.615, 0.694] | 1.000 (2) | 0.500 | flat +0.009 (noise 0.051) |
| reversal_k13_next | 0.244 (45) | 0.316 (471) [0.290, 0.342] | 0.314 (2053) [0.299, 0.330] | 0.305 (2977) [0.293, 0.319] | 0.319 (872) [0.303, 0.334] | 0.571 (7) | 0.077 | flat +0.005 (noise 0.029) |
| reversal_k13_now | 0.548 (42) | 0.593 (346) [0.566, 0.621] | 0.587 (1480) [0.567, 0.609] | 0.583 (2108) [0.567, 0.601] | 0.588 (636) [0.559, 0.621] | 1.000 (3) | 0.077 | flat +0.004 (noise 0.036) |
| reversal_k3_next | 0.591 (66) | 0.574 (676) [0.552, 0.598] | 0.583 (2477) [0.569, 0.599] | 0.584 (3532) [0.572, 0.597] | 0.576 (1092) [0.557, 0.599] | 0.556 (9) | 0.293 | flat -0.011 (noise 0.028) |
| reversal_k3_now | 0.980 (49) | 0.929 (423) [0.915, 0.947] | 0.939 (1723) [0.931, 0.947] | 0.938 (2459) [0.931, 0.945] | 0.930 (696) [0.919, 0.941] | 0.833 (6) | 0.293 | flat -0.001 (noise 0.018) |
| reversal_k5_next | 0.543 (94) | 0.489 (564) [0.469, 0.510] | 0.489 (2146) [0.472, 0.507] | 0.485 (3005) [0.471, 0.501] | 0.469 (1015) [0.445, 0.495] | 0.545 (11) | 0.187 | flat +0.027 (noise 0.028) |
| reversal_k5_now | 0.849 (33) | 0.811 (354) [0.785, 0.839] | 0.831 (1577) [0.815, 0.846] | 0.833 (2241) [0.820, 0.846] | 0.822 (630) [0.799, 0.844] | 0.800 (5) | 0.188 | flat -0.030 (noise 0.028) |
| reversal_k8_next | 0.386 (57) | 0.398 (571) [0.379, 0.418] | 0.410 (2107) [0.394, 0.429] | 0.396 (3097) [0.382, 0.410] | 0.395 (991) [0.376, 0.414] | 0.636 (11) | 0.122 | flat +0.000 (noise 0.030) |
| reversal_k8_now | 0.725 (40) | 0.674 (374) [0.640, 0.712] | 0.714 (1578) [0.693, 0.735] | 0.709 (2257) [0.693, 0.726] | 0.699 (670) [0.668, 0.730] | 0.750 (4) | 0.122 | flat -0.052 (noise 0.033) |
| overall | 0.507 (22062) | 0.504 (154090) [0.503, 0.506] | 0.504 (661111) [0.502, 0.505] | 0.503 (947293) [0.502, 0.504] | 0.504 (264012) [0.501, 0.506] | 0.507 (2090) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07564, 0.1171] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5252, 'levels': [{'threshold': 0.07564, 'calls_per_day': 140.7, 'win_rate': 0.596}, {'threshold': 0.1171, 'calls_per_day': 34.9, 'win_rate': 0.6599}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 16082, 'rate': 0.5293}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14925 | 0.336 | 0.520 (14692) | 0.601 (1231) | 0.776 (2421) |
| volatility: normal | 14925 | 0.362 | 0.511 (14863) | 0.582 (280) | 0.779 (2076) |
| volatility: wild | 14925 | 0.374 | 0.501 (14884) | 0.682 (107) | 0.774 (2066) |
| session: Asia 00-08 | 15015 | 0.355 | 0.516 (14918) | 0.605 (585) | 0.776 (2164) |
| session: Europe 08-13 | 9300 | 0.351 | 0.509 (9220) | 0.582 (407) | 0.783 (1425) |
| session: US 13-21 | 14880 | 0.367 | 0.507 (14785) | 0.583 (396) | 0.781 (2160) |
| session: late 21-24 | 5580 | 0.350 | 0.510 (5516) | 0.670 (230) | 0.753 (814) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.367 | 0.395 | 0.295 | 0.295 | 0.483 | 0.258 | 0.477 | 1.103 |
| 6h | 360 | 0.360 | 0.375 | 0.293 | 0.343 | 0.508 | 0.250 | 0.469 | 1.144 |
| 24h | 1440 | 0.376 | 0.368 | 0.295 | 0.342 | 0.531 | 0.270 | 0.482 | 1.153 |
| 7d | 10080 | 0.357 | 0.350 | 0.274 | 0.304 | 0.525 | 0.258 | 0.456 | 1.242 |
| 30d | 43200 | 0.357 | 0.355 | 0.280 | 0.309 | 0.511 | 0.250 | 0.465 | 1.291 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.367 / 0.483 / 0.900; 2: 0.350 / 0.467 / 0.917; 3: 0.346 / 0.483 / 0.933; 4: 0.401 / 0.583 / 0.967; 5: 0.336 / 0.450 / 0.950; 6: 0.343 / 0.500 / 0.983; 7: 0.354 / 0.450 / 0.950; 8: 0.334 / 0.433 / 0.950; 9: 0.381 / 0.550 / 0.917; 10: 0.331 / 0.500 / 0.967; 11: 0.373 / 0.550 / 1.000; 12: 0.322 / 0.450 / 0.933; 13: 0.364 / 0.567 / 0.967; 14: 0.324 / 0.467 / 0.983; 15: 0.364 / 0.583 / 0.950
- 6h: 1: 0.360 / 0.508 / 0.889; 2: 0.355 / 0.489 / 0.886; 3: 0.352 / 0.492 / 0.903; 4: 0.366 / 0.533 / 0.894; 5: 0.347 / 0.492 / 0.897; 6: 0.348 / 0.483 / 0.894; 7: 0.364 / 0.553 / 0.903; 8: 0.338 / 0.447 / 0.894; 9: 0.358 / 0.497 / 0.906; 10: 0.339 / 0.475 / 0.900; 11: 0.358 / 0.522 / 0.914; 12: 0.338 / 0.450 / 0.908; 13: 0.358 / 0.542 / 0.917; 14: 0.336 / 0.469 / 0.908; 15: 0.369 / 0.561 / 0.892
- 24h: 1: 0.376 / 0.531 / 0.906; 2: 0.361 / 0.491 / 0.899; 3: 0.365 / 0.503 / 0.899; 4: 0.369 / 0.506 / 0.903; 5: 0.363 / 0.505 / 0.903; 6: 0.367 / 0.513 / 0.910; 7: 0.363 / 0.508 / 0.907; 8: 0.357 / 0.474 / 0.912; 9: 0.369 / 0.499 / 0.910; 10: 0.363 / 0.503 / 0.913; 11: 0.366 / 0.513 / 0.918; 12: 0.356 / 0.478 / 0.919; 13: 0.365 / 0.521 / 0.920; 14: 0.359 / 0.490 / 0.926; 15: 0.371 / 0.535 / 0.924
- 7d: 1: 0.357 / 0.525 / 0.901; 2: 0.346 / 0.496 / 0.900; 3: 0.349 / 0.511 / 0.900; 4: 0.346 / 0.498 / 0.900; 5: 0.348 / 0.508 / 0.900; 6: 0.346 / 0.501 / 0.901; 7: 0.345 / 0.502 / 0.902; 8: 0.344 / 0.499 / 0.901; 9: 0.344 / 0.494 / 0.901; 10: 0.346 / 0.506 / 0.901; 11: 0.343 / 0.494 / 0.902; 12: 0.344 / 0.500 / 0.902; 13: 0.344 / 0.502 / 0.902; 14: 0.342 / 0.501 / 0.902; 15: 0.346 / 0.504 / 0.902
- 30d: 1: 0.357 / 0.511 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.505 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.502 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.093 (body 0.063, range 0.122); 'price stays where it was' would score 0.094; colour right 0.500; typical miss of the close 17.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.124 (body 0.083, range 0.165); 'price stays where it was' would score 0.128; colour right 0.472; typical miss of the close 12.6 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.133; colour right 0.490; typical miss of the close 11.3 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.160); 'price stays where it was' would score 0.126; colour right 0.496; typical miss of the close 7.4 bp; chain ended on the right side 0.502 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.512 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.197 / 4.5; 3: 0.164 / 6.1; 4: 0.132 / 6.7; 5: 0.120 / 7.4; 6: 0.108 / 8.0; 7: 0.101 / 8.3; 8: 0.095 / 8.7; 9: 0.086 / 8.8; 10: 0.082 / 9.6; 11: 0.078 / 10.3; 12: 0.074 / 10.7; 13: 0.062 / 10.9; 14: 0.065 / 11.1; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 105009, probability skill vs chance 0.2343, widened contest next: False
  - now: threshold 0.8422, hit rate recent 0.948 / long run 0.934
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.301, naive rule 0.507, lift 3.04x
    - 24h: 53 calls (53 a day), hit rate 0.962, chance 0.294, naive rule 0.493, lift 3.27x
    - 7d: 419 calls (60 a day), hit rate 0.926, chance 0.296, naive rule 0.500, lift 3.12x
    - 30d: 1721 calls (57 a day), hit rate 0.940, chance 0.291, naive rule 0.482, lift 3.23x
  - next: threshold 0.5511, hit rate recent 0.5689 / long run 0.5769
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.301, lift 1.81x
    - 24h: 63 calls (63 a day), hit rate 0.556, chance 0.294, lift 1.89x
    - 7d: 676 calls (97 a day), hit rate 0.574, chance 0.296, lift 1.94x
    - 30d: 2481 calls (83 a day), hit rate 0.584, chance 0.291, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.491; 0.35: 539, 0.513; 0.40: 484, 0.562; 0.45: 415, 0.631; 0.50: 362, 0.685; 0.55: 317, 0.728; 0.60: 271, 0.772; 0.65: 224, 0.802; 0.70: 180, 0.834; 0.75: 139, 0.872; 0.80: 96, 0.913; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 497, 0.460; 0.40: 410, 0.490; 0.45: 315, 0.526; 0.50: 205, 0.560; 0.55: 92, 0.582; 0.60: 14, 0.601; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 105007, probability skill vs chance 0.2224, widened contest next: False
  - now: threshold 0.7012, hit rate recent 0.8218 / long run 0.8271
    - 6h: 9 calls (37 a day), hit rate 0.889, chance 0.212, naive rule 0.479, lift 4.18x
    - 24h: 37 calls (37 a day), hit rate 0.865, chance 0.199, naive rule 0.433, lift 4.35x
    - 7d: 349 calls (50 a day), hit rate 0.811, chance 0.190, naive rule 0.411, lift 4.27x
    - 30d: 1576 calls (53 a day), hit rate 0.831, chance 0.187, naive rule 0.393, lift 4.44x
  - next: threshold 0.425, hit rate recent 0.5472 / long run 0.4865
    - 6h: 16 calls (65 a day), hit rate 0.500, chance 0.212, lift 2.35x
    - 24h: 100 calls (100 a day), hit rate 0.560, chance 0.199, lift 2.82x
    - 7d: 565 calls (81 a day), hit rate 0.488, chance 0.190, lift 2.57x
    - 30d: 2150 calls (72 a day), hit rate 0.488, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 424, 0.419; 0.35: 355, 0.481; 0.40: 286, 0.553; 0.45: 234, 0.609; 0.50: 182, 0.663; 0.55: 139, 0.708; 0.60: 109, 0.749; 0.65: 82, 0.791; 0.70: 60, 0.822; 0.75: 33, 0.864; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.390; 0.35: 251, 0.426; 0.40: 162, 0.456; 0.45: 79, 0.476; 0.50: 18, 0.513; 0.55: 2, 0.569
- **K=8**: model 1791936000, labels learned 105004, probability skill vs chance 0.2178, widened contest next: False
  - now: threshold 0.5841, hit rate recent 0.7012 / long run 0.7025
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.124, naive rule 0.404, lift 7.04x
    - 24h: 39 calls (39 a day), hit rate 0.769, chance 0.124, naive rule 0.358, lift 6.21x
    - 7d: 372 calls (53 a day), hit rate 0.675, chance 0.123, naive rule 0.347, lift 5.46x
    - 30d: 1575 calls (53 a day), hit rate 0.714, chance 0.122, naive rule 0.331, lift 5.83x
  - next: threshold 0.3502, hit rate recent 0.4333 / long run 0.4022
    - 6h: 15 calls (62 a day), hit rate 0.533, chance 0.124, lift 4.29x
    - 24h: 60 calls (60 a day), hit rate 0.433, chance 0.124, lift 3.50x
    - 7d: 572 calls (82 a day), hit rate 0.399, chance 0.123, lift 3.23x
    - 30d: 2112 calls (70 a day), hit rate 0.411, chance 0.122, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 262, 0.416; 0.35: 197, 0.489; 0.40: 152, 0.550; 0.45: 119, 0.593; 0.50: 91, 0.635; 0.55: 66, 0.685; 0.60: 45, 0.726; 0.65: 24, 0.778; 0.70: 9, 0.832; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 180, 0.353; 0.35: 109, 0.390; 0.40: 45, 0.424; 0.45: 9, 0.466; 0.50: 1, 0.371
- **K=13**: model 1792022400, labels learned 104999, probability skill vs chance 0.1896, widened contest next: False
  - now: threshold 0.4229, hit rate recent 0.5979 / long run 0.5862
    - 6h: 7 calls (29 a day), hit rate 1.000, chance 0.083, naive rule 0.353, lift 12.11x
    - 24h: 40 calls (40 a day), hit rate 0.600, chance 0.077, naive rule 0.289, lift 7.81x
    - 7d: 344 calls (49 a day), hit rate 0.596, chance 0.079, naive rule 0.289, lift 7.54x
    - 30d: 1479 calls (49 a day), hit rate 0.588, chance 0.078, naive rule 0.272, lift 7.56x
  - next: threshold 0.301, hit rate recent 0.2977 / long run 0.3111
    - 6h: 9 calls (38 a day), hit rate 0.556, chance 0.083, lift 6.73x
    - 24h: 43 calls (43 a day), hit rate 0.302, chance 0.077, lift 3.93x
    - 7d: 470 calls (67 a day), hit rate 0.319, chance 0.079, lift 4.04x
    - 30d: 2055 calls (69 a day), hit rate 0.315, chance 0.078, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.513; 0.40: 61, 0.564; 0.45: 41, 0.616; 0.50: 25, 0.651; 0.55: 14, 0.707; 0.60: 4, 0.762; 0.65: 1, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.328; 0.35: 13, 0.371; 0.40: 2, 0.429; 0.45: 0, 0.375

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.758 | 5.75% | 0.867 | 0.467 | 0.242 | 0.600 | 0.040 |
| 6h | 19.789 | 2.51% | 0.864 | 0.481 | 0.247 | 0.558 | 0.398 |
| 24h | 17.908 | 4.14% | 0.897 | 0.500 | 0.250 | 0.492 | 0.558 |
| 7d | 13.592 | 4.32% | 0.900 | 0.499 | 0.251 | 0.494 | 0.679 |
| 30d | 14.031 | 4.06% | 0.900 | 0.500 | 0.251 | 0.496 | 0.686 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 27.329 | 26.196 | 26.066 | 26.250 | 26.278 | 26.365 | 25.872 | 26.062 | 25.999 | 25.758 |
| 6h | 20.298 | 19.953 | 19.961 | 19.872 | 20.206 | 20.101 | 19.831 | 19.836 | 19.820 | 19.789 |
| 24h | 18.682 | 18.018 | 18.061 | 17.901 | 18.200 | 18.160 | 17.912 | 17.907 | 17.891 | 17.908 |
| 7d | 14.206 | 13.708 | 13.692 | 13.618 | 13.853 | 13.802 | 13.595 | 13.561 | 13.572 | 13.592 |
| 30d | 14.625 | 14.154 | 14.116 | 14.056 | 14.292 | 14.223 | 14.030 | 14.003 | 14.005 | 14.031 |

## Next candle

- candle starting 2026-10-15 02:15 UTC, last close 2403.72
- P(up) 0.4583, return quantiles (bp): {'05': -15.85, '10': -11.637, '25': -7.159, '40': -3.214, '50': -1.064, '60': 1.522, '75': 6.205, '90': 12.69, '95': 16.039}
- changepoint probability 0.0375, regime age 66.3 min
- agent weights: empirical 0.004, ewma 0.120, garch 0.087, har 0.218, bocpd 0.028, hmm 0.034, online_qr 0.268, lgbm 0.241

## Learning log

- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- 2026-10-15 00:00 UTC: {"garch": {"alpha": 0.1468, "beta": 0.8362}, "hmm": {"sd_bp": [2.09, 5.01, 13.97], "stay": [0.966, 0.968, 0.901]}, "lgbm": {"challenger_loss": 0.24892, "champion_loss": 0.24887, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47837, "challengers": 1, "chance_loss": 0.6018, "widened": false, "champion_loss": 0.47429, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3659, "challengers": 1, "chance_loss": 0.47673, "widened": false, "champion_loss": 0.36443, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27292, "challengers": 1, "chance_loss": 0.37099, "widened": false, "champion_loss": 0.27192, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18834, "challengers": 3, "chance_loss": 0.26708, "widened": true, "champion_loss": 0.18845, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.09, 5.01, 13.97], current probabilities: [0.0, 0.339, 0.661]
- live generator: {'versions': 60, 'latest_effective': '2026-10-15 02:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.378, 'l_abs': 0.698, 'l_hi': 0.714, 'l_lo': 0.719, 'b05': 0.754, 'b25': 0.643, 'b75': 0.715, 'b95': 0.762}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.535, 1.81, 1.933, 2.166, 2.239, 2.375, 2.701, 2.758, 2.972, 2.883, 2.958, 2.848, 3.021, 3.327]}
- calibration offsets (in sigma): {'05': 0.017, '10': -0.006, '25': -0.125, '40': -0.134, '50': -0.14, '60': -0.106, '75': -0.005, '90': 0.066, '95': 0.013}
