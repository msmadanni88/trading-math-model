// Live page: real candles from the exchange feed (updated on every trade),
// generated candles from the model, overlaid on the same chart.
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
  const KEEP = 900;                       // candles kept on the chart
  const $ = (id) => document.getElementById(id);
  const css = (v) => getComputedStyle(document.documentElement).getPropertyValue(v).trim();
  const C = { up: css("--up"), down: css("--down"), gen: css("--gen"), text: css("--text-2"), line: css("--line"), surface: css("--surface") };
  const tz = new Date().getTimezoneOffset() * 60;
  const toChart = (ts) => ts - tz;        // the chart library draws UTC; shift so the axis shows local time
  const fromChart = (t) => t + tz;
  const fmtP = (x) => x.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
  const fmtT = (ts) => new Date(ts * 1000).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" });
  const el = (tag, cls, text) => { const e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; };

  // ---------------------------------------------------------------- state
  let product = "ETH-USD";
  const cmap = new Map();                 // ts -> [ts,o,h,l,c,v] closed candles
  let closed = [];                        // regularized, ascending
  let idx = new Map();                    // ts -> index in closed
  let forming = null;                     // candle being built right now
  const official = new Map();             // for_ts -> generated candle stored by the cloud
  const live = new Map();                 // for_ts -> generated candle computed in this browser
  let versions = [];
  let cloud = null;
  let lastTradeAt = 0, wsOpen = false, cloudOkAt = 0, dirty = false, lastPrice = null;

  // ---------------------------------------------------------------- chart
  const chart = LC.createChart($("chart"), {
    autoSize: true,
    layout: { background: { color: C.surface }, textColor: C.text, fontFamily: css("--mono"), fontSize: 11 },
    grid: { vertLines: { color: "rgba(255,255,255,0.03)" }, horzLines: { color: "rgba(255,255,255,0.05)" } },
    rightPriceScale: { borderColor: C.line, scaleMargins: { top: 0.05, bottom: 0.24 } },
    timeScale: { borderColor: C.line, timeVisible: true, secondsVisible: false, rightOffset: 4, barSpacing: 13 },
    crosshair: { mode: LC.CrosshairMode.Normal },
  });
  const realS = chart.addCandlestickSeries({
    upColor: C.up, downColor: C.down, borderVisible: false, wickUpColor: C.up, wickDownColor: C.down,
    priceLineVisible: true, priceLineColor: "rgba(255,255,255,0.35)",
  });
  const bandOpt = { color: "rgba(57,135,229,0.55)", lineWidth: 1, lineStyle: LC.LineStyle.Dashed, lineType: LC.LineType.WithSteps,
    priceLineVisible: false, lastValueVisible: false, crosshairMarkerVisible: false };
  const hiS = chart.addLineSeries(bandOpt), loS = chart.addLineSeries(bandOpt);
  const genS = chart.addCandlestickSeries({
    upColor: "rgba(57,135,229,0)", downColor: "rgba(57,135,229,0.42)", borderVisible: true,
    borderUpColor: C.gen, borderDownColor: C.gen, wickUpColor: C.gen, wickDownColor: C.gen,
    priceLineVisible: false, lastValueVisible: false,
  });

  // match score of every generated candle, 1-100, drawn like a volume pane
  const scoreS = chart.addHistogramSeries({ priceScaleId: "score", priceLineVisible: false, lastValueVisible: false,
    autoscaleInfoProvider: () => ({ priceRange: { minValue: 0, maxValue: 100 } }),     // fixed 0-100 scale
    priceFormat: { type: "custom", minMove: 1, formatter: (v) => v.toFixed(0) } });
  chart.priceScale("score").applyOptions({ scaleMargins: { top: 0.82, bottom: 0 }, visible: false });
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
  const prevClose = (forTs) => { const i = idx.get(forTs - GRAN); return i == null ? null : closed[i][4]; };
  const genFor = (forTs) => official.get(forTs) || live.get(forTs) || null;

  // the generated candle for minute `forTs`, computed here with the parameter
  // version that was already published before that minute started
  function computeLive(forTs) {
    if (official.has(forTs)) return;
    const i = idx.get(forTs - GRAN);
    if (i == null || i < S.WIN) return;
    const ver = S.versionAt(versions, forTs);
    if (!ver) return;
    const { f, sig } = S.compact(closed.slice(i - S.WIN, i + 1), forTs);
    const g = S.generate(ver.W, f, sig);
    const old = live.get(forTs);
    g.eff = ver.eff; g.madeAt = old ? old.madeAt : Date.now() / 1000;
    live.set(forTs, g);
  }
  // the candles after the one being formed: generated now, from the last closed candle
  function futurePath() {
    if (!closed.length || !formingOk()) return [];
    const i = closed.length - 1, origin = closed[i][0], first = genBar(origin + GRAN);
    if (!first) return [];
    let path = null;
    if (cloud && cloud.path && cloud.path.origin === origin) {
      path = cloud.path.candles.map((c) => ({ b: c[0], u: c[1], d: c[2], p: c[3], lo: c[4], hi: c[5] }));
    } else if (i >= S.WIN) {
      const ver = S.versionAt(versions, origin + GRAN);
      if (ver && ver.H) { const { f, sig } = S.compact(closed.slice(i - S.WIN, i + 1), origin + GRAN); path = S.generatePath(ver, f, sig); }
    }
    if (!path) return [];
    const p0 = first.o, out = [];
    let open = first.c;
    for (let h = 1; h < path.length; h++) {
      const g = path[h], c = open * Math.exp(g.b);
      out.push({ ts: origin + (h + 1) * GRAN, o: open, c, h: Math.max(open, c) * Math.exp(g.u), l: Math.min(open, c) * Math.exp(-g.d),
                 lo: p0 * Math.exp(g.lo), hi: p0 * Math.exp(g.hi), g, ahead: h + 1 });
      open = c;
    }
    return out;
  }
  // every minute the cloud has not stored yet (deterministic: same inputs, same candle)
  function ensureLive() {
    if (!closed.length) return;
    const lastTs = closed[closed.length - 1][0];
    let from = lastTs - 400 * GRAN;
    for (const t of official.keys()) if (t > from) from = t;
    for (let t = from; t <= lastTs; t += GRAN) computeLive(t + GRAN);
  }
  function genBar(forTs) {
    const g = genFor(forTs), p = prevClose(forTs);
    if (!g || p == null) return null;
    const c = p * Math.exp(g.b);
    return { o: p, c, h: Math.max(p, c) * Math.exp(g.u), l: Math.min(p, c) * Math.exp(-g.d),
             q05: p * Math.exp(g.q05), q95: p * Math.exp(g.q95), g, p };
  }
  function scoreOf(k, forTs) {
    const g = genFor(forTs), p = prevClose(forTs);
    if (!g || p == null) return null;
    return S.candleScore(g, Math.log(k[1] / p), Math.log(k[4] / p), Math.log(k[2] / p), Math.log(k[3] / p));
  }

  // ---------------------------------------------------------------- rendering
  let future = [];
  function renderAll() {
    const bars = closed.slice(-KEEP);
    const all = formingOk() ? bars.concat([forming]) : bars;
    realS.setData(all.map((k) => ({ time: toChart(k[0]), open: k[1], high: k[2], low: k[3], close: k[4] })));
    const g = [], hi = [], lo = [], sc = [];
    for (const k of all) {
      const b = genBar(k[0]);
      if (!b) continue;
      g.push({ time: toChart(k[0]), open: b.o, high: b.h, low: b.l, close: b.c });
      hi.push({ time: toChart(k[0]), value: b.q95 });
      lo.push({ time: toChart(k[0]), value: b.q05 });
      const s = scoreOf(k, k[0]), v = Math.max(1, Math.round(100 * s.score));
      sc.push({ time: toChart(k[0]), value: v, color: scoreColor(v) });
    }
    future = futurePath();
    for (const b of future) {                              // candles that have not started yet
      g.push({ time: toChart(b.ts), open: b.o, high: b.h, low: b.l, close: b.c });
      hi.push({ time: toChart(b.ts), value: b.hi });
      lo.push({ time: toChart(b.ts), value: b.lo });
    }
    genS.setData(g);
    hiS.setData(hi);
    loS.setData(lo);
    scoreS.setData(sc);
    applyToggles();
    renderNext();
    renderSession();
  }
  function applyToggles() {
    realS.applyOptions({ visible: $("t-real").checked });
    genS.applyOptions({ visible: $("t-gen").checked });
    hiS.applyOptions({ visible: $("t-band").checked });
    loS.applyOptions({ visible: $("t-band").checked });
    scoreS.applyOptions({ visible: $("t-score").checked });
  }
  const formingOk = () => forming && (!closed.length || forming[0] > closed[closed.length - 1][0]);
  function renderForming() {
    if (!formingOk()) return;
    realS.update({ time: toChart(forming[0]), open: forming[1], high: forming[2], low: forming[3], close: forming[4] });
    const fs = scoreOf(forming, forming[0]);
    if (fs) { const v = Math.max(1, Math.round(100 * fs.score)); scoreS.update({ time: toChart(forming[0]), value: v, color: scoreColor(v) }); }
    const pe = $("price");
    pe.textContent = fmtP(forming[4]);
    const p = prevClose(forming[0]);
    pe.className = "price" + (p == null || forming[4] === p ? "" : forming[4] > p ? " up" : " down");
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
    if (future.length) {
      const ul = el("ol", "ahead");
      for (const f of future) {
        const li = el("li", f.g.b >= 0 ? "up" : "down");
        li.append(el("span", "when", fmtT(f.ts)), el("span", "arrow", f.g.b >= 0 ? "▲" : "▼"),
          el("span", null, fmtP(f.c)), el("span", "muted", `${fmtP(f.lo)} – ${fmtP(f.hi)}`));
        ul.append(li);
      }
      box.append(el("p", "muted small", "then, generated now for the minutes after — close, and 90% range:"), ul);
    }
    const s = scoreOf(forming, forming[0]);
    const ls = el("div", "livescore");
    ls.append("match so far this minute: ", el("b", null, s ? Math.max(1, Math.round(100 * s.score)) + "/100" : "–"),
      official.has(forming[0]) ? "  · stored by the cloud" : "  · generated in your browser at " + fmtT(b.g.madeAt || forming[0]));
    box.append(ls);
  }
  function renderSession() {
    let n = 0, sum = 0, dirOk = 0, dirN = 0;
    for (const k of closed.slice(-KEEP)) {
      const s = scoreOf(k, k[0]);
      if (!s) continue;
      n++; sum += s.score;
      const p = prevClose(k[0]), g = genFor(k[0]);
      if (k[4] !== p) { dirN++; if ((g.b > 0) === (k[4] > p)) dirOk++; }
    }
    $("chartnote").textContent = n
      ? `On this chart: ${n} generated candles, average match ${(100 * sum / n).toFixed(0)}/100, colour right ${(100 * dirOk / Math.max(dirN, 1)).toFixed(1)}%. Bars at the bottom: match of each candle, 1–100. Hover a candle for its numbers.`
      : "Generated candles appear here as soon as the model's parameters and 4 hours of candles are loaded.";
  }
  function renderCloud() {
    if (!cloud) return;
    product = cloud.product || product;
    $("product").textContent = product;
    document.title = `${product} · candle generator`;
    const tb = $("score").tBodies[0];
    tb.replaceChildren();
    for (const [name, w] of Object.entries(cloud.windows || {})) {
      const s = w.student;
      if (!s) continue;
      const tr = el("tr");
      const typ = w.baseline.typical.score, rep = w.baseline.repeat.score;
      const pc = (x) => (100 * x).toFixed(1);
      tr.append(el("td", null, name), el("td", "model" + (s.score < typ ? " behind" : ""), pc(s.score)),
        el("td", null, pc(typ)), el("td", null, pc(rep)),
        el("td", null, s.dir_acc == null ? "–" : (s.dir_acc * 100).toFixed(1) + "%"));
      tb.append(tr);
    }
    const d = (cloud.windows || {})["24h"];
    $("scorenote").textContent = d
      ? `Last 24h: the 90% range held ${(d.cov90 * 100).toFixed(1)}% of closes, the 50% range ${(d.cov50 * 100).toFixed(1)}%. "typical" and "repeat" are naive generators the model has to beat.`
      : "";
    const ab = $("ahead").tBodies[0];
    ab.replaceChildren();
    for (const [h, a] of Object.entries((d && d.ahead) || {})) {
      const tr = el("tr");
      tr.append(el("td", null, h === "1" ? "1 minute" : h + " minutes"), el("td", "model", (100 * a.score).toFixed(1)),
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
    if (cloud.student) kv(rg, "live generator versions", String(cloud.student.versions));
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
    c.className = "feed " + (age == null ? "bad" : age < 20 ? "ok" : "warn");
    c.lastChild.textContent = age == null ? "model cloud: no data yet" : `model cloud: updated ${Math.max(0, Math.round(age))} min ago`;
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
    ensureLive();
    renderAll();
    if (missed) syncExchange().catch(() => {});
  }
  function onTrade(price, size, t) {
    if (!(price > 0)) return;
    lastTradeAt = Date.now() / 1000;
    lastPrice = price;
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
  // official exchange candles: fills the gap after the cloud's last run and
  // corrects anything this page built from the trade stream
  async function syncExchange() {
    const rows = await getJSON(`${API}/products/${product}/candles?granularity=${GRAN}`);
    const now = Date.now() / 1000;
    let newest = null;
    for (const r of rows) {                                 // [time, low, high, open, close, volume]
      const k = [r[0], r[3], r[2], r[1], r[4], r[5]];
      if (k[0] + GRAN <= now) cmap.set(k[0], k);
      else newest = k;
    }
    rebuild();
    const c = closed.length ? closed[closed.length - 1] : null;
    if (c && (!forming || forming[0] <= c[0])) {
      forming = newest && newest[0] === c[0] + GRAN ? newest : [c[0] + GRAN, c[4], c[4], c[4], c[4], 0];
      lastPrice = forming[4];
    }
    if (rows.length) lastTradeAt = Math.max(lastTradeAt, wsOpen ? lastTradeAt : now);
    ensureLive();
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
    cloud = latest;
    cloudOkAt = Date.now() / 1000;
    versions = params.versions || [];
    const now = Date.now() / 1000;
    for (const k of latest.candles || []) if (k[0] + GRAN <= now) cmap.set(k[0], k);
    for (const g of latest.gen || []) {
      official.set(g[0], { b: g[1], u: g[2], d: g[3], p: g[4], q05: g[5], q25: g[6], q75: g[7], q95: g[8] });
    }
    rebuild();
    const c = closed.length ? closed[closed.length - 1] : null;
    if (c && (!forming || forming[0] <= c[0])) forming = [c[0] + GRAN, c[4], c[4], c[4], c[4], 0];
    ensureLive();
    renderCloud();
    renderAll();
  }

  // ---------------------------------------------------------------- hover readout
  function readout(ts) {
    const box = $("readout");
    box.replaceChildren();
    const k = forming && forming[0] === ts ? forming : (idx.has(ts) ? closed[idx.get(ts)] : null);
    const fut = future.find((f) => f.ts === ts);
    if (!k && fut) {
      box.append(el("span", "tag", fmtT(ts) + " generated"));
      const v = el("span");
      v.append((fut.c >= fut.o ? "▲ " : "▼ "), "O ", el("b", null, fmtP(fut.o)), "  H ", el("b", null, fmtP(fut.h)), "  L ", el("b", null, fmtP(fut.l)),
        "  C ", el("b", null, fmtP(fut.c)), `   ${fut.ahead} minutes ahead · this candle has not started yet`);
      box.append(v);
      return;
    }
    if (!k) return;
    const line = (tag, o, h, l, c, extra) => {
      box.append(el("span", "tag", tag));
      const v = el("span");
      v.append((c >= o ? "▲ " : "▼ "), "O ", el("b", null, fmtP(o)), "  H ", el("b", null, fmtP(h)), "  L ", el("b", null, fmtP(l)), "  C ", el("b", null, fmtP(c)), extra || "");
      box.append(v);
    };
    line(fmtT(ts) + " real", k[1], k[2], k[3], k[4]);
    const b = genBar(ts), s = scoreOf(k, ts);
    if (b) line("generated", b.o, b.h, b.l, b.c, s ? `   match ${Math.max(1, Math.round(100 * s.score))}/100 (body ${Math.round(100 * s.body)}, range ${Math.round(100 * s.range)})` : "");
  }
  let hovering = false;
  chart.subscribeCrosshairMove((p) => {
    hovering = !!(p && p.time != null);
    if (hovering) readout(fromChart(p.time));
    else if (forming) readout(forming[0]);
  });
  for (const id of ["t-real", "t-gen", "t-band", "t-score"]) $(id).addEventListener("change", applyToggles);

  // ---------------------------------------------------------------- loops
  setInterval(() => {                                          // once a second, exactly like the market clock
    const now = Date.now() / 1000;
    if (forming && Math.floor(now / GRAN) * GRAN > forming[0]) roll(Math.floor(now / GRAN) * GRAN, null);
    if (dirty || forming) { renderForming(); dirty = false; }
    if (forming && !hovering) readout(forming[0]);
    renderFeeds();
    if (forming && Math.floor(now) % 5 === 0) renderNext();
  }, 1000);
  setInterval(pollTicker, 2000);
  setInterval(() => syncExchange().catch(() => {}), 30000);
  setInterval(() => syncCloud().catch(() => {}), 45000);

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
