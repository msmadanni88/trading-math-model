import gzip
import json
import os
import pickle

import numpy as np
import pandas as pd

from probcast import goal, store, student
from probcast.agents.base import Ring
from probcast.config import BUF, GRAN, STUDENT_WIN
from probcast.core import BOCPD, QUANTILES, VolHMM, garch_fit, normal_mixture_quantiles, pinball
from probcast.engine import Engine, Hedge, QuantileTracker, median_abs, p_up
from probcast.features import compute_features, feature_names, regularize
from probcast.run import run_engine


def synth(n=3000, seed=1):
    rng = np.random.default_rng(seed)
    vol = 0.0006 * np.exp(0.5 * np.sin(np.arange(n) / 150))
    r = rng.standard_t(4, n) * vol / np.sqrt(2)
    c = np.round(2000 * np.exp(np.cumsum(r)), 2)
    o = np.r_[c[0], c[:-1]]
    h = np.round(np.maximum(o, c) * (1 + np.abs(rng.normal(0, 0.0002, n))), 2)
    l = np.round(np.minimum(o, c) * (1 - np.abs(rng.normal(0, 0.0002, n))), 2)
    v = rng.lognormal(3, 1, n)
    return [[1_600_000_020 + i * GRAN, o[i], h[i], l[i], c[i], v[i]] for i in range(n)]


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
    cols = [c for c in a.columns if c.startswith(("cal_", "g", "t_", "c"))] + ["p_up"]
    assert a["g_b"].notna().sum() > 300
    assert a["g5_b"].notna().sum() > 300 and a["c5_in"].notna().sum() > 300     # candles 2..5 ahead exist
    assert np.allclose(a[cols].to_numpy(), b[cols].to_numpy(), rtol=1e-5, atol=1e-9, equal_nan=True)


def test_forecast_never_uses_its_own_outcome():
    """Everything stored for candle t must be identical whatever candle t is."""
    rows = synth(4300, seed=4)
    alt = [list(r) for r in rows]
    alt[-1][1:5] = [x * 1.003 for x in alt[-1][1:5]]         # change only the last candle
    outs = []
    for rr in (rows, alt):
        fc = run_engine(Engine(), regularize(rr), 0)
        outs.append(fc[-1])
    assert outs[0]["ts"] == outs[1]["ts"] and outs[0]["y"] != outs[1]["y"]
    assert np.isfinite(outs[0]["g_b"])
    assert np.isfinite(outs[0]["g3_b"])
    for k in outs[0]:
        if k.startswith(("cal_", "g", "t_")) or k in ("p_up", "sigma"):       # includes g2_..g5_
            assert outs[0][k] == outs[1][k], k


def test_live_generator_only_uses_published_versions():
    """A version may be used only from its effective time on, and it is fitted
    on data that ended STUDENT_LEAD seconds earlier."""
    from probcast.config import STUDENT_LEAD
    e = Engine()
    fc = pd.DataFrame(run_engine(e, regularize(synth(2400, seed=6)), 0))
    g = fc[fc["g_b"].notna()]
    assert len(g) > 200 and (g["g_eff"] <= g["ts"]).all()
    for v in e.versions:
        assert v["eff"] % 300 == 0
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
    rng = np.random.default_rng(12)
    raw = synth(700, seed=13)
    del raw[500:503]                                   # a gap the browser must fill the same way
    df = regularize(raw)
    C = df[["open", "high", "low", "close", "volume"]].to_numpy()
    W = rng.normal(size=(len(student.OUTPUTS), len(student.FEATURES))) * 0.2
    H = rng.normal(size=(4, len(student.H_OUTPUTS), len(student.FEATURES))) * 0.1
    ver = {"W": W, "H": H, "scale": [[1.1, 1.4], [1.0, 1.3], [0.9, 1.2], [1.2, 1.6]], "cone": [1.4, 1.7, 2.0, 2.3]}
    cases = []
    for end in (300, 455, 640, len(df) - 1):
        nts = int(df["ts"].iloc[end]) + GRAN
        f, sig = student.compact(C[end - STUDENT_WIN:end + 1], nts)
        cases.append({"last_ts": int(df["ts"].iloc[end]), "f": f.tolist(), "sig": sig,
                      "gen": student.generate(W, f, sig), "path": student.generate_path(ver, f, sig)})
    sc = goal.candle_score(0.0011, 0.0004, 0.0002, 0.0001, -0.0007, 0.0009, -0.0012)
    out = {"raw": raw, "n_regular": len(df), "W": W.tolist(), "cases": cases,
           "ver": {"W": W.tolist(), "H": H.tolist(), "scale": ver["scale"], "cone": ver["cone"]},
           "score": [float(x) for x in sc]}
    path = os.environ.get("PARITY_FIXTURE", str(tmp_path / "parity.json"))
    with open(path, "w") as fh:
        json.dump(out, fh)


def test_restoring_an_older_engine_gives_the_same_record():
    """In the cloud the fitted engine is saved only every ~30 minutes. A run
    that starts from an older copy must reproduce exactly what the runs in
    between stored, including which live-generator version each minute used."""
    import copy
    df = regularize(synth(2300, seed=21))
    eng = Engine()
    run_engine(eng, df.iloc[:2000], 0)
    eng.simulate_publish = False
    rows, snap, snap_at, published = [], None, None, []
    for k in range(2000, 2300, 5):                      # one "cloud run" every 5 candles
        if k == 2265:                                  # 7 runs before the end
            snap, snap_at = copy.deepcopy(eng), len(rows)
        rows += run_engine(eng, df.iloc[:k + 5], k)
        now = int(df["ts"].iloc[k + 4]) + GRAN
        v = eng.fit_student(-(-(now + 420) // 300) * 300, np.iinfo(np.int64).max)
        if v:
            published.append({"eff": v["eff"], "W": json.loads(json.dumps(v["W"].tolist()))})
    assert len(published) > 10
    snap.merge_versions(published[-12:])                # what params.json on the state branch holds
    again = run_engine(snap, df, 2265)
    a, b = pd.DataFrame(rows[snap_at:]), pd.DataFrame(again)
    assert len(a) == len(b) == 35
    cols = [c for c in a.columns if c.startswith(("cal_", "g_", "t_"))] + ["p_up"]
    assert a["g_eff"].nunique() > 3
    assert (a["g_eff"] == b["g_eff"]).all()             # same version used for every minute
    # features come from differently sized tails -> last-digit float noise only
    d = np.abs(a[cols].to_numpy() - b[cols].to_numpy()) / (np.abs(a[cols].to_numpy()) + 1e-12)
    assert np.nanmax(d) < 1e-6, np.nanmax(d)
