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
HORIZON = 15                   # candles generated ahead at every minute (see GOAL.md for why 15)
STUDENT_ROWS = 2880            # distilled on the latest 2 days of teacher output
STUDENT_ROWS_H = 10080         # the per-candle heads learn from one week of real outcomes
STUDENT_STEP = 300             # a new version can become effective every 5 minutes
STUDENT_LEAD = 420             # ... and never sooner than 7 minutes after it was fitted
STUDENT_WIN = 240              # candles the live generator looks back on

# reversal agents (one per swing size)
REV_KS = (3, 5, 8, 13)         # a swing point is the highest high / lowest low of the K candles on each side
REV_K = 5                      # the swing size the site shows first
REV_HS = (0, 2)                # call types: 0 = "the turn is in" (the candle that just closed, +-1),
                               #             2 = "a turn is coming" (one of the next three candles)
REV_TRAIN = 28800              # origins (20 days) the tree model of a reversal agent trains on
REV_MIN_PER_DAY = 48           # an agent must keep making at least this many calls a day, per call type
REV_TUNE_EVERY = 360           # it re-picks its confidence thresholds every 6 hours ...
REV_TUNE_WIN = 10080           # ... from its own last 7 days

# colour caller (see agents/colour.py)
COL_PER_DAY = (144, 36)        # colour calls a day: "confident" (one minute in ten) and "strong" (one in forty)
COL_TUNE_WIN = 10080           # the lines are re-drawn from its last 7 days of judged candles
CLEAR_K = 0.5                  # a "clear" candle moved more than this many typical moves (ledger layer colour_clear)
