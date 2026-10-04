# ETH-USD 60s candle generator - report

- generated: 2026-10-04 20:29 UTC
- last closed candle: 2026-10-04 20:29 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k13_next 0.276 in the last 7 days, -0.063 against the 7 before
- WIN RATE FALLING: reversal_k5_next 0.451 in the last 7 days, -0.094 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.380 in the last 7 days, -0.071 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.521 (670) [0.491, 0.551] | 0.510 (2876) [0.491, 0.528] | 0.512 (3068) [0.495, 0.530] | 0.531 (96) | 0.667 (81) | 0.500 | flat -0.024 (noise 0.030) |
| colour_clear | 0.546 (721) | 0.501 (5394) [0.487, 0.516] | 0.499 (23299) [0.494, 0.504] | 0.498 (24959) [0.493, 0.503] | 0.546 (721) | 0.563 (545) | 0.500 | flat +0.001 (noise 0.010) |
| colour_confident | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.618 (246) | 0.500 | - |
| colour_next | 0.521 (1404) | 0.507 (10003) [0.501, 0.512] | 0.502 (42884) [0.498, 0.505] | 0.501 (45753) [0.497, 0.505] | 0.521 (1404) | 0.555 (1206) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.493 (19656) | 0.501 (140042) [0.498, 0.504] | 0.501 (600376) [0.500, 0.502] | 0.500 (640542) [0.499, 0.502] | 0.493 (19656) | 0.502 (16884) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.635 (85) | 0.500 | - |
| reversal_k13_next | 0.324 (102) | 0.276 (635) [0.256, 0.295] | 0.307 (1993) [0.292, 0.323] | 0.301 (2207) [0.287, 0.318] | 0.324 (102) | 0.352 (71) | 0.076 | down -0.063 (noise 0.031) |
| reversal_k13_now | 0.756 (45) | 0.594 (342) [0.539, 0.654] | 0.588 (1428) [0.566, 0.613] | 0.586 (1517) [0.564, 0.608] | 0.756 (45) | 0.636 (55) | 0.076 | flat -0.026 (noise 0.040) |
| reversal_k3_next | 0.535 (144) | 0.578 (689) [0.549, 0.610] | 0.584 (2430) [0.568, 0.599] | 0.584 (2584) [0.570, 0.599] | 0.535 (144) | 0.586 (111) | 0.292 | flat +0.006 (noise 0.031) |
| reversal_k3_now | 0.930 (57) | 0.946 (388) [0.936, 0.958] | 0.942 (1710) [0.933, 0.950] | 0.941 (1820) [0.933, 0.949] | 0.930 (57) | 0.942 (52) | 0.292 | flat +0.003 (noise 0.016) |
| reversal_k5_next | 0.407 (189) | 0.451 (658) [0.418, 0.484] | 0.486 (2076) [0.466, 0.506] | 0.486 (2179) [0.469, 0.506] | 0.407 (189) | 0.467 (105) | 0.187 | down -0.094 (noise 0.034) |
| reversal_k5_now | 0.820 (61) | 0.858 (366) [0.838, 0.886] | 0.836 (1587) [0.821, 0.851] | 0.837 (1672) [0.823, 0.851] | 0.820 (61) | 0.930 (57) | 0.187 | flat +0.041 (noise 0.027) |
| reversal_k8_next | 0.377 (77) | 0.380 (418) [0.355, 0.406] | 0.400 (2018) [0.382, 0.419] | 0.395 (2183) [0.379, 0.414] | 0.377 (77) | 0.432 (74) | 0.121 | down -0.071 (noise 0.035) |
| reversal_k8_now | 0.780 (50) | 0.735 (325) [0.700, 0.772] | 0.718 (1551) [0.698, 0.738] | 0.716 (1637) [0.697, 0.736] | 0.780 (50) | 0.812 (48) | 0.121 | flat -0.013 (noise 0.033) |
| overall | 0.496 (21881) | 0.503 (154536) [0.500, 0.506] | 0.503 (660929) [0.502, 0.504] | 0.502 (705162) [0.501, 0.504] | 0.496 (21881) | 0.510 (18744) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07548, 0.1127] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5306, 'levels': [{'threshold': 0.07548, 'calls_per_day': 144.9, 'win_rate': 0.5616}, {'threshold': 0.1127, 'calls_per_day': 36.7, 'win_rate': 0.6255}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 1478, 'rate': 0.5575}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15290 | 0.331 | 0.509 (15057) | 0.615 (330) | 0.784 (2406) |
| volatility: normal | 15289 | 0.359 | 0.507 (15223) | - | 0.775 (2137) |
| volatility: wild | 15290 | 0.373 | 0.492 (15246) | - | 0.778 (2135) |
| session: Asia 00-08 | 15360 | 0.350 | 0.500 (15249) | 0.635 (115) | 0.784 (2200) |
| session: Europe 08-13 | 9600 | 0.348 | 0.505 (9531) | 0.562 (64) | 0.768 (1459) |
| session: US 13-21 | 15329 | 0.364 | 0.503 (15227) | 0.624 (109) | 0.785 (2274) |
| session: late 21-24 | 5580 | 0.351 | 0.503 (5519) | 0.619 (42) | 0.770 (745) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.332 | 0.308 | 0.244 | 0.244 | 0.667 | 0.260 | 0.403 | 1.184 |
| 6h | 360 | 0.337 | 0.313 | 0.238 | 0.262 | 0.609 | 0.270 | 0.404 | 1.272 |
| 24h | 1440 | 0.310 | 0.298 | 0.232 | 0.244 | 0.561 | 0.236 | 0.384 | 1.386 |
| 7d | 10080 | 0.353 | 0.352 | 0.281 | 0.306 | 0.511 | 0.241 | 0.465 | 1.409 |
| 30d | 43200 | 0.354 | 0.353 | 0.277 | 0.307 | 0.503 | 0.245 | 0.463 | 1.299 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.332 / 0.667 / 0.833; 2: 0.323 / 0.483 / 0.833; 3: 0.320 / 0.533 / 0.917; 4: 0.307 / 0.433 / 0.933; 5: 0.345 / 0.567 / 0.917; 6: 0.312 / 0.450 / 0.933; 7: 0.334 / 0.500 / 0.900; 8: 0.339 / 0.600 / 0.900; 9: 0.327 / 0.500 / 0.967; 10: 0.311 / 0.483 / 0.950; 11: 0.296 / 0.400 / 0.933; 12: 0.335 / 0.517 / 0.983; 13: 0.313 / 0.483 / 0.983; 14: 0.312 / 0.467 / 0.983; 15: 0.316 / 0.567 / 1.000
- 6h: 1: 0.337 / 0.609 / 0.883; 2: 0.311 / 0.479 / 0.894; 3: 0.321 / 0.547 / 0.933; 4: 0.317 / 0.518 / 0.936; 5: 0.312 / 0.490 / 0.950; 6: 0.309 / 0.504 / 0.961; 7: 0.311 / 0.501 / 0.950; 8: 0.323 / 0.527 / 0.950; 9: 0.321 / 0.552 / 0.975; 10: 0.317 / 0.544 / 0.975; 11: 0.310 / 0.484 / 0.972; 12: 0.320 / 0.544 / 0.994; 13: 0.306 / 0.504 / 0.994; 14: 0.304 / 0.462 / 0.989; 15: 0.320 / 0.552 / 0.994
- 24h: 1: 0.310 / 0.561 / 0.876; 2: 0.293 / 0.509 / 0.898; 3: 0.296 / 0.527 / 0.908; 4: 0.287 / 0.499 / 0.908; 5: 0.287 / 0.478 / 0.909; 6: 0.288 / 0.493 / 0.910; 7: 0.286 / 0.498 / 0.909; 8: 0.293 / 0.500 / 0.911; 9: 0.287 / 0.492 / 0.910; 10: 0.292 / 0.515 / 0.912; 11: 0.293 / 0.501 / 0.912; 12: 0.291 / 0.532 / 0.909; 13: 0.287 / 0.491 / 0.914; 14: 0.286 / 0.485 / 0.917; 15: 0.290 / 0.496 / 0.917
- 7d: 1: 0.353 / 0.511 / 0.896; 2: 0.347 / 0.493 / 0.899; 3: 0.350 / 0.512 / 0.900; 4: 0.347 / 0.498 / 0.901; 5: 0.346 / 0.505 / 0.901; 6: 0.344 / 0.496 / 0.901; 7: 0.345 / 0.501 / 0.901; 8: 0.344 / 0.503 / 0.901; 9: 0.341 / 0.492 / 0.901; 10: 0.344 / 0.507 / 0.902; 11: 0.345 / 0.507 / 0.901; 12: 0.345 / 0.514 / 0.900; 13: 0.344 / 0.501 / 0.900; 14: 0.342 / 0.494 / 0.901; 15: 0.342 / 0.498 / 0.901
- 30d: 1: 0.354 / 0.503 / 0.898; 2: 0.350 / 0.497 / 0.900; 3: 0.352 / 0.506 / 0.900; 4: 0.348 / 0.499 / 0.900; 5: 0.348 / 0.501 / 0.900; 6: 0.348 / 0.503 / 0.900; 7: 0.348 / 0.506 / 0.900; 8: 0.347 / 0.503 / 0.900; 9: 0.345 / 0.499 / 0.900; 10: 0.346 / 0.504 / 0.900; 11: 0.346 / 0.503 / 0.900; 12: 0.345 / 0.502 / 0.900; 13: 0.344 / 0.500 / 0.900; 14: 0.344 / 0.495 / 0.900; 15: 0.343 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.101 (body 0.082, range 0.121); 'price stays where it was' would score 0.117; colour right 0.450; typical miss of the close 3.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.106 (body 0.075, range 0.137); 'price stays where it was' would score 0.108; colour right 0.504; typical miss of the close 3.3 bp; chain ended on the right side 0.625 of 24 chains; n=360
- 24h: match 0.114 (body 0.081, range 0.146); 'price stays where it was' would score 0.111; colour right 0.495; typical miss of the close 2.9 bp; chain ended on the right side 0.635 of 96 chains; n=1440
- 7d: match 0.118 (body 0.077, range 0.159); 'price stays where it was' would score 0.119; colour right 0.492; typical miss of the close 7.0 bp; chain ended on the right side 0.531 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.160); 'price stays where it was' would score 0.126; colour right 0.497; typical miss of the close 7.9 bp; chain ended on the right side 0.513 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.2; 2: 0.197 / 4.3; 3: 0.169 / 6.0; 4: 0.133 / 6.3; 5: 0.122 / 7.1; 6: 0.112 / 8.0; 7: 0.099 / 8.3; 8: 0.092 / 8.7; 9: 0.088 / 9.0; 10: 0.083 / 9.7; 11: 0.077 / 10.3; 12: 0.075 / 10.7; 13: 0.067 / 11.0; 14: 0.067 / 11.1; 15: 0.063 / 11.4

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 90263, probability skill vs chance 0.2201, widened contest next: False
  - now: threshold 0.8398, hit rate recent 0.9329 / long run 0.9406
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.248, naive rule 0.392, lift 3.78x
    - 24h: 63 calls (63 a day), hit rate 0.937, chance 0.288, naive rule 0.473, lift 3.25x
    - 7d: 399 calls (57 a day), hit rate 0.945, chance 0.287, naive rule 0.479, lift 3.30x
    - 30d: 1711 calls (57 a day), hit rate 0.943, chance 0.292, naive rule 0.482, lift 3.23x
  - next: threshold 0.5503, hit rate recent 0.5796 / long run 0.5767
    - 6h: 46 calls (187 a day), hit rate 0.587, chance 0.248, lift 2.37x
    - 24h: 131 calls (131 a day), hit rate 0.573, chance 0.288, lift 1.99x
    - 7d: 708 calls (101 a day), hit rate 0.582, chance 0.287, lift 2.03x
    - 30d: 2488 calls (83 a day), hit rate 0.584, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.518; 0.40: 489, 0.560; 0.45: 421, 0.626; 0.50: 367, 0.680; 0.55: 321, 0.725; 0.60: 273, 0.767; 0.65: 224, 0.804; 0.70: 182, 0.835; 0.75: 139, 0.870; 0.80: 99, 0.909; 0.85: 49, 0.951; 0.90: 1, 0.976
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 584, 0.424; 0.35: 498, 0.459; 0.40: 414, 0.487; 0.45: 318, 0.518; 0.50: 210, 0.550; 0.55: 95, 0.586; 0.60: 13, 0.612; 0.65: 0, 0.714
- **K=5**: model 1790208000, labels learned 90261, probability skill vs chance 0.2207, widened contest next: False
  - now: threshold 0.7106, hit rate recent 0.8871 / long run 0.8469
    - 6h: 16 calls (65 a day), hit rate 0.938, chance 0.169, naive rule 0.305, lift 5.56x
    - 24h: 67 calls (67 a day), hit rate 0.896, chance 0.178, naive rule 0.363, lift 5.02x
    - 7d: 384 calls (55 a day), hit rate 0.857, chance 0.185, naive rule 0.388, lift 4.62x
    - 30d: 1595 calls (53 a day), hit rate 0.840, chance 0.186, naive rule 0.390, lift 4.51x
  - next: threshold 0.4504, hit rate recent 0.4633 / long run 0.4696
    - 6h: 36 calls (147 a day), hit rate 0.472, chance 0.169, lift 2.80x
    - 24h: 132 calls (133 a day), hit rate 0.447, chance 0.178, lift 2.51x
    - 7d: 730 calls (104 a day), hit rate 0.453, chance 0.185, lift 2.45x
    - 30d: 2139 calls (71 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 433, 0.410; 0.35: 373, 0.462; 0.40: 301, 0.531; 0.45: 246, 0.589; 0.50: 192, 0.649; 0.55: 147, 0.699; 0.60: 115, 0.741; 0.65: 88, 0.784; 0.70: 65, 0.822; 0.75: 35, 0.861; 0.80: 9, 0.883
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.385; 0.35: 255, 0.422; 0.40: 170, 0.447; 0.45: 89, 0.472; 0.50: 22, 0.516; 0.55: 3, 0.570
- **K=8**: model 1791072000, labels learned 90258, probability skill vs chance 0.2092, widened contest next: False
  - now: threshold 0.5589, hit rate recent 0.7834 / long run 0.7346
    - 6h: 16 calls (66 a day), hit rate 0.875, chance 0.131, naive rule 0.294, lift 6.66x
    - 24h: 57 calls (57 a day), hit rate 0.789, chance 0.130, naive rule 0.319, lift 6.07x
    - 7d: 326 calls (47 a day), hit rate 0.733, chance 0.123, naive rule 0.328, lift 5.94x
    - 30d: 1548 calls (52 a day), hit rate 0.725, chance 0.122, naive rule 0.327, lift 5.95x
  - next: threshold 0.3583, hit rate recent 0.4187 / long run 0.4062
    - 6h: 29 calls (119 a day), hit rate 0.483, chance 0.131, lift 3.67x
    - 24h: 84 calls (85 a day), hit rate 0.440, chance 0.130, lift 3.39x
    - 7d: 438 calls (63 a day), hit rate 0.386, chance 0.123, lift 3.13x
    - 30d: 2024 calls (67 a day), hit rate 0.402, chance 0.122, lift 3.30x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 276, 0.398; 0.35: 208, 0.474; 0.40: 161, 0.539; 0.45: 127, 0.587; 0.50: 97, 0.628; 0.55: 69, 0.683; 0.60: 46, 0.731; 0.65: 25, 0.766; 0.70: 9, 0.807; 0.75: 1, 0.806
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 190, 0.344; 0.35: 119, 0.382; 0.40: 49, 0.410; 0.45: 10, 0.418; 0.50: 1, 0.410
- **K=13**: model 1791072000, labels learned 90253, probability skill vs chance 0.1954, widened contest next: False
  - now: threshold 0.4081, hit rate recent 0.6685 / long run 0.5995
    - 6h: 16 calls (67 a day), hit rate 0.812, chance 0.110, naive rule 0.312, lift 7.38x
    - 24h: 63 calls (64 a day), hit rate 0.651, chance 0.086, naive rule 0.269, lift 7.57x
    - 7d: 356 calls (51 a day), hit rate 0.590, chance 0.078, naive rule 0.264, lift 7.52x
    - 30d: 1443 calls (48 a day), hit rate 0.591, chance 0.077, naive rule 0.267, lift 7.71x
  - next: threshold 0.2667, hit rate recent 0.3644 / long run 0.3035
    - 6h: 25 calls (104 a day), hit rate 0.520, chance 0.110, lift 4.72x
    - 24h: 83 calls (84 a day), hit rate 0.361, chance 0.086, lift 4.20x
    - 7d: 654 calls (94 a day), hit rate 0.286, chance 0.078, lift 3.65x
    - 30d: 1999 calls (67 a day), hit rate 0.308, chance 0.077, lift 4.02x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.437; 0.35: 90, 0.493; 0.40: 65, 0.541; 0.45: 45, 0.603; 0.50: 29, 0.622; 0.55: 16, 0.667; 0.60: 7, 0.686; 0.65: 2, 0.770; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.315; 0.35: 17, 0.345; 0.40: 4, 0.327; 0.45: 1, 0.409

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 5.306 | -0.34% | 0.850 | 0.483 | 0.249 | 0.500 | 0.054 |
| 6h | 5.544 | 1.08% | 0.889 | 0.497 | 0.250 | 0.501 | 0.373 |
| 24h | 5.236 | 2.17% | 0.890 | 0.499 | 0.251 | 0.493 | 0.407 |
| 7d | 12.410 | 4.15% | 0.899 | 0.501 | 0.251 | 0.496 | 0.695 |
| 30d | 14.017 | 4.19% | 0.899 | 0.500 | 0.251 | 0.499 | 0.696 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.288 | 5.311 | 5.353 | 5.360 | 5.383 | 5.452 | 5.305 | 5.263 | 5.300 | 5.306 |
| 6h | 5.604 | 5.559 | 5.577 | 5.583 | 5.685 | 5.697 | 5.548 | 5.516 | 5.533 | 5.544 |
| 24h | 5.353 | 5.288 | 5.283 | 5.251 | 5.432 | 5.524 | 5.238 | 5.226 | 5.232 | 5.236 |
| 7d | 12.948 | 12.510 | 12.491 | 12.421 | 12.659 | 12.591 | 12.402 | 12.400 | 12.388 | 12.410 |
| 30d | 14.629 | 14.147 | 14.105 | 14.042 | 14.288 | 14.239 | 14.021 | 13.990 | 13.990 | 14.017 |

## Next candle

- candle starting 2026-10-04 20:29 UTC, last close 2701.54
- P(up) 0.4702, return quantiles (bp): {'05': -3.359, '10': -2.19, '25': -0.991, '40': -0.352, '50': -0.103, '60': 0.251, '75': 1.004, '90': 2.31, '95': 3.42}
- changepoint probability 0.0412, regime age 171.8 min
- agent weights: empirical 0.040, ewma 0.125, garch 0.116, har 0.163, bocpd 0.012, hmm 0.006, online_qr 0.219, lgbm 0.319

## Learning log

- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- HMM volatility states (sd, bp per minute): [1.75, 4.62, 12.53], current probabilities: [0.932, 0.067, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-10-04 20:40 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.339, 'l_abs': 0.703, 'l_hi': 0.751, 'l_lo': 0.711, 'b05': 0.692, 'b25': 0.682, 'b75': 0.548, 'b95': 0.592}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6], [1.3, 1.6]], 'cone_width': [1.617, 1.657, 1.918, 2.106, 2.221, 2.356, 2.474, 2.629, 2.668, 2.918, 3.179, 3.0, 2.822, 2.869]}
- calibration offsets (in sigma): {'05': -0.076, '10': 0.058, '25': 0.04, '40': 0.012, '50': -0.04, '60': -0.052, '75': -0.04, '90': -0.008, '95': 0.106}
