# ETH-USD 60s candle generator - report

- generated: 2026-10-20 12:28 UTC
- last closed candle: 2026-10-20 12:28 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.604 (96) | 0.539 (672) [0.501, 0.576] | 0.525 (2876) [0.506, 0.545] | 0.514 (4602) [0.499, 0.529] | 0.520 (1630) [0.491, 0.548] | 0.449 (49) | 0.500 | flat +0.044 (noise 0.034) |
| colour_clear | 0.556 (806) | 0.548 (5555) [0.539, 0.557] | 0.524 (23366) [0.516, 0.533] | 0.514 (37413) [0.507, 0.520] | 0.545 (13175) [0.539, 0.550] | 0.605 (471) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.664 (152) | 0.602 (721) [0.575, 0.632] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.680 (100) | 0.500 | flat +0.013 (noise 0.026) |
| colour_next | 0.549 (1436) | 0.530 (10019) [0.521, 0.539] | 0.517 (42857) [0.511, 0.522] | 0.511 (68583) [0.506, 0.515] | 0.529 (24234) [0.523, 0.534] | 0.570 (747) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140266) [0.499, 0.505] | 0.501 (599998) [0.500, 0.502] | 0.501 (960162) [0.500, 0.502] | 0.500 (339276) [0.498, 0.503] | 0.497 (10458) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.615 (39) | 0.611 (162) [0.575, 0.662] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.875 (24) | 0.500 | flat -0.041 (noise 0.048) |
| reversal_k13_next | 0.313 (83) | 0.300 (443) [0.284, 0.315] | 0.308 (2089) [0.295, 0.321] | 0.306 (3301) [0.295, 0.318] | 0.318 (1196) [0.306, 0.330] | 0.444 (36) | 0.077 | flat -0.029 (noise 0.030) |
| reversal_k13_now | 0.474 (57) | 0.535 (383) [0.499, 0.575] | 0.577 (1552) [0.557, 0.599] | 0.575 (2406) [0.558, 0.591] | 0.565 (934) [0.539, 0.593] | 0.500 (30) | 0.077 | flat -0.033 (noise 0.036) |
| reversal_k3_next | 0.547 (117) | 0.561 (780) [0.551, 0.573] | 0.576 (2618) [0.563, 0.589] | 0.581 (4081) [0.571, 0.592] | 0.572 (1641) [0.559, 0.588] | 0.557 (70) | 0.292 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.911 (56) | 0.938 (371) [0.912, 0.963] | 0.935 (1706) [0.927, 0.944] | 0.937 (2737) [0.930, 0.944] | 0.928 (974) [0.917, 0.939] | 0.939 (33) | 0.293 | flat +0.021 (noise 0.018) |
| reversal_k5_next | 0.440 (141) | 0.453 (853) [0.434, 0.476] | 0.470 (2467) [0.455, 0.486] | 0.476 (3660) [0.464, 0.490] | 0.456 (1670) [0.440, 0.474] | 0.414 (70) | 0.187 | flat -0.015 (noise 0.029) |
| reversal_k5_now | 0.821 (56) | 0.818 (351) [0.793, 0.841] | 0.828 (1605) [0.814, 0.842] | 0.831 (2513) [0.819, 0.843] | 0.820 (902) [0.802, 0.837] | 0.800 (30) | 0.187 | flat +0.014 (noise 0.029) |
| reversal_k8_next | 0.333 (114) | 0.365 (702) [0.339, 0.390] | 0.393 (2286) [0.376, 0.410] | 0.390 (3661) [0.377, 0.402] | 0.381 (1555) [0.362, 0.399] | 0.406 (64) | 0.121 | flat -0.024 (noise 0.027) |
| reversal_k8_now | 0.580 (50) | 0.672 (329) [0.637, 0.704] | 0.710 (1566) [0.690, 0.730] | 0.705 (2500) [0.689, 0.721] | 0.689 (913) [0.663, 0.715] | 0.636 (22) | 0.122 | flat +0.006 (noise 0.035) |
| overall | 0.504 (22310) | 0.505 (155169) [0.502, 0.507] | 0.504 (661620) [0.502, 0.505] | 0.503 (1058206) [0.502, 0.504] | 0.504 (374925) [0.502, 0.506] | 0.503 (11609) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06589, 0.09829] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5328, 'levels': [{'threshold': 0.06589, 'calls_per_day': 146.1, 'win_rate': 0.5821}, {'threshold': 0.09829, 'calls_per_day': 36.5, 'win_rate': 0.6537}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 23843, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15130 | 0.336 | 0.523 (14882) | 0.592 (1448) | 0.768 (2487) |
| volatility: normal | 15129 | 0.363 | 0.519 (15065) | 0.627 (612) | 0.764 (2233) |
| volatility: wild | 15129 | 0.378 | 0.510 (15090) | 0.649 (242) | 0.779 (2045) |
| session: Asia 00-08 | 15360 | 0.358 | 0.523 (15260) | 0.613 (864) | 0.770 (2280) |
| session: Europe 08-13 | 9568 | 0.353 | 0.518 (9483) | 0.597 (595) | 0.774 (1494) |
| session: US 13-21 | 14880 | 0.367 | 0.512 (14777) | 0.591 (523) | 0.776 (2161) |
| session: late 21-24 | 5580 | 0.350 | 0.513 (5517) | 0.637 (320) | 0.748 (830) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.344 | 0.326 | 0.237 | 0.237 | 0.533 | 0.260 | 0.429 | 1.042 |
| 6h | 360 | 0.373 | 0.360 | 0.254 | 0.289 | 0.563 | 0.289 | 0.458 | 0.997 |
| 24h | 1440 | 0.376 | 0.369 | 0.273 | 0.309 | 0.551 | 0.276 | 0.477 | 1.103 |
| 7d | 10080 | 0.369 | 0.359 | 0.277 | 0.310 | 0.534 | 0.267 | 0.472 | 1.201 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.518 | 0.253 | 0.466 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.344 / 0.533 / 0.817; 2: 0.340 / 0.517 / 0.683; 3: 0.318 / 0.500 / 0.717; 4: 0.315 / 0.500 / 0.600; 5: 0.338 / 0.517 / 0.617; 6: 0.319 / 0.550 / 0.700; 7: 0.316 / 0.467 / 0.583; 8: 0.313 / 0.550 / 0.633; 9: 0.317 / 0.483 / 0.683; 10: 0.340 / 0.600 / 0.717; 11: 0.345 / 0.600 / 0.800; 12: 0.302 / 0.450 / 0.817; 13: 0.286 / 0.400 / 0.833; 14: 0.306 / 0.433 / 0.883; 15: 0.305 / 0.417 / 0.867
- 6h: 1: 0.373 / 0.563 / 0.889; 2: 0.362 / 0.540 / 0.797; 3: 0.366 / 0.563 / 0.850; 4: 0.351 / 0.476 / 0.808; 5: 0.354 / 0.496 / 0.814; 6: 0.349 / 0.493 / 0.853; 7: 0.348 / 0.485 / 0.831; 8: 0.348 / 0.515 / 0.836; 9: 0.352 / 0.504 / 0.836; 10: 0.353 / 0.496 / 0.847; 11: 0.354 / 0.515 / 0.875; 12: 0.348 / 0.485 / 0.892; 13: 0.350 / 0.499 / 0.872; 14: 0.349 / 0.493 / 0.892; 15: 0.352 / 0.471 / 0.900
- 24h: 1: 0.376 / 0.551 / 0.900; 2: 0.364 / 0.508 / 0.890; 3: 0.363 / 0.508 / 0.898; 4: 0.356 / 0.484 / 0.888; 5: 0.354 / 0.476 / 0.893; 6: 0.356 / 0.483 / 0.907; 7: 0.351 / 0.481 / 0.900; 8: 0.358 / 0.510 / 0.906; 9: 0.359 / 0.492 / 0.909; 10: 0.361 / 0.511 / 0.907; 11: 0.356 / 0.500 / 0.915; 12: 0.360 / 0.517 / 0.919; 13: 0.355 / 0.489 / 0.917; 14: 0.361 / 0.505 / 0.926; 15: 0.348 / 0.466 / 0.920
- 7d: 1: 0.369 / 0.534 / 0.899; 2: 0.355 / 0.493 / 0.897; 3: 0.359 / 0.505 / 0.898; 4: 0.354 / 0.495 / 0.897; 5: 0.355 / 0.500 / 0.897; 6: 0.355 / 0.501 / 0.898; 7: 0.353 / 0.498 / 0.898; 8: 0.353 / 0.500 / 0.898; 9: 0.355 / 0.504 / 0.898; 10: 0.357 / 0.510 / 0.898; 11: 0.351 / 0.499 / 0.899; 12: 0.354 / 0.506 / 0.900; 13: 0.353 / 0.503 / 0.899; 14: 0.352 / 0.503 / 0.900; 15: 0.352 / 0.502 / 0.900
- 30d: 1: 0.360 / 0.518 / 0.899; 2: 0.351 / 0.496 / 0.899; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.497 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.502 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.499 / 0.900; 12: 0.348 / 0.504 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.066 (body 0.042, range 0.089); 'price stays where it was' would score 0.076; colour right 0.367; typical miss of the close 11.4 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.113 (body 0.074, range 0.153); 'price stays where it was' would score 0.108; colour right 0.451; typical miss of the close 10.3 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.114 (body 0.074, range 0.155); 'price stays where it was' would score 0.117; colour right 0.507; typical miss of the close 10.4 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.126 (body 0.085, range 0.167); 'price stays where it was' would score 0.132; colour right 0.499; typical miss of the close 9.2 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.0; 2: 0.195 / 4.5; 3: 0.163 / 6.1; 4: 0.132 / 6.6; 5: 0.119 / 7.3; 6: 0.108 / 7.8; 7: 0.103 / 8.2; 8: 0.096 / 8.5; 9: 0.086 / 8.6; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.077 / 10.2; 13: 0.065 / 10.4; 14: 0.066 / 10.7; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 112822, probability skill vs chance 0.2225, widened contest next: False
  - now: threshold 0.8355, hit rate recent 0.9254 / long run 0.9312
    - 6h: 16 calls (65 a day), hit rate 1.000, chance 0.293, naive rule 0.488, lift 3.41x
    - 24h: 63 calls (63 a day), hit rate 0.905, chance 0.279, naive rule 0.461, lift 3.24x
    - 7d: 385 calls (55 a day), hit rate 0.935, chance 0.288, naive rule 0.478, lift 3.25x
    - 30d: 1709 calls (57 a day), hit rate 0.934, chance 0.291, naive rule 0.483, lift 3.21x
  - next: threshold 0.5328, hit rate recent 0.5813 / long run 0.5679
    - 6h: 36 calls (146 a day), hit rate 0.611, chance 0.293, lift 2.09x
    - 24h: 119 calls (119 a day), hit rate 0.563, chance 0.279, lift 2.01x
    - 7d: 760 calls (109 a day), hit rate 0.563, chance 0.288, lift 1.96x
    - 30d: 2639 calls (88 a day), hit rate 0.574, chance 0.291, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.514; 0.40: 482, 0.567; 0.45: 413, 0.636; 0.50: 361, 0.688; 0.55: 316, 0.730; 0.60: 269, 0.773; 0.65: 225, 0.802; 0.70: 179, 0.834; 0.75: 139, 0.870; 0.80: 94, 0.910; 0.85: 48, 0.950; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 498, 0.461; 0.40: 406, 0.492; 0.45: 311, 0.524; 0.50: 202, 0.555; 0.55: 91, 0.572; 0.60: 14, 0.609; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 112820, probability skill vs chance 0.2146, widened contest next: False
  - now: threshold 0.6828, hit rate recent 0.8025 / long run 0.8222
    - 6h: 14 calls (57 a day), hit rate 0.786, chance 0.195, naive rule 0.436, lift 4.02x
    - 24h: 58 calls (58 a day), hit rate 0.793, chance 0.178, naive rule 0.380, lift 4.46x
    - 7d: 357 calls (51 a day), hit rate 0.818, chance 0.185, naive rule 0.394, lift 4.42x
    - 30d: 1599 calls (53 a day), hit rate 0.826, chance 0.187, naive rule 0.393, lift 4.41x
  - next: threshold 0.4168, hit rate recent 0.4376 / long run 0.4485
    - 6h: 34 calls (139 a day), hit rate 0.441, chance 0.195, lift 2.26x
    - 24h: 130 calls (131 a day), hit rate 0.423, chance 0.178, lift 2.38x
    - 7d: 872 calls (125 a day), hit rate 0.445, chance 0.185, lift 2.40x
    - 30d: 2479 calls (83 a day), hit rate 0.468, chance 0.187, lift 2.50x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 348, 0.487; 0.40: 280, 0.558; 0.45: 228, 0.614; 0.50: 180, 0.662; 0.55: 137, 0.707; 0.60: 107, 0.748; 0.65: 80, 0.788; 0.70: 58, 0.820; 0.75: 32, 0.863; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.418; 0.40: 158, 0.444; 0.45: 73, 0.460; 0.50: 18, 0.498; 0.55: 2, 0.549
- **K=8**: model 1792454400, labels learned 112817, probability skill vs chance 0.2008, widened contest next: True
  - now: threshold 0.5692, hit rate recent 0.6243 / long run 0.6861
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.133, naive rule 0.397, lift 4.18x
    - 24h: 54 calls (54 a day), hit rate 0.574, chance 0.117, naive rule 0.309, lift 4.89x
    - 7d: 328 calls (47 a day), hit rate 0.668, chance 0.119, naive rule 0.321, lift 5.61x
    - 30d: 1563 calls (52 a day), hit rate 0.706, chance 0.122, naive rule 0.328, lift 5.80x
  - next: threshold 0.3461, hit rate recent 0.409 / long run 0.3752
    - 6h: 31 calls (128 a day), hit rate 0.516, chance 0.133, lift 3.88x
    - 24h: 116 calls (117 a day), hit rate 0.345, chance 0.117, lift 2.94x
    - 7d: 723 calls (103 a day), hit rate 0.364, chance 0.119, lift 3.06x
    - 30d: 2322 calls (77 a day), hit rate 0.391, chance 0.122, lift 3.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.420; 0.35: 194, 0.491; 0.40: 148, 0.547; 0.45: 116, 0.589; 0.50: 89, 0.630; 0.55: 65, 0.678; 0.60: 43, 0.723; 0.65: 24, 0.783; 0.70: 10, 0.829; 0.75: 1, 0.793
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.350; 0.35: 103, 0.381; 0.40: 41, 0.410; 0.45: 8, 0.438; 0.50: 1, 0.471
- **K=13**: model 1792454400, labels learned 112812, probability skill vs chance 0.1829, widened contest next: True
  - now: threshold 0.424, hit rate recent 0.481 / long run 0.5537
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.074, naive rule 0.266, lift 5.80x
    - 24h: 65 calls (66 a day), hit rate 0.462, chance 0.075, naive rule 0.248, lift 6.18x
    - 7d: 390 calls (56 a day), hit rate 0.523, chance 0.077, naive rule 0.270, lift 6.81x
    - 30d: 1557 calls (52 a day), hit rate 0.572, chance 0.078, naive rule 0.271, lift 7.37x
  - next: threshold 0.2758, hit rate recent 0.3789 / long run 0.318
    - 6h: 17 calls (71 a day), hit rate 0.529, chance 0.074, lift 7.16x
    - 24h: 71 calls (72 a day), hit rate 0.380, chance 0.075, lift 5.09x
    - 7d: 435 calls (62 a day), hit rate 0.317, chance 0.077, lift 4.13x
    - 30d: 2104 calls (70 a day), hit rate 0.311, chance 0.078, lift 4.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.450; 0.35: 86, 0.504; 0.40: 61, 0.553; 0.45: 41, 0.609; 0.50: 25, 0.655; 0.55: 14, 0.709; 0.60: 5, 0.745; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.322; 0.35: 13, 0.360; 0.40: 2, 0.433

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 17.114 | -0.45% | 0.817 | 0.500 | 0.253 | 0.450 | 0.333 |
| 6h | 14.371 | 0.56% | 0.894 | 0.469 | 0.251 | 0.504 | 0.281 |
| 24h | 16.074 | 2.35% | 0.899 | 0.489 | 0.250 | 0.510 | 0.583 |
| 7d | 15.928 | 4.12% | 0.900 | 0.499 | 0.251 | 0.493 | 0.644 |
| 30d | 13.825 | 3.99% | 0.900 | 0.500 | 0.251 | 0.495 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.038 | 17.237 | 17.118 | 17.077 | 17.236 | 17.184 | 17.173 | 17.052 | 17.098 | 17.114 |
| 6h | 14.453 | 14.424 | 14.394 | 14.445 | 14.471 | 14.426 | 14.389 | 14.347 | 14.366 | 14.371 |
| 24h | 16.461 | 16.214 | 16.177 | 16.091 | 16.376 | 16.202 | 16.070 | 16.046 | 16.052 | 16.074 |
| 7d | 16.612 | 16.102 | 16.018 | 15.941 | 16.173 | 16.130 | 15.922 | 15.908 | 15.897 | 15.928 |
| 30d | 14.400 | 13.948 | 13.911 | 13.849 | 14.072 | 14.011 | 13.821 | 13.800 | 13.799 | 13.825 |

## Next candle

- candle starting 2026-10-20 12:28 UTC, last close 2390.03
- P(up) 0.4893, return quantiles (bp): {'05': -10.812, '10': -8.554, '25': -5.03, '40': -2.054, '50': -0.168, '60': 1.42, '75': 4.644, '90': 8.807, '95': 11.626}
- changepoint probability 0.0867, regime age 63.6 min
- agent weights: empirical 0.042, ewma 0.105, garch 0.134, har 0.150, bocpd 0.041, hmm 0.098, online_qr 0.186, lgbm 0.245

## Learning log

- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.79, 15.89], current probabilities: [0.006, 0.791, 0.203]
- live generator: {'versions': 60, 'latest_effective': '2026-10-20 12:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.195, 'l_abs': 0.736, 'l_hi': 0.814, 'l_lo': 0.783, 'b05': 0.723, 'b25': 0.696, 'b75': 0.747, 'b95': 0.723}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [2.417, 2.154, 3.044, 3.342, 2.773, 3.452, 3.482, 3.628, 3.537, 3.105, 2.94, 3.389, 3.125, 3.053]}
- calibration offsets (in sigma): {'05': 0.0535, '10': -0.023, '25': -0.0925, '40': -0.052, '50': 0.005, '60': 0.012, '75': 0.0925, '90': 0.063, '95': 0.0265}
