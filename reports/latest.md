# ETH-USD 60s candle generator - report

- generated: 2026-10-06 22:59 UTC
- last closed candle: 2026-10-06 22:59 UTC (staleness 0.1 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.432 (95) | 0.508 (669) [0.470, 0.551] | 0.506 (2875) [0.488, 0.526] | 0.513 (3259) [0.495, 0.531] | 0.533 (287) [0.465, 0.601] | 0.549 (91) | 0.500 | flat -0.030 (noise 0.033) |
| colour_clear | 0.563 (766) | 0.515 (5282) [0.493, 0.538] | 0.503 (23277) [0.496, 0.510] | 0.501 (26399) [0.495, 0.507] | 0.556 (2161) [0.550, 0.561] | 0.521 (744) | 0.500 | flat +0.018 (noise 0.014) |
| colour_confident | 0.718 (103) | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.642 (447) [0.617, 0.686] | 0.509 (159) | 0.500 | - |
| colour_next | 0.552 (1430) | 0.518 (9994) [0.504, 0.532] | 0.504 (42889) [0.499, 0.510] | 0.504 (48600) [0.499, 0.509] | 0.541 (4251) [0.530, 0.551] | 0.506 (1364) | 0.500 | flat +0.019 (noise 0.010) |
| colour_path | 0.508 (20020) | 0.502 (139916) [0.499, 0.506] | 0.501 (600446) [0.500, 0.503] | 0.501 (680400) [0.500, 0.502] | 0.502 (59514) [0.497, 0.507] | 0.497 (19096) | 0.500 | flat +0.002 (noise 0.002) |
| colour_strong | 0.800 (15) | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.669 (130) [0.650, 0.737] | 0.514 (35) | 0.500 | - |
| reversal_k13_next | 0.288 (73) | 0.291 (635) [0.267, 0.316] | 0.308 (2020) [0.293, 0.324] | 0.303 (2366) [0.288, 0.318] | 0.326 (261) [0.302, 0.347] | 0.303 (66) | 0.077 | flat -0.009 (noise 0.029) |
| reversal_k13_now | 0.559 (68) | 0.581 (387) [0.535, 0.631] | 0.587 (1468) [0.564, 0.610] | 0.586 (1650) [0.566, 0.606] | 0.624 (178) [0.572, 0.690] | 0.500 (60) | 0.077 | flat -0.030 (noise 0.037) |
| reversal_k3_next | 0.653 (49) | 0.590 (656) [0.564, 0.621] | 0.584 (2457) [0.569, 0.599] | 0.586 (2757) [0.573, 0.601] | 0.577 (317) [0.552, 0.622] | 0.683 (41) | 0.292 | flat +0.039 (noise 0.029) |
| reversal_k3_now | 0.958 (48) | 0.940 (417) [0.930, 0.952] | 0.941 (1702) [0.933, 0.950] | 0.941 (1932) [0.933, 0.949] | 0.935 (169) [0.924, 0.948] | 0.895 (57) | 0.292 | flat +0.004 (noise 0.017) |
| reversal_k5_next | 0.538 (39) | 0.466 (726) [0.435, 0.498] | 0.486 (2120) [0.466, 0.506] | 0.487 (2338) [0.470, 0.505] | 0.448 (348) [0.420, 0.505] | 0.489 (45) | 0.187 | flat -0.042 (noise 0.036) |
| reversal_k5_now | 0.867 (45) | 0.853 (395) [0.839, 0.870] | 0.838 (1583) [0.823, 0.852] | 0.840 (1785) [0.825, 0.854] | 0.862 (174) [0.832, 0.889] | 0.755 (53) | 0.187 | flat +0.019 (noise 0.027) |
| reversal_k8_next | 0.365 (74) | 0.400 (468) [0.365, 0.433] | 0.401 (2030) [0.383, 0.421] | 0.397 (2344) [0.381, 0.415] | 0.408 (238) [0.369, 0.442] | 0.412 (85) | 0.122 | flat -0.009 (noise 0.034) |
| reversal_k8_now | 0.770 (61) | 0.740 (358) [0.711, 0.764] | 0.724 (1569) [0.705, 0.743] | 0.720 (1758) [0.701, 0.739] | 0.778 (171) [0.773, 0.782] | 0.645 (62) | 0.122 | flat -0.015 (noise 0.033) |
| overall | 0.512 (22002) | 0.505 (154621) [0.502, 0.509] | 0.503 (661159) [0.502, 0.505] | 0.503 (749189) [0.502, 0.504] | 0.507 (65908) [0.502, 0.512] | 0.500 (21020) | - | flat +0.002 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07772, 0.1158] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5339, 'levels': [{'threshold': 0.07772, 'calls_per_day': 144.7, 'win_rate': 0.5841}, {'threshold': 0.1158, 'calls_per_day': 36.5, 'win_rate': 0.6395}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 4483, 'rate': 0.538}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15340 | 0.332 | 0.512 (15096) | 0.607 (540) | 0.779 (2460) |
| volatility: normal | 15339 | 0.358 | 0.508 (15271) | 0.564 (55) | 0.778 (2188) |
| volatility: wild | 15340 | 0.373 | 0.494 (15295) | - | 0.776 (2128) |
| session: Asia 00-08 | 15360 | 0.351 | 0.505 (15248) | 0.604 (207) | 0.780 (2230) |
| session: Europe 08-13 | 9600 | 0.347 | 0.503 (9525) | 0.549 (111) | 0.770 (1465) |
| session: US 13-21 | 15360 | 0.363 | 0.505 (15252) | 0.611 (185) | 0.786 (2282) |
| session: late 21-24 | 5699 | 0.351 | 0.506 (5637) | 0.670 (103) | 0.763 (799) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.294 | 0.295 | 0.223 | 0.223 | 0.414 | 0.194 | 0.394 | 1.708 |
| 6h | 360 | 0.340 | 0.338 | 0.282 | 0.314 | 0.483 | 0.236 | 0.445 | 1.272 |
| 24h | 1440 | 0.358 | 0.352 | 0.284 | 0.311 | 0.507 | 0.256 | 0.459 | 1.189 |
| 7d | 10080 | 0.351 | 0.348 | 0.275 | 0.299 | 0.518 | 0.245 | 0.456 | 1.285 |
| 30d | 43200 | 0.356 | 0.354 | 0.278 | 0.308 | 0.505 | 0.247 | 0.465 | 1.289 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.294 / 0.414 / 0.950; 2: 0.339 / 0.500 / 0.983; 3: 0.338 / 0.569 / 0.983; 4: 0.290 / 0.414 / 0.950; 5: 0.340 / 0.569 / 0.883; 6: 0.310 / 0.500 / 0.867; 7: 0.307 / 0.517 / 0.967; 8: 0.292 / 0.448 / 0.967; 9: 0.305 / 0.500 / 1.000; 10: 0.303 / 0.483 / 0.933; 11: 0.294 / 0.500 / 1.000; 12: 0.324 / 0.500 / 1.000; 13: 0.303 / 0.500 / 0.983; 14: 0.317 / 0.517 / 0.983; 15: 0.304 / 0.466 / 0.983
- 6h: 1: 0.340 / 0.483 / 0.919; 2: 0.340 / 0.497 / 0.928; 3: 0.354 / 0.539 / 0.931; 4: 0.341 / 0.489 / 0.911; 5: 0.343 / 0.486 / 0.900; 6: 0.346 / 0.511 / 0.911; 7: 0.328 / 0.469 / 0.933; 8: 0.322 / 0.441 / 0.939; 9: 0.337 / 0.489 / 0.942; 10: 0.335 / 0.489 / 0.953; 11: 0.326 / 0.472 / 0.953; 12: 0.343 / 0.503 / 0.947; 13: 0.338 / 0.542 / 0.947; 14: 0.344 / 0.525 / 0.947; 15: 0.333 / 0.461 / 0.942
- 24h: 1: 0.358 / 0.507 / 0.908; 2: 0.350 / 0.503 / 0.906; 3: 0.350 / 0.502 / 0.899; 4: 0.347 / 0.493 / 0.903; 5: 0.346 / 0.492 / 0.901; 6: 0.345 / 0.502 / 0.902; 7: 0.340 / 0.493 / 0.897; 8: 0.341 / 0.485 / 0.906; 9: 0.339 / 0.487 / 0.901; 10: 0.346 / 0.511 / 0.902; 11: 0.343 / 0.505 / 0.906; 12: 0.349 / 0.500 / 0.902; 13: 0.350 / 0.531 / 0.910; 14: 0.343 / 0.488 / 0.911; 15: 0.344 / 0.489 / 0.906
- 7d: 1: 0.351 / 0.518 / 0.899; 2: 0.345 / 0.503 / 0.900; 3: 0.346 / 0.512 / 0.901; 4: 0.342 / 0.501 / 0.901; 5: 0.341 / 0.502 / 0.901; 6: 0.341 / 0.499 / 0.901; 7: 0.342 / 0.505 / 0.901; 8: 0.340 / 0.499 / 0.901; 9: 0.336 / 0.491 / 0.901; 10: 0.339 / 0.505 / 0.902; 11: 0.340 / 0.506 / 0.902; 12: 0.341 / 0.511 / 0.901; 13: 0.342 / 0.509 / 0.901; 14: 0.337 / 0.493 / 0.902; 15: 0.338 / 0.495 / 0.902
- 30d: 1: 0.356 / 0.505 / 0.899; 2: 0.352 / 0.498 / 0.900; 3: 0.353 / 0.507 / 0.900; 4: 0.350 / 0.499 / 0.900; 5: 0.350 / 0.501 / 0.900; 6: 0.349 / 0.503 / 0.900; 7: 0.349 / 0.506 / 0.900; 8: 0.349 / 0.504 / 0.900; 9: 0.346 / 0.498 / 0.900; 10: 0.348 / 0.504 / 0.901; 11: 0.347 / 0.502 / 0.900; 12: 0.346 / 0.502 / 0.900; 13: 0.346 / 0.502 / 0.900; 14: 0.345 / 0.495 / 0.900; 15: 0.345 / 0.496 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.116 (body 0.077, range 0.154); 'price stays where it was' would score 0.116; colour right 0.517; typical miss of the close 2.6 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.102 (body 0.059, range 0.144); 'price stays where it was' would score 0.112; colour right 0.489; typical miss of the close 4.3 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.111 (body 0.074, range 0.148); 'price stays where it was' would score 0.124; colour right 0.494; typical miss of the close 5.7 bp; chain ended on the right side 0.542 of 96 chains; n=1440
- 7d: match 0.115 (body 0.076, range 0.154); 'price stays where it was' would score 0.120; colour right 0.496; typical miss of the close 6.1 bp; chain ended on the right side 0.524 of 670 chains; n=10080
- 30d: match 0.120 (body 0.080, range 0.159); 'price stays where it was' would score 0.126; colour right 0.498; typical miss of the close 8.1 bp; chain ended on the right side 0.510 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.366 / 4.2; 2: 0.199 / 4.4; 3: 0.169 / 6.0; 4: 0.133 / 6.5; 5: 0.123 / 7.3; 6: 0.111 / 8.1; 7: 0.099 / 8.5; 8: 0.090 / 8.9; 9: 0.085 / 9.2; 10: 0.080 / 10.1; 11: 0.074 / 10.7; 12: 0.072 / 11.0; 13: 0.064 / 11.3; 14: 0.066 / 11.5; 15: 0.061 / 11.5

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1790553600, labels learned 93293, probability skill vs chance 0.2367, widened contest next: False
  - now: threshold 0.8427, hit rate recent 0.9194 / long run 0.936
    - 6h: 13 calls (53 a day), hit rate 1.000, chance 0.311, naive rule 0.539, lift 3.21x
    - 24h: 58 calls (58 a day), hit rate 0.897, chance 0.302, naive rule 0.502, lift 2.96x
    - 7d: 410 calls (59 a day), hit rate 0.929, chance 0.294, naive rule 0.492, lift 3.17x
    - 30d: 1701 calls (57 a day), hit rate 0.939, chance 0.292, naive rule 0.482, lift 3.22x
  - next: threshold 0.5633, hit rate recent 0.6578 / long run 0.5915
    - 6h: 15 calls (61 a day), hit rate 0.667, chance 0.311, lift 2.14x
    - 24h: 42 calls (42 a day), hit rate 0.690, chance 0.302, lift 2.28x
    - 7d: 602 calls (86 a day), hit rate 0.586, chance 0.294, lift 2.00x
    - 30d: 2412 calls (80 a day), hit rate 0.585, chance 0.292, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.494; 0.35: 538, 0.518; 0.40: 487, 0.561; 0.45: 421, 0.627; 0.50: 367, 0.680; 0.55: 322, 0.724; 0.60: 275, 0.767; 0.65: 225, 0.803; 0.70: 182, 0.835; 0.75: 139, 0.871; 0.80: 98, 0.909; 0.85: 49, 0.948; 0.90: 2, 0.980
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 583, 0.424; 0.35: 497, 0.459; 0.40: 413, 0.488; 0.45: 316, 0.520; 0.50: 207, 0.552; 0.55: 92, 0.586; 0.60: 13, 0.622; 0.65: 1, 0.765
- **K=5**: model 1790208000, labels learned 93291, probability skill vs chance 0.2166, widened contest next: False
  - now: threshold 0.7138, hit rate recent 0.8163 / long run 0.8389
    - 6h: 15 calls (61 a day), hit rate 0.933, chance 0.208, naive rule 0.475, lift 4.48x
    - 24h: 57 calls (57 a day), hit rate 0.754, chance 0.196, naive rule 0.412, lift 3.85x
    - 7d: 393 calls (56 a day), hit rate 0.842, chance 0.191, naive rule 0.403, lift 4.40x
    - 30d: 1579 calls (53 a day), hit rate 0.837, chance 0.186, naive rule 0.390, lift 4.49x
  - next: threshold 0.4558, hit rate recent 0.5109 / long run 0.478
    - 6h: 12 calls (49 a day), hit rate 0.583, chance 0.208, lift 2.80x
    - 24h: 48 calls (48 a day), hit rate 0.479, chance 0.196, lift 2.44x
    - 7d: 722 calls (103 a day), hit rate 0.463, chance 0.191, lift 2.42x
    - 30d: 2099 calls (70 a day), hit rate 0.486, chance 0.186, lift 2.61x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 431, 0.412; 0.35: 370, 0.465; 0.40: 299, 0.534; 0.45: 245, 0.592; 0.50: 190, 0.650; 0.55: 144, 0.699; 0.60: 113, 0.740; 0.65: 86, 0.785; 0.70: 64, 0.821; 0.75: 34, 0.862; 0.80: 9, 0.886
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 340, 0.385; 0.35: 254, 0.423; 0.40: 166, 0.449; 0.45: 86, 0.474; 0.50: 21, 0.523; 0.55: 2, 0.597
- **K=8**: model 1791158400, labels learned 93288, probability skill vs chance 0.1981, widened contest next: False
  - now: threshold 0.5645, hit rate recent 0.7012 / long run 0.7282
    - 6h: 15 calls (62 a day), hit rate 0.667, chance 0.107, naive rule 0.331, lift 6.22x
    - 24h: 65 calls (65 a day), hit rate 0.646, chance 0.120, naive rule 0.332, lift 5.40x
    - 7d: 375 calls (54 a day), hit rate 0.733, chance 0.126, naive rule 0.339, lift 5.83x
    - 30d: 1570 calls (52 a day), hit rate 0.725, chance 0.121, naive rule 0.325, lift 5.99x
  - next: threshold 0.3474, hit rate recent 0.4094 / long run 0.4077
    - 6h: 23 calls (95 a day), hit rate 0.348, chance 0.107, lift 3.25x
    - 24h: 88 calls (89 a day), hit rate 0.409, chance 0.120, lift 3.42x
    - 7d: 493 calls (70 a day), hit rate 0.398, chance 0.126, lift 3.16x
    - 30d: 2041 calls (68 a day), hit rate 0.403, chance 0.121, lift 3.33x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 274, 0.399; 0.35: 206, 0.475; 0.40: 159, 0.536; 0.45: 126, 0.584; 0.50: 96, 0.628; 0.55: 68, 0.684; 0.60: 46, 0.729; 0.65: 24, 0.767; 0.70: 9, 0.805; 0.75: 1, 0.828
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 187, 0.344; 0.35: 116, 0.384; 0.40: 48, 0.414; 0.45: 10, 0.425; 0.50: 1, 0.421
- **K=13**: model 1791072000, labels learned 93283, probability skill vs chance 0.1748, widened contest next: True
  - now: threshold 0.4197, hit rate recent 0.5434 / long run 0.5837
    - 6h: 16 calls (67 a day), hit rate 0.500, chance 0.062, naive rule 0.229, lift 8.02x
    - 24h: 63 calls (64 a day), hit rate 0.508, chance 0.068, naive rule 0.243, lift 7.50x
    - 7d: 392 calls (56 a day), hit rate 0.587, chance 0.078, naive rule 0.272, lift 7.51x
    - 30d: 1481 calls (49 a day), hit rate 0.583, chance 0.077, naive rule 0.266, lift 7.63x
  - next: threshold 0.2777, hit rate recent 0.308 / long run 0.3038
    - 6h: 19 calls (79 a day), hit rate 0.211, chance 0.062, lift 3.38x
    - 24h: 71 calls (72 a day), hit rate 0.310, chance 0.068, lift 4.58x
    - 7d: 598 calls (86 a day), hit rate 0.296, chance 0.078, lift 3.79x
    - 30d: 2029 calls (68 a day), hit rate 0.307, chance 0.077, lift 4.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 123, 0.436; 0.35: 90, 0.493; 0.40: 64, 0.543; 0.45: 45, 0.600; 0.50: 28, 0.616; 0.55: 15, 0.668; 0.60: 6, 0.701; 0.65: 2, 0.755; 0.70: 0, 0.600
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 51, 0.313; 0.35: 17, 0.353; 0.40: 4, 0.336; 0.45: 1, 0.381

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 4.449 | 12.38% | 0.950 | 0.583 | 0.255 | 0.414 | 0.504 |
| 6h | 6.686 | 2.78% | 0.908 | 0.522 | 0.252 | 0.489 | 0.427 |
| 24h | 8.918 | 2.94% | 0.901 | 0.501 | 0.251 | 0.485 | 0.473 |
| 7d | 10.798 | 4.68% | 0.901 | 0.500 | 0.251 | 0.495 | 0.682 |
| 30d | 14.123 | 4.18% | 0.900 | 0.500 | 0.251 | 0.497 | 0.694 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 5.077 | 4.450 | 4.486 | 4.380 | 4.641 | 4.624 | 4.419 | 4.410 | 4.431 | 4.449 |
| 6h | 6.878 | 6.698 | 6.698 | 6.694 | 6.781 | 6.767 | 6.674 | 6.671 | 6.672 | 6.686 |
| 24h | 9.188 | 8.986 | 8.956 | 8.911 | 9.064 | 9.041 | 8.928 | 8.919 | 8.902 | 8.918 |
| 7d | 11.328 | 10.890 | 10.884 | 10.827 | 11.026 | 10.988 | 10.793 | 10.788 | 10.780 | 10.798 |
| 30d | 14.740 | 14.252 | 14.207 | 14.150 | 14.393 | 14.337 | 14.126 | 14.098 | 14.096 | 14.123 |

## Next candle

- candle starting 2026-10-06 22:59 UTC, last close 2696.34
- P(up) 0.5168, return quantiles (bp): {'05': -2.165, '10': -1.598, '25': -0.803, '40': -0.222, '50': 0.043, '60': 0.282, '75': 0.676, '90': 1.675, '95': 2.228}
- changepoint probability 0.0191, regime age 84.1 min
- agent weights: empirical 0.006, ewma 0.121, garch 0.148, har 0.222, bocpd 0.045, hmm 0.047, online_qr 0.195, lgbm 0.216

## Learning log

- 2026-10-04 12:00 UTC: {"garch": {"alpha": 0.0822, "beta": 0.9141}, "hmm": {"sd_bp": [1.75, 4.62, 12.53], "stay": [0.973, 0.963, 0.932]}}
- 2026-10-05 00:00 UTC: {"garch": {"alpha": 0.0824, "beta": 0.9129}, "hmm": {"sd_bp": [1.75, 4.48, 11.78], "stay": [0.971, 0.951, 0.918]}, "lgbm": {"challenger_loss": 0.25325, "champion_loss": 0.25317, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48652, "challengers": 1, "chance_loss": 0.6045, "widened": false, "champion_loss": 0.48437, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37186, "challengers": 1, "chance_loss": 0.47797, "widened": false, "champion_loss": 0.37143, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28228, "challengers": 1, "chance_loss": 0.37838, "widened": false, "champion_loss": 0.28279, "promoted": true}, "reversal_k13": {"challenger_loss": 0.20596, "challengers": 1, "chance_loss": 0.28931, "widened": false, "champion_loss": 0.20534, "promoted": false}}
- 2026-10-05 12:00 UTC: {"garch": {"alpha": 0.0799, "beta": 0.9158}, "hmm": {"sd_bp": [1.73, 4.67, 11.81], "stay": [0.97, 0.951, 0.896]}}
- 2026-10-06 00:00 UTC: {"garch": {"alpha": 0.0779, "beta": 0.9171}, "hmm": {"sd_bp": [1.76, 4.58, 12.58], "stay": [0.968, 0.946, 0.896]}, "lgbm": {"challenger_loss": 0.25204, "champion_loss": 0.25219, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48084, "challengers": 1, "chance_loss": 0.60737, "widened": false, "champion_loss": 0.47951, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37424, "challengers": 1, "chance_loss": 0.48796, "widened": false, "champion_loss": 0.37382, "promoted": false}, "reversal_k8": {"challenger_loss": 0.28793, "challengers": 1, "chance_loss": 0.38611, "widened": false, "champion_loss": 0.28759, "promoted": false}, "reversal_k13": {"challenger_loss": 0.2089, "challengers": 1, "chance_loss": 0.28669, "widened": false, "champion_loss": 0.2087, "promoted": false}}
- 2026-10-06 12:00 UTC: {"garch": {"alpha": 0.078, "beta": 0.9157}, "hmm": {"sd_bp": [1.78, 4.45, 12.43], "stay": [0.968, 0.941, 0.914]}}
- HMM volatility states (sd, bp per minute): [1.78, 4.45, 12.43], current probabilities: [0.975, 0.025, 0.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-06 23:10 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.194, 'l_abs': 0.64, 'l_hi': 0.76, 'l_lo': 0.752, 'b05': 0.712, 'b25': 0.643, 'b75': 0.707, 'b95': 0.709}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.6], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6], [1.3, 1.6], [1.3, 1.8], [1.3, 1.6]], 'cone_width': [1.174, 1.441, 1.735, 1.944, 1.97, 2.09, 2.284, 2.736, 2.228, 2.588, 2.602, 2.505, 2.554, 2.702]}
- calibration offsets (in sigma): {'05': 0.049, '10': 0.028, '25': -0.005, '40': 0.032, '50': 0.02, '60': -0.002, '75': -0.065, '90': -0.018, '95': -0.069}
