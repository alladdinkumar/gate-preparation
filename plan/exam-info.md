# Exam Info — GATE CS, PSU Route, Day 0 Checklist

Everything about the exam itself: pattern, marking, dates, PSU route, eligibility. Replaces `company-targets.md` from the Study system.

> **Facts in this file expire.** Every date and eligibility rule must be re-verified against the official brochure / notification before acting on it. Last verified: 2026-09-13 against gate2027.iitm.ac.in.

---

## Day 0 Checklist (do on Sun 2026-09-13, before Week 1)

- [ ] **PSU age eligibility.** Pull the last 2 years of GATE-based recruitment notifications for your target PSUs (list below). Note each one's upper age limit and the date age is counted on. Compute your age on those dates in **2028**. Write the result in `trackers/progress.md` → Current State.
  - If eligible for ≥2 target PSUs: plan proceeds as is.
  - If eligible for 0–1: tell the coach. The plan (syllabus, phases, hours) doesn't change — the goal line changes to "IIT/IISc M.Tech or PSU where eligible", and the target score stays 75+.
- [ ] **Category relaxation.** Check whether any age relaxation (OBC-NCL / SC / ST / PwD / other) applies to you.
- [ ] **Decide on a GATE 2027 practice attempt** (see below). Deadline: 27 Sep 2026 regular, 5 Oct 2026 with late fee.
- [ ] **DigiLocker.** GATE 2027 made DigiLocker registration mandatory for Indian nationals — set it up now, you'll need it for 2028 too.
- [ ] Download the GATE Overflow PDFs (see `resources.md`) and bookmark the TCS iON virtual calculator.

---

## Exam Pattern (GATE CS — as of GATE 2026/2027)

| Item | Value |
|------|-------|
| Duration | 3 hours, computer-based |
| Questions | 65 |
| Total marks | 100 |
| General Aptitude | 10 questions — 5 × 1 mark + 5 × 2 marks = 15 marks |
| Engineering Maths + CS | 55 questions — 25 × 1 mark + 30 × 2 marks = 85 marks |
| Question types | MCQ (one correct), MSQ (one or more correct), NAT (numerical answer, typed) |
| Calculator | On-screen virtual calculator only (no physical calculator) |

### Marking scheme

| Type | Correct | Wrong | Notes |
|------|---------|-------|-------|
| MCQ, 1 mark | +1 | −1/3 | Only MCQs carry negative marks |
| MCQ, 2 marks | +2 | −2/3 | |
| MSQ | +1 / +2 | 0 | No negative, no partial credit — all correct options needed |
| NAT | +1 / +2 | 0 | No negative. Watch the rounding / range instruction |

**Implications you drill in every mock:**
- NAT and MSQ are free attempts — never leave one blank if you have any working.
- MCQ guessing is expected-value positive only if you can eliminate ≥2 of 4 options. Below ~50% confidence, skip.
- MSQ is unforgiving — one wrong option = 0. Verify every option independently.

---

## GATE 2027 (for reference + optional practice attempt)

| Item | Value (verified 2026-09-13) |
|------|------------------------------|
| Organising institute | IIT Madras |
| Website | https://gate2027.iitm.ac.in |
| Registration (GOAPS) | Opened 2 Sep 2026 → closes 27 Sep 2026 (regular), 5 Oct 2026 (late fee) |
| Exam dates | 6, 7, 13, 14, 20, 21 Feb 2027 |
| Results | 19 Mar 2027 |
| Fee | See the official brochure |

### Should you take GATE 2027 as a practice attempt?

**Coach position: yes, take it** — but only as a rehearsal, never as a target.

- By 6–21 Feb 2027 (Weeks 21–23) you'll have covered C, DS, Discrete Maths, Algorithms, Linear Algebra, Calculus, Probability and most of Digital Logic, plus 20+ weeks of GA — roughly 40–45 marks of syllabus.
- What you get: a real centre, real interface, real nerves, a real score calibration — for the cost of a fee and one weekend.
- What it costs: the fee, 1–2 days, and a low score you must not read as a verdict. Pre-commit now: the score goes in `trackers/mocks.md` as a diagnostic, nothing more.
- If you skip it: no plan change. Week 21–23 Saturdays stay as topic tests.

---

## GATE 2028 (your attempt)

| Item | Status |
|------|--------|
| Organising institute | Not yet announced — check ~mid 2027 |
| Brochure | Expected ~Jul/Aug 2027 (GATE 2027's came out 20 Jul 2026) |
| Registration | Expected ~Sep 2027 → falls in **Phase 5, Weeks 52–55**. Hard reminder in the Phase 5 file |
| Exam | Expected early–mid Feb 2028. Plan's structured weeks end 2028-01-30; the exam window follows |
| Syllabus | Re-check against `syllabus.md` the day the brochure is released |

---

## PSU Route (GATE CS)

**How it works:** PSUs publish recruitment notifications (usually after GATE registration or near results, varies by PSU) that name the GATE year(s) they accept. You apply separately to each PSU with your GATE registration number. Shortlisting is by GATE score/rank, then group discussion / interview / medical, depending on the PSU. Selection weightage (GATE vs interview) varies by PSU.

**PSUs / organisations that have used GATE CS scores in recent cycles** (the list changes every year; many PSUs skip CS in some years — verify each notification):

| Organisation | Notes |
|--------------|-------|
| IOCL | Historically among the most competitive CS openings |
| GAIL | |
| BHEL | |
| PGCIL (POWERGRID) | |
| NLC India (NLCIL) | |
| NPCIL | Branches recruited vary year to year |
| ECIL | |
| NFL | |
| BARC (OCES / DGFS) | Uses GATE score for interview shortlisting; separate selection interview |
| NIC / others | Occasional |

**Age limits (typical, verify per notification):** general category upper limit usually in the **25–28 years** range, counted on a date the notification specifies. Common relaxations: OBC-NCL +3 years, SC/ST +5 years, PwD +10 years.

**Cut-offs:** don't trust coaching-site "expected cut-off" numbers. Track the actual shortlisting ranks each PSU publishes for GATE 2026 and 2027 CS, and add them here during the monthly review when they appear.

| PSU | GATE year | Shortlist cut-off (score / AIR) | Source | Added on |
|-----|-----------|----------------------------------|--------|----------|
| — | — | — | — | — |

---

## Exam-Day Strategy (drilled in Phases 6–7, written here so it never changes mid-exam)

1. **Pass 1 (0:00–1:30):** GA first (~20 min, target 13+/15), then the technical section in order — attempt only what you can solve in <3 min. Mark everything else.
2. **Pass 2 (1:30–2:40):** Marked 2-mark NATs and MSQs you have working for, then long calculations.
3. **Pass 3 (2:40–2:55):** Leftover MCQs only if you can eliminate 2 options. Otherwise leave blank.
4. **Last 5 min:** Re-check NAT entries (units, rounding) and unanswered-but-attempted status.
5. Virtual calculator: practise it every Saturday from Week 1 — no mental-maths pride on NATs.
