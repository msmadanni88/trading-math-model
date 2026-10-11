# ETH-USD 60s candle generator - report

- generated: 2026-10-11 01:02 UTC
- last closed candle: 2026-10-11 01:02 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- none: on track

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.594 (96) | 0.508 (671) [0.454, 0.562] | 0.508 (2875) [0.488, 0.529] | 0.511 (3739) [0.494, 0.528] | 0.511 (767) [0.465, 0.557] | 0.500 (4) | 0.500 | flat -0.013 (noise 0.036) |
| colour_clear | 0.537 (778) | 0.545 (5363) [0.536, 0.553] | 0.510 (23183) [0.502, 0.518] | 0.506 (30322) [0.500, 0.512] | 0.545 (6084) [0.538, 0.552] | 0.448 (29) | 0.500 | up +0.044 (noise 0.010) |
| colour_confident | 0.567 (275) | 0.607 (1140) [0.574, 0.646] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.607 (1224) [0.576, 0.643] | 0.600 (15) | 0.500 | flat -0.000 (noise 0.055) |
| colour_next | 0.529 (1387) | 0.530 (9958) [0.521, 0.539] | 0.508 (42835) [0.502, 0.513] | 0.506 (55711) [0.501, 0.511] | 0.529 (11362) [0.521, 0.537] | 0.491 (59) | 0.500 | up +0.023 (noise 0.007) |
| colour_path | 0.500 (19418) | 0.500 (139412) [0.497, 0.503] | 0.501 (599690) [0.500, 0.502] | 0.500 (779954) [0.499, 0.502] | 0.499 (159068) [0.496, 0.502] | 0.517 (826) | 0.500 | flat -0.001 (noise 0.003) |
| colour_strong | 0.648 (88) | 0.656 (305) [0.602, 0.720] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.657 (332) [0.612, 0.710] | 0.400 (5) | 0.500 | - |
| reversal_k13_next | 0.361 (72) | 0.329 (511) [0.312, 0.345] | 0.312 (2046) [0.297, 0.328] | 0.306 (2718) [0.293, 0.320] | 0.328 (613) [0.314, 0.341] | 1.000 (1) | 0.077 | flat +0.053 (noise 0.027) |
| reversal_k13_now | 0.576 (59) | 0.575 (400) [0.548, 0.604] | 0.587 (1490) [0.565, 0.612] | 0.584 (1917) [0.566, 0.602] | 0.593 (445) [0.559, 0.637] | 0.500 (2) | 0.077 | flat -0.019 (noise 0.039) |
| reversal_k3_next | 0.620 (129) | 0.591 (557) [0.559, 0.621] | 0.586 (2386) [0.571, 0.602] | 0.586 (3141) [0.573, 0.598] | 0.579 (701) [0.550, 0.610] | 0.667 (3) | 0.293 | flat +0.013 (noise 0.028) |
| reversal_k3_now | 0.910 (67) | 0.923 (418) [0.914, 0.936] | 0.940 (1718) [0.931, 0.947] | 0.938 (2238) [0.931, 0.945] | 0.924 (475) [0.916, 0.935] | 1.000 (3) | 0.293 | flat -0.022 (noise 0.017) |
| reversal_k5_next | 0.507 (73) | 0.471 (480) [0.441, 0.496] | 0.485 (2092) [0.467, 0.503] | 0.484 (2659) [0.467, 0.501] | 0.453 (669) [0.425, 0.487] | - | 0.187 | flat +0.019 (noise 0.030) |
| reversal_k5_now | 0.873 (63) | 0.827 (387) [0.791, 0.861] | 0.838 (1590) [0.823, 0.853] | 0.835 (2059) [0.821, 0.849] | 0.826 (448) [0.795, 0.855] | 0.000 (1) | 0.187 | flat -0.031 (noise 0.026) |
| reversal_k8_next | 0.449 (69) | 0.396 (613) [0.367, 0.429] | 0.407 (2098) [0.389, 0.427] | 0.396 (2796) [0.382, 0.411] | 0.394 (690) [0.369, 0.422] | - | 0.122 | flat +0.016 (noise 0.031) |
| reversal_k8_now | 0.770 (61) | 0.699 (418) [0.654, 0.741] | 0.722 (1585) [0.703, 0.742] | 0.712 (2055) [0.694, 0.731] | 0.707 (468) [0.665, 0.745] | 0.500 (2) | 0.122 | flat -0.037 (noise 0.034) |
| overall | 0.506 (21494) | 0.504 (153825) [0.500, 0.508] | 0.504 (660405) [0.502, 0.505] | 0.503 (858987) [0.501, 0.504] | 0.503 (175706) [0.499, 0.507] | 0.517 (901) | - | flat +0.001 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.08096, 0.1223] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5304, 'levels': [{'threshold': 0.08096, 'calls_per_day': 144.9, 'win_rate': 0.6047}, {'threshold': 0.1223, 'calls_per_day': 36.1, 'win_rate': 0.6641}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 10288, 'rate': 0.5307}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14901 | 0.332 | 0.517 (14640) | 0.598 (982) | 0.779 (2403) |
| volatility: normal | 14900 | 0.359 | 0.510 (14828) | 0.633 (191) | 0.775 (2148) |
| volatility: wild | 14901 | 0.373 | 0.496 (14857) | 0.667 (66) | 0.776 (2067) |
| session: Asia 00-08 | 14942 | 0.352 | 0.510 (14832) | 0.596 (436) | 0.780 (2138) |
| session: Europe 08-13 | 9300 | 0.348 | 0.505 (9211) | 0.596 (282) | 0.769 (1471) |
| session: US 13-21 | 14880 | 0.364 | 0.505 (14773) | 0.588 (325) | 0.783 (2198) |
| session: late 21-24 | 5580 | 0.348 | 0.512 (5509) | 0.679 (196) | 0.767 (811) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.311 | 0.285 | 0.207 | 0.207 | 0.509 | 0.247 | 0.375 | 1.338 |
| 6h | 360 | 0.320 | 0.323 | 0.244 | 0.275 | 0.538 | 0.247 | 0.392 | 1.174 |
| 24h | 1440 | 0.318 | 0.306 | 0.232 | 0.256 | 0.526 | 0.249 | 0.386 | 1.251 |
| 7d | 10080 | 0.352 | 0.345 | 0.272 | 0.298 | 0.529 | 0.256 | 0.447 | 1.213 |
| 30d | 43200 | 0.355 | 0.353 | 0.277 | 0.306 | 0.508 | 0.248 | 0.462 | 1.297 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.311 / 0.509 / 0.933; 2: 0.308 / 0.491 / 0.950; 3: 0.331 / 0.667 / 0.967; 4: 0.302 / 0.544 / 0.933; 5: 0.324 / 0.561 / 0.967; 6: 0.306 / 0.491 / 0.983; 7: 0.289 / 0.421 / 1.000; 8: 0.303 / 0.544 / 0.983; 9: 0.272 / 0.386 / 0.983; 10: 0.302 / 0.509 / 1.000; 11: 0.313 / 0.509 / 1.000; 12: 0.302 / 0.509 / 1.000; 13: 0.291 / 0.509 / 1.000; 14: 0.311 / 0.526 / 1.000; 15: 0.318 / 0.579 / 1.000
- 6h: 1: 0.320 / 0.538 / 0.894; 2: 0.318 / 0.480 / 0.908; 3: 0.313 / 0.538 / 0.911; 4: 0.310 / 0.486 / 0.931; 5: 0.320 / 0.538 / 0.933; 6: 0.314 / 0.509 / 0.964; 7: 0.307 / 0.520 / 0.992; 8: 0.315 / 0.523 / 0.944; 9: 0.302 / 0.457 / 0.953; 10: 0.313 / 0.500 / 0.975; 11: 0.310 / 0.497 / 0.978; 12: 0.309 / 0.509 / 1.000; 13: 0.301 / 0.497 / 0.992; 14: 0.305 / 0.500 / 0.986; 15: 0.307 / 0.523 / 0.975
- 24h: 1: 0.318 / 0.526 / 0.880; 2: 0.306 / 0.487 / 0.900; 3: 0.305 / 0.520 / 0.903; 4: 0.302 / 0.495 / 0.894; 5: 0.313 / 0.540 / 0.897; 6: 0.304 / 0.496 / 0.901; 7: 0.300 / 0.497 / 0.901; 8: 0.301 / 0.498 / 0.901; 9: 0.300 / 0.482 / 0.903; 10: 0.306 / 0.511 / 0.903; 11: 0.302 / 0.487 / 0.904; 12: 0.304 / 0.503 / 0.898; 13: 0.301 / 0.500 / 0.903; 14: 0.304 / 0.506 / 0.906; 15: 0.300 / 0.489 / 0.908
- 7d: 1: 0.352 / 0.529 / 0.898; 2: 0.341 / 0.499 / 0.901; 3: 0.342 / 0.512 / 0.900; 4: 0.340 / 0.502 / 0.900; 5: 0.339 / 0.504 / 0.901; 6: 0.337 / 0.497 / 0.901; 7: 0.336 / 0.502 / 0.900; 8: 0.337 / 0.496 / 0.901; 9: 0.333 / 0.488 / 0.901; 10: 0.337 / 0.505 / 0.900; 11: 0.335 / 0.494 / 0.900; 12: 0.336 / 0.500 / 0.900; 13: 0.336 / 0.506 / 0.900; 14: 0.335 / 0.502 / 0.901; 15: 0.336 / 0.499 / 0.901
- 30d: 1: 0.355 / 0.508 / 0.899; 2: 0.349 / 0.497 / 0.900; 3: 0.351 / 0.509 / 0.900; 4: 0.348 / 0.500 / 0.900; 5: 0.348 / 0.505 / 0.900; 6: 0.347 / 0.502 / 0.900; 7: 0.347 / 0.504 / 0.900; 8: 0.346 / 0.503 / 0.900; 9: 0.343 / 0.496 / 0.900; 10: 0.345 / 0.504 / 0.900; 11: 0.344 / 0.501 / 0.900; 12: 0.345 / 0.502 / 0.900; 13: 0.344 / 0.501 / 0.900; 14: 0.343 / 0.497 / 0.900; 15: 0.343 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.140 (body 0.118, range 0.162); 'price stays where it was' would score 0.142; colour right 0.596; typical miss of the close 2.9 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.125 (body 0.090, range 0.159); 'price stays where it was' would score 0.162; colour right 0.540; typical miss of the close 3.9 bp; chain ended on the right side 0.583 of 24 chains; n=360
- 24h: match 0.122 (body 0.090, range 0.154); 'price stays where it was' would score 0.130; colour right 0.503; typical miss of the close 3.6 bp; chain ended on the right side 0.583 of 96 chains; n=1440
- 7d: match 0.117 (body 0.081, range 0.154); 'price stays where it was' would score 0.124; colour right 0.499; typical miss of the close 6.1 bp; chain ended on the right side 0.508 of 671 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.125; colour right 0.498; typical miss of the close 7.8 bp; chain ended on the right side 0.508 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.363 / 3.9; 2: 0.199 / 4.3; 3: 0.167 / 5.9; 4: 0.133 / 6.5; 5: 0.121 / 7.1; 6: 0.111 / 7.7; 7: 0.101 / 8.1; 8: 0.093 / 8.4; 9: 0.086 / 8.8; 10: 0.080 / 9.4; 11: 0.076 / 9.9; 12: 0.075 / 10.5; 13: 0.063 / 10.8; 14: 0.065 / 10.9; 15: 0.061 / 11.1

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 99176, probability skill vs chance 0.2272, widened contest next: False
  - now: threshold 0.8257, hit rate recent 0.913 / long run 0.9314
    - 6h: 15 calls (61 a day), hit rate 0.867, chance 0.317, naive rule 0.493, lift 2.73x
    - 24h: 68 calls (68 a day), hit rate 0.926, chance 0.314, naive rule 0.521, lift 2.95x
    - 7d: 417 calls (60 a day), hit rate 0.923, chance 0.295, naive rule 0.492, lift 3.12x
    - 30d: 1719 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.483, lift 3.22x
  - next: threshold 0.5497, hit rate recent 0.641 / long run 0.5855
    - 6h: 33 calls (134 a day), hit rate 0.697, chance 0.317, lift 2.20x
    - 24h: 127 calls (127 a day), hit rate 0.622, chance 0.314, lift 1.98x
    - 7d: 552 calls (79 a day), hit rate 0.589, chance 0.295, lift 1.99x
    - 30d: 2385 calls (80 a day), hit rate 0.587, chance 0.292, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 538, 0.518; 0.40: 485, 0.563; 0.45: 418, 0.629; 0.50: 365, 0.684; 0.55: 321, 0.725; 0.60: 273, 0.769; 0.65: 225, 0.803; 0.70: 181, 0.835; 0.75: 139, 0.874; 0.80: 97, 0.913; 0.85: 49, 0.948; 0.90: 2, 0.972
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 498, 0.459; 0.40: 412, 0.488; 0.45: 317, 0.519; 0.50: 206, 0.554; 0.55: 92, 0.583; 0.60: 14, 0.603; 0.65: 1, 0.682
- **K=5**: model 1791590400, labels learned 99174, probability skill vs chance 0.2198, widened contest next: False
  - now: threshold 0.7131, hit rate recent 0.8445 / long run 0.831
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.194, naive rule 0.410, lift 4.42x
    - 24h: 63 calls (63 a day), hit rate 0.873, chance 0.199, naive rule 0.434, lift 4.38x
    - 7d: 384 calls (55 a day), hit rate 0.823, chance 0.191, naive rule 0.399, lift 4.31x
    - 30d: 1590 calls (53 a day), hit rate 0.837, chance 0.187, naive rule 0.392, lift 4.47x
  - next: threshold 0.4644, hit rate recent 0.507 / long run 0.4714
    - 6h: 12 calls (49 a day), hit rate 0.667, chance 0.194, lift 3.44x
    - 24h: 70 calls (70 a day), hit rate 0.500, chance 0.199, lift 2.51x
    - 7d: 471 calls (67 a day), hit rate 0.469, chance 0.191, lift 2.46x
    - 30d: 2086 calls (70 a day), hit rate 0.485, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 428, 0.416; 0.35: 364, 0.472; 0.40: 294, 0.542; 0.45: 240, 0.601; 0.50: 186, 0.660; 0.55: 140, 0.705; 0.60: 109, 0.749; 0.65: 84, 0.795; 0.70: 62, 0.825; 0.75: 34, 0.866; 0.80: 9, 0.887
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 339, 0.386; 0.35: 252, 0.424; 0.40: 164, 0.452; 0.45: 83, 0.474; 0.50: 20, 0.516; 0.55: 2, 0.540
- **K=8**: model 1791417600, labels learned 99171, probability skill vs chance 0.2135, widened contest next: False
  - now: threshold 0.5764, hit rate recent 0.7266 / long run 0.7106
    - 6h: 15 calls (62 a day), hit rate 0.867, chance 0.141, naive rule 0.385, lift 6.13x
    - 24h: 60 calls (60 a day), hit rate 0.783, chance 0.140, naive rule 0.402, lift 5.60x
    - 7d: 417 calls (60 a day), hit rate 0.698, chance 0.124, naive rule 0.338, lift 5.62x
    - 30d: 1585 calls (53 a day), hit rate 0.722, chance 0.122, naive rule 0.329, lift 5.92x
  - next: threshold 0.3691, hit rate recent 0.4117 / long run 0.3983
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.141, lift 3.03x
    - 24h: 67 calls (67 a day), hit rate 0.433, chance 0.140, lift 3.09x
    - 7d: 609 calls (87 a day), hit rate 0.396, chance 0.124, lift 3.19x
    - 30d: 2095 calls (70 a day), hit rate 0.407, chance 0.122, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 268, 0.408; 0.35: 202, 0.483; 0.40: 155, 0.544; 0.45: 122, 0.591; 0.50: 93, 0.634; 0.55: 67, 0.689; 0.60: 46, 0.730; 0.65: 24, 0.770; 0.70: 9, 0.820; 0.75: 1, 0.840
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 183, 0.351; 0.35: 112, 0.390; 0.40: 47, 0.416; 0.45: 10, 0.442; 0.50: 1, 0.405
- **K=13**: model 1791504000, labels learned 99166, probability skill vs chance 0.1853, widened contest next: False
  - now: threshold 0.4337, hit rate recent 0.6006 / long run 0.5869
    - 6h: 14 calls (58 a day), hit rate 0.643, chance 0.100, naive rule 0.374, lift 6.43x
    - 24h: 59 calls (60 a day), hit rate 0.593, chance 0.098, naive rule 0.351, lift 6.06x
    - 7d: 398 calls (57 a day), hit rate 0.575, chance 0.080, naive rule 0.280, lift 7.17x
    - 30d: 1491 calls (50 a day), hit rate 0.587, chance 0.078, naive rule 0.270, lift 7.56x
  - next: threshold 0.2862, hit rate recent 0.3588 / long run 0.3177
    - 6h: 13 calls (54 a day), hit rate 0.462, chance 0.100, lift 4.62x
    - 24h: 68 calls (69 a day), hit rate 0.353, chance 0.098, lift 3.61x
    - 7d: 509 calls (73 a day), hit rate 0.330, chance 0.080, lift 4.11x
    - 30d: 2044 calls (68 a day), hit rate 0.313, chance 0.078, lift 4.03x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 119, 0.447; 0.35: 87, 0.509; 0.40: 62, 0.556; 0.45: 43, 0.610; 0.50: 27, 0.635; 0.55: 14, 0.688; 0.60: 5, 0.714; 0.65: 1, 0.758
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.326; 0.35: 15, 0.349; 0.40: 3, 0.341; 0.45: 0, 0.286

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.520 | 0.09% | 0.933 | 0.550 | 0.255 | 0.456 | 0.101 |
| 6h | 7.006 | 1.45% | 0.900 | 0.508 | 0.249 | 0.538 | 0.313 |
| 24h | 6.343 | 5.66% | 0.890 | 0.498 | 0.251 | 0.476 | 0.470 |
| 7d | 11.036 | 4.99% | 0.900 | 0.500 | 0.251 | 0.494 | 0.672 |
| 30d | 13.941 | 4.54% | 0.900 | 0.500 | 0.251 | 0.497 | 0.702 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.526 | 5.491 | 5.453 | 5.475 | 5.603 | 5.652 | 5.531 | 5.467 | 5.485 | 5.520 |
| 6h | 7.109 | 7.047 | 7.011 | 7.056 | 7.109 | 7.090 | 6.982 | 6.982 | 6.992 | 7.006 |
| 24h | 6.724 | 6.386 | 6.400 | 6.378 | 6.454 | 6.473 | 6.343 | 6.317 | 6.332 | 6.343 |
| 7d | 11.616 | 11.140 | 11.110 | 11.086 | 11.229 | 11.239 | 11.034 | 11.017 | 11.018 | 11.036 |
| 30d | 14.604 | 14.071 | 14.025 | 13.973 | 14.211 | 14.173 | 13.944 | 13.914 | 13.915 | 13.941 |

## Next candle

- candle starting 2026-10-11 01:02 UTC, last close 2501.81
- P(up) 0.5142, return quantiles (bp): {'05': -3.109, '10': -2.315, '25': -1.037, '40': -0.178, '50': 0.022, '60': 0.452, '75': 1.025, '90': 2.276, '95': 3.172}
- changepoint probability 0.0298, regime age 74.8 min
- agent weights: empirical 0.013, ewma 0.108, garch 0.144, har 0.126, bocpd 0.043, hmm 0.048, online_qr 0.226, lgbm 0.292

## Learning log

- 2026-10-09 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9071}, "hmm": {"sd_bp": [2.22, 4.81, 14.65], "stay": [0.958, 0.964, 0.907]}, "lgbm": {"challenger_loss": 0.25492, "champion_loss": 0.25489, "promoted": false}, "reversal_k3": {"challenger_loss": 0.46907, "challengers": 3, "chance_loss": 0.5899, "widened": true, "champion_loss": 0.47119, "promoted": true}, "reversal_k5": {"challenger_loss": 0.37741, "challengers": 3, "chance_loss": 0.47543, "widened": true, "champion_loss": 0.37713, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26875, "challengers": 3, "chance_loss": 0.35831, "widened": true, "champion_loss": 0.26852, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19288, "challengers": 1, "chance_loss": 0.26943, "widened": false, "champion_loss": 0.19309, "promoted": true}}
- 2026-10-09 12:00 UTC: {"garch": {"alpha": 0.0812, "beta": 0.9097}, "hmm": {"sd_bp": [2.34, 4.79, 15.13], "stay": [0.964, 0.967, 0.915]}}
- 2026-10-10 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9015}, "hmm": {"sd_bp": [2.35, 4.9, 15.58], "stay": [0.968, 0.97, 0.919]}, "lgbm": {"challenger_loss": 0.25374, "champion_loss": 0.25379, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47228, "challengers": 1, "chance_loss": 0.599, "widened": false, "champion_loss": 0.46738, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37368, "challengers": 3, "chance_loss": 0.48488, "widened": true, "champion_loss": 0.3743, "promoted": true}, "reversal_k8": {"challenger_loss": 0.26821, "challengers": 3, "chance_loss": 0.36481, "widened": true, "champion_loss": 0.26802, "promoted": false}, "reversal_k13": {"challenger_loss": 0.1905, "challengers": 1, "chance_loss": 0.26749, "widened": false, "champion_loss": 0.19016, "promoted": false}}
- 2026-10-10 12:00 UTC: {"garch": {"alpha": 0.0811, "beta": 0.913}, "hmm": {"sd_bp": [2.22, 4.82, 15.52], "stay": [0.978, 0.976, 0.918]}}
- 2026-10-11 00:00 UTC: {"garch": {"alpha": 0.0894, "beta": 0.9056}, "hmm": {"sd_bp": [2.18, 4.75, 14.95], "stay": [0.985, 0.978, 0.925]}, "lgbm": {"challenger_loss": 0.25081, "champion_loss": 0.25085, "promoted": true}, "reversal_k3": {"challenger_loss": 0.49765, "challengers": 1, "chance_loss": 0.61979, "widened": false, "champion_loss": 0.49423, "promoted": false}, "reversal_k5": {"challenger_loss": 0.3828, "challengers": 1, "chance_loss": 0.49459, "widened": false, "champion_loss": 0.38006, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28458, "challengers": 1, "chance_loss": 0.38541, "widened": false, "champion_loss": 0.28396, "promoted": false}, "reversal_k13": {"challenger_loss": 0.21986, "challengers": 1, "chance_loss": 0.2966, "widened": false, "champion_loss": 0.21917, "promoted": false}}
- HMM volatility states (sd, bp per minute): [2.18, 4.75, 14.95], current probabilities: [0.98, 0.02, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-11 01:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.18, 'l_abs': 0.66, 'l_hi': 0.713, 'l_lo': 0.678, 'b05': 0.635, 'b25': 0.623, 'b75': 0.599, 'b95': 0.527}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8]], 'cone_width': [1.29, 1.648, 2.024, 2.136, 2.164, 2.437, 2.559, 2.613, 2.873, 2.901, 3.562, 3.362, 3.227, 3.152]}
- calibration offsets (in sigma): {'05': -0.0095, '10': -0.029, '25': 0.0025, '40': 0.074, '50': -0.005, '60': 0.006, '75': -0.0525, '90': -0.041, '95': 0.0195}
