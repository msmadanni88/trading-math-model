# ETH-USD 60s candle generator - report

- generated: 2026-11-22 14:27 UTC
- last closed candle: 2026-11-22 14:27 UTC (staleness 0.5 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.527 (672) [0.494, 0.558] | 0.520 (2879) [0.504, 0.536] | 0.516 (7769) [0.505, 0.527] | 0.519 (4797) [0.505, 0.533] | 0.456 (57) | 0.500 | flat -0.007 (noise 0.028) |
| colour_clear | 0.540 (705) | 0.549 (5561) [0.536, 0.562] | 0.541 (23851) [0.535, 0.547] | 0.526 (63754) [0.520, 0.531] | 0.544 (39516) [0.539, 0.548] | 0.520 (477) | 0.500 | flat +0.007 (noise 0.010) |
| colour_confident | 0.594 (224) | 0.563 (1286) [0.540, 0.586] | 0.577 (4508) [0.565, 0.588] | 0.586 (7230) [0.576, 0.596] | 0.586 (7230) [0.576, 0.596] | 0.544 (158) | 0.500 | flat +0.010 (noise 0.023) |
| colour_next | 0.519 (1437) | 0.531 (10048) [0.525, 0.537] | 0.530 (42898) [0.526, 0.534] | 0.519 (115789) [0.515, 0.522] | 0.530 (71440) [0.527, 0.533] | 0.525 (864) | 0.500 | flat -0.001 (noise 0.008) |
| colour_path | 0.503 (20118) | 0.504 (140672) [0.502, 0.506] | 0.502 (600572) [0.501, 0.504] | 0.501 (1621046) [0.500, 0.502] | 0.502 (1000160) [0.500, 0.502] | 0.497 (12096) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.586 (70) | 0.606 (355) [0.577, 0.642] | 0.611 (1213) [0.595, 0.627] | 0.624 (1897) [0.609, 0.639] | 0.624 (1897) [0.609, 0.639] | 0.620 (50) | 0.500 | flat -0.004 (noise 0.047) |
| reversal_k13_next | 0.469 (49) | 0.311 (495) [0.279, 0.355] | 0.332 (1868) [0.315, 0.351] | 0.316 (5354) [0.306, 0.325] | 0.326 (3249) [0.315, 0.337] | 0.435 (23) | 0.077 | flat -0.037 (noise 0.031) |
| reversal_k13_now | 0.638 (47) | 0.562 (370) [0.522, 0.607] | 0.573 (1634) [0.552, 0.594] | 0.574 (4176) [0.561, 0.586] | 0.570 (2704) [0.554, 0.587] | 0.600 (30) | 0.078 | flat -0.032 (noise 0.038) |
| reversal_k3_next | 0.634 (164) | 0.584 (663) [0.560, 0.609] | 0.600 (2447) [0.590, 0.612] | 0.589 (6892) [0.581, 0.597] | 0.590 (4452) [0.580, 0.601] | 0.644 (101) | 0.293 | flat -0.047 (noise 0.033) |
| reversal_k3_now | 0.936 (47) | 0.936 (373) [0.919, 0.954] | 0.931 (1721) [0.923, 0.941] | 0.935 (4632) [0.929, 0.941] | 0.931 (2869) [0.924, 0.938] | 1.000 (26) | 0.293 | flat +0.009 (noise 0.018) |
| reversal_k5_next | 0.719 (32) | 0.468 (376) [0.420, 0.531] | 0.510 (1986) [0.493, 0.528] | 0.486 (6035) [0.475, 0.497] | 0.482 (4045) [0.468, 0.497] | 0.632 (19) | 0.187 | flat -0.056 (noise 0.045) |
| reversal_k5_now | 0.760 (50) | 0.794 (422) [0.768, 0.817] | 0.794 (1760) [0.777, 0.809] | 0.816 (4418) [0.806, 0.826] | 0.804 (2807) [0.792, 0.815] | 0.900 (30) | 0.187 | up +0.059 (noise 0.029) |
| reversal_k8_next | 0.519 (77) | 0.397 (562) [0.369, 0.435] | 0.415 (2336) [0.400, 0.430] | 0.398 (6311) [0.388, 0.408] | 0.399 (4205) [0.387, 0.411] | 0.452 (42) | 0.121 | flat -0.036 (noise 0.033) |
| reversal_k8_now | 0.640 (50) | 0.655 (420) [0.627, 0.681] | 0.679 (1640) [0.659, 0.698] | 0.695 (4268) [0.683, 0.706] | 0.683 (2681) [0.668, 0.698] | 0.607 (28) | 0.122 | flat -0.021 (noise 0.034) |
| overall | 0.507 (22167) | 0.507 (155073) [0.505, 0.510] | 0.506 (661741) [0.505, 0.507] | 0.504 (1786690) [0.503, 0.505] | 0.505 (1103409) [0.504, 0.506] | 0.502 (13316) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07362, 0.1045] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5323, 'levels': [{'threshold': 0.07362, 'calls_per_day': 147.8, 'win_rate': 0.5684}, {'threshold': 0.1045, 'calls_per_day': 37.4, 'win_rate': 0.616}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42899, 'rate': 0.5297}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15169 | 0.349 | 0.532 (14952) | 0.567 (2249) | 0.756 (2533) |
| volatility: normal | 15169 | 0.378 | 0.527 (15116) | 0.578 (1448) | 0.736 (2391) |
| volatility: wild | 15169 | 0.390 | 0.530 (15129) | 0.592 (1104) | 0.756 (2115) |
| session: Asia 00-08 | 15360 | 0.370 | 0.529 (15247) | 0.566 (1699) | 0.750 (2299) |
| session: Europe 08-13 | 9600 | 0.367 | 0.532 (9525) | 0.584 (1205) | 0.753 (1536) |
| session: US 13-21 | 14967 | 0.380 | 0.534 (14878) | 0.603 (1308) | 0.745 (2380) |
| session: late 21-24 | 5580 | 0.366 | 0.517 (5547) | 0.526 (589) | 0.751 (824) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.355 | 0.369 | 0.291 | 0.291 | 0.483 | 0.227 | 0.482 | 1.027 |
| 6h | 360 | 0.367 | 0.367 | 0.261 | 0.295 | 0.557 | 0.256 | 0.478 | 1.304 |
| 24h | 1440 | 0.375 | 0.372 | 0.273 | 0.297 | 0.523 | 0.259 | 0.492 | 1.308 |
| 7d | 10080 | 0.385 | 0.376 | 0.301 | 0.336 | 0.532 | 0.268 | 0.503 | 1.199 |
| 30d | 43200 | 0.372 | 0.366 | 0.286 | 0.317 | 0.530 | 0.265 | 0.479 | 1.269 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.355 / 0.483 / 0.900; 2: 0.368 / 0.550 / 0.917; 3: 0.359 / 0.483 / 0.917; 4: 0.350 / 0.467 / 0.933; 5: 0.352 / 0.500 / 0.950; 6: 0.371 / 0.533 / 0.900; 7: 0.356 / 0.500 / 0.950; 8: 0.354 / 0.517 / 0.967; 9: 0.345 / 0.483 / 0.967; 10: 0.354 / 0.483 / 0.983; 11: 0.333 / 0.450 / 0.967; 12: 0.351 / 0.500 / 0.967; 13: 0.342 / 0.467 / 1.000; 14: 0.332 / 0.417 / 1.000; 15: 0.335 / 0.433 / 1.000
- 6h: 1: 0.367 / 0.557 / 0.917; 2: 0.353 / 0.471 / 0.919; 3: 0.356 / 0.535 / 0.906; 4: 0.343 / 0.479 / 0.914; 5: 0.358 / 0.526 / 0.914; 6: 0.355 / 0.510 / 0.894; 7: 0.334 / 0.490 / 0.917; 8: 0.355 / 0.554 / 0.931; 9: 0.335 / 0.465 / 0.939; 10: 0.339 / 0.460 / 0.950; 11: 0.339 / 0.482 / 0.936; 12: 0.335 / 0.479 / 0.936; 13: 0.341 / 0.507 / 0.956; 14: 0.346 / 0.524 / 0.975; 15: 0.342 / 0.518 / 0.997
- 24h: 1: 0.375 / 0.523 / 0.908; 2: 0.356 / 0.466 / 0.900; 3: 0.358 / 0.488 / 0.895; 4: 0.358 / 0.494 / 0.897; 5: 0.364 / 0.503 / 0.899; 6: 0.361 / 0.502 / 0.894; 7: 0.356 / 0.500 / 0.895; 8: 0.365 / 0.524 / 0.898; 9: 0.352 / 0.481 / 0.894; 10: 0.359 / 0.513 / 0.900; 11: 0.355 / 0.507 / 0.899; 12: 0.357 / 0.502 / 0.898; 13: 0.351 / 0.500 / 0.897; 14: 0.352 / 0.503 / 0.902; 15: 0.354 / 0.504 / 0.901
- 7d: 1: 0.385 / 0.532 / 0.901; 2: 0.373 / 0.493 / 0.901; 3: 0.373 / 0.505 / 0.900; 4: 0.372 / 0.497 / 0.902; 5: 0.374 / 0.508 / 0.901; 6: 0.372 / 0.506 / 0.901; 7: 0.371 / 0.503 / 0.900; 8: 0.373 / 0.513 / 0.901; 9: 0.368 / 0.496 / 0.900; 10: 0.371 / 0.509 / 0.900; 11: 0.369 / 0.506 / 0.900; 12: 0.371 / 0.506 / 0.901; 13: 0.368 / 0.502 / 0.900; 14: 0.368 / 0.500 / 0.901; 15: 0.367 / 0.501 / 0.901
- 30d: 1: 0.372 / 0.530 / 0.898; 2: 0.359 / 0.491 / 0.900; 3: 0.363 / 0.511 / 0.900; 4: 0.359 / 0.498 / 0.900; 5: 0.360 / 0.506 / 0.900; 6: 0.357 / 0.502 / 0.900; 7: 0.358 / 0.501 / 0.900; 8: 0.359 / 0.508 / 0.900; 9: 0.357 / 0.501 / 0.900; 10: 0.358 / 0.503 / 0.900; 11: 0.357 / 0.506 / 0.900; 12: 0.357 / 0.503 / 0.900; 13: 0.356 / 0.502 / 0.900; 14: 0.356 / 0.502 / 0.900; 15: 0.356 / 0.502 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.158 (body 0.113, range 0.204); 'price stays where it was' would score 0.136; colour right 0.450; typical miss of the close 13.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.138 (body 0.095, range 0.181); 'price stays where it was' would score 0.147; colour right 0.485; typical miss of the close 14.7 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.146 (body 0.097, range 0.195); 'price stays where it was' would score 0.157; colour right 0.495; typical miss of the close 10.3 bp; chain ended on the right side 0.500 of 96 chains; n=1440
- 7d: match 0.133 (body 0.086, range 0.179); 'price stays where it was' would score 0.139; colour right 0.505; typical miss of the close 14.4 bp; chain ended on the right side 0.531 of 672 chains; n=10080
- 30d: match 0.127 (body 0.085, range 0.168); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 10.3 bp; chain ended on the right side 0.517 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.369 / 5.5; 2: 0.204 / 6.2; 3: 0.168 / 8.1; 4: 0.136 / 8.5; 5: 0.126 / 9.2; 6: 0.119 / 9.8; 7: 0.116 / 10.5; 8: 0.101 / 11.4; 9: 0.093 / 11.9; 10: 0.090 / 12.5; 11: 0.087 / 12.9; 12: 0.080 / 13.0; 13: 0.074 / 13.8; 14: 0.069 / 14.2; 15: 0.067 / 14.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1794960000, labels learned 160461, probability skill vs chance 0.2337, widened contest next: False
  - now: threshold 0.8295, hit rate recent 0.9579 / long run 0.9331
    - 6h: 10 calls (41 a day), hit rate 1.000, chance 0.311, naive rule 0.592, lift 3.21x
    - 24h: 45 calls (45 a day), hit rate 1.000, chance 0.310, naive rule 0.559, lift 3.22x
    - 7d: 377 calls (54 a day), hit rate 0.942, chance 0.293, naive rule 0.507, lift 3.22x
    - 30d: 1708 calls (57 a day), hit rate 0.931, chance 0.293, naive rule 0.502, lift 3.18x
  - next: threshold 0.5103, hit rate recent 0.6434 / long run 0.6067
    - 6h: 50 calls (203 a day), hit rate 0.620, chance 0.311, lift 1.99x
    - 24h: 175 calls (176 a day), hit rate 0.629, chance 0.310, lift 2.03x
    - 7d: 744 calls (106 a day), hit rate 0.594, chance 0.293, lift 2.03x
    - 30d: 2501 calls (83 a day), hit rate 0.603, chance 0.293, lift 2.06x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 558, 0.503; 0.35: 528, 0.528; 0.40: 477, 0.575; 0.45: 412, 0.641; 0.50: 363, 0.686; 0.55: 315, 0.732; 0.60: 265, 0.778; 0.65: 223, 0.807; 0.70: 175, 0.838; 0.75: 140, 0.872; 0.80: 92, 0.904; 0.85: 43, 0.940; 0.90: 4, 0.964
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 581, 0.435; 0.35: 490, 0.468; 0.40: 388, 0.508; 0.45: 292, 0.543; 0.50: 186, 0.576; 0.55: 79, 0.588; 0.60: 10, 0.636; 0.65: 0, 0.533
- **K=5**: model 1794528000, labels learned 160459, probability skill vs chance 0.2317, widened contest next: False
  - now: threshold 0.7001, hit rate recent 0.8291 / long run 0.7922
    - 6h: 12 calls (49 a day), hit rate 0.917, chance 0.217, naive rule 0.532, lift 4.23x
    - 24h: 49 calls (49 a day), hit rate 0.857, chance 0.200, naive rule 0.472, lift 4.29x
    - 7d: 418 calls (60 a day), hit rate 0.809, chance 0.192, naive rule 0.425, lift 4.21x
    - 30d: 1750 calls (58 a day), hit rate 0.795, chance 0.187, naive rule 0.413, lift 4.25x
  - next: threshold 0.461, hit rate recent 0.5996 / long run 0.5046
    - 6h: 8 calls (33 a day), hit rate 0.625, chance 0.217, lift 2.88x
    - 24h: 36 calls (36 a day), hit rate 0.694, chance 0.200, lift 3.48x
    - 7d: 356 calls (51 a day), hit rate 0.486, chance 0.192, lift 2.53x
    - 30d: 1921 calls (64 a day), hit rate 0.511, chance 0.187, lift 2.73x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.423; 0.35: 362, 0.475; 0.40: 293, 0.542; 0.45: 237, 0.603; 0.50: 186, 0.655; 0.55: 149, 0.688; 0.60: 114, 0.735; 0.65: 82, 0.772; 0.70: 51, 0.805; 0.75: 27, 0.840; 0.80: 7, 0.854
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 336, 0.392; 0.35: 250, 0.432; 0.40: 159, 0.463; 0.45: 64, 0.505; 0.50: 8, 0.555; 0.55: 0, 0.500
- **K=8**: model 1794960000, labels learned 160456, probability skill vs chance 0.214, widened contest next: False
  - now: threshold 0.5803, hit rate recent 0.6491 / long run 0.6714
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.129, naive rule 0.414, lift 5.66x
    - 24h: 47 calls (47 a day), hit rate 0.638, chance 0.121, naive rule 0.368, lift 5.26x
    - 7d: 418 calls (60 a day), hit rate 0.663, chance 0.124, naive rule 0.353, lift 5.35x
    - 30d: 1631 calls (54 a day), hit rate 0.680, chance 0.123, naive rule 0.348, lift 5.54x
  - next: threshold 0.3537, hit rate recent 0.4779 / long run 0.4202
    - 6h: 20 calls (82 a day), hit rate 0.500, chance 0.129, lift 3.89x
    - 24h: 81 calls (82 a day), hit rate 0.494, chance 0.121, lift 4.07x
    - 7d: 563 calls (81 a day), hit rate 0.409, chance 0.124, lift 3.30x
    - 30d: 2291 calls (76 a day), hit rate 0.416, chance 0.123, lift 3.39x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 254, 0.428; 0.35: 199, 0.488; 0.40: 156, 0.538; 0.45: 120, 0.579; 0.50: 85, 0.637; 0.55: 62, 0.673; 0.60: 41, 0.709; 0.65: 24, 0.766; 0.70: 9, 0.809; 0.75: 1, 0.721
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 160, 0.376; 0.35: 83, 0.406; 0.40: 27, 0.442; 0.45: 6, 0.468; 0.50: 1, 0.690
- **K=13**: model 1795132800, labels learned 160451, probability skill vs chance 0.1995, widened contest next: False
  - now: threshold 0.4548, hit rate recent 0.6152 / long run 0.576
    - 6h: 12 calls (50 a day), hit rate 0.667, chance 0.080, naive rule 0.400, lift 8.36x
    - 24h: 45 calls (45 a day), hit rate 0.667, chance 0.084, naive rule 0.349, lift 7.92x
    - 7d: 376 calls (54 a day), hit rate 0.564, chance 0.080, naive rule 0.298, lift 7.02x
    - 30d: 1623 calls (54 a day), hit rate 0.575, chance 0.079, naive rule 0.294, lift 7.26x
  - next: threshold 0.3069, hit rate recent 0.4251 / long run 0.3348
    - 6h: 9 calls (38 a day), hit rate 0.444, chance 0.080, lift 5.58x
    - 24h: 45 calls (45 a day), hit rate 0.489, chance 0.084, lift 5.81x
    - 7d: 479 calls (69 a day), hit rate 0.322, chance 0.080, lift 4.00x
    - 30d: 1841 calls (61 a day), hit rate 0.333, chance 0.079, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 139, 0.424; 0.35: 102, 0.474; 0.40: 70, 0.535; 0.45: 49, 0.585; 0.50: 34, 0.623; 0.55: 21, 0.648; 0.60: 10, 0.675; 0.65: 2, 0.552; 0.70: 0, 0.200
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 54, 0.342; 0.35: 15, 0.375; 0.40: 2, 0.434

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 21.688 | 0.99% | 0.883 | 0.450 | 0.249 | 0.567 | 0.191 |
| 6h | 25.362 | 2.86% | 0.906 | 0.533 | 0.249 | 0.521 | 0.522 |
| 24h | 19.643 | 6.46% | 0.902 | 0.498 | 0.250 | 0.513 | 0.568 |
| 7d | 24.289 | 4.12% | 0.900 | 0.501 | 0.250 | 0.498 | 0.660 |
| 30d | 18.927 | 4.87% | 0.900 | 0.501 | 0.250 | 0.504 | 0.716 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 21.905 | 21.791 | 21.824 | 21.746 | 22.127 | 21.627 | 21.588 | 21.561 | 21.630 | 21.688 |
| 6h | 26.110 | 26.003 | 25.750 | 25.366 | 26.542 | 25.559 | 25.357 | 25.322 | 25.343 | 25.362 |
| 24h | 20.999 | 19.951 | 19.865 | 19.667 | 20.294 | 19.953 | 19.658 | 19.610 | 19.629 | 19.643 |
| 7d | 25.333 | 24.520 | 24.452 | 24.298 | 24.800 | 24.570 | 24.281 | 24.239 | 24.251 | 24.289 |
| 30d | 19.895 | 19.113 | 19.065 | 18.983 | 19.319 | 19.242 | 18.912 | 18.886 | 18.895 | 18.927 |

## Next candle

- candle starting 2026-11-22 14:27 UTC, last close 1702.11
- P(up) 0.5412, return quantiles (bp): {'05': -10.137, '10': -7.702, '25': -2.92, '40': -0.757, '50': 0.506, '60': 1.885, '75': 4.351, '90': 7.43, '95': 9.994}
- changepoint probability 0.0431, regime age 83.2 min
- agent weights: empirical 0.005, ewma 0.030, garch 0.070, har 0.249, bocpd 0.008, hmm 0.077, online_qr 0.269, lgbm 0.292

## Learning log

- 2026-11-20 12:00 UTC: {"garch": {"alpha": 0.0623, "beta": 0.9234}, "hmm": {"sd_bp": [5.82, 9.8, 20.43], "stay": [0.979, 0.945, 0.9]}}
- 2026-11-21 00:00 UTC: {"garch": {"alpha": 0.0609, "beta": 0.9306}, "hmm": {"sd_bp": [5.81, 9.88, 20.94], "stay": [0.982, 0.949, 0.932]}, "lgbm": {"challenger_loss": 0.25791, "champion_loss": 0.25798, "promoted": true}, "reversal_k3": {"challenger_loss": 0.4762, "challengers": 1, "chance_loss": 0.60349, "widened": false, "champion_loss": 0.47382, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38171, "challengers": 1, "chance_loss": 0.49295, "widened": false, "champion_loss": 0.38009, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27383, "challengers": 1, "chance_loss": 0.36979, "widened": false, "champion_loss": 0.27333, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20234, "challengers": 1, "chance_loss": 0.27673, "widened": false, "champion_loss": 0.20172, "promoted": false}}
- 2026-11-21 12:00 UTC: {"garch": {"alpha": 0.0979, "beta": 0.8879}, "hmm": {"sd_bp": [5.86, 10.53, 26.19], "stay": [0.982, 0.953, 0.91]}}
- 2026-11-22 00:00 UTC: {"garch": {"alpha": 0.0712, "beta": 0.9215}, "hmm": {"sd_bp": [5.69, 10.58, 28.33], "stay": [0.985, 0.953, 0.874]}, "lgbm": {"challenger_loss": 0.24557, "champion_loss": 0.24554, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48129, "challengers": 1, "chance_loss": 0.60807, "widened": false, "champion_loss": 0.47918, "promoted": false}, "reversal_k5": {"challenger_loss": 0.381, "challengers": 1, "chance_loss": 0.49754, "widened": false, "champion_loss": 0.37986, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28291, "challengers": 1, "chance_loss": 0.38778, "widened": false, "champion_loss": 0.28187, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20591, "challengers": 1, "chance_loss": 0.29298, "widened": false, "champion_loss": 0.20541, "promoted": false}}
- 2026-11-22 12:00 UTC: {"garch": {"alpha": 0.0748, "beta": 0.9173}, "hmm": {"sd_bp": [5.55, 10.36, 28.43], "stay": [0.982, 0.95, 0.859]}}
- HMM volatility states (sd, bp per minute): [5.55, 10.36, 28.43], current probabilities: [0.754, 0.239, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-11-22 14:35 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.329, 'l_abs': 0.742, 'l_hi': 0.811, 'l_lo': 0.757, 'b05': 0.792, 'b25': 0.73, 'b75': 0.739, 'b95': 0.755}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.2, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.3, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.2, 1.5], [1.3, 1.5], [1.3, 1.5]], 'cone_width': [1.227, 1.567, 1.887, 2.201, 2.565, 2.832, 2.973, 3.098, 3.02, 3.238, 3.389, 3.985, 3.981, 4.212]}
- calibration offsets (in sigma): {'05': 0.083, '10': 0.036, '25': 0.115, '40': 0.044, '50': 0.02, '60': 0.016, '75': 0.025, '90': -0.076, '95': -0.093}
