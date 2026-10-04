# ETH-USD 60s candle generator - report

- generated: 2026-10-04 01:42 UTC
- last closed candle: 2026-10-04 01:42 UTC (staleness 0.7 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- WIN RATE FALLING: reversal_k13_next 0.276 in the last 7 days, -0.063 against the 7 before
- WIN RATE FALLING: reversal_k5_next 0.451 in the last 7 days, -0.094 against the 7 before
- WIN RATE FALLING: reversal_k8_next 0.380 in the last 7 days, -0.071 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.531 (96) | 0.521 (670) [0.491, 0.551] | 0.510 (2876) [0.491, 0.528] | 0.512 (3068) [0.495, 0.530] | 0.531 (96) | 0.500 (6) | 0.500 | flat -0.024 (noise 0.030) |
| colour_clear | 0.546 (721) | 0.501 (5394) [0.487, 0.516] | 0.499 (23299) [0.494, 0.504] | 0.498 (24959) [0.493, 0.503] | 0.546 (721) | 0.538 (52) | 0.500 | flat +0.001 (noise 0.010) |
| colour_confident | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.607 (84) | 0.562 (16) | 0.500 | - |
| colour_next | 0.521 (1404) | 0.507 (10003) [0.501, 0.512] | 0.502 (42884) [0.498, 0.505] | 0.501 (45753) [0.497, 0.505] | 0.521 (1404) | 0.560 (100) | 0.500 | flat +0.009 (noise 0.007) |
| colour_path | 0.493 (19656) | 0.501 (140042) [0.498, 0.504] | 0.501 (600376) [0.500, 0.502] | 0.500 (640542) [0.499, 0.502] | 0.493 (19656) | 0.474 (1400) | 0.500 | flat -0.000 (noise 0.002) |
| colour_strong | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 0.667 (27) | 1.000 (3) | 0.500 | - |
| reversal_k13_next | 0.324 (102) | 0.276 (635) [0.256, 0.295] | 0.307 (1993) [0.292, 0.323] | 0.301 (2207) [0.287, 0.318] | 0.324 (102) | 0.200 (5) | 0.076 | down -0.063 (noise 0.031) |
| reversal_k13_now | 0.756 (45) | 0.594 (342) [0.539, 0.654] | 0.588 (1428) [0.566, 0.613] | 0.586 (1517) [0.564, 0.608] | 0.756 (45) | 0.500 (4) | 0.076 | flat -0.026 (noise 0.040) |
| reversal_k3_next | 0.535 (144) | 0.578 (689) [0.549, 0.610] | 0.584 (2430) [0.568, 0.599] | 0.584 (2584) [0.570, 0.599] | 0.535 (144) | 0.800 (10) | 0.292 | flat +0.006 (noise 0.031) |
| reversal_k3_now | 0.930 (57) | 0.946 (388) [0.936, 0.958] | 0.942 (1710) [0.933, 0.950] | 0.941 (1820) [0.933, 0.949] | 0.930 (57) | 1.000 (4) | 0.292 | flat +0.003 (noise 0.016) |
| reversal_k5_next | 0.407 (189) | 0.451 (658) [0.418, 0.484] | 0.486 (2076) [0.466, 0.506] | 0.486 (2179) [0.469, 0.506] | 0.407 (189) | 0.500 (12) | 0.187 | down -0.094 (noise 0.034) |
| reversal_k5_now | 0.820 (61) | 0.858 (366) [0.838, 0.886] | 0.836 (1587) [0.821, 0.851] | 0.837 (1672) [0.823, 0.851] | 0.820 (61) | 1.000 (4) | 0.187 | flat +0.041 (noise 0.027) |
| reversal_k8_next | 0.377 (77) | 0.380 (418) [0.355, 0.406] | 0.400 (2018) [0.382, 0.419] | 0.395 (2183) [0.379, 0.414] | 0.377 (77) | 0.600 (5) | 0.121 | down -0.071 (noise 0.035) |
| reversal_k8_now | 0.780 (50) | 0.735 (325) [0.700, 0.772] | 0.718 (1551) [0.698, 0.738] | 0.716 (1637) [0.697, 0.736] | 0.780 (50) | 0.667 (3) | 0.121 | flat -0.013 (noise 0.033) |
| overall | 0.496 (21881) | 0.503 (154536) [0.500, 0.506] | 0.503 (660929) [0.502, 0.504] | 0.502 (705162) [0.501, 0.504] | 0.496 (21881) | 0.485 (1553) | - | flat -0.001 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07462, 0.1101] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5315, 'levels': [{'threshold': 0.07462, 'calls_per_day': 142.7, 'win_rate': 0.5641}, {'threshold': 0.1101, 'calls_per_day': 35.4, 'win_rate': 0.64}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 372, 'rate': 0.5672}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14915 | 0.333 | 0.505 (14699) | 0.600 (100) | 0.784 (2312) |
| volatility: normal | 14913 | 0.361 | 0.507 (14851) | - | 0.767 (2072) |
| volatility: wild | 14914 | 0.373 | 0.491 (14870) | - | 0.782 (2097) |
| session: Asia 00-08 | 14982 | 0.352 | 0.499 (14877) | - | 0.782 (2140) |
| session: Europe 08-13 | 9300 | 0.350 | 0.505 (9235) | - | 0.768 (1404) |
| session: US 13-21 | 14880 | 0.365 | 0.501 (14789) | - | 0.782 (2192) |
| session: late 21-24 | 5580 | 0.351 | 0.503 (5519) | 0.619 (42) | 0.770 (745) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.278 | 0.259 | 0.181 | 0.181 | 0.542 | 0.199 | 0.357 | 1.398 |
| 6h | 360 | 0.313 | 0.290 | 0.204 | 0.227 | 0.586 | 0.256 | 0.370 | 1.264 |
| 24h | 1440 | 0.314 | 0.304 | 0.232 | 0.246 | 0.529 | 0.238 | 0.390 | 1.212 |
| 7d | 10080 | 0.357 | 0.357 | 0.284 | 0.311 | 0.507 | 0.244 | 0.471 | 1.350 |
| 30d | 43200 | 0.355 | 0.355 | 0.278 | 0.308 | 0.502 | 0.245 | 0.465 | 1.282 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.278 / 0.542 / 0.867; 2: 0.265 / 0.525 / 0.900; 3: 0.266 / 0.475 / 0.950; 4: 0.283 / 0.559 / 0.950; 5: 0.268 / 0.458 / 0.933; 6: 0.286 / 0.475 / 0.933; 7: 0.247 / 0.508 / 0.950; 8: 0.274 / 0.508 / 0.900; 9: 0.240 / 0.373 / 0.950; 10: 0.259 / 0.373 / 0.983; 11: 0.265 / 0.508 / 1.000; 12: 0.269 / 0.441 / 0.983; 13: 0.267 / 0.407 / 0.967; 14: 0.286 / 0.525 / 0.983; 15: 0.262 / 0.373 / 0.983
- 6h: 1: 0.313 / 0.586 / 0.853; 2: 0.292 / 0.513 / 0.900; 3: 0.294 / 0.501 / 0.931; 4: 0.288 / 0.510 / 0.919; 5: 0.278 / 0.438 / 0.914; 6: 0.282 / 0.455 / 0.914; 7: 0.276 / 0.507 / 0.917; 8: 0.284 / 0.458 / 0.908; 9: 0.283 / 0.478 / 0.919; 10: 0.284 / 0.487 / 0.928; 11: 0.290 / 0.490 / 0.944; 12: 0.285 / 0.530 / 0.925; 13: 0.293 / 0.484 / 0.925; 14: 0.282 / 0.484 / 0.922; 15: 0.283 / 0.443 / 0.919
- 24h: 1: 0.314 / 0.529 / 0.869; 2: 0.305 / 0.503 / 0.897; 3: 0.309 / 0.505 / 0.907; 4: 0.307 / 0.514 / 0.908; 5: 0.302 / 0.485 / 0.907; 6: 0.303 / 0.483 / 0.901; 7: 0.301 / 0.491 / 0.905; 8: 0.299 / 0.467 / 0.901; 9: 0.299 / 0.476 / 0.907; 10: 0.307 / 0.503 / 0.908; 11: 0.308 / 0.521 / 0.908; 12: 0.303 / 0.497 / 0.903; 13: 0.309 / 0.503 / 0.899; 14: 0.302 / 0.476 / 0.897; 15: 0.297 / 0.459 / 0.898
- 7d: 1: 0.357 / 0.507 / 0.897; 2: 0.351 / 0.491 / 0.900; 3: 0.355 / 0.509 / 0.900; 4: 0.352 / 0.497 / 0.901; 5: 0.351 / 0.505 / 0.900; 6: 0.349 / 0.497 / 0.900; 7: 0.350 / 0.500 / 0.900; 8: 0.349 / 0.503 / 0.900; 9: 0.346 / 0.492 / 0.901; 10: 0.348 / 0.504 / 0.901; 11: 0.348 / 0.506 / 0.901; 12: 0.350 / 0.510 / 0.900; 13: 0.349 / 0.502 / 0.900; 14: 0.347 / 0.497 / 0.899; 15: 0.346 / 0.495 / 0.899
- 30d: 1: 0.355 / 0.502 / 0.899; 2: 0.352 / 0.497 / 0.900; 3: 0.353 / 0.506 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.501 / 0.900; 6: 0.350 / 0.504 / 0.900; 7: 0.349 / 0.506 / 0.900; 8: 0.348 / 0.503 / 0.900; 9: 0.346 / 0.499 / 0.900; 10: 0.348 / 0.504 / 0.900; 11: 0.347 / 0.503 / 0.900; 12: 0.346 / 0.501 / 0.900; 13: 0.346 / 0.500 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.344 / 0.495 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.093 (body 0.069, range 0.117); 'price stays where it was' would score 0.105; colour right 0.542; typical miss of the close 4.3 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.132 (body 0.102, range 0.163); 'price stays where it was' would score 0.129; colour right 0.499; typical miss of the close 2.5 bp; chain ended on the right side 0.458 of 24 chains; n=360
- 24h: match 0.112 (body 0.080, range 0.143); 'price stays where it was' would score 0.102; colour right 0.491; typical miss of the close 3.6 bp; chain ended on the right side 0.552 of 96 chains; n=1440
- 7d: match 0.119 (body 0.078, range 0.159); 'price stays where it was' would score 0.119; colour right 0.495; typical miss of the close 7.6 bp; chain ended on the right side 0.518 of 670 chains; n=10080
- 30d: match 0.121 (body 0.081, range 0.161); 'price stays where it was' would score 0.127; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.509 of 2876 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.365 / 4.3; 2: 0.197 / 4.4; 3: 0.169 / 6.2; 4: 0.133 / 6.5; 5: 0.122 / 7.3; 6: 0.113 / 8.3; 7: 0.101 / 8.6; 8: 0.093 / 9.1; 9: 0.089 / 9.3; 10: 0.083 / 10.2; 11: 0.077 / 10.7; 12: 0.075 / 11.1; 13: 0.067 / 11.5; 14: 0.068 / 11.5; 15: 0.063 / 11.6

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 89136, probability skill vs chance 0.223, widened contest next: False
  - now: threshold 0.8391, hit rate recent 0.9271 / long run 0.9409
    - 6h: 17 calls (69 a day), hit rate 0.941, chance 0.334, naive rule 0.547, lift 2.82x
    - 24h: 57 calls (57 a day), hit rate 0.930, chance 0.304, naive rule 0.523, lift 3.06x
    - 7d: 389 calls (56 a day), hit rate 0.946, chance 0.289, naive rule 0.483, lift 3.27x
    - 30d: 1707 calls (57 a day), hit rate 0.941, chance 0.293, naive rule 0.482, lift 3.22x
  - next: threshold 0.5515, hit rate recent 0.5942 / long run 0.5787
    - 6h: 36 calls (146 a day), hit rate 0.611, chance 0.334, lift 1.83x
    - 24h: 145 calls (146 a day), hit rate 0.572, chance 0.304, lift 1.88x
    - 7d: 690 calls (99 a day), hit rate 0.580, chance 0.289, lift 2.01x
    - 30d: 2433 calls (81 a day), hit rate 0.584, chance 0.293, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 567, 0.494; 0.35: 538, 0.519; 0.40: 490, 0.560; 0.45: 423, 0.625; 0.50: 369, 0.680; 0.55: 322, 0.725; 0.60: 274, 0.766; 0.65: 224, 0.803; 0.70: 182, 0.835; 0.75: 140, 0.868; 0.80: 99, 0.907; 0.85: 49, 0.949; 0.90: 1, 0.971
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.425; 0.35: 497, 0.459; 0.40: 414, 0.487; 0.45: 318, 0.518; 0.50: 209, 0.550; 0.55: 94, 0.586; 0.60: 13, 0.607; 0.65: 0, 0.714
- **K=5**: model 1790208000, labels learned 89134, probability skill vs chance 0.2176, widened contest next: True
  - now: threshold 0.7081, hit rate recent 0.8331 / long run 0.8398
    - 6h: 17 calls (69 a day), hit rate 0.824, chance 0.195, naive rule 0.406, lift 4.21x
    - 24h: 61 calls (61 a day), hit rate 0.820, chance 0.195, naive rule 0.404, lift 4.21x
    - 7d: 368 calls (53 a day), hit rate 0.859, chance 0.187, naive rule 0.395, lift 4.58x
    - 30d: 1583 calls (53 a day), hit rate 0.836, chance 0.187, naive rule 0.391, lift 4.48x
  - next: threshold 0.4177, hit rate recent 0.4287 / long run 0.4707
    - 6h: 46 calls (188 a day), hit rate 0.413, chance 0.195, lift 2.11x
    - 24h: 184 calls (185 a day), hit rate 0.418, chance 0.195, lift 2.15x
    - 7d: 666 calls (95 a day), hit rate 0.452, chance 0.187, lift 2.41x
    - 30d: 2079 calls (69 a day), hit rate 0.485, chance 0.187, lift 2.60x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 433, 0.410; 0.35: 374, 0.462; 0.40: 302, 0.530; 0.45: 248, 0.587; 0.50: 193, 0.647; 0.55: 147, 0.696; 0.60: 116, 0.737; 0.65: 88, 0.780; 0.70: 64, 0.818; 0.75: 35, 0.857; 0.80: 9, 0.869
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 342, 0.386; 0.35: 255, 0.423; 0.40: 169, 0.446; 0.45: 89, 0.472; 0.50: 22, 0.514; 0.55: 3, 0.573
- **K=8**: model 1791072000, labels learned 89131, probability skill vs chance 0.1979, widened contest next: False
  - now: threshold 0.5621, hit rate recent 0.7393 / long run 0.7277
    - 6h: 15 calls (62 a day), hit rate 0.733, chance 0.146, naive rule 0.395, lift 5.03x
    - 24h: 48 calls (48 a day), hit rate 0.750, chance 0.123, naive rule 0.337, lift 6.08x
    - 7d: 325 calls (46 a day), hit rate 0.732, chance 0.123, naive rule 0.333, lift 5.94x
    - 30d: 1547 calls (52 a day), hit rate 0.719, chance 0.122, naive rule 0.327, lift 5.91x
  - next: threshold 0.3651, hit rate recent 0.4046 / long run 0.4045
    - 6h: 18 calls (74 a day), hit rate 0.500, chance 0.146, lift 3.43x
    - 24h: 76 calls (77 a day), hit rate 0.395, chance 0.123, lift 3.20x
    - 7d: 417 calls (60 a day), hit rate 0.384, chance 0.123, lift 3.11x
    - 30d: 2015 calls (67 a day), hit rate 0.400, chance 0.122, lift 3.29x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 278, 0.396; 0.35: 210, 0.471; 0.40: 162, 0.535; 0.45: 128, 0.584; 0.50: 98, 0.624; 0.55: 69, 0.678; 0.60: 46, 0.724; 0.65: 25, 0.759; 0.70: 9, 0.800; 0.75: 1, 0.812
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 190, 0.343; 0.35: 119, 0.380; 0.40: 50, 0.406; 0.45: 11, 0.424; 0.50: 1, 0.452
- **K=13**: model 1791072000, labels learned 89126, probability skill vs chance 0.1871, widened contest next: False
  - now: threshold 0.4077, hit rate recent 0.6688 / long run 0.5951
    - 6h: 15 calls (63 a day), hit rate 0.733, chance 0.088, naive rule 0.347, lift 8.30x
    - 24h: 46 calls (46 a day), hit rate 0.739, chance 0.081, naive rule 0.288, lift 9.08x
    - 7d: 344 calls (49 a day), hit rate 0.590, chance 0.078, naive rule 0.267, lift 7.53x
    - 30d: 1425 calls (48 a day), hit rate 0.588, chance 0.076, naive rule 0.266, lift 7.70x
  - next: threshold 0.2661, hit rate recent 0.302 / long run 0.2961
    - 6h: 22 calls (92 a day), hit rate 0.364, chance 0.088, lift 4.11x
    - 24h: 97 calls (98 a day), hit rate 0.320, chance 0.081, lift 3.93x
    - 7d: 637 calls (91 a day), hit rate 0.273, chance 0.078, lift 3.49x
    - 30d: 1991 calls (66 a day), hit rate 0.306, chance 0.076, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 124, 0.432; 0.35: 91, 0.490; 0.40: 65, 0.536; 0.45: 45, 0.598; 0.50: 29, 0.615; 0.55: 16, 0.657; 0.60: 7, 0.674; 0.65: 2, 0.762; 0.70: 0, 0.667
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 52, 0.315; 0.35: 18, 0.346; 0.40: 4, 0.333; 0.45: 1, 0.417

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.772 | 1.43% | 0.850 | 0.517 | 0.250 | 0.542 | 0.274 |
| 6h | 5.106 | 1.03% | 0.878 | 0.503 | 0.251 | 0.504 | 0.298 |
| 24h | 5.268 | 10.17% | 0.882 | 0.492 | 0.251 | 0.492 | 0.293 |
| 7d | 12.790 | 4.09% | 0.899 | 0.500 | 0.251 | 0.497 | 0.675 |
| 30d | 14.326 | 4.21% | 0.900 | 0.500 | 0.251 | 0.499 | 0.682 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 6.871 | 6.817 | 6.824 | 6.956 | 7.032 | 7.025 | 6.788 | 6.723 | 6.774 | 6.772 |
| 6h | 5.159 | 5.134 | 5.148 | 5.160 | 5.271 | 5.542 | 5.114 | 5.080 | 5.102 | 5.106 |
| 24h | 5.865 | 5.294 | 5.397 | 5.314 | 5.420 | 5.710 | 5.259 | 5.251 | 5.255 | 5.268 |
| 7d | 13.336 | 12.889 | 12.871 | 12.802 | 13.033 | 12.956 | 12.781 | 12.776 | 12.766 | 12.790 |
| 30d | 14.956 | 14.464 | 14.416 | 14.353 | 14.607 | 14.547 | 14.334 | 14.300 | 14.300 | 14.326 |

## Next candle

- candle starting 2026-10-04 01:42 UTC, last close 2692.16
- P(up) 0.5173, return quantiles (bp): {'05': -3.544, '10': -2.546, '25': -1.077, '40': -0.242, '50': 0.049, '60': 0.228, '75': 1.068, '90': 2.604, '95': 3.76}
- changepoint probability 0.0574, regime age 70.0 min
- agent weights: empirical 0.010, ewma 0.146, garch 0.099, har 0.124, bocpd 0.022, hmm 0.003, online_qr 0.257, lgbm 0.338

## Learning log

- 2026-10-02 00:00 UTC: {"garch": {"alpha": 0.0807, "beta": 0.9002}, "hmm": {"sd_bp": [2.96, 5.32, 11.21], "stay": [0.943, 0.95, 0.951]}, "lgbm": {"challenger_loss": 0.2552, "champion_loss": 0.25534, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47291, "challengers": 1, "chance_loss": 0.5983, "widened": false, "champion_loss": 0.47002, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36458, "challengers": 1, "chance_loss": 0.47913, "widened": false, "champion_loss": 0.36223, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28467, "challengers": 1, "chance_loss": 0.38296, "widened": false, "champion_loss": 0.28407, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19829, "challengers": 1, "chance_loss": 0.27138, "widened": false, "champion_loss": 0.1979, "promoted": false}}
- 2026-10-02 12:00 UTC: {"garch": {"alpha": 0.081, "beta": 0.8977}, "hmm": {"sd_bp": [3.12, 5.5, 12.2], "stay": [0.95, 0.947, 0.932]}}
- 2026-10-03 00:00 UTC: {"garch": {"alpha": 0.0973, "beta": 0.8751}, "hmm": {"sd_bp": [3.13, 5.67, 13.01], "stay": [0.959, 0.947, 0.917]}}
- 2026-10-03 12:00 UTC: {"garch": {"alpha": 0.0794, "beta": 0.9127}, "hmm": {"sd_bp": [2.66, 5.39, 13.26], "stay": [0.967, 0.956, 0.918]}}
- 2026-10-04 00:00 UTC: {"garch": {"alpha": 0.0743, "beta": 0.9219}, "hmm": {"sd_bp": [1.97, 4.8, 13.0], "stay": [0.968, 0.966, 0.932]}, "lgbm": {"challenger_loss": 0.24341, "champion_loss": 0.24354, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48523, "challengers": 1, "chance_loss": 0.60613, "widened": false, "champion_loss": 0.48213, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38132, "challengers": 3, "chance_loss": 0.49185, "widened": true, "champion_loss": 0.38091, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28016, "challengers": 1, "chance_loss": 0.37478, "widened": false, "champion_loss": 0.2811, "promoted": true}, "reversal_k13": {"challenger_loss": 0.19748, "challengers": 1, "chance_loss": 0.27721, "widened": false, "champion_loss": 0.19828, "promoted": true}}
- HMM volatility states (sd, bp per minute): [1.97, 4.8, 13.0], current probabilities: [0.935, 0.064, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-04 01:50 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.196, 'l_abs': 0.676, 'l_hi': 0.752, 'l_lo': 0.712, 'b05': 0.642, 'b25': 0.691, 'b75': 0.656, 'b95': 0.629}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.3, 'reach_scale': 1.4, 'ahead': [[1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.4, 1.6], [1.2, 1.6], [1.3, 1.6], [1.3, 1.6], [1.4, 1.6], [1.3, 1.6], [1.2, 1.6], [1.3, 1.6]], 'cone_width': [1.544, 1.681, 2.149, 2.408, 2.591, 2.588, 2.944, 2.831, 2.816, 2.843, 3.16, 3.43, 3.566, 3.774]}
- calibration offsets (in sigma): {'05': -0.0195, '10': 0.051, '25': 0.0625, '40': 0.064, '50': 0.025, '60': -0.054, '75': -0.0425, '90': 0.029, '95': 0.0595}
