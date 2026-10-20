# ETH-USD 60s candle generator - report

- generated: 2026-10-20 06:52 UTC
- last closed candle: 2026-10-20 06:52 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=3: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.604 (96) | 0.539 (672) [0.501, 0.576] | 0.525 (2876) [0.506, 0.545] | 0.514 (4602) [0.499, 0.529] | 0.520 (1630) [0.491, 0.548] | 0.407 (27) | 0.500 | flat +0.044 (noise 0.034) |
| colour_clear | 0.556 (806) | 0.548 (5555) [0.539, 0.557] | 0.524 (23366) [0.516, 0.533] | 0.514 (37413) [0.507, 0.520] | 0.545 (13175) [0.539, 0.550] | 0.615 (247) | 0.500 | flat +0.011 (noise 0.009) |
| colour_confident | 0.664 (152) | 0.602 (721) [0.575, 0.632] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.604 (2202) [0.584, 0.625] | 0.614 (44) | 0.500 | flat +0.013 (noise 0.026) |
| colour_next | 0.549 (1436) | 0.530 (10019) [0.521, 0.539] | 0.517 (42857) [0.511, 0.522] | 0.511 (68583) [0.506, 0.515] | 0.529 (24234) [0.523, 0.534] | 0.575 (412) | 0.500 | flat +0.007 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.502 (140266) [0.499, 0.505] | 0.501 (599998) [0.500, 0.502] | 0.501 (960162) [0.500, 0.502] | 0.500 (339276) [0.498, 0.503] | 0.489 (5768) | 0.500 | flat +0.004 (noise 0.002) |
| colour_strong | 0.615 (39) | 0.611 (162) [0.575, 0.662] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.645 (574) [0.614, 0.675] | 0.769 (13) | 0.500 | flat -0.041 (noise 0.048) |
| reversal_k13_next | 0.313 (83) | 0.300 (443) [0.284, 0.315] | 0.308 (2089) [0.295, 0.321] | 0.306 (3301) [0.295, 0.318] | 0.318 (1196) [0.306, 0.330] | 0.368 (19) | 0.077 | flat -0.029 (noise 0.030) |
| reversal_k13_now | 0.474 (57) | 0.535 (383) [0.499, 0.575] | 0.577 (1552) [0.557, 0.599] | 0.575 (2406) [0.558, 0.591] | 0.565 (934) [0.539, 0.593] | 0.562 (16) | 0.077 | flat -0.033 (noise 0.036) |
| reversal_k3_next | 0.547 (117) | 0.561 (780) [0.551, 0.573] | 0.576 (2618) [0.563, 0.589] | 0.581 (4081) [0.571, 0.592] | 0.572 (1641) [0.559, 0.588] | 0.460 (37) | 0.292 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.911 (56) | 0.938 (371) [0.912, 0.963] | 0.935 (1706) [0.927, 0.944] | 0.937 (2737) [0.930, 0.944] | 0.928 (974) [0.917, 0.939] | 0.882 (17) | 0.293 | flat +0.021 (noise 0.018) |
| reversal_k5_next | 0.440 (141) | 0.453 (853) [0.434, 0.476] | 0.470 (2467) [0.455, 0.486] | 0.476 (3660) [0.464, 0.490] | 0.456 (1670) [0.440, 0.474] | 0.359 (39) | 0.187 | flat -0.015 (noise 0.029) |
| reversal_k5_now | 0.821 (56) | 0.818 (351) [0.793, 0.841] | 0.828 (1605) [0.814, 0.842] | 0.831 (2513) [0.819, 0.843] | 0.820 (902) [0.802, 0.837] | 0.812 (16) | 0.187 | flat +0.014 (noise 0.029) |
| reversal_k8_next | 0.333 (114) | 0.365 (702) [0.339, 0.390] | 0.393 (2286) [0.376, 0.410] | 0.390 (3661) [0.377, 0.402] | 0.381 (1555) [0.362, 0.399] | 0.278 (36) | 0.121 | flat -0.024 (noise 0.027) |
| reversal_k8_now | 0.580 (50) | 0.672 (329) [0.637, 0.704] | 0.710 (1566) [0.690, 0.730] | 0.705 (2500) [0.689, 0.721] | 0.689 (913) [0.663, 0.715] | 0.692 (13) | 0.122 | flat +0.006 (noise 0.035) |
| overall | 0.504 (22310) | 0.505 (155169) [0.502, 0.507] | 0.504 (661620) [0.502, 0.505] | 0.503 (1058206) [0.502, 0.504] | 0.504 (374925) [0.502, 0.506] | 0.494 (6400) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06546, 0.09794] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5312, 'levels': [{'threshold': 0.06546, 'calls_per_day': 146.9, 'win_rate': 0.5754}, {'threshold': 0.09794, 'calls_per_day': 36.4, 'win_rate': 0.6406}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 23508, 'rate': 0.5308}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15018 | 0.336 | 0.522 (14771) | 0.591 (1443) | 0.767 (2468) |
| volatility: normal | 15017 | 0.363 | 0.518 (14953) | 0.618 (568) | 0.768 (2216) |
| volatility: wild | 15017 | 0.378 | 0.509 (14978) | 0.651 (235) | 0.778 (2028) |
| session: Asia 00-08 | 15292 | 0.358 | 0.523 (15192) | 0.612 (848) | 0.771 (2268) |
| session: Europe 08-13 | 9300 | 0.353 | 0.517 (9216) | 0.586 (555) | 0.775 (1453) |
| session: US 13-21 | 14880 | 0.367 | 0.512 (14777) | 0.591 (523) | 0.776 (2161) |
| session: late 21-24 | 5580 | 0.350 | 0.513 (5517) | 0.637 (320) | 0.748 (830) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.373 | 0.362 | 0.276 | 0.276 | 0.567 | 0.262 | 0.485 | 1.208 |
| 6h | 360 | 0.387 | 0.365 | 0.261 | 0.314 | 0.567 | 0.286 | 0.489 | 1.113 |
| 24h | 1440 | 0.374 | 0.369 | 0.275 | 0.312 | 0.553 | 0.270 | 0.478 | 1.186 |
| 7d | 10080 | 0.369 | 0.359 | 0.279 | 0.312 | 0.532 | 0.265 | 0.473 | 1.205 |
| 30d | 43200 | 0.359 | 0.355 | 0.279 | 0.308 | 0.517 | 0.253 | 0.466 | 1.293 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.373 / 0.567 / 0.850; 2: 0.372 / 0.533 / 0.933; 3: 0.355 / 0.483 / 0.933; 4: 0.358 / 0.467 / 0.967; 5: 0.324 / 0.383 / 0.983; 6: 0.344 / 0.467 / 0.983; 7: 0.328 / 0.333 / 0.967; 8: 0.373 / 0.583 / 0.950; 9: 0.352 / 0.417 / 0.933; 10: 0.350 / 0.417 / 0.967; 11: 0.390 / 0.617 / 0.983; 12: 0.352 / 0.433 / 0.950; 13: 0.360 / 0.467 / 0.967; 14: 0.374 / 0.433 / 0.983; 15: 0.351 / 0.517 / 0.983
- 6h: 1: 0.387 / 0.567 / 0.894; 2: 0.362 / 0.500 / 0.942; 3: 0.358 / 0.481 / 0.942; 4: 0.359 / 0.497 / 0.956; 5: 0.352 / 0.447 / 0.947; 6: 0.354 / 0.483 / 0.956; 7: 0.351 / 0.467 / 0.956; 8: 0.354 / 0.492 / 0.953; 9: 0.365 / 0.511 / 0.950; 10: 0.364 / 0.517 / 0.950; 11: 0.364 / 0.514 / 0.956; 12: 0.376 / 0.561 / 0.956; 13: 0.367 / 0.514 / 0.961; 14: 0.360 / 0.469 / 0.961; 15: 0.343 / 0.461 / 0.953
- 24h: 1: 0.374 / 0.553 / 0.899; 2: 0.362 / 0.496 / 0.902; 3: 0.359 / 0.492 / 0.904; 4: 0.354 / 0.483 / 0.909; 5: 0.354 / 0.478 / 0.907; 6: 0.355 / 0.487 / 0.903; 7: 0.351 / 0.477 / 0.906; 8: 0.358 / 0.508 / 0.906; 9: 0.360 / 0.501 / 0.904; 10: 0.362 / 0.517 / 0.906; 11: 0.360 / 0.511 / 0.906; 12: 0.360 / 0.519 / 0.903; 13: 0.353 / 0.482 / 0.904; 14: 0.361 / 0.508 / 0.902; 15: 0.348 / 0.482 / 0.902
- 7d: 1: 0.369 / 0.532 / 0.899; 2: 0.355 / 0.490 / 0.900; 3: 0.359 / 0.504 / 0.901; 4: 0.355 / 0.497 / 0.901; 5: 0.355 / 0.499 / 0.901; 6: 0.355 / 0.502 / 0.901; 7: 0.353 / 0.498 / 0.902; 8: 0.354 / 0.500 / 0.901; 9: 0.355 / 0.504 / 0.901; 10: 0.356 / 0.508 / 0.901; 11: 0.350 / 0.496 / 0.902; 12: 0.354 / 0.506 / 0.902; 13: 0.353 / 0.503 / 0.903; 14: 0.352 / 0.502 / 0.903; 15: 0.352 / 0.502 / 0.902
- 30d: 1: 0.359 / 0.517 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.354 / 0.509 / 0.900; 4: 0.349 / 0.497 / 0.901; 5: 0.350 / 0.502 / 0.900; 6: 0.349 / 0.501 / 0.900; 7: 0.349 / 0.502 / 0.900; 8: 0.349 / 0.502 / 0.900; 9: 0.346 / 0.495 / 0.901; 10: 0.349 / 0.506 / 0.901; 11: 0.346 / 0.499 / 0.901; 12: 0.348 / 0.504 / 0.900; 13: 0.348 / 0.503 / 0.900; 14: 0.346 / 0.499 / 0.900; 15: 0.346 / 0.497 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.121 (body 0.073, range 0.168); 'price stays where it was' would score 0.095; colour right 0.533; typical miss of the close 7.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.109 (body 0.069, range 0.149); 'price stays where it was' would score 0.115; colour right 0.564; typical miss of the close 11.0 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.116 (body 0.076, range 0.157); 'price stays where it was' would score 0.124; colour right 0.510; typical miss of the close 10.2 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.126 (body 0.086, range 0.167); 'price stays where it was' would score 0.132; colour right 0.502; typical miss of the close 9.2 bp; chain ended on the right side 0.540 of 672 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.523 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.9; 2: 0.196 / 4.5; 3: 0.163 / 6.1; 4: 0.131 / 6.6; 5: 0.120 / 7.2; 6: 0.109 / 7.8; 7: 0.103 / 8.1; 8: 0.096 / 8.4; 9: 0.086 / 8.6; 10: 0.085 / 9.3; 11: 0.082 / 9.8; 12: 0.077 / 10.1; 13: 0.065 / 10.4; 14: 0.066 / 10.6; 15: 0.058 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 112486, probability skill vs chance 0.2182, widened contest next: True
  - now: threshold 0.8352, hit rate recent 0.9024 / long run 0.9294
    - 6h: 13 calls (53 a day), hit rate 0.923, chance 0.277, naive rule 0.459, lift 3.33x
    - 24h: 57 calls (57 a day), hit rate 0.877, chance 0.270, naive rule 0.455, lift 3.25x
    - 7d: 376 calls (54 a day), hit rate 0.934, chance 0.288, naive rule 0.478, lift 3.24x
    - 30d: 1707 calls (57 a day), hit rate 0.934, chance 0.291, naive rule 0.483, lift 3.21x
  - next: threshold 0.5329, hit rate recent 0.5126 / long run 0.5623
    - 6h: 34 calls (138 a day), hit rate 0.441, chance 0.277, lift 1.59x
    - 24h: 115 calls (115 a day), hit rate 0.522, chance 0.270, lift 1.93x
    - 7d: 775 calls (111 a day), hit rate 0.556, chance 0.288, lift 1.93x
    - 30d: 2630 calls (88 a day), hit rate 0.573, chance 0.291, lift 1.97x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 569, 0.490; 0.35: 540, 0.513; 0.40: 482, 0.566; 0.45: 413, 0.635; 0.50: 361, 0.687; 0.55: 316, 0.729; 0.60: 269, 0.773; 0.65: 224, 0.801; 0.70: 179, 0.834; 0.75: 138, 0.870; 0.80: 94, 0.911; 0.85: 48, 0.950; 0.90: 4, 0.982
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 585, 0.424; 0.35: 499, 0.460; 0.40: 407, 0.491; 0.45: 311, 0.522; 0.50: 202, 0.553; 0.55: 91, 0.570; 0.60: 14, 0.608; 0.65: 1, 0.690
- **K=5**: model 1791590400, labels learned 112484, probability skill vs chance 0.2115, widened contest next: True
  - now: threshold 0.6826, hit rate recent 0.8079 / long run 0.8231
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.178, naive rule 0.393, lift 4.67x
    - 24h: 54 calls (54 a day), hit rate 0.796, chance 0.174, naive rule 0.372, lift 4.58x
    - 7d: 352 calls (50 a day), hit rate 0.821, chance 0.185, naive rule 0.393, lift 4.45x
    - 30d: 1599 calls (53 a day), hit rate 0.827, chance 0.187, naive rule 0.393, lift 4.43x
  - next: threshold 0.4125, hit rate recent 0.3962 / long run 0.4466
    - 6h: 36 calls (147 a day), hit rate 0.333, chance 0.178, lift 1.87x
    - 24h: 142 calls (143 a day), hit rate 0.423, chance 0.174, lift 2.43x
    - 7d: 872 calls (125 a day), hit rate 0.447, chance 0.185, lift 2.42x
    - 30d: 2476 calls (83 a day), hit rate 0.469, chance 0.187, lift 2.51x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 420, 0.421; 0.35: 348, 0.487; 0.40: 280, 0.558; 0.45: 228, 0.614; 0.50: 180, 0.662; 0.55: 137, 0.707; 0.60: 107, 0.748; 0.65: 80, 0.790; 0.70: 58, 0.822; 0.75: 32, 0.866; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.387; 0.35: 250, 0.418; 0.40: 158, 0.444; 0.45: 73, 0.460; 0.50: 17, 0.500; 0.55: 2, 0.560
- **K=8**: model 1792454400, labels learned 112481, probability skill vs chance 0.1882, widened contest next: True
  - now: threshold 0.5696, hit rate recent 0.6343 / long run 0.6881
    - 6h: 9 calls (37 a day), hit rate 0.667, chance 0.111, naive rule 0.299, lift 5.98x
    - 24h: 51 calls (51 a day), hit rate 0.549, chance 0.111, naive rule 0.289, lift 4.94x
    - 7d: 328 calls (47 a day), hit rate 0.674, chance 0.119, naive rule 0.319, lift 5.68x
    - 30d: 1563 calls (52 a day), hit rate 0.709, chance 0.122, naive rule 0.328, lift 5.83x
  - next: threshold 0.3369, hit rate recent 0.2923 / long run 0.3657
    - 6h: 31 calls (128 a day), hit rate 0.290, chance 0.111, lift 2.61x
    - 24h: 120 calls (121 a day), hit rate 0.283, chance 0.111, lift 2.55x
    - 7d: 719 calls (103 a day), hit rate 0.357, chance 0.119, lift 3.01x
    - 30d: 2304 calls (77 a day), hit rate 0.391, chance 0.122, lift 3.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 256, 0.420; 0.35: 194, 0.490; 0.40: 148, 0.548; 0.45: 116, 0.590; 0.50: 89, 0.631; 0.55: 65, 0.680; 0.60: 43, 0.725; 0.65: 24, 0.787; 0.70: 10, 0.836; 0.75: 1, 0.793
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 177, 0.349; 0.35: 103, 0.380; 0.40: 41, 0.411; 0.45: 8, 0.438; 0.50: 1, 0.471
- **K=13**: model 1792454400, labels learned 112476, probability skill vs chance 0.1791, widened contest next: True
  - now: threshold 0.4127, hit rate recent 0.4936 / long run 0.5566
    - 6h: 12 calls (50 a day), hit rate 0.583, chance 0.065, naive rule 0.212, lift 8.94x
    - 24h: 60 calls (61 a day), hit rate 0.467, chance 0.072, naive rule 0.243, lift 6.46x
    - 7d: 385 calls (55 a day), hit rate 0.532, chance 0.077, naive rule 0.272, lift 6.92x
    - 30d: 1551 calls (52 a day), hit rate 0.576, chance 0.078, naive rule 0.272, lift 7.41x
  - next: threshold 0.2763, hit rate recent 0.3241 / long run 0.3118
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.065, lift 6.57x
    - 24h: 79 calls (80 a day), hit rate 0.304, chance 0.072, lift 4.20x
    - 7d: 441 calls (63 a day), hit rate 0.306, chance 0.077, lift 3.98x
    - 30d: 2093 calls (70 a day), hit rate 0.310, chance 0.078, lift 3.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.451; 0.35: 85, 0.506; 0.40: 61, 0.555; 0.45: 41, 0.613; 0.50: 25, 0.658; 0.55: 14, 0.711; 0.60: 5, 0.748; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.323; 0.35: 13, 0.359; 0.40: 2, 0.433

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 14.734 | -1.10% | 0.867 | 0.517 | 0.252 | 0.483 | 0.044 |
| 6h | 16.402 | 0.95% | 0.886 | 0.492 | 0.252 | 0.486 | 0.436 |
| 24h | 15.860 | 2.43% | 0.896 | 0.499 | 0.250 | 0.519 | 0.577 |
| 7d | 16.019 | 4.12% | 0.899 | 0.499 | 0.251 | 0.493 | 0.642 |
| 30d | 13.801 | 4.00% | 0.900 | 0.500 | 0.251 | 0.496 | 0.674 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 14.573 | 14.618 | 14.657 | 14.746 | 14.790 | 14.661 | 14.744 | 14.642 | 14.664 | 14.734 |
| 6h | 16.558 | 16.383 | 16.388 | 16.375 | 16.644 | 16.400 | 16.384 | 16.308 | 16.326 | 16.402 |
| 24h | 16.255 | 15.999 | 15.977 | 15.854 | 16.209 | 16.025 | 15.840 | 15.830 | 15.831 | 15.860 |
| 7d | 16.708 | 16.201 | 16.117 | 16.029 | 16.280 | 16.225 | 16.013 | 15.999 | 15.987 | 16.019 |
| 30d | 14.376 | 13.924 | 13.888 | 13.825 | 14.049 | 13.987 | 13.797 | 13.775 | 13.775 | 13.801 |

## Next candle

- candle starting 2026-10-20 06:52 UTC, last close 2396.03
- P(up) 0.482, return quantiles (bp): {'05': -7.769, '10': -6.029, '25': -3.231, '40': -1.268, '50': -0.239, '60': 1.109, '75': 3.382, '90': 6.342, '95': 8.468}
- changepoint probability 0.0435, regime age 158.4 min
- agent weights: empirical 0.021, ewma 0.098, garch 0.114, har 0.179, bocpd 0.022, hmm 0.088, online_qr 0.214, lgbm 0.263

## Learning log

- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- 2026-10-18 12:00 UTC: {"garch": {"alpha": 0.1271, "beta": 0.8608}, "hmm": {"sd_bp": [3.34, 6.61, 20.42], "stay": [0.987, 0.978, 0.944]}}
- 2026-10-19 00:00 UTC: {"garch": {"alpha": 0.0965, "beta": 0.8934}, "hmm": {"sd_bp": [3.31, 6.6, 20.94], "stay": [0.985, 0.977, 0.932]}, "lgbm": {"challenger_loss": 0.25518, "champion_loss": 0.25518, "promoted": false}, "reversal_k3": {"challenger_loss": 0.49245, "challengers": 1, "chance_loss": 0.61166, "widened": false, "champion_loss": 0.49037, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38763, "challengers": 1, "chance_loss": 0.49381, "widened": false, "champion_loss": 0.38605, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27859, "challengers": 1, "chance_loss": 0.3679, "widened": false, "champion_loss": 0.27798, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19505, "challengers": 3, "chance_loss": 0.26944, "widened": true, "champion_loss": 0.19472, "promoted": false}}
- 2026-10-19 12:00 UTC: {"garch": {"alpha": 0.0685, "beta": 0.9231}, "hmm": {"sd_bp": [3.26, 6.11, 16.29], "stay": [0.981, 0.973, 0.945]}}
- 2026-10-20 00:00 UTC: {"garch": {"alpha": 0.0524, "beta": 0.9418}, "hmm": {"sd_bp": [3.17, 5.81, 15.74], "stay": [0.981, 0.97, 0.909]}, "lgbm": {"challenger_loss": 0.24955, "champion_loss": 0.24958, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47852, "challengers": 1, "chance_loss": 0.59979, "widened": false, "champion_loss": 0.47659, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37017, "challengers": 1, "chance_loss": 0.47595, "widened": false, "champion_loss": 0.36775, "promoted": false}, "reversal_k8": {"challenger_loss": 0.2667, "challengers": 3, "chance_loss": 0.35488, "widened": true, "champion_loss": 0.26716, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19377, "challengers": 3, "chance_loss": 0.27008, "widened": true, "champion_loss": 0.19403, "promoted": true}}
- HMM volatility states (sd, bp per minute): [3.17, 5.81, 15.74], current probabilities: [0.079, 0.897, 0.025]
- live generator: {'versions': 60, 'latest_effective': '2026-10-20 07:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.246, 'l_abs': 0.746, 'l_hi': 0.814, 'l_lo': 0.785, 'b05': 0.724, 'b25': 0.725, 'b75': 0.714, 'b95': 0.709}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.144, 1.491, 1.53, 1.714, 1.881, 1.996, 2.095, 2.183, 2.305, 2.472, 2.639, 2.644, 2.805, 2.91]}
- calibration offsets (in sigma): {'05': 0.0455, '10': 0.001, '25': -0.0325, '40': -0.026, '50': -0.035, '60': -0.014, '75': 0.0425, '90': 0.009, '95': 0.0045}
