# ETH-USD 60s candle generator - report

- generated: 2026-10-12 08:04 UTC
- last closed candle: 2026-10-12 08:04 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.453 (95) | 0.482 (670) [0.439, 0.525] | 0.508 (2874) [0.487, 0.527] | 0.510 (3834) [0.493, 0.526] | 0.505 (862) [0.462, 0.548] | 0.625 (32) | 0.500 | flat -0.045 (noise 0.036) |
| colour_clear | 0.531 (718) | 0.541 (5407) [0.533, 0.549] | 0.511 (23135) [0.503, 0.519] | 0.507 (31040) [0.500, 0.513] | 0.543 (6802) [0.536, 0.550] | 0.571 (280) | 0.500 | up +0.034 (noise 0.012) |
| colour_confident | 0.602 (196) | 0.602 (1076) [0.569, 0.646] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.643 (28) | 0.500 | flat -0.017 (noise 0.030) |
| colour_next | 0.529 (1419) | 0.527 (9960) [0.520, 0.535] | 0.509 (42822) [0.504, 0.515] | 0.507 (57130) [0.502, 0.511] | 0.529 (12781) [0.522, 0.536] | 0.548 (480) | 0.500 | flat +0.015 (noise 0.008) |
| colour_path | 0.499 (19866) | 0.499 (139440) [0.496, 0.502] | 0.501 (599508) [0.500, 0.502] | 0.500 (799820) [0.499, 0.501] | 0.499 (178934) [0.496, 0.502] | 0.503 (6720) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.661 (65) | 0.660 (282) [0.605, 0.725] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 0.833 (6) | 0.500 | flat +0.007 (noise 0.053) |
| reversal_k13_next | 0.373 (67) | 0.329 (492) [0.312, 0.347] | 0.314 (2061) [0.300, 0.331] | 0.308 (2785) [0.295, 0.321] | 0.332 (680) [0.319, 0.346] | 0.333 (21) | 0.077 | flat +0.040 (noise 0.028) |
| reversal_k13_now | 0.588 (51) | 0.573 (386) [0.546, 0.601] | 0.585 (1499) [0.564, 0.609] | 0.584 (1968) [0.566, 0.602] | 0.593 (496) [0.562, 0.632] | 0.524 (21) | 0.077 | flat -0.012 (noise 0.036) |
| reversal_k3_next | 0.605 (86) | 0.592 (519) [0.557, 0.624] | 0.589 (2389) [0.574, 0.604] | 0.586 (3227) [0.574, 0.599] | 0.582 (787) [0.556, 0.609] | 0.722 (18) | 0.294 | flat +0.002 (noise 0.028) |
| reversal_k3_now | 0.914 (70) | 0.922 (424) [0.913, 0.934] | 0.938 (1738) [0.930, 0.946] | 0.937 (2308) [0.930, 0.944] | 0.923 (545) [0.915, 0.932] | 0.947 (19) | 0.294 | flat -0.019 (noise 0.018) |
| reversal_k5_next | 0.492 (61) | 0.470 (421) [0.438, 0.500] | 0.485 (2076) [0.467, 0.504] | 0.484 (2720) [0.468, 0.501] | 0.456 (730) [0.430, 0.489] | 0.556 (18) | 0.188 | flat +0.013 (noise 0.030) |
| reversal_k5_now | 0.840 (50) | 0.816 (369) [0.787, 0.845] | 0.837 (1601) [0.822, 0.852] | 0.835 (2109) [0.821, 0.848] | 0.827 (498) [0.800, 0.853] | 0.929 (14) | 0.188 | flat -0.038 (noise 0.027) |
| reversal_k8_next | 0.357 (84) | 0.380 (610) [0.357, 0.404] | 0.406 (2114) [0.388, 0.426] | 0.394 (2880) [0.381, 0.410] | 0.390 (774) [0.367, 0.415] | 0.524 (21) | 0.122 | flat -0.020 (noise 0.031) |
| reversal_k8_now | 0.683 (60) | 0.684 (418) [0.648, 0.724] | 0.721 (1600) [0.700, 0.741] | 0.712 (2115) [0.694, 0.729] | 0.705 (528) [0.667, 0.742] | 0.714 (21) | 0.122 | flat -0.045 (noise 0.033) |
| overall | 0.503 (21909) | 0.503 (153709) [0.499, 0.506] | 0.504 (660282) [0.502, 0.505] | 0.503 (880896) [0.502, 0.504] | 0.503 (197615) [0.500, 0.506] | 0.509 (7385) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08015, 0.1219] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5271, 'levels': [{'threshold': 0.08015, 'calls_per_day': 143.0, 'win_rate': 0.5943}, {'threshold': 0.1219, 'calls_per_day': 35.9, 'win_rate': 0.6654}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 12127, 'rate': 0.5315}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15042 | 0.331 | 0.521 (14766) | 0.597 (1140) | 0.778 (2477) |
| volatility: normal | 15041 | 0.358 | 0.507 (14971) | 0.632 (228) | 0.778 (2148) |
| volatility: wild | 15041 | 0.374 | 0.499 (14997) | 0.688 (80) | 0.775 (2064) |
| session: Asia 00-08 | 15360 | 0.352 | 0.513 (15241) | 0.602 (530) | 0.773 (2223) |
| session: Europe 08-13 | 9304 | 0.347 | 0.506 (9213) | 0.594 (345) | 0.775 (1465) |
| session: US 13-21 | 14880 | 0.363 | 0.505 (14771) | 0.590 (366) | 0.785 (2191) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5509) | 0.671 (207) | 0.773 (810) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.353 | 0.358 | 0.271 | 0.271 | 0.407 | 0.213 | 0.493 | 1.001 |
| 6h | 360 | 0.367 | 0.344 | 0.275 | 0.290 | 0.542 | 0.265 | 0.469 | 1.218 |
| 24h | 1440 | 0.350 | 0.337 | 0.267 | 0.289 | 0.533 | 0.253 | 0.447 | 1.268 |
| 7d | 10080 | 0.354 | 0.347 | 0.273 | 0.300 | 0.526 | 0.258 | 0.450 | 1.208 |
| 30d | 43200 | 0.354 | 0.352 | 0.276 | 0.305 | 0.510 | 0.248 | 0.460 | 1.306 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.353 / 0.407 / 0.950; 2: 0.358 / 0.390 / 0.917; 3: 0.380 / 0.508 / 0.933; 4: 0.398 / 0.559 / 0.917; 5: 0.364 / 0.492 / 0.933; 6: 0.337 / 0.356 / 0.850; 7: 0.395 / 0.559 / 0.883; 8: 0.353 / 0.441 / 0.900; 9: 0.378 / 0.508 / 0.917; 10: 0.371 / 0.458 / 0.883; 11: 0.366 / 0.441 / 0.867; 12: 0.376 / 0.492 / 0.950; 13: 0.386 / 0.508 / 0.950; 14: 0.350 / 0.441 / 0.900; 15: 0.367 / 0.424 / 0.867
- 6h: 1: 0.367 / 0.542 / 0.925; 2: 0.344 / 0.458 / 0.894; 3: 0.365 / 0.539 / 0.881; 4: 0.344 / 0.478 / 0.875; 5: 0.354 / 0.506 / 0.856; 6: 0.340 / 0.458 / 0.825; 7: 0.358 / 0.522 / 0.842; 8: 0.358 / 0.511 / 0.856; 9: 0.351 / 0.511 / 0.814; 10: 0.358 / 0.531 / 0.825; 11: 0.339 / 0.472 / 0.792; 12: 0.369 / 0.575 / 0.850; 13: 0.346 / 0.478 / 0.836; 14: 0.340 / 0.472 / 0.817; 15: 0.336 / 0.433 / 0.783
- 24h: 1: 0.350 / 0.533 / 0.907; 2: 0.337 / 0.498 / 0.904; 3: 0.341 / 0.515 / 0.899; 4: 0.334 / 0.489 / 0.898; 5: 0.332 / 0.488 / 0.897; 6: 0.331 / 0.476 / 0.895; 7: 0.337 / 0.504 / 0.901; 8: 0.339 / 0.507 / 0.899; 9: 0.337 / 0.512 / 0.897; 10: 0.336 / 0.498 / 0.898; 11: 0.328 / 0.487 / 0.894; 12: 0.338 / 0.519 / 0.899; 13: 0.337 / 0.497 / 0.901; 14: 0.330 / 0.493 / 0.904; 15: 0.332 / 0.493 / 0.907
- 7d: 1: 0.354 / 0.526 / 0.900; 2: 0.344 / 0.498 / 0.900; 3: 0.345 / 0.510 / 0.900; 4: 0.342 / 0.498 / 0.900; 5: 0.342 / 0.505 / 0.899; 6: 0.338 / 0.491 / 0.898; 7: 0.339 / 0.500 / 0.898; 8: 0.339 / 0.494 / 0.899; 9: 0.337 / 0.491 / 0.898; 10: 0.340 / 0.502 / 0.897; 11: 0.337 / 0.494 / 0.897; 12: 0.338 / 0.497 / 0.899; 13: 0.340 / 0.505 / 0.899; 14: 0.337 / 0.500 / 0.898; 15: 0.338 / 0.495 / 0.898
- 30d: 1: 0.354 / 0.510 / 0.898; 2: 0.348 / 0.497 / 0.900; 3: 0.351 / 0.510 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.347 / 0.505 / 0.900; 6: 0.346 / 0.501 / 0.899; 7: 0.346 / 0.504 / 0.899; 8: 0.346 / 0.503 / 0.900; 9: 0.342 / 0.495 / 0.899; 10: 0.345 / 0.504 / 0.899; 11: 0.343 / 0.500 / 0.899; 12: 0.344 / 0.503 / 0.899; 13: 0.344 / 0.501 / 0.899; 14: 0.342 / 0.497 / 0.899; 15: 0.342 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.097 (body 0.073, range 0.121); 'price stays where it was' would score 0.109; colour right 0.441; typical miss of the close 14.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.112 (body 0.079, range 0.144); 'price stays where it was' would score 0.101; colour right 0.486; typical miss of the close 10.4 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.117 (body 0.079, range 0.154); 'price stays where it was' would score 0.131; colour right 0.503; typical miss of the close 6.3 bp; chain ended on the right side 0.463 of 95 chains; n=1440
- 7d: match 0.118 (body 0.081, range 0.155); 'price stays where it was' would score 0.125; colour right 0.499; typical miss of the close 6.4 bp; chain ended on the right side 0.496 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.6 bp; chain ended on the right side 0.510 of 2874 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 3.8; 2: 0.198 / 4.3; 3: 0.165 / 5.8; 4: 0.132 / 6.4; 5: 0.119 / 7.0; 6: 0.109 / 7.6; 7: 0.101 / 8.0; 8: 0.093 / 8.3; 9: 0.086 / 8.5; 10: 0.082 / 9.3; 11: 0.076 / 9.8; 12: 0.075 / 10.3; 13: 0.063 / 10.6; 14: 0.065 / 10.7; 15: 0.060 / 10.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 101038, probability skill vs chance 0.23, widened contest next: False
  - now: threshold 0.8344, hit rate recent 0.9293 / long run 0.9299
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.254, naive rule 0.405, lift 3.68x
    - 24h: 61 calls (61 a day), hit rate 0.934, chance 0.304, naive rule 0.533, lift 3.08x
    - 7d: 424 calls (61 a day), hit rate 0.922, chance 0.300, naive rule 0.503, lift 3.08x
    - 30d: 1733 calls (58 a day), hit rate 0.938, chance 0.292, naive rule 0.485, lift 3.21x
  - next: threshold 0.5698, hit rate recent 0.6706 / long run 0.5923
    - 6h: 13 calls (53 a day), hit rate 0.692, chance 0.254, lift 2.73x
    - 24h: 61 calls (61 a day), hit rate 0.721, chance 0.304, lift 2.37x
    - 7d: 521 calls (74 a day), hit rate 0.595, chance 0.300, lift 1.99x
    - 30d: 2392 calls (80 a day), hit rate 0.589, chance 0.292, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 538, 0.517; 0.40: 485, 0.564; 0.45: 417, 0.631; 0.50: 364, 0.685; 0.55: 319, 0.726; 0.60: 272, 0.769; 0.65: 225, 0.802; 0.70: 181, 0.833; 0.75: 139, 0.873; 0.80: 97, 0.912; 0.85: 49, 0.949; 0.90: 3, 0.975
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 498, 0.460; 0.40: 412, 0.489; 0.45: 317, 0.523; 0.50: 206, 0.557; 0.55: 92, 0.583; 0.60: 14, 0.608; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 101036, probability skill vs chance 0.224, widened contest next: False
  - now: threshold 0.6956, hit rate recent 0.8724 / long run 0.8353
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.174, naive rule 0.366, lift 5.22x
    - 24h: 45 calls (45 a day), hit rate 0.867, chance 0.201, naive rule 0.462, lift 4.31x
    - 7d: 368 calls (53 a day), hit rate 0.821, chance 0.195, naive rule 0.414, lift 4.21x
    - 30d: 1599 calls (53 a day), hit rate 0.839, chance 0.188, naive rule 0.394, lift 4.46x
  - next: threshold 0.4379, hit rate recent 0.5218 / long run 0.476
    - 6h: 16 calls (65 a day), hit rate 0.500, chance 0.174, lift 2.87x
    - 24h: 60 calls (60 a day), hit rate 0.533, chance 0.201, lift 2.65x
    - 7d: 427 calls (61 a day), hit rate 0.475, chance 0.195, lift 2.44x
    - 30d: 2075 calls (69 a day), hit rate 0.485, chance 0.188, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 427, 0.418; 0.35: 361, 0.476; 0.40: 291, 0.546; 0.45: 238, 0.604; 0.50: 185, 0.660; 0.55: 140, 0.707; 0.60: 110, 0.750; 0.65: 84, 0.796; 0.70: 62, 0.828; 0.75: 34, 0.868; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.389; 0.35: 252, 0.427; 0.40: 164, 0.454; 0.45: 82, 0.475; 0.50: 20, 0.517; 0.55: 2, 0.550
- **K=8**: model 1791417600, labels learned 101033, probability skill vs chance 0.214, widened contest next: False
  - now: threshold 0.5804, hit rate recent 0.7187 / long run 0.7091
    - 6h: 14 calls (58 a day), hit rate 0.786, chance 0.113, naive rule 0.319, lift 6.96x
    - 24h: 58 calls (58 a day), hit rate 0.759, chance 0.128, naive rule 0.388, lift 5.93x
    - 7d: 419 calls (60 a day), hit rate 0.685, chance 0.124, naive rule 0.346, lift 5.53x
    - 30d: 1601 calls (53 a day), hit rate 0.721, chance 0.122, naive rule 0.330, lift 5.90x
  - next: threshold 0.3666, hit rate recent 0.4402 / long run 0.3981
    - 6h: 17 calls (70 a day), hit rate 0.529, chance 0.113, lift 4.69x
    - 24h: 75 calls (76 a day), hit rate 0.467, chance 0.128, lift 3.65x
    - 7d: 606 calls (87 a day), hit rate 0.389, chance 0.124, lift 3.14x
    - 30d: 2114 calls (70 a day), hit rate 0.406, chance 0.122, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 266, 0.410; 0.35: 201, 0.485; 0.40: 154, 0.545; 0.45: 122, 0.590; 0.50: 93, 0.636; 0.55: 67, 0.690; 0.60: 46, 0.731; 0.65: 25, 0.778; 0.70: 9, 0.830; 0.75: 1, 0.857
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 182, 0.351; 0.35: 111, 0.388; 0.40: 47, 0.418; 0.45: 10, 0.450; 0.50: 1, 0.390
- **K=13**: model 1791504000, labels learned 101028, probability skill vs chance 0.1844, widened contest next: False
  - now: threshold 0.4359, hit rate recent 0.5817 / long run 0.5852
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.065, naive rule 0.241, lift 8.76x
    - 24h: 51 calls (52 a day), hit rate 0.588, chance 0.077, naive rule 0.310, lift 7.66x
    - 7d: 383 calls (55 a day), hit rate 0.574, chance 0.079, naive rule 0.284, lift 7.30x
    - 30d: 1501 calls (50 a day), hit rate 0.586, chance 0.078, naive rule 0.271, lift 7.54x
  - next: threshold 0.2882, hit rate recent 0.36 / long run 0.323
    - 6h: 16 calls (67 a day), hit rate 0.312, chance 0.065, lift 4.79x
    - 24h: 60 calls (61 a day), hit rate 0.383, chance 0.077, lift 4.99x
    - 7d: 481 calls (69 a day), hit rate 0.335, chance 0.079, lift 4.25x
    - 30d: 2072 calls (69 a day), hit rate 0.313, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.449; 0.35: 86, 0.510; 0.40: 62, 0.557; 0.45: 43, 0.614; 0.50: 26, 0.639; 0.55: 14, 0.696; 0.60: 5, 0.740; 0.65: 1, 0.792
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 14, 0.349; 0.40: 3, 0.325; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.205 | 0.52% | 0.950 | 0.450 | 0.251 | 0.475 | 0.192 |
| 6h | 13.793 | 3.21% | 0.911 | 0.522 | 0.251 | 0.447 | 0.401 |
| 24h | 11.347 | 4.68% | 0.907 | 0.497 | 0.251 | 0.460 | 0.553 |
| 7d | 11.363 | 4.82% | 0.901 | 0.500 | 0.251 | 0.490 | 0.658 |
| 30d | 13.626 | 4.17% | 0.900 | 0.500 | 0.251 | 0.497 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.269 | 12.250 | 12.324 | 12.240 | 12.412 | 12.199 | 12.105 | 12.044 | 12.095 | 12.205 |
| 6h | 14.251 | 13.929 | 13.911 | 13.856 | 14.050 | 13.999 | 13.855 | 13.711 | 13.768 | 13.793 |
| 24h | 11.904 | 11.493 | 11.442 | 11.383 | 11.662 | 11.509 | 11.356 | 11.296 | 11.322 | 11.347 |
| 7d | 11.938 | 11.477 | 11.427 | 11.408 | 11.567 | 11.552 | 11.365 | 11.339 | 11.343 | 11.363 |
| 30d | 14.219 | 13.748 | 13.709 | 13.654 | 13.884 | 13.832 | 13.624 | 13.599 | 13.600 | 13.626 |

## Next candle

- candle starting 2026-10-12 08:04 UTC, last close 2557.0
- P(up) 0.5081, return quantiles (bp): {'05': -9.111, '10': -6.096, '25': -3.269, '40': -1.179, '50': 0.103, '60': 1.301, '75': 3.572, '90': 7.394, '95': 9.08}
- changepoint probability 0.0408, regime age 90.7 min
- agent weights: empirical 0.003, ewma 0.040, garch 0.067, har 0.148, bocpd 0.010, hmm 0.037, online_qr 0.189, lgbm 0.507

## Learning log

- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.02, 4.65, 13.74], current probabilities: [0.051, 0.938, 0.011]
- live generator: {'versions': 60, 'latest_effective': '2026-10-12 08:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.328, 'l_abs': 0.684, 'l_hi': 0.72, 'l_lo': 0.654, 'b05': 0.667, 'b25': 0.635, 'b75': 0.664, 'b95': 0.643}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.538, 2.004, 2.462, 2.988, 3.849, 3.77, 3.803, 5.036, 5.009, 6.303, 4.79, 5.304, 5.856, 6.987]}
- calibration offsets (in sigma): {'05': 0.0115, '10': 0.123, '25': 0.0075, '40': -0.048, '50': -0.005, '60': -0.002, '75': 0.0125, '90': 0.047, '95': -0.0115}
