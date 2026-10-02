"""All tunable constants in one place. Windows are in CANDLES (1 candle = GRAN seconds)."""
import os

PRODUCT = os.environ.get("PRODUCT", "ETH-USD")
GRAN = 60                      # candle length in seconds (1 minute)
START = "2026-08-01"           # first candle ever downloaded
REPLAY_DAYS = 60               # history replayed when the engine has to be rebuilt

# volatility / feature windows
W_SHORT, W_MID, W_LONG = 10, 60, 360
BUF = 1000                     # tail length that is always enough for every feature

# learning cadence
RETRAIN_EVERY = 720            # GARCH / HMM refit (12 hours)
LGBM_EVERY = 1440              # tree challenger (daily)
TRAIN_WINDOW = 43200           # 30 days of rows for the tree models
LGBM_HOLDOUT = 2880            # challenger is judged on the latest 2 unseen days
LGBM_EMBARGO = 60

# live generator (student) schedule
HORIZON = 5                    # candles generated ahead at every minute
STUDENT_ROWS = 2880            # distilled on the latest 2 days of teacher output
STUDENT_ROWS_H = 10080         # candles 2..HORIZON learn from one week of real outcomes
STUDENT_STEP = 300             # a new version can become effective every 5 minutes
STUDENT_LEAD = 420             # ... and never sooner than 7 minutes after it was fitted
STUDENT_WIN = 240              # candles the live generator looks back on
