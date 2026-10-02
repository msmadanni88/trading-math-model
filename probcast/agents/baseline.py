from .base import Agent, Ring


class Empirical(Agent):
    """Unconditional benchmark: empirical quantiles of the last day. Every
    other agent is measured against this one."""
    name = "empirical"

    def __init__(self, n=1440, min_n=240):
        self.buf, self.min_n = Ring(n), min_n

    def observe(self, r, bar, ctx_prev):
        self.buf.add(r)

    def predict(self, ctx):
        return self.buf.quantiles() if self.buf.count >= self.min_n else None
