// End-to-end checks of the page against tests/site_mock.mjs (see that file):
//   node tests/site_mock.mjs docs <live dir> 8 8765 &
//   CHROME=/path/to/chrome node tests/site.mjs http://127.0.0.1:8765 [screenshot dir]
// Every check is an invariant the page must keep at all times:
//   - every closed candle equals the exchange's candle; the candle in progress has the exchange's open
//   - nothing in the record (predicted candles, fixed history, reversal calls) ever changes once written
//   - the predicted chain is connected, colours match bodies, wicks never point inwards
//   - the details card opens from a match bar and from nothing else
//   - a colour call is marked confident exactly when the published threshold says so
//   - the prediction stays in view when the width of the page changes
// including after a reload, a gap in the trade stream, a frozen tab and a dropped connection.
import { createRequire } from "node:module";
const require = createRequire(import.meta.url);
const { chromium } = require("playwright-core");
const base = process.argv[2] || "http://127.0.0.1:8765", shots = process.argv[3] || null;
const port = +new URL(base).port;
const url = `${base}/?data=${base}/live&api=${base}&ws=ws://127.0.0.1:${port + 1}`;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let failed = 0, passed = 0;
const ok = (cond, msg) => { if (cond) passed++; else { failed++; console.error("FAIL", msg); } };
const truth = async () => new Map((await (await fetch(base + "/truth")).json()).map((k) => [k[0], k]));
const ctl = (q) => fetch(base + "/ctl?" + q);
const untilSecond = async (s) => { let w = (s - (Date.now() / 1000) % 60 + 60) % 60; if (w < 0.5) w += 60; await sleep(w * 1000); };

// everything the page has drawn, as plain data
const dump = (page) => page.evaluate(() => {
  const s = window.__site.state();
  const closeAt = new Map(s.closed.map((k) => [k[0], k[4]]));
  const bars = (fn) => { const o = {}; for (const k of s.closed.slice(-400)) { const b = fn(k[0]); if (b) o[k[0]] = { o: b.o, h: b.h, l: b.l, c: b.c, n: b.g.h || 0, b: b.g.b }; } return o; };
  const fut = {};
  if (s.forming) for (let h = 0; h < s.HZ; h++) { const b = window.__site.lockBar(s.forming[0] + h * 60); if (b) fut[s.forming[0] + h * 60] = { o: b.o, c: b.c, n: b.g.h }; }
  return { closed: s.closed.slice(-400), forming: s.forming, trusted: s.trusted, HZ: s.HZ, provisional: [...s.provisional],
    G: Object.fromEntries(s.G), K: Object.fromEntries(s.K), R: Object.fromEntries(s.R),
    gen: bars(window.__site.genBar), lock: bars(window.__site.lockBar), lockFuture: fut, prevClose: Object.fromEntries(closeAt),
    chain: s.chain.map((q) => ({ ts: q.ts, o: q.o, h: q.h, l: q.l, c: q.c, b: q.g.b, lo: q.lo, hi: q.hi })),
    calls: window.__site.shownCalls(0).length, inspector: !document.getElementById("inspector").hidden,
    price: document.getElementById("price").textContent, next: document.getElementById("next").innerText.slice(0, 80) };
});

async function candlesMatch(page, label, { settle = true } = {}) {
  const d = await dump(page), T = await truth(), nowB = Math.floor(Date.now() / 60000) * 60;
  let bad = 0, n = 0;
  for (const k of d.closed) {
    const t = T.get(k[0]);
    if (!t || k[0] >= nowB) continue;
    n++;
    if (k[1] !== t[1] || k[2] !== t[2] || k[3] !== t[3] || k[4] !== t[4]) { bad++; if (bad < 4) console.error("   candle", new Date(k[0] * 1000).toISOString(), "page", k.slice(1, 5), "exchange", t.slice(1, 5)); }
  }
  ok(n > 100 && bad === 0, `${label}: ${bad} of ${n} closed candles differ from the exchange`);
  ok(d.closed.length && d.closed[d.closed.length - 1][0] === nowB - 60, `${label}: history reaches the minute before now`);
  if (settle) {
    ok(d.forming && d.forming[0] === nowB, `${label}: the candle in progress is the current minute`);
    const t = T.get(nowB);
    if (d.forming && t) {
      ok(d.forming[1] === t[1], `${label}: candle in progress opens at ${d.forming[1]}, exchange says ${t[1]}`);
      ok(d.forming[2] <= t[2] && d.forming[3] >= t[3], `${label}: candle in progress high/low inside the exchange's`);
    }
  }
  return d;
}
function shape(d, label) {
  const eq = (a, b) => Math.abs(a - b) <= 1e-12 * Math.max(Math.abs(a), Math.abs(b));
  ok(d.chain.length === d.HZ, `${label}: the predicted chain has ${d.chain.length} candles, expected ${d.HZ}`);
  d.chain.forEach((q, i) => {
    ok(q.h >= Math.max(q.o, q.c) && q.l <= Math.min(q.o, q.c), `${label}: chain candle ${i + 1} has a wick inside its body`);
    ok((q.c >= q.o) === (q.b >= 0), `${label}: chain candle ${i + 1} colour does not match its body`);
    ok(q.lo <= q.hi, `${label}: chain candle ${i + 1} range is inverted`);
    if (i) ok(q.o === d.chain[i - 1].c && q.ts === d.chain[i - 1].ts + 60, `${label}: chain candle ${i + 1} does not open where candle ${i} closed`);
  });
  if (d.chain.length && d.forming) {
    ok(d.chain[0].ts === d.forming[0], `${label}: the chain starts at the minute in progress`);
    ok(d.chain[0].o === d.prevClose[d.forming[0] - 60], `${label}: the chain starts from the last real close`);
  }
  let n = 0;
  for (const [ts, g] of Object.entries(d.gen)) {            // each past predicted candle opens at the real close before it
    n++;
    ok(g.o === d.prevClose[+ts - 60], `${label}: predicted candle ${ts} does not open at the real close before it`);
    ok((g.c >= g.o) === (g.b >= 0) && g.h >= Math.max(g.o, g.c) && g.l <= Math.min(g.o, g.c), `${label}: predicted candle ${ts} is malformed`);
  }
  ok(n > 100, `${label}: ${n} predicted candles on the chart`);
  let m = 0;
  const all = Object.assign({}, d.lock, d.lockFuture);
  for (const [ts, q] of Object.entries(all)) {              // fixed history: frozen chains, connected inside, aligned to the clock
    m++;
    ok(q.n === (+ts % 900) / 60 + 1, `${label}: fixed-history candle ${ts} has number ${q.n}`);
    const p = all[+ts - 60];
    if (q.n > 1 && p) ok(p.n === q.n - 1 && eq(q.o, p.c), `${label}: fixed-history candle ${ts} does not open where the one before closed`);
    if (q.n === 1 && d.prevClose[+ts - 60] != null) ok(eq(q.o, d.prevClose[+ts - 60]), `${label}: a frozen chain does not start from the real close`);
  }
  ok(m > 100, `${label}: ${m} fixed-history candles on the chart`);
}
function recordKept(before, after, label) {
  for (const name of ["G", "K", "R"]) {
    let n = 0, bad = 0;
    for (const [k, v] of Object.entries(before[name])) {
      n++;
      const w = after[name][k];
      const strip = (x) => { const y = Object.assign({}, x); if (name === "R") delete y.hit; return JSON.stringify(y); };
      if (!w || strip(w) !== strip(v) || (name === "R" && v.hit != null && w.hit !== v.hit)) { bad++; if (bad < 3) console.error("   changed", name, k, JSON.stringify(v), "->", JSON.stringify(w)); }
    }
    ok(n > 0 && bad === 0, `${label}: ${bad} of ${n} entries of record ${name} changed`);
  }
}

const browser = await chromium.launch({ executablePath: process.env.CHROME });
const errors = [];
async function open(viewport, extra = {}) {
  const ctx = await browser.newContext({ viewport, ...extra });
  const page = await ctx.newPage();
  page.on("pageerror", (e) => errors.push("pageerror: " + e.message));
  page.on("console", (m) => { if (m.type() === "error" && !/Failed to load resource|ERR_INTERNET_DISCONNECTED|WebSocket/.test(m.text())) errors.push("console: " + m.text()); });
  await page.goto(url);
  return { ctx, page };
}

// ---- A. load in the middle of a minute
await ctl("partial=1&lag=0&drop=0");
await untilSecond(20);
let { ctx, page } = await open({ width: 1440, height: 1000 });
await sleep(8000);
let d = await candlesMatch(page, "A load");
shape(d, "A load");
ok(d.calls > 0, "A load: reversal calls are on the chart");
ok(!d.inspector, "A load: details card is closed");
// confident colour calls: decided with the published threshold, shown in the cards
const cc = await page.evaluate(() => {
  const s = window.__site.state(), G = [...s.G.values()].filter((g) => g.p != null);
  const conf = (g) => Math.abs(g.p - 0.5), mean = (a) => a.reduce((x, y) => x + y, 0) / Math.max(a.length, 1);
  const yes = G.filter((g) => g.c >= 1), no = G.filter((g) => !g.c), strong = G.filter((g) => g.c === 2);
  const rows = [...document.querySelectorAll("#ledger tbody tr")].map((r) => r.innerText);
  return { yes: yes.length, no: no.length, strong: strong.length, cy: mean(yes.map(conf)), cn: mean(no.map(conf)),
    head: document.querySelector("#ledger thead").innerText, rows, ci: document.querySelectorAll("#ledger .ci").length,
    slices: document.querySelectorAll("#slices tbody tr").length, sliceShown: !document.getElementById("slicebox").hidden,
    badge: (document.querySelector("#next .callbadge") || {}).textContent, note: document.getElementById("chartnote").textContent };
});
ok(cc.yes > 10 && cc.no > cc.yes && cc.strong > 0 && cc.strong < cc.yes, `A: ${cc.yes} confident colour calls (${cc.strong} strong) and ${cc.no} others on the chart`);
ok(cc.cy > 1.5 * cc.cn, `A: confident calls are the ones far from 50% (${cc.cy.toFixed(4)} vs ${cc.cn.toFixed(4)})`);
ok(/today/.test(cc.head) && cc.rows.some((r) => /confident calls/.test(r)) && cc.rows.some((r) => /strong calls/.test(r)) && cc.rows.some((r) => /really moved/.test(r)), "A: the win-rate table lists the confident calls and the clear candles");
ok(cc.ci >= 10, `A: win rates carry their interval (${cc.ci})`);
ok(cc.sliceShown && cc.slices === 7, `A: the regime table has ${cc.slices} rows`);
ok(/confident call|strong call/.test(cc.badge || ""), `A: the next-candle card says whether the call is confident (${cc.badge})`);
ok(/confident and strong calls/.test(cc.note), `A: the chart note counts the confident calls (${cc.note.slice(0, 160)})`);
if (shots) await page.screenshot({ path: shots + "/site-desktop.png", fullPage: true });

// ---- B. the details card opens from a match bar only
const box = await page.locator("#chart").boundingBox();
const at = (fx, fy) => page.mouse.click(box.x + box.width * fx, box.y + box.height * fy);
await at(0.5, 0.30); await sleep(700);
ok(!(await dump(page)).inspector, "B: a click on the candles must not open the details card");
await at(0.45, 0.95); await sleep(700);
ok(!(await dump(page)).inspector, "B: a click on the colour rows must not open the details card");
await at(0.5, 0.80); await sleep(700);
ok((await dump(page)).inspector, "B: a click on a match bar opens the details card");
ok(/match of the predicted candle/.test(await page.locator("#inspector").innerText()), "B: the card shows the match");
if (shots) await page.screenshot({ path: shots + "/site-inspector.png" });
await at(0.4, 0.30); await sleep(700);
ok(!(await dump(page)).inspector, "B: a click elsewhere closes the details card");
await page.mouse.dblclick(box.x + box.width * 0.6, box.y + box.height * 0.80); await sleep(700);
ok((await dump(page)).inspector, "B: a double click on a match bar opens the details card too");
await page.keyboard.press("Escape"); await sleep(200);
ok(!(await dump(page)).inspector, "B: Escape closes the details card");

// ---- C. a minute passes: the record does not change, the new candle is exact
const before = await dump(page);
await untilSecond(8);
d = await candlesMatch(page, "C after a minute");
shape(d, "C after a minute");
recordKept(before, d, "C after a minute");
ok(d.forming[0] > before.forming[0], "C: a new minute started");
await untilSecond(8);
d = await candlesMatch(page, "C after two minutes");
recordKept(before, d, "C after two minutes");
ok(d.trusted, "C: the candle in progress was built from the complete trade stream");

// ---- D. trades go missing from the stream: nothing wrong may be kept
await untilSecond(25); await ctl("drop=12"); await sleep(6000);
await untilSecond(9);
d = await candlesMatch(page, "D after a gap in the trade stream");
shape(d, "D after a gap");
recordKept(before, d, "D after a gap");

// ---- E. reload while the exchange does not show the candle in progress and publishes closed minutes late
await ctl("partial=0&lag=3");
await untilSecond(30);
await page.reload(); await sleep(7000);
let e = await dump(page);
ok(e.forming && e.forming[0] === Math.floor(Date.now() / 60000) * 60, "E: a candle in progress is shown after the reload");
recordKept(d, e, "E after a reload");
await untilSecond(12);
e = await candlesMatch(page, "E a minute after the reload");
shape(e, "E a minute after the reload");
await ctl("partial=1&lag=0");

// ---- F. the tab is frozen for more than two minutes (phone screen off), then comes back
const cdp = await ctx.newCDPSession(page);
let frozen = true;
try { await cdp.send("Page.setWebLifecycleState", { state: "frozen" }); } catch (err) { frozen = false; console.log("  (cannot freeze the page here: skipped)"); }
if (frozen) {
  const stale = await dump(page).catch(() => null);
  await sleep(135000);
  await cdp.send("Page.setWebLifecycleState", { state: "active" });
  await page.evaluate(() => document.dispatchEvent(new Event("visibilitychange")));
  await sleep(9000);
  const f = await candlesMatch(page, "F after a frozen tab");
  shape(f, "F after a frozen tab");
  recordKept(e, f, "F after a frozen tab");
}

// ---- G. the connection drops for a while
await ctx.setOffline(true); await sleep(75000); await ctx.setOffline(false);
await sleep(14000);
d = await candlesMatch(page, "G after a dropped connection");
shape(d, "G after a dropped connection");
recordKept(e, d, "G after a dropped connection");

// ---- H. the control panel
const callsOwn = d.calls;
await page.locator("#rev-k button", { hasText: /^3$/ }).click(); await sleep(2500);
let p = await dump(page);
ok(p.calls > 0 && p.calls !== callsOwn, `H: turn size 3 shows its own calls (${p.calls} vs ${callsOwn})`);
await page.locator("#rev-auto-now").uncheck();
await page.locator("#rev-thr-now").fill("40"); await sleep(400);
const loose = (await dump(page)).calls;
await page.locator("#rev-thr-now").fill("90"); await sleep(400);
const strict = (await dump(page)).calls;
ok(loose > strict, `H: a lower confidence gives more calls (${loose} vs ${strict})`);
ok(/What-if/.test(await page.locator("#revmode").innerText()), "H: what-if mode is announced");
await page.locator("#rev-auto-now").check(); await sleep(300);
ok((await dump(page)).calls === p.calls, "H: back to the agent's own calls");
await page.locator("#rev-type button", { hasText: "turn coming" }).click(); await sleep(300);
ok((await dump(page)).calls < p.calls, "H: showing one call type hides the other");
await page.locator("#rev-type button", { hasText: "both" }).click();
await page.locator("#rev-k button", { hasText: /^5$/ }).click(); await sleep(500);
for (const id of ["t-real", "t-gen", "t-lock", "t-band", "t-score", "t-dots", "t-rev"]) { await page.locator("#" + id).uncheck(); await page.locator("#" + id).check(); }
recordKept(d, await dump(page), "H after using the panel");
if (shots) await page.screenshot({ path: shots + "/site-desktop-end.png", fullPage: true });

// ---- J. the width changes (window resized, phone rotated): the prediction stays in view
const inView = () => page.evaluate(() => {
  const s = window.__site.state(), last = s.chain[s.chain.length - 1];
  return { x: window.__site.xOf(last.ts), x0: window.__site.xOf(s.chain[0].ts), w: document.getElementById("chart").clientWidth };
});
for (const w of [900, 420, 1280, 600]) {
  await page.setViewportSize({ width: w, height: 900 }); await sleep(900);
  const v = await inView();
  ok(v.x != null && v.x0 != null && v.x0 > 0 && v.x < v.w - 30, `J: at width ${w} the predicted chain is in view (x ${Math.round(v.x0)}..${Math.round(v.x)} of ${v.w})`);
}
recordKept(d, await dump(page), "J after resizing");
await ctx.close();

// ---- I. phone: tap a bar, tap a candle
({ ctx, page } = await open({ width: 390, height: 800 }, { hasTouch: true, isMobile: true }));
await sleep(8000);
d = await candlesMatch(page, "I phone");
shape(d, "I phone");
await page.locator("#chart").scrollIntoViewIfNeeded();
const pb = await page.locator("#chart").boundingBox();
const spot = await page.evaluate(() => { const s = window.__site.state(); return { x: window.__site.xOf(s.closed[s.closed.length - 4][0]), y: window.__site.yOfBars() }; });
ok(spot.x > 40, `I phone: the last closed candles are in view (x = ${spot.x})`);
await page.touchscreen.tap(pb.x + spot.x, pb.y + pb.height * 0.3); await sleep(800);
ok(!(await dump(page)).inspector, "I phone: a tap on the candles must not open the details card");
await page.touchscreen.tap(pb.x + spot.x, pb.y + spot.y); await sleep(800);
ok((await dump(page)).inspector, "I phone: a tap on a match bar opens the details card");
const over = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
ok(over <= 1, `I phone: the page scrolls sideways by ${over}px`);
if (shots) { await page.screenshot({ path: shots + "/site-phone.png" }); await page.screenshot({ path: shots + "/site-phone-full.png", fullPage: true }); }
await ctx.close();

await browser.close();
ok(errors.length === 0, "page errors: " + errors.slice(0, 5).join(" | "));
console.log(`${passed} checks passed, ${failed} failed`);
process.exit(failed ? 1 : 0);
