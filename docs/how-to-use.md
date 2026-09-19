# How to Use This Prep System

A practical guide. Keep this open for the first two weeks — habits form by Day 14.

---

## Day 0 — Setup (Sunday 2026-09-13, ~90 minutes)

1. Read `README.md` end-to-end.
2. Skim `plan/PLAN.md` so you know the 72-week shape, the Sealed-Paper Rule and the PYQ Split Rule.
3. **Do the Day 0 checklist in `plan/exam-info.md`:**
   - PSU age eligibility check for 2028 → record in `trackers/progress.md`
   - Decide on the GATE 2027 practice attempt (registration closes 27 Sep 2026; 5 Oct with late fee)
   - DigiLocker set up
4. Read `plan/syllabus.md` once — this is the contract.
5. Read `plan/phase-1-foundations.md` in detail.
6. Open `plan/resources.md`: bookmark the links, download the GO PDFs, create a GATE Overflow account, bookmark the virtual calculator.
7. Set up recurring calendar blocks (see `plan/weekly-schedule.md`).
8. Open `daily-logs/2026-09-14.md` — your bootstrap Day 1 log is already there.
9. Get a physical rough-work notebook. GATE is solved on paper, not in your head.

---

## Daily Flow (Mon–Fri, ~5 minutes of overhead)

### Morning (08:30, before logging in for work) — practice

1. Open `daily-logs/YYYY-MM-DD.md` (today's file)
   - If it doesn't exist, copy `daily-logs/TEMPLATE.md` to today's date filename
2. Fill in YAML frontmatter (date, phase, overall_week, subject, focus_topic)
3. **Redo yesterday's error-log rows first** (10–15 min) — no looking at the solution
4. Solve today's PYQ quota on yesterday evening's topic, timed, per the phase file
   - Even years + 2021 on weekdays (Phases 1–4); skip anything 2022+
5. One line per question under **Questions Attempted**
6. Every wrong / guessed question → a row in `trackers/error-log.md` **now**, with an error type

**Don't:** look at the answer before committing to one. **Don't:** track time to the second — round to the minute per question.

### Evening (20:00, after dinner) — lecture

1. Open the same daily log
2. Watch the lecture for today's topic (primary series only) — 60–70 min
3. Write the short note in `notes/<subject>/` — definitions, formulas, one worked example, traps
4. Add any formula to the subject's sheet in `notes/formula-sheets/`
5. Fill in Evening Session + Reflection (5 min)
6. Update Adherence Flags before sleep

**Don't:** skip the Reflection section. It's where insights compound.

---

## Saturday Flow

1. Open today's daily log (Saturday's file)
2. **09:00 — Timed test** (Phases 1–5) on the week's topics, odd-year PYQs, virtual calculator, negative marking. Phase 6+: full 3-hour mock from 09:00 to 12:00
3. **11:00 — General Aptitude** hour (rotation in `plan/curriculum-aptitude.md`)
4. **12:00 — Error analysis:** score the test, log every lost mark in `error-log.md`, revise the week's notes, jot numbers for Sunday
5. **13:00 — Done.** Rest of day is yours.

---

## Sunday Flow (30–45 min, morning recommended)

1. Open `reviews/weekly/2026-MM-DD-to-2026-MM-DD.md`
   - Copy `reviews/weekly/TEMPLATE.md` to that filename
2. Read this week's 6 daily logs
3. Fill in hours, PYQs, test score, error-type counts, what worked / didn't
4. Update all 8 trackers:
   - `trackers/progress.md` — weekly adherence row, milestones, mock trend
   - `trackers/subjects.md` — per-topic counts, accuracy, confidence
   - `trackers/pyq.md` — subject totals, question-type accuracy
   - `trackers/mocks.md` — Saturday test / mock row
   - `trackers/error-log.md` — weekly summary row, promote recurring traps
   - `trackers/revision.md` — revision rounds, quiz scores, stale topics
   - `trackers/aptitude.md` — GA row
   - `trackers/weak-areas.md` — add new gaps, archive remediated ones
5. Set focus for next week (one sentence)
6. **Close laptop. Rest.**

---

## Monthly Flow (last Sunday of month, 90 min)

1. Do the weekly review first (above)
2. Open `reviews/monthly/YYYY-MM.md` (copy template)
3. Read all 4–5 weekly reviews from the month
4. Error-type trend for the month → one process fix
5. Check revision health: any finished subject >30 days untouched?
6. External checks: GATE 2028 site, PSU notifications (Phase 5+)
7. Decide: proceed / extend / re-scope
8. Write 3 concrete commitments for next month

Monthly review Sundays: the phase files mark them. The first one is 2026-10-25 (Week 6).

---

## When You Want to Run a Claude Code Coach Session

Open this folder in Claude Code (`cd "D:\Projects\Gate Preparation"` and run `claude`). `CLAUDE.md` loads the coach persona from `prompt.md`.

Useful prompts:

- **"Read this week's daily logs, update the trackers and write the weekly review."** — full Sunday automation
- **"Read today's log. What should I focus on this evening?"** — mid-day course-correct
- **"What's today's plan?"** — pulls the day's rows from the phase file
- **"Give me 5 GATE-style questions on my weakest topic — don't show answers until I submit."** — practice generator from `weak-areas.md` + `error-log.md`
- **"Analyse Saturday's mock."** — lost-marks breakdown + remediation subjects for the week
- **"Quiz me on DBMS normalization — make me explain first."** — concept check
- **"What's the current state of my prep? Be honest."** — readiness check

The coach won't solve PYQs for you before you've attempted them. It coaches.

---

## Common Pitfalls

| Pitfall | Why it happens | Fix |
|---------|----------------|-----|
| Watching lectures, skipping next-morning PYQs | Lectures feel productive | No lecture without PYQs within 24h — rule in `README.md` |
| Logging errors on Sunday instead of immediately | "I'll batch it" | Log in the moment. Sunday logging loses the *why* |
| Checking the answer after 30 seconds | Discomfort with being stuck | Commit to an answer (or skip) first. Being stuck is where learning happens |
| Solving numericals by mental maths | Pride / speed | Virtual calculator for every multi-step NAT — the exam won't give you anything else |
| Peeking at 2022+ papers | Curiosity | They're your only unseen mocks. Sealed means sealed |
| Hopping between lecture series | "Maybe this teacher explains it better" | Backup only for one concept that didn't land, never the whole subject |
| Editing `plan/` when frustrated | Procrastination disguised as planning | Don't. Flag in the weekly review instead |
| Doing a Sunday study session anyway | "I have time, why not?" | Don't. Sunday rest = Monday performance |
| Re-reading notes instead of redoing errors | Passive feels safe | Error-log redos beat re-reading every time |

---

## Habit Building Tip

**Weeks 1–2 will feel hard.** Habit research says 14–21 days to feel natural. Push through. If you only adhere 50% in Week 1, that's normal — log honestly and don't panic. Adherence climbs to 70–80% by Week 3 if you don't quit.

If after 3 weeks you're still <50% adherent, **don't push harder**. Re-evaluate: is the schedule realistic? Is morning the wrong slot for you? Is something at work draining you? Adjust the *schedule*, not your willpower. 72 weeks rewards a sustainable rhythm, not an heroic one.
