# ETH-USD 60s candle generator - report

- generated: 2026-10-14 12:47 UTC
- last closed candle: 2026-10-14 12:47 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- reversal agent K=5: recent hit rate is below its long-run level - its next daily contest is widened
- reversal agent K=13: recent hit rate is below its long-run level - its next daily contest is widened

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.521 (96) | 0.489 (671) [0.448, 0.530] | 0.509 (2875) [0.489, 0.530] | 0.510 (4026) [0.494, 0.526] | 0.508 (1054) [0.473, 0.542] | 0.569 (51) | 0.500 | flat -0.035 (noise 0.034) |
| colour_clear | 0.526 (780) | 0.538 (5463) [0.532, 0.544] | 0.512 (23311) [0.504, 0.520] | 0.508 (32638) [0.502, 0.514] | 0.541 (8400) [0.535, 0.547] | 0.586 (459) | 0.500 | flat +0.018 (noise 0.013) |
| colour_confident | 0.633 (60) | 0.605 (926) [0.583, 0.636] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.606 (1541) [0.580, 0.633] | 0.544 (57) | 0.500 | flat -0.003 (noise 0.038) |
| colour_next | 0.514 (1433) | 0.523 (9974) [0.519, 0.527] | 0.510 (42868) [0.504, 0.515] | 0.507 (59997) [0.503, 0.512] | 0.527 (15648) [0.521, 0.533] | 0.567 (764) | 0.500 | flat +0.004 (noise 0.008) |
| colour_path | 0.504 (20062) | 0.499 (139636) [0.496, 0.501] | 0.501 (600152) [0.500, 0.503] | 0.500 (839958) [0.499, 0.501] | 0.500 (219072) [0.497, 0.502] | 0.506 (10696) | 0.500 | flat -0.003 (noise 0.003) |
| colour_strong | 0.714 (7) | 0.676 (250) [0.633, 0.740] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.659 (419) [0.623, 0.700] | 0.462 (13) | 0.500 | flat +0.043 (noise 0.052) |
| reversal_k13_next | 0.270 (74) | 0.321 (495) [0.299, 0.343] | 0.316 (2093) [0.302, 0.331] | 0.306 (2932) [0.294, 0.319] | 0.323 (827) [0.307, 0.338] | 0.241 (29) | 0.077 | flat +0.020 (noise 0.028) |
| reversal_k13_now | 0.651 (43) | 0.589 (353) [0.560, 0.621] | 0.592 (1488) [0.572, 0.614] | 0.584 (2066) [0.567, 0.601] | 0.591 (594) [0.562, 0.625] | 0.518 (27) | 0.077 | flat +0.003 (noise 0.036) |
| reversal_k3_next | 0.539 (165) | 0.566 (664) [0.541, 0.592] | 0.585 (2478) [0.570, 0.600] | 0.584 (3466) [0.571, 0.597] | 0.575 (1026) [0.555, 0.599] | 0.609 (46) | 0.293 | flat -0.021 (noise 0.028) |
| reversal_k3_now | 0.977 (44) | 0.926 (417) [0.915, 0.941] | 0.939 (1717) [0.931, 0.947] | 0.937 (2410) [0.930, 0.945] | 0.926 (647) [0.917, 0.936] | 1.000 (29) | 0.293 | flat -0.004 (noise 0.018) |
| reversal_k5_next | 0.481 (104) | 0.468 (524) [0.440, 0.488] | 0.484 (2110) [0.466, 0.502] | 0.484 (2911) [0.469, 0.500] | 0.462 (921) [0.439, 0.486] | 0.489 (47) | 0.187 | flat +0.004 (noise 0.029) |
| reversal_k5_now | 0.804 (46) | 0.809 (367) [0.784, 0.836] | 0.832 (1586) [0.816, 0.848] | 0.833 (2208) [0.819, 0.846] | 0.821 (597) [0.796, 0.845] | 0.789 (19) | 0.188 | flat -0.033 (noise 0.028) |
| reversal_k8_next | 0.407 (81) | 0.387 (607) [0.363, 0.414] | 0.411 (2117) [0.394, 0.429] | 0.396 (3040) [0.383, 0.410] | 0.395 (934) [0.375, 0.416] | 0.394 (33) | 0.122 | flat -0.013 (noise 0.030) |
| reversal_k8_now | 0.674 (46) | 0.669 (393) [0.639, 0.703] | 0.717 (1590) [0.696, 0.738] | 0.709 (2217) [0.692, 0.726] | 0.697 (630) [0.665, 0.730] | 0.704 (27) | 0.122 | flat -0.065 (noise 0.033) |
| overall | 0.506 (22194) | 0.502 (154101) [0.499, 0.505] | 0.504 (661074) [0.503, 0.505] | 0.503 (925231) [0.502, 0.504] | 0.503 (241950) [0.501, 0.506] | 0.512 (11768) | - | flat -0.003 (noise 0.003) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07641, 0.1185] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5253, 'levels': [{'threshold': 0.07641, 'calls_per_day': 142.1, 'win_rate': 0.6}, {'threshold': 0.1185, 'calls_per_day': 35.6, 'win_rate': 0.6627}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 15275, 'rate': 0.5303}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 15136 | 0.334 | 0.519 (14888) | 0.597 (1214) | 0.779 (2433) |
| volatility: normal | 15135 | 0.361 | 0.512 (15070) | 0.603 (282) | 0.772 (2127) |
| volatility: wild | 15136 | 0.374 | 0.501 (15092) | 0.686 (102) | 0.774 (2120) |
| session: Asia 00-08 | 15360 | 0.353 | 0.515 (15251) | 0.605 (575) | 0.777 (2211) |
| session: Europe 08-13 | 9587 | 0.350 | 0.508 (9504) | 0.582 (407) | 0.778 (1469) |
| session: US 13-21 | 14880 | 0.366 | 0.508 (14780) | 0.588 (388) | 0.781 (2165) |
| session: late 21-24 | 5580 | 0.349 | 0.509 (5515) | 0.667 (228) | 0.751 (835) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.403 | 0.360 | 0.295 | 0.295 | 0.583 | 0.298 | 0.509 | 1.032 |
| 6h | 360 | 0.369 | 0.341 | 0.280 | 0.312 | 0.567 | 0.272 | 0.466 | 1.277 |
| 24h | 1440 | 0.375 | 0.359 | 0.286 | 0.324 | 0.537 | 0.270 | 0.481 | 1.123 |
| 7d | 10080 | 0.357 | 0.349 | 0.273 | 0.302 | 0.526 | 0.258 | 0.455 | 1.259 |
| 30d | 43200 | 0.357 | 0.355 | 0.279 | 0.308 | 0.511 | 0.249 | 0.465 | 1.294 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.403 / 0.583 / 0.883; 2: 0.356 / 0.517 / 0.783; 3: 0.347 / 0.433 / 0.767; 4: 0.354 / 0.550 / 0.767; 5: 0.330 / 0.400 / 0.650; 6: 0.393 / 0.667 / 0.617; 7: 0.318 / 0.417 / 0.600; 8: 0.339 / 0.500 / 0.533; 9: 0.325 / 0.417 / 0.533; 10: 0.360 / 0.533 / 0.550; 11: 0.332 / 0.483 / 0.567; 12: 0.316 / 0.450 / 0.567; 13: 0.322 / 0.467 / 0.533; 14: 0.337 / 0.567 / 0.550; 15: 0.347 / 0.550 / 0.533
- 6h: 1: 0.369 / 0.567 / 0.892; 2: 0.341 / 0.486 / 0.831; 3: 0.348 / 0.508 / 0.878; 4: 0.349 / 0.517 / 0.872; 5: 0.342 / 0.497 / 0.839; 6: 0.356 / 0.547 / 0.819; 7: 0.325 / 0.447 / 0.844; 8: 0.342 / 0.494 / 0.814; 9: 0.330 / 0.430 / 0.806; 10: 0.334 / 0.486 / 0.828; 11: 0.345 / 0.514 / 0.825; 12: 0.331 / 0.486 / 0.833; 13: 0.351 / 0.536 / 0.808; 14: 0.343 / 0.522 / 0.831; 15: 0.345 / 0.545 / 0.833
- 24h: 1: 0.375 / 0.537 / 0.903; 2: 0.358 / 0.496 / 0.883; 3: 0.362 / 0.500 / 0.885; 4: 0.361 / 0.496 / 0.885; 5: 0.365 / 0.524 / 0.877; 6: 0.363 / 0.514 / 0.875; 7: 0.360 / 0.496 / 0.878; 8: 0.358 / 0.503 / 0.874; 9: 0.359 / 0.494 / 0.871; 10: 0.362 / 0.516 / 0.874; 11: 0.353 / 0.495 / 0.874; 12: 0.359 / 0.498 / 0.874; 13: 0.363 / 0.523 / 0.871; 14: 0.358 / 0.497 / 0.870; 15: 0.362 / 0.520 / 0.872
- 7d: 1: 0.357 / 0.526 / 0.900; 2: 0.345 / 0.496 / 0.900; 3: 0.348 / 0.511 / 0.900; 4: 0.345 / 0.496 / 0.900; 5: 0.347 / 0.507 / 0.899; 6: 0.344 / 0.499 / 0.898; 7: 0.344 / 0.501 / 0.898; 8: 0.344 / 0.501 / 0.897; 9: 0.341 / 0.491 / 0.897; 10: 0.345 / 0.505 / 0.898; 11: 0.341 / 0.493 / 0.898; 12: 0.343 / 0.499 / 0.898; 13: 0.344 / 0.504 / 0.897; 14: 0.342 / 0.503 / 0.897; 15: 0.344 / 0.500 / 0.897
- 30d: 1: 0.357 / 0.511 / 0.900; 2: 0.351 / 0.497 / 0.900; 3: 0.354 / 0.510 / 0.900; 4: 0.350 / 0.498 / 0.900; 5: 0.350 / 0.504 / 0.900; 6: 0.349 / 0.502 / 0.900; 7: 0.349 / 0.505 / 0.900; 8: 0.349 / 0.503 / 0.899; 9: 0.345 / 0.495 / 0.899; 10: 0.348 / 0.505 / 0.899; 11: 0.346 / 0.500 / 0.899; 12: 0.347 / 0.503 / 0.899; 13: 0.347 / 0.502 / 0.899; 14: 0.345 / 0.498 / 0.899; 15: 0.345 / 0.496 / 0.899

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.082 (body 0.062, range 0.102); 'price stays where it was' would score 0.083; colour right 0.417; typical miss of the close 21.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.106 (body 0.074, range 0.138); 'price stays where it was' would score 0.106; colour right 0.486; typical miss of the close 9.8 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.121 (body 0.080, range 0.162); 'price stays where it was' would score 0.127; colour right 0.493; typical miss of the close 8.5 bp; chain ended on the right side 0.562 of 96 chains; n=1440
- 7d: match 0.121 (body 0.083, range 0.159); 'price stays where it was' would score 0.125; colour right 0.496; typical miss of the close 7.2 bp; chain ended on the right side 0.502 of 671 chains; n=10080
- 30d: match 0.119 (body 0.079, range 0.158); 'price stays where it was' would score 0.124; colour right 0.497; typical miss of the close 8.0 bp; chain ended on the right side 0.512 of 2875 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.364 / 4.1; 2: 0.197 / 4.5; 3: 0.164 / 6.1; 4: 0.132 / 6.7; 5: 0.119 / 7.4; 6: 0.107 / 8.0; 7: 0.100 / 8.4; 8: 0.094 / 8.7; 9: 0.086 / 8.8; 10: 0.082 / 9.6; 11: 0.077 / 10.3; 12: 0.075 / 10.8; 13: 0.062 / 10.9; 14: 0.064 / 11.2; 15: 0.059 / 11.2

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 104201, probability skill vs chance 0.229, widened contest next: False
  - now: threshold 0.8423, hit rate recent 0.9628 / long run 0.9344
    - 6h: 17 calls (69 a day), hit rate 1.000, chance 0.301, naive rule 0.507, lift 3.32x
    - 24h: 52 calls (52 a day), hit rate 0.981, chance 0.293, naive rule 0.480, lift 3.34x
    - 7d: 425 calls (61 a day), hit rate 0.927, chance 0.296, naive rule 0.498, lift 3.14x
    - 30d: 1723 calls (57 a day), hit rate 0.940, chance 0.290, naive rule 0.482, lift 3.24x
  - next: threshold 0.5649, hit rate recent 0.5783 / long run 0.5781
    - 6h: 16 calls (65 a day), hit rate 0.625, chance 0.301, lift 2.07x
    - 24h: 118 calls (118 a day), hit rate 0.559, chance 0.293, lift 1.91x
    - 7d: 682 calls (97 a day), hit rate 0.573, chance 0.296, lift 1.94x
    - 30d: 2484 calls (83 a day), hit rate 0.584, chance 0.290, lift 2.01x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 566, 0.490; 0.35: 539, 0.513; 0.40: 484, 0.561; 0.45: 416, 0.630; 0.50: 363, 0.683; 0.55: 318, 0.726; 0.60: 271, 0.770; 0.65: 224, 0.800; 0.70: 180, 0.833; 0.75: 139, 0.872; 0.80: 96, 0.913; 0.85: 49, 0.950; 0.90: 3, 0.977
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 582, 0.424; 0.35: 497, 0.459; 0.40: 410, 0.488; 0.45: 315, 0.523; 0.50: 204, 0.558; 0.55: 92, 0.582; 0.60: 14, 0.600; 0.65: 1, 0.640
- **K=5**: model 1791590400, labels learned 104199, probability skill vs chance 0.2156, widened contest next: True
  - now: threshold 0.7036, hit rate recent 0.7945 / long run 0.8249
    - 6h: 12 calls (49 a day), hit rate 0.750, chance 0.191, naive rule 0.416, lift 3.92x
    - 24h: 39 calls (39 a day), hit rate 0.795, chance 0.177, naive rule 0.369, lift 4.48x
    - 7d: 364 calls (52 a day), hit rate 0.808, chance 0.189, naive rule 0.404, lift 4.28x
    - 30d: 1586 calls (53 a day), hit rate 0.830, chance 0.187, naive rule 0.392, lift 4.45x
  - next: threshold 0.4276, hit rate recent 0.4899 / long run 0.4764
    - 6h: 26 calls (106 a day), hit rate 0.577, chance 0.191, lift 3.02x
    - 24h: 97 calls (97 a day), hit rate 0.454, chance 0.177, lift 2.56x
    - 7d: 539 calls (77 a day), hit rate 0.479, chance 0.189, lift 2.54x
    - 30d: 2129 calls (71 a day), hit rate 0.484, chance 0.187, lift 2.59x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 425, 0.417; 0.35: 356, 0.478; 0.40: 287, 0.549; 0.45: 235, 0.605; 0.50: 183, 0.659; 0.55: 139, 0.706; 0.60: 109, 0.748; 0.65: 83, 0.790; 0.70: 60, 0.821; 0.75: 33, 0.866; 0.80: 10, 0.893
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 338, 0.388; 0.35: 251, 0.424; 0.40: 162, 0.454; 0.45: 79, 0.473; 0.50: 19, 0.513; 0.55: 2, 0.566
- **K=8**: model 1791936000, labels learned 104196, probability skill vs chance 0.2111, widened contest next: False
  - now: threshold 0.5846, hit rate recent 0.6769 / long run 0.7007
    - 6h: 15 calls (62 a day), hit rate 0.667, chance 0.137, naive rule 0.400, lift 4.86x
    - 24h: 47 calls (47 a day), hit rate 0.681, chance 0.127, naive rule 0.333, lift 5.35x
    - 7d: 391 calls (56 a day), hit rate 0.662, chance 0.124, naive rule 0.345, lift 5.33x
    - 30d: 1591 calls (53 a day), hit rate 0.713, chance 0.122, naive rule 0.330, lift 5.83x
  - next: threshold 0.3721, hit rate recent 0.3979 / long run 0.3987
    - 6h: 15 calls (62 a day), hit rate 0.400, chance 0.137, lift 2.92x
    - 24h: 68 calls (68 a day), hit rate 0.368, chance 0.127, lift 2.89x
    - 7d: 592 calls (85 a day), hit rate 0.395, chance 0.124, lift 3.18x
    - 30d: 2114 calls (70 a day), hit rate 0.409, chance 0.122, lift 3.34x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 263, 0.414; 0.35: 199, 0.487; 0.40: 152, 0.547; 0.45: 120, 0.591; 0.50: 92, 0.634; 0.55: 66, 0.685; 0.60: 45, 0.726; 0.65: 24, 0.775; 0.70: 9, 0.832; 0.75: 1, 0.773
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 181, 0.352; 0.35: 109, 0.389; 0.40: 46, 0.423; 0.45: 10, 0.462; 0.50: 1, 0.378
- **K=13**: model 1791849600, labels learned 104191, probability skill vs chance 0.1911, widened contest next: True
  - now: threshold 0.4363, hit rate recent 0.5641 / long run 0.5837
    - 6h: 14 calls (58 a day), hit rate 0.429, chance 0.074, naive rule 0.315, lift 5.80x
    - 24h: 45 calls (45 a day), hit rate 0.556, chance 0.078, naive rule 0.284, lift 7.10x
    - 7d: 354 calls (51 a day), hit rate 0.579, chance 0.079, naive rule 0.286, lift 7.35x
    - 30d: 1487 calls (50 a day), hit rate 0.588, chance 0.078, naive rule 0.273, lift 7.55x
  - next: threshold 0.3007, hit rate recent 0.2651 / long run 0.3096
    - 6h: 12 calls (50 a day), hit rate 0.167, chance 0.074, lift 2.25x
    - 24h: 58 calls (59 a day), hit rate 0.259, chance 0.078, lift 3.31x
    - 7d: 494 calls (71 a day), hit rate 0.318, chance 0.079, lift 4.03x
    - 30d: 2083 calls (69 a day), hit rate 0.314, chance 0.078, lift 4.04x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 118, 0.451; 0.35: 85, 0.512; 0.40: 61, 0.563; 0.45: 42, 0.616; 0.50: 25, 0.648; 0.55: 14, 0.706; 0.60: 4, 0.756; 0.65: 1, 0.895
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 48, 0.328; 0.35: 14, 0.364; 0.40: 2, 0.422; 0.45: 0, 0.333

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 30.205 | 7.24% | 0.883 | 0.467 | 0.251 | 0.450 | 0.417 |
| 6h | 15.522 | 3.29% | 0.900 | 0.550 | 0.251 | 0.441 | 0.476 |
| 24h | 14.099 | 2.85% | 0.897 | 0.508 | 0.251 | 0.464 | 0.525 |
| 7d | 12.967 | 4.22% | 0.900 | 0.501 | 0.251 | 0.491 | 0.668 |
| 30d | 14.023 | 4.05% | 0.900 | 0.500 | 0.251 | 0.496 | 0.685 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 32.561 | 30.741 | 31.655 | 29.538 | 32.884 | 31.059 | 30.293 | 30.349 | 30.104 | 30.205 |
| 6h | 16.050 | 15.761 | 15.873 | 15.375 | 16.191 | 15.745 | 15.510 | 15.484 | 15.477 | 15.522 |
| 24h | 14.513 | 14.189 | 14.231 | 14.073 | 14.405 | 14.252 | 14.070 | 14.063 | 14.063 | 14.099 |
| 7d | 13.538 | 13.085 | 13.065 | 12.991 | 13.238 | 13.159 | 12.966 | 12.933 | 12.945 | 12.967 |
| 30d | 14.615 | 14.147 | 14.109 | 14.049 | 14.287 | 14.221 | 14.021 | 13.995 | 13.996 | 14.023 |

## Next candle

- candle starting 2026-10-14 12:47 UTC, last close 2475.03
- P(up) 0.5272, return quantiles (bp): {'05': -27.522, '10': -19.648, '25': -9.146, '40': -2.61, '50': 0.949, '60': 4.6, '75': 11.096, '90': 19.821, '95': 26.388}
- changepoint probability 0.1058, regime age 13.4 min
- agent weights: empirical 0.005, ewma 0.045, garch 0.024, har 0.408, bocpd 0.005, hmm 0.045, online_qr 0.216, lgbm 0.251

## Learning log

- 2026-10-12 12:00 UTC: {"garch": {"alpha": 0.1014, "beta": 0.8909}, "hmm": {"sd_bp": [2.02, 4.61, 13.8], "stay": [0.978, 0.967, 0.912]}}
- 2026-10-13 00:00 UTC: {"garch": {"alpha": 0.1114, "beta": 0.8763}, "hmm": {"sd_bp": [2.01, 4.48, 12.03], "stay": [0.977, 0.966, 0.895]}, "lgbm": {"challenger_loss": 0.25505, "champion_loss": 0.25507, "promoted": true}, "reversal_k3": {"challenger_loss": 0.48915, "challengers": 1, "chance_loss": 0.6132, "widened": false, "champion_loss": 0.48603, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37859, "challengers": 3, "chance_loss": 0.49163, "widened": true, "champion_loss": 0.37806, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27792, "challengers": 3, "chance_loss": 0.37544, "widened": true, "champion_loss": 0.27804, "promoted": true}, "reversal_k13": {"challenger_loss": 0.1947, "challengers": 3, "chance_loss": 0.26858, "widened": true, "champion_loss": 0.1948, "promoted": true}}
- 2026-10-13 12:00 UTC: {"garch": {"alpha": 0.1208, "beta": 0.869}, "hmm": {"sd_bp": [2.04, 4.71, 13.13], "stay": [0.978, 0.96, 0.892]}}
- 2026-10-14 00:00 UTC: {"garch": {"alpha": 0.1058, "beta": 0.8858}, "hmm": {"sd_bp": [2.05, 4.75, 12.9], "stay": [0.979, 0.957, 0.88]}, "lgbm": {"challenger_loss": 0.25311, "champion_loss": 0.25313, "promoted": true}, "reversal_k3": {"challenger_loss": 0.471, "challengers": 3, "chance_loss": 0.59613, "widened": true, "champion_loss": 0.4699, "promoted": false}, "reversal_k5": {"challenger_loss": 0.35688, "challengers": 3, "chance_loss": 0.46886, "widened": true, "champion_loss": 0.35599, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26784, "challengers": 3, "chance_loss": 0.36945, "widened": true, "champion_loss": 0.2685, "promoted": true}, "reversal_k13": {"challenger_loss": 0.18638, "challengers": 1, "chance_loss": 0.26601, "widened": false, "champion_loss": 0.18636, "promoted": false}}
- 2026-10-14 12:00 UTC: {"garch": {"alpha": 0.11, "beta": 0.8796}, "hmm": {"sd_bp": [2.03, 4.75, 13.0], "stay": [0.975, 0.963, 0.872]}}
- HMM volatility states (sd, bp per minute): [2.03, 4.75, 13.0], current probabilities: [0.0, 0.0, 1.0]
- live generator: {'versions': 60, 'latest_effective': '2026-10-14 12:55 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.483, 'l_abs': 0.702, 'l_hi': 0.736, 'l_lo': 0.714, 'b05': 0.76, 'b25': 0.642, 'b75': 0.716, 'b95': 0.749}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.4, 'ahead': [[1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8], [1.3, 1.8]], 'cone_width': [1.983, 2.116, 2.399, 3.417, 3.982, 4.141, 4.805, 5.315, 5.183, 5.339, 5.476, 6.312, 6.696, 6.673]}
- calibration offsets (in sigma): {'05': 0.033, '10': 0.096, '25': 0.025, '40': 0.024, '50': 0.01, '60': -0.004, '75': -0.005, '90': 0.004, '95': -0.013}
