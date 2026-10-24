# ETH-USD 60s candle generator - report

- generated: 2026-10-24 23:46 UTC
- last closed candle: 2026-10-24 23:46 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.573 (96) | 0.539 (672) [0.503, 0.576] | 0.518 (2876) [0.500, 0.538] | 0.515 (4986) [0.500, 0.528] | 0.519 (2014) [0.495, 0.544] | 0.516 (95) | 0.500 | flat +0.019 (noise 0.029) |
| colour_clear | 0.544 (845) | 0.557 (5691) [0.549, 0.564] | 0.531 (23456) [0.522, 0.539] | 0.517 (40748) [0.510, 0.523] | 0.547 (16510) [0.542, 0.552] | 0.543 (739) | 0.500 | flat +0.019 (noise 0.009) |
| colour_confident | 0.648 (202) | 0.605 (1144) [0.582, 0.628] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.604 (2924) [0.588, 0.620] | 0.606 (269) | 0.500 | flat +0.018 (noise 0.022) |
| colour_next | 0.538 (1434) | 0.538 (10023) [0.531, 0.544] | 0.521 (42858) [0.516, 0.527] | 0.513 (74325) [0.508, 0.517] | 0.530 (29976) [0.526, 0.535] | 0.522 (1417) | 0.500 | flat +0.013 (noise 0.007) |
| colour_path | 0.503 (20076) | 0.499 (140322) [0.496, 0.502] | 0.501 (600012) [0.499, 0.502] | 0.500 (1040550) [0.499, 0.502] | 0.500 (419664) [0.498, 0.502] | 0.502 (19838) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.692 (52) | 0.642 (271) [0.608, 0.673] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.651 (736) [0.626, 0.678] | 0.602 (98) | 0.500 | flat -0.009 (noise 0.043) |
| reversal_k13_next | 0.304 (69) | 0.314 (465) [0.295, 0.331] | 0.305 (2157) [0.292, 0.317] | 0.307 (3555) [0.296, 0.318] | 0.317 (1450) [0.306, 0.329] | 0.279 (61) | 0.077 | flat +0.001 (noise 0.031) |
| reversal_k13_now | 0.466 (58) | 0.526 (369) [0.488, 0.568] | 0.567 (1554) [0.547, 0.587] | 0.572 (2600) [0.556, 0.588] | 0.560 (1128) [0.536, 0.586] | 0.640 (50) | 0.077 | flat -0.032 (noise 0.037) |
| reversal_k3_next | 0.603 (63) | 0.586 (759) [0.559, 0.615] | 0.578 (2788) [0.565, 0.592] | 0.583 (4508) [0.573, 0.594] | 0.578 (2068) [0.564, 0.594] | 0.630 (54) | 0.293 | flat +0.010 (noise 0.025) |
| reversal_k3_now | 0.952 (63) | 0.929 (410) [0.907, 0.951] | 0.936 (1693) [0.928, 0.945] | 0.938 (2974) [0.931, 0.944] | 0.931 (1211) [0.921, 0.942] | 0.980 (49) | 0.293 | flat -0.010 (noise 0.018) |
| reversal_k5_next | 0.523 (132) | 0.456 (956) [0.429, 0.482] | 0.464 (2735) [0.449, 0.479] | 0.475 (4181) [0.463, 0.489] | 0.459 (2191) [0.442, 0.475] | 0.471 (123) | 0.187 | flat -0.018 (noise 0.025) |
| reversal_k5_now | 0.793 (58) | 0.813 (358) [0.801, 0.825] | 0.830 (1553) [0.817, 0.844] | 0.830 (2716) [0.819, 0.841] | 0.819 (1105) [0.804, 0.834] | 0.818 (55) | 0.187 | flat -0.013 (noise 0.029) |
| reversal_k8_next | 0.405 (126) | 0.377 (791) [0.358, 0.393] | 0.383 (2493) [0.370, 0.396] | 0.389 (4101) [0.377, 0.400] | 0.381 (1995) [0.366, 0.396] | 0.377 (85) | 0.120 | flat -0.002 (noise 0.026) |
| reversal_k8_now | 0.571 (56) | 0.659 (326) [0.614, 0.708] | 0.701 (1525) [0.680, 0.722] | 0.702 (2684) [0.685, 0.717] | 0.684 (1097) [0.659, 0.709] | 0.709 (55) | 0.121 | flat -0.030 (noise 0.036) |
| overall | 0.507 (22231) | 0.503 (155451) [0.500, 0.506] | 0.504 (662244) [0.502, 0.505] | 0.503 (1147180) [0.502, 0.504] | 0.504 (463899) [0.502, 0.506] | 0.505 (21882) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0725, 0.1066] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5352, 'levels': [{'threshold': 0.0725, 'calls_per_day': 147.6, 'win_rate': 0.6031}, {'threshold': 0.1066, 'calls_per_day': 37.3, 'win_rate': 0.6412}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 30255, 'rate': 0.5309}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15356 | 0.337 | 0.524 (15103) | 0.590 (1667) | 0.766 (2540) |
| volatility: normal | 15355 | 0.365 | 0.521 (15289) | 0.617 (1050) | 0.752 (2258) |
| volatility: wild | 15355 | 0.378 | 0.515 (15320) | 0.626 (476) | 0.773 (1973) |
| session: Asia 00-08 | 15360 | 0.358 | 0.526 (15258) | 0.613 (1120) | 0.767 (2224) |
| session: Europe 08-13 | 9600 | 0.355 | 0.521 (9513) | 0.597 (780) | 0.763 (1543) |
| session: US 13-21 | 15360 | 0.368 | 0.516 (15259) | 0.597 (798) | 0.768 (2171) |
| session: late 21-24 | 5746 | 0.351 | 0.513 (5682) | 0.610 (495) | 0.741 (833) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.339 | 0.324 | 0.221 | 0.221 | 0.533 | 0.247 | 0.432 | 1.475 |
| 6h | 360 | 0.367 | 0.353 | 0.276 | 0.288 | 0.525 | 0.272 | 0.461 | 1.377 |
| 24h | 1440 | 0.362 | 0.349 | 0.271 | 0.301 | 0.523 | 0.268 | 0.456 | 1.200 |
| 7d | 10080 | 0.371 | 0.362 | 0.274 | 0.307 | 0.534 | 0.269 | 0.474 | 1.200 |
| 30d | 43200 | 0.360 | 0.353 | 0.277 | 0.305 | 0.523 | 0.256 | 0.464 | 1.286 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.339 / 0.533 / 0.867; 2: 0.317 / 0.550 / 0.817; 3: 0.330 / 0.500 / 0.800; 4: 0.312 / 0.483 / 0.767; 5: 0.307 / 0.500 / 0.833; 6: 0.308 / 0.550 / 0.783; 7: 0.324 / 0.600 / 0.783; 8: 0.315 / 0.567 / 0.800; 9: 0.300 / 0.500 / 0.817; 10: 0.320 / 0.583 / 0.833; 11: 0.293 / 0.533 / 0.817; 12: 0.328 / 0.600 / 0.783; 13: 0.321 / 0.533 / 0.783; 14: 0.313 / 0.533 / 0.750; 15: 0.327 / 0.567 / 0.733
- 6h: 1: 0.367 / 0.525 / 0.906; 2: 0.352 / 0.514 / 0.892; 3: 0.351 / 0.525 / 0.889; 4: 0.349 / 0.506 / 0.903; 5: 0.339 / 0.503 / 0.914; 6: 0.345 / 0.520 / 0.903; 7: 0.344 / 0.503 / 0.897; 8: 0.338 / 0.486 / 0.897; 9: 0.350 / 0.520 / 0.906; 10: 0.341 / 0.483 / 0.903; 11: 0.348 / 0.525 / 0.903; 12: 0.352 / 0.520 / 0.900; 13: 0.362 / 0.539 / 0.894; 14: 0.361 / 0.539 / 0.908; 15: 0.352 / 0.520 / 0.911
- 24h: 1: 0.362 / 0.523 / 0.908; 2: 0.346 / 0.491 / 0.900; 3: 0.350 / 0.515 / 0.901; 4: 0.340 / 0.475 / 0.902; 5: 0.346 / 0.512 / 0.908; 6: 0.336 / 0.482 / 0.904; 7: 0.343 / 0.500 / 0.909; 8: 0.344 / 0.506 / 0.907; 9: 0.343 / 0.500 / 0.903; 10: 0.343 / 0.499 / 0.902; 11: 0.343 / 0.507 / 0.898; 12: 0.345 / 0.496 / 0.899; 13: 0.346 / 0.525 / 0.898; 14: 0.340 / 0.496 / 0.894; 15: 0.347 / 0.525 / 0.897
- 7d: 1: 0.371 / 0.534 / 0.900; 2: 0.359 / 0.500 / 0.900; 3: 0.360 / 0.511 / 0.900; 4: 0.354 / 0.491 / 0.901; 5: 0.354 / 0.499 / 0.901; 6: 0.354 / 0.496 / 0.900; 7: 0.353 / 0.494 / 0.900; 8: 0.356 / 0.511 / 0.899; 9: 0.353 / 0.499 / 0.899; 10: 0.354 / 0.506 / 0.899; 11: 0.352 / 0.499 / 0.898; 12: 0.353 / 0.503 / 0.898; 13: 0.351 / 0.495 / 0.898; 14: 0.353 / 0.500 / 0.898; 15: 0.352 / 0.504 / 0.898
- 30d: 1: 0.360 / 0.523 / 0.899; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.509 / 0.900; 4: 0.348 / 0.497 / 0.900; 5: 0.349 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.505 / 0.900; 11: 0.345 / 0.498 / 0.900; 12: 0.346 / 0.503 / 0.899; 13: 0.346 / 0.503 / 0.899; 14: 0.344 / 0.498 / 0.899; 15: 0.345 / 0.500 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.096 (body 0.058, range 0.134); 'price stays where it was' would score 0.145; colour right 0.500; typical miss of the close 5.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.082, range 0.154); 'price stays where it was' would score 0.135; colour right 0.514; typical miss of the close 7.5 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.124 (body 0.087, range 0.161); 'price stays where it was' would score 0.144; colour right 0.493; typical miss of the close 7.3 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.128 (body 0.088, range 0.168); 'price stays where it was' would score 0.133; colour right 0.505; typical miss of the close 9.0 bp; chain ended on the right side 0.545 of 672 chains; n=10080
- 30d: match 0.122 (body 0.082, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.8; 2: 0.197 / 4.4; 3: 0.168 / 5.8; 4: 0.130 / 6.4; 5: 0.122 / 7.1; 6: 0.110 / 7.6; 7: 0.105 / 7.9; 8: 0.097 / 8.2; 9: 0.088 / 8.2; 10: 0.087 / 8.9; 11: 0.084 / 9.4; 12: 0.077 / 9.7; 13: 0.068 / 9.9; 14: 0.068 / 10.3; 15: 0.059 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 119260, probability skill vs chance 0.2289, widened contest next: False
  - now: threshold 0.8356, hit rate recent 0.9642 / long run 0.9392
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.301, naive rule 0.527, lift 3.32x
    - 24h: 49 calls (49 a day), hit rate 0.980, chance 0.303, naive rule 0.523, lift 3.23x
    - 7d: 398 calls (57 a day), hit rate 0.945, chance 0.296, naive rule 0.498, lift 3.19x
    - 30d: 1691 calls (56 a day), hit rate 0.937, chance 0.294, naive rule 0.491, lift 3.19x
  - next: threshold 0.5681, hit rate recent 0.6203 / long run 0.5912
    - 6h: 8 calls (32 a day), hit rate 0.500, chance 0.301, lift 1.66x
    - 24h: 54 calls (54 a day), hit rate 0.630, chance 0.303, lift 2.08x
    - 7d: 699 calls (100 a day), hit rate 0.592, chance 0.296, lift 2.00x
    - 30d: 2793 calls (93 a day), hit rate 0.580, chance 0.294, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.494; 0.35: 539, 0.518; 0.40: 479, 0.574; 0.45: 409, 0.645; 0.50: 357, 0.698; 0.55: 312, 0.739; 0.60: 264, 0.784; 0.65: 221, 0.809; 0.70: 175, 0.841; 0.75: 136, 0.875; 0.80: 92, 0.914; 0.85: 47, 0.952; 0.90: 4, 0.984
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.426; 0.35: 500, 0.463; 0.40: 406, 0.499; 0.45: 310, 0.533; 0.50: 202, 0.565; 0.55: 91, 0.573; 0.60: 14, 0.614; 0.65: 1, 0.688
- **K=5**: model 1792540800, labels learned 119258, probability skill vs chance 0.2255, widened contest next: False
  - now: threshold 0.6751, hit rate recent 0.7979 / long run 0.8197
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.157, naive rule 0.380, lift 5.00x
    - 24h: 55 calls (55 a day), hit rate 0.818, chance 0.176, naive rule 0.417, lift 4.64x
    - 7d: 361 calls (52 a day), hit rate 0.812, chance 0.185, naive rule 0.402, lift 4.39x
    - 30d: 1562 calls (52 a day), hit rate 0.830, chance 0.188, naive rule 0.400, lift 4.42x
  - next: threshold 0.4197, hit rate recent 0.4709 / long run 0.4685
    - 6h: 33 calls (135 a day), hit rate 0.333, chance 0.157, lift 2.12x
    - 24h: 124 calls (125 a day), hit rate 0.476, chance 0.176, lift 2.70x
    - 7d: 940 calls (134 a day), hit rate 0.459, chance 0.185, lift 2.48x
    - 30d: 2840 calls (95 a day), hit rate 0.464, chance 0.188, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 417, 0.426; 0.35: 344, 0.495; 0.40: 276, 0.567; 0.45: 223, 0.623; 0.50: 176, 0.673; 0.55: 135, 0.712; 0.60: 104, 0.755; 0.65: 76, 0.792; 0.70: 53, 0.832; 0.75: 31, 0.875; 0.80: 10, 0.907
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.390; 0.35: 252, 0.422; 0.40: 158, 0.451; 0.45: 70, 0.463; 0.50: 15, 0.491; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 119255, probability skill vs chance 0.2035, widened contest next: False
  - now: threshold 0.5598, hit rate recent 0.6647 / long run 0.6818
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.116, naive rule 0.356, lift 7.20x
    - 24h: 55 calls (55 a day), hit rate 0.709, chance 0.122, naive rule 0.346, lift 5.81x
    - 7d: 332 calls (47 a day), hit rate 0.654, chance 0.116, naive rule 0.318, lift 5.64x
    - 30d: 1524 calls (51 a day), hit rate 0.701, chance 0.121, naive rule 0.330, lift 5.79x
  - next: threshold 0.3433, hit rate recent 0.3969 / long run 0.3776
    - 6h: 18 calls (74 a day), hit rate 0.389, chance 0.116, lift 3.36x
    - 24h: 86 calls (87 a day), hit rate 0.372, chance 0.122, lift 3.05x
    - 7d: 759 calls (109 a day), hit rate 0.375, chance 0.116, lift 3.24x
    - 30d: 2518 calls (84 a day), hit rate 0.383, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 249, 0.426; 0.35: 189, 0.496; 0.40: 145, 0.551; 0.45: 111, 0.596; 0.50: 84, 0.636; 0.55: 62, 0.676; 0.60: 41, 0.724; 0.65: 23, 0.791; 0.70: 10, 0.838; 0.75: 1, 0.829
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 175, 0.351; 0.35: 98, 0.378; 0.40: 36, 0.400; 0.45: 8, 0.436; 0.50: 1, 0.567
- **K=13**: model 1792800000, labels learned 119250, probability skill vs chance 0.1825, widened contest next: False
  - now: threshold 0.4112, hit rate recent 0.577 / long run 0.5574
    - 6h: 9 calls (38 a day), hit rate 0.889, chance 0.091, naive rule 0.372, lift 9.74x
    - 24h: 50 calls (51 a day), hit rate 0.640, chance 0.073, naive rule 0.273, lift 8.77x
    - 7d: 365 calls (52 a day), hit rate 0.529, chance 0.075, naive rule 0.270, lift 7.09x
    - 30d: 1560 calls (52 a day), hit rate 0.569, chance 0.077, naive rule 0.274, lift 7.35x
  - next: threshold 0.2903, hit rate recent 0.2949 / long run 0.3074
    - 6h: 16 calls (67 a day), hit rate 0.375, chance 0.091, lift 4.11x
    - 24h: 62 calls (63 a day), hit rate 0.274, chance 0.073, lift 3.76x
    - 7d: 480 calls (69 a day), hit rate 0.308, chance 0.075, lift 4.13x
    - 30d: 2171 calls (72 a day), hit rate 0.304, chance 0.077, lift 3.93x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 121, 0.447; 0.35: 87, 0.499; 0.40: 61, 0.553; 0.45: 41, 0.608; 0.50: 25, 0.662; 0.55: 15, 0.706; 0.60: 6, 0.755; 0.65: 2, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.315; 0.35: 13, 0.352; 0.40: 2, 0.429; 0.45: 0, 0.429

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.580 | 1.91% | 0.883 | 0.550 | 0.251 | 0.450 | 0.578 |
| 6h | 11.657 | 1.13% | 0.894 | 0.506 | 0.250 | 0.508 | 0.507 |
| 24h | 13.249 | 5.61% | 0.903 | 0.503 | 0.251 | 0.492 | 0.705 |
| 7d | 15.169 | 3.29% | 0.901 | 0.500 | 0.250 | 0.501 | 0.644 |
| 30d | 13.421 | 4.19% | 0.900 | 0.500 | 0.251 | 0.496 | 0.671 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.824 | 12.780 | 12.732 | 12.628 | 12.805 | 12.635 | 12.653 | 12.550 | 12.594 | 12.580 |
| 6h | 11.790 | 11.677 | 11.667 | 11.791 | 11.819 | 11.711 | 11.679 | 11.614 | 11.635 | 11.657 |
| 24h | 14.037 | 13.469 | 13.325 | 13.305 | 13.506 | 13.452 | 13.272 | 13.201 | 13.231 | 13.249 |
| 7d | 15.685 | 15.313 | 15.246 | 15.186 | 15.434 | 15.304 | 15.158 | 15.133 | 15.141 | 15.169 |
| 30d | 14.009 | 13.548 | 13.504 | 13.443 | 13.663 | 13.611 | 13.417 | 13.398 | 13.396 | 13.421 |

## Next candle

- candle starting 2026-10-24 23:46 UTC, last close 2355.68
- P(up) 0.5052, return quantiles (bp): {'05': -7.256, '10': -5.309, '25': -2.694, '40': -0.985, '50': 0.05, '60': 1.196, '75': 2.84, '90': 5.227, '95': 7.447}
- changepoint probability 0.7149, regime age 11.0 min
- agent weights: empirical 0.003, ewma 0.041, garch 0.156, har 0.114, bocpd 0.027, hmm 0.087, online_qr 0.173, lgbm 0.400

## Learning log

- 2026-10-22 12:00 UTC: {"garch": {"alpha": 0.0832, "beta": 0.8913}, "hmm": {"sd_bp": [3.89, 6.21, 16.2], "stay": [0.977, 0.963, 0.903]}}
- 2026-10-23 00:00 UTC: {"garch": {"alpha": 0.0768, "beta": 0.9004}, "hmm": {"sd_bp": [4.11, 6.6, 17.07], "stay": [0.981, 0.959, 0.884]}, "lgbm": {"challenger_loss": 0.2551, "champion_loss": 0.2552, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49591, "challengers": 1, "chance_loss": 0.61723, "widened": false, "champion_loss": 0.49471, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37764, "challengers": 1, "chance_loss": 0.48613, "widened": false, "champion_loss": 0.37429, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26615, "challengers": 1, "chance_loss": 0.35692, "widened": false, "champion_loss": 0.26465, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18908, "challengers": 3, "chance_loss": 0.26473, "widened": true, "champion_loss": 0.18972, "promoted": true}}
- 2026-10-23 12:00 UTC: {"garch": {"alpha": 0.0735, "beta": 0.9118}, "hmm": {"sd_bp": [4.3, 6.8, 17.27], "stay": [0.984, 0.956, 0.882]}}
- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- HMM volatility states (sd, bp per minute): [4.1, 7.07, 17.69], current probabilities: [0.784, 0.212, 0.003]
- live generator: {'versions': 60, 'latest_effective': '2026-10-24 23:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.397, 'l_abs': 0.657, 'l_hi': 0.766, 'l_lo': 0.769, 'b05': 0.719, 'b25': 0.697, 'b75': 0.612, 'b95': 0.691}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8]], 'cone_width': [1.472, 1.957, 2.175, 2.341, 2.729, 2.953, 3.293, 3.791, 4.004, 4.744, 5.066, 5.498, 5.717, 5.697]}
- calibration offsets (in sigma): {'05': 0.0725, '10': 0.095, '25': 0.0725, '40': 0.05, '50': 0.055, '60': 0.07, '75': 0.0075, '90': -0.065, '95': -0.0825}
