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
- **Topic blocks:** under each session, the syllabus topics it covers — each with **three lecture alternatives**, the PYQs tagged to it, its note file, and five Gemini prompts that open an answered chat, already carrying that session's context. See [Topics on a session](#topics-on-a-session).
- **Edit daily log:** creates `daily-logs/YYYY-MM-DD.md` from the template with phase, week and subject frontmatter filled in.
- **Save daily progress:** writes a checklist snapshot into the day's log. Runs automatically when every session for the day is ticked.
- **Day palette:** every day of the phase as a square — green done, amber partial, red missed, grey upcoming, violet ring on today. Tabs 1–7 switch phases. On a phone it starts collapsed behind a tap.
- **Catch-up notice** for unfinished earlier sessions, plus the week strip and subject links.

Keyboard: ←/→ move days, `T` jumps to today, `Esc` closes a dialog. Each day has its own address (`#day-42`).

## Topics on a session

The subject playlist tells you where the lectures are. It does not help at 21:00 when
pointer arithmetic will not go in. So each session also lists the **syllabus topics** it
covers, and each topic carries:

| Row | What it is |
|-----|------------|
| Watch | Up to three **named videos** — the actual lecture, one link each, from three different teachers |
| If none of those land | Topic-scoped searches on the same channels, as a fallback when a video is pulled |
| Questions on this topic | The GATE Overflow tags for that topic, a GO search, and the subject's full PYQ list |
| GATE questions solved on video | People working through GATE's actual questions on this topic — for *after* you have attempted them |
| Ask Gemini · your notes | Five prompts (below) and the topic's note file |

The first topic on each session is open; the rest are one tap away.

### The Gemini prompts

**Make notes**, **Give me questions**, **Explain it**, **Where did I go wrong**, and
**Ask anything** — the last for follow-ups and half-remembered tangents.

Tapping one **opens an answered prompt**, not an empty chat. Two things make that work:

**1. The link goes to Google's AI Mode, not gemini.google.com.** The Gemini web app
ignores `?q=` and `?prompt=` — both were tested, the input box stays empty. AI Mode
(`google.com/search?udm=50&q=...`) is the same model and does read the prompt from the
URL. Its query survives to at least 2044 characters; the planner budgets 1900 and, on
the rare prompt that would exceed it, drops the optional context lines before trimming.
The full prompt is copied to the clipboard on every tap regardless, as a backstop.

**2. Every prompt states the required answer format.** An ask without a shape comes back
as an essay, which cannot be pasted into a note file or marked against a key. So
"Make notes" demands `Must know / Worked example / Traps / Formula-sheet lines`,
"Give me questions" demands `Q1. [MCQ | 1 mark]` with no answers printed and a fixed
reply line, and so on. The topic test fails the build if a prompt stops specifying one.

What actually gets sent is the context block plus the ask:

```
<the goal: GATE 2028 CS, PSU shortlist, answer in GATE terms, no analogies>

Where I am: day 9 of 504, week 2 of 72, phase 1 (Foundations). Today is 2026-09-22.
Subject: C Programming. Syllabus topic PD-3 - Pointers - declaration, dereferencing, ...
This session (Morning, 08:30-10:00): PYQs: pointer basics, swap-style output questions
What I have to record from it: Daily log + error log
Already done today: ...
Still to do today: Evening - Lecture: pointer arithmetic, arrays vs pointers, ...

<the ask, with its required answer structure>
```

So the model is told where in 72 weeks you are, what this session is, and what you have
already ticked off today — the difference between a textbook answer and a useful one.
**Ticking sessions off as you go is what keeps those two lines true.**

The questions prompt withholds answers until you have committed to yours. That is the
whole point of it; don't soften it.

### Where the topic data comes from

Three files, none repeating another:

| File | Holds |
|------|-------|
| `plan/curriculum-*.md` | The topic text, its week, its note file, its GATE Overflow tags |
| `plan/topic-videos.md` | **The lectures** — id, channel and title, one row per video |
| `plan/topic-pyq-videos.md` | **The solved questions** — same shape, found and checked the same way |
| `plan/topic-lectures.md` | The search phrase and which channels to search, used as the fallback |

`webapp/topics.py` joins them and works out which topics a session is about — by the ids
the phase table names outright (`PD-1 … PD-4`), else by matching the focus text against
topic names and tags.

**Why `topic-videos.md` exists.** The first version of this linked channel searches, so a
session on C operators opened a list of search results rather than a lecture. Worse, the
subject playlists `resources.md` points at are thinner than they look — the GO Classes
"C Programming" playlist is nine videos, all about structs, with nothing on operators at
all. So the videos are named individually.

**How they were found.** `webapp/tools/build_videos.py` searches YouTube for each topic
from three angles, ranks results by channel and title match, and keeps the best three
from three different teachers. **Every id is then confirmed against YouTube's oEmbed
endpoint**, which rejects anything that does not exist or cannot be embedded; the channel
and title stored are the ones YouTube returned. A C topic hard-excludes any title
mentioning Python, Java or C++ — GATE code questions are C, and "Operators in Python"
outranked everything until that rule existed.

It matches on **titles, not descriptions**. A title that lies will get through. If a link
is wrong, delete its row and the planner falls back to the channel search for that topic.

**Two kinds of video, deliberately separate.** `topic-videos.md` teaches the topic;
`topic-pyq-videos.md` is someone solving GATE's questions on it. Mixing them would
hide the teaching video behind eight solution videos, and they are used at different
points: watch the lecture first, attempt the PYQs from GATE Overflow, *then* watch
someone else's working. A PYQ video has to say so in its own title — "PYQ",
"previous year", "GATE 2015", "solved" — or it is treated as an ordinary lecture and
rejected. Unlike the lecture file, one teacher may appear several times: Part 1 and
Part 2 of the same PYQ series are both worth having.

**To fix one topic:** `python webapp/tools/build_videos.py PD-3` after deleting its rows.
**To change which channels are trusted:** the `TIER1` / `TIER2` tables in that script.
**To change a fallback search:** the Sources table in `topic-lectures.md` — one row there
covers all 124 topics.

## Where things are stored

| What | Where |
|---|---|
| The plan | `plan/phase-*.md`, parsed on every local page load; baked into `site/data/plan.json` for the hosted build |
| Topic videos | `plan/topic-videos.md` (video id, channel, title — verified against YouTube) |
| Topic resources | `plan/curriculum-*.md` (tags, note files) + `plan/topic-lectures.md` (fallback searches) |
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
python webapp/build_site.py             # build site/
python webapp/tests/topics_test.py      # assert every topic still has its links
python webapp/tests/videos_audit.py     # walk all 504 days: on-topic videos, no channel pages
python webapp/tools/build_videos.py     # re-find the lectures (slow, hits YouTube)
python webapp/tools/build_videos.py --pyq   # re-find the solved-question videos
python webapp/tools/verify_videos.py    # check each video against its own description
python webapp/tests/make_fixtures.py # dump what server.py produces
node webapp/tests/parity.mjs         # assert the JS twins match it byte for byte
node webapp/tests/hosted.mjs         # drive the live repo end to end (needs gh auth)
```

The first three run in CI on every push and gate the deploy; the two tools hit
YouTube, so they are run by hand when the videos need refreshing.

`tests/render-sweep.js` is the one that catches what the others cannot. Paste it into
the browser console on the planner and it clicks through all 504 days, checking the
DOM that actually came out: every video link a `watch?v=`, no channel pages, and no
topic block that renders without something to watch. The Python checks inspect
plan.json, which is the *input* to rendering - twice that passed while the page
itself showed a channel page instead of a lecture. `hosted.mjs` writes real commits, so run it by hand; it restores everything it touches.

## Links

Subject-level link targets live in the `SUBJECTS` and `NAMED_LINKS` tables at the top of
`server.py`, mirroring `plan/resources.md`. If a playlist moves, update both.

Topic-level links are not in `server.py` at all — they are built from
`plan/topic-lectures.md`, so a channel that moves is fixed in one row of one Markdown
file. `topics_test.py` fails the build if a link stops pointing at a source that file
names.

## Safety

- The local server listens on 127.0.0.1 only and rejects writes without its own header.
- Both backends enforce the same allow-list: `.md` files inside `notes/`, `trackers/`, `reviews/`, `daily-logs/`, `plan/`, `docs/`. Nothing else is writable.
- The hosted page sets a Content-Security-Policy that permits no third-party scripts and no network destination but `api.github.com` — the token in localStorage is only as safe as the code that can run on the page, so nothing else is allowed to.
