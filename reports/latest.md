# ETH-USD 60s candle generator - report

- generated: 2026-10-12 01:43 UTC
- last closed candle: 2026-10-12 01:43 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.453 (95) | 0.482 (670) [0.439, 0.525] | 0.508 (2874) [0.487, 0.527] | 0.510 (3834) [0.493, 0.526] | 0.505 (862) [0.462, 0.548] | 0.667 (6) | 0.500 | flat -0.045 (noise 0.036) |
| colour_clear | 0.531 (718) | 0.541 (5407) [0.533, 0.549] | 0.511 (23135) [0.503, 0.519] | 0.507 (31040) [0.500, 0.513] | 0.543 (6802) [0.536, 0.550] | 0.552 (67) | 0.500 | up +0.034 (noise 0.012) |
| colour_confident | 0.602 (196) | 0.602 (1076) [0.569, 0.646] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.606 (1420) [0.579, 0.638] | 0.571 (7) | 0.500 | flat -0.017 (noise 0.030) |
| colour_next | 0.529 (1419) | 0.527 (9960) [0.520, 0.535] | 0.509 (42822) [0.504, 0.515] | 0.507 (57130) [0.502, 0.511] | 0.529 (12781) [0.522, 0.536] | 0.594 (101) | 0.500 | flat +0.015 (noise 0.008) |
| colour_path | 0.499 (19866) | 0.499 (139440) [0.496, 0.502] | 0.501 (599508) [0.500, 0.502] | 0.500 (799820) [0.499, 0.501] | 0.499 (178934) [0.496, 0.502] | 0.521 (1414) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.661 (65) | 0.660 (282) [0.605, 0.725] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 0.657 (397) [0.620, 0.703] | 1.000 (1) | 0.500 | flat +0.007 (noise 0.053) |
| reversal_k13_next | 0.373 (67) | 0.329 (492) [0.312, 0.347] | 0.314 (2061) [0.300, 0.331] | 0.308 (2785) [0.295, 0.321] | 0.332 (680) [0.319, 0.346] | 0.000 (2) | 0.077 | flat +0.040 (noise 0.028) |
| reversal_k13_now | 0.588 (51) | 0.573 (386) [0.546, 0.601] | 0.585 (1499) [0.564, 0.609] | 0.584 (1968) [0.566, 0.602] | 0.593 (496) [0.562, 0.632] | 0.500 (4) | 0.077 | flat -0.012 (noise 0.036) |
| reversal_k3_next | 0.605 (86) | 0.592 (519) [0.557, 0.624] | 0.589 (2389) [0.574, 0.604] | 0.586 (3227) [0.574, 0.599] | 0.582 (787) [0.556, 0.609] | 0.667 (3) | 0.294 | flat +0.002 (noise 0.028) |
| reversal_k3_now | 0.914 (70) | 0.922 (424) [0.913, 0.934] | 0.938 (1738) [0.930, 0.946] | 0.937 (2308) [0.930, 0.944] | 0.923 (545) [0.915, 0.932] | 1.000 (3) | 0.294 | flat -0.019 (noise 0.018) |
| reversal_k5_next | 0.492 (61) | 0.470 (421) [0.438, 0.500] | 0.485 (2076) [0.467, 0.504] | 0.484 (2720) [0.468, 0.501] | 0.456 (730) [0.430, 0.489] | - | 0.188 | flat +0.013 (noise 0.030) |
| reversal_k5_now | 0.840 (50) | 0.816 (369) [0.787, 0.845] | 0.837 (1601) [0.822, 0.852] | 0.835 (2109) [0.821, 0.848] | 0.827 (498) [0.800, 0.853] | 1.000 (2) | 0.188 | flat -0.038 (noise 0.027) |
| reversal_k8_next | 0.357 (84) | 0.380 (610) [0.357, 0.404] | 0.406 (2114) [0.388, 0.426] | 0.394 (2880) [0.381, 0.410] | 0.390 (774) [0.367, 0.415] | 0.000 (2) | 0.122 | flat -0.020 (noise 0.031) |
| reversal_k8_now | 0.683 (60) | 0.684 (418) [0.648, 0.724] | 0.721 (1600) [0.700, 0.741] | 0.712 (2115) [0.694, 0.729] | 0.705 (528) [0.667, 0.742] | 0.600 (5) | 0.122 | flat -0.045 (noise 0.033) |
| overall | 0.503 (21909) | 0.503 (153709) [0.499, 0.506] | 0.504 (660282) [0.502, 0.505] | 0.503 (880896) [0.502, 0.504] | 0.503 (197615) [0.500, 0.506] | 0.527 (1542) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08035, 0.122] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5266, 'levels': [{'threshold': 0.08035, 'calls_per_day': 142.0, 'win_rate': 0.5994}, {'threshold': 0.122, 'calls_per_day': 35.7, 'win_rate': 0.664}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 11748, 'rate': 0.5313}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14915 | 0.330 | 0.521 (14639) | 0.597 (1137) | 0.778 (2455) |
| volatility: normal | 14914 | 0.358 | 0.508 (14845) | 0.630 (216) | 0.780 (2123) |
| volatility: wild | 14914 | 0.374 | 0.497 (14871) | 0.676 (74) | 0.774 (2050) |
| session: Asia 00-08 | 14983 | 0.351 | 0.512 (14866) | 0.599 (509) | 0.773 (2162) |
| session: Europe 08-13 | 9300 | 0.347 | 0.506 (9209) | 0.594 (345) | 0.775 (1465) |
| session: US 13-21 | 14880 | 0.363 | 0.505 (14771) | 0.590 (366) | 0.785 (2191) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5509) | 0.671 (207) | 0.773 (810) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.386 | 0.362 | 0.275 | 0.275 | 0.593 | 0.288 | 0.484 | 1.128 |
| 6h | 360 | 0.363 | 0.347 | 0.276 | 0.296 | 0.549 | 0.269 | 0.456 | 1.120 |
| 24h | 1440 | 0.339 | 0.329 | 0.253 | 0.272 | 0.540 | 0.253 | 0.426 | 1.198 |
| 7d | 10080 | 0.354 | 0.347 | 0.273 | 0.300 | 0.527 | 0.257 | 0.450 | 1.200 |
| 30d | 43200 | 0.354 | 0.352 | 0.276 | 0.305 | 0.509 | 0.248 | 0.460 | 1.307 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.386 / 0.593 / 0.900; 2: 0.411 / 0.627 / 0.833; 3: 0.377 / 0.492 / 0.917; 4: 0.369 / 0.458 / 0.917; 5: 0.370 / 0.475 / 0.967; 6: 0.368 / 0.492 / 0.983; 7: 0.401 / 0.559 / 0.967; 8: 0.346 / 0.424 / 0.967; 9: 0.395 / 0.576 / 0.983; 10: 0.364 / 0.492 / 0.983; 11: 0.339 / 0.475 / 0.983; 12: 0.362 / 0.492 / 1.000; 13: 0.401 / 0.593 / 1.000; 14: 0.337 / 0.458 / 1.000; 15: 0.351 / 0.424 / 1.000
- 6h: 1: 0.363 / 0.549 / 0.897; 2: 0.348 / 0.524 / 0.903; 3: 0.362 / 0.563 / 0.931; 4: 0.332 / 0.454 / 0.933; 5: 0.354 / 0.518 / 0.961; 6: 0.338 / 0.479 / 0.969; 7: 0.344 / 0.499 / 0.961; 8: 0.341 / 0.487 / 0.969; 9: 0.345 / 0.532 / 0.967; 10: 0.349 / 0.515 / 0.967; 11: 0.333 / 0.510 / 0.961; 12: 0.342 / 0.515 / 0.972; 13: 0.340 / 0.499 / 0.961; 14: 0.329 / 0.496 / 0.961; 15: 0.345 / 0.518 / 0.967
- 24h: 1: 0.339 / 0.540 / 0.897; 2: 0.330 / 0.518 / 0.899; 3: 0.326 / 0.505 / 0.899; 4: 0.321 / 0.484 / 0.905; 5: 0.321 / 0.494 / 0.904; 6: 0.322 / 0.493 / 0.903; 7: 0.323 / 0.498 / 0.904; 8: 0.326 / 0.508 / 0.901; 9: 0.323 / 0.499 / 0.904; 10: 0.321 / 0.489 / 0.903; 11: 0.320 / 0.498 / 0.906; 12: 0.319 / 0.495 / 0.903; 13: 0.325 / 0.501 / 0.902; 14: 0.320 / 0.498 / 0.903; 15: 0.320 / 0.505 / 0.907
- 7d: 1: 0.354 / 0.527 / 0.900; 2: 0.344 / 0.499 / 0.900; 3: 0.344 / 0.509 / 0.901; 4: 0.343 / 0.501 / 0.901; 5: 0.342 / 0.505 / 0.902; 6: 0.339 / 0.495 / 0.902; 7: 0.339 / 0.500 / 0.901; 8: 0.339 / 0.496 / 0.901; 9: 0.336 / 0.490 / 0.901; 10: 0.339 / 0.501 / 0.901; 11: 0.337 / 0.494 / 0.901; 12: 0.337 / 0.494 / 0.900; 13: 0.340 / 0.505 / 0.900; 14: 0.338 / 0.502 / 0.900; 15: 0.338 / 0.498 / 0.900
- 30d: 1: 0.354 / 0.509 / 0.898; 2: 0.348 / 0.497 / 0.900; 3: 0.350 / 0.510 / 0.900; 4: 0.347 / 0.499 / 0.900; 5: 0.347 / 0.505 / 0.900; 6: 0.346 / 0.502 / 0.900; 7: 0.346 / 0.504 / 0.900; 8: 0.345 / 0.503 / 0.900; 9: 0.342 / 0.496 / 0.900; 10: 0.344 / 0.504 / 0.900; 11: 0.343 / 0.501 / 0.900; 12: 0.344 / 0.503 / 0.900; 13: 0.343 / 0.501 / 0.900; 14: 0.342 / 0.497 / 0.900; 15: 0.342 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.128 (body 0.108, range 0.149); 'price stays where it was' would score 0.195; colour right 0.492; typical miss of the close 6.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.122 (body 0.084, range 0.159); 'price stays where it was' would score 0.150; colour right 0.504; typical miss of the close 5.9 bp; chain ended on the right side 0.522 of 23 chains; n=360
- 24h: match 0.114 (body 0.079, range 0.149); 'price stays where it was' would score 0.130; colour right 0.504; typical miss of the close 5.1 bp; chain ended on the right side 0.453 of 95 chains; n=1440
- 7d: match 0.118 (body 0.081, range 0.155); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 6.4 bp; chain ended on the right side 0.484 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.6 bp; chain ended on the right side 0.509 of 2874 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 3.8; 2: 0.199 / 4.2; 3: 0.165 / 5.7; 4: 0.132 / 6.3; 5: 0.119 / 6.9; 6: 0.109 / 7.5; 7: 0.101 / 7.9; 8: 0.093 / 8.2; 9: 0.087 / 8.4; 10: 0.082 / 9.2; 11: 0.076 / 9.7; 12: 0.075 / 10.2; 13: 0.063 / 10.5; 14: 0.065 / 10.5; 15: 0.061 / 10.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 100657, probability skill vs chance 0.2306, widened contest next: False
  - now: threshold 0.84, hit rate recent 0.9268 / long run 0.9297
    - 6h: 10 calls (40 a day), hit rate 1.000, chance 0.316, naive rule 0.579, lift 3.16x
    - 24h: 66 calls (66 a day), hit rate 0.909, chance 0.327, naive rule 0.577, lift 2.78x
    - 7d: 424 calls (61 a day), hit rate 0.922, chance 0.302, naive rule 0.506, lift 3.06x
    - 30d: 1736 calls (58 a day), hit rate 0.938, chance 0.293, naive rule 0.486, lift 3.20x
  - next: threshold 0.5693, hit rate recent 0.6518 / long run 0.5887
    - 6h: 7 calls (28 a day), hit rate 0.857, chance 0.316, lift 2.71x
    - 24h: 78 calls (78 a day), hit rate 0.628, chance 0.327, lift 1.92x
    - 7d: 519 calls (74 a day), hit rate 0.592, chance 0.302, lift 1.96x
    - 30d: 2390 calls (80 a day), hit rate 0.588, chance 0.293, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.495; 0.35: 538, 0.519; 0.40: 485, 0.565; 0.45: 417, 0.632; 0.50: 364, 0.686; 0.55: 320, 0.726; 0.60: 273, 0.769; 0.65: 225, 0.802; 0.70: 181, 0.834; 0.75: 139, 0.873; 0.80: 97, 0.913; 0.85: 49, 0.948; 0.90: 3, 0.975
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.426; 0.35: 498, 0.460; 0.40: 412, 0.490; 0.45: 317, 0.523; 0.50: 206, 0.557; 0.55: 92, 0.582; 0.60: 14, 0.607; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 100655, probability skill vs chance 0.2254, widened contest next: False
  - now: threshold 0.7117, hit rate recent 0.8632 / long run 0.8337
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.229, naive rule 0.568, lift 4.37x
    - 24h: 50 calls (50 a day), hit rate 0.860, chance 0.209, naive rule 0.477, lift 4.12x
    - 7d: 369 calls (53 a day), hit rate 0.818, chance 0.195, naive rule 0.414, lift 4.20x
    - 30d: 1602 calls (53 a day), hit rate 0.837, chance 0.188, naive rule 0.395, lift 4.45x
  - next: threshold 0.4422, hit rate recent 0.5118 / long run 0.4736
    - 6h: 6 calls (24 a day), hit rate 0.833, chance 0.229, lift 3.64x
    - 24h: 60 calls (60 a day), hit rate 0.500, chance 0.209, lift 2.40x
    - 7d: 420 calls (60 a day), hit rate 0.471, chance 0.195, lift 2.42x
    - 30d: 2069 calls (69 a day), hit rate 0.484, chance 0.188, lift 2.57x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 427, 0.419; 0.35: 361, 0.477; 0.40: 292, 0.546; 0.45: 238, 0.604; 0.50: 185, 0.660; 0.55: 140, 0.708; 0.60: 109, 0.751; 0.65: 84, 0.796; 0.70: 62, 0.826; 0.75: 34, 0.866; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.389; 0.35: 252, 0.426; 0.40: 164, 0.453; 0.45: 82, 0.474; 0.50: 20, 0.514; 0.55: 2, 0.550
- **K=8**: model 1791417600, labels learned 100652, probability skill vs chance 0.2107, widened contest next: False
  - now: threshold 0.573, hit rate recent 0.7083 / long run 0.708
    - 6h: 14 calls (57 a day), hit rate 0.714, chance 0.140, naive rule 0.470, lift 5.12x
    - 24h: 61 calls (61 a day), hit rate 0.689, chance 0.128, naive rule 0.376, lift 5.40x
    - 7d: 419 calls (60 a day), hit rate 0.685, chance 0.124, naive rule 0.344, lift 5.52x
    - 30d: 1602 calls (53 a day), hit rate 0.720, chance 0.122, naive rule 0.331, lift 5.88x
  - next: threshold 0.3645, hit rate recent 0.3886 / long run 0.3923
    - 6h: 12 calls (49 a day), hit rate 0.333, chance 0.140, lift 2.39x
    - 24h: 81 calls (82 a day), hit rate 0.370, chance 0.128, lift 2.90x
    - 7d: 608 calls (87 a day), hit rate 0.378, chance 0.124, lift 3.05x
    - 30d: 2110 calls (70 a day), hit rate 0.404, chance 0.122, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 266, 0.410; 0.35: 201, 0.485; 0.40: 155, 0.545; 0.45: 122, 0.591; 0.50: 93, 0.636; 0.55: 67, 0.689; 0.60: 46, 0.729; 0.65: 25, 0.774; 0.70: 9, 0.823; 0.75: 1, 0.857
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 182, 0.350; 0.35: 112, 0.388; 0.40: 47, 0.414; 0.45: 10, 0.446; 0.50: 1, 0.390
- **K=13**: model 1791504000, labels learned 100647, probability skill vs chance 0.1803, widened contest next: False
  - now: threshold 0.4353, hit rate recent 0.5963 / long run 0.5868
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.084, naive rule 0.378, lift 6.96x
    - 24h: 51 calls (52 a day), hit rate 0.588, chance 0.078, naive rule 0.306, lift 7.56x
    - 7d: 385 calls (55 a day), hit rate 0.569, chance 0.079, naive rule 0.283, lift 7.21x
    - 30d: 1501 calls (50 a day), hit rate 0.585, chance 0.078, naive rule 0.272, lift 7.52x
  - next: threshold 0.2908, hit rate recent 0.3562 / long run 0.3215
    - 6h: 9 calls (37 a day), hit rate 0.222, chance 0.084, lift 2.65x
    - 24h: 63 calls (64 a day), hit rate 0.365, chance 0.078, lift 4.69x
    - 7d: 486 calls (70 a day), hit rate 0.327, chance 0.079, lift 4.15x
    - 30d: 2063 calls (69 a day), hit rate 0.314, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.448; 0.35: 86, 0.509; 0.40: 62, 0.556; 0.45: 43, 0.612; 0.50: 27, 0.636; 0.55: 14, 0.690; 0.60: 5, 0.730; 0.65: 1, 0.769
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 14, 0.349; 0.40: 3, 0.325; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.195 | 2.28% | 0.900 | 0.417 | 0.251 | 0.458 | 0.111 |
| 6h | 11.046 | 4.04% | 0.900 | 0.469 | 0.251 | 0.456 | 0.457 |
| 24h | 9.237 | 4.67% | 0.903 | 0.495 | 0.251 | 0.483 | 0.586 |
| 7d | 11.330 | 4.87% | 0.901 | 0.501 | 0.251 | 0.493 | 0.658 |
| 30d | 13.561 | 4.28% | 0.900 | 0.500 | 0.251 | 0.497 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.480 | 12.263 | 12.326 | 12.180 | 12.500 | 12.402 | 12.170 | 12.111 | 12.147 | 12.195 |
| 6h | 11.510 | 11.328 | 11.206 | 11.020 | 11.322 | 11.088 | 11.019 | 11.024 | 11.018 | 11.046 |
| 24h | 9.689 | 9.362 | 9.303 | 9.260 | 9.523 | 9.365 | 9.239 | 9.201 | 9.218 | 9.237 |
| 7d | 11.909 | 11.441 | 11.397 | 11.379 | 11.534 | 11.519 | 11.328 | 11.307 | 11.310 | 11.330 |
| 30d | 14.167 | 13.683 | 13.646 | 13.590 | 13.820 | 13.769 | 13.559 | 13.535 | 13.536 | 13.561 |

## Next candle

- candle starting 2026-10-12 01:43 UTC, last close 2537.33
- P(up) 0.5096, return quantiles (bp): {'05': -7.12, '10': -4.843, '25': -2.503, '40': -0.75, '50': 0.076, '60': 1.165, '75': 2.749, '90': 5.458, '95': 7.227}
- changepoint probability 0.0548, regime age 71.6 min
- agent weights: empirical 0.003, ewma 0.026, garch 0.068, har 0.176, bocpd 0.005, hmm 0.046, online_qr 0.254, lgbm 0.423

## Learning log

- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- 2026-10-11 12:00 UTC: {"garch": {"alpha": 0.0776, "beta": 0.9184}, "hmm": {"sd_bp": [2.07, 4.68, 13.59], "stay": [0.983, 0.975, 0.932]}}
- 2026-10-12 00:00 UTC: {"garch": {"alpha": 0.1094, "beta": 0.8821}, "hmm": {"sd_bp": [2.02, 4.65, 13.74], "stay": [0.978, 0.968, 0.934]}, "lgbm": {"challenger_loss": 0.25169, "champion_loss": 0.25161, "promoted": false}, "reversal_k3": {"challenger_loss": 0.50763, "challengers": 1, "chance_loss": 0.62888, "widened": false, "champion_loss": 0.50482, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39292, "challengers": 1, "chance_loss": 0.50479, "widened": false, "champion_loss": 0.39029, "promoted": false}, "reversal_k8": {"challenger_loss": 0.29362, "challengers": 1, "chance_loss": 0.39039, "widened": false, "champion_loss": 0.29284, "promoted": false}, "reversal_k13": {"challenger_loss": 0.22489, "challengers": 1, "chance_loss": 0.29984, "widened": false, "champion_loss": 0.22422, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.02, 4.65, 13.74], current probabilities: [0.071, 0.921, 0.008]
- live generator: {'versions': 60, 'latest_effective': '2026-10-12 01:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.279, 'l_abs': 0.658, 'l_hi': 0.723, 'l_lo': 0.667, 'b05': 0.659, 'b25': 0.617, 'b75': 0.636, 'b95': 0.626}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.367, 1.612, 1.792, 1.928, 1.993, 2.201, 2.504, 2.36, 2.647, 2.619, 3.348, 3.423, 3.352, 3.146]}
- calibration offsets (in sigma): {'05': -0.019, '10': 0.082, '25': -0.015, '40': -0.002, '50': -0.01, '60': 0.022, '75': 0.025, '90': 0.008, '95': -0.021}
