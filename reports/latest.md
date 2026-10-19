# ETH-USD 60s candle generator - report

- generated: 2026-10-19 14:03 UTC
- last closed candle: 2026-10-19 14:03 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.615 (96) | 0.527 (672) [0.495, 0.561] | 0.522 (2875) [0.504, 0.542] | 0.512 (4506) [0.497, 0.527] | 0.514 (1534) [0.486, 0.543] | 0.518 (56) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.555 (785) | 0.545 (5567) [0.537, 0.555] | 0.522 (23331) [0.514, 0.530] | 0.513 (36607) [0.506, 0.519] | 0.544 (12369) [0.539, 0.550] | 0.573 (487) | 0.500 | flat +0.004 (noise 0.009) |
| colour_confident | 0.568 (139) | 0.584 (630) [0.568, 0.603] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.600 (2050) [0.580, 0.620] | 0.727 (88) | 0.500 | flat -0.018 (noise 0.025) |
| colour_next | 0.520 (1430) | 0.526 (10017) [0.519, 0.534] | 0.515 (42854) [0.509, 0.520] | 0.510 (67147) [0.505, 0.514] | 0.528 (22798) [0.523, 0.533] | 0.569 (839) | 0.500 | flat -0.001 (noise 0.007) |
| colour_path | 0.504 (20020) | 0.502 (140238) [0.499, 0.505] | 0.501 (599956) [0.500, 0.503] | 0.501 (940058) [0.500, 0.502] | 0.500 (319172) [0.498, 0.503] | 0.506 (11746) | 0.500 | flat +0.003 (noise 0.003) |
| colour_strong | 0.583 (36) | 0.616 (138) [0.574, 0.680] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.647 (535) [0.614, 0.683] | 0.739 (23) | 0.500 | flat -0.044 (noise 0.050) |
| reversal_k13_next | 0.309 (81) | 0.296 (433) [0.281, 0.310] | 0.312 (2060) [0.298, 0.327] | 0.306 (3218) [0.294, 0.318] | 0.318 (1113) [0.305, 0.330] | 0.302 (53) | 0.077 | flat -0.034 (noise 0.030) |
| reversal_k13_now | 0.469 (64) | 0.543 (381) [0.510, 0.582] | 0.584 (1534) [0.564, 0.605] | 0.577 (2349) [0.561, 0.595] | 0.571 (877) [0.548, 0.599] | 0.500 (28) | 0.077 | flat -0.029 (noise 0.036) |
| reversal_k3_next | 0.584 (101) | 0.566 (737) [0.555, 0.578] | 0.578 (2604) [0.565, 0.592] | 0.582 (3964) [0.572, 0.594] | 0.574 (1524) [0.560, 0.590] | 0.532 (77) | 0.293 | flat -0.026 (noise 0.028) |
| reversal_k3_now | 0.946 (55) | 0.938 (373) [0.913, 0.964] | 0.938 (1718) [0.929, 0.947] | 0.937 (2681) [0.931, 0.945] | 0.929 (918) [0.918, 0.941] | 0.964 (28) | 0.293 | flat +0.016 (noise 0.018) |
| reversal_k5_next | 0.434 (152) | 0.458 (799) [0.439, 0.484] | 0.472 (2424) [0.457, 0.489] | 0.478 (3519) [0.464, 0.492] | 0.457 (1529) [0.440, 0.477] | 0.433 (90) | 0.187 | flat -0.012 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.810 (348) [0.784, 0.838] | 0.832 (1608) [0.816, 0.847] | 0.832 (2457) [0.819, 0.844] | 0.820 (846) [0.800, 0.840] | 0.844 (32) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k8_next | 0.393 (117) | 0.378 (667) [0.348, 0.403] | 0.400 (2238) [0.381, 0.419] | 0.391 (3547) [0.379, 0.405] | 0.385 (1441) [0.365, 0.404] | 0.378 (74) | 0.121 | flat -0.003 (noise 0.027) |
| reversal_k8_now | 0.651 (43) | 0.681 (335) [0.657, 0.706] | 0.719 (1571) [0.698, 0.739] | 0.707 (2450) [0.691, 0.723] | 0.695 (863) [0.670, 0.721] | 0.560 (25) | 0.122 | flat -0.004 (noise 0.034) |
| overall | 0.506 (22206) | 0.505 (155000) [0.502, 0.507] | 0.504 (661442) [0.503, 0.505] | 0.503 (1035896) [0.502, 0.504] | 0.504 (352615) [0.502, 0.506] | 0.510 (13048) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06497, 0.09767] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5279, 'levels': [{'threshold': 0.06497, 'calls_per_day': 143.3, 'win_rate': 0.5709}, {'threshold': 0.09767, 'calls_per_day': 35.4, 'win_rate': 0.6386}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 22499, 'rate': 0.5302}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15161 | 0.336 | 0.523 (14913) | 0.593 (1429) | 0.772 (2480) |
| volatility: normal | 15161 | 0.363 | 0.517 (15095) | 0.619 (514) | 0.765 (2237) |
| volatility: wild | 15161 | 0.378 | 0.508 (15117) | 0.656 (195) | 0.773 (2049) |
| session: Asia 00-08 | 15360 | 0.357 | 0.521 (15256) | 0.612 (804) | 0.770 (2288) |
| session: Europe 08-13 | 9600 | 0.353 | 0.516 (9514) | 0.586 (555) | 0.773 (1496) |
| session: US 13-21 | 14943 | 0.367 | 0.511 (14839) | 0.587 (492) | 0.775 (2178) |
| session: late 21-24 | 5580 | 0.350 | 0.515 (5516) | 0.652 (287) | 0.752 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.390 | 0.355 | 0.354 | 0.354 | 0.533 | 0.278 | 0.502 | 1.021 |
| 6h | 360 | 0.367 | 0.355 | 0.274 | 0.294 | 0.564 | 0.262 | 0.472 | 1.254 |
| 24h | 1440 | 0.377 | 0.360 | 0.269 | 0.299 | 0.558 | 0.278 | 0.477 | 1.182 |
| 7d | 10080 | 0.368 | 0.358 | 0.280 | 0.311 | 0.529 | 0.264 | 0.473 | 1.213 |
| 30d | 43200 | 0.359 | 0.354 | 0.279 | 0.308 | 0.516 | 0.252 | 0.465 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.390 / 0.533 / 0.867; 2: 0.372 / 0.433 / 0.717; 3: 0.372 / 0.450 / 0.750; 4: 0.343 / 0.417 / 0.750; 5: 0.377 / 0.583 / 0.650; 6: 0.369 / 0.533 / 0.617; 7: 0.362 / 0.483 / 0.600; 8: 0.347 / 0.433 / 0.583; 9: 0.364 / 0.500 / 0.550; 10: 0.371 / 0.583 / 0.650; 11: 0.332 / 0.467 / 0.650; 12: 0.353 / 0.550 / 0.667; 13: 0.340 / 0.500 / 0.717; 14: 0.351 / 0.550 / 0.700; 15: 0.355 / 0.533 / 0.700
- 6h: 1: 0.367 / 0.564 / 0.875; 2: 0.353 / 0.466 / 0.814; 3: 0.348 / 0.469 / 0.850; 4: 0.339 / 0.461 / 0.867; 5: 0.362 / 0.528 / 0.825; 6: 0.352 / 0.514 / 0.794; 7: 0.353 / 0.480 / 0.803; 8: 0.346 / 0.469 / 0.786; 9: 0.357 / 0.536 / 0.756; 10: 0.359 / 0.531 / 0.800; 11: 0.359 / 0.534 / 0.797; 12: 0.355 / 0.536 / 0.792; 13: 0.343 / 0.469 / 0.792; 14: 0.356 / 0.536 / 0.769; 15: 0.350 / 0.506 / 0.794
- 24h: 1: 0.377 / 0.558 / 0.906; 2: 0.356 / 0.476 / 0.887; 3: 0.363 / 0.513 / 0.894; 4: 0.351 / 0.484 / 0.899; 5: 0.356 / 0.495 / 0.888; 6: 0.356 / 0.513 / 0.883; 7: 0.352 / 0.484 / 0.882; 8: 0.355 / 0.497 / 0.875; 9: 0.356 / 0.519 / 0.873; 10: 0.360 / 0.523 / 0.883; 11: 0.354 / 0.515 / 0.877; 12: 0.359 / 0.531 / 0.880; 13: 0.354 / 0.512 / 0.881; 14: 0.357 / 0.526 / 0.875; 15: 0.356 / 0.517 / 0.882
- 7d: 1: 0.368 / 0.529 / 0.901; 2: 0.354 / 0.491 / 0.897; 3: 0.360 / 0.506 / 0.898; 4: 0.354 / 0.497 / 0.899; 5: 0.356 / 0.502 / 0.897; 6: 0.357 / 0.508 / 0.897; 7: 0.355 / 0.501 / 0.897; 8: 0.353 / 0.497 / 0.896; 9: 0.354 / 0.504 / 0.896; 10: 0.355 / 0.507 / 0.898; 11: 0.350 / 0.495 / 0.898; 12: 0.354 / 0.506 / 0.896; 13: 0.353 / 0.504 / 0.896; 14: 0.351 / 0.503 / 0.896; 15: 0.354 / 0.507 / 0.898
- 30d: 1: 0.359 / 0.516 / 0.899; 2: 0.350 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.502 / 0.899; 7: 0.348 / 0.502 / 0.899; 8: 0.348 / 0.502 / 0.899; 9: 0.346 / 0.496 / 0.899; 10: 0.348 / 0.506 / 0.899; 11: 0.346 / 0.500 / 0.899; 12: 0.347 / 0.504 / 0.899; 13: 0.347 / 0.503 / 0.899; 14: 0.345 / 0.498 / 0.899; 15: 0.346 / 0.498 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.111 (body 0.092, range 0.130); 'price stays where it was' would score 0.099; colour right 0.483; typical miss of the close 18.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.123 (body 0.084, range 0.161); 'price stays where it was' would score 0.134; colour right 0.464; typical miss of the close 9.5 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.129 (body 0.088, range 0.170); 'price stays where it was' would score 0.137; colour right 0.492; typical miss of the close 9.3 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.131; colour right 0.497; typical miss of the close 9.3 bp; chain ended on the right side 0.516 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.521 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 3.9; 2: 0.196 / 4.5; 3: 0.164 / 6.0; 4: 0.133 / 6.5; 5: 0.121 / 7.2; 6: 0.110 / 7.7; 7: 0.102 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.4; 10: 0.086 / 9.2; 11: 0.082 / 9.8; 12: 0.076 / 10.2; 13: 0.065 / 10.5; 14: 0.065 / 10.6; 15: 0.058 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 111477, probability skill vs chance 0.2236, widened contest next: False
  - now: threshold 0.835, hit rate recent 0.9411 / long run 0.9342
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.246, naive rule 0.450, lift 3.65x
    - 24h: 40 calls (40 a day), hit rate 0.950, chance 0.284, naive rule 0.478, lift 3.34x
    - 7d: 361 calls (52 a day), hit rate 0.939, chance 0.288, naive rule 0.481, lift 3.26x
    - 30d: 1703 calls (57 a day), hit rate 0.938, chance 0.292, naive rule 0.484, lift 3.22x
  - next: threshold 0.5337, hit rate recent 0.5419 / long run 0.5683
    - 6h: 31 calls (126 a day), hit rate 0.548, chance 0.246, lift 2.22x
    - 24h: 118 calls (118 a day), hit rate 0.568, chance 0.284, lift 2.00x
    - 7d: 781 calls (112 a day), hit rate 0.562, chance 0.288, lift 1.95x
    - 30d: 2624 calls (87 a day), hit rate 0.576, chance 0.292, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.514; 0.40: 482, 0.566; 0.45: 412, 0.636; 0.50: 360, 0.688; 0.55: 315, 0.730; 0.60: 269, 0.773; 0.65: 224, 0.802; 0.70: 179, 0.835; 0.75: 138, 0.871; 0.80: 94, 0.913; 0.85: 48, 0.952; 0.90: 4, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.424; 0.35: 498, 0.460; 0.40: 407, 0.490; 0.45: 312, 0.523; 0.50: 203, 0.555; 0.55: 92, 0.574; 0.60: 14, 0.608; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 111475, probability skill vs chance 0.2154, widened contest next: False
  - now: threshold 0.6837, hit rate recent 0.8159 / long run 0.8247
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.167, naive rule 0.374, lift 4.90x
    - 24h: 48 calls (48 a day), hit rate 0.792, chance 0.182, naive rule 0.397, lift 4.35x
    - 7d: 351 calls (50 a day), hit rate 0.809, chance 0.184, naive rule 0.395, lift 4.39x
    - 30d: 1603 calls (53 a day), hit rate 0.830, chance 0.187, naive rule 0.394, lift 4.43x
  - next: threshold 0.4038, hit rate recent 0.4348 / long run 0.4527
    - 6h: 42 calls (171 a day), hit rate 0.429, chance 0.167, lift 2.56x
    - 24h: 145 calls (146 a day), hit rate 0.441, chance 0.182, lift 2.43x
    - 7d: 842 calls (120 a day), hit rate 0.450, chance 0.184, lift 2.44x
    - 30d: 2459 calls (82 a day), hit rate 0.471, chance 0.187, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.422; 0.35: 349, 0.487; 0.40: 280, 0.558; 0.45: 228, 0.614; 0.50: 180, 0.664; 0.55: 137, 0.709; 0.60: 107, 0.749; 0.65: 80, 0.789; 0.70: 58, 0.824; 0.75: 32, 0.868; 0.80: 10, 0.891
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.388; 0.35: 250, 0.420; 0.40: 159, 0.447; 0.45: 75, 0.462; 0.50: 18, 0.500; 0.55: 2, 0.560
- **K=8**: model 1791936000, labels learned 111472, probability skill vs chance 0.1943, widened contest next: True
  - now: threshold 0.5704, hit rate recent 0.6302 / long run 0.6917
    - 6h: 10 calls (41 a day), hit rate 0.300, chance 0.126, naive rule 0.331, lift 2.39x
    - 24h: 39 calls (39 a day), hit rate 0.590, chance 0.121, naive rule 0.338, lift 4.86x
    - 7d: 325 calls (46 a day), hit rate 0.671, chance 0.120, naive rule 0.325, lift 5.60x
    - 30d: 1564 calls (52 a day), hit rate 0.715, chance 0.122, naive rule 0.330, lift 5.85x
  - next: threshold 0.3417, hit rate recent 0.369 / long run 0.3795
    - 6h: 40 calls (165 a day), hit rate 0.350, chance 0.126, lift 2.78x
    - 24h: 120 calls (121 a day), hit rate 0.392, chance 0.121, lift 3.23x
    - 7d: 698 calls (100 a day), hit rate 0.374, chance 0.120, lift 3.12x
    - 30d: 2274 calls (76 a day), hit rate 0.398, chance 0.122, lift 3.25x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.421; 0.35: 194, 0.492; 0.40: 148, 0.551; 0.45: 116, 0.593; 0.50: 89, 0.633; 0.55: 65, 0.683; 0.60: 44, 0.729; 0.65: 24, 0.788; 0.70: 9, 0.838; 0.75: 1, 0.786
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.352; 0.35: 104, 0.384; 0.40: 42, 0.414; 0.45: 9, 0.440; 0.50: 1, 0.471
- **K=13**: model 1792022400, labels learned 111467, probability skill vs chance 0.1803, widened contest next: True
  - now: threshold 0.4131, hit rate recent 0.4942 / long run 0.5619
    - 6h: 13 calls (54 a day), hit rate 0.385, chance 0.070, naive rule 0.257, lift 5.53x
    - 24h: 48 calls (49 a day), hit rate 0.479, chance 0.077, naive rule 0.277, lift 6.24x
    - 7d: 377 calls (54 a day), hit rate 0.541, chance 0.076, naive rule 0.274, lift 7.08x
    - 30d: 1539 calls (51 a day), hit rate 0.582, chance 0.078, naive rule 0.273, lift 7.45x
  - next: threshold 0.2768, hit rate recent 0.2881 / long run 0.3088
    - 6h: 26 calls (109 a day), hit rate 0.269, chance 0.070, lift 3.87x
    - 24h: 85 calls (86 a day), hit rate 0.282, chance 0.077, lift 3.67x
    - 7d: 444 calls (64 a day), hit rate 0.300, chance 0.076, lift 3.92x
    - 30d: 2089 calls (70 a day), hit rate 0.309, chance 0.078, lift 3.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.509; 0.40: 61, 0.560; 0.45: 41, 0.616; 0.50: 25, 0.659; 0.55: 14, 0.712; 0.60: 5, 0.755; 0.65: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.322; 0.35: 13, 0.352; 0.40: 2, 0.406; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.163 | 3.43% | 0.900 | 0.450 | 0.251 | 0.433 | 0.674 |
| 6h | 14.956 | 0.97% | 0.878 | 0.508 | 0.251 | 0.503 | 0.581 |
| 24h | 15.893 | 2.75% | 0.907 | 0.505 | 0.250 | 0.486 | 0.555 |
| 7d | 16.132 | 4.20% | 0.900 | 0.501 | 0.251 | 0.493 | 0.643 |
| 30d | 13.734 | 4.02% | 0.900 | 0.500 | 0.251 | 0.495 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.914 | 21.664 | 21.630 | 20.887 | 21.149 | 21.964 | 21.174 | 21.455 | 21.204 | 21.163 |
| 6h | 15.103 | 15.029 | 15.077 | 14.884 | 15.116 | 15.227 | 14.929 | 14.985 | 14.930 | 14.956 |
| 24h | 16.342 | 16.049 | 16.010 | 15.907 | 16.173 | 16.115 | 15.866 | 15.872 | 15.864 | 15.893 |
| 7d | 16.840 | 16.317 | 16.233 | 16.147 | 16.393 | 16.344 | 16.133 | 16.113 | 16.102 | 16.132 |
| 30d | 14.310 | 13.858 | 13.820 | 13.759 | 13.979 | 13.920 | 13.731 | 13.708 | 13.708 | 13.734 |

## Next candle

- candle starting 2026-10-19 14:03 UTC, last close 2387.37
- P(up) 0.5031, return quantiles (bp): {'05': -19.337, '10': -14.517, '25': -7.063, '40': -2.598, '50': 0.083, '60': 2.796, '75': 6.935, '90': 12.53, '95': 16.945}
- changepoint probability 0.0122, regime age 32.1 min
- agent weights: empirical 0.017, ewma 0.067, garch 0.072, har 0.271, bocpd 0.035, hmm 0.028, online_qr 0.290, lgbm 0.220

## Learning log

- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- HMM volatility states (sd, bp per minute): [3.26, 6.11, 16.29], current probabilities: [0.0, 0.04, 0.96]
- live generator: {'versions': 60, 'latest_effective': '2026-10-19 14:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.405, 'l_abs': 0.759, 'l_hi': 0.77, 'l_lo': 0.748, 'b05': 0.738, 'b25': 0.769, 'b75': 0.711, 'b95': 0.712}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [2.254, 2.357, 2.467, 3.514, 4.526, 4.613, 5.572, 6.677, 5.437, 6.068, 6.35, 6.363, 7.921, 6.463]}
- calibration offsets (in sigma): {'05': 0.001, '10': -0.058, '25': -0.075, '40': -0.052, '50': -0.04, '60': -0.018, '75': -0.025, '90': -0.082, '95': -0.041}
