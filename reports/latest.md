# ETH-USD 60s candle generator - report

- generated: 2026-10-20 20:48 UTC
- last closed candle: 2026-10-20 20:48 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.604 (96) | 0.539 (672) [0.501, 0.576] | 0.525 (2876) [0.506, 0.545] | 0.514 (4602) [0.499, 0.529] | 0.520 (1630) [0.491, 0.548] | 0.482 (83) | 0.500 | flat +0.044 (noise 0.034) |
| colour_clear | 0.556 (806) | 0.548 (5555) [0.539, 0.557] | 0.524 (23366) [0.516, 0.533] | 0.514 (37413) [0.507, 0.520] | 0.545 (13175) [0.539, 0.550] | 0.584 (740) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.664 (152) | 0.602 (721) [0.575, 0.632] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.606 (165) | 0.500 | flat +0.013 (noise 0.026) |
| colour_next | 0.549 (1436) | 0.530 (10019) [0.521, 0.539] | 0.517 (42857) [0.511, 0.522] | 0.511 (68583) [0.506, 0.515] | 0.529 (24234) [0.523, 0.534] | 0.550 (1247) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140266) [0.499, 0.505] | 0.501 (599998) [0.500, 0.502] | 0.501 (960162) [0.500, 0.502] | 0.500 (339276) [0.498, 0.503] | 0.495 (17458) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.615 (39) | 0.611 (162) [0.575, 0.662] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.756 (41) | 0.500 | flat -0.041 (noise 0.048) |
| reversal_k13_next | 0.313 (83) | 0.300 (443) [0.284, 0.315] | 0.308 (2089) [0.295, 0.321] | 0.306 (3301) [0.295, 0.318] | 0.318 (1196) [0.306, 0.330] | 0.397 (63) | 0.077 | flat -0.029 (noise 0.030) |
| reversal_k13_now | 0.474 (57) | 0.535 (383) [0.499, 0.575] | 0.577 (1552) [0.557, 0.599] | 0.575 (2406) [0.558, 0.591] | 0.565 (934) [0.539, 0.593] | 0.523 (44) | 0.077 | flat -0.033 (noise 0.036) |
| reversal_k3_next | 0.547 (117) | 0.561 (780) [0.551, 0.573] | 0.576 (2618) [0.563, 0.589] | 0.581 (4081) [0.571, 0.592] | 0.572 (1641) [0.559, 0.588] | 0.528 (108) | 0.292 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.911 (56) | 0.938 (371) [0.912, 0.963] | 0.935 (1706) [0.927, 0.944] | 0.937 (2737) [0.930, 0.944] | 0.928 (974) [0.917, 0.939] | 0.920 (50) | 0.293 | flat +0.021 (noise 0.018) |
| reversal_k5_next | 0.440 (141) | 0.453 (853) [0.434, 0.476] | 0.470 (2467) [0.455, 0.486] | 0.476 (3660) [0.464, 0.490] | 0.456 (1670) [0.440, 0.474] | 0.400 (115) | 0.187 | flat -0.015 (noise 0.029) |
| reversal_k5_now | 0.821 (56) | 0.818 (351) [0.793, 0.841] | 0.828 (1605) [0.814, 0.842] | 0.831 (2513) [0.819, 0.843] | 0.820 (902) [0.802, 0.837] | 0.844 (45) | 0.187 | flat +0.014 (noise 0.029) |
| reversal_k8_next | 0.333 (114) | 0.365 (702) [0.339, 0.390] | 0.393 (2286) [0.376, 0.410] | 0.390 (3661) [0.377, 0.402] | 0.381 (1555) [0.362, 0.399] | 0.400 (95) | 0.121 | flat -0.024 (noise 0.027) |
| reversal_k8_now | 0.580 (50) | 0.672 (329) [0.637, 0.704] | 0.710 (1566) [0.690, 0.730] | 0.705 (2500) [0.689, 0.721] | 0.689 (913) [0.663, 0.715] | 0.657 (35) | 0.122 | flat +0.006 (noise 0.035) |
| overall | 0.504 (22310) | 0.505 (155169) [0.502, 0.507] | 0.504 (661620) [0.502, 0.505] | 0.503 (1058206) [0.502, 0.504] | 0.504 (374925) [0.502, 0.506] | 0.499 (19343) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06626, 0.09896] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.533, 'levels': [{'threshold': 0.06626, 'calls_per_day': 146.4, 'win_rate': 0.5771}, {'threshold': 0.09896, 'calls_per_day': 36.6, 'win_rate': 0.6473}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 24343, 'rate': 0.531}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15296 | 0.336 | 0.522 (15048) | 0.590 (1459) | 0.768 (2509) |
| volatility: normal | 15296 | 0.363 | 0.519 (15231) | 0.633 (624) | 0.766 (2244) |
| volatility: wild | 15296 | 0.378 | 0.509 (15258) | 0.613 (284) | 0.777 (2071) |
| session: Asia 00-08 | 15360 | 0.358 | 0.523 (15260) | 0.613 (864) | 0.770 (2280) |
| session: Europe 08-13 | 9600 | 0.354 | 0.518 (9515) | 0.599 (598) | 0.774 (1505) |
| session: US 13-21 | 15348 | 0.367 | 0.512 (15245) | 0.578 (585) | 0.776 (2209) |
| session: late 21-24 | 5580 | 0.350 | 0.513 (5517) | 0.637 (320) | 0.748 (830) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.392 | 0.361 | 0.271 | 0.271 | 0.567 | 0.276 | 0.508 | 1.214 |
| 6h | 360 | 0.369 | 0.366 | 0.286 | 0.340 | 0.511 | 0.250 | 0.487 | 1.268 |
| 24h | 1440 | 0.377 | 0.367 | 0.275 | 0.313 | 0.541 | 0.275 | 0.478 | 1.104 |
| 7d | 10080 | 0.369 | 0.359 | 0.277 | 0.311 | 0.533 | 0.267 | 0.472 | 1.203 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.518 | 0.253 | 0.466 | 1.295 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.392 / 0.567 / 0.900; 2: 0.352 / 0.450 / 1.000; 3: 0.373 / 0.533 / 0.950; 4: 0.388 / 0.583 / 1.000; 5: 0.364 / 0.433 / 1.000; 6: 0.367 / 0.517 / 1.000; 7: 0.356 / 0.483 / 1.000; 8: 0.353 / 0.483 / 1.000; 9: 0.377 / 0.483 / 1.000; 10: 0.365 / 0.500 / 0.933; 11: 0.393 / 0.583 / 0.933; 12: 0.353 / 0.483 / 0.967; 13: 0.344 / 0.467 / 0.967; 14: 0.391 / 0.533 / 0.983; 15: 0.361 / 0.483 / 0.983
- 6h: 1: 0.369 / 0.511 / 0.922; 2: 0.372 / 0.547 / 0.975; 3: 0.360 / 0.494 / 0.944; 4: 0.361 / 0.531 / 0.967; 5: 0.353 / 0.469 / 0.964; 6: 0.361 / 0.489 / 0.950; 7: 0.360 / 0.508 / 0.964; 8: 0.349 / 0.461 / 0.950; 9: 0.353 / 0.481 / 0.953; 10: 0.355 / 0.494 / 0.942; 11: 0.361 / 0.533 / 0.925; 12: 0.349 / 0.469 / 0.919; 13: 0.348 / 0.467 / 0.939; 14: 0.358 / 0.500 / 0.931; 15: 0.344 / 0.489 / 0.936
- 24h: 1: 0.377 / 0.541 / 0.898; 2: 0.368 / 0.523 / 0.900; 3: 0.362 / 0.510 / 0.895; 4: 0.357 / 0.494 / 0.895; 5: 0.357 / 0.486 / 0.897; 6: 0.355 / 0.477 / 0.900; 7: 0.354 / 0.486 / 0.897; 8: 0.355 / 0.504 / 0.899; 9: 0.357 / 0.491 / 0.903; 10: 0.358 / 0.502 / 0.897; 11: 0.360 / 0.516 / 0.897; 12: 0.357 / 0.504 / 0.897; 13: 0.352 / 0.485 / 0.897; 14: 0.355 / 0.490 / 0.903; 15: 0.345 / 0.473 / 0.897
- 7d: 1: 0.369 / 0.533 / 0.899; 2: 0.356 / 0.496 / 0.901; 3: 0.359 / 0.504 / 0.900; 4: 0.354 / 0.496 / 0.901; 5: 0.354 / 0.499 / 0.901; 6: 0.355 / 0.500 / 0.900; 7: 0.353 / 0.498 / 0.900; 8: 0.352 / 0.497 / 0.900; 9: 0.354 / 0.503 / 0.900; 10: 0.356 / 0.509 / 0.900; 11: 0.351 / 0.500 / 0.900; 12: 0.353 / 0.504 / 0.900; 13: 0.352 / 0.500 / 0.900; 14: 0.352 / 0.504 / 0.900; 15: 0.351 / 0.500 / 0.900
- 30d: 1: 0.360 / 0.518 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.497 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.495 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.118 (body 0.062, range 0.174); 'price stays where it was' would score 0.112; colour right 0.483; typical miss of the close 8.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.085, range 0.166); 'price stays where it was' would score 0.133; colour right 0.497; typical miss of the close 12.0 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.114 (body 0.076, range 0.151); 'price stays where it was' would score 0.114; colour right 0.507; typical miss of the close 10.7 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.132; colour right 0.500; typical miss of the close 9.3 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.9; 2: 0.196 / 4.5; 3: 0.163 / 6.1; 4: 0.132 / 6.6; 5: 0.119 / 7.4; 6: 0.109 / 7.8; 7: 0.103 / 8.2; 8: 0.095 / 8.5; 9: 0.086 / 8.5; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.077 / 10.2; 13: 0.065 / 10.5; 14: 0.067 / 10.7; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 113322, probability skill vs chance 0.2177, widened contest next: False
  - now: threshold 0.8354, hit rate recent 0.9159 / long run 0.9299
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.301, naive rule 0.467, lift 3.02x
    - 24h: 64 calls (64 a day), hit rate 0.906, chance 0.287, naive rule 0.469, lift 3.16x
    - 7d: 384 calls (55 a day), hit rate 0.930, chance 0.289, naive rule 0.478, lift 3.22x
    - 30d: 1706 calls (57 a day), hit rate 0.934, chance 0.292, naive rule 0.483, lift 3.20x
  - next: threshold 0.5247, hit rate recent 0.5351 / long run 0.5622
    - 6h: 24 calls (97 a day), hit rate 0.542, chance 0.301, lift 1.80x
    - 24h: 122 calls (122 a day), hit rate 0.566, chance 0.287, lift 1.97x
    - 7d: 732 calls (105 a day), hit rate 0.561, chance 0.289, lift 1.94x
    - 30d: 2646 calls (88 a day), hit rate 0.572, chance 0.292, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 541, 0.514; 0.40: 482, 0.567; 0.45: 413, 0.636; 0.50: 361, 0.689; 0.55: 316, 0.730; 0.60: 269, 0.774; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 138, 0.870; 0.80: 94, 0.911; 0.85: 48, 0.950; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 498, 0.461; 0.40: 406, 0.492; 0.45: 311, 0.524; 0.50: 201, 0.555; 0.55: 91, 0.570; 0.60: 14, 0.610; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 113320, probability skill vs chance 0.2095, widened contest next: True
  - now: threshold 0.6834, hit rate recent 0.8307 / long run 0.825
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.190, naive rule 0.386, lift 4.74x
    - 24h: 56 calls (56 a day), hit rate 0.821, chance 0.188, naive rule 0.398, lift 4.37x
    - 7d: 356 calls (51 a day), hit rate 0.823, chance 0.186, naive rule 0.397, lift 4.43x
    - 30d: 1589 calls (53 a day), hit rate 0.828, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.4183, hit rate recent 0.4044 / long run 0.4434
    - 6h: 26 calls (106 a day), hit rate 0.385, chance 0.190, lift 2.03x
    - 24h: 124 calls (125 a day), hit rate 0.411, chance 0.188, lift 2.19x
    - 7d: 870 calls (124 a day), hit rate 0.443, chance 0.186, lift 2.38x
    - 30d: 2496 calls (83 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 348, 0.488; 0.40: 280, 0.558; 0.45: 227, 0.615; 0.50: 179, 0.663; 0.55: 137, 0.708; 0.60: 107, 0.750; 0.65: 79, 0.789; 0.70: 57, 0.822; 0.75: 32, 0.864; 0.80: 10, 0.889
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 250, 0.417; 0.40: 157, 0.443; 0.45: 73, 0.459; 0.50: 17, 0.495; 0.55: 2, 0.500
- **K=8**: model 1792454400, labels learned 113317, probability skill vs chance 0.1979, widened contest next: True
  - now: threshold 0.5692, hit rate recent 0.6392 / long run 0.6863
    - 6h: 6 calls (25 a day), hit rate 0.833, chance 0.111, naive rule 0.295, lift 7.48x
    - 24h: 47 calls (47 a day), hit rate 0.638, chance 0.117, naive rule 0.322, lift 5.43x
    - 7d: 326 calls (47 a day), hit rate 0.669, chance 0.119, naive rule 0.321, lift 5.64x
    - 30d: 1554 calls (52 a day), hit rate 0.705, chance 0.122, naive rule 0.328, lift 5.80x
  - next: threshold 0.3506, hit rate recent 0.3946 / long run 0.3757
    - 6h: 16 calls (66 a day), hit rate 0.375, chance 0.111, lift 3.37x
    - 24h: 105 calls (106 a day), hit rate 0.390, chance 0.117, lift 3.32x
    - 7d: 723 calls (103 a day), hit rate 0.364, chance 0.119, lift 3.07x
    - 30d: 2328 calls (78 a day), hit rate 0.388, chance 0.122, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 255, 0.420; 0.35: 194, 0.490; 0.40: 148, 0.547; 0.45: 116, 0.590; 0.50: 88, 0.633; 0.55: 64, 0.679; 0.60: 43, 0.722; 0.65: 24, 0.780; 0.70: 10, 0.828; 0.75: 1, 0.821
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.349; 0.35: 102, 0.379; 0.40: 40, 0.405; 0.45: 8, 0.425; 0.50: 1, 0.471
- **K=13**: model 1792454400, labels learned 113312, probability skill vs chance 0.1876, widened contest next: True
  - now: threshold 0.4298, hit rate recent 0.5003 / long run 0.5541
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.087, naive rule 0.314, lift 6.57x
    - 24h: 59 calls (60 a day), hit rate 0.492, chance 0.074, naive rule 0.254, lift 6.67x
    - 7d: 392 calls (56 a day), hit rate 0.520, chance 0.077, naive rule 0.271, lift 6.78x
    - 30d: 1550 calls (52 a day), hit rate 0.570, chance 0.078, naive rule 0.272, lift 7.34x
  - next: threshold 0.2755, hit rate recent 0.3671 / long run 0.3187
    - 6h: 13 calls (54 a day), hit rate 0.462, chance 0.087, lift 5.31x
    - 24h: 72 calls (73 a day), hit rate 0.389, chance 0.074, lift 5.28x
    - 7d: 439 calls (63 a day), hit rate 0.317, chance 0.077, lift 4.12x
    - 30d: 2112 calls (70 a day), hit rate 0.309, chance 0.078, lift 3.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.450; 0.35: 86, 0.504; 0.40: 61, 0.553; 0.45: 41, 0.608; 0.50: 25, 0.655; 0.55: 14, 0.708; 0.60: 5, 0.748; 0.65: 1, 0.844
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.320; 0.35: 13, 0.354; 0.40: 2, 0.433

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.725 | 3.31% | 0.900 | 0.500 | 0.252 | 0.500 | 0.203 |
| 6h | 19.502 | 2.74% | 0.908 | 0.556 | 0.251 | 0.506 | 0.625 |
| 24h | 17.243 | 3.21% | 0.892 | 0.502 | 0.251 | 0.505 | 0.655 |
| 7d | 16.239 | 4.29% | 0.900 | 0.501 | 0.251 | 0.494 | 0.652 |
| 30d | 13.897 | 4.04% | 0.900 | 0.500 | 0.251 | 0.496 | 0.676 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.126 | 11.841 | 11.848 | 11.838 | 11.996 | 12.047 | 11.598 | 11.701 | 11.699 | 11.725 |
| 6h | 20.052 | 19.593 | 19.453 | 19.472 | 19.822 | 19.687 | 19.371 | 19.328 | 19.379 | 19.502 |
| 24h | 17.816 | 17.323 | 17.256 | 17.235 | 17.461 | 17.362 | 17.243 | 17.193 | 17.196 | 17.243 |
| 7d | 16.968 | 16.419 | 16.324 | 16.250 | 16.484 | 16.443 | 16.237 | 16.218 | 16.207 | 16.239 |
| 30d | 14.482 | 14.022 | 13.983 | 13.920 | 14.145 | 14.085 | 13.894 | 13.872 | 13.871 | 13.897 |

## Next candle

- candle starting 2026-10-20 20:48 UTC, last close 2442.32
- P(up) 0.5099, return quantiles (bp): {'05': -7.354, '10': -5.469, '25': -2.614, '40': -0.788, '50': 0.084, '60': 0.992, '75': 3.066, '90': 5.673, '95': 7.409}
- changepoint probability 0.0406, regime age 157.2 min
- agent weights: empirical 0.004, ewma 0.093, garch 0.169, har 0.185, bocpd 0.039, hmm 0.052, online_qr 0.186, lgbm 0.272

## Learning log

- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.79, 15.89], current probabilities: [0.104, 0.886, 0.01]
- live generator: {'versions': 60, 'latest_effective': '2026-10-20 21:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.209, 'l_abs': 0.718, 'l_hi': 0.8, 'l_lo': 0.794, 'b05': 0.713, 'b25': 0.667, 'b75': 0.694, 'b95': 0.712}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.3, 1.661, 1.846, 2.11, 2.459, 2.609, 2.909, 3.03, 3.2, 3.431, 3.591, 3.598, 3.742, 3.729]}
- calibration offsets (in sigma): {'05': 0.0135, '10': 0.027, '25': 0.0475, '40': 0.048, '50': 0.015, '60': -0.028, '75': 0.0225, '90': 0.013, '95': -0.0135}
