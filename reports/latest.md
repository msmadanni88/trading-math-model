# ETH-USD 60s candle generator - report

- generated: 2026-11-07 18:38 UTC
- last closed candle: 2026-11-07 18:38 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k3_now 0.915 in the last 7 days, -0.037 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.484 (672) [0.454, 0.512] | 0.514 (2879) [0.498, 0.531] | 0.512 (6330) [0.500, 0.525] | 0.513 (3358) [0.496, 0.532] | 0.513 (74) | 0.500 | flat -0.042 (noise 0.027) |
| colour_clear | 0.577 (807) | 0.534 (5528) [0.516, 0.553] | 0.542 (23933) [0.536, 0.548] | 0.521 (51854) [0.515, 0.526] | 0.543 (27616) [0.537, 0.548] | 0.547 (568) | 0.500 | flat -0.004 (noise 0.012) |
| colour_confident | 0.646 (96) | 0.578 (888) [0.561, 0.600] | 0.595 (4261) [0.584, 0.605] | 0.597 (4987) [0.586, 0.609] | 0.597 (4987) [0.586, 0.609] | 0.550 (198) | 0.500 | flat -0.015 (noise 0.022) |
| colour_next | 0.554 (1436) | 0.530 (9980) [0.519, 0.541] | 0.529 (42874) [0.525, 0.533] | 0.516 (94331) [0.512, 0.520] | 0.529 (49982) [0.525, 0.533] | 0.523 (1086) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.503 (139720) [0.501, 0.505] | 0.502 (600236) [0.500, 0.503] | 0.501 (1320634) [0.500, 0.502] | 0.501 (699748) [0.500, 0.502] | 0.499 (15204) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.550 (20) | 0.611 (198) [0.580, 0.639] | 0.626 (1104) [0.608, 0.645] | 0.629 (1303) [0.611, 0.648] | 0.629 (1303) [0.611, 0.648] | 0.621 (66) | 0.500 | flat +0.015 (noise 0.043) |
| reversal_k13_next | 0.358 (53) | 0.371 (369) [0.342, 0.399] | 0.327 (1809) [0.313, 0.342] | 0.313 (4315) [0.303, 0.324] | 0.326 (2210) [0.314, 0.338] | 0.296 (54) | 0.077 | flat +0.054 (noise 0.034) |
| reversal_k13_now | 0.633 (49) | 0.585 (393) [0.547, 0.620] | 0.566 (1650) [0.547, 0.586] | 0.574 (3412) [0.561, 0.588] | 0.569 (1940) [0.550, 0.587] | 0.513 (39) | 0.077 | flat +0.010 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.612 (610) [0.585, 0.638] | 0.588 (2988) [0.577, 0.599] | 0.587 (5844) [0.578, 0.596] | 0.587 (3404) [0.576, 0.598] | 0.667 (45) | 0.293 | flat +0.021 (noise 0.027) |
| reversal_k3_now | 0.933 (60) | 0.915 (422) [0.905, 0.924] | 0.932 (1753) [0.922, 0.942] | 0.936 (3789) [0.930, 0.943] | 0.932 (2026) [0.923, 0.941] | 0.933 (45) | 0.294 | down -0.037 (noise 0.017) |
| reversal_k5_next | 0.528 (36) | 0.539 (395) [0.516, 0.559] | 0.483 (2715) [0.469, 0.499] | 0.484 (5156) [0.473, 0.495] | 0.478 (3166) [0.464, 0.492] | 0.509 (53) | 0.187 | flat +0.032 (noise 0.033) |
| reversal_k5_now | 0.862 (58) | 0.818 (407) [0.802, 0.834] | 0.819 (1636) [0.809, 0.828] | 0.829 (3523) [0.820, 0.838] | 0.821 (1912) [0.811, 0.831] | 0.800 (35) | 0.187 | flat -0.012 (noise 0.027) |
| reversal_k8_next | 0.438 (48) | 0.461 (414) [0.440, 0.480] | 0.395 (2692) [0.381, 0.409] | 0.395 (5218) [0.385, 0.406] | 0.395 (3112) [0.381, 0.407] | 0.400 (50) | 0.121 | up +0.067 (noise 0.031) |
| reversal_k8_now | 0.719 (57) | 0.704 (371) [0.676, 0.728] | 0.683 (1548) [0.663, 0.702] | 0.701 (3431) [0.688, 0.715] | 0.690 (1844) [0.672, 0.708] | 0.711 (38) | 0.121 | flat +0.007 (noise 0.034) |
| overall | 0.507 (22038) | 0.508 (153753) [0.506, 0.509] | 0.505 (662780) [0.504, 0.506] | 0.504 (1455983) [0.503, 0.505] | 0.505 (772702) [0.504, 0.506] | 0.502 (16723) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07698, 0.1163] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5273, 'levels': [{'threshold': 0.07698, 'calls_per_day': 146.0, 'win_rate': 0.5735}, {'threshold': 0.1163, 'calls_per_day': 36.4, 'win_rate': 0.624}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42846, 'rate': 0.5288}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15253 | 0.341 | 0.526 (14999) | 0.573 (2330) | 0.740 (2546) |
| volatility: normal | 15252 | 0.368 | 0.535 (15183) | 0.612 (1429) | 0.754 (2278) |
| volatility: wild | 15253 | 0.384 | 0.524 (15212) | 0.617 (811) | 0.768 (2117) |
| session: Asia 00-08 | 15360 | 0.364 | 0.534 (15252) | 0.599 (1604) | 0.759 (2248) |
| session: Europe 08-13 | 9600 | 0.359 | 0.534 (9499) | 0.595 (1220) | 0.749 (1584) |
| session: US 13-21 | 15218 | 0.371 | 0.525 (15110) | 0.593 (1173) | 0.753 (2305) |
| session: late 21-24 | 5580 | 0.354 | 0.512 (5533) | 0.574 (573) | 0.744 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.349 | 0.333 | 0.235 | 0.235 | 0.586 | 0.249 | 0.448 | 1.818 |
| 6h | 360 | 0.341 | 0.332 | 0.251 | 0.277 | 0.553 | 0.262 | 0.419 | 1.309 |
| 24h | 1440 | 0.338 | 0.338 | 0.252 | 0.281 | 0.524 | 0.251 | 0.425 | 1.339 |
| 7d | 10080 | 0.363 | 0.359 | 0.275 | 0.306 | 0.527 | 0.260 | 0.466 | 1.291 |
| 30d | 43200 | 0.364 | 0.357 | 0.275 | 0.306 | 0.529 | 0.262 | 0.465 | 1.257 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.349 / 0.586 / 0.950; 2: 0.335 / 0.431 / 0.967; 3: 0.337 / 0.552 / 0.950; 4: 0.346 / 0.552 / 0.950; 5: 0.320 / 0.448 / 1.000; 6: 0.330 / 0.483 / 0.950; 7: 0.306 / 0.414 / 1.000; 8: 0.337 / 0.466 / 0.983; 9: 0.337 / 0.500 / 1.000; 10: 0.344 / 0.603 / 1.000; 11: 0.308 / 0.414 / 1.000; 12: 0.328 / 0.534 / 1.000; 13: 0.334 / 0.517 / 1.000; 14: 0.302 / 0.379 / 1.000; 15: 0.305 / 0.431 / 1.000
- 6h: 1: 0.341 / 0.553 / 0.903; 2: 0.313 / 0.435 / 0.931; 3: 0.322 / 0.507 / 0.925; 4: 0.309 / 0.496 / 0.933; 5: 0.321 / 0.499 / 0.919; 6: 0.317 / 0.493 / 0.900; 7: 0.311 / 0.461 / 0.911; 8: 0.318 / 0.484 / 0.897; 9: 0.323 / 0.507 / 0.886; 10: 0.320 / 0.504 / 0.900; 11: 0.315 / 0.493 / 0.886; 12: 0.326 / 0.516 / 0.906; 13: 0.319 / 0.527 / 0.892; 14: 0.320 / 0.487 / 0.897; 15: 0.321 / 0.516 / 0.892
- 24h: 1: 0.338 / 0.524 / 0.886; 2: 0.326 / 0.472 / 0.899; 3: 0.331 / 0.511 / 0.899; 4: 0.331 / 0.509 / 0.904; 5: 0.332 / 0.514 / 0.900; 6: 0.328 / 0.498 / 0.919; 7: 0.325 / 0.495 / 0.897; 8: 0.328 / 0.494 / 0.908; 9: 0.332 / 0.512 / 0.886; 10: 0.330 / 0.498 / 0.890; 11: 0.329 / 0.505 / 0.891; 12: 0.330 / 0.499 / 0.887; 13: 0.324 / 0.490 / 0.895; 14: 0.327 / 0.491 / 0.894; 15: 0.327 / 0.493 / 0.897
- 7d: 1: 0.363 / 0.527 / 0.896; 2: 0.351 / 0.489 / 0.900; 3: 0.355 / 0.513 / 0.900; 4: 0.352 / 0.501 / 0.901; 5: 0.353 / 0.508 / 0.900; 6: 0.351 / 0.510 / 0.901; 7: 0.350 / 0.500 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.351 / 0.508 / 0.899; 10: 0.349 / 0.499 / 0.899; 11: 0.349 / 0.503 / 0.900; 12: 0.349 / 0.503 / 0.900; 13: 0.349 / 0.499 / 0.900; 14: 0.348 / 0.500 / 0.900; 15: 0.349 / 0.507 / 0.901
- 30d: 1: 0.364 / 0.529 / 0.898; 2: 0.352 / 0.494 / 0.900; 3: 0.355 / 0.510 / 0.900; 4: 0.351 / 0.499 / 0.900; 5: 0.352 / 0.506 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.350 / 0.499 / 0.900; 8: 0.350 / 0.504 / 0.900; 9: 0.350 / 0.502 / 0.900; 10: 0.350 / 0.504 / 0.900; 11: 0.347 / 0.498 / 0.900; 12: 0.349 / 0.503 / 0.900; 13: 0.348 / 0.500 / 0.900; 14: 0.348 / 0.501 / 0.900; 15: 0.348 / 0.503 / 0.901

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.147 (body 0.096, range 0.199); 'price stays where it was' would score 0.138; colour right 0.517; typical miss of the close 2.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.117 (body 0.081, range 0.152); 'price stays where it was' would score 0.130; colour right 0.527; typical miss of the close 4.0 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.129 (body 0.092, range 0.167); 'price stays where it was' would score 0.134; colour right 0.512; typical miss of the close 4.5 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.123; colour right 0.503; typical miss of the close 8.6 bp; chain ended on the right side 0.482 of 672 chains; n=10080
- 30d: match 0.125 (body 0.086, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.4 bp; chain ended on the right side 0.515 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.4; 2: 0.198 / 5.1; 3: 0.167 / 6.6; 4: 0.132 / 6.9; 5: 0.127 / 7.6; 6: 0.115 / 8.3; 7: 0.112 / 8.6; 8: 0.099 / 9.6; 9: 0.092 / 9.5; 10: 0.092 / 10.0; 11: 0.087 / 10.2; 12: 0.080 / 10.5; 13: 0.073 / 10.9; 14: 0.072 / 11.3; 15: 0.065 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 139112, probability skill vs chance 0.2149, widened contest next: False
  - now: threshold 0.8375, hit rate recent 0.9268 / long run 0.9299
    - 6h: 13 calls (53 a day), hit rate 0.846, chance 0.321, naive rule 0.555, lift 2.63x
    - 24h: 56 calls (56 a day), hit rate 0.946, chance 0.319, naive rule 0.534, lift 2.97x
    - 7d: 405 calls (58 a day), hit rate 0.916, chance 0.298, naive rule 0.503, lift 3.07x
    - 30d: 1744 calls (58 a day), hit rate 0.932, chance 0.296, naive rule 0.498, lift 3.15x
  - next: threshold 0.5655, hit rate recent 0.6512 / long run 0.6108
    - 6h: 8 calls (32 a day), hit rate 0.750, chance 0.321, lift 2.34x
    - 24h: 49 calls (49 a day), hit rate 0.653, chance 0.319, lift 2.05x
    - 7d: 528 calls (75 a day), hit rate 0.625, chance 0.298, lift 2.10x
    - 30d: 2983 calls (99 a day), hit rate 0.590, chance 0.296, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.501; 0.35: 534, 0.526; 0.40: 474, 0.582; 0.45: 406, 0.653; 0.50: 355, 0.702; 0.55: 308, 0.745; 0.60: 260, 0.789; 0.65: 219, 0.814; 0.70: 173, 0.846; 0.75: 139, 0.877; 0.80: 92, 0.909; 0.85: 46, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.431; 0.35: 500, 0.465; 0.40: 402, 0.501; 0.45: 304, 0.537; 0.50: 196, 0.570; 0.55: 89, 0.578; 0.60: 12, 0.658; 0.65: 1, 0.600
- **K=5**: model 1792540800, labels learned 139110, probability skill vs chance 0.2062, widened contest next: False
  - now: threshold 0.6863, hit rate recent 0.8247 / long run 0.8214
    - 6h: 9 calls (37 a day), hit rate 0.778, chance 0.208, naive rule 0.436, lift 3.74x
    - 24h: 47 calls (47 a day), hit rate 0.830, chance 0.195, naive rule 0.416, lift 4.25x
    - 7d: 388 calls (55 a day), hit rate 0.825, chance 0.188, naive rule 0.411, lift 4.39x
    - 30d: 1623 calls (54 a day), hit rate 0.820, chance 0.188, naive rule 0.409, lift 4.37x
  - next: threshold 0.4546, hit rate recent 0.5324 / long run 0.5154
    - 6h: 16 calls (65 a day), hit rate 0.625, chance 0.208, lift 3.00x
    - 24h: 55 calls (55 a day), hit rate 0.491, chance 0.195, lift 2.51x
    - 7d: 393 calls (56 a day), hit rate 0.539, chance 0.188, lift 2.87x
    - 30d: 2716 calls (91 a day), hit rate 0.485, chance 0.188, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.425; 0.35: 349, 0.490; 0.40: 281, 0.563; 0.45: 231, 0.614; 0.50: 186, 0.664; 0.55: 148, 0.700; 0.60: 113, 0.748; 0.65: 76, 0.788; 0.70: 48, 0.824; 0.75: 29, 0.854; 0.80: 11, 0.868
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.385; 0.35: 256, 0.423; 0.40: 160, 0.463; 0.45: 67, 0.491; 0.50: 11, 0.514; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 139107, probability skill vs chance 0.2029, widened contest next: False
  - now: threshold 0.5707, hit rate recent 0.7162 / long run 0.6957
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.131, naive rule 0.372, lift 5.71x
    - 24h: 50 calls (50 a day), hit rate 0.720, chance 0.127, naive rule 0.348, lift 5.67x
    - 7d: 358 calls (51 a day), hit rate 0.701, chance 0.122, naive rule 0.343, lift 5.74x
    - 30d: 1537 calls (51 a day), hit rate 0.686, chance 0.121, naive rule 0.338, lift 5.67x
  - next: threshold 0.3578, hit rate recent 0.4294 / long run 0.4234
    - 6h: 15 calls (62 a day), hit rate 0.533, chance 0.131, lift 4.06x
    - 24h: 54 calls (54 a day), hit rate 0.389, chance 0.127, lift 3.06x
    - 7d: 379 calls (54 a day), hit rate 0.451, chance 0.122, lift 3.70x
    - 30d: 2648 calls (88 a day), hit rate 0.396, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.434; 0.35: 191, 0.496; 0.40: 152, 0.543; 0.45: 117, 0.589; 0.50: 84, 0.640; 0.55: 60, 0.676; 0.60: 40, 0.709; 0.65: 24, 0.780; 0.70: 12, 0.806; 0.75: 2, 0.761
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.363; 0.35: 89, 0.391; 0.40: 24, 0.422; 0.45: 4, 0.457; 0.50: 1, 0.720
- **K=13**: model 1793577600, labels learned 139102, probability skill vs chance 0.1788, widened contest next: False
  - now: threshold 0.4596, hit rate recent 0.5682 / long run 0.5697
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.093, naive rule 0.368, lift 6.29x
    - 24h: 52 calls (53 a day), hit rate 0.538, chance 0.073, naive rule 0.261, lift 7.38x
    - 7d: 378 calls (54 a day), hit rate 0.577, chance 0.079, naive rule 0.288, lift 7.32x
    - 30d: 1651 calls (55 a day), hit rate 0.565, chance 0.078, naive rule 0.283, lift 7.26x
  - next: threshold 0.2847, hit rate recent 0.3285 / long run 0.3337
    - 6h: 16 calls (67 a day), hit rate 0.438, chance 0.093, lift 4.72x
    - 24h: 61 calls (62 a day), hit rate 0.279, chance 0.073, lift 3.82x
    - 7d: 375 calls (54 a day), hit rate 0.360, chance 0.079, lift 4.57x
    - 30d: 1806 calls (60 a day), hit rate 0.327, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 130, 0.438; 0.35: 94, 0.487; 0.40: 66, 0.545; 0.45: 45, 0.589; 0.50: 30, 0.647; 0.55: 20, 0.678; 0.60: 11, 0.712; 0.65: 4, 0.673; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.331; 0.35: 12, 0.346; 0.40: 3, 0.420; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.035 | 2.92% | 0.950 | 0.633 | 0.248 | 0.552 | -0.175 |
| 6h | 7.589 | 3.60% | 0.911 | 0.497 | 0.251 | 0.513 | 0.329 |
| 24h | 7.781 | 12.71% | 0.899 | 0.508 | 0.250 | 0.522 | 0.550 |
| 7d | 15.121 | 5.03% | 0.900 | 0.500 | 0.250 | 0.506 | 0.746 |
| 30d | 14.999 | 4.47% | 0.900 | 0.500 | 0.250 | 0.500 | 0.707 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.186 | 5.107 | 5.002 | 4.966 | 5.175 | 5.775 | 5.142 | 5.037 | 5.056 | 5.035 |
| 6h | 7.873 | 7.770 | 7.704 | 7.632 | 7.900 | 8.088 | 7.557 | 7.544 | 7.571 | 7.589 |
| 24h | 8.914 | 7.872 | 7.980 | 7.861 | 7.971 | 8.354 | 7.773 | 7.756 | 7.773 | 7.781 |
| 7d | 15.922 | 15.247 | 15.227 | 15.172 | 15.402 | 15.492 | 15.103 | 15.098 | 15.094 | 15.121 |
| 30d | 15.701 | 15.152 | 15.099 | 15.030 | 15.278 | 15.238 | 14.989 | 14.968 | 14.971 | 14.999 |

## Next candle

- candle starting 2026-11-07 18:38 UTC, last close 2233.7
- P(up) 0.5281, return quantiles (bp): {'05': -3.866, '10': -2.821, '25': -1.234, '40': -0.204, '50': 0.076, '60': 0.473, '75': 1.24, '90': 2.607, '95': 3.564}
- changepoint probability 0.0236, regime age 92.5 min
- agent weights: empirical 0.003, ewma 0.083, garch 0.056, har 0.169, bocpd 0.026, hmm 0.003, online_qr 0.307, lgbm 0.354

## Learning log

- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- HMM volatility states (sd, bp per minute): [3.63, 7.08, 18.92], current probabilities: [0.985, 0.014, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-07 18:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.229, 'l_abs': 0.665, 'l_hi': 0.746, 'l_lo': 0.697, 'b05': 0.664, 'b25': 0.626, 'b75': 0.606, 'b95': 0.662}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.3, 1.473, 1.542, 1.987, 2.054, 2.361, 2.479, 3.486, 3.681, 3.363, 3.89, 3.527, 3.742, 3.582]}
- calibration offsets (in sigma): {'05': 0.0085, '10': 0.007, '25': 0.0425, '40': 0.058, '50': -0.005, '60': -0.038, '75': -0.0725, '90': -0.067, '95': -0.0485}
