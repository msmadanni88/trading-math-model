# ETH-USD 60s candle generator - report

- generated: 2026-10-20 01:51 UTC
- last closed candle: 2026-10-20 01:51 UTC (staleness 0.6 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.604 (96) | 0.539 (672) [0.501, 0.576] | 0.525 (2876) [0.506, 0.545] | 0.514 (4602) [0.499, 0.529] | 0.520 (1630) [0.491, 0.548] | 0.286 (7) | 0.500 | flat +0.044 (noise 0.034) |
| colour_clear | 0.556 (806) | 0.548 (5555) [0.539, 0.557] | 0.524 (23366) [0.516, 0.533] | 0.514 (37413) [0.507, 0.520] | 0.545 (13175) [0.539, 0.550] | 0.618 (76) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.664 (152) | 0.602 (721) [0.575, 0.632] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.556 (18) | 0.500 | flat +0.013 (noise 0.026) |
| colour_next | 0.549 (1436) | 0.530 (10019) [0.521, 0.539] | 0.517 (42857) [0.511, 0.522] | 0.511 (68583) [0.506, 0.515] | 0.529 (24234) [0.523, 0.534] | 0.613 (111) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140266) [0.499, 0.505] | 0.501 (599998) [0.500, 0.502] | 0.501 (960162) [0.500, 0.502] | 0.500 (339276) [0.498, 0.503] | 0.487 (1554) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.615 (39) | 0.611 (162) [0.575, 0.662] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.800 (5) | 0.500 | flat -0.041 (noise 0.048) |
| reversal_k13_next | 0.313 (83) | 0.300 (443) [0.284, 0.315] | 0.308 (2089) [0.295, 0.321] | 0.306 (3301) [0.295, 0.318] | 0.318 (1196) [0.306, 0.330] | 0.250 (8) | 0.077 | flat -0.029 (noise 0.030) |
| reversal_k13_now | 0.474 (57) | 0.535 (383) [0.499, 0.575] | 0.577 (1552) [0.557, 0.599] | 0.575 (2406) [0.558, 0.591] | 0.565 (934) [0.539, 0.593] | 0.500 (6) | 0.077 | flat -0.033 (noise 0.036) |
| reversal_k3_next | 0.547 (117) | 0.561 (780) [0.551, 0.573] | 0.576 (2618) [0.563, 0.589] | 0.581 (4081) [0.571, 0.592] | 0.572 (1641) [0.559, 0.588] | 0.714 (7) | 0.292 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.911 (56) | 0.938 (371) [0.912, 0.963] | 0.935 (1706) [0.927, 0.944] | 0.937 (2737) [0.930, 0.944] | 0.928 (974) [0.917, 0.939] | 0.833 (6) | 0.293 | flat +0.021 (noise 0.018) |
| reversal_k5_next | 0.440 (141) | 0.453 (853) [0.434, 0.476] | 0.470 (2467) [0.455, 0.486] | 0.476 (3660) [0.464, 0.490] | 0.456 (1670) [0.440, 0.474] | 0.667 (6) | 0.187 | flat -0.015 (noise 0.029) |
| reversal_k5_now | 0.821 (56) | 0.818 (351) [0.793, 0.841] | 0.828 (1605) [0.814, 0.842] | 0.831 (2513) [0.819, 0.843] | 0.820 (902) [0.802, 0.837] | 0.833 (6) | 0.187 | flat +0.014 (noise 0.029) |
| reversal_k8_next | 0.333 (114) | 0.365 (702) [0.339, 0.390] | 0.393 (2286) [0.376, 0.410] | 0.390 (3661) [0.377, 0.402] | 0.381 (1555) [0.362, 0.399] | 0.286 (7) | 0.121 | flat -0.024 (noise 0.027) |
| reversal_k8_now | 0.580 (50) | 0.672 (329) [0.637, 0.704] | 0.710 (1566) [0.690, 0.730] | 0.705 (2500) [0.689, 0.721] | 0.689 (913) [0.663, 0.715] | 0.667 (6) | 0.122 | flat +0.006 (noise 0.035) |
| overall | 0.504 (22310) | 0.505 (155169) [0.502, 0.507] | 0.504 (661620) [0.502, 0.505] | 0.503 (1058206) [0.502, 0.504] | 0.504 (374925) [0.502, 0.506] | 0.497 (1724) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06508, 0.09756] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5295, 'levels': [{'threshold': 0.06508, 'calls_per_day': 144.6, 'win_rate': 0.5766}, {'threshold': 0.09756, 'calls_per_day': 35.9, 'win_rate': 0.6245}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 23207, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14917 | 0.336 | 0.523 (14670) | 0.591 (1441) | 0.767 (2456) |
| volatility: normal | 14917 | 0.363 | 0.517 (14853) | 0.618 (550) | 0.769 (2197) |
| volatility: wild | 14917 | 0.377 | 0.509 (14878) | 0.646 (229) | 0.777 (2021) |
| session: Asia 00-08 | 14991 | 0.357 | 0.522 (14891) | 0.611 (822) | 0.771 (2230) |
| session: Europe 08-13 | 9300 | 0.353 | 0.517 (9216) | 0.586 (555) | 0.775 (1453) |
| session: US 13-21 | 14880 | 0.367 | 0.512 (14777) | 0.591 (523) | 0.776 (2161) |
| session: late 21-24 | 5580 | 0.350 | 0.513 (5517) | 0.637 (320) | 0.748 (830) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.411 | 0.377 | 0.269 | 0.269 | 0.583 | 0.291 | 0.530 | 1.123 |
| 6h | 360 | 0.365 | 0.365 | 0.279 | 0.312 | 0.539 | 0.262 | 0.469 | 1.095 |
| 24h | 1440 | 0.373 | 0.367 | 0.276 | 0.311 | 0.554 | 0.270 | 0.476 | 1.164 |
| 7d | 10080 | 0.369 | 0.360 | 0.279 | 0.311 | 0.531 | 0.265 | 0.473 | 1.216 |
| 30d | 43200 | 0.359 | 0.355 | 0.279 | 0.308 | 0.517 | 0.253 | 0.466 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.411 / 0.583 / 0.900; 2: 0.391 / 0.567 / 0.883; 3: 0.382 / 0.517 / 0.900; 4: 0.367 / 0.483 / 0.883; 5: 0.371 / 0.467 / 0.817; 6: 0.376 / 0.517 / 0.850; 7: 0.356 / 0.500 / 0.833; 8: 0.367 / 0.517 / 0.833; 9: 0.378 / 0.600 / 0.833; 10: 0.368 / 0.550 / 0.833; 11: 0.352 / 0.500 / 0.817; 12: 0.360 / 0.583 / 0.850; 13: 0.337 / 0.433 / 0.850; 14: 0.336 / 0.417 / 0.833; 15: 0.351 / 0.500 / 0.833
- 6h: 1: 0.365 / 0.539 / 0.897; 2: 0.369 / 0.531 / 0.881; 3: 0.360 / 0.514 / 0.856; 4: 0.344 / 0.472 / 0.844; 5: 0.349 / 0.475 / 0.864; 6: 0.351 / 0.464 / 0.886; 7: 0.347 / 0.486 / 0.867; 8: 0.360 / 0.542 / 0.889; 9: 0.359 / 0.511 / 0.908; 10: 0.357 / 0.511 / 0.881; 11: 0.351 / 0.500 / 0.872; 12: 0.340 / 0.486 / 0.883; 13: 0.338 / 0.458 / 0.875; 14: 0.349 / 0.494 / 0.894; 15: 0.342 / 0.486 / 0.875
- 24h: 1: 0.373 / 0.554 / 0.904; 2: 0.362 / 0.499 / 0.892; 3: 0.361 / 0.505 / 0.894; 4: 0.351 / 0.478 / 0.893; 5: 0.356 / 0.497 / 0.892; 6: 0.358 / 0.498 / 0.895; 7: 0.350 / 0.483 / 0.894; 8: 0.360 / 0.513 / 0.895; 9: 0.358 / 0.506 / 0.899; 10: 0.361 / 0.522 / 0.899; 11: 0.356 / 0.506 / 0.897; 12: 0.357 / 0.515 / 0.898; 13: 0.350 / 0.480 / 0.899; 14: 0.360 / 0.513 / 0.897; 15: 0.350 / 0.492 / 0.901
- 7d: 1: 0.369 / 0.531 / 0.901; 2: 0.355 / 0.491 / 0.901; 3: 0.360 / 0.507 / 0.901; 4: 0.355 / 0.496 / 0.901; 5: 0.356 / 0.501 / 0.902; 6: 0.356 / 0.504 / 0.901; 7: 0.354 / 0.499 / 0.902; 8: 0.354 / 0.500 / 0.902; 9: 0.355 / 0.504 / 0.902; 10: 0.356 / 0.509 / 0.902; 11: 0.350 / 0.496 / 0.902; 12: 0.354 / 0.505 / 0.903; 13: 0.353 / 0.502 / 0.904; 14: 0.352 / 0.504 / 0.903; 15: 0.353 / 0.504 / 0.903
- 30d: 1: 0.359 / 0.517 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.349 / 0.497 / 0.900; 5: 0.350 / 0.503 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.502 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.349 / 0.506 / 0.900; 11: 0.346 / 0.500 / 0.900; 12: 0.348 / 0.504 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.346 / 0.498 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.106 (body 0.079, range 0.133); 'price stays where it was' would score 0.110; colour right 0.600; typical miss of the close 19.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.098 (body 0.063, range 0.133); 'price stays where it was' would score 0.113; colour right 0.542; typical miss of the close 8.7 bp; chain ended on the right side 0.667 of 24 chains; n=360
- 24h: match 0.120 (body 0.079, range 0.162); 'price stays where it was' would score 0.126; colour right 0.494; typical miss of the close 9.3 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.167); 'price stays where it was' would score 0.132; colour right 0.499; typical miss of the close 9.2 bp; chain ended on the right side 0.536 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.525 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.0; 2: 0.196 / 4.5; 3: 0.163 / 6.1; 4: 0.131 / 6.6; 5: 0.120 / 7.2; 6: 0.109 / 7.8; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.082 / 9.8; 12: 0.076 / 10.2; 13: 0.065 / 10.5; 14: 0.066 / 10.6; 15: 0.058 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 112185, probability skill vs chance 0.2178, widened contest next: False
  - now: threshold 0.8349, hit rate recent 0.9011 / long run 0.9297
    - 6h: 22 calls (89 a day), hit rate 0.864, chance 0.268, naive rule 0.460, lift 3.23x
    - 24h: 55 calls (55 a day), hit rate 0.891, chance 0.273, naive rule 0.457, lift 3.27x
    - 7d: 373 calls (53 a day), hit rate 0.936, chance 0.288, naive rule 0.478, lift 3.25x
    - 30d: 1708 calls (57 a day), hit rate 0.935, chance 0.291, naive rule 0.483, lift 3.21x
  - next: threshold 0.5329, hit rate recent 0.5874 / long run 0.5706
    - 6h: 26 calls (105 a day), hit rate 0.731, chance 0.268, lift 2.73x
    - 24h: 115 calls (115 a day), hit rate 0.548, chance 0.273, lift 2.01x
    - 7d: 772 calls (110 a day), hit rate 0.562, chance 0.288, lift 1.95x
    - 30d: 2618 calls (87 a day), hit rate 0.576, chance 0.291, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 483, 0.566; 0.45: 413, 0.635; 0.50: 361, 0.687; 0.55: 316, 0.729; 0.60: 269, 0.772; 0.65: 224, 0.801; 0.70: 179, 0.834; 0.75: 138, 0.870; 0.80: 94, 0.911; 0.85: 48, 0.950; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.424; 0.35: 499, 0.459; 0.40: 407, 0.490; 0.45: 311, 0.523; 0.50: 202, 0.555; 0.55: 91, 0.574; 0.60: 14, 0.606; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 112183, probability skill vs chance 0.209, widened contest next: False
  - now: threshold 0.6823, hit rate recent 0.8084 / long run 0.8235
    - 6h: 19 calls (78 a day), hit rate 0.789, chance 0.170, naive rule 0.360, lift 4.64x
    - 24h: 57 calls (57 a day), hit rate 0.825, chance 0.173, naive rule 0.368, lift 4.75x
    - 7d: 353 calls (50 a day), hit rate 0.816, chance 0.184, naive rule 0.394, lift 4.42x
    - 30d: 1606 calls (54 a day), hit rate 0.828, chance 0.187, naive rule 0.393, lift 4.43x
  - next: threshold 0.4036, hit rate recent 0.4672 / long run 0.4547
    - 6h: 22 calls (90 a day), hit rate 0.500, chance 0.170, lift 2.94x
    - 24h: 140 calls (141 a day), hit rate 0.450, chance 0.173, lift 2.59x
    - 7d: 854 calls (122 a day), hit rate 0.453, chance 0.184, lift 2.46x
    - 30d: 2464 calls (82 a day), hit rate 0.471, chance 0.187, lift 2.52x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.421; 0.35: 348, 0.487; 0.40: 280, 0.558; 0.45: 228, 0.614; 0.50: 180, 0.662; 0.55: 137, 0.707; 0.60: 107, 0.748; 0.65: 80, 0.789; 0.70: 58, 0.821; 0.75: 32, 0.866; 0.80: 10, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.418; 0.40: 158, 0.446; 0.45: 74, 0.460; 0.50: 18, 0.501; 0.55: 2, 0.549
- **K=8**: model 1792454400, labels learned 112180, probability skill vs chance 0.1849, widened contest next: True
  - now: threshold 0.57, hit rate recent 0.6247 / long run 0.6878
    - 6h: 20 calls (82 a day), hit rate 0.600, chance 0.103, naive rule 0.270, lift 5.83x
    - 24h: 52 calls (52 a day), hit rate 0.577, chance 0.113, naive rule 0.298, lift 5.11x
    - 7d: 332 calls (47 a day), hit rate 0.669, chance 0.118, naive rule 0.319, lift 5.65x
    - 30d: 1570 calls (52 a day), hit rate 0.710, chance 0.122, naive rule 0.328, lift 5.83x
  - next: threshold 0.3324, hit rate recent 0.3077 / long run 0.3702
    - 6h: 22 calls (91 a day), hit rate 0.273, chance 0.103, lift 2.65x
    - 24h: 114 calls (115 a day), hit rate 0.325, chance 0.113, lift 2.87x
    - 7d: 701 calls (100 a day), hit rate 0.359, chance 0.118, lift 3.04x
    - 30d: 2286 calls (76 a day), hit rate 0.392, chance 0.122, lift 3.22x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.420; 0.35: 194, 0.491; 0.40: 148, 0.548; 0.45: 116, 0.590; 0.50: 90, 0.630; 0.55: 65, 0.679; 0.60: 44, 0.725; 0.65: 24, 0.787; 0.70: 10, 0.835; 0.75: 1, 0.793
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.351; 0.35: 103, 0.382; 0.40: 41, 0.411; 0.45: 9, 0.438; 0.50: 1, 0.471
- **K=13**: model 1792454400, labels learned 112175, probability skill vs chance 0.179, widened contest next: True
  - now: threshold 0.4128, hit rate recent 0.4769 / long run 0.5559
    - 6h: 21 calls (88 a day), hit rate 0.429, chance 0.074, naive rule 0.228, lift 5.80x
    - 24h: 58 calls (59 a day), hit rate 0.466, chance 0.078, naive rule 0.271, lift 5.98x
    - 7d: 387 calls (55 a day), hit rate 0.532, chance 0.077, naive rule 0.273, lift 6.92x
    - 30d: 1556 calls (52 a day), hit rate 0.576, chance 0.078, naive rule 0.272, lift 7.40x
  - next: threshold 0.2766, hit rate recent 0.2983 / long run 0.3092
    - 6h: 22 calls (92 a day), hit rate 0.318, chance 0.074, lift 4.30x
    - 24h: 86 calls (87 a day), hit rate 0.314, chance 0.078, lift 4.03x
    - 7d: 444 calls (64 a day), hit rate 0.302, chance 0.077, lift 3.92x
    - 30d: 2093 calls (70 a day), hit rate 0.308, chance 0.078, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.450; 0.35: 86, 0.505; 0.40: 62, 0.555; 0.45: 42, 0.613; 0.50: 25, 0.657; 0.55: 14, 0.709; 0.60: 5, 0.747; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.321; 0.35: 13, 0.355; 0.40: 2, 0.419; 0.45: 0, 0.400

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 24.579 | 2.87% | 0.883 | 0.533 | 0.256 | 0.467 | 0.280 |
| 6h | 13.536 | 3.52% | 0.894 | 0.503 | 0.251 | 0.522 | 0.525 |
| 24h | 15.316 | 2.81% | 0.901 | 0.497 | 0.250 | 0.512 | 0.588 |
| 7d | 16.074 | 4.16% | 0.900 | 0.499 | 0.251 | 0.495 | 0.640 |
| 30d | 13.825 | 4.04% | 0.900 | 0.500 | 0.251 | 0.496 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 25.307 | 24.664 | 24.576 | 24.285 | 25.235 | 24.139 | 24.635 | 24.287 | 24.341 | 24.579 |
| 6h | 14.030 | 13.662 | 13.596 | 13.510 | 13.856 | 13.545 | 13.509 | 13.481 | 13.484 | 13.536 |
| 24h | 15.758 | 15.497 | 15.461 | 15.319 | 15.676 | 15.498 | 15.291 | 15.277 | 15.289 | 15.316 |
| 7d | 16.771 | 16.265 | 16.177 | 16.092 | 16.339 | 16.275 | 16.070 | 16.053 | 16.043 | 16.074 |
| 30d | 14.407 | 13.951 | 13.913 | 13.850 | 14.075 | 14.011 | 13.822 | 13.799 | 13.799 | 13.825 |

## Next candle

- candle starting 2026-10-20 01:51 UTC, last close 2397.85
- P(up) 0.4574, return quantiles (bp): {'05': -10.025, '10': -8.138, '25': -4.561, '40': -2.427, '50': -0.728, '60': 1.015, '75': 3.858, '90': 7.759, '95': 11.005}
- changepoint probability 0.0372, regime age 29.8 min
- agent weights: empirical 0.006, ewma 0.051, garch 0.077, har 0.238, bocpd 0.013, hmm 0.093, online_qr 0.234, lgbm 0.287

## Learning log

- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- HMM volatility states (sd, bp per minute): [3.17, 5.81, 15.74], current probabilities: [0.039, 0.945, 0.016]
- live generator: {'versions': 60, 'latest_effective': '2026-10-20 02:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.274, 'l_abs': 0.733, 'l_hi': 0.802, 'l_lo': 0.778, 'b05': 0.721, 'b25': 0.735, 'b75': 0.687, 'b95': 0.698}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.579, 2.016, 2.333, 2.666, 2.986, 3.232, 3.326, 3.396, 3.587, 4.083, 4.189, 4.369, 4.728, 4.618]}
- calibration offsets (in sigma): {'05': 0.085, '10': 0.02, '25': -0.025, '40': -0.06, '50': -0.05, '60': -0.02, '75': 0.005, '90': -0.01, '95': 0.005}
