# Gate Preparation — GATE 2028 CS Prep System

A personal prep system to take Sandeep from "5 years out of college, core CS rusty" to a **PSU-grade GATE CS score** (target AIR ≤ 200, working target 75+ marks) in 72 weeks (Sep 2026 → Feb 2028).

This repo is a **markdown-first prep tracker**, built on the same design as `D:\Projects\Study\`. The plan, curriculum, daily logs, trackers, and reviews are all plain markdown files you can edit in any editor. A planner page (`webapp/`) shows each day's sessions with links and checkboxes — on the desk via `webapp\start.bat`, and from any other device at [https://alladdinkumar.github.io/gate-preparation/](https://alladdinkumar.github.io/gate-preparation/) — but everything works with nothing but a text editor too.

---

## The Core Rules

1. **Log first, judge later.** A skipped session is data. A wrong answer is data. Logging is non-negotiable, performance is not.
2. **Don't edit `plan/` files yourself.** If something isn't working, write it in the daily log under "Misses" and discuss it in the Sunday review.
3. **Consistency over heroics.** 80% adherence for 72 weeks beats 100% for 6 weeks then burnout.
4. **One subject per session.** Don't context-switch between OS, TOC, and maths inside the same 1.5h block.
5. **Re-attempt yesterday's wrong questions first.** Before starting today's quota, redo every question logged in `trackers/error-log.md` yesterday.

**Supporting rule — No lecture without PYQs.** Every lecture you watch in the evening is followed by that topic's previous-year questions (PYQs) the next morning. Lectures are passive; PYQs are the exam.

---

## Time Budget

| Day | Slot | Hours |
|-----|------|-------|
| Mon–Fri | 08:30 – 10:00 (pre-work) | 1.5 |
| Mon–Fri | 20:00 – 21:30 (post-work) | 1.5 |
| Saturday | 09:00 – 13:00 (deep work) | 4 |
| Sunday | Rest (30–45 min review only) | 0 |

**Weekly total: 19 hours × 72 weeks = ~1,368 hours.**

---

## Daily Flow (~3 hours total Mon-Fri)

GATE flips the Study split: **new concepts enter in the evening, get tested next morning.** Recall within 24h is what makes a lecture stick.

**Morning session (1.5h, fresh mind → PYQs + numericals)**
1. Open today's daily log: `daily-logs/YYYY-MM-DD.md` (copy from TEMPLATE.md if it doesn't exist)
2. Redo yesterday's wrong questions from `trackers/error-log.md` (10–15 min)
3. Solve today's PYQ quota on yesterday evening's topic (count is in your phase plan)
4. Every wrong / guessed question → one row in `trackers/error-log.md` immediately

**Evening session (1.5h, tired mind → lecture + short notes)**
1. Continue today's daily log
2. Watch the lecture(s) listed in the phase plan for today
3. Write short notes under `notes/<subject>/...` — definitions, formulas, one solved example. Not transcripts.
4. Fill in Reflection section (5 min) before closing

**Saturday (4h)**
- 09:00 – 11:00 — Timed topic test: the week's subject, PYQs you haven't seen, under GATE conditions (virtual calculator, negative marking)
- 11:00 – 12:00 — General Aptitude (15 easy marks — never skip)
- 12:00 – 13:00 — Error analysis of the test + revise the week's short notes + compile data for Sunday review

**Sunday (rest, but 30–45 min Sunday morning recommended)**
- Write the weekly review (`reviews/weekly/YYYY-MM-DD-to-YYYY-MM-DD.md`)
- Update all 8 trackers in `trackers/`
- Set focus for next week

---

## Folder Map

| Folder | What it is |
|--------|------------|
| `plan/` | Syllabus, curriculum, phase roadmap, exam info, resources. **Read-only for you** — coach-edited. |
| `daily-logs/` | One file per day, `YYYY-MM-DD.md`. **You write these every day.** |
| `trackers/` | Rolling dashboards. **You update these once a week** during Sunday review. (Error log is the exception — append as you go.) |
| `reviews/` | Weekly + monthly synthesis. **You write these on Sunday / month-end.** |
| `notes/` | Short notes + formula sheets per subject. **You write these inline as you study.** |
| `docs/` | How-to, architecture, FAQ. |
| `webapp/` | Study planner: day-by-day checklist with lecture / PYQ / material links. Run locally with `webapp\start.bat`, or open the hosted copy at [https://alladdinkumar.github.io/gate-preparation/](https://alladdinkumar.github.io/gate-preparation/) from a phone. See `webapp/README.md`. |
| `.github/workflows/` | Builds the hosted planner and runs the parity tests on every push. |

---

## Where to Start

**Today / day 0 (Sunday 2026-09-13):**
1. Read `plan/PLAN.md` — the master 72-week roadmap.
2. Read `plan/exam-info.md` — **do the Day 0 checklist there** (PSU age eligibility check, GATE 2027 practice-attempt decision).
3. Read `plan/syllabus.md` — the official syllabus you are being tested on.
4. Read `plan/phase-1-foundations.md` — your first 10 weeks in detail.
5. Read `plan/resources.md` — bookmark every link, download the GATE Overflow PDFs.
6. Read `plan/weekly-schedule.md` — set recurring calendar blocks for your sessions.

**Monday 2026-09-14 (day 1):**
1. Double-click `webapp\start.bat` — the planner page opens on today's sessions with every link you need. Tick sessions off as you finish them. Away from the desk, use [https://alladdinkumar.github.io/gate-preparation/](https://alladdinkumar.github.io/gate-preparation/) instead; it writes to the same files.
2. Edit `daily-logs/2026-09-14.md` in the planner (later days: use "Edit daily log" on the planner page).
3. Fill in sessions as you go.
4. Don't skip the Reflection section — even if it's one-line answers.

---

## How to Work With the Claude Code Coach

When you open this folder in a new Claude Code session, `CLAUDE.md` loads `prompt.md` (your coach's persona). You can say:

- **"Read this week's logs and update trackers, then write the weekly review."** → Sunday flow, fully automated.
- **"Read today's log and tell me what to focus on this evening."** → Mid-day course-correction.
- **"Give me 5 GATE-style questions on my weakest topic."** → Practice generator (using `trackers/weak-areas.md` + `trackers/error-log.md`).
- **"Analyse my mock from Saturday."** → Mock post-mortem.

Don't ask the coach to *do the studying for you*. Ask the coach to plan, review, and challenge.

---

## Two-Track Roadmap

- **Track A — Content (done):** Plan, syllabus, curriculum, daily-log template, trackers, reviews — all the markdown that lets you start tomorrow.
- **Track B — Webapp:** the day-by-day planner page is built (`webapp/`) and hosted, so sessions can be ticked from a phone. Dashboard features (charts, auto-rollups) are deferred until manual tracker upkeep is eating study time.

See `docs/architecture.md` for the rationale.

---

## When You Fall Behind

You will. Plan for it.

- **One bad day:** Log it, move on. Don't try to "make up" by doubling tomorrow's load.
- **One bad week (<60% adherence):** Mention it in the weekly review under "What's not working." The coach will adjust next week's plan.
- **Two bad weeks in a row:** Extend the current subject by 1 week in the monthly review. Don't compress to "catch up."
- **A bad month:** Re-scope. Phase 5 (revision) and Phase 6 (test series) are the buffer — they can shrink by up to 3 weeks combined. Beyond that, drop depth in the lowest-weightage topics, never skip a subject.

The plan exists for you. You don't exist for the plan.
