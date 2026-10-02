"""Learning agents: models that map the feature vector to the distribution."""
import numpy as np

from ..config import LGBM_EMBARGO, LGBM_HOLDOUT
from ..core import QUANTILES, pinball
from .base import NQ, Agent, OnlineStd

_NORM_Q = np.array([-1.6449, -1.2816, -0.6745, -0.2533, 0.0, 0.2533, 0.6745, 1.2816, 1.6449])


class OnlineQR(Agent):
    """Linear quantile regression trained by stochastic gradient descent on the
    pinball loss: one update per candle. Target is the volatility-standardised
    return."""
    name = "online_qr"

    def __init__(self, d, lr=0.01, l2=2e-3, min_n=1000):
        self.W = np.zeros((NQ, d))
        self.b = _NORM_Q.copy()
        self.GW = np.full((NQ, d), 1e-2)
        self.Gb = np.full(NQ, 1e-2)
        self.std = OnlineStd(d)
        self.lr, self.l2, self.min_n = lr, l2, min_n
        self.n = 0

    def observe(self, r, bar, ctx_prev):
        if ctx_prev is None or ctx_prev.get("x") is None or not ctx_prev.get("sigma"):
            return
        x = ctx_prev["x"]
        z = float(np.clip(r / ctx_prev["sigma"], -10, 10))
        xs = self.std.transform(x)
        pred = self.W @ xs + self.b
        g = (z < pred).astype(float) - QUANTILES          # d pinball / d pred
        gW = g[:, None] * xs[None, :] + self.l2 * self.W
        self.GW += gW * gW
        self.Gb += g * g
        self.W -= self.lr * gW / np.sqrt(self.GW)
        self.b -= self.lr * g / np.sqrt(self.Gb)
        self.std.update(x)
        self.n += 1

    def predict(self, ctx):
        if self.n < self.min_n or ctx.get("x") is None or not ctx.get("sigma"):
            return None
        return np.sort(self.W @ self.std.transform(ctx["x"]) + self.b) * ctx["sigma"]


LGB_PARAMS = dict(objective="quantile", learning_rate=0.03, num_leaves=8, min_data_in_leaf=400,
                  feature_fraction=0.7, bagging_fraction=0.7, bagging_freq=1, lambda_l2=10.0,
                  verbose=-1, seed=7, deterministic=True, force_col_wise=True, num_threads=2)
LGB_ROUNDS = 120


class Lgbm(Agent):
    """Gradient-boosted quantile trees on a rolling 30-day window. A new model
    (challenger) replaces the current one (champion) only if it has a lower
    pinball loss on the latest two days, which it never saw."""
    name = "lgbm"

    def __init__(self, min_n=8000):
        self.models = None            # list of model strings (picklable)
        self._boost = None
        self.min_n = min_n

    def __getstate__(self):
        s = dict(self.__dict__)
        s["_boost"] = None
        return s

    def _boosters(self):
        if self._boost is None and self.models is not None:
            import lightgbm as lgb
            self._boost = [lgb.Booster(model_str=m) for m in self.models]
        return self._boost

    @staticmethod
    def _predict(boost, X):
        return np.sort(np.column_stack([b.predict(X) for b in boost]), axis=1)

    def retrain(self, hist):
        import lightgbm as lgb
        X, z = hist["X"], hist["z"]
        if len(z) < self.min_n:
            return None
        cut = len(z) - LGBM_HOLDOUT
        Xtr, ztr = X[:cut - LGBM_EMBARGO], z[:cut - LGBM_EMBARGO]
        Xho, zho = X[cut:], z[cut:]
        cand = []
        for tau in QUANTILES:
            ds = lgb.Dataset(Xtr, label=ztr, free_raw_data=False)
            cand.append(lgb.train(dict(LGB_PARAMS, alpha=float(tau)), ds, num_boost_round=LGB_ROUNDS))
        l_c = float(pinball(self._predict(cand, Xho), zho[:, None]).mean())
        info = {"challenger_loss": round(l_c, 5)}
        cur = self._boosters()
        if cur is not None:
            l_o = float(pinball(self._predict(cur, Xho), zho[:, None]).mean())
            info["champion_loss"] = round(l_o, 5)
            info["promoted"] = bool(l_c < l_o)
            if not info["promoted"]:
                return info
        else:
            info["promoted"] = True
        self.models = [b.model_to_string() for b in cand]
        self._boost = cand
        return info

    def predict(self, ctx):
        b = self._boosters()
        if b is None or ctx.get("x") is None or not ctx.get("sigma"):
            return None
        return self._predict(b, ctx["x"][None, :])[0] * ctx["sigma"]
