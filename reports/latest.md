# ETH-USD 60s candle generator - report

- generated: 2026-11-07 07:07 UTC
- last closed candle: 2026-11-07 07:07 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k3_now 0.915 in the last 7 days, -0.037 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.484 (672) [0.454, 0.512] | 0.514 (2879) [0.498, 0.531] | 0.512 (6330) [0.500, 0.525] | 0.513 (3358) [0.496, 0.532] | 0.643 (28) | 0.500 | flat -0.042 (noise 0.027) |
| colour_clear | 0.577 (807) | 0.534 (5528) [0.516, 0.553] | 0.542 (23933) [0.536, 0.548] | 0.521 (51854) [0.515, 0.526] | 0.543 (27616) [0.537, 0.548] | 0.553 (228) | 0.500 | flat -0.004 (noise 0.012) |
| colour_confident | 0.646 (96) | 0.578 (888) [0.561, 0.600] | 0.595 (4261) [0.584, 0.605] | 0.597 (4987) [0.586, 0.609] | 0.597 (4987) [0.586, 0.609] | 0.536 (69) | 0.500 | flat -0.015 (noise 0.022) |
| colour_next | 0.554 (1436) | 0.530 (9980) [0.519, 0.541] | 0.529 (42874) [0.525, 0.533] | 0.516 (94331) [0.512, 0.520] | 0.529 (49982) [0.525, 0.533] | 0.523 (421) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.503 (139720) [0.501, 0.505] | 0.502 (600236) [0.500, 0.503] | 0.501 (1320634) [0.500, 0.502] | 0.501 (699748) [0.500, 0.502] | 0.497 (5894) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.550 (20) | 0.611 (198) [0.580, 0.639] | 0.626 (1104) [0.608, 0.645] | 0.629 (1303) [0.611, 0.648] | 0.629 (1303) [0.611, 0.648] | 0.619 (21) | 0.500 | flat +0.015 (noise 0.043) |
| reversal_k13_next | 0.358 (53) | 0.371 (369) [0.342, 0.399] | 0.327 (1809) [0.313, 0.342] | 0.313 (4315) [0.303, 0.324] | 0.326 (2210) [0.314, 0.338] | 0.263 (19) | 0.077 | flat +0.054 (noise 0.034) |
| reversal_k13_now | 0.633 (49) | 0.585 (393) [0.547, 0.620] | 0.566 (1650) [0.547, 0.586] | 0.574 (3412) [0.561, 0.588] | 0.569 (1940) [0.550, 0.587] | 0.364 (11) | 0.077 | flat +0.010 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.612 (610) [0.585, 0.638] | 0.588 (2988) [0.577, 0.599] | 0.587 (5844) [0.578, 0.596] | 0.587 (3404) [0.576, 0.598] | 0.650 (20) | 0.293 | flat +0.021 (noise 0.027) |
| reversal_k3_now | 0.933 (60) | 0.915 (422) [0.905, 0.924] | 0.932 (1753) [0.922, 0.942] | 0.936 (3789) [0.930, 0.943] | 0.932 (2026) [0.923, 0.941] | 1.000 (10) | 0.294 | down -0.037 (noise 0.017) |
| reversal_k5_next | 0.528 (36) | 0.539 (395) [0.516, 0.559] | 0.483 (2715) [0.469, 0.499] | 0.484 (5156) [0.473, 0.495] | 0.478 (3166) [0.464, 0.492] | 0.421 (19) | 0.187 | flat +0.032 (noise 0.033) |
| reversal_k5_now | 0.862 (58) | 0.818 (407) [0.802, 0.834] | 0.819 (1636) [0.809, 0.828] | 0.829 (3523) [0.820, 0.838] | 0.821 (1912) [0.811, 0.831] | 0.625 (8) | 0.187 | flat -0.012 (noise 0.027) |
| reversal_k8_next | 0.438 (48) | 0.461 (414) [0.440, 0.480] | 0.395 (2692) [0.381, 0.409] | 0.395 (5218) [0.385, 0.406] | 0.395 (3112) [0.381, 0.407] | 0.333 (15) | 0.121 | up +0.067 (noise 0.031) |
| reversal_k8_now | 0.719 (57) | 0.704 (371) [0.676, 0.728] | 0.683 (1548) [0.663, 0.702] | 0.701 (3431) [0.688, 0.715] | 0.690 (1844) [0.672, 0.708] | 0.571 (7) | 0.121 | flat +0.007 (noise 0.034) |
| overall | 0.507 (22038) | 0.508 (153753) [0.506, 0.509] | 0.505 (662780) [0.504, 0.506] | 0.504 (1455983) [0.503, 0.505] | 0.505 (772702) [0.504, 0.506] | 0.499 (6452) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0762, 0.1148] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5299, 'levels': [{'threshold': 0.0762, 'calls_per_day': 145.2, 'win_rate': 0.5764}, {'threshold': 0.1148, 'calls_per_day': 36.6, 'win_rate': 0.6216}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42869, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15023 | 0.343 | 0.527 (14793) | 0.575 (2240) | 0.739 (2492) |
| volatility: normal | 15022 | 0.368 | 0.534 (14954) | 0.611 (1402) | 0.755 (2245) |
| volatility: wild | 15022 | 0.384 | 0.525 (14982) | 0.618 (799) | 0.766 (2083) |
| session: Asia 00-08 | 15307 | 0.364 | 0.534 (15203) | 0.599 (1587) | 0.759 (2241) |
| session: Europe 08-13 | 9300 | 0.360 | 0.536 (9208) | 0.597 (1151) | 0.747 (1510) |
| session: US 13-21 | 14880 | 0.372 | 0.524 (14785) | 0.596 (1130) | 0.753 (2265) |
| session: late 21-24 | 5580 | 0.354 | 0.512 (5533) | 0.574 (573) | 0.744 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.300 | 0.305 | 0.181 | 0.181 | 0.552 | 0.233 | 0.367 | 1.862 |
| 6h | 360 | 0.339 | 0.348 | 0.247 | 0.284 | 0.527 | 0.257 | 0.421 | 1.384 |
| 24h | 1440 | 0.380 | 0.375 | 0.276 | 0.309 | 0.544 | 0.276 | 0.484 | 1.363 |
| 7d | 10080 | 0.363 | 0.359 | 0.275 | 0.306 | 0.530 | 0.261 | 0.465 | 1.282 |
| 30d | 43200 | 0.365 | 0.358 | 0.277 | 0.308 | 0.529 | 0.263 | 0.467 | 1.249 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.300 / 0.552 / 0.883; 2: 0.276 / 0.397 / 0.917; 3: 0.288 / 0.534 / 0.950; 4: 0.292 / 0.569 / 0.967; 5: 0.305 / 0.603 / 0.983; 6: 0.285 / 0.500 / 0.933; 7: 0.305 / 0.569 / 0.950; 8: 0.282 / 0.448 / 0.950; 9: 0.286 / 0.483 / 1.000; 10: 0.275 / 0.483 / 1.000; 11: 0.296 / 0.500 / 0.983; 12: 0.273 / 0.414 / 0.967; 13: 0.269 / 0.448 / 0.983; 14: 0.288 / 0.534 / 1.000; 15: 0.292 / 0.586 / 0.983
- 6h: 1: 0.339 / 0.527 / 0.881; 2: 0.327 / 0.456 / 0.892; 3: 0.332 / 0.501 / 0.894; 4: 0.338 / 0.515 / 0.897; 5: 0.337 / 0.521 / 0.936; 6: 0.326 / 0.485 / 0.900; 7: 0.326 / 0.487 / 0.919; 8: 0.332 / 0.496 / 0.911; 9: 0.346 / 0.544 / 0.958; 10: 0.331 / 0.487 / 0.967; 11: 0.334 / 0.485 / 0.956; 12: 0.326 / 0.476 / 0.953; 13: 0.315 / 0.434 / 0.942; 14: 0.323 / 0.487 / 0.975; 15: 0.326 / 0.496 / 0.947
- 24h: 1: 0.380 / 0.544 / 0.901; 2: 0.360 / 0.469 / 0.899; 3: 0.369 / 0.517 / 0.899; 4: 0.364 / 0.500 / 0.898; 5: 0.370 / 0.527 / 0.903; 6: 0.365 / 0.509 / 0.889; 7: 0.361 / 0.497 / 0.904; 8: 0.357 / 0.482 / 0.894; 9: 0.366 / 0.508 / 0.905; 10: 0.366 / 0.510 / 0.908; 11: 0.365 / 0.512 / 0.908; 12: 0.357 / 0.483 / 0.902; 13: 0.354 / 0.468 / 0.896; 14: 0.360 / 0.503 / 0.901; 15: 0.358 / 0.498 / 0.890
- 7d: 1: 0.363 / 0.530 / 0.896; 2: 0.351 / 0.492 / 0.901; 3: 0.355 / 0.513 / 0.901; 4: 0.352 / 0.502 / 0.899; 5: 0.353 / 0.510 / 0.900; 6: 0.350 / 0.509 / 0.899; 7: 0.349 / 0.497 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.352 / 0.510 / 0.901; 10: 0.348 / 0.496 / 0.901; 11: 0.348 / 0.503 / 0.900; 12: 0.348 / 0.501 / 0.901; 13: 0.348 / 0.499 / 0.900; 14: 0.347 / 0.500 / 0.900; 15: 0.349 / 0.508 / 0.899
- 30d: 1: 0.365 / 0.529 / 0.898; 2: 0.353 / 0.495 / 0.900; 3: 0.356 / 0.510 / 0.900; 4: 0.352 / 0.499 / 0.900; 5: 0.353 / 0.505 / 0.901; 6: 0.351 / 0.502 / 0.900; 7: 0.351 / 0.499 / 0.900; 8: 0.351 / 0.504 / 0.901; 9: 0.351 / 0.501 / 0.901; 10: 0.351 / 0.504 / 0.901; 11: 0.348 / 0.497 / 0.901; 12: 0.350 / 0.503 / 0.901; 13: 0.349 / 0.499 / 0.901; 14: 0.348 / 0.501 / 0.901; 15: 0.349 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.133 (body 0.100, range 0.167); 'price stays where it was' would score 0.098; colour right 0.586; typical miss of the close 1.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.105 (body 0.069, range 0.140); 'price stays where it was' would score 0.088; colour right 0.521; typical miss of the close 4.8 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.136 (body 0.093, range 0.179); 'price stays where it was' would score 0.142; colour right 0.516; typical miss of the close 7.9 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.160); 'price stays where it was' would score 0.123; colour right 0.503; typical miss of the close 8.7 bp; chain ended on the right side 0.491 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.6 bp; chain ended on the right side 0.516 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.5; 2: 0.200 / 5.1; 3: 0.166 / 6.8; 4: 0.132 / 7.1; 5: 0.126 / 7.7; 6: 0.115 / 8.6; 7: 0.112 / 8.8; 8: 0.100 / 9.8; 9: 0.092 / 9.7; 10: 0.091 / 10.3; 11: 0.087 / 10.3; 12: 0.081 / 10.7; 13: 0.074 / 11.1; 14: 0.072 / 11.6; 15: 0.065 / 11.8

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 138421, probability skill vs chance 0.2223, widened contest next: False
  - now: threshold 0.838, hit rate recent 0.9431 / long run 0.9309
    - 6h: 8 calls (32 a day), hit rate 1.000, chance 0.310, naive rule 0.526, lift 3.23x
    - 24h: 45 calls (45 a day), hit rate 0.956, chance 0.317, naive rule 0.525, lift 3.01x
    - 7d: 410 calls (59 a day), hit rate 0.915, chance 0.296, naive rule 0.500, lift 3.09x
    - 30d: 1743 calls (58 a day), hit rate 0.932, chance 0.295, naive rule 0.497, lift 3.16x
  - next: threshold 0.5658, hit rate recent 0.6322 / long run 0.6079
    - 6h: 15 calls (61 a day), hit rate 0.667, chance 0.310, lift 2.15x
    - 24h: 40 calls (40 a day), hit rate 0.625, chance 0.317, lift 1.97x
    - 7d: 580 calls (83 a day), hit rate 0.617, chance 0.296, lift 2.08x
    - 30d: 2984 calls (99 a day), hit rate 0.588, chance 0.295, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.500; 0.35: 533, 0.525; 0.40: 474, 0.581; 0.45: 406, 0.652; 0.50: 356, 0.701; 0.55: 309, 0.745; 0.60: 261, 0.789; 0.65: 220, 0.814; 0.70: 173, 0.845; 0.75: 139, 0.876; 0.80: 93, 0.908; 0.85: 46, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.431; 0.35: 499, 0.465; 0.40: 402, 0.501; 0.45: 304, 0.537; 0.50: 196, 0.570; 0.55: 89, 0.578; 0.60: 12, 0.644; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 138419, probability skill vs chance 0.2119, widened contest next: False
  - now: threshold 0.6874, hit rate recent 0.8168 / long run 0.8201
    - 6h: 5 calls (20 a day), hit rate 0.600, chance 0.176, naive rule 0.397, lift 3.42x
    - 24h: 46 calls (46 a day), hit rate 0.804, chance 0.183, naive rule 0.407, lift 4.39x
    - 7d: 395 calls (56 a day), hit rate 0.810, chance 0.187, naive rule 0.411, lift 4.32x
    - 30d: 1625 calls (54 a day), hit rate 0.818, chance 0.187, naive rule 0.408, lift 4.37x
  - next: threshold 0.4548, hit rate recent 0.5023 / long run 0.5129
    - 6h: 13 calls (53 a day), hit rate 0.385, chance 0.176, lift 2.19x
    - 24h: 39 calls (39 a day), hit rate 0.462, chance 0.183, lift 2.52x
    - 7d: 393 calls (56 a day), hit rate 0.529, chance 0.187, lift 2.82x
    - 30d: 2714 calls (90 a day), hit rate 0.483, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 349, 0.489; 0.40: 282, 0.562; 0.45: 231, 0.613; 0.50: 185, 0.663; 0.55: 148, 0.699; 0.60: 112, 0.747; 0.65: 77, 0.786; 0.70: 48, 0.821; 0.75: 29, 0.856; 0.80: 10, 0.872
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.385; 0.35: 256, 0.423; 0.40: 159, 0.462; 0.45: 67, 0.488; 0.50: 11, 0.504; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 138416, probability skill vs chance 0.2046, widened contest next: False
  - now: threshold 0.5701, hit rate recent 0.6929 / long run 0.6932
    - 6h: 5 calls (21 a day), hit rate 0.400, chance 0.127, naive rule 0.378, lift 3.15x
    - 24h: 46 calls (46 a day), hit rate 0.717, chance 0.123, naive rule 0.349, lift 5.81x
    - 7d: 360 calls (51 a day), hit rate 0.700, chance 0.122, naive rule 0.343, lift 5.75x
    - 30d: 1541 calls (51 a day), hit rate 0.682, chance 0.121, naive rule 0.337, lift 5.65x
  - next: threshold 0.3583, hit rate recent 0.4155 / long run 0.423
    - 6h: 13 calls (53 a day), hit rate 0.308, chance 0.127, lift 2.42x
    - 24h: 47 calls (47 a day), hit rate 0.426, chance 0.123, lift 3.45x
    - 7d: 392 calls (56 a day), hit rate 0.454, chance 0.122, lift 3.73x
    - 30d: 2673 calls (89 a day), hit rate 0.394, chance 0.121, lift 3.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 192, 0.495; 0.40: 152, 0.541; 0.45: 117, 0.588; 0.50: 85, 0.637; 0.55: 60, 0.672; 0.60: 40, 0.707; 0.65: 24, 0.779; 0.70: 12, 0.805; 0.75: 2, 0.765
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.362; 0.35: 89, 0.389; 0.40: 24, 0.416; 0.45: 5, 0.445; 0.50: 1, 0.692
- **K=13**: model 1793577600, labels learned 138411, probability skill vs chance 0.1889, widened contest next: False
  - now: threshold 0.4571, hit rate recent 0.5613 / long run 0.5696
    - 6h: 9 calls (38 a day), hit rate 0.222, chance 0.074, naive rule 0.310, lift 3.01x
    - 24h: 46 calls (46 a day), hit rate 0.587, chance 0.081, naive rule 0.302, lift 7.24x
    - 7d: 386 calls (55 a day), hit rate 0.570, chance 0.080, naive rule 0.292, lift 7.12x
    - 30d: 1649 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.283, lift 7.24x
  - next: threshold 0.2852, hit rate recent 0.3175 / long run 0.3347
    - 6h: 16 calls (67 a day), hit rate 0.250, chance 0.074, lift 3.38x
    - 24h: 56 calls (57 a day), hit rate 0.321, chance 0.081, lift 3.97x
    - 7d: 371 calls (53 a day), hit rate 0.358, chance 0.080, lift 4.48x
    - 30d: 1807 calls (60 a day), hit rate 0.327, chance 0.078, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.438; 0.35: 94, 0.486; 0.40: 66, 0.544; 0.45: 45, 0.588; 0.50: 30, 0.645; 0.55: 20, 0.675; 0.60: 11, 0.713; 0.65: 3, 0.687; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.345; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.120 | 27.15% | 0.883 | 0.617 | 0.250 | 0.517 | -0.058 |
| 6h | 6.814 | 19.25% | 0.889 | 0.517 | 0.248 | 0.563 | 0.365 |
| 24h | 15.160 | 7.66% | 0.908 | 0.510 | 0.249 | 0.517 | 0.736 |
| 7d | 15.168 | 5.13% | 0.900 | 0.500 | 0.250 | 0.508 | 0.745 |
| 30d | 15.259 | 4.52% | 0.900 | 0.501 | 0.250 | 0.500 | 0.707 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.028 | 5.120 | 5.568 | 5.200 | 5.351 | 6.409 | 5.127 | 5.106 | 5.128 | 5.120 |
| 6h | 8.438 | 6.853 | 7.075 | 6.871 | 6.954 | 7.537 | 6.815 | 6.817 | 6.821 | 6.814 |
| 24h | 16.418 | 15.273 | 15.348 | 15.226 | 15.510 | 15.557 | 15.092 | 15.112 | 15.126 | 15.160 |
| 7d | 15.988 | 15.293 | 15.277 | 15.219 | 15.451 | 15.521 | 15.150 | 15.146 | 15.141 | 15.168 |
| 30d | 15.981 | 15.415 | 15.358 | 15.289 | 15.540 | 15.500 | 15.249 | 15.229 | 15.231 | 15.259 |

## Next candle

- candle starting 2026-11-07 07:07 UTC, last close 2243.17
- P(up) 0.5488, return quantiles (bp): {'05': -3.17, '10': -2.21, '25': -0.974, '40': -0.127, '50': 0.114, '60': 0.395, '75': 1.133, '90': 2.238, '95': 3.077}
- changepoint probability 0.011, regime age 150.0 min
- agent weights: empirical 0.003, ewma 0.139, garch 0.055, har 0.154, bocpd 0.055, hmm 0.008, online_qr 0.299, lgbm 0.287

## Learning log

- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.22, 7.18, 18.37], current probabilities: [0.977, 0.022, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-07 07:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.196, 'l_abs': 0.705, 'l_hi': 0.763, 'l_lo': 0.733, 'b05': 0.715, 'b25': 0.697, 'b75': 0.557, 'b95': 0.673}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.499, 1.803, 2.128, 1.913, 2.415, 2.273, 2.434, 2.249, 2.283, 2.651, 2.561, 3.012, 2.834, 3.314]}
- calibration offsets (in sigma): {'05': 0.043, '10': 0.086, '25': 0.085, '40': 0.124, '50': 0.05, '60': -0.004, '75': -0.005, '90': -0.076, '95': -0.073}
