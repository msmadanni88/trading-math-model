// Live page: real candles from the exchange (updated on every trade), the
// model's predicted candles, the fixed history of what it said, the match of
// every candle, and the reversal agents' calls with their control panel.
(() => {
  "use strict";
  const S = window.Student, LC = window.LightweightCharts, GRAN = S.GRAN;
  const qs = new URLSearchParams(location.search);
  const onPages = location.hostname.endsWith("github.io");
  const owner = onPages ? location.hostname.split(".")[0] : "msmadanni88";
  const repo = onPages ? (location.pathname.split("/")[1] || "trading-math-model") : "trading-math-model";
  const DATA = qs.get("data") || `https://raw.githubusercontent.com/${owner}/${repo}/state/live`;
  const API = qs.get("api") || "https://api.exchange.coinbase.com";
  const WSS = qs.get("ws") || "wss://ws-feed.exchange.coinbase.com";
  const XAPI = qs.get("x") || "https://www.okx.com";          // the other venue (cross-venue agent)
  const KEEP = 900;                       // candles kept on the chart
  const $ = (id) => document.getElementById(id);
  const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  const C = { up: css("--up"), down: css("--down"), gen: css("--gen"), lock: css("--lock"), warn: css("--warn"),
    text: css("--text-2"), mute: css("--text-3"), line: css("--line"), surface: css("--surface") };
  const tz = new Date().getTimezoneOffset() * 60;
  const toChart = (ts) => ts - tz;        // the chart library draws UTC; shift so the axis shows local time
  const fromChart = (t) => t + tz;
  const fmtP = (x) => x.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const fmtT = (ts) => new Date(ts * 1000).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  const pct = (x) => Math.max(1, Math.round(100 * x));
  const pc1 = (x) => (100 * x).toFixed(1) + "%";
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };
  const store = { get: (k) => { try { return JSON.parse(localStorage.getItem(k) || "null"); } catch (e) { return null; } },
    set: (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* no storage: fine */ } } };

  // ---------------------------------------------------------------- state
  let product = "ETH-USD";
  let HZ = 15;                            // candles in the chain (from the cloud)
  let rev = { ks: [3, 5, 8, 13], k: 5, hs: [0, 2] };
  const cmap = new Map();                 // ts -> [ts,o,h,l,c,v] closed candles
  const provisional = new Set();          // closed candles built from the trade stream, not yet confirmed by the exchange
  let closed = [];                        // regularized, ascending
  let idx = new Map();                    // ts -> index in closed
  // The candle being built right now. `trusted`: its open is the real open of
  // the minute (this page saw the minute start, or the exchange supplied it).
  let forming = null, trusted = false, openPending = false;
  let versions = [];
  let models = {};                        // swing size -> {model id -> packed trees}
  let cloud = null, cloudOld = false;
  // The other venue: complete one-minute candles of the same asset there (ts -> close).
  // xinfo: what the cloud says to read ({inst, ...}); xTried: a first attempt has finished;
  // xOkAt: when it last answered. Without it the page predicts from this market alone.
  const XC = new Map();
  let xinfo = null, xTried = false, xOkAt = 0;
  let lastTickAt = 0, wsOpen = false, dirty = false, syncing = false;
  let skew = 0;                           // exchange clock minus this device's clock, seconds
  const skews = [];
  const now = () => Date.now() / 1000 + skew;

  // THE RECORD. One entry per minute, written once and never changed afterwards:
  //   G   the predicted candle of that minute, made one minute ahead   {b,u,d,p,q05,q95}
  //   K   fixed history: that minute's candle in the chain frozen at the
  //       start of its quarter hour                                    {h,o,b,u,d}
  //   R   reversal calls, key "size|for_ts|side|type"   {made,for,k,side,typ,p,level,hit}
  //   PR  what the reversal model said after each candle, per swing size  [topNow, topNext, bottomNow, bottomNext]
  // Sources, in this order: what this browser already showed (kept across
  // reloads), what the cloud stored, what this page computes now.
  const G = new Map(), K = new Map(), R = new Map(), PR = {};
  let doneTs = 0;                         // last candle whose predictions this page has written
  const setOnce = (m, k, v) => { if (!m.has(k)) m.set(k, v); };
  const STORE = "candle-generator-record-v2";
  function loadRecord() {
    const s = store.get(STORE);
    if (!s || s.product !== product) return;
    for (const [k, v] of s.g || []) G.set(k, v);
    for (const [k, v] of s.k || []) K.set(k, v);
    for (const [k, v] of s.r || []) R.set(k, v);
    for (const [kk, rows] of Object.entries(s.pr || {})) { PR[kk] = PR[kk] || new Map(); for (const [k, v] of rows) PR[kk].set(k, v); }
  }
  function saveRecord() {
    const cut = Date.now() / 1000 - 1500 * GRAN;
    const pack = (m, ts) => [...m].filter(([k, v]) => ts(k, v) >= cut);
    store.set(STORE, { product, g: pack(G, (k) => k), k: pack(K, (k) => k), r: pack(R, (k, v) => v.for),
      pr: Object.fromEntries(Object.entries(PR).map(([kk, m]) => [kk, pack(m, (k) => k)])) });
  }

  // reversal control panel (what the user chose; "auto" = the agent's own thresholds)
  const panel = Object.assign({ k: null, type: "both", autoNow: true, autoNext: true, thrNow: 60, thrNext: 45 }, store.get("candle-generator-panel") || {});

  // ---------------------------------------------------------------- chart
  const chart = LC.createChart($("chart"), {
    autoSize: true,
    // the TradingView attribution required by the licence is the link in the page footer
    layout: { background: { color: C.surface }, textColor: C.text, fontFamily: css("--mono"), fontSize: 11, attributionLogo: false },
    grid: { vertLines: { color: "rgba(255,255,255,0.03)" }, horzLines: { color: "rgba(255,255,255,0.05)" } },
    rightPriceScale: { borderColor: C.line, scaleMargins: { top: 0.04, bottom: 0.33 } },
    // narrow screens: thinner candles, so the last half hour stays in view next to the 15 predicted ones
    timeScale: { borderColor: C.line, timeVisible: true, secondsVisible: false, rightOffset: 2, barSpacing: window.innerWidth < 700 ? 6 : 11 },
    crosshair: { mode: LC.CrosshairMode.Normal },
  });
  // A change of width (rotating a phone, resizing the window) must not push the predicted
  // candles out of view: if the chart was showing the present, it keeps showing it.
  let chartW = $("chart").clientWidth, edgePos = 0;
  chart.timeScale().subscribeVisibleLogicalRangeChange(() => {
    if ($("chart").clientWidth === chartW) edgePos = chart.timeScale().scrollPosition();
  });
  if (typeof ResizeObserver !== "undefined") {
    new ResizeObserver(() => {
      const w = $("chart").clientWidth;
      if (!w || w === chartW) return;
      const narrow = window.innerWidth < 700, was = chartW;
      chartW = w;
      if ((was < 700) !== narrow || Math.abs(w - was) > 40) chart.timeScale().applyOptions({ barSpacing: narrow ? 6 : 11 });
      if (edgePos > -10) chart.timeScale().scrollToPosition(Math.max(edgePos, 0), false);
    }).observe($("chart"));
  }
  const quiet = { priceLineVisible: false, lastValueVisible: false };
  // start of every frozen chain: a faint column behind the candles
  const segS = chart.addHistogramSeries({ ...quiet, priceScaleId: "seg", color: "rgba(217,215,204,0.07)",
    autoscaleInfoProvider: () => ({ priceRange: { minValue: 0, maxValue: 1 } }) });
  chart.priceScale("seg").applyOptions({ scaleMargins: { top: 0.02, bottom: 0.31 }, visible: false });
  const realS = chart.addCandlestickSeries({
    upColor: C.up, downColor: C.down, borderVisible: false, wickUpColor: C.up, wickDownColor: C.down,
    priceLineVisible: true, priceLineColor: "rgba(255,255,255,0.35)",
  });
  const bandOpt = { ...quiet, color: "rgba(57,135,229,0.55)", lineWidth: 1, lineStyle: LC.LineStyle.Dashed,
    lineType: LC.LineType.WithSteps, crosshairMarkerVisible: false };
  const hiS = chart.addLineSeries(bandOpt), loS = chart.addLineSeries(bandOpt);
  const LK = "rgba(217,215,204,0.62)";
  const lockS = chart.addCandlestickSeries({ ...quiet, upColor: "rgba(217,215,204,0)", downColor: "rgba(217,215,204,0.30)",
    borderVisible: true, borderUpColor: LK, borderDownColor: LK, wickUpColor: LK, wickDownColor: LK });
  const genS = chart.addCandlestickSeries({ ...quiet, upColor: "rgba(57,135,229,0)", downColor: "rgba(57,135,229,0.42)",
    borderVisible: true, borderUpColor: C.gen, borderDownColor: C.gen, wickUpColor: C.gen, wickDownColor: C.gen });
  // reversal calls: an invisible line that only carries the markers
  const revS = chart.addLineSeries({ ...quiet, lineVisible: false, pointMarkersVisible: false, crosshairMarkerVisible: false, color: "rgba(0,0,0,0)" });

  // match of every predicted candle, 1-100, drawn like a volume pane
  const scoreS = chart.addHistogramSeries({ ...quiet, priceScaleId: "score",
    autoscaleInfoProvider: () => ({ priceRange: { minValue: 0, maxValue: 100 } }),     // fixed 0-100 scale
    priceFormat: { type: "custom", minMove: 1, formatter: (v) => v.toFixed(0) } });
  chart.priceScale("score").applyOptions({ scaleMargins: { top: 0.71, bottom: 0.12 }, visible: false });
  // colour rows: what colour the model said (top row) and what the market printed (bottom row)
  const dotOpt = { ...quiet, priceScaleId: "dots", lineVisible: false, pointMarkersVisible: false, crosshairMarkerVisible: false,
    color: "rgba(0,0,0,0)", autoscaleInfoProvider: () => ({ priceRange: { minValue: -0.7, maxValue: 1.7 } }) };
  const dotModelS = chart.addLineSeries(dotOpt), dotRealS = chart.addLineSeries(dotOpt);
  chart.priceScale("dots").applyOptions({ scaleMargins: { top: 0.91, bottom: 0.005 }, visible: false });
  const RAMP = [[230, 103, 103], [217, 161, 58], [25, 158, 112]];          // red -> amber -> green
  function scoreColor(v) {                                                 // v in 0..100
    const t = Math.max(0, Math.min(1, v / 100)) * 2, i = t >= 1 ? 1 : 0, f = t - i;
    const c = RAMP[i].map((a, k) => Math.round(a + (RAMP[i + 1][k] - a) * f));
    return `rgb(${c[0]},${c[1]},${c[2]})`;
  }

  // ---------------------------------------------------------------- data helpers
  function rebuild() {
    const keys = [...cmap.keys()].sort((a, b) => a - b);
    for (const k of keys.slice(0, Math.max(0, keys.length - KEEP - 300))) { cmap.delete(k); provisional.delete(k); }
    closed = S.regularize(keys.slice(-KEEP - 300).map((k) => cmap.get(k)));
    idx = new Map(closed.map((k, i) => [k[0], i]));
  }
  const closeAt = (ts) => { const i = idx.get(ts); return i == null ? null : closed[i][4]; };
  const candleAt = (ts) => (forming && forming[0] === ts ? forming : idx.has(ts) ? closed[idx.get(ts)] : null);
  const lastClosed = () => (closed.length ? closed[closed.length - 1] : null);
  const formingOk = () => !!forming && !!closed.length && forming[0] === lastClosed()[0] + GRAN;

  function pathAt(i) {                     // the chain made when closed[i] closed, or null
    const t = closed[i][0], nxt = t + GRAN, ver = S.versionAt(versions, nxt);
    if (!ver || i < S.WIN) return null;
    const win = closed.slice(i - S.WIN, i + 1);
    const { f, sig } = S.compact(win, nxt);
    const x = xinfo && ver.HX ? xView(i, sig) : null;
    return { ver, win, f, sig, x, path: S.generatePath(ver, f, sig, x) };
  }
  function xView(i, sig) {                 // what the other venue said when closed[i] closed, or null
    if (i < S.X_WIN - 1) return null;
    const w = closed.slice(i - S.X_WIN + 1, i + 1);
    return S.xFeatures(w.map((k) => k[4]), w.map((k) => (XC.has(k[0]) ? XC.get(k[0]) : null)), sig);
  }
  // Is the other venue's candle for the minute that started at `t` still on its way? Then the
  // prediction made from that minute waits a moment for it (a few seconds at most).
  const xAlive = () => !xTried || Date.now() / 1000 - xOkAt < 300;
  const xWaiting = (t) => !!xinfo && !XC.has(t) && (!xTried || (xAlive() && now() - (t + GRAN) < 3.5));
  // Writes the record for every closed candle this page has not handled yet.
  // Same functions and same published parameters as the cloud, so the cloud
  // later stores the same numbers. Nothing already in the record is touched.
  function advance() {
    if (!closed.length || !versions.length) return;
    let wrote = false;
    for (let i = S.WIN; i < closed.length; i++) {
      const t = closed[i][0], nxt = t + GRAN;
      if (t <= doneTs) continue;
      if (xWaiting(t) && (S.versionAt(versions, nxt) || {}).HX) break;        // its view of this minute is a moment away
      const m = pathAt(i);
      if (!m) continue;
      const { ver, win, f, sig, path } = m, made = Math.round(now());
      const p0 = path[0];
      setOnce(G, nxt, { b: p0.b, u: p0.u, d: p0.d, p: p0.p, q05: p0.q05, q95: p0.q95, c: p0.call, x: p0.x, made });
      if (path.length === HZ && nxt % (HZ * GRAN) === 0) {          // a quarter hour starts: freeze the chain
        path.forEach((q, j) => setOnce(K, nxt + j * GRAN, { h: j + 1, o: q.o, b: q.b, u: q.u, d: q.d, made }));
      }
      doneTs = t;
      wrote = true;
    }
    for (const k of activeKs()) if (advanceRev(k)) wrote = true;
    if (wrote) saveRecord();
  }
  // Reversal agents, with the published trees. Done per swing size, for the
  // sizes whose model this page has loaded: the one on show and the default.
  const doneRev = {};                       // swing size -> last candle this page has spoken about
  const activeKs = () => [...new Set([rev.k, panelK()])];
  function advanceRev(k) {
    const byId = models[k];
    if (!byId || !closed.length || !versions.length) return false;
    const from = doneRev[k] != null ? doneRev[k] : cloud ? cloud.last_ts : Infinity;
    let wrote = false;
    for (let i = S.WIN; i < closed.length; i++) {
      const t = closed[i][0], nxt = t + GRAN;
      if (t <= from) continue;
      const ver = S.versionAt(versions, nxt);
      const model = ver ? byId[(ver.rm || {})[k]] : null, thr = ver ? (ver.rt || {})[k] : null;
      if (!model || !thr) continue;
      const win = closed.slice(i - S.WIN, i + 1);
      const { f, sig } = S.compact(win, nxt);
      const pr = S.revProbs(model, S.revFeatures(win, f, sig, 1, k), S.revFeatures(win, f, sig, -1, k), rev.hs);
      PR[k] = PR[k] || new Map();
      setOnce(PR[k], t, [pr[0][0], pr[0][1], pr[1][0], pr[1][1]]);
      [1, -1].forEach((side, si) => {
        for (let a = 0; a < rev.hs.length; a++) {
          const p = pr[si][a];
          if (!(p >= thr[a])) continue;
          const forTs = t + rev.hs[a] * GRAN;
          if ([-2, -1, 0, 1, 2].some((d) => R.has(`${k}|${forTs + d * GRAN}|${side}|${a}`))) continue;      // already called
          R.set(`${k}|${forTs}|${side}|${a}`, { made: nxt, for: forTs, k, side, typ: a, p: Math.round(p * 1e4) / 1e4,
            level: callLevel(i, side, a), hit: null });
        }
      });
      doneRev[k] = t;
      wrote = true;
    }
    return wrote;
  }
  // where a call is marked: the extreme of the turn that is in, or the last price for a turn still to come
  function callLevel(i, side, a) {
    if (rev.hs[a] !== 0) return closed[i][4];
    const two = closed.slice(Math.max(0, i - 1), i + 1);
    return side > 0 ? Math.max(...two.map((k) => k[2])) : Math.min(...two.map((k) => k[3]));
  }
  function bar(o, g) {                      // drawn candle from an opening price and {b,u,d}
    const c = o * Math.exp(g.b);
    return { o, c, h: Math.max(o, c) * Math.exp(g.u), l: Math.min(o, c) * Math.exp(-g.d) };
  }
  function genBar(ts) {
    const g = G.get(ts), p = closeAt(ts - GRAN);
    if (!g || p == null) return null;
    return Object.assign(bar(p, g), { q05: p * Math.exp(g.q05), q95: p * Math.exp(g.q95), g });
  }
  // Fixed history. A frozen chain is drawn from the close it started from;
  // every candle after its first opens exactly where the one before closed.
  function lockBar(ts) {
    const g = K.get(ts);
    if (!g) return null;
    const p = closeAt(ts - g.h * GRAN);     // the close its chain started from
    if (p == null) return null;
    let first = ts;                         // earliest candle of this chain that is in the record without a break
    for (let t = ts - GRAN, h = g.h - 1; h >= 1 && K.has(t) && K.get(t).h === h; t -= GRAN, h--) first = t;
    let open = p * Math.exp(K.get(first).o), b = null;
    for (let t = first; t <= ts; t += GRAN) { b = bar(open, K.get(t)); open = b.c; }
    return Object.assign(b, { g, from: p, start: ts - (g.h - 1) * GRAN });
  }
  // The prediction right of the price: the chain made at the last close.
  // Candle 1 is the predicted candle of the minute that is forming (from the
  // record); the rest hang on it, each opening where the one before closed.
  let liveCache = null;
  function liveChain() {
    if (!formingOk()) return [];
    const i = closed.length - 1, key = closed[i][0] + "|" + versions.length + "|" + (versions.length ? versions[versions.length - 1].eff : 0) + "|" + XC.has(closed[i][0]);
    if (!liveCache || liveCache.key !== key) liveCache = { key, m: pathAt(i) };
    const m = liveCache.m, first = genBar(forming[0]);
    if (!m || !first) return [];
    const p0 = closed[i][4], out = [];
    let prev = first.c;
    m.path.forEach((q, j) => {
      if (j === 0) { out.push(Object.assign({ ts: forming[0], h: 1, p: first.g.p, lo: first.q05, hi: first.q95 }, first)); return; }
      const b = bar(prev, q);
      out.push(Object.assign({ ts: forming[0] + j * GRAN, h: j + 1, p: q.p, lo: p0 * Math.exp(q.lo), hi: p0 * Math.exp(q.hi), g: q }, b));
      prev = b.c;
    });
    return out;
  }
  // overlap of a predicted candle (given as a drawn bar) with the real candle
  function scoreBar(b, k) {
    if (!b || !k) return null;
    return S.candleScore({ b: Math.log(b.c / b.o), u: Math.log(b.h / Math.max(b.o, b.c)), d: Math.log(Math.min(b.o, b.c) / b.l) },
      Math.log(k[1] / b.o), Math.log(k[4] / b.o), Math.log(k[2] / b.o), Math.log(k[3] / b.o));
  }

  // ---------------------------------------------------------------- reversal calls shown on the chart
  const panelK = () => (rev.ks.includes(panel.k) ? panel.k : rev.k);
  const custom = () => !panel.autoNow || !panel.autoNext;
  function ownThr(k) {
    const ver = S.versionAt(versions, now());
    const t = ver && ver.rt && ver.rt[k];
    return t || (cloud && cloud.rev && cloud.rev[k] ? ["now", "next"].map((n) => cloud.rev[k].types[n].threshold) : null);
  }
  function activeThr(k) {
    const own = ownThr(k) || [0.6, 0.45];
    return [panel.autoNow ? own[0] : panel.thrNow / 100, panel.autoNext ? own[1] : panel.thrNext / 100];
  }
  function callOutcome(c) {                 // true / false once the candles around it are known, else null
    if (c.hit != null) return !!c.hit;
    const i = idx.get(c.for);
    return i == null ? null : S.swingNear(closed, i, c.side, c.k);
  }
  // The calls to draw. With the agent's own thresholds: the record. With the
  // sliders moved: what those thresholds would have called, from the
  // probabilities the published model issued at the time.
  function shownCalls(from) {
    const k = panelK();
    let calls;
    if (!custom()) calls = [...R.values()].filter((c) => c.k === k && c.for >= from);
    else {
      calls = [];
      const thr = activeThr(k), seen = new Set(), m = PR[k] || new Map();
      for (const t of [...m.keys()].filter((t) => t >= from - 2 * GRAN).sort((a, b) => a - b)) {
        const v = m.get(t), i = idx.get(t);
        if (i == null) continue;
        [1, -1].forEach((side, si) => {
          for (let a = 0; a < rev.hs.length; a++) {
            const p = v[si * rev.hs.length + a];
            if (!(p >= thr[a])) continue;
            const forTs = t + rev.hs[a] * GRAN;
            if ([-2, -1, 0, 1, 2].some((d) => seen.has(`${forTs + d * GRAN}|${side}|${a}`))) continue;
            seen.add(`${forTs}|${side}|${a}`);
            calls.push({ made: t + GRAN, for: forTs, k, side, typ: a, p, level: callLevel(i, side, a), hit: null, whatIf: true });
          }
        });
      }
      calls = calls.filter((c) => c.for >= from);
    }
    if (panel.type !== "both") calls = calls.filter((c) => c.typ === (panel.type === "now" ? 0 : 1));
    return calls.sort((a, b) => a.for - b.for || b.side - a.side);
  }

  // ---------------------------------------------------------------- rendering
  function renderAll() {
    const bars = closed.slice(-KEEP);
    const all = formingOk() ? bars.concat([forming]) : bars;
    realS.setData(all.map((k) => ({ time: toChart(k[0]), open: k[1], high: k[2], low: k[3], close: k[4] })));
    const g = [], hi = [], lo = [], sc = [], lk = [], seg = [], d1 = [], d0 = [], m1 = [], m0 = [];
    const dotCol = (x) => (x > 0 ? C.up : x < 0 ? C.down : C.mute);
    const cndl = (t, b) => ({ time: t, open: b.o, high: b.h, low: b.l, close: b.c });
    const lockAt = (ts) => {
      const q = lockBar(ts);
      if (!q) return;
      lk.push(cndl(toChart(ts), q));
      if (q.g.h === 1) seg.push({ time: toChart(ts), value: 1 });
    };
    for (const k of all) {
      const t = toChart(k[0]), b = genBar(k[0]), isClosed = k !== forming;
      lockAt(k[0]);
      if (!b) continue;
      g.push(cndl(t, b));
      hi.push({ time: t, value: b.q95 });
      lo.push({ time: t, value: b.q05 });
      const v = pct(scoreBar(b, k).score);
      sc.push({ time: t, value: v, color: scoreColor(v) });
      d1.push({ time: t, value: 1 }); m1.push({ time: t, position: "inBar", shape: "circle", size: b.g.c >= 2 ? 1.6 : b.g.c ? 1.0 : 0.4, color: dotCol(b.g.b) });
      if (isClosed) { d0.push({ time: t, value: 0 }); m0.push({ time: t, position: "inBar", shape: "circle", size: 0.4, color: dotCol(k[4] - b.o) }); }
    }
    // minutes that have not started: the rest of the live chain, and the rest of the frozen one
    const chain = liveChain();
    for (const q of chain.slice(1)) {
      const t = toChart(q.ts);
      g.push(cndl(t, q));
      hi.push({ time: t, value: q.hi });
      lo.push({ time: t, value: q.lo });
      d1.push({ time: t, value: 1 }); m1.push({ time: t, position: "inBar", shape: "circle", size: 0.4, color: dotCol(q.c - q.o) });
    }
    if (all.length) { const last = all[all.length - 1][0]; for (let h = 1; h < HZ; h++) lockAt(last + h * GRAN); }
    genS.setData(g); hiS.setData(hi); loS.setData(lo); lockS.setData(lk); segS.setData(seg); scoreS.setData(sc);
    dotModelS.setData(d1); dotModelS.setMarkers(m1); dotRealS.setData(d0); dotRealS.setMarkers(m0);
    renderCalls(all);
    applyToggles();
    renderNext();
    renderSession();
    renderPanel();
    placeOverlays();
  }
  function renderCalls(all) {
    if (!all.length) { revS.setData([]); revS.setMarkers([]); return; }
    const pts = new Map(), marks = [];
    for (const c of shownCalls(all[0][0])) {
      const out = callOutcome(c);
      if (!pts.has(c.for)) pts.set(c.for, c.level);
      marks.push({ time: toChart(c.for), position: c.side > 0 ? "aboveBar" : "belowBar",
        shape: c.typ === 0 ? (c.side > 0 ? "arrowDown" : "arrowUp") : "circle", size: c.typ === 0 ? 1 : 0.7,
        color: out === null ? C.warn : out ? C.up : C.down, text: out === null ? Math.round(c.p * 100) + "%" : out ? "✓" : "✗" });
    }
    revS.setData([...pts].sort((a, b) => a[0] - b[0]).map(([t, v]) => ({ time: toChart(t), value: v })));
    revS.setMarkers(marks);
  }
  const TOGGLES = ["t-real", "t-gen", "t-lock", "t-band", "t-score", "t-dots", "t-rev"];
  function applyToggles() {
    const on = (id) => $(id).checked;
    realS.applyOptions({ visible: on("t-real") });
    genS.applyOptions({ visible: on("t-gen") });
    lockS.applyOptions({ visible: on("t-lock") }); segS.applyOptions({ visible: on("t-lock") });
    hiS.applyOptions({ visible: on("t-band") }); loS.applyOptions({ visible: on("t-band") });
    scoreS.applyOptions({ visible: on("t-score") });
    dotModelS.applyOptions({ visible: on("t-dots") }); dotRealS.applyOptions({ visible: on("t-dots") });
    revS.applyOptions({ visible: on("t-rev") });
    store.set("candle-generator-toggles", Object.fromEntries(TOGGLES.map((id) => [id, on(id)])));
    if (!on("t-score")) closeInspector();
    placeOverlays();
  }
  function renderForming() {
    if (!formingOk()) { $("countdown").hidden = true; return; }
    realS.update({ time: toChart(forming[0]), open: forming[1], high: forming[2], low: forming[3], close: forming[4] });
    const fs = scoreBar(genBar(forming[0]), forming);
    if (fs) { const v = pct(fs.score); scoreS.update({ time: toChart(forming[0]), value: v, color: scoreColor(v) }); }
    const pe = $("price");
    pe.textContent = fmtP(forming[4]);
    const p = closeAt(forming[0] - GRAN);
    pe.className = "price" + (p == null || forming[4] === p ? "" : forming[4] > p ? " up" : " down");
    placeOverlays();
  }
  // countdown under the price marker, and the labels of the two colour rows
  function placeOverlays() {
    const cd = $("countdown");
    const y = formingOk() ? realS.priceToCoordinate(forming[4]) : null;
    const w = chart.priceScale("right").width();
    if (y == null || !w || !$("t-real").checked) cd.hidden = true;
    else {
      const left = Math.max(0, Math.ceil(forming[0] + GRAN - now()));
      cd.hidden = false;
      cd.textContent = `0:${String(Math.min(left, 59)).padStart(2, "0")}`;
      cd.style.width = w + "px";
      cd.style.top = Math.round(y + 11) + "px";
    }
    const show = $("t-dots").checked;
    for (const [id, s, v] of [["lab-model", dotModelS, 1], ["lab-market", dotRealS, 0]]) {
      const yy = show ? s.priceToCoordinate(v) : null;
      $(id).hidden = yy == null;
      if (yy != null) $(id).style.top = Math.round(yy - 7) + "px";
    }
  }
  function kv(dl, k, v) { dl.append(el("dt", null, k), el("dd", null, v)); }
  function renderNext() {
    const box = $("next");
    box.replaceChildren();
    if (!formingOk()) { box.append(el("p", "muted", syncing || lastTickAt ? "syncing with the exchange…" : "waiting for the market feed…")); return; }
    const b = genBar(forming[0]);
    if (!b) {
      const wait = versions.length && xinfo && closed.length && xWaiting(lastClosed()[0]);
      box.append(el("p", "muted", wait ? "reading the other venue…" : versions.length ? "collecting candles before the first prediction…" : "waiting for the model…"));
      return;
    }
    const up = b.g.b >= 0;
    const dir = el("div", "dir " + (up ? "up" : "down"));
    dir.append(el("span", "arrow", up ? "▲ up" : "▼ down"), el("span", "p", `P(up) ${(b.g.p * 100).toFixed(1)}%`),
      el("span", "callbadge " + (b.g.c >= 2 ? "strong" : b.g.c ? "yes" : "no"), b.g.c >= 2 ? "strong call" : b.g.c ? "confident call" : "no confident call"));
    const dl = el("dl", "kv");
    kv(dl, "opens at", fmtP(b.o));
    kv(dl, "predicted close", `${fmtP(b.c)}  (${(b.g.b * 1e4).toFixed(1)} bp)`);
    kv(dl, "predicted high / low", `${fmtP(b.h)} / ${fmtP(b.l)}`);
    kv(dl, "90% range for the close", `${fmtP(b.q05)} – ${fmtP(b.q95)}`);
    if (xinfo) {
      const i = closed.length - 1, v = i >= S.WIN ? xView(i, S.compact(closed.slice(i - S.WIN, i + 1), forming[0]).sig) : null;
      kv(dl, "other venue", !b.g.x ? "not read for this candle"
        : v ? `${v[1] >= 0 ? "ahead" : "behind"} by ${Math.abs(v[1]).toFixed(1)} typical moves` : "read");
    }
    box.append(dir, dl);
    const s = scoreBar(b, forming);
    const ls = el("div", "livescore");
    ls.append("match so far this minute: ", el("b", null, s ? pct(s.score) + "/100" : "–"));
    box.append(ls);
    const chain = liveChain();
    if (chain.length > 1) {
      const ul = el("ol", "ahead");
      for (const q of chain) {
        const li = el("li", q.c >= q.o ? "up" : "down");
        li.append(el("span", "when", fmtT(q.ts)), el("span", "arrow", q.c >= q.o ? "▲" : "▼"),
          el("span", null, `${fmtP(q.o)} → ${fmtP(q.c)}`), el("span", "muted", `±${((q.hi - q.lo) / 2).toFixed(2)}`));
        ul.append(li);
      }
      box.append(el("p", "muted small", `the next ${chain.length} candles — open → close, and how wide the 90% range for that close is:`), ul);
    }
    const pend = shownCalls(forming[0]).filter((c) => callOutcome(c) === null);
    if (pend.length) {
      const pl = el("ol", "ahead");
      for (const c of pend) {
        const li = el("li", c.side > 0 ? "down" : "up");
        li.append(el("span", "when", fmtT(c.for)), el("span", "arrow", c.side > 0 ? "▼" : "▲"),
          el("span", null, (c.side > 0 ? "top" : "bottom") + (c.typ === 0 ? " in, near " : " coming, near ") + fmtP(c.level)),
          el("span", "muted", Math.round(c.p * 100) + "%"));
        pl.append(li);
      }
      box.append(el("p", "muted small", `reversal calls waiting for their result (turn size ${panelK()}):`), pl);
    }
  }
  function renderSession() {
    let n = 0, sum = 0, dirOk = 0, dirN = 0, ln = 0, lsum = 0, cN = 0, cOk = 0;
    for (const k of closed.slice(-KEEP)) {
      const b = genBar(k[0]), s = scoreBar(b, k);
      if (s) { n++; sum += s.score; if (k[4] !== b.o) { const ok = (b.g.b > 0) === (k[4] > b.o); dirN++; if (ok) dirOk++; if (b.g.c) { cN++; if (ok) cOk++; } } }
      const q = scoreBar(lockBar(k[0]), k);
      if (q) { ln++; lsum += q.score; }
    }
    $("chartnote").textContent = n
      ? `On this chart: ${n} predicted candles, average match ${(100 * sum / n).toFixed(0)}/100, colour right ${(100 * dirOk / Math.max(dirN, 1)).toFixed(1)}%` +
        (cN ? ` (confident and strong calls — the bigger dots: ${cOk} of ${cN})` : "") +
        (ln ? `; fixed history: ${ln} candles, average match ${(100 * lsum / ln).toFixed(0)}/100 at their real price level.` : ".")
      : "Predicted candles appear here as soon as the model's parameters and 4 hours of candles are loaded.";
  }
  const cell = (a) => (a ? pc1(a.rate) : "–");
  function ciCell(a) {                     // win rate with its 90% interval underneath
    const td = el("td", null, cell(a));
    if (a && a.ci) td.append(el("span", "ci", `${(100 * a.ci[0]).toFixed(1)}–${(100 * a.ci[1]).toFixed(1)}`));
    else if (a) td.append(el("span", "ci", `n ${a.n.toLocaleString("en-US")}`));
    return td;
  }
  const LAYERS = { colour_next: "colour of the next candle", colour_confident: "· its confident calls only", colour_strong: "· its strong calls only", colour_clear: "· candles that really moved", colour_path: "colour of candles 2–15", chain_end_side: "side of price 15 min on (fixed history)", overall: "everything pooled" };
  function layerName(l) {
    const m = /^reversal_k(\d+)_(now|next)$/.exec(l);
    return m ? `${m[2] === "now" ? "turn is in" : "turn coming"} · size ${m[1]}` : LAYERS[l] || l;
  }
  function renderCloud() {
    if (!cloud || cloudOld) return;
    document.querySelectorAll(".hz").forEach((e) => { e.textContent = HZ; });
    const tb = $("score").tBodies[0];
    tb.replaceChildren();
    const pc = (x) => (100 * x).toFixed(1);
    for (const [name, w] of Object.entries(cloud.windows || {})) {
      const s = w.student;
      if (!s) continue;
      const tr = el("tr");
      const typ = w.baseline.typical.score, rep = w.baseline.repeat.score;
      tr.append(el("td", null, name), el("td", "model" + (s.score < typ ? " behind" : ""), pc(s.score)),
        el("td", null, pc(typ)), el("td", null, pc(rep)), el("td", null, s.dir_acc == null ? "–" : pc1(s.dir_acc)));
      tb.append(tr);
    }
    const d = (cloud.windows || {})["24h"];
    $("scorenote").textContent = d
      ? `Last 24h: the 90% range held ${pc1(d.cov90)} of closes, the 50% range ${pc1(d.cov50)}. "typical" and "repeat" are naive generators the model has to beat.`
      : "";
    const ab = $("ahead").tBodies[0];
    ab.replaceChildren();
    const by = (d && d.locked && d.locked.by_candle) || {};
    for (const [h, a] of Object.entries((d && d.ahead) || {})) {
      const tr = el("tr");
      tr.append(el("td", null, h), el("td", "model", pc(a.score)), el("td", null, a.dir_acc == null ? "–" : pc1(a.dir_acc)),
        el("td", null, a.cone90 == null ? "–" : pc1(a.cone90)), el("td", null, by[h] ? `${pc(by[h].score)} · ${by[h].miss_bp.toFixed(1)} bp` : "–"));
      ab.append(tr);
    }
    const lk = d && d.locked;
    $("aheadnote").textContent = lk
      ? `"match" judges each candle from its own open (shape and colour). "fixed history" judges the frozen chain where it actually stood: match and how far its close missed. All of its candles together: ${pc(lk.score)}; a chain that simply stayed at the starting price would score ${pc(lk.flat_score)}` +
        (lk.end_side_right != null ? `; it ended on the right side of the start ${pc1(lk.end_side_right)} of the time.` : ".")
      : "";
    // win-rate ledger
    const lt = $("ledger").tBodies[0];
    lt.replaceChildren();
    const led = cloud.ledger || {};
    const rank = (l) => {                                    // candles first, then the reversal agents by size, the total last
      const m = /^reversal_k(\d+)_(now|next)$/.exec(l);
      return m ? 10 + 2 * +m[1] + (m[2] === "next") : l === "overall" ? 999 : ["colour_next", "colour_confident", "colour_strong", "colour_clear", "colour_path", "chain_end_side"].indexOf(l);
    };
    const order = Object.keys(led).filter((l) => led[l]).sort((a, b) => rank(a) - rank(b));
    for (const l of order) {
      const b = led[l], tr = el("tr"), t = b.trend;
      const tcell = el("td", t ? "trend " + t.verdict : null, t ? `${t.verdict === "up" ? "▲" : t.verdict === "down" ? "▼" : "→"} ${(100 * t.change >= 0 ? "+" : "") + (100 * t.change).toFixed(1)}` : "–");
      const c7 = ciCell(b["7d"]);
      c7.className = "model";
      tr.append(el("td", null, layerName(l)), el("td", null, cell(b.today)), el("td", null, cell(b["1d"])), c7, ciCell(b["30d"]),
        el("td", null, b.base == null ? "–" : pc1(b.base)), tcell);
      if (l === "overall") tr.className = "total";
      if (l === "colour_confident" || l === "colour_strong" || l === "colour_clear") tr.className = "sub";
      lt.append(tr);
    }
    const since = cloud.live_since ? new Date(cloud.live_since * 1000).toLocaleDateString([], { month: "short", day: "numeric" }) : null;
    $("ledgernote").textContent = order.length
      ? `Under each win rate: the range it would fall in 9 times out of 10 if the same days were drawn again. Trend: the last 7 days against the 7 before, in points; → means the change is within noise. "Today" is the UTC day still running.` +
        (cloud.colour && cloud.colour.threshold ? ` A colour call is confident when P(up) is at least ${(100 * cloud.colour.threshold[0]).toFixed(1)} points from 50% and strong from ${(100 * cloud.colour.threshold[1]).toFixed(1)}: the lines that give about ${cloud.colour.per_day[0]} and ${cloud.colour.per_day[1]} calls a day, re-drawn every six hours.` : "") +
        (since ? ` These models went live on ${since}; earlier days are a replay of history in which the models saw only the past.` : "")
      : "The archive starts with the first full day.";
    // the same numbers by market regime
    const sl = cloud.slices, st = $("slices").tBodies[0];
    st.replaceChildren();
    $("slicebox").hidden = !sl;
    if (sl) {
      const rc = (a) => (a ? `${pc1(a.rate)}` : "–");
      for (const kind of Object.keys(sl)) {
        let first = true;
        for (const [name, r] of Object.entries(sl[kind])) {
          const tr = el("tr", first ? "kind" : null);
          first = false;
          tr.append(el("td", null, name), el("td", null, r.score == null ? "–" : pc(r.score)), el("td", null, rc(r.colour)),
            el("td", null, rc(r.confident)), el("td", null, rc(r.turn_in)));
          st.append(tr);
        }
      }
    }
    const lf = $("learning");
    lf.replaceChildren();
    const L = cloud.learning;
    if (L) {
      kv(lf, "candles learned from", L.candles_learned.toLocaleString("en-US"));
      kv(lf, "sizing learned from the score", `body ×${L.body_scale}, reach ×${L.reach_scale}`);
      if (L.last_contest) kv(lf, "last tree-model contest", L.last_contest.promoted ? "new model won" : "old model kept");
      kv(lf, "generator versions published", String(L.versions_published));
      const ct = cloud.colour && cloud.colour.tuned;
      if (ct) kv(lf, "does confidence pay? last 7 days", `every minute ${pc1(ct.every_minute)} · confident ${ct.levels[0].win_rate == null ? "–" : pc1(ct.levels[0].win_rate)} · strong ${ct.levels[1].win_rate == null ? "–" : pc1(ct.levels[1].win_rate)}`);
    }
    const wbox = $("weights");
    wbox.replaceChildren();
    const ws = Object.entries((cloud.next && cloud.next.weights) || {}).sort((a, b) => b[1] - a[1]);
    const wmax = Math.max(...ws.map((x) => x[1]), 0.01);
    for (const [name, w] of ws) {
      const row = el("div", "wrow"), barEl = el("span", "bar"), fill = el("i");
      fill.style.width = (100 * w / wmax).toFixed(1) + "%";
      barEl.append(fill);
      row.append(el("span", null, name), barEl, el("span", null, (w * 100).toFixed(0) + "%"));
      wbox.append(row);
    }
    const rg = $("regime");
    rg.replaceChildren();
    if (cloud.next) {
      kv(rg, "regime change (last 12 min)", pc1(cloud.next.changepoint_prob));
      kv(rg, "current regime age", Math.round(cloud.next.regime_age_min) + " min");
    }
    if (cloud.hmm) {
      const i = cloud.hmm.state_prob.indexOf(Math.max(...cloud.hmm.state_prob));
      kv(rg, "volatility state", ["calm", "normal", "turbulent"][i] + ` (${(cloud.hmm.state_prob[i] * 100).toFixed(0)}%)`);
    }
    const vn = cloud.venue;
    if (vn && vn.head) {
      const cx = vn.colour_30d || {};
      kv(rg, "cross-venue agent", `${vn.source} ${vn.inst}` + (vn.used_24h != null ? ` · read for ${pc1(vn.used_24h)} of the last 24 h` : ""));
      if (cx.with) kv(rg, "colour right, 30 days: with it / without", `${pc1(cx.with.rate)} / ${cx.without ? pc1(cx.without.rate) : "–"}`);
    }
    const last = (cloud.retrain_log || []).slice(-1)[0];
    if (last) kv(rg, "last self-retrain", fmtT(last.ts) + ", " + new Date(last.ts * 1000).toLocaleDateString());
    const al = $("alerts");
    al.replaceChildren();
    if (!(cloud.alerts || []).length) al.append(el("li", "ok", "on track: no alerts from the last cloud run"));
    for (const a of cloud.alerts || []) al.append(el("li", null, a));
  }

  // ---------------------------------------------------------------- reversal control panel
  function buildPanel() {
    const kb = $("rev-k");
    kb.replaceChildren();
    for (const k of rev.ks) {
      const b = el("button", null, String(k));
      b.type = "button"; b.dataset.v = k;
      b.title = `${k} candles on each side`;
      b.addEventListener("click", () => {
        panel.k = k;
        panelChanged();
        ensureModels(k).then(() => { if (advanceRev(k)) { saveRecord(); panelChanged(); } }).catch(() => {});
      });
      kb.append(b);
    }
  }
  function panelChanged() {
    store.set("candle-generator-panel", panel);
    closeInspector();
    renderCalls(formingOk() ? closed.slice(-KEEP).concat([forming]) : closed.slice(-KEEP));
    renderNext();
    renderPanel();
  }
  function renderPanel() {
    const k = panelK(), own = ownThr(k);
    for (const b of $("rev-k").children) b.setAttribute("aria-pressed", String(+b.dataset.v === k));
    for (const b of $("rev-type").children) b.setAttribute("aria-pressed", String(b.dataset.v === panel.type));
    for (const [n, i] of [["now", 0], ["next", 1]]) {
      const auto = n === "now" ? panel.autoNow : panel.autoNext, sl = $("rev-thr-" + n);
      $("rev-auto-" + n).checked = auto;
      sl.disabled = auto;
      if (auto && own) sl.value = Math.round(own[i] * 100);
      else if (!auto) sl.value = n === "now" ? panel.thrNow : panel.thrNext;
      $("rev-out-" + n).textContent = sl.value + "%";
    }
    const cu = custom();
    $("revmode").textContent = cu
      ? "What-if: the marks on the chart are what these confidence levels would have called, from the probabilities the model issued at the time. The agent's own calls stay in the record."
      : "The marks on the chart are the agent's own calls, stored when they were made. Arrow = the turn is in; dot = a turn coming within three candles. Move a slider to see what another confidence level would do.";
    const tb = $("rev").tBodies[0];
    tb.replaceChildren();
    const info = cloud && !cloudOld && cloud.rev ? cloud.rev[k] : null;
    const thr = activeThr(k);
    const bars = closed.slice(-KEEP);
    const calls = bars.length ? shownCallsAll(bars[0][0]) : [];
    [["turn is in", "now", 0], ["turn coming", "next", 1]].forEach(([label, name, a]) => {
      if (panel.type !== "both" && panel.type !== name) return;
      // on this chart, counted here
      const mine = calls.filter((c) => c.typ === a).map(callOutcome).filter((x) => x !== null);
      const row = (period, perDay, hit, chance, cls) => {
        const tr = el("tr");
        tr.append(el("td", null, label), el("td", null, period), el("td", null, perDay == null ? "–" : perDay.toFixed(0)),
          el("td", cls || "model", hit == null ? "–" : pc1(hit)), el("td", null, chance == null ? "–" : pc1(chance)));
        tb.append(tr);
      };
      const hours = bars.length / 60;
      row("this chart", hours ? mine.length / hours * 24 : null, mine.length ? mine.filter(Boolean).length / mine.length : null, chartChance(k, a, bars));
      for (const w of ["7d", "30d"]) {
        if (!info) continue;
        if (!cu) {
          const x = ((info.windows || {})[w] || {})[name];
          if (x && x.hit_rate != null) row(w === "7d" ? "7 days" : "30 days", x.per_day, x.hit_rate, x.chance, x.naive_rule != null && x.hit_rate < x.naive_rule ? "model behind" : "model");
        } else {
          const cv = ((info.curve || {})[w] || {})[name];
          if (!cv) continue;
          const pt = cv.reduce((best, p) => (Math.abs(p[0] - thr[a]) < Math.abs(best[0] - thr[a]) ? p : best), cv[0]);
          const ch = (((info.windows || {})[w] || {})[name] || {}).chance;
          row(`${w === "7d" ? "7 days" : "30 days"} at ${Math.round(pt[0] * 100)}%`, pt[1], pt[2], ch);
        }
      }
    });
    const rf = $("revfacts");
    rf.replaceChildren();
    if (info) {
      const ty = info.types;
      kv(rf, "agent's own confidence", `${Math.round(ty.now.threshold * 100)}% in · ${Math.round(ty.next.threshold * 100)}% coming`);
      kv(rf, "it must keep making", `${cloud.rev_min_per_day} calls a day of each kind`);
      kv(rf, "turns learned from", info.labels_learned.toLocaleString("en-US"));
      if (info.brier_skill != null) kv(rf, "probability skill vs chance", pc1(info.brier_skill));
      const w7 = ((info.windows || {})["7d"] || {}).now;
      if (w7 && w7.naive_rule != null) kv(rf, "naive rule “new high = top”, 7 days", pc1(w7.naive_rule));
      kv(rf, "daily contest", info.stalled ? "widened: hit rate has slipped" : "normal: one challenger a day");
    }
  }
  function shownCallsAll(from) {            // like shownCalls but both types (for the table)
    const t = panel.type;
    panel.type = "both";
    const c = shownCalls(from);
    panel.type = t;
    return c;
  }
  function chartChance(k, a, bars) {        // how often the event happens anyway, on the candles of this chart
    let n = 0, h = 0;
    const i0 = idx.get(bars[0][0]);
    for (let i = i0; i < closed.length; i += 3) {
      for (const side of [1, -1]) {
        const v = S.swingNear(closed, i + rev.hs[a], side, k);
        if (v !== null) { n++; if (v) h++; }
      }
    }
    return n > 30 ? h / n : null;
  }
  $("rev-type").addEventListener("click", (e) => { const b = e.target.closest("button"); if (b) { panel.type = b.dataset.v; panelChanged(); } });
  for (const n of ["now", "next"]) {
    $("rev-auto-" + n).addEventListener("change", (e) => {
      const own = ownThr(panelK());
      if (n === "now") { panel.autoNow = e.target.checked; if (own) panel.thrNow = Math.round(own[0] * 100); }
      else { panel.autoNext = e.target.checked; if (own) panel.thrNext = Math.round(own[1] * 100); }
      panelChanged();
    });
    $("rev-thr-" + n).addEventListener("input", (e) => {
      if (n === "now") panel.thrNow = +e.target.value; else panel.thrNext = +e.target.value;
      $("rev-out-" + n).textContent = e.target.value + "%";
      panelChanged();
    });
  }

  function renderFeeds() {
    const t = Date.now() / 1000;
    const m = $("feed-market"), c = $("feed-cloud");
    const fresh = t - lastTickAt < 20;
    m.className = "feed " + (syncing && !formingOk() ? "warn" : fresh ? "ok" : lastTickAt ? "warn" : "bad");
    m.lastChild.textContent = syncing && !formingOk() ? "market feed: syncing…"
      : fresh ? (wsOpen ? "market feed: live" : "market feed: polling") : lastTickAt ? "market feed: quiet" : "market feed: not connected";
    const age = cloud ? (t - cloud.generated) / 60 : null;
    c.className = "feed " + (age == null ? "bad" : cloudOld ? "warn" : age < 30 ? "ok" : "warn");
    c.lastChild.textContent = age == null ? "model cloud: no data yet"
      : cloudOld ? "model cloud: moving to the new models…"
      : age < 90 ? `model cloud: learned ${Math.max(0, Math.round(age))} min ago` : `model cloud: learned ${(age / 60).toFixed(1)} h ago`;
    const xf = $("feed-x");
    xf.hidden = !xinfo;
    if (xinfo) {
      const okx = t - xOkAt < 150;
      xf.className = "feed " + (okx ? "ok" : xTried ? "bad" : "warn");
      xf.lastChild.textContent = okx ? "other venue: live" : xTried ? "other venue: not reachable" : "other venue: connecting…";
    }
    if (formingOk()) {
      const left = Math.max(0, forming[0] + GRAN - now());
      $("clock").textContent = `closes in ${Math.ceil(left)}s`;
      $("progress").style.width = (100 * (1 - left / GRAN)).toFixed(1) + "%";
    } else { $("clock").textContent = ""; $("progress").style.width = "0"; }
  }

  // ---------------------------------------------------------------- market feed
  // Rule: a candle on this chart is the exchange's own candle, or - for the
  // minute in progress and the few seconds until the exchange publishes a
  // minute that just closed - built here from the trade stream. Such a candle
  // counts as exact (`trusted`) only if this page heard every trade of that
  // minute: the stream was already running when the minute began and no trade
  // number was skipped. Anything else is approximate: it is shown, but it is
  // replaced by the exchange's numbers before a prediction is made from it.
  // A stale price is never carried into a new candle.
  const tape = [];                          // trades heard on the stream: [time, price, size]
  let wsSince = Infinity;                   // exchange time from which the stream has been complete
  let lastTradeId = null, lastWsAt = 0;
  let obs = null;                           // every price seen during the current minute: {bucket, hi, lo, last}
  const heard = () => wsOpen && Date.now() / 1000 - lastWsAt < 10;
  function fromTape(bucket, prevClose) {    // the candle of `bucket` from the trades heard, or flat if none yet
    const mine = tape.filter((x) => x[0] >= bucket && x[0] < bucket + GRAN);
    if (!mine.length) return [bucket, prevClose, prevClose, prevClose, prevClose, 0];
    return [bucket, mine[0][1], Math.max(...mine.map((x) => x[1])), Math.min(...mine.map((x) => x[1])), mine[mine.length - 1][1],
      mine.reduce((v, x) => v + x[2], 0)];
  }
  function resync() {
    forming = null; trusted = false; openPending = false;
    renderForming();
    syncExchange().catch(() => {});
  }
  function roll(bucket) {                   // the minute `bucket` begins
    const late = bucket - forming[0] !== GRAN;                    // the tab slept through at least one minute
    if (late || !trusted || !heard()) { resync(); return; }
    cmap.set(forming[0], forming);          // exact: every trade of it was heard
    provisional.add(forming[0]);
    const c = forming[4];
    forming = [bucket, c, c, c, c, 0];
    openPending = true;                     // the first trade of the minute sets the open
    rebuild();
    advance();
    renderAll();
    xPoll(bucket - GRAN);                   // the other venue's candle of the minute that closed, then the prediction
    setTimeout(() => syncExchange().catch(() => {}), 4000);       // then take the exchange's own candle for the minute that closed
  }
  function onTrade(price, size, t, isTrade) {
    if (!(price > 0)) return;
    lastTickAt = Date.now() / 1000;
    const bucket = Math.floor(t / GRAN) * GRAN;
    if (!obs || obs.bucket !== bucket) { if (!obs || bucket > obs.bucket) obs = { bucket, hi: price, lo: price, last: price }; }
    else { obs.hi = Math.max(obs.hi, price); obs.lo = Math.min(obs.lo, price); obs.last = price; }
    $("price").textContent = fmtP(price);
    if (!forming) return;                                         // syncing: the exchange's candles come first
    if (bucket < forming[0]) return;                              // late print for a minute that is already closed
    if (bucket > forming[0]) { roll(bucket); if (!forming || bucket !== forming[0]) return; }
    if (openPending && isTrade) { forming[1] = forming[2] = forming[3] = price; openPending = false; }
    forming[2] = Math.max(forming[2], price);
    forming[3] = Math.min(forming[3], price);
    forming[4] = price;
    forming[5] += size;
    dirty = true;
  }
  let ws = null;
  function connect() {
    if (ws && (ws.readyState === 0 || ws.readyState === 1)) return;
    try { ws = new WebSocket(WSS); } catch (e) { return; }
    const sock = ws;
    sock.onopen = () => { wsOpen = true; lastWsAt = Date.now() / 1000; sock.send(JSON.stringify({ type: "subscribe", product_ids: [product], channels: ["matches", "heartbeat"] })); };
    sock.onmessage = (ev) => {
      let m; try { m = JSON.parse(ev.data); } catch (e) { return; }
      lastWsAt = Date.now() / 1000;
      if (m.type === "subscriptions") { if (wsSince === Infinity) wsSince = now(); return; }      // complete from here on
      if (m.type === "last_match") {                                // the trade before the stream started: a price, nothing more
        lastTradeId = +m.trade_id;
        if (wsSince === Infinity) wsSince = now();
        onTrade(+m.price, 0, now(), false);
        return;
      }
      if (m.type !== "match") return;
      const id = +m.trade_id, t = Date.parse(m.time) / 1000;
      if (lastTradeId != null && id <= lastTradeId) return;         // already counted
      if (lastTradeId != null && id !== lastTradeId + 1) { wsSince = t; trusted = false; }       // a trade was missed
      lastTradeId = id;
      skews.push(t - Date.now() / 1000);                            // exchange clock vs this device's clock
      if (skews.length > 40) skews.shift();
      skew = Math.max(...skews);
      if (Math.abs(skew) < 0.75) skew = 0;
      tape.push([t, +m.price, +m.size]);
      while (tape.length && tape[0][0] < t - 180) tape.shift();
      onTrade(+m.price, +m.size, t, true);
    };
    sock.onclose = () => { if (ws === sock) { wsOpen = false; wsSince = Infinity; lastTradeId = null; trusted = false; setTimeout(connect, 3000); } };
    sock.onerror = () => { try { sock.close(); } catch (e) { /* ignore */ } };
  }
  async function getJSON(url, bust) {
    const r = await fetch(bust ? url + (url.includes("?") ? "&" : "?") + "t=" + Math.floor(Date.now() / 30000) : url, { cache: "no-store" });
    if (!r.ok) throw new Error(url + " -> " + r.status);
    return r.json();
  }
  // The other venue's candles. Only candles it has marked complete are taken. Failures are
  // silent: the page then predicts from this market alone and says so.
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
  async function xGet(path) {
    const r = await fetch(XAPI + path, { cache: "no-store" });
    if (!r.ok) throw new Error("other venue -> " + r.status);
    const j = await r.json();
    if (String(j.code) !== "0") throw new Error("other venue: " + j.msg);
    for (const k of j.data || []) if (String(k[k.length - 1]) === "1") XC.set(Math.floor(+k[0] / 1000), +k[4]);
    xOkAt = Date.now() / 1000;
    return j.data || [];
  }
  async function xSync(fromTs) {             // the latest candles, and further back to `fromTs` if asked
    if (!xinfo) return;
    try {
      await xGet(`/api/v5/market/candles?instId=${xinfo.inst}&bar=1m&limit=${fromTs ? 300 : 5}`);
      let oldest = Math.min(...XC.keys());
      for (let page = 0; page < 14 && fromTs && oldest > fromTs; page++) {
        const rows = await xGet(`/api/v5/market/history-candles?instId=${xinfo.inst}&bar=1m&after=${oldest * 1000}&limit=100`);
        if (!rows.length) break;
        oldest = Math.min(oldest - GRAN, ...rows.map((k) => Math.floor(+k[0] / 1000)));
      }
      const cut = now() - 1600 * GRAN;
      for (const k of XC.keys()) if (k < cut) XC.delete(k);
    } catch (e) { /* carry on without it */ } finally { xTried = true; }
  }
  // A minute just closed: ask for the other venue's candle of that minute until it is there
  // (it is marked complete a moment after the minute ends), then make the prediction.
  let xPollRun = 0;
  async function xPoll(t) {
    if (!xinfo) return;
    const run = ++xPollRun;
    for (const wait of [250, 550, 800, 900, 1000]) {
      await sleep(wait);
      if (run !== xPollRun) return;
      await xSync(0);
      if (XC.has(t)) break;
    }
    if (run !== xPollRun) return;
    advance();
    renderAll();
  }
  // The exchange's own candles: fill everything since the cloud's last run,
  // replace anything this page built from the trade stream, and (re)start the
  // candle in progress.
  let syncRun = 0, retry = null;
  const again = (ms) => { clearTimeout(retry); retry = setTimeout(() => syncExchange().catch(() => {}), ms); };
  async function syncExchange() {
    const run = ++syncRun;
    syncing = true;
    try {
      let newest = null;
      const take = (rows) => {
        const t = now();
        for (const r of rows) {                             // [time, low, high, open, close, volume]
          const k = [r[0], r[3], r[2], r[1], r[4], r[5]];
          // a minute is final two seconds after it ended (the exchange is still adding its last trades before that)
          if (k[0] + GRAN + 2 <= t) { cmap.set(k[0], k); provisional.delete(k[0]); }
          else if (k[0] <= t && k[0] + GRAN > t) newest = k;
        }
      };
      take(await getJSON(`${API}/products/${product}/candles?granularity=${GRAN}`));
      // the cloud may be hours behind: page back until its candles are reached (at most 15 hours)
      const have = cloud ? cloud.last_ts : 0, t0 = now();
      let oldest = Math.min(...[...cmap.keys()].filter((k) => k > t0 - 300 * GRAN), t0);
      for (let page = 0; page < 3 && have && oldest - GRAN > have; page++) {
        const end = oldest - GRAN, start = end - 299 * GRAN;
        const iso = (t) => new Date(t * 1000).toISOString();
        const rows = await getJSON(`${API}/products/${product}/candles?granularity=${GRAN}&start=${iso(start)}&end=${iso(end)}`);
        if (!rows.length) break;
        take(rows);
        oldest = start;
      }
      if (xinfo && xTried) await Promise.race([xSync(0), sleep(2500)]);
      if (run !== syncRun) return;                          // a newer sync is on its way
      lastTickAt = Date.now() / 1000;
      rebuild();
      const bucket = Math.floor(now() / GRAN) * GRAN;
      let c = lastClosed();
      // a minute without a single trade has no candle at the exchange: once that is certain, it is a flat candle
      if (c && c[0] + GRAN < bucket && bucket - c[0] <= 4 * GRAN && now() - bucket > 20) {
        for (let t = c[0] + GRAN; t < bucket; t += GRAN) cmap.set(t, [t, c[4], c[4], c[4], c[4], 0]);
        rebuild();
        c = lastClosed();
      }
      if (c && c[0] + GRAN === bucket) {                    // history is complete up to the minute in progress
        if (forming && forming[0] === bucket && trusted) { /* exact already: leave it alone */ }
        else if (heard() && wsSince < bucket) {             // every trade of this minute was heard: exact
          forming = fromTape(bucket, c[4]);
          openPending = forming[5] === 0;
          trusted = true;
        } else {                                            // joined mid-minute: the exchange's numbers so far, plus what was seen since
          const k = newest && newest[0] === bucket ? newest.slice() : [bucket, c[4], c[4], c[4], c[4], 0];
          if (obs && obs.bucket === bucket) {               // prices this page saw during this minute
            k[2] = Math.max(k[2], obs.hi); k[3] = Math.min(k[3], obs.lo); k[4] = obs.last;
          }
          forming = k; trusted = false; openPending = false;
          if (!(newest && newest[0] === bucket)) again(5000);          // its real open is not known yet: ask again
        }
      } else {                                              // the minute that just closed is not published yet
        forming = null; trusted = false;
        again(2000);
      }
      advance();
      renderAll();
      renderForming();
    } finally { if (run === syncRun) syncing = false; }
  }
  async function pollTicker() {                              // fallback when the websocket is blocked
    if (wsOpen && Date.now() / 1000 - lastTickAt < 15) return;
    try {
      const t = await getJSON(`${API}/products/${product}/ticker`);
      onTrade(+t.price, 0, now(), false);
    } catch (e) { /* next round */ }
  }
  // the tree models of one swing size: fetched when a published version names one this page does not have
  async function ensureModels(k) {
    const need = versions.map((v) => (v.rm || {})[k]).filter((id) => id && !(models[k] || {})[id]);
    if (!need.length) return;
    const r = await getJSON(`${DATA}/rev_k${k}.json`, true).catch(() => null);
    if (r && r.models) models[k] = Object.assign(models[k] || {}, r.models);
  }
  let headSeen = null;
  async function syncCloud() {
    // a few bytes tell whether anything changed; the big files are fetched only then
    const head = await getJSON(DATA + "/head.json", true).catch(() => null);
    const key = head ? `${head.generated}|${JSON.stringify(head.models || {})}` : null;
    if (head && cloud && key === headSeen) return;
    const [latest, params] = await Promise.all([getJSON(DATA + "/latest.json", true), getJSON(DATA + "/params.json", true)]);
    const first = !cloud;
    cloud = latest;
    cloudOld = latest.v !== 2 || params.v !== 2;
    if (first) {
      product = cloud.product || product;
      $("product").textContent = product;
      document.title = `${product} · candle generator`;
      loadRecord();                                         // what this browser already showed stays as it was
    }
    const t = now();
    for (const k of latest.candles || []) if (k[0] + GRAN <= t) { cmap.set(k[0], k); provisional.delete(k[0]); }
    if (!cloudOld) {
      HZ = latest.horizon || HZ;
      if (params.rev) rev = { ks: params.rev.ks, k: params.rev.k, hs: params.rev.hs };
      versions = (params.versions || []).filter((v) => v.fmt === S.FORMAT);
      xinfo = params.x && versions.some((v) => v.HX) ? params.x : null;
      await Promise.all(activeKs().map(ensureModels));
      for (const g of latest.gen || []) setOnce(G, g[0], { b: g[1], u: g[2], d: g[3], p: g[4], q05: g[5], q95: g[8], c: g[9] == null ? 0 : g[9], x: g[10] == null ? 0 : g[10] });
      for (const g of latest.locked || []) setOnce(K, g[0], { h: g[1], o: g[2], b: g[3], u: g[4], d: g[5] });
      for (const [kk, r] of Object.entries(latest.rev || {})) {
        const k = +kk;
        PR[k] = PR[k] || new Map();
        for (const p of r.probs || []) setOnce(PR[k], p[0], [p[1] / 1000, p[2] / 1000, p[3] / 1000, p[4] / 1000]);
        for (const c of r.calls || []) {
          const id = `${k}|${c[1]}|${c[2]}|${c[3]}`, cur = R.get(id);
          if (!cur) R.set(id, { made: c[0], for: c[1], k, side: c[2], typ: c[3], p: c[4], level: c[5], hit: c[6] });
          else if (cur.hit == null && c[6] != null) cur.hit = c[6];       // only the outcome may be filled in
        }
      }
      doneTs = Math.max(doneTs, latest.last_ts || 0);
      // the other venue's candles since the cloud's last run (and an hour before, for its view of them)
      if (xinfo && (first || !xTried)) await Promise.race([xSync(Math.max((latest.last_ts || 0) - 70 * GRAN, now() - 1300 * GRAN)), sleep(9000)]);
      xTried = true;
      if (first) buildPanel();
    }
    headSeen = key;
    rebuild();
    advance();
    renderCloud();
    renderAll();
  }

  // ---------------------------------------------------------------- readout (hover) and inspector (tap a match bar)
  function ohlc(parent, tag, o, h, l, c, extra) {
    parent.append(el("span", "tag", tag));
    const v = el("span");
    v.append((c >= o ? "▲ " : "▼ "), "O ", el("b", null, fmtP(o)), "  H ", el("b", null, fmtP(h)), "  L ", el("b", null, fmtP(l)), "  C ", el("b", null, fmtP(c)), extra || "");
    parent.append(v);
  }
  function futureBar(ts) { return liveChain().find((q) => q.ts === ts && q.h > 1) || null; }
  function readout(ts) {
    const box = $("readout");
    box.replaceChildren();
    const k = candleAt(ts), b = genBar(ts) || futureBar(ts), q = lockBar(ts);
    if (k) ohlc(box, fmtT(ts) + " real", k[1], k[2], k[3], k[4]);
    const s = k ? scoreBar(b, k) : null, sq = k ? scoreBar(q, k) : null;
    if (b) ohlc(box, k ? "predicted" : fmtT(ts) + " predicted", b.o, b.h, b.l, b.c, s ? `   match ${pct(s.score)}/100` : k ? "" : "   not started yet");
    if (q) ohlc(box, k || b ? "fixed" : fmtT(ts) + " fixed", q.o, q.h, q.l, q.c, sq ? `   match ${pct(sq.score)}/100` : "");
  }
  let pinned = null;
  function closeInspector() { $("inspector").hidden = true; pinned = null; }
  function inspect(ts, point) {
    const box = $("inspector"), k = candleAt(ts), b = genBar(ts), q = lockBar(ts);
    if (!k || !b) { closeInspector(); return; }
    pinned = ts;
    box.replaceChildren();
    const head = el("div", "ihead");
    const x = el("button", "iclose", "×");
    x.type = "button";
    x.setAttribute("aria-label", "Close");
    x.addEventListener("click", closeInspector);
    head.append(el("strong", null, new Date(ts * 1000).toLocaleString([], { hour: "2-digit", minute: "2-digit", month: "short", day: "numeric" })), x);
    box.append(head);
    const s = scoreBar(b, k), sq = scoreBar(q, k);
    const big = el("div", "ibig");
    const num = el("span", "num", pct(s.score) + "%");
    num.style.color = scoreColor(pct(s.score));
    big.append(num, el("span", "muted", k === forming ? " match so far (candle still open)" : " match of the predicted candle"));
    box.append(big);
    const dl = el("dl", "kv");
    kv(dl, "body overlap / range overlap", `${Math.round(100 * s.body)}% / ${Math.round(100 * s.range)}%`);
    const mUp = b.g.b >= 0, rUp = k[4] > b.o, flat = k[4] === b.o;
    kv(dl, "colour: model → market", `${mUp ? "green" : "red"} → ${flat ? "unchanged" : rUp ? "green" : "red"}  ${flat ? "" : mUp === rUp ? "✓ right" : "✗ wrong"}`);
    kv(dl, "model's P(up)", (b.g.p * 100).toFixed(1) + "%" + (b.g.c >= 2 ? "  · strong call" : b.g.c ? "  · confident call" : "  · no confident call"));
    if (xinfo || b.g.x) kv(dl, "other venue's price read for this prediction", b.g.x ? "yes" : "no — from this market alone");
    kv(dl, "real  O H L C", `${fmtP(k[1])}  ${fmtP(k[2])}  ${fmtP(k[3])}  ${fmtP(k[4])}`);
    kv(dl, "predicted  O H L C", `${fmtP(b.o)}  ${fmtP(b.h)}  ${fmtP(b.l)}  ${fmtP(b.c)}`);
    kv(dl, "90% range for the close", `${fmtP(b.q05)} – ${fmtP(b.q95)}` + (k !== forming ? (k[4] >= b.q05 && k[4] <= b.q95 ? "  ✓ held" : "  ✗ missed") : ""));
    if (k !== forming) kv(dl, "close missed by", `${fmtP(Math.abs(k[4] - b.c))}  (${(Math.abs(Math.log(k[4] / b.c)) * 1e4).toFixed(1)} bp)`);
    if (q) {
      kv(dl, `fixed history: candle ${q.g.h} of the chain frozen at ${fmtT(q.start)}`, `${fmtP(q.o)}  ${fmtP(q.h)}  ${fmtP(q.l)}  ${fmtP(q.c)}`);
      if (sq) kv(dl, "fixed history: match at its real price level", pct(sq.score) + "%");
    }
    for (const c of shownCalls(ts).filter((c) => c.for === ts)) {
      const out = callOutcome(c);
      kv(dl, `reversal call: ${c.side > 0 ? "top" : "bottom"} ${c.typ === 0 ? "is in" : "coming"} (size ${c.k})`,
        `${Math.round(c.p * 100)}% · made ${fmtT(c.made)} · ${out === null ? "waiting for the result" : out ? "✓ hit" : "✗ miss"}`);
    }
    box.append(dl);
    box.hidden = false;
    if (point === undefined) return;                       // refresh of an open panel: keep its place
    const wrap = $("chartwrap").getBoundingClientRect();
    if (wrap.width < 620 || !point) { box.style.left = "8px"; box.style.right = "8px"; box.style.top = "8px"; box.style.width = "auto"; }
    else {
      box.style.right = "auto"; box.style.width = "360px";
      box.style.left = Math.max(8, Math.min(point.x + 14, wrap.width - 360 - chart.priceScale("right").width() - 8)) + "px";
      box.style.top = "8px";
    }
  }
  // is this point of the chart inside the row of match bars?
  function onBars(point) {
    if (!point || !$("t-score").checked) return false;
    const top = scoreS.priceToCoordinate(100), bottom = scoreS.priceToCoordinate(0);
    return top != null && bottom != null && point.y >= top - 3 && point.y <= bottom + 3;
  }
  let hovering = false;
  chart.subscribeCrosshairMove((p) => {
    hovering = !!(p && p.time != null);
    $("chart").classList.toggle("onbars", hovering && onBars(p.point) && !!G.get(fromChart(p.time)));
    if (hovering) readout(fromChart(p.time));
    else if (forming) readout(forming[0]);
  });
  const onClick = (p) => {                                   // the card opens only from a match bar
    if (!p || p.time == null || !onBars(p.point)) { closeInspector(); return; }
    inspect(fromChart(p.time), p.point);
  };
  chart.subscribeClick(onClick);
  chart.subscribeDblClick(onClick);
  chart.timeScale().subscribeVisibleLogicalRangeChange(placeOverlays);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeInspector(); });
  {
    const t = store.get("candle-generator-toggles") || {};
    for (const id of TOGGLES) if (typeof t[id] === "boolean") $(id).checked = t[id];
  }
  for (const id of TOGGLES) $(id).addEventListener("change", applyToggles);

  // ---------------------------------------------------------------- loops
  setInterval(() => {                                          // once a second, exactly like the market clock
    const t = now();
    if (forming && Math.floor(t / GRAN) * GRAN > forming[0]) roll(Math.floor(t / GRAN) * GRAN);
    if (dirty || forming) { renderForming(); dirty = false; }
    if (forming && !hovering) readout(forming[0]);
    if (pinned != null && forming && pinned === forming[0]) inspect(pinned);
    renderFeeds();
    if (forming && Math.floor(t) % 5 === 0) renderNext();
  }, 1000);
  setInterval(pollTicker, 2000);
  setInterval(() => syncExchange().catch(() => {}), 30000);
  setInterval(() => syncCloud().catch(() => {}), 60000);

  document.addEventListener("visibilitychange", () => {
    if (document.hidden) return;
    // back from the background: timers were frozen, so whatever was in progress is stale
    if (Date.now() / 1000 - lastTickAt > 20 || !formingOk()) resync();
    else syncExchange().catch(() => {});
    connect();
    syncCloud().catch(() => {});
  });
  window.addEventListener("online", () => { resync(); connect(); });

  (async () => {
    buildPanel();
    await syncCloud().catch((e) => console.warn("cloud data not available yet", e));
    await syncExchange().catch((e) => console.warn("exchange not reachable", e));
    connect();
    renderFeeds();
    if (forming) readout(forming[0]);
  })();

  // for the automated checks of this page (tests/site.mjs): a read-only view of what is drawn
  window.__x = () => ({ info: xinfo, n: XC.size, okAt: xOkAt, tried: xTried });
  window.__site = {
    state: () => ({ closed, forming, trusted, G, K, R, PR, HZ, rev, versions, provisional, panel, chain: liveChain(), doneTs }),
    genBar, lockBar, shownCalls, callOutcome, now,
    xOf: (ts) => chart.timeScale().timeToCoordinate(toChart(ts)),
    yOfBars: () => (scoreS.priceToCoordinate(100) + scoreS.priceToCoordinate(0)) / 2,
  };
})();
