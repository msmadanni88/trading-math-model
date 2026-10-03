// Live page: real candles from the exchange feed (updated on every trade),
// the model's generated candles, the fixed record of what it said five minutes
// ahead, the match of every candle, and the reversal agent's calls.
(() => {
  "use strict";
  const S = window.Student, LC = window.LightweightCharts, GRAN = S.GRAN, RK = S.REV_K;
  const qs = new URLSearchParams(location.search);
  const onPages = location.hostname.endsWith("github.io");
  const owner = onPages ? location.hostname.split(".")[0] : "msmadanni88";
  const repo = onPages ? (location.pathname.split("/")[1] || "trading-math-model") : "trading-math-model";
  const DATA = qs.get("data") || `https://raw.githubusercontent.com/${owner}/${repo}/state/live`;
  const API = qs.get("api") || "https://api.exchange.coinbase.com";
  const WSS = qs.get("ws") || "wss://ws-feed.exchange.coinbase.com";
  const KEEP = 900;                       // candles kept on the chart
  const AHEAD = 5;                        // the fixed record is written this many minutes ahead
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
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };

  // ---------------------------------------------------------------- state
  let product = "ETH-USD";
  const cmap = new Map();                 // ts -> [ts,o,h,l,c,v] closed candles
  let closed = [];                        // regularized, ascending
  let idx = new Map();                    // ts -> index in closed
  let forming = null;                     // candle being built right now
  let versions = [];
  let cloud = null;
  let lastTradeAt = 0, wsOpen = false, dirty = false;

  // THE RECORD. One entry per minute, written once and never changed afterwards:
  //   G  candle generated 1 minute ahead        {b,u,d,p,q05,q95}
  //   K  candle locked 5 minutes ahead           {o,b,u,d}   (o: where it opens, from the close it was made from)
  //   R  reversal calls, key "for_ts|side"       {made,for,side,p,level,hit}
  // Sources, in this order: what this browser already showed (kept across
  // reloads), what the cloud stored, what this page computes now.
  const G = new Map(), K = new Map(), R = new Map();
  let doneTs = 0;                         // last candle whose forecasts this page has written
  const setOnce = (m, k, v) => { if (!m.has(k)) m.set(k, v); };
  const STORE = "candle-generator-record-v1";
  function loadRecord() {
    try {
      const s = JSON.parse(localStorage.getItem(STORE) || "null");
      if (!s || s.product !== product) return;
      for (const [k, v] of s.g || []) G.set(k, v);
      for (const [k, v] of s.k || []) K.set(k, v);
      for (const [k, v] of s.r || []) R.set(k, v);
    } catch (e) { /* no storage: the record still holds for this visit */ }
  }
  function saveRecord() {
    try {
      const cut = Date.now() / 1000 - 1500 * GRAN;
      const pack = (m, ts) => [...m].filter(([k, v]) => ts(k, v) >= cut);
      localStorage.setItem(STORE, JSON.stringify({ product, g: pack(G, (k) => k), k: pack(K, (k) => k), r: pack(R, (k, v) => v.for) }));
    } catch (e) { /* ignore */ }
  }

  // ---------------------------------------------------------------- chart
  const chart = LC.createChart($("chart"), {
    autoSize: true,
    // the TradingView attribution required by the licence is the link in the page footer
    layout: { background: { color: C.surface }, textColor: C.text, fontFamily: css("--mono"), fontSize: 11, attributionLogo: false },
    grid: { vertLines: { color: "rgba(255,255,255,0.03)" }, horzLines: { color: "rgba(255,255,255,0.05)" } },
    rightPriceScale: { borderColor: C.line, scaleMargins: { top: 0.04, bottom: 0.33 } },
    timeScale: { borderColor: C.line, timeVisible: true, secondsVisible: false, rightOffset: 3, barSpacing: 13 },
    crosshair: { mode: LC.CrosshairMode.Normal },
  });
  const quiet = { priceLineVisible: false, lastValueVisible: false };
  const realS = chart.addCandlestickSeries({
    upColor: C.up, downColor: C.down, borderVisible: false, wickUpColor: C.up, wickDownColor: C.down,
    priceLineVisible: true, priceLineColor: "rgba(255,255,255,0.35)",
  });
  const bandOpt = { ...quiet, color: "rgba(57,135,229,0.55)", lineWidth: 1, lineStyle: LC.LineStyle.Dashed,
    lineType: LC.LineType.WithSteps, crosshairMarkerVisible: false };
  const hiS = chart.addLineSeries(bandOpt), loS = chart.addLineSeries(bandOpt);
  const lockS = chart.addCandlestickSeries({ ...quiet, upColor: "rgba(217,215,204,0)", downColor: "rgba(217,215,204,0.38)",
    borderVisible: true, borderUpColor: C.lock, borderDownColor: C.lock, wickUpColor: C.lock, wickDownColor: C.lock });
  const genS = chart.addCandlestickSeries({ ...quiet, upColor: "rgba(57,135,229,0)", downColor: "rgba(57,135,229,0.42)",
    borderVisible: true, borderUpColor: C.gen, borderDownColor: C.gen, wickUpColor: C.gen, wickDownColor: C.gen });
  // reversal calls: an invisible line that only carries the markers
  const revS = chart.addLineSeries({ ...quiet, lineVisible: false, pointMarkersVisible: false, crosshairMarkerVisible: false, color: "rgba(0,0,0,0)" });

  // match of every generated candle, 1-100, drawn like a volume pane
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
    for (const k of keys.slice(0, Math.max(0, keys.length - KEEP - 300))) cmap.delete(k);
    closed = S.regularize(keys.slice(-KEEP - 300).map((k) => cmap.get(k)));
    idx = new Map(closed.map((k, i) => [k[0], i]));
  }
  const closeAt = (ts) => { const i = idx.get(ts); return i == null ? null : closed[i][4]; };
  const candleAt = (ts) => (forming && forming[0] === ts ? forming : idx.has(ts) ? closed[idx.get(ts)] : null);
  const formingOk = () => forming && (!closed.length || forming[0] > closed[closed.length - 1][0]);

  // Writes the record for every closed candle this page has not handled yet.
  // Same function and same published parameters as the cloud, so the cloud
  // later stores the same numbers. Nothing already in the record is touched.
  function advance() {
    if (!closed.length || !versions.length) return;
    let wrote = false;
    for (let i = Math.max(S.WIN, 0); i < closed.length; i++) {
      const t = closed[i][0], nxt = t + GRAN;
      if (t <= doneTs) continue;
      const ver = S.versionAt(versions, nxt);
      if (!ver) continue;
      const win = closed.slice(i - S.WIN, i + 1);
      const { f, sig } = S.compact(win, nxt);
      const path = S.generatePath(ver, f, sig);
      const made = Date.now() / 1000;
      setOnce(G, nxt, { b: path[0].b, u: path[0].u, d: path[0].d, p: path[0].p, q05: path[0].q05, q95: path[0].q95, made });
      if (path[AHEAD - 1]) { const q = path[AHEAD - 1]; setOnce(K, t + AHEAD * GRAN, { o: q.o, b: q.b, u: q.u, d: q.d, made }); }
      if (ver.R) {
        for (const side of [1, -1]) {
          const probs = S.revProbs(ver.R, S.revFeatures(win, f, sig, side));
          let j = 0;
          probs.forEach((p, k) => { if (p > probs[j]) j = k; });
          if (probs[j] < ver.rt) continue;
          const forTs = t + j * GRAN;                   // j = 0: the candle that just closed
          if ([-2, -1, 0, 1, 2].some((d) => R.has(`${forTs + d * GRAN}|${side}`))) continue;      // already called
          const known = win.slice(-(RK - j + 1)).map((k) => (side > 0 ? k[2] : k[3]));
          R.set(`${forTs}|${side}`, { made: nxt, for: forTs, side, p: probs[j], level: side > 0 ? Math.max(...known) : Math.min(...known), hit: null });
        }
      }
      doneTs = t;
      wrote = true;
    }
    if (wrote) saveRecord();
  }
  function genBar(ts) {
    const g = G.get(ts), p = closeAt(ts - GRAN);
    if (!g || p == null) return null;
    const c = p * Math.exp(g.b);
    return { o: p, c, h: Math.max(p, c) * Math.exp(g.u), l: Math.min(p, c) * Math.exp(-g.d),
             q05: p * Math.exp(g.q05), q95: p * Math.exp(g.q95), g };
  }
  function lockBar(ts) {
    const g = K.get(ts), p = closeAt(ts - AHEAD * GRAN);     // the close it was made from, five minutes earlier
    if (!g || p == null) return null;
    const o = p * Math.exp(g.o), c = o * Math.exp(g.b);
    return { o, c, h: Math.max(o, c) * Math.exp(g.u), l: Math.min(o, c) * Math.exp(-g.d), g, from: p };
  }
  // overlap of a generated candle (given as a drawn bar) with the real candle
  function scoreBar(b, k) {
    if (!b || !k) return null;
    return S.candleScore({ b: Math.log(b.c / b.o), u: Math.log(b.h / Math.max(b.o, b.c)), d: Math.log(Math.min(b.o, b.c) / b.l) },
      Math.log(k[1] / b.o), Math.log(k[4] / b.o), Math.log(k[2] / b.o), Math.log(k[3] / b.o));
  }
  function callOutcome(c) {                 // true / false once the candles around it are known, else null
    if (c.hit != null) return !!c.hit;
    const i = idx.get(c.for);
    if (i == null) return null;
    const v = [-1, 0, 1].map((d) => S.isSwing(closed, i + d, c.side));
    if (v.some((x) => x === null)) return null;
    return v.some((x) => x === true);
  }

  // ---------------------------------------------------------------- rendering
  function renderAll() {
    const bars = closed.slice(-KEEP);
    const all = formingOk() ? bars.concat([forming]) : bars;
    realS.setData(all.map((k) => ({ time: toChart(k[0]), open: k[1], high: k[2], low: k[3], close: k[4] })));
    const g = [], hi = [], lo = [], sc = [], lk = [], d1 = [], d0 = [], m1 = [], m0 = [];
    const dotCol = (x) => (x > 0 ? C.up : x < 0 ? C.down : C.mute);
    for (const k of all) {
      const t = toChart(k[0]), b = genBar(k[0]), isClosed = k !== forming;
      const q = lockBar(k[0]);
      if (q) lk.push({ time: t, open: q.o, high: q.h, low: q.l, close: q.c });
      if (!b) continue;
      g.push({ time: t, open: b.o, high: b.h, low: b.l, close: b.c });
      hi.push({ time: t, value: b.q95 });
      lo.push({ time: t, value: b.q05 });
      const v = pct(scoreBar(b, k).score);
      sc.push({ time: t, value: v, color: scoreColor(v) });
      d1.push({ time: t, value: 1 }); m1.push({ time: t, position: "inBar", shape: "circle", size: 0.4, color: dotCol(b.g.b) });
      if (isClosed) { d0.push({ time: t, value: 0 }); m0.push({ time: t, position: "inBar", shape: "circle", size: 0.4, color: dotCol(k[4] - b.o) }); }
    }
    if (all.length) {                                       // minutes that have not started: only the fixed record reaches there
      const last = all[all.length - 1][0];
      for (let h = 1; h <= AHEAD; h++) { const q = lockBar(last + h * GRAN); if (q) lk.push({ time: toChart(last + h * GRAN), open: q.o, high: q.h, low: q.l, close: q.c }); }
    }
    genS.setData(g); hiS.setData(hi); loS.setData(lo); lockS.setData(lk); scoreS.setData(sc);
    dotModelS.setData(d1); dotModelS.setMarkers(m1); dotRealS.setData(d0); dotRealS.setMarkers(m0);
    renderCalls(all);
    applyToggles();
    renderNext();
    renderSession();
    placeOverlays();
  }
  function renderCalls(all) {
    if (!all.length) return;
    const from = all[0][0], pts = new Map(), marks = [];
    const calls = [...R.values()].filter((c) => c.for >= from).sort((a, b) => a.for - b.for || b.side - a.side);
    for (const c of calls) {
      const out = callOutcome(c);
      if (!pts.has(c.for)) pts.set(c.for, c.level);
      marks.push({ time: toChart(c.for), position: c.side > 0 ? "aboveBar" : "belowBar", shape: c.side > 0 ? "arrowDown" : "arrowUp",
        color: out === null ? C.warn : out ? C.up : C.down, text: out === null ? Math.round(c.p * 100) + "%" : out ? "✓" : "✗" });
    }
    revS.setData([...pts].map(([t, v]) => ({ time: toChart(t), value: v })));
    revS.setMarkers(marks);
  }
  const TOGGLES = ["t-real", "t-gen", "t-lock", "t-band", "t-score", "t-dots", "t-rev"];
  function applyToggles() {
    const on = (id) => $(id).checked;
    realS.applyOptions({ visible: on("t-real") });
    genS.applyOptions({ visible: on("t-gen") });
    lockS.applyOptions({ visible: on("t-lock") });
    hiS.applyOptions({ visible: on("t-band") }); loS.applyOptions({ visible: on("t-band") });
    scoreS.applyOptions({ visible: on("t-score") });
    dotModelS.applyOptions({ visible: on("t-dots") }); dotRealS.applyOptions({ visible: on("t-dots") });
    revS.applyOptions({ visible: on("t-rev") });
    try { localStorage.setItem("candle-generator-toggles", JSON.stringify(Object.fromEntries(TOGGLES.map((id) => [id, on(id)])))); } catch (e) { /* ignore */ }
    placeOverlays();
  }
  function renderForming() {
    if (!formingOk()) return;
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
    if (y == null || !w) cd.hidden = true;
    else {
      const left = Math.max(0, Math.ceil(forming[0] + GRAN - Date.now() / 1000));
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
    if (!forming) { box.append(el("p", "muted", "waiting for the market feed…")); return; }
    const b = genBar(forming[0]);
    if (!b) {
      box.append(el("p", "muted", versions.length ? "collecting candles before the first generated one…" : "waiting for the model…"));
      return;
    }
    const up = b.g.b >= 0;
    const dir = el("div", "dir " + (up ? "up" : "down"));
    dir.append(el("span", "arrow", up ? "▲ up" : "▼ down"), el("span", "p", `P(up) ${(b.g.p * 100).toFixed(1)}%`));
    const dl = el("dl", "kv");
    kv(dl, "opens at", fmtP(b.o));
    kv(dl, "generated close", `${fmtP(b.c)}  (${(b.g.b * 1e4).toFixed(1)} bp)`);
    kv(dl, "generated high / low", `${fmtP(b.h)} / ${fmtP(b.l)}`);
    kv(dl, "90% range for the close", `${fmtP(b.q05)} – ${fmtP(b.q95)}`);
    box.append(dir, dl);
    const s = scoreBar(b, forming);
    const ls = el("div", "livescore");
    ls.append("match so far this minute: ", el("b", null, s ? pct(s.score) + "/100" : "–"));
    box.append(ls);
    const ul = el("ol", "ahead");
    for (let h = 0; h <= AHEAD; h++) {
      const ts = forming[0] + h * GRAN, q = lockBar(ts);
      if (!q) continue;
      const li = el("li", q.c >= q.o ? "up" : "down");
      li.append(el("span", "when", fmtT(ts)), el("span", "arrow", q.c >= q.o ? "▲" : "▼"),
        el("span", null, `${fmtP(q.o)} → ${fmtP(q.c)}`), el("span", "muted", `${fmtP(q.l)} – ${fmtP(q.h)}`));
      ul.append(li);
    }
    if (ul.children.length) box.append(el("p", "muted small", "fixed record for the coming minutes — open → close, low – high. Written once, never redrawn:"), ul);
    const pend = [...R.values()].filter((c) => c.for >= forming[0]).sort((a, b) => a.for - b.for);
    if (pend.length) {
      const pl = el("ol", "ahead");
      for (const c of pend) {
        const li = el("li", c.side > 0 ? "down" : "up");
        li.append(el("span", "when", fmtT(c.for)), el("span", "arrow", c.side > 0 ? "▼" : "▲"),
          el("span", null, (c.side > 0 ? "top near " : "bottom near ") + fmtP(c.level)), el("span", "muted", Math.round(c.p * 100) + "%"));
        pl.append(li);
      }
      box.append(el("p", "muted small", "reversal calls ahead:"), pl);
    }
  }
  function renderSession() {
    let n = 0, sum = 0, dirOk = 0, dirN = 0, ln = 0, lsum = 0;
    for (const k of closed.slice(-KEEP)) {
      const b = genBar(k[0]), s = scoreBar(b, k);
      if (s) { n++; sum += s.score; if (k[4] !== b.o) { dirN++; if ((b.g.b > 0) === (k[4] > b.o)) dirOk++; } }
      const q = scoreBar(lockBar(k[0]), k);
      if (q) { ln++; lsum += q.score; }
    }
    $("chartnote").textContent = n
      ? `On this chart: ${n} candles generated 1 minute ahead, average match ${(100 * sum / n).toFixed(0)}/100, colour right ${(100 * dirOk / Math.max(dirN, 1)).toFixed(1)}%` +
        (ln ? `; ${ln} locked 5 minutes ahead, average match ${(100 * lsum / ln).toFixed(0)}/100 at their real price level.` : ".") + " Click or tap any candle or bar for its numbers."
      : "Generated candles appear here as soon as the model's parameters and 4 hours of candles are loaded.";
  }
  function renderCloud() {
    if (!cloud) return;
    const tb = $("score").tBodies[0];
    tb.replaceChildren();
    const pc = (x) => (100 * x).toFixed(1);
    for (const [name, w] of Object.entries(cloud.windows || {})) {
      const s = w.student;
      if (!s) continue;
      const tr = el("tr");
      const typ = w.baseline.typical.score, rep = w.baseline.repeat.score;
      tr.append(el("td", null, name), el("td", "model" + (s.score < typ ? " behind" : ""), pc(s.score)),
        el("td", null, pc(typ)), el("td", null, pc(rep)),
        el("td", null, s.dir_acc == null ? "–" : (s.dir_acc * 100).toFixed(1) + "%"),
        el("td", null, w.locked ? pc(w.locked.score) : "–"));
      tb.append(tr);
    }
    const d = (cloud.windows || {})["24h"];
    $("scorenote").textContent = d
      ? `Last 24h: the 90% range held ${(d.cov90 * 100).toFixed(1)}% of closes, the 50% range ${(d.cov50 * 100).toFixed(1)}%. "typical" and "repeat" are naive generators the model has to beat. "locked" is the fixed record, compared at its real price level` +
        (d.locked ? ` (its close misses by ${d.locked.median_miss_bp.toFixed(1)} bp, typically).` : ".")
      : "";
    const ab = $("ahead").tBodies[0];
    ab.replaceChildren();
    for (const [h, a] of Object.entries((d && d.ahead) || {})) {
      const tr = el("tr");
      tr.append(el("td", null, h === "1" ? "1 minute" : h + " minutes"), el("td", "model", pc(a.score)),
        el("td", null, a.dir_acc == null ? "–" : (a.dir_acc * 100).toFixed(1) + "%"),
        el("td", null, h === "1" ? (d.cov90 * 100).toFixed(1) + "%" : a.cone90 == null ? "–" : (a.cone90 * 100).toFixed(1) + "%"));
      ab.append(tr);
    }
    const lf = $("learning");
    lf.replaceChildren();
    const L = cloud.learning;
    if (L) {
      kv(lf, "candles learned from", L.candles_learned.toLocaleString("en-US"));
      kv(lf, "sizing learned from the score", `body ×${L.body_scale}, reach ×${L.reach_scale}`);
      if (L.last_contest) kv(lf, "last tree-model contest", L.last_contest.promoted ? "new model won" : "old model kept");
      kv(lf, "generator versions published", String(L.versions_published));
    }
    const rv = cloud.reversal, rt = $("rev").tBodies[0], rf = $("revfacts");
    rt.replaceChildren(); rf.replaceChildren();
    if (rv) {
      for (const [name, w] of Object.entries(rv.windows || {})) {
        if (w.hit_rate == null) continue;
        const tr = el("tr");
        tr.append(el("td", null, name), el("td", null, String(w.n)),
          el("td", "model" + (w.naive_rule != null && w.hit_rate < w.naive_rule ? " behind" : ""), (w.hit_rate * 100).toFixed(1) + "%"),
          el("td", null, w.naive_rule == null ? "–" : (w.naive_rule * 100).toFixed(1) + "%"), el("td", null, (w.chance * 100).toFixed(1) + "%"));
        rt.append(tr);
      }
      kv(rf, "swing labels learned from", rv.labels_learned.toLocaleString("en-US"));
      kv(rf, "model mix", Object.entries(rv.weights).map(([k, v]) => `${k} ${(v * 100).toFixed(0)}%`).join(", "));
      if (rv.brier_skill != null) kv(rf, "probability skill vs chance", (rv.brier_skill * 100).toFixed(1) + "%");
      kv(rf, "call threshold (self-set)", (rv.threshold * 100).toFixed(0) + "%");
    }
    const wbox = $("weights");
    wbox.replaceChildren();
    const ws = Object.entries((cloud.next && cloud.next.weights) || {}).sort((a, b) => b[1] - a[1]);
    const wmax = Math.max(...ws.map((x) => x[1]), 0.01);
    for (const [name, w] of ws) {
      const row = el("div", "wrow"), bar = el("span", "bar"), fill = el("i");
      fill.style.width = (100 * w / wmax).toFixed(1) + "%";
      bar.append(fill);
      row.append(el("span", null, name), bar, el("span", null, (w * 100).toFixed(0) + "%"));
      wbox.append(row);
    }
    const rg = $("regime");
    rg.replaceChildren();
    if (cloud.next) {
      kv(rg, "regime change (last 12 min)", (cloud.next.changepoint_prob * 100).toFixed(1) + "%");
      kv(rg, "current regime age", Math.round(cloud.next.regime_age_min) + " min");
    }
    if (cloud.hmm) {
      const i = cloud.hmm.state_prob.indexOf(Math.max(...cloud.hmm.state_prob));
      kv(rg, "volatility state", ["calm", "normal", "turbulent"][i] + ` (${(cloud.hmm.state_prob[i] * 100).toFixed(0)}%)`);
    }
    const last = (cloud.retrain_log || []).slice(-1)[0];
    if (last) kv(rg, "last self-retrain", fmtT(last.ts) + ", " + new Date(last.ts * 1000).toLocaleDateString());
    const al = $("alerts");
    al.replaceChildren();
    if (!(cloud.alerts || []).length) al.append(el("li", "ok", "on track: no alerts from the last cloud run"));
    for (const a of cloud.alerts || []) al.append(el("li", null, a));
  }
  function renderFeeds() {
    const now = Date.now() / 1000;
    const m = $("feed-market"), c = $("feed-cloud");
    const fresh = now - lastTradeAt < 20;
    m.className = "feed " + (fresh ? "ok" : lastTradeAt ? "warn" : "bad");
    m.lastChild.textContent = fresh ? (wsOpen ? "market feed: live" : "market feed: polling") : lastTradeAt ? "market feed: quiet" : "market feed: not connected";
    const age = cloud ? (now - cloud.generated) / 60 : null;
    c.className = "feed " + (age == null ? "bad" : age < 30 ? "ok" : "warn");
    c.lastChild.textContent = age == null ? "model cloud: no data yet"
      : age < 90 ? `model cloud: learned ${Math.max(0, Math.round(age))} min ago` : `model cloud: learned ${(age / 60).toFixed(1)} h ago`;
    if (forming) {
      const left = Math.max(0, forming[0] + GRAN - now);
      $("clock").textContent = `closes in ${Math.ceil(left)}s`;
      $("progress").style.width = (100 * (1 - left / GRAN)).toFixed(1) + "%";
    }
  }

  // ---------------------------------------------------------------- market feed
  function roll(bucket, firstPrice) {
    const missed = (bucket - forming[0]) / GRAN > 1;          // tab was asleep: fetch those minutes instead of guessing
    if (!cmap.has(forming[0])) cmap.set(forming[0], forming);
    const c = forming[4], p = firstPrice != null ? firstPrice : c;
    forming = [bucket, p, p, p, p, 0];
    rebuild();
    if (missed) { syncExchange().catch(() => {}); return; }
    advance();
    renderAll();
  }
  function onTrade(price, size, t) {
    if (!(price > 0)) return;
    lastTradeAt = Date.now() / 1000;
    const bucket = Math.floor(t / GRAN) * GRAN;
    if (!forming) {
      if (!closed.length) return;
      const c = closed[closed.length - 1];
      forming = [c[0] + GRAN, c[4], c[4], c[4], c[4], 0];
    }
    if (bucket < forming[0]) return;                        // late print for a minute that is already closed
    if (bucket > forming[0]) roll(bucket, size > 0 ? price : null);
    if (forming[5] === 0 && size > 0) forming[1] = forming[2] = forming[3] = price;   // first trade sets the open
    forming[2] = Math.max(forming[2], price);
    forming[3] = Math.min(forming[3], price);
    forming[4] = price;
    forming[5] += size;
    dirty = true;
  }
  let ws = null;
  function connect() {
    try { ws = new WebSocket(WSS); } catch (e) { return; }
    ws.onopen = () => { wsOpen = true; ws.send(JSON.stringify({ type: "subscribe", product_ids: [product], channels: ["matches", "heartbeat"] })); };
    ws.onmessage = (ev) => {
      let m; try { m = JSON.parse(ev.data); } catch (e) { return; }
      if (m.type === "match" || m.type === "last_match") onTrade(+m.price, m.type === "match" ? +m.size : 0, Date.parse(m.time) / 1000);
    };
    ws.onclose = () => { wsOpen = false; setTimeout(connect, 3000); };
    ws.onerror = () => { try { ws.close(); } catch (e) { /* ignore */ } };
  }
  async function getJSON(url, bust) {
    const r = await fetch(bust ? url + (url.includes("?") ? "&" : "?") + "t=" + Math.floor(Date.now() / 30000) : url, { cache: "no-store" });
    if (!r.ok) throw new Error(url + " -> " + r.status);
    return r.json();
  }
  // official exchange candles: fill everything since the cloud's last run and
  // correct anything this page built from the trade stream
  async function syncExchange() {
    const now = Date.now() / 1000;
    let newest = null;
    const take = (rows) => {
      for (const r of rows) {                               // [time, low, high, open, close, volume]
        const k = [r[0], r[3], r[2], r[1], r[4], r[5]];
        if (k[0] + GRAN <= now) cmap.set(k[0], k);
        else newest = k;
      }
    };
    take(await getJSON(`${API}/products/${product}/candles?granularity=${GRAN}`));
    // the cloud may be hours behind: page back until its candles are reached (at most 15 hours)
    const have = cloud ? cloud.last_ts : 0;
    let oldest = Math.min(...[...cmap.keys()].filter((k) => k > now - 300 * GRAN), now);
    for (let page = 0; page < 3 && have && oldest - GRAN > have; page++) {
      const end = oldest - GRAN, start = end - 299 * GRAN;
      const iso = (t) => new Date(t * 1000).toISOString();
      const rows = await getJSON(`${API}/products/${product}/candles?granularity=${GRAN}&start=${iso(start)}&end=${iso(end)}`);
      if (!rows.length) break;
      take(rows);
      oldest = start;
    }
    rebuild();
    const c = closed.length ? closed[closed.length - 1] : null;
    if (c && (!forming || forming[0] <= c[0])) forming = newest && newest[0] === c[0] + GRAN ? newest : [c[0] + GRAN, c[4], c[4], c[4], c[4], 0];
    if (!wsOpen) lastTradeAt = now;
    advance();
    renderAll();
    renderForming();
  }
  async function pollTicker() {                              // fallback when the websocket is blocked
    if (wsOpen && Date.now() / 1000 - lastTradeAt < 15) return;
    try {
      const t = await getJSON(`${API}/products/${product}/ticker`);
      onTrade(+t.price, 0, Date.now() / 1000);
    } catch (e) { /* next round */ }
  }
  async function syncCloud() {
    const [latest, params] = await Promise.all([getJSON(DATA + "/latest.json", true), getJSON(DATA + "/params.json", true)]);
    const first = !cloud;
    cloud = latest;
    if (first) {
      product = cloud.product || product;
      $("product").textContent = product;
      document.title = `${product} · candle generator`;
      loadRecord();                                         // what this browser already showed stays as it was
    }
    versions = params.versions || [];
    const now = Date.now() / 1000;
    for (const k of latest.candles || []) if (k[0] + GRAN <= now) cmap.set(k[0], k);
    for (const g of latest.gen || []) setOnce(G, g[0], { b: g[1], u: g[2], d: g[3], p: g[4], q05: g[5], q95: g[8] });
    for (const g of latest.locked || []) setOnce(K, g[0], { o: g[1], b: g[2], u: g[3], d: g[4] });
    for (const c of latest.rev_calls || []) {
      const key = `${c[1]}|${c[2]}`, cur = R.get(key);
      if (!cur) R.set(key, { made: c[0], for: c[1], side: c[2], p: c[3], level: c[4], hit: c[5] });
      else if (cur.hit == null && c[5] != null) cur.hit = c[5];       // only the outcome may be filled in
    }
    doneTs = Math.max(doneTs, latest.last_ts || 0);
    rebuild();
    const c = closed.length ? closed[closed.length - 1] : null;
    if (c && (!forming || forming[0] <= c[0])) forming = [c[0] + GRAN, c[4], c[4], c[4], c[4], 0];
    advance();
    renderCloud();
    renderAll();
  }

  // ---------------------------------------------------------------- readout (hover) and inspector (click / tap)
  function ohlc(parent, tag, o, h, l, c, extra) {
    parent.append(el("span", "tag", tag));
    const v = el("span");
    v.append((c >= o ? "▲ " : "▼ "), "O ", el("b", null, fmtP(o)), "  H ", el("b", null, fmtP(h)), "  L ", el("b", null, fmtP(l)), "  C ", el("b", null, fmtP(c)), extra || "");
    parent.append(v);
  }
  function readout(ts) {
    const box = $("readout");
    box.replaceChildren();
    const k = candleAt(ts), b = genBar(ts), q = lockBar(ts);
    if (k) ohlc(box, fmtT(ts) + " real", k[1], k[2], k[3], k[4]);
    const s = scoreBar(b, k), sq = scoreBar(q, k);
    if (b) ohlc(box, "generated", b.o, b.h, b.l, b.c, s ? `   match ${pct(s.score)}/100` : "");
    if (q) ohlc(box, k ? "locked" : fmtT(ts) + " locked", q.o, q.h, q.l, q.c, sq ? `   match ${pct(sq.score)}/100` : k ? "" : "   not started yet");
  }
  let pinned = null;
  function inspect(ts, point) {
    const box = $("inspector"), k = candleAt(ts), b = genBar(ts), q = lockBar(ts);
    if (!k && !b && !q) { box.hidden = true; pinned = null; return; }
    pinned = ts;
    box.replaceChildren();
    const head = el("div", "ihead");
    const x = el("button", "iclose", "×");
    x.setAttribute("aria-label", "Close");
    x.addEventListener("click", () => { box.hidden = true; pinned = null; });
    head.append(el("strong", null, new Date(ts * 1000).toLocaleString([], { hour: "2-digit", minute: "2-digit", month: "short", day: "numeric" })), x);
    box.append(head);
    const s = scoreBar(b, k), sq = scoreBar(q, k);
    if (s) {
      const big = el("div", "ibig");
      const num = el("span", "num", pct(s.score) + "%");
      num.style.color = scoreColor(pct(s.score));
      big.append(num, el("span", "muted", k === forming ? " match so far (candle still open)" : " match of the generated candle"));
      box.append(big);
    }
    const dl = el("dl", "kv");
    if (s) {
      kv(dl, "body overlap / range overlap", `${Math.round(100 * s.body)}% / ${Math.round(100 * s.range)}%`);
      const mUp = b.g.b >= 0, rUp = k[4] > b.o, flat = k[4] === b.o;
      kv(dl, "colour: model → market", `${mUp ? "green" : "red"} → ${flat ? "unchanged" : rUp ? "green" : "red"}  ${flat ? "" : mUp === rUp ? "✓ right" : "✗ wrong"}`);
      kv(dl, "model's P(up)", (b.g.p * 100).toFixed(1) + "%");
    }
    if (k) kv(dl, "real  O H L C", `${fmtP(k[1])}  ${fmtP(k[2])}  ${fmtP(k[3])}  ${fmtP(k[4])}`);
    if (b) {
      kv(dl, "generated  O H L C", `${fmtP(b.o)}  ${fmtP(b.h)}  ${fmtP(b.l)}  ${fmtP(b.c)}`);
      kv(dl, "90% range for the close", `${fmtP(b.q05)} – ${fmtP(b.q95)}` + (k && k !== forming ? (k[4] >= b.q05 && k[4] <= b.q95 ? "  ✓ held" : "  ✗ missed") : ""));
      if (k && k !== forming) kv(dl, "close missed by", `${fmtP(Math.abs(k[4] - b.c))}  (${(Math.abs(Math.log(k[4] / b.c)) * 1e4).toFixed(1)} bp)`);
    }
    if (q) {
      kv(dl, "locked 5 min ahead  O H L C", `${fmtP(q.o)}  ${fmtP(q.h)}  ${fmtP(q.l)}  ${fmtP(q.c)}`);
      kv(dl, "locked: made from the close", fmtP(q.from) + " at " + fmtT(ts - AHEAD * GRAN));
      if (sq) kv(dl, "locked: match at real price level", pct(sq.score) + "%");
    }
    for (const side of [1, -1]) {
      const c = R.get(`${ts}|${side}`);
      if (!c) continue;
      const out = callOutcome(c);
      kv(dl, `reversal call: ${side > 0 ? "top" : "bottom"} near ${fmtP(c.level)}`,
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
  let hovering = false;
  chart.subscribeCrosshairMove((p) => {
    hovering = !!(p && p.time != null);
    if (hovering) readout(fromChart(p.time));
    else if (forming) readout(forming[0]);
  });
  chart.subscribeClick((p) => {
    if (!p || p.time == null) { $("inspector").hidden = true; pinned = null; return; }
    inspect(fromChart(p.time), p.point);
  });
  chart.timeScale().subscribeVisibleLogicalRangeChange(placeOverlays);
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") { $("inspector").hidden = true; pinned = null; } });
  try {
    const t = JSON.parse(localStorage.getItem("candle-generator-toggles") || "{}");
    for (const id of TOGGLES) if (typeof t[id] === "boolean") $(id).checked = t[id];
  } catch (e) { /* defaults */ }
  for (const id of TOGGLES) $(id).addEventListener("change", applyToggles);

  // ---------------------------------------------------------------- loops
  setInterval(() => {                                          // once a second, exactly like the market clock
    const now = Date.now() / 1000;
    if (forming && Math.floor(now / GRAN) * GRAN > forming[0]) roll(Math.floor(now / GRAN) * GRAN, null);
    if (dirty || forming) { renderForming(); dirty = false; }
    if (forming && !hovering) readout(forming[0]);
    if (pinned != null && forming && pinned === forming[0]) inspect(pinned);
    renderFeeds();
    if (forming && Math.floor(now) % 5 === 0) renderNext();
  }, 1000);
  setInterval(pollTicker, 2000);
  setInterval(() => syncExchange().catch(() => {}), 30000);
  setInterval(() => syncCloud().catch(() => {}), 60000);

  document.addEventListener("visibilitychange", () => {
    if (!document.hidden) { syncExchange().catch(() => {}); syncCloud().catch(() => {}); }
  });

  (async () => {
    await syncCloud().catch((e) => console.warn("cloud data not available yet", e));
    await syncExchange().catch((e) => console.warn("exchange not reachable", e));
    connect();
    renderFeeds();
    if (forming) readout(forming[0]);
  })();
})();
