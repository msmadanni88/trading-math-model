# ETH-USD 60s candle generator - report

- generated: 2026-10-11 07:04 UTC
- last closed candle: 2026-10-11 07:04 UTC (staleness 0.9 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=8: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.508 (671) [0.454, 0.562] | 0.508 (2875) [0.488, 0.529] | 0.511 (3739) [0.494, 0.528] | 0.511 (767) [0.465, 0.557] | 0.607 (28) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.537 (778) | 0.545 (5363) [0.536, 0.553] | 0.510 (23183) [0.502, 0.518] | 0.506 (30322) [0.500, 0.512] | 0.545 (6084) [0.538, 0.552] | 0.514 (216) | 0.500 | up +0.044 (noise 0.010) |
| colour_confident | 0.567 (275) | 0.607 (1140) [0.574, 0.646] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.589 (73) | 0.500 | flat -0.000 (noise 0.055) |
| colour_next | 0.529 (1387) | 0.530 (9958) [0.521, 0.539] | 0.508 (42835) [0.502, 0.513] | 0.506 (55711) [0.501, 0.511] | 0.529 (11362) [0.521, 0.537] | 0.516 (415) | 0.500 | up +0.023 (noise 0.007) |
| colour_path | 0.500 (19418) | 0.500 (139412) [0.497, 0.503] | 0.501 (599690) [0.500, 0.502] | 0.500 (779954) [0.499, 0.502] | 0.499 (159068) [0.496, 0.502] | 0.509 (5810) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.648 (88) | 0.656 (305) [0.602, 0.720] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.625 (24) | 0.500 | - |
| reversal_k13_next | 0.361 (72) | 0.329 (511) [0.312, 0.345] | 0.312 (2046) [0.297, 0.328] | 0.306 (2718) [0.293, 0.320] | 0.328 (613) [0.314, 0.341] | 0.308 (26) | 0.077 | flat +0.053 (noise 0.027) |
| reversal_k13_now | 0.576 (59) | 0.575 (400) [0.548, 0.604] | 0.587 (1490) [0.565, 0.612] | 0.584 (1917) [0.566, 0.602] | 0.593 (445) [0.559, 0.637] | 0.556 (18) | 0.077 | flat -0.019 (noise 0.039) |
| reversal_k3_next | 0.620 (129) | 0.591 (557) [0.559, 0.621] | 0.586 (2386) [0.571, 0.602] | 0.586 (3141) [0.573, 0.598] | 0.579 (701) [0.550, 0.610] | 0.512 (41) | 0.293 | flat +0.013 (noise 0.028) |
| reversal_k3_now | 0.910 (67) | 0.923 (418) [0.914, 0.936] | 0.940 (1718) [0.931, 0.947] | 0.938 (2238) [0.931, 0.945] | 0.924 (475) [0.916, 0.935] | 0.920 (25) | 0.293 | flat -0.022 (noise 0.017) |
| reversal_k5_next | 0.507 (73) | 0.471 (480) [0.441, 0.496] | 0.485 (2092) [0.467, 0.503] | 0.484 (2659) [0.467, 0.501] | 0.453 (669) [0.425, 0.487] | 0.438 (16) | 0.187 | flat +0.019 (noise 0.030) |
| reversal_k5_now | 0.873 (63) | 0.827 (387) [0.791, 0.861] | 0.838 (1590) [0.823, 0.853] | 0.835 (2059) [0.821, 0.849] | 0.826 (448) [0.795, 0.855] | 0.812 (16) | 0.187 | flat -0.031 (noise 0.026) |
| reversal_k8_next | 0.449 (69) | 0.396 (613) [0.367, 0.429] | 0.407 (2098) [0.389, 0.427] | 0.396 (2796) [0.382, 0.411] | 0.394 (690) [0.369, 0.422] | 0.214 (28) | 0.122 | flat +0.016 (noise 0.031) |
| reversal_k8_now | 0.770 (61) | 0.699 (418) [0.654, 0.741] | 0.722 (1585) [0.703, 0.742] | 0.712 (2055) [0.694, 0.731] | 0.707 (468) [0.665, 0.745] | 0.526 (19) | 0.122 | flat -0.037 (noise 0.034) |
| overall | 0.506 (21494) | 0.504 (153825) [0.500, 0.508] | 0.504 (660405) [0.502, 0.505] | 0.503 (858987) [0.501, 0.504] | 0.503 (175706) [0.499, 0.507] | 0.510 (6442) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08115, 0.1227] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5285, 'levels': [{'threshold': 0.08115, 'calls_per_day': 144.5, 'win_rate': 0.6025}, {'threshold': 0.1227, 'calls_per_day': 36.7, 'win_rate': 0.6577}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 10643, 'rate': 0.5304}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15022 | 0.331 | 0.517 (14757) | 0.597 (1034) | 0.778 (2438) |
| volatility: normal | 15021 | 0.359 | 0.510 (14948) | 0.631 (195) | 0.777 (2165) |
| volatility: wild | 15021 | 0.374 | 0.496 (14976) | 0.676 (68) | 0.775 (2085) |
| session: Asia 00-08 | 15304 | 0.351 | 0.510 (15188) | 0.595 (494) | 0.778 (2208) |
| session: Europe 08-13 | 9300 | 0.348 | 0.505 (9211) | 0.596 (282) | 0.769 (1471) |
| session: US 13-21 | 14880 | 0.364 | 0.505 (14773) | 0.588 (325) | 0.783 (2198) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5509) | 0.679 (196) | 0.767 (811) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.327 | 0.292 | 0.200 | 0.200 | 0.633 | 0.270 | 0.384 | 1.887 |
| 6h | 360 | 0.311 | 0.318 | 0.233 | 0.251 | 0.520 | 0.243 | 0.378 | 1.246 |
| 24h | 1440 | 0.314 | 0.306 | 0.233 | 0.254 | 0.527 | 0.247 | 0.382 | 1.250 |
| 7d | 10080 | 0.352 | 0.346 | 0.272 | 0.298 | 0.528 | 0.257 | 0.447 | 1.197 |
| 30d | 43200 | 0.354 | 0.353 | 0.277 | 0.306 | 0.508 | 0.247 | 0.461 | 1.301 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.327 / 0.633 / 0.917; 2: 0.315 / 0.550 / 0.900; 3: 0.304 / 0.550 / 0.900; 4: 0.259 / 0.383 / 0.900; 5: 0.298 / 0.583 / 0.867; 6: 0.252 / 0.367 / 0.883; 7: 0.308 / 0.617 / 0.900; 8: 0.281 / 0.550 / 0.917; 9: 0.289 / 0.450 / 0.900; 10: 0.271 / 0.467 / 0.900; 11: 0.271 / 0.400 / 0.900; 12: 0.314 / 0.633 / 0.900; 13: 0.280 / 0.483 / 0.900; 14: 0.275 / 0.533 / 0.883; 15: 0.270 / 0.417 / 0.883
- 6h: 1: 0.311 / 0.520 / 0.886; 2: 0.319 / 0.548 / 0.853; 3: 0.300 / 0.486 / 0.872; 4: 0.298 / 0.500 / 0.883; 5: 0.310 / 0.540 / 0.867; 6: 0.301 / 0.525 / 0.839; 7: 0.300 / 0.494 / 0.833; 8: 0.307 / 0.523 / 0.847; 9: 0.300 / 0.497 / 0.819; 10: 0.299 / 0.483 / 0.831; 11: 0.311 / 0.528 / 0.808; 12: 0.294 / 0.475 / 0.861; 13: 0.309 / 0.514 / 0.828; 14: 0.296 / 0.480 / 0.800; 15: 0.296 / 0.511 / 0.767
- 24h: 1: 0.314 / 0.527 / 0.883; 2: 0.306 / 0.488 / 0.894; 3: 0.304 / 0.519 / 0.897; 4: 0.299 / 0.494 / 0.896; 5: 0.311 / 0.541 / 0.892; 6: 0.300 / 0.493 / 0.884; 7: 0.298 / 0.497 / 0.879; 8: 0.300 / 0.503 / 0.885; 9: 0.300 / 0.493 / 0.880; 10: 0.303 / 0.508 / 0.878; 11: 0.301 / 0.498 / 0.875; 12: 0.299 / 0.499 / 0.879; 13: 0.301 / 0.510 / 0.874; 14: 0.297 / 0.491 / 0.871; 15: 0.300 / 0.508 / 0.867
- 7d: 1: 0.352 / 0.528 / 0.897; 2: 0.342 / 0.500 / 0.899; 3: 0.343 / 0.510 / 0.900; 4: 0.341 / 0.503 / 0.899; 5: 0.340 / 0.506 / 0.899; 6: 0.337 / 0.498 / 0.898; 7: 0.337 / 0.501 / 0.898; 8: 0.337 / 0.497 / 0.899; 9: 0.334 / 0.489 / 0.898; 10: 0.337 / 0.503 / 0.898; 11: 0.336 / 0.494 / 0.898; 12: 0.336 / 0.499 / 0.898; 13: 0.338 / 0.509 / 0.897; 14: 0.335 / 0.501 / 0.897; 15: 0.337 / 0.500 / 0.896
- 30d: 1: 0.354 / 0.508 / 0.898; 2: 0.349 / 0.497 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.348 / 0.500 / 0.900; 5: 0.348 / 0.505 / 0.900; 6: 0.347 / 0.502 / 0.900; 7: 0.346 / 0.504 / 0.899; 8: 0.346 / 0.503 / 0.900; 9: 0.343 / 0.496 / 0.899; 10: 0.345 / 0.504 / 0.899; 11: 0.344 / 0.501 / 0.899; 12: 0.344 / 0.502 / 0.899; 13: 0.344 / 0.501 / 0.899; 14: 0.343 / 0.497 / 0.899; 15: 0.342 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.131 (body 0.108, range 0.153); 'price stays where it was' would score 0.091; colour right 0.483; typical miss of the close 2.1 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.093 (body 0.069, range 0.117); 'price stays where it was' would score 0.086; colour right 0.492; typical miss of the close 4.4 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.112 (body 0.082, range 0.142); 'price stays where it was' would score 0.120; colour right 0.498; typical miss of the close 3.9 bp; chain ended on the right side 0.594 of 96 chains; n=1440
- 7d: match 0.117 (body 0.080, range 0.153); 'price stays where it was' would score 0.122; colour right 0.498; typical miss of the close 6.2 bp; chain ended on the right side 0.504 of 671 chains; n=10080
- 30d: match 0.119 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.7 bp; chain ended on the right side 0.509 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.362 / 3.9; 2: 0.199 / 4.3; 3: 0.166 / 5.9; 4: 0.133 / 6.4; 5: 0.121 / 7.0; 6: 0.110 / 7.6; 7: 0.102 / 8.1; 8: 0.092 / 8.4; 9: 0.086 / 8.7; 10: 0.080 / 9.4; 11: 0.076 / 9.9; 12: 0.075 / 10.4; 13: 0.063 / 10.8; 14: 0.065 / 10.8; 15: 0.061 / 10.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 99538, probability skill vs chance 0.2247, widened contest next: False
  - now: threshold 0.8176, hit rate recent 0.914 / long run 0.9306
    - 6h: 21 calls (85 a day), hit rate 0.905, chance 0.327, naive rule 0.553, lift 2.77x
    - 24h: 70 calls (70 a day), hit rate 0.929, chance 0.321, naive rule 0.531, lift 2.90x
    - 7d: 424 calls (61 a day), hit rate 0.922, chance 0.296, naive rule 0.493, lift 3.11x
    - 30d: 1730 calls (58 a day), hit rate 0.939, chance 0.292, naive rule 0.483, lift 3.22x
  - next: threshold 0.5608, hit rate recent 0.58 / long run 0.5803
    - 6h: 38 calls (154 a day), hit rate 0.500, chance 0.327, lift 1.53x
    - 24h: 139 calls (139 a day), hit rate 0.604, chance 0.321, lift 1.89x
    - 7d: 571 calls (82 a day), hit rate 0.580, chance 0.296, lift 1.96x
    - 30d: 2402 calls (80 a day), hit rate 0.586, chance 0.292, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 538, 0.517; 0.40: 486, 0.563; 0.45: 418, 0.629; 0.50: 365, 0.684; 0.55: 321, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.802; 0.70: 181, 0.835; 0.75: 139, 0.874; 0.80: 97, 0.913; 0.85: 49, 0.948; 0.90: 2, 0.973
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.425; 0.35: 498, 0.459; 0.40: 413, 0.487; 0.45: 317, 0.519; 0.50: 206, 0.553; 0.55: 92, 0.582; 0.60: 14, 0.603; 0.65: 1, 0.696
- **K=5**: model 1791590400, labels learned 99536, probability skill vs chance 0.2135, widened contest next: False
  - now: threshold 0.7126, hit rate recent 0.8517 / long run 0.8319
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.214, naive rule 0.434, lift 4.01x
    - 24h: 61 calls (61 a day), hit rate 0.902, chance 0.208, naive rule 0.446, lift 4.34x
    - 7d: 384 calls (55 a day), hit rate 0.820, chance 0.192, naive rule 0.400, lift 4.27x
    - 30d: 1596 calls (53 a day), hit rate 0.838, chance 0.188, naive rule 0.392, lift 4.47x
  - next: threshold 0.4645, hit rate recent 0.4953 / long run 0.4705
    - 6h: 16 calls (65 a day), hit rate 0.438, chance 0.214, lift 2.05x
    - 24h: 71 calls (71 a day), hit rate 0.507, chance 0.208, lift 2.44x
    - 7d: 466 calls (67 a day), hit rate 0.466, chance 0.192, lift 2.43x
    - 30d: 2079 calls (69 a day), hit rate 0.485, chance 0.188, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 428, 0.416; 0.35: 363, 0.473; 0.40: 293, 0.543; 0.45: 239, 0.602; 0.50: 186, 0.659; 0.55: 140, 0.705; 0.60: 110, 0.748; 0.65: 84, 0.795; 0.70: 63, 0.826; 0.75: 34, 0.868; 0.80: 10, 0.888
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 252, 0.424; 0.40: 164, 0.451; 0.45: 83, 0.474; 0.50: 20, 0.515; 0.55: 2, 0.540
- **K=8**: model 1791417600, labels learned 99533, probability skill vs chance 0.198, widened contest next: True
  - now: threshold 0.5659, hit rate recent 0.6773 / long run 0.7055
    - 6h: 16 calls (66 a day), hit rate 0.500, chance 0.101, naive rule 0.248, lift 4.93x
    - 24h: 63 calls (63 a day), hit rate 0.746, chance 0.130, naive rule 0.363, lift 5.74x
    - 7d: 423 calls (60 a day), hit rate 0.686, chance 0.123, naive rule 0.334, lift 5.56x
    - 30d: 1593 calls (53 a day), hit rate 0.720, chance 0.122, naive rule 0.329, lift 5.90x
  - next: threshold 0.3631, hit rate recent 0.3451 / long run 0.39
    - 6h: 28 calls (115 a day), hit rate 0.214, chance 0.101, lift 2.11x
    - 24h: 76 calls (77 a day), hit rate 0.329, chance 0.130, lift 2.53x
    - 7d: 622 calls (89 a day), hit rate 0.383, chance 0.123, lift 3.10x
    - 30d: 2105 calls (70 a day), hit rate 0.406, chance 0.122, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 267, 0.408; 0.35: 202, 0.483; 0.40: 155, 0.543; 0.45: 122, 0.590; 0.50: 93, 0.635; 0.55: 67, 0.690; 0.60: 46, 0.728; 0.65: 25, 0.770; 0.70: 9, 0.818; 0.75: 1, 0.840
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 183, 0.350; 0.35: 112, 0.389; 0.40: 47, 0.415; 0.45: 10, 0.443; 0.50: 1, 0.405
- **K=13**: model 1791504000, labels learned 99528, probability skill vs chance 0.1747, widened contest next: False
  - now: threshold 0.4345, hit rate recent 0.5913 / long run 0.5863
    - 6h: 15 calls (63 a day), hit rate 0.533, chance 0.070, naive rule 0.197, lift 7.67x
    - 24h: 60 calls (61 a day), hit rate 0.600, chance 0.092, naive rule 0.305, lift 6.55x
    - 7d: 402 calls (58 a day), hit rate 0.572, chance 0.080, naive rule 0.279, lift 7.13x
    - 30d: 1498 calls (50 a day), hit rate 0.587, chance 0.078, naive rule 0.270, lift 7.56x
  - next: threshold 0.2864, hit rate recent 0.3345 / long run 0.3161
    - 6h: 25 calls (104 a day), hit rate 0.280, chance 0.070, lift 4.03x
    - 24h: 72 calls (73 a day), hit rate 0.333, chance 0.092, lift 3.64x
    - 7d: 517 calls (74 a day), hit rate 0.329, chance 0.080, lift 4.10x
    - 30d: 2056 calls (69 a day), hit rate 0.313, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.448; 0.35: 87, 0.510; 0.40: 62, 0.557; 0.45: 43, 0.613; 0.50: 27, 0.637; 0.55: 14, 0.692; 0.60: 5, 0.724; 0.65: 1, 0.750
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.327; 0.35: 15, 0.349; 0.40: 3, 0.337; 0.45: 0, 0.286

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.644 | 2.33% | 0.917 | 0.550 | 0.250 | 0.550 | 0.187 |
| 6h | 5.688 | 1.64% | 0.889 | 0.500 | 0.250 | 0.565 | 0.401 |
| 24h | 6.200 | 4.06% | 0.893 | 0.501 | 0.251 | 0.492 | 0.487 |
| 7d | 11.091 | 4.96% | 0.900 | 0.498 | 0.251 | 0.496 | 0.670 |
| 30d | 13.899 | 4.54% | 0.900 | 0.500 | 0.251 | 0.498 | 0.703 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 4.755 | 4.670 | 4.646 | 4.547 | 4.780 | 4.827 | 4.586 | 4.599 | 4.609 | 4.644 |
| 6h | 5.783 | 5.739 | 5.703 | 5.698 | 5.796 | 5.774 | 5.724 | 5.682 | 5.691 | 5.688 |
| 24h | 6.462 | 6.247 | 6.240 | 6.229 | 6.314 | 6.320 | 6.208 | 6.179 | 6.192 | 6.200 |
| 7d | 11.670 | 11.194 | 11.164 | 11.141 | 11.278 | 11.282 | 11.089 | 11.071 | 11.072 | 11.091 |
| 30d | 14.561 | 14.030 | 13.984 | 13.932 | 14.169 | 14.131 | 13.903 | 13.872 | 13.874 | 13.899 |

## Next candle

- candle starting 2026-10-11 07:04 UTC, last close 2504.74
- P(up) 0.5381, return quantiles (bp): {'05': -3.518, '10': -2.65, '25': -1.097, '40': -0.221, '50': 0.13, '60': 0.542, '75': 1.238, '90': 2.427, '95': 3.415}
- changepoint probability 0.0423, regime age 130.0 min
- agent weights: empirical 0.027, ewma 0.102, garch 0.158, har 0.170, bocpd 0.039, hmm 0.055, online_qr 0.174, lgbm 0.274

## Learning log

- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.18, 4.75, 14.95], current probabilities: [0.975, 0.025, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-11 07:15 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.282, 'l_abs': 0.651, 'l_hi': 0.732, 'l_lo': 0.693, 'b05': 0.642, 'b25': 0.615, 'b75': 0.588, 'b95': 0.559}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.805, 2.004, 2.273, 2.704, 3.346, 3.923, 3.727, 4.649, 4.718, 5.59, 4.695, 5.632, 6.603, 8.199]}
- calibration offsets (in sigma): {'05': -0.0685, '10': -0.077, '25': 0.0475, '40': 0.072, '50': 0.045, '60': 0.028, '75': -0.0075, '90': -0.033, '95': 0.0085}
