# Master Plan — 72 Weeks to GATE 2028 CS (PSU rank)

**Start:** Mon 2026-09-14
**Structured plan ends:** Sun 2028-01-30 (end of Week 72)
**Exam:** GATE 2028 — expected early/mid Feb 2028 (GATE 2027 runs 6–21 Feb 2027; confirm 2028 dates when the brochure is out, ~Jul/Aug 2027)
**Total weeks:** 72 (+ exam window)
**Total hours:** ~1,368 (19h/week)

---

## Profile Snapshot

| Item | Value |
|------|-------|
| Age | 26 (as of 2026) — **see PSU age-limit risk in `exam-info.md`** |
| Current role | Senior SWE @ Privafy, ~5.5 yrs, studying alongside full-time work |
| Degree | B.Tech CSE, LPU, 2021, CGPA 8.82 |
| Paper | GATE CS (Computer Science and Information Technology) — single paper |
| Target | PSU recruitment → AIR ≤ 200, working target **75+ / 100** |
| Fallback the same score unlocks | M.Tech at IITs / IISc |
| Resources | Free-only |
| Baseline | Unknown — measured by the Week 1 Saturday diagnostic |
| Likely strong | Programming, practical OS / CN intuition |
| Likely weak | Engineering Maths, Discrete Maths, TOC, Compiler Design, Digital Logic, COA |

---

## Phase Overview

| Phase | Weeks | Dates | Hours | Subjects (weeks each) | Outcome |
|-------|-------|-------|-------|------------------------|---------|
| **1. Foundations** | 1–10 | 2026-09-14 → 2026-11-22 | 190h | C Programming (3), Data Structures (3), Discrete Maths (4) | PDS + DM syllabus done, PYQs 2000–2021 attempted |
| **2. Algorithms + Maths + Digital** | 11–22 | 2026-11-23 → 2027-02-14 | 228h | Algorithms (4), Linear Algebra (1), Calculus (1), Probability & Statistics (2), Digital Logic (4) | All maths + Algo + DL done |
| **3. Systems** | 23–36 | 2027-02-15 → 2027-05-23 | 266h | COA (5), OS (5), DBMS (4) | Three highest-weight core subjects done |
| **4. Networks + Theory** | 37–49 | 2027-05-24 → 2027-08-22 | 247h | CN (5), TOC (5), Compiler Design (3) | **Full syllabus covered once** |
| **5. Revision + PYQ Pass 2** | 50–60 | 2027-08-23 → 2027-11-07 | 209h | One subject per week, second pass | Every subject revised, formula sheets written, first full mock ≥50 |
| **6. Test Series** | 61–70 | 2027-11-08 → 2028-01-16 | 190h | 2 mock papers/week + targeted remediation | Mock average ≥65, rising |
| **7. Final Sprint** | 71–72 | 2028-01-17 → 2028-01-30 | 38h | Formula sheets, error-log redo, last mocks | Last 3 mocks ≥75. Walk in calm. |
| Exam window | 73+ | 2028-01-31 → exam | light | 30–45 min/day recall only | — |

**General Aptitude** (15 marks) runs through every phase: Saturday 11:00–12:00, rotating verbal / quantitative / analytical / spatial. See `curriculum-aptitude.md`.

---

## Per-Phase Detail

Each phase has its own file with a day-by-day table for every week:

- `phase-1-foundations.md`
- `phase-2-algorithms-maths-digital.md`
- `phase-3-systems.md`
- `phase-4-networks-theory.md`
- `phase-5-revision.md`
- `phase-6-test-series.md`
- `phase-7-final-sprint.md`

Subject depth lives in the curriculum files (`curriculum-*.md`); the official syllabus and weightage in `syllabus.md`.

---

## Subject Weightage (why the order is what it is)

Approximate marks per paper, GATE CS 2023–2025 (GO Classes analysis). Use for prioritisation, not prediction — any subject can swing ±3 marks.

| Subject | ~Marks | Weeks in first pass |
|---------|--------|---------------------|
| General Aptitude | 15 (fixed) | every Saturday |
| Engineering Maths (DM + LA + Calc + Prob) | ~10–13 | 8 |
| Programming & Data Structures | ~8–11 | 6 |
| COA | ~8–12 | 5 |
| Operating Systems | ~7–10 | 5 |
| Theory of Computation | ~7–9 | 5 |
| Computer Networks | ~8–9 | 5 |
| Algorithms | ~6–8 | 4 |
| DBMS | ~5–8 | 4 |
| Digital Logic | ~5–6 | 4 |
| Compiler Design | ~5–8 | 3 |

Order logic: C + DS first (everything else uses them) → Discrete Maths (needed for Algorithms, TOC, DBMS) → Algorithms → rest of maths → Digital Logic (needed for COA) → COA (needed for OS) → OS → DBMS → CN → TOC → CD (needs TOC).

---

## The Sealed-Paper Rule

Full GATE CS papers from **2022 onward (all sets)** are **sealed**. Don't attempt their questions in daily practice during Phases 1–5 — skip questions whose year tag is 2022 or later (`gatecse-2022`, `gatecse-2023`, `gatecse-2024-set1`, …) in GATE Overflow / GO PDFs. They are your unseen full-length mocks in Phases 6–7. Daily practice uses PYQs from 2000–2021 (older ones where the topic is still in syllabus).

If you accidentally see a sealed question, don't stress — just note it in the daily log.

## The PYQ Split Rule (Phases 1–4)

So Saturday tests are never questions you solved on Tuesday:

| Slot | PYQs used |
|------|-----------|
| Weekday AM practice | **Even years** (2000, 2002, … 2020) **+ all of 2021** |
| Saturday topic test | **Odd years** (2001, 2003, … 2019) |
| Top-up when a topic runs dry (<8 questions) | Pre-2000 GATE questions → GO Classes free practice sets → textbook exercises |

Phase 5 redoes **every** 2000–2021 question subject-wise. Phases 6–7 use the sealed 2022+ papers.

---

## What You're Being Measured On

By the exam you should be able to honestly say yes to all of these:

**Coverage**
- [ ] Every topic in `syllabus.md` studied, short notes written, confidence ≥3 in `trackers/subjects.md`
- [ ] 100% of GATE CS PYQs 2000–2021 attempted subject-wise (counts per subject in `trackers/pyq.md`)
- [ ] One formula / fact sheet per subject in `notes/formula-sheets/`
- [ ] Every subject revised at least 3 times (`trackers/revision.md`)

**Accuracy**
- [ ] Subject PYQ accuracy ≥70% in every subject, ≥80% in the top-6 weightage subjects
- [ ] General Aptitude ≥12/15 in the last 5 mocks
- [ ] Error-log redo success ≥85%

**Exam skill**
- [ ] 20+ full-length mocks under GATE conditions (virtual calculator, 3h, negative marking)
- [ ] Last 3 mocks ≥75/100
- [ ] Negative marks ≤3 per mock over the last 5 mocks
- [ ] Finish a paper with ≥10 min to spare

---

## What the Coach Watches (and thresholds to react on)

| Metric | Watching for | Action if triggered |
|--------|--------------|----------------------|
| Weekly adherence | <60% for 2 consecutive weeks | Re-scope: extend current subject by 1 week |
| Subject PYQ accuracy | <50% after 30 PYQs in that subject | Remediation block: re-watch weakest lectures + 15 easier PYQs, then retest |
| Saturday topic test | <40% | Next week's Wed + Thu PM go back to that topic |
| Error-log redo backlog | >40 un-redone rows | Next morning session is redo-only, no new PYQs |
| Revision gap | Any finished subject untouched >30 days | Schedule a 1.5h revision slot within the week |
| Mock score trend (Phase 5+) | Flat or declining across 3 mocks | Root-cause by subject + error type, concentrate next 2 weeks there |
| Negative marks | >5 marks lost to negatives in one mock | Enforce guessing rule: no MCQ attempt below ~50% confidence |
| Skipped reviews | >1 missed Sunday review | Hard-flag in next daily-log Reflection: "Why am I avoiding the review?" |
| Sleep / energy <6/10 sustained | 5+ days in a row | Force a rest day mid-week. Plan adjusts down 20% next week. |

---

## What's Off the Table

These are explicitly **not** in scope:

- Paid courses and paid test series (free-only — revisit only at a monthly review, see Deferred Decisions)
- GATE DA or any second paper
- Topics no longer in the CS syllabus: Software Engineering, Web Technologies, IPv6 deep-dives, SMTP/FTP/email protocols, application-layer trivia beyond DNS and HTTP
- Reading textbooks cover to cover — textbooks are reference only
- Hopping between lecture series for the same topic. One primary per subject (listed in `resources.md`); backup only for a specific concept that didn't land
- FAANG DSA / LeetCode prep (paused — `D:\Projects\Study\` stays as-is)
- Premature webapp dashboard work

---

## Deferred Decisions (revisit at month-end)

- **GATE 2027 practice attempt** — decide by **5 Oct 2026** (late-fee registration close). See `exam-info.md`. If taken, the exam (6–21 Feb 2027) falls in Weeks 21–23 and replaces that weekend's test.
- **Saturday block structure** — start with 9am–1pm continuous; switch to 2+2 split if energy flags.
- **Free all-India mock sources for Phase 6** — shortlist at the Week 54 monthly review (Sep 2027) (what's free changes year to year).
- **Paid test series** — only if the free full-length pool (sealed papers + free all-India mocks) runs out before Week 66. Decide at the Week 59 monthly review (Oct 2027).
- **PSU shortlist** — finalise once the GATE 2028 brochure and PSU notifications are out; eligibility check happens on Day 0.

---

## Phase Transitions

End of each phase, the coach asks:
1. Did you hit the phase goals? (yes / mostly / no)
2. Confidence level on phase outcomes (1-10)
3. Top 3 carry-over weaknesses
4. Adjust next phase, or proceed as planned?

If "no" or confidence <6, the **default is to extend by 1 week**, not to compress the next phase. Extensions come out of Phase 5 first (it has 11 weeks and can shrink to 8), then Phase 6 (10 → 8). Phase 7 never shrinks.
