# ETH-USD 60s candle generator - report

- generated: 2026-10-07 02:14 UTC
- last closed candle: 2026-10-07 02:14 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.524 (670) [0.487, 0.563] | 0.510 (2875) [0.490, 0.530] | 0.515 (3355) [0.497, 0.531] | 0.540 (383) [0.482, 0.599] | 0.125 (8) | 0.500 | flat -0.007 (noise 0.035) |
| colour_clear | 0.523 (776) | 0.520 (5262) [0.498, 0.541] | 0.503 (23269) [0.497, 0.510] | 0.502 (27175) [0.496, 0.508] | 0.547 (2937) [0.534, 0.559] | 0.483 (91) | 0.500 | flat +0.025 (noise 0.013) |
| colour_confident | 0.518 (168) | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.548 (31) | 0.500 | - |
| colour_next | 0.511 (1423) | 0.519 (9981) [0.506, 0.532] | 0.505 (42883) [0.500, 0.510] | 0.504 (50023) [0.499, 0.509] | 0.533 (5674) [0.518, 0.549] | 0.496 (133) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.498 (19922) | 0.502 (139734) [0.498, 0.506] | 0.501 (600362) [0.500, 0.503] | 0.501 (700322) [0.500, 0.502] | 0.501 (79436) [0.496, 0.506] | 0.488 (1862) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.513 (39) | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.778 (9) | 0.500 | - |
| reversal_k13_next | 0.324 (71) | 0.301 (598) [0.277, 0.324] | 0.308 (2033) [0.293, 0.324] | 0.303 (2437) [0.289, 0.318] | 0.325 (332) [0.306, 0.344] | 0.214 (14) | 0.077 | flat +0.016 (noise 0.028) |
| reversal_k13_now | 0.508 (63) | 0.587 (392) [0.546, 0.634] | 0.583 (1481) [0.560, 0.607] | 0.583 (1713) [0.563, 0.603] | 0.593 (241) [0.534, 0.664] | 0.600 (5) | 0.077 | flat -0.005 (noise 0.039) |
| reversal_k3_next | 0.689 (45) | 0.587 (605) [0.562, 0.621] | 0.586 (2414) [0.570, 0.602] | 0.588 (2802) [0.575, 0.602] | 0.591 (362) [0.563, 0.661] | 0.300 (10) | 0.292 | flat +0.022 (noise 0.032) |
| reversal_k3_now | 0.902 (61) | 0.929 (411) [0.920, 0.939] | 0.939 (1701) [0.930, 0.949] | 0.940 (1993) [0.932, 0.948] | 0.926 (230) [0.912, 0.943] | 1.000 (2) | 0.293 | flat -0.018 (noise 0.017) |
| reversal_k5_next | 0.490 (49) | 0.463 (723) [0.432, 0.495] | 0.486 (2101) [0.466, 0.507] | 0.487 (2387) [0.470, 0.505] | 0.453 (397) [0.424, 0.510] | 0.154 (13) | 0.187 | flat -0.046 (noise 0.036) |
| reversal_k5_now | 0.768 (56) | 0.843 (394) [0.816, 0.866] | 0.837 (1579) [0.822, 0.853] | 0.838 (1841) [0.823, 0.851] | 0.839 (230) [0.795, 0.879] | 0.667 (6) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.416 (89) | 0.400 (495) [0.367, 0.430] | 0.404 (2043) [0.387, 0.423] | 0.398 (2433) [0.383, 0.415] | 0.410 (327) [0.374, 0.448] | 0.125 (16) | 0.122 | flat +0.002 (noise 0.033) |
| reversal_k8_now | 0.651 (66) | 0.734 (376) [0.700, 0.766] | 0.726 (1570) [0.708, 0.745] | 0.718 (1824) [0.699, 0.736] | 0.743 (237) [0.707, 0.781] | 0.500 (6) | 0.122 | flat -0.018 (noise 0.033) |
| overall | 0.501 (21941) | 0.505 (154379) [0.501, 0.509] | 0.504 (661042) [0.502, 0.505] | 0.503 (771130) [0.502, 0.504] | 0.505 (87849) [0.500, 0.512] | 0.480 (2075) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07771, 0.1156] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.534, 'levels': [{'threshold': 0.07771, 'calls_per_day': 143.9, 'win_rate': 0.587}, {'threshold': 0.1156, 'calls_per_day': 35.5, 'win_rate': 0.6255}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 4675, 'rate': 0.538}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14925 | 0.334 | 0.513 (14706) | 0.608 (574) | 0.777 (2409) |
| volatility: normal | 14925 | 0.359 | 0.508 (14859) | 0.564 (55) | 0.775 (2099) |
| volatility: wild | 14924 | 0.373 | 0.494 (14880) | - | 0.775 (2079) |
| session: Asia 00-08 | 15014 | 0.351 | 0.504 (14911) | 0.597 (238) | 0.774 (2175) |
| session: Europe 08-13 | 9300 | 0.349 | 0.501 (9238) | 0.549 (111) | 0.770 (1427) |
| session: US 13-21 | 14880 | 0.365 | 0.505 (14778) | 0.611 (185) | 0.786 (2200) |
| session: late 21-24 | 5580 | 0.351 | 0.510 (5518) | 0.670 (112) | 0.762 (785) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.300 | 0.353 | 0.368 | 0.368 | 0.373 | 0.180 | 0.420 | 0.622 |
| 6h | 360 | 0.325 | 0.325 | 0.266 | 0.267 | 0.510 | 0.236 | 0.414 | 1.129 |
| 24h | 1440 | 0.351 | 0.347 | 0.282 | 0.303 | 0.507 | 0.248 | 0.454 | 1.179 |
| 7d | 10080 | 0.350 | 0.347 | 0.275 | 0.298 | 0.519 | 0.245 | 0.455 | 1.262 |
| 30d | 43200 | 0.355 | 0.354 | 0.279 | 0.308 | 0.505 | 0.246 | 0.464 | 1.289 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.300 / 0.373 / 0.767; 2: 0.314 / 0.475 / 0.650; 3: 0.293 / 0.441 / 0.617; 4: 0.300 / 0.576 / 0.583; 5: 0.281 / 0.373 / 0.567; 6: 0.299 / 0.593 / 0.500; 7: 0.269 / 0.424 / 0.450; 8: 0.259 / 0.407 / 0.450; 9: 0.258 / 0.525 / 0.500; 10: 0.240 / 0.407 / 0.467; 11: 0.263 / 0.593 / 0.467; 12: 0.270 / 0.542 / 0.450; 13: 0.233 / 0.508 / 0.433; 14: 0.229 / 0.339 / 0.400; 15: 0.252 / 0.610 / 0.350
- 6h: 1: 0.325 / 0.510 / 0.883; 2: 0.338 / 0.552 / 0.864; 3: 0.326 / 0.499 / 0.839; 4: 0.316 / 0.521 / 0.822; 5: 0.320 / 0.487 / 0.783; 6: 0.317 / 0.527 / 0.756; 7: 0.304 / 0.450 / 0.775; 8: 0.299 / 0.459 / 0.786; 9: 0.305 / 0.507 / 0.814; 10: 0.308 / 0.521 / 0.742; 11: 0.302 / 0.476 / 0.797; 12: 0.312 / 0.510 / 0.797; 13: 0.301 / 0.484 / 0.772; 14: 0.308 / 0.482 / 0.756; 15: 0.304 / 0.504 / 0.772
- 24h: 1: 0.351 / 0.507 / 0.901; 2: 0.348 / 0.513 / 0.895; 3: 0.346 / 0.498 / 0.881; 4: 0.341 / 0.499 / 0.883; 5: 0.341 / 0.486 / 0.877; 6: 0.341 / 0.511 / 0.872; 7: 0.333 / 0.480 / 0.865; 8: 0.337 / 0.491 / 0.879; 9: 0.333 / 0.488 / 0.878; 10: 0.338 / 0.509 / 0.865; 11: 0.336 / 0.498 / 0.876; 12: 0.341 / 0.495 / 0.878; 13: 0.339 / 0.517 / 0.880; 14: 0.335 / 0.480 / 0.876; 15: 0.337 / 0.493 / 0.876
- 7d: 1: 0.350 / 0.519 / 0.899; 2: 0.345 / 0.505 / 0.899; 3: 0.345 / 0.511 / 0.898; 4: 0.342 / 0.502 / 0.898; 5: 0.340 / 0.500 / 0.897; 6: 0.340 / 0.498 / 0.896; 7: 0.340 / 0.503 / 0.896; 8: 0.339 / 0.499 / 0.896; 9: 0.335 / 0.492 / 0.896; 10: 0.338 / 0.505 / 0.896; 11: 0.339 / 0.505 / 0.896; 12: 0.341 / 0.512 / 0.896; 13: 0.340 / 0.506 / 0.895; 14: 0.336 / 0.491 / 0.895; 15: 0.337 / 0.495 / 0.895
- 30d: 1: 0.355 / 0.505 / 0.899; 2: 0.351 / 0.498 / 0.899; 3: 0.353 / 0.507 / 0.899; 4: 0.349 / 0.499 / 0.899; 5: 0.349 / 0.501 / 0.899; 6: 0.349 / 0.503 / 0.899; 7: 0.349 / 0.505 / 0.899; 8: 0.348 / 0.504 / 0.899; 9: 0.346 / 0.498 / 0.899; 10: 0.347 / 0.504 / 0.899; 11: 0.346 / 0.502 / 0.899; 12: 0.346 / 0.502 / 0.899; 13: 0.346 / 0.501 / 0.899; 14: 0.344 / 0.495 / 0.899; 15: 0.344 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.052 (body 0.026, range 0.077); 'price stays where it was' would score 0.059; colour right 0.508; typical miss of the close 16.5 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.091 (body 0.055, range 0.126); 'price stays where it was' would score 0.104; colour right 0.496; typical miss of the close 4.2 bp; chain ended on the right side 0.417 of 24 chains; n=360
- 24h: match 0.106 (body 0.069, range 0.143); 'price stays where it was' would score 0.120; colour right 0.487; typical miss of the close 5.6 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.114 (body 0.076, range 0.152); 'price stays where it was' would score 0.119; colour right 0.497; typical miss of the close 6.1 bp; chain ended on the right side 0.516 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 8.0 bp; chain ended on the right side 0.510 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.1; 2: 0.199 / 4.4; 3: 0.168 / 6.0; 4: 0.132 / 6.5; 5: 0.122 / 7.2; 6: 0.111 / 8.1; 7: 0.098 / 8.5; 8: 0.090 / 8.9; 9: 0.085 / 9.2; 10: 0.081 / 10.1; 11: 0.075 / 10.6; 12: 0.072 / 10.9; 13: 0.064 / 11.3; 14: 0.065 / 11.4; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 93488, probability skill vs chance 0.234, widened contest next: False
  - now: threshold 0.8428, hit rate recent 0.9272 / long run 0.9366
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.270, naive rule 0.427, lift 3.70x
    - 24h: 52 calls (52 a day), hit rate 0.885, chance 0.294, naive rule 0.484, lift 3.01x
    - 7d: 407 calls (58 a day), hit rate 0.929, chance 0.293, naive rule 0.489, lift 3.17x
    - 30d: 1698 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.481, lift 3.22x
  - next: threshold 0.5662, hit rate recent 0.6078 / long run 0.5877
    - 6h: 17 calls (69 a day), hit rate 0.412, chance 0.270, lift 1.52x
    - 24h: 51 calls (51 a day), hit rate 0.608, chance 0.294, lift 2.07x
    - 7d: 605 calls (86 a day), hit rate 0.583, chance 0.293, lift 1.99x
    - 30d: 2416 calls (81 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 538, 0.518; 0.40: 487, 0.561; 0.45: 421, 0.626; 0.50: 367, 0.680; 0.55: 322, 0.724; 0.60: 275, 0.766; 0.65: 225, 0.803; 0.70: 182, 0.835; 0.75: 139, 0.871; 0.80: 97, 0.909; 0.85: 48, 0.948; 0.90: 2, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 497, 0.459; 0.40: 413, 0.487; 0.45: 316, 0.519; 0.50: 207, 0.551; 0.55: 93, 0.585; 0.60: 13, 0.620; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 93486, probability skill vs chance 0.2071, widened contest next: True
  - now: threshold 0.7149, hit rate recent 0.8098 / long run 0.8379
    - 6h: 18 calls (73 a day), hit rate 0.833, chance 0.178, naive rule 0.352, lift 4.67x
    - 24h: 53 calls (53 a day), hit rate 0.774, chance 0.192, naive rule 0.398, lift 4.04x
    - 7d: 394 calls (56 a day), hit rate 0.840, chance 0.190, naive rule 0.401, lift 4.41x
    - 30d: 1577 calls (53 a day), hit rate 0.836, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4557, hit rate recent 0.4407 / long run 0.4712
    - 6h: 22 calls (90 a day), hit rate 0.318, chance 0.178, lift 1.78x
    - 24h: 55 calls (55 a day), hit rate 0.436, chance 0.192, lift 2.28x
    - 7d: 733 calls (105 a day), hit rate 0.458, chance 0.190, lift 2.41x
    - 30d: 2105 calls (70 a day), hit rate 0.485, chance 0.186, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 431, 0.411; 0.35: 370, 0.464; 0.40: 299, 0.533; 0.45: 245, 0.591; 0.50: 190, 0.650; 0.55: 144, 0.698; 0.60: 112, 0.739; 0.65: 86, 0.785; 0.70: 64, 0.820; 0.75: 34, 0.864; 0.80: 9, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 254, 0.422; 0.40: 167, 0.448; 0.45: 86, 0.473; 0.50: 21, 0.519; 0.55: 2, 0.597
- **K=8**: model 1791158400, labels learned 93483, probability skill vs chance 0.1906, widened contest next: True
  - now: threshold 0.566, hit rate recent 0.6837 / long run 0.7261
    - 6h: 18 calls (74 a day), hit rate 0.556, chance 0.113, naive rule 0.272, lift 4.92x
    - 24h: 62 calls (62 a day), hit rate 0.677, chance 0.121, naive rule 0.329, lift 5.58x
    - 7d: 377 calls (54 a day), hit rate 0.729, chance 0.126, naive rule 0.338, lift 5.80x
    - 30d: 1571 calls (52 a day), hit rate 0.726, chance 0.121, naive rule 0.325, lift 5.99x
  - next: threshold 0.3472, hit rate recent 0.3449 / long run 0.4008
    - 6h: 28 calls (115 a day), hit rate 0.250, chance 0.113, lift 2.22x
    - 24h: 94 calls (95 a day), hit rate 0.372, chance 0.121, lift 3.07x
    - 7d: 502 calls (72 a day), hit rate 0.394, chance 0.126, lift 3.13x
    - 30d: 2052 calls (68 a day), hit rate 0.402, chance 0.121, lift 3.32x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 274, 0.399; 0.35: 206, 0.474; 0.40: 159, 0.535; 0.45: 126, 0.584; 0.50: 96, 0.627; 0.55: 68, 0.685; 0.60: 46, 0.730; 0.65: 24, 0.769; 0.70: 9, 0.807; 0.75: 1, 0.828
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 187, 0.344; 0.35: 116, 0.383; 0.40: 48, 0.413; 0.45: 10, 0.421; 0.50: 1, 0.410
- **K=13**: model 1791072000, labels learned 93478, probability skill vs chance 0.1746, widened contest next: True
  - now: threshold 0.4212, hit rate recent 0.5527 / long run 0.5843
    - 6h: 16 calls (67 a day), hit rate 0.562, chance 0.075, naive rule 0.224, lift 7.46x
    - 24h: 57 calls (58 a day), hit rate 0.561, chance 0.072, naive rule 0.250, lift 7.77x
    - 7d: 394 calls (56 a day), hit rate 0.586, chance 0.078, naive rule 0.270, lift 7.49x
    - 30d: 1482 calls (49 a day), hit rate 0.584, chance 0.077, naive rule 0.265, lift 7.64x
  - next: threshold 0.278, hit rate recent 0.3063 / long run 0.3041
    - 6h: 27 calls (113 a day), hit rate 0.296, chance 0.075, lift 3.93x
    - 24h: 79 calls (80 a day), hit rate 0.316, chance 0.072, lift 4.38x
    - 7d: 603 calls (86 a day), hit rate 0.300, chance 0.078, lift 3.84x
    - 30d: 2043 calls (68 a day), hit rate 0.307, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.436; 0.35: 90, 0.494; 0.40: 64, 0.544; 0.45: 44, 0.603; 0.50: 28, 0.619; 0.55: 15, 0.672; 0.60: 6, 0.705; 0.65: 2, 0.750; 0.70: 0, 0.600
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.314; 0.35: 17, 0.353; 0.40: 4, 0.336; 0.45: 1, 0.381

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 33.957 | 16.90% | 0.750 | 0.400 | 0.246 | 0.525 | 0.553 |
| 6h | 10.443 | 11.73% | 0.867 | 0.461 | 0.251 | 0.476 | 0.644 |
| 24h | 9.821 | 5.25% | 0.896 | 0.497 | 0.251 | 0.479 | 0.598 |
| 7d | 10.880 | 4.96% | 0.900 | 0.499 | 0.251 | 0.494 | 0.671 |
| 30d | 14.116 | 4.22% | 0.900 | 0.500 | 0.251 | 0.497 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 40.861 | 35.192 | 34.033 | 35.112 | 32.324 | 37.012 | 33.949 | 34.105 | 34.050 | 33.957 |
| 6h | 11.832 | 10.652 | 10.466 | 10.655 | 10.267 | 11.015 | 10.423 | 10.444 | 10.442 | 10.443 |
| 24h | 10.364 | 9.934 | 9.856 | 9.872 | 9.910 | 10.049 | 9.831 | 9.833 | 9.813 | 9.821 |
| 7d | 11.447 | 10.979 | 10.966 | 10.918 | 11.099 | 11.088 | 10.876 | 10.871 | 10.863 | 10.880 |
| 30d | 14.739 | 14.246 | 14.198 | 14.145 | 14.384 | 14.334 | 14.119 | 14.092 | 14.090 | 14.116 |

## Next candle

- candle starting 2026-10-07 02:14 UTC, last close 2614.66
- P(up) 0.4143, return quantiles (bp): {'05': -42.683, '10': -33.463, '25': -18.816, '40': -7.371, '50': -2.391, '60': 0.467, '75': 7.111, '90': 21.479, '95': 30.225}
- changepoint probability 0.2164, regime age 16.2 min
- agent weights: empirical 0.003, ewma 0.019, garch 0.118, har 0.027, bocpd 0.496, hmm 0.003, online_qr 0.188, lgbm 0.146

## Learning log

- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.74, 3.96, 8.7], current probabilities: [0.01, 0.322, 0.669]
- live generator: {'versions': 60, 'latest_effective': '2026-10-07 02:25 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.201, 'l_abs': 0.651, 'l_hi': 0.732, 'l_lo': 0.731, 'b05': 0.696, 'b25': 0.592, 'b75': 0.655, 'b95': 0.721}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.917, 2.76, 3.46, 4.548, 5.742, 6.869, 6.929, 7.075, 8.596, 7.545, 7.587, 8.236, 9.851, 9.244]}
- calibration offsets (in sigma): {'05': -0.0835, '10': -0.117, '25': -0.1475, '40': -0.048, '50': -0.045, '60': -0.092, '75': -0.0725, '90': -0.013, '95': -0.0465}
