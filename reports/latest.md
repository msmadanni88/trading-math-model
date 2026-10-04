# ETH-USD 60s candle generator - report

- generated: 2026-10-04 07:26 UTC
- last closed candle: 2026-10-04 07:26 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k13_next 0.276 in the last 7 days, -0.063 against the 7 before
- WIN RATE FALLING: reversal_k5_next 0.451 in the last 7 days, -0.094 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.380 in the last 7 days, -0.071 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.521 (670) [0.491, 0.551] | 0.510 (2876) [0.491, 0.528] | 0.512 (3068) [0.495, 0.530] | 0.531 (96) | 0.724 (29) | 0.500 | flat -0.024 (noise 0.030) |
| colour_clear | 0.546 (721) | 0.501 (5394) [0.487, 0.516] | 0.499 (23299) [0.494, 0.504] | 0.498 (24959) [0.493, 0.503] | 0.546 (721) | 0.575 (181) | 0.500 | flat +0.001 (noise 0.010) |
| colour_confident | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.651 (106) | 0.500 | - |
| colour_next | 0.521 (1404) | 0.507 (10003) [0.501, 0.512] | 0.502 (42884) [0.498, 0.505] | 0.501 (45753) [0.497, 0.505] | 0.521 (1404) | 0.556 (439) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.493 (19656) | 0.501 (140042) [0.498, 0.504] | 0.501 (600376) [0.500, 0.502] | 0.500 (640542) [0.499, 0.502] | 0.493 (19656) | 0.496 (6146) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.652 (46) | 0.500 | - |
| reversal_k13_next | 0.324 (102) | 0.276 (635) [0.256, 0.295] | 0.307 (1993) [0.292, 0.323] | 0.301 (2207) [0.287, 0.318] | 0.324 (102) | 0.300 (20) | 0.076 | down -0.063 (noise 0.031) |
| reversal_k13_now | 0.756 (45) | 0.594 (342) [0.539, 0.654] | 0.588 (1428) [0.566, 0.613] | 0.586 (1517) [0.564, 0.608] | 0.756 (45) | 0.625 (16) | 0.076 | flat -0.026 (noise 0.040) |
| reversal_k3_next | 0.535 (144) | 0.578 (689) [0.549, 0.610] | 0.584 (2430) [0.568, 0.599] | 0.584 (2584) [0.570, 0.599] | 0.535 (144) | 0.714 (28) | 0.292 | flat +0.006 (noise 0.031) |
| reversal_k3_now | 0.930 (57) | 0.946 (388) [0.936, 0.958] | 0.942 (1710) [0.933, 0.950] | 0.941 (1820) [0.933, 0.949] | 0.930 (57) | 0.947 (19) | 0.292 | flat +0.003 (noise 0.016) |
| reversal_k5_next | 0.407 (189) | 0.451 (658) [0.418, 0.484] | 0.486 (2076) [0.466, 0.506] | 0.486 (2179) [0.469, 0.506] | 0.407 (189) | 0.533 (30) | 0.187 | down -0.094 (noise 0.034) |
| reversal_k5_now | 0.820 (61) | 0.858 (366) [0.838, 0.886] | 0.836 (1587) [0.821, 0.851] | 0.837 (1672) [0.823, 0.851] | 0.820 (61) | 0.947 (19) | 0.187 | flat +0.041 (noise 0.027) |
| reversal_k8_next | 0.377 (77) | 0.380 (418) [0.355, 0.406] | 0.400 (2018) [0.382, 0.419] | 0.395 (2183) [0.379, 0.414] | 0.377 (77) | 0.579 (19) | 0.121 | down -0.071 (noise 0.035) |
| reversal_k8_now | 0.780 (50) | 0.735 (325) [0.700, 0.772] | 0.718 (1551) [0.698, 0.738] | 0.716 (1637) [0.697, 0.736] | 0.780 (50) | 0.857 (14) | 0.121 | flat -0.013 (noise 0.033) |
| overall | 0.496 (21881) | 0.503 (154536) [0.500, 0.506] | 0.503 (660929) [0.502, 0.504] | 0.502 (705162) [0.501, 0.504] | 0.496 (21881) | 0.505 (6779) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07494, 0.1112] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5318, 'levels': [{'threshold': 0.07494, 'calls_per_day': 145.7, 'win_rate': 0.5599}, {'threshold': 0.1112, 'calls_per_day': 37.0, 'win_rate': 0.6398}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 711, 'rate': 0.5612}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15029 | 0.332 | 0.506 (14811) | 0.632 (190) | 0.783 (2325) |
| volatility: normal | 15028 | 0.360 | 0.508 (14963) | - | 0.771 (2099) |
| volatility: wild | 15029 | 0.373 | 0.491 (14985) | - | 0.781 (2110) |
| session: Asia 00-08 | 15326 | 0.351 | 0.500 (15216) | 0.645 (107) | 0.784 (2193) |
| session: Europe 08-13 | 9300 | 0.350 | 0.505 (9235) | - | 0.768 (1404) |
| session: US 13-21 | 14880 | 0.365 | 0.501 (14789) | - | 0.782 (2192) |
| session: late 21-24 | 5580 | 0.351 | 0.503 (5519) | 0.619 (42) | 0.770 (745) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.327 | 0.320 | 0.259 | 0.259 | 0.542 | 0.251 | 0.403 | 1.266 |
| 6h | 360 | 0.304 | 0.303 | 0.239 | 0.240 | 0.552 | 0.221 | 0.388 | 1.825 |
| 24h | 1440 | 0.310 | 0.300 | 0.228 | 0.238 | 0.545 | 0.237 | 0.383 | 1.354 |
| 7d | 10080 | 0.356 | 0.356 | 0.284 | 0.310 | 0.508 | 0.243 | 0.470 | 1.377 |
| 30d | 43200 | 0.355 | 0.354 | 0.278 | 0.308 | 0.502 | 0.245 | 0.465 | 1.290 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.327 / 0.542 / 0.883; 2: 0.291 / 0.458 / 0.850; 3: 0.306 / 0.576 / 0.817; 4: 0.277 / 0.356 / 0.850; 5: 0.323 / 0.627 / 0.750; 6: 0.297 / 0.492 / 0.750; 7: 0.307 / 0.525 / 0.700; 8: 0.284 / 0.390 / 0.700; 9: 0.302 / 0.475 / 0.650; 10: 0.308 / 0.542 / 0.650; 11: 0.308 / 0.508 / 0.617; 12: 0.303 / 0.525 / 0.633; 13: 0.301 / 0.542 / 0.650; 14: 0.301 / 0.492 / 0.650; 15: 0.294 / 0.492 / 0.700
- 6h: 1: 0.304 / 0.552 / 0.897; 2: 0.284 / 0.518 / 0.897; 3: 0.288 / 0.552 / 0.878; 4: 0.274 / 0.490 / 0.919; 5: 0.282 / 0.487 / 0.906; 6: 0.285 / 0.504 / 0.911; 7: 0.279 / 0.501 / 0.889; 8: 0.281 / 0.485 / 0.892; 9: 0.282 / 0.487 / 0.883; 10: 0.292 / 0.549 / 0.872; 11: 0.285 / 0.513 / 0.861; 12: 0.286 / 0.527 / 0.894; 13: 0.272 / 0.442 / 0.906; 14: 0.294 / 0.515 / 0.894; 15: 0.279 / 0.468 / 0.908
- 24h: 1: 0.310 / 0.545 / 0.870; 2: 0.295 / 0.506 / 0.894; 3: 0.297 / 0.517 / 0.897; 4: 0.294 / 0.516 / 0.903; 5: 0.292 / 0.485 / 0.898; 6: 0.290 / 0.480 / 0.901; 7: 0.292 / 0.500 / 0.894; 8: 0.289 / 0.473 / 0.894; 9: 0.288 / 0.475 / 0.894; 10: 0.299 / 0.525 / 0.894; 11: 0.294 / 0.510 / 0.888; 12: 0.292 / 0.507 / 0.890; 13: 0.296 / 0.486 / 0.889; 14: 0.295 / 0.490 / 0.886; 15: 0.287 / 0.460 / 0.892
- 7d: 1: 0.356 / 0.508 / 0.897; 2: 0.350 / 0.491 / 0.899; 3: 0.354 / 0.511 / 0.899; 4: 0.350 / 0.498 / 0.901; 5: 0.350 / 0.505 / 0.900; 6: 0.348 / 0.497 / 0.900; 7: 0.348 / 0.501 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.491 / 0.900; 10: 0.347 / 0.507 / 0.900; 11: 0.348 / 0.505 / 0.900; 12: 0.349 / 0.510 / 0.900; 13: 0.347 / 0.499 / 0.900; 14: 0.346 / 0.497 / 0.900; 15: 0.345 / 0.494 / 0.900
- 30d: 1: 0.355 / 0.502 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.506 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.350 / 0.501 / 0.900; 6: 0.349 / 0.504 / 0.900; 7: 0.349 / 0.506 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.498 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.503 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.345 / 0.500 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.344 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.085 (body 0.058, range 0.111); 'price stays where it was' would score 0.078; colour right 0.492; typical miss of the close 3.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.109 (body 0.076, range 0.141); 'price stays where it was' would score 0.126; colour right 0.530; typical miss of the close 2.5 bp; chain ended on the right side 0.792 of 24 chains; n=360
- 24h: match 0.109 (body 0.079, range 0.139); 'price stays where it was' would score 0.106; colour right 0.498; typical miss of the close 3.2 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.118 (body 0.077, range 0.159); 'price stays where it was' would score 0.119; colour right 0.494; typical miss of the close 7.4 bp; chain ended on the right side 0.525 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.0 bp; chain ended on the right side 0.510 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.3; 2: 0.198 / 4.4; 3: 0.169 / 6.2; 4: 0.133 / 6.5; 5: 0.122 / 7.3; 6: 0.113 / 8.2; 7: 0.100 / 8.5; 8: 0.093 / 9.0; 9: 0.090 / 9.2; 10: 0.083 / 10.1; 11: 0.077 / 10.6; 12: 0.075 / 11.0; 13: 0.068 / 11.3; 14: 0.067 / 11.4; 15: 0.063 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 89480, probability skill vs chance 0.2216, widened contest next: False
  - now: threshold 0.8403, hit rate recent 0.9272 / long run 0.9407
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.303, naive rule 0.513, lift 3.08x
    - 24h: 57 calls (57 a day), hit rate 0.930, chance 0.305, naive rule 0.512, lift 3.05x
    - 7d: 397 calls (57 a day), hit rate 0.947, chance 0.290, naive rule 0.485, lift 3.27x
    - 30d: 1713 calls (57 a day), hit rate 0.941, chance 0.293, naive rule 0.483, lift 3.21x
  - next: threshold 0.5417, hit rate recent 0.6138 / long run 0.5813
    - 6h: 19 calls (77 a day), hit rate 0.684, chance 0.303, lift 2.26x
    - 24h: 140 calls (140 a day), hit rate 0.564, chance 0.305, lift 1.85x
    - 7d: 691 calls (99 a day), hit rate 0.579, chance 0.290, lift 2.00x
    - 30d: 2440 calls (81 a day), hit rate 0.586, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.495; 0.35: 538, 0.520; 0.40: 490, 0.561; 0.45: 423, 0.626; 0.50: 369, 0.681; 0.55: 322, 0.725; 0.60: 274, 0.767; 0.65: 224, 0.803; 0.70: 182, 0.835; 0.75: 140, 0.869; 0.80: 99, 0.908; 0.85: 49, 0.949; 0.90: 1, 0.972
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.425; 0.35: 497, 0.460; 0.40: 414, 0.487; 0.45: 318, 0.519; 0.50: 209, 0.552; 0.55: 94, 0.588; 0.60: 13, 0.613; 0.65: 0, 0.714
- **K=5**: model 1790208000, labels learned 89478, probability skill vs chance 0.2146, widened contest next: False
  - now: threshold 0.7106, hit rate recent 0.8544 / long run 0.8421
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.180, naive rule 0.384, lift 5.19x
    - 24h: 61 calls (61 a day), hit rate 0.852, chance 0.188, naive rule 0.390, lift 4.53x
    - 7d: 377 calls (54 a day), hit rate 0.859, chance 0.188, naive rule 0.394, lift 4.58x
    - 30d: 1589 calls (53 a day), hit rate 0.838, chance 0.187, naive rule 0.392, lift 4.48x
  - next: threshold 0.4367, hit rate recent 0.4614 / long run 0.4732
    - 6h: 19 calls (78 a day), hit rate 0.526, chance 0.180, lift 2.93x
    - 24h: 159 calls (160 a day), hit rate 0.421, chance 0.188, lift 2.24x
    - 7d: 678 calls (97 a day), hit rate 0.451, chance 0.188, lift 2.41x
    - 30d: 2083 calls (69 a day), hit rate 0.487, chance 0.187, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 433, 0.411; 0.35: 374, 0.463; 0.40: 302, 0.531; 0.45: 247, 0.588; 0.50: 192, 0.648; 0.55: 147, 0.697; 0.60: 115, 0.738; 0.65: 88, 0.781; 0.70: 65, 0.820; 0.75: 35, 0.859; 0.80: 9, 0.874
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 254, 0.424; 0.40: 168, 0.448; 0.45: 88, 0.473; 0.50: 22, 0.514; 0.55: 3, 0.573
- **K=8**: model 1791072000, labels learned 89475, probability skill vs chance 0.202, widened contest next: False
  - now: threshold 0.5624, hit rate recent 0.769 / long run 0.7311
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.120, naive rule 0.313, lift 7.58x
    - 24h: 48 calls (48 a day), hit rate 0.771, chance 0.123, naive rule 0.328, lift 6.26x
    - 7d: 326 calls (47 a day), hit rate 0.736, chance 0.123, naive rule 0.332, lift 5.97x
    - 30d: 1544 calls (51 a day), hit rate 0.721, chance 0.122, naive rule 0.327, lift 5.92x
  - next: threshold 0.3664, hit rate recent 0.4388 / long run 0.4083
    - 6h: 14 calls (58 a day), hit rate 0.571, chance 0.120, lift 4.76x
    - 24h: 77 calls (78 a day), hit rate 0.429, chance 0.123, lift 3.48x
    - 7d: 420 calls (60 a day), hit rate 0.386, chance 0.123, lift 3.13x
    - 30d: 2010 calls (67 a day), hit rate 0.403, chance 0.122, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 278, 0.397; 0.35: 209, 0.472; 0.40: 162, 0.536; 0.45: 128, 0.584; 0.50: 98, 0.625; 0.55: 69, 0.680; 0.60: 46, 0.726; 0.65: 25, 0.761; 0.70: 9, 0.802; 0.75: 1, 0.812
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 190, 0.344; 0.35: 119, 0.382; 0.40: 49, 0.409; 0.45: 11, 0.425; 0.50: 1, 0.452
- **K=13**: model 1791072000, labels learned 89470, probability skill vs chance 0.1865, widened contest next: False
  - now: threshold 0.4076, hit rate recent 0.6684 / long run 0.5966
    - 6h: 12 calls (50 a day), hit rate 0.667, chance 0.074, naive rule 0.229, lift 9.02x
    - 24h: 46 calls (46 a day), hit rate 0.717, chance 0.081, naive rule 0.275, lift 8.81x
    - 7d: 346 calls (50 a day), hit rate 0.587, chance 0.078, naive rule 0.266, lift 7.50x
    - 30d: 1430 calls (48 a day), hit rate 0.589, chance 0.076, naive rule 0.266, lift 7.71x
  - next: threshold 0.2721, hit rate recent 0.3104 / long run 0.297
    - 6h: 15 calls (63 a day), hit rate 0.333, chance 0.074, lift 4.51x
    - 24h: 93 calls (94 a day), hit rate 0.301, chance 0.081, lift 3.70x
    - 7d: 642 calls (92 a day), hit rate 0.273, chance 0.078, lift 3.49x
    - 30d: 1986 calls (66 a day), hit rate 0.306, chance 0.076, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.433; 0.35: 91, 0.490; 0.40: 65, 0.537; 0.45: 45, 0.597; 0.50: 29, 0.616; 0.55: 16, 0.657; 0.60: 7, 0.674; 0.65: 2, 0.762; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.315; 0.35: 18, 0.347; 0.40: 4, 0.339; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.782 | 0.23% | 0.900 | 0.450 | 0.249 | 0.525 | 0.084 |
| 6h | 4.042 | 3.22% | 0.914 | 0.539 | 0.252 | 0.499 | 0.274 |
| 24h | 4.820 | 6.38% | 0.887 | 0.514 | 0.251 | 0.501 | 0.302 |
| 7d | 12.677 | 4.13% | 0.899 | 0.503 | 0.251 | 0.497 | 0.682 |
| 30d | 14.258 | 4.22% | 0.900 | 0.501 | 0.251 | 0.499 | 0.684 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 4.792 | 4.819 | 4.833 | 4.790 | 5.215 | 5.120 | 4.758 | 4.739 | 4.768 | 4.782 |
| 6h | 4.177 | 4.114 | 4.093 | 4.037 | 4.333 | 4.438 | 4.053 | 4.066 | 4.058 | 4.042 |
| 24h | 5.148 | 4.858 | 4.900 | 4.858 | 4.994 | 5.254 | 4.816 | 4.814 | 4.816 | 4.820 |
| 7d | 13.223 | 12.775 | 12.758 | 12.688 | 12.923 | 12.853 | 12.668 | 12.665 | 12.654 | 12.677 |
| 30d | 14.886 | 14.396 | 14.347 | 14.284 | 14.539 | 14.481 | 14.266 | 14.232 | 14.231 | 14.258 |

## Next candle

- candle starting 2026-10-04 07:26 UTC, last close 2694.13
- P(up) 0.5019, return quantiles (bp): {'05': -3.37, '10': -2.34, '25': -1.029, '40': -0.35, '50': 0.007, '60': 0.349, '75': 0.905, '90': 2.467, '95': 3.493}
- changepoint probability 0.0855, regime age 45.7 min
- agent weights: empirical 0.015, ewma 0.114, garch 0.109, har 0.210, bocpd 0.008, hmm 0.003, online_qr 0.261, lgbm 0.280

## Learning log

- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- HMM volatility states (sd, bp per minute): [1.97, 4.8, 13.0], current probabilities: [0.958, 0.042, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-04 07:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.317, 'l_abs': 0.707, 'l_hi': 0.772, 'l_lo': 0.725, 'b05': 0.648, 'b25': 0.742, 'b75': 0.603, 'b95': 0.607}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.2, 1.6], [1.2, 1.6], [1.2, 1.6], [1.4, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.595, 1.957, 1.891, 2.295, 2.42, 2.838, 3.101, 3.23, 3.481, 3.884, 3.396, 3.402, 3.833, 3.669]}
- calibration offsets (in sigma): {'05': 0.0225, '10': 0.095, '25': 0.0725, '40': 0.02, '50': -0.005, '60': -0.05, '75': -0.1725, '90': -0.015, '95': 0.0475}
