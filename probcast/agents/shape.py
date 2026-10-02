"""Shape agent: how far above and below the last close will the next candle reach."""
import numpy as np

from .base import Agent, OnlineStd


class WickAgent(Agent):
    """Online median regression (SGD on the absolute loss) of the candle's
    reach above and below the last close (its high and low), in units of
    current volatility, on the feature vector."""
    name = "reach"
    role = "shape"

    def __init__(self, d, lr=0.01, l2=2e-3, min_n=300):
        self.W = np.zeros((2, d))
        self.b = np.full(2, 0.7)
        self.GW = np.full((2, d), 1e-2)
        self.Gb = np.full(2, 1e-2)
        self.std = OnlineStd(d)
        self.lr, self.l2, self.min_n, self.n = lr, l2, min_n, 0

    def observe(self, r, bar, ctx_prev):
        if ctx_prev is None or ctx_prev.get("x") is None or not ctx_prev.get("sigma"):
            return
        x = ctx_prev["x"]
        t = np.clip(np.array([bar["up"], bar["dn"]]) / ctx_prev["sigma"], 0, 10)
        xs = self.std.transform(x)
        pred = self.W @ xs + self.b
        g = (t < pred).astype(float) - 0.5
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
        return np.maximum(self.W @ self.std.transform(ctx["x"]) + self.b, 0.0) * ctx["sigma"]
