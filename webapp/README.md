# Study Planner

A day-by-day view of the plan with checkboxes, direct lecture / PYQ / material links, daily-progress saving, and a built-in Markdown editor for notes and trackers.

It runs in two places off the same data:

| | Where | Backend | Use it for |
|---|---|---|---|
| **Hosted** | https://alladdinkumar.github.io/gate-preparation/ | The repo, over the GitHub API | Phone, tablet, any machine that isn't yours |
| **Local** | `webapp\start.bat` | `webapp/server.py`, reading D: directly | The desk, offline, editing long notes |

Both read the same plan and write the same files. The local server pulls on startup and pushes after you save, so the two never drift apart.

## Hosted — first run on a new device

Open the link. The plan renders immediately, but it is **read-only** until you give that device a token.

1. Tap **Add token**.
2. On github.com: **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
   - **Repository access:** Only select repositories → `gate-preparation`
   - **Permissions → Repository → Contents: Read and write**. Nothing else.
   - Set an expiry you're willing to renew. When it lapses the page goes read-only and says so.
3. Paste it and save.

The token is kept in that browser's localStorage. It is never committed and never leaves the device except as an `Authorization` header to `api.github.com`. Remove it with **Settings → Remove from this device**; revoke it on github.com if a device is lost.

Add it to your home screen (Share → Add to Home Screen, or the browser's install prompt) and it opens full-screen like an app.

### How saving works

Ticks are batched: four seconds after your last tap, they go up as one commit (`progress: +3 -1 (w4-Mon-AM, ...)`). The status text in the header says `Syncing…`, then `Synced`.

Tick things with no signal and they queue on the device; they go up when you're back online. Closing the tab with unsent ticks prompts you first.

## Local

- **Windows:** double-click `webapp\start.bat`
- **Any OS:** `python webapp/server.py`

It opens http://127.0.0.1:8765. Keep the terminal open; Ctrl+C stops it and pushes anything outstanding.

On startup it runs `git pull --rebase` to collect whatever you ticked on the phone, and prints what it found. After each save it commits and pushes ten seconds later. If git fails it says so and keeps serving — a sync problem never stops you studying. `GATE_NO_SYNC=1` turns it off.

Opening `index.html` as a file does not work: the page needs either the server or the hosted deployment.

## What's on the page

- **Day view:** today's sessions (morning, evening, Saturday block, Sunday review), each with a checkbox, its focus, and the study record the plan requires.
- **Links on every session:** red play icon → the lecture; green tick → the matching GATE Overflow PYQs; blue page → the material or tool; pencil → edit that Markdown file in the planner. Notes and reviews are created from their template if they don't exist yet.
- **Edit daily log:** creates `daily-logs/YYYY-MM-DD.md` from the template with phase, week and subject frontmatter filled in.
- **Save daily progress:** writes a checklist snapshot into the day's log. Runs automatically when every session for the day is ticked.
- **Day palette:** every day of the phase as a square — green done, amber partial, red missed, grey upcoming, violet ring on today. Tabs 1–7 switch phases. On a phone it starts collapsed behind a tap.
- **Catch-up notice** for unfinished earlier sessions, plus the week strip and subject links.

Keyboard: ←/→ move days, `T` jumps to today, `Esc` closes a dialog. Each day has its own address (`#day-42`).

## Where things are stored

| What | Where |
|---|---|
| The plan | `plan/phase-*.md`, parsed on every local page load; baked into `site/data/plan.json` for the hosted build |
| Checkbox progress | `webapp/progress.json` (task id → completion time) |
| Daily checklist snapshots | `daily-logs/YYYY-MM-DD.md` |
| Your token | That browser's localStorage. Nowhere else. |

Task ids look like `w12-Wed-PM` (week, day, slot), so progress survives wording edits to the plan. Changing a phase table's day or slot resets that one checkbox.

The planner is a convenience layer: trackers and reviews remain the source of truth for accuracy, errors and mock scores.

## How it fits together

```
plan/phase-*.md ──► server.py parse_plan() ──┬─► /api/plan          (local)
                                             └─► site/data/plan.json (built in CI)

index.html ──► lib/backend.js ──┬─► backend-local.js  ──► server.py ──► D: drive
                                └─► backend-github.js ──► GitHub API ──► the repo
```

`lib/templates.js` rebuilds daily logs, note skeletons and the checklist block in the browser, because the hosted page has no server to do it. That is the only logic written twice, so it is pinned by a test.

## Tests

```sh
python webapp/build_site.py          # build site/
python webapp/tests/make_fixtures.py # dump what server.py produces
node webapp/tests/parity.mjs         # assert the JS twins match it byte for byte
node webapp/tests/hosted.mjs         # drive the live repo end to end (needs gh auth)
```

The first three run in CI on every push and gate the deploy. `hosted.mjs` writes real commits, so run it by hand; it restores everything it touches.

## Links

Link targets live in the `SUBJECTS` and `NAMED_LINKS` tables at the top of `server.py`, mirroring `plan/resources.md`. If a playlist moves, update both.

## Safety

- The local server listens on 127.0.0.1 only and rejects writes without its own header.
- Both backends enforce the same allow-list: `.md` files inside `notes/`, `trackers/`, `reviews/`, `daily-logs/`, `plan/`, `docs/`. Nothing else is writable.
- The hosted page sets a Content-Security-Policy that permits no third-party scripts and no network destination but `api.github.com` — the token in localStorage is only as safe as the code that can run on the page, so nothing else is allowed to.
