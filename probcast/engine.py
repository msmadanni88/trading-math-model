"""The orchestrator.

For every closed candle, strictly in time order:
  1. score the forecast and the generated candle that were made for it,
  2. re-weight the forecast agents (Hedge), update the calibration layer and
     let every agent learn from the candle,
  3. periodically refit the heavier models,
  4. forecast the next candle: calibrated return distribution (teacher),
     wick sizes, and the generated candle the site draws (student).
Evaluation is therefore always out-of-sample (prequential): a forecast is
stored before its outcome exists.
"""
import numpy as np

from . import student
from .agents.learners import Lgbm
from .agents.registry import forecast_agents, shape_agents, signal_agents
from .agents.reversal import ReversalAgent
from .config import (GRAN, HORIZON, LGBM_EVERY, RETRAIN_EVERY, REV_H, STUDENT_LEAD, STUDENT_ROWS,
                     STUDENT_ROWS_H, STUDENT_STEP, STUDENT_WIN, TRAIN_WINDOW)
from .core import BOCPD, QUANTILES, pinball
from .features import feature_names
from .goal import candle_score

STATE_VERSION = 4            # bump when a change makes old saved state invalid
EXTRA = ["cp_prob", "log_run", "bocpd_lsd"]
BP = 1e4
NQ = len(QUANTILES)
_RAMP = np.arange(NQ) * 1e-13


class Hist:
    """Append-only rolling window without re-allocating on every candle."""

    def __init__(self, window, shape=(), dtype=float):
        self.w = window
        self.a = np.empty((2 * window,) + tuple(shape), dtype=dtype)
        self.n = 0

    def add(self, v):
        if self.n == len(self.a):
            self.a[:self.w] = self.a[self.w:]
            self.n = self.w
        self.a[self.n] = v
        self.n += 1

    def view(self):
        return self.a[max(0, self.n - self.w):self.n]

    def __len__(self):
        return min(self.n, self.w)


class Hedge:
    """Exponentially weighted aggregation with discounted losses: an agent's
    weight follows its recent out-of-sample pinball loss."""

    def __init__(self, names, eta=0.25, decay=0.998, floor=0.02):
        self.L = {n: 0.0 for n in names}
        self.eta, self.decay, self.floor = eta, decay, floor
        self.scale = None

    def weights(self, active):
        if not active:
            return {}
        for n in active:                      # an agent added later starts neutral
            if n not in self.L:
                self.L[n] = float(np.mean(list(self.L.values()))) if self.L else 0.0
        L = np.array([self.L[n] for n in active])
        w = np.exp(-self.eta * (L - L.min()))
        w /= w.sum()
        w = (1 - self.floor) * w + self.floor / len(active)
        return dict(zip(active, w))

    def update(self, losses):
        m = float(np.mean(list(losses.values())))
        self.scale = m if self.scale is None else 0.999 * self.scale + 0.001 * m
        sc = max(self.scale, 1e-12)
        for n in self.L:
            # agents that did not forecast get the average loss (neutral)
            self.L[n] = self.decay * self.L[n] + losses.get(n, m) / sc


class QuantileTracker:
    """Online conformal calibration (adaptive conformal inference / quantile
    tracking). Each quantile gets an additive offset, in units of current
    volatility, nudged after every candle so that the long-run frequency of
    `y <= q_tau` converges to tau even when the market shifts."""

    def __init__(self, gamma=0.01):
        self.theta = np.zeros(NQ)
        self.gamma = gamma

    def apply(self, q, scale):
        return np.sort(q + self.theta * scale)

    def update(self, q_cal, y):
        self.theta += self.gamma * (QUANTILES - (y <= q_cal))


class GoalTuner:
    """Closes the loop between the forecast and the goal. The probabilistic
    model says how big a candle typically is; this layer learns, from the
    realised candle-match score itself, how to turn that into the generated
    candle that scores best: it keeps a running score for a grid of body and
    reach multipliers and always uses the current winners."""
    BODY = np.array([0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6])
    REACH = np.array([0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.8, 2.0])

    def __init__(self, decay=0.9995, warm=720):
        self.sb = np.zeros(len(self.BODY))
        self.sr = np.zeros(len(self.REACH))
        self.decay, self.warm, self.n = decay, warm, 0

    def scales(self):
        if self.n < self.warm:
            return 1.0, 1.0
        return float(self.BODY[int(np.argmax(self.sb))]), float(self.REACH[int(np.argmax(self.sr))])

    @staticmethod
    def candle(base, kb, kr):
        """base = (direction, median |body|, reach up, reach down) -> (b, u, d)"""
        d, a, e_up, e_dn = base
        b = d * a * kb
        return b, max(kr * e_up - max(b, 0.0), 0.0), max(kr * e_dn - max(-b, 0.0), 0.0)

    def update(self, base, ao, ac, ah, al):
        d, a, e_up, e_dn = base
        kb, kr = self.scales()
        b = d * a * self.BODY
        body, _, _ = candle_score(b, 0.0, 0.0, ao, ac, ah, al)
        b0 = d * a * kb
        up = np.maximum(self.REACH * e_up, max(b0, 0.0))
        dn = np.maximum(self.REACH * e_dn, max(-b0, 0.0))
        inter = np.maximum(0.0, np.minimum(up, ah) - np.maximum(-dn, al))
        union = np.maximum(up, ah) - np.minimum(-dn, al)
        rng = np.where(union > 0, inter / np.where(union > 0, union, 1.0), 1.0)
        k = 1 - self.decay
        self.sb += k * (body - self.sb)
        self.sr += k * (rng - self.sr)
        self.n += 1


def _cdf(q, x):
    return float(np.interp(x, q + _RAMP, QUANTILES))


def p_up(q, eps):
    """P(next close above the last close | it moves), read off the quantile
    curve. `eps` is a tiny band around zero (unchanged closes are common on
    one-minute candles)."""
    up, dn = 1.0 - _cdf(q, eps), _cdf(q, -eps)
    return float(np.clip(up / (up + dn), 0.02, 0.98)) if up + dn > 0 else 0.5


def median_abs(q):
    """Median of |return| implied by the quantile curve: m with
    F(m) - F(-m) = 0.5."""
    lo, hi = 0.0, float(max(abs(q[0]), abs(q[-1]))) + 1e-12
    for _ in range(40):
        m = 0.5 * (lo + hi)
        if _cdf(q, m) - _cdf(q, -m) < 0.5:
            lo = m
        else:
            hi = m
    return 0.5 * (lo + hi)


class Engine:
    def __init__(self, fast_backfill=False):
        self.version = STATE_VERSION
        self.fnames = feature_names()
        d = len(self.fnames) + len(EXTRA)
        self.agents = forecast_agents(d)
        self.shapers = shape_agents(d)
        self.signals = signal_agents()
        self.names = [e.name for e in self.agents]
        self.hedge = Hedge(self.names)
        self.calib = QuantileTracker()
        self.tuner = GoalTuner()
        self.bocpd = BOCPD()
        self.last_ts = None
        self.prev_close = None
        self.n = 0
        self.var_fast = None                 # EWMA variance used as the scale
        self.var_slow = None
        self.pending = None
        self.r_hist = Hist(TRAIN_WINDOW)
        self.X = Hist(TRAIN_WINDOW, (d,), np.float32)
        self.z = Hist(TRAIN_WINDOW, (), np.float32)
        self.retrain_log = []
        self.fast_backfill = fast_backfill
        # student (live generator)
        self.candles = Hist(STUDENT_WIN + 1, (5,))
        ns, no = len(student.FEATURES), len(student.OUTPUTS)
        self.sX = Hist(STUDENT_ROWS_H, (ns,))
        self.sY = Hist(STUDENT_ROWS_H, (no,))
        self.sT = Hist(STUDENT_ROWS_H, (), np.int64)
        self.sS = Hist(STUDENT_ROWS_H)                    # volatility scale of each row
        self.oT = Hist(STUDENT_ROWS_H + 64, (), np.int64)  # what every candle actually did:
        self.oY = Hist(STUDENT_ROWS_H + 64, (3,))          #   return, reach up, reach down
        self.versions = []                   # [{"eff", "W", "H", "scale", "cone", "n", "r2"}]
        # candles 2..HORIZON: one goal tuner and one cone width per horizon
        self.tuners_h = [GoalTuner() for _ in range(HORIZON - 1)]
        self.cone = [float(np.sqrt(h)) for h in range(2, HORIZON + 1)]
        self.multi = {}                      # target ts -> {h: what was generated h candles ahead}
        # reversal agent and the rows its browser-side copy is distilled from
        self.rev = ReversalAgent()
        nr = len(student.REV_FEATURES)
        self.rP = Hist(STUDENT_ROWS_H, (2, nr))
        self.rL = Hist(STUDENT_ROWS_H, (2, REV_H + 1))
        self.cum = 0.0                       # cumulative log return (to score the cones)
        self.simulate_publish = True         # replay mode: emulate a cloud run every STUDENT_STEP

    # ------------------------------------------------------------------
    def _retrain(self, ts):
        hist = {"r": self.r_hist.view(), "X": self.X.view(), "z": self.z.view()}
        entry = {"ts": int(ts)}
        every_l = LGBM_EVERY * (4 if self.fast_backfill else 1)
        for e in self.agents + self.shapers:
            if isinstance(e, Lgbm) and self.n % every_l != 0:
                continue
            info = e.retrain(hist)
            if info is not None:
                entry[e.name] = info
        if self.n % every_l == 0:
            info = self.rev.retrain()
            if info is not None:
                entry["reversal"] = info
        if len(entry) > 1:
            self.retrain_log.append(entry)
            self.retrain_log = self.retrain_log[-60:]

    def fit_student(self, eff, cutoff_ts):
        """Fit a new live-generator version using only what was known at
        `cutoff_ts`; it becomes effective at `eff`."""
        if self.versions and self.versions[-1]["eff"] >= eff:
            return None
        T = self.sT.view()
        ok = T <= cutoff_ts
        if ok.sum() < 600:
            return None
        rnd = lambda A: np.array([float(f"{x:.9g}") for x in np.ravel(A)]).reshape(np.shape(A))
        # candle 1: distilled from the full model (latest STUDENT_ROWS rows)
        X, Y = self.sX.view()[ok][-STUDENT_ROWS:], self.sY.view()[ok][-STUDENT_ROWS:]
        W = rnd(student.fit(X, Y))            # rounded: the published numbers ARE the ones used
        res = Y - X @ W.T
        r2 = 1 - res.var(0) / np.maximum(Y.var(0), 1e-12)
        # candles 2..HORIZON: learned from what the market really did. While
        # replaying history these heads are refitted every 30 minutes instead
        # of every 5 (the last ones are reused in between) to keep a rebuild fast.
        prev = self.versions[-1] if self.versions else None
        if self.simulate_publish and prev is not None and prev.get("H") is not None and eff % 1800 != 0:
            H = prev["H"]
        else:
            H, oT, oY = [], self.oT.view(), self.oY.view()
            Xa, Sa = self.sX.view(), self.sS.view()
            for h in range(2, HORIZON + 1):
                tt = T + (h - 1) * GRAN
                idx = np.minimum(np.searchsorted(oT, tt), len(oT) - 1)
                use = (oT[idx] == tt) & (tt <= cutoff_ts)
                if use.sum() < 1500:
                    H = None
                    break
                o = oY[idx[use]]
                H.append(student.fit(Xa[use], student.outcome_targets(o[:, 0], o[:, 1], o[:, 2], Sa[use]), student.RIDGE_H))
            H = None if H is None else rnd(np.array(H))
        # reversal agent: linear copy of its teacher (same refit rhythm as the heads above)
        if self.simulate_publish and prev is not None and prev.get("R") is not None and eff % 1800 != 0:
            R = prev["R"]
        else:
            Xr = self.rP.view()[ok][-STUDENT_ROWS:].reshape(-1, self.rP.a.shape[-1])
            Yr = self.rL.view()[ok][-STUDENT_ROWS:].reshape(-1, REV_H + 1)
            fin = np.isfinite(Yr).all(1)
            R = rnd(student.fit(Xr[fin], Yr[fin])) if fin.sum() >= 2000 else None
        self.versions.append({
            "eff": int(eff), "W": W, "H": H, "R": R, "rt": float(f"{self.rev.thr:.4g}"),
            "scale": [[float(x) for x in t.scales()] for t in self.tuners_h],
            "cone": [float(f"{c:.6g}") for c in self.cone],
            "n": int(len(X)), "r2": [round(float(x), 3) for x in r2]})
        self.versions = self.versions[-60:]
        return self.versions[-1]

    def merge_versions(self, published):
        """published: versions as stored on the state branch (the source of
        truth: a restored engine may be older than the last run)."""
        have = {v["eff"] for v in self.versions}
        for v in published:
            if v["eff"] not in have:
                self.versions.append({"eff": int(v["eff"]), "W": np.array(v["W"], float),
                                      "H": None if v.get("H") is None else np.array(v["H"], float),
                                      "R": None if v.get("R") is None else np.array(v["R"], float),
                                      "rt": v.get("rt"),
                                      "scale": v.get("scale"), "cone": v.get("cone"), "n": 0, "r2": []})
        self.versions = sorted(self.versions, key=lambda v: v["eff"])[-60:]

    def version_at(self, ts):
        best = None
        for v in self.versions:
            if v["eff"] <= ts and (best is None or v["eff"] > best["eff"]):
                best = v
        return best

    # ------------------------------------------------------------------
    def process(self, ts, o, h, l, c, v, feat, gk):
        """One closed candle. feat: full feature vector (may contain NaN in
        warm-up). Returns a log row (dict) if a pending forecast was scored."""
        row = None
        pc = self.prev_close
        self.prev_close = c
        self.last_ts = int(ts)
        self.candles.add([o, h, l, c, v])
        if pc is None:
            return None
        r = float(np.log(c / pc))
        ao, ah, al = float(np.log(o / pc)), float(np.log(h / pc)), float(np.log(l / pc))
        self.cum += r
        self.oT.add(int(ts))
        self.oY.add([r, max(ah, 0.0), max(-al, 0.0)])
        nxt = int(ts) + GRAN
        minute, hour = (nxt // 60) % 60, (nxt // 3600) % 24
        cal = (float(np.sin(2 * np.pi * hour / 24)), float(np.cos(2 * np.pi * hour / 24)),
               1.0 if minute == 0 else 0.0, 1.0 if minute % 15 == 0 else 0.0)
        bar = {"gk": float(gk), "cal_next": cal,
               "up": max(ah, 0.0), "dn": max(-al, 0.0)}     # how far above / below the last close it reached

        # 1) score what was forecast for this candle
        P = self.pending
        if P is not None and P["ens"] is not None:
            losses = {n: float(pinball(q, r).mean()) for n, q in P["exp_q"].items()}
            row = {"ts": int(ts), "y": r, "ao": ao, "ah": ah, "al": al, "sigma": P["sigma"], "p_up": P["p_up"],
                   "loss_ens": float(pinball(P["ens"], r).mean()), "loss_cal": float(pinball(P["cal"], r).mean()),
                   "cp_prob": P["cp_prob"]}
            for i, t in enumerate(QUANTILES):
                row[f"cal_{int(round(t * 100)):02d}"] = float(P["cal"][i])
            for n in self.names:
                row[f"loss_{n}"] = losses.get(n, np.nan)
            tg, g = P["teacher_gen"], P["gen"]
            row.update({"t_b": tg[0], "t_u": tg[1], "t_d": tg[2]} if tg else {"t_b": np.nan, "t_u": np.nan, "t_d": np.nan})
            if g:
                row.update({"g_b": g["b"], "g_u": g["u"], "g_d": g["d"], "g_p": g["p"], "g_05": g["q05"],
                            "g_25": g["q25"], "g_75": g["q75"], "g_95": g["q95"], "g_eff": g["eff"]})
            else:
                row.update({k: np.nan for k in ("g_b", "g_u", "g_d", "g_p", "g_05", "g_25", "g_75", "g_95")})
                row["g_eff"] = 0
            self.hedge.update(losses)
            self.calib.update(P["cal"], r)
            if P["base"] is not None:
                self.tuner.update(P["base"], ao, r, ah, al)
            # candles that were generated 2..HORIZON minutes before this one
            ahead = self.multi.pop(int(ts), {})
            for hz in range(2, HORIZON + 1):
                e = ahead.get(hz)
                if e is None:
                    row.update({f"g{hz}_b": np.nan, f"g{hz}_u": np.nan, f"g{hz}_d": np.nan, f"c{hz}_in": np.nan})
                    if hz == HORIZON:
                        row["g5_o"] = np.nan
                    continue
                if hz == HORIZON:
                    row["g5_o"] = e["o"]            # where that candle opens, relative to the close it was made from
                inside = e["lo"] <= self.cum - e["cum0"] <= e["hi"]
                row.update({f"g{hz}_b": e["b"], f"g{hz}_u": e["u"], f"g{hz}_d": e["d"], f"c{hz}_in": float(inside)})
                # feedback: the goal tuner and the cone width of that horizon learn from the result
                self.tuners_h[hz - 2].update(e["base"], ao, r, ah, al)
                self.cone[hz - 2] *= float(np.exp(0.02 * ((not inside) - 0.10)))
        for k in [k for k in self.multi if k <= int(ts)]:
            del self.multi[k]
        if P is not None and P["x"] is not None and P["sigma"]:
            self.X.add(P["x"])
            self.z.add(np.clip(r / P["sigma"], -10, 10))

        # 2) every agent learns from the realised candle
        for e in self.agents + self.shapers:
            e.observe(r, bar, P)
        self.r_hist.add(r)
        if self.var_fast is None:
            if len(self.r_hist) >= 60:
                self.var_fast = self.var_slow = max(float(np.mean(self.r_hist.view() ** 2)), 1e-14)
        else:
            self.var_fast = max(0.98 * self.var_fast + 0.02 * r * r, 1e-14)
            self.var_slow = max(0.999 * self.var_slow + 0.001 * r * r, 1e-14)
        if self.var_slow is not None:
            self.bocpd.update(r * BP, self.var_slow * BP * BP)
        self.n += 1

        # 3) periodic refit
        if self.n % RETRAIN_EVERY == 0:
            self._retrain(ts)

        # 4) forecast the next candle
        sigma = None if self.var_fast is None else float(np.sqrt(self.var_fast))
        x = None
        cp, er = float("nan"), float("nan")
        if self.bocpd.n > 0:
            cp, er = self.bocpd.cp_prob(), self.bocpd.expected_run()
        if sigma and feat is not None and np.all(np.isfinite(feat)) and self.bocpd.n > 0:
            lsd = float(np.log(self.bocpd.predictive_sd() / BP / sigma + 1e-12))
            x = np.concatenate([feat, [cp, np.log1p(er), np.clip(lsd, -3, 3)]])
        ctx = {"x": x, "sigma": sigma, "bocpd": self.bocpd, "bocpd_scale": BP, "signals": {}}
        for s in self.signals:
            ctx["signals"].update(s.signals(ctx) or {})
        exp_q = {}
        for e in self.agents:
            q = e.predict(ctx)
            if q is not None and np.all(np.isfinite(q)):
                exp_q[e.name] = np.asarray(q, float)
        # reversal agent: learn from the swing label that just became known, then look ahead
        f = sig = phi_t = phi_b = rev_teacher = None
        if len(self.candles) == STUDENT_WIN + 1:
            cv = self.candles.view()
            f, sig = student.compact(cv, nxt)
            phi_t, phi_b = student.rev_features(cv, f, sig, 1), student.rev_features(cv, f, sig, -1)
        self.rev.observe(h, l, phi_t, phi_b)
        self.rev.settle(int(ts), GRAN)
        if phi_t is not None:
            rev_teacher = self.rev.predict(phi_t, phi_b)

        P = {"x": x, "sigma": sigma, "exp_q": exp_q, "w": {}, "ens": None, "cal": None, "p_up": float("nan"),
             "cp_prob": cp, "exp_run": er, "for_ts": nxt, "teacher_gen": None, "gen": None, "base": None, "path": None}
        if exp_q and sigma:
            w = self.hedge.weights(list(exp_q))
            ens = np.sort(sum(w[n] * exp_q[n] for n in exp_q))
            cal = self.calib.apply(ens, sigma)
            P.update(w=w, ens=ens, cal=cal, p_up=p_up(cal, 0.02 * sigma))
            ext = self.shapers[0].predict(ctx)          # reach above / below the last close
            if ext is not None and f is not None:
                P["base"] = (1.0 if P["p_up"] >= 0.5 else -1.0, median_abs(cal), float(ext[0]), float(ext[1]))
                kb, kr = self.tuner.scales()
                P["teacher_gen"] = self.tuner.candle(P["base"], kb, kr)
                a, e_up, e_dn = P["base"][1] * kb, P["base"][2] * kr, P["base"][3] * kr
                # --- student: what the site can compute by itself -------------
                self.sX.add(f)
                self.sY.add(student.teacher_targets(P["p_up"], a, e_up, e_dn, cal[0], cal[2], cal[6], cal[8], sig))
                self.sT.add(nxt)
                self.sS.add(sig)
                self.rP.add(np.vstack([phi_t, phi_b]))
                pt = np.clip(rev_teacher, 1e-3, 1 - 1e-3)
                self.rL.add(np.log(pt / (1 - pt)) if self.rev.ready() else np.nan)
                if self.simulate_publish and nxt % STUDENT_STEP == 0:
                    self.fit_student(nxt, nxt - STUDENT_LEAD)
                ver = self.version_at(nxt)
                if ver is not None:
                    path = student.generate_path(ver, f, sig)
                    P["gen"] = dict(path[0], eff=ver["eff"])
                    for j, g in enumerate(path[1:]):
                        base = student.horizon_raw(ver["H"][j], f, sig)[:4]
                        self.multi.setdefault(nxt + (j + 1) * GRAN, {})[j + 2] = dict(
                            b=g["b"], u=g["u"], d=g["d"], o=g["o"], lo=g["lo"], hi=g["hi"], base=base, cum0=self.cum)
                    P["path"] = path
                    if ver.get("R") is not None:       # official reversal calls, from the published copy
                        probs = np.vstack([student.rev_probs(ver["R"], phi_t), student.rev_probs(ver["R"], phi_b)])
                        self.rev.call(int(ts), GRAN, probs, ver["rt"], ver["eff"])
        self.pending = P
        return row
