"""Volatility agents: how big will the next candle be."""
import numpy as np

from ..config import W_LONG
from ..core import RLS, garch_fit
from .base import Ring, ScaleAgent


class Ewma(ScaleAgent):
    name = "ewma"

    def __init__(self, lam=0.97):
        super().__init__()
        self.lam, self.var, self.warm = lam, None, []

    def observe(self, r, bar, ctx_prev):
        self._push_resid(r)
        if self.var is None:
            self.warm.append(r)
            if len(self.warm) >= 60:
                self.var = float(np.mean(np.square(self.warm)))
                self.warm = []
        else:
            self.var = self.lam * self.var + (1 - self.lam) * r * r
        self.sig_pred = None if not self.var else float(np.sqrt(self.var))


class Garch(ScaleAgent):
    name = "garch"

    def __init__(self, window=6000, min_n=2000):
        super().__init__()
        self.par, self.h = None, None
        self.window, self.min_n = window, min_n

    def observe(self, r, bar, ctx_prev):
        self._push_resid(r)
        if self.par is not None:
            w, a, b = self.par
            self.h = w + a * r * r + b * self.h
            self.sig_pred = float(np.sqrt(self.h))

    def retrain(self, hist):
        r = hist["r"][-self.window:]
        if len(r) < self.min_n or float(np.var(r)) <= 0:
            return None
        start = (self.par[1], self.par[2]) if self.par else (0.08, 0.90)
        w, a, b = garch_fit(r, start)
        self.par = (w, a, b)
        h = float(np.var(r))
        for x in r:
            h = w + a * x * x + b * h
        self.h = h
        self.sig_pred = float(np.sqrt(h))
        return {"alpha": round(a, 4), "beta": round(b, 4)}


class Har(ScaleAgent):
    """HAR-type model on Garman-Klass range variance with intraday
    seasonality, fitted online by recursive least squares with forgetting."""
    name = "har"

    def __init__(self):
        super().__init__()
        self.gk = Ring(W_LONG)
        self.rls = RLS(9, lam=0.9998)
        self.x_prev = None

    def _x(self, cal):
        g = self.gk.values()
        m = g.mean()
        fl = 0.05 * m + 1e-14
        lg = lambda v: np.log(v + fl)
        return np.array([1.0, lg(g[-1]), lg(g[-5:].mean()), lg(g[-30:].mean()), lg(m), *cal]), fl

    def observe(self, r, bar, ctx_prev):
        self._push_resid(r)
        if self.x_prev is not None:
            x, fl = self.x_prev
            self.rls.update(x, float(np.log(bar["gk"] + fl)))
        self.gk.add(bar["gk"])
        self.x_prev = None
        self.sig_pred = None
        if self.gk.count >= W_LONG:
            x, fl = self._x(bar["cal_next"])
            self.x_prev = (x, fl)
            if self.rls.n >= 1000:
                self.sig_pred = float(np.exp(0.5 * np.clip(self.rls.predict(x), -40, 0)))
