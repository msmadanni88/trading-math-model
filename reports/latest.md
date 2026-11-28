# ETH-USD 60s candle generator - report

- generated: 2026-11-28 10:57 UTC
- last closed candle: 2026-11-28 10:57 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.487 (671) [0.469, 0.507] | 0.507 (2878) [0.492, 0.522] | 0.514 (8344) [0.504, 0.524] | 0.515 (5372) [0.502, 0.529] | 0.558 (43) | 0.500 | flat -0.051 (noise 0.027) |
| colour_clear | 0.578 (770) | 0.559 (5422) [0.547, 0.573] | 0.545 (23728) [0.538, 0.552] | 0.528 (68471) [0.523, 0.533] | 0.546 (44233) [0.541, 0.550] | 0.554 (361) | 0.500 | flat +0.008 (noise 0.011) |
| colour_confident | 0.542 (155) | 0.568 (1411) [0.553, 0.582] | 0.566 (4515) [0.557, 0.576] | 0.583 (8417) [0.574, 0.592] | 0.583 (8417) [0.574, 0.592] | 0.568 (95) | 0.500 | flat +0.012 (noise 0.020) |
| colour_next | 0.553 (1435) | 0.541 (10040) [0.531, 0.550] | 0.533 (42909) [0.529, 0.538] | 0.520 (124392) [0.517, 0.524] | 0.531 (80043) [0.528, 0.535] | 0.527 (654) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.506 (20090) | 0.500 (140560) [0.498, 0.503] | 0.502 (600726) [0.501, 0.503] | 0.501 (1741488) [0.500, 0.502] | 0.501 (1120602) [0.500, 0.502] | 0.504 (9156) | 0.500 | flat -0.003 (noise 0.002) |
| colour_strong | 0.500 (44) | 0.545 (437) [0.496, 0.585] | 0.591 (1191) [0.567, 0.614] | 0.610 (2264) [0.592, 0.626] | 0.610 (2264) [0.592, 0.626] | 0.654 (26) | 0.500 | flat -0.067 (noise 0.037) |
| reversal_k13_next | 0.245 (53) | 0.352 (366) [0.303, 0.407] | 0.333 (1824) [0.316, 0.353] | 0.317 (5671) [0.307, 0.326] | 0.327 (3566) [0.316, 0.338] | 0.476 (21) | 0.078 | flat +0.042 (noise 0.039) |
| reversal_k13_now | 0.491 (59) | 0.599 (357) [0.544, 0.656] | 0.579 (1591) [0.557, 0.602] | 0.575 (4486) [0.563, 0.587] | 0.572 (3014) [0.557, 0.588] | 0.704 (27) | 0.078 | flat +0.023 (noise 0.048) |
| reversal_k3_next | 0.653 (98) | 0.609 (984) [0.583, 0.633] | 0.603 (2715) [0.590, 0.617] | 0.591 (7712) [0.583, 0.598] | 0.592 (5272) [0.582, 0.602] | 0.708 (48) | 0.295 | flat +0.031 (noise 0.027) |
| reversal_k3_now | 0.933 (60) | 0.934 (407) [0.922, 0.946] | 0.929 (1735) [0.922, 0.937] | 0.935 (4992) [0.930, 0.940] | 0.931 (3229) [0.925, 0.938] | 0.935 (31) | 0.294 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.400 (55) | 0.503 (382) [0.454, 0.560] | 0.506 (1702) [0.485, 0.529] | 0.486 (6385) [0.475, 0.497] | 0.482 (4395) [0.469, 0.496] | 0.576 (33) | 0.187 | flat +0.026 (noise 0.051) |
| reversal_k5_now | 0.769 (52) | 0.817 (427) [0.789, 0.847] | 0.794 (1789) [0.777, 0.810] | 0.817 (4795) [0.807, 0.826] | 0.806 (3184) [0.795, 0.817] | 0.864 (22) | 0.188 | flat +0.023 (noise 0.027) |
| reversal_k8_next | 0.348 (66) | 0.419 (527) [0.368, 0.471] | 0.418 (2143) [0.401, 0.438] | 0.398 (6761) [0.388, 0.408] | 0.399 (4655) [0.387, 0.411] | 0.500 (22) | 0.121 | flat +0.022 (noise 0.038) |
| reversal_k8_now | 0.576 (59) | 0.675 (409) [0.634, 0.714] | 0.680 (1668) [0.662, 0.698] | 0.694 (4627) [0.681, 0.706] | 0.683 (3040) [0.668, 0.697] | 0.846 (26) | 0.122 | flat -0.001 (noise 0.035) |
| overall | 0.510 (22123) | 0.506 (155130) [0.504, 0.507] | 0.506 (661680) [0.505, 0.507] | 0.504 (1919653) [0.504, 0.505] | 0.505 (1236372) [0.504, 0.506] | 0.510 (10083) | - | flat -0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08735, 0.1256] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5409, 'levels': [{'threshold': 0.08735, 'calls_per_day': 148.3, 'win_rate': 0.5672}, {'threshold': 0.1256, 'calls_per_day': 37.0, 'win_rate': 0.5577}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42911, 'rate': 0.5332}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15099 | 0.355 | 0.537 (14882) | 0.553 (2002) | 0.750 (2609) |
| volatility: normal | 15099 | 0.381 | 0.528 (15047) | 0.564 (1541) | 0.752 (2396) |
| volatility: wild | 15099 | 0.392 | 0.534 (15065) | 0.591 (1187) | 0.756 (2148) |
| session: Asia 00-08 | 15360 | 0.374 | 0.533 (15257) | 0.557 (1692) | 0.749 (2319) |
| session: Europe 08-13 | 9477 | 0.370 | 0.532 (9400) | 0.578 (1136) | 0.776 (1506) |
| session: US 13-21 | 14880 | 0.383 | 0.537 (14791) | 0.593 (1322) | 0.739 (2433) |
| session: late 21-24 | 5580 | 0.372 | 0.524 (5546) | 0.512 (580) | 0.760 (895) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.342 | 0.336 | 0.297 | 0.297 | 0.533 | 0.211 | 0.473 | 1.443 |
| 6h | 360 | 0.365 | 0.365 | 0.289 | 0.307 | 0.534 | 0.252 | 0.478 | 1.256 |
| 24h | 1440 | 0.383 | 0.367 | 0.283 | 0.313 | 0.544 | 0.276 | 0.490 | 1.127 |
| 7d | 10080 | 0.385 | 0.376 | 0.288 | 0.322 | 0.542 | 0.272 | 0.499 | 1.214 |
| 30d | 43200 | 0.376 | 0.369 | 0.288 | 0.320 | 0.533 | 0.268 | 0.485 | 1.264 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.342 / 0.533 / 0.817; 2: 0.319 / 0.383 / 0.717; 3: 0.333 / 0.533 / 0.833; 4: 0.331 / 0.517 / 0.717; 5: 0.329 / 0.550 / 0.783; 6: 0.325 / 0.583 / 0.850; 7: 0.348 / 0.567 / 0.950; 8: 0.343 / 0.567 / 0.950; 9: 0.357 / 0.600 / 1.000; 10: 0.337 / 0.517 / 1.000; 11: 0.348 / 0.533 / 0.983; 12: 0.320 / 0.517 / 1.000; 13: 0.335 / 0.433 / 0.983; 14: 0.332 / 0.483 / 1.000; 15: 0.335 / 0.450 / 0.983
- 6h: 1: 0.365 / 0.534 / 0.869; 2: 0.345 / 0.450 / 0.822; 3: 0.356 / 0.536 / 0.889; 4: 0.358 / 0.517 / 0.817; 5: 0.362 / 0.534 / 0.869; 6: 0.352 / 0.522 / 0.878; 7: 0.354 / 0.528 / 0.947; 8: 0.350 / 0.494 / 0.947; 9: 0.365 / 0.578 / 0.978; 10: 0.352 / 0.506 / 0.975; 11: 0.357 / 0.531 / 0.958; 12: 0.348 / 0.525 / 0.964; 13: 0.343 / 0.466 / 0.944; 14: 0.339 / 0.469 / 0.983; 15: 0.347 / 0.492 / 0.964
- 24h: 1: 0.383 / 0.544 / 0.895; 2: 0.360 / 0.494 / 0.876; 3: 0.364 / 0.519 / 0.883; 4: 0.365 / 0.516 / 0.882; 5: 0.370 / 0.525 / 0.883; 6: 0.356 / 0.496 / 0.890; 7: 0.363 / 0.528 / 0.895; 8: 0.357 / 0.500 / 0.891; 9: 0.361 / 0.517 / 0.899; 10: 0.354 / 0.486 / 0.901; 11: 0.356 / 0.488 / 0.899; 12: 0.353 / 0.488 / 0.899; 13: 0.361 / 0.507 / 0.901; 14: 0.351 / 0.482 / 0.890; 15: 0.354 / 0.491 / 0.896
- 7d: 1: 0.385 / 0.542 / 0.899; 2: 0.365 / 0.485 / 0.897; 3: 0.369 / 0.509 / 0.898; 4: 0.366 / 0.499 / 0.897; 5: 0.367 / 0.502 / 0.899; 6: 0.363 / 0.494 / 0.899; 7: 0.367 / 0.511 / 0.900; 8: 0.365 / 0.508 / 0.900; 9: 0.363 / 0.496 / 0.900; 10: 0.364 / 0.507 / 0.901; 11: 0.363 / 0.500 / 0.900; 12: 0.364 / 0.505 / 0.900; 13: 0.361 / 0.493 / 0.901; 14: 0.361 / 0.498 / 0.900; 15: 0.361 / 0.501 / 0.901
- 30d: 1: 0.376 / 0.533 / 0.898; 2: 0.362 / 0.490 / 0.899; 3: 0.366 / 0.512 / 0.900; 4: 0.362 / 0.498 / 0.900; 5: 0.363 / 0.505 / 0.900; 6: 0.360 / 0.500 / 0.900; 7: 0.362 / 0.503 / 0.900; 8: 0.361 / 0.506 / 0.900; 9: 0.360 / 0.500 / 0.900; 10: 0.360 / 0.503 / 0.901; 11: 0.360 / 0.505 / 0.900; 12: 0.360 / 0.503 / 0.900; 13: 0.359 / 0.500 / 0.900; 14: 0.358 / 0.500 / 0.900; 15: 0.358 / 0.501 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.105 (body 0.074, range 0.135); 'price stays where it was' would score 0.110; colour right 0.467; typical miss of the close 8.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.132 (body 0.093, range 0.171); 'price stays where it was' would score 0.155; colour right 0.545; typical miss of the close 8.7 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.130 (body 0.087, range 0.173); 'price stays where it was' would score 0.149; colour right 0.517; typical miss of the close 9.3 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.135 (body 0.088, range 0.182); 'price stays where it was' would score 0.146; colour right 0.497; typical miss of the close 11.6 bp; chain ended on the right side 0.495 of 671 chains; n=10080
- 30d: match 0.128 (body 0.085, range 0.171); 'price stays where it was' would score 0.132; colour right 0.503; typical miss of the close 11.1 bp; chain ended on the right side 0.509 of 2878 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.371 / 6.0; 2: 0.206 / 6.8; 3: 0.169 / 8.8; 4: 0.136 / 9.1; 5: 0.124 / 9.9; 6: 0.120 / 10.8; 7: 0.118 / 11.1; 8: 0.105 / 12.2; 9: 0.093 / 13.0; 10: 0.089 / 13.3; 11: 0.086 / 13.8; 12: 0.083 / 14.1; 13: 0.077 / 14.9; 14: 0.069 / 15.3; 15: 0.067 / 15.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 168891, probability skill vs chance 0.2381, widened contest next: False
  - now: threshold 0.8297, hit rate recent 0.9295 / long run 0.9314
    - 6h: 19 calls (77 a day), hit rate 0.895, chance 0.311, naive rule 0.544, lift 2.87x
    - 24h: 67 calls (67 a day), hit rate 0.925, chance 0.312, naive rule 0.542, lift 2.96x
    - 7d: 417 calls (60 a day), hit rate 0.935, chance 0.308, naive rule 0.533, lift 3.04x
    - 30d: 1737 calls (58 a day), hit rate 0.928, chance 0.296, naive rule 0.508, lift 3.13x
  - next: threshold 0.5507, hit rate recent 0.6642 / long run 0.6132
    - 6h: 34 calls (138 a day), hit rate 0.706, chance 0.311, lift 2.27x
    - 24h: 108 calls (108 a day), hit rate 0.657, chance 0.312, lift 2.11x
    - 7d: 961 calls (137 a day), hit rate 0.612, chance 0.308, lift 1.99x
    - 30d: 2700 calls (90 a day), hit rate 0.607, chance 0.296, lift 2.05x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 560, 0.506; 0.35: 531, 0.531; 0.40: 484, 0.573; 0.45: 422, 0.634; 0.50: 371, 0.682; 0.55: 324, 0.727; 0.60: 274, 0.770; 0.65: 229, 0.801; 0.70: 180, 0.831; 0.75: 144, 0.869; 0.80: 96, 0.900; 0.85: 41, 0.943; 0.90: 3, 0.944
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.437; 0.35: 487, 0.473; 0.40: 382, 0.515; 0.45: 289, 0.548; 0.50: 186, 0.578; 0.55: 78, 0.598; 0.60: 9, 0.644; 0.65: 0, 0.538
- **K=5**: model 1795824000, labels learned 168889, probability skill vs chance 0.2265, widened contest next: False
  - now: threshold 0.7053, hit rate recent 0.8105 / long run 0.8057
    - 6h: 11 calls (45 a day), hit rate 0.818, chance 0.211, naive rule 0.477, lift 3.88x
    - 24h: 49 calls (49 a day), hit rate 0.755, chance 0.203, naive rule 0.453, lift 3.72x
    - 7d: 427 calls (61 a day), hit rate 0.822, chance 0.197, naive rule 0.447, lift 4.17x
    - 30d: 1787 calls (60 a day), hit rate 0.794, chance 0.190, naive rule 0.420, lift 4.18x
  - next: threshold 0.445, hit rate recent 0.4985 / long run 0.495
    - 6h: 20 calls (82 a day), hit rate 0.600, chance 0.211, lift 2.84x
    - 24h: 64 calls (64 a day), hit rate 0.484, chance 0.203, lift 2.39x
    - 7d: 402 calls (57 a day), hit rate 0.502, chance 0.197, lift 2.55x
    - 30d: 1715 calls (57 a day), hit rate 0.508, chance 0.190, lift 2.68x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 421, 0.429; 0.35: 364, 0.478; 0.40: 296, 0.546; 0.45: 239, 0.605; 0.50: 186, 0.655; 0.55: 150, 0.686; 0.60: 117, 0.730; 0.65: 86, 0.765; 0.70: 55, 0.803; 0.75: 27, 0.841; 0.80: 5, 0.847
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 327, 0.399; 0.35: 243, 0.439; 0.40: 155, 0.464; 0.45: 63, 0.506; 0.50: 9, 0.566; 0.55: 1, 0.529
- **K=8**: model 1794960000, labels learned 168886, probability skill vs chance 0.2056, widened contest next: False
  - now: threshold 0.59, hit rate recent 0.7047 / long run 0.6834
    - 6h: 14 calls (58 a day), hit rate 0.929, chance 0.131, naive rule 0.440, lift 7.07x
    - 24h: 62 calls (62 a day), hit rate 0.645, chance 0.132, naive rule 0.392, lift 4.89x
    - 7d: 413 calls (59 a day), hit rate 0.688, chance 0.127, naive rule 0.376, lift 5.40x
    - 30d: 1670 calls (56 a day), hit rate 0.683, chance 0.124, naive rule 0.354, lift 5.50x
  - next: threshold 0.3668, hit rate recent 0.4122 / long run 0.41
    - 6h: 13 calls (53 a day), hit rate 0.615, chance 0.131, lift 4.68x
    - 24h: 61 calls (61 a day), hit rate 0.393, chance 0.132, lift 2.98x
    - 7d: 517 calls (74 a day), hit rate 0.416, chance 0.127, lift 3.27x
    - 30d: 2119 calls (71 a day), hit rate 0.422, chance 0.124, lift 3.40x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 261, 0.427; 0.35: 206, 0.486; 0.40: 161, 0.536; 0.45: 122, 0.577; 0.50: 88, 0.633; 0.55: 65, 0.670; 0.60: 44, 0.712; 0.65: 26, 0.773; 0.70: 9, 0.812; 0.75: 1, 0.742
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 155, 0.378; 0.35: 85, 0.409; 0.40: 31, 0.439; 0.45: 8, 0.469; 0.50: 1, 0.605; 0.55: 0, 0.200
- **K=13**: model 1795478400, labels learned 168881, probability skill vs chance 0.189, widened contest next: False
  - now: threshold 0.4574, hit rate recent 0.5963 / long run 0.5864
    - 6h: 14 calls (58 a day), hit rate 0.714, chance 0.087, naive rule 0.380, lift 8.21x
    - 24h: 62 calls (63 a day), hit rate 0.565, chance 0.081, naive rule 0.317, lift 7.00x
    - 7d: 360 calls (52 a day), hit rate 0.608, chance 0.084, naive rule 0.337, lift 7.25x
    - 30d: 1590 calls (53 a day), hit rate 0.584, chance 0.081, naive rule 0.304, lift 7.24x
  - next: threshold 0.2996, hit rate recent 0.3292 / long run 0.3336
    - 6h: 9 calls (38 a day), hit rate 0.778, chance 0.087, lift 8.94x
    - 24h: 51 calls (52 a day), hit rate 0.314, chance 0.081, lift 3.89x
    - 7d: 364 calls (52 a day), hit rate 0.357, chance 0.084, lift 4.26x
    - 30d: 1825 calls (61 a day), hit rate 0.337, chance 0.081, lift 4.18x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 145, 0.425; 0.35: 107, 0.473; 0.40: 73, 0.537; 0.45: 52, 0.585; 0.50: 36, 0.620; 0.55: 22, 0.645; 0.60: 10, 0.664; 0.65: 2, 0.527
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 56, 0.340; 0.35: 15, 0.379; 0.40: 2, 0.435

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 16.440 | -0.60% | 0.867 | 0.500 | 0.254 | 0.483 | 0.327 |
| 6h | 14.353 | 1.65% | 0.881 | 0.494 | 0.249 | 0.550 | 0.437 |
| 24h | 17.622 | 7.20% | 0.903 | 0.503 | 0.250 | 0.503 | 0.763 |
| 7d | 21.621 | 4.78% | 0.900 | 0.500 | 0.250 | 0.512 | 0.647 |
| 30d | 20.319 | 4.95% | 0.900 | 0.500 | 0.250 | 0.507 | 0.705 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 16.342 | 16.575 | 16.519 | 16.466 | 16.784 | 16.679 | 16.330 | 16.277 | 16.360 | 16.440 |
| 6h | 14.594 | 14.568 | 14.454 | 14.331 | 14.788 | 14.574 | 14.334 | 14.314 | 14.341 | 14.353 |
| 24h | 18.988 | 17.839 | 17.731 | 17.641 | 17.941 | 17.910 | 17.582 | 17.588 | 17.592 | 17.622 |
| 7d | 22.706 | 21.863 | 21.788 | 21.646 | 22.207 | 21.969 | 21.593 | 21.560 | 21.586 | 21.621 |
| 30d | 21.377 | 20.514 | 20.463 | 20.374 | 20.754 | 20.671 | 20.299 | 20.272 | 20.285 | 20.319 |

## Next candle

- candle starting 2026-11-28 10:57 UTC, last close 1644.39
- P(up) 0.5534, return quantiles (bp): {'05': -10.536, '10': -7.513, '25': -3.609, '40': -0.664, '50': 0.731, '60': 1.69, '75': 3.416, '90': 7.084, '95': 9.184}
- changepoint probability 0.5519, regime age 15.8 min
- agent weights: empirical 0.004, ewma 0.074, garch 0.109, har 0.214, bocpd 0.020, hmm 0.026, online_qr 0.260, lgbm 0.293

## Learning log

- 2026-11-26 00:00 UTC: {"garch": {"alpha": 0.0825, "beta": 0.9031}, "hmm": {"sd_bp": [4.93, 9.77, 29.75], "stay": [0.961, 0.952, 0.896]}, "lgbm": {"challenger_loss": 0.25027, "champion_loss": 0.25026, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4913, "challengers": 1, "chance_loss": 0.61261, "widened": false, "champion_loss": 0.48878, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3733, "challengers": 1, "chance_loss": 0.48537, "widened": false, "champion_loss": 0.37193, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27724, "challengers": 3, "chance_loss": 0.38432, "widened": true, "champion_loss": 0.27674, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20768, "challengers": 1, "chance_loss": 0.30017, "widened": false, "champion_loss": 0.20674, "promoted": false}}
- 2026-11-26 12:00 UTC: {"garch": {"alpha": 0.0874, "beta": 0.8951}, "hmm": {"sd_bp": [5.1, 9.79, 29.67], "stay": [0.964, 0.952, 0.897]}}
- 2026-11-27 00:00 UTC: {"garch": {"alpha": 0.086, "beta": 0.8972}, "hmm": {"sd_bp": [4.98, 9.67, 29.65], "stay": [0.967, 0.957, 0.909]}, "lgbm": {"challenger_loss": 0.24936, "champion_loss": 0.2495, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48669, "challengers": 1, "chance_loss": 0.61724, "widened": false, "champion_loss": 0.48438, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37811, "challengers": 1, "chance_loss": 0.49376, "widened": false, "champion_loss": 0.37659, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27446, "challengers": 1, "chance_loss": 0.3744, "widened": false, "champion_loss": 0.27383, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21177, "challengers": 1, "chance_loss": 0.29738, "widened": false, "champion_loss": 0.21069, "promoted": false}}
- 2026-11-27 12:00 UTC: {"garch": {"alpha": 0.0974, "beta": 0.8821}, "hmm": {"sd_bp": [5.02, 9.65, 29.47], "stay": [0.968, 0.955, 0.908]}}
- 2026-11-28 00:00 UTC: {"garch": {"alpha": 0.0767, "beta": 0.9088}, "hmm": {"sd_bp": [4.93, 9.34, 24.25], "stay": [0.971, 0.955, 0.925]}, "lgbm": {"challenger_loss": 0.24844, "champion_loss": 0.24848, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49387, "challengers": 1, "chance_loss": 0.6223, "widened": false, "champion_loss": 0.49186, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38744, "challengers": 3, "chance_loss": 0.50214, "widened": true, "champion_loss": 0.38761, "promoted": true}, "reversal_k8": {"challenger_loss": 0.28933, "challengers": 3, "chance_loss": 0.38088, "widened": true, "champion_loss": 0.2893, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20501, "challengers": 3, "chance_loss": 0.27801, "widened": true, "champion_loss": 0.20422, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.93, 9.34, 24.25], current probabilities: [0.545, 0.45, 0.005]
- live generator: {'versions': 60, 'latest_effective': '2026-11-28 11:05 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.48, 'l_abs': 0.714, 'l_hi': 0.761, 'l_lo': 0.744, 'b05': 0.712, 'b25': 0.644, 'b75': 0.653, 'b95': 0.694}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [2.191, 1.876, 2.816, 2.384, 2.368, 2.056, 2.247, 2.205, 2.107, 2.305, 2.364, 2.417, 3.07, 2.939]}
- calibration offsets (in sigma): {'05': -0.042, '10': -0.004, '25': 0.0, '40': 0.084, '50': 0.08, '60': 0.016, '75': -0.08, '90': -0.086, '95': -0.158}
