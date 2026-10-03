import gzip
import json
import os
import pickle

import numpy as np
import pandas as pd

from probcast import goal, store, student
from probcast.agents.base import Ring
from probcast.config import BUF, GRAN, HORIZON, REV_HS, REV_KS, STUDENT_WIN
from probcast.core import BOCPD, QUANTILES, VolHMM, garch_fit, normal_mixture_quantiles, pinball
from probcast.engine import Engine, Hedge, QuantileTracker, median_abs, p_up
from probcast.features import compute_features, feature_names, regularize
from probcast.run import run_engine


T0 = 1_600_000_020


def synth(n=3000, seed=1, t0=T0):
    rng = np.random.default_rng(seed)
    vol = 0.0006 * np.exp(0.5 * np.sin(np.arange(n) / 150))
    r = rng.standard_t(4, n) * vol / np.sqrt(2)
    c = np.round(2000 * np.exp(np.cumsum(r)), 2)
    o = np.r_[c[0], c[:-1]]
    h = np.round(np.maximum(o, c) * (1 + np.abs(rng.normal(0, 0.0002, n))), 2)
    l = np.round(np.minimum(o, c) * (1 - np.abs(rng.normal(0, 0.0002, n))), 2)
    v = rng.lognormal(3, 1, n)
    return [[t0 + i * GRAN, o[i], h[i], l[i], c[i], v[i]] for i in range(n)]


def test_features_have_no_lookahead_and_finite_memory():
    df = regularize(synth(3200))
    full = compute_features(df)[feature_names()].to_numpy()
    for t in (1500, 2377, 3199):
        # only candles <= t, and only the last BUF of them
        part = compute_features(df.iloc[t - BUF + 1:t + 1].reset_index(drop=True))[feature_names()].to_numpy()
        assert np.allclose(part[-1], full[t], rtol=1e-6, atol=1e-7), t
    df2 = df.copy()
    df2.loc[2500:, ["open", "high", "low", "close"]] *= 1.5
    part = compute_features(df2)[feature_names()].to_numpy()
    assert np.allclose(part[:2500], full[:2500], rtol=1e-9, atol=1e-10, equal_nan=True)


def test_regularize_fills_gaps():
    rows = synth(100)
    del rows[40:43]
    df = regularize(rows)
    assert len(df) == 100 and df["filled"].sum() == 3
    assert (df["volume"][df["filled"] == 1] == 0).all()
    assert df["close"].iloc[41] == df["close"].iloc[39]


def test_ring_quantiles_match_numpy():
    r = Ring(500)
    x = np.random.default_rng(0).normal(size=1234)
    for v in x:
        r.add(v)
    assert np.allclose(r.quantiles(), np.quantile(x[-500:], QUANTILES))
    assert np.allclose(r.values(), x[-500:])


def test_pinball_minimised_at_true_quantile():
    y = np.random.default_rng(0).normal(size=20000)
    tq = np.quantile(y, QUANTILES)
    base = pinball(tq[None, :], y[:, None]).mean(0)
    for shift in (-0.2, 0.2):
        assert (pinball(tq[None, :] + shift, y[:, None]).mean(0) > base).all()


def test_normal_mixture_quantiles():
    q = normal_mixture_quantiles(np.array([1.0]), np.array([2.0]))
    assert np.allclose(q, 2.0 * np.array([-1.6449, -1.2816, -0.6745, -0.2533, 0, 0.2533, 0.6745, 1.2816, 1.6449]), atol=5e-3)


def test_bocpd_detects_variance_shift_and_is_calibrated():
    rng = np.random.default_rng(3)
    x = np.r_[rng.normal(0, 1, 600), rng.normal(0, 4, 300)]
    b = BOCPD()
    hits, cps = [], []
    for i, v in enumerate(x):
        if i > 100:
            hits.append(v <= b.predictive_quantiles())
        b.update(v, 1.0)
        cps.append(b.expected_run())
    assert cps[595] > 200 and min(cps[600:640]) < 40
    assert np.all(np.abs(np.mean(hits[:450], axis=0) - QUANTILES) < 0.06)
    assert abs(b.p.sum() - 1) < 1e-9


def test_hmm_recovers_two_volatility_states():
    rng = np.random.default_rng(5)
    st = (np.arange(4000) // 500) % 2
    x = rng.normal(0, np.where(st == 0, 0.5, 2.0))
    m = VolHMM(2).fit(x)
    assert abs(m.sd[0] - 0.5) < 0.08 and abs(m.sd[1] - 2.0) < 0.25
    assert m.alpha[1] > 0.9
    assert np.allclose(m.A.sum(1), 1)


def test_garch_fit_recovers_persistence():
    rng = np.random.default_rng(7)
    w, a, b = 0.05, 0.10, 0.85
    h, r = 1.0, []
    for _ in range(6000):
        x = rng.normal() * np.sqrt(h)
        r.append(x)
        h = w + a * x * x + b * h
    _, ah, bh = garch_fit(np.array(r))
    assert abs(ah - a) < 0.04 and abs(bh - b) < 0.06


def test_quantile_tracker_converges_to_nominal_coverage():
    rng = np.random.default_rng(11)
    qt = QuantileTracker(gamma=0.01)
    wrong = np.quantile(rng.normal(size=100000), QUANTILES) * 0.6      # intervals 40% too narrow
    hits = []
    for _ in range(20000):
        y = rng.normal()
        q = qt.apply(wrong, 1.0)
        hits.append(y <= q)
        qt.update(q, y)
    assert np.all(np.abs(np.mean(hits[5000:], axis=0) - QUANTILES) < 0.015)


def test_hedge_prefers_the_better_agent_and_accepts_new_ones():
    hg = Hedge(["a", "b"])
    for _ in range(600):
        hg.update({"a": 1.0, "b": 1.1})
    w = hg.weights(["a", "b"])
    assert w["a"] > 0.9 and abs(sum(w.values()) - 1) < 1e-12
    w = hg.weights(["a", "b", "newcomer"])                 # an agent added later
    assert abs(sum(w.values()) - 1) < 1e-12 and w["newcomer"] > 0


def test_p_up_and_median_abs():
    q = np.array([-2, -1.5, -1, -0.2, 0.0, 0.2, 1, 1.5, 2.0])
    assert abs(p_up(q, 0.01) - 0.5) < 1e-9
    assert p_up(q + 0.5, 0.01) > 0.6 and p_up(q - 0.5, 0.01) < 0.4
    nq = np.array([-1.6449, -1.2816, -0.6745, -0.2533, 0.0, 0.2533, 0.6745, 1.2816, 1.6449])
    assert abs(median_abs(nq) - 0.6745) < 0.01
    flat = np.zeros(9)                                      # many unchanged closes: must not crash
    assert 0.0 <= p_up(flat, 0.01) <= 1.0


def test_candle_score():
    # identical candle -> 1
    b, r, s = goal.candle_score(0.002, 0.001, 0.0005, 0.0, 0.002, 0.003, -0.0005)
    assert abs(b - 1) < 1e-12 and abs(r - 1) < 1e-12 and abs(s - 1) < 1e-12
    # wrong colour -> body overlap 0, range overlap still partial
    b, r, s = goal.candle_score(-0.002, 0.001, 0.001, 0.0, 0.002, 0.003, -0.001)
    assert b == 0 and 0 < r < 1
    # half-size body, right colour -> body IoU 0.5
    b, _, _ = goal.candle_score(0.001, 0, 0, 0.0, 0.002, 0.002, 0.0)
    assert abs(b - 0.5) < 1e-12


def _version(rng, fmt=student.FORMAT):
    W = rng.normal(size=(len(student.OUTPUTS), len(student.FEATURES))) * 0.05
    W[4:, 0] = [-1.6, -0.67, 0.67, 1.6]                # ordered quantiles, like a fitted model has
    H = rng.normal(size=(HORIZON, len(student.H_OUTPUTS), len(student.FEATURES))) * 0.1
    ver = {"fmt": fmt, "W": W, "H": H, "scale": [[1.0, 1.0]] + [[1.0 + 0.02 * h, 1.2 + 0.03 * h] for h in range(1, HORIZON)],
           "cone": [1.0] + [float(np.sqrt(h)) for h in range(2, HORIZON + 1)], "ct": [0.04, 0.09]}
    return W, H, ver


def test_student_fit_recovers_linear_teacher_and_generates_valid_candle():
    rng = np.random.default_rng(2)
    n, d, k = 2000, len(student.FEATURES), len(student.OUTPUTS)
    X = np.c_[np.ones(n), rng.normal(size=(n, d - 1))]
    Wt = rng.normal(size=(k, d)) * 0.1
    W = student.fit(X, X @ Wt.T + rng.normal(0, 0.01, (n, k)))
    assert np.allclose(W, Wt, atol=0.02)
    rows = regularize(synth(600, seed=3))
    C = rows[["open", "high", "low", "close", "volume"]].to_numpy()[-(STUDENT_WIN + 1):]
    f, sig = student.compact(C, int(rows["ts"].iloc[-1]) + GRAN)
    assert len(f) == d and np.all(np.isfinite(f)) and sig > 0
    g = student.generate(W, f, sig)
    assert g["u"] >= 0 and g["d"] >= 0 and 0 < g["p"] < 1 and (g["b"] > 0) == (g["p"] >= 0.5)


def test_chain_of_generated_candles_is_connected_and_stays_in_its_own_range():
    """Every candle opens where the previous one closed, its colour is the
    sign of its body, wicks never point inwards, and the chain never ends a
    candle outside the model's own 50% range if the other colour avoids it."""
    rng = np.random.default_rng(5)
    df = regularize(synth(900, seed=5))
    C = df[["open", "high", "low", "close", "volume"]].to_numpy()
    flips, calls = 0, []
    for trial in range(60):
        W, H, ver = _version(rng)
        end = 300 + trial * 9
        f, sig = student.compact(C[end - STUDENT_WIN:end + 1], int(df["ts"].iloc[end]) + GRAN)
        path = student.generate_path(ver, f, sig)
        assert len(path) == HORIZON
        n = student._next_raw(W, f, sig)
        iq = 0.5 * (n["q75"] - n["q25"])
        o = 0.0
        for h, g in enumerate(path, 1):
            assert g["o"] == o and g["u"] >= 0 and g["d"] >= 0
            head_colour = 1.0 if g["p"] >= 0.5 else -1.0
            assert (np.sign(g["b"]) == head_colour) != bool(g["flip"]) or g["b"] == 0
            w = max(ver["cone"][h - 1] * iq, abs(g["b"]))
            if abs(o + g["b"]) > w:                      # outside: only allowed if the other colour is no better
                assert abs(o - g["b"]) >= abs(o + g["b"])
            assert g["lo"] <= g["hi"]
            flips += g["flip"]
            o += g["b"]
        assert path[0]["flip"] == 0 and path[0]["o"] == 0.0
        # the confident-call flag belongs to candle 1 only and follows the published threshold
        assert path[0]["call"] == sum(abs(path[0]["p"] - 0.5) >= t for t in ver["ct"]) and all("call" not in g for g in path[1:])
        calls.append(path[0]["call"])
        assert student.generate_path(dict(ver, ct=None), f, sig)[0]["call"] == 0     # no lines published yet: no calls
    assert set(calls) == {0, 1, 2}                       # every level occurred
    assert flips > 20                                    # the rule was actually exercised
    # an old-format version still gives the next candle, and only that
    W, H, ver = _version(rng, fmt=None)
    assert len(student.generate_path(ver, f, sig)) == 1


def test_packed_trees_give_the_same_probabilities_as_lightgbm():
    import lightgbm as lgb
    rng = np.random.default_rng(7)
    X = rng.normal(size=(4000, 12)).astype(np.float32)
    y = (X[:, 0] + 0.5 * X[:, 3] * X[:, 5] + rng.normal(0, 1, 4000) > 0).astype(float)
    m = lgb.train(dict(objective="binary", num_leaves=16, min_data_in_leaf=40, verbose=-1, seed=1), lgb.Dataset(X, label=y),
                  num_boost_round=60)
    packed = student.pack_trees(m.dump_model())
    Xt = rng.normal(size=(500, 12))                      # double precision in: rounded to single inside
    assert np.allclose(student.tree_probs(packed, Xt), m.predict(Xt.astype(np.float32)), rtol=0, atol=5e-4)     # rounding of the published numbers
    again = json.loads(json.dumps({k: v for k, v in packed.items() if k != "_np"}))     # as the site receives it
    assert np.array_equal(student.tree_probs(again, Xt), student.tree_probs(packed, Xt))


RECORD = ("cal_", "g_", "t_", "lk_", "s", "d", "c") + tuple(f"r{K}_" for K in REV_KS)


def test_engine_resume_equals_single_run(tmp_path):
    """Incremental running must give the same forecasts as one pass."""
    df = regularize(synth(4600, seed=9))
    e1 = Engine()
    a = pd.DataFrame(run_engine(e1, df, 0))
    e2 = Engine()
    rows = run_engine(e2, df.iloc[:4000], 0)
    p = tmp_path / "s.pkl.gz"
    with gzip.open(p, "wb") as f:
        pickle.dump(e2, f)
    with gzip.open(p, "rb") as f:
        e3 = pickle.load(f)
    for k in range(4000, 4600, 7):                 # arrive in small batches
        rows += run_engine(e3, df.iloc[:min(k + 7, 4600)], k)
    b = pd.DataFrame(rows)
    assert len(a) == len(b) and (a["ts"] == b["ts"]).all()
    cols = [c for c in a.columns if c.startswith(RECORD)] + ["p_up"]
    assert a["g_b"].notna().sum() > 300
    last = f"s{HORIZON}"
    assert a[last].notna().sum() > 300 and a[f"c{HORIZON}_in"].notna().sum() > 300      # the whole chain is scored
    assert a["lk_o"].notna().sum() > 300
    assert np.allclose(a[cols].to_numpy(float), b[cols].to_numpy(float), rtol=1e-5, atol=1e-9, equal_nan=True)


def test_forecast_never_uses_its_own_outcome():
    """Everything generated for candle t must be identical whatever candle t is."""
    rows = synth(4300, seed=4)
    alt = [list(r) for r in rows]
    alt[-1][1:5] = [x * 1.003 for x in alt[-1][1:5]]         # change only the last candle
    outs = []
    for rr in (rows, alt):
        fc = run_engine(Engine(), regularize(rr), 0)
        outs.append(fc[-1])
    assert outs[0]["ts"] == outs[1]["ts"] and outs[0]["y"] != outs[1]["y"]
    assert np.isfinite(outs[0]["g_b"]) and np.isfinite(outs[0]["lk_b"])
    for k in outs[0]:
        if k.startswith(("cal_", "g_", "t_")) or k in ("p_up", "sigma", "lk_h", "lk_o", "lk_b", "lk_u", "lk_d"):
            assert outs[0][k] == outs[1][k], k


def test_fixed_record_is_the_chain_frozen_at_the_start_of_each_quarter_hour():
    """Rows of one frozen chain: candle numbers 1..HORIZON aligned to the
    clock, candle 1 opens at the last real close and is the candle generated
    for that minute, and every later candle opens where the previous one closed."""
    fc = pd.DataFrame(run_engine(Engine(), regularize(synth(4500, seed=41)), 0))
    x = fc[fc["lk_o"].notna()]
    seg = HORIZON * GRAN
    assert len(x) > 600
    assert ((x["ts"] % seg) // GRAN + 1 == x["lk_h"]).all()
    first = x[x["lk_h"] == 1]
    assert (first["lk_o"] == 0).all()
    assert np.array_equal(first["lk_b"].to_numpy(), first["g_b"].to_numpy())
    assert np.array_equal(first["lk_r"].to_numpy(), np.zeros(len(first)))
    by = x.set_index("ts")
    n = 0
    for ts, r in by.iterrows():
        if r["lk_h"] > 1 and ts - GRAN in by.index:
            prev = by.loc[ts - GRAN]
            assert abs(r["lk_o"] - (prev["lk_o"] + prev["lk_b"])) < 1e-15
            # where the market really stood: one more real candle than the row before
            assert abs(r["lk_r"] - (prev["lk_r"] + fc.set_index("ts").loc[ts - GRAN, "y"])) < 1e-12
            n += 1
    assert n > 500


def test_live_generator_only_uses_published_versions():
    """A version may be used only from its effective time on, and it is fitted
    on data that ended STUDENT_LEAD seconds earlier."""
    e = Engine()
    fc = pd.DataFrame(run_engine(e, regularize(synth(2400, seed=6)), 0))
    g = fc[fc["g_b"].notna()]
    assert len(g) > 200 and (g["g_eff"] <= g["ts"]).all()
    for v in e.versions:
        assert v["eff"] % 300 == 0 and v["fmt"] == student.FORMAT
    assert e.version_at(e.versions[0]["eff"] - 1) is None


def test_store_roundtrip(tmp_path):
    rows = synth(3000, seed=8)
    store.write_candles(str(tmp_path), rows)
    back = store.read_candles(str(tmp_path))
    assert back == [[int(r[0])] + [float(x) for x in r[1:]] for r in rows]
    assert len(os.listdir(tmp_path / "candles")) >= 2
    assert store.read_candles(str(tmp_path), rows[-1][0])[-1] == back[-1]


def test_write_js_parity_fixture(tmp_path):
    """Writes the fixture that tests/parity.mjs checks docs/student.js against."""
    import lightgbm as lgb
    rng = np.random.default_rng(12)
    raw = synth(700, seed=13)
    del raw[500:503]                                   # a gap the browser must fill the same way
    df = regularize(raw)
    C = df[["open", "high", "low", "close", "volume"]].to_numpy()
    W, H, ver = _version(rng)
    nf = len(student.REV_FEATURES) + 1
    Xm = rng.normal(size=(3000, nf)).astype(np.float32) * 3
    Xm[:, -1] = rng.choice(REV_HS, 3000)
    ym = (Xm[:, 21] - Xm[:, 27] + rng.normal(0, 2, 3000) > 0).astype(float)
    model = student.pack_trees(lgb.train(dict(objective="binary", num_leaves=12, min_data_in_leaf=30, verbose=-1, seed=3),
                                         lgb.Dataset(Xm, label=ym), num_boost_round=40).dump_model())
    hi, lo = df["high"].to_numpy(), df["low"].to_numpy()
    swings = [[int(i), int(K), bool(hi[i] >= hi[i - K:i + K + 1].max()), bool(lo[i] <= lo[i - K:i + K + 1].min())]
              for i in (100, 257, 333, 480, 612) for K in REV_KS]
    cases = []
    keys = ("p", "b", "u", "d", "o", "lo", "hi", "flip", "call")
    for end in (300, 455, 640, len(df) - 1):
        nts = int(df["ts"].iloc[end]) + GRAN
        Cw = C[end - STUDENT_WIN:end + 1]
        f, sig = student.compact(Cw, nts)
        rev = {}
        for K in REV_KS:
            phis = [student.rev_features(Cw, f, sig, sd, K) for sd in (1, -1)]
            pr = student.tree_probs(model, student.rev_rows(phis[0], phis[1], REV_HS)).reshape(2, len(REV_HS))
            rev[str(K)] = {"phi": [x.tolist() for x in phis], "probs": pr.tolist()}
        cases.append({"last_ts": int(df["ts"].iloc[end]), "f": f.tolist(), "sig": sig,
                      "gen": student.generate(W, f, sig),
                      "path": [{k: g[k] for k in keys if k in g} for g in student.generate_path(ver, f, sig)], "rev": rev})
    sc = goal.candle_score(0.0011, 0.0004, 0.0002, 0.0001, -0.0007, 0.0009, -0.0012)
    out = {"raw": raw, "n_regular": len(df), "W": W.tolist(), "cases": cases, "horizon": HORIZON,
           "ver": {"fmt": ver["fmt"], "W": W.tolist(), "H": H.tolist(), "scale": ver["scale"], "cone": ver["cone"], "ct": ver["ct"]},
           "conf": [[float(p), [float(ct), float(2 * ct)], int(student.call_level({"ct": [ct, 2 * ct]}, p))]
                    for ct in (0.02, 0.0317, 0.05)
                    for p in np.r_[np.linspace(0.38, 0.62, 97), 0.5 + ct, 0.5 - ct, 0.5 + ct - 4e-7, 0.5 - ct + 6e-7, 0.5 + 2 * ct, 0.5 - 2 * ct + 6e-7]],
           "model": {k: v for k, v in model.items() if k != "_np"}, "hs": list(REV_HS), "swings": swings,
           "score": [float(x) for x in sc]}
    path = os.environ.get("PARITY_FIXTURE", str(tmp_path / "parity.json"))
    with open(path, "w") as fh:
        json.dump(out, fh)


def _small_reversal(monkeypatch):
    """Lets the reversal agents get a tree model within a few thousand candles."""
    from probcast import engine
    from probcast.agents import reversal
    monkeypatch.setattr(reversal, "LGBM_HOLDOUT", 300)
    monkeypatch.setattr(reversal, "LGBM_EMBARGO", 10)
    monkeypatch.setattr(reversal, "CONTEST", [dict(rows=4000, rounds=40, min_data_in_leaf=60)] * 2)
    monkeypatch.setattr(reversal, "REV_MIN_PER_DAY", 20)
    monkeypatch.setattr(engine, "LGBM_EVERY", 720)
    return reversal


def test_restoring_an_older_engine_gives_the_same_record(monkeypatch):
    """In the cloud the fitted engine is saved only every ~30 minutes. A run
    that starts from an older copy must reproduce exactly what the runs in
    between stored, including which live-generator version each minute used."""
    import copy
    _small_reversal(monkeypatch)
    df = regularize(synth(3300, seed=21))
    eng = Engine()
    run_engine(eng, df.iloc[:3000], 0)
    eng.simulate_publish = False
    rows, snap, snap_at, published = [], None, None, []
    for k in range(3000, 3300, 5):                      # one "cloud run" every 5 candles
        if k == 3265:                                  # 7 runs before the end
            snap, snap_at = copy.deepcopy(eng), len(rows)
        rows += run_engine(eng, df.iloc[:k + 5], k)
        now = int(df["ts"].iloc[k + 4]) + GRAN
        v = eng.fit_student(-(-(now + 420) // 300) * 300, np.iinfo(np.int64).max)
        if v:                                          # exactly what report.publish writes to versions.json
            published.append(json.loads(json.dumps({"eff": v["eff"], "fmt": v["fmt"], "W": v["W"].tolist(), "H": v["H"].tolist(),
                                                    "scale": v["scale"], "cone": v["cone"], "rm": v["rm"], "rt": v["rt"], "ct": v["ct"]})))
    assert len(published) > 10
    snap.merge_versions(published[-14:])                # what versions.json on the state branch holds
    again = run_engine(snap, df, 3265)
    a, b = pd.DataFrame(rows[snap_at:]), pd.DataFrame(again)
    assert len(a) == len(b) == 35
    cols = [c for c in a.columns if c.startswith(RECORD)] + ["p_up"]
    assert a["g_eff"].nunique() > 3
    assert (a["g_eff"] == b["g_eff"]).all()             # same version used for every minute
    assert a["r5_tn"].notna().all()                     # the reversal model spoke on every one of them
    # features come from differently sized tails -> last-digit float noise only
    x, y = a[cols].to_numpy(float), b[cols].to_numpy(float)
    d = np.abs(x - y) / (np.abs(x) + 1e-12)
    assert np.nanmax(d) < 1e-6, np.nanmax(d)
    assert np.array_equal(np.isnan(x), np.isnan(y))


def test_reversal_agents_labels_learning_and_calls(monkeypatch):
    reversal = _small_reversal(monkeypatch)
    df = regularize(synth(6400, seed=31))
    e = Engine()
    fc = pd.DataFrame(run_engine(e, df, 0))
    hi, lo = df["high"].to_numpy(), df["low"].to_numpy()
    ts = df["ts"].to_numpy()
    pos = {int(t): k for k, t in enumerate(ts)}
    n = len(df)
    total = 0
    for K, rv in e.rev.items():
        # the label ring holds the true swing status of the candles that are K back
        for back in range(0, 3):
            i = n - 1 - K - back
            want = [float(hi[i] >= hi[i - K:i + K + 1].max()), float(lo[i] <= lo[i - K:i + K + 1].min())]
            assert list(rv.lab.back(back)) == want
        assert rv.n_fit > 5000 and rv.model_id > 0 and rv.model_id in rv.models
        news = [x[1] for x in rv.events if x[0] == "new"]
        hits = [x[1] for x in rv.events if x[0] == "hit"]
        total += len(news)
        for c in news:               # "now" names the candle that just closed, "next" the one two minutes on
            assert c["k"] == K and c["for_ts"] == c["made_ts"] - GRAN + REV_HS[c["typ"]] * GRAN
            row = fc[fc["ts"] == c["made_ts"] - GRAN].iloc[0]          # the stored probability is the one acted on
            col = f"r{K}_{'t' if c['side'] > 0 else 'b'}{'n' if c['typ'] == 0 else 'x'}"
            assert abs(row[col] - c["p"]) < 6e-4
        # every outcome matches the definition: a swing of that side within one candle
        for for_ts, k_, side, typ, hit in hits:
            k = pos[for_ts]
            ext = hi if side > 0 else -lo
            want = any(ext[m] >= ext[m - K:m + K + 1].max() for m in (k - 1, k, k + 1))
            assert k_ == K and hit == int(want)
        # no two calls of the same side and type within two minutes of each other
        seen = {(c["for_ts"], c["side"], c["typ"]) for c in news}
        assert not any((t + d * GRAN, s, a) in seen for t, s, a in seen for d in (1, 2))
        # the history the thresholds are tuned on is aligned: outcome of origin t, type a = label of candle t + horizon
        P, Y = rv.history()
        ok = np.nonzero(np.isfinite(Y[:, 0, 0]))[0]
        assert len(ok) > 3000
        base = n - len(P)                              # history row i is candle base + i
        for i in ok[-40:]:
            for a, j in enumerate(REV_HS):
                m = base + i + j
                assert Y[i, 0, a] == float(any(hi[q] >= hi[q - K:q + K + 1].max() for q in (m - 1, m, m + 1)))
    assert total > 30
    # thresholds were re-picked from the agents' own history
    assert any(rv.tuned for rv in e.rev.values())
    assert reversal.spaced([1, 2, 3, 4, 7, 8, 20]) == [1, 4, 7, 20]
    assert 0.0 < reversal.wilson_low(8, 10) < reversal.wilson_low(800, 1000) < 0.8      # more calls, less doubt


def test_stored_calls_are_never_rewritten_and_record_columns_are_protected(tmp_path):
    sd = str(tmp_path)
    c1 = {"made_ts": 1000, "for_ts": 1060, "k": 5, "side": 1, "typ": 0, "p": 0.4, "level": 2000.0, "model": 900}
    store.merge_calls(sd, [("new", c1)])
    store.merge_calls(sd, [("new", dict(c1, p=0.9, level=1.0)), ("hit", (1060, 5, 1, 0, 1))])  # same call again
    store.merge_calls(sd, [("hit", (1060, 5, 1, 0, 0))])                                        # outcome again
    store.merge_calls(sd, [("new", dict(c1, k=8, p=0.7)), ("new", dict(c1, typ=1, p=0.5))])     # another agent / the other call type
    got = store.read_calls(sd).to_dict("records")
    assert len(got) == 3 and got[0]["p"] == 0.4 and got[0]["level"] == 2000.0 and got[0]["hit"] == 1
    assert (got[1]["typ"], got[1]["p"]) == (1, 0.5) and got[2]["k"] == 8 and got[2]["hit"] != got[2]["hit"]
    from probcast.run import PROTECTED
    cols = ["g_b", "g_u", "g_p", "g_95", "g_eff", "g_call", "g2_b", "g5_o", "c3_in", "c15_in", "s2", "s15", "d7", "lk_o", "lk_h", "r5_tn", "r13_bx",
            "t_b", "y", "cal_50", "cp_prob", "loss_garch", "sigma", "p_up", "ts"]
    assert [c for c in cols if PROTECTED.match(c)] == cols[:17]


def test_ledger_keeps_days_that_are_two_days_old(tmp_path):
    sd = str(tmp_path)
    mk = lambda rows: pd.DataFrame(rows, columns=store.LEDGER_COLS)
    a = store.merge_ledger(sd, mk([["2026-10-01", "x", 100, 55, 0.5, 0], ["2026-10-02", "x", 100, 60, 0.5, 1]]), "2026-10-02")
    assert len(a) == 2
    # two days later a recomputation disagrees about the 1st: the archive wins; the 3rd (yesterday) is still open
    b = store.merge_ledger(sd, mk([["2026-10-01", "x", 100, 99, 0.5, 0], ["2026-10-03", "x", 50, 30, 0.5, 1],
                                   ["2026-10-04", "x", 10, 5, 0.5, 1]]), "2026-10-04")
    got = {r["day"]: r["wins"] for r in b.to_dict("records")}
    assert got == {"2026-10-01": 55, "2026-10-02": 60, "2026-10-03": 30, "2026-10-04": 5}
    c = store.merge_ledger(sd, mk([["2026-10-03", "x", 50, 31, 0.5, 1]]), "2026-10-04")
    assert {r["day"]: r["wins"] for r in c.to_dict("records")}["2026-10-03"] == 31       # yesterday may still change


def test_full_run_writes_everything_and_a_rebuild_changes_nothing_already_stored(tmp_path, monkeypatch):
    """End to end on a state folder: one run, then the fitted engine is thrown
    away and everything is rebuilt from the candles. Whatever the first run
    stored as the models' word must still be there, value for value."""
    from probcast import config, run
    _small_reversal(monkeypatch)
    monkeypatch.setattr(run, "START", "2026-09-01")
    t0 = 1_790_000_040
    rows = synth(5200, seed=51, t0=t0)
    sd, cd = str(tmp_path / "state"), str(tmp_path / "cache")
    store.write_candles(sd, rows[:5000])
    now1 = rows[4999][0] + 70
    status, rep = run.step(sd, cd, offline=True, now=now1)
    assert status["replay"] and status["error"] is None
    live = lambda name: json.load(open(os.path.join(sd, "live", name)))
    latest, params, head = live("latest.json"), live("params.json"), live("head.json")
    assert head["generated"] == latest["generated"] == int(now1) and head["last_ts"] == rows[4999][0]
    assert len(latest["path"]["candles"]) == HORIZON and latest["horizon"] == HORIZON
    assert len(latest["locked"]) > 500 and latest["locked"][-1][0] > latest["last_ts"]          # reaches into the open chain
    assert all(v["fmt"] == student.FORMAT and len(v["H"]) == HORIZON for v in params["versions"])
    for K in REV_KS:
        used = {str(v["rm"][str(K)]) for v in params["versions"]} - {"0"}
        assert used and used <= set(live(f"rev_k{K}.json")["models"]) and used <= set(head["models"][str(K)])     # every model in use is published
        assert len(latest["rev"][str(K)]["probs"]) > 300
    assert rep["ledger"] and "colour_next" in rep["ledger"] and "overall" in rep["ledger"]
    # the colour caller has picked its line; the decision is stored with every generated candle and published
    assert len(rep["colour"]["threshold"]) == 2 and params["versions"][-1]["ct"] == rep["colour"]["threshold"]
    assert latest["gen_cols"][-1] == "call" and all(len(g) == 10 for g in latest["gen"])
    assert {"colour_confident", "colour_strong", "colour_clear"} <= set(rep["ledger"])
    cn, ov = rep["ledger"]["colour_next"], rep["ledger"]["overall"]
    assert cn["all"]["ci"][0] <= cn["all"]["rate"] <= cn["all"]["ci"][1]
    pooled = sum(b["all"]["n"] for l, b in rep["ledger"].items() if l not in ("overall", "colour_confident", "colour_strong", "colour_clear") and b["all"])
    assert ov["all"]["n"] == pooled                           # selections of a layer are not pooled twice
    assert set(rep["slices"]) == {"volatility", "session"} and sum(r["n"] for r in rep["slices"]["volatility"].values()) > 3000
    meta = json.load(open(os.path.join(sd, "meta.json")))
    assert meta["live_since"] == int(now1)
    fc1 = store.read_forecasts(sd)
    called = fc1["g_call"].dropna()
    assert set(called.unique()) == {0.0, 1.0, 2.0} and (called == 0).mean() > 0.6 and (called == 1).sum() > (called == 2).sum()
    calls1 = store.read_calls(sd)
    assert len(calls1) > 20
    # two kinds of older rows in the archive, both without the confident-call decision:
    # A - the stored prediction is the one a rebuild makes again; B - it is a different one
    ix = fc1.index[fc1["g_call"].notna()]
    A, B = ix[-400:-200], ix[-200:]
    fc1.loc[A.union(B), "g_call"] = np.nan
    fc1.loc[B, "g_p"] = (fc1.loc[B, "g_p"] + 0.011).round(6)
    store.write_forecasts(sd, fc1, int(fc1["ts"].iloc[0]))
    fc1 = store.read_forecasts(sd)
    # second run: new candles arrive and the saved engine is lost -> full rebuild
    store.write_candles(sd, rows)
    os.remove(os.path.join(cd, "engine.pkl.gz"))
    status2, _ = run.step(sd, cd, offline=True, now=rows[-1][0] + 70)
    assert status2["replay"]
    fc2 = store.read_forecasts(sd)
    assert len(fc2) > len(fc1)
    a, b = fc1.set_index("ts"), fc2.set_index("ts").loc[fc1["ts"]]
    prot = [c for c in a.columns if run.PROTECTED.match(c)]
    assert len(prot) > 60
    x, y = a[prot].to_numpy(float), b[prot].to_numpy(float)
    was = ~np.isnan(x)
    assert np.array_equal(x[was], y[was])                      # nothing that was written has changed
    # the decision is filled in for the predictions it belongs to, and never attached to a different one
    assert b["g_call"].loc[fc1.loc[A, "ts"]].notna().all() and b["g_call"].loc[fc1.loc[B, "ts"]].isna().all()
    calls2 = store.read_calls(sd).set_index(["for_ts", "k", "side", "typ"])
    for r in calls1.itertuples():
        q = calls2.loc[(r.for_ts, r.k, r.side, r.typ)]
        assert q["p"] == r.p and q["made_ts"] == r.made_ts
        assert r.hit != r.hit or q["hit"] == r.hit
    assert json.load(open(os.path.join(sd, "meta.json")))["live_since"] == int(now1)      # go-live date is kept


def test_colour_caller_draws_its_lines_by_call_rate():
    """The lines are the confidences that give the set number of calls a day;
    a strong call is always also a confident one; where confidence carries an
    edge the calls beat calling every minute, and the report says by how much."""
    from probcast.agents.colour import ColourCaller
    from probcast.config import COL_PER_DAY
    rng = np.random.default_rng(4)
    n = 6 * 1440
    conf = np.abs(rng.normal(0, 0.03, n))
    for edge in (True, False):
        cc = ColourCaller()
        assert cc.tune() is None and cc.thr is None            # nothing to learn from yet
        win = rng.random(n) < (0.5 + (1.5 * conf if edge else 0.0))
        for i in range(n):
            cc.observe(T0 + i * GRAN, conf[i], win[i])
        info = cc.tune()
        assert 0 < cc.thr[0] < cc.thr[1] < 0.2
        for lv, per_day in zip(info["levels"], COL_PER_DAY):
            assert abs(lv["calls_per_day"] - per_day) < 2
            assert abs((conf >= lv["threshold"]).sum() / 6 - lv["calls_per_day"]) < 2
        if edge:
            assert info["levels"][1]["win_rate"] > info["levels"][0]["win_rate"] > info["every_minute"] + 0.02
        first = list(cc.thr)
        cc.tune()
        assert np.allclose(cc.thr, first, atol=1e-3)            # stable when nothing changed
    ver = {"ct": [0.05, 0.08]}
    assert [student.call_level(ver, p) for p in (0.5, 0.5499, 0.55, 0.45, 0.579, 0.58, 0.42, 0.98)] == [0, 0, 1, 1, 1, 2, 2, 2]
    assert student.call_level({}, 0.9) == 0 and student.call_level({"ct": None}, 0.9) == 0


def test_ledger_intervals_trend_and_today():
    """The interval comes from resampling whole days; a layer that is only a
    selection of another one is listed but not pooled twice; the trend is
    `flat` unless the change is beyond the day-to-day noise."""
    from probcast import report
    rng = np.random.default_rng(8)
    days = [f"2026-09-{d:02d}" for d in range(1, 29)]
    rows = []
    for i, d in enumerate(days):
        p = 0.52 + 0.03 * np.sin(i)                             # days differ more than coin flips would
        rows.append([d, "colour_next", 1400, int(rng.binomial(1400, p)), 0.5, int(i >= 20)])
        rows.append([d, "colour_confident", 150, int(rng.binomial(150, 0.56)), 0.5, int(i >= 20)])
        rows.append([d, "reversal_k5_now", 50, int(rng.binomial(50, 0.60 if i < 21 else 0.90)), 0.2, int(i >= 20)])
    rows.append(["2026-09-29", "colour_next", 300, 160, 0.5, 1])          # the day still running
    led = pd.DataFrame(rows, columns=store.LEDGER_COLS)
    out = report.ledger_summary(led, "2026-09-29")
    cn = out["colour_next"]
    assert cn["today"] == {"n": 300, "rate": round(160 / 300, 4)} and cn["1d"]["n"] == 1400 and cn["30d"]["n"] == 28 * 1400
    lo, hi = cn["30d"]["ci"]
    binom = 1.645 * np.sqrt(0.25 / cn["30d"]["n"])
    assert lo < cn["30d"]["rate"] < hi and (hi - lo) / 2 > 1.5 * binom       # wider than independent flips would give
    assert cn["trend"]["verdict"] == "flat"
    assert out["reversal_k5_now"]["trend"]["verdict"] == "up" and out["reversal_k5_now"]["trend"]["change"] > 0.2
    assert out["overall"]["30d"]["n"] == 28 * 1450 and out["overall"]["today"]["n"] == 300
    assert out["colour_confident"]["live"]["n"] == 8 * 150
    # only the running day exists: the layer is listed with today's numbers and nothing else
    one = report.ledger_summary(led[led["day"] == "2026-09-29"], "2026-09-29")
    assert one["colour_next"]["today"]["n"] == 300 and one["colour_next"]["7d"] is None
