# ETH-USD 60s candle generator - report

- generated: 2026-10-20 23:30 UTC
- last closed candle: 2026-10-20 23:30 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.604 (96) | 0.539 (672) [0.501, 0.576] | 0.525 (2876) [0.506, 0.545] | 0.514 (4602) [0.499, 0.529] | 0.520 (1630) [0.491, 0.548] | 0.479 (94) | 0.500 | flat +0.044 (noise 0.034) |
| colour_clear | 0.556 (806) | 0.548 (5555) [0.539, 0.557] | 0.524 (23366) [0.516, 0.533] | 0.514 (37413) [0.507, 0.520] | 0.545 (13175) [0.539, 0.550] | 0.580 (834) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.664 (152) | 0.602 (721) [0.575, 0.632] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.582 (201) | 0.500 | flat +0.013 (noise 0.026) |
| colour_next | 0.549 (1436) | 0.530 (10019) [0.521, 0.539] | 0.517 (42857) [0.511, 0.522] | 0.511 (68583) [0.506, 0.515] | 0.529 (24234) [0.523, 0.534] | 0.551 (1409) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140266) [0.499, 0.505] | 0.501 (599998) [0.500, 0.502] | 0.501 (960162) [0.500, 0.502] | 0.500 (339276) [0.498, 0.503] | 0.493 (19726) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.615 (39) | 0.611 (162) [0.575, 0.662] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.698 (53) | 0.500 | flat -0.041 (noise 0.048) |
| reversal_k13_next | 0.313 (83) | 0.300 (443) [0.284, 0.315] | 0.308 (2089) [0.295, 0.321] | 0.306 (3301) [0.295, 0.318] | 0.318 (1196) [0.306, 0.330] | 0.351 (74) | 0.077 | flat -0.029 (noise 0.030) |
| reversal_k13_now | 0.474 (57) | 0.535 (383) [0.499, 0.575] | 0.577 (1552) [0.557, 0.599] | 0.575 (2406) [0.558, 0.591] | 0.565 (934) [0.539, 0.593] | 0.500 (50) | 0.077 | flat -0.033 (noise 0.036) |
| reversal_k3_next | 0.547 (117) | 0.561 (780) [0.551, 0.573] | 0.576 (2618) [0.563, 0.589] | 0.581 (4081) [0.571, 0.592] | 0.572 (1641) [0.559, 0.588] | 0.529 (121) | 0.292 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.911 (56) | 0.938 (371) [0.912, 0.963] | 0.935 (1706) [0.927, 0.944] | 0.937 (2737) [0.930, 0.944] | 0.928 (974) [0.917, 0.939] | 0.911 (56) | 0.293 | flat +0.021 (noise 0.018) |
| reversal_k5_next | 0.440 (141) | 0.453 (853) [0.434, 0.476] | 0.470 (2467) [0.455, 0.486] | 0.476 (3660) [0.464, 0.490] | 0.456 (1670) [0.440, 0.474] | 0.383 (128) | 0.187 | flat -0.015 (noise 0.029) |
| reversal_k5_now | 0.821 (56) | 0.818 (351) [0.793, 0.841] | 0.828 (1605) [0.814, 0.842] | 0.831 (2513) [0.819, 0.843] | 0.820 (902) [0.802, 0.837] | 0.837 (49) | 0.187 | flat +0.014 (noise 0.029) |
| reversal_k8_next | 0.333 (114) | 0.365 (702) [0.339, 0.390] | 0.393 (2286) [0.376, 0.410] | 0.390 (3661) [0.377, 0.402] | 0.381 (1555) [0.362, 0.399] | 0.380 (108) | 0.121 | flat -0.024 (noise 0.027) |
| reversal_k8_now | 0.580 (50) | 0.672 (329) [0.637, 0.704] | 0.710 (1566) [0.690, 0.730] | 0.705 (2500) [0.689, 0.721] | 0.689 (913) [0.663, 0.715] | 0.610 (41) | 0.122 | flat +0.006 (noise 0.035) |
| overall | 0.504 (22310) | 0.505 (155169) [0.502, 0.507] | 0.504 (661620) [0.502, 0.505] | 0.503 (1058206) [0.502, 0.504] | 0.504 (374925) [0.502, 0.506] | 0.497 (21856) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06626, 0.09896] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.533, 'levels': [{'threshold': 0.06626, 'calls_per_day': 146.4, 'win_rate': 0.5771}, {'threshold': 0.09896, 'calls_per_day': 36.6, 'win_rate': 0.6473}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 24505, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15350 | 0.336 | 0.522 (15102) | 0.589 (1468) | 0.768 (2515) |
| volatility: normal | 15350 | 0.363 | 0.520 (15286) | 0.627 (651) | 0.764 (2260) |
| volatility: wild | 15350 | 0.378 | 0.509 (15311) | 0.613 (284) | 0.777 (2071) |
| session: Asia 00-08 | 15360 | 0.358 | 0.523 (15260) | 0.613 (864) | 0.770 (2280) |
| session: Europe 08-13 | 9600 | 0.354 | 0.518 (9515) | 0.599 (598) | 0.774 (1505) |
| session: US 13-21 | 15360 | 0.367 | 0.512 (15257) | 0.576 (587) | 0.774 (2215) |
| session: late 21-24 | 5730 | 0.350 | 0.514 (5667) | 0.624 (354) | 0.748 (846) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.341 | 0.328 | 0.288 | 0.288 | 0.417 | 0.212 | 0.470 | 1.080 |
| 6h | 360 | 0.365 | 0.357 | 0.272 | 0.323 | 0.533 | 0.253 | 0.477 | 1.196 |
| 24h | 1440 | 0.379 | 0.367 | 0.273 | 0.314 | 0.549 | 0.279 | 0.480 | 1.078 |
| 7d | 10080 | 0.370 | 0.359 | 0.277 | 0.311 | 0.535 | 0.267 | 0.472 | 1.201 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.518 | 0.253 | 0.466 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.341 / 0.417 / 0.867; 2: 0.361 / 0.517 / 0.833; 3: 0.345 / 0.450 / 0.883; 4: 0.367 / 0.550 / 0.867; 5: 0.329 / 0.433 / 0.867; 6: 0.346 / 0.417 / 0.867; 7: 0.348 / 0.467 / 0.850; 8: 0.369 / 0.500 / 0.867; 9: 0.346 / 0.450 / 0.867; 10: 0.371 / 0.617 / 0.817; 11: 0.341 / 0.500 / 0.867; 12: 0.338 / 0.467 / 0.883; 13: 0.352 / 0.483 / 0.867; 14: 0.349 / 0.467 / 0.833; 15: 0.331 / 0.400 / 0.833
- 6h: 1: 0.365 / 0.533 / 0.903; 2: 0.367 / 0.536 / 0.928; 3: 0.347 / 0.456 / 0.922; 4: 0.371 / 0.558 / 0.942; 5: 0.339 / 0.428 / 0.942; 6: 0.350 / 0.456 / 0.942; 7: 0.354 / 0.500 / 0.933; 8: 0.347 / 0.464 / 0.933; 9: 0.347 / 0.469 / 0.928; 10: 0.351 / 0.497 / 0.908; 11: 0.352 / 0.519 / 0.919; 12: 0.339 / 0.453 / 0.928; 13: 0.344 / 0.461 / 0.919; 14: 0.357 / 0.503 / 0.908; 15: 0.347 / 0.497 / 0.917
- 24h: 1: 0.379 / 0.549 / 0.896; 2: 0.369 / 0.524 / 0.899; 3: 0.360 / 0.498 / 0.906; 4: 0.363 / 0.504 / 0.905; 5: 0.354 / 0.480 / 0.901; 6: 0.355 / 0.473 / 0.899; 7: 0.356 / 0.488 / 0.899; 8: 0.352 / 0.488 / 0.899; 9: 0.356 / 0.491 / 0.897; 10: 0.358 / 0.508 / 0.892; 11: 0.358 / 0.512 / 0.896; 12: 0.356 / 0.497 / 0.896; 13: 0.352 / 0.481 / 0.895; 14: 0.353 / 0.482 / 0.892; 15: 0.347 / 0.480 / 0.890
- 7d: 1: 0.370 / 0.535 / 0.899; 2: 0.356 / 0.496 / 0.900; 3: 0.359 / 0.503 / 0.900; 4: 0.354 / 0.497 / 0.900; 5: 0.354 / 0.497 / 0.900; 6: 0.354 / 0.498 / 0.900; 7: 0.353 / 0.498 / 0.899; 8: 0.352 / 0.496 / 0.899; 9: 0.354 / 0.502 / 0.900; 10: 0.356 / 0.509 / 0.899; 11: 0.351 / 0.500 / 0.899; 12: 0.353 / 0.504 / 0.899; 13: 0.352 / 0.499 / 0.899; 14: 0.352 / 0.504 / 0.899; 15: 0.351 / 0.502 / 0.899
- 30d: 1: 0.360 / 0.518 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.508 / 0.900; 4: 0.350 / 0.497 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.350 / 0.501 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.495 / 0.900; 10: 0.349 / 0.505 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.085 (body 0.063, range 0.107); 'price stays where it was' would score 0.139; colour right 0.550; typical miss of the close 10.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.107 (body 0.071, range 0.144); 'price stays where it was' would score 0.119; colour right 0.514; typical miss of the close 10.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.113 (body 0.076, range 0.151); 'price stays where it was' would score 0.114; colour right 0.511; typical miss of the close 11.3 bp; chain ended on the right side 0.479 of 96 chains; n=1440
- 7d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.132; colour right 0.501; typical miss of the close 9.4 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.9 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.9; 2: 0.196 / 4.5; 3: 0.164 / 6.1; 4: 0.132 / 6.6; 5: 0.119 / 7.4; 6: 0.109 / 7.8; 7: 0.103 / 8.2; 8: 0.096 / 8.5; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.077 / 10.2; 13: 0.066 / 10.5; 14: 0.066 / 10.7; 15: 0.058 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 113484, probability skill vs chance 0.2197, widened contest next: False
  - now: threshold 0.8354, hit rate recent 0.9087 / long run 0.9289
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.296, naive rule 0.477, lift 2.86x
    - 24h: 59 calls (59 a day), hit rate 0.881, chance 0.292, naive rule 0.476, lift 3.01x
    - 7d: 383 calls (55 a day), hit rate 0.930, chance 0.288, naive rule 0.478, lift 3.22x
    - 30d: 1703 calls (57 a day), hit rate 0.934, chance 0.292, naive rule 0.484, lift 3.20x
  - next: threshold 0.5247, hit rate recent 0.5367 / long run 0.5617
    - 6h: 29 calls (118 a day), hit rate 0.586, chance 0.296, lift 1.98x
    - 24h: 122 calls (122 a day), hit rate 0.533, chance 0.292, lift 1.82x
    - 7d: 736 calls (105 a day), hit rate 0.561, chance 0.288, lift 1.95x
    - 30d: 2651 calls (88 a day), hit rate 0.571, chance 0.292, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 541, 0.514; 0.40: 482, 0.567; 0.45: 413, 0.636; 0.50: 361, 0.689; 0.55: 316, 0.730; 0.60: 269, 0.774; 0.65: 224, 0.802; 0.70: 178, 0.835; 0.75: 138, 0.870; 0.80: 94, 0.911; 0.85: 48, 0.950; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 498, 0.461; 0.40: 406, 0.492; 0.45: 311, 0.524; 0.50: 201, 0.554; 0.55: 90, 0.568; 0.60: 14, 0.607; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 113482, probability skill vs chance 0.2059, widened contest next: True
  - now: threshold 0.6834, hit rate recent 0.8259 / long run 0.8245
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.174, naive rule 0.347, lift 4.46x
    - 24h: 52 calls (52 a day), hit rate 0.808, chance 0.186, naive rule 0.396, lift 4.35x
    - 7d: 354 calls (51 a day), hit rate 0.822, chance 0.186, naive rule 0.397, lift 4.42x
    - 30d: 1585 calls (53 a day), hit rate 0.827, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.4183, hit rate recent 0.3708 / long run 0.4388
    - 6h: 28 calls (114 a day), hit rate 0.321, chance 0.174, lift 1.84x
    - 24h: 128 calls (129 a day), hit rate 0.383, chance 0.186, lift 2.06x
    - 7d: 877 calls (125 a day), hit rate 0.439, chance 0.186, lift 2.36x
    - 30d: 2498 calls (83 a day), hit rate 0.462, chance 0.187, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 348, 0.488; 0.40: 280, 0.558; 0.45: 227, 0.615; 0.50: 179, 0.663; 0.55: 137, 0.708; 0.60: 107, 0.750; 0.65: 79, 0.789; 0.70: 57, 0.822; 0.75: 32, 0.864; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 250, 0.417; 0.40: 157, 0.442; 0.45: 73, 0.457; 0.50: 17, 0.492; 0.55: 2, 0.490
- **K=8**: model 1792454400, labels learned 113479, probability skill vs chance 0.1925, widened contest next: True
  - now: threshold 0.5692, hit rate recent 0.6109 / long run 0.6827
    - 6h: 10 calls (41 a day), hit rate 0.500, chance 0.086, naive rule 0.215, lift 5.83x
    - 24h: 44 calls (44 a day), hit rate 0.591, chance 0.113, naive rule 0.310, lift 5.22x
    - 7d: 324 calls (46 a day), hit rate 0.664, chance 0.117, naive rule 0.318, lift 5.66x
    - 30d: 1554 calls (52 a day), hit rate 0.705, chance 0.121, naive rule 0.327, lift 5.81x
  - next: threshold 0.3506, hit rate recent 0.3644 / long run 0.3727
    - 6h: 20 calls (82 a day), hit rate 0.250, chance 0.086, lift 2.92x
    - 24h: 108 calls (109 a day), hit rate 0.380, chance 0.113, lift 3.35x
    - 7d: 729 calls (104 a day), hit rate 0.362, chance 0.117, lift 3.09x
    - 30d: 2334 calls (78 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 255, 0.420; 0.35: 194, 0.490; 0.40: 148, 0.546; 0.45: 116, 0.590; 0.50: 88, 0.632; 0.55: 64, 0.678; 0.60: 43, 0.722; 0.65: 24, 0.781; 0.70: 9, 0.830; 0.75: 1, 0.786
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.348; 0.35: 102, 0.378; 0.40: 40, 0.404; 0.45: 8, 0.425; 0.50: 1, 0.471
- **K=13**: model 1792454400, labels learned 113474, probability skill vs chance 0.1804, widened contest next: True
  - now: threshold 0.4298, hit rate recent 0.4853 / long run 0.5519
    - 6h: 9 calls (38 a day), hit rate 0.444, chance 0.065, naive rule 0.193, lift 6.81x
    - 24h: 54 calls (55 a day), hit rate 0.481, chance 0.073, naive rule 0.244, lift 6.63x
    - 7d: 390 calls (56 a day), hit rate 0.518, chance 0.076, naive rule 0.268, lift 6.80x
    - 30d: 1553 calls (52 a day), hit rate 0.570, chance 0.078, naive rule 0.271, lift 7.35x
  - next: threshold 0.2755, hit rate recent 0.321 / long run 0.3146
    - 6h: 16 calls (67 a day), hit rate 0.250, chance 0.065, lift 3.83x
    - 24h: 75 calls (76 a day), hit rate 0.347, chance 0.073, lift 4.77x
    - 7d: 444 calls (64 a day), hit rate 0.313, chance 0.076, lift 4.11x
    - 30d: 2117 calls (71 a day), hit rate 0.308, chance 0.078, lift 3.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.449; 0.35: 86, 0.504; 0.40: 61, 0.552; 0.45: 41, 0.608; 0.50: 25, 0.655; 0.55: 14, 0.709; 0.60: 5, 0.753; 0.65: 1, 0.849
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.318; 0.35: 13, 0.352; 0.40: 2, 0.433

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 10.635 | 3.95% | 0.867 | 0.450 | 0.254 | 0.400 | 0.129 |
| 6h | 11.654 | 2.89% | 0.900 | 0.503 | 0.251 | 0.492 | 0.292 |
| 24h | 17.291 | 3.21% | 0.892 | 0.500 | 0.251 | 0.500 | 0.651 |
| 7d | 16.253 | 4.25% | 0.900 | 0.501 | 0.251 | 0.494 | 0.651 |
| 30d | 13.860 | 4.04% | 0.900 | 0.500 | 0.251 | 0.495 | 0.676 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.072 | 10.533 | 10.501 | 10.545 | 10.721 | 10.588 | 10.529 | 10.607 | 10.536 | 10.635 |
| 6h | 12.001 | 11.671 | 11.646 | 11.775 | 11.736 | 11.749 | 11.614 | 11.625 | 11.620 | 11.654 |
| 24h | 17.865 | 17.362 | 17.296 | 17.291 | 17.491 | 17.405 | 17.290 | 17.240 | 17.242 | 17.291 |
| 7d | 16.975 | 16.432 | 16.336 | 16.265 | 16.498 | 16.456 | 16.251 | 16.232 | 16.220 | 16.253 |
| 30d | 14.444 | 13.984 | 13.945 | 13.883 | 14.107 | 14.047 | 13.856 | 13.835 | 13.834 | 13.860 |

## Next candle

- candle starting 2026-10-20 23:30 UTC, last close 2445.15
- P(up) 0.5048, return quantiles (bp): {'05': -6.342, '10': -4.709, '25': -2.511, '40': -0.851, '50': 0.041, '60': 0.982, '75': 2.649, '90': 5.21, '95': 6.919}
- changepoint probability 0.0379, regime age 165.9 min
- agent weights: empirical 0.004, ewma 0.113, garch 0.179, har 0.149, bocpd 0.048, hmm 0.061, online_qr 0.194, lgbm 0.252

## Learning log

- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- HMM volatility states (sd, bp per minute): [3.17, 5.79, 15.89], current probabilities: [0.953, 0.046, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-20 23:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.181, 'l_abs': 0.691, 'l_hi': 0.795, 'l_lo': 0.797, 'b05': 0.707, 'b25': 0.657, 'b75': 0.657, 'b95': 0.706}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.431, 1.654, 1.876, 2.102, 2.499, 2.815, 2.84, 3.141, 3.594, 3.629, 3.723, 4.041, 4.462, 4.628]}
- calibration offsets (in sigma): {'05': 0.0345, '10': 0.039, '25': -0.0075, '40': -0.004, '50': -0.005, '60': -0.016, '75': -0.0125, '90': 0.011, '95': 0.0155}
