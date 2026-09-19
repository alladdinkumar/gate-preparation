# System Architecture

How this prep system is built and why.

---

## Design Philosophy

**Markdown is the source of truth.** Everything else is a convenience layer.

This means:
- The files in `daily-logs/`, `trackers/`, `plan/`, `reviews/`, `notes/` are *the system*.
- You can edit them in any editor — VS Code, Notepad++, vim, Obsidian.
- Git (if you initialise it) gives free version history and backup.
- Claude Code reads and writes the same markdown.
- A future webapp (Track B) is a *thin shell over markdown*, not a replacement.

This mirrors `D:\Projects\Study\` (the FAANG prep system), which itself borrowed the pattern from `D:\Projects\Fitness and SkinCare\`. Same skeleton, GATE content.

---

## Mapping from the Study System

| Study (FAANG) | Gate Preparation | Why it changed |
|---------------|------------------|----------------|
| `plan/PLAN.md` — 26 weeks, 5 phases | `plan/PLAN.md` — 72 weeks, 7 phases | GATE 2028 horizon; revision + test-series phases matter more than in interview prep |
| `plan/curriculum-{dsa,hld,lld,core-subjects,behavioral}.md` | `plan/curriculum-{engineering-maths,programming-algorithms,digital-coa,systems,theory,aptitude}.md` | Grouped by GATE syllabus sections |
| `plan/company-targets.md` | `plan/exam-info.md` | Exam pattern, marking, dates, PSU route, eligibility |
| — | `plan/syllabus.md` | GATE has an official syllabus — it's the contract, so it gets its own file with row IDs |
| `plan/resources.md`, `plan/weekly-schedule.md` | same names | Free-only rule kept; slot purposes flipped (see below) |
| `trackers/{dsa,hld,lld,core-subjects,behavioral}.md` | `trackers/{subjects,pyq,aptitude,revision}.md` | One syllabus-row tracker replaces per-domain ones; PYQ and revision tracking are GATE-specific |
| `trackers/mocks.md`, `weak-areas.md`, `progress.md` | same names | Mocks are exam papers, not interviews |
| — | `trackers/error-log.md` | GATE rank is decided by repeated mistakes and negative marks; needs its own append-only log |
| `notes/{dsa,hld,lld,core}/` | `notes/{maths,programming-ds,algorithms,digital-logic,coa,os,dbms,cn,toc,compiler,aptitude,formula-sheets}/` | One folder per GATE subject + formula sheets for final revision |
| `prompt.md` (auto-load implied) | `prompt.md` + `CLAUDE.md` (`@prompt.md`) | `CLAUDE.md` makes Claude Code actually load the persona |

**Slot flip:** Study used mornings for coding and evenings for theory. GATE uses **evening = new lecture, next morning = PYQs on it**. Recall within 24 hours, under a fresh mind, is the core learning loop.

---

## Two-Track Build

### Track A — Content (built)

All markdown:
- 1 master plan + syllabus + exam info
- 6 curriculum docs
- 7 phase plans with a day-by-day table for every one of 72 weeks
- 1 resources doc, 1 weekly-schedule doc
- 1 daily-log template + Day-1 bootstrap
- 8 tracker files
- 2 review templates (weekly + monthly)
- 12 notes index files
- 3 docs files

**Usable today with zero additional tooling.**

### Track B — Webapp (planner page built early; dashboard features deferred)

The day-by-day planner page (`webapp/`, see `webapp/README.md`) was built on request before Week 1: it reads `plan/phase-*.md`, stores checkboxes in `webapp/progress.json`, and uses only the Python standard library — no Flask, no build step. The dashboard features below remain deferred.

Dashboard features get built only if, after ~6 weeks of real use:
- Daily logging habit is established
- The markdown schema has been battle-tested (some fields will turn out to be cruft)
- Manual tracker upkeep is measurably eating study time (>45 min on Sundays)

**Tech stack** (same as the Study plan's sketch):
- **Backend:** Flask 3+, python-frontmatter (YAML + markdown)
- **Frontend:** vanilla HTML + Alpine.js (CDN) + Tailwind (CDN) — **zero build step**
- **Storage:** pure markdown (no DB)

**Features** (in priority order):
1. Open today's daily log (auto-create from template, pre-fill frontmatter + today's rows from the phase file)
2. Question-entry form that appends to the daily log **and** `error-log.md` in one step
3. Sunday auto-rollup: PYQ counts, accuracy per subject / question type, error-type breakdown
4. Charts: mock score trend, accuracy per subject, error types over time, hours adherence
5. Pending-items rules ("error-log backlog >40", "subject untouched >30 days", "no log yesterday", "Saturday test <40%")

---

## File Organization Rationale

### Why `plan/` is read-only

The plan represents *committed decisions*. Editing it casually leaks "I'll just tweak one thing" into procrastination. The plan only changes during the monthly review's explicit adjustment step — or when an official source (brochure, syllabus) changes.

### Why `trackers/` are updated weekly (not daily)

Daily updates create busy-work and false signal. A week is the smallest window with enough data to see a trend. Per-day data lives in `daily-logs/`.

**Exception: `error-log.md`** is appended in the moment. An error logged on Sunday has lost its *why*.

### Why syllabus row IDs (PD-3, CO-6, …)

Every topic has one ID used in `syllabus.md`, the curriculum files, the phase tables, `subjects.md`, the error log and the notes indexes. It makes grep-based coverage checks trivial ("is every syllabus row in a phase week?") and lets the coach aggregate errors by topic reliably.

### Why `notes/` is by subject, not by date

Notes are reference material — you'll return to `notes/coa/co-06-cache-mapping.md` in Phase 5 and Phase 7. Organise by what you search *for*, not when you wrote it.

### Why `reviews/` separates weekly from monthly

Different functions: weekly = "what happened" + "next week"; monthly = "are we on track" + "extend / re-scope". Mixing them dilutes both.

### Why YAML frontmatter on daily logs

Machine-readable (Claude Code and a future webapp can parse it) while staying human-readable.

---

## How Claude Code Coach Sessions Work

When you run `claude` in this directory:

1. Claude Code loads `CLAUDE.md`, which imports `prompt.md` (the coach persona)
2. Claude has tools to read, write and search across this directory
3. You issue a coaching prompt (see `docs/how-to-use.md`)
4. Claude reads the relevant files (today's log, phase file, trackers)
5. Claude responds in-conversation or writes to files (reviews, tracker updates)
6. Closing the session preserves all file changes (they're real markdown)

No shared state outside markdown files. Restart-safe.

---

## Why Not Use [Notion / Obsidian / Anki / etc.]?

| Tool | Why not (as the primary system) |
|------|----------------------------------|
| Notion | Lock-in, slow, export friction |
| Obsidian | Actually fine — can sit on top of these files as a viewer. Just don't add a second system |
| Anki | Great for pure recall, but GATE questions are problem-solving, not flashcards. The error log + redo schedule is the GATE-shaped version of spaced repetition |
| Excel / Sheets | Bad for prose (notes, reflections), version-control hostile |
| Coaching app dashboards | Tied to one resource; you're free-only and multi-source |

**Markdown wins on:** portability, version control, tool flexibility, longevity, plain-text durability, AI-readability.
