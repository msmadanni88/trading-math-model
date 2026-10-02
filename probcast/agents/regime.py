"""Regime agents: has the market just changed its behaviour."""
import numpy as np

from ..core import VolHMM
from .base import Agent


class BocpdAgent(Agent):
    """Predictive Student-t mixture of the Bayesian changepoint model. The
    model itself is shared: the engine updates it and publishes its summaries
    on the blackboard for every other agent."""
    name = "bocpd"

    def predict(self, ctx):
        b = ctx["bocpd"]
        if b.n < 500:
            return None
        return b.predictive_quantiles() / ctx["bocpd_scale"]


class Hmm(Agent):
    """3-state volatility hidden Markov model, online forward filter."""
    name = "hmm"

    def __init__(self, window=6000, min_n=2000):
        self.m = VolHMM(3)
        self.window, self.min_n = window, min_n
        self.scale = 1e4

    def observe(self, r, bar, ctx_prev):
        self.m.update(r * self.scale)

    def retrain(self, hist):
        r = hist["r"][-self.window:]
        if len(r) < self.min_n or float(np.var(r)) <= 0:
            return None
        self.m.fit(r * self.scale)
        return {"sd_bp": [round(float(s), 2) for s in self.m.sd],
                "stay": [round(float(x), 3) for x in np.diag(self.m.A)]}

    def predict(self, ctx):
        if self.m.A is None:
            return None
        return self.m.predictive_quantiles() / self.scale
