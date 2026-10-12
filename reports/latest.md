# ETH-USD 60s candle generator - report

- generated: 2026-10-12 17:49 UTC
- last closed candle: 2026-10-12 17:49 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.453 (95) | 0.482 (670) [0.439, 0.525] | 0.508 (2874) [0.487, 0.527] | 0.510 (3834) [0.493, 0.526] | 0.505 (862) [0.462, 0.548] | 0.592 (71) | 0.500 | flat -0.045 (noise 0.036) |
| colour_clear | 0.531 (718) | 0.541 (5407) [0.533, 0.549] | 0.511 (23135) [0.503, 0.519] | 0.507 (31040) [0.500, 0.513] | 0.543 (6802) [0.536, 0.550] | 0.557 (612) | 0.500 | up +0.034 (noise 0.012) |
| colour_confident | 0.602 (196) | 0.602 (1076) [0.569, 0.646] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.600 (50) | 0.500 | flat -0.017 (noise 0.030) |
| colour_next | 0.529 (1419) | 0.527 (9960) [0.520, 0.535] | 0.509 (42822) [0.504, 0.515] | 0.507 (57130) [0.502, 0.511] | 0.529 (12781) [0.522, 0.536] | 0.539 (1064) | 0.500 | flat +0.015 (noise 0.008) |
| colour_path | 0.499 (19866) | 0.499 (139440) [0.496, 0.502] | 0.501 (599508) [0.500, 0.502] | 0.500 (799820) [0.499, 0.501] | 0.499 (178934) [0.496, 0.502] | 0.503 (14896) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.661 (65) | 0.660 (282) [0.605, 0.725] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 0.700 (10) | 0.500 | flat +0.007 (noise 0.053) |
| reversal_k13_next | 0.373 (67) | 0.329 (492) [0.312, 0.347] | 0.314 (2061) [0.300, 0.331] | 0.308 (2785) [0.295, 0.321] | 0.332 (680) [0.319, 0.346] | 0.275 (51) | 0.077 | flat +0.040 (noise 0.028) |
| reversal_k13_now | 0.588 (51) | 0.573 (386) [0.546, 0.601] | 0.585 (1499) [0.564, 0.609] | 0.584 (1968) [0.566, 0.602] | 0.593 (496) [0.562, 0.632] | 0.553 (38) | 0.077 | flat -0.012 (noise 0.036) |
| reversal_k3_next | 0.605 (86) | 0.592 (519) [0.557, 0.624] | 0.589 (2389) [0.574, 0.604] | 0.586 (3227) [0.574, 0.599] | 0.582 (787) [0.556, 0.609] | 0.561 (41) | 0.294 | flat +0.002 (noise 0.028) |
| reversal_k3_now | 0.914 (70) | 0.922 (424) [0.913, 0.934] | 0.938 (1738) [0.930, 0.946] | 0.937 (2308) [0.930, 0.944] | 0.923 (545) [0.915, 0.932] | 0.958 (48) | 0.294 | flat -0.019 (noise 0.018) |
| reversal_k5_next | 0.492 (61) | 0.470 (421) [0.438, 0.500] | 0.485 (2076) [0.467, 0.504] | 0.484 (2720) [0.468, 0.501] | 0.456 (730) [0.430, 0.489] | 0.508 (63) | 0.188 | flat +0.013 (noise 0.030) |
| reversal_k5_now | 0.840 (50) | 0.816 (369) [0.787, 0.845] | 0.837 (1601) [0.822, 0.852] | 0.835 (2109) [0.821, 0.848] | 0.827 (498) [0.800, 0.853] | 0.875 (40) | 0.188 | flat -0.038 (noise 0.027) |
| reversal_k8_next | 0.357 (84) | 0.380 (610) [0.357, 0.404] | 0.406 (2114) [0.388, 0.426] | 0.394 (2880) [0.381, 0.410] | 0.390 (774) [0.367, 0.415] | 0.411 (56) | 0.122 | flat -0.020 (noise 0.031) |
| reversal_k8_now | 0.683 (60) | 0.684 (418) [0.648, 0.724] | 0.721 (1600) [0.700, 0.741] | 0.712 (2115) [0.694, 0.729] | 0.705 (528) [0.667, 0.742] | 0.691 (42) | 0.122 | flat -0.045 (noise 0.033) |
| overall | 0.503 (21909) | 0.503 (153709) [0.499, 0.506] | 0.504 (660282) [0.502, 0.505] | 0.503 (880896) [0.502, 0.504] | 0.503 (197615) [0.500, 0.506] | 0.508 (16410) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08029, 0.122] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5264, 'levels': [{'threshold': 0.08029, 'calls_per_day': 144.4, 'win_rate': 0.5934}, {'threshold': 0.122, 'calls_per_day': 36.0, 'win_rate': 0.6588}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 12711, 'rate': 0.5315}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15237 | 0.331 | 0.520 (14960) | 0.596 (1143) | 0.778 (2496) |
| volatility: normal | 15236 | 0.358 | 0.509 (15167) | 0.625 (245) | 0.780 (2193) |
| volatility: wild | 15236 | 0.374 | 0.499 (15191) | 0.695 (82) | 0.774 (2093) |
| session: Asia 00-08 | 15360 | 0.352 | 0.513 (15241) | 0.602 (530) | 0.773 (2223) |
| session: Europe 08-13 | 9600 | 0.347 | 0.506 (9508) | 0.590 (361) | 0.777 (1509) |
| session: US 13-21 | 15169 | 0.364 | 0.506 (15060) | 0.591 (372) | 0.783 (2240) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5509) | 0.671 (207) | 0.773 (810) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.374 | 0.378 | 0.309 | 0.309 | 0.483 | 0.235 | 0.512 | 1.062 |
| 6h | 360 | 0.370 | 0.378 | 0.280 | 0.333 | 0.538 | 0.258 | 0.482 | 1.127 |
| 24h | 1440 | 0.362 | 0.352 | 0.273 | 0.304 | 0.532 | 0.260 | 0.465 | 1.157 |
| 7d | 10080 | 0.354 | 0.346 | 0.272 | 0.300 | 0.526 | 0.258 | 0.449 | 1.226 |
| 30d | 43200 | 0.355 | 0.353 | 0.277 | 0.306 | 0.510 | 0.248 | 0.462 | 1.302 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.374 / 0.483 / 0.883; 2: 0.379 / 0.550 / 0.917; 3: 0.351 / 0.400 / 0.900; 4: 0.353 / 0.433 / 0.900; 5: 0.380 / 0.483 / 0.967; 6: 0.390 / 0.517 / 0.967; 7: 0.364 / 0.500 / 0.933; 8: 0.351 / 0.383 / 0.900; 9: 0.392 / 0.533 / 0.950; 10: 0.361 / 0.483 / 0.867; 11: 0.375 / 0.467 / 0.983; 12: 0.361 / 0.483 / 0.767; 13: 0.383 / 0.517 / 0.817; 14: 0.378 / 0.500 / 0.867; 15: 0.349 / 0.350 / 0.917
- 6h: 1: 0.370 / 0.538 / 0.903; 2: 0.363 / 0.513 / 0.944; 3: 0.366 / 0.507 / 0.944; 4: 0.349 / 0.460 / 0.956; 5: 0.361 / 0.490 / 0.972; 6: 0.368 / 0.501 / 0.975; 7: 0.361 / 0.507 / 0.969; 8: 0.357 / 0.479 / 0.958; 9: 0.360 / 0.496 / 0.983; 10: 0.359 / 0.507 / 0.969; 11: 0.365 / 0.496 / 0.992; 12: 0.361 / 0.526 / 0.947; 13: 0.362 / 0.510 / 0.958; 14: 0.357 / 0.487 / 0.969; 15: 0.362 / 0.476 / 0.983
- 24h: 1: 0.362 / 0.532 / 0.908; 2: 0.352 / 0.504 / 0.912; 3: 0.359 / 0.529 / 0.919; 4: 0.341 / 0.466 / 0.915; 5: 0.355 / 0.505 / 0.925; 6: 0.349 / 0.489 / 0.922; 7: 0.352 / 0.508 / 0.921; 8: 0.350 / 0.495 / 0.922; 9: 0.350 / 0.515 / 0.917; 10: 0.355 / 0.527 / 0.916; 11: 0.345 / 0.492 / 0.913; 12: 0.353 / 0.528 / 0.922; 13: 0.345 / 0.492 / 0.922; 14: 0.344 / 0.496 / 0.924; 15: 0.349 / 0.493 / 0.920
- 7d: 1: 0.354 / 0.526 / 0.900; 2: 0.343 / 0.496 / 0.900; 3: 0.345 / 0.510 / 0.902; 4: 0.341 / 0.496 / 0.901; 5: 0.343 / 0.505 / 0.902; 6: 0.339 / 0.493 / 0.901; 7: 0.339 / 0.498 / 0.902; 8: 0.339 / 0.495 / 0.900; 9: 0.337 / 0.491 / 0.900; 10: 0.341 / 0.506 / 0.902; 11: 0.338 / 0.494 / 0.900; 12: 0.339 / 0.498 / 0.900; 13: 0.340 / 0.503 / 0.900; 14: 0.338 / 0.502 / 0.900; 15: 0.339 / 0.496 / 0.900
- 30d: 1: 0.355 / 0.510 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.351 / 0.510 / 0.900; 4: 0.347 / 0.498 / 0.900; 5: 0.348 / 0.505 / 0.901; 6: 0.347 / 0.501 / 0.900; 7: 0.347 / 0.504 / 0.900; 8: 0.346 / 0.502 / 0.900; 9: 0.343 / 0.495 / 0.900; 10: 0.345 / 0.505 / 0.900; 11: 0.344 / 0.500 / 0.900; 12: 0.345 / 0.503 / 0.900; 13: 0.344 / 0.502 / 0.900; 14: 0.343 / 0.497 / 0.900; 15: 0.343 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.119 (body 0.069, range 0.168); 'price stays where it was' would score 0.114; colour right 0.450; typical miss of the close 10.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.128 (body 0.076, range 0.180); 'price stays where it was' would score 0.144; colour right 0.474; typical miss of the close 10.5 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.124 (body 0.083, range 0.166); 'price stays where it was' would score 0.130; colour right 0.493; typical miss of the close 7.9 bp; chain ended on the right side 0.547 of 95 chains; n=1440
- 7d: match 0.119 (body 0.081, range 0.157); 'price stays where it was' would score 0.126; colour right 0.496; typical miss of the close 6.4 bp; chain ended on the right side 0.496 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.124; colour right 0.498; typical miss of the close 7.7 bp; chain ended on the right side 0.512 of 2874 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 3.9; 2: 0.198 / 4.3; 3: 0.164 / 5.9; 4: 0.132 / 6.5; 5: 0.119 / 7.1; 6: 0.109 / 7.6; 7: 0.101 / 8.1; 8: 0.093 / 8.4; 9: 0.087 / 8.6; 10: 0.082 / 9.3; 11: 0.076 / 9.9; 12: 0.074 / 10.4; 13: 0.063 / 10.7; 14: 0.065 / 10.8; 15: 0.060 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 101623, probability skill vs chance 0.2341, widened contest next: False
  - now: threshold 0.8391, hit rate recent 0.9438 / long run 0.9316
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.297, naive rule 0.537, lift 3.36x
    - 24h: 57 calls (57 a day), hit rate 0.965, chance 0.287, naive rule 0.499, lift 3.36x
    - 7d: 438 calls (63 a day), hit rate 0.922, chance 0.299, naive rule 0.502, lift 3.09x
    - 30d: 1730 calls (58 a day), hit rate 0.940, chance 0.292, naive rule 0.484, lift 3.22x
  - next: threshold 0.5349, hit rate recent 0.6002 / long run 0.5864
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.297, lift 2.07x
    - 24h: 50 calls (50 a day), hit rate 0.620, chance 0.287, lift 2.16x
    - 7d: 522 calls (75 a day), hit rate 0.584, chance 0.299, lift 1.96x
    - 30d: 2364 calls (79 a day), hit rate 0.588, chance 0.292, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.493; 0.35: 538, 0.517; 0.40: 485, 0.564; 0.45: 416, 0.631; 0.50: 363, 0.685; 0.55: 319, 0.726; 0.60: 272, 0.769; 0.65: 224, 0.802; 0.70: 180, 0.834; 0.75: 139, 0.873; 0.80: 97, 0.913; 0.85: 49, 0.950; 0.90: 3, 0.976
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 498, 0.460; 0.40: 412, 0.489; 0.45: 316, 0.524; 0.50: 206, 0.559; 0.55: 91, 0.584; 0.60: 14, 0.603; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 101621, probability skill vs chance 0.2262, widened contest next: False
  - now: threshold 0.6876, hit rate recent 0.8621 / long run 0.8358
    - 6h: 16 calls (65 a day), hit rate 0.812, chance 0.154, naive rule 0.362, lift 5.26x
    - 24h: 48 calls (48 a day), hit rate 0.896, chance 0.189, naive rule 0.429, lift 4.74x
    - 7d: 379 calls (54 a day), hit rate 0.818, chance 0.193, naive rule 0.410, lift 4.25x
    - 30d: 1594 calls (53 a day), hit rate 0.838, chance 0.187, naive rule 0.393, lift 4.47x
  - next: threshold 0.436, hit rate recent 0.4958 / long run 0.4768
    - 6h: 27 calls (110 a day), hit rate 0.519, chance 0.154, lift 3.36x
    - 24h: 73 calls (73 a day), hit rate 0.534, chance 0.189, lift 2.83x
    - 7d: 454 calls (65 a day), hit rate 0.469, chance 0.193, lift 2.44x
    - 30d: 2082 calls (69 a day), hit rate 0.485, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 426, 0.417; 0.35: 360, 0.476; 0.40: 290, 0.546; 0.45: 237, 0.604; 0.50: 184, 0.659; 0.55: 140, 0.705; 0.60: 110, 0.748; 0.65: 84, 0.794; 0.70: 62, 0.826; 0.75: 34, 0.868; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 252, 0.426; 0.40: 163, 0.455; 0.45: 82, 0.477; 0.50: 20, 0.519; 0.55: 2, 0.534
- **K=8**: model 1791417600, labels learned 101618, probability skill vs chance 0.2162, widened contest next: False
  - now: threshold 0.5839, hit rate recent 0.6999 / long run 0.7076
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.116, naive rule 0.338, lift 5.56x
    - 24h: 55 calls (55 a day), hit rate 0.691, chance 0.124, naive rule 0.369, lift 5.57x
    - 7d: 414 calls (59 a day), hit rate 0.679, chance 0.123, naive rule 0.345, lift 5.50x
    - 30d: 1595 calls (53 a day), hit rate 0.720, chance 0.122, naive rule 0.330, lift 5.90x
  - next: threshold 0.3681, hit rate recent 0.3958 / long run 0.3949
    - 6h: 20 calls (82 a day), hit rate 0.400, chance 0.116, lift 3.46x
    - 24h: 71 calls (71 a day), hit rate 0.423, chance 0.124, lift 3.40x
    - 7d: 605 calls (87 a day), hit rate 0.388, chance 0.123, lift 3.15x
    - 30d: 2120 calls (71 a day), hit rate 0.406, chance 0.122, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 266, 0.410; 0.35: 200, 0.485; 0.40: 154, 0.544; 0.45: 121, 0.590; 0.50: 92, 0.637; 0.55: 67, 0.689; 0.60: 46, 0.731; 0.65: 25, 0.777; 0.70: 9, 0.826; 0.75: 1, 0.850
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 182, 0.351; 0.35: 111, 0.388; 0.40: 47, 0.417; 0.45: 10, 0.449; 0.50: 1, 0.357
- **K=13**: model 1791504000, labels learned 101613, probability skill vs chance 0.1839, widened contest next: False
  - now: threshold 0.4355, hit rate recent 0.5814 / long run 0.5853
    - 6h: 11 calls (46 a day), hit rate 0.545, chance 0.074, naive rule 0.287, lift 7.38x
    - 24h: 47 calls (47 a day), hit rate 0.574, chance 0.078, naive rule 0.302, lift 7.41x
    - 7d: 371 calls (53 a day), hit rate 0.574, chance 0.078, naive rule 0.282, lift 7.34x
    - 30d: 1491 calls (50 a day), hit rate 0.587, chance 0.078, naive rule 0.271, lift 7.55x
  - next: threshold 0.2873, hit rate recent 0.3147 / long run 0.3187
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.074, lift 4.23x
    - 24h: 60 calls (61 a day), hit rate 0.300, chance 0.078, lift 3.87x
    - 7d: 487 calls (70 a day), hit rate 0.329, chance 0.078, lift 4.20x
    - 30d: 2080 calls (69 a day), hit rate 0.313, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.449; 0.35: 86, 0.510; 0.40: 61, 0.559; 0.45: 42, 0.617; 0.50: 26, 0.644; 0.55: 14, 0.699; 0.60: 5, 0.741; 0.65: 1, 0.762
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.328; 0.35: 14, 0.347; 0.40: 3, 0.338; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.840 | -0.77% | 0.883 | 0.483 | 0.249 | 0.550 | 0.244 |
| 6h | 17.212 | 3.52% | 0.903 | 0.528 | 0.250 | 0.535 | 0.484 |
| 24h | 13.596 | 3.08% | 0.902 | 0.493 | 0.251 | 0.475 | 0.497 |
| 7d | 11.485 | 4.69% | 0.900 | 0.499 | 0.251 | 0.490 | 0.656 |
| 30d | 13.719 | 4.11% | 0.900 | 0.500 | 0.251 | 0.497 | 0.691 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.726 | 14.900 | 15.026 | 14.829 | 14.912 | 14.986 | 14.974 | 14.965 | 14.893 | 14.840 |
| 6h | 17.839 | 17.368 | 17.409 | 17.269 | 17.513 | 17.532 | 17.193 | 17.157 | 17.187 | 17.212 |
| 24h | 14.028 | 13.750 | 13.737 | 13.625 | 13.822 | 13.745 | 13.600 | 13.549 | 13.570 | 13.596 |
| 7d | 12.050 | 11.596 | 11.549 | 11.527 | 11.685 | 11.676 | 11.488 | 11.459 | 11.466 | 11.485 |
| 30d | 14.307 | 13.842 | 13.804 | 13.748 | 13.977 | 13.926 | 13.717 | 13.692 | 13.693 | 13.719 |

## Next candle

- candle starting 2026-10-12 17:49 UTC, last close 2507.58
- P(up) 0.4804, return quantiles (bp): {'05': -8.767, '10': -6.89, '25': -3.503, '40': -1.42, '50': -0.221, '60': 0.927, '75': 2.797, '90': 6.122, '95': 7.968}
- changepoint probability 0.0756, regime age 130.5 min
- agent weights: empirical 0.005, ewma 0.072, garch 0.059, har 0.157, bocpd 0.026, hmm 0.033, online_qr 0.247, lgbm 0.401

## Learning log

- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- HMM volatility states (sd, bp per minute): [2.02, 4.61, 13.8], current probabilities: [0.001, 0.971, 0.028]
- live generator: {'versions': 60, 'latest_effective': '2026-10-12 18:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.397, 'l_abs': 0.653, 'l_hi': 0.734, 'l_lo': 0.638, 'b05': 0.681, 'b25': 0.617, 'b75': 0.67, 'b95': 0.672}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.021, 1.18, 1.449, 1.412, 1.678, 1.745, 1.946, 2.196, 2.463, 2.588, 2.551, 2.407, 2.554, 2.927]}
- calibration offsets (in sigma): {'05': -0.036, '10': -0.092, '25': -0.09, '40': -0.088, '50': -0.07, '60': -0.052, '75': -0.05, '90': 0.002, '95': -0.064}
