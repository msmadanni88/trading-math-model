"""Reversal agent: where will the next turning points be?

DEFINITION. Candle s is a swing high of order K if its high is the highest of
the K candles before it and the K candles after it (swing low: mirrored).
The agent estimates, after every candle t and for every j = 0..H,

    p_top[j]    = P(a swing high forms within one candle of candle t+j | known at t)
    p_bottom[j] = P(a swing low  forms within one candle of candle t+j | known at t)

j = 0 is the candle that has just closed ("the turn is in": it cannot be
confirmed for another K candles); j >= 1 are candles that have not started.
This is exactly the event a call is judged on, so the models are trained on
the goal itself. A bottom is a top of the mirrored price, so both sides share
one model and every candle gives two training examples.

MODELS (the "teacher"), each learning from every resolved swing label:
  base    running frequency per horizon (what chance alone gives)
  logit   online logistic regression, one Adagrad step per label
  trees   LightGBM classifier on a rolling 10-day window, daily
          champion / challenger on unseen log-loss
They are mixed by Hedge on log-loss, so whichever has been predicting swing
points better lately gets the weight.

GOAL. The agent may "call" a swing point on about REV_BUDGET of the minutes
(a threshold that tracks that budget online). A call names a side and a
minute; it is a hit if a swing point of that side forms within one candle of
that minute. The goal is the hit rate of the calls, judged against the chance
level - how often a swing point sits there anyway. Every call is stored when
it is made and never edited; only its outcome is filled in later.

A label is only known K + 1 candles after its candle, so all learning here is
delayed by up to K + H + 1 candles; nothing ever uses a candle that has not closed.
"""
import numpy as np

from ..config import LGBM_EMBARGO, LGBM_HOLDOUT, REV_BUDGET, REV_H, REV_K, REV_TRAIN
from ..student import REV_FEATURES

D = len(REV_FEATURES)
LGB_PARAMS = dict(objective="binary", learning_rate=0.05, num_leaves=12, min_data_in_leaf=300,
                  feature_fraction=0.8, bagging_fraction=0.7, bagging_freq=1, lambda_l2=5.0,
                  verbose=-1, seed=11, deterministic=True, force_col_wise=True, num_threads=2)
LGB_ROUNDS = 80
EXPERTS = ("base", "logit", "trees")
NH = REV_H + 1                     # horizons 0..H


def _sig(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))


def _logloss(p, y):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


class _Ring:
    """Fixed-length history of arrays, newest last."""

    def __init__(self, n, shape, fill=np.nan):
        self.a = np.full((n,) + tuple(shape), fill, dtype=float)

    def push(self, v):
        self.a[:-1] = self.a[1:]
        self.a[-1] = v

    def back(self, k):
        """k = 0 is the newest entry."""
        return self.a[-1 - k]


class ReversalAgent:
    name = "reversal"
    role = "reversal"

    def __init__(self):
        n = 4 * (REV_K + REV_H)
        self.hl = _Ring(n, (2,))                    # high, low of the latest candles
        self.phi = _Ring(n, (2, D))                 # features, [top, bottom]
        self.pred = _Ring(n, (len(EXPERTS) + 1, 2, NH))      # what each expert (+ the mix) said
        self.lab = _Ring(n, (2,))                   # is candle t-K a swing point [top, bottom]
        self.lab3 = _Ring(n, (2,))                  # ... is there one within a candle of candle t-K-1
        self.n = 0
        # online logistic regression (one weight vector per horizon)
        self.W = np.zeros((NH, D))
        self.G = np.full((NH, D), 1e-2)
        self.n_fit = 0
        self.base = np.full(NH, 0.2)
        self.L = np.zeros(len(EXPERTS))             # discounted log-loss per expert (Hedge)
        self.scale = 0.3
        # rolling training set of the tree model
        self.tX = np.zeros((2 * 2 * REV_TRAIN, D), dtype=np.float32)
        self.tY = np.zeros((2 * 2 * REV_TRAIN, NH), dtype=np.float32)
        self.tn = 0
        self.model, self._boost = None, None
        # running quality (exponentially weighted): Brier of the mix and of chance
        self.brier = np.zeros(2)
        self.thr = 0.35                             # call threshold (tracks the budget)
        self.calls = {}                             # (for_ts, side) -> call awaiting its outcome
        self.recent = {}                            # (for_ts, side) -> True, for de-duplication
        self.events = []                            # new calls / outcomes since the last drain
        self.hit_rate, self.base_rate, self.n_calls = 0.0, 0.0, 0

    def __getstate__(self):
        s = dict(self.__dict__)
        s["_boost"] = None
        return s

    # ------------------------------------------------------------------ models
    def _booster(self):
        if self._boost is None and self.model is not None:
            import lightgbm as lgb
            self._boost = lgb.Booster(model_str=self.model)
        return self._boost

    @staticmethod
    def _stack(X):
        """(n, D) -> (n * H, D + 1): one row per horizon, horizon as a feature."""
        n = len(X)
        j = np.tile(np.arange(NH, dtype=np.float32), n)[:, None]
        return np.hstack([np.repeat(X, NH, axis=0), j])

    def _weights(self):
        ready = np.array([True, self.n_fit >= 2000, self.model is not None])
        w = np.exp(-0.5 * (self.L - self.L[ready].min())) * ready
        w = w / w.sum()
        return 0.97 * w + 0.03 * ready / ready.sum()

    def predict(self, phi_top, phi_bottom):
        """Teacher probabilities, shape (2, H + 1): [top, bottom] x horizon 0..H."""
        X = np.vstack([phi_top, phi_bottom])
        P = np.empty((len(EXPERTS) + 1, 2, NH))
        P[0] = self.base[None, :]
        P[1] = _sig(X @ self.W.T) if self.n_fit >= 2000 else P[0]
        b = self._booster()
        P[2] = b.predict(self._stack(X.astype(np.float32))).reshape(2, NH) if b is not None else P[0]
        w = self._weights()
        P[3] = np.tensordot(w, P[:3], axes=1)
        self.pred.a[-1] = P
        return P[3]

    def ready(self):
        return self.n_fit >= 2000

    def retrain(self, hist=None):
        """Daily: train a challenger tree model; keep it only if it beats the
        champion on the latest two days, which it never saw."""
        import lightgbm as lgb
        n = min(self.tn, 2 * REV_TRAIN)
        hold = 2 * LGBM_HOLDOUT
        if n < 3 * hold:
            return None
        X, Y = self.tX[self.tn - n:self.tn], self.tY[self.tn - n:self.tn]
        cut = n - hold
        Xtr, ytr = self._stack(X[:cut - 2 * LGBM_EMBARGO]), Y[:cut - 2 * LGBM_EMBARGO].ravel()
        Xho, yho = self._stack(X[cut:]), Y[cut:].ravel()
        cand = lgb.train(LGB_PARAMS, lgb.Dataset(Xtr, label=ytr, free_raw_data=False), num_boost_round=LGB_ROUNDS)
        l_c = float(_logloss(cand.predict(Xho), yho).mean())
        info = {"challenger_loss": round(l_c, 5), "chance_loss": round(float(_logloss(ytr.mean(), yho).mean()), 5)}
        cur = self._booster()
        if cur is not None:
            l_o = float(_logloss(cur.predict(Xho), yho).mean())
            info["champion_loss"] = round(l_o, 5)
            info["promoted"] = bool(l_c < l_o)
            if not info["promoted"]:
                return info
        else:
            info["promoted"] = True
        self.model, self._boost = cand.model_to_string(), cand
        return info

    # ------------------------------------------------------------------ one candle
    def observe(self, high, low, phi_top, phi_bottom):
        """Called once per closed candle, BEFORE predict() for that candle.
        Resolves the swing label that just became known and learns from it."""
        self.hl.push([high, low])
        self.phi.push(np.vstack([phi_top, phi_bottom]) if phi_top is not None else np.nan)
        self.pred.push(np.nan)                         # filled in by predict() for this candle
        self.n += 1
        if self.n < 2 * REV_K + 1:
            self.lab.push(np.nan)
            self.lab3.push(np.nan)
            return None
        w = self.hl.a[-(2 * REV_K + 1):]
        s = w[REV_K]                                   # candle t-K: now K candles on each side are known
        y = np.array([float(s[0] >= w[:, 0].max()), float(s[1] <= w[:, 1].min())])
        self.lab.push(y)
        self.lab3.push(self.lab.a[-3:].max(0))         # centre t-K-1: a swing among t-K-2, t-K-1, t-K
        # the row whose labels are all known now: forecast origin o = t - K - 1 - H
        Y = self.lab3.a[-NH:].T                        # (2 sides, H + 1)  centres o .. o+H
        o = REV_K + 1 + REV_H
        X, P = self.phi.back(o), self.pred.back(o)
        if not (np.all(np.isfinite(Y)) and np.all(np.isfinite(X))):
            return y
        if np.all(np.isfinite(P)):                     # score what each expert said for this row
            loss = np.array([_logloss(P[e], Y).mean() for e in range(len(EXPERTS))])
            self.scale += 0.001 * (loss[0] - self.scale)           # typical loss of chance
            self.L = 0.999 * self.L + loss / self.scale
            k = 0.0005
            self.brier += k * (np.array([((P[3] - Y) ** 2).mean(), ((self.base[None, :] - Y) ** 2).mean()]) - self.brier)
        for side in (0, 1):                            # online logistic regression step
            g = (_sig(X[side] @ self.W.T) - Y[side])[:, None] * X[side][None, :] + 1e-4 * self.W
            self.G += g * g
            self.W -= 0.05 * g / np.sqrt(self.G)
        self.n_fit += 1
        self.base += 0.0005 * (Y.mean(0) - self.base)
        if self.tn + 2 > len(self.tX):                 # rolling training set of the tree model
            keep = 2 * REV_TRAIN
            self.tX[:keep], self.tY[:keep] = self.tX[self.tn - keep:self.tn], self.tY[self.tn - keep:self.tn]
            self.tn = keep
        self.tX[self.tn:self.tn + 2], self.tY[self.tn:self.tn + 2] = X, Y
        self.tn += 2
        return y

    # ------------------------------------------------------------------ calls
    def call(self, ts, gran, probs, thr, eff):
        """ts: the candle that just closed. probs: official (published)
        probabilities (2, H + 1) for the candles ts, ts + gran, ...
        Issues at most one call per side."""
        out = []
        for side, sgn in ((0, 1), (1, -1)):
            j = int(np.argmax(probs[side]))
            p = float(probs[side][j])
            self.thr += 0.002 * ((p >= self.thr) - REV_BUDGET)      # threshold tracks the call budget
            self.thr = float(min(max(self.thr, 0.12), 0.95))
            if p < thr:
                continue
            for_ts = int(ts + j * gran)
            if any((for_ts + d * gran, sgn) in self.recent for d in (-2, -1, 0, 1, 2)):
                continue                                           # that turning point is already called
            known = self.hl.a[-(REV_K - j + 1):, side]              # candles of its window that have closed
            level = float(known.max() if sgn > 0 else known.min())
            c = {"made_ts": int(ts + gran), "for_ts": for_ts, "side": sgn, "p": round(p, 4),
                 "level": round(level, 2), "eff": int(eff)}
            self.calls[(for_ts, sgn)] = c
            self.recent[(for_ts, sgn)] = True
            self.events.append(("new", c))
            out.append(c)
        return out

    def settle(self, ts, gran):
        """ts: the candle that just closed. The call for candle ts - (K+1)*gran
        can be judged now: its own swing label and both neighbours' exist."""
        target = int(ts - (REV_K + 1) * gran)
        lab3 = self.lab3.a[-1]
        if np.all(np.isfinite(lab3)):
            for side, sgn in ((0, 1), (1, -1)):
                self.base_rate += 0.0005 * (lab3[side] - self.base_rate)
                c = self.calls.pop((target, sgn), None)
                if c is not None:
                    self.n_calls += 1
                    self.hit_rate += 0.01 * (lab3[side] - self.hit_rate)
                    self.events.append(("hit", (target, sgn, int(lab3[side]))))
        for k in [k for k in self.recent if k[0] < target - 3 * gran]:
            del self.recent[k]
        for k in [k for k in self.calls if k[0] < target - 3 * gran]:   # could not be judged (gap)
            del self.calls[k]

    def summary(self):
        w = self._weights()
        return {"weights": {e: round(float(x), 3) for e, x in zip(EXPERTS, w)},
                "brier_skill": round(float(1 - self.brier[0] / self.brier[1]), 4) if self.brier[1] > 0 else None,
                "threshold": round(self.thr, 3), "labels_learned": int(self.n_fit),
                "chance_per_horizon": [round(float(b), 3) for b in self.base]}
