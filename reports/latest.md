# ETH-USD 60s candle generator - report

- generated: 2026-11-05 21:12 UTC
- last closed candle: 2026-11-05 21:12 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.470 in the last 7 days, -0.067 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.470 (672) [0.448, 0.490] | 0.511 (2879) [0.494, 0.530] | 0.512 (6138) [0.500, 0.525] | 0.513 (3166) [0.494, 0.532] | 0.536 (84) | 0.500 | down -0.067 (noise 0.027) |
| colour_clear | 0.483 (783) | 0.526 (5464) [0.511, 0.541] | 0.541 (23808) [0.535, 0.546] | 0.520 (50207) [0.514, 0.526] | 0.542 (25969) [0.537, 0.547] | 0.532 (748) | 0.500 | flat -0.016 (noise 0.009) |
| colour_confident | 0.556 (108) | 0.575 (901) [0.562, 0.591] | 0.592 (4356) [0.581, 0.603] | 0.597 (4803) [0.585, 0.608] | 0.597 (4803) [0.585, 0.608] | 0.557 (88) | 0.500 | flat -0.026 (noise 0.021) |
| colour_next | 0.500 (1435) | 0.526 (9978) [0.516, 0.536] | 0.528 (42861) [0.524, 0.531] | 0.515 (91461) [0.511, 0.519] | 0.529 (47112) [0.525, 0.532] | 0.515 (1266) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.504 (20090) | 0.502 (139692) [0.500, 0.504] | 0.501 (600054) [0.500, 0.502] | 0.501 (1280454) [0.500, 0.502] | 0.501 (659568) [0.500, 0.502] | 0.509 (17724) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.556 (27) | 0.631 (198) [0.592, 0.675] | 0.627 (1141) [0.608, 0.648] | 0.631 (1271) [0.612, 0.650] | 0.631 (1271) [0.612, 0.650] | 0.583 (12) | 0.500 | flat +0.024 (noise 0.042) |
| reversal_k13_next | 0.318 (44) | 0.355 (349) [0.312, 0.394] | 0.326 (1830) [0.312, 0.340] | 0.313 (4196) [0.302, 0.324] | 0.326 (2091) [0.314, 0.339] | 0.339 (56) | 0.077 | flat +0.038 (noise 0.034) |
| reversal_k13_now | 0.547 (53) | 0.574 (413) [0.538, 0.610] | 0.561 (1658) [0.541, 0.580] | 0.573 (3308) [0.559, 0.587] | 0.567 (1836) [0.548, 0.587] | 0.562 (48) | 0.077 | flat +0.006 (noise 0.036) |
| reversal_k3_next | 0.641 (39) | 0.600 (743) [0.581, 0.618] | 0.586 (2983) [0.574, 0.597] | 0.586 (5740) [0.577, 0.595] | 0.585 (3300) [0.573, 0.596] | 0.690 (58) | 0.293 | flat +0.008 (noise 0.026) |
| reversal_k3_now | 0.922 (51) | 0.927 (413) [0.908, 0.951] | 0.932 (1738) [0.922, 0.943] | 0.937 (3670) [0.930, 0.943] | 0.932 (1907) [0.923, 0.942] | 0.906 (53) | 0.293 | flat -0.015 (noise 0.020) |
| reversal_k5_next | 0.510 (51) | 0.537 (376) [0.514, 0.557] | 0.478 (2721) [0.464, 0.494] | 0.482 (5059) [0.471, 0.494] | 0.475 (3069) [0.461, 0.490] | 0.593 (54) | 0.187 | flat +0.036 (noise 0.031) |
| reversal_k5_now | 0.812 (48) | 0.810 (410) [0.796, 0.823] | 0.815 (1631) [0.805, 0.825] | 0.828 (3416) [0.819, 0.837] | 0.819 (1805) [0.810, 0.829] | 0.841 (44) | 0.187 | flat -0.018 (noise 0.027) |
| reversal_k8_next | 0.429 (49) | 0.436 (488) [0.411, 0.465] | 0.391 (2762) [0.378, 0.405] | 0.394 (5106) [0.383, 0.404] | 0.392 (3000) [0.379, 0.405] | 0.518 (56) | 0.121 | flat +0.049 (noise 0.029) |
| reversal_k8_now | 0.652 (46) | 0.697 (369) [0.663, 0.729] | 0.679 (1570) [0.660, 0.698] | 0.701 (3328) [0.687, 0.715] | 0.689 (1741) [0.669, 0.707] | 0.725 (40) | 0.121 | flat +0.014 (noise 0.037) |
| overall | 0.505 (22002) | 0.506 (153903) [0.504, 0.508] | 0.504 (662687) [0.503, 0.506] | 0.504 (1411876) [0.503, 0.505] | 0.505 (728595) [0.503, 0.506] | 0.512 (19483) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07661, 0.1154] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5255, 'levels': [{'threshold': 0.07661, 'calls_per_day': 142.0, 'win_rate': 0.5707}, {'threshold': 0.1154, 'calls_per_day': 35.4, 'win_rate': 0.628}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42866, 'rate': 0.5278}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15304 | 0.344 | 0.528 (15063) | 0.575 (2251) | 0.737 (2619) |
| volatility: normal | 15304 | 0.366 | 0.533 (15234) | 0.610 (1452) | 0.753 (2277) |
| volatility: wild | 15304 | 0.382 | 0.523 (15260) | 0.616 (844) | 0.765 (2108) |
| session: Asia 00-08 | 15360 | 0.364 | 0.536 (15256) | 0.599 (1587) | 0.752 (2283) |
| session: Europe 08-13 | 9600 | 0.358 | 0.534 (9501) | 0.596 (1180) | 0.742 (1578) |
| session: US 13-21 | 15360 | 0.371 | 0.522 (15259) | 0.591 (1174) | 0.756 (2316) |
| session: late 21-24 | 5592 | 0.351 | 0.513 (5541) | 0.584 (606) | 0.744 (827) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.424 | 0.401 | 0.349 | 0.349 | 0.593 | 0.327 | 0.521 | 1.075 |
| 6h | 360 | 0.399 | 0.402 | 0.304 | 0.342 | 0.503 | 0.260 | 0.537 | 1.188 |
| 24h | 1440 | 0.377 | 0.373 | 0.293 | 0.327 | 0.514 | 0.256 | 0.499 | 1.109 |
| 7d | 10080 | 0.361 | 0.357 | 0.275 | 0.306 | 0.526 | 0.258 | 0.464 | 1.257 |
| 30d | 43200 | 0.364 | 0.356 | 0.277 | 0.308 | 0.528 | 0.262 | 0.466 | 1.247 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.424 / 0.593 / 0.883; 2: 0.398 / 0.492 / 0.733; 3: 0.390 / 0.458 / 0.817; 4: 0.397 / 0.508 / 0.867; 5: 0.415 / 0.508 / 0.917; 6: 0.415 / 0.576 / 0.900; 7: 0.412 / 0.542 / 0.983; 8: 0.403 / 0.576 / 0.917; 9: 0.435 / 0.576 / 1.000; 10: 0.410 / 0.525 / 1.000; 11: 0.405 / 0.542 / 0.983; 12: 0.392 / 0.492 / 1.000; 13: 0.399 / 0.492 / 1.000; 14: 0.398 / 0.525 / 1.000; 15: 0.397 / 0.542 / 1.000
- 6h: 1: 0.399 / 0.503 / 0.908; 2: 0.391 / 0.472 / 0.839; 3: 0.396 / 0.486 / 0.864; 4: 0.400 / 0.497 / 0.858; 5: 0.392 / 0.472 / 0.892; 6: 0.399 / 0.514 / 0.847; 7: 0.396 / 0.503 / 0.964; 8: 0.397 / 0.534 / 0.842; 9: 0.401 / 0.528 / 0.975; 10: 0.394 / 0.489 / 0.989; 11: 0.394 / 0.525 / 0.992; 12: 0.386 / 0.511 / 1.000; 13: 0.387 / 0.494 / 1.000; 14: 0.401 / 0.550 / 0.997; 15: 0.395 / 0.517 / 1.000
- 24h: 1: 0.377 / 0.514 / 0.890; 2: 0.370 / 0.496 / 0.889; 3: 0.375 / 0.516 / 0.894; 4: 0.375 / 0.514 / 0.895; 5: 0.373 / 0.503 / 0.900; 6: 0.375 / 0.521 / 0.890; 7: 0.374 / 0.516 / 0.907; 8: 0.374 / 0.528 / 0.886; 9: 0.376 / 0.523 / 0.915; 10: 0.370 / 0.502 / 0.910; 11: 0.364 / 0.486 / 0.906; 12: 0.369 / 0.516 / 0.898; 13: 0.366 / 0.494 / 0.896; 14: 0.369 / 0.516 / 0.897; 15: 0.364 / 0.505 / 0.901
- 7d: 1: 0.361 / 0.526 / 0.896; 2: 0.352 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.351 / 0.502 / 0.899; 5: 0.351 / 0.508 / 0.900; 6: 0.350 / 0.509 / 0.899; 7: 0.350 / 0.500 / 0.902; 8: 0.348 / 0.509 / 0.900; 9: 0.351 / 0.510 / 0.903; 10: 0.346 / 0.493 / 0.902; 11: 0.347 / 0.499 / 0.902; 12: 0.348 / 0.505 / 0.902; 13: 0.349 / 0.504 / 0.902; 14: 0.347 / 0.500 / 0.902; 15: 0.349 / 0.508 / 0.902
- 30d: 1: 0.364 / 0.528 / 0.898; 2: 0.352 / 0.496 / 0.900; 3: 0.355 / 0.509 / 0.900; 4: 0.351 / 0.499 / 0.900; 5: 0.352 / 0.505 / 0.900; 6: 0.350 / 0.501 / 0.899; 7: 0.350 / 0.499 / 0.900; 8: 0.349 / 0.504 / 0.899; 9: 0.349 / 0.501 / 0.900; 10: 0.350 / 0.503 / 0.900; 11: 0.347 / 0.497 / 0.900; 12: 0.349 / 0.502 / 0.900; 13: 0.348 / 0.500 / 0.899; 14: 0.348 / 0.501 / 0.899; 15: 0.348 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.112 (body 0.073, range 0.151); 'price stays where it was' would score 0.100; colour right 0.508; typical miss of the close 19.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.127 (body 0.082, range 0.173); 'price stays where it was' would score 0.135; colour right 0.517; typical miss of the close 23.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.125 (body 0.082, range 0.167); 'price stays where it was' would score 0.126; colour right 0.515; typical miss of the close 12.3 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.160); 'price stays where it was' would score 0.123; colour right 0.504; typical miss of the close 9.0 bp; chain ended on the right side 0.476 of 672 chains; n=10080
- 30d: match 0.124 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.5 bp; chain ended on the right side 0.511 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.4; 2: 0.199 / 5.1; 3: 0.168 / 6.7; 4: 0.131 / 7.0; 5: 0.125 / 7.8; 6: 0.115 / 8.6; 7: 0.111 / 8.8; 8: 0.099 / 9.7; 9: 0.091 / 9.7; 10: 0.090 / 10.2; 11: 0.086 / 10.3; 12: 0.078 / 10.7; 13: 0.071 / 11.1; 14: 0.072 / 11.6; 15: 0.064 / 11.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 136386, probability skill vs chance 0.2278, widened contest next: False
  - now: threshold 0.8369, hit rate recent 0.912 / long run 0.9286
    - 6h: 18 calls (73 a day), hit rate 0.944, chance 0.300, naive rule 0.495, lift 3.15x
    - 24h: 59 calls (59 a day), hit rate 0.915, chance 0.282, naive rule 0.474, lift 3.25x
    - 7d: 410 calls (59 a day), hit rate 0.915, chance 0.292, naive rule 0.496, lift 3.13x
    - 30d: 1736 calls (58 a day), hit rate 0.933, chance 0.293, naive rule 0.493, lift 3.18x
  - next: threshold 0.5651, hit rate recent 0.6518 / long run 0.6063
    - 6h: 17 calls (69 a day), hit rate 0.647, chance 0.300, lift 2.16x
    - 24h: 60 calls (60 a day), hit rate 0.700, chance 0.282, lift 2.49x
    - 7d: 688 calls (98 a day), hit rate 0.609, chance 0.292, lift 2.08x
    - 30d: 3002 calls (100 a day), hit rate 0.586, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 564, 0.497; 0.35: 533, 0.523; 0.40: 473, 0.579; 0.45: 404, 0.650; 0.50: 354, 0.700; 0.55: 308, 0.743; 0.60: 260, 0.787; 0.65: 218, 0.812; 0.70: 173, 0.842; 0.75: 138, 0.875; 0.80: 92, 0.908; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 499, 0.462; 0.40: 403, 0.498; 0.45: 306, 0.533; 0.50: 197, 0.569; 0.55: 89, 0.573; 0.60: 12, 0.632; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 136384, probability skill vs chance 0.2158, widened contest next: False
  - now: threshold 0.6866, hit rate recent 0.8221 / long run 0.8189
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.190, naive rule 0.408, lift 4.89x
    - 24h: 50 calls (50 a day), hit rate 0.800, chance 0.178, naive rule 0.373, lift 4.49x
    - 7d: 392 calls (56 a day), hit rate 0.811, chance 0.186, naive rule 0.410, lift 4.36x
    - 30d: 1626 calls (54 a day), hit rate 0.817, chance 0.187, naive rule 0.405, lift 4.38x
  - next: threshold 0.4541, hit rate recent 0.5586 / long run 0.5161
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.190, lift 3.07x
    - 24h: 59 calls (59 a day), hit rate 0.593, chance 0.178, lift 3.33x
    - 7d: 393 calls (56 a day), hit rate 0.542, chance 0.186, lift 2.91x
    - 30d: 2734 calls (91 a day), hit rate 0.481, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.424; 0.35: 347, 0.490; 0.40: 280, 0.562; 0.45: 230, 0.615; 0.50: 183, 0.663; 0.55: 146, 0.699; 0.60: 111, 0.748; 0.65: 76, 0.787; 0.70: 48, 0.821; 0.75: 29, 0.861; 0.80: 10, 0.877
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.385; 0.35: 256, 0.420; 0.40: 160, 0.460; 0.45: 68, 0.484; 0.50: 12, 0.493; 0.55: 1, 0.421
- **K=8**: model 1793059200, labels learned 136381, probability skill vs chance 0.2167, widened contest next: False
  - now: threshold 0.5714, hit rate recent 0.6922 / long run 0.6924
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.129, naive rule 0.366, lift 6.36x
    - 24h: 47 calls (47 a day), hit rate 0.660, chance 0.119, naive rule 0.335, lift 5.53x
    - 7d: 358 calls (51 a day), hit rate 0.696, chance 0.122, naive rule 0.347, lift 5.68x
    - 30d: 1552 calls (52 a day), hit rate 0.682, chance 0.121, naive rule 0.335, lift 5.65x
  - next: threshold 0.3582, hit rate recent 0.4859 / long run 0.4266
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.129, lift 5.00x
    - 24h: 62 calls (62 a day), hit rate 0.516, chance 0.119, lift 4.33x
    - 7d: 458 calls (65 a day), hit rate 0.456, chance 0.122, lift 3.73x
    - 30d: 2739 calls (91 a day), hit rate 0.393, chance 0.121, lift 3.26x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 191, 0.495; 0.40: 150, 0.543; 0.45: 116, 0.591; 0.50: 84, 0.639; 0.55: 60, 0.672; 0.60: 41, 0.707; 0.65: 24, 0.782; 0.70: 12, 0.814; 0.75: 2, 0.776
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.362; 0.35: 90, 0.389; 0.40: 25, 0.413; 0.45: 5, 0.441; 0.50: 1, 0.667
- **K=13**: model 1793577600, labels learned 136376, probability skill vs chance 0.1812, widened contest next: False
  - now: threshold 0.4504, hit rate recent 0.5611 / long run 0.5683
    - 6h: 12 calls (50 a day), hit rate 0.750, chance 0.083, naive rule 0.326, lift 9.08x
    - 24h: 55 calls (56 a day), hit rate 0.509, chance 0.075, naive rule 0.261, lift 6.75x
    - 7d: 399 calls (57 a day), hit rate 0.584, chance 0.079, naive rule 0.290, lift 7.36x
    - 30d: 1649 calls (55 a day), hit rate 0.564, chance 0.078, naive rule 0.281, lift 7.27x
  - next: threshold 0.2859, hit rate recent 0.3423 / long run 0.3374
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.083, lift 6.05x
    - 24h: 61 calls (62 a day), hit rate 0.328, chance 0.075, lift 4.35x
    - 7d: 361 calls (52 a day), hit rate 0.366, chance 0.079, lift 4.61x
    - 30d: 1824 calls (61 a day), hit rate 0.327, chance 0.078, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 130, 0.439; 0.35: 93, 0.489; 0.40: 66, 0.545; 0.45: 45, 0.589; 0.50: 30, 0.649; 0.55: 20, 0.679; 0.60: 10, 0.713; 0.65: 3, 0.684; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.330; 0.35: 13, 0.339; 0.40: 3, 0.410; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 25.465 | 4.05% | 0.883 | 0.400 | 0.249 | 0.525 | 0.127 |
| 6h | 32.530 | 9.59% | 0.897 | 0.494 | 0.251 | 0.506 | 0.721 |
| 24h | 19.631 | 7.54% | 0.891 | 0.497 | 0.251 | 0.494 | 0.809 |
| 7d | 15.966 | 5.30% | 0.900 | 0.500 | 0.250 | 0.505 | 0.757 |
| 30d | 15.064 | 4.42% | 0.900 | 0.500 | 0.250 | 0.499 | 0.699 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.539 | 25.779 | 25.847 | 25.723 | 25.832 | 26.193 | 25.368 | 25.347 | 25.452 | 25.465 |
| 6h | 35.980 | 32.608 | 32.580 | 32.747 | 33.149 | 33.569 | 32.325 | 32.522 | 32.438 | 32.530 |
| 24h | 21.231 | 19.771 | 19.694 | 19.697 | 19.845 | 20.151 | 19.603 | 19.641 | 19.610 | 19.631 |
| 7d | 16.861 | 16.109 | 16.084 | 16.022 | 16.265 | 16.327 | 15.956 | 15.947 | 15.943 | 15.966 |
| 30d | 15.761 | 15.219 | 15.157 | 15.095 | 15.335 | 15.294 | 15.058 | 15.036 | 15.037 | 15.064 |

## Next candle

- candle starting 2026-11-05 21:12 UTC, last close 2235.77
- P(up) 0.4816, return quantiles (bp): {'05': -18.745, '10': -14.352, '25': -7.393, '40': -3.639, '50': -0.458, '60': 2.066, '75': 6.446, '90': 12.778, '95': 17.496}
- changepoint probability 0.0344, regime age 232.7 min
- agent weights: empirical 0.003, ewma 0.062, garch 0.140, har 0.154, bocpd 0.048, hmm 0.004, online_qr 0.358, lgbm 0.231

## Learning log

- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- HMM volatility states (sd, bp per minute): [2.39, 4.93, 13.06], current probabilities: [0.0, 0.159, 0.841]
- live generator: {'versions': 60, 'latest_effective': '2026-11-05 21:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.292, 'l_abs': 0.71, 'l_hi': 0.741, 'l_lo': 0.796, 'b05': 0.75, 'b25': 0.708, 'b75': 0.564, 'b95': 0.68}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [2.043, 2.269, 2.732, 2.883, 4.104, 2.694, 5.052, 2.946, 3.239, 3.614, 4.62, 5.325, 5.215, 5.63]}
- calibration offsets (in sigma): {'05': -0.0145, '10': -0.059, '25': -0.0525, '40': -0.116, '50': -0.045, '60': -0.044, '75': -0.0375, '90': -0.081, '95': -0.0155}
