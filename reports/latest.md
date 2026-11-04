# ETH-USD 60s candle generator - report

- generated: 2026-11-04 03:17 UTC
- last closed candle: 2026-11-04 03:17 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: chain_end_side 0.478 in the last 7 days, -0.059 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.396 (96) | 0.478 (672) [0.449, 0.504] | 0.509 (2878) [0.490, 0.528] | 0.512 (6042) [0.499, 0.525] | 0.513 (3070) [0.494, 0.532] | 0.385 (13) | 0.500 | down -0.059 (noise 0.028) |
| colour_clear | 0.518 (819) | 0.534 (5467) [0.525, 0.544] | 0.543 (23791) [0.539, 0.548] | 0.521 (49424) [0.515, 0.527] | 0.544 (25186) [0.539, 0.548] | 0.458 (120) | 0.500 | flat -0.010 (noise 0.009) |
| colour_confident | 0.621 (95) | 0.576 (913) [0.564, 0.593] | 0.596 (4351) [0.584, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.400 (10) | 0.500 | flat -0.028 (noise 0.021) |
| colour_next | 0.526 (1436) | 0.531 (9974) [0.524, 0.537] | 0.529 (42856) [0.526, 0.533] | 0.515 (90026) [0.511, 0.519] | 0.530 (45677) [0.526, 0.533] | 0.515 (196) | 0.500 | flat +0.003 (noise 0.007) |
| colour_path | 0.505 (20104) | 0.502 (139636) [0.500, 0.504] | 0.501 (599984) [0.500, 0.502] | 0.501 (1260364) [0.500, 0.502] | 0.501 (639478) [0.499, 0.502] | 0.498 (2744) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.571 (14) | 0.621 (203) [0.570, 0.671] | 0.631 (1129) [0.610, 0.652] | 0.633 (1244) [0.613, 0.652] | 0.633 (1244) [0.613, 0.652] | - | 0.500 | flat +0.007 (noise 0.042) |
| reversal_k13_next | 0.409 (66) | 0.352 (358) [0.311, 0.391] | 0.324 (1859) [0.310, 0.339] | 0.313 (4152) [0.303, 0.324] | 0.326 (2047) [0.313, 0.339] | 0.333 (6) | 0.077 | flat +0.031 (noise 0.034) |
| reversal_k13_now | 0.649 (57) | 0.582 (423) [0.544, 0.615] | 0.561 (1673) [0.543, 0.580] | 0.574 (3255) [0.560, 0.588] | 0.568 (1783) [0.547, 0.589] | 0.455 (11) | 0.077 | flat +0.016 (noise 0.036) |
| reversal_k3_next | 0.523 (65) | 0.597 (819) [0.580, 0.614] | 0.586 (2993) [0.575, 0.598] | 0.586 (5701) [0.577, 0.595] | 0.584 (3261) [0.574, 0.596] | 0.750 (4) | 0.293 | flat -0.010 (noise 0.025) |
| reversal_k3_now | 0.904 (52) | 0.925 (428) [0.905, 0.949] | 0.933 (1735) [0.922, 0.944] | 0.937 (3619) [0.931, 0.943] | 0.933 (1856) [0.923, 0.942] | 0.909 (11) | 0.293 | flat -0.029 (noise 0.018) |
| reversal_k5_next | 0.476 (63) | 0.535 (389) [0.511, 0.556] | 0.479 (2709) [0.464, 0.495] | 0.482 (5008) [0.471, 0.494] | 0.474 (3018) [0.460, 0.490] | 0.667 (6) | 0.187 | flat +0.036 (noise 0.031) |
| reversal_k5_now | 0.784 (51) | 0.814 (436) [0.799, 0.827] | 0.816 (1628) [0.806, 0.826] | 0.828 (3368) [0.819, 0.837] | 0.820 (1757) [0.809, 0.830] | 0.750 (12) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.409 (66) | 0.439 (540) [0.414, 0.465] | 0.389 (2787) [0.376, 0.403] | 0.393 (5057) [0.383, 0.404] | 0.391 (2951) [0.378, 0.405] | 0.429 (7) | 0.121 | up +0.057 (noise 0.028) |
| reversal_k8_now | 0.714 (49) | 0.714 (384) [0.676, 0.744] | 0.683 (1585) [0.664, 0.702] | 0.701 (3282) [0.687, 0.716] | 0.690 (1695) [0.669, 0.709] | 0.545 (11) | 0.121 | flat +0.039 (noise 0.036) |
| overall | 0.507 (22105) | 0.506 (154059) [0.504, 0.509] | 0.505 (662687) [0.503, 0.506] | 0.504 (1389874) [0.503, 0.505] | 0.505 (706593) [0.503, 0.506] | 0.502 (3021) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07848, 0.1182] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5311, 'levels': [{'threshold': 0.07848, 'calls_per_day': 140.9, 'win_rate': 0.5707}, {'threshold': 0.1182, 'calls_per_day': 34.4, 'win_rate': 0.6296}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42854, 'rate': 0.5291}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14946 | 0.338 | 0.528 (14690) | 0.577 (2312) | 0.749 (2600) |
| volatility: normal | 14945 | 0.366 | 0.534 (14877) | 0.611 (1499) | 0.745 (2242) |
| volatility: wild | 14946 | 0.381 | 0.528 (14902) | 0.628 (810) | 0.764 (2081) |
| session: Asia 00-08 | 15077 | 0.362 | 0.537 (14967) | 0.602 (1648) | 0.753 (2254) |
| session: Europe 08-13 | 9300 | 0.356 | 0.534 (9200) | 0.595 (1173) | 0.740 (1559) |
| session: US 13-21 | 14880 | 0.369 | 0.526 (14772) | 0.595 (1196) | 0.760 (2275) |
| session: late 21-24 | 5580 | 0.351 | 0.512 (5530) | 0.589 (604) | 0.749 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.338 | 0.357 | 0.296 | 0.296 | 0.492 | 0.193 | 0.482 | 1.293 |
| 6h | 360 | 0.356 | 0.361 | 0.266 | 0.288 | 0.493 | 0.243 | 0.469 | 1.268 |
| 24h | 1440 | 0.370 | 0.369 | 0.275 | 0.302 | 0.525 | 0.258 | 0.482 | 1.187 |
| 7d | 10080 | 0.359 | 0.356 | 0.272 | 0.302 | 0.529 | 0.259 | 0.459 | 1.276 |
| 30d | 43200 | 0.363 | 0.356 | 0.276 | 0.307 | 0.529 | 0.262 | 0.464 | 1.249 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.338 / 0.492 / 0.917; 2: 0.372 / 0.492 / 0.917; 3: 0.356 / 0.508 / 0.933; 4: 0.362 / 0.492 / 0.933; 5: 0.365 / 0.525 / 0.900; 6: 0.331 / 0.424 / 0.883; 7: 0.350 / 0.475 / 0.883; 8: 0.312 / 0.441 / 0.850; 9: 0.356 / 0.475 / 0.817; 10: 0.333 / 0.508 / 0.817; 11: 0.360 / 0.627 / 0.817; 12: 0.347 / 0.525 / 0.767; 13: 0.345 / 0.559 / 0.767; 14: 0.322 / 0.508 / 0.767; 15: 0.340 / 0.508 / 0.733
- 6h: 1: 0.356 / 0.493 / 0.889; 2: 0.361 / 0.518 / 0.933; 3: 0.356 / 0.518 / 0.889; 4: 0.370 / 0.521 / 0.883; 5: 0.355 / 0.476 / 0.933; 6: 0.339 / 0.454 / 0.856; 7: 0.353 / 0.507 / 0.911; 8: 0.339 / 0.476 / 0.906; 9: 0.355 / 0.510 / 0.908; 10: 0.339 / 0.454 / 0.906; 11: 0.339 / 0.476 / 0.917; 12: 0.349 / 0.501 / 0.842; 13: 0.348 / 0.499 / 0.886; 14: 0.352 / 0.510 / 0.856; 15: 0.344 / 0.493 / 0.853
- 24h: 1: 0.370 / 0.525 / 0.898; 2: 0.365 / 0.512 / 0.905; 3: 0.366 / 0.528 / 0.898; 4: 0.364 / 0.498 / 0.897; 5: 0.359 / 0.498 / 0.903; 6: 0.355 / 0.507 / 0.890; 7: 0.361 / 0.502 / 0.909; 8: 0.356 / 0.492 / 0.906; 9: 0.359 / 0.511 / 0.904; 10: 0.355 / 0.484 / 0.909; 11: 0.360 / 0.511 / 0.902; 12: 0.355 / 0.499 / 0.892; 13: 0.358 / 0.497 / 0.900; 14: 0.357 / 0.500 / 0.896; 15: 0.364 / 0.520 / 0.894
- 7d: 1: 0.359 / 0.529 / 0.898; 2: 0.349 / 0.496 / 0.900; 3: 0.350 / 0.509 / 0.900; 4: 0.348 / 0.501 / 0.900; 5: 0.348 / 0.510 / 0.899; 6: 0.345 / 0.504 / 0.899; 7: 0.347 / 0.499 / 0.899; 8: 0.344 / 0.506 / 0.899; 9: 0.346 / 0.505 / 0.899; 10: 0.344 / 0.494 / 0.900; 11: 0.344 / 0.500 / 0.900; 12: 0.344 / 0.496 / 0.899; 13: 0.345 / 0.502 / 0.899; 14: 0.343 / 0.496 / 0.898; 15: 0.345 / 0.508 / 0.898
- 30d: 1: 0.363 / 0.529 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.500 / 0.900; 7: 0.349 / 0.500 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.348 / 0.499 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.346 / 0.497 / 0.900; 12: 0.348 / 0.501 / 0.899; 13: 0.347 / 0.501 / 0.899; 14: 0.346 / 0.500 / 0.899; 15: 0.347 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.080 (body 0.031, range 0.129); 'price stays where it was' would score 0.084; colour right 0.492; typical miss of the close 15.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.102 (body 0.063, range 0.141); 'price stays where it was' would score 0.102; colour right 0.471; typical miss of the close 12.3 bp; chain ended on the right side 0.333 of 24 chains; n=360
- 24h: match 0.115 (body 0.076, range 0.154); 'price stays where it was' would score 0.116; colour right 0.502; typical miss of the close 10.1 bp; chain ended on the right side 0.385 of 96 chains; n=1440
- 7d: match 0.122 (body 0.084, range 0.161); 'price stays where it was' would score 0.124; colour right 0.502; typical miss of the close 8.5 bp; chain ended on the right side 0.472 of 672 chains; n=10080
- 30d: match 0.124 (body 0.084, range 0.163); 'price stays where it was' would score 0.129; colour right 0.500; typical miss of the close 8.2 bp; chain ended on the right side 0.508 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.368 / 4.2; 2: 0.200 / 4.8; 3: 0.169 / 6.4; 4: 0.131 / 6.8; 5: 0.124 / 7.6; 6: 0.114 / 8.2; 7: 0.111 / 8.4; 8: 0.098 / 9.2; 9: 0.089 / 9.3; 10: 0.088 / 9.7; 11: 0.085 / 10.1; 12: 0.076 / 10.5; 13: 0.069 / 10.7; 14: 0.070 / 11.3; 15: 0.062 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 133871, probability skill vs chance 0.2265, widened contest next: True
  - now: threshold 0.8387, hit rate recent 0.9106 / long run 0.9311
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.328, naive rule 0.552, lift 2.86x
    - 24h: 51 calls (51 a day), hit rate 0.922, chance 0.293, naive rule 0.490, lift 3.14x
    - 7d: 431 calls (62 a day), hit rate 0.926, chance 0.293, naive rule 0.497, lift 3.16x
    - 30d: 1741 calls (58 a day), hit rate 0.933, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.5659, hit rate recent 0.565 / long run 0.596
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.328, lift 1.66x
    - 24h: 50 calls (50 a day), hit rate 0.600, chance 0.293, lift 2.05x
    - 7d: 811 calls (116 a day), hit rate 0.596, chance 0.293, lift 2.03x
    - 30d: 2989 calls (100 a day), hit rate 0.586, chance 0.294, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.498; 0.35: 534, 0.523; 0.40: 474, 0.580; 0.45: 406, 0.651; 0.50: 355, 0.701; 0.55: 310, 0.743; 0.60: 262, 0.788; 0.65: 220, 0.813; 0.70: 174, 0.844; 0.75: 139, 0.878; 0.80: 93, 0.909; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 500, 0.464; 0.40: 404, 0.499; 0.45: 307, 0.535; 0.50: 198, 0.571; 0.55: 89, 0.572; 0.60: 12, 0.640; 0.65: 1, 0.636
- **K=5**: model 1792540800, labels learned 133869, probability skill vs chance 0.2174, widened contest next: False
  - now: threshold 0.6859, hit rate recent 0.7959 / long run 0.8164
    - 6h: 18 calls (73 a day), hit rate 0.778, chance 0.188, naive rule 0.399, lift 4.13x
    - 24h: 52 calls (52 a day), hit rate 0.769, chance 0.180, naive rule 0.386, lift 4.27x
    - 7d: 436 calls (62 a day), hit rate 0.812, chance 0.186, naive rule 0.410, lift 4.37x
    - 30d: 1636 calls (55 a day), hit rate 0.817, chance 0.188, naive rule 0.406, lift 4.35x
  - next: threshold 0.4488, hit rate recent 0.523 / long run 0.5104
    - 6h: 17 calls (69 a day), hit rate 0.588, chance 0.188, lift 3.12x
    - 24h: 56 calls (56 a day), hit rate 0.518, chance 0.180, lift 2.88x
    - 7d: 387 calls (55 a day), hit rate 0.532, chance 0.186, lift 2.87x
    - 30d: 2712 calls (90 a day), hit rate 0.480, chance 0.188, lift 2.56x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 347, 0.492; 0.40: 280, 0.566; 0.45: 230, 0.617; 0.50: 183, 0.665; 0.55: 145, 0.702; 0.60: 110, 0.749; 0.65: 77, 0.787; 0.70: 50, 0.819; 0.75: 29, 0.862; 0.80: 10, 0.881
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.387; 0.35: 255, 0.421; 0.40: 159, 0.459; 0.45: 67, 0.483; 0.50: 12, 0.497; 0.55: 1, 0.457
- **K=8**: model 1793059200, labels learned 133866, probability skill vs chance 0.1986, widened contest next: False
  - now: threshold 0.5736, hit rate recent 0.6766 / long run 0.6907
    - 6h: 16 calls (66 a day), hit rate 0.688, chance 0.110, naive rule 0.305, lift 6.25x
    - 24h: 52 calls (52 a day), hit rate 0.692, chance 0.110, naive rule 0.310, lift 6.27x
    - 7d: 386 calls (55 a day), hit rate 0.707, chance 0.123, naive rule 0.345, lift 5.74x
    - 30d: 1591 calls (53 a day), hit rate 0.683, chance 0.121, naive rule 0.335, lift 5.66x
  - next: threshold 0.364, hit rate recent 0.4219 / long run 0.4168
    - 6h: 15 calls (62 a day), hit rate 0.400, chance 0.110, lift 3.64x
    - 24h: 60 calls (60 a day), hit rate 0.417, chance 0.110, lift 3.77x
    - 7d: 536 calls (77 a day), hit rate 0.437, chance 0.123, lift 3.55x
    - 30d: 2788 calls (93 a day), hit rate 0.390, chance 0.121, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.432; 0.35: 191, 0.497; 0.40: 150, 0.542; 0.45: 115, 0.590; 0.50: 85, 0.637; 0.55: 61, 0.673; 0.60: 42, 0.703; 0.65: 24, 0.777; 0.70: 12, 0.808; 0.75: 2, 0.766
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.360; 0.35: 91, 0.386; 0.40: 26, 0.416; 0.45: 5, 0.453; 0.50: 1, 0.667
- **K=13**: model 1793577600, labels learned 133861, probability skill vs chance 0.1868, widened contest next: False
  - now: threshold 0.452, hit rate recent 0.577 / long run 0.5688
    - 6h: 17 calls (71 a day), hit rate 0.529, chance 0.083, naive rule 0.274, lift 6.41x
    - 24h: 59 calls (60 a day), hit rate 0.610, chance 0.081, naive rule 0.289, lift 7.50x
    - 7d: 424 calls (61 a day), hit rate 0.575, chance 0.080, naive rule 0.292, lift 7.23x
    - 30d: 1676 calls (56 a day), hit rate 0.560, chance 0.077, naive rule 0.280, lift 7.25x
  - next: threshold 0.2876, hit rate recent 0.3763 / long run 0.3386
    - 6h: 13 calls (54 a day), hit rate 0.308, chance 0.083, lift 3.72x
    - 24h: 58 calls (59 a day), hit rate 0.397, chance 0.081, lift 4.87x
    - 7d: 356 calls (51 a day), hit rate 0.351, chance 0.080, lift 4.41x
    - 30d: 1851 calls (62 a day), hit rate 0.325, chance 0.077, lift 4.20x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.439; 0.35: 93, 0.491; 0.40: 66, 0.544; 0.45: 45, 0.585; 0.50: 30, 0.645; 0.55: 19, 0.676; 0.60: 10, 0.715; 0.65: 3, 0.694; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.330; 0.35: 13, 0.354; 0.40: 3, 0.415; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 23.119 | 11.25% | 0.933 | 0.517 | 0.251 | 0.424 | 0.653 |
| 6h | 17.637 | 6.12% | 0.900 | 0.489 | 0.252 | 0.479 | 0.693 |
| 24h | 15.194 | 3.65% | 0.906 | 0.502 | 0.250 | 0.512 | 0.617 |
| 7d | 15.208 | 5.13% | 0.900 | 0.500 | 0.250 | 0.509 | 0.744 |
| 30d | 14.488 | 4.29% | 0.900 | 0.500 | 0.250 | 0.499 | 0.685 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 26.050 | 24.343 | 23.389 | 23.212 | 23.349 | 23.765 | 23.232 | 22.906 | 23.128 | 23.119 |
| 6h | 18.788 | 17.973 | 17.765 | 17.598 | 17.886 | 17.892 | 17.588 | 17.605 | 17.606 | 17.637 |
| 24h | 15.770 | 15.322 | 15.268 | 15.205 | 15.428 | 15.404 | 15.149 | 15.171 | 15.160 | 15.194 |
| 7d | 16.030 | 15.385 | 15.338 | 15.249 | 15.541 | 15.537 | 15.190 | 15.179 | 15.183 | 15.208 |
| 30d | 15.137 | 14.639 | 14.582 | 14.519 | 14.755 | 14.700 | 14.480 | 14.459 | 14.461 | 14.488 |

## Next candle

- candle starting 2026-11-04 03:17 UTC, last close 2235.59
- P(up) 0.478, return quantiles (bp): {'05': -18.179, '10': -14.186, '25': -8.141, '40': -3.116, '50': -0.46, '60': 1.67, '75': 5.971, '90': 12.454, '95': 16.931}
- changepoint probability 0.054, regime age 18.6 min
- agent weights: empirical 0.003, ewma 0.034, garch 0.093, har 0.209, bocpd 0.028, hmm 0.031, online_qr 0.314, lgbm 0.289

## Learning log

- 2026-11-02 00:00 UTC: {"garch": {"alpha": 0.0655, "beta": 0.9301}, "hmm": {"sd_bp": [2.63, 6.47, 19.79], "stay": [0.98, 0.963, 0.938]}, "lgbm": {"challenger_loss": 0.24981, "champion_loss": 0.24974, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49132, "challengers": 1, "chance_loss": 0.61323, "widened": false, "champion_loss": 0.48783, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3808, "challengers": 1, "chance_loss": 0.49249, "widened": false, "champion_loss": 0.37821, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27949, "challengers": 1, "chance_loss": 0.37306, "widened": false, "champion_loss": 0.27944, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20126, "challengers": 1, "chance_loss": 0.27977, "widened": false, "champion_loss": 0.20154, "promoted": true}}
- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.34, 4.65, 10.51], current probabilities: [0.0, 0.035, 0.965]
- live generator: {'versions': 60, 'latest_effective': '2026-11-04 03:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.21, 'l_abs': 0.678, 'l_hi': 0.781, 'l_lo': 0.789, 'b05': 0.742, 'b25': 0.64, 'b75': 0.657, 'b95': 0.704}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.529, 1.876, 2.305, 2.582, 3.26, 3.13, 3.56, 3.635, 3.839, 4.035, 5.158, 4.584, 5.267, 5.801]}
- calibration offsets (in sigma): {'05': -0.052, '10': -0.044, '25': -0.1, '40': -0.036, '50': -0.03, '60': -0.044, '75': -0.05, '90': -0.026, '95': -0.038}
