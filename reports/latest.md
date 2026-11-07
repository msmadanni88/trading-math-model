# ETH-USD 60s candle generator - report

- generated: 2026-11-07 13:57 UTC
- last closed candle: 2026-11-07 13:57 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k3_now 0.915 in the last 7 days, -0.037 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.484 (672) [0.454, 0.512] | 0.514 (2879) [0.498, 0.531] | 0.512 (6330) [0.500, 0.525] | 0.513 (3358) [0.496, 0.532] | 0.527 (55) | 0.500 | flat -0.042 (noise 0.027) |
| colour_clear | 0.577 (807) | 0.534 (5528) [0.516, 0.553] | 0.542 (23933) [0.536, 0.548] | 0.521 (51854) [0.515, 0.526] | 0.543 (27616) [0.537, 0.548] | 0.528 (439) | 0.500 | flat -0.004 (noise 0.012) |
| colour_confident | 0.646 (96) | 0.578 (888) [0.561, 0.600] | 0.595 (4261) [0.584, 0.605] | 0.597 (4987) [0.586, 0.609] | 0.597 (4987) [0.586, 0.609] | 0.548 (166) | 0.500 | flat -0.015 (noise 0.022) |
| colour_next | 0.554 (1436) | 0.530 (9980) [0.519, 0.541] | 0.529 (42874) [0.525, 0.533] | 0.516 (94331) [0.512, 0.520] | 0.529 (49982) [0.525, 0.533] | 0.503 (817) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.503 (139720) [0.501, 0.505] | 0.502 (600236) [0.500, 0.503] | 0.501 (1320634) [0.500, 0.502] | 0.501 (699748) [0.500, 0.502] | 0.500 (11438) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.550 (20) | 0.611 (198) [0.580, 0.639] | 0.626 (1104) [0.608, 0.645] | 0.629 (1303) [0.611, 0.648] | 0.629 (1303) [0.611, 0.648] | 0.617 (60) | 0.500 | flat +0.015 (noise 0.043) |
| reversal_k13_next | 0.358 (53) | 0.371 (369) [0.342, 0.399] | 0.327 (1809) [0.313, 0.342] | 0.313 (4315) [0.303, 0.324] | 0.326 (2210) [0.314, 0.338] | 0.233 (43) | 0.077 | flat +0.054 (noise 0.034) |
| reversal_k13_now | 0.633 (49) | 0.585 (393) [0.547, 0.620] | 0.566 (1650) [0.547, 0.586] | 0.574 (3412) [0.561, 0.588] | 0.569 (1940) [0.550, 0.587] | 0.516 (31) | 0.077 | flat +0.010 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.612 (610) [0.585, 0.638] | 0.588 (2988) [0.577, 0.599] | 0.587 (5844) [0.578, 0.596] | 0.587 (3404) [0.576, 0.598] | 0.641 (39) | 0.293 | flat +0.021 (noise 0.027) |
| reversal_k3_now | 0.933 (60) | 0.915 (422) [0.905, 0.924] | 0.932 (1753) [0.922, 0.942] | 0.936 (3789) [0.930, 0.943] | 0.932 (2026) [0.923, 0.941] | 0.971 (34) | 0.294 | down -0.037 (noise 0.017) |
| reversal_k5_next | 0.528 (36) | 0.539 (395) [0.516, 0.559] | 0.483 (2715) [0.469, 0.499] | 0.484 (5156) [0.473, 0.495] | 0.478 (3166) [0.464, 0.492] | 0.455 (44) | 0.187 | flat +0.032 (noise 0.033) |
| reversal_k5_now | 0.862 (58) | 0.818 (407) [0.802, 0.834] | 0.819 (1636) [0.809, 0.828] | 0.829 (3523) [0.820, 0.838] | 0.821 (1912) [0.811, 0.831] | 0.828 (29) | 0.187 | flat -0.012 (noise 0.027) |
| reversal_k8_next | 0.438 (48) | 0.461 (414) [0.440, 0.480] | 0.395 (2692) [0.381, 0.409] | 0.395 (5218) [0.385, 0.406] | 0.395 (3112) [0.381, 0.407] | 0.357 (42) | 0.121 | up +0.067 (noise 0.031) |
| reversal_k8_now | 0.719 (57) | 0.704 (371) [0.676, 0.728] | 0.683 (1548) [0.663, 0.702] | 0.701 (3431) [0.688, 0.715] | 0.690 (1844) [0.672, 0.708] | 0.710 (31) | 0.121 | flat +0.007 (noise 0.034) |
| overall | 0.507 (22038) | 0.508 (153753) [0.506, 0.509] | 0.505 (662780) [0.504, 0.506] | 0.504 (1455983) [0.503, 0.505] | 0.505 (772702) [0.504, 0.506] | 0.502 (12603) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.0767, 0.1157] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5288, 'levels': [{'threshold': 0.0767, 'calls_per_day': 147.2, 'win_rate': 0.571}, {'threshold': 0.1157, 'calls_per_day': 37.4, 'win_rate': 0.6151}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42858, 'rate': 0.5284}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15159 | 0.341 | 0.525 (14916) | 0.573 (2315) | 0.741 (2536) |
| volatility: normal | 15159 | 0.368 | 0.534 (15091) | 0.613 (1416) | 0.755 (2274) |
| volatility: wild | 15159 | 0.384 | 0.524 (15118) | 0.617 (807) | 0.766 (2099) |
| session: Asia 00-08 | 15360 | 0.364 | 0.534 (15252) | 0.599 (1604) | 0.759 (2248) |
| session: Europe 08-13 | 9600 | 0.359 | 0.534 (9499) | 0.595 (1220) | 0.749 (1584) |
| session: US 13-21 | 14937 | 0.372 | 0.524 (14841) | 0.594 (1141) | 0.754 (2273) |
| session: late 21-24 | 5580 | 0.354 | 0.512 (5533) | 0.574 (573) | 0.744 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.338 | 0.353 | 0.292 | 0.292 | 0.475 | 0.236 | 0.440 | 1.459 |
| 6h | 360 | 0.309 | 0.322 | 0.228 | 0.255 | 0.471 | 0.227 | 0.390 | 1.520 |
| 24h | 1440 | 0.350 | 0.352 | 0.261 | 0.293 | 0.522 | 0.254 | 0.447 | 1.202 |
| 7d | 10080 | 0.362 | 0.359 | 0.274 | 0.306 | 0.527 | 0.259 | 0.465 | 1.288 |
| 30d | 43200 | 0.364 | 0.357 | 0.276 | 0.307 | 0.528 | 0.262 | 0.466 | 1.255 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.338 / 0.475 / 0.867; 2: 0.344 / 0.492 / 0.867; 3: 0.346 / 0.542 / 0.883; 4: 0.325 / 0.508 / 0.883; 5: 0.341 / 0.475 / 0.733; 6: 0.327 / 0.441 / 0.833; 7: 0.293 / 0.288 / 0.783; 8: 0.328 / 0.441 / 0.767; 9: 0.339 / 0.492 / 0.650; 10: 0.324 / 0.458 / 0.633; 11: 0.351 / 0.525 / 0.700; 12: 0.373 / 0.627 / 0.683; 13: 0.352 / 0.542 / 0.700; 14: 0.357 / 0.576 / 0.683; 15: 0.346 / 0.458 / 0.767
- 6h: 1: 0.309 / 0.471 / 0.853; 2: 0.304 / 0.480 / 0.886; 3: 0.306 / 0.509 / 0.894; 4: 0.303 / 0.506 / 0.903; 5: 0.308 / 0.500 / 0.839; 6: 0.302 / 0.474 / 0.892; 7: 0.301 / 0.509 / 0.844; 8: 0.309 / 0.503 / 0.847; 9: 0.307 / 0.540 / 0.789; 10: 0.305 / 0.500 / 0.767; 11: 0.310 / 0.520 / 0.822; 12: 0.310 / 0.534 / 0.772; 13: 0.304 / 0.506 / 0.828; 14: 0.302 / 0.474 / 0.794; 15: 0.308 / 0.474 / 0.844
- 24h: 1: 0.350 / 0.522 / 0.885; 2: 0.339 / 0.473 / 0.887; 3: 0.345 / 0.517 / 0.892; 4: 0.344 / 0.508 / 0.897; 5: 0.346 / 0.521 / 0.885; 6: 0.342 / 0.499 / 0.909; 7: 0.339 / 0.499 / 0.887; 8: 0.339 / 0.494 / 0.895; 9: 0.343 / 0.515 / 0.878; 10: 0.342 / 0.500 / 0.875; 11: 0.347 / 0.519 / 0.885; 12: 0.339 / 0.496 / 0.873; 13: 0.335 / 0.479 / 0.890; 14: 0.339 / 0.492 / 0.877; 15: 0.337 / 0.485 / 0.892
- 7d: 1: 0.362 / 0.527 / 0.895; 2: 0.351 / 0.491 / 0.899; 3: 0.355 / 0.514 / 0.899; 4: 0.352 / 0.501 / 0.900; 5: 0.353 / 0.510 / 0.899; 6: 0.351 / 0.509 / 0.901; 7: 0.349 / 0.498 / 0.900; 8: 0.348 / 0.503 / 0.901; 9: 0.351 / 0.510 / 0.899; 10: 0.348 / 0.498 / 0.898; 11: 0.349 / 0.503 / 0.901; 12: 0.349 / 0.504 / 0.899; 13: 0.348 / 0.499 / 0.900; 14: 0.347 / 0.500 / 0.900; 15: 0.349 / 0.506 / 0.902
- 30d: 1: 0.364 / 0.528 / 0.898; 2: 0.352 / 0.495 / 0.900; 3: 0.355 / 0.509 / 0.900; 4: 0.351 / 0.499 / 0.900; 5: 0.352 / 0.506 / 0.900; 6: 0.350 / 0.502 / 0.900; 7: 0.350 / 0.499 / 0.900; 8: 0.350 / 0.504 / 0.900; 9: 0.350 / 0.502 / 0.899; 10: 0.350 / 0.504 / 0.899; 11: 0.348 / 0.498 / 0.900; 12: 0.349 / 0.503 / 0.899; 13: 0.348 / 0.499 / 0.900; 14: 0.348 / 0.501 / 0.899; 15: 0.349 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.076 (body 0.038, range 0.115); 'price stays where it was' would score 0.102; colour right 0.576; typical miss of the close 4.8 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.118 (body 0.081, range 0.154); 'price stays where it was' would score 0.106; colour right 0.517; typical miss of the close 3.9 bp; chain ended on the right side 0.375 of 24 chains; n=360
- 24h: match 0.132 (body 0.092, range 0.172); 'price stays where it was' would score 0.131; colour right 0.519; typical miss of the close 5.7 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.124; colour right 0.503; typical miss of the close 8.6 bp; chain ended on the right side 0.488 of 672 chains; n=10080
- 30d: match 0.125 (body 0.085, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.5 bp; chain ended on the right side 0.515 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.4; 2: 0.200 / 5.1; 3: 0.166 / 6.7; 4: 0.132 / 6.9; 5: 0.127 / 7.6; 6: 0.115 / 8.5; 7: 0.111 / 8.7; 8: 0.099 / 9.7; 9: 0.092 / 9.5; 10: 0.091 / 10.1; 11: 0.087 / 10.2; 12: 0.080 / 10.6; 13: 0.073 / 11.0; 14: 0.072 / 11.5; 15: 0.065 / 11.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 138831, probability skill vs chance 0.2203, widened contest next: False
  - now: threshold 0.8376, hit rate recent 0.9479 / long run 0.932
    - 6h: 22 calls (89 a day), hit rate 0.955, chance 0.332, naive rule 0.557, lift 2.87x
    - 24h: 52 calls (52 a day), hit rate 0.962, chance 0.324, naive rule 0.539, lift 2.97x
    - 7d: 413 calls (59 a day), hit rate 0.915, chance 0.298, naive rule 0.502, lift 3.08x
    - 30d: 1741 calls (58 a day), hit rate 0.933, chance 0.295, naive rule 0.498, lift 3.16x
  - next: threshold 0.566, hit rate recent 0.6311 / long run 0.6086
    - 6h: 15 calls (61 a day), hit rate 0.600, chance 0.332, lift 1.81x
    - 24h: 46 calls (46 a day), hit rate 0.630, chance 0.324, lift 1.95x
    - 7d: 551 calls (79 a day), hit rate 0.624, chance 0.298, lift 2.10x
    - 30d: 2989 calls (100 a day), hit rate 0.588, chance 0.295, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.501; 0.35: 533, 0.526; 0.40: 474, 0.582; 0.45: 406, 0.653; 0.50: 356, 0.702; 0.55: 308, 0.746; 0.60: 260, 0.790; 0.65: 219, 0.815; 0.70: 173, 0.846; 0.75: 139, 0.877; 0.80: 92, 0.908; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.431; 0.35: 499, 0.465; 0.40: 402, 0.501; 0.45: 304, 0.537; 0.50: 196, 0.570; 0.55: 89, 0.577; 0.60: 12, 0.648; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 138829, probability skill vs chance 0.2121, widened contest next: False
  - now: threshold 0.6867, hit rate recent 0.8409 / long run 0.823
    - 6h: 19 calls (78 a day), hit rate 0.895, chance 0.194, naive rule 0.404, lift 4.61x
    - 24h: 52 calls (52 a day), hit rate 0.827, chance 0.189, naive rule 0.415, lift 4.37x
    - 7d: 399 calls (57 a day), hit rate 0.817, chance 0.187, naive rule 0.410, lift 4.36x
    - 30d: 1626 calls (54 a day), hit rate 0.820, chance 0.187, naive rule 0.408, lift 4.38x
  - next: threshold 0.4549, hit rate recent 0.4912 / long run 0.5115
    - 6h: 22 calls (90 a day), hit rate 0.500, chance 0.194, lift 2.58x
    - 24h: 52 calls (52 a day), hit rate 0.423, chance 0.189, lift 2.24x
    - 7d: 399 calls (57 a day), hit rate 0.531, chance 0.187, lift 2.84x
    - 30d: 2725 calls (91 a day), hit rate 0.483, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.425; 0.35: 349, 0.489; 0.40: 282, 0.562; 0.45: 231, 0.613; 0.50: 185, 0.664; 0.55: 148, 0.699; 0.60: 112, 0.748; 0.65: 76, 0.788; 0.70: 48, 0.824; 0.75: 29, 0.856; 0.80: 11, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.385; 0.35: 256, 0.423; 0.40: 160, 0.463; 0.45: 67, 0.488; 0.50: 11, 0.506; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 138826, probability skill vs chance 0.2051, widened contest next: False
  - now: threshold 0.5705, hit rate recent 0.7155 / long run 0.6955
    - 6h: 22 calls (91 a day), hit rate 0.773, chance 0.137, naive rule 0.348, lift 5.63x
    - 24h: 52 calls (52 a day), hit rate 0.712, chance 0.128, naive rule 0.354, lift 5.54x
    - 7d: 367 calls (52 a day), hit rate 0.700, chance 0.122, naive rule 0.343, lift 5.75x
    - 30d: 1544 calls (51 a day), hit rate 0.685, chance 0.121, naive rule 0.337, lift 5.66x
  - next: threshold 0.3582, hit rate recent 0.399 / long run 0.4206
    - 6h: 24 calls (99 a day), hit rate 0.333, chance 0.137, lift 2.43x
    - 24h: 60 calls (60 a day), hit rate 0.367, chance 0.128, lift 2.86x
    - 7d: 385 calls (55 a day), hit rate 0.455, chance 0.122, lift 3.73x
    - 30d: 2668 calls (89 a day), hit rate 0.394, chance 0.121, lift 3.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.433; 0.35: 192, 0.496; 0.40: 152, 0.542; 0.45: 117, 0.589; 0.50: 84, 0.640; 0.55: 60, 0.675; 0.60: 40, 0.708; 0.65: 24, 0.781; 0.70: 12, 0.803; 0.75: 2, 0.757
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 172, 0.363; 0.35: 89, 0.389; 0.40: 24, 0.415; 0.45: 4, 0.440; 0.50: 1, 0.692
- **K=13**: model 1793577600, labels learned 138821, probability skill vs chance 0.1812, widened contest next: True
  - now: threshold 0.4585, hit rate recent 0.5771 / long run 0.5706
    - 6h: 19 calls (79 a day), hit rate 0.579, chance 0.057, naive rule 0.183, lift 10.24x
    - 24h: 53 calls (54 a day), hit rate 0.566, chance 0.072, naive rule 0.259, lift 7.91x
    - 7d: 385 calls (55 a day), hit rate 0.571, chance 0.079, naive rule 0.287, lift 7.25x
    - 30d: 1653 calls (55 a day), hit rate 0.565, chance 0.078, naive rule 0.282, lift 7.28x
  - next: threshold 0.2853, hit rate recent 0.2828 / long run 0.3298
    - 6h: 22 calls (92 a day), hit rate 0.182, chance 0.057, lift 3.22x
    - 24h: 63 calls (64 a day), hit rate 0.270, chance 0.072, lift 3.77x
    - 7d: 376 calls (54 a day), hit rate 0.356, chance 0.079, lift 4.52x
    - 30d: 1811 calls (60 a day), hit rate 0.325, chance 0.078, lift 4.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.437; 0.35: 94, 0.486; 0.40: 66, 0.546; 0.45: 46, 0.590; 0.50: 30, 0.647; 0.55: 20, 0.677; 0.60: 11, 0.713; 0.65: 3, 0.676; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.328; 0.35: 13, 0.342; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.110 | 9.18% | 0.900 | 0.483 | 0.253 | 0.525 | 0.349 |
| 6h | 5.869 | 14.24% | 0.872 | 0.517 | 0.249 | 0.557 | 0.253 |
| 24h | 11.801 | 9.89% | 0.895 | 0.510 | 0.249 | 0.528 | 0.825 |
| 7d | 15.122 | 5.06% | 0.899 | 0.500 | 0.250 | 0.507 | 0.747 |
| 30d | 15.157 | 4.58% | 0.900 | 0.500 | 0.250 | 0.500 | 0.710 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.728 | 6.125 | 6.185 | 6.122 | 6.132 | 6.599 | 6.107 | 6.075 | 6.092 | 6.110 |
| 6h | 6.844 | 5.889 | 6.101 | 5.936 | 5.999 | 6.766 | 5.882 | 5.868 | 5.871 | 5.869 |
| 24h | 13.097 | 11.874 | 11.990 | 11.915 | 12.016 | 12.370 | 11.762 | 11.769 | 11.778 | 11.801 |
| 7d | 15.927 | 15.245 | 15.228 | 15.174 | 15.400 | 15.489 | 15.104 | 15.101 | 15.095 | 15.122 |
| 30d | 15.885 | 15.312 | 15.257 | 15.188 | 15.437 | 15.403 | 15.148 | 15.126 | 15.129 | 15.157 |

## Next candle

- candle starting 2026-11-07 13:57 UTC, last close 2242.1
- P(up) 0.5367, return quantiles (bp): {'05': -3.371, '10': -2.419, '25': -1.095, '40': -0.202, '50': 0.112, '60': 0.315, '75': 1.058, '90': 2.237, '95': 3.243}
- changepoint probability 0.0154, regime age 514.4 min
- agent weights: empirical 0.003, ewma 0.188, garch 0.049, har 0.142, bocpd 0.074, hmm 0.003, online_qr 0.262, lgbm 0.280

## Learning log

- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- 2026-11-07 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.922}, "hmm": {"sd_bp": [3.63, 7.08, 18.92], "stay": [0.987, 0.973, 0.925]}}
- HMM volatility states (sd, bp per minute): [3.63, 7.08, 18.92], current probabilities: [0.986, 0.013, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-11-07 14:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.236, 'l_abs': 0.657, 'l_hi': 0.739, 'l_lo': 0.716, 'b05': 0.668, 'b25': 0.623, 'b75': 0.545, 'b95': 0.63}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.759, 1.914, 2.086, 2.97, 2.464, 3.39, 3.286, 4.907, 5.961, 4.459, 6.175, 4.771, 5.821, 4.749]}
- calibration offsets (in sigma): {'05': -0.012, '10': 0.036, '25': 0.07, '40': 0.104, '50': 0.05, '60': -0.024, '75': -0.04, '90': -0.076, '95': -0.008}
