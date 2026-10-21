# ETH-USD 60s candle generator - report

- generated: 2026-10-21 01:57 UTC
- last closed candle: 2026-10-21 01:57 UTC (staleness 0.4 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.534 (672) [0.497, 0.571] | 0.521 (2876) [0.502, 0.539] | 0.514 (4698) [0.498, 0.528] | 0.518 (1726) [0.491, 0.545] | 0.714 (7) | 0.500 | flat +0.045 (noise 0.033) |
| colour_clear | 0.579 (848) | 0.556 (5623) [0.548, 0.565] | 0.526 (23426) [0.517, 0.535] | 0.515 (38261) [0.508, 0.522] | 0.547 (14023) [0.541, 0.553] | 0.549 (71) | 0.500 | flat +0.018 (noise 0.009) |
| colour_confident | 0.579 (209) | 0.594 (870) [0.572, 0.620] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.602 (2411) [0.583, 0.621] | 0.571 (14) | 0.500 | flat -0.011 (noise 0.023) |
| colour_next | 0.548 (1439) | 0.535 (10025) [0.526, 0.543] | 0.517 (42863) [0.512, 0.524] | 0.511 (70022) [0.507, 0.516] | 0.530 (25673) [0.525, 0.535] | 0.504 (117) | 0.500 | flat +0.012 (noise 0.007) |
| colour_path | 0.493 (20146) | 0.500 (140350) [0.496, 0.504] | 0.501 (600082) [0.499, 0.502] | 0.500 (980308) [0.499, 0.501] | 0.500 (359422) [0.498, 0.502] | 0.504 (1638) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.691 (55) | 0.629 (210) [0.581, 0.672] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.649 (629) [0.621, 0.678] | 0.625 (8) | 0.500 | flat -0.047 (noise 0.045) |
| reversal_k13_next | 0.355 (76) | 0.315 (445) [0.298, 0.330] | 0.308 (2119) [0.296, 0.320] | 0.307 (3377) [0.296, 0.319] | 0.320 (1272) [0.308, 0.332] | 0.429 (7) | 0.077 | flat -0.007 (noise 0.030) |
| reversal_k13_now | 0.510 (51) | 0.519 (391) [0.491, 0.550] | 0.571 (1553) [0.551, 0.591] | 0.574 (2457) [0.557, 0.590] | 0.562 (985) [0.538, 0.588] | 0.250 (4) | 0.077 | flat -0.070 (noise 0.036) |
| reversal_k3_next | 0.533 (122) | 0.562 (737) [0.550, 0.573] | 0.571 (2652) [0.559, 0.584] | 0.580 (4203) [0.570, 0.591] | 0.570 (1763) [0.557, 0.585] | 0.778 (9) | 0.292 | flat -0.005 (noise 0.026) |
| reversal_k3_now | 0.912 (57) | 0.930 (384) [0.906, 0.954] | 0.933 (1700) [0.925, 0.943] | 0.936 (2794) [0.929, 0.944] | 0.927 (1031) [0.917, 0.938] | 0.800 (5) | 0.293 | flat +0.004 (noise 0.018) |
| reversal_k5_next | 0.380 (129) | 0.439 (878) [0.415, 0.464] | 0.462 (2498) [0.447, 0.478] | 0.473 (3789) [0.460, 0.488] | 0.450 (1799) [0.434, 0.469] | 0.444 (9) | 0.187 | flat -0.029 (noise 0.028) |
| reversal_k5_now | 0.840 (50) | 0.823 (355) [0.796, 0.846] | 0.827 (1584) [0.813, 0.841] | 0.831 (2563) [0.819, 0.843] | 0.821 (952) [0.804, 0.838] | 0.500 (4) | 0.187 | flat +0.013 (noise 0.029) |
| reversal_k8_next | 0.376 (109) | 0.362 (730) [0.337, 0.384] | 0.387 (2335) [0.372, 0.401] | 0.389 (3770) [0.377, 0.402] | 0.380 (1664) [0.363, 0.398] | 0.444 (9) | 0.121 | flat -0.025 (noise 0.027) |
| reversal_k8_now | 0.619 (42) | 0.665 (325) [0.629, 0.701] | 0.704 (1553) [0.685, 0.724] | 0.703 (2542) [0.687, 0.720] | 0.686 (955) [0.661, 0.710] | 0.400 (5) | 0.122 | flat -0.005 (noise 0.035) |
| overall | 0.497 (22317) | 0.504 (155292) [0.501, 0.507] | 0.503 (661815) [0.502, 0.505] | 0.503 (1080523) [0.502, 0.504] | 0.503 (397242) [0.501, 0.506] | 0.505 (1814) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06671, 0.1004] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5342, 'levels': [{'threshold': 0.06671, 'calls_per_day': 146.9, 'win_rate': 0.5706}, {'threshold': 0.1004, 'calls_per_day': 37.4, 'win_rate': 0.635}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 24652, 'rate': 0.5309}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14920 | 0.336 | 0.522 (14676) | 0.589 (1473) | 0.764 (2442) |
| volatility: normal | 14918 | 0.365 | 0.521 (14856) | 0.625 (670) | 0.758 (2191) |
| volatility: wild | 14919 | 0.378 | 0.510 (14881) | 0.610 (282) | 0.776 (2014) |
| session: Asia 00-08 | 14997 | 0.358 | 0.524 (14900) | 0.613 (878) | 0.766 (2218) |
| session: Europe 08-13 | 9300 | 0.354 | 0.519 (9216) | 0.599 (598) | 0.771 (1463) |
| session: US 13-21 | 14880 | 0.368 | 0.512 (14778) | 0.576 (587) | 0.769 (2141) |
| session: late 21-24 | 5580 | 0.351 | 0.515 (5519) | 0.622 (362) | 0.744 (825) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.356 | 0.359 | 0.282 | 0.282 | 0.500 | 0.244 | 0.468 | 1.004 |
| 6h | 360 | 0.370 | 0.361 | 0.270 | 0.298 | 0.531 | 0.262 | 0.477 | 1.145 |
| 24h | 1440 | 0.376 | 0.365 | 0.270 | 0.310 | 0.539 | 0.274 | 0.478 | 1.073 |
| 7d | 10080 | 0.370 | 0.360 | 0.277 | 0.311 | 0.534 | 0.267 | 0.472 | 1.205 |
| 30d | 43200 | 0.360 | 0.355 | 0.279 | 0.308 | 0.518 | 0.253 | 0.466 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.356 / 0.500 / 0.850; 2: 0.318 / 0.433 / 0.833; 3: 0.351 / 0.500 / 0.800; 4: 0.358 / 0.500 / 0.767; 5: 0.363 / 0.567 / 0.733; 6: 0.341 / 0.467 / 0.783; 7: 0.350 / 0.567 / 0.833; 8: 0.363 / 0.550 / 0.800; 9: 0.330 / 0.433 / 0.817; 10: 0.350 / 0.567 / 0.767; 11: 0.356 / 0.517 / 0.733; 12: 0.362 / 0.567 / 0.733; 13: 0.359 / 0.583 / 0.767; 14: 0.350 / 0.567 / 0.767; 15: 0.351 / 0.583 / 0.817
- 6h: 1: 0.370 / 0.531 / 0.878; 2: 0.351 / 0.475 / 0.892; 3: 0.347 / 0.464 / 0.878; 4: 0.374 / 0.531 / 0.878; 5: 0.346 / 0.461 / 0.875; 6: 0.340 / 0.428 / 0.892; 7: 0.354 / 0.517 / 0.903; 8: 0.358 / 0.497 / 0.900; 9: 0.349 / 0.483 / 0.897; 10: 0.355 / 0.533 / 0.878; 11: 0.346 / 0.475 / 0.883; 12: 0.350 / 0.483 / 0.881; 13: 0.353 / 0.489 / 0.886; 14: 0.354 / 0.494 / 0.878; 15: 0.357 / 0.542 / 0.881
- 24h: 1: 0.376 / 0.539 / 0.894; 2: 0.363 / 0.513 / 0.901; 3: 0.358 / 0.498 / 0.899; 4: 0.361 / 0.501 / 0.899; 5: 0.354 / 0.483 / 0.898; 6: 0.350 / 0.464 / 0.901; 7: 0.354 / 0.493 / 0.904; 8: 0.353 / 0.493 / 0.901; 9: 0.353 / 0.486 / 0.899; 10: 0.356 / 0.509 / 0.896; 11: 0.356 / 0.508 / 0.900; 12: 0.357 / 0.500 / 0.898; 13: 0.355 / 0.493 / 0.901; 14: 0.354 / 0.489 / 0.899; 15: 0.348 / 0.487 / 0.899
- 7d: 1: 0.370 / 0.534 / 0.898; 2: 0.356 / 0.494 / 0.900; 3: 0.359 / 0.504 / 0.899; 4: 0.355 / 0.496 / 0.899; 5: 0.354 / 0.497 / 0.899; 6: 0.354 / 0.497 / 0.900; 7: 0.353 / 0.498 / 0.900; 8: 0.353 / 0.498 / 0.901; 9: 0.354 / 0.501 / 0.901; 10: 0.356 / 0.509 / 0.901; 11: 0.351 / 0.500 / 0.901; 12: 0.353 / 0.505 / 0.901; 13: 0.352 / 0.501 / 0.901; 14: 0.352 / 0.503 / 0.902; 15: 0.351 / 0.502 / 0.902
- 30d: 1: 0.360 / 0.518 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.508 / 0.900; 4: 0.350 / 0.497 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.350 / 0.500 / 0.900; 7: 0.349 / 0.501 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.347 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.347 / 0.500 / 0.900; 12: 0.348 / 0.503 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.128 (body 0.077, range 0.179); 'price stays where it was' would score 0.098; colour right 0.533; typical miss of the close 11.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.126 (body 0.083, range 0.168); 'price stays where it was' would score 0.131; colour right 0.533; typical miss of the close 8.6 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.120 (body 0.080, range 0.160); 'price stays where it was' would score 0.120; colour right 0.508; typical miss of the close 10.6 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.166); 'price stays where it was' would score 0.132; colour right 0.502; typical miss of the close 9.3 bp; chain ended on the right side 0.533 of 672 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.522 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 3.9; 2: 0.197 / 4.5; 3: 0.164 / 6.1; 4: 0.132 / 6.6; 5: 0.119 / 7.3; 6: 0.109 / 7.8; 7: 0.104 / 8.2; 8: 0.096 / 8.5; 9: 0.086 / 8.5; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.077 / 10.1; 13: 0.066 / 10.4; 14: 0.067 / 10.6; 15: 0.059 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 113631, probability skill vs chance 0.2227, widened contest next: False
  - now: threshold 0.8354, hit rate recent 0.9013 / long run 0.928
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.315, naive rule 0.541, lift 2.72x
    - 24h: 55 calls (55 a day), hit rate 0.909, chance 0.295, naive rule 0.484, lift 3.08x
    - 7d: 387 calls (55 a day), hit rate 0.928, chance 0.289, naive rule 0.480, lift 3.21x
    - 30d: 1697 calls (57 a day), hit rate 0.933, chance 0.292, naive rule 0.484, lift 3.20x
  - next: threshold 0.5204, hit rate recent 0.5772 / long run 0.5656
    - 6h: 28 calls (114 a day), hit rate 0.607, chance 0.315, lift 1.92x
    - 24h: 124 calls (124 a day), hit rate 0.540, chance 0.295, lift 1.83x
    - 7d: 736 calls (105 a day), hit rate 0.562, chance 0.289, lift 1.94x
    - 30d: 2655 calls (89 a day), hit rate 0.572, chance 0.292, lift 1.96x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.491; 0.35: 541, 0.514; 0.40: 482, 0.567; 0.45: 413, 0.637; 0.50: 361, 0.689; 0.55: 316, 0.730; 0.60: 269, 0.774; 0.65: 224, 0.802; 0.70: 178, 0.835; 0.75: 138, 0.871; 0.80: 94, 0.910; 0.85: 48, 0.949; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.425; 0.35: 498, 0.461; 0.40: 406, 0.492; 0.45: 311, 0.524; 0.50: 201, 0.554; 0.55: 90, 0.568; 0.60: 14, 0.607; 0.65: 1, 0.690
- **K=5**: model 1792540800, labels learned 113629, probability skill vs chance 0.2059, widened contest next: True
  - now: threshold 0.6832, hit rate recent 0.8074 / long run 0.8226
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.170, naive rule 0.361, lift 4.12x
    - 24h: 48 calls (48 a day), hit rate 0.812, chance 0.186, naive rule 0.396, lift 4.36x
    - 7d: 358 calls (51 a day), hit rate 0.821, chance 0.186, naive rule 0.398, lift 4.40x
    - 30d: 1578 calls (53 a day), hit rate 0.827, chance 0.187, naive rule 0.393, lift 4.42x
  - next: threshold 0.419, hit rate recent 0.3761 / long run 0.4382
    - 6h: 28 calls (114 a day), hit rate 0.321, chance 0.170, lift 1.89x
    - 24h: 132 calls (133 a day), hit rate 0.371, chance 0.186, lift 1.99x
    - 7d: 882 calls (126 a day), hit rate 0.440, chance 0.186, lift 2.36x
    - 30d: 2499 calls (83 a day), hit rate 0.462, chance 0.187, lift 2.47x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.422; 0.35: 348, 0.487; 0.40: 279, 0.558; 0.45: 227, 0.614; 0.50: 179, 0.663; 0.55: 136, 0.708; 0.60: 106, 0.751; 0.65: 79, 0.789; 0.70: 57, 0.822; 0.75: 32, 0.864; 0.80: 9, 0.894
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 249, 0.417; 0.40: 157, 0.441; 0.45: 73, 0.457; 0.50: 17, 0.496; 0.55: 2, 0.511
- **K=8**: model 1792540800, labels learned 113626, probability skill vs chance 0.1924, widened contest next: True
  - now: threshold 0.5683, hit rate recent 0.6004 / long run 0.6809
    - 6h: 13 calls (53 a day), hit rate 0.462, chance 0.094, naive rule 0.234, lift 4.90x
    - 24h: 41 calls (41 a day), hit rate 0.585, chance 0.114, naive rule 0.309, lift 5.12x
    - 7d: 325 calls (46 a day), hit rate 0.665, chance 0.118, naive rule 0.319, lift 5.65x
    - 30d: 1548 calls (52 a day), hit rate 0.705, chance 0.121, naive rule 0.327, lift 5.81x
  - next: threshold 0.3452, hit rate recent 0.3712 / long run 0.3731
    - 6h: 26 calls (107 a day), hit rate 0.308, chance 0.094, lift 3.26x
    - 24h: 111 calls (112 a day), hit rate 0.387, chance 0.114, lift 3.39x
    - 7d: 732 calls (105 a day), hit rate 0.363, chance 0.118, lift 3.09x
    - 30d: 2337 calls (78 a day), hit rate 0.387, chance 0.121, lift 3.19x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 255, 0.419; 0.35: 194, 0.490; 0.40: 148, 0.546; 0.45: 115, 0.590; 0.50: 88, 0.633; 0.55: 64, 0.678; 0.60: 43, 0.722; 0.65: 24, 0.783; 0.70: 9, 0.833; 0.75: 1, 0.808
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 176, 0.349; 0.35: 102, 0.378; 0.40: 40, 0.405; 0.45: 8, 0.430; 0.50: 1, 0.500
- **K=13**: model 1792454400, labels learned 113621, probability skill vs chance 0.18, widened contest next: True
  - now: threshold 0.4326, hit rate recent 0.4776 / long run 0.5506
    - 6h: 11 calls (46 a day), hit rate 0.364, chance 0.070, naive rule 0.219, lift 5.23x
    - 24h: 48 calls (49 a day), hit rate 0.479, chance 0.073, naive rule 0.251, lift 6.60x
    - 7d: 390 calls (56 a day), hit rate 0.518, chance 0.076, naive rule 0.269, lift 6.80x
    - 30d: 1548 calls (52 a day), hit rate 0.570, chance 0.078, naive rule 0.270, lift 7.36x
  - next: threshold 0.281, hit rate recent 0.3386 / long run 0.3165
    - 6h: 21 calls (88 a day), hit rate 0.286, chance 0.070, lift 4.11x
    - 24h: 75 calls (76 a day), hit rate 0.373, chance 0.073, lift 5.14x
    - 7d: 443 calls (63 a day), hit rate 0.318, chance 0.076, lift 4.18x
    - 30d: 2120 calls (71 a day), hit rate 0.308, chance 0.078, lift 3.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.450; 0.35: 85, 0.504; 0.40: 61, 0.552; 0.45: 41, 0.608; 0.50: 25, 0.655; 0.55: 14, 0.709; 0.60: 5, 0.757; 0.65: 1, 0.849
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.318; 0.35: 13, 0.352; 0.40: 2, 0.441

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 17.724 | -0.50% | 0.850 | 0.483 | 0.250 | 0.550 | 0.103 |
| 6h | 11.943 | 3.61% | 0.894 | 0.486 | 0.251 | 0.489 | 0.387 |
| 24h | 16.846 | 3.19% | 0.894 | 0.501 | 0.251 | 0.496 | 0.673 |
| 7d | 16.262 | 4.26% | 0.900 | 0.501 | 0.251 | 0.494 | 0.650 |
| 30d | 13.792 | 3.99% | 0.900 | 0.500 | 0.251 | 0.495 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 17.636 | 17.815 | 17.763 | 17.813 | 18.114 | 17.949 | 17.697 | 17.827 | 17.748 | 17.724 |
| 6h | 12.390 | 12.000 | 11.971 | 12.020 | 12.118 | 12.088 | 11.897 | 11.941 | 11.927 | 11.943 |
| 24h | 17.402 | 16.895 | 16.841 | 16.861 | 17.025 | 16.991 | 16.843 | 16.808 | 16.806 | 16.846 |
| 7d | 16.984 | 16.440 | 16.347 | 16.272 | 16.508 | 16.468 | 16.259 | 16.242 | 16.229 | 16.262 |
| 30d | 14.366 | 13.915 | 13.876 | 13.816 | 14.037 | 13.979 | 13.787 | 13.768 | 13.766 | 13.792 |

## Next candle

- candle starting 2026-10-21 01:57 UTC, last close 2454.43
- P(up) 0.5116, return quantiles (bp): {'05': -8.816, '10': -6.605, '25': -3.483, '40': -1.19, '50': 0.153, '60': 1.366, '75': 3.774, '90': 7.45, '95': 9.567}
- changepoint probability 0.0762, regime age 57.3 min
- agent weights: empirical 0.006, ewma 0.114, garch 0.177, har 0.157, bocpd 0.046, hmm 0.064, online_qr 0.210, lgbm 0.226

## Learning log

- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- 2026-10-20 12:00 UTC: {"garch": {"alpha": 0.0559, "beta": 0.9377}, "hmm": {"sd_bp": [3.17, 5.79, 15.89], "stay": [0.985, 0.974, 0.902]}}
- 2026-10-21 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.927}, "hmm": {"sd_bp": [3.18, 5.74, 16.45], "stay": [0.984, 0.975, 0.917]}, "lgbm": {"challenger_loss": 0.25213, "champion_loss": 0.25212, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47803, "challengers": 1, "chance_loss": 0.59725, "widened": false, "champion_loss": 0.47568, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36709, "challengers": 3, "chance_loss": 0.47519, "widened": true, "champion_loss": 0.36734, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26629, "challengers": 3, "chance_loss": 0.35795, "widened": true, "champion_loss": 0.26654, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1917, "challengers": 3, "chance_loss": 0.26643, "widened": true, "champion_loss": 0.19114, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.18, 5.74, 16.45], current probabilities: [0.077, 0.914, 0.009]
- live generator: {'versions': 60, 'latest_effective': '2026-10-21 02:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.139, 'l_abs': 0.683, 'l_hi': 0.771, 'l_lo': 0.788, 'b05': 0.707, 'b25': 0.649, 'b75': 0.651, 'b95': 0.707}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8]], 'cone_width': [1.529, 2.033, 2.399, 2.797, 2.892, 2.832, 3.221, 3.423, 3.996, 4.035, 4.395, 4.231, 4.766, 4.655]}
- calibration offsets (in sigma): {'05': 0.038, '10': 0.036, '25': 0.02, '40': 0.054, '50': 0.05, '60': 0.026, '75': 0.03, '90': 0.074, '95': 0.042}
