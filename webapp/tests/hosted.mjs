// End-to-end check of the hosted backend against the real repository.
//
//     node webapp/tests/hosted.mjs            (uses `gh auth token`)
//     GATE_TOKEN=github_pat_... node webapp/tests/hosted.mjs
//
// This exercises the path a phone takes: read the plan, tick a session, let
// the debounced flush commit it, read it back, untick it, and write a daily
// log. It leaves progress.json as it found it.
//
// Not part of CI - it writes real commits and needs a token.

import { execSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const here = dirname(fileURLToPath(import.meta.url));
const webapp = dirname(here);

const token = process.env.GATE_TOKEN || execSync("gh auth token").toString().trim();
if (!token) throw new Error("No token. Set GATE_TOKEN or run `gh auth login`.");

// ---- just enough browser for the backend to run in -------------------------
const store = new Map();
const sandbox = {
  window: {},
  console,
  fetch,
  btoa: (s) => Buffer.from(s, "binary").toString("base64"),
  atob: (s) => Buffer.from(s, "base64").toString("binary"),
  TextEncoder,
  TextDecoder,
  navigator: { onLine: true },
  setTimeout,
  clearTimeout,
  localStorage: {
    getItem: (k) => (store.has(k) ? store.get(k) : null),
    setItem: (k, v) => store.set(k, String(v)),
    removeItem: (k) => store.delete(k),
  },
};
sandbox.window = sandbox;                     // the modules assign onto window
sandbox.window.addEventListener = () => {};
vm.createContext(sandbox);
for (const f of ["templates.js", "backend-github.js"]) {
  vm.runInContext(readFileSync(join(webapp, "lib", f), "utf8"), sandbox);
}

const SITE = "https://alladdinkumar.github.io/gate-preparation";
const config = await (await fetch(`${SITE}/data/config.json`)).json();
const backend = sandbox.window.createGitHubBackend(config);

let failures = 0;
function assert(name, condition, detail = "") {
  if (condition) {
    console.log(`  ok    ${name}`);
  } else {
    failures++;
    console.error(`  FAIL  ${name}${detail ? ` - ${detail}` : ""}`);
  }
}

// getPlan() fetches a path relative to the page, so point it at the live site.
const realFetch = sandbox.fetch;
sandbox.fetch = (url, opts) =>
  realFetch(String(url).startsWith("data/") ? `${SITE}/${url}` : url, opts);

console.log(`\nhosted backend -> ${backend.describe()}`);

// ---- 1. plan --------------------------------------------------------------
const plan = await backend.getPlan();
assert("getPlan returns 7 phases", plan.phases.length === 7, `got ${plan.phases.length}`);
assert("getPlan carries templates", Boolean(plan.templates && plan.templates.dailyLog));

// ---- 2. token -------------------------------------------------------------
assert("read-only before a token", backend.needsSetup());
await backend.setToken(token);
assert("writable after setToken", backend.canWrite() && !backend.needsSetup());

// ---- 3. baseline ----------------------------------------------------------
const before = await backend.getProgress();
const baseline = JSON.stringify(before.done);
const day = plan.days.find((d) => d.tasks.length >= 2);
const [taskA, taskB] = day.tasks;
console.log(`  using ${day.date}: ${taskA.id}, ${taskB.id}`);

// ---- 4. tick two sessions, one commit -------------------------------------
await backend.setTask(taskA.id, true);
await backend.setTask(taskB.id, true);
assert("both ticks queued", backend.offlineCount() === 2, `queued ${backend.offlineCount()}`);
await backend.flush();
assert("queue drained after flush", backend.offlineCount() === 0);

const afterTick = await backend.getProgress();
assert("tick A landed in the repo", Boolean(afterTick.done[taskA.id]));
assert("tick B landed in the repo", Boolean(afterTick.done[taskB.id]));

// ---- 5. unticking must remove the key, not resurrect it --------------------
await backend.setTask(taskA.id, false);
await backend.flush();
const afterUntick = await backend.getProgress();
assert("untick removed A", !afterUntick.done[taskA.id]);
assert("untick left B alone", Boolean(afterUntick.done[taskB.id]));

// ---- 6. daily log + checklist ---------------------------------------------
// This writes to a real daily log, so remember its exact state first and put
// it back at the end. A test must never leave marks in the study record.
const logPath = `daily-logs/${day.date}.md`;
let logBefore = null;
try {
  logBefore = (await backend.readFile(logPath)).content;
} catch { /* not in the repo yet */ }

const log = await backend.createDailyLog(day.date);
assert("daily log has the right date", log.content.includes(`date: ${day.date}`));
const saved = await backend.saveDailyProgress(day.date, { day, done: afterUntick.done });
assert("checklist counts the ticks", saved.completed === 1 && saved.total === day.tasks.length,
  `${saved.completed}/${saved.total}`);
assert("checklist marks B done", saved.content.includes(`**${taskB.slot} (${taskB.time})**`));

// Writing it twice must replace the block, not stack two of them.
const twice = await backend.saveDailyProgress(day.date, { day, done: afterUntick.done });
const marks = twice.content.split(plan.templates.progressStart).length - 1;
assert("checklist block is replaced, not duplicated", marks === 1, `${marks} blocks`);

// ---- 7. non-ASCII survives the base64 round trip --------------------------
assert("em dash survived the round trip", twice.content.includes("—"));

// ---- 8. path guard --------------------------------------------------------
for (const bad of ["webapp/server.py", "../escape.md", "notes/x.txt"]) {
  let threw = false;
  try { await backend.readFile(bad); } catch { threw = true; }
  assert(`readFile rejects ${bad}`, threw);
}

// ---- restore --------------------------------------------------------------
if (logBefore !== null) {
  await backend.writeFile(logPath, logBefore);
  const check = await backend.readFile(logPath);
  assert("daily log restored", check.content === logBefore);
} else {
  // The log did not exist before this run, so remove the one we created.
  const meta = await (await fetch(
    `https://api.github.com/repos/${config.repo.owner}/${config.repo.name}/contents/${logPath}`,
    { headers: { Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json" } }
  )).json();
  const res = await fetch(
    `https://api.github.com/repos/${config.repo.owner}/${config.repo.name}/contents/${logPath}`,
    {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
        Accept: "application/vnd.github+json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message: `test: remove ${logPath}`, sha: meta.sha }),
    }
  );
  assert("test daily log removed", res.ok, `HTTP ${res.status}`);
}

for (const id of Object.keys(afterUntick.done)) {
  if (!JSON.parse(baseline)[id]) await backend.setTask(id, false);
}
for (const [id, at] of Object.entries(JSON.parse(baseline))) {
  if (!afterUntick.done[id]) await backend.setTask(id, true, at);
}
await backend.flush();
const restored = await backend.getProgress();
assert("progress.json restored to baseline",
  JSON.stringify(restored.done) === baseline,
  `now ${JSON.stringify(restored.done)}`);

console.log(failures ? `\n${failures} check(s) failed` : "\nall hosted checks passed");
process.exit(failures ? 1 : 0);
