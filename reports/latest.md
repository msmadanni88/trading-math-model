# ETH-USD 60s candle generator - report

- generated: 2026-11-07 22:18 UTC
- last closed candle: 2026-11-07 22:18 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k3_now 0.915 in the last 7 days, -0.037 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.484 (672) [0.454, 0.512] | 0.514 (2879) [0.498, 0.531] | 0.512 (6330) [0.500, 0.525] | 0.513 (3358) [0.496, 0.532] | 0.528 (89) | 0.500 | flat -0.042 (noise 0.027) |
| colour_clear | 0.577 (807) | 0.534 (5528) [0.516, 0.553] | 0.542 (23933) [0.536, 0.548] | 0.521 (51854) [0.515, 0.526] | 0.543 (27616) [0.537, 0.548] | 0.553 (687) | 0.500 | flat -0.004 (noise 0.012) |
| colour_confident | 0.646 (96) | 0.578 (888) [0.561, 0.600] | 0.595 (4261) [0.584, 0.605] | 0.597 (4987) [0.586, 0.609] | 0.597 (4987) [0.586, 0.609] | 0.580 (238) | 0.500 | flat -0.015 (noise 0.022) |
| colour_next | 0.554 (1436) | 0.530 (9980) [0.519, 0.541] | 0.529 (42874) [0.525, 0.533] | 0.516 (94331) [0.512, 0.520] | 0.529 (49982) [0.525, 0.533] | 0.528 (1303) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.503 (139720) [0.501, 0.505] | 0.502 (600236) [0.500, 0.503] | 0.501 (1320634) [0.500, 0.502] | 0.501 (699748) [0.500, 0.502] | 0.498 (18242) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.550 (20) | 0.611 (198) [0.580, 0.639] | 0.626 (1104) [0.608, 0.645] | 0.629 (1303) [0.611, 0.648] | 0.629 (1303) [0.611, 0.648] | 0.641 (78) | 0.500 | flat +0.015 (noise 0.043) |
| reversal_k13_next | 0.358 (53) | 0.371 (369) [0.342, 0.399] | 0.327 (1809) [0.313, 0.342] | 0.313 (4315) [0.303, 0.324] | 0.326 (2210) [0.314, 0.338] | 0.267 (60) | 0.077 | flat +0.054 (noise 0.034) |
| reversal_k13_now | 0.633 (49) | 0.585 (393) [0.547, 0.620] | 0.566 (1650) [0.547, 0.586] | 0.574 (3412) [0.561, 0.588] | 0.569 (1940) [0.550, 0.587] | 0.500 (44) | 0.077 | flat +0.010 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.612 (610) [0.585, 0.638] | 0.588 (2988) [0.577, 0.599] | 0.587 (5844) [0.578, 0.596] | 0.587 (3404) [0.576, 0.598] | 0.633 (49) | 0.293 | flat +0.021 (noise 0.027) |
| reversal_k3_now | 0.933 (60) | 0.915 (422) [0.905, 0.924] | 0.932 (1753) [0.922, 0.942] | 0.936 (3789) [0.930, 0.943] | 0.932 (2026) [0.923, 0.941] | 0.897 (58) | 0.294 | down -0.037 (noise 0.017) |
| reversal_k5_next | 0.528 (36) | 0.539 (395) [0.516, 0.559] | 0.483 (2715) [0.469, 0.499] | 0.484 (5156) [0.473, 0.495] | 0.478 (3166) [0.464, 0.492] | 0.491 (59) | 0.187 | flat +0.032 (noise 0.033) |
| reversal_k5_now | 0.862 (58) | 0.818 (407) [0.802, 0.834] | 0.819 (1636) [0.809, 0.828] | 0.829 (3523) [0.820, 0.838] | 0.821 (1912) [0.811, 0.831] | 0.800 (45) | 0.187 | flat -0.012 (noise 0.027) |
| reversal_k8_next | 0.438 (48) | 0.461 (414) [0.440, 0.480] | 0.395 (2692) [0.381, 0.409] | 0.395 (5218) [0.385, 0.406] | 0.395 (3112) [0.381, 0.407] | 0.382 (55) | 0.121 | up +0.067 (noise 0.031) |
| reversal_k8_now | 0.719 (57) | 0.704 (371) [0.676, 0.728] | 0.683 (1548) [0.663, 0.702] | 0.701 (3431) [0.688, 0.715] | 0.690 (1844) [0.672, 0.708] | 0.702 (47) | 0.121 | flat +0.007 (noise 0.034) |
| overall | 0.507 (22038) | 0.508 (153753) [0.506, 0.509] | 0.505 (662780) [0.504, 0.506] | 0.504 (1455983) [0.503, 0.505] | 0.505 (772702) [0.504, 0.506] | 0.502 (20051) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07698, 0.1163] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5273, 'levels': [{'threshold': 0.07698, 'calls_per_day': 146.0, 'win_rate': 0.5735}, {'threshold': 0.1163, 'calls_per_day': 36.4, 'win_rate': 0.624}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42844, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15326 | 0.341 | 0.526 (15070) | 0.575 (2353) | 0.740 (2567) |
| volatility: normal | 15326 | 0.368 | 0.535 (15256) | 0.614 (1436) | 0.752 (2281) |
| volatility: wild | 15326 | 0.384 | 0.524 (15285) | 0.618 (821) | 0.768 (2130) |
| session: Asia 00-08 | 15360 | 0.364 | 0.534 (15252) | 0.599 (1604) | 0.759 (2248) |
| session: Europe 08-13 | 9600 | 0.359 | 0.534 (9499) | 0.595 (1220) | 0.749 (1584) |
| session: US 13-21 | 15360 | 0.371 | 0.525 (15250) | 0.596 (1204) | 0.753 (2329) |
| session: late 21-24 | 5658 | 0.355 | 0.514 (5610) | 0.577 (582) | 0.742 (817) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.410 | 0.363 | 0.227 | 0.227 | 0.661 | 0.332 | 0.489 | 1.476 |
| 6h | 360 | 0.356 | 0.344 | 0.240 | 0.290 | 0.557 | 0.270 | 0.443 | 1.420 |
| 24h | 1440 | 0.336 | 0.336 | 0.242 | 0.273 | 0.527 | 0.255 | 0.417 | 1.312 |
| 7d | 10080 | 0.364 | 0.360 | 0.276 | 0.308 | 0.526 | 0.260 | 0.468 | 1.287 |
| 30d | 43200 | 0.364 | 0.356 | 0.275 | 0.306 | 0.529 | 0.262 | 0.465 | 1.260 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.410 / 0.661 / 0.917; 2: 0.358 / 0.458 / 0.900; 3: 0.341 / 0.441 / 0.900; 4: 0.362 / 0.593 / 0.900; 5: 0.337 / 0.424 / 0.917; 6: 0.362 / 0.593 / 0.900; 7: 0.334 / 0.458 / 0.917; 8: 0.345 / 0.458 / 0.867; 9: 0.325 / 0.441 / 0.967; 10: 0.326 / 0.407 / 0.967; 11: 0.366 / 0.593 / 0.917; 12: 0.334 / 0.492 / 0.983; 13: 0.340 / 0.458 / 0.950; 14: 0.346 / 0.475 / 0.983; 15: 0.367 / 0.576 / 0.983
- 6h: 1: 0.356 / 0.557 / 0.900; 2: 0.331 / 0.463 / 0.900; 3: 0.331 / 0.497 / 0.886; 4: 0.329 / 0.509 / 0.856; 5: 0.334 / 0.494 / 0.892; 6: 0.328 / 0.517 / 0.883; 7: 0.335 / 0.503 / 0.911; 8: 0.331 / 0.463 / 0.908; 9: 0.335 / 0.497 / 0.956; 10: 0.330 / 0.483 / 0.956; 11: 0.318 / 0.460 / 0.925; 12: 0.335 / 0.520 / 0.944; 13: 0.323 / 0.477 / 0.931; 14: 0.335 / 0.480 / 0.936; 15: 0.328 / 0.517 / 0.933
- 24h: 1: 0.336 / 0.527 / 0.881; 2: 0.320 / 0.469 / 0.900; 3: 0.322 / 0.498 / 0.890; 4: 0.326 / 0.512 / 0.887; 5: 0.328 / 0.514 / 0.892; 6: 0.322 / 0.499 / 0.901; 7: 0.321 / 0.505 / 0.903; 8: 0.322 / 0.487 / 0.896; 9: 0.329 / 0.520 / 0.912; 10: 0.324 / 0.496 / 0.912; 11: 0.322 / 0.496 / 0.912; 12: 0.326 / 0.506 / 0.910; 13: 0.316 / 0.479 / 0.900; 14: 0.323 / 0.490 / 0.920; 15: 0.321 / 0.496 / 0.901
- 7d: 1: 0.364 / 0.526 / 0.896; 2: 0.353 / 0.491 / 0.900; 3: 0.357 / 0.513 / 0.899; 4: 0.354 / 0.501 / 0.899; 5: 0.354 / 0.507 / 0.899; 6: 0.353 / 0.510 / 0.899; 7: 0.352 / 0.501 / 0.899; 8: 0.350 / 0.501 / 0.900; 9: 0.353 / 0.507 / 0.900; 10: 0.350 / 0.497 / 0.900; 11: 0.351 / 0.501 / 0.900; 12: 0.351 / 0.503 / 0.900; 13: 0.350 / 0.499 / 0.900; 14: 0.350 / 0.500 / 0.900; 15: 0.351 / 0.507 / 0.901
- 30d: 1: 0.364 / 0.529 / 0.898; 2: 0.352 / 0.494 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.351 / 0.499 / 0.900; 5: 0.352 / 0.505 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.350 / 0.499 / 0.900; 8: 0.350 / 0.504 / 0.900; 9: 0.350 / 0.502 / 0.900; 10: 0.350 / 0.504 / 0.900; 11: 0.347 / 0.498 / 0.900; 12: 0.349 / 0.503 / 0.900; 13: 0.348 / 0.499 / 0.900; 14: 0.347 / 0.500 / 0.900; 15: 0.348 / 0.503 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.230 (body 0.186, range 0.274); 'price stays where it was' would score 0.156; colour right 0.508; typical miss of the close 2.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.149 (body 0.109, range 0.189); 'price stays where it was' would score 0.147; colour right 0.503; typical miss of the close 3.5 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.133 (body 0.098, range 0.168); 'price stays where it was' would score 0.129; colour right 0.518; typical miss of the close 4.0 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.123 (body 0.084, range 0.162); 'price stays where it was' would score 0.124; colour right 0.502; typical miss of the close 8.7 bp; chain ended on the right side 0.485 of 672 chains; n=10080
- 30d: match 0.125 (body 0.086, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.3 bp; chain ended on the right side 0.516 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.4; 2: 0.198 / 5.0; 3: 0.167 / 6.6; 4: 0.132 / 6.8; 5: 0.128 / 7.5; 6: 0.116 / 8.3; 7: 0.112 / 8.5; 8: 0.099 / 9.6; 9: 0.092 / 9.4; 10: 0.092 / 9.9; 11: 0.087 / 10.1; 12: 0.080 / 10.5; 13: 0.073 / 10.8; 14: 0.072 / 11.3; 15: 0.066 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 139332, probability skill vs chance 0.2131, widened contest next: True
  - now: threshold 0.8375, hit rate recent 0.8951 / long run 0.9265
    - 6h: 17 calls (69 a day), hit rate 0.824, chance 0.300, naive rule 0.502, lift 2.75x
    - 24h: 60 calls (60 a day), hit rate 0.900, chance 0.317, naive rule 0.537, lift 2.84x
    - 7d: 407 calls (58 a day), hit rate 0.909, chance 0.297, naive rule 0.500, lift 3.07x
    - 30d: 1745 calls (58 a day), hit rate 0.931, chance 0.296, naive rule 0.499, lift 3.15x
  - next: threshold 0.5655, hit rate recent 0.6252 / long run 0.6084
    - 6h: 5 calls (20 a day), hit rate 0.400, chance 0.300, lift 1.33x
    - 24h: 50 calls (50 a day), hit rate 0.640, chance 0.317, lift 2.02x
    - 7d: 509 calls (73 a day), hit rate 0.621, chance 0.297, lift 2.09x
    - 30d: 2968 calls (99 a day), hit rate 0.591, chance 0.296, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.501; 0.35: 534, 0.526; 0.40: 474, 0.582; 0.45: 406, 0.653; 0.50: 355, 0.702; 0.55: 308, 0.745; 0.60: 260, 0.789; 0.65: 219, 0.813; 0.70: 173, 0.845; 0.75: 139, 0.875; 0.80: 92, 0.907; 0.85: 46, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.431; 0.35: 499, 0.465; 0.40: 402, 0.502; 0.45: 304, 0.537; 0.50: 196, 0.571; 0.55: 88, 0.578; 0.60: 12, 0.661; 0.65: 1, 0.600
- **K=5**: model 1792540800, labels learned 139330, probability skill vs chance 0.208, widened contest next: False
  - now: threshold 0.6863, hit rate recent 0.8204 / long run 0.8211
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.187, naive rule 0.409, lift 4.38x
    - 24h: 47 calls (47 a day), hit rate 0.809, chance 0.191, naive rule 0.418, lift 4.24x
    - 7d: 388 calls (55 a day), hit rate 0.820, chance 0.187, naive rule 0.410, lift 4.37x
    - 30d: 1624 calls (54 a day), hit rate 0.820, chance 0.188, naive rule 0.409, lift 4.37x
  - next: threshold 0.4546, hit rate recent 0.5123 / long run 0.5136
    - 6h: 10 calls (41 a day), hit rate 0.600, chance 0.187, lift 3.21x
    - 24h: 59 calls (59 a day), hit rate 0.492, chance 0.191, lift 2.58x
    - 7d: 391 calls (56 a day), hit rate 0.535, chance 0.187, lift 2.85x
    - 30d: 2708 calls (90 a day), hit rate 0.486, chance 0.188, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.425; 0.35: 349, 0.490; 0.40: 282, 0.562; 0.45: 231, 0.613; 0.50: 186, 0.663; 0.55: 148, 0.699; 0.60: 113, 0.747; 0.65: 76, 0.785; 0.70: 48, 0.823; 0.75: 29, 0.853; 0.80: 11, 0.869
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.385; 0.35: 256, 0.423; 0.40: 159, 0.464; 0.45: 67, 0.492; 0.50: 11, 0.515; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 139327, probability skill vs chance 0.2028, widened contest next: False
  - now: threshold 0.5707, hit rate recent 0.709 / long run 0.6953
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.131, naive rule 0.355, lift 5.33x
    - 24h: 49 calls (49 a day), hit rate 0.714, chance 0.130, naive rule 0.362, lift 5.51x
    - 7d: 360 calls (51 a day), hit rate 0.694, chance 0.123, naive rule 0.344, lift 5.66x
    - 30d: 1533 calls (51 a day), hit rate 0.686, chance 0.121, naive rule 0.338, lift 5.66x
  - next: threshold 0.3578, hit rate recent 0.4109 / long run 0.4215
    - 6h: 6 calls (25 a day), hit rate 0.333, chance 0.131, lift 2.54x
    - 24h: 56 calls (56 a day), hit rate 0.375, chance 0.130, lift 2.89x
    - 7d: 378 calls (54 a day), hit rate 0.442, chance 0.123, lift 3.60x
    - 30d: 2632 calls (88 a day), hit rate 0.396, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.434; 0.35: 192, 0.496; 0.40: 152, 0.542; 0.45: 117, 0.588; 0.50: 84, 0.639; 0.55: 60, 0.674; 0.60: 40, 0.710; 0.65: 24, 0.780; 0.70: 12, 0.805; 0.75: 2, 0.764
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.364; 0.35: 88, 0.391; 0.40: 24, 0.422; 0.45: 4, 0.448; 0.50: 1, 0.708
- **K=13**: model 1793577600, labels learned 139322, probability skill vs chance 0.1776, widened contest next: True
  - now: threshold 0.4596, hit rate recent 0.5544 / long run 0.5683
    - 6h: 6 calls (25 a day), hit rate 0.500, chance 0.101, naive rule 0.340, lift 4.93x
    - 24h: 48 calls (49 a day), hit rate 0.521, chance 0.078, naive rule 0.276, lift 6.72x
    - 7d: 376 calls (54 a day), hit rate 0.566, chance 0.079, naive rule 0.286, lift 7.20x
    - 30d: 1647 calls (55 a day), hit rate 0.563, chance 0.078, naive rule 0.283, lift 7.24x
  - next: threshold 0.2847, hit rate recent 0.297 / long run 0.3304
    - 6h: 8 calls (33 a day), hit rate 0.250, chance 0.101, lift 2.46x
    - 24h: 62 calls (63 a day), hit rate 0.258, chance 0.078, lift 3.33x
    - 7d: 374 calls (54 a day), hit rate 0.348, chance 0.079, lift 4.42x
    - 30d: 1805 calls (60 a day), hit rate 0.325, chance 0.078, lift 4.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.438; 0.35: 94, 0.486; 0.40: 66, 0.544; 0.45: 45, 0.587; 0.50: 30, 0.645; 0.55: 20, 0.676; 0.60: 11, 0.710; 0.65: 4, 0.673; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.329; 0.35: 12, 0.346; 0.40: 3, 0.420; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.730 | 0.07% | 0.933 | 0.483 | 0.250 | 0.458 | 0.316 |
| 6h | 7.349 | 1.16% | 0.911 | 0.508 | 0.251 | 0.494 | 0.253 |
| 24h | 6.947 | 12.29% | 0.896 | 0.504 | 0.250 | 0.528 | 0.359 |
| 7d | 15.128 | 5.01% | 0.900 | 0.499 | 0.250 | 0.504 | 0.745 |
| 30d | 14.964 | 4.48% | 0.900 | 0.500 | 0.250 | 0.500 | 0.708 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.736 | 7.701 | 7.733 | 7.651 | 7.954 | 8.041 | 7.677 | 7.638 | 7.649 | 7.730 |
| 6h | 7.436 | 7.495 | 7.433 | 7.361 | 7.547 | 7.822 | 7.348 | 7.316 | 7.332 | 7.349 |
| 24h | 7.920 | 7.023 | 7.131 | 7.002 | 7.119 | 7.587 | 6.940 | 6.932 | 6.940 | 6.947 |
| 7d | 15.925 | 15.252 | 15.228 | 15.179 | 15.400 | 15.492 | 15.110 | 15.104 | 15.100 | 15.128 |
| 30d | 15.666 | 15.118 | 15.064 | 14.994 | 15.244 | 15.205 | 14.955 | 14.933 | 14.936 | 14.964 |

## Next candle

- candle starting 2026-11-07 22:18 UTC, last close 2229.94
- P(up) 0.5051, return quantiles (bp): {'05': -4.361, '10': -3.353, '25': -1.6, '40': -0.491, '50': 0.032, '60': 0.397, '75': 1.383, '90': 2.904, '95': 4.005}
- changepoint probability 0.0399, regime age 50.4 min
- agent weights: empirical 0.005, ewma 0.102, garch 0.091, har 0.164, bocpd 0.035, hmm 0.004, online_qr 0.277, lgbm 0.323

## Learning log

- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- HMM volatility states (sd, bp per minute): [3.63, 7.08, 18.92], current probabilities: [0.984, 0.015, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-07 22:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.234, 'l_abs': 0.65, 'l_hi': 0.749, 'l_lo': 0.694, 'b05': 0.654, 'b25': 0.617, 'b75': 0.599, 'b95': 0.656}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.557, 1.949, 2.492, 2.737, 2.773, 2.826, 2.968, 3.03, 3.265, 3.644, 3.738, 3.671, 3.817, 3.729]}
- calibration offsets (in sigma): {'05': -0.0115, '10': -0.033, '25': 0.0225, '40': 0.038, '50': 0.025, '60': -0.018, '75': -0.0225, '90': -0.067, '95': -0.0585}
