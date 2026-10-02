"""Mathematical building blocks: BOCPD, HMM, GARCH, RLS, mixture quantiles."""
import math

import numpy as np
from scipy.optimize import minimize
from scipy.special import gammaln, ndtr, stdtr

QUANTILES = np.array([0.05, 0.10, 0.25, 0.40, 0.50, 0.60, 0.75, 0.90, 0.95])

# grid in units of standard deviations: dense where the 5%..95% quantiles live
_G = np.concatenate([[-14, -9, -6.5, -5, -4.2], np.linspace(-3.6, 3.6, 73), [4.2, 5, 6.5, 9, 14]])


def pinball(q, y, taus=QUANTILES):
    """Pinball (quantile) loss per quantile. Mean over taus*2 approximates CRPS."""
    d = y - q
    return np.where(d >= 0, taus * d, (taus - 1) * d)


def quantiles_from_cdf(x, cdf, taus=QUANTILES):
    return np.interp(taus, cdf, x)


def normal_mixture_quantiles(w, sd, taus=QUANTILES):
    """Quantiles of sum_k w_k N(0, sd_k^2)."""
    s = np.sqrt(np.sum(w * sd ** 2))
    x = _G * s
    cdf = (w[None, :] * ndtr(x[:, None] / sd[None, :])).sum(1)
    return quantiles_from_cdf(x, cdf, taus)


# ---------------------------------------------------------------------------
class BOCPD:
    """Bayesian Online Changepoint Detection (Adams & MacKay 2007) with a
    Normal-Inverse-Gamma conjugate model: unknown mean AND variance per regime.
    The posterior over the current run length is updated exactly at every
    observation; the predictive is a Student-t mixture over run lengths."""

    def __init__(self, hazard=1 / 200, kappa0=10.0, alpha0=2.0, prune=1e-7, max_len=3000):
        self.h = hazard
        self.k0, self.a0 = kappa0, alpha0
        self.prune, self.max_len = prune, max_len
        self.rl = np.array([0])
        self.p = np.array([1.0])
        self.mu = np.array([0.0])
        self.kap = np.array([kappa0])
        self.al = np.array([alpha0])
        self.be = np.array([(alpha0 - 1) * 1.0])
        self.n = 0

    def _pred_params(self):
        df = 2 * self.al
        scale = np.sqrt(self.be * (self.kap + 1) / (self.al * self.kap))
        return df, self.mu, scale

    def update(self, x, prior_var):
        """x: new observation; prior_var: variance used as the prior scale for
        a regime that starts now (a slow-moving estimate)."""
        df, loc, sc = self._pred_params()
        z = (x - loc) / sc
        # Student-t density
        logpdf = (gammaln((df + 1) / 2) - gammaln(df / 2) - 0.5 * np.log(df * np.pi)
                  - np.log(sc) - (df + 1) / 2 * np.log1p(z * z / df))
        pred = np.exp(logpdf)
        grow = self.p * pred * (1 - self.h)
        cp = np.sum(self.p * pred * self.h)
        # posterior parameter updates for grown runs
        mu = (self.kap * self.mu + x) / (self.kap + 1)
        be = self.be + self.kap * (x - self.mu) ** 2 / (2 * (self.kap + 1))
        kap = self.kap + 1
        al = self.al + 0.5
        self.rl = np.concatenate([[0], self.rl + 1])
        p = np.concatenate([[cp], grow])
        tot = p.sum()
        p = p / tot if tot > 0 and np.isfinite(tot) else np.r_[1.0, np.zeros(len(grow))]
        self.mu = np.concatenate([[0.0], mu])
        self.kap = np.concatenate([[self.k0], kap])
        self.al = np.concatenate([[self.a0], al])
        self.be = np.concatenate([[(self.a0 - 1) * prior_var], be])
        keep = p > self.prune
        keep[0] = True
        if keep.sum() > self.max_len:
            thr = np.sort(p)[-self.max_len]
            keep &= p >= thr
            keep[0] = True
        self.rl, self.mu, self.kap = self.rl[keep], self.mu[keep], self.kap[keep]
        self.al, self.be = self.al[keep], self.be[keep]
        self.p = p[keep] / p[keep].sum()
        self.n += 1

    # summaries -------------------------------------------------------------
    def cp_prob(self, within=12):
        return float(self.p[self.rl < within].sum())

    def expected_run(self):
        return float((self.p * self.rl).sum())

    def predictive_sd(self):
        df, loc, sc = self._pred_params()
        var = sc ** 2 * df / np.maximum(df - 2, 0.5)
        m = (self.p * loc).sum()
        return float(np.sqrt((self.p * (var + (loc - m) ** 2)).sum()))

    def predictive_quantiles(self, taus=QUANTILES):
        df, loc, sc = self._pred_params()
        w = self.p
        if len(w) > 24:                       # keep the components carrying 99.5% of the mass
            order = np.argsort(w)[::-1]
            k = int(np.searchsorted(np.cumsum(w[order]), 0.995)) + 1
            idx = order[:min(max(k, 8), 64)]
            w, df, loc, sc = w[idx] / w[idx].sum(), df[idx], loc[idx], sc[idx]
        m = (w * loc).sum()
        s = self.predictive_sd()
        x = m + _G * s
        cdf = (w[None, :] * stdtr(df[None, :], (x[:, None] - loc[None, :]) / sc[None, :])).sum(1)
        return quantiles_from_cdf(x, cdf, taus)


# ---------------------------------------------------------------------------
class VolHMM:
    """K-state zero-mean Gaussian hidden Markov model = regime-switching
    volatility. Parameters by EM (Baum-Welch), state by the online forward
    filter."""

    def __init__(self, k=3):
        self.k = k
        self.A = None
        self.sd = None
        self.alpha = None          # filtered state probabilities

    def _emis(self, x):
        return np.exp(-0.5 * (x[:, None] / self.sd[None, :]) ** 2) / self.sd[None, :] + 1e-300

    def fit(self, x, iters=6, first_iters=40):
        x = np.asarray(x, float)
        T, K = len(x), self.k
        if self.A is None:
            ax = np.abs(x)
            qs = np.quantile(ax, np.linspace(0, 1, K + 1))
            self.sd = np.array([max(np.sqrt(np.mean(x[(ax >= qs[i]) & (ax <= qs[i + 1])] ** 2)), 1e-8)
                                for i in range(K)])
            self.A = np.full((K, K), 0.02 / (K - 1))
            np.fill_diagonal(self.A, 0.98)
            iters = first_iters
        pi = np.full(K, 1.0 / K)
        for _ in range(iters):
            B = self._emis(x)
            al = np.empty((T, K))
            cs = np.empty(T)
            a = pi * B[0]
            cs[0] = a.sum()
            al[0] = a / cs[0]
            A = self.A
            for t in range(1, T):
                a = (al[t - 1] @ A) * B[t]
                cs[t] = a.sum()
                al[t] = a / cs[t]
            be = np.empty((T, K))
            be[-1] = 1.0
            for t in range(T - 2, -1, -1):
                be[t] = (A @ (B[t + 1] * be[t + 1])) / cs[t + 1]
            gam = al * be
            gam /= gam.sum(1, keepdims=True)
            xi = (al[:-1, :, None] * A[None, :, :] * (B[1:] * be[1:])[:, None, :]) / cs[1:, None, None]
            A_new = xi.sum(0)
            A_new /= A_new.sum(1, keepdims=True)
            self.A = 0.999 * A_new + 0.001 / K          # keep every transition possible
            self.sd = np.sqrt((gam * x[:, None] ** 2).sum(0) / (gam.sum(0) + 1e-12))
            self.sd = np.maximum(self.sd, 1e-8)
            pi = gam[0]
        order = np.argsort(self.sd)
        self.sd = self.sd[order]
        self.A = self.A[np.ix_(order, order)]
        self.alpha = al[-1][order]
        return self

    def update(self, x):
        if self.A is None:
            return
        a = (self.alpha @ self.A) * self._emis(np.array([x]))[0]
        s = a.sum()
        self.alpha = a / s if s > 0 and np.isfinite(s) else np.full(self.k, 1.0 / self.k)

    def next_state_probs(self):
        return self.alpha @ self.A

    def predictive_quantiles(self, taus=QUANTILES):
        return normal_mixture_quantiles(self.next_state_probs(), self.sd, taus)


# ---------------------------------------------------------------------------
def garch_fit(r, start=(0.08, 0.90)):
    """GARCH(1,1) with variance targeting, Gaussian quasi-likelihood.
    Returns (omega, alpha, beta)."""
    r = np.asarray(r, float)
    v = float(np.var(r))
    r2 = (r * r).tolist()

    def nll(p):
        a, b = p
        if a < 1e-4 or b < 0.5 or a + b > 0.9995 or a > 0.4:
            return 1e12
        w = v * (1 - a - b)
        h = v
        tot = 0.0
        for x in r2:
            tot += math.log(h) + x / h
            h = w + a * x + b * h
        return tot

    res = minimize(nll, start, method="Nelder-Mead", options={"xatol": 1e-3, "fatol": 1e-2, "maxiter": 80})
    a, b = res.x if res.fun < 1e11 else start
    return v * (1 - a - b), float(a), float(b)


class RLS:
    """Recursive least squares with exponential forgetting."""

    def __init__(self, d, lam=0.9995, delta=100.0):
        self.w = np.zeros(d)
        self.P = np.eye(d) * delta
        self.lam = lam
        self.n = 0

    def predict(self, x):
        return float(self.w @ x)

    def update(self, x, y):
        Px = self.P @ x
        k = Px / (self.lam + x @ Px)
        self.w = self.w + k * (y - self.w @ x)
        self.P = (self.P - np.outer(k, Px)) / self.lam
        self.P = 0.5 * (self.P + self.P.T)
        self.n += 1
