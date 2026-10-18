# ETH-USD 60s candle generator - report

- generated: 2026-10-18 09:22 UTC
- last closed candle: 2026-10-18 09:22 UTC (staleness 0.0 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.479 (96) | 0.504 (671) [0.478, 0.533] | 0.518 (2875) [0.499, 0.537] | 0.510 (4410) [0.495, 0.524] | 0.508 (1438) [0.480, 0.536] | 0.595 (37) | 0.500 | flat -0.004 (noise 0.038) |
| colour_clear | 0.567 (765) | 0.542 (5500) [0.534, 0.552] | 0.520 (23346) [0.512, 0.529] | 0.512 (35822) [0.505, 0.518] | 0.544 (11584) [0.538, 0.549] | 0.549 (308) | 0.500 | flat -0.003 (noise 0.010) |
| colour_confident | 0.573 (131) | 0.592 (687) [0.576, 0.607] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.602 (1911) [0.580, 0.625] | 0.543 (81) | 0.500 | flat -0.015 (noise 0.025) |
| colour_next | 0.546 (1415) | 0.527 (10006) [0.520, 0.535] | 0.515 (42856) [0.509, 0.520] | 0.509 (65717) [0.505, 0.514] | 0.528 (21368) [0.523, 0.533] | 0.504 (556) | 0.500 | flat -0.002 (noise 0.007) |
| colour_path | 0.493 (19810) | 0.501 (140084) [0.498, 0.505] | 0.501 (599984) [0.500, 0.503] | 0.501 (920038) [0.499, 0.502] | 0.500 (299152) [0.498, 0.502] | 0.503 (7784) | 0.500 | flat +0.001 (noise 0.003) |
| colour_strong | 0.588 (34) | 0.641 (167) [0.590, 0.689] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.651 (499) [0.617, 0.688] | 0.636 (22) | 0.500 | flat -0.015 (noise 0.046) |
| reversal_k13_next | 0.319 (47) | 0.305 (419) [0.282, 0.331] | 0.313 (2037) [0.298, 0.328] | 0.306 (3137) [0.294, 0.318] | 0.319 (1032) [0.305, 0.332] | 0.367 (30) | 0.077 | flat -0.023 (noise 0.031) |
| reversal_k13_now | 0.611 (54) | 0.562 (368) [0.534, 0.595] | 0.587 (1528) [0.568, 0.607] | 0.580 (2285) [0.564, 0.597] | 0.579 (813) [0.555, 0.607] | 0.500 (24) | 0.077 | flat -0.013 (noise 0.036) |
| reversal_k3_next | 0.570 (114) | 0.568 (722) [0.555, 0.583] | 0.580 (2587) [0.566, 0.594] | 0.582 (3863) [0.572, 0.594] | 0.573 (1423) [0.558, 0.591] | 0.543 (35) | 0.293 | flat -0.023 (noise 0.028) |
| reversal_k3_now | 0.871 (62) | 0.933 (388) [0.908, 0.960] | 0.937 (1719) [0.928, 0.946] | 0.937 (2626) [0.930, 0.944] | 0.928 (863) [0.916, 0.941] | 0.963 (27) | 0.293 | flat +0.010 (noise 0.018) |
| reversal_k5_next | 0.451 (142) | 0.466 (708) [0.443, 0.493] | 0.477 (2327) [0.460, 0.494] | 0.480 (3367) [0.466, 0.494] | 0.460 (1377) [0.441, 0.482] | 0.419 (62) | 0.187 | flat -0.005 (noise 0.029) |
| reversal_k5_now | 0.827 (52) | 0.818 (351) [0.792, 0.845] | 0.830 (1614) [0.815, 0.845] | 0.832 (2410) [0.820, 0.844] | 0.822 (799) [0.801, 0.842] | 0.850 (20) | 0.187 | flat -0.009 (noise 0.028) |
| reversal_k8_next | 0.383 (120) | 0.372 (634) [0.343, 0.400] | 0.402 (2181) [0.384, 0.422] | 0.391 (3430) [0.378, 0.405] | 0.384 (1324) [0.364, 0.404] | 0.409 (44) | 0.122 | flat -0.024 (noise 0.028) |
| reversal_k8_now | 0.755 (49) | 0.685 (352) [0.664, 0.709] | 0.717 (1583) [0.697, 0.737] | 0.708 (2407) [0.692, 0.724] | 0.698 (820) [0.671, 0.724] | 0.765 (17) | 0.122 | flat -0.014 (noise 0.033) |
| overall | 0.499 (21961) | 0.504 (154703) [0.502, 0.507] | 0.504 (661291) [0.503, 0.505] | 0.503 (1013690) [0.502, 0.504] | 0.504 (330409) [0.501, 0.506] | 0.504 (8636) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.06849, 0.1054] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5278, 'levels': [{'threshold': 0.06849, 'calls_per_day': 138.3, 'win_rate': 0.5651}, {'threshold': 0.1054, 'calls_per_day': 33.9, 'win_rate': 0.6444}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 20786, 'rate': 0.5286}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15069 | 0.336 | 0.521 (14821) | 0.591 (1393) | 0.778 (2460) |
| volatility: normal | 15066 | 0.362 | 0.515 (15000) | 0.608 (431) | 0.769 (2198) |
| volatility: wild | 15067 | 0.377 | 0.505 (15023) | 0.649 (168) | 0.769 (2050) |
| session: Asia 00-08 | 15360 | 0.357 | 0.519 (15256) | 0.602 (752) | 0.766 (2261) |
| session: Europe 08-13 | 9382 | 0.352 | 0.513 (9299) | 0.578 (497) | 0.777 (1470) |
| session: US 13-21 | 14880 | 0.367 | 0.509 (14775) | 0.586 (466) | 0.782 (2157) |
| session: late 21-24 | 5580 | 0.349 | 0.513 (5514) | 0.653 (277) | 0.756 (820) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.348 | 0.357 | 0.317 | 0.317 | 0.450 | 0.251 | 0.445 | 0.888 |
| 6h | 360 | 0.339 | 0.338 | 0.261 | 0.291 | 0.499 | 0.238 | 0.441 | 1.236 |
| 24h | 1440 | 0.346 | 0.340 | 0.252 | 0.282 | 0.531 | 0.255 | 0.437 | 1.171 |
| 7d | 10080 | 0.365 | 0.356 | 0.279 | 0.311 | 0.525 | 0.261 | 0.469 | 1.222 |
| 30d | 43200 | 0.358 | 0.354 | 0.279 | 0.308 | 0.515 | 0.252 | 0.465 | 1.300 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.348 / 0.450 / 0.800; 2: 0.363 / 0.533 / 0.767; 3: 0.368 / 0.567 / 0.750; 4: 0.318 / 0.450 / 0.683; 5: 0.351 / 0.583 / 0.700; 6: 0.365 / 0.617 / 0.750; 7: 0.310 / 0.417 / 0.733; 8: 0.353 / 0.517 / 0.783; 9: 0.324 / 0.517 / 0.767; 10: 0.316 / 0.433 / 0.817; 11: 0.337 / 0.517 / 0.833; 12: 0.317 / 0.450 / 0.783; 13: 0.351 / 0.567 / 0.850; 14: 0.330 / 0.500 / 0.833; 15: 0.355 / 0.517 / 0.817
- 6h: 1: 0.339 / 0.499 / 0.858; 2: 0.327 / 0.476 / 0.861; 3: 0.337 / 0.507 / 0.839; 4: 0.327 / 0.479 / 0.842; 5: 0.330 / 0.487 / 0.858; 6: 0.326 / 0.485 / 0.878; 7: 0.326 / 0.482 / 0.867; 8: 0.338 / 0.532 / 0.889; 9: 0.324 / 0.504 / 0.892; 10: 0.327 / 0.470 / 0.897; 11: 0.333 / 0.518 / 0.914; 12: 0.326 / 0.485 / 0.897; 13: 0.335 / 0.524 / 0.906; 14: 0.322 / 0.468 / 0.900; 15: 0.335 / 0.527 / 0.897
- 24h: 1: 0.346 / 0.531 / 0.871; 2: 0.329 / 0.473 / 0.894; 3: 0.338 / 0.513 / 0.885; 4: 0.331 / 0.495 / 0.883; 5: 0.333 / 0.504 / 0.887; 6: 0.333 / 0.502 / 0.892; 7: 0.335 / 0.510 / 0.888; 8: 0.331 / 0.504 / 0.894; 9: 0.327 / 0.485 / 0.897; 10: 0.331 / 0.502 / 0.899; 11: 0.324 / 0.491 / 0.901; 12: 0.324 / 0.489 / 0.895; 13: 0.326 / 0.493 / 0.897; 14: 0.324 / 0.493 / 0.893; 15: 0.328 / 0.499 / 0.892
- 7d: 1: 0.365 / 0.525 / 0.901; 2: 0.353 / 0.495 / 0.900; 3: 0.357 / 0.509 / 0.899; 4: 0.352 / 0.496 / 0.899; 5: 0.354 / 0.502 / 0.900; 6: 0.354 / 0.503 / 0.900; 7: 0.353 / 0.503 / 0.900; 8: 0.351 / 0.499 / 0.901; 9: 0.352 / 0.503 / 0.902; 10: 0.353 / 0.506 / 0.902; 11: 0.347 / 0.491 / 0.902; 12: 0.352 / 0.504 / 0.901; 13: 0.351 / 0.502 / 0.902; 14: 0.348 / 0.498 / 0.902; 15: 0.352 / 0.505 / 0.903
- 30d: 1: 0.358 / 0.515 / 0.899; 2: 0.351 / 0.496 / 0.900; 3: 0.353 / 0.510 / 0.900; 4: 0.349 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.503 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.495 / 0.900; 10: 0.348 / 0.506 / 0.900; 11: 0.346 / 0.499 / 0.900; 12: 0.347 / 0.503 / 0.900; 13: 0.347 / 0.503 / 0.900; 14: 0.345 / 0.498 / 0.900; 15: 0.346 / 0.498 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.103 (body 0.072, range 0.134); 'price stays where it was' would score 0.077; colour right 0.617; typical miss of the close 9.0 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.109 (body 0.080, range 0.138); 'price stays where it was' would score 0.101; colour right 0.541; typical miss of the close 6.4 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.130 (body 0.096, range 0.163); 'price stays where it was' would score 0.126; colour right 0.521; typical miss of the close 6.6 bp; chain ended on the right side 0.531 of 96 chains; n=1440
- 7d: match 0.124 (body 0.085, range 0.164); 'price stays where it was' would score 0.130; colour right 0.498; typical miss of the close 8.8 bp; chain ended on the right side 0.505 of 671 chains; n=10080
- 30d: match 0.120 (body 0.081, range 0.160); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.520 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 4.0; 2: 0.196 / 4.4; 3: 0.165 / 6.0; 4: 0.134 / 6.6; 5: 0.121 / 7.3; 6: 0.110 / 7.7; 7: 0.103 / 8.1; 8: 0.096 / 8.5; 9: 0.087 / 8.5; 10: 0.086 / 9.3; 11: 0.080 / 9.9; 12: 0.076 / 10.3; 13: 0.064 / 10.5; 14: 0.066 / 10.7; 15: 0.058 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 109756, probability skill vs chance 0.2276, widened contest next: False
  - now: threshold 0.8378, hit rate recent 0.9315 / long run 0.933
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.295, naive rule 0.498, lift 3.16x
    - 24h: 64 calls (64 a day), hit rate 0.938, chance 0.293, naive rule 0.495, lift 3.20x
    - 7d: 383 calls (55 a day), hit rate 0.940, chance 0.290, naive rule 0.487, lift 3.24x
    - 30d: 1723 calls (57 a day), hit rate 0.937, chance 0.291, naive rule 0.484, lift 3.22x
  - next: threshold 0.5422, hit rate recent 0.5497 / long run 0.5697
    - 6h: 27 calls (109 a day), hit rate 0.593, chance 0.295, lift 2.01x
    - 24h: 90 calls (90 a day), hit rate 0.489, chance 0.293, lift 1.67x
    - 7d: 710 calls (101 a day), hit rate 0.569, chance 0.290, lift 1.96x
    - 30d: 2592 calls (86 a day), hit rate 0.579, chance 0.291, lift 1.99x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 568, 0.490; 0.35: 540, 0.514; 0.40: 483, 0.565; 0.45: 414, 0.635; 0.50: 361, 0.688; 0.55: 316, 0.730; 0.60: 270, 0.774; 0.65: 224, 0.803; 0.70: 179, 0.836; 0.75: 139, 0.871; 0.80: 95, 0.912; 0.85: 49, 0.951; 0.90: 3, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.425; 0.35: 499, 0.460; 0.40: 408, 0.491; 0.45: 313, 0.525; 0.50: 204, 0.557; 0.55: 92, 0.577; 0.60: 14, 0.611; 0.65: 1, 0.654
- **K=5**: model 1791590400, labels learned 109754, probability skill vs chance 0.2177, widened contest next: True
  - now: threshold 0.69, hit rate recent 0.8401 / long run 0.8276
    - 6h: 12 calls (49 a day), hit rate 0.833, chance 0.191, naive rule 0.390, lift 4.37x
    - 24h: 58 calls (58 a day), hit rate 0.828, chance 0.196, naive rule 0.415, lift 4.22x
    - 7d: 349 calls (50 a day), hit rate 0.819, chance 0.187, naive rule 0.404, lift 4.38x
    - 30d: 1609 calls (54 a day), hit rate 0.832, chance 0.188, naive rule 0.395, lift 4.43x
  - next: threshold 0.4041, hit rate recent 0.4143 / long run 0.4577
    - 6h: 51 calls (207 a day), hit rate 0.373, chance 0.191, lift 1.95x
    - 24h: 159 calls (160 a day), hit rate 0.409, chance 0.196, lift 2.08x
    - 7d: 749 calls (107 a day), hit rate 0.463, chance 0.187, lift 2.48x
    - 30d: 2369 calls (79 a day), hit rate 0.474, chance 0.188, lift 2.53x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 422, 0.421; 0.35: 351, 0.486; 0.40: 282, 0.559; 0.45: 230, 0.615; 0.50: 181, 0.666; 0.55: 137, 0.711; 0.60: 108, 0.751; 0.65: 81, 0.793; 0.70: 60, 0.825; 0.75: 33, 0.869; 0.80: 10, 0.882
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.389; 0.35: 251, 0.423; 0.40: 160, 0.449; 0.45: 76, 0.465; 0.50: 18, 0.502; 0.55: 2, 0.558
- **K=8**: model 1791936000, labels learned 109751, probability skill vs chance 0.1968, widened contest next: False
  - now: threshold 0.5774, hit rate recent 0.7344 / long run 0.7028
    - 6h: 10 calls (41 a day), hit rate 0.800, chance 0.107, naive rule 0.275, lift 7.49x
    - 24h: 53 calls (53 a day), hit rate 0.755, chance 0.120, naive rule 0.321, lift 6.28x
    - 7d: 343 calls (49 a day), hit rate 0.700, chance 0.121, naive rule 0.333, lift 5.79x
    - 30d: 1576 calls (53 a day), hit rate 0.719, chance 0.122, naive rule 0.331, lift 5.87x
  - next: threshold 0.3409, hit rate recent 0.3732 / long run 0.3795
    - 6h: 33 calls (135 a day), hit rate 0.394, chance 0.107, lift 3.69x
    - 24h: 125 calls (126 a day), hit rate 0.352, chance 0.120, lift 2.93x
    - 7d: 644 calls (92 a day), hit rate 0.384, chance 0.121, lift 3.17x
    - 30d: 2198 calls (73 a day), hit rate 0.402, chance 0.122, lift 3.28x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 258, 0.421; 0.35: 195, 0.493; 0.40: 149, 0.553; 0.45: 117, 0.596; 0.50: 90, 0.637; 0.55: 65, 0.687; 0.60: 44, 0.732; 0.65: 24, 0.789; 0.70: 9, 0.838; 0.75: 1, 0.778
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 178, 0.353; 0.35: 105, 0.386; 0.40: 42, 0.420; 0.45: 9, 0.441; 0.50: 1, 0.419
- **K=13**: model 1792022400, labels learned 109746, probability skill vs chance 0.1819, widened contest next: False
  - now: threshold 0.4161, hit rate recent 0.556 / long run 0.5729
    - 6h: 15 calls (62 a day), hit rate 0.467, chance 0.069, naive rule 0.239, lift 6.73x
    - 24h: 62 calls (63 a day), hit rate 0.565, chance 0.079, naive rule 0.285, lift 7.19x
    - 7d: 367 calls (53 a day), hit rate 0.561, chance 0.077, naive rule 0.279, lift 7.31x
    - 30d: 1526 calls (51 a day), hit rate 0.586, chance 0.078, naive rule 0.274, lift 7.50x
  - next: threshold 0.2794, hit rate recent 0.3184 / long run 0.3128
    - 6h: 24 calls (100 a day), hit rate 0.333, chance 0.069, lift 4.81x
    - 24h: 65 calls (66 a day), hit rate 0.277, chance 0.079, lift 3.53x
    - 7d: 417 calls (60 a day), hit rate 0.309, chance 0.077, lift 4.03x
    - 30d: 2041 calls (68 a day), hit rate 0.314, chance 0.078, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.452; 0.35: 85, 0.512; 0.40: 61, 0.565; 0.45: 41, 0.620; 0.50: 25, 0.659; 0.55: 14, 0.707; 0.60: 5, 0.759; 0.65: 1, 0.833
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.326; 0.35: 13, 0.355; 0.40: 2, 0.397

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 13.185 | 3.43% | 0.833 | 0.450 | 0.251 | 0.500 | 0.631 |
| 6h | 9.261 | 0.81% | 0.869 | 0.497 | 0.253 | 0.479 | 0.515 |
| 24h | 11.310 | 4.84% | 0.885 | 0.492 | 0.250 | 0.502 | 0.638 |
| 7d | 15.610 | 4.40% | 0.900 | 0.500 | 0.251 | 0.491 | 0.649 |
| 30d | 13.823 | 4.11% | 0.900 | 0.500 | 0.251 | 0.496 | 0.678 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 13.653 | 13.476 | 13.257 | 13.289 | 13.444 | 13.199 | 13.173 | 13.154 | 13.178 | 13.185 |
| 6h | 9.336 | 9.300 | 9.259 | 9.304 | 9.309 | 9.254 | 9.244 | 9.230 | 9.231 | 9.261 |
| 24h | 11.886 | 11.479 | 11.338 | 11.344 | 11.468 | 11.418 | 11.304 | 11.299 | 11.290 | 11.310 |
| 7d | 16.329 | 15.790 | 15.710 | 15.628 | 15.875 | 15.815 | 15.615 | 15.587 | 15.580 | 15.610 |
| 30d | 14.415 | 13.946 | 13.908 | 13.850 | 14.071 | 14.008 | 13.821 | 13.797 | 13.797 | 13.823 |

## Next candle

- candle starting 2026-10-18 09:22 UTC, last close 2412.95
- P(up) 0.4871, return quantiles (bp): {'05': -9.207, '10': -6.606, '25': -3.369, '40': -1.488, '50': -0.183, '60': 1.253, '75': 3.187, '90': 6.766, '95': 9.188}
- changepoint probability 0.1187, regime age 21.9 min
- agent weights: empirical 0.005, ewma 0.048, garch 0.165, har 0.140, bocpd 0.061, hmm 0.122, online_qr 0.201, lgbm 0.258

## Learning log

- 2026-10-16 00:00 UTC: {"garch": {"alpha": 0.1738, "beta": 0.7899}, "hmm": {"sd_bp": [3.23, 6.04, 18.9], "stay": [0.956, 0.967, 0.908]}, "lgbm": {"challenger_loss": 0.25071, "champion_loss": 0.25066, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47886, "challengers": 1, "chance_loss": 0.59857, "widened": false, "champion_loss": 0.4753, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37145, "challengers": 1, "chance_loss": 0.47761, "widened": false, "champion_loss": 0.36967, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26951, "challengers": 3, "chance_loss": 0.36003, "widened": true, "champion_loss": 0.26906, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19816, "challengers": 3, "chance_loss": 0.2703, "widened": true, "champion_loss": 0.19764, "promoted": false}}
- 2026-10-16 12:00 UTC: {"garch": {"alpha": 0.1713, "beta": 0.7877}, "hmm": {"sd_bp": [3.83, 6.59, 20.28], "stay": [0.971, 0.966, 0.908]}}
- 2026-10-17 00:00 UTC: {"garch": {"alpha": 0.1669, "beta": 0.792}, "hmm": {"sd_bp": [3.98, 7.01, 21.66], "stay": [0.979, 0.971, 0.896]}, "lgbm": {"challenger_loss": 0.25057, "champion_loss": 0.25056, "promoted": false}, "reversal_k3": {"challenger_loss": 0.47269, "challengers": 3, "chance_loss": 0.59288, "widened": true, "champion_loss": 0.47267, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3634, "challengers": 3, "chance_loss": 0.4687, "widened": true, "champion_loss": 0.36318, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26964, "challengers": 3, "chance_loss": 0.35524, "widened": true, "champion_loss": 0.2695, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20303, "challengers": 1, "chance_loss": 0.27352, "widened": false, "champion_loss": 0.20212, "promoted": false}}
- 2026-10-17 12:00 UTC: {"garch": {"alpha": 0.13, "beta": 0.8537}, "hmm": {"sd_bp": [3.62, 6.89, 21.68], "stay": [0.985, 0.977, 0.919]}}
- 2026-10-18 00:00 UTC: {"garch": {"alpha": 0.1316, "beta": 0.8546}, "hmm": {"sd_bp": [3.41, 6.6, 20.67], "stay": [0.985, 0.978, 0.942]}, "lgbm": {"challenger_loss": 0.25556, "champion_loss": 0.25559, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48287, "challengers": 3, "chance_loss": 0.60271, "widened": true, "champion_loss": 0.4824, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.48691, "widened": true, "champion_loss": 0.37779, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28366, "challengers": 3, "chance_loss": 0.37373, "widened": true, "champion_loss": 0.28347, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19986, "challengers": 1, "chance_loss": 0.27202, "widened": false, "champion_loss": 0.19842, "promoted": false}}
- HMM volatility states (sd, bp per minute): [3.41, 6.6, 20.67], current probabilities: [0.064, 0.93, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-10-18 09:30 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.357, 'l_abs': 0.662, 'l_hi': 0.717, 'l_lo': 0.719, 'b05': 0.664, 'b25': 0.65, 'b75': 0.624, 'b95': 0.66}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8]], 'cone_width': [1.776, 2.508, 2.901, 2.826, 2.751, 3.099, 2.944, 2.946, 2.99, 2.959, 3.289, 3.43, 3.426, 3.699]}
- calibration offsets (in sigma): {'05': 0.0005, '10': -0.009, '25': -0.0375, '40': -0.066, '50': -0.035, '60': 0.016, '75': -0.0125, '90': 0.029, '95': 0.0495}
