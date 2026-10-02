// Live generator - mirror of probcast/student.py (see that file for the idea).
// tests/parity.mjs checks that both implementations return the same numbers.
(function (root) {
  const WIN = 240, LAM = 0.97, OFF = 0.01, GRAN = 60;
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

  const api = { WIN, GRAN, regularize, compact, generate, versionAt, candleScore };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.Student = api;
})(typeof self !== "undefined" ? self : this);
