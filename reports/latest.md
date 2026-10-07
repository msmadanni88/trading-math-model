# ETH-USD 60s candle generator - report

- generated: 2026-10-07 08:48 UTC
- last closed candle: 2026-10-07 08:48 UTC (staleness 0.8 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.562 (96) | 0.524 (670) [0.487, 0.563] | 0.510 (2875) [0.490, 0.530] | 0.515 (3355) [0.497, 0.531] | 0.540 (383) [0.482, 0.599] | 0.400 (35) | 0.500 | flat -0.007 (noise 0.035) |
| colour_clear | 0.523 (776) | 0.520 (5262) [0.498, 0.541] | 0.503 (23269) [0.497, 0.510] | 0.502 (27175) [0.496, 0.508] | 0.547 (2937) [0.534, 0.559] | 0.545 (264) | 0.500 | flat +0.025 (noise 0.013) |
| colour_confident | 0.518 (168) | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.608 (615) [0.552, 0.668] | 0.596 (52) | 0.500 | - |
| colour_next | 0.511 (1423) | 0.519 (9981) [0.506, 0.532] | 0.505 (42883) [0.500, 0.510] | 0.504 (50023) [0.499, 0.509] | 0.533 (5674) [0.518, 0.549] | 0.535 (525) | 0.500 | up +0.021 (noise 0.009) |
| colour_path | 0.498 (19922) | 0.502 (139734) [0.498, 0.506] | 0.501 (600362) [0.500, 0.503] | 0.501 (700322) [0.500, 0.502] | 0.501 (79436) [0.496, 0.506] | 0.491 (7350) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.513 (39) | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.633 (169) [0.576, 0.699] | 0.846 (13) | 0.500 | - |
| reversal_k13_next | 0.324 (71) | 0.301 (598) [0.277, 0.324] | 0.308 (2033) [0.293, 0.324] | 0.303 (2437) [0.289, 0.318] | 0.325 (332) [0.306, 0.344] | 0.261 (23) | 0.077 | flat +0.016 (noise 0.028) |
| reversal_k13_now | 0.508 (63) | 0.587 (392) [0.546, 0.634] | 0.583 (1481) [0.560, 0.607] | 0.583 (1713) [0.563, 0.603] | 0.593 (241) [0.534, 0.664] | 0.643 (14) | 0.077 | flat -0.005 (noise 0.039) |
| reversal_k3_next | 0.689 (45) | 0.587 (605) [0.562, 0.621] | 0.586 (2414) [0.570, 0.602] | 0.588 (2802) [0.575, 0.602] | 0.591 (362) [0.563, 0.661] | 0.400 (20) | 0.292 | flat +0.022 (noise 0.032) |
| reversal_k3_now | 0.902 (61) | 0.929 (411) [0.920, 0.939] | 0.939 (1701) [0.930, 0.949] | 0.940 (1993) [0.932, 0.948] | 0.926 (230) [0.912, 0.943] | 1.000 (13) | 0.293 | flat -0.018 (noise 0.017) |
| reversal_k5_next | 0.490 (49) | 0.463 (723) [0.432, 0.495] | 0.486 (2101) [0.466, 0.507] | 0.487 (2387) [0.470, 0.505] | 0.453 (397) [0.424, 0.510] | 0.217 (23) | 0.187 | flat -0.046 (noise 0.036) |
| reversal_k5_now | 0.768 (56) | 0.843 (394) [0.816, 0.866] | 0.837 (1579) [0.822, 0.853] | 0.838 (1841) [0.823, 0.851] | 0.839 (230) [0.795, 0.879] | 0.692 (13) | 0.187 | flat -0.007 (noise 0.027) |
| reversal_k8_next | 0.416 (89) | 0.400 (495) [0.367, 0.430] | 0.404 (2043) [0.387, 0.423] | 0.398 (2433) [0.383, 0.415] | 0.410 (327) [0.374, 0.448] | 0.250 (36) | 0.122 | flat +0.002 (noise 0.033) |
| reversal_k8_now | 0.651 (66) | 0.734 (376) [0.700, 0.766] | 0.726 (1570) [0.708, 0.745] | 0.718 (1824) [0.699, 0.736] | 0.743 (237) [0.707, 0.781] | 0.765 (17) | 0.122 | flat -0.018 (noise 0.033) |
| overall | 0.501 (21941) | 0.505 (154379) [0.501, 0.509] | 0.504 (661042) [0.502, 0.505] | 0.503 (771130) [0.502, 0.504] | 0.505 (87849) [0.500, 0.512] | 0.492 (8069) | - | flat +0.003 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07767, 0.1153] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5324, 'levels': [{'threshold': 0.07767, 'calls_per_day': 143.4, 'win_rate': 0.5848}, {'threshold': 0.1153, 'calls_per_day': 35.6, 'win_rate': 0.6349}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 5067, 'rate': 0.5388}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15057 | 0.334 | 0.514 (14839) | 0.611 (591) | 0.778 (2430) |
| volatility: normal | 15055 | 0.359 | 0.507 (14988) | 0.552 (58) | 0.776 (2112) |
| volatility: wild | 15056 | 0.373 | 0.494 (15010) | - | 0.775 (2083) |
| session: Asia 00-08 | 15360 | 0.352 | 0.505 (15255) | 0.605 (253) | 0.775 (2200) |
| session: Europe 08-13 | 9348 | 0.349 | 0.502 (9286) | 0.547 (117) | 0.770 (1440) |
| session: US 13-21 | 14880 | 0.365 | 0.505 (14778) | 0.611 (185) | 0.786 (2200) |
| session: late 21-24 | 5580 | 0.351 | 0.510 (5518) | 0.670 (112) | 0.762 (785) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.394 | 0.371 | 0.307 | 0.307 | 0.567 | 0.283 | 0.505 | 1.156 |
| 6h | 360 | 0.361 | 0.342 | 0.281 | 0.322 | 0.550 | 0.272 | 0.450 | 1.262 |
| 24h | 1440 | 0.349 | 0.346 | 0.285 | 0.313 | 0.504 | 0.243 | 0.454 | 1.233 |
| 7d | 10080 | 0.350 | 0.346 | 0.274 | 0.298 | 0.519 | 0.246 | 0.454 | 1.249 |
| 30d | 43200 | 0.356 | 0.354 | 0.278 | 0.308 | 0.506 | 0.247 | 0.464 | 1.290 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.394 / 0.567 / 0.833; 2: 0.360 / 0.450 / 0.967; 3: 0.383 / 0.550 / 0.983; 4: 0.410 / 0.600 / 1.000; 5: 0.391 / 0.533 / 1.000; 6: 0.380 / 0.550 / 1.000; 7: 0.382 / 0.500 / 1.000; 8: 0.360 / 0.483 / 1.000; 9: 0.334 / 0.350 / 1.000; 10: 0.363 / 0.433 / 1.000; 11: 0.337 / 0.400 / 1.000; 12: 0.364 / 0.500 / 1.000; 13: 0.385 / 0.533 / 1.000; 14: 0.378 / 0.500 / 1.000; 15: 0.376 / 0.533 / 1.000
- 6h: 1: 0.361 / 0.550 / 0.906; 2: 0.348 / 0.492 / 0.983; 3: 0.346 / 0.511 / 0.992; 4: 0.352 / 0.539 / 0.997; 5: 0.338 / 0.503 / 1.000; 6: 0.342 / 0.517 / 1.000; 7: 0.339 / 0.483 / 1.000; 8: 0.333 / 0.466 / 1.000; 9: 0.329 / 0.464 / 1.000; 10: 0.336 / 0.478 / 1.000; 11: 0.336 / 0.466 / 1.000; 12: 0.342 / 0.506 / 1.000; 13: 0.326 / 0.458 / 1.000; 14: 0.345 / 0.528 / 1.000; 15: 0.335 / 0.480 / 1.000
- 24h: 1: 0.349 / 0.504 / 0.904; 2: 0.349 / 0.511 / 0.909; 3: 0.346 / 0.505 / 0.910; 4: 0.343 / 0.510 / 0.908; 5: 0.341 / 0.489 / 0.905; 6: 0.342 / 0.511 / 0.899; 7: 0.333 / 0.477 / 0.900; 8: 0.337 / 0.493 / 0.897; 9: 0.331 / 0.482 / 0.897; 10: 0.339 / 0.506 / 0.908; 11: 0.337 / 0.489 / 0.902; 12: 0.344 / 0.509 / 0.903; 13: 0.331 / 0.490 / 0.903; 14: 0.338 / 0.503 / 0.896; 15: 0.336 / 0.493 / 0.900
- 7d: 1: 0.350 / 0.519 / 0.899; 2: 0.344 / 0.502 / 0.902; 3: 0.345 / 0.511 / 0.902; 4: 0.341 / 0.503 / 0.902; 5: 0.339 / 0.499 / 0.901; 6: 0.339 / 0.498 / 0.900; 7: 0.339 / 0.503 / 0.899; 8: 0.338 / 0.496 / 0.900; 9: 0.334 / 0.491 / 0.900; 10: 0.337 / 0.505 / 0.900; 11: 0.338 / 0.505 / 0.900; 12: 0.340 / 0.512 / 0.900; 13: 0.338 / 0.504 / 0.899; 14: 0.336 / 0.494 / 0.899; 15: 0.335 / 0.494 / 0.899
- 30d: 1: 0.356 / 0.506 / 0.899; 2: 0.351 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.349 / 0.499 / 0.900; 5: 0.349 / 0.501 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.348 / 0.505 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.346 / 0.498 / 0.900; 10: 0.347 / 0.504 / 0.900; 11: 0.346 / 0.501 / 0.900; 12: 0.346 / 0.503 / 0.900; 13: 0.346 / 0.501 / 0.900; 14: 0.344 / 0.495 / 0.900; 15: 0.344 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.104 (body 0.034, range 0.173); 'price stays where it was' would score 0.176; colour right 0.417; typical miss of the close 6.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.094 (body 0.056, range 0.131); 'price stays where it was' would score 0.127; colour right 0.475; typical miss of the close 9.0 bp; chain ended on the right side 0.500 of 24 chains; n=360
- 24h: match 0.105 (body 0.067, range 0.144); 'price stays where it was' would score 0.124; colour right 0.479; typical miss of the close 6.5 bp; chain ended on the right side 0.521 of 96 chains; n=1440
- 7d: match 0.114 (body 0.076, range 0.152); 'price stays where it was' would score 0.119; colour right 0.498; typical miss of the close 6.2 bp; chain ended on the right side 0.518 of 670 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.158); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.510 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.2; 2: 0.198 / 4.4; 3: 0.168 / 6.0; 4: 0.131 / 6.6; 5: 0.121 / 7.3; 6: 0.110 / 8.1; 7: 0.098 / 8.5; 8: 0.090 / 9.0; 9: 0.084 / 9.2; 10: 0.080 / 10.1; 11: 0.074 / 10.6; 12: 0.072 / 11.0; 13: 0.063 / 11.3; 14: 0.065 / 11.3; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 93882, probability skill vs chance 0.2276, widened contest next: False
  - now: threshold 0.8423, hit rate recent 0.9394 / long run 0.9378
    - 6h: 11 calls (45 a day), hit rate 1.000, chance 0.299, naive rule 0.516, lift 3.35x
    - 24h: 45 calls (45 a day), hit rate 0.978, chance 0.301, naive rule 0.501, lift 3.25x
    - 7d: 406 calls (58 a day), hit rate 0.931, chance 0.294, naive rule 0.490, lift 3.17x
    - 30d: 1697 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.564, hit rate recent 0.5897 / long run 0.5862
    - 6h: 9 calls (37 a day), hit rate 0.444, chance 0.299, lift 1.49x
    - 24h: 50 calls (50 a day), hit rate 0.600, chance 0.301, lift 1.99x
    - 7d: 588 calls (84 a day), hit rate 0.577, chance 0.294, lift 1.96x
    - 30d: 2405 calls (80 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 537, 0.518; 0.40: 487, 0.561; 0.45: 420, 0.627; 0.50: 367, 0.680; 0.55: 322, 0.723; 0.60: 275, 0.765; 0.65: 225, 0.802; 0.70: 182, 0.834; 0.75: 139, 0.870; 0.80: 97, 0.909; 0.85: 48, 0.948; 0.90: 2, 0.981
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.423; 0.35: 497, 0.458; 0.40: 413, 0.488; 0.45: 316, 0.519; 0.50: 207, 0.552; 0.55: 92, 0.584; 0.60: 13, 0.616; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 93880, probability skill vs chance 0.2034, widened contest next: True
  - now: threshold 0.7133, hit rate recent 0.7997 / long run 0.8365
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.178, naive rule 0.389, lift 4.00x
    - 24h: 50 calls (50 a day), hit rate 0.780, chance 0.190, naive rule 0.395, lift 4.10x
    - 7d: 388 calls (55 a day), hit rate 0.838, chance 0.191, naive rule 0.399, lift 4.40x
    - 30d: 1572 calls (52 a day), hit rate 0.836, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4559, hit rate recent 0.4178 / long run 0.4683
    - 6h: 8 calls (33 a day), hit rate 0.250, chance 0.178, lift 1.40x
    - 24h: 56 calls (56 a day), hit rate 0.429, chance 0.190, lift 2.25x
    - 7d: 733 calls (105 a day), hit rate 0.456, chance 0.191, lift 2.39x
    - 30d: 2097 calls (70 a day), hit rate 0.485, chance 0.186, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 431, 0.412; 0.35: 369, 0.465; 0.40: 299, 0.535; 0.45: 244, 0.593; 0.50: 190, 0.650; 0.55: 144, 0.698; 0.60: 112, 0.739; 0.65: 86, 0.785; 0.70: 63, 0.820; 0.75: 34, 0.863; 0.80: 9, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 253, 0.422; 0.40: 166, 0.448; 0.45: 86, 0.474; 0.50: 21, 0.519; 0.55: 2, 0.597
- **K=8**: model 1791158400, labels learned 93877, probability skill vs chance 0.1888, widened contest next: True
  - now: threshold 0.5664, hit rate recent 0.721 / long run 0.7294
    - 6h: 10 calls (41 a day), hit rate 0.900, chance 0.111, naive rule 0.325, lift 8.08x
    - 24h: 56 calls (56 a day), hit rate 0.714, chance 0.119, naive rule 0.326, lift 6.03x
    - 7d: 380 calls (54 a day), hit rate 0.732, chance 0.126, naive rule 0.337, lift 5.82x
    - 30d: 1566 calls (52 a day), hit rate 0.726, chance 0.121, naive rule 0.325, lift 6.00x
  - next: threshold 0.3473, hit rate recent 0.3412 / long run 0.3991
    - 6h: 18 calls (74 a day), hit rate 0.278, chance 0.111, lift 2.49x
    - 24h: 90 calls (91 a day), hit rate 0.378, chance 0.119, lift 3.19x
    - 7d: 504 calls (72 a day), hit rate 0.391, chance 0.126, lift 3.11x
    - 30d: 2052 calls (68 a day), hit rate 0.400, chance 0.121, lift 3.31x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 273, 0.400; 0.35: 206, 0.474; 0.40: 159, 0.535; 0.45: 125, 0.583; 0.50: 96, 0.626; 0.55: 68, 0.685; 0.60: 46, 0.730; 0.65: 24, 0.770; 0.70: 8, 0.809; 0.75: 1, 0.815
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 186, 0.344; 0.35: 116, 0.384; 0.40: 48, 0.411; 0.45: 10, 0.421; 0.50: 1, 0.410
- **K=13**: model 1791072000, labels learned 93872, probability skill vs chance 0.1745, widened contest next: False
  - now: threshold 0.4215, hit rate recent 0.5692 / long run 0.5855
    - 6h: 7 calls (29 a day), hit rate 0.714, chance 0.074, naive rule 0.268, lift 9.66x
    - 24h: 52 calls (53 a day), hit rate 0.577, chance 0.073, naive rule 0.254, lift 7.90x
    - 7d: 391 calls (56 a day), hit rate 0.591, chance 0.078, naive rule 0.271, lift 7.55x
    - 30d: 1479 calls (49 a day), hit rate 0.585, chance 0.077, naive rule 0.266, lift 7.63x
  - next: threshold 0.278, hit rate recent 0.3096 / long run 0.3045
    - 6h: 8 calls (33 a day), hit rate 0.375, chance 0.074, lift 5.07x
    - 24h: 68 calls (69 a day), hit rate 0.338, chance 0.073, lift 4.63x
    - 7d: 582 calls (83 a day), hit rate 0.302, chance 0.078, lift 3.86x
    - 30d: 2036 calls (68 a day), hit rate 0.308, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.437; 0.35: 90, 0.495; 0.40: 64, 0.544; 0.45: 44, 0.603; 0.50: 28, 0.622; 0.55: 15, 0.676; 0.60: 6, 0.704; 0.65: 2, 0.755; 0.70: 0, 0.600
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.314; 0.35: 17, 0.353; 0.40: 4, 0.333; 0.45: 1, 0.381

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 9.864 | -0.68% | 0.850 | 0.450 | 0.252 | 0.417 | 0.065 |
| 6h | 9.940 | -1.02% | 0.914 | 0.514 | 0.252 | 0.469 | 0.277 |
| 24h | 10.806 | 4.06% | 0.899 | 0.501 | 0.252 | 0.477 | 0.568 |
| 7d | 10.888 | 4.87% | 0.901 | 0.500 | 0.251 | 0.491 | 0.667 |
| 30d | 14.095 | 4.21% | 0.900 | 0.500 | 0.251 | 0.497 | 0.692 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.797 | 9.973 | 9.924 | 9.788 | 9.887 | 9.847 | 9.862 | 9.833 | 9.856 | 9.864 |
| 6h | 9.840 | 10.139 | 9.838 | 10.087 | 9.920 | 9.848 | 10.172 | 10.034 | 9.906 | 9.940 |
| 24h | 11.263 | 10.972 | 10.798 | 10.871 | 10.850 | 10.945 | 10.862 | 10.823 | 10.783 | 10.806 |
| 7d | 11.446 | 10.996 | 10.969 | 10.928 | 11.102 | 11.082 | 10.890 | 10.879 | 10.868 | 10.888 |
| 30d | 14.714 | 14.225 | 14.175 | 14.124 | 14.361 | 14.310 | 14.099 | 14.071 | 14.068 | 14.095 |

## Next candle

- candle starting 2026-10-07 08:48 UTC, last close 2611.51
- P(up) 0.5116, return quantiles (bp): {'05': -5.694, '10': -4.324, '25': -2.172, '40': -0.767, '50': 0.099, '60': 0.845, '75': 1.873, '90': 3.993, '95': 5.305}
- changepoint probability 0.0448, regime age 247.8 min
- agent weights: empirical 0.003, ewma 0.025, garch 0.304, har 0.049, bocpd 0.294, hmm 0.049, online_qr 0.099, lgbm 0.177

## Learning log

- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- 2026-10-07 00:00 UTC: {"garch": {"alpha": 0.0675, "beta": 0.9232}, "hmm": {"sd_bp": [1.74, 3.96, 8.7], "stay": [0.963, 0.928, 0.915]}, "lgbm": {"challenger_loss": 0.24856, "champion_loss": 0.24858, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48363, "challengers": 1, "chance_loss": 0.61694, "widened": false, "champion_loss": 0.48301, "promoted": false}, "reversal_k5": {"challenger_loss": 0.39181, "challengers": 1, "chance_loss": 0.50106, "widened": false, "champion_loss": 0.38872, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28494, "challengers": 1, "chance_loss": 0.37527, "widened": false, "champion_loss": 0.28479, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.26599, "widened": false, "champion_loss": 0.19636, "promoted": false}}
- HMM volatility states (sd, bp per minute): [1.74, 3.96, 8.7], current probabilities: [0.584, 0.409, 0.007]
- live generator: {'versions': 60, 'latest_effective': '2026-10-07 09:00 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.21, 'l_abs': 0.638, 'l_hi': 0.694, 'l_lo': 0.708, 'b05': 0.658, 'b25': 0.574, 'b75': 0.592, 'b95': 0.687}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.2, 1.8], [1.3, 1.6]], 'cone_width': [1.003, 1.36, 1.605, 2.068, 2.611, 3.124, 3.151, 3.218, 3.909, 3.431, 3.45, 3.745, 4.57, 4.376]}
- calibration offsets (in sigma): {'05': -0.0365, '10': -0.053, '25': -0.0225, '40': -0.012, '50': 0.015, '60': 0.022, '75': -0.0575, '90': -0.067, '95': -0.0735}
