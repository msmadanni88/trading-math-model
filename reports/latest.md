# ETH-USD 60s candle generator - report

- generated: 2026-10-13 04:08 UTC
- last closed candle: 2026-10-13 04:08 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k8_now 0.666 in the last 7 days, -0.074 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.495 (671) [0.453, 0.537] | 0.509 (2874) [0.488, 0.531] | 0.510 (3930) [0.494, 0.526] | 0.506 (958) [0.470, 0.545] | 0.375 (16) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.535 (818) | 0.537 (5459) [0.532, 0.543] | 0.512 (23268) [0.504, 0.520] | 0.507 (31858) [0.501, 0.514] | 0.543 (7620) [0.536, 0.549] | 0.538 (117) | 0.500 | flat +0.022 (noise 0.014) |
| colour_confident | 0.574 (61) | 0.589 (1034) [0.561, 0.625] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 1.000 (4) | 0.500 | flat -0.053 (noise 0.033) |
| colour_next | 0.523 (1434) | 0.523 (9964) [0.518, 0.527] | 0.510 (42853) [0.504, 0.515] | 0.507 (58564) [0.503, 0.511] | 0.528 (14215) [0.522, 0.535] | 0.524 (248) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.502 (20076) | 0.498 (139496) [0.496, 0.500] | 0.501 (599942) [0.500, 0.502] | 0.500 (819896) [0.499, 0.501] | 0.499 (199010) [0.497, 0.502] | 0.502 (3472) | 0.500 | flat -0.004 (noise 0.003) |
| colour_strong | 0.667 (15) | 0.652 (282) [0.598, 0.712] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 1.000 (1) | 0.500 | flat -0.017 (noise 0.051) |
| reversal_k13_next | 0.288 (73) | 0.329 (492) [0.312, 0.347] | 0.315 (2092) [0.300, 0.330] | 0.307 (2858) [0.294, 0.321] | 0.328 (753) [0.314, 0.342] | 0.308 (13) | 0.077 | flat +0.038 (noise 0.028) |
| reversal_k13_now | 0.527 (55) | 0.568 (373) [0.540, 0.601] | 0.586 (1493) [0.565, 0.608] | 0.582 (2023) [0.565, 0.601] | 0.586 (551) [0.555, 0.622] | 0.875 (8) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.581 (74) | 0.585 (544) [0.553, 0.613] | 0.588 (2388) [0.573, 0.603] | 0.586 (3301) [0.574, 0.599] | 0.582 (861) [0.559, 0.606] | 0.615 (26) | 0.294 | flat -0.005 (noise 0.029) |
| reversal_k3_now | 0.914 (58) | 0.917 (434) [0.910, 0.926] | 0.939 (1726) [0.931, 0.947] | 0.937 (2366) [0.929, 0.944] | 0.922 (603) [0.915, 0.930] | 1.000 (7) | 0.293 | flat -0.023 (noise 0.018) |
| reversal_k5_next | 0.483 (87) | 0.467 (469) [0.439, 0.491] | 0.483 (2085) [0.466, 0.502] | 0.484 (2807) [0.469, 0.500] | 0.459 (817) [0.435, 0.487] | 0.545 (11) | 0.188 | flat +0.001 (noise 0.030) |
| reversal_k5_now | 0.774 (53) | 0.804 (377) [0.777, 0.832] | 0.834 (1588) [0.819, 0.851] | 0.834 (2162) [0.820, 0.847] | 0.822 (551) [0.796, 0.848] | 0.889 (9) | 0.188 | flat -0.050 (noise 0.027) |
| reversal_k8_next | 0.430 (79) | 0.389 (615) [0.365, 0.415] | 0.409 (2131) [0.393, 0.426] | 0.395 (2959) [0.382, 0.410] | 0.394 (853) [0.373, 0.417] | 0.533 (15) | 0.122 | flat -0.011 (noise 0.030) |
| reversal_k8_now | 0.643 (56) | 0.666 (413) [0.636, 0.698] | 0.718 (1592) [0.698, 0.739] | 0.710 (2171) [0.692, 0.727] | 0.699 (584) [0.663, 0.733] | 0.750 (8) | 0.122 | down -0.074 (noise 0.033) |
| overall | 0.505 (22141) | 0.502 (153848) [0.499, 0.504] | 0.504 (660764) [0.503, 0.505] | 0.503 (903037) [0.502, 0.504] | 0.503 (219756) [0.500, 0.506] | 0.507 (3833) | - | flat -0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07991, 0.1222] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5229, 'levels': [{'threshold': 0.07991, 'calls_per_day': 141.8, 'win_rate': 0.5886}, {'threshold': 0.1222, 'calls_per_day': 36.0, 'win_rate': 0.6588}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 13328, 'rate': 0.5299}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14963 | 0.331 | 0.521 (14689) | 0.596 (1147) | 0.773 (2465) |
| volatility: normal | 14962 | 0.358 | 0.508 (14894) | 0.624 (250) | 0.781 (2150) |
| volatility: wild | 14963 | 0.374 | 0.500 (14921) | 0.693 (88) | 0.772 (2077) |
| session: Asia 00-08 | 15128 | 0.351 | 0.513 (15012) | 0.605 (534) | 0.775 (2199) |
| session: Europe 08-13 | 9300 | 0.347 | 0.507 (9210) | 0.590 (361) | 0.779 (1456) |
| session: US 13-21 | 14880 | 0.363 | 0.507 (14772) | 0.591 (379) | 0.779 (2213) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5510) | 0.663 (211) | 0.757 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.388 | 0.394 | 0.278 | 0.278 | 0.500 | 0.277 | 0.498 | 1.256 |
| 6h | 360 | 0.368 | 0.370 | 0.297 | 0.320 | 0.506 | 0.241 | 0.494 | 1.283 |
| 24h | 1440 | 0.363 | 0.359 | 0.282 | 0.309 | 0.516 | 0.252 | 0.474 | 1.103 |
| 7d | 10080 | 0.353 | 0.346 | 0.273 | 0.300 | 0.523 | 0.255 | 0.451 | 1.236 |
| 30d | 43200 | 0.356 | 0.354 | 0.278 | 0.307 | 0.510 | 0.248 | 0.463 | 1.296 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.388 / 0.500 / 0.950; 2: 0.388 / 0.500 / 0.967; 3: 0.395 / 0.583 / 0.967; 4: 0.382 / 0.517 / 0.967; 5: 0.364 / 0.450 / 1.000; 6: 0.367 / 0.583 / 1.000; 7: 0.347 / 0.450 / 1.000; 8: 0.353 / 0.417 / 1.000; 9: 0.354 / 0.533 / 1.000; 10: 0.360 / 0.517 / 0.983; 11: 0.351 / 0.550 / 0.967; 12: 0.360 / 0.483 / 0.983; 13: 0.330 / 0.433 / 1.000; 14: 0.353 / 0.567 / 1.000; 15: 0.342 / 0.467 / 1.000
- 6h: 1: 0.368 / 0.506 / 0.922; 2: 0.366 / 0.525 / 0.914; 3: 0.369 / 0.517 / 0.911; 4: 0.366 / 0.514 / 0.908; 5: 0.356 / 0.450 / 0.925; 6: 0.367 / 0.542 / 0.936; 7: 0.358 / 0.472 / 0.919; 8: 0.350 / 0.486 / 0.919; 9: 0.341 / 0.450 / 0.931; 10: 0.357 / 0.506 / 0.933; 11: 0.350 / 0.478 / 0.928; 12: 0.361 / 0.500 / 0.911; 13: 0.352 / 0.517 / 0.889; 14: 0.354 / 0.522 / 0.892; 15: 0.358 / 0.519 / 0.911
- 24h: 1: 0.363 / 0.516 / 0.912; 2: 0.356 / 0.503 / 0.899; 3: 0.361 / 0.518 / 0.892; 4: 0.349 / 0.485 / 0.896; 5: 0.356 / 0.487 / 0.891; 6: 0.356 / 0.506 / 0.892; 7: 0.356 / 0.501 / 0.883; 8: 0.352 / 0.492 / 0.886; 9: 0.350 / 0.492 / 0.887; 10: 0.355 / 0.517 / 0.888; 11: 0.350 / 0.481 / 0.885; 12: 0.357 / 0.522 / 0.882; 13: 0.347 / 0.494 / 0.876; 14: 0.351 / 0.510 / 0.876; 15: 0.353 / 0.490 / 0.877
- 7d: 1: 0.353 / 0.523 / 0.900; 2: 0.343 / 0.498 / 0.900; 3: 0.345 / 0.511 / 0.899; 4: 0.341 / 0.496 / 0.899; 5: 0.343 / 0.502 / 0.898; 6: 0.340 / 0.497 / 0.899; 7: 0.339 / 0.495 / 0.898; 8: 0.339 / 0.497 / 0.899; 9: 0.336 / 0.489 / 0.899; 10: 0.341 / 0.505 / 0.900; 11: 0.338 / 0.492 / 0.898; 12: 0.339 / 0.498 / 0.898; 13: 0.339 / 0.502 / 0.897; 14: 0.338 / 0.503 / 0.897; 15: 0.338 / 0.495 / 0.898
- 30d: 1: 0.356 / 0.510 / 0.899; 2: 0.351 / 0.498 / 0.900; 3: 0.352 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.349 / 0.504 / 0.900; 6: 0.348 / 0.502 / 0.900; 7: 0.348 / 0.504 / 0.899; 8: 0.347 / 0.503 / 0.899; 9: 0.344 / 0.495 / 0.899; 10: 0.346 / 0.505 / 0.899; 11: 0.345 / 0.501 / 0.899; 12: 0.346 / 0.504 / 0.899; 13: 0.345 / 0.502 / 0.899; 14: 0.344 / 0.497 / 0.899; 15: 0.344 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.103 (body 0.073, range 0.132); 'price stays where it was' would score 0.128; colour right 0.317; typical miss of the close 18.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.091 (body 0.058, range 0.125); 'price stays where it was' would score 0.110; colour right 0.458; typical miss of the close 20.6 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.111 (body 0.073, range 0.148); 'price stays where it was' would score 0.113; colour right 0.483; typical miss of the close 11.2 bp; chain ended on the right side 0.490 of 96 chains; n=1440
- 7d: match 0.118 (body 0.080, range 0.155); 'price stays where it was' would score 0.125; colour right 0.492; typical miss of the close 6.7 bp; chain ended on the right side 0.493 of 671 chains; n=10080
- 30d: match 0.118 (body 0.079, range 0.158); 'price stays where it was' would score 0.124; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.509 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.0; 2: 0.197 / 4.4; 3: 0.163 / 6.0; 4: 0.132 / 6.6; 5: 0.119 / 7.3; 6: 0.107 / 7.9; 7: 0.101 / 8.3; 8: 0.093 / 8.5; 9: 0.086 / 8.7; 10: 0.082 / 9.4; 11: 0.076 / 10.1; 12: 0.073 / 10.6; 13: 0.062 / 10.9; 14: 0.063 / 11.1; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 102242, probability skill vs chance 0.2357, widened contest next: False
  - now: threshold 0.8429, hit rate recent 0.9173 / long run 0.9286
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.296, naive rule 0.540, lift 3.10x
    - 24h: 56 calls (56 a day), hit rate 0.911, chance 0.275, naive rule 0.477, lift 3.31x
    - 7d: 427 calls (61 a day), hit rate 0.918, chance 0.297, naive rule 0.501, lift 3.09x
    - 30d: 1720 calls (57 a day), hit rate 0.938, chance 0.291, naive rule 0.483, lift 3.23x
  - next: threshold 0.5097, hit rate recent 0.6127 / long run 0.5887
    - 6h: 33 calls (134 a day), hit rate 0.636, chance 0.296, lift 2.15x
    - 24h: 90 calls (90 a day), hit rate 0.567, chance 0.275, lift 2.06x
    - 7d: 563 calls (80 a day), hit rate 0.586, chance 0.297, lift 1.97x
    - 30d: 2400 calls (80 a day), hit rate 0.589, chance 0.291, lift 2.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.492; 0.35: 538, 0.515; 0.40: 484, 0.562; 0.45: 416, 0.629; 0.50: 362, 0.683; 0.55: 318, 0.725; 0.60: 271, 0.768; 0.65: 224, 0.801; 0.70: 180, 0.833; 0.75: 139, 0.873; 0.80: 96, 0.912; 0.85: 49, 0.949; 0.90: 3, 0.976
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 497, 0.460; 0.40: 412, 0.488; 0.45: 316, 0.523; 0.50: 206, 0.558; 0.55: 91, 0.584; 0.60: 14, 0.603; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 102240, probability skill vs chance 0.2317, widened contest next: True
  - now: threshold 0.6971, hit rate recent 0.7983 / long run 0.8286
    - 6h: 13 calls (53 a day), hit rate 0.769, chance 0.177, naive rule 0.441, lift 4.34x
    - 24h: 55 calls (55 a day), hit rate 0.764, chance 0.170, naive rule 0.381, lift 4.49x
    - 7d: 376 calls (54 a day), hit rate 0.809, chance 0.191, naive rule 0.409, lift 4.24x
    - 30d: 1585 calls (53 a day), hit rate 0.833, chance 0.187, naive rule 0.392, lift 4.47x
  - next: threshold 0.4357, hit rate recent 0.489 / long run 0.4758
    - 6h: 15 calls (61 a day), hit rate 0.600, chance 0.177, lift 3.39x
    - 24h: 91 calls (91 a day), hit rate 0.462, chance 0.170, lift 2.72x
    - 7d: 471 calls (67 a day), hit rate 0.471, chance 0.191, lift 2.47x
    - 30d: 2075 calls (69 a day), hit rate 0.483, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 426, 0.416; 0.35: 358, 0.476; 0.40: 289, 0.546; 0.45: 236, 0.604; 0.50: 184, 0.658; 0.55: 139, 0.704; 0.60: 109, 0.747; 0.65: 83, 0.792; 0.70: 61, 0.823; 0.75: 34, 0.867; 0.80: 10, 0.892
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.389; 0.35: 252, 0.425; 0.40: 163, 0.453; 0.45: 81, 0.474; 0.50: 19, 0.517; 0.55: 2, 0.544
- **K=8**: model 1791849600, labels learned 102237, probability skill vs chance 0.22, widened contest next: True
  - now: threshold 0.5872, hit rate recent 0.6664 / long run 0.7034
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.110, naive rule 0.355, lift 5.30x
    - 24h: 53 calls (53 a day), hit rate 0.642, chance 0.114, naive rule 0.330, lift 5.61x
    - 7d: 407 calls (58 a day), hit rate 0.673, chance 0.123, naive rule 0.346, lift 5.48x
    - 30d: 1593 calls (53 a day), hit rate 0.717, chance 0.122, naive rule 0.329, lift 5.88x
  - next: threshold 0.3699, hit rate recent 0.4424 / long run 0.4014
    - 6h: 20 calls (82 a day), hit rate 0.500, chance 0.110, lift 4.55x
    - 24h: 86 calls (87 a day), hit rate 0.430, chance 0.114, lift 3.76x
    - 7d: 613 calls (88 a day), hit rate 0.393, chance 0.123, lift 3.20x
    - 30d: 2126 calls (71 a day), hit rate 0.410, chance 0.122, lift 3.36x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 265, 0.409; 0.35: 200, 0.485; 0.40: 154, 0.544; 0.45: 121, 0.590; 0.50: 92, 0.636; 0.55: 66, 0.687; 0.60: 45, 0.729; 0.65: 24, 0.774; 0.70: 9, 0.827; 0.75: 1, 0.850
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 182, 0.351; 0.35: 111, 0.389; 0.40: 47, 0.420; 0.45: 10, 0.447; 0.50: 1, 0.357
- **K=13**: model 1791849600, labels learned 102232, probability skill vs chance 0.1873, widened contest next: False
  - now: threshold 0.4362, hit rate recent 0.5919 / long run 0.5859
    - 6h: 13 calls (54 a day), hit rate 0.615, chance 0.046, naive rule 0.229, lift 13.27x
    - 24h: 52 calls (53 a day), hit rate 0.577, chance 0.070, naive rule 0.270, lift 8.22x
    - 7d: 366 calls (52 a day), hit rate 0.585, chance 0.078, naive rule 0.284, lift 7.46x
    - 30d: 1493 calls (50 a day), hit rate 0.587, chance 0.077, naive rule 0.270, lift 7.59x
  - next: threshold 0.2925, hit rate recent 0.3152 / long run 0.3184
    - 6h: 19 calls (79 a day), hit rate 0.263, chance 0.046, lift 5.67x
    - 24h: 78 calls (79 a day), hit rate 0.282, chance 0.070, lift 4.02x
    - 7d: 494 calls (71 a day), hit rate 0.332, chance 0.078, lift 4.24x
    - 30d: 2094 calls (70 a day), hit rate 0.314, chance 0.077, lift 4.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.447; 0.35: 86, 0.508; 0.40: 61, 0.559; 0.45: 42, 0.615; 0.50: 26, 0.642; 0.55: 14, 0.698; 0.60: 5, 0.739; 0.65: 1, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.328; 0.35: 14, 0.349; 0.40: 3, 0.333; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 18.682 | 2.95% | 0.917 | 0.483 | 0.245 | 0.583 | 0.581 |
| 6h | 24.572 | 4.64% | 0.908 | 0.539 | 0.249 | 0.528 | 0.522 |
| 24h | 17.001 | 3.39% | 0.906 | 0.510 | 0.250 | 0.504 | 0.593 |
| 7d | 12.224 | 4.55% | 0.900 | 0.501 | 0.251 | 0.492 | 0.660 |
| 30d | 13.897 | 4.13% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 19.249 | 19.129 | 18.764 | 19.132 | 19.239 | 18.631 | 18.826 | 18.666 | 18.750 | 18.682 |
| 6h | 25.769 | 24.775 | 24.717 | 24.641 | 25.283 | 24.856 | 24.766 | 24.526 | 24.567 | 24.572 |
| 24h | 17.597 | 17.135 | 17.126 | 17.032 | 17.349 | 17.182 | 17.053 | 16.955 | 16.980 | 17.001 |
| 7d | 12.807 | 12.341 | 12.293 | 12.260 | 12.450 | 12.417 | 12.236 | 12.197 | 12.205 | 12.224 |
| 30d | 14.496 | 14.022 | 13.982 | 13.925 | 14.159 | 14.100 | 13.897 | 13.870 | 13.871 | 13.897 |

## Next candle

- candle starting 2026-10-13 04:08 UTC, last close 2505.56
- P(up) 0.5385, return quantiles (bp): {'05': -10.744, '10': -7.517, '25': -3.006, '40': -0.777, '50': 0.468, '60': 1.68, '75': 3.68, '90': 7.108, '95': 9.178}
- changepoint probability 0.0584, regime age 32.7 min
- agent weights: empirical 0.003, ewma 0.069, garch 0.090, har 0.196, bocpd 0.006, hmm 0.061, online_qr 0.127, lgbm 0.449

## Learning log

- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.01, 4.48, 12.03], current probabilities: [0.096, 0.875, 0.029]
- live generator: {'versions': 60, 'latest_effective': '2026-10-13 04:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.293, 'l_abs': 0.692, 'l_hi': 0.752, 'l_lo': 0.648, 'b05': 0.693, 'b25': 0.639, 'b75': 0.707, 'b95': 0.686}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6]], 'cone_width': [1.496, 2.197, 2.347, 2.965, 2.829, 3.971, 3.849, 3.776, 3.909, 4.632, 5.576, 6.962, 6.955, 6.398]}
- calibration offsets (in sigma): {'05': -0.0165, '10': 0.047, '25': 0.1075, '40': 0.088, '50': 0.075, '60': 0.062, '75': 0.0125, '90': -0.077, '95': -0.1035}
