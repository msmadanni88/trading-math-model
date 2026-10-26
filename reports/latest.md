# ETH-USD 60s candle generator - report

- generated: 2026-10-26 10:22 UTC
- last closed candle: 2026-10-26 10:22 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.646 (96) | 0.548 (672) [0.509, 0.588] | 0.525 (2876) [0.506, 0.545] | 0.517 (5178) [0.503, 0.532] | 0.524 (2206) [0.501, 0.548] | 0.463 (41) | 0.500 | flat +0.021 (noise 0.030) |
| colour_clear | 0.534 (802) | 0.550 (5686) [0.543, 0.559] | 0.535 (23445) [0.527, 0.542] | 0.518 (42293) [0.511, 0.524] | 0.546 (18055) [0.541, 0.551] | 0.561 (358) | 0.500 | flat +0.005 (noise 0.009) |
| colour_confident | 0.578 (268) | 0.607 (1411) [0.590, 0.627] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.602 (3461) [0.588, 0.617] | 0.657 (67) | 0.500 | flat +0.023 (noise 0.024) |
| colour_next | 0.523 (1434) | 0.535 (10043) [0.528, 0.541] | 0.524 (42849) [0.520, 0.529] | 0.513 (77190) [0.509, 0.517] | 0.530 (32841) [0.525, 0.534] | 0.532 (617) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.506 (20076) | 0.501 (140602) [0.498, 0.503] | 0.501 (599886) [0.499, 0.502] | 0.501 (1080660) [0.500, 0.502] | 0.500 (459774) [0.499, 0.502] | 0.504 (8638) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.589 (107) | 0.628 (406) [0.603, 0.666] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.639 (941) [0.617, 0.663] | 0.692 (26) | 0.500 | flat +0.012 (noise 0.048) |
| reversal_k13_next | 0.364 (66) | 0.318 (466) [0.295, 0.338] | 0.304 (2171) [0.292, 0.315] | 0.307 (3684) [0.297, 0.318] | 0.318 (1579) [0.307, 0.329] | 0.280 (25) | 0.077 | flat +0.022 (noise 0.031) |
| reversal_k13_now | 0.600 (55) | 0.552 (357) [0.510, 0.599] | 0.569 (1575) [0.549, 0.590] | 0.574 (2706) [0.558, 0.590] | 0.566 (1234) [0.543, 0.590] | 0.517 (29) | 0.077 | flat +0.009 (noise 0.037) |
| reversal_k3_next | 0.588 (80) | 0.593 (678) [0.563, 0.626] | 0.580 (2811) [0.566, 0.594] | 0.584 (4642) [0.573, 0.595] | 0.580 (2202) [0.566, 0.595] | 0.614 (44) | 0.293 | flat +0.027 (noise 0.026) |
| reversal_k3_now | 0.870 (46) | 0.936 (388) [0.911, 0.958] | 0.935 (1685) [0.926, 0.945] | 0.937 (3069) [0.930, 0.944] | 0.931 (1306) [0.920, 0.942] | 1.000 (20) | 0.293 | flat -0.003 (noise 0.021) |
| reversal_k5_next | 0.496 (137) | 0.470 (924) [0.441, 0.494] | 0.464 (2951) [0.450, 0.478] | 0.476 (4443) [0.464, 0.489] | 0.462 (2453) [0.447, 0.477] | 0.531 (49) | 0.186 | flat +0.012 (noise 0.024) |
| reversal_k5_now | 0.837 (49) | 0.818 (363) [0.807, 0.829] | 0.831 (1563) [0.817, 0.844] | 0.830 (2820) [0.819, 0.841] | 0.820 (1209) [0.806, 0.833] | 0.952 (21) | 0.187 | flat +0.008 (noise 0.029) |
| reversal_k8_next | 0.403 (119) | 0.378 (759) [0.359, 0.396] | 0.382 (2589) [0.370, 0.395] | 0.389 (4306) [0.378, 0.401] | 0.382 (2200) [0.368, 0.396] | 0.364 (44) | 0.120 | flat +0.000 (noise 0.026) |
| reversal_k8_now | 0.729 (48) | 0.665 (337) [0.621, 0.710] | 0.698 (1525) [0.677, 0.718] | 0.702 (2787) [0.686, 0.717] | 0.687 (1200) [0.665, 0.710] | 0.632 (19) | 0.121 | flat -0.016 (noise 0.036) |
| overall | 0.509 (22206) | 0.504 (155589) [0.502, 0.507] | 0.504 (662481) [0.503, 0.506] | 0.503 (1191485) [0.502, 0.504] | 0.504 (508204) [0.502, 0.506] | 0.508 (9547) | - | flat -0.000 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07786, 0.1158] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5332, 'levels': [{'threshold': 0.07786, 'calls_per_day': 148.8, 'win_rate': 0.6172}, {'threshold': 0.1158, 'calls_per_day': 37.6, 'win_rate': 0.6629}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 32319, 'rate': 0.5306}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15088 | 0.336 | 0.523 (14842) | 0.588 (1726) | 0.764 (2495) |
| volatility: normal | 15087 | 0.365 | 0.524 (15017) | 0.609 (1213) | 0.752 (2230) |
| volatility: wild | 15087 | 0.379 | 0.520 (15045) | 0.638 (589) | 0.775 (1896) |
| session: Asia 00-08 | 15360 | 0.358 | 0.529 (15254) | 0.608 (1272) | 0.765 (2214) |
| session: Europe 08-13 | 9442 | 0.355 | 0.524 (9354) | 0.600 (873) | 0.759 (1488) |
| session: US 13-21 | 14880 | 0.367 | 0.519 (14778) | 0.599 (867) | 0.775 (2095) |
| session: late 21-24 | 5580 | 0.351 | 0.513 (5518) | 0.607 (516) | 0.740 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.347 | 0.320 | 0.310 | 0.310 | 0.417 | 0.219 | 0.475 | 1.773 |
| 6h | 360 | 0.387 | 0.364 | 0.305 | 0.344 | 0.546 | 0.280 | 0.494 | 1.287 |
| 24h | 1440 | 0.365 | 0.356 | 0.284 | 0.317 | 0.527 | 0.264 | 0.467 | 1.176 |
| 7d | 10080 | 0.370 | 0.360 | 0.276 | 0.309 | 0.532 | 0.268 | 0.472 | 1.216 |
| 30d | 43200 | 0.360 | 0.353 | 0.276 | 0.305 | 0.524 | 0.257 | 0.463 | 1.283 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.347 / 0.417 / 0.950; 2: 0.361 / 0.550 / 0.967; 3: 0.353 / 0.583 / 0.967; 4: 0.327 / 0.433 / 0.950; 5: 0.347 / 0.500 / 0.950; 6: 0.337 / 0.533 / 0.933; 7: 0.338 / 0.483 / 0.917; 8: 0.295 / 0.383 / 0.900; 9: 0.341 / 0.550 / 0.900; 10: 0.338 / 0.517 / 0.883; 11: 0.331 / 0.500 / 0.883; 12: 0.335 / 0.550 / 0.917; 13: 0.347 / 0.500 / 0.917; 14: 0.356 / 0.617 / 0.883; 15: 0.306 / 0.467 / 0.883
- 6h: 1: 0.387 / 0.546 / 0.908; 2: 0.362 / 0.465 / 0.881; 3: 0.364 / 0.546 / 0.881; 4: 0.343 / 0.448 / 0.861; 5: 0.367 / 0.535 / 0.900; 6: 0.349 / 0.490 / 0.881; 7: 0.361 / 0.513 / 0.853; 8: 0.353 / 0.479 / 0.853; 9: 0.358 / 0.501 / 0.844; 10: 0.369 / 0.543 / 0.828; 11: 0.359 / 0.501 / 0.822; 12: 0.358 / 0.515 / 0.844; 13: 0.352 / 0.473 / 0.822; 14: 0.360 / 0.524 / 0.814; 15: 0.355 / 0.501 / 0.831
- 24h: 1: 0.365 / 0.527 / 0.892; 2: 0.350 / 0.483 / 0.901; 3: 0.355 / 0.524 / 0.901; 4: 0.348 / 0.502 / 0.899; 5: 0.348 / 0.492 / 0.906; 6: 0.350 / 0.521 / 0.902; 7: 0.348 / 0.508 / 0.897; 8: 0.350 / 0.519 / 0.897; 9: 0.350 / 0.505 / 0.899; 10: 0.351 / 0.519 / 0.894; 11: 0.351 / 0.519 / 0.892; 12: 0.346 / 0.513 / 0.895; 13: 0.348 / 0.512 / 0.891; 14: 0.340 / 0.490 / 0.887; 15: 0.343 / 0.493 / 0.892
- 7d: 1: 0.370 / 0.532 / 0.898; 2: 0.358 / 0.502 / 0.900; 3: 0.358 / 0.510 / 0.900; 4: 0.353 / 0.496 / 0.900; 5: 0.354 / 0.500 / 0.901; 6: 0.352 / 0.496 / 0.901; 7: 0.352 / 0.497 / 0.900; 8: 0.355 / 0.511 / 0.900; 9: 0.352 / 0.496 / 0.900; 10: 0.353 / 0.507 / 0.899; 11: 0.351 / 0.500 / 0.899; 12: 0.352 / 0.503 / 0.900; 13: 0.349 / 0.495 / 0.900; 14: 0.350 / 0.496 / 0.900; 15: 0.349 / 0.499 / 0.900
- 30d: 1: 0.360 / 0.524 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.510 / 0.900; 4: 0.348 / 0.497 / 0.900; 5: 0.348 / 0.503 / 0.900; 6: 0.347 / 0.499 / 0.900; 7: 0.347 / 0.500 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.496 / 0.900; 10: 0.347 / 0.506 / 0.900; 11: 0.344 / 0.499 / 0.900; 12: 0.346 / 0.504 / 0.900; 13: 0.345 / 0.502 / 0.900; 14: 0.344 / 0.499 / 0.900; 15: 0.345 / 0.500 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.102 (body 0.081, range 0.123); 'price stays where it was' would score 0.135; colour right 0.433; typical miss of the close 9.7 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.132 (body 0.090, range 0.175); 'price stays where it was' would score 0.154; colour right 0.487; typical miss of the close 9.7 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.122 (body 0.082, range 0.162); 'price stays where it was' would score 0.129; colour right 0.494; typical miss of the close 9.4 bp; chain ended on the right side 0.573 of 96 chains; n=1440
- 7d: match 0.128 (body 0.087, range 0.168); 'price stays where it was' would score 0.134; colour right 0.501; typical miss of the close 8.9 bp; chain ended on the right side 0.546 of 672 chains; n=10080
- 30d: match 0.122 (body 0.083, range 0.161); 'price stays where it was' would score 0.126; colour right 0.499; typical miss of the close 7.6 bp; chain ended on the right side 0.523 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 3.9; 2: 0.195 / 4.4; 3: 0.168 / 5.9; 4: 0.131 / 6.5; 5: 0.123 / 7.1; 6: 0.112 / 7.6; 7: 0.106 / 7.9; 8: 0.097 / 8.3; 9: 0.087 / 8.3; 10: 0.088 / 9.0; 11: 0.084 / 9.5; 12: 0.076 / 9.8; 13: 0.068 / 9.9; 14: 0.069 / 10.4; 15: 0.060 / 10.7

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 121336, probability skill vs chance 0.2352, widened contest next: False
  - now: threshold 0.834, hit rate recent 0.9351 / long run 0.9361
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.306, naive rule 0.513, lift 3.27x
    - 24h: 45 calls (45 a day), hit rate 0.933, chance 0.291, naive rule 0.491, lift 3.20x
    - 7d: 387 calls (55 a day), hit rate 0.935, chance 0.296, naive rule 0.501, lift 3.16x
    - 30d: 1689 calls (56 a day), hit rate 0.935, chance 0.294, naive rule 0.492, lift 3.18x
  - next: threshold 0.5318, hit rate recent 0.5951 / long run 0.592
    - 6h: 26 calls (105 a day), hit rate 0.615, chance 0.306, lift 2.01x
    - 24h: 99 calls (99 a day), hit rate 0.566, chance 0.291, lift 1.94x
    - 7d: 667 calls (95 a day), hit rate 0.600, chance 0.296, lift 2.03x
    - 30d: 2827 calls (94 a day), hit rate 0.582, chance 0.294, lift 1.98x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.495; 0.35: 538, 0.520; 0.40: 478, 0.576; 0.45: 408, 0.647; 0.50: 356, 0.699; 0.55: 311, 0.741; 0.60: 263, 0.785; 0.65: 220, 0.811; 0.70: 174, 0.843; 0.75: 135, 0.875; 0.80: 91, 0.914; 0.85: 46, 0.951; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 589, 0.426; 0.35: 502, 0.464; 0.40: 408, 0.499; 0.45: 310, 0.534; 0.50: 201, 0.570; 0.55: 90, 0.575; 0.60: 14, 0.627; 0.65: 1, 0.677
- **K=5**: model 1792540800, labels learned 121334, probability skill vs chance 0.2261, widened contest next: False
  - now: threshold 0.6727, hit rate recent 0.8576 / long run 0.8255
    - 6h: 14 calls (57 a day), hit rate 0.929, chance 0.203, naive rule 0.434, lift 4.58x
    - 24h: 49 calls (49 a day), hit rate 0.918, chance 0.177, naive rule 0.380, lift 5.20x
    - 7d: 361 calls (52 a day), hit rate 0.823, chance 0.183, naive rule 0.403, lift 4.49x
    - 30d: 1565 calls (52 a day), hit rate 0.831, chance 0.187, naive rule 0.400, lift 4.44x
  - next: threshold 0.4198, hit rate recent 0.5155 / long run 0.4795
    - 6h: 28 calls (114 a day), hit rate 0.607, chance 0.203, lift 3.00x
    - 24h: 124 calls (125 a day), hit rate 0.484, chance 0.177, lift 2.74x
    - 7d: 911 calls (130 a day), hit rate 0.476, chance 0.183, lift 2.60x
    - 30d: 2989 calls (100 a day), hit rate 0.464, chance 0.187, lift 2.48x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 416, 0.426; 0.35: 344, 0.493; 0.40: 276, 0.565; 0.45: 224, 0.620; 0.50: 176, 0.670; 0.55: 136, 0.711; 0.60: 105, 0.755; 0.65: 75, 0.792; 0.70: 52, 0.832; 0.75: 30, 0.878; 0.80: 10, 0.900
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.389; 0.35: 252, 0.421; 0.40: 158, 0.453; 0.45: 70, 0.463; 0.50: 15, 0.486; 0.55: 1, 0.528
- **K=8**: model 1792800000, labels learned 121331, probability skill vs chance 0.2071, widened contest next: False
  - now: threshold 0.5562, hit rate recent 0.6758 / long run 0.6837
    - 6h: 11 calls (45 a day), hit rate 0.545, chance 0.116, naive rule 0.328, lift 4.71x
    - 24h: 44 calls (44 a day), hit rate 0.705, chance 0.120, naive rule 0.321, lift 5.89x
    - 7d: 340 calls (49 a day), hit rate 0.662, chance 0.116, naive rule 0.321, lift 5.71x
    - 30d: 1523 calls (51 a day), hit rate 0.693, chance 0.121, naive rule 0.329, lift 5.75x
  - next: threshold 0.336, hit rate recent 0.3717 / long run 0.3816
    - 6h: 28 calls (115 a day), hit rate 0.321, chance 0.116, lift 2.78x
    - 24h: 109 calls (110 a day), hit rate 0.376, chance 0.120, lift 3.15x
    - 7d: 754 calls (108 a day), hit rate 0.377, chance 0.116, lift 3.25x
    - 30d: 2611 calls (87 a day), hit rate 0.381, chance 0.121, lift 3.16x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 247, 0.427; 0.35: 188, 0.496; 0.40: 144, 0.549; 0.45: 110, 0.594; 0.50: 84, 0.634; 0.55: 61, 0.672; 0.60: 40, 0.719; 0.65: 23, 0.788; 0.70: 10, 0.829; 0.75: 1, 0.814
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 174, 0.352; 0.35: 96, 0.378; 0.40: 35, 0.397; 0.45: 8, 0.418; 0.50: 1, 0.581
- **K=13**: model 1792800000, labels learned 121326, probability skill vs chance 0.1864, widened contest next: False
  - now: threshold 0.4044, hit rate recent 0.5612 / long run 0.5597
    - 6h: 16 calls (67 a day), hit rate 0.438, chance 0.083, naive rule 0.293, lift 5.30x
    - 24h: 59 calls (60 a day), hit rate 0.593, chance 0.077, naive rule 0.265, lift 7.68x
    - 7d: 369 calls (53 a day), hit rate 0.547, chance 0.074, naive rule 0.267, lift 7.42x
    - 30d: 1584 calls (53 a day), hit rate 0.566, chance 0.077, naive rule 0.272, lift 7.33x
  - next: threshold 0.2943, hit rate recent 0.3136 / long run 0.3123
    - 6h: 14 calls (58 a day), hit rate 0.286, chance 0.083, lift 3.46x
    - 24h: 60 calls (61 a day), hit rate 0.300, chance 0.077, lift 3.89x
    - 7d: 455 calls (65 a day), hit rate 0.316, chance 0.074, lift 4.29x
    - 30d: 2167 calls (72 a day), hit rate 0.305, chance 0.077, lift 3.95x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 122, 0.444; 0.35: 88, 0.495; 0.40: 62, 0.550; 0.45: 41, 0.603; 0.50: 26, 0.661; 0.55: 15, 0.705; 0.60: 7, 0.746; 0.65: 2, 0.811
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.314; 0.35: 14, 0.343; 0.40: 2, 0.422; 0.45: 0, 0.500

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 11.220 | 3.98% | 0.967 | 0.600 | 0.254 | 0.400 | 0.520 |
| 6h | 16.011 | 1.29% | 0.908 | 0.525 | 0.251 | 0.493 | 0.383 |
| 24h | 16.253 | 4.48% | 0.892 | 0.503 | 0.250 | 0.508 | 0.641 |
| 7d | 15.276 | 3.54% | 0.899 | 0.500 | 0.250 | 0.502 | 0.655 |
| 30d | 13.499 | 4.16% | 0.900 | 0.500 | 0.251 | 0.496 | 0.670 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 11.685 | 11.694 | 11.171 | 11.009 | 11.953 | 11.307 | 11.085 | 11.228 | 11.114 | 11.220 |
| 6h | 16.221 | 16.178 | 16.087 | 16.009 | 16.380 | 16.114 | 15.916 | 15.956 | 15.942 | 16.011 |
| 24h | 17.014 | 16.430 | 16.437 | 16.280 | 16.639 | 16.516 | 16.218 | 16.204 | 16.213 | 16.253 |
| 7d | 15.836 | 15.426 | 15.367 | 15.291 | 15.562 | 15.440 | 15.261 | 15.239 | 15.247 | 15.276 |
| 30d | 14.085 | 13.631 | 13.584 | 13.523 | 13.744 | 13.687 | 13.494 | 13.475 | 13.474 | 13.499 |

## Next candle

- candle starting 2026-10-26 10:22 UTC, last close 2326.2
- P(up) 0.5069, return quantiles (bp): {'05': -6.594, '10': -4.982, '25': -2.552, '40': -0.929, '50': 0.071, '60': 0.92, '75': 2.499, '90': 5.379, '95': 7.354}
- changepoint probability 0.0373, regime age 44.6 min
- agent weights: empirical 0.003, ewma 0.049, garch 0.055, har 0.195, bocpd 0.013, hmm 0.026, online_qr 0.346, lgbm 0.314

## Learning log

- 2026-10-24 00:00 UTC: {"garch": {"alpha": 0.0916, "beta": 0.8861}, "hmm": {"sd_bp": [4.32, 7.07, 17.63], "stay": [0.986, 0.955, 0.886]}, "lgbm": {"challenger_loss": 0.25706, "champion_loss": 0.25712, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48502, "challengers": 1, "chance_loss": 0.60783, "widened": false, "champion_loss": 0.48275, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37323, "challengers": 1, "chance_loss": 0.48334, "widened": false, "champion_loss": 0.37104, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26739, "challengers": 3, "chance_loss": 0.35656, "widened": true, "champion_loss": 0.2677, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19276, "challengers": 3, "chance_loss": 0.26901, "widened": true, "champion_loss": 0.19334, "promoted": true}}
- 2026-10-24 12:00 UTC: {"garch": {"alpha": 0.0884, "beta": 0.8957}, "hmm": {"sd_bp": [4.1, 7.07, 17.69], "stay": [0.985, 0.954, 0.886]}}
- 2026-10-25 00:00 UTC: {"garch": {"alpha": 0.1123, "beta": 0.8621}, "hmm": {"sd_bp": [3.96, 7.08, 20.11], "stay": [0.984, 0.951, 0.843]}, "lgbm": {"challenger_loss": 0.25302, "champion_loss": 0.25304, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48062, "challengers": 1, "chance_loss": 0.60677, "widened": false, "champion_loss": 0.47902, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35986, "challengers": 1, "chance_loss": 0.47298, "widened": false, "champion_loss": 0.35858, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27355, "challengers": 1, "chance_loss": 0.36549, "widened": false, "champion_loss": 0.27249, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19061, "challengers": 1, "chance_loss": 0.26514, "widened": false, "champion_loss": 0.18978, "promoted": false}}
- 2026-10-25 12:00 UTC: {"garch": {"alpha": 0.1093, "beta": 0.8694}, "hmm": {"sd_bp": [3.72, 6.8, 19.68], "stay": [0.978, 0.949, 0.836]}}
- 2026-10-26 00:00 UTC: {"garch": {"alpha": 0.1111, "beta": 0.8658}, "hmm": {"sd_bp": [3.48, 6.3, 19.28], "stay": [0.974, 0.951, 0.837]}, "lgbm": {"challenger_loss": 0.25099, "champion_loss": 0.25099, "promoted": false}, "reversal_k3": {"challenger_loss": 0.4884, "challengers": 1, "chance_loss": 0.61064, "widened": false, "champion_loss": 0.48683, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35937, "challengers": 1, "chance_loss": 0.46639, "widened": false, "champion_loss": 0.35872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26862, "challengers": 1, "chance_loss": 0.361, "widened": false, "champion_loss": 0.26837, "promoted": false}, "reversal_k13": {"challenger_loss": 0.18228, "challengers": 1, "chance_loss": 0.25309, "widened": false, "champion_loss": 0.18177, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.48, 6.3, 19.28], current probabilities: [0.945, 0.054, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-26 10:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.353, 'l_abs': 0.722, 'l_hi': 0.799, 'l_lo': 0.777, 'b05': 0.734, 'b25': 0.706, 'b75': 0.671, 'b95': 0.703}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.6], [1.4, 1.8], [1.4, 1.8], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.454, 1.785, 2.282, 2.136, 2.539, 3.161, 3.386, 3.746, 4.372, 4.688, 4.351, 5.015, 5.537, 5.094]}
- calibration offsets (in sigma): {'05': 0.0305, '10': -0.009, '25': -0.0375, '40': -0.026, '50': 0.005, '60': -0.014, '75': -0.0225, '90': 0.009, '95': 0.0395}
