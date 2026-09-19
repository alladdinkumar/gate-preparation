# Phase 2 — Algorithms + Engineering Maths + Digital Logic (Weeks 11–22)

**Dates:** 2026-11-23 → 2027-02-14 (12 weeks)
**Budget:** ~228 hours (19h/week)
**Subjects:** Algorithms (Wk 11–14) · Linear Algebra (Wk 15) · Calculus (Wk 16) · Probability & Statistics (Wk 17–18) · Digital Logic (Wk 19–22)
**Theme:** Finish all of mathematics and the analytical core. By the end of this phase, ~45 marks of syllabus have been through a first pass.

---

## Why This Phase Exists

Algorithms turns Phase 1's C, DS and Discrete Maths into analysis: complexity, recurrences, design techniques. Doing it straight after Discrete Maths means recurrences and graph theory are still fresh.

The rest of Engineering Maths (LA, Calculus, Probability) is short, formula-driven and very scoreable. Finishing it here gives it 12+ months to settle before the exam.

Digital Logic closes the phase because COA opens the next one — number representation, adders and flip-flops are COA's vocabulary.

---

## Phase Goals (end-of-phase state)

- [ ] Syllabus rows AL-1 … AL-10, LA-1 … LA-5, CA-1 … CA-5, PS-1 … PS-5, DL-1 … DL-8 at confidence ≥3
- [ ] PYQ accuracy ≥60% in Algorithms, LA + Calculus, Probability, Digital Logic
- [ ] Formula sheets complete: `algorithms.md`, `engineering-maths.md`, `digital-logic.md`
- [ ] Phase 1 subjects kept alive: R2 revision of C, DS, DM logged in `trackers/revision.md`
- [ ] GA mixed-set score ≥10/15
- [ ] Adherence ≥70%

---

## How to Read the Weekly Tables

Same conventions as Phase 1:
- Lecture = primary GO Classes series; map video numbers on the subject's first day.
- PYQ Split Rule: weekday AM = even years + 2021; Saturday = odd years; 2022+ sealed.
- Every AM starts with error-log redos. Every PM ends with Reflection.
- **New in Phase 2:** the first Saturday of each new subject spends 15 min of the 12:00–13:00 slot on a **R2 revision** of an older subject (listed in the row).

---

## Weekly Breakdown

### Week 11 — Algorithms: Asymptotics + Recurrences (2026-11-23 → 2026-11-29)
**Hours: 19** | **Topics: AL-1, AL-2** | **GA rotation 2: Grammar**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; even-year PYQs on graph matching / colouring (carried from Week 10). Map Algorithms playlist → Weeks 11–14 | GO PYQs; GO Classes Algorithms | Error log; mapping |
| Mon | PM | Lecture: asymptotic notations O, Ω, Θ, o, ω; comparing growth rates (log, poly, exp, factorial) | GO Classes Algorithms | `notes/algorithms/al-01-asymptotic.md` |
| Tue | AM | PYQs: order functions by growth, true/false notation statements | GO tag asymptotic-notation | Daily log + error log |
| Tue | PM | Lecture: time + space complexity of loops (nested, logarithmic, dependent loops), recursive code | GO Classes Algorithms | `al-01` (complete) |
| Wed | AM | PYQs: loop complexity (NAT / MCQ) | GO tag time-complexity | Daily log + error log |
| Wed | PM | Lecture: recurrences — substitution method, recursion tree | GO Classes Algorithms | `notes/algorithms/al-02-recurrences.md` |
| Thu | AM | PYQs: solve recurrences by tree / substitution | GO tag recurrence-relation | Daily log + error log |
| Thu | PM | Lecture: master theorem (all 3 cases + extended form), when it doesn't apply, change of variables | GO Classes Algorithms | `al-02` (complete) |
| Fri | AM | PYQs: master theorem | GO tag master-theorem | Daily log + error log |
| Fri | PM | Start `notes/formula-sheets/algorithms.md` (growth-rate ladder, master theorem cases); concept repair | Own notes / backup: NPTEL DAA (Mukund) | Formula sheet (start) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs AL-1, AL-2 + 5 DM carry-over | GO PYQs (odd years) | Topic test T11 |
| Sat | 11:00–12:00 | GA rotation 2 — Grammar | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: C** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #11 **+ Monthly review (November 2026)** | — | `reviews/weekly/2026-11-23-to-2026-11-29.md` + `reviews/monthly/2026-11.md` |

---

### Week 12 — Algorithms: Searching, Sorting, Hashing, Divide & Conquer (2026-11-30 → 2026-12-06)
**Hours: 19** | **Topics: AL-3, AL-4, AL-5** | **GA rotation 3: Data interpretation**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs AL-1, AL-2 | GO PYQs | Error log |
| Mon | PM | Lecture: searching (linear, binary — comparisons count); elementary sorts (insertion, selection, bubble) — swaps, comparisons, stability, in-place | GO Classes Algorithms | `notes/algorithms/al-03-searching-sorting.md` |
| Tue | AM | PYQs: binary search, elementary sort comparisons / swaps (NAT) | GO tag sorting | Daily log + error log |
| Tue | PM | Lecture: merge sort, quick sort (partition schemes, best / worst / average), heap sort; comparison-sort lower bound; counting + radix sort | GO Classes Algorithms | `al-03` (complete) |
| Wed | AM | PYQs: quick / merge / heap sort behaviour on given inputs | GO tag quick-sort, merge-sort | Daily log + error log |
| Wed | PM | Lecture: hashing — hash functions, chaining, open addressing (linear, quadratic, double hashing), load factor, expected probes | GO Classes Algorithms | `notes/algorithms/al-04-hashing.md` |
| Thu | AM | PYQs: hash table contents, probes (NAT) | GO tag hashing | Daily log + error log |
| Thu | PM | Lecture: divide and conquer — recurrence set-up, max-min, binary search, merge sort analysis, matrix multiplication (Strassen), closest pair idea | GO Classes Algorithms | `notes/algorithms/al-05-divide-conquer.md` |
| Fri | AM | PYQs: divide and conquer | GO tag divide-and-conquer | Daily log + error log |
| Fri | PM | Sorting comparison table into the formula sheet (best / avg / worst / space / stable / in-place) | Own notes | `notes/formula-sheets/algorithms.md` |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs AL-3 … AL-5 | GO PYQs (odd years) | Topic test T12 |
| Sat | 11:00–12:00 | GA rotation 3 — Data interpretation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #12 | — | `reviews/weekly/2026-11-30-to-2026-12-06.md` |

---

### Week 13 — Algorithms: Greedy, Graph Traversals, MST (2026-12-07 → 2026-12-13)
**Hours: 19** | **Topics: AL-6, AL-7, AL-8** | **GA rotation 4: Logic + reasoning**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs AL-3 … AL-5 | GO PYQs | Error log |
| Mon | PM | Lecture: greedy — activity selection, fractional knapsack, job sequencing with deadlines, optimal merge pattern | GO Classes Algorithms | `notes/algorithms/al-06-greedy.md` |
| Tue | AM | PYQs: greedy choices, job sequencing | GO tag greedy-algorithms | Daily log + error log |
| Tue | PM | Lecture: Huffman coding — tree construction, average code length, number of bits | GO Classes Algorithms | `al-06` (complete) |
| Wed | AM | PYQs: Huffman (NAT) | GO tag huffman-code | Daily log + error log |
| Wed | PM | Lecture: BFS, DFS, discovery / finish times, edge classification, topological sort, connected + strongly connected components | GO Classes Algorithms | `notes/algorithms/al-07-graph-traversals.md` |
| Thu | AM | PYQs: DFS / BFS order, topological orderings count, SCCs | GO tag dfs, bfs, topological-sort | Daily log + error log |
| Thu | PM | Lecture: MST — cut property, Kruskal, Prim (with heap), uniqueness, MST edge must / may questions | GO Classes Algorithms | `notes/algorithms/al-08-mst.md` |
| Fri | AM | PYQs: MST weight, edge inclusion | GO tag minimum-spanning-tree | Daily log + error log |
| Fri | PM | Graph algorithms complexity table + worked Kruskal / Prim on paper | Own notes / backup: Abdul Bari | `notes/formula-sheets/algorithms.md` |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs AL-6 … AL-8 | GO PYQs (odd years) | Topic test T13 |
| Sat | 11:00–12:00 | GA rotation 4 — Logic + reasoning | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Data Structures** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #13 | — | `reviews/weekly/2026-12-07-to-2026-12-13.md` |

---

### Week 14 — Algorithms: Shortest Paths + Dynamic Programming (2026-12-14 → 2026-12-20)
**Hours: 19** | **Topics: AL-9, AL-10** | **GA rotation 5: Vocabulary + reading**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs AL-6 … AL-8 | GO PYQs | Error log |
| Mon | PM | Lecture: single-source shortest paths — relaxation, Dijkstra (and why negative edges break it) | GO Classes Algorithms | `notes/algorithms/al-09-shortest-paths.md` |
| Tue | AM | PYQs: Dijkstra order / distances | GO tag dijkstras-algorithm | Daily log + error log |
| Tue | PM | Lecture: Bellman–Ford (negative cycles), Floyd–Warshall, all-pairs complexity comparison | GO Classes Algorithms | `al-09` (complete) |
| Wed | AM | PYQs: shortest paths mixed | GO tag shortest-path | Daily log + error log |
| Wed | PM | Lecture: dynamic programming principles — overlapping subproblems, optimal substructure; LCS | GO Classes Algorithms | `notes/algorithms/al-10-dynamic-programming.md` |
| Thu | AM | PYQs: LCS table values (NAT) | GO tag dynamic-programming | Daily log + error log |
| Thu | PM | Lecture: 0/1 knapsack, subset sum, edit distance | GO Classes Algorithms | `al-10` |
| Fri | AM | PYQs: knapsack / subset sum DP | GO tag dynamic-programming | Daily log + error log |
| Fri | PM | Lecture: matrix chain multiplication, optimal BST idea; DP recurrence → table-fill order | GO Classes Algorithms | `al-10` (complete) + `notes/formula-sheets/algorithms.md` (complete) |
| Sat | 09:00–11:00 | **Algorithms subject test:** ~30 odd-year PYQs AL-1 … AL-10 | GO PYQs (odd years) | Topic test T14 |
| Sat | 11:00–12:00 | GA rotation 5 — Vocabulary + reading / sequencing | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis; **R1 revision: Algorithms** (skim all notes) | — | `trackers/revision.md` |
| Sun | — | Weekly review #14 | — | `reviews/weekly/2026-12-14-to-2026-12-20.md` |

**Resources:**
- GO Classes Algorithms — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHjUCHdJp-_soSSmhgmO4i0T
- Backup: NPTEL Design and Analysis of Algorithms (Madhavan Mukund) — https://nptel.ac.in/courses/106106131
- Backup: Abdul Bari — https://www.youtube.com/@abdul_bari
- Reference: CLRS Ch 2–4, 6–8, 11, 15–16, 22–25

---

### Week 15 — Linear Algebra (2026-12-21 → 2026-12-27)
**Hours: 19** | **Topics: LA-1 … LA-5** | **GA rotation 6: Mensuration + geometry**

Holiday week (25 Dec). If you're travelling, apply the "heavy week" rule from `weekly-schedule.md`: mornings only, and LA extends into Week 16's Monday.

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs AL-9, AL-10. Map LA playlist | GO PYQs; GO Classes Linear Algebra | Error log; mapping |
| Mon | PM | Lecture: matrices — types, operations, row echelon form, rank, inverse | GO Classes Linear Algebra | `notes/maths/la-01-matrices-rank.md` |
| Tue | AM | PYQs: rank, matrix properties | GO tag rank-of-matrix | Daily log + error log |
| Tue | PM | Lecture: determinants — properties, cofactor expansion, determinant of special / structured matrices | GO Classes Linear Algebra | `notes/maths/la-02-determinants.md` |
| Wed | AM | PYQs: determinants | GO tag determinant | Daily log + error log |
| Wed | PM | Lecture: systems of linear equations — consistency, unique / infinite / no solution, rank method, homogeneous systems | GO Classes Linear Algebra | `notes/maths/la-03-linear-systems.md` |
| Thu | AM | PYQs: systems of equations | GO tag system-of-equations | Daily log + error log |
| Thu | PM | Lecture: eigenvalues + eigenvectors — characteristic equation, properties (trace, determinant, powers, inverse, triangular), Cayley–Hamilton, diagonalisability | GO Classes Linear Algebra | `notes/maths/la-04-eigen.md` |
| Fri | AM | PYQs: eigenvalues (NAT) | GO tag eigen-value | Daily log + error log |
| Fri | PM | Lecture: LU decomposition (Doolittle / Crout) + LA property sheet | GO Classes Linear Algebra / backup: MIT 18.06 | `notes/maths/la-05-lu-decomposition.md` + `engineering-maths.md` (LA section) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs LA-1 … LA-5 (top up with pre-2000 if short) | GO PYQs (odd years) | Topic test T15 |
| Sat | 11:00–12:00 | GA rotation 6 — Mensuration + geometry | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Discrete Maths (logic, relations)** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #15 **+ Monthly review (December 2026)** | — | `reviews/weekly/2026-12-21-to-2026-12-27.md` + `reviews/monthly/2026-12.md` |

---

### Week 16 — Calculus (2026-12-28 → 2027-01-03)
**Hours: 19** | **Topics: CA-1 … CA-5** | **GA rotation 7: Statistics + probability + PnC**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year LA PYQs | GO PYQs | Error log |
| Mon | PM | Lecture: limits — standard limits, indeterminate forms, L'Hôpital's rule | GO Classes free Engineering Mathematics course | `notes/maths/ca-01-limits.md` |
| Tue | AM | PYQs: limits (NAT) | GO tag limits | Daily log + error log |
| Tue | PM | Lecture: continuity + differentiability — piecewise functions, points of non-differentiability | GO Classes Engineering Mathematics | `notes/maths/ca-02-continuity-differentiability.md` |
| Wed | AM | PYQs: continuity / differentiability | GO tag continuity, differentiation | Daily log + error log |
| Wed | PM | Lecture: maxima and minima — first / second derivative tests, closed-interval extrema | GO Classes Engineering Mathematics | `notes/maths/ca-03-maxima-minima.md` |
| Thu | AM | PYQs: maxima / minima | GO tag maxima-minima | Daily log + error log |
| Thu | PM | Lecture: mean value theorems (Rolle's, Lagrange's) | GO Classes Engineering Mathematics | `notes/maths/ca-04-mean-value-theorem.md` |
| Fri | AM | PYQs: mean value theorem | GO tag mean-value-theorem | Daily log + error log |
| Fri | PM | Lecture: integration — definite integrals, properties (symmetry, King's rule), substitution, by parts | GO Classes Engineering Mathematics / backup: 3Blue1Brown Essence of Calculus | `notes/maths/ca-05-integration.md` + `engineering-maths.md` (calculus section) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs LA + Calculus (top up with pre-2000) | GO PYQs (odd years) | Topic test T16 |
| Sat | 11:00–12:00 | GA rotation 7 — Statistics + probability + PnC | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #16 | — | `reviews/weekly/2026-12-28-to-2027-01-03.md` |

---

### Week 17 — Probability 1: Conditional Probability, Random Variables, Statistics (2027-01-04 → 2027-01-10)
**Hours: 19** | **Topics: PS-1, PS-2, PS-3** | **GA rotation 8: Spatial aptitude**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year calculus PYQs | GO PYQs | Error log |
| Mon | PM | Lecture: probability axioms, sample spaces, counting-based probability, independence | GO Classes Engineering Mathematics | `notes/maths/ps-01-conditional-bayes.md` |
| Tue | AM | PYQs: basic probability | GO tag probability | Daily log + error log |
| Tue | PM | Lecture: conditional probability, total probability, Bayes theorem | GO Classes Engineering Mathematics | `ps-01` (complete) |
| Wed | AM | PYQs: conditional + Bayes (NAT) | GO tag conditional-probability, bayes-theorem | Daily log + error log |
| Wed | PM | Lecture: random variables — PMF, PDF, CDF; expectation, variance; linearity of expectation + indicator variables | GO Classes Engineering Mathematics | `notes/maths/ps-02-random-variables.md` |
| Thu | AM | PYQs: expectation, variance | GO tag random-variable, expectation | Daily log + error log |
| Thu | PM | Lecture: mean, median, mode, standard deviation (grouped / ungrouped), effect of transformations | GO Classes Engineering Mathematics | `notes/maths/ps-03-descriptive-stats.md` |
| Fri | AM | PYQs: descriptive statistics | GO tag statistics | Daily log + error log |
| Fri | PM | Concept repair: expected number of trials / indicator-variable problems | Backup: MIT RES.6-012 (Tsitsiklis) | `ps-02` worked examples |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs PS-1 … PS-3 | GO PYQs (odd years) | Topic test T17 |
| Sat | 11:00–12:00 | GA rotation 8 — Spatial aptitude | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Discrete Maths (counting, graphs)** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #17 | — | `reviews/weekly/2027-01-04-to-2027-01-10.md` |

---

### Week 18 — Probability 2: Distributions + Maths Consolidation (2027-01-11 → 2027-01-17)
**Hours: 19** | **Topics: PS-4, PS-5** | **GA rotation 9: Mixed timed GA section**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs PS-1 … PS-3 | GO PYQs | Error log |
| Mon | PM | Lecture: Bernoulli + binomial distribution (mean, variance, when to use) | GO Classes Engineering Mathematics | `notes/maths/ps-04-binomial-poisson.md` |
| Tue | AM | PYQs: binomial | GO tag binomial-distribution | Daily log + error log |
| Tue | PM | Lecture: Poisson distribution, Poisson as a binomial limit | GO Classes Engineering Mathematics | `ps-04` (complete) |
| Wed | AM | PYQs: Poisson | GO tag poisson-distribution | Daily log + error log |
| Wed | PM | Lecture: uniform + exponential distributions, memoryless property | GO Classes Engineering Mathematics | `notes/maths/ps-05-continuous-distributions.md` |
| Thu | AM | PYQs: uniform, exponential | GO tag uniform-distribution, exponential-distribution | Daily log + error log |
| Thu | PM | Lecture: normal distribution, standardisation, symmetry-based probability | GO Classes Engineering Mathematics | `ps-05` (complete) |
| Fri | AM | PYQs: normal distribution + mixed probability | GO tag normal-distribution | Daily log + error log |
| Fri | PM | **Finish `notes/formula-sheets/engineering-maths.md`** — distribution table (PMF/PDF, mean, variance) + read the whole sheet once | Own notes | Formula sheet (complete) |
| Sat | 09:00–11:00 | **Engineering Maths subject test:** ~30 odd-year PYQs across LA, Calculus, Probability (+ 5 DM) | GO PYQs (odd years) | Topic test T18 |
| Sat | 11:00–12:00 | GA rotation 9 — one full GA section, 25 min timed, score /15 | GA PYQs | `trackers/aptitude.md` mixed-set score |
| Sat | 12:00–13:00 | Error analysis, maths confidence ratings in `subjects.md` | — | Error log |
| Sun | — | Weekly review #18 | — | `reviews/weekly/2027-01-11-to-2027-01-17.md` |

**Resources:**
- GO Classes Linear Algebra — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHhGLQ1ZT37KLpBMAD90CM4_
- GO Classes free Engineering Mathematics course — https://www.goclasses.in
- Backup: MIT OCW 18.06 — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- Backup: MIT OCW RES.6-012 Introduction to Probability — https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/
- Reference: Kreyszig — Advanced Engineering Mathematics

---

### Week 19 — Digital Logic: Number Representation + Boolean Algebra (2027-01-18 → 2027-01-24)
**Hours: 19** | **Topics: DL-1 … DL-4** | **GA rotation 1: Numerical computation**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs PS-4, PS-5. Map DL playlist → Weeks 19–22 | GO PYQs; GO Classes Digital Logic | Error log; mapping |
| Mon | PM | Lecture: number systems, base conversions, signed magnitude, 1's and 2's complement, BCD, Gray code | GO Classes Digital Logic | `notes/digital-logic/dl-01-number-systems.md` |
| Tue | AM | PYQs: conversions, complement representation | GO tag number-representation | Daily log + error log |
| Tue | PM | Lecture: fixed point — range of n-bit representations, signed arithmetic, overflow detection | GO Classes Digital Logic | `notes/digital-logic/dl-02-fixed-point.md` |
| Wed | AM | PYQs: range + overflow (NAT) | GO tag number-representation, overflow | Daily log + error log |
| Wed | PM | Lecture: floating point — IEEE 754 single / double, bias, normalised vs denormalised, special values, precision | GO Classes Digital Logic | `notes/digital-logic/dl-03-ieee754.md` |
| Thu | AM | PYQs: IEEE 754 hex ↔ decimal | GO tag ieee-representation | Daily log + error log |
| Thu | PM | Lecture: Boolean algebra — laws, duality, SOP / POS, canonical forms, algebraic minimisation, functionally complete sets, self-dual functions | GO Classes Digital Logic | `notes/digital-logic/dl-04-boolean-algebra.md` |
| Fri | AM | PYQs: Boolean identities, functional completeness, counting Boolean functions | GO tag boolean-algebra | Daily log + error log |
| Fri | PM | Start `notes/formula-sheets/digital-logic.md` — representation ranges, IEEE 754 layout; concept repair | Own notes / backup: Neso Academy | Formula sheet (start) |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs DL-1 … DL-4 | GO PYQs (odd years) | Topic test T19 |
| Sat | 11:00–12:00 | GA rotation 1 — Numerical computation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Algorithms** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #19 | — | `reviews/weekly/2027-01-18-to-2027-01-24.md` |

---

### Week 20 — Digital Logic: Minimisation + Combinational Circuits (2027-01-25 → 2027-01-31)
**Hours: 19** | **Topics: DL-5, DL-6** | **GA rotation 2: Grammar**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DL-1 … DL-4 | GO PYQs | Error log |
| Mon | PM | Lecture: K-maps (2–4 variables), don't-cares, prime + essential prime implicants | GO Classes Digital Logic | `notes/digital-logic/dl-05-kmap-tabular.md` |
| Tue | AM | PYQs: K-map minimisation, counting prime implicants (NAT) | GO tag k-map | Daily log + error log |
| Tue | PM | Lecture: 5-variable K-maps, tabular (Quine–McCluskey) method | GO Classes Digital Logic | `dl-05` (complete) |
| Wed | AM | PYQs: minimal SOP / POS | GO tag min-sum-of-products-form | Daily log + error log |
| Wed | PM | Lecture: combinational — half / full adder, ripple-carry, carry-lookahead, subtractor, gate-delay calculation | GO Classes Digital Logic | `notes/digital-logic/dl-06-combinational.md` |
| Thu | AM | PYQs: adders, delays | GO tag combinational-circuit | Daily log + error log |
| Thu | PM | Lecture: MUX (implementing functions), decoder, encoder, priority encoder, comparator | GO Classes Digital Logic | `dl-06` (complete) |
| Fri | AM | PYQs: MUX-based function implementation | GO tag multiplexer | Daily log + error log |
| Fri | PM | Untimed practice: implement 3 functions with 4:1 / 8:1 MUX and decoders on paper | GO Classes DL practice / backup: Neso Academy | `dl-06` worked examples |
| Sat | 09:00–11:00 | Timed test: ~25 odd-year PYQs DL-5, DL-6 | GO PYQs (odd years) | Topic test T20 |
| Sat | 11:00–12:00 | GA rotation 2 — Grammar | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis, revise week notes | — | Error log |
| Sun | — | Weekly review #20 **+ Monthly review (January 2027)** | — | `reviews/weekly/2027-01-25-to-2027-01-31.md` + `reviews/monthly/2027-01.md` |

---

### Week 21 — Digital Logic: Sequential Circuits (2027-02-01 → 2027-02-07)
**Hours: 19** | **Topics: DL-7** | **GA rotation 3: Data interpretation**

**If you registered for GATE 2027 as a practice attempt:** your paper may fall on 6/7 Feb (this weekend), 13/14 Feb (Week 22) or 20/21 Feb (Week 23, first week of Phase 3). The exam replaces that weekend's test block. Record it in `trackers/mocks.md` as "GATE 2027 (real exam, diagnostic)". Friday PM that week becomes a light GA + calculator warm-up, not a lecture.

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DL-5, DL-6 | GO PYQs | Error log |
| Mon | PM | Lecture: latches — SR latch, gated latches; flip-flops SR, D, JK, T; characteristic tables + equations | GO Classes Digital Logic | `notes/digital-logic/dl-07-flip-flops.md` |
| Tue | AM | PYQs: flip-flop behaviour | GO tag flip-flop | Daily log + error log |
| Tue | PM | Lecture: excitation tables, flip-flop conversions, race-around condition, master–slave, edge triggering | GO Classes Digital Logic | `dl-07` |
| Wed | AM | PYQs: conversions, output waveforms | GO tag flip-flop | Daily log + error log |
| Wed | PM | Lecture: timing — setup / hold time, propagation delay, maximum clock frequency | GO Classes Digital Logic | `dl-07` |
| Thu | AM | PYQs: max clock frequency (NAT) | GO tag sequential-circuit | Daily log + error log |
| Thu | PM | Lecture: sequential circuit analysis — state tables, state diagrams from a given circuit | GO Classes Digital Logic | `dl-07` (complete) |
| Fri | AM | PYQs: analyse the circuit — output sequence | GO tag sequential-circuit | Daily log + error log |
| Fri | PM | Flip-flop tables into the formula sheet; worked circuit analysis on paper | Own notes / backup: Neso Academy | `notes/formula-sheets/digital-logic.md` |
| Sat | 09:00–11:00 | Timed test: ~20 odd-year PYQs DL-7 + 5 DL carry-over *(or GATE 2027 exam)* | GO PYQs (odd years) | Topic test T21 |
| Sat | 11:00–12:00 | GA rotation 3 — Data interpretation | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + 15-min **R2 revision: Engineering Maths formula sheet** | Own notes | `trackers/revision.md` |
| Sun | — | Weekly review #21 | — | `reviews/weekly/2027-02-01-to-2027-02-07.md` |

---

### Week 22 — Digital Logic: Counters, Registers, FSMs + Phase 2 Wrap (2027-02-08 → 2027-02-14)
**Hours: 19** | **Topics: DL-8** | **GA rotation 4: Logic + reasoning**

| Day | Slot | Focus | Resource | Output |
|-----|------|-------|----------|--------|
| Mon | AM | Redo Sat errors; remaining even-year PYQs DL-7 | GO PYQs | Error log |
| Mon | PM | Lecture: asynchronous (ripple) counters, synchronous counters, mod-N design | GO Classes Digital Logic | `notes/digital-logic/dl-08-counters-fsm.md` |
| Tue | AM | PYQs: counter sequence / modulus (NAT) | GO tag counter | Daily log + error log |
| Tue | PM | Lecture: ring counter, Johnson counter, shift registers (SISO / SIPO / PISO / PIPO) | GO Classes Digital Logic | `dl-08` |
| Wed | AM | PYQs: ring / Johnson / shift register states | GO tag counter | Daily log + error log |
| Wed | PM | Lecture: FSM design — Mealy vs Moore, sequence detectors, state minimisation | GO Classes Digital Logic | `dl-08` (complete) |
| Thu | AM | PYQs: FSM / sequence detector | GO tag finite-state-machine | Daily log + error log |
| Thu | PM | **Finish `notes/formula-sheets/digital-logic.md`** (counters section) + R1 revision of all DL notes | Own notes | Formula sheet (complete) |
| Fri | AM | Mixed DL PYQs: all remaining even-year questions | GO PYQs | Daily log + error log |
| Fri | PM | Phase 2 audit: fill confidence for AL / LA / CA / PS / DL rows in `subjects.md`; list the 5 weakest topics | `trackers/subjects.md` | Audit notes in daily log |
| Sat | 09:00–11:00 | **Digital Logic subject test:** ~30 odd-year PYQs DL-1 … DL-8 *(or GATE 2027 exam)* | GO PYQs (odd years) | Topic test T22 |
| Sat | 11:00–12:00 | GA rotation 4 — Logic + reasoning | GO PDF Vol 1 GA | `trackers/aptitude.md` |
| Sat | 12:00–13:00 | Error analysis + walk the **Phase 2 exit checklist** below | — | Exit checklist answers |
| Sun | — | Weekly review #22 + **Phase 2 retrospective** | — | `reviews/weekly/2027-02-08-to-2027-02-14.md` |

**Resources:**
- GO Classes Digital Logic — https://www.youtube.com/playlist?list=PLIPZ2_p3RNHiwFGR4fqKlj9C_eo8R6hbY
- Backup: Neso Academy — https://www.youtube.com/channel/UCQYMhOMi_Cdj1CEAU-fv80A
- Reference: Morris Mano — Digital Design

---

## Daily Quota Cheat Sheet

| Slot | PYQ target | Lecture time |
|------|------------|--------------|
| Mon–Fri AM | 12–15 PYQs + redos (maths weeks: fewer PYQs exist — top up per the Split Rule) | — |
| Mon–Fri PM | 0 | 60–70 min lecture + 20 min notes |
| Sat 09:00–11:00 | 20–30 odd-year PYQs, timed, virtual calculator | — |
| Sat 11:00–12:00 | 20–25 GA questions | — |

---

## Phase-2 Exit Criteria

Before moving to Phase 3 (Mon 2027-02-15), confirm:

- [ ] AL / LA / CA / PS / DL rows at confidence ≥3 in `trackers/subjects.md`
- [ ] PYQ accuracy ≥60% in Algorithms, Engineering Maths (LA + Calc + Prob combined), Digital Logic
- [ ] Can solve any recurrence in the master-theorem family and state the complexity of every standard algorithm without notes
- [ ] Can compute eigenvalues of structured matrices and do Bayes problems in <3 min
- [ ] Can convert IEEE 754 hex ↔ decimal and minimise a 4-variable K-map in <3 min
- [ ] Formula sheets complete: algorithms, engineering-maths, digital-logic
- [ ] Phase 1 subjects revised (R2 logged for C, DS, DM)
- [ ] Adherence ≥70%

If any of these are "no", **extend Phase 2 by 1 week** (the extension comes out of Phase 5). COA assumes Digital Logic is solid.
