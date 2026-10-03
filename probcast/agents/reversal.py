"""Reversal agents: where are the turning points?

DEFINITION. Candle s is a swing high of size K if its high is the highest of
the K candles before it and the K candles after it (swing low: mirrored).
There is one agent per swing size K (config.REV_KS): small K = every little
turn, large K = only the turns that matter for a quarter of an hour.

WHAT AN AGENT SAYS. After every candle t it gives, for tops and for bottoms,

    now   P(a swing point forms at candle t-1, t or t+1)     "the turn is in"
    next  P(a swing point forms at candle t+1, t+2 or t+3)   "a turn is coming"

Neither can be read off the chart at time t: a swing point is only confirmed
K candles later. "next" names minutes that have not started at all.

MODEL. A gradient-boosted tree classifier (LightGBM) on what the last candles
look like relative to the recent extremes (student.rev_features). A bottom is
a top of the mirrored price, so both sides share one model and every candle
gives two training examples. The fitted trees are published as plain numbers;
the site walks the same trees, so a call made in the browser and the call the
cloud stores are the same call.

SELF-TRAINING. Every swing label that becomes known is a new training row.
Once a day a challenger is trained and replaces the champion only if it
predicts the latest two days - which it never saw - better. If the hit rate
of the calls has been falling, the daily contest widens: several challengers
with different memory and complexity compete instead of one.

GOAL. The hit rate of the calls. A call is made when the probability is at
least the agent's confidence threshold, and it is a hit if a swing point of
that side forms within one candle of the minute it names. Calls of one type
and side never name minutes closer than three candles apart. Every six hours the
agent re-picks the threshold that gave the best hit rate over its last seven
days among those that still make REV_MIN_PER_DAY calls a day - it may become
pickier, but it may not go silent. A call is stored when it is made and never
edited; only its outcome is filled in.

A label is only known K + 1 candles after its candle, so all learning here is
delayed by a few candles; nothing ever uses a candle that has not closed.
"""
import numpy as np

from .. import student
from ..config import LGBM_EMBARGO, LGBM_HOLDOUT, REV_HS, REV_MIN_PER_DAY, REV_TRAIN, REV_TUNE_WIN

D = len(student.REV_FEATURES)
NH = len(REV_HS)
HMAX = max(REV_HS)
TYPES = ("now", "next")
LGB_BASE = dict(objective="binary", learning_rate=0.05, num_leaves=16, min_data_in_leaf=250,
                feature_fraction=0.8, bagging_fraction=0.7, bagging_freq=1, lambda_l2=5.0,
                verbose=-1, seed=11, deterministic=True, force_col_wise=True, num_threads=2)
# the daily contest: one challenger normally, all three when the hit rate has been falling
CONTEST = [dict(rows=REV_TRAIN, rounds=100),
           dict(rows=REV_TRAIN // 2, rounds=80, num_leaves=12),
           dict(rows=REV_TRAIN, rounds=160, num_leaves=31, learning_rate=0.03, min_data_in_leaf=150)]
RATES = (1.0, 1.25, 1.6, 2.0, 2.6, 3.4, 4.5, 6.0, 8.0)       # thresholds tried: these multiples of the minimum call rate


def _logloss(p, y):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def wilson_low(hits, n, z=1.64):
    """Lower end of the confidence interval of a hit rate: a threshold is
    preferred only if it is better beyond what luck explains."""
    if n == 0:
        return 0.0
    p = hits / n
    return (p + z * z / (2 * n) - z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / (1 + z * z / n)


def spaced(idx, gap=2):
    """Calls of one side cannot name minutes within `gap` candles of each
    other: keep the first of every such cluster (idx sorted ascending)."""
    keep, last = [], -10 ** 9
    for i in idx:
        if i - last > gap:
            keep.append(i)
            last = i
    return keep


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
    role = "reversal"

    def __init__(self, K):
        self.K = K
        self.name = f"reversal_k{K}"
        self.lag = K + 1 + HMAX                     # candles until every label of an origin is known
        self.hl = _Ring(2 * K + 2, (2,))            # high, low of the latest candles
        self.phi = _Ring(self.lag + 2, (2, D))      # features, [top, bottom]
        self.lab = _Ring(4, (2,))                   # is candle t-K a swing point [top, bottom]
        self.lab3 = _Ring(HMAX + 2, (2,))           # ... is there one within a candle of candle t-K-1
        self.n = 0
        self.n_fit = 0
        # rolling training set of the tree model (two rows per candle: top, bottom)
        self.tX = np.zeros((2 * 2 * REV_TRAIN, D), dtype=np.float32)
        self.tY = np.zeros((2 * 2 * REV_TRAIN, NH), dtype=np.float32)
        self.tn = 0
        self.model_str, self.model_id, self._boost = None, 0, None
        self.models = {}                            # id -> packed trees (what is published)
        # what the published model said on each of the last REV_TUNE_WIN candles, and what happened
        self.hP = np.full((REV_TUNE_WIN, 2, NH), np.nan)
        self.hY = np.full((REV_TUNE_WIN, 2, NH), np.nan)
        self.thr = [0.60, 0.45]                     # confidence thresholds [now, next]
        self.tuned = None                           # how the thresholds were last picked
        self.base = np.full(NH, 0.2)                # how often the event happens anyway (chance)
        self.calls = {}                             # (for_ts, side, type) -> call awaiting its outcome
        self.recent = {}                            # (for_ts, side, type) -> True, for de-duplication
        self.events = []                            # new calls / outcomes since the last drain
        self.count = np.zeros(NH)                   # judged calls per type
        self.hits = np.zeros(NH)
        self.fast = np.full(NH, np.nan)             # recent hit rate (about the last 60 calls)
        self.slow = np.full(NH, np.nan)             # long-run hit rate (about the last 600 calls)
        self.brier = np.zeros(2)                    # running Brier score: model, chance

    def __getstate__(self):
        s = dict(self.__dict__)
        s["_boost"] = None
        s["models"] = {k: {a: b for a, b in m.items() if a != "_np"} for k, m in self.models.items()}
        return s

    # ------------------------------------------------------------------ model
    def _booster(self):
        if self._boost is None and self.model_str is not None:
            import lightgbm as lgb
            self._boost = lgb.Booster(model_str=self.model_str)
        return self._boost

    @staticmethod
    def _stack(X):
        """(n, D) -> (n * NH, D + 1): one row per call type, the type's horizon as the last feature."""
        j = np.tile(np.asarray(REV_HS, dtype=np.float32), len(X))[:, None]
        return np.hstack([np.repeat(X, NH, axis=0), j])

    def stalled(self):
        """True when the recent hit rate of either call type has dropped below its long-run level."""
        ok = (self.count >= 300) & np.isfinite(self.fast) & np.isfinite(self.slow)
        return bool(np.any(ok & (self.fast < self.slow - 0.03)))

    def retrain(self, ts):
        """Daily contest. Challengers are trained on everything except the
        latest two days and judged on those two days; the best one replaces
        the champion only if it beats it there."""
        import lightgbm as lgb
        hold = 2 * LGBM_HOLDOUT
        if self.tn < 3 * hold:
            return None
        wide = self.stalled()
        Xho, yho = self._stack(self.tX[self.tn - hold:self.tn]), self.tY[self.tn - hold:self.tn].ravel()
        best, tried = None, []
        for cfg in (CONTEST if wide else CONTEST[:1]):
            cfg = dict(cfg)
            rows, rounds = 2 * cfg.pop("rows"), cfg.pop("rounds")
            lo = max(0, self.tn - hold - rows)
            hi = self.tn - hold - 2 * LGBM_EMBARGO
            m = lgb.train(dict(LGB_BASE, **cfg), lgb.Dataset(self._stack(self.tX[lo:hi]), label=self.tY[lo:hi].ravel(),
                                                             free_raw_data=False), num_boost_round=rounds)
            loss = float(_logloss(m.predict(Xho), yho).mean())
            tried.append(round(loss, 5))
            if best is None or loss < best[0]:
                best = (loss, m)
        info = {"challenger_loss": round(best[0], 5), "challengers": len(tried),
                "chance_loss": round(float(_logloss(self.tY[:self.tn - hold].mean(), yho).mean()), 5),
                "widened": wide}
        cur = self._booster()
        if cur is not None:
            l_o = float(_logloss(cur.predict(Xho), yho).mean())
            info["champion_loss"] = round(l_o, 5)
            info["promoted"] = bool(best[0] < l_o)
            if not info["promoted"]:
                return info
        else:
            info["promoted"] = True
        self.model_str, self._boost = best[1].model_to_string(), best[1]
        self.model_id = int(ts)
        self.models[self.model_id] = student.pack_trees(best[1].dump_model())
        for k in sorted(self.models)[:-3]:              # the last three stay available to the site
            del self.models[k]
        return info

    def probs(self, model_id, phi_top, phi_bottom):
        """What the published model `model_id` says: array (2 sides, NH types), or None."""
        m = self.models.get(model_id)
        if m is None or phi_top is None:
            return None
        return student.tree_probs(m, student.rev_rows(phi_top, phi_bottom, REV_HS)).reshape(2, NH)

    # ------------------------------------------------------------------ one candle
    def observe(self, ts, gran, high, low, phi_top, phi_bottom):
        """Called once per closed candle, before anything is said about it.
        Resolves the swing label that just became known, judges the calls
        that named it and adds the training row whose labels are complete."""
        K = self.K
        self.hl.push([high, low])
        self.phi.push(np.vstack([phi_top, phi_bottom]) if phi_top is not None else np.nan)
        self.n += 1
        pos = (self.n - 1) % REV_TUNE_WIN
        self.hP[pos] = np.nan
        self.hY[pos] = np.nan
        if self.n < 2 * K + 1:
            self.lab.push(np.nan)
            self.lab3.push(np.nan)
            return
        w = self.hl.a[-(2 * K + 1):]
        s = w[K]                                       # candle t-K: now K candles on each side are known
        self.lab.push([float(s[0] >= w[:, 0].max()), float(s[1] <= w[:, 1].min())])
        l3 = self.lab.a[-3:].max(0)                    # centre t-K-1: a swing among t-K-2, t-K-1, t-K
        self.lab3.push(l3)
        if not np.all(np.isfinite(l3)):
            return
        # calls that named candle t-K-1 can be judged now
        target = int(ts - (K + 1) * gran)
        for side, sgn, a in ((0, 1, 0), (0, 1, 1), (1, -1, 0), (1, -1, 1)):
            c = self.calls.pop((target, sgn, a), None)
            if c is not None:
                hit = float(l3[side])
                self.count[a] += 1
                self.hits[a] += hit
                n = self.count[a]                      # plain average until enough calls, then a moving one
                self.fast[a] = hit if n == 1 else self.fast[a] + (hit - self.fast[a]) / min(n, 60)
                self.slow[a] = hit if n == 1 else self.slow[a] + (hit - self.slow[a]) / min(n, 600)
                self.events.append(("hit", (target, self.K, sgn, a, int(hit))))
        for store in (self.recent, self.calls):         # forget what can no longer matter
            for k in [k for k in store if k[0] < target - 3 * gran]:
                del store[k]
        # the origin whose labels are all known now: t - lag
        Y = np.array([self.lab3.back(HMAX - j) for j in REV_HS]).T      # (2 sides, NH)
        X = self.phi.back(self.lag)
        if not (np.all(np.isfinite(Y)) and np.all(np.isfinite(X))):
            return
        op = (self.n - 1 - self.lag) % REV_TUNE_WIN
        self.hY[op] = Y
        P = self.hP[op]
        if np.all(np.isfinite(P)):
            k = 0.0005
            self.brier += k * (np.array([((P - Y) ** 2).mean(), ((self.base[None, :] - Y) ** 2).mean()]) - self.brier)
        self.base += 0.0005 * (Y.mean(0) - self.base)
        if self.tn + 2 > len(self.tX):                 # rolling training set
            keep = 2 * REV_TRAIN
            self.tX[:keep], self.tY[:keep] = self.tX[self.tn - keep:self.tn], self.tY[self.tn - keep:self.tn]
            self.tn = keep
        self.tX[self.tn:self.tn + 2], self.tY[self.tn:self.tn + 2] = X, Y
        self.tn += 2
        self.n_fit += 1

    def record(self, P):
        """P: what the published model said after this candle (2, NH) or None."""
        self.hP[(self.n - 1) % REV_TUNE_WIN] = np.nan if P is None else P

    def call(self, ts, gran, P, thr, close, model_id):
        """ts: the candle that just closed. P: probabilities of the published
        model `model_id` (2, NH). thr: published thresholds [now, next].
        The two call types are separate records: a turn can first be called
        as coming and then, when it happens, as in."""
        out = []
        if P is None or thr is None:
            return out
        for side, sgn in ((0, 1), (1, -1)):
            for a, j in enumerate(REV_HS):
                p = float(P[side, a])
                if not p >= thr[a]:
                    continue
                for_ts = int(ts + j * gran)
                if any((for_ts + d * gran, sgn, a) in self.recent for d in (-2, -1, 0, 1, 2)):
                    continue                           # that turning point is already called (same call type)
                if j == 0:                             # the extreme of the turn that is in
                    lv = self.hl.a[-2:, side]
                    level = float(np.nanmax(lv) if sgn > 0 else np.nanmin(lv))
                else:                                  # not printed yet: marked at the last price
                    level = float(close)
                c = {"made_ts": int(ts + gran), "for_ts": for_ts, "k": self.K, "side": sgn, "typ": a,
                     "p": round(p, 4), "level": round(level, 2), "model": int(model_id)}
                self.calls[(for_ts, sgn, a)] = c
                self.recent[(for_ts, sgn, a)] = True
                self.events.append(("new", c))
                out.append(c)
        return out

    # ------------------------------------------------------------------ self-tuning
    def history(self):
        """(P, Y) of the last REV_TUNE_WIN candles in time order."""
        k = self.n % REV_TUNE_WIN
        return np.roll(self.hP, -k, axis=0), np.roll(self.hY, -k, axis=0)

    @staticmethod
    def simulate(P, Y, a, thr):
        """Calls of type `a` the threshold would have produced on a history:
        (number, hits). Only minutes whose outcome is known count."""
        n = h = 0
        for side in (0, 1):
            ok = np.isfinite(Y[:, side, a]) & (P[:, side, a] >= thr)
            idx = spaced(np.nonzero(ok)[0])
            n += len(idx)
            h += float(Y[idx, side, a].sum()) if idx else 0.0
        return n, h

    def tune(self):
        """Re-pick the thresholds: best hit rate (beyond luck) over the last
        seven days among thresholds that keep at least REV_MIN_PER_DAY calls a day."""
        P, Y = self.history()
        info = {}
        for a in range(NH):
            known = np.isfinite(Y[:, :, a]) & np.isfinite(P[:, :, a])
            days = known[:, 0].sum() / 1440.0
            if days < 2.0:
                continue
            p = np.sort(P[:, :, a][known])
            tried = []
            for mult in RATES:
                want = int(REV_MIN_PER_DAY * mult * days)
                if want >= len(p):
                    break
                thr = float(p[-want - 1])
                n, h = self.simulate(P, Y, a, thr)
                tried.append((wilson_low(h, n), thr, n, h))
            if not tried:
                continue
            enough = [t for t in tried if t[2] / days >= REV_MIN_PER_DAY]
            best = max(enough) if enough else max(tried, key=lambda t: t[2])
            new = float(min(max(0.5 * self.thr[a] + 0.5 * best[1], 0.05), 0.98))
            info[TYPES[a]] = {"threshold": round(new, 4), "calls_per_day": round(best[2] / days, 1),
                              "hit_rate": round(best[3] / max(best[2], 1), 4)}
            self.thr[a] = new
        if info:
            self.tuned = info
        return info

    def summary(self):
        out = {"k": self.K, "model_id": int(self.model_id), "labels_learned": int(self.n_fit),
               "brier_skill": round(float(1 - self.brier[0] / self.brier[1]), 4) if self.brier[1] > 0 else None,
               "stalled": self.stalled(), "types": {}}
        for a, t in enumerate(TYPES):
            out["types"][t] = {"threshold": round(float(self.thr[a]), 4), "chance": round(float(self.base[a]), 4),
                               "calls": int(self.count[a]),
                               "hit_rate": round(float(self.hits[a] / self.count[a]), 4) if self.count[a] else None,
                               "recent": None if not np.isfinite(self.fast[a]) else round(float(self.fast[a]), 4),
                               "long_run": None if not np.isfinite(self.slow[a]) else round(float(self.slow[a]), 4)}
        return out
