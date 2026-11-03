# ETH-USD 60s candle generator - report

- generated: 2026-11-03 18:32 UTC
- last closed candle: 2026-11-03 18:32 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.498 (672) [0.476, 0.521] | 0.517 (2878) [0.498, 0.536] | 0.514 (5946) [0.501, 0.527] | 0.517 (2974) [0.499, 0.536] | 0.419 (74) | 0.500 | flat -0.031 (noise 0.027) |
| colour_clear | 0.524 (809) | 0.540 (5488) [0.531, 0.550] | 0.544 (23646) [0.540, 0.549] | 0.521 (48605) [0.515, 0.527] | 0.545 (24367) [0.540, 0.548] | 0.531 (637) | 0.500 | flat -0.008 (noise 0.009) |
| colour_confident | 0.568 (88) | 0.575 (979) [0.564, 0.587] | 0.597 (4516) [0.585, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.597 (4600) [0.586, 0.609] | 0.685 (73) | 0.500 | flat -0.026 (noise 0.021) |
| colour_next | 0.530 (1434) | 0.531 (9968) [0.525, 0.538] | 0.530 (42837) [0.526, 0.534] | 0.515 (88590) [0.511, 0.519] | 0.530 (44241) [0.526, 0.533] | 0.534 (1108) | 0.500 | flat +0.000 (noise 0.007) |
| colour_path | 0.498 (20076) | 0.502 (139552) [0.500, 0.504] | 0.501 (599718) [0.500, 0.502] | 0.501 (1240260) [0.500, 0.502] | 0.501 (619374) [0.499, 0.502] | 0.506 (15512) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.706 (17) | 0.619 (236) [0.577, 0.663] | 0.633 (1203) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.633 (1230) [0.614, 0.653] | 0.600 (10) | 0.500 | flat -0.008 (noise 0.040) |
| reversal_k13_next | 0.404 (47) | 0.356 (343) [0.308, 0.402] | 0.323 (1879) [0.310, 0.337] | 0.311 (4086) [0.301, 0.323] | 0.323 (1981) [0.311, 0.336] | 0.460 (50) | 0.077 | flat +0.043 (noise 0.034) |
| reversal_k13_now | 0.471 (51) | 0.581 (422) [0.543, 0.614] | 0.560 (1681) [0.541, 0.579] | 0.572 (3198) [0.558, 0.586] | 0.565 (1726) [0.545, 0.585] | 0.628 (43) | 0.077 | flat +0.035 (noise 0.035) |
| reversal_k3_next | 0.646 (113) | 0.599 (877) [0.587, 0.614] | 0.588 (3052) [0.577, 0.598] | 0.586 (5636) [0.578, 0.596] | 0.585 (3196) [0.575, 0.597] | 0.542 (48) | 0.293 | flat -0.002 (noise 0.025) |
| reversal_k3_now | 0.898 (59) | 0.934 (441) [0.912, 0.958] | 0.934 (1747) [0.924, 0.944] | 0.938 (3567) [0.931, 0.944] | 0.933 (1804) [0.923, 0.943] | 0.875 (40) | 0.293 | flat -0.012 (noise 0.020) |
| reversal_k5_next | 0.564 (55) | 0.543 (392) [0.528, 0.558] | 0.479 (2766) [0.464, 0.494] | 0.482 (4945) [0.471, 0.494] | 0.474 (2955) [0.460, 0.490] | 0.500 (46) | 0.187 | up +0.064 (noise 0.030) |
| reversal_k5_now | 0.803 (66) | 0.822 (443) [0.808, 0.834] | 0.821 (1645) [0.809, 0.832] | 0.829 (3317) [0.820, 0.838] | 0.821 (1706) [0.810, 0.831] | 0.744 (39) | 0.187 | flat +0.002 (noise 0.027) |
| reversal_k8_next | 0.475 (40) | 0.435 (575) [0.411, 0.461] | 0.391 (2808) [0.377, 0.405] | 0.393 (4991) [0.382, 0.404] | 0.391 (2885) [0.378, 0.404] | 0.426 (54) | 0.121 | up +0.056 (noise 0.027) |
| reversal_k8_now | 0.635 (52) | 0.716 (391) [0.680, 0.746] | 0.686 (1596) [0.665, 0.706] | 0.701 (3233) [0.687, 0.716] | 0.689 (1646) [0.667, 0.709] | 0.658 (41) | 0.122 | flat +0.058 (noise 0.036) |
| overall | 0.503 (22089) | 0.507 (154076) [0.504, 0.509] | 0.505 (662607) [0.503, 0.506] | 0.504 (1367769) [0.503, 0.505] | 0.505 (684488) [0.503, 0.506] | 0.509 (17055) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07903, 0.1193] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5299, 'levels': [{'threshold': 0.07903, 'calls_per_day': 140.8, 'win_rate': 0.5783}, {'threshold': 0.1193, 'calls_per_day': 34.2, 'win_rate': 0.6322}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42851, 'rate': 0.5298}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15251 | 0.334 | 0.527 (14969) | 0.576 (2271) | 0.758 (2669) |
| volatility: normal | 15250 | 0.366 | 0.534 (15174) | 0.611 (1566) | 0.741 (2273) |
| volatility: wild | 15251 | 0.381 | 0.529 (15206) | 0.634 (836) | 0.763 (2103) |
| session: Asia 00-08 | 15360 | 0.360 | 0.536 (15245) | 0.603 (1639) | 0.759 (2286) |
| session: Europe 08-13 | 9600 | 0.355 | 0.533 (9495) | 0.594 (1187) | 0.743 (1609) |
| session: US 13-21 | 15212 | 0.368 | 0.527 (15088) | 0.598 (1214) | 0.760 (2308) |
| session: late 21-24 | 5580 | 0.351 | 0.516 (5521) | 0.596 (633) | 0.744 (842) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.358 | 0.348 | 0.271 | 0.271 | 0.542 | 0.269 | 0.446 | 1.145 |
| 6h | 360 | 0.378 | 0.376 | 0.276 | 0.307 | 0.531 | 0.263 | 0.494 | 1.276 |
| 24h | 1440 | 0.378 | 0.375 | 0.287 | 0.327 | 0.530 | 0.268 | 0.487 | 1.173 |
| 7d | 10080 | 0.360 | 0.355 | 0.274 | 0.305 | 0.531 | 0.261 | 0.459 | 1.277 |
| 30d | 43200 | 0.363 | 0.356 | 0.276 | 0.307 | 0.530 | 0.263 | 0.464 | 1.247 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.358 / 0.542 / 0.883; 2: 0.381 / 0.542 / 0.767; 3: 0.362 / 0.542 / 0.917; 4: 0.349 / 0.424 / 0.933; 5: 0.348 / 0.525 / 0.750; 6: 0.339 / 0.525 / 0.983; 7: 0.368 / 0.508 / 0.800; 8: 0.337 / 0.373 / 0.850; 9: 0.355 / 0.559 / 0.833; 10: 0.379 / 0.492 / 0.867; 11: 0.372 / 0.576 / 0.817; 12: 0.364 / 0.508 / 0.917; 13: 0.342 / 0.407 / 0.867; 14: 0.327 / 0.356 / 0.933; 15: 0.382 / 0.525 / 0.900
- 6h: 1: 0.378 / 0.531 / 0.906; 2: 0.375 / 0.503 / 0.808; 3: 0.375 / 0.522 / 0.953; 4: 0.358 / 0.472 / 0.944; 5: 0.365 / 0.520 / 0.833; 6: 0.357 / 0.522 / 0.969; 7: 0.363 / 0.489 / 0.867; 8: 0.365 / 0.489 / 0.869; 9: 0.361 / 0.508 / 0.869; 10: 0.366 / 0.494 / 0.867; 11: 0.366 / 0.511 / 0.836; 12: 0.363 / 0.503 / 0.906; 13: 0.365 / 0.466 / 0.856; 14: 0.362 / 0.500 / 0.894; 15: 0.370 / 0.500 / 0.867
- 24h: 1: 0.378 / 0.530 / 0.892; 2: 0.368 / 0.498 / 0.882; 3: 0.370 / 0.519 / 0.914; 4: 0.364 / 0.491 / 0.917; 5: 0.365 / 0.509 / 0.897; 6: 0.364 / 0.514 / 0.914; 7: 0.371 / 0.513 / 0.903; 8: 0.364 / 0.495 / 0.904; 9: 0.364 / 0.507 / 0.903; 10: 0.359 / 0.479 / 0.903; 11: 0.370 / 0.514 / 0.892; 12: 0.361 / 0.489 / 0.901; 13: 0.366 / 0.498 / 0.897; 14: 0.360 / 0.498 / 0.905; 15: 0.373 / 0.524 / 0.900
- 7d: 1: 0.360 / 0.531 / 0.897; 2: 0.347 / 0.493 / 0.897; 3: 0.350 / 0.508 / 0.900; 4: 0.347 / 0.499 / 0.901; 5: 0.348 / 0.512 / 0.898; 6: 0.345 / 0.506 / 0.900; 7: 0.348 / 0.499 / 0.898; 8: 0.345 / 0.507 / 0.898; 9: 0.346 / 0.504 / 0.898; 10: 0.344 / 0.496 / 0.899; 11: 0.344 / 0.500 / 0.897; 12: 0.343 / 0.495 / 0.899; 13: 0.345 / 0.502 / 0.898; 14: 0.344 / 0.499 / 0.899; 15: 0.346 / 0.508 / 0.898
- 30d: 1: 0.363 / 0.530 / 0.899; 2: 0.351 / 0.496 / 0.899; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.505 / 0.899; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.500 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.348 / 0.499 / 0.900; 10: 0.349 / 0.504 / 0.900; 11: 0.346 / 0.497 / 0.899; 12: 0.347 / 0.501 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.346 / 0.500 / 0.900; 15: 0.347 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.071 (body 0.045, range 0.096); 'price stays where it was' would score 0.060; colour right 0.475; typical miss of the close 12.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.134 (body 0.085, range 0.183); 'price stays where it was' would score 0.121; colour right 0.520; typical miss of the close 11.7 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.124 (body 0.086, range 0.163); 'price stays where it was' would score 0.118; colour right 0.508; typical miss of the close 9.7 bp; chain ended on the right side 0.417 of 96 chains; n=1440
- 7d: match 0.123 (body 0.085, range 0.162); 'price stays where it was' would score 0.125; colour right 0.503; typical miss of the close 8.2 bp; chain ended on the right side 0.490 of 672 chains; n=10080
- 30d: match 0.124 (body 0.085, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.1 bp; chain ended on the right side 0.510 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.1; 2: 0.199 / 4.8; 3: 0.168 / 6.4; 4: 0.131 / 6.8; 5: 0.125 / 7.5; 6: 0.114 / 8.2; 7: 0.111 / 8.3; 8: 0.098 / 9.2; 9: 0.089 / 9.2; 10: 0.089 / 9.6; 11: 0.086 / 10.0; 12: 0.077 / 10.4; 13: 0.068 / 10.6; 14: 0.070 / 11.2; 15: 0.062 / 11.3

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 133346, probability skill vs chance 0.2169, widened contest next: True
  - now: threshold 0.8388, hit rate recent 0.8914 / long run 0.9301
    - 6h: 9 calls (37 a day), hit rate 1.000, chance 0.286, naive rule 0.482, lift 3.50x
    - 24h: 56 calls (56 a day), hit rate 0.875, chance 0.278, naive rule 0.446, lift 3.15x
    - 7d: 424 calls (61 a day), hit rate 0.925, chance 0.291, naive rule 0.493, lift 3.18x
    - 30d: 1743 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.5655, hit rate recent 0.5781 / long run 0.5985
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.286, lift 1.94x
    - 24h: 68 calls (68 a day), hit rate 0.515, chance 0.278, lift 1.85x
    - 7d: 833 calls (119 a day), hit rate 0.595, chance 0.291, lift 2.05x
    - 30d: 3005 calls (100 a day), hit rate 0.587, chance 0.294, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 535, 0.523; 0.40: 474, 0.580; 0.45: 406, 0.651; 0.50: 356, 0.700; 0.55: 310, 0.743; 0.60: 263, 0.787; 0.65: 221, 0.812; 0.70: 175, 0.843; 0.75: 139, 0.877; 0.80: 93, 0.909; 0.85: 47, 0.946; 0.90: 5, 0.986
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 500, 0.464; 0.40: 404, 0.499; 0.45: 307, 0.534; 0.50: 198, 0.571; 0.55: 89, 0.573; 0.60: 12, 0.653; 0.65: 1, 0.652
- **K=5**: model 1792540800, labels learned 133344, probability skill vs chance 0.2148, widened contest next: True
  - now: threshold 0.6789, hit rate recent 0.7797 / long run 0.8158
    - 6h: 7 calls (29 a day), hit rate 0.857, chance 0.194, naive rule 0.431, lift 4.42x
    - 24h: 56 calls (56 a day), hit rate 0.768, chance 0.178, naive rule 0.363, lift 4.32x
    - 7d: 430 calls (61 a day), hit rate 0.812, chance 0.187, naive rule 0.412, lift 4.33x
    - 30d: 1635 calls (55 a day), hit rate 0.815, chance 0.188, naive rule 0.406, lift 4.34x
  - next: threshold 0.4497, hit rate recent 0.5338 / long run 0.5116
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.194, lift 3.09x
    - 24h: 53 calls (53 a day), hit rate 0.472, chance 0.178, lift 2.66x
    - 7d: 391 calls (56 a day), hit rate 0.535, chance 0.187, lift 2.85x
    - 30d: 2717 calls (91 a day), hit rate 0.480, chance 0.188, lift 2.56x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 347, 0.492; 0.40: 280, 0.566; 0.45: 230, 0.617; 0.50: 183, 0.665; 0.55: 145, 0.702; 0.60: 110, 0.749; 0.65: 77, 0.786; 0.70: 50, 0.817; 0.75: 29, 0.860; 0.80: 10, 0.880
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 346, 0.387; 0.35: 255, 0.421; 0.40: 159, 0.460; 0.45: 67, 0.483; 0.50: 12, 0.501; 0.55: 1, 0.486
- **K=8**: model 1793059200, labels learned 133341, probability skill vs chance 0.2008, widened contest next: False
  - now: threshold 0.5738, hit rate recent 0.663 / long run 0.6893
    - 6h: 8 calls (33 a day), hit rate 0.875, chance 0.121, naive rule 0.364, lift 7.21x
    - 24h: 59 calls (59 a day), hit rate 0.610, chance 0.119, naive rule 0.316, lift 5.12x
    - 7d: 382 calls (55 a day), hit rate 0.709, chance 0.125, naive rule 0.349, lift 5.69x
    - 30d: 1597 calls (53 a day), hit rate 0.682, chance 0.121, naive rule 0.335, lift 5.64x
  - next: threshold 0.3637, hit rate recent 0.4387 / long run 0.4183
    - 6h: 16 calls (66 a day), hit rate 0.375, chance 0.121, lift 3.09x
    - 24h: 57 calls (57 a day), hit rate 0.404, chance 0.119, lift 3.38x
    - 7d: 552 calls (79 a day), hit rate 0.440, chance 0.125, lift 3.53x
    - 30d: 2797 calls (93 a day), hit rate 0.391, chance 0.121, lift 3.24x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.432; 0.35: 191, 0.498; 0.40: 150, 0.543; 0.45: 115, 0.590; 0.50: 85, 0.637; 0.55: 62, 0.672; 0.60: 41, 0.702; 0.65: 24, 0.777; 0.70: 12, 0.808; 0.75: 2, 0.758
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.360; 0.35: 91, 0.388; 0.40: 27, 0.421; 0.45: 5, 0.456; 0.50: 1, 0.680
- **K=13**: model 1793577600, labels learned 133336, probability skill vs chance 0.1898, widened contest next: False
  - now: threshold 0.4505, hit rate recent 0.5758 / long run 0.5676
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.080, naive rule 0.326, lift 8.69x
    - 24h: 59 calls (60 a day), hit rate 0.559, chance 0.084, naive rule 0.288, lift 6.70x
    - 7d: 418 calls (60 a day), hit rate 0.581, chance 0.080, naive rule 0.295, lift 7.27x
    - 30d: 1676 calls (56 a day), hit rate 0.560, chance 0.077, naive rule 0.281, lift 7.24x
  - next: threshold 0.2877, hit rate recent 0.4207 / long run 0.3411
    - 6h: 11 calls (46 a day), hit rate 0.455, chance 0.080, lift 5.70x
    - 24h: 58 calls (59 a day), hit rate 0.448, chance 0.084, lift 5.37x
    - 7d: 355 calls (51 a day), hit rate 0.358, chance 0.080, lift 4.47x
    - 30d: 1865 calls (62 a day), hit rate 0.326, chance 0.077, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.439; 0.35: 93, 0.492; 0.40: 66, 0.545; 0.45: 44, 0.585; 0.50: 29, 0.644; 0.55: 19, 0.678; 0.60: 10, 0.720; 0.65: 3, 0.699; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.333; 0.35: 13, 0.359; 0.40: 3, 0.422; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 12.319 | 0.41% | 0.900 | 0.450 | 0.247 | 0.576 | 0.020 |
| 6h | 18.951 | 3.54% | 0.908 | 0.492 | 0.249 | 0.547 | 0.546 |
| 24h | 14.677 | 2.44% | 0.895 | 0.500 | 0.250 | 0.514 | 0.542 |
| 7d | 14.965 | 5.03% | 0.900 | 0.500 | 0.250 | 0.510 | 0.743 |
| 30d | 14.431 | 4.33% | 0.900 | 0.500 | 0.250 | 0.499 | 0.685 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 12.370 | 12.340 | 12.437 | 12.247 | 12.484 | 12.558 | 12.347 | 12.369 | 12.332 | 12.319 |
| 6h | 19.647 | 19.105 | 19.059 | 19.016 | 19.357 | 19.055 | 18.875 | 18.923 | 18.909 | 18.951 |
| 24h | 15.044 | 14.743 | 14.754 | 14.749 | 14.888 | 14.893 | 14.636 | 14.638 | 14.640 | 14.677 |
| 7d | 15.758 | 15.134 | 15.095 | 15.009 | 15.296 | 15.285 | 14.948 | 14.938 | 14.941 | 14.965 |
| 30d | 15.084 | 14.581 | 14.528 | 14.465 | 14.698 | 14.643 | 14.424 | 14.402 | 14.405 | 14.431 |

## Next candle

- candle starting 2026-11-03 18:32 UTC, last close 2296.57
- P(up) 0.531, return quantiles (bp): {'05': -7.276, '10': -5.5, '25': -3.036, '40': -0.751, '50': 0.328, '60': 0.952, '75': 2.86, '90': 5.961, '95': 8.381}
- changepoint probability 0.0691, regime age 103.8 min
- agent weights: empirical 0.005, ewma 0.098, garch 0.102, har 0.137, bocpd 0.023, hmm 0.040, online_qr 0.326, lgbm 0.269

## Learning log

- 2026-11-01 12:00 UTC: {"garch": {"alpha": 0.0654, "beta": 0.9319}, "hmm": {"sd_bp": [2.72, 6.38, 19.49], "stay": [0.98, 0.965, 0.926]}}
- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- HMM volatility states (sd, bp per minute): [2.59, 5.61, 12.38], current probabilities: [0.001, 0.891, 0.108]
- live generator: {'versions': 60, 'latest_effective': '2026-11-03 18:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.215, 'l_abs': 0.678, 'l_hi': 0.759, 'l_lo': 0.79, 'b05': 0.736, 'b25': 0.618, 'b75': 0.645, 'b95': 0.729}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [2.258, 1.461, 1.657, 3.665, 1.997, 3.564, 3.742, 3.899, 4.036, 5.181, 3.708, 4.916, 4.185, 4.993]}
- calibration offsets (in sigma): {'05': 0.0455, '10': 0.051, '25': -0.0225, '40': 0.064, '50': 0.075, '60': 0.006, '75': 0.0225, '90': 0.029, '95': 0.0745}
