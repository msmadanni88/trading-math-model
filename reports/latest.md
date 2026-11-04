# ETH-USD 60s candle generator - report

- generated: 2026-11-04 23:57 UTC
- last closed candle: 2026-11-04 23:57 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.478 in the last 7 days, -0.059 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.396 (96) | 0.478 (672) [0.449, 0.504] | 0.509 (2878) [0.490, 0.528] | 0.512 (6042) [0.499, 0.525] | 0.513 (3070) [0.494, 0.532] | 0.495 (95) | 0.500 | down -0.059 (noise 0.028) |
| colour_clear | 0.518 (819) | 0.534 (5467) [0.525, 0.544] | 0.543 (23791) [0.539, 0.548] | 0.521 (49424) [0.515, 0.527] | 0.544 (25186) [0.539, 0.548] | 0.482 (782) | 0.500 | flat -0.010 (noise 0.009) |
| colour_confident | 0.621 (95) | 0.576 (913) [0.564, 0.593] | 0.596 (4351) [0.584, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.556 (108) | 0.500 | flat -0.028 (noise 0.021) |
| colour_next | 0.526 (1436) | 0.531 (9974) [0.524, 0.537] | 0.529 (42856) [0.526, 0.533] | 0.515 (90026) [0.511, 0.519] | 0.530 (45677) [0.526, 0.533] | 0.500 (1432) | 0.500 | flat +0.003 (noise 0.007) |
| colour_path | 0.505 (20104) | 0.502 (139636) [0.500, 0.504] | 0.501 (599984) [0.500, 0.502] | 0.501 (1260364) [0.500, 0.502] | 0.501 (639478) [0.499, 0.502] | 0.503 (20048) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.571 (14) | 0.621 (203) [0.570, 0.671] | 0.631 (1129) [0.610, 0.652] | 0.633 (1244) [0.613, 0.652] | 0.633 (1244) [0.613, 0.652] | 0.556 (27) | 0.500 | flat +0.007 (noise 0.042) |
| reversal_k13_next | 0.409 (66) | 0.352 (358) [0.311, 0.391] | 0.324 (1859) [0.310, 0.339] | 0.313 (4152) [0.303, 0.324] | 0.326 (2047) [0.313, 0.339] | 0.318 (44) | 0.077 | flat +0.031 (noise 0.034) |
| reversal_k13_now | 0.649 (57) | 0.582 (423) [0.544, 0.615] | 0.561 (1673) [0.543, 0.580] | 0.574 (3255) [0.560, 0.588] | 0.568 (1783) [0.547, 0.589] | 0.547 (53) | 0.077 | flat +0.016 (noise 0.036) |
| reversal_k3_next | 0.523 (65) | 0.597 (819) [0.580, 0.614] | 0.586 (2993) [0.575, 0.598] | 0.586 (5701) [0.577, 0.595] | 0.584 (3261) [0.574, 0.596] | 0.641 (39) | 0.293 | flat -0.010 (noise 0.025) |
| reversal_k3_now | 0.904 (52) | 0.925 (428) [0.905, 0.949] | 0.933 (1735) [0.922, 0.944] | 0.937 (3619) [0.931, 0.943] | 0.933 (1856) [0.923, 0.942] | 0.922 (51) | 0.293 | flat -0.029 (noise 0.018) |
| reversal_k5_next | 0.476 (63) | 0.535 (389) [0.511, 0.556] | 0.479 (2709) [0.464, 0.495] | 0.482 (5008) [0.471, 0.494] | 0.474 (3018) [0.460, 0.490] | 0.510 (51) | 0.187 | flat +0.036 (noise 0.031) |
| reversal_k5_now | 0.784 (51) | 0.814 (436) [0.799, 0.827] | 0.816 (1628) [0.806, 0.826] | 0.828 (3368) [0.819, 0.837] | 0.820 (1757) [0.809, 0.830] | 0.812 (48) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.409 (66) | 0.439 (540) [0.414, 0.465] | 0.389 (2787) [0.376, 0.403] | 0.393 (5057) [0.383, 0.404] | 0.391 (2951) [0.378, 0.405] | 0.429 (49) | 0.121 | up +0.057 (noise 0.028) |
| reversal_k8_now | 0.714 (49) | 0.714 (384) [0.676, 0.744] | 0.683 (1585) [0.664, 0.702] | 0.701 (3282) [0.687, 0.716] | 0.690 (1695) [0.669, 0.709] | 0.652 (46) | 0.121 | flat +0.039 (noise 0.036) |
| overall | 0.507 (22105) | 0.506 (154059) [0.504, 0.509] | 0.505 (662687) [0.503, 0.506] | 0.504 (1389874) [0.503, 0.505] | 0.505 (706593) [0.503, 0.506] | 0.505 (21956) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07741, 0.1163] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5281, 'levels': [{'threshold': 0.07741, 'calls_per_day': 143.4, 'win_rate': 0.5838}, {'threshold': 0.1163, 'calls_per_day': 35.6, 'win_rate': 0.6508}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42860, 'rate': 0.5276}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15359 | 0.339 | 0.529 (15100) | 0.579 (2361) | 0.749 (2641) |
| volatility: normal | 15359 | 0.366 | 0.534 (15289) | 0.612 (1506) | 0.745 (2318) |
| volatility: wild | 15359 | 0.381 | 0.524 (15316) | 0.615 (852) | 0.763 (2117) |
| session: Asia 00-08 | 15360 | 0.362 | 0.537 (15249) | 0.602 (1670) | 0.755 (2295) |
| session: Europe 08-13 | 9600 | 0.356 | 0.533 (9499) | 0.597 (1196) | 0.743 (1593) |
| session: US 13-21 | 15360 | 0.369 | 0.525 (15251) | 0.593 (1236) | 0.760 (2327) |
| session: late 21-24 | 5757 | 0.352 | 0.512 (5706) | 0.587 (617) | 0.740 (861) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.399 | 0.358 | 0.276 | 0.276 | 0.533 | 0.289 | 0.509 | 1.462 |
| 6h | 360 | 0.367 | 0.358 | 0.287 | 0.341 | 0.494 | 0.250 | 0.484 | 1.388 |
| 24h | 1440 | 0.369 | 0.368 | 0.290 | 0.326 | 0.499 | 0.250 | 0.487 | 1.253 |
| 7d | 10080 | 0.360 | 0.356 | 0.274 | 0.305 | 0.526 | 0.258 | 0.461 | 1.284 |
| 30d | 43200 | 0.363 | 0.356 | 0.277 | 0.307 | 0.528 | 0.262 | 0.465 | 1.254 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.399 / 0.533 / 0.933; 2: 0.347 / 0.517 / 0.950; 3: 0.371 / 0.517 / 0.950; 4: 0.361 / 0.500 / 0.933; 5: 0.389 / 0.617 / 0.917; 6: 0.365 / 0.567 / 0.917; 7: 0.349 / 0.483 / 0.900; 8: 0.363 / 0.533 / 0.900; 9: 0.347 / 0.433 / 0.900; 10: 0.367 / 0.483 / 0.883; 11: 0.357 / 0.500 / 0.833; 12: 0.399 / 0.550 / 0.850; 13: 0.378 / 0.533 / 0.817; 14: 0.373 / 0.500 / 0.817; 15: 0.350 / 0.517 / 0.817
- 6h: 1: 0.367 / 0.494 / 0.911; 2: 0.363 / 0.506 / 0.939; 3: 0.372 / 0.514 / 0.922; 4: 0.373 / 0.525 / 0.931; 5: 0.358 / 0.494 / 0.897; 6: 0.368 / 0.522 / 0.933; 7: 0.358 / 0.483 / 0.872; 8: 0.364 / 0.497 / 0.914; 9: 0.363 / 0.486 / 0.922; 10: 0.363 / 0.508 / 0.917; 11: 0.359 / 0.483 / 0.867; 12: 0.387 / 0.570 / 0.908; 13: 0.371 / 0.522 / 0.881; 14: 0.357 / 0.478 / 0.883; 15: 0.369 / 0.550 / 0.892
- 24h: 1: 0.369 / 0.499 / 0.908; 2: 0.366 / 0.507 / 0.907; 3: 0.366 / 0.498 / 0.908; 4: 0.364 / 0.507 / 0.906; 5: 0.359 / 0.479 / 0.897; 6: 0.359 / 0.505 / 0.901; 7: 0.359 / 0.486 / 0.892; 8: 0.356 / 0.505 / 0.897; 9: 0.363 / 0.513 / 0.892; 10: 0.357 / 0.497 / 0.894; 11: 0.356 / 0.502 / 0.887; 12: 0.365 / 0.528 / 0.891; 13: 0.362 / 0.509 / 0.882; 14: 0.361 / 0.510 / 0.882; 15: 0.356 / 0.499 / 0.881
- 7d: 1: 0.360 / 0.526 / 0.897; 2: 0.351 / 0.500 / 0.900; 3: 0.351 / 0.508 / 0.899; 4: 0.349 / 0.501 / 0.899; 5: 0.349 / 0.509 / 0.899; 6: 0.346 / 0.504 / 0.900; 7: 0.348 / 0.497 / 0.899; 8: 0.345 / 0.503 / 0.899; 9: 0.347 / 0.504 / 0.898; 10: 0.344 / 0.494 / 0.898; 11: 0.345 / 0.500 / 0.898; 12: 0.345 / 0.501 / 0.898; 13: 0.347 / 0.504 / 0.898; 14: 0.345 / 0.498 / 0.898; 15: 0.347 / 0.508 / 0.898
- 30d: 1: 0.363 / 0.528 / 0.899; 2: 0.352 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.351 / 0.504 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.498 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.348 / 0.499 / 0.900; 10: 0.349 / 0.503 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.502 / 0.900; 13: 0.347 / 0.501 / 0.900; 14: 0.347 / 0.500 / 0.900; 15: 0.347 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.082 (body 0.059, range 0.106); 'price stays where it was' would score 0.060; colour right 0.567; typical miss of the close 15.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.112 (body 0.075, range 0.149); 'price stays where it was' would score 0.103; colour right 0.503; typical miss of the close 12.6 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.125 (body 0.085, range 0.166); 'price stays where it was' would score 0.123; colour right 0.503; typical miss of the close 12.8 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.160); 'price stays where it was' would score 0.123; colour right 0.504; typical miss of the close 8.8 bp; chain ended on the right side 0.470 of 672 chains; n=10080
- 30d: match 0.124 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 8.3 bp; chain ended on the right side 0.511 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.3; 2: 0.199 / 4.9; 3: 0.168 / 6.6; 4: 0.131 / 6.9; 5: 0.125 / 7.6; 6: 0.114 / 8.3; 7: 0.111 / 8.5; 8: 0.099 / 9.4; 9: 0.090 / 9.4; 10: 0.089 / 9.9; 11: 0.085 / 10.2; 12: 0.077 / 10.5; 13: 0.070 / 10.8; 14: 0.071 / 11.4; 15: 0.064 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 135111, probability skill vs chance 0.233, widened contest next: False
  - now: threshold 0.8381, hit rate recent 0.9231 / long run 0.9308
    - 6h: 14 calls (57 a day), hit rate 1.000, chance 0.292, naive rule 0.502, lift 3.43x
    - 24h: 51 calls (51 a day), hit rate 0.922, chance 0.290, naive rule 0.496, lift 3.18x
    - 7d: 413 calls (59 a day), hit rate 0.927, chance 0.293, naive rule 0.499, lift 3.17x
    - 30d: 1738 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.494, lift 3.17x
  - next: threshold 0.5656, hit rate recent 0.5982 / long run 0.5979
    - 6h: 10 calls (41 a day), hit rate 0.700, chance 0.292, lift 2.40x
    - 24h: 39 calls (39 a day), hit rate 0.641, chance 0.290, lift 2.21x
    - 7d: 744 calls (106 a day), hit rate 0.599, chance 0.293, lift 2.05x
    - 30d: 2983 calls (99 a day), hit rate 0.586, chance 0.294, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.497; 0.35: 533, 0.523; 0.40: 473, 0.580; 0.45: 404, 0.651; 0.50: 354, 0.701; 0.55: 308, 0.743; 0.60: 261, 0.787; 0.65: 219, 0.812; 0.70: 173, 0.843; 0.75: 138, 0.876; 0.80: 92, 0.909; 0.85: 46, 0.947; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.429; 0.35: 500, 0.463; 0.40: 404, 0.499; 0.45: 306, 0.534; 0.50: 198, 0.569; 0.55: 89, 0.573; 0.60: 12, 0.627; 0.65: 1, 0.619
- **K=5**: model 1792540800, labels learned 135109, probability skill vs chance 0.2235, widened contest next: False
  - now: threshold 0.6906, hit rate recent 0.8007 / long run 0.8173
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.183, naive rule 0.376, lift 3.98x
    - 24h: 48 calls (48 a day), hit rate 0.812, chance 0.187, naive rule 0.422, lift 4.34x
    - 7d: 410 calls (59 a day), hit rate 0.810, chance 0.187, naive rule 0.416, lift 4.32x
    - 30d: 1631 calls (54 a day), hit rate 0.815, chance 0.187, naive rule 0.406, lift 4.35x
  - next: threshold 0.4511, hit rate recent 0.51 / long run 0.5089
    - 6h: 10 calls (41 a day), hit rate 0.400, chance 0.183, lift 2.19x
    - 24h: 51 calls (51 a day), hit rate 0.510, chance 0.187, lift 2.72x
    - 7d: 376 calls (54 a day), hit rate 0.537, chance 0.187, lift 2.87x
    - 30d: 2721 calls (91 a day), hit rate 0.479, chance 0.187, lift 2.56x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.425; 0.35: 346, 0.491; 0.40: 280, 0.564; 0.45: 230, 0.615; 0.50: 184, 0.663; 0.55: 146, 0.700; 0.60: 111, 0.748; 0.65: 77, 0.785; 0.70: 49, 0.817; 0.75: 29, 0.860; 0.80: 10, 0.877
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.385; 0.35: 256, 0.421; 0.40: 160, 0.460; 0.45: 67, 0.481; 0.50: 12, 0.492; 0.55: 1, 0.444
- **K=8**: model 1793059200, labels learned 135106, probability skill vs chance 0.2084, widened contest next: False
  - now: threshold 0.5748, hit rate recent 0.67 / long run 0.6903
    - 6h: 10 calls (41 a day), hit rate 0.500, chance 0.116, naive rule 0.313, lift 4.32x
    - 24h: 46 calls (46 a day), hit rate 0.652, chance 0.121, naive rule 0.353, lift 5.41x
    - 7d: 369 calls (53 a day), hit rate 0.696, chance 0.123, naive rule 0.346, lift 5.67x
    - 30d: 1570 calls (52 a day), hit rate 0.679, chance 0.120, naive rule 0.334, lift 5.64x
  - next: threshold 0.3634, hit rate recent 0.4336 / long run 0.4177
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.116, lift 5.50x
    - 24h: 49 calls (49 a day), hit rate 0.429, chance 0.121, lift 3.55x
    - 7d: 489 calls (70 a day), hit rate 0.436, chance 0.123, lift 3.54x
    - 30d: 2762 calls (92 a day), hit rate 0.391, chance 0.120, lift 3.24x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.431; 0.35: 191, 0.495; 0.40: 151, 0.541; 0.45: 115, 0.590; 0.50: 84, 0.636; 0.55: 61, 0.669; 0.60: 41, 0.700; 0.65: 24, 0.773; 0.70: 12, 0.809; 0.75: 2, 0.766
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.361; 0.35: 90, 0.388; 0.40: 26, 0.415; 0.45: 5, 0.438; 0.50: 1, 0.640
- **K=13**: model 1793577600, labels learned 135101, probability skill vs chance 0.1828, widened contest next: False
  - now: threshold 0.4566, hit rate recent 0.5589 / long run 0.5688
    - 6h: 12 calls (50 a day), hit rate 0.500, chance 0.067, naive rule 0.205, lift 7.50x
    - 24h: 54 calls (55 a day), hit rate 0.537, chance 0.077, naive rule 0.289, lift 6.96x
    - 7d: 413 calls (59 a day), hit rate 0.574, chance 0.080, naive rule 0.292, lift 7.21x
    - 30d: 1658 calls (55 a day), hit rate 0.561, chance 0.077, naive rule 0.280, lift 7.26x
  - next: threshold 0.2863, hit rate recent 0.3483 / long run 0.3372
    - 6h: 10 calls (42 a day), hit rate 0.300, chance 0.067, lift 4.50x
    - 24h: 44 calls (44 a day), hit rate 0.318, chance 0.077, lift 4.12x
    - 7d: 349 calls (50 a day), hit rate 0.355, chance 0.080, lift 4.46x
    - 30d: 1830 calls (61 a day), hit rate 0.326, chance 0.077, lift 4.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.438; 0.35: 93, 0.489; 0.40: 66, 0.545; 0.45: 45, 0.586; 0.50: 30, 0.644; 0.55: 19, 0.673; 0.60: 10, 0.712; 0.65: 3, 0.685; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.332; 0.35: 13, 0.349; 0.40: 3, 0.415; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.019 | 3.90% | 0.917 | 0.533 | 0.251 | 0.450 | 0.466 |
| 6h | 15.084 | 2.01% | 0.919 | 0.506 | 0.251 | 0.453 | 0.361 |
| 24h | 20.582 | 4.22% | 0.908 | 0.506 | 0.251 | 0.477 | 0.675 |
| 7d | 15.858 | 4.99% | 0.900 | 0.500 | 0.250 | 0.506 | 0.748 |
| 30d | 14.736 | 4.24% | 0.900 | 0.500 | 0.250 | 0.498 | 0.688 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.587 | 13.997 | 14.086 | 13.933 | 14.690 | 14.097 | 14.026 | 13.962 | 14.001 | 14.019 |
| 6h | 15.394 | 15.089 | 15.107 | 15.163 | 15.354 | 15.214 | 15.098 | 15.059 | 15.064 | 15.084 |
| 24h | 21.488 | 20.780 | 20.635 | 20.581 | 20.901 | 20.890 | 20.641 | 20.578 | 20.550 | 20.582 |
| 7d | 16.690 | 16.023 | 15.973 | 15.901 | 16.168 | 16.199 | 15.854 | 15.833 | 15.833 | 15.858 |
| 30d | 15.389 | 14.888 | 14.828 | 14.764 | 15.006 | 14.952 | 14.731 | 14.707 | 14.709 | 14.736 |

## Next candle

- candle starting 2026-11-04 23:57 UTC, last close 2423.57
- P(up) 0.4948, return quantiles (bp): {'05': -6.528, '10': -4.661, '25': -2.219, '40': -0.792, '50': -0.035, '60': 0.688, '75': 2.655, '90': 5.108, '95': 6.657}
- changepoint probability 0.0457, regime age 68.6 min
- agent weights: empirical 0.004, ewma 0.113, garch 0.211, har 0.218, bocpd 0.033, hmm 0.036, online_qr 0.143, lgbm 0.241

## Learning log

- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- HMM volatility states (sd, bp per minute): [2.15, 4.45, 10.37], current probabilities: [0.237, 0.75, 0.013]
- live generator: {'versions': 60, 'latest_effective': '2026-11-05 00:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.34, 'l_abs': 0.729, 'l_hi': 0.749, 'l_lo': 0.805, 'b05': 0.746, 'b25': 0.728, 'b75': 0.674, 'b95': 0.721}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.252, 1.664, 1.964, 2.635, 2.669, 3.39, 3.221, 3.86, 3.917, 4.928, 4.395, 5.379, 5.482, 5.918]}
- calibration offsets (in sigma): {'05': 0.078, '10': 0.096, '25': 0.06, '40': 0.004, '50': -0.02, '60': -0.064, '75': -0.01, '90': -0.026, '95': -0.078}
