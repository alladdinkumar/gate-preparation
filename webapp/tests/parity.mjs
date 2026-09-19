// Assert the JavaScript template twins match what server.py produces.
//
//     python webapp/tests/make_fixtures.py
//     node webapp/tests/parity.mjs
//
// Any divergence here means the hosted planner would write different Markdown
// than the local one for the same action, which is exactly the failure this
// whole design is meant to avoid.

import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const here = dirname(fileURLToPath(import.meta.url));
const webapp = dirname(here);
const root = dirname(webapp);

// templates.js targets a browser, so give it just enough of one.
const sandbox = { window: {}, console };
vm.createContext(sandbox);
vm.runInContext(readFileSync(join(webapp, "lib", "templates.js"), "utf8"), sandbox);
const T = sandbox.window.GateTemplates;

const plan = JSON.parse(readFileSync(join(root, "site", "data", "plan.json"), "utf8"));
const templates = plan.templates;
const byDate = new Map(plan.days.map((d) => [d.date, d]));
const fixtures = JSON.parse(readFileSync(join(here, "fixtures.json"), "utf8"));

let failures = 0;
let checks = 0;

// The checklist carries a "saved at" wall-clock stamp, which can never match
// across two processes. Everything else must.
const STAMP = /Saved from the study planner: \d{4}-\d{2}-\d{2} \d{2}:\d{2}\./g;
const normalise = (s) => String(s).replace(STAMP, "Saved from the study planner: <stamp>.");

function check(name, expected, actual) {
  checks++;
  if (normalise(expected) === normalise(actual)) return;
  failures++;
  console.error(`\nFAIL  ${name}`);
  const e = normalise(expected).split("\n");
  const a = normalise(actual).split("\n");
  for (let i = 0; i < Math.max(e.length, a.length); i++) {
    if (e[i] !== a[i]) {
      console.error(`  line ${i + 1}`);
      console.error(`    python: ${JSON.stringify(e[i])}`);
      console.error(`    js    : ${JSON.stringify(a[i])}`);
      break;
    }
  }
}

// ---- daily logs -----------------------------------------------------------
for (const [date, expected] of Object.entries(fixtures.dailyLogs)) {
  check(`dailyLog ${date}`, expected, T.dailyLog(templates, date));
}

// ---- checklist blocks -----------------------------------------------------
for (const entry of fixtures.progress) {
  const day = byDate.get(entry.date);
  if (!day) {
    failures++;
    console.error(`\nFAIL  progress ${entry.date}: date missing from plan.json`);
    continue;
  }
  const { block, completed, total } = T.progressBlock(templates, day, entry.done);
  check(`progressBlock ${entry.date}`, entry.block, block);
  checks++;
  if (completed !== entry.completed || total !== entry.total) {
    failures++;
    console.error(`\nFAIL  progress counts ${entry.date}: python ${entry.completed}/${entry.total}, js ${completed}/${total}`);
  }
  const base = T.dailyLog(templates, entry.date);
  check(`append ${entry.date}`, entry.appended, T.applyProgressBlock(base, templates, block));
  check(`replace ${entry.date}`, entry.replaced,
    T.applyProgressBlock(T.applyProgressBlock(base, templates, block), templates, block));
}

// ---- note / review skeletons ----------------------------------------------
for (const [path, expected] of Object.entries(fixtures.skeletons)) {
  const actual = T.skeletonFor(templates, path);
  checks++;
  if (expected === null) {
    if (actual !== null) {
      failures++;
      console.error(`\nFAIL  skeleton ${path}: python creates nothing, js returned ${JSON.stringify(String(actual).slice(0, 60))}`);
    }
    continue;
  }
  check(`skeleton ${path}`, expected, actual);
}

// ---- path allow-list ------------------------------------------------------
for (const [path, allowed] of Object.entries(fixtures.safePaths)) {
  checks++;
  const actual = T.safePath(templates, path) !== null;
  if (actual !== allowed) {
    failures++;
    console.error(`\nFAIL  safePath ${path}: python ${allowed ? "allows" : "rejects"}, js ${actual ? "allows" : "rejects"}`);
  }
}

console.log(`\n${checks - failures}/${checks} parity checks passed`);
process.exit(failures ? 1 : 0);
