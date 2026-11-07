# ETH-USD 60s candle generator - report

- generated: 2026-11-07 01:08 UTC
- last closed candle: 2026-11-07 01:08 UTC (staleness 0.3 min)
- this generation of the models went live: 2026-10-03 20:04 UTC (numbers for earlier days are a replay of history, minute by minute, with only the past visible)

## Goal keeper alerts

- WIN RATE FALLING: reversal_k3_now 0.915 in the last 7 days, -0.037 against the 7 before

## Win-rate ledger (complete UTC days; archived in ledger/winrate.csv)

win rate (predictions judged) [90% interval, resampling whole days]. `colour_confident`, `colour_strong` and `colour_clear` are selections of `colour_next` and are not counted again in `overall`.

| layer | last day | 7 days | 30 days | all | since go-live | today so far | chance | trend |
|---|---|---|---|---|---|---|---|---|
| chain_end_side | 0.490 (96) | 0.484 (672) [0.454, 0.512] | 0.514 (2879) [0.498, 0.531] | 0.512 (6330) [0.500, 0.525] | 0.513 (3358) [0.496, 0.532] | 1.000 (4) | 0.500 | flat -0.042 (noise 0.027) |
| colour_clear | 0.577 (807) | 0.534 (5528) [0.516, 0.553] | 0.542 (23933) [0.536, 0.548] | 0.521 (51854) [0.515, 0.526] | 0.543 (27616) [0.537, 0.548] | 0.487 (39) | 0.500 | flat -0.004 (noise 0.012) |
| colour_confident | 0.646 (96) | 0.578 (888) [0.561, 0.600] | 0.595 (4261) [0.584, 0.605] | 0.597 (4987) [0.586, 0.609] | 0.597 (4987) [0.586, 0.609] | 0.455 (11) | 0.500 | flat -0.015 (noise 0.022) |
| colour_next | 0.554 (1436) | 0.530 (9980) [0.519, 0.541] | 0.529 (42874) [0.525, 0.533] | 0.516 (94331) [0.512, 0.520] | 0.529 (49982) [0.525, 0.533] | 0.507 (67) | 0.500 | flat +0.005 (noise 0.007) |
| colour_path | 0.501 (20104) | 0.503 (139720) [0.501, 0.505] | 0.502 (600236) [0.500, 0.503] | 0.501 (1320634) [0.500, 0.502] | 0.501 (699748) [0.500, 0.502] | 0.528 (938) | 0.500 | flat +0.001 (noise 0.002) |
| colour_strong | 0.550 (20) | 0.611 (198) [0.580, 0.639] | 0.626 (1104) [0.608, 0.645] | 0.629 (1303) [0.611, 0.648] | 0.629 (1303) [0.611, 0.648] | 0.200 (5) | 0.500 | flat +0.015 (noise 0.043) |
| reversal_k13_next | 0.358 (53) | 0.371 (369) [0.342, 0.399] | 0.327 (1809) [0.313, 0.342] | 0.313 (4315) [0.303, 0.324] | 0.326 (2210) [0.314, 0.338] | 0.000 (2) | 0.077 | flat +0.054 (noise 0.034) |
| reversal_k13_now | 0.633 (49) | 0.585 (393) [0.547, 0.620] | 0.566 (1650) [0.547, 0.586] | 0.574 (3412) [0.561, 0.588] | 0.569 (1940) [0.550, 0.587] | 1.000 (1) | 0.077 | flat +0.010 (noise 0.035) |
| reversal_k3_next | 0.610 (41) | 0.612 (610) [0.585, 0.638] | 0.588 (2988) [0.577, 0.599] | 0.587 (5844) [0.578, 0.596] | 0.587 (3404) [0.576, 0.598] | 0.600 (5) | 0.293 | flat +0.021 (noise 0.027) |
| reversal_k3_now | 0.933 (60) | 0.915 (422) [0.905, 0.924] | 0.932 (1753) [0.922, 0.942] | 0.936 (3789) [0.930, 0.943] | 0.932 (2026) [0.923, 0.941] | 1.000 (2) | 0.294 | down -0.037 (noise 0.017) |
| reversal_k5_next | 0.528 (36) | 0.539 (395) [0.516, 0.559] | 0.483 (2715) [0.469, 0.499] | 0.484 (5156) [0.473, 0.495] | 0.478 (3166) [0.464, 0.492] | 0.400 (5) | 0.187 | flat +0.032 (noise 0.033) |
| reversal_k5_now | 0.862 (58) | 0.818 (407) [0.802, 0.834] | 0.819 (1636) [0.809, 0.828] | 0.829 (3523) [0.820, 0.838] | 0.821 (1912) [0.811, 0.831] | 0.667 (3) | 0.187 | flat -0.012 (noise 0.027) |
| reversal_k8_next | 0.438 (48) | 0.461 (414) [0.440, 0.480] | 0.395 (2692) [0.381, 0.409] | 0.395 (5218) [0.385, 0.406] | 0.395 (3112) [0.381, 0.407] | 0.000 (1) | 0.121 | up +0.067 (noise 0.031) |
| reversal_k8_now | 0.719 (57) | 0.704 (371) [0.676, 0.728] | 0.683 (1548) [0.663, 0.702] | 0.701 (3431) [0.688, 0.715] | 0.690 (1844) [0.672, 0.708] | 1.000 (1) | 0.121 | flat +0.007 (noise 0.034) |
| overall | 0.507 (22038) | 0.508 (153753) [0.506, 0.509] | 0.505 (662780) [0.504, 0.506] | 0.504 (1455983) [0.503, 0.505] | 0.505 (772702) [0.504, 0.506] | 0.529 (1029) | - | flat +0.002 (noise 0.002) |

- colour caller: a colour call is confident / strong when |P(up) - 0.5| is at least [0.07576, 0.1143] (about [144, 36] calls a day); over its last 7 days: {'every_minute': 0.5297, 'levels': [{'threshold': 0.07576, 'calls_per_day': 144.6, 'win_rate': 0.5773}, {'threshold': 0.1143, 'calls_per_day': 36.2, 'win_rate': 0.6211}]}
- cross-venue agent: OKX ETH-USDT-SWAP; its candle was there for 1.0 of the last 24 hours, the head that reads it made 1.0 of the predictions; colour right over 30 days with it: {'n': 42872, 'rate': 0.5289}, without it: None

## By market regime (last 30 days of the record)

| regime | candles | candle score | colour right | confident colour right | 'turn is in' hit rate |
|---|---|---|---|---|---|
| volatility: calm | 14903 | 0.343 | 0.527 (14677) | 0.576 (2202) | 0.743 (2520) |
| volatility: normal | 14902 | 0.368 | 0.533 (14835) | 0.610 (1391) | 0.753 (2205) |
| volatility: wild | 14903 | 0.384 | 0.525 (14863) | 0.620 (790) | 0.766 (2066) |
| session: Asia 00-08 | 14948 | 0.365 | 0.534 (14849) | 0.600 (1529) | 0.761 (2212) |
| session: Europe 08-13 | 9300 | 0.360 | 0.536 (9208) | 0.597 (1151) | 0.747 (1510) |
| session: US 13-21 | 14880 | 0.372 | 0.524 (14785) | 0.596 (1130) | 0.753 (2265) |
| session: late 21-24 | 5580 | 0.354 | 0.512 (5533) | 0.574 (573) | 0.744 (804) |

## The goal: generated candle vs real candle

score = 0.5 x body overlap + 0.5 x range overlap (1.0 = identical candle). `site` is the live generator the site draws, `full` is the complete cloud model, `repeat` and `typical` are naive baselines.

| window | n | site score | full score | repeat | typical | site colour right | site body IoU | site range IoU | body size ratio |
|---|---|---|---|---|---|---|---|---|---|
| 1h | 60 | 0.328 | 0.335 | 0.223 | 0.223 | 0.492 | 0.255 | 0.402 | 1.347 |
| 6h | 360 | 0.370 | 0.366 | 0.297 | 0.313 | 0.517 | 0.263 | 0.476 | 1.398 |
| 24h | 1440 | 0.395 | 0.384 | 0.295 | 0.324 | 0.553 | 0.282 | 0.508 | 1.317 |
| 7d | 10080 | 0.363 | 0.359 | 0.275 | 0.305 | 0.531 | 0.261 | 0.466 | 1.273 |
| 30d | 43200 | 0.365 | 0.358 | 0.277 | 0.308 | 0.529 | 0.263 | 0.468 | 1.243 |

## Every candle of the 15-candle chain, judged from its own open (score / colour right / 90% range held the close)

- 1h: 1: 0.328 / 0.492 / 0.883; 2: 0.350 / 0.593 / 0.900; 3: 0.340 / 0.559 / 0.850; 4: 0.372 / 0.627 / 0.833; 5: 0.350 / 0.593 / 0.850; 6: 0.346 / 0.475 / 0.983; 7: 0.320 / 0.390 / 0.983; 8: 0.315 / 0.441 / 0.883; 9: 0.360 / 0.542 / 0.967; 10: 0.358 / 0.593 / 0.950; 11: 0.337 / 0.559 / 0.967; 12: 0.352 / 0.542 / 1.000; 13: 0.306 / 0.458 / 0.783; 14: 0.353 / 0.559 / 1.000; 15: 0.322 / 0.492 / 0.750
- 6h: 1: 0.370 / 0.517 / 0.903; 2: 0.369 / 0.525 / 0.883; 3: 0.367 / 0.520 / 0.864; 4: 0.372 / 0.522 / 0.867; 5: 0.368 / 0.534 / 0.861; 6: 0.367 / 0.520 / 0.947; 7: 0.357 / 0.478 / 0.867; 8: 0.350 / 0.475 / 0.911; 9: 0.365 / 0.486 / 0.842; 10: 0.365 / 0.506 / 0.853; 11: 0.359 / 0.522 / 0.839; 12: 0.366 / 0.486 / 0.850; 13: 0.354 / 0.472 / 0.853; 14: 0.369 / 0.525 / 0.839; 15: 0.355 / 0.486 / 0.839
- 24h: 1: 0.395 / 0.553 / 0.905; 2: 0.373 / 0.475 / 0.902; 3: 0.382 / 0.519 / 0.900; 4: 0.373 / 0.488 / 0.896; 5: 0.381 / 0.521 / 0.894; 6: 0.376 / 0.511 / 0.905; 7: 0.372 / 0.493 / 0.892; 8: 0.367 / 0.477 / 0.908; 9: 0.374 / 0.494 / 0.884; 10: 0.379 / 0.520 / 0.883; 11: 0.376 / 0.522 / 0.884; 12: 0.371 / 0.489 / 0.893; 13: 0.372 / 0.492 / 0.894; 14: 0.374 / 0.509 / 0.887; 15: 0.372 / 0.501 / 0.891
- 7d: 1: 0.363 / 0.531 / 0.896; 2: 0.352 / 0.494 / 0.900; 3: 0.355 / 0.513 / 0.900; 4: 0.352 / 0.501 / 0.900; 5: 0.353 / 0.511 / 0.900; 6: 0.350 / 0.508 / 0.900; 7: 0.350 / 0.499 / 0.900; 8: 0.348 / 0.504 / 0.900; 9: 0.352 / 0.510 / 0.899; 10: 0.347 / 0.495 / 0.900; 11: 0.348 / 0.503 / 0.899; 12: 0.348 / 0.502 / 0.899; 13: 0.349 / 0.501 / 0.899; 14: 0.347 / 0.499 / 0.898; 15: 0.350 / 0.510 / 0.898
- 30d: 1: 0.365 / 0.529 / 0.898; 2: 0.353 / 0.495 / 0.900; 3: 0.356 / 0.510 / 0.900; 4: 0.352 / 0.498 / 0.900; 5: 0.353 / 0.505 / 0.900; 6: 0.351 / 0.502 / 0.900; 7: 0.351 / 0.499 / 0.900; 8: 0.351 / 0.504 / 0.900; 9: 0.351 / 0.501 / 0.900; 10: 0.351 / 0.504 / 0.900; 11: 0.348 / 0.498 / 0.900; 12: 0.350 / 0.503 / 0.900; 13: 0.349 / 0.500 / 0.900; 14: 0.349 / 0.501 / 0.900; 15: 0.349 / 0.503 / 0.900

## The fixed record: the chain frozen at the start of every 15 minutes, compared at its real price level

- 1h: match 0.192 (body 0.172, range 0.212); 'price stays where it was' would score 0.192; colour right 0.610; typical miss of the close 3.2 bp; chain ended on the right side - of 0 chains; n=60
- 6h: match 0.160 (body 0.116, range 0.205); 'price stays where it was' would score 0.188; colour right 0.489; typical miss of the close 6.0 bp; chain ended on the right side 0.542 of 24 chains; n=360
- 24h: match 0.139 (body 0.094, range 0.184); 'price stays where it was' would score 0.151; colour right 0.514; typical miss of the close 10.3 bp; chain ended on the right side 0.510 of 96 chains; n=1440
- 7d: match 0.122 (body 0.084, range 0.161); 'price stays where it was' would score 0.125; colour right 0.502; typical miss of the close 8.7 bp; chain ended on the right side 0.485 of 672 chains; n=10080
- 30d: match 0.126 (body 0.086, range 0.165); 'price stays where it was' would score 0.130; colour right 0.501; typical miss of the close 8.6 bp; chain ended on the right side 0.515 of 2879 chains; n=43200
- by candle of the chain (match / typical miss of the close in bp): 1: 0.370 / 4.5; 2: 0.201 / 5.2; 3: 0.168 / 6.9; 4: 0.132 / 7.1; 5: 0.126 / 7.8; 6: 0.116 / 8.7; 7: 0.113 / 8.9; 8: 0.100 / 9.9; 9: 0.092 / 9.8; 10: 0.091 / 10.3; 11: 0.087 / 10.4; 12: 0.080 / 10.8; 13: 0.073 / 11.2; 14: 0.072 / 11.7; 15: 0.065 / 11.9

## Reversal agents

- a swing point of size K = highest high / lowest low of K candles on each side
- `now`: the turn is in (a swing point at the candle that just closed, give or take one); `next`: a turn is coming (a swing point in one of the next three candles). A call is a hit if that happens.
- an agent picks its own confidence threshold: the best hit rate of its last 7 days among thresholds that keep 48 calls a day
- **K=3**: model 1791504000, labels learned 138062, probability skill vs chance 0.2268, widened contest next: False
  - now: threshold 0.8386, hit rate recent 0.9349 / long run 0.93
    - 6h: 12 calls (49 a day), hit rate 1.000, chance 0.287, naive rule 0.467, lift 3.48x
    - 24h: 56 calls (56 a day), hit rate 0.946, chance 0.316, naive rule 0.524, lift 3.00x
    - 7d: 418 calls (60 a day), hit rate 0.916, chance 0.296, naive rule 0.499, lift 3.09x
    - 30d: 1750 calls (58 a day), hit rate 0.932, chance 0.294, naive rule 0.495, lift 3.17x
  - next: threshold 0.566, hit rate recent 0.6238 / long run 0.6064
    - 6h: 9 calls (37 a day), hit rate 0.556, chance 0.287, lift 1.93x
    - 24h: 39 calls (39 a day), hit rate 0.590, chance 0.316, lift 1.87x
    - 7d: 608 calls (87 a day), hit rate 0.612, chance 0.296, lift 2.07x
    - 30d: 2987 calls (100 a day), hit rate 0.588, chance 0.294, lift 2.00x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 565, 0.499; 0.35: 533, 0.524; 0.40: 474, 0.580; 0.45: 406, 0.650; 0.50: 356, 0.701; 0.55: 309, 0.744; 0.60: 261, 0.789; 0.65: 220, 0.814; 0.70: 173, 0.845; 0.75: 139, 0.876; 0.80: 93, 0.908; 0.85: 47, 0.946; 0.90: 4, 0.985
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 588, 0.431; 0.35: 498, 0.465; 0.40: 402, 0.501; 0.45: 304, 0.536; 0.50: 196, 0.570; 0.55: 89, 0.578; 0.60: 12, 0.642; 0.65: 1, 0.591
- **K=5**: model 1792540800, labels learned 138060, probability skill vs chance 0.215, widened contest next: False
  - now: threshold 0.6882, hit rate recent 0.8349 / long run 0.8219
    - 6h: 14 calls (57 a day), hit rate 0.857, chance 0.188, naive rule 0.386, lift 4.55x
    - 24h: 56 calls (56 a day), hit rate 0.839, chance 0.194, naive rule 0.424, lift 4.32x
    - 7d: 405 calls (58 a day), hit rate 0.820, chance 0.188, naive rule 0.412, lift 4.35x
    - 30d: 1635 calls (55 a day), hit rate 0.818, chance 0.187, naive rule 0.407, lift 4.37x
  - next: threshold 0.4547, hit rate recent 0.5225 / long run 0.5149
    - 6h: 7 calls (29 a day), hit rate 0.286, chance 0.188, lift 1.52x
    - 24h: 34 calls (34 a day), hit rate 0.529, chance 0.194, lift 2.72x
    - 7d: 394 calls (56 a day), hit rate 0.538, chance 0.188, lift 2.86x
    - 30d: 2714 calls (90 a day), hit rate 0.483, chance 0.187, lift 2.58x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 419, 0.424; 0.35: 349, 0.489; 0.40: 282, 0.562; 0.45: 231, 0.613; 0.50: 185, 0.663; 0.55: 148, 0.700; 0.60: 112, 0.747; 0.65: 77, 0.787; 0.70: 48, 0.822; 0.75: 29, 0.858; 0.80: 10, 0.875
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 348, 0.386; 0.35: 256, 0.423; 0.40: 160, 0.463; 0.45: 67, 0.487; 0.50: 11, 0.506; 0.55: 1, 0.432
- **K=8**: model 1793059200, labels learned 138057, probability skill vs chance 0.2074, widened contest next: False
  - now: threshold 0.5711, hit rate recent 0.7129 / long run 0.6951
    - 6h: 11 calls (45 a day), hit rate 0.727, chance 0.110, naive rule 0.288, lift 6.61x
    - 24h: 55 calls (55 a day), hit rate 0.709, chance 0.121, naive rule 0.338, lift 5.86x
    - 7d: 367 calls (52 a day), hit rate 0.706, chance 0.122, naive rule 0.343, lift 5.78x
    - 30d: 1547 calls (52 a day), hit rate 0.683, chance 0.121, naive rule 0.336, lift 5.66x
  - next: threshold 0.3586, hit rate recent 0.433 / long run 0.4245
    - 6h: 5 calls (21 a day), hit rate 0.200, chance 0.110, lift 1.82x
    - 24h: 47 calls (47 a day), hit rate 0.426, chance 0.121, lift 3.52x
    - 7d: 410 calls (59 a day), hit rate 0.461, chance 0.122, lift 3.78x
    - 30d: 2687 calls (90 a day), hit rate 0.395, chance 0.121, lift 3.27x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 246, 0.432; 0.35: 192, 0.495; 0.40: 152, 0.541; 0.45: 117, 0.589; 0.50: 85, 0.639; 0.55: 60, 0.673; 0.60: 40, 0.708; 0.65: 25, 0.781; 0.70: 12, 0.806; 0.75: 2, 0.768
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 173, 0.362; 0.35: 89, 0.391; 0.40: 25, 0.419; 0.45: 5, 0.445; 0.50: 1, 0.692
- **K=13**: model 1793577600, labels learned 138052, probability skill vs chance 0.1868, widened contest next: False
  - now: threshold 0.455, hit rate recent 0.6102 / long run 0.5741
    - 6h: 13 calls (54 a day), hit rate 0.692, chance 0.078, naive rule 0.237, lift 8.85x
    - 24h: 47 calls (47 a day), hit rate 0.638, chance 0.084, naive rule 0.308, lift 7.64x
    - 7d: 389 calls (56 a day), hit rate 0.586, chance 0.080, naive rule 0.292, lift 7.30x
    - 30d: 1649 calls (55 a day), hit rate 0.566, chance 0.078, naive rule 0.282, lift 7.29x
  - next: threshold 0.2855, hit rate recent 0.3281 / long run 0.3359
    - 6h: 9 calls (38 a day), hit rate 0.111, chance 0.078, lift 1.42x
    - 24h: 51 calls (52 a day), hit rate 0.333, chance 0.084, lift 3.99x
    - 7d: 368 calls (53 a day), hit rate 0.370, chance 0.080, lift 4.60x
    - 30d: 1806 calls (60 a day), hit rate 0.327, chance 0.078, lift 4.21x
  - now, what each threshold would give (threshold: calls a day, hit rate): 0.30: 131, 0.438; 0.35: 94, 0.488; 0.40: 66, 0.546; 0.45: 45, 0.591; 0.50: 30, 0.648; 0.55: 20, 0.677; 0.60: 11, 0.715; 0.65: 3, 0.687; 0.70: 0, 0.375
  - next, what each threshold would give (threshold: calls a day, hit rate): 0.30: 50, 0.330; 0.35: 13, 0.347; 0.40: 3, 0.415; 0.45: 0, 0.444

## Probability quality (full model)

| window | pinball x1e5 | skill vs empirical | cov 90% | cov 50% | Brier | dir acc | vol corr |
|---|---|---|---|---|---|---|---|
| 1h | 6.903 | 23.71% | 0.933 | 0.533 | 0.252 | 0.475 | 0.099 |
| 6h | 10.461 | 12.46% | 0.919 | 0.503 | 0.251 | 0.478 | 0.516 |
| 24h | 18.023 | 4.91% | 0.912 | 0.504 | 0.250 | 0.502 | 0.657 |
| 7d | 15.222 | 5.13% | 0.900 | 0.501 | 0.250 | 0.506 | 0.744 |
| 30d | 15.324 | 4.43% | 0.900 | 0.500 | 0.250 | 0.499 | 0.706 |

## Per-agent pinball loss x1e5

| window | empirical | ewma | garch | har | bocpd | hmm | online_qr | lgbm | ensemble | calibrated |
|---|---|---|---|---|---|---|---|---|---|---|
| 1h | 9.048 | 6.885 | 7.120 | 6.958 | 7.080 | 7.510 | 6.889 | 6.915 | 6.919 | 6.903 |
| 6h | 11.950 | 10.620 | 10.634 | 10.583 | 10.640 | 10.576 | 10.451 | 10.405 | 10.446 | 10.461 |
| 24h | 18.954 | 18.147 | 18.143 | 18.088 | 18.403 | 18.299 | 17.944 | 17.971 | 17.979 | 18.023 |
| 7d | 16.045 | 15.347 | 15.331 | 15.273 | 15.507 | 15.562 | 15.204 | 15.199 | 15.195 | 15.222 |
| 30d | 16.035 | 15.480 | 15.421 | 15.353 | 15.606 | 15.561 | 15.314 | 15.294 | 15.296 | 15.324 |

## Next candle

- candle starting 2026-11-07 01:08 UTC, last close 2239.47
- P(up) 0.492, return quantiles (bp): {'05': -4.623, '10': -3.494, '25': -1.796, '40': -0.691, '50': -0.045, '60': 0.544, '75': 1.868, '90': 3.567, '95': 5.019}
- changepoint probability 0.0299, regime age 170.3 min
- agent weights: empirical 0.003, ewma 0.089, garch 0.088, har 0.125, bocpd 0.035, hmm 0.046, online_qr 0.315, lgbm 0.299

## Learning log

- 2026-11-05 00:00 UTC: {"garch": {"alpha": 0.0904, "beta": 0.8932}, "hmm": {"sd_bp": [2.25, 4.78, 12.71], "stay": [0.97, 0.97, 0.931]}, "lgbm": {"challenger_loss": 0.25476, "champion_loss": 0.25479, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47805, "challengers": 1, "chance_loss": 0.60092, "widened": false, "champion_loss": 0.47636, "promoted": false}, "reversal_k5": {"challenger_loss": 0.36469, "challengers": 1, "chance_loss": 0.47256, "widened": false, "champion_loss": 0.36302, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26527, "challengers": 1, "chance_loss": 0.35726, "widened": false, "champion_loss": 0.26314, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20069, "challengers": 1, "chance_loss": 0.27954, "widened": false, "champion_loss": 0.19974, "promoted": false}}
- 2026-11-05 12:00 UTC: {"garch": {"alpha": 0.0844, "beta": 0.8924}, "hmm": {"sd_bp": [2.39, 4.93, 13.06], "stay": [0.951, 0.972, 0.93]}}
- 2026-11-06 00:00 UTC: {"garch": {"alpha": 0.0899, "beta": 0.894}, "hmm": {"sd_bp": [2.92, 5.43, 14.8], "stay": [0.927, 0.965, 0.939]}, "lgbm": {"challenger_loss": 0.25805, "champion_loss": 0.25821, "promoted": true}, "reversal_k3": {"challenger_loss": 0.47625, "challengers": 1, "chance_loss": 0.60251, "widened": false, "champion_loss": 0.47346, "promoted": false}, "reversal_k5": {"challenger_loss": 0.37044, "challengers": 1, "chance_loss": 0.47902, "widened": false, "champion_loss": 0.36878, "promoted": false}, "reversal_k8": {"challenger_loss": 0.26912, "challengers": 1, "chance_loss": 0.36652, "widened": false, "champion_loss": 0.267, "promoted": false}, "reversal_k13": {"challenger_loss": 0.19613, "challengers": 1, "chance_loss": 0.26901, "widened": false, "champion_loss": 0.19539, "promoted": false}}
- 2026-11-06 12:00 UTC: {"garch": {"alpha": 0.0792, "beta": 0.9086}, "hmm": {"sd_bp": [3.63, 6.36, 16.62], "stay": [0.949, 0.957, 0.924]}}
- 2026-11-07 00:00 UTC: {"garch": {"alpha": 0.0829, "beta": 0.9061}, "hmm": {"sd_bp": [4.22, 7.18, 18.37], "stay": [0.984, 0.963, 0.924]}, "lgbm": {"challenger_loss": 0.25477, "champion_loss": 0.25461, "promoted": false}, "reversal_k3": {"challenger_loss": 0.48968, "challengers": 1, "chance_loss": 0.61415, "widened": false, "champion_loss": 0.48862, "promoted": false}, "reversal_k5": {"challenger_loss": 0.38056, "challengers": 1, "chance_loss": 0.4869, "widened": false, "champion_loss": 0.37882, "promoted": false}, "reversal_k8": {"challenger_loss": 0.27281, "challengers": 1, "chance_loss": 0.36927, "widened": false, "champion_loss": 0.27272, "promoted": false}, "reversal_k13": {"challenger_loss": 0.20245, "challengers": 1, "chance_loss": 0.27868, "widened": false, "champion_loss": 0.20219, "promoted": false}}
- HMM volatility states (sd, bp per minute): [4.22, 7.18, 18.37], current probabilities: [0.964, 0.036, 0.001]
- live generator: {'versions': 60, 'latest_effective': '2026-11-07 01:20 UTC', 'rows': 2880, 'fit_r2': {'logit_p': 0.209, 'l_abs': 0.722, 'l_hi': 0.755, 'l_lo': 0.744, 'b05': 0.738, 'b25': 0.721, 'b75': 0.579, 'b95': 0.698}}
- goal tuner (multipliers that currently maximise the candle score): {'body_scale': 1.2, 'reach_scale': 1.5, 'ahead': [[1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.3, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8], [1.4, 1.8]], 'cone_width': [1.409, 1.729, 2.082, 2.476, 2.411, 2.609, 2.685, 3.416, 3.681, 3.947, 3.738, 4.057, 4.853, 4.74]}
- calibration offsets (in sigma): {'05': 0.1135, '10': 0.077, '25': 0.0375, '40': 0.018, '50': 0.005, '60': -0.018, '75': 0.0125, '90': -0.077, '95': -0.0435}
