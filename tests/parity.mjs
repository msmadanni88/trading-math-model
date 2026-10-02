// Checks that docs/student.js (what the browser runs) gives the same numbers
// as probcast/student.py (what the cloud runs).   node tests/parity.mjs fixture.json
import { createRequire } from "node:module";
import { readFileSync } from "node:fs";
const require = createRequire(import.meta.url);
const S = require("../docs/student.js");
const fx = JSON.parse(readFileSync(process.argv[2], "utf8"));
const close = (a, b, tol = 1e-9) => Math.abs(a - b) <= tol * Math.max(1, Math.abs(a), Math.abs(b));
let bad = 0;
const check = (ok, msg) => { if (!ok) { bad++; console.error("MISMATCH", msg); } };

const reg = S.regularize(fx.raw);
check(reg.length === fx.n_regular, `regularize length ${reg.length} vs ${fx.n_regular}`);
for (const c of fx.cases) {
  const end = reg.findIndex((k) => k[0] === c.last_ts);
  const { f, sig } = S.compact(reg.slice(end - S.WIN, end + 1), c.last_ts + S.GRAN);
  check(close(sig, c.sig), `sigma ${sig} vs ${c.sig}`);
  f.forEach((x, i) => check(close(x, c.f[i]), `feature ${i}: ${x} vs ${c.f[i]}`));
  const g = S.generate(fx.W, f, sig);
  for (const k of Object.keys(c.gen)) check(close(g[k], c.gen[k]), `gen.${k}: ${g[k]} vs ${c.gen[k]}`);
  const path = S.generatePath(fx.ver, f, sig);
  check(path.length === c.path.length && path.length === 5, `path length ${path.length}`);
  path.forEach((q, h) => { for (const k of Object.keys(c.path[h])) check(close(q[k], c.path[h][k]), `path[${h}].${k}: ${q[k]} vs ${c.path[h][k]}`); });
}
const s = S.candleScore({ b: 0.0011, u: 0.0004, d: 0.0002 }, 0.0001, -0.0007, 0.0009, -0.0012);
check(close(s.body, fx.score[0]) && close(s.range, fx.score[1]) && close(s.score, fx.score[2]), "candle score");
check(S.versionAt([{ eff: 100 }, { eff: 400 }, { eff: 700 }], 450).eff === 400, "versionAt");
check(S.versionAt([{ eff: 100 }], 50) === null, "versionAt before first");
if (bad) { console.error(`${bad} mismatches`); process.exit(1); }
console.log(`parity ok: ${fx.cases.length} cases, ${fx.cases[0].f.length} features`);
