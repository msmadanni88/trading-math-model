// Checks that docs/student.js (what the browser runs) gives the same numbers
// as probcast/student.py (what the cloud runs).   node tests/parity.mjs fixture.json
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
const require = createRequire(import.meta.url);
const S = require("../docs/student.js");
const fx = JSON.parse(readFileSync(process.argv[2], "utf8"));
const close = (a, b, tol = 1e-9) => Math.abs(a - b) <= tol * Math.max(1, Math.abs(a), Math.abs(b));
let bad = 0, n = 0;
const check = (ok, msg) => { n++; if (!ok) { bad++; if (bad < 30) console.error("MISMATCH", msg); } };

const reg = S.regularize(fx.raw);
check(reg.length === fx.n_regular, `regularize length ${reg.length} vs ${fx.n_regular}`);
for (const c of fx.cases) {
  const end = reg.findIndex((k) => k[0] === c.last_ts);
  const win = reg.slice(end - S.WIN, end + 1);
  const { f, sig } = S.compact(win, c.last_ts + S.GRAN);
  check(close(sig, c.sig), `sigma ${sig} vs ${c.sig}`);
  f.forEach((x, i) => check(close(x, c.f[i]), `feature ${i}: ${x} vs ${c.f[i]}`));
  const g = S.generate(fx.W, f, sig);
  for (const k of Object.keys(c.gen)) check(close(g[k], c.gen[k]), `gen.${k}: ${g[k]} vs ${c.gen[k]}`);
  // the whole chain: colour (flip included), size, opening level and range of every candle
  const path = S.generatePath(fx.ver, f, sig);
  check(path.length === c.path.length && path.length === fx.horizon, `path length ${path.length}`);
  path.forEach((q, h) => {
    for (const k of Object.keys(c.path[h])) check(close(q[k], c.path[h][k], 1e-12), `path[${h}].${k}: ${q[k]} vs ${c.path[h][k]}`);
    if (h > 0) check(q.o === path[h - 1].o + path[h - 1].b, `chain is connected at candle ${h + 1}`);
  });
  // the cross-venue agent: its view of the other venue, and the chain when that view is used
  const xf = S.xFeatures(win.map((k) => k[4]), c.xclose, sig);
  check((xf === null) === (c.xf === null), `cross-venue view present: ${xf !== null} vs ${c.xf !== null}`);
  if (xf && c.xf) xf.forEach((x, i) => check(close(x, c.xf[i], 1e-9), `cross-venue feature ${i}: ${x} vs ${c.xf[i]}`));
  const px = S.generatePath(fx.ver, f, sig, xf);
  px.forEach((q, h) => { for (const k of Object.keys(c.path_x[h])) check(close(q[k], c.path_x[h][k], 1e-12), `path with the other venue [${h}].${k}: ${q[k]} vs ${c.path_x[h][k]}`); });
  check(px[0].x === (xf ? 1 : 0), "the head that reads the other venue is used exactly when its view exists");
  // an old-format version: only the next candle
  check(S.generatePath({ W: fx.W, H: fx.ver.H }, f, sig).length === 1, "old-format version gives one candle");
  // reversal agents: features of every swing size and the walk through the trees
  for (const [K, want] of Object.entries(c.rev)) {
    const phis = [1, -1].map((side) => S.revFeatures(win, f, sig, side, +K));
    phis.forEach((phi, si) => {
      check(phi.length === want.phi[si].length, `reversal feature count K=${K}`);
      phi.forEach((x, i) => check(close(x, want.phi[si][i], 1e-12), `rev feature K=${K} side ${si} #${i}: ${x} vs ${want.phi[si][i]}`));
    });
    const pr = S.revProbs(fx.model, phis[0], phis[1], fx.hs);
    pr.forEach((row, si) => row.forEach((p, a) => check(close(p, want.probs[si][a], 1e-12), `rev prob K=${K} side ${si} type ${a}: ${p} vs ${want.probs[si][a]}`)));
  }
}
for (const [p, ct, want] of fx.conf) check(S.callLevel({ ct }, p) === want, `callLevel(${p}, ${ct})`);
check(S.callLevel({}, 0.9) === 0 && S.callLevel({ ct: null }, 0.9) === 0, "no lines published: no colour call is claimed");
const s = S.candleScore({ b: 0.0011, u: 0.0004, d: 0.0002 }, 0.0001, -0.0007, 0.0009, -0.0012);
check(close(s.body, fx.score[0]) && close(s.range, fx.score[1]) && close(s.score, fx.score[2]), "candle score");
for (const [i, K, top, bot] of fx.swings) {
  check(S.isSwing(reg, i, 1, K) === top && S.isSwing(reg, i, -1, K) === bot, `swing label at ${i}, K=${K}`);
}
check(S.isSwing(reg, 2, 1, 5) === null && S.isSwing(reg, reg.length - 3, 1, 5) === null, "swing unknown near the edges");
check(S.versionAt([{ eff: 100 }, { eff: 400 }, { eff: 700 }], 450).eff === 400, "versionAt");
check(S.versionAt([{ eff: 100 }], 50) === null, "versionAt before first");
check(fx.cases.some((c) => c.xf) && fx.cases.some((c) => !c.xf), "cases with and without the other venue");
if (bad) { console.error(`${bad} mismatches of ${n} checks`); process.exit(1); }
console.log(`parity ok: ${n} checks, ${fx.cases.length} cases, ${fx.cases[0].f.length} features, ${fx.model.roots.length} trees`);
