// Everything the browser computes itself - mirror of probcast/student.py (see
// that file for the idea). tests/parity.mjs checks that both implementations
// return the same numbers.
(function (root) {
  const WIN = 240, LAM = 0.97, OFF = 0.01, OFF_H = 0.1, GRAN = 60, FORMAT = 2;
  const FLIP = [1, 2, 3, 4, 5, 6, 9, 14];
  const clip = (x, a) => Math.max(-a, Math.min(a, x));
  const dot = (row, f) => { let s = 0; for (let i = 0; i < row.length; i++) s += row[i] * f[i]; return s; };

  // candles: array of [ts, o, h, l, c, v] sorted by time. Fills missing minutes
  // with flat zero-volume candles, exactly like the cloud does.
  function regularize(candles) {
    const out = [];
    for (const k of candles) {
      if (out.length) {
        let prev = out[out.length - 1];
        if (k[0] <= prev[0]) continue;
        while (prev[0] + GRAN < k[0]) {
          prev = [prev[0] + GRAN, prev[4], prev[4], prev[4], prev[4], 0];
          out.push(prev);
        }
      }
      out.push(k);
    }
    return out;
  }

  // C: the latest WIN + 1 closed candles (regularized), oldest first.
  function compact(C, nextTs) {
    const n = C.length;
    const [, o, h, l, c, v] = C[n - 1];
    const r = new Array(WIN);
    for (let i = 0; i < WIN; i++) r[i] = Math.log(C[n - WIN + i][4] / C[n - WIN + i - 1][4]);
    let sw = 0, swr = 0, s2 = 0, w = 1;
    for (let j = 0; j < WIN; j++) {           // j = 0 is the newest return
      const x = r[WIN - 1 - j];
      swr += w * x * x; sw += w; s2 += x * x; w *= LAM;
    }
    const sig = Math.max(Math.sqrt(swr / sw), 1e-6);
    const slong = Math.max(Math.sqrt(s2 / WIN), 1e-6);
    const sum = (k) => { let s = 0; for (let i = WIN - k; i < WIN; i++) s += r[i]; return s; };
    let r5 = 0; for (let i = WIN - 5; i < WIN; i++) r5 += r[i] * r[i];
    let hi60 = -Infinity, lo60 = Infinity, v30 = 0;
    for (let i = n - 60; i < n; i++) { hi60 = Math.max(hi60, C[i][2]); lo60 = Math.min(lo60, C[i][3]); }
    for (let i = n - 30; i < n; i++) v30 += C[i][5];
    const rng = h - l;
    const minute = Math.floor(nextTs / 60) % 60, hour = Math.floor(nextTs / 3600) % 24;
    const f = [1,
      clip(r[WIN - 1] / sig, 6), clip(r[WIN - 2] / sig, 6), clip(r[WIN - 3] / sig, 6),
      clip(sum(5) / (sig * Math.sqrt(5)), 6),
      clip(sum(15) / (sig * Math.sqrt(15)), 6),
      clip(sum(60) / (sig * Math.sqrt(60)), 6),
      clip(Math.log(sig / slong), 3),
      clip(Math.log(Math.sqrt(r5 / 5) / sig + 0.05), 3),
      rng > 0 ? (c - o) / rng : 0,
      rng > 0 ? (h - Math.max(o, c)) / rng : 0,
      rng > 0 ? (Math.min(o, c) - l) / rng : 0,
      clip(Math.log(Math.log(h / l) / sig + 0.05), 3),
      clip(Math.log((v + 1e-6) / (v30 / 30 + 1e-6)), 5),
      (c - lo60) / (hi60 - lo60 + 1e-12) - 0.5,
      Math.sin(2 * Math.PI * minute / 60), Math.cos(2 * Math.PI * minute / 60),
      minute === 0 ? 1 : 0, minute % 15 === 0 ? 1 : 0,
      Math.sin(2 * Math.PI * hour / 24), Math.cos(2 * Math.PI * hour / 24)];
    return { f, sig };
  }

  // the full model's view of the next candle, through its linear copy
  function nextRaw(W, f, sig) {
    const y = W.map((row) => dot(row, f));
    return {
      p: 1 / (1 + Math.exp(-y[0])), a: sig * Math.max(Math.exp(y[1]) - OFF, 0),
      eUp: sig * Math.max(Math.exp(y[2]) - OFF, 0), eDn: sig * Math.max(Math.exp(y[3]) - OFF, 0),
      q05: sig * y[4], q25: sig * y[5], q75: sig * y[6], q95: sig * y[7],
    };
  }
  // The next candle from the linear copy alone. Offsets are log-price moves from the last close.
  function generate(W, f, sig) {
    const n = nextRaw(W, f, sig);
    const b = n.p >= 0.5 ? n.a : -n.a;
    return { p: n.p, b, u: Math.max(n.eUp - Math.max(b, 0), 0), d: Math.max(n.eDn - Math.max(-b, 0), 0),
      q05: n.q05, q25: n.q25, q75: n.q75, q95: n.q95 };
  }
  function horizonRaw(Wh, f, sig) {
    const y = Wh.map((row) => dot(row, f));
    const p = Math.min(Math.max(0.5 + 0.5 * y[0], 0.02), 0.98);
    const size = (v) => sig * Math.max(Math.exp(v) - OFF_H, 0);
    return { d: p >= 0.5 ? 1 : -1, a: size(y[1]), eUp: size(y[2]), eDn: size(y[3]), p };
  }

  // The next candles as one connected chain (see generate_path in probcast/student.py).
  // ver: {fmt, W, H, scale, cone}. o: where a candle opens; lo / hi: 90% range of its
  // close - all log-offsets from the last real close. The chain never leaves the model's
  // own 50% range: a candle that would is drawn in the other colour (flip).
  function generatePath(ver, f, sig) {
    const n = nextRaw(ver.W, f, sig);
    if (!ver.H || ver.fmt !== FORMAT) {
      const g = generate(ver.W, f, sig);
      g.o = 0; g.lo = g.q05; g.hi = g.q95; g.flip = 0;
      return [g];
    }
    const iq = 0.5 * (n.q75 - n.q25);
    const path = [];
    let o = 0;
    for (let h = 1; h <= ver.H.length; h++) {
      const r = horizonRaw(ver.H[h - 1], f, sig);
      let a = r.a, eUp = r.eUp, eDn = r.eDn, cone = 1;
      if (h === 1) { a = n.a; eUp = n.eUp; eDn = n.eDn; }
      else { const [kb, kr] = ver.scale[h - 1]; a = a * kb; eUp = eUp * kr; eDn = eDn * kr; cone = ver.cone[h - 1]; }
      let b = r.d * a;
      const w = Math.max(cone * iq, a);
      const flip = Math.abs(o + b) > w && Math.abs(o - b) < Math.abs(o + b);
      if (flip) b = -b;
      const g = { p: r.p, b, u: Math.max(eUp - Math.max(b, 0), 0), d: Math.max(eDn - Math.max(-b, 0), 0),
        o, lo: cone * n.q05, hi: cone * n.q95, flip: flip ? 1 : 0 };
      if (h === 1) { g.q05 = n.q05; g.q25 = n.q25; g.q75 = n.q75; g.q95 = n.q95; }
      path.push(g);
      o += b;
    }
    return path;
  }

  // ---- reversal agents (mirror of rev_features / tree_probs / rev_rows in probcast/student.py)
  // side = +1 top (swing high), -1 bottom (swing low). C: closed candles [ts,o,h,l,c,v]. K: swing size.
  function revFeatures(C, f, sig, side, K) {
    const m = f.slice();
    for (const i of FLIP) m[i] = side * m[i];
    if (side < 0) { const t = m[10]; m[10] = m[11]; m[11] = t; }
    const n = Math.max(4 * K, 30) + 2;
    const W = C.slice(C.length - n);
    const Hh = [], Ll = [], Cc = [], Oo = [];
    for (const r of W) {
      if (side > 0) { Hh.push(r[2]); Ll.push(r[3]); Cc.push(r[4]); Oo.push(r[1]); }
      else { Hh.push(-r[3]); Ll.push(-r[2]); Cc.push(-r[4]); Oo.push(-r[1]); }
    }
    const N = W.length, last = W[N - 1];
    const sg = sig * last[4], rng = last[2] - last[3];
    const top = (w) => { let x = -Infinity; for (let i = N - w; i < N; i++) x = Math.max(x, Hh[i]); return x; };
    const low = (w) => { let x = Infinity; for (let i = N - w; i < N; i++) x = Math.min(x, Ll[i]); return x; };
    const best = top(2 * K + 1);
    let age = 0;
    while (Hh[N - 1 - age] !== best) age++;
    let run = 0;
    while (run < 5 && Cc[N - 1 - run] > Cc[N - 2 - run]) run++;
    let prevTop = -Infinity;
    for (let i = N - K - 1; i < N - 1; i++) prevTop = Math.max(prevTop, Hh[i]);
    const x = [(top(K) - Hh[N - 1]) / sg, (top(2 * K) - Hh[N - 1]) / sg, (top(4 * K) - Hh[N - 1]) / sg, (top(30) - Hh[N - 1]) / sg,
      (top(K) - Cc[N - 1]) / sg, (top(30) - Cc[N - 1]) / sg, (Hh[N - 1] - Cc[N - 1]) / sg,
      (Hh[N - 1] - Hh[N - 2]) / sg, (Hh[N - 2] - Hh[N - 3]) / sg, (Cc[N - 1] - Cc[N - 2]) / sg, (Cc[N - 2] - Cc[N - 3]) / sg, rng / sg,
      (Cc[N - 1] - low(10)) / sg, (Cc[N - 1] - low(2 * K)) / sg,
      rng > 0 ? (Hh[N - 1] - Cc[N - 1]) / rng : 0.5, rng > 0 ? (Cc[N - 1] - Oo[N - 1]) / rng : 0,
      age / (2 * K), run / 5,
      (Hh[N - 2] - Cc[N - 2]) / sg, (prevTop - Hh[N - 2]) / sg];
    return m.concat(x.map((v) => clip(v, 20)));
  }
  // model input for both sides and every call type: [top x horizons, bottom x horizons]
  function revRows(phiTop, phiBottom, horizons) {
    const out = [];
    for (const phi of [phiTop, phiBottom]) for (const j of horizons) out.push(phi.concat([j]));
    return out;
  }
  // Probability from a packed tree model for one row. Features are rounded to
  // single precision first - the precision the trees were trained in.
  function treeProb(model, row) {
    const x = row.map(Math.fround);
    const { f, t, l, r, v, roots } = model;
    let raw = 0;
    for (let k = 0; k < roots.length; k++) {
      let nd = roots[k];
      while (nd >= 0) nd = x[f[nd]] <= t[nd] ? l[nd] : r[nd];
      raw += v[-nd - 1];
    }
    return 1 / (1 + Math.exp(-raw));
  }
  // [[top now, top next], [bottom now, bottom next]]
  function revProbs(model, phiTop, phiBottom, horizons) {
    const p = revRows(phiTop, phiBottom, horizons).map((row) => treeProb(model, row));
    const nh = horizons.length;
    return [p.slice(0, nh), p.slice(nh)];
  }
  // is candle i a swing high (side +1) / swing low (side -1) of size K? Needs K candles on both sides.
  function isSwing(C, i, side, K) {
    if (i - K < 0 || i + K >= C.length) return null;
    for (let k = i - K; k <= i + K; k++) {
      if (side > 0 ? C[k][2] > C[i][2] : C[k][3] < C[i][3]) return false;
    }
    return true;
  }
  // was the call right: a swing point of that side at candle i-1, i or i+1? null while unknown
  function swingNear(C, i, side, K) {
    const v = [-1, 0, 1].map((d) => isSwing(C, i + d, side, K));
    if (v.some((x) => x === true)) {
      // a hit is final only when it cannot be un-made: a swing point, once confirmed, stays one
      return true;
    }
    return v.some((x) => x === null) ? null : false;
  }

  // parameter version that was already published when the minute `ts` started
  function versionAt(versions, ts) {
    let best = null;
    for (const v of versions) if (v.eff <= ts && (!best || v.eff > best.eff)) best = v;
    return best;
  }

  // score of a generated candle against the real one (same as probcast/goal.py)
  function candleScore(g, ao, ac, ah, al) {
    const iou = (lo1, hi1, lo2, hi2) => {
      const inter = Math.max(0, Math.min(hi1, hi2) - Math.max(lo1, lo2));
      const uni = Math.max(hi1, hi2) - Math.min(lo1, lo2);
      return uni > 0 ? inter / uni : 1;
    };
    const gLo = Math.min(0, g.b), gHi = Math.max(0, g.b);
    const body = iou(gLo, gHi, Math.min(ao, ac), Math.max(ao, ac));
    const range = iou(gLo - g.d, gHi + g.u, al, ah);
    return { body, range, score: 0.5 * body + 0.5 * range };
  }

  const api = { WIN, GRAN, FORMAT, regularize, compact, generate, generatePath, revFeatures, revRows, treeProb, revProbs,
    isSwing, swingNear, versionAt, candleScore };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.Student = api;
})(typeof self !== "undefined" ? self : this);
