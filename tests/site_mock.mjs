// A stand-in for the exchange and for the `state` branch, to check the site end to end:
//   node tests/site_mock.mjs <docs dir> <live dir> [minutes the cloud is behind] [port]
// It serves the page, the cloud's files (shifted in time so that they end a few minutes ago),
// an exchange REST API with a random-walk market, and the trade stream. /truth returns the
// candles exactly as this "exchange" defines them, so a test can compare what the page drew.
// /ctl?drop=N drops the next N trades from the stream, ?partial=0 hides the candle in
// progress from the REST API, ?lag=S publishes a closed minute S seconds late.
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const { WebSocketServer } = require("ws");
const DOCS = path.resolve(process.argv[2]), LIVE = process.argv[3], LAG_MIN = +(process.argv[4] || 8), PORT = +(process.argv[5] || 8765);
const GRAN = 60, SEG = 900;
const now = () => Date.now() / 1000;
const read = (n) => JSON.parse(fs.readFileSync(path.join(LIVE, n)));
const latest = read("latest.json"), params = read("params.json");
const head = fs.existsSync(path.join(LIVE, "head.json")) ? read("head.json") : null;     // absent in the old file format
const D = Math.round((Math.floor(now() / SEG) * SEG - LAG_MIN * 60 - latest.last_ts) / SEG) * SEG;      // keeps the quarter hours aligned
latest.last_ts += D; latest.generated = latest.last_ts + 90; if (latest.live_since) latest.live_since += D;
latest.candles.forEach((k) => (k[0] += D)); latest.gen.forEach((g) => (g[0] += D)); (latest.locked || []).forEach((g) => (g[0] += D));
for (const r of Object.values(latest.rev || {})) { r.calls.forEach((c) => { c[0] += D; c[1] += D; }); r.probs.forEach((p) => (p[0] += D)); }
if (latest.path) latest.path.origin += D;
(latest.retrain_log || []).forEach((e) => (e.ts += D));
params.versions.forEach((v) => (v.eff += D));
if (head) { head.generated = latest.generated; head.last_ts = latest.last_ts; head.eff = params.versions.map((v) => v.eff); }

const ctl = { drop: 0, partial: 1, lag: 0 };
const candles = new Map(latest.candles.map((k) => [k[0], k.slice()]));
let price = latest.candles[latest.candles.length - 1][4], tradeId = 1000;
let seed = 12345; const rnd = () => { seed = (seed * 1103515245 + 12345) % 2147483648; return seed / 2147483648; };
const gauss = () => Math.sqrt(-2 * Math.log(rnd() + 1e-12)) * Math.cos(2 * Math.PI * rnd());
function trade(t) {
  price = Math.round(price * Math.exp(gauss() * 0.00012) * 100) / 100;
  const b = Math.floor(t / GRAN) * GRAN, size = Math.round((0.01 + rnd() * 3) * 100) / 100;
  const k = candles.get(b);
  if (!k) candles.set(b, [b, price, price, price, price, size]);
  else { k[2] = Math.max(k[2], price); k[3] = Math.min(k[3], price); k[4] = price; k[5] = Math.round((k[5] + size) * 1e6) / 1e6; }
  return { type: "match", trade_id: ++tradeId, price: String(price), size: String(size), time: new Date(t * 1000).toISOString(), product_id: "ETH-USD" };
}
for (let t = latest.last_ts + GRAN; t < now(); t += 1.7) trade(t);
const types = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".json": "application/json" };
http.createServer((req, res) => {
  const u = new URL(req.url, "http://x");
  res.setHeader("Access-Control-Allow-Origin", "*");
  const json = (o) => { res.setHeader("Content-Type", "application/json"); res.end(JSON.stringify(o)); };
  if (u.pathname === "/ctl") { for (const [k, v] of u.searchParams) ctl[k] = +v; return json(ctl); }
  if (u.pathname === "/truth") return json([...candles.values()].sort((a, b) => a[0] - b[0]));
  if (u.pathname === "/live/latest.json") return json(latest);
  if (u.pathname === "/live/params.json") return json(params);
  if (u.pathname === "/live/head.json" && head) return json(head);
  if (u.pathname.startsWith("/live/") && fs.existsSync(path.join(LIVE, path.basename(u.pathname)))) return json(read(path.basename(u.pathname)));
  if (u.pathname.endsWith("/candles")) {
    const t = now(), cur = Math.floor(t / GRAN) * GRAN;
    let keys = [...candles.keys()].sort((a, b) => b - a);
    if (u.searchParams.get("end")) { const e = Date.parse(u.searchParams.get("end")) / 1000, s = Date.parse(u.searchParams.get("start")) / 1000; keys = keys.filter((k) => k >= s && k <= e); }
    keys = keys.filter((k) => (k === cur ? ctl.partial : true) && !(k === cur - GRAN && t - cur < ctl.lag)).slice(0, 300);
    return json(keys.map((k) => { const c = candles.get(k); return [c[0], c[3], c[2], c[1], c[4], c[5]]; }));
  }
  if (u.pathname.endsWith("/ticker")) return json({ price: String(price) });
  const f = path.join(DOCS, u.pathname === "/" ? "index.html" : u.pathname);
  if (!f.startsWith(DOCS) || !fs.existsSync(f)) { res.statusCode = 404; return res.end("nf"); }
  res.setHeader("Content-Type", types[path.extname(f)] || "application/octet-stream");
  res.end(fs.readFileSync(f));
}).listen(PORT);
const wss = new WebSocketServer({ port: PORT + 1 });
wss.on("connection", (ws) => ws.on("message", () => {
  ws.send(JSON.stringify({ type: "subscriptions", channels: [] }));
  ws.send(JSON.stringify({ type: "last_match", trade_id: tradeId, price: String(price), size: "0.1", time: new Date().toISOString() }));
}));
setInterval(() => {
  const m = JSON.stringify(trade(now()));
  if (ctl.drop > 0) { ctl.drop--; return; }
  wss.clients.forEach((c) => c.send(m));
}, 350);
setInterval(() => wss.clients.forEach((c) => c.send(JSON.stringify({ type: "heartbeat", time: new Date().toISOString() }))), 1000);
console.log("mock up on", PORT, "shift", D, "cloud last", new Date(latest.last_ts * 1000).toISOString());
