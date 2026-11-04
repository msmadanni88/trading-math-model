# ETH-USD 60s candle generator - report

- generated: 2026-11-04 18:40 UTC
- last closed candle: 2026-11-04 18:40 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: chain_end_side 0.478 in the last 7 days, -0.059 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.396 (96) | 0.478 (672) [0.449, 0.504] | 0.509 (2878) [0.490, 0.528] | 0.512 (6042) [0.499, 0.525] | 0.513 (3070) [0.494, 0.532] | 0.500 (74) | 0.500 | down -0.059 (noise 0.028) |
| colour_clear | 0.518 (819) | 0.534 (5467) [0.525, 0.544] | 0.543 (23791) [0.539, 0.548] | 0.521 (49424) [0.515, 0.527] | 0.544 (25186) [0.539, 0.548] | 0.489 (609) | 0.500 | flat -0.010 (noise 0.009) |
| colour_confident | 0.621 (95) | 0.576 (913) [0.564, 0.593] | 0.596 (4351) [0.584, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.597 (4695) [0.586, 0.609] | 0.584 (89) | 0.500 | flat -0.028 (noise 0.021) |
| colour_next | 0.526 (1436) | 0.531 (9974) [0.524, 0.537] | 0.529 (42856) [0.526, 0.533] | 0.515 (90026) [0.511, 0.519] | 0.530 (45677) [0.526, 0.533] | 0.502 (1117) | 0.500 | flat +0.003 (noise 0.007) |
| colour_path | 0.505 (20104) | 0.502 (139636) [0.500, 0.504] | 0.501 (599984) [0.500, 0.502] | 0.501 (1260364) [0.500, 0.502] | 0.501 (639478) [0.499, 0.502] | 0.501 (15638) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.571 (14) | 0.621 (203) [0.570, 0.671] | 0.631 (1129) [0.610, 0.652] | 0.633 (1244) [0.613, 0.652] | 0.633 (1244) [0.613, 0.652] | 0.565 (23) | 0.500 | flat +0.007 (noise 0.042) |
| reversal_k13_next | 0.409 (66) | 0.352 (358) [0.311, 0.391] | 0.324 (1859) [0.310, 0.339] | 0.313 (4152) [0.303, 0.324] | 0.326 (2047) [0.313, 0.339] | 0.324 (34) | 0.077 | flat +0.031 (noise 0.034) |
| reversal_k13_now | 0.649 (57) | 0.582 (423) [0.544, 0.615] | 0.561 (1673) [0.543, 0.580] | 0.574 (3255) [0.560, 0.588] | 0.568 (1783) [0.547, 0.589] | 0.571 (42) | 0.077 | flat +0.016 (noise 0.036) |
| reversal_k3_next | 0.523 (65) | 0.597 (819) [0.580, 0.614] | 0.586 (2993) [0.575, 0.598] | 0.586 (5701) [0.577, 0.595] | 0.584 (3261) [0.574, 0.596] | 0.621 (29) | 0.293 | flat -0.010 (noise 0.025) |
| reversal_k3_now | 0.904 (52) | 0.925 (428) [0.905, 0.949] | 0.933 (1735) [0.922, 0.944] | 0.937 (3619) [0.931, 0.943] | 0.933 (1856) [0.923, 0.942] | 0.897 (39) | 0.293 | flat -0.029 (noise 0.018) |
| reversal_k5_next | 0.476 (63) | 0.535 (389) [0.511, 0.556] | 0.479 (2709) [0.464, 0.495] | 0.482 (5008) [0.471, 0.494] | 0.474 (3018) [0.460, 0.490] | 0.537 (41) | 0.187 | flat +0.036 (noise 0.031) |
| reversal_k5_now | 0.784 (51) | 0.814 (436) [0.799, 0.827] | 0.816 (1628) [0.806, 0.826] | 0.828 (3368) [0.819, 0.837] | 0.820 (1757) [0.809, 0.830] | 0.842 (38) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.409 (66) | 0.439 (540) [0.414, 0.465] | 0.389 (2787) [0.376, 0.403] | 0.393 (5057) [0.383, 0.404] | 0.391 (2951) [0.378, 0.405] | 0.368 (38) | 0.121 | up +0.057 (noise 0.028) |
| reversal_k8_now | 0.714 (49) | 0.714 (384) [0.676, 0.744] | 0.683 (1585) [0.664, 0.702] | 0.701 (3282) [0.687, 0.716] | 0.690 (1695) [0.669, 0.709] | 0.694 (36) | 0.121 | flat +0.039 (noise 0.036) |
| overall | 0.507 (22105) | 0.506 (154059) [0.504, 0.509] | 0.505 (662687) [0.503, 0.506] | 0.504 (1389874) [0.503, 0.505] | 0.505 (706593) [0.503, 0.506] | 0.503 (17126) | - | flat +0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07741, 0.1163] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5281, 'levels': [{'threshold': 0.07741, 'calls_per_day': 143.4, 'win_rate': 0.5838}, {'threshold': 0.1163, 'calls_per_day': 35.6, 'win_rate': 0.6508}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42861, 'rate': 0.5282}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15254 | 0.339 | 0.529 (14996) | 0.578 (2350) | 0.750 (2634) |
| volatility: normal | 15253 | 0.366 | 0.535 (15183) | 0.614 (1504) | 0.747 (2296) |
| volatility: wild | 15253 | 0.381 | 0.525 (15211) | 0.619 (846) | 0.761 (2103) |
| session: Asia 00-08 | 15360 | 0.362 | 0.537 (15249) | 0.602 (1670) | 0.755 (2295) |
| session: Europe 08-13 | 9600 | 0.356 | 0.533 (9499) | 0.597 (1196) | 0.743 (1593) |
| session: US 13-21 | 15220 | 0.369 | 0.526 (15112) | 0.594 (1230) | 0.758 (2310) |
| session: late 21-24 | 5580 | 0.351 | 0.512 (5530) | 0.589 (604) | 0.749 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.397 | 0.346 | 0.277 | 0.277 | 0.533 | 0.291 | 0.503 | 1.377 |
| 6h | 360 | 0.374 | 0.367 | 0.287 | 0.321 | 0.492 | 0.242 | 0.505 | 1.257 |
| 24h | 1440 | 0.364 | 0.366 | 0.278 | 0.310 | 0.503 | 0.248 | 0.480 | 1.271 |
| 7d | 10080 | 0.360 | 0.357 | 0.275 | 0.304 | 0.528 | 0.259 | 0.462 | 1.283 |
| 30d | 43200 | 0.363 | 0.356 | 0.276 | 0.307 | 0.528 | 0.262 | 0.464 | 1.254 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.397 / 0.533 / 0.933; 2: 0.357 / 0.450 / 0.833; 3: 0.382 / 0.483 / 0.900; 4: 0.391 / 0.550 / 0.833; 5: 0.399 / 0.583 / 0.900; 6: 0.360 / 0.417 / 0.867; 7: 0.393 / 0.550 / 0.917; 8: 0.371 / 0.483 / 0.833; 9: 0.386 / 0.517 / 0.817; 10: 0.378 / 0.517 / 0.833; 11: 0.371 / 0.483 / 0.933; 12: 0.417 / 0.567 / 0.900; 13: 0.366 / 0.450 / 0.917; 14: 0.373 / 0.467 / 0.933; 15: 0.398 / 0.600 / 0.883
- 6h: 1: 0.374 / 0.492 / 0.917; 2: 0.367 / 0.506 / 0.875; 3: 0.360 / 0.450 / 0.881; 4: 0.383 / 0.567 / 0.858; 5: 0.370 / 0.478 / 0.878; 6: 0.360 / 0.486 / 0.847; 7: 0.362 / 0.486 / 0.903; 8: 0.363 / 0.533 / 0.847; 9: 0.357 / 0.492 / 0.825; 10: 0.362 / 0.483 / 0.847; 11: 0.349 / 0.469 / 0.889; 12: 0.366 / 0.522 / 0.858; 13: 0.347 / 0.472 / 0.872; 14: 0.351 / 0.467 / 0.878; 15: 0.349 / 0.478 / 0.844
- 24h: 1: 0.364 / 0.503 / 0.909; 2: 0.365 / 0.517 / 0.911; 3: 0.361 / 0.500 / 0.890; 4: 0.363 / 0.508 / 0.886; 5: 0.357 / 0.479 / 0.913; 6: 0.354 / 0.492 / 0.881; 7: 0.355 / 0.488 / 0.910; 8: 0.349 / 0.498 / 0.903; 9: 0.358 / 0.511 / 0.894; 10: 0.353 / 0.493 / 0.898; 11: 0.353 / 0.505 / 0.915; 12: 0.359 / 0.517 / 0.893; 13: 0.357 / 0.504 / 0.903; 14: 0.358 / 0.509 / 0.896; 15: 0.353 / 0.495 / 0.896
- 7d: 1: 0.360 / 0.528 / 0.898; 2: 0.351 / 0.499 / 0.900; 3: 0.351 / 0.507 / 0.900; 4: 0.349 / 0.500 / 0.899; 5: 0.350 / 0.510 / 0.900; 6: 0.346 / 0.504 / 0.899; 7: 0.348 / 0.497 / 0.901; 8: 0.345 / 0.506 / 0.900; 9: 0.348 / 0.506 / 0.899; 10: 0.345 / 0.493 / 0.899; 11: 0.345 / 0.500 / 0.900; 12: 0.345 / 0.499 / 0.900; 13: 0.346 / 0.502 / 0.899; 14: 0.345 / 0.498 / 0.899; 15: 0.347 / 0.507 / 0.898
- 30d: 1: 0.363 / 0.528 / 0.899; 2: 0.351 / 0.496 / 0.899; 3: 0.354 / 0.509 / 0.900; 4: 0.350 / 0.498 / 0.899; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.500 / 0.899; 7: 0.349 / 0.499 / 0.900; 8: 0.348 / 0.502 / 0.899; 9: 0.348 / 0.500 / 0.899; 10: 0.349 / 0.503 / 0.900; 11: 0.346 / 0.498 / 0.900; 12: 0.348 / 0.501 / 0.899; 13: 0.347 / 0.501 / 0.899; 14: 0.347 / 0.500 / 0.899; 15: 0.347 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.206 (body 0.170, range 0.242); 'price stays where it was' would score 0.187; colour right 0.517; typical miss of the close 9.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.149 (body 0.106, range 0.193); 'price stays where it was' would score 0.148; colour right 0.508; typical miss of the close 14.4 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.125 (body 0.084, range 0.165); 'price stays where it was' would score 0.128; colour right 0.495; typical miss of the close 11.5 bp; chain ended on the right side 0.458 of 96 chains; n=1440
- 7d: match 0.122 (body 0.083, range 0.160); 'price stays where it was' would score 0.124; colour right 0.503; typical miss of the close 8.8 bp; chain ended on the right side 0.464 of 672 chains; n=10080
- 30d: match 0.124 (body 0.085, range 0.164); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 8.2 bp; chain ended on the right side 0.510 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.367 / 4.3; 2: 0.200 / 4.9; 3: 0.169 / 6.5; 4: 0.131 / 6.8; 5: 0.125 / 7.6; 6: 0.114 / 8.2; 7: 0.112 / 8.5; 8: 0.099 / 9.3; 9: 0.090 / 9.3; 10: 0.089 / 9.8; 11: 0.085 / 10.1; 12: 0.077 / 10.4; 13: 0.070 / 10.8; 14: 0.071 / 11.3; 15: 0.064 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 134794, probability skill vs chance 0.2241, widened contest next: False
  - now: threshold 0.8381, hit rate recent 0.9059 / long run 0.9294
    - 6h: 11 calls (45 a day), hit rate 0.909, chance 0.297, naive rule 0.520, lift 3.06x
    - 24h: 49 calls (49 a day), hit rate 0.918, chance 0.298, naive rule 0.506, lift 3.08x
    - 7d: 415 calls (59 a day), hit rate 0.928, chance 0.293, naive rule 0.497, lift 3.17x
    - 30d: 1737 calls (58 a day), hit rate 0.931, chance 0.294, naive rule 0.494, lift 3.17x
  - next: threshold 0.5656, hit rate recent 0.5776 / long run 0.5962
    - 6h: 5 calls (20 a day), hit rate 0.600, chance 0.297, lift 2.02x
    - 24h: 45 calls (45 a day), hit rate 0.578, chance 0.298, lift 1.94x
    - 7d: 759 calls (108 a day), hit rate 0.598, chance 0.293, lift 2.04x
    - 30d: 2982 calls (99 a day), hit rate 0.586, chance 0.294, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.498; 0.35: 533, 0.523; 0.40: 473, 0.580; 0.45: 404, 0.651; 0.50: 354, 0.701; 0.55: 308, 0.743; 0.60: 261, 0.787; 0.65: 219, 0.811; 0.70: 173, 0.843; 0.75: 138, 0.876; 0.80: 92, 0.908; 0.85: 46, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.428; 0.35: 500, 0.463; 0.40: 404, 0.498; 0.45: 306, 0.534; 0.50: 198, 0.569; 0.55: 89, 0.572; 0.60: 12, 0.631; 0.65: 1, 0.636
- **K=5**: model 1792540800, labels learned 134792, probability skill vs chance 0.2215, widened contest next: False
  - now: threshold 0.6906, hit rate recent 0.8224 / long run 0.8193
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.218, naive rule 0.521, lift 3.33x
    - 24h: 49 calls (49 a day), hit rate 0.857, chance 0.188, naive rule 0.426, lift 4.56x
    - 7d: 413 calls (59 a day), hit rate 0.818, chance 0.187, naive rule 0.416, lift 4.37x
    - 30d: 1634 calls (54 a day), hit rate 0.816, chance 0.188, naive rule 0.407, lift 4.35x
  - next: threshold 0.4511, hit rate recent 0.5286 / long run 0.5107
    - 6h: 11 calls (45 a day), hit rate 0.636, chance 0.218, lift 2.92x
    - 24h: 57 calls (57 a day), hit rate 0.509, chance 0.188, lift 2.71x
    - 7d: 378 calls (54 a day), hit rate 0.537, chance 0.187, lift 2.87x
    - 30d: 2719 calls (91 a day), hit rate 0.479, chance 0.188, lift 2.55x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 418, 0.426; 0.35: 346, 0.493; 0.40: 279, 0.566; 0.45: 229, 0.617; 0.50: 183, 0.665; 0.55: 145, 0.701; 0.60: 110, 0.749; 0.65: 77, 0.786; 0.70: 49, 0.818; 0.75: 29, 0.862; 0.80: 10, 0.877
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.386; 0.35: 255, 0.421; 0.40: 159, 0.459; 0.45: 67, 0.481; 0.50: 12, 0.490; 0.55: 1, 0.444
- **K=8**: model 1793059200, labels learned 134789, probability skill vs chance 0.2053, widened contest next: False
  - now: threshold 0.5748, hit rate recent 0.7037 / long run 0.6935
    - 6h: 7 calls (29 a day), hit rate 0.571, chance 0.143, naive rule 0.473, lift 4.00x
    - 24h: 43 calls (43 a day), hit rate 0.744, chance 0.121, naive rule 0.351, lift 6.15x
    - 7d: 368 calls (53 a day), hit rate 0.709, chance 0.124, naive rule 0.349, lift 5.73x
    - 30d: 1572 calls (52 a day), hit rate 0.681, chance 0.121, naive rule 0.335, lift 5.64x
  - next: threshold 0.3634, hit rate recent 0.3948 / long run 0.4137
    - 6h: 11 calls (45 a day), hit rate 0.364, chance 0.143, lift 2.55x
    - 24h: 49 calls (49 a day), hit rate 0.367, chance 0.121, lift 3.04x
    - 7d: 498 calls (71 a day), hit rate 0.436, chance 0.124, lift 3.52x
    - 30d: 2762 calls (92 a day), hit rate 0.390, chance 0.121, lift 3.23x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 245, 0.432; 0.35: 191, 0.496; 0.40: 150, 0.542; 0.45: 115, 0.590; 0.50: 84, 0.637; 0.55: 61, 0.671; 0.60: 41, 0.702; 0.65: 24, 0.774; 0.70: 12, 0.810; 0.75: 2, 0.766
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.361; 0.35: 90, 0.388; 0.40: 26, 0.416; 0.45: 5, 0.438; 0.50: 1, 0.640
- **K=13**: model 1793577600, labels learned 134784, probability skill vs chance 0.1862, widened contest next: False
  - now: threshold 0.4566, hit rate recent 0.5847 / long run 0.571
    - 6h: 11 calls (46 a day), hit rate 0.364, chance 0.080, naive rule 0.373, lift 4.56x
    - 24h: 55 calls (56 a day), hit rate 0.600, chance 0.083, naive rule 0.306, lift 7.22x
    - 7d: 411 calls (59 a day), hit rate 0.586, chance 0.080, naive rule 0.296, lift 7.33x
    - 30d: 1659 calls (55 a day), hit rate 0.561, chance 0.077, naive rule 0.281, lift 7.26x
  - next: threshold 0.2863, hit rate recent 0.3586 / long run 0.3379
    - 6h: 12 calls (50 a day), hit rate 0.417, chance 0.080, lift 5.23x
    - 24h: 49 calls (50 a day), hit rate 0.306, chance 0.083, lift 3.68x
    - 7d: 348 calls (50 a day), hit rate 0.362, chance 0.080, lift 4.52x
    - 30d: 1836 calls (61 a day), hit rate 0.326, chance 0.077, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 129, 0.439; 0.35: 93, 0.490; 0.40: 66, 0.545; 0.45: 44, 0.587; 0.50: 30, 0.644; 0.55: 19, 0.675; 0.60: 10, 0.712; 0.65: 3, 0.685; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.332; 0.35: 13, 0.349; 0.40: 3, 0.415; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 15.973 | 0.75% | 0.933 | 0.483 | 0.253 | 0.317 | 0.020 |
| 6h | 28.038 | 6.11% | 0.911 | 0.525 | 0.252 | 0.458 | 0.706 |
| 24h | 19.712 | 4.25% | 0.910 | 0.507 | 0.251 | 0.484 | 0.703 |
| 7d | 15.926 | 5.05% | 0.900 | 0.501 | 0.250 | 0.508 | 0.750 |
| 30d | 14.670 | 4.29% | 0.900 | 0.500 | 0.251 | 0.498 | 0.690 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 16.093 | 16.092 | 16.096 | 16.014 | 16.387 | 16.435 | 15.993 | 16.004 | 15.990 | 15.973 |
| 6h | 29.862 | 28.327 | 28.032 | 27.916 | 28.429 | 28.824 | 28.325 | 28.153 | 28.023 | 28.038 |
| 24h | 20.588 | 19.908 | 19.764 | 19.692 | 20.021 | 20.027 | 19.770 | 19.711 | 19.679 | 19.712 |
| 7d | 16.774 | 16.098 | 16.046 | 15.967 | 16.245 | 16.273 | 15.920 | 15.904 | 15.902 | 15.926 |
| 30d | 15.327 | 14.823 | 14.762 | 14.699 | 14.939 | 14.886 | 14.665 | 14.641 | 14.643 | 14.670 |

## Next candle

- candle starting 2026-11-04 18:40 UTC, last close 2424.07
- P(up) 0.4914, return quantiles (bp): {'05': -10.447, '10': -7.211, '25': -3.602, '40': -1.633, '50': -0.139, '60': 1.495, '75': 4.303, '90': 8.262, '95': 11.063}
- changepoint probability 0.071, regime age 78.5 min
- agent weights: empirical 0.003, ewma 0.059, garch 0.218, har 0.354, bocpd 0.029, hmm 0.014, online_qr 0.107, lgbm 0.217

## Learning log

- 2026-11-02 12:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8951}, "hmm": {"sd_bp": [2.67, 6.37, 20.05], "stay": [0.98, 0.96, 0.932]}}
- 2026-11-03 00:00 UTC: {"garch": {"alpha": 0.0952, "beta": 0.8976}, "hmm": {"sd_bp": [2.67, 6.48, 20.04], "stay": [0.981, 0.964, 0.935]}, "lgbm": {"challenger_loss": 0.25144, "champion_loss": 0.25148, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47796, "challengers": 1, "chance_loss": 0.60093, "widened": false, "champion_loss": 0.47378, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36939, "challengers": 1, "chance_loss": 0.48461, "widened": false, "champion_loss": 0.36616, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28787, "challengers": 1, "chance_loss": 0.3844, "widened": false, "champion_loss": 0.28763, "promoted": false}, "reversal_k13": {"challenger_loss": 0.199, "challengers": 3, "chance_loss": 0.27245, "widened": true, "champion_loss": 0.19863, "promoted": false}}
- 2026-11-03 12:00 UTC: {"garch": {"alpha": 0.0801, "beta": 0.9062}, "hmm": {"sd_bp": [2.59, 5.61, 12.38], "stay": [0.975, 0.959, 0.94]}}
- 2026-11-04 00:00 UTC: {"garch": {"alpha": 0.0816, "beta": 0.8974}, "hmm": {"sd_bp": [2.34, 4.65, 10.51], "stay": [0.967, 0.961, 0.941]}, "lgbm": {"challenger_loss": 0.25412, "champion_loss": 0.25409, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48045, "challengers": 3, "chance_loss": 0.5985, "widened": true, "champion_loss": 0.48021, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36601, "challengers": 1, "chance_loss": 0.47408, "widened": false, "champion_loss": 0.36315, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2789, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.27769, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20663, "challengers": 1, "chance_loss": 0.2832, "widened": false, "champion_loss": 0.20558, "promoted": false}}
- 2026-11-04 12:00 UTC: {"garch": {"alpha": 0.0858, "beta": 0.8968}, "hmm": {"sd_bp": [2.15, 4.45, 10.37], "stay": [0.967, 0.965, 0.946]}}
- HMM volatility states (sd, bp per minute): [2.15, 4.45, 10.37], current probabilities: [0.038, 0.517, 0.445]
- live generator: {'versions': 60, 'latest_effective': '2026-11-04 18:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.274, 'l_abs': 0.728, 'l_hi': 0.753, 'l_lo': 0.806, 'b05': 0.748, 'b25': 0.73, 'b75': 0.663, 'b95': 0.714}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.783, 1.98, 2.584, 2.672, 3.582, 2.815, 3.757, 4.976, 4.755, 3.777, 4.732, 4.742, 4.833, 5.883]}
- calibration offsets (in sigma): {'05': 0.0695, '10': 0.129, '25': 0.0675, '40': -0.034, '50': -0.035, '60': -0.016, '75': 0.0025, '90': -0.029, '95': -0.0295}
