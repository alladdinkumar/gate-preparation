# Error Log

**The most important file in this repo.** Every wrong, guessed, or slow-but-correct-by-luck question gets a row — from daily PYQs, Saturday tests, quizzes and mocks. At GATE's PSU cut-offs, rank is decided by the mistakes you stop repeating.

**Append-only.** Never delete a row. Mark it redone.

---

## How to Use

1. **Log immediately** after the attempt (morning session, or test analysis). Don't batch it for Sunday.
2. **Error type** — pick exactly one:
   - `concept` — didn't know / misunderstood the idea
   - `formula` — knew the idea, forgot or misapplied the formula
   - `calculation` — arithmetic / calculator / unit slip
   - `misread` — misread the question, options, "NOT", or NAT rounding instruction
   - `time` — could solve, ran out of time or abandoned
   - `guess` — attempted without knowing (right or wrong — both get logged)
3. **Correct idea** — one line in your own words: what makes this question solvable. Not the full solution.
4. **Redo date** — next morning for daily PYQs; +3 days for test / mock errors.
5. **Redo result** — `✓` solved cleanly without looking, `✗` failed again (re-schedule +3 days and add a new redo date), `✓✓` solved cleanly twice (row closed).
6. **Sunday review:** count rows by error type and subject. The dominant error type is next week's fix.

**ID format:** `E-<week>-<n>` — e.g. `E-3-07` is the 7th error logged in Week 3.

---

## Log

| ID | Date | Source (year-Q# / test ID) | Subject | Topic (syllabus ID) | Type | Marks | Error type | Correct idea (one line) | Redo date | Redo result |
|----|------|----------------------------|---------|---------------------|------|-------|------------|--------------------------|-----------|-------------|
| E-1-01 | 2026-09-15 | (example) GATE-2008-Q__ | C | PD-1 | MCQ | 2 | misread | Postfix `++` returns old value; precedence ≠ evaluation order | 2026-09-16 | — |

---

## Weekly Error Summary (fill every Sunday)

| Week | Rows added | concept | formula | calculation | misread | time | guess | Redone ✓ | Redone ✗ | Open backlog |
|------|------------|---------|---------|-------------|---------|------|-------|----------|----------|--------------|
| 1 | __ | __ | __ | __ | __ | __ | __ | __ | __ | __ |

**Backlog rule:** open (not ✓✓) rows >40 → next morning session is redo-only (see `plan/PLAN.md` coach thresholds).

---

## Recurring Traps (promote here when the same mistake appears 3+ times)

These become `notes/formula-sheets/top-30-traps.md` in Phase 7.

| # | Trap | Subjects | First seen | Times repeated |
|---|------|----------|------------|----------------|
| — | — | — | — | — |
