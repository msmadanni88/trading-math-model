"""Agent interface.

Three kinds of agents share one blackboard (`ctx`, a dict the engine rebuilds
for every candle):

  ForecastAgent  outputs quantiles of the next candle's log return. The
                 orchestrator weights them by how well they have been doing.
  ShapeAgent     outputs the wick sizes of the next candle.
  SignalAgent    (extension point, none registered yet) writes named signals
                 onto the blackboard for the other agents to read: a BTC lead
                 signal, a trend state, volume-profile levels, ...

Every agent has the same life cycle, driven by the engine in strict time order:

  observe(r, bar, ctx_prev)  learn from the candle that just closed
  predict(ctx)               forecast the next candle (None while warming up)
  retrain(hist)              periodic heavier refit
"""
import numpy as np

from ..core import QUANTILES

NQ = len(QUANTILES)


class Ring:
    def __init__(self, n):
        self.a = np.full(n, np.nan)
        self.i = 0
        self.count = 0

    def add(self, x):
        self.a[self.i] = x
        self.i = (self.i + 1) % len(self.a)
        self.count = min(self.count + 1, len(self.a))

    def values(self):
        if self.count < len(self.a):
            return self.a[:self.count]
        return np.concatenate([self.a[self.i:], self.a[:self.i]])

    def quantiles(self, taus=QUANTILES):
        a = np.sort(self.a[:self.count] if self.count < len(self.a) else self.a)
        pos = taus * (len(a) - 1)
        lo = np.floor(pos).astype(int)
        hi = np.minimum(lo + 1, len(a) - 1)
        return a[lo] + (a[hi] - a[lo]) * (pos - lo)


class OnlineStd:
    """Running mean / variance used to standardise model inputs."""

    def __init__(self, d):
        self.mu, self.var, self.n = np.zeros(d), np.ones(d), 0

    def transform(self, x):
        return np.clip((x - self.mu) / np.sqrt(self.var + 1e-8), -4, 4)

    def update(self, x):
        k = 0.002 if self.n > 500 else 1.0 / (self.n + 1)
        self.mu += k * (x - self.mu)
        self.var += k * ((x - self.mu) ** 2 - self.var)
        self.n += 1


class Agent:
    name = "base"
    role = "forecast"

    def observe(self, r, bar, ctx_prev):
        pass

    def predict(self, ctx):
        return None

    def retrain(self, hist):
        return None


class ScaleAgent(Agent):
    """sigma forecast x empirical quantiles of past standardised residuals
    (filtered historical simulation: no distributional assumption)."""

    def __init__(self, zn=3000, zmin=300):
        self.z = Ring(zn)
        self.zmin = zmin
        self.sig_pred = None

    def _push_resid(self, r):
        if self.sig_pred is not None and self.sig_pred > 0:
            self.z.add(float(np.clip(r / self.sig_pred, -12, 12)))

    def predict(self, ctx):
        if self.sig_pred is None or self.z.count < self.zmin:
            return None
        return self.z.quantiles() * self.sig_pred
