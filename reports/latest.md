# ETH-USD 60s candle generator - report

- generated: 2026-11-12 16:21 UTC
- last closed candle: 2026-11-12 16:21 UTC (staleness 0.2 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.531 (672) [0.497, 0.561] | 0.519 (2880) [0.502, 0.537] | 0.514 (6810) [0.502, 0.526] | 0.516 (3838) [0.500, 0.532] | 0.508 (65) | 0.500 | up +0.061 (noise 0.027) |
| colour_clear | 0.517 (842) | 0.546 (5562) [0.533, 0.559] | 0.543 (23911) [0.536, 0.548] | 0.522 (55769) [0.517, 0.528] | 0.543 (31531) [0.538, 0.547] | 0.545 (539) | 0.500 | flat +0.019 (noise 0.011) |
| colour_confident | 0.507 (67) | 0.567 (947) [0.535, 0.591] | 0.587 (4269) [0.577, 0.598] | 0.592 (5750) [0.581, 0.602] | 0.592 (5750) [0.581, 0.602] | 0.600 (55) | 0.500 | flat -0.008 (noise 0.023) |
| colour_next | 0.507 (1439) | 0.531 (9972) [0.520, 0.544] | 0.530 (42869) [0.525, 0.534] | 0.517 (101433) [0.513, 0.521] | 0.529 (57084) [0.525, 0.533] | 0.538 (976) | 0.500 | flat +0.005 (noise 0.009) |
| colour_path | 0.508 (20146) | 0.502 (139608) [0.499, 0.505] | 0.502 (600166) [0.500, 0.503] | 0.501 (1420062) [0.500, 0.502] | 0.501 (799176) [0.500, 0.502] | 0.509 (13664) | 0.500 | flat +0.000 (noise 0.002) |
| colour_strong | 0.400 (5) | 0.628 (242) [0.588, 0.648] | 0.620 (1101) [0.604, 0.637] | 0.630 (1513) [0.614, 0.647] | 0.630 (1513) [0.614, 0.647] | 0.556 (9) | 0.500 | flat -0.003 (noise 0.046) |
| reversal_k13_next | 0.347 (72) | 0.332 (500) [0.309, 0.355] | 0.326 (1838) [0.312, 0.341] | 0.315 (4696) [0.304, 0.325] | 0.327 (2591) [0.315, 0.338] | 0.289 (45) | 0.077 | flat -0.023 (noise 0.033) |
| reversal_k13_now | 0.577 (52) | 0.577 (350) [0.551, 0.605] | 0.563 (1635) [0.543, 0.582] | 0.574 (3658) [0.561, 0.586] | 0.569 (2186) [0.551, 0.586] | 0.481 (27) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.694 (49) | 0.627 (362) [0.592, 0.659] | 0.591 (2801) [0.579, 0.604] | 0.588 (6102) [0.579, 0.597] | 0.589 (3662) [0.578, 0.600] | 0.542 (48) | 0.293 | flat +0.027 (noise 0.031) |
| reversal_k3_now | 0.912 (57) | 0.920 (412) [0.911, 0.930] | 0.933 (1716) [0.923, 0.944] | 0.935 (4082) [0.929, 0.941] | 0.930 (2319) [0.922, 0.938] | 0.932 (44) | 0.294 | flat -0.007 (noise 0.018) |
| reversal_k5_next | 0.404 (57) | 0.518 (398) [0.477, 0.550] | 0.486 (2650) [0.471, 0.503] | 0.485 (5457) [0.474, 0.496] | 0.480 (3467) [0.466, 0.495] | 0.413 (46) | 0.187 | flat -0.020 (noise 0.036) |
| reversal_k5_now | 0.667 (69) | 0.774 (389) [0.724, 0.821] | 0.808 (1643) [0.791, 0.821] | 0.822 (3805) [0.812, 0.832] | 0.811 (2194) [0.798, 0.824] | 0.676 (37) | 0.187 | flat -0.036 (noise 0.031) |
| reversal_k8_next | 0.429 (70) | 0.423 (466) [0.392, 0.452] | 0.397 (2613) [0.383, 0.411] | 0.396 (5572) [0.386, 0.407] | 0.396 (3466) [0.384, 0.408] | 0.396 (48) | 0.121 | flat -0.014 (noise 0.032) |
| reversal_k8_now | 0.661 (56) | 0.695 (367) [0.675, 0.716] | 0.686 (1524) [0.668, 0.704] | 0.700 (3695) [0.687, 0.713] | 0.690 (2108) [0.672, 0.706] | 0.586 (29) | 0.122 | flat -0.002 (noise 0.034) |
| overall | 0.510 (22163) | 0.506 (153496) [0.503, 0.509] | 0.505 (662335) [0.504, 0.507] | 0.504 (1565372) [0.503, 0.505] | 0.505 (882091) [0.504, 0.506] | 0.511 (15029) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07526, 0.1146] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5323, 'levels': [{'threshold': 0.07526, 'calls_per_day': 141.6, 'win_rate': 0.5798}, {'threshold': 0.1146, 'calls_per_day': 35.5, 'win_rate': 0.6335}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42866, 'rate': 0.53}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15207 | 0.346 | 0.533 (14968) | 0.568 (2276) | 0.732 (2568) |
| volatility: normal | 15207 | 0.370 | 0.530 (15142) | 0.607 (1347) | 0.752 (2246) |
| volatility: wild | 15207 | 0.386 | 0.526 (15169) | 0.610 (762) | 0.766 (2063) |
| session: Asia 00-08 | 15360 | 0.367 | 0.535 (15234) | 0.592 (1551) | 0.752 (2277) |
| session: Europe 08-13 | 9600 | 0.361 | 0.532 (9520) | 0.586 (1146) | 0.751 (1557) |
| session: US 13-21 | 15081 | 0.374 | 0.528 (14981) | 0.597 (1141) | 0.750 (2259) |
| session: late 21-24 | 5580 | 0.359 | 0.513 (5544) | 0.554 (547) | 0.730 (784) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.405 | 0.392 | 0.307 | 0.307 | 0.550 | 0.299 | 0.511 | 1.248 |
| 6h | 360 | 0.379 | 0.390 | 0.306 | 0.308 | 0.521 | 0.270 | 0.488 | 1.404 |
| 24h | 1440 | 0.379 | 0.379 | 0.298 | 0.326 | 0.531 | 0.274 | 0.483 | 1.125 |
| 7d | 10080 | 0.370 | 0.365 | 0.281 | 0.312 | 0.533 | 0.268 | 0.472 | 1.357 |
| 30d | 43200 | 0.367 | 0.360 | 0.279 | 0.310 | 0.530 | 0.264 | 0.470 | 1.254 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.405 / 0.550 / 0.917; 2: 0.379 / 0.483 / 0.850; 3: 0.399 / 0.583 / 0.817; 4: 0.377 / 0.517 / 0.917; 5: 0.400 / 0.550 / 0.933; 6: 0.380 / 0.500 / 0.917; 7: 0.400 / 0.517 / 0.900; 8: 0.380 / 0.500 / 0.883; 9: 0.394 / 0.483 / 0.917; 10: 0.406 / 0.517 / 0.917; 11: 0.380 / 0.483 / 0.817; 12: 0.386 / 0.500 / 0.833; 13: 0.394 / 0.550 / 0.833; 14: 0.401 / 0.583 / 0.850; 15: 0.393 / 0.533 / 0.833
- 6h: 1: 0.379 / 0.521 / 0.900; 2: 0.359 / 0.482 / 0.875; 3: 0.364 / 0.524 / 0.858; 4: 0.374 / 0.543 / 0.919; 5: 0.368 / 0.507 / 0.931; 6: 0.372 / 0.535 / 0.911; 7: 0.365 / 0.504 / 0.886; 8: 0.369 / 0.518 / 0.878; 9: 0.364 / 0.493 / 0.892; 10: 0.364 / 0.515 / 0.869; 11: 0.345 / 0.465 / 0.783; 12: 0.375 / 0.577 / 0.786; 13: 0.350 / 0.504 / 0.789; 14: 0.371 / 0.571 / 0.786; 15: 0.354 / 0.515 / 0.778
- 24h: 1: 0.379 / 0.531 / 0.903; 2: 0.355 / 0.472 / 0.899; 3: 0.370 / 0.514 / 0.896; 4: 0.370 / 0.523 / 0.913; 5: 0.362 / 0.484 / 0.915; 6: 0.368 / 0.514 / 0.912; 7: 0.370 / 0.520 / 0.904; 8: 0.367 / 0.509 / 0.901; 9: 0.365 / 0.504 / 0.904; 10: 0.362 / 0.491 / 0.900; 11: 0.363 / 0.514 / 0.875; 12: 0.366 / 0.514 / 0.874; 13: 0.367 / 0.521 / 0.878; 14: 0.362 / 0.515 / 0.878; 15: 0.364 / 0.506 / 0.878
- 7d: 1: 0.370 / 0.533 / 0.897; 2: 0.354 / 0.482 / 0.900; 3: 0.361 / 0.517 / 0.899; 4: 0.356 / 0.497 / 0.901; 5: 0.357 / 0.502 / 0.902; 6: 0.354 / 0.496 / 0.902; 7: 0.354 / 0.497 / 0.901; 8: 0.356 / 0.501 / 0.901; 9: 0.357 / 0.507 / 0.902; 10: 0.355 / 0.503 / 0.902; 11: 0.357 / 0.514 / 0.899; 12: 0.354 / 0.503 / 0.900; 13: 0.354 / 0.501 / 0.901; 14: 0.354 / 0.508 / 0.901; 15: 0.353 / 0.499 / 0.901
- 30d: 1: 0.367 / 0.530 / 0.897; 2: 0.354 / 0.493 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.354 / 0.499 / 0.900; 5: 0.354 / 0.504 / 0.900; 6: 0.352 / 0.501 / 0.900; 7: 0.353 / 0.499 / 0.900; 8: 0.353 / 0.504 / 0.900; 9: 0.353 / 0.504 / 0.900; 10: 0.353 / 0.503 / 0.900; 11: 0.351 / 0.502 / 0.899; 12: 0.352 / 0.503 / 0.899; 13: 0.351 / 0.500 / 0.899; 14: 0.351 / 0.502 / 0.899; 15: 0.351 / 0.502 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.130 (body 0.080, range 0.179); 'price stays where it was' would score 0.138; colour right 0.450; typical miss of the close 18.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.134 (body 0.093, range 0.175); 'price stays where it was' would score 0.124; colour right 0.476; typical miss of the close 15.3 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.132 (body 0.088, range 0.175); 'price stays where it was' would score 0.136; colour right 0.514; typical miss of the close 10.5 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.125 (body 0.083, range 0.166); 'price stays where it was' would score 0.125; colour right 0.505; typical miss of the close 8.8 bp; chain ended on the right side 0.530 of 672 chains; n=10080
- 30d: match 0.126 (body 0.085, range 0.166); 'price stays where it was' would score 0.130; colour right 0.502; typical miss of the close 8.9 bp; chain ended on the right side 0.520 of 2880 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 4.6; 2: 0.202 / 5.4; 3: 0.169 / 7.0; 4: 0.133 / 7.2; 5: 0.126 / 8.0; 6: 0.116 / 8.9; 7: 0.110 / 9.1; 8: 0.098 / 10.0; 9: 0.091 / 10.2; 10: 0.093 / 10.5; 11: 0.089 / 10.7; 12: 0.079 / 11.1; 13: 0.074 / 11.6; 14: 0.070 / 12.1; 15: 0.067 / 12.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 146175, probability skill vs chance 0.2241, widened contest next: False
  - now: threshold 0.84, hit rate recent 0.9135 / long run 0.9252
    - 6h: 17 calls (69 a day), hit rate 0.882, chance 0.306, naive rule 0.536, lift 2.89x
    - 24h: 61 calls (61 a day), hit rate 0.902, chance 0.298, naive rule 0.500, lift 3.03x
    - 7d: 419 calls (60 a day), hit rate 0.924, chance 0.298, naive rule 0.507, lift 3.09x
    - 30d: 1730 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.5675, hit rate recent 0.5951 / long run 0.6052
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.306, lift 2.38x
    - 24h: 69 calls (69 a day), hit rate 0.609, chance 0.298, lift 2.05x
    - 7d: 366 calls (52 a day), hit rate 0.607, chance 0.298, lift 2.03x
    - 30d: 2720 calls (91 a day), hit rate 0.593, chance 0.294, lift 2.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 563, 0.499; 0.35: 532, 0.524; 0.40: 474, 0.579; 0.45: 407, 0.649; 0.50: 357, 0.696; 0.55: 310, 0.739; 0.60: 261, 0.783; 0.65: 220, 0.810; 0.70: 173, 0.843; 0.75: 138, 0.874; 0.80: 92, 0.904; 0.85: 46, 0.944; 0.90: 4, 0.993
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 587, 0.431; 0.35: 497, 0.464; 0.40: 397, 0.502; 0.45: 298, 0.535; 0.50: 191, 0.567; 0.55: 86, 0.577; 0.60: 12, 0.648; 0.65: 1, 0.636
- **K=5**: model 1794441600, labels learned 146173, probability skill vs chance 0.2079, widened contest next: True
  - now: threshold 0.6872, hit rate recent 0.6902 / long run 0.7849
    - 6h: 16 calls (65 a day), hit rate 0.750, chance 0.181, naive rule 0.404, lift 4.14x
    - 24h: 55 calls (55 a day), hit rate 0.618, chance 0.186, naive rule 0.398, lift 3.32x
    - 7d: 394 calls (56 a day), hit rate 0.761, chance 0.187, naive rule 0.410, lift 4.07x
    - 30d: 1646 calls (55 a day), hit rate 0.804, chance 0.186, naive rule 0.405, lift 4.32x
  - next: threshold 0.4479, hit rate recent 0.4206 / long run 0.5027
    - 6h: 15 calls (61 a day), hit rate 0.400, chance 0.181, lift 2.21x
    - 24h: 65 calls (65 a day), hit rate 0.385, chance 0.186, lift 2.07x
    - 7d: 400 calls (57 a day), hit rate 0.497, chance 0.187, lift 2.66x
    - 30d: 2617 calls (87 a day), hit rate 0.485, chance 0.186, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.420; 0.35: 355, 0.480; 0.40: 287, 0.551; 0.45: 234, 0.605; 0.50: 187, 0.653; 0.55: 149, 0.690; 0.60: 112, 0.739; 0.65: 75, 0.775; 0.70: 47, 0.812; 0.75: 28, 0.847; 0.80: 10, 0.871
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 347, 0.382; 0.35: 256, 0.422; 0.40: 160, 0.457; 0.45: 65, 0.491; 0.50: 10, 0.518; 0.55: 1, 0.432
- **K=8**: model 1794182400, labels learned 146170, probability skill vs chance 0.1976, widened contest next: True
  - now: threshold 0.5677, hit rate recent 0.6464 / long run 0.6866
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.124, naive rule 0.333, lift 5.36x
    - 24h: 44 calls (44 a day), hit rate 0.568, chance 0.124, naive rule 0.340, lift 4.58x
    - 7d: 366 calls (52 a day), hit rate 0.686, chance 0.123, naive rule 0.343, lift 5.56x
    - 30d: 1522 calls (51 a day), hit rate 0.684, chance 0.121, naive rule 0.335, lift 5.67x
  - next: threshold 0.3622, hit rate recent 0.4041 / long run 0.4183
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.124, lift 3.45x
    - 24h: 69 calls (69 a day), hit rate 0.362, chance 0.124, lift 2.92x
    - 7d: 468 calls (67 a day), hit rate 0.412, chance 0.123, lift 3.35x
    - 30d: 2598 calls (87 a day), hit rate 0.396, chance 0.121, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 248, 0.427; 0.35: 193, 0.489; 0.40: 153, 0.533; 0.45: 118, 0.580; 0.50: 84, 0.634; 0.55: 59, 0.671; 0.60: 39, 0.710; 0.65: 23, 0.777; 0.70: 12, 0.814; 0.75: 2, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 170, 0.364; 0.35: 86, 0.391; 0.40: 23, 0.418; 0.45: 4, 0.421; 0.50: 1, 0.773
- **K=13**: model 1794355200, labels learned 146165, probability skill vs chance 0.1857, widened contest next: False
  - now: threshold 0.4488, hit rate recent 0.556 / long run 0.5693
    - 6h: 10 calls (42 a day), hit rate 0.600, chance 0.064, naive rule 0.273, lift 9.41x
    - 24h: 43 calls (43 a day), hit rate 0.465, chance 0.072, naive rule 0.271, lift 6.47x
    - 7d: 339 calls (49 a day), hit rate 0.578, chance 0.080, naive rule 0.295, lift 7.27x
    - 30d: 1631 calls (54 a day), hit rate 0.559, chance 0.078, naive rule 0.282, lift 7.20x
  - next: threshold 0.2959, hit rate recent 0.3118 / long run 0.3338
    - 6h: 13 calls (54 a day), hit rate 0.231, chance 0.064, lift 3.62x
    - 24h: 68 calls (69 a day), hit rate 0.265, chance 0.072, lift 3.68x
    - 7d: 499 calls (71 a day), hit rate 0.331, chance 0.080, lift 4.15x
    - 30d: 1824 calls (61 a day), hit rate 0.327, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 134, 0.429; 0.35: 97, 0.476; 0.40: 67, 0.534; 0.45: 46, 0.580; 0.50: 31, 0.638; 0.55: 20, 0.660; 0.60: 12, 0.689; 0.65: 3, 0.660; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.333; 0.35: 13, 0.332; 0.40: 3, 0.397; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 34.359 | 7.42% | 0.900 | 0.533 | 0.252 | 0.500 | 0.334 |
| 6h | 29.919 | 9.03% | 0.914 | 0.508 | 0.248 | 0.543 | 0.595 |
| 24h | 19.238 | 5.19% | 0.910 | 0.503 | 0.249 | 0.541 | 0.655 |
| 7d | 16.614 | 6.01% | 0.901 | 0.500 | 0.250 | 0.512 | 0.663 |
| 30d | 15.835 | 4.82% | 0.900 | 0.500 | 0.250 | 0.503 | 0.690 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 37.115 | 34.284 | 34.122 | 34.350 | 34.477 | 34.536 | 34.308 | 34.266 | 34.237 | 34.359 |
| 6h | 32.889 | 30.713 | 30.558 | 29.987 | 31.075 | 30.626 | 29.857 | 29.816 | 29.864 | 29.919 |
| 24h | 20.290 | 19.584 | 19.509 | 19.279 | 19.759 | 19.632 | 19.216 | 19.193 | 19.210 | 19.238 |
| 7d | 17.676 | 16.779 | 16.766 | 16.753 | 16.983 | 17.000 | 16.571 | 16.554 | 16.578 | 16.614 |
| 30d | 16.636 | 15.998 | 15.944 | 15.888 | 16.132 | 16.106 | 15.819 | 15.801 | 15.805 | 15.835 |

## Next candle

- candle starting 2026-11-12 16:21 UTC, last close 2015.15
- P(up) 0.4585, return quantiles (bp): {'05': -19.625, '10': -15.308, '25': -7.728, '40': -4.408, '50': -1.586, '60': 2.289, '75': 7.439, '90': 14.799, '95': 19.399}
- changepoint probability 0.0386, regime age 127.3 min
- agent weights: empirical 0.003, ewma 0.012, garch 0.020, har 0.185, bocpd 0.004, hmm 0.011, online_qr 0.352, lgbm 0.413

## Learning log

- 2026-11-10 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9328}, "hmm": {"sd_bp": [2.27, 5.7, 16.94], "stay": [0.987, 0.976, 0.948]}}
- 2026-11-11 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.933}, "hmm": {"sd_bp": [2.27, 5.87, 18.61], "stay": [0.986, 0.974, 0.949]}, "lgbm": {"challenger_loss": 0.244, "champion_loss": 0.244, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46792, "challengers": 3, "chance_loss": 0.5967, "widened": true, "champion_loss": 0.46772, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36456, "challengers": 1, "chance_loss": 0.47585, "widened": false, "champion_loss": 0.36241, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27127, "challengers": 1, "chance_loss": 0.37219, "widened": false, "champion_loss": 0.2703, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20458, "challengers": 1, "chance_loss": 0.28749, "widened": false, "champion_loss": 0.20483, "promoted": true}}
- 2026-11-11 12:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9329}, "hmm": {"sd_bp": [2.2, 5.74, 18.32], "stay": [0.986, 0.982, 0.953]}}
- 2026-11-12 00:00 UTC: {"garch": {"alpha": 0.0652, "beta": 0.9331}, "hmm": {"sd_bp": [2.15, 5.74, 18.21], "stay": [0.983, 0.982, 0.947]}, "lgbm": {"challenger_loss": 0.25402, "champion_loss": 0.25403, "promoted": true}, "reversal_k3": {"challenger_loss": 0.46372, "challengers": 1, "chance_loss": 0.59421, "widened": false, "champion_loss": 0.46111, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3576, "challengers": 3, "chance_loss": 0.47314, "widened": true, "champion_loss": 0.35795, "promoted": true}, "reversal_k8": {"challenger_loss": 0.27185, "challengers": 1, "chance_loss": 0.37476, "widened": false, "champion_loss": 0.27108, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20242, "challengers": 1, "chance_loss": 0.28746, "widened": false, "champion_loss": 0.20222, "promoted": false}}
- 2026-11-12 12:00 UTC: {"garch": {"alpha": 0.0653, "beta": 0.9304}, "hmm": {"sd_bp": [2.31, 5.8, 18.24], "stay": [0.968, 0.981, 0.945]}}
- HMM volatility states (sd, bp per minute): [2.31, 5.8, 18.24], current probabilities: [0.0, 0.237, 0.763]
- live generator: {'versions': 60, 'latest_effective': '2026-11-12 16:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.248, 'l_abs': 0.657, 'l_hi': 0.745, 'l_lo': 0.711, 'b05': 0.713, 'b25': 0.691, 'b75': 0.698, 'b95': 0.71}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.1, 'reach_scale': 1.4, 'ahead': [[1.3, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.5, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6]], 'cone_width': [1.676, 2.366, 1.872, 1.975, 2.349, 3.168, 3.393, 3.396, 3.886, 7.744, 8.105, 7.96, 8.113, 8.248]}
- calibration offsets (in sigma): {'05': 0.07, '10': 0.0, '25': 0.02, '40': -0.08, '50': -0.07, '60': -0.0, '75': 0.01, '90': -0.03, '95': -0.06}
