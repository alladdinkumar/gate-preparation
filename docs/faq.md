# FAQ

---

### Q: I missed a few days. Should I delete those daily logs?

**A: No.** Leave them. If you didn't study, create the file anyway with "skipped — reason: __" in the Reflection section. **Skipped days are data.** Patterns of skipping reveal more than streak counts ever do.

---

### Q: Should I study on Sunday to catch up?

**A: No.** Sunday rest is non-negotiable. Recovery is when consolidation happens. 72 weeks is a marathon — you'll perform worse on Monday morning, and worse in month 12, if you grind Sundays.

---

### Q: I want to add a topic that's not in the plan. How?

**A: First check `plan/syllabus.md`.** If it's not in the official syllabus, it's not worth marks — don't add it. If it *is* in the syllabus and the plan somehow misses it, write it in your weekly review's "Plan adjustments" section; the coach fixes the plan at month-end.

---

### Q: I'm ahead of schedule. Can I move to the next subject early?

**A: Be cautious.** Check the exit criteria of your current phase and the accuracy numbers in `trackers/subjects.md`. If every row is at confidence ≥3 and accuracy ≥60%, you can move on. If you're just bored, you're not done — use the extra days on error-log redos and the weakest rows. Spare time is never wasted in GATE prep; it goes into Phase 6 mocks.

---

### Q: I'm behind. Should I extend the subject?

**A: Yes — by default.** Compressing the next subject is how plans collapse. Extensions come out of Phase 5 first (11 weeks → minimum 8), then Phase 6 (10 → 8). Phase 7 never shrinks.

If you're behind 3+ weeks total, do a monthly re-scope: merge revision weeks for the lowest-weight subjects. Don't skip a subject — every one is worth 5+ marks.

---

### Q: I solved a PYQ but peeked at a hint / the discussion. Does it count?

**A: Count it as wrong.** "Correct" means right on the first timed attempt with no help. Log it in the error log with the error type you'd have hit. The point is to surface weakness, not to game your own accuracy.

---

### Q: I keep watching lectures but not doing PYQs. How do I stop?

**A: Hard rule: no lecture without PYQs.** Tomorrow morning's PYQs must be on tonight's lecture topic. If yesterday's PYQs weren't done, tonight's slot is PYQs, not a new lecture. Lectures are passive; PYQs are the exam.

---

### Q: Isn't it wasteful to solve old PYQs from 2000–2010? The pattern has changed.

**A: The concepts haven't.** Old questions are shorter and more conceptual — ideal for the first pass. The newer style (MSQ, harder NATs) shows up in 2015–2021 practice and fully in the sealed 2022+ mocks. Skip any old question whose topic is no longer in `syllabus.md` (e.g. software engineering, web technologies).

---

### Q: Why can't I look at 2022+ papers?

**A: They're your only truly unseen, current-pattern full papers.** Once you've seen a question, that paper is no longer a mock — it's a quiz you remember. Sealing them is what makes Phase 6 scores meaningful.

---

### Q: Should I buy a test series / paid course?

**A: Not before the Week 59 monthly review.** The plan is free-only: GO Classes free playlists, NPTEL, GATE Overflow PYQs and PDFs are enough to reach a top rank — the gap is almost never resources, it's practice volume and error analysis. The one exception worth discussing at Week 59: if the free full-length pool (sealed papers + free all-India mocks) can't supply ~20 unseen papers for Phases 6–7.

---

### Q: Should I take GATE 2027 as a practice attempt?

**A: The coach's position is yes** (see `plan/exam-info.md`): a real exam experience costs a fee and a weekend. But you must pre-commit that the score is a diagnostic, not a verdict — at that point you'll have covered only ~40–45 marks of syllabus. Registration closes 27 Sep 2026 (5 Oct with late fee).

---

### Q: What about the PSU age limit?

**A: Check it on Day 0, not in 2028.** PSU notifications set their own upper age limits and cut-off dates (typically in the 25–28 range for general category, with relaxations for reserved categories). If you're outside the limit for most target PSUs, the plan doesn't change — the goal line shifts to "IIT/IISc M.Tech, and PSUs where eligible". A 75+ score serves both.

---

### Q: Should I tell my manager I'm preparing for GATE?

**A: Your call — but you don't need to.** It's 19 hours a week outside work hours. You'll only need leave for the exam day (and possibly interviews later). Don't let prep leak into work hours; that creates problems you don't need.

---

### Q: What if I get a strong job offer mid-prep?

**A: Evaluate it on its own merits.** The plan exists to serve a career goal, not the other way round. If the offer beats what a PSU / M.Tech would give you, taking it is a legitimate outcome. You can pause the plan and log the decision in a monthly review — the markdown will still be here.

---

### Q: My daily log is getting tedious. Can I skip sections?

**A: Skip the Interleaved Quiz and GA sections on days they don't apply.** Don't skip:
- YAML frontmatter (machines parse this)
- Questions Attempted entries (data)
- Error-log rows (the most valuable data in the system)
- Reflection section (your future self needs this)

If the template feels long, that's a sign to streamline the template, not to skip filling it. Bring it up in the monthly review.

---

### Q: What if Claude Code is unavailable?

**A: This system works without Claude.** Everything is plain markdown. You can do weekly reviews by hand (open the 6 logs, fill in the template). Claude accelerates the busywork; it doesn't enable the system.

---

### Q: How do I handle the moment of "I don't want to do this today"?

**A: Show up anyway. Cut the session in half.** 45 minutes of PYQs today beats 0 today and "I'll do double tomorrow" (you won't). The friction of starting is the highest barrier. Once you open the daily log and attempt the first question, momentum usually arrives. If 30 minutes in you genuinely have nothing left, stop and log honestly.

The rule: **negotiate down, not down to zero.**

---

### Q: My family is unhappy with the time commitment.

**A: This is a real concern, and 72 weeks is long.** The time budget:
- 1.5h before work
- 1.5h after work (yes, this is family time)
- 4h Saturday morning (Saturday afternoon and all of Sunday stay free)

Conversations to have:
- "This is finite — the exam is Feb 2028" — give the date
- "I'll keep [X commitment] no matter what" — explicit carve-out
- "I need [Y support]" — specific ask

Don't sneak prep time. Be upfront, get buy-in, deliver. If you genuinely can't get the time, **reduce the plan** (e.g. 14h/week and push the target to GATE 2029) rather than compromising both family and prep.

---

### Q: What if my GATE score isn't good enough?

**A: That's data.** After the exam:

1. Compute your score from the official key and log it in `trackers/mocks.md`
2. Compare section-wise with your mock averages — where did the exam diverge from mocks?
3. Write `reviews/monthly/2028-02.md` honestly: coverage gap, accuracy gap, or exam-day execution gap?
4. Decide consciously: another attempt (the system, notes and error log carry over), M.Tech with the score you have, or a different path

A GATE score is valid for 3 years, and plenty of top rankers had a previous attempt. It's normal.

---

### Q: When can I delete this whole `Gate Preparation/` folder?

**A: After you've joined wherever the score takes you and settled in.** Keep the notes and formula sheets — they're a compact CS reference. Otherwise: archive (zip + cloud) and delete locally if it bothers you.
