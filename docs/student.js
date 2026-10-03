// Live generator - mirror of probcast/student.py (see that file for the idea).
// tests/parity.mjs checks that both implementations return the same numbers.
(function (root) {
  const WIN = 240, LAM = 0.97, OFF = 0.01, OFF_H = 0.1, GRAN = 60, REV_K = 5;
  const FLIP = [1, 2, 3, 4, 5, 6, 9, 14];
  const clip = (x, a) => Math.max(-a, Math.min(a, x));

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

  // W: matrix (outputs x features). Offsets are log-price moves from the last close.
  function generate(W, f, sig) {
    const y = W.map((row) => row.reduce((s, w, i) => s + w * f[i], 0));
    const p = 1 / (1 + Math.exp(-y[0]));
    const a = sig * Math.max(Math.exp(y[1]) - OFF, 0);
    const b = p >= 0.5 ? a : -a;
    const eUp = sig * Math.max(Math.exp(y[2]) - OFF, 0), eDn = sig * Math.max(Math.exp(y[3]) - OFF, 0);
    return {
      p, b,
      u: Math.max(eUp - Math.max(b, 0), 0), d: Math.max(eDn - Math.max(-b, 0), 0),
      q05: sig * y[4], q25: sig * y[5], q75: sig * y[6], q95: sig * y[7],
    };
  }

  // The next candles (see generate_path in probcast/student.py). ver: {W, H, scale, cone}.
  // lo / hi bound the close of each candle as a log-offset from the last real close.
  function generatePath(ver, f, sig) {
    const g = generate(ver.W, f, sig);
    g.o = 0; g.lo = g.q05; g.hi = g.q95;
    const path = [g];
    if (!ver.H) return path;
    let o = g.b;
    ver.H.forEach((Wh, j) => {
      const y = Wh.map((row) => row.reduce((s, w, i) => s + w * f[i], 0));
      const p = Math.min(Math.max(0.5 + 0.5 * y[0], 0.02), 0.98);
      const size = (v) => sig * Math.max(Math.exp(v) - OFF_H, 0);
      const [kb, kr] = ver.scale[j];
      const b = (p >= 0.5 ? 1 : -1) * size(y[1]) * kb;
      const c = ver.cone[j];
      path.push({
        p, b, u: Math.max(kr * size(y[2]) - Math.max(b, 0), 0), d: Math.max(kr * size(y[3]) - Math.max(-b, 0), 0),
        o, lo: c * g.q05, hi: c * g.q95,
      });
      o += b;
    });
    return path;
  }

  // ---- reversal agent (mirror of rev_features / rev_probs in probcast/student.py)
  // side = +1 top (swing high), -1 bottom (swing low). C: closed candles [ts,o,h,l,c,v].
  function revFeatures(C, f, sig, side) {
    const m = f.slice();
    for (const i of FLIP) m[i] = side * m[i];
    if (side < 0) { const t = m[10]; m[10] = m[11]; m[11] = t; }
    const n = C.length, c = C[n - 1][4];
    const hi = [], lo = [];
    for (let i = Math.max(0, n - 31); i < n; i++) { hi.push(C[i][2]); lo.push(C[i][3]); }
    const last = (a, k) => a.slice(a.length - k);
    const ext = side > 0 ? hi : lo;
    const dist = (k) => (side > 0 ? Math.log(Math.max(...last(ext, k)) / c) : Math.log(c / Math.min(...last(ext, k)))) / sig;
    const reject = (side > 0 ? Math.log(hi[hi.length - 1] / c) : Math.log(c / lo[lo.length - 1])) / sig;
    const leg = (side > 0 ? Math.log(c / Math.min(...last(lo, 10))) : Math.log(Math.max(...last(hi, 10)) / c)) / sig;
    const prev = ext.slice(ext.length - REV_K - 1, ext.length - 1);
    const isNew = side > 0 ? (hi[hi.length - 1] >= Math.max(...prev) ? 1 : 0) : (lo[lo.length - 1] <= Math.min(...prev) ? 1 : 0);
    const best = side > 0 ? Math.max(...last(ext, 10)) : Math.min(...last(ext, 10));
    let age = 0;
    while (ext[ext.length - 1 - age] !== best) age++;
    let run = 0;
    while (run < 5 && side * (C[n - 1 - run][4] - C[n - 2 - run][4]) > 0) run++;
    const cl = (x, a) => Math.min(Math.max(x, 0), a);
    return m.concat([cl(dist(REV_K), 8), cl(dist(2 * REV_K), 8), cl(dist(30), 8), isNew, age / 10, run / 5, cl(reject, 8), cl(leg, 12)]);
  }
  function revProbs(R, phi) {
    return R.map((row) => {
      const z = Math.max(-30, Math.min(30, row.reduce((s, w, i) => s + w * phi[i], 0)));
      return 1 / (1 + Math.exp(-z));
    });
  }
  // is candle i a swing high (side +1) / swing low (side -1) of order REV_K? Needs K candles on both sides.
  function isSwing(C, i, side) {
    if (i - REV_K < 0 || i + REV_K >= C.length) return null;
    for (let k = i - REV_K; k <= i + REV_K; k++) {
      if (side > 0 ? C[k][2] > C[i][2] : C[k][3] < C[i][3]) return false;
    }
    return true;
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

  const api = { WIN, GRAN, REV_K, regularize, compact, generate, generatePath, revFeatures, revProbs, isSwing, versionAt, candleScore };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.Student = api;
})(typeof self !== "undefined" ? self : this);
