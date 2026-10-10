# ETH-USD 60s candle generator - report

- generated: 2026-10-10 02:12 UTC
- last closed candle: 2026-10-10 02:12 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.500 (96) | 0.499 (671) [0.449, 0.550] | 0.503 (2875) [0.483, 0.524] | 0.509 (3643) [0.492, 0.526] | 0.499 (671) [0.449, 0.550] | 0.625 (8) | 0.500 | flat -0.029 (noise 0.036) |
| colour_clear | 0.544 (796) | 0.546 (5306) [0.538, 0.554] | 0.508 (23193) [0.502, 0.516] | 0.505 (29544) [0.499, 0.512] | 0.546 (5306) [0.538, 0.554] | 0.500 (84) | 0.500 | up +0.051 (noise 0.010) |
| colour_confident | 0.687 (134) | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.619 (949) [0.580, 0.657] | 0.640 (25) | 0.500 | - |
| colour_next | 0.516 (1433) | 0.529 (9975) [0.520, 0.538] | 0.507 (42879) [0.502, 0.512] | 0.506 (54324) [0.501, 0.510] | 0.529 (9975) [0.520, 0.538] | 0.534 (131) | 0.500 | up +0.024 (noise 0.007) |
| colour_path | 0.501 (20062) | 0.499 (139650) [0.495, 0.503] | 0.501 (600306) [0.499, 0.502] | 0.500 (760536) [0.499, 0.501] | 0.499 (139650) [0.495, 0.503] | 0.480 (1834) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.880 (25) | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.660 (244) [0.598, 0.735] | 0.714 (7) | 0.500 | - |
| reversal_k13_next | 0.338 (74) | 0.324 (541) [0.309, 0.337] | 0.311 (2040) [0.297, 0.327] | 0.305 (2646) [0.291, 0.319] | 0.324 (541) [0.309, 0.337] | 0.444 (9) | 0.077 | up +0.057 (noise 0.027) |
| reversal_k13_now | 0.660 (47) | 0.596 (386) [0.555, 0.647] | 0.588 (1486) [0.565, 0.611] | 0.584 (1858) [0.566, 0.604] | 0.596 (386) [0.555, 0.647] | 0.200 (5) | 0.077 | flat +0.015 (noise 0.038) |
| reversal_k3_next | 0.565 (85) | 0.570 (572) [0.541, 0.607] | 0.584 (2351) [0.569, 0.599] | 0.584 (3012) [0.572, 0.598] | 0.570 (572) [0.541, 0.607] | 0.667 (9) | 0.292 | flat -0.008 (noise 0.029) |
| reversal_k3_now | 0.921 (63) | 0.926 (408) [0.917, 0.939] | 0.940 (1711) [0.932, 0.948] | 0.939 (2171) [0.931, 0.946] | 0.926 (408) [0.917, 0.939] | 0.750 (8) | 0.292 | flat -0.023 (noise 0.017) |
| reversal_k5_next | 0.486 (74) | 0.446 (596) [0.419, 0.481] | 0.488 (2110) [0.468, 0.508] | 0.483 (2586) [0.467, 0.500] | 0.446 (596) [0.419, 0.481] | 0.750 (4) | 0.187 | flat -0.028 (noise 0.030) |
| reversal_k5_now | 0.787 (47) | 0.818 (385) [0.787, 0.851] | 0.835 (1578) [0.819, 0.850] | 0.834 (1996) [0.820, 0.848] | 0.818 (385) [0.787, 0.851] | 0.429 (7) | 0.187 | flat -0.052 (noise 0.027) |
| reversal_k8_next | 0.407 (81) | 0.388 (621) [0.361, 0.417] | 0.405 (2121) [0.388, 0.424] | 0.394 (2727) [0.380, 0.410] | 0.388 (621) [0.361, 0.417] | 1.000 (4) | 0.121 | flat +0.005 (noise 0.032) |
| reversal_k8_now | 0.596 (47) | 0.698 (407) [0.656, 0.740] | 0.720 (1585) [0.700, 0.740] | 0.711 (1994) [0.693, 0.729] | 0.698 (407) [0.656, 0.740] | 0.333 (6) | 0.122 | flat -0.041 (noise 0.035) |
| overall | 0.503 (22109) | 0.503 (154212) [0.498, 0.507] | 0.503 (661042) [0.502, 0.505] | 0.503 (837493) [0.501, 0.504] | 0.503 (154212) [0.498, 0.507] | 0.486 (2025) | - | flat -0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07816, 0.1175] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5319, 'levels': [{'threshold': 0.07816, 'calls_per_day': 146.9, 'win_rate': 0.6208}, {'threshold': 0.1175, 'calls_per_day': 36.7, 'win_rate': 0.6654}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 8974, 'rate': 0.5312}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14924 | 0.334 | 0.515 (14710) | 0.616 (743) | 0.775 (2389) |
| volatility: normal | 14924 | 0.361 | 0.510 (14856) | 0.612 (165) | 0.768 (2102) |
| volatility: wild | 14924 | 0.374 | 0.496 (14881) | 0.667 (66) | 0.779 (2067) |
| session: Asia 00-08 | 15012 | 0.353 | 0.509 (14909) | 0.597 (352) | 0.778 (2125) |
| session: Europe 08-13 | 9300 | 0.351 | 0.505 (9241) | 0.598 (194) | 0.762 (1476) |
| session: US 13-21 | 14880 | 0.366 | 0.505 (14783) | 0.630 (249) | 0.783 (2165) |
| session: late 21-24 | 5580 | 0.349 | 0.510 (5514) | 0.670 (179) | 0.761 (792) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.302 | 0.313 | 0.212 | 0.212 | 0.500 | 0.237 | 0.367 | 0.993 |
| 6h | 360 | 0.336 | 0.327 | 0.246 | 0.264 | 0.511 | 0.253 | 0.419 | 1.244 |
| 24h | 1440 | 0.356 | 0.356 | 0.271 | 0.304 | 0.513 | 0.255 | 0.457 | 1.173 |
| 7d | 10080 | 0.351 | 0.345 | 0.272 | 0.296 | 0.530 | 0.255 | 0.447 | 1.221 |
| 30d | 43200 | 0.356 | 0.354 | 0.279 | 0.308 | 0.507 | 0.248 | 0.464 | 1.284 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.302 / 0.500 / 0.833; 2: 0.347 / 0.650 / 0.867; 3: 0.305 / 0.483 / 0.933; 4: 0.331 / 0.567 / 0.817; 5: 0.323 / 0.533 / 0.883; 6: 0.277 / 0.417 / 0.883; 7: 0.277 / 0.417 / 0.900; 8: 0.289 / 0.433 / 0.917; 9: 0.285 / 0.433 / 0.917; 10: 0.262 / 0.383 / 0.933; 11: 0.308 / 0.450 / 0.883; 12: 0.279 / 0.333 / 0.883; 13: 0.295 / 0.433 / 0.933; 14: 0.291 / 0.433 / 0.967; 15: 0.289 / 0.450 / 0.950
- 6h: 1: 0.336 / 0.511 / 0.889; 2: 0.338 / 0.517 / 0.903; 3: 0.327 / 0.480 / 0.967; 4: 0.327 / 0.477 / 0.889; 5: 0.331 / 0.475 / 0.908; 6: 0.316 / 0.444 / 0.878; 7: 0.326 / 0.508 / 0.886; 8: 0.335 / 0.511 / 0.886; 9: 0.323 / 0.506 / 0.883; 10: 0.329 / 0.511 / 0.872; 11: 0.323 / 0.506 / 0.861; 12: 0.326 / 0.460 / 0.869; 13: 0.325 / 0.508 / 0.869; 14: 0.329 / 0.497 / 0.889; 15: 0.333 / 0.511 / 0.881
- 24h: 1: 0.356 / 0.513 / 0.900; 2: 0.349 / 0.499 / 0.903; 3: 0.347 / 0.494 / 0.905; 4: 0.351 / 0.512 / 0.904; 5: 0.348 / 0.497 / 0.904; 6: 0.347 / 0.498 / 0.906; 7: 0.338 / 0.479 / 0.908; 8: 0.349 / 0.509 / 0.907; 9: 0.342 / 0.480 / 0.904; 10: 0.348 / 0.500 / 0.902; 11: 0.348 / 0.501 / 0.899; 12: 0.344 / 0.485 / 0.899; 13: 0.346 / 0.497 / 0.898; 14: 0.346 / 0.513 / 0.898; 15: 0.347 / 0.503 / 0.892
- 7d: 1: 0.351 / 0.530 / 0.895; 2: 0.341 / 0.503 / 0.900; 3: 0.343 / 0.510 / 0.901; 4: 0.341 / 0.506 / 0.901; 5: 0.338 / 0.496 / 0.902; 6: 0.336 / 0.494 / 0.901; 7: 0.336 / 0.500 / 0.901; 8: 0.336 / 0.491 / 0.901; 9: 0.333 / 0.487 / 0.901; 10: 0.337 / 0.504 / 0.900; 11: 0.336 / 0.498 / 0.900; 12: 0.336 / 0.499 / 0.900; 13: 0.338 / 0.506 / 0.900; 14: 0.335 / 0.497 / 0.899; 15: 0.336 / 0.495 / 0.900
- 30d: 1: 0.356 / 0.507 / 0.899; 2: 0.351 / 0.497 / 0.900; 3: 0.353 / 0.508 / 0.900; 4: 0.350 / 0.500 / 0.900; 5: 0.350 / 0.502 / 0.900; 6: 0.348 / 0.502 / 0.900; 7: 0.348 / 0.504 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.345 / 0.497 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.106 (body 0.084, range 0.128); 'price stays where it was' would score 0.099; colour right 0.483; typical miss of the close 5.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.133 (body 0.096, range 0.170); 'price stays where it was' would score 0.127; colour right 0.503; typical miss of the close 4.1 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.130 (body 0.091, range 0.169); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 6.8 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.116 (body 0.080, range 0.153); 'price stays where it was' would score 0.120; colour right 0.498; typical miss of the close 6.0 bp; chain ended on the right side 0.505 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.0 bp; chain ended on the right side 0.504 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.1; 2: 0.200 / 4.4; 3: 0.166 / 6.1; 4: 0.132 / 6.7; 5: 0.120 / 7.4; 6: 0.111 / 8.0; 7: 0.100 / 8.5; 8: 0.091 / 8.7; 9: 0.086 / 9.1; 10: 0.080 / 9.8; 11: 0.076 / 10.5; 12: 0.075 / 10.8; 13: 0.063 / 11.1; 14: 0.064 / 11.2; 15: 0.061 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 97806, probability skill vs chance 0.2268, widened contest next: True
  - now: threshold 0.8416, hit rate recent 0.8867 / long run 0.931
    - 6h: 19 calls (77 a day), hit rate 0.842, chance 0.334, naive rule 0.565, lift 2.52x
    - 24h: 68 calls (68 a day), hit rate 0.897, chance 0.313, naive rule 0.533, lift 2.87x
    - 7d: 411 calls (59 a day), hit rate 0.922, chance 0.295, naive rule 0.493, lift 3.13x
    - 30d: 1709 calls (57 a day), hit rate 0.939, chance 0.291, naive rule 0.482, lift 3.22x
  - next: threshold 0.5519, hit rate recent 0.58 / long run 0.5772
    - 6h: 22 calls (89 a day), hit rate 0.591, chance 0.334, lift 1.77x
    - 24h: 89 calls (89 a day), hit rate 0.573, chance 0.313, lift 1.83x
    - 7d: 569 calls (81 a day), hit rate 0.576, chance 0.295, lift 1.96x
    - 30d: 2354 calls (78 a day), hit rate 0.585, chance 0.291, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.493; 0.35: 537, 0.517; 0.40: 486, 0.562; 0.45: 418, 0.629; 0.50: 366, 0.683; 0.55: 321, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.802; 0.70: 181, 0.834; 0.75: 138, 0.872; 0.80: 97, 0.912; 0.85: 49, 0.948; 0.90: 2, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.458; 0.40: 412, 0.487; 0.45: 316, 0.519; 0.50: 206, 0.552; 0.55: 91, 0.584; 0.60: 13, 0.600; 0.65: 1, 0.682
- **K=5**: model 1791590400, labels learned 97804, probability skill vs chance 0.2027, widened contest next: True
  - now: threshold 0.713, hit rate recent 0.7459 / long run 0.8229
    - 6h: 15 calls (61 a day), hit rate 0.600, chance 0.203, naive rule 0.419, lift 2.96x
    - 24h: 51 calls (51 a day), hit rate 0.745, chance 0.197, naive rule 0.421, lift 3.78x
    - 7d: 387 calls (55 a day), hit rate 0.809, chance 0.190, naive rule 0.395, lift 4.25x
    - 30d: 1573 calls (52 a day), hit rate 0.833, chance 0.187, naive rule 0.391, lift 4.46x
  - next: threshold 0.4564, hit rate recent 0.4999 / long run 0.4686
    - 6h: 12 calls (49 a day), hit rate 0.500, chance 0.203, lift 2.47x
    - 24h: 72 calls (72 a day), hit rate 0.486, chance 0.197, lift 2.47x
    - 7d: 578 calls (83 a day), hit rate 0.448, chance 0.190, lift 2.35x
    - 30d: 2106 calls (70 a day), hit rate 0.489, chance 0.187, lift 2.62x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 429, 0.414; 0.35: 365, 0.469; 0.40: 295, 0.539; 0.45: 240, 0.599; 0.50: 186, 0.657; 0.55: 141, 0.703; 0.60: 109, 0.746; 0.65: 84, 0.791; 0.70: 62, 0.823; 0.75: 34, 0.862; 0.80: 9, 0.885
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 252, 0.424; 0.40: 165, 0.452; 0.45: 84, 0.475; 0.50: 20, 0.517; 0.55: 2, 0.548
- **K=8**: model 1791417600, labels learned 97801, probability skill vs chance 0.1995, widened contest next: True
  - now: threshold 0.5798, hit rate recent 0.5917 / long run 0.7009
    - 6h: 15 calls (62 a day), hit rate 0.400, chance 0.113, naive rule 0.293, lift 3.54x
    - 24h: 50 calls (50 a day), hit rate 0.580, chance 0.121, naive rule 0.342, lift 4.78x
    - 7d: 407 calls (58 a day), hit rate 0.688, chance 0.122, naive rule 0.328, lift 5.65x
    - 30d: 1581 calls (53 a day), hit rate 0.718, chance 0.121, naive rule 0.326, lift 5.92x
  - next: threshold 0.3677, hit rate recent 0.4365 / long run 0.3966
    - 6h: 14 calls (58 a day), hit rate 0.500, chance 0.113, lift 4.43x
    - 24h: 78 calls (79 a day), hit rate 0.436, chance 0.121, lift 3.59x
    - 7d: 619 calls (89 a day), hit rate 0.393, chance 0.122, lift 3.22x
    - 30d: 2116 calls (71 a day), hit rate 0.406, chance 0.121, lift 3.35x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 269, 0.404; 0.35: 203, 0.479; 0.40: 156, 0.540; 0.45: 123, 0.587; 0.50: 94, 0.630; 0.55: 67, 0.684; 0.60: 45, 0.725; 0.65: 24, 0.768; 0.70: 9, 0.821; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 184, 0.349; 0.35: 114, 0.389; 0.40: 48, 0.416; 0.45: 10, 0.437; 0.50: 1, 0.429
- **K=13**: model 1791504000, labels learned 97796, probability skill vs chance 0.1828, widened contest next: False
  - now: threshold 0.4285, hit rate recent 0.5886 / long run 0.5849
    - 6h: 11 calls (46 a day), hit rate 0.364, chance 0.086, naive rule 0.292, lift 4.25x
    - 24h: 49 calls (50 a day), hit rate 0.633, chance 0.075, naive rule 0.270, lift 8.43x
    - 7d: 387 calls (55 a day), hit rate 0.589, chance 0.078, naive rule 0.273, lift 7.55x
    - 30d: 1485 calls (50 a day), hit rate 0.587, chance 0.077, naive rule 0.268, lift 7.62x
  - next: threshold 0.2819, hit rate recent 0.3541 / long run 0.313
    - 6h: 21 calls (88 a day), hit rate 0.381, chance 0.086, lift 4.46x
    - 24h: 77 calls (78 a day), hit rate 0.351, chance 0.075, lift 4.67x
    - 7d: 540 calls (77 a day), hit rate 0.326, chance 0.078, lift 4.18x
    - 30d: 2044 calls (68 a day), hit rate 0.312, chance 0.077, lift 4.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 120, 0.442; 0.35: 87, 0.503; 0.40: 62, 0.554; 0.45: 43, 0.610; 0.50: 27, 0.630; 0.55: 15, 0.682; 0.60: 5, 0.711; 0.65: 1, 0.763
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 49, 0.323; 0.35: 15, 0.352; 0.40: 3, 0.348; 0.45: 0, 0.250

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 7.685 | 3.25% | 0.850 | 0.383 | 0.248 | 0.533 | 0.052 |
| 6h | 6.639 | 10.50% | 0.894 | 0.492 | 0.251 | 0.494 | 0.283 |
| 24h | 11.532 | 5.20% | 0.900 | 0.510 | 0.250 | 0.510 | 0.583 |
| 7d | 10.899 | 5.27% | 0.899 | 0.498 | 0.251 | 0.497 | 0.677 |
| 30d | 14.179 | 4.45% | 0.900 | 0.500 | 0.251 | 0.498 | 0.695 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 7.943 | 7.672 | 7.638 | 7.735 | 7.637 | 7.714 | 7.745 | 7.701 | 7.678 | 7.685 |
| 6h | 7.418 | 6.692 | 6.728 | 6.653 | 6.792 | 6.765 | 6.612 | 6.612 | 6.624 | 6.639 |
| 24h | 12.164 | 11.673 | 11.640 | 11.578 | 11.815 | 11.700 | 11.529 | 11.470 | 11.514 | 11.532 |
| 7d | 11.506 | 11.000 | 10.982 | 10.951 | 11.096 | 11.143 | 10.896 | 10.882 | 10.881 | 10.899 |
| 30d | 14.840 | 14.310 | 14.262 | 14.210 | 14.449 | 14.407 | 14.182 | 14.152 | 14.152 | 14.179 |

## Next candle

- candle starting 2026-10-10 02:12 UTC, last close 2493.81
- P(up) 0.5393, return quantiles (bp): {'05': -4.227, '10': -3.121, '25': -1.474, '40': -0.392, '50': 0.247, '60': 0.691, '75': 1.69, '90': 3.15, '95': 4.305}
- changepoint probability 0.0301, regime age 175.3 min
- agent weights: empirical 0.003, ewma 0.098, garch 0.105, har 0.163, bocpd 0.034, hmm 0.052, online_qr 0.234, lgbm 0.311

## Learning log

- 2026-10-08 00:00 UTC: {"garch": {"alpha": 0.0787, "beta": 0.9139}, "hmm": {"sd_bp": [1.75, 4.19, 12.48], "stay": [0.956, 0.949, 0.874]}, "lgbm": {"challenger_loss": 0.24893, "champion_loss": 0.24884, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4892, "challengers": 1, "chance_loss": 0.60681, "widened": false, "champion_loss": 0.48748, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38922, "challengers": 1, "chance_loss": 0.48475, "widened": false, "champion_loss": 0.38743, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27619, "challengers": 3, "chance_loss": 0.36379, "widened": true, "champion_loss": 0.27724, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19165, "challengers": 3, "chance_loss": 0.26169, "widened": true, "champion_loss": 0.1913, "promoted": false}}
- 2026-10-08 12:00 UTC: {"garch": {"alpha": 0.0757, "beta": 0.9148}, "hmm": {"sd_bp": [2.0, 4.45, 12.64], "stay": [0.96, 0.958, 0.863]}}
- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.35, 4.9, 15.58], current probabilities: [0.838, 0.161, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-10 02:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.539, 'l_abs': 0.745, 'l_hi': 0.747, 'l_lo': 0.705, 'b05': 0.696, 'b25': 0.662, 'b75': 0.658, 'b95': 0.658}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.5, 1.8], [1.4, 1.8], [1.5, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.426, 1.785, 1.945, 1.932, 2.252, 2.437, 2.509, 2.831, 3.05, 3.337, 3.355, 3.499, 3.496, 3.699]}
- calibration offsets (in sigma): {'05': 0.0455, '10': 0.051, '25': 0.0375, '40': 0.054, '50': 0.075, '60': 0.046, '75': 0.0425, '90': 0.019, '95': -0.0155}
