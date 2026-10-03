"""The colour caller: which of the model's colour predictions does it stand behind?

The colour of the next candle is close to a coin flip most minutes, and the
model knows it: its direction head gives a probability near one half. A few
times an hour it is further from one half - those are the minutes it has
something to say. This agent draws two lines.

    confidence = |P(up) - 0.5|      of the direction head of candle 1
    level 1  CONFIDENT  confidence >= ct[0]   about COL_PER_DAY[0] calls a day
    level 2  STRONG     confidence >= ct[1]   about COL_PER_DAY[1] calls a day
    level 0             the candle is still drawn, but no colour call is claimed

WHY THE LINES ARE WHERE THEY ARE. Measured walking forward through two months
(EXPERIMENTS.md, E09): the win rate rises steadily with confidence - every
minute 51.0%, the 144 most confident a day 52.6%, the 36 most confident 54.9% -
and it did so in both halves of the period. Picking the line by its recent
win rate instead was tried and was worse (51.5%): one week of calls is too
few to tell neighbouring lines apart, so that rule chases noise. So the rule
is the plain one: each line is the confidence that produced its number of
calls a day over the last seven days. The lever that raises these win rates
is a better direction head (new information), not a cleverer line.

GOAL. The win rates of the calls (ledger layers `colour_confident`,
`colour_strong`). Every six hours the agent re-draws the lines and measures
whether confidence still pays: the win rate of its calls against the win rate
of calling every minute. If it does not, the goal keeper says so.

The lines are published with the model parameters, so the site makes the
same decision at the same minute, and the decision is stored with the
generated candle (`g_call`) before the candle exists.
"""
from collections import deque

from ..config import COL_PER_DAY, COL_TUNE_WIN


class ColourCaller:
    name = "colour_caller"

    def __init__(self):
        self.hist = deque(maxlen=COL_TUNE_WIN)     # (ts, confidence, colour was right) of every judged candle
        self.thr = None                            # no calls until the lines are drawn for the first time
        self.tuned = None

    def observe(self, ts, conf, win):
        self.hist.append((int(ts), float(conf), bool(win)))

    def tune(self):
        if len(self.hist) < 2880:
            return None
        days = (self.hist[-1][0] - self.hist[0][0]) / 86400.0
        if days < 2.0:
            return None
        rows = sorted(((c, w) for _, c, w in self.hist), reverse=True)      # most confident first
        new, info = [], {"every_minute": round(sum(w for _, w in rows) / len(rows), 4), "levels": []}
        for a, per_day in enumerate(COL_PER_DAY):
            n = max(min(int(round(per_day * days)), len(rows)), 1)
            line = rows[n - 1][0]
            if self.thr is not None:                # move half way: the lines should not jump
                line = 0.5 * self.thr[a] + 0.5 * line
            new.append(float(f"{line:.4g}"))
        new = [new[0]] + [max(t, new[0]) for t in new[1:]]                   # a stronger call is also a confident one
        for a, t in enumerate(new):
            n = sum(1 for c, _ in rows if c >= t)
            wins = sum(w for c, w in rows if c >= t)
            info["levels"].append({"threshold": t, "calls_per_day": round(n / days, 1),
                                   "win_rate": round(wins / n, 4) if n else None})
        self.thr, self.tuned = new, info
        return info

    def summary(self):
        return {"threshold": self.thr, "tuned": self.tuned, "judged": len(self.hist)}
