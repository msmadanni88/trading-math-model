# ETH-USD 60s candle generator - report

- generated: 2026-10-13 11:45 UTC
- last closed candle: 2026-10-13 11:45 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k8_now 0.666 in the last 7 days, -0.074 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.495 (671) [0.453, 0.537] | 0.509 (2874) [0.488, 0.531] | 0.510 (3930) [0.494, 0.526] | 0.506 (958) [0.470, 0.545] | 0.468 (47) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.535 (818) | 0.537 (5459) [0.532, 0.543] | 0.512 (23268) [0.504, 0.520] | 0.507 (31858) [0.501, 0.514] | 0.543 (7620) [0.536, 0.549] | 0.550 (371) | 0.500 | flat +0.022 (noise 0.014) |
| colour_confident | 0.574 (61) | 0.589 (1034) [0.561, 0.625] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 0.605 (1481) [0.579, 0.634] | 0.667 (30) | 0.500 | flat -0.053 (noise 0.033) |
| colour_next | 0.523 (1434) | 0.523 (9964) [0.518, 0.527] | 0.510 (42853) [0.504, 0.515] | 0.507 (58564) [0.503, 0.511] | 0.528 (14215) [0.522, 0.535] | 0.526 (703) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.502 (20076) | 0.498 (139496) [0.496, 0.500] | 0.501 (599942) [0.500, 0.502] | 0.500 (819896) [0.499, 0.501] | 0.499 (199010) [0.497, 0.502] | 0.503 (9842) | 0.500 | flat -0.004 (noise 0.003) |
| colour_strong | 0.667 (15) | 0.652 (282) [0.598, 0.712] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 0.658 (412) [0.621, 0.703] | 1.000 (4) | 0.500 | flat -0.017 (noise 0.051) |
| reversal_k13_next | 0.288 (73) | 0.329 (492) [0.312, 0.347] | 0.315 (2092) [0.300, 0.330] | 0.307 (2858) [0.294, 0.321] | 0.328 (753) [0.314, 0.342] | 0.256 (43) | 0.077 | flat +0.038 (noise 0.028) |
| reversal_k13_now | 0.527 (55) | 0.568 (373) [0.540, 0.601] | 0.586 (1493) [0.565, 0.608] | 0.582 (2023) [0.565, 0.601] | 0.586 (551) [0.555, 0.622] | 0.727 (22) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.581 (74) | 0.585 (544) [0.553, 0.613] | 0.588 (2388) [0.573, 0.603] | 0.586 (3301) [0.574, 0.599] | 0.582 (861) [0.559, 0.606] | 0.529 (87) | 0.294 | flat -0.005 (noise 0.029) |
| reversal_k3_now | 0.914 (58) | 0.917 (434) [0.910, 0.926] | 0.939 (1726) [0.931, 0.947] | 0.937 (2366) [0.929, 0.944] | 0.922 (603) [0.915, 0.930] | 1.000 (18) | 0.293 | flat -0.023 (noise 0.018) |
| reversal_k5_next | 0.483 (87) | 0.467 (469) [0.439, 0.491] | 0.483 (2085) [0.466, 0.502] | 0.484 (2807) [0.469, 0.500] | 0.459 (817) [0.435, 0.487] | 0.500 (48) | 0.188 | flat +0.001 (noise 0.030) |
| reversal_k5_now | 0.774 (53) | 0.804 (377) [0.777, 0.832] | 0.834 (1588) [0.819, 0.851] | 0.834 (2162) [0.820, 0.847] | 0.822 (551) [0.796, 0.848] | 0.818 (22) | 0.188 | flat -0.050 (noise 0.027) |
| reversal_k8_next | 0.430 (79) | 0.389 (615) [0.365, 0.415] | 0.409 (2131) [0.393, 0.426] | 0.395 (2959) [0.382, 0.410] | 0.394 (853) [0.373, 0.417] | 0.425 (40) | 0.122 | flat -0.011 (noise 0.030) |
| reversal_k8_now | 0.643 (56) | 0.666 (413) [0.636, 0.698] | 0.718 (1592) [0.698, 0.739] | 0.710 (2171) [0.692, 0.727] | 0.699 (584) [0.663, 0.733] | 0.727 (22) | 0.122 | down -0.074 (noise 0.033) |
| overall | 0.505 (22141) | 0.502 (153848) [0.499, 0.504] | 0.504 (660764) [0.503, 0.505] | 0.503 (903037) [0.502, 0.504] | 0.503 (219756) [0.500, 0.506] | 0.506 (10894) | - | flat -0.004 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07929, 0.122] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.523, 'levels': [{'threshold': 0.07929, 'calls_per_day': 141.1, 'win_rate': 0.5906}, {'threshold': 0.122, 'calls_per_day': 35.5, 'win_rate': 0.6574}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 13783, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15115 | 0.331 | 0.520 (14840) | 0.595 (1150) | 0.773 (2480) |
| volatility: normal | 15115 | 0.358 | 0.509 (15047) | 0.620 (263) | 0.783 (2162) |
| volatility: wild | 15115 | 0.374 | 0.501 (15072) | 0.704 (98) | 0.770 (2102) |
| session: Asia 00-08 | 15360 | 0.352 | 0.514 (15243) | 0.606 (548) | 0.774 (2234) |
| session: Europe 08-13 | 9525 | 0.347 | 0.507 (9434) | 0.590 (373) | 0.780 (1473) |
| session: US 13-21 | 14880 | 0.363 | 0.507 (14772) | 0.591 (379) | 0.779 (2213) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5510) | 0.663 (211) | 0.757 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.341 | 0.347 | 0.300 | 0.300 | 0.467 | 0.217 | 0.466 | 1.172 |
| 6h | 360 | 0.367 | 0.369 | 0.289 | 0.303 | 0.518 | 0.262 | 0.472 | 1.142 |
| 24h | 1440 | 0.367 | 0.366 | 0.287 | 0.314 | 0.517 | 0.255 | 0.478 | 1.200 |
| 7d | 10080 | 0.354 | 0.347 | 0.273 | 0.300 | 0.522 | 0.256 | 0.452 | 1.250 |
| 30d | 43200 | 0.357 | 0.354 | 0.279 | 0.308 | 0.510 | 0.249 | 0.464 | 1.292 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.341 / 0.467 / 0.883; 2: 0.342 / 0.417 / 0.883; 3: 0.366 / 0.550 / 0.933; 4: 0.385 / 0.600 / 0.933; 5: 0.322 / 0.367 / 0.933; 6: 0.380 / 0.550 / 0.917; 7: 0.372 / 0.567 / 0.917; 8: 0.361 / 0.467 / 0.883; 9: 0.370 / 0.533 / 0.867; 10: 0.353 / 0.450 / 0.850; 11: 0.354 / 0.483 / 0.867; 12: 0.373 / 0.517 / 0.917; 13: 0.392 / 0.617 / 0.983; 14: 0.383 / 0.600 / 0.967; 15: 0.380 / 0.517 / 0.950
- 6h: 1: 0.367 / 0.518 / 0.917; 2: 0.346 / 0.435 / 0.906; 3: 0.380 / 0.557 / 0.936; 4: 0.372 / 0.543 / 0.936; 5: 0.362 / 0.501 / 0.947; 6: 0.370 / 0.518 / 0.925; 7: 0.363 / 0.513 / 0.958; 8: 0.363 / 0.504 / 0.947; 9: 0.361 / 0.515 / 0.933; 10: 0.346 / 0.443 / 0.933; 11: 0.347 / 0.468 / 0.944; 12: 0.354 / 0.487 / 0.964; 13: 0.365 / 0.501 / 0.992; 14: 0.350 / 0.474 / 0.986; 15: 0.361 / 0.476 / 0.975
- 24h: 1: 0.367 / 0.517 / 0.915; 2: 0.358 / 0.502 / 0.901; 3: 0.366 / 0.522 / 0.902; 4: 0.356 / 0.501 / 0.911; 5: 0.357 / 0.483 / 0.910; 6: 0.365 / 0.523 / 0.912; 7: 0.359 / 0.499 / 0.910; 8: 0.356 / 0.499 / 0.909; 9: 0.354 / 0.495 / 0.917; 10: 0.353 / 0.494 / 0.915; 11: 0.352 / 0.481 / 0.920; 12: 0.358 / 0.513 / 0.908; 13: 0.355 / 0.501 / 0.908; 14: 0.351 / 0.498 / 0.911; 15: 0.357 / 0.493 / 0.919
- 7d: 1: 0.354 / 0.522 / 0.900; 2: 0.344 / 0.496 / 0.900; 3: 0.347 / 0.514 / 0.900; 4: 0.342 / 0.497 / 0.901; 5: 0.344 / 0.503 / 0.901; 6: 0.342 / 0.497 / 0.901; 7: 0.341 / 0.497 / 0.901; 8: 0.341 / 0.497 / 0.900; 9: 0.338 / 0.492 / 0.900; 10: 0.342 / 0.504 / 0.902; 11: 0.339 / 0.491 / 0.901; 12: 0.340 / 0.499 / 0.901; 13: 0.340 / 0.499 / 0.901; 14: 0.339 / 0.505 / 0.901; 15: 0.340 / 0.495 / 0.901
- 30d: 1: 0.357 / 0.510 / 0.899; 2: 0.351 / 0.498 / 0.900; 3: 0.353 / 0.511 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.495 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.345 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.155 (body 0.116, range 0.195); 'price stays where it was' would score 0.120; colour right 0.533; typical miss of the close 11.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.124 (body 0.091, range 0.157); 'price stays where it was' would score 0.104; colour right 0.501; typical miss of the close 10.8 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.113 (body 0.076, range 0.150); 'price stays where it was' would score 0.115; colour right 0.487; typical miss of the close 11.8 bp; chain ended on the right side 0.448 of 96 chains; n=1440
- 7d: match 0.118 (body 0.081, range 0.156); 'price stays where it was' would score 0.124; colour right 0.494; typical miss of the close 6.9 bp; chain ended on the right side 0.490 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.124; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.510 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.0; 2: 0.198 / 4.4; 3: 0.164 / 6.0; 4: 0.133 / 6.7; 5: 0.119 / 7.4; 6: 0.107 / 7.9; 7: 0.101 / 8.4; 8: 0.093 / 8.6; 9: 0.086 / 8.8; 10: 0.082 / 9.5; 11: 0.077 / 10.2; 12: 0.074 / 10.7; 13: 0.062 / 10.9; 14: 0.063 / 11.1; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 102699, probability skill vs chance 0.2308, widened contest next: True
  - now: threshold 0.8431, hit rate recent 0.9313 / long run 0.9299
    - 6h: 7 calls (28 a day), hit rate 1.000, chance 0.286, naive rule 0.453, lift 3.50x
    - 24h: 43 calls (43 a day), hit rate 0.930, chance 0.285, naive rule 0.492, lift 3.26x
    - 7d: 420 calls (60 a day), hit rate 0.926, chance 0.296, naive rule 0.500, lift 3.13x
    - 30d: 1716 calls (57 a day), hit rate 0.939, chance 0.290, naive rule 0.481, lift 3.23x
  - next: threshold 0.5051, hit rate recent 0.5213 / long run 0.5792
    - 6h: 52 calls (211 a day), hit rate 0.481, chance 0.286, lift 1.68x
    - 24h: 133 calls (133 a day), hit rate 0.556, chance 0.285, lift 1.95x
    - 7d: 616 calls (88 a day), hit rate 0.576, chance 0.296, lift 1.94x
    - 30d: 2443 calls (81 a day), hit rate 0.586, chance 0.290, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.491; 0.35: 539, 0.514; 0.40: 485, 0.561; 0.45: 416, 0.628; 0.50: 363, 0.682; 0.55: 319, 0.724; 0.60: 271, 0.767; 0.65: 224, 0.800; 0.70: 180, 0.832; 0.75: 139, 0.872; 0.80: 96, 0.913; 0.85: 49, 0.949; 0.90: 3, 0.976
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.459; 0.40: 412, 0.488; 0.45: 316, 0.523; 0.50: 206, 0.557; 0.55: 91, 0.584; 0.60: 14, 0.603; 0.65: 1, 0.667
- **K=5**: model 1791590400, labels learned 102697, probability skill vs chance 0.2301, widened contest next: True
  - now: threshold 0.7032, hit rate recent 0.7954 / long run 0.8274
    - 6h: 7 calls (29 a day), hit rate 1.000, chance 0.190, naive rule 0.400, lift 5.27x
    - 24h: 51 calls (51 a day), hit rate 0.725, chance 0.175, naive rule 0.392, lift 4.14x
    - 7d: 375 calls (54 a day), hit rate 0.813, chance 0.190, naive rule 0.408, lift 4.28x
    - 30d: 1585 calls (53 a day), hit rate 0.833, chance 0.187, naive rule 0.392, lift 4.46x
  - next: threshold 0.4356, hit rate recent 0.4864 / long run 0.4765
    - 6h: 32 calls (131 a day), hit rate 0.500, chance 0.190, lift 2.63x
    - 24h: 99 calls (99 a day), hit rate 0.485, chance 0.175, lift 2.77x
    - 7d: 496 calls (71 a day), hit rate 0.472, chance 0.190, lift 2.48x
    - 30d: 2093 calls (70 a day), hit rate 0.484, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 426, 0.416; 0.35: 358, 0.476; 0.40: 289, 0.546; 0.45: 236, 0.604; 0.50: 184, 0.658; 0.55: 140, 0.705; 0.60: 109, 0.748; 0.65: 83, 0.792; 0.70: 61, 0.823; 0.75: 33, 0.867; 0.80: 10, 0.896
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 252, 0.426; 0.40: 163, 0.454; 0.45: 80, 0.475; 0.50: 19, 0.518; 0.55: 2, 0.554
- **K=8**: model 1791849600, labels learned 102694, probability skill vs chance 0.2214, widened contest next: False
  - now: threshold 0.5708, hit rate recent 0.6787 / long run 0.7037
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.120, naive rule 0.322, lift 7.29x
    - 24h: 50 calls (50 a day), hit rate 0.640, chance 0.120, naive rule 0.339, lift 5.35x
    - 7d: 403 calls (58 a day), hit rate 0.672, chance 0.122, naive rule 0.343, lift 5.50x
    - 30d: 1589 calls (53 a day), hit rate 0.719, chance 0.122, naive rule 0.329, lift 5.89x
  - next: threshold 0.3703, hit rate recent 0.4161 / long run 0.3997
    - 6h: 22 calls (91 a day), hit rate 0.364, chance 0.120, lift 3.03x
    - 24h: 83 calls (84 a day), hit rate 0.434, chance 0.120, lift 3.63x
    - 7d: 613 calls (88 a day), hit rate 0.388, chance 0.122, lift 3.18x
    - 30d: 2121 calls (71 a day), hit rate 0.411, chance 0.122, lift 3.37x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 264, 0.410; 0.35: 200, 0.485; 0.40: 154, 0.545; 0.45: 121, 0.591; 0.50: 92, 0.636; 0.55: 66, 0.688; 0.60: 45, 0.731; 0.65: 24, 0.778; 0.70: 9, 0.835; 0.75: 1, 0.842
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 182, 0.353; 0.35: 110, 0.391; 0.40: 47, 0.422; 0.45: 10, 0.456; 0.50: 1, 0.375
- **K=13**: model 1791849600, labels learned 102689, probability skill vs chance 0.1914, widened contest next: False
  - now: threshold 0.4366, hit rate recent 0.6062 / long run 0.5873
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.077, naive rule 0.278, lift 11.39x
    - 24h: 50 calls (51 a day), hit rate 0.600, chance 0.072, naive rule 0.275, lift 8.30x
    - 7d: 366 calls (52 a day), hit rate 0.585, chance 0.078, naive rule 0.282, lift 7.51x
    - 30d: 1492 calls (50 a day), hit rate 0.590, chance 0.078, naive rule 0.271, lift 7.61x
  - next: threshold 0.2956, hit rate recent 0.286 / long run 0.3143
    - 6h: 24 calls (100 a day), hit rate 0.250, chance 0.077, lift 3.25x
    - 24h: 81 calls (82 a day), hit rate 0.284, chance 0.072, lift 3.93x
    - 7d: 502 calls (72 a day), hit rate 0.323, chance 0.078, lift 4.14x
    - 30d: 2106 calls (70 a day), hit rate 0.314, chance 0.078, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.448; 0.35: 86, 0.509; 0.40: 61, 0.562; 0.45: 42, 0.619; 0.50: 26, 0.649; 0.55: 14, 0.708; 0.60: 5, 0.763; 0.65: 1, 0.826
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.328; 0.35: 14, 0.357; 0.40: 2, 0.368; 0.45: 0, 0.300

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.735 | 1.16% | 0.867 | 0.583 | 0.250 | 0.533 | 0.469 |
| 6h | 15.716 | 1.85% | 0.894 | 0.467 | 0.250 | 0.524 | 0.534 |
| 24h | 17.722 | 3.33% | 0.903 | 0.503 | 0.250 | 0.520 | 0.587 |
| 7d | 12.538 | 4.45% | 0.900 | 0.498 | 0.251 | 0.494 | 0.661 |
| 30d | 13.961 | 4.08% | 0.900 | 0.500 | 0.251 | 0.497 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.036 | 25.860 | 26.262 | 25.498 | 27.728 | 26.077 | 25.508 | 25.582 | 25.595 | 25.735 |
| 6h | 16.013 | 15.948 | 15.905 | 15.731 | 16.181 | 15.855 | 15.711 | 15.706 | 15.707 | 15.716 |
| 24h | 18.333 | 17.912 | 17.891 | 17.757 | 18.181 | 17.901 | 17.752 | 17.677 | 17.698 | 17.722 |
| 7d | 13.123 | 12.661 | 12.615 | 12.576 | 12.774 | 12.730 | 12.545 | 12.508 | 12.517 | 12.538 |
| 30d | 14.554 | 14.085 | 14.047 | 13.988 | 14.222 | 14.159 | 13.959 | 13.933 | 13.934 | 13.961 |

## Next candle

- candle starting 2026-10-13 11:45 UTC, last close 2504.7
- P(up) 0.4755, return quantiles (bp): {'05': -14.194, '10': -11.017, '25': -6.15, '40': -2.726, '50': -0.504, '60': 1.593, '75': 5.615, '90': 10.364, '95': 13.287}
- changepoint probability 0.2256, regime age 19.4 min
- agent weights: empirical 0.007, ewma 0.047, garch 0.052, har 0.207, bocpd 0.006, hmm 0.077, online_qr 0.227, lgbm 0.376

## Learning log

- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- HMM volatility states (sd, bp per minute): [2.01, 4.48, 12.03], current probabilities: [0.064, 0.825, 0.111]
- live generator: {'versions': 60, 'latest_effective': '2026-10-13 11:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.347, 'l_abs': 0.739, 'l_hi': 0.753, 'l_lo': 0.708, 'b05': 0.74, 'b25': 0.666, 'b75': 0.761, 'b95': 0.697}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.3, 'ahead': [[1.3, 1.8], [1.4, 1.6], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.8], [1.2, 1.8], [1.3, 1.8], [1.2, 1.8], [1.2, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.308, 1.482, 1.583, 1.773, 2.026, 2.192, 2.302, 2.446, 2.636, 2.826, 2.899, 2.964, 3.082, 3.133]}
- calibration offsets (in sigma): {'05': -0.008, '10': -0.036, '25': -0.09, '40': -0.094, '50': -0.07, '60': -0.036, '75': -0.0, '90': -0.024, '95': -0.082}
